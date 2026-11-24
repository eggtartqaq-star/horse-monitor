# -*- coding: utf-8 -*-
"""
Swing V6.6 Telegram 查詢機械人
==============================
同 V6.4.2 bot 一樣:喺 Telegram 打代號(美股字母 / 港股數字),回覆訊號同交易計劃。
分別:
  1. 所有規則來自 V6.6 共用核心(signals/sizing/guardrails)—— 唔再有第二份規則副本
  2. 同時講兩條路徑:交易路徑(回測驗證版)同舊掃描器路徑(只記錄)
  3. 安全:
     - Token 唔寫喺代碼:用環境變數 SWING_BOT_TOKEN,或者放喺資料夾外面嘅檔
       (預設 %USERPROFILE%\\.swing_bot_token)
     - 只回覆你批准嘅 chat ID(SWING_BOT_ALLOWED_CHATS 或 %USERPROFILE%\\.swing_bot_allowed)
     - 所有錯誤訊息會遮住 token(舊版 print(e) 會連 /bot<token>/ 網址一齊印出)

第一次設定:
  1. @BotFather → /revoke → 攞新 token
  2. 將 token 存入 %USERPROFILE%\\.swing_bot_token(一行,唔好有空格)
  3. python telegram_bot_v66.py  → 喺 Telegram 打任何字,bot 會喺電腦視窗印出你嘅 chat ID
  4. 將 chat ID 存入 %USERPROFILE%\\.swing_bot_allowed,再重新開 bot
"""
import os
import re
import sys
import time

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
import rules_v642 as R        # noqa: E402
import signals_v66 as S       # noqa: E402
import sizing_v66 as Z        # noqa: E402
from indicators import calc_indicators  # noqa: E402

PLACEHOLDER = "在這裡貼上你的TOKEN"
POOL = set(R.TICKERS)
HOME = os.path.expanduser("~")
TOKEN_FILE = os.environ.get("SWING_BOT_TOKEN_FILE", os.path.join(HOME, ".swing_bot_token"))
ALLOW_FILE = os.environ.get("SWING_BOT_ALLOWED_FILE", os.path.join(HOME, ".swing_bot_allowed"))
# Tom 2026-11-24:冒號有時會被 URL 編碼成 %3A
_TOKEN_RE = re.compile(r"\d{6,12}(?::|%3[Aa])[A-Za-z0-9_-]{20,}")


# ============================================================
# 安全
# ============================================================
def redact(text, token=None) -> str:
    s = str(text)
    if token:
        s = s.replace(token, "<TOKEN>")
    return _TOKEN_RE.sub("<TOKEN>", s)


def load_token():
    tok = os.environ.get("SWING_BOT_TOKEN", "").strip()
    if not tok and os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, encoding="utf-8-sig") as f:
            tok = f.read().strip()
    if not tok or tok == PLACEHOLDER:
        raise SystemExit("❌ 未設定 token。將新 token 存入 " + TOKEN_FILE +
                         "(或設環境變數 SWING_BOT_TOKEN)。唔好寫入任何 .py 檔。")
    tf, here = os.path.abspath(TOKEN_FILE), os.path.abspath(HERE)
    if os.path.commonpath([tf, here]) == here:       # Tom 2026-11-24:子資料夾(例如 ledger/)都唔得
        raise SystemExit("❌ token 檔唔可以放喺 V6.6 資料夾(或者佢嘅子資料夾)入面(會被一齊複製/上載)。")
    return tok


def load_allowed():
    raw = os.environ.get("SWING_BOT_ALLOWED_CHATS", "")
    if not raw and os.path.exists(ALLOW_FILE):
        with open(ALLOW_FILE, encoding="utf-8-sig") as f:
            raw = f.read()
    return {x.strip() for x in re.split(r"[,\s]+", raw) if x.strip()}


# ============================================================
# 分析(唔使網絡都可以測:傳入 fetch)
# ============================================================
def normalize_ticker(user_input):
    s = user_input.strip().upper()
    if s.isdigit():
        return f"{s.zfill(4)}.HK", "港股"
    return s, "美股"


def _yf_fetch(tk, period="2y"):
    import yfinance as yf
    df = yf.Ticker(tk).history(period=period, auto_adjust=True)
    if df is None or df.empty:
        return None
    df.index = df.index.tz_localize(None).normalize()
    return df[["Open", "High", "Low", "Close", "Volume"]]


