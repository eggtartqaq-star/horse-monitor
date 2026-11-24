# CRO Ruling — Swing-account single-position notional cap (CL-3 / D-03 review)

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-24
**Subject:** Whether to keep, raise or replace the 10% single-position notional cap adopted in V6.4.2
**Status:** FINAL, 2026-11-24. Built on the corrected lab (Tom F-1/F-2) and both signal paths (F-3).

---

## 0. Verdict

**APPROVED WITH CONDITIONS: a narrow amendment, path-dependent. Flat 15% is not recommended (not vetoed). 20% and "no cap" are VETOED.**

1. **The 10% cap stays operative today.** It stays on the scanner path until that path's rules are validated.
2. **Construct B′ is cleared on risk.** B′ means 10% for every position, except that an Engine 2 entry may be **one share up to 15%** (US$192.31) if that share's risk to the stop is ≤ 1% (US$12.82).
   - Its worst trade is essentially the same as 10% flat (−1.09 / −1.06% per signal; ≤ −1.17% in any perturbed run).
   - Its median max DD is better than 10% on the scanner path (−3.40 vs −4.84).
3. **B′ becomes the recommended limit** if the Owner aligns his live scanner to the validated (backtest-path) rules, **and** costs, code tests and parity are verified (§5 gates G-1, V-1 to V-3).
4. **On the scanner path B′ fails the both-halves test I pre-registered** (base IS 1.51% vs 2.29%; it wins only 64% of perturbed runs), so there the recommendation lapses to keep 10%.
5. **Flat 15% is not recommended, but not vetoed.** On the scanner path it beats 10% in 93% of IS runs with better drawdown. Its edge over B′ comes from sizing Engine 1 and multi-share positions above 10%, which is where every loss above 1.25% of the account occurred (worst −2.19% / −1.67%).
6. **20% is vetoed** (the Owner may override). The worst observed same-night pair would cost 9.6% against the −10% monthly breaker, and it exceeds the firm's 15% at-market ceiling. Its strong scanner-path returns are recorded and do not move a tail-based veto.

**The CEO report's cap numbers (0.96% CAGR; "10% worst in both halves") are superseded** by Tom's F-1 and F-2. Corrected 10% = 2.21% CAGR (backtest path) / 0.81% (scanner path). A higher cap wins OOS on both paths in every run. IS is a coin flip on the backtest path and favours flat caps on the scanner path. The evidence rests mainly on 2025–26.

**How the scanner/backtest divergence (Tom F-3) affects this ruling:** it decides it.
- The two paths rank the options differently, and the scanner path, the one the Owner trades, runs on rules no one has validated (E2 OOS +0.17–0.20% per trade; −0.82% CAGR OOS at the current limit).
- A risk limit must be set for a defined system. **Escalated to the CEO and the Owner:** decide which rules are live (G-1) before any limit is changed.
- On the backtest path: B′. On the scanner path: 10% until its rules are validated, then re-decide on forward data under the test pre-registered in §5.

**On my July recommendation:** the mechanism was right. Gap loss scales with notional, and the multi-share 10% wall still earns its place. The calibration was wrong: a firm-book 10% was applied to single-share positions in a 2-slot account and shipped before the portfolio test (CL-5) I had specified to price it. See §6.

**Risk score: 74 / 100 for B′** (conditional, backtest path), **70 for keeping 10%**, 50 for flat 15%, veto for 20% and no cap.

## 1. Inputs read

| Input | Status |
|---|---|
| CEO report `reports/quant/2026-11-24-v642-real-code-v66-lab.md` (§4–§6) | Read in full |
| `strategy/v6.6/README.md`, `lab.py`, `rules_v642.py::position_plan`, `results/caps.csv`, `results/summary.csv` | Read. **`--mode caps` re-run independently into scratchpad: all 30 rows of `caps.csv` reproduced to the second decimal.** |
| My July ruling `reports/risk/2026-07-30-v64-risk-review.md` (C-1, §4.3, CL-3, CL-5, CL-8, escalation item 2) | Re-read |
| `strategy/v6.5/risk_config.py` (`RiskLimits`) and `config/risk-limits.yaml` | Read |
| Tom's review `reports/quant/2026-11-24-v66-lab-tom-review.md` | Read in final form. **It refutes the CEO's cap numbers**: F-1 slot bug (HIGH), F-2 MSTR split, F-3 scanner ≠ backtest (HIGH), F-5 CEO report must be reissued. The ruling below is built on the corrected lab. |
| CEO correction (coordinator message, 2026-11-24) and `bt/results2/caps.csv` | Corrected cap table on both signal paths; A, D and F re-run by me with identical output |
| Webull read-only daily bars, 38 names + SPY (scratchpad `bt/data/`, split-adjusted; un-adjusted for sizing via lab `SPLITS`) | Used for all new measurements below |
| Mo Peter (VaR) / Mario (stress) | Not available in this session. I computed an **interim** historical 1-day VaR on the pre-correction simulation (§8), indicative only; formal runs commissioned in §5. |

**My own measurement tooling (scratchpad, not shipped):** an instrumented copy of `lab.py` that additionally records each trade's initial stop and whether the exit was a gap through the stop (`px < stop`), plus a hook that lets `position_plan` see the engine. No signal rule, fill rule or cost assumption was changed. Scripts are in `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/cro/` (`lab_f3.py` = corrected lab plus instrumentation, `f3.py`, `f3b.py`, `pertrade_tom.py`, `perturb.py`, `gaps.py`; the earlier `lab_cro*.py` runs are pre-correction and superseded).

