# SKHY — AI Audit of Committee Package (2026-11-13)

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence)
**Scope:** Consistency and provenance audit of files on disk only. No web searches performed (CEO instruction; rate limit). No Bash tool was available in this session — all arithmetic below is shown inline, step by step, so it can be re-run.
**Under audit:** CEO synthesis (`reports/committee/2026-11-12-skhy-ceo-synthesis.md`), CRO review (`reports/risk/2026-11-12-skhy-cro-review.md`), valuation (`reports/equity/2026-11-12-skhy-valuation.md`), sizing (`reports/portfolio/2026-11-13-skhy-sizing.md`), and their upstream desk reports dated 2026-11-11 (technical, news, financials, regulatory, industry/memory-cycle).
**Not audited:** `reports/execution/2026-11-13-skhy-tickets.md` and `memory/decisions/2026-11-13-skhy-retrospective.md` (both exist on disk; outside this brief). The tickets may inherit the C9 rounding and "7 cents" slips — 死潘狗 should check.
**Checkpoint:** C1–C9 complete. Audit COMPLETE.

## Verdict

**PASS WITH FLAGS for the decision package. The three operative conclusions survive the audit; several Owner-facing sentences do not.**

| Conclusion | Survives? | Why |
|---|---|---|
| **Hold with conditions at ≤3% of LNW** | **YES** | The cap arithmetic reproduces (1% ÷ 33.3% = 3.0%). Re-run at dated-FX premiums (43.1–52.2%) the cap is **2.9–3.3%** — 3.0% sits inside the band. Risk score is 29.75 computed / 32 published, both below the ~40 initiation-veto line. Stop arithmetic reproduces. **Caveat:** the hold approval is conditional on a denominator nobody has. If the ~US$690 Webull account is all of the Owner's liquid net worth (reading (a)), the hold converts to reduce-to-zero, and that stays true when the denominator is corrected (C9). |
| **Add vetoed** | **YES** | MoS is negative on every central construction at every measured premium. At ×1.40 it is −26%; re-run at ×1.47 it is −21%, and at ×1.52 it is −18% (C3). The add stays blocked even with **no** required margin of safety, so the 40% number is not doing the work. Committee approval is also missing (CRO row 13). |
| **Zac's 1.5% now** | **YES, as a recommendation** | The parity gap at 1.5% is 1.5 × 0.35 = 0.525% of LNW, inside budget on every premium measurement. The MoS-failure argument stands (C3). The counter-argument understates forgone upside (~$864, not ~$530, per 100 ADS). That narrows the trade-off on the gap case but does not reverse it (C9). |

**Per report:**
- **CEO synthesis — FAIL (returns to author).** Six or more sentences state as fact things a department marked as inference, illustration, supplier narrative or NOT OBTAINED (C8). One headline number is wrong ($98, C1). The "premium is roughly half its value" line overstates the at-risk share by ~1.5× (C8). The verdict it reached is not changed by any of this, but the document is Owner-facing and fails rule 5 as written. It is also superseded by the CRO, valuation and sizing files.
- **CRO review — PASS WITH FLAGS.** The cap holds. Flags: the E[loss at stop] rows use an undisclosed 7.5% input (C4). The ₩1.64m "Aug peak" was derived when the ₩1,759,000 print was already on disk (C7). The $98 anchor row (C1) and the "October selloff −20% vs −31%" label are also wrong (C7).
- **Valuation — PASS WITH FLAGS.** All load-bearing figures reproduce. Flags: "16% above MS target" is 7.8%. The 40% MoS has no firm rule behind it and no moat review. The FX-direction prose is backwards. The DCF script is not persisted (C1d, C3).
- **Sizing memo — PASS WITH FLAGS.** All cap, stop, table and worked-example arithmetic reproduces. Flags: "7 cents above cost" is 18 cents. The §3 L2 rounding is inconsistent with §5.4. The forgone-upside figure is understated. Reading (a)'s denominator excludes the SKHY position itself, and the conclusion survives correcting it (C9).
- **Industry memory-cycle — FAIL on one item.** It still carries the retired "HBM margins 2–3x DDR5" as a live baseline (C5). One-line fix.

## Claims checked

| # | Claim | Result | One-line note |
|---|-------|--------|---------------|
| C1 | ADS premium 44–56% | **PARTIAL** | Each desk reproduces its own %. The 50–56% top of the range rests on FX of 1,400–1,460, and no dated print supports that. At the only dated 10 Nov rate (₩1,337.5) the premium is 43%. The "$98 ADS-equivalent buyback price" uses a stale FX rate: it is ~$111 at Nov rates. |
| C2 | Peak-to-trough survival 13% / <0% | **PASS** | Arithmetic reproduces. Peak and trough years are defined the same way in both cycles (annual peak year → annual trough year). Minor: 3Q18 OP unconfirmed. |
| C3 | Valuation $80 / $112 / $102 / 40% MoS | **PASS WITH FLAGS** | $102 reproduces ($102.40). ×1.40 is at or below the bottom of the dated Nov measurements (43–52%), which is not material. The 40% MoS is reasoned in-file but is analyst judgement: **no numeric MoS rule exists anywhere in `knowledge/` or `config/`**. One prose arithmetic error ("16% above MS target" is 7.8%). |
| C4 | CRO 3% cap arithmetic | **PASS WITH FLAGS** | 1 − 1/1.50 = 33.3% ✓; 1% ÷ 33.3% = 3.0% ✓; 1% ÷ 35% = 2.857% ✓. Rounding to 3.0% is immaterial next to measurement error. But the CRO's own §9 shows 1.05% at risk at −35%, which breaches the 1% budget at his own cap. The E[loss at stop] rows are overstated by ~0.5pp (undisclosed 7.5% input). Risk score 29.75 → 32 is a discretionary uplift, and it is disclosed. |
| C5 | Retired "HBM 2–3x DDR5" claim | **PARTIAL** | The financials citation is carried faithfully into the CEO file (source not re-fetched). **But the Nov memory-cycle report still carries "HBM margins 2–3x DDR5" (line 16) as a live baseline with no retraction.** The retirement also treats two different metrics as the same (margin multiple vs per-wafer profitability). |
| C6 | tradingkey blacklist compliance | **PASS** | 10 mentions across 7 SKHY reports, every one an exclusion note. Zero citations and zero tradingkey URLs. |
| C7 | Price timeline consistency | **PASS WITH FLAGS** | No desk quotes a conflicting print for any session. $131.07 = $137.71 × (1 − 4.82%) ✓. Flags: the CRO derived a ₩1.64m "Aug peak" when ₩1,759,000 (24 Aug) was on disk. "October selloff −20% vs −31%" actually covers late Aug → 10 Nov. ₩1,132,000 is dated to both 5 and 6 Nov in the memory-cycle report. "Thu 6 Nov" should be Fri. |
| C8 | Inference presented as fact in CEO synthesis | **FAIL** | 9 instances. The material ones: "four departments independently arrived at the same number"; "$98"; "roughly half its value" (it is ~⅓); "volume-locked through 2029… ceilings, not floors" (supplier narrative / NOT OBTAINED); "50%+ of a trough-year revenue" (an illustrative ₩60tn trough presented as fact). All harden in the same (cautious) direction. |
| C9 | Sizing memo arithmetic | **PASS WITH FLAGS** | 22 ADS ✓; $10.72 = 8.18% ✓; 2.86% ✓; §5.3 (a)/(b)/(c) ✓. Flags: "7 cents" is 18 cents; L2 rounding; forgone upside understated; reading (a)'s denominator omits the SKHY position itself (conclusion unchanged). |

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

**Regulatory (The dictator §4.4):** does not compute a premium. It cites Money Today / Maeil for a range of 16–51% since listing, ~35% on 28 Jul and 15.8% on day one, and states "Current premium (Nov 2026): NOT OBTAINED". The CEO table attributes "16–51% since listing" correctly.

### 1b. Do the inputs agree across desks? Prices yes; FX no.

| Input | Technicals | News | Valuation | Financials | Dated print on disk |
|---|---|---|---|---|---|
| 000660 10 Nov | ₩1,212,000 (Yahoo art. 10 Nov) | "undated 1,212,000 … may be 9 Nov" | ₩1,212,000 (10 Nov) | — | one source; two desks date it 10 Nov, one is unsure |
| 000660 6 Nov | — | ₩1,132,000 (GuruFocus) | ₩1,132,000 | — | agree (but see C7c) |
| SKHY 10 Nov | $129.66 | $129.66 (back-derived from 4 prints) | $129.66 | — | agree |
| **USDKRW** | **1,350–1,460 sensitivity, "NOT OBTAINED"** | 1,340–1,353 (FRED 30 Oct 1,333.99; TE 5 Nov 1,353) | **₩1,337.5 (10 Nov, dated)** | **₩1,523.5 (29 Jul press rate)** | 1,333.99 / 1,353 / 1,337.5 |

