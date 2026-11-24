# Risk Review — Prospective NEW LONG: MRVL (Marvell Technology)

**Author:** John, Chief Risk Officer (Dept. 6 — Risk Management)
**Date:** 2026-07-19 (Sunday) · **For:** Investment Committee / CEO 皮褸黃 / Owner
**Price context:** $188.68 (Fri 2026-07-17 close), **−42.8%** from the 6/18 ATH
$329.88; realized daily ranges 8–9% during the mid-July selloff.
**Inputs reviewed:** risk-limits.yaml, portfolio.yaml, 𢦀鳩仔 (valuation 25/100,
FV $55–105 central ~$70, MoS ≈ −170%), 巴爺爺 (financials 66/100, 82% top-10
customer concentration), Peterson (macro 52/100), 老詹 (technical 34/100), Tim Cook
(structure — confirmed downtrend, RS 2:1 vs SOX, gap risk), 王老吉 (flow —
distribution ~60%), LeBron James (geopolitical MEDIUM-HIGH), The dictator
(regulatory — mild net headwind, Section 232 Phase 2 live binary).
**Missing inputs:** Mo Peter VaR — none on file. Mario stress test — none on file.
Standalone moat file (菲比斯) not on disk; moat terms taken from the valuation and
financials reports. All three are binding conditions on any future resubmission.
**Precedent:** `reports/risk/2026-07-18-mu-risk-review.md` (MU — APPROVED WITH
CONDITIONS, 6.5% gap-adjusted cap, 38/100). This review applies the same gap-risk
sizing method and reaches a harder verdict for name-specific reasons.

---

## VERDICT: VETOED (for initiation now or on the current near-term entry map)

The proposal does **not** proceed to committee as a live buy in its present form. Two
independent grounds each suffice; together they are decisive:

1. **Timing / location (risk-limit + technical).** 老詹 is explicit: "do NOT
   initiate at $188." Technical 34/100 — fresh, breadth-confirmed markdown, bearish
   20/50-day alignment, MACD deeply bearish, **no** reversal or divergence signal,
   and negative relative strength ~2:1 vs SOX (weakest horse in a weak group). A
   buy-now at $188.68 is the lowest-edge location on the chart, in an 8–9% gap
   regime. Vetoed on timing.

2. **Valuation (the disqualifying input, and the reason a pullback does not rescue
   this).** 𢦀鳩仔 values MRVL at $55–105, central ~$70; at $188.68 the margin of
   safety is **≈ −170%** and price is **~2.7x the firm's own fair value**. Crucially,
   this does **not** clear at 老詹's *preferred* entry either: at $164–166 the stock
   is still **~2.3x** central FV (MoS ≈ −136%); even at the $147.84 invalidation it
   is **~2.1x** FV. The desk does not turn constructive until ~$60–70 — a further
   **~57–63%** below the current price and still **~50–58% below** any entry on
   老詹's near-term map. **There is no technically-plausible near-term entry that is
   also inside the firm's valuation discipline.** A risk-limit review can *size* a
   position to survive a drawdown; it cannot cure a −136% to −170% margin of safety.

**Distinguishing the two proposals the brief asks me to separate:**
- **Buy-now at ~$188.68:** VETOED — fails timing *and* valuation.
- **Buy-on-pullback to $164–166 on a confirmed reversal:** NOT APPROVED — passes
  timing only *if* 老詹's reversal triggers, but still fails the valuation gate by a
  wide margin. This is not a risk-limit fix; it is a **valuation veto that belongs to
  the committee/CIO.** I flag it as such rather than sizing my way around it.

A conditional re-entry door is left ajar in §5 for a **future, materially lower-price
proposal** — that is not an approval of the position now in front of the committee.

---

## 1. Sizing arithmetic (what a *legal* size would be, if valuation ever cleared)

Per-trade law: `max_risk_per_trade: 0.01` — weight × distance-to-stop ≤ 1% of
portfolio. Computed at 老詹's preferred Zone 1 to show the ceiling any future
proposal faces.

