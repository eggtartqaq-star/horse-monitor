# -*- coding: utf-8 -*-
"""
============================================================
Swing Trade Telegram 查詢機械⼈ V6.4（護欄版）
============================================================
功能：
  在 Telegram 輸入股票代碼，機械⼈回覆：
    - 市場環境（⽜市/熊市）
    - 訊號級別（
頂級 / 
強 / 
普通 / 無訊號）
    - ⽌蝕位、⽌盈位、R值
    - 建議風險倉位
⽀援格式：
  美股：直接打字⺟，如 AAPL、CVX、NVDA
  港股：直接打數字，如 700、9988、1810（⾃動轉 .HK）
使⽤⽅法：
  1. 先跑 telegram_token_test.py 確認 token 有效
  2. 把下⾯ BOT_TOKEN 換成你的（同test腳本⽤同⼀個）
  3. python telegram_swing_bot.py
  4. 保持這個視窗開著（關掉=bot停⽌回覆）
  5. 在 Telegram 打開你的 bot，輸入股票代碼即可
重要限制：
  這個 bot 只在你電腦運⾏這個腳本時才會回覆。
  不是24⼩時雲端服務——關電腦=bot離線。
============================================================
"""
import requests
import time
import pandas as pd
import yfinance as yf
import ta
import warnings
warnings.filterwarnings("ignore")
# 貼上你的 token（與 telegram_token_test.py ⽤同⼀個，測試通過的那個）
BOT_TOKEN = "在這裡貼上你的TOKEN"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN.strip()}"
MIN_R = 2.0
# ---- V6.4 資⾦設定(同 dual_engine_v6_4.py ⼀致) ----

ACCOUNT_HKD = 10000
RISK_PCT    = 1.0
USD_HKD     = 7.8
# ---- V6.4 引擎⼆(趨勢)參數 ----
ATR_TRAIL_MULT  = 3.0
TREND_SCORE_MIN = 0.65
# ---- V6.4 護欄 ----
MAX_STOP_PCT = 15.0     # ⽌蝕距離上限
# ---- 你嘅38隻股票池(護欄6:訊號必須來⾃股票池) ----
POOL = {
    "AAPL","MSFT","GOOGL","AMZN","NVDA","META","TSLA","AVGO",
    "AMD","QCOM","MU","INTC","JPM","BAC","GS","V","MA",
    "COST","WMT","MCD","NKE","SBUX","UNH","JNJ","PFE","LLY",
    "XOM","CVX","CAT","BA","PLTR","CRM","ADBE","NFLX","SHOP","UBER","COIN","MSTR"
}
# ============================================================
# 代號格式轉換
# ============================================================
def normalize_ticker(user_input):
    s = user_input.strip().upper()
    if s.isdigit():
        return f"{s.zfill(4)}.HK", "港股"
    return s, "美股"
# ============================================================
# 市場環境
# ============================================================
def check_market_regime(market):
    index_ticker = "SPY" if market == "美股" else "^HSI"
    index_name = "SPY" if market == "美股" else "恒⽣指數"
    try:
        idx = yf.Ticker(index_ticker).history(period="1y")
        idx["MA200"] = idx["Close"].rolling(200).mean()
        latest = idx.iloc[-1]
        if pd.isna(latest["MA200"]):
            return None, f"{index_name} 數據不⾜"
        is_bull = latest["Close"] > latest["MA200"]
        gap = (latest["Close"] - latest["MA200"]) / latest["MA200"] * 100
        return is_bull, f"{index_name} {'⾼於' if is_bull else '低於'}200⽇均線 {abs
    except Exception:
        return None, f"無法取得{index_name}數據"
# ============================================================

