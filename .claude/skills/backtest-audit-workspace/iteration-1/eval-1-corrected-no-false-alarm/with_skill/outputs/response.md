# V6.5 Measurement Audit — `strategy/v6.5/`

**Scope:** read-only review of `rules.py`, `risk_config.py`, `portfolio_sim.py`, `selftest.py`, `README.md`, with `strategy/v6.4/` used as the comparison baseline. Nothing under `strategy/` was modified.

**What I could and could not run:** `selftest.py` runs and passes all 22 checks in this environment. I could **not** run `portfolio_sim.py` against real data — Yahoo is blocked by the proxy here (`curl 56 / CONNECT tunnel failed 403`). So every finding below is reasoned from the code, and every dollar figure is an *illustrative* calculation from the constants in your own files, not a measured result. Substitute your real commission schedule before acting on any of them.

---

## Verdict

Two different verdicts, and the distinction matters:

| Question | Verdict |
| --- | --- |
| Is the system tradeable at HK$10,000 today? | **REFUTED** — the cost arithmetic decides it, and V6.5 already computes the arithmetic itself. |
| Does the underlying strategy have an edge? | **UNPROVEN** — the instrument is much better, but two defects still sit upstream of every number it will print. |

"UNPROVEN" is not "it doesn't work." It means the evidence this code can currently produce cannot distinguish a real edge from the remaining biases. That is the correct and expected state after a measurement-layer rebuild; it is not a failure of the rebuild.

**The honest summary of V6.5:** you set out to fix *how you measure* rather than *what you buy*, and on that specific goal you largely succeeded. Costs, drawdown, portfolio constraints, look-ahead in the signal path, and boundary truncation are all genuinely fixed. What V6.5 has *not* done — and what the README is only half-honest about — is fix the two things that determine whether the output means anything: the universe, and (new to V6.5) the fact that the dollar-denominated risk gates you just built are being fed prices that were never traded.

---

## What is right — do not destroy these in V6.6

I am listing these first deliberately, because the next rewrite is where good work usually dies.

1. **The report order in `report()` (`portfolio_sim.py:359-384`) is exactly correct.** Max drawdown, drawdown duration, worst month, worst single trade, 5th percentile, worst five — then return, then Sharpe last, under a heading that literally says "先講醜嘅". Most professional backtests do not do this. Keep the order and keep the headings.

2. **Stop is checked *before* the trailing level is updated** (`portfolio_sim.py:201-215`, with the comment `★ 先檢查止蝕,後更新移動止蝕 —— 唔可以掉轉`). This is the single most common silent inflator in trailing-stop backtests and you got it right and knew why.

3. **Gap protection on the stop fill** (`portfolio_sim.py:204`): `exit_px = min(pos["stop"], row["Open"])`. A gap through the stop fills at the open, not at the stop. Correct.

4. **Same-bar ambiguity resolved against the trader** (`portfolio_sim.py:202-207`): when a bar's Low touches the stop *and* its High touches the target, the stop wins. That is the conservative choice and it is the right one.

5. **The signal path has no look-ahead.** Signal computed on bar `t`'s close, filled at bar `t+1`'s open (`portfolio_sim.py:284-286`), with the SPY regime flag shifted by `REGIME_LAG_BARS = 1` (`portfolio_sim.py:117`). `NOTE_REGIME_LAG` in `rules.py:160-169` explains the reasoning and even tells the reader to set it to 0 and compare, which is the right experiment. This is a real fix to a real V6.4 defect.

6. **`OPEN_AT_END` (`portfolio_sim.py:316-330`) fixes a genuine bug.** V6.4's `oos_validation.py:246` has a bare `break # OOS邊界:未平倉交易棄掉` — trades open at the window boundary were discarded. In a trailing-stop system losers exit fast and winners run, so the discarded population skewed to winners. Marking them and marking them to market is the correct fix.

