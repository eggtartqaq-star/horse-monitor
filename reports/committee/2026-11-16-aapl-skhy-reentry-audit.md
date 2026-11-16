# Audit — AAPL pipeline (2026-11-16) and SKHY re-entry analysis

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence) · **Date:** 2026-11-16 · **Status:** COMPLETE

**Under audit (full depth):** `reports/equity/2026-11-16-aapl-valuation.md` (𢦀鳩仔); `reports/technical/2026-11-16-aapl-technical.md` (CEO for 老詹); `reports/technical/2026-11-16-skhy-reentry.md` (CEO); `reports/risk/2026-11-16-aapl-and-skhy-reentry-cro.md` (John; read after completion, commit abf6982 per coordinator). **Skimmed:** AAPL financials, moat, management, news, regulatory, industry (all 2026-11-16). No audited report was edited.

**Checklist.** The brief cites "C1–C10 as defined in `reports/committee/2026-11-13-skhy-audit.md`". **That file defines only C1–C9, and they are SKHY-specific topics** (premium, survival ratios, valuation, cap, HBM claim, tradingkey, price timeline, CEO inference-as-fact, sizing). No audit checklist C10 exists on disk. ("C1–C10" does appear in the CRO ruling B.1, where it refers to the CRO's 12 Nov SKHY *hold conditions* — a different thing; the brief may have conflated the two.) I therefore apply the 13 Nov audit's *method* as a generic ten-point checklist, carrying over its named tests and its 床狗 patterns (a)–(e):

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

| Report | Verdict | HIGH | MEDIUM | Key items |
|---|---|---|---|---|
| AAPL valuation (𢦀鳩仔) | **PASS WITH CORRECTIONS** | 0 | 6 | Arithmetic fully reproduces. ERP 4.41% and 10y 5.15% unverified, with contrary search data (4.14%; 4.86–4.88% on 6–9 Nov); two betas in use across desks; "no defensible DCF" needs its condition stated (bull + ≤7.5% cost of equity reaches price); headline 4% vs 6% expected return; "growth it has never sustained" false as worded |
| AAPL technical (CEO for 老詹) | **PASS WITH CORRECTIONS** | 0 | 2 | All 15 probability cells reproduce. "Unfilled gap $334.25–340.73" contradicted by its own $338.04 6 Nov low; "no technical sign of a top" contradicted by its own §3 |
| SKHY re-entry (CEO) | **PASS WITH CORRECTIONS — fix before Owner release** | 0 | 4 | Probability table reproduces, but the log-driftless model implies +29%/6m expected drift; at zero expected return, $61.44-in-6m is 22–40%, not 15–29%. "Never own again", "quota is exhausted", ₩850,000 underived |
| CRO ruling (John) | **PASS WITH CORRECTIONS** | 0 | 1 | All A and B arithmetic reproduces; consistent with `config/risk-limits.yaml`. The 6.4% is a CRO construction stricter than the config's literal rule (10%) and should be labelled so. Inherits ₩850,000 and the 4%-vs-Treasury line |
| Financials / moat / management / news / regulatory / industry | skim: **PASS WITH CORRECTIONS** (moat, management, news, financials) · **PASS** (regulatory, industry) | 0 | 3 | Moat equates all Services (43.7%) with "the toll + Google"; management's Siri test is mis-specified and misses on-disk evidence; grading scales conflict |

**No HIGH-severity finding. The TRIM signal survives (§7). The SKHY no-re-entry verdict survives (§7).**

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

**V1 — ERP 4.41% UNVERIFIED, possible digit transposition (MEDIUM; §2 line 51, §3 A1, §6).** The source is self-described as a "garbled snippet". My WebSearch (result summary of Damodaran's site, [pages.stern.nyu.edu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm) — the page itself failed DNS here) returned a latest implied ERP of **4.14%** (T12m, adjusted payout; variants 3.56–6.05%), dated ~1 Sep 2026; no November figure found. 4.41 vs 4.14 is the classic transposition pattern. Effect if 4.14% is right: CAPM = 5.15 + 1.09 × 4.14 = **9.66%** (not 9.96%), so the "0.5pt below CAPM, worth ~+7%" offset in §3 becomes ~0.16pt (~+2%), and the claim that bullish and bearish choices "roughly net out" weakens to a **net ~4% bearish tilt**. Does not move any signal. **Correction:** mark 4.41% UNVERIFIED with the 4.14% datapoint; restate the "net out" sentence.

**V2 — 10y Treasury 5.15% on 13 Nov UNVERIFIED, contrary nearby data (MEDIUM; §2 line 50, §1, §11).** Two WebSearches found: FRED DGS10 **4.86% (6 Nov), 4.88% (9 Nov)**; Advisor Perspectives 4.86% on 6 Nov; YCharts shows **5.15% on 19 Oct 2026**; ~5.15% also touched ~24 Sep ([YCharts](https://ycharts.com/indicators/10_year_treasury_rate), [Advisor Perspectives 6 Nov 2026](https://www.advisorperspectives.com/dshort/updates/2026/11/06/treasury-yields-snapshot-november-6-2026), [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/586498)). 5.15% on 13 Nov requires +27bp in four sessions. Possible (the file says a Dec hike is being priced), but the figure exactly matches a dated October print. Not resolvable here (FRED DNS-blocked). **Effect if ~4.9%:** CAPM 9.4–9.7% — 9.5% still defensible; but the headline "expected return below the risk-free rate" becomes 4.0% vs ~4.9%, and the price-implied ERP ~1.2pt instead of ~1pt. Rhetoric moves, signal does not. **Correction:** cite the H.15/DGS10 13 Nov value or mark UNVERIFIED.

**V3 — Beta: two betas for one stock across desks (MEDIUM, C3).** The CEO's primary-bar report the same day (`reports/technical/2026-11-16-skhy-live-kline-and-aapl-switch.md` §1) computes AAPL **beta to SPY 0.38** (90 sessions, correlation 0.20), and the CRO ruling uses that 0.38 (A.2 #4, A.8) to call AAPL "low beta". The valuation lists only Yahoo 1.09 / Finbox 1.11 / WSN 0.57. A 90-session beta with R² ≈ 4% is not a credible long-run estimate. But **the firm is using two betas for one stock, one per desk, each in the direction that suits its argument.** See 1c for why it matters. **Correction:** the valuation addresses the 0.38 in one line; the CRO labels 0.38 as short-window.

### 1c. V4 — "I could not construct a defensible DCF that reaches the current price" (C9, MEDIUM) — fair as a judgement, overstated as written

- The report's own numbers locate the break-even. Steel-man stack: $287 at 8.5%, $320 at 8.0% (×1.115 per −0.5pt). One more step: **≈$357 at 7.5%** [auditor's extrapolation]. So **bull fundamentals at a ≤~7.5% cost of equity reach the price.** 7.5% = 5.15% + ERP 2.35pt; at ERP 4.41% that is β ≈ 0.53; at 4.14%, β ≈ 0.57 — i.e. the WSN beta the file dismisses as a stale outlier. On base fundamentals the price needs ~6.1% (β ≈ 0.2). With the CEO's 0.38 beta: CAPM = 5.15 + 0.38 × 4.41 = 6.83% < bull IRR 7.3% → the bull DCF exceeds the price.
- Against that: a ~1.1 five-year beta is the standard input, and the market-implied ~6% return against a ~4.9–5.15% Treasury means the price treats Apple as a quasi-bond. "Not defensible" is a reasonable judgement. But the Owner-facing sentence should state the condition, not the conclusion.
- **Correction (§1 bullet 3, §6 steel-man, §8 item 4, §12):** replace with: "The price is reached only by bull fundamentals (7.8% NI CAGR for ten years) at a cost of equity ≤~7.5% (ERP ≤~2.3pt, β ≲0.55), or by base fundamentals at ~6.1%. I regard neither as defensible against a ~1.1 five-year beta and a ~4.1–4.4% market ERP."

### 1d. V5 — Headline expected return: 4% or 6%? (C8, C10 — MEDIUM)

§1 bullet 2 and §11 headline **"≈ +4%/yr base … versus a 5.15% Treasury"** and state "the base expected return is below the risk-free rate". §6 calls the **6.1%** DCF IRR "the most rate-independent statement in the report", and §12 says "the market currently implies ~6%". The two differ only by the exit multiple: §11 de-rates to 30x; the IRR implicitly exits at 1.03/(0.061 − 0.03) = **33.2x** (file says ~33x ✓). The Owner-facing headline picks the construction that lands below the Treasury. The CRO ruling (A.3 item 3, A.9) has already inherited "below the Treasury". **Correction:** "Expected return ≈ +3–6%/yr on base fundamentals (+4% if the multiple de-rates to 30x, +6% if it holds ~33x), versus a 10y Treasury of ~4.9–5.15% (13 Nov figure unverified)." Also §8 items 1–2 compare a 2.5% *earnings yield* with a 5.15% *nominal* Treasury (Fed-model comparison); the report's own IRR framing is the correct one — Low.

### 1e. V6 — "Priced for ~15% a year of growth it has never sustained" (C8 — MEDIUM; Owner-facing verdict line, §1 line 19 and §12 line 307)

The evidence in the file is the five-year record (FY21→26 NI CAGR 6.9%). "Never" is false over Apple's history: FY2005 → FY2015 net income rose from ~$1.3bn to ~$53bn, far above 15%/yr (auditor's recollection of Apple's 10-Ks; not re-fetched this session). **Correction:** "priced for ~15% a year of total earnings growth for a decade — more than double its 6.9% five-year record, from a $479bn revenue base."

### 1f. Bearish-leaning choices (C10) — disclosed; one is better described as a likely error

- FCF 1.00× vs 1.03× NI: +3%. Disclosed with reasons (SBC NOT OBTAINED, working-capital tailwind). Acceptable.
- 14.72bn vs 14.27bn: +3.2%. 14.72bn = 132.18/8.98 is the **FY26 weighted-average diluted** count. A per-share value struck *today* needs the current diluted count, which after ~297m shares bought back in FY26 is almost certainly **below** the FY average. So 14.72bn is not a neutral choice but a likely overstatement of the denominator. Auditor's recollection (unverified): the FY25 10-K cover showed ~14.78bn outstanding in Oct 2025, which less FY26 buybacks implies ~14.5–14.6bn — between the two desk figures. Resolve from the FY26 10-K cover page. Low (≤+3%).
- Combined: 169 × 1.03 × 1.032 = **$179.6** ✓ (file "$180"; "~6%" ✓). Against V1, the offsetting A1 credit is ~+2%, not ~+7%, if the ERP is 4.14%. **Net bearish tilt ≈ 4%** — immaterial against a −70% MoS.

### 1g. Unsourced or weakly sourced numbers (C2)

| Item | Status | Severity |
|---|---|---|
| ERP 4.41% | garbled snippet; search shows 4.14% latest (V1) | Medium |
| 10y 5.15% on 13 Nov | contrary 6–9 Nov prints 4.86–4.88% (V2) | Medium |
| Capex ~$9.0bn | "low-quality source", disclosed | Low |
| Cash $136.9bn | single search extraction, first appearance in firm files; disclosed; ~1% of value | Low |
| App Store pool $32bn, 85% margin | labelled [A] | OK |
| Google ~$20bn | "trial-era estimate", labelled — see §4.4 | OK |
| Relative-band central "~$250" | not derived; band midpoint is $255 | Low |
| Required MoS 25% | from a moat report the analyst **did not read in full** (§13 #16) | Low (MoS −70% fails any hurdle) |

C6: §14 states tradingkey not used; no tradingkey URL in the file ✓.

### 1h. Verdict — PASS WITH CORRECTIONS
Arithmetic is clean and unusually well self-audited (two self-corrections disclosed, L-003 calibration applied). Required corrections: V1–V6. **None changes the TRIM signal** (§7).

## 2. AAPL technical (CEO for 老詹) — `reports/technical/2026-11-16-aapl-technical.md` — **PASS WITH CORRECTIONS**

The bars are not on disk as data (Glob `**/*aapl*.{csv,json,parquet}` → none), so I check the report against itself, the news desk and the CEO's switch report.

### 2a. What reproduces (C1)
- vs cost: 356.27/357.60 → −0.37% ✓; 360.83 → +0.9% ✓; 338.04 → −5.5% ✓; 334.25/340.73 → −6.5%/−4.7% ✓; 325.08 → −9.1% ✓; 308.91 → −13.6% ✓; 300.77 → −15.9% ✓.
- Trend: 356.27/345.91 = +3.0% ✓; /338.79 = +5.2% ✓; /300.77 = +18.5% ✓; MACD hist 4.21 − 3.29 = 0.92 ✓. Bollinger: L = 345.91 − (357.92 − 345.91) = 333.90; %b = 22.37/24.02 = **0.93** ✓. ATR 8.21/356.27 = 2.3% ✓. +46.9% from the 52w low ✓.
- Cross-report: SKHY column (101%, −9.0/−10.9%, −37.6%, 32.6%, +1.06, $10.10/7.7%) matches the switch report §1/§3 ✓. AAPL 12m figures (24.7%, +33.0%, −13.8%, 1.2%) match ✓. 4 Nov +5.31% / 89.6m matches 修大哥 ✓.

**Barrier-touch table — all 15 cells re-run.** P = 2·N(ln(B/S)/(σ√T)), S = 356.27.
| Level | ln(B/S) | 1m (σ√T = 0.279×0.2887 = 0.0805) | 3m (0.222×0.5 = 0.111) | 6m (0.247×0.7071 = 0.1747) |
|---|---|---|---|---|
| $340 | −0.04675 | z −0.580 → **56.2%** ✓ | z −0.421 → **67.4%** ✓ | z −0.268 → **78.9%** ✓ |
| $330 | −0.07660 | −0.951 → **34.2%** ✓ | −0.690 → **49.0%** ✓ | −0.439 → **66.1%** ✓ |
| $325 | −0.09186 | −1.141 → **25.4%** (file ≈26%) | −0.828 → **40.8%** ✓ | −0.526 → **59.9%** ✓ |
| $308.91 | −0.14264 | −1.771 → **7.7%** ✓ | −1.285 → **19.9%** ✓ | −0.817 → **41.4%** ✓ |
| $290 | −0.20581 | −2.555 → **1.1%** ✓ | −1.854 → **6.4%** ✓ | −1.178 → **23.9%** ✓ |

The table reproduces. At 25% vol the log-driftless assumption implies only ~+3%/yr drift, so the model choice that matters for SKHY (S1) does not matter here.

### 2b. Findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| T1 | **MEDIUM** | §3 last para, §4 "Gap zone", §6 add zone | "**Unfilled** gap between $334.25 and $340.73" — but §4 gives the **6 Nov swing low $338.04**, which is *inside* that gap. The gap was partly filled on 6 Nov; on the report's own levels the unfilled remainder is **$334.25–338.04**. (C3 internal) | "Partly filled 6 Nov to $338.04; unfilled remainder $334.25–338.04"; restate the "$334–341 retest zone" accordingly |
| T2 | **MEDIUM** | §2 last line | "Primary trend is up, **with no technical sign of a top**" is contradicted by §3, which lists a volume divergence at the new high — the caution the report itself says "often precedes a pause". Judgement stated as fact (C8) | "Primary trend is up; the only caution signs are the volume divergence and the extension (§3)" |
| T3 | LOW–MED | §3 item 1 | "New high on **falling volume** … thinning participation" rests on a two-day comparison (13 Nov 40.0m vs 4 Nov 89.6m, the window's event day). The up/down ratio 0.67 covers a 20-session window that includes the 3 Nov post-earnings gap-down — an event, not a participation trend. No 20d/50d average volume is given (C9) | Give 13 Nov volume vs 20d and 50d average; say the 0.67 includes the 3 Nov earnings session |
| T4 | LOW–MED | §2 | "Monthly closes rose for **seven months straight**, from $253.15 (Mar)". Unverifiable from disk, and in tension with 修大哥 (news line 53: Jan→Jun move to "roughly the $330s") and the 31 Jul close of $308.91 — if June closed above $308.91, July was a down month and the streak breaks. Also counts mid-month Nov as a "monthly close" (C7) | Print the monthly close series; label Nov month-to-date |
| T5 | LOW | NOT OBTAINED #4 vs §4 | Bars "appear dividend-adjusted" (4 Nov $349.24 vs $349.51), yet the $308.91 31 Jul level equals the **unadjusted** close reported by 修大哥 (news line 61). Mixed bases; ~$0.27–0.55, immaterial | State which levels are adjusted |
| T6 | LOW | §5 footnote | "$325 interpolated between the $330 and $320 rows" — **there is no $320 row.** 3m/6m cells equal the direct calculation; only 1m (26%) matches an interpolation from an unshown $320 value (18.3%); direct is 25.4% (C4) | Print direct values 25% / 41% / 60% and drop the note |
| T7 | LOW | §1 | "a low-volatility **core holding**" — no portfolio classification exists (`config/portfolio.yaml` empty) (C8) | "a low-volatility large-cap" |
| T8 | PROCESS | §6 | The "review trigger" at $325.08 does not satisfy `per_trade.stop_required: true` ("老詹's invalidation level"), and there is no 老詹 sign-off. **Resolved by the CRO:** amended to a binding close-basis exit; 老詹 to confirm within 5 sessions (CRO A.5, A-2, A-3) | 老詹 sign-off by 21 Nov |

Also checked, consistent: 3 Nov range $325.08–334.25 contains the implied 3 Nov close (349.51 − 17.61 = **$331.90**) ✓; 4 Nov low $340.73 > 3 Nov high ✓ (a true gap); 2 Nov 2026 = Monday, 3 Nov Tuesday (midterms), 4 Nov Wednesday ✓; "−4% during the 2 Nov call" matches 修大哥 ✓.

**C8 direction check.** Unlike the 12 Nov SKHY synthesis, the CEO's hardenings here run **both ways** (T2 bullish, T3 bearish). No directional bias found.

### 2c. Verdict — PASS WITH CORRECTIONS
Statistics, levels and the probability table reproduce. Fix T1–T4 before 老詹 signs off; T1 matters most because the gap is the report's only "add" zone.

## 3. SKHY re-entry (CEO) — `reports/technical/2026-11-16-skhy-reentry.md` — **PASS WITH CORRECTIONS (fix S1–S4 before Owner release)**

### 3a. Arithmetic and cross-file checks (C1, C3)
- +$8.00 / 129 = **6.20%** ✓; 137 − 131.79 = **$5.21**, ÷131.79 = **3.95%** ✓. 131.79/102.40 = **+28.7%** ✓; 102.40/131.79 = −22.3% ✓; 0.6 × 102.40 = **$61.44** ✓; 0.6 × 1,070,000 = **₩642,000** ✓.
- §2 "buying back at $131 isn't a 3.8% gain": 5.21/137 = 3.80% (sale-price base) vs 3.95% in §0 (hold-value base) — two bases for one number, Low.
- Exit date: 12 Nov range $134.04–139.56 contains $137; 11 Nov low $137.49 and 13 Nov high $135.76 exclude it (switch report §3) → "consistent with 12 Nov" ✓.

**Probability table — 14 endpoints across 7 of the 12 cells re-run** (S = 131.79; σ 101% / 75.7%):
| Cell | ln(B/S) | σ = 1.01 | σ = 0.757 | File |
|---|---|---|---|---|
| $122.20, 1m | −0.07555 | z −0.259 → 79.6% | −0.346 → 73.0% | 73–80% ✓ |
| $102.40, 1m | −0.25233 | −0.865 → 38.7% | −1.155 → 24.8% | 25–39% ✓ |
| $102.40, 3m | −0.25233 | −0.500 → 61.7% | −0.667 → 50.5% | 51–62% ✓ |
| $80, 1m | −0.49917 | −1.712 → 8.7% | −2.284 → 2.2% | 2–9% ✓ |
| $80, 6m | −0.49917 | −0.699 → 48.5% | −0.933 → 35.1% | 35–48% ✓ |
| $61.44, 3m | −0.76315 | −1.511 → 13.1% | −2.016 → 4.4% | 4–13% ✓ |
| $61.44, 6m | −0.76315 | −1.069 → 28.5% | −1.426 → 15.4% | 15–29% ✓ |
Life vol 98.9% sits inside the bracket (e.g. $102.40 1m → 37.7%) ✓. **The table reproduces as computed.**

**Korean-ordinary comparison vs `reports/equity/2026-11-12-skhy-valuation.md`:** FV ₩1,070,000 ✓ (line 133); +13% to +21% ✓ (1,212,000/1,070,000 = 1.133; 1,299,000/1,070,000 = 1.214; valuation line 217 "13–21% above the central") ✓; $102 blended / $80 parity ✓; premium risk $300–340 per $1,000 = 1 − 1/1.431 → 30.1%, 1 − 1/1.522 → 34.3% ✓; 1 share ≈ US$906–971 at ₩1,337.5 ✓.

**Gates vs `reports/risk/2026-11-12-skhy-cro-review.md`:** "Risk score ≥ ~40 for any initiation — FAIL 32/100" matches CRO 12 Nov lines 24/230 ✓. Precision (Low): 32 was the **hold** score; the CRO's 16 Nov ruling now scores an ADS initiation at **26** (B.6), so the gate fails by more than shown. `committee_approval_required: true` ✓. Zac's 7.5–10% stop-only ceiling ✓ (sizing line 27) — the CRO has since declined to adopt it (B.3).

**Propagation of the 13 Nov audit — credit.** The CEO now uses the dated-FX **43–52%** (not 44–56%), **$300–340 per $1,000** (≈⅓, not "half its value"), "31 Dec … **derived**" for the Wuxi licence, and (switch report §6) "no written firm rule sets [the 40% MoS]". Pattern (a) has improved.

### 3b. Findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| S1 | **MEDIUM** | §6 model; "Two things follow" | **The model choice is undisclosed and not neutral at 100% vol.** "Driftless random walk" here means zero drift in **log** price, which implies an expected *price* gain of e^{σ²T/2} − 1 = e^{0.255} − 1 ≈ **+29% over six months** at 101% vol. Under a zero-expected-return (martingale) price, log drift μ = −σ²/2 and P = N((b − μT)/σ√T) + (S/B)·N((b + μT)/σ√T). Re-run: **$61.44 in 6m → 22–40%** (σ 0.757: 12.3% + 2.145 × 4.5% = 22.0%; σ 1.01: 23.8% + 2.145 × 7.7% = 40.4%) vs published 15–29%; **$102.40 in 3m → 57–69%** vs 51–62%. The published table makes low levels look more remote (C9) | State the log-driftless assumption and its implied +29%/6m drift; show the martingale column, or quote "15–40%" / "51–69%" |
| S2 | **MEDIUM** | §6 "If you only ever buy at $61, you will most likely never own SKHY again" | A claim about an unbounded horizon drawn from a six-month model. Under the report's own driftless model the touch probability **rises toward 1** as the horizon lengthens (C8) | "On this model there is a ~15–40% chance of reaching $61 within six months" |
| S3 | **MEDIUM** | §4 line 46 | "a Korea Securities Depository quota on ADR issuance **is exhausted**" — present-tense fact. The 13 Nov audit register and the CRO (16 Nov NOT OBTAINED #16) list the quota status after July as **NOT OBTAINED** (C8, same pattern as 13 Nov) | "was reported exhausted as of 23 Jul; current status NOT OBTAINED" |
| S4 | **MEDIUM** | §7 R2 | "≤ $80 / **≈₩850,000**" — ₩850,000 is derived nowhere. ADS $80 is the **parity** fair value, whose ordinary equivalent is ₩1,070,000 (= R1); ₩850,000 implies an unexplained ~26% premium, or is the R1/R3 midpoint (₩856,000) unlabelled (C2). **The CRO has now made ₩850,000 a binding trigger (B-4)** without deriving it | Derive it or label it "≈ midpoint of R1 and R3"; the CRO updates B-4 to match |
| S5 | LOW–MED | §4 line 45 | "The dominant risk in the ADS is not SK hynix. It's the premium." The premium (30–34% to parity) is the risk **no stop can intercept**. It is not the largest: a cycle halving of the ordinary is −49% to −51% at parity (13 Nov audit C7b) (C8) | "The risk no stop protects against is the premium" |
| S6 | LOW | §4 line 66 | "Even on the ordinary, price is above fair value **today**" — last Korean print 10–11 Nov (C7) | "as of 10–11 Nov" |
| S7 | LOW | §3 heading | "The gates … (**firm rules**)": the valuation gate (40% MoS) is desk judgement | "(firm rules and desk requirements)" |
| S8 | LOW | §5 Cycle row | "any two of **老詹's** falsifier list, per Elon Musk §11.3" — the list is Elon Musk's (memory-cycle §11.3, lines 349–354, "move me back to OVERWEIGHT"). Item 1 drops "conventional" and "QoQ" (the CRO B.4 correctly says "Elon Musk's falsifiers") | Re-attribute; restore "≥+15% QoQ, conventional DRAM" |
| S9 | LOW | §8 | "~24–28 Dec" watch window has no source (tickets use "by 24 Dec") | Cite or drop |
| S10 | LOW | §4 | The ordinary removes premium risk but adds KRX access, settlement and direct KRW exposure; only access is mentioned (the CRO B.3 covers this) | One line |

**C8 count and direction.** Four Medium (S1–S4) plus six Low. **All run the same way: they make re-entry look less attractive** — the same direction as the 12 Nov synthesis (see §8). The difference from 13 Nov: no wrong headline number, a reproducible table, and the audit's corrections propagated. Hence PASS WITH CORRECTIONS, not FAIL. But S1–S4 must be fixed before the Owner sees the document.

## 4. Cross-desk consistency

### 4.1 Siri — who is right, and is the "slip #3" test valid? (MEDIUM)
- **News (修大哥 lines 34, 50, 121–123):** "[FACT] Siri AI shipped in beta around 14 Sep 2026", English-only, no EU. Sources for the date: **iClarified 2026-09-10** (dated *before* the event it supports) and **pasqualepillitteri.it** (personal blog). Corroboration on disk that something shipped: Apple support documentation (9 Sep) on daily usage limits for server-side features "including Siri AI"; MacRumors 9 Nov "Apple Continues to Say Some AI Features Will Have Fees for Extra Usage"; the 2 Nov guide citing "**costs from the Siri AI ramp**" (Reuters/iPhoneWired). Moat (line 261): shown at WWDC; "sources disagree on whether it has fully shipped".
- **Management (Peter, lines 62–68, 173):** "Delivery status as of 2026-11-16 **not obtained**"; WWDC unveiling excluded as "single, low-reliability source".
- **Ruling.** The news desk is **substantively right**: on-disk evidence from three independent lines (Apple support doc, MacRumors, the CFO's guide) shows a Gemini-based Siri was released to users by Nov, in a limited (English, non-EU, metered) form. Its **exact date and "beta" status are [OUTLET]-grade, not [FACT]** — the label should be downgraded (LOW). The management desk is **accurate about its own searches but stale against the firm's own files**: the WWDC unveiling it excluded is carried by MacRumors in the news file.
- **The "slip #3 if not GA by 31 Dec" test is mis-specified.** (1) The promise it tests (Apr 2026 call, per management's own source) was "on schedule for **this year**" — not "GA". A public English beta from ~Sep 2026 arguably meets "this year" for US English. (2) Apple has a history of keeping "beta" labels on Apple Intelligence features for long periods, so a GA-label test would score a naming convention as a slip. **Correction:** re-specify as a scope test — by 31 Dec 2026, do the 2024-announced capabilities (personal context, on-screen awareness, in-app actions) work in shipped US-English builds? Non-English and EU absence is a separate scope limit, not a slip unless promised. Re-score the "Promise vs delivery" pillar (11/25) after reconciling with the news file. Grade impact likely +0 to +3; no effect on TRIM.

### 4.2 Services share of gross profit — 40.2% vs 43.7%: compatible (LOW, labelling) — but see the moat's use of it (MEDIUM)
- Financials (lines 25, 72): FY26 Services GP 93.9 ÷ total 233.6 = **40.2%** ✓; revenue share 123.3/478.83 = 25.8% ✓.
- Moat (lines 25, 199–203): **Q4 FY26** 31.6 × 76.0% = 24.0 ÷ (114.5 × 47.9% = 54.8) = **43.7–43.8%** ✓.
- Different periods; both reproduce. The September quarter is a light product quarter, so its Services share runs high. **But** the moat uses the quarterly figure for annual exposure claims (lines 414, 457 "43.7% of GP is exposed"), and twice equates **all Services** with the contested rent: line 22 "About 44% of Apple's gross profit comes from that rent"; line 335 "the App Store toll and the Google search payment — **the 43.7% of gross profit**". Services also includes AppleCare, iCloud and subscriptions, and the moat itself says it "cannot split the 43.7% into its parts" (line 205). **MEDIUM (C8)** for lines 22/335; **correction:** "Services, ~40% of FY26 gross profit (43.7% in Q4), of which the toll and the Google payment are an unquantified part".

### 4.3 Grading scales — inconsistent across desks (MEDIUM, for the Committee)
- Financials-desk usage on disk: AAPL **A− 78**; MSFT **A− 79** (`2026-08-21-msft-financials.md:58`); 6160.HK **A− 82**; SKHY **B+ 72** (statements-only "A− (~88)"); MRVL B− 66; BE B− 67; INTC C+ 55; MiniMax D+ 48. De facto financials A− spans **78–88**.
- Management's proposed mapping (line 137): **A− ≈ 85–89, B ≈ 70–79**. Under it, AAPL financials 78 and MSFT 79 are **B**, and SKHY's financials "B+ 72" is a B.
- AAPL financials 78 is consistent with the MSFT A− 79 precedent **within the financials desk** ✓. The conflict is between desks. The CRO's score cites "A− 78" (A.9).
- **Required:** the Committee scores on the **numeric** values only until one mapping is ratified; nobody converts letters across desks. The proposed mapping also leaves gaps (no B−, C+ or ≥90 bands).

### 4.4 Google payment ~$20bn — provenance and caveats
- Provenance: US v. Google trial evidence for **2022** (regulatory line 227: "USD ~20bn/yr is the 2022 trial figure, not re-sourced"). It is a revenue share, so its 2026 value could be higher (search growth) or lower (AI erosion); four years stale either way.
- Caveats by desk: regulatory ✓ (dated 2022); industry ✓ ("trial evidence for an earlier year", line 144); financials ✓ ("estimate … may be stale … trial evidence", line 89); valuation ✓ ("trial-era estimate", plus ~100% margin labelled an assumption). **CRO A.9** writes "Google ~$20bn/yr" bare (LOW). News carries MoffettNathanson's "more than a quarter of OI" as [OUTLET], likely stale — inconsistent with ~13% of FY26 OI and not reconciled (LOW).
- **Appeal date conflict (LOW):** financials line 100 "DOJ and states filed notices of appeal **13-Apr-2026**" (single source, flagged unverified) vs regulatory line 48 "**3 Feb 2026** cross-appeal" (MediaPost 30 Jul 2026), which the valuation uses. Financials should defer to the regulatory desk's dated source.

### 4.5 Share count 14.72bn vs 14.27bn (LOW)
Both desks flag it unreconciled. Financials line 125: MarketBeat Q3 basic ≈14.7bn supports the higher figure; the FY weighted-diluted method overstates a current count (see 1f). Market-cap ratios use 14.27bn (financials lines 81, 123) while per-share values use 14.72bn — **the same report family uses both denominators for different ratios.** Disclosed; ≤3.2% on any figure. Resolve from the FY26 10-K cover page.

### 4.6 Greater China +21% vs +28%: compatible (LOW, labelling)
- News: **Q4** $17.54bn vs $14.49bn = **+21.0%** ✓ (own arithmetic, labelled).
- Financials: **FY** +28% (single source S7); $82.4bn "low confidence". Check: 82.4 ÷ 1.28 = **$64.4bn** FY25 — the same FY25 base the valuation derives (§5) — so the $82.4bn looks like the segment basis after all. Implied Q1–Q3: 82.4 − 17.54 = 64.86 vs 64.4 − 14.49 = 49.9 → **+30%**, then +21% in Q4: a deceleration, consistent with the Stocktwits "tapering" headline. Compatible. Both desks should label the period every time the figure is used (the valuation's "China +28% revert" is correctly FY).

## 5. Skim of remaining AAPL reports (C1–C10, sampled lines only)

| Report | Verdict (skim) | Findings |
|---|---|---|
| Financials (巴爺爺) | PASS WITH CORRECTIONS | Appeal date 13 Apr vs 3 Feb (4.4); grading scale (4.3); FY21/FY23–FY25 NI and EPS rows match the auditor's recollection of Apple's 10-Ks. Share count flagged ✓; FY24 dip cause flagged unverified ✓. No tradingkey citation |
| Moat (菲比斯) | PASS WITH CORRECTIONS | "44% of GP is rent" / "toll + Google = 43.7%" (4.2, MEDIUM). Q4 figure used for annual claims. 43.7% cross-check reproduces ✓ |
| Management (Peter) | PASS WITH CORRECTIONS | Siri evidence on disk not incorporated; WWDC exclusion; slip-#3 test mis-specified (4.1, MEDIUM). Proposed grade mapping conflicts with financials-desk usage (4.3). Recollection items correctly excluded from the score ✓ |
| News (修大哥) | PASS WITH CORRECTIONS | "[FACT] beta ~14 Sep" rests on a 10 Sep source and a blog → [OUTLET] (LOW). The Lapaas +7% vs +5.3% contradiction is disclosed, not hidden ✓. "The mean is dragged down by a handful of bears" is labelled [READ] ✓ |
| Regulatory (The dictator) | PASS | $20bn dated to the 2022 trial ✓; appeal timeline dated and sourced ✓; tradingkey excluded ✓ |
| Industry (Elon Musk) | PASS | $20bn caveated ✓; Counterpoint figures dated and graded ✓; tradingkey excluded ✓ |

C6 (tradingkey): Grep across all 2026-11-16 files → every mention is an exclusion note; zero citations ✓.

## 6. CRO ruling consistency — `reports/risk/2026-11-16-aapl-and-skhy-reentry-cro.md` — **PASS WITH CORRECTIONS**

The file was complete when read (Rulings A and B, consolidated conditions, NOT OBTAINED, disclosures).

### 6a. Arithmetic (C1) — reproduces
- **Ruling A:** stop distance 325.08/356.27 → −8.75% ✓; tail $325.08 × 0.9265 = **$301.19** ✓ (the coordinator's 301.17 uses 7.354%; immaterial); 301.19/356.27 → **−15.46%** ✓; 1% ÷ 15.46% = **6.47% → 6.4%** ✓; from cost −15.78% ✓. E[loss] 0.6 × 8.75 + 0.3 × 12.11 + 0.1 × 15.46 = **10.43%** → 9.6% ✓. Held-through caps 3.2 / 2.4 / 1.5% ✓. Stress table (all 20 cells) ✓. Trim formula: $360.83 → 6.05%; $370 → 5.38% ("5.3%", rounded down); $380 → 4.82%; $400 → 4.05% ✓. Option B: 308.91 × 0.9265 = 286.21 → −19.66%; blended 17.56% → **5.69% → 5.6%** ✓. Proximity line 325.08/0.9265 = **$350.87** ✓. −10% day: 292.57 → −17.9% → 1.15% of LNW ✓. Score 27.0 + 9.75 + 4.0 + 5.5 + 5.0 + 6.0 = **57.25** ✓. Hedge ratio −0.21 × 24.7/101 = −0.051 ✓. Disclosure thresholds 356.27/0.10 = $3,563; /0.064 = $5,567 ✓.
- **Ruling B:** cap (i) at p = 52/50/45/43/25/20/15% → 2.92/3.00/3.22/3.33/5.00/6.00/7.67% ✓; (ii) 5.35/4.90/4.22% ✓; B.2 table (parity ÷1.45, ×10 × 1,350–1,380) all ✓; R1 pair equivalence "~29% premium" (102.40 × 13,500/1,070,000 = 1.292) ✓; min-ticket $790 ÷ (0.05/3) = **$47,400** ✓; ADS score 26.0 ✓; ordinary 40.25 ✓; "to ~48" = 40.25 + 3.75 + 3.75 = 47.75 ✓. The coordinator's ADS cap formula "1% ÷ (p/(1+p))" equals the file's 1% ÷ [1 − 1/(1+p)] ✓.

### 6b. Consistency with `config/risk-limits.yaml`
| Limit | CRO use | Consistent? |
|---|---|---|
| `max_risk_per_trade: 0.01 # size x distance to stop` | Sized on distance **plus one worst-day gap** (15.46% → 6.4%). Literal config reading gives 1% ÷ 8.75% = 11.4% → capped at 10% | **Stricter than the config, disclosed** (A.4 method note; proposed config change (c), "NOT applied"). Legitimate under veto authority, same pattern as the 12 Nov premium extension. **But** A.1 and A.2 #9 present ">6.4%" as "over `max_risk_per_trade`" / "FAIL" — that is the CRO's reading, not the file's text. See R1 |
| `max_single_position: 0.10` (at cost) | >10% = breach, reduce next session | ✓ |
| `max_single_position_drifted: 0.15` | Not available to a position bought above 10% | ✓ reasonable reading, stated |
| `leverage: none` | Webull −$12.06 flagged as breach on face; KRW buying power prohibited | ✓ |
| `stop_required: true` | CEO review trigger rejected as a stop; 老詹 sign-off required | ✓ |
| `max_var_95_1d: 0.03` | Name VaR only; portfolio not computable | ✓ |
| `committee_approval_required`, `decision_record_before_ticket` | Add blocked; retrospective record required; R1 committee | ✓ |
| `live_trading: forbidden`; CLAUDE.md rule 1 | "No agent places … orders" ✓; the "resting limit sell at $360.83" is framed as the Owner's choice ✓ | ✓ |
| Country/FX | No line in config; CRO proposes a line, not a number | ✓ |

### 6c. Valuation TRIM vs CRO "HOLD up to 6.4%" — not a contradiction, but the Owner could read it as one
They answer different questions. The valuation's TRIM is a **price** signal (above $245) that explicitly leaves sizing to John and Zac (valuation §10). The CRO's HOLD is a **survivability** ruling: at ≤6.4% with the stop, no limit is breached. The CRO does not overrule TRIM. A.4 says trimming toward ~3.2% is "recommended (valuation/conviction) but not required"; the add veto above $245 adopts the valuation's level; and the mechanical cap shrinks as price rises, so it trims into strength in the same direction. **The firm's coherent position for the Owner is: "Valuation recommends a trim; risk permits holding up to 6.4% only with the hard stop; Zac's conviction rule points to ~3.2%; a trim is mandatory only above 6.4%."** The committee pack should print that sentence. A bare "HOLD APPROVED" headline would mislead.

### 6d. Findings
| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| R1 | LOW–MED | A.1, A.2 #9, A-4 | 6.4% presented as a config-limit fail; it is a stricter CRO construction (6b) | Label as "CRO ruling under rule 3, pending config change (c)"; config-literal ceiling is 10% |
| R2 | MEDIUM | B.4 amendment 1, B-4 | Adopts **₩850,000** as a binding KRW trigger with no derivation (inherits S4) | Derive or label as R1/R3 midpoint |
| R3 | LOW–MED | A.3 item 3, A.9 | "Base expected return ~4% … below the 5.15% Treasury" inherits V2/V5 (4–6% range; 13 Nov rate unverified) | Update once the valuation is corrected |
| R4 | LOW | §0 line 16, B.2, B.4 | USD/KRW **1,350–1,380 [A]**, although a dated ₩1,337.5 (10 Nov) is on disk in the valuation and was the 13 Nov audit's corrected input (propagation, pattern a). At 1,337.5, $102.40 at zero premium = ₩1.37m (+28%), not ₩1.38–1.41m; immaterial | Use the dated rate, keep the band as sensitivity |
| R5 | LOW | B.2 (ii) vs B.3 | Formula uses the 13.7% worst day (16 Jul); the 5.0% ceiling is derived with 13.4% (1 ÷ 20.1%). With 13.7%: 1 ÷ 20.4% = **4.9%** | Use one gap figure |
| R6 | LOW | B.4 amendment 4 | "1% ÷ 40% ≈ 2.4%" — it is **2.5%** (C4) | Fix |
| R7 | LOW | A.7 | "About −3% after hours on 2 Nov" cites CEO tech §6 and 修大哥, both of which say **about −4%** | −4% |
| R8 | LOW | A.4 tail | A close-basis stop exits at the **next** open, so the realised tail is the breach-day close plus one more overnight gap; 15.46% understates it slightly. Partly covered by the ~5% pre-print recommendation | One sentence |
| R9 | LOW | A.2 #4, A.8 | Uses the 90-session 0.38 beta to classify AAPL as low-beta while the valuation uses 1.09 (V3) | Label 0.38 short-window |
| R10 | LOW | A.9 | "Google ~$20bn/yr" without the 2022/estimate caveat (4.4) | Add caveat |

## 7. Does the TRIM signal survive? Does the SKHY no-re-entry verdict survive?

**AAPL TRIM — SURVIVES.**
- Every correction I raise either leaves value unchanged or moves it modestly. Stacking all of them in the bullish direction (FCF 1.03×, share count resolved toward 14.27bn, CAPM ≈ 9.4% on ERP 4.14% and rf ~4.9%) lifts the base from $169 to roughly **$180–185** and the PW DCF to ~$175–180. With the relative band unchanged, the blended central becomes **~$213–215** [auditor's estimate from the file's own elasticities: (175 to 180 + 250)/2]. MoS stays around **−66% to −68%** against a 20–25% hurdle.
- The relative band tops out at $295 (−17% vs price) on the file's own history; the corrections do not touch it.
- What would overturn it: accepting bull fundamentals *and* a ≤~7.5% cost of equity (β ≲0.55). That is the explicit bull argument the Committee should hear (V4); no desk on disk makes it.
- **Scope of the signal:** TRIM is a valuation signal. The *amount* is the Committee's, inside the CRO's 6.4% risk cap (6c). The CRO's hard stop and the mandatory trim above 6.4% stand independently of valuation.

**SKHY no-re-entry — SURVIVES.**
- At $131.79 the ADS is 28.7% above the $102.40 blended value — negative MoS at a **0%** hurdle — so no re-specification of the 40% hurdle changes it (13 Nov C3f still applies).
- The CRO has independently **VETOED** re-entry in both instruments (B.1). The ADS initiation scores 26 and the ordinary 40 (at the line, not above it). Premium unmeasured → ADS cap zero. Committee not convened. Leverage flag open.
- My findings S1–S4 change the *odds* shown for the conditional plan (lower levels are likelier than shown under a zero-drift price) and the *wording*. They do not change the verdict at today's price. If anything, S1 makes the conditional plan's triggers **more** reachable, which favours keeping the plan written down.

## 8. Bias observations and patterns for 床狗

**Bias.**
1. **Directional hardening on SKHY persists (narrative lock-in).** The 12 Nov synthesis hardened 10 inferences bearish; today's re-entry note hardens S1–S5 the same way ("dominant risk", "never own again", "is exhausted", a model that makes low prices look remote). The verdict is independently supported, so it did not change the outcome. It is still the second consecutive SKHY document from the same author with one-directional hardening.
2. **Desk-convenient inputs (C3).** One stock, two betas: 1.09 where a high discount rate is argued (valuation), 0.38 where low risk is argued (CEO, CRO). Neither desk mentions the other's figure.
3. **Headline selection.** The valuation headlines the 4% (below-Treasury) construction over its own 6.1% IRR (V5); the CRO then cites it. Each step was disclosed somewhere; the Owner-facing line kept the bearish one.
4. **Dissent check (groupthink).** Every desk is at or below "fully priced" on AAPL. The only on-disk bull voices are the sell-side median ($356.50) and the valuation's own steel-man ($320). No desk was tasked to argue the low-beta/quasi-bond case (V4), which is the actual argument for the price. Unanimous caution deserves the same scrutiny as unanimous enthusiasm. **Recommend:** the Committee assigns one desk to argue it before voting.
5. **Credit where due.** The valuation self-corrected twice and disclosed its bearish choices with sizes; the CEO propagated four 13 Nov corrections; the CRO's arithmetic is clean across every check I ran (§6a).

**Recurring patterns for 床狗 (prompt fixes):**
- (f) **Snippet numbers.** A figure from a "garbled snippet" cannot be used as a point input. It is shown as a range with the nearest verified datapoint, or marked UNVERIFIED in the headline (V1).
- (g) **Model assumptions at extreme volatility.** Any barrier/touch probability on an instrument with σ > 50% must state whether drift is zero in log or in price, and show both (S1).
- (h) **One stock, one input.** Beta, share count and the risk-free rate are firm-level inputs, recorded once in `knowledge/` with a date. Desks cite that record rather than choosing their own (V3, 4.5, R4).
- (i) **Underived trigger levels.** Any price level that becomes a trigger needs a one-line derivation where it first appears; downstream desks may not adopt a level that has none (S4 → R2).
- (j) **Unbounded-horizon claims** ("never", "most likely never") are banned unless the model horizon supports them (V6, S2).
- Carry-over from 13 Nov: (b) epistemic tags must survive synthesis — S3 is a repeat of the 13 Nov "NOT OBTAINED stated as fact" pattern.

## Required fixes (summary)

| Report | Before Committee / Owner |
|---|---|
| Valuation | V1, V2 (mark UNVERIFIED, cite the contrary datapoints); V3 (one line on 0.38); V4 (conditional wording); V5 (4–6% range); V6 ("never sustained") |
| AAPL technical | T1 (gap partly filled), T2 ("no sign of a top"), T3, T4; 老詹 sign-off (T8) |
| SKHY re-entry | S1 (model drift disclosure / martingale column), S2, S3, S4 — **before Owner release**; S5–S10 at next revision |
| CRO | R1, R2 before Committee; R3–R10 at next revision |
| Moat | Lines 22 and 335: Services ≠ toll + Google; label Q4 vs FY |
| Management | Re-specify the Siri test as a scope test; reconcile with the news file; re-score the AI pillar |
| News | "[FACT] beta ~14 Sep" → [OUTLET], approximate |
| Financials | Appeal date: defer to the regulatory desk (3 Feb 2026) |
| Committee | Score on numeric grades only until one mapping is ratified (4.3); print the 6c sentence; assign a steel-man of the low-beta case |

## NOT OBTAINED / not verified by this audit
- Damodaran ERP for Nov 2026 (site DNS-blocked; search shows 4.14% ~1 Sep).
- 10y Treasury close 13 Nov 2026 (FRED DNS-blocked; search shows 4.86–4.88% on 6–9 Nov).
- AAPL daily bars (not on disk as data): the monthly-close streak (T4), volume averages (T3) and the higher-low sequence cannot be checked.
- FY26 10-K cover-page share count (4.5).
- Apple FY2005/FY2015 net income (V6) and the FY25 cover-page share count (1f): auditor's recollection, not fetched.
- Siri feature scope in shipped builds (4.1).

---
*Audit of argument, not conclusion. Every computation is shown inline. No audited report or config file was modified. Research and decision support only — not financial advice.*

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
