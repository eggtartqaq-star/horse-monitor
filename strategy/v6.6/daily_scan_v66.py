# -*- coding: utf-8 -*-
"""
V6.6 每日掃描(取代 daily_strong_signals.py;舊檔留低做後備)
==============================================================
同 V6.4.2 嘅分別:
  1. 交易清單 = 回測驗證版規則(引擎二要「今日高 ≥ 20日高」,手冊第三節條件3)
  2. 舊掃描器版訊號照列出,但標明「只記錄,唔交易」
  3. 頂部印版本、指紋、路徑、名義上限模式 —— 一眼睇到跑緊邊個版本
  4. 每個訊號自動寫入影子記錄簿(ledger/signals.csv)
  5. 下載失敗會列出,唔會靜靜雞跳過
  6. 美股開市期間跑 → 警告「今日條 bar 未收市」

用法:
  python daily_scan_v66.py                         # 每日(收市後)
  python daily_scan_v66.py --dry-run               # 唔寫記錄簿
  python daily_scan_v66.py --source csv --data data --asof 2026-09-28   # 歷史重跑(財報檢查關閉)
"""
import argparse
import os
import platform
import sys
from datetime import datetime

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config_v66 as C        # noqa: E402
import guardrails_v66 as G    # noqa: E402
import ledger_v66 as L        # noqa: E402
import rules_v642 as R        # noqa: E402
import signals_v66 as S       # noqa: E402
import sizing_v66 as Z        # noqa: E402
from indicators import calc_indicators  # noqa: E402


def stamp(source):
    C.check_config()
    try:
        import yfinance as yf
        yfv = yf.__version__
    except Exception:
        yfv = "未裝"
    mode = Z.live_mode()
    lines = [
        "=" * 64,
        f"Swing {C.VERSION}  指紋 {C.fingerprint()}  |  {datetime.now():%Y-%m-%d %H:%M}",
        f"交易路徑: {C.LIVE_PATH}(回測驗證版)  影子路徑: {', '.join(C.SHADOW_PATHS)}(只記錄)",
        f"名義上限: {mode}({'10% 一律' if mode == 'A' else 'B′:引擎二1股≤15%'})  "
        f"B′ {'開' if C.B_PRIME_ENABLED else '關'}  |  每筆風險 {C.RISK_PCT}%  最多 {C.MAX_POSITIONS} 倉",
        f"未過關卡: {', '.join(C.gates_outstanding()) or '冇'}",
        f"Python {platform.python_version()}  pandas {pd.__version__}  yfinance {yfv}  數據: {source}",
        "=" * 64,
    ]
    print("\n".join(lines))


def partial_bar_warning():
    now = pd.Timestamp.now(tz="America/New_York")
    if now.weekday() < 5 and (now.hour, now.minute) >= (9, 30) and now.hour < 16:
        print("⚠️ 美股而家開緊市 —— 今日條 bar 未收市,訊號會變。收市後(香港時間朝早)再跑。")
        return True
    return False


def load(tickers, source, data_dir, asof):
    data, failed = {}, []
    if source == "csv":
        import lab
        data = lab.load_csv(data_dir, tickers)
        failed = [t for t in tickers if t not in data]
    else:
        import yfinance as yf
        for tk in tickers:
            try:
                df = yf.Ticker(tk).history(period="2y", auto_adjust=True)
                if df is None or df.empty:
                    failed.append(tk); continue
                df.index = df.index.tz_localize(None).normalize()
                data[tk] = df[["Open", "High", "Low", "Close", "Volume"]]
            except Exception as e:
                failed.append(f"{tk}({type(e).__name__})")
    if asof is not None:
        data = {k: v[v.index <= asof] for k, v in data.items()}
    return data, failed


def raw_factor(tk, d, source):
    """歷史 CSV 係拆股調整價;倉位要用當時真實價。live yfinance 嘅今日價本身就係真實價。"""
    if source != "csv":
        return 1.0
    import lab
    return lab.raw_factor(tk, d)