7. **The cash ledger is internally consistent, and I checked the arithmetic.** Entry debits `notional + one_side(entry)`; exit credits `exit_px*shares - one_side(exit)`; the trade record's `net_usd = gross - round_trip`. The two agree exactly. `selftest.py` confirms cash never goes negative (min $712.05 in the synthetic run). Integer shares, max 5 positions, portfolio heat cap, sector cap, cash floor — all present, all enforced by exception rather than by warning.

8. **The reject ledger is an unusually good idea.** Recording *why* a signal did not become a trade — and treating that record as a finding in its own right — is something most retail and plenty of institutional backtests never do. It is the mechanism that separates "the strategy is bad" from "the account is too small," which are completely different problems with completely different fixes. (See M-1 below for a counting bug that currently degrades it.)

9. **Freezing `mr_score()` / `trend_score()` unchanged from V6.4 was the correct experimental design**, and `rules.py:191-196` states the reason precisely: change the measurement and the strategy together and you can never attribute the EV difference to either. This is disciplined thinking and it is rarer than it should be.

10. **`selftest.py` exists, runs offline, and passes** — and the README explicitly warns (lines 84-88) that synthetic random-walk results have no edge *by definition* and that the negative numbers prove the simulator can count costs, not that the strategy loses. That warning prevents a specific and very common self-deception.

11. **`budget_used_pct`** (`risk_config.py:181`) surfaces how much of the risk budget integer-share rounding throws away — 47% in the synthetic run. Most backtests never look at this.

12. **The `--mode compare` table with `free` as an explicit row** (`portfolio_sim.py:464-522`) is the best single artifact in V6.5. Framing the zero-cost row as "the world V6.4 was implicitly assuming" and every other row as "the world you actually live in" is exactly the right way to present it.

13. **`BROKERS` is labelled as illustrative** (`risk_config.py:56`: `★ 佣金數字係說明性假設,唔係查證過嘅收費表`). Good. Keep that label until you paste in your real schedule.

---

## Findings

### CRITICAL

#### C-1 — The universe is unchanged, and it is now being applied to a *longer* window than it was written for

`portfolio_sim.py:45-53`. The 38 tickers are byte-for-byte identical to `strategy/v6.4/oos_validation.py:32-40`. That V6.4 file downloads `DATA_PERIOD = "4y"`. `portfolio_sim.py:529-530` now defaults to `--start 2019-01-01 --end 2026-07-01` — 7.5 years.

So a hand-written list, composed no earlier than roughly 2022 for a four-year test, is now being run back to 2019. Every name on it is a name that still existed, still mattered, and was still worth typing at the moment it was typed. The list contains PLTR, COIN, MSTR, SHOP, UBER, NVDA — six names whose presence is inseparable from how the period turned out. It contains no name that was delisted, acquired, or destroyed during the window, because nobody types those.

The README is honest that this is unfixed (F-01, lines 72-75) and Tom's sequencing — confirm the edge survives costs before spending US$50-150/month on point-in-time data — is correct. I am not disputing the sequencing. I am flagging that the README's framing understates the problem in one specific way: **this is not merely "the universe is incomplete." It is "the universe was selected with knowledge of the outcome, and V6.5 extended the test backwards into the part of history where that knowledge is most contaminating."**

This matters most for Engine 2 (trend). Engine 2 buys 20-day highs with ADX ≥ 25 and DI+ > DI−. It buys strength. The names that were strong and then died are precisely the ones absent. Engine 2's reported edge is the one you should trust least.

**Direction: overstates returns. Magnitude: unknowable from this code — which is the entire point.**

**Fix (do not do this first — see the priority list):** point-in-time index membership (Norgate, Sharadar). Until then, when you read the concentration block in `report()` (`portfolio_sim.py:406-414`), treat "top 3 names contribute > 50% of P&L" not as a warning but as confirmation that C-1 is the whole answer.

---

#### C-2 — Split-adjusted prices are feeding dollar-denominated risk gates. This one is new to V6.5, and it corrupts the diagnostic V6.5 was built to produce.

`portfolio_sim.py:104` and `:113`: `yf.Ticker(tk).history(..., auto_adjust=True)`.

