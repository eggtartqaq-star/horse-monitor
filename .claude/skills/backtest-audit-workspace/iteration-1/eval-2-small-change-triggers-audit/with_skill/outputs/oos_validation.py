# -*- coding: utf-8 -*-
"""
============================================================
OOS 樣本外驗證(畢業試)  —— 加入固定止盈版本
============================================================
⽬的:
  驗證V6.4系統嘅優勢係「真實」定係「背數據」(過度擬合)
⽅法:
  將約4年數據分成兩段,⽤完全相同嘅規則分開跑:
    樣本內(In-Sample):  頭段 —— 模型設計時「⾒過」嘅市況
    樣本外(OOS):        尾段(近18個⽉) —— 模型「未⾒過」嘅市況
判定標準(業界慣例):
  健康:   OOS嘅EV仍為正,且唔低過樣本內EV嘅50%
  警戒:   OOS EV跌超過50%但仍為正 → 優勢存在但脆弱
  不合格: OOS EV轉負 → 過度擬合,唔可以⽤真錢
測試對象:
  引擎⼀(均值回歸,C臂⽌蝕,10⽇持倉) —— 主⼒
  引擎⼆(趨勢跟蹤,3×ATR移動⽌損)    —— 副引擎
使⽤⽅法:
  python oos_validation.py
  (需時約15-20分鐘,下載4年數據)
============================================================
本次改動(2026-08-03)
------------------------------------------------------------
[1] 新增固定 TAKE_PROFIT_PCT = 2.0 止盈,兩個引擎都有。
    - 同一條 bar 內止蝕同止盈都掂到 → 一律當止蝕先成交(對自己不利嗰邊)。
    - 止盈近過結構性目標,所以擺喺結構目標之前檢查。
    - 跳空高開過止盈價時,仍然只計 +2.0%(保守,唔賺跳空)。

[2] ★ 唔係直接覆蓋你原本嘅數字 —— 而係「原版 vs 加止盈」並排跑。
    加一個出場條件而唔對照,你只會見到一堆新數字,分唔清係好咗定衰咗。
    輸出會有四組:引擎一/引擎二 × 原版/加止盈,每組再分 IS / OOS。

[3] 新增 exit_reason 分佈(STOP / TP / TARGET / TIME),
    直接睇到 2% 止盈截咗幾多筆本來會行到結構目標嘅交易。

[4] 新增淨EV(扣成本)一行。2% 止盈嘅毛利喺你戶口規模下係 US$2.56,
    而來回成本 US$0.70–4.32 —— 呢個對照唔擺出嚟,個 EV 係讀唔到意思嘅。
    成本模型由 strategy/v6.5/risk_config.py 抄過嚟(數字係假設,要換自己嘅)。

[5] 修復:原檔第 64/68/74/75/77/206/208/259/368 行喺 81 字元位置被截斷,
    第 304/307/311 行嘅字串被換行斷開 —— 呢個檔案喺 repo 入面根本
    import 唔到(SyntaxError)。已按原意接返。詳見交付報告。

[6] 冇改:MR_SCORE_MIN / MIN_R / ATR_STOP_MULT / TREND_SCORE_MIN /
    ATR_TRAIL_MULT / 持倉上限 —— 一個門檻都冇郁。
============================================================
"""
import yfinance as yf
import pandas as pd
import numpy as np
import ta
import time
import warnings
warnings.filterwarnings("ignore")
TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO",
    "AMD", "QCOM", "MU", "INTC",
    "JPM", "BAC", "GS", "V", "MA",
    "COST", "WMT", "MCD", "NKE", "SBUX",
    "UNH", "JNJ", "PFE", "LLY",
    "XOM", "CVX", "CAT", "BA",
    "PLTR", "CRM", "ADBE", "NFLX", "SHOP", "UBER", "COIN", "MSTR"

]
# ---- 分段設定 ----
DATA_PERIOD   = "4y"           # 下載4年
OOS_MONTHS    = 18             # 最後18個⽉做樣本外
# ---- 引擎⼀參數(同V6.4⼀致,不得改動) ----
MR_SCORE_MIN  = 0.55
MIN_R         = 2.0
MR_MAX_HOLD   = 10
ATR_STOP_MULT = 2.0            # C臂
COOLDOWN      = 10
# ---- 引擎⼆參數(同V6.4⼀致) ----
TREND_SCORE_MIN = 0.65
ATR_TRAIL_MULT  = 3.0
TREND_MAX_HOLD  = 60