def scan(source="yf", data_dir=None, asof=None, ledger_dir=L.DEFAULT_DIR, dry_run=False, quiet=False):
    asof_ts = pd.Timestamp(asof) if asof else None
    asof_mode = asof_ts is not None
    partial = (not asof_mode and source == "yf" and partial_bar_warning())
    data, failed = load(R.TICKERS + ["SPY"], source, data_dir, asof_ts)
    if failed:
        print(f"⚠️ 下載失敗 {len(failed)} 隻(今日唔會出佢哋嘅訊號):{', '.join(failed)}")
    if "SPY" not in data:
        print("❌ 冇 SPY 數據,今日唔掃描。"); return None
    spy = data["SPY"].copy()
    spy["MA200"] = spy["Close"].rolling(200).mean()
    s = spy.iloc[-1]
    bar_date = spy.index[-1]
    if pd.isna(s["MA200"]):
        print("SPY MA200 數據不足,今日唔出訊號。"); return None
    is_bull = bool(s["Close"] > s["MA200"])
    gap = (s["Close"] - s["MA200"]) / s["MA200"] * 100
    print(f"\n市場環境({bar_date.date()}): {'牛市' if is_bull else '熊市'}(SPY 對 MA200 {gap:+.1f}%)")
    if not is_bull:
        print("熊市:系統停手,今日唔搵做多訊號。"); return {"bull": False, "rows": []}

    held = set(L.open_fills(ledger_dir)["ticker"])
    mode = Z.live_mode()          # Tom 2026-11-24:交易清單用 config 嘅模式(而家 = A);以前寫死 "A",開 B′ 都唔會生效
    rows, live, shadow_only, blocked, held_sigs = [], [], [], [], []
    for tk in R.TICKERS:
        df = data.get(tk)
        if df is None or len(df) < 100:
            continue
        ind = calc_indicators(df)
        row = ind.iloc[-1].copy()
        if ind.index[-1] != bar_date:
            print(f"⚠️ {tk} 最後一條 bar 係 {ind.index[-1].date()},唔係 {bar_date.date()} —— 跳過")
            continue
        row["bull"] = is_bull
        ev = S.evaluate(row)
        per_path = {p: S.on_path(ev, p) for p in (C.LIVE_PATH,) + C.SHADOW_PATHS}
        if not any(per_path.values()):
            continue
        any_sig = next(v for v in per_path.values() if v)
        g = G.check(tk, ind, any_sig["risk_pct"], asof_mode=asof_mode)
        f = raw_factor(tk, bar_date, source)
        for path, sg in per_path.items():
            if not sg:
                continue
            close = float(row["Close"])
            a_ = Z.size(close * f, sg["stop"] * f, sg["engine"], "A")
            bp = Z.size(close * f, sg["stop"] * f, sg["engine"], "B_PRIME")
            d_ = Z.size(close * f, sg["stop"] * f, sg["engine"], "D")
            tier = ""
            if sg["engine"] == "E1":
                plan = {"stop": sg["stop"], "target": sg["target"], "r": sg["r"]}
                tier = R.classify_mr_tier(row, sg["score"], plan,
                                          g["days_er"] if isinstance(g["days_er"], int) else None) or ""
            rec = {
                "logged_at": datetime.now().strftime("%Y-%m-%d %H:%M"), "bar_date": bar_date.strftime("%Y-%m-%d"),
                "ticker": tk, "path": path, "live": path == C.LIVE_PATH, "engine": sg["engine"], "tier": tier,
                "score": sg["score"], "close": round(close, 4), "stop": sg["stop"],
                "target": sg.get("target") or "", "r": sg.get("r", "") if sg["engine"] == "E1" else "",
                "risk_pct": round(float(sg["risk_pct"]), 2), "breakout": sg.get("breakout", ""),
                "rsi2": round(float(sg["rsi2"]), 2) if sg.get("rsi2") is not None and pd.notna(sg.get("rsi2")) else "",
                "guard_ok": g["ok"], "guard_reason": g["reason"], "spec_flag": g["flag"],
                "days_er": g["days_er"] if g["days_er"] is not None else "?",
                "earnings_date": g["earnings_date"].strftime("%Y-%m-%d") if isinstance(g["earnings_date"], pd.Timestamp) else "",
                "size_A": a_["shares"], "notional_A": a_["notional"], "size_Bp": bp["shares"], "rule_Bp": bp["rule"],
                "size_D": d_["shares"], "rank": "", "held": tk in held, "partial_bar": partial,
                "version": C.VERSION, "fingerprint": C.fingerprint(),
            }
            lv = bp if mode == "B_PRIME" else a_
            rec["size_live"], rec["notional_live"] = lv["shares"], lv["notional"]   # 只供顯示;記錄簿欄位不變
            rows.append(rec)
            if path == C.LIVE_PATH:
                if not g["ok"]:
                    blocked.append((tk, sg["engine"], g["reason"]))
                elif lv["shares"] < 1:
                    why = f"{'10% 上限' if mode == 'A' else 'B′'}/1%風險下買唔起1股(${close * f:.0f})"
                    blocked.append((tk, sg["engine"], why))
                elif tk in held:
                    # Tom 2026-11-24:lab.simulate 會跳過已持倉嘅股,所以佢唔可以佔排名
                    held_sigs.append(rec)
                else:
                    live.append((S.rank_key(sg), rec))
        if per_path.get("scan") and not per_path.get(C.LIVE_PATH):
            shadow_only.append(next(r for r in rows if r["ticker"] == tk and r["path"] == "scan"))

    live.sort(key=lambda x: x[0])
    for k, (_, rec) in enumerate(live, 1):
        rec["rank"] = k

    if not quiet:
        _print(live, shadow_only, blocked, held, ledger_dir, data, held_sigs)
    if asof_mode and not dry_run and os.path.abspath(ledger_dir) == os.path.abspath(L.DEFAULT_DIR):
        # Tom 2026-11-24(CRO C-3):歷史重跑唔可以寫入正式記錄簿(會污染 6 個月時鐘同 resolve)
        print("\nℹ️ 歷史重跑(--asof)唔寫正式記錄簿。要測試請加 --ledger 其他資料夾。")
    elif partial and not dry_run:
        # Tom 2026-11-24:記錄簿係「同一 (日期,代號,路徑) 只寫第一次」—— 未收市嘅數一寫入,
        # 收市後嘅正確數就永遠寫唔入。所以開市期間一律唔寫。
        print("\n⚠️ 今日條 bar 未收市 → 唔寫影子記錄簿。收市後再跑一次。")
    elif not dry_run:
        n = L.append_signals(rows, ledger_dir)
        print(f"\n影子記錄簿:新增 {n} 行 → {os.path.join(ledger_dir, 'signals.csv')}")
    return {"bull": True, "rows": rows, "live": [r for _, r in live], "shadow_only": shadow_only,
            "blocked": blocked, "held_signals": held_sigs, "bar_date": bar_date}


