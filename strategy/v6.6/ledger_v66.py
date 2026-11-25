# -*- coding: utf-8 -*-
"""
V6.6 影子記錄簿(shadow ledger)
================================
三個檔(喺 ledger/ 資料夾,唔會上載 GitHub):
  signals.csv  每日掃描自動寫入:每個訊號、兩條路徑、A/B′/D 三種倉位。只會加,唔會改。
  fills.csv    你真正落嘅單(用 fill 指令記,唔好用 Excel 改)
  results.csv  resolve 每次由頭計:每個訊號「如果做咗」嘅結果(用回測同一套出場規則)
  runs.csv     每次正式掃描嘅「心跳」(包括熊市、冇訊號嘅日子)—— fill 用嚟判斷訊號係咪今日有效
  s2_clearances.csv  已經向 CRO 解釋咗嘅 S2(未解釋嘅 S2 → 停開新倉,Owner 2026-11-25 決定,CRO N-11)

指令:
  python ledger_v66.py fill open  --ticker PFE --price 27.10 --shares 4 --stop 25.30 --engine E2 [--target X] [--date YYYY-MM-DD] [--fees 0]
  python ledger_v66.py fill close --ticker PFE --price 28.40 [--date YYYY-MM-DD] [--fees 0] [--reason 移動止損]
  python ledger_v66.py fill open --legacy --ticker AVGO --price 353.16 --shares 2 --stop 270 --date 2026-10-01
                                         # 轉用之前已經持有嘅倉(CRO N-13)
  python ledger_v66.py s2-clear --fill-id 2026-12-01_PFE --cro-note "reports/risk/2026-12-02-xxx.md 2026-12-02"
                                         # 向 CRO 解釋咗之後先記(CRO N-11)
  python ledger_v66.py resolve  [--source yf|csv --data DIR]
  python ledger_v66.py review
  python ledger_v66.py show
"""
import argparse
import csv
import os
import re
import shutil
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
import sizing_v66 as Z        # noqa: E402

DEFAULT_DIR = os.path.join(HERE, "ledger")

SIGNAL_COLS = ["logged_at", "bar_date", "ticker", "path", "live", "engine", "tier", "score", "close",
               "stop", "target", "r", "risk_pct", "breakout", "rsi2", "guard_ok", "guard_reason",
               "spec_flag", "days_er", "earnings_date", "size_A", "notional_A", "size_Bp", "rule_Bp",
               "size_D", "rank", "held", "partial_bar", "version", "fingerprint",
               "source", "asof", "account_hkd", "cap_mode", "gates"]          # CRO N-16、N-6(V6.6.4)
FILL_COLS = ["fill_id", "ticker", "engine", "source_path", "open_date", "open_px", "shares", "init_stop",
             "target", "open_fees", "close_date", "close_px", "close_fees", "close_reason",
             "notional_pct", "flags", "version", "fingerprint", "logged_at",
             "account_hkd", "cap_mode", "gates"]                                 # CRO N-6(V6.6.4)
# CRO C-4r(2026-11-25):每次正式掃描都寫一行,熊市/冇訊號都寫 —— 否則「上次掃描」會停喺舊日子
RUN_COLS = ["logged_at", "bar_date", "bull", "live_path", "source", "n_failed", "version", "fingerprint",
            "asof", "account_hkd", "cap_mode", "gates"]                          # CRO N-16、N-6(V6.6.4)
CLEAR_COLS = ["fill_id", "cleared_at", "cro_note", "version", "fingerprint"]   # CRO N-11(V6.6.4)
# CRO N-14:臨時休市(唔喺固定假期表)。2025-01-09 = 卡特總統國殤日;用 data/SPY.csv 核對過,1,200 個交易日只差呢一日。
NYSE_ADHOC_CLOSURES = ("2025-01-09",)


# ============================================================
# 讀寫(UTF-8;BOM 只喺新檔寫一次,Excel 開都唔會亂碼)
# ============================================================
def _path(folder, name, create=True):
    if create:
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, name)


