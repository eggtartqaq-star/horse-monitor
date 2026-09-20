#!/usr/bin/env python3
"""
Static scanner for common backtest defects.

A smoke detector, not a verdict. It finds textual signatures fast so the audit
can go straight to the code that matters. It cannot see ordering bugs, capital
constraints, or whether a universe is survivor-selected in spirit — read the
flagged code yourself.

    python scan_backtest.py <file-or-directory> [--json]

Exit code is 0 always; this reports, it does not gate.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SRC_SUFFIXES = {".py", ".pine", ".js", ".ts", ".r", ".R", ".ipynb", ".jl", ".cs", ".java"}

# (id, severity, regex, what it means, what to check)
CHECKS = [
    ("COST-MISSING", "critical",
     None,  # absence check, handled specially
     "No transaction cost terms found anywhere",
     "Grep found no commission/fee/spread/slippage. Reported EV is gross. Do the "
     "currency arithmetic in check 3 — it often ends the analysis."),

    ("DD-MISSING", "high",
     None,  # absence check
     "No drawdown / equity curve / risk statistic computed",
     "No equity curve means no drawdown. The user is trading without the number "
     "that actually makes people quit."),

    ("UNIVERSE-CURRENT", "critical",
     r"(wikipedia\.org/wiki/List_of|read_html\s*\(|current[_ ]constituents|"
     r"sp500[_ ]?(tickers|symbols|list)|\.components\b)",
     "Universe may be scraped from CURRENT index membership",
     "If this list is today's constituents and the test runs over past years, "
     "every delisted/acquired/bankrupt name is missing. Point-in-time RANKING "
     "does not fix a survivor-selected UNIVERSE."),

    ("UNIVERSE-HARDCODED", "high",
     r"^\s*(FALLBACK|TICKERS|UNIVERSE|SYMBOLS|STOCKS)\s*=\s*[\[\(]",
     "Hard-coded ticker list",
     "Who chose these names, and when? A list written today for a test over past "
     "years encodes hindsight. Check for obvious post-hoc winners."),

    ("FILL-AT-CLOSE", "medium",
     r"(entry|fill|buy|exec\w*)\s*=\s*[^=\n]*\[?[\"']?Close",
     "Entry appears to be at the signal bar's close",
     "Executable only if the trader really transacts at the close. Prefer signal "
     "at bar t, fill at bar t+1 open, and state the assumption either way."),

    ("BOUNDARY-BREAK", "high",
     r"break\b(?![^\n]*#[^\n]*(record|append|log))",
     "A `break` — check whether it discards an open position at a window edge",
     "If a trade still open at a boundary is never appended, it vanishes. In a "
     "trailing-stop system the open-at-boundary population skews to winners, so "
     "the shorter window is penalised more."),

    ("TRAIL-BEFORE-CHECK", "critical",
     r"(trail|stop)\s*=\s*max\(",
     "Trailing stop update — verify it happens AFTER the stop is tested",
     "Updating the trail before testing today's low against it is a classic "
     "look-ahead that inflates every trend result. Confirm the order."),

    ("NO-CONCURRENCY-CAP", "high",
     r"(open_positions|positions|portfolio)\s*\[",
     "Position container — check for a cap on simultaneous holdings",
     "A per-trade risk rule with no concurrency cap is an uncapped leverage rule. "
     "Count what N open positions implies for total heat."),

    ("SAME-BAR-REGIME", "medium",
     r"(rolling\(\s*200|sma\(\s*close\s*,\s*200|MA200|ma_?200)",
     "Long moving average used as a regime filter",
     "Does the average include the current bar, and is that same bar traded? "
     "Shift it one bar and see how much of the edge depended on it."),

    ("MANY-THRESHOLDS", "medium",
     r"(elif|else\s+if)\s+[^\n]*(<=|>=|<|>)\s*-?\d+(\.\d+)?\s*[:{]",
     "Hand-tuned numeric threshold in a scoring function",
     "Each one is a researcher degree of freedom. Count them; a scoring function "
     "with ~20 is common and makes a single out-of-sample split weak evidence."),

    ("VERSION-SPRAWL", "low",
     r"[vV]\d+[._]\d+",
     "Version number in code or filename",
     "Evidence of how many variants preceded this one. Feeds the trial count for "
     "a deflated Sharpe."),

    ("DATA-SINGLE-SOURCE", "medium",
     r"(yfinance|yf\.|pandas_datareader|get_data_yahoo|alpha_vantage|quandl)",
     "Single market-data vendor",
     "If one vendor supplies prices, stops and sizing with no cross-check, a "
     "silent adjustment change moves stop levels without raising an error."),

    ("SECRET-INLINE", "high",
     r"(TOKEN|API_KEY|SECRET|PASSWORD)\s*=\s*[\"'][^\"']{8,}",
     "Possible credential in source",
     "Move it to an environment variable — this file gets shared."),
]

COST_TERMS = re.compile(
    r"(commission|slippage|\bspread\b|brokerage|\bfees?\b|transaction[_ ]cost|"
    r"cost_bps|滑價|手續費|佣金)", re.I)
RISK_TERMS = re.compile(
    r"(drawdown|max_dd|\bsharpe\b|sortino|equity_curve|\bequity\b|calmar|"
    r"回撤|淨值)", re.I)

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

# Checks whose finding is the COUNT, not the individual lines. Listing 40 tuned
# thresholds one by one buries everything else; the number is the signal.
COUNT_ONLY = {"MANY-THRESHOLDS", "VERSION-SPRAWL"}


def strip_comments(text: str, suffix: str) -> str:
    """
    Rough comment/string removal for the ABSENCE checks.

    This matters more than it looks. A file can carry a comment saying
    "remember to check drawdown" and contain zero lines that compute one — the
    naive grep then reports a clean bill of health on the single most important
    missing statistic. Same for a "TODO: add slippage".
    """
    # Triple-quoted blocks first — a module docstring saying "remember to check
    # drawdown" is prose, not an implementation, and must not read as one.
    text = re.sub(r'"""[\s\S]*?"""', " ", text)
    text = re.sub(r"'''[\s\S]*?'''", " ", text)
    # Pine and C-style block comments
    text = re.sub(r"/\*[\s\S]*?\*/", " ", text)

    out = []
    for line in text.splitlines():
        s = line
        if suffix in {".py", ".r", ".R", ".jl"}:
            s = re.sub(r"#.*$", "", s)
        if suffix in {".pine", ".js", ".ts", ".cs", ".java"}:
            s = re.sub(r"//.*$", "", s)
        # single-line string literals — a printed message is not an implementation
        s = re.sub(r'"[^"]*"|\'[^\']*\'', " ", s)
        out.append(s)
    return "\n".join(out)


def iter_files(root: Path):
    if root.is_file():
        yield root
        return
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix in SRC_SUFFIXES:
            if any(part in {".git", "__pycache__", "node_modules", ".venv", "venv"}
                   for part in p.parts):
                continue
            yield p


def scan(root: Path):
    findings, files, cost_hits, risk_hits, total_lines = [], [], [], [], 0

    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        files.append(path)
        lines = text.splitlines()
        total_lines += len(lines)

        # absence checks run on CODE only — comments and printed strings removed
        code_only = strip_comments(text, path.suffix)
        if COST_TERMS.search(code_only):
            cost_hits.append(path)
        if RISK_TERMS.search(code_only):
            risk_hits.append(path)

        for cid, sev, pattern, title, why in CHECKS:
            if pattern is None:
                continue
            rx = re.compile(pattern, re.M)
            hits = [(n, ln.strip()[:120]) for n, ln in enumerate(lines, 1) if rx.search(ln)]
            if not hits:
                continue
            if cid in COUNT_ONLY:
                findings.append({
                    "id": cid, "severity": sev, "title": title, "why": why,
                    "file": str(path), "line": 0, "count": len(hits),
                    "code": f"{len(hits)} occurrence(s) — the count is the finding",
                })
                continue
            for n, code in hits[:3]:
                findings.append({"id": cid, "severity": sev, "title": title,
                                 "why": why, "file": str(path), "line": n, "code": code})
            if len(hits) > 3:
                findings.append({
                    "id": cid, "severity": sev, "title": title, "why": why,
                    "file": str(path), "line": 0,
                    "code": f"... and {len(hits) - 3} more in this file",
                })

    # absence checks — only meaningful once we know files were actually read
    if files and not cost_hits:
        c = next(c for c in CHECKS if c[0] == "COST-MISSING")
        findings.append({"id": c[0], "severity": c[1], "title": c[3], "why": c[4],
                         "file": str(root), "line": 0,
                         "code": "(no commission/slippage/spread/fee terms in any file)"})
    if files and not risk_hits:
        c = next(c for c in CHECKS if c[0] == "DD-MISSING")
        findings.append({"id": c[0], "severity": c[1], "title": c[3], "why": c[4],
                         "file": str(root), "line": 0,
                         "code": "(no drawdown/equity/Sharpe terms in any file)"})

    findings.sort(key=lambda f: (SEV_ORDER[f["severity"]], f["id"], f["file"], f["line"]))
    return findings, files, total_lines, bool(cost_hits), bool(risk_hits)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    root = Path(a.path)
    if not root.exists():
        print(f"not found: {root}", file=sys.stderr)
        return 0

    findings, files, nlines, has_cost, has_risk = scan(root)

    if a.json:
        print(json.dumps({"root": str(root), "files": len(files), "lines": nlines,
                          "has_cost_model": has_cost, "has_risk_stats": has_risk,
                          "findings": findings}, indent=1))
        return 0

    print("=" * 74)
    print(f"Backtest scan — {root}")
    print(f"{len(files)} source file(s), {nlines:,} lines")
    print("=" * 74)

    if not files:
        print("\nNo source files found. Point this at the code, not the output.")
        return 0

    print(f"\n  transaction cost model present : {'yes' if has_cost else 'NO'}")
    print(f"  drawdown / equity statistics   : {'yes' if has_risk else 'NO'}")

    counts = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    print("\n  " + "  ".join(f"{s}: {counts.get(s, 0)}"
                             for s in ("critical", "high", "medium", "low")))

    current = None
    for f in findings:
        if f["id"] != current:
            current = f["id"]
            print(f"\n{'-' * 74}\n[{f['severity'].upper()}] {f['id']} — {f['title']}")
            print(f"  → {f['why']}")
        loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
        print(f"     {loc}")
        if f["code"]:
            print(f"       {f['code']}")

    print("\n" + "=" * 74)
    print("This is a smoke detector, not a verdict. Every item above is a place to")
    print("READ, not a confirmed defect — and the checks it cannot do statically")
    print("(universe provenance, capital constraints, trail ordering, parity between")
    print("chart and backtest) are usually where the fatal ones live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
