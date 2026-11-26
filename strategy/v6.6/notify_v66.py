# -*- coding: utf-8 -*-
"""
Swing V6.6 每日 Telegram 訊息(模擬盤)
======================================
美股收市後(香港時間大約早上 6:30,由 notify_v66.bat + Windows 工作排程器自動行):
  跑一次每日掃描 → 將「① 交易清單 + 落單規則 + ④ 持倉止蝕位」用 Telegram 傳畀你。
開市檢查唔喺呢度做:開市價要用 TradingView(Owner 2026-11-26:唔用 Yahoo)—— 見 pine/swing_v66.pine 嘅開市提示。

用法:
  python notify_v66.py                 # 掃描(照寫記錄簿)+ 傳訊息
  python notify_v66.py --print-only    # 掃描 + 只喺視窗印訊息,唔傳
  python notify_v66.py --test          # 傳一句測試訊息(確認 token 同 chat ID 設定啱)
  python notify_v66.py --alert selftest   # 傳「自我測試失敗,今日唔好交易」(notify_v66.bat 用)

安全:
  - 唔會落單、唔會連券商(呢個檔冇任何券商代碼);所有單由你自己喺模擬盤落。
  - Token 用 telegram_bot_v66.load_token():只喺資料夾外面嘅檔或者環境變數讀,唔可以放喺 v6.6 資料夾入面。
  - 只傳畀你批准嘅 chat ID;所有錯誤訊息都會遮住 token。
"""
import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import config_v66 as C            # noqa: E402
import daily_scan_v66 as DS       # noqa: E402
import ledger_v66 as L            # noqa: E402
import telegram_bot_v66 as TB     # noqa: E402

MAX_LEN = 4000                    # Telegram 一則訊息上限 4,096 字;留啲位
C_MR_MAX_HOLD = DS.R.MR_MAX_HOLD     # 引擎一最多持 10 日(V6.4.2 鎖死參數)
ALERTS = {
    "selftest": "❌ 自我測試失敗 —— 今日唔好交易(模擬盤都唔好)。將 v6.6 資料夾嘅 selftest_last.log 畀 AI 睇。",
    "scan": "❌ 每日掃描出錯 —— 今日唔好交易。雙擊 掃描_v66.bat 睇錯誤訊息,畀 AI 睇。",
}
OPEN_CHECK = ("開市檢查(美國夏令時間香港 21:30、其他時間 22:30 開市):你**一定要開市嗰陣睇住**;睇唔到就**唔好預先落單**,或者瞓之前取消。"
              "以券商張單狀態為準;TradingView 開市提示(開市價嚟自 TradingView,唔係 Yahoo)只係提你。"
              "未成交 → 取消張單(唔好留住佢全日等成交);成交價 ≤ 系統止蝕 → 即刻沽,當日記 fill open 同 fill close,S2 交 CRO;"
              "成交咗、高過系統止蝕 → 即刻自己落止蝕單(用上面嘅系統止蝕)。")
PARTIAL = ("⚠️ 美股未收市(呢次係開市時間跑嘅)—— ❌ 呢個訊息**唔可以用嚟落單**,冇交易清單。"
           "等收市後(香港時間朝早)嘅訊息(CRO N-31)。")
FOOTER = "研究工具,唔會落單;所有單由你自己落(模擬盤)。唔係投資建議。"


def _msg_line(rec, rank_txt, hide=False, held=False):
    """手機睇嘅短版(同掃描器 ① 同一批數,唔另計)。"""
    size = "股數 —(持倉中)" if held else DS._size_txt(rec, hide)
    eng = "引擎二" if rec["engine"] == "E2" else f"引擎一[{rec.get('tier') or '-'}]"
    tgt = "" if rec["engine"] == "E2" else f"  止盈 ${float(rec['target']):.2f}(R {rec['r']})"
    flag = f"  {rec['spec_flag']}" if rec.get("spec_flag") and rec["spec_flag"] != "✅" else ""
    return (f"{rank_txt} {eng} {rec['ticker']}:{size}\n"
            f"    止蝕 ${float(rec['stop']):.2f}(-{float(rec['risk_pct']):.1f}%){tgt}\n"
            f"    收市 ${float(rec['close']):.2f}  距財報 {rec['days_er']}{flag}")