def read(folder, name, cols):
    p = _path(folder, name, create=False)
    if not os.path.exists(p) or os.path.getsize(p) == 0 or not _header(p):
        return pd.DataFrame(columns=cols)                 # CRO N-21:空檔 / 淨係 BOM 都當冇資料
    df = pd.read_csv(p, encoding="utf-8-sig", dtype=str, keep_default_na=False)
    for c in cols:                                        # 舊版檔(未升級)讀落嚟都有齊欄位,冇嘅當空
        if c not in df.columns:
            df[c] = ""
    return df


def _migrate_header(p, cols):
    """CRO N-12(2026-11-25):舊版寫嘅檔欄位少過而家(例如 V6.6.1 嘅 fills.csv 冇 logged_at)。
    唔處理嘅話,新一行會多一欄 → 之後每次讀都死,掃描器每個牛市日都話「掃描出錯」。
    做法:先備份,再補空欄,之後先加新行。有唔識嘅欄位 → 唔郁,停低。"""
    header = _header(p)
    if header == list(cols):
        return
    extra = [c for c in header if c not in cols]
    if extra:
        raise SystemExit(f"❌ {p} 有唔識嘅欄位 {extra} —— 冇改動。將呢個檔畀 AI 睇。")
    backup = f"{p}.bak-{datetime.now():%Y%m%d-%H%M%S}"
    shutil.copy2(p, backup)
    old = pd.read_csv(p, encoding="utf-8-sig", dtype=str, keep_default_na=False)
    _rewrite(os.path.dirname(p), os.path.basename(p), cols, old)
    added = [c for c in cols if c not in header]
    what = f"加咗 {added}" if added else "重新排列欄位"          # CRO N-23
    print(f"ℹ️ {os.path.basename(p)} 由舊版格式升級({what});備份:{backup}")


