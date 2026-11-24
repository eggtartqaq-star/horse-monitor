# -*- coding: utf-8 -*-
"""
V6.6 對照測試(關卡 V-3)—— 喺你部電腦跑(要有 yfinance + ta)
================================================================
證明 V6.6(純 pandas 指標 + signals_v66)同你每日用嘅 dual_engine_v6_4.py(用 ta)
喺每一日、兩條路徑,出一樣嘅訊號。

用法:
  1. 將你嘅 dual_engine_v6_4.py 複製入 V6.6 資料夾(唔好改佢)
  2. python parity_check.py
過關標準(Tom F-6,2026-11-24 收緊):
  A. 第250條bar之後:|ΔADX|、|ΔDI+|、|ΔDI−| 最大值 < 0.01;|ΔRSI14|、|ΔRSI2| < 0.01;ATR 相對差 < 0.01%
  B. 「有訊號嘅日子」(兩邊任何一邊有訊號)一致率 ≥ 98%,兩條路徑分開計
     (舊版計「所有日子」—— 大部分日子冇訊號,99% 都可以藏住 7% 嘅訊號日唔同)
全部過關 → 喺 config_v66.py 將 GATES["V3_對照測試"] 改做 True,並將輸出畀 AI / CRO 睇。
"""
import sys
import warnings

warnings.filterwarnings("ignore")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import numpy as np
import pandas as pd

TICKERS = ["AAPL", "NVDA", "PFE", "BAC", "WMT", "COIN", "XOM", "UBER", "MU", "LLY"]
TOL_IND = 0.01
TOL_SIG = 98.0


def old_paths(OLD, row, bull):
    """用你嘅 dual_engine_v6_4 原函數砌兩條路徑(同 signals_v66 定義一樣)。"""
    if not bull:
        return (None, None)
    route = OLD.classify(row)
    if route == "MR":
        sc = OLD.mr_score(row)
        plan = OLD.mr_plan(row)
        if sc >= OLD.MR_SCORE_MIN and plan:
            risk = (row["Close"] - plan["stop"]) / row["Close"] * 100
            if risk > OLD.MAX_STOP_PCT_MR:
                return (None, None)
            strong = pd.notna(row["RSI2"]) and row["RSI2"] < 10 and plan["r"] >= 3.0
            return ("E1", "E1" if strong else None)
    elif route == "TREND_UP":
        sc, _ = OLD.trend_score(row)
        plan = OLD.trend_plan(row)
        if sc >= OLD.TREND_SCORE_MIN and plan:
            brk = pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]
            return ("E2" if brk else None, "E2")
    return (None, None)


def main():
    import yfinance as yf
    import dual_engine_v6_4 as OLD           # 你每日用嘅真引擎(用 ta)
    import config_v66 as C
    import indicators as NEW_IND
    import signals_v66 as S

    print(f"V6.6 parity check  |  V6.6 指紋 {C.fingerprint()}  |  pandas {pd.__version__}")
    spy = yf.Ticker("SPY").history(period="3y", auto_adjust=True)
    spy.index = spy.index.tz_localize(None).normalize()
    bull = spy["Close"] > spy["Close"].rolling(200).mean()

    worst = {"ADX": 0.0, "DI_PLUS": 0.0, "DI_MINUS": 0.0, "RSI14": 0.0, "RSI2": 0.0, "ATR_rel%": 0.0}
    agree = {"bt": [0, 0], "scan": [0, 0]}
    diffs = []
    for tk in TICKERS:
        df = yf.Ticker(tk).history(period="3y", auto_adjust=True)
        df.index = df.index.tz_localize(None).normalize()
        a = OLD.calc_indicators(df).iloc[250:]
        b = NEW_IND.calc_indicators(df).iloc[250:]
        for c in ("ADX", "DI_PLUS", "DI_MINUS", "RSI14", "RSI2"):
            worst[c] = max(worst[c], float((a[c] - b[c]).abs().max()))
        worst["ATR_rel%"] = max(worst["ATR_rel%"], float(((a["ATR"] - b["ATR"]).abs() / a["ATR"]).max() * 100))
        bb = bull.reindex(b.index).ffill().fillna(False)
        for i in range(len(b)):
            d = b.index[i]
            ra, rb = a.iloc[i], b.iloc[i].copy()
            rb["bull"] = bool(bb.iloc[i])
            o_bt, o_scan = old_paths(OLD, ra, bool(bb.iloc[i]))
            ev = S.evaluate(rb)
            n_bt = (S.on_path(ev, "bt") or {}).get("engine")
            n_scan = (S.on_path(ev, "scan") or {}).get("engine")
            for path, o, n in (("bt", o_bt, n_bt), ("scan", o_scan, n_scan)):
                if o or n:
                    agree[path][1] += 1
                    if o == n:
                        agree[path][0] += 1
                    else:
                        diffs.append((tk, d.date(), path, o, n, round(ra["ADX"], 2), round(rb["ADX"], 2)))
        print(f"  ✓ {tk}")

    print("\nA. 指標最大差(第250條bar之後)")
    ok_a = True
    for k, v in worst.items():
        good = v < TOL_IND
        ok_a &= good
        print(f"   {k:9} {v:.5f}  {'✅' if good else '❌'}")
    print("\nB. 有訊號日子一致率")
    ok_b = True
    for path, (s, n) in agree.items():
        rate = s / n * 100 if n else 100.0
        good = rate >= TOL_SIG
        ok_b &= good
        print(f"   {path:5} {s}/{n} = {rate:.2f}%  {'✅' if good else '❌'}")
    if diffs:
        print("\n唔一致嘅日子(頭20個):代號, 日期, 路徑, 舊, 新, 舊ADX, 新ADX")
        for x in diffs[:20]:
            print("  ", x)
    verdict = ok_a and ok_b
    if verdict:
        print('\n✅ V-3 過關 —— 可以將 config_v66.py 入面 GATES["V3_對照測試"] 改做 True')
    else:
        print("\n❌ V-3 未過 —— 唔好信 V6.6 回測同掃描,將呢個輸出畀 AI 睇")
    sys.exit(0 if verdict else 1)


if __name__ == "__main__":
    main()
