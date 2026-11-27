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
import sizing_v66 as Z           # noqa: E402
from indicators import calc_indicators  # noqa: E402

TICKERS = ["AAPL", "MSFT", "PFE", "WMT", "NFLX", "BAC", "XOM", "JPM", "UBER", "INTC", "MU", "NVDA"]


# 2026-11-27(Tom 11-24 檢閱 INFO):評分要離門檻 > 0.05 —— 大過一個引擎二評分級距(0.0375 / 0.045),
# 咁 TradingView 數據少少唔同、令一個評分項轉級,都唔會令 golden 行跨過門檻。
def far(x, thr, gap):
    return pd.notna(x) and abs(x - thr) > gap


def a_ok(close_real, stop_real, engine):
    """Tom 2026-11-24:Pine 嘅級別/交易路徑旗號包括「A(10%)買得起1股」(同 V6.4.2 Pine 一樣)。
    golden 行一定要遠離呢條界線(價 ≤ 97% 上限、1股風險 ≤ 97% 預算),否則 Pine 會「正確地」顯示 0 而對照失敗。"""
    cap = Z.C.ACCOUNT_HKD / Z.C.USD_HKD * Z.C.CAP_A_PCT / 100
    budget = Z.C.ACCOUNT_HKD * Z.C.RISK_PCT / 100 / Z.C.USD_HKD
    sh = Z.size(close_real, stop_real, engine, "A")["shares"]
    return sh, (sh >= 1 and close_real <= 0.97 * cap and close_real - stop_real <= 0.97 * budget)


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
        for i in range(len(ind) - 250, len(ind)):
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
                if not (far(e1["score"], 0.55, 0.05) and far(e1["r"], 2.0, 0.2) and far(e1["r"], 3.0, 0.2)
                        and far(e1["rsi2"], 10, 2) and far(e1["risk_pct"], 15, 0.5)):
                    continue
                # Pine 級別:頂級 = 強 + OBV背離(Pine 唔知財報);強 = RSI2<10 且 R≥3
                rec.update({"E1_R": e1["r"], "E1_stop%": round(e1["risk_pct"], 1),
                            "E1_tier": ("頂級" if e1["obv_div"] else "強") if e1["strong"] else "普通"})
            elif ev["route"] == "TREND_UP" and not (far(sc_t, 0.65, 0.05) and far(rec["E2_stop%"], 12, 0.5)):
                continue
            sg = S.on_path(ev, "bt") or S.on_path(ev, "scan")
            if sg:
                f = lab.raw_factor(tk, d)
                sh, ok = a_ok(row["Close"] * f, sg["stop"] * f, sg["engine"])
                if not ok:
                    continue
                rec["A股數"] = sh
            rows.append(rec)
    df = pd.DataFrame(rows)
    # 分層抽樣:引擎二交易路徑 / 引擎二只記錄 / 引擎一 / 冇訊號;每隻股最多3行,取最近
    buckets = [
        ("E2交易", df[df["path_bt"] == "E2"], 6),
        ("E2只記錄", df[(df["path_scan"] == "E2") & (df["path_bt"] == "")], 5),
        ("E1強", df[df["E1_tier"].isin(["強", "頂級"])], 2),      # Tom:要至少有強/頂級先測到 Pine 嘅級別
        ("E1", df[(df["path_bt"] == "E1") & ~df["E1_tier"].isin(["強", "頂級"])], 5),
        ("冇訊號", df[(df["path_bt"] == "") & (df["path_scan"] == "")], 6),
    ]
    parts = []
    for name, sub, k in buckets:
        sub = sub.sort_values("date").groupby("ticker").tail(3).sort_values("date").tail(k)
        parts.append(sub.assign(bucket=name))
        print(f"  {name}: {len(sub)}")
    pick = pd.concat(parts)
    pick["A股數"] = pick["A股數"].astype("Int64")
    out = os.path.join(HERE, "pine", "golden_v66.csv")
    pick.sort_values(["ticker", "date"]).to_csv(out, index=False, encoding="utf-8-sig")
    print(f"已寫入 {out}({len(pick)} 行)")
    print(pick.sort_values(["ticker", "date"]).to_string(index=False))


if __name__ == "__main__":
    main()