def _header(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return [h for h in next(csv.reader(f), []) if h.strip()]


def _append_rows(folder, name, cols, rows):
    p = _path(folder, name)
    new = not os.path.exists(p) or os.path.getsize(p) == 0
    if not new and not _header(p):
        # CRO N-21:有內容但冇表頭(例如淨係 BOM / 空行)→ 備份,當新檔
        shutil.copy2(p, f"{p}.bak-{datetime.now():%Y%m%d-%H%M%S}")
        new = True
    if not new:
        _migrate_header(p, cols)
        with open(p, "rb") as f:
            f.seek(-1, os.SEEK_END)
            last = f.read(1)
        if last != b"\n":
            # CRO N-20:最後一行冇換行(例如人手改過)→ 先補換行,否則新行會黐埋舊行,舊行靜靜雞唔見
            with open(p, "ab") as f:
                f.write(b"\r\n")
    with open(p, "w" if new else "a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
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


def append_run(row, folder=DEFAULT_DIR):
    """掃描心跳。冪等:同一 bar_date 只寫第一次。"""
    have = read(folder, "runs.csv", RUN_COLS)
    if len(have) and str(row["bar_date"]) in set(have["bar_date"]):
        return 0
    _append_rows(folder, "runs.csv", RUN_COLS, [row])
    return 1


def _nyse_calendar():
    from pandas.tseries.holiday import (AbstractHolidayCalendar, GoodFriday, Holiday, USLaborDay,
                                        USMartinLutherKingJr, USMemorialDay, USPresidentsDay,
                                        USThanksgivingDay, nearest_workday, sunday_to_monday)

    class NYSE(AbstractHolidayCalendar):
        rules = [Holiday("NewYear", month=1, day=1, observance=sunday_to_monday),
                 USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay,
                 Holiday("Juneteenth", month=6, day=19, start_date="2022-06-19", observance=nearest_workday),
                 Holiday("July4", month=7, day=4, observance=nearest_workday),
                 USLaborDay, USThanksgivingDay,
                 Holiday("Christmas", month=12, day=25, observance=nearest_workday)]
    return NYSE()


def nyse_sessions_between(d0, d1):
    """d0 同 d1 之間(兩邊都唔計)有幾多個 NYSE 交易日。
    只計固定假期;臨時休市(例如國殤日)會當交易日計 → 只會多報「過期」,唔會漏報。"""
    a = pd.Timestamp(d0) + pd.Timedelta(days=1)
    b = pd.Timestamp(d1) - pd.Timedelta(days=1)
    if b < a:
        return 0
    cbd = pd.offsets.CustomBusinessDay(calendar=_nyse_calendar())
    days = pd.date_range(a, b, freq=cbd)
    adhoc = {pd.Timestamp(d) for d in NYSE_ADHOC_CLOSURES}
    return int(sum(1 for d in days if d not in adhoc))


def open_fills(folder=DEFAULT_DIR):
    f = read(folder, "fills.csv", FILL_COLS)
    return f[f["close_date"] == ""] if len(f) else f


def uncleared_s2(folder=DEFAULT_DIR):
    """CRO N-11(Owner 2026-11-25 決定):有 S2 而未向 CRO 解釋(未 s2-clear)嘅交易 → 停開新倉。"""
    f = read(folder, "fills.csv", FILL_COLS)
    if not len(f):
        return []
    clr = read(folder, "s2_clearances.csv", CLEAR_COLS)
    done = set(clr["fill_id"]) if len(clr) else set()
    bad = f[f["flags"].str.contains("S2", regex=False) & ~f["fill_id"].isin(done)]
    return [f"{r.fill_id}({r.ticker})" for r in bad.itertuples()]


def _valid_cro_note(note, not_before=None, today=None):
    """CRO N-25(V6.6.5):要有 reports/risk/….md 路徑同一個真日期;日期唔可以早過嗰筆交易、唔可以係將來。
    (CRO 每次檢討會逐個對返真文件 —— 呢度只係擋明顯作假,唔係證明文件存在。)"""
    note = note or ""
    if not re.search(r"reports/risk/\S+\.md", note):
        return False
    dates = re.findall(r"\d{4}-\d{2}-\d{2}", note)
    if not dates:
        return False
    try:
        ds = [pd.Timestamp(d) for d in dates]
    except Exception:
        return False
    today = pd.Timestamp(today or pd.Timestamp.now(tz="America/New_York").strftime("%Y-%m-%d"))
    if any(d > today for d in ds):
        return False
    if not_before is not None and max(ds) < pd.Timestamp(not_before):
        return False
    return True


def _valid_date(d):
    """CRO N-24(V6.6.5):--date 一定要係 YYYY-MM-DD 嘅真日期,而且唔可以係將來(紐約日期)。"""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d or ""):
        return False
    try:
        ts = pd.Timestamp(d)
    except Exception:
        return False
    return ts <= pd.Timestamp(pd.Timestamp.now(tz="America/New_York").strftime("%Y-%m-%d"))


def cmd_s2_clear(a, folder):
    """記錄「呢筆 S2 已經向 CRO 解釋咗」。要寫 CRO 文件路徑同日期;唔會刪除 S2 標記(歷史照留)。"""
    f = read(folder, "fills.csv", FILL_COLS)
    row = f[f["fill_id"] == a.fill_id] if len(f) else f
    if not len(row):
        sys.exit(f"❌ 搵唔到 fill_id {a.fill_id}(用 python ledger_v66.py show 睇)")
    if "S2" not in row["flags"].iloc[0]:
        sys.exit(f"❌ {a.fill_id} 冇 S2,唔使 clear")
    if a.fill_id not in [x.split("(")[0] for x in uncleared_s2(folder)]:
        sys.exit(f"❌ {a.fill_id} 已經 clear 咗")
    if not _valid_cro_note(a.cro_note, not_before=row["open_date"].iloc[0]):
        sys.exit("❌ --cro-note 要寫 CRO 文件路徑(reports/risk/….md)同日期(YYYY-MM-DD);"
                 "日期唔可以早過嗰筆交易,亦唔可以係將來")
    _append_rows(folder, "s2_clearances.csv", CLEAR_COLS, [{
        "fill_id": a.fill_id, "cleared_at": datetime.now().strftime("%Y-%m-%d %H:%M"), "cro_note": a.cro_note,
        "version": C.VERSION, "fingerprint": C.fingerprint()}])
    left = uncleared_s2(folder)
    print(f"✅ 已記錄:{a.fill_id} 嘅 S2 已向 CRO 解釋。" + (f" 仲有未解釋:{', '.join(left)}" if left else " 冇其他未解釋 S2,可以再開新倉。"))


# ============================================================
# fill:記錄真實交易 + 即時檢查違規(S2)
# ============================================================
def cmd_fill(a, folder):
    fills = read(folder, "fills.csv", FILL_COLS)
    # Tom 2026-11-24:預設用「紐約日期」。bar_date 係紐約日期;你喺香港朝早(紐約前一晚)記錄,
    # 用香港日期會將開倉日記遲一日 → 移動止損漏咗入場日,訊號來源亦會對錯 bar。
    if a.date and not _valid_date(a.date):
        sys.exit(f"❌ --date {a.date} 唔啱:要係 YYYY-MM-DD(紐約日期),而且唔可以係將來")
    ny_today = pd.Timestamp.now(tz="America/New_York").strftime("%Y-%m-%d")
    today = a.date or ny_today
    acct_usd = C.ACCOUNT_HKD / C.USD_HKD
    if a.action == "open":
        if len(fills) and ((fills["ticker"] == a.ticker) & (fills["close_date"] == "")).any():
            sys.exit(f"❌ {a.ticker} 已經有未平倉記錄")
        legacy = bool(getattr(a, "legacy", False))
        if legacy and C.SWITCH_DATE and (today >= C.SWITCH_DATE or ny_today >= C.SWITCH_DATE):
            # CRO N-24:轉用日之後一律唔准再用 --legacy(就算 --date 填返轉用前都唔得,防倒填日期)
            sys.exit(f"❌ --legacy 只限轉用日({C.SWITCH_DATE})之前記錄、之前開嘅倉;之後開嘅倉要用正常 fill")
        if legacy and not a.date:
            sys.exit("❌ --legacy 一定要用 --date 填返買入日(YYYY-MM-DD)")
        hold = [] if legacy else uncleared_s2(folder)     # 記錄舊倉唔算「開新倉」
        flags = []
        if hold:
            flags.append(f"S2:未解釋 S2 期間開新倉({', '.join(hold)})")
        n_open = int((fills["close_date"] == "").sum()) if len(fills) else 0
        if n_open >= C.MAX_POSITIONS:
            flags.append(f"S2:已有{n_open}倉(最多{C.MAX_POSITIONS})")
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
        runs = read(folder, "runs.csv", RUN_COLS)
        if len(runs):
            # CRO N-16:只信 live(yfinance)而唔係歷史重跑嘅心跳
            runs = runs[(runs["source"] == "yf") & (runs["asof"] != "True")]
        if len(sig):
            sig = sig[(sig["asof"] != "True") & (sig["days_er"] != "off")]
        src = "none"
        # CRO C-4r(2026-11-25):「上次掃描」由 runs.csv(心跳)決定,唔再由 signals.csv 估。
        # 熊市日、冇訊號日、冇跑掃描嘅日子 signals.csv 都冇行 → 舊方法會將幾日前嘅訊號當今日有效。
        prior = runs[runs["bar_date"] < today] if len(runs) else runs
        last_bar = prior["bar_date"].max() if len(prior) else None
        pl = sig.iloc[0:0] if len(sig) else sig
        if legacy:
            src = "legacy"                                # CRO N-13:轉用前已持有;唔查訊號,但照查名義同風險
        elif last_bar is None:
            src = "none:冇掃描記錄(runs.csv),要先跑 daily_scan_v66"
        elif not (prior[prior["bar_date"] == last_bar]["bull"] == "True").any():
            src = f"bear:上次掃描{last_bar}係熊市,系統停手"
        elif nyse_sessions_between(last_bar, today) >= 1:
            src = f"stale:上次掃描{last_bar},之後漏咗{nyse_sessions_between(last_bar, today)}個交易日"
        elif len(sig):
            pl = sig[(sig["ticker"] == a.ticker) & (sig["bar_date"] == last_bar)]
            if not len(pl):
                had = ((sig["ticker"] == a.ticker) & (sig["bar_date"] < today)).any()
                src = f"{'stale' if had else 'none'}:上次掃描{last_bar}冇呢隻"
        if len(pl):
            src = "live" if (pl["live"] == "True").any() else "scan_only"
            lv = pl[pl["live"] == "True"]
            if len(lv) and not (lv["guard_ok"] == "True").any():
                # Tom 2026-11-24:交易路徑有訊號,但被護欄擋咗(財報/止蝕過闊)—— 唔係「可以交易」
                flags.append(f"S2:護欄擋咗({lv['guard_reason'].iloc[0]})")
            if len(lv):
                # Tom 2026-11-24(CRO C-4b):系統話 A 買唔起,或者自己將止蝕收緊去「造」出股數 → 違規
                if (lv["size_A"] == "0").all() and "B'例外" not in flags:
                    flags.append("S2:系統A倉位=0(買唔起)")
                sys_stop = pd.to_numeric(lv["stop"], errors="coerce").max()
                # CRO C-4r:容差 1 仙(以前係 max(1仙, 0.5%),會令自訂收緊止蝕「造」多一股)
                if pd.notna(sys_stop) and a.stop > sys_stop + 0.01 + 1e-9:
                    flags.append(f"S2:止蝕{a.stop}高過系統止蝕{sys_stop}(自訂收緊)")
                # CRO C-4r:股數唔可以多過「成交價 + 系統止蝕」按現行模式計出嚟嘅股數
                if pd.notna(sys_stop) and not (lv["size_A"] == "0").all():
                    sys_sh = Z.size(a.price, sys_stop, lv["engine"].iloc[0], Z.live_mode())["shares"]
                    if a.shares > sys_sh:
                        flags.append(f"S2:股數{a.shares:g}多過系統{sys_sh}股(按成交價${a.price}、系統止蝕${sys_stop}計)")
            if (pl["live"] == "True").any():
                rk = pd.to_numeric(pl[pl["live"] == "True"]["rank"], errors="coerce").min()
                # 空位 = 2 − 今日之前已開嘅倉(同日開兩筆唔會誤報)
                n_before = int(((fills["close_date"] == "") & (fills["open_date"] < today)).sum()) if len(fills) else 0
                if pd.notna(rk) and rk > C.MAX_POSITIONS - n_before:
                    flags.append(f"留意:揀咗第{int(rk)}名(當時得{max(C.MAX_POSITIONS - n_before, 0)}個空位)")
        if legacy:
            flags.append("legacy")
        elif src != "live":
            flags.append(f"S2:冇 live 訊號({src})")
        row = {"fill_id": f"{today}_{a.ticker}", "ticker": a.ticker, "engine": a.engine or "LEGACY", "source_path": src,
               "open_date": today, "open_px": a.price, "shares": a.shares, "init_stop": a.stop,
               "target": a.target or "", "open_fees": a.fees, "notional_pct": round(pct, 2),
               "flags": ";".join(flags), "version": C.VERSION, "fingerprint": C.fingerprint(),
               "logged_at": datetime.now().strftime("%Y-%m-%d %H:%M"),     # CRO N-10:--date 補記都睇到幾時記
               **C.settings_record()}                                          # CRO N-6
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
    sig = sig[(sig["guard_ok"] == "True") & (sig["partial_bar"] != "True")]   # Tom:未收市嘅舊行唔計
    if not getattr(a, "include_asof", False):
        sig = sig[(sig["days_er"] != "off") & (sig["asof"] != "True")]   # CRO C-3r / N-16:歷史重跑行唔計
    if not len(sig):
        print("ledger 未有可計嘅訊號。"); return None
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
    if len(sig):
        sig = sig[(sig["days_er"] != "off") & (sig["asof"] != "True")]   # CRO C-3r / N-16:唔計入時鐘同點數
    res = read(folder, "results.csv", [])
    fills = read(folder, "fills.csv", FILL_COLS)
    clr = read(folder, "s2_clearances.csv", CLEAR_COLS)
    cleared = set(clr["fill_id"]) if len(clr) else set()
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
        # Tom 2026-11-24:用「第一次記錄嘅日子」(logged_at)計 6 個月,--asof 歷史行唔會令時鐘提早
        t0 = pd.to_datetime(sig["logged_at"], errors="coerce").min() if len(sig) else pd.NaT
        if pd.isna(t0) and len(sig):
            t0 = pd.Timestamp(sig["bar_date"].min())
        months = (today - t0.normalize()).days / 30.4 if len(sig) else 0
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
                if x.fill_id in cleared:
                    out["notes"].append(f"S2(已向 CRO 解釋):{x.ticker} {fl}")
                else:
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
            print(f"  已平倉 {len(closed)} 筆,扣費淨盈虧 US${net:.2f}(資料,唔係 S4)")
        # 持倉期間有冇財報(CRO §5 earnings log)—— 只知道「訊號嗰日」查到嘅下次財報日
        for x in f.itertuples():
            ed = _signal_earnings(sig, x.ticker, x.open_date)
            end = x.close_date or today.strftime("%Y-%m-%d")
            if ed and x.open_date <= ed <= end:
                out["notes"].append(f"財報喺持倉期內:{x.ticker} {x.open_date}→{end},財報 {ed}")
    else:
        print("  未有真實交易記錄(fills.csv)")

    # ---- S4(CRO 定義):V-1 真實收費下,淨 EV ≤ 0 → 呢個戶口規模下,任何上限都唔應該交易 ----
    out["s4"] = s4_status(sig, res)
    print(f"  S4 收費關卡:{out['s4']['text']}")
    if out["s4"]["state"] == "fail":
        out["breaches"].append("S4:真實收費下淨 EV ≤ 0")

    for b in out["breaches"]:
        print(f"  🔴 {b}")
    for n in out["notes"]:
        print(f"  ℹ️ {n}")
    if any(b.startswith("S4") for b in out["breaches"]):
        print("\n  ★ S4:真實收費食晒優勢 → 呢個戶口規模下,任何名義上限都唔應該交易。通知 CRO。")
    elif out["breaches"]:
        # CRO N-11(Owner 2026-11-25 決定):A 之下「返去 A」冇作用 → 停開新倉,直至向 CRO 解釋
        back = "即刻返去 A(10%)," if Z.live_mode() != "A" else ""
        print(f"\n  ★ 有違規 → {back}停開新倉,通知 CRO。向 CRO 解釋之後用 "
              "python ledger_v66.py s2-clear --fill-id … --cro-note … 記錄,先可以再開新倉。")
    elif len(fills):
        print("  ✅ 冇違規")
    return out


def _signal_earnings(sig, ticker, open_date):
    """搵入場前最近一個 live 訊號記錄嘅下次財報日(YYYY-MM-DD)或 None。"""
    if not len(sig):
        return None
    s = sig[(sig["ticker"] == ticker) & (sig["bar_date"] < open_date) & (sig["earnings_date"] != "")]
    if not len(s):
        return None
    return s.sort_values("bar_date")["earnings_date"].iloc[-1]


def s4_status(sig, res):
    """CRO S4/V-1:真實收費(owner_settings.json real_fee)下,交易路徑每筆淨 EV。
    回測版:python lab.py --mode feecheck --fee-min X --fee-bp Y(V-1 之後跑一次,結果畀 CRO)。
    呢度係前向版:用記錄簿已完結嘅交易路徑訊號,按 A 倉位名義值扣真實收費。"""
    fee = C.REAL_FEE or {}
    if not C.GATES.get("V1_真實收費已核") or fee.get("bp_per_side") is None or fee.get("min_per_side_usd") is None:
        return {"state": "pending", "text": "未能檢查 —— 要先做 V-1(微牛成交單據),再喺 owner_settings.json 填 real_fee"}
    if not len(res) or not len(sig):
        return {"state": "pending", "text": "未有已完結訊號"}
    r = res[(res["mode"] == "per_trade") & (res["path"] == C.LIVE_PATH) & (res["reason"] != "持倉中")].copy()
    sz = sig[sig["path"] == C.LIVE_PATH][["ticker", "bar_date", "notional_A"]].rename(columns={"bar_date": "sig_date"})
    r = r.merge(sz, on=["ticker", "sig_date"], how="left")
    r["notional_A"] = pd.to_numeric(r["notional_A"], errors="coerce")
    r = r[r["notional_A"] > 0]
    if len(r) < 30:
        return {"state": "pending", "text": f"已完結而買得起嘅交易路徑訊號 {len(r)}/30,未夠計"}
    cost_pct = 2 * float(fee["bp_per_side"]) / 100 + 2 * float(fee["min_per_side_usd"]) / r["notional_A"] * 100
    ev = (r["gross_pct"].astype(float) - cost_pct).mean()
    state = "fail" if ev <= 0 else "pass"
    return {"state": state, "text": f"前向 {len(r)} 個訊號,真實收費下每筆淨 EV {ev:+.2f}% → {'❌ 唔過' if state == 'fail' else '✅ 過'}"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["fill", "resolve", "review", "show", "s2-clear"])
    ap.add_argument("action", nargs="?", choices=["open", "close"])
    ap.add_argument("--ledger", default=DEFAULT_DIR)
    ap.add_argument("--ticker"); ap.add_argument("--price", type=float); ap.add_argument("--shares", type=float)
    ap.add_argument("--stop", type=float); ap.add_argument("--target", type=float)
    ap.add_argument("--engine", choices=["E1", "E2"]); ap.add_argument("--date")
    ap.add_argument("--legacy", action="store_true", help="轉用前已持有嘅倉(CRO N-13)")
    ap.add_argument("--fill-id"); ap.add_argument("--cro-note")
    ap.add_argument("--fees", type=float, default=0.0); ap.add_argument("--reason")
    ap.add_argument("--source", choices=["yf", "csv"], default="yf")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    a = ap.parse_args()
    C.check_config()
    if a.cmd == "fill":
        if a.action is None or not a.ticker or a.price is None:
            sys.exit("用法:fill open|close --ticker X --price P [...]")
        if a.action == "open" and (a.shares is None or a.stop is None or (a.engine is None and not a.legacy)):
            sys.exit("開倉要 --shares --stop --engine(舊倉用 --legacy,唔使 --engine;止蝕用你自己嘅)")
        a.ticker = a.ticker.upper()
        cmd_fill(a, a.ledger)
    elif a.cmd == "s2-clear":
        if not a.fill_id or not a.cro_note:
            sys.exit("用法:s2-clear --fill-id YYYY-MM-DD_TICKER --cro-note \"reports/risk/... YYYY-MM-DD\"")
        cmd_s2_clear(a, a.ledger)
    elif a.cmd == "resolve":
        cmd_resolve(a, a.ledger)
    elif a.cmd == "review":
        review(a.ledger)
    else:
        print(read(a.ledger, "signals.csv", SIGNAL_COLS).tail(30).to_string())
        print(read(a.ledger, "fills.csv", FILL_COLS).to_string())
        hold = uncleared_s2(a.ledger)
        print(f"\n未向 CRO 解釋嘅 S2:{', '.join(hold) if hold else '冇'}" + ("  → 停開新倉(CRO N-11)" if hold else ""))


if __name__ == "__main__":
    main()
