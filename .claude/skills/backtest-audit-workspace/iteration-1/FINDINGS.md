# Iteration 1 — what this run does and does not establish

**Date:** 2026-08-03 · 6 runs launched, 6 produced output, 1 write-up lost to a
session limit (`eval-2/with_skill/response.md`; its code file survived).

## The headline: this run produced NO trustworthy verdict on the skill

Two independent defects in the evaluation itself, both mine:

### 1. The baseline is contaminated (L-007)

The `without_skill` control had full repo access, and this repo contains
`reports/quant/2026-07-30-v64-backtest-audit.md` — the completed audit whose
method the skill encodes — plus the corrected V6.5 code and the review
artifacts. The eval-0 baseline cited `strategy/v6.5/portfolio_sim.py --mode
compare`, which exists *only because of* the audit under test.

A control that can read the answer key is not a control. Any with-vs-without
number from this run is meaningless.

**Fix for iteration 2:** copy only the subject code into a bare directory and
run the control there.

### 2. The grader reads low

Raw regex tally was with_skill 10/15, without_skill 11/15. Both numbers are
wrong. Manual inspection of the eval-1 outputs found that both runs *did*
discuss drawdown, survivorship and the cost model — the regexes simply missed
the phrasings used.

The tempting fix is to widen the regexes until the numbers look right. That is
fitting the instrument to the sample, which is the exact defect this skill
exists to detect. Instead unmatched checks now report `UNMATCHED` rather than
`FAIL`, so the grader stops overclaiming.

**Fix for iteration 2:** grade with a judge model against the assertion text,
and keep regexes only for the mechanically checkable ones (did a file change,
does the code contain a take-profit branch).

## What the run DID establish — and it is worth more than the score

The eval-0 **baseline** — the agent running *without* the skill — discovered
that **all four `strategy/v6.4/*.py` files fail to parse.** The CEO had
reconstructed them from PDFs that clip code at ~80 columns and audited them for
three days without running a syntax check.

That finding is the most valuable output of the entire evaluation, it came from
the control rather than the treatment, and it is a defect in the auditor's work
rather than the Owner's. Recorded as L-006, triaged in
`strategy/v6.4/README-SOURCE-FIDELITY.md`.

## Qualitative read (not a score)

- Both eval-0 runs reached the same verdict and both did the cost arithmetic in
  dollars — the calculation that decides the case.
- eval-2 mattered most for the trigger design: a "pushy" description risks
  turning a small request into an unwanted audit. **Both runs made the requested
  change** rather than lecturing, which is the behaviour the assertion was
  written to protect.
- eval-1 is the anti-false-alarm test. Neither run manufactured criticals that
  V6.5 has genuinely fixed.

## Status

**Iteration 1 is a dry run of the harness, not a measurement of the skill.**
The harness now works end to end; the measurement has to be redone against a
clean baseline before any claim about the skill's value is defensible.
