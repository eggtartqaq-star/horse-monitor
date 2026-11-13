# SKHY — AI Audit of Committee Package (2026-11-13)

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence)
**Scope:** Consistency and provenance audit of files on disk only. No web searches performed (CEO instruction; rate limit). No Bash tool was available in this session — all arithmetic below is shown inline, step by step, so it can be re-run.
**Under audit:** CEO synthesis (`reports/committee/2026-11-12-skhy-ceo-synthesis.md`), CRO review (`reports/risk/2026-11-12-skhy-cro-review.md`), valuation (`reports/equity/2026-11-12-skhy-valuation.md`), sizing (`reports/portfolio/2026-11-13-skhy-sizing.md`), and their upstream desk reports dated 2026-11-11 (technical, news, financials, regulatory, industry/memory-cycle).
**Checkpoint:** C1–C6 complete. C7–C9, verdict, register pending.

## Verdict

_(pending — filled after C9)_

## Claims checked

| # | Claim | Result | One-line note |
|---|-------|--------|---------------|
| C1 | ADS premium 44–56% | **PARTIAL** | Each desk reproduces its own %; the 50–56% top of the range rests on FX 1,400–1,460 that no dated print supports; at the only dated 10 Nov rate (₩1,337.5) the premium is 43%. The "$98 ADS-equivalent buyback price" is FX-stale: ~$111 at Nov rates. |
| C2 | Peak-to-trough survival 13% / <0% | **PASS** | Arithmetic reproduces; peak/trough years defined consistently (annual peak year → annual trough year) in both cycles. Minor: 3Q18 OP unconfirmed. |
| C3 | Valuation $80 / $112 / $102 / 40% MoS | **PASS WITH FLAGS** | $102 reproduces ($102.40). ×1.40 is at/below the bottom of the dated Nov measurements (43–52%); not material. 40% MoS is reasoned in-file but is analyst judgement — **no numeric MoS rule exists anywhere in `knowledge/` or `config/`**. One prose arithmetic error ("16% above MS target" is 7.8%). |
| C4 | CRO 3% cap arithmetic | **PASS WITH FLAGS** | 1 − 1/1.50 = 33.3% ✓; 1% ÷ 33.3% = 3.0% ✓; 1% ÷ 35% = 2.857% ✓. Rounding to 3.0% is immaterial vs measurement error, but the CRO's own §9 shows 1.05% at risk at −35% — a breach of the 1% budget at its own cap. E[loss at stop] rows are overstated ~0.5pp (undisclosed 7.5% input). Risk score 29.75 → 32 is a discretionary uplift, disclosed. |
| C5 | Retired "HBM 2–3x DDR5" claim | **PARTIAL** | Financials' citation transcribes faithfully into the CEO file (source not re-fetched). **But the Nov memory-cycle report still carries "HBM margins 2–3x DDR5" (line 16) as a live baseline with no retraction.** Retirement also equates two different metrics (margin multiple vs per-wafer profitability). |
| C6 | tradingkey blacklist compliance | **PASS** | 8 mentions across 7 SKHY reports; every one is an exclusion note. Zero citations, zero tradingkey URLs. |
| C7 | Price timeline consistency | pending | |
| C8 | Inference presented as fact in CEO synthesis | pending | |
| C9 | Sizing memo arithmetic | pending | |

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

## C3 — Valuation $80 / $112 / $102 / 40% MoS — PASS WITH FLAGS

Source: `reports/equity/2026-11-12-skhy-valuation.md` §0, §3, §6, §8.

### 3a. Ordinary central ₩1,070,000 — reproduces from the stated scenarios
- 0.40 × 964,000 + 0.25 × 719,000 + 0.35 × 1,440,000 = 385,600 + 179,750 + 504,000 = **₩1,069,350** → "~₩1,069,000 / ₩1,070,000" ✓
- I cannot re-run the scenario DCFs themselves: the cited script lives in a session scratchpad (`…/scratchpad/skhy_val.py`), not in the repo, so the per-scenario values (964k / 719k / 1,440k) are **taken on trust**. Flag (Low): the audit trail the analyst names is not persisted on disk.

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
- Structural note: the weight (30% lift) and multiplier are both labelled "mine, no source" (§8.2) — correctly marked as judgement under rule 5.

