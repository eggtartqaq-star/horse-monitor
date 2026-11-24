# -*- coding: utf-8 -*-
"""
V6.6 回測實驗室 —— 用 V6.4.2 真規則,以「你實際點交易」嘅方式重跑
=====================================================================
V6.4 嘅 OOS 數字(引擎二 +1.325%)係「每筆EV」,條件係:
  收市判斷 + 同一個收市價成交 + 零成本 + 冇倉位上限 + 每個訊號都做到。
但你實際係:收市後掃描 → 聽日開市落單(偏離>1%重計) → 最多2倉 →
  名義值 ≤ 戶口10% → 唔可以買碎股 → 月熔斷10%。

呢個檔案將兩種量度並排:
  as_tested  = V6.4 回測嘅假設(用嚟對返你舊數字)
  as_traded  = 你真正執行嘅方式(呢個先係你會拎到嘅結果)
然後喺 as_traded 之上,逐次只改一樣嘢做 A/B(手冊第十二節嘅紀律)。

用法(你部電腦,有 yfinance):
    python lab.py --source yf
用法(CSV 資料夾,每隻一個 TICKER.csv,欄位 Date,Open,High,Low,Close,Volume):
    python lab.py --source csv --data ./data
"""
import argparse
import os
import sys
from dataclasses import dataclass, replace, field
from typing import Optional

import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rules_v642 as R                      # noqa: E402
from indicators import calc_indicators      # noqa: E402

VERSION = "V6.6-lab 2026-11-24"

# ============================================================
# 拆股表 —— 倉位計算要用「當時真實股價」,唔可以用拆股調整後嘅價
# ============================================================
# yfinance / Webull 歷史價係拆股調整過嘅:WMT 2023 年顯示 ~$48,其實當時 ~$145。
# 名義上限 US$128 同「買唔買得起1股」完全取決於真實股價,所以要還原。
# 回報% 唔受影響。★ 呢張表只包括 2022-11 之後、而 2026-06 之前已知嘅拆股;
#   之後嘅拆股要自己加(格式:日期 = 拆股後第一個交易日,比例 = 新股數/舊股數)。
SPLITS = {
    "WMT":  [("2024-02-26", 3)],
    "NVDA": [("2024-06-10", 10)],
    "AVGO": [("2024-07-15", 10)],
    "NFLX": [("2025-11-17", 10)],
}


def raw_factor(tk, d):
    """調整後價 × factor = 當日真實股價。"""
    f = 1.0
    for ds, ratio in SPLITS.get(tk, []):
        if d < pd.Timestamp(ds):
            f *= ratio
    return f


# ============================================================
# 成本模型
# ============================================================
@dataclass(frozen=True)
class Broker:
    name: str
    min_comm: float = 0.0        # 每邊最低佣金 US$
    per_share: float = 0.0       # 每股 US$
    bp_side: float = 0.0         # 差價+滑價,每邊基點(假設)

    def side_cost(self, notional, shares):
        return max(self.min_comm, self.per_share * shares) + self.bp_side / 1e4 * notional


BROKERS = {
    "free": Broker("零成本(V6.4回測隱含假設)"),
    # 手冊:微牛零佣金。差價+滑價 10bp/邊係假設,唔係查證過嘅數。
    "webull0": Broker("微牛零佣金 + 10bp/邊差價滑價(假設)", 0.0, 0.0, 10.0),
    # 壓力情境:如果其實有平台費/最低收費
    "min1": Broker("每邊最低US$1 + 10bp(壓力情境)", 1.0, 0.0, 10.0),
}


