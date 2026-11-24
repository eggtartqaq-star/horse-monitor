# -*- coding: utf-8 -*-
"""
V6.6 護欄 —— 由 V6.4.2 dual_engine_v6_4.check_guardrails / get_days_to_earnings 搬過嚟
====================================================================================
改動只有三樣(全部係令佢更安全,唔會令訊號變多):
  1. yfinance 延遲 import(離線測試唔使裝)
  2. 回傳下次財報日期本身(影子記錄要用嚟檢查「持倉期間有冇財報」)
  3. --asof 歷史重跑時財報檢查關閉,標明 "off" —— 因為 yfinance 只知「今日」嘅下次財報日
"""
import pandas as pd

import rules_v642 as R


def get_next_earnings(ticker):
    """回傳 pd.Timestamp 或 None(查唔到)。同時處理 yfinance 新舊兩種 .calendar 格式。"""
    try:
        import yfinance as yf
        cal = yf.Ticker(ticker).calendar
        if cal is None:
            return None
        ed = None
        if isinstance(cal, dict):
            ed = cal.get("Earnings Date")
            if isinstance(ed, (list, tuple)) and ed:
                ed = ed[0]
        else:
            if "Earnings Date" in getattr(cal, "index", []):
                ed = cal.loc["Earnings Date"][0]
        if ed is None:
            return None
        ts = pd.Timestamp(ed)
        return ts.tz_localize(None) if ts.tzinfo is not None else ts
    except Exception:
        return None


def days_to(ts, today=None):
    if ts is None:
        return None
    today = (today or pd.Timestamp.now()).normalize()
    return int((ts.normalize() - today).days)


def is_speculative(df_upto) -> bool:
    try:
        return R.is_speculative(df_upto)
    except Exception:
        return False


def check(ticker, df_upto, risk_pct, earnings_ts="lookup", asof_mode=False):
    """
    同 V6.4.2 check_guardrails 一樣嘅次序:
      1. 止蝕距離 > 15% → 擋
      2. 財報 0–5 日內 → 擋;查唔到 → "?"(唔擋,要你自己上網查)
      3. 半年高低 ≥2 倍 → ⚠️投機(唔擋)
    回傳 dict(ok, reason, flag, days_er, earnings_date)
    earnings_ts: "lookup" = 用 yfinance 查;或者直接傳入 Timestamp/None(測試用)
    """
    out = {"ok": True, "reason": "", "flag": "✅", "days_er": None, "earnings_date": None}
    if risk_pct is not None and risk_pct > R.MAX_STOP_PCT_MR:
        out.update(ok=False, reason=f"止蝕{risk_pct:.0f}%過闊")
        return out
    if is_speculative(df_upto):
        out["flag"] = "⚠️投機"
    if asof_mode:
        out["reason"] = "財報檢查:off(歷史重跑)"
        out["days_er"] = "off"
        return out
    ts = get_next_earnings(ticker) if earnings_ts == "lookup" else earnings_ts
    d = days_to(ts)
    out["days_er"], out["earnings_date"] = d, ts
    if d is not None and 0 <= d <= 5:
        out.update(ok=False, reason=f"財報{d}日內")
    return out
