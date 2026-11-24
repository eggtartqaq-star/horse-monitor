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
import config_v66 as C          # noqa: E402
import signals_v66 as S         # noqa: E402
import sizing_v66 as Z          # noqa: E402
import guardrails_v66 as G      # noqa: E402
import ledger_v66 as L          # noqa: E402

FAILS = []
EXPECTED_SYNTH_HASH = "c76849eb6539"   # 由 V6.6.0 第一次跑出嚟;改規則/模擬器 = 要人手更新 + 寫原因


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

    # ---------------- V6.6 核心 ----------------
    # 1) 訊號等價:signals_v66 同 lab.build_signal 每日每隻每條路徑一樣
    diffs = 0; n = 0
    for tk, dfx in sig.items():
        for i in range(80, len(dfx)):
            row = dfx.iloc[i]
            ev = S.evaluate(row)
            for path, cfg in (("bt", lab.AS_TRADED), ("scan", lab.SCANNER)):
                a = lab.build_signal(row["sig"], cfg); b = S.on_path(ev, path)
                n += 1
                if (a or {}).get("engine") != (b or {}).get("engine") or (a and abs(a["stop"] - b["stop"]) > 1e-9):
                    diffs += 1
    check(f"signals_v66 == lab.build_signal(合成數據 {n} 次比較,差異 {diffs})", diffs == 0 and n > 1000)

    # 2) 路徑:突破門檻
    base = {"bull": True, "ADX": 30.0, "DI_PLUS": 30.0, "DI_MINUS": 10.0, "Close": 100.0, "MA20": 98.0,
            "MA50": 95.0, "MA200": 90.0, "dist_60h": 0.5, "vol_ratio": 1.3, "ATR": 2.0,
            "high_20d": 101.0, "High": 100.5}
    ev = S.evaluate(pd.Series(base))
    check("引擎二冇突破:bt 唔認,scan 認", S.on_path(ev, "bt") is None and (S.on_path(ev, "scan") or {}).get("engine") == "E2")
    ev = S.evaluate(pd.Series({**base, "High": 101.0}))
    check("引擎二有突破(今日高 = 20日高,包括今日):兩條路徑都認",
          (S.on_path(ev, "bt") or {}).get("engine") == "E2" and (S.on_path(ev, "scan") or {}).get("engine") == "E2")
    check("熊市(bull=False)→ 冇訊號", S.evaluate(pd.Series({**base, "bull": False}))["route"] == "SKIP")

    # 3) CRO V-2 倉位(B′ 用 size(mode="B_PRIME") 直接測;現行 live 係 A)
    cases = [("$200,止蝕2%,E2 → 擋", 200, 196, "E2", 0), ("E2 $150,止蝕7% → 1股", 150, 139.5, "E2", 1),
             ("E1 $150,止蝕7% → 擋", 150, 139.5, "E1", 0), ("E2 $195 → 擋", 195, 190, "E2", 0),
             ("E2 $185,止蝕7.5%(1股風險$13.88)→ 擋", 185, 171.125, "E2", 0), ("$60,止蝕5% → 2股唔係3股", 60, 57, "E2", 2)]
    for name, e, st, eng, want in cases:
        got = Z.size(e, st, eng, "B_PRIME")["shares"]
        check(f"CRO V-2 B′:{name}(得 {got})", got == want)
    check("A 模式:E2 $150,止蝕7% → 擋(10%)", Z.size(150, 139.5, "E2", "A")["shares"] == 0)
    check("D 模式(影子):$60,止蝕5% → 3股", Z.size(60, 57, "E2", "D")["shares"] == 3)
    check("現行 live 模式 = A", Z.live_mode() == "A")

    # 4) 設定結構性控制:關卡未過唔可以開 B′
    old = (C.CAP_MODE, C.B_PRIME_ENABLED)
    try:
        C.CAP_MODE, C.B_PRIME_ENABLED = "B_PRIME", True
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("關卡未過 → 開 B′ 會被 assert 擋", blocked)
    finally:
        C.CAP_MODE, C.B_PRIME_ENABLED = old
    check("設定自檢通過", C.check_config())

    # 5) 指紋:改一個字節就變
    import shutil, tempfile
    tmp = tempfile.mkdtemp()
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        for fn in C.CORE_FILES:
            shutil.copy(os.path.join(here, fn), tmp)
        f0 = C.fingerprint(tmp)
        with open(os.path.join(tmp, "rules_v642.py"), "ab") as f:
            f.write(b"\n# x\n")
        check("指紋:規則檔改動 → 指紋改變", C.fingerprint(tmp) != f0)
        f1 = C.fingerprint(tmp)
        p_cfg = os.path.join(tmp, "config_v66.py")
        with open(p_cfg, "rb") as f:
            raw = f.read().replace(b"\r\n", b"\n")
        with open(p_cfg, "wb") as f:
            f.write(raw.replace(b"\n", b"\r\n"))
        check("指紋:Windows 行尾(CRLF)唔影響", C.fingerprint(tmp) == f1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # 6) 護欄
    df_small = synth(n=200)
    check("護欄:止蝕16% → 擋", not G.check("X", df_small, 16.0, earnings_ts=None)["ok"])
    check("護欄:財報3日後 → 擋", not G.check("X", df_small, 5.0, earnings_ts=pd.Timestamp.now() + pd.Timedelta(days=3))["ok"])
    g = G.check("X", df_small, 5.0, earnings_ts=None)
    check("護欄:查唔到財報 → 唔擋,標 ?", g["ok"] and g["days_er"] is None)
    check("護欄:歷史重跑 → 財報 off", G.check("X", df_small, 5.0, asof_mode=True)["days_er"] == "off")
    check("classify_mr_tier:查唔到財報 → 最多 STRONG",
          R.classify_mr_tier({"RSI2": 5.0, "OBV_Div": True}, 0.6, {"target": 1, "r": 3.2}, None) == "STRONG")

    # 7) 回歸指紋(合成數據交易清單;只用代號/引擎/日期/出場原因,避開浮點雜訊)
    sig_list = tr[["ticker", "engine", "sig_date", "exit_date", "reason"]].astype(str).values.tolist() if len(tr) else []
    import hashlib
    h = hashlib.sha256(repr(sig_list).encode()).hexdigest()[:12]
    check(f"合成數據交易清單回歸指紋 {h} == {EXPECTED_SYNTH_HASH}", h == EXPECTED_SYNTH_HASH)

    # 8) 影子記錄簿:冪等、BOM 只寫一次、S1/S3 偵測
    import io, contextlib
    tmpL = tempfile.mkdtemp()
    try:
        row = {c: "" for c in L.SIGNAL_COLS}
        row.update(bar_date="2026-01-05", ticker="AAA", path="bt", live=True, engine="E2", score=0.8,
                   close=50, stop=46, guard_ok=True, size_A=2, size_Bp=2, size_D=3)
        n1 = L.append_signals([row], tmpL); n2 = L.append_signals([row], tmpL)
        row2 = dict(row, ticker="BBB"); n3 = L.append_signals([row2], tmpL)
        raw = open(os.path.join(tmpL, "signals.csv"), "rb").read()
        check("記錄簿:同一 (日期,代號,路徑) 唔會寫兩次", (n1, n2, n3) == (1, 0, 1))
        check("記錄簿:UTF-8 BOM 只喺檔頭出現一次", raw.count(b"\xef\xbb\xbf") == 1 and raw.startswith(b"\xef\xbb\xbf"))
        acct = C.ACCOUNT_HKD / C.USD_HKD
        fills = [
            {"fill_id": "1", "ticker": "EXC", "engine": "E2", "open_date": "2026-02-02", "open_px": 180,
             "shares": 1, "init_stop": 168, "open_fees": 0, "close_date": "2026-02-10", "close_px": 150,
             "close_fees": 0, "flags": "B'例外", "notional_pct": 14.0},
            {"fill_id": "2", "ticker": "BIG", "engine": "E1", "open_date": "2026-02-03", "open_px": 60,
             "shares": 2, "init_stop": 50, "open_fees": 0, "close_date": "2026-02-20",
             "close_px": 60 - 0.10 * acct / 2, "close_fees": 0, "flags": "", "notional_pct": 9.4},
            {"fill_id": "3", "ticker": "EX2", "engine": "E2", "open_date": "2026-02-04", "open_px": 150,
             "shares": 1, "init_stop": 140, "open_fees": 0, "close_date": "", "close_px": "",
             "close_fees": "", "flags": "B'例外", "notional_pct": 11.7},
        ]
        L._append_rows(tmpL, "fills.csv", L.FILL_COLS, fills)
        with contextlib.redirect_stdout(io.StringIO()):
            rv = L.review(tmpL, today="2026-03-01")
        check("review:例外倉蝕 >2% 戶口 → S1", any(b.startswith("S1") for b in rv["breaches"]))
        check("review:月熔斷時有例外倉 → S3", any(b.startswith("S3") for b in rv["breaches"]))
    finally:
        shutil.rmtree(tmpL, ignore_errors=True)

    # 9) Telegram bot(離線)
    import telegram_bot_v66 as B
    check("bot:遮 token", "<TOKEN>" in B.redact("/bot123456789:AAEhBP0av18tR_ABCDEFGHIJKLMNOPQ/getMe")
          and "AAEhBP0av18tR" not in B.redact("/bot123456789:AAEhBP0av18tR_ABCDEFGHIJKLMNOPQ/getMe"))
    old_env = os.environ.get("SWING_BOT_TOKEN")
    os.environ["SWING_BOT_TOKEN"] = B.PLACEHOLDER
    try:
        B.load_token(); refused = False
    except SystemExit:
        refused = True
    finally:
        if old_env is None:
            os.environ.pop("SWING_BOT_TOKEN", None)
        else:
            os.environ["SWING_BOT_TOKEN"] = old_env
    check("bot:placeholder token → 拒絕啟動", refused)
    fetch = lambda tk: data.get(tk)
    txt = B.analyze(R.TICKERS[0], fetch=fetch, earnings="off")
    check("bot:離線分析有版本指紋同兩條路徑", C.fingerprint() in txt and "舊掃描器路徑" in txt)
    check("bot:唔喺股票池 → 擋", "唔喺你38隻股票池" in B.analyze("ZZZZ", fetch=lambda tk: data.get(tk, data["SPY"]), earnings="off"))

    print(f"\n{'全部通過' if not FAILS else f'{len(FAILS)} 項失敗'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
