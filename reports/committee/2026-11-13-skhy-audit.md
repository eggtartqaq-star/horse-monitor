# SKHY — AI Audit of Committee Package (2026-11-13)

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence)
**Scope:** Consistency and provenance audit of files on disk only. No web searches performed (CEO instruction; rate limit). No Bash tool was available in this session — all arithmetic below is shown inline, step by step, so it can be re-run.
**Under audit:** CEO synthesis (`reports/committee/2026-11-12-skhy-ceo-synthesis.md`), CRO review (`reports/risk/2026-11-12-skhy-cro-review.md`), valuation (`reports/equity/2026-11-12-skhy-valuation.md`), and their upstream desk reports dated 2026-11-11 (technical, news, financials, regulatory, industry/memory-cycle).
**Checkpoint:** C1–C2 complete. C3–C8, verdict, register pending.

## Verdict

_(pending — filled after C8)_

## Claims checked

| # | Claim | Result | One-line note |
|---|-------|--------|---------------|
| C1 | ADS premium 44–56% | **PARTIAL** | Each desk reproduces its own %; the 50–56% top of the range rests on FX 1,400–1,460 that no dated print supports; at the only dated 10 Nov rate (₩1,337.5) the premium is 43%. The "$98 ADS-equivalent buyback price" is FX-stale: ~$111 at Nov rates. |
| C2 | Peak-to-trough survival 13% / <0% | **PASS** | Arithmetic reproduces; peak/trough years defined consistently (annual peak year → annual trough year) in both cycles. Minor: 3Q18 OP unconfirmed. |
| C3 | Valuation $80 / $112 / $102 / 40% MoS | pending | |
| C4 | CRO 3% cap arithmetic | pending | |
| C5 | Retired "HBM 2–3x DDR5" claim | pending | |
| C6 | tradingkey blacklist compliance | pending | |
| C7 | Price timeline consistency | pending | |
| C8 | Inference presented as fact in CEO synthesis | pending | |

## C1 — ADS premium 44–56% — PARTIAL

### 1a. Does each desk reproduce its stated percentage? Yes.

Formula (all desks): premium = SKHY(USD) × USDKRW ÷ (000660 ÷ 10) − 1.

**Technicals (老詹 §7), 10 Nov close, SKHY $129.66, 000660 ₩1,212,000 → ₩121,200 per ADS-equivalent:**
- 129.66 × 1,350 = 175,041 ÷ 121,200 = 1.4442 → **44.4%** (file: 44.4%) ✓
- 129.66 × 1,380 = 178,931 ÷ 121,200 = 1.4763 → **47.6%** ✓
- 129.66 × 1,400 = 181,524 ÷ 121,200 = 1.4977 → **49.8%** ✓
- 129.66 × 1,430 = 185,414 ÷ 121,200 = 1.5298 → **53.0%** ✓
- 129.66 × 1,460 = 189,304 ÷ 121,200 = 1.5619 → **56.2%** ✓
- Late-Aug column: 161.61 × 1,350 = 218,174 ÷ 175,900 = 1.2403 → 24.0% ✓; 161.61 × 1,460 = 235,951 ÷ 175,900 = 1.3414 → 34.1% ✓

**News (修大哥 §3), 6 Nov close, SKHY $127.34, 000660 ₩1,132,000 → ₩113,200:**
- 113,200 ÷ 1,340 = $84.48; 113,200 ÷ 1,353 = $83.67 (file: $83.7–84.5) ✓
- 127.34 ÷ 84.48 = 1.5073 → **50.7%**; 127.34 ÷ 83.67 = 1.5219 → **52.2%** (file: 50.7–52.2%) ✓

**Valuation (𢦀鳩仔 §8), 10 Nov, dated FX ₩1,337.5 (Money Today, 10 Nov Seoul close):**
- 121,200 ÷ 1,337.5 = $90.62 parity; 129.66 ÷ 90.62 = 1.4309 → **43.1%** (file: 43%) ✓
- 11 Nov intraday: ₩1,299,000 → 129,900 ÷ 1,337.5 = $97.12; 143 ÷ 97.12 = 1.472 → **47%** (file: ~47%) ✓

**Financials (巴爺爺 §5), 28 Oct 000660 ₩1,487,000 → ₩148,700, FX ₩1,523.5 (a 29 Jul press-conversion rate):**
- 148,700 ÷ 1,523.5 = **$97.60** → "≈US$98" ✓ (arithmetic)
- vs SKHY $142.62 (**26 Oct**, MarketChameleon — note the two-day date mismatch): 142.62 ÷ 97.60 = 1.461 → 46%; file says "40%+" ✓ (conservative)

**Regulatory (The dictator §4.4):** does not compute; cites Money Today / Maeil range 16–51% since listing, ~35% on 28 Jul, 15.8% day one; states "Current premium (Nov 2026): NOT OBTAINED". The CEO table's "16–51% since listing" is correctly attributed.

