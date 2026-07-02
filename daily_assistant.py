"""
============================================================
每日交易助手 V1.0（整合腳本）
============================================================
一個指令，依序完成：
  1. 市場環境檢查（SPY 200日均線）
  2. V4.1 信號掃描（38隻股票）
  3. 成交量異動掃描（美股+港股）
  4. 整理成一份清晰的總結報告

使用方法：
  python daily_assistant.py          ← 全部跑一次
  python daily_assistant.py quick    ← 只跑環境+V4.1（較快，跳過港股成交量）

輸出：
  daily_report.txt          （完整報告）
  v41_signals_today.csv     （V4.1信號）
  volume_scan_result.csv    （成交量異動）
============================================================
"""

import yfinance as yf
import pandas as pd
import numpy as np
import ta
import time
import sys
import io
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 設定
# ============================================================
US_TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO",
    "AMD", "QCOM", "MU", "INTC",
    "JPM", "BAC", "GS", "V", "MA",
    "COST", "WMT", "MCD", "NKE", "SBUX",
    "UNH", "JNJ", "PFE", "LLY",
    "XOM", "CVX", "CAT", "BA",
    "PLTR", "CRM", "ADBE", "NFLX", "SHOP", "UBER", "COIN", "MSTR"
]

HK_TICKERS = [
    "0700.HK", "9988.HK", "3690.HK", "1810.HK", "0941.HK",
    "0005.HK", "1299.HK", "0388.HK", "0939.HK", "1398.HK",
    "3988.HK", "2318.HK", "0883.HK", "0857.HK", "0386.HK",
    "2628.HK", "1024.HK", "9618.HK", "9999.HK", "2020.HK",
    "1211.HK", "0175.HK", "2382.HK", "0992.HK", "0981.HK",
]

FORWARD_DAYS = 10
MIN_R_RATIO  = 2.0
VOLUME_LOOKBACK = 20

# 收集報告文字（同時輸出到螢幕和檔案）
report_lines = []

def out(text=""):
    """同時印到螢幕並記錄到報告"""
    print(text)
    report_lines.append(text)


# ============================================================
# 第一部分：市場環境檢查
# ============================================================
def check_regime():
    out("=" * 60)
    out("【第一部分】市場環境檢查")
    out("=" * 60)
    try:
        spy = yf.Ticker("SPY").history(period="1y")
        spy["MA200"] = spy["Close"].rolling(200).mean()
        latest = spy.iloc[-1]
        spy_close = round(latest["Close"], 2)
        spy_ma200 = round(latest["MA200"], 2)
        is_bull = spy_close > spy_ma200
        gap_pct = round((spy_close - spy_ma200) / spy_ma200 * 100, 2)

        out(f"數據日期: {spy.index[-1].strftime('%Y-%m-%d')}")
        out(f"SPY收盤:  ${spy_close}")
        out(f"MA200:    ${spy_ma200}")
        if is_bull:
            out(f"結果: 牛市環境（高於MA200 {gap_pct}%）")
            out("→ 可以尋找做多均值回歸機會")
        else:
            out(f"結果: 熊市環境（低於MA200 {abs(gap_pct)}%）")
            out("→ 今日不做多，等待環境改善")
        out("")
        return is_bull
    except Exception as e:
        out(f"無法取得SPY數據: {e}")
        out("")
        return True


# ============================================================
# 技術指標計算（V4.1）
# ============================================================
def calc_indicators(df):
    df = df.copy()
    df["MA20"]  = df["Close"].rolling(20).mean()
    df["MA50"]  = df["Close"].rolling(50).mean()
    df["RSI14"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()
    df["RSI2"]  = ta.momentum.RSIIndicator(df["Close"], window=2).rsi()
    adx_ind     = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14)
    df["ADX"]   = adx_ind.adx()
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"]  = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"]  = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).mean()
    obv = ta.volume.OnBalanceVolumeIndicator(df["Close"], df["Volume"]).on_balance_volume()
    df["OBV"] = obv
    price_falling = df["Close"] < df["Close"].shift(5)
    obv_rising    = df["OBV"] > df["OBV"].shift(5)
    df["OBV_Div"] = price_falling & obv_rising
    df["low_10d"]  = df["Low"].rolling(10).min()
    df["high_60d"] = df["High"].rolling(60).max()
    return df


