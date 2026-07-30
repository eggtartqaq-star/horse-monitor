# -*- coding: utf-8 -*-
"""
============================================================
每⽇強訊號掃描器 V1.0
============================================================
⼀鍵掃描38隻股票,淨係列出「
強」同「
頂級」訊號。
普通訊號唔顯示,免得阻眼。
分級定義(同Telegram bot / signal_tier⼀致):
  
 頂級: 均值回歸 評分≥0.55 + 2R + RSI2<10 + R值≥3 + OBV背離 + 距財報>5天
  
 強  : 均值回歸 評分≥0.55 + 2R + RSI2<10 + R值≥3
  (趨勢引擎: 評分≥0.65 ⼀律視為強訊號候選,因為趨勢冇RSI2概念)
★ ⽤法規矩:每⽇收市後跑⼀次就夠,唔好開住成⽇等訊號。
  有訊號 → 記錄評估;冇訊號 → 閂機做第⼆啲嘢。
  ⼤部分⽇⼦冇強訊號係正常嘅。
執⾏:
  python daily_strong_signals.py
  或  雙擊桌⾯「掃描.bat」
============================================================
"""
import sys
import time
from datetime import datetime
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# 直接引⽤ V6.4 嘅邏輯(確保完全⼀致,改V6.4呢度⾃動跟)
try:
    import yfinance as yf
    from dual_engine_v6_4 import (
        TICKERS, calc_indicators, classify,
        mr_score, mr_plan, trend_score, trend_plan,
        check_guardrails, position_plan, get_days_to_earnings,
        MR_SCORE_MIN, TREND_SCORE_MIN, MIN_R,
    )
