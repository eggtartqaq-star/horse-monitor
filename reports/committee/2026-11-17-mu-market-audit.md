# Audit — MU vs SK hynix, market regime, tech vs defensives (2026-11-17)

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence) · **Date:** 2026-11-17 (evening UTC) · **Status:** IN PROGRESS — §1 complete

**Under audit (full depth):**
1. `reports/equity/2026-11-17-mu-valuation-refresh-vs-skhy.md` (𢦀鳩仔)
2. `reports/macro/2026-11-17-market-regime-tech-vs-defensive.md` (Peterson)
3. `reports/technical/2026-11-17-mu-skhy-defensives-technical.md` (CEO for 老詹)
4. `reports/news/2026-11-17-mu-skhy-semis-staples-news.md` and `reports/news/2026-11-17-nvda-earnings.md` (修大哥)
5. `reports/risk/2026-11-17-mu-skhy-style-cro.md` (John) — present at completion; checked in §5

**Checklist:** C1–C10 as in `reports/committee/2026-11-16-aapl-skhy-reentry-audit.md`, plus 床狗 patterns (f)–(j): (f) snippet numbers, (g) both drift models when σ > 50%, (h) one stock / one input, (i) underived triggers, (j) unbounded-horizon claims.

**Method / network.** No Bash: every computation is by hand and shown. Scripts read: `models/valuation/mu_val_nov.py`, `models/valuation/mu_vs_skhy.py`. Ten WebSearches run (results cited where used). No WebFetch attempted; no 403/DNS host retried. tradingkey.com appeared once in a result list and was not opened or used.

## 0. Verdict summary
_pending_

## 1. MU valuation refresh vs SKHY (𢦀鳩仔) — **PASS WITH CORRECTIONS**

### 1a. Arithmetic re-derived by hand from `mu_val_nov.py` inputs (C1) — reproduces

Discount factors at 12% (t = 0.4 / 1.3 / 2.3 / 3.3 / 4.3 / 4.8): 0.95568 / 0.86301 / 0.77054 / 0.68799 / 0.61428 / 0.58044. NOPAT = (rev × GM − opex) × 0.845.

| Scenario | FY27 NOPAT / FCF | FY28 FCF | FY29 FCF | FY30 FCF | FY31 FCF (value-driver) | PV explicit | PV(TV) | Equity / share | File |
|---|---|---|---|---|---|---|---|---|---|
| Bear | 129.29 / 88.29 | −0.79 | −1.40 (no shield) | 6.80 | 12.89 × 0.65 = 8.38 | **92.4** | 12.89 × 1.035 × 0.65 / 0.085 = 102.0 → **59.2** | 189.6 / 1.13 = **$167.8** | $168 ✓ |
| Base | 166.47 / 125.47 | 31.11 | 9.98 | 19.38 | 24.93 × 0.7333 = 18.28 | **179.0** | 24.93 × 1.04 × 0.7333 / 0.08 = 237.7 → **138.0** | 355.0 / 1.13 = **$314.1** | $314 ✓ |
| Bull | 195.83 / 154.83 | 97.31 | 44.22 | 45.35 | 50.02 × 0.75 = 37.52 | **320.3** | 50.02 × 1.05 × 0.75 / 0.07 = 562.7 → **326.6** | 684.9 / 1.13 = **$606.1** | $606 ✓ |