Window: tradeable 2022-11-30 → 2026-11-23, IS to 2024-12-31, OOS after. **All return and drawdown figures in §2, §4, §5 and §8 are from the corrected lab** unless marked pre-correction. Account US$1,282.05 (HK$10,000 / 7.8). All "derived" numbers below are my arithmetic on these sources.

## 2. What the corrected backtest shows about the cap

> **The CEO report's cap numbers (§4–§5: 10% = 0.96% CAGR, "10% is worst in both halves") are superseded.** Tom found and fixed:
> - **F-1:** an unaffordable signal held a slot overnight, blocking an affordable candidate.
> - **F-2:** the MSTR 10:1 split (2024-08-08) was missing from `SPLITS`.
> - **F-3:** the Owner's daily scanner (`daily_strong_signals.py`) does **not** emit what the backtest tests. E2 has no 20-day breakout gate, and E1 is strong-tier only (RSI2 < 10 and R ≥ 3). The CEO confirmed this in the source.
>
> Everything below uses the corrected lab (`strategy/v6.6/lab.py` working copy, with Tom's fixes) and reports **both** signal paths. I re-ran A, D and F myself on both paths and reproduce the CEO's corrected figures (scratchpad `bt/results2/caps.csv`) exactly.

**What the 10% cap does.** Under `position_plan()`, shares = min(⌊US$12.82 / per-share risk⌋, ⌊US$128.21 / price⌋). The 1% risk rule alone already caps notional at 1% ÷ stop% (derived: 20% at a 5% stop, 12.5% at 8%, 8.3% at 12%). So the cap does two different jobs:

1. **Multi-share, tight-stop positions** (the July C-1 case). The cap stops a "1% risk" position from becoming a large gap exposure. **This job is valid, and §3 confirms it.**
2. **Single-share positions in US$128–256 names.** One share already exceeds US$128.21, so the trade is blocked outright, although the 1% rule would allow 1 share at 10–20% notional. This is the **share-price barrier**.

**Corrected cap table, 2 slots, CAGR % ALL / IS / OOS · max DD % (ALL):**

| Cap | Backtest path (validated rules) | Scanner path (what the Owner trades) |
|---|---|---|
| 10% (V6.4.2) | 2.21 / 1.82 / 2.62 · −4.49 | 0.81 / 2.29 / **−0.82** · −4.87 |
| 15% | 3.90 / 2.07 / 4.88 · −5.86 | 3.16 / 2.43 / 4.08 · −3.45 |
| 20% | 5.68 / **1.01** / 10.00 · −6.61 | 4.51 / 4.04 / 5.49 · −3.77 |
| none | 2.49 / **−0.01** / 6.01 · −8.89 | 4.16 / 4.36 / 4.28 · −3.77 |

Source: `bt/results2/caps.csv` (CEO, corrected lab); A, D and F re-run by me with identical output.

**What survives the corrections:**

- **OOS (2025–26): 10% is the worst setting on both paths.** Tom: 15% beats 10% in 100% of 48 perturbed backtest-path runs.
- **IS (Dec 2022–2024) is a coin flip on the backtest path.** 15% beats 10% in 58% of Tom's runs; 20% and none lose to 10%. On the scanner path at base, 15% and 20% beat 10% (§4 tests whether that is robust).
- **The cap's measured cost comes mainly from one regime**, 2025–26, when the mega-cap trend names a US$128 cap excludes did very well (Tom §5). That is one regime, not a structural law.

**Price-band check on actual prices** (lab `raw_factor`, with MSTR fixed). Backtest path, E2 gross EV per trade:

| E2 entry price (actual) | IS | OOS |
|---|---|---|
| ≤ US$128.21 | +0.25% (61) | +0.08% (29) |
| US$128–250 | +2.07% (59) | +3.10% (33) |
| > US$250 | +1.90% (93) | +0.55% (75) |

Bootstrap of the (US$128–250) minus (≤ US$128) difference (E2 per-trade SD 8.9pp):
- IS: +1.82pp, 90% CI [−0.65, +4.35], P(≤ 0) = 0.12.
- OOS: +3.02pp, [−1.14, +7.27], P(≤ 0) = 0.12.

Same direction in both halves; neither half significant. The bootstrap is iid on time-clustered trades, so the true CIs are wider. **I do not rely on the band effect.**

## 3. Gap-through-stop risk quantified (10% / 15% / 20% / alternatives)

### 3.1 The gap census: 38 names, 2022-11-30 → 2026-11-23 (37,962 name-days)

Overnight gap = Open(t) / Close(t−1) − 1, from Webull daily bars (split-adjusted, so splits do not show up as gaps).

| Gap at least this bad | Count | Per name-year (derived) |
|---|---|---|
| −10% | 54 | 0.36 |
| −15% | 12 | 0.08 |
| −20% | 4 | 0.03 |
| −25% | 2 | 0.01 |

Worst single gaps: **MSTR −27.4% (2024-08-05)**, INTC −25.8% (2026-10-30), INTC −24.5% (2024-08-02), COIN −20.8% (2024-08-05), NKE −18.1% (2024-06-28), CRM −17.8% (2024-05-30), UNH −17.6% (2025-04-17). The median name's worst gap was −11.4%. **The worst same-night pair was 2024-08-05 (MSTR + COIN, both crypto-linked), averaging −24.1%.** That is the 2-slot correlated tail.

**The finding that matters for cap design.** Measured in multiples of the prior day's ATR, the worst gaps are in **low-volatility** names: NKE 9.4×ATR, SBUX 8.7×, CRM 8.1×, UNH 6.7×, LLY 6.6×. Engine 2's stop is 3×ATR, so a low-ATR name gets a tight stop and therefore the largest risk-sized notional, and those are the names whose gaps most exceed their ATR. An ATR stop under-prices exactly this tail. **The notional cap's legitimate job is to bound multi-share, tight-stop positions in names whose gaps are large relative to their ATR.** The census supports that job.

### 3.2 What gaps actually cost: every signal, sized at each cap

I sized every `per_trade` signal (next-open fills, every signal taken) at each cap. Sizing uses actual share prices (MSTR split included) and **gap-through-stop fills for both engines**. The lab's `PER_TRADE` inherits `e1_gap_fill=False`, so I switched it on; see §7. Loss is gross P&L as a % of the US$1,282 account.

| Sizing rule | Backtest path (1,087 signals): worst trade · count < −1.25% / < −2% | Scanner path (631 signals): worst trade · count < −1.25% / < −2% |
|---|---|---|
| A. 10% flat | **−1.09%** · 0 / 0 | **−1.06%** · 0 / 0 |
| **B′. 10% + 1 share ≤ 15%, E2 only** (§4) | **−1.09%** · 0 / 0 | **−1.06%** · 0 / 0 |
| B. 10% + 1 share ≤ 15%, both engines | −1.26% · 1 / 0 | n/a |
| D. 15% flat | −2.19% · 5 / 1 | −1.67% · 2 / 0 |
| F. 20% flat | −2.19% · 5 / 1 | −1.67% · 3 / 0 (CAT E1, 1 share = 18.6%: −1.50%) |
| G. no cap | −6.57% · 6 / 2 (max notional 364.7%) | −3.81% · 4 / 1 (CRM E1, −3.81%) |

**Where the tail comes from, on both paths.** Every trade that lost more than 1.25% of the account was an **Engine 1 position sized above 10%** and held through a gap:

- NKE E1, entered 2024-06-17 with a 2.19% stop, 2 shares = 13.5%, held into the −18.1% gap of 2024-06-28: −2.19% (−1.09% at a 10% cap).
- NKE E1 2025-03-25, 2 shares: −1.67%.
- PFE E1 2023-12-04, 8 shares: −1.41%.
- TSLA E1 2024-04-16, 1 share: −1.26%.

**Engine 2 losses never exceeded about 1.02% of the account at any cap, on either path.** Its trailing stop has usually ratcheted up by the time a gap arrives.

**"No cap" is vetoed outright.** A notional of 364.7% is leverage, a breach of `leverage: none`, and it is exactly the July C-1 failure.

### 3.3 Stress arithmetic beyond the sample

The sample is survivor-selected (F-01: a 2026 universe) and contains no 2022-style bear market (CEO report, NOT OBTAINED items 6–7). So I also bound the tail arithmetically. Loss ≈ notional × gap measured from entry. The 40% row is an **assumption**, a gap larger than anything in the sample, chosen because survivorship hides the names that did worse.

| Scenario | 10% flat | B′ (E2 1-share ≤ 15%) | 15% flat | 20% flat |
|---|---|---|---|---|
| Single name, worst observed gap −27.4% | 2.7% | 4.1% (1 share) / 2.7% (multi) | 4.1% | 5.5% |
| Both slots, worst observed pair −24.1% | 4.8% | 7.2% max | 7.2% | 9.6% |
| Single name, −40% (assumption) | 4.0% | 6.0% / 4.0% | 6.0% | 8.0% |
| Both slots, −40% each (assumption) | 8.0% | 12.0% max | 12.0% | **16.0%** |
| Owner's monthly breaker −10%: tripped in one night by the observed pair? | No | No | No | No (9.6%, near it) |
| Interim 1-day VaR95 / VaR99 on invested days (**pre-correction** sim, indicative only) | 0.31 / 0.65% | 0.36 / 0.68% (B) | 0.41 / 0.73% | 0.51 / 0.92% |

At 20%, the worst **observed** correlated pair costs 9.6% of the account in one night, effectively the whole monthly breaker. At 15% (either form), that pair costs 7.2%, which leaves headroom. 15% is also the firm's own `max_single_position_drifted: 0.15` in `config/risk-limits.yaml`, the most the firm tolerates in one name at market. I anchor on that.

### 3.4 What the backtest cannot show

- Earnings dates are not in any backtest (CEO, NOT OBTAINED 3). The gaps above **are** in the price data, so earnings gaps are counted. The entry guardrail ("no entry within 5 days of earnings") is missing, so the backtest **over**-states entry-side earnings exposure.
- That guardrail does **not** cover holding periods. E1 holds up to 10 days and E2 up to 60 (`rules_v642`), and the NKE −2.19% case was entered 8 trading days before earnings. A live position will cross earnings whatever the entry guardrail says.
- Fat-tail events absent from a 4-year survivor sample: halts, fraud and crash gaps.

These are reasons to keep a ceiling. They are not reasons for that ceiling to be 10% for a single share.

## 4. Ruling on the construct

### 4.1 Constructs tested on the corrected lab, both signal paths (2 slots, `as_traded`; only sizing changes)

| Construct | Backtest path: CAGR ALL / IS / OOS · DD · worst trade | Scanner path: CAGR ALL / IS / OOS · DD · worst trade |
|---|---|---|
| A. 10% flat (V6.4.2) | 2.21 / 1.82 / 2.62 · −4.49 · −1.04 | 0.81 / 2.29 / −0.82 · −4.87 · −1.04 |
| **B′. 10% + 1 share ≤ 15%, E2 only** | **3.66 / 2.31 / 5.09 · −4.20 · −0.84** | **1.74 / 1.51 / 2.02 · −3.35 · −0.87** |
| B. 10% + 1 share ≤ 15%, both engines | 3.28 / 1.28 / 4.59 · −4.96 · −0.95 | 2.48 / 1.51 / 3.63 · −3.43 · −0.87 |
| C. E2 15% / E1 10% | 3.90 / 2.61 / 5.39 · −4.39 · −0.84 | 2.18 / 2.12 / 2.31 · −3.55 · −0.87 |
| D. 15% flat | 3.90 / 2.07 / 4.88 · −5.86 · −1.69 | 3.16 / 2.43 / 4.08 · −3.45 · −1.69 |
| F. 20% flat | 5.68 / 1.01 / 10.00 · −6.61 · −1.69 | 4.51 / 4.04 / 5.49 · −3.77 · −1.69 |

Sources: my runs on an instrumented copy of the corrected `lab.py` (scratchpad `cro/lab_f3.py`, `f3_base.csv`, `f3b_base.csv`). A, D and F match the CEO's corrected `caps.csv` exactly.

**Path perturbations** (base, 7 start shifts, 20 random within-engine picks: 28 runs each; Tom's method). "P(beats A)" is the share of runs in which the construct's CAGR exceeds 10% flat.

| Perturbation stat (28 runs each) | Backtest path | Scanner path |
|---|---|---|
| P(B′ beats A), IS / OOS / ALL | **0.61** (median +0.50pp) / 1.00 / 1.00 | **0.64** (median +0.89pp) / 1.00 / 1.00 |
| P(C beats A), IS | 0.68 | 0.64 |
| P(D 15% beats A), IS | 0.64 | **0.93** (median +1.69pp) |
| P(F 20% beats A), IS | n/a (Tom: 20% < 10% at base) | **1.00** (median +1.83pp) |
| Median ALL max DD: A / B′ / C / D / F | −4.60 / −5.08 / −5.34 / −6.09 / n/a | −4.84 / **−3.40** / −3.67 / −3.62 / −3.99 |
| Worst ALL max DD over runs: A / B′ / D / F | −5.38 / −9.34 / −9.53 / n/a | −6.70 / −6.24 / −6.50 / −5.76 |
| Worst single trade in any run: A / B′ / D / F | −1.11 / −1.11 / −1.69 / n/a | −1.07 / −1.17 / −1.69 / −1.69 |

Sources: scratchpad `perturb.csv` (backtest path, my run) and `f3_perturb.csv` (scanner path). Tom's independent 48-run backtest-path test: 15% beats 10% in IS in 58% of runs.

**Note on the −9.34% backtest-path worst case for B′.** It is a 14-month run of small losses in 2023, each at most about −1% of the account and mostly in positions at or under 10%, with a worst month of −1.76%. It is path dispersion from different trade selection, not gap risk.

### 4.2 Reading the two paths together

1. **OOS (2025–26): every alternative beats 10% on both paths, in every run.** This is robust, but it is one regime.
2. **IS on the backtest path: nothing robustly beats 10%** (Tom 58%; my runs 61–68%).
3. **IS on the scanner path: the flat caps win robustly** (D 93%, F 100%). The constructs that keep E1 and multi-share positions at 10% win only 64% of the time. **The robust part of the scanner-path IS gain therefore comes from sizing E1 and multi-share positions above 10%**, which is where every loss above 1.25% of the account occurred (§3.2). It buys return with the gap-tail engine. B′'s base-path IS loss (1.51 vs 2.29) sits in the unlucky third of its own distribution, but it is a loss.
4. **Drawdown does not favour 10%.** On the scanner path every alternative has a better median max DD than 10%, B′ best (−3.40 vs −4.84). The 10% cap buys a smaller worst single trade (−1.07 vs −1.17 for B′, −1.69 for D and F), not a smaller drawdown.
5. **The divergence is the larger finding.** On the path the Owner actually trades, the current limit simulates −0.82% CAGR OOS, and Tom puts that path's E2 OOS edge at +0.17–0.20% per trade. Tuning a risk limit to flatter an unvalidated signal set would be backwards.

### 4.3 Ruling

> **The single-position limit may be amended, for the backtest-path system only, to: "No position may exceed 10% of the account (US$128.21), with one exception. An Engine 2 entry may be exactly one share of up to 15% of the account (US$192.31), provided that one share's risk to the initial stop is no more than 1% of the account (US$12.82). Engine 1 stays at 10% with no exception."** (construct B′)

| Option | Ruling | Reason |
|---|---|---|
| A. Keep 10% flat | **Operative today, and remains so on the scanner path** | B′ fails my pre-registered V-0 on the scanner path (§5); a limit should not be tuned to an unvalidated signal set |
| **B′. E2 single share ≤ 15%** | **APPROVED WITH CONDITIONS**, on the backtest path after gates G-1 and V-1 to V-3 | Tail-neutral on both paths; passes V-0 on the backtest path; removes only the share-price barrier |
| C. E2 15% / E1 10% | Not recommended; not vetoed | Lets multi-share E2 positions reach 15% at 3×ATR stops in low-ATR names, the 6–9 ATR gappers of §3.1. Loses IS on the scanner path. |
| B. 1 share ≤ 15%, both engines | Not recommended | Adds an E1 tail (TSLA −1.26%); loses IS on both paths |
| D. 15% flat | **Not recommended; not vetoed** | Breaches no survival limit, and on the scanner path it beats 10% in 93% of IS runs with a better median DD. But that extra return over B′ comes from E1 and multi-share positions above 10%, which raises the worst trade to −2.19% / −1.67%; on the backtest path its IS gain is a coin flip. The Owner may choose it knowingly; I do not recommend it. |
| F. 20% flat | **VETOED** (the Owner may override) | Worst observed same-night pair costs 9.6% against the −10% breaker, and a −40% pair (assumption) costs 16%. Above the firm's 15% `max_single_position_drifted`. IS 1.01 vs 1.82 on the backtest path. **On the scanner path its return case is the strongest of all (100% of IS runs) and its DD is fine. I record that plainly. It does not move a veto grounded in the one-night tail**, and I would reconsider only on forward data plus Mario's stress. |
| G. No cap | **VETOED** | Notional up to 364.7% is leverage |
| Per-name gap-risk cap | Hypothesis | Needs a look-ahead-free per-name gap estimate and its own validation |

**Honest disclosure.** B′ was shaped after seeing this data, so its backtest numbers are in-sample to this decision. What protects the Owner is that it does not depend on the return evidence being right: it adds no measured risk. Where it does fail the return test (the scanner path), I have applied my own pre-registered rule against it.

**Firm limits are not changed.** `config/risk-limits.yaml` governs the firm book and stays as written. The swing-account limit is the **Owner's personal limit**. This is a proposal to him; `MAX_POSITION_PCT` in his V6.4.2 code, and `RiskLimits` in `strategy/v6.5/risk_config.py`, change only if he adopts it.

## 5. Is the evidence strong enough? Validation protocol

**Short answer:** the evidence is **not** strong enough to claim the system earns more at a higher cap. Tom's own words: the direction "rests on 2025–26 alone". The evidence **is** strong enough on one point: the **E2 single-share exception (B′) adds no measurable tail on either signal path.** So B′ may be adopted on the narrow ground that it removes a share-price barrier without adding risk, but only where it also passes the Owner's own both-halves rule.

| Question | Evidence | Strength |
|---|---|---|
| Does a higher cap earn more? | ~45–67 trades per half; E2 per-trade SD 8.9pp. IS is a coin flip on the backtest path (Tom 58%), but robust for flat 15–20% on the scanner path (93–100%). The two paths disagree, and the scanner path's rules are themselves unvalidated. | **Weak to moderate, and path-dependent.** Do not quote any higher-cap CAGR as an expectation. |
| Is 10% the worst setting OOS? | Both paths; 100% of Tom's runs | **Moderate, one regime (2025–26)** |
| Does B′ add tail risk? | Worst trade equal to 10% on both paths (−1.09 / −1.06 per-signal); max DD better at base on both paths (−4.20 vs −4.49; −3.35 vs −4.87); exception-tier worst −0.78% | **Adequate for a bounded change** |
| Do flat 15% or 20% add tail risk? | Worst trade −2.19% (bt) / −1.67% (scan), every case an E1 position above 10%; 20% pair stress 9.6% | **Yes.** 15%: not recommended (not vetoed). 20%: vetoed. |

### V-0, the test I pre-registered for Tom's corrections, applied honestly

Earlier in this ruling I pre-registered that B′ stands only if, on Tom's corrected simulator, (a) its worst trade and max DD are no worse than 10% flat by more than 0.5pp, and (b) its CAGR is not below 10% flat in either half.

| Path | (a) tail and DD | (b) both halves at base | Perturbations: P(B′ beats A in IS) | V-0 |
|---|---|---|---|---|
| Backtest (validated rules) | Pass at base (−0.84 vs −1.04; −4.20 vs −4.49). Disclosed: the perturbed worst path is −9.34 vs −5.38, from small-loss dispersion, not gaps (§4.1) | Pass (IS 2.31 vs 1.82; OOS 5.09 vs 2.62) | 0.61 (median +0.50pp) | **PASS** (IS robustness marginal) |
| Scanner (what the Owner trades) | Pass (−0.87 vs −1.04; −3.35 vs −4.87) | **FAIL** (IS 1.51 vs 2.29) | 0.64 (median +0.89pp) | **FAIL** on the test as written → recommendation lapses to **keep 10%** on this path |

**I will not move the goalposts.** On the scanner path B′ fails the test I set before seeing those numbers, so on that path the operative limit stays 10%. The perturbation result (64%, median +0.89pp) says the base path was somewhat unlucky. It is recorded, but it was not the test I set, and 64% is not robust either. Per signal, B′-tier E2 trades do outperform the E2 trades that 10% can already size, in all four cells (bt IS/OOS +0.91/+4.36% vs +0.05/−1.27%; scan +1.16/+2.99% vs +0.79/0.00%; 9–40 trades per cell). The scanner-path portfolio shortfall is therefore slot allocation (B′ trades displace E1 trades), not worse trades. That is worth watching forward, but it is not a reason to override V-0.

### Gates before any change reaches real capital

- **G-1. Resolve the signal path (Tom F-3).** The Owner decides whether the live scanner is aligned to the validated rules (E2 breakout gate, E1 as backtested) or stays as it is. **The cap ruling follows the path:**
  - **Aligned to the backtest path:** adopt B′ once V-1 to V-3 pass.
  - **Scanner kept as is:** 10% flat stays. The scanner's rules must be validated on their own before any limit is tuned to them; that is a bigger issue than the cap (−0.82% OOS CAGR at the current limit). The scanner-path cap is then re-decided on **forward shadow-ledger data**, not this window. The test is pre-registered now: a construct must beat 10% flat in at least two-thirds of perturbed runs **in each half**, with a worst single trade no worse than −1.5% of the account. On today's data, B′ (64%) and C (64%) fall just short, and D and F (worst trade −1.69%) fail the tail clause.
- **V-1. Costs (July CL-7, still open).** One real Webull contract note covering commission, platform fee, SEC/TAF and FX. If there is any fixed per-order charge, re-run `as_traded` at that fee. If net EV ≤ 0, the system does not trade at this size under any cap.
- **V-2. Code, structurally enforced.**
  - The construct lives in one function, reads from one config, and its `assert` is added to the scanner's version stamp. The scanner also prints which **signal path** it runs.
  - The CEO's README snippet `assert E.MAX_POSITION_PCT == 10.0` must be **replaced**, not deleted.
  - Unit tests:
    - $200 stock, 2% stop → BLOCK.
    - E2 $150 stock, 7% stop → 1 share.
    - E1 $150 stock, 7% stop → BLOCK.
    - E2 $195 stock → BLOCK.
    - E2 $185 stock, 7.5% stop (1-share risk $13.88 > $12.82) → BLOCK.
    - $60 stock, 5% stop → 2 shares, not 3.
- **V-3. Parity.** `parity_check.py` passes on the Owner's PC, using Tom's tightened metric (F-6).

### Forward test: a risk test, not a return test

- **Shadow ledger, starting now on either path.** Every scanner signal is logged with its size under A (10% flat), B′ and D (15% flat), whether or not it is traded. This costs nothing and is the only clean way to get the out-of-sample A/B data that four over-examined years cannot provide.
- **Paper first.** If the account is still in the July CL-8 paper phase, B′ runs in paper.
- **Horizon.** Review at **30 closed E2 trades or 6 months, whichever is later**. This is not "20 trades side by side": the CEO's §6.5 puts the 20-trade E2 CI at about ±3.3pp. **No return comparison between caps before 100 forward trades.**
- **Pre-registered stop conditions.** Any one reverts the account to 10% flat immediately; the firm is informed; there is no re-argument inside the test.
  - **S1.** An exception-tier position loses more than **2.0% of the account**.
  - **S2.** Any sizing breach: a multi-share position above 10%, E1 using the exception, a share above US$192.31, or a scanner running an unstamped path. This also resets the CL-8 counter.
  - **S3.** The −10% monthly breaker trips while an exception-tier position is open.
  - **S4.** V-1 shows net EV ≤ 0 at the real fee.
- **Earnings log.** For every exception-tier position, record whether an earnings date fell inside the hold.

**Commissioned (Dept 6), before any real-capital change:**

- **Mo Peter:** 1-day 95% VaR on the maximum-exposure B′ book against the 3% ceiling.
- **Mario:**
  - a replay of 2024-08-05 at maximum B′ exposure;
  - a −40% single-name gap (assumption);
  - a −10% index gap with both slots in one sector.

**No further raise on this data.** Raising beyond 15%, or letting E1 exceed 10%, may only be argued on data collected after 2026-11-24.

## 6. Owning the July recommendation

**Verdict on myself: the mechanism was right and the calibration was wrong. I shipped the limit without the pricing that I myself said it needed.**

**What I got right, which the backtest confirms:**

- July C-1 said that gap loss is bounded by notional, not by stop distance, and that 1%-risk sizing turns tight stops into large notionals. §3 confirms both in this firm's own data:
  - The worst gaps in ATR terms are in low-volatility names (NKE 9.4×ATR).
  - Every trade that lost more than 1.25% of the account at a 15–20% cap was an Engine 1 position above 10%, mostly multi-share with a tight stop (NKE E1: 2.19% stop, −2.19% of the account at 15%, −1.09% at 10%).
  - With no cap, notional reaches 364.7%. The multi-share 10% wall I recommended still earns its place, and B′ keeps it.

**What I got wrong:**

1. **I imported a firm-book number into a 2-slot account without re-deriving it.** The 10% is `config/risk-limits.yaml`'s `max_single_position`, a limit built for a diversified book. I paired it with **5** concurrent positions (CL-3: 5 × 10% = 50% deployed). The Owner chose **2**. At 2 × 10% the account is at most 20% deployed and at least 80% in cash, far above anything my own 10% cash floor called for. When the slot count changed, the cap needed re-deriving and I did not ask for that. That miss is mine.
2. **I treated two different exposures as one.** My July §4.3(b) argument, that one share above US$128.21 breaches concentration, applied the multi-share logic to single-share positions. A single share's notional is already bounded by the 1% rule (1% ÷ stop%, ≤ 20% at a 5% stop). The single-share case needed its own, looser ceiling. I wrote one number for both.
3. **I specified the test and let the limit ship without it.** CL-5 required a portfolio-level backtest "under CL-3's caps". That is this backtest. It was blocked on market data in July and arrived four months later. I should have marked CL-3's 10% figure **provisional pending CL-5** rather than final. A limit that has not been priced should say so.

**What the backtest cannot show, and why the July cap was still defensible as an emergency control:**

- In July the account had just recorded a ≥2.3x leverage breach (BAC, 2026-07-18) and two overrides in six trading days, and every guardrail was a display. The backtest assumes perfect rule execution. The July cap was partly a **behavioural** containment, and the backtest cannot price that value.
- The Sep screenshots (CVX US$209 at about 16%; PFE 8 shares = US$229 at about 18%; CEO §6.6) suggest the cap was not even running in the scanner then. Tom's F-3 shows the daily scanner does not emit the backtested rules at all. Both tell against the control's effectiveness, not in favour of it.
- A 4-year, survivor-selected, bull-dominated window cannot show the tail the cap insures against. §3.3's arithmetic is my answer to that, and it is why B′ keeps a ceiling at all.

**Net cost of my error (derived, corrected lab):**

- **Backtest path:** 10% earned US$116 over four years, vs US$197 (B′) and US$211 (15% flat). That is about **US$80–95 foregone, all of it in 2025–26.** In-sample the cap cost nothing robust: Tom's runs make it a coin flip.
- **Scanner path:** US$42 vs US$91 (B′) and US$169 (15%).

In money this is small. The larger cost is model risk. For four months the account validated a system in which the share-price barrier shut E2 out of US$128–192 names. On the scanner path the live system ran at **−0.82% CAGR OOS** under my limit (corrected `caps.csv`). A process-validation account testing a distorted process is the real loss in Dept 6 terms.

**Lesson for 腦大裝草 (memory):** a limit copied from another book must be re-derived for the target's slot count and lot size, and must be marked provisional until a portfolio simulation prices it.

## 7. Other risk issues in the CEO's report

| # | Issue | CRO position |
|---|---|---|
| 7.1 | **`PER_TRADE` inherits `e1_gap_fill=False` from `AS_TESTED`** (`lab.py`, `PER_TRADE = replace(AS_TESTED, ...)`). E1 stop exits fill at the stop even when the open gapped through it. | With gap fills on, E1 `per_trade` net is **IS +0.23% / OOS −0.16%** (ALL +0.05%), vs the reported +0.39 / −0.03. E2 is unaffected (its gap fill is unconditional). This strengthens "E1 has no edge" and matters for risk: E1 is where the gap tail is. `as_traded` already has gap fills on. Fix: set `e1_gap_fill=True` in `PER_TRADE`. Referred to Tom. |
| 7.2 | **Slot reservation for unaffordable signals** (Tom F-1, HIGH). | Confirmed and fixed by Tom. I found the same mechanic independently. The CEO's headline figures (0.96% / +US$50, "10% worst in both halves") are artefacts of it, and **the CEO report must be reissued** (Tom F-5). This ruling uses only corrected numbers. |
| 7.2a | **Scanner/backtest divergence** (Tom F-3, HIGH). The Owner's daily scanner has no E2 breakout gate and lists only strong-tier E1. | **This is a bigger risk issue than the cap.** The Owner trades a signal set that was never validated: Tom puts scanner-path E2 OOS at +0.17–0.20% per trade vs +0.86%, and under the current 10% limit the scanner path simulates **−0.82% CAGR OOS**. A risk limit cannot be calibrated for a system that is not defined. **Escalated** (§0): the Owner must choose which rules are live, and the scanner must print a version and path stamp. |
| 7.3 | **Price bands on split-adjusted prices.** | Re-cut on actual prices, the direction holds and IS strengthens (§2). The CEO's caveat was adequate. |
| 7.4 | **Costs unverified.** The M2 stress (US$1/side) gives −1.9% CAGR (Tom: this side number does not reproduce; −2.6% in `summary.csv`). | Agree this is decisive. I add one point: **the cap and costs interact.** A fixed per-order fee costs more in percentage terms on a smaller notional (derived: US$1/side is 1.56% round trip on US$128, 1.04% on US$192). The cap decision and the fee check must be read together. V-1 is a gate, not a footnote. |
| 7.5 | **Earnings guardrail absent from all backtests.** | Agree, with a correction. The entry guardrail (5 days) does not protect **holds**: E1 holds 10 days and E2 up to 60, and the NKE −2.19% loss was entered 8 trading days before earnings. Live positions will cross earnings regardless. The backtest's earnings gaps are in the price data, so the gap tail is measured, not missing. Earnings log required (§5). |
| 7.6 | **Version drift.** The Sep scans show CVX at about 16% and PFE 8 shares at about 18% of the account. | **Escalated.** If trades were placed from those scans after V6.4.2 was adopted, those are realised breaches of the Owner's own personal limit, and PFE (multi-share, about 18%) would breach B′ as well. Request: the Owner confirms whether any order was placed from the 6 Sep or 28 Sep scans. The version stamp is endorsed, with the assert updated per V-2. |
| 7.7 | **`RiskLimits` drift.** `strategy/v6.5/risk_config.py` still says `max_open_positions = 5`; the Owner runs 2. | My own file disagrees with the live system, the same "limits arriving by accident" failure I warned about in July. If B′ is adopted, `RiskLimits` and `plan_position()` must encode B′ **and** `max_open_positions = 2`. Until then, V6.4.2 constants are the operative limits. |
| 7.8 | **CEO README: "paper-trade both caps side by side, 20 trades."** | Inconsistent with the CEO's own §6.5. 20 trades cannot separate the caps. Replaced by the shadow ledger and risk-based stop conditions (§5). |
| 7.9 | **"Drawdown barely moves because the 1% rule binds."** | Partly agree. Max DD in a survivor-selected bull window is the wrong measure of gap risk; the per-trade tail (§3.2) and stress arithmetic (§3.3) are the right ones. On those, flat 15–20% **does** move the tail (−2.19% vs −1.09% on the backtest path; −1.67% vs −1.06% on the scanner path), and B′ does not. |
| 7.10 | **The 2-slot correlated pair.** | Not discussed by the CEO. With 2 slots, both positions can sit in one cluster (2024-08-05: MSTR and COIN both gapped about 20–27%). B′ bounds that pair at 7.2% (derived) against the −10% breaker. No change proposed. Mario is to stress it. |
| 7.11 | **Idle-cash interest excluded from all CAGRs; universe chosen in 2026 (F-01).** | Agree with the CEO's disclosure. Neither obviously favours one cap over another, but survivorship biases the **gap tail downward**. Hence the 40% assumption row in §3.3. |

## 8. Limit-by-limit check

Measured against the swing account's operative limits (V6.4.2 constants, the Owner's manual, and my July personal-limit proposals). `config/risk-limits.yaml` is shown for reference; it governs the firm book. Post-change = B′. Corrected lab; "bt" = backtest path, "scan" = scanner path.

| Limit | Limit value | Current (A: 10% flat) | Post-change (B′) | Pass / Fail |
|---|---|---|---|---|
| Single position, multi-share | 10% | ≤ 10% | ≤ 10% (unchanged) | **PASS** |
| Single position, single share | 10% → **15% proposed** (= firm `max_single_position_drifted`) | ≤ 10% | ≤ 15% (US$192.31), E2 only | **PASS** under the proposed limit; Owner decision |
| Max risk per trade | 1% (US$12.82) | ≤ 1% | ≤ 1%; the exception requires 1-share risk ≤ 1% | **PASS** |
| Concurrent positions | 2 | 2 | 2 | **PASS** |
| Gross exposure / cash floor | cash ≥ 10% | max 20% gross | max 30% gross, cash ≥ 70% | **PASS** |
| Leverage | none (CL-1) | none | none | **PASS** |
| Sector / correlated cluster (firm ref.) | 35% / 40% | ≤ 20% | ≤ 30% | **PASS** |
| Monthly circuit breaker | −10% | worst observed pair gap 4.8% | worst observed pair 7.2%; −40% pair (assumption) 12.0% | **PASS** on observed data; fails only under an unobserved two-name 40% gap. Mario to stress. |
| Drawdown budget | 20% | base DD −4.49% (bt) / −4.87% (scan); perturbed median −4.60 / −4.84, worst −5.38 / −6.70 | base −4.20 / −3.35; perturbed median −5.08 / −3.40, worst −9.34 / −6.24 | **PASS** |
| Worst single trade | (no written limit; S1 sets 2%) | every signal −1.09% (bt) / −1.06% (scan); any perturbed portfolio run −1.11 / −1.07 | −1.09 / −1.06; −1.11 / −1.17 | **PASS**, essentially unchanged |
| 1-day VaR95 (firm ref. 3%) | 3% | interim 0.31% (pre-correction sim) | interim about 0.36% (B, pre-correction) | **PASS**, indicative only; Mo Peter to confirm |
| Stop discipline / max initial stop | never moved down; E2 12% / E1 15% | unchanged | unchanged | **PASS** |
| Signal path defined and stamped | (July H-6 / CL-6 spirit) | **NO**: scanner ≠ backtest (F-3) | must be resolved (G-1) | **OPEN, escalated** |
| Cost gate (CL-7) | net EV > 0 at the real fee | **UNVERIFIED** | **UNVERIFIED** | **OPEN**: V-1 |

## 9. Risk score input to committee

Scale as in July: 0 = do not deploy, 100 = clear at full size; higher is safer. These are **risk** scores; upside is not scored.

| Option | Score | Basis |
|---|---|---|
| A. Keep 10% flat | 70 | Smallest single-trade tail, but it does not buy drawdown protection (worst median DD of all options on the scanner path), and it keeps the share-price barrier distorting the system under test |
| **B′. E2 single share ≤ 15%** | **74**, conditional (about 80 once G-1, V-1 to V-3 and Mo Peter/Mario are done) | Tail equal to A on both paths; DD equal or better at base; bounded stress arithmetic |
| C. E2 15% / E1 10% | 62 | Multi-share E2 at 15% in low-ATR, gap-prone names |
| B. 1 share ≤ 15%, both engines | 58 | E1 exception widens the tail |
| D. 15% flat | 50 (not vetoed) | Worst trade −2.19% / −1.67% from E1 above 10%; robust IS gain only on the unvalidated scanner path |
| F. 20% flat | **VETO** (30) | Pair stress 9.6% against the −10% breaker; above the firm's 15% ceiling |
| G. No cap | **VETO** (10) | Leverage |

**Committee input: 74 / 100 for B′, conditional on G-1** (the Owner aligns the scanner to the validated rules) **and V-1 to V-3.** If the scanner path stays live, the input is **70 for keeping 10%**, and the committee's first item should be validating the scanner's own rules, not the cap. Conditions S1–S4 are binding on Zac and 死潘狗 for any tickets.

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

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
