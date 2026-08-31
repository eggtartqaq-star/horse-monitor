# Risk Review — Prospective NEW LONG: KLAC (KLA Corporation)

**Author:** John, Chief Risk Officer (Dept. 6 — Risk Management)
**Date:** 2026-07-19 · **For:** Investment Committee / CEO 皮褸黃 / Owner
**Price context:** **$212.75** (Fri 2026-07-17 close, POST-SPLIT — 10-for-1 effective
2026-06-12; verified by 老詹 and Tim Cook against ≥2 independent sources). Market cap
~$284B. **−31%** from the split-adjusted ATH ($307.37 / $301.71 close, Jun 30).
Realized single-session shocks ~4–6.8% (materially lower than MU/MRVL). **Binary
event risk: KLA fiscal-Q4 earnings Jul 28 (±8% implied), FOMC Jul 29 — one to two
days after any near-term entry.**
**Inputs reviewed:** risk-limits.yaml, portfolio.yaml, 𢦀鳩仔 (valuation **22/100**,
FV $75–145 base ~$74, prob-wtd ~$79, MoS ≈ **−188%** on base), 菲比斯 (moat
**WIDE/WIDENING**, ~43% ROIC / ~25% trough — best moat in coverage), 巴爺爺
(financials **91/100 grade A** — bulletproof balance sheet, ~15–18x coverage, 0.3x
net-debt/EBITDA — highest financial score in coverage), Peterson (macro 56/100 — "not
a capitulation entry"), 老詹 (technical **58/100** — "prepare to buy in zones, not yet
a green light"), Tim Cook (structure — transitional/corrective, held up far better
than MU/MRVL, no liquidity constraint), 王老吉 (flow — neutral), LeBron James
(geopolitical MEDIUM), The dictator (regulatory — net headwind, China ~24–30% of rev).
**Missing inputs:** Mo Peter VaR — none on file. Mario stress test — none on file.
Both binding conditions on any resubmission; a Mo Peter run must **separately model
the Jul 28 earnings jump** (normal-vol VaR does not capture a binary).
**Precedent:** `reports/risk/2026-07-18-mu-risk-review.md` (APPROVED WITH CONDITIONS,
6.5% cap, 38/100) and `reports/risk/2026-07-19-mrvl-risk-review.md` (VETOED,
valuation gate, 24/100). This review applies the identical gap-adjusted sizing method
and the identical valuation-gate logic, and lands on a **veto for the current price
with the most constructive conditional door in the pipeline** — for name-specific
reasons set out below.

---

## VERDICT: VETOED — for initiation at $212.75 and anywhere on 老詹's near-term entry map

The proposal does **not** proceed to committee as a live buy in its present form. As
with MRVL, this is a **valuation veto**, and it belongs to the committee/CIO, not to a
risk-limit fix. But unlike MRVL — where I vetoed on **both** timing *and* valuation —
here the veto rests on **valuation alone**. Timing (58/100), business quality (moat
WIDE/WIDENING, financials 91/100 grade A), and volatility (single-session ~4–7% vs
MU/MRVL 9%) are all the **most** risk-acceptable in the current pipeline. That is
exactly why the conditional re-entry door in §5 is left wider than MRVL's: **of the
three semis names, KLA is the one I would most want the firm to own — if price ever
comes to us.** It has not.

**The disqualifying fact:** at $212.75 the price is **+188% above 𢦀鳩仔's base fair
value ($74)** — the stock trades at **~2.9x base intrinsic value**, at **~61x trailing
earnings / ~2.5x its own historical multiple.** This is the same over-pricing error as
MU/MRVL in a higher-quality wrapper. A risk-limit review can *size* a position to
survive a drawdown; it cannot cure a −188% margin of safety. **Business quality does
not rescue a price 2.9x fair value — it only lowers the odds of *permanent* impairment
(KLA will not go bankrupt), not the odds of a large multiple de-rate.**

**Distinguishing the two proposals the brief asks me to separate:**
- **Buy-now at $212.75:** **VETOED** — fails the valuation gate by 188%; timing is
  constructive but timing is not the binding constraint here.
