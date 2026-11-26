# -*- coding: utf-8 -*-
"""
V6.6 收入研究(2026-11-26)—— Owner 問:「贏唔到大市都唔緊要,長期跑當額外收入,得唔得?」
==========================================================================================
比較標準唔係大市,係「同一筆錢全部放 T-bill」(差唔多冇風險):
系統 + 閒置現金收息,一年多過(或者少過)淨係放 T-bill 幾多港幣?幾大機會輸畀 T-bill?

用法:python income_study.py
  要 data/ 入面嘅股票 CSV(同 lab.py 一樣),同埋 data/BIL.csv(見下)。研究工具,唔係規則指紋嘅一部分。

T-bill 數據(CLAUDE.md 第 5 條:來源、日期、修正都要寫清楚):
  - data/BIL.csv = BIL(SPDR Bloomberg 1–3 Month T-Bill ETF)日線,Webull 唯讀 API(2026-11-26 拉),
    2022-02-15 → 2026-11-25,「調整後」價。
  - Webull 有 4 日冇調整派息:單日跌 0.34%–0.40%(2024-10-01、11-01、12-02、12-19),T-bill ETF 正常日回報
    唔會咁跌。build_tbill() 將「單日回報低過當月中位數 0.15 個百分點以上」嘅日子(Tom F-6)換做「同月其他日子嘅日回報中位數」,
    寫入 data/TBILL.csv。修正後年回報:2023 4.94%、2024 5.16%、2025 4.15%(衍生數據,估算)。
  - 預扣稅情境:香港居民持有美國 T-bill ETF,派息可能被預扣 30%(券商有冇用「合資格利息收入」豁免,未核實)。
    呢個係情境,唔係事實:日回報 × 0.7。

輸出:results/income_scenarios.csv、income_decomposition.csv、income_yearly.csv、income_bootstrap.csv
"""
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
import lab                    # noqa: E402
import rules_v642 as R        # noqa: E402

FX = R.USD_HKD
OOS_START = pd.Timestamp("2025-01-01")
WHT = 0.30                                    # 預扣稅情境(未核實)
SIZES = [(12_500, 10_000), (25_000, 20_000), (50_000, 40_000), (100_000, 80_000)]   # (資金, 倉位基數) = CRO C-7 嘅比例
FEES = ("webull0", "real35", "min1")
lab.BROKERS["real35"] = lab.Broker("每邊最低US$0.35 + 10bp(CRO N-9 估算情境)", 0.35, 0.0, 10.0)
BAD_GAP = 0.0015                             # Tom F-6:低過當月中位數 0.15pp = 派息冇調整(利率低都捉到)
RESERVE = 30.0                               # CRO R-1(2026-11-26):已交收現金 ≥ account_hkd 嘅 30%


def build_tbill(bil_csv, out_csv=None):
    """BIL 調整後收市 → 修正 Webull 漏咗調整嘅派息日 → T-bill 指數。回傳 (指數, 修正咗嘅日子)。"""
    b = pd.read_csv(bil_csv, index_col=0, parse_dates=True)["Close"].sort_index()
    r = b.pct_change()
    med = r.groupby([r.index.year, r.index.month]).transform("median")
    bad = list(r[r < med - BAD_GAP].index)
    for d in bad:
        same_month = r[(r.index.year == d.year) & (r.index.month == d.month)].drop(d)
        r[d] = same_month.drop([x for x in bad if x in same_month.index]).median()
    idx = b.iloc[0] * (1 + r.fillna(0.0)).cumprod()
    if out_csv:
        idx.to_frame("Close").to_csv(out_csv)
    return idx, bad


def haircut(index, keep):
    """日回報 × keep(預扣稅情境)。"""
    r = index.pct_change().fillna(0.0) * keep
    return index.iloc[0] * (1 + r).cumprod()


def window(s, a, b):
    return s[(s.index >= a) & (s.index <= b)]


def stats(eq, a, b, cap_usd):
    e = window(eq, a, b)
    yrs = (e.index[-1] - e.index[0]).days / 365.25
    g = e.iloc[-1] / e.iloc[0]
    m = e.resample("ME").last()
    m = pd.concat([e.iloc[:1], m]).pct_change().dropna()
    return {"CAGR%": (g ** (1 / yrs) - 1) * 100,
            "HKD_per_yr": (e.iloc[-1] - e.iloc[0]) * FX / yrs * (cap_usd / e.iloc[0]),   # 按期初資金換算
            "maxDD%": (e / e.cummax() - 1).min() * 100,
            "worst_month%": m.min() * 100, "pos_months%": (m > 0).mean() * 100, "years": yrs}