### 3d. Is ×1.40 consistent with the measured premium?
Measured at dated FX (C1): 6 Nov 50.7–52.2%; 10 Nov 43.1%; 11 Nov intraday ~47%. Earlier: ~41% late Sep, ~30% 23 Jul (valuation §8).
- ×1.40 sits **at or just below the bottom** of the November measurements, not at their centre. The file's justification is "≈ the Sep–Nov level" — true if September (41%) is weighted in; it is not the November level.
- Is the gap explained? **Partly.** §8.2 explains the 1.15 floor (premium can compress without a rule change; fell to 16% once) and the multiplier is explicitly a forecast of a scarcity rent, not a measurement. A forward-looking multiplier below spot is defensible; it is not stated *as* a mean-reversion assumption, which it is. Low.
- Materiality, recomputed at the November midpoint (×1.47): 80 × 1.47 = 117.6; PW = 24.0 + 0.70 × 117.6 = 24.0 + 82.3 = **$106.3**; MoS at $129 = (106.3 − 129) ÷ 106.3 = **−21%** (vs −26%). At ×1.52 (6 Nov high): 80 × 1.52 = 121.6; PW = 24.0 + 85.1 = **$109.1**; MoS = **−18%**. **Every construction remains negative; the conclusion "fails the MoS test" is insensitive to the multiplier choice within the measured band.**
- Also: the "persists" band 1.15–1.55 is described as "observed premium band since listing excluding the listing-week spike (16–56%)". The 56% top is the technicals' FX-1,460 sensitivity row, which C1 found unsupported by any dated print; the dated top is ~52%. Immaterial to the result (high PW at ×1.52 instead of ×1.55: 93.46 × (0.30 + 1.064) = $127.5 vs $129.4).

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
- `config/risk-limits.yaml` — no MoS field. (Read in full: portfolio / concentration / per_trade / options / process blocks only.)
- `knowledge/investment-philosophy.md` line 14–15 — "bought with a margin of safety (菲比斯 and 𢦀鳩仔's departments)". **No number.**
- `.claude/agents/valuation-analyst.md` line 27–28 — "Demand a wider margin when 菲比斯 rates the moat narrow or eroding." **No number.**
- Precedents cited by the valuation are real: `reports/equity/2026-08-14-6160hk-moat.md:621` ("I require a 30% margin of safety") and `reports/equity/2026-08-21-msft-moat.md:967` ("I require a 20% margin of safety"). Also `reports/equity/2026-07-19-klac-valuation.md:37` (菲比斯 25–30%).

**Finding:** **The firm has no numeric margin-of-safety rule on disk.** Every required MoS to date (20 / 25–30 / 30 / 40%) is set per-name by the moat analyst or valuation analyst. The 40% here is **reasoned, not asserted** — §8.4 gives three compounding reasons (late-cycle central unreliability with a 2x scenario spread; an independent premium-collapse leg; eroding HBM pricing power) — but the trigger the agent prompt names ("when 菲比斯 rates the moat narrow or eroding") **has not fired: no 菲比斯 moat report on SKHY exists** (Glob `reports/**/*skhy*` returns no moat file). The valuation substitutes "巴爺爺's moat-equivalent reading". Severity **Low–Medium**: it does not change the result (the position fails at 0% required MoS on the PW central, −26%), but the committee should know the 40% is one analyst's number, with no firm-level anchor and no moat review behind it.

### 3g. Arithmetic error in prose (§0 line 21) — Low
"at parity it is ₩1.73m — … 16% above the Morgan Stanley target (₩1.6m, cut 11 Nov)":
- 129 × 1,337.5 × 10 = **₩1,725,375** ✓ (₩1.73m)
- 1,725,375 ÷ 1,600,000 = 1.0784 → **7.8% above**, not 16%.
Also checked, correct: 129 ÷ 1.40 = 92.14 × 13,375 = ₩1,232,400 (₩1.23m) ✓; 129 ÷ 107.66 = 1.198 ("(c) at 20% premium") ✓; 129 ÷ 80 = 1.6125 ("base at 60%") ✓; ordinary vs central 1,132 ÷ 1,070 = +5.8%, 1,299 ÷ 1,070 = +21.4% ("6–21%") ✓.