`auto_adjust=True` back-adjusts the entire OHLC series for splits and dividends using the *full future* history. This is harmless for every **ratio-based** quantity in `rules.py` — RSI, ADX, ATR-as-a-fraction, MA crossovers, `price_vs_ma20`, `ret_10d` are all scale-invariant, so the *signals* are fine.

It is **not** harmless for anything denominated in dollars — and V6.5 is the first version that has anything denominated in dollars. Specifically:

- `RiskLimits.max_notional_usd` = **US$128.21** (`risk_config.py:91-92`)
- `max_affordable_price` = **US$128.21** (`risk_config.py:95-97`) — "the price at which a single share already exceeds the concentration cap"
- the `shares < 1` "買唔起" gate (`risk_config.py:151-153`)
- the concentration gate at `risk_config.py:159-164`
- `per_share_usd` commission (`risk_config.py:44`), which is computed on a share count that is itself split-distorted

These gates compare a *price* against a *fixed dollar threshold*. Back-adjustment makes historical prices **lower** than the prices that were actually quoted, for every name that later split. Your universe is full of them: AAPL, TSLA, NVDA, AMZN, GOOGL, AVGO, SHOP, MSTR and WMT all executed splits inside 2019-2026 (verify the exact ratios against your own data — see the snippet below).

Worked mechanism, using NVDA as the illustration. NVDA's cumulative post-2019 split factor is large (a 4:1 in 2021 and a 10:1 in 2024 compound to 40:1). Take a hypothetical 2019 bar:

| | As actually traded (illustrative) | As `auto_adjust=True` presents it |
| --- | --- | --- |
| Price | ~US$200 | ~US$5 |
| Risk budget | US$12.82 | US$12.82 |
| Stop distance @ 5% | US$10.00/share | US$0.25/share |
| Shares from risk budget | 1 | 51 |
| Notional | US$200 | US$255 → capped to 25 sh = US$125 |
| `plan_position` outcome | **Blocked** — 一股 US$200 > 上限 US$128.21 | **Passes** — a normal 25-share position |

The backtest takes a trade that reality would have refused, in the name that contributed most of the period's momentum. And it does this **selectively**: only for the names that later split, which — because companies split after their price rises a lot — is the same set as "the names that went up the most."

The consequence is worse than a mis-sized position. **It corrupts the reject ledger**, which the README (line 45, lines 98-99) designates as *the* output you read to decide whether the problem is the strategy or the account size, and to decide whether to spend money on data. The ledger will systematically under-count "買唔起" and "單一倉位集中度超標" for exactly the winners, so it will tell you the account is less of a constraint than it really was. The instrument's flagship new reading is biased, and biased in the flattering direction.

**Fix.** Naively switching to `auto_adjust=False` is **not sufficient** — Yahoo's raw OHLC is already split-adjusted; only the dividend adjustment is removed. You must reconstruct the as-traded price from the splits column:

```python
# in load(), illustrative
df = yf.Ticker(tk).history(start=start, end=end, auto_adjust=True, actions=True)
sp = df["Stock Splits"].replace(0.0, 1.0)
# forward-looking cumulative split factor: divide out future splits to recover as-traded price
df["px_as_traded"] = df["Close"] * sp[::-1].cumprod()[::-1] / sp
```

Then: keep the adjusted series for `add_indicators()` and for return/P&L continuity, and pass `px_as_traded` to `plan_position()` and to the commission model. Two price columns, two jobs. Verify with one line against a known split:

```python
# should show ~US$150-240 for NVDA in early 2019, not ~US$5
print(df.loc["2019-01":"2019-02", ["Close", "px_as_traded"]].head())
```

Add a `selftest.py` invariant: inject a synthetic 10:1 split and assert `plan_position` blocks on the pre-split price.

---

### HIGH

#### H-1 — `fx_flat_usd` is declared, populated, documented as charged, and never charged

