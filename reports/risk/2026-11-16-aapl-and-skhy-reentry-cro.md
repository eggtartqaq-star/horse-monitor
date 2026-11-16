# CRO Rulings — AAPL (existing position) and SKHY re-entry
**John, Chief Risk Officer (Dept 6) · 2026-11-16 · binding reference: config/risk-limits.yaml**

## 0. Sources and data status

**Binding:** `config/risk-limits.yaml` (read 16 Nov; unchanged since 12 Nov). `config/portfolio.yaml` (read 16 Nov: `holdings: []`, `cash_balance: 0.00`, so it is still empty).
**My prior rulings:** `reports/risk/2026-11-12-skhy-cro-review.md` (SKHY: hold approved at ≤3.0% of LNW, add vetoed, score 32/100). Zac's `reports/portfolio/2026-11-13-skhy-sizing.md`.
**AAPL, all dated 2026-11-16:** valuation (𢦀鳩仔), financials (巴爺爺), moat (菲比斯), management (Peter), news (修大哥), regulatory (The dictator), industry (Elon Musk), technical (CEO standing in for 老詹, with **no technical-desk sign-off**).
**SKHY:** `reports/technical/2026-11-16-skhy-reentry.md` (CEO, read in full) and `reports/technical/2026-11-16-skhy-live-kline-and-aapl-switch.md` (CEO; primary Webull bars; source of the −0.21 correlation).
**Firm:** `knowledge/investment-philosophy.md` ("Survival first … the limits are the constitution"). `memory/decisions/2026-11-13-skhy-retrospective.md`.

**Labels used below.** [C] config file · [R:desk] a dated firm report · [D] derived, meaning my arithmetic on cited inputs (formula shown) · [A] assumption, stated as such. I made no web fetches for this review. Every market figure comes from the reports above. tradingkey.com was not used.

**What I could not do.** Mo Peter (VaR) and Mario (stress) were **not commissioned**, because this session cannot dispatch agents. Position-level VaR comes from the CEO's computation on primary bars. I run the stress scenarios myself in A.3 and B.2, and both are labelled as such. Portfolio VaR is undefined while the portfolio file is empty. This is the **ninth** empty-portfolio escalation (eighth: SKHY, 12 Nov).

**Price references.** AAPL $356.27 (close 13 Nov, Webull) · cost $357.60 · ATH $360.83 (13 Nov). SKHY $131.79 (close 13 Nov, primary bars) · exit $137.00 · 000660.KS ₩1.21–1.30m (last available, 10–11 Nov) · USD/KRW 1,350–1,380 [A], as used on 12 Nov. No dated 13 Nov rate is on disk.


## RULING A — AAPL existing position
### A.1 Verdict

| Decision in front of the Owner | Verdict |
|---|---|
| **Hold AAPL, if it is ≤ 6.4% of liquid net worth (LNW) at market** | **APPROVED WITH CONDITIONS.** The binding conditions are A-1 to A-9 (consolidated section). The load-bearing one is a **hard stop**: a daily close below $325.08 means a full exit at the next open. Without the stop, the approval lapses and the cap falls to 2.4% (A.3). |
| **Hold above 6.4% and up to 10%** | **TRIM to ≤ 6.4%.** This is inside `max_single_position` but over `max_risk_per_trade` once a gap through the stop is counted. Deadline: **20 Jan 2027**, or 5 sessions before the FQ1-27 report, whichever is earlier. The Owner may use strength before that (A.4). |
| **Hold above 10%** | **BREACH of `max_single_position` (0.10 at cost).** Reduce to ≤ 10% **in the next session, not at a level**. Then reduce to ≤ 6.4% by the same pre-earnings deadline. This is escalated to the CEO and the Owner. The 15% "drifted" trigger **does not apply**: AAPL is −0.37% vs cost, so it did not grow into its size. It was bought at that size. |
| **Add** | **VETOED** at any price above $245, the top of 𢦀鳩仔's fair-value range. No committee has convened and no decision record exists. The firm's add level is ≤ ~$158. |
| **Exit in full** | **Permitted at any time**; risk has no objection. It is not *required* by any limit at ≤ 6.4%. Whether to exit on valuation is the committee's call, not mine: upside is not my department. |

**One-paragraph reasoning.** AAPL is the mirror image of SKHY. SKHY was a sound business inside an instrument with an unstoppable risk, the ADS premium. AAPL is a clean instrument (25% vol, deepest liquidity, no basis) priced 70% above the firm's central value. Its valuation risk is large (−31% to −41% to the fair-value range, A.3) but **slow and path-dependent**, so a stop can intercept it. Its volatility is low enough that a stop 8.75% away is a real loss-stop, not a coin-flip: the worst day in a year was −7.35%. So the stop does the work. The cap is set by sizing for the stop being breached on a worst-day earnings gap: 1% ÷ 15.46% = **6.4% of LNW**. Valuation lowers conviction and raises the cost of not honouring the stop. It does not, by itself, threaten survival at ≤ 6.4%, so it does not set the cap.

**Risk score: 57 / 100** (A.9). That is above the ~40 initiation line, so this is not a risk veto at ≤ 6.4%. The score rates survivability, not attractiveness; 𢦀鳩仔's valuation score is 28/100 on its own axis.

### A.2 Limit-by-limit check (AAPL)

Position size and LNW are **NOT DISCLOSED**, so ratio limits are shown per % of LNW held. The "at 6.4%" column is the post-ruling state.

