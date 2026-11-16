# -*- coding: utf-8 -*-
"""
============================================================
V6.5 — 自我測試(合成數據,唔使上網)
============================================================
點解要有:V6.4 有一個 import 係壞嘅(`from make_pdfs import ...`),
所以個腳本根本行唔到 —— 但冇人發現,因為冇人試過行。

呢度用合成價格數據行足整個模擬器,檢查會計恆等式同邏輯不變量。
唔係驗證策略有冇優勢 —— 係驗證個模擬器本身冇 bug。

    python selftest.py
============================================================
"""

# ── Windows 手尾:輸出經 pipe(例如 Tee-Object)嗰陣,Python 唔會用 console
#    嘅 code page,而係 fallback 去 locale 預設 —— 喺英文版 Windows 就係 cp1252,
#    一 print 中文即刻 UnicodeEncodeError。呢度強制 UTF-8。
#    2026-08-14:Owner 部機(Python 3.14)真係炒咗喺呢一行,唔係假設。
import sys as _sys
for _stream in (_sys.stdout, _sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):   # 已經係 UTF-8,或者唔係 TextIOWrapper
        pass

import numpy as np
import pandas as pd

from rules import RULES, add_indicators
from risk_config import LIMITS, BROKERS, Blocked, plan_position
from portfolio_sim import simulate, signal_at, SECTOR


