# INTC — Research Package Audit

**Auditor:** Ai 管理層, Department 9 (AI Intelligence) · **Date:** 2026-07-28
**Package audited:** 𢦀鳩仔 valuation · 菲比斯 moat · 巴爺爺 financials · 修大哥 news
**CRO review:** not on disk at audit time — audited what was available.
**Audit method:** independent re-verification via WebSearch (WebFetch returned HTTP 403 on
every attempt for me too — stockanalysis.com and trefis.com both denied — confirming the
research agents' egress claim as a **real proxy-policy fault, not an excuse**).

---

## 0. Verdicts

| Report | Score claimed | **Verdict** | Reason |
|---|---|---|---|
| 𢦀鳩仔 — Valuation | 12/100 | **PASS WITH FLAGS** | Arithmetic reproduces; conclusion survives removal of every flagged input. Six flags, none conclusion-changing. |
| 巴爺爺 — Financials | 55/100 (C+) | **PASS WITH FLAGS** | One HIGH flag: an unsupported "~$40B annualized OCF" that is ~43% overstated and load-bearing to the self-funding conclusion. |
| 菲比斯 — Moat | Narrow/Eroding + None | **PASS WITH FLAGS** | One MEDIUM-HIGH flag: an uncited "~105x forward earnings" that is unreconcilable with the package's own numbers and propagated into the 12/100 scorecard. |
| 修大哥 — News | 62/100 | **PASS WITH FLAGS** | Best sourcing discipline in the package. Missed a dated external-foundry-customer headline; understates sovereign capital by ~$4B. |

**No FAIL.** No report goes back before committee. **Package is FIT FOR COMMITTEE, with
five conditions in §6.**

---

## 1. Citation audit — load-bearing numbers

### 1.1 Q2 FY2026 income statement — **ALL VERIFIED**

Independently re-confirmed via search extraction of CNBC, Yahoo Finance, TradingKey,
DataCenterDynamics and TheNextWeb (all 2026-07-23/24):

| Claim | Report(s) | Result |
|---|---|---|
| Revenue $16.1B, +25% YoY, fastest in ~15 years | all four | **VERIFIED** |
| Consensus revenue $14.42B | 修大哥 | **VERIFIED** |
| Non-GAAP EPS $0.42 vs $0.21 consensus | 巴爺爺, 修大哥 | **VERIFIED** |
| GAAP net loss $(11.0)B / $(2.16) EPS | all | **VERIFIED** |
| $12,529M / $12.5B escrowed-shares mark-to-market | 菲比斯, 巴爺爺, 修大哥 | **VERIFIED** (headline $12.5B confirmed; exact $12,529M rests on the StockTitan 10-Q summary — one source, but consistent) |
| DCAI $6.3B, +59% | all | **VERIFIED** |
| CCG $8.9B, +13% | 巴爺爺, 修大哥 | **VERIFIED** |
| GAAP GM 40.4% (vs 27.5%) | 菲比斯, 巴爺爺 | **CORROBORATED** (secondary; non-GAAP 41.8% independently confirmed) |
| DCAI op margin 39.5% (vs 16.1%) | 菲比斯, 巴爺爺 | **CORROBORATED** (secondary only — segment operating income was not in any primary extract I could reach) |
| Foundry $5.8B rev, $(2.1)B / −36.2% | all | **CORROBORATED** (FourWeekMBA, marklapedus — both secondary) |

### 1.2 The bull's best datapoint — **VERIFIED**

**External foundry revenue $293M in Q2'26 vs $307M for all of FY2025.** Independently
confirmed (Analysis.org, Windows Forum, and the Q2 10-Q index). This is the single most
load-bearing bull datapoint in the package and it survives audit intact. Credit to 巴爺爺
for naming it "the single most encouraging number in the entire release" *in a report that
grades the company C+* — that is the correct behaviour.

### 1.3 CHIPS escrow and the anti-correlation claim

- **$12,529M derivative charge: VERIFIED.**
- **Derivative liability $15.6B at 27 Jun 2026 vs $2.7B at 27 Dec 2025:** single-sourced
  (StockTitan 10-Q summary). **CORROBORATED, THIN.**
- **Mechanism check:** the DOC escrow is a fixed share count (158.74M issued into escrow)
  marked at market. Liability = N × price, so the MTM loss *does* grow as the stock rises.
  **The mechanism is correct.**
- **FLAG (LOW):** 菲比斯's phrasing — "Intel's GAAP EPS is now **anti-correlated** with its
  share price" — overstates. GAAP EPS is operating earnings *plus* the derivative line; the
  anti-correlation is conditional on the derivative dominating, which it did in Q2 ($12.5B
  vs $2.2B) but need not always. The practical instruction (exclude INTC from GAAP-EPS and
  book-value factor screens) is **correct and should be actioned by 賭馬狗 regardless**.
- 巴爺爺's refusal to dismiss the charge as cosmetic ("$15.6B of real value transfer to the
  US Government") is an independent judgement that *diverges* from 菲比斯. Noted as
  evidence against groupthink.

### 1.4 The DOC warrants — **VERIFIED, with new detail**

Confirmed against the Intel 8-K / 424B7 resale registration: **a warrant over up to
240,516,150 shares at an initial exercise price of $20.00**, exercisable **only on a
Triggering Event that reduces Intel's ownership of the foundry business below 51%**,
settleable in cash or shares, capped at 19.9% of pre-transaction shares absent stockholder
approval. All three reports describe this correctly.

**New reconciliation the package did not make:** the DOC received **274,583,000 shares
issued directly + 158,740,000 shares issued into escrow = 433,323,000**, which is exactly
菲比斯's "433.3M shares at $20.47 (~9.9%)". **菲比斯's figure is now VERIFIED** and its
composition is known. This matters — see flag V-1.

### 1.5 Zero committed external 14A customers — **CORROBORATED**

Consistent across all three reports and Tom's Hardware: **two prospective 14A customers
with early PDK access, binding decisions expected 2H26–1H27, zero committed today.**
菲比斯 states this precisely ("14A committed external customers: ZERO"). 巴爺爺 and
𢦀鳩仔 use looser phrasing ("committed customers today = zero") that reads as *no external
foundry customers at all*, which is not true — see N-1.

### 1.6 Equity base $103,143M at 28 Mar 2026 — **FLAGGED**

Confirmed that stock-analysis-on.net does publish **total equity ~$103,143M** and **total
assets ~$202,439M** for the quarter. But my own re-query of the same source surfaced
**conflicting adjacent figures: non-controlling interests ~$13.6B and stockholders' equity
excluding NCI ~$111.4B** — which do not reconcile with a $103,143M total. See flag V-2.

### 1.7 Share count progression — **PARTIALLY FLAGGED**

| Figure | Source | Result |
|---|---|---|
| ~5.04B outstanding, Jul 2026 | 巴爺爺, 菲比斯 | **CORROBORATED** (consistent with ~$464B cap at ~$92) |
| 5,083M basic, Q1'26 | 巴爺爺 | **UNRESOLVED** — a *weighted-average* figure that exceeds the *point-in-time* 5,023M outstanding at 28 Mar 2026. In a rising-share-count company the weighted average should be *lower*. One of the two is mislabelled. (LOW) |
| ~4.15B in 2023 | 巴爺爺 [self-marked UNVERIFIED] | **UNVERIFIED, PROPAGATED** — see flag F-3 |
| ~4.23B in 2023 | 菲比斯 | **CONFLICTS with 巴爺爺's 4.15B**, unreconciled in-package; produces 19% vs 22% dilution |
| 5.424B fully loaded | 𢦀鳩仔 | **ARITHMETIC OK, CONSTRUCTION FLAWED** — see flags V-1 and V-3 |

---

## 2. THE PRICE — resolved

### Resolution: **$91.68 is the correct input. Two of the four "quotes" were never candidates.**

Reconstructed tape, each step independently corroborated:

| Date | Price | Basis |
|---|---|---|
| ~20–22 Jul (pre-print) | **$97.06** | Finbold's own reference close. My search confirms Finbold wrote "$113.72, implying roughly **17% upside from the recent closing price of $97.06**" — 113.72/97.06 = 1.172 ✓. The article is titled *"...ahead of earnings."* **This is a PRE-PRINT close mislabelled as "recent."** |
| Wed 22 Jul | **$102.62** | stockinvest extract (修大哥). **This is the source of the "~$102" figure.** Also pre-print. |
| Thu 23 Jul (close) | ~$100.23 | Back-solved: $92.32 ÷ (1 − 0.0789). Q2 reported after this close. |
| Fri 24 Jul | **$92.32**, −7.89% | Verified twice (stockanalysis, TradingView) |
| Mon 27 Jul | **$91.68** (feed 2: $91.88) | 巴爺爺's two feeds. **Independently corroborated by a quote page showing $91.52 in the same session band.** |

**Verdict: there was never a four-way conflict.** $102 and $97.06 are stale pre-earnings
prints from 20–22 Jul that two secondary outlets described as "recent close." $91.88 vs
$91.68 is a feed-timing difference of 0.2%. **𢦀鳩仔 and 巴爺爺 chose correctly.**

**Credit where due:** 修大哥 was the most rigorous of the three — he refused to assert the
27 Jul close, marked it UNKNOWN, and *reported the $102 contradiction as a contradiction
rather than resolving it on a guess*. That is exactly right. I have now resolved it in his
favour on process and in 巴爺爺's favour on the number.

**Materiality: nil.** Across the full $91.52–$102.62 range the MoS moves from −177% to
−211%. No conclusion in the package turns on it.

### Flag F-2 (MEDIUM) — the unsupported intraday range
巴爺爺 states "close **$91.68** on 27 July 2026 (**intraday $86.94–$94.98**)". The $91.68
close is corroborated; **the $86.94–$94.98 intraday range is not, by anything.** An $86.94
low implies a −5.2% intraday excursion on a day with no news, and the independent quote
page I reached shows a session low of $91.22. This is a **suspiciously precise, unsourced,
uncorroborated figure** — a textbook hallucination pattern. It is not used downstream, so
severity is capped at MEDIUM, but it should be struck.

### 52-week range and +343% — **VERIFIED, and the CEO's correction is confirmed**

- **52-week range $18.97 – $142.35: INDEPENDENTLY VERIFIED.** (巴爺爺 $142.35, 修大哥
  $142.34 — a one-cent difference; $142.35 is correct.)
- **+343% over 52 weeks: CORROBORATED.** It implies a price of ~$20.70 twelve months ago,
  consistent with the verified $18.97 low. Independently supported by a Trefis piece dated
  **2026-07-27** headlined *"Intel More Than Quadrupled In A Year"* (>+300%) and by Motley
  Fool's "+270% in the first half."
- **Drawdown:** $91.68 / $142.35 = **−35.6%**. 巴爺爺's "~36%" ✓; 修大哥's "−35.1%" from
  $92.32 ✓. Both correct.

**On the CEO's self-correction — VERIFIED, and I will state it more strongly than the
package did.** At $91.68 on ~5.04B shares INTC carries a **~$462B market capitalisation on
revenue 33% below its 2021 peak**. That is materially above Intel's 2020 cycle-peak market
value and is being paid on **~7.2x annualised sales and ~55x the run-rate non-GAAP EPS**
[my derivation from the package's verified inputs; Intel's own historical sales multiple
range is my estimate, not fetched]. **"Cheap turnaround" was not a mild mis-framing — it
was inverted.** The correction is verified and should be minuted; the framing error is the
kind that, uncorrected, manufactures confirmation bias for every downstream agent.

**Flag F-1 secondary (MEDIUM):** 巴爺爺 states the $91.68 close and "+343%" as **fact**;
修大哥, working the same session, marked the 27 Jul close **UNKNOWN** and the 12-month
change **"not precisely verifiable."** Same package, same day, same access constraints, two
different confidence standards on the same number. Both happen to be right in substance —
this is a **process** flag, and it is the (e)-pattern. See §5.

---

## 3. Logic audit — does $22–55 follow?

**Model integrity check — I recomputed 𢦀鳩仔's base case from his own assumption table:**

- Products: (34.0 × 22%) + (21.0 × 25%) = $12.73B EBIT → 23.15% blended ✓ (he states 23.1%)
- NOPAT = 12.73 × 0.85 = $10.82B × 12x = **$129.8B** ✓
- Sum: 129.8 + 0 + 3.4 + 4.2 − 20 − 18.8 + 4.8 + 39 = **$142.4B** ✓ (he states $142.5B)
- ÷ 5.424B = **$26.25** ✓ (he states $26.27)
- Weighted 30/45/25: (−0.43 × .30) + (26.27 × .45) + (84.05 × .25) = **$32.70** ✓

**The model is arithmetically sound. Nothing is fudged.** That is worth saying plainly
before the criticisms.

### V-1 (MEDIUM) — the escrowed shares are probably double-counted in the denominator

𢦀鳩仔 builds 5.424B as **5,040 outstanding + 143 escrowed + 241 warrants**. But the
escrowed shares were **issued into escrow** (158.74M per the 8-K I verified in §1.4), and
巴爺爺 states that **71M of the 143M are already in basic EPS**. Shares issued into escrow
are normally already inside "shares outstanding." **Adding 143M on top of 5,040M therefore
double-counts somewhere between 71M and 143M shares** — in the very section titled
*"Dilution, handled properly"* and immediately after a subsection on *"the double-counting
trap."*

Effect: up to **−$0.70/share**. Immaterial, and it runs **against** his own conclusion
(over-dilution lowers FV). But it is a genuine methodological error in the section claiming
special rigour, and it must be fixed before the number is reused.

*Separately, and to his credit:* his escrow treatment (include the shares, exclude the
$15.6B liability) is the **bull-favourable** of the two valid options — subtracting the
liability instead would give $24.03/share, not $26.27. He picked the option worth **+$2.24
to the bull** and explained why. That is not a bear thumb on the scale.

### V-2 (MEDIUM) — "verified" equity is an aggregator figure, at the wrong date, with an unreconciled NCI

巴爺爺 marked total stockholders' equity **[UNVERIFIED — could not retrieve]** and his ROIC
**[ESTIMATE]**. 𢦀鳩仔 then labels his recomputation *"巴爺爺 (recomputed on **verified**
equity)"*. The $103,143M is:
1. from **stock-analysis-on.net**, a tertiary aggregator — not the 10-Q;
2. at **28 Mar 2026 (Q1)**, not the 27 Jun 2026 balance-sheet date everything else uses;
3. **not reconciled** — my own query of the same source returned adjacent figures of NCI
   ~$13.6B and equity-ex-NCI ~$111.4B, which do not sum to $103,143M.

