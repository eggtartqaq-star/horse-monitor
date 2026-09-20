# Financial Statement Analysis — Bloom Energy Corp (NYSE: BE)

> ## ⚠️ CORRECTION NOTICE — this report FAILED audit on 2026-07-19
> **Issued by the CEO (皮褸黃) on the AI Auditor's finding. See `reports/committee/2026-07-19-be-audit.md`.**
>
> **The FY2025 GAAP net income figure of +$6.0m in this report is WRONG.** The filed
> FY2025 figure is a **net LOSS of $87.1m**. The +$6.0m is a *trailing-twelve-month*
> number, not a fiscal-year one (FY25 −$87.1m, less the ~$22m Q1'25 loss, plus the
> $70.7m Q1'26 profit ≈ +$6m TTM). Two independent confirmations: the FY2025 10-K, and
> 菲比斯's accumulated-deficit delta in `2026-07-19-be-moat.md`
> ($3,986.98m − $3,897.62m = **−$89.36m**) — which sits in the same package, filed the
> same day, and was crossed by four analysts without reconciliation.
>
> **Corrections that follow:**
> 1. **"GAAP profitability arrived in FY2025" is FALSE.** Bloom's first GAAP-profitable
>    quarter is **Q1 2026** — one quarter old, not one year.
> 2. **FY2025 ROE is NEGATIVE**, not the +0.8% stated below.
> 3. The earnings-to-cash gap is **~$505m (~25% of revenue)**, not $412m (~20%).
> 4. The **67/100 score contradicts this report's own published trigger** (related-party
>    revenue above 50% of a quarter → score ≤45), a condition now confirmed three
>    quarters running. Treat the 67 as unreliable pending re-score; the auditor's view
>    is that the fundamentals score should be **≤45**.
> 5. Red flag #1 below misattributes the Q3'25 related-party revenue to SK ecoplant. It
>    is **Brookfield**. SK ecoplant is ~$29.9m, ~1.5% of FY25 revenue. See the
>    reconciliation in `2026-07-19-be-valuation.md`, upheld by the audit.
>
> Everything else in this report — the price verification, the balance-sheet analysis,
> the dilution history, and the accounting-quality concern — survived the audit. The
> **direction** of the conclusion is unchanged and arguably strengthened: the correction
> removes a year of claimed profitability that never happened.

**Analyst:** 巴爺爺 (Dept. 2, Equity Research — Financial Statements)
**Reference date:** 2026-07-19 · **Last close used:** Friday 2026-07-17
**Fiscal year:** ends Dec 31 · **Latest reported period:** Q1 2026 (reported 2026-04-28)
**Data staleness:** last audited period is FY2025 (6.5 months stale); last reported period is Q1 2026 (**2.6 months stale**). **Q2 2026 reports 2026-07-28 — 9 days after this reference date.** Treat every conclusion here as pre-Q2.

> Tooling note: direct WebFetch of sec.gov, businesswire, bloomenergy.com, stockanalysis.com, macrotrends, investing.com and stocktitan **all returned HTTP 403 from the agent egress proxy** for this session. All figures below were obtained via search-index extraction of those same primary documents. Figures traceable to the company's own press release / 8-K exhibit text are marked **[PR]**; figures from third-party aggregators are marked **[3P]** and carry lower confidence. Nothing below is from memory.

---

## PART 1 — PRICE VERIFICATION (desk-wide)

### Verdict: **$214.96 is CORRECT. The re-rating is REAL. No stock split.**

| Item | Value | Source / cross-check |
|---|---|---|
| Close, Fri 2026-07-17 | **$214.96** | Search extraction of stockanalysis.com / CNBC quote pages |
| Shares outstanding | **284.44 million** | stockanalysis.com statistics [3P] |
| Market capitalisation | **~$61.14 billion** | companiesmarketcap / stockanalysis [3P] |
| Arithmetic check | 284.44M × $214.96 = **$61.14B** ✓ | Independent confirmation — the price and the market cap were sourced separately and reconcile to the dollar |
| Stock split | **None on record.** BE has never split since its 2018 IPO | stockanalysis.com corporate-actions record |
| 52-week range | **$23.75 – $351.28** [3P, low confidence on the high] | financhill / stockinvest |
| ~12-month price change | **≈ +700% to +1,100%** — magnitude confirmed, exact figure varies by source snapshot date | see below |

**Why the earlier "implausibly high" flag should be withdrawn.** Three independent consistency checks all pass:

1. **Market cap ÷ share count = the quoted price, exactly.** Two separately-sourced numbers reconciling is the strongest available evidence that the quote is not a data error or a foreign-listing/ADR artefact.
2. **The convertible bond confirms the price level from a primary, non-quote source.** In Oct/Nov 2025 Bloom priced **$2.2bn of 0% convertible senior notes due 15 Nov 2030 at a conversion rate of 5.1290 shares per $1,000 = a conversion price of ~$194.97/share** [PR]. Converts are priced at a 25–40% premium to spot. A $194.97 conversion price mathematically requires a **spot price of roughly $140–$156 in Nov 2025**. A stock cannot have a $195 conversion price if it is trading at $30. This independently corroborates the three-digit price regime and is immune to quote-feed error.
3. **The sell-side has repriced accordingly.** JPMorgan's PT path $18 → $33 (Jul 2025) → **~$346 (Jul 2026)** and a 29-analyst mean PT of **$286.20** [3P] are only coherent against a ~$215 spot.

