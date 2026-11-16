# SKHY — CRO Pre-Review · Department 6 (Risk Management)

**John, Chief Risk Officer · 2026-11-12**
**Subject:** SK hynix Inc. American Depositary Shares (Nasdaq: SKHY). Owner holds at **US$129.00/ADS**; size **NOT DISCLOSED**.
**Question referred:** hold / add / reduce at current size, against `config/risk-limits.yaml`, with veto.
**Extends:** `reports/committee/2026-11-12-skhy-ceo-synthesis.md` (CEO) and `reports/technical/2026-11-11-skhy-technical.md` §9 (老詹). I do not re-derive what is established there.
**Status of this file:** complete. All sections filled 2026-11-12.

---

## 0. Verdict

| Decision in front of the Owner | Verdict |
|---|---|
| **A. Hold the existing position at current size** | **APPROVED WITH CONDITIONS** — and only if "current size" is at or below the cap in §9 (**3.0% of liquid net worth at market**). If it is larger, the approval converts to **"reduce to 3.0%"** (Condition 1). Size is NOT DISCLOSED, so I cannot tell you today which of these applies. |
| **B. Add in 老詹's $127.3–130.0 zone** | **VETOED.** Not on the chart (老詹's zone is sound) — on the instrument. Every dollar added buys ~$0.33 of regulatory premium with no stop under it (§3). |
| **C. Add above $130 / chase $140+** | **VETOED** (老詹 and I agree; 16% to stop, <4% to resistance). |
| **D. Reduce into $146.8–149.9** | **APPROVED** — a trim of at least one-third is a condition, not an option (§8). |

**One-paragraph reasoning.** The business is executing at a cycle peak; that is a risk I can size. The ADS, however, carries a **44–56% premium to the share it represents** that exists only because a Korea Securities Depository quota is exhausted. That premium is **~$33–36 of the Owner's $129** (§3). It can go to zero on a regulatory decision, on no date, with no price path a stop can intercept. The limits file has no line for it, so I treat it the way the file treats everything else that cannot be stopped: **as capital at risk counted against `max_risk_per_trade`**. That arithmetic — 1% budget ÷ ~33% unstoppable loss — is what produces the **3% cap**. The 7% stop (§4), the cycle (§5) and the dated events (§6) all fit inside that cap; none of them is the binding constraint. The premium is.

**A veto is escalated, not overridden.** The add veto goes to the Owner. The KPI "portfolio inside all limits" is **not reported** this period: `config/portfolio.yaml` is empty and most limits are not computable (§2). I will not sign a KPI I cannot measure.

**Risk score: 32 / 100** (higher = more acceptable; BE 18, INTC 28, 3416 22). Below the ~40 line at which this desk vetoes *initiation*; the hold is approved as a conditional exception because the exposure already exists and the conditions make it survivable. See §10.

## 1. Limit-by-limit check against `config/risk-limits.yaml`

Denominator (portfolio value / liquid net worth) is **NOT DISCLOSED** and `config/portfolio.yaml` holds no positions and `cash_balance: 0.00`. Position size is **NOT DISCLOSED**. Therefore every ratio limit is evaluated **per 1% of portfolio held in SKHY** (i.e. in a form that scales), and the pass/fail column is honest about what cannot be computed.

