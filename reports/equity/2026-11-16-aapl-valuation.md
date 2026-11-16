# AAPL — Valuation (𢦀鳩仔, Valuation Analyst)

Date: 2026-11-16 · Price reference: $356.27 (Webull close 13 Nov 2026, read-only, via CEO)

> STATUS: **COMPLETE** (2026-11-16). Tier-2 inputs throughout; no primary filing opened. First Apple valuation in firm history. Position context: Owner **holds**; the question is HOLD / TRIM / ADD.

## 1. Fair value range & target price

| | Low | **Central** | High | Basis |
|---|---|---|---|---|
| **Fair value / share (blended)** | **$185** | **$210** | **$245** | 50% intrinsic DCF + 50% relative (§8) |
| Intrinsic: DCF, probability-weighted 30/50/20 | $153 (10.0%) | $165 (9.5%) | $196 (8.5%) | §6 |
| Relative: own P/E history + peers | $215 | ~$250 | $295 | §8 |
| Scenarios at 9.5% | bear $119 | base $169 | bull $224 | §6 |
| **Target price (central fair value, not a 12-month forecast)** | | **$210** | | |
| **Price 13 Nov 2026** | | **$356.27** | | [W] |
| **Margin of safety** | | **−70%** vs central; −45% vs top of range | | required **25%** (§10) |

**Verdict:** *A wide-moat, cash-rich franchise priced for ~15% a year of growth it has never sustained. Fair value $185–$245; MoS −70%; valuation signal TRIM (levels in §10 for the CRO, not orders).*

- **Reverse DCF:** $356 needs ~15%/yr owner-earnings growth for 10 years at 9.5% (11% even at 8.0%), against a 6.9% five-year NI CAGR (§4).
- **Expected return from $356.27:** ≈ **+4%/yr** base (−1.5% to +8.4%), versus a **5.15%** 10-year Treasury (§11).
- **Steel-man:** stacking every generous assumption gives **$320**, still below the price (§6).
- **Most sensitive to:** discount rate, long-run growth, steady-state operating margin (§12).

## 2. Inputs & data provenance

Tiers: **[R]** = firm report on disk (itself search-extracted, Tier-2) · **[W]** = Webull read-only close 13 Nov 2026, held by the CEO · **[F]** = fetched/searched today, dated, cited in §14 · **[D]** = derived (my arithmetic, shown) · **[A]** = assumption (mine, labelled).

| Input | Value | Tier / source |
|---|---|---|
| Price | **$356.27** (close 13 Nov 2026); ATH $360.83; realised vol 24.7% | [W] |
| Owner cost (context only, **no weight**, L-003) | $357.60 | caller |
| FY2026 revenue / operating income / net income / EPS | $478.83bn / $158.1bn / $132.18bn / $8.98 | [R] 巴爺爺 §2–3 |
| Gross margin FY26 / Services GM / Services share of GP | 48.8% / 76.2% / 40.2% | [R] 巴爺爺 §3 |
| Opex / revenue FY26 | 15.8% ((233.6 − 158.1)/478.83) | [D] |
| NI / OI ratio (tax + other income, held constant) | 0.836 (132.18/158.1) — implies ~16.4% "effective" leakage; true tax rate NOT OBTAINED | [D] |
| OCF / capex / FCF FY26 | $145.1bn / ~$9.0bn (low-quality source) / ~$136.1bn | [R] 巴爺爺 §6 |
| Tariff refund (Q4 only) | $0.05 EPS ≈ $0.74bn NI (0.05 × 14.72bn); ~1pt Q4 GM | [R] / [D] |
| **Shares** | **14.72bn** FY26 weighted diluted (NI/EPS) — used as base denominator · 14.27bn Webull outstanding — sensitivity (+3.2% to every per-share value) · **UNRECONCILED** | [R] / [W] |
| Cash + marketable securities 26 Sep 2026 | **$136.9bn** (cash $36.3bn, current securities $20.4bn, non-current ~$80bn by subtraction) | [F] FY26 10-K via search extraction (sec.gov not opened) — **Tier-2; first appearance in firm files, 巴爺爺 had it NOT OBTAINED** |
| Gross debt | $80.7bn ($78.7bn notes + $2.0bn CP) | [R] 巴爺爺 §7 |
| **Net cash** | **$56.2bn ≈ $3.82/share** (14.72bn). Shown both ways: with it and at zero. It moves value by ~1%; **not load-bearing** | [D] |
| Capital return FY26 | Buybacks $85.8bn (297m shares, avg ~$289), dividends $15.7bn | [R] 巴爺爺 §5 |
| Dec-qtr FY27 guide | Revenue +7–10%, GM 45–46% (memory, Siri ramp), Services +8–9% | [R] 修大哥 §2 |
| Consensus FY27 EPS | **$9.40–$9.84** (sources disagree; ~$9.40 = 37.1x on a ~12 Nov price; $9.84 Chartmill ~3 Nov) | [F] Yahoo/TipRanks "Apple shares look expensive heading into 2027"; Chartmill; Stockrow 36.5x fwd (~9 Nov) |
| Analyst targets | Median $356.50, mean ~$346, 45 analysts, low $250 (KeyBanc), Jefferies $263.66 | [R] 修大哥 §6 |
| AAPL P/E history | 5y avg **30–33x**, 10y avg **25–31x** (method-dependent); GuruFocus 10y median 27.7x, 10y range 12.2–42.1x (13 Nov 2026) | [F] Financecharts (Nov 2026), GuruFocus, Wisesheets, TIKR |
| Peer forward P/E | MSFT ~23–27x, GOOGL ~23–24x (dated Sep–Oct 2026, mixed bases, **not same-day**) | [F] Investing.com (~30 Oct 2026), TipRanks (~19 Sep 2026), Yahoo |
| 10y US Treasury | **5.15%** (13 Nov 2026 close; Investing.com 5.153%, MND 5.141%); market pricing a Dec Fed hike | [F] Forbes / CNBC / Investing.com 13 Nov 2026 |
| Equity risk premium | **4.41%** implied, Damodaran, 1 Nov 2026 (snippet garbled — **verify**); start-2026 4.23% | [F] Damodaran Online |
| Beta | **1.09** (Yahoo 5y monthly, ~Nov 2026); Investing/Finbox 1.11; outlier 0.57 (WallStreetNumbers, stale) | [F] |
| Google default-search payment | ~$20bn/yr, trial-era estimate, not disclosed by Apple; ≈12.7% of OI if ~100% margin | [R] 巴爺爺 §4; The dictator §1 |
| Google payment legal state | Continues under Mehta remedies (non-exclusive, 1-yr terms); DOJ cross-appeal 3 Feb 2026 seeks to stop payments; D.C. Cir. decision realistically 2027 (estimate) | [R] The dictator §1; CEO note |
| App Store commission pool | ~$27.4bn global 2024 (Appfigures), ~$30bn LTM mid-2025 (asymco); US ~$10.1bn 2024. **No FY26 figure** | [F] TechCrunch 8 May 2025; asymco 6 Jun 2025 |
| Moat | **Wide, 76/100**, slowly narrowing at the App Store toll, stable at the device. Required MoS **20%**, **25% if the model holds Services take rate flat for 10 years** | [R] 菲比斯 (complete per CEO note) |
| Management | B, 72; buybacks programmatic, not price-sensitive | [R] Peter |
| Industry | NEUTRAL 6/10; smartphones −20% Q3 2026; Apple units flat to −4%, share up; growth "ASP-led"; no AI unit-upgrade cycle in data | [R] Elon Musk §1–3 |

