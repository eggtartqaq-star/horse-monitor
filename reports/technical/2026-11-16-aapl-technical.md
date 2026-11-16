# AAPL — technicals and statistics for an existing position

> **CORRECTED 2026-11-16 after audit** (`reports/committee/2026-11-16-aapl-skhy-reentry-audit.md` §2).
> T1: the 3–4 Nov gap is partly filled. T2: "no technical sign of a top" contradicted §3. T3: volume
> claim now uses averages. T4: "seven monthly rises" was wrong — June was a down month. T6, T7 reworded.
> T8: the CRO has turned the $325.08 review into a binding exit; 老詹 to confirm by 21 Nov.

**皮褸黃 (CEO), standing in for 老詹 · 2026-11-16 · Webull read-only daily bars, 3 Nov 2025 → 13 Nov 2026 (260 sessions)**

> **Why the CEO wrote this.** The technical desk's job here is mechanical: compute levels from the
> bars. The bars were already on disk from the SKHY switch analysis (`2026-11-16-skhy-live-kline-and-aapl-switch.md`),
> so dispatching an agent would have re-fetched the same data. **No 老詹 sign-off.** The audit should
> treat this as a CEO product and check it the same way.

## 0. Position context

| | |
|---|---|
| Owner's cost | **$357.60** (disclosed 16 Nov; size and broker NOT DISCLOSED) |
| Close 13 Nov | **$356.27** — **−0.37%** vs cost |
| All-time high | **$360.83**, intraday 13 Nov |
| 52-week low | $242.57, 20 Jan 2026 |
| 12-month return | **+33.0%** |

The Owner bought at the top of a 47% run from the January low. That is a fact about timing, not
a reason to sell — cost basis is irrelevant to what the stock does next (L-003).

## 1. Statistics (12 months)

| Measure | AAPL | For comparison: SKHY |
|---|---|---|
| Annualised volatility | **24.7%** (20d 27.9%, 60d 22.2%) | 101% |
| Daily 95% VaR / CVaR | −1.95% / −3.47% | −9.0% / −10.9% |
| Max drawdown (12m, on closes) | **−13.8%** | −37.6% |
| Days moving more than 5% | 1.2% | 32.6% |
| Worst / best day | −7.35% (31 Jul) / +5.31% (4 Nov) | −13.7% / +27.3% |
| Skew | −0.36 (down moves bigger than up) | +1.06 |
| ATR(14) | $8.21 (2.3%) | $10.10 (7.7%) |

**AAPL is a low-volatility large-cap with a mild downside skew.** Its single worst day in a
year was an earnings reaction (31 Jul, −7.4% on a weak guide). The next earnings report (late
January, date NOT OBTAINED) is the most likely source of a gap.

## 2. Trend

| Indicator | Reading | Read |
|---|---|---|
| vs MA20 ($345.91) | +3.0% | up |
| vs MA50 ($338.79) | +5.2% | up |
| vs MA200 ($300.77) | **+18.5%** | extended |
| MACD | 4.21 vs signal 3.29, histogram +0.92 | positive, rising |
| RSI(14) | 60.9 | firm, not overbought |
| Bollinger %b | **0.93** (upper band $357.92) | at the top of its range |

**Month-end closes (Webull bars, dividend-adjusted):** Mar $253.15 · Apr $270.66 · May $311.55 ·
**Jun $288.89 (down)** · Jul $308.41 · Aug $316.61 · Sep $332.77 · Oct $344.37 · Nov $356.27
(month to date, 13 Nov). Five consecutive higher closes since June. *(The first version said
"seven months straight"; June broke the run.)*
Primary trend is up; the only caution signs are the volume divergence and the extension in §3.

## 3. The two things the chart warns about

