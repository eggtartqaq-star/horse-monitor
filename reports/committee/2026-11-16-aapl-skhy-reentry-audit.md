# Audit — AAPL pipeline (2026-11-16) and SKHY re-entry analysis

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence) · **Date:** 2026-11-16 · **Status:** IN PROGRESS — §1 complete

**Checklist.** The brief cites "C1–C10 as defined in `reports/committee/2026-11-13-skhy-audit.md`". **That file defines only C1–C9, and they are SKHY-specific topics** (premium, survival ratios, valuation, cap, HBM claim, tradingkey, price timeline, CEO inference-as-fact, sizing). No C10 exists anywhere on disk (Grep `C10` across the repo matches only this file). I therefore apply the 13 Nov audit's *method* as a generic ten-point checklist, carrying over its named tests and its 床狗 patterns (a)–(e):

| # | Test (origin in 13 Nov audit) |
|---|---|
| C1 | Load-bearing figures reproduce from stated inputs (13 Nov C1/C3/C4/C9 method) |
| C2 | Every load-bearing number has a dated source or is labelled derived/assumption (rule 5) |
| C3 | Inputs agree across desks (13 Nov C1b) |
| C4 | Prose numbers are computed, not typed (pattern c) |
| C5 | Stale / retired figures not carried as live (13 Nov C5) |
| C6 | tradingkey.com not cited (13 Nov C6) |
| C7 | Dates, sessions, price timeline consistent (13 Nov C7) |
| C8 | Inference / estimate / NOT OBTAINED not stated as fact (13 Nov C8; pattern b) |
| C9 | Conclusion strength ≤ evidence strength; model limits disclosed |
| C10 | Bias: direction of discretionary choices; dissent present; corrections propagated (patterns a, e) |

**Network.** `pages.stern.nyu.edu` and `fred.stlouisfed.org` failed DNS (ENOTFOUND) — not retried. Three WebSearches were run (ERP, 10y Treasury); results are cited where used. No Bash tool: every computation is shown by hand.

## 0. Verdict summary
_pending_

## 1. AAPL valuation (𢦀鳩仔) — `reports/equity/2026-11-16-aapl-valuation.md` — **PASS WITH CORRECTIONS**

### 1a. Arithmetic re-derived (C1) — reproduces

**Reverse DCF (§4), re-run by hand.** Owner earnings E0 = $131.44bn; operating value to explain $356.27 × 14.72bn = 5,244.3 − 56 = **$5,188bn** ✓.
- r 9.5%, g 15.1%, gT 3%: q = 1.151/1.095 = 1.05114; Σq^t (t=1..10) = 1.05114 × (1.64670 − 1)/0.05114 = 13.292 → PV years 1–10 = 131.44 × 13.292 = **1,747**. E10 = 131.44 × 1.151^10 (= 4.0809) = 536.4; TV = 536.4 × 1.03/0.065 = 8,500; ÷ 1.095^10 (2.4782) = **3,430**. Total **5,177** vs 5,188 target → g solves at ≈15.1% ✓.
- r 8.0%, g 11.2%: q = 1.02963; Σ = 11.784 → 1,549; E10 = 131.44 × 2.8910 = 380.0; TV = 380.0 × 20.6 = 7,828 ÷ 2.1589 = 3,626. Total **5,175** ✓ (≈11.2%).