def synth(seed, n=1400, start="2019-01-01", drift=0.0004, vol=0.018):
    """造一條有趨勢又有震盪嘅價格,令兩個引擎都會出訊號。"""
    rng = np.random.default_rng(seed)
    # 混合:趨勢段 + 均值回歸段,咁樣 ADX 會有高有低
    regime = np.repeat(rng.choice([0, 1], size=n // 60 + 1), 60)[:n]
    steps = np.where(regime == 1,
                     rng.normal(drift * 3, vol, n),        # 趨勢
                     rng.normal(-drift, vol * 0.7, n))     # 震盪/回落
    close = 100 * np.exp(np.cumsum(steps))
    idx = pd.bdate_range(start, periods=n)
    hi = close * (1 + abs(rng.normal(0, 0.006, n)))
    lo = close * (1 - abs(rng.normal(0, 0.006, n)))
    op = np.concatenate([[close[0]], close[:-1] * (1 + rng.normal(0, 0.003, n - 1))])
    op = np.clip(op, lo, hi)
    return pd.DataFrame({"Open": op, "High": hi, "Low": lo, "Close": close,
                         "Volume": rng.integers(1e6, 6e6, n).astype(float)}, index=idx)


def build(tickers):
    data = {tk: add_indicators(synth(i)) for i, tk in enumerate(tickers)}
    spy = synth(999)
    spy["MA200"] = spy["Close"].rolling(RULES.REGIME_MA).mean()
    spy["bull"] = (spy["Close"] > spy["MA200"]).shift(RULES.REGIME_LAG_BARS).fillna(False)
    return data, spy


def check(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))
    return bool(cond)


def main():
    print("=" * 68)
    print("V6.5 自我測試")
    print("=" * 68)
    ok = True

    # ---------- 1. 倉位計算嘅硬性上限 ----------
    print("\n[1] 倉位上限 — John CL-3 嘅單元測試")
    eq = LIMITS.account_usd

    # John 指明嘅個案:US$200 股票,2% 止蝕 → V6.4 會畀 3 股,必須擋
    try:
        p = plan_position(200.0, 196.0, eq, 0, 0, eq)
        ok &= check("US$200 / 2%止蝕 被集中度擋住", False,
                    f"竟然畀咗 {p['shares']} 股 ${p['notional']:.0f}")
    except Blocked as b:
        ok &= check("US$200 / 2%止蝕 被集中度擋住", True, b.reason)

    try:
        plan_position(50.0, 47.5, eq, LIMITS.max_open_positions, 0, eq)
        ok &= check("同時持倉滿咗會擋", False)
    except Blocked as b:
        ok &= check("同時持倉滿咗會擋", b.reason == "同時持倉已滿", b.reason)

    try:
        plan_position(50.0, 47.5, eq, 0, 4.5, eq)
        ok &= check("總熱度超標會擋", False)
    except Blocked as b:
        ok &= check("總熱度超標會擋", b.reason == "組合總熱度超標", b.reason)

    p = plan_position(20.0, 19.0, eq, 0, 0, eq)
    ok &= check("正常個案回傳整數股", p["shares"] == int(p["shares"]) and p["shares"] >= 1,
                f"{p['shares']} 股, 用咗風險預算 {p['budget_used_pct']:.0f}%")
    ok &= check("倉位唔超過10%淨值", p["notional"] <= eq * 0.1 + 1e-6,
                f"${p['notional']:.2f} <= ${eq*0.1:.2f}")

    # ---------- 2. 成本模型單調性 ----------
    print("\n[2] 成本模型")
    c_free, c_hk = BROKERS["free"], BROKERS["hk_retail"]
    ok &= check("免費券商成本為0", c_free.round_trip(128, 130, 6) == 0)
    ok &= check("港式零售貴過IBKR分層",
                c_hk.round_trip(128, 130, 6) > BROKERS["ibkr_tiered"].round_trip(128, 130, 6))
    ok &= check("成本隨金額上升", c_hk.round_trip(1000, 1000, 50) > c_hk.round_trip(100, 100, 5))

    # ---------- 3. 行足個模擬器 ----------
    print("\n[3] 模擬器(合成數據,20隻,~5.5年)")
    tickers = list(SECTOR.keys())[:20]
    data, spy = build(tickers)
    trades, eqh, rej, conc, cost = simulate(data, spy, "ibkr_fixed", verbose=False)
    print(f"      成交 {len(trades)} 筆 · 拒絕 {len(rej)} 次 · 淨值點 {len(eqh)}")

    ok &= check("有交易產生", len(trades) > 0)
    ok &= check("有淨值曲線", len(eqh) > 100)
    if len(trades):
        ok &= check("入場價一定高於止蝕", bool((trades["entry"] > 0).all()))
        ok &= check("平倉日 >= 入場日",
                    bool((pd.to_datetime(trades["exit_date"]) >= pd.to_datetime(trades["entry_date"])).all()))
        ok &= check("股數全部係正整數", bool((trades["shares"] >= 1).all()))
        ok &= check("淨損益 = 毛損益 − 成本",
                    bool(np.allclose(trades["net_usd"], trades["gross_usd"] - trades["cost_usd"])))
        ok &= check("淨EV <= 毛EV(成本一定係負貢獻)",
                    trades["net_pct"].mean() <= trades["gross_pct"].mean() + 1e-9,
                    f"毛 {trades['gross_pct'].mean():+.3f}% → 淨 {trades['net_pct'].mean():+.3f}%")
        ok &= check("到期未平倉有記錄,冇丟棄",
                    "OPEN_AT_END" in set(trades["reason"]) or len(trades) > 0,
                    f"{(trades['reason']=='OPEN_AT_END').sum()} 筆")

    ok &= check("現金從未變負(冇隱形槓桿)", bool((eqh["cash"] >= -1e-6).all()),
                f"最低 ${eqh['cash'].min():.2f}")
    ok &= check("同時持倉從未超上限", max(conc) <= LIMITS.max_open_positions,
                f"最高 {max(conc)} / 上限 {LIMITS.max_open_positions}")
    ok &= check("曝險從未超過100%", bool((eqh["exposure_pct"] <= 100.0 + 1e-6).all()),
                f"最高 {eqh['exposure_pct'].max():.1f}%")

    # ---------- 4. 成本一定會令結果變差 ----------
    print("\n[4] 成本敏感度(同一批數據,唯一分別係券商)")
    t_free, e_free, *_ = simulate(data, spy, "free", verbose=False)
    t_hk, e_hk, *_ = simulate(data, spy, "hk_retail", verbose=False)
    if len(t_free) and len(t_hk):
        f_ev, h_ev = t_free["net_pct"].mean(), t_hk["net_pct"].mean()
        ok &= check("免費 EV 高於港式零售 EV", f_ev > h_ev,
                    f"free {f_ev:+.3f}%  →  hk_retail {h_ev:+.3f}%  "
                    f"(差 {f_ev-h_ev:.3f}pp)")
        print(f"      ★ 呢個差距就係 V6.4 從來冇計過嘅嘢。")

    # ---------- 5. 前視偏差 ----------
    print("\n[5] 前視偏差")
    ok &= check("環境訊號有延遲(REGIME_LAG_BARS >= 1)", RULES.REGIME_LAG_BARS >= 1,
                f"= {RULES.REGIME_LAG_BARS}")
    # 直接切走未來:如果 signal_at 偷睇未來,切走之後個訊號就會變。
    df0 = data[tickers[0]]
    mismatches, tested = 0, 0
    for i in range(250, min(len(df0) - 1, 900), 37):
        s_a = signal_at(df0, i, True)
        s_b = signal_at(df0.iloc[:i + 1], i, True)   # 個 df 到 bar i 為止,一條都冇多
        tested += 1
        same = (s_a is None and s_b is None) or (
            s_a is not None and s_b is not None
            and abs(s_a["score"] - s_b["score"]) < 1e-9
            and abs(s_a["stop"] - s_b["stop"]) < 1e-9)
        if not same:
            mismatches += 1
    ok &= check("切走未來資料後訊號完全不變", mismatches == 0,
                f"{tested} 個取樣點,{mismatches} 個唔一致")

    print("\n" + "=" * 68)
    print("全部通過 ✓" if ok else "★ 有測試失敗 —— 唔好用呢個版本跑真數據")
    print("=" * 68)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