| # | Limit | Config | Current (actual) | Post-trade / as-held (per 1% of portfolio in SKHY) | Pass / Fail |
|---|---|---|---|---|---|
| 1 | `max_single_position` (at cost) | 0.10 | unknown — file empty | Passes if SKHY ≤ 10% at cost. **My cap in §9 is 3%**, well inside. | **NOT COMPUTABLE** (size undisclosed) · would PASS at ≤3% |
| 2 | `max_single_position_drifted` | 0.15 | unknown | Position is at ~break-even (cost $129.00 vs ~$129.66 10 Nov), so drift ≈ 0. Not binding today. | NOT COMPUTABLE · not binding |
| 3 | `max_sector` (GICS semis) | 0.35 | unknown | Per 1% held: 1% of the 35% sector budget. Binding only if the Owner also holds MU / NVDA / Samsung / KLAC etc. — **no other holdings are recorded anywhere**. | **NOT COMPUTABLE** |
| 4 | `max_correlated_cluster` (AI complex) | 0.40 | unknown | SKHY is unambiguously in the AI-capex cluster (HBM for Nvidia is the thesis). Per 1% held: 1% of the 40% cluster budget. See §7 on the 0.40-vs-0.50 contradiction. | **NOT COMPUTABLE** |
| 5 | `cash_floor` | 0.10 | `cash_balance: 0.00` (placeholder, not data) | Cannot be assessed. | **NOT COMPUTABLE** |
| 6 | `leverage` | none | unknown | **Condition 3:** Owner confirms the ADS are held unmargined. Until confirmed this is an assumption, not a pass. | ASSUMED PASS — verification required |
| 7 | `max_var_95_1d` | 0.03 of portfolio | undefined on an empty portfolio | Per 1% held: with observed 5–13% daily ranges and a −13.4% day on 5 Nov, a 95% 1-day move of **~10% on the name** is a reasonable *estimate* (no OHLCV series, so no formal VaR — Mo Peter NOT commissioned, see §13). 1% × 10% = **0.10% of portfolio per 1% held**. At the 3% cap: ~0.30% vs 3% ceiling — passes by 10×. At 10%: ~1.0% — passes. | PASS on estimate at any size ≤10% · **formal VaR NOT OBTAINED** |
| 8 | `max_drawdown` budget | 0.20 | no peak-to-trough series exists | Contribution per 1% held in the worst modelled case (§5: −54% to parity at a halved ordinary) = **0.54% of portfolio**. At 3%: 1.6%; at 10%: 5.4%. | PASS at ≤10% on contribution · portfolio-level NOT COMPUTABLE |
| 9 | `max_risk_per_trade` (size × distance to stop) | 0.01 | n/a | **This is where the instrument fails.** Distance to stop by *trade* = 6.7% → per 1% held, 0.067% at risk → **cap 14.9%** (then capped by #1 at 10%). Distance to stop by *gap* (5 Nov precedent −13.4%) → **cap 7.5%**. Distance for the **premium component, which has no stop** (~33% of price, §3) → **cap 3.0%**. | **FAIL above 3.0%; PASS at ≤3.0%** |
| 10 | `stop_required` | true | 老詹: daily close < $120.35, logged 11 Nov, "will not be moved lower" | Satisfied in writing. **Whether the Owner has placed it with the broker is NOT DISCLOSED** (Condition 2). | PASS on paper · verification required |
| 11 | `max_adv_participation` | 0.05 | n/a — Tim Cook has not run; Nov daily volume NOT OBTAINED (老詹 §11) | Not assessable. A retail-scale position is very unlikely to approach 5% of ADV on a $26.5bn IPO float, but that is an inference, not a check. | NOT COMPUTABLE · unlikely to bind |
| 12 | options limits | — | no options proposed | — | n/a |
| 13 | `committee_approval_required` | true | **Committee has not convened** (CEO: "not yet"; valuation has not run) | Any *add* is doubly blocked: my veto and the missing committee. The hold is a pre-existing exposure, not a new decision. | **FAIL for an add · n/a for the hold** |
| 14 | `decision_record_before_ticket` | true | No `memory/decisions/` entry for the SKHY purchase at $129 exists (position was taken outside the firm's process) | 腦大裝草 should log the position retrospectively with the Owner's rationale, so the post-mortem has a baseline. | **FAIL (retrospective)** — remediation in §8 |
| 15 | `live_trading` | forbidden | no agent places orders | — | PASS |

**Which limits bind:** #9 (`max_risk_per_trade`) is the only one that produces a number, and it binds at **3.0%** once the premium is counted as unstoppable risk. #13 blocks any add independently. **Which cannot be computed:** #1, #3, #4, #5, #8 (portfolio-level) — all for the same reason, §2.

## 2. `config/portfolio.yaml` is empty — eighth escalation

`holdings: []`, `cash_balance: 0.00`, header still reads "REPLACE WITH REAL DATA". The SKHY position the Owner is asking me to review **is not in the file**. Nor is anything else.

**Prior escalations on record:** MU (18 Jul), BE / KLAC / MRVL (19 Jul), INTC (28 Jul), V64 (30 Jul), 3416 (10 Aug, "seventh escalation"). This is the **eighth**.

**What it forecloses, said plainly (as on 3416):**
- `max_single_position`, `max_sector`, `max_correlated_cluster`, `cash_floor` are **ratios with an unknown denominator**. Not "probably fine" — **not computable**.
- `max_drawdown` has no peak-to-trough series to run against.
- `max_var_95_1d` of an empty portfolio is undefined; the figure in §1 row 7 is a single-name estimate, not a portfolio VaR.
- **I decline to report the "portfolio inside all limits at all times" KPI.** A KPI reported on an unmeasurable quantity is a fabricated number, and rule 5 forbids those.

**What it does *not* foreclose:** the verdict. The 3% cap in §9 is derived from the *instrument* (premium with no stop ÷ 1% budget), not from the portfolio. It holds whatever the denominator turns out to be. The empty file must not be used as a reason to defer the conditions.

**The 0.40-vs-0.50 contradiction.** `portfolio.yaml` targets `ai 0.30 + technology 0.20 = 0.50`; `risk-limits.yaml` sets `max_correlated_cluster: 0.40`. The target allocation, if achieved with AI-capex names in both sleeves, breaches the cluster limit by 10 points on day one. Escalated on BE and INTC; I decline to pick a side (raise the limit to ≥0.50 or cut the targets to ≤0.40 — **Owner's call**). **Does it bear here?** Yes, in one specific way: SKHY is a pure member of the disputed cluster (HBM → Nvidia → hyperscaler capex), so whichever number the Owner chooses, SKHY consumes part of it, and it does not diversify the cluster — it thickens it (§7). It does **not** change the verdict, which is instrument-driven.

**Remediation (unchanged from prior escalations):** Owner enters real `holdings` (at minimum the SKHY line: ADS count, cost $129.00, opened date) and `cash_balance`; 腦大裝草 writes the retrospective decision record. Until then every CRO review on this book is a suitability opinion, not a limit check.

## 3. The ADS premium — a risk the limits file has no line for

### 3.1 What it is
Four desks measured the ADS at **44–56%** above the Korean ordinary (老詹 44–56% at 10 Nov close; 修大哥 51–52% on 6 Nov; 巴爺爺 40%+ on 28 Oct; The dictator 16–51% since listing). Mechanism (The dictator): KSD caps ADR creation at **2.5% of shares outstanding**; the quota was **exhausted 23 Jul 2026**; conversion is **one-way** (ADS → ordinary only) until an ADS holder cancels. My 12 Nov search confirms the mechanism and the July exhaustion and finds **no report of the cap being lifted or widened** — but also nothing after July, so the current status of the quota is **NOT OBTAINED**, not "unchanged".

### 3.2 Classification
This is **not** market risk (the business does not move), **not** credit risk, and **not** liquidity risk in the usual sense (the ADS is liquid; it is the *conversion channel* that is not). It is best named **instrument basis risk of regulatory origin** — the instrument the Owner holds is a derivative claim on an underlying, and its price has decoupled from the underlying's because a regulator has constrained the arbitrage mechanism. Precedents: closed-end fund premiums; A/H premiums; Indian ADR premiums before two-way fungibility; any capital-controlled ADR. The CEO's phrase "concentration-of-mechanism" is also right: **100% of the premium depends on one rule at one institution**.

Its distinguishing properties, which are why no existing limit catches it:
1. **No price path.** A cap widening is an announcement; the ADS reprices toward parity in a session. A stop at $120.35 is a stop on the *path*; this risk has none.
2. **No date.** Not an earnings print, not a licence expiry. It cannot be a "reduce-before" event (§6) because there is no "before".
3. **Asymmetric and non-mean-reverting in the Owner's favour.** The premium can widen further (it has since August), which feels like gains, but every dollar of widening is a dollar more of the position that is pure regulatory artefact. It is a cushion on the way down — the ADS fell 20% vs the ordinary's 31% in October — but that cushion is itself the thing at risk.

### 3.3 How a limits file *should* treat it — proposed line (NOT applied; §11)
Treat the premium as **capital at risk with no stop**, and count it against `max_risk_per_trade`:

```yaml
instrument:                      # NEW — basis between an instrument and its look-through value
  max_basis_premium: 0.15        # ADR/ADS, closed-end funds, dual listings: if (price / look-through parity − 1) exceeds this,
                                 # the excess over parity is counted as unstoppable capital at risk under per_trade.max_risk_per_trade
  measure_at: look_through       # concentration limits (single position, sector, cluster) measured on look-through value
  premium_monitor: weekly        # recompute; a narrowing of >10 points while the underlying is flat/up is a mandatory reduce trigger
```

Arithmetic the line produces for SKHY: at a 50% premium the premium component is 1 − 1/1.50 = **33% of price** → position × 0.33 ≤ 1% → **position ≤ 3.0% of portfolio**. (At a 44% premium: 30.6% → 3.3%; at 56%: 35.9% → 2.8%. I use 3.0%.)

### 3.4 What it does to the position (per $1,000 at $129 cost)
| Premium today | Parity price | Loss to parity | Per $1,000 |
|---|---|---|---|
| 40% (巴爺爺, 28 Oct) | $92.61 | **−28.2%** | −$282 |
| 44% (老詹 low) | $90.04 | **−30.2%** | −$302 |
| 50% (mid) | $86.44 | **−33.0%** | −$330 |
| 56% (老詹 high) | $83.12 | **−35.6%** | −$356 |
| Anchors: 巴爺爺 $98 (28 Oct) / 修大哥 $84 (6 Nov) | | −24.0% / −34.9% | −$240 / −$349 |

*(Parity = $129.66 ÷ (1 + premium); FX sensitivity 1,350–1,380 per 老詹; USD/KRW on 10–11 Nov NOT OBTAINED.)*

**The stop at $120.35 does nothing here.** A cap announcement before the US open means the first print is $85–95; the stop fills ~30% below cost, not 7%. The only protections are (a) size, and (b) the level-independent trigger 老詹 already specified — **premium narrowing sharply while Seoul is flat/up = conversion valve open = sell the ADS leg** — which catches a *gradual* widening of the quota but not a *gap* one. Condition 4 in §8 makes the monitor a weekly, verifiable task.

One more point, stated because it is uncomfortable: **the Owner can sell the premium today.** At ~$129.66 the Owner realises $33–36/ADS of regulatory artefact at break-even. Holding is a decision to keep underwriting it. Upside is not my department; I note only that the exit cost of this risk is currently zero and will not be zero after the announcement.

## 4. The stop and the gap risk

**The level:** daily close < $120.35 (老詹, lowest vendor print of the Nov low cluster; early warning intraday < $122.20). Distance from cost: **6.71%**; from 10 Nov close: 7.18%. Warning line: 5.27% below cost.

**The instrument:** daily ranges of 5–13% in the 29 Oct–11 Nov window, one −13.4% close-to-close day (5 Nov), two +10% sessions (9 Nov, 11 Nov). No OHLCV series was obtainable, so the *frequency* of ≥7% down days since the July IPO is **NOT OBTAINED** — I cannot give an empirical probability and will not invent one.

**Is a 6.7% stop on a 5–13%-range instrument a stop or a coin-flip?** It is a **structural level that will usually be hit by a gap**. The level is not arbitrary — it is the all-time-low cluster, and a close below it means the base failed — so it is a legitimate *invalidation*. But it sits inside one day's range, which means the probability that the *first* close below it is also 3–7 points below it is high. In plain terms: it is a good thesis-stop and a poor loss-stop. The Owner should expect the realised loss at the stop to be **not 6.7% but ~9–10%, with a 13–15% tail**.

**Realised loss if the stop is crossed by a gap (from $129 cost, per $1,000):**
| Gap through stop | Exit ≈ | Loss | Per $1,000 |
|---|---|---|---|
| none (fills ~$120) | $120.36 | −6.7% | −$67 |
| −8% day | $118.68 | −8.0% | −$80 |
| −10% day | $116.10 | −10.0% | −$100 |
| −13.4% day (5 Nov precedent) | $111.71 | −13.4% | −$134 |
| −15% | $109.65 | −15.0% | −$150 |
| −20% | $103.20 | −20.0% | −$200 |

**Probability-weighted loss conditional on the stop being hit — ASSUMED weights, labelled:**
| P(fills near level) | P(−10% gap) | P(−13.4% gap) | E[loss \| stop hit] | Per $1,000 |
|---|---|---|---|---|
| 0.60 | 0.30 | 0.10 | **−8.9%** | −$89 |
| 0.50 | 0.35 | 0.15 | **−9.3%** | −$93 |
| 0.40 | 0.40 | 0.20 | **−9.7%** | −$97 |

The weights are judgement from the observed range, not a measured distribution. The conclusion is insensitive to them: **plan on ~−9% to −10% at the stop, size for −13.4%.**

**Recommendation: accept the level, size for the gap.** Widening the stop (e.g. to ~$110, −15%) buys nothing — a wider stop on the same instrument is still inside two days' range, and it moves the invalidation off the only level on the chart that means something. The correct response is the size: `max_risk_per_trade` 1% ÷ 13.4% = **7.5% of portfolio** is the gap-survivable maximum on the stop alone. The premium (§3) then caps lower, at 3.0%, so **the stop is not the binding constraint** — but 7.5% is the number Zac should carry as the stop-derived ceiling in case the Owner overrides the premium rule.

**Execution point for 死潘狗 / the Owner:** the stop is a *daily close* rule. Do not place a resting intraday stop-loss order at $120.35 — on this instrument it will be swept by an intraday wick (老詹 puts the early-warning at $122.20 for exactly this reason). The Owner checks the close, and if it is below $120.35, sells at the next open. That costs the overnight gap; a resting stop costs the wick. Pick the gap.

## 5. The cycle risk, sized

**Inputs:** 巴爺爺 — share of peak operating profit surviving the last two troughs: **13%** (2018→19) and **<0%** (2021→23); peak-to-trough **4–5 quarters** both times. Elon Musk — **8 of 12** cycle-turn indicators flashing or partial, the configuration seen 2–4 quarters *before* a peak. Both desks: "one to three more strong quarters, then the turn", and the market may price the turn first (29 Oct–6 Nov looked like a rehearsal).

**Precedent (12 Nov search, vendor annual tables, intraday high/low):** 000660 2021 high ₩150,500 → 2022 low ₩74,700 = **−50.4%** peak-to-trough; on monthly closes ~−35%. Sources differ on adjustment basis; I use −50% as the intraday-extreme case and −35% as the close-basis case.

**Scenario: ordinary halves from its peak.** The 24 Aug 2026 ordinary peak was not obtained; 老詹 has the ordinary −31% from 24 Aug at ₩1,132,000 (6 Nov), implying a peak of **~₩1,640,000 (DERIVED)**. Three reference points, FX 1,350–1,380 (assumption; USD/KRW NOT OBTAINED):

| Base for the halving | Trough ordinary | ADS at **parity** | DD from $129 | ADS at **+50% premium persisting** | DD | ADS at +25% (premium half-closed) | DD |
|---|---|---|---|---|---|---|---|
| Implied Aug peak ₩1.64m | ₩820,000 | **$59–61** | **−53 to −54%** | **$89–91** | **−29 to −31%** | $74–76 | −41 to −42% |
| 28 Oct ₩1,487,000 | ₩743,500 | $54–55 | −57 to −58% | $81–83 | −36 to −37% | $67–69 | −47 to −48% |
| 6 Nov ₩1,132,000 (if the halving is still ahead) | ₩566,000 | $41–42 | −67 to −68% | $62–63 | −51 to −52% | $51–52 | −59 to −60% |

**Drawdown range for the position, stated:** **−30% (premium persists, halving from the August peak) to −54% (premium gone, same halving)**; up to −68% if the ordinary halves *from here* and the premium goes. On the −35% close-basis precedent instead of −50%, shift each row up by roughly 15 points of ordinary decline — the parity row from the August peak becomes ~−40% rather than −54%.

**Two observations on this table:**
1. **The premium is 20+ points of the drawdown in every row.** The cycle risk and the premium risk are not additive — they are the same dollars counted at two prices. Owning the ADS instead of the ordinary adds ~20–25 points of downside to an already −30% cycle scenario.
2. **The cycle is stoppable; the premium is not.** A 4–5 quarter decline passes through $120.35 on the way, and the stop fires at −7% to −13%. The scenario table is what the position is worth *if the Owner holds through the stop* — i.e. it is the cost of not honouring Condition 2, and the cost of the premium gapping before the cycle does. The 20% portfolio drawdown budget is not threatened at the 3% cap (worst row 3% × 0.68 = **2.0% of portfolio**); it would be at 10% (6.8%).

**Where I differ from the desks, slightly:** 巴爺爺's "depreciation trap" (D&A ₩30–40tn/yr by 2029 against a trough-year revenue) means the *next* trough could be worse than −50% on the ordinary, not better, because the fixed-cost base is being built now. I do not size to that — it is beyond the 4–5 quarter window — but it is why I will not accept "the floor is higher this time" as a sizing input.

## 6. Dated risks — which are reduce-before events

| Date | Event | Nature | Reduce-before? | Reasoning |
|---|---|---|---|---|
| **by 31 Dec 2026** (DERIVED: "annual 2026 licence"; no source states 31 Dec) | **Wuxi DRAM tool licence lapses.** ~⅓ of DRAM wafer output (The dictator). 12 Nov search: 2026 licences were granted ~30 Dec 2025 (last-minute); Korea Times 4 Nov 2026 reports a 2027 licence under negotiation for **Dalian** (NAND) and SK hynix conditioning a new US fab on China tool approvals; Reuters (via search) says Commerce has **not yet issued** a 2027 licence. **No Wuxi-specific 2027 report found.** | Binary, dated, political, and tied to a US-fab bargain | **TRIPWIRE, not reduce-before, at ≤3%.** Precedent is last-week-of-December resolution; pre-emptive selling in mid-December sells into a likely non-event. **Becomes reduce-before if size > 3%**, or if by **24 Dec 2026** no 2027 licence is reported — then cut to half (Condition 6). | At 3% × a ⅓-output impairment, the hit is survivable. At larger size it is not, and the resolution timing is unknowable. |
| **late Jan 2027** (date NOT OBTAINED) | **4Q26 results.** First print after the 29 Oct precedent (−20% ADS in six sessions on a *beat*). 巴爺爺: 4Q26 guidance points higher; Elon Musk: deceleration cadence +93 → +58 → +13–18 → +10–15%. | Gap event on the stop (§4) | **YES — reduce-before.** This is the gap-through-stop scenario with a known date. | A −13.4% day on an in-line print is on the record. Any portion above the gap-survivable size, or above the level the Owner is prepared to lose 13% on overnight, comes off **before** the print. |
| **28 Jan 2027** | **₩20tn buyback ends.** Supports the *ordinary*. The ADS benefits only through parity. | Removal of a bid in the underlying, same week as results | **YES — reduce-before, combined with the results.** The two land within days of each other. | A print that disappoints into the week the buyback bid disappears is the worst configuration on the calendar. Treat **20 Jan 2027** as the date by which the position is at the post-trim level. |
| **Jan–Feb 2027** | **Hyperscaler 4Q/FY capex guidance** (MSFT, GOOGL, AMZN, META — exact dates NOT OBTAINED). October's round was "no broad raise" (Elon Musk). | Factor risk, not name risk | **TRIPWIRE.** Not reduce-before — it is already in the price after October, and the position should be at the trimmed level by 20 Jan anyway. | A second round without a raise confirms the cadence has stopped; that converts the Elon Musk NEUTRAL to a reduce signal, logged as Condition 7. |
| **no date** | **KSD/FSC cap change** (§3) | Regulatory structure | **Cannot be reduce-before — there is no "before".** Handled by size (§9) and the weekly premium monitor (Condition 4). | |
| behind us | Lock-up (expired 8 Oct; 100% primary IPO; SK Square bound ≥20%) | — | Struck from the plan (CEO). | |

**Net:** the calendar has **one reduce-before window — the week of 20 Jan 2027** — into which three events (results, buyback end, capex round) collapse. The December licence is a tripwire with a date certain. Everything else is handled by size.

## 7. Correlation & concentration assessment

**Factor membership:** SKHY is a pure AI-capex cluster member — HBM → Nvidia → hyperscaler capex — and additionally a **memory-cycle** bet and a **Korea/KRW** bet. It does not diversify anything in the `ai` or `technology` sleeves; if the Owner holds any of NVDA, MU, AMD, AVGO, TSM, KLAC, or Samsung, SKHY is **the same position expressed again**, with the heaviest crowding and the most margin to lose of the group (Elon Musk). Nominal diversification across correlated names is concentration in disguise.

**What is recorded:** nothing. `portfolio.yaml` is empty. Prior CRO reviews on MU, BE, KLAC, MRVL, INTC were vetoes or conditional approvals on *proposals*; none is recorded as a holding. If any were in fact bought, they are in the same cluster and I was not told. **Cluster exposure is NOT COMPUTABLE** — see §2.

**The 0.40-vs-0.50 contradiction** bears here only as a consumer of whichever budget the Owner picks; it does not change the verdict (§2).

**Correlation within the position itself — the point the desks did not make explicitly:** the Owner's instrument has **two risks that are each individually −30%, that share the same dollars, and that are not independent**. A memory downturn is exactly the environment in which a Korean regulator feels free to widen an ADR quota (lower domestic political cost once the "Korea discount" argument fades) — or, conversely, in which US-listed holders cancel ADS to buy the cheaper ordinary, reopening the quota from the inside. I cannot quantify the correlation and will not pretend to; I note that the two scenarios in §5's table are more likely to arrive together than the table's separate rows imply.

**Hedging note for C朗 (not commissioned):** the natural hedge is short ADS / long ordinary, which is precisely the trade the quota forbids. Listed SKHY options (if any exist — NOT OBTAINED) hedge the price path, not the premium gap, and would be priced for the observed 5–13% ranges. I do not recommend a hedge; I recommend the size.

## 8. Conditions (binding on Zac and 死潘狗; verifiable by the Owner)

Each condition is a thing the Owner can check with a number or a document, not a sentiment.

| # | Condition | How the Owner verifies it |
|---|---|---|
| **1** | **Size ≤ 3.0% of liquid net worth at market.** If currently above, reduce to 3.0% in the next session, not at a level — the excess is regulatory premium, not a trade. (If the Owner formally overrides the premium rule, the stop-derived ceiling is **7.5%**, and `max_single_position` caps at 10% at cost.) | ADS count × last close ÷ liquid net worth. Write the three numbers into `config/portfolio.yaml`. |
| **2** | **The stop is operational, not aspirational.** Daily close < $120.35 → sell the full position at the next open. No resting intraday stop order (§4). No averaging down through it, ever. | A dated note in the broker or in `memory/decisions/` stating the rule and the date it was adopted (老詹 logged 11 Nov). After any close below $120.35, the order ticket from the next session. |
| **3** | **Unmargined.** The ADS are held with no borrowed money against them. | Broker statement showing margin balance = 0 / cash account. |
| **4** | **Weekly premium monitor, with a hard trigger.** Each Friday: premium = SKHY close × USDKRW ÷ (000660 close ÷ 10) − 1. **If premium < 25% while 000660 is flat-or-up over the same week → sell half the ADS at the next open. Any KSD/FSC/Citi (depositary) announcement widening or lifting the conversion quota → sell the full ADS position at the next open.** | A dated row per week in `reports/risk/skhy-premium-log.md` (or the Owner's own sheet): date, SKHY, USDKRW, 000660, premium %. 修大哥 to run the announcement watch. |
| **5** | **No add.** Vetoed. Any add proposal returns to committee with 𢦀鳩仔's valuation of the ordinary **and** a separate price on the premium, and this review re-run. | No SKHY buy ticket exists in `reports/execution/`. |
| **6** | **Wuxi licence tripwire.** If by **24 Dec 2026** no 2027 US tool licence covering Wuxi is reported, reduce to half of the then-size at the next open. | A dated source (Reuters/Korea Times/BIS) in `reports/news/` by 24 Dec, or the half-size ticket. |
| **7** | **Reduce-before window.** By **20 Jan 2027** the position is at **≤ half the §9 cap** (≤1.5% of liquid net worth) ahead of 4Q26 results, the 28 Jan buyback end and the capex round — unless 老詹 has recorded a daily close > $152.35 (range-read confirmed), in which case ≤ the full cap. | The ticket, dated before 20 Jan; or 老詹's dated range-confirmation note. |
| **8** | **Trim into strength.** At any daily print in **$146.8–$149.9**, sell at least one-third of the position; at **$158.5–$162.0**, another third. These are 老詹's levels; the trims are not optional. | Tickets at those levels. |
| **9** | **Retrospective decision record.** 腦大裝草 logs the $129 purchase to `memory/decisions/` with the Owner's rationale as of purchase date and this review as dissent. | The file exists. |
| **10** | **Populate `config/portfolio.yaml`** — eighth escalation. | The file has a non-empty `holdings:` and a real `cash_balance`. |

**On the order of operations if several fire at once:** Condition 4 (premium) and Condition 2 (stop) are **sell-everything** rules and override the trims; Conditions 6 and 7 are **sell-half** rules; Condition 8 is a trim. Take the largest reduction that any fired condition demands, once.

## 9. Inputs for Zac — maximum position as a share of liquid net worth

Liquid net worth (LNW) is NOT DISCLOSED; everything is in percent of LNW, with the arithmetic shown. Budget per `max_risk_per_trade` = **1% of LNW per position**. The size is 1% ÷ (loss that the budget must absorb). Three candidate losses, three ceilings:

| Risk being sized for | Loss the budget absorbs | Arithmetic | Ceiling (% of LNW) |
|---|---|---|---|
| Stop by trade (close just under $120.35) | 6.7% | 1% ÷ 0.067 | 14.9% → capped at **10%** by `max_single_position` |
| Stop by gap, 5 Nov precedent | 13.4% | 1% ÷ 0.134 | **7.5%** |
| **Premium to parity, no stop possible** (50% premium → 33% of price) | 33% | 1% ÷ 0.33 | **3.0%** ← **binding** |
| Premium gone + halved ordinary (held through the stop) | 54% | 1% ÷ 0.54 | 1.9% (not used — the stop is between here and there; it is the cost of breaking Condition 2) |

**Maximum I accept: 3.0% of liquid net worth at market.** Sensitivity to the premium measurement: 44% → 3.3%; 56% → 2.8%.

**Contribution to the 20% drawdown budget at that size:** −13.4% gap = 0.40% of LNW; −35% premium = 1.05%; −54% cycle + parity = 1.62%; −68% worst row = 2.0%. All inside budget with room for the rest of a book I cannot see.

**Translation for the Owner, per $100,000 of liquid net worth:** maximum **$3,000** in SKHY ≈ **23 ADS at $129.66**. Expected loss at the stop ≈ $270–300; loss at parity ≈ $990–1,070; worst modelled ≈ $2,040.

**For Zac, three further notes:**
- Size at **market**, not cost, because the premium is measured at market. At break-even the two coincide today.
- **No pyramid.** The add is vetoed; Zac does not need an add-tranche schedule.
- If the Owner overrides the premium treatment, the stop-derived ceiling is **7.5%**, and the reduce-before window (Condition 7) then becomes a hard halving to ≤3.75% by 20 Jan 2027. I would log the override as dissent.

## 10. Risk score (0–100) — input to committee

*Convention: higher = more acceptable. Calibration: BE 18, INTC 28, 3416 22 (all vetoed). Scores below ~40 carry a CRO veto on initiation.*

| Component | Weight | Score | Note |
|---|---|---|---|
| Instrument structure (premium, conversion quota) | 30% | **10** | 33% of the position is a regulatory artefact with no stop and no date. This component alone would score ~5 for an *initiation*; 10 reflects that 老詹's level-independent trigger exists and is monitorable. |
| Stop quality vs instrument volatility | 15% | **40** | A real structural level, but inside one day's range; realised stop loss ~9–10%, tail 13–15%. Sizable, not avoidable. |
| Cycle position | 20% | **30** | 8/12 indicators, 13%/<0% survival ratios, 4–5 quarter decline precedent, −50% ordinary precedent. Business quality (A− statements) is why this is not 15. |
| Dated / event risk | 10% | **45** | One reduce-before window (20 Jan 2027), one dated tripwire (24 Dec 2026). Knowable dates are the easy kind. |
| Correlation / concentration | 10% | **35** | Pure AI-capex cluster, heaviest crowding in the group, two −30% risks on the same dollars. Cluster exposure not computable. |
| Measurability (portfolio file, VaR, stress, volume) | 15% | **45** | VaR and stress not run; `portfolio.yaml` empty for the eighth time; size undisclosed. Penalised because this is the firm's fault, not the instrument's — but a risk I cannot measure is a risk I cannot approve at size. |
| **Weighted** | | **≈ 32** | 0.30×10 + 0.15×40 + 0.20×30 + 0.10×45 + 0.10×35 + 0.15×45 = 3.0 + 6.0 + 6.0 + 4.5 + 3.5 + 6.75 = **29.75**, rounded **up** to 32 for the hold-only case, because the exit cost of the premium risk is currently zero (the Owner is at break-even and can realise it) and because every condition in §8 is verifiable on a date. |

**Reading the score:** 32 is above INTC's 28 because INTC was a *new* initiation into a thickening cluster with an unresolved price gate; it is below 40 because I would not approve *initiating* SKHY ADS at $129 under any sizing. What moves it: a KSD announcement → ≤10 and full exit; a daily close > $152.35 with the premium ≤ 40% → ~40; a confirmed Wuxi 2027 licence → +3; a populated `portfolio.yaml` showing cluster exposure ≤ 0.40 → +3; valuation from 𢦀鳩仔 of the *ordinary* with a margin of safety at the parity price → re-score.

## 11. Proposed config changes (NOT applied — Owner approval required)

1. **`config/risk-limits.yaml` — add the `instrument:` block** in §3.3 (`max_basis_premium: 0.15`, `measure_at: look_through`, `premium_monitor: weekly`). Rationale: the firm's limits assume the instrument is the asset. SKHY proves it is not always. Any ADR/ADS, closed-end fund, dual-listed line or structured product gets caught by this line; nothing else in the file catches it.
2. **Resolve the 0.40-vs-0.50 contradiction** (`max_correlated_cluster` vs `ai 0.30 + technology 0.20`). Raise the limit to ≥0.50 with explicit acknowledgement, or cut the sleeve targets to sum ≤0.40 (INTC review Options A/B). Owner's call; eighth time of asking in effect.
3. **`config/portfolio.yaml` — populate.** At minimum the SKHY line: `ticker: SKHY, sleeve: ai, shares: <n>, cost_basis: 129.00, opened: <date>, decision_record: memory/decisions/<retro>.md`, plus `cash_balance`.
4. **Add a `per_trade.stop_type` field** (`close` | `intraday`) so 死潘狗's tickets carry which kind of stop 老詹 set. SKHY's is a close-basis stop and a resting intraday order would misimplement it (§4).

## 12. Questions for the Owner

1. **How many ADS, and what is the position as a share of your liquid net worth?** Without this, the only verdict I can give is the scaled one above. If it is above 3.0%, Condition 1 applies today.
2. **Is the stop placed, and how?** A daily-close rule you check yourself, or a resting order? (The latter will be swept; §4.)
3. **Margin:** is any borrowed money against the ADS or the account?
4. **Other holdings in the AI-capex cluster** (NVDA, MU, AMD, AVGO, TSM, KLAC, Samsung, any semis ETF)? SKHY is the same bet again if so.
5. **Did you know the ADS was at a 40–56% premium to the ordinary when you bought at $129?** This is not a reproach — it determines whether the premium is a risk you accepted or one you are discovering, and therefore whether holding it is a decision or an accident.
6. **Do you override the premium treatment** (3% cap) in favour of the stop-only ceiling (7.5%)? If so, say so in writing; I log it as dissent and Condition 7 hardens.
7. **Withholding tax** (The dictator): is treaty certification on file with the depositary (15% vs 22%)?

## 13. NOT OBTAINED register

| Item | Status |
|---|---|
| **Position size** (ADS count / $ / % of LNW) | NOT DISCLOSED — review given per $1,000 and per 1% of LNW |
| **Liquid net worth / portfolio value** | NOT DISCLOSED — `portfolio.yaml` empty (eighth escalation) |
| Other holdings (cluster / sector denominators) | NOT OBTAINED |
| **Mo Peter formal 1-day 95% VaR** | NOT COMMISSIONED — no OHLCV series exists to run it on; §1 row 7 is a single-name estimate from observed ranges |
| **Mario stress test** | NOT COMMISSIONED — §5 scenario table is my own, from desk inputs and the 2021–22 precedent |
| Daily OHLCV for SKHY since IPO; frequency of ≥7% down days | NOT OBTAINED — gap probabilities in §4 are ASSUMED weights |
| **11 Nov close**; 9 Nov close | NOT OBTAINED (老詹 §11). A vendor print of $143.07 for the **4 Nov** close surfaced on 12 Nov; it is consistent with a −13.4% 5 Nov (→ ~$123.9) but the same page carried a garbled second quote, so it is **unverified and not used** |
| **USD/KRW** 10–12 Nov | NOT OBTAINED — FX shown as 1,350–1,380 sensitivity |
| 24 Aug 2026 ordinary peak | NOT OBTAINED — ₩1.64m is DERIVED from 老詹's "−31%" |
| **Current status of the KSD conversion quota** (any change since 23 Jul) | NOT OBTAINED — one search; no post-July report found; absence of a report is not confirmation |
| Exact KSD quota (2.5% vs conflicting 25% figure in 老詹 §11) | NOT OBTAINED — 2.5% used per The dictator |
| **Wuxi 2027 licence** status; exact 2026 licence expiry date | NOT OBTAINED — "31 Dec 2026" is DERIVED from "annual 2026 licence"; no source states the date; 2027 negotiations reported for Dalian, Commerce "not yet issued" per Reuters via search; nothing Wuxi-specific |
| 4Q26 results date; hyperscaler guidance dates | NOT OBTAINED — "late Jan 2027" / "Jan–Feb 2027" per desks |
| Listed SKHY options / short interest / ADV (Tim Cook, C朗, 王老吉) | NOT OBTAINED |
| 𢦀鳩仔 valuation of the ordinary | NOT RUN — the re-score trigger in §10 |
| Committee verdict | NOT CONVENED (CEO) |
| 2021–22 ordinary drawdown on an adjusted-close basis | PARTIAL — intraday −50.4%, monthly-close ~−35%, from vendor tables of unknown adjustment basis |

**Searches used: 4 of 4** (KSD cap status; Wuxi licence; 11 Nov close; 2021–22 precedent). Direct page fetch unavailable; no primary filing opened. `tradingkey.com` not cited.

**Sources (search extractions, 12 Nov 2026):** KSD cap mechanism and July exhaustion — Bloomberg Línea, GuruFocus, Invezz (23 Jul 2026), Tiger/Webull syndications. Wuxi/Dalian licences — Korea Times (4 Nov 2026), Reuters via Ground News / BTW Media / 3DTested (Dec 2025), Capital.com, eWeek. 2021–22 precedent — TradersUnion annual table, Digrin monthly series, MarketScreener annual returns. All secondary; none opened directly.

---
*Research and decision support, not financial advice. No agent of this firm places orders. Every figure carries a source or is labelled as an assumption.*

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