- **Entry (老詹 Zone 1):** $164–166, midpoint ~$165, only on a *confirmed* reversal.
- **Invalidation:** daily close below **$147.84**.
- **Nominal stop distance:** ($165 − $147.84) / $165 = **~10.4%** (≈9.9% from $164) —
  much wider than MU's 4–6% nominal.

**Naive (nominal) solve:** 1% ÷ 10.4% = **9.6% max size** — the per-trade budget
already binds *below* the 10% single-position cap on nominal distance alone. Unlike
MU (where the 10% cap bound first), a 10% MRVL position is **illegal even before gap
risk** (10% × 10.4% = 1.04% > 1% budget). I reject the nominal basis anyway:

- 老詹/Tim Cook: 8–9% daily ranges, catalysts (TSMC capex, hyperscaler headlines,
  Asia-sourced policy) land pre-open; stops are close-basis and *gappable*.
- A close-basis stop at $147.84 realistically fills near the Zone-2 shelf (~$138) or
  lower in a gap-through session: ($165 − $138) / $165 = **~16%**; a worse gap toward
  the ~$132 200-day region = **~20%**.

**Gap-adjusted stop distance: −18% (estimate; −20% stress).** Consistent with the MU
method (there: ~5% nominal → 15% gapped; here ~10.4% nominal → ~18–20% gapped).

| Sizing basis | Stop distance | Max size under 1% rule |
|---|---|---|
| Nominal ($165 → $147.84 close) | ~10.4% | 9.6% (per-trade budget binds *below* the 10% cap) |
| **Gap-adjusted (CRO basis)** | **~18%** | **5.6% → capped at 5.0%** |
| Gap-adjusted stress | ~20% | 5.0% |

**Ceiling for any future proposal: 5.0% of portfolio at cost, starter tranche
≤ 2.0%.** Tighter than MU's 6.5% because the nominal stop is wider *and* the name
carries the worst valuation, technical, and moat profile in the current pipeline.
This number is academic until §2's valuation gate is cleared — I compute it only so
the committee sees that even a *legal* MRVL is a small, late, deeply-discounted
position, never a 10% one.

---

## 2. Limit-by-limit check

Book is empty (`holdings: []`, `cash_balance: 0.00`). Post-trade columns show (a) the
brief's hypothetical 10% and (b) my gap-adjusted 5.0% ceiling — **both shown for
completeness only; the position is vetoed regardless of size.**

| Limit | Law | Current | Post @10% (hypo) | Post @5.0% (ceiling) | Pass/Fail |
|---|---|---|---|---|---|
| max_single_position | 10% at cost | 0% | 10.0% | 5.0% | @10% PASS (at limit) / @5% PASS |
| max_risk_per_trade | 1% (size × stop) | n/a | **Nominal 1.04% FAIL; gap-adj 1.8% FAIL** | Nominal 0.52%; gap-adj ~0.90% | **@10% FAIL (even nominal)** / @5% PASS |
| stop_required | yes | n/a | 老詹 $147.84 close | adopted binding | PASS conditional |
| max_sector (semis/IT) | 35% | 0% | 10% | 5.0% | PASS |
| max_correlated_cluster (AI) | 40% | 0% | 10% | 5.0% | PASS on paper — see §3 (nets vs MU + Taiwan ledger) |
| cash_floor | ≥10% | **unverifiable — cash 0.00** | ~90% if cash-funded | ~95% | PASS on assumption; **unverifiable until Owner enters data** |
| leverage | none | none | cash purchase assumed | cash required | PASS conditional |
| max_var_95_1d | ≤3% | 0% | ~0.99% (est.) | ~0.50% (est.) | PASS (estimate) — **no Mo Peter run on file** |
| max_adv_participation | ≤5% $ADV | n/a | negligible at personal size (Tim Cook) | same | PASS — no liquidity constraint |
| max_drawdown budget | 20% peak-to-trough | fresh book | −50% severe = −5.0% portfolio (25% of budget on one name) | −50% severe = −2.5% (12.5% of budget) | @10% imprudent / @5% PASS |
| committee_approval_required | yes | — | this review is the risk input | same | Pending |
| decision_record_before_ticket | yes | none | required | required | Pending |