**Conclusion for the desk: use $214.96 and a ~$61bn market cap.** Bloom is no longer a $10–100 stock; the "historically $10–100" prior is stale by roughly a year and should be purged from all models.

**Two cautions attached to the price.**
- **Bloom may be ~39% below its 52-week high of $351.28** [3P, unverified]. If that high is real, the "unstoppable AI-power compounder" framing is already wrong — the stock has had a violent drawdown (consistent with the 8 Jul 2026 Hunterbrook report and/or an AI-power sector de-rate). **Recommend Technical Analysis (老詹) verify the $351.28 high and the drawdown date before the committee treats $215 as "near highs."**
- Secondary aggregator YTD/1-yr percentages are **mutually inconsistent** across sources (one implies a 2025 year-end close of ~$67, another ~$90). I have not been able to pin the exact 12-month return. **The direction and order of magnitude are certain; the precise % is unverified.**

**Valuation context this price implies** (owned by 𢦀鳩仔, but the arithmetic is mine): $61.14bn market cap on FY2026 guided revenue of $3.4–3.8bn = **~16–18× EV/Sales**; on guided non-GAAP EPS of $1.85–2.25 = **~96–116× forward non-GAAP earnings**. The financial statements below must be read against that bar.

---

## PART 2 — FINANCIALS

## Summary & Grade

### **Fundamentals quality grade: B–**

Bloom Energy has genuinely crossed from "cash-burning hardware science project" to "GAAP-profitable, self-funding scale-up." That inflection is real and is visible in three separate statements simultaneously — revenue accelerating to +130%, GAAP operating income positive for six-plus consecutive quarters, and two consecutive years of positive operating cash flow. The balance sheet is, on paper, one of the best in the AI-power complex: **~$2.52bn cash against ~$2.60bn of debt that pays a 0% coupon and does not mature until Nov 2030.** There is no refinancing cliff and no meaningful cash interest burden.

