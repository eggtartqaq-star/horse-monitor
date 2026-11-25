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
            L.append_run({"bar_date": day, "bull": bull, "live_path": "bt", "source": "test"}, folder or tmpF)
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

    print(f"\n{'全部通過' if not FAILS else f'{len(FAILS)} 項失敗'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
