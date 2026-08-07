# Valuation — Bloom Energy Corp (NYSE: BE)

**Analyst:** 𢦀鳩仔 (Dept. 2, Equity Research — Valuation)
**Reference date:** 2026-07-19 · **Price used:** **$214.96** (Fri 2026-07-17 close, verified by 巴爺爺)
**Inputs:** `reports/equity/2026-07-19-be-financials.md` (grade B–, 67/100) · `reports/equity/2026-07-19-be-moat.md` (NARROW, cyclically widening → erosion 2029-31) · `reports/news/2026-07-19-be.md` (68/100)
**Model file:** `/tmp/.../scratchpad/be_v2.py` (arithmetic reproduced inline below)

> **Health warning on this report.** My central fair value is **~87% below the market price** and **5–10x below the entire sell-side band ($193–$346)**. A number that far from consensus is either a genuine finding or a broken model. I have stress-tested it in §7 and stated exactly what would falsify it. Read §7 before acting on §1.

---

## 1. Headline

| Output | Value |
|---|---|
| **Intrinsic fair value range (DCF, scenario span)** | **$9 – $59 per share** |
| **Central (probability-weighted) fair value** | **$28.70** |
| **Most generous defensible construction** (relative value, §6) | **~$85** — reported as a ceiling, **not adopted** as fair value |
| **12-month target price (intrinsic)** | **$30** |
| **Margin of safety at $214.96** | **–649%** — the stock trades at **7.5x** central fair value |
| **菲比斯's 60% MoS met?** | **NO.** Requires ≤ **$11.48**. Price is **18.7x** that level. |
| **菲比斯's "bear returns ≥0%" rule met?** | **NO.** Requires ≤ **$8.66**. Price is **24.8x** that level. |
| **Valuation score (input to committee)** | **8 / 100** |
| **Recommendation** | **AVOID / DO NOT INITIATE.** Not a short recommendation (see §8). |

---

## 2. Housekeeping: two corrections to the desk's shared numbers

### 2.1 Enterprise value must be struck **fully diluted, if-converted** — and it is higher than the desk has been using

The $2.2–2.5bn 0% converts at a **$194.97 conversion price** are ~10% in the money. Conversion is the expected case. Under if-converted treatment the notes become equity and the cash proceeds stay on the balance sheet — so you cannot both count the $2.5bn as debt *and* count the shares.

```
Diluted equity value = 319.70m sh × $214.96      = $68.72bn
+ other recourse debt ($99m) + non-recourse ($4m) = $  0.10bn
– cash, equivalents & restricted (2026-03-31)     = $  2.52bn
                                                  ------------
Enterprise value (if-converted)                   = $66.31bn
```

菲比斯 used **$61.6bn** (basic shares, converts as debt). The correct figure is **$66.31bn — 7.6% higher.** Every implied-expectations number in his §6 should be scaled up by that factor. **EV/FY26E sales = 18.4x** (not 17x), on the $3.6bn guide midpoint; 19.5x on the low guide, 17.4x on the high.

### 2.2 The two related-party figures RECONCILE — and the reconciliation identifies the counterparty

巴爺爺 cites "$288m = 55.5% of Q3'25, SK ecoplant" [3P, Panabee]. 菲比斯 cites FY25 related-party $892.0m (44.1%), of which **$862.1m from Brookfield Fund JVs**, and Q4'25 $574.2m. These look contradictory. They are not:

```
Q3'25 related-party $288.0m + Q4'25 related-party $574.2m = $862.2m
Brookfield Fund-JV FY2025 total (菲比斯, from 10-K)        = $862.1m
                                                    difference = $0.1m
```

**An exact match to rounding.** The conclusion: the $288m in Q3'25 is **Brookfield Fund-JV revenue, not SK ecoplant.** The Brookfield JVs were formed in August 2025 — precisely the start of Q3'25's second month. Residual related-party revenue (SK ecoplant and others) for FY2025 is therefore only **$892.0m – $862.1m = $29.9m = 1.5% of revenue.**