def analyze(user_input, fetch=None, earnings="lookup"):
    """回傳畀 Telegram 嘅文字。fetch(ticker) -> DataFrame;earnings="lookup" 或 Timestamp/None/"off"。"""
    fetch = fetch or _yf_fetch
    ticker, market = normalize_ticker(user_input)
    idx_tk, idx_name = ("SPY", "SPY") if market == "美股" else ("^HSI", "恒生指數")
    lines = [f"📊 {ticker}({market})  |  Swing {C.VERSION} 指紋 {C.fingerprint()}"]
    idx = fetch(idx_tk)
    is_bull = None
    if idx is not None and len(idx) >= 200:
        ma = idx["Close"].rolling(200).mean().iloc[-1]
        is_bull = bool(idx["Close"].iloc[-1] > ma)
        gap = (idx["Close"].iloc[-1] - ma) / ma * 100
        lines.append(f"市場環境: {idx_name} {'高於' if is_bull else '低於'}200日均線 {abs(gap):.1f}%")
    else:
        lines.append(f"市場環境: 無法取得{idx_name}數據")
    try:
        df = fetch(ticker)
    except Exception as e:
        return "\n".join(lines + [f"❌ 無法取得 {ticker} 數據({type(e).__name__})"])
    if df is None or len(df) < 60:
        return "\n".join(lines + [f"❌ 無法分析 {ticker}:數據不足,請確認代碼。"])

    ind = calc_indicators(df)
    row = ind.iloc[-1].copy()
    row["bull"] = bool(is_bull)
    close = float(row["Close"])
    lines.append(f"現價: ${close:.2f}  (數據至 {ind.index[-1].date()})")
    if pd.notna(row["ADX"]):
        route = R.classify(row)
        lines.append(f"ADX: {row['ADX']:.1f}  " + {"MR": "(橫盤→引擎一)", "TREND_UP": "(升勢→引擎二)",
                                                  "TREND_DOWN": "(趨勢向下)"}.get(route, ""))
    lines.append(f"RSI14: {row['RSI14']:.1f}   RSI2: {row['RSI2']:.1f}")

    ev = S.evaluate(row) if is_bull else {"route": "SKIP", "e1": None, "e2": None}
    sig = {p: S.on_path(ev, p) for p in ("bt", "scan")}
    any_sig = sig["bt"] or sig["scan"]

    blocks = []
    if market == "美股" and ticker not in POOL:
        blocks.append("❌ 唔喺你38隻股票池 → 訊號必須來自掃描器")
    if market == "港股":
        blocks.append("❌ 港股:系統以美股回測,未經驗證,唔做")
    if not is_bull:
        blocks.append("❌ 熊市(或無法判斷)→ 系統停手")

    plan_lines = []
    if any_sig:
        g = G.check(ticker, ind, any_sig["risk_pct"], earnings_ts=earnings if earnings != "off" else None,
                    asof_mode=(earnings == "off"))
        ccy = "HKD" if market == "港股" else "USD"
        sz = Z.size(close, any_sig["stop"], any_sig["engine"], Z.live_mode(), ccy)
        lines.append("")
        if any_sig["engine"] == "E1":
            plan = {"stop": any_sig["stop"], "target": any_sig["target"], "r": any_sig["r"]}
            tier = R.classify_mr_tier(row, any_sig["score"], plan,
                                      g["days_er"] if isinstance(g["days_er"], int) else None)
            tmap = {"PREMIUM": "⭐頂級", "STRONG": "💪強", "BASIC": "🔵普通", None: "⚪無"}
            lines.append(f"引擎一(均值回歸)評分 {any_sig['score']}  級別 {tmap.get(tier)}")
            plan_lines = ["── 交易計劃 ──", f"入場: ${close:.2f}",
                          f"止蝕: ${any_sig['stop']}  (-{any_sig['risk_pct']:.1f}%)",
                          f"止盈: ${any_sig['target']}  R值 {any_sig['r']}R",
                          "持倉: 最多10個交易日,第10日收市出"]
        else:
            lines.append(f"引擎二(趨勢)評分 {any_sig['score']}  突破20日高: {'✅' if any_sig['breakout'] else '❌'}")
            plan_lines = ["── 交易計劃 ──", f"入場: ${close:.2f}",
                          f"初始止損: ${any_sig['stop']}  (-{any_sig['risk_pct']:.1f}%)",
                          "移動止損: 每日收市後 = 入場以嚟最高價 − 3×ATR,只升不降;冇固定止盈"]
        plan_lines.append(f"建議股數(上限 {Z.live_mode()}): {sz['shares']}股 (~{sz['notional']:.0f})")
        if not g["ok"]:
            blocks.append(f"❌ {g['reason']}")
        if sz["shares"] < 1:
            blocks.append("❌ 買唔起1股(10%上限/1%風險,唔准硬買)")
        if g["flag"] != "✅":
            blocks.append(f"⚠️ {g['flag']} → 加倍小心或跳過")
        lines.append(f"距財報: {g['days_er'] if g['days_er'] is not None else '?(必須自己上網查)'}")
    elif is_bull:
        lines.append("\n今日冇任何訊號(兩條路徑都冇)")

    bt_ok = sig["bt"] is not None and not [b for b in blocks if b.startswith("❌")]
    if bt_ok:
        lines += [""] + plan_lines        # CRO C-2:只有交易路徑、護欄全過先顯示交易計劃同股數
    lines.append("")
    lines.append("=" * 22)
    if bt_ok:
        lines += ["✅ 交易路徑(回測驗證版):訊號成立,自動護欄全過",
                  "最後一關:你自己認唔認同?落單後即刻設止損 + 用 ledger fill 記錄"]
    else:
        why = list(blocks)
        if sig["bt"] is None and sig["scan"] is not None:
            why = ["❌ 只係舊掃描器路徑先有(例如引擎二冇突破20日高)→ 只記錄,唔交易"] + why
        elif sig["bt"] is None and not why:
            why = ["❌ 交易路徑冇訊號"]
        lines += ["🚫 唔入場(所以唔顯示交易計劃同股數):"] + [f"  {b}" for b in why]
    lines.append(f"舊掃描器路徑(只記錄):{'有訊號' if sig['scan'] else '冇訊號'}")
    return "\n".join(lines)