**"Retrieved" ≠ "verified."** This is the clearest instance in the package of an
UNVERIFIED figure being upgraded to fact by a downstream agent. **Mitigant:** the lower
equity base *raises* ROIC from 6.5% to 7.2%, i.e. it works **against** his own conclusion,
so this is a rigour failure and not a bias failure. And he runs the sensitivity showing the
SOTP frame survives at 7.2%.

### V-3 (LOW) — the warrants are included unconditionally against his own stated assumption

The 241M warrants are exercisable **only** on a Foundry-divestiture Triggering Event
(verified §1.4). 𢦀鳩仔 lists among his *"Deliberate non-assumptions"*: **"a Foundry
spin-off (the 241M $20-strike warrants make it prohibitively expensive)."** In his base case
the trigger therefore **never occurs and the warrants can never be exercised** — yet he puts
241M shares in the denominator *and* $4.8B of proceeds in the numerator. That is internally
contradictory: he assumes the event doesn't happen and prices its consequences anyway.

**On the specific question asked — is including both the shares and the proceeds
double-counting? No.** If you add the shares you *must* add the cash; that is the
if-converted method and it is more conservative than treasury-stock, exactly as he says. His
*mechanics* are right. His *conditionality* is wrong. Net effect of removing both:
$26.27 → ~$26.57, i.e. **+$0.30/share.** Immaterial.