**VaR estimate (not a Mo Peter figure):** realized daily ranges 8–9% → daily σ ≈
~6%; 95% 1-day VaR ≈ 1.65 × 6% ≈ 9.9% of position value → ~0.99% of portfolio at
10%, ~0.50% at 5.0%. Under the 3% ceiling *only because the rest of the book is
cash*. Formal run required before any ticket.

**The single most important cell:** `max_risk_per_trade` fails at 10% on *nominal*
stop distance — before any gap adjustment. This name cannot legally occupy the
single-position cap. Anyone who sizes MRVL to 10% has breached the 1% budget by ~1.8x
on the tape's own volatility.

---

## 3. Correlation & concentration assessment

- **Today, standalone:** MRVL would be the first position in an empty book — no
  existing factor bet to concentrate. Nominal concentration nil.
- **Against MU (also under review) — the real issue:** MRVL and MU are the **same
  two-factor bet** — hyperscaler AI-capex and Taiwan-strait manufacturing — booked
  against the **40% AI-cluster cap** and the **Taiwan-concentration factor ledger**
  I opened in the MU review. LeBron James is explicit: MRVL contributes **more per
  dollar** to the Taiwan factor than MU — it is **effectively 100% TSMC-dependent at
  the leading edge for both wafers *and* CoWoS packaging, with no owned capacity and
  no self-hedge in motion** (MU at least owns Japan/Singapore/US-2027 fabs and sells
  a fungible commodity; MRVL sells single-source custom ASICs with zero alternative
  supply). Holding MU **and** MRVL is not diversification — it is **doubling the same
  fat left tail** (severe strait scenario ~5–8%, MRVL impact −50%+). If both ever
  clear their gates, the combined AI-cluster + Taiwan-factor exposure must be sized
  *jointly*, and Mario must run a **joint MU+MRVL Taiwan-shock** before either
  reaches committee. Nominal diversification across two Taiwan-fab proxies is
  concentration in disguise.
- **Idiosyncratic concentration inside the name:** 巴爺爺 flags **82% top-10 customer
  concentration** and thin GAAP; the custom-ASIC leg (the entire bull thesis) has
  already lost Trainium 3 and Maia 200 *compute dies* to Alchip/GUC — a narrow,
  eroding moat that has **never earned its cost of capital** (ROIC ~6–8% < WACC).
  This is a high-beta, high-gap, single-customer-cluster instrument on top of the
  Taiwan tail.

---

## 4. The valuation-veto question (routed to committee/CIO)

The brief asks directly: does a name at ~2.7x the firm's own fair value belong in the
book at *any* size? **My answer as CRO:** not on a risk-limit basis I can cure, and
not at any entry on 老詹's near-term map. This is a **valuation veto**, and it sits
with the committee and CIO, not with me. I record the following as the risk-relevant
consequence: buying an asset the firm's own analysts value at ~37% of the entry price
makes the risk/reward **structurally asymmetric against us** — the downside is the
firm's own base case ($55, −71%), the "upside" is paying a wide-moat price for a
sub-WACC business. That asymmetry is why I will not size around it. Even the
valuation *bull* case ($103) sits 45% below the current price. The desk turns
constructive at ~$60–70. **On the firm's philosophy, MRVL is a watchlist name, not a
buy — at $188.68 or at $165.**

---

## 5. Conditional re-entry door (binding on any FUTURE resubmission; not an approval now)

Should a *new* proposal ever return, it must satisfy **all** of the following before
it re-enters committee. Absent these, the veto stands.

1. **Valuation gate (the gate that killed this one):** entry price in or credibly
   near the desk's value zone — **≤ ~$70** on current fair value, or a documented
   re-rating of 𢦀鳩仔's estimate (new revenue/margin facts, not multiple
   expansion) that brings MoS to at least 菲比斯's demanded **35%**. No amount of
   technical confirmation substitutes for this.
2. **Timing gate (老詹):** a *confirmed* bullish reversal — reversal candle and/or
   RSI positive divergence at a tested support, and RS ceasing to print new relative
   lows vs SMH/SOX. No buying the touch; no chasing $198–206 as initiation.
