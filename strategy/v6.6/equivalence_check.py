# -*- coding: utf-8 -*-
"""
等價測試:signals_v66(掃描器/bot 用)vs lab.build_signal(回測用)
=================================================================
每一日、每一隻、兩條路徑逐個比較。差異 = 掃描器同回測唔係同一套規則 → 唔准發佈。
用法:python equivalence_check.py [--data DIR | --source yf]
"""
import argparse
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lab                  # noqa: E402
import rules_v642 as R      # noqa: E402
import signals_v66 as S     # noqa: E402


def compare(sig):
    n, diffs = 0, []
    for tk, df in sig.items():
        for i in range(80, len(df)):
            row = df.iloc[i]
            ev = S.evaluate(row)
            for path, cfg in (("bt", lab.AS_TRADED), ("scan", lab.SCANNER)):
                a = lab.build_signal(row["sig"], cfg)
                b = S.on_path(ev, path)
                n += 1
                ea, eb = (a or {}).get("engine"), (b or {}).get("engine")
                same = ea == eb and (ea is None or (abs(a["stop"] - b["stop"]) < 1e-9
                                                    and (a["target"] or 0) == (b["target"] or 0)
                                                    and a["score"] == b["score"]))
                if not same:
                    diffs.append((tk, str(df.index[i].date()), path, ea, eb))
    return n, diffs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["csv", "yf"], default="csv")
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    a = ap.parse_args()
    tickers = R.TICKERS + ["SPY"]
    data = lab.load_csv(a.data, tickers) if a.source == "csv" else lab.load_yf(tickers)
    sig, _ = lab.precompute(data)
    n, diffs = compare(sig)
    print(f"比較 {n} 次,差異 {len(diffs)}")
    for d in diffs[:20]:
        print("  ", d)
    sys.exit(0 if not diffs else 1)


if __name__ == "__main__":
    main()