Finding: **the only dated November FX prints on disk are 1,333.99–1,353.** The technicals' rows at 1,400 / 1,430 / 1,460 (→ 49.8% / 53.0% / 56.2%) are sensitivity rows with no dated support. Even the 1,350–1,380 band sits above the dated prints. The firm-wide headline "44–56%" (CEO line 13, CRO §0 and §3.1) therefore has a top half that is an FX assumption, not a measurement.

**Measured at dated FX the premium is: 6 Nov 50.7–52.2%; 10 Nov 43.1%; 11 Nov intraday ~47%.** The honest headline is "**~43–52% across 6–11 Nov at dated FX**". The valuation desk had already recomputed this (43%) on 12 Nov. On the same day the CRO wrote "USD/KRW on 10–11 Nov NOT OBTAINED". The correction never reached the CRO or CEO files.

### 1c. The "$98 per ADS-equivalent" recomputed at November rates — the number does not survive, the conclusion does.

- At ₩1,337.5 (10 Nov): 148,700 ÷ 1,337.5 = **$111.18**
- At ₩1,353 (5 Nov): 148,700 ÷ 1,353 = **$109.90**
- At ₩1,333.99 (30 Oct FRED, closest dated print to 28 Oct): 148,700 ÷ 1,333.99 = **$111.47**

So the 28 Oct ordinary price was ≈ **$110–111** per ADS-equivalent at contemporaneous FX, not $98. The $98 is ~12% too low purely because of the stale rate (1,523.5 ÷ 1,337.5 = 1.139).

Premium at 28 Oct, recomputed with matched dates where possible:
- vs financials' own $142.62 (26 Oct, mismatched): 142.62 ÷ 111.18 = 1.283 → **28%**
- vs technicals' derived 29 Oct close ≈ $162.0: 162.0 ÷ 111.18 = 1.457 → **46%**
- vs industry's "~$164.70 (28 Oct)" (chartrow, tier C): 164.70 ÷ 111.18 = 1.481 → **48%**

The financials desk's "40%+" was right only because two errors happened to offset: the stale FX overstates the premium by ~14% and the mismatched date understates it by ~14%. The conclusion survives on matched-date inputs (46–48%): a large, non-arbitraged ADS premium existed at end-October. The figure "$98" **does not survive** and must not be used.

**Downstream effect:**
- **CEO synthesis line 29.** It says the company is "repurchasing its own ordinary shares at roughly $98 per ADS-equivalent. The Owner paid $129 for the same economic claim". The correct figures are **~$111 at the 28 Oct price, ~$91 at the 10 Nov price (121,200 ÷ 1,337.5) and ~$97 at the 11 Nov price**. The buyback executes at whatever the ordinary trades at over 29 Oct–28 Jan, so no single figure is right. The sentence should be rewritten around current parity ($91–97).
- **CRO §3.4 anchor row** "巴爺爺 $98 (28 Oct) → −24.0%": at Nov FX it is 111.18 ÷ 129 − 1 = **−13.8%**. This row is an anchor, not the cap input, so the cap (§9) is unaffected.
- **Financials §4** "net ≈ US$26.2bn … ≈ ₩39.9tn at ₩1,523.5": 26.2 × 1,523.5 = 39,916 ✓ arithmetic. The IPO settled in mid-July, though, so if the actual July rate differed the won figure moves.
- **The ₩1,523.5 rate itself is suspicious** (added to the NOT OBTAINED register). It implies 12.2% won appreciation between late July and 10 Nov (1,523.5 ÷ 1,337.5 = 1.139), a macro event no desk mentions. The technicals desk's late-Aug back-test reproduces the sourced "~30%" premium at FX 1,400–1,430, not at 1,523.5. That is further evidence the July rate is wrong or mis-extracted.

### 1d. Sign error in the valuation's FX commentary (low severity, does not feed a number)
Valuation §8.1 says: "[₩1,337.5] is 12% stronger than July's, which is itself part of why the premium has widened in USD terms." The direction is reversed. Premium = SKHY × USDKRW ÷ KRW-parity, so a *stronger* won (lower USDKRW) *raises* USD parity and *lowers* the measured premium. Won strength since July has therefore **compressed** the measured premium. The widening from ~30% (23 Jul) to 43–52% (Nov) happened despite FX, not because of it. The same section's "each ₩50 of won weakness lowers parity by 3.6%" is correct (1,337.5 ÷ 1,387.5 = 0.964), so this is a slip in the prose, not in the model.

### C1 result: PARTIAL
- Each desk's arithmetic reproduces its own stated percentage. ✓
- Cross-desk FX inputs do not agree. No dated print supports the 50–56% top of the headline range; dated-FX measurements are 43–52% across 6–11 Nov.
- "$98" fails recomputation (→ ~$111 at 28 Oct, ~$91–97 at 10–11 Nov). The premium conclusion survives at 43–48% on matched inputs.
- Severity: **Medium** for the headline range, because it feeds the CRO cap midpoint (see C4; the conclusion survives). **Medium** for "$98", because the Owner-facing sentence in the CEO synthesis is wrong.

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

**Peak/trough definition consistency.** Both cycles use the same rule: annual peak-year OP → annual trough-year OP, with the quarterly extreme shown alongside. 2021 (₩12.41tn) is correctly identified as the peak year of cycle 2. 2022 (₩7.01tn / ₩6.81tn, sources differ) is an intermediate decline year, not a peak. The report's third row ("2022 → 2023 as the coordinator framed it") is shown as an alternative and also gives <0%, so the headline holds under either framing. The CEO synthesis (line 65) and CRO §5 quote "13% and <0%" and "4–5 quarters" correctly.

**Residual issues (do not change the result):**
1. §1 NOT OBTAINED #14: 3Q18 OP is "₩6.47tn widely cited, not confirmed." If 3Q18 was the quarterly peak, the quarterly survival is 0.236 ÷ 6.47 = **3.6%** (not 5%). Peak-quarter-to-trough would then be **5 quarters** (3Q18→4Q19), still inside "4–5 quarters". The annual 13% is unaffected.
2. FY2020 OP is NOT OBTAINED (valuation §1 also flags it). 2019 is treated as the trough year of cycle 1, which holds only if 2020 OP > 2019 OP. This cannot be verified from disk, so it is flagged, not failed.
3. The cycle table's "quarterly extreme" column for cycle 1 uses 4Q18 ₩4.4tn. That figure does not appear in the §1 quarterly table, which starts at 4Q21; the §1 annual row (storagenewsletter 4Q18) sources it only by implication. Low.

### C2 result: PASS
Arithmetic reproduces to the stated precision. Peak and trough are defined by the same rule in both cycles, and the alternative framing gives the same sign. Severity of residuals: **Low**.

## C3 — Valuation $80 / $112 / $102 / 40% MoS — PASS WITH FLAGS

Source: `reports/equity/2026-11-12-skhy-valuation.md` §0, §3, §6, §8.

### 3a. Ordinary central ₩1,070,000 — reproduces from the stated scenarios
- 0.40 × 964,000 + 0.25 × 719,000 + 0.35 × 1,440,000 = 385,600 + 179,750 + 504,000 = **₩1,069,350** → "~₩1,069,000 / ₩1,070,000" ✓
- I cannot re-run the scenario DCFs themselves. The cited script lives in a session scratchpad (`…/scratchpad/skhy_val.py`), not in the repo, so the per-scenario values (964k / 719k / 1,440k) are **taken on trust**. Flag (Low): the audit trail the analyst names is not persisted on disk.

### 3b. Parity and premium lines — reproduce
- Central parity: 1,070,000 ÷ 10 = 107,000 ÷ 1,337.5 = **$80.00** ✓ (1,337.5 × 80 = 107,000 exactly)
- Low: 90,000 ÷ 1,337.5 = $67.29 ✓ · High: 125,000 ÷ 1,337.5 = $93.46 ✓
- Scenarios: 71,900 ÷ 1,337.5 = $53.76; 96,400 ÷ 1,337.5 = $72.07; 144,000 ÷ 1,337.5 = $107.66 ✓
- Premium-persists central: 80.00 × 1.40 = **$112.00** ✓; low 67.29 × 1.15 = $77.38 ✓; high 93.46 × 1.55 = $144.86 ✓
- Scenarios × 1.40: 53.76 × 1.4 = $75.3; 72.07 × 1.4 = $100.9; 107.66 × 1.4 = $150.7 ✓

### 3c. Does 0.30 × $80 + 0.70 × $112 = $102? Yes.
- 0.30 × 80 = 24.00; 0.70 × 112 = 78.40; sum = **$102.40** ✓ (file §8.4 shows 102.4)
- Low: 67.29 × (0.30 + 0.70 × 1.15) = 67.29 × 1.105 = **$74.36** → "$74" ✓
- High: 93.46 × (0.30 + 0.70 × 1.55) = 93.46 × 1.385 = **$129.44** → "$129" ✓
- Structural note: the weight (30% lift) and the multiplier are both labelled "mine, no source" (§8.2). They are correctly marked as judgement under rule 5.

