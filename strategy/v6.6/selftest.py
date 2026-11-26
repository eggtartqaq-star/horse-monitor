# -*- coding: utf-8 -*-
"""V6.6 自我測試 —— 合成數據,唔使上網。改完代碼一定要跑:python selftest.py"""
import os
import re
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
    # 2026-11-25:selftest 一律用臨時空記錄簿 —— 唔讀、唔寫你真嘅 ledger/(否則你真有未解釋 S2 嗰陣,
    # bot 測試會失敗,.bat 會叫你「今日唔好交易」,同 N-1 一樣係假警報)
    import tempfile as _tf
    # 審計 X-1(2026-11-25):你嘅設定先做一次自檢(設定錯 = 真問題,唔係假警報)……
    try:
        C.check_config()
        cfg_ok, cfg_msg = True, ""
    except AssertionError as e:                      # ConfigError 係 AssertionError 嘅子類
        cfg_ok, cfg_msg = False, f"({e})"
    check(f"你嘅 owner_settings.json 通過設定自檢{cfg_msg}", cfg_ok)
    # ……然後所有測試用預設設定跑:預期數係按 HK$10,000、上限 A 寫嘅。
    # 唔咁做,你照 CRO C-7 將 account_hkd 改做真實淨值,自我測試就會日日失敗,.bat 日日叫你「今日唔好交易」。
    keep = {k: getattr(C, k) for k in ("ACCOUNT_HKD", "CAP_MODE", "B_PRIME_ENABLED", "_B_PRIME_RAW",
                                        "B_PRIME_CRO_NOTE", "SWITCH_DATE")}
    keep_gates, keep_fee = dict(C.GATES), dict(C.REAL_FEE)
    C.ACCOUNT_HKD = float(C.DEFAULT_SETTINGS["account_hkd"])
    C.CAP_MODE, C.B_PRIME_ENABLED, C._B_PRIME_RAW = "A", False, False
    C.B_PRIME_CRO_NOTE, C.SWITCH_DATE = "", None
    C.GATES.clear(); C.GATES.update(C.DEFAULT_SETTINGS["gates"])
    C.REAL_FEE.clear(); C.REAL_FEE.update(C.DEFAULT_SETTINGS["real_fee"])
    real_ledger = L.DEFAULT_DIR
    L.DEFAULT_DIR = _tf.mkdtemp(prefix="selftest_ledger_")
    try:
        _main_body()
    finally:
        import shutil as _sh
        _sh.rmtree(L.DEFAULT_DIR, ignore_errors=True)
        L.DEFAULT_DIR = real_ledger
        for k, v in keep.items():
            setattr(C, k, v)
        C.GATES.clear(); C.GATES.update(keep_gates)
        C.REAL_FEE.clear(); C.REAL_FEE.update(keep_fee)
    print(f"\n{'全部通過' if not FAILS else f'{len(FAILS)} 項失敗'}")
    sys.exit(1 if FAILS else 0)


