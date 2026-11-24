# -*- coding: utf-8 -*-
"""
V6.6 影子記錄簿(shadow ledger)
================================
三個檔(喺 ledger/ 資料夾,唔會上載 GitHub):
  signals.csv  每日掃描自動寫入:每個訊號、兩條路徑、A/B′/D 三種倉位。只會加,唔會改。
  fills.csv    你真正落嘅單(用 fill 指令記,唔好用 Excel 改)
  results.csv  resolve 每次由頭計:每個訊號「如果做咗」嘅結果(用回測同一套出場規則)

指令:
  python ledger_v66.py fill open  --ticker PFE --price 27.10 --shares 4 --stop 25.30 --engine E2 [--target X] [--date YYYY-MM-DD] [--fees 0]
  python ledger_v66.py fill close --ticker PFE --price 28.40 [--date YYYY-MM-DD] [--fees 0] [--reason 移動止損]
  python ledger_v66.py resolve  [--source yf|csv --data DIR]
  python ledger_v66.py review
  python ledger_v66.py show
"""
import argparse
import csv
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config_v66 as C        # noqa: E402
import rules_v642 as R        # noqa: E402

DEFAULT_DIR = os.path.join(HERE, "ledger")

SIGNAL_COLS = ["logged_at", "bar_date", "ticker", "path", "live", "engine", "tier", "score", "close",
               "stop", "target", "r", "risk_pct", "breakout", "rsi2", "guard_ok", "guard_reason",
               "spec_flag", "days_er", "earnings_date", "size_A", "notional_A", "size_Bp", "rule_Bp",
               "size_D", "rank", "held", "partial_bar", "version", "fingerprint"]
FILL_COLS = ["fill_id", "ticker", "engine", "source_path", "open_date", "open_px", "shares", "init_stop",
             "target", "open_fees", "close_date", "close_px", "close_fees", "close_reason",
             "notional_pct", "flags", "version", "fingerprint"]


# ============================================================
# 讀寫(UTF-8;BOM 只喺新檔寫一次,Excel 開都唔會亂碼)
# ============================================================
def _path(folder, name, create=True):
    if create:
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, name)


def read(folder, name, cols):
    p = _path(folder, name, create=False)
    if not os.path.exists(p):
        return pd.DataFrame(columns=cols)
    return pd.read_csv(p, encoding="utf-8-sig", dtype=str, keep_default_na=False)


