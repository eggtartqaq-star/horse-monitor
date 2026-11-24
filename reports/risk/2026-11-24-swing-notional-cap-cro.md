# CRO Ruling — Swing-account single-position notional cap (CL-3 / D-03 review)

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-24
**Subject:** Whether to keep, raise or replace the 10% single-position notional cap adopted in V6.4.2
**Status:** DRAFT — being filled section by section

---

## 0. Verdict

_(pending)_

## 1. Inputs read

| Input | Status |
|---|---|
| CEO report `reports/quant/2026-11-24-v642-real-code-v66-lab.md` (§4–§6) | Read in full |
| `strategy/v6.6/README.md`, `lab.py`, `rules_v642.py::position_plan`, `results/caps.csv`, `results/summary.csv` | Read. **`--mode caps` re-run independently into scratchpad: all 30 rows of `caps.csv` reproduced to the second decimal.** |
| My July ruling `reports/risk/2026-07-30-v64-risk-review.md` (C-1, §4.3, CL-3, CL-5, CL-8, escalation item 2) | Re-read |
| `strategy/v6.5/risk_config.py` (`RiskLimits`) and `config/risk-limits.yaml` | Read |
| Tom's parallel review `reports/quant/2026-11-24-v66-lab-tom-review.md` | **File exists but every section reads PENDING as of this ruling.** It neither confirms nor refutes the cap numbers. See §5, condition V-0. |
| Webull read-only daily bars, 38 names + SPY (scratchpad `bt/data/`, split-adjusted; un-adjusted for sizing via lab `SPLITS`) | Used for all new measurements below |
| Mo Peter (VaR) / Mario (stress) | Not available in this session. I computed an **interim** historical 1-day VaR from the simulated equity curves (§8), labelled as such; formal runs commissioned in §5. |

**My own measurement tooling (scratchpad, not shipped):** an instrumented copy of `lab.py` that additionally records each trade's initial stop and whether the exit was a gap through the stop (`px < stop`), plus a hook that lets `position_plan` see the engine. No signal rule, fill rule or cost assumption was changed. Scripts are in `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/cro/` (`lab_cro.py`, `gaps.py`, `pertrade_gf.py`, `constructs.py`).

Window: tradeable 2022-11-30 → 2026-11-23, IS to 2024-12-31, OOS after (as in the CEO report). Account US$1,282.05 (HK$10,000 / 7.8). All "derived" numbers below are my arithmetic on these sources.

## 2. What the CEO's backtest shows about the cap

**What the 10% cap actually does.** Under `position_plan()`, shares = min(⌊US$12.82 / per-share risk⌋, ⌊US$128.21 / price⌋). The 1% risk rule alone already caps notional at 1% ÷ stop% (derived: 20% at a 5% stop, 12.5% at 8%, 8.3% at 12%). So the 10% cap does two different jobs, and only one of them is the job I wrote it for in July:

1. **Multi-share, tight-stop positions** (the July C-1 case: $200 stock, 2% stop → 3 shares = 46.8%). Here the cap prevents a "1% risk" position from becoming a large gap exposure. **This job is valid, and the data below confirms it (§3).**
2. **Single-share positions in US$128–256 names with stops under ~10%.** Here one share already exceeds US$128.21, so the cap blocks the trade outright. The 1% rule would have allowed 1 share at 10–20% notional. **This is the job that starves Engine 2.** `caps.csv` records 611 zero-share rejections at 10% vs 381 at 15% (ALL period).

**Reproduced cap table (2 slots, `as_traded`, ALL / IS / OOS):**

| Cap | CAGR % | Max DD % | Net EV/trade % | Trades |
|---|---|---|---|---|
| 10% (V6.4.2) | 0.96 / 0.94 / 0.51 | −3.89 / −3.89 / −2.82 | 0.40 / 0.62 / −0.03 | 88 |
| 15% | 4.28 / 3.40 / 5.27 | −4.66 / −4.66 / −3.08 | 1.67 / 1.40 / 1.90 | 89 |
| 20% | 4.24 / 3.06 / 5.45 | −5.65 / −5.65 / −3.51 | 1.38 / 0.89 / 1.78 | 96 |
| none | 3.55 / 2.25 / 4.75 | −6.46 / −6.46 / −3.53 | 1.29 / 0.84 / 1.61 | 96 |