`risk_config.py:40` declares `fx_flat_usd: float = 0.0`. `risk_config.py:59-60` sets it to `2.0` for both IBKR scenarios. `one_side()` (`:42-49`) and `round_trip()` (`:51-53`) **never reference it**. I verified by introspection: the string `fx_flat_usd` appears exactly once in the class source — the declaration.

Meanwhile `README.md:55` states the V6.5 fix as `兩邊都計:佣金 + 半差價 + 滑價 + 匯兌` — commission + half-spread + slippage + **FX**. The document claims a cost line the code silently drops.

This is not cosmetic at your account size. With `max_notional_usd = US$128.21`, a US$2.00 FX charge is **1.56% of a full-size position** — larger than every other cost component combined.

Here is what it does to the decision, using V6.4's own gross EV of 1.325% (`risk_config.py:225`) on a US$128.21 position → **US$1.70 expected gross profit per trade**:

| Broker | Round trip as coded | Net EV/trade | If FX were charged once per round trip | Net EV/trade |
| --- | --- | --- | --- | --- |
| `free` | $0.00 | **+$1.70** | $0.00 | +$1.70 |
| `ibkr_tiered` | $0.94 | **+$0.76** | $2.94 | **−$1.24** |
| `ibkr_fixed` | $2.24 | **−$0.54** | $4.24 | **−$2.54** |
| `hk_retail` | $4.32 | **−$2.62** | $4.32 | −$2.62 |