### 3h. Multiples (§5) — reproduce
1,212,000 × 700M = ₩848.4tn; − 98.7 = ₩749.7tn EV ✓; 750 ÷ 269 = 2.79x ✓; 848 ÷ (269 × 0.75 = 201.75) = 4.20x ✓; 750 ÷ 65 = 11.5x ✓; 848 ÷ 48.75 = 17.4x ✓.

### C3 result: PASS WITH FLAGS
Every load-bearing valuation figure reproduces. Flags: ×1.40 is below the November measured band, unexplained as a mean-reversion assumption (Low; immaterial — MoS stays −18% to −26%); 40% MoS has no firm-level rule and the moat review that would justify widening was never run (Low–Medium); "16% above MS target" is 7.8% (Low); DCF script not persisted to the repo (Low).

## C4 — CRO 3% cap — PASS WITH FLAGS

Source: `reports/risk/2026-11-12-skhy-cro-review.md` §0, §1 row 9, §3.3, §4, §9, §10; `config/risk-limits.yaml`.

### 4a. Config input
`config/risk-limits.yaml` line 18: `max_risk_per_trade: 0.01  # 1% of portfolio at risk (size x distance to stop)` ✓ **1%.**
Note: the config defines risk as *size × distance to stop*. Counting the premium (which has no stop) against this line is the CRO's **extension** of the rule, which he labels as such and proposes as a new `instrument:` block "NOT applied — Owner approval required" (§3.3, §11). The 3% cap is therefore a CRO veto-authority judgement built on the 1% budget, not a number the config produces by itself. Correctly disclosed.

### 4b. Premium → loss to parity
- 50% premium: loss = 1 − 1 ÷ 1.50 = 1 − 0.6667 = **0.3333 → 33.3%** ✓
- Cap: 0.01 ÷ 0.3333 = **3.00%** ✓
- 44%: 1 − 1 ÷ 1.44 = 0.3056 → 0.01 ÷ 0.3056 = **3.27%** ("3.3%") ✓
- 56%: 1 − 1 ÷ 1.56 = 0.3590 → 0.01 ÷ 0.3590 = **2.79%** ("2.8%") ✓
- **At dated-FX premiums (C1):** 43.1% → loss 30.1% → cap **3.32%**; 47% → 32.0% → **3.13%**; 52.2% → 34.3% → **2.92%**. Dated-FX band for the cap: **2.9–3.3%**.

### 4c. Zac's −35% / 2.86%
- 0.01 ÷ 0.35 = **0.02857 → 2.857%** ✓
- −35% to parity corresponds to a premium of 1 ÷ 0.65 − 1 = **53.8%**, which is above every dated-FX measurement (max 52.2%). So −35% is a conservative stress, not the measured case.
- Is 3.0% vs 2.86% material? At 3.0% × 35% = **1.05%** at risk — 0.05pp (5%) over the 1% budget; per $100,000 LNW, **$50**. That is well inside the measurement band in 4b (2.9–3.3%). **Not material to the decision.** But it is an internal inconsistency: the CRO's own §9 line "−35% premium = 1.05%" shows the cap breaching the budget it was derived from. A one-line acknowledgement ("3.0% is a rounded cap; at the −35% stress it is 1.05% at risk") would close it. Low.

