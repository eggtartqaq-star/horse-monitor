"""
============================================================
單一股票分析器 V1.0
============================================================
輸入股票代號，立即用V4.1系統分析是否值得入場

支援格式：
  美股：直接輸入字母，如 AAPL、CVX、NVDA
  港股：直接輸入數字，如 700、9988、1810（自動轉換格式）

使用方法：
  python stock_check.py AAPL       ← 分析美股
  python stock_check.py 700        ← 分析港股（騰訊）
  python stock_check.py            ← 互動模式（逐隻輸入）

分析內容：
  1. 市場環境（美股看SPY，港股看恒指）
  2. V4.1評分（RSI/支撐/跌幅/成交量/OBV）
  3. ADX趨勢過濾
  4. 2R止蝕止盈計算
  5. 明確結論：值得入場 / 觀察 / 不要碰
============================================================
"""

import yfinance as yf
import pandas as pd
import numpy as np
import ta
import sys
import warnings
warnings.filterwarnings("ignore")

MIN_R_RATIO = 2.0


# ============================================================
# 代號格式轉換
# ============================================================
def normalize_ticker(user_input):
    """
    自動識別港股/美股格式
    700 → 0700.HK
    9988 → 9988.HK
    AAPL → AAPL
    """
    s = user_input.strip().upper()
    if s.isdigit():
        # 港股：補齊4位數字 + .HK
        code = s.zfill(4)
        return f"{code}.HK", "港股"
    else:
        return s, "美股"


# ============================================================
# 市場環境檢查
# ============================================================
def check_market_regime(market):
    """美股看SPY，港股看恒指(^HSI)"""
    index_ticker = "SPY" if market == "美股" else "^HSI"
    index_name = "SPY" if market == "美股" else "恒生指數"
    try:
        idx = yf.Ticker(index_ticker).history(period="1y")
        idx["MA200"] = idx["Close"].rolling(200).mean()
        latest = idx.iloc[-1]
        is_bull = latest["Close"] > latest["MA200"]
        gap = (latest["Close"] - latest["MA200"]) / latest["MA200"] * 100
        return is_bull, f"{index_name} {'高於' if is_bull else '低於'}200日均線 {abs(gap):.1f}%"
    except Exception:
        return None, f"無法取得{index_name}數據"


# ============================================================
# 個股分析
# ============================================================
def analyze_stock(ticker, market):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="2y")
        if df.empty or len(df) < 60:
            return None, "數據不足（新股或代號錯誤？）"
    except Exception as e:
        return None, f"無法取得數據: {e}"

    # 計算指標
    df["MA20"]  = df["Close"].rolling(20).mean()
    df["MA50"]  = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    df["RSI14"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()
    df["RSI2"]  = ta.momentum.RSIIndicator(df["Close"], window=2).rsi()
    adx_ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=14)
    df["ADX"] = adx_ind.adx()
    df["price_vs_ma20"] = (df["Close"] - df["MA20"]) / df["MA20"] * 100
    df["ma20_vs_ma50"]  = (df["MA20"] - df["MA50"]) / df["MA50"] * 100
    df["ret_5d"]  = df["Close"].pct_change(5) * 100
    df["ret_10d"] = df["Close"].pct_change(10) * 100
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).mean()
    obv = ta.volume.OnBalanceVolumeIndicator(df["Close"], df["Volume"]).on_balance_volume()
    df["OBV"] = obv
    df["OBV_Div"] = (df["Close"] < df["Close"].shift(5)) & (df["OBV"] > df["OBV"].shift(5))
    df["low_10d"]  = df["Low"].rolling(10).min()
    df["high_60d"] = df["High"].rolling(60).max()

    latest = df.iloc[-1]
    return latest, None


