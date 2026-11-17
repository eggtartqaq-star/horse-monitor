# Audit — MU vs SK hynix, market regime, tech vs defensives (2026-11-17)

**Auditor:** Ai 管理層 (Dept 9, AI Intelligence) · **Date:** 2026-11-17 (evening UTC) · **Status:** COMPLETE

**Under audit (full depth):**
1. `reports/equity/2026-11-17-mu-valuation-refresh-vs-skhy.md` (𢦀鳩仔)
2. `reports/macro/2026-11-17-market-regime-tech-vs-defensive.md` (Peterson)
3. `reports/technical/2026-11-17-mu-skhy-defensives-technical.md` (CEO for 老詹)
4. `reports/news/2026-11-17-mu-skhy-semis-staples-news.md` and `reports/news/2026-11-17-nvda-earnings.md` (修大哥)
5. `reports/risk/2026-11-17-mu-skhy-style-cro.md` (John). COMPLETE (v1) when re-read; all sections audited (§5)

No audited report or config file was edited.

**Checklist:** C1–C10 as in `reports/committee/2026-11-16-aapl-skhy-reentry-audit.md`, plus 床狗 patterns (f)–(j): (f) snippet numbers, (g) both drift models when σ > 50%, (h) one stock / one input, (i) underived triggers, (j) unbounded-horizon claims.

**Method / network.** No Bash: every computation is by hand and shown. Scripts read: `models/valuation/mu_val_nov.py`, `models/valuation/mu_vs_skhy.py`. Ten WebSearches run (results cited where used). No WebFetch attempted; no 403/DNS host retried. tradingkey.com appeared once in a result list and was not opened or used.

## 0. Verdict summary