# 指標與評分
# ============================================================
def calc_indicators(df):
    df = df.copy()
    df["MA20"]  = df["Close"].rolling(20).mean()
    df["MA50"]  = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["RSI14"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()
    df["RSI2"]  = ta.momentum.RSIIndicator(df["Close"], window=2).rsi()
    adx_ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14
    df["ADX"] = adx_ind.adx()
    df["DI_PLUS"]  = adx_ind.adx_pos()
    df["DI_MINUS"] = adx_ind.adx_neg()
    atr_ind = ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"], 
    df["ATR"] = atr_ind.average_true_range()
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"]  = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"]  = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).m
    obv = ta.volume.OnBalanceVolumeIndicator(df["Close"], df["Volume"]).on_balanc
    df["OBV"] = obv
    df["OBV_Div"] = (df["Close"] < df["Close"].shift(5)) & (df["OBV"] > df["OBV"]
    df["low_10d"]  = df["Low"].rolling(10).min()
    df["high_20d"] = df["High"].rolling(20).max()
    df["high_60d"] = df["High"].rolling(60).max()
    df["dist_60h"] = (df["high_60d"] - df["Close"]) / df["Close"] * 100
    return df
# ============================================================
# V6.4 引擎⼆:趨勢評分 + 計劃
# ============================================================
def trend_score(row):
    score = 0.0
    ts = 0.0
    adx = row["ADX"]
    if pd.notna(adx):
        if adx >= 40:   ts = 1.0
        elif adx >= 30: ts = 0.85
        elif adx >= 25: ts = 0.6
    score += ts * 0.25
    ma = 0.3
    c, m20, m50, m200 = row["Close"], row["MA20"], row["MA50"], row["MA200"]
    if pd.notna(m20) and pd.notna(m50):
        if pd.notna(m200) and c > m20 > m50 > m200: ma = 1.0
        elif c > m20 > m50: ma = 0.8

        elif c > m20: ma = 0.5
        else: ma = 0.1
    score += ma * 0.25
    ph = 0.0
    d = row["dist_60h"]
    if pd.notna(d):
        if d <= 1:    ph = 1.0
        elif d <= 3:  ph = 0.85
        elif d <= 5:  ph = 0.6
        elif d <= 10: ph = 0.35
        else:         ph = 0.1
    score += ph * 0.25
    vs = 0.4
    vr = row["vol_ratio"]
    if pd.notna(vr):
        vs = 1.0 if vr > 1.2 else (0.7 if vr > 1.0 else 0.4)
    score += vs * 0.15
    if pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]:
        score += 0.10
    return round(min(score, 1.0), 4)
def trend_plan(row):
    close = row["Close"]; atr = row["ATR"]
    if pd.isna(atr) or atr <= 0 or pd.isna(close):
        return None
    stop = close - ATR_TRAIL_MULT * atr
    risk_pct = (close - stop) / close * 100
    if risk_pct > 12:
        return None
    return {"stop": round(stop, 2), "risk_pct": round(risk_pct, 1)}
def classify_route(row):
    """V6.4分流器"""
    adx, dip, din = row["ADX"], row["DI_PLUS"], row["DI_MINUS"]
    if pd.isna(adx) or pd.isna(dip) or pd.isna(din):
        return "SKIP"
    if adx < 25:
        return "MR"
    return "TREND_UP" if dip > din else "TREND_DOWN"