- **Buy-on-pullback into 老詹's zones ($194–210):** **NOT APPROVED.** It *passes* the
  timing gate (58/100, buy-the-correction posture) — but **every one of 老詹's entry
  zones is still 2.4–2.9x base FV**: $206–210 = ~2.8x, $194–198 = ~2.65x, even the
  $177 reserve = ~2.4x. **There is no technically-plausible near-term entry that is
  also inside the firm's valuation discipline.** Same structural problem as MRVL: the
  chart's best buy zone and the desk's fair value do not overlap. This is a valuation
  veto, not a sizing problem, and I will not size around it.

A genuinely constructive conditional door is left open in §5 for a **future,
materially lower-price proposal** (𢦀鳩仔's ~$130 watch alert / ~$95–105 base-FV
size-up / 菲比斯's ~$106 bull-MoS line). That is not an approval of the position now
in front of the committee.

---

## 1. Sizing arithmetic (the *legal* ceiling, if valuation ever cleared)

Per-trade law: `max_risk_per_trade: 0.01` — weight × distance-to-stop ≤ 1% of
portfolio. Computed on 老詹's near-term map to establish the name's ceiling; note the
actual stop at any *future* valuation-cleared entry ($95–130) must be re-derived by
老詹 for that price.

**老詹 tranches & nominal stops (close basis):**
- Starter $206–210 (mid ~$208), stop < $200 → nominal **~3.8%**.
- Core $194–198 (mid ~$196), weekly close < $190 (hard $185) → nominal **~3.1% / 5.6%**.
- Reserve $177–180 (mid ~$178.5), stop < $168 → nominal **~5.9%**.

**Naive solve:** 1% ÷ 3.8% = 26% — nominal stops are tight (KLA's vol is genuinely
lower), so the per-trade budget does **not** bind below the 10% cap on nominal
distance. **I reject the naive basis**, as with MU/MRVL — this is a gappy, headline-
driven chip tape and, decisively, **there is a ±8% implied binary (Jul 28 earnings)
one day after any near-term entry.**

**Two gap regimes:**
- *Non-earnings sessions:* SMH ±4% days compound a 3.8% close-stop into a realistic
  ~7% gapped fill. Gap-adjusted ~7% — still **tighter** than MU (15%) / MRVL (18%),
  reflecting KLA's real resilience (Tim Cook: KLAC −18% peak-to-current vs MRVL −43%,
  MU −33%).
- *Earnings (Jul 28):* ±8% implied, tail to ~10–12%. For any tranche held **through**
  the print, this dominates.

| Sizing basis | Stop distance | Max size under 1% rule |
|---|---|---|
| Nominal (starter, $208 → $200 close) | ~3.8% | 26% (cap binds at 10%) — REJECTED basis |
| Gap-adjusted, non-earnings (CRO basis) | ~7% | 14% (cap binds at 10%) |
| **Gap-adjusted, earnings-inclusive (CRO basis)** | **~10%** | **~10% → capped at 8% for tail buffer** |
| Gap-adjusted stress (bad print + guide) | ~12% | 8.3% |

**Ceiling for any future proposal: 8.0% of portfolio at cost.** This is **higher** than
MU (6.5%) and MRVL (5.0%) — the *only* name in the pipeline whose genuinely lower
volatility earns room toward the single-position cap. That is the correct, non-
sentimental reflection of KLA being the better business *and* the lower-vol stock.

**The Jul 28 binary is a hard sizing constraint of its own:** no material size goes in
front of a binary. Any tranche entered **before** Jul 28 is capped at **≤ 2.0%**, so a
worst-case 8–12% adverse earnings gap costs **0.16–0.24% of portfolio** — a rounding
error. The book takes its real KLA size **after** the print, once the binary is
resolved and (per §5) only if the price is inside the valuation gate.

---

## 2. Limit-by-limit check

Book is empty (`holdings: []`, `cash_balance: 0.00`). Post-trade columns show (a) the
brief's hypothetical 10% and (b) my 8.0% gap-adjusted ceiling — **both for completeness
only; the position is vetoed at the current price regardless of size.**