# ============================================================
# ★ 新增:固定止盈
# ============================================================
# 你要求嘅 2% 固定止盈。設 None 就完全還原成 V6.4 原版行為。
TAKE_PROFIT_PCT = 2.0

# 並排對照:每個引擎都會用呢兩個設定各跑一次。
# 唔好淨係睇「加止盈」嗰欄 —— 要睇兩欄之間嘅差。
VARIANTS = [
    ("V6.4 原版(無止盈)", None),
    (f"加 {TAKE_PROFIT_PCT:.1f}% 止盈", TAKE_PROFIT_PCT),
]

# ============================================================
# 成本模型(抄自 strategy/v6.5/risk_config.py)
# ★ 呢啲佣金數字係說明性假設,唔係查證過嘅收費表。用之前換成你自己嘅。
# ============================================================
ACCOUNT_HKD = 10_000.0
USD_HKD     = 7.8
ACCOUNT_USD = ACCOUNT_HKD / USD_HKD
MAX_POS_NOTIONAL_PCT = 10.0
NOTIONAL_USD = ACCOUNT_USD * MAX_POS_NOTIONAL_PCT / 100.0   # ≈ US$128.21

# name: (min_commission, per_share, pct_of_notional, half_spread_bp, slippage_bp)
BROKERS = {
    "free(V6.4隱含假設)": (0.00, 0.0000, 0.0, 0.0, 0.0),
    "ibkr_tiered":        (0.35, 0.0035, 0.0, 2.5, 7.0),
    "ibkr_fixed":         (1.00, 0.0050, 0.0, 2.5, 7.0),
    "hk_retail":          (2.00, 0.0000, 0.0, 2.5, 10.0),
}


def round_trip_cost_pct(broker_key, notional=NOTIONAL_USD, share_price=100.0):
    """來回成本,用「佔名義金額嘅百分比」表示,方便直接減落 EV%。"""
    mn, ps, pct, hs_bp, slip_bp = BROKERS[broker_key]
    shares = max(1, int(notional // share_price))
    one_side = (max(mn, ps * shares, pct / 100.0 * notional)
                + (hs_bp + slip_bp) / 10000.0 * notional)
    return one_side * 2 / notional * 100.0


# ============================================================
# 指標(同V6.4完全⼀致)
# ============================================================
def calc_indicators(df):
    df = df.copy()
    df["MA20"]  = df["Close"].rolling(20).mean()
    df["MA50"]  = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["RSI14"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()
    df["RSI2"]  = ta.momentum.RSIIndicator(df["Close"], window=2).rsi()
    adx_ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14)
    df["ADX"] = adx_ind.adx()
    df["DI_PLUS"]  = adx_ind.adx_pos()
    df["DI_MINUS"] = adx_ind.adx_neg()
    atr = ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"],
                                         window=14)
    df["ATR"] = atr.average_true_range()
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"]  = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"]  = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = (df["Volume"].rolling(5).mean()
                       / df["Volume"].rolling(20).mean())
    obv = ta.volume.OnBalanceVolumeIndicator(df["Close"],
                                             df["Volume"]).on_balance_volume()
    df["OBV"] = obv
    df["OBV_Div"] = ((df["Close"] < df["Close"].shift(5))
                     & (df["OBV"] > df["OBV"].shift(5)))
    df["low_10d"]   = df["Low"].rolling(10).min()
    df["high_20d"]  = df["High"].rolling(20).max()
    df["high_60d"]  = df["High"].rolling(60).max()
    df["dist_60h"]  = (df["high_60d"] - df["Close"]) / df["Close"] * 100
    return df

