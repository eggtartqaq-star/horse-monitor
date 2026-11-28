# V6.6 execution cost per side: spread and slippage estimate (CRO condition V1-b), 2026-11-28

**Messi, Execution Analyst (Dept 8).** Written for John (CRO). It answers condition V1-b (`reports/risk/2026-11-28-v1-ruling.md` §1) and the slippage input in prereg amendment 3 (`reports/quant/2026-11-28-v66-development-prereg.md:69`).

**Data used** (all primary, read-only, already on disk):
- Webull daily OHLCV, `strategy/v6.6/data/*.csv`, 2022-11-01 → 2026-11-23, 1,019 bars per name.
- Trade lists in `strategy/v6.6/results/hk_exec/`: `trades_lab.csv` gives the names and weights (17 names, 262 sides); `trades_hk2.csv` gives the exit mix (258 sides).
- The Owner's three fills (`reports/risk/2026-11-28-v1-fee-evidence.md` §2).

**Not done:** no broker call, no web fetch, no pip install, no edit under `strategy/v6.6/`, nothing committed.

## Answer

Every figure in this section is an **estimate**. It covers spread and slippage only. The regulatory fee, about 0.2 bp per side, comes on top (V-1 evidence §3.2).

| Order type, as V6.6 trades | Sides (HK-2 basis) | **Planning value**, bp per side (central estimate) | **Cautious upper bound**, bp per side |
|---|---|---|---|
| Limit buy at the open (at or below max limit; cancelled if not filled at the open) | 130 | **4** | **9** |
| Stop-market sell triggered at the open (gap through the stop) | 17 | **6** | **15** |
| Manual market sell at the next open | 63 | **4** | **11** |
| *(for information)* Stop-market sell triggered during the session | 48 | 6 | 13 |
| **Blended over the HK-2 mix: the single `--fee-bp` input** | 258 | **4.5** | **10.6** |

**Against the thresholds:**
- The **planning value, 4.5 bp, is below 10 bp and below 13 bp.** With the regulatory fee it is 4.7 bp.
- The **cautious bound, 10.6 bp, is above 10 bp and below 13 bp.** With the regulatory fee it is 10.8 bp.
- One order type is above 13 bp at its cautious bound: the stop at a gap open (15 bp). It is 17 of the 258 sides.
- **Daily bars cannot exclude 13 bp.** If every pessimistic choice is stacked (the uncorrected estimator and double the stop allowances), the blended cost reaches about 14 bp. The 2.8 bp margin between 10.2 and 13 is inside the measurement error.

**In dollars.** The average side is about US$101.
- Per side: planning about US$0.05; cautious about US$0.11.
- Over the 258 backtest sides (US$26,192 traded): planning US$11.78; cautious US$27.81. The current 10 bp assumption costs US$26.19.

**Recommendation for the V1-b re-run and the amendment-3 verdict runs** (one cost, no brackets):
- Use the **cautious 10.8 bp per side, including the regulatory fee.** This is my recommendation; the CRO decides.
- Why: the planning value rests on a daily-bar estimator. It passes a near-zero-spread control only once calibrated (§3).
- Running the gates at 4.7 bp would add about 0.11 pp of EV per trade, using Tom's sweep slope of about 0.02 pp per bp per side (`reports/quant/2026-11-28-v1-feecheck.md` §1). Nobody has measured that gain.

## 1. What the backtest already prices

The per-side cost here is **fill price minus the backtest's own fill price**. It is not decision price to fill.
- **Entry:** the backtest fills at the bar's Open when the Open is at or below the max limit and above the stop (`lab.py:337–362`, called with `row["Open"]` at `:405`).
- **Stops:** the backtest fills at min(Open, stop) (`lab.py:318`, `:327`).
- **Manual sells (HK-2):** they fill at the next bar's Open.
- **What this means:** the overnight gap, the open-versus-day effects in §4, and missed fills (`--tif open`) are already in the backtest's P&L. They are **not** added again here.