| Limit | Law | Current | Post @10% (hypo) | Post @8.0% (ceiling) | Pass/Fail |
|---|---|---|---|---|---|
| max_single_position | 10% at cost | 0% | 10.0% | 8.0% | @10% PASS (at limit) / @8% PASS |
| max_risk_per_trade | 1% (size × stop) | n/a | Nominal 0.38% pass; **earnings-gap 1.0–1.2% borderline/FAIL** | Nominal 0.30%; earnings-gap ~0.80–0.96% | @10% borderline/FAIL on earnings gap / @8% PASS |
| stop_required | yes | n/a | 老詹 $200/$190/$168 close levels | adopted binding | PASS conditional |
| max_sector (semis/IT) | 35% | 0% | 10% | 8.0% | PASS |
| max_correlated_cluster (AI complex) | 40% | 0% | 10% | 8.0% | PASS on paper — see §3 (nets vs MU/MRVL + Taiwan ledger) |
| cash_floor | ≥10% | **unverifiable — cash 0.00** | ~90% if cash-funded | ~92% | PASS on assumption; **unverifiable until Owner enters data** |
| leverage | none | none | cash purchase assumed | cash required | PASS conditional |
| max_var_95_1d | ≤3% | 0% | ~0.66% (est.) | ~0.53% (est.) | PASS (estimate) — **no Mo Peter run; must model Jul 28 jump** |
| max_adv_participation | ≤5% $ADV | n/a | negligible (~$2.2B ADV; personal size <0.2%) | same | PASS — no liquidity constraint (Tim Cook) |
| max_drawdown budget | 20% peak-to-trough | fresh book | −65% to base FV = −6.5% portfolio (**33% of the entire budget on one name**) | −65% = −5.2% (26% of budget) | @10% imprudent / @8% imprudent-at-$212.75 |
| committee_approval_required | yes | — | this review is the risk input | same | Pending |
| decision_record_before_ticket | yes | none | required | required | Pending |

**VaR estimate (not a Mo Peter figure):** single-session ~4–7% → daily σ ≈ ~4%; 95%
1-day VaR ≈ 1.65 × 4% ≈ 6.6% of position → ~0.66% of portfolio at 10%, ~0.53% at 8%.
Comfortably under the 3% ceiling — the *lowest* estimated VaR in the pipeline, because
KLA is the lowest-vol name. **Caveat:** this normal-vol VaR does **not** capture the
Jul 28 earnings jump; a formal Mo Peter run must overlay the ±8% binary before any
ticket that would straddle the print.

**The single most important cell:** `max_drawdown budget`. At $212.75, the firm's own
**base case is −65%** (price → base FV $74). At the 8% ceiling that is **−5.2% of
portfolio — 26% of the entire 20% drawdown budget consumed on one name at a price the
valuation desk scores 22/100.** This is not a limit *breach* (the book is cash, so the
fraction "passes"), but it is the arithmetic that makes the veto correct: you do not
spend a quarter of the firm's survival budget buying a wonderful company at 2.9x its
fair value the week of a binary print.

---

## 3. Correlation & concentration assessment

- **Today, standalone:** KLAC would be the first position in an empty book — no
  existing factor bet to concentrate. Nominal concentration nil.