# ============================================================
# Telegram 輪詢
# ============================================================
def main():
    import requests
    C.check_config()
    token = load_token()

    def _redacting_hook(t, v, tb):
        # Tom 2026-11-24:任何冇被捉到嘅錯誤(包括喺 except 入面撳 Ctrl+C 帶出嘅「連鎖」錯誤)
        # 都會印出原本嘅 URL(/bot<token>/...)。全部經 redact 先印。
        import traceback
        sys.stderr.write(redact("".join(traceback.format_exception(t, v, tb)), token))
    sys.excepthook = _redacting_hook
    allowed = load_allowed()
    api = f"https://api.telegram.org/bot{token}"
    print("=" * 50)
    print(f"Swing {C.VERSION} Telegram Bot  指紋 {C.fingerprint()}")
    try:
        me = requests.get(f"{api}/getMe", timeout=10).json()
        if not me.get("ok"):
            print("❌ Token 無效(" + redact(me.get("description", ""), token) + ")")
            return
        print(f"✅ 已連接: @{me['result']['username']}")
    except Exception as e:
        print("❌ 連線失敗: " + redact(f"{type(e).__name__}: {e}", token)); return
    if not allowed:
        print("⚠️ 未設定准許嘅 chat ID —— 設定模式:bot 唔會回覆分析,只會喺呢度印出 chat ID。")
    offset = None
    while True:
        try:
            r = requests.get(f"{api}/getUpdates", params={"timeout": 30, **({"offset": offset} if offset else {})},
                             timeout=35).json()
            if not r.get("ok"):
                print("取得訊息失敗: " + redact(r, token)); time.sleep(5); continue
            for u in r.get("result", []):
                offset = u["update_id"] + 1
                msg = u.get("message") or {}
                chat = str((msg.get("chat") or {}).get("id", ""))
                text = (msg.get("text") or "").strip()
                if not chat or not text:
                    continue
                if chat not in allowed:
                    print(f"⛔ 未授權 chat ID {chat}(如果係你,將佢加入 {ALLOW_FILE})")
                    continue
                if text.startswith("/start"):
                    reply = "輸入股票代號(美股 AAPL / 港股 700)。只係研究工具,唔會落單。"
                else:
                    try:
                        reply = analyze(text)
                    except Exception as e:
                        reply = "❌ 分析失敗:" + redact(f"{type(e).__name__}: {e}", token)
                requests.post(f"{api}/sendMessage", data={"chat_id": chat, "text": reply}, timeout=15)
        except KeyboardInterrupt:
            print("已停止"); return
        except Exception as e:
            print("錯誤: " + redact(f"{type(e).__name__}: {e}", token)); time.sleep(5)


if __name__ == "__main__":
    main()
