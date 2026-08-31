# Risk Review — Prospective NEW LONG: MU (Micron Technology)

**Author:** John, Chief Risk Officer (Dept. 6 — Risk Management)
**Date:** 2026-07-18 · **For:** Investment Committee / CEO 皮褸黃 / Owner
**Price context:** ~$806–853 (Jul 17 close ~$806.46 per 老詹; ~$850 intraday reference), −30% to −32% from the Jun 25 ATH ($1,255 intraday / $1,213.37 close) in three weeks. Realized daily ranges 5–9%.
**Inputs reviewed:** risk-limits.yaml, portfolio.yaml, Peterson (macro 40/100), 老詹 (technical 45/100), Tim Cook (structure), 王老吉 (flow: distribution ~70% conf.), 菲比斯 (narrow moat, 40–50% MoS demanded), LeBron James (geopolitical MEDIUM, Taiwan fat tail).
**Missing inputs:** Mo Peter VaR run — none on file. Mario stress test — none on file. Both are commissioned as binding conditions below.

---

## VERDICT: APPROVED WITH CONDITIONS

The proposal may proceed to committee. It may NOT proceed to a decision record or
execution ticket until every numbered condition below is satisfied. Two structural
defects force the conditional form:

1. **The portfolio state file is empty.** `config/portfolio.yaml` shows
   `holdings: []` and `cash_balance: 0.00`. I can verify limit *fractions* but not a
   single dollar. No sizing, no ticket, no trade until the Owner enters real data.
2. **The 10%-cap sizing assumption fails my gap-risk test.** The hypothetical 10%
   position passes the nominal limit checks but breaches `max_risk_per_trade` once
   gap risk is priced (see §2). Maximum permitted total MU exposure is **6.5% at
   cost**, not 10%.

---

## 1. Sizing arithmetic (the binding constraint)

Per-trade risk law: `max_risk_per_trade: 0.01` — position weight × distance to stop
≤ 1% of portfolio.

**Nominal stop distances (老詹, closing basis):**
- Zone A: entry ~$795, closing stop $760 (−4.4%), hard stop $745 (−6.3%).
- Zone B: entry ~$692, closing stop $655 (−5.3%), hard stop $645 (−6.8%).

**Naive solve:** 1% ÷ 4.4–6.3% supports a 15.9–22.7% position — i.e., on nominal
stop distance the 1% budget does NOT bind below the 10% cap; the cap would bind
first. **I reject the naive solve.** In this tape, nominal stop distance is a
fiction:

- Tim Cook: "gap risk is the dominant execution hazard" — catalysts are
  Asia-sourced (Seoul/Taipei/Beijing) and land before the US open; MU is *gapping*,
  not trending, on news. Stops are honored on a closing basis.
- Observed single sessions: −9%, −8%, −5.7%, −5.65%, −4.6% (Jul 13–17). Daily
  ranges 5–9%.
- A closing-basis stop at −4.4% therefore carries a realistic fill 8–15% below
  entry in a gap scenario (e.g., a −9% overnight gap that keeps running before the
  daily close confirms the stop).

**Gap-adjusted stop distance: −15% (estimate, marked as estimate — one bad
overnight gap through the stop, consistent with observed tape).**
Gap-adjusted solve: 1% ÷ 15% = **6.7% maximum total position**. I round down to
**6.5%** and require it staged.

| Sizing basis | Stop distance | Max size under 1% rule |
|---|---|---|
| Nominal, Zone A closing stop | 4.4% | 22.7% (cap binds at 10%) — REJECTED basis |
| Nominal, Zone A hard stop | 6.3% | 15.9% (cap binds at 10%) — REJECTED basis |
| **Gap-adjusted (CRO basis)** | **~15%** | **6.7% → capped at 6.5%** |

Cross-check at the hypothetical 10%: gap-adjusted loss = 10% × 15% = **1.5% of
portfolio — breach of the 1% per-trade budget. FAIL.** At 6.5%: 6.5% × 15% ≈
0.98% — passes at the limit.

---

## 2. Limit-by-limit check

Post-trade columns shown for (a) the CEO's hypothetical 10% position and (b) my
permitted 6.5% total / ~2.5% starter. Current book = empty (no holdings entered).

