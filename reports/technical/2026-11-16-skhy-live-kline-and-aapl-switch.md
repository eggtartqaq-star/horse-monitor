# SKHY — live K-line statistics, the AAPL→SKHY switch, intrinsic value and entry point

**皮褸黃 (CEO) · 2026-11-16 · data to the 13 Nov 2026 close**
**Chart:** `reports/technical/2026-11-16-skhy-kline.png`

> **First report in this firm built on primary market data.** Every price statistic below is
> computed from daily OHLCV bars pulled read-only from the Owner's Webull connector (amended
> rule 1): **SKHY 90 bars — its entire listing life, 10 Jul → 13 Nov 2026 — and AAPL, SPY, SOXX
> 260 bars each.** All four series were parsed in full by script; none was summarised by eye.
> No search extraction, no vendor screen.

## 0. Corrections to the firm's own files from the primary data

| Item | Firm file said | Primary bars say | Consequence |
|---|---|---|---|
| All-time high | $194.80, 14 Jul (technicals §1) | **$199.87, 9 Sep 2026** | Full-range Fibonacci grid moves: 38.2% = **$151.87** (was $149.93); 50% = $161.03; 61.8% = $170.20 |
| 13 Nov close | $131.07 (sizing, tickets) | **$131.79** — $131.07 was a 19:50 UTC intraday print | All "+1.6%" figures become **+2.2%** |
| Reduce-1 upper bound | $149.9 | $151.87 on the corrected range | **Tickets unaffected** — T3 triggers at the lower bound, $146.80, which derives from the Oct–Nov swing and is unchanged |

## 1. Live statistics — SKHY's whole life vs AAPL over the same 90 sessions

| Statistic | **SKHY** | **AAPL** (same window) | AAPL (1 year) |
|---|---|---|---|
| Return over window | **−21.5%** | **+13.2%** | +33.0% |
| Annualised volatility | **101.2%** | 26.1% | 24.7% |
| Daily standard deviation | 6.38% | 1.64% | 1.55% |
| Sessions moving more than ±5% | **32.6%** — one in three | 2.2% | 1.2% |
| Sessions moving more than ±10% | 6.7% | 0% | 0% |
| Worst day | −13.7% (16 Jul) | −7.4% (31 Jul) | — |
| Best day | +27.3% (14 Jul) | +5.3% (4 Nov) | — |
| Max drawdown (close basis) | **−37.6%** | −11.1% | −13.8% |
| Current drawdown from peak close | **−33.6%** | 0% — **at an all-time high** | — |
| 1-day 95% VaR / CVaR | −9.0% / −10.9% | −1.9% / −3.3% | — |
| Skew / excess kurtosis | **+1.06** / 3.40 | −0.50 / 4.87 | — |
| Beta to SPY | **3.21** | 0.38 | — |
| Beta to SOXX (semis) | 1.45 | — | — |
| Correlation with SPY / SOXX | 0.45 / **0.76** | 0.20 | — |
| **Correlation SKHY ↔ AAPL** | **−0.21** | | |

**Reading the distribution.** SKHY is a semiconductor-beta instrument (0.76 correlation with SOXX, 1.45 beta) carrying three times the market's beta. Its returns are **positively skewed** — the big days are disproportionately up days (+27.3% on 14 Jul) — which is why it can fall 34% from its peak while consensus still points to doubling. Apple over the same window is a low-beta, slightly negatively skewed large cap that has **moved against SKHY on average**.

## 2. Listing-life statistics

| | |
|---|---|
| Sessions traded | 90 |
| Sessions closed above the $149 IPO price | 61 (67.8%) |
| Last close above IPO | 3 Nov 2026 — **none in the 8 sessions since** |
| Sessions closed at or below today's $131.79 | **7 (7.8%)** — today sits in the bottom decile of the instrument's whole life |
| Sessions closed below the Owner's $129 cost | 3 |
| Longest up streak / down streak | 5 / **10** sessions |

## 3. K-line read

**Trend — down, on every measure available.** Full bearish moving-average stack: MA5 $135.16 < MA10 $136.86 < MA20 $141.36 < MA50 $164.00. Price is **−6.8% below MA20 and −19.6% below MA50**, and both are falling (−2.5% and −1.7% over five sessions). There is no MA200; the instrument has not existed for 200 sessions.

