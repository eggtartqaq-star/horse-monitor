# -*- coding: utf-8 -*-
"""V6.6 自我測試 —— 合成數據,唔使上網。改完代碼一定要跑:python selftest.py"""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules_v642 as R          # noqa: E402
import indicators as I          # noqa: E402
import lab                      # noqa: E402

FAILS = []


def check(name, cond):
    print(("  ✅ " if cond else "  ❌ ") + name)
    if not cond:
        FAILS.append(name)


def synth(n=600, seed=1, drift=0.0006, vol=0.018, start=50.0):
    rng = np.random.default_rng(seed)
    r = rng.normal(drift, vol, n)
    c = start * np.exp(np.cumsum(r))
    o = c * (1 + rng.normal(0, 0.004, n))
    h = np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.008, n)))
    l = np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.008, n)))
    v = rng.integers(1_000_000, 5_000_000, n).astype(float)
    idx = pd.bdate_range("2021-01-04", periods=n)
    return pd.DataFrame({"Open": o, "High": h, "Low": l, "Close": c, "Volume": v}, index=idx)


def main():
    print("V6.6 selftest")
    df = I.calc_indicators(synth())
    check("RSI 喺 0–100", df["RSI14"].dropna().between(0, 100).all())
    check("ATR 種子前 = 0,之後 > 0", (df["ATR"].iloc[:13] == 0).all() and (df["ATR"].iloc[14:] > 0).all())
    check("ADX 喺 0–100", df["ADX"].dropna().between(0, 100).all())
    check("OBV 持平日 = +成交量(ta 寫法)",
          float(I.obv_ta(pd.Series([1.0, 1.0]), pd.Series([5.0, 7.0])).iloc[1]) == 12.0)

    # 真 V6.4.2 mr_plan:先篩 R≥2 再揀最近(V6.5 走樣嘅案例)
    row = {"low_10d": 98.0, "Close": 100.0, "ATR": 1.0, "MA50": 102.0, "high_60d": 110.0}
    p = R.mr_plan(row)
    check("mr_plan:MA50 R<2 但 60日高 R≥2 → 用 60日高(V6.5 會錯拒)",
          p is not None and p["target"] == 110.0)

    # position_plan
    sh, _ = R.position_plan(120.0, 115.0)
    check("position_plan:$120 股,止蝕$5 → 1股(名義上限 $128.21)", sh == 1)
    sh, _ = R.position_plan(130.0, 128.0)
    check("position_plan:$130 股 → 0股(貴過名義上限)", sh == 0)

    # 模擬器不變量
    data = {tk: synth(seed=k + 2, drift=0.0008 + 0.0002 * (k % 3), start=20 + 7 * k)
            for k, tk in enumerate(R.TICKERS)}
    data["SPY"] = synth(seed=99, drift=0.0007, vol=0.009, start=400)
    sig, bull = lab.precompute(data)
    tr, eq, rej = lab.simulate(sig, lab.AS_TRADED)
    check("有交易產生", len(tr) > 0)
    if len(tr):
        check("入場日 > 訊號日(聽日開市,冇前視)", (pd.to_datetime(tr["entry_date"]) > pd.to_datetime(tr["sig_date"])).all())
        ok = all(abs(t.entry - data[t.ticker].loc[pd.Timestamp(t.entry_date), "Open"]) < 1e-9 for t in tr.itertuples())
        check("成交價 = 入場日開市價", ok)
        # 同時持倉 ≤ 2
        ev = []
        for t in tr.itertuples():
            ev += [(pd.Timestamp(t.entry_date), 1), (pd.Timestamp(t.exit_date), -1)]
        ev.sort(key=lambda x: (x[0], x[1]))
        cur = mx = 0
        for _, d in ev:
            cur += d; mx = max(mx, cur)
        check(f"同時持倉 ≤ 2(實際最大 {mx})", mx <= 2)
        check("每筆股數 ≥ 1 且名義值 ≤ US$128.21", ((tr["shares"] >= 1) & (tr["shares"] * tr["entry"] <= 10000 / 7.8 * 0.10 + 1e-6)).all())
        net_lt_gross = (tr["net_pct"] <= tr["gross_pct"] + 1e-9).all()
        check("扣成本後回報 ≤ 毛回報", net_lt_gross)
    # Tom 2026-11-24:買唔起(股數<1)嘅訊號唔可以霸住倉位(真掃描器收市已經唔列出)
    idx2 = pd.bdate_range("2024-01-01", periods=4)
    def mini(px, kind_e2):
        e = ({"kind": "TR", "score": 0.9, "close": px, "atr": px * 0.02, "brk": True} if kind_e2 else
             {"kind": "MR", "score": 0.9, "close": px, "atr": px * 0.02, "low10": px * 0.95,
              "ma50": px * 1.3, "h60": px * 1.4, "plan": {"stop": round(px * 0.945, 2), "target": round(px * 1.3, 2)}})
        f = pd.DataFrame({"Open": px, "High": px * 1.001, "Low": px * 0.999, "Close": px, "Volume": 1e6,
                          "ATR": px * 0.02, "mom_126": 0.0}, index=idx2)
        f["sig"] = [e, {"route": "SKIP"}, {"route": "SKIP"}, {"route": "SKIP"}]
        return f
    trs, _, rj = lab.simulate({"EXP": mini(500.0, True), "CHP": mini(50.0, False)},
                              lab.replace(lab.AS_TRADED, max_positions=1))
    check("買唔起嘅 E2 訊號唔霸倉位 → 買得起嘅 E1 成交",
          len(trs) == 1 and trs["ticker"].iloc[0] == "CHP" and rj["scan_0_shares"] == 1)
    check("拆股表包括 MSTR 2024-08-08(10拆1)", lab.raw_factor("MSTR", pd.Timestamp("2024-08-07")) == 10
          and lab.raw_factor("MSTR", pd.Timestamp("2024-08-08")) == 1)

    trf, _, _ = lab.simulate(sig, lab.AS_TESTED)
    check("as_tested(零成本):淨 = 毛", len(trf) == 0 or np.allclose(trf["net_pct"], trf["gross_pct"]))

    print(f"\n{'全部通過' if not FAILS else f'{len(FAILS)} 項失敗'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