## 2. Liquidity and market impact

There is no liquidity profile from Tim Cook on file for these names, so I computed one from the bars (last 12 months).

- **Order size:** 1 to 15 shares, median 1; about US$100 per side.
- **Average daily dollar volume:** US$0.79 bn (SBUX) to US$26.7 bn (MU).
- **Order as a share of daily volume:** at most 1.6 × 10⁻⁷.
- **Square-root impact,** σ·√(Q/ADV) with a coefficient of 1 (**assumed**): at most 0.12 bp (SHOP); most names are below 0.08 bp.
- **Result: impact is nil at this size.** The cost is the spread at the moment of execution, plus timing.
- **Floor:** half of a US$0.01 tick at the prices actually traded is **1.0 bp per side**, trade-weighted. The tick size is the standard US quoting increment and is assumed, not re-checked here; if a half-cent tick now applies to some names, the floor is lower. The bars are adjusted (Tom, feecheck §3), so the prices really traded were higher, and this floor is slightly overstated.

## 3. Effective spread from daily bars

### 3.1 Formulas

All estimators give the **full** proportional spread S. The cost per side is S/2.

- **Corwin–Schultz (2012), high–low:**
  - β = [ln(H_t/L_t)]² + [ln(H_t+1/L_t+1)]²
  - γ = [ln(max(H_t, H_t+1) / min(L_t, L_t+1))]²
  - α = (√(2β) − √β)/(3 − 2√2) − √(γ/(3 − 2√2))
  - S = 2(e^α − 1)/(1 + e^α)
  - Overnight adjustment, as in the paper: shift day t+1's high and low by the part of the gap that lies outside its range.
  - Three versions are reported:
    - **CS0:** two-day estimates below zero set to 0 (the paper's default).
    - **CS raw:** the mean, negatives kept.
    - **CS full-gap** (my variant): day t+1's high and low divided by O_t+1/C_t on every day.
- **Abdi–Ranaldo (2017), close–high–low:**
  - η_t = (ln H_t + ln L_t)/2
  - S² = 4·E[(ln C_t − η_t)(ln C_t − η_t+1)]
  - Reported as the signed square root of the mean.
- **EDGE (Ardia, Guidotti and Kroencke, 2024):** combines open- and close-based moments of the same kind, weighted by GMM.
  - I **re-implemented it from memory** of the authors' reference code and did not check it against that code.
  - In simulation it recovers spreads of 50 and 100 bp (52.8 and 101.1), so the code is at least self-consistent.

### 3.2 Known biases, and how they show here

**CS:**
- Setting negative two-day values to 0 biases the estimate upward when spreads are small relative to volatility. In simulation it gives 59–70 bp at a true spread of 0.
- Overnight moves that the partial adjustment does not remove bias the raw mean downward: about −7 to −10 bp at a zero spread, for these names' volatility.
- Discrete trading shrinks the observed ranges, which also biases it downward.
- At small spreads its sensitivity is well below 1: in simulation, 0.2 to 0.8 bp of estimate per bp of true spread. Inverting it therefore amplifies any error in the bias.
- It assumes the high is a trade at the ask, the low a trade at the bid, and constant variance over the two days.

**Abdi–Ranaldo and EDGE:**
- They assume the close or open is a trade at the bid or the ask, and that the efficient price is a martingale.
- Any short-horizon predictability enters the moment one for one: for example, a late-day move that reverses the next day, or an opening gap that fades.
- US opens and closes are largely auction prints, so the bid–ask bounce these estimators rely on is weak.
- Noise in simulation is about ±35–40 bp (1 sd) per name over 4 years.

**Control test.** SPY and QQQ are **assumed** to trade at about one tick, which is 0.14–0.15 bp full at their prices. There is no quote data on disk to confirm this. An estimator that reports tens of bp for them is measuring something other than the spread.

| Estimator (full S, bp) | Traded names, trade-weighted | SPY | QQQ | Verdict |
|---|---|---|---|---|
| CS0 (paper default) | 65.1 | 25.1 | 33.0 | **Fails**: truncation bias |
| Abdi–Ranaldo (pooled moment) | 39.7 (90% CI −22.9 to 50.3) | 43.3 | 52.5 | **Fails**: return dynamics, not spread |
| EDGE | 29.1 | 37.5 | 49.4 | **Fails**: same cause |
| CS raw | −0.65 (90% CI −2.8 to 1.7) | 0.0 | −2.3 | Not refuted; biased, so it needs calibration |
| CS full-gap | 16.7 (90% CI 14.4 to 19.0) | 5.7 | 6.2 | Not refuted; biased, so it needs calibration |

Equal-weighted over all 38 names: CS0 66.7, CS raw −1.2, Abdi–Ranaldo 23.3, EDGE 34.2.

### 3.3 Calibration by simulation at known spreads

**Model:**
- the efficient price is a Brownian motion;
- a daily stochastic-volatility multiplier (lognormal, sd 0.4);
- U-shaped intraday variance (7 times higher at the open and close than at midday);
- Student-t(4) overnight gaps;
- 1,019 days;
- each trade is at the efficient price ± S/2, with a random sign.

**Method:**
- Each name is simulated with its own open-to-close and overnight volatility.
- Spreads simulated: 0, 5, 10, 20 and 40 bp.
- The trade-weighted curve is inverted at the observed pooled value.
- The 90% CI comes from a 20-day moving-block bootstrap.

| Estimator | Simulated trades per day | Traded names: implied full S, bp (90% CI) | SPY implied | QQQ implied |
|---|---|---|---|---|
| **CS full-gap** | **5,000** | **7.8 (4.5 to 11.0)** | **−0.6** | **−0.1** |
| CS full-gap | 2,000 | 11.7 (8.4 to 14.5) | 2.0 | −12.3 |
| CS raw | 5,000 | 19.0 (14.4 to 22.8) | 6.2 | 4.5 |
| CS raw | 2,000 | 19.9 (16.6 to 23.9) | 9.0 | 7.3 |

- **Central half-spread: 3.9 bp, rounded to 4.** It comes from the first row, the only setup in which both controls come back at about 0.
- **Cautious half-spread: 8.7 bp, rounded to 9.** Rule: the largest value, across the four rows, of (90% upper bound minus that row's positive control residual) ÷ 2. The CS raw row at 5,000 trades gives (22.8 − 5.35) ÷ 2.
- CS raw is ill-conditioned below 10 bp, so it feeds only the cautious bound.

### 3.4 Per name

The per-name implied values are **noisy**, from −20 to +10 bp. Only the pooled value is used.

| Name | Sides | Median traded price, US$ | Half-tick, bp | CS0 | CS raw | Abdi–Ranaldo | EDGE | CS full-gap | Implied half-spread, bp (5,000-trade calibration) | ADV, US$ bn |
|---|---|---|---|---|---|---|---|---|---|---|
| PFE | 31 | 26.4 | 1.89 | 50.2 | 5.3 | 23.8 | −11.6 | 12.3 | 3.1 | 1.03 |
| SBUX | 26 | 93.2 | 0.57 | 52.9 | 5.4 | 57.9 | 37.0 | 10.5 | 1.6 | 0.79 |
| UBER | 24 | 70.2 | 0.85 | 77.9 | 7.8 | −40.2 | 68.4 | 16.7 | 1.7 | 1.41 |
| NKE | 24 | 67.2 | 0.70 | 56.3 | −0.3 | 56.4 | 50.0 | 18.5 | 5.7 | 1.09 |
| WMT | 24 | 101.5 | 0.55 | 42.9 | 2.1 | −21.1 | 17.3 | 11.6 | 3.6 | 2.87 |
| BAC | 23 | 44.0 | 1.26 | 49.1 | 1.5 | −30.4 | −10.3 | 13.7 | 4.3 | 2.01 |
| MU | 18 | 87.6 | 0.62 | 91.2 | −15.8 | 60.2 | 34.5 | 30.8 | 10.2 | 26.68 |
| INTC | 18 | 30.7 | 1.74 | 88.6 | −11.2 | 84.0 | −46.4 | 24.4 | 6.6 | 9.26 |
| NFLX | 16 | 88.1 | 0.59 | 62.6 | 2.3 | 43.8 | 60.7 | 5.9 | −20.0 | 3.53 |
| PLTR | 12 | 22.2 | 2.76 | 104.4 | −18.7 | −66.0 | 85.0 | 26.6 | 4.8 | 6.10 |
| XOM | 12 | 103.0 | 0.47 | 48.6 | −1.0 | 13.8 | 10.9 | 17.6 | 6.6 | 2.55 |
| SHOP | 10 | 76.2 | 0.69 | 97.2 | −3.8 | 4.5 | 39.3 | 21.0 | 4.2 | 1.28 |
| QCOM | 8 | 109.5 | 0.45 | 74.2 | 6.1 | 86.2 | 83.3 | 20.9 | 6.2 | 2.51 |
| AMD | 6 | 104.3 | 0.48 | 90.4 | −12.8 | 86.8 | 80.7 | 23.3 | 4.9 | 12.08 |
| AMZN | 6 | 101.5 | 0.47 | 59.1 | 1.4 | 59.4 | 63.0 | 17.6 | 5.8 | 11.02 |
| JPM | 2 | 122.4 | 0.41 | 45.0 | 4.0 | 29.8 | 28.9 | 11.2 | 3.0 | 2.85 |
| GOOGL | 2 | 118.9 | 0.42 | 52.4 | −3.2 | 22.8 | 52.9 | 8.4 | −1.5 | 10.62 |
| **Trade-weighted** | 262 | | **1.00** | 65.1 | −0.65 | 22.2 | 29.1 | 16.7 | **3.9 (pooled)** | |
| SPY (control) | — | 722 (last) | 0.07 | 25.1 | 0.0 | 43.3 | 37.5 | 5.7 | −0.3 | 44.08 |
| QQQ (control) | — | 651 (last) | 0.08 | 33.0 | −2.3 | 52.5 | 49.4 | 6.2 | −0.1 | 32.01 |

Units: CS0, CS raw, Abdi–Ranaldo, EDGE and CS full-gap are full S in bp. The other 21 names are in the scratch file `per_name.csv` (see the end of this report).

## 4. Open-auction effects

**Benchmarks:**
- **Previous close:** for an entry, this is the decision price.
- **Day's VWAP proxy:** the typical price (H+L+C)/3. Daily VWAP is not on disk. The typical price ignores the U-shaped volume profile, so on any single day it can be tens of bp off. Averaged over 17 to 130 trades it is used only as a check of sign.
- (O+H+L+C)/4 gives the same signs.

| Side (HK-2 basis) | n | ln(Open / previous close): mean bp (se) | ln(Open / typical price): mean bp (se) | Reading |
|---|---|---|---|---|
| Limit buy at the open | 130 | −22.8 (6.1) | −13.0 (11.5) | Bought below the signal close, and not above the day's average. No cost from trading at the open. |
| Manual sell at the next open | 63 | −24.2 (20.8) | −8.0 (16.6) | Sold 8 bp below the day's average; not significant. |
| Stop at a gap open | 17 | −675 (136) | −30.1 (28.6) | After a gap down, the day's average was 30 bp above the open; not significant. No sign of a continued slide. |
| Stop during the session | 48 | −60.6 (13.5) | +107.9 (15.5) | These days fell during the session. Stop minus the day's low: median 51 bp, mean 92 bp. That is a worst-case bound per fill, not an estimate. |
| All name-days, traded names | about 17,000 | mean absolute gap 88 | mean −1.1; mean absolute value 96 | The open is not biased against the day's average, but it is noisy. |

**Conclusion:**
- Over 2022–26, trading at the open did not cost the system anything systematic against a VWAP-style benchmark.
- These effects are already in the backtest (§1).
- The cost that daily bars cannot see is the spread in the first minute. The planning value treats it as included in the range-based estimate, because daily extremes cluster at the open. That is a **stylised fact, not tested here.** The cautious value, at 2.2 times the planning value, is the allowance for it.

## 5. Cost build per order type

Values are bp per side. 1 tick = US$0.01 = 2.0 bp at the trade-weighted traded price.

| Component | Planning | Cautious | Measured or assumed |
|---|---|---|---|
| Half effective spread (all day, trade-weighted) | 4 | 9 | **Measured** (§3.3, calibrated) |
| Opening premium on top of that | 0 | inside the 9 | **Assumed** (§4) |
| Market impact | 0.0 | 0.1 | Square-root law, coefficient **assumed** |
| Manual sell: market order placed minutes after the open | +0 | +1 tick (2) | **Assumed.** No adverse drift was seen (§4). |
| Stop at the open: trigger, then execution | +1 tick (2) | +3 ticks (6) | **Assumed.** The CoreWeave fill was 21 bp better (§6). |
| Stop during the session: trigger-through | +1 tick (2) | +2 ticks (4) | **Assumed.** Hard bound: median 51 bp (§4). |

- **Results:**
  - Entry: 4 (planning), 9 (cautious).
  - Manual sell: 4 and 11.
  - Stop at the open: 6 and 15.
  - Stop during the session: 6 and 13.
  - Blended: **4.5 and 10.6.**
- **Floor case:** if the spread is one tick and the same allowances apply, the blended cost is 1.5 bp.

## 6. Estimate vs realized: the Owner's three fills

These are anecdotes. Three fills are not a sample.

| Fill | Backtest price rule | Actual | Realized against the rule | Comparable to V6.6? |
|---|---|---|---|---|
| CoreWeave, 2026-10-01: stop-market sell, 15 shares, trigger US$87.00 | At or below US$87.00 (min(Open, stop)) | US$87.185, 09:31:08 EDT | **At least 21.3 bp better** (at least US$2.775 on US$1,307.78) | Yes (stop at the open). Planning estimate: a 6 bp cost. A favourable miss. |
| AVGO, 2026-10-02: limit buy at US$353.17, DAY, 4 shares | Limit US$353.17. That day's bar Open was US$349.855. | US$353.155, 10:01:25 EDT | 0.4 bp better than the limit (US$0.06); 4.2 bp below the day's typical price | No. It was entered after the open. |
| AVGO, 2026-11-05: limit buy at US$301.97, overnight session, 2 shares | Limit | US$301.97, 23:50 EST | 0 bp against the limit | No. V6.6 does not trade the overnight session. |

**Limits of the CoreWeave check:**
- CoreWeave is not a V6.6 name, and there is no bar for it on disk. So whether the stop fired on a gap cannot be checked.
- One fill that is 21 bp better sits well inside the per-trade noise at the open, where the mean absolute gap between the Open and the day's typical price is about 96 bp.

**No model change** is warranted on three fills.

## 7. Tactics

Input for 死潘狗's tickets and for the CRO; nothing here changes a rule.

1. **Entries.** Keep C-8: a limit order at the max limit, entered before the open.
   - A limit order cannot fill above its limit, so the entry cost has a hard cap.
   - If Webull HK routes the order into the opening auction, the fill is the official open, and the cost against the backtest is about 0.
   - The routing is unknown. The first real fills will show it: a 09:30:00 time stamp and a price equal to the open would confirm it.
2. **Manual sells.** F-8 says "sell at market".
   - A marketable limit order (limit a few ticks below the bid) would cap the loss on a bad print, at a small risk of not filling.
   - This would change the CRO's wording, so it is a **question for the CRO**, not a change.
3. **Stops.** Keep stop-market.
   - A stop-limit caps the price, but it can fail to fill on exactly the gap days the stop exists for.
   - Protection is worth more than the bp.
4. **Time of day.** The open is the widest-spread moment of the day, but the system is designed around it. No change is proposed.
5. **Flags for Morris: structurally dearer trades.**
   - Low-priced names: PLTR at a US$22 traded median (half-tick 2.8 bp), PFE (1.9), INTC (1.7), BAC (1.3).
   - Stops on earnings-gap days.
   - None of these changes the blended number. No traded name is illiquid; the lowest daily volume is US$0.79 bn.

## 8. Cost model updates

**The file is missing.** `quant/cost-model.md`, which my mandate says I keep, does not exist. I have not created it; that was outside this task.

**Proposed entries, for the CEO to approve:**
- **Commission and platform fee:** US$0 (V-1 evidence §1–2).
- **Regulatory fee:** about 0.2 bp per side, averaged (charged on sells), pending V1-a.
- **Spread and slippage per side,** for entry / stop at the open / manual sell / stop during the session:
  - planning: 4 / 6 / 4 / 6;
  - cautious: 9 / 15 / 11 / 13;
  - blended: 4.5 planning, 10.6 cautious.
- **Gate input:** the cautious 10.8 bp including the regulatory fee (recommendation).
- **Impact:** nil at US$130 or less per order.
- **When to review:**
  - after 20 to 30 real fills logged against bar prices;
  - when an opening-quote log exists;
  - if order sizes rise more than 100-fold, or names with daily volume under US$100 m join the universe.

**How to replace this estimate with a measurement:**
1. **Real fills.** For every real fill the Owner reports the time, the price and the order type, and I log fill price against the bar's Open or the stop. Paper fills do not count, because Webull's paper engine is a simulation.
2. **Opening quotes.** Either of these would give a direct measurement:
   - Screenshots of the bid and ask at 09:30–09:32 ET for the day's names, on a few days. Webull HK shows US Level 2 quotes free (V-1 evidence §1).
   - A read-only quote logger. Standing rule 1 permits it, if it carries the self-audit used in `scripts/futu_export.py`.
   - **Only the Owner can supply the screenshots or approve the network access.**

## 9. Limits

- **The opening spread is not measured.** Daily bars cannot see it. The estimate is a calibrated, range-based, all-day measure, and the opening premium is an assumption.
- **What the bars contain is unknown.** Nothing on disk documents whether Webull's daily Open is the official auction price or the first consolidated trade, or whether the high and low include extended-hours prints.
  - AVGO on 2026-10-02 shows an Open of US$349.855, and its high and low have sub-penny digits. That suggests the consolidated tape, including off-exchange prints.
- **The calibration rests on a model.** The SPY and QQQ controls are the check on it. Their true spreads are **assumed** to be about one tick.
- **EDGE was re-implemented from memory.** It is reported but not used.
- **The trades come from the 2026 hindsight universe.** The 2022 list (K-6) may trade names at other price levels, which means other tick costs. Re-weight the estimate on that list's trades before the verdict run.
- **The past is not the future.** The AI cannot predict markets. This describes four years of past bars, not future fills.

**Scripts and outputs (scratch):** `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/slip/`, which contains:
- scripts: `est.py`, `sim.py`, `calib.py`, `trades.py`;
- outputs: `per_name.csv`, `sides_hk2.csv`, `sides_lab.csv`, `calib_out.txt`, `calib_out_5000_full.txt`.

*Research and decision support, not financial advice. Every cost here is an estimate from daily bars; it cannot predict live fills. No agent of this firm places orders.*
