# -*- coding: utf-8 -*-
"""
============================================================
V6.5 — 組合層模擬器 (Tom 嘅 U-1)
============================================================
呢個檔案取代 oos_validation.py 同 momentum_pit_backtest.py 嘅統計部分。

點解要重寫,唔係修補:
  舊嘅兩個腳本報「每筆EV」。每筆EV答唔到你真正想知嘅嘢 ——
    「呢個系統最衰會蝕幾多?」
  你嘅整套代碼入面搵唔到一條計最大回撤嘅式。grep 得返兩句廣東話註釋
  提你「記得睇回撤」,零行代碼真係計。

呢度修正咗嘅嘢(每項對應審計findings):
  C-2  每筆成交兩邊都計成本(佣金+差價+滑價+匯兌)
  C-3  真現金帳、整數股、同時持倉上限、總熱度上限
  D-02 資產淨值曲線 → 最大回撤、回撤持續日數、最差月份、尾部
  H-1  訊號喺 bar t 收市,成交喺 bar t+1 開市 —— 完全冇前視
  F-03 COOLDOWN 真係執行(V6.4 宣告咗但冇用)
  F-04 到期未平嘅倉唔會靜靜雞消失,會標記 OPEN_AT_END
  F-07 止蝕闊度由 rules.py 單一來源提供
  ★    每一個被擋嘅訊號都會記低 —— 拒絕紀錄本身就係一個發現

用法:
    python portfolio_sim.py --mode diagnostics     # 先跑呢個,免費,~5分鐘
    python portfolio_sim.py --mode sim --broker ibkr_fixed
    python portfolio_sim.py --mode sim --broker free    # 對比 V6.4 嘅隱含假設

★ 先跑 diagnostics。如果 EV 集中喺三四隻股身上,生存者偏差就係全部答案,
  唔使再建其他嘢。—— Tom
============================================================
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

from rules import RULES, add_indicators, mr_score, trend_score, mr_stop, mr_target, is_speculative
from risk_config import BROKERS, LIMITS, Blocked, plan_position

TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO",
    "AMD", "QCOM", "MU", "INTC",
    "JPM", "BAC", "GS", "V", "MA",
    "COST", "WMT", "MCD", "NKE", "SBUX",
    "UNH", "JNJ", "PFE", "LLY",
    "XOM", "CVX", "CAT", "BA",
    "PLTR", "CRM", "ADBE", "NFLX", "SHOP", "UBER", "COIN", "MSTR",
]

# 粗略板塊對照,淨係用嚟做 max_per_sector。★ 唔係正式 GICS。
SECTOR = {
    **{t: "semi" for t in ["NVDA", "AMD", "QCOM", "MU", "INTC", "AVGO"]},
    **{t: "megatech" for t in ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA"]},
    **{t: "software" for t in ["CRM", "ADBE", "NFLX", "SHOP", "UBER", "PLTR"]},
    **{t: "crypto" for t in ["COIN", "MSTR"]},
    **{t: "fin" for t in ["JPM", "BAC", "GS", "V", "MA"]},
    **{t: "consumer" for t in ["COST", "WMT", "MCD", "NKE", "SBUX"]},
    **{t: "health" for t in ["UNH", "JNJ", "PFE", "LLY"]},
    **{t: "energy_ind" for t in ["XOM", "CVX", "CAT", "BA"]},
}


# ============================================================
# 數據
# ============================================================

def preflight():
    """開頭就檢查環境,唔好行到一半先死。"""
    missing = []
    for m in ("yfinance", "pandas", "numpy"):
        try:
            __import__(m)
        except ImportError:
            missing.append(m)
    if missing:
        print("★ 缺少套件:" + ", ".join(missing))
        print("  裝法:  pip install " + " ".join(missing))
        sys.exit(1)
    try:
        import yfinance as yf
        t = yf.Ticker("SPY").history(period="5d")
        if len(t) == 0:
            raise RuntimeError("回傳空數據")
    except Exception as e:
        print("★ 攞唔到市場數據 —— yfinance 連唔到 Yahoo。")
        print(f"  錯誤: {type(e).__name__}: {str(e)[:120]}")
        print("  常見原因:公司/學校網絡封鎖、VPN、或者 yfinance 版本太舊。")
        print("  試下:  pip install -U yfinance   然後喺屋企網絡再跑。")
        sys.exit(1)
    print("環境檢查 OK — yfinance 連得到。\n")


def load(tickers, start, end):
    import yfinance as yf
    print(f"下載 {len(tickers)} 隻 + SPY ({start} → {end})...")
    out = {}
    for i, tk in enumerate(tickers, 1):
        try:
            df = yf.Ticker(tk).history(start=start, end=end, auto_adjust=True)
            if len(df) < 300:
                print(f"  [{i}/{len(tickers)}] {tk} 數據不足 ({len(df)}) — 跳過")
                continue
            df.index = pd.to_datetime(df.index).tz_localize(None)
            out[tk] = add_indicators(df)
            print(f"  [{i}/{len(tickers)}] {tk} {len(df)} 條", end="\r")
        except Exception as e:
            print(f"  [{i}/{len(tickers)}] {tk} 失敗: {e}")
    spy = yf.Ticker("SPY").history(start=start, end=end, auto_adjust=True)
    spy.index = pd.to_datetime(spy.index).tz_localize(None)
    spy["MA200"] = spy["Close"].rolling(RULES.REGIME_MA).mean()
    # ★ 落後 N 條 bar —— 用尋日嘅環境判斷今日,冇前視
    spy["bull"] = (spy["Close"] > spy["MA200"]).shift(RULES.REGIME_LAG_BARS).fillna(False)
    print(f"\n  成功 {len(out)} 隻,SPY {len(spy)} 條\n")
    return out, spy


# ============================================================
# 訊號 — 喺 bar i 收市判斷,bar i+1 開市成交
# ============================================================

def signal_at(df, i, is_bull):
    """回傳 dict(engine, stop, target, score) 或 None。只用 bar i 及之前嘅資料。"""
    if not is_bull or i < 200:
        return None
    row = df.iloc[i]
    adx = row["ADX"]
    if pd.isna(adx) or pd.isna(row["ATR"]) or row["ATR"] <= 0:
        return None
    close = row["Close"]

    # ---- 引擎一:均值回歸 ----
    if adx < RULES.ADX_RANGE_MAX:
        sc = mr_score(row)
        if sc < RULES.MR_SCORE_MIN:
            return None
        stop = mr_stop(row)
        target = mr_target(row)
        if stop is None or target is None or stop >= close:
            return None
        r = (target - close) / (close - stop)
        if r < RULES.MR_MIN_R:
            return None
        # ★ V6.4 嘅回測完全冇呢個過濾,但 live 有。呢次終於一致。
        if (close - stop) / close * 100 > RULES.MR_STOP_WIDTH_MAX_PCT:
            return None
        return {"engine": "E1", "stop": stop, "target": target,
                "score": sc, "r": r, "trail_mult": None}

    # ---- 引擎二:趨勢 ----
    if (adx >= RULES.ADX_TREND_MIN
            and pd.notna(row["DI_PLUS"]) and pd.notna(row["DI_MINUS"])
            and row["DI_PLUS"] > row["DI_MINUS"]
            and pd.notna(row["high_20d"]) and row["High"] >= row["high_20d"]):
        sc = trend_score(row)
        if sc < RULES.TREND_SCORE_MIN:
            return None
        stop = close - RULES.TREND_ATR_TRAIL_MULT * row["ATR"]
        if stop <= 0 or (close - stop) / close * 100 > RULES.TREND_STOP_WIDTH_MAX_PCT:
            return None
        return {"engine": "E2", "stop": stop, "target": None,
                "score": sc, "r": None,
                "trail_mult": RULES.TREND_ATR_TRAIL_MULT}
    return None


# ============================================================
# 模擬器
# ============================================================

def simulate(data, spy, broker_key="ibkr_fixed", limits=LIMITS, verbose=True):
    cost = BROKERS[broker_key]
    cash = limits.account_usd
    equity_hist, open_pos, trades, rejects = [], {}, [], []
    cooldown = defaultdict(lambda: pd.Timestamp.min)
    concurrency = []

    all_dates = sorted(set().union(*[set(d.index) for d in data.values()]))
    all_dates = [d for d in all_dates if d in spy.index]
    # 需要 bar i 同 bar i+1,所以最後一日唔開新倉
    idx_of = {tk: {d: n for n, d in enumerate(df.index)} for tk, df in data.items()}

    for day_n, today in enumerate(all_dates):
        is_bull = bool(spy.at[today, "bull"]) if today in spy.index else False

        # ---------- 1. 管理現有倉位 ----------
        for tk in list(open_pos.keys()):
            pos = open_pos[tk]
            df = data[tk]
            if today not in idx_of[tk]:
                continue
            i = idx_of[tk][today]
            row = df.iloc[i]
            pos["days"] += 1
            exit_px = exit_reason = None

            # ★ 先檢查止蝕,後更新移動止蝕 —— 唔可以掉轉
            if row["Low"] <= pos["stop"]:
                # 跳空保護:開市價已經低於止蝕就用開市價
                exit_px = min(pos["stop"], row["Open"]) if pd.notna(row["Open"]) else pos["stop"]
                exit_reason = "止蝕"
            elif pos["target"] is not None and row["High"] >= pos["target"]:
                exit_px, exit_reason = pos["target"], "止盈"
            elif pos["days"] >= pos["max_hold"]:
                exit_px, exit_reason = row["Close"], f"滿{pos['max_hold']}日"

            if exit_px is None and pos["trail_mult"]:
                a = row["ATR"] if pd.notna(row["ATR"]) else pos["last_atr"]
                pos["last_atr"] = a
                pos["highest"] = max(pos["highest"], row["High"])
                pos["stop"] = max(pos["stop"], pos["highest"] - pos["trail_mult"] * a)

            if exit_px is not None:
                sh = pos["shares"]
                gross = (exit_px - pos["entry"]) * sh
                c = cost.round_trip(pos["entry"] * sh, exit_px * sh, sh)
                cash += exit_px * sh - cost.one_side(exit_px * sh, sh)
                trades.append({
                    "ticker": tk, "engine": pos["engine"],
                    "entry_date": pos["entry_date"], "exit_date": today,
                    "entry": pos["entry"], "exit": exit_px, "shares": sh,
                    "days": pos["days"], "reason": exit_reason,
                    "gross_usd": gross, "cost_usd": c, "net_usd": gross - c,
                    "gross_pct": (exit_px - pos["entry"]) / pos["entry"] * 100,
                    "net_pct": (gross - c) / (pos["entry"] * sh) * 100,
                    "risk_usd": pos["risk_usd"],
                    "r_multiple": (gross - c) / pos["risk_usd"] if pos["risk_usd"] else np.nan,
                })
                cd = RULES.MR_COOLDOWN if pos["engine"] == "E1" else RULES.TREND_COOLDOWN
                cooldown[tk] = today + pd.Timedelta(days=cd)
                del open_pos[tk]

        # ---------- 2. 按市值計淨值 ----------
        mtm = 0.0
        for tk, pos in open_pos.items():
            if today in idx_of[tk]:
                mtm += pos["shares"] * data[tk].iloc[idx_of[tk][today]]["Close"]
            else:
                mtm += pos["shares"] * pos["entry"]
        equity = cash + mtm
        equity_hist.append({"date": today, "equity": equity, "cash": cash,
                            "positions": len(open_pos), "exposure_pct": mtm / equity * 100})
        concurrency.append(len(open_pos))

        # 回撤預算:超過就停手(唔係建議)
        # ★ 自我審計 MEDIUM-2:呢個係「終止開關」,唔係會自動重置嘅斷路器。
        #   一旦觸發,除非淨值升返到距離高位 20% 以內,否則之後每一個交易日
        #   都唔會再開新倉 —— 而冇新倉通常就升唔返。當佢係永久停手。
        peak = max(e["equity"] for e in equity_hist)
        if (peak - equity) / peak * 100 > limits.drawdown_budget_pct:
            rejects.append({"date": today, "ticker": "-", "reason": "回撤預算耗盡",
                            "detail": f"DD {(peak-equity)/peak*100:.1f}%"})
            continue

        if day_n + 1 >= len(all_dates):
            continue
        tomorrow = all_dates[day_n + 1]

        # ---------- 3. 搵新訊號(bar i 判斷) ----------
        heat = sum(p["risk_usd"] for p in open_pos.values()) / equity * 100
        sector_n = Counter(SECTOR.get(t, "other") for t in open_pos)
        candidates = []
        for tk, df in data.items():
            if tk in open_pos or today < cooldown[tk] or today not in idx_of[tk]:
                continue
            i = idx_of[tk][today]
            if tomorrow not in idx_of[tk]:
                continue
            sig = signal_at(df, i, is_bull)
            if sig is None:
                continue
            if is_speculative(df, i):
                rejects.append({"date": today, "ticker": tk,
                                "reason": "投機股", "detail": "126日高低 >= 2x"})
                continue
            sig["ticker"], sig["next_i"] = tk, idx_of[tk][tomorrow]
            candidates.append(sig)

        # 訊號多過位:分數高者先。★ V6.4 冇呢個問題因為佢冇上限。
        candidates.sort(key=lambda s: -s["score"])

        # ---------- 4. 落單(bar i+1 開市成交) ----------
        for sig in candidates:
            tk = sig["ticker"]
            entry = data[tk].iloc[sig["next_i"]]["Open"]
            if pd.isna(entry) or entry <= sig["stop"]:
                rejects.append({"date": today, "ticker": tk, "reason": "跳空穿止蝕",
                                "detail": f"開市 {entry:.2f} <= 止蝕 {sig['stop']:.2f}"})
                continue
            # ★ 自我審計 MEDIUM-1:止蝕闊度要用「真實成交價」再驗一次。
            #   訊號喺 bar t 收市計,成交喺 bar t+1 開市 —— 跳空會令實際風險
            #   偏離當初檢查嗰個數。引擎二喺 20 日新高突破日入場,正正就係
            #   最容易跳空嗰啲日子。倉位計算一直用 entry-stop,本身冇錯;
            #   錯嘅係個「閘」用咗收市價去檢查。
            cap = (RULES.MR_STOP_WIDTH_MAX_PCT if sig["engine"] == "E1"
                   else RULES.TREND_STOP_WIDTH_MAX_PCT)
            actual_width = (entry - sig["stop"]) / entry * 100
            if actual_width > cap:
                rejects.append({"date": today, "ticker": tk, "reason": "跳空後止蝕過闊",
                                "detail": f"成交價計 {actual_width:.1f}% > 上限 {cap:.0f}%"})
                continue
            try:
                plan = plan_position(entry, sig["stop"], equity, len(open_pos),
                                     heat, cash, sector_n[SECTOR.get(tk, "other")], limits)
            except Blocked as b:
                rejects.append({"date": today, "ticker": tk,
                                "reason": b.reason, "detail": b.detail})
                continue
            entry_cost = cost.one_side(plan["notional"], plan["shares"])
            if cash < plan["notional"] + entry_cost:
                rejects.append({"date": today, "ticker": tk, "reason": "現金不足",
                                "detail": f"需 ${plan['notional']+entry_cost:.2f} 有 ${cash:.2f}"})
                continue
            cash -= plan["notional"] + entry_cost
            heat += plan["risk_pct_of_equity"]
            sector_n[SECTOR.get(tk, "other")] += 1
            open_pos[tk] = {
                "engine": sig["engine"], "entry": entry, "entry_date": tomorrow,
                "shares": plan["shares"], "stop": sig["stop"], "target": sig["target"],
                "trail_mult": sig["trail_mult"], "highest": entry,
                "last_atr": data[tk].iloc[sig["next_i"]]["ATR"],
                "days": 0, "risk_usd": plan["risk_usd"],
                "max_hold": RULES.MR_MAX_HOLD if sig["engine"] == "E1" else RULES.TREND_MAX_HOLD,
                "budget_used_pct": plan["budget_used_pct"],
            }

    # ---------- 收尾:未平倉唔可以消失 ----------
    for tk, pos in open_pos.items():
        last = data[tk].iloc[-1]
        gross = (last["Close"] - pos["entry"]) * pos["shares"]
        c = cost.round_trip(pos["entry"] * pos["shares"], last["Close"] * pos["shares"], pos["shares"])
        trades.append({
            "ticker": tk, "engine": pos["engine"], "entry_date": pos["entry_date"],
            "exit_date": data[tk].index[-1], "entry": pos["entry"], "exit": last["Close"],
            "shares": pos["shares"], "days": pos["days"], "reason": "OPEN_AT_END",
            "gross_usd": gross, "cost_usd": c, "net_usd": gross - c,
            "gross_pct": (last["Close"] - pos["entry"]) / pos["entry"] * 100,
            "net_pct": (gross - c) / (pos["entry"] * pos["shares"]) * 100,
            "risk_usd": pos["risk_usd"],
            "r_multiple": (gross - c) / pos["risk_usd"] if pos["risk_usd"] else np.nan,
        })

    return (pd.DataFrame(trades), pd.DataFrame(equity_hist),
            pd.DataFrame(rejects), concurrency, cost)


# ============================================================
# 報告 —— 醜陋嘅數字行先
# ============================================================

def report(trades, eq, rejects, concurrency, cost, limits=LIMITS):
    print("=" * 68)
    print(f"組合模擬結果 — 券商: {cost.name}")
    print("=" * 68)
    if eq.empty or trades.empty:
        print("冇交易。")
        return

    eq = eq.set_index("date")
    start_eq, end_eq = limits.account_usd, eq["equity"].iloc[-1]
    peak = eq["equity"].cummax()
    dd = (eq["equity"] - peak) / peak * 100
    max_dd = dd.min()
    trough = dd.idxmin()
    # 回撤持續:由高位到重返高位
    peak_date = eq.loc[:trough, "equity"].idxmax()
    rec = eq.loc[trough:][eq.loc[trough:, "equity"] >= eq.at[peak_date, "equity"]]
    dd_days = ((rec.index[0] if len(rec) else eq.index[-1]) - peak_date).days

    print("\n── 先講醜嘅 ──")
    print(f"  最大回撤          {max_dd:.2f}%   (由 {peak_date.date()} 到 {trough.date()})")
    print(f"  回撤持續          {dd_days} 日" + ("" if len(rec) else "  ★ 到測試結束都未收復"))
    m = eq["equity"].resample("ME").last().pct_change() * 100
    if len(m.dropna()):
        print(f"  最差月份          {m.min():.2f}%  ({m.idxmin().strftime('%Y-%m')})")
    print(f"  最差單筆(淨)      {trades['net_pct'].min():.2f}%")
    p5 = trades["net_pct"].quantile(0.05)
    print(f"  第5百分位交易      {p5:.2f}%")
    print(f"  最差5筆            " + ", ".join(
        f"{r.ticker} {r.net_pct:.1f}%" for r in
        trades.nsmallest(5, "net_pct").itertuples()))

    print("\n── 然後先講好嘅 ──")
    tot = (end_eq / start_eq - 1) * 100
    yrs = max((eq.index[-1] - eq.index[0]).days / 365.25, 1e-9)
    print(f"  期初 / 期末       US${start_eq:,.2f}  →  US${end_eq:,.2f}   ({tot:+.2f}%)")
    print(f"  年化(CAGR)      {((end_eq/start_eq)**(1/yrs)-1)*100:+.2f}%")
    dr = eq["equity"].pct_change().dropna()
    if dr.std() > 0:
        print(f"  Sharpe(無風險0)  {dr.mean()/dr.std()*np.sqrt(252):.2f}")
        dn = dr[dr < 0]
        if len(dn) and dn.std() > 0:
            print(f"  Sortino           {dr.mean()/dn.std()*np.sqrt(252):.2f}")
    print(f"  平均曝險          {eq['exposure_pct'].mean():.1f}%   "
          f"(即係有 {100-eq['exposure_pct'].mean():.0f}% 時間資金閒置)")

    print("\n── 交易 ──")
    w = trades[trades["net_pct"] > 0]
    print(f"  筆數 {len(trades)}   勝率 {len(w)/len(trades)*100:.1f}%   "
          f"平均持倉 {trades['days'].mean():.1f} 日")
    print(f"  每筆EV(毛)       {trades['gross_pct'].mean():+.3f}%")
    print(f"  每筆EV(淨)       {trades['net_pct'].mean():+.3f}%   "
          f"← 呢個先係真嘅")
    eaten = trades["cost_usd"].sum() / max(abs(trades["gross_usd"].sum()), 1e-9) * 100
    print(f"  總成本            US${trades['cost_usd'].sum():.2f}  "
          f"(= 毛利嘅 {eaten:.1f}%)")
    print(f"  平均R倍數(淨)     {trades['r_multiple'].mean():+.2f}R")
    n_open = (trades["reason"] == "OPEN_AT_END").sum()
    if n_open:
        print(f"  ★ {n_open} 筆到期未平 —— 已按市值計入,冇丟棄(V6.4 會丟)")

    print("\n  按引擎:")
    for e, g in trades.groupby("engine"):
        print(f"    {e}  {len(g):>4}筆  勝率{(g['net_pct']>0).mean()*100:>5.1f}%  "
              f"淨EV{g['net_pct'].mean():+.3f}%")

    print("\n── 集中度:EV 係咪只靠幾隻股? ──")
    by_tk = trades.groupby("ticker").agg(n=("net_usd", "size"), pnl=("net_usd", "sum")).sort_values("pnl", ascending=False)
    tot_pnl = by_tk["pnl"].sum()
    top3 = by_tk.head(3)["pnl"].sum()
    print(f"  頭3隻貢獻 US${top3:.2f} / 總 US${tot_pnl:.2f}", end="")
    print(f"  = {top3/tot_pnl*100:.0f}%" if abs(tot_pnl) > 1e-9 else "")
    print("  頭5:  " + ", ".join(f"{t} ${r.pnl:+.0f}({r.n})" for t, r in by_tk.head(5).iterrows()))
    print("  尾5:  " + ", ".join(f"{t} ${r.pnl:+.0f}({r.n})" for t, r in by_tk.tail(5).iterrows()))
    print("  ★ 如果頭3隻佔咗大部分,生存者偏差就係全部答案。")

    print("\n── 同時持倉分佈 ──")
    c = Counter(concurrency)
    for k in sorted(c):
        print(f"    {k} 個倉: {c[k]:>5} 日 ({c[k]/len(concurrency)*100:>5.1f}%)")

    if not rejects.empty:
        print("\n── 被擋嘅訊號(呢個本身就係發現) ──")
        for reason, n in rejects["reason"].value_counts().items():
            print(f"    {reason:<20} {n:>5}")
        print(f"    {'總計':<20} {len(rejects):>5}")
        print("  ★ 「買唔起」/「集中度」佔大多數 = 戶口太細,唔係策略唔得。")

    trades.to_csv("v65_trades.csv", index=False, encoding="utf-8-sig")
    eq.to_csv("v65_equity.csv", encoding="utf-8-sig")
    rejects.to_csv("v65_rejects.csv", index=False, encoding="utf-8-sig")
    print("\n已儲存: v65_trades.csv / v65_equity.csv / v65_rejects.csv")


def diagnostics(data, spy):
    """Tom 嘅免費30分鐘檢查。喺起模擬器之前跑。"""
    print("=" * 68)
    print("免費診斷 —— 跑呢個之前唔好寫任何新代碼")
    print("=" * 68)
    bull = spy["bull"]
    print(f"\n1. 環境覆蓋率")
    print(f"   牛市日數佔比: {bull.mean()*100:.1f}%")
    print(f"   ★ 系統淨係喺牛市做多。如果呢個數 > 80%,你嘅『4年數據』")
    print(f"     其實只係一個環境嘅4年,獨立證據遠少過你以為。")
    yr = bull.groupby(bull.index.year).mean() * 100
    print("   逐年牛市%: " + "  ".join(f"{y}:{v:.0f}%" for y, v in yr.items()))

    print(f"\n2. 訊號分佈(未計倉位、未計成本)")
    counts, per_tk = Counter(), Counter()
    for tk, df in data.items():
        for i in range(200, len(df)):
            d = df.index[i]
            if d not in spy.index:
                continue
            s = signal_at(df, i, bool(spy.at[d, "bull"]))
            if s:
                counts[s["engine"]] += 1
                per_tk[tk] += 1
    print(f"   引擎一 {counts['E1']} 個 / 引擎二 {counts['E2']} 個")
    print(f"   訊號最多: " + ", ".join(f"{t}:{n}" for t, n in per_tk.most_common(5)))
    print(f"   訊號最少: " + ", ".join(f"{t}:{n}" for t, n in per_tk.most_common()[-5:]))
    print(f"   ★ 如果訊號集中喺幾隻,個池就唔係38隻,係幾隻。")


def compare(data, spy, limits=LIMITS):
    """
    同一批數據、同一批訊號,唯一分別係券商成本。
    ★ 呢個係整套 V6.5 最重要嘅一張表。
      「free」嗰行就係 V6.4 一直隱含假設緊嘅世界。
      其他行係你真係要住喺入面嘅世界。
    """
    rows = []
    for key in ("free", "ibkr_tiered", "ibkr_fixed", "hk_retail"):
        trades, eq, rej, conc, cost = simulate(data, spy, key, limits)
        if trades.empty or eq.empty:
            rows.append({"broker": key, "n": 0}); continue
        e = eq.set_index("date")["equity"]
        peak = e.cummax()
        rows.append({
            "broker": key,
            "name": cost.name,
            "n": len(trades),
            "win": (trades["net_pct"] > 0).mean() * 100,
            "gross_ev": trades["gross_pct"].mean(),
            "net_ev": trades["net_pct"].mean(),
            "cost_usd": trades["cost_usd"].sum(),
            "end_equity": e.iloc[-1],
            "total_ret": (e.iloc[-1] / limits.account_usd - 1) * 100,
            "max_dd": ((e - peak) / peak * 100).min(),
        })

    print("=" * 78)
    print("券商成本對比 —— 同一批訊號,唯一分別係手續費")
    print("=" * 78)
    print(f"\n{'券商':<14}{'筆數':>6}{'勝率':>8}{'毛EV':>9}{'淨EV':>9}"
          f"{'總成本':>10}{'期末':>11}{'總回報':>9}{'最大回撤':>10}")
    print("-" * 78)
    base = None
    for r in rows:
        if not r.get("n"):
            print(f"{r['broker']:<14}{'冇交易':>6}"); continue
        if base is None:
            base = r["net_ev"]
        print(f"{r['broker']:<14}{r['n']:>6}{r['win']:>7.1f}%"
              f"{r['gross_ev']:>+8.3f}%{r['net_ev']:>+8.3f}%"
              f"{r['cost_usd']:>9.0f}${r['end_equity']:>10.0f}"
              f"{r['total_ret']:>+8.1f}%{r['max_dd']:>9.1f}%")
    print("-" * 78)

    valid = [r for r in rows if r.get("n")]
    if len(valid) >= 2:
        free = next((r for r in valid if r["broker"] == "free"), valid[0])
        print("\n每個券商食咗你幾多優勢(相對「免費」):")
        for r in valid:
            if r["broker"] == "free":
                continue
            lost = free["net_ev"] - r["net_ev"]
            pct = lost / abs(free["net_ev"]) * 100 if abs(free["net_ev"]) > 1e-9 else float("inf")
            verdict = "★ 優勢全部被食晒" if r["net_ev"] <= 0 < free["net_ev"] else ""
            print(f"  {r['broker']:<14} −{lost:.3f}pp  (= 免費EV嘅 {pct:.0f}%)  {verdict}")
        print("\n★ 「free」嗰行 = V6.4 一直報畀你聽嘅數字。")
        print("  其餘每一行 = 你真係會攞到嘅數字。兩者之差就係之前冇人計過嘅錢。")
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["diagnostics", "sim", "compare"], default="diagnostics")
    ap.add_argument("--broker", choices=list(BROKERS), default="ibkr_fixed")
    ap.add_argument("--start", default="2019-01-01")
    ap.add_argument("--end", default="2026-07-01")
    a = ap.parse_args()

    preflight()
    data, spy = load(TICKERS, a.start, a.end)
    if not data:
        print("冇數據。"); sys.exit(1)
    if a.mode == "diagnostics":
        diagnostics(data, spy)
        print("\n★ 睇完先決定使唔使跑 --mode sim / --mode compare。")
    elif a.mode == "compare":
        compare(data, spy).to_csv("v65_broker_compare.csv", index=False, encoding="utf-8-sig")
        print("\n已儲存: v65_broker_compare.csv")
    else:
        report(*simulate(data, spy, a.broker))
        print("\n★ 想一次過睇曬所有券商:  python portfolio_sim.py --mode compare")


if __name__ == "__main__":
    main()