def position_plan(entry, stop):
    """V6.4護欄4:1%風險可買幾多整數股"""
    per_share = entry - stop
    if per_share <= 0:

        return 0, 0
    risk_usd = ACCOUNT_HKD * RISK_PCT / 100 / USD_HKD
    shares = int(risk_usd // per_share)
    return shares, round(shares * entry, 0)
def check_spec(df):
    """V6.4護欄3:半年⾼低波幅≥2倍 = 投機股"""
    try:
        h6 = df.tail(126)
        if h6["Low"].min() > 0 and h6["High"].max() / h6["Low"].min() >= 2.0:
            return True
    except Exception:
        pass
    return False
def mr_score(row):
    score = 0.0
    rsi14 = row["RSI14"]
    if pd.notna(rsi14):
        if 35 <= rsi14 <= 45:   rs = 1.0
        elif 45 < rsi14 <= 55:  rs = 0.8
        elif 30 <= rsi14 < 35:  rs = 0.6
        elif 55 < rsi14 <= 65:  rs = 0.4
        elif rsi14 > 65:        rs = 0.1
        else:                    rs = 0.3
        score += rs * 0.20
    rsi2 = row["RSI2"]
    if pd.notna(rsi2):
        if rsi2 < 5:    r2 = 1.0
        elif rsi2 < 10: r2 = 0.85
        elif rsi2 < 20: r2 = 0.70
        elif rsi2 < 30: r2 = 0.50
        else:           r2 = 0.20
        score += r2 * 0.15
    pma20 = row["price_vs_ma20"]; ma_t = row["ma20_vs_ma50"]
    if pd.notna(pma20) and pd.notna(ma_t):
        if -5 <= pma20 <= 0 and ma_t > 0:    ss = 1.0
        elif -10 <= pma20 < -5 and ma_t > 0: ss = 0.8
        elif 0 < pma20 <= 3 and ma_t > 0:    ss = 0.7
        elif pma20 < -10 and ma_t > 0:        ss = 0.4
        else:                                  ss = 0.2
        score += ss * 0.20
    ret10 = row["ret_10d"]
    if pd.notna(ret10):
        if -15 <= ret10 <= -5:    r3 = 1.0

        elif -20 <= ret10 < -15:  r3 = 0.7
        elif -5 < ret10 <= -2:    r3 = 0.5
        elif ret10 > 0:           r3 = 0.1
        else:                     r3 = 0.3
        score += r3 * 0.20
    vr = row["vol_ratio"]; ret5 = row["ret_5d"]
    if pd.notna(vr) and pd.notna(ret5):
        if ret5 < 0 and vr > 1.3:    vs = 1.0
        elif ret5 < 0 and vr > 1.1:  vs = 0.8
        elif ret5 < 0 and vr > 0.9:  vs = 0.5
        elif ret5 >= 0 and vr > 1.2: vs = 0.6
        else:                         vs = 0.2
        score += vs * 0.15
    if row.get("OBV_Div", False):
        score += 0.10
    return round(min(score, 1.0), 4)
def mr_plan(row):
    # V6.2升級：⽌蝕=結構位與2×ATR取較闊(C臂,回測EV 0.24%→1.10%)
    if pd.isna(row["low_10d"]) or pd.isna(row["Close"]):
        return None
    close = row["Close"]
    atr = row.get("ATR")
    if pd.isna(atr) or atr <= 0:
        return None
    stop_struct = row["low_10d"] * 0.995
    stop_atr = close - 2.0 * atr
    stop = min(stop_struct, stop_atr)
    risk = close - stop
    if risk <= 0:
        return None
    targets = []
    if pd.notna(row["MA50"]) and row["MA50"] > close:
        targets.append((row["MA50"], (row["MA50"] - close) / risk))
    if pd.notna(row["high_60d"]) and row["high_60d"] > close:
        targets.append((row["high_60d"], (row["high_60d"] - close) / risk))
    valid = [(p, r) for p, r in targets if r >= MIN_R]
    if not valid:
        best_r = max([r for _, r in targets], default=0)
        return {"stop": round(stop, 2), "target": None, "r": None, "best_r": roun
    tp, r = min(valid, key=lambda x: x[0])
    return {"stop": round(stop, 2), "target": round(tp, 2), "r": round(r, 2), "be
# ============================================================
# 訊號分級（同 signal_tier_v62.py 邏輯）

# ============================================================
def get_days_to_earnings(ticker):
    try:
        cal = yf.Ticker(ticker).calendar
        if cal is None:
            return None
        ed = None
        if isinstance(cal, dict):
            ed = cal.get("Earnings Date")
            if isinstance(ed, (list, tuple)) and ed:
                ed = ed[0]
        else:
            if "Earnings Date" in getattr(cal, "index", []):
                ed = cal.loc["Earnings Date"][0]
        if ed is None:
            return None
        ed = pd.Timestamp(ed).tz_localize(None)
        today = pd.Timestamp.now().normalize()
        return (ed - today).days
    except Exception:
        return None
def classify_tier(row, score, plan, ticker):
    if plan is None or plan.get("target") is None or plan.get("r") is None:
        return None, {}
    r = plan["r"]
    rsi2 = row.get("RSI2")
    obv_div = bool(row.get("OBV_Div", False))
    is_basic = score >= 0.55 and r >= MIN_R
    if not is_basic:
        return None, {}
    cond_rsi2 = pd.notna(rsi2) and rsi2 < 10
    cond_r3 = r >= 3.0
    is_strong = is_basic and cond_rsi2 and cond_r3
    days_to_er = get_days_to_earnings(ticker)
    cond_earnings = days_to_er is not None and abs(days_to_er) > 5
    is_premium = is_strong and obv_div and cond_earnings
    reasons = {
        "RSI2<10": cond_rsi2, "R值≥3": cond_r3,
        "OBV背離": obv_div, "距財報>5天": cond_earnings,
        "財報天數": days_to_er,
    }

    if is_premium:
        return "PREMIUM", reasons
    elif is_strong:
        return "STRONG", reasons
    else:
        return "BASIC", reasons
# ============================================================
# 主分析邏輯 → 產⽣ Telegram 回覆⽂字
# ============================================================
def analyze_and_format(user_input):
    ticker, market = normalize_ticker(user_input)
    is_bull, regime_msg = check_market_regime(market)
    try:
        df = yf.Ticker(ticker).history(period="2y")
        if df.empty or len(df) < 60:
            return f"
 無法分析 {ticker}\n數據不⾜，請確認代碼是否正確。"
    except Exception as e:
        return f"
 無法取得 {ticker} 數據\n{e}"
    df = calc_indicators(df)
    row = df.iloc[-1]
    close = round(row["Close"], 2)
    rsi14 = round(row["RSI14"], 1) if pd.notna(row["RSI14"]) else None
    rsi2  = round(row["RSI2"], 1) if pd.notna(row["RSI2"]) else None
    adx   = round(row["ADX"], 1) if pd.notna(row["ADX"]) else None
    route = classify_route(row)
    is_spec = check_spec(df)
    days_er = get_days_to_earnings(ticker)
    lines = []
    lines.append(f"
 {ticker}（{market}）")
    lines.append(f"現價: ${close}")
    lines.append("")
    lines.append(f"市場環境: {regime_msg}")
    if adx is not None:
        lines.append(f"ADX: {adx} {'(橫盤→引擎⼀)' if route=='MR' else '(趨勢→引擎⼆)
    if rsi14 is not None:
        lines.append(f"RSI14: {rsi14}   RSI2: {rsi2}")
    lines.append("")
    # ============ 護欄檢查 ============

    blocks = []   # 被擋原因
    # 護欄6:必須喺38隻股票池入⾯(港股⼀律唔喺池)
    in_pool = (market == "美股" and ticker.upper() in POOL)
    if not in_pool:
        blocks.append("
 唔喺你38隻股票池 → 訊號必須來⾃掃描器")
    # ⼤市環境
    if not is_bull:
        blocks.append("
 熊市環境 → 系統停⼿")
    # 路由
    if route == "TREND_DOWN":
        blocks.append("
 趨勢向下 → 唔做多")
    if route == "SKIP":
        blocks.append("
 數據不⾜,無法分流")
    # ---- 引擎⼀:均值回歸 ----
    if route == "MR":
        score = mr_score(row)
        plan = mr_plan(row)
        lines.append(f"引擎⼀(均值回歸) 評分: {score}  [OOS偏弱,觀察狀態]")
        if plan is None:
            blocks.append("
 無有效交易計劃")
        else:
            stop = plan["stop"]
            risk_pct = round((close - stop) / close * 100, 1)
            shares, cost = position_plan(close, stop)
            tier, reasons = classify_tier(row, score, plan, ticker)
            tier_map = {
                "PREMIUM": "
頂級", "STRONG": "
強",
                "BASIC": "
普通", None: "
無訊號",
            }
            lines.append(f"訊號級別: {tier_map.get(tier, '
無訊號')}")
            lines.append("")
            lines.append("── 交易計劃 ──")
            lines.append(f"入場: ${close}")
            lines.append(f"⽌蝕: ${stop}  (-{risk_pct}%)")
            if plan.get("target"):
                rew = round((plan["target"] - close) / close * 100, 1)
                lines.append(f"⽌盈: ${plan['target']}  (+{rew}%)")
                lines.append(f"R值:  {plan['r']}R")
            lines.append(f"建議股數: {shares}股 (~${cost})" if shares >= 1 else "建
            # 護欄
            if tier not in ("STRONG", "PREMIUM"):
                blocks.append(f"
 級別只係{tier_map.get(tier,'無訊號')} → 只做
強以
            if risk_pct > MAX_STOP_PCT:

                blocks.append(f"
 ⽌蝕距離{risk_pct}% > 15% → 波動失控")
            if shares < 1:
                blocks.append(f"
 1股風險${round(close-stop,1)} > 預算${round(ACCO
            if plan.get("r") is None or plan["r"] < MIN_R:
                blocks.append("
 R值未達2")
    # ---- 引擎⼆:趨勢跟蹤 ----
    elif route == "TREND_UP":
        tsc = trend_score(row)
        tplan = trend_plan(row)
        lines.append(f"引擎⼆(趨勢跟蹤) 評分: {tsc}  [OOS已驗證,主⼒]")
        if tplan is None:
            blocks.append("
 初始風險>12% 或 無有效計劃")
        else:
            stop = tplan["stop"]
            shares, cost = position_plan(close, stop)
            lines.append(f"訊號級別: {'
強' if tsc >= TREND_SCORE_MIN else '
未達
            lines.append("")
            lines.append("── 交易計劃 ──")
            lines.append(f"入場: ${close}")
            lines.append(f"初始⽌損: ${stop}  (-{tplan['risk_pct']}%)")
            lines.append(f"建議股數: {shares}股 (~${cost})" if shares >= 1 else "建
            lines.append("移動⽌損: 每⽇收市後 = 最⾼價 − 3×ATR,只升不降")
            lines.append("冇固定⽌盈 —— ⽌損被打先出")
            if tsc < TREND_SCORE_MIN:
                blocks.append(f"
 趨勢評分{tsc} < 0.65")
            if tplan["risk_pct"] > MAX_STOP_PCT:
                blocks.append(f"
 ⽌蝕距離{tplan['risk_pct']}% > 15%")
            if shares < 1:
                blocks.append("
 買唔起(需碎股)")
    # ---- 共同護欄:財報 / 投機股 ----
    if days_er is not None and 0 <= days_er <= 5:
        blocks.append(f"
 距財報只有{days_er}⽇ → 唔入")
    lines.append("")
    lines.append(f"距財報: {days_er if days_er is not None else '?(必須⾃⼰上網查)'}
    if is_spec:
        lines.append("投機股: 
係(半年波幅≥2倍)")
        blocks.append("
 投機股標記 → 加倍⼩⼼或跳過")
    # ============ 總結 ============
    lines.append("")
    lines.append("=" * 22)
    if blocks:
        lines.append("
 唔可以入場,原因:")
        for b in blocks:
            lines.append(f"  {b}")

    else:
        lines.append("
 ⾃動護欄全過")
        lines.append("最後⼀關:你⾃⼰認唔認同?(直覺唔妥=唔做)")
        lines.append("落單後即刻設⽌損 + 記⽇誌")
    if market == "港股":
        lines.append("\n
 港股:系統以美股回測,未經驗證,唔應該做")
    return "\n".join(lines)
# ============================================================
# Telegram 輪詢
# ============================================================
def get_updates(offset=None):
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    resp = requests.get(f"{API_URL}/getUpdates", params=params, timeout=35)
    return resp.json()
def send_message(chat_id, text):
    requests.post(f"{API_URL}/sendMessage", data={"chat_id": chat_id, "text": tex
def main():
    print("=" * 50)
    print("Swing Trade Telegram Bot 啟動中...")
    print("=" * 50)
    try:
        me = requests.get(f"{API_URL}/getMe", timeout=10).json()
        if not me.get("ok"):
            print(f"
 Token 無效: {me}")
            print("先跑 telegram_token_test.py 確認問題")
            return
        print(f"
 Bot 已連接: @{me['result']['username']}")
        print("在 Telegram 打開你的 bot，輸入股票代碼開始使⽤")
        print("（保持此視窗開著，關閉=bot停⽌回覆）")
        print("=" * 50)
    except Exception as e:
        print(f"
 連線失敗: {e}")
        return
    offset = None
    while True:

        try:
            updates = get_updates(offset)
            if not updates.get("ok"):
                print(f"取得訊息失敗: {updates}")
                time.sleep(5)
                continue
            for update in updates.get("result", []):
                offset = update["update_id"] + 1
                message = update.get("message", {})
                text = (message.get("text") or "").strip()
                chat_id = message.get("chat", {}).get("id")
                if not text or not chat_id:
                    continue
                print(f"收到訊息: {text} (chat_id={chat_id})")
                if text.startswith("/start"):
                    send_message(chat_id,
                        "歡迎使⽤ Swing Trade 查詢機械⼈！\n\n"
                        "輸入股票代碼即可查詢：\n"
                        "美股：AAPL、CVX、NVDA\n"
                        "港股：700、9988、1810\n\n"
                        "我會回覆訊號級別、⽌蝕⽌盈位置。")
                    continue
                send_message(chat_id, "分析中，請稍等...")
                try:
                    reply = analyze_and_format(text)
                except Exception as e:
                    reply = f"
 分析 {text} 時發⽣錯誤:\n{e}"
                send_message(chat_id, reply)
        except requests.exceptions.Timeout:
            continue
        except Exception as e:
            print(f"錯誤: {e}")
            time.sleep(5)
if __name__ == "__main__":
    main()
