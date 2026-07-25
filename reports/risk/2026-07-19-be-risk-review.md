# Risk Review — Prospective NEW LONG: BE (Bloom Energy Corp.)

**Author:** John, Chief Risk Officer (Dept. 6 — Risk Management)
**Date:** 2026-07-19 (written 2026-07-25) · **For:** Investment Committee / CEO 皮褸黃 / Owner
**Price context:** **$214.96** (Fri 2026-07-17 close). Market cap **~$61.14bn**; **284.44m** shares
outstanding, **319.7m diluted** (Q1'26). **No stock split** — the ~+700% to +1,100% twelve-month
re-rating is **real and verified** by 巴爺爺 on three independent checks (cap ÷ shares reconciles
to the quoted price; the Nov-2025 0% convert struck at **$194.97** mathematically requires a
$140–156 spot at issue; the sell-side band has repriced to $193–346). The stale "$10–100 stock"
prior is purged. BE may be **~39% below a 52-week high of $351.28** (third-party, **unverified**);
修大哥 puts the late-June peak in the **$335–351** band and the drawdown into 17 Jul at **~35–40%**
— *the level is contested, the shape is not.*
**Binary event:** **Q2 2026 earnings, Tue 2026-07-28 — options implying a ~32.4% move**, against a
trailing four-quarter average post-earnings move of ~12.04%. **This is the largest single-name
event binary in the entire pipeline**, roughly 4x KLAC's ±8% and 3.5x MU/MRVL.

**Inputs reviewed:** `config/risk-limits.yaml`, `config/portfolio.yaml`; 菲比斯 (moat **NARROW**,
cyclically widening → erosion 2029–2031; ROIC test **FAILED on history, UNPROVEN forward**;
demands **60% MoS** and a **hard 1.5%-of-NAV position cap**); 巴爺爺 (financials **67/100, grade
B–**; **accounting quality sub-score 3/10**); 修大哥 (news **68/100**, OVERWEIGHT theme at 6/10
confidence, and the portfolio warning quoted in §4); The dictator (regulatory **net TAILWIND** —
48E ITC restored — with an active FEOC/litigation overlay).

**Inputs MISSING — and this is itself a finding (§6):** 𢦀鳩仔 **valuation — none on file**;
老詹 **technical / invalidation level — none on file**; Tim Cook market structure / ADV — none;
王老吉 flow — none; Peter management quality — none; Peterson macro — none; LeBron James
geopolitics — none; **Mo Peter VaR — none**; **Mario stress — none**. **BE has four of roughly
thirteen pipeline inputs on file.** MU, MRVL and KLAC each arrived at my desk with a complete set.
BE has not.

**Precedent applied:** `2026-07-18-mu-risk-review.md` (APPROVED WITH CONDITIONS, 6.5% ceiling,
38/100), `2026-07-19-mrvl-risk-review.md` (VETOED on valuation, 5.0% ceiling, 24/100),
`2026-07-19-klac-risk-review.md` (VETOED on valuation, 8.0% ceiling, 31/100). Identical
gap-adjusted sizing method and identical valuation-gate logic are applied here.

---

## VERDICT: **VETOED** — for initiation at $214.96, and for any entry ahead of the 2026-07-28 print

The proposal does **not** proceed to committee as a live buy. Three independent gates fail, and
**each one is sufficient on its own**:

1. **Process gate — FAILED (hard).** `stop_required: true` is law and there is **no invalidation
   level on file** for BE, because 老詹 has not covered the name. I cannot approve a position
   whose stop does not exist. There is also **no valuation report** on a name whose own moat
   analyst demands a **60% margin of safety**, and **no VaR and no stress test** on the
   highest-volatility name the firm has looked at. This is not a close call; it is an incomplete
   file.
2. **Valuation gate — FAILED (by inference, and the inference is not marginal).** 𢦀鳩仔 has not
   filed, so I use the only valuation-adjacent work on the desk — 菲比斯's implied-expectations
   check: at EV ~$61.6bn, a 20x terminal EV/EBIT implies **~$3.1bn of steady-state EBIT**, i.e.
   **~$20bn of revenue at a generous 15% through-cycle EBIT margin — roughly 6x the FY2026 guide
   and 4–6x the 2 GW capacity Bloom is spending to reach by end-2026, in perpetuity, with no
   margin compression when turbines free up.** His conclusion, quoted: *"the current price
   contains no margin of safety at all — it prices the wide-moat branch at close to 100%
   probability against my 25–30%."* His buy rule is **≤40% of appraised value**. There is no
   reading of the file in which $214.96 satisfies a 60% MoS hurdle. **I vetoed KLAC — the best
   business in the pipeline, WIDE/WIDENING moat, grade-A 91/100 financials, ~43% ROIC, the lowest
   volatility of the four — at a −188% MoS. BE is a narrow, cyclically-widening moat that has
   never earned its cost of capital in 25 years, with a 3/10 accounting score and no valuation
   report at all. Approving BE after vetoing KLAC would be incoherent.**
3. **Event gate — FAILED for any pre-print entry.** A **~32.4% implied move nine days out** is not
   a risk to be sized around at initiation; it is a coin flip the firm has no edge on. 修大哥, the
   most constructive analyst on the name, says it himself: *"I would not treat a 68 as actionable
   for initiating size before that print."* No material size goes in front of a binary of this
   magnitude. This gate expires on 2026-07-28 — the other two do not.

**What this veto is NOT.** It is not a rejection of the theme. The interconnection bottleneck is
physical, measurable and multi-year (~2,600 GW queue; PJM interconnection >8 years; GE Vernova
116 GW backlog against ~10 GW/yr capacity). It is not a solvency call — the balance sheet is
genuinely strong (§3). It is a refusal to initiate a position at a price with no margin of safety,
with no stop, with no valuation, with half the research file missing, nine days before a 32%
binary, in a company where **44.1% of FY2025 revenue and 73.8% of Q4'25 revenue was booked to
related parties.**

---

## 1. Sizing arithmetic — what the 1% per-trade budget actually supports

Per-trade law: `max_risk_per_trade: 0.01` — weight × distance-to-stop ≤ 1% of portfolio.

**Realized volatility on file (all from 修大哥's sweep, dated):** −12% intraday 8 Jul (Hunterbrook);
+6% 9 Jul (8-K rebuttal); **>−12% 26 Jun** (FCEL upgrade rotation); ~+12% extended-hours 30 Jun
(Brookfield $25bn); **16 Jul opened ~$228, closed $206.73** (~−9% on the session; one outlet
reported −14%) **on unambiguously good news** — a $1.7bn financed order that could not hold a bid.
Peak-to-17 Jul: **−35% to −40% in about three weeks.** BE routinely prints **9–14% single
sessions**. For calibration: KLAC 4–7%, MU/MRVL ~9%. **BE is roughly 2x the daily-shock magnitude
of the worst semiconductor name in the pipeline and 2.5–3x KLAC.**

| Sizing basis | Effective loss distance | Max size under the 1% rule |
|---|---|---|
| Nominal close-basis stop (hypothetical ~10%; **no 老詹 input exists**) | ~10% | 10% — cap binds. **REJECTED basis: no stop is on file** |
| Gap-adjusted, non-earnings regime (a ~10% close stop compounds with 9–14% shocks to a ~20% realistic fill) | ~20% | **5.0%** |
| Earnings-inclusive, at the implied move | ~32% | **3.1%** |
| Earnings tail (~1.5x implied — plausible on a name that fell 39% in three weeks) | ~46% | **2.2%** |
| **Accounting/restatement branch — the stop does not execute** (gap-to-halt, −70% to −90%) | **~80%** | **1.25%** |

**Reading the table.** Every stop-based row is optimistic, because each assumes the stop *works*.
Rows 2–4 are the honest price-risk answer: **2.2%–5.0%** depending on whether the position
straddles the print. Row 5 is the answer that governs, and it is the one the desk must internalise:
**against a restatement, a filed complaint with specific accounting allegations, or a trading halt,
a stop is not a control. Price does not travel through those levels — it teleports past them.**
The only instrument that works is notional size.

**Reconciling with 菲比斯's cap.** He imposes **1.5% of NAV**, explicitly on the ground that the
related-party structure risk *"is managed by position size, not by price."* My stop-based math
gives 2.2%–5.0%; his cap is tighter, so **his cap binds**. My accounting-branch math independently
gives **1.25%** — tighter still, because I price a control failure he did not have to price.

> ### **Operative ceiling for any future BE proposal: 1.25% of NAV at cost.**
> **Pre-print / unresolved-accounting tranche: ≤ 0.40% of NAV.**

The lowest ceiling the firm has ever set. Cross-check at 1.25%: a full **−85% restatement outcome
costs 1.06% of portfolio** — 5.3% of the entire 20% drawdown budget, survivable, and the firm
continues. **At the 10% single-position cap the same event costs 8.5% of portfolio — 42.5% of the
firm's entire survival budget on one name.** That contrast is the whole argument for the cap.

---

## 2. Limit-by-limit check

`config/risk-limits.yaml` as at 2026-07-19. Book is empty (`holdings: []`, `cash_balance: 0.00`).
Post-trade columns show (a) the naive 10% single-position cap and (b) my 1.25% operative ceiling —
**both for completeness only; the position is vetoed at this price and on this file regardless of
size.**

| Limit | Law | Current | Post @10% (naive) | Post @1.25% (ceiling) | Pass/Fail |
|---|---|---|---|---|---|
| `max_single_position` | 10% at cost | 0% | 10.0% | 1.25% | @10% at limit / @1.25% PASS |
| `max_single_position_drifted` | 15% trim trigger | n/a | live at 10% | headroom to 15% | n/a at inception |
| **`max_risk_per_trade`** | **1% (size × stop)** | n/a | earnings-gap **3.2%**; restatement branch **8.0%** — **FAIL by 3–8x** | earnings-gap 0.40%; restatement 1.06% (marginal) | **@10% HARD FAIL / @1.25% PASS** |
| **`stop_required`** | **yes** | n/a | **none exists — 老詹 has not covered BE** | same | **FAIL — no invalidation level on file** |
| `max_sector` | 35% | 0% | 10% | 1.25% | PASS on the GICS label — **but see §4, the label is wrong** |
| **`max_correlated_cluster`** | **40% (AI complex)** | 0% | 10% → cluster 16.5% with MU | 1.25% → **cluster 7.75% with MU** | PASS numerically — **§4 is where the real finding is** |
| `cash_floor` | ≥10% | **unverifiable — cash 0.00** | ~90% | ~98.75% | PASS on assumption; **unverifiable until Owner populates the file** |
| `leverage` | none | none | cash purchase required | cash purchase required | PASS conditional |
| `max_var_95_1d` | ≤3% | 0% | ~1.16% (est.) | ~0.14% (est.) | PASS (estimate) — **no Mo Peter run; see note below** |
| `max_adv_participation` | ≤5% $ADV | n/a | **ADV unverified — no Tim Cook report** | same | **UNTESTED** |
| `max_drawdown` budget | 20% peak-to-trough | fresh book | −60% = −6.0% (30% of budget); −85% = −8.5% (**42.5% of budget**) | −60% = −0.75%; −85% = −1.06% (**5.3%**) | **@10% imprudent / @1.25% acceptable** |
| `naked_short_options` | forbidden | — | — | — | see Condition 9 |
| `max_options_premium_at_risk` | 2% aggregate | 0% | — | — | see Condition 9 |
| `committee_approval_required` | yes | — | this review is the risk input | same | Pending |
| `decision_record_before_ticket` | yes | none | required | required | Pending |
| `live_trading` | forbidden | — | ticket-only | ticket-only | PASS |

**VaR note (estimate, not a Mo Peter figure).** Single-session shocks of 9–14% imply a daily σ of
roughly **7%**; 95% 1-day VaR ≈ 1.65 × 7% ≈ **11.6% of position value**. At 1.25% NAV that is
~0.14% of portfolio; even at a naive 10% weight it is ~1.16% — **still inside the 3% ceiling.**
**That is a limit-design finding, and I am flagging it rather than hiding behind it:
`max_var_95_1d` at 3% does not bind on a single-name position of any size the firm would sensibly
take. A portfolio-level VaR ceiling is structurally blind to concentrated single-name tail risk,
and it is blind by construction to jump risk — a normal-vol VaR does not model a 32% implied
binary at all.** The controls actually protecting the firm on BE are `max_risk_per_trade` and the
position cap, not VaR. Any Mo Peter run commissioned on this name **must model the 28 Jul jump
separately** and must report a jump-diffusion or scenario VaR alongside the normal-vol number,
or it will produce a comfortable and meaningless figure.

**The two cells that decide this review** are `stop_required` (**FAIL — no stop exists**) and
`max_risk_per_trade` (**HARD FAIL at any size above ~2%**). Neither is curable by argument; one is
curable by 老詹 filing a report, the other by size.

---

## 3. Accounting & related-party risk — assessed as a DISTINCT risk category

The brief asks me to treat this separately from price risk and volatility risk. It is right to, and
this is the most important section of the review.

**The facts on file (not allegations — reported figures):**
- FY2025 related-party revenue **$892.0M = 44.1% of total**, of which **$862.1M from Brookfield
  "Fund JVs" that did not exist before August 2025** (菲比斯, from the FY2025 10-K).
- **Q4 2025: $574.2M of $777.7M = 73.8% related-party.** Q1 2026: ~$373M of $751.1M ≈ 50%.
  Q1'26 Brookfield-JV sales were **$373.3M against $2.8M a year earlier** (修大哥).
- Bloom booked a **$19.6M equity loss on the unconsolidated Brookfield AI-infrastructure affiliate
  against an initial investment of only $24.6M** — ~80% of the stake, in a partial period.
- Separately, **$288M = 55.5% of Q3 2025 revenue reportedly to SK ecoplant**, a **10.5%
  shareholder** — 巴爺爺 flags this as **unverified**; he could not open the primary filing.
- **FY2025 OCF is disputed at the figure level**: company **$418.1M** vs Sheephill Group **$114M**,
  "almost entirely non-cash add-backs," with FCF ex-SBC at **−$82M**. 巴爺爺 could not reconcile
  and explicitly declines to pick a side.
- **Accounts receivable and inventory could not be obtained for any period** — the single most
  diagnostic test for a hardware business growing 130% is simply absent from the file.
- **Prior restatement:** FY2018–Q3 2019 restated 12 Feb 2020 over Managed Service Agreement
  accounting, after Hindenburg; $3.0M class-action settlement, final approval May 2024.
- **Live:** Hunterbrook 8 Jul 2026; company 8-K rebuttal 9 Jul; **Rosen Law and Kessler Topaz
  investigations open** (no complaint filed as at the reference date).
- 巴爺爺's accounting-quality sub-score: **3 out of 10.** The lowest sub-score he has issued to any
  name in the pipeline, and he states it is deliberate.

**Why this is not price risk.** Price risk is the risk that a correctly-measured business is
worth less than you paid. This is the risk that **the measurement itself is wrong** — that the
revenue base is not what it appears. 菲比斯 names the mechanism precisely: Bloom books ~30% gross
margin selling equipment into a vehicle it part-owns, then takes the vehicle's losses back through
the equity line. That is *"the signature of a financing structure being reported as demand."*
The **$25bn Brookfield commitment must be read as a capital facility, not an arm's-length order
book.** I make no allegation of impropriety and neither does he — this may be entirely proper
project finance, properly disclosed. **But the firm cannot currently state what the arm's-length
revenue base is, and that is a different problem from disagreeing about a multiple.**

**Is it sizeable-around? Partially — and the honest answer has two branches.**

- **Branch A (the likely one, call it ~85–90%): the structure is legitimate and correctly
  reported.** The risk then expresses as a **quality discount** — the market eventually
  re-underwrites related-party revenue at a lower multiple. Loss −50% to −70%, delivered over
  weeks-to-quarters, **through prices a stop can actually trade against.** This branch **is**
  sizeable-around: at 1.25% NAV a −70% outcome costs 0.88% of portfolio.
- **Branch B (low probability, non-trivial): a restatement, a material-weakness disclosure, an
  auditor change, an SEC comment letter, or a filed complaint with specific revenue-recognition
  allegations.** Loss −70% to −90%, delivered **discontinuously**, quite possibly through a
  trading halt. **A stop provides no protection whatsoever in this branch.** The probability is
  low, but it is *materially higher than the base rate* for one specific and unavoidable reason:
  **this company has already restated once, over exactly this family of issue — off-balance-sheet
  and related-party structures — and 巴爺爺's judgement is that it therefore has "no credibility
  buffer."** Branch B is sizeable-around **only** at notional so small that no stop is needed.

**My conclusion — a hybrid, and I want the committee to hear the distinction clearly.**
It is **not a permanent stand-aside**; a fraud-adjacent *structure* risk with no allegation
attached is exactly what position caps exist for, and 菲比斯 is right that this is managed by size,
not by price. **But it is a stand-aside on the *current file*, for a reason that is about the
firm's process rather than about Bloom:** three of the highest-information items in the accounting
file are **unresolved by our own analyst's admission** — the >55% related-party quarter is
unverified, the FY2025 OCF figure is *disputed at the figure level*, and AR/inventory were never
obtained. **The desk does not initiate a position where its own financial-statements analyst has
been unable to open the primary statements.** That is a data-integrity gate, and it is cheap to
clear: the FY2025 10-K and the Q3'25 10-Q are public documents, and the Q2 print on 28 Jul
publishes the deciding line. **Clear the gate, then size to 1.25% — do not size around a
measurement you have not made.** Note also that 巴爺爺's own scoring band says confirmation that
related-party revenue exceeds 50% of a quarter takes the financial score **to 45 or below** — and
Q4'25 is *already* reported at 73.8%.

---

## 4. Correlation & concentration — is the firm building a one-factor book?

**Yes, and BE is the name that would prove it.**

**The finding.** 修大哥's warning is the single most important portfolio-level sentence produced by
any department in this batch, and I adopt it as a binding risk finding, not as commentary:

> **"BE is the highest-beta expression of the same AI-capex factor as MU/MRVL/KLAC — not an
> energy-sector diversifier, it's the same trade with a different label."**

Four names, four sector labels — memory semiconductors, networking silicon, semicap equipment,
and *electrical equipment / industrials*. **One funding source: hyperscaler and neocloud capex
budgets.** MU sells HBM into AI accelerators. MRVL sells custom AI silicon. KLA sells the process
control that builds the wafers. Bloom sells the electricity that runs the racks. If hyperscaler
capex guidance is cut by 20%, all four re-rate together, and realized correlation in that drawdown
converges toward 0.8–0.9 regardless of what the GICS field says. **Nominal diversification across
four correlated names is concentration in disguise — this batch is one bet wearing four labels.**

BE is not merely *in* the factor; 修大哥 establishes it is the **highest-beta expression** of it,
for four specific reasons: the highest multiple of the four (~30x trailing P/S); revenue
concentrated in a handful of *named* counterparties (Oracle, Brookfield JVs, AEP, Nebius) rather
than diversified end-markets; an order book heavily composed of **"up to X GW" options that can be
quietly unexercised without ever producing a cancellation headline**; and **Nebius-type neocloud
customers who are themselves capital-markets-dependent** — i.e. a second-order funding beta stacked
on top of the first.

**The cluster arithmetic.** Against `max_correlated_cluster: 0.40`:

| Name | Status | Ceiling | Cluster contribution |
|---|---|---|---|
| MU | APPROVED WITH CONDITIONS | 6.5% | 6.50% |
| MRVL | **VETOED** (valuation) | 5.0% | 0% live |
| KLAC | **VETOED** (valuation) | 8.0% | 0% live |
| BE | **VETOED** (this review) | 1.25% | 0% live |
| **Live cluster today** | | | **6.50%** |
| *If all four ever cleared at ceiling* | | | **20.75%** — inside 40% |

The cluster cap is not the binding constraint today and would not be even in the maximal case.
**But the cap passing is not the same as the firm being diversified**, and I will not let a green
cell in a table create false comfort. Two structural findings follow.

**Finding A — a factor-tagging rule, binding on Morris, So Ma and Zac.** BE must be tagged to the
**AI-capex cluster from inception**, irrespective of its GICS sector, its "energy" label, or which
sleeve it is funded from. If BE were booked to an energy or industrials sleeve and netted only
against `max_sector`, the firm would carry a fourth position in its single largest factor while
its own control framework reported it as diversification. **That is precisely the failure mode the
40% cap exists to prevent, and a naive sleeve-tagging would defeat it silently.** The same rule
applies prospectively to GEV, VRT, ETN, CEG, VST, NBIS, and any other "power for AI" name.

**Finding B — escalation to the Owner: the target allocation conflicts with the correlation cap.**
`config/portfolio.yaml` targets **ai 0.30 + technology 0.20 = 0.50**. `config/risk-limits.yaml`
sets **`max_correlated_cluster: 0.40`**. **If the technology sleeve is populated with AI-capex
names — which, on the current watchlist and this batch, it would be — then hitting the target
allocation breaches the correlation cap by 10 percentage points.** The targets and the limits are
not mutually consistent. I am not bending either: I am reporting the conflict and proposing that
the Owner either (i) lower the combined ai+technology target to ≤40%, (ii) raise
`max_correlated_cluster` with explicit acknowledgement of the factor concentration, or
(iii) mandate that the technology sleeve be filled only with names that are *not* AI-capex-funded.
**Until the Owner rules, I will enforce the 40% cap as the binding constraint and treat the
targets as aspirational.**

**Second-order correlation notes.** (a) BE swaps the semis' Taiwan-strait tail for a **China
rare-earth (scandium) tail** — different geography, same "single chokepoint in an adversarial
jurisdiction" structure, and **no LeBron James geopolitical report exists on BE**, which is a
conspicuous gap on a name whose central short thesis *is* a China-supply-chain claim.
(b) A **FEOC/48E cross-link** could impair **customers'** 30% ITC eligibility — a risk vector that
runs through demand, pricing, *and* the revenue-recognition and collectability assumptions on
already-booked contracts. That makes the regulatory risk and the accounting risk **the same risk**,
which is unusual and which I have not seen elsewhere in this pipeline. (c) 26 Jun is instructive:
BE fell >12% because Jefferies upgraded **a competitor**. Capital rotating between names inside
one crowded theme is late-stage thematic behaviour, and it means BE's idiosyncratic risk includes
*other companies' news*.

---

## 5. Conditions — binding on any FUTURE resubmission (this is not an approval now)

All of the following must be satisfied. Absent any one, the veto stands. Conditions 1–5 are
binding on Zac and 死潘狗 without further discussion.

1. **Event gate.** **No entry before the close on 2026-07-28.** A ~32.4% implied move is not
   sizeable-around at initiation. This condition expires the moment the print is out and is the
   only condition here that does.
2. **Data-integrity gate (§3) — the gate that is unique to this name.** Before *any* size, the
   desk must obtain and reconcile, from primary documents: (a) **related-party revenue as a % of
   total for Q2 and 1H 2026**, versus Q4'25's 73.8% and Q1'26's ~50%; (b) the **FY2025
   consolidated statement of cash flows**, resolving the **$418.1M vs $114M** dispute line by line
   (SBC, working capital, debt-related charges); (c) **accounts receivable and inventory versus
   revenue growth** — the diagnostic 巴爺爺 calls the largest hole in his report; (d) **actual
   capex** and any shift toward operating leases or contract manufacturing; (e) **contracted
   backlog with take-or-pay terms**, separated from the Brookfield "commitment" headline. Per
   菲比斯: **do not size up before the disclosure shows related-party revenue declining as a
   percentage of total.** If Q2 confirms related-party revenue above 50%, 巴爺爺's own scoring band
   takes the financial score **to ≤45** and the name returns to me for a fresh veto.
3. **Valuation gate.** 𢦀鳩仔 must file a full valuation with a three-scenario probability weighting
   (菲比斯's suggested Wide 30% / Narrow-fading 45% / None 25%). Entry must satisfy 菲比斯's
   **60% MoS — buy only at ≤40% of appraised value**, with his test that **the bear/"None" case
   still returns ≥0% from the entry price.** His None-case anchor: normalised 2030 revenue at
   ~2 GW/yr, 20% gross margin, 12% NOPAT margin, ~2.5x EV/Sales. **No initiation at $214.96.**
   A strong Q2 print does not clear this gate; only a materially lower price or a materially
   higher appraised value does, and per 菲比斯 the re-rating must come from cash-flow facts,
   not multiple expansion.
4. **Stop must exist before size does.** 老詹 files a technical report with a **close-basis
   invalidation level** re-derived at whatever future price clears gate 3. `stop_required: true`
   is not waivable. **And the committee must understand what the stop does and does not cover:**
   it protects Branch A of §3; it is **worthless against Branch B.** Notional size is the only
   control that covers both.
5. **Size.** Total BE ≤ **1.25% of NAV at cost** (my accounting-branch-adjusted ceiling; tighter
   than 菲比斯's 1.5%, and the tighter binds). Any tranche entered before gate 2 is fully cleared:
   ≤ **0.40% of NAV**. Staged entry in thirds. **No averaging down through the stop, ever, and
   specifically no averaging down into a disclosure event** — adding to a position whose
   measurement is in question is the exact behaviour that converts a small loss into a
   career-ending one.
6. **VaR and stress.** Mo Peter files a 1-day 95% VaR that **separately models the earnings jump**
   (a normal-vol VaR on this name is worse than useless — see §2). Mario runs a joint
   **MU + BE (+ MRVL/KLAC if either ever clears)** scenario covering: (i) hyperscaler AI-capex
   guidance cut of 20–30%; (ii) BE-specific restatement / material-weakness / halt; (iii) FEOC
   guidance impairing customer ITC eligibility on booked contracts; (iv) the scarcity window
   closing early via a GE Vernova capacity surprise. Both filed in `reports/risk/` before any
   decision record.
7. **Liquidity.** Tim Cook verifies BE's $ADV against `max_adv_participation: 0.05`. Currently
   **untested** — no market-structure report exists on this name.
8. **Portfolio data first.** Owner populates `config/portfolio.yaml` with real `cash_balance` and
   holdings. Every figure in this review is a **fraction of an unknown denominator.** Cash-funded
   only; `leverage: none`.
9. **Options — an explicit prohibition, because the temptation here is obvious.** A ~32% implied
   move makes BE premium look extraordinarily rich, and someone will propose harvesting it.
   **Selling puts or strangles on BE into the 28 Jul print is prohibited.** Uncovered structures
   breach `naked_short_options: forbidden` outright; a *cash-secured* short put is technically
   compliant with `covered_only: true` but is **economically a leveraged long at a size far above
   the 1.25% cap**, and I will treat any such proposal as a cap breach and veto it on sight. Long
   premium only, within `max_options_premium_at_risk: 0.02`, separately priced and separately
   signed off by me.
10. **Factor tagging (§4, Finding A).** BE tags to the **AI-capex cluster** from inception
    regardless of sector label, and is sized **jointly** with MU and any future MU/MRVL/KLAC/
    AI-power position against the 40% cap.
11. **Tripwires (assigned, monitored from now — the name stays on watch even under veto).**
    The dictator + 巴爺爺: Treasury/IRS **FEOC "material assistance"** guidance under 48E; any
    **filed** class-action complaint (converts headline risk to legal risk); SEC comment letter or
    subpoena; **auditor change or material-weakness disclosure**; any change in scandium /
    supply-chain disclosure language in the 10-Q. 修大哥: **new equity or convert issuance** —
    the stock is above the $194.97 conversion price and an opportunistic raise into post-earnings
    strength is live; **GE Vernova capacity commentary** (the clock on the scarcity window);
    competitor rotation (FCEL/PLUG). **Any tripwire firing re-opens the name from scratch.**
12. **Process.** Committee approval, then 腦大裝草 files the decision record in `memory/decisions/`
    including this veto and its reasoning as recorded dissent, then and only then an execution
    ticket for the Owner. **No live trading.**

---

## 6. Risk score (committee input): **18 / 100**

Scale: higher = more risk-acceptable to initiate *as proposed, at $214.96, on the current file*.
Pipeline ranking: **MU 38 · KLAC 31 · MRVL 24 · BE 18.** The lowest score the firm has issued.

**What earns it points above zero** — and these are real, not consolation:
- **The balance sheet is genuinely excellent and it is the strongest single argument in the file.**
  ~$2.52bn cash against ~$2.60bn debt = **net-debt-zero**; **0% coupon on ~96% of the stack**; **no
  maturity until 15 Nov 2030** — 4.3 years with no refinancing event; $600m undrawn revolver;
  **~$3.1bn total liquidity** against $150–200m of guided FY26 capex. 巴爺爺 scores it 13/15 and
  rates financing-need risk for the 2 GW ramp **LOW**. **The near-term bankruptcy tail is close to
  zero, and that is why this is a veto rather than an outright permanent exclusion.**
- Regulatory is a **net tailwind** (48E ITC restored under enacted law; EPA endangerment rescission
  removes the federal carbon tail on a gas-burning installed base), and it is being **underwritten
  by real money** — Morgan Stanley took sole tax-equity on the Nebius deal, which is a bank
  putting capital behind 48E eligibility on Bloom projects specifically.
- The demand bottleneck is **physical and measurable**, not narrative: ~2,600 GW interconnection
  queue, PJM >8 years, GEV 116 GW backlog against ~10 GW/yr. Customers are buying **schedule**, and
  they are the best-capitalised buyers on earth.
- Operating inflection is real: GAAP gross margin 27.5% → 29.0% → 30.0% across three periods, two
  consecutive positive-OCF years, and a **$184.3m y/y swing in a seasonally weak Q1**.

**What holds it to 18:**
- **Accounting quality 3/10** — the lowest sub-score in firm history, with a prior restatement over
  exactly this family of issue, an **unresolved dispute about the FY2025 cash flow figure itself**,
  **73.8% related-party revenue in Q4'25**, and AR/inventory never obtained.
- **A ~32.4% implied binary nine days out** — 4x KLAC's, on a name that already fell 35–40% in
  three weeks and where **good news stopped holding a bid on 16 July**.
- **No valuation report, no technical report, no stop, no VaR, no stress test, no management-quality
  report, no geopolitical report.** Four of ~13 inputs. **On process alone this is not
  committee-ready**, and the management-quality gap on a company with a restatement history, plus
  the geopolitical gap on a company whose short thesis is a China-supply-chain claim, are the two
  most conspicuous absences.
- **Never earned its cost of capital in 25 years**: $4.0bn accumulated deficit, FY25 ROIC ~2.2%,
  ~80x price-to-book on $769m of book equity — thin enough that a single large write-down consumes
  a material fraction of it. **+84.8% five-year diluted dilution**, +38.9% y/y.
- **A narrow moat its own analyst will not underwrite widening**, with erosion called for
  2029–2031, and only **25–30%** subjective probability on the wide-moat branch against a price
  that embeds it at ~100%.
- **The fourth position in a single factor**, and the highest-beta expression of it.

**Why below MRVL's 24.** MRVL arrived with a complete research file including a valuation carrying
a quantified MoS, a clean accounting record, a defined technical stop, and ~9% single-session
volatility. BE has a 3/10 accounting score, a 32% binary, 9–14% daily shocks, and half its file
missing. **MRVL was a veto about price. BE is a veto about price *and* measurement *and* process.**

**A 31/100 said of KLAC: "the name the firm should most want to own, at the wrong price."**
**An 18/100 says of BE: a real business inside a genuine bottleneck, wrapped in a revenue structure
the firm has not yet been able to measure, at a price that assumes the best branch, nine days
before a coin flip.** I am not moved by JPMorgan's $346, by the $25bn Brookfield headline, or by
the +1,100% twelve-month return — those are the market's assumptions, not the firm's findings.
**Upside is not my department. Survival is.** If gate 2 clears cleanly on 28 July and price comes
to the firm's value zone, BE returns to committee as a **≤1.25% NAV starter** — a real position,
deliberately small, and small *by design* rather than by timidity.

**Escalation to CEO 皮褸黃 and the Owner — three items:**
1. **STANDING (fourth repetition — MU, MRVL, KLAC, now BE):** `config/portfolio.yaml` is empty
   (`holdings: []`, `cash_balance: 0.00`). **No proposal from any department can receive an
   unconditional risk verdict while the denominator is unknown.** I can check limit *fractions*;
   I cannot check a single dollar, cannot verify the 10% cash floor, and cannot compute a real
   position size. Remediation: Owner enters holdings and cash; I re-certify the entire pipeline
   (MU, MRVL, KLAC, BE) against real numbers within one session. **This gap does not change today's
   BE verdict** — the veto rests on price, measurement and process, not on missing dollars — but it
   caps every other name at "conditional" and it has now been open across four consecutive reviews.
2. **NEW — limit-design conflict (§4, Finding B):** target `ai 0.30 + technology 0.20 = 0.50`
   exceeds `max_correlated_cluster: 0.40`. The firm's own targets, if achieved with AI-capex names,
   breach its own correlation cap. **Owner ruling requested.** I enforce the 40% cap in the interim.
3. **NEW — limit-design observation (§2):** `max_var_95_1d: 0.03` is structurally non-binding on
   single-name risk and blind to jump risk. I propose the Owner consider adding a **single-name
   contribution-to-VaR sub-limit** and a **stated stress-loss limit per position**, which would
   have bound where VaR did not. **Proposing, not bending** — the current limits stand until the
   Owner changes them.

---

*Limit citations: `config/risk-limits.yaml` and `config/portfolio.yaml` (2026-07-19). Market and
company figures are drawn from the cited 2026-07-19 department reports and carry their sourcing and
confidence flags; where those reports mark a figure unverified or disputed, it is marked so here.
Volatility-derived VaR, gap-adjusted loss distances, and the branch-loss magnitudes in §3 are my
estimates and are labelled as such. No allegation of wrongdoing is made against Bloom Energy, its
management, or its auditors; §3 assesses disclosed structures and unresolved third-party claims as
risk factors only. Research and decision support only — not financial advice; markets cannot be
reliably predicted.*