### 1b. Do the inputs agree across desks? Prices yes; FX no.

| Input | Technicals | News | Valuation | Financials | Dated print on disk |
|---|---|---|---|---|---|
| 000660 10 Nov | ₩1,212,000 (Yahoo art. 10 Nov) | "undated 1,212,000 … may be 9 Nov" | ₩1,212,000 (10 Nov) | — | one source; two desks date it 10 Nov, one is unsure |
| 000660 6 Nov | — | ₩1,132,000 (GuruFocus) | ₩1,132,000 | — | agree |
| SKHY 10 Nov | $129.66 | $129.66 (back-derived from 4 prints) | $129.66 | — | agree |
| **USDKRW** | **1,350–1,460 sensitivity, "NOT OBTAINED"** | 1,340–1,353 (FRED 30 Oct 1,333.99; TE 5 Nov 1,353) | **₩1,337.5 (10 Nov, dated)** | **₩1,523.5 (29 Jul press rate)** | 1,333.99 / 1,353 / 1,337.5 |

Finding: **the only dated November FX prints on disk are 1,333.99–1,353.** The technicals' rows at 1,400 / 1,430 / 1,460 (→ 49.8% / 53.0% / 56.2%) are sensitivity rows with no dated support, and even the 1,350–1,380 band sits above the dated prints. The firm-wide headline "44–56%" (CEO line 13, CRO §0 and §3.1) therefore carries a top half that is an FX assumption, not a measurement. **Measured at dated FX the premium is: 6 Nov 50.7–52.2%; 10 Nov 43.1%; 11 Nov intraday ~47%.** The honest headline is "**~43–52% across 6–11 Nov at dated FX**". The valuation desk already recomputed this (43%) on 12 Nov — the same day the CRO wrote "USD/KRW on 10–11 Nov NOT OBTAINED" — and the correction was not propagated to the CRO or CEO files.

### 1c. The "$98 per ADS-equivalent" recomputed at November rates — the number does not survive, the conclusion does.

- At ₩1,337.5 (10 Nov): 148,700 ÷ 1,337.5 = **$111.18**
- At ₩1,353 (5 Nov): 148,700 ÷ 1,353 = **$109.90**
- At ₩1,333.99 (30 Oct FRED, closest dated print to 28 Oct): 148,700 ÷ 1,333.99 = **$111.47**

So the 28 Oct ordinary price was ≈ **$110–111** per ADS-equivalent at contemporaneous FX, not $98. The $98 is ~12% too low purely because of the stale rate (1,523.5 ÷ 1,337.5 = 1.139).

Premium at 28 Oct, recomputed with matched dates where possible:
- vs financials' own $142.62 (26 Oct, mismatched): 142.62 ÷ 111.18 = 1.283 → **28%**
- vs technicals' derived 29 Oct close ≈ $162.0: 162.0 ÷ 111.18 = 1.457 → **46%**
- vs industry's "~$164.70 (28 Oct)" (chartrow, tier C): 164.70 ÷ 111.18 = 1.481 → **48%**

The financials desk's "40%+" was therefore right only by the coincidence of two offsetting errors (stale FX overstates by ~14%; mismatched date understates by ~14%). The conclusion — a large, non-arbitraged ADS premium existed at end-October — **survives** on matched-date inputs (46–48%). The figure "$98" **does not** and must not be used.

**Downstream effect:**
- CEO synthesis line 29 ("repurchasing its own ordinary shares at roughly $98 per ADS-equivalent. The Owner paid $129 for the same economic claim") → correct statement is **~$111 at the 28 Oct price; ~$91 at the 10 Nov price (121,200 ÷ 1,337.5); ~$97 at the 11 Nov price**. The buyback executes at whatever the ordinary trades at over 29 Oct–28 Jan, so no single figure is right; the sentence should be rewritten around current parity ($91–97).
- CRO §3.4 anchor row "巴爺爺 $98 (28 Oct) → −24.0%": 111.18 ÷ 129 − 1 = **−13.8%** at Nov FX. This row is an anchor, not the cap input; the cap (§9) is unaffected.
- Financials §4 "net ≈ US$26.2bn … ≈ ₩39.9tn at ₩1,523.5": 26.2 × 1,523.5 = 39,916 ✓ arithmetic, but the IPO settled in mid-July; if the actual July rate differed, the won figure moves. Flagged to the NOT OBTAINED register: **the ₩1,523.5 rate itself is suspicious** — it implies a 12.2% won appreciation between late July and 10 Nov (1,523.5 ÷ 1,337.5 = 1.139), a macro event no desk mentions. The technicals desk's late-Aug back-test reproduces the sourced "~30%" premium at FX 1,400–1,430, not at 1,523.5, which is further evidence the July rate is wrong or mis-extracted.