### 3d. Is ×1.40 consistent with the measured premium?
Measured at dated FX (C1): 6 Nov 50.7–52.2%; 10 Nov 43.1%; 11 Nov intraday ~47%. Earlier: ~41% late Sep, ~30% 23 Jul (valuation §8).
- ×1.40 sits **at or just below the bottom** of the November measurements, not at their centre. The file justifies it as "≈ the Sep–Nov level". That is true if September (41%) is included, but it is not the November level.
- Is the gap explained? **Partly.** §8.2 explains the 1.15 floor: the premium can compress without a rule change, and it has already fallen to 16% once. The multiplier is also explicitly a forecast of a scarcity rent, not a measurement. A forward-looking multiplier below spot is defensible. The file just doesn't say it is assuming mean reversion, which it is. Low.
- Materiality, recomputed at the November midpoint (×1.47): 80 × 1.47 = 117.6; PW = 24.0 + 0.70 × 117.6 = 24.0 + 82.3 = **$106.3**; MoS at $129 = (106.3 − 129) ÷ 106.3 = **−21%** (vs −26%). At ×1.52 (6 Nov high): 80 × 1.52 = 121.6; PW = 24.0 + 85.1 = **$109.1**; MoS = **−18%**. **Every construction remains negative. The conclusion "fails the MoS test" does not depend on where in the measured band the multiplier is set.**
- The "persists" band of 1.15–1.55 is described as the "observed premium band since listing excluding the listing-week spike (16–56%)". Its 56% top is the technicals' FX-1,460 sensitivity row, which C1 found has no dated support; the dated top is ~52%. This does not affect the result: high PW at ×1.52 instead of ×1.55 is 93.46 × (0.30 + 1.064) = $127.5 vs $129.4.

### 3e. MoS arithmetic — reproduces
MoS = (FV − 129) ÷ FV:
- Parity central: (80 − 129) ÷ 80 = −0.6125 → **−61%** ✓
- Parity high: (93.5 − 129) ÷ 93.5 = −0.380 → **−38%** ✓
- Premium-inclusive central: (112 − 129) ÷ 112 = −0.152 → **−15%** ✓
- PW central: (102.4 − 129) ÷ 102.4 = −0.260 → **−26%** ✓
- PW high: (129.4 − 129) ÷ 129.4 = +0.003 → **0%** ✓
- Scenario (c) × 1.40: (150.7 − 129) ÷ 150.7 = +0.144 → **+14%** ✓
- Entry at 40% MoS: 80 × 0.6 = **$48**; 102.4 × 0.6 = **$61.4**; 112 × 0.6 = **$67.2** ✓

### 3f. Is the 40% required MoS justified or asserted? Reasoned in-file; no firm rule exists.
**Search of the firm's rulebook (Grep for "margin of safety|MoS|margin_of_safety" across `knowledge/`, `config/`, `.claude/`):**
- `config/risk-limits.yaml` has no MoS field. I read it in full: it contains only the portfolio, concentration, per_trade, options and process blocks.
- `knowledge/investment-philosophy.md` lines 14–15 say "bought with a margin of safety (菲比斯 and 𢦀鳩仔's departments)". **No number.**
- `.claude/agents/valuation-analyst.md` lines 27–28 say "Demand a wider margin when 菲比斯 rates the moat narrow or eroding." **No number.**
- The precedents the valuation cites are real: `reports/equity/2026-08-14-6160hk-moat.md:621` ("I require a 30% margin of safety") and `reports/equity/2026-08-21-msft-moat.md:967` ("I require a 20% margin of safety"). There is also `reports/equity/2026-07-19-klac-valuation.md:37` (菲比斯 25–30%).

**Finding: the firm has no numeric margin-of-safety rule on disk.** Every required MoS to date (20 / 25–30 / 30 / 40%) has been set per name by the moat analyst or the valuation analyst.

The 40% here is **reasoned, not asserted**. §8.4 gives three compounding reasons:
1. The late-cycle central estimate is unreliable, with a 2x scenario spread.
2. The premium-collapse leg is an independent second downside.
3. HBM pricing power is eroding.

But the trigger the agent prompt names ("when 菲比斯 rates the moat narrow or eroding") **has not fired: no 菲比斯 moat report on SKHY exists** (Glob `reports/**/*skhy*` returns no moat file). The valuation substitutes "巴爺爺's moat-equivalent reading". Severity **Low–Medium**. It does not change the result, because the position fails even at 0% required MoS (−26% on the PW central). But the committee should know the 40% is one analyst's number, with no firm-level anchor and no moat review behind it.

### 3g. Arithmetic error in prose (§0 line 21) — Low
"at parity it is ₩1.73m — … 16% above the Morgan Stanley target (₩1.6m, cut 11 Nov)":
- 129 × 1,337.5 × 10 = **₩1,725,375** ✓ (₩1.73m)
- 1,725,375 ÷ 1,600,000 = 1.0784 → **7.8% above**, not 16%.
Also checked, correct: 129 ÷ 1.40 = 92.14 × 13,375 = ₩1,232,400 (₩1.23m) ✓; 129 ÷ 107.66 = 1.198 ("(c) at 20% premium") ✓; 129 ÷ 80 = 1.6125 ("base at 60%") ✓; ordinary vs central 1,132 ÷ 1,070 = +5.8%, 1,299 ÷ 1,070 = +21.4% ("6–21%") ✓.

### 3h. Multiples (§5) — reproduce
1,212,000 × 700M = ₩848.4tn; − 98.7 = ₩749.7tn EV ✓; 750 ÷ 269 = 2.79x ✓; 848 ÷ (269 × 0.75 = 201.75) = 4.20x ✓; 750 ÷ 65 = 11.5x ✓; 848 ÷ 48.75 = 17.4x ✓.

### C3 result: PASS WITH FLAGS
Every load-bearing valuation figure reproduces. Flags:
- ×1.40 is below the November measured band and is not explained as a mean-reversion assumption (Low; immaterial, since MoS stays between −18% and −26%).
- The 40% MoS has no firm-level rule, and the moat review that would justify widening it was never run (Low–Medium).
- "16% above MS target" is 7.8% (Low).
- The DCF script is not persisted to the repo (Low).

## C4 — CRO 3% cap — PASS WITH FLAGS

Source: `reports/risk/2026-11-12-skhy-cro-review.md` §0, §1 row 9, §3.3, §4, §9, §10; `config/risk-limits.yaml`.

### 4a. Config input
`config/risk-limits.yaml` line 18: `max_risk_per_trade: 0.01  # 1% of portfolio at risk (size x distance to stop)` ✓ **1%.**
Note: the config defines risk as *size × distance to stop*. Counting the premium, which has no stop, against this line is the CRO's **extension** of the rule. He labels it as such and proposes it as a new `instrument:` block, "NOT applied — Owner approval required" (§3.3, §11). So the 3% cap is a judgement the CRO makes under his veto authority, built on the 1% budget; the config does not produce that number by itself. This is correctly disclosed.

### 4b. Premium → loss to parity
- 50% premium: loss = 1 − 1 ÷ 1.50 = 1 − 0.6667 = **0.3333 → 33.3%** ✓
- Cap: 0.01 ÷ 0.3333 = **3.00%** ✓
- 44%: 1 − 1 ÷ 1.44 = 0.3056 → 0.01 ÷ 0.3056 = **3.27%** ("3.3%") ✓
- 56%: 1 − 1 ÷ 1.56 = 0.3590 → 0.01 ÷ 0.3590 = **2.79%** ("2.8%") ✓
- **At dated-FX premiums (C1):** 43.1% → loss 30.1% → cap **3.32%**; 47% → 32.0% → **3.13%**; 52.2% → 34.3% → **2.92%**. Dated-FX band for the cap: **2.9–3.3%**.

### 4c. Zac's −35% / 2.86%
- 0.01 ÷ 0.35 = **0.02857 → 2.857%** ✓
- A −35% drop to parity corresponds to a premium of 1 ÷ 0.65 − 1 = **53.8%**, above every dated-FX measurement (max 52.2%). So −35% is a conservative stress, not the measured case.
- **Is 3.0% vs 2.86% material?** At 3.0% × 35% = **1.05%** at risk, which is 0.05pp (5%) over the 1% budget, or **$50** per $100,000 of LNW. That is well inside the measurement band in 4b (2.9–3.3%), so it is **not material to the decision.**
- It is, however, an internal inconsistency. The CRO's own §9 line "−35% premium = 1.05%" shows the cap breaching the budget it was derived from. A one-line acknowledgement would close it: "3.0% is a rounded cap; at the −35% stress it is 1.05% at risk". Low.

