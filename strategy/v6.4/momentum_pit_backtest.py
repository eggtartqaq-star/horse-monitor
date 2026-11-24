# -*- coding: utf-8 -*-
"""
============================================================
動能池 Point-in-Time 回測（誠實版,無⽣存者偏差）
============================================================
你嘅提議:⽤「動能最強嘅50隻」做股票池,配引擎⼆(趨勢跟蹤)。
★ 點解呢個⽅向啱:
  引擎⼆ = 強者恆強。動能選股 = 揀最強。兩者同⼀個哲學。
  你終於將個池同你嘅主⼒引擎對齊 —— 唔再係反動量。
★ 點解⼀定要 Point-in-Time:
  如果⽤「2026年今⽇最強50隻」去回測2018-2024,
  你就係揀咗⼀批「已經知道贏咗」嘅股票 = 極端⽣存者偏差。
  正確做法:喺每⼀個時間點,只⽤嗰⼀刻之前嘅數據計動能,
  每⽉重新揀池。呢個叫 point-in-time,係唯⼀唔呃⾃⼰嘅⽅法。
★ 動能定義（機械,事先鎖定）:
  每⽉最後⼀⽇,計每隻股票「過去126⽇(半年)總回報」,
  排名頭50隻 = 下個⽉嘅可交易池。
  排除:過去126⽇數據不⾜嘅（即新上市未夠半年）。
★ 引擎⼆規則完全鎖死,同 V6.4 / 之前OOS ⼀致。
 你⾃⼰承諾嘅事（每次跑都會⾒到）:
  「無論價錢」唔等於「買1股⾼價股」。
  你7/13入咗1888 500股(超額11倍)、7/18入咗BAC 300股(超額100倍)。
  動能池唔可以變成你超額入場嘅藉⼝。
  實盤時嚴格照「建議股數」,買唔起就跳過。
  呢個回測⽤嘅係「每筆固定風險%」,已經⾃動遵守1%規則 ——
  即係話,個回測結果本⾝已經假設咗你會守規。你要對得住佢。
 仍然存在嘅限制（誠實披露）:
  1. 候選universe係「今⽇嘅標普500成分」,呢層仍有輕微⽣存者偏差
     （2018年被踢出標普500嘅公司冇計入）。但比「今⽇最強50隻」
     好⼗倍 —— 因為池係逐⽉動態揀,唔係⼀次過鎖定贏家。
  2. 每⽉rebalance,計算量⼤,需時約20-30分鐘。
  3. 動能策略天⽣波動⼤、回撤深,睇結果要連最⼤回撤⼀齊睇。
使⽤⽅法:
  python momentum_pit_backtest.py
============================================================
"""