**Base DCF (§6, $169), re-run from §3 inputs.** Revenue 478.83 → FY27 +7% = 512.35; FY28–31 +5.5%; FY32–36 fade 5.0/4.5/4.0/3.5/3.0%. OM 31.5% → 32.25% → 33%. NI = OI × 0.836.
- NI path ($bn): 134.92, 145.73, 157.32, 165.97, 175.10, 183.86, 192.14, 199.82, 206.81, 213.02. FY27 EPS 134.92/14.72 = **$9.17** ✓; ÷0.98 = **$9.35** ✓. Revenue CAGR 772.14/478.83 → **4.9%** ✓; NI CAGR 213.02/131.44 → **4.9%** ✓.
- PV at 9.5% (DF 0.9132 … 0.4035): Σ = **1,073.7**; TV = 213.02 × 1.03/0.065 = 3,375.5 × 0.40351 = **1,362.1**; EV = **2,435.8** (file: $2,432bn ✓); TV share 55.9% (file 56% ✓). (2,435.8 + 56.2)/14.72 = **$169.3** ✓.
- Google 100% cut from FY28 (§7a): 16.72bn/yr × ΣDF(yr2–10) 5.3656 = 89.7 + TV 16.72 × 1.03/0.065 × 0.40351 = 106.9 → 196.6/14.72 = −$13.36 → **$155.9** ✓ ($156, −7.9%). App Store −25%/−50% scale to $164.7 / $160.2 ✓; combined $146.8 ✓.
- PW: 0.3×119 + 0.5×169 + 0.2×224 = **$165.0** ✓; at 8.5% $195.4 ✓; at 10% $153.2 ✓; 25/50/25 $170.3 ✓.
- Normalised EPS steps 2–4: −22.05 × 0.393 × 0.836/14.72 = −$0.49 ✓; 456.78 × 0.038 × 0.836/14.72 = −$0.99 ✓; 16.72/14.72 = −$1.14 ✓. P/Es 39.7/39.9/42.2/47.8/56.4x ✓.
- Relative cells: 27.7 × 8.44–8.93 = 233.8–247.4 ✓; 25–31x → 211–277 ✓; 30–33x → 253–295 ✓; 23–27x × 9.40–9.84 → 216–266 ✓.
- Blend: (153+215)/2 = 184 ✓; (165+250)/2 = **207.5** (published "$210", rounded up 2.5); (196+295)/2 = 245.5 ✓. MoS at 210: −69.7% ✓ (at 207.5: −71.7%; immaterial).
- §11: 85.8/5,244 = 1.64% ✓; ln(30/39.9)/10 = −2.81% ✓; to 25x −4.57% ✓; to 35x −1.30% ✓; PW 3.23% ✓. Sensitivity elasticities (−7.1/+8.3/−5.3/+5.9/−4.1/+4.7/+5.3%) ✓. MoS table, $158/$168 entry, 35% below 52w low ✓.

**C1 result: PASS.** Every figure I re-ran reproduces to the stated precision. Two cosmetic slips: central 207.5 → "$210"; A6 says GM 45–46% ⇒ OM "29.5–30.5%" but 45 − 15.8 = **29.2** and 46 − 15.8 = **30.2** (§7c itself uses 29.2%) — Low.

### 1b. Discount rate 9.5% / ERP 4.41% / beta 1.09 (C2, C3, C10)

**Firm precedent (Grep `reports/equity/*valuation*`):** MU 11.0% (rf 4.55% + β1.4 × ERP 4.75%, line 35); KLAC 10.5% base / 9.5% bull (rf 4.55% + ERP ~5% × β1.4–1.6, lines 95, 106); MRVL 11% base, and calls 9% "a wide-moat rate" (lines 70, 129); BE 9.5–12.5%; SKHY 11% KRW. Re-pricing AAPL on the **firm's own precedent ERP (~5%)** gives 5.15 + 1.09 × 5.0 = **10.6%**. The 9.5% is therefore **at or below** firm precedent for a β≈1.1 name — consistent, and if anything lenient. Defensible.