def bench_equity(series, a, b, cap_usd):
    s = window(series, a, b)
    return s / s.iloc[0] * cap_usd


def monthly_excess(sys_eq, bm_eq):
    a = sys_eq.resample("ME").last()
    b = bm_eq.resample("ME").last()
    a = pd.concat([sys_eq.iloc[:1], a]).pct_change().dropna()
    b = pd.concat([bm_eq.iloc[:1], b]).pct_change().dropna()
    return (a - b).dropna()


def boot(x, horizons=(12, 36, 60), n=5000, block=3, seed=11):
    """每月超額回報,circular block bootstrap(3 個月一組,頭尾接駁,Tom F-1)→ 1/3/5 年累積超額 < 0 嘅機會。
    「+均值不確定」:每條路徑再加一個 N(0, sd/√n) 嘅均值偏移(真正平均數本身都唔知)。"""
    x = np.asarray(x)
    rng = np.random.default_rng(seed)
    out = {}
    for h in horizons:
        nb = int(np.ceil(h / block))
        xx = np.concatenate([x, x[:block - 1]])
        st = rng.integers(0, len(x), (n, nb))
        paths = np.stack([np.concatenate([xx[s:s + block] for s in row])[:h] for row in st])
        shift = rng.normal(0.0, x.std(ddof=1) / np.sqrt(len(x)), (n, 1))
        cum = (np.prod(1 + paths, axis=1) - 1) * 100
        cum2 = (np.prod(1 + paths + shift, axis=1) - 1) * 100
        out[f"{h}個月"] = {"P(輸畀T-bill)%": (cum < 0).mean() * 100,
                         "P(輸)%+均值不確定": (cum2 < 0).mean() * 100,
                         "P10%": np.percentile(cum2, 10), "P50%": np.percentile(cum2, 50),
                         "P90%": np.percentile(cum2, 90)}
    return out


def load():
    data = lab.load_csv(os.path.join(HERE, "data"), R.TICKERS + ["SPY"])
    tb, bad = build_tbill(os.path.join(HERE, "data", "BIL.csv"), os.path.join(HERE, "data", "TBILL.csv"))
    sig, bull = lab.precompute(data)
    first = bull[bull].index[0]
    last = data["SPY"].index[-1]
    return data, sig, first, last, tb, bad