except ImportError as e:
    print("
 搵唔到 dual_engine_v6_4.py")
    print("   請確認 daily_strong_signals.py 同 dual_engine_v6_4.py 喺同⼀個資料夾")
    print(f"   ({e})")
    sys.exit(1)

def classify_mr_tier(row, score, plan, ticker):
    """均值回歸三級判定,回傳 'PREMIUM'/'STRONG'/'BASIC'/None"""
    if plan is None or plan.get("target") is None or plan.get("r") is None:
        return None
    r = plan["r"]
    rsi2 = row.get("RSI2")
    obv_div = bool(row.get("OBV_Div", False))
    if not (score >= 0.55 and r >= MIN_R):
        return None
    cond_rsi2 = pd.notna(rsi2) and rsi2 < 10
    cond_r3 = r >= 3.0
    is_strong = cond_rsi2 and cond_r3
    if not is_strong:
        return "BASIC"
    days_er = get_days_to_earnings(ticker)
    cond_er = days_er is not None and abs(days_er) > 5
    if obv_div and cond_er:
        return "PREMIUM"
    return "STRONG"
def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("=" * 60)
    print(f"每⽇強訊號掃描  {now}")
    print("只列 
強 同 
頂級,
普通唔顯示")
    print("=" * 60)
    # 市場環境
    spy = yf.Ticker("SPY").history(period="1y")
    spy["MA200"] = spy["Close"].rolling(200).mean()
    s = spy.iloc[-1]
    if pd.isna(s["MA200"]):
        print("SPY數據不⾜,今⽇不掃描。")
        return
    is_bull = s["Close"] > s["MA200"]
    gap = (s["Close"] - s["MA200"]) / s["MA200"] * 100
    print(f"\n市場環境: {'⽜市' if is_bull else '熊市'} "
          f"(SPY⾼於MA200 {gap:.1f}%)")
    if not is_bull:
        print("熊市環境,系統停⼿,今⽇唔搵做多訊號。")
        return
    print()
    strong_mr = []      # 均值回歸 強/頂級

    strong_trend = []   # 趨勢 強訊號
    for i, tk in enumerate(TICKERS):
        print(f"  掃描中 [{i+1}/{len(TICKERS)}] {tk}...", end="\r")
        try:
            df = yf.Ticker(tk).history(period="2y")
            if df.empty or len(df) < 100:
                continue
            df = calc_indicators(df)
            row = df.iloc[-1]
            route = classify(row)
            # ---- 引擎⼀:均值回歸(只要強/頂級)----
            if route == "MR":
                sc = mr_score(row)
                plan = mr_plan(row)
                if sc >= MR_SCORE_MIN and plan and plan.get("target"):
                    tier = classify_mr_tier(row, sc, plan, tk)
                    if tier in ("STRONG", "PREMIUM"):
                        risk_pct = (row["Close"] - plan["stop"]) / row["Close"] *
                        ok, flag, days_er = check_guardrails(tk, df, risk_pct)
                        shares, cost = position_plan(row["Close"], plan["stop"])
                        if ok and shares >= 1:
                            strong_mr.append({
                                "級別": "
頂級" if tier == "PREMIUM" else "
強",
                                "代號": tk, "評分": sc,
                                "入場": round(row["Close"], 2),
                                "⽌蝕": plan["stop"], "⽌盈": plan["target"],
                                "R值": plan["r"], "股數": shares, "投入$": cost,
                                "距財報": days_er if days_er is not None else "?",
                            })
            # ---- 引擎⼆:趨勢(評分≥0.65當強候選)----
            elif route == "TREND_UP":
                sc, _ = trend_score(row)
                plan = trend_plan(row)
                if sc >= TREND_SCORE_MIN and plan:
                    ok, flag, days_er = check_guardrails(tk, df, plan["risk_pct"]
                    shares, cost = position_plan(row["Close"], plan["stop"])
                    if ok and shares >= 1:
                        strong_trend.append({
                            "代號": tk, "趨勢評分": sc, "ADX": round(row["ADX"], 1)
                            "入場": round(row["Close"], 2),
                            "初始⽌蝕": plan["stop"], "風險%": plan["risk_pct"],
                            "股數": shares, "投入$": cost,
                            "距財報": days_er if days_er is not None else "?",
                        })

        except Exception:
            continue
        time.sleep(0.2)
    print(" " * 50, end="\r")
    # ---- 輸出 ----
    print("=" * 60)
    print("
 引擎⼆(趨勢跟蹤) 強訊號 —— OOS已驗證,主⼒")
    print("=" * 60)
    if strong_trend:
        df_t = pd.DataFrame(strong_trend).sort_values("趨勢評分", ascending=False)
        print(df_t.to_string(index=False))
    else:
        print("今⽇無趨勢強訊號")
    print()
    print("=" * 60)
    print("
 引擎⼀(均值回歸) 強/頂級訊號 —— OOS偏弱,觀察為主")
    print("=" * 60)
    if strong_mr:
        df_m = pd.DataFrame(strong_mr).sort_values("評分", ascending=False)
        print(df_m.to_string(index=False))
    else:
        print("今⽇無均值回歸強訊號")
    # 總結
    total = len(strong_trend) + len(strong_mr)
    print()
    print("=" * 60)
    if total == 0:
        print("
 今⽇無強訊號 —— 唔使交易,閂機做第⼆啲嘢。")
        print("   (⼤部分⽇⼦冇強訊號係正常,唔好焦慮,唔好為交易⽽交易)")
    else:
        print(f"
 今⽇共 {total} 個強訊號")
        print("   下⼀步: 揀⼀個 → 核對財報(距財報'?'要⾃⼰查) → 微⽜模擬倉落單")
        print("   → 記錄入⽇誌(訊號級別+入場+⽌蝕+⼼情)")
        print("   提醒: 引擎⼆為主⼒;每筆風險1%;⽌損絕不下移")
    print("=" * 60)
    # 儲存(有先儲)
    if strong_trend or strong_mr:
        rows = []
        for r in strong_trend:
            rows.append({"引擎": "趨勢", **r})
        for r in strong_mr:
            rows.append({"引擎": "均值回歸", **r})
        pd.DataFrame(rows).to_csv("daily_strong_signals.csv",

                                   index=False, encoding="utf-8-sig")
        print("已儲存: daily_strong_signals.csv")
if __name__ == "__main__":
    main()
    print("\n(掃描完成,按 Enter 關閉視窗)")
    try:
        input()
    except EOFError:
        pass