| Report | Verdict | HIGH | MEDIUM | Key items |
|---|---|---|---|---|
| MU valuation refresh (𢦀鳩仔) | **PASS WITH CORRECTIONS** | 0 | 4 | Every figure reproduces by hand. 12% is the top of a 10.7–11.8% CAPM band, reached through an asymmetric round-up and a second ERP (4.75% vs AAPL's 4.41%). "Even the bull case is below the price" holds only at 12% (≈$673–692 at 11%). The head-to-head is not on one basis: MU ≈ 26.5× on SK's 24% rule, so 1.5–1.7× the ordinary, not 2×. Weights frozen since July despite Nvidia's memory commitments: PW should read $351–405 |
| Market regime (Peterson) | **PASS WITH CORRECTIONS** | 0 | 1 | Data reproduce against the CEO table. The 10y reconciliation is correct. "Bear steepening" is contradicted by its own numbers: the 2y rose 35bp and the 10y 28–30bp, so this is a **bear flattening**. That weakens the financials leg. Regime confidence is proportionate |
| Technical (CEO for 老詹) | **PASS WITH CORRECTIONS** | 0 | 1 | Rule (g) complied; six cells re-run and all reproduce. "Staples … a hedge to semis" rests on four months inside a rotation (C9). No 老詹 sign-off |
| News, pre-close (修大哥) | **PASS WITH CORRECTIONS** | 0 | 0 | Huang resignation corroborated. 5 Nov SOX settled at −12.25% (close). "Quota recycling" overstates the two-way finding. MU 5 Nov close conflicts with Webull |
| News, NVDA (修大哥) | **PASS WITH CORRECTIONS** | 0 | 1 | $115.8bn corroborated against the 8-K extraction. $130bn guide and $390bn commitments not found by my searches (index lag; not contradicted). **The SEC civil probe is labelled [FACT] on an unread, single-relay WSJ story; I found no report of it** |
| CRO ruling (John) | **PASS WITH CORRECTIONS** | 0 | 1 | All arithmetic reproduces. Consistent with `config/risk-limits.yaml` except two constructions tagged [C] (tail method; cluster as "one name"). The "continuous leak" mechanism for two-way conversion is wrong; the formula ruling is right. The 0.40-vs-0.50 conflict is genuine (§5c) |

**No FAIL and no HIGH-severity finding. The MU WAIT verdict survives (§7). The style tilt survives with one weakened leg (§7). On the bias check: yes, the firm's discretionary memory inputs lean bearish for the fourth document running. The verdicts are robust to removing that lean (§8).**

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
- SK hynix-consistent normalisation (`mu_vs_skhy.py` lines 36–38): CY26-equivalent EBIT 16.35 + 33.7 + 45.58 + 51.34 = **$147.0bn**; × 24% × 0.845 / 1.13 = **$26.4** ✓; FY26 EBIT $102.0bn → **$18.3** ✓.
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
| V5 | LOW–MED | `mu_val_nov.py` lines 37–38; §3 "Timing" | Explicit flows sit at mid-year (FY31 at t = 4.3), but the Gordon TV is discounted from t = 4.8, so the first terminal flow lands at t = 5.8, not 5.3. PV(TV) is understated by 1.12^0.5 − 1 = **5.8%**: base +$7, bear +$3, bull +$17, **PW +$8.5**. Methodological, bearish | Discount TV from t = 4.3, or disclose |
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
- **The other direction holds too.** The fall from $850 to $700 is not treated as vindication (§2.2) ✓, and the $1,550 consensus is examined, not adopted (§6) ✓. The valuation also uses β 1.4, not the 60-day 3.1 the technical desk measured; at 3.1 the rate would be ~20%. **No anchoring to the price or to July's verdict is evident in the conclusion.** The anchoring is in which inputs were left untouched.

### 1f. Verdict — PASS WITH CORRECTIONS

Arithmetic is clean. Required before committee: **V1–V4** (rate band and rounding; the bull-case sentence conditioned; head-to-head on one basis, "1.5–2×"; weights shown as a $351–405 band). V5–V14 at next revision. **None of them overturns WAIT** (§7).

## 2. Market regime (Peterson) — **PASS WITH CORRECTIONS**

### 2a. What reproduces (C1, C3)
- **Data table vs the CEO table** (as printed in the technical report §4): SPY, RSP, QQQ, XLK, SMH, NVDA, XLP, KO, PG, XLV, GLD and TLT agree on every shared column (1m / 3m / YTD / from-high) ✓. MU dd −42.7 / v20 103.3 / RSI 40.1 match the technical §2 ✓.
- Spreads: +5.4 / +6.3 / +20.1 / +27.8pt ✓. Earnings yields 1/29.2 = 3.42%, 1/26 = 3.85%, 1/18 = 5.56%, 1/19.4 = 5.15%, 1/39 = 2.56% ✓. Spreads vs 5.10–5.15%: −1.7 / −1.3 / +0.4 / ≈0 / −2.6pt ✓. PEG 29.2/11 = 2.65 ✓. 2y − funds top: 4.86 − 4.00 = 86bp ✓. AAPL 352.8/357.60 = −1.3% ✓. Probabilities sum: 60 + 25 + 15 = 100 ✓; 75 + 22 + <3 = 100 ✓.
- **10y reconciliation paragraph: correct** and now corroborated (see §1b). The "secondary, not primary-verified" label is the right strength ✓.
- **Falsifiers (rule i):** every level is derived on the page: 4.85% = 5–6 Nov level, DXY 101.5 = early-Nov low, KO/PG MA50 = last ÷ (1 + % above MA50), RSP MA200 from the table ✓.

### 2b. Findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| P1 | **MEDIUM** | Policy read ("2s10s ~+28bp … a **bear steepening**"); Style table, Financials row ("Bear-steepening curve") | **Contradicted by the report's own numbers.** Week to 13 Nov: 2y **+35bp** (4.51 → 4.86), 10y **+28–30bp** (4.86 → 5.14). 2s10s went from **+35bp (6 Nov) to +28bp (13 Nov)**: the curve **flattened** ~7bp. Short-end-led selling is a **bear flattening**, which is what hike repricing looks like. It weakens the "term premium, not growth" inference and one of the two legs of the financials overweight | Re-label "bear flattening, short-end led"; re-justify financials on positive slope + 5.6% nominal GDP only, or cut to "neutral / modest" |
| P2 | LOW–MED | Summary bullet 1; "Gold and long bonds falling together" | The "real-rate shock" signature rests on TLT **−0.4% 1m** (−1.6% 3m) and a 10y that is **flat over one month** (~5.15% on 19 Oct and on 13 Nov). The 1m staples-vs-semis gap (+20pt) cannot be a rate effect. The report half-says this (the staples bid is "flow, not a bond trade") ✓. But the Summary leads with the rate scare as the regime driver | Say "rate scare = last 2 weeks; the 1m rotation predates it" in the Summary |
| P3 | LOW | Hypothesis table, "TLT −3.1% 1w" | 1-week figure not in the data table, no source | Cite or drop |
| P4 | LOW | "RSP set its 52-week high on 5 Nov" | 5 Nov was the day the S&P fell **4.4%** (Trefis, valuation §2.1) and the Nasdaq-100 **6.36%** (this report). A 52-week **closing** high that day is implausible; an intraday high at the open is possible | State intraday or close; check the bar |
| P5 | LOW | B-table "5 Nov tech rout … semis ETF ~−10%" | The news desk carries SMH **−11.21%** / SOXX **−12.15%** / SOX **−12.25%** (247wallst, Reuters-attributed; see §4e) | Update |
| P6 | LOW | Dec-hike pricing "~80% as of 9 Nov … after CPI not obtained" | The same-day news file relays **~90% after CPI** (Equiti / The Edge). Cross-desk; both secondary | Cite the relay as secondary |
| P7 | LOW | CPI "released 10 Nov" | 修大哥 dates the CPI move "~12 Nov". Peterson's BLS archive URL (`cpi_11102026`) is the stronger source | News desk defers |

### 2c. Regime call, confidence and tilt logic (C9)
- **Confidence is proportionate.** It is 60% with named alternatives (25% mid-cycle wobble, 15% pre-recession), a self-written bear case against each tilt, and dated, numeric falsifiers. This is the best-structured report in today's set.
- **The tilt follows from the evidence, with one weakened leg** (P1, financials). Cash / equal-weight overweight rests on hike pricing and breadth data that reproduce. Staples "neutral, staged" rests on valuation (earnings yield −1.7pt vs the 10y) and RSI 74, both reproduced.
- **Post-NVDA status of the "AI unwind over" falsifier:** it needs three legs. Leg 1 (a strong NVDA guide) has **probably fired**: $130bn reported, which I could not verify, §4. Legs 2 (SMH reclaims MA50, ~17% away) and 3 (no MU guide cut ~16 Dec) are open. **Underweight semis stands** until Peterson re-reads it.

### 2d. Verdict — PASS WITH CORRECTIONS
P1 before committee; P2–P7 at next revision.

## 3. Technical (CEO for 老詹) — **PASS WITH CORRECTIONS**

### 3a. What reproduces (C1)
- MU: 50% retracement (192.37 + 1,254.61)/2 = **$723.5** ✓; 61.8%: 1,254.61 − 0.618 × 1,062.24 = **$598.2** ✓; worst drawdown on closes 656.39/1,213.37 − 1 = **−45.9%** ✓; ATR 59.18/719.02 = **8.2%** ✓; 719.02 vs MA200 767 → −6.3% (macro table −6.2) ✓.
- SKHY: 122.18/199.86 − 1 = **−38.9%** ✓. §5: MU 712.42/719.02 = −0.9% ✓; 827.58/737 = +12.3% (news) ✓.
- **Rule (g) complied. Both models shown in every cell.** Six cells re-run (S = 697.83; martingale P = N((b − μT)/σ√T) + (S/B)·N((b + μT)/σ√T), μ = −σ²/2):

| Cell | b = ln(B/S) | Zero log-drift | Zero price drift | File |
|---|---|---|---|---|
| $620, 1m @ 72% | −0.11826 | 2N(−0.569) = **56.9%** | 32.1% + 1.1255 × 25.1% = **60.3%** | 57 / 60 ✓ |
| $550, 1m @ 72% | −0.23807 | 2N(−1.145) = **25.2%** | — | 25 ✓ |
| $500, 3m @ 103% | −0.33337 | 2N(−0.647) = **51.7%** | 34.8% + 1.3957 × 18.3% = **60.3%** | 52 / 60 ✓ |
| $400, 6m @ 72% | −0.55652 | 2N(−1.093) = **27.4%** | 20.1% + 1.7446 × 8.9% = **35.6%** | 27 / 36 ✓ |

- **Rule (j):** no unbounded-horizon claim found ✓. "A further 20% fall within a quarter is about a coin flip on either model" holds at 60-day vol (51–57% for −21%). At 20-day vol it is 64–72%, so "coin flip" understates it (LOW).

### 3b. Findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| T1 | **MEDIUM** | §1 "Staples move against memory (−0.4 to −0.5). **That makes them a hedge to semis**" | The correlations are measured over 15 Jul–16 Nov, a window that contains what 修大哥 calls the **largest tech-to-staples rotation since 2001**. A correlation measured inside a rotation **is** the rotation. Peterson and 修大哥 both describe staples as **rate-exposed**, and in a rate shock both legs can fall together. The conclusion is stronger than four months of one regime can support (C9). **Mitigated downstream:** the CRO explicitly grants "no hedge credit for staples" (CRO §4.1 caveat 1) | "Over this rotation (15 Jul–16 Nov) staples moved against memory. Whether that holds in a rate shock is untested; a longer window is NOT OBTAINED" |
| T2 | LOW | §2 "From the high −42.7% (close)" | 719.02 vs the **intraday** high $1,254.61. From the ATH **close** $1,213.37 it is **−40.7%** | Label the basis |
| T3 | LOW | §3 "now **below** the Bollinger lower band area (%b 0.10)" | %b 0.10 means **above** the lower band (0 = on it) | "near the lower band" |
| T4 | LOW | §3 vs §5 | New low $117.41 (§3) vs $117.40 (§5); 9 Sep high $199.86 vs news $199.87 | One print each |
| T5 | LOW | §2 levels table | July FV **$266** "being refreshed today". It is superseded by base $314 / PW $351 (propagation) | Update |
| T6 | LOW | §1 "MU's 60-day beta to SPY is 3.1" | Labelled short-window ✓. The valuation uses **β 1.4** in CAPM and doesn't mention 3.1 (pattern h). Here the generous figure sits in the valuation, so this is not desk-convenient bias | One line in the valuation |
| T7 | PROCESS | header | No 老詹 sign-off, so `stop_required` ("老詹's invalidation level") is unmet for any memory entry. The CRO says so (§1.2 ground 4) | 老詹 sign-off |

**Not in this report:** the brief says the 5 Nov "SOXX −12.15%, SMH −11.21%" are Webull bars in the technical report. **They are not.** Those figures appear only in 修大哥's pre-close file (line 48), sourced to 247wallst. The technical report has no 5 Nov ETF bar. See §4e.

### 3c. Verdict — PASS WITH CORRECTIONS
Statistics and the full both-model probability table reproduce. T1 before committee; T2–T6 at next revision.

## 4. News (修大哥) — extraordinary-claim verification

### 4a. Huang resignation (11–12 Nov) and Kress as interim CEO — **CORROBORATED (secondary, many outlets)**
My search returned SF Standard (12 Nov), wccftech, iconnect007, americanbazaar (12 Nov), YourStory, Keengamer and others. All report Huang resigning as president, CEO and director, effective immediately; CFO Colette Kress as interim CEO while staying CFO; and Harvey C. Jones named the board's first chair. Announced Thursday 12 Nov ([SF Standard](https://sfstandard.com/2026/11/12/nvidia-ceo-jensen-huang-resigns/), [wccftech](https://wccftech.com/jensen-huang-resigns-nvidia-ceo-colette-kress-interim/), [American Bazaar](https://americanbazaaronline.com/2026/11/12/nvidia-names-kress-interim-ceo-after-jensen-huang-resigns-492157/)). The board probe opened 8–9 Nov (Dow Jones via [Morningstar 9 Nov](https://www.morningstar.com/news/dow-jones/202611092210/nvidia-shares-drop-as-board-launches-probe-2nd-update)) ✓. "11–12 Nov" (8-K dated 11 Nov, public 12 Nov) is consistent. The reason is contradictory across outlets, and the file reports that without resolving it ✓. No primary Nvidia newsroom page was read (DNS, per the file).

### 4b. SEC civil probe — **NOT CORROBORATED; label too strong (MEDIUM, `nvda-earnings.md` Bottom line item 3, §4.5, §5.2, §6 item 9)**
Two searches found **no** report of an SEC probe. They did find a Semafor report of **DOJ** probes (antitrust) that could reach Nvidia, and former SEC chair Gensler saying the key question in the *board* probe is "whether Huang misled shareholders" ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/gary-gensler-says-key-question-in-nvidia-probe-is-whether-huang-misled-shareholders-sees-ai-repricing-ahead/cNGrO6sR9ev), [Newsquawk/Semafor](https://www.newsquawk.com/headlines/multiple-us-doj-probes-threaten-to-sweep-up-nvidia-nvda-reports-semafor-citing-two-admin-officials)). The file's "disclosures misled investors" focus matches Gensler's framing closely enough that conflation in a relay is possible. The item may simply be too new for the index (Axios URL dated 17 Nov). But the file labels it **[FACT]** on a WSJ story **it did not read**, relayed by Axios and an aggregator. The CRO has already used it in MU's event component. **Correction:** relabel "[REPORTED — WSJ via Axios, single relay, unverified]"; the CRO tags it the same way. (The CRO's own NOT OBTAINED #12 already says "not read directly" ✓.)

### 4c. NVDA FQ3 FY27 $115.8bn; FQ4 guide $130bn; supply commitments $390bn — **revenue CORROBORATED; guide and commitments NOT VERIFIED by this audit**
- **$115.8bn: corroborated.** A search extraction of the SEC 8-K exhibit (`q3fy27pr.htm`) gives GAAP revenue $115.8bn, +20% QoQ, +103% YoY, net income $65.3bn, diluted EPS $2.70, GM 74.8%, quarter ended 25 Oct 2026 ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000088/q3fy27pr.htm)) ✓. Internal checks: 115.8/96.2 = +20.4% ✓; DC 107.6/89 (Q2 DC, search) = +20.9% ✓; hyperscale 60.1 + other 47.5 = 107.6 ✓; + edge 8.2 = 115.8 ✓; beat over the top of the guide 115.8 − 110.16 = $5.6bn ✓; FQ4 guide vs LSEG 130/125.25 = +3.8% ✓; inventory 39.7/31.6 = +26% ✓.
- **$130bn FQ4 guide and $390bn commitments: not found** in three searches. Results pre-date the release (a 12 Nov S&P preview; the Q2 commentary). **Not contradicted.** The file cites the SEC CFO-commentary exhibit URL and four relays. The Q2 base is confirmed: **$279bn, "primarily related to the procurement of memory"**, schedule **$92bn / $87bn / $88bn** for rest-of-FY27 / FY28 / FY29 ([Nasdaq](https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock)).
- **LOW (§2.1):** the Q2 wording has no "multi-year"; the Q3 quote adds it. The FY28 bucket would jump **$87bn → $203bn** in one quarter (2.3×) while the total rises $111bn. That is plausible, but it is the single most memory-relevant number in the file. Verify both against the exhibit before the committee leans on it.