### 4d. Other CRO arithmetic checked
- §3.4: 129.66 ÷ 1.40 = 92.61 → (92.61 − 129) ÷ 129 = −28.2% ✓; ÷ 1.44 = 90.04 → −30.2% ✓; ÷ 1.50 = 86.44 → −33.0% ✓; ÷ 1.56 = 83.12 → −35.6% ✓; $84 → −34.9% ✓; $98 → −24.0% ✓ (but $98 itself fails, C1c → −13.8%).
- §4: 120.35 ÷ 129 = 0.93295 → −6.71% ✓; 120.35 ÷ 129.66 = 0.9282 → −7.18% ✓; 122.20 ÷ 129 = 0.9473 → −5.27% ✓; 1 ÷ 0.067 = 14.9% ✓; 1 ÷ 0.134 = 7.46% → 7.5% ✓.
- **§4 E[loss | stop hit] does NOT reproduce from the table's own inputs.** With near-level = 6.7%, −10%, −13.4%:
  - 0.60 × 6.7 + 0.30 × 10 + 0.10 × 13.4 = 4.02 + 3.00 + 1.34 = **8.36%** (file: 8.9%)
  - 0.50 × 6.7 + 0.35 × 10 + 0.15 × 13.4 = 3.35 + 3.50 + 2.01 = **8.86%** (file: 9.3%)
  - 0.40 × 6.7 + 0.40 × 10 + 0.20 × 13.4 = 2.68 + 4.00 + 2.68 = **9.36%** (file: 9.7%)
  - The file's figures reproduce only if "fills near level" = **7.5%**: 4.50 + 3.00 + 1.34 = 8.84 ✓; 3.75 + 3.50 + 2.01 = 9.26 ✓; 3.00 + 4.00 + 2.68 = 9.68 ✓.
  - That 7.5% input is **undisclosed** and contradicts the table directly above it (−6.7%).
  - Corrected range: **−8.4% to −9.4%**, not −8.9% to −9.7%. The headline "plan on ~−9% to −10%" should read "~−8.5% to −9.5%".
  - Severity Low: it is not the binding constraint, and "size for −13.4%" is unaffected.
- §5: 1,132,000 ÷ 0.69 = ₩1,640,580 ("~₩1.64m DERIVED") ✓ arithmetic. The input is wrong, though: see C7b.
- §9 translation: 3,000 ÷ 129.66 = 23.14 → **23 ADS** ✓; parity loss 3,000 × 0.33 = $990 / × 0.356 = $1,068 ✓; worst 3,000 × 0.68 = $2,040 ✓.
- §10 risk score: 0.30×10 + 0.15×40 + 0.20×30 + 0.10×45 + 0.10×35 + 0.15×45 = 3.0 + 6.0 + 6.0 + 4.5 + 3.5 + 6.75 = **29.75** ✓. It is published as **32**, a **+2.25 discretionary uplift** that is disclosed in-line with reasons. Flag (Low): the sizing memo quotes "32/100" without the computed 29.75. Either figure is below the ~40 initiation-veto line, so no conclusion changes.

### C4 result: PASS WITH FLAGS
- The cap arithmetic reproduces (3.0%; 2.86% at −35%).
- Rounding 2.86% to 3.0% is immaterial: ≤$50 per $100k, and inside the 2.9–3.3% dated-FX band. It does leave the CRO's own table showing 1.05% at risk at the cap (Low).
- E[loss at stop] is overstated by ~0.5pp because of an undisclosed 7.5% input (Low).
- The risk score is 29.75 computed and 32 published (Low; disclosed).

## C5 — Retired claim "HBM margins 2–3x DDR5" — PARTIAL

### 5a. Does the Nov memory-cycle report still carry it? **Yes — FAIL on this sub-check.**
`reports/industry/2026-11-11-skhy-memory-cycle.md` §0, lines 14–16:
> **Baseline from `reports/industry/2026-08-21-msft-industry.md` (21 Aug 2026), not re-derived:** … - HBM margins **2–3x DDR5**.

I grepped the same file for "baseline|retire|stale|Introl|HBM (price|pricing|margin)" and found **no retraction, correction or caveat** anywhere else in the report. The later sections move in the same direction as the retirement: line 138 says "the mechanism by which HBM pricing power erodes", and line 313 says "HBM pricing power is eroding before volume". Neither **withdraws the 2–3x figure**.

So the claim the CEO declares "retired" (synthesis lines 69–71, 136–139) is still on disk, in bold, in the industry desk's current report, presented as a live baseline. Anyone reading the industry report alone would take it as current.

Secondary point: the CEO's "Where the departments disagree" #1 frames this as "**Elon Musk vs 巴爺爺** on HBM economics". On disk, Elon Musk did not argue for 2–3x in November; he carried it forward "not re-derived". It is a stale carry-forward, not a disagreement, and calling it dissent overstates the evidence that a debate took place (Low).

### 5b. Does the financials file's citation say what is claimed? **The CEO file carries it faithfully; the source was not re-verified.**
`reports/equity/2026-11-11-skhy-financials.md` line 18 and §2 line 90:
> TrendForce estimates that **HBM revenue and profitability per wafer fell below 64GB DDR5 RDIMM in 1Q26** … ([TrendForce 22 Jul 2026, "sk-hynix-set-to-post-record-operating-margin-in-q2-as-hbm-mix-weighs-on-asp-growth-and-ltas-gain-focus"])

- CEO lines 68–69 say "TrendForce estimates HBM per-wafer profitability fell *below* DDR5 RDIMM in 1Q26". This is **faithful** to financials, including the "estimates" qualifier ✓.
- The URL slug supports the topic ("HBM mix weighs on ASP growth"). It does **not** by itself confirm the specific per-wafer comparison. Under this session's no-fetch instruction the source text is **NOT VERIFIED** (see register).
- Corroboration on disk is thin. There is one wccftech item (SK hynix prioritising DDR5 output), which is directional only. There is also one analyst construction (65% HBM vs 90% DDR5 margins), which the financials desk itself labels "**low-quality source, directional only**". So the retirement rests on **one TrendForce estimate for one quarter (1Q26)**, relayed by search extraction.

### 5c. Logic: does the evidence retire the claim?
- **Metric mismatch.** The August claim is a *margin multiple* ("HBM margins 2–3x DDR5"). The TrendForce point is *revenue and profitability per wafer*. HBM uses materially more wafer area per bit than DDR5, so per-wafer profitability can fall below DDR5 while HBM's margin *percentage* stays comparable or higher. The two statements do not directly contradict each other. The financials' own wording ("That was true in 2024–25 and is not true now") is stronger than a per-wafer estimate supports.
- **Time mismatch.** The evidence is a 1Q26 estimate published on 22 Jul. The CEO says "currently inverted" in November. Nothing on disk dates the comparison after 1Q26. Since then, commodity DRAM contract growth has decelerated (+13–18%, with +10–15% forecast; synthesis line 84), which would narrow the gap.
- **Verdict on the retirement:** it is correct to **stop reusing "2–3x"**, an August figure sourced from Introl and contradicted by a better-tier source. It is **overstated** to call the HBM thesis "inverted" as fact. Defensible wording would be: "TrendForce estimated HBM per-wafer profitability below DDR5 RDIMM in 1Q26; the August '2–3x margin' figure is withdrawn pending a current HBM-vs-DDR5 margin comparison."
- The valuation handles the downstream use appropriately (§2 line 68: "If one believes the HBM layer earns no premium … every value below falls ~15%").

### C5 result: PARTIAL
- Financials → CEO citation: PASS (source unverified this session).
- "The memory-cycle report no longer carries it": **FAIL**. Line 16 still carries it, with no retraction.
- Logic: the retirement is directionally justified, but "inverted" (CEO line 67, financials §2) is stronger than one per-wafer estimate for 1Q26 supports.
- Severity: **Medium** for the stale claim, because a stale figure sitting in a current report is exactly the reuse risk the CEO is trying to prevent. **Low** for the metric and framing points.

## C6 — tradingkey blacklist — PASS

Grep `tradingkey` (case-insensitive) across all files matching `reports/**/*skhy*`:

| File | Line | Text (abridged) | Type |
|---|---|---|---|
| `reports/news/2026-11-11-skhy-news.md` | 12 | "surfaced in results … **Blacklisted firm-wide; not cited.**" | exclusion |
| `reports/news/2026-11-11-skhy-regulatory.md` | 337 | "**blacklisted — not cited** (it surfaced on the Dalian story and the ADR-quota story; the same facts are taken from Reuters-syndicated outlets and Money Today respectively)" | exclusion, with substitute sources named |
| `reports/technical/2026-11-11-skhy-technical.md` | 13 | "blacklisted firm-wide and is not cited" | exclusion |
| `reports/technical/2026-11-11-skhy-technical.md` | 432 | "blacklisted, not cited" | exclusion |
| `reports/equity/2026-11-11-skhy-financials.md` | 8 | "tradingkey.com blacklisted and not cited" | exclusion |
| `reports/equity/2026-11-12-skhy-valuation.md` | 236 | "tradingkey.com blacklisted and not cited" | exclusion |
| `reports/risk/2026-11-12-skhy-cro-review.md` | 283 | "`tradingkey.com` not cited" | exclusion |
| `reports/industry/2026-11-11-skhy-memory-cycle.md` | 25, 172, 367 | "blacklisted and not cited; it surfaced for this name and was discarded" / "Nothing from `tradingkey.com`" / "deliberately not used" | exclusion |

