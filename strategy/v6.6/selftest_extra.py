# -*- coding: utf-8 -*-
"""V6.6 額外自我測試(2026-11-27 健康檢查加)—— 雲端跑,唔使你部電腦跑
=====================================================================
點解有呢個檔:2026-11-27 嘅「突變測試」(故意改壞代碼,睇 selftest 捉唔捉到)
23 個突變捉到 13 個;下面每一項測試對應一個捉唔到嘅突變(M05、M09、M12、M14、M16–M21)。

點解唔加入 selftest.py:selftest.py 嘅指紋(da356fb483a3)寫咗喺 results/release_stamp.txt,
你部電腦嘅電腦檢查會對照;而家改佢,你手上 V6.6.9 嗰包嘅「153 項過」同指紋就對唔上。
呢個檔唔改任何規則代碼(規則指紋 2b7b62182068 不變),只係測試現有代碼。
下次出新版本時,呢度嘅測試會併入 selftest.py。

用法:python selftest_extra.py      (合成數據,唔上網,唔寫你嘅 ledger/)
報告:reports/quant/2026-11-27-v66-9-health-check.md
"""
import contextlib
import io
import os
import shutil
import sys
import tempfile
import types

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config_v66 as C            # noqa: E402
import rules_v642 as R            # noqa: E402
import signals_v66 as S           # noqa: E402
import sizing_v66 as Z            # noqa: E402
import guardrails_v66 as G        # noqa: E402
import ledger_v66 as L            # noqa: E402
import daily_scan_v66 as D        # noqa: E402
import notify_v66 as N            # noqa: E402
from selftest import synth        # noqa: E402  (只借合成數據函數;import 唔會跑 selftest)

FAILS = []


def check(name, cond):
    print(("  ✅ " if cond else "  ❌ ") + name)
    if not cond:
        FAILS.append(name)