### 4d. SK hynix ADS↔ordinary conversion: one-way or two-way? — **RULING: two-way since 29 Jul within the cap is the better-sourced statement; the economic premise ("the premium can't be arbitraged while the cap is exhausted") stands; current implementation status UNRESOLVED**
- **On disk, the firm already had it.** `reports/news/2026-11-11-skhy-regulatory.md` line 229: "**One-way until 29 Jul 2026** … KSD said **two-way conversion from 29 Jul 2026**" (Korea Times 14 Jul; iTiger); line 289: "two-way conversion since 29 Jul 2026". Line 24 of the same file says "one-way conversion only **until 29 Jul**".
- **The qualifier was dropped in synthesis**: the 12 Nov CEO synthesis (line 33, "one-way conversion only"), then the 12 Nov SKHY valuation (line 163), the 12 Nov CRO review (line 71), `config/watchlist.yaml` line 67 ("Four desks converged independently") and today's MU valuation line 350. **This is a repeat of pattern (b)**: an epistemic qualifier lost in synthesis. The "four desks" did not converge independently; three copied a truncated phrase.
- **My search:** KSD said it would accept conversion applications **in both directions from 29 Jul**. The depositary (Citi) had not then announced a timetable. **Because the 2.5% quota was exhausted by the 10 Jul issuance, outlets judged the reopening "may do little" unless SK hynix expands the ADR programme** (search summary of edaily / mt.co.kr / iTiger / Mitrade, 21–29 Jul) ([iTiger](https://www.itiger.com/news/2654305994), [mt.co.kr](https://www.mt.co.kr/en/stock/2026/07/28/2026072817304086600), [edaily](https://en.edaily.co.kr/news/eda202607295683/)). Whether 29 Jul was implemented: **not verified** (all sources pre-date it).
- **Economic ruling.** At the cap, ordinary → ADS needs headroom, and headroom appears only when an ADS holder cancels into ordinaries. While the ADS trades at a premium, a rational holder sells the ADS rather than cancelling it, so headroom is not created and **ADS supply stays fixed**. Even if a cancellation is refilled, total ADS outstanding is unchanged. So "two-way within an exhausted cap" and "one-way" produce the **same premium dynamics**. The only premium-relevant event is still a **cap increase**. 修大哥's "the quota is not frozen, it is **recycling**" overstates it: it is legally two-way and economically dormant while the premium persists (LOW–MED, pre-close §3.2 and Bottom line item 3).
- **Disposition:** the watchlist line and the valuations should read "two-way since 29 Jul (KSD, July reports) within an exhausted 2.5% cap; inbound conversion effectively closed while the premium persists". Implementation and current ADS count NOT OBTAINED (The dictator). The CRO's UNVERIFIED label (H-3) is the right strength; its "contradicts the four-desk finding" framing is not (see R1).

### 4e. 5 Nov SOX fall (−12.25% / −7.1% / −3.1%) — **RULING: −12.25% on the close (secondary, Reuters-attributed)**
My search: "PHLX Semiconductor Index fell **12.25%** … closing at **9,011.14**, second-largest one-day decline on record, largest since 16 Mar 2020" (247wallst citing Reuters; AlphaMaven syndication). **Intraday** prints were −9.2% at 2:21 p.m. ET (Stocktwits) and "~9% after briefly exceeding 11%" (Grafa). That explains the smaller figures as **pre-close prints** ([247wallst](https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/), [Stocktwits](https://stocktwits.com/news-articles/markets/equity/soxx-etf-semiconductor-is-set-for-its-worst-week-in-over-18-months/cNG1sEhR94Z), [Grafa](https://grafa.com/en/news/united-states/us-semiconductor-stocks-selloff-ai-trade-unwind-november-2026)). The −3.1% (Motley Fool) and −7.1% (Finimize) have no support for the close. It is consistent with Webull's MU −17.5% that day. **The SMH −11.21% / SOXX −12.15% figures are 247wallst's, not Webull bars** (§3b note). Dept 5 should still print the Webull 5 Nov SMH/SOXX bars to close it on primary data.

### 4f. Other news findings

| # | Severity | File / location | Finding | Correction |
|---|---|---|---|---|
| N1 | LOW | pre-close §2.2, 5 Nov | MU "−15.81% to $669.51" (247wallst) conflicts with Webull **$656.39 / −17.5%**; not flagged | Add to the contradiction list; primary governs |
| N2 | LOW | pre-close §1.2 | October CPI dated "~12 Nov"; Peterson cites the BLS archive for **10 Nov** | Defer to macro |
| N3 | credit | NVDA §4.8 / Bottom line item 4 | The pre-close "no November export-control action" was self-corrected the same evening, with sources ✓ | — |
| N4 | credit | NVDA §5.4, §7 | Scores (MU 50, SKHY 40, KO 45) move by less than the pre-specified +10–15, with the reason stated (HBM commentary not obtained) ✓. Pre-registration honoured | — |

### 4g. Verdicts
- **Pre-close news: PASS WITH CORRECTIONS** (4d "recycling" wording; N1; N2). Contradictions are reported, not hidden ✓. tradingkey not used ✓.
- **NVDA earnings: PASS WITH CORRECTIONS** (4b SEC-probe label, **MEDIUM**; 4c verify the FY28 bucket). Results headline corroborated against the 8-K extraction.

## 5. CRO ruling (John) — `reports/risk/2026-11-17-mu-skhy-style-cro.md` — **PASS WITH CORRECTIONS**

First read at "IN PROGRESS (§0–3)". Re-read after the CEO's notice at **COMPLETE (v1)**. §0–3 were unchanged between reads (Grep on the flagged phrases); §4–8 were audited on the second read.

### 5a. Arithmetic (C1) — reproduces
- Score 0.30 × 90 + 0.15 × 20 + 0.20 × 5 + 0.10 × 25 + 0.10 × 30 + 0.15 × 35 = **41.75** ✓. ADS 25.4 ✓; ordinary 40.25 ✓.
- Ground 1: 737/351 = **2.10×** ✓; 737/606 = **1.22×** ✓; 1 − 351/737 = **52.4%** ✓; 1 − 168/737 = **77.2%** ✓.
- §1.4 tail table: 650 × 0.825 = **536.25** ✓; from 712.42 → 24.73% → **4.04%** ✓ (file 4.0%); from 737 → 27.24% → **3.67%** (file "3.6%", rounded down, conservative); 598 × 0.825 = 493.35 → 3.25% ✓ / 3.02% ✓. Held-through 1.91% / 1.30% ✓. VaR 103%/√252 × 1.645 = **10.7%** → 0.43% of LNW ✓. T-path at $830: 4.21 / 3.93 / 3.29 / 2.83% ✓.
- **CEO spot-check note:** the coordinator's "712/650 → 4.07%, 737/650 → 3.64%" do not reproduce exactly. By hand: 1 ÷ (1 − 536.25/712) = **4.05%**; 1 ÷ (1 − 536.25/737) = **3.67%**. The file's 4.0% / 3.6% stand; the differences are immaterial.
- §2: 122.61/102.40 = 1.197 ✓; /80.45 = 1.524 ✓; 1.25m/1.07m = 1.168 ✓; premium illustration **30.5%** ✓; 1 ÷ (1 − 1/1.30) = **4.33%** ✓. R2 = 0.8 × 1,070,000 = **₩856,000** ✓. **Yesterday's S4/R2 (underived ₩850,000) is fixed (rule i, credit).**
- §3: 0.88² = 0.774 ✓; 2.0% × 24.7% = 0.49% ✓; 0.51/0.20 = 2.5% ✓.
- §4.4 AI band (**rule i: derived ✓**): SMH v20 67.3%/√252 = 4.24% × 1.645 = **6.97%**; 1.5%/7.0% = **21% → 20%** ✓; 40% × 7.0% = 2.8% ✓; 31.2% × 20% = 6.2%, × 40% = 12.5% ✓. Info Tech 6.4 + 20 = 26.4 → 8.6pp headroom ✓. LNW thresholds 737/0.10 = $7,370, 737/0.04 = $18,425 ✓.
- §4.2: PG 154.2 × 1.122 = **$173.0** ✓; KO 91.0/98.79 − 1 = −7.9% ✓; PG −10.9% ✓; KO cap 1 ÷ (1 − 91.0 × 0.95/98.79) = **8.0%** ✓ (w = 5% labelled [A] ✓).
- §5 AVGO: 2 × 344.87 = 689.74 ✓; 12.06/689.74 = 1.75% ✓; 1/15% = 6.67% → 6.6% ✓; 689.74/0.066 = $10,451 ✓; /0.10 = $6,897 ✓.
- §6 calendar: 17 Nov is a Tuesday, so 19 Nov Thu, 25 Nov Wed, 3 Dec Thu, 4 Dec Fri, 9 Dec Wed, 10 Dec Thu, 15 Dec Tue, 16 Dec Wed ✓. The MU date conflict (15 vs 16 Dec) is flagged ✓.
- §7 #8: 4% × (1 − 351/712.42) = **2.03%** ✓; 4% × (1 − 168/712.42) = **3.06%** ✓.

### 5b. Consistency with `config/risk-limits.yaml` (and `config/portfolio.yaml`)

| Limit [config] | CRO use | Finding |
|---|---|---|
| `max_risk_per_trade: 0.01 # size x distance to stop` | Tail method ("size × tail loss") | **A CRO construction, stricter than the config text.** §7 #9 now shows both bases and §8.3(c) proposes formalising it (partial credit). But §1.5's table still tags "Size × tail loss" as **[C]**. Yesterday's R1 is not fully propagated (**LOW–MED**) |
| `max_single_position: 0.10 # per name` | Applied to the **sum** MU + SKHY + 000660 (§3.1, C-1) | A veto-authority reading, not the config text. Label it a CRO construction (LOW) |
| `max_correlated_cluster: 0.40` | Hard 40%; CRO band 20%; Tier A/B definition "binding until the Owner amends" | Consistent. The band is derived; the "half the VaR ceiling" choice is a judgement and should carry [A] (LOW). Tier B at 100% with no measured correlation is labelled conservative ✓ |
| `max_sector: 0.35` | Info Tech; staples; healthcare ≤ 35% ✓ | ✓ (see 5c on the targets conflict) |
| `cash_floor: 0.10` | Hard 10%; CRO band ≥ 30% (= `portfolio.yaml` target); T-bills-as-cash flagged as an interpretation ✓ | ✓ |
| `leverage: none` | AVGO margin debit = breach on its face; no de-minimis; cure by 3 Dec; margin to be disabled ("structural, not behavioural", CLAUDE.md rule 1) ✓ | ✓ |
| `max_var_95_1d: 0.03` | Name-level VaR shown; cluster band derived from it ✓ | ✓ |
| `stop_required`, `committee_approval_required`, `decision_record_before_ticket`, `naked_short_options: forbidden`, `covered_only`, `live_trading: forbidden` | All applied as written; no "trading" carve-out invented; cash-secured puts barred as a back-door entry ✓ | ✓ |
| `max_adv_participation: 0.05` | "PASS on inference", Tim Cook not run ✓ | ✓ |

### 5c. The "0.40 vs 0.50" cluster conflict — **genuine; correctly escalated, not resolved silently; one more conflict missed**
- `config/portfolio.yaml` targets: `ai: 0.30` + `technology: 0.20` = **0.50**. `config/risk-limits.yaml`: `max_correlated_cluster: 0.40 # e.g. total AI-complex exposure across sleeves`. If the `technology` sleeve holds AI-complex names, the targets **cannot be met inside the hard limit**. ✓ The CRO's reading is correct.
- **Precedence:** `risk-limits.yaml` holds the *hard* limits and says they "change only with the Owner's explicit approval". `portfolio.yaml` targets are "proposed by Morris, approved by the Owner". When they conflict, the hard limit binds and the target is infeasible. The CRO does exactly this (hard 40%, band 20%) and leaves the fix to the Owner ✓. It does **not** bind today because holdings are unknown and the CRO band is 20%.
- **Missed by the CRO (LOW–MED):** the same 0.50 also exceeds **`max_sector: 0.35`** if the `ai` + `technology` sleeves are mostly GICS Information Technology. Part of Tier B (GOOGL, META, AMZN) sits in other GICS sectors, so this is a *potential*, not certain, conflict. It belongs in the same Owner ruling. And `portfolio.yaml` labels `cash: 0.30` a "strategic cash **floor** — see risk-limits.yaml", while risk-limits sets `cash_floor: 0.10`. The CRO treats 30% as a target and 10% as the floor, which is the sensible reading, but the label conflict should go to the Owner too.
- "Tenth time of asking" is the CRO's count; not verified here.

### 5d. Findings

| # | Severity | Location | Finding | Correction |
|---|---|---|---|---|
| R1 | **MEDIUM** | §2.3 "continuous leak"; §2.4 ADS instrument 5 → 8 | **The mechanism is wrong.** A cancellation into ordinaries removes one ADS, and the refill adds one back, so **ADS outstanding is unchanged**. With the cap exhausted, recycling cannot add net ADS supply. While the ADS trades at a premium, rational holders sell rather than cancel. So "two-way within the cap" does **not** make compression a "live, unannounced" flow risk (§4d). The formula ruling (unchanged, mechanism-agnostic) is **right**. The narrative that it "strengthens" three rules, and the +3 instrument score, don't follow. **Numerically immaterial** (+0.9 to the ADS score), but it is Owner-facing reasoning (C9) | Delete the leak argument; keep "formula unchanged; status UNVERIFIED"; H-3 annotation as in §4d |
| R2 | LOW–MED | §1.2 ground 1 ("Price above the bull case", "sufficient alone"); §0 paragraph; §3.3 | Inherits V2. Against the **close** ($712.42) and an 11% bull case (≈$673–692), the price is **≈1.03–1.06×** the bull case, not 1.15–1.22×. Ground 1 survives, narrowly. Ground 2 and the process grounds are independent | "At or above the bull case (1.03–1.22× depending on r and print)" |
| R3 | LOW–MED | §1.4 "naive cap is **2.4–3× too large at every row**" | Rows 3–4: 6.2/3.2 = **1.9×**, 5.3/3.0 = **1.8×**. False for the $598 rows (C4) | "1.8–2.9×" |
| R4 | LOW–MED | §1.5 table, `max_risk_per_trade` row | Tail method tagged [C] (5b) | "[CRO construction; config text = distance to stop; §8.3(c) proposed]" |
| R5 | LOW | §1.3 event component; §2.1; §2.4 | SEC civil probe used as fact (inherits 4b); NOT OBTAINED #12 is correctly hedged | Tag "unverified" in the score notes |
| R6 | LOW | §1.2 ground 2, §1.3 "1.07 ATR" | (712.42 − 650)/59.18 = **1.05 ATR**; 1.07 mixes a 17 Nov distance with a 16 Nov ATR% | 1.05 |
| R7 | LOW | §3.2 | 5.0% derived with the 13.4% gap; the 16 Nov B-3 formula uses 13.7% (yesterday's R5, not propagated) | One gap figure |
| R8 | LOW | §3.3, §2 "~15–17× vs MU ~32×" | Inherits V3 (MU ≈ 26.5× on the SK basis) | Update when the valuation is fixed |
| R9 | LOW–MED | §4.5 / §8.2 item 3 | 0.40-vs-0.50 escalation correct; the `max_sector` 0.35 and "cash floor 0.30" label conflicts are not raised (5c) | Add both to the Owner ruling |
| R10 | LOW | §4.4 AI band | "Half the 3% VaR ceiling" is a judgement, and SMH vol understates a memory-heavy cluster (MU 103%) | Label [A]; note it is not conservative for a memory-heavy mix (the 5% memory sub-cap covers this) |

**Credit.** It refuses to invent a "trading" carve-out (§1.5). The T-path trigger ($827.58) is derived and the time-stop is labelled [A]. ₩856,000 replaces the underived ₩850,000. The illustration premium is ruled inadmissible for a ticket. The +4 score change is explained as a method artefact. **"No hedge credit for staples" (§4.1)** declines exactly the inference T1 flags. Staples get staging, a stop and a pipeline, not a veto, and "KO/PG/XLP have had no pipeline" is enforced as a process gate. Blackouts are dated and risk reduction is exempt (E-6).

### 5e. Verdict — PASS WITH CORRECTIONS
R1 before committee; R2–R10 at next revision. Consistent with `config/risk-limits.yaml` on every hard limit. The two stricter constructions should be labelled as such.

## 6. Cross-desk consistency

| Item | Desks and values | Ruling |
|---|---|---|
| **10y on 13 Nov** | Valuation 5.13–5.16% · Peterson 5.14–5.15% (5.10% 12 Nov) · 修大哥 5.14% | **Consistent**; corroborated by audit search (secondary). Yesterday's V2 closed |
| **ERP** | 𢦀鳩仔 AAPL 4.41% (16 Nov) vs MU 4.75% (17 Nov); Damodaran 4.14% (~1 Sep) | **Inconsistent (pattern h)**. One firm ERP needed in `knowledge/` |
| **MU beta** | Valuation 1.4 (CAPM) · technical / CRO 3.1 (60-day) | Different uses, both labelled. Not desk-convenient: the valuation took the lenient one. Record the long-run beta in `knowledge/` |
| **MU 5 Nov close** | Webull $656.39 (−17.5%) · 修大哥 $669.51 (−15.81%) | Primary governs; news to note |
| **5 Nov SOX / semis ETFs** | 修大哥 −12.25% / −7.1% / −3.1% (contradiction) · Peterson "~−10%" · technical none | **−12.25% close** (§4e); Peterson to update; Dept 5 to print Webull bars |
| **SK hynix conversion** | Regulatory 11 Nov "two-way from 29 Jul" · synthesis / valuation / CRO 12 Nov, watchlist, MU valuation 17 Nov "one-way" · 修大哥 17 Nov "two-way, recycling" · CRO 17 Nov "UNVERIFIED; contradicts four desks" | **Two-way within an exhausted cap; economically closed** (§4d). The "four-desk convergence" was one truncated phrase copied three times |
| **Dec hike odds** | Peterson ~80% (9 Nov) · 修大哥 ~90% (post-CPI relay) · CRO cites both ✓ | Both secondary; Peterson to cite the relay |
| **CPI release date** | Peterson 10 Nov (BLS archive URL) · 修大哥 "~12 Nov" | Peterson governs |
| **MU FQ1 date** | Valuation 15 Dec · Peterson / 修大哥 ~16 Dec (third-party) · CRO flags both ✓ | Unconfirmed; the blackout covers both |
| **MU vs ordinary multiple** | Valuation ~32× vs 15–17× → CRO "~2×" | ~26.5–31.7× → **1.5–2×** (V3) |
| **"Above the bull case"** | Valuation → CRO ground 1 | Rate-conditional (V2/R2) |
| **Staples as hedge** | Technical "a hedge to semis" · Peterson / 修大哥 "rate-exposed, flow-driven" · CRO "no hedge credit" | Technical overstates (T1); CRO and macro agree with each other |
| **Curve** | Peterson "bear steepening" · own data → flattening | P1 |
| **MU fair value in the technical** | $266 (July base) vs $314 / $351 today | Propagation (T5) |
| **SKHY low** | $117.41 vs $117.40 | Trivial (T4) |
| **NVDA print** | 修大哥 raises scores; CRO credits the cycle component; **valuation pre-dates the print** | The valuation should add a post-print note under V4 |
| **Quant** | Dept 3 filed nothing (provenance stamps on valuation and technical) | Coverage gap: no independent statistical check of the touch tables or correlations exists outside this audit |

## 7. Does the MU WAIT verdict survive? Does the style tilt survive?

**MU WAIT — SURVIVES.**
- Stack every correction in the bullish direction: r at 11% (CAPM band), SK-consistent normalisation (24% → $26.4), TV mid-year timing. PW ≈ **$400–410**. Replace base with the late-peak variant (the NVDA-commitments case) and it's ≈ **$460–470**. Against the $712.42 close (AH $737): **1.5–1.8× value; MoS −52% to −80%** against a 40% hurdle. On the file's own grid, no base or weighted cell reaches $700.
- What would overturn it: the late-peak harvest **and** r ≤ 10% **and** a bull weight well above 25%, or accepting the $1,550 premise (~$90 of permanent normalised EPS, ~4× base). No desk on disk argues either with evidence.
- **What does not survive as written:** "the price is above even the bull case". At an 11% CAPM rate the bull case is ≈ the price (V2/R2). WAIT rests on the weighted value, not the bull case, so the verdict stands; the rhetoric needs conditioning.
- **Independent of valuation:** the CRO veto (42/100) stands on stop geometry, calendar, process and the margin account. None of my findings touches those grounds.
- **Levels:** the "committee ≤ $350 / entry ≤ $210" levels are the most sensitive output. Under the corrections they move to roughly **≤ $400 / ≤ $240** (≤ $460 / ≤ $280 with late-peak) [auditor's estimate]. The committee should treat $210 as the conservative end of a $210–280 band, not a point.

**Style tilt — SURVIVES, with one weakened leg.**
- Cash/T-bills and equal-weight overweight: the supporting data reproduce (hike pricing, RSP vs QQQ, vol). Unaffected.
- Staples neutral / staged: survives; the CRO's "no hedge credit" removes reliance on T1.
- Financials "modest overweight": **weakened** by P1, since the curve is bear-flattening, not steepening. Neutral-to-modest is defensible.
- Underweight semis: stands. Of the three "AI unwind over" legs, one has probably fired (NVDA guide, unverified); two are open. Re-read after 18–20 Nov (CRO E-7) and MU's print.
- **Groupthink check:** macro, technical, news and risk all land on "cash, don't chase either side". Dissent exists inside reports (Peterson's three bear cases against himself; the valuation's §6 steel-man; 修大哥's "more than a sentiment bounce"). **No desk owns the opposite case.** As yesterday, I recommend the committee assign one: the "late-peak + NVDA commitments" case for memory, and the "staples keep working in a growth scare" case.

## 8. Bias direction check and patterns for 床狗

**Is the firm systematically bearish on memory?** **Yes, in discretionary inputs. No, in verdicts.**
- **Record.** 12 Nov SKHY synthesis: 10 inferences hardened bearish (13 Nov audit). 16 Nov SKHY re-entry: S1–S5 all bearish (16 Nov audit §8). Today's MU valuation: every input **not** re-opened leans bearish. That's asymmetric rounding (V1), the higher of two ERPs (V1), frozen weights (V4), TV timing (V5), the 20%-not-24% normalisation in the head-to-head (V3), and a base FY27 GM below the guided floor (V9). Today's CRO: the "continuous leak" (R1) hardens a neutral fact against SKHY. 修大哥: the SEC probe as [FACT] (4b). **That is the fourth consecutive memory document with one-directional discretionary choices.**
- **Size.** Today the stack is worth ≈ +$50–60 on PW (≈15%), or ≈ +$110–120 (≈30%) with late-peak, against a price gap of ≥ 75%. In each of the four documents the verdict was robust to removing the lean. That is why none fails.
- **Counter-evidence (credit).** The valuation raises FV for the second time against a falling price, uses β 1.4 not 3.1, self-corrects a bearish July opex lean, and refuses to call the price fall vindication. The technical complies with rule (g) and states no unbounded claim. 修大哥's NVDA read is two-sided and raised scores. On price, the firm's July caution ($850 → $712) has so far been right, though the valuation says honestly that fundamentals moved the other way.
- **Narrative lock-in risk.** The same framing ("peak multiple on peak earnings"; "memory = one trade, wait") now runs through valuation, CRO, macro and news. New bullish data (the Q2 $279bn commitments, public since August) entered the valuation's weights **nowhere**. That is the signature of lock-in, not of error.
- **Recommendation.** Before the committee votes, (1) the valuation publishes its "bullish-corrections stack" (§1e) alongside the base; (2) one desk (Elon Musk or Dept 3) steel-mans the late-peak case using Nvidia's verified commitment schedule; (3) the committee records the levels as a band ($210–280), not a point.

**Recurring patterns for 床狗 (prompt fixes):**
- **(b) recurrence, now severe: dropped qualifiers.** "One-way **until 29 Jul**" became "one-way" and was copied into four documents and the watchlist as an "independent convergence". Rule: a synthesis may not shorten a dated qualifier. "Independent" may be claimed only when sources are traced and differ.
- **(h) recurrence: one input, one value.** ERP 4.41 / 4.75; β 1.4 / 3.1. Record ERP, rf (with date) and long-run beta per name in `knowledge/`.
- **(k) new: rounding direction.** Discount rates round to the nearest 0.5pt or carry the unrounded figure. Any directional rounding is disclosed with its value effect.
- **(l) new: carry-over defaults.** An input "unchanged from [prior report]" (weights, ERP, β) must be re-justified when dated evidence bearing on it has arrived since. Name that evidence.
- **(m) new: regime-window correlations.** A correlation measured inside a single regime episode (< 6 months, or a named rotation) cannot ground a "hedge" or "diversifier" claim without a longer window.
- **(n) new: [FACT] for unread relays.** A story the desk did not read, reaching it through one relay, is [REPORTED], never [FACT], whatever the outlet.
- **(g) partial compliance.** The technical complied fully. The valuation showed one model (the right one to show if only one) but omitted the second: rule (g) applies to every desk, not only Dept 5.

## Required fixes (summary)

| Report | Before committee / Owner | Next revision |
|---|---|---|
| MU valuation | **V1** (rate band, rounding, ERP), **V2** (bull-case sentence conditioned), **V3** (head-to-head on one basis, "1.5–2×"), **V4** (PW $351–405; weights re-examined post-NVDA) | V5–V14 |
| Macro | **P1** (bear flattening; financials rationale) | P2–P7 |
| Technical | **T1** (staples "hedge"); 老詹 sign-off (T7) | T2–T6 |
| News, pre-close | — | 4d "recycling" wording; N1; N2 |
| News, NVDA | **4b** (SEC probe → [REPORTED, unverified]) | 4c verify $390bn / $203bn and "multi-year" against the exhibit |
| CRO | **R1** (delete the "continuous leak") | R2–R10; add `max_sector` and cash-label conflicts to the Owner ruling |
| Watchlist / CIO | Annotate the SKHY conversion line per §4d (not by this auditor; no config edited) | — |
| Committee | Treat MU entry as a $210–280 band; assign a late-peak steel-man; treat the SEC probe as unverified | — |

## NOT OBTAINED / not verified by this audit

1. **NVDA FQ4 guide $130bn, supply commitments $390bn, the $203bn FY28 bucket and the "multi-year" wording.** Three searches did not surface the Q3 CFO commentary (index lag). Not contradicted.
2. **WSJ / SEC civil probe on Nvidia:** no report found in two searches.
3. **KSD two-way conversion: implementation after 29 Jul**, and current ADS outstanding (all sources found are dated 21–29 Jul).
4. **10y H.15 / DGS10 close for 13 Nov** (primary). Secondary corroboration only.
5. **Webull 5 Nov SMH / SOXX bars**: not in any report on disk.
6. **RSP 5 Nov bar** (P4); a 2s10s series from a primary source (P1 uses the report's own secondary figures).
7. **Damodaran ERP for November 2026** (yesterday's 4.14% is ~1 Sep).
8. MU historical peak-to-mid-cycle EPS ratios: not used numerically; the defensibility test in §1c relies on the file's own construction.

---
*Audit of argument, not conclusion. Every computation is shown inline. Research and decision support only — not financial advice. No agent of this firm places orders.*

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

**Coverage gap — no quantitative input.** Department 3 (Quant Research:
賭馬狗, Math King, Tom, AI指標) filed **nothing** on this name. Session
limits forced the pipeline down to a three-agent core and quant was cut
first, without being logged as a gap at the time. Any conclusion here
rests on fundamentals, valuation, news and technicals only.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
