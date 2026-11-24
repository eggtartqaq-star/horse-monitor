# -*- coding: utf-8 -*-
"""
匯出 golden_v66.csv —— Pine 對照用(Pine 讀唔到檔,要人手對)
==============================================================
揀最近嘅 bar,而且數值遠離門檻(唔會因為少少數據差異而轉向),咁先公平。
TradingView 價格冇派息調整,所以比較「評分、R值、止蝕%、級別、突破」,唔比較絕對價格。
用法:python golden_export.py [--source yf]     (預設用 data/ CSV)
"""
import argparse
import os
import sys

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lab                       # noqa: E402
import rules_v642 as R           # noqa: E402
import signals_v66 as S          # noqa: E402
from indicators import calc_indicators  # noqa: E402

TICKERS = ["AAPL", "MSFT", "PFE", "WMT", "NFLX", "BAC", "XOM", "JPM", "UBER", "INTC", "MU", "NVDA"]


def far(x, thr, gap):
    return pd.notna(x) and abs(x - thr) > gap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["csv", "yf"], default="csv")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    ap.add_argument("--n", type=int, default=24)
    a = ap.parse_args()
    data = lab.load_csv(a.data, TICKERS + ["SPY"]) if a.source == "csv" else lab.load_yf(TICKERS + ["SPY"], "2y")
    spy = data["SPY"]
    bull = spy["Close"] > spy["Close"].rolling(200).mean()
    rows = []
    for tk in TICKERS:
        ind = calc_indicators(data[tk])
        for i in range(len(ind) - 120, len(ind)):
            row = ind.iloc[i].copy()
            d = ind.index[i]
            row["bull"] = bool(bull.reindex([d]).fillna(False).iloc[0])
            if not row["bull"] or not (far(row["ADX"], 25, 1.5) and far(row["ADX"], 30, 0.7) and far(row["ADX"], 40, 0.7)):
                continue
            ev = S.evaluate(row)
            e1, e2 = ev["e1"], ev["e2"]
            sc_t = R.trend_score(row)
            rec = {"date": d.strftime("%Y-%m-%d"), "ticker": tk, "ADX": round(row["ADX"], 1),
                   "route": ev["route"], "E1_score": round(R.mr_score(row), 3), "E1_R": "", "E1_stop%": "",
                   "E1_tier": "", "E2_score": round(sc_t, 3), "E2_breakout": int(row["High"] >= row["high_20d"]),
                   "E2_stop%": round(3 * row["ATR"] / row["Close"] * 100, 1),
                   "path_bt": (S.on_path(ev, "bt") or {}).get("engine", ""),
                   "path_scan": (S.on_path(ev, "scan") or {}).get("engine", "")}
            if e1:
                if not (far(e1["score"], 0.55, 0.03) and far(e1["r"], 2.0, 0.2) and far(e1["r"], 3.0, 0.2)
                        and far(e1["rsi2"], 10, 2) and far(e1["risk_pct"], 15, 0.5)):
                    continue
                rec.update({"E1_R": e1["r"], "E1_stop%": round(e1["risk_pct"], 1),
                            "E1_tier": "強" if e1["strong"] else "普通"})
            elif ev["route"] == "TREND_UP" and not (far(sc_t, 0.65, 0.03) and far(rec["E2_stop%"], 12, 0.5)):
                continue
            rows.append(rec)
    df = pd.DataFrame(rows)
    # 分層抽樣:引擎二交易路徑 / 引擎二只記錄 / 引擎一 / 冇訊號;每隻股最多3行,取最近
    buckets = [
        ("E2交易", df[df["path_bt"] == "E2"], 6),
        ("E2只記錄", df[(df["path_scan"] == "E2") & (df["path_bt"] == "")], 5),
        ("E1", df[df["path_bt"] == "E1"], 7),
        ("冇訊號", df[(df["path_bt"] == "") & (df["path_scan"] == "")], 6),
    ]
    parts = []
    for name, sub, k in buckets:
        sub = sub.sort_values("date").groupby("ticker").tail(3).sort_values("date").tail(k)
        parts.append(sub.assign(bucket=name))
        print(f"  {name}: {len(sub)}")
    pick = pd.concat(parts)
    out = os.path.join(HERE, "pine", "golden_v66.csv")
    pick.sort_values(["ticker", "date"]).to_csv(out, index=False, encoding="utf-8-sig")
    print(f"已寫入 {out}({len(pick)} 行)")
    print(pick.sort_values(["ticker", "date"]).to_string(index=False))


if __name__ == "__main__":
    main()