def main():
    print(f"V6.6 selftest_extra(規則指紋 {C.fingerprint()})")
    C.ACCOUNT_HKD = float(C.DEFAULT_SETTINGS["account_hkd"])           # 同 selftest 一樣:預期數按 HK$10,000、上限 A
    C.CAP_MODE, C.B_PRIME_ENABLED, C._B_PRIME_RAW = "A", False, False
    acct_usd = C.ACCOUNT_HKD / C.USD_HKD

    # X01(M05):限價上限 —— 收市價都買唔到咁多股 → 冇限價
    check("X01 限價上限:收市價買唔到 99 股 → None;買 2 股 → $50.50",
          Z.max_limit(50.0, 46.0, 99, "E2") is None and Z.max_limit(50.0, 46.0, 2, "E2") == 50.50)

    # X02(M09):引擎一止蝕上限 15%(V6.3 護欄1)喺 on_path 擋
    e1 = {"score": 0.6, "stop": 85.0, "target": 130.0, "r": 2.5, "risk_pct": 15.0, "rsi2": 20.0,
          "obv_div": False, "strong": False}
    ok15 = S.on_path({"e1": dict(e1), "e2": None}, "bt")
    no155 = S.on_path({"e1": dict(e1, risk_pct=15.5), "e2": None}, "bt")
    check("X02 引擎一:止蝕 15.0% → 有訊號;15.5% → 擋", ok15 is not None and no155 is None)

    # X03(M12):財報 0–5 日內擋,第 6 日唔擋
    df_small = synth(n=200)
    today = pd.Timestamp.now().normalize()
    blk = [not G.check("X", df_small, 5.0, earnings_ts=today + pd.Timedelta(days=d))["ok"] for d in (0, 4, 5)]
    ok6 = G.check("X", df_small, 5.0, earnings_ts=today + pd.Timedelta(days=6))["ok"]
    check("X03 財報護欄:0、4、5 日 → 擋;6 日 → 唔擋", all(blk) and ok6)

    # 合成數據(同 selftest 一樣嘅種子)
    data = {tk: synth(seed=k + 2, drift=0.0008 + 0.0002 * (k % 3), start=20 + 7 * k)
            for k, tk in enumerate(R.TICKERS)}
    data["SPY"] = synth(seed=99, drift=0.0007, vol=0.009, start=400)

    tmp = tempfile.mkdtemp()
    orig = (D.load, D.partial_bar_warning, D.G.get_next_earnings)
    try:
        D.G.get_next_earnings = lambda tk: None
        D.partial_bar_warning = lambda: False

        # X04(M14):今日最多開幾個 = 2 − 持倉數
        rec = {"ticker": "ZZZ", "engine": "E2", "tier": "", "rank": 1, "score": 0.8, "close": 50.0, "stop": 46.0,
               "target": "", "r": "", "risk_pct": 8.0, "days_er": 30, "spec_flag": "✅", "size_live": 2,
               "notional_live": 100.0, "limit_max": 50.5}
        base = {"bull": True, "bar_date": data["SPY"].index[-1], "gap": 3.0, "failed": [], "data": data,
                "live": [rec], "held_signals": [], "s2_hold": []}
        led0 = tempfile.mkdtemp(dir=tmp)
        m0 = N.compose_morning(base, led0)
        led1 = tempfile.mkdtemp(dir=tmp)
        tk1 = R.TICKERS[0]
        L._append_rows(led1, "fills.csv", L.FILL_COLS, [{"fill_id": "h1", "ticker": tk1, "engine": "E2",
                                                       "open_date": str(data[tk1].index[-30].date()),
                                                       "open_px": float(data[tk1]["Close"].iloc[-30]),
                                                       "init_stop": float(data[tk1]["Close"].iloc[-30]) * 0.9,
                                                       "close_date": ""}])
        m1 = N.compose_morning(base, led1)
        check("X04 訊息:冇持倉 → 今日最多開 2 個;1 個持倉 → 今日最多開 1 個",
              "今日最多開 2 個" in m0 and "今日最多開 1 個" in m1)

        # X05、X06(M16、M17):fill 時名義上限 10% 同每筆風險 1%(+5% 容差)
        def fill(folder, tk, px, sh, st):
            a = types.SimpleNamespace(action="open", ticker=tk, price=px, shares=sh, stop=st, engine="E2",
                                      date="2026-03-04", fees=0.0, reason=None, target=None)
            with contextlib.redirect_stdout(io.StringIO()):
                L.cmd_fill(a, folder)
            f = L.read(folder, "fills.csv", L.FILL_COLS)
            return f[f["ticker"] == tk]["flags"].iloc[-1]
        fa = tempfile.mkdtemp(dir=tmp)
        f_ok = fill(fa, "AAA", 50.0, 2, 46.0)                    # 7.8%、風險 $8
        fb = tempfile.mkdtemp(dir=tmp)
        f_nom = fill(fb, "BBB", 50.0, 3, 46.0)                   # 11.7%、風險 $12(< $13.46)
        fc = tempfile.mkdtemp(dir=tmp)
        f_rsk = fill(fc, "CCC", 50.0, 2, 40.0)                   # 7.8%、風險 $20(> $13.46)
        check(f"X05 fill:名義 11.7% → S2 名義超上限;7.8% → 冇(戶口 US${acct_usd:.2f})",
              "S2:名義11.7%超上限" in f_nom and "名義" not in f_ok)
        check("X06 fill:風險 $20(> 1% × 1.05 = $13.46)→ S2 風險>1%;$8 → 冇",
              "S2:風險>1%" in f_rsk and "風險>1%" not in f_ok and "風險>1%" not in f_nom)

        # X07、X08(M18、M19):牛熊 = SPY 收市 vs 200 日平均(唔係 150 日,冇折讓)
        def scan_with(spy):
            D.load = lambda t, s_, dd, a_: ({**data, "SPY": spy}, [])
            with contextlib.redirect_stdout(io.StringIO()):
                return D.scan("syn", None, None, tempfile.mkdtemp(dir=tmp), dry_run=True, quiet=True)
        spy = data["SPY"].copy()
        ma200 = float(spy["Close"].iloc[-200:].mean())
        spy_m = spy.copy()
        spy_m.iloc[-1, spy_m.columns.get_loc("Close")] = ma200 * 0.99     # 低過 MA200 1%(約;最後一日都入平均)
        o_m = scan_with(spy_m)
        check("X07 牛熊:SPY 收市低過 200 日平均 → 熊市", o_m is not None and o_m.get("bull") is False)
        o = scan_with(spy)
        ma = float(spy["Close"].rolling(200).mean().iloc[-1])
        gap_exp = (float(spy["Close"].iloc[-1]) - ma) / ma * 100
        check("X08 牛熊:gap 用 200 日平均計(獨立重算,差 < 0.001 個百分點)",
              o is not None and abs(float(o.get("gap")) - gap_exp) < 1e-3)
    finally:
        D.load, D.partial_bar_warning, D.G.get_next_earnings = orig
        shutil.rmtree(tmp, ignore_errors=True)

    # X09(M20):V6.4.2 鎖死門檻(改咗要 CRO 批 + 新指紋)
    check("X09 V6.4.2 門檻:評分 0.65 / 0.55,止蝕上限 12% / 15%,風險 1%,最多 2 倉,上限 A 10%",
          (R.TREND_SCORE_MIN, R.MR_SCORE_MIN, R.MAX_STOP_PCT_TREND, R.MAX_STOP_PCT_MR) == (0.65, 0.55, 12.0, 15.0)
          and (C.RISK_PCT, C.MAX_POSITIONS, C.CAP_A_PCT, C.MONTH_BREAKER_PCT) == (1.0, 2, 10.0, 10.0))

    # X10(M21):開市檢查三個結果 + 睇唔到唔落(CRO C-8 (a)、R-6 第 9 點)
    oc = N.OPEN_CHECK
    check("X10 開市檢查文字:未成交取消、≤止蝕即刻沽、高過止蝕即刻落止蝕單、睇唔到唔好預先落單",
          "未成交 → 取消張單" in oc and "成交價 ≤ 系統止蝕 → 即刻沽" in oc
          and "高過系統止蝕 → 即刻自己落止蝕單" in oc and "睇唔到就**唔好預先落單**" in oc)

    print()
    if FAILS:
        print(f"❌ {len(FAILS)} 項唔過")
        return 1
    print("全部通過")
    return 0


if __name__ == "__main__":
    sys.exit(main())
