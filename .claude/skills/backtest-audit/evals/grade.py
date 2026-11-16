#!/usr/bin/env python3
"""
Grade backtest-audit eval outputs against the assertions in evals.json.

Checks are regex-based so they are reproducible and re-runnable across
iterations. Where an assertion needs judgement rather than pattern matching it
is marked NEEDS-REVIEW rather than guessed at — a grader that fakes certainty
is the same failure the skill under test exists to catch.

    python grade.py <workspace-iteration-dir>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RUNS = ["with_skill", "without_skill"]


def rx(*pats):
    return [re.compile(p, re.I | re.S) for p in pats]


# assertion_index -> (checker, note). Checker returns True/False/None(=needs review).
def has(text, *pats):
    return any(p.search(text) for p in rx(*pats))


def grade_eval0(text, files):
    return [
        ("Flags the Wikipedia/current-constituents universe as survivorship bias",
         has(text, r"survivor", ) and has(text, r"wikipedia|current .{0,20}constituent|read_html|S&P ?500 (list|member)")),
        ("Notes that point-in-time RANKING does not fix a survivor-selected UNIVERSE",
         has(text, r"point[- ]in[- ]time") and has(text, r"universe")
         and has(text, r"rank\w*|selection")),
        ("Flags the complete absence of commission/slippage/spread modelling",
         has(text, r"no (transaction )?cost|zero cost|without cost|absence of.{0,30}cost|no commission|commission.{0,40}(absent|missing|not modell?ed)|frictionless")),
        ("Computes expected profit per trade in currency, not only percent",
         has(text, r"US?\$\s?\d+(\.\d+)?\s*(per trade|/trade)|per trade.{0,40}US?\$\s?\d")),
        ("Notes that no drawdown or equity curve is computed anywhere",
         has(text, r"(no|never|absent|missing|zero).{0,40}(drawdown|equity curve)|drawdown.{0,40}(not|never) (computed|calculated)")),
        ("Gives a verdict of UNPROVEN or REFUTED, and does not claim SUPPORTED",
         has(text, r"\bunproven\b|\brefuted\b|cannot (tell|establish|support)|not established")
         and not has(text, r"verdict[:\s]+supported")),
        ("Names at least one thing the code does correctly",
         has(text, r"(done|got) (this |it )?right|correct\w*ly|credit where|to (his|its|your) credit|good (instinct|practice)|gap protection|先檢查")),
        ("Does not present illustrative broker rates as measured figures",
         None),  # judgement
    ]


def grade_eval1(text, files):
    return [
        ("Confirms a transaction cost model is present",
         has(text, r"cost model.{0,30}(present|exists|implemented)|CostModel|cost.{0,20}(is|are) (now )?(present|modell?ed|implemented)")),
        ("Confirms drawdown / equity curve statistics are computed",
         has(text, r"(drawdown|equity curve).{0,40}(present|computed|implemented|reported|now)")),
        ("Still flags the hard-coded ticker list as an outstanding survivorship issue",
         has(text, r"(hard[- ]?cod|TICKERS\s*=|38[- ]name|ticker list).{0,200}survivor|survivor.{0,200}(hard[- ]?cod|ticker list|38)")),
        ("Does not report a critical finding that the code has actually fixed",
         None),  # judgement
    ]


def grade_eval2(text, files):
    py = files.get("oos_validation.py", "")
    return [
        ("Actually makes the requested take-profit change rather than only auditing",
         bool(py) and has(py, r"take[_ ]?profit|TAKE_PROFIT|tp_pct|2\.0\s*#.*profit")),
        ("Surfaces at least one pre-existing defect that affects the reported result",
         has(text, r"cost|commission|survivor|cooldown|boundary|drawdown|look[- ]?ahead|truncat|syntax")),
        ("Does not refuse or lecture instead of doing the work",
         bool(py)),
    ]


GRADERS = {0: grade_eval0, 1: grade_eval1, 2: grade_eval2}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1
                else ".claude/skills/backtest-audit-workspace/iteration-1")
    rows = []
    for d in sorted(root.glob("eval-*")):
        meta = json.loads((d / "eval_metadata.json").read_text(encoding="utf-8"))
        eid = meta["eval_id"]
        for run in RUNS:
            out = d / run / "outputs"
            if not out.exists():
                continue
            text, files = "", {}
            for f in out.iterdir():
                body = f.read_text(encoding="utf-8", errors="replace")
                files[f.name] = body
                if f.suffix == ".md":
                    text += "\n" + body
            if not files:
                rows.append((d.name, run, None, "NO OUTPUT"))
                continue
            results = GRADERS[eid](text, files)
            graded = [(t, p) for t, p in results]
            json.dump({"eval_id": eid, "run": run,
                       "expectations": [{"text": t,
                                         "passed": (p if p is not None else False),
                                         "evidence": ("pattern matched" if p
                                                      else "needs human review" if p is None
                                                      else "no matching evidence found")}
                                        for t, p in graded]},
                      open(d / run / "grading.json", "w"), indent=1, ensure_ascii=False)
            rows.append((d.name, run, graded, None))

    print("=" * 78)
    print("backtest-audit — assertion grading")
    print("=" * 78)
    print("\n★ The without_skill baseline had full repo access, and the repo contains")
    print("  the completed audit this skill encodes. Treat with-vs-without as")
    print("  CONTAMINATED (lesson L-007), not as a measure of skill value.\n")

    totals = {r: [0, 0] for r in RUNS}
    for name, run, graded, err in rows:
        if err:
            print(f"{name:34} {run:14} {err}")
            continue
        ok = sum(1 for _, p in graded if p is True)
        # counted, but see the health warning printed above
        rev = sum(1 for _, p in graded if p is None)
        n = len(graded)
        totals[run][0] += ok
        totals[run][1] += n
        print(f"{name:34} {run:14} {ok}/{n} pass" + (f"  ({rev} need review)" if rev else ""))
        for t, p in graded:
            # An unmatched regex means THIS GRADER did not find evidence, which is
            # not the same as the agent failing. Regex graders read low. Saying
            # "FAIL" here would be the exact overclaim the skill exists to catch.
            mark = "PASS" if p is True else ("REVIEW" if p is None else "UNMATCHED")
            print(f"    [{mark:6}] {t}")
        print()

    print("-" * 78)
    for run in RUNS:
        o, n = totals[run]
        if n:
            print(f"  {run:14} {o}/{n} = {o/n*100:.0f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