# ============================================================
# 實驗設定
# ============================================================
@dataclass(frozen=True)
class Cfg:
    name: str
    fill: str = "next_open"          # "close" = V6.4回測;"next_open" = 你實際
    broker: str = "webull0"
    engines: tuple = ("E1", "E2")
    max_positions: Optional[int] = 2  # None = 每個訊號都做(每筆EV模式)
    notional_cap: bool = True
    fractional: bool = False
    deviation_pct: Optional[float] = 1.0   # 開市偏離訊號價 >1% → 重計,唔達標放棄
    month_breaker_pct: Optional[float] = 10.0
    e1_gap_fill: bool = True         # 引擎一跳空穿止蝕以開市價出(V6.4回測冇)
    mom_filter: Optional[str] = None  # "top_half" = 引擎二只做126日動能前50%
    account_hkd: float = 10000.0
    # 敏感度測試用(預設 = V6.4.2 鎖死值)
    trend_score_min: float = R.TREND_SCORE_MIN
    trail_mult: float = R.ATR_TRAIL_MULT
    mr_score_min: float = R.MR_SCORE_MIN
    min_r: float = R.MIN_R
    mr_atr_mult: float = R.ATR_STOP_MULT
    mr_max_hold: int = R.MR_MAX_HOLD
    trend_max_hold: int = R.TREND_MAX_HOLD


def build_signal(e, cfg):
    """由預先計算嘅原始欄位,用 cfg 參數砌返 V6.4.2 訊號。預設參數 = 真 mr_plan/trend_plan。"""
    k = e.get("kind")
    if k == "MR":
        if e["score"] < cfg.mr_score_min:
            return None
        if (cfg.min_r == R.MIN_R and cfg.mr_atr_mult == R.ATR_STOP_MULT):
            plan = e["plan"]                                  # 原汁原味
        else:
            close, atr = e["close"], e["atr"]
            if pd.isna(e["low10"]) or pd.isna(atr) or atr <= 0:
                return None
            stop = min(e["low10"] * 0.995, close - cfg.mr_atr_mult * atr)
            risk = close - stop
            if risk <= 0:
                return None
            t = [(p, (p - close) / risk) for p in (e["ma50"], e["h60"]) if pd.notna(p) and p > close]
            v = [x for x in t if x[1] >= cfg.min_r]
            plan = None if not v else {"stop": round(stop, 2), "target": round(min(v)[0], 2)}
        if not plan:
            return None
        if (e["close"] - plan["stop"]) / e["close"] * 100 > R.MAX_STOP_PCT_MR:
            return None
        return {"engine": "E1", "score": e["score"], "stop": plan["stop"], "target": plan["target"]}
    if k == "TR":
        if e["score"] < cfg.trend_score_min or pd.isna(e["atr"]) or e["atr"] <= 0:
            return None
        stop = e["close"] - cfg.trail_mult * e["atr"]
        if (e["close"] - stop) / e["close"] * 100 > R.MAX_STOP_PCT_TREND:
            return None
        return {"engine": "E2", "score": e["score"], "stop": round(stop, 2), "target": None}
    return None


AS_TESTED = Cfg("as_tested(V6.4回測假設)", fill="close", broker="free", max_positions=None,
                notional_cap=False, deviation_pct=None, month_breaker_pct=None, e1_gap_fill=False)
AS_TRADED = Cfg("as_traded(你實際執行)")


# ============================================================
# 數據
# ============================================================
def load_csv(folder, tickers):
    out = {}
    for tk in tickers:
        p = os.path.join(folder, f"{tk}.csv")
        if not os.path.exists(p):
            print(f"  ⚠ 缺 {tk}")
            continue
        df = pd.read_csv(p, parse_dates=["Date"]).set_index("Date").sort_index()
        out[tk] = df[["Open", "High", "Low", "Close", "Volume"]].astype(float)
    return out


def load_yf(tickers, period="5y"):
    import yfinance as yf
    out = {}
    for tk in tickers:
        df = yf.Ticker(tk).history(period=period, auto_adjust=True)
        if df.empty:
            print(f"  ⚠ 缺 {tk}")
            continue
        df.index = df.index.tz_localize(None).normalize()
        out[tk] = df[["Open", "High", "Low", "Close", "Volume"]]
    return out