3. **Size:** total MRVL ≤ **5.0% of portfolio at cost** (gap-adjusted; §1). Starter
   ≤ 2.0%. The 10% single-position cap is **not** available to this name — it fails
   the 1% per-trade budget on nominal stop distance alone.
4. **Stop is law:** daily close below **$147.84** exits the entire position; no
   averaging down through it. Deeper Zone-2 catch (< $150) only per 老詹's smaller-
   size plan with a ~$138 close stop.
5. **Portfolio data first:** Owner populates `config/portfolio.yaml` with real
   `cash_balance` and holdings. Every fraction here is re-run against real dollars by
   Zac and re-checked by me before any ticket. (Same standing control gap escalated
   in the MU review — see §6.)
6. **Cluster gate:** MRVL nets against the 40% AI-cluster cap **and** the Taiwan
   factor ledger from inception; any concurrent MU position is sized *jointly*, and
   Mario runs a joint MU+MRVL Taiwan-shock scenario. Mo Peter formal 1-day 95% VaR on
   the sized position; both filed in `reports/risk/` before any decision record.
7. **Funding:** cash only, no margin (`leverage: none`). Any options overlay
   (LeBron/C朗 note skew is rich post-selloff) is covered-only, separately priced,
   separately signed off.
8. **Tripwire monitoring (assigned):** The dictator + LeBron James — Section 232
   Phase 2 HTSUS scope for fabless importers; BIS action on networking/interconnect
   ECCNs; truce lapse by ~Nov 1, 2026; MRVL CoWoS allocation cuts / TSMC price
   hikes; any AWS/Microsoft in-sourcing signal. Any tripwire firing re-opens the
   name from scratch.
9. **Process:** committee approval, then decision record in `memory/decisions/` with
   this review's conditions and any dissent, then and only then an execution ticket
   for the Owner. No live trading.

---

## 6. Risk score (committee input): **24 / 100**

Scale: higher = more risk-acceptable to initiate *as proposed*. Rationale (below MU's
38 for concrete, name-specific reasons):

- **Against (dominant):** worst-in-pipeline valuation (25/100; MoS ≈ −170%; price
  ~2.7x FV; the entire plausible sensitivity grid tops out at $87 vs $188.68);
  hostile technical location (34/100; do-not-initiate; no reversal; RS 2:1 vs SOX
  underperformance); 8–9% gap regime so a 10% size is illegal on nominal stop alone;
  narrow, eroding moat that has never earned its cost of capital; 82% top-10 customer
  concentration; effectively 100% TSMC/CoWoS dependence with no self-hedge
  (geopolitical MEDIUM-HIGH, one notch above MU); Section 232 Phase 2 a live headwind
  for a fabless importer with no offset eligibility; no VaR/stress on file; **no real
  portfolio data on file**.
- **For (keeps it off the floor, does not save it):** primary weekly uptrend not yet
  broken (price ~47% above a rising 200-day); deeply oversold RSI (bounce potential);
  well-defined invalidation levels; strong management delivery record (Peter) and a
  sound balance sheet (net debt ~$1.1B) — which support the *business*, not the
  *price*; no liquidity constraint at personal size.

A 24 says: this is **not** a risk-acceptable initiation as proposed, and it is
**illegal at the hypothesized 10% size** on the tape's own volatility. Upside is not
my department; survival is. The veto is not moved by return arguments (KeyBanc $400,
the AI-inflation narrative) — those are the market's assumptions, not the firm's.

**Escalation note to CEO/Owner (repeat of the MU standing item):** `config/portfolio.yaml`
remains empty (`holdings: []`, `cash_balance: 0.00`). Until it is populated, **no**
proposal from any department can receive an unconditional risk verdict — I can check
limit *fractions* but not a single dollar. Remediation: Owner enters holdings and cash;
I re-certify the pipeline against real numbers within one session. This gap does not
change today's MRVL verdict (the veto rests on valuation and timing, not on missing
dollars), but it caps every other name at "conditional" and must be closed.

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