def run():
    data, sig, first, last, tb, bad = load()
    tbw = haircut(tb, 1 - WHT)
    spy = data["SPY"]["Close"]
    print(f"期間 {first.date()} → {last.date()}(SPY MA200 有效之後);樣本外由 {OOS_START.date()} 起")
    print(f"T-bill 修正咗 {len(bad)} 日:{', '.join(str(d.date()) for d in bad)}")
    periods = (("全期", first, last), ("樣本外", OOS_START, last))
    rows, decomp, keep = [], [], {}

    def bench_rows(cap_hkd):
        cap = cap_hkd / FX
        for nm, s in (("純T-bill", tb), (f"純T-bill(預扣{int(WHT * 100)}%情境)", tbw), ("SPY買入持有", spy)):
            for per, a, b in periods:
                st = stats(bench_equity(s, a, b, cap), a, b, cap)
                rows.append({"情境": f"基準|{cap_hkd / 1000:g}k|{nm}", "期間": per, "資金HKD": cap_hkd,
                             **{k: round(v, 2) for k, v in st.items()}})

    def one(label, cfg, cap_hkd, bm, base_cfg=None):
        """bm = 用嚟比較嘅 T-bill(同一個稅務假設)。base_cfg = 同一設定但唔收息(用嚟拆開「交易」同「利息」)。"""
        cap = cap_hkd / FX
        tr, eq, rej = lab.simulate(sig, cfg, first, last)
        e = eq["equity"]
        e0 = lab.simulate(sig, base_cfg, first, last)[1]["equity"] if base_cfg is not None else None
        for per, a, b in periods:
            st = stats(e, a, b, cap)
            bq = bench_equity(bm, a, b, cap)
            st_b = stats(bq, a, b, cap)
            done = tr[(tr["reason"] != "數據結束") & (pd.to_datetime(tr["entry_date"]) >= a)] if len(tr) else tr
            ew = window(e, a, b)
            rows.append({"情境": label, "期間": per, "資金HKD": cap_hkd, **{k: round(v, 2) for k, v in st.items()},
                         "T-bill_CAGR%": round(st_b["CAGR%"], 2),
                         "超額%/年": round(st["CAGR%"] - st_b["CAGR%"], 2),
                         "超額HKD/年": round(st["HKD_per_yr"] - st_b["HKD_per_yr"], 0),
                         "交易": len(done), "持倉日%": round((window(eq["n_pos"], a, b) > 0).mean() * 100, 1),
                         # Tom F-5:拒絕次數只係全期數(樣本外唔另計)
                         "限價冇成交(全期)": rej.get("limit", 0) if per == "全期" else None,
                         "開市低過止蝕(全期)": rej.get("floor", 0) if per == "全期" else None})
            if e0 is not None:
                w0 = window(e0, a, b)
                yrs = st["years"]
                trade = (w0.iloc[-1] - w0.iloc[0]) * FX / yrs
                interest = ((ew.iloc[-1] - ew.iloc[0]) - (w0.iloc[-1] - w0.iloc[0])) * FX / yrs
                bq0 = bench_equity(bm, a, b, ew.iloc[0])        # 「期初戶口全部放 T-bill」(實際港幣,唔換算)
                alt = (bq0.iloc[-1] - bq0.iloc[0]) * FX / yrs
                decomp.append({"情境": label, "期間": per, "資金HKD": cap_hkd,
                               "交易盈虧HKD/年": round(trade, 0), "現金利息HKD/年": round(interest, 0),
                               "合計HKD/年": round(trade + interest, 0), "全部放T-bill HKD/年": round(alt, 0),
                               "少收咗嘅利息HKD/年": round(alt - interest, 0),
                               "超額HKD/年": round(trade + interest - alt, 0)})
        return tr, eq

    def cfg_of(fee, cap, base, cy, res, rule="limit", slots=None, tif="open"):
        c = replace(lab.AS_TRADED, name="x", broker=fee, entry_rule=rule, account_hkd=base, capital_hkd=cap,
                    cash_yield=cy, cash_reserve_pct=res, entry_tif=tif)
        return replace(c, max_positions=slots) if slots else c

    # 基準
    for cap, _ in SIZES:
        bench_rows(cap)

    # A) 12,500 資金、10,000 基數(CRO C-7 (A)),實盤入場。
    #    限價單有效期(Tom F-3,CRO 定):開市單 = 開市冇成交即取消(C-8 字面);全日單 = 盤中跌到限價都成交
    res_lbl = f"留{RESERVE:g}%現金(CRO R-1)、其餘T-bill"
    for tif, tl in (("open", "開市單"), ("day", "全日單")):
        for fee in FEES:
            nocash = cfg_of(fee, 12_500, 10_000, None, 0.0, tif=tif)
            one(f"A|12.5k|{fee}|{tl}|現金唔收息", nocash, 12_500, tb)
            one(f"A|12.5k|{fee}|{tl}|{res_lbl}", cfg_of(fee, 12_500, 10_000, tb, RESERVE, tif=tif), 12_500, tb, nocash)
            if tif == "open":
                one(f"A|12.5k|{fee}|{tl}|閒置現金全部T-bill(上限)", cfg_of(fee, 12_500, 10_000, tb, 0.0), 12_500, tb,
                    nocash)
                one(f"A|12.5k|{fee}|{tl}|留{RESERVE:g}%、T-bill預扣30%", cfg_of(fee, 12_500, 10_000, tbw, RESERVE),
                    12_500, tbw, nocash)
    # A0) 對照:舊回測入場規則(手冊 1% 重計),冇收息
    one("A0|12.5k|webull0|舊入場規則|現金唔收息", cfg_of("webull0", 12_500, 10_000, None, 0.0, rule="deviation"),
        12_500, tb)

    # B) 資金規模(實盤入場、CRO 30% 已交收現金、其餘 T-bill)
    for cap, base in SIZES:
        for tif, tl in (("open", "開市單"), ("day", "全日單")):
            for fee in ("webull0", "real35"):
                tr, eq = one(f"B|{cap / 1000:g}k|{fee}|{tl}|{res_lbl}", cfg_of(fee, cap, base, tb, RESERVE, tif=tif),
                             cap, tb, cfg_of(fee, cap, base, None, 0.0, tif=tif))
                keep[(cap, fee, tif)] = eq["equity"]

    # C) 研究(未批准):大戶口多倉位(MAX_POSITIONS 係鎖死參數,只係假設)。留底 = 倉數 × 10% + 10% 緩衝(同 R-1 一樣道理)
    for slots in (3, 4):
        one(f"C(研究,未批准)|100k|real35|開市單|{slots}倉", cfg_of("real35", 100_000, 80_000, tb, 10.0 * (slots + 1), slots=slots),
            100_000, tb, cfg_of("real35", 100_000, 80_000, None, 0.0, slots=slots))

    out = os.path.join(HERE, "results")
    df = pd.DataFrame(rows)
    dd = pd.DataFrame(decomp)
    df.to_csv(os.path.join(out, "income_scenarios.csv"), index=False, encoding="utf-8-sig")
    dd.to_csv(os.path.join(out, "income_decomposition.csv"), index=False, encoding="utf-8-sig")

    # 年度表 + bootstrap
    ys, bs = [], {}
    for key in ((12_500, "real35", "open"), (12_500, "webull0", "open"), (12_500, "real35", "day"),
                (12_500, "webull0", "day"), (100_000, "real35", "open")):
        cap, fee, tif = key
        lbl = f"{cap / 1000:g}k|{fee}|{'開市單' if tif == 'open' else '全日單'}|留{RESERVE:g}%"
        e = keep[key]
        tbq, spq = bench_equity(tb, first, last, cap / FX), bench_equity(spy, first, last, cap / FX)
        yr = pd.DataFrame({"系統+T-bill": e, "純T-bill": tbq, "SPY": spq})
        ye = pd.concat([yr.iloc[:1], yr.resample("YE").last()])
        yret = (ye.pct_change().dropna() * 100).round(2)
        yret["超額 vs T-bill"] = (yret["系統+T-bill"] - yret["純T-bill"]).round(2)
        yret.index = [f"{d.year}" + ("(由 " + str(first.date()) + ")" if d.year == first.year else "")
                      + ("(至 " + str(last.date()) + ")" if d.year == last.year else "") for d in yret.index]
        yret.insert(0, "情境", lbl)
        ys.append(yret)
        x = monthly_excess(e, tbq)
        for h, v in boot(x.values).items():
            bs[(lbl, h)] = {**{k: round(w, 2) for k, w in v.items()},
                            "月均超額%": round(x.mean() * 100, 3), "月超額標準差%": round(x.std() * 100, 3),
                            "t值": round(x.mean() / (x.std(ddof=1) / np.sqrt(len(x))), 2), "月數": len(x)}
    yall = pd.concat(ys)
    yall.to_csv(os.path.join(out, "income_yearly.csv"), encoding="utf-8-sig")
    bsd = pd.DataFrame(bs).T
    bsd.index.names = ["情境", "年期"]
    bsd.to_csv(os.path.join(out, "income_bootstrap.csv"), encoding="utf-8-sig")

    pd.set_option("display.width", 260); pd.set_option("display.max_columns", 30); pd.set_option("display.max_rows", 200)
    cols = ["情境", "期間", "CAGR%", "T-bill_CAGR%", "超額%/年", "HKD_per_yr", "超額HKD/年", "maxDD%", "worst_month%",
            "pos_months%", "交易", "持倉日%", "限價冇成交(全期)", "開市低過止蝕(全期)"]
    print(df.reindex(columns=cols).to_string(index=False))
    print("\n拆開:交易盈虧 vs 現金利息 vs 全部放 T-bill(HKD/年)")
    print(dd.to_string(index=False))
    print("\n年度回報 %:")
    print(yall.to_string())
    print("\nCircular block bootstrap(3 個月一組,5,000 次;Tom F-1)—— 累積超額 vs 純 T-bill:")
    print(bsd.to_string())
    return df, dd, yall, bsd


if __name__ == "__main__":
    run()