# ============================================================
# 預先計算每隻股每日嘅訊號(用 V6.4.2 真函數)
# ============================================================
def precompute(data):
    spy = data["SPY"].copy()
    spy["MA200"] = spy["Close"].rolling(200).mean()
    bull = (spy["Close"] > spy["MA200"]) & spy["MA200"].notna()

    sig = {}
    for tk in R.TICKERS:
        if tk not in data:
            continue
        df = calc_indicators(data[tk])
        df["bull"] = bull.reindex(df.index).ffill().fillna(False).astype(bool)
        recs = []
        for i, (dt, row) in enumerate(df.iterrows()):
            e = {"route": "SKIP"}
            if i >= 80 and row["bull"]:
                route = R.classify(row)
                e["route"] = route
                if route == "MR":
                    plan = R.mr_plan(row)          # 用 V6.4.2 真函數(MIN_R=2)
                    e.update(kind="MR", score=R.mr_score(row), close=row["Close"],
                             atr=row["ATR"], low10=row["low_10d"], ma50=row["MA50"],
                             h60=row["high_60d"], plan=plan)
                elif route == "TREND_UP" and R.trend_entry_ok(row):
                    e.update(kind="TR", score=R.trend_score(row), close=row["Close"], atr=row["ATR"])
            recs.append(e)
        df["sig"] = recs
        sig[tk] = df
    return sig, bull


# ============================================================
# 模擬器
# ============================================================
class Pos:
    __slots__ = ("tk", "engine", "entry", "stop", "target", "shares", "edate", "days",
                 "highest", "atr", "sig_date")


