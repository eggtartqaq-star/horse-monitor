# -*- coding: utf-8 -*-
"""
V6.6 香港實際執行測試(2026-11-28)—— 研究工具,唔係規則指紋嘅一部分,唔改 lab.py
================================================================================
問題(CRO V6.6.9 留畀 Tom:「第一次前向檢討之前做」):回測假設你任何時間都郁到手 ——
  · 引擎一止盈:盤中一掂到止盈價就以止盈價成交;
  · 引擎一第 10 日 / 引擎二第 60 日:以當日收市價出。
但你喺香港:美股交易時間你瞓緊覺;而且 CRO F-8 規定券商淨係留一張止蝕單,冇 OCO 就唔可以再掛止盈賣單。
所以你實際做到嘅係:
  · 引擎一止盈:朝早睇到「昨晚掂咗止盈」→ 當晚開市先賣(次日開市價);
  · 到期出場:收市後先知 → 次日開市賣。
止蝕唔變:券商止蝕單(C-9)任何時間都有效。

做法:用 inspect 攞 lab.simulate 嘅原碼,做幾處逐字檢查過嘅修改,喺記憶體入面整一個 simulate_hk。
  守門:兩個選項都關嗰陣,simulate_hk 一定要同 lab.simulate 交易指紋(lab.trade_hash)完全一樣,否則停。

版本:
  Lab   = 回測原樣(止盈盤中成交、到期收市出)
  HK-1  = 到期改次日開市出;止盈照盤中(等於券商有 OCO,可以同時掛止蝕同止盈)
  HK-2  = HK-1 + 止盈要次日開市先賣(冇 OCO;F-8)—— 呢個先係你而家實際做到嘅
設定同穩健度測試一樣(robustness_v66.live_cfg:資金 HK$12,500、基數 HK$10,000、每邊最低 US$0.35 + 10bp(估算)、
  實盤入場、開市單、留 30% 現金、其餘 T-bill)。

用法:python hk_exec_v66.py [--out results/hk_exec]
"""
import argparse
import inspect
import os
import sys
import textwrap

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
import income_study as IS        # noqa: E402
import robustness_v66 as RB      # noqa: E402

PATCHES = [
    # (原文, 新文) —— 每段原文喺 lab.simulate 入面一定要啱啱出現一次
    ("    busy_until = {}",
     "    busy_until = {}\n    hk_pending = {}                     # HK:id(倉) → 次日開市出場嘅原因"),
    ("    def close_trade(p, d, px, reason):\n        nonlocal realized, month_pnl",
     "    def close_trade(p, d, px, reason):\n        nonlocal realized, month_pnl\n        hk_pending.pop(id(p), None)"),
    ("        o, h, l, c = row[\"Open\"], row[\"High\"], row[\"Low\"], row[\"Close\"]",
     "        o, h, l, c = row[\"Open\"], row[\"High\"], row[\"Low\"], row[\"Close\"]\n"
     "        if id(p) in hk_pending:                       # HK:昨晚已經決定出場 → 今日開市賣\n"
     "            close_trade(p, d, o, hk_pending[id(p)]); return True"),
    ("            if h >= p.target:\n                close_trade(p, d, p.target, \"止盈\"); return True",
     "            if h >= p.target:\n"
     "                if HK_TARGET:\n"
     "                    hk_pending[id(p)] = \"止盈→次日開市\"; return False\n"
     "                close_trade(p, d, p.target, \"止盈\"); return True"),
    ("                close_trade(p, d, c, \"滿10日\"); return True",
     "                if HK_TIME:\n"
     "                    hk_pending[id(p)] = \"滿10日→次日開市\"; return False\n"
     "                close_trade(p, d, c, \"滿10日\"); return True"),
    ("            close_trade(p, d, c, \"滿60日\"); return True",
     "            if HK_TIME:\n"
     "                hk_pending[id(p)] = \"滿60日→次日開市\"; return False\n"
     "            close_trade(p, d, c, \"滿60日\"); return True"),
]


def make_simulate(hk_target, hk_time):
    src = textwrap.dedent(inspect.getsource(lab.simulate))
    for old, new in PATCHES:
        n = src.count(old)
        if n != 1:
            print(f"★ lab.simulate 改咗,修改位出現 {n} 次(應該 1 次):{old.strip()[:60]!r}。停。")
            sys.exit(1)
        src = src.replace(old, new)
    ns = dict(vars(lab))
    ns.update(HK_TARGET=hk_target, HK_TIME=hk_time)
    exec(compile(src, "<simulate_hk>", "exec"), ns)
    return ns["simulate"]


