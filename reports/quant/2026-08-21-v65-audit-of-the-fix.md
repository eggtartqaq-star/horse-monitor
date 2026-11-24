# V6.5 — audit of the data-loading fix, and what the real-data run changed

**皮褸黃 (CEO), applying `.claude/skills/backtest-audit` · 2026-08-21**

> **Conflict of interest, declared again.** I wrote V6.5, I wrote the fix audited here,
> and I am auditing it. That is not independent and should be re-run by Tom. It is
> nonetheless worth doing, because **the fix I shipped on 2026-08-14 contained a defect
> of the same class as the one it was fixing.**

## VERDICT: **UNPROVEN** — unchanged, and the reason has moved

The 2026-08-07 self-audit said the simulator was no longer the weak link. The Owner's
first real-data run on 2026-08-14 confirmed that and simultaneously exposed a data-layer
defect the simulator could not see. That defect is now fixed and tested. **The verdict is
unchanged because the two things that decide whether an edge exists — the survivor-selected
universe (F-01) and the absence of walk-forward validation (F-10) — remain untouched.**

---

## Findings against the seven checks

### Check 1 — Universe · **HIGH, unfixed, and now measured**

`portfolio_sim.py` still carries the same hand-written 38-name list chosen in 2026 and run
over 2019–2026. Disclosed in the README, still not remediated.

**New this cycle:** the first real run silently completed on **31 of 38 names** — NVDA,
META, TSLA, AVGO, AMD, QCOM and UNH returned no data — and printed its signal-distribution
conclusions as though the universe were whole. The count appeared only in the download log.

**This is the check-1 failure mode in a form the skill does not list:** not a survivor-biased
universe, but a **silently truncated** one. A ticker with no data produces zero signals, so a
missing name reads as an unimportant one. The seven absent names included the five strongest
trend performers of the period — precisely what a survivorship analysis exists to examine.

I drew a survivorship conclusion from that partial sample and **retracted it in place** in
`reports/quant/2026-08-14-v65-diagnostics-first-real-data.md`.

### Check 2 — Look-ahead · **PASS**

Unchanged and still verified. Signal at bar *t*, fill at *t+1* open; regime flag lagged one
bar; `selftest.py` asserts the signal function is identical when the frame is truncated —
18 sample points, zero mismatches. Positions open at the end are recorded as `OPEN_AT_END`.

**The scanner's HIGH on `portfolio_sim.py:133` is a FALSE POSITIVE.** It matched a `break`
inside the download retry loop — a loop-exit on success, not a window-edge discard. Recorded
so the next auditor does not re-investigate it.

### Check 3 — Costs · **PASS, and now with real numbers**

The Owner's run produced the first cost figures from the corrected instrument. On synthetic
data, same signals, broker as the only variable:

| Broker | Net EV per trade |
|---|---|
| free | **+0.423%** |
| ibkr_fixed | **−1.953%** |
| hk_retail | **−4.627%** |

**A 5.050pp spread per trade.** At a Hong Kong retail broker the strategy must clear ~5%
gross per trade merely to break even; realistic swing edges are under 1%. Broker choice is
a **precondition, not an optimisation.**

Test [1] also showed a normal position resolving to **6 shares, $120 notional, consuming 47%
of the entire risk budget.** The account, not the strategy, is the binding constraint —
the same fixed-cost-on-small-notional arithmetic that decided the 3416 review.

**Still not measured on real prices.** `--mode compare` has not been run.

### Check 4 — Portfolio realism · **PASS**

Unchanged: real cash ledger, integer sizing, six blocking conditions, rejection log,
concurrency and heat caps asserted in the self-test. MEDIUM-2 (the drawdown breaker being a
one-way kill switch) is now documented in code rather than fixed — acceptable, as it is
labelled.

### Check 5 — Overfitting · **UNFIXED**

21 hand-tuned thresholds in `rules.py`, unchanged by design. No walk-forward, no purging, no
embargo, no deflated Sharpe.

**New evidence that sharpens this.** The real run showed **Engine 1: 324 signals, Engine 2:
3,000 — a 9.3:1 ratio.** Engine 1 carries its own thresholds, stops and cooldown for under a
tenth of the signals. Those are researcher degrees of freedom bought at almost no
contribution. Whether Engine 1 is a deliberately extreme filter or a mis-calibrated one
**has never been checked, because nobody had counted.**