def _line(rec, rank_txt, tag=""):
    if rec["engine"] == "E2":
        return (f" {rank_txt} 引擎二 {rec['ticker']:5} 評分{rec['score']:.3f}  收市${rec['close']:.2f}  "
                f"初始止蝕${rec['stop']:.2f}(-{rec['risk_pct']:.1f}%)  股數 {rec['size_live']}(${rec['notional_live']:.0f})  "
                f"距財報 {rec['days_er']}  {rec['spec_flag']} {tag}")
    return (f" {rank_txt} 引擎一 {rec['ticker']:5} [{rec['tier']}] 評分{rec['score']:.3f}  收市${rec['close']:.2f}  "
            f"止蝕${rec['stop']:.2f} 止盈${rec['target']:.2f} R{rec['r']}  股數 {rec['size_live']}(${rec['notional_live']:.0f})  "
            f"距財報 {rec['days_er']}  {rec['spec_flag']} {tag}")


def _print(live, shadow_only, blocked, held, ledger_dir, data, held_sigs=()):
    print("\n" + "=" * 64)
    print("① 交易清單(回測驗證版)—— 按排名揀,最多 2 倉(扣返現有持倉)")
    print("=" * 64)
    if not live:
        print("今日冇訊號。空手係一種倉位。")
    for _, rec in live:
        print(_line(rec, f"#{rec['rank']}"))
    for rec in held_sigs:
        print(_line(rec, " — ", "持倉中(唔計排名,唔好加注)"))
    if live:
        print("  落單:聽日開市;開市價偏離收市 >1% → 重計 R/風險,唔達標放棄。成交後即刻設止蝕單。")
        print("  落單後記錄:python ledger_v66.py fill open --ticker X --price P --shares N --stop S --engine E2")
    print("\n② 舊掃描器版先有嘅訊號 —— 只記錄,唔交易")
    print("   " + (", ".join(f"{r['ticker']}({r['engine']})" for r in shadow_only) if shadow_only else "冇"))
    if blocked:
        print("\n③ 交易路徑被擋(學習用)")
        for tk, eng, why in blocked:
            print(f"   {tk:5} {eng}  {why}")
    of = L.open_fills(ledger_dir)
    if len(of):
        print("\n④ 你嘅持倉 —— 今日止蝕位")
        for x in of.itertuples():
            print("   " + trailing_line(x, data))


def trailing_line(x, data):
    df = data.get(x.ticker)
    if df is None:
        return f"{x.ticker}: 冇數據"
    stop = float(x.init_stop)
    if x.engine == "E2":
        ind = calc_indicators(df)
        since = ind[ind.index >= pd.Timestamp(x.open_date)]
        highest, atr = float(x.open_px), None
        for _, r in since.iterrows():
            if pd.notna(r["ATR"]) and r["ATR"] > 0:
                atr = r["ATR"]
            highest = max(highest, r["High"])
            if atr:
                stop = max(stop, highest - R.ATR_TRAIL_MULT * atr)
        return (f"{x.ticker} 引擎二  入${float(x.open_px):.2f}  最高${highest:.2f}  今日止蝕 ${stop:.2f}"
                f"(只升不降;收市 ${df['Close'].iloc[-1]:.2f})")
    days = (df.index >= pd.Timestamp(x.open_date)).sum()
    return (f"{x.ticker} 引擎一  入${float(x.open_px):.2f}  止蝕${stop:.2f}  止盈 {x.target or '?'}  "
            f"第 {days} 日 / 10(滿10日收市出)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["yf", "csv"], default="yf")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    ap.add_argument("--asof")
    ap.add_argument("--ledger", default=L.DEFAULT_DIR)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    stamp(a.source if not a.asof else f"{a.source} asof {a.asof}")
    scan(a.source, a.data, a.asof, a.ledger, a.dry_run)


if __name__ == "__main__":
    main()