Source: `strategy/v6.6/results/caps.csv`, re-run by me with identical output.

**Path robustness (new).** Because 2 slots make the result depend on which signals arrive first, I re-ran from 12 monthly start offsets (2022-11-30 → 2023-11-01, each running to 2026-11-23). **10% was the worst setting at every one of the 12 starts:** mean CAGR 1.57% (range 0.96–2.17) vs 15% 5.04% (4.28–5.82) and 20% 5.07% (4.24–6.10). Mean max DD was −2.96% (10%), −3.05% (15%), −4.33% (20%). These runs share most of their data, so they show **path robustness, not statistical independence**. **These figures use the lab as committed. §4.1 shows that one plausible change to how slots are reserved roughly doubles the 10% result and reorders the alternatives. Read this table as an upper bound on the cap's cost.**

**Price-band check, corrected for splits (new).** The CEO's band table uses split-adjusted prices, which he flags. Re-cut on **actual** entry prices (lab `raw_factor`), E2 gross EV per trade at next-open fills:

| E2 entry price (actual) | IS | OOS |
|---|---|---|
| ≤ US$128.21 | +0.25% (61) | +0.08% (29) |
| US$128–250 | +2.07% (59) | +3.10% (33) |
| > US$250 | +1.90% (93) | +0.55% (75) |