### V-4 (MEDIUM) — the $20B unallocated-corporate deduction is directionally right, quantitatively unsupported

His justification: "Segments sum to $2.7B of op income vs a barely-positive consolidated
GAAP line." Check: 2.3 + 2.5 − 2.1 = **$2.7B ✓**. But:

1. **The consolidated GAAP operating income line was never retrieved by anyone.** 巴爺爺's
   table records it as "positive (swung)" — unquantified — and marks the FY2021–25 operating
   income rows **[UNVERIFIED]**. So the *size* of the unallocated bucket is inferred from a
   number nobody in the package has. There is also an "all other" segment (Mobileye, IMS)
   between the three named segments and consolidated, which is not accounted for.
2. **Tax inconsistency:** he capitalises a **pre-tax** cost at 10x, then values Products
   **NOPAT** (after 15% tax) at 12x. A $2.5B pre-tax cost is $2.1B after tax. This
   **overstates the deduction by roughly 15%, ~$3B, ~$0.55/share.**
3. **Composition:** he names "SBC, intangible amortisation, chronic restructuring."
   Intangible amortisation is non-cash and should not be capitalised at 10x in a cash-based
   SOTP.
4. The bear-bull range (−$30B to −$12B) is a 2.5x spread on pure judgement.

**But his core criticism of published SOTPs is legitimate:** unallocated corporate cost is
real and omitting it does flatter every street SOTP. **The line should stay; the magnitude
needs a retrieved consolidated operating-income figure.** Cost of the whole line:
**$3.69/share, 11% of the $33 target.** Not conclusion-changing.