def mr_score(row):
    score = 0.0
    rsi14 = row["RSI14"]
    if pd.notna(rsi14):
        if 35 <= rsi14 <= 45:   rs = 1.0
        elif 45 < rsi14 <= 55:  rs = 0.8
        elif 30 <= rsi14 < 35:  rs = 0.6
        elif 55 < rsi14 <= 65:  rs = 0.4
        elif rsi14 > 65:        rs = 0.1
        else:                    rs = 0.3
        score += rs * 0.20
    rsi2 = row["RSI2"]
    if pd.notna(rsi2):
        if rsi2 < 5:    r2 = 1.0
        elif rsi2 < 10: r2 = 0.85
        elif rsi2 < 20: r2 = 0.70
        elif rsi2 < 30: r2 = 0.50
        else:           r2 = 0.20
        score += r2 * 0.15
    pma20 = row["price_vs_ma20"]; ma_t = row["ma20_vs_ma50"]
    if pd.notna(pma20) and pd.notna(ma_t):
        if -5 <= pma20 <= 0 and ma_t > 0:    ss = 1.0
        elif -10 <= pma20 < -5 and ma_t > 0: ss = 0.8
        elif 0 < pma20 <= 3 and ma_t > 0:    ss = 0.7
        elif pma20 < -10 and ma_t > 0:        ss = 0.4
        else:                                  ss = 0.2
        score += ss * 0.20
    ret10 = row["ret_10d"]
    if pd.notna(ret10):
        if -15 <= ret10 <= -5:    r3 = 1.0
        elif -20 <= ret10 < -15:  r3 = 0.7
        elif -5 < ret10 <= -2:    r3 = 0.5
        elif ret10 > 0:           r3 = 0.1
        else:                     r3 = 0.3
        score += r3 * 0.20
    vr = row["vol_ratio"]; ret5 = row["ret_5d"]
    if pd.notna(vr) and pd.notna(ret5):
        if ret5 < 0 and vr > 1.3:    vs = 1.0
        elif ret5 < 0 and vr > 1.1:  vs = 0.8
        elif ret5 < 0 and vr > 0.9:  vs = 0.5
        elif ret5 >= 0 and vr > 1.2: vs = 0.6
        else:                         vs = 0.2
        score += vs * 0.15
    if row.get("OBV_Div", False):
        score += 0.10
    return round(min(score, 1.0), 4)

def trend_score_calc(row):
    score = 0.0
    adx = row["ADX"]
    ts = 0.0
    if pd.notna(adx):
        if adx >= 40:   ts = 1.0
        elif adx >= 30: ts = 0.85
        elif adx >= 25: ts = 0.6
    score += ts * 0.25
    ma = 0.3
    c, m20, m50, m200 = row["Close"], row["MA20"], row["MA50"], row["MA200"]
    if pd.notna(m20) and pd.notna(m50):
        if pd.notna(m200) and c > m20 > m50 > m200:
            ma = 1.0
        elif c > m20 > m50:
            ma = 0.8
        elif c > m20:
            ma = 0.5
        else:
            ma = 0.1
    score += ma * 0.25
    ph = 0.0
    d = row["dist_60h"]
    if pd.notna(d):
        if d <= 1:    ph = 1.0
        elif d <= 3:  ph = 0.85
        elif d <= 5:  ph = 0.6
        elif d <= 10: ph = 0.35
        else:         ph = 0.1
    score += ph * 0.25
    vs = 0.4
    vr = row["vol_ratio"]
    if pd.notna(vr):
        vs = 1.0 if vr > 1.2 else (0.7 if vr > 1.0 else 0.4)
    score += vs * 0.15
    if pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]:
        score += 0.10
    return round(min(score, 1.0), 4)