### Check 6 — Reporting · **PASS** — ugly numbers first, unchanged.

### Check 7 — Parity · **PARTIAL** — `rules.py` remains the single Python source of truth;
Pine still cannot import it and the golden-file test is still unbuilt.

---

## The fix I shipped on 14 August, audited

### **HIGH — SPY was the one call with no retry, and it ran last.**

The 14 August fix added retry logic to every ticker and **left SPY on a single unprotected
call, executed after all 38 tickers** — i.e. at the moment rate-limiting is most likely.

SPY is the sole source of the regime filter. Had it failed, `spy` would have been empty and
the diagnostic would have printed a bull-share percentage computed from nothing. **The regime
finding was the only part of the 14 August run that survived scrutiny**, and it rested on the
one fetch I had not protected.

**Fixed and tested:** SPY now goes through the same retry path, and a failure calls
`sys.exit(1)` with an explanation rather than continuing. Verified by injecting a fake
yfinance in which SPY is unobtainable — the function now raises `SystemExit(1)` instead of
returning normally.

### **MEDIUM — a genuinely short history was misdiagnosed as rate-limiting.**

The 14 August version tested `len(df) >= 300` and treated any shortfall as a failure to
retry. A recent IPO with 120 bars would burn 17 seconds of sleeps, be added to `missing`, and
trigger a warning telling the Owner to wait and re-run — **which can never help, because
re-running does not lengthen a company's price history.** The original code distinguished
these two cases; my rewrite lost the distinction.

**Fixed and tested:** `_fetch()` now returns `ok` / `short` / `none`. A short history returns
on the **first** attempt and is reported separately as "歷史不足(非限流,重跑冇用)".
Verified: short history uses 1 attempt, a persistently failing ticker uses 4.

### LOW — worst-case sleep budget is ~10.8 minutes if every ticker fails (38 × 17s). The
Owner was told 6–7 minutes. Not corrected; recorded so the estimate can be stated honestly.

---

## What is right, and must survive any rewrite

1. **Costs on both legs of every fill**, broker as a switch rather than an assumption.
2. **A real cash ledger** — an unfundable signal is recorded as rejected, not silently taken.
3. **Signal at *t*, fill at *t+1* open**, with a test proving the signal cannot read forward.
4. **The rejection log**, which turned "the account is too small" into a count.
5. **Ugly numbers first**, by explicit design.
6. **A self-test that runs without market data** — 20 assertions, all passing.
7. **The diagnostic gate itself.** It cost nothing, ran in five minutes, and caught a data
   defect that would have corrupted every downstream conclusion including a paid one.

## Fix order

1. **Re-run the diagnostic with all 38 names.** Everything downstream inherits the sample.
2. **`--mode compare` on real prices** — the cost question, unmeasured on real data.
3. **Diagnose Engine 1's 9.7% share.** Free, and it changes what "the model" is.
4. **Walk-forward with 2022 held out** — the only genuine bear year in the sample.
5. **Point-in-time universe.** Priority restored after the retraction above.

**None of these change the verdict.** UNPROVEN stands until the universe and the validation
scheme are fixed.

---

*Research and decision support. No performance figure here is a return. The cost table is
from synthetic data with a gap distribution I chose, and is explicitly not evidence about
real markets.*

---

<!-- provenance-stamp -->
## Provenance and coverage

*Appended by `scripts/stamp_provenance.py`. Records how this report was
produced, so its weight can be judged later without reconstructing the
conditions from memory.*

**Sourcing — direct page fetch was blocked.** In this environment every
direct page fetch returned HTTP 403 under an organisation egress policy
(verified against the proxy status endpoint; hosts denied included
`hkexnews.hk`, `finance.yahoo.com`, `stooq.com`, `alphavantage.co`,
`data.nasdaq.com`). **No primary filing or factsheet was opened.** Figures
here are search-engine extractions of those documents plus secondary
reporting. Treat structural claims (share structure, fee schedules, exact
line items) as lower confidence than headline financials, which were
generally cross-checked against two or more independent sources.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