The grade is held to B– rather than A-territory by four things that the P&L headline does not show: (1) **returns on capital remain mediocre** — FY2025 ROE was ~0.8% and ROIC on total invested capital ~2%; the impressive Q1 numbers are one quarter annualised; (2) **shareholders have been diluted ~64% in five years and ~39% on a diluted basis in the last twelve months alone** — the equity re-rating has been shared with a lot of new paper; (3) **customer concentration in a related party appears extreme** (reportedly >55% of one recent quarter's revenue from SK ecoplant, an affiliate); and (4) the company carries an **unresolved accounting-credibility overhang** — a 2020 restatement over Managed Service Agreement accounting, complex PPA/related-party structures, and a live short-seller allegation with two law firms circling.

**Cash flow over reported earnings:** here the two mostly agree at the quarter level (Q1 2026 net income $70.7m vs OCF $73.6m), which is reassuring. But FY2025's $418.1m of OCF is far larger than FY2025's $6.0m of net income — a **$412m gap** that I cannot decompose without the primary cash flow statement. On an order-taking hardware business ramping data-centre deals, the most likely bridge is customer deposits / deferred revenue plus non-cash stock comp. **Working-capital-funded operating cash flow is not durable cash flow.** One third-party research note disputes the figure outright (see Red Flags §3). This is the single most important item to verify on 28 July.

### The 3 numbers that matter most for the thesis

1. **Non-GAAP gross margin — 31.5% in Q1 2026, guided to ~34% for FY2026 [PR].** This is the whole thesis. Bloom is a manufacturer scaling from 1GW to 2GW. If GM holds ≥30% through the ramp, the ~100× forward multiple has a path to being grown into. If it slips back toward the mid-20s as the Fremont expansion absorbs fixed costs, the operating leverage story collapses and there is no valuation support underneath.
2. **Diluted share count — 319.7m in Q1 2026 vs 230.2m in Q1 2025 (+38.9% y/y) [PR].** Per-share value creation, not enterprise growth, is what the Owner owns. At this dilution rate the company must grow enterprise value ~39%/yr just to hold per-share value flat.
3. **Related-party revenue share — reportedly $288m = 55.5% of Q3 2025 revenue (SK ecoplant) [3P, MUST VERIFY].** If accurate, more than half of a quarter's revenue came from a 10.5% shareholder. That is simultaneously a concentration risk, a revenue-quality question, and the exact structural pattern that produced the 2020 restatement. This is the number that decides whether the grade is B– or D.

---

## Profitability

### Revenue trajectory (5 years) [3P aggregation of company filings; FY2025 and Q1 2026 **[PR]**]

| Period | Revenue | YoY growth |
|---|---|---|
| FY2021 | $972m | — |
| FY2022 | $1,199m | +23.4% |
| FY2023 | $1,333m | +11.2% |
| FY2024 | $1,474m | +10.6% |
| FY2025 | **$2,021m** | **+37.3%** |
| Q1 2025 | $326.0m | — |
| **Q1 2026** | **$751.1m** | **+130.4%** |
| FY2026 guidance | **$3.4bn – $3.8bn** | ~+68% to +88% |

The shape matters more than the level. FY2022–FY2024 was a **decelerating** 23% → 11% → 11% business — a mediocre industrial with a nice story. The inflection to +37% and then +130% is entirely attributable to the AI data-centre demand shock, not to a change in Bloom's underlying product economics. **This is a demand-driven, not an execution-driven, re-rating**, which means it is as reversible as the demand shock. Ten years of ~10% growth is the base rate; four quarters of triple-digit growth is the anomaly.

### Margin trajectory

| Metric | FY2024 | FY2025 | Q1 2026 | FY2026 guide |
|---|---|---|---|---|
| GAAP gross margin | 27.5% | **29.0%** (+1.6pp) | **30.0%** (+2.8pp y/y) | — |
| Non-GAAP gross margin | 28.7% | **30.3%** (+1.6pp) | **31.5%** (+2.8pp y/y) | **~34%** |
| GAAP operating income | $22.9m | **$72.8m** | **$72.2m** | — |
| Non-GAAP operating income | — | — | **$129.7m** (vs $13.2m) | **$600–750m** |
| GAAP operating margin | 1.6% | 3.6% | **9.6%** | — |

All **[PR]**.

**Is positive gross margin durable? Yes — with a caveat.** Bloom has now posted positive and *rising* gross margin for at least three consecutive annual periods with a consistent +1.6pp to +2.8pp cadence. This is not a one-quarter mix fluke; it is a manufacturing cost curve. The 2.8pp expansion in Q1 2026 came alongside 130% volume growth, which is exactly what genuine fixed-cost absorption looks like. **The caveat is the 34% guide:** getting from 31.5% to 34% while simultaneously commissioning a doubling of capacity is aggressive. Capacity expansions typically *depress* gross margin for two to four quarters as new lines run below yield. Management is guiding the opposite. **Treat the 34% as the single most likely place for a guidance miss.**

**Has GAAP profitability arrived? Yes, but it is thin and young.**
- Net income/(loss) attributable to common: FY2021 **–$164.5m**, FY2022 **–$301.4m**, FY2023 **–$302.1m**, FY2024 **–$88.4m**, FY2025 **+$6.0m**, Q1 2026 **+$70.7m** [3P for 2021–24; **[PR]** for FY2025 and Q1 2026].
- Q1 2026 GAAP diluted EPS **$0.23**; non-GAAP diluted EPS **$0.44** (vs $0.03 in Q1 2025) **[PR]**.

FY2025's $6.0m of net income on $2,021m of revenue is a **0.3% net margin** — statistically indistinguishable from breakeven. GAAP profitability "arrived" in FY2025 in a technical sense only. Q1 2026's $70.7m (9.4% net margin) is the first quarter where profitability is economically meaningful. **One quarter is not a trend.** The honest statement: Bloom crossed breakeven in 2025 and is in the *first* quarter of real profitability.

Note the **$0.23 GAAP vs $0.44 non-GAAP gap** — non-GAAP EPS is 1.9× GAAP. The bridge is predominantly stock-based compensation (a third-party note cites ~$139m of SBC in FY2025 [3P]). At ~$139m/yr on $2,021m of revenue, SBC is ~6.9% of revenue and **larger than FY2025's entire operating income**. The committee should price BE on GAAP or on a GAAP-plus-SBC-charged basis; the $1.85–2.25 non-GAAP EPS guide overstates economic earnings by roughly 2×.

### ROE and ROIC — the weakest part of the story

Inputs: total stockholders' equity **$768.6m at 2025-12-31** [3P]; total recourse debt **$2,598.7m** and non-recourse debt **$4.0m at 2026-03-31** [3P]; cash + equivalents + restricted cash **$2.52bn at 2026-03-31** [3P]. Total assets at 2025-12-31 **unverified** (Dec 2024 was ~$2.66bn [3P]).

| Measure | FY2025 (actual) | Q1 2026 annualised (**estimate**) |
|---|---|---|
| Net income | $6.0m | $282.8m (4 × $70.7m) |
| **ROE** | **~0.8%** | **~34%** — *not credible as a run-rate* |
| Operating income | $72.8m | $288.8m (4 × $72.2m) |
| Invested capital *incl.* cash (debt + equity) | ~$3.37bn | ~$3.44bn |
| **ROIC on total capital** | **~2.2%** | **~8.4%** |
| Invested capital *net of* cash | ~$0.87bn | ~$0.92bn |
| **ROIC net of cash** | **~8.4%** | **~31%** |

*Method: NOPAT ≈ operating income, because Bloom carries very large NOL carryforwards and pays negligible cash tax. Equity at 2026-03-31 estimated at ~$840m (2025 year-end equity plus Q1 net income and SBC); **flagged as an estimate**, not a filed figure.*

**Read:** ROE and ROIC are the metrics that most clearly say "this is early." FY2025 ROIC of ~2% on total capital is below any plausible cost of capital — Bloom **destroyed** economic value in FY2025 on an all-in-capital basis, notwithstanding the positive net income line. The Q1 2026 annualised figures look excellent, but they rest on (a) a single quarter, and (b) whether you net out $2.5bn of cash. **The cash should NOT be fully netted out** — it is earmarked working capital and capex for the 2GW ramp, not surplus. The defensible current ROIC is the ~8% total-capital figure, i.e. **roughly at, not above, cost of capital.** A ~100× forward multiple on an 8% ROIC business requires the ROIC to triple. That is the bull case in one sentence, and it is not yet in the numbers.

Equity is also **very thin relative to enterprise value**: $769m of book equity supporting a $61bn market cap = a **~80× price-to-book**. High ROE on a small equity base is a fragile construct; a single large write-down (inventory, a PPA entity, a scandium supply contract) would consume a material fraction of book equity.

---

## Cash Generation

| Period | Operating cash flow | Capex | Free cash flow |
|---|---|---|---|
| FY2024 | positive (first positive year) — **amount unverified** | unverified | unverified |
| FY2025 | **+$418.1m** **[PR]** | **unverified** | **est. +$270m to +$320m** (estimate; assumes $100–150m capex) |
| Q1 2025 | **–$110.7m** (derived: $73.6m less the stated $184.3m y/y improvement) | unverified | negative |
| Q1 2026 | **+$73.6m** **[PR]** | unverified | **unverified — likely modestly positive to modestly negative** |
| FY2026 guide | — | **$150m – $200m** [3P] | — |

**What is solid.** Bloom has now delivered **two consecutive years of positive operating cash flow** — after a decade of burn. Q1 2026's +$73.6m against Q1 2025's –$110.7m is a **$184.3m swing in a single year** and is the most important number in the cash flow story: Q1 is seasonally Bloom's weakest quarter, and it was cash-positive.

**What is not solid — earnings-to-cash bridge.** FY2025: net income $6.0m, OCF $418.1m. That $412m gap is roughly 20% of revenue. On a business shipping multi-hundred-megawatt data-centre orders, the overwhelmingly likely composition is **customer prepayments and deferred revenue**, plus ~$139m of non-cash stock comp [3P] and depreciation. **Deferred-revenue-funded operating cash flow reverses when order intake plateaus.** It is a financing of the ramp by customers, not a demonstration of cash-generative economics. Q1 2026's much tighter net-income-to-OCF relationship ($70.7m vs $73.6m) is actually the *higher-quality* datapoint of the two.

**Conversion quality:** FY2025 OCF/net income = 70×, which is meaningless at near-zero earnings. Q1 2026 OCF/net income = **1.04×** — clean, and the number to track. If Q2 2026 shows OCF materially *below* net income, that is the tell that the working-capital tailwind has turned.

**Capex is the gap in my analysis.** I could not verify FY2025 or Q1 2026 capex from any source. FY2026 guidance of $150–200m [3P] against guided revenue of $3.4–3.8bn is only ~4–5% of revenue — **remarkably low for a company doubling manufacturing capacity**, and consistent with management's claim that the 1GW→2GW Fremont expansion costs only ~$100m [3P]. If that $100m figure is accurate, Bloom's capacity expansion is unusually capital-light for heavy manufacturing and the financing-need risk is low. **If it is understated — or if capacity is being expanded via operating leases, contract manufacturers, or capitalised into inventory rather than PP&E — the reported FCF is flattered.** Verify capex and any change in the PP&E/operating-lease mix on 28 July.

---

## Balance Sheet & Debt

**As at 2026-03-31** [3P unless noted]:

| Item | Amount |
|---|---|
| Cash, cash equivalents and restricted cash | **~$2.52bn** |
| Total recourse debt | **$2,598.7m** (of which $4.0m short-term, remainder long-term) |
| Non-recourse debt (Korean JV / SK ecoplant term loans) | **$4.0m** |
| **Net debt** | **~$0.08bn — effectively net-cash-neutral** |
| Total stockholders' equity (2025-12-31) | **$768.6m** |
| Undrawn credit facility | **$600m multi-currency, Wells Fargo, secured Dec 2025** [3P] |
| **Total liquidity** | **~$3.1bn** |

### Debt profile — this is the strongest element of the story

| Instrument | Principal | Coupon | Maturity | Conversion |
|---|---|---|---|---|
| Convertible senior notes | **$2.2bn** (upsized from $1.75bn; +$300m purchaser option, i.e. **up to $2.5bn**) **[PR]** | **0.00%** — notes bear no regular interest and the principal does not accrete **[PR]** | **15 Nov 2030** **[PR]** | 5.1290 sh / $1,000 = **$194.97/share** **[PR]** |
| Other recourse debt (residual) | ~$99m (inferred: $2,598.7m total less ~$2.5bn converts) | unverified | unverified |
| Non-recourse (Korean JV) | $4.0m | unverified | unverified |
| Wells Fargo revolver | $600m committed, undrawn [3P] | unverified | unverified |

**Coverage:** with a 0% coupon on ~96% of the debt stack, **cash interest expense is de minimis**. Q1 2026 operating income of $72.2m vs net income of $70.7m implies net interest and other expense of only ~$1.5m — and that is *after* Bloom should be earning roughly $25m/quarter of interest income on $2.5bn of cash at prevailing short rates. Interest coverage is not a meaningful risk metric here. **The maturity wall is empty until Nov 2030 — 4.3 years of runway with no refinancing event.**

**Financing-need risk against the 2GW ramp: LOW.** Against ~$3.1bn of liquidity, a guided $150–200m of FY2026 capex and positive operating cash flow, Bloom does not need to raise capital to complete the 1GW→2GW expansion. **This materially de-risks the equity story** and is the single best argument for owning the balance sheet.

**But the debt was paid for in equity, and the bill is now due.** With the stock at **$214.96 versus the $194.97 conversion price, the 2030 converts are ~10% in the money.** Conversion is now the expected outcome rather than a tail scenario. At $2.5bn / $194.97, that is **~12.8m additional shares (~4.5% of current shares outstanding)** already embedded in the 319.7m diluted count. The 0% coupon was never free — it was a call option sold on Bloom's own equity, and the buyer is now in the money.

### Share-count dilution — quantified (the required analysis)

| Period | Basic weighted-avg shares | Diluted weighted-avg shares |
|---|---|---|
| FY2021 | **173m** [3P] | — |
| FY2022 | 186m [3P] (+7.5%) | — |
| FY2023 | 213m [3P] (+14.4%) | — |
| FY2024 | 227m [3P] (+6.9%) | — |
| Q1 2025 | — | **230.2m** **[PR]** |
| Current (Jul 2026) | **284.44m** shares outstanding [3P] — **+14.99% y/y** | — |
| **Q1 2026** | — | **319.7m** **[PR]** |

**Five-year dilution: 173m (FY2021) → 284.4m (Jul 2026) = +64.4% on a basic share count, a ~10.5% CAGR.** On a fully diluted basis, 173m → 319.7m = **+84.8%**.

**Year-over-year dilution: +38.9% diluted (230.2m → 319.7m), +15.0% on shares outstanding.** The y/y diluted jump is far larger than the outstanding-share jump, which is exactly what happens when (a) the 2030 converts move into the money and enter the if-converted diluted count, and (b) a large stock of employee options moves deep in the money after a 7–10× share-price move.

**Inference on the share-count jump from 227m (FY2024) to 284m (Jul 2026):** total recourse debt of $2,598.7m is almost exactly the ~$2.5bn of new 2030 converts plus ~$99m of residue. Bloom's previously outstanding 3.00% Green Convertible Notes due 2028 therefore appear to have been **converted or retired**, which with a low-$20s conversion price against a $200+ stock would have issued a substantial block of new shares. **This is an inference from the debt total, not a verified disclosure — confirm the 2028 greens' status in the Q2 10-Q.**

**Interpretation:** this is *not* pathological dilution — most of it is (i) converts converting because the stock went up 10×, and (ii) options going in the money for the same reason. That is a high-class problem. But it is real economic transfer: **an investor who bought BE in 2021 owns ~35% less of the company per share than they did then, before any of the 2026 option exercises.** Any per-share model must run off the diluted 319.7m base and assume it keeps rising.

---

## Accounting Red Flags

Ranked by how much they should move the committee's confidence.

### 1. Related-party revenue concentration — SK ecoplant (HIGH, and the top verification priority)
Reported: **related-party revenue of $288m = 55.5% of Q3 2025 total revenue**, with SK ecoplant as the counterparty [3P, extracted from the Q3 2025 10-Q; **I could not open the primary filing and this figure is UNVERIFIED**]. SK ecoplant became a related party in September 2023 with beneficial ownership of **10.5% of Class A common stock**, and has committed to purchase **500MW of Energy Servers through 2027** for ~$1.5bn of product revenue plus ~$3bn of 20-year service revenue [3P from filings]. The FY2025 10-K reportedly carries **$13.9m of deferred profit on transactions with unconsolidated affiliates** at 2025-12-31 [3P], and there is **non-recourse term-loan debt between the Korean JV and SK ecoplant** [3P].

**Why this matters more than it looks.** Revenue recognised on sales to an entity that owns 10.5% of you, financed partly by loans within the same structure, with deferred profit eliminations, is the highest-judgement revenue a hardware company can book. It is also **structurally the same family of issue as the 2020 restatement**. If the 55.5% figure is correct, more than half of a quarter's revenue rests on related-party judgement. **Action: 巴爺爺 or the committee must open the Q3 2025 10-Q and the FY2025 10-K related-party footnote directly and confirm or refute this number before any position is sized.**

### 2. Restatement history and live short-seller allegation (HIGH, unresolved)
Per Dept. 4's regulatory brief (`reports/news/2026-07-19-regulatory-be.md`): Bloom **restated FY2018–Q3 2019 financials on 12 Feb 2020** over **Managed Service Agreement accounting**, following the Sept 2019 Hindenburg report; the securities class action settled for $3.0m with final approval 6 May 2024. On **8 July 2026 Hunterbrook** published a report alleging understated China dependence for scandium oxide (~220t needed to reach 5GW vs ~240t global supply); Bloom filed an **8-K on 9 July 2026** rebutting the claims as "false and misleading." **Rosen Law and Kessler Topaz have opened securities class-action investigations** (no complaint filed as of the reference date).

**Accounting-analyst read:** the scandium allegation is primarily a *supply-chain and disclosure* claim, not a revenue-recognition claim — but a company with a prior restatement over accounting judgement has **no credibility buffer**. The financially dangerous vector is the one Dept. 4 identified: if the China-sourcing claim is directionally true, it collides with **48E FEOC "material assistance" restrictions phasing in from 2026**, which could impair *customers'* 30% ITC eligibility. That would hit **pricing, demand, and — critically — the collectability and revenue-recognition assumptions on contracts already booked.** An ITC-eligibility failure is a contract-modification and variable-consideration event, i.e. it lands in revenue, not just in the narrative.

### 3. Disputed FY2025 operating cash flow (MEDIUM-HIGH, unresolved conflict — flagging explicitly)
The company reports **FY2025 OCF of $418.1m** **[PR]**. A third-party research note (Sheephill Group, initiating coverage) instead states **"operating cash flow of $114m in FY2025, almost entirely composed of non-cash add-backs: $139m in stock-based compensation and $111m in debt-related charges,"** and **"free cash flow excluding stock-based compensation was negative $82m in FY2025"** [3P]. **I could not reconcile these two figures** — Sheephill may be using a different definition, a different period, or may simply be wrong; equally, the company figure may include a working-capital release Sheephill strips out. **I am recording this as an unresolved conflict rather than picking a side.** Under the desk rule "cash flow over reported earnings," a dispute *about the cash flow figure itself* is a serious issue. **Resolve by pulling the FY2025 10-K consolidated statement of cash flows directly.**

Regardless of who is right, the qualitative point stands: **if $139m of SBC is a large share of OCF, then OCF materially overstates economic cash generation**, because SBC is a real cost paid in the dilution documented above.

### 4. GAAP vs non-GAAP gap (MEDIUM)
Q1 2026 non-GAAP diluted EPS of **$0.44 is 1.9× GAAP $0.23**; non-GAAP operating income of **$129.7m is 1.8× GAAP $72.2m** **[PR]**. A ~$57.5m quarterly add-back on $751m of revenue (7.7% of revenue) is large. Full-year guidance is issued **exclusively in non-GAAP terms** ($600–750m operating income, $1.85–2.25 EPS, ~34% gross margin) with **no GAAP guidance provided** — a presentational choice that deserves note. The committee should haircut the guided EPS by roughly half to reach a GAAP-equivalent.

### 5. Complex PPA / unconsolidated-affiliate structures (MEDIUM, structural)
Bloom continues to operate PPA entities and unconsolidated affiliates (the $13.9m deferred-profit line, the Korean JV, non-recourse project debt). These structures are where the 2020 restatement originated. Their current scale is **unverified** in this report — I could not open the consolidation footnote. **Track: any change in consolidation conclusions, any new VIE, any growth in non-recourse debt.**

### 6. Receivables / inventory vs revenue (NOT ASSESSED — data gap)
**I could not obtain accounts receivable or inventory balances for any period.** With revenue growing 130% y/y, receivables and inventory growth versus revenue growth is one of the most diagnostic tests available for a hardware scale-up, and **it is missing from this analysis.** DSO expansion would signal channel/customer stress; inventory outgrowing revenue would signal a demand air-pocket ahead of the 2GW ramp. **This is the largest hole in the report and must be closed with the Q2 10-Q.**

### 7. Off-balance-sheet capacity financing (LOW-MEDIUM, watch)
The claim that 1GW→2GW of capacity costs only ~$100m [3P], with FY2026 capex guided at $150–200m on $3.4–3.8bn of revenue, is unusually capital-light. **Check whether capacity is being added through operating leases, contract manufacturing, or supplier-funded tooling** — legitimate strategies, but they move cost off the capex line and flatter free cash flow.

### 8. Backlog vs commitments language (LOW-MEDIUM, watch)
The Brookfield relationship is variously described as a **$5bn partnership** and a **$25bn commitment** (expanded 30 June 2026). **A commitment/framework is not backlog and is not revenue.** Confirm what portion, if any, sits in contracted backlog with take-or-pay terms versus a non-binding MOU. Any model built off $25bn is building off a press release.

**No red flag was found in:** share-count creep (large, but explained by conversion and option exercise after a 10× move, not by serial ATM issuance); debt maturity risk (none until 2030); interest coverage (immaterial cash interest); or earnings-vs-cash divergence *at the quarterly level* (Q1 2026 OCF/NI = 1.04×, clean).

---

## Financial Score: **67 / 100**

Input to the Investment Committee scorecard.

| Component | Weight | Score | Rationale |
|---|---|---|---|
| Revenue growth & durability | 20 | **17** | +130% y/y, guide implies +68–88% FY26. Docked because the 10-year base rate is ~10–12% and the acceleration is a demand shock, not an execution change — high level, low proven durability. |
| Margin quality & trajectory | 20 | **15** | Genuinely improving: GAAP GM 27.5%→29.0%→30.0%, three periods of consistent +1.6–2.8pp expansion. Docked for the aggressive ~34% FY26 guide during a capacity doubling, and for the 1.9× non-GAAP/GAAP gap. |
| Returns on capital (ROE/ROIC) | 20 | **9** | The weak link. FY2025 ROE ~0.8%, ROIC on total capital ~2.2%. Even Q1 2026 annualised is only ~8.4% ROIC on total capital — at, not above, cost of capital. ~80× price-to-book on $769m of book equity is fragile. |
| Cash generation & FCF | 15 | **10** | Two consecutive positive OCF years and a $184.3m y/y Q1 swing are real achievements. Docked hard for the unresolved $418.1m-vs-$114m FY2025 OCF dispute, unverifiable capex, and an FY2025 earnings-to-cash bridge that is probably working-capital-funded. |
| Balance sheet & debt | 15 | **13** | Best-in-class: ~$2.52bn cash, ~net-debt-zero, **0% coupon**, no maturity until Nov 2030, $600m undrawn revolver, ~$3.1bn liquidity. Financing-need risk for the 2GW ramp is LOW. Docked only for thin book equity and in-the-money convert dilution. |
| Accounting quality & disclosure | 10 | **3** | 2020 MSA restatement; reported >55% related-party revenue concentration in a recent quarter (unverified but credible); live short-seller report with two class-action investigations open; complex PPA/affiliate structures; guidance given only in non-GAAP; and I could not verify AR/inventory at all. **This is the lowest sub-score and it is deliberate.** |
| **Total** | **100** | **67** | |

**Score interpretation.** 67 is a **"good business, unproven returns, compromised disclosure confidence"** profile. The operating and balance-sheet halves of Bloom would score in the low-80s standalone; the returns-on-capital and accounting-quality halves drag it to the high-60s. Note that the score assesses **fundamentals quality, not valuation** — at ~16–18× EV/Sales and ~100× forward non-GAAP EPS, a 67 fundamentals score provides no margin of safety whatsoever. That judgement belongs to 𢦀鳩仔 and the committee.

**Conditions that would move the score:**
- **Up to ~78:** Q2 confirms related-party revenue is well below 30% of total; capex and AR/inventory verify clean; OCF ≥ net income again; GM holds ≥31%.
- **Down to ~45 or below:** confirmation that related-party revenue exceeds 50% of a quarter; any restatement, auditor change, material-weakness disclosure, or SEC comment letter; a filed class-action complaint with specific accounting allegations; or FEOC guidance that impairs customer ITC eligibility on booked contracts.

---

## Verification Queue for 28 July 2026 (Q2 results)

Priority order for whoever covers the print:
1. **Related-party revenue as % of total** (Q2 and 1H) — decides the grade.
2. **Consolidated statement of cash flows**: FY2025 comparative OCF, SBC, and the working-capital lines — resolves the $418.1m/$114m dispute.
3. **Capex** (actual Q2 and 1H) and any shift toward operating leases or contract manufacturing.
4. **Accounts receivable and inventory** vs revenue growth — the untested diagnostic.
5. **Gross margin** vs the ~34% FY26 guide, and whether the Fremont ramp is compressing it.
6. **Diluted share count** and status of the 2028 Green Converts.
7. **Any change to scandium / supply-chain / FEOC disclosure language**, and any new risk factor or legal-proceedings addition.
8. **Contracted backlog** vs the Brookfield "commitment" figures.

---

## Sources

**Price / market data**
- Bloom Energy (BE) overview & statistics — stockanalysis.com: https://stockanalysis.com/stocks/be/ · https://stockanalysis.com/stocks/be/statistics/
- Market cap — companiesmarketcap: https://companiesmarketcap.com/gbp/bloom-energy/marketcap/ · capital.com: https://capital.com/en-int/markets/shares/bloom-energy-corporation-share-price/market-cap
- CNBC quote: https://www.cnbc.com/quotes/BE · CNN: https://www.cnn.com/markets/stocks/BE
- 52-week range / 1-yr return: https://financhill.com/stock-forecast/be-stock-prediction · https://stockinvest.us/stock/BE
- Macrotrends market cap / shares outstanding: https://www.macrotrends.net/stocks/charts/BE/bloom-energy/market-cap · https://www.macrotrends.net/stocks/charts/BE/bloom-energy/shares-outstanding
- 24/7 Wall St (21 Jul 2026), "+140% YTD": https://247wallst.com/investing/2026/07/21/prediction-up-140-ytd-does-bloom-energy-have-more-room-to-run/

**Company filings & releases (primary, accessed via search extraction — direct fetch 403'd)**
- Q1 2026 8-K earnings exhibit: https://www.sec.gov/Archives/edgar/data/0001664703/000162828026027913/ex991_q126financialresults.htm · supplemental: https://www.sec.gov/Archives/edgar/data/0001664703/000162828026027913/ex992_q126supplementalde.htm
- Q1 2026 10-Q: https://www.sec.gov/Archives/edgar/data/0001664703/000162828026028021/be-20260331.htm
- Q1 2026 press release: https://investor.bloomenergy.com/press-releases/press-release-details/2026/Bloom-Energy-Reports-Record-First-Quarter-2026-Results-and-Raises-Full-Year-2026-Guidance/default.aspx · https://www.businesswire.com/news/home/20260428374369/en/Bloom-Energy-Reports-Record-First-Quarter-2026-Results-and-Raises-Full-Year-2026-Guidance
- FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm
- Q4/FY2025 8-K exhibit: https://www.sec.gov/Archives/edgar/data/1664703/000162828026005798/ex991_q42025financialresul.htm · press release: https://investor.bloomenergy.com/press-releases/press-release-details/2026/Bloom-Energy-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results-with-Record-Full-Year-Revenues/default.aspx
- Q3 2025 10-Q: https://www.sec.gov/Archives/edgar/data/1664703/000162828025046844/be-20250930.htm
- FY2024 10-K/ARS: https://www.sec.gov/Archives/edgar/data/1664703/000162828025016212/a202410kars.pdf
- Convertible notes pricing (0%, due 2030, $194.97 conversion): https://investor.bloomenergy.com/press-releases/press-release-details/2025/Bloom-Energy-Corporation-Prices-Upsized-2-2-Billion-Convertible-Senior-Notes-Offering/default.aspx · Latham: https://www.lw.com/en/news/2025/10/latham-represents-bloom-energy-in-upsized-convertible-senior-notes-offering · Davis Polk: https://www.davispolk.com/experience/bloom-energy-25-billion-convertible-senior-notes-offering
- Q1 2026 earnings call transcript: https://www.fool.com/earnings/call-transcripts/2026/04/28/bloom-energy-be-q1-2026-earnings-transcript/ · Q4 2025: https://www.fool.com/earnings/call-transcripts/2026/02/05/bloom-energy-be-q4-2025-earnings-call-transcript/

**Third-party analysis [3P]**
- Sheephill Group initiating coverage (disputed OCF/FCF figures): https://sheephillgroup.com/research-bloom-energy
- Panabee Q3 2025 (related-party revenue 55.5%): https://www.panabee.com/news/bloom-energy-earnings-q3-2025
- Investing.com Q1 2026 slides: https://www.investing.com/news/company-news/bloom-energy-q1-2026-slides-revenue-surges-130-guidance-raised-93CH-4643316
- Simply Wall St past performance: https://simplywall.st/stocks/us/capital-goods/nyse-be/bloom-energy/past
- Utility Dive 2GW capacity: https://www.utilitydive.com/news/bloom-energy-says-its-on-track-for-2-gw-annual-production-capacity/804291/
- CNBC on the AI data-centre power trade: https://www.cnbc.com/2026/01/11/bloom-energy-ai-data-center-power-stock-bubble.html
- Hunterbrook report (8 Jul 2026): https://hntrbrk.com/investigations/bloom

**Internal**
- `reports/news/2026-07-19-regulatory-be.md` — The dictator (Dept. 4), restatement history, Hunterbrook, 48E/FEOC linkage.

---
*Research and decision support only — not financial advice. Committee and Owner decide.*

---

<!-- provenance-stamp -->
## Provenance and coverage

*Appended by `scripts/stamp_provenance.py`. Records how this report was
produced, so its weight can be judged later without reconstructing the
conditions from memory.*

**Sourcing.** This report predates 2026-07-30, when the environment's
HTTP 403 egress restriction was first observed and verified. Whether
direct page fetch was available when this was written **was not recorded
at the time**, so no claim is made either way — rely on the sourcing
stated in the body of the report itself.

**Coverage gap — no quantitative input.** Department 3 (Quant Research:
賭馬狗, Math King, Tom, AI指標) filed **nothing** on this name. Session
limits forced the pipeline down to a three-agent core and quant was cut
first, without being logged as a gap at the time. Any conclusion here
rests on fundamentals, valuation, news and technicals only.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