| Limit | Law | Current | Post-trade @10% (hypo) | Post-trade @6.5% (permitted) | Pass/Fail |
|---|---|---|---|---|---|
| max_single_position | 10% at cost | 0% | 10.0% (at limit) | 6.5% | @10%: PASS (at limit) / @6.5%: PASS |
| max_risk_per_trade | 1% (size × stop) | n/a | Nominal 0.44–0.63%: pass. **Gap-adjusted 1.5%: FAIL** | Nominal 0.29–0.41%; gap-adjusted ~0.98% | **@10%: FAIL (gap basis)** / @6.5%: PASS |
| stop_required | yes | n/a | 老詹 levels defined | Adopted as binding (Cond. 4) | PASS conditional |
| max_sector (semis/IT) | 35% | 0% | 10% | 6.5% | PASS |
| max_correlated_cluster (AI complex) | 40% | 0% | 10% | 6.5% | PASS — first AI-sleeve name; see §3 flag |
| cash_floor | ≥10% | **unverifiable — cash_balance 0.00** | ~90% if fully cash-funded | ~93.5% | PASS on assumption; **unverifiable until Owner enters data** |
| leverage | none | none | cash purchase assumed | cash purchase required (Cond. 5) | PASS conditional |
| max_var_95_1d | ≤3% of portfolio | 0% | ~0.91% (est.) | ~0.59% (est.) | PASS (estimate) — **no formal Mo Peter run; commissioned (Cond. 6)** |
| max_adv_participation | ≤5% of $ADV | n/a | <0.005% even at $1M order (Tim Cook) | same | PASS — no liquidity constraint |
| max_drawdown budget | 20% peak-to-trough | fresh book | −40% severe scenario = −4.0% portfolio (20% of entire budget on one name) | −40% severe = −2.6% portfolio (13% of budget) | @10%: legal but imprudent / @6.5%: PASS |
| committee_approval_required | yes | — | this review is the risk input | same | Pending committee |
| decision_record_before_ticket | yes | none exists | required | required (Cond. 9) | Pending |

**VaR estimate basis (marked as estimate, not a Mo Peter figure):** realized daily
sigma ~5.5% from Jul 13–17 closes (moves of −4.6%, −9%, −5.7%, +3.3%, −5.65% per
Dept. 5 reports). 95% 1-day VaR ≈ 1.65 × 5.5% ≈ 9.1% of position value → 0.91% of
portfolio at 10% weight, 0.59% at 6.5%, remainder in cash. Under the 3% ceiling in
both cases *only because the rest of the book is cash*. Formal run required before
any ticket.

---

## 3. Correlation & concentration assessment

- **Today:** MU would be the book's first and only position. No existing factor bet
  to concentrate. Nominal concentration risk is nil.
- **Forward flag (binding on Morris/Zac):** MU is a leveraged play on the same two
  factors as the entire planned AI sleeve — (1) hyperscaler AI capex and (2)
  Taiwan-strait manufacturing concentration. LeBron James: MU's leading-edge DRAM
  bits are majority-Taiwan through at least 2027, and any future NVDA/AI-accelerator
  holding is highly correlated on both factors. From day one, MU is booked against
  the **40% max_correlated_cluster** for the AI complex, and I am additionally
  opening a **Taiwan-concentration factor ledger**: MU + any future TSMC-dependent
  name share one fat left tail (severe scenario ~5–8% probability, −40%+ single-name
  impact). Nominal diversification across MU/NVDA/AVGO-type names would be
  concentration in disguise; every subsequent AI-sleeve proposal nets against this
  cluster.
- **Character of the name:** narrow-moat cyclical at record margins (菲比斯: median
  ~4% ROIC over 42 years, 34 drawdowns of 30%+), in confirmed daily downtrend under
  distribution (王老吉 ~70% conf.), in a hostile macro quadrant (Peterson 40/100).
  This is a high-volatility, high-gap-risk instrument and is sized as such — the
  6.5% cap is not negotiable upward on return arguments.

---

## 4. Binding conditions (each is a hard gate; breach of any = position closed / ticket void)

1. **Portfolio data first.** The Owner must populate `config/portfolio.yaml` with
   real `cash_balance` and any existing holdings. Every fraction in this review is
   re-run against real dollars by Zac and re-checked by me before a ticket is cut.
   Until then this verdict authorizes committee discussion only — nothing else.