| # | Limit [C] | Value | Current (actual) | At the 6.4% cap / per 1% held | Pass / Fail |
|---|---|---|---|---|---|
| 1 | `max_single_position` (at cost) | 0.10 | unknown | 6.4% < 10%. Cost ≈ market (−0.37%), so at-cost and at-market agree | **NOT COMPUTABLE** · PASS at ≤ 10% · **BREACH if > 10%** |
| 2 | `max_single_position_drifted` | 0.15 | unknown | Not applicable: the position has not drifted (−0.37%). If AAPL rises, the stop rule in A.4 trims well before 15% | n/a |
| 3 | `max_sector` (GICS Info Tech) | 0.35 | unknown | AAPL is Tech Hardware. AVGO, 2 shares at Webull (13 Nov pull, Zac §1.6), is also Info Tech. Index ETFs, if held, add look-through AAPL weight | **NOT COMPUTABLE** |
| 4 | `max_correlated_cluster` (AI complex) | 0.40 | unknown | AAPL is **not** an AI-capex beneficiary. It rents its model (Gemini) and AI is a cost on its P&L [R:Elon Musk §summary]. Beta to SPY is 0.38 over 90 sessions [R:CEO switch §1]. I count it **outside** the AI-capex cluster | NOT COMPUTABLE · AAPL not counted |
| 5 | `cash_floor` | 0.10 | `cash_balance: 0.00` placeholder | — | **NOT COMPUTABLE** |
| 6 | `leverage` | none | **Webull: individual MARGIN account, USD cash −$12.06** (13 Nov, Zac §1.6). AAPL account type unknown | See A.6. A negative USD balance in a margin account is, on its face, borrowed money | **FAIL ON FACE (Webull) · AAPL UNVERIFIED** → escalated |
| 7 | `max_var_95_1d` | 0.03 | portfolio VaR undefined (empty file) | Name VaR −1.95%/day [R:CEO tech §1]. At 6.4%: **0.12% of LNW**; at 15%: 0.29% | PASS at any size ≤ 15% (single-name) · portfolio NOT COMPUTABLE |
| 8 | `max_drawdown` budget | 0.20 | no series | Contribution at 6.4%: stop-tail 0.99%, reversion to $245 2.0%, to $210 2.6%, bear DCF $119 4.3% [D] (table A.3) | PASS at 6.4% · portfolio NOT COMPUTABLE |
| 9 | `max_risk_per_trade` | 0.01 | n/a | Stop by trade 8.75% → 11.4% (capped at 10% by #1). Expected loss given the stop is hit, 10.4% → 9.6%. **Gap-through tail 15.46% → 6.4%** ← binding | **FAIL above 6.4% · PASS at ≤ 6.4%** |
| 10 | `stop_required` | true | CEO "review trigger" at $325.08. **No 老詹 sign-off; not a stop** | Amended to a binding close-basis exit (A.5) | **FAIL as received** → PASS once A-2 is adopted |
| 11 | `max_adv_participation` | 0.05 | not run (Tim Cook) | Volume 40.0m shares on 13 Nov [R:CEO tech §3]. A retail position cannot approach 5% of that | PASS on inference · not formally checked |
| 12 | options limits | — | none | — | n/a |
| 13 | `committee_approval_required` | true | never convened on AAPL | Holding is not a new decision. An add is blocked. A trim to restore a limit needs no committee; it is a limit action | n/a for hold/trim · **FAIL for any add** |
| 14 | `decision_record_before_ticket` | true | **none**: bought outside the process | Retrospective record required (A-8) | **FAIL (retrospective)** |
| 15 | `live_trading` | forbidden | no agent places orders | — | PASS |

**Binding:** #9 at **6.4%**, and #1 at **10%** as the hard ceiling. **Failed on receipt:** #6 (Webull), #10, and #14.

### A.3 Valuation risk vs volatility risk: how risk weighs a 70%-overvalued, 25%-vol mega-cap

They are two different risks, and I hold them on different instruments.

| | Volatility risk | Valuation risk |
|---|---|---|
| What it is | the **speed and path** of a loss | the **size** of the loss if price reverts to value |
| AAPL evidence | ann. vol 24.7%, daily σ 1.55%, worst day −7.35% (31 Jul, earnings), 95% VaR −1.95%, 12m max DD −13.8%, ATR $8.21 = 2.3% [R:CEO tech §1] | to $320 steel-man −10.2% · to $295 −17.2% · to $245 (top of FV) **−31.2%** · to $210 (central) **−41.1%** · to $185 −48.1% · bear DCF $119 −66.6% [D from R:𢦀鳩仔 §1, §10] |
| How it arrives | daily noise and an earnings gap | **de-rating over quarters**: the reverse DCF needs ~15%/yr growth for 10 years against a 6.9% 5-yr NI CAGR [R:𢦀鳩仔 §4]. There is no solvency tail (net cash ~$56bn per 𢦀鳩仔 §12; FCF ≈ NI) |
| Can a stop intercept it? | **Yes.** The stop is 8.75% away, which is 5.6 daily σ and larger than the worst day in a year | **Yes, because it is path-dependent.** A −31% to −41% reversion passes through $325.08 on the way |

**The ruling in one line: the stop turns a −41% valuation risk into a −9% to −15% realised loss. That makes the stop non-negotiable, and makes valuation a conviction input rather than a cap input.**

Three consequences:

1. **Low volatility is not low risk here.** The 12-month max drawdown (−13.8%) was sampled in a year when the stock rose 33% and the multiple expanded. It is a sample from a *re-rating*, not the drawdown distribution of a *de-rating*. A move from ~40x to the 30x base exit multiple with flat earnings is −25% on its own (40→30, [D] from 𢦀鳩仔 §11). I do not use the 12m drawdown as a sizing input. A historical mega-cap de-rating precedent was **NOT OBTAINED**, and I will not quote one from memory.
2. **The price of refusing the stop.** If the Owner holds through $325.08, the loss the 1% budget must absorb is the reversion, not the stop. Held-through caps: to $245 → 1% ÷ 31.2% = **3.2%**; to $210 → **2.4%**; to bear $119 → 1.5% [D]. **If the Owner declines Condition A-2, the cap is 2.4%, not 6.4%.** This is the same construction as SKHY's 3%, applied to the risk that has no stop.
3. **Valuation sets conviction, and conviction is Zac's lever inside my cap.** Valuation 28/100 is below the ~40 line on Zac's method (13 Nov). His conviction rule would put a below-40 idea at half the cap, ~3.2%. I record that as a **recommendation for Zac and the committee, not a CRO condition**. The base expected return of ~4%/yr (−1.5% to +8.4%) is below the 5.15% 10-year Treasury [R:𢦀鳩仔 §11]. That says the Owner is being paid less than the risk-free rate to carry a −41% reversion risk. It is a return argument, and it belongs to the committee. It is not a limit, and I do not convert it into one.

**Stress table (my scenarios; Mario not commissioned): loss as % of LNW by size held**

| Scenario | Name move from $356.27 | at 6.4% | at 10% | at 15% | at 20% |
|---|---|---|---|---|---|
| Stop fills near level | −8.75% | 0.56% | 0.88% | 1.31% | 1.75% |
| **Gap-through stop (worst-day tail)** | **−15.46%** | **0.99%** | 1.55% | 2.32% | 3.09% |
| Held through, to $245 | −31.2% | 2.00% | 3.12% | 4.68% | 6.25% |
| Held through, to $210 | −41.1% | 2.63% | 4.11% | 6.16% | 8.21% |
| Held through, bear DCF $119 | −66.6% | 4.26% | 6.66% | 9.99% | 13.32% |

*[D] = size × move. The bear row at 15% uses half the 20% drawdown budget on one name.*

### A.4 Concentration: the ruling as a function of AAPL's share of LNW

**How the 6.4% is derived.** The stop is a daily close below $325.08, executed at the next open (A.5). The worst realistic exit is a close that breaches the stop on a worst-day move from just above it: $325.08 × (1 − 0.0735) = **$301.19**. That is **−15.46% from $356.27** (−15.78% from cost) [D]. 1% ÷ 15.46% = **6.47%, rounded down to 6.4%**. For comparison: the expected loss if the stop is hit is −10.4%, using **assumed** weights of 0.6 for a fill near the level, 0.3 for a half-worst-day gap and 0.1 for a full worst-day gap. That gives a 9.6% ceiling. The trade stop alone gives 11.4%, capped to 10% [D]. The rule I apply on every position is **plan on the expected loss and size for the tail**.

*A note on method consistency.* On 12 Nov I sized SKHY's gap case as the worst day alone (13.4% → 7.5%). Here I use stop distance plus the worst day. That is stricter, and it is the method I will apply from now on. Re-run on SKHY, it would have given 1% ÷ (6.7% + 13.4%) ≈ 5.0%. That would not have changed the SKHY verdict, because the premium bound at 3.0%.

| AAPL as % of LNW at market | Status | Ruling | Timing |
|---|---|---|---|
| **≤ 3.2%** | inside every construction, including held-through to $245 | **HOLD with conditions A-1 to A-9.** This is the conviction-scaled size (A.3 item 3) | — |
| **3.2% – 6.4%** | inside the risk budget **with** the stop; outside it without | **HOLD with conditions.** The stop is mandatory at this size. Trimming toward ~3.2% is recommended (valuation/conviction) but not required | — |
| **6.4% – 10%** | over `max_risk_per_trade` on the gap tail | **TRIM to ≤ 6.4%.** Sell fraction = 1 − 6.4 ÷ position%. At 8%, sell 20%; at 10%, sell 36% | **by 20 Jan 2027**, or 5 sessions before the FQ1-27 date, whichever is earlier. Strength may be used before then (below) |
| **10% – 15%** | **BREACH** of `max_single_position` 0.10 at cost | **Reduce to ≤ 10% next session, not at a level** (sell 1 − 10 ÷ position%: at 12%, 17%; at 15%, 33%). **Then to ≤ 6.4%** by the pre-earnings deadline. Escalated | next session; then the deadline |
| **> 15%** | **BREACH**, and over the drifted ceiling as well | as above. At 20%: sell 50% next session, then 68% of the original position in total by the deadline [D: 1 − 6.4/20]. The bear row in A.3 then stops being theoretical (13% of LNW at 20%) | next session; then the deadline |

**Trims into strength (recommendation for the Owner, not orders).** The stop is fixed at $325.08 and the tail exit at $301.19. If AAPL rises, the *distance* to the stop grows, so the cap **shrinks**, unless 老詹 raises the stop to a new structural higher low. Re-test the cap at each price with **cap = 1% ÷ (1 − 301.19 ÷ price)**:

| AAPL price | Tail loss | Cap (% of LNW) |
|---|---|---|
| $356.27 (13 Nov) | 15.5% | 6.4% |
| **$360.83 (ATH)** | 16.5% | **6.0%** |
| $370 | 18.6% | 5.3% |
| $380 | 20.7% | 4.8% |
| $400 | 24.7% | 4.0% |

[D]. The excess over the cap at the then-price is the trim. 𢦀鳩仔's TRIM signal (> $245) and this mechanical rule point the same way. For a position in the 6.4–10% band, a resting limit sell at or above **$360.83** is a sensible way to meet the 20 Jan deadline, and it is the Owner's choice. If the price never gets there, the deadline still binds. **If 老詹 raises the stop**, the formula uses his new level, and the cap recovers.

**Why 10–15% is not a "drift tolerance" band.** The limits file allows 15% only for "a winner that grows past" 10%. AAPL at −0.37% has not grown; a position above 10% was *bought* above 10%. Reading the 15% line as permission would be bending the limit silently.

### A.5 Stop / invalidation: the CEO's $325.08 is AMENDED

**Accepted:** the **level**. $325.08 is the 3 Nov low. A daily close below it breaks the sequence of higher lows that has held since September [R:CEO tech §4]. It is 8.75% from the close and 9.1% from cost, which is 3.8 ATR, larger than any single day in the past year. It is a structural level, not an arbitrary percentage.

**Amended:** the **consequence**. The CEO wrote "review trigger … not an automatic sale; the decision then belongs to John against the valuation report." I make that decision now, in advance, so it is not made in the moment:

> **A-2. Daily close < $325.08 → exit the full AAPL position at the next session's open.** Close basis; no resting intraday stop order. No averaging down, no "wait for earnings", no re-entry above $245 without a committee. The level is never moved lower. It may be raised only by 老詹 to a new structural higher low.

**Why a full exit and not a review.** Against the valuation report there is nothing under the price until $245, which is 31% lower. The only thing that justifies holding at −70% MoS is quality plus an intact trend. When the trend breaks, the second leg is gone and the first does not need the stock to be held at $325. A "review" at that point would be a decision taken under a loss, which is what pre-registration exists to prevent. Upside after the exit is not my department. The valuation desk would not re-buy above $245 in any case.

**Whipsaw, stated honestly.** On the CEO's driftless model, the probability of *touching* ~$325 is ≈26% in 1 month, ≈41% in 3 months and ≈60% in 6 months. That is a touch, intraday; a close below is less likely [R:CEO tech §5, model not forecast]. The Owner should expect a material chance that this stop fires. I accept that: the cost is exiting a stock the firm values at $210 at $325.

**Alternative the Owner may elect (Option B, logged as the Owner's choice).** Sell half on a close below $325.08 and the remainder on a close below **$308.91** (the 31 Jul post-guide close [R:CEO tech §4]). Tail of the second leg: $308.91 × 0.9265 = $286.21, −19.7%. Blended tail −17.6% → **cap 5.6%** instead of 6.4% [D]. A wider stop buys a smaller position, not a free option.

**Provisional status.** `stop_required` says the level is 老詹's. The technical report is a CEO product with no technical-desk sign-off. **A-3: 老詹 confirms or replaces $325.08 within 5 sessions.** If he replaces it, the cap is recomputed with the A.4 formula using his level. Until then, $325.08 binds.

**Execution note for 死潘狗 and the Owner.** Because AAPL's ATR is 2.3% against SKHY's 7.7%, a resting stop is less hazardous here than it was on SKHY. I still require close-basis, so that the rule means what the level means (a broken structure) and is not a wick. The cost is the overnight gap, and that cost is already in the 6.4%.

### A.6 Margin / leverage

`leverage: none` is a **hard rule** [C]. The philosophy file repeats it: "No leverage".

**What is known.** The Owner's Webull account is an **individual MARGIN account, HKD base, carrying USD cash of −$12.06** (read-only pull, 13 Nov; Zac §1.6). It holds 2 AVGO, and AAPL is **not** in it (CEO switch §4, 16 Nov pull). The broker holding AAPL, and whether that account is cash or margin, is **NOT DISCLOSED**.

**Rulings.**
1. **The Webull −$12.06 is a `leverage: none` breach on its face.** It is trivially small, but a negative cash balance in a margin account is borrowed money by the account's mechanics. Whether the HKD side nets it to non-negative, and whether interest is charged, is NOT OBTAINED. **Escalated to the CEO and the Owner.** Remediation options: (a) deposit or convert HKD to bring USD cash to ≥ 0; (b) sell enough to clear the debit; (c) show a statement proving net cash ≥ 0 with no interest accrued. Any of the three closes it. Smallest-first is fine: this is a hygiene breach, not a solvency one.
2. **A-1 (AAPL): the approval to hold is conditional on the AAPL account carrying no debit balance and AAPL not securing any loan.** If AAPL sits in a margin account with a debit, the debit is leverage. It must be extinguished **in the next session**, before any other condition, by cash or by selling AAPL. A margin-*type* account with zero debit is compliant but not preferred. I recommend switching it to a cash account or disabling margin, so the rule is structural rather than behavioural (the same principle as CLAUDE.md rule 1).
3. **If AAPL is held on margin, the A.4 bands are measured on equity, not on gross position.** A 6% position financed half with debit is a 6% gross exposure on 3% of the Owner's own money, so the risk is doubled. I do not approve that structure at any size.

### A.7 Earnings gap risk (FQ1-27, late January; date NOT OBTAINED)

**Precedent (12 months, primary bars):** −7.35% on 31 Jul (FQ3 beat with a weak guide), the worst day of the year. About −3% after hours on 2 Nov (gross-margin guide of 45–46%, memory costs) before a recovery [R:CEO tech §6; R:修大哥 bottom line]. That is **two** relevant reactions. The sample is tiny; longer history was NOT OBTAINED.

**Why this print carries more gap risk than usual.**
- The December-quarter GM guide (45–46% vs 47.9%) is attributed to memory. Elon Musk calls the squeeze "not yet fully landed" and likely to persist into the March quarter as carry-in inventory fades [R:industry §2, §9].
- The stock enters the print **18.5% over its 200-day average at %b 0.93** [R:CEO tech §2].
- **The SKHY offset is gone (A.8).** The print most exposed to memory prices arrives with the Owner no longer long memory.
- Also in the window: the SCOTUS Apple v. Epic argument on **11 Jan 2027**, which is upside-skewed for Apple [R:The dictator §0]. Not a reduce-before event.

**The proximity line.** $325.08 ÷ (1 − 0.0735) = **$350.87** [D]. If AAPL's last close before the print is **below $350.87**, a precedent-sized reaction is enough to close below the stop. Today's $356.27 is only 1.5% above that line.

**Rulings.**
- **At ≤ 6.4%, the print is NOT a reduce-before event.** The cap was built on a worst-day gap through the stop, so the tail is budgeted at 0.99% of LNW.
- **A-5: any holding above 6.4% must be at ≤ 6.4% before the print.** The deadline is 20 Jan 2027, or 5 sessions before the announced date if that is earlier. This is the same date discipline as SKHY Condition 7.
- **A-6: no add in the 10 sessions before the print**, at any price. (Adds are vetoed anyway above $245.)
- **The stop is honoured after the print** at the next open, however large the gap. "It was only earnings" is not an exception.
- **Recommendation (not a condition):** if the last pre-print close is below $350.87 *and* the position is at the full 6.4%, consider sitting at ≈5% through the print. The tail budget assumes a precedent-sized gap, and a gap larger than the one-year worst day would overrun it slightly. For example, a −10% day from just above the stop is −17.9% from market, which costs 1.15% of LNW at 6.4% [D].

### A.8 Correlation and concentration, including the removed SKHY hedge

**Factor membership.** AAPL is a mega-cap quality and consumer-hardware name. It is **short memory prices**: it buys DRAM/NAND, and memory is named in its margin guide. Its beta to SPY is 0.38 and correlation with SPY 0.20 over 90 sessions [R:CEO switch §1]. It is **not** an AI-capex beneficiary, and I do not count it in the 0.40 AI cluster. It is a **top index weight**, so any SPY/QQQ holding (QQQ is on the watchlist) is look-through AAPL. That look-through is **NOT OBTAINED**, and it is the most likely hidden concentration in this book.

**The SKHY "hedge", sized honestly.**
- Correlation −0.21 over 90 sessions (SKHY's whole life) [R:CEO switch §1]. R² = **4.4%** [D]. On 90 observations the standard error is ≈ 0.105, so −0.21 is about two standard errors from zero: marginal [D, large-sample approximation].
- Minimum-variance hedge ratio = ρ × σ_AAPL ÷ σ_SKHY = −0.21 × 24.7/101 ≈ **−0.05** [D]. To hedge $1 of AAPL statistically took about 5 cents of SKHY.
- In the opposite direction, a 3% SKHY (101% vol) carried ~3.0 "vol-points" of risk, against ~1.6 for a 6.4% AAPL (24.7% vol) [D]. **SKHY was the larger risk in the pair, not AAPL's hedge.**
- The fundamental link is real: the same memory dollars sit on opposite sides of one contract [R:Elon Musk §2, §9]. But a narrative hedge with 4% explained variance is not a risk control.

**What it means for the AAPL ruling: nothing numerical.** I gave AAPL **no hedge credit**. The 6.4% comes from AAPL's own stop, so removing SKHY neither loosens nor tightens it. Exiting SKHY *reduced* the book's total risk, because SKHY's own variance dwarfed the 4% the correlation offset. The one qualitative effect is that the FQ1-27 print, the event most exposed to memory prices, is now un-offset (A.7). That supports sizing for the tail rather than changing the number.

**Sector.** AAPL (Tech Hardware) and AVGO (Semis) are both GICS Info Tech, and so are any SKHY/000660 re-entry and any QQQ. The 0.35 sector limit is **NOT COMPUTABLE** until `config/portfolio.yaml` is populated. The 0.40-vs-0.50 cluster/target contradiction still stands, unresolved (ninth time of asking). It does not bind on AAPL, which I place outside the AI cluster.

### A.9 Risk score: AAPL hold

*Convention, as on SKHY 12 Nov: higher = more acceptable. Calibration: BE 18, 3416 22, INTC 28, SKHY 32 (hold only). Below ~40 = CRO veto on initiation.*

| Component | Weight | Score | Note |
|---|---|---|---|
| Instrument structure | 30% | **90** | Common stock, Nasdaq, deepest liquidity in the market, no basis/premium, no conversion mechanics. (SKHY: 10.) Not 100: undisclosed broker/account type (A.6) |
| Stop quality vs volatility | 15% | **65** | Stop 8.75% away = 3.8 ATR, larger than the worst day. A real loss-stop. Penalised for a ~41% 3-month touch probability (whipsaw) and for having no 老詹 sign-off |
| Valuation / cycle position (downside if wrong) | 20% | **20** | −70% MoS vs a 25% requirement; −41% to central; base expected return below the Treasury; ATH, +18.5% over MA200; memory headwind not fully landed. Not lower because the path is a slow de-rating with no solvency tail (wide moat 76, A− 78, net cash) |
| Dated / event risk | 10% | **55** | One gap event (late-Jan print, worst-day precedent −7.35%), budgeted. SCOTUS 11 Jan is upside-skewed. D.C. Circuit (Google ~$20bn/yr) and Section 232 Phase 2 are binary but undated and 2027-or-later [R:The dictator §0, §6] |
| Correlation / concentration | 10% | **50** | Low beta, outside the AI cluster, but a top index weight (look-through unknown). The SKHY offset is gone (immaterial, A.8). Size unknown, bought at the high |
| Measurability | 15% | **40** | Primary bars exist (+). But size, LNW, broker and margin status are all undisclosed; the portfolio file is empty (9th); VaR/stress not run; technical not desk-signed; no decision record |
| **Weighted** | | **57** | 0.30×90 + 0.15×65 + 0.20×20 + 0.10×55 + 0.10×50 + 0.15×40 = 27.0 + 9.75 + 4.0 + 5.5 + 5.0 + 6.0 = **57.25 → 57** [D] |

**Reading the score.** 57 vs SKHY's 32 is the gap between a clean instrument at a rich price and a rich instrument at a fair-ish price. **57 is not a buy signal.** It says the position is survivable at ≤ 6.4% with the stop. 𢦀鳩仔's 28 says it is expensive. The committee weighs both. **What moves it** (directional judgement, not re-computed):
- A-2 refused (no stop) → ~45, cap 2.4%.
- Margin debit found against AAPL → ≤ 40 until cleared.
- Size > 10% → breach, and the score is moot until cured.
- 老詹 confirms the stop, LNW disclosed and the portfolio file populated → ~62.
- A close below $350.87 into the print → −5 for the event component.


## RULING B — SK hynix re-entry
### B.1 Verdict on re-entry at today's price: **VETOED** (formal)

> **CRO VETO, 2026-11-16.** Re-entry into SK hynix at today's price is **VETOED**, in either instrument: the SKHY ADS at ~$131.79 and the ordinary 000660.KS at ~₩1.21–1.30m. Under standing rule 3 this veto does not proceed unless the Owner personally overrides it in writing. Any override is logged as dissent.

**Grounds (each sufficient on its own for the ADS):**
1. **Risk score.** The ADS initiation scores **26/100** (B.6), below the ~40 line. On 12 Nov I wrote that I "would not approve *initiating* SKHY ADS at $129 under any sizing." Nothing since then improves it: the premium is unmeasured, the trend is down on every measure, and the bars confirm a 101% vol [R:CEO switch §1, §3].
2. **Premium unmeasured.** The last range is 43–52%. The current level is **NOT OBTAINED** (no dated 13 Nov Korean close or FX). The CEO's own do-not list says: "Don't buy the ADS without a dated premium reading." I make that a condition.
3. **Value.** $131.79 is 28.7% above the $102.40 probability-weighted value. The ordinary is +13% to +21% above ₩1,070,000 [R:CEO re-entry §3, §4]. Price above value is not a risk-limit failure in itself, but it removes the only reason to accept the risks below.
4. **Process.** `committee_approval_required` is not met, and `decision_record_before_ticket` is not met.
5. **Leverage.** The only account the firm can see is a margin account carrying a debit (A.6). No new position may be opened into it.
6. **Ordinary only.** KRX access is unconfirmed, there are no ordinary bars on disk and no 老詹 stop, so `stop_required` cannot be met. Its provisional score is 40, at the line (B.6), not above it.

**On the exit.** The full exit at $137 satisfied every SKHY condition (C1–C10 of 12 Nov) at once. It beat holding by $5.21/ADS against the 13 Nov close [R:CEO re-entry §0]. Tickets T0–T9 are **VOID**. Each was a sell, so placing one now would open a **short**, which no limit permits. 腦大裝草 should append the exit to `memory/decisions/2026-11-13-skhy-retrospective.md` with the date as NOT DISCLOSED.

**The anchoring point, endorsed.** $131.79 being below the $137 exit is not a discount (CEO §2). It plays no part in this ruling.

### B.2 ADS re-entry cap at $102.40 / $80 / $61.44: does my 3% still bind?

**The 3% was never a price rule. It is a premium rule.** On 12 Nov: cap = 1% ÷ premium component, where the premium component = 1 − 1/(1 + premium). At a 50% premium that is 33% of price, so the cap is 3.0%. **The cap therefore depends on the *measured premium at entry*, not on the ADS price.** The same $80 can mean two different instruments:

| ADS price | If the premium persists (~45%) | If the premium has collapsed (~0%) |
|---|---|---|
| **$102.40** | Parity ≈ $70.6 → ordinary-equivalent ≈ ₩0.95–0.97m, ~10% below FV. Premium component 31% → **cap 3.2%** | Ordinary-equivalent = $102.40 × 10 × 1,350–1,380 = **₩1.38–1.41m, 29–32% *above* FV ₩1,070,000**. Fails value. **No entry** |
| **$80** | Parity ≈ $55 → ordinary ≈ ₩0.74–0.76m, ~30% below FV. Premium risk intact → **cap 3.2%** | Ordinary-equivalent **₩1.08–1.10m ≈ FV**. MoS ≈ 0%. Premium risk gone. **Cap set by the stop (≤ 5.0%, below)**, but the value case is only fair value, not a bargain |
| **$61.44** | Parity ≈ $42 → ordinary ≈ ₩0.57–0.59m, **below** the ₩642,000 40%-MoS line. Deep value on the business, **cap still 3.2%** | Ordinary-equivalent ₩0.83–0.85m, ~21–22% below FV. **Cap set by the stop (≤ 5.0%)** |

[D: parity = price ÷ 1.45; ordinary-equivalent = ADS × 10 × USD/KRW, USD/KRW 1,350–1,380 [A]; 1 ADS = 0.1 ordinary per the SKHY retrospective record.]

**Ruling on the ADS cap (binding):**

> **ADS cap = the smallest of:**
> (i) **1% ÷ [1 − 1/(1 + p)]**, where p is the ADS premium measured on a **dated** 000660 close and a **dated** USD/KRW, no more than one session before the entry;
> (ii) **1% ÷ (d + 13.7%)**, where d is 老詹's stop distance at entry and 13.7% is the ADS's worst day on primary bars (16 Jul) [R:CEO switch §1];
> (iii) **5.0%** provisional ceiling, as for the ordinary (B.3); and
> (iv) 10% (`max_single_position`).
> **If p cannot be measured, the cap is zero. There is no default to 3%.**

Values of (i): p = 52% → 2.9% · 50% → 3.0% · 45% → 3.2% · 43% → 3.3% · 25% → 5.0% · 20% → 6.0% · 15% → 7.7% [D]. Values of (ii): d = 5% → 5.3% · 6.7% → 4.9% · 10% → 4.2% [D].

**So does the 3% still bind?** **Yes, at any price where the premium is still ~43–52%.** It binds at $102, at $80 and at $61 alike. **No, where the premium has collapsed.** But then the ADS is just the ordinary in a dollar wrapper, the stop governs (≤ ~5%), and **the value test must be re-run on the ordinary-equivalent price**, because the ADS's $102.40 fair value is probability-weighted *with* the premium. At zero premium, the ADS's fair value is parity central, $80 [R:𢦀鳩仔 via CEO switch §5].

**The $80 point the CEO raised is correct, and it has a sharper edge.** If the ADS reaches $80 because the premium collapsed, the Owner is buying the business at fair value, not at a 22% discount. **If the collapse came from a KSD/FSC quota change**, the conversion valve is open two ways. The premium is then structurally bounded near zero, and the instrument is clean: that is the best case for an ADS re-entry. **If it came from flows with the quota still exhausted**, the premium can re-widen (good for a holder), and a discount is bounded by cancellation arbitrage. In both cases the downside basis risk at a near-zero premium is small. Below a 15% premium, I stop counting it, which matches the `max_basis_premium: 0.15` line proposed on 12 Nov (not applied; Owner's call).

**Premium monitor after entry (binding if an ADS is bought):** weekly, as SKHY Condition 4. Two triggers:
- If p rises after entry, the premium component grows and the cap is recomputed with (i). The excess is trimmed next session.
- Any KSD/FSC/depositary announcement on the quota leads to a same-week re-rule.

### B.3 Provisional cap and conditions for the ordinary 000660.KS

**Premium risk: removed.** This is the CEO's best finding, and I endorse it: the ordinary is the cleaner instrument. **Three risks replace the premium.**

| Risk | Status | How I handle it |
|---|---|---|
| **Market access** | KRX access at any of the Owner's brokers is **NOT OBTAINED**. Webull's ₩888,241 of "KRW buying power" is **margin capacity**, not evidence of access [R:CEO re-entry §4] | **Gate (B-R0).** No KRX access confirmed in a **cash** account → no ordinary re-entry. **Using the KRW buying power = borrowing KRW = `leverage: none` breach.** Prohibited |
| **FX (KRW/USD)** | Base currency USD [C]. Dated USD/KRW and KRW volatility **NOT OBTAINED**. The direction of KRW in a memory downturn is NOT OBTAINED; **I assume the FX leg does not hedge the equity leg [A]** | KRW is bought with **cash converted at the time**, never borrowed. Risk is measured in USD. A 5% KRW move is 5% on the position [D, trivially]. The stop is measured in KRW; FX is an additional unstopped leg, which is one reason the provisional ceiling sits below the stop-only number |
| **Single-name Korea** | The ordinary carries SK hynix, the memory cycle, Korea country/governance and the KRW. There is **no country limit** in `risk-limits.yaml` | SKHY ADS + 000660 count as **one name** for `max_single_position` (look-through). Both count in Info Tech (`max_sector`) and the AI cluster. I flag the missing country line for the Owner; I do not invent a number for it |
| **Stop** | No ordinary bars on disk; no 老詹 level in KRW | **Gate.** 老詹 sets a close-basis KRX stop from KRX structure before any entry. A placeholder from ADS levels is not acceptable, because ADS levels contain premium noise |
| **Cycle** | 12 Nov: ordinary −50.4% peak-to-trough 2021→22 (intraday); 8/12 cycle indicators flashing [R:CRO 12 Nov §5] | Covered by the stop. Held through the stop at the cap: 5% × 50% = 2.5% of LNW, inside the 20% budget |

**Provisional cap (binding until re-ruled at R1):**

> **000660.KS cap = min[ 1% ÷ (d + 13.7%), 5.0% of LNW at market ]**, combined with any SKHY ADS. d = 老詹's KRX stop distance at entry. 13.7% is the ADS worst day used as a **proxy [A]** for the ordinary's gap until the ordinary's own worst day is computed from KRX bars, at which point it replaces the proxy.

The **5.0%** is derived: 1% ÷ (6.7% + 13.4%) ≈ 5.0%, using SKHY's 12 Nov stop distance and gap under the stricter method in A.4 [D]. It is provisional because the ordinary's volatility, gap history and FX volatility are all unmeasured. It is a ceiling, not a target. The CEO quotes Zac's stop-only 7.5–10%; **I do not adopt it**, because it excludes the FX leg and uses the lenient gap method.

**Minimum-ticket check.** One share ≈ ₩1.2–1.3m ≈ US$900–970 at today's price [R:CEO §4]. At R1 (≤ ₩1,070,000, ≈ US$775–790 [D at 1,350–1,380]), a ⅓-of-5% tranche needs LNW ≥ ~US$47,000 to buy even one share [D: 790 ÷ (0.05/3)]. **If LNW is below that, the ordinary cannot be staged, and the Owner's choice is one share or none.** That is a reason to disclose LNW first.

### B.4 The CEO's staging and confirmations: **ACCEPTED WITH AMENDMENTS**

The structure is sound: a pre-registered plan, value plus confirmation, thirds, a committee at R1, and no buying because the price is under the exit. Seven amendments are needed. Three of them fix internal inconsistencies.

| # | CEO plan | Amendment | Why |
|---|---|---|---|
| **1** | Triggers are given in pairs: "≤ $102.40 / ₩1,070,000", "≤ $80 / ≈₩850,000", "≤ $61.44 / ₩642,000" | **Key every value trigger to the ordinary's KRW price.** R1 ≤ ₩1,070,000 · R2 ≤ ₩850,000 · R3 ≤ ₩642,000. An ADS price qualifies **only** through its ordinary-equivalent (ADS × 10 × USD/KRW) together with a measured premium (B.2) | The pairs are not equivalent. $102.40 at zero premium is ₩1.38–1.41m, 29–32% *over* FV. The pair matches only at a ~29% premium [D]. A trigger that means different things in two currencies is not a trigger |
| **2** | "Premium below ~20% … **or re-entry via the ordinary**" counts as a *confirmation* | **The premium is an instrument gate, not a confirmation.** Each tranche needs value **plus one confirmation from the cycle or trend-repair families**. Choosing the ordinary removes a risk; it confirms nothing | Confirmations exist to show that the decline has ended or the thesis has improved. Switching instruments tells you neither. As written, "buy the ordinary at ₩1,070,000" would self-confirm |
| **3** | Trend repair: "higher low above $122.20, then a daily close above $145.79" | **Redefine at the time, from the new structure, by 老詹, in KRW for the ordinary.** Form: a higher low above the post-decline low, then a close above the most recent lower high | **Internally inconsistent with R1–R3.** A close above $145.79 cannot coexist with a price ≤ $102.40. By the time value triggers, $122.20 has broken and these levels no longer exist (the CEO says so for the stop in §7) |
| **4** | Thirds bought at successively lower prices | **Each tranche carries its own close-basis stop from 老詹. If any tranche's stop fires, the remaining ladder is VOID.** A later tranche then needs a fresh confirmation and my re-run. **No averaging down through a stop** | R2 sits ~20% below R1 [D: 850/1,070]. A structural stop on R1 will almost certainly fire before R2. Without this rule the ladder is a held-through scale-in. Sized that way (one stop below R3, ≥ 40% away), the cap would be ~1% ÷ 40% ≈ 2.4% total [D], not thirds of 5% |
| **5** | "⅓ of the maximum John approves" | **Aggregate risk across all open tranches ≤ 1% of LNW**, computed as Σ size × (d + 13.7%). The maximum is **recomputed at each tranche** (premium, stop and LNW change) | `max_risk_per_trade` is per name in substance. Three tranches must not add up to 3% at risk |
| **6** | "Avoid … the week before 4Q26 results unless already in the value zone" | **No tranche in the 5 sessions before 4Q26 results, with no value-zone exception. No tranche from 24 Dec 2026 until a 2027 Wuxi tool licence is reported or refused** (the licence is due ~31 Dec; that expiry date is derived) | A 10–15% gap either way on a cycle-turn print [R:CEO §7] is a coin-flip whatever the zone. The Wuxi licence is a dated binary on ~⅓ of DRAM wafer output (The dictator, via CRO 12 Nov §6) |
| **7** | R0: confirm KRX access; disclose LNW | **R0 expanded. All of these before R1:** (a) LNW disclosed and `config/portfolio.yaml` populated; (b) KRX access in a **cash** account, or a dated premium reading for the ADS; (c) the Webull USD debit cleared (A.6); (d) a decision record written *before* the ticket; (e) the committee convened at the R1 trigger, approving the whole ladder **with these amendments**; (f) 老詹's stop for the instrument; (g) my re-score ≥ 40 | Every one of these is a limit or rule in the config, not a preference |

**Accepted as written:** the cycle confirmation family ("any two" of Elon Musk's falsifiers); "what does NOT qualify" (price below the exit, single gap-up days, analyst targets); the close-basis stop with a next-open fill; and the do-not list (CEO §9) in full.

**R2/R3 do not need a new committee** if the R1 committee approved the ladder with these amendments. **They do need my re-score** (premium, stop and cycle will all have moved). That re-score can be a one-page addendum.

### B.5 Cross-position: is a SKHY re-entry a hedge for AAPL, or a separate bet?

**A separate bet. It gets no hedge credit in either direction.**

1. **The statistics do not support a hedge.** ρ = −0.21, R² = 4.4%, about two standard errors from zero on 90 sessions, all of them from one regime (AAPL re-rating, SKHY falling from its peak). The minimum-variance ratio is ~0.05 [D, A.8]. As a hedge for AAPL, SKHY is a 101%-vol instrument used to offset 4% of a 25%-vol instrument's variance. That would add risk, not hedge it.
2. **The fundamental link is real but unsized.** AAPL buys memory and SK hynix sells it [R:Elon Musk §2, §9]. That is a reason to *note* the offset. It is not a reason to size either position around it. No desk has produced a memory-price beta for either name (NOT OBTAINED).
3. **Consequences for the rulings.**
   - **AAPL:** its cap (6.4%) was set with no hedge credit. Losing SKHY changes nothing numerical (A.8). The exit lowered total book risk.
   - **SKHY re-entry:** sized on its own premium and stop (B.2/B.3). It may **not** be sized up as "the AAPL hedge", and the AAPL cap may **not** be relaxed because SKHY is held. The two are checked separately against their own limits, and together against `max_sector` (both Info Tech).
   - **The AAPL→SKHY switch** (CEO switch §4) is not available under these rulings. Proceeds of any AAPL trim go to **cash** (the 10% floor, which is unmeasured). They are not pre-committed to SKHY. A SKHY purchase funded by an AAPL sale is a SKHY initiation and must pass B.4 R0–R1 like any other.
4. **If the Owner actually wants a memory-price hedge for AAPL**, that is a different proposal. It needs a hedge ratio, an instrument chosen for the hedge rather than the thesis, and C朗/Mario input. Nothing on file proposes one, and I do not recommend one. The recommended answer to AAPL's memory exposure is **size and the stop**.

### B.6 Risk scores: SK hynix re-entry

| Component | Weight | ADS at $131.79 | Ordinary at ₩1.21–1.30m | Note |
|---|---|---|---|---|
| Instrument structure | 30% | **5** | **60** | ADS: 31–34% of price is a regulatory artefact, *unmeasured today*. An initiation scores 5, as I said on 12 Nov. Ordinary: no premium, but FX, access and single-country risk, and no ordinary bars |
| Stop quality vs volatility | 15% | **35** | **30** | ADS: $120.35 is 8.7% below $131.79, ≈ 1.1 ATR on a 101%-vol instrument. Ordinary: no KRX stop exists |
| Cycle position | 20% | **30** | **30** | Unchanged from 12 Nov: 8/12 indicators; down-trend in full bearish MA stack [R:CEO switch §3] |
| Dated / event risk | 10% | **40** | **40** | Wuxi licence ~31 Dec, 4Q26 results late Jan, buyback end 28 Jan: all inside 11 weeks |
| Correlation / concentration | 10% | **40** | **40** | AI-capex cluster; AVGO already held; no hedge credit (B.5) |
| Measurability | 15% | **35** | **25** | Primary ADS bars (+). Premium, LNW, KRX access and FX are all NOT OBTAINED |
| **Weighted** | | **26** | **40** | ADS: 1.5 + 5.25 + 6.0 + 4.0 + 4.0 + 5.25 = **26.0**. Ordinary: 18.0 + 4.5 + 6.0 + 4.0 + 4.0 + 3.75 = **40.25 → 40** [D] |

**Reading.**
- **ADS 26** is below the hold-only 32 of 12 Nov. That 32 was rounded up for an *existing* exposure that could be exited at zero cost, and an initiation gets no such credit.
- **Ordinary 40** sits exactly at the line. It is **not** an approval: it carries the measurability penalty that B-R0 is designed to clear, and price, committee and stop gates still fail today.
- **Neither score is pre-registered for R1.** Both are re-run when R1's value and confirmation conditions are met.

**What moves them.**
- A dated premium ≤ 15% with a quota change confirmed → ADS ≈ ordinary.
- KRX cash access, ordinary bars and a 老詹 stop → ordinary to ~48 [D: stop component 30→55, measurability 25→50].
- No Wuxi 2027 licence → −5 on both.
- A cycle confirmation (two of the falsifiers) → +5 to +10 on the cycle component.


## Binding conditions (consolidated)

Each condition is binding on Zac and 死潘狗, and each is verifiable by the Owner with a number or a document. **All trims and entries are recommendations for the Owner to execute himself. No agent places, modifies or cancels orders** (CLAUDE.md rule 1).

**AAPL (Ruling A)**

| # | Condition | Owner verifies by |
|---|---|---|
| **A-1** | **No leverage.** The AAPL account carries no debit and AAPL secures no loan. If it does, the debit is cleared next session, before anything else. The Webull −$12.06 USD debit is cleared by any of the A.6 options | broker statement: debit = 0 / net cash ≥ 0 |
| **A-2** | **Hard stop: daily close < $325.08 → full exit at the next open.** Close-basis; never lowered; raised only by 老詹. (Option B, if the Owner elects it in writing: half at < $325.08, the rest at < $308.91, with the cap at 5.6%) | dated note of the rule; after a qualifying close, the next-session sale |
| **A-3** | 老詹 confirms or replaces $325.08 **within 5 sessions** (by 21 Nov 2026). The cap is recomputed with the A.4 formula if the level changes | dated note in `reports/technical/` |
| **A-4** | **Size.** ≤ 6.4% of LNW at market → hold. 6.4–10% → trim to ≤ 6.4% by the A-5 deadline. **> 10% → reduce to ≤ 10% next session (breach)**, then to ≤ 6.4% by A-5. As price rises, cap = 1% ÷ (1 − 301.19/price); trim the excess (e.g. 6.0% at $360.83, 4.8% at $380) | shares × price ÷ LNW, written into `config/portfolio.yaml` |
| **A-5** | **Pre-earnings:** at ≤ 6.4% **by 20 Jan 2027**, or 5 sessions before the announced FQ1-27 date if earlier. The stop is honoured after the print whatever the gap | dated trade confirmation, or position ≤ 6.4% on that date |
| **A-6** | **No add** above $245, and none in the 10 sessions before the print. An add at any price needs the committee | no AAPL buy ticket in `reports/execution/` |
| **A-7** | **Disclose** share count, broker, account type and LNW (see the final section). Until then, A-4 is self-assessed by the Owner against the table | the numbers |
| **A-8** | **Retrospective decision record** for the $357.60 purchase (腦大裝草), with the Owner's thesis in his own words and this ruling as the risk view | file exists in `memory/decisions/` |
| **A-9** | **Event tripwires go to the committee at once:** a D.C. Circuit opinion disturbing "payments permitted" (Google); a Section 232 Phase 2 proclamation naming smartphones/HTS 8517; a Chinese action naming Apple [R:The dictator §7]. These are not automatic sells. They trigger a same-week re-rule | 修大哥 / The dictator note |

**SK hynix re-entry (Ruling B)**

| # | Condition | Owner verifies by |
|---|---|---|
| **B-1** | **Re-entry at today's price: VETOED**, in both ADS and ordinary. Escalated, not overridden | no SKHY/000660 buy ticket |
| **B-2** | **ADS cap = min[1% ÷ (1 − 1/(1+p)), 1% ÷ (d + 13.7%), 5.0%, 10%].** p is measured on a dated KRX close and FX ≤ 1 session old. **p not measured → cap zero.** At p ≈ 43–52% the cap is 2.9–3.3%, so **the 3% binds at $102, $80 and $61 alike** while the premium persists | dated premium computation attached to any ticket |
| **B-3** | **Ordinary cap = min[1% ÷ (d + 13.7%), 5.0%]**, combined with any ADS (one name). Cash-funded KRW only; **using Webull's KRW buying power is prohibited (leverage)** | account type; FX conversion confirmation |
| **B-4** | **Staging per B.4:** value triggers in KRW (₩1,070,000 / ₩850,000 / ₩642,000); value + one **cycle or trend-repair** confirmation (premium is a gate, not a confirmation); trend repair redefined by 老詹 at the time; a stop per tranche, with a stop-out voiding the ladder; aggregate name risk ≤ 1% of LNW | committee minutes at R1 approving the amended ladder |
| **B-5** | **R0 gates before R1:** LNW disclosed and portfolio file populated; KRX access in a cash account (or a dated premium for the ADS); Webull debit cleared; decision record before the ticket; committee at R1; 老詹 stop; CRO re-score ≥ 40 | each item on file |
| **B-6** | **Blackouts:** no tranche from 24 Dec 2026 until the Wuxi 2027 licence is reported or refused; none in the 5 sessions before 4Q26 results | calendar |
| **B-7** | **No hedge credit:** SKHY is not sized as an AAPL hedge, and AAPL's cap is not relaxed by a SKHY holding. AAPL trim proceeds go to cash, not to SKHY | — |
| **B-8** | **Weekly premium monitor** for any ADS held (12 Nov Condition 4, carried forward). If p rises, the cap is recomputed and the excess trimmed | weekly log row |

**Escalations to the CEO and the Owner (made by this report):**
1. Webull margin debit: `leverage: none` breach on its face (A.6).
2. `config/portfolio.yaml` is empty, for the **ninth** time. The KPI "portfolio inside all limits" is **not reported**, because I will not sign a number I cannot measure.
3. Possible AAPL `max_single_position` breach if the position is > 10%. Unknowable until disclosed.
4. The 0.40-vs-0.50 cluster/target contradiction remains unresolved.

**Proposed config changes (NOT applied; Owner approval required):**
- (a) the `instrument:` block from 12 Nov §3.3, which B.2 now relies on;
- (b) `per_trade.stop_type: close | intraday`, as proposed 12 Nov;
- (c) a gap-allowance rule: risk at stop = (distance + one worst-day move), formalising the A.4 method;
- (d) a country/FX line for non-USD single names. I propose the line, **not a number**, because the Owner's tolerance sets it.


## NOT OBTAINED

1. **AAPL position size, broker, account type (cash/margin), purchase date.** No decision record exists.
2. **Owner's liquid net worth.** This is the denominator for every cap in this report.
3. `config/portfolio.yaml` holdings and cash, so all portfolio-level limits (#1, #3, #4, #5, #8) are **NOT COMPUTABLE**.
4. Whether the Webull HKD balance nets the −$12.06 USD to non-negative, and whether interest accrues.
5. **AAPL FQ1-27 earnings date** (late Jan / early Feb 2027).
6. 老詹's sign-off on the AAPL levels (CEO stand-in product).
7. Mo Peter's VaR and Mario's stress runs. Not commissioned in this session; my scenarios substitute and are labelled.
8. AAPL earnings-reaction history beyond 12 months; any historical mega-cap de-rating drawdown precedent.
9. Index/ETF look-through (SPY/QQQ holdings) for AAPL concentration.
10. SKHY sale date.
11. **ADS premium at the 13 Nov close.** No dated 000660 close or USD/KRW on disk.
12. **KRX access** at any of the Owner's brokers; whether that account is cash.
13. 000660.KS daily bars, volatility and worst day (13.7% ADS proxy used [A]); a KRX stop level.
14. USD/KRW (1,350–1,380 used as an assumption) and KRW volatility; the KRW's behaviour in a memory downturn.
15. Memory-price beta for AAPL or SK hynix, which would be needed to size any genuine hedge.
16. Status of the KSD conversion quota after July 2026 (carried from 12 Nov).
17. Owner's tax residency and broker commissions (relevant to trim friction; not to the risk ruling).


## What the Owner must disclose

1. **AAPL share count and the broker/account that holds it.** With the price, this fixes the A.4 band. If it is above 10% of LNW, the next-session reduction applies.
2. **Liquid net worth**, or at minimum the total of all brokerage accounts. One AAPL share at $356.27 is above 10% of any LNW under **$3,563**, and above 6.4% of any LNW under **$5,567** [D]. The only account the firm can see (Webull, ~US$690, no AAPL) is too small to tell us anything. If total LNW is in that range, A-4 converts to "exit", because the cap is smaller than one share.
3. **Is the AAPL account cash or margin, and is there any debit?** Also: clear or explain the Webull −$12.06.
4. **Does the Owner accept A-2 (full exit on a close < $325.08) or elect Option B?** If neither, say so in writing: the cap becomes **2.4%**, and I log dissent.
5. **Other holdings**, especially SPY/QQQ, AVGO beyond the 2 shares and any semis: needed for the sector and look-through checks.
6. **SKHY sale date** and where the proceeds sit (cash, or redeployed).
7. **KRX access:** which broker, and whether it is a cash account. This decides the re-entry instrument.
8. **The Owner's AAPL thesis at purchase**, in his own words, for the retrospective record (A-8).
9. **Whether the Owner overrides the SKHY re-entry veto.** If he does, it must be in writing; I log dissent and the B-conditions still apply to size.

---

*John, Chief Risk Officer. This is research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders; every trim or entry above is a recommendation for the Owner to execute himself.*
