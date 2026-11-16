# V6.5 diagnostics — the first real-data evidence this firm has ever had

**皮褸黃 (CEO) · 2026-08-14 · run by the Owner on his own machine**

> Every prior number on this strategy came from synthetic data or from a backtest whose
> defects had not been fixed. This is the first output produced by the corrected simulator
> against **real prices, 2019-01-01 → 2026-07-01, 1,883 bars**. It was meant to answer the
> two gating questions Tom set before further money or work is committed. It answers one
> of them, and exposes a defect in the tool while failing to answer the other.

## ⚠️ Read this first — the run was made on an incomplete sample

**Seven of the 38 tickers returned no data: NVDA, META, TSLA, AVGO, AMD, QCOM, UNH.**
The log records `成功 31 隻` — the simulator continued on **31 names** and printed its
conclusions without flagging the gap in the diagnostic section. This was visible only in
the log file, not on screen.

Yahoo reported them as "possibly delisted". They are not delisted. The failures fall in a
near-contiguous block (positions 5–10 of the download loop, plus position 23), which is the
signature of **transient rate-limiting**, not a data problem.

**Consequence: the signal-distribution finding in §2 is not usable, and the survivorship
conclusion I drew from it in the first version of this note was wrong and is retracted.**
A ticker with no data necessarily produces zero signals, so absent names look
"unimportant" when in fact they were never tested. The missing seven include **NVDA, META,
TSLA, AVGO and AMD** — the strongest trend names of the period and precisely the ones a
survivorship analysis most needs to see.

**The regime finding in §1 is unaffected**, because it is computed from SPY alone, which
downloaded in full (1,883 bars).

| Gate | Threshold | Result | Verdict |
|---|---|---|---|
| Bull-market share of sample | abandon if >80% | **71.7% raw / ~80.2% on valid days** | **MARGINAL — at the line** |
| Signal concentration | abandon if 3–4 names dominate | top 5 = 26.1% **of a 31-name sample** | **VOID — re-run required** |

The run also surfaced a **finding that was not on the checklist and survives the data gap
entirely** — see §3.

---

## 1 · Regime coverage — the headline flatters it

**牛市日數佔比: 71.7%**, below the 80% abandon threshold. The per-year breakdown is far
more informative than the headline:

| Year | Bull-day % | Note |
|---|---|---|
| 2019 | **21%** | **Artifact — see below** |
| 2020 | 77% | COVID crash and recovery |
| 2021 | **100%** | flag never turned off |
| 2022 | **19%** | the only genuine sustained bear year |
| 2023 | 93% | |
| 2024 | **100%** | flag never turned off |
| 2025 | 83% | |
| 2026 | 90% | part-year, sample ends 1 July |

**2019 is a warm-up artifact, not a bear market — and this is now verified, not inferred.**
The sample runs 2019-01-01 → 2026-07-01 (1,883 bars), so 2019 is a *full* year of data. But
the MA200 regime filter needs 200 trading days before it can produce any reading at all, so
roughly the first 200 bars of 2019 are structurally incapable of registering as "bull".

**Verification:** running the same diagnostic against a strictly monotonic rising series —
100% bull by construction — 2019 still reports **23%**. The Owner's real data reports
**21%**. The year carries essentially no information.

**Counting only days where the filter can actually read, the bull share is ~80.2%**
(1,350 bull days ÷ 1,683 valid days) — **at the abandon threshold, not comfortably below
it.** *(My arithmetic on the reported per-year percentages and trading-day counts; the
day counts reconstruct the printed 71.7% headline exactly, which validates the model.)*

**What this means in plain terms: the strategy has been tested against exactly one
sustained bear market — 2022 — plus one crash-and-recovery in 2020.** Two independent
adverse episodes is a very thin basis for any claim about drawdown behaviour, regardless
of how many calendar years the sample spans.

**This does not kill the project.** It does mean that any drawdown statistic produced from
this sample should be read as a **best case**, and that walk-forward validation must be
built so that the 2022 window is a genuine out-of-sample test rather than part of the
fitting set.

## 2 · Signal concentration — VOID, computed on 31 of 38 names

> **VOID pending a clean re-run.** Everything in this section was computed on 31 of 38
> names, with NVDA, META, TSLA, AVGO, AMD, QCOM and UNH absent. It is recorded for
> completeness and must not be used to draw a survivorship conclusion.

**Top five by signal count:** AAPL 195, COST 195, MSFT 162, NFLX 159, LLY 158 —
**869 of 3,324 signals, 26.1%.**
**Bottom five:** SHOP 67, INTC 62, PLTR 43, MSTR 25, **COIN 4.**

Five names are 13.2% of the *loaded* sample and produce 26.1% of signals — roughly **2.0×
over-representation.** Taken at face value that is not the failure case. **It cannot be
taken at face value**, because the denominator is wrong and the seven absent names are the
ones the test exists to examine.