**Why this matters for valuation, in both directions:**
- **Better than feared:** the SK ecoplant concentration story is essentially dead. SK is ~1.5% of revenue, not 55%. 巴爺爺's stated "grade decider" resolves *in Bloom's favour on the counterparty question*, and his conditional downgrade-to-45 trigger ("confirmation that related-party revenue exceeds 50% of a quarter") should be re-read as already-confirmed-but-for-a-different-reason.
- **Worse than feared:** **100% of the related-party concentration is the financing vehicle.** It went $2.8m (Q1'25) → $288m (Q3'25) → $574.2m (Q4'25) → $373.3m (Q1'26). Diversified related-party revenue across two industrial partners would be ordinary. A single co-owned fund vehicle accounting for 44% of FY25 and ~50% of Q1'26 revenue, with a $19.6m equity loss taken back on a $24.6m stake, is 菲比斯's "financing structure reported as demand" — and the reconciliation **strengthens** his reading rather than weakening it.

**Modelling consequence (§3, assumption R):** I do not capitalise Brookfield-JV revenue as recurring third-party demand at full value.

---

## 3. Assumptions table — the audit trail

Every number below is an input I chose, not an output I needed. Sources: [PR] = company release, [3P] = third party, [EST] = my estimate.

| # | Assumption | Bear (25%) | Base (45%) | Bull (30%) | Basis |
|---|---|---|---|---|---|
| A | FY2026 revenue | $3.40bn | $3.60bn | $3.80bn | Company guide $3.4–3.8bn [PR] — low/mid/high |
| B | FY2030 revenue | $3.30bn | $7.50bn | $12.00bn | See D, R |
| C | FY2035 revenue | $3.33bn | $8.14bn | $17.30bn | Post-window path |
| D | Implied 2030 shipments | ~1.3 GW/yr | ~2.9 GW/yr | ~4.7 GW/yr | At $2.57bn revenue/GW (=$3.6bn ÷ 1.4GW FY26E, product + attached service) [EST] |
| E | Announced capacity | 2 GW/yr by end-2026; 5 GW/yr ambition [3P] | — | — | Fremont 1→2GW for ~$100m [3P] |
| F | Peak GAAP operating margin | 8.5% (2026-27) | 14.0% (2029) | 18.5% (2030) | Q1'26 actual GAAP op margin 9.6% [PR]; GAAP **includes SBC** — see G |
| G | SBC treatment | **Expensed, not added back.** All margins are GAAP. Non-GAAP EPS guide ($1.85–2.25) is **halved** for cross-checks | — | — | SBC ~$139m FY25 [3P] = 6.9% of revenue, > FY25 operating income |
| H | **Terminal** GAAP operating margin (post-2031) | 5.0% | 10.0% | 16.0% | 菲比斯 erosion call: turbine slots free 2029/30, product GM compresses; service annuity (20% GM, $14bn backlog) is the floor |
| I | Terminal growth (g) | 1.5% | 2.5% | 3.0% | ≤ nominal GDP |
| J | WACC | 12.5% | 11.0% | 9.5% | 菲比斯 estimates 10–12%; high-beta, 0%-coupon quasi-equity capital structure, near-zero cash tax. Sensitised 8–14% in §5 |
| K | Cash tax rate | 2% → 21% | 2% → 23% | 2% → 23% | ~$4.0bn NOL (accumulated deficit) shields to ~2029; post-2017 NOLs capped at 80% of taxable income |
| L | Capex, forecast years | 5.5% of revenue | 5.0% | 5.0% | FY26 guide $150–200m on $3.4–3.8bn = 4–5% [3P] |
| M | **Terminal** capex | D&A (3.0%) + g/asset-turns | same | same | **Correction made mid-model:** a ~flat business does not need permanent growth capex. Asset turns 4.0x (asset-light per company's own $100m-per-GW claim). Terminal capex = 3.4–3.8% of revenue |
| N | D&A | 3.0% of revenue | 3.0% | 3.0% | [EST] consistent with L/M |
| O | Working capital | 10% of Δrevenue | 8% | 8% | Low, reflecting customer deposits/deferred revenue. **Generous to the bull** — it assumes the FY25 working-capital tailwind persists |
| P | Share count (start) | 325m | 325m | 325m | Q1'26 diluted **319.7m** [PR] + ~5m further option/convert creep. **Converts already inside this number** (12.8m sh at $2.5bn ÷ $194.97) |
| Q | Ongoing dilution | 3.0%/yr | 3.0% | 3.0% | Model share count = **377m** (10-yr midpoint). **Generous to the bull:** actual 5-yr basic dilution was **10.5% CAGR** (173m → 284.4m) |
| R | Related-party (Brookfield-JV) revenue | Treated as a **bridge**: rolls off from ~50% to ~15% of revenue by 2029 and is **not replaced** | Rolls to ~20% by 2029, **half replaced** by third-party demand | Converts fully to arm's-length demand; JVs are genuine incremental capacity | §2.2. Not capitalised at full value in bear/base |
| S | Electrolyzers / hydrogen | $0 | $0 | $0 | 修大哥: "treat as zero in the base case"; 45V sunset pulled to a Jan-1-2028 construction start |
| T | Scandium / FEOC risk | Caps shipments at ~1.3GW | Caps at ~3GW | Not binding | Hunterbrook: ~220t Sc₂O₃ needed for 5GW vs ~240t global supply [3P, disputed by 8-K]. **Bloom denied *China dependence*, not the *scale arithmetic*** |
| U | Brookfield "$25bn" | $0 direct value | $0 direct value | $0 direct value | It is a **financing framework, not backlog** (修大哥, 巴爺爺 red flag #8). Its value shows up as *customers being able to fund purchases*, which is already inside the revenue path |
| V | FY2025 OCF dispute | Sheephill ($114m) assumed right | Split the difference | Company ($418.1m) assumed right | Unresolved. Affects the 2026 starting FCF only, **not** intrinsic value materially (<$1/sh) — noted so the committee does not over-weight it |

**Assumptions I deliberately made generous to the bull:** Q (3% dilution vs 10.5% actual), O (permanent working-capital benefit), U (no charge for the JV equity-loss drag), M (terminal capex correction, worth +$2/sh), and using the guide midpoint rather than haircutting a company whose GM guide 巴爺爺 flags as the likeliest miss.

---

## 4. Bear / Base / Bull

Revenue in $m; margins are GAAP operating margins (SBC expensed).

### BEAR — 25%. "The bridge is demolished when the road opens."
Related-party revenue is a financing bridge that rolls off and is not replaced; AI capex digests; GEV/Siemens/Mitsubishi capacity unclogs from 2028-30; Bloom terminal-values as a specialty genset OEM (菲比斯 §4.1).

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2035 |
|---|---|---|---|---|---|---|---|
| Revenue | 3,400 | 3,900 | 4,100 | 3,800 | 3,300 | 3,000 | 3,330 |
| Op margin | 8.5% | 8.5% | 7.0% | 4.5% | 2.0% | 1.0% | 5.0% |

WACC 12.5%, g 1.5%, terminal margin 5.0% → **EV $0.85bn · equity $3.26bn · $8.66/share**
Note: of that $3.26bn, **$2.42bn is net cash** — the bear case values the operating business at ~$0.8bn, i.e. ~0.25x terminal sales. That is what a business with a 25-year record of sub-cost-of-capital returns is worth once the window shuts.

### BASE — 45%. "Real business, real window, real erosion."
Bloom hits ~3GW/yr, wins genuine third-party share, margins peak ~14% in 2029, then compress as turbines free up; the $14bn service backlog becomes the durable annuity.

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2035 |
|---|---|---|---|---|---|---|---|
| Revenue | 3,600 | 4,900 | 6,100 | 7,000 | 7,500 | 7,300 | 8,140 |
| Op margin | 9.6% | 11.5% | 13.0% | 14.0% | 13.5% | 11.0% | 10.0% |

WACC 11.0%, g 2.5%, terminal margin 10.0% → **EV $5.08bn · equity $7.50bn · $19.89/share**
Terminal value = 47% of EV; implied terminal multiple 8.1x EV/EBIT; implied **1.4x EV/FY26 sales**.

### BULL — 30%. Steel-manned.
This is the genuine bull, not a straw man. Take it seriously: **+130% y/y growth, a 90-day deployment against 4–8 year interconnection queues, a $6bn product backlog up 2.5x, a $14bn contracted service annuity, Oracle 2.8GW / 1.2GW contracted, AEP $2.65bn / 20-year, Morgan Stanley underwriting tax equity with real money, a $25bn Brookfield facility removing the customer's financing constraint, net-debt-zero with a 0% coupon and no maturity to Nov 2030, and a competitive set that is *quitting* (FuelCell exited SOFC with a $64.5m impairment; Doosan runs 50MW/yr = 2.5% of Bloom).** In this branch Bloom scales to ~5GW/yr, holds ~18% GAAP operating margins because it locks 15–20 year offtakes *before* the window closes, and the installed base becomes a genuine wide moat.

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2035 |
|---|---|---|---|---|---|---|---|
| Revenue | 3,800 | 5,600 | 7,800 | 10,000 | 12,000 | 13,500 | 17,300 |
| Op margin | 10.5% | 14.0% | 16.5% | 18.0% | 18.5% | 18.0% | 16.5% |

WACC 9.5%, g 3.0%, terminal margin 16.0% → **EV $19.68bn · equity $22.10bn · $58.61/share**

**This is the critical result of the whole report.** A scenario in which Bloom grows revenue **4.8x by 2035**, reaches its full **5GW ambition**, **triples** its operating margin, **defeats the turbine normalisation**, and is discounted at a **9.5%** rate — is worth **$58.61**. That is **–73% from $214.96.** The bull case does not get you to the price. It does not get you halfway to the price. It does not get you a third of the way.

### Probability weighting

```
0.25 × $8.66  =  $2.17
0.45 × $19.89 =  $8.95
0.30 × $58.61 = $17.58
                -------
Central fair value = $28.70
```

Weights follow 菲比斯's own recommendation (Wide 30% / Narrow-fading 45% / None 25%). I did not adjust them.

---

## 5. Sensitivity — the two most influential assumptions

**(a) WACC × terminal operating margin** (base-case revenue path). Value per share, $:

| WACC \ Terminal op margin | 6% | 8% | **10%** | 12% | 15% | 20% |
|---|---|---|---|---|---|---|
| 8.0% | 21.71 | 24.58 | 27.45 | 30.32 | 34.62 | 41.80 |
| 9.0% | 19.72 | 21.93 | 24.15 | 26.36 | 29.68 | 35.22 |
| 10.0% | 18.23 | 19.98 | 21.73 | 23.48 | 26.11 | 30.49 |
| **11.0%** | 17.06 | 18.47 | **19.89** | 21.30 | 23.42 | 26.95 |
| 12.5% | 15.71 | 16.76 | 17.81 | 18.86 | 20.44 | 23.06 |
| 14.0% | 14.69 | 15.49 | 16.29 | 17.08 | 18.28 | 20.28 |

Full range across this entire grid: **$14.69 – $41.80.** Nothing within ±3pp of any defensible WACC and ±10pp of any defensible terminal margin comes within **5x** of $214.96.

**(b) 2030 revenue level × terminal operating margin** (WACC 11%). Value per share, $:

| 2030 revenue \ margin | 6% | 8% | **10%** | 12% | 15% | 20% |
|---|---|---|---|---|---|---|
| $5.3bn (~2.1 GW) | 14.24 | 15.23 | 16.22 | 17.21 | 18.69 | 21.16 |
| **$7.5bn (~2.9 GW)** | 17.06 | 18.47 | **19.89** | 21.30 | 23.42 | 26.95 |
| $10.5bn (~4.1 GW) | 20.82 | 22.80 | 24.77 | 26.75 | 29.71 | 34.66 |
| $15.0bn (~5.8 GW) | 26.45 | 29.28 | 32.10 | 34.93 | 39.16 | 46.22 |
| $21.8bn (~8.5 GW) | 34.91 | 39.00 | 43.10 | 47.19 | 53.34 | 63.57 |
| $30.0bn (~11.7 GW) | 45.24 | 50.89 | 56.54 | 62.18 | 70.66 | 84.78 |

**Read the bottom-right cell.** Bloom shipping **11.7 GW/yr by 2030** — nearly **6x** the capacity it is building and **2.3x** its stated 5GW ambition — at a **20% terminal operating margin** that survives turbine normalisation, is worth **$84.78**. Still **–61%** from the price.

**Grid search — what assumption set *does* defend $214.96?** Scanning WACC 6–9% × terminal margin 15–30% × 2030 revenue $5bn–$150bn, the cheapest combination that clears $214.96 is:

> **WACC 6.0%, terminal operating margin 20%, 2030 revenue $30bn (11.7 GW/yr) → $244.46/share.**

A 6% WACC is roughly a regulated-utility cost of capital, applied to a company that has never earned its cost of capital in 25 years, whose stock has a 52-week range of $23.75–$351.28 and a 32% implied earnings move. Combining a utility discount rate with 11.7 GW/yr of shipments and a 20% margin that ignores the erosion call is not a scenario; it is three separate implausibilities multiplied together.

---

## 6. Reverse DCF and method cross-check

### 6.1 Reverse DCF — what $214.96 requires

**Method 1 — steady-state perpetuity.** Solve for the perpetual revenue that supports EV $66.31bn:

| WACC / g | 10% EBIT mgn | 15% | 20% | 25% |
|---|---|---|---|---|
| 11% / 2.5% | $102.5bn (39.9 GW) | $60.3bn (23.5 GW) | $42.7bn (16.6 GW) | $33.1bn (12.9 GW) |
| 9.5% / 3.0% | $78.9bn (30.7 GW) | $46.3bn (18.0 GW) | $32.8bn (12.7 GW) | $25.3bn (9.9 GW) |
| 8.0% / 3.0% | $60.7bn (23.6 GW) | $35.6bn (13.9 GW) | $25.2bn (9.8 GW) | $19.5bn (7.6 GW) |

**Method 2 — 菲比斯's terminal-multiple approach, corrected for the EV restatement.** $66.31bn ÷ 20x EV/EBIT = **$3.32bn of steady-state EBIT**. At a generous 15% through-cycle margin = **$22.1bn revenue = 8.6 GW/yr**. (His figure was ~$20bn / 8–13 GW; the corrected EV raises it to ~$22bn.) Note that a 20x exit multiple is itself internally inconsistent with a 10–12% WACC — at 11% WACC and 2.5% g, the *arithmetically implied* terminal multiple is only **6.5–8.1x EV/EBIT**, not 20x. **Method 2 is therefore the generous bound, and even it demands 8.6 GW/yr in perpetuity.**

### 6.2 Reverse DCF vs the capacity Bloom is actually building

| Shipments | Blended revenue @ $2.57bn/GW | Status |
|---|---|---|
| **2 GW/yr** | $5.1bn | **What Bloom is actually building** (Fremont, end-2026, ~$100m capex) |
| 3 GW/yr | $7.7bn | My base case 2030 |
| **5 GW/yr** | $12.8bn | **Bloom's stated maximum ambition** — and the level at which Hunterbrook alleges scandium supply (~220t vs ~240t global) becomes binding |
| 8.6 GW/yr | $22.1bn | **Minimum required by the most generous reverse DCF** |
| 12.7–16.6 GW/yr | $33–43bn | Required at 9.5–11% WACC and a 20% perpetual margin |
| 23.5–39.9 GW/yr | $60–103bn | Required at a realistic 10–15% margin |

**This is the single cleanest fact in the report: the price requires between 1.7x and 8x Bloom's own maximum stated ambition, in perpetuity, with no margin compression when turbine capacity frees up.** And the low end of that requirement (8.6 GW) sits above the physical input ceiling implied by the scandium arithmetic — which Bloom's 8-K rebutted on *China dependence*, not on *scale*.

### 6.3 Multiples cross-check

| Multiple | BE at $214.96 (diluted EV $66.31bn) | Anchor |
|---|---|---|
| EV / FY26E sales | **18.4x** | **GE Vernova ~4.8x** — the company that *owns* the bottleneck (116GW turbine backlog, $176bn total backlog, prices +195% vs 2019, sold out to 2030) trades at **a quarter of BE's multiple** |
| EV / FY26E gross profit (34% GM) | **54.2x** | Software-like multiple on a 30%-gross-margin metal-bending business |
| EV / FY26E non-GAAP operating income ($675m mid) | **98x** | — |
| EV / FY26E GAAP EBIT (~$396m at 11%) | **167x** | — |
| Forward P/E, non-GAAP ($2.05 mid) | **105x** | — |
| Forward P/E, GAAP-equivalent (~$1.08, per 巴爺爺's ~2x haircut) | **199x** | — |
| Price / book ($769m equity) | **89x** | Sector median P/B is low single digits |
| Trailing P/E | ~10,135x | Meaningless, but reported for the record |

**The SOFC peer set is empty, and that is itself the finding.** FuelCell Energy *exited* SOFC in June 2025 with a $64.5m impairment. Doosan runs 50 MW/yr. Ceres licenses rather than manufactures. There is no scaled listed SOFC comparable — so the market is pricing BE off **narrative and flows**, not off a comp set. Where there *is* a comp (GEV, the direct competitor for the same data-centre power dollar), BE trades at **3.8x** its multiple while GEV holds the structurally superior position.

### 6.4 Where DCF and comps disagree — explained before averaging

They disagree by ~2.5x on the base case, and I will **not** average them.

- **DCF base** implies fair EV/FY26 sales of **1.4x** → $19.89/sh.
- **Relative value:** applying GEV's ~4.8x EV/Sales to BE's FY26 revenue gives EV $17.3bn → equity $19.7bn → **~$52/sh**; rolling to FY28 revenue of $6.1bn at 4.8x and discounting 2 years at 11% gives **~$68/sh**; the most generous roll (FY2030 $7.5bn × 4.8x, discounted 4 years) gives **~$85/sh**.

**Why the gap, and which I trust.** A 4.8x sales multiple on a business with a 12–14% EBIT margin embeds ~35x EV/EBIT — that is itself a *growth* multiple, not a value anchor. Applying a currently re-rated peer's multiple to BE imports GEV's own optimism as though it were evidence. (One source puts GEV's own EV/EBITDA at ~89x, which flags GEV as a poor safe-harbour anchor.) The DCF, by contrast, makes the growth explicit and forces me to state the shipment volumes and margins required. **I trust the DCF as the primary method and report the relative-value output as a ceiling.**

**So the honest bounding statement is: even at the most generous defensible construction I can build without abandoning discipline (~$85), the stock is ~61% overvalued. At the primary method it is ~87% overvalued.**

---

## 7. Anti-anchoring check (KLAC audit discipline)

**The question the audit requires me to answer: is $214.96 defensible on any reasonable assumption set? My answer is no — and here is the falsification test rather than the assertion.**

**Where I could be wrong, ranked:**

1. **Discount rate.** If the market is applying a ~6% WACC on the view that a $14bn contracted 20-year service annuity plus 15–20 year offtakes makes BE utility-like, my 11% is far too punitive. **Test:** contract tenor disclosure. 修大哥 is right that this is the whole question — "judge every announcement on contract tenor, not gigawatts." If Bloom discloses that a majority of backlog carries 15–20 year take-or-pay terms with investment-grade counterparties, my WACC is wrong and my fair value roughly doubles. **Even doubled, it is $57, not $215.**
2. **Terminal margin.** I follow 菲比斯's erosion call. If Bloom's cost curve (~10%/yr unit cost-down, claimed) closes the 5–8x capex/kW gap versus turbines before 2030, terminal margins hold at 18–20% and there is no erosion. **Even at a 20% perpetual margin and 11% WACC, base value is $26.95.** This assumption cannot carry the price on its own.
3. **Revenue ceiling.** My $2.57bn/GW revenue conversion is derived, not disclosed. If Bloom's realised revenue per GW is materially higher — or if it expands past 5GW — the volume requirement falls. This is the assumption most worth attacking, and it is why I ran the grid search rather than a point estimate.
4. **The market may simply not be valuing BE on cash flows at all.** BE may be trading as a call option on AI-infrastructure power, a scarce listed vehicle for a theme, or a squeeze/flow phenomenon. **This is very likely true, and it is not a valuation argument — it is a positioning argument.** It belongs to 老詹 and Tim Cook, not to me.

**What would make me raise my fair value by ≥50%:** (i) contract tenor disclosure showing >50% of backlog on 15-year+ take-or-pay; (ii) related-party revenue falling below 25% of total *while total revenue keeps growing* (菲比斯's condition 3 — the highest-information line in the file); (iii) verified capacity commitments above 5 GW/yr with a credible non-Chinese scandium chain; (iv) two consecutive quarters of OCF ≥ net income with clean AR/inventory.

**What I refuse to do:** raise the WACC assumption downward or the terminal margin upward until the price fits. The grid in §5 is the audit trail. The only cell that clears $214.96 requires a utility discount rate applied to a 25-year value-destroyer.

**On being 5–10x below the sell-side ($193–$346, mean $286, JPM $346).** I note it, I do not defer to it. 巴爺爺 observes the JPM path went $18 → $33 (Jul 2025) → $346 (Jul 2026) — a 10.5x price-target revision inside twelve months. That is a target chasing a price, not a valuation leading one. A $193–$346 band on a $61bn company is, in 修大哥's phrase, "a coin flip with error bars."

**Explicit KPI note (assumption honesty over KPI optimisation).** My intrinsic band of **$9–$59** will very likely *not* contain the realised price over the next 12 months; flows, the Jul 28 print (~32% implied move) and the AI-power bid can hold price far above intrinsic value for years. My *separate, non-valuation* expectation for the 12-month trading range is roughly **$120–$350**. That is a positioning observation and must **not** be scored as my valuation band, nor used as a target. Widening the intrinsic band to catch the tape would be exactly the reverse-engineering my mandate forbids. **Score me on $9–$59.**

---

## 8. Margin of safety at $214.96

```
MoS = (fair value – price) / fair value
    = ($28.70 – $214.96) / $28.70  =  –649%
Price / central fair value = 214.96 / 28.70 = 7.49x
```

| 菲比斯's requirement | Required price | Actual | Met? |
|---|---|---|---|
| 60% discount to central intrinsic value (buy ≤40% of appraised value) | **≤ $11.48** | $214.96 | **NO — price is 18.7x the buy level** |
| Bear case still returns ≥0% from entry | **≤ $8.66** | $214.96 | **NO — price is 24.8x the buy level** |
| Hard position cap 1.5% of NAV (if ever bought) | n/a | n/a | Moot at this price |
| MoS even against the most generous ceiling ($85) | ≤ $34 for 60% MoS | $214.96 | **NO** |

**There is no margin of safety at any level of the analysis.** The price does not merely lack a discount to intrinsic value — it exceeds the *bull case* by 267%.

Because 菲比斯 rates the moat narrow and eroding from 2029-31, my mandate requires me to demand a *wider* margin than normal, not a narrower one. The gap is not close enough for that adjustment to matter.

---

## 9. Valuation input to committee score

### **Valuation score: 8 / 100**

| Component | Weight | Score | Rationale |
|---|---|---|---|
| Absolute valuation vs DCF | 30 | **1** | –87% to central fair value; –73% to the *bull* case. Worst absolute gap the desk has scored. |
| Relative valuation vs peers | 20 | **3** | 18.4x EV/sales vs GEV ~4.8x, on a weaker structural position; 54x EV/gross profit on a 30%-GM manufacturer; 89x book. No usable SOFC comp exists. |
| Margin of safety | 25 | **0** | Requirement ≤$11.48; price $214.96. Not met by a factor of 18.7x. Bear-case-≥0% rule missed by 24.8x. |
| Reverse-DCF plausibility | 15 | **2** | Price requires 8.6–39.9 GW/yr in perpetuity vs a 2 GW build and a 5 GW ambition; the low end collides with the scandium input ceiling. |
| Balance-sheet / downside support | 10 | **6** | **The one genuine positive.** ~$2.42bn net cash ≈ $6.4/share of hard downside support, 0% coupon, no maturity to Nov 2030, ~$3.1bn liquidity, no financing need for the 2GW ramp. Real, and worth ~22% of the bear case. |
| **Total** | **100** | **8** | |

**Score interpretation.** 8/100 is not a statement that Bloom is a bad company — 巴爺爺's 67 and the genuine 130% growth say otherwise. It is a statement that **the entire distribution of outcomes I can construct sits below the price.** A valuation score can only be low when the asset is good *and* the price is impossible; here the price is doing all the work.

**Interaction with the other scores the committee should see:** the fundamentals score (67) and news score (68) are *quality* and *flow* readings. Neither is a valuation. 巴爺爺 said it precisely: "a 67 fundamentals score provides no margin of safety whatsoever." The committee should not average 67, 68 and 8 into a "48, hold." The valuation score is a **gate**, not a weight.

**Recommendation to the committee: AVOID / DO NOT INITIATE at $214.96.** This is explicitly **not** a short recommendation — a 32% implied earnings move on 28 July, a $25bn financing headline generator, a 0%-coupon net-cash balance sheet, an empty maturity wall to 2030, genuine +130% revenue growth and an unresolvable flow/positioning bid make the borrow-and-wait trade an unbounded-loss proposition against a thesis whose catalyst is *time*, not an event. Overvaluation is a reason not to own something; it is not, by itself, a reason to be short.

**Re-engagement triggers (price-based, stated in advance so they cannot be reverse-engineered later):**
- **Watch level: $60** — parity with the bull case. Below this the asset stops being priced for perfection.
- **Interest level: $30** — approximately central fair value.
- **菲比斯-compliant buy level: $11.48**, with a hard 1.5%-of-NAV cap.
- **Independent of price**, revisit the model in full if the Q2 10-Q (28 Jul) discloses (a) related-party revenue below 25% of total with total revenue still growing, or (b) contract-tenor detail showing >50% of backlog on 15-year+ take-or-pay terms. Either would materially raise my fair value; (b) is the one that could plausibly double it.

---

## 10. Open items handed back

1. **To 巴爺爺:** the SK ecoplant 55.5% figure is, per §2.2, almost certainly a mis-attributed Brookfield-JV number. Your "grade decider" resolves — but to the *worse* structural reading (single financing vehicle), not the better one. Suggest revisiting whether the accounting-quality sub-score of 3/10 should move up (SK concentration is not real) or stay (Brookfield-JV circularity is worse).
2. **To 菲比斯:** your EV should be **$66.31bn**, not $61.6bn (if-converted). Your implied-expectations revenue moves from ~$20bn to ~$22.1bn.
3. **To 老詹:** I need the verified 52-week high and the drawdown date. My §7 trading-range comment is unsupported without it.
4. **To the committee:** the FY2025 OCF dispute ($418.1m vs $114m) turns out to be worth **less than $1/share** of intrinsic value. It matters enormously for *trust*; it barely matters for *valuation*. Do not let it crowd out the related-party and contract-tenor questions, which are worth 2–3x the share price between them.

---

*Research and decision support only — not financial advice. Every assumption is stated in §3 and sensitised in §5; the arithmetic is reproducible from the model file. Committee and Owner decide.*

**Sources:** [GE Vernova valuation multiples](https://multiples.vc/public-comps/ge-vernova-valuation-multiples) · [GEV statistics](https://stockanalysis.com/stocks/gev/statistics/) · [GEV EV/EBITDA](https://valueinvesting.io/GEV/valuation/ev_ebitda-multiples) · [GEV Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gev2q2026form8-k.pdf) · plus all primary sources carried through from `2026-07-19-be-financials.md`, `2026-07-19-be-moat.md` and `2026-07-19-be.md`.

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