def simulate(sig, cfg: Cfg, start=None, end=None):
    broker = BROKERS[cfg.broker]
    acct_usd = cfg.account_hkd / R.USD_HKD
    dates = sorted(set().union(*[set(df.index) for df in sig.values()]))
    dates = [d for d in dates if (start is None or d >= pd.Timestamp(start))
             and (end is None or d <= pd.Timestamp(end))]
    idx = {tk: {d: k for k, d in enumerate(df.index)} for tk, df in sig.items()}
    arr = {tk: df for tk, df in sig.items()}

    open_pos, pending, trades, equity = [], [], [], []
    busy_until = {}                     # 同一隻股出場當日唔再入
    rejects = {"no_slot": 0, "notional_or_risk_0_shares": 0, "deviation": 0,
               "breaker": 0, "mom_filter": 0}
    realized = 0.0
    month_pnl, cur_month = 0.0, None
    unlimited = cfg.max_positions is None

    def close_trade(p, d, px, reason):
        nonlocal realized, month_pnl
        gross = (px - p.entry) / p.entry * 100
        if unlimited:
            cost_pct = 2 * broker.bp_side / 100 + (2 * broker.min_comm / max(p.entry, 1e-9) * 100 if broker.min_comm else 0)
            pnl_usd = None
            net = gross - (2 * broker.bp_side / 100)
        else:
            c = broker.side_cost(p.entry * p.shares, p.shares) + broker.side_cost(px * p.shares, p.shares)
            pnl_usd = (px - p.entry) * p.shares - c
            net = pnl_usd / (p.entry * p.shares) * 100
            realized += pnl_usd
            month_pnl += pnl_usd
        trades.append({"ticker": p.tk, "engine": p.engine, "sig_date": p.sig_date, "entry_date": p.edate,
                       "exit_date": d, "entry": p.entry, "exit": px, "days": p.days,
                       "gross_pct": gross, "net_pct": net, "pnl_usd": pnl_usd,
                       "shares": p.shares, "reason": reason})
        busy_until[p.tk] = d

    def manage(p, row, d):
        """處理持倉喺 bar d。回傳 True = 已出場。"""
        p.days += 1
        o, h, l, c = row["Open"], row["High"], row["Low"], row["Close"]
        if p.engine == "E1":
            if l <= p.stop:
                px = o if (cfg.e1_gap_fill and o < p.stop) else p.stop
                close_trade(p, d, px, "止蝕"); return True
            if h >= p.target:
                close_trade(p, d, p.target, "止盈"); return True
            if p.days >= cfg.mr_max_hold:
                close_trade(p, d, c, "滿10日"); return True
            return False
        # E2:先檢查、後更新(同 V6.4.2 bt 一致)
        if l <= p.stop:
            px = o if o < p.stop else p.stop
            close_trade(p, d, px, "移動止損"); return True
        if pd.notna(row["ATR"]) and row["ATR"] > 0:
            p.atr = row["ATR"]
        p.highest = max(p.highest, h)
        p.stop = max(p.stop, p.highest - cfg.trail_mult * p.atr)
        if p.days >= cfg.trend_max_hold:
            close_trade(p, d, c, "滿60日"); return True
        return False

    def open_position(tk, s, d, px, sig_date, atr_sig):
        stop = s["stop"]
        if cfg.fill == "next_open" and cfg.deviation_pct is not None:
            dev = abs(px - s["sig_close"]) / s["sig_close"] * 100
            if dev > cfg.deviation_pct:
                # 手冊第七節:重計 R值/風險,唔達標放棄
                if px <= stop:
                    rejects["deviation"] += 1; return None
                if s["engine"] == "E1":
                    if (s["target"] - px) / (px - stop) < cfg.min_r:
                        rejects["deviation"] += 1; return None
                else:
                    if (px - stop) / px * 100 > R.MAX_STOP_PCT_TREND:
                        rejects["deviation"] += 1; return None
        if px <= stop:
            rejects["deviation"] += 1; return None
        if unlimited:
            sh = 1
        else:
            f = raw_factor(tk, d)              # 用真實股價計股數同名義上限
            sh_raw, _ = R.position_plan(px * f, stop * f, account_hkd=cfg.account_hkd,
                                        max_position_pct=R.MAX_POSITION_PCT if cfg.notional_cap else 1e9,
                                        fractional=cfg.fractional)
            if sh_raw <= 0:
                rejects["notional_or_risk_0_shares"] += 1; return None
            sh = sh_raw * f                    # 換算返調整後股數,$ 計算全部喺調整後價格做
        p = Pos()
        p.tk, p.engine, p.entry, p.stop, p.target = tk, s["engine"], px, stop, s.get("target")
        p.shares, p.edate, p.days, p.highest, p.atr, p.sig_date = sh, d, 0, px, atr_sig, sig_date
        return p

    for d in dates:
        m = (d.year, d.month)
        if m != cur_month:
            cur_month, month_pnl = m, 0.0

        # 1) 開市成交上一日嘅掛單(next_open 模式)
        if pending:
            new_pending = []
            for (tk, s, sig_date, atr_sig) in pending:
                k = idx[tk].get(d)
                if k is None:
                    continue
                row = arr[tk].iloc[k]
                p = open_position(tk, s, d, row["Open"], sig_date, atr_sig)
                if p is not None:
                    open_pos.append(p)
                    if manage(p, row, d):          # 入場當日都可以觸發止蝕
                        open_pos.remove(p)
            pending = new_pending

        # 2) 管理持倉(今日 bar)
        still = []
        for p in open_pos:
            if p.edate == d and cfg.fill == "next_open":
                still.append(p); continue          # 今日先入,已處理
            k = idx[p.tk].get(d)
            if k is None:
                still.append(p); continue
            if not manage(p, arr[p.tk].iloc[k], d):
                still.append(p)
        open_pos = still

        # 3) 收市後掃描
        cands = []
        held = {p.tk for p in open_pos} | {x[0] for x in pending}
        moms = {}
        if cfg.mom_filter:
            for tk, df in arr.items():
                k = idx[tk].get(d)
                if k is not None and pd.notna(df["mom_126"].iloc[k]):
                    moms[tk] = df["mom_126"].iloc[k]
            ranked = sorted(moms, key=moms.get, reverse=True)
            top = set(ranked[: max(1, len(ranked) // 2)])
        for tk, df in arr.items():
            k = idx[tk].get(d)
            if k is None or tk in held or busy_until.get(tk) == d:
                continue
            s = build_signal(df["sig"].iloc[k], cfg)
            eng = s.get("engine") if s else None
            if eng is None or eng not in cfg.engines:
                continue
            if cfg.mom_filter and eng == "E2" and tk not in top:
                rejects["mom_filter"] += 1
                continue
            s = dict(s); s["sig_close"] = df["Close"].iloc[k]
            cands.append((0 if eng == "E2" else 1, -s["score"], tk, s, df["ATR"].iloc[k], k))
        cands.sort()

        breaker = (cfg.month_breaker_pct is not None and not unlimited
                   and month_pnl <= -cfg.month_breaker_pct / 100 * acct_usd)
        for _, _, tk, s, atr_sig, k in cands:
            if breaker:
                rejects["breaker"] += 1; continue
            if not unlimited and len(open_pos) + len(pending) >= cfg.max_positions:
                rejects["no_slot"] += 1; continue
            if cfg.fill == "close":
                p = open_position(tk, s, d, s["sig_close"], d, atr_sig)
                if p is not None:
                    open_pos.append(p)
            else:
                pending.append((tk, s, d, atr_sig))

        # 4) 淨值(按收市價計)
        if not unlimited:
            mtm = 0.0
            for p in open_pos:
                k = idx[p.tk].get(d)
                if k is not None:
                    mtm += (arr[p.tk]["Close"].iloc[k] - p.entry) * p.shares
            equity.append((d, acct_usd + realized + mtm, len(open_pos)))

    # 數據結束:強制平倉
    for p in open_pos:
        df = arr[p.tk]
        close_trade(p, df.index[-1], df["Close"].iloc[-1], "數據結束")
    tr = pd.DataFrame(trades)
    eq = pd.DataFrame(equity, columns=["date", "equity", "n_pos"]).set_index("date") if equity else None
    return tr, eq, rejects


# ============================================================
# 統計
# ============================================================
def block_bootstrap_ci(x, block=10, n=2000, seed=7):
    """按入場日排序嘅交易做 block bootstrap(保留時間聚集)。樣本 <30 唔計 —— 唔可信。"""
    x = np.asarray(x, float)
    if len(x) < 30:
        return (np.nan, np.nan)
    block = max(2, min(block, len(x) // 5))
    rng = np.random.default_rng(seed)
    nb = int(np.ceil(len(x) / block))
    means = []
    for _ in range(n):
        starts = rng.integers(0, max(1, len(x) - block + 1), nb)
        sample = np.concatenate([x[s:s + block] for s in starts])[: len(x)]
        means.append(sample.mean())
    return tuple(np.percentile(means, [5, 95]))


def summarize(tr, eq, label=""):
    out = {"label": label}
    done = tr[tr["reason"] != "數據結束"] if len(tr) else tr
    out["trades"] = len(done)
    if len(done):
        out["win%"] = (done["net_pct"] > 0).mean() * 100
        out["EV_gross%"] = done["gross_pct"].mean()
        out["EV_net%"] = done["net_pct"].mean()
        d2 = done.sort_values("entry_date")
        lo, hi = block_bootstrap_ci(d2["net_pct"].values)
        out["EV_net_90CI"] = f"[{lo:+.2f}, {hi:+.2f}]"
        out["avg_days"] = done["days"].mean()
        out["best%"] = done["net_pct"].max()
        out["worst%"] = done["net_pct"].min()
        top = done.groupby("ticker")["pnl_usd" if done["pnl_usd"].notna().any() else "net_pct"].sum()
        tot = top.sum()
        out["top3_share%"] = (top.sort_values(ascending=False).head(3).sum() / tot * 100) if tot > 0 else np.nan
    if eq is not None and len(eq):
        e = eq["equity"]
        yrs = (e.index[-1] - e.index[0]).days / 365.25
        out["start$"] = e.iloc[0]
        out["end$"] = e.iloc[-1]
        out["CAGR%"] = ((e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1) * 100 if yrs > 0 else np.nan
        dd = e / e.cummax() - 1
        out["maxDD%"] = dd.min() * 100
        out["exposure%"] = (eq["n_pos"] > 0).mean() * 100
        out["pnl$"] = e.iloc[-1] - e.iloc[0]
    return out


def bench(data, start, end):
    res = {}
    for k in ("SPY",):
        s = data[k]["Close"]
        s = s[(s.index >= pd.Timestamp(start)) & (s.index <= pd.Timestamp(end))]
        yrs = (s.index[-1] - s.index[0]).days / 365.25
        res[k] = ((s.iloc[-1] / s.iloc[0]) ** (1 / yrs) - 1) * 100
    rets = []
    for tk in R.TICKERS:
        if tk in data:
            s = data[tk]["Close"]
            s = s[(s.index >= pd.Timestamp(start)) & (s.index <= pd.Timestamp(end))]
            if len(s) > 10:
                rets.append(s.iloc[-1] / s.iloc[0])
    yrs = (pd.Timestamp(end) - pd.Timestamp(start)).days / 365.25
    res["EW38"] = (np.mean(rets) ** (1 / yrs) - 1) * 100
    return res


PER_TRADE = replace(AS_TESTED, name="per_trade(聽日開市+10bp)", fill="next_open",
                    deviation_pct=1.0, broker="webull0")


def periods(first, last, is_end):
    return {"ALL": (first, last), "IS": (first, is_end), "OOS": (is_end + pd.Timedelta(days=1), last)}


def run_ab(sig, data, first, last, is_end, out):
    exps = [
        AS_TESTED,
        replace(AS_TESTED, name="as_tested+成本10bp", broker="webull0"),
        PER_TRADE,
        AS_TRADED,
        replace(AS_TRADED, name="A1 只做引擎二", engines=("E2",)),
        replace(AS_TRADED, name="A2 引擎二動能前50%", mom_filter="top_half"),
        replace(AS_TRADED, name="M1 量度:碎股", fractional=True),
        replace(AS_TRADED, name="M2 量度:壓力成本US$1/邊", broker="min1"),
        replace(AS_TRADED, name="M4 量度:冇名義上限(整數股)", notional_cap=False),
    ]
    rows = []
    for cfg in exps:
        for per, (s, e) in periods(first, last, is_end).items():
            tr, eq, rej = simulate(sig, cfg, s, e)
            for eng in ("ALL", "E1", "E2"):
                sub = tr if eng == "ALL" or len(tr) == 0 else tr[tr["engine"] == eng]
                r = summarize(sub, eq if eng == "ALL" else None)
                r.update(exp=cfg.name, period=per, engine=eng)
                if eng == "ALL":
                    r.update({f"rej_{k}": v for k, v in rej.items()})
                rows.append(r)
            if per == "ALL":
                safe = "".join(ch if ch.isalnum() else "_" for ch in cfg.name)[:40]
                tr.to_csv(os.path.join(out, f"trades_{safe}.csv"), index=False, encoding="utf-8-sig")
                if eq is not None:
                    eq.to_csv(os.path.join(out, f"equity_{safe}.csv"), encoding="utf-8-sig")
        print(f"  ✓ {cfg.name}")
    res = pd.DataFrame(rows)
    res.to_csv(os.path.join(out, "summary.csv"), index=False, encoding="utf-8-sig")
    b = {p: bench(data, s, e) for p, (s, e) in periods(first, last, is_end).items()}
    pd.DataFrame(b).to_csv(os.path.join(out, "benchmarks.csv"), encoding="utf-8-sig")
    cols = ["exp", "period", "engine", "trades", "win%", "EV_gross%", "EV_net%", "EV_net_90CI",
            "avg_days", "CAGR%", "maxDD%", "exposure%", "pnl$"]
    print(res[res.engine == "ALL"][[c for c in cols if c in res]].round(3).to_string(index=False))
    print(res[res.engine != "ALL"][["exp", "period", "engine", "trades", "win%", "EV_net%"]].round(3).to_string(index=False))
    print("\n基準 CAGR%:", {p: {k: round(v, 1) for k, v in x.items()} for p, x in b.items()})


def run_sens(sig, first, last, is_end, out):
    """U-9:每個鎖死參數 ±20%,一次只郁一個。標準:優勢要喺每個擾動之下都仲喺度。"""
    base = PER_TRADE
    grid = [("base", {})]
    for k, v in [("trend_score_min", R.TREND_SCORE_MIN), ("trail_mult", R.ATR_TRAIL_MULT),
                 ("mr_score_min", R.MR_SCORE_MIN), ("min_r", R.MIN_R),
                 ("mr_atr_mult", R.ATR_STOP_MULT), ("mr_max_hold", R.MR_MAX_HOLD),
                 ("trend_max_hold", R.TREND_MAX_HOLD)]:
        for f in (0.8, 1.2):
            nv = v * f
            if isinstance(v, int):
                nv = int(round(nv))
            grid.append((f"{k}×{f}", {k: nv}))
    rows = []
    for name, kw in grid:
        cfg = replace(base, name=name, **kw)
        for per, (s, e) in periods(first, last, is_end).items():
            tr, _, _ = simulate(sig, cfg, s, e)
            for eng in ("E1", "E2"):
                sub = tr[tr["engine"] == eng] if len(tr) else tr
                done = sub[sub["reason"] != "數據結束"] if len(sub) else sub
                rows.append({"param": name, "period": per, "engine": eng, "n": len(done),
                             "EV_net%": done["net_pct"].mean() if len(done) else np.nan})
        print(f"  ✓ {name}")
    res = pd.DataFrame(rows)
    res.to_csv(os.path.join(out, "sensitivity.csv"), index=False, encoding="utf-8-sig")
    piv = res.pivot_table(index="param", columns=["engine", "period"], values="EV_net%")
    print(piv.round(3).to_string())


def run_caps(sig, first, last, is_end, out):
    """量度:名義上限 × 同時持倉數 嘅取捨。★ 呢個係風控參數,唔係訊號參數 —— 改唔改由 Owner + CRO 決定。"""
    orig = R.MAX_POSITION_PCT
    rows = []
    try:
        for cap in (10, 15, 20, 30, 1e9):
            for slots in (2, 3):
                R.MAX_POSITION_PCT = cap
                cfg = replace(AS_TRADED, name=f"cap{int(cap) if cap < 1e6 else 'none'}_slots{slots}",
                              max_positions=slots)
                for per, (s, e) in periods(first, last, is_end).items():
                    tr, eq, rej = simulate(sig, cfg, s, e)
                    r = summarize(tr, eq)
                    rows.append({"cfg": cfg.name, "per": per, "trades": r["trades"], "EV_net%": r.get("EV_net%"),
                                 "CAGR%": r.get("CAGR%"), "maxDD%": r.get("maxDD%"), "pnl$": r.get("pnl$"),
                                 "rej_0_shares": rej["notional_or_risk_0_shares"]})
    finally:
        R.MAX_POSITION_PCT = orig
    res = pd.DataFrame(rows)
    res.to_csv(os.path.join(out, "caps.csv"), index=False, encoding="utf-8-sig")
    print(res.pivot_table(index="cfg", columns="per", values=["CAGR%", "maxDD%", "EV_net%", "trades"]).round(2).to_string())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["csv", "yf"], default="csv")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    ap.add_argument("--is_end", default="2024-12-31")
    ap.add_argument("--mode", choices=["ab", "sens", "caps"], default="ab")
    ap.add_argument("--out", default=os.path.join(HERE, "results"))
    a = ap.parse_args()
    pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)

    print(f"{VERSION}  |  規則 = V6.4.2 真代碼  |  數據來源 = {a.source}")
    tickers = R.TICKERS + ["SPY"]
    data = load_csv(a.data, tickers) if a.source == "csv" else load_yf(tickers)
    missing = [t for t in tickers if t not in data]
    if missing:
        print(f"★ 缺數據 {missing} —— 結果唔完整,唔好用嚟做決定")
    sig, bull = precompute(data)
    first = bull[bull].index[0]
    last = data["SPY"].index[-1]
    is_end = pd.Timestamp(a.is_end)
    print(f"可交易期: {first.date()} → {last.date()}(SPY MA200 有效之後)  樣本內至 {is_end.date()}")
    os.makedirs(a.out, exist_ok=True)
    if a.mode == "ab":
        run_ab(sig, data, first, last, is_end, a.out)
    elif a.mode == "sens":
        run_sens(sig, first, last, is_end, a.out)
    else:
        run_caps(sig, first, last, is_end, a.out)


if __name__ == "__main__":
    main()