*What I wrongly concluded, and why it was wrong:* the low counts on COIN (4), MSTR (25)
and PLTR (43) initially looked like evidence that the hindsight-suspect names contribute
little, making survivorship a smaller problem than the audit assumed. **That inference is
invalid.** The names that would most inflate a 2019–2026 backtest chosen in 2026 are NVDA,
META, TSLA, AVGO and AMD — and all five were missing from this run. Their absence, not
their unimportance, is why they do not appear. **F-01 remains fully open.**

*Uncomfortable for the thesis:* the names that do fire are **AAPL, COST, MSFT, NFLX,
LLY** — large, liquid, trending mega-caps. A system whose signals concentrate there is
close in character to owning the mega-cap index.

> **The benchmark is therefore not zero, and not cash. It is buy-and-hold of the names the
> system actually trades.** Beating zero is not evidence of skill when the signal set is
> "long quality mega-caps in a bull regime."

**Important limitation.** This gate measures **signal counts, not profit contribution.**
A handful of trades in one name can dominate P&L while contributing few signals. The
question "is the *P&L* secretly four stocks?" is **not answered by this run** and requires
`--mode sim`.

## 3 · The finding that was not on the checklist — the dual engine is not dual

**Engine 1 (mean reversion): 324 signals. Engine 2 (trend): 3,000 signals. A ratio of
9.3 : 1.**

Engine 1 generates **9.7% of all signals.** The system is documented, reasoned about and
maintained as a two-engine design; in practice it is a trend system with a rounding error
attached.

This matters for three reasons:

1. **Complexity without contribution.** Engine 1 carries its own thresholds, its own stop
   logic, its own cooldown, and its own share of the 21 hand-tuned parameters — for under
   a tenth of the signals. Every one of those parameters is a degree of freedom that
   inflates overfitting risk while buying almost nothing.
2. **It may be mis-calibrated rather than genuinely rare.** A mean-reversion engine that
   fires 324 times in seven years across 38 names is firing roughly **once per name per
   1.6 years.** That is either a deliberately extreme filter or a threshold set too tight
   to trigger. **Which one it is has never been checked**, because nobody had counted.
3. **The regime gate probably explains part of it.** If Engine 1 is restricted to
   non-bull conditions and the sample is ~80% bull, its opportunity set is structurally
   about a fifth of Engine 2's. That is a design consequence, not a bug — but it means
   **the mean-reversion engine is almost untested**, and it is the engine that would carry
   the system through the market conditions the sample barely contains.

**This is now the highest-value question about the strategy itself**, and unlike the other
open items it costs nothing to investigate — the data is already downloaded.

## 4 · What this changes about the upgrade path

Previously the ordering was: run the diagnostic → decide on point-in-time data → build
walk-forward. The diagnostic has now run, and it re-orders the queue.

| Priority | Action | Cost | Why now |
|---|---|---|---|
| **0** | **Re-run the diagnostic with all 38 tickers** | free, ~5 min | Everything downstream inherits the sample. Retry logic now added. |
| **1** | **`--mode compare` on real data** | free, ~5 min | Net EV per broker on real prices. Until this is known, nothing else is worth deciding. |
| **2** | **Diagnose Engine 1's 9.7% share** | free | Deliberate filter or dead code path? Changes what "the model" even is. |
| **3** | Establish the right benchmark | free | Against buy-and-hold of AAPL/MSFT/COST/NFLX/LLY, not against zero. |
| **4** | Walk-forward with 2022 held out | session budget | The one genuine bear year must be out-of-sample. |
| 5 | Point-in-time universe | ~US$50–150/mo | **Unchanged in priority.** The evidence that would have downgraded it turned out to be an artifact of missing data. Still gated on a clean run plus `--mode sim` P&L attribution. |

**Point-in-time data has not moved.** I briefly concluded it could be downgraded; that
rested on the missing-data artifact and does not survive. Tom's sequencing argument — run
the free diagnostic before spending — still holds, and this episode is an argument for it:
the free run caught a defect that would otherwise have corrupted a paid one.

## 5 · What is still unknown

0. **The signal distribution across the full 38-name universe.** Voided by the data gap.
1. **Net EV after costs on real data.** The synthetic self-test showed a **5.050pp
   per-trade spread between a free broker and a Hong Kong retail broker**. On real data
   this number decides everything, and it has not been measured.
2. **P&L attribution by ticker.** Signal counts are spread; profits may not be.
3. **Drawdown behaviour outside 2022.** One bear year is not a distribution.
4. **Whether Engine 1 works at all.** 324 signals is enough to look at, not enough to
   conclude from.
5. **The V6.4 line numbers.** All four V6.4 Python files still fail to parse from the
   PDFs; the real `.py` and `.pine` files have not been received. Structural findings
   survive; specific line references do not.

---

## Verdict

**RE-RUN FIRST, then proceed.**

One abandon gate was passed marginally; the other could not be evaluated. The strategy is not disqualified. But the
run has changed what the open question is: it is no longer "is the universe rigged" — it is
**"does a trend system on mega-caps beat holding those same mega-caps, after real costs, in
a sample containing one bear market?"**

That question is answerable, and the next step toward it is free.

*Research and decision support. Not financial advice. No performance figure in this note is
a return — the diagnostic reports sample composition only, and no trade was simulated
against real prices in this run.*

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