## 3. Assumptions table

Model: 10-year FCF-to-equity DCF on **revenue × operating margin × 0.836 (NI/OI) × FCF conversion 1.00**, then a Gordon terminal value; plus net cash $56.2bn; ÷ 14.72bn shares. Year 1 = FY2027 (to Sep 2027). Revenue growth: year 1 = g1; years 2–5 = g2; years 6–10 fade linearly to gT. Operating margin: year 1 = OM1, year 2 = midway, years 3–10 = OMss. **Same discount rate (9.5%) in all three scenarios**, so the scenario spread is fundamentals only; the rate is varied in §9.

| # | Assumption | Bear | **Base** | Bull | Basis |
|---|---|---|---|---|---|
| A1 | Discount rate (cost of equity; Apple's WACC ≈ ke given net cash) | 9.5% | **9.5%** | 9.5% | [D] CAPM = 5.15% + 1.09 × 4.41% = **9.96%**. I use **9.5%**, 0.5pt *below* CAPM, for net cash and the most stable franchise in coverage. Judgment call; firm precedent KLAC 10.5% base / 9.5% bull. Varied 8.0–11.0% in §9 |
| A2 | FY27 revenue growth (g1) | +2% | **+7%** | +10% | [A] Dec-qtr guide +7–10% [R]; base takes the bottom of the guide for the full year because the Dec quarter is seasonally the strongest and the iPhone/China comps toughen through FY27 |
| A3 | FY28 revenue growth | **−3%** (iPhone/China mean reversion) | +5.5% | +8% | [A] Bear: iPhone FY26 +21% and China +28% revert (§5) |
| A4 | FY29–31 revenue growth (g2) | +3% | **+5.5%** | +8% | [A] FY21→26 NI CAGR 6.9% [R]; smartphone market shrinking, Apple share rising [R]; Services +8–9% guided [R] |
| A5 | Terminal growth gT (after FY36) | 2.5% | **3.0%** | 3.5% | [A] Below nominal GDP; 10y Treasury 5.15% [F] |
| A6 | FY27 operating margin (OM1) | 30.0% | **31.5%** | 32.5% | [D] FY26 33.0% incl. tariff refund. GM 45–46% Dec-qtr guide = OM ~29.5–30.5% at a 15.8% opex ratio; base assumes memory costs ease in H2 FY27 (Bloomberg Intelligence: DRAM balance 4Q27 [R Elon Musk]) |
| A7 | Steady-state operating margin (OMss, FY29+) | 30.0% (GM ~46% sustained) | **33.0%** (= FY26) | 36.0% (Services/AI-fee mix, memory roll-over) | [A] **The base holds group OM flat; it does NOT explicitly erode the Services take rate** → 菲比斯's 25% MoS condition applies (§10) |
| A8 | NI / OI | 0.836 | 0.836 | 0.836 | [D] FY26; tax rate NOT OBTAINED |
| A9 | FCF / NI conversion | 1.00 | **1.00** | 1.00 | [D] FY26 FCF/NI ≈ 1.03 [R], but SBC NOT OBTAINED and FY26 OCF had a working-capital tailwind [R]. Using 1.03 adds ~3% to every value |
| A10 | Net cash | $56.2bn | $56.2bn | $56.2bn | [F]/[D]; at zero, −$3.8/share |
| A11 | Share denominator | 14.72bn | **14.72bn** | 14.72bn | [D]; at Webull 14.27bn, +3.2% to every value |
| A12 | Google payment | in base revenue | in base revenue | in base revenue | Stressed separately (§7) |
| A13 | Scenario probabilities | **30%** | **50%** | **20%** | [A] Bear > bull because the FY26 base is a cyclical high (iPhone +21%, China +28%, refund), the guide is down, and the smartphone market is −12% to −20% [R]. At 25/50/25 the weighted value is $170 instead of $165 |

**Resulting paths (derived):**

| | Bear | Base | Bull |
|---|---|---|---|
| FY27 net income / EPS (14.72bn; ~2% fewer shares) | $122.5bn / $8.32 ($8.49) | $134.9bn / $9.17 (**$9.35**) | $143.1bn / $9.72 ($9.92) |
| vs FY27 consensus $9.40–9.84 [F] | below | **≈ consensus low end** | ≈ consensus high end |
| Revenue CAGR FY26→36 | 2.1% | 4.9% | 6.8% |
| Net income CAGR FY26(norm.)→36 | 1.2% | 4.9% | 7.8% |
| Terminal value share of EV | 52% | 56% | 60% |

*Calibration note (L-003).* My first base draft had FY27 EPS of $8.97, **4–5% below the consensus low**, with a lower FY27 margin. That is the same pattern the KLAC audit flagged (a below-consensus near-year EPS stacked on other bearish choices). I re-set the base to the consensus low end before running anything else. Remaining bearish-leaning choices, disclosed: FCF = 1.00× NI (not 1.03×) and the 14.72bn denominator (not 14.27bn). Together they are worth **~6%** (base $169 → $180 with both reversed). The bullish-leaning choice is A1, 0.5pt below CAPM (worth ~+7%). They roughly net out.

## 4. Reverse DCF — what does $356 imply?

**Method.** Owner earnings = FY26 net income ex-tariff refund **$131.44bn** [D] (FCF ≈ 1.03× NI in FY26, so NI is used as a conservative FCF proxy that treats SBC — NOT OBTAINED — as a cash cost). Market equity value = $356.27 × 14.72bn = **$5,244bn**, less net cash $56bn = **$5,188bn** of operating value to explain. Solve for the constant 10-year owner-earnings CAGR, then a perpetual terminal growth rate. Script: scratchpad `aapl.py` (arithmetic reproduced below).

| Discount rate | Required 10y CAGR (gT 3%) | (gT 3.5%) | Net cash = 0 | 14.27bn shares |
|---|---|---|---|---|
| 8.0% | **11.2%** | 10.2% | 11.4% | 10.8% |
| 8.5% | 12.6% | 11.7% | 12.7% | 12.2% |
| 9.0% | 13.9% | 13.1% | 14.0% | 13.5% |
| **9.5% (base)** | **15.1%** | 14.4% | 15.3% | 14.7% |
| 10.0% (pure CAPM) | 16.3% | 15.6% | 16.5% | 15.9% |
| 10.5% | 17.4% | 16.8% | 17.6% | 17.0% |

**Reading.**
- At my base 9.5%, $356 needs **~15% a year of total (not per-share) earnings growth for ten years**, then 3% forever. At an investor-friendly 8.0%, it still needs **~11%**.
- Against that: net income CAGR FY21→FY26 **6.9%** [R]; FY21→FY24 **flat** [R]; FY27 consensus EPS +5–10% [F]; Dec-qtr revenue guide +7–10% with GM down 2–3pt [R]; smartphone market −12% to −20% in 2026 [R]. The required rate is **roughly double** Apple's own five-year record, delivered for a decade, from a $479bn revenue base.
- Net cash and the share-count dispute move the answer by ≤0.6pt. **They are not what this question turns on.**
- What would justify $356 at 9.5% [D, solved]: revenue **+15.1%/yr for ten years at a flat 33% OM**, or **+12.9%/yr with OM rising to 40%**. At 8.5% and 3.5% terminal growth: **+11.6%/yr at a flat OM**. *(An earlier draft line said "+9% with OM to 42%"; that gives $277, not $356, and was corrected; see §6.)* Nothing in the department reports evidences any of these paths today.
- **Implied discount rate** (the other way round): see §6. On my base fundamentals the price implies an expected return of **~6.1%/yr** (4.8–7.3% across scenarios), an equity premium of **~1pt** over a 5.15% Treasury.

## 5. Normalised EPS (tariff refund, cyclical-peak test)

Each step is cumulative and derived; per-share at 14.72bn; after-tax via NI/OI 0.836; product revenue lost at the FY26 product GM of 39.3% [R], with opex assumed fixed.

| Step | Adjustment | EPS | P/E at $356.27 |
|---|---|---|---|
| Reported FY26 | — | **$8.98** | 39.7x |
| 1. Strip tariff refund | −$0.05 (Q4 only; full-year effect NOT OBTAINED) [R] | **$8.93** | 39.9x |
| 2. iPhone at mid-cycle | iPhone FY25 = $254.1bn/1.21 = $210.0bn [D]; mid-cycle = FY25–26 midpoint $232.1bn → −$22.0bn revenue × 39.3% × 0.836 = −$0.49 | **$8.44** | 42.2x |
| 3. + memory GM 45% sustained | −3.8pt GM on the remaining $456.8bn revenue × 0.836 = −$0.99 | **$7.45** | 47.8x |
| 4. + Google payment cut 100% | −$20bn × 0.836 = −$1.14 | $6.32 | 56.4x |

- **China +28% is mostly inside step 2**, since iPhone is the bulk of Greater China revenue. A separate China-only test (China FY26 $82.4bn, low confidence [R] → FY25 $64.4bn [D] → normalised at +10% instead of +28%) removes **$11.6bn revenue / ~$0.26 EPS**. It is not added to step 2, to avoid double counting.
- **Normalised EPS used in this report: $8.44–$8.93** (mid-cycle to ex-refund). Steps 3–4 are stresses, not normalisations: the Dec-qtr guide is evidence for 45–46% GM *now*, not for ten years, and the Google payment is currently being paid.
- **Is FY26 a cyclical peak?** Partly. Revenue +15%, iPhone +21%, China +28% on a smartphone market that shrank [R] is ASP/mix and share gain, not units [R Elon Musk]; the Dec-qtr guide (+7–10%, GM −2 to −3pt) is already the first step down. Against "peak": Apple *gained* share as the low end collapsed, and there is a deferred replacement pool if memory prices roll over in 2027–28 [R Elon Musk §3]. My base treats FY26 as a high-but-not-reversing level (FY27 +7% revenue, OM down 1.5pt); the bear treats it as a peak (FY28 −3%).
- **On any of the normalised EPS figures the trailing P/E is 40–42x**, versus a 5-year average of 30–33x and a 10-year median of 27.7x [F].

## 6. DCF — bear / base / bull with probabilities

Discount rate 9.5% in all three (§3 A1). Values per share, 14.72bn shares, net cash included.

| Scenario | Narrative | Fair value | at 8.5% | at 10.0% | Prob. | Implied return (IRR) if bought at $356.27 |
|---|---|---|---|---|---|---|
| **Bear** | FY26 was the peak: iPhone/China revert (FY28 −3%), GM ~46% sustained on memory/Siri costs, growth 3% then 2.5% | **$119** | $138 | $111 | 30% | **4.8%/yr** |
| **Base** | Guide-consistent FY27 (≈ consensus EPS $9.35), 5.5% growth fading to 3%, OM back to 33% | **$169** | $200 | $157 | 50% | **6.1%/yr** |
| **Bull** | Memory rolls over in 2027–28, deferred replacement pool returns, AI fees + Services mix lift OM to 36%, 8% growth, 3.5% terminal | **$224** | $270 | $207 | 20% | **7.3%/yr** |
| **Probability-weighted** | | **$165** | $196 | $153 | 100% | **6.1%/yr** |

- **Variants (base):** net cash at zero $165 (−$4); 14.27bn shares $175 (+3.2%); FCF 1.03× NI and 14.27bn shares $180.
- **Steel-man of the bull case (L-003).** Stack every generous choice at once: bull fundamentals (7.8% NI CAGR for ten years, above Apple's own 6.9% five-year record), an **8.0%** discount rate (an ERP of under 2.9pt over a 5.15% Treasury), 3.5% terminal growth, FCF = 1.03× NI, and the 14.27bn share count. Result: **$320**, which is **still 10% below $356.27**. At 8.5% the same stack gives $287. **I could not construct a defensible DCF that reaches the current price.**
- **Reading the IRR column.** This is the most rate-independent statement in the report. On my base fundamentals, an owner who pays $356.27 earns about **6%/yr** for ever after (4.8–7.3% across scenarios), against a 10-year Treasury at **5.15%** [F]. The price implies an equity risk premium of **~1pt**, against a Damodaran implied market ERP of 4.41% [F, unverified snippet].
- **Correction to §4.** I first wrote that revenue +9%/yr with OM rising to 42% would justify $356 at 9.5%. The arithmetic gives **$277**, so that claim was wrong and has been replaced. What is actually required at 9.5%: revenue **+15.1%/yr for ten years at a flat 33% OM**, or **+12.9%/yr with OM rising to 40%**. At 8.5% and 3.5% terminal growth: **+11.6%/yr at a flat OM**.

## 7. Special scenarios — Google payment cut; App Store toll; memory-cost GM compression

Applied to the **base** path at 9.5%. Each is a pre-tax operating-income reduction from **FY28** (a D.C. Circuit decision is realistically a 2027 event [R The dictator, estimate]), taxed at NI/OI 0.836. **No offset assumed** (e.g. a replacement search deal or Apple's own search ads); that is conservative and labelled.

**7a. Google default-search payment** (~$20bn/yr, trial-era estimate, ~100% margin assumed) [R]

| Cut | OI lost | EPS hit (annual) | Base fair value | Change |
|---|---|---|---|---|
| 0% (status quo: payments continue under Mehta remedies, 1-yr terms) | 0 | 0 | **$169** | — |
| 50% (annual renegotiation, or AI search eroding Safari queries) | $10bn | −$0.57 | **$163** | −3.9% |
| 100% (D.C. Circuit sides with DOJ cross-appeal → payment ban) | $20bn | −$1.14 | **$156** | −7.9% |

On the bull path, a 100% cut takes $224 to **$210**. **Why so small in value terms when it is ~13% of OI?** Because the base already values the operations at ~18x FY27 owner earnings ($2,432bn / $134.9bn) [D]; removing 13% of earnings removes ~8% of value once ten years of growth on the rest is included. **In market terms it is bigger:** at today's ~40x multiple, $1.14 of EPS is ~$45/share (~13%) if the multiple holds. The regulatory desk rates a payment ban a minority tail [R The dictator §1]; I assign it **~15% probability within the bear-weighted mass** (assumption) and do not add it separately to the probability weighting.

**7b. App Store commission (stressed separately from the rest of Services, per 菲比斯)**

Commission pool **~$32bn FY26 [A]** (Appfigures $27.4bn 2024 global; asymco ~$30bn LTM mid-2025 [F], grown at roughly Services' pace); incremental margin **85% [A]** (payment processing and review costs not disclosed).

| Stress | OI lost | Base fair value | Change |
|---|---|---|---|
| Pool −25% (court-set US link-out ceiling + DMA/Japan copycats) | $6.8bn | **$165** | −2.7% |
| Pool −50% (large developers move payments off-platform globally) | $13.6bn | **$160** | −5.4% |

The current US state (0% on link-outs) is already the adverse case, and the SCOTUS ruling (argument reported 11 Jan 2027) is **upside-skewed** for Apple [R The dictator §3]. **Combined worst case (Google 100% + App Store −50%): ~$147 (−13%).**

**7c. Memory-cost margin compression (GM 45% sustained)**

GM 45% at the FY26 opex ratio of 15.8% = **OM 29.2%** [D].

| Case | Base fair value | Change |
|---|---|---|
| GM 45% for FY27 only, then recovers (the guide as a transitory hit) | **$168** | −0.5% |
| **GM 45% for all ten years** | **$151** | −10.9% |
| GM 45% sustained **+** Google 100% cut | **$137** | −19% |

**Reading.** A one-year margin dip is almost irrelevant to value; a *permanent* one is worth ~11%. The Dec-qtr guide alone cannot distinguish the two. The deciding data are TrendForce mobile-DRAM prints for 1Q–2Q27 and Apple's FQ2 FY27 GM [R Elon Musk §6]. **None of the three stresses, alone or combined, is what puts value below price.** The gap between ~$165 and $356 comes from the base itself, not from the tails.

## 8. Method cross-check — P/E, FCF yield vs history and vs MSFT/GOOGL

| Method | Inputs | Value / share | Source |
|---|---|---|---|
| **DCF, probability-weighted** | §6; discount rate 10.0% → 8.5% | **$153 – $196**, central **$165** (9.5%) | [D] |
| Own history: 10y median P/E 27.7x | × normalised EPS $8.44–8.93 | $234 – $247 | [F] GuruFocus 13 Nov 2026 |
| Own history: 10y average 25–31x | × $8.44–8.93 | $211 – $277 | [F] Financecharts, Wisesheets, TIKR, FinBox (methods differ) |
| Own history: 5y average 30–33x | × $8.44–8.93 | $253 – $295 | [F] Financecharts (Nov 2026), Wisesheets, VCP |
| Peers: MSFT/GOOGL forward 23–27x | × FY27 consensus $9.40–9.84 | $216 – $266 | [F] Investing.com ~30 Oct 2026; TipRanks ~19 Sep 2026; Yahoo. **Not same-day; mixed fiscal bases** |
| **Relative band** | | **$215 – $295**, central **~$250** | [D] |
| Market today | | $356.27 = **39.9x** ex-refund trailing, **36–38x** FY27 consensus | [W] / [F] |

**Earnings and FCF yields.**

| | AAPL | MSFT | GOOGL | 10y UST |
|---|---|---|---|---|
| Earnings yield | 2.5% (trailing, normalised) · 2.6–2.8% (FY27 consensus) | ~3.7–4.3% (inverse of 23–27x fwd) | ~4.2–4.3% (inverse of 23–24x fwd) | **5.15%** |
| FCF yield | **2.6–2.7%** ($136.1bn / $5.08–5.24tn) [D] | **NOT OBTAINED** (latest quarter FCF $18.6bn, −27% y/y, after ~$39–45bn quarterly capex [F]; market cap not obtained) | **Not meaningful**: latest-quarter FCF reported **negative (−$9.1bn)** on $51.4bn capex; 2026 capex guided $195–205bn [F, sources disagree on quarter] | |

**Why DCF and multiples disagree (explained before anything is averaged).**
1. **Different questions.** The DCF asks what Apple is worth to a buyer who requires 9.5%. Multiples ask where Apple would trade if it re-rated to its own past or to its peers *in today's market*. Relative methods inherit the market's current pricing. The S&P 500 at ~19.8x forward [F, TipRanks/Yahoo ~12 Nov 2026] is a ~5.0% earnings yield, against a **5.15%** Treasury. The whole market is pricing a thin premium, so a relative value is a "no worse than the market" value, not an intrinsic one.
2. **History was set under other rate regimes.** Apple's 5-year average multiple was earned in a period whose rate history I did **not** obtain this session, so I cannot quantify the regime shift. The direction is clear, though: with a 5.15% Treasury, a 2.5% earnings yield is harder to defend than in any period I can source.
3. **Peers flatter Apple on P/E and penalise it on FCF.** This is the strongest relative argument for the bull. MSFT and GOOGL show 23–27x P/E, but their FCF is far below their earnings because of AI capex (GOOGL's latest quarter was FCF-negative). Apple's FCF ≈ its net income. **On cash, Apple's premium to peers is much smaller than the 36–38x vs 23–27x P/E gap suggests**, and Apple carries none of the AI-capex risk. That earns Apple *a* premium. It does not make 2.6% FCF yield cheap in absolute terms, and it is the reason I do not weight the peer-P/E line more heavily than its 25% share of the relative band.
4. **Both methods agree on direction.** Every method lands below $356.27. The most generous relative cell (5y-average 33x on ex-refund EPS) is **$295, 17% below price**. The most generous DCF stack (§6) is **$320, 10% below price**.

**Synthesis.** I weight intrinsic and relative **50/50**. That is not a split-the-difference: it says I expect *partial* convergence. The market's thin equity premium may persist for some years (relative), but over a holding period the cash flows decide (intrinsic).
- Low: (153 + 215)/2 ≈ **$185** · Central: (165 + 250)/2 ≈ **$210** · High: (196 + 295)/2 ≈ **$245**
- **Fair value range $185–$245, central $210.** Full envelope across methods: $153–$295 (bear DCF $119 and steel-man $320 excluded as tails).
- **Sell-side median $356.50** [R]: brokers value Apple on a forward-EPS multiple at roughly today's market multiple, so their targets are relative values that follow price. 修大哥's evidence (targets cut in July, now below spot through price movement) fits that reading. The two dated bear targets (KeyBanc $250, Jefferies $263.66) sit just above the top of my band; the other four bearish targets were not obtained.

## 9. Sensitivity tables

**9a. Base case: discount rate × stage-2 revenue growth (FY29–31; FY27 +7%; fade to 3%; OM path as base).** $/share. The base cell is in bold.

| r \ g2 | 3.5% | 4.5% | **5.5%** | 6.5% | 8.0% | 9.5% |
|---|---|---|---|---|---|---|
| 8.0% | 200 | 210 | 220 | 231 | 248 | 267 |
| 8.5% | 182 | 191 | 200 | 210 | 225 | 242 |
| 9.0% | 167 | 175 | 183 | 192 | 206 | 221 |
| **9.5%** | 154 | 162 | **169** | 177 | 190 | 203 |
| 10.0% | 144 | 150 | 157 | 164 | 176 | 188 |
| 10.5% | 134 | 140 | 147 | 153 | 164 | 175 |
| 11.0% | 126 | 132 | 137 | 144 | 153 | 164 |

**9b. Base case: discount rate × steady-state operating margin (FY29+).**

| r \ OMss | 29% | 31% | **33%** | 35% | 37% | 40% |
|---|---|---|---|---|---|---|
| 8.0% | 196 | 208 | 220 | 233 | 245 | 264 |
| 8.5% | 178 | 189 | 200 | 211 | 222 | 239 |
| 9.0% | 163 | 173 | 183 | 194 | 204 | 219 |
| **9.5%** | 151 | 160 | **169** | 179 | 188 | 202 |
| 10.0% | 140 | 149 | 157 | 166 | 174 | 187 |
| 10.5% | 131 | 139 | 147 | 155 | 162 | 174 |

**9c. Base case: terminal growth × discount rate.**

| gT \ r | 8.0% | 8.5% | 9.0% | **9.5%** | 10.0% | 10.5% |
|---|---|---|---|---|---|---|
| 2.0% | 196 | 181 | 168 | 156 | 146 | 137 |
| 2.5% | 207 | 190 | 175 | 162 | 151 | 142 |
| **3.0%** | 220 | 200 | 183 | **169** | 157 | 147 |
| 3.5% | 236 | 213 | 194 | 178 | 164 | 152 |
| 4.0% | 257 | 228 | 206 | 187 | 172 | 159 |

**Elasticities around the base (derived from the tables):** discount rate +0.5pt / −0.5pt → **−7% / +8%**; steady-state OM ±2pt → **−5% / +6%**; stage-2 growth ±1pt → **−4% / +5%**; terminal growth ±0.5pt → **−4% / +5%**. Largest discrete item: Google payment 100% cut → **−8%**. **No cell in any table reaches $356.27**; the highest is $267 (8.0% rate, 9.5% stage-2 growth).

## 10. Margin of safety at current price; HOLD / TRIM / ADD levels

MoS = (fair value − price) / fair value, at **$356.27**.

| Reference value | $ | MoS at $356.27 |
|---|---|---|
| DCF probability-weighted (9.5%) | 165 | **−116%** |
| **Blended central** | **210** | **−70%** |
| Top of blended range | 245 | −45% |
| Top of relative band (33x 5y-avg on ex-refund EPS) | 295 | −21% |
| Steel-man DCF (every generous choice stacked, §6) | 320 | −11% |

**Required margin of safety: 25%.** 菲比斯 rates the moat Wide (76/100), but slowly narrowing at the App Store toll, and requires 20%, **raised to 25% if the model holds the Services take rate flat**. My base holds group OM flat at 33% and does not explicitly erode the take rate (that is in the §7b stress only), so the 25% condition applies. I am not choosing the assumption that would earn the lower hurdle. At 20%, the levels below move by ~$10.

**Price at which the firm's required MoS is met:** 0.75 × $210 = **~$158** (at 20%: ~$168). That is **56% below** today's price and **35% below** the 52-week low of $242.57 [R].

**Levels (valuation-only recommendations for the CRO and PM; not orders):**

| Zone | Price | Reasoning |
|---|---|---|
| **ADD** | **≤ ~$158** | Required 25% MoS to the $210 central is met. Not plausible near-term (below the 52-week low); stated for completeness |
| **HOLD** | **~$158 – $245** | Inside the fair value range: owned at a price the cash flows can justify within a defensible discount rate |
| **TRIM** | **> $245** (top of range) | Above every central estimate. **Above $295** the price is beyond even the most generous relative cell; **$356.27 is there** |

**Valuation signal at $356.27: TRIM.** The price is 45% above the top of my range and above every method except a deliberately stacked steel-man, which still falls short. *How much* to trim, and whether tax lots, the SKHY memory-cycle hedge (Elon Musk: correlation −0.21, a fundamental partial hedge), or concentration limits change the answer, belongs to Zac, John and the committee, not to valuation. Momentum (RSI 60.9, +18.5% above MA200 [W]) is not a valuation input; 老詹 owns timing.

**Owner cost $357.60 (context only; L-003, no weight):** 0.4% above the price, 70% above the central, 46% above the top of the range, 21% above the most generous relative value. The cost basis changes none of the levels.

## 11. Expected annual return from today's price

10-year horizon, additive approximation [D]. Components are labelled; ranges are scenario-driven.

| Component | Bear | **Base** | Bull | Basis |
|---|---|---|---|---|
| Earnings yield (reference only, not added) | 2.5% | **2.5%** | 2.5% | $8.93 / $356.27 [D]. Funds the two lines below; the rest accumulates as cash |
| + Dividend yield | 0.3% | **0.3%** | 0.3% | [W] |
| + Buyback accretion (net share-count shrink) | 1.6% | **1.6%** | 1.6% | $85.8bn / $5.24tn [D]. Gross of SBC (NOT OBTAINED); shrinks as price rises; FY26 actual −1.9% [R] |
| + Organic net income growth | 1.2% | **4.9%** | 7.8% | §3 scenario CAGRs |
| **= Return at constant multiple (~40x)** | 3.1% | **6.8%** | 9.7% | — |
| + Multiple change over 10 years | to 25x: −4.6% | **to 30x: −2.8%** | to 35x: −1.3% | from 39.9x ex-refund trailing [D]; 25–35x spans the 10y median to 5y average and above [F] |
| **= Expected annual return** | **≈ −1.5%** | **≈ +4.0%** | **≈ +8.4%** | — |

- **Probability-weighted (30/50/20): ≈ +3.2%/yr.** Cross-check: the DCF IRR at $356.27 is **6.1%** (§6). It implicitly assumes a terminal multiple of ~33x FCF, i.e. little de-rating, so it is the upper estimate.
- **Hurdle comparison:** 10-year Treasury **5.15%** [F]; firm-implied required return 9.5%. **The base expected return is below the risk-free rate.** Only the bull case clears the Treasury by a margin; nothing clears 9.5% without the multiple *staying* near 40x *and* bull growth.

## 12. Valuation input to committee score

**Valuation score: 28 / 100** (higher = more attractive at the current price; scores the price, not the business).

| Calibration | Score | Situation |
|---|---|---|
| KLAC (Jul 2026, corrected) | 33 | ~2.2x base intrinsic; A-grade business with a 15%+ growth runway that could grow into the multiple |
| **AAPL at $356.27** | **28** | 1.7x blended central, 2.2x DCF; −70% MoS against a 25% requirement; ~5% organic growth; expected return (~3–4%) below the Treasury; above the steel-man DCF |
| SKHY ADS (Nov 2026) | 25 | −26% MoS, but two stacked downside mechanisms (cycle plus ADS-premium collapse) |

- **Not lower,** because the downside path is a slow de-rating, not a collapse. Wide moat; net cash ~$56bn; FCF ≈ NI with no AI-capex drain; realised vol 24.7% [W]. The bear DCF ($119) is a 30% scenario, not a solvency tail.
- **Not higher,** because no method, including one built to be generous, reaches the price.

**One-line verdict:** *A wide-moat, cash-rich franchise priced for ~15% a year of growth it has never sustained. Fair value $185–$245 (central $210); MoS −70% against a required 25%; valuation signal TRIM, with sizing left to John and Zac.*

**The three assumptions the value is most sensitive to:**
1. **Discount rate / required return** (+0.5pt/−0.5pt → −7% / +8%). Given a 5.15% Treasury, this is where the bull case must argue, and the market currently implies ~6%.
2. **Long-run growth** (terminal ±0.5pt → −4% / +5%; stage-2 ±1pt → −4% / +5%). Whether FY26's +15% revenue was a new level or a cyclical high.
3. **Steady-state operating margin** (±2pt → −5% / +6%). Memory costs (GM 45% sustained → −11%) and the Services toll (Google −8%, App Store −3 to −5%).

**What would move me** (pre-registered): up, if Q1–Q2 FY27 shows GM back above 47% with revenue ≥ +8% (memory roll-over plus a real replacement cycle), or if a Siri/AI fee tier shows priced, material Services revenue; down, if the D.C. Circuit disturbs the "payments permitted" holding, or FY27 iPhone revenue declines year on year.

**Anti-anchoring disclosure (L-003).** This is the firm's first Apple valuation, so there is no prior same-direction verdict to lock into. The risk here is the reverse: the stock sits at an all-time high, the Owner's cost is at that high, and the sell-side median equals the price. I did not let any of these into the model. In the other direction, I caught and corrected one bearish drift: a below-consensus FY27 EPS in the first base draft (§3). Remaining bearish-leaning choices (FCF = 1.00× NI; 14.72bn shares) are worth ~6% and are disclosed; the 0.5pt-below-CAPM discount rate offsets them. I also caught and corrected one arithmetic over-statement in §4.

## 13. NOT OBTAINED

1. **Any primary document.** I did not open the FY26 10-K, Apple's Newsroom release or the call transcript. Every company figure is Tier-2 (search-extracted by me or by the department reports). I made no direct page fetches in this session, so I hit no 403 or DNS failures myself; the departments report sec.gov, apple.com and macrumors.com as blocked.
2. **Cash balance verified against the filing.** $136.9bn is a search extraction of the 10-K and appears in no other firm report. The non-current securities figure (~$80bn) is by subtraction.
3. **Reconciliation of the share count** (14.27bn Webull vs 14.72bn derived). Shown as a ±3.2% sensitivity.
4. **Stock-based compensation.** This is why FCF is proxied by NI.
5. **Effective tax rate.** NI/OI 0.836 is used instead.
6. **Capex verified** (~$9.0bn from a low-quality source).
7. **Full-year tariff-refund effect** (only Q4's $0.05 is known).
8. **Google payment** size for FY25/26, its margin, and the D.C. Circuit argument date.
9. **App Store commission pool for FY26.** The $32bn is my assumption grown from 2024–25 third-party estimates; the incremental margin of 85% is also an assumption.
10. **Same-day peer multiples.** The MSFT/GOOGL forward P/Es are dated Sep–Oct 2026 on mixed bases. MSFT and GOOGL market caps and FCF yields were not obtained.
11. **Date distribution of the 45 analyst targets.**
12. **Historical 10-year Treasury series** (for the rate-regime argument in §8).
13. **ERP figure confirmed** (Damodaran 4.41%, 1 Nov 2026, from a garbled snippet) and an **authoritative beta** (1.09 Yahoo; sources range 0.57–1.11).
14. **FY22–FY25 Services gross margin trend**, needed to test 菲比斯's "slowly narrowing" claim against the margin line.
15. **Fleet-average memory cost per iPhone**, and the TrendForce 1Q27 mobile-DRAM forecast.
16. **The full text of 菲比斯's moat report.** I used the CEO's summary plus keyword extracts, not a full read.

## 14. Sources (fetched or searched 2026-11-16; tradingkey.com not used)

- Apple FY2026 10-K (cash $136.9bn, via search extraction): https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000026/aapl-20260926.htm ; FourWeekMBA: https://fourweekmba.com/ai-apple-bought-54-9b-of-securities-in-fy26-6x-its-capex/
- 10y Treasury 13 Nov 2026: [CNBC](https://www.cnbc.com/2026/11/13/treasury-yields-fed-rates.html), [Forbes](https://www.forbes.com/advisor/investing/treasury-rates/), [Investing.com](https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield-historical-data), [Mortgage News Daily](https://www.mortgagenewsdaily.com/treasury/10yr)
- ERP: [Damodaran Online](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm); [Damodaran Data Update 2 for 2026](https://aswathdamodaran.substack.com/p/data-update-2-for-2026-a-testing)
- Beta: [Yahoo Finance AAPL](https://finance.yahoo.com/quote/AAPL/), [Finbox](https://finbox.com/BVL:AAPL/explorer/beta/), [WallStreetNumbers](https://wallstreetnumbers.com/stocks/aapl/beta)
- Consensus and forward P/E: [Yahoo/TipRanks "Apple Shares Look Expensive Heading into 2027"](https://www.tipranks.com/news/article/apple-shares-aapl-look-expensive-heading-into-2027), [Chartmill](https://www.chartmill.com/news/AAPL/Chartmill-57483-Apple-NASDAQAAPL-Falls-After-Revenue-Shortfall-Tariff-Lifted-Margins-and-iPhone-Duo-Supply-Constraints), [Stockrow](https://stockrow.com/AAPL), [American Banking News 25 Oct 2026](https://www.americanbankingnews.com/2026/10/25/fy2027-eps-estimates-for-apple-increased-by-erste-group-bank.html)
- AAPL P/E history: [Financecharts](https://www.financecharts.com/stocks/AAPL/value/pe-ratio), [GuruFocus](https://www.gurufocus.com/term/pettm/AAPL), [Wisesheets](https://www.wisesheets.io/pe-ratio/AAPL), [TIKR](https://www.tikr.com/blog/apples-p-e-ratio-current-levels-historical-trends-and-outlook), [FinBox](https://finbox.com/NASDAQGS:AAPL/explorer/pe_ltm_avg_10y/), [VCP Scanner](https://vcpscanner.com/stock/aapl/pe-history)
- Peers: [Investing.com MSFT vs GOOGL](https://www.investing.com/news/stock-market-news/microsoft-vs-alphabet-earnings-execution-versus-valuation-discount-93CH-4984441), [TipRanks MSFT vs GOOGL](https://www.tipranks.com/news/article/microsoft-vs-alphabet-one-ai-stock-gets-an-upgrade-but-the-sidelines-call-for-the-other-says-top-investor), [Investing.com hyperscaler FCF](https://uk.investing.com/news/stock-market-news/microsoft-only-us-hyperscaler-with-positive-free-cash-flow-as-ai-capex-bites-93CH-4819848), [Windowsforum capex/FCF](https://windowsforum.com/news/microsoft-vs-alphabet-ai-capex-corrected-2026-cash-flow-backlog-and-azure-capacity.446341/)
- App Store commissions: [TechCrunch / Appfigures, 8 May 2025](https://techcrunch.com/2025/05/08/appfigures-apple-made-over-10b-from-us-app-store-comissions-last-year/), [asymco, 6 Jun 2025](https://asymco.com/2025/06/06/the-purpose-of-the-app-store/)
- Firm reports on disk: `reports/equity/2026-11-16-aapl-financials.md`, `-management.md`, `-moat.md`; `reports/news/2026-11-16-aapl-news.md`, `-regulatory.md`; `reports/industry/2026-11-16-aapl-industry.md`; calibration `reports/equity/2026-07-19-klac-valuation.md`, `2026-11-12-skhy-valuation.md`, `reports/committee/2026-07-19-klac-audit.md`; `memory/lessons.md` (L-003).
- Arithmetic: Python scripts in the session scratchpad (`aapl.py`, `aapl2.py`); every figure is reproduced in the tables above.

*Research only. Not financial advice, not an order, not a recommendation to the Owner. The committee and the Owner decide; John (CRO) may veto.*

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