# ============================================================
# 引擎⼀模擬(C臂⽌蝕,同三臂測試邏輯⼀致)
# ============================================================
def simulate_mr(df, i, entry, stop, target, take_profit=None):
    """
    take_profit = None  → V6.4 原版行為(只有止蝕 / 結構目標 / 10日到期)
    take_profit = 價位  → 多一個固定止盈出場

    同一條 bar 內嘅先後次序(★ 全部向不利自己嗰邊解讀):
      1. 止蝕  —— 就算同一條 bar 都掂到止盈,都當止蝕先中
      2. 止盈  —— 2% 近過結構目標,所以擺喺結構目標之前
      3. 結構目標(MA50 / 60日高)
      4. 第10日收市平倉
    """
    n = len(df)

    for d in range(1, MR_MAX_HOLD + 1):
        j = i + d
        if j >= n:
            return None
        r = df.iloc[j]
        if r["Low"] <= stop:
            return (stop - entry) / entry * 100, d, "STOP"
        if take_profit is not None and r["High"] >= take_profit:
            # 跳空高開過止盈價時仍然只計止盈價,唔賺跳空(保守)
            return (take_profit - entry) / entry * 100, d, "TP"
        if r["High"] >= target:
            return (target - entry) / entry * 100, d, "TARGET"
        if d == MR_MAX_HOLD:
            return (r["Close"] - entry) / entry * 100, d, "TIME"
    return None
def run_engine1(df, bull_series, start_idx, end_idx, take_profit_pct=None):
    """喺指定index範圍內跑引擎⼀,回傳交易list"""
    trades = []
    i = start_idx
    while i < end_idx - 2:
        row = df.iloc[i]
        ok = bool(bull_series.iloc[i]) if i < len(bull_series) else False
        if (ok and pd.notna(row["ADX"]) and row["ADX"] < 25):
            sc = mr_score(row)
            if sc >= MR_SCORE_MIN:
                close = row["Close"]; atr = row["ATR"]
                if pd.notna(atr) and atr > 0 and pd.notna(row["low_10d"]):
                    stop_struct = row["low_10d"] * 0.995
                    stop_atr = close - ATR_STOP_MULT * atr
                    stop = min(stop_struct, stop_atr)
                    risk = close - stop
                    if risk > 0:
                        targets = []
                        if pd.notna(row["MA50"]) and row["MA50"] > close:
                            targets.append((row["MA50"],
                                            (row["MA50"] - close) / risk))
                        if pd.notna(row["high_60d"]) and row["high_60d"] > close:
                            targets.append((row["high_60d"],
                                            (row["high_60d"] - close) / risk))
                        valid = [(p, r) for p, r in targets if r >= MIN_R]
                        if valid:
                            target = min(valid, key=lambda x: x[0])[0]
                            # ★ 固定止盈價位
                            tp_price = (close * (1 + take_profit_pct / 100.0)
                                        if take_profit_pct is not None else None)
                            res = simulate_mr(df, i, close, stop, target, tp_price)
                            if res:
                                trades.append({"ret": res[0], "days": res[1],
                                               "exit": res[2],
                                               "stop_pct": risk / close * 100})
                                i += max(res[1], 1)
        i += 1
    return trades

