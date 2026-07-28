# Intel Corporation (NASDAQ: INTC) — Valuation / Sum-of-the-Parts

**Analyst:** 𢦀鳩仔, Valuation Analyst — Department 2, Equity Research
**Reference date:** 2026-07-28 · **Price used: $91.68** (close 27 Jul 2026)
**Inputs:** 巴爺爺 `2026-07-28-intc-financials.md` (grade C+, 55/100) · 菲比斯 `2026-07-28-intc-moat.md` (Products NARROW/ERODING, Foundry NONE)
**Framework:** Sum-of-the-parts, per 菲比斯's instruction. **No franchise DCF** — see §0.

---

## 0. Headline

| | |
|---|---|
| **Fair value range (per share)** | **$22 – $55** |
| **Central estimate / target** | **$33** |
| Full scenario spread | $0–10 (bear) · $26 (base) · $84 (bull) |
| **Current price** | **$91.68** |
| **Margin of safety** | **−178%** (price is ~2.8x central FV) |
| 菲比斯's 50% MoS met? | **No.** 50% MoS requires **~$16/share** |
| Sell-side consensus | **$113.72** — I am **71% below** it |
| **Valuation score** | **12 / 100** |

**The one-line finding:** at $91.68 the market is paying today for ~$31–41B of annual operating profit. Intel's *shortage-peak* product-segment operating income annualises to **$19.4B**, and my normalised mid-cycle estimate is **$12.7B**. Even management's own full 2030 plan, delivered on time and in full, discounts back to **$39–46/share**.

### Price-source conflict (disclosed)
Four quotes appear in the source set for 27 Jul 2026: **$91.68** (used — cross-checked on two feeds), $91.88, ~$97.06 (Finbold, "recent close"), and ~$102 (one extract flagged by the CIO). The spread is ~11%. I use **$91.68** as instructed. **This does not change any conclusion** — at $102 the MoS worsens to −209%; at $91.68 it is −178%. No cell in either sensitivity table reaches any of the four quotes.

---

## 1. Why SOTP and not a DCF — and the ROIC disagreement, resolved

菲比斯 says ROIC **2.45% TTM (Mar 2026)**. 巴爺爺 says **~6.5% [estimate, equity base unverified]**. This is load-bearing: if there is no return above WACC, there is no franchise to discount and a DCF is a DCF on management's promises.

**They are not in conflict. They measure different things.** I retrieved the missing equity base and reconciled all three:

| Measure | Numerator | Invested capital | ROIC |
|---|---|---|---|
| 菲比斯 (GuruFocus, TTM to Mar'26) | GAAP NOPAT, TTM — includes the FY2025 loss quarters | ~$122B | **2.45%** |
| 巴爺爺 (recomputed on **verified** equity) | Annualised **Q2'26 non-GAAP** net income $8.8B | $103.1B equity + $48.5B debt − $29.7B cash = **$121.9B** | **7.2%** |
| Same, on est. Jun'26 equity (~$95B after the $11.0B Q2 GAAP loss) | $8.8B | $113.8B | **7.7%** |
| **𢦀鳩仔 — normalised mid-cycle** | Products EBIT $12.7B − Foundry loss $5.0B − corporate $2.5B = $5.2B EBIT → NOPAT $4.4B | ~$117.8B | **3.8%** |

**Resolution:** 巴爺爺's ~6.5% is arithmetically low — on the actual equity base ($103.1B at 28 Mar 2026, retrieved this session; he could not fetch it) it is **7.2%**. But it is the *annualised single best quarter in five years, on a non-GAAP numerator*. 菲比斯's 2.45% is a trailing GAAP figure over a period that includes the trough. **Neither is the decision-relevant number.** The right figure for valuation is the normalised mid-cycle one: **~3.8%**, and it is much closer to 菲比斯.

**Therefore 菲比斯 is right on the call that matters.** At ~3.8% normalised ROIC against a 9–11% WACC there is **no franchise return to capitalise**. SOTP is the correct frame. *Sensitivity: even if I am wrong and the true normalised ROIC is 7.2%, that is still 2–4 points below WACC — the SOTP frame survives either reading. The frame would only break at ROIC >10%, which requires the shortage margins to be permanent.*

**One caveat against myself:** the $103.1B equity figure is at 28 Mar 2026 and includes non-controlling interests (Mobileye). Invested capital is also inflated by ~$110B of net PP&E built for a foundry that does not yet earn — an ROIC denominator problem that resolves *if* Foundry fills. That is the bull case, and I price it in §6.

---

## 2. Assumptions table — every input, visible

| # | Assumption | Bear | **Base** | Bull | Source / justification |
|---|---|---|---|---|---|
| **PRODUCTS** | | | | | |
| A1 | CCG normalised revenue ($B) | 32.0 | **34.0** | 40.0 | Q2'26 annualised = $35.6B. Base strips ~5% consumer shortage pricing (TrendForce: +5–10% since Mar'26) and assumes flat units. |
| A2 | CCG normalised op margin | 18% | **22%** | 26% | Q2'26 actual **26.4%** — shortage-aided. FY2024 was ~25% at trough volumes; 2021 was 40%+. Base = midpoint of the post-2022 range. |
| A3 | DCAI normalised revenue ($B) | 18.0 | **21.0** | 35.0 | Q2'26 annualised = $25.2B. Base strips ~15% price rent (server CPU +10–20% since Mar'26, +8–10% guided 2H26 — 菲比斯 §C) and ~3%/yr continued share loss (server units flat while market grew >10%). |
| A4 | DCAI normalised op margin | 18% | **25%** | 35% | Q2'26 actual **39.5%**, vs **16.1%** one year ago. A 23-point swing in four quarters is not a structural margin. Base sits between the two. |
| A5 | Blended product op margin (derived) | 18.0% | **23.1%** | 30.2% | vs Q2'26 shortage-peak **31.8%** |
| A6 | Cash tax rate | 15% | **15%** | 15% | Large NOL/credit carryforwards; below statutory. |
| A7 | Products multiple (× NOPAT) | 9x | **12x** | 16x | 12x ≈ 8.3% earnings yield ≈ 10.2x EBIT. A share-losing annuity, not a compounder. Cross-check: implies **2.36x EV/sales** vs QCOM ~4–5x, TXN ~9x. |
| **FOUNDRY** | | | | | |
| B1 | Net PP&E allocated to Foundry ($B) | 85 | **85** | 85 | **[ESTIMATE — UNVERIFIED]** Total assets $202.4B (Q1'26); Intel net PP&E ~$105–110B; ~$85B is fab. Could not retrieve the PP&E line. |
| B2 | Replacement-value haircut | 90% | **80%** | 62% | Purpose-specific leading-edge fabs, −36.2% op margin, no merchant buyer. A fab is worth its cash flows, not its cost. Base leaves **$17B** realisable on $85B of book. |
| B3 | PV of operating losses to breakeven ($B) | −26 | **−14** | −7 | Q2 loss $2.1B, improving ~$300M/qtr → breakeven late-2027/2028 (巴爺爺). Base sums H2'26–2028 discounted at 12%. Bear = breakeven slips to 2030. |
| B4 | PV of capex above D&A ($B) | −20 | **−10** | −5 | 2026 capex >$20B, 2027 "significantly above". ~$15B is Foundry vs ~$11B Foundry D&A. **This line IS the funding gap** — see §5. |
| B5 | SCIP partner / CHIPS offset ($B) | +4 | **+7** | +9 | Q2 net partner outflow $12.2B is a co-investment structure, not a burn (巴爺爺 §4). |
| B6 | **Foundry-core value ($B)** | **−33.5** | **0.0** | **+35** | *Excludes 14A merchant success, priced separately at F1.* |
| **STAKES** | | | | | |
| C1 | Altera whole-co value ($B) | 8.75 | **8.75** | 8.75 | Silver Lake 51% at an $8.75B valuation. *Note: the brief's "$3.3B for 51%" implies $6.5B whole; the transacted valuation was $8.75B with ~$4.46B gross to Intel. I use $8.75B and flag the discrepancy.* |
| C2 | Minority-stake discount on 49% | 35% | **20%** | 10% | Non-controlling, illiquid, Silver Lake controls exit timing. |
| C3 | Mobileye market cap ($B) | 6.77 | **6.77** | 6.77 | **Retrieved 2026-07-28.** Corroborates the $3.9B H1'26 goodwill impairment as a *realisable-value signal*, exactly as 菲比斯 argued. |
| C4 | Intel economic ownership | 86% | **86%** | 86% | Post-IPO majority stake **[ESTIMATE — exact % unverified]**. |
| C5 | Block / tax discount | 40% | **28%** | 15% | Selling 86% of a $6.8B float moves the price; embedded gain is taxable. |
| **CORPORATE & CAPITAL** | | | | | |
| D1 | PV of unallocated corporate cost ($B) | −30 | **−20** | −12 | Segments sum to $2.7B of op income vs a barely-positive consolidated GAAP line: ~$2.0–2.5B/yr of real unallocated cost (SBC, intangible amortisation, chronic restructuring) capitalised at ~10x. **Most published SOTPs omit this line. It is real.** |
| D2 | Net debt ($B) | −18.8 | **−18.8** | −18.8 | 巴爺爺, 10-Q at 27 Jun 2026: $48.5B debt − $29.7B liquid. |
| D3 | Warrant exercise proceeds ($B) | +4.82 | **+4.82** | +4.82 | 241M × $20 strike. |
| D4 | **Fully-loaded share count (B)** | **5.424** | **5.424** | **5.424** | 5.040 outstanding + 0.143 escrowed + 0.241 DOC warrants. See §4. |
| **OPTION** | | | | | |
| F1 | 14A success-state incremental value ($B) | — | **130** | — | Merchant foundry with ~$15–20B external revenue at ~20% margins by 2030, plus the re-rating of the internal fab base. |
| F2 | P(≥2 committed high-volume non-strategic 14A logos by YE2027) | 0% | **30%** | 100% | 菲比斯 calls it "roughly a coin-flip." I use **30%** — lower, because committed customers today = **zero**, and the binding constraint is structural conflict-of-interest, not process quality. Decisions due 2H26–1H27. |
| F3 | **14A option value ($B)** | **0** | **39** | **130** | |

**Deliberate non-assumptions.** I have not assumed: a Foundry spin-off (the 241M $20-strike warrants make it prohibitively expensive); any further government equity; a return to 50%+ gross margin (巴爺爺: unsupported by current disclosure); or any value for AI accelerators (Crescent Island is in testing; Jaguar Shores is 2027).

---

## 3. The sum-of-the-parts

| Component ($B) | Bear | **Base** | Bull |
|---|---:|---:|---:|
| Intel Products (normalised) | 68.8 | **129.8** | 308.0 |
| Intel Foundry — core, ex-14A | (33.5) | **0.0** | 35.0 |
| Altera 49% | 2.8 | **3.4** | 3.9 |
| Mobileye stake | 3.5 | **4.2** | 5.0 |
| Unallocated corporate | (30.0) | **(20.0)** | (12.0) |
| Net debt | (18.8) | **(18.8)** | (18.8) |
| Warrant proceeds | 4.8 | **4.8** | 4.8 |
| 14A option | 0.0 | **39.0** | 130.0 |
| **Equity value** | **(2.4)** | **142.5** | **455.9** |
| **÷ 5.424B shares** | **$(0.43)** | **$26.27** | **$84.05** |

*Bear floored at $0–10/share in the headline range: $29.7B of liquidity, investment-grade debt termed to 2066 and a 9.9% sovereign holder mean the equity does not go to zero. A mechanically negative SOTP means the equity is pure option value on a levered turnaround, not that it is worthless.*

| Probability weighting | Bear | Base | Bull | **FV/share** | MoS at $91.68 | 50%-MoS buy price |
|---|---|---|---|---|---|---|
| Cautious | 35% | 45% | 20% | $28.48 | −222% | $14.24 |
| **Adopted** | **30%** | **45%** | **25%** | **$32.70** | **−180%** | **$16.35** |
| Generous | 25% | 45% | 30% | $36.93 | −148% | $18.46 |

**I adopt 30/45/25** and round the central estimate to **$33**, with a stated fair-value **band of $22–$55** (roughly the 25th–75th percentile of the outcome distribution). *The band is deliberately not widened to reach the price — see §8.*

### On the double-counting trap
Two places where SOTPs on Intel routinely double-count, and how I handled them:
1. **Products vs Foundry transfer pricing.** Product-segment margins already reflect an internal wafer charge; the Foundry loss is the under-utilisation and start-up cost. I value Products on *segment-reported* economics and Foundry as a standalone loss-maker. I do **not** additionally credit Products with "free" fabs.
2. **Escrowed shares.** The $15.6B derivative liability *is* the value of the shares to be delivered. I include the 143M shares in the denominator and therefore do **not** also subtract the $15.6B liability. Doing both would double-count ~$13–16B.

---

## 4. Dilution, handled properly

| Layer | Shares (M) | Note |
|---|---|---|
| Outstanding, Jul 2026 | 5,040 | |
| Escrowed, not yet released | 143 | 71M contingently issuable, currently outside both basic and diluted EPS |
| DOC warrants, $20 strike | 241 | **~$17.3B in the money at $91.68** |
| **Fully loaded** | **5,424** | +~30% vs ~4.15B in 2023 |

The warrants are not a footnote. At $91.68 they are a **$17.3B claim on equity value** for $4.8B of cash. I have included the shares in the denominator *and* the $4.8B proceeds in the numerator — the correct treatment, and more conservative than the treasury-stock method (which nets to only 188M incremental shares and would flatter FV by ~$1.15/share).

They also carry a **strategic cost**: they trigger if Intel ceases to own ≥51% of Foundry. This is precisely why I cannot value Foundry at a sale/spin-off price. The one clean route to crystallising Foundry's asset value is legally expensive to take.

**The permanent haircut:** recovering FY2021's $19.9B of net income on 5.424B shares yields **$3.67 EPS** versus the $4.86 that same profit produced in 2021 — a **~24% permanent reduction in peak per-share earnings power**, before any of this year's operating questions.

---

## 5. The funding gap through 2027

Embedded in assumption B4, but stated explicitly:

| | 2026E | 2027E |
|---|---|---|
| Gross capex | >$20B (guided, raised from $18B) | "significantly above 2026" — assume $23–25B |
| Normalised OCF (my mid-cycle assumptions, **not** Q2 run-rate) | ~$18B | ~$19B |
| **Gap** | **~$2–4B** | **~$4–6B** |
| Offsets | SCIP partner contributions, CHIPS incentives (B5: +$7B PV) | |

At the **Q2'26 run-rate** (OCF $7.0B/qtr) there is no gap — H1'26 OCF exceeded PP&E capex by $1.9B, a $7.8B YoY swing, and that is genuinely the survival question answered. **But my base case is that Q2 margins are shortage-aided and normalise.** On normalised cash flow the gap is real but modest: ~$6–10B cumulative through 2027, inside existing liquidity ($29.7B) and offset by partner structures. **I do not model further equity dilution in the base case** — that is a bear-case item, and it is one of the ways I could be wrong in *either* direction.

---

## 6. Method cross-check — SOTP vs multiples

| Method | Implied value | vs $91.68 |
|---|---|---|
| **SOTP, prob-weighted** | **$33** | −64% |
| EV/sales on normalised $55B at 3.0x (generous for 23% margins, declining share) | ~$31/sh | −66% |
| P/E: 20x on normalised EPS ($4.4B NOPAT ÷ 5.424B = $0.82) | ~$16/sh | −82% |
| P/E: 30x on the **Q2 shortage run-rate** ($1.68 annualised) | ~$50/sh | −45% |
| **Management's full 2030 plan** (Products $70B @ 32%, Foundry $30B @ 30% adj), discounted 4yr @ 10–14% | **$39–46/sh** | −50% to −57% |
| **Current market** | $91.68 | — |

**The methods agree, which is unusual and worth flagging.** SOTP, EV/sales and a normalised P/E all cluster in the **$16–33** range. The only method that gets near half the current price is capitalising the shortage quarter at a growth multiple.

**Current multiples for the record:** EV ≈ $481B (or $511B fully diluted). **7.5x** Q2-annualised sales, **8.7x** normalised sales, **~55x** the $1.68 non-GAAP run-rate — and ~105x forward GAAP-adjusted earnings on 菲比斯's read. For a business at 3.8% normalised ROIC.

### Reverse-engineering the price — the most useful number in this report

| If the 14A option is worth… | …then Products+Foundry must be worth | …which needs annual EBIT of (at 15x NOPAT) |
|---|---|---|
| $0B | $524B | **$41.1B** |
| $39B (my base) | $485B | **$38.0B** |
| $130B (full success) | $394B | **$30.9B** |
| $200B (blue sky) | $324B | **$25.4B** |

Against: **Q2'26 annualised product-segment EBIT of $19.4B** (at shortage-peak margins) and normalised **$12.7B**.

**So $91.68 requires Intel to roughly double its shortage-peak operating profit and hold it — while also succeeding in foundry.** That is the underwrite. It is not impossible. It is a demanding, specific, and testable claim, and it is not what I would call a margin of safety.

---

## 7. Sensitivity

### 7.1 Products normalised operating margin × products multiple
*(base-case revenue $55B; all other lines at base. Per-share FV.)*

| Blended op margin ↓ / NOPAT multiple → | 9x | 11x | **12x** | 14x | 16x | 18x |
|---|---|---|---|---|---|---|
| 15% | $13.97 | $16.55 | $17.84 | $20.43 | $23.02 | $25.60 |
| 19% | $17.07 | $20.34 | $21.98 | $25.26 | $28.53 | $31.81 |
| **23% (base)** | $20.17 | $24.14 | **$26.12** | $30.08 | $34.05 | $38.01 |
| 27% | $23.27 | $27.93 | $30.26 | $34.91 | $39.56 | $44.22 |
| **31.8% = Q2 shortage peak** | $26.38 | $31.72 | $34.39 | $39.74 | **$45.08** | **$50.42** |

**Read this cell:** the **top-right corner — Q2's peak margin declared permanent AND an 18x multiple — is $50.42.** Still **45% below** the current price. There is no combination of these two assumptions, within any defensible range, that reaches $91.68.

### 7.2 P(14A success) × Foundry-core value
*(base-case Products. Per-share FV.)*

| P(14A) ↓ / Foundry-core → | −$35B | −$20B | **$0B** | +$20B | +$35B |
|---|---|---|---|---|---|
| 0% | $12.63 | $15.39 | $19.08 | $22.77 | $25.53 |
| 15% | $16.22 | $18.99 | $22.67 | $26.36 | $29.13 |
| **30% (base)** | $19.82 | $22.58 | **$26.27** | $29.96 | $32.72 |
| 45% | $23.41 | $26.18 | $29.86 | $33.55 | $36.32 |
| 60% | $27.01 | $29.77 | $33.46 | $37.15 | $39.91 |

Foundry is worth **~$0.68/share per $B** of value. Even a certain 14A success (P=100%) plus a $35B Foundry adds only ~$40/share to the base — reaching ~$66. **The valuation gap is not primarily a foundry question. It is a Products-margin question.**

---

## 8. Anti-anchoring discipline

*Mandatory section. The desk has vetoed five consecutive names on price and the auditor has flagged it twice. What follows is written against my own conclusion.*

### (a) Where I sit versus the sell-side

| | Value |
|---|---|
| Sell-side consensus target (36 analysts) | **$113.72** |
| Distribution | 10 Buy / **24 Hold** / 2 Sell |
| Recent revisions | KeyBanc $100→**$155**; Citi **$130**; UBS $83→**$121**; Susquehanna $80→**$115** |
| **My central estimate** | **$33** |
| **Gap** | **I am 71% below consensus** |

**This is an enormous gap and I will not soften it by pretending otherwise.** Being 71% below 36 covering analysts is either an edge or an error, and the base rate says error. Here is my honest diagnosis of the disagreement, in a form that can be checked:

Consensus $113.72 at ~30x implies **~$3.79 of EPS**, i.e. **~$20.5B of net income on 5.42B shares**. That is *exactly FY2021's peak profit of $19.9B* — the sell-side is underwriting a full return to franchise-era profit dollars within roughly two years, on a 30%-larger share base, and paying 30x for it. **The disagreement is not about the multiple. It is entirely about whether Q2'26's margins are the new baseline or the top of a shortage.** 菲比斯 has logged the falsification test (2027–28: does DCAI hold ~40% once capacity loosens?). If the sell-side is right about margins, they are right about the price and I am wrong. That is a clean, dated, testable fork — not a matter of taste.

I also note the sell-side is **24 Hold** — the *modal* analyst is not actually recommending purchase at these levels either. The high targets are a minority.

### (b) Three ways I could be wrong

1. **The shortage may not be cyclical.** My entire case rests on normalising DCAI from 39.5% to 25% and CCG from 26.4% to 22%. If AI compute demand structurally exceeds foundry capacity through 2030 — which is a coherent and increasingly mainstream view — then Q2'26 margins are a *floor*, not a peak, and my A2/A4 are the single biggest error in this report. Sensitivity 7.1 shows this is worth ~$24/share on its own (base $26 → $50 at peak margins and a high multiple). **This is my largest exposure and I rate it a genuine one-in-three.**
2. **My Products multiple may be too punitive.** 12x NOPAT / 2.36x EV/sales is a cigar-butt multiple applied to a business generating $12.7B of normalised EBIT with 67% x86 share and real switching costs. QCOM trades at 4–5x sales, TXN at ~9x. If Products deserves 4x normalised sales ($220B), the base rises to ~$43/share. My defence is 菲比斯's evidence on share loss — but a 2.36x multiple prices in *permanent* decline, and Intel just posted its fastest growth since 2011.
3. **Foundry's replacement value may be badly understated — and my PP&E figure is unverified.** B1 ($85B allocated) and B2 (80% haircut) are estimates; I could not retrieve the PP&E line. In a world where leading-edge capacity is the scarce global resource and Washington will not let it be idle, an 80% haircut on functioning 18A fabs may be absurd. At a 40% haircut and no burn, Foundry alone is worth +$51B ≈ $9.40/share more. Relatedly, my $20B unallocated-corporate deduction (D1) is a judgement call that most SOTPs omit entirely; it costs $3.69/share.

*A fourth, structural: I am valuing a special situation with a static model. The government's 9.9% stake, the SCIP structures and the escrow derivative make Intel's capital structure genuinely reflexive — the higher the stock goes, the more capital it can raise on better terms, which improves fundamentals. My model has no mechanism for that feedback loop, and momentum has been right for 52 weeks and I have not been.*

### (c) Steel-man of the bull case — written to persuade

Take the five facts seriously, together, rather than one at a time:

**18A is shipping and beat its output target by ~25%, up 50% QoQ, with Clearwater Forest launched.** After a decade of roadmap failure, this is the first hard, physical evidence of manufacturing recovery — and it is the *precondition* for everything else. **External foundry revenue did $293M in one quarter versus $307M for all of FY2025** — a ~4x annualised step-up and a turn in the second derivative that no bear model anticipated. **Solvency is de-risked by ~$16B of sovereign and strategic capital** (US Government $8.9B, NVIDIA $5B, SoftBank $2B) at $20.47–$23.28, plus $29.7B of liquidity and maturities termed to 2066 — meaning the bear case cannot express itself as bankruptcy, only as underperformance. **The guide beat on both lines for the seventh consecutive quarter**, with gross margin 280bps above guidance and Q3 guided higher still. And **a signed 14A customer in H2'26 is a live, near-dated, binary catalyst** with two prospects already holding PDK access.

Assembled, the bull argument is: *this is not a cigar butt being re-rated, it is the only non-Asian leading-edge logic manufacturer inflecting simultaneously on process, margin, cash flow and external demand, at the exact moment compute capacity became the scarce global input, with a sovereign underwriting the downside.* You do not get to buy that at 10x. My own bull scenario — which I have deliberately built to be *winnable*, with Products at $75B revenue and 30% margins and full 14A success — produces **$84/share**, within 8% of the current price. **The market is not obviously irrational; it is pricing my bull case as the base case.** That is a defensible thing for a market to do when the second derivative has turned on five metrics at once.

**Why I still do not buy it:** because my bull case reaching $84 means the *entire* distribution of good outcomes is required to be certain, today, with no discount for the four years and the execution required to get there — and management's own 2030 plan, delivered in full, only discounts back to $39–46. At $91.68 you are not being paid for the probability that any of it goes wrong, and 菲比斯's list of what could go wrong (Arm at 50% of hyperscaler compute, up from 18% in two years; zero committed 14A logos; server units flat while the market grew >10%) is not short.

**What I am explicitly NOT doing:** I have not widened the fair-value band to protect the scorecard. The honest band from my assumptions is $22–55; a band wide enough to touch $91.68 would require a 27%+ normalised operating margin *and* an 18x multiple *and* certain 14A success — that is not a range, it is a wish. And the four prior bear verdicts are not evidence about this one: **INTC is the first name in this sequence where the operating fundamentals are genuinely improving.** My negative conclusion here rests on price, not on the business, and I want that distinction on the record.

---

## 9. Margin of safety

| | |
|---|---|
| Central fair value | **$33.00** |
| Current price | $91.68 |
| **MoS = (FV − price) / FV** | **−178%** |
| 菲比斯's required MoS (narrow/eroding moat) | **50%** |
| Price required to satisfy it | **$16.35** |
| Price at bull-case FV (no MoS at all) | $84.05 |
| Price at the *most generous single cell* in Sensitivity 7.1 | $50.42 |

**Verdict: the 50% margin of safety is not met, and is not close.** It would require a ~82% decline. Even a *zero* margin of safety — paying full fair value — requires a ~64% decline. Note that 菲比斯's $16 buy zone is approximately where the US Government, NVIDIA and SoftBank were issued stock nine months ago.

**On 菲比斯's $150–250B SOTP anchor:** my built-up base equity value is **$142.5B**, just below the bottom of his order-of-magnitude range, and my bear/bull spread ($0–456B) brackets it. His estimate was well-calibrated. Note both of us land far below the **$497B** fully-diluted market value.

---

## 10. Valuation input to committee score

### **Valuation score: 12 / 100**

| Component | Weight | Score | Rationale |
|---|---|---|---|
| Absolute value vs price | 40% | 5 | Price is ~2.8x central FV. MoS −178%. Every method cross-checks to $16–33. |
| Margin of safety vs required | 20% | 0 | 50% required; −178% delivered. Binary fail. |
| Multiple reasonableness | 15% | 10 | 55x run-rate non-GAAP EPS, 7.5x sales, ~105x forward, on 3.8% normalised ROIC. |
| Asset backing / downside protection | 15% | 35 | Genuine: $29.7B liquidity, IG debt to 2066, sovereign holder, ~$110B PP&E. The equity is not going to zero — but asset backing is ~$0.4–4/share against a $91.68 price. |
| Optionality not in the price | 10% | 30 | 14A is a real, near-dated, binary option — but at $39B EV it is ~8% of market cap, and the *price already embeds far more than the option is worth*. |
| **Weighted** | | **~12** | |

**Recommendation to committee:** **Not a valuation-supported purchase at $91.68.** This is a *quality-improving, price-unsupported* name — the opposite of the four names this desk previously rejected, where the businesses were also deteriorating.

**Actionable levels:**
- **Fair value: $33** (band $22–55)
- **50%-MoS accumulation zone: below $16** — realistic only on a shortage unwind
- **A price at which I would revisit without a 50% MoS: below $45**, i.e. the discounted value of management's own full 2030 plan. Below that you are at least paying a discounted price for a plan rather than a premium to it.
- **Falsification triggers that would force me to raise FV, in order of power:**
  1. **DCAI operating margin holds ≥35% for two quarters after server capacity loosens (2027–28).** Kills my A4 and adds ~$15–20/share.
  2. **Two committed high-volume, non-strategic 14A customers by mid-2027.** Moves F2 from 30% toward 100%: +$25/share.
  3. **External foundry revenue holds >$290M/quarter and grows** — validates the merchant thesis.
  4. **Gross margin sustained above 45%** — would invalidate my normalisation entirely.

If (1) and (2) both land, my base case goes to roughly **$70–85** and this becomes a debate about paying up for quality rather than a valuation veto. I will re-run on the Q3'26 print (late Oct 2026).

---

## Sources

- 巴爺爺, *INTC Financial Statement Analysis*, `/home/user/horse-monitor/reports/equity/2026-07-28-intc-financials.md`
- 菲比斯, *INTC Economic Moat Assessment*, `/home/user/horse-monitor/reports/equity/2026-07-28-intc-moat.md`
- [Intel Corp — Liabilities and Stockholders' Equity (quarterly), stock-analysis-on.net](https://www.stock-analysis-on.net/NASDAQ/Company/Intel-Corp/Financial-Statement/Liabilities-and-Stockholders-Equity/Quarterly-Data) — total equity $103,143M, total assets $202,439M at 28 Mar 2026
- [Intel Quarterly Report Q1 2026 (Form 10-Q) — MarketScreener](https://www.marketscreener.com/news/intel-quarterly-report-for-quarter-ending-march-28-2026-form-10-q-ce7f59dfd88ef12c)
- [Mobileye Global (MBLY) Market Cap — stockanalysis.com](https://stockanalysis.com/stocks/mbly/market-cap/) · [companiesmarketcap.com/mobileye](https://companiesmarketcap.com/mobileye/marketcap/) — $6.77B, Jul 2026
- [Wall Street analysts update Intel stock price ahead of earnings — Finbold](https://finbold.com/wall-street-analysts-update-intel-stock-price-ahead-of-earnings/) — consensus $113.72, 10 Buy / 24 Hold / 2 Sell
- [Most Accurate Analysts Revise Intel Forecasts — Benzinga](https://www.benzinga.com/analyst-stock-ratings/price-target/26/07/60633471/intel-earnings-are-imminent-these-most-accurate-analysts-revise-forecasts-ahead-of-earnings-call-7)
- [Citi raises Intel price target ahead of Q2 — Finviz](https://finviz.com/news/99598/intel-intc-price-target-raised-by-citi-ahead-of-q2-earnings)
- [Intel (INTC) Q2 2026 earnings report — CNBC](https://www.cnbc.com/2026/07/23/intel-intc-earnings-report-q2-2026.html)
- [Intel Q2 2026 Earnings: What the Results Mean for the Stock — TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262049825-intel-intc-q2-2026-earnings-results-analysis-july-23-tradingkey)
- [Intel Corp (INTC) Forecast & Analyst Ratings — ChartMill](https://www.chartmill.com/stock/quote/INTC/analyst-ratings)
- [Intel (INTC) Statistics & Valuation — stockanalysis.com](https://stockanalysis.com/stocks/intc/statistics/)
- Working model: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/sotp.py`, `sotp2.py`

---
*Research and decision support only. Committee and Owner decide. Not financial advice.*
*Assumption-honesty attestation: no assumption in §2 was set to produce a target. The bull case was rebuilt once — upward — after the first pass produced a bull below the current price, which I judged to be a failed steel-man rather than a finding. No other assumption was revised after seeing its output.*