def score_v41(row):
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
        if rsi2 < 5:    rs2 = 1.0
        elif rsi2 < 10: rs2 = 0.85
        elif rsi2 < 20: rs2 = 0.70
        elif rsi2 < 30: rs2 = 0.50
        else:           rs2 = 0.20
        score += rs2 * 0.15
    pma20 = row["price_vs_ma20"]; ma_trend = row["ma20_vs_ma50"]
    if pd.notna(pma20) and pd.notna(ma_trend):
        if -5 <= pma20 <= 0 and ma_trend > 0:    ss = 1.0
        elif -10 <= pma20 < -5 and ma_trend > 0: ss = 0.8
        elif 0 < pma20 <= 3 and ma_trend > 0:    ss = 0.7
        elif pma20 < -10 and ma_trend > 0:        ss = 0.4
        else:                                      ss = 0.2
        score += ss * 0.20
    ret10 = row["ret_10d"]
    if pd.notna(ret10):
        if -15 <= ret10 <= -5:    rs3 = 1.0
        elif -20 <= ret10 < -15:  rs3 = 0.7
        elif -5 < ret10 <= -2:    rs3 = 0.5
        elif ret10 > 0:           rs3 = 0.1
        else:                     rs3 = 0.3
        score += rs3 * 0.20
    vol_ratio = row["vol_ratio"]; ret5 = row["ret_5d"]
    if pd.notna(vol_ratio) and pd.notna(ret5):
        if ret5 < 0 and vol_ratio > 1.3:    vs = 1.0
        elif ret5 < 0 and vol_ratio > 1.1:  vs = 0.8
        elif ret5 < 0 and vol_ratio > 0.9:  vs = 0.5
        elif ret5 >= 0 and vol_ratio > 1.2: vs = 0.6
        else:                                vs = 0.2
        score += vs * 0.15
    if pd.notna(row.get("OBV_Div")) and row["OBV_Div"]:
        score += 0.10
    return round(min(score, 1.0), 4)


def calc_2r(row):
    close = row["Close"]; low_10d = row["low_10d"]
    high_60d = row["high_60d"]; ma50 = row["MA50"]
    stop_loss = low_10d * 0.995
    risk = close - stop_loss
    if risk <= 0:
        return None, None, None
    targets = []
    if pd.notna(ma50) and ma50 > close:
        targets.append((ma50, (ma50 - close) / risk))
    if pd.notna(high_60d) and high_60d > close:
        targets.append((high_60d, (high_60d - close) / risk))
    valid = [(p, r) for p, r in targets if r >= MIN_R_RATIO]
    if not valid:
        return round(stop_loss, 2), None, None
    best = min(valid, key=lambda x: x[0])
    return round(stop_loss, 2), round(best[0], 2), round(best[1], 2)


# ============================================================
# 第二部分：V4.1 信號掃描
# ============================================================
def scan_v41(is_bull):
    out("=" * 60)
    out("【第二部分】V4.1 信號掃描")
    out("=" * 60)
    if not is_bull:
        out("熊市環境，跳過做多信號掃描。")
        out("")
        return []

    passed = []
    skipped_adx = 0
    for i, ticker in enumerate(US_TICKERS):
        print(f"  掃描中 [{i+1}/{len(US_TICKERS)}] {ticker}...", end="\r")
        try:
            df = yf.Ticker(ticker).history(period="2y")
            if df.empty or len(df) < 60:
                continue
            df = calc_indicators(df)
            latest = df.iloc[-1]
            if pd.notna(latest["ADX"]) and latest["ADX"] >= 25:
                skipped_adx += 1
                continue
            score = score_v41(latest)
            sl, tp, r = calc_2r(latest)
            if score >= 0.55 and r and r >= MIN_R_RATIO:
                passed.append({
                    "代號": ticker,
                    "評分": score,
                    "RSI14": round(latest["RSI14"], 1) if pd.notna(latest["RSI14"]) else "-",
                    "RSI2": round(latest["RSI2"], 1) if pd.notna(latest["RSI2"]) else "-",
                    "10日跌幅": round(latest["ret_10d"], 1) if pd.notna(latest["ret_10d"]) else "-",
                    "OBV背離": "有" if latest.get("OBV_Div") else "無",
                    "收盤": round(latest["Close"], 2),
                    "止蝕": sl, "止盈": tp, "R值": r,
                })
        except Exception:
            continue
        time.sleep(0.2)
    print(" " * 50, end="\r")  # 清除進度行

    if passed:
        df_p = pd.DataFrame(passed).sort_values("評分", ascending=False)
        out(f"找到 {len(df_p)} 隻通過2R+高評分的股票：\n")
        out(df_p.to_string(index=False))
        out("")
        out("入場詳情（前3隻）：")
        for _, row in df_p.head(3).iterrows():
            out(f"  {row['代號']}  評分{row['評分']}  R值{row['R值']}")
            out(f"    入場${row['收盤']}  止蝕${row['止蝕']}  止盈${row['止盈']}")
        df_p.to_csv("v41_signals_today.csv", index=False, encoding="utf-8-sig")
    else:
        out("今日無通過2R的信號。沒有好機會就不交易。")
    out(f"（已跳過{skipped_adx}隻ADX過高的股票）")
    out("")
    return passed