### V-5 — Foundry at zero: **DEFENSIBLE**

Not a shortcut. It is built up: +$17B realisable asset − $14B PV of losses − $10B PV of
excess capex + $7B SCIP/CHIPS = **$0.0B**. Landing exactly on zero is suspiciously round,
but the components are individually disclosed and, decisively, **Sensitivity 7.2 spans
−$35B to +$35B of Foundry value and the conclusion is invariant across the entire range**
($19.08 to $32.72 at base P(14A)). The double-count he needed to avoid — crediting Products
with "free" fabs — he explicitly avoids and explains.

**Residual flag (LOW, self-disclosed):** B1 ($85B PP&E allocated to Foundry) is **UNVERIFIED**
and drives B2. He flags it himself in §8(b)(3) and quantifies the error at +$9.40/share.
Adequate disclosure. Minor consistency slip: he calls it "[ESTIMATE]" in §2 but writes
"~$110B PP&E" as a hard figure in the scorecard's asset-backing rationale.

### V-6 (LOW) — Mobileye

**$6.77B market cap: VERIFIED** (companiesmarketcap, stockanalysis, both July 2026).
I checked the Class A / Class B float trap specifically, because MBLY aggregator market caps
sometimes reflect only the Class A float — **it does not appear to be the case here**;
$6.77B is the whole-company figure.

**However:** the 2026 proxy shows Intel holds **50,000,000 Class A + all 597,768,015 Class
B = ~647.8M shares**, which against a plausible ~810M total implies **~80% economic
ownership, not the 86%** 𢦀鳩仔 assumed [my estimate — I did not retrieve total shares
outstanding directly]. Note the widely-quoted "96.9%" is **voting** power, not economic.
Effect of 86% → 80%: about **−$0.06/share.** He tagged it **[ESTIMATE — exact % unverified]**.
Properly handled; immaterial.

Chain check: $6.77B × 86% × (1 − 28%) = **$4.19B** ✓ reproduces his $4.2B.

### V-7 (LOW) — the bear floor is inconsistent between text and arithmetic

He floors the bear at "$0–10/share" in the headline and argues at length that the equity
cannot go to zero. He then probability-weights using the **unfloored −$0.43**. Using a $5
midpoint instead gives **$34.33, not $32.70.** The inconsistency biases his own FV **down**
by $1.63/share.

### **Does the conclusion follow? YES — and here is the test that settles it.**

Strip out **every single flagged input** — delete the $20B corporate deduction, use the
correct share count, floor the bear, restore the 14A probability to 菲比斯's 50%, accept the
7.2% ROIC reading, hand Foundry the +$35B bull value — and you are still nowhere near
$91.68.

The decisive number is the one that depends on **none of his assumptions**:
**management's own full 2030 plan, delivered on time and in full, discounts back to
$39–46/share.** That is Intel's own guidance, discounted. It is **50–57% below the current
price.** Every contested judgement in this report could be wrong in the bull's favour and
the gap would still be roughly halved, not closed.

**Conclusion-strength does not exceed evidence-strength.** He says "not a
valuation-supported purchase at $91.68" — not "short it," not "the business is bad." He
explicitly records the opposite ("quality-improving, price-unsupported"). The calibration
is correct.

---

## 4. Cross-report contamination — unverified treated as fact

*This was priority (e). Four instances found; the ROIC dispute is not the worst one.*