The correction makes the IS contrast **stronger** (the CEO's +1.49% IS for ≤$128 included pre-split NVDA and AVGO at their adjusted prices). Bootstrap of the ($128–250) minus (≤$128) difference, E2 per-trade SD 8.9pp: IS +1.82pp, 90% CI [−0.65, +4.35], P(≤0) = 0.12. OOS +3.02pp, [−1.14, +7.27], P(≤0) = 0.12. Pooled +2.24pp, [+0.04, +4.45]. This is an iid bootstrap on time-clustered trades, so the true CIs are wider. **The direction is the same in both halves, but neither half is significant on its own.** I do not rely on the band effect for this ruling (see §5).

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

I sized all 1,087 `per_trade` signals (next-open fills, every signal taken) at each cap, using actual share prices and **gap-through-stop fills for both engines**. The lab's `PER_TRADE` config inherits `e1_gap_fill=False`, so I switched it on; see §7. Loss is gross P&L as a % of the US$1,282 account.

| Sizing rule | Trades sizable | Mean / max notional | Worst trade, % of account | Trades losing > 1.25% / > 1.5% / > 2% | Gap exits |
|---|---|---|---|---|---|
| 10% flat | 339 | 7.9% / 10.0% | **−1.17%** | 0 / 0 / 0 | 38 |
| **B′: 10% + 1-share ≤ 15%, E2 only** (§4) | 380 | n/a / 15.0% | **−1.17%** | 0 / 0 / 0 | n/a |
| B: 10% + 1-share ≤ 15%, both engines | 468 | n/a / 15.0% | −1.26% | 1 / 0 / 0 | n/a |
| 15% flat | 468 | 11.0% / 15.0% | **−2.19%** | 5 / 2 / 1 | 44 |
| 20% flat | 526 | 13.2% / 20.0% | **−2.19%** | 5 / 3 / 1 | 46 |
| no cap | 577 | 18.3% / **364.7%** | **−6.57%** | 6 / 4 / 2 | 50 |

**Where the tail comes from.** Every trade that lost more than 1.25% of the account at 15% or 20% was an **Engine 1, multi-share, tight-stop** position held through a gap:

- NKE E1, entered 2024-06-17 with a 2.19% stop, 2 shares = 13.5% notional, held into the −18.1% gap on 2024-06-28: **−2.19%** of the account (−1.09% at a 10% cap).
- NKE E1 2025-03-25: −1.67%.
- PFE E1 2023-12-04, 8 shares: −1.41%.

**Engine 2 gap exits never cost more than about 1.02% of the account at any cap.** Its trailing stop has usually ratcheted above entry by the time a gap arrives.

**"No cap" is vetoed outright.** A 364.7% notional is leverage, a breach of `leverage: none`, and it is exactly the July C-1 failure.

### 3.3 Stress arithmetic beyond the sample

The sample is survivor-selected (F-01: a 2026 universe) and contains no 2022-style bear market (CEO report, NOT OBTAINED items 6–7). So I also bound the tail arithmetically. Loss ≈ notional × gap measured from entry. The 40% row is an **assumption**, a gap larger than anything in the sample, chosen because survivorship hides the names that did worse.

| Scenario | 10% flat | B′ (E2 1-share ≤ 15%) | 15% flat | 20% flat |
|---|---|---|---|---|
| Single name, worst observed gap −27.4% | 2.7% | 4.1% (1 share) / 2.7% (multi) | 4.1% | 5.5% |
| Both slots, worst observed pair −24.1% | 4.8% | 7.2% max | 7.2% | 9.6% |
| Single name, −40% (assumption) | 4.0% | 6.0% / 4.0% | 6.0% | 8.0% |
| Both slots, −40% each (assumption) | 8.0% | 12.0% max | 12.0% | **16.0%** |
| Owner's monthly breaker −10%: tripped in one night by the observed pair? | No | No | No | No (9.6%, near it) |
| Interim 1-day VaR95 / VaR99 on invested days (original sim) | 0.31 / 0.65% | 0.36 / 0.68% (B) | 0.41 / 0.73% | 0.51 / 0.92% |
| Worst simulated day / worst month (original sim, approx.) | −0.96 / −1.42% | −1.12 / −1.52% (B) | −1.20 / −1.54% | −1.61 / −1.94% |

At 20%, the worst **observed** correlated pair costs 9.6% of the account in one night, effectively the whole monthly breaker. At 15% (either form), that pair costs 7.2%, which leaves headroom. 15% is also the firm's own `max_single_position_drifted: 0.15` in `config/risk-limits.yaml`, the most the firm tolerates in one name at market. I anchor on that.

### 3.4 What the backtest cannot show

- Earnings dates are not in any backtest (CEO, NOT OBTAINED 3). The gaps above **are** in the price data, so earnings gaps are counted. The entry guardrail ("no entry within 5 days of earnings") is missing, so the backtest **over**-states entry-side earnings exposure.
- That guardrail does **not** cover holding periods. E1 holds up to 10 days and E2 up to 60 (`rules_v642`), and the NKE −2.19% case was entered 8 trading days before earnings. A live position will cross earnings whatever the entry guardrail says.
- Fat-tail events absent from a 4-year survivor sample: halts, fraud and crash gaps.

These are reasons to keep a ceiling. They are not reasons for that ceiling to be 10% for a single share.

## 4. Ruling on the construct

### 4.1 A simulator mechanic changes the ranking

In `lab.py`, a signal reserves one of the 2 slots at the close (`pending.append`), and is only sized at the next open. If it then gets 0 shares (unaffordable under the cap), the slot was **wasted for that day**, and an affordable candidate ranked below it was rejected as `no_slot`. A human reading a scanner that already prints `買唔起` would skip to the next name. Under a tight cap this mechanic penalises the 10% setting the most: 611 zero-share rejects at 10% vs 381 at 15% (`caps.csv`).

I therefore ran every construct twice:

- **"original":** the lab as committed.
- **"prescreen":** unaffordable signals are skipped at scan time and do not take a slot.

Neither is certified. Tom reports he has found two defects that "move (c) and (d)", meaning the as-traded result and the cap table, and has not yet published them (§1). This may or may not be one of them.

| Construct (2 slots, `as_traded`) | Original: CAGR ALL / IS / OOS · DD | Prescreen: CAGR ALL / IS / OOS · DD | Prescreen 12-start mean CAGR · mean DD |
|---|---|---|---|
| A. 10% flat (V6.4.2) | 0.96 / 0.94 / 0.51 · −3.89 | 2.04 / 1.49 / 2.62 · −4.49 | 2.77 · −5.86 |
| D. 15% flat | 4.28 / 3.40 / 5.27 · −4.66 | 3.15 / **0.51** / 4.88 · −6.02 | 4.46 · −5.26 |
| F. 20% flat | 4.24 / 3.06 / 5.45 · −5.65 | 5.46 / **0.51** / 10.00 · −7.55 | 7.25 · −5.26 |
| B. 10% + 1 share ≤ 15%, both engines | 4.12 / 2.85 / 5.39 · −3.82 | 2.60 / **−0.13** / 4.59 · −6.10 | 3.92 · −4.96 |
| C. E2 15% / E1 10% | 4.35 / 3.09 / 5.66 · −4.33 | 3.52 / 1.83 / 5.39 · −4.66 | 4.57 · −3.46 |
| **B′. 10% + 1 share ≤ 15%, Engine 2 only** | **4.19 / 3.02 / 5.38 · −3.82** | **3.28 / 1.52 / 5.09 · −4.45** | **4.30 · −4.34** |

Sources: rows A, D, F (original) match `caps.csv`. Everything else is my runs (scratchpad `constructs*.csv`, `starts*.csv`).

**What is robust across both mechanics:**

1. Flat 10% has the **lowest full-period CAGR at every one of the 24 start-date runs** (12 per variant).
2. The **ranking among the alternatives is not robust.** 15% flat and B lose to 10% in-sample under prescreen. 20% goes from roughly equal to 15% to best. Choosing among the alternatives on CAGR would be fitting noise.
3. **The 10% cap does not reliably buy drawdown protection.** Under prescreen it has the deepest mean drawdown of all constructs (−5.86%).

### 4.2 Tail risk by construct (every-signal sample, §3.2 method)

| Construct | Worst trade, % of account | Exception tier: trades / mean gross / worst |
|---|---|---|
| A. 10% flat | −1.17 | n/a |
| **B′. E2-only 1-share ≤ 15%** | **−1.17** | 41 / +1.86% / −0.78% |
| B. 1-share ≤ 15%, both engines | −1.26 | 129 / +1.48% / −1.26% (TSLA E1) |
| D / F. 15% / 20% flat | −2.19 | n/a (NKE E1, 2 shares) |

### 4.3 Ruling

**Recommendation to the Owner: adopt B′. VETO flat 20% and no cap. Do not recommend flat 15% or B.**

> **Single-position limit (swing account): no position may exceed 10% of the account (US$128.21), with one exception. An Engine 2 entry may be exactly one share of up to 15% of the account (US$192.31), provided that one share's risk to the initial stop is no more than 1% of the account (US$12.82). Engine 1 stays at 10% with no exception.**

Why:

1. **It is risk-neutral on every measure I can compute.** On the every-signal sample its worst trade equals 10% flat (−1.17%). Max DD is equal or slightly better in both simulator variants (−3.82 vs −3.89; −4.45 vs −4.49). Its 12-start mean DD under prescreen is better (−4.34 vs −5.86). The worst-case single-name gap from entry is 15% × 27.4% = **4.1%** of the account (derived; worst observed gap). The worst same-night pair is ≤ 7.2%, inside the −10% monthly breaker.
2. **It removes exactly the defect that was measured, and nothing else.** That defect is the whole-share price barrier that blocks Engine 2 in US$128–192 names. Multi-share positions stay at 10% in both engines. E1 keeps the 10% wall entirely, because E1 is where the gap tail lives (NKE, PFE, TSLA in §3.2) and E1 has no robust per-trade edge (OOS −0.16% with gap fills, §7).
3. **It is the only construct that is not worse than 10% in either half under either mechanic** (IS: 3.02 vs 0.94 and 1.52 vs 1.49; OOS: 5.38 vs 0.51 and 5.09 vs 2.62). The prescreen IS result is a **tie**, not a win, and I record it as such.
4. **Flat 15% (D) and B are not recommended.** Under prescreen both lose to 10% in-sample, and both let E1 positions reach 15%, which doubles the worst-trade tail (D: −2.19%).
5. **C (E2 15% / E1 10%)** is acceptable on returns. I prefer B′ because C lets **multi-share** E2 positions reach 15% at tight 3×ATR stops in low-ATR names, exactly the names that gapped 6–9 ATRs (§3.1). I would not veto C, but I record it as the riskier option.
6. **20% flat is vetoed.** The worst observed correlated pair would cost 9.6% in one night against a −10% monthly breaker, and it exceeds the firm's 15% drifted ceiling. Its prescreen IS (0.51) is worse than 10%.
7. **No cap is vetoed.** Notional reaches 364.7%, which is leverage, and the worst trade was −6.57%.
8. **A per-name gap-risk cap** (notional ≤ Y ÷ that name's stressed gap) is theoretically better but needs a look-ahead-free gap estimate and its own validation. It is recorded as a hypothesis for a larger account.

**Honest disclosure.** B′ was shaped after seeing this data: the E2-only restriction came from the NKE/PFE finding. Its backtest numbers are therefore in-sample to this decision, and only the forward protocol in §5 can validate it. What protects the Owner is that the change does not depend on the return evidence being right. It is justified by not adding measurable risk while removing a mechanical defect that keeps the account from running the strategy it is supposed to be testing.

**Firm limits are not changed.** `config/risk-limits.yaml` governs the firm book and stays as written. The swing-account limit is the **Owner's personal limit** (July escalation item 2). This ruling is a proposal to him. `MAX_POSITION_PCT` in his V6.4.2 code, and `RiskLimits` in `strategy/v6.5/risk_config.py`, change only if he adopts it.

## 5. Is the evidence strong enough? Validation protocol

**Short answer:** the evidence is **not** strong enough to claim the system earns more at a higher cap. It **is** strong enough to make the narrow B′ change, because B′ does not depend on the return evidence. Its risk is measured on 1,087 signals plus arithmetic, and it is indistinguishable from the status quo. The status quo is shown to stop the account from running the strategy it is meant to test.

| Question | Evidence | Strength |
|---|---|---|
| Does a higher cap earn more? | ~88–136 portfolio trades per run; E2 per-trade SD 8.9pp; ranking flips with a single simulator mechanic (§4.1); Tom reports unpublished defects in the cap table | **Weak.** Do not quote 4%/yr as an expectation. |
| Is the 10% cap the worst setting? | 24 of 24 start-date runs across two mechanics | **Moderate**, on one survivor-selected 4-year window |
| Does the $128–250 band carry E2's edge? | Same direction in both halves; neither half significant (P ≈ 0.12) | **Weak to moderate.** Not relied on. |
| Does B′ add tail risk? | Worst trade −1.17% vs −1.17%; exception tier worst −0.78% over 41 signals; DD equal or better; worst-case gap arithmetic 4.1% single / 7.2% pair | **Adequate for a bounded change.** Survivorship and the absence of a bear market are covered by the arithmetic in §3.3, not by the sample. |
| Does flat 15% or 20% add tail risk? | Worst trade doubles to −2.19% (E1 multi-share); 20% pair stress 9.6% | **Yes.** Not approved. |

### Validation protocol (binding if the Owner adopts B′; pre-registered today, 2026-11-24)

**Before anything goes live (gates):**

- **V-0. Tom's corrections.** When Tom publishes his corrected cap tables, B′ stands only if, under his corrected simulator, **both** of these hold:
  - (a) B′'s worst trade and max DD are no worse than 10% flat by more than 0.5 percentage points of the account;
  - (b) B′'s CAGR is not below 10% flat in either IS or OOS.

  If either fails, **this recommendation lapses automatically to "keep 10% flat"**, and it is not re-argued on the same 2022–2026 data. If Tom's defects are in the signal rules rather than the simulator, everything is re-run first.
- **V-1. Costs (July CL-7, still open).** One real Webull contract note covering commission, platform fee, SEC/TAF and FX. If there is any fixed per-order charge, re-run `as_traded` at that fee. If net EV ≤ 0, the system does not trade at this size under any cap.
- **V-2. Code, structurally enforced.**
  - The construct is implemented in one function and read from one config. `assert` statements are added to the scanner's version stamp.
  - The CEO's README snippet `assert E.MAX_POSITION_PCT == 10.0` must be **replaced**, not deleted. Otherwise it fails on a correct install or gets commented out.
  - Unit tests:
    - $200 stock, 2% stop → BLOCK (July C-1 case).
    - E2 $150 stock, 7% stop → 1 share.
    - E1 $150 stock, 7% stop → BLOCK.
    - E2 $195 stock → BLOCK (above US$192.31).
    - E2 $185 stock, 7.5% stop (1-share risk $13.88 > $12.82) → BLOCK.
    - $60 stock, 5% stop → 2 shares, not 3.
- **V-3. Parity.** `parity_check.py` passes on the Owner's PC (CEO, NOT OBTAINED 2).

**Forward test: a risk test, not a return test.**

- **Shadow ledger.** Every scanner signal is logged with the size under **both** A (10% flat) and B′, whether or not it is traded. This costs nothing and builds the clean forward A/B sample that the backtest cannot provide.
- **Paper first.** If the account is still inside the July CL-8 paper phase, B′ runs in paper. Real capital follows only after V-0 to V-3.
- **Horizon.** Review at **30 closed Engine 2 trades or 6 months, whichever is later**. This is not "20 trades side by side": the CEO's own §6.5 puts the 20-trade E2 CI at about ±3.3pp, which cannot separate two caps. The review checks risk behaviour only. **No return comparison between caps is made before 100 forward trades.**
- **Pre-registered stop conditions.** Any one of these reverts the account to 10% flat immediately. The Owner reverts; the firm is informed; there is no re-argument inside the test.
  - **S1.** Any exception-tier position loses more than **2.0% of the account**. That is twice its planned risk, against a backtest worst of −0.78% for the tier.
  - **S2.** Any sizing breach: a multi-share position above 10%, an E1 position using the exception, or a share above US$192.31. This also resets the CL-8 counter.
  - **S3.** The −10% monthly breaker trips while an exception-tier position is open.
  - **S4.** V-1 shows net EV ≤ 0 at the real fee.
- **Earnings log.** For every exception-tier position, record whether an earnings date fell inside the hold, and the gap if so. Earnings dates are absent from every backtest (CEO, NOT OBTAINED 3).

**Commissioned (Dept 6), to report before real-capital adoption:**

- **Mo Peter:** 1-day 95% VaR on the maximum-exposure B′ book (one 15% E2 single share plus one 10% position, and two 15% E2 single shares) against the 3% ceiling. My interim simulated figure is 0.36% VaR95 on invested days (construct B, original sim), not a substitute.
- **Mario:**
  - a replay of 2024-08-05 (MSTR/COIN/NVDA gap cluster) at maximum B′ exposure;
  - a −40% single-name gap (assumption);
  - a −10% overnight index gap with both slots in the same sector.

**No further raise on this data.** Raising beyond 15%, or extending the exception to E1, may only be argued on data collected after 2026-11-24. The 2022–2026 window has now been looked at too often to adjudicate a risk limit.

## 6. Owning the July recommendation

**Verdict on myself: the mechanism was right and the calibration was wrong. I shipped the limit without the pricing that I myself said it needed.**

**What I got right, which the backtest confirms:**

- July C-1 said that gap loss is bounded by notional, not by stop distance, and that 1%-risk sizing turns tight stops into large notionals. §3 confirms both in this firm's own data:
  - The worst gaps in ATR terms are in low-volatility names (NKE 9.4×ATR).
  - Every trade that lost more than 1.25% of the account at a 15–20% cap was a multi-share, tight-stop position (NKE E1: 2.19% stop, −2.19% of the account at 15%, −1.09% at 10%).
  - With no cap, notional reaches 364.7%. The multi-share 10% wall I recommended still earns its place, and B′ keeps it.

**What I got wrong:**

1. **I imported a firm-book number into a 2-slot account without re-deriving it.** The 10% is `config/risk-limits.yaml`'s `max_single_position`, a limit built for a diversified book. I paired it with **5** concurrent positions (CL-3: 5 × 10% = 50% deployed). The Owner chose **2**. At 2 × 10% the account is at most 20% deployed and at least 80% in cash, far above anything my own 10% cash floor called for. When the slot count changed, the cap needed re-deriving and I did not ask for that. That miss is mine.
2. **I treated two different exposures as one.** My July §4.3(b) argument, that one share above US$128.21 breaches concentration, applied the multi-share logic to single-share positions. A single share's notional is already bounded by the 1% rule (1% ÷ stop%, ≤ 20% at a 5% stop). The single-share case needed its own, looser ceiling. I wrote one number for both.
3. **I specified the test and let the limit ship without it.** CL-5 required a portfolio-level backtest "under CL-3's caps". That is this backtest. It was blocked on market data in July and arrived four months later. I should have marked CL-3's 10% figure **provisional pending CL-5** rather than final. A limit that has not been priced should say so.

**What the backtest cannot show, and why the July cap was still defensible as an emergency control:**

- In July the account had just recorded a ≥2.3x leverage breach (BAC, 2026-07-18) and two overrides in six trading days, and every guardrail was a display. The backtest assumes perfect rule execution. The July cap was partly a **behavioural** containment, and the backtest cannot price that value.
- The Sep screenshots (CVX US$209 at about 16%; PFE 8 shares = US$229 at about 18%; CEO §6.6) suggest the cap was not even running in the scanner then. That tells against the control's effectiveness, not in favour of it.
- A 4-year, survivor-selected, bull-dominated window cannot show the tail the cap insures against. §3.3's arithmetic is my answer to that, and it is why B′ keeps a ceiling at all.

**Net cost of my error (derived, original sim, so an upper bound given §4.1):** roughly US$175–185 of foregone P&L (B′, B or 15% vs 10%) over four years on a US$1,282 account, with no measurable risk reduction from the single-share part of the cap. Under the prescreen mechanic the cost is smaller (about 1.2pt CAGR, ALL). In money it is small. The larger cost is that for four months the account was validating a system in which Engine 2 was starved and Engine 1 dominated: the reverse of the per-trade picture (CEO §4). A process-validation account testing the wrong process is model risk, and in Dept 6 terms that is the real loss.

**Lesson for 腦大裝草 (memory):** a limit copied from another book must be re-derived for the target's slot count and lot size, and must be marked provisional until a portfolio simulation prices it.

## 7. Other risk issues in the CEO's report

| # | Issue | CRO position |
|---|---|---|
| 7.1 | **`PER_TRADE` inherits `e1_gap_fill=False` from `AS_TESTED`** (`lab.py`, `PER_TRADE = replace(AS_TESTED, ...)`). E1 stop exits fill at the stop even when the open gapped through it. | With gap fills on, E1 `per_trade` net is **IS +0.23% / OOS −0.16%** (ALL +0.05%), vs the reported +0.39 / −0.03. E2 is unaffected (its gap fill is unconditional). This strengthens "E1 has no edge" and matters for risk: E1 is where the gap tail is. `as_traded` already has gap fills on. Fix: set `e1_gap_fill=True` in `PER_TRADE`. Referred to Tom. |
| 7.2 | **Slot reservation for unaffordable signals** (§4.1). | It moves the 10% result from 0.96% to 2.04% CAGR and reorders the alternatives. The CEO's "10% is the single largest drag" holds in direction; its **size is overstated** by the committed mechanic. The report should not quote 0.96% vs 4.28% without this caveat. Referred to Tom; it may or may not be one of his two defects. |
| 7.3 | **Price bands on split-adjusted prices.** | Re-cut on actual prices, the direction holds and IS strengthens (§2). The CEO's caveat was adequate. |
| 7.4 | **Costs unverified.** The M2 stress (US$1/side) gives −1.9% CAGR. | Agree this is decisive. I add one point: **the cap and costs interact.** A fixed per-order fee costs more in percentage terms on a smaller notional (derived: US$1/side is 1.56% round trip on US$128, 1.04% on US$192). The cap decision and the fee check must be read together. V-1 is a gate, not a footnote. |
| 7.5 | **Earnings guardrail absent from all backtests.** | Agree, with a correction. The entry guardrail (5 days) does not protect **holds**: E1 holds 10 days and E2 up to 60, and the NKE −2.19% loss was entered 8 trading days before earnings. Live positions will cross earnings regardless. The backtest's earnings gaps are in the price data, so the gap tail is measured, not missing. Earnings log required (§5). |
| 7.6 | **Version drift.** The Sep scans show CVX at about 16% and PFE 8 shares at about 18% of the account. | **Escalated.** If trades were placed from those scans after V6.4.2 was adopted, those are realised breaches of the Owner's own personal limit, and PFE (multi-share, about 18%) would breach B′ as well. Request: the Owner confirms whether any order was placed from the 6 Sep or 28 Sep scans. The version stamp is endorsed, with the assert updated per V-2. |
| 7.7 | **`RiskLimits` drift.** `strategy/v6.5/risk_config.py` still says `max_open_positions = 5`; the Owner runs 2. | My own file disagrees with the live system, the same "limits arriving by accident" failure I warned about in July. If B′ is adopted, `RiskLimits` and `plan_position()` must encode B′ **and** `max_open_positions = 2`. Until then, V6.4.2 constants are the operative limits. |
| 7.8 | **CEO README: "paper-trade both caps side by side, 20 trades."** | Inconsistent with the CEO's own §6.5. 20 trades cannot separate the caps. Replaced by the shadow ledger and risk-based stop conditions (§5). |
| 7.9 | **"Drawdown barely moves because the 1% rule binds."** | Partly agree. Max DD in a survivor-selected bull window is the wrong measure of gap risk; the per-trade tail (§3.2) and stress arithmetic (§3.3) are the right ones. On those, flat 15–20% **does** move the tail (−2.19% vs −1.17%), and B′ does not. |
| 7.10 | **The 2-slot correlated pair.** | Not discussed by the CEO. With 2 slots, both positions can sit in one cluster (2024-08-05: MSTR and COIN both gapped about 20–27%). B′ bounds that pair at 7.2% (derived) against the −10% breaker. No change proposed. Mario is to stress it. |
| 7.11 | **Idle-cash interest excluded from all CAGRs; universe chosen in 2026 (F-01).** | Agree with the CEO's disclosure. Neither obviously favours one cap over another, but survivorship biases the **gap tail downward**. Hence the 40% assumption row in §3.3. |

## 8. Limit-by-limit check

Measured against the swing account's operative limits (V6.4.2 constants, the Owner's manual, and my July personal-limit proposals). The firm's `config/risk-limits.yaml` is shown for reference only; it governs the firm book.

| Limit | Limit value | Current (A: 10% flat) | Post-change (B′) | Pass / Fail |
|---|---|---|---|---|
| Single position, multi-share | 10% | ≤ 10% | ≤ 10% (unchanged) | **PASS** |
| Single position, single share | 10% today → **15% proposed** (= firm `max_single_position_drifted` 0.15) | ≤ 10% | ≤ 15% (US$192.31), E2 only | **PASS** under the proposed limit; Owner decision |
| Max risk per trade | 1% (US$12.82) | ≤ 1% | ≤ 1%; the exception requires 1-share risk ≤ 1% | **PASS** |
| Concurrent positions | 2 (Owner's manual) | 2 | 2 | **PASS** |
| Gross exposure / cash floor | cash ≥ 10% | max 20% gross, cash ≥ 80% | max 30% gross (two E2 single shares), cash ≥ 70% | **PASS** |
| Leverage | none (cash account, CL-1) | none | none; max notional 15% | **PASS** |
| Sector / correlated cluster (firm ref.) | 35% / 40% | ≤ 20% | ≤ 30% if both slots share a cluster | **PASS** |
| Monthly circuit breaker | −10% | worst observed pair gap 4.8%; −40% pair (assumption) 8.0% | worst observed pair 7.2%; −40% pair (assumption) 12.0% | **PASS** on observed data; **FAILS only under a two-name 40% overnight gap**, beyond anything in the sample. Accepted, with Mario to stress it. |
| Drawdown budget | 20% (July proposal) | sim max DD −3.89% (orig.) / −4.49% (prescreen) | −3.82% / −4.45% | **PASS** |
| 1-day VaR95 (firm ref. 3%) | 3% | interim 0.31% | interim about 0.36% (B, a proxy for B′) | **PASS**, interim; Mo Peter to confirm |
| Stop discipline | stop required, never moved down | unchanged | unchanged | **PASS** |
| Max initial stop | E2 12% / E1 15% | unchanged | unchanged | **PASS** |
| Cost gate (July CL-7) | net EV > 0 at the real fee | **UNVERIFIED** | **UNVERIFIED** | **OPEN**: gate V-1 |

## 9. Risk score input to committee

Scale as in July: 0 = do not deploy, 100 = clear at full size; higher is safer. These are **risk** scores; upside is not scored.

| Option | Score | Basis |
|---|---|---|
| A. Keep 10% flat | 72 | Safe tail, but it distorts the system under test (model risk) and does not buy drawdown protection under prescreen |
| **B′. 10% + E2 single share ≤ 15%** | **74** (rises to about 80 once V-0, V-1 and Mo Peter/Mario are done) | Tail equal to A, removes the distortion, bounded stress arithmetic |
| C. E2 15% / E1 10% | 62 | Allows multi-share E2 at 15% in low-ATR, gap-prone names |
| B. 1-share ≤ 15%, both engines | 60 | E1 exception widens the tail; loses to A in-sample under prescreen |
| D. 15% flat | 52 | Worst trade doubles (−2.19%); loses to A in-sample under prescreen |
| F. 20% flat | **VETO** (30) | Observed pair stress 9.6% against the −10% breaker; above the firm's 15% drifted ceiling |
| G. No cap | **VETO** (10) | Notional up to 364.7% is leverage; worst trade −6.57% |

Committee input: **74 / 100 for B′, conditional.** Gates V-0 (Tom) and V-1 (costs) must clear before real capital, and the pre-registered stop conditions S1–S4 are binding on Zac and 死潘狗 for any tickets.

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