### 4d. Other CRO arithmetic checked
- §3.4: 129.66 ÷ 1.40 = 92.61 → (92.61 − 129) ÷ 129 = −28.2% ✓; ÷ 1.44 = 90.04 → −30.2% ✓; ÷ 1.50 = 86.44 → −33.0% ✓; ÷ 1.56 = 83.12 → −35.6% ✓; $84 → −34.9% ✓; $98 → −24.0% ✓ (but $98 itself fails, C1c → −13.8%).
- §4: 120.35 ÷ 129 = 0.93295 → −6.71% ✓; 120.35 ÷ 129.66 = 0.9282 → −7.18% ✓; 122.20 ÷ 129 = 0.9473 → −5.27% ✓; 1 ÷ 0.067 = 14.9% ✓; 1 ÷ 0.134 = 7.46% → 7.5% ✓.
- **§4 E[loss | stop hit] — does NOT reproduce from the table's own inputs.** With near-level = 6.7%, −10%, −13.4%:
  - 0.60 × 6.7 + 0.30 × 10 + 0.10 × 13.4 = 4.02 + 3.00 + 1.34 = **8.36%** (file: 8.9%)
  - 0.50 × 6.7 + 0.35 × 10 + 0.15 × 13.4 = 3.35 + 3.50 + 2.01 = **8.86%** (file: 9.3%)
  - 0.40 × 6.7 + 0.40 × 10 + 0.20 × 13.4 = 2.68 + 4.00 + 2.68 = **9.36%** (file: 9.7%)
  - The file's figures reproduce only if "fills near level" = **7.5%**: 4.50 + 3.00 + 1.34 = 8.84 ✓; 3.75 + 3.50 + 2.01 = 9.26 ✓; 3.00 + 4.00 + 2.68 = 9.68 ✓. The 7.5% input is **undisclosed** and contradicts the table directly above (−6.7%). Corrected range: **−8.4% to −9.4%**, not −8.9% to −9.7%. Headline "plan on ~−9% to −10%" should read "~−8.5% to −9.5%". Low — it is not the binding constraint, and "size for −13.4%" is unaffected.
- §5: 1,132,000 ÷ 0.69 = ₩1,640,580 ("~₩1.64m DERIVED") ✓; ₩820,000 → 82,000 ÷ 1,350 = $60.74, ÷ 1,380 = $59.42 → −52.9% / −53.9% ✓. At dated ₩1,337.5: 82,000 ÷ 1,337.5 = $61.31 → −52.5% (immaterial).
- §9 translation: 3,000 ÷ 129.66 = 23.14 → **23 ADS** ✓; parity loss 3,000 × 0.33 = $990 / × 0.356 = $1,068 ✓; worst 3,000 × 0.68 = $2,040 ✓.
- §10 risk score: 0.30×10 + 0.15×40 + 0.20×30 + 0.10×45 + 0.10×35 + 0.15×45 = 3.0 + 6.0 + 6.0 + 4.5 + 3.5 + 6.75 = **29.75** ✓. Published as **32** — a **+2.25 discretionary uplift**, disclosed in-line with reasons. Flag (Low): the CEO brief and sizing memo quote "32/100" without the 29.75 computed figure. Either way it is below the ~40 initiation-veto line, so no conclusion changes.

### C4 result: PASS WITH FLAGS
The cap arithmetic reproduces (3.0%; 2.86% at −35%). Rounding 2.86 → 3.0 is immaterial (≤$50 per $100k; inside the 2.9–3.3% dated-FX band) but leaves the CRO's own table showing 1.05% at risk at the cap (Low). E[loss at stop] overstated by ~0.5pp from an undisclosed 7.5% input (Low). Risk score is 29.75 computed / 32 published (Low, disclosed).

## C5 — Retired claim "HBM margins 2–3x DDR5" — PARTIAL

### 5a. Does the Nov memory-cycle report still carry it? **Yes — FAIL on this sub-check.**
`reports/industry/2026-11-11-skhy-memory-cycle.md` §0, lines 14–16:
> **Baseline from `reports/industry/2026-08-21-msft-industry.md` (21 Aug 2026), not re-derived:** … - HBM margins **2–3x DDR5**.

Grep of the same file for "baseline|retire|stale|Introl|HBM (price|pricing|margin)" finds **no retraction, correction or caveat** anywhere else in the report. The file's later sections (line 138: "the mechanism by which HBM pricing power erodes"; line 313: "HBM pricing power is eroding before volume") move in the same direction as the retirement but **never withdraw the 2–3x figure**. The claim the CEO declares "retired" (synthesis lines 69–71, 136–139) is still on disk, bold, in the industry desk's current report, presented as a live baseline. Anyone reading the industry report alone would take it as current.

Secondary point: CEO §"Where the departments disagree" #1 frames this as "**Elon Musk vs 巴爺爺** on HBM economics". On disk, Elon Musk did not argue for 2–3x in November — he carried it forward "not re-derived". It is a stale carry-forward, not a disagreement; presenting it as dissent overstates the evidence that a debate occurred (Low).

