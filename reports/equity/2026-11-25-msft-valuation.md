# MSFT: Microsoft Corporation, Valuation

**Analyst:** 𢦀鳩仔 (Dept 2, Equity Research, Valuation)
**Date:** 2026-11-25 (written 2026-11-25/26) · **First MSFT valuation in firm history**
**Price reference:** **US$496.13**, close 2026-11-24 (Webull daily bar, via `reports/technical/2026-11-25-msft-technical.md`). That bar is unadjusted for the 19 Nov ex-dividend.
**Position context:** none. MSFT is on the watchlist (`ai:` sleeve) and is not held.
**Status:** COMPLETE.
- Income statement, cash flow and balance sheet are **primary** (microsoft.com IR pages opened by 巴爺爺).
- Leases, OpenAI revenue and receivables, and the OpenAI stake are **search extractions of the 10-Q/10-K** (`sec.gov` DNS-blocked).
- Peer multiples are search extractions from mixed vendors and dates.
- `tradingkey.com` was not used.

---

## 0. Bottom line

| Item | Value |
|---|---|
| **Fair value range** | **US$340–450 per share** |
| **Central fair value (target)** | **US$400** |
| DCF (FCF, explicit capex incl. finance leases), probability-weighted 25/50/25 | **US$344** (bear $122 · base $346 · bull $564) |
| Owner-earnings method (normalised maintenance capex + growth reinvestment at RONIC), weighted | US$338 (bear $117 · base $339 · bull $554) |
| Relative (forward P/E and EV/EBITDA vs megacap software and hyperscalers) | US$370–520, central US$460 |
| **Margin of safety at US$496.13** | **−24%** against the US$400 central. −10% against the top of the range. **+12% against the bull DCF.** |
| **What the price implies** | On base cash flows, an **IRR of ~7.4%** (9.7% on bull cash flows), against a 4.90% Treasury and my 9.0% WACC. To justify US$496 at 9%, you need one of: revenue CAGR of **~12.8% for ten years** (base 8.9%); **perpetual capex of ~7% of revenue** (FY24 actual 18.1%, TTM 39.2%); or a **flat EBITDA margin of ~76%** (TTM 59%). Only the first is plausible. |
| Required margin of safety (菲比斯, Wide/narrowing) | 20%. The implied buy level is **≤ US$320** |
| **Valuation score for committee** | **38 / 100** |

**The three assumptions the answer is most sensitive to:**
1. **Steady-state capex intensity** (capex incl. finance leases, % of revenue). The bull or bear capex path moves value **+10% / −23%**. The 14% → 35% perpetual grid spans **US$408 → US$206** at a 60% EBITDA margin.
2. **The discount rate.** ±0.5pt moves value **−9% / +11%**.
3. **Ex-OpenAI revenue growth.** ±2pt a year moves value **+17% / −14%**.

Next in line: terminal RONIC (−8% at 12%) and the uncommenced leases' PV treatment (−4% at full nominal).

---

## 1. Fair value range and target price

| Method | Low | Central | High | Note |
|---|---|---|---|---|
| **FCF DCF, probability-weighted** | 313 (WACC 9.5%) | **344** (9.0%) | 382 (8.5%) | §5 and §9 |
| Owner-earnings method (cross-check) | — | 338 | — | §6. Agrees with the FCF DCF within 2%. |
| **Relative** | 370 | **460** | 520 | §7: P/E 18–28× on FY27 EPS of ~US$19.9; EV/EBITDA 14–19× TTM after leases |
| **Blend (50/50, firm precedent)** | **342 → 340** | **402 → 400** | **451 → 450** | Rounded; ranges, not points |

**Target price: US$400** (central intrinsic estimate; **not a 12-month forecast**). The intrinsic and relative methods disagree by ~25%. The reason is explained in §8 before the blend.

---

## 2. Inputs and data provenance

**Tags:**
- **[P]** primary microsoft.com, via 巴爺爺
- **[S]** search extraction of a filing, via a firm report
- **[W]** my web search, dated (search extraction, no page opened)
- **[C]** arithmetic
- **[E]** estimate
- **[A]** analyst assumption

| Input | Value | Tag / source |
|---|---|---|
| Revenue: FY26 / TTM / Q1 FY27 | US$331,839M / US$346,445M / US$92,279M (+18.8%) | [P] financials update §2 |
| Q2 FY27 guide | Revenue US$96.0–97.1B; operating margin "down slightly YoY"; capex ">US$50B"; ETR ~20% | [P] §9 |
| Operating income TTM; operating margin | US$163,191M; 47.1% (Q1 49.8%) | [P/C] |
| D&A and other: TTM / Q1 | US$42,131M / US$11,744M (+44% YoY; run-rate US$47.0B) | [P/C] |
| **EBITDA TTM** | **US$205.3B (59.3% of revenue)** | [C] operating income + D&A |
| OCF / cash capex / **FCF**, TTM | US$195,878M / US$135,921M / **US$59,957M** | [P/C] |
| Q1 capex incl. finance leases | US$45.2B (finance leases US$7.4B) | [P] call |
| CY26 capex | ~US$170B (supply-delayed, not cut) | [P] |
| SBC TTM | US$12,556M; FCF − SBC US$47,401M | [P/C] |
| Cash + STI / bonds, 30 Sep 2026 | US$64,509M / US$35,481M → **net cash ex-leases US$29,028M** | [P/C] |
| **Finance lease liabilities** | **US$62,304M at 30 Jun 2026** (Sep NOT OBTAINED; likely higher after US$7.4B of Q1 additions) | [S] |
| Operating lease liabilities (long-term) | US$21,719M, 30 Sep 2026 (current portion NOT OBTAINED) | [P] |
| **Leases signed, not commenced** | **US$329.1B at 30 Jun 2026**; commence FY27–FY33; 1–20-year terms; nominal | [S] FY26 10-K extraction |
| Net PP&E | US$313,076M (30 Jun 2026); US$346,844M (30 Sep 2026) | [P] |
| **Shares** | **7,446M diluted weighted, Q1 FY27** (basic 7,426M). Diluted −0.27% YoY. **Period-end count NOT OBTAINED.** | [P] |
| **OpenAI revenue** | **US$10.0B in Q1 FY27 = 10.8% of revenue**; receivables US$7.2B | [S] 10-Q via secondary |
| OpenAI share of RPO | ~45% of US$625B (Dec 2025 disclosure); no update since | [S] news refresh B3.2 |
| **OpenAI stake** | ~24% as-converted (10-Q via secondary, financials §7) vs ~27% (news refresh; Mar 2026 10-Q). **Conflicting.** Equity method, HLBV. | [S] |
| OpenAI valuation | **US$852B post-money** (round closed 31 Mar 2026, CNBC). A round reported at **US$1.25T** (Nov 2026, Benzinga citing CNBC; **not closed or confirmed**) | [W] CNBC 2026-03-31; Benzinga, Nov 2026 |
| Non-GAAP EPS TTM / GAAP EPS TTM | ~US$18.04 / ~US$19.15 (GAAP includes +US$8.3B of OpenAI marks) | [P/C] |
| FY27 consensus EPS | US$19.53–20.39 (sources conflict) | [CONS] financials §12 |
| Sell-side | ~US$632 average (TipRanks, 39 analysts; range 440–750) | [F] news refresh B3.8 |
| 10-year Treasury | **4.90%**, 24 Nov 2026 close | [W] Investing.com / MND / Longbridge |
| ERP | **4.41%** Damodaran implied, 1 Nov 2026 (**garbled snippet; unverified**) | [W] |
| Beta | **1.04** (Yahoo 5-year monthly, ~Nov 2026; single source) | [W] |
| Moat | Wide, narrowing, 74/100; **MoS 20%, conditional on the capex treatment**; binding guidance in §13 of that report | [F] 菲比斯 2026-08-21 |

---

## 3. Assumptions table (the audit trail)

US$B. Fiscal years end in June.
- **FY27 is weighted 0.75**, because Q1 is already in the 30 Sep balance sheet. It is discounted at t = 0.30.
- FY28–FY36 are discounted mid-year.
- The explicit period is 10 years, then a terminal value.
- **The same WACC (9.0%) is used in every scenario.** The rate is varied in §9.

