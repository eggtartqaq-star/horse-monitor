# V6.5 Measurement-Layer Review

**Scope:** `strategy/v6.5/` — `rules.py`, `risk_config.py`, `portfolio_sim.py`, `selftest.py`, `README.md`.
**Baseline:** `reports/quant/2026-07-30-v64-backtest-audit.md` (the U-1 specification) and `strategy/v6.4/`.
**Method:** full read of all four modules, plus execution of `selftest.py` and two purpose-written probes against a scratchpad copy. Nothing under `strategy/` was modified.

---

## Verdict

**Substantially better, but not yet sound. Do not treat a positive number from this simulator as evidence of an edge.**

V6.5 does what it says it does: it is a measurement upgrade, not a strategy change, and it closes most of the *accounting* defects the V6.4 audit found. The cash ledger, the cost model, the integer-share sizing, the next-open fill, the rejection ledger and the drawdown block are all real and all correctly implemented. I checked the accounting identities directly and they hold.

But "sound measurement" means the number you get out is an unbiased estimate of the thing you care about, and there are still five defects that break that chain. Two of them are new to V6.5 — introduced by the very fixes that make it better than V6.4 — and one of them means the file that is supposed to prove there is no look-ahead **cannot fail**, which I demonstrated experimentally.

Ranked by how much they distort the answer:

| # | Defect | Direction | Status |
|---|---|---|---|
| B-1 | Split-adjusted prices drive absolute-price position limits → multi-year look-ahead in sizing | **Inflates** (materially) | New in V6.5 |
| B-2 | The look-ahead self-test is vacuous — it passes on deliberately contaminated data | Unknown / unverified | New in V6.5 |
| B-3 | The broker comparison table does not hold the trade set constant | Overstates cost drag | New in V6.5 |
| B-4 | No benchmark, no confidence interval, no walk-forward | Cannot distinguish edge from beta or noise | Carried over |
| B-5 | Drawdown budget is enforced *inside* the measurement | Bounds the headline risk stat by construction | New in V6.5 |

---

## 1. What V6.5 genuinely fixed — credit where it is due

I verified each of these in the code rather than taking the README's word for it.

