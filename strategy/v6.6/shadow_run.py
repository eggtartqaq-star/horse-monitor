# -*- coding: utf-8 -*-
"""
V6.6 雲端影子記錄(2026-11-27)—— 研究工具,唔係規則指紋嘅一部分
====================================================================
Owner 揀咗「雲端影子記錄」:每個美股交易日收市後,雲端用 Webull 唯讀日線跑一次同你部電腦一樣嘅掃描,
記低「系統會做咩」。用途:
  1. 累積真正嘅前向(樣本外)證據 —— 回測以外唯一嘅證據;
  2. 同你 Telegram(Yahoo 數據)對照:兩個數據源出嘅訊號、限價、止蝕一唔一致。

佢做嘅嘢:Webull 日線 JSON → CSV(暫存)→ daily_scan_v66.scan(csv)→ notify_v66.compose_morning(只砌文字)
  → 寫 shadow/YYYY-MM-DD.txt、shadow/shadow_log.csv、shadow/ledger/(影子記錄簿,唔係你嘅 ledger/)。
佢唔做嘅嘢(下面自我審計會檢查,違反就拒絕執行 —— CLAUDE.md 第 1 條「結構性控制」):
  唔傳 Telegram、唔讀 token、唔落單 / 改單 / 取消單、唔寫你嘅 ledger/。
財報檢查:CSV 模式一律 off(雲端冇 Yahoo)—— 所以影子清單可能包括你 Telegram 會因財報擋咗嘅股。

用法:
  python shadow_run.py --webull-json 檔1 檔2 檔3     (get_stock_bars 嘅 JSON 結果;每檔可以有幾隻股)
  python shadow_run.py --data 某個CSV資料夾           (Date,Open,High,Low,Close,Volume;測試用)
"""
import argparse
import csv
import json
import os
import pathlib
import re
import sys
import tempfile
from datetime import datetime, timezone

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FORBIDDEN = ("place_order", "modify_order", "cancel_order", "unlock_trade", "send_message", "send_text",
             "load_token", "sendMessage", "api.telegram.org", "requests.post", "urlopen")


def self_audit() -> None:
    """讀自己個源碼,確認冇傳訊息、讀 token 或者落單嘅呼叫。有就即刻停(同 scripts/futu_export.py 一樣)。"""
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    body = src.split("FORBIDDEN = (", 1)[1].split(")", 1)[1]      # 跳過定義自己嗰幾行
    hits = [w for w in FORBIDDEN if re.search(re.escape(w), body)]
    if hits:
        print(f"★ 自我審計失敗:呢個檔案入面有禁止嘅呼叫 {hits}。拒絕執行。")
        sys.exit(2)


SHADOW = os.path.join(HERE, "shadow")
LOG_COLS = ["run_utc", "bar_date", "market", "spy_vs_ma200_pct", "n_live", "live", "held_signals", "missing",
            "data_source", "earnings_check", "version", "fingerprint"]


def webull_json_to_csv(paths, out_dir):
    """get_stock_bars 結果(新到舊)→ 每隻一個 CSV(舊到新)。回傳寫咗嘅代號。"""
    done = []
    for p in paths:
        raw = open(p, encoding="utf-8").read()
        raw = raw[raw.index("{"):]                                     # 容許前面有說明文字
        blocks = json.loads(raw)["result"]
        for blk in blocks:
            rows = blk.get("result") or []
            if not rows:
                continue
            df = pd.DataFrame(rows)
            df["Date"] = pd.to_datetime(df["time"].str[:10])
            out = pd.DataFrame({"Date": df["Date"], "Open": df["open"].astype(float), "High": df["high"].astype(float),
                                "Low": df["low"].astype(float), "Close": df["close"].astype(float),
                                "Volume": df["volume"].astype(float)})
            out = out.drop_duplicates("Date").sort_values("Date")
            out.to_csv(os.path.join(out_dir, f"{blk['symbol']}.csv"), index=False, date_format="%Y-%m-%d")
            done.append(blk["symbol"])
    return done


def main():
    self_audit()
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--webull-json", nargs="+")
    g.add_argument("--data")
    ap.add_argument("--shadow", default=SHADOW)
    a = ap.parse_args()

    import config_v66 as C
    import rules_v642 as R
    import daily_scan_v66 as D
    import notify_v66 as N

    data_dir = a.data
    if a.webull_json:
        data_dir = tempfile.mkdtemp(prefix="shadow_csv_")
        got = webull_json_to_csv(a.webull_json, data_dir)
        print(f"Webull JSON → CSV:{len(got)} 隻({data_dir})")
    need = R.TICKERS + ["SPY"]
    missing = [t for t in need if not os.path.exists(os.path.join(data_dir, f"{t}.csv"))]
    if "SPY" in missing:
        print("❌ 冇 SPY 數據,唔記錄。"); return 1

    ledger = os.path.join(a.shadow, "ledger")
    os.makedirs(ledger, exist_ok=True)
    if D._same_dir(ledger, D.L.DEFAULT_DIR):
        print("❌ 影子記錄簿唔可以係你嘅 ledger/。"); return 1
    D.G.get_next_earnings = lambda tk: None                            # 雲端冇 Yahoo;CSV 模式本身都係 off
    out = D.scan("csv", data_dir, None, ledger, dry_run=False, quiet=True)
    if out is None:
        print("❌ 掃描冇結果(數據唔夠?),唔記錄。"); return 1
    msg = N.compose_morning(out, ledger)
    bar = pd.Timestamp(out["bar_date"]).strftime("%Y-%m-%d")
    header = (f"【雲端影子記錄,唔係落單訊息】數據:Webull 唯讀日線;財報檢查:off;"
              f"缺數據:{', '.join(missing) or '冇'};跑於 {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n")
    with open(os.path.join(a.shadow, f"{bar}.txt"), "w", encoding="utf-8") as f:
        f.write(header + msg + "\n")

    live = out.get("live") or []
    fmt = lambda r: (f"{r.get('ticker')} {r.get('engine')} 股{r.get('size_live')} "
                     f"限價≤{r.get('limit_max')} 止蝕{round(float(r['stop']), 2) if r.get('stop') not in (None, '') else ''}")
    row = {"run_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"), "bar_date": bar,
           "market": "bull" if out.get("bull") else "bear", "spy_vs_ma200_pct": round(float(out.get("gap") or 0), 2),
           "n_live": len(live), "live": " | ".join(fmt(r) for r in live),
           "held_signals": " ".join(r.get("ticker", "") for r in (out.get("held_signals") or [])),
           "missing": " ".join(missing), "data_source": "Webull read-only daily bars",
           "earnings_check": "off (no Yahoo in cloud)", "version": C.VERSION, "fingerprint": C.fingerprint()}
    log = os.path.join(a.shadow, "shadow_log.csv")
    prev = pd.read_csv(log, dtype=str, encoding="utf-8-sig") if os.path.exists(log) else pd.DataFrame(columns=LOG_COLS)
    if (prev.get("bar_date") == bar).any():
        print(f"ℹ️ {bar} 已經記錄過,唔重複寫 shadow_log.csv(訊息檔已更新)。")
    else:
        new = not os.path.exists(log)
        with open(log, "a", encoding="utf-8-sig" if new else "utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=LOG_COLS)
            if new:
                w.writeheader()
            w.writerow(row)
    print(f"✅ {bar}:{row['market']},SPY 對 MA200 {row['spy_vs_ma200_pct']:+.2f}%,交易清單 {len(live)} 隻 → {a.shadow}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