def compose_morning(out, ledger_dir=None):
    """將 daily_scan_v66.scan() 嘅結果變做一則訊息。out = None → 掃描出錯訊息。"""
    ledger_dir = ledger_dir or L.DEFAULT_DIR
    head = f"📋 模擬盤 Swing {C.VERSION}  指紋 {C.fingerprint()}"
    if out is None:
        return "\n".join([head, ALERTS["scan"], FOOTER])
    bull = out.get("bull")
    gap = out.get("gap")
    gap_txt = f"(SPY 對 MA200 {gap:+.1f}%)" if gap is not None else ""
    lines = [head, f"美股 {out['bar_date'].date()} 收市 | {'牛市' if bull else '熊市'}{gap_txt}"]
    if out.get("failed"):
        lines.append(f"⚠️ 下載失敗 {len(out['failed'])} 隻(今日冇佢哋嘅訊號):{', '.join(out['failed'])}")
    hold = out.get("s2_hold") or []
    if hold:
        lines.append(f"⛔ 有未向 CRO 解釋嘅 S2({', '.join(hold)})—— 停開新倉(CRO N-11)。")
    of = L.open_fills(ledger_dir)
    if out.get("partial"):
        lines.append(PARTIAL)                         # CRO N-31 / Tom F-1:未收市 → 冇 ①、冇落單規則
    elif bull:
        free = 0 if hold else max(0, C.MAX_POSITIONS - len(of))      # Tom F-5:停開新倉期間 = 0
        live = out.get("live") or []
        lines.append(f"\n① 交易清單(回測驗證版)—— 而家持倉 {len(of)} 個,今日最多開 {free} 個,由 #1 開始揀")
        if not live:
            lines.append("今日冇訊號。空手係一種倉位。")
        for rec in live:
            lines.append(_msg_line(rec, f"#{rec['rank']}", hide=bool(hold)))
        for rec in out.get("held_signals") or []:
            lines.append(_msg_line(rec, " — ", held=True) + "\n    持倉中(唔計排名,唔好加注)")
        if live and not hold and free > 0:
            lines.append("")
            lines += list(DS.ORDER_RULES)
            lines.append(OPEN_CHECK)
        elif live and free == 0:
            lines.append("倉位已滿 —— 今日唔開新倉。")
    else:
        lines.append("熊市:系統停手,今日唔搵做多訊號(唔開新倉);持倉照管。")
    if len(of):
        lines.append("\n④ 你嘅持倉 —— 今日止蝕位(券商止蝕單只可以調高,永遠唔好調低)"
                     + ("\n  ⚠️ 未收市數據,只係參考;以收市後嘅訊息為準" if out.get("partial") else ""))
        data = out.get("data") or {}
        for x in of.itertuples():
            lines.append("  " + DS.trailing_line(x, data) + _e1_exit_note(x, data))
    lines.append("\n" + FOOTER)
    return "\n".join(lines)


def _e1_exit_note(x, data):
    """引擎一滿 10 日(連入場日)收市出:今日係第 9 日 → 聽日收市出。日數同 trailing_line 一樣計。"""
    df = data.get(x.ticker)
    if x.engine != "E1" or df is None:
        return ""
    days = int((df.index >= DS.pd.Timestamp(x.open_date)).sum())
    if days == C_MR_MAX_HOLD - 1:
        return f"\n    ⚠️ 聽日係第 {C_MR_MAX_HOLD} 日:未到止蝕或者止盈,就聽日收市前出"
    if days >= C_MR_MAX_HOLD:
        return f"\n    ⚠️ 已經滿 {C_MR_MAX_HOLD} 日:應該已經收市出咗;未出就問 AI"
    return ""


def build_message(out, ledger_dir=None):
    """compose_morning 出錯都要通知你(Tom F-7):回傳 (訊息, exit code)。"""
    try:
        return compose_morning(out, ledger_dir), (0 if out is not None else 1)
    except Exception as e:
        return "\n".join([f"📋 模擬盤 Swing {C.VERSION}", ALERTS["scan"], f"(整訊息出錯:{type(e).__name__})"]), 1


def split(text, n=MAX_LEN):
    """按行切開,每段 ≤ n 字。"""
    parts, cur = [], ""
    for ln in text.split("\n"):
        while len(ln) > n:                     # 單一行太長(唔應該發生)都要切
            if cur:
                parts.append(cur); cur = ""
            parts.append(ln[:n]); ln = ln[n:]
        if len(cur) + len(ln) + 1 > n:
            parts.append(cur); cur = ln
        else:
            cur = f"{cur}\n{ln}" if cur else ln
    if cur:
        parts.append(cur)
    return parts


def send(text, token, chats, post=None, timeout=15):
    """傳去 Telegram。回傳 True = 全部成功。所有錯誤都遮住 token。post 可以換(測試用,唔上網)。"""
    if post is None:
        import requests
        post = requests.post
    if not chats:
        print(f"❌ 未設定准許嘅 chat ID(見 {TB.ALLOW_FILE})—— 冇傳。")
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    ok = True
    for part in [p for p in split(text) if p.strip()]:          # Tom F-11:唔傳空段
        for chat in sorted(chats):
            try:
                r = post(url, data={"chat_id": chat, "text": part}, timeout=timeout)
                js = r.json()
                if not js.get("ok"):
                    ok = False
                    print("❌ 傳送失敗:" + TB.redact(js.get("description", js), token))
            except Exception as e:
                ok = False
                print("❌ 傳送失敗:" + TB.redact(f"{type(e).__name__}: {e}", token))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--print-only", action="store_true", help="只印,唔傳")
    ap.add_argument("--test", action="store_true", help="傳一句測試訊息")
    ap.add_argument("--alert", choices=sorted(ALERTS), help="傳一句警告(.bat 用)")
    ap.add_argument("--source", choices=["yf", "csv"], default="yf")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    ap.add_argument("--asof")
    ap.add_argument("--ledger", default=L.DEFAULT_DIR)
    ap.add_argument("--dry-run", action="store_true", help="掃描唔寫記錄簿")
    a = ap.parse_args(argv)

    code = 0
    if a.alert:
        text = "\n".join([f"📋 模擬盤 Swing {C.VERSION}", ALERTS[a.alert]])
        code = 1
    elif a.test:
        text = f"✅ 測試訊息:Swing {C.VERSION} 指紋 {C.fingerprint()} —— Telegram 設定啱咗。{FOOTER}"
    else:
        C.check_config()
        try:
            out = DS.scan(a.source, a.data, a.asof, a.ledger, a.dry_run, quiet=True)
        except Exception as e:                       # 掃描出錯都要通知你
            print(f"掃描出錯:{type(e).__name__}: {e}")
            out = None
        text, code = build_message(out, a.ledger)
    print(text)
    if a.print_only:
        return code
    if not send(text, TB.load_token(), TB.load_allowed()):
        return 3
    print("\n已傳送。")
    return code


if __name__ == "__main__":
    sys.exit(main())