**Structure — lower highs, lower lows.** Pivot highs: $199.87 (9 Sep) → $196.48 → $195.97 → $166.06 (28 Oct) → **$145.79 (11 Nov)**. Pivot lows: $136.23 → $130.79 → **$122.20 (5 Nov)**. The 11 Nov rally — +9.7% on the CoreWeave print — **failed at $145.79, one dollar below the Reduce-1 zone**, closing at 57% of its range with a 43% upper wick. That is a rejection, not a breakout.

**The last ten candles.**

| Date | O | H | L | C | Δ | Close in range | Vol (M) | Read |
|---|---|---|---|---|---|---|---|---|
| 5 Nov | 133.28 | 134.07 | **122.20** | 123.90 | **−13.4%** | 14% | **52.9** | Capitulation-type bar: widest body, heaviest volume of the window, closed near the low |
| 6 Nov | 129.12 | 133.45 | 124.83 | 127.34 | +2.8% | 29% | 28.0 | Gap-up faded — 50% upper wick |
| 9 Nov | 126.86 | 135.60 | 125.83 | 134.38 | +5.5% | **88%** | 23.1 | Strongest bar of the bounce; closed near the high |
| 10 Nov | 131.00 | 135.15 | 127.38 | 129.66 | −3.5% | 29% | 15.8 | Rejected, 53% upper wick |
| 11 Nov | 139.62 | **145.79** | 137.49 | 142.25 | +9.7% | 57% | 20.9 | Gap-up on CoreWeave; failed below Reduce-1 |
| 12 Nov | 134.25 | 139.56 | 134.04 | 137.71 | −3.2% | 66% | 15.2 | Gap-down, recovered intraday |
| 13 Nov | 133.97 | 135.76 | 129.18 | 131.79 | −4.3% | 40% | 16.4 | Lower high, lower low |

**Momentum.** RSI(14) **41.6** — neutral-bearish, not oversold. MACD −7.69 crossed above its signal (−7.81) from deep negative territory, but the histogram is already shrinking (+0.22 → +0.12): **the bullish cross is fading on its second day.**

**Volatility and volume.** Bollinger width **29.7%** — an extreme-volatility regime; %b 0.27, in the lower third. ATR(14) **$10.10, 7.66% of price.** 20-day volume is 0.86× the instrument's average and up/down volume is balanced at 0.96: **no accumulation signal.** The 5 Nov bar is the only high-volume event, and it was a down day.

**The finding that matters most for the plan.** The Bollinger lower band sits at **$120.34** — one cent from 老詹's stop at $120.35. The stop is **1.13 ATR below the close**. On this instrument that is roughly one ordinary day's range. The stop is correctly placed at a genuine confluence, and it is also very likely to be tested.

## 4. The switch: sell AAPL, buy SKHY — opportunity cost per $1,000

**The Owner's AAPL position is not in the Webull account** (read 16 Nov: 2 AVGO only). Size, cost basis and broker are NOT DISCLOSED. Everything is per $1,000 switched.

### 4.1 Friction — firm cost model (`strategy/v6.5/risk_config.py`; its own header labels the commissions illustrative)

| Broker model | One AAPL sell + one SKHY buy |
|---|---|
| hk_retail (Futu-type) | **$6.50 — 0.65%** |
| ibkr_fixed | $3.90 — 0.39% |
| ibkr_tiered | $2.60 — 0.26% |

Plus whole-share residue: $1,000 buys **7 SKHY ($922.53), leaving $77.47 idle.** Dividend yield foregone: AAPL 0.30% vs SKHY 0.02% — **~$2.84 a year per $1,000**, before withholding. Capital-gains tax on the AAPL sale depends on the Owner's tax residency and cost basis, both NOT DISCLOSED.

### 4.2 Risk added — this is the real cost

| Per $1,000 | Keep AAPL | Switch to SKHY | Change |
|---|---|---|---|
| Annualised volatility | $261 | **$1,012** | **3.9×** |
| 1-day 95% VaR | $19 | **$90** | +$71 |
| 1-day 95% CVaR (average bad day) | $33 | **$109** | +$76 |
| Max drawdown in this window | $111 | **$376** | +$265 |
| Structural premium-to-parity risk | $0 | **$300–340** | new; no stop protects it |