2. **Size:** total MU exposure ≤ **6.5% of portfolio at cost**. The 10%
   single-position cap is NOT the operative limit for this name; gap-adjusted
   per-trade risk is. Starter tranche ≤ **2.5%**.
3. **Entry discipline (老詹's plan is binding):** starter only in Zone A ($780–805)
   *after* the stabilization trigger (daily close > $830 with RSI higher low) — no
   buying the touch; add in Zone B ($680–705) only per plan; alternative momentum
   entry only on daily close > $930. **No entries in the $830–895 no-trade zone.**
   Limit orders only, no market orders at the open, no resting overnight orders
   (Tim Cook's execution notes bind 死潘狗/Messi).
4. **Stops are law:** Zone A — exit on daily close < $760, hard intraday $745.
   Zone B — daily close < $655, hard $645. Momentum entry — stop < $860. Trend
   invalidation: two daily closes (or one weekly close) below **$678** = exit the
   entire position; re-entry requires a fresh committee review. No averaging down
   through any stop.
5. **Funding:** cash purchase only, no margin (leverage: none is a hard rule). No
   options overlay without C朗 pricing, covered-only, and separate risk sign-off;
   note IV is pumped — spreads over outright premium if hedging.
6. **Commission before ticket:** Mo Peter formal 1-day 95% VaR on the sized
   position; Mario stress test covering at minimum (a) Taiwan
   blockade/quarantine (−40%+ scenario), (b) formal BIS HBM export rule with
   third-country scope, (c) 2027 memory-glut margin normalization, (d) truce lapse
   Oct–Nov 2026. Both filed in `reports/risk/` before the decision record.
7. **Cluster ledger:** MU is booked against the 40% AI-complex cluster cap and the
   Taiwan factor ledger from inception. Any subsequent AI/semis proposal must show
   the post-trade cluster total in its risk review.
8. **Tripwire monitoring (assigned):** The dictator + LeBron James to watch: BIS
   Federal Register HBM rule; truce extension/lapse by ~Nov 1, 2026; CXMT IPO
   pricing and DDR5 yield claims; 2027 HBM contract pricing direction (set ~Q4
   2026); Micron HBM share < 20%. Any tripwire firing triggers an immediate
   re-review of the position at current size.
9. **Process:** committee approval, then decision record in `memory/decisions/`
   (with this review's conditions attached and any dissent recorded), then and only
   then an execution ticket in `reports/execution/` for the Owner. No live trading.

---

## 5. Risk score (committee input): **38 / 100**

Scale: higher = more risk-acceptable to initiate as proposed. Rationale:

- **Against (dominant):** realized daily vol 5–9% with overnight-gap regime;
  confirmed daily downtrend under active distribution (~70% conf.); insider selling
  at 16-year high; narrow-moat deep cyclical at record (shortage) margins with a
  documented history of −30%+ drawdowns; hostile late-cycle macro (40/100); Taiwan
  fat tail through 2027; no VaR/stress work on file; **no real portfolio data on
  file**.
- **For:** first position in an empty book (no existing concentration); mega-cap
  liquidity with zero participation constraint; well-defined technical invalidation
  levels; contract-backed 2026 HBM demand caps near-term fundamental downside; at
  6.5% gap-adjusted size, worst plausible single-name outcome (−40% severe
  scenario) costs ~2.6% of portfolio — survivable within the 20% drawdown budget.

A 38 says: this is a legal trade at the *conditioned* size and entry plan, and an
illegal one as hypothesized at 10%. Upside is not my department; survival is. The
conditions are binding on Zac and 死潘狗.

**Escalation note to CEO/Owner:** the empty `config/portfolio.yaml` is itself a
standing control gap — until it is populated, *no* proposal from any department can
be given an unconditional risk verdict. Remediation: Owner enters holdings and cash
balance; I re-certify this review against real numbers within one session.

---

*Limit citations: `config/risk-limits.yaml` (2026-07-18). All market figures from
the cited department reports of 2026-07-18; volatility-based VaR and gap-adjusted
stop distances are marked estimates. Research and decision support, not financial
advice.*

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