**ERP 4.41% — UNVERIFIED, possible digit transposition (MEDIUM).** The source is self-described as a "garbled snippet". My WebSearch ([search results summarising Damodaran's site](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm)) returned a latest Damodaran implied ERP of **4.14%** (T12m, adjusted payout; variants 3.56–6.05%), dated ~1 Sep 2026; no November figure; the site itself failed DNS here. 4.41 vs 4.14 is the classic transposition pattern. Effect if 4.14% is right: CAPM = 5.15 + 1.09 × 4.14 = **9.66%** (not 9.96%), so the "0.5pt below CAPM, worth ~+7%" offset in §3 becomes ~0.16pt (~+2%), and the claim that bullish and bearish choices "roughly net out" weakens to a **net ~4% bearish tilt**. Does not move any signal.

**10y Treasury 5.15% on 13 Nov — UNVERIFIED, contrary nearby data (MEDIUM).** Two WebSearches found: FRED DGS10 **4.86% (6 Nov), 4.88% (9 Nov)**; Advisor Perspectives 4.86% on 6 Nov; YCharts shows **5.15% on 19 Oct 2026**; 5.15% also touched ~24 Sep ([YCharts](https://ycharts.com/indicators/10_year_treasury_rate), [Advisor Perspectives 6 Nov 2026](https://www.advisorperspectives.com/dshort/updates/2026/11/06/treasury-yields-snapshot-november-6-2026), [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/586498)). 5.15% on 13 Nov requires +27bp in four sessions. Possible (the file says a Dec hike is being priced), but the exact figure matches a dated October print. Not resolvable from here; FRED DNS-blocked. **Effect if ~4.9%:** CAPM 9.4–9.7% — 9.5% still defensible; but the headline "expected return below the risk-free rate" (§1, §11) becomes 4.0% vs ~4.9%, and the price-implied ERP ~1.2pt instead of ~1pt. Rhetoric moves, signal does not.

**Beta 1.09 — defensible, but a firm-produced contrary figure is ignored (LOW–MEDIUM).** The CEO's primary-bar report the same day (`reports/technical/2026-11-16-skhy-live-kline-and-aapl-switch.md` §1) computes AAPL **beta to SPY 0.38** (90 sessions, correlation 0.20). It is a short, low-R² window and not a credible long-run beta, but it is on disk and the valuation lists only Yahoo 1.09 / Finbox 1.11 / WSN 0.57. See 1c for why this matters.

### 1c. "I could not construct a defensible DCF that reaches the current price" (C9) — fair as a judgement, overstated as written

- The report's own numbers locate the break-even. Steel-man stack: $287 at 8.5%, $320 at 8.0% (×1.115 per −0.5pt). One more step: **≈$357 at 7.5%**. So **bull fundamentals at a ≤~7.5% cost of equity reach the price.** 7.5% = 5.15% + ERP 2.35pt; at ERP 4.41% that is β ≈ 0.53; at 4.14%, β ≈ 0.57 — i.e. the "stale outlier" WSN beta (0.57) the file dismisses. On base fundamentals the price needs ~6.1% (β ≈ 0.2).
- Against that, the market-implied ~6% return vs a 5.15% (or ~4.9%) Treasury means the market prices Apple as a quasi-bond. "Not defensible" is a reasonable judgement under standard 5y beta (~1.1) and any ERP ≥ ~3%. But the Owner-facing sentence should state the condition, not the conclusion.
- **Correction (MEDIUM, §1 bullet 3, §6 steel-man, §8.4, §12):** replace "I could not construct a defensible DCF that reaches the current price" with: "The price is reached only by bull fundamentals (7.8% NI CAGR for ten years) at a cost of equity ≤~7.5% (ERP ≤~2.3pt, β ≈0.55), or by base fundamentals at ~6.1%. I regard neither as defensible against a ~1.1 five-year beta and a ~4.1–4.4% market ERP."

### 1d. Headline expected return: 4% or 6%? (C8, C10 — MEDIUM)

§1 bullet 2 and §11 headline **"≈ +4%/yr base … versus a 5.15% Treasury"** and state "the base expected return is below the risk-free rate". §6 calls the **6.1%** DCF IRR "the most rate-independent statement in the report", and §12 says "the market currently implies ~6%". The two differ only by the exit multiple: §11 de-rates to 30x; the IRR implicitly exits at 1.03/(0.061 − 0.03) = **33.2x** (file says ~33x ✓). The Owner-facing headline picks the de-rating construction, which is the one that lands below the Treasury. **Correction:** "Expected return ≈ +3–6%/yr on base fundamentals (+4% if the multiple de-rates to 30x, +6% if it holds ~33x), versus a 10y Treasury of ~4.9–5.15%." Also §8 point 1–2 compare a 2.5% *earnings yield* with a 5.15% *nominal* Treasury (Fed-model comparison: real-ish vs nominal); the report's own IRR framing is the correct one and already makes the point — Low.

### 1e. "Priced for ~15% a year of growth it has never sustained" (C8 — MEDIUM, Owner-facing verdict line, §1 and §12)

The evidence in the file is the five-year record (FY21→26 NI CAGR 6.9%). "Never" is false over Apple's history: FY2005 → FY2015 net income grew from ~$1.3bn to ~$53bn (≫15%/yr; auditor's knowledge of Apple's 10-Ks, not re-fetched this session). The defensible statement is scale-bound. **Correction:** "priced for ~15% a year of total earnings growth for a decade — more than double its 6.9% five-year record, from a $479bn revenue base."

### 1f. Bearish-leaning choices (C10) — disclosed; one is better described as an error

- FCF 1.00× vs 1.03× NI: +3%. Disclosed with reasons (SBC NOT OBTAINED, working-capital tailwind). Acceptable.
- 14.72bn vs 14.27bn: +3.2%. 14.72bn = 132.18/8.98 is the **FY26 weighted-average diluted** count. A per-share value struck *today* needs the current diluted count, which after ~297m shares bought back in FY26 is almost certainly **below** the FY average. So 14.72bn is not a neutral "choice" but a likely overstatement of the denominator; 14.27bn may be closer. Resolve from the 10-K cover-page share count. Low (+3%).
- Combined: 169 × 1.03 × 1.032 = **$179.6** ✓ (file "$180"; "~6%" ✓). Against 1b, the offsetting A1 credit is ~+2% not ~+7% if the ERP is 4.14%. **Net bearish tilt ≈ 4%** — immaterial against a −70% MoS.

### 1g. Unsourced or weakly sourced numbers (C2)

| Item | Status | Severity |
|---|---|---|
| ERP 4.41% | garbled snippet; search shows 4.14% latest (1b) | Medium |
| 10y 5.15% 13 Nov | contrary 6–9 Nov prints 4.86–4.88% (1b) | Medium |
| Capex ~$9.0bn | "low-quality source", disclosed | Low |
| Cash $136.9bn | single search extraction, first appearance in firm files; disclosed; not load-bearing (~1%) | Low |
| App Store pool $32bn, 85% margin | labelled [A] | OK |
| Google ~$20bn | trial-era estimate, labelled [R] — see §4 | Low |
| Relative-band central "~$250" | not derived; band midpoint is $255 | Low |
| Required MoS 25% | from a moat report the analyst **did not read in full** (§13 #16) | Low (MoS −70% fails any hurdle) |

C6 tradingkey: §14 states not used; no tradingkey URL in the file ✓.

### 1h. Verdict — PASS WITH CORRECTIONS
Arithmetic is clean and unusually well self-audited (two self-corrections disclosed). Required corrections: 1b (ERP and 10y flagged UNVERIFIED with the contrary datapoints; restate the "net out" claim), 1c (conditional wording), 1d (4–6% range), 1e ("never sustained"). **None changes the TRIM signal** — see §7.

## 2. AAPL technical (CEO for 老詹) — reports/technical/2026-11-16-aapl-technical.md
_pending_

## 3. SKHY re-entry (CEO) — reports/technical/2026-11-16-skhy-reentry.md
_pending_

## 4. Cross-desk consistency
_pending_

## 5. Skim of remaining AAPL reports
_pending_

## 6. CRO ruling consistency
_pending_

## 7. Does the TRIM signal survive? Does the SKHY no-re-entry verdict survive?
_pending_

## 8. Patterns for 床狗
_pending_