1. **The new high came on below-average volume.** 13 Nov's all-time high traded 40.0m shares,
   against a 20-day average of 47.2m and a 50-day average of 43.5m (4 Nov, the midterm-rally day,
   traded 89.6m). Over the last 20 sessions volume on down days exceeded volume on up days (ratio
   0.67; 0.75 excluding the 3 Nov post-earnings session, an event day). A mild caution, not a sell
   signal.
2. **The stock is 18.5% above its 200-day average** with %b at 0.93. Extensions like this are
   usually worked off by time or a pullback. Neither has started.

**And one structural feature:** 3 Nov gapped down to $325.08–334.25; 4 Nov gapped up above it,
leaving a gap between $334.25 and $340.73. **The 6 Nov low of $338.04 partly filled it; the unfilled
remainder is $334.25–338.04.** Unfilled gaps tend to act as magnets on a pullback, which places a
plausible retest zone at **$334–339**, with the 50-day average ($338.79) at its top.

## 4. Levels

| Level | Price | vs cost $357.60 | Basis |
|---|---|---|---|
| Resistance | **$360.83** | +0.9% | All-time high; no overhead supply above it |
| First support | **$338.04** | −5.5% | 6 Nov swing low, ≈ MA50 |
| Gap zone | **$334.25–338.04** | −5.5% to −6.5% | Unfilled remainder of the 3–4 Nov gap |
| **Structure** | **$325.08** | **−9.1%** | 3 Nov low. A daily close below it breaks the higher-low sequence since September |
| Deeper | $308.91 | −13.6% | 31 Jul close as reported by 修大哥, unadjusted (Webull adjusted: $308.41) |
| Trend floor | ≈$300.77 (rising) | −15.9% | MA200 |

## 5. How likely is a pullback? (model, not forecast)

Probability of **touching** each level at least once from $356.27, under a driftless random walk
at constant realised volatility — the same model as the SKHY re-entry report. It ignores drift,
mean reversion and earnings gaps.

| Level | 1 month (20d vol) | 3 months (60d vol) | 6 months (12m vol) |
|---|---|---|---|
| $340 | 56% | 67% | 79% |
| $330 | 34% | 49% | 66% |
| **$325 structure** | 25% | 41% | 60% |
| $308.91 | 8% | 20% | 41% |
| $290 | 1% | 6% | 24% |

($325 computed directly: 25% / 41% / 60%. The 6-month column includes a January earnings report. At
AAPL's volatility the drift assumption barely matters: a zero-expected-change model adds 1–3 points per cell.)

**Read:** a return to the $334–341 gap within three months is more likely than not on this model.
That is ordinary noise for a 25%-vol stock, not a thesis event.

**Beta note.** The 0.38 beta to SPY in the 16 Nov switch report is a 90-session estimate with
R² ≈ 4% — a short-window statistic, not a long-run beta. The valuation uses the 5-year 1.09.

## 6. Technical guidance for the holder (for the CRO, not an order)

- **Hold signal intact** while daily closes stay above **$325.08**.
- **Superseded by the CRO:** a daily close below $325.08 is now a **full exit at the next open**
  (`reports/risk/2026-11-16-aapl-and-skhy-reentry-cro.md`), pending 老詹's confirmation by 21 Nov.
- **Do not add on strength into $360.** At %b 0.93 and +18.5% over the 200-day, an add here is
  chasing. Valuation does not support an add (ADD only ≤ ~$158); the CRO bars adds above $245.
- **Earnings:** late-January report. The last two reactions were −7.4% (31 Jul) and about
  −4% during the 2 Nov call before a recovery.

## NOT OBTAINED

1. Intraday and options-flow data (王老吉) and liquidity analysis (Tim Cook) — not run.
2. Next earnings date.
3. Bars after 13 Nov.
4. Adjusted vs unadjusted status of Webull's bars (13 Nov close matches the snapshot; earlier
   bars appear dividend-adjusted, e.g. 4 Nov $349.24 here vs $349.51 reported by 修大哥).

*Research and decision support, not financial advice. No agent of this firm places orders.*

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
