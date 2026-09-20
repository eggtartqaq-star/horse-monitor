#!/usr/bin/env python3
"""
Append a provenance + coverage block to every dated research report.

Why this exists
---------------
69 reports sit in reports/ and almost none record two facts that decide how much
weight a reader should give them:

  1. From 2026-07-30 onward, every direct page fetch in this environment returned
     HTTP 403 (organisation egress policy). Figures in those reports are
     search-engine extractions of primary documents, not the documents. A reader
     six months from now has no way to know that from the report alone.

  2. Department 3 (Quant Research) filed nothing on any of the researched names.
     Every verdict rested on fundamentals, valuation, news and technicals with no
     quantitative input. That is a coverage gap and it was never recorded in the
     reports themselves.

Design notes
------------
- IDEMPOTENT. Re-running does nothing to a file already stamped.
- HONEST ABOUT DATES. The 403 condition is only *confirmed* from 2026-07-30, when
  it was first observed and verified. Earlier reports get a weaker, accurate
  statement rather than a claim backdated onto them.
- APPENDS, never rewrites. Existing content is untouched.

    python scripts/stamp_provenance.py --dry-run
    python scripts/stamp_provenance.py
"""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

REPORTS = Path("reports")
MARKER = "<!-- provenance-stamp -->"

# The date the 403 egress condition was first observed AND verified
# (proxy status endpoint checked, relay failures logged).
EGRESS_CONFIRMED_FROM = date(2026, 7, 30)

# Names that went through a research pipeline with no Department 3 input.
NO_QUANT = {"mu", "mrvl", "klac", "be", "intc", "minimax", "0100hk", "3416hk"}

DATED = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")


def names_in(slug: str) -> bool:
    """
    Token match, not substring. A two-letter ticker like "be" would otherwise
    match any slug containing it — "tube-analysis" for instance. Correct today
    by luck; this makes it correct by construction.
    """
    tokens = {t.lower() for t in re.split(r"[-_. ]+", slug) if t}
    return bool(tokens & NO_QUANT)


def report_date(p: Path):
    m = DATED.search(p.name)
    if not m:
        return None, None
    y, mo, d, slug = m.groups()
    try:
        return date(int(y), int(mo), int(d)), slug
    except ValueError:
        return None, None


def block(d: date, slug: str) -> str:
    lines = [
        "",
        "---",
        "",
        MARKER,
        "## Provenance and coverage",
        "",
        "*Appended by `scripts/stamp_provenance.py`. Records how this report was",
        "produced, so its weight can be judged later without reconstructing the",
        "conditions from memory.*",
        "",
    ]

    if d >= EGRESS_CONFIRMED_FROM:
        lines += [
            "**Sourcing — direct page fetch was blocked.** In this environment every",
            "direct page fetch returned HTTP 403 under an organisation egress policy",
            "(verified against the proxy status endpoint; hosts denied included",
            "`hkexnews.hk`, `finance.yahoo.com`, `stooq.com`, `alphavantage.co`,",
            "`data.nasdaq.com`). **No primary filing or factsheet was opened.** Figures",
            "here are search-engine extractions of those documents plus secondary",
            "reporting. Treat structural claims (share structure, fee schedules, exact",
            "line items) as lower confidence than headline financials, which were",
            "generally cross-checked against two or more independent sources.",
            "",
        ]
    else:
        lines += [
            "**Sourcing.** This report predates 2026-07-30, when the environment's",
            "HTTP 403 egress restriction was first observed and verified. Whether",
            "direct page fetch was available when this was written **was not recorded",
            "at the time**, so no claim is made either way — rely on the sourcing",
            "stated in the body of the report itself.",
            "",
        ]

    if names_in(slug):
        lines += [
            "**Coverage gap — no quantitative input.** Department 3 (Quant Research:",
            "賭馬狗, Math King, Tom, AI指標) filed **nothing** on this name. Session",
            "limits forced the pipeline down to a three-agent core and quant was cut",
            "first, without being logged as a gap at the time. Any conclusion here",
            "rests on fundamentals, valuation, news and technicals only.",
            "",
        ]

    lines += [
        "**Standing rules.** No figure in this report may be invented; every number",
        "should carry a source and a date, and estimates should be marked as",
        "estimates (CLAUDE.md rule 5). Research and decision support only — not",
        "financial advice, and no agent of this firm places orders.",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    stamped = skipped = undated = 0
    changes = []
    for p in sorted(REPORTS.rglob("*.md")):
        d, slug = report_date(p)
        if d is None:
            undated += 1
            continue
        text = p.read_text(encoding="utf-8")
        if MARKER in text:
            skipped += 1
            continue
        new = text.rstrip() + "\n" + block(d, slug)
        changes.append((p, len(new) - len(text),
                        "egress-403" if d >= EGRESS_CONFIRMED_FROM else "date-unverified",
                        "no-quant" if names_in(slug) else "-"))
        if not a.dry_run:
            p.write_text(new, encoding="utf-8")
        stamped += 1

    print(f"{'DRY RUN — ' if a.dry_run else ''}stamped {stamped} · "
          f"already stamped {skipped} · undated/skipped {undated}")
    print(f"{'file':<52}{'+chars':>8}  {'sourcing':<18}{'coverage'}")
    for p, delta, src, cov in changes[:80]:
        print(f"{str(p):<52}{delta:>8}  {src:<18}{cov}")
    if len(changes) > 80:
        print(f"  ... and {len(changes)-80} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
