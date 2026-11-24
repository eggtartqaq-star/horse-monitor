# -*- coding: utf-8 -*-
"""
V6.6 對照測試 —— 喺你部電腦跑(要有 yfinance + ta)
==================================================
目的:證明 V6.6 實驗室用嘅指標同訊號,同你每日用嘅 dual_engine_v6_4.py 一致。
雲端環境裝唔到 `ta`,所以指標係自己寫嘅 —— 呢個測試係唯一嘅驗證。

用法:
  1. 將呢個檔案、indicators.py、rules_v642.py 放入同 dual_engine_v6_4.py 同一個資料夾
  2. python parity_check.py
判讀:
  ✅ 訊號一致率 ≥ 99%  → V6.6 回測結果可以信
  ⚠️ 95–99%            → 大致可信,差異係 ADX 喺 25 附近嘅邊界日子
  ❌ < 95%             → 唔好信 V6.6 回測,將輸出畀 AI 睇
"""
import sys
import warnings

warnings.filterwarnings("ignore")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd
import yfinance as yf

import dual_engine_v6_4 as OLD                # 你每日用嘅真引擎
import indicators as NEW_IND
import rules_v642 as NEW

TICKERS = ["AAPL", "NVDA", "PFE", "BAC", "WMT", "COIN"]
COLS = ["RSI14", "RSI2", "ADX", "DI_PLUS", "DI_MINUS", "ATR", "OBV_Div"]


def sig(rules, row):
    route = rules.classify(row)
    if route == "MR":
        return ("MR", rules.mr_score(row) >= rules.MR_SCORE_MIN and rules.mr_plan(row) is not None)
    if route == "TREND_UP":
        sc = rules.trend_score(row)
        sc = sc[0] if isinstance(sc, tuple) else sc
        return ("TR", sc >= rules.TREND_SCORE_MIN and rules.trend_plan(row) is not None)
    return (route, False)


def main():
    print("V6.6 parity check —— 對比 ta 版 (你嘅 dual_engine_v6_4) vs 純 pandas 版 (V6.6)")
    tot = same = 0
    for tk in TICKERS:
        df = yf.Ticker(tk).history(period="3y", auto_adjust=True)
        a = OLD.calc_indicators(df)
        b = NEW_IND.calc_indicators(df)
        a, b = a.iloc[250:], b.iloc[250:]          # 跳過暖身期
        diffs = {}
        for c in COLS:
            if c == "OBV_Div":
                diffs[c] = f"{(a[c] != b[c]).mean() * 100:.2f}% 日子唔同"
            else:
                diffs[c] = f"最大差 {(a[c] - b[c]).abs().max():.4f}"
        n = len(a)
        ok = sum(sig(OLD, a.iloc[i]) == sig(NEW, b.iloc[i]) for i in range(n))
        tot += n; same += ok
        print(f"\n{tk}: 訊號一致 {ok}/{n} = {ok / n * 100:.1f}%")
        for k, v in diffs.items():
            print(f"   {k:9} {v}")
    rate = same / tot * 100
    verdict = "✅ 可信" if rate >= 99 else ("⚠️ 大致可信" if rate >= 95 else "❌ 唔好信 V6.6 回測")
    print(f"\n總訊號一致率 {rate:.2f}%  →  {verdict}")


if __name__ == "__main__":
    main()
