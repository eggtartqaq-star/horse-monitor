# -*- coding: utf-8 -*-
"""
V6.6 穩健度測試(2026-11-27)—— 研究工具,唔係規則指紋嘅一部分,唔改任何規則
================================================================================
Owner 問(2026-11-27):有冇嘢而家可以做,升級或者測試個系統?揀咗「誠實嘅穩健度測試」。

問題:收入研究(reports/quant/2026-11-26-v66-income-study.md)話「可以做細額附加,收入係 T-bill 利息」。
呢個結論喺下面幾種壓力之下仲企唔企得住?
  A. 逐年:2023、2024、2025、2026 年初至今,每年分開睇(唔係全期平均)。
  B. 滾動 6 個月窗(每月起步一次):幾多個窗贏 T-bill?(規則鎖死,冇重新擬合 —— 純粹睇穩定度)
  C. 參數 ±20%(一次郁一個,用實盤設定、組合層面):超額回報會唔會轉負?
  D. 「事後贏家」測試(生存者偏差嘅代理):38 隻股係 2026 年揀嘅(Tom F-01)。
     將全期升得最多嘅 5 隻 / 10 隻剔走再跑。呢個係偏嚴嘅上下限,唔係偏差嘅估算;
     真正嘅測試要用 2022 年初已經固定嘅名單(S&P 100,2022-01),等網絡開咗再做。

設定(同收入研究 A 情境一樣):資金 HK$12,500、倉位基數 HK$10,000、每邊最低 US$0.35 + 10bp(CRO 估算,未核實)、
  實盤入場(限價 ≤ 限價上限、開市 ≤ 止蝕唔買)、開市單(冇成交即取消)、留 30% 已交收現金、其餘閒置現金收 T-bill。
數據:data/*.csv(Webull 唯讀,2022-02 → 2026-11-23);T-bill = data/TBILL.csv(由 BIL 修正,見 income_study.py)。

用法:python robustness_v66.py [--out results/robustness]
"""
import argparse
import os
import sys
from dataclasses import replace

import numpy as np
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lab                       # noqa: E402
import rules_v642 as R           # noqa: E402
import income_study as IS        # noqa: E402

CAP_HKD, BASE_HKD, FEE, RESERVE = 12_500, 10_000, "real35", IS.RESERVE
FX = IS.FX


def live_cfg(**kw):
    c = replace(lab.AS_TRADED, name="live", broker=FEE, entry_rule="limit", account_hkd=BASE_HKD,
                capital_hkd=CAP_HKD, cash_reserve_pct=RESERVE, entry_tif="open")
    return replace(c, **kw)


def run_one(sig, cfg, tb, first, last):
    tr, eq, rej = lab.simulate(sig, replace(cfg, cash_yield=tb), first, last)
    return tr, eq["equity"]


def anchored(e, a, b, floor):
    """Tom 2026-11-27 R-1:窗口回報要由「窗口開始之前最後一個收市」計起,唔係由窗口第一日收市 ——
    否則每個窗口都漏咗第一個交易日嘅回報(例:2024-01-02 系統 −0.51%,2024 年超額由 −0.57% 變咗 −0.02%)。
    floor = 期間第一日:窗口由 floor 開始就由 floor 收市計(系統同 T-bill 用同一個起點)。"""
    w = IS.window(e, a, b)
    pre = e[(e.index < a) & (e.index >= floor)]
    return pd.concat([pre.iloc[-1:], w]) if len(pre) else w


def ret(e, a, b, floor):
    w = anchored(e, a, b, floor)
    return (w.iloc[-1] / w.iloc[0] - 1) * 100 if len(w) > 1 else np.nan