- **Cost model is real and the accounting is consistent.** `portfolio_sim.py:217-235` charges `one_side()` on entry (line 303) and `one_side()` on exit (line 221) against cash, while the trade record carries `round_trip()` (line 220). Cash flow and trade-level P&L agree — no double-counting, no leakage. `selftest.py` line 112 asserts the identity and it passes.
- **Look-ahead in the signal path is genuinely removed** (structurally — see B-2 for why it isn't *proven*). Regime is `.shift(1)` on the SPY bull flag (`portfolio_sim.py:117`), the signal reads bar `i` (`signal_at`, line 126), the fill is bar `i+1`'s open (line 286). Regime information is actually two days stale, which is conservative. Every indicator in `rules.py:33-109` is causal (`rolling`, `ewm`, `diff`, `shift(1)`) — I read them all.
- **Gap-through-stop is modelled**, and on the correct side: `min(pos["stop"], row["Open"])` at line 204 closes V6.4's H-2, and a gap that opens below the intended stop rejects the entry outright (lines 287-290).
- **Stop is checked before the trailing stop is raised** (lines 202 vs 211-215). This ordering is the single easiest thing to get wrong in a trailing-stop backtest and it is right here.
- **`OPEN_AT_END` positions are marked to market, not discarded** (lines 317-330) — closes M-1.
- **Cooldown is actually executed** (lines 265, 233-234) — closes H-6, though see S-2 on its units.
- **Engine 1's stop-width filter now exists in the backtest** (line 149), so the backtested population finally matches the live population — closes H-3/F-07.
- **The rejection ledger is the best idea in the release.** Treating "the trade the system refused to take" as data rather than as an exception is exactly right, and my synthetic run shows why: 497 of 515 rejections were `單一倉位集中度超標` or `買唔起`. That is a capital-size finding, not a strategy finding, and V6.4 could not have surfaced it.
- **The discipline of freezing `mr_score`/`trend_score` line-for-line** (`rules.py:198-277`) so that any EV change is attributable to the measurement change alone is methodologically correct and worth protecting in future versions.
- **The README's warning that self-test numbers are meaningless** (lines 84-88) is correct and I am glad it is there.

`selftest.py` passes 22/22 on my machine (pandas 3.0.5 / numpy 2.4.6).

---

## 2. Blocking defects

### B-1 — Split-adjusted prices are used to enforce absolute-price limits. This is a multi-year look-ahead in position sizing, and it is the largest remaining inflator.

**Where:** `portfolio_sim.py:104` and `:113` (`auto_adjust=True`) feeding `risk_config.plan_position()` (`risk_config.py:114-182`), specifically the `max_notional` test at lines 156-164 and the `shares` computation at line 149.

**What is wrong.** `auto_adjust=True` returns *back-adjusted* prices: every price before a split is divided by the split ratio. That is the right choice for computing *returns*. It is the wrong series to make *sizing and affordability* decisions on, and V6.5 makes every one of them on it.

The entire V6.5 risk architecture is keyed to an absolute dollar threshold: `max_affordable_price = US$128.21` (`risk_config.py:95-97`). Whether a stock is buyable at time *t* is therefore being decided by corporate actions that happened *after* t.

Concretely, inside the default `2019-01-01 → 2026-07-01` window:

| Ticker | Split in window | Actual price, early 2019 | Price the simulator sees |
|---|---|---|---|
| AMZN | 20:1 (Jun 2022) | ~US$1,700 | ~US$85 |
| GOOGL | 20:1 (Jul 2022) | ~US$1,100 | ~US$55 |
| NVDA | 4:1 (2021) + 10:1 (2024) | ~US$160 | ~US$4 |
| TSLA | 5:1 (2020) + 3:1 (2022) | ~US$65 | ~US$4 |
| AAPL | 4:1 (Aug 2020) | ~US$160 | ~US$40 |
| AVGO, MSTR, SHOP, WMT | 10:1 / 10:1 / 10:1 / 3:1 | — | 3–10x understated |

In 2019 a single AMZN share cost 133% of the entire HK$10,000 account. The simulator will buy it, and will let the 10% concentration cap wave it through, because it thinks the share costs US$85.

**Why this is first-order rather than cosmetic.** The two headline V6.5 fixes are the concentration cap and the integer-share cash ledger. Both are pure functions of absolute share price. My synthetic run shows the concentration cap firing on **344 of 515 rejections (67%)** — it is the single most active constraint in the system. On real data, every one of those decisions is being made on a price that is wrong by 3–20x for roughly a third of the universe, and wrong in a systematically *time-varying* way: the distortion is largest at the start of the sample and zero at the end. The simulator is therefore most permissive precisely where it should be most constrained, and the trade population it produces is not the population a real HK$10,000 account could have traded in 2019-2021.

Note this is *not* the V6.4 M-8 finding. M-8 was "`auto_adjust` is unpinned and might be False". V6.5 correctly closed that by passing it explicitly. This is a new problem created by adding a dollar-denominated constraint on top of an adjusted series — V6.4 had no notional cap, so it did not have this exposure.

**Fix.** Carry two price series. Fetch with `auto_adjust=False` and keep `Close`/`Adj Close` plus the split factor, or fetch twice. Use the **unadjusted** price for `plan_position()` (share count, notional, concentration cap, cash), and the **adjusted** series for indicators and return computation. Reconcile by applying the split factor to the share count on the split date. Until this is done, treat every affordability and concentration statistic — and therefore every fill decision — as unreliable.

---

### B-2 — The look-ahead test cannot fail. I proved this.

**Where:** `selftest.py:143-157`.

```python
df0 = data[tickers[0]]
for i in range(250, min(len(df0) - 1, 900), 37):
    s_a = signal_at(df0, i, True)
    s_b = signal_at(df0.iloc[:i + 1], i, True)   # 個 df 到 bar i 為止,一條都冇多
```

**What is wrong.** `df0` has already been through `add_indicators()` (`selftest.py:42`). Slicing `.iloc[:i+1]` truncates *rows*; it does not recompute the indicator columns. Both calls therefore read byte-identical values out of columns computed on the **full** dataset. The test proves only that `signal_at` does not index past `i` — which is obvious from reading its 40 lines — and proves nothing whatsoever about whether the indicators themselves peek forward. That is where look-ahead actually hides.

**Demonstration.** I replaced `high_20d` with a deliberately future-peeking centred window (`rolling(20, center=True).max()`, which reads 10 bars ahead) and re-ran the exact test loop:

```
with a CENTERED (future-peeking) rolling window injected: 18 samples, 0 mismatches
-> the selftest's test reports PASS on a knowingly look-ahead-contaminated frame
```

The test reports **PASS** on data I had just contaminated on purpose. It is a placebo.

This matters more than a normal test bug. The README's entire claim to have fixed H-1 rests on this check, and the whole point of V6.5 is that you can trust the measurement. A green light that cannot turn red is worse than no light, because it stops anyone looking.

**Fix.** Truncate the *raw* frame and recompute:

```python
raw_trunc = raw.iloc[:i + 1]
s_b = signal_at(add_indicators(raw_trunc), i, True)
```

Also add the same check for the SPY regime flag, which is currently untested end-to-end. Only 18 sample points are tested (`range(250, 900, 37)`); once the test can actually fail, widen it.

---

### B-3 — The broker comparison changes the trade set, so it does not measure the cost of the broker.

**Where:** `portfolio_sim.py:464-522`. The docstring (line 466) says *"同一批數據、同一批訊號,唯一分別係券商成本"* and the printed header (line 492) repeats *"同一批訊號,唯一分別係手續費"*. The README calls this table *"整套 V6.5 最重要嘅一張表"*.

**What is wrong.** The claim is false. Costs are deducted from cash, cash gates the `cash_floor` check (`risk_config.py:167-172`) and the sufficiency check (`portfolio_sim.py:299`), and a rejected fill leaves a position slot open that a *different* signal then occupies. The runs diverge and never reconverge.

**Measured, on identical input data and identical seeds:**

```
free         n=136  grossEV=+0.423%
ibkr_tiered  n=128  grossEV=+0.426%
ibkr_fixed   n=118  grossEV=+0.520%
hk_retail    n= 63  grossEV=+0.049%

entries shared with 'free':  ibkr_tiered 126/136 · ibkr_fixed 117/136 · hk_retail 63/136
```

`hk_retail` keeps **46%** of the free run's trades, and its **gross** EV — before a single dollar of commission is charged — is +0.049% against free's +0.423%. So of the headline "5.05pp of edge eaten by the broker" that `selftest.py:134-137` prints, a large share is not cost at all; it is a different, worse trade population arrived at by path dependence.

The direction is not even guaranteed. A cost model that blocks a slot can just as easily block a loser as a winner. This table cannot be read as a cost decomposition in either direction.

**Fix.** Two changes. (a) Correct the docstring and header — they currently assert something the code does not do. (b) Add a genuine cost decomposition: run the simulation once with `free` to fix the trade set, then re-price *that same fill list* under each cost model. The difference is then attributable to cost alone. Keep the current full re-simulation as a separate "realised path" table, because the path effect is real and worth seeing — it just must not be labelled as cost.

---

### B-4 — There is still no test of whether the edge is real. No benchmark, no interval, no out-of-sample.

Grep-confirmed absent across all four modules: `bootstrap`, `confidence`, `t_stat`, `p_value`, `deflated`, `DSR`, `benchmark`, `buy-and-hold`, `alpha`, `beta`, `walk`, `fold`, `purge`, `embargo`, `holdout`.

Three separate gaps, each sufficient on its own to block a conclusion:

1. **No benchmark.** This is a long-only system that trades only when SPY is above its 200dma, on 38 hand-picked large-caps, over 2019-2026. That description is close to "leveraged beta with extra steps". `report()` prints CAGR, Sharpe and Sortino (lines 372-384) with no SPY buy-and-hold line anywhere. Without it there is no way to tell an edge from beta, and given the structural cap of 5 positions × 10% = **50% maximum exposure** with a 10% cash floor, the most likely honest finding is that this underperforms buy-and-hold badly. That finding should be one line of code away and it currently isn't.

2. **No confidence interval.** `report()` prints net EV to three decimals (line 391) and `compare()` ranks four brokers on it. With ~100-400 trades and several-percent per-trade dispersion, the standard error on that mean is comfortably larger than the number itself. The V6.4 audit's H-7 (trades are clustered in time, so effective *n* is well below nominal *n*) is untouched — clustering is arguably *worse* in V6.5 because the 5-slot cap concentrates entries into whichever days had capacity. **Report EV as an interval or don't report it.** If the interval crosses zero, the verdict is "no conclusion", and the reporting code currently has no way to express that.

3. **Single period, no walk-forward.** The README acknowledges this (line 75). I want to make the consequence explicit, because the README's decision rule leans on the result: the thresholds in `rules.py` were tuned across V1→V6.4 on this same universe over an overlapping window (`momentum_pit_backtest.py:54` also starts `2019-01-01`). Re-running frozen parameters on the data they were tuned on is not validation, no matter how clean the execution model. The V6.4 audit put the honest trial count at N ≥ 20; nothing here has changed that.

**Practical consequence for the README's gate.** The README says: confirm an edge survives costs, *then* pay for point-in-time data. The **negative** branch of that gate is sound — if net EV is negative on a survivor-biased universe with in-sample parameters, it will not improve, and you should stop. The **positive** branch is not. A positive result here is fully explainable by survivorship + in-sample fit + B-1 without any edge existing. Worth writing that asymmetry into the README so nobody reads a green number as permission.

---

### B-5 — The drawdown budget is enforced inside the simulation, so max drawdown is bounded by construction.

**Where:** `portfolio_sim.py:249-254`.

```python
peak = max(e["equity"] for e in equity_hist)
if (peak - equity) / peak * 100 > limits.drawdown_budget_pct:
    rejects.append({... "reason": "回撤預算耗盡" ...})
    continue
```

**What is wrong.** The README's reading order puts max drawdown first (line 96): *"超過 20% 就係 John 嘅 drawdown_budget_pct,系統應該停手"*. But the simulator already stops. Once equity is 20% below peak, no new entries are taken until it recovers. The reported max drawdown is therefore a *conditional* statistic that is mechanically pinned near the limit — it can only exceed 20% through open-position mark-to-market drift.

You cannot use an output to validate the constraint that produced it. As written, the number tells you the kill-switch works; it tells you nothing about the strategy's natural drawdown, which is what sizing, capital allocation and the CRO's limit itself should be set from.

Secondary effect: this appends **one reject row per day** for the entire duration of a drawdown. A single 200-day drawdown injects 200 rows of `回撤預算耗盡` into a ledger the README asks you to read as a composition (rule 3, line 98). That will swamp the signal-level reasons.

**Fix.** Make the budget a flag: `--drawdown-halt / --no-drawdown-halt`. Report unconstrained max drawdown as the primary risk statistic and the halted path as a separate scenario. Record the halt as a state transition (start date, end date, days) rather than one row per day.

---

## 3. Secondary findings

**S-1 — `fx_flat_usd` is declared and never used.** `risk_config.py:40` defines it and sets it to 2.00 for both IBKR models. `one_side()` (lines 42-49) returns `commission + friction` and never references it. Grep across the whole package returns exactly one hit — the declaration. Both `portfolio_sim.py`'s docstring (line 16) and the README (line 55) claim FX conversion is costed. It isn't. This is exactly the class of "declared but dead" defect (`COOLDOWN`, `RISK_PCT`) that V6.5 exists to eliminate, reintroduced. Decide whether FX is per-conversion or per-trade and wire it in, or delete the field.

**S-2 — Cooldown is in calendar days, but the rule is in bars.** `portfolio_sim.py:234` does `today + pd.Timedelta(days=cd)` with `MR_COOLDOWN = 10`. V6.4 declared this in a bar-indexed loop. Ten calendar days is ~7 trading days, so the implemented cooldown is ~30% shorter than the documented rule. `rules.py:124` gives no unit. Add the unit to the field name (`MR_COOLDOWN_BARS`) and index off the ticker's own bar index.

**S-3 — Two report statistics break exactly when the result is bad.**
- `portfolio_sim.py:393`: `eaten = cost_usd.sum() / abs(gross_usd.sum())`. If gross P&L is near zero — the expected case — this prints an arbitrarily large percentage. If it is negative, `abs()` hides the sign and the line reads as though costs ate a positive profit.
- `portfolio_sim.py:407-414`: top-3 concentration is `top3_pnl / total_pnl`. With negative total P&L this returns a negative or >100% percentage, and the README's rule ("if the top 3 are most of it, survivorship is the whole story", line 100) becomes unreadable. Measure concentration on **absolute** contribution (share of gross P&L magnitude), which is well-defined in every sign case.

**S-4 — Portfolio heat is checked in nominal risk and accumulated in realised risk, and can never bind independently.** `risk_config.py:141-145` tests `current_heat_pct + risk_pct` using the nominal 1.0%, while `portfolio_sim.py:304` accumulates `plan["risk_pct_of_equity"]`, the post-rounding realised risk, which is always smaller (47% of budget in the self-test). Separately: `max_portfolio_heat_pct = 5.0` with `risk_pct = 1.0` and `max_open_positions = 5` means the heat cap binds at exactly the same point as the position cap and is therefore redundant. Either lower it so it does real work, or document it as a backstop.

**S-5 — No indicator warm-up buffer.** `load()` (lines 98-119) uses the same start date for download and test. `MA200` needs 200 bars and `signal_at` returns `None` for `i < 200` (line 128), so with the default `--start 2019-01-01` the first ~10 months are structurally trade-free. Those ~200 zero-return days sit in the equity curve and pollute the CAGR window (line 374) and the Sharpe denominator (lines 377-379). V6.4's `momentum_pit_backtest.py:56` had a `DOWNLOAD_START` a year earlier; V6.5 lost it. Add a warm-up download offset and start the equity curve at the first eligible bar.

**S-6 — Rejection reasons are order-dependent and single-valued.** `plan_position` returns on the *first* failing gate in a fixed order (positions full → sector full → heat → can't afford → concentration → cash floor), so a signal blocked by three constraints is attributed to one. With `max_open_positions = 5` against 38 tickers, capacity gates will systematically mask the sizing gates the README asks you to diagnose from (rule 3). Record **all** failing constraints per signal, not the first.

**S-7 — Reproducibility (C-5) is still open.** No `requirements.txt`, no pinned `yfinance`/`pandas`/`numpy`, no run metadata (date, universe, parameter hash, library versions) written into `v65_trades.csv` / `v65_equity.csv` / `v65_rejects.csv`. Two runs a month apart are not comparable and nothing in the artifacts records why. The V6.4 audit's M-8 fix also recommended a data-integrity assert — flag any single-day return below −35% with no matching corporate action — which would have caught B-1 immediately. Not implemented.

**S-8 — Per-trade net EV is re-elevated to headline status.** `report()` line 391 labels it *"呢個先係真嘅"* and `compare()` ranks brokers on it. But C-3's original point was that per-trade EV is *not* a portfolio answer, and per B-3 the trade counts differ across brokers (136 vs 63), so it isn't comparable across the rows of that table either. Rank on terminal equity / CAGR, which the table already computes.

**S-9 — Mark-to-market falls back to entry price on a missing bar.** `portfolio_sim.py:243` uses `pos["entry"]` when a ticker has no bar today. It should carry the last known close forward. As written, a halted or gappy name silently freezes at cost basis, understating both volatility and drawdown.

**S-10 — Gap-up through an Engine 1 target manufactures fictitious losses.** Entry is bar `t+1`'s open (line 286); the target check on that same bar (lines 206-207) fills at `pos["target"]`. If the open gaps *above* the target, the simulator records a buy at the open and a sale below it — a guaranteed loss no real trader would take. Low frequency (the `MR_MIN_R ≥ 2.0` filter puts targets ~10%+ above the close, so it needs a large overnight gap), but it is a free fix: skip the entry, or fill at the open.

**S-11 — Average exposure is misdescribed as idle time.** `portfolio_sim.py:383-384` prints mean `exposure_pct` and then infers *"即係有 X% 時間資金閒置"*. Mean exposure of 20% does not mean 80% of days were flat. The concurrency histogram printed just below (lines 416-419) is the correct statistic for that claim; the inference line should be deleted.

**S-12 — Cosmetics.** `simulate()` accepts `verbose` and never uses it (line 175). `base` in `compare()` (lines 497, 511) is assigned and dead. `report()` writes CSVs to the process CWD (lines 428-430) rather than the repo's `reports/` tree; `.gitignore` covers them, but running from another directory scatters output. `peak` is recomputed by scanning the full history each day (line 251) — O(n²), harmless at this size, one line to fix with a running max.

---

## 4. Scorecard against the U-1 specification

| U-1 requirement | Status |
|---|---|
| Daily event loop over a cash ledger, real starting equity | **Done** |
| Integer share counts via the live position plan | **Done** |
| Explicit `MAX_CONCURRENT` + hard total-risk cap | **Done** (heat cap redundant — S-4) |
| Log every rejected signal | **Done** (single-reason and order-dependent — S-6) |
| Full cost model: commission + half-spread + slippage **+ FX** | **Partial — FX declared, never charged (S-1)** |
| Pessimistic stop fills | **Done** |
| Entry at next bar's open | **Done** |
| Equity curve, max DD, DD duration, worst month, tail | **Done** (max DD bounded by construction — B-5) |
| Exposure %, then and only then Sharpe / Sortino / CAGR | **Done** (ordering respected; no benchmark — B-4) |
| Apply live guardrails so tested = tradeable | **Done for stop-width; broken by B-1 for sizing** |
| U-2 point-in-time universe | Not done — acknowledged |
| U-3 walk-forward with purge/embargo | Not done — acknowledged |
| U-4 Deflated Sharpe / trial count | Not done — **not acknowledged** |
| U-6 Pine golden-file test | Not done — acknowledged, parity table added |
| U-7 Block-bootstrap CI | Not done — **not acknowledged** |
| U-8 Regime-conditional reporting | Partial — `diagnostics()` prints bull-day coverage only |
| U-9 Parameter sensitivity surface | Not done — **not acknowledged** |
| C-5 reproducibility | Not done — **not acknowledged** (S-7) |

The "已知未修" list in the README is honest about U-2, U-3 and U-6. It is silent on U-4, U-7, U-9 and C-5, which together are the entire question of statistical significance. Worth adding them so the gap is visible.

---

## 5. Recommended order of work

**Before running this on real data at all:**

1. **Fix B-2 first** — it is ten lines, and until the look-ahead test can fail, none of the other results mean anything. Recompute indicators on the truncated frame, confirm it still passes, then confirm it *fails* on an injected centred window.
2. **Fix B-1** — split-unadjusted prices for sizing, adjusted for returns. Without this the concentration cap, the affordability rejections and the fill list are all wrong for roughly a third of the universe over the first half of the sample.
3. **Wire in or delete `fx_flat_usd` (S-1)** — one line either way, and leaving a dead cost field in the cost module undermines the module's purpose.

**Before drawing any conclusion from the output:**

4. **Add the SPY buy-and-hold benchmark line** to `report()` (B-4.1). Cheapest high-value addition in this list — it may make everything else moot.
5. **Add a block bootstrap CI on net EV** (B-4.2), 20-day blocks to preserve clustering, and make "interval crosses zero → no conclusion" an expressible verdict.
6. **Make the drawdown halt a flag** (B-5) and report unconstrained drawdown as the primary risk number.
7. **Fix the broker comparison** (B-3): re-price a fixed trade set for the cost decomposition, keep the re-simulation as a separately labelled path-effect table, and correct the docstring and header text.

**Then, and only then**, the README's gate becomes meaningful — with the caveat from B-4 that a negative result is conclusive and a positive one is not.

**Non-negotiable before any real capital**, per the firm's standing rules: S-7 reproducibility. Pin the libraries, stamp run metadata into every CSV. A decision journal entry that cites a number nobody can reproduce is not institutional memory.

---

## 6. One structural observation

The most valuable thing in V6.5 is not any single fix — it is the rejection ledger and the insistence on printing the ugly numbers first. That is the right instinct and it should survive into V7.

The pattern worth watching, though, is that **V6.5's two new defects (B-1, B-5) were both created by its own fixes.** Adding a dollar-denominated concentration cap created the split-adjustment exposure. Adding a drawdown kill-switch made the drawdown statistic self-referential. Each new control introduced a new coupling between the risk layer and the measurement layer, and neither coupling was tested for.

The general defence is the one already half-built here: every constraint added to `risk_config.py` needs a corresponding invariant in `selftest.py` that can actually fail. B-2 shows the test suite currently contains at least one assertion that cannot — which is worth checking for across the rest of the file before the next constraint is added.