### 1d. Sign error in the valuation's FX commentary (low severity, does not feed a number)
Valuation §8.1: "[₩1,337.5] is 12% stronger than July's, which is itself part of why the premium has widened in USD terms." The direction is reversed. Premium = SKHY × USDKRW ÷ KRW-parity; a *stronger* won (lower USDKRW) *raises* USD parity and *lowers* the measured premium. Won strength since July has **compressed** the measured premium, so the widening from ~30% (23 Jul) to 43–52% (Nov) is despite FX, not because of it. The same section's "each ₩50 of won weakness lowers parity by 3.6%" (1,337.5 ÷ 1,387.5 = 0.964) is correct, so this is a slip in prose, not in the model.

### C1 result: PARTIAL
- Each desk's arithmetic reproduces its own stated percentage. ✓
- Cross-desk FX inputs do not agree; the 50–56% top of the headline range is unsupported by any dated print; dated-FX measurements are 43–52% across 6–11 Nov.
- "$98" fails recomputation (→ ~$111 at 28 Oct, ~$91–97 at 10–11 Nov). The premium conclusion survives at 43–48% on matched inputs.
- Severity: **Medium** for the headline range (feeds CRO cap midpoint — see C4, conclusion survives); **Medium** for "$98" (Owner-facing sentence in the CEO synthesis is wrong).

## C2 — Peak-to-trough survival ratios 13% and <0% — PASS

Source: financials §8 cycle table against §1 annual anchors (same file).

**Cycle 1, 2018 → 2019 (annual OP):** peak ₩20.84tn (2018), trough ₩2.7tn (2019).
- 2.7 ÷ 20.84 = 0.1296 → **13% survived** ✓
- (2.7 − 20.84) ÷ 20.84 = −18.14 ÷ 20.84 = −0.870 → **−87%** ✓ (matches the cdrinfo "declined 87 percent" citation in §1)
- Quarterly extreme: 4Q18 ₩4.4tn → 4Q19 ₩0.236tn: 0.236 ÷ 4.4 = 0.0536 → **5%** ✓; 4Q18 → 4Q19 = **4 quarters** ✓

**Cycle 2, 2021 → 2023 (annual OP):** peak ₩12.41tn (2021), trough −₩7.73tn (2023).
- −7.73 ÷ 12.41 = −0.623 → **less than zero** ✓
- (−7.73 − 12.41) ÷ 12.41 = −20.14 ÷ 12.41 = −1.623 → **−162%** ✓
- Quarterly extreme: 4Q21 ₩4.22tn → 1Q23 −₩3.40tn: 4Q21→1Q22→2Q22→3Q22→4Q22→1Q23 = **5 quarters** ✓

**Peak/trough definition consistency.** Both cycles use the same rule: annual peak-year OP → annual trough-year OP, with the quarterly extreme shown alongside. 2021 (₩12.41tn) is correctly identified as the peak year of cycle 2 — 2022 (₩7.01tn / ₩6.81tn, sources differ) is an intermediate decline year, not a peak. The report's third row ("2022 → 2023 as the coordinator framed it") is shown as an alternative and also yields <0%, so the headline is robust to the framing. The CEO synthesis (line 65) and CRO §5 quote "13% and <0%" and "4–5 quarters" correctly.

**Residual issues (do not change the result):**
1. §1 NOT OBTAINED #14: 3Q18 OP "₩6.47tn widely cited, not confirmed." If 3Q18 was the quarterly peak, then the quarterly survival is 0.236 ÷ 6.47 = **3.6%** (not 5%) and peak-quarter-to-trough is **5 quarters** (3Q18→4Q19), still inside "4–5 quarters". The annual 13% is unaffected.
2. FY2020 OP is NOT OBTAINED (valuation §1 also flags). 2019 is treated as the trough year of cycle 1; this holds only if 2020 OP > 2019 OP. Not verifiable from disk; flagged, not failed.
3. The cycle table's "quarterly extreme" column for cycle 1 uses 4Q18 ₩4.4tn, which does not appear in the §1 quarterly table (which starts at 4Q21). The figure is sourced in the §1 annual row (storagenewsletter 4Q18) only by implication. Low.

### C2 result: PASS
Arithmetic reproduces to the stated precision; peak and trough are defined by the same rule in both cycles; the alternative framing gives the same sign. Severity of residuals: **Low**.

## C3 — Valuation
_(pending)_

## C4 — CRO 3% cap
_(pending)_

## C5 — Retired claim
_(pending)_

## C6 — Blacklist
_(pending)_

## C7 — Date / price consistency
_(pending)_

## C8 — Inference as fact
_(pending)_

## Flags with severity
_(pending)_

## Bias observations
_(pending)_

## Required fixes
_(pending)_

## NOT OBTAINED register
_(pending)_