# ============================================================
# 引擎⼆模擬(3×ATR移動⽌損,先檢查後更新+跳空保護)
# ============================================================
def run_engine2(df, bull_series, start_idx, end_idx, take_profit_pct=None):
    trades = []
    i = max(start_idx, 80)
    while i < end_idx - 2:
        row = df.iloc[i]
        ok = (bool(bull_series.iloc[i]) if i < len(bull_series) else False)
        ok = (ok and pd.notna(row["ADX"]) and row["ADX"] >= 25
              and pd.notna(row["DI_PLUS"]) and pd.notna(row["DI_MINUS"])
              and row["DI_PLUS"] > row["DI_MINUS"]
              and pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"])
        if ok:
            sc = trend_score_calc(row)
            atr0 = row["ATR"]
            if sc >= TREND_SCORE_MIN and pd.notna(atr0) and atr0 > 0:
                entry = row["Close"]
                trail = entry - ATR_TRAIL_MULT * atr0
                risk_pct = (entry - trail) / entry * 100
                # ★ 固定止盈價位
                tp_price = (entry * (1 + take_profit_pct / 100.0)
                            if take_profit_pct is not None else None)
                if risk_pct <= 12:
                    highest = entry
                    current_atr = atr0
                    exit_ret, exit_day, exit_why = None, None, None
                    for d in range(1, TREND_MAX_HOLD + 1):
                        j = i + d
                        if j >= end_idx:
                            break  # OOS邊界:未平倉交易棄掉,唔跨段
                        r2 = df.iloc[j]
                        # 1. 移動止損先檢查(保留原本嘅跳空保護)
                        if r2["Low"] <= trail:
                            if pd.notna(r2["Open"]) and r2["Open"] < trail:
                                exit_price = r2["Open"]
                            else:
                                exit_price = trail
                            exit_ret = (exit_price - entry) / entry * 100
                            exit_day = d
                            exit_why = "TRAIL"
                            break
                        # 2. ★ 新增:固定止盈(同一條bar止損優先,已喺上面處理)
                        if tp_price is not None and r2["High"] >= tp_price:
                            exit_ret = take_profit_pct
                            exit_day = d
                            exit_why = "TP"
                            break
                        if pd.notna(r2["ATR"]):
                            current_atr = r2["ATR"]
                        highest = max(highest, r2["High"])
                        trail = max(trail,
                                    highest - ATR_TRAIL_MULT * current_atr)
                        if d == TREND_MAX_HOLD:
                            exit_ret = (r2["Close"] - entry) / entry * 100
                            exit_day = d
                            exit_why = "TIME"
                    if exit_ret is not None:
                        trades.append({"ret": exit_ret, "days": exit_day,
                                       "exit": exit_why, "stop_pct": risk_pct})
                        i += max(exit_day, 1)

        i += 1
    return trades
# ============================================================
# 統計
# ============================================================
def stats(trades):
    if not trades:
        return None
    d = pd.DataFrame(trades)
    wins = d[d["ret"] > 0]; losses = d[d["ret"] <= 0]
    return {
        "n": len(d),
        "win": len(wins) / len(d) * 100,
        "avg_win": wins["ret"].mean() if len(wins) else 0,
        "avg_loss": losses["ret"].mean() if len(losses) else 0,
        "ev": d["ret"].mean(),
        "days": d["days"].mean(),
        "worst": d["ret"].min(),
        # ★ 新增:出場原因分佈 + 平均止蝕闊度(拎嚟計打和勝率)
        "exits": d["exit"].value_counts().to_dict() if "exit" in d else {},
        "avg_stop_pct": (d["stop_pct"].mean() if "stop_pct" in d
                         else float("nan")),
    }
def show(s, title):
    if s is None:
        print(f"\n【{title}】無交易樣本")
        return
    print(f"\n【{title}】")
    print(f"  筆數:{s['n']}  勝率:{s['win']:.1f}%  EV:{s['ev']:+.3f}%")
    print(f"  平均贏:+{s['avg_win']:.2f}%  平均輸:{s['avg_loss']:.2f}%")
    print(f"  平均持倉:{s['days']:.1f}天  最差單筆:{s['worst']:.1f}%")
    if s["exits"]:
        parts = "  ".join(f"{k}:{v}" for k, v in sorted(s["exits"].items()))
        print(f"  出場原因:{parts}")
    if s["avg_stop_pct"] == s["avg_stop_pct"]:   # 唔係 NaN
        print(f"  平均止蝕闊度:{s['avg_stop_pct']:.2f}%")
    # ★ 淨EV —— 上面個 EV 一蚊成本都冇扣。呢幾行先係戶口真正見到嘅嘢。
    print(f"  淨EV(US${NOTIONAL_USD:.2f} 倉位,US$100 股價,說明性假設):")
    for bk in BROKERS:
        c = round_trip_cost_pct(bk)
        print(f"    {bk:22} 成本 {c:5.2f}%  →  淨EV {s['ev'] - c:+.3f}%")
def breakeven_note(s, tp_pct):
    """止盈定死之後,盈虧比就係固定嘅 —— 直接計要幾高勝率先打和。"""
    if s is None or s["avg_stop_pct"] != s["avg_stop_pct"]:
        return
    stop = s["avg_stop_pct"]
    if stop <= 0:
        return
    be = stop / (stop + tp_pct) * 100
    print(f"  ★ 止盈 +{tp_pct:.1f}% vs 平均止蝕 -{stop:.2f}% "
          f"→ 毛打和勝率要 {be:.1f}%(實際勝率 {s['win']:.1f}%)")
def verdict(is_stats, oos_stats, engine_name):
    print(f"\n{'='*64}")
    print(f"{engine_name} OOS判定")
    print("="*64)
    if is_stats is None or oos_stats is None:
        print("  樣本不⾜,無法判定")
        return
    is_ev, oos_ev = is_stats["ev"], oos_stats["ev"]
    print(f"  樣本內EV: {is_ev:+.3f}%   樣本外EV: {oos_ev:+.3f}%")
    if oos_ev <= 0:
        print("  [不合格] 樣本外EV轉負 → 過度擬合,此引擎唔可以⽤真錢")
    elif is_ev > 0 and oos_ev >= is_ev * 0.5:
        print("  [健康] 樣本外優勢保持(冇跌超過50%) → 優勢係真實嘅")
    elif oos_ev > 0:
        print("  [警戒] 樣本外EV為正但衰減超過50% → 優勢存在但脆弱,")
        print("     模擬交易階段要密切觀察實際表現")
    if oos_stats["n"] < 30:
        print(f"  (注意:樣本外只有{oos_stats['n']}筆,統計說服⼒有限)")
def compare(base_is, base_oos, tp_is, tp_oos, engine_name):
    """★ 加止盈之前 / 之後 並排。淨係睇一欄係睇唔出好定衰嘅。"""
    print(f"\n{'='*64}")
    print(f"{engine_name} —— 原版 vs 加 {TAKE_PROFIT_PCT:.1f}% 止盈")
    print("="*64)
    print(f"  {'':14}{'原版IS':>11}{'止盈IS':>11}{'原版OOS':>12}{'止盈OOS':>12}")
    def g(s, k):
        return float("nan") if s is None else s[k]
    for label, key, fmt in [("筆數", "n", "{:>11.0f}"),
                            ("勝率%", "win", "{:>11.1f}"),
                            ("EV%", "ev", "{:>11.3f}"),
                            ("平均贏%", "avg_win", "{:>11.2f}"),
                            ("平均輸%", "avg_loss", "{:>11.2f}"),
                            ("最差單筆%", "worst", "{:>11.1f}"),
                            ("平均持倉日", "days", "{:>11.1f}")]:
        row = f"  {label:14}"
        for s in (base_is, tp_is, base_oos, tp_oos):
            v = g(s, key)
            row += fmt.format(v) if v == v else f"{'—':>11}"
        print(row)
    for tag, s in (("原版OOS", base_oos), ("止盈OOS", tp_oos)):
        if s and s["exits"]:
            print(f"  {tag} 出場分佈:" +
                  "  ".join(f"{k}:{v}" for k, v in sorted(s["exits"].items())))
    breakeven_note(tp_oos, TAKE_PROFIT_PCT)
# ============================================================
# 主程式
# ============================================================
def main():
    print("=" * 64)
    print("OOS 樣本外驗證 —— V6.4系統畢業試(原版 vs 加止盈 對照)")
    print(f"數據:{DATA_PERIOD}  |  樣本外 = 最後{OOS_MONTHS}個⽉")
    print(f"止盈:{TAKE_PROFIT_PCT:.1f}%(同一條bar止蝕優先)")
    print("=" * 64)
    print("\n下載SPY環境數據...")
    spy = yf.Ticker("SPY").history(period=DATA_PERIOD)
    spy["MA200"] = spy["Close"].rolling(200).mean()
    spy_bull_raw = (spy["Close"] > spy["MA200"])
    # 分段⽇期
    cutoff = spy.index[-1] - pd.DateOffset(months=OOS_MONTHS)
    print(f"樣本內: 開始 ~ {cutoff.strftime('%Y-%m-%d')}")
    print(f"樣本外: {cutoff.strftime('%Y-%m-%d')} ~ 最新\n")
    # buckets[(engine, variant_name, sample)] = [trades]
    buckets = {(e, v, s): []
               for e in (1, 2)
               for v, _ in VARIANTS
               for s in ("IS", "OOS")}
    for t_i, tk in enumerate(TICKERS):
        print(f"[{t_i+1}/{len(TICKERS)}] {tk}...")
        try:
            df = yf.Ticker(tk).history(period=DATA_PERIOD)
            if df.empty or len(df) < 300:
                continue
            df = calc_indicators(df)
            bull = spy_bull_raw.reindex(df.index, method="ffill").fillna(False)
            # 搵cutoff對應嘅index位置
            cut_idx = df.index.searchsorted(cutoff)
            # 樣本內: 60 → cut_idx;  樣本外: cut_idx → 尾
            for vname, tp in VARIANTS:
                buckets[(1, vname, "IS")]  += run_engine1(df, bull, 60,
                                                          cut_idx, tp)
                buckets[(1, vname, "OOS")] += run_engine1(df, bull, cut_idx,
                                                          len(df), tp)
                buckets[(2, vname, "IS")]  += run_engine2(df, bull, 80,
                                                          cut_idx, tp)
                buckets[(2, vname, "OOS")] += run_engine2(df, bull, cut_idx,
                                                          len(df), tp)
        except Exception as e:
            print(f"  {tk} 錯誤: {e}")
            continue
        time.sleep(0.2)

    print("\n" + "=" * 64)
    print("結果")
    print("=" * 64)
    names = {1: "引擎⼀(均值回歸)", 2: "引擎⼆(趨勢)"}
    S = {k: stats(v) for k, v in buckets.items()}
    for eng in (1, 2):
        for vname, _ in VARIANTS:
            show(S[(eng, vname, "IS")],  f"{names[eng]} {vname} 樣本內")
            show(S[(eng, vname, "OOS")], f"{names[eng]} {vname} 樣本外OOS")
            verdict(S[(eng, vname, "IS")], S[(eng, vname, "OOS")],
                    f"{names[eng]} {vname}")
        compare(S[(eng, VARIANTS[0][0], "IS")], S[(eng, VARIANTS[0][0], "OOS")],
                S[(eng, VARIANTS[1][0], "IS")], S[(eng, VARIANTS[1][0], "OOS")],
                names[eng])
    # 儲存
    for (eng, vname, sample), data in buckets.items():
        if data:
            tag = "base" if vname == VARIANTS[0][0] else "tp"
            fn = f"oos_e{eng}_{tag}_{sample.lower()}.csv"
            pd.DataFrame(data).to_csv(fn, index=False, encoding="utf-8-sig")
    print("\n明細已儲存: oos_e{1,2}_{base,tp}_{is,oos}.csv")
    print("\n提醒: 呢個測試本來冇任何參數可以調 —— 規則鎖死同V6.4⼀致。")
    print("      如果OOS唔合格,正確反應係承認過度擬合,唔係調參數令佢過關。")
    print("      ★ 你今次加咗一個止盈參數落嚟。所以上面一定要睇「原版 vs 止盈」")
    print("        個對照表,同埋記住:呢個 OOS 由今次開始已經唔再係乾淨樣本外。")
if __name__ == "__main__":
    main()