| # | Assumption | Bear (25%) | **Base (50%)** | Bull (25%) | Basis |
|---|---|---|---|---|---|
| A1 | FY27 revenue growth | +16% | **+17% (US$388B)** | +18% | [C/A] Q1 +18.8%, Q2 guide +18–19%; consensus US$383–391B |
| A2 | **OpenAI revenue** (10.8% of FY27), growth FY28 → FY36 | **−25%, −35%**, then 0–2% (falls to ~US$20B: lost IP access or multi-cloud) | +15%, +10%, +5%, then +3% | +25% fading to +4% | [S] 10.8% share; "prepare for loss of OpenAI IP" (19 Nov) [F news]; OpenAI can serve any cloud [F news] |
| A3 | Ex-OpenAI revenue growth FY28 → FY36 | 10 → 4% | **14, 12, 10, 9, 8, 7, 6, 5, 4%** | 16 → 6% | [A] Azure +48% on a ~36% revenue share today; M365 commercial +17%; Windows OEM −22% |
| A4 | EBITDA margin (after SBC; **excludes rent on the uncommenced leases**, which are deducted as debt, A9) | 59% → 55% | **60%** | 61% → 62% | [C] TTM 59.3%; Q2 guide has margin down slightly; gross-margin erosion vs opex leverage |
| A5 | **Capex incl. finance leases, % of revenue**, FY27 → FY36 | 53, 47, 42, 38, 35, 33, 32, 31, 30, 30% | **52, 42, 34, 28, 24, 22, 20, 19, 18, 18%** | 50, 38, 29, 22, 18, 16, 15, 15, 15, 15% | [P/E] FY27 base US$202B (Q1 45.2 + Q2 >50 + H2 accelerating). FY24 capex/revenue 18.1%; TTM 39.2% (cash). **Scenario pair per 菲比斯 §13.2: bull normalises to mid-teens; bear stays ≥30%.** |
| A6 | D&A rate (on opening net PP&E + ½ capex) | 14.5% | **13.0%** | 12.5% | [C] FY27 base D&A US$54B vs Q1 run-rate US$47B and +44% YoY. ~¾ of capex is short-lived kit [P]. |
| A7 | Cash tax | 20% | **20%** | 20% | [P] Q2 guide ~20%; TTM 19.7% |
| A8 | ΔNWC | 0 | 0 | 0 | [A] Unearned revenue funds receivables (structural; financials §8.1) |
| A9 | **Debt-like: finance leases + operating leases + uncommenced leases** | 62.3 + 21.7 + **100% × 329.1** | 62.3 + 21.7 + **65% × 329.1 (PV) = US$298B** | 62.3 + 21.7 + 50% × 329.1 | [S/P/A] 65% ≈ PV of the nominal payments: average start ~FY29–30, ~15-year average life, 5.5% discount [E]. The bear treats nominal as debt (commitments run beyond the PV horizon, and cancellation terms are unknown). |
| A10 | **OpenAI equity stake** (added as a non-operating asset) | **US$100B** | **US$150B** | **US$300B** | [W/S/A] 24% × US$852B ≈ US$204B; base haircut ~25% for illiquidity, preference/HLBV structure and counterparty circularity [A]. Bull = 24% × US$1.25T (unconfirmed round). Bear = down-round or restructuring. |
| A11 | Net cash ex-leases | 29.0 | 29.0 | 29.0 | [C/P] |
| A12 | **Shares** | 7,446M | **7,446M, flat** | 7,446M | [P] SBC is expensed inside EBITDA, so buybacks that offset dilution are the cash settlement of a cost already charged. Diluted −0.27% YoY confirms the offset. No net-buyback accretion is modelled. |
| A13 | **WACC** | 9.0% | **9.0%** | 9.0% | [C] CAPM: 4.90% + 1.04 × 4.41% = **9.49%** cost of equity. With leases and bonds as debt (US$333B, 8.3% weight) at ~4.5% after tax [A: AAA spread ~0.7pt], WACC = **9.07%**, rounded to 9.0%. GuruFocus 12.06% (Jun 2026) [F moat] is not used: its inputs were not verified. |
| A14 | Terminal growth / RONIC | 2.5% / 12% | **3.0% / 20%** | 3.5% / 28% | [A] Reinvestment = g/RONIC. ROIC is ~26% today and falling [F]. The bear assumes AI infrastructure earns barely above WACC. |
| A15 | Owner-earnings method: maintenance capex / RONIC on growth | 1.30 × D&A / 15% | **1.10 × D&A / 25%** | 1.00 × D&A / 35% | [A] §6 |
| — | Probabilities | 25% | **50%** | 25% | [A] |

**Not in the model:**
- The **Anthropic stakes** (up to US$5B, plus ~US$1B in the Nov 2026 placement [F news]): ≤ ~US$0.8/share.
- **The voluntary-exit charge** (unquantified; a one-off).
- **Other income.** Valuation is on operating income, which removes the HLBV OpenAI marks, per moat guidance #1.

---

## 4. How the mandated items are handled

### 4.1 FCF depressed by capex vs strong operating earnings: valued on both, with explicit normalised capex
- **Reported FCF basis.** TTM FCF of US$60.0B is a **1.62% yield** on a US$3,694B market cap (1.28% after SBC). That is **61.6× P/FCF**. Capitalising it implies a value near US$100–150/share. **That is wrong**, because ~US$135.9B of capex is building capacity for growth, not maintaining it.
- **Owner-earnings basis (normalised capex).** NOPAT US$130.6B (TTM operating income × 0.8) + D&A US$42.1B − **maintenance capex 1.10 × run-rate D&A of US$47.0B = US$51.7B** gives **TTM owner earnings ≈ US$121B, a 3.28% yield (30.5× P/OE)** [C]. The range across maintenance assumptions (1.0–1.3× D&A) is US$112–126B, a 3.0–3.4% yield.
- **The DCF does not pick one.** It carries the actual capex path (A5) through FY36, and the owner-earnings method (§6) replaces management's capex with maintenance plus RONIC-disciplined growth capex. **The two agree within 2% (US$346 vs US$339 base).** **Normalised capex in the terminal year is 18% of revenue in the base, 15% in the bull and 30% in the bear** (A5).
- **No-growth anchor.** TTM owner earnings of US$121B ÷ 9%, plus net cash and the OpenAI stake, less leases ≈ **US$165/share**. **Growth must supply ~67% of today's price** [C].

### 4.2 Finance leases and the US$329B of uncommenced leases as debt
| Debt-like item | Base | Per share |
|---|---|---|
| Finance leases (30 Jun 2026; Sep NOT OBTAINED) | US$62.3B | −US$8.4 |
| Operating leases, long-term (30 Sep 2026) | US$21.7B | −US$2.9 |
| **Uncommenced leases at 65% PV of US$329.1B nominal** | **US$213.9B** | **−US$28.7** |
| **Total deducted** | **US$298B** | **−US$40.0** |

- **Consistency:** EBITDA (A4) **excludes** the rent these leases will carry once they commence, so the capacity's cost is charged once, as debt. The revenue that capacity produces is inside the growth path.
- Treating the nominal US$329B as debt (bear) costs a further **−4%**; 50% PV (bull) gives **+2%**.
- If finance leases at 30 Sep were ~US$69.7B (June plus Q1 additions, before repayments), that is **−US$1.0/share**.
- **Including the uncommenced PV, EV/EBITDA rises from 17.9× to 19.3×** (§7).

