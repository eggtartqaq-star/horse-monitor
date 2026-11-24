---
name: backtest-audit
description: >
  Audit a trading strategy backtest for the biases that make a losing system look
  profitable — survivorship in the universe, look-ahead in the signal, missing
  transaction costs, per-trade EV masquerading as a portfolio result, and
  overfitting from hand-tuned thresholds. Use this whenever the user shares
  backtest code, strategy code, a Pine Script indicator, a trading bot, an
  equity curve, or reported performance statistics (win rate, EV per trade,
  Sharpe, profit factor) — and especially when they ask "is this edge real?",
  "why is my live result worse than my backtest?", "should I trade this?", or
  want a strategy reviewed, validated, or improved. Trigger it even when the
  user only asks for a small change to backtest code, because the defects below
  are usually already present and silently inflating every number in the file.
---

# Backtest Audit

A backtest is a measurement instrument. Most retail backtests — and plenty of
professional ones — are broken instruments that read high. The job here is not to
judge whether the *strategy* is good. It is to establish whether the *measurement*
can support any conclusion at all.

Hold that distinction firmly, because it changes the verdict language. "This
strategy loses money" and "this evidence cannot tell us whether this strategy
makes money" are different findings, and only the second one is usually
defensible from code alone.

## Start here

Run the scanner first. It greps for the textual signatures of the common defects
and gives you a map of where to read closely:

```bash
python scripts/scan_backtest.py <path-to-code-or-directory>
```

It is a smoke detector, not a verdict — it finds candidates fast and it does miss
things. Read the code yourself for anything it flags, and for the logic it cannot
see (ordering bugs, boundary handling, capital constraints).

## The seven checks

Work through these in order. The first three decide most cases.

### 1. Universe — who was allowed to be in the test?

The single most common fatal defect, and the one most often *believed* to be
handled. Ask where the ticker list came from. If it was scraped from a current
index membership page, or hand-written by someone who knows how the period turned
out, every company that went bankrupt, got acquired, or was deleted from the index
is missing from the test.

Watch for a specific trap: a backtest can compute its rankings in a properly
point-in-time way — only using data available at each moment — and still draw those
rankings from a survivor-selected candidate set. A clean ranking over a dirty
universe is still dirty. Files that do this often *claim* to have solved
survivorship, sometimes in a printed message, because the author fixed the part
they were thinking about.

Momentum and trend strategies are hit hardest: they buy strength, and the names
that were strong and then died are exactly the ones absent.

**Direction: overstates returns. Magnitude: unknown until re-run — which is the point.**

### 2. Look-ahead — did the test use information it could not have had?

Several distinct forms, and they hide in different places:

- **Signal and fill on the same bar.** A signal computed from a bar's close and
  filled at that same close is only executable if the trader actually transacts at
  the close. Not fatal, but it must be stated, and shifting the fill to the next
  bar's open is the honest default.