The CEO synthesis and sizing memo have **zero mentions**. No `tradingkey` string appears inside any URL or link in any SKHY file; the grep would have matched it.

Residual observation (not a finding): the regulatory desk notes that tradingkey surfaced on the **ADR-quota story** and that it took "the same facts" from Money Today. The quota mechanism is the load-bearing fact behind the CRO's binding cap. It is independently sourced on disk (CRO §13: Bloomberg Línea, GuruFocus, Invezz 23 Jul, Tiger/Webull syndications), so the blacklist did not leave it single-sourced.

### C6 result: PASS
Ten occurrences across seven reports; every one is an exclusion note; zero citations.

## C7 — Price timeline consistency — PASS WITH FLAGS

### 7a. The ADS sequence — consistent across every desk that quotes it
| Session | Print | Source on disk | Desks quoting it | Conflict? |
|---|---|---|---|---|
| Thu 29 Oct | ~$162.0 (derived: 149.21 ÷ 0.921 = 162.01 ✓) | news §1.1, technicals | news, technicals, CEO (implicitly) | none |
| Fri 30 Oct | $149.21 (−7.9%) | debelegger | technicals, news, memory-cycle | none |
| Wed 4 Nov | $143.07 (−5.12%) | chartrow (memory-cycle line 252) | memory-cycle uses it; CRO §13 "unverified and not used" | not a conflict: one desk uses it, one declines it. 143.07 × (1 − 0.134) = **$123.90** → consistent with 5 Nov "~$124" and with 6 Nov $127.34 (+2.8%) |
| Fri 6 Nov | $127.34 | Google Finance / StockTitan (brief) | technicals, news, valuation, CEO, CRO | none. Week change 127.34 ÷ 149.21 − 1 = **−14.7%** ✓ (news) |
| Mon 9 Nov | $134.38 (+5.53%) | StockAnalysis snippet | news, CEO | none. 127.34 × 1.0553 = **134.38** ✓ |
| Tue 10 Nov | $129.66 (derived from 4 prints) | news, technicals | all desks | none. 129.66 ÷ 134.38 − 1 = **−3.51%** ✓ |
| Wed 11 Nov | intraday $137.49–144.77 (Yahoo range); prints 142.49 / 142.68 / 143.42 / 144.71 | technicals, news | CEO "$138–145" ✓; valuation "$138–145" ✓; sizing "$142.68–$143.42" (see 7e) | none; **close NOT OBTAINED** by every desk |
| Thu 12 Nov | **$137.71 close** | Webull pull via coordinator (sizing §1.1) | sizing only | none: no earlier desk quotes a 12 Nov print |
| Fri 13 Nov | **$131.07** at 19:50 UTC (−4.82%); range $129.18–135.76 | same | sizing only | 137.71 × (1 − 0.0482) = 137.71 − 6.64 = **$131.07** ✓; 131.07 inside the range ✓ |

Weekdays: 1 Nov 2026 is a Sunday (2026-01-01 is a Thursday, and 304 days later = Thursday + 3 = Sunday). That makes 5 Nov Thu, 6 Nov Fri, 9 Nov Mon, 10 Nov Tue, 11 Nov Wed, 12 Nov Thu and 13 Nov Fri. The news desk's labels are all correct.

**Grep check:** `137.71` and `131.07` appear only in `reports/portfolio/2026-11-13-skhy-sizing.md` and `reports/execution/2026-11-13-skhy-tickets.md`. No earlier desk claims a 12 or 13 Nov print, so none could conflict with them. The 11 and 12 Nov desks could not have had $131.07. The sizing memo correctly marks $129.66 as "**superseded** by the live print; shown for reconciliation only". It also correctly re-runs John's "23 ADS per $100k at $129.66" as 22 at $131.07 (C9).

Owner P&L at the live print: 131.07 − 129.00 = $2.07; 2.07 ÷ 129 = **+1.60%** ✓.

### 7b. CRO derived an "Aug peak" of ₩1.64m that is already on disk as ₩1,759,000 — Low–Medium
CRO §5 (line 146) says: "The 24 Aug 2026 ordinary peak was not obtained; 老詹 has the ordinary −31% from 24 Aug at ₩1,132,000 (6 Nov), implying a peak of ~₩1,640,000 (DERIVED)." The register (§13 line 273) repeats NOT OBTAINED.

On disk, technicals line 77 / 220 has "**24 Aug | 000660.KS ₩1,759,000** (prev ₩1,730,000) — PROXY | Eulerpool". Technicals line 226 has "Proxy drawdown 24 Aug → 10 Nov: **−31.1%**", i.e. 1,212,000 ÷ 1,759,000 = 0.689 → −31.1% ✓. **The −31% runs to the 10 Nov price (₩1,212,000), not to the 6 Nov price (₩1,132,000).** The CRO applied it to the wrong endpoint and then reported the peak as NOT OBTAINED, even though the technicals desk had it (as a proxy).

Corrected CRO §5 row 1 (halving from ₩1,759,000 → ₩879,500 → ₩87,950 per ADS-equivalent):
- At FX 1,350: 87,950 ÷ 1,350 = $65.15 → (65.15 − 129) ÷ 129 = **−49.5%**; at 1,380: $63.73 → **−50.6%** (CRO: −53 to −54%)
- With the premium persisting at +50%: $97.7 / $95.6 → **−24.3% / −25.9%** (CRO: −29 to −31%)
- At dated ₩1,337.5: 87,950 ÷ 1,337.5 = $65.76 → **−49.0%**

**Effect:** the CRO's drawdown range "−30% to −54%" becomes "**~−25% to −51%**". Because the CRO's derivation erred on the conservative side, **no conclusion changes**: the cap is premium-derived, not cycle-derived. It is still a provenance failure. A number on disk was declared NOT OBTAINED and replaced with a wrong derivation.

### 7c. "October selloff (−20% vs −31%)" compares a late-Aug → 10 Nov window, not October — Low
CEO line 35, CRO §3.2 item 3 ("in October") and valuation line 205 all quote "ADS −20% vs ordinary −31%". The source (technicals lines 226–227, 273) is **24/27 Aug → 10 Nov**: ADS 161.61 → 129.66 = **−19.8%** ✓; ordinary 1,759,000 → 1,212,000 = **−31.1%** ✓. It is not the October selloff.

The actual 29 Oct → 6 Nov selloff is ADS 162.0 → 127.34 = **−21.4%** against ordinary **−25.8%** (memory-cycle line 254). That is the same direction but a 4-point gap, not 11. The conclusion ("the premium cushioned the ADS") survives in both windows; only the label and the size of the cushion are wrong.

### 7d. ₩1,132,000 is dated to two different sessions in the memory-cycle report — Low–Medium
- Memory-cycle line 253 (5 Nov row): "SK hynix **−9.5% to −10.4% to 1,132,000 won**".
- Memory-cycle line 254 (6 Nov row): "**Further slide**; ordinary closes **1,132,000 won** = −25.8% from 29 Oct".

A "further slide" cannot close at the same price. The news, valuation and CRO date ₩1,132,000 to **6 Nov** (GuruFocus via news). If it is actually the 5 Nov close and 6 Nov was lower, then the 6 Nov premium (news: 50.7–52.2%) was computed against a stale ordinary and is understated. The memory-cycle's "−25.8% from 29 Oct" would also move. This can't be resolved from disk (see register). It does not affect the 10 Nov measurement (43.1%) or the cap.

### 7e. Minor
- Technicals line 31: "$127.34 close on **Thu** 6 Nov 2026". 6 Nov 2026 is a **Friday** (line 40 of the same file has "6 Nov (Fri)"). Internal weekday slip. Low.
- Sizing §1.1 gives "11 Nov intraday **$142.68–$143.42**". Those are two prints presented as a range. The technicals-recorded day range is **$137.49–$144.77**. Low; not used in any computation.

### C7 result: PASS WITH FLAGS
No desk quotes a print for any session that conflicts with another desk, and the full chain from 6 Nov to 13 Nov reconciles arithmetically. Flags: CRO ₩1.64m mis-derivation (Low–Medium, conservative error); the "October" label on an Aug→Nov window (Low); ₩1,132,000 double-dated (Low–Medium, unresolved); weekday and range slips (Low).

## C8 — Inference presented as fact in the CEO synthesis — FAIL

Each row below is a sentence in `reports/committee/2026-11-12-skhy-ceo-synthesis.md` that states as fact something a department marked as inference, estimate, illustration, supplier narrative or NOT OBTAINED, or that misstates the department's figure.