def score_v41(row):
    """V4.1評分（回傳總分和各因子明細）"""
    detail = {}
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
        detail["RSI14超賣"] = rs

    rsi2 = row["RSI2"]
    if pd.notna(rsi2):
        if rsi2 < 5:    rs2 = 1.0
        elif rsi2 < 10: rs2 = 0.85
        elif rsi2 < 20: rs2 = 0.70
        elif rsi2 < 30: rs2 = 0.50
        else:           rs2 = 0.20
        score += rs2 * 0.15
        detail["RSI2觸發"] = rs2

    pma20 = row["price_vs_ma20"]; ma_trend = row["ma20_vs_ma50"]
    if pd.notna(pma20) and pd.notna(ma_trend):
        if -5 <= pma20 <= 0 and ma_trend > 0:    ss = 1.0
        elif -10 <= pma20 < -5 and ma_trend > 0: ss = 0.8
        elif 0 < pma20 <= 3 and ma_trend > 0:    ss = 0.7
        elif pma20 < -10 and ma_trend > 0:        ss = 0.4
        else:                                      ss = 0.2
        score += ss * 0.20
        detail["支撐位"] = ss

    ret10 = row["ret_10d"]
    if pd.notna(ret10):
        if -15 <= ret10 <= -5:    rs3 = 1.0
        elif -20 <= ret10 < -15:  rs3 = 0.7
        elif -5 < ret10 <= -2:    rs3 = 0.5
        elif ret10 > 0:           rs3 = 0.1
        else:                     rs3 = 0.3
        score += rs3 * 0.20
        detail["回調幅度"] = rs3

    vol_ratio = row["vol_ratio"]; ret5 = row["ret_5d"]
    if pd.notna(vol_ratio) and pd.notna(ret5):
        if ret5 < 0 and vol_ratio > 1.3:    vs = 1.0
        elif ret5 < 0 and vol_ratio > 1.1:  vs = 0.8
        elif ret5 < 0 and vol_ratio > 0.9:  vs = 0.5
        elif ret5 >= 0 and vol_ratio > 1.2: vs = 0.6
        else:                                vs = 0.2
        score += vs * 0.15
        detail["成交量"] = vs

    obv_div = bool(row.get("OBV_Div"))
    if obv_div:
        score += 0.10
    detail["OBV背離"] = 1.0 if obv_div else 0.0

    return round(min(score, 1.0), 4), detail


def calc_2r(row):
    close = row["Close"]; low_10d = row["low_10d"]
    high_60d = row["high_60d"]; ma50 = row["MA50"]
    stop_loss = low_10d * 0.995
    risk = close - stop_loss
    if risk <= 0:
        return None, None, None, None
    targets = []
    if pd.notna(ma50) and ma50 > close:
        targets.append((ma50, (ma50 - close) / risk))
    if pd.notna(high_60d) and high_60d > close:
        targets.append((high_60d, (high_60d - close) / risk))
    valid = [(p, r) for p, r in targets if r >= MIN_R_RATIO]
    if not valid:
        # 回傳最佳可得R值供參考
        best_r = max([r for _, r in targets], default=0)
        return round(stop_loss, 2), None, None, round(best_r, 2)
    best = min(valid, key=lambda x: x[0])
    return round(stop_loss, 2), round(best[0], 2), round(best[1], 2), round(best[1], 2)