**And the diversification you give up.** Over SKHY's life the two moved **against** each other (correlation −0.21). If the Owner holds both, Apple is the position that cushions SKHY's bad days. Selling it to buy more SKHY removes the hedge and doubles the concentration in one trade.

### 4.3 Return — this depends entirely on whose valuation you believe

| | AAPL | SKHY | Switch, per $1,000 |
|---|---|---|---|
| **Firm valuation** (𢦀鳩仔) | **none — the firm has never valued AAPL** | $102.40 central → **−22.3%** | **−$223** on the SKHY leg alone (range −$439 to −$21; at parity −$393) |
| **Analyst consensus** (Webull, sentiment proxy) | mean $346.37 → **−2.8%** (45 analysts; 26 buy, 13 hold, 6 sell) | mean $259.50 → **+96.9%** (15 analysts; 14 buy, 1 hold) | **+$997** |

**The two are a thousand dollars apart per $1,000, in opposite directions.** The difference is the ADS premium. The firm values the Korean business, then prices the 43–52% premium separately as a regulatory artefact that can disappear. The consensus targets do not separate it; 修大哥 found the aggregates had not absorbed the 9 Nov Morgan Stanley cut; and **even the lowest analyst target ($164) is above the firm's best case with the premium fully intact ($145).** Consensus is a statement about analysts, not the asset. The firm's decisions run on its own valuation.

### 4.4 The constraint that decides it before the arithmetic does

**Buying SKHY with Apple proceeds is an add to SKHY. John vetoed adds on 12 Nov**, on the instrument rather than the chart, and capped the position at 3% of liquid net worth. A veto is escalated to the Owner, not overridden. Under the firm's rules this switch is not available without a committee and a re-run CRO review.

A behavioural note, offered once: this is a rotation **out of a stock at its all-time high into one 34% below its peak**. That can be good mean-reversion investing. It can also be paying for a winner's strength with a position the firm values below its price. The arithmetic above is how to tell which.

## 5. Intrinsic value — SK hynix only

From `reports/equity/2026-11-12-skhy-valuation.md` (𢦀鳩仔), audited 13 Nov (C3: PASS WITH FLAGS):

| | Low | **Central** | High |
|---|---|---|---|
| Ordinary 000660.KS (KRW) | ₩900,000 | **₩1,070,000** | ₩1,250,000 |
| **ADS at parity** — if the KSD cap is lifted | $67 | **$80** | $94 |
| ADS if the cap persists (×1.40) | $77 | **$112** | $145 |
| **ADS probability-weighted** (30% chance the cap lifts within 12m) | $74 | **$102** | $129 |

## 6. Entry point

| Basis | Price | From $131.79 |
|---|---|---|
| **Value entry — 40% margin of safety on $102.40** | **$61.44** | **−53.4%** |
| Fair value, 0% margin of safety | $102.40 | −22.3% |
| 40% MoS on parity $80 | $48.00 | −63.6% |
| All-time low | $122.20 | −7.3% |
| Technical add zone (老詹) — **VETOED by CRO** | $127.3–130.0 | price is in it now |

**There is no entry at today's price under the firm's rules.** The chart's add zone is exactly where the price sits, which is why it is tempting, and exactly why the veto was written on the instrument rather than the chart. The value entry is **$61** — below anything this instrument has traded at.

**Two caveats the audit requires.** The 40% margin of safety is the valuation desk's judgement; **no written firm rule sets it** (audit C3). And the audit found the margin of safety **negative even at 0% required** — so it is the price, not the hurdle, that blocks entry.

## NOT OBTAINED

1. Owner's AAPL position: size, cost basis, broker, purchase date. No decision record exists.
2. Owner's tax residency — governs capital-gains tax on the AAPL sale and dividend withholding.
3. The actual commission schedule of the broker holding AAPL and SKHY.
4. 000660.KS close and USD/KRW for 13 Nov — the ADS premium at $131.79 cannot be computed.
5. A firm valuation of AAPL. AAPL is in the `technology` sleeve and has never been analysed.

*Research and decision support, not financial advice. No order has been or will be placed by any
agent of this firm. All price statistics are from primary bars; valuation figures from the audited
valuation report.*

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