def _append_rows(folder, name, cols, rows):
    p = _path(folder, name)
    new = not os.path.exists(p)
    with open(p, "a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({c: ("" if r.get(c) is None else r.get(c)) for c in cols})


def _rewrite(folder, name, cols, df):
    p = _path(folder, name)
    tmp = p + ".tmp"
    df.reindex(columns=cols).to_csv(tmp, index=False, encoding="utf-8-sig")
    os.replace(tmp, p)


def append_signals(rows, folder=DEFAULT_DIR):
    """冪等:(bar_date, ticker, path) 已經有就唔再寫。回傳實際寫入數目。"""
    have = read(folder, "signals.csv", SIGNAL_COLS)
    keys = set(zip(have["bar_date"], have["ticker"], have["path"])) if len(have) else set()
    fresh = [r for r in rows if (str(r["bar_date"]), r["ticker"], r["path"]) not in keys]
    if fresh:
        _append_rows(folder, "signals.csv", SIGNAL_COLS, fresh)
    return len(fresh)


def open_fills(folder=DEFAULT_DIR):
    f = read(folder, "fills.csv", FILL_COLS)
    return f[f["close_date"] == ""] if len(f) else f


# ============================================================
# fill:記錄真實交易 + 即時檢查違規(S2)
# ============================================================
def cmd_fill(a, folder):
    fills = read(folder, "fills.csv", FILL_COLS)
    today = a.date or datetime.now().strftime("%Y-%m-%d")
    acct_usd = C.ACCOUNT_HKD / C.USD_HKD
    if a.action == "open":
        if len(fills) and ((fills["ticker"] == a.ticker) & (fills["close_date"] == "")).any():
            sys.exit(f"❌ {a.ticker} 已經有未平倉記錄")
        flags = []
        notional = a.price * a.shares
        pct = notional / acct_usd * 100
        if pct > C.CAP_A_PCT + 1e-9:
            exception_ok = (C.B_PRIME_ENABLED and a.engine == "E2" and a.shares == 1
                            and pct <= C.CAP_BPRIME_PCT + 1e-9
                            and (a.price - a.stop) <= C.ACCOUNT_HKD * C.RISK_PCT / 100 / C.USD_HKD + 1e-9)
            flags.append("B'例外" if exception_ok else f"S2:名義{pct:.1f}%超上限")
        if (a.price - a.stop) * a.shares > C.ACCOUNT_HKD * C.RISK_PCT / 100 / C.USD_HKD * 1.05:
            flags.append("S2:風險>1%")
        sig = read(folder, "signals.csv", SIGNAL_COLS)
        src = "none"
        if len(sig):
            prior = sig[(sig["ticker"] == a.ticker) & (sig["bar_date"] < today)]
            if len(prior):
                last_bar = prior["bar_date"].max()
                pl = prior[prior["bar_date"] == last_bar]
                src = "live" if (pl["live"] == "True").any() else "scan_only"
                if (pl["live"] == "True").any():
                    rk = pd.to_numeric(pl[pl["live"] == "True"]["rank"], errors="coerce").min()
                    if pd.notna(rk) and rk > C.MAX_POSITIONS:
                        flags.append(f"留意:揀咗第{int(rk)}名")
        if src != "live":
            flags.append(f"S2:冇 live 訊號({src})")
        row = {"fill_id": f"{today}_{a.ticker}", "ticker": a.ticker, "engine": a.engine, "source_path": src,
               "open_date": today, "open_px": a.price, "shares": a.shares, "init_stop": a.stop,
               "target": a.target or "", "open_fees": a.fees, "notional_pct": round(pct, 2),
               "flags": ";".join(flags), "version": C.VERSION, "fingerprint": C.fingerprint()}
        _append_rows(folder, "fills.csv", FILL_COLS, [row])
        print(f"✅ 已記錄開倉 {a.ticker} {a.shares}股 @ {a.price}(名義 {pct:.1f}%)" +
              (f"  ⚠️ {';'.join(flags)}" if flags else ""))
    else:
        m = (fills["ticker"] == a.ticker) & (fills["close_date"] == "") if len(fills) else None
        if m is None or not m.any():
            sys.exit(f"❌ 搵唔到 {a.ticker} 嘅未平倉記錄")
        i = fills[m].index[0]
        fills.loc[i, ["close_date", "close_px", "close_fees", "close_reason"]] = [today, str(a.price), str(a.fees), a.reason or ""]
        _rewrite(folder, "fills.csv", FILL_COLS, fills)
        print(f"✅ 已記錄平倉 {a.ticker} @ {a.price}")


# ============================================================
# resolve:用回測同一個模擬器計每個訊號「如果做咗」嘅結果
# ============================================================
def _load_prices(tickers, source, data_dir):
    import lab
    return lab.load_csv(data_dir, tickers) if source == "csv" else lab.load_yf(tickers, period="5y")


def build_sig_from_ledger(sig_rows, data):
    """將 ledger 訊號砌成 lab.simulate 用嘅格式。價位按「最新收市 ÷ 記錄收市」重新縮放
    (派息/拆股會令歷史調整價變,呢度對返)。"""
    from indicators import calc_indicators
    out = {}
    for tk, g in sig_rows.groupby("ticker"):
        if tk not in data:
            continue
        df = calc_indicators(data[tk])
        recs = [{"route": "SKIP"}] * len(df)
        pos = {d.strftime("%Y-%m-%d"): k for k, d in enumerate(df.index)}
        for r in g.itertuples():
            k = pos.get(r.bar_date)
            if k is None:
                continue
            fresh = df["Close"].iloc[k]
            scale = fresh / float(r.close) if float(r.close) > 0 else 1.0
            if r.engine == "E1":
                e = {"kind": "MR", "score": float(r.score), "close": fresh, "atr": df["ATR"].iloc[k],
                     "low10": np.nan, "ma50": np.nan, "h60": np.nan, "rsi2": float(r.rsi2 or "nan"),
                     "plan": {"stop": float(r.stop) * scale, "target": float(r.target) * scale,
                              "r": float(r.r)}}
            else:
                e = {"kind": "TR", "score": float(r.score), "close": fresh, "atr": df["ATR"].iloc[k],
                     "brk": True}
            recs[k] = e
        df["sig"] = recs
        out[tk] = df
    return out


def cmd_resolve(a, folder):
    import lab
    from dataclasses import replace
    sig = read(folder, "signals.csv", SIGNAL_COLS)
    if not len(sig):
        print("ledger 未有訊號。"); return None
    sig = sig[sig["guard_ok"] == "True"]
    data = _load_prices(sorted(set(sig["ticker"])) + ["SPY"], a.source, a.data)
    first = pd.Timestamp(sig["bar_date"].min())
    rows = []
    for path in sorted(set(sig["path"])):
        built = build_sig_from_ledger(sig[sig["path"] == path], data)
        if not built:
            continue
        # 訊號喺記錄時已按路徑篩選好,呢度唔再加任何門檻
        base = dict(e2_breakout_gate=False, e1_strong_only=False)
        for mode, cfg in (("per_trade", replace(lab.PER_TRADE, **base)),
                          ("book_2slot", replace(lab.AS_TRADED, **base))):
            tr, _, _ = lab.simulate(built, cfg, start=first)
            if len(tr):
                tr = tr.assign(path=path, mode=mode)
                rows.append(tr)
    res = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    if len(res):
        for c in ("sig_date", "entry_date", "exit_date"):
            res[c] = pd.to_datetime(res[c]).dt.strftime("%Y-%m-%d")
        res.loc[res["reason"] == "數據結束", "reason"] = "持倉中"
    p = _path(folder, "results.csv")
    res.to_csv(p + ".tmp", index=False, encoding="utf-8-sig"); os.replace(p + ".tmp", p)
    print(f"✅ resolve 完成:{len(res)} 行 → {p}")
    return res


# ============================================================
# review:兩部分 —— 優勢(由影子記錄)同風險(由真實交易)
# ============================================================
def review(folder, today=None):
    today = pd.Timestamp(today or datetime.now().strftime("%Y-%m-%d"))
    sig = read(folder, "signals.csv", SIGNAL_COLS)
    res = read(folder, "results.csv", [])
    fills = read(folder, "fills.csv", FILL_COLS)
    out = {"breaches": [], "notes": []}
    print("=" * 64)
    print(f"V6.6 影子記錄檢討  |  {C.VERSION}  指紋 {C.fingerprint()}")
    print("=" * 64)

    # ---- 1. 優勢(唔受你有冇真係落單影響) ----
    if len(res):
        r = res[(res["mode"] == "per_trade") & (res["reason"] != "持倉中")].copy()
        r["net_pct"] = r["net_pct"].astype(float)
        print("\n【1】每個訊號「如果做咗」(回測同一套出場規則,10bp/邊成本)")
        g = r.groupby(["path", "engine"])["net_pct"].agg(["size", "mean"]).round(3)
        print(g.to_string() if len(g) else "  未有已完結訊號")
        e2 = r[(r["path"] == C.LIVE_PATH) & (r["engine"] == "E2")]
        months = (today - pd.Timestamp(sig["bar_date"].min())).days / 30.4 if len(sig) else 0
        out["closed_e2_live"] = len(e2)
        due = len(e2) >= 30 and months >= 6
        print(f"\n  檢討時間表:已完結引擎二(交易路徑)訊號 {len(e2)}/30,已記錄 {months:.1f}/6 個月 → "
              f"{'✅ 可以做第一次正式檢討' if due else '⏳ 未夠,唔好下結論'}")
    else:
        print("\n【1】未有 results.csv —— 先跑 python ledger_v66.py resolve")

    # ---- 2. 名義上限影子比較(CRO:100 筆前唔比較回報) ----
    if len(sig):
        live = sig[sig["live"] == "True"]
        bp = live[(live["size_A"] == "0") & (pd.to_numeric(live["size_Bp"], errors="coerce") >= 1)]
        out["bprime_only_signals"] = len(bp)
        print(f"\n【2】名義上限:A(10%)買唔到、B′(1股≤15%)買得到嘅交易路徑訊號:{len(bp)} 個")
        print("    ★ CRO 規定:累積夠 100 筆之前,唔比較 A / B′ / D 嘅回報。")

    # ---- 3. 風險(由真實交易) ----
    print("\n【3】真實交易風險檢查(S1–S4)")
    acct = C.ACCOUNT_HKD / C.USD_HKD
    if len(fills):
        f = fills.copy()
        for c in ("open_px", "shares", "close_px", "open_fees", "close_fees", "notional_pct"):
            f[c] = pd.to_numeric(f[c], errors="coerce").fillna(0.0)
        f["pnl"] = np.where(f["close_date"] != "", (f["close_px"] - f["open_px"]) * f["shares"]
                            - f["open_fees"] - f["close_fees"], np.nan)
        for x in f.itertuples():
            fl = x.flags or ""
            if "B'例外" in fl and pd.notna(x.pnl) and x.pnl < -0.02 * acct:
                out["breaches"].append(f"S1:{x.ticker} 例外倉蝕 {x.pnl:.2f}(>{0.02 * acct:.2f})")
            if "S2" in fl:
                out["breaches"].append(f"S2:{x.ticker} {fl}")
        closed = f[f["close_date"] != ""].copy()
        if len(closed):
            closed["month"] = closed["close_date"].str[:7]
            for m, g in closed.groupby("month"):
                if g["pnl"].sum() <= -C.MONTH_BREAKER_PCT / 100 * acct:
                    exc_open = f[(f["flags"].str.contains("B'例外")) & (f["open_date"].str[:7] <= m)
                                 & ((f["close_date"] == "") | (f["close_date"].str[:7] >= m))]
                    out["notes"].append(f"月熔斷 {m}:{g['pnl'].sum():.2f}")
                    if len(exc_open):
                        out["breaches"].append(f"S3:{m} 月熔斷時有例外倉")
            net = closed["pnl"].sum()
            print(f"  已平倉 {len(closed)} 筆,扣費淨盈虧 US${net:.2f}")
            if C.GATES.get("V1_真實收費已核") and len(closed) >= 10 and net <= 0:
                out["breaches"].append("S4:扣真實收費後淨盈虧 ≤ 0")
    else:
        print("  未有真實交易記錄(fills.csv)")
    if not C.GATES.get("V1_真實收費已核"):
        out["notes"].append("S4 未能檢查:V-1 真實收費未核(要一張微牛成交單據)")
    for b in out["breaches"]:
        print(f"  🔴 {b}")
    for n in out["notes"]:
        print(f"  ℹ️ {n}")
    if out["breaches"]:
        print("\n  ★ 有違規 → 即刻返去 A(10%),通知 CRO。測試期內唔可以爭拗。")
    elif len(fills):
        print("  ✅ 冇違規")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["fill", "resolve", "review", "show"])
    ap.add_argument("action", nargs="?", choices=["open", "close"])
    ap.add_argument("--ledger", default=DEFAULT_DIR)
    ap.add_argument("--ticker"); ap.add_argument("--price", type=float); ap.add_argument("--shares", type=float)
    ap.add_argument("--stop", type=float); ap.add_argument("--target", type=float)
    ap.add_argument("--engine", choices=["E1", "E2"]); ap.add_argument("--date")
    ap.add_argument("--fees", type=float, default=0.0); ap.add_argument("--reason")
    ap.add_argument("--source", choices=["yf", "csv"], default="yf")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    a = ap.parse_args()
    C.check_config()
    if a.cmd == "fill":
        if a.action is None or not a.ticker or a.price is None:
            sys.exit("用法:fill open|close --ticker X --price P [...]")
        if a.action == "open" and (a.shares is None or a.stop is None or a.engine is None):
            sys.exit("開倉要 --shares --stop --engine")
        a.ticker = a.ticker.upper()
        cmd_fill(a, a.ledger)
    elif a.cmd == "resolve":
        cmd_resolve(a, a.ledger)
    elif a.cmd == "review":
        review(a.ledger)
    else:
        print(read(a.ledger, "signals.csv", SIGNAL_COLS).tail(30).to_string())
        print(read(a.ledger, "fills.csv", FILL_COLS).to_string())


if __name__ == "__main__":
    main()
