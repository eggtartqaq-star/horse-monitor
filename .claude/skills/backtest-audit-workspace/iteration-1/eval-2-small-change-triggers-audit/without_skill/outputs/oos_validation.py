# -*- coding: utf-8 -*-
"""
============================================================
OOS 樣本外驗證(畢業試)
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
# ---- 新增:固定2%獲利了結(兩個引擎共用) ----
TAKE_PROFIT_PCT = 2.0          # % —— 設 None 即關閉此出場條件
# ---- 引擎⼆參數(同V6.4⼀致) ----
TREND_SCORE_MIN = 0.65
ATR_TRAIL_MULT  = 3.0
TREND_MAX_HOLD  = 60
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
    adx_ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14
    df["ADX"] = adx_ind.adx()
    df["DI_PLUS"]  = adx_ind.adx_pos()
    df["DI_MINUS"] = adx_ind.adx_neg()
    atr = ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"], wind
    df["ATR"] = atr.average_true_range()
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"]  = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"]  = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).m
    obv = ta.volume.OnBalanceVolumeIndicator(df["Close"], df["Volume"]).on_balanc
    df["OBV"] = obv
    df["OBV_Div"] = (df["Close"] < df["Close"].shift(5)) & (df["OBV"] > df["OBV"]
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
def simulate_mr(df, i, entry, stop, target):
    n = len(df)
    tp = entry * (1 + TAKE_PROFIT_PCT / 100) if TAKE_PROFIT_PCT else None
    for d in range(1, MR_MAX_HOLD + 1):
        j = i + d
        if j >= n:
            return None
        r = df.iloc[j]
        # 同一支K棒內無法知道先觸止蝕定先觸獲利,保守起見先判止蝕
        if r["Low"] <= stop:
            return (stop - entry) / entry * 100, d
        if tp is not None and r["High"] >= tp:
            # 跳空高開:成交價用開市價,唔會好過實際
            if pd.notna(r["Open"]) and r["Open"] > tp:
                exit_price = r["Open"]
            else:
                exit_price = tp
            return (exit_price - entry) / entry * 100, d
        if r["High"] >= target:
            return (target - entry) / entry * 100, d
        if d == MR_MAX_HOLD:
            return (r["Close"] - entry) / entry * 100, d
    return None
def run_engine1(df, bull_series, start_idx, end_idx):
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
                            targets.append((row["MA50"], (row["MA50"] - close) / 
                        if pd.notna(row["high_60d"]) and row["high_60d"] > close:
                            targets.append((row["high_60d"], (row["high_60d"] - c
                        valid = [(p, r) for p, r in targets if r >= MIN_R]
                        if valid:
                            target = min(valid, key=lambda x: x[0])[0]
                            res = simulate_mr(df, i, close, stop, target)
                            if res:
                                trades.append({"ret": res[0], "days": res[1]})
                                i += max(res[1], 1)
        i += 1
    return trades

# ============================================================
# 引擎⼆模擬(3×ATR移動⽌損,先檢查後更新+跳空保護)
# ============================================================
def run_engine2(df, bull_series, start_idx, end_idx):
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
                if risk_pct <= 12:
                    highest = entry
                    current_atr = atr0
                    tp = entry * (1 + TAKE_PROFIT_PCT / 100) if TAKE_PROFIT_PCT else None
                    exit_ret, exit_day = None, None
                    for d in range(1, TREND_MAX_HOLD + 1):
                        j = i + d
                        if j >= end_idx:
                            break  # OOS邊界:未平倉交易棄掉,唔跨段
                        r2 = df.iloc[j]
                        if r2["Low"] <= trail:
                            if pd.notna(r2["Open"]) and r2["Open"] < trail:
                                exit_price = r2["Open"]
                            else:
                                exit_price = trail
                            exit_ret = (exit_price - entry) / entry * 100
                            exit_day = d
                            break
                        if tp is not None and r2["High"] >= tp:
                            if pd.notna(r2["Open"]) and r2["Open"] > tp:
                                exit_price = r2["Open"]
                            else:
                                exit_price = tp
                            exit_ret = (exit_price - entry) / entry * 100
                            exit_day = d
                            break
                        if pd.notna(r2["ATR"]):
                            current_atr = r2["ATR"]
                        highest = max(highest, r2["High"])
                        trail = max(trail, highest - ATR_TRAIL_MULT * current_atr
                        if d == TREND_MAX_HOLD:
                            exit_ret = (r2["Close"] - entry) / entry * 100
                            exit_day = d
                    if exit_ret is not None:
                        trades.append({"ret": exit_ret, "days": exit_day})
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
    }
def show(s, title):
    if s is None:
        print(f"\n【{title}】無交易樣本")
        return
    print(f"\n【{title}】")
    print(f"  筆數:{s['n']}  勝率:{s['win']:.1f}%  EV:{s['ev']:+.3f}%")
    print(f"  平均贏:+{s['avg_win']:.2f}%  平均輸:{s['avg_loss']:.2f}%")
    print(f"  平均持倉:{s['days']:.1f}天  最差單筆:{s['worst']:.1f}%")
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
        print("  
 不合格:樣本外EV轉負 → 過度擬合,此引擎唔可以⽤真錢")
    elif is_ev > 0 and oos_ev >= is_ev * 0.5:
        print("  
 健康:樣本外優勢保持(冇跌超過50%) → 優勢係真實嘅")
    elif oos_ev > 0:

        print("  
 警戒:樣本外EV為正但衰減超過50% → 優勢存在但脆弱,")
        print("     模擬交易階段要密切觀察實際表現")
    if oos_stats["n"] < 30:
        print(f"  (注意:樣本外只有{oos_stats['n']}筆,統計說服⼒有限)")
# ============================================================
# 主程式
# ============================================================
def main():
    print("=" * 64)
    print("OOS 樣本外驗證 —— V6.4系統畢業試")
    print(f"數據:{DATA_PERIOD}  |  樣本外 = 最後{OOS_MONTHS}個⽉")
    print(f"獲利了結:{'關閉' if not TAKE_PROFIT_PCT else f'+{TAKE_PROFIT_PCT}%'}")
    print("=" * 64)
    print("\n下載SPY環境數據...")
    spy = yf.Ticker("SPY").history(period=DATA_PERIOD)
    spy["MA200"] = spy["Close"].rolling(200).mean()
    spy_bull_raw = (spy["Close"] > spy["MA200"])
    # 分段⽇期
    cutoff = spy.index[-1] - pd.DateOffset(months=OOS_MONTHS)
    print(f"樣本內: 開始 ~ {cutoff.strftime('%Y-%m-%d')}")
    print(f"樣本外: {cutoff.strftime('%Y-%m-%d')} ~ 最新\n")
    e1_is, e1_oos, e2_is, e2_oos = [], [], [], []
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
            e1_is  += run_engine1(df, bull, 60, cut_idx)
            e1_oos += run_engine1(df, bull, cut_idx, len(df))
            e2_is  += run_engine2(df, bull, 80, cut_idx)
            e2_oos += run_engine2(df, bull, cut_idx, len(df))
        except Exception as e:
            print(f"  {tk} 錯誤: {e}")
            continue
        time.sleep(0.2)

    print("\n" + "=" * 64)
    print("結果")
    print("=" * 64)
    s1i, s1o = stats(e1_is), stats(e1_oos)
    s2i, s2o = stats(e2_is), stats(e2_oos)
    show(s1i, "引擎⼀(均值回歸) 樣本內")
    show(s1o, "引擎⼀(均值回歸) 樣本外OOS")
    verdict(s1i, s1o, "引擎⼀(均值回歸)")
    show(s2i, "引擎⼆(趨勢) 樣本內")
    show(s2o, "引擎⼆(趨勢) 樣本外OOS")
    verdict(s2i, s2o, "引擎⼆(趨勢)")
    # 儲存
    for name, data in [("oos_e1_insample", e1_is), ("oos_e1_oos", e1_oos),
                        ("oos_e2_insample", e2_is), ("oos_e2_oos", e2_oos)]:
        if data:
            pd.DataFrame(data).to_csv(f"{name}.csv", index=False, encoding="utf-8
    print("\n明細已儲存: oos_e1_insample / oos_e1_oos / oos_e2_insample / oos_e2_oo
    print("\n提醒: 呢個測試冇任何參數可以調 —— 規則鎖死同V6.4⼀致。")
    print("      如果OOS唔合格,正確反應係承認過度擬合,唔係調參數令佢過關。")
if __name__ == "__main__":
    main()