- PW: 0.25 × 167.8 + 0.5 × 314.1 + 0.25 × 606.1 = **$350.5** → "$351" ✓. TV share of base EV 138/317 = 44% ✓. MoS (351 − 697.83)/351 = **−98.8%** ✓; 0.6 × 351 = **$210.6** ✓.
- Reverse DCF (§7): value is linear in FY31 NOPAT with slope [0.7333 × 0.61428 + 1.04 × 0.7333/0.08 × 0.58044]/1.13 = **5.296 $/share per $bn**. $700 → 24.93 + (700 − 314.1)/5.296 = **$97.8bn** (EPS $86.5) ✓; $1,550 → **$258.3bn** (EPS $229) ✓. $98bn → (98/0.845 + 12.5)/0.42 = **$306bn** revenue ✓.
- Bridge: −44 + 87 + 28 + 59 − 57 − 25 = **+48** = 314 − 266 ✓.
- SK hynix-consistent normalisation (`mu_vs_skhy.py` line 36–38): CY26-equivalent EBIT 16.35 + 33.7 + 45.58 + 51.34 = **$147.0bn**; × 24% × 0.845 / 1.13 = **$26.4** ✓; FY26 EBIT $102.0bn → **$18.3** ✓.
- Head-to-head: SK mid-cycle NOPAT ₩65tn × 0.75 / 1,330 = **$36.65bn**; ordinary mkt cap ₩1,059,000–1,212,000 × 700M / 1,330 = $557–638bn → **15.2–17.4×** ✓; ADS × 1.43–1.52 → 21.7–26.5× ✓. MU 697.83 × 1.13 / 24.9 = **31.7×** ✓.
- IRR (§10): 1.12 × (351/700)^(1/3) − 1 = **−11.0%** ✓; bull +6.7% ✓.
- Touch table (§10), martingale model: $351 6m @ 72% → 13.7% + 1.988 × 5.4% = **24.5%** ✓; $211 6m @ 103% → 10.1% + 3.307 × 2.2% = **17.5%** ✓.

**C1 result: PASS.** Every figure I re-ran reproduces.

### 1b. The 10-year / discount-rate test (C2, C3, C10)