# ============================================================
# 第三部分：成交量異動掃描
# ============================================================
def analyze_volume(ticker):
    try:
        df = yf.Ticker(ticker).history(period="2mo")
        if df.empty or len(df) < VOLUME_LOOKBACK + 1:
            return None
        latest = df.iloc[-1]
        avg_vol = df["Volume"].iloc[-(VOLUME_LOOKBACK+1):-1].mean()
        if avg_vol == 0 or pd.isna(avg_vol):
            return None
        vol_ratio = latest["Volume"] / avg_vol
        prev_close = df["Close"].iloc[-2]
        daily_chg = (latest["Close"] - prev_close) / prev_close * 100
        return {
            "代號": ticker,
            "收盤": round(latest["Close"], 2),
            "日漲跌%": round(daily_chg, 2),
            "成交量比率": round(vol_ratio, 2),
        }
    except Exception:
        return None


def scan_volume(include_hk=True):
    out("=" * 60)
    out("【第三部分】成交量異動掃描")
    out("=" * 60)
    all_res = []
    tickers = US_TICKERS + (HK_TICKERS if include_hk else [])
    for i, ticker in enumerate(tickers):
        print(f"  掃描中 [{i+1}/{len(tickers)}] {ticker}...", end="\r")
        data = analyze_volume(ticker)
        if data:
            data["市場"] = "港股" if ".HK" in ticker else "美股"
            all_res.append(data)
        time.sleep(0.15)
    print(" " * 50, end="\r")

    if all_res:
        df = pd.DataFrame(all_res).sort_values("成交量比率", ascending=False)
        out("成交量異動最大 TOP 10（今日成交量 vs 20日均量）：\n")
        out(df[["市場","代號","收盤","日漲跌%","成交量比率"]].head(10).to_string(index=False))
        out("")
        # 放量上升
        rising = df[df["日漲跌%"] > 0].head(5)
        if len(rising) > 0:
            out("放量上升（可能買盤湧入）：")
            out(rising[["市場","代號","日漲跌%","成交量比率"]].to_string(index=False))
            out("")
        df.to_csv("volume_scan_result.csv", index=False, encoding="utf-8-sig")
    else:
        out("無成交量數據。")
    out("")
    return all_res


# ============================================================
# 主程式
# ============================================================
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"
    include_hk = (mode != "quick")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    out("#" * 60)
    out(f"# 每日交易助手報告  {now}")
    out("#" * 60)
    out("")

    # 依序執行三部分
    is_bull = check_regime()
    signals = scan_v41(is_bull)
    volumes = scan_volume(include_hk=include_hk)

    # 總結
    out("=" * 60)
    out("【今日總結】")
    out("=" * 60)
    out(f"市場環境: {'牛市（可交易）' if is_bull else '熊市（觀望）'}")
    out(f"V4.1信號: {len(signals)} 個通過2R")
    if signals:
        top = sorted(signals, key=lambda x: x['評分'], reverse=True)[0]
        out(f"最高評分: {top['代號']}（評分{top['評分']}, R值{top['R值']}）")
    out("")
    out("提醒：")
    out("- 實際入場價會與信號價不同，下單前重新確認R值是否仍達2R")
    out("- 每筆風險控制在1%（約HKD$100）")
    out("- 這是模擬交易累積階段，目標20筆")
    out("")

    # 儲存報告
    with open("daily_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    out("完整報告已儲存至 daily_report.txt")


if __name__ == "__main__":
    main()