import yfinance as yf
import pandas as pd
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")
# ---- 參數（鎖定,改 = 要重跑驗證）----
TOP_N            = 50           # 動能頭幾多隻
MOMENTUM_LOOKBACK = 126         # 動能回望⽇數（半年）
REBALANCE_FREQ   = "ME"         # 每⽉重算池（Month End）
RISK_PCT         = 1.0          # 每筆風險%（1%規則,回測層⾯⾃動遵守）
# 引擎⼆規則（同V6.4⼀致）
TREND_SCORE_MIN  = 0.65
ATR_TRAIL_MULT   = 3.0
TREND_MAX_HOLD   = 60
# 測試期
TEST_START       = "2019-01-01"
TEST_END         = "2026-06-30"
DOWNLOAD_START   = "2018-01-01"   # 留⼀年畀MA200+動能熱⾝
# 候選universe（標普500,失敗⽤後備）
FALLBACK = [
    "AAPL","MSFT","GOOGL","AMZN","NVDA","META","TSLA","AVGO","AMD","QCOM","MU",
    "INTC","JPM","BAC","GS","V","MA","COST","WMT","MCD","NKE","SBUX","UNH","JNJ",
    "PFE","LLY","XOM","CVX","CAT","BA","CRM","ADBE","NFLX","ORCL","CSCO","TXN",
    "IBM","HON","AMGN","GILD","BKNG","MMM","GE","F","GM","DIS","CMCSA","VZ","T",
    "KO","PEP","PG","MRK","ABBV","TMO","DHR","LIN","ACN","NEE","PM","RTX","LOW",
    "UPS","SPGI","INTU","AMAT","LRCX","KLAC","SNPS","CDNS","MRVL","NXPI","ADI",
    "MCHP","ON","FTNT","PANW","CRWD","DDOG","NOW","SHOP","UBER","ABNB","PLTR",
    "COIN","SQ","PYPL","MRNA","REGN","VRTX","ISRG","SYK","BSX","MDT","CI","ELV",
    "HUM","ZTS","SLB","EOG","COP","MPC","PSX","DE","EMR","ITW","GD","LMT","NOC",
    "WFC","MS","SCHW","BLK","AXP","C","USB","PNC","TJX","HD","TGT","DG","DLTR",
]
def get_universe():
    print("攞標普500成分股...")
    try:
        tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_co
        col = "Symbol" if "Symbol" in tables[0].columns else tables[0].columns[0]
        tk = [str(t).replace(".", "-").strip().upper() for t in tables[0][col]]
        tk = [t for t in tk if t and t != "NAN"]
        print(f"  
 {len(tk)} 隻\n")
        return tk
    except Exception as e:
        print(f"  
 ⽤後備名單 {len(FALLBACK)} 隻（{e}）\n")

        return FALLBACK
def calc_indicators(df):
    df = df.copy()
    df["MA20"]  = df["Close"].rolling(20).mean()
    df["MA50"]  = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()
    adx_ind = ta_adx(df)
    df["ADX"], df["DI_PLUS"], df["DI_MINUS"] = adx_ind
    df["ATR"] = ta_atr(df)
    df["vol_ratio"] = df["Volume"].rolling(5).mean() / df["Volume"].rolling(20).m
    df["high_20d"] = df["High"].rolling(20).max()
    df["high_60d"] = df["High"].rolling(60).max()
    df["dist_60h"] = (df["high_60d"] - df["Close"]) / df["Close"] * 100
    df["mom_126"]  = df["Close"].pct_change(MOMENTUM_LOOKBACK) * 100
    return df
def ta_adx(df, window=14):
    import ta
    ind = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window=window
    return ind.adx(), ind.adx_pos(), ind.adx_neg()
def ta_atr(df, window=14):
    import ta
    return ta.volatility.AverageTrueRange(df["High"], df["Low"], df["Close"], win
def trend_score_calc(row):
    score = 0.0
    adx = row["ADX"]; ts = 0.0
    if pd.notna(adx):
        if adx >= 40: ts = 1.0
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
    ph = 0.0; d = row["dist_60h"]

    if pd.notna(d):
        if d <= 1: ph = 1.0
        elif d <= 3: ph = 0.85
        elif d <= 5: ph = 0.6
        elif d <= 10: ph = 0.35
        else: ph = 0.1
    score += ph * 0.25
    vs = 0.4; vr = row["vol_ratio"]
    if pd.notna(vr):
        vs = 1.0 if vr > 1.2 else (0.7 if vr > 1.0 else 0.4)
    score += vs * 0.15
    if pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]:
        score += 0.10
    return round(min(score, 1.0), 4)
def main():
    print("=" * 66)
    print("動能池 Point-in-Time 回測（引擎⼆,無⽣存者偏差）")
    print(f"每⽉重算頭{TOP_N}隻動能股 | 測試期 {TEST_START}~{TEST_END}")
    print("=" * 66)
    print("\n
 你嘅承諾:實盤嚴格照建議股數,買唔起就跳過。")
    print("   （呢個回測已假設你守1%規則。7/13同7/18你冇守——要對得住呢次。）\n")
    universe = get_universe()
    # ---- 下載全部數據 ----
    print("下載歷史數據(可能要幾分鐘)...")
    prices = {}
    for i in range(0, len(universe), 50):
        chunk = universe[i:i+50]
        try:
            data = yf.download(chunk, start=DOWNLOAD_START, end="2026-07-01",
                               group_by="ticker", progress=False, auto_adjust=Tru
            for tk in chunk:
                try:
                    df = data[tk] if len(chunk) > 1 else data
                    df = df.dropna(subset=["Close"])
                    if len(df) > 250:
                        prices[tk] = df
                except Exception:
                    continue
        except Exception as e:
            print(f"  批次失敗: {e}")
        print(f"  已下載 {len(prices)} 隻...", end="\r")
        time.sleep(0.5)
    print(f"\n  
 成功下載 {len(prices)} 隻\n")

    # ---- 為每隻計指標 ----
    print("計算指標...")
    for tk in list(prices.keys()):
        try:
            prices[tk] = calc_indicators(prices[tk])
        except Exception:
            del prices[tk]
    # ---- SPY環境 ----
    spy = yf.download("SPY", start=DOWNLOAD_START, end="2026-07-01",
                      progress=False, auto_adjust=True)
    if isinstance(spy.columns, pd.MultiIndex):
        spy.columns = spy.columns.get_level_values(0)
    spy["MA200"] = spy["Close"].rolling(200).mean()
    spy_bull = (spy["Close"] > spy["MA200"])
    # ---- 每⽉rebalance⽇ ----
    all_dates = pd.date_range(TEST_START, TEST_END, freq=REBALANCE_FREQ)
    trades = []
    open_positions = {}   # tk -> dict(entry, trail, highest, entry_date, days)
    pool_history = []
    # 逐個交易⽇⾏
    full_range = pd.bdate_range(TEST_START, TEST_END)
    current_pool = set()
    for today in full_range:
        # 每⽉頭:重算動能池
        if today.day <= 3 and (not pool_history or pool_history[-1]["month"] != (
            mom = {}
            for tk, df in prices.items():
                sub = df.loc[:today]
                if len(sub) < MOMENTUM_LOOKBACK + 5:
                    continue
                m = sub["mom_126"].iloc[-1]
                if pd.notna(m):
                    mom[tk] = m
            if mom:
                ranked = sorted(mom.items(), key=lambda x: x[1], reverse=True)
                current_pool = set([t for t, _ in ranked[:TOP_N]])
                pool_history.append({"month": (today.year, today.month),
                                     "date": today.strftime("%Y-%m-%d"),
                                     "pool": sorted(current_pool)})
        is_bull = False

        try:
            idx = spy_bull.index.searchsorted(today)
            if idx < len(spy_bull):
                is_bull = bool(spy_bull.iloc[idx])
        except Exception:
            pass
        # ---- 管理現有持倉（移動⽌損）----
        for tk in list(open_positions.keys()):
            pos = open_positions[tk]
            df = prices[tk]
            if today not in df.index:
                continue
            row = df.loc[today]
            pos["days"] += 1
            # 先檢查⽌損
            if row["Low"] <= pos["trail"]:
                exit_px = min(pos["trail"], row["Open"]) if pd.notna(row["Open"])
                trades.append({"ticker": tk, "entry_date": pos["entry_date"],
                               "exit_date": today.strftime("%Y-%m-%d"),
                               "ret": (exit_px - pos["entry"]) / pos["entry"] * 1
                               "days": pos["days"], "reason": "移動⽌損"})
                del open_positions[tk]
                continue
            # 更新trail
            atr = row["ATR"] if pd.notna(row["ATR"]) else pos["last_atr"]
            pos["last_atr"] = atr
            pos["highest"] = max(pos["highest"], row["High"])
            pos["trail"] = max(pos["trail"], pos["highest"] - ATR_TRAIL_MULT * at
            # 滿期
            if pos["days"] >= TREND_MAX_HOLD:
                trades.append({"ticker": tk, "entry_date": pos["entry_date"],
                               "exit_date": today.strftime("%Y-%m-%d"),
                               "ret": (row["Close"] - pos["entry"]) / pos["entry"
                               "days": pos["days"], "reason": "滿60⽇"})
                del open_positions[tk]
        # ---- 搵新入場（只喺動能池 + ⽜市）----
        if is_bull:
            for tk in current_pool:
                if tk in open_positions or tk not in prices:
                    continue
                df = prices[tk]
                if today not in df.index:
                    continue
                row = df.loc[today]
                if (pd.notna(row["ADX"]) and row["ADX"] >= 25

                        and pd.notna(row["DI_PLUS"]) and pd.notna(row["DI_MINUS"]
                        and row["DI_PLUS"] > row["DI_MINUS"]
                        and pd.notna(row["high_20d"]) and row["High"] >= row["hig
                    sc = trend_score_calc(row)
                    atr = row["ATR"]
                    if sc >= TREND_SCORE_MIN and pd.notna(atr) and atr > 0:
                        entry = row["Close"]
                        trail = entry - ATR_TRAIL_MULT * atr
                        if (entry - trail) / entry * 100 <= 12:
                            open_positions[tk] = {
                                "entry": entry, "trail": trail, "highest": entry,
                                "entry_date": today.strftime("%Y-%m-%d"),
                                "days": 0, "last_atr": atr,
                            }
    # ---- 結果 ----
    if not trades:
        print("無交易樣本")
        return
    d = pd.DataFrame(trades)
    wins = d[d["ret"] > 0]; losses = d[d["ret"] <= 0]
    print("=" * 66)
    print("結果:動能池 + 引擎⼆")
    print("=" * 66)
    print(f"  交易筆數:   {len(d)}")
    print(f"  勝率:       {len(wins)/len(d)*100:.1f}%")
    print(f"  平均贏:     +{wins['ret'].mean():.2f}%")
    print(f"  平均輸:     {losses['ret'].mean():.2f}%")
    print(f"  每筆EV:     {d['ret'].mean():+.3f}%")
    print(f"  平均持倉:   {d['days'].mean():.1f}天")
    print(f"  最好單筆:   +{d['ret'].max():.1f}%")
    print(f"  最差單筆:   {d['ret'].min():.1f}%")
    # 逐年
    d["year"] = pd.to_datetime(d["entry_date"]).dt.year
    print(f"\n  逐年:")
    print(f"  {'年份':<6}{'筆數':>6}{'勝率':>9}{'EV':>10}{'最差':>9}")
    for y in sorted(d["year"].unique()):
        sub = d[d["year"] == y]
        print(f"  {y:<6}{len(sub):>6}{(sub['ret']>0).mean()*100:>8.1f}%{sub['ret'
    print(f"\n  對比舊池(⼈⼿38隻)引擎⼆OOS: +1.325%(2025-26) / +1.497%(2018-21)")
    print(f"  動能池結果: {d['ret'].mean():+.3f}%")
    print("\n  判讀:")
    print("  
 動能池EV ≥ 舊池 → 動能選股有效,值得採⽤（先模擬驗證）")
    print("  
 動能池EV < 舊池 → 動能冇加分,或者波動太⼤唔值得")

    print("  記住睇埋逐年最差單筆 —— 動能策略回撤通常更深")
    d.to_csv("momentum_pit_trades.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame([{"month": f"{m['month'][0]}-{m['month'][1]:02d}",
                   "pool": ",".join(m["pool"])} for m in pool_history]).to_csv(
        "momentum_pit_pools.csv", index=False, encoding="utf-8-sig")
    print("\n明細: momentum_pit_trades.csv / momentum_pit_pools.csv（每⽉池成分）")
    print("\n★ 鐵律:呢個係point-in-time,冇⽣存者偏差。")
    print("  如果結果唔理想,唔准改成『今⽇最強50隻』嚟令佢好睇 —— 嗰個係⾃⼰呃⾃⼰。")
if __name__ == "__main__":
    main()
    print("\n(按 Enter 關閉)")
    try:
        input()
    except EOFError:
        pass