# ============================================================
# 綜合判斷
# ============================================================
def make_verdict(is_bull, regime_msg, latest, score, detail, sl, tp, r, best_r, market):
    close = round(latest["Close"], 2)
    rsi14 = round(latest["RSI14"], 1) if pd.notna(latest["RSI14"]) else None
    rsi2  = round(latest["RSI2"], 1) if pd.notna(latest["RSI2"]) else None
    adx   = round(latest["ADX"], 1) if pd.notna(latest["ADX"]) else None
    ret10 = round(latest["ret_10d"], 1) if pd.notna(latest["ret_10d"]) else None
    is_range = adx is not None and adx < 25

    print("-" * 55)
    print("【指標數據】")
    print(f"  現價:      ${close}" if market == "美股" else f"  現價:      HK${close}")
    print(f"  RSI(14):   {rsi14}")
    print(f"  RSI(2):    {rsi2}")
    print(f"  ADX:       {adx} {'（橫盤，適合均值回歸）' if is_range else '（趨勢強，不適合）'}")
    print(f"  10日漲跌:  {ret10}%")
    print(f"  OBV背離:   {'有（資金可能低位流入）' if detail.get('OBV背離') else '無'}")

    print("-" * 55)
    print("【V4.1評分】")
    print(f"  總分: {score}  （入場門檻 ≥ 0.55）")

    print("-" * 55)
    print("【2R交易計劃】")
    if tp:
        risk_pct = (close - sl) / close * 100
        reward_pct = (tp - close) / close * 100
        print(f"  入場: ${close}")
        print(f"  止蝕: ${sl}  （風險 -{risk_pct:.1f}%）")
        print(f"  止盈: ${tp}  （回報 +{reward_pct:.1f}%）")
        print(f"  R值:  {r} ✓ 通過2R")
    else:
        print(f"  止蝕: ${sl}")
        print(f"  最佳可得R值: {best_r}（未達2R門檻）")

    # 綜合判斷
    print("=" * 55)
    print("【結論】")

    checks = {
        "市場環境（牛市）": is_bull,
        "ADX橫盤（<25）": is_range,
        "評分達標（≥0.55）": score >= 0.55,
        "2R通過": tp is not None,
    }
    for name, ok in checks.items():
        print(f"  {'✓' if ok else '✗'} {name}")

    passed = sum(checks.values())
    print()
    if passed == 4:
        print("  🟢 值得入場：全部條件通過")
        print("  → 可以考慮模擬下單，記得：")
        print("    1. 實際入場價要重新確認R值（CVX教訓）")
        print("    2. 每筆風險1%（約HKD$100）")
    elif checks["市場環境（牛市）"] and checks["評分達標（≥0.55）"] and not checks["2R通過"]:
        print("  🟡 觀察名單：評分夠但2R不通過")
        print("  → 等回調更深或結構改善再看")
    elif not checks["市場環境（牛市）"]:
        print("  🔴 不要碰：市場環境是熊市")
        print("  → 大環境不對，任何個股信號都不可靠")
    elif not checks["ADX橫盤（<25）"]:
        print("  🔴 不要碰：趨勢太強（ADX≥25）")
        print("  → 強趨勢中「超賣」可以更超賣，等ADX回落")
    else:
        print("  ⚪ 不符合條件：評分不足")
        print("  → 這隻股票現在不是均值回歸的好目標")

    if market == "港股":
        print()
        print("  ⚠️ 港股注意：你的V4.1是用美股回測的，")
        print("     港股結果僅供參考，未經驗證。")


# ============================================================
# 主程式
# ============================================================
def analyze_one(user_input):
    ticker, market = normalize_ticker(user_input)
    print()
    print("=" * 55)
    print(f"分析 {ticker}（{market}）")
    print("=" * 55)

    # 市場環境
    is_bull, regime_msg = check_market_regime(market)
    if is_bull is None:
        print(f"環境檢查失敗: {regime_msg}")
        is_bull = True  # 無法確認時保守放行但註明
    print(f"市場環境: {regime_msg}")

    # 個股分析
    latest, err = analyze_stock(ticker, market)
    if latest is None:
        print(f"分析失敗: {err}")
        return

    score, detail = score_v41(latest)
    sl, tp, r, best_r = calc_2r(latest)
    make_verdict(is_bull, regime_msg, latest, score, detail, sl, tp, r, best_r, market)


def main():
    if len(sys.argv) > 1:
        # 命令列模式：python stock_check.py AAPL
        analyze_one(sys.argv[1])
    else:
        # 互動模式
        print("=" * 55)
        print("單一股票分析器（輸入 q 離開）")
        print("美股輸入字母（AAPL），港股輸入數字（700）")
        print("=" * 55)
        while True:
            user_input = input("\n輸入股票代號: ").strip()
            if user_input.lower() in ["q", "quit", "exit", ""]:
                print("再見！")
                break
            analyze_one(user_input)


if __name__ == "__main__":
    main()