def _main_body():
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

    # ---- V6.6.6(2026-11-26 收入研究):lab 實盤入場規則 + 閒置現金收息 ----
    rng66 = np.random.default_rng(66)
    n66 = bad66 = 0
    for _ in range(400):
        cl = round(float(rng66.uniform(5, 130)), 2)
        st = round(cl * (1 - float(rng66.uniform(0.01, 0.15))), 2)
        eng = "E1" if rng66.random() < 0.5 else "E2"
        tg = round(cl * (1 + float(rng66.uniform(0.05, 0.40))), 2) if eng == "E1" else None
        sh = R.position_plan(cl, st, account_hkd=10000)[0]
        if sh < 1:
            continue
        n66 += 1
        a = lab._max_limit_adj({"sig_close": cl, "stop": st, "engine": eng, "target": tg}, 1.0, sh, lab.AS_TRADED)
        bad66 += a != Z.max_limit(cl, st, sh, eng, target=tg)
    check(f"V6.6.6:lab 限價上限 == sizing_v66.max_limit({n66} 個隨機組合,差異 {bad66})", n66 > 100 and bad66 == 0)

    LIM66 = lab.replace(lab.AS_TRADED, entry_rule="limit")
    sh66 = R.position_plan(50.0, 47.25, account_hkd=10000)[0]
    lim66 = Z.max_limit(50.0, 47.25, sh66, "E1", target=65.0)

    def chp(open1):
        f = mini(50.0, False)
        f.loc[idx2[1], "Open"] = open1
        f.loc[idx2[1], "Low"] = min(f.loc[idx2[1], "Low"], open1)
        f.loc[idx2[1], "High"] = max(f.loc[idx2[1], "High"], open1)
        return {"CHP": f}
    t_hi, _, r_hi = lab.simulate(chp(round(lim66 + 0.01, 2)), LIM66)
    check(f"V6.6.6:開市高過限價上限(${lim66})一仙 → 冇成交", len(t_hi) == 0 and r_hi["limit"] == 1)
    t_fl, _, r_fl = lab.simulate(chp(47.25), LIM66)
    check("V6.6.6:開市 ≤ 系統止蝕 → 唔買(C-8 修訂、N-26)", len(t_fl) == 0 and r_fl["floor"] == 1)
    t_ok, e_ok, _ = lab.simulate(chp(49.0), LIM66)
    check(f"V6.6.6:止蝕 < 開市 ≤ 限價上限 → 開市價成交、股數 = 收市計嗰個({sh66} 股)",
          len(t_ok) == 1 and abs(t_ok["entry"].iloc[0] - 49.0) < 1e-9 and t_ok["shares"].iloc[0] == sh66)
    t_lim, _, _ = lab.simulate(chp(lim66), LIM66)
    check("V6.6.6:開市 = 限價上限 → 成交", len(t_lim) == 1)

    r66 = 0.0002
    cy66 = pd.Series(100 * (1 + r66) ** np.arange(len(idx2)), index=idx2)
    skip = mini(50.0, False); skip["sig"] = [{"route": "SKIP"}] * len(idx2)
    cap66, base66 = 12500 / R.USD_HKD, 10000 / R.USD_HKD
    _, e_none, _ = lab.simulate({"CHP": skip}, lab.replace(lab.AS_TRADED, capital_hkd=12500))
    check("V6.6.6:唔收息 → 淨值 = 資金(12,500)", np.allclose(e_none["equity"], cap66, atol=1e-9, rtol=0))
    _, e_cy, _ = lab.simulate({"CHP": skip}, lab.replace(lab.AS_TRADED, capital_hkd=12500, cash_yield=cy66,
                                                         cash_reserve_pct=20.0))
    want = 0.2 * base66 + (cap66 - 0.2 * base66) * (1 + r66) ** (len(idx2) - 1)
    check("V6.6.6:閒置現金收息 = 留底(基數 20%)+ 其餘 × T-bill 回報",
          abs(e_cy["equity"].iloc[-1] - want) < 1e-9)
    _, e_pos, _ = lab.simulate(chp(49.0), lab.replace(LIM66, capital_hkd=12500, cash_yield=cy66))
    cb, it = 49.0 * sh66, 0.0
    for _ in range(len(idx2) - 1):
        it += (cap66 + it - cb) * r66
    check("V6.6.6:持倉嘅錢唔收息(現金 = 資金 − 成本)",
          e_pos["n_pos"].iloc[-1] == 1 and abs(e_pos["equity"].iloc[-1] - (cap66 + it + (50.0 - 49.0) * sh66)) < 1e-9)
    cfg_cap = lab.replace(lab.AS_TRADED, capital_hkd=10000)
    cfg_zero = lab.replace(lab.AS_TRADED, cash_yield=pd.Series(1.0, index=eq.index))
    same = all(np.array_equal(lab.simulate(sig, c)[1]["equity"].values, eq["equity"].values) for c in (cfg_cap, cfg_zero))
    check("V6.6.6:預設(資金 = 基數、唔收息)淨值同舊公式一樣", same)

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
    # Tom 2026-11-24:B′ 依手續正式開咗(關卡全過 + CRO 文件)之後,呢兩項唔可以令 selftest 失敗(否則 .bat 拒絕掃描)
    authorised = (C.CAP_MODE == "B_PRIME" and C.B_PRIME_ENABLED and not C.gates_outstanding()
                  and C.B_PRIME_CRO_NOTE in C.APPROVED_BPRIME_NOTES)
    check(f"現行 live 模式 = {'B_PRIME(已授權)' if authorised else 'A'}", Z.live_mode() == ("B_PRIME" if authorised else "A"))

    # 4) 設定結構性控制:關卡未過 / 冇 CRO 文件唔可以開 B′(用臨時設定測,唔受現行設定影響)
    old = (C.CAP_MODE, C.B_PRIME_ENABLED, dict(C.GATES), C.B_PRIME_CRO_NOTE, C.APPROVED_BPRIME_NOTES)
    try:
        C.CAP_MODE, C.B_PRIME_ENABLED, C.B_PRIME_CRO_NOTE = "B_PRIME", True, "test"
        C.GATES.update({k: True for k in C.GATES}); C.GATES[next(iter(C.GATES))] = False
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("關卡未過 → 開 B′ 會被 assert 擋", blocked)
        C.GATES.update({k: True for k in C.GATES}); C.B_PRIME_CRO_NOTE = ""
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("關卡全過但冇 CRO 文件 → 開 B′ 會被擋", blocked)
        C.B_PRIME_CRO_NOTE = "ok"
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("CRO 文件唔係 reports/risk/...+日期 → 擋", blocked)
        C.B_PRIME_CRO_NOTE = "reports/risk/2026-12-01-bprime-approval.md 2026-12-01"
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("CRO 文件格式啱但唔喺 APPROVED_BPRIME_NOTES(代碼)→ 擋(CRO N-7)", blocked)
        C.APPROVED_BPRIME_NOTES = (C.B_PRIME_CRO_NOTE,)
        try:
            ok_full = C.check_config()
        except AssertionError:
            ok_full = False
        check("關卡全過 + CRO 文件喺代碼批准清單 → 准開 B′", ok_full is True)
        C.GATES[next(iter(C.GATES))] = "true"
        try:
            C.check_config(); blocked = False
        except AssertionError:
            blocked = True
        check("關卡寫成文字 \"true\"(有引號)→ 擋(CRO N-7)", blocked)
        C.GATES.update({k: "false" for k in C.GATES})
        check("關卡寫成 \"false\"(有引號)→ 唔當過關", len(C.gates_outstanding()) == len(C.GATES))
    finally:
        C.CAP_MODE, C.B_PRIME_ENABLED, C.B_PRIME_CRO_NOTE = old[0], old[1], old[3]
        C.APPROVED_BPRIME_NOTES = old[4]
        C.GATES.clear(); C.GATES.update(old[2])
    import subprocess
    code = ("import config_v66 as C; C.CAP_MODE='B_PRIME'; C.B_PRIME_ENABLED=True; "
            "C.GATES.update({k: True for k in C.GATES}); C.B_PRIME_CRO_NOTE='reports/risk/2099-01-01-x.md'; "
            "C.check_config()")
    rc = subprocess.run([sys.executable, "-O", "-c", code], cwd=os.path.dirname(os.path.abspath(__file__)),
                        capture_output=True).returncode
    check("python -O 之下,未批准嘅 B′ 都會被擋(CRO B-3)", rc != 0)
    check("設定自檢通過", C.check_config())
    import inspect
    check("check_config 冇用 assert(python -O 關唔到)", "assert " not in inspect.getsource(C.check_config))
    check("規則指紋唔包括 owner_settings.json", "owner_settings.json" not in C.CORE_FILES)
    bat = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "掃描_v66.bat"), "rb").read().decode("utf-8")
    check("掃描_v66.bat:冇半形括號(Tom F-1)、selftest 失敗會 goto 停、CRLF、冇 BOM",
          "(" not in bat and ")" not in bat and "if errorlevel 1 goto FAILED" in bat
          and "if errorlevel 1 goto SCANFAILED" in bat and "V6.4" not in bat
          and bat.count("\r\n") == bat.count("\n") and not bat.startswith("\ufeff"))

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

    # 8b) Tom 2026-11-24:fill 時嘅 S2 偵測(過期訊號、護欄擋、A=0、自訂收緊止蝕、超過2倉)
    import types
    tmpF = tempfile.mkdtemp()
    try:
        def srow(day, tk, **kw):
            r = {c: "" for c in L.SIGNAL_COLS}
            r.update(bar_date=day, ticker=tk, path="bt", live=True, engine="E2", score=0.8, close=50, stop=46,
                     guard_ok=True, size_A=2, size_Bp=2, size_D=3, rank=1)
            r.update(kw); return r
        def run(day, bull=True, folder=None):
            L.append_run({"bar_date": day, "bull": bull, "live_path": "bt", "source": "yf"}, folder or tmpF)
        L.append_signals([srow("2026-03-02", "OLD"), srow("2026-03-03", "NEW"),
                          srow("2026-03-03", "ERN", guard_ok=False, guard_reason="財報2日內"),
                          srow("2026-03-03", "EXP", close=126, stop=112, size_A=0, size_Bp=0)], tmpF)
        run("2026-03-02"); run("2026-03-03")

        def fill(tk, px, sh, st, day="2026-03-04", folder=None):
            a = types.SimpleNamespace(action="open", ticker=tk, price=px, shares=sh, stop=st, engine="E2",
                                      date=day, fees=0.0, reason=None, target=None)
            with contextlib.redirect_stdout(io.StringIO()):
                L.cmd_fill(a, folder or tmpF)
            f = L.read(folder or tmpF, "fills.csv", L.FILL_COLS)
            return f[f["ticker"] == tk]["flags"].iloc[-1]
        check("fill:今日有 live 訊號 → 冇 S2", "S2" not in fill("NEW", 50.0, 2, 46.0))
        check("fill:幾日前嘅 live 訊號(上次掃描冇呢隻)→ S2 過期", "S2:冇 live 訊號(stale" in fill("OLD", 50.0, 2, 46.0))
        L._rewrite(tmpF, "fills.csv", L.FILL_COLS, L.read(tmpF, "fills.csv", L.FILL_COLS).iloc[0:0])
        check("fill:護欄擋咗嘅訊號 → S2", "S2:護欄擋咗" in fill("ERN", 50.0, 2, 46.0))
        fl = fill("EXP", 126.0, 1, 116.0)
        check("fill:A=0 + 自訂收緊止蝕 → S2(兩樣都標)", "S2:系統A倉位=0" in fl and "自訂收緊" in fl)
        check("fill:已有2倉再開 → S2", "S2:已有2倉" in fill("NEW", 50.0, 2, 46.0))

        # CRO C-4r(2026-11-25):心跳(runs.csv)決定「上次掃描」;熊市日、漏咗嘅交易日都會標
        def fresh(runs, rows):
            d = tempfile.mkdtemp(dir=tmpF)
            L.append_signals(rows, d)
            for day, bull in runs:
                run(day, bull, d)
            return d
        d1 = fresh([("2026-03-03", True), ("2026-03-04", False)], [srow("2026-03-03", "PFE")])
        check("fill:訊號之後有熊市日(CRO F1)→ S2", "S2:冇 live 訊號(bear" in fill("PFE", 50.0, 2, 46.0, "2026-03-05", d1))
        d2 = fresh([("2026-03-03", True)], [srow("2026-03-03", "PFE")])
        check("fill:上次掃描之後漏咗2個交易日 → S2 過期", "漏咗2個交易日" in fill("PFE", 50.0, 2, 46.0, "2026-03-06", d2))
        d3 = fresh([], [srow("2026-03-03", "PFE")])
        check("fill:冇 runs.csv(冇掃描心跳)→ S2", "S2:冇 live 訊號(none:冇掃描記錄" in fill("PFE", 50.0, 2, 46.0, "2026-03-04", d3))
        d4 = fresh([("2026-04-02", True)], [srow("2026-04-02", "PFE")])
        check("fill:中間係假期(2026-04-03 耶穌受難節)+ 週末 → 唔算過期",
              "S2" not in fill("PFE", 50.0, 2, 46.0, "2026-04-06", d4))
        check("NYSE 交易日:感恩節前後(11-25 → 11-27)中間 0 日", L.nyse_sessions_between("2026-11-25", "2026-11-27") == 0)
        d5 = fresh([("2026-03-03", True)], [srow("2026-03-03", "PFE"), srow("2026-03-03", "KO")])
        check("fill:止蝕高過系統 2 仙 → S2 自訂收緊(容差而家係 1 仙)", "自訂收緊" in fill("PFE", 50.0, 2, 46.02, "2026-03-04", d5))
        check("fill:止蝕高過系統 0.5 仙 → 唔標", "自訂收緊" not in fill("KO", 50.0, 2, 46.005, "2026-03-04", d5))
        d6 = fresh([("2026-03-03", True)], [srow("2026-03-03", "RBD", close=20, stop=17.8, size_A=5, size_Bp=5, engine="E1")])
        fl6 = fill("RBD", 20.0, 6, 17.8, "2026-03-04", d6)
        check("fill:股數多過系統(按成交價同系統止蝕計 5 股,買咗 6 股)→ S2(CRO F6)", "S2:股數6多過系統5股" in fl6)

        # CRO N-12:舊版(V6.6.0/6.6.1)fills.csv 冇 logged_at → 新版記錄要先升級表頭,唔可以變成「18 欄表頭 + 19 欄資料」
        d7 = fresh([("2026-03-03", True)], [srow("2026-03-03", "PFE")])
        old_cols = [c for c in L.FILL_COLS if c != "logged_at"]
        with open(os.path.join(d7, "fills.csv"), "w", encoding="utf-8-sig", newline="") as fo:
            fo.write(",".join(old_cols) + "\n")
            fo.write(",".join({"fill_id": "old1", "ticker": "AVGO", "engine": "E2", "open_date": "2026-02-02",
                               "open_px": "150", "shares": "2", "close_date": ""}.get(c, "") for c in old_cols) + "\n")
        fill("PFE", 50.0, 2, 46.0, "2026-03-04", d7)
        f7 = L.read(d7, "fills.csv", L.FILL_COLS)
        check("記錄簿:舊版 fills.csv(冇 logged_at)自動升級,有備份,舊行保留,新行讀得返(CRO N-12)",
              list(f7.columns) == L.FILL_COLS and len(f7) == 2 and f7["ticker"].tolist() == ["AVGO", "PFE"]
              and f7["logged_at"].iloc[0] == "" and f7["logged_at"].iloc[1] != ""
              and any(n.startswith("fills.csv.bak-") for n in os.listdir(d7)) and len(L.open_fills(d7)) == 2)
        d8 = fresh([], [])
        with open(os.path.join(d8, "fills.csv"), "w", encoding="utf-8-sig", newline="") as fo:
            fo.write("fill_id,ticker,mystery\nx,AAA,1\n")
        try:
            L._append_rows(d8, "fills.csv", L.FILL_COLS, [{"fill_id": "y", "ticker": "BBB"}]); refused = False
        except SystemExit:
            refused = True
        check("記錄簿:檔案有唔識嘅欄位 → 拒絕寫入,檔案唔郁",
              refused and open(os.path.join(d8, "fills.csv"), encoding="utf-8-sig").read() == "fill_id,ticker,mystery\nx,AAA,1\n")
    finally:
        shutil.rmtree(tmpF, ignore_errors=True)

    # 8c) Tom 2026-11-24:掃描器 —— 未收市唔寫記錄簿;已持倉唔佔排名(合成數據,唔使上網)
    # CRO N-1(2026-11-25):財報查詢一律換走 —— 以前會真係上網查 15 隻股,
    # 撞正 MSFT 業績前後幾日 selftest 就會失敗,.bat 叫你「今日唔好交易」(假警報)。
    import daily_scan_v66 as D
    orig = (D.load, D.partial_bar_warning, D.G.get_next_earnings, L.DEFAULT_DIR)
    er_calls = []
    D.G.get_next_earnings = lambda tk: er_calls.append(tk)      # 回傳 None = 查唔到,唔上網
    D.load = lambda t, s_, dd, a_: ({k: (v if a_ is None else v[v.index <= a_]) for k, v in data.items()}, [])
    days = [d for d in data["SPY"].index[-200:]][::-1]
    found = None
    tmpS = tempfile.mkdtemp()
    try:
        for d0 in days[:80]:
            with contextlib.redirect_stdout(io.StringIO()):
                out = D.scan("syn", None, str(d0.date()), tmpS, dry_run=True, quiet=True)
            if out and out.get("live"):
                found = (d0, out); break
        check("掃描器:合成數據搵到有 live 訊號嘅日子(下面幾項嘅前提)", found is not None)
        if found:
            d0, out = found
            D.load = lambda t, s_, dd, a_: ({k: v[v.index <= d0] for k, v in data.items()}, [])
            D.partial_bar_warning = lambda: True
            with contextlib.redirect_stdout(io.StringIO()):
                o2 = D.scan("yf", None, None, tmpS, dry_run=False, quiet=True)
            check("掃描器:開市中(未收市)→ 有訊號都唔寫記錄簿、唔寫心跳",
                  o2 is not None and len(o2["rows"]) > 0 and not os.path.exists(os.path.join(tmpS, "signals.csv"))
                  and not os.path.exists(os.path.join(tmpS, "runs.csv")))
            tk0 = out["live"][0]["ticker"]
            L._append_rows(tmpS, "fills.csv", L.FILL_COLS, [{"fill_id": "x", "ticker": tk0, "engine": "E2",
                                                            "open_date": "2020-01-01", "close_date": ""}])
            D.partial_bar_warning = lambda: False
            with contextlib.redirect_stdout(io.StringIO()):
                o3 = D.scan("yf", None, None, tmpS, dry_run=True, quiet=True)
            ranks = [r["rank"] for r in o3["live"]]
            check("掃描器:已持倉嘅股唔佔排名(同 lab 一樣跳過)",
                  tk0 not in [r["ticker"] for r in o3["live"]] and tk0 in [r["ticker"] for r in o3["held_signals"]]
                  and ranks == list(range(1, len(ranks) + 1)))
            check("掃描器:selftest 冇上網查財報(查詢已被攔截)", len(er_calls) > 0)

            # CRO C-4r:收市後正式掃描 → 寫訊號 + 一行心跳;再跑唔會重複
            for _ in range(2):
                with contextlib.redirect_stdout(io.StringIO()):
                    D.scan("yf", None, None, tmpS, dry_run=False, quiet=True)
            rr = L.read(tmpS, "runs.csv", L.RUN_COLS)
            check("掃描器:正式掃描寫一行心跳(bull=True),再跑唔重複",
                  len(rr) == 1 and rr["bull"].iloc[0] == "True" and rr["bar_date"].iloc[0] == str(d0.date()))
            # 熊市日:冇訊號都要有心跳(CRO F1 嘅根源)
            tmpB = os.path.join(tmpS, "bear")

            def bear_load(t, s_, dd, a_):
                out_ = {k: v[v.index <= d0].copy() for k, v in data.items()}
                out_["SPY"].loc[out_["SPY"].index[-1], "Close"] *= 0.5        # 將 SPY 壓落 MA200 之下
                return out_, []
            D.load = bear_load
            with contextlib.redirect_stdout(io.StringIO()):
                ob = D.scan("yf", None, None, tmpB, dry_run=False, quiet=True)
            rr = L.read(tmpB, "runs.csv", L.RUN_COLS)
            check("掃描器:熊市日都寫心跳(bull=False),唔寫訊號",
                  ob is not None and ob["bull"] is False and len(rr) == 1 and rr["bull"].iloc[0] == "False"
                  and rr["bar_date"].iloc[0] == str(d0.date())
                  and not os.path.exists(os.path.join(tmpB, "signals.csv")))

            # CRO C-3r:歷史重跑 / CSV 唔可以寫正式記錄簿(用臨時資料夾扮正式記錄簿,唔掂你真嘅 ledger/)
            liveL = os.path.join(tmpS, "live_ledger")
            L.DEFAULT_DIR = liveL
            D.load = lambda t, s_, dd, a_: ({k: (v if a_ is None else v[v.index <= a_]) for k, v in data.items()}, [])
            tries = [("syn", str(d0.date()), liveL), ("syn", str(d0.date()), os.path.join(liveL, "x", "..")),
                     ("csv", None, liveL)]
            try:
                os.makedirs(liveL, exist_ok=True)
                link = os.path.join(tmpS, "link_to_live")
                os.symlink(liveL, link, target_is_directory=True)
                tries.append(("syn", str(d0.date()), link))
            except (OSError, NotImplementedError):
                pass                                   # Windows 冇權限開 symlink → 跳過呢個變化
            for src_, asof_, led in tries:
                with contextlib.redirect_stdout(io.StringIO()):
                    D.scan(src_, None, asof_, led, dry_run=False, quiet=True)
            ctrl = os.path.join(tmpS, "test_ledger")      # 對照:同一個歷史重跑寫去測試資料夾 → 寫到
            with contextlib.redirect_stdout(io.StringIO()):
                D.scan("syn", None, str(d0.date()), ctrl, dry_run=False, quiet=True)
            check(f"掃描器:歷史重跑 / CSV 用 {len(tries)} 種路徑寫法都寫唔入正式記錄簿;寫去測試資料夾就得(CRO C-3r)",
                  not any(os.path.exists(os.path.join(liveL, f)) for f in ("signals.csv", "runs.csv"))
                  and os.path.exists(os.path.join(ctrl, "signals.csv")) and os.path.exists(os.path.join(ctrl, "runs.csv")))
    finally:
        D.load, D.partial_bar_warning, D.G.get_next_earnings, L.DEFAULT_DIR = orig
        shutil.rmtree(tmpS, ignore_errors=True)

    # 9) Telegram bot(離線)
    import telegram_bot_v66 as B
    check("bot:遮 token", "<TOKEN>" in B.redact("/bot123456789:AAEhBP0av18tR_ABCDEFGHIJKLMNOPQ/getMe")
          and "AAEhBP0av18tR" not in B.redact("/bot123456789:AAEhBP0av18tR_ABCDEFGHIJKLMNOPQ/getMe"))
    check("bot:遮 URL 編碼咗嘅 token(%3A)", "AAEhBP0av18tR" not in B.redact("/bot123456789%3AAAEhBP0av18tR_ABCDEFGHIJKLMNOPQ/getMe"))
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

    # 10) 2026-11-24 第二輪修正(CRO C-2、Tom F-8/F-9)
    txt_scan = None
    for tk in R.TICKERS:
        dfx = sig.get(tk)
        if dfx is None:
            continue
        for i in range(len(dfx) - 1, 200, -1):
            ev = S.evaluate(dfx.iloc[i])
            if S.on_path(ev, "scan") and not S.on_path(ev, "bt"):
                cut = dfx.index[i]
                txt_scan = B.analyze(tk, fetch=lambda t, c=cut: None if data.get(t) is None else data[t][data[t].index <= c],
                                     earnings="off")
                break
        if txt_scan:
            break
    check("bot:只有舊掃描器路徑嘅訊號 → 唔顯示交易計劃同股數(CRO C-2)",
          txt_scan is not None and "建議股數(" not in txt_scan and "── 交易計劃 ──" not in txt_scan
          and "只係舊掃描器路徑先有" in txt_scan)
    # CRO N-5(2026-11-25):今日條 bar 未收市 → bot 唔顯示交易計劃同股數(對照:同一日收市後會顯示)
    after_close = intraday = None
    for tk in R.TICKERS:
        dfx = sig.get(tk)
        if dfx is None or after_close:
            continue
        for i in range(len(dfx) - 1, 200, -1):
            if not S.on_path(S.evaluate(dfx.iloc[i]), "bt"):
                continue
            cut = dfx.index[i]
            f_ = lambda t, c=cut: None if data.get(t) is None else data[t][data[t].index <= c]
            ny = pd.Timestamp(cut.date()).tz_localize("America/New_York")
            t_close = B.analyze(tk, fetch=f_, earnings="off", now=ny + pd.Timedelta(hours=17))
            if "建議股數(" in t_close:
                after_close = t_close
                intraday = B.analyze(tk, fetch=f_, earnings="off", now=ny + pd.Timedelta(hours=11))
                break
    check("bot:未收市(紐約 11:00)→ 唔顯示交易計劃同股數;收市後(17:00)先顯示(CRO N-5)",
          after_close is not None and intraday is not None and "建議股數(" not in intraday
          and "── 交易計劃 ──" not in intraday and "未收市,收市後再查" in intraday)
    tmpE = tempfile.mkdtemp()
    try:
        L._append_rows(tmpE, "signals.csv", L.SIGNAL_COLS, [dict({c: "" for c in L.SIGNAL_COLS}, bar_date="2026-03-02",
                       ticker="EEE", path="bt", live=True, engine="E2", earnings_date="2026-03-10", guard_ok=True)])
        L._append_rows(tmpE, "fills.csv", L.FILL_COLS, [{"fill_id": "e", "ticker": "EEE", "engine": "E2",
                       "open_date": "2026-03-03", "open_px": 50, "shares": 2, "init_stop": 46,
                       "close_date": "2026-03-20", "close_px": 51, "flags": "", "notional_pct": 7.8}])
        with contextlib.redirect_stdout(io.StringIO()):
            rv = L.review(tmpE, today="2026-03-25")
        check("review:持倉期內有財報 → 記錄(CRO §5)", any("財報喺持倉期內" in n for n in rv["notes"]))
        check("review:V-1 未做 → S4 pending(唔會誤報)", rv["s4"]["state"] == "pending")
        # CRO N-18:review 唔計歷史重跑行(days_er=off)
        bp_row = dict({c: "" for c in L.SIGNAL_COLS}, bar_date="2026-03-04", path="bt", live=True, engine="E2",
                      guard_ok=True, size_A=0, size_Bp=1)
        L._append_rows(tmpE, "signals.csv", L.SIGNAL_COLS, [dict(bp_row, ticker="OFF", days_er="off")])
        with contextlib.redirect_stdout(io.StringIO()):
            rv1 = L.review(tmpE, today="2026-03-25")
        L._append_rows(tmpE, "signals.csv", L.SIGNAL_COLS, [dict(bp_row, ticker="LIV", days_er="9")])
        with contextlib.redirect_stdout(io.StringIO()):
            rv2 = L.review(tmpE, today="2026-03-25")
        check("review:歷史重跑行(off)唔計入 B′ 點數;live 行先計(CRO N-18)",
              rv1["bprime_only_signals"] == 0 and rv2["bprime_only_signals"] == 1)
    finally:
        shutil.rmtree(tmpE, ignore_errors=True)

    # 11) V6.6.4 —— Owner 2026-11-25 決定(N-11 停開新倉、N-13 舊倉、N-15 限價上限)+ CRO N-6/N-14/N-16/N-19/N-20/N-21
    import pc_check as P
    tmp11 = tempfile.mkdtemp()
    orig19 = (D.load, D.partial_bar_warning, D.G.bar_still_open, D.G.get_next_earnings, C.SWITCH_DATE)
    try:
        def srow11(day, tk, **kw):
            r = {c: "" for c in L.SIGNAL_COLS}
            r.update(bar_date=day, ticker=tk, path="bt", live=True, engine="E2", score=0.8, close=50, stop=46,
                     guard_ok=True, size_A=2, size_Bp=2, size_D=3, rank=1, source="yf", asof=False)
            r.update(kw); return r

        def led(runs, rows):
            d = tempfile.mkdtemp(dir=tmp11)
            L.append_signals(rows, d)
            for rn in runs:
                day, bull = rn[0], rn[1]
                L.append_run({"bar_date": day, "bull": bull, "live_path": "bt",
                              "source": rn[2] if len(rn) > 2 else "yf", "asof": rn[3] if len(rn) > 3 else False}, d)
            return d

        def fill11(d, tk, px, sh, st, day, engine="E2", legacy=False):
            a = types.SimpleNamespace(action="open", ticker=tk, price=px, shares=sh, stop=st, engine=engine,
                                      date=day, fees=0.0, reason=None, target=None, legacy=legacy)
            with contextlib.redirect_stdout(io.StringIO()):
                L.cmd_fill(a, d)
            f = L.read(d, "fills.csv", L.FILL_COLS)
            return f[f["ticker"] == tk].iloc[-1]

        # ---- N-11:未解釋 S2 → 停開新倉 ----
        d11 = led([("2026-03-03", True), ("2026-03-04", True)], [srow11("2026-03-04", "BBB")])
        r1 = fill11(d11, "OLD1", 50, 2, 46, "2026-03-04")                 # 冇訊號 → S2
        r2 = fill11(d11, "BBB", 50, 2, 46, "2026-03-05")                  # 有 live 訊號,但有未解釋 S2
        check("N-11:有未解釋 S2 → 下一筆開倉標 S2「未解釋 S2 期間開新倉」(訊號本身冇問題)",
              "S2" in r1["flags"] and "未解釋 S2 期間開新倉" in r2["flags"] and "冇 live 訊號" not in r2["flags"])
        hold1 = L.uncleared_s2(d11)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                L.cmd_s2_clear(types.SimpleNamespace(fill_id=r1["fill_id"], cro_note="explained"), d11)
            refused = False
        except SystemExit:
            refused = True
        with contextlib.redirect_stdout(io.StringIO()):
            L.cmd_s2_clear(types.SimpleNamespace(fill_id=r1["fill_id"],
                                                 cro_note="reports/risk/2026-03-06-s2-old1.md 2026-03-06"), d11)
        hold2 = L.uncleared_s2(d11)
        with contextlib.redirect_stdout(io.StringIO()):
            rv11 = L.review(d11, today="2026-03-10")
        check("N-11:s2-clear 要 CRO 文件路徑+日期;clear 咗嗰筆唔再擋,其他照擋;review 分開列",
              refused and len(hold1) == 2 and hold2 == [f"{r2['fill_id']}(BBB)"]
              and any(b.startswith("S2:BBB") for b in rv11["breaches"]) and not any(b.startswith("S2:OLD1") for b in rv11["breaches"])
              and any("已向 CRO 解釋" in n and "OLD1" in n for n in rv11["notes"]))
        rec_h = {"engine": "E2", "ticker": "ZZZ", "score": 0.8, "close": 50.0, "stop": 46.0, "risk_pct": 8.0,
                 "size_live": 2, "notional_live": 100.0, "days_er": 9, "spec_flag": "✅", "rank": 1, "limit_max": 50.5}
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            D._print([((0,), rec_h)], [], [], set(), d11, {})
        out_h = buf.getvalue()
        check("N-11:掃描器 ① —— 有未解釋 S2 → 停開新倉,唔顯示股數同限價",
              "停開新倉" in out_h and "股數 2" not in out_h and "限價上限 $" not in out_h)
        d_ok = led([], [])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            D._print([((0,), rec_h)], [], [], set(), d_ok, {})
        check("N-11 / N-15:冇 S2 → ① 照常顯示股數同限價上限", "股數 2" in buf.getvalue() and "限價上限 $50.50" in buf.getvalue())
        check("N-26:① 落單指示有「開市價 ≤ 系統止蝕 → 唔買」(CRO C-8 修訂)", "開市價 ≤ 系統止蝕 → 唔買" in buf.getvalue())

        # bot:有未解釋 S2 → 唔顯示計劃(對照:同一隻、同一日,冇 S2 就顯示)
        bot_hold = bot_free = None
        for tk in R.TICKERS:
            dfx = sig.get(tk)
            if dfx is None or bot_free:
                continue
            for i in range(len(dfx) - 1, 200, -1):
                if not S.on_path(S.evaluate(dfx.iloc[i]), "bt"):
                    continue
                cut = dfx.index[i]
                f_ = lambda t, c=cut: None if data.get(t) is None else data[t][data[t].index <= c]
                ny = pd.Timestamp(cut.date()).tz_localize("America/New_York") + pd.Timedelta(hours=17)
                t_free = B.analyze(tk, fetch=f_, earnings="off", now=ny, ledger_dir=d_ok)
                if "建議股數(" in t_free:
                    bot_free = t_free
                    bot_hold = B.analyze(tk, fetch=f_, earnings="off", now=ny, ledger_dir=d11)
                    break
        check("N-26:bot 計劃有「開市價 ≤ 止蝕 → 唔買」", bot_free is not None and "開市價 ≤ 止蝕" in bot_free)
        check("N-11:bot —— 有未解釋 S2 → 唔顯示計劃同股數;冇就顯示(連限價上限)",
              bot_free is not None and "限價上限" in bot_free and bot_hold is not None
              and "建議股數(" not in bot_hold and "停開新倉" in bot_hold)

        # ---- N-13:--legacy 舊倉 ----
        d13 = led([("2026-03-03", True)], [srow11("2026-03-03", "PFE")])
        lg = fill11(d13, "AVGO", 293.69, 2, 270.0, "2026-02-02", engine=None, legacy=True)
        check("N-13:--legacy → 唔標「冇 live 訊號」,標 legacy;超上限同風險照 S2(CRO 唔豁免)",
              "legacy" in lg["flags"] and "冇 live 訊號" not in lg["flags"] and "超上限" in lg["flags"]
              and "風險>1%" in lg["flags"] and lg["engine"] == "LEGACY" and lg["source_path"] == "legacy")
        ko = fill11(d13, "KO", 60.0, 1, 57.0, "2026-02-03", engine=None, legacy=True)
        pf = fill11(d13, "PFE", 50.0, 2, 46.0, "2026-03-04")
        check("N-13:細嘅舊倉冇 S2、唔受停開新倉影響;舊倉佔倉位(之後開第3倉 → S2)",
              ko["flags"] == "legacy" and "S2:已有2倉" in pf["flags"])
        C.SWITCH_DATE = "2026-03-01"
        try:
            fill11(d13, "MSFT", 400.0, 1, 380.0, "2026-03-05", engine=None, legacy=True); blocked13 = False
        except SystemExit:
            blocked13 = True
        C.SWITCH_DATE = orig19[4]
        check("N-13:轉用日之後唔准用 --legacy", blocked13)
        x_av = L.open_fills(d13).set_index("ticker").loc["AVGO"]
        x_av = types.SimpleNamespace(ticker="AVGO", **x_av.to_dict())
        check("N-13:④ 舊倉顯示「唔屬於系統」,唔計系統移動止損",
              "舊倉(唔屬於系統)" in D.trailing_line(x_av, {"AVGO": synth(n=60)}))

        # ---- N-15:限價上限 ----
        check("N-15:限價上限 —— 收市+1% 封頂($50/$46/2股 → $50.50)", Z.max_limit(50, 46, 2, "E2") == 50.5)
        check("N-15:限價上限 —— 10% 上限封頂($42.50/$41/3股 → $42.73)", Z.max_limit(42.5, 41, 3, "E2") == 42.73)
        l1 = Z.max_limit(20, 18, 6, "E1", target=24.1)
        check("N-15:引擎一限價上限保住 R ≥ 2($20/$18/止盈$24.10 → $20.03)",
              l1 == 20.03 and (24.1 - l1) / (l1 - 18) >= 2)
        grid_ok = True
        for cl in (8.3, 19.9, 37.2, 55.0, 99.9, 127.0):
            for sp in (0.02, 0.05, 0.09, 0.14):
                st = round(cl * (1 - sp), 2)
                n = Z.size(cl, st, "E2")["shares"]
                if n < 1:
                    continue
                lm = Z.max_limit(cl, st, n, "E2")
                if lm is None or Z.size(lm, st, "E2")["shares"] < n or lm > cl * 1.01 + 1e-9:
                    grid_ok = False
                elif lm < int(cl * 1.01 * 100) / 100 and Z.size(round(lm + 0.01, 2), st, "E2")["shares"] >= n:
                    grid_ok = False                                       # 仲可以再高一仙 → 唔係最高
        check("N-15:限價上限 = 「仲買得到同樣股數」嘅最高價(24 個組合)", grid_ok)
        d15 = led([("2026-03-03", True)], [srow11("2026-03-03", "LIM", close=42.5, stop=41, size_A=3)])
        f_at = fill11(d15, "LIM", 42.73, 3, 41.0, "2026-03-04")
        d15b = led([("2026-03-03", True)], [srow11("2026-03-03", "LIM", close=42.5, stop=41, size_A=3)])
        f_over = fill11(d15b, "LIM", 42.74, 3, 41.0, "2026-03-04")
        check("N-15:喺限價上限成交 → 冇 S2;高一仙 → S2(上限 / 股數)", "S2" not in f_at["flags"] and "S2" in f_over["flags"])

        # ---- V6.6.5:CRO N-24(日期)、N-25(s2-clear 文件)、N-28(測試檔指紋)----
        def fill_raw(d, **kw):
            base = dict(action="open", ticker="DTX", price=50.0, shares=2, stop=46.0, engine="E2", date=None,
                        fees=0.0, reason=None, target=None, legacy=False)
            base.update(kw)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    L.cmd_fill(types.SimpleNamespace(**base), d)
                return "ok"
            except SystemExit as e:
                return f"refused:{e}"
        d24 = led([("2026-03-03", True)], [srow11("2026-03-03", "DTX")])
        sw_keep = C.SWITCH_DATE
        C.SWITCH_DATE = "2026-03-01"                       # 已經過咗(而家係 2026-11 之後)
        r_back = fill_raw(d24, ticker="OLDX", legacy=True, engine=None, date="2026-02-01")
        C.SWITCH_DATE = sw_keep
        check("N-24:--date 格式錯 / 將來日子 / --legacy 冇日期 / 轉用之後倒填日期 → 全部拒絕",
              fill_raw(d24, date="2026/03/04").startswith("refused")
              and fill_raw(d24, date="2099-01-01").startswith("refused")
              and fill_raw(d24, ticker="LGX", legacy=True, engine=None, date=None).startswith("refused")
              and r_back.startswith("refused") and fill_raw(d24, date="2026-03-04") == "ok")
        d25 = led([("2026-03-03", True)], [])
        r25 = fill11(d25, "NOSIG", 50, 2, 46, "2026-03-04")          # 冇訊號 → S2
        def clear(note):
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    L.cmd_s2_clear(types.SimpleNamespace(fill_id=r25["fill_id"], cro_note=note), d25)
                return True
            except SystemExit:
                return False
        check("N-25:s2-clear 拒絕:日期早過交易、將來日期、冇 .md 文件路徑;接受:交易之後嘅真日期",
              not clear("reports/risk/2026-03-01-x.md 2026-03-01") and not clear("reports/risk/2099-01-01-x.md 2099-01-01")
              and not clear("reports/risk/ 2026-03-06") and clear("reports/risk/2026-03-06-nosig.md 2026-03-06"))
        check("N-28:電腦檢查報告有三個測試檔嘅指紋",
              re.fullmatch(r"tests selftest\.py=[0-9a-f]{12} parity_check\.py=[0-9a-f]{12} pc_check\.py=[0-9a-f]{12}",
                           P.test_hashes()) is not None)

        # ---- 審計 X-1:非預設戶口金額(HK$4,497 = 11-25 唯讀讀取嘅淨值)—— 倉位、限價上限、fill 檢查都跟住變 ----
        acct_keep = C.ACCOUNT_HKD
        C.ACCOUNT_HKD = 4497.0
        try:
            sm = (Z.size(50, 46, "E2")["shares"], Z.size(60, 57, "E2")["shares"], Z.max_limit(50, 46, 1, "E2"))
            dx = led([("2026-03-03", True)], [srow11("2026-03-03", "SML", size_A=1)])
            fx = fill11(dx, "SML", 50.0, 2, 46.0, "2026-03-04")
        finally:
            C.ACCOUNT_HKD = acct_keep
        check("X-1:戶口 HK$4,497 → $50/$46 得 1 股、$60 股 0 股、限價上限 $50.50;買 2 股 → S2(超上限 / 股數)",
              sm == (1, 0, 50.5) and "S2" in fx["flags"])

        # ---- N-16:只信 live 心跳 / 訊號 ----
        dc = led([("2026-03-03", True, "csv")], [srow11("2026-03-03", "PFE")])
        da = led([("2026-03-03", True, "yf", True)], [srow11("2026-03-03", "PFE")])
        ds = led([("2026-03-03", True)], [srow11("2026-03-03", "PFE", asof=True)])
        check("N-16:CSV 心跳、歷史重跑心跳、歷史重跑訊號 → 全部唔算(S2)",
              "none:冇掃描記錄" in fill11(dc, "PFE", 50, 2, 46, "2026-03-04")["flags"]
              and "none:冇掃描記錄" in fill11(da, "PFE", 50, 2, 46, "2026-03-04")["flags"]
              and "冇 live 訊號" in fill11(ds, "PFE", 50, 2, 46, "2026-03-04")["flags"])

        # ---- N-14:臨時休市 ----
        check("N-14:2025-01-09(國殤日休市)唔當交易日:01-08 → 01-10 中間 0 日;01-07 → 01-10 中間 1 日",
              L.nyse_sessions_between("2025-01-08", "2025-01-10") == 0
              and L.nyse_sessions_between("2025-01-07", "2025-01-10") == 1)

        # ---- N-19:掃描器用同 bot 一樣嘅「未收市」規則;N-6:記錄設定 ----
        D.load = lambda t, s_, dd, a_: ({k: v for k, v in data.items()}, [])
        D.partial_bar_warning = lambda: False
        D.G.get_next_earnings = lambda tk: None
        D.G.bar_still_open = lambda *a, **k: True
        t19 = tempfile.mkdtemp(dir=tmp11)
        with contextlib.redirect_stdout(io.StringIO()):
            D.scan("yf", None, None, t19, dry_run=False, quiet=True)
        D.G.bar_still_open = lambda *a, **k: False
        t19b = tempfile.mkdtemp(dir=tmp11)
        with contextlib.redirect_stdout(io.StringIO()):
            D.scan("yf", None, None, t19b, dry_run=False, quiet=True)
        rr19 = L.read(t19b, "runs.csv", L.RUN_COLS)
        check("N-19:最後一條 bar 係今日而未收市(例如盤前)→ 唔寫記錄簿同心跳;收咗市就寫",
              not os.path.exists(os.path.join(t19, "runs.csv")) and not os.path.exists(os.path.join(t19, "signals.csv"))
              and len(rr19) == 1)
        sg19 = L.read(t19b, "signals.csv", L.SIGNAL_COLS)
        check("N-6 / N-16:掃描行記錄 source、asof、戶口金額、模式、關卡",
              rr19["source"].iloc[0] == "yf" and rr19["asof"].iloc[0] == "False" and rr19["account_hkd"].iloc[0] != ""
              and rr19["gates"].iloc[0].startswith("G1=") and (not len(sg19) or (sg19["account_hkd"] != "").all()))

        # ---- N-20 / N-21:檔尾冇換行、淨係 BOM ----
        d20 = tempfile.mkdtemp(dir=tmp11)
        with open(os.path.join(d20, "fills.csv"), "w", encoding="utf-8-sig", newline="") as fo:
            fo.write(",".join(L.FILL_COLS) + "\r\n"
                     + ",".join({"fill_id": "x1", "ticker": "AVGO"}.get(c, "") for c in L.FILL_COLS))
        L._append_rows(d20, "fills.csv", L.FILL_COLS, [{"fill_id": "x2", "ticker": "PFE"}])
        check("N-20:檔尾冇換行 → 補換行先加,兩行都喺度",
              L.read(d20, "fills.csv", L.FILL_COLS)["ticker"].tolist() == ["AVGO", "PFE"])
        d21 = tempfile.mkdtemp(dir=tmp11)
        with open(os.path.join(d21, "runs.csv"), "wb") as fo:
            fo.write(b"\xef\xbb\xbf\r\n")
        L.append_run({"bar_date": "2026-03-03", "bull": True, "source": "yf"}, d21)
        rr21 = L.read(d21, "runs.csv", L.RUN_COLS)
        check("N-21:淨係 BOM / 空行嘅檔 → 讀得、備份後當新檔",
              len(rr21) == 1 and list(rr21.columns) == L.RUN_COLS and any(".bak-" in n for n in os.listdir(d21)))

        # ---- N-6 升級:V6.6.3 格式嘅三個檔(L-010:用上一版嘅檔測)----
        d6 = tempfile.mkdtemp(dir=tmp11)
        newc = {"signals.csv": {"source", "asof", "account_hkd", "cap_mode", "gates"},    # V6.6.3 冇呢啲欄
                "runs.csv": {"asof", "account_hkd", "cap_mode", "gates"},
                "fills.csv": {"account_hkd", "cap_mode", "gates"}}
        for name, cols, row in (
                ("signals.csv", L.SIGNAL_COLS, srow11("2026-03-03", "OLDS")),
                ("runs.csv", L.RUN_COLS, {"bar_date": "2026-03-04", "bull": "True", "source": "yf"}),
                ("fills.csv", L.FILL_COLS, {"fill_id": "2026-02-02_OLDF", "ticker": "OLDF", "engine": "E2",
                                            "open_date": "2026-02-02", "open_px": "20", "shares": "1",
                                            "init_stop": "19", "close_date": "2026-02-10", "flags": ""})):
            oc = [c for c in cols if c not in newc[name]]
            with open(os.path.join(d6, name), "w", encoding="utf-8-sig", newline="") as fo:
                fo.write(",".join(oc) + "\r\n" + ",".join(str(row.get(c, "")) for c in oc) + "\r\n")
        L.append_signals([srow11("2026-03-04", "NEW")], d6)
        nf = fill11(d6, "NEW", 50, 2, 46, "2026-03-05")      # 讀舊版 runs.csv(冇 asof 欄)都唔可以死
        s6, f6 = L.read(d6, "signals.csv", L.SIGNAL_COLS), L.read(d6, "fills.csv", L.FILL_COLS)
        check("N-6:V6.6.3 格式記錄簿 → 自動升級,舊行保留,新行有戶口金額同關卡,fill 照常判斷",
              list(s6.columns) == L.SIGNAL_COLS and s6["ticker"].tolist() == ["OLDS", "NEW"]
              and list(f6.columns) == L.FILL_COLS and f6["ticker"].tolist() == ["OLDF", "NEW"]
              and nf["account_hkd"] == str(C.ACCOUNT_HKD) and nf["gates"].startswith("G1=") and "S2" not in nf["flags"])

        # ---- 電腦檢查(pc_check.py):淨係測純函數,唔可以喺 selftest 入面再跑 selftest ----
        home = os.path.expanduser("~")
        red = P.redact(f"{home}{os.sep}Desktop{os.sep}v6.6 bot 123456789:AAEhBP0av18tR_ABCDEFGHIJKLMNOPQ")
        check("電腦檢查:報告將用戶路徑變 ~、遮住似 token 嘅字串",
              home not in red and "~" in red and "AAEhBP0av18tR" not in red)
        inv = P.ledger_inventory(d11)
        check("電腦檢查:記錄簿清單(檔案、行數、未解釋 S2)",
              ("fills.csv", 2) in inv["files"] and inv["uncleared_s2"] == hold2)
        src_pc = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pc_check.py"), encoding="utf-8").read()
        check("電腦檢查:唔讀 token 檔、唔改設定檔", ".swing_bot_token" not in src_pc and "json.dump" not in src_pc
              and "owner_settings.json\", \"w" not in src_pc)
        bat2 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "電腦檢查_v66.bat"), "rb").read().decode("utf-8")
        check("電腦檢查_v66.bat:冇半形括號、失敗 goto 停、CRLF、冇 BOM",
              "(" not in bat2 and ")" not in bat2 and "if errorlevel 1 goto FAILED" in bat2
              and bat2.count("\r\n") == bat2.count("\n") and not bat2.startswith("﻿"))
    finally:
        D.load, D.partial_bar_warning, D.G.bar_still_open, D.G.get_next_earnings, C.SWITCH_DATE = orig19
        shutil.rmtree(tmp11, ignore_errors=True)



if __name__ == "__main__":
    main()