- **Against MU + MRVL (the cluster question):** KLAC nets against the **40%
  max_correlated_cluster (AI complex)** and the **Taiwan factor ledger** I opened in
  the MU review. It shares **factor #1 — hyperscaler AI-capex — strongly**: the −31%
  selloff *was* an AI-capex-sustainability de-rating; a WFE downturn hits KLA directly
  (bear case in 𢦀鳩仔's grid is a multi-year WFE downturn to a $34 floor). So on the
  demand factor, KLA is **fully correlated** with any MU/MRVL/NVDA sleeve — holding all
  three is one AI-capex bet in three wrappers, not diversification.
- **The KLA differentiator on the Taiwan ledger (favorable):** KLA is **picks-and-
  shovels equipment**, not a fabless chip that *is* manufactured in Taiwan. Its Taiwan
  exposure is **indirect** — via customer (TSMC) capex — not the **single-source,
  100%-TSMC-for-its-own-product** dependence that makes MRVL the worst Taiwan-tail
  name. KLA sells globally (TSMC, Samsung, Intel, SMIC), so it contributes **less per
  dollar to the Taiwan fat-left-tail** than MRVL and differently than MU. **But** it
  carries a **distinct exposure MU/MRVL do not have to the same degree: China revenue
  ~24–30%**, squarely in the BIS semicap-export-control crosshairs (The dictator: net
  headwind; 𢦀鳩仔's bear case is "China structurally lost"). So KLA swaps some Taiwan-
  strait tail for **China-export-control tail** — a different, not smaller, geopolitical
  factor.
- **Joint-sizing rule (binding on Morris/Zac):** if any two of MU/MRVL/KLAC clear
  their gates, the AI-cluster and factor ledgers are sized **jointly**, and Mario runs
  a **joint MU+MRVL+KLAC scenario** covering (a) AI-capex de-rating, (b) Taiwan-strait
  shock, (c) BIS China semicap rule. Nominal diversification across three AI-capex
  proxies is concentration in disguise.

---

## 4. The valuation-veto question (routed to committee/CIO)

The brief asks it directly: is this a valuation veto I route to committee (like MRVL),
or is the wide moat + A balance sheet + lower vol enough to APPROVE WITH CONDITIONS a
small valuation-contingent starter? **My answer as CRO: it is a valuation veto — same
category as MRVL — routed to committee/CIO.** Reasons, in order:

1. **The MoS is worse than MRVL on base.** MRVL was −170% to base; KLAC is **−188%**.
   The *price*-risk here is not smaller because the *business* is better.
2. **No near-term entry clears the gate.** 老詹's entire zone map ($177–210) sits
   2.4–2.9x base FV; even the bull case ($142) is 33% below spot. A pullback does not
   rescue this any more than it rescued MRVL.
3. **It is not curable by position sizing.** Sizing controls *how much* of the
   drawdown budget one name can spend; it cannot convert a −188% MoS into a positive
   one. That decision — "do we pay 2.9x fair value for the best moat in the group?" —
   is a philosophy/valuation call for the CIO and committee, not a risk-limit call.

**Where KLA genuinely differs from MRVL (and why the score and the door differ):** the
*consequence* of being wrong on price is milder. MRVL is a narrow, eroding moat with
82% top-10 customer concentration and a sub-WACC ASIC leg — if its thesis breaks, the
loss can be permanent. KLA is a WIDE/WIDENING moat, ~43% ROIC, grade-A balance sheet
(15–18x coverage) — a multiple de-rate is painful but the *franchise* survives and
compounds. So the **probability of permanent capital impairment is far lower**, even
though the **magnitude of a multiple-compression drawdown is similar**. That lowers
risk-*acceptability* meaningfully (reflected in the higher score, §6) but does **not**
clear the valuation gate — I am not paid to buy quality at any price.

---

## 5. Conditional re-entry door (binding on any FUTURE resubmission; not an approval now)

This door is left **wider than MRVL's** because KLA is the highest-quality vehicle for
AI-capex exposure in the pipeline (agree with Peterson and 𢦀鳩仔's own note). A *new*
proposal must satisfy **all** of the following before it re-enters committee. Absent
these, the veto stands.

1. **Valuation gate (the gate that killed this one).** Entry price inside the firm's
   discipline: 𢦀鳩仔's **~$130 watch/starter-consideration alert** as the *earliest*
   door (still ~1.8x base FV — a starter only, on a partial-credit-to-the-moat basis),
   with real size only toward **~$95–105 (base FV reached)** or 菲比斯's **~$106
   bull-case 25% MoS**. No initiation at $212.75 or on 老詹's near-term map. A strong
   Jul 28 print that *raises FY27 WFE guidance* may lift the growth inputs, but per
   𢦀鳩仔 it does **not** by itself rescue a 55–61x entry multiple — a re-rating must
   come from cash-flow facts, not multiple expansion.
2. **Earnings-binary gate.** No material size in front of Jul 28. Any pre-print tranche
   ≤ **2.0%**. The book's real KLA size is taken **after** the binary resolves, and
   only if the post-print price sits inside gate 1.
3. **Timing gate (老詹).** At whatever future price clears gate 1, 老詹 re-derives the
   entry zones and the close-basis stop; buy in thirds, defend the invalidation on
   close, no chasing into overhead ($224–225 reclaim, then $259) without a confirmed
   structure-repair.
4. **Size.** Total KLAC ≤ **8.0% of portfolio at cost** (gap-adjusted; §1). Starter
   ≤ 2.0%. The full 10% single-position cap is **not** available while the Jul 28
   binary is live and until the position is post-print and valuation-cleared.
5. **Stop is law.** On 老詹's current map: daily close < $200 (starter), weekly close
   < $190 / hard $185 (core), < $168 (reserve); decisive close < **$194** abandons the
   buy-the-dip thesis; a break of the **200-day (~$177)** breaks the primary trend and
   exits. No averaging down through any stop. Future entries carry their own re-derived
   stop.
6. **Portfolio data first.** Owner populates `config/portfolio.yaml` with real
   `cash_balance` and holdings. Every fraction here is re-run against real dollars by
   Zac and re-checked by me before any ticket. (Same standing control gap escalated in
   the MU and MRVL reviews — see §6.)
7. **Cluster gate.** KLAC nets against the 40% AI-cluster cap **and** the Taiwan/China
   factor ledger from inception; any concurrent MU/MRVL position is sized *jointly*,
   and Mario runs a joint MU+MRVL+KLAC scenario (AI-capex de-rate, Taiwan shock, BIS
   China semicap rule). Mo Peter runs a formal 1-day 95% VaR on the sized position that
   **separately models the earnings jump**; both filed in `reports/risk/` before any
   decision record.
8. **Funding.** Cash only, no margin (`leverage: none`). Any options overlay
   (C朗) is covered-only, separately priced, separately signed off.
9. **Tripwire monitoring (assigned).** The dictator + LeBron James — BIS semicap
   export-control action on China (KLA ~24–30% China rev); WFE capex-guide cuts from
   TSMC/Samsung/Intel; AI-capex-sustainability headlines; truce lapse ~Nov 1, 2026;
   any KLA-specific insider-selling disclosure (an early-July gap catalyst per Tim
   Cook). Any tripwire firing re-opens the name from scratch.
10. **Process.** Committee approval, then decision record in `memory/decisions/` with
    this review's conditions and any dissent, then and only then an execution ticket
    for the Owner. No live trading.

---

## 6. Risk score (committee input): **31 / 100**

Scale: higher = more risk-acceptable to initiate *as proposed at $212.75*. Placed
**above MRVL (24) and below MU (38)**, deliberately:

- **Why above MRVL (24):** genuinely the best business in the pipeline — moat
  WIDE/WIDENING (~43% ROIC, ~25% at trough), financials grade-A 91/100 (bulletproof
  balance sheet, 15–18x coverage, 0.3x net debt), the lowest realized volatility
  (single-session ~4–7% vs MU/MRVL 9%; held up at −18% peak-to-current vs MRVL −43%),
  constructive timing (58/100, buy-the-correction posture), no liquidity constraint,
  and a lighter/less-single-source Taiwan-tail than MRVL. The probability of
  *permanent* capital impairment is the lowest of the three.
- **Why still well below the midline (the veto):** the valuation is the disqualifier —
  22/100, price **2.9x base fair value, MoS −188%** (worse than MRVL on base), ~61x
  trailing / ~2.5x its own history; a base-case −65% drawdown that would consume ~26%
  of the firm's entire drawdown budget at the 8% ceiling; a ±8% binary one day after
  any near-term entry; China-export-control tail; no VaR/stress on file; **no real
  portfolio data on file.**

A 31 says: this is the name the firm should most *want* to own — and it is **not a
risk-acceptable initiation at $212.75.** Business quality lifts it above MRVL; the
−188% margin of safety keeps it a veto. Upside is not my department; survival is. The
veto is not moved by return arguments (BofA "enhanced buying opportunity," the AI-capex
narrative) — those are the market's assumptions, not the firm's. If price comes to the
firm's value zone ($95–130) post-print, this converts to the strongest
APPROVED-WITH-CONDITIONS candidate in the pipeline.

**Escalation note to CEO/Owner (repeat of the MU/MRVL standing item):**
`config/portfolio.yaml` remains empty (`holdings: []`, `cash_balance: 0.00`). Until it
is populated, **no** proposal from any department can receive an unconditional risk
verdict — I can check limit *fractions* but not a single dollar. Remediation: Owner
enters holdings and cash; I re-certify the entire pipeline (MU, MRVL, KLAC) against
real numbers within one session. This gap does not change today's KLAC verdict (the
veto rests on valuation, not on missing dollars), but it caps every other name at
"conditional" and must be closed.

---

*Limit citations: `config/risk-limits.yaml` (2026-07-19). Market figures from the
cited 2026-07-19 department reports; volatility-based VaR and gap-adjusted stop
distances are marked estimates. Research and decision support only — not financial
advice; markets cannot be reliably predicted.*

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