### 4.3 OpenAI: revenue concentration (10.8%) and the equity stake
- **Revenue:** OpenAI is a **separate revenue line** from FY27 (US$42B base). In the **bear it falls ~50% over two years** (to ~US$20B), while the capex path stays high. **Losing the customer does not cancel the data centres.** The bull or bear OpenAI path alone moves value **+5% / −6%**. The concentration matters more as a **correlation** with the bear capex and RONIC assumptions than on its own, which is why those three move together in the bear scenario.
- **Stake:** added at **US$150B base (US$20/share)**, US$100B bear, US$300B bull. US$300B vs US$100B moves value **+6% / −2%**. **GAAP equity-method marks (HLBV) are excluded** from earnings, so the stake is not counted twice.
- The ~45% share of RPO (Dec 2025) is why **the US$677B RPO headline is not used** as a growth input (moat guidance #6).

### 4.4 Share count
- 7,446M diluted weighted (Q1 FY27) [P]. The period-end count was not obtained.
- At US$496.13 that is a **US$3,694B** market cap.
- Held flat for the reasons in A12. Using the basic 7,426M instead would add +0.3%, which is immaterial.

### 4.5 Moat-analyst conditions on the 20% MoS (菲比斯 §13)
| # | Condition | Met? |
|---|---|---|
| 1 | Non-GAAP / strip other income | **Yes.** The model is built on operating income; other income and OpenAI marks are excluded. |
| 2 | Capex scenario pair: mid-teens bull vs >30% bear | **Yes.** A5 and the §9.3 grid. |
| 3 | Server-life stress (revert to ~5 years; show the operating-income effect) | **Yes, as a proxy.** Raising the D&A rate from 13.0% to 14.5% lowers base operating income by **US$6.2B (−3.5%) in FY27 and US$7.4B (−3.8%) in FY28**. The effect on value is only **−1%**, because depreciation affects cash only through tax. **The economic server-life question is the replacement-capex level, which is condition 2.** |
| 4 | Value the software franchise and the AI infrastructure separately | **Not possible on current disclosure.** The Sept 2026 segment change removed the Intelligent Cloud margin [F]. Proxy: the capex/EBITDA grid (§9.3) is in effect the value of the infrastructure business at different returns. |
| 5 | Haircut the AI run-rate | **Yes:** the separate OpenAI line with a bear collapse |
| 6 | Don't use the RPO headline | **Yes:** not used |

---

## 5. DCF: scenario results

| Scenario | Prob | PV FCFF FY27–36 | PV terminal | TV % of EV | EV | Leases (debt-like) | OpenAI stake | Equity | **US$/share** |
|---|---|---|---|---|---|---|---|---|---|
| Bear | 25% | 379 | 813 | 68% | 1,193 | −413 | +100 | 909 | **122** |
| **Base** | **50%** | 926 | 1,766 | 66% | 2,692 | −298 | +150 | 2,573 | **346** |
| Bull | 25% | 1,313 | 2,806 | 68% | 4,119 | −249 | +300 | 4,199 | **564** |
| **Probability-weighted** | | | | | | | | | **344** |

Equity = EV + US$29.0B net cash − leases + OpenAI stake. Terminal value is 66–68% of EV. That is acceptable for an **undated** moat (unlike BeOne).

**Base path (US$B):**

| FY | Revenue | of which OpenAI | EBITDA % | D&A | EBIT % | NOPAT | Capex incl. finance leases | Capex % | FCFF |
|---|---|---|---|---|---|---|---|---|---|
| FY27 | 388 | 42 | 60% | 54 | 46.1% | 143 | 202 | 52% | −5 |
| FY28 | 443 | 48 | 60% | 72 | 43.7% | 155 | 186 | 42% | 41 |
| FY29 | 495 | 53 | 60% | 86 | 42.7% | 169 | 168 | 34% | 86 |
| FY30 | 542 | 56 | 60% | 95 | 42.4% | 184 | 152 | 28% | 127 |
| FY31 | 588 | 57 | 60% | 102 | 42.6% | 200 | 141 | 24% | 161 |
| FY32 | 632 | 59 | 60% | 107 | 43.1% | 218 | 139 | 22% | 186 |
| FY33 | 674 | 61 | 60% | 111 | 43.5% | 235 | 135 | 20% | 211 |
| FY34 | 712 | 63 | 60% | 114 | 44.0% | 251 | 135 | 19% | 229 |
| FY35 | 746 | 65 | 60% | 117 | 44.4% | 265 | 134 | 18% | 247 |
| FY36 | 776 | 67 | 60% | 119 | 44.6% | 277 | 140 | 18% | 257 |

**Checks:**
- **FY27 FCFF of −US$5B** includes ~US$28B of finance leases. **On management's cash-capex basis, FY27 FCF is ≈ +US$23B**, consistent with "remain FCF positive in FY27" [P].
- **FY27E non-GAAP EPS ≈ US$19.2** vs consensus US$19.5–20.4. That is **1.5–6% below the street**. The base operating margin of 46.1% sits below Q1's 49.8% and the guided "down slightly" from 47.1% in Q2. It is a mildly bearish choice, disclosed in §12.
- **Operating margin falls to ~42–43% in FY29–31** as D&A catches up with capex, then recovers to 44.6%. That is the August "depreciation wave" thesis, in numbers.

**Bear (US$122):**
- Revenue reaches US$607B by FY36 (5.5% CAGR).
- OpenAI shrinks to US$20B.
- EBITDA margin falls to 55%.
- **Capex stays ≥30% of revenue**, so EBIT margin drops to ~31% and FY36 FCFF is US$115B.
- Uncommenced leases at full nominal; RONIC 12%.

This is the "AI infrastructure earns utility returns" world.

**Bull (US$564):**
- Revenue reaches US$963B (11.2% CAGR).
- EBITDA margin 62%.
- Capex normalises to 15% by FY33, so EBIT margin is ~50% and FY36 FCFF is US$355B.
- RONIC 28%; OpenAI stake US$300B.

---

## 6. Owner-earnings method (cross-check on normalised capex)

Cash flow = NOPAT + D&A − (maintenance × D&A) − NOPAT × (next-year growth ÷ RONIC on growth investment). Same revenue, margin and terminal value as the DCF. **Management's capex path is replaced by a return-disciplined reinvestment rule.**

| Scenario | Maintenance capex | RONIC on growth | US$/share | vs FCF DCF |
|---|---|---|---|---|
| Bear | 1.30 × D&A | 15% | 117 | −4% |
| **Base** | **1.10 × D&A** | **25%** | **339** | −2% |
| Bull | 1.00 × D&A | 35% | 554 | −2% |
| **Weighted** | | | **338** | −2% |

**Agreement within 2% means the capex path in A5 is consistent with ~25% returns on growth investment.** The DCF is not hiding a capex assumption that the returns cannot support.

---

## 7. Comparables

### 7.1 MSFT at US$496.13
| Multiple | Value | Basis |
|---|---|---|
| Market cap | **US$3,694B** | 7,446M diluted [C] |
| EV ex leases / incl. recognised leases / incl. uncommenced PV | US$3,665B / US$3,749B / US$3,963B | [C] |
| **EV/EBITDA, TTM** (US$205.3B) | **17.9×** ex leases · 18.3× incl. recognised leases · **19.3×** incl. uncommenced PV | [C] |
| EV/EBITDA, FY27E (US$233B) | 15.7× / 16.1× | [C] base |
| **P/E** | **27.5×** TTM non-GAAP (US$18.04) · 25.9× GAAP · **24.3–25.4× FY27 consensus** | [C] |
| **FCF yield** | **1.62%** reported · 1.28% after SBC · **3.28% owner earnings** · dividend 0.79% | [C] |

### 7.2 Peers (search extractions, mixed dates and vendors, Tier-3)
| Peer | Fwd P/E | EV/EBITDA | FCF yield | Source / date |
|---|---|---|---|---|
| **Alphabet** (US$279.05 close 24 Nov; mkt cap US$3.43T) | 19.0–28.1× (vendors conflict) | 15.1× (LTM, Oct 2026) to 18.7× (29 Oct 2026) | **0.55–1.34%** (FinanceCharts, Oct–Nov 2026) | Gotrade 24 Nov; stockanalysis via search; multiples.vc; FinanceCharts; GuruFocus; stockti |
| **Meta** (~US$589.82, 24 Nov) | **22.1×** (tracker, 24 Nov); 17.9–18× elsewhere | 13.8–16.7× (Sep–Oct 2026) | 1.26–3.37% (conflicting) | stockti; FinanceCharts; GuruFocus; Yahoo |
| **Amazon** (~US$247, 21 Nov) | **23.0×** (GuruFocus, 21 Nov); 24.2–25.5× | 15.4–16.0× (Oct 2026) | **negative** (−0.1% to −1.6%) | GuruFocus; FinanceCharts; Finbox |
| **Oracle** (US$109–124, mid-Nov) | **~15×** (24/7 Wall St, 17 Nov); 15.3–17.8× | n/o | negative now; FY29 target ≥US$30B (8-K) | 24/7 Wall St; GuruFocus; Oracle 8-K via search |
| **Apple** (firm file, 16 Nov) | 36–38× FY27 consensus | n/o | **2.6–2.7%** | `reports/equity/2026-11-16-aapl-valuation.md` |
| MSFT per vendors (cross-check) | 20.7–26.8× | 14.8–19.6× | — | Finviz, Yahoo SG/UK, Alpha Spread, Investing.com (undated) |

### 7.3 Reading the comps
- **On forward P/E, MSFT (24–25×) sits in the middle of the hyperscalers** (Meta ~18–22×, Amazon ~23–25×, Alphabet ~19–28×) and well below Apple. Peer central ~23× on FY27 EPS of ~US$19.9 gives **US$458**. The 18–28× span gives **US$358–557**.
- **On EV/EBITDA, MSFT's 17.9× sits at the top of the 14–19× peer band.** Applying 14–19× to TTM EBITDA, after leases, gives **US$379–517**.
- **On FCF yield, every hyperscaler is in the same position:** 1–1.6% or negative, because of AI capex. **Peer FCF yields therefore cannot anchor value. They show the whole group is priced on an assumption that capex normalises.** Only Apple (2.6%, no AI capex) has a clean FCF yield, and it trades at a premium for exactly that reason.
- **Relative band: US$370–520, central US$460.**

---

## 8. Method cross-check: why DCF (US$344) and comps (US$460) disagree

1. **Comps inherit the group's capex assumption.** All four hyperscalers trade on earnings while generating ~1% FCF yields. A relative value says "MSFT is fairly priced **if** the market is right that AI capex normalises for everyone." The DCF makes that assumption explicit: normalisation to 18% of revenue by FY35 in the base. Even that **does not reach the price**.
2. **Rates.** A 4.90% Treasury against a ~24× forward P/E (a 4.1% earnings yield) means the whole group is priced at a **negative** earnings-yield gap. Relative value is "no worse than peers", not intrinsic.
3. **Leases.** Peer EV/EBITDA figures from vendors almost certainly exclude **uncommenced** leases. Including MSFT's lifts its multiple from 17.9× to 19.3×.
4. **Both methods agree on direction for the central case.** The central relative value (US$460) is 7% below the price, and the central DCF is 31% below. Only the top of the relative band (US$520) and the bull DCF (US$564) clear US$496.

**Blend 50/50** (as in the AAPL precedent; expect partial convergence): **US$340–450, central US$400.**

---

## 9. Sensitivity tables

### 9.1 WACC × terminal growth, base case (US$/share)
| WACC \ g | 2.0% | 2.5% | **3.0%** | 3.5% | 4.0% |
|---|---|---|---|---|---|
| 8.0% | 387 | 405 | 426 | 452 | 485 |
| 8.5% | 352 | 366 | 382 | 402 | 426 |
| **9.0%** | 322 | 333 | **346** | 361 | 379 |
| 9.5% | 296 | 304 | 315 | 327 | 341 |
| 10.0% | 273 | 280 | 288 | 298 | 309 |
| 10.5% | 253 | 259 | 266 | 273 | 282 |

### 9.2 WACC × terminal-growth shift, probability-weighted (US$/share)
| WACC \ g shift | −1.0pt | −0.5pt | **0** | +0.5pt | +1.0pt |
|---|---|---|---|---|---|
| 8.0% | 385 | 404 | 427 | 455 | 491 |
| 8.5% | 349 | 364 | 382 | 403 | 429 |
| **9.0%** | 319 | 331 | **344** | 361 | 380 |
| 9.5% | 293 | 302 | 313 | 325 | 340 |
| 10.0% | 270 | 277 | 286 | 296 | 308 |
| 10.5% | 250 | 256 | 263 | 271 | 280 |

**The price (US$496) appears in no cell of either table.** The closest is 491: an 8.0% WACC, with every scenario's terminal growth +1pt (bull at 4.5%).

### 9.3 Steady-state capex/revenue (FY32–36 and in perpetuity) × EBITDA margin, base (US$/share)
| Capex \ EBITDA | 55% | 58% | **60%** | 62% | 64% |
|---|---|---|---|---|---|
| 14% | 356 | 387 | 408 | 429 | 450 |
| 16% | 337 | 368 | 389 | 410 | 430 |
| **18%** | 318 | 349 | **370** | 390 | 411 |
| 22% | 279 | 310 | 331 | 352 | 373 |
| 26% | 241 | 272 | 293 | 314 | 334 |
| 30% | 203 | 234 | 254 | 275 | 296 |
| 35% | 155 | 186 | 206 | 227 | 248 |

Here terminal reinvestment is set by the capex ratio rather than g/RONIC, so the 18%/60% cell (US$370) sits above the RONIC-based base (US$346). Read the grid for its **gradient**: **each 4pt of perpetual capex intensity is worth ~US$40/share.** This is the moat analyst's "single largest source of dispersion", now quantified.

### 9.4 One at a time (base US$346)
| Driver | Up / down | US$/share | Δ |
|---|---|---|---|
| **Ex-OpenAI growth ±2pt a year** | | 403 / 296 | **+17% / −14%** |
| **Capex path: bull / bear** | | 381 / 265 | **+10% / −23%** |
| **WACC 8.5% / 9.5%** | | 382 / 315 | **+11% / −9%** |
| Terminal RONIC 28% / 12% | | 358 / 318 | +3% / −8% |
| OpenAI revenue path: bull / bear | | 363 / 324 | +5% / −6% |
| OpenAI stake US$300B / US$100B | | 366 / 339 | +6% / −2% |
| EBITDA margin ±2pt | | 364 / 327 | +5% / −5% |
| Terminal g 3.5% / 2.5% | | 361 / 333 | +4% / −4% |
| Uncommenced leases at 50% / 100% of nominal | | 352 / 330 | +2% / −4% |
| D&A rate 12.5% / 14.5% (server-life proxy) | | 346 / 343 | 0% / −1% |

---

## 10. Reverse DCF: what US$496.13 implies

| Question | Answer |
|---|---|
| **Implied IRR on base cash flows** | **7.4%** (probability-weighted 7.4%; bull 9.7%). Against the 4.90% Treasury, that is a **~2.5pt equity premium**, below the ~4.1–4.4% ERP. **Only bull cash flows earn the 9% WACC.** |
| **Growth needed** (base margins and capex) | Growth scaled **1.54×**: FY26–36 revenue CAGR of **12.8%** (base 8.9%), giving **FY36 revenue of ~US$1.1T** (3.3× FY26) |
| Perpetual capex intensity needed (base growth and margins) | **~7% of revenue.** Not credible: FY24 was 18.1% before AI. **The price cannot be explained by capex normalisation alone.** |
| Flat EBITDA margin needed | **~76%** (TTM 59%). Not credible. |
| Owner-earnings framing | Growth must supply **~67%** of the price (no-growth value ~US$165) |

**Plain statement:** US$496 prices **a decade of ~13% compound revenue growth, with AI capex normalising, at today's margins.** That is the bull case, and it is not an absurd one: Azure is +48% and guided to 49–50%. But it leaves no margin of safety against the three things the firm's own reports flag:
- capex intensity that does not normalise (FCF −27% YoY; capex/revenue 39%);
- OpenAI concentration (10.8% of revenue, ~45% of RPO);
- ROIC still falling (from ~45% to ~26%).

---

## 11. Margin of safety at the current price

MoS = (fair value − price) / fair value.

| Reference | US$ | MoS at US$496.13 |
|---|---|---|
| Bear DCF | 122 | −307% |
| Weighted DCF | 344 | −44% |
| **Central (blend)** | **400** | **−24%** |
| Top of range | 450 | −10% |
| Top of relative band | 520 | +5% |
| Bull DCF | 564 | +12% |

**Required MoS: 20%** (菲比斯; the capex conditions are met, §4.5). **Buy-below level: 0.80 × US$400 = US$320.**

| Zone (valuation signal only, not orders) | Price | Reasoning |
|---|---|---|
| INITIATE / ADD | ≤ US$320 | 20% MoS to the central value. The 52-week low was US$349.20 [F]. |
| WATCH (fair) | US$320–450 | Inside the range |
| **DO NOT INITIATE** | **> US$450** | Above the top of the range. **US$496.13 is here.** |

**Valuation signal at US$496.13: do not initiate.** The price is 10% above the top of my range and 24% above the central value, though it is below the bull DCF. The −6.4% move since 29 Oct and the SMA20/50 cross [F technical] are timing inputs for Dept 5, not valuation inputs.

---

## 12. Valuation input to committee score

**Valuation score: 38 / 100.** Higher means more attractive at the current price. The score rates the price, not the business.

| Calibration | Score | Situation |
|---|---|---|
| 6160/ONC at US$415.62 (this session) | 20 | 2.0× central; above the bull DCF; IRR ≈ the Treasury |
| AAPL at US$356.27 | 28 | 1.7× central; above the steel-man DCF |
| KLAC (Jul, corrected) | 33 | ~2.2× base intrinsic, with a growth runway |
| **MSFT at US$496.13** | **38** | **1.24× central; below the bull DCF; IRR 7.4% (2.5pt over the Treasury); the price is reachable on bull growth alone without stacking exotic assumptions** |

**Why not lower:** this is the highest-quality franchise in coverage (Wide moat, 74). It has accelerating Azure, ~50% operating margins and net cash ex-leases. **A defensible bull case (US$564) clears the price.**

**Why not higher:** the base and weighted DCFs sit 30–31% below the price. FCF is falling. And the price needs about 13% compound growth for a decade.

**One-line verdict:** *The best business the firm covers, priced for its bull case. Fair value US$340–450, central US$400; MoS −24% against a required 20%; buy-below level US$320; valuation signal: do not initiate.*

**The three assumptions the value is most sensitive to:**
1. **Steady-state capex intensity** (bull/bear path +10% / −23%; ~US$40/share per 4pt of revenue)
2. **The discount rate** (±0.5pt → −9% / +11%)
3. **Ex-OpenAI revenue growth** (±2pt a year → +17% / −14%)

**What would move me (pre-registered):**
- **Up:**
  - Q2–Q3 FY27 cash capex flattens while Azure holds above 40%: evidence of normalisation (watch capex/revenue < 35% in H2 FY27);
  - disclosed Microsoft Cloud gross margin ≥ 66% with D&A growth decelerating;
  - an OpenAI listing at ≥ US$1.25T (+~US$20/share to the stake).
- **Down:**
  - Q2 FCF negative, or bond issuance to fund capex and buybacks;
  - OpenAI revenue or receivables diverging (receivables growing faster than revenue for a second quarter);
  - a server-life extension beyond 6 years;
  - uncommenced leases growing faster than revenue;
  - a binding CMA/DMA remedy on the M365/Copilot bundle.

**Anti-anchoring disclosure (L-003):**
- This is the first MSFT valuation, with no position and no prior verdict. The exposures were the sell-side's ~US$632 average with zero Sells, and the firm's own negative AAPL/6160 calls this month (an "everything is expensive" habit risk).
- **Bearish-leaning choices:** FY27 EPS ~2–4% below consensus (§5); uncommenced leases at 65% PV; the OpenAI stake haircut 25% below the last closed round. Together roughly **−8%**.
- **Bullish-leaning choices:** WACC rounded down from 9.07% to 9.0% (+1%); finance leases at the stale June figure (+US$1).
- **Removing every bearish choice gives a base of ~US$375, still 24% below the price.**

---

## 13. NOT OBTAINED
1. **The Q1 FY27 10-Q** (sec.gov DNS-blocked): finance leases at 30 Sep 2026, current operating-lease liabilities, the lease maturity schedule, **uncommenced leases at 30 Sep 2026**, the period-end share count, and the OpenAI carrying value and exact stake (24% vs 27%, conflicting).
2. **Server and network useful life** (10-K) and the cash-flow profile of the uncommenced leases (start dates, terms, cancellation rights). The 65% PV factor is my estimate.
3. **Official FY26 capex including finance leases.** The FY27 path is anchored on Q1 (US$45.2B) and the Q2 guide (>US$50B).
4. **A full-year FY27 operating-margin guide; FY28 consensus.**
5. **Same-day, same-vendor peer multiples.** EV/EBITDA for Oracle; consistent peer FCF yields.
6. **OpenAI's latest round terms** (the US$1.25T round is unconfirmed) and liquidation preferences.
7. **Segment-level cost data** to value software and infrastructure separately (removed by the Sept 2026 segment change).
8. **A verified ERP** (the Damodaran 4.41% snippet is garbled) and a second beta source.

---

## 14. Sources

**Firm files (inputs):**
- `reports/equity/2026-11-25-msft-financials-update.md` (巴爺爺)
- `reports/equity/2026-08-21-msft-moat.md` (菲比斯)
- `reports/industry/2026-08-21-msft-industry.md` (Elon Musk)
- `reports/equity/2026-11-25-msft-management.md` (Peter)
- `reports/news/2026-11-25-6160hk-msft-news-refresh.md` (修大哥)
- `reports/technical/2026-11-25-msft-technical.md` (老詹)
- `reports/equity/2026-11-16-aapl-valuation.md` (method and calibration)

**Web (searched 2026-11-25; search extractions, no page opened):**
- 10-year Treasury: [Investing.com](https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data) · [Mortgage News Daily](https://www.mortgagenewsdaily.com/treasury/10yr) · [Longbridge](https://longbridge.com/en/news/306679499) · [CNBC 24 Nov](https://www.cnbc.com/2026/11/24/treasury-yields-bonds-inflation.html)
- ERP: [Damodaran Online](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm)
- Beta: [Yahoo Finance MSFT](https://finance.yahoo.com/quote/MSFT/)
- OpenAI valuation: [CNBC, US$852B round closed (31 Mar 2026)](https://www.cnbc.com/2026/03/31/openai-funding-round-ipo.html) · [Benzinga, US$1.25T (Nov 2026)](https://www.benzinga.com/markets/private-markets/26/11/63213967/openai-raises-15b-at-1-25t-valuation-in-latest-funding-round-amid-ipo-plans) · [CNBC, round pared (31 Oct 2026)](https://www.cnbc.com/2026/10/31/openai-fundraising-20-billion-valuation.html)
- OpenAI stake disclosure: [om.co on the 10-Q](https://om.co/2026/05/01/what-microsofts-10-q-says-about-openai/) · [Microsoft blog, Oct 2025](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
- Peers and MSFT multiples:
  - Alphabet: [Gotrade GOOGL 24 Nov](https://www.heygotrade.com/en/news/google-googl-stock-news-november-25-2026/) · [stockanalysis GOOGL market cap (via search)](https://stockanalysis.com/stocks/googl/market-cap/) · [multiples.vc Alphabet](https://multiples.vc/public-comps/alphabet-valuation-multiples) · [FinanceCharts GOOG EV/EBITDA](https://www.financecharts.com/stocks/GOOG/value/ev-to-ebitda) · [FinanceCharts GOOG FCF yield](https://www.financecharts.com/stocks/GOOG/value/fcf-yield)
  - Meta: [FinanceCharts META EV/EBITDA](https://www.financecharts.com/stocks/META/value/ev-to-ebitda)
  - Amazon: [GuruFocus AMZN forward P/E](https://www.gurufocus.com/term/forward-pe-ratio/AMZN) · [FinanceCharts AMZN/META/MSFT FCF yield](https://www.financecharts.com/compare/AMZN,META,MSFT/value/fcf-yield)
  - Oracle: [GuruFocus ORCL forward P/E](https://www.gurufocus.com/term/forward-pe-ratio/ORCL) · [24/7 Wall St, Oracle (17 Nov)](https://247wallst.com/investing/2026/11/17/oracles-40-6-month-slide-continues-this-analyst-maintains-his-buy-rating-predicting-230-returns/)
  - Cross-group: [stockti mega-cap forward P/E](https://stockti.com/stocks/mega-cap-forward-pe) · [GuruFocus 5-way compare](https://www.gurufocus.com/stocks/compare/aapl-vs-amzn-vs-googl-vs-meta-vs-msft)
  - MSFT: [Finviz MSFT](https://finviz.com/stock?t=MSFT&ty=rv) · [Yahoo SG MSFT key stats](https://sg.finance.yahoo.com/quote/MSFT/key-statistics/) · [Alpha Spread MSFT EV/EBITDA](https://www.alphaspread.com/security/nasdaq/msft/relative-valuation/ratio/enterprise-value-to-ebitda)

**Not used:**
- `tradingkey.com` (blacklisted; excluded from every search)
- `stockanalysis.com` (direct fetch DNS-blocked; one market-cap figure is from a search snippet only)

---

*Research only. Not investment advice. The levels are valuation signals, not orders, and the Committee and the Owner decide. Markets cannot be reliably predicted.*

---

## Appendix A: model code (exactly as run)

Reproduce with `python3 -I val_msft.py` (standard library only). Script path at run time: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/val/val_msft.py`. That is scratch space and may be cleared, so the full text is below.

Script SHA-256: `e9ec7e8ea0943afdfb37fe02cc89401b6ca3ff03ab298bffcabae503ea912c3f`. On 2026-11-26 a re-run produced output byte-identical to the run used for this report.

The multiples arithmetic in §7 and the blends in §1 come from a separate short script (`comps.py`, same folder), reproduced in Appendix B.

```python
# MSFT -- FCF DCF (explicit capex incl. finance leases), owner-earnings / ROIC-linked cross-check,
# leases as debt (incl. $329.1bn signed-not-commenced), OpenAI revenue split + equity stake (SOTP),
# bear/base/bull, sensitivities, reverse DCF.  𢦀鳩仔, 2026-11-25. Pure Python. US$ billions; shares millions.
# Tags (see report): [P] primary microsoft.com via 巴爺爺, [S] search extraction, [W] web search (dated),
# [C] arithmetic, [A] analyst assumption.
import copy

PRICE = 496.13       # [F] close 2026-11-24 (Webull bar via technical report)
SHARES = 7446.0      # [P] Q1 FY27 weighted diluted shares (period-end count NOT OBTAINED)
REV_FY26 = 331.839   # [P] FY26 revenue
PPE_FY26 = 313.076   # [P] net PP&E 30 Jun 2026
OAI_SHARE_FY27 = 0.108   # [S] OpenAI = $10.0bn of Q1 FY27 revenue (10-Q via secondary)
TAX = 0.20           # [P] Q2 guide ~20%; TTM 19.7% [C]
NET_CASH = 29.028    # [C/P] cash + STI 64.509 less bonds 35.481 at 30 Sep 2026
FIN_LEASE = 62.304   # [S] finance lease liabilities 30 Jun 2026 (Sep NOT OBTAINED; stale-low)
OP_LEASE = 21.719    # [P] long-term operating lease liabilities 30 Sep 2026 (current portion NOT OBTAINED)
UNCOMMENCED = 329.1  # [S] leases signed, not commenced, 30 Jun 2026 (nominal, undiscounted)
FY = list(range(2027, 2037))   # FY27..FY36 (June year-ends)
T = [0.30] + [1.10 + k for k in range(9)]   # FY27 midpoint of remaining 7 months; then mid-year
W = [0.75] + [1.0] * 9                       # Q1 FY27 already in the 30 Sep balance sheet

BASE = dict(
    name="Base",
    g27=0.17,                                                   # FY27 total revenue growth
    g_ex=[0.14, 0.12, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04],  # ex-OpenAI growth FY28..FY36
    g_oai=[0.15, 0.10, 0.05, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03],  # OpenAI revenue growth FY28..FY36
    ebitda=[0.60] * 10,          # EBITDA margin, ex rent on the uncommenced leases (they are deducted as debt)
    capex=[0.52, 0.42, 0.34, 0.28, 0.24, 0.22, 0.20, 0.19, 0.18, 0.18],  # cash capex + finance leases, % revenue
    d=0.13,                      # D&A / (opening net PP&E + half of year capex)
    g=0.03, ronic=0.20,          # terminal growth and return on new invested capital
    wacc=0.09,
    oai_stake=150.0,             # OpenAI equity stake value
    unc_pv=0.65,                 # PV of uncommenced leases as fraction of nominal
    ronic_explicit=0.25,         # owner-earnings method: return on growth investment in FY28-FY36
    maint=1.10,                  # owner-earnings method: maintenance capex = maint x D&A
)
BEAR = copy.deepcopy(BASE); BEAR.update(
    name="Bear", g27=0.16,
    g_ex=[0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05, 0.04, 0.04],
    g_oai=[-0.25, -0.35, 0.0, 0.0, 0.02, 0.02, 0.02, 0.02, 0.02],
    ebitda=[0.59, 0.57, 0.56, 0.55] + [0.55] * 6,
    capex=[0.53, 0.47, 0.42, 0.38, 0.35, 0.33, 0.32, 0.31, 0.30, 0.30],
    d=0.145, g=0.025, ronic=0.12, oai_stake=100.0, unc_pv=1.00,
    ronic_explicit=0.15, maint=1.30,
)
BULL = copy.deepcopy(BASE); BULL.update(
    name="Bull", g27=0.18,
    g_ex=[0.16, 0.14, 0.13, 0.12, 0.10, 0.09, 0.08, 0.07, 0.06],
    g_oai=[0.25, 0.20, 0.15, 0.10, 0.08, 0.06, 0.05, 0.04, 0.04],
    ebitda=[0.61, 0.62] + [0.62] * 8,
    capex=[0.50, 0.38, 0.29, 0.22, 0.18, 0.16, 0.15, 0.15, 0.15, 0.15],
    d=0.125, g=0.035, ronic=0.28, oai_stake=300.0, unc_pv=0.50,
    ronic_explicit=0.35, maint=1.00,
)
SCEN = (BEAR, BASE, BULL)
PROBS = {"Bear": 0.25, "Base": 0.50, "Bull": 0.25}


def path(s):
    rev27 = REV_FY26 * (1 + s["g27"])
    oai, ex = rev27 * OAI_SHARE_FY27, rev27 * (1 - OAI_SHARE_FY27)
    rows, ppe = [], PPE_FY26
    for i, y in enumerate(FY):
        if i:
            ex *= 1 + s["g_ex"][i - 1]; oai *= 1 + s["g_oai"][i - 1]
        rev = ex + oai
        capex = s["capex"][i] * rev
        da = s["d"] * (ppe + 0.5 * capex)
        ppe = ppe + capex - da
        ebitda = s["ebitda"][i] * rev
        ebit = ebitda - da
        nopat = ebit * (1 - TAX)
        fcff = nopat + da - capex          # delta-NWC set to 0 (unearned revenue funds receivables)
        rows.append(dict(y=y, rev=rev, oai=oai, ebitda=ebitda, da=da, ebit=ebit, m=ebit / rev,
                         nopat=nopat, capex=capex, fcff=fcff, ppe=ppe))
    return rows


def bridge(s, ev):
    debt_like = FIN_LEASE + OP_LEASE + UNCOMMENCED * s["unc_pv"]
    eq = ev + NET_CASH - debt_like + s["oai_stake"]
    return eq, eq / SHARES * 1000, debt_like


def tv(s, last):
    g = s["g"]
    if s.get("tv_capex") is None:   # default: reinvestment = g / RONIC of NOPAT
        return last["ebit"] * (1 + g) * (1 - TAX) * (1 - g / s["ronic"]) / (s["wacc"] - g)
    # explicit perpetual capex/revenue (moat analyst's requested framing)
    rev1, da1 = last["rev"] * (1 + g), last["da"] * (1 + g)
    ebit1 = s["ebitda"][-1] * rev1 - da1
    return (ebit1 * (1 - TAX) + da1 - s["tv_capex"] * rev1) / (s["wacc"] - g)


def run(s):
    rows = path(s)
    wacc = s["wacc"]
    pv = sum(W[i] * r["fcff"] / (1 + wacc) ** T[i] for i, r in enumerate(rows))
    TV = tv(s, rows[-1])
    pv_tv = TV / (1 + wacc) ** (T[-1] + 0.5)
    ev = pv + pv_tv
    eq, ps, debt_like = bridge(s, ev)
    # Method 2: owner earnings less growth reinvestment at RONIC (ignores management's capex path)
    pv2 = 0.0
    for i, r in enumerate(rows):
        g_next = (rows[i + 1]["rev"] / r["rev"] - 1) if i + 1 < len(rows) else s["g"]
        oe = r["nopat"] + r["da"] - s["maint"] * r["da"]
        cf = oe - r["nopat"] * g_next / s["ronic_explicit"]
        pv2 += W[i] * cf / (1 + wacc) ** T[i]
    ev2 = pv2 + pv_tv
    eq2, ps2, _ = bridge(s, ev2)
    return dict(rows=rows, pv=pv, pv_tv=pv_tv, tv_share=pv_tv / ev, ev=ev, eq=eq, ps=ps,
                debt_like=debt_like, ev2=ev2, ps2=ps2)


def weighted(mod=lambda s: s, key="ps"):
    return sum(PROBS[sc["name"]] * run(mod(copy.deepcopy(sc)))[key] for sc in SCEN)


def solve(f, lo, hi, target, it=200):
    flo = f(lo) - target
    for _ in range(it):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


if __name__ == "__main__":
    mcap = PRICE * SHARES / 1000
    print(f"Market cap ${mcap:,.0f}bn at ${PRICE} x {SHARES:,.0f}m diluted")
    # TTM owner earnings (normalised capex), from 巴爺爺's TTM table [P/C]
    ttm_oi, ttm_da, ttm_capex, ttm_fcf, ttm_sbc = 163.191, 42.131, 135.921, 59.957, 12.556
    q1_da_run = 11.744 * 4
    print("\nTTM owner earnings = NOPAT + D&A - maintenance capex (maintenance = m x run-rate D&A $%.1fbn):" % q1_da_run)
    for lab, m in (("Bull m=1.00", 1.00), ("Base m=1.10", 1.10), ("Bear m=1.30", 1.30)):
        oe = ttm_oi * (1 - TAX) + ttm_da - m * q1_da_run
        print(f"| {lab} | {oe:.1f} | yield {oe / mcap:.2%} | P/OE {mcap / oe:.1f}x |")
    print(f"| Reported FCF TTM | {ttm_fcf:.1f} | yield {ttm_fcf / mcap:.2%} | P/FCF {mcap / ttm_fcf:.1f}x |")
    print(f"| FCF - SBC TTM | {ttm_fcf - ttm_sbc:.1f} | yield {(ttm_fcf - ttm_sbc) / mcap:.2%} |")

    res = {s["name"]: run(s) for s in SCEN}
    print("\n| Scenario | Prob | PV FCFF FY27-36 | PV terminal | TV % EV | EV | Debt-like (leases) | OpenAI stake | Equity | $/share (FCF DCF) | $/share (owner-earnings method) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for n in ("Bear", "Base", "Bull"):
        r = res[n]; s = {x["name"]: x for x in SCEN}[n]
        print(f"| {n} | {PROBS[n]:.0%} | {r['pv']:,.0f} | {r['pv_tv']:,.0f} | {r['tv_share']:.0%} | {r['ev']:,.0f} | -{r['debt_like']:,.0f} | +{s['oai_stake']:.0f} | {r['eq']:,.0f} | {r['ps']:.0f} | {r['ps2']:.0f} |")
    w1, w2 = weighted(), weighted(key="ps2")
    print(f"\nWeighted FCF-DCF ${w1:.1f}; owner-earnings method ${w2:.1f}; price ${PRICE}")
    print(f"MoS vs FCF-DCF {(w1 - PRICE) / w1:+.1%}; vs OE method {(w2 - PRICE) / w2:+.1%}")

    for n in ("Bear", "Base", "Bull"):
        print(f"\n{n}:")
        print("| FY | Revenue | of which OpenAI | EBITDA % | D&A | EBIT % | NOPAT | Capex (incl. fin. leases) | Capex % | FCFF |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for r in res[n]["rows"]:
            print(f"| FY{r['y'] % 100} | {r['rev']:.0f} | {r['oai']:.0f} | {r['ebitda'] / r['rev']:.0%} | {r['da']:.0f} | {r['m']:.1%} | {r['nopat']:.0f} | {r['capex']:.0f} | {r['capex'] / r['rev']:.0%} | {r['fcff']:.0f} |")

    print("\nWACC x g, Base ($/share, FCF DCF):")
    gs = [0.020, 0.025, 0.030, 0.035, 0.040]; ws = [0.080, 0.085, 0.090, 0.095, 0.100, 0.105]
    print("| WACC \\ g | " + " | ".join(f"{x:.1%}" for x in gs) + " |"); print("|---" * 6 + "|")
    for wv in ws:
        print(f"| {wv:.1%} | " + " | ".join(f"{run(dict(BASE, wacc=wv, g=gv))['ps']:.0f}" for gv in gs) + " |")
    print("\nWACC x g shift, probability-weighted ($/share, FCF DCF):")
    ds = [-0.01, -0.005, 0.0, 0.005, 0.01]
    print("| WACC \\ g shift | " + " | ".join(f"{d:+.1%}" for d in ds) + " |"); print("|---" * 6 + "|")
    for wv in ws:
        print(f"| {wv:.1%} | " + " | ".join(f"{weighted(lambda s, wv=wv, d=d: dict(s, wacc=wv, g=s['g'] + d)):.0f}" for d in ds) + " |")

    print("\nSteady-state capex/revenue (FY32-36 AND in perpetuity) x EBITDA margin, Base ($/share):")
    caps = [0.14, 0.16, 0.18, 0.22, 0.26, 0.30, 0.35]; ems = [0.55, 0.58, 0.60, 0.62, 0.64]
    print("| Capex \\ EBITDA | " + " | ".join(f"{x:.0%}" for x in ems) + " |"); print("|---" * 6 + "|")
    for c in caps:
        cp = BASE["capex"][:5] + [c] * 5
        cells = [f"{run(dict(BASE, capex=cp, ebitda=[em] * 10, tv_capex=c))['ps']:.0f}" for em in ems]
        print(f"| {c:.0%} | " + " | ".join(cells) + " |")
    print("Base with explicit terminal capex 18%%: $%.0f (RONIC-based base: $%.0f)" % (
        run(dict(BASE, tv_capex=0.18))["ps"], run(BASE)["ps"]))

    base_v = res["Base"]["ps"]
    print("\nOne-at-a-time (Base):")
    tests = [
        ("WACC 8.5% / 9.5%", dict(wacc=0.085), dict(wacc=0.095)),
        ("Terminal g 3.5% / 2.5%", dict(g=0.035), dict(g=0.025)),
        ("Terminal RONIC 28% / 12%", dict(ronic=0.28), dict(ronic=0.12)),
        ("Capex path bull / bear", dict(capex=BULL["capex"]), dict(capex=BEAR["capex"])),
        ("EBITDA margin +2pt / -2pt", dict(ebitda=[x + 0.02 for x in BASE["ebitda"]]), dict(ebitda=[x - 0.02 for x in BASE["ebitda"]])),
        ("Ex-OpenAI growth +2pt / -2pt", dict(g_ex=[x + 0.02 for x in BASE["g_ex"]]), dict(g_ex=[x - 0.02 for x in BASE["g_ex"]])),
        ("OpenAI revenue bull / bear path", dict(g_oai=BULL["g_oai"]), dict(g_oai=BEAR["g_oai"])),
        ("OpenAI stake $300bn / $100bn", dict(oai_stake=300.0), dict(oai_stake=100.0)),
        ("Uncommenced leases PV 50% / 100%", dict(unc_pv=0.50), dict(unc_pv=1.00)),
        ("Server life: d 12.5% / 14.5%", dict(d=0.125), dict(d=0.145)),
    ]
    for lab, up, dn in tests:
        v1, v2 = run(dict(BASE, **up))["ps"], run(dict(BASE, **dn))["ps"]
        print(f"| {lab} | {v1:.0f} | {v2:.0f} | {(v1 - base_v) / base_v:+.0%} / {(v2 - base_v) / base_v:+.0%} |")
    print(f"Finance leases at $69.7bn (Jun + Q1 additions, no repayments) instead of $62.3bn: {(-7.4e3 / SHARES):+.2f}/share")

    print("\nReverse DCF at $%.2f:" % PRICE)
    irr = solve(lambda x: run(dict(BASE, wacc=x))["ps"], 0.035, 0.20, PRICE)
    print(f"  Implied IRR on base cash flows: {irr:.2%}")
    irr_b = solve(lambda x: run(dict(BULL, wacc=x))["ps"], 0.04, 0.20, PRICE)
    print(f"  Implied IRR on bull cash flows: {irr_b:.2%}")
    irr_w = solve(lambda x: weighted(lambda s: dict(s, wacc=x)), 0.04, 0.20, PRICE)
    print(f"  Implied IRR on probability-weighted cash flows: {irr_w:.2%}")
    # implied steady-state capex intensity (FY32-36), glide FY28-31 linear from 42%
    def f_cap(c):
        cp = [0.52] + [0.42 + (c - 0.42) * k / 4 for k in range(1, 5)] + [c] * 5
        return run(dict(BASE, capex=cp))["ps"]
    for c in (0.10, 0.14, 0.18):
        cp = [0.52] + [0.42 + (c - 0.42) * k / 4 for k in range(1, 5)] + [c] * 5
        print(f"  Capex glides to {c:.0%} by FY31 and stays there (incl. perpetuity): ${run(dict(BASE, capex=cp, tv_capex=c))['ps']:.0f}")
    c_star = solve(lambda c: run(dict(BASE, capex=[0.52] + [0.42 + (c - 0.42) * k / 4 for k in range(1, 5)] + [c] * 5, tv_capex=c))["ps"], 0.0, 0.40, PRICE)
    print(f"  Implied perpetual capex/revenue to reach the price on base growth and margins: {c_star:.1%} (FY24 actual 18.1%; TTM 39.2%)")
    k = solve(lambda k: run(dict(BASE, g_ex=[x * k for x in BASE["g_ex"]], g_oai=[x * k for x in BASE["g_oai"]]))["ps"], 0.0, 4.0, PRICE)
    rr = run(dict(BASE, g_ex=[x * k for x in BASE["g_ex"]], g_oai=[x * k for x in BASE["g_oai"]]))["rows"]
    cagr = (rr[-1]["rev"] / REV_FY26) ** (1 / 10) - 1
    print(f"  Implied growth scale {k:.2f}x -> FY26-36 revenue CAGR {cagr:.1%} (base {((res['Base']['rows'][-1]['rev'] / REV_FY26) ** 0.1 - 1):.1%}); FY36 revenue ${rr[-1]['rev']:.0f}bn")
    em = solve(lambda m: run(dict(BASE, ebitda=[m] * 10))["ps"], 0.40, 0.90, PRICE)
    print(f"  Implied flat EBITDA margin: {em:.1%} (base 60%; TTM 59.3%)")
    # No-growth value from owner earnings
    for lab, m in (("base m=1.10", 1.10),):
        oe = ttm_oi * (1 - TAX) + ttm_da - m * q1_da_run
        ng = oe / BASE["wacc"]
        eq = ng + NET_CASH - (FIN_LEASE + OP_LEASE + UNCOMMENCED * BASE["unc_pv"]) + BASE["oai_stake"]
        print(f"  No-growth value (TTM OE ${oe:.0f}bn / 9%): ${eq / SHARES * 1000:.0f}/share -> growth must supply {(PRICE - eq / SHARES * 1000) / PRICE:.0%} of the price")
```

## Appendix B: comparables and blend arithmetic (comps.py, as run; covers both names)

```python
# Comparables arithmetic for both names (inputs tagged in reports). US$bn unless noted.
FX=7.842
def hk(v): return v/13*FX
print("== 6160 / ONC ==")
P=415.62; N=118.0; mcap=P*N/1000
for nc in (4.8,3.7):
    ev=mcap-nc
    print(f"net cash {nc}: mcap {mcap:.2f} EV {ev:.2f} | EV/S TTM {ev/6.6065:.1f}x FY26G {ev/6.95:.1f}x FY27 base {ev/7.99:.1f}x FY27 cons {ev/7.77:.1f}x | EV/EBIT TTM {ev/1.1787:.1f}x FY26G {ev/1.25:.1f}x FY27 base {ev/1.53:.1f}x")
eps_ttm=7.88; eps26=7.30+0.256*0.82/118*1000; eps27=1.53*0.82/119.2*1000; eps29=2.20*0.82/121.6*1000
print(f"EPS: TTM {eps_ttm} FY26E {eps26:.2f} FY27E base {eps27:.2f} cons 10.45 FY29E {eps29:.2f}; CAGR26-29 {(eps29/eps26)**(1/3)-1:.1%}")
print(f"P/E TTM {P/eps_ttm:.1f}x FY26E {P/eps26:.1f}x FY27E {P/eps27:.1f}x cons {P/10.45:.1f}x; PEG (FY27E P/E / 26-29 CAGR) {P/eps27/(((eps29/eps26)**(1/3)-1)*100):.2f}")
for lab,m in (("LOE-exposed low 13.5x",13.5),("LOE-exposed high 16.2x",16.2),("mid 21x",21),("growth low 24.6x",24.6),("growth high 28x",28)):
    print(f"  {lab}: ${m*eps27:.0f} (cons basis ${m*10.45:.0f})")
for lab,m in (("EV/S 3.5x",3.5),("EV/S 5.6x",5.6),("EV/S 9.6x",9.6)):
    print(f"  {lab} on FY27E rev 7.99: ${(m*7.99+4.8)/N*1000:.0f}")
dcf=(186,202,219); rel=(160,220,295)
lo=0.5*dcf[0]+0.5*rel[0]; mid=0.5*dcf[1]+0.5*rel[1]; hi=0.5*dcf[2]+0.5*rel[2]
print(f"Blend 50/50: low {lo:.0f} central {mid:.0f} high {hi:.0f} | HK$ {hk(lo):.0f} / {hk(mid):.0f} / {hk(hi):.0f}")
for v in (175,210,255,301,313):
    print(f"  value ${v}: MoS at $415.62 {(v-P)/v:+.0%}; HK${hk(v):.0f} MoS at HK$230.80 {(hk(v)-230.80)/hk(v):+.0%}")
print(f"Required 30% MoS -> buy below ${0.7*210:.0f}/ADS = HK${hk(0.7*210):.0f}")
print(f"HK line vs ADS parity: HK$230.80 vs ADS-implied HK${hk(P):.2f} ({230.80/hk(P)-1:+.1%}); dates differ (20 Nov vs 24 Nov)")

print("\n== MSFT ==")
P=496.13; S=7446; mcap=P*S/1000
ebitda_ttm=163.191+42.131; ebitda27=0.60*388.2
ev_ex=mcap-29.028; ev_in=ev_ex+62.304+21.719
print(f"mcap {mcap:.0f}; EV ex leases {ev_ex:.0f}; EV incl. recognised leases {ev_in:.0f}; EV incl. +uncommenced PV 214 {ev_in+0.65*329.1:.0f}")
print(f"EV/EBITDA TTM {ev_ex/ebitda_ttm:.1f}x / {ev_in/ebitda_ttm:.1f}x; FY27E {ev_ex/ebitda27:.1f}x / {ev_in/ebitda27:.1f}x; incl uncommenced {(ev_in+0.65*329.1)/ebitda_ttm:.1f}x")
print(f"P/E TTM non-GAAP {P/18.04:.1f}x GAAP {P/19.15:.1f}x FY27 cons {P/20.39:.1f}-{P/19.53:.1f}x; FY27E base EPS {(143.3-0.3*0.8)/S*1000:.2f}")
print(f"FCF yield {59.957/mcap:.2%}; FCF-SBC {47.401/mcap:.2%}; OE base {121.0/mcap:.2%}; dividend {0.98*4/P:.2%}")
eps27=19.9
for m in (18,23,28): print(f"  P/E {m}x x ${eps27}: ${m*eps27:.0f}")
for m in (14,17,19): print(f"  EV/EBITDA {m}x TTM: ${(m*ebitda_ttm+29.028-62.304-21.719)/S*1000:.0f}")
dcf=(313,344,382); rel=(370,460,520)
lo=0.5*dcf[0]+0.5*rel[0]; mid=0.5*dcf[1]+0.5*rel[1]; hi=0.5*dcf[2]+0.5*rel[2]
print(f"Blend 50/50: low {lo:.0f} central {mid:.0f} high {hi:.0f}")
for v in (345,400,450,564):
    print(f"  value ${v}: MoS {(v-P)/v:+.0%}")
print(f"Required 20% MoS -> buy below ${0.8*400:.0f}")
```