def excess_cagr(e, tb, a, b):
    cap = CAP_HKD / FX
    st = IS.stats(e, a, b, cap)
    sb = IS.stats(IS.bench_equity(tb, a, b, cap), a, b, cap)
    return st["CAGR%"] - sb["CAGR%"], st, sb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "results", "robustness"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    data, sig, first, last, tb, _ = IS.load()
    spy = data["SPY"]["Close"]
    print(f"期間 {first.date()} → {last.date()}  |  設定:資金 HK${CAP_HKD:,}、基數 HK${BASE_HKD:,}、收費 {FEE}、開市單、"
          f"留 {RESERVE:g}% 現金、閒置收 T-bill")

    tr0, e0 = run_one(sig, live_cfg(), tb, first, last)
    done0 = tr0[tr0["reason"] != "數據結束"]
    x_all, st_all, sb_all = excess_cagr(e0, tb, first, last)
    x_oos, _, _ = excess_cagr(e0, tb, IS.OOS_START, last)
    print(f"\n基準(全期):系統 CAGR {st_all['CAGR%']:.2f}%,T-bill {sb_all['CAGR%']:.2f}%,超額 {x_all:+.2f}%/年;"
          f"樣本外(2025-01-01 起)超額 {x_oos:+.2f}%/年;交易 {len(done0)}")

    # Tom 2026-11-27 R-3:冇交易嘅同一個戶口(留 30% 現金、其餘 T-bill)—— 將「留底現金唔收息」同「交易」拆開
    _, en = run_one(sig, live_cfg(engines=()), tb, first, last)
    xn_all, _, _ = excess_cagr(en, tb, first, last)
    xn_oos, _, _ = excess_cagr(en, tb, IS.OOS_START, last)
    open_end = tr0[tr0["reason"] == "數據結束"]
    print(f"   拆開:冇交易(只係留底現金唔收息)超額 {xn_all:+.2f}%/年(樣本外 {xn_oos:+.2f}%);"
          f"交易本身 {x_all - xn_all:+.2f}%/年(樣本外 {x_oos - xn_oos:+.2f}%)")
    print(f"   已完成交易盈虧:引擎一 US${done0[done0['engine'] == 'E1']['pnl_usd'].sum():+.1f}、"
          f"引擎二 US${done0[done0['engine'] == 'E2']['pnl_usd'].sum():+.1f};"
          f"期末未平倉 {len(open_end)} 筆按市值 US${open_end['pnl_usd'].sum():+.1f}")
    dd = e0 / e0.cummax() - 1
    trough = dd.idxmin()
    peak = e0[:trough].idxmax()
    rec = e0[trough:][e0[trough:] >= e0[peak]]
    rel = e0 / IS.bench_equity(tb, first, last, CAP_HKD / FX)
    rdd = rel / rel.cummax() - 1
    print(f"   全期最大回撤 {dd.min() * 100:.2f}%(高位 {peak.date()} → 低位 {trough.date()} → "
          f"{'收復 ' + str(rec.index[0].date()) if len(rec) else '未收復'});"
          f"相對 T-bill 最大回撤 {rdd.min() * 100:.2f}%({rdd.idxmin().date()}),"
          f"戶口高過 T-bill 線嘅日子 {(rel.iloc[1:] > 1).mean() * 100:.1f}%")

    # A. 逐年(Tom R-1:由上一年最後一個收市計起;2022 係 11-30 起嘅零碎月份,都列出,令交易數加埋 = 全期)
    rows = []
    for y in sorted(set(e0.index.year)):
        a_, b_ = max(pd.Timestamp(f"{y}-01-01"), first), min(pd.Timestamp(f"{y}-12-31"), last)
        t = tr0[(pd.to_datetime(tr0["entry_date"]) >= a_) & (pd.to_datetime(tr0["entry_date"]) <= b_)]
        t = t[t["reason"] != "數據結束"]
        w = anchored(e0, a_, b_, first)
        rows.append({"年": y, "由": str(a_.date()), "至": str(b_.date()), "系統%": round(ret(e0, a_, b_, first), 2),
                     "T-bill%": round(ret(tb, a_, b_, first), 2),
                     "超額%": round(ret(e0, a_, b_, first) - ret(tb, a_, b_, first), 2),
                     "冇交易戶口%": round(ret(en, a_, b_, first), 2),
                     "交易貢獻%": round(ret(e0, a_, b_, first) - ret(en, a_, b_, first), 2),
                     "SPY%": round(ret(spy, a_, b_, first), 2), "交易": len(t),
                     "年內最大回撤%": round((w / w.cummax() - 1).min() * 100, 2)})
    yr = pd.DataFrame(rows)
    yr.to_csv(os.path.join(a.out, "yearly.csv"), index=False, encoding="utf-8-sig")
    print("\nA. 逐年(系統 vs T-bill,同一個戶口)\n" + yr.to_string(index=False))

    # B. 滾動 6 個月窗(每月月初起步)
    starts = pd.date_range(first.normalize() + pd.offsets.MonthBegin(1), last - pd.DateOffset(months=6), freq="MS")
    wf = []
    for s in starts:
        e_ = s + pd.DateOffset(months=6) - pd.Timedelta(days=1)
        wf.append({"由": str(s.date()), "至": str(e_.date()),
                   "超額%": ret(e0, s, e_, first) - ret(tb, s, e_, first)})
    wf = pd.DataFrame(wf)
    wf.to_csv(os.path.join(a.out, "rolling6m.csv"), index=False, encoding="utf-8-sig")
    win = (wf["超額%"] > 0).mean() * 100
    print(f"\nB. 滾動 6 個月窗:{len(wf)} 個,贏 T-bill {win:.0f}%;超額中位數 {wf['超額%'].median():+.2f}%,"
          f"最差 {wf['超額%'].min():+.2f}%,最好 {wf['超額%'].max():+.2f}%(每 6 個月,唔係年化)")
    # Tom R-2:窗口重疊 5 個月 → 獨立窗口只有約 len/6 個;6 個起步相位嘅「唔重疊」贏 T-bill 數
    ph = [f"{int((wf['超額%'].iloc[p::6] > 0).sum())}/{len(wf['超額%'].iloc[p::6])}" for p in range(6)]
    print(f"   唔重疊窗口(6 個起步相位)贏 T-bill:{', '.join(ph)}")

    # C. 參數 ±20%(組合層面,實盤設定)
    grid = [("base", {})]
    for k, v in [("trend_score_min", R.TREND_SCORE_MIN), ("trail_mult", R.ATR_TRAIL_MULT),
                 ("mr_score_min", R.MR_SCORE_MIN), ("min_r", R.MIN_R), ("mr_atr_mult", R.ATR_STOP_MULT),
                 ("mr_max_hold", R.MR_MAX_HOLD), ("trend_max_hold", R.TREND_MAX_HOLD)]:
        for f in (0.8, 1.2):
            nv = int(round(v * f)) if isinstance(v, int) else v * f
            grid.append((f"{k}×{f}", {k: nv}))
    sens = []
    for name, kw in grid:
        tr_, e_ = run_one(sig, live_cfg(**kw), tb, first, last)
        xa, _, _ = excess_cagr(e_, tb, first, last)
        xo, _, _ = excess_cagr(e_, tb, IS.OOS_START, last)
        sens.append({"參數": name, "全期超額%/年": round(xa, 2), "樣本外超額%/年": round(xo, 2),
                     "交易": int((tr_["reason"] != "數據結束").sum())})
    sens = pd.DataFrame(sens)
    sens.to_csv(os.path.join(a.out, "sensitivity_live.csv"), index=False, encoding="utf-8-sig")
    flips = sens[(sens["參數"] != "base") & (np.sign(sens["全期超額%/年"]) != np.sign(x_all))]
    print("\nC. 參數 ±20%(一次郁一個)\n" + sens.to_string(index=False))
    print(f"   全期超額正負號同基準唔同嘅組合:{len(flips)} / {len(sens) - 1}")

    # D. 剔走事後贏家
    tot = {tk: data[tk]["Close"][first:last].iloc[-1] / data[tk]["Close"][first:last].iloc[0] - 1
           for tk in R.TICKERS if tk in data}
    rank = sorted(tot, key=tot.get, reverse=True)
    drows = [{"剔走": "冇(38 隻)", "剔走嘅股": "", "全期超額%/年": round(x_all, 2), "樣本外超額%/年": round(x_oos, 2),
              "交易": len(done0)}]
    for k in (5, 10):
        drop = rank[:k]
        sub = {tk: v for tk, v in data.items() if tk not in drop}
        sig_k, _ = lab.precompute(sub)
        tr_k, e_k = run_one(sig_k, live_cfg(), tb, first, last)
        xa, _, _ = excess_cagr(e_k, tb, first, last)
        xo, _, _ = excess_cagr(e_k, tb, IS.OOS_START, last)
        drows.append({"剔走": f"升得最多 {k} 隻", "剔走嘅股": " ".join(drop), "全期超額%/年": round(xa, 2),
                      "樣本外超額%/年": round(xo, 2), "交易": int((tr_k["reason"] != "數據結束").sum())})
    dw = pd.DataFrame(drows)
    dw.to_csv(os.path.join(a.out, "drop_winners.csv"), index=False, encoding="utf-8-sig")
    print("\nD. 剔走事後贏家(全期升幅排名,"
          f"{first.date()} → {last.date()})\n" + dw.to_string(index=False))
    tw = pd.Series(tot).sort_values(ascending=False).head(10).mul(100).round(0)
    print("   升幅頭 10 名(%):" + ", ".join(f"{k} {v:+.0f}" for k, v in tw.items()))
    # Tom R-8:剔走嘅股入面,邊啲本身就冇交易?(收市訊號日,用訊號價計 position_plan = 0 股 → 掃描器唔會列出)
    cfg0 = live_cfg()
    aff = []
    for tk in rank[:10]:
        df = sig[tk][(sig[tk].index >= first) & (sig[tk].index <= last)]
        n_sig = n_ok = 0
        for d, e in zip(df.index, df["sig"]):
            s = lab.build_signal(e, cfg0)
            if not s:
                continue
            n_sig += 1
            f0 = lab.raw_factor(tk, d)
            n_ok += R.position_plan(df.at[d, "Close"] * f0, s["stop"] * f0, account_hkd=cfg0.account_hkd)[0] > 0
        aff.append(f"{tk} {int((done0['ticker'] == tk).sum())} 筆/買得起 {n_ok} of {n_sig} 訊號日")
    print("   剔走嘅股,基準交易數 / 買得起 1 股嘅訊號日:" + "; ".join(aff))
    print(f"   基準有完成交易嘅股:{done0['ticker'].nunique()} / {len(R.TICKERS)}")

    # 每隻股貢獻(基準)
    if len(done0):
        by = done0.groupby("ticker")["pnl_usd"].sum().sort_values(ascending=False)
        by.to_csv(os.path.join(a.out, "pnl_by_ticker.csv"), encoding="utf-8-sig")
        print(f"\n基準每隻股盈虧(US$,頭 5 / 尾 3):{by.head(5).round(1).to_dict()} / {by.tail(3).round(1).to_dict()}")
        print(f"   全部交易盈虧合計 US${by.sum():.1f}")
    print(f"\n已寫入 {a.out}")


if __name__ == "__main__":
    main()
