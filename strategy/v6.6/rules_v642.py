# -*- coding: utf-8 -*-
"""
V6.4.2 規則 —— 由 Owner 2026-11-24 交嘅真正 `dual_engine_v6_4.py` 逐行搬過嚟
==========================================================================
★ 一個數、一個 if 都冇改。parity_check.py 會喺你部電腦對比兩邊輸出。

同 V6.5 rules.py 嘅分別(V6.5 係由截斷咗嘅 PDF 還原,有一處走樣):
  V6.5 mr_target() 揀「最近嘅目標」先,之後先檢查 R≥2 →
    當 MA50 好近(R<2)但 60日高 R≥2,V6.5 會錯誤咁拒絕成筆交易。
  真正 V6.4.2 mr_plan():先篩 R≥2,再喺合格目標入面揀最近。
  呢度用真版本。
"""
import pandas as pd

# ---- 鎖死參數(AGENT_交接文件 第三節) ----
MIN_R = 2.0
ATR_TRAIL_MULT = 3.0
TREND_SCORE_MIN = 0.65
MR_SCORE_MIN = 0.55
TREND_MAX_HOLD = 60
MR_MAX_HOLD = 10
ATR_STOP_MULT = 2.0
MAX_STOP_PCT_TREND = 12.0
MAX_STOP_PCT_MR = 15.0
MAX_POSITION_PCT = 10.0
ACCOUNT_HKD = 10000
RISK_PCT = 1.0
USD_HKD = 7.8

TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO",
    "AMD", "QCOM", "MU", "INTC",
    "JPM", "BAC", "GS", "V", "MA",
    "COST", "WMT", "MCD", "NKE", "SBUX",
    "UNH", "JNJ", "PFE", "LLY",
    "XOM", "CVX", "CAT", "BA",
    "PLTR", "CRM", "ADBE", "NFLX", "SHOP", "UBER", "COIN", "MSTR",
]


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


def mr_plan(row):
    if pd.isna(row["low_10d"]) or pd.isna(row["Close"]):
        return None
    close = row["Close"]
    atr = row.get("ATR")
    if pd.isna(atr) or atr <= 0:
        return None
    stop_struct = row["low_10d"] * 0.995
    stop_atr = close - 2.0 * atr
    stop = min(stop_struct, stop_atr)
    risk = close - stop
    if risk <= 0:
        return None
    targets = []
    if pd.notna(row["MA50"]) and row["MA50"] > close:
        targets.append((row["MA50"], (row["MA50"] - close) / risk))
    if pd.notna(row["high_60d"]) and row["high_60d"] > close:
        targets.append((row["high_60d"], (row["high_60d"] - close) / risk))
    valid = [(p, r) for p, r in targets if r >= MIN_R]
    if not valid:
        return None
    tp, r = min(valid, key=lambda x: x[0])
    return {"stop": round(stop, 2), "target": round(tp, 2), "r": round(r, 2)}


def trend_score(row):
    score = 0.0
    ts = 0.0
    adx = row["ADX"]
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


def trend_plan(row):
    close = row["Close"]; atr = row["ATR"]
    if pd.isna(atr) or atr <= 0 or pd.isna(close):
        return None
    stop = close - ATR_TRAIL_MULT * atr
    risk_pct = (close - stop) / close * 100
    if risk_pct > MAX_STOP_PCT_TREND:
        return None
    return {"stop": round(stop, 2), "risk_pct": round(risk_pct, 1)}


def classify(row):
    adx, dip, din = row["ADX"], row["DI_PLUS"], row["DI_MINUS"]
    if pd.isna(adx) or pd.isna(dip) or pd.isna(din):
        return "SKIP"
    if adx < 25:
        return "MR"
    if dip > din:
        return "TREND_UP"
    return "TREND_DOWN"