### C-1 (MEDIUM-HIGH) — "~105x forward earnings" · **the worst instance**
菲比斯 asserts INTC trades at **"~105x forward earnings and ~7.9x sales"** with **no
citation and no derivation**. 𢦀鳩仔 then carries it as fact — into §6 ("~105x forward
GAAP-adjusted earnings on 菲比斯's read") and, critically, into the **12/100 scorecard's
"Multiple reasonableness" rationale**.

**It does not reconcile with the package's own numbers.** $462B ÷ 105 implies ~$4.4B of
forward earnings. Against the package's own $8.8B annualised non-GAAP net income the
multiple is **~53x**. 巴爺爺 independently computes **~55x**. **𢦀鳩仔 quotes 55x and 105x
in the same sentence without noticing they are incompatible by a factor of two.**

The bear case does not need the 105x — 55x on peak-cycle earnings already makes the point.
But an uncited figure that is 2x wrong, sitting inside the rationale for the headline score,
is precisely what this desk exists to catch. **Required fix: derive it or delete it.**

### C-2 (MEDIUM) — the ROIC "resolution" is a substitution, not a resolution
The brief asked me to check the claimed resolution at a normalised 3.8%. **Arithmetic
checks:** $4.4B NOPAT ÷ ~$117.8B ≈ 3.7–3.8% ✓; 巴爺爺's 6.5% ✓ ($8.8B ÷ $133.8B); the
recomputed 7.2% ✓ ($8.8B ÷ $121.9B).

**But 3.8% does not *reconcile* 2.45% and 6.5% — it is a fourth, differently-constructed
number** (consolidated normalised NOPAT after deducting the full Foundry loss and corporate
cost, over total invested capital). 𢦀鳩仔 then declares that because his number is "much
closer to 菲比斯," **"菲比斯 is right on the call that matters."** That is a rhetorical
move: introduce your own construct, then award the argument. And it is the analyst who was
*handed* the SOTP framework by 菲比斯 ("Framework: sum-of-the-parts, **per 菲比斯's
instruction**") producing the number that validates that framework.

**Two strong mitigants, which is why this is MEDIUM and not a FAIL:**
- He runs the sensitivity explicitly: **"even if I am wrong and the true normalised ROIC is
  7.2%, that is still 2–4 points below WACC — the SOTP frame survives either reading."**
  All three readings are below a 9–11% WACC, so the framework choice is invariant.
- The framework choice is **not outcome-determinative anyway**: his EV/sales, normalised P/E
  and management-2030-plan cross-checks are all independent of SOTP and land $16–46.

**Also flagged:** the underlying 2.45% is single-sourced to **GuruFocus**, a tertiary
aggregator, and it is the gate for the entire methodological choice. It deserved a second
source.

### C-3 (MEDIUM) — sovereign capital: three different totals for the same three cheques
US Govt $8.9B + NVIDIA $5B + SoftBank $2B = **$15.9B** (巴爺爺, correct). 𢦀鳩仔 uses
"~$16B" ✓. **修大哥 uses "~$12B" twice** — apparently substituting the $5.7B CHIPS
conversion for the $8.9B total. The news analyst's figure understates the strongest
solvency datapoint in the bull case by ~25%. **Fix 修大哥's number to $15.9B.**

### C-4 (LOW-MEDIUM) — the 2023 share base
巴爺爺 marks "~4.15B (mid-2023)" **[UNVERIFIED — approximate]** in his §5 table, then states
it as fact in his §1 summary and his "watch-item #4." 菲比斯 independently uses **~4.23B**.
Neither reconciles the other. 𢦀鳩仔 adopts 4.15B **untagged** and headlines
**"+~30% vs ~4.15B in 2023."** An unverified denominator is carrying a headline dilution
claim in three reports. The true FY2023 figure was ~4.19–4.23B [my estimate, not fetched],
which would make the fully-loaded dilution ~28%, not 30%. Immaterial in magnitude;
the propagation pattern is the point.

### F-1 (HIGH) — 巴爺爺's "~$40B of annualized OCF"
> "At $20B+ against **~$40B of annualized OCF-if-margins-hold**, Intel can self-fund — but
> only just."

**This figure appears nowhere else in his report and is not supportable from it.** Q2'26 OCF
was **$7.0B → $28B annualised**. FY2025 OCF was **$9.7B**. **$40B is ~43% above his own
best-case run-rate**, and it is the number on which he rests "Intel can self-fund."

**Highest-severity flag in the package**, because unlike the others it makes the *bull* case
look stronger than the evidence supports, and it sits inside the section headed "the
Survival Question." **Mitigant:** the self-funding conclusion is independently supported by
the verified H1'26 fact (OCF exceeded PP&E capex by $1.9B, a $7.8B YoY swing), and
𢦀鳩仔 did **not** propagate it — he independently modelled ~$18–19B normalised OCF, far
more conservatively. **Required fix: correct to ~$28B annualised and re-word the
conclusion.**

### N-1 (MEDIUM) — a missed external-foundry-customer headline
All four reports frame external foundry customers as an unbroken silence. My search
surfaced a TechTimes piece dated **2026-07-23**: *"Intel Foundry Breaks Customer Silence
With Fortinet Deal as Q2 Earnings Approach."* **I have the headline only** — I could not
verify the node, size, or whether it is a binding commitment, and it is likely small and
probably not 14A. **I am not asserting it as fact and neither should the committee.** But a
named external foundry customer announced on the day of the print, missed by the Global
News Analyst in a sweep whose §M1 is entirely about foundry customer commitments, is a
**coverage gap on the single most catalyst-sensitive item in the name.**

**It also sharpens a precision point:** 菲比斯 states the claim correctly — *"14A committed
external customers: ZERO"* — while 巴爺爺 and 𢦀鳩仔 use the looser "committed customers
today = zero." The qualifier "committed, high-volume, non-strategic **14A**" is doing real
work, because Amazon, Microsoft and the US DoD are already named 18A external commitments
in 菲比斯's own report. **Route to 修大哥 for verification.**

### N-2 (LOW-MEDIUM) — 修大哥 overrides his own scorecard
He computes the weighted score as **60.1** and then writes "**adjusted to 62** for the
quality of the Q3 guide." Disclosed, small, and in the *bullish* direction — but a
scorecard you can hand-adjust is not a scorecard. Either weight the guide inside the model
or report 60.

---

## 5. BIAS AUDIT

*This was the central question. Answering it adversarially, in both directions.*

### 5.1 The prosecution: five for five, and a scorecard that cannot say otherwise

MU (watch) · MRVL 25 · KLAC 33 · BE 8 · **INTC 12**. Five consecutive rejections on price.
I have already confirmed narrative lock-in twice — analyst-level on KLAC, package-level on
BE. The base rate now demands a structural explanation, and I have found one.

**Finding B-1 (HIGH) — the valuation score is near-deterministic in a single variable, so
"12/100" carries almost no information beyond "price > FV."**

Look at the scorecard construction:
- *Absolute value vs price* — **40% weight**, a direct function of price ÷ FV.
- *Margin of safety vs required* — **20% weight**, and explicitly **binary**: "50%
  required; −178% delivered. **Binary fail.**" → scored **0**.

**60% of the weight is one variable, and 20% of it is a hard zero for any stock not trading
at a 50%+ discount to the analyst's own fair value.** Mechanically, **no stock trading at or
above the analyst's FV can score much above ~40, and any stock without a 50% discount is
capped at 80** — regardless of business quality, catalyst, optionality or improvement. The
score is not a verdict on the opportunity. **It is a restatement of the margin of safety
wearing a scorecard's clothes.** That is why five names in a row score in the 8–33 band: the
instrument can only produce that band in an expensive tape.

**And it produces a result that flatly contradicts its own author.** 𢦀鳩仔 writes that INTC
is **"the first name in this sequence where the operating fundamentals are genuinely
improving"** and **"the opposite of the four names this desk previously rejected, where the
businesses were also deteriorating"** — and then scores it **12, below MRVL (25) and below
KLAC (33)**. On the analyst's own reasoning INTC is the *best* business of the five and it
receives the *second-worst* score. **The text and the number disagree, and the committee
will read the number.** This is precisely how narrative lock-in manifests numerically: not
through a biased analyst, but through an instrument that cannot express "good business,
wrong price."

**Aggravating: the 50% MoS hurdle is set by one unaudited qualitative moat call** (菲比斯)
and then becomes a 20%-weight binary gate in a different analyst's score. Single point of
failure, no review step.

**Aggravating: framework pre-commitment.** 𢦀鳩仔's header reads "Framework: Sum-of-the-parts,
**per 菲比斯's instruction. No franchise DCF.**" The methodology was handed down before the
valuation was built, by the analyst whose conclusion it supports. *Mitigated* by C-2 above —
the conclusion is invariant to the framework.

### 5.2 The defence: the anti-anchoring work is real, and I can prove it quantitatively

I tested for a systematic thumb on the scale by cataloguing **every discretionary choice
𢦀鳩仔 made where the evidence permitted two answers**, and scoring its direction:

| Discretionary choice | Direction | $/share |
|---|---|---|
| Escrow: include shares rather than subtract the $15.6B liability | **pro-bull** | **+2.24** |
| Equity base: adopt the aggregator figure that lifts ROIC 6.5% → 7.2% | **pro-bull** | (frame) |
| Sovereign capital: use $16B (not 修大哥's $12B) in the steel-man | **pro-bull** | (frame) |
| Bear floor: weight the unfloored −$0.43, not his stated $0–10 floor | **pro-bear** | **−1.63** |
| P(14A): override 菲比斯's 50% down to 30% | **pro-bear** | **−4.80** |
| Carry 菲比斯's uncited 105x alongside his own 55x | **pro-bear** | (frame) |
| Escrowed-share double-count in denominator | pro-bear (error) | **−0.70** |
| Warrants included though their trigger is assumed not to occur | pro-bear (error) | **−0.30** |

**Roughly three pro-bull, five pro-bear, netting to about −$5/share on a $33 target.** A
fully de-biased rebuild lands near **$37–38 against a price of $91.68.** **There is no thumb
on the scale of a size that matters.** An analyst who was reverse-engineering a bearish
answer does not hand the bull $2.24/share on the escrow treatment and then flag that he did
it.

**The other exculpatory evidence is substantive, not cosmetic:**
1. He **quantifies his own heresy** — "I am 71% below consensus… **the base rate says
   error**" — and then *diagnoses the disagreement in a falsifiable form*: consensus $113.72
   implies ~$3.79 EPS ≈ **exactly FY2021's peak profit on a 30%-larger share base**. That
   reframes the debate as one testable question (are Q2 margins a floor or a peak?) with a
   **dated** resolution (2027–28). Unfalsifiable house views do not generate dated tests.
2. He **rebuilt the bull upward** after the first pass came in below market, and **disclosed
   doing so** in a signed attestation rather than banking a convenient finding. That is the
   single most persuasive item in the file.
3. He states **"the market is not obviously irrational; it is pricing my bull case as the
   base case"** and **"momentum has been right for 52 weeks and I have not been."** Locked-in
   narratives do not concede the other side's rationality.
4. He publishes **four dated falsification triggers**, a **revisit level ($45, below which
   he would re-engage without a 50% MoS)**, and a **re-run date (Q3'26 print)** — and states
   that if two triggers land his base goes to **$70–85** and it "becomes a debate about
   paying up for quality rather than a valuation veto."
5. His sensitivity tables are **honest in the hostile direction**: he displays the top-right
   corner (peak margin declared permanent × 18x multiple) and reports the answer that
   embarrasses him least-favourably — $50.42, still 45% below.

**Is that discipline or sophisticated cover? My verdict: discipline.** Cover does not
publish a revisit price, a re-run date, four falsification triggers, an admission of being
wrong for 52 weeks, and a signed record of having rebuilt the bull case *upward*. Cover
also does not give away $2.24/share on a judgement call nobody would have checked. **I
checked, and it holds.**

### 5.3 Steel-manning the bull myself — and did the package give it a fair hearing?

**The bull case, at full strength:** Intel is the only non-Asian leading-edge logic
manufacturer, and in a single quarter it inflected on **five independent axes at once** —
process (18A in HVM, output **~25% above target and +50% QoQ**, Clearwater Forest launched),
margin (GAAP GM 27.5% → 40.4%, **280bps above guidance**, guided higher again), demand
(revenue **+25%, fastest in 15 years**; DCAI **+59%**), cash (H1 OCF exceeded PP&E capex by
**$1.9B, a $7.8B YoY swing**), and merchant traction (**external foundry revenue of $293M in
one quarter versus $307M for all of FY2025 — a ~4x annualised step-up**). Solvency is
underwritten by **~$15.9B of sovereign and strategic equity** at $20.47–$23.28 plus $29.7B of
liquidity and maturities termed to **2066** — so the bear case cannot express itself as
bankruptcy, only as underperformance. Management **beat and guided above on both lines for a
seventh consecutive quarter**. And a **binding 14A commitment is a live, dated, binary
catalyst inside two quarters**, with two prospects already holding PDK access. When compute
capacity is the scarce global input and Washington is an equity holder, the second
derivative turning on five metrics simultaneously is not a cigar butt being re-rated — it is
a franchise being rebuilt, and you do not get to buy that at 10x.

**Did the package give it a fair hearing? On the numbers, yes — unusually so.** 𢦀鳩仔's
§8(c) is a genuine steel-man written to persuade, it lands at **$84/share (within 8% of the
market)**, and he concedes the market may simply be pricing his bull as its base. 巴爺爺
calls the external-foundry number "the single most encouraging number in the entire release"
and lists every positive second derivative. 修大哥 scores news 62 and rates the name NEUTRAL,
not underweight, explicitly citing solvency, 18A, the guide and the policy backstop.
**Dissent exists in this package** — a **50-point spread** between 𢦀鳩仔's 12 and 修大哥's
62 — so this is **not** groupthink at the evidence level. Convergence happens only at the
conclusion, and only through one variable.

**Two places where it did not get a fair hearing:**

**B-2 (MEDIUM) — reflexivity is acknowledged and then dropped.** 𢦀鳩仔 raises it in a
single italicised footnote: *"the government's 9.9% stake, the SCIP structures and the
escrow derivative make Intel's capital structure genuinely reflexive — the higher the stock
goes, the more capital it can raise on better terms, which improves fundamentals. My model
has no mechanism for that feedback loop."* **He is right, and then he does nothing with
it.** For this specific company that is not a footnote: a higher share price directly
shrinks the **−$10B PV-of-excess-capex line (B4)** that he himself calls "the funding gap,"
and directly reduces the probability of the dilution he models as a bear item. A static SOTP
**structurally under-values a company whose fundamentals improve with its own share price.**
Nobody in the package modelled it, and nobody bounded it. **This is the largest unpriced
bull item in the file.**

**B-3 (MEDIUM) — the one clear directional override goes against the bull, on non-evidence.**
𢦀鳩仔 marks P(14A success) **down** from 菲比斯's "roughly a coin-flip" to **30%**, citing
"committed customers today = **zero**." But **the decisions are not due until 2H26–1H27** —
zero committed customers *before the decision date* is the **expected** count, not adverse
evidence. He is discounting on a fact that carries no information, and it is arguably the
same fact that already generated 菲比斯's coin-flip, i.e. counted twice. Restoring 50% adds
**~$4.80/share**. It is the clearest single instance of a directional thumb in the report —
which is worth naming *precisely because* everything around it was clean.

### 5.4 Bias verdict

**"Expensive" has NOT become an unfalsifiable house view — but the scoring instrument
has.**

The analysis is falsifiable, dated, and self-critical to an unusual degree; the flags I found
run in both directions and net to under $5/share. **The 12/100 is a defensible valuation
output.** But it is a **misleading committee input**, because the scorecard is ~60%
determined by one variable and therefore cannot distinguish "good business, wrong price"
from "bad business, wrong price" — which is the exact distinction the analyst spent his §8
insisting upon, and which is the only distinction that matters after five rejections in a
row.

**The real institutional risk is no longer that an analyst is anchored. It is that the
firm's scoring architecture converts every price-based rejection into a low quality score,
building a false record that the desk has examined five bad businesses when it has actually
examined at least one good one at a price it did not like.** That record will bias the sixth
name before anyone reads it.

**Routed to 床狗 (Prompt Engineering) — recurring failure patterns:**
1. **Split the valuation score into two reported numbers: Business Quality and Price
   Attractiveness.** Never composite them into one figure the committee reads as a verdict.
   Retro-apply to MU/MRVL/KLAC/BE so the record is corrected.
2. **Ban binary zero-weighted components.** A 20% weight that can only be 0 or 100 is a veto
   disguised as a score.
3. **Require the moat analyst's MoS hurdle to be audited before it becomes a scoring gate.**
4. **Prohibit downstream agents from re-labelling an upstream `[UNVERIFIED]`/`[ESTIMATE]` tag
   as "verified" without an independent second source at the correct reporting date** (V-2).
   Tags must propagate.
5. **Require every multiple quoted in a scorecard rationale to carry its derivation** (C-1:
   a 2x-wrong uncited 105x reached the headline score).
6. **Require the sender's framework instruction to be disclosed as an instruction** when one
   analyst hands another a methodology (C-2) — 𢦀鳩仔 did this correctly; make it standard.
7. **Where an analyst overrides a colleague's stated probability, require new evidence to be
   cited for the override** (B-3).

---

## 6. Fitness for committee

**FIT FOR COMMITTEE — with five conditions.**

The recommendation on the table is **no position / watchlist with a dated catalyst**. The
portfolio holds **zero** INTC and INTC is **not in the watchlist**, so **no capital is at
risk and no exposure needs defending.** The evidentiary bar for "do not buy a stock we do
not own" is low, and this package clears it comfortably — the conclusion survives the
deletion of every flag I raised. Had the recommendation been **BUY at $91.68**, the same
flags (V-2, V-4, C-1, F-1) would have required a FAIL and a rebuild.

**Conditions:**
1. **Correct C-1 before the meeting.** The "~105x forward earnings" must be derived or
   deleted from both 菲比斯's §6 and 𢦀鳩仔's scorecard rationale. It is ~2x wrong.
2. **Correct F-1 before the meeting.** 巴爺爺's "~$40B annualized OCF" → **~$28B**, and
   re-word the self-funding conclusion accordingly.
3. **Present the 12/100 alongside 巴爺爺's 55 and 修大哥's 62, with the explicit statement
   that the valuation score is ~60% determined by price ÷ FV** and therefore does not
   measure business quality. Minute 𢦀鳩仔's own finding that INTC is the first improving
   business of the five.
4. **Minute the coverage gap.** Six of ten departments did not report — Macro, Geopolitics,
   Industry, Management Quality, Technical/Order Flow/Market Structure, and Social
   Sentiment. **These are not randomly missing: they are systematically where the bull case
   lives** (18A execution durability, shortage persistence, the political underwriting of
   14A, Lip-Bu Tan's credibility, and the "post-blowoff correction within an intact uptrend"
   read). A 3-agent core team is **not neutral with respect to this answer.** The most
   constructive score in the package (62) came from the only non-Department-2 agent.
5. **Do not treat the 12/100 as a quality judgement, and do not log this decision to
   `memory/decisions/` as "fifth consecutive low-quality business."** Log it as
   *"improving business, price-unsupported, revisit below $45 or on the Q3'26 print."*
   The precise wording matters for the sixth name.

**Also required before any future sizing (not before this committee, since no position is
proposed):** a live quote (my resolution of $91.68 is corroborated but derived from
secondary extraction), and a direct 10-Q read once proxy egress is restored — specifically
net PP&E (B1), consolidated GAAP operating income (V-4), total stockholders' equity at
27 Jun 2026 (V-2), and receivables/inventory vs revenue growth (巴爺爺's own open item — a
+25% revenue quarter is exactly where channel stuffing would hide, and nobody has checked).

**Note on confidence tier for the whole package:** every primary source was 403-blocked for
all four analysts **and for me**. Everything here is search-extraction of primary documents,
one notch below a direct read. The Q2 headline figures are corroborated across four to six
independent outlets and I regard them as solid. **The balance-sheet and segment-detail
figures are single- or double-sourced from aggregators and summarisers and should carry a
visible confidence discount in committee.** The three analysts disclosed this constraint
prominently and unprompted, which is the correct behaviour and should be credited.

---

## 7. Flag register

| ID | Report | Severity | Flag | Conclusion-changing? |
|---|---|---|---|---|
| **B-1** | 𢦀鳩仔 / firm-wide | **HIGH** | Valuation score ~60% determined by price÷FV, with a 20% binary-zero gate; contradicts the author's own text; explains all five rejections | No — but corrupts the institutional record |
| **F-1** | 巴爺爺 | **HIGH** | "~$40B annualized OCF" unsupported, ~43% overstated, load-bearing to "Intel can self-fund" | No (H1 fact supports it independently) |
| **C-1** | 菲比斯 → 𢦀鳩仔 | **MED-HIGH** | Uncited "~105x forward earnings," ~2x irreconcilable with the package's own 55x; propagated into the headline scorecard | No |
| **V-1** | 𢦀鳩仔 | MED | 71–143M escrowed shares likely double-counted in the denominator | No (−$0.70/sh, against himself) |
| **V-2** | 巴爺爺 → 𢦀鳩仔 | MED | `[UNVERIFIED]` equity re-labelled "verified"; aggregator source, Q1 date, unreconciled NCI | No (works against his conclusion) |
| **V-4** | 𢦀鳩仔 | MED | $20B corporate deduction inferred from an unretrieved consolidated line; pre-tax cost at 10x vs after-tax NOPAT at 12x; includes non-cash amortisation | No ($3.69/sh) |
| **C-2** | 菲比斯 / 𢦀鳩仔 | MED | ROIC dispute superseded rather than resolved; framework handed down then validated; 2.45% single-sourced to GuruFocus | No (invariant across all readings) |
| **C-3** | 修大哥 | MED | Sovereign capital "~$12B" vs the correct $15.9B; understates the bull's best solvency datapoint | No |
| **B-2** | package | MED | Capital-structure reflexivity acknowledged then dropped; largest unpriced bull item | Unquantified — bounded upside |
| **B-3** | 𢦀鳩仔 | MED | P(14A) marked down 50% → 30% on a fact that carries no information before the decision date | No (+$4.80/sh) |
| **F-2** | 巴爺爺 | MED | Intraday range "$86.94–$94.98" for 27 Jul uncorroborated and inconsistent with independent quote data; hallucination pattern | No (unused) |
| **F-1b** | 巴爺爺 vs 修大哥 | MED | $91.68 close and "+343%" asserted as fact where the sibling report marked both unverified | No (both now corroborated) |
| **N-1** | 修大哥 | MED | Missed 2026-07-23 "Fortinet deal" external-foundry headline; "zero committed customers" needs the "14A / high-volume / non-strategic" qualifier | No |
| **C-4** | 巴爺爺 → 𢦀鳩仔 | LOW-MED | 2023 share base ~4.15B `[UNVERIFIED]` (菲比斯 says 4.23B) carries a headline "+30% dilution" claim untagged | No |
| **N-2** | 修大哥 | LOW-MED | Scorecard hand-adjusted 60.1 → 62 | No |
| **M-1** | 菲比斯 | LOW-MED | Market cap given as "$413–464B"; $413B does not reconcile at ~5.04B shares × ~$92 and appears stale | No |
| **V-3** | 𢦀鳩仔 | LOW | Warrants priced in although their trigger is an explicitly excluded assumption (mechanics correct, conditionality wrong) | No (+$0.30/sh) |
| **V-6** | 𢦀鳩仔 | LOW | Mobileye economic ownership 86% vs ~80% implied by the 2026 proxy (properly tagged as estimate) | No (−$0.06/sh) |
| **V-7** | 𢦀鳩仔 | LOW | Bear floored at $0–10 in text, weighted at −$0.43 in arithmetic | No (−$1.63/sh, against himself) |
| **M-2** | 菲比斯 | LOW | "GAAP EPS anti-correlated with share price" — mechanism correct, unconditional phrasing overstated | No |
| **S-1** | 巴爺爺 | LOW | 5,083M basic (weighted-avg) exceeds 5,023M outstanding at the same date; one is mislabelled | No |

---

*Audit only. The auditor's own claims are sourced above; where I estimated rather than
fetched, I said so. Committee and Owner decide. Not financial advice.*

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