### 5b. Does the financials file's citation say what is claimed? **Transcribes faithfully; source not re-verified.**
`reports/equity/2026-11-11-skhy-financials.md` line 18 and §2 line 90:
> TrendForce estimates that **HBM revenue and profitability per wafer fell below 64GB DDR5 RDIMM in 1Q26** … ([TrendForce 22 Jul 2026, "sk-hynix-set-to-post-record-operating-margin-in-q2-as-hbm-mix-weighs-on-asp-growth-and-ltas-gain-focus"])

- CEO line 68–69: "TrendForce estimates HBM per-wafer profitability fell *below* DDR5 RDIMM in 1Q26" — **faithful** to financials, including the "estimates" qualifier ✓.
- The URL slug supports the topic ("HBM mix weighs on ASP growth"); it does **not** by itself confirm the specific per-wafer comparison. Under this session's no-fetch instruction the source text is **NOT VERIFIED** — register.
- Corroboration on disk is thin: one wccftech item (SK hynix prioritising DDR5 output — directional) and one analyst construction (65% HBM vs 90% DDR5 margins) that the financials desk itself labels "**low-quality source, directional only**". So the retirement rests on **one TrendForce estimate for one quarter (1Q26)**, relayed by search extraction.

### 5c. Logic: does the evidence retire the claim?
- **Metric mismatch.** The August claim is a *margin multiple* ("HBM margins 2–3x DDR5"). The TrendForce point is *revenue and profitability per wafer*. HBM consumes materially more wafer area per bit than DDR5, so per-wafer profitability can fall below DDR5 while HBM's margin *percentage* remains comparable or higher. The two statements are not direct contradictions. The financials' own wording ("That was true in 2024–25 and is not true now") is stronger than a per-wafer estimate supports.
- **Time mismatch.** The evidence is a 1Q26 estimate published 22 Jul. The CEO says "currently inverted" in November. Nothing on disk dates the comparison after 1Q26; commodity DDR5 contract growth has since decelerated (+13–18%, +10–15% forecast — synthesis line 84), which would narrow the gap.
- **Verdict on the retirement:** correct to **stop reusing "2–3x"** (it is an August, Introl-sourced figure contradicted by a better-tier source); **overstated** to call the HBM thesis "inverted" as fact. The defensible wording is: "TrendForce estimated HBM per-wafer profitability below DDR5 RDIMM in 1Q26; the August '2–3x margin' figure is withdrawn pending a current HBM-vs-DDR5 margin comparison." The downstream use is appropriately hedged in the valuation (§2 line 68: "If one believes the HBM layer earns no premium … every value below falls ~15%") — that is the right treatment.

### C5 result: PARTIAL
- Citation transcription financials → CEO: PASS (source unverified this session).
- "Memory-cycle report no longer carries it": **FAIL** — line 16 still carries it with no retraction.
- Logic: retirement directionally justified; "inverted" (CEO line 67, financials §2) is stronger than one per-wafer estimate for 1Q26 supports.
- Severity: **Medium** (stale claim on disk in a current report is exactly the reuse risk the CEO is trying to prevent); **Low** for the metric/framing points.

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

CEO synthesis and sizing memo: **zero mentions**. No `tradingkey` string appears inside any URL or link in any SKHY file (the grep would have matched it).

Residual observation (not a finding): the regulatory desk notes tradingkey surfaced on the **ADR-quota story** and took "the same facts" from Money Today. The quota mechanism is the load-bearing fact behind the CRO's binding cap; it is independently sourced on disk (CRO §13: Bloomberg Línea, GuruFocus, Invezz 23 Jul, Tiger/Webull syndications), so the blacklist did not leave it single-sourced.

### C6 result: PASS
Eight occurrences across seven reports; every one is an exclusion note; zero citations.

## C7 — Date / price consistency
_(pending)_

## C8 — Inference as fact
_(pending)_

## C9 — Sizing memo arithmetic
_(pending)_

## Flags with severity
_(pending)_

## Bias observations
_(pending)_

## Required fixes
_(pending)_

## NOT OBTAINED register
_(pending)_