def trend_entry_ok(row):
    """引擎二入場前置條件 —— 回測版(run_trend_backtest / oos_validation / momentum_pit):
    ADX≥25、DI+>DI−、今日高 ≥ 20日高(手冊第三節條件3)。
    ★ 更正(Tom F-3):V6.4.2 嘅 run_scan() 同 daily_strong_signals.py **冇**最後一個突破條件。
      以前呢度寫「scan 同 bt 一致」係錯嘅。"""
    return (pd.notna(row["ADX"]) and row["ADX"] >= 25
            and pd.notna(row["DI_PLUS"]) and pd.notna(row["DI_MINUS"])
            and row["DI_PLUS"] > row["DI_MINUS"]
            and pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"])


def is_speculative(df_upto: pd.DataFrame) -> bool:
    h6 = df_upto.tail(126)
    lo = h6["Low"].min()
    return bool(lo > 0 and h6["High"].max() / lo >= 2.0)


def position_plan(entry, stop, account_hkd=ACCOUNT_HKD, usd_hkd=USD_HKD,
                  risk_pct=RISK_PCT, max_position_pct=MAX_POSITION_PCT, fractional=False):
    """V6.4.2 美股版。fractional=True 只供實驗(量度名義上限嘅副作用),唔係建議。"""
    per_share_risk = entry - stop
    if per_share_risk <= 0 or entry <= 0:
        return 0, 0.0
    risk_budget = account_hkd * risk_pct / 100 / usd_hkd
    account_val = account_hkd / usd_hkd
    max_notional = account_val * max_position_pct / 100
    if fractional:
        sh = min(risk_budget / per_share_risk, max_notional / entry)
        sh = int(sh * 100) / 100.0
    else:
        sh = min(int(risk_budget // per_share_risk), int(max_notional // entry))
    return sh, sh * entry


# ============================================================
# 以下兩個函數由 V6.4.2 原檔逐行搬過嚟,只改咗「點樣攞財報日」(由參數傳入,方便離線測試)
# ============================================================
def classify_mr_tier(row, score, plan, days_er):
    """daily_strong_signals.classify_mr_tier:'PREMIUM'/'STRONG'/'BASIC'/None。
    原版喺函數入面 call get_days_to_earnings(ticker);呢度由 days_er 參數傳入(None = 查唔到)。"""
    if plan is None or plan.get("target") is None or plan.get("r") is None:
        return None
    r = plan["r"]
    rsi2 = row.get("RSI2")
    obv_div = bool(row.get("OBV_Div", False))
    if not (score >= 0.55 and r >= MIN_R):
        return None
    cond_rsi2 = pd.notna(rsi2) and rsi2 < 10
    cond_r3 = r >= 3.0
    is_strong = cond_rsi2 and cond_r3
    if not is_strong:
        return "BASIC"
    cond_er = days_er is not None and abs(days_er) > 5
    if obv_div and cond_er:
        return "PREMIUM"
    return "STRONG"


def position_plan_ccy(entry, stop, currency="USD", account_hkd=ACCOUNT_HKD, usd_hkd=USD_HKD,
                      risk_pct=RISK_PCT, max_position_pct=MAX_POSITION_PCT):
    """dual_engine_v6_4.position_plan 原版(含 V6.4.2 港股貨幣修正 D-05)。回傳 (股數, 投入金額)。"""
    per_share_risk = entry - stop
    if per_share_risk <= 0 or entry <= 0:
        return 0, 0
    risk_hkd = account_hkd * risk_pct / 100
    if currency == "HKD":
        risk_budget = risk_hkd
        account_val = account_hkd
    else:
        risk_budget = risk_hkd / usd_hkd
        account_val = account_hkd / usd_hkd
    shares_by_risk = int(risk_budget // per_share_risk)
    max_notional = account_val * max_position_pct / 100
    shares_by_notional = int(max_notional // entry)
    shares = min(shares_by_risk, shares_by_notional)
    return shares, round(shares * entry, 0)