**Reconciling the 10y (closes yesterday's V2).** Both figures are right for their own dates. Today's searches: Trading Economics 13 Nov, "US 10Y Bond Yield Hits 4-week High", 5.16% midday and 5.15% at the week's end, "a 30bp surge on the week"; CNBC via Biztoc 5.127% early 13 Nov; 4.86% close 6 Nov ([Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/601151), [Advisor Perspectives 6 Nov](https://www.advisorperspectives.com/dshort/updates/2026/11/06/treasury-yields-snapshot-november-6-2026)). Peterson's 5.10% on 12 Nov (NST/Reuters) fits the path. **Ruling: 5.13–5.16% on 13 Nov is corroborated by three independent secondary outlets. It is still not primary (no H.15/DGS10 read).** It is also a **4-week high** that matches the ~5.15% YCharts print of 19 Oct cited in yesterday's audit. Over one month the 10y is roughly flat, which is what TLT's −0.4% 1m in the CEO table shows.

**V1 — 12% sits at the top of the defensible CAPM band, rounded up (MEDIUM; §3 "Discount rate", §2.2 bridge, §9).**
- File: 5.15 + 1.4 × 4.75 = **11.8%, rounded up to 12%**. July used 4.55 + 1.4 × 4.75 = 11.2%, **rounded down to 11%** (yesterday's audit, firm precedent line). A 60bp rise in rf became a 100bp rise in r, through two roundings that both point the bearish way.
- **One desk, two ERPs in 24 hours (pattern h).** 𢦀鳩仔 used ERP **4.41%** for AAPL on 16 Nov and **4.75%** for MU today ("same as July"). The only dated datapoint on disk is Damodaran **4.14%** (~1 Sep 2026, yesterday's audit V1).
- Defensible band, using inputs actually on disk: rf 4.86–5.15% × ERP 4.14–4.75% × β 1.4 → **10.7–11.8%**.
- Effect, from the file's own §9(c) grid: PW **$382 at 11%** (≈$366 at 11.5%). The bull case at 11%, by hand: PV explicit 324.3 + PV(TV) 656.5 × 0.60599 = 397.8 + 38 = 760.1 / 1.13 = **≈$673**.
- **Correction:** state r as a band (11–12%) with the reason for choosing its top; drop the round-up or disclose it; record one firm ERP in `knowledge/` (pattern h).

**V2 — "Even the bull case ($606) is below today's ~$700"; "1.15× the bull case" (MEDIUM; §1 table, §4, §0).** This holds only at r = 12%. At 11% the bull case is ≈$673, and ≈$692 with the V5 timing fix: **about the price**, not 13% below it. The sentence is the report's strongest rhetorical line. Its strength exceeds the evidence by one rounding step. **Correction:** "At 12% the bull case ($606) is below the price; at 11% it is ≈$670–690, roughly the price. No base or weighted case reaches it at any rate in the grid."

### 1c. Mid-cycle EPS $22.1 — defensible as a base, but not "the same basis" as SK hynix (C3, C9)

**Is $22.1 defensible against FY27 consensus ~$176.5 and NVDA's commitments?**
- **The ratio to peak is the wrong test.** $22.1 is 12.5% of FY27 consensus, but this peak runs at 86% GM, far above any prior memory peak. The file's construction is more testable: FY25-like margins (42% GM) on a business 2.7× FY25's revenue ($100bn vs $37.4bn), ROIC ~15% at the top of 菲比斯's band. That is internally coherent and disclosed.
- **NVDA commitments bear on timing, not on the FY31 level.** My search confirms the Q2 FY27 base: supply commitments **$119bn → $279bn, "primarily related to the procurement of memory"**, scheduled **$92bn rest of FY27 / $87bn FY28 / $88bn FY29** ([Nasdaq](https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock), [Fortune 26 Aug](https://fortune.com/2026/08/26/nvidia-q2-growth-results-jensen-huang/)). Tonight's $390bn / $203bn-in-FY28 was **not** found by my searches (index lag; not contradicted; see §4). Nvidia's FY28 runs Feb 2027–Jan 2028, which overlaps MU's FY27 and first half of FY28. It speaks directly to the file's **base FY28 (−38% revenue to $150bn at 55% GM)**, and so to the base-vs-late-peak weighting. It says little about FY31.
- **V3 — the head-to-head is not on "the same normalisation basis" (MEDIUM; §11 table row "Market cap ÷ mid-cycle NOPAT", §0 table, §11 item 1).** SK hynix mid-cycle = **24%** of CY26 peak OP. MU's $24.9bn NOPAT = 24.9 / (147.0 × 0.845 = 124.2) = **20%** of CY26-equivalent. The file says "~20–24%", which is two bases, not one. On the SK basis (24% → $26.4 EPS, NOPAT $29.8bn), MU = 789 / 29.8 = **26.5×**, so **1.5–1.7× the ordinary's 15.2–17.4×, not "~2×"**. The ranking **000660.KS > ADS > MU survives**: 1.5–1.7× still exceeds the 20–30% premium the file grants MU. But the Owner-facing "roughly twice" overstates it. Value effect at 12%: base 314 + 4.87 × 5.296 = **≈$340**, PW ≈ **$364** (file §8 already shows ~$290–345). **Correction:** use one ratio for both names, or print MU at 26.5–31.7× and say "1.5–2×".
- **V4 — scenario weights frozen at July's 25/50/25 (MEDIUM; §3 "Scenario-specific", §4).** "Fixed before the model was run; unchanged from July" is good anti-hindsight practice for a single run. Carried across four months, it ignores the dated evidence that has arrived since: the CFO's "86% floor", 28 up / 2 down revisions, the Q2 $279bn memory commitments, and now (unverified) $203bn in Nvidia's FY28. The file's own late-peak variant (base → $424) gives PW **$405**, and it already says "every reasonable weighting lands at $330–420". **Correction:** print PW as **$351–405** with the late-peak weight as the explicit open question. Name the datum that moves it (FY28 consensus; Nvidia's FY28 commitment schedule once verified against the 8-K).

### 1d. Other findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| V5 | LOW–MED | `mu_val_nov.py` line 37–38; §3 "Timing" | Explicit flows sit at mid-year (FY31 at t = 4.3), but the Gordon TV is discounted from t = 4.8, so the first terminal flow lands at t = 5.8, not 5.3. PV(TV) is understated by 1.12^0.5 − 1 = **5.8%**: base +$7, bear +$3, bull +$17, **PW +$8.5**. Methodological, bearish | Discount TV from t = 4.3, or disclose |
| V6 | LOW–MED | §10 touch table | **Rule (g): only one drift model shown.** It is the martingale ("zero expected price change"), labelled ✓, which is the *higher*-probability model, so no remoteness bias. The log-driftless column is missing, e.g. $351 in 6m @ 72%: **17.7%** vs 24% | Add the second column |
| V7 | LOW–MED | §10 "Expected return … about −11% a year over three years" | Headline picks N = 3. The same table gives **−2%/yr at N = 5** (pattern from yesterday's V5: headline selection) | "−2% to −11%/yr over 3–5 years; below T-bills either way" |
| V8 | LOW–MED | §11 "Instrument structure" | "**one-way conversion**". The firm's own regulatory desk (`2026-11-11-skhy-regulatory.md` lines 229, 289) recorded **two-way conversion from 29 Jul 2026, within the cap**. See §4d for the ruling. The economic conclusion (the premium can't be arbitraged while the cap is exhausted) is unchanged | "two-way since 29 Jul within an exhausted 2.5% cap; inbound conversion effectively closed" |
| V9 | LOW | §3 base FY27 | Base FY27 GM **85%** sits below the CFO's guided **86% FY27 floor** quoted in §2.1/§2.2 (+$1.7/share if 86%). §3 says "~15% below street", §5.1 "~17%" | Use ≥86% or say why; one figure |
| V10 | LOW | §2.2 prose under bridge | "+$174 up / −$82 down" omits the −$44 first step (capex wave / re-timing). Arithmetic nets correctly (+48) | Name all three |
| V11 | LOW | §6 DCF row | "No memory company has ever held peak margins through a capacity wave": unsourced universal (pattern j-adjacent) | "No case in the firm's files (2018–19, 2022–23)" |
| V12 | LOW | §3, §13 "Scripts" | Cites scratchpad paths ("not durable") although the scripts are on disk at `models/valuation/` | Cite the durable path |
| V13 | LOW | §11 price row | ADS-implied ordinary (₩1.06–1.13m) uses the 10 Nov 43–52% premium. The news desk reads the premium as **narrowed** since 6 Nov, so the inversion is circular. Disclosed as derived | Keep the label; widen to "≥ ₩1.06m" |
| V14 | LOW | §2.1 price path | Webull 5 Nov close **$656.39 (−17.5%)** vs 修大哥's **$669.51 (−15.81%)** (247wallst). Primary governs; the news file should note the conflict | Note in news file |

### 1e. Anti-anchoring, both ways

- **Not anchored in the arithmetic.** Every bridge step is disclosed and reproduces. The file self-corrects one bearish July lean (opex $13.5bn → $12.5bn, +) and one bullish one (terminal reinvestment, −). The value-driver terminal is the correct method; July's was not.
- **But the discretionary choices that were *not* re-opened all lean the same way:** the asymmetric rounding (V1), "same β and ERP as July" (V1), weights "unchanged from July" (V4), and the TV timing (V5). Each is small. Together, in the bullish direction (r 11%, SK-consistent 24% normalisation, TV timing): **PW ≈ $400–410** [auditor's estimate: 382 + 0.5 × 30.5 + 10.2]. Swap in late-peak for base and it's **≈$460–470**. MoS at $697.83: **−70% to −75%** (late-peak ≈ −50%). The 40%-MoS entry moves from $211 to **≈$240–280**.
- **The other direction holds too.** The fall from $850 to $700 is not treated as vindication (§2.2) ✓, and the $1,550 consensus is examined, not adopted (§6) ✓. **No anchoring to the price or to July's verdict is evident in the conclusion.** The anchoring is in which inputs were left untouched.

### 1f. Verdict — PASS WITH CORRECTIONS

Arithmetic is clean. Required before committee: **V1–V4** (rate band and rounding; the bull-case sentence conditioned; head-to-head on one basis, "1.5–2×"; weights shown as a $351–405 band). V5–V14 at next revision. **None of them overturns WAIT** (§7).

## 2. Market regime (Peterson)
_pending_

## 3. Technical (CEO for 老詹)
_pending_

## 4. News (修大哥) — extraordinary-claim verification
_pending_

## 5. CRO ruling
_pending_

## 6. Cross-desk consistency
_pending_

## 7. Does the MU WAIT verdict survive? Does the style tilt survive?
_pending_

## 8. Bias direction check and patterns for 床狗
_pending_

## Required fixes (summary)
_pending_

## NOT OBTAINED / not verified by this audit
_pending_