- **Indicators that include the current bar** in a regime filter (a 200-day
  average that includes today, then gating today's entry).
- **Boundary handling in walk-forward or in-sample/out-of-sample splits.** Look for
  a loop that `break`s at a window edge without recording the position. Trades
  still open at a boundary are silently discarded. In a trailing-stop system,
  losers exit fast and winners run, so the open-at-boundary population skews to
  winners — and the shorter window loses a larger *share* of its trades.
- **Any parameter chosen by looking at the whole sample**, then "validated" on a
  slice of that same sample.

To test a signal function directly: call it at bar *i* on the full data, then call
it again on data truncated at bar *i*, and assert the result is identical. If it
changes, the function reads forward.

### 3. Costs — is the reported edge bigger than a ticket?

Grep for commission, fee, spread, slippage. Finding nothing is common and decisive.

Then do the arithmetic **in currency, not percent**, because percent hides the
problem at small account sizes:

```
position notional = risk budget / stop distance
expected gross profit per trade = notional x EV%
round-trip cost = max(min_commission, per_share x shares, pct x notional) x 2
                  + spread + slippage + FX
```

When expected gross profit per trade is on the order of a couple of dollars and the
round-trip ticket is also a couple of dollars, the strategy is a
commission-generation machine and no amount of further optimisation changes that.
This calculation needs no market data and often ends the analysis.

Also derive the **minimum viable account size**: the notional at which ticket cost
falls below ~20% of gross EV. That number, not the EV, tells the user whether the
system is tradeable by them today.

### 4. Portfolio realism — is this a portfolio result or an average of daydreams?

Per-trade EV pooled across many symbols treats trades as independent draws. They
are concurrent, correlated, and capital-constrained. Check for:

- a cap on simultaneous positions (usually absent),
- a cash ledger that can actually fund the positions taken,
- integer share sizing, and how much risk budget rounding discards,
- a total portfolio heat limit,
- what the per-trade risk rule implies when N positions are open at once.

A "1% risk per trade" rule with no concurrency cap is an uncapped leverage rule
wearing a modest label.

### 5. Overfitting — how many things were tried?

Count the researcher degrees of freedom: every hand-chosen threshold, every weight,
every lookback. Scoring functions with twenty tuned boundaries are common.

A large jump in reported performance from a single parameter change is the
signature of a fitted parameter rather than a discovered effect — treat it as a
red flag, not a triumph. Ask how many variants preceded the current one; version
numbers in filenames are evidence. If the count is high, the honest tools are
walk-forward validation, a deflated Sharpe using the real trial count, and
reporting a distribution across folds rather than one number.

### 6. Reporting — the ugly numbers come first

Many backtests never compute a drawdown. Grep for drawdown, equity, Sharpe,
Sortino. If there is no equity curve, there is no drawdown, and the user is
trading without knowing the number that actually makes people quit.

Insist on this order: **max drawdown, drawdown duration, worst month, tail (worst
trades, 5th percentile) — then** return, then Sharpe. A strategy with an attractive
Sharpe and a 40% drawdown is one the user will abandon at the bottom.

### 7. Parity — is the tested system the traded system?

When a strategy exists in more than one place (a Python backtest, a Pine Script
indicator on the chart, a live bot, a scanner), diff them. Divergences found in
practice: different stop-width caps in each file, a constant declared as "locked"
and never referenced, different take-profit selection rules, and an indicator that
implements only one of two engines.

This matters more than it sounds. If the chart disagrees with the backtest, the
user is trading a strategy nobody has tested.

## Reporting the findings

Severity-rank them: CRITICAL / HIGH / MEDIUM / LOW. For each finding give the
exact file and function, what is wrong, **why it matters in money terms**, and a
concrete fix. Vague findings get ignored; a finding with a dollar figure attached
gets acted on.

Then give a verdict, and be precise about which one:

- **SUPPORTED** — the evidence survives the checks.
- **UNPROVEN** — the evidence cannot distinguish a real edge from the defects
  found. Usually the correct verdict. Say plainly that this is not the same as
  saying the strategy does not work.
- **REFUTED** — something decisive, most often the cost arithmetic in check 3.

Rank the fixes by what unblocks the most, and name the one to do first. Prefer the
fix that can **change the sign of the answer** over the one that refines a number
which may well be negative. There is no point buying point-in-time data to more
precisely measure a strategy that costs more to trade than it earns.

## Also say what is right

A review that only lists faults gets dismissed, and the good parts get destroyed in
the next rewrite. Look for and name things done well — gap protection on stops,
checking a stop before updating a trailing level, resolving same-bar ambiguity
against the trader, an out-of-sample test with the pass mark written down in
advance. Preserving those is part of the deliverable.

## Tone

The user usually has real money on this and often built it themselves over months.
Be direct about what is broken and never soften a fatal finding — but attack the
measurement, not the person. When their instincts were good, say so specifically.

If the code contains signs of the user breaking their own rules (a comment
reproaching themselves for a trade), treat it as a control-design problem rather
than a character problem: a control that routes through willpower at the moment of
the trade has already failed. Look for a mechanism instead. And check whether a
bug caused the incident before concluding it was indiscipline.

## Do not invent numbers

You usually cannot run the backtest — no market data, no time, or the code does not
run. Reason from the code and say so. Where a figure is needed to illustrate a
cost or a bias, label it as an assumption and tell the user to substitute their
real values. Never present an illustrative number as a measured one.

If you write or fix code as part of the audit, test it before handing it over.
Shipping an untested backtest fix inside a backtest audit is its own punchline.