| # | CEO line | CEO says | What the department actually said | Severity |
|---|---|---|---|---|
| 1 | 13–15 | "**Four departments independently arrived at the same number**: … 44–56% premium" | Regulatory: "Current premium (Nov 2026): **NOT OBTAINED**" — it gave a 16–51% since-listing range, not a current measurement. Financials: "40%+" on **28 Oct**, at a stale July FX rate (C1c). News: the 10 Nov ADS close is **back-derived**, not printed. Technicals: "FX **NOT OBTAINED**", sensitivity table. **Two** desks measured a November premium, both on assumed FX; the valuation desk later measured 43% at dated FX. "Independently … same number" is false. | **Medium** |
| 2 | 19 | Technicals: "FX sensitivity **1,350–1,380** … **44–56%**" | 1,350–1,380 yields **44.4–47.6%**. 56% requires FX 1,460 (C1a). The CEO table puts the top of the range inside a narrower FX band than the one that produces it, so the 56% looks measured. (CRO line 103 repeats "1,350–1,380".) | **Low–Medium** |
| 3 | 29–30 | "repurchasing … at roughly **$98 per ADS-equivalent**. The Owner paid $129 for the same economic claim" | The $98 uses the stale ₩1,523.5 rate. At Nov FX it is ~$111 at the 28 Oct price and **~$91–97** at the 10–11 Nov prices (C1c). | **Medium** |
| 4 | 35 | "the ADS fell less than the ordinary **in the October selloff (−20% vs −31%)**" | The technicals' window is 24/27 Aug → 10 Nov. October is −21% vs −26% (C7c). | Low |
| 5 | 67–69 | "**The HBM thesis is currently inverted.**" | Financials: TrendForce **estimates** per-wafer profitability below DDR5 RDIMM **in 1Q26**. That is a single estimate for one quarter and a different metric from margin (C5c). | **Low–Medium** |
| 6 | 72–74 | "D&A of ₩30–40tn/yr by 2029 — **50%+ of a trough-year revenue**. This is the mechanism by which 80% margins become losses." | Financials §3 line 113: "At a trough revenue of, **say, ₩60tn** (2024's level), that is 50–65%" — an **illustration** on an assumed trough revenue. The valuation's scenario (a) puts trough revenue at **₩120–150tn** (§3 line 76), giving 28 ÷ 150 = 19% to 40 ÷ 120 = 33%. The CEO dropped the "say" and stated the high illustration as fact, against the firm's own valuation. | **Medium** |
| 7 | 93–94 | "HBM is **volume-locked through 2029 across 14 LTAs**, but **priced annually with ceilings, not floors**" | Memory-cycle line 27: "**'Sold out through 2029' … are supplier narrative and are treated as such.**" Line 155: 14 LTAs cover ">50% of **2027 and 2028** capacity", which is not 2029 and not all volume. Line 166: "**no evidence** of take-or-pay or price floors". Line 374 lists the LTA terms as **NOT OBTAINED**. Financials and valuation both list floor prices as **NOT OBTAINED**, and the valuation gives "LTA floors hold" a **35%** scenario weight. The CEO converted a supplier narrative into fact and an absence of evidence into "not floors". | **Medium** |
| 8 | 102–104 | "one-year US tool licence that **expires 31 December 2026**" | Regulatory states 31 Dec as fact, sourced to a licence "covering **calendar-2026** shipments" (Tom's Hardware / Business Today, 30 Dec 2025). The CRO (§6, §13) marks it "**DERIVED** — no source states the date". The CEO follows the regulatory desk. The inference is strong, and the CEO's wording is defensible, but it should carry the CRO's qualifier. | Low |
| 9 | 153–154 | "an instrument carrying a regulatory premium of **roughly half its value** that can vanish without notice" | A 43–52% premium **over parity** is 1 − 1/1.43 = **30%** to 1 − 1/1.52 = **34%** of the ADS's value. The CRO: "**33% of price**". The valuation: "$30–50 scarcity rent" on $129 = 23–39%. "Half its value" overstates the share of the Owner's money at regulatory risk by ~1.5×. It is the closing verdict sentence the Owner reads. | **Medium** |
| 10 | 62–63 | "**₩98.7tn net cash**" (unqualified) | Financials line 132: "some portion of the ₩114.5tn is customer prepayments, not earned cash. The amount is **NOT OBTAINED**." The valuation (§1) carries the caveat; the CEO drops it. | Low |

**Checked and found faithful (no finding):**
- Line 47–48, lock-up 90 days / 8 Oct / company-affiliates-management / 100% primary / SK Square 20.07% "legally bound": all sourced in financials §2 line 135–138 (Tech Capital, Motley Fool, Briefs, Webull, Korea Times 2 Nov).
- Line 55, Elon Musk "half demand-side re-rating, half politics": memory-cycle line 258 ✓. Musk adds that he weights it "as a genuine cycle signal … not as noise", which the CEO abbreviates but does not contradict.
- Line 59–60, B+/72 and "roughly 60% … is price": financials line 20 ✓.
- Line 63, 9M OP = 3.8x 2025: 181.5 ÷ 47.21 = 3.84 ✓.
- Line 75, "~₩96tn non-operating swing": financials line 222 ✓.
- Line 86, "eight of twelve": consistent with valuation §3 and CRO §5.
- Line 109–111, withholding 22% / 15%: regulatory lines 204, 290, 303 ✓.

### C8 result: FAIL
Ten flagged sentences; five are Medium (rows 1, 3, 6, 7, 9). **Every one of them moves in the same direction.** Each makes the position look worse, the premium look larger or the business look more fragile than the department's own qualified statement. None changes the verdict, which the later CRO, valuation and sizing work independently supports. But the synthesis is an Owner-facing document that tells the Owner "Every figure above is a search extraction". As written, it breaches rule 5 ("Mark estimates as estimates") in at least six places. It returns to the author.

## C9 — Sizing memo arithmetic — PASS WITH FLAGS

Source: `reports/portfolio/2026-11-13-skhy-sizing.md`.

### 9a. Required checks
- **3% of $100,000 ÷ $131.07:** 3,000 ÷ 131.07 = **22.89 → 22 ADS** ✓. Check: 22 × 131.07 = $2,883.54 ≤ $3,000; 23 × 131.07 = $3,014.61 > $3,000. Rounding down is correct.
- **Stop distance from $131.07:** 131.07 − 120.35 = **$10.72** ✓; 10.72 ÷ 131.07 = 0.08179 → **8.18%** ✓. From cost: 8.65 ÷ 129 = 6.705% → **6.71%** ✓. Per $1,000: $81.8 → $82 ✓; $67.1 → $67 ✓.
- **Parity −35% survivable at ≤2.86%:** 0.01 ÷ 0.35 = **2.857%** ✓. The memo discloses that it carries 3.0% and that 3.0% × 0.35 = **1.05%**, "fractionally over" (§5.2). This is consistent with C4c.
- **§5.3 three-denominator table:**
  - (a) LNW $690: 0.03 × 690 = **$20.70** ✓; 131.07 ÷ 690 = **19.0%** ✓; 19.0 ÷ 3.0 = 6.3 → "at least 6×" ✓; 1% = $6.90 < stop loss of $8.65–10.72 per ADS ✓; 1.5% = $10.35 → 0 ADS ✓.
  - (b) LNW $6,900: 0.03 × 6,900 = **$207** → floor(207 ÷ 131.07 = 1.58) = **1 ADS** ✓; 131.07 ÷ 6,900 = **1.90%** ✓; 1.5% = $103.50 → 0 ✓; two ADS = 262.14 ÷ 6,900 = **3.80%** ✓; parity gap on one ADS = 131.07 × 0.35 = **$45.87** = 0.665% ✓.
  - (c) LNW $69,000: 0.03 × 69,000 = $2,070 ÷ 131.07 = 15.79 → **15** ✓; 1.5% = $1,035 ÷ 131.07 = 7.90 → **7** ✓. Divisors: 131.07 ÷ 0.03 = **4,369** ✓; 131.07 ÷ 0.015 = **8,738** ✓.
  - HK$5,396 ÷ US$690 = 7.82 (implied HKD/USD) ✓, as disclosed.

### 9b. Other arithmetic re-run (all ✓ unless noted)
- §1.2 distances from $131.07: 122.20 → −6.8%; 127.3 → −2.9%; 130.0 → −0.8%; 140 → +6.8%; 146.8 → +12.0%; 149.9 → +14.4%; 152.35 → +16.2%; 158.5 → +20.9%; 162.0 → +23.6% ✓ (all nine).
- §1.5 MoS at $131.07: (80 − 131.07) ÷ 80 = −63.8%; (102.4 − 131.07) ÷ 102.4 = −28.0%; (112 − 131.07) ÷ 112 = −17.0%; (129.4 − 131.07) ÷ 129.4 = −1.3%; (150.7 − 131.07) ÷ 150.7 = +13.0%; 129.4 × 0.6 = $77.6 → $78 ✓.
- §2.2: 1,000 ÷ 131.07 = 7.63; 100 × 131.07 = 13,107; 1,500 ÷ 131.07 = 11.44 → 11; 7,500 ÷ 131.07 = 57.2 → 57 ✓.
- §2.3 drift: 3.0 × 137.71 ÷ 131.07 = 3.15; × 146.8 ÷ 131.07 = 3.36; × 149.9 ÷ 131.07 = 3.43; 3.36 × ⅔ = 2.24 ✓. Excess fractions 1 − 3/4 = 25%, 1 − 3/5 = 40%, 1 − 3/6 = 50% ✓.
- §2.4 ADV: 15.77M × $131 = $2.07bn; 5% = $103M ✓ (inference, labelled).
- §4.3: 3.0 × 6.71% = 0.20%; × 8.18% = 0.25%; × 13.4% = 0.40%; × 33% = 0.99% → 1.00% ✓. Override 7.5 × 6.71% = 0.50%, × 8.18% = 0.61% ✓.
- §4.3 Kelly: (148.35 − 129) ÷ 129 = 15.0%; b = 15.0 ÷ 9.3 = 1.61; break-even p = 1 ÷ 2.61 = 38% ✓; f(0.45) = 0.45 − 0.55 ÷ 1.61 = 0.108; f(0.50) = 0.50 − 0.50 ÷ 1.61 = 0.189 → quarter-Kelly 2.7–4.7% ✓. (It inherits the CRO's 9.3%, which C4d corrects to 8.86%. With b = 15.0 ÷ 8.86 = 1.69, quarter-Kelly is 3.1–5.1%. Informational only; immaterial.)
- §5.1: 131.07 × 0.866 = 113.51; 13,107 × 0.134 = 1,756; × 0.65 = 85.20; 13,107 × 0.35 = 4,587; × 0.46 = 60.29; 13,107 × 0.54 = 7,078 ✓.
- §5.2: at 1.5% → 0.20 / 0.525 / 0.81; at 7.5% → 1.005 / 2.625 / 4.05 ✓.
- §5.4 worked example ($500k illustrative): 15,000 ÷ 131.07 = 114.4 → 114; 114 × 131.07 = 14,942 = 2.99% ✓; 114 × 8.65 = 986 ✓; 14,942 × 0.134 = 2,002 ✓; × 0.35 = 5,230 = 1.05% ✓; L1 ⌈38⌉ → 76; L2 ⌈25.3⌉ = 26 → 50 ✓; 50 × 158.5 = 7,925 = 1.585% ✓; floor(7,500 ÷ 158.5 = 47.3) = 47 → sell 3 ✓; 150 × 131.07 = 19,661 = 3.93% → sell 36 ✓.
- §3 proceeds: 33.33 × 146.8 = 4,893; × 149.9 = 4,997; 22.22 × 158.5 = 3,522; × 162 = 3,600 ✓.

### 9c. Findings
1. **"7 cents above cost" is 18 cents (Low).** §1.1 line 47 and §6 line 299 say "the day's low ($129.18) was **7 cents** above cost". 129.18 − 129.00 = **$0.18**. The rhetorical point ("touched cost") survives.
2. **§3 L2 rounding is inconsistent with §5.4 (Low).** §3 sells 34 at L1 (leaving 66), then sells "**23** (22.2 rounded up)", computed as ⅓ of the *fractional* 66.7. Its residual column then shows "**44**", but 66 − 23 = **43**. On whole ADS, ⅓ of 66 = 22.0 → sell 22 → residual 44. §5.4 does it correctly on integers (⅓ of 76 → 26). D2 "after L1 only: sell 17" has the same problem: 66 − 50 = **16**. 死潘狗's tickets should use the §5.4 (integer) method. Not material to any cap.
3. **Forgone upside in the §6 counter-argument is understated (Low–Medium).** The memo states "~$530 of foregone gain per 100 ADS (33 ADS × ~$16)". The trade being evaluated is selling **50** ADS now at $131.07 instead of holding them. If Reduce 1 is reached at its midpoint ($148.35), the forgone mark-to-market is 50 × (148.35 − 131.07) = 50 × 17.28 = **~$864**, of which ~17 ADS would have been realised at L1. The memo's 33-ADS count matches neither framing.
   - Re-stated trade-off: **~$864 of conditional upside against ~$878 (−13.4% gap; 50 × 131.07 × 0.134) to ~$2,294 (parity; 50 × 131.07 × 0.35) of conditional loss per 100 ADS.**
   - On the gap case alone it is roughly even. Only the parity case makes it lopsided.
   - "It is not a close call on the numbers" is therefore overstated.
   - The recommendation survives on its two independent grounds: the MoS failure, and parity inside budget at 1.5%. The memo correctly labels it a recommendation, not a condition.
4. **Reading (a)'s denominator excludes the SKHY position itself (Low; conclusion unchanged).** If the Owner holds N ≥ 1 SKHY ADS at another broker, LNW cannot be $690. It is at least 690 + 131.07N. For N = 1: 131.07 ÷ 821.07 = **16.0%**, not 19.0%. The cap is 3% × 821.07 = $24.63, still 0 ADS. For any N, the position share is 131.07N ÷ (690 + 131.07N) ≥ 16%. **Reduce-to-zero under reading (a) is robust**; only the "19.0%" and "6×" figures change (to ≥16%, ≥5.3×).
5. **Conviction proxy (Low, disclosed).** Method step 3 (`.claude/agents/position-sizing-analyst.md` lines 22–23) scales size by **committee** score. The committee has not convened, so Zac uses desk scores (25 / 32 / 35) as a proxy and says so. Acceptable as disclosed. The committee score should replace the proxy when it exists.

### C9 result: PASS WITH FLAGS
Every cap, stop, conversion and worked-example number reproduces, including the four checks in the brief (22 ADS; $10.72 = 8.18%; 2.86%; the §5.3 table). Flags: the 18-cent slip; L2/D2 rounding; the understated forgone upside; the reading-(a) denominator. None changes the 3.0% cap or the 1.5% recommendation.

## Flags with severity

| # | Severity | Report | Flag | Changes a conclusion? |
|---|---|---|---|---|
| F1 | **Medium** | CEO, CRO | "44–56%" headline: the top half rests on undated FX; the dated measurement is 43–52% (C1b) | No — cap band 2.9–3.3% brackets 3.0% |
| F2 | **Medium** | CEO, financials, CRO | "$98 per ADS-equivalent" uses a stale ₩1,523.5 rate; correct is ~$111 (28 Oct) / ~$91–97 (10–11 Nov) (C1c) | No — Owner-facing sentence wrong |
| F3 | **Medium** | CEO | "Four departments independently arrived at the same number" — false (C8 #1) | No |
| F4 | **Medium** | CEO | "Premium of roughly half its value" — it is ~30–34% of value (C8 #9) | No — but it overstates the at-risk share ~1.5× in the verdict sentence |
| F5 | **Medium** | CEO | "Volume-locked through 2029 … ceilings, not floors" — supplier narrative / NOT OBTAINED stated as fact; contradicts the valuation's 35% "floors hold" scenario (C8 #7) | No |
| F6 | **Medium** | CEO | "D&A 50%+ of trough-year revenue" — an illustrative ₩60tn trough stated as fact; the valuation's trough revenue gives 19–33% (C8 #6) | No |
| F7 | **Medium** | Industry memory-cycle | "HBM margins 2–3x DDR5" still on disk as a live baseline (C5a) | No — reuse risk |
| F8 | Low–Med | Valuation | 40% MoS has no firm rule and no 菲比斯 moat review behind it (C3f) | No — fails at 0% MoS too |
| F9 | Low–Med | CRO | ₩1.64m "Aug peak" derived from the wrong endpoint; ₩1,759,000 was on disk (C7b) | No — the error was conservative |
| F10 | Low–Med | Memory-cycle | ₩1,132,000 dated to both 5 and 6 Nov (C7d) | Unknown — 6 Nov premium possibly understated |
| F11 | Low–Med | CEO, financials | HBM "inverted" stronger than one 1Q26 per-wafer estimate supports (C5c) | No |
| F12 | Low–Med | Sizing | Forgone upside $530 vs ~$864 (C9c-3) | No |
| F13 | Low | CRO | E[loss at stop] uses an undisclosed 7.5% input; correct −8.4% to −9.4% (C4d) | No |
| F14 | Low | CRO | 3.0% cap shows 1.05% at risk at −35% in its own table (C4c) | No |
| F15 | Low | CRO | Risk score 29.75 published as 32 (disclosed) (C4d) | No |
| F16 | Low | Valuation | "16% above MS target" → 7.8% (C3g) | No |
| F17 | Low | Valuation | FX-direction prose reversed (C1d) | No |
| F18 | Low | Valuation | DCF script in session scratchpad, not in repo (C3a) | No — audit trail gap |
| F19 | Low | CEO, CRO, valuation | "October selloff −20% vs −31%" is an Aug→Nov window (C7c) | No |
| F20 | Low | CEO | Stale carry-forward framed as "Elon Musk vs 巴爺爺" dissent (C5a) | No |
| F21 | Low | Sizing | "7 cents" → 18 cents; L2/D2 rounding; reading-(a) denominator (C9c) | No |
| F22 | Low | Technicals | "Thu 6 Nov" → Fri (C7e) | No |

**No High-severity flags.** No flag changes the hold-with-conditions verdict, the add veto, the 3.0% cap or the 1.5% recommendation.

## Bias observations

1. **Directional hardening in the CEO synthesis (confirmation bias).** All ten C8 items push the same way: a larger premium, a lower parity, more fragile economics, a weaker LTA book. Not one inference was hardened in the bullish direction. Each is individually small. Together they make the Owner-facing narrative more bearish than the departments' qualified evidence. The verdict happens to be supported independently by the later valuation and CRO work, so the bias did not change the outcome this time. It is still a pattern, not noise.
2. **Narrative lock-in on "44–56%".** One desk's FX sensitivity range became the firm-wide measured fact in four documents (CEO, CRO twice, valuation §1). The valuation desk measured 43% at dated FX on 12 Nov and wrote it down, and the number was not updated anywhere downstream. **A correction that does not propagate is the main failure mode in this package.** The same thing happened with the CRO's ₩1.64m: the right number was on disk in the technicals file.
3. **Groupthink check: does dissent exist?** Yes, but only inside the bear frame. On-disk dissent includes:
   - the valuation's scenario (c) at 35%, worth $151/ADS;
   - Morgan Stanley's ₩1.6m and the Rosenblatt $400 PT (technicals §1);
   - financials' "cannot say the peak is reached";
   - Zac's honest counter-argument.

   No desk argues for adding, or for holding above 3%. The bull case exists only as one scenario branch. The firm's philosophy says "Unanimous enthusiasm is a warning sign"; unanimous caution deserves the same scrutiny. The committee should ask whether any desk was tasked to steelman the broker 2027 OP (₩394–489tn) and the LTA book. None was.
4. **Recency.** The sizing memo handles the 13 Nov −4.8% print soberly: it reprices to market and does not change the recommendation on one session. No recency bias found.
5. **Anchoring on cost.** The CRO and valuation measure MoS and stop distance from $129 (the Owner's cost). The sizing memo correctly moves to market ($131.07) because the cap is measured at market. The $129 anchor is a sunk cost; the CEO says so (line 132). Acceptable.

**Recurring failure patterns for 床狗 (prompt fixes):**
- (a) **Propagation.** When a downstream desk recomputes an upstream figure, the CEO/committee synthesis must use the recomputed figure, and the upstream file should get a dated correction note.
- (b) **Epistemic tags survive synthesis.** Any qualifier in the source ("say", "estimate", "MY READ", "supplier narrative", "DERIVED", "NOT OBTAINED") must appear in the sentence that uses the figure.
- (c) **Every prose number computed, not typed.** The 16%, 7 cents and 7.5% slips are all prose arithmetic. Require that any percentage or difference in prose come from a shown calculation.
- (d) **Scripts persist.** Analysis scripts cited as an audit trail must be copied into the repo (e.g. `scripts/analysis/`), not left in a session scratchpad.
- (e) **Retirements must be executed.** When a figure is retired, the retiring desk files a correction note on every current report that carries it.

## Required fixes

**CEO synthesis (FAIL — return to author before committee):**
1. Line 13–15: replace "Four departments independently arrived at the same number" with "Two desks measured the November premium on assumed FX (44–56%); at the dated 10 Nov rate it is 43%, and 43–52% across 6–11 Nov."
2. Line 19: correct "FX sensitivity 1,350–1,380 → 44–56%" to "1,350–1,460 → 44–56%".
3. Line 29–30: replace "$98" with "the ordinary trades at ~$91–97 per ADS-equivalent at current FX (10–11 Nov); the Owner paid $129".
4. Line 35: relabel "October selloff (−20% vs −31%)" as "late Aug → 10 Nov (−20% vs −31%); 29 Oct → 6 Nov −21% vs −26%".
5. Line 67: replace "currently inverted" with "TrendForce estimated HBM per-wafer profitability below DDR5 RDIMM in 1Q26".
6. Line 72–74: restore the qualifier: "at an illustrative trough revenue of ~₩60tn, 50–65%; at the valuation's ₩120–150tn, ~20–33%".
7. Line 93–94: "14 LTAs cover >50% of 2027–28 capacity (company); 'sold out through 2029' is supplier narrative; floors and take-or-pay NOT OBTAINED; post-2Q26 LTAs carry ceilings."
8. Line 154: "a regulatory premium worth roughly a third of its price".
9. Line 102 and 62: add "(DERIVED from a calendar-2026 licence)" and "(includes an undisclosed amount of customer deposits)".

**Industry memory-cycle:** add a dated correction note at line 16 that "HBM margins 2–3x DDR5" is withdrawn (see financials §2, CEO synthesis), and resolve the 5 vs 6 Nov dating of ₩1,132,000 (lines 253–254).

**CRO (PASS WITH FLAGS — fix before the next re-score, not before committee):**
- §4: disclose or correct the near-level input (7.5% vs 6.7%). Corrected E[loss] is −8.4% / −8.9% / −9.4%.
- §5 and §13: replace the derived ₩1.64m with technicals' ₩1,759,000 (24 Aug, Eulerpool, PROXY). The range becomes ~−25% to −51%.
- §3.1 and §3.4: use the valuation's dated-FX 43% (10 Nov), and drop or correct the $98 anchor row.
- §9: add one line acknowledging 1.05% at risk at −35% under the rounded 3.0% cap.

**Valuation (PASS WITH FLAGS):** "16% above" → "8% above" (§0); reverse the FX-direction sentence (§8.1); commit `skhy_val.py` to the repo; state ×1.40 as a mean-reversion assumption below the November measured band.

**Sizing (PASS WITH FLAGS):** "7 cents" → "18 cents" (§1.1, §6); use integer rounding in §3 L2/D2 (22 → residual 44; D2 after L1 sells 16); restate the §6 trade-off as ~$864 vs ~$878–2,294; note that reading (a) gives ≥16% (not 19.0%) once SKHY is in the denominator.

**Firm-level (for the CIO / Owner):** decide whether the firm wants a default numeric margin-of-safety rule in `knowledge/investment-philosophy.md`, or wants to keep per-name analyst discretion. Either way, write the decision down.

## NOT OBTAINED register

| Item | Status | Bears on |
|---|---|---|
| USD/KRW for 11, 12 and 13 Nov 2026 | NOT OBTAINED — only 10 Nov ₩1,337.5 dated | premium at $131.07 and $137.71; cap band |
| 000660.KS close 11, 12 and 13 Nov | NOT OBTAINED (11 Nov ≈ ₩1,299,000 is *computed* from +7.2%) | premium at the live print |
| **Premium at the live $131.07 print** | NOT COMPUTABLE from disk | whether 3.0% is still the right cap today |
| SKHY 11 Nov official close | NOT OBTAINED by any desk | timeline |
| 13 Nov SKHY close | NOT OBTAINED — $131.07 is a 19:50 UTC intraday print; the stop is a close rule | stop monitoring |
| Whether ₩1,132,000 is the 5 Nov or 6 Nov close | UNRESOLVED (memory-cycle lines 253–254 conflict) | 6 Nov premium (50.7–52.2%) |
| ₩1,523.5 July conversion rate | SUSPECT — implies 12% won appreciation that no desk records; the late-Aug back-test fits 1,400–1,430 | financials' ₩39.9tn net proceeds; $98 |
| TrendForce 22 Jul 2026 article text (HBM per-wafer < DDR5 RDIMM, 1Q26) | NOT VERIFIED — no fetch this session; the URL slug is consistent with the topic only | C5 retirement |
| Scenario DCF values 964k / 719k / 1,440k | NOT RE-RUN — script not in repo | C3 central |
| 菲比斯 moat review of SKHY | NOT RUN | basis for widening MoS to 40% |
| Firm numeric MoS rule | DOES NOT EXIST on disk (`knowledge/`, `config/`, `.claude/agents/`) | C3f |
| 24 Aug 2026 ordinary price | ON DISK as PROXY (₩1,759,000, Eulerpool, technicals line 77) — the CRO wrongly lists it NOT OBTAINED | CRO §5 |
| 3Q18 OP; FY2020 OP | NOT OBTAINED (financials, valuation) | C2 residuals |
| LTA floor prices / take-or-pay / deposit amounts | NOT OBTAINED (all desks) | CEO line 93–94; valuation scenario (c) weight |
| Customer deposits inside ₩114.5tn cash | NOT OBTAINED | net cash; CEO line 62 |
| Owner's SKHY ADS count, broker, margin status; LNW | NOT DISCLOSED | every % of LNW figure; reading (a)/(b)/(c) |
| KSD conversion-quota status since 23 Jul | NOT OBTAINED | the binding cap's premise |
| Wuxi 2027 licence; exact 2026 expiry | NOT OBTAINED / 31 Dec DERIVED | Condition 6 |
| Execution tickets (`reports/execution/2026-11-13-skhy-tickets.md`) | NOT AUDITED (outside brief) | may inherit C9 slips |

---
*Audit of argument, not conclusion. Every check above cites the file and line it was run against; every computation is shown. No report or config file was modified. No web searches were performed. Research and decision support only — not financial advice.*

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
