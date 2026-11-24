# -*- coding: utf-8 -*-
"""
V6.6 訊號 —— 一個函數,兩條路徑
================================
evaluate() 用 V6.4.2 原函數(rules_v642)計晒所有嘢;on_path() 決定邊條路徑認唔認呢個訊號。

  "bt"   回測驗證版(真正交易):
         引擎一 = 評分≥0.55 + mr_plan(R≥2)+ 止蝕距離 ≤15%,所有級別
         引擎二 = ADX≥25 + DI+>DI− + **今日高 ≥ 20日高** + 評分≥0.65 + 止蝕 ≤12%
  "scan" 舊 daily_strong_signals 版(只記錄):
         引擎一 = 同上,但只要 RSI2<10 且 R≥3(💪強/⭐頂級)
         引擎二 = 同上,但**冇**突破條件

★ 財報同投機股護欄喺 guardrails_v66,唔喺呢度 —— 呢度只係純規則,方便同回測逐日對比。
"""
import pandas as pd

import rules_v642 as R

PATHS = ("bt", "scan")


def evaluate(row) -> dict:
    """row = calc_indicators() 之後嘅一行,另加 'bull'(SPY 收市 > MA200)。"""
    out = {"route": "SKIP", "bull": bool(row.get("bull", False)), "e1": None, "e2": None}
    if not out["bull"]:
        return out
    route = R.classify(row)
    out["route"] = route
    close = row["Close"]
    if route == "MR":
        sc = R.mr_score(row)
        plan = R.mr_plan(row)
        if sc >= R.MR_SCORE_MIN and plan:
            risk_pct = (close - plan["stop"]) / close * 100
            rsi2 = row.get("RSI2")
            out["e1"] = {
                "score": sc, "stop": plan["stop"], "target": plan["target"], "r": plan["r"],
                "risk_pct": risk_pct, "rsi2": rsi2, "obv_div": bool(row.get("OBV_Div", False)),
                # 級別(未計財報):STRONG = RSI2<10 且 R≥3;頂級要再加 OBV背離 + 距財報>5日
                "strong": bool(pd.notna(rsi2) and rsi2 < 10 and plan["r"] >= 3.0),
            }
    elif route == "TREND_UP":
        sc = R.trend_score(row)
        plan = R.trend_plan(row)                     # 已包括止蝕 ≤12%
        if sc >= R.TREND_SCORE_MIN and plan:
            out["e2"] = {
                "score": sc, "stop": plan["stop"], "risk_pct": plan["risk_pct"],
                "breakout": bool(R.trend_entry_ok(row)),
                "adx": row["ADX"], "dist_60h": row["dist_60h"],
            }
    return out


def on_path(ev: dict, path: str):
    """回傳呢條路徑認可嘅訊號 {'engine','score','stop','target',...} 或 None。"""
    assert path in PATHS
    if ev["e1"] is not None:
        e = ev["e1"]
        if e["risk_pct"] > R.MAX_STOP_PCT_MR:          # V6.3 護欄1(引擎一 15%)
            return None
        if path == "scan" and not e["strong"]:
            return None
        return {"engine": "E1", **e}
    if ev["e2"] is not None:
        e = ev["e2"]
        if path == "bt" and not e["breakout"]:
            return None
        return {"engine": "E2", "target": None, **e}
    return None


def rank_key(sig: dict):
    """同 lab.simulate 一樣嘅排序:引擎二先,之後評分高先。"""
    return (0 if sig["engine"] == "E2" else 1, -sig["score"])