*(Round-trip figures computed directly from your `CostModel` at notional US$128.21; the FX column is my arithmetic, not the code's.)*

**`ibkr_tiered` is the only scenario in which V6.5 currently reports a positive net EV, and it survives solely because the FX charge is dropped.** Charge it and every scenario is negative. A one-line bug is holding up the only surviving positive result in the whole comparison table.

**Fix — and be careful, because the obvious fix is also wrong.** Do not simply add `self.fx_flat_usd` to `one_side()`: that charges a currency conversion on every leg of every trade, which nobody actually does. FX is an **account-level** cost — you convert HKD to USD once, or a few times a year. The honest model is to deduct it from the opening cash balance and on any top-up, not per trade. Either implement it that way, or set the field to `0.0` and delete the word 匯兌 from `README.md:55`. What you must not leave is a documented cost that does not exist.

---

#### H-2 — There is no benchmark, and V6.5 removed the only out-of-sample test that existed

Two related gaps that together prevent the output from supporting a decision even if C-1 and C-2 were fixed.

**No benchmark.** `report()` computes CAGR, Sharpe, Sortino, and total return — all in absolute terms. There is no comparison to SPY buy-and-hold. SPY is already downloaded and sitting in the `spy` DataFrame at `portfolio_sim.py:113-118`. This is a strategy that goes long US megacaps, only when SPY is above its 200-day MA, at an average exposure the report itself will tell you is low (`portfolio_sim.py:383-384` prints the idle-capital percentage). Over 2019-2026, a modest positive CAGR is entirely compatible with severe underperformance of simply holding the index. Without that row, the report cannot answer the only question that matters: *is this better than doing nothing?*

**No out-of-sample split.** V6.4's `oos_validation.py` had an IS/OOS split (`OOS_MONTHS = 18`) with the pass mark **written down in advance** (lines 12-15: healthy = OOS EV positive and ≥ 50% of in-sample; fail = OOS EV negative) and an explicit warning at line 371 that the correct response to a failure is to admit overfitting rather than tune until it passes. That is genuinely good methodology.

V6.5 deletes that file's role (`portfolio_sim.py:6`: "呢個檔案取代 oos_validation.py 同 momentum_pit_backtest.py 嘅統計部分") and replaces it with a single continuous full-period simulation. The `break` boundary-truncation bug is fixed by construction — there is no boundary — but so is the boundary. The README lists walk-forward as "known unfixed, next step" (F-10), which reads as *not yet added*. It is more accurate to say it was **removed**: V6.5 reports one in-sample number where V6.4 at least attempted a split.

This matters because of what is in `rules.py`. `mr_score()` and `trend_score()` contain **21 hand-tuned numeric boundaries** (confirmed by the scanner), plus `MR_SCORE_MIN`, `TREND_SCORE_MIN`, `ADX_RANGE_MAX`, `MR_MIN_R`, the two ATR multiples, two max-hold values, and the cooldown. Every one of them was chosen while looking at this universe over this period. V6.5 re-measures on the same universe over a *longer* slice of the same period. Freezing the thresholds was the right call for attributing the EV change (see strength #9) — but it does not make the resulting number out-of-sample. It is in-sample with respect to roughly thirty researcher degrees of freedom.

**Fix.** (a) Add a SPY buy-and-hold row to `report()` and to the `compare()` table — it costs about ten lines and the data is already loaded. (b) Restore an OOS split with the pass mark written down *before* you look, reusing V6.4's criteria. (c) Longer term, walk-forward with a deflated Sharpe using the real trial count. On trial count: git history shows V6.4 → V6.5, and both `rules.py` and `risk_config.py` carry 13 version references each. The true number of variants tried before V6.4 is known only to you, and it is the input the deflation needs.

---

### MEDIUM

**M-1 — The reject ledger mixes per-day and per-signal events, so its counts are not comparable.** `portfolio_sim.py:251-254` appends a `回撤預算耗盡` row **once per calendar day** while drawdown exceeds 20%, whereas every other reason is appended **once per rejected signal**. `report()` (`:423-425`) then prints `rejects["reason"].value_counts()` as a single ranked table and instructs the reader (`:426`) to conclude "account too small, not strategy broken" if 買唔起/集中度 dominate. A single long drawdown will contribute hundreds of rows and can dominate the table on its own. *Fix:* record the drawdown halt in a separate counter, or emit it once per halt episode rather than once per day.

**M-2 — The look-ahead selftest cannot detect indicator-level look-ahead.** `selftest.py:146-155` calls `signal_at(df0, i, True)` and `signal_at(df0.iloc[:i+1], i, True)` and asserts equality. But `df0` is the output of `add_indicators()` run once over the *full* series — the test slices an already-computed frame. If someone later adds a non-causal indicator (a `center=True` rolling window, a `.bfill()`, a percentile over the whole sample), both calls read the same contaminated value at bar `i` and the test **passes**. It currently passes honestly because every indicator in `rules.py:85-109` is causal — I checked each one — but the test has no power to catch the regression it exists to catch, and V6.5's central claim is that the instrument is now verified. *Fix:* keep the raw OHLCV and recompute: `s_b = signal_at(add_indicators(raw.iloc[:i+1]), i, True)`. Also widen the sample — it currently tests 18 points on one ticker.

**M-3 — Candidates from both engines are ranked by raw score, which are not on the same scale.** `portfolio_sim.py:281`: `candidates.sort(key=lambda s: -s["score"])`. Engine 1 admits scores ≥ 0.55, Engine 2 ≥ 0.65. When the 5-position cap or the heat cap binds, E2 signals systematically win the tie against E1 signals of equal *quality*, purely because their admission floor is higher. This is a capital-allocation rule between engines that nobody chose. *Fix:* rank on a normalised score (e.g. `(score - engine_min) / (1 - engine_min)`), or rank by expected R, or alternate — but choose it deliberately and record the choice.

**M-4 — Stop-loss exits are charged the same slippage as entries.** `CostModel.one_side()` applies `(half_spread_bp + slippage_bp)` symmetrically. Real stop exits are worse than entries: they fire into moving markets and, in this simulator, sometimes into gaps (`portfolio_sim.py:204`). Understating exit slippage biases net EV upward, and it biases it most on losing trades. *Fix:* separate `entry_slippage_bp` from `stop_slippage_bp` and set the latter 2-3× higher, then re-read `compare()`.

**M-5 — Six new free parameters entered with V6.5 and none has a sensitivity test.** `max_open_positions = 5`, `max_portfolio_heat_pct = 5.0`, `max_per_sector = 2`, `cash_floor_pct = 10.0`, `drawdown_budget_pct = 20.0`, `max_position_notional_pct = 10.0` (`risk_config.py:74-79`). These came from John as risk policy rather than from fitting, which is the right provenance — but they materially determine the result. `max_open_positions = 5` alone caps the whole system's exposure. If reported performance moves a lot when 5 becomes 4 or 6, that is a fitted parameter wearing a risk-policy label. *Fix:* one sensitivity sweep, reported as a range rather than a point.

**M-6 — Two reporting statistics mislead under plausible conditions.** (a) `portfolio_sim.py:393`: `eaten = cost_usd.sum() / max(abs(gross_usd.sum()), 1e-9) * 100`, printed as `= 毛利嘅 {eaten}%`. If gross P&L is a *loss*, `abs()` makes this print a meaningless positive percentage described as a share of gross profit. Guard the negative case explicitly. (b) `portfolio_sim.py:365-367` prints 最差單筆(淨) and 第5百分位交易 as percentages of *position notional*, directly beneath 最大回撤 as a percentage of *equity*, under one heading. With a 10% position cap a −15% trade is −1.5% of equity. The two numbers differ by roughly an order of magnitude and the report invites the reader to compare them. Label the denominators.

---

### LOW

**L-1 — Parity is unresolved, and the live path is still V6.4.** `rules.py` is a real single source of truth *for the V6.5 simulator*, and that is progress. But `strategy/v6.4/telegram_swing_bot.py` — the thing that actually messages you — does not import it and still hardcodes `MAX_STOP_PCT = 15.0` at line 49. `NOTE_PINE_PARITY` (`rules.py:171-185`) honestly documents three divergences and two missing items in the Pine script, all unfixed: Engine 2 absent from Pine entirely, opposite take-profit selection (Pine prefers the farther `high60`, `mr_target()` at `rules.py:280-288` takes the nearest qualifying target), no cooldown in Pine. **The chart, the bot, and the backtest are still three different strategies.** Tom's golden-file proposal (export N historical bars of tier/stop/target/R and require Pine to reproduce them) is the correct mechanism — it is the only one that stops the drift recurring. Until then, the honest move is John's: rename the Pine script to state that it is Engine 1, observation only.

**L-2 — The `1.325%` gross EV constant is inherited from the measurement V6.5 exists to replace.** It is hardcoded in a docstring and a print at `risk_config.py:13` and `:225`. It came from V6.4's per-trade pooling — no costs, no concurrency cap, boundary-truncated. Once `portfolio_sim.py` produces a real number, replace it, or the cost-vs-EV comparison is anchored to a figure you have already declared unreliable.

**L-3 — Dead code.** `simulate(..., verbose=True)` accepts `verbose` and never uses it (`portfolio_sim.py:175`). `base` in `compare()` (`:497`, `:501-502`) is assigned and never read. Small, but "declared and never used" is exactly the class of bug that H-1 turned out to be — worth a sweep.

**L-4 — Default `--end 2026-07-01` is a month stale** (today is 2026-08-03). Consider defaulting to today so the window does not silently freeze.

**L-5 — `load()` silently drops tickers with `len(df) < 300`** (`portfolio_sim.py:106`). Harmless in the current window, but it is a listing-date filter: a 2025 IPO would vanish rather than enter from its listing date. Log the drops so they appear in the run record.

---

## Minimum viable account size

This is the calculation that ends the analysis, and it needs no market data. Using your own `CostModel` constants and V6.4's gross EV of 1.325% of notional (**replace both with your real numbers**), and the standard bar that round-trip cost should be under ~20% of gross EV:

| Broker | Cost as % of gross EV **at your current US$128.21 position** | Min viable position | Min account @ 10% cap |
| --- | --- | --- | --- |
| `ibkr_tiered` | 55% | ~US$930 | **~US$9,300 (HK$73k)** |
| `ibkr_fixed` | **132%** | ~US$2,670 | **~US$26,700 (HK$208k)** |
| `hk_retail` | **254%** | ~US$26,700 | **~US$267,000 (HK$2.1M)** |

Your account is **HK$10,000 = US$1,282**, with a maximum position of **US$128.21**.

Note the `hk_retail` row especially. Its spread-plus-slippage alone is 0.25% round trip, which is **19% of a 1.325% gross EV before a single dollar of commission**. No account size fixes that — scaling up removes the commission floor but never the friction. Under this cost model `hk_retail` is not a "needs a bigger account" problem; it is structurally unviable for this strategy.

Every figure here is illustrative and derived from constants in your files. But the shape of the conclusion does not depend on the precise inputs: **at HK$10,000, the expected gross profit per trade and the round-trip ticket are the same order of magnitude.** That is the definition of a commission-generation machine, and no further optimisation of the signal changes it. V6.5 deserves real credit here — `risk_config.py:219-226` computes and prints this itself, and says so plainly ("有幾多個情境嘅來回成本大過 US$1.70,就有幾多個情境你係喺度做義工"). The instrument told you the truth. The remaining work is to believe it.

---

## Priority — what to do first, and what not to do

Ranked by what unblocks the most, with a bias toward fixes that can **change the sign of the answer** over fixes that refine a number which may well be negative.

1. **Fix H-1 (FX), today.** Ten minutes. It is the only thing standing between "one broker scenario is positive" and "no broker scenario is positive." Decide whether FX is per-trade or account-level, implement that, or zero the field and correct the README. Do not spend another hour on anything else while a documented cost is silently absent.

2. **Fix C-2 (split-adjusted prices vs dollar gates).** Half a day, no purchase required. Until this is done the reject ledger — the diagnostic the README tells you to base the point-in-time-data decision on — is biased in your favour, precisely in the names that matter. Fixing it is a prerequisite for the decision in step 4.

3. **Add the SPY buy-and-hold row (H-2a).** Ten lines, data already loaded. Without it the report cannot say whether the system beats doing nothing.

4. **Then run `--mode diagnostics`, then `--mode compare`.** Read them in the README's own order: max drawdown, net vs gross EV, reject ledger, concentration, concurrency. Tom's sequencing at README line 45 is right and I would not change it. If the top-3 names carry most of the P&L, C-1 is the whole answer and you stop there.

5. **Only then decide about point-in-time data.** There is no point paying US$50-150/month to more precisely measure a system whose ticket cost exceeds its expected profit at your account size. Steps 1-4 answer that for free.

6. **Restore the OOS split with the pass mark written down first (H-2b).** Reuse V6.4's criteria verbatim — they were well specified. Then M-2 (strengthen the look-ahead test), then M-5 (sensitivity sweep), then walk-forward.

**Do not** touch `mr_score()` / `trend_score()` yet. Your reasoning at `rules.py:191-196` is correct and holds: change the measurement and the strategy at the same time and you lose the ability to attribute anything. Leave them frozen until `portfolio_sim.py` — with H-1 and C-2 fixed — has produced a baseline.

---

## Closing

The question was "is the measurement sound now?" The precise answer: **the accounting is sound; the inference is not yet.**

V6.5 fixed the things a backtest gets wrong about *arithmetic* — costs on both sides, a cash ledger that balances, concurrency and concentration limits that block rather than warn, drawdown statistics that exist at all, no look-ahead in the signal path, and no silent disposal of open trades at the boundary. I checked those and they hold up. That is a substantial and well-executed piece of work, and the decision to freeze the strategy while rebuilding the instrument was the right one for the right reason.

What it has not fixed is the *provenance* of the evidence: a universe selected with hindsight, prices that were never traded feeding the new dollar gates, no benchmark, and no out-of-sample split. Those four sit upstream of every number the new instrument will print, so a better instrument does not yet produce a better answer.

And on the narrower question — should this be traded at HK$10,000 — V6.5 already answered it, in its own output, before I got here. Fix the FX line so the last positive number stops being an artifact, and the answer will be unanimous across all four broker scenarios.
