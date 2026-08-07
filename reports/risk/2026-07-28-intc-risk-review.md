# INTC — Risk Review (pre-review of a prospective NEW LONG)

**John, Chief Risk Officer — Department 6, Risk Management · 皮褸黃 Capital**
**Reference date: 2026-07-28** · Price basis **$91.68** (close 27 Jul 2026, source conflict disclosed below)
**Status:** pre-committee risk pre-review. Fifth name in the current sequence (MU 38 · KLAC 31 · MRVL 24 · BE 18).

---

## VERDICT: **VETOED** — for initiation at $91.68, and for any initiation above the price gate in Condition 1

This is the fifth consecutive veto and I am uncomfortable with that fact, so I will
state the distinction that makes this one different rather than bury it:

> **The four prior vetoes were quality-and-price vetoes. This is a price-only veto on an
> improving asset.** 𢦀鳩仔 says so explicitly and I endorse it: *"INTC is the first name
> in this sequence where the operating fundamentals are genuinely improving. My negative
> conclusion here rests on price, not on the business."* 巴爺爺 grades it C+/55 — the
> second-highest financial score of the five, behind only KLAC. Every second derivative
> at Intel is positive.

**It does not change the verdict, and here is precisely why.** My department does not
underwrite direction; it underwrites loss distributions. The size of a loss is set by the
price paid against value, not by the sign of the fundamental trend. At $91.68 against a
prob-weighted fair value of $32.70 the loss distance to fair value is **−64%**, and to
the single most generous cell in 𢦀鳩仔's own sensitivity grid ($50.42) it is **−45%**.
Improving fundamentals do not shorten those distances. In one specific respect they
*lengthen* them: improving fundamentals are exactly what sustains a crowded momentum
position, and the unwind of a crowded momentum position is the most violent loss pattern
there is. The tape already demonstrated it — **−36% from the 52-week high in five weeks,
and −7.9% on a 2x EPS beat with an above-consensus guide.** When good news cannot lift a
stock, the marginal buyer is exhausted. That is a risk fact, not a research opinion.

What *does* change materially is **survivability**. With $29.7B of liquidity, investment-grade
debt termed to 2066, and a 9.9% sovereign holder, a small INTC position cannot go to zero.
BE could. MRVL could de-rate and deteriorate simultaneously. INTC can only underperform.
That is why this veto is **narrow, priced and time-boxed**, with a live conditional-approval
pathway (§7) rather than a flat "no." It is a veto on *this price at this size before this
binary resolves*, not on the name.

**Risk score (committee input): 28 / 100.**

### Price-source conflict — my treatment
Four quotes appear for 27 Jul 2026: **$91.68** (used; cross-checked on two feeds), $91.88,
~$97.06 and ~$102; 修大哥 could only verify **$92.32 for 24 Jul** and flags the 27 Jul close
as UNKNOWN. Spread ~11%. **This does not change my verdict in either direction** — at $102
the loss distances widen (MoS −209%), at $91.68 they are as computed. But it is a live
control defect: *an 11% uncertainty band on the entry price is larger than the entire
position I would authorise even if I approved this.* Condition 4 addresses it.

---

## 1. Sizing — gap-adjusted method (answer to question (b))

Identical method to the KLAC and BE reviews. Two legal caps apply; I compute both and take
the tighter as operative.

### 1.1 The two statutory caps

| Cap | Config | Arithmetic | Max size |
|---|---|---|---|
| `max_single_position` | 0.10 | at cost, 10% of NAV | **10.00% of NAV** |
| `max_risk_per_trade` | 0.01 | 1% of NAV ÷ realistic loss distance | see §1.3 |

### 1.2 Establishing the realistic loss distance

There is **no stop level from 老詹** — Department 5 has not produced a chart read on INTC.
`stop_required: true` is therefore already failed (§2). For sizing purposes I derive a
provisional distance from observed price behaviour only; **no invented figures**:

| Observed | Value | Date / source |
|---|---|---|
| Single-session drop on a *beat* | **−7.89%** | 24 Jul 2026 (修大哥 §2.5; Yahoo/Motley Fool) |
| Single-session drop on a *sector* day | **−9%** (vs SOX −6.7%, AMD −7%) | 2 Jul 2026 (修大哥 §M6) |
| Intraday range, 27 Jul | $86.94–$94.98 = **8.77%** of close | 巴爺爺 market-data line |
| Drawdown from 52-wk high | **−35.6%** ($142.35 → $91.68) in ~5 weeks | 巴爺爺 / 修大哥 |
| 52-week range | $18.97–$142.35; **+343%** | 巴爺爺 |

A name that produces 8–9% single-session moves twice in a month has a daily sigma of
**~4–5% [ESTIMATE, derived from the four observations above; to be replaced by Mo Peter's
measured figure]**. A defensible nominal stop is therefore **≥2 sigma over several
sessions ≈ 15%**, i.e. **$77.93**. Anything tighter is guaranteed to be taken out by noise.

### 1.3 The four sizing branches

| Branch | Realistic adverse fill | Max size at 1% risk |
|---|---:|---:|
| Naive (stop assumed to fill at $77.93) | 15.0% | 6.67% |
| **Gap-adjusted, non-event regime** (a 15% stop compounds with routine 8–9% gaps to a ~22% fill) | ~22% | **4.55%** |
| **Gap-adjusted, event-inclusive** (quarterly print + the two known binaries: 14A commitment disclosure within two quarters, and the equity-raise fear cited as the #1 driver of the −7.9%) | ~30% | **3.33%** |
| **Valuation-reversion stress** (price converges to $50.42 — the *most generous single cell* in 𢦀鳩仔's sensitivity 7.1, i.e. Q2 shortage margin declared permanent AND an 18x multiple) | **45.0%** | **2.22%** |
| *Memo — full convergence to central FV $32.70* | *64.4%* | *1.55%* |

I size on the **valuation-reversion branch (45%)** rather than the event branch, because
unlike MU/MRVL/BE this name's dominant loss mode is not a business break — it is a
multiple de-rate that the tape has *already started* (−36% in five weeks). I do **not**
size on the full-convergence branch (64%), because a move to $33 is a multi-year
fundamental scenario, not a within-horizon stop distance; I carry it as a drawdown-budget
item instead (§2).

> ### **Operative ceiling for any INTC initiation: 2.00% of NAV at cost.**
> (2.22% from the binding branch, rounded down for tail buffer.)

**The operative ceiling is set by `max_risk_per_trade`, not by `max_single_position`.**
The 10% concentration cap is **non-binding by a factor of five** and must not be quoted to
the committee as "the limit." The 1% risk budget binds first, at 2.00%. Anyone proposing
a 5% or 10% INTC position is proposing a 2.3%–4.5%-of-NAV risk unit against a 1% budget —
a limit breach, not an aggressive expression of conviction.

For calibration against my own prior work: KLAC 8.00% · **INTC 2.00%** · BE 1.25%. INTC
sits between them because its solvency and liquidity are far better than BE's while its
volatility and price-to-value gap are far worse than KLAC's.

**Starter tranche if the gate in Condition 1 is ever cleared: 0.75% of NAV**, second
tranche only after the 14A binary resolves.

### 1.4 Liquidity / ADV
INTC is among the most liquid equities listed in the US and at any plausible firm NAV a
2.00% position is orders of magnitude inside `max_adv_participation: 0.05`. **I have not
verified an ADV figure this session and will not state one.** Marked UNVERIFIED; Tim Cook
must supply it before any ticket. Liquidity is the one dimension on which INTC is
unambiguously the best of the five names.

---

## 2. Limit-by-limit check

NAV is **undefined** (`holdings: []`, `cash_balance: 0.00`). Every percentage limit is a
fraction of a denominator that does not exist. I check fractions and mark the rest.

| # | Limit | Config | Current | Post-trade (at 2.00% ceiling) | Verdict |
|---|---|---|---|---|---|
| 1 | `max_drawdown` | 0.20 | undefined (no NAV, no peak) | INTC contributes ≤0.90% NAV at the 45% branch; ≤1.29% at full FV convergence | **CONDITIONAL PASS** — unmeasurable without NAV |
| 2 | `cash_floor` | 0.10 | `cash_balance: 0.00` | cannot be computed | **FAIL TO VERIFY** — 5th escalation |
| 3 | `leverage` | none | none | none required; unlevered cash purchase | **PASS** |
| 4 | `max_var_95_1d` | 0.03 | n/a | est. 1-day 95% VaR ≈ 7.4% of position ≈ **0.15% of NAV** standalone (σ≈4.5% × 1.645) | **PASS [ESTIMATE]** — Mo Peter must confirm |
| 5 | `max_single_position` | 0.10 | 0% | 2.00% | **PASS** (non-binding — see §1.3) |
| 6 | `max_single_position_drifted` | 0.15 | 0% | 2.00% | **PASS** |
| 7 | `max_sector` (GICS) | 0.35 | 0% | 2.00% Information Technology | **PASS** — but see defect D2 |
| 8 | `max_correlated_cluster` | 0.40 | 0% actual / **0.50 by policy target** | 2.00% | **PASS on actuals · FAIL on the config's own targets** — §3 |
| 9 | `max_risk_per_trade` | 0.01 | — | exactly 1.00% **only at 2.00% size**; 5.0% size = 2.25% risk | **PASS AT CEILING ONLY** |
| 10 | `stop_required` | true | **no 老詹 level exists** | provisional $77.93 is mine, not Department 5's | **FAIL** — hard, blocking |
| 11 | `max_adv_participation` | 0.05 | — | far inside, but figure not retrieved | **UNVERIFIED** |
| 12 | Options limits | naked forbidden / covered only / 2% premium | n/a | no options leg proposed | **N/A** |
| 13 | `committee_approval_required` | true | pre-review stage | pending | **PENDING** |
| 14 | `decision_record_before_ticket` | true | none | 腦大裝草 must log before any ticket | **PENDING** |
| 15 | `live_trading` | forbidden | — | ticket-only, Owner executes | **PASS** |

**Two hard failures block this trade independently of price:** #10 (no invalidation level
from Department 5) and #2 (cash floor unverifiable). Even if the Owner overrode the
valuation gate tomorrow, the trade could not lawfully be sized or ticketed today.

---

## 3. The cluster question (answer to question (a)) — **reinforced, not changed, and now materially worse**

### 3.1 The standing escalation, restated for the fifth time
`config/portfolio.yaml` targets **ai 0.30 + technology 0.20 = 0.50**.
`config/risk-limits.yaml` sets **`max_correlated_cluster: 0.40`**.

**The firm's own target allocation breaches the firm's own correlated-cluster limit by
10 percentage points, before a single share is bought.** This is not a drift problem that
rebalancing fixes; it is a policy document that is internally inconsistent with the law it
is supposed to obey. Four names in, nothing has changed.

### 3.2 What INTC adds — it does not diversify the cluster, it *thickens* it
修大哥's §5 is the most decision-relevant page in the whole INTC file and I adopt it
without amendment. The prior working assumption — that INTC, as a PC/server cyclical with
no HBM, no XPU, no WFE and no data-centre power kit, would *dilute* the AI-capex factor —
**is wrong on the evidence:**

1. **Realised correlation, measured in stress.** On 2 Jul 2026, the worst day of the
   selloff: **MU −13%, INTC −9%, AMD −7%, SOX −6.7%.** INTC fell *more* than the index and
   *more* than AMD. A hedge that loses more than the thing it is hedging is not a hedge.
   On 24 Jul it fell 7.9% partly on "durability of AI capex" — the identical factor.
2. **The bull case *is* the AI trade.** DCAI +59% is AI-server host-CPU attach; NVIDIA is
   both a $5B shareholder and the custom-Xeon partner; the entire foundry terminal value
   is AI wafers. You cannot own the upside case without owning AI capex. There is no
   version of "INTC works" that is not "AI capex continues."
3. **INTC and KLAC are anti-diversified against each other — same invoice, both sides.**
   Intel's capex going from ~$18B to **>$20B in 2026 and higher in 2027** *is KLAC revenue*.
   Holding both is not two positions in one cluster; it is **one position expressed twice**,
   and the second expression is negatively convex to the first: the event that makes INTC's
   thesis work (capex up) is the same event that makes KLAC's work, and the event that
   breaks one breaks both. This is the single most important line in this review after the
   verdict.
4. **What INTC does add is different risk, not less risk.** Sovereign cap-table
   entanglement, escrow-derivative mechanics, a contingent warrant block, a single-customer
   binary on 14A, and explicit equity-raise fear. These are **idiosyncratic and
   uncompensated** — they widen the loss distribution without narrowing the factor exposure.

> **Answer, plainly: INTC does not change my cluster escalation. It reinforces it and
> raises its urgency.** Adding INTC to a book targeted at 50% AI+tech is not
> diversification within an over-cap cluster; it is a fifth name loading the same factor
> while importing four new idiosyncratic risks. **Do not size INTC as a hedge, and do not
> let anyone present it as one.**

### 3.3 What the Owner should actually do — three concrete options, in my order of preference

**Option A (recommended) — replace exposure caps with a factor ledger and a risk-at-risk cap.**
Sleeve labels ("ai", "technology") are accounting fiction when the constituents are five
semiconductor names. Redefine the cluster on the *factor*, not the sleeve:

```yaml
concentration:
  max_correlated_cluster: 0.40
  clusters:                        # NEW — the mapping the config currently lacks
    ai_capex:                      # membership is by factor, not by sleeve label
      members: [NVDA, MU, KLAC, MRVL, INTC, AMD, AVGO, TSM, BE, ...]
      max_exposure: 0.40
      max_risk_at_risk: 0.02       # NEW — see D1 below
```

**Option B — cut the targets to make them legal.** `ai 0.25 + technology 0.15 = 0.40`,
recycling the 10pp into `etf` or `cash`. Cheapest fix, one line, available today.

**Option C — raise `max_correlated_cluster` to 0.50** with an explicit, signed
acknowledgement that the firm is running a 50% single-factor book. **I would not veto
this, but I will not propose it**, and if the Owner chooses it I require it recorded in
`memory/decisions/` as a deliberate risk-appetite expansion, not a housekeeping edit.

**In all three cases, one additional standing rule I am now formally proposing:**
a **joint cap on INTC + KLAC** of the lesser of their individual ceilings plus 50%, i.e.
**≤12% combined**, on the grounds in §3.2(3). Two sides of the same invoice must be sized
as one bet.

**What the Owner must NOT do:** approve INTC on the argument that it broadens the
semiconductor sleeve. That argument is now factually refuted by 修大哥's tape evidence and
I will treat any proposal built on it as a limit-circumvention attempt.

---

## 4. The dilution and warrant structure (answer to question (d))

### 4.1 The arithmetic

| Layer | Shares (M) | Note |
|---|---:|---|
| Outstanding, Jul 2026 | 5,040 | |
| Escrowed, not yet released | 143 | 71M contingently issuable, currently outside both basic and diluted EPS |
| **DOC warrants, $20.00 strike** | **241** | ~**$17.3B in the money** at $91.68; proceeds only $4.8B |
| **Fully loaded** | **5,424** | **+30% vs ~4.15B in 2023** |
| Escrowed Shares derivative liability | — | **$15.6B** at 27 Jun 2026, vs $2.7B at 27 Dec 2025 |

### 4.2 As a risk to equity holders — an *anti-convex* claim on the upside
The warrants deliver ~$17.3B of value for $4.8B of cash — a **~$12.5B net transfer from
existing holders, ~2.7% of the $464B market cap**, on top of ~4.6% share-count dilution.
Combined with the escrow derivative, the structure has a property I want the committee to
understand precisely:

> **The government's claims grow as the stock rises. The escrow liability went from $2.7B
> to $15.6B in six months *because the stock went up*. The warrants gain ~$241M of value
> for every $1 the stock advances.** Existing holders own an asset whose upside is
> continuously taxed by a sovereign counterparty and whose downside is not correspondingly
> subsidised.

And the most important correction I have to make to a claim that will be made in committee:
**"the government backstop protects the downside" is false as stated.** The government's
cost basis is **$20.47**; NVIDIA's is $23.28; SoftBank's is $23.00. Those holders are
protecting the *enterprise* against failure — they are not protecting a buyer at $91.68
against a 65% decline. The sovereign floor sits at roughly $20, which is 78% below the
proposed entry. It removes the bankruptcy tail. It does nothing whatsoever for the loss
distribution that actually threatens this book. Anyone citing the sovereign stake as
downside protection at $91.68 is confusing solvency risk with drawdown risk, and drawdown
is my department.

### 4.3 As a constraint on the value-unlock — the decisive point
The warrants are exercisable **only if Intel ceases to own ≥51% of Foundry.** That is a
poison pill aimed squarely at the single most commonly proposed value-unlock. Note the
asymmetry: **the cost of the unlock scales with the share price.** The better INTC does,
the more expensive it becomes to crystallise Foundry's asset value — at $91.68 the exit
toll is ~$17.3B; at $142 it would be ~$29B. The unlock gets further away as the thesis
works.

This is decisive for how I classify the name. 菲比斯 rates Foundry **NONE / stable** and
frames INTC as an **asset-value case, not a compounder**. 𢦀鳩仔 states outright that he
*cannot* value Foundry at a sale or spin price because of these warrants, and lists a
spin-off among his **deliberate non-assumptions**.

> **An asset-value thesis whose realisation route is contractually blocked is not an
> asset-value thesis. It is a hope with a balance sheet attached.** The risk classification
> that follows is: INTC is a **high-beta semiconductor operating-turnaround bet**, and it
> must be sized as one. It gets **no asset-backing credit** in my framework, and it gets
> **no "sum-of-the-parts floor"** in any committee presentation.

Supporting: 巴爺爺's red flag #5 — Foundry as a separate legal entity with standalone
financials — means the structure that *enables* an eventual Foundry IPO is the same one
whose majority sale triggers the warrants. Watch for any change in consolidation or segment
definition that resets the loss baseline; route to The dictator (Dept 4) for the CHIPS
Secure Enclave mechanics.

**Third dilution vector, live and near-dated:** 修大哥 records that fear of *another*
equity raise was among the explicit drivers of the −7.9% on 24 Jul. With capex guided
>$20B in 2026 and "significantly above" in 2027, against 𢦀鳩仔's normalised funding gap of
~$6–10B cumulative through 2027, a raise is a real branch. It is the reason my sizing uses
the event-inclusive gap and the reason Condition 6 exists.

---

## 5. Correlation & concentration assessment (summary)

| Dimension | Assessment |
|---|---|
| Factor loading | **AI capex — the same factor as MU/KLAC/MRVL/BE.** Not a diversifier (§3.2). |
| Realised stress correlation | **High.** −9% vs SOX −6.7% on the worst day of the July selloff. |
| Pairwise, vs KLAC | **Negative diversification** — Intel's >$20B capex is KLAC's revenue line. |
| Pairwise, vs MU | Both high-beta semis; MU −13% / INTC −9% same session. |
| Idiosyncratic additions | Sovereign cap table, escrow derivative, $20-strike contingent warrants, 14A single-disclosure binary, equity-raise risk. All **uncompensated**. |
| Geographic / policy | US-policy-levered rather than Taiwan-levered — the **one genuine** offset to the Taiwan factor ledger opened in the KLAC review. Small, and it substitutes US political capital-allocation risk for Taiwan risk rather than removing risk. |
| Momentum / positioning | **+343% in 52 weeks; −36% from the high in five weeks; failed +11% after-hours reversed to −7.9%.** Textbook distribution pattern. Department 5 has not been asked for a chart read — this is a gap (Condition 3). |

---

## 6. Missing risk work — commissioned, not waived

Neither of my analysts has produced INTC work. For a proposal of this size the absence is
tolerable only because I am vetoing; **it would not be tolerable for an approval.**

- **Mo Peter (VaR) — COMMISSIONED.** Measured daily σ and 1-day 95% VaR for INTC; marginal
  and component VaR of a 2.00% INTC sleeve against a hypothetical AI-cluster book;
  explicit correlation matrix INTC × {MU, KLAC, MRVL, BE}. My σ≈4.5% is an estimate from
  four observed sessions and must be replaced.
- **Mario (Stress Testing) — COMMISSIONED.** Three named scenarios: (i) AI-capex
  deceleration repeat of 2 Jul 2026 magnitude across the whole cluster simultaneously;
  (ii) **INTC-specific binary — 14A yields zero committed logos by mid-2027**, with the
  KLAC read-through of an Intel capex cut; (iii) equity raise announced at a discount.
  Scenario (ii) is the one no one else in the firm is modelling, because it is the only
  event that hits INTC and KLAC through *opposite* mechanisms from the *same* cause.

---

## 7. Binding conditions

These bind Zac (sizing), 死潘狗 (execution) and Morris (PM). They are not advisory.

1. **Price gate — no initiation at or above $45.00.** This is not 𢦀鳩仔's 50%-MoS level
   ($16.35); I am not gating on his fair value. I gate on **loss distance**, and I adopt
   his stated "revisit" level — **$45, the discounted value of management's own full 2030
   plan delivered in full** — because above it the firm is paying a premium to a plan
   rather than a discount to it, and there is no positive branch left to underwrite. For
   the record, at $91.68 the price is **9.1% above 𢦀鳩仔's deliberately-winnable bull case
   of $84.05**: the firm would be paying more than the best case it can construct. I am
   proposing that as a general limit (D3 below).
2. **Alternative gate — evidence, not price.** The gate in (1) is waived if **both** of
   𢦀鳩仔's falsification triggers land: **(a) DCAI operating margin holds ≥35% for two
   quarters after server capacity loosens**, and **(b) two committed high-volume,
   non-strategic 14A logos by mid-2027.** On both, his base goes to $70–85 and this
   becomes a pay-up-for-quality debate rather than a valuation veto — at which point the
   entry price must still be **≤30% below the then-current base case**. One trigger is not
   two.
3. **老詹 must produce an invalidation level before any ticket.** `stop_required: true` is
   currently FAILED. My provisional $77.93 (−15%) is a sizing input, not a Department 5
   stop, and may not be used as one.
4. **Entry price must be verified against a live quote on the day.** An 11% dispersion
   across four sources on a single close is larger than the entire authorised position.
   死潘狗 must reconcile to a single verified print; if dispersion exceeds 2% at ticket
   time, the ticket is void.
5. **Size — total INTC ≤ 2.00% of NAV at cost**, starter tranche **≤0.75%**, second tranche
   only after the 14A binary resolves. The 10% single-position cap is **non-binding here**
   and may not be cited as the limit.
6. **No entry within 5 trading sessions before a scheduled earnings date, and none while an
   equity raise is an open question.** The known binaries (Q3 print late Oct 2026; 14A
   commitments expected 2H26–1H27) must be entered *after*, not *into*. Taking a
   directional view ahead of a coin-flip disclosure is not investing.
7. **Joint cap with KLAC: combined INTC + KLAC ≤ 12% of NAV at cost**, on the
   same-invoice grounds in §3.2(3). Neither may be sized without reference to the other.
8. **Cluster gate.** INTC nets against the 40% AI-cluster cap. **No INTC initiation until
   the Owner resolves the ai+tech = 50% vs cluster = 40% contradiction** via Option A, B or
   C in §3.3. I will not open a fifth name into a cluster whose cap is unenforceable.
9. **Mo Peter's VaR and Mario's scenarios (§6) must be delivered and reviewed before any
   approval**, not before any ticket. A material initiation without them is a process
   breach.
10. **Portfolio state must be populated first.** See §8 — this is a precondition, not a
    condition.

---

## 8. Empty-portfolio caveat (fifth escalation) — answer to question (e), part 1

`config/portfolio.yaml` still reads `holdings: []` and `cash_balance: 0.00`.

**I have now escalated this on MU, KLAC, MRVL, BE and INTC. Nothing has changed.** The
consequence is unchanged and I restate it without softening: **`max_drawdown`, `cash_floor`,
`max_var_95_1d`, `max_single_position`, `max_sector` and `max_correlated_cluster` are all
fractions of a denominator that does not exist.** I can enforce the *ratios* — and I have —
but I cannot certify the *portfolio* inside its limits, which is my first KPI. Today the
book is trivially compliant because it is empty; the moment the Owner's real holdings exist
and are not in this file, the firm will be running unmeasured exposure against limits it
believes it is honouring, and my "zero limit breaches discovered after the fact" KPI becomes
unfalsifiable.

**This caveat does not weaken the INTC veto** — the veto rests on price, loss distance,
factor concentration and two hard limit failures (#2, #10), none of which need a NAV. But
it does mean **no APPROVAL of any name can be issued as unconditional while the denominator
is unknown.** Requested of the Owner, again: populate real holdings and cash, or state in
writing that the book is genuinely empty and the firm is starting from cash, so that I can
certify against a known zero.

---

## 9. New limit-design defects (answer to question (e), part 2)

### D1 — **No aggregate or correlated risk-at-risk limit.** *(new; the most important defect I have found in five reviews)*
`max_risk_per_trade: 0.01` caps risk **per trade**. Nothing caps risk **in aggregate**, and
nothing caps risk **per factor**. Five names each sized to exactly 1% risk are, on the
config's reading, five compliant trades. But if all five load the same AI-capex factor —
which, on 修大哥's evidence, MU, KLAC, MRVL, BE and now INTC all do — then those are not
five 1% risks. In a correlated drawdown they are **one 5% risk**, and the config contains
no line that notices. `max_correlated_cluster` caps *exposure* (dollars), not *risk*
(dollars × loss distance), and exposure is the wrong unit: a 5% position in a name that can
fall 20% and a 2% position in a name that can fall 50% are the same risk and count
differently under the current limit.

**Proposed additions:**
```yaml
per_trade:
  max_risk_per_trade: 0.01
  max_aggregate_risk_at_risk: 0.03      # NEW — sum of (size x realistic loss distance), all names
  max_correlated_risk_at_risk: 0.02     # NEW — same sum, within a single cluster
```
At a 2.00% INTC position on a 45% loss distance, INTC consumes **1.00% of a 2.00%
correlated budget — half of it, on one name.** That is the number the committee should be
looking at, and today the config does not compute it.

### D2 — **`max_sector` uses GICS, which does not measure this firm's actual concentration.**
GICS places INTC, KLAC, MU and MRVL in Information Technology and BE in Industrials. A book
of four semis plus BE reads as ~80% IT / 20% Industrials and would trip the 35% sector cap
at four names — but for the wrong reason and at the wrong threshold, while the *real*
exposure (one AI-capex factor, 100% of the book) is measured by nothing. Sector labels and
factor exposures have diverged. Superseded by D1 and the §3.3 Option A cluster registry.

### D3 — **No limit prohibits initiation above the firm's own bull case.**
INTC at $91.68 is **9.1% above 𢦀鳩仔's bull-case fair value of $84.05** — a bull case he
had to rebuild *upward* because his first pass came out below the market price. The firm
can currently buy a security at a price exceeding the best outcome its own research desk
can construct, and no limit says otherwise. I propose:
```yaml
process:
  max_entry_vs_desk_bull_case: 0.90     # NEW — no initiation above 90% of the desk's own bull FV
```
This is a cleaner and more general gate than any MoS rule, because it does not require
agreement on fair value — only that the firm not pay more than its own optimist.

### D4 — **`max_correlated_cluster` has no membership definition and is therefore unenforceable as written.**
The config states a 40% cap and never defines what belongs to a cluster, who assigns
membership, or where the ledger lives. I have been maintaining the AI-cluster and Taiwan
ledgers as CRO judgement inside individual reviews. That is not law, it is my opinion, and
it will not survive my absence. §3.3 Option A fixes it.

### D5 — **No cap-table-integrity screen.**
Nothing in the config notices that a name's share count is not fixed. INTC carries 143M
escrowed shares, 241M contingent warrants, and a $15.6B derivative liability that grows
with the share price — a **+30% fully-loaded share count vs 2023**, and a claim structure
that transfers value to a third party as the position works. Per-share risk limits
implicitly assume a stable denominator. Suggested screen: flag any name where fully-loaded
shares exceed outstanding by >5%, or where three-year dilution exceeds 20%, for explicit
committee acknowledgement. **INTC fails both.**

---

## 10. Risk score (committee input): **28 / 100**

| Component | Weight | Score | Rationale |
|---|---:|---:|---|
| Price-to-value loss distance | 25% | **5** | −64% to central FV, −45% to the most generous cell in the desk's own grid, and 9% *above* the desk's bull case. The worst of the five on this axis. |
| Volatility & drawdown profile | 20% | **15** | +343%/52wk, −36% in five weeks, 8–9% single sessions twice in a month, −7.9% on a 2x beat. Textbook distribution. |
| Solvency & survivability | 15% | **70** | The best of the five. $29.7B liquidity, IG debt to 2066, maturities termed out, sovereign holder, H1'26 OCF above capex by $1.9B (+$7.8B YoY swing). This position cannot go to zero. |
| Liquidity & executability | 10% | **85** | Mega-cap, deepest liquidity of the five; ADV constraint non-binding at any plausible NAV. |
| Correlation / factor contribution | 15% | **10** | Not a diversifier — loads the same AI-capex factor and is **anti**-diversified against KLAC. Adds four uncompensated idiosyncratic risks. |
| Structural / cap-table risk | 10% | **20** | $20-strike contingent warrants blocking the value-unlock; escrow claim that grows with the stock; +30% fully-loaded dilution; live equity-raise fear. |
| Process & measurability | 5% | **10** | No stop from Dept 5, no VaR, no stress test, NAV undefined, 11% price dispersion. |
| **Weighted** | | **~28** | |

**Placement in the sequence: MU 38 · KLAC 31 · INTC 28 · MRVL 24 · BE 18.**

Between KLAC and MRVL, and I want the reasoning on the record because it will be
challenged from both directions. **Above MRVL and BE** because the business is genuinely
improving, the balance sheet is genuinely repaired, and the position is genuinely
survivable — a small INTC holding cannot be destroyed, only embarrassed. **Below KLAC**
because the price-to-value gap is the most extreme in the entire sequence (2.8x central
FV), the realised volatility is the highest, the position is anti-diversifying against the
holding the CIO already prefers, and the cap-table structure blocks the one route by which
the asset-value case could be realised.

**28 is the highest score I have given to a name I am vetoing on price alone, and it should
be read as such:** this is the first of the five that I expect to see again on better terms
rather than never again. If both of 𢦀鳩仔's falsification triggers land, I will re-score
it, and I would expect it to land in the 45–55 range at a price 30% below a $70–85 base —
which would be an approvable risk profile at 2–3% of NAV.

---

## 11. Escalation to the CEO and Owner

1. **Cluster contradiction — fifth escalation, now urgent.** ai 0.30 + technology 0.20 =
   0.50 vs `max_correlated_cluster: 0.40`. Three concrete remedies in §3.3. **A decision is
   required before a fifth semiconductor name is considered, not after.**
2. **Portfolio state — fifth escalation.** `holdings: []`, `cash_balance: 0.00`. No name
   can receive an unconditional approval until this is resolved (§8).
3. **Five new limit-design defects (D1–D5)**, of which **D1 (no aggregate or correlated
   risk-at-risk cap)** is the one I would fix first if only one change were permitted.
4. **A pattern I am obliged to name.** Five consecutive vetoes is either a market in which
   this firm's philosophy finds nothing to buy, or a research process anchored to the
   bearish side. 𢦀鳩仔 confronted this directly and honestly in his §8 and still landed at
   $33 with a $22–55 band; 巴爺爺 upgraded INTC to C+. I do not believe the desk is
   anchored. **But I would ask the Owner to note that Risk has not been the binding
   constraint in any of the five — the valuation gate has.** If the Owner's intent is for
   this firm to hold positions rather than to hold cash, the conversation to have is about
   the required margin of safety in `knowledge/investment-philosophy.md`, not about my
   limits. That is a philosophy decision and it belongs to the Owner, not to me. I will
   enforce whatever is decided; I will not lower a gate on my own authority.

---

*Prepared by John, Chief Risk Officer, Department 6 — Risk Management.*
*Limits checked against `config/risk-limits.yaml` and `config/portfolio.yaml` as at 2026-07-28.*
*Every figure is sourced from a dated department report or a config file. Volatility,
VaR, loss distances and the σ estimate are my own derivations from the observed price
moves cited in §1.2 and are marked as estimates. No invented numbers.*
*Research and decision support only. Committee and Owner decide. No live trading.*

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