def run(sim, sig, cfg, tb, first, last):
    tr, eq, rej = sim(sig, lab.replace(cfg, cash_yield=tb), first, last)
    return tr, eq["equity"], rej


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "results", "hk_exec"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    data, sig, first, last, tb, _ = IS.load()
    cfg = RB.live_cfg()
    print(f"期間 {first.date()} → {last.date()}  |  設定 = 穩健度測試實盤設定(收費 {RB.FEE},估算)")

    # 守門:兩個選項都關 → 一定同 lab.simulate 一模一樣
    sim0 = make_simulate(False, False)
    for name, c in (("AS_TRADED", lab.AS_TRADED), ("live", cfg)):
        t_ref, _, _ = lab.simulate(sig, lab.replace(c, cash_yield=tb if name == "live" else None), first, last)
        t_new, _, _ = sim0(sig, lab.replace(c, cash_yield=tb if name == "live" else None), first, last)
        h_ref, h_new = lab.trade_hash(t_ref), lab.trade_hash(t_new)
        print(f"守門 {name}:lab {h_ref} / 複製 {h_new} → {'一樣 ✅' if h_ref == h_new else '唔一樣 ❌'}")
        if h_ref != h_new:
            sys.exit(1)

    variants = [("Lab(回測原樣)", False, False), ("HK-1(到期次日開市;止盈照盤中=有OCO)", False, True),
                ("HK-2(到期同止盈都次日開市;冇OCO,你而家嘅做法)", True, True)]
    rows, trades = [], {}
    for name, ht, hm in variants:
        tr, e, rej = run(make_simulate(ht, hm), sig, cfg, tb, first, last)
        done = tr[tr["reason"] != "數據結束"]
        xa, st, sb = RB.excess_cagr(e, tb, first, last)
        xo, _, _ = RB.excess_cagr(e, tb, IS.OOS_START, last)
        s = lab.summarize(tr, None)
        rows.append({"版本": name, "全期CAGR%": round(st["CAGR%"], 2), "T-bill CAGR%": round(sb["CAGR%"], 2),
                     "全期超額%/年": round(xa, 2), "2025起超額%/年": round(xo, 2), "完成交易": len(done),
                     "每筆淨EV%": round(float(s.get("EV_net%", np.nan)), 3),
                     "引擎一US$": round(done[done.engine == "E1"]["pnl_usd"].sum(), 1),
                     "引擎二US$": round(done[done.engine == "E2"]["pnl_usd"].sum(), 1),
                     "交易合計US$": round(done["pnl_usd"].sum(), 1), "最大回撤%": round(st["maxDD%"], 2),
                     "交易指紋": lab.trade_hash(tr)})
        trades[name] = tr
        tr.to_csv(os.path.join(a.out, f"trades_{['lab', 'hk1', 'hk2'][len(trades) - 1]}.csv"), index=False,
                  encoding="utf-8-sig")
    res = pd.DataFrame(rows)
    res.to_csv(os.path.join(a.out, "summary.csv"), index=False, encoding="utf-8-sig")
    print("\n" + res.drop(columns=["交易指紋"]).to_string(index=False))

    # 同一筆交易(同股、同入場日)喺 Lab 同 HK-2 嘅出場價比較
    lab_t, hk_t = trades[variants[0][0]], trades[variants[2][0]]
    k = ["ticker", "entry_date"]
    m = hk_t.merge(lab_t, on=k, suffixes=("_hk", "_lab"))
    m = m[m["reason_hk"].str.contains("→次日開市", na=False)]
    m["出場價差%"] = (m["exit_hk"] / m["exit_lab"] - 1) * 100
    m["盈虧差US$"] = m["pnl_usd_hk"] - m["pnl_usd_lab"]
    by = m.groupby("reason_hk").agg(筆數=("出場價差%", "size"), 平均價差pct=("出場價差%", "mean"),
                                    中位數pct=("出場價差%", "median"), 較差筆數=("出場價差%", lambda x: int((x < 0).sum())),
                                    盈虧差合計US=("盈虧差US$", "sum")).round(3)
    by.to_csv(os.path.join(a.out, "next_open_vs_lab.csv"), encoding="utf-8-sig")
    print("\n同一筆交易:HK-2 次日開市出場 vs Lab 原本出場價(只計兩邊都有嘅交易)\n" + by.to_string())
    print(f"\n已寫入 {a.out}")


if __name__ == "__main__":
    main()
