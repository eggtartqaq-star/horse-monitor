# Backtest Audit — `strategy/v6.4/`

**Question asked:** is the +1.3% EV / 45% win rate edge real?

**Short answer:** the number is not measuring what you think it is measuring, and at
your stated account size the strategy cannot clear its own commission bill even if
the number were true. Two separate findings, and they need separate verdicts:

| | Verdict |
|---|---|
| Is the system tradeable at HK$10,000? | **REFUTED** — the ticket costs more than the expected profit. |
| Does the system have an edge at *any* size? | **UNPROVEN** — the test cannot distinguish a real edge from its own biases. |

"UNPROVEN" is not "this doesn't work." It means the instrument you built to measure
the strategy reads high, and you cannot tell by how much without re-running it. I
want to be precise about that because you have months in this and the distinction
matters for what you do next.

I did not run the backtests (no market data, and the download step needs 15–30
minutes of live yfinance calls). Everything below is reasoned from the code. Where a
figure is needed to make a cost or a bias concrete, I label it as an assumption and
tell you what to substitute.

---

## What's actually right — read this first

There is real craft in here, and some of it is better than what I see in
professional code. It needs to survive whatever you do next.

1. **Gap protection on the trailing stop.** `oos_validation.py:249–252` fills at
   `r2["Open"]` when the open gaps below the trail rather than at the stop price;
   `momentum_pit_backtest.py:227` does the same with `min(pos["trail"], row["Open"])`.
   The overwhelming majority of retail backtests fill every stop at the stop price
   and quietly book a few percent per year that does not exist. You didn't.

2. **The stop is checked *before* the trail is updated.** `oos_validation.py`
   tests `r2["Low"] <= trail` at line 248 and only then raises the trail at line 259.
   `momentum_pit_backtest.py` does the same (line 226 before line 238). Getting this
   backwards is the single most common look-ahead in trend-following code and it
   inflates every result. My scanner flagged both files as candidates; reading them,
   the ordering is correct in both. This is the thing I most want you not to break.

3. **Same-bar ambiguity resolved against yourself.** `simulate_mr()` checks
   `Low <= stop` before `High >= target`. When a bar touches both, you book the loss.
   That is the conservative choice and it is the right one.

4. **The OOS pass mark was written down in advance.** `oos_validation.py:12–15`
   states 健康 / 警戒 / 不合格 with a numeric 50%-decay threshold, and line 371 says
   the correct response to failure is to admit overfitting rather than re-tune. Writing
   the failure criterion before seeing the result is genuine discipline. The test
   underneath it is broken — that's most of this report — but the intent is right.

5. **The momentum pool ranking really is point-in-time.** `momentum_pit_backtest.py:197`
   slices `df.loc[:today]` before ranking and re-ranks monthly. The ranking logic is
   correct. Only the candidate set it ranks over is contaminated (finding C-1).

6. **`mr_plan` takes the wider of the structural and ATR stop** (`min(stop_struct,
   stop_atr)`), and puts a 0.5% buffer below the 10-day low. Both are conservative,
   both are real-trader details.

7. **The Telegram bot refuses HK tickers** ("港股:系統以美股回測,未經驗證,唔應該做")
   and refuses anything outside the 38-name pool. Those are *mechanical* controls —
   the software says no. Keep this shape; see the note on position sizing at the end.

---

## CRITICAL findings

### C-1 — The 38-ticker list was chosen in 2026 to be backtested over 2022–2026

**Where:** `oos_validation.py:31–40` (and the same 38 names in
`telegram_swing_bot.py:51–56`, `momentum_pit_backtest.py:58–69` for the 121-name fallback)

```
"NVDA", "PLTR", "MSTR", "COIN", "AVGO", "META", "TSLA", "SHOP", "UBER", "AMD", ...
```

This is the list that produced your +1.3%. It is 38 names, hand-written, containing
NVDA, PLTR, MSTR, COIN and AVGO — four of which are famous specifically *because* of
what they did between 2023 and 2026. MSTR and PLTR were not names a 2022 trader would
have put on a 38-stock shortlist; they are on this list because you already know how
the period ended.

Engine 2 buys 20-day highs in strong uptrends. You have pointed a trend-following
system at a hand-picked list of the period's biggest trends. That is close to a
tautology, and it is enough on its own to generate the entire +1.3%.

The mirror-image problem is worse and less obvious: **there is not a single name on
this list that failed.** No delisting, no acquisition, no company that broke a 20-day
high and then went to zero. The failure mode Engine 2 is most exposed to — buying
strength into a collapse — has been removed from the sample by construction. You are
measuring the upside of a distribution with the left tail deleted.

**Why the OOS split does not fix this.** Your graduation exam splits *time*, not
*universe*. In-sample and out-of-sample both draw from the same 38 hindsight-selected
names. A temporal split can detect parameter instability. It is structurally incapable
of detecting universe selection. The test you trust most is blind to the largest bias
in the study.

**Direction: overstates. Magnitude: unknown until re-run — which is the point.**

---

### C-2 — `momentum_pit_backtest.py` claims to have solved survivorship and has not

**Where:** `momentum_pit_backtest.py:70–84` vs `:309`

The file scrapes **today's** S&P 500 membership from Wikipedia
(`pd.read_html(".../List_of_S%26P_500_companies")`) and then runs a 2019–2026 backtest
over it. Every company deleted from the index between 2019 and 2026 — the bankruptcies,
the acquisitions, the ones that shrank out — is absent.

The file's own docstring is honest about this (limitation #1, lines 27–30: "呢層仍有
輕微生存者偏差"). Then line 309 prints:

> `★ 鐵律:呢個係point-in-time,冇生存者偏差。`

Both statements are in the same file. The second one is what you'll remember at 11pm
when the result looks good, and it is false. You fixed the *ranking* to be
point-in-time — correctly, and it was the harder engineering job — and then filed the
whole survivorship question as solved. A clean ranking over a dirty universe is still
dirty.

Also: "輕微" (slight) is doing unearned work there. S&P 500 turnover is roughly 4–5%
of constituents per year; over 7.5 years that's on the order of 200+ name-entries that
existed in the tradeable universe at some point and are missing from yours. For a
momentum strategy that specifically buys the top 50 by 126-day return, the deleted
names are disproportionately the ones that ran up and then broke.

**Concrete fix:** delete line 309. Then either buy a point-in-time constituent file
(Norgate, CRSP, or the S&P DJI historical membership file) or run the cheap diagnostic
in finding H-4 first.

---

### C-3 — No transaction costs anywhere, and the arithmetic ends the analysis

**Where:** all five files. `grep -rin "commission\|slippage\|spread\|fee"` over
`strategy/v6.4/` returns nothing. Every fill in every backtest is at `Close`, for free.

Here is the calculation, in dollars rather than percent, because percent hides this
problem at small account sizes.

From `telegram_swing_bot.py:42–44` and `:167–175`:

```
ACCOUNT_HKD = 10000  →  US$1,282
RISK_PCT    = 1.0    →  risk budget per trade = US$12.82
```

Engine 2's stop is `3 × ATR`, capped at 12% of entry (`oos_validation.py:239`).
*Assumption:* take a 10% stop distance as typical for the high-ADX names this engine
selects — substitute your own median from `oos_e2_oos.csv`, you have the data.

```
position notional  = 12.82 / 0.10            = US$128
gross expected P/L = 128 × 1.325%            = US$1.70 per trade
```

Now the ticket. *These commission figures are illustrative — replace them with your
actual broker's schedule:*

| Broker scenario | Round-trip cost | vs US$1.70 gross |
|---|---|---|
| IBKR tiered, USD already funded | ~US$0.94 | eats 55% |
| IBKR fixed (US$1.00/side min) | ~US$2.24 | **loses money** |
| IBKR fixed + HKD→USD conversion | ~US$4.24 | **loses 2.5×** |
| HK retail broker (HK$100/side min) | ~US$25.6 | **loses 15×** |

You trade HK names too — 1888 appears in your own note at the top of
`momentum_pit_backtest.py`. On a US$128 position a HK retail minimum commission is
fifteen times the expected profit. That is not a strategy, it is a subscription to
your broker.

**Minimum viable account size.** Solving for the notional at which the round trip
falls below 20% of gross EV (IBKR tiered, USD pre-funded, 9.5bp of spread+slippage
per side):

```
2 × 0.35 + 0.0019 × N  ≤  0.20 × 0.01325 × N
                  0.70 ≤  N × 0.00075
                     N ≥ US$933  notional
```

At a 10% stop and 1% risk, notional = 10% of account, so:

```
minimum account ≈ US$9,300   ≈ HK$73,000     (IBKR tiered)
minimum account ≈ US$27,000  ≈ HK$208,000    (IBKR fixed)
```

Your account is HK$10,000. You are **7× to 20× below** the size at which this system
can pay for its own execution. No amount of further parameter work changes that
number; it is arithmetic on the commission schedule, not on the strategy.

This is the finding I would act on first, because it needs no market data, no
point-in-time universe, and no further code — and it can flip the sign of the answer.
There is no point spending money on clean data to more precisely measure a system that
costs more to trade than it earns.

I'll note that `strategy/v6.5/risk_config.py` already contains a cost model reaching
the same conclusion (net EV: best +0.53%, median −0.49%, HK retail −2.06%). My
arithmetic above was done independently from v6.4 alone and lands on the same US$128
notional and US$1.70 gross figure, which is a real corroboration. **Run
`python portfolio_sim.py --mode diagnostics` before you do anything else.**

---

## HIGH findings

### H-1 — The in-sample window is ~10 months shorter than advertised, and it deletes the 2022 bear market

**Where:** `oos_validation.py:325–331`

```python
spy = yf.Ticker("SPY").history(period=DATA_PERIOD)   # "4y"
spy["MA200"] = spy["Close"].rolling(200).mean()
spy_bull_raw = (spy["Close"] > spy["MA200"])
```

SPY is downloaded for exactly 4 years, then MA200 is computed on it. The first ~200
trading days have `MA200 = NaN`, and `NaN > NaN` is `False` in pandas — so `bull` is
`False` for the first ten months and **no trade is ever taken there.** Both engines gate
on `bull`.

Consequence: a 4-year download minus 18 months of OOS leaves a nominal 30-month
in-sample window, of which the first ~10 months are silently dead. The real in-sample
period is roughly 20 months, and — running from today's date — the discarded stretch
is precisely the late-2022 bear tail.

So the trend-following engine's entire evidence base is ~2023-06 to 2026-08: one very
large bull market with two shallow corrections. A trend follower tested only inside a
trend. Combined with C-1, that is two independent reasons the +1.3% is not evidence
about the strategy.

**Fix:** download `period="5y"` (or `"6y"`) for SPY and slice the test window to the
last 4 years *after* the MA200 has warmed up. Print the actual first-trade date so the
shrinkage can never be invisible again.

---

### H-2 — In-sample Engine 1 trades resolve using out-of-sample data; Engine 2 trades at the boundary vanish

**Where:** `oos_validation.py:172–186` (Engine 1) vs `:243–246` (Engine 2)

Engine 1:
```python
def simulate_mr(df, i, entry, stop, target):
    n = len(df)          # ← the FULL dataframe, not end_idx
```
`run_engine1(df, bull, 60, cut_idx)` opens trades up to the cutoff, but `simulate_mr`
is bounded by `len(df)` — so an in-sample trade opened 3 bars before the cutoff
resolves using up to 7 bars of **out-of-sample data**. Your in-sample number is
contaminated with the sample you were supposed to be holding back.

Engine 2, in the same file, does the opposite:
```python
j = i + d
if j >= end_idx:
    break        # exit_ret stays None → trade silently discarded
```
Trades still open at a window edge are dropped entirely. In a trailing-stop system,
losers exit in days and winners run to the 60-day cap, so the open-at-boundary
population is winner-skewed. This one works *against* you — it suppresses reported EV.
I'm flagging it anyway, because:

**The two engines handle the same boundary in opposite directions.** One leaks forward,
one truncates. The in-sample and out-of-sample numbers you compare are not
measurements of the same thing, and the 50%-decay pass criterion is applied to a ratio
of two differently-biased quantities.

The same silent discard exists in `momentum_pit_backtest.py`: positions left in
`open_positions` when `full_range` is exhausted are never appended to `trades`.

**Fix:** one boundary policy, applied to both engines and stated in the output — either
(a) allow trades to resolve past the edge and label the window by *entry* date, or
(b) truncate at the edge and mark the exit as forced, counting them. Print the number
of boundary-affected trades either way.

---

### H-3 — Per-trade EV pooled across 38 tickers is not a portfolio result

**Where:** `oos_validation.py:344–347`, `momentum_pit_backtest.py:187, 266`

```python
e2_is  += run_engine2(df, bull, 80, cut_idx)      # pooled across all 38 tickers
```

Every ticker is simulated in isolation and the trades are averaged as if they were
independent draws from an urn. They are not: they are concurrent, correlated (38 US
large-caps, heavily tech-weighted, in a common bull regime), and they compete for the
same capital. Missing entirely:

- **No cap on simultaneous positions.** `momentum_pit_backtest.py` can hold up to 50
  at once (the whole pool). At 1% risk each with 10% stops, that is 50% portfolio heat
  and ~500% notional leverage. Not fundable in a cash account.
- **No cash ledger.** Nothing checks whether the money exists.
- **No integer share sizing in the backtest at all.** The backtest works purely in
  percent returns, which implicitly assumes fractional shares. Live,
  `position_plan()` does `int(risk_usd // per_share)` with a US$12.82 budget — so on a
  US$200 stock with a US$20/share stop you get **0 shares**, and the trade doesn't
  happen. On a US$128 stock you get exactly 1 share, and that one share is 10% of your
  entire account in a single name.

That last point is a genuine backtest-vs-live divergence, not a rounding nitpick: at
HK$10,000 you can only take the *cheap* signals. The live system trades a
price-biased subset of the backtest's trades, and the sizing rule discards up to 100%
of the risk budget to rounding. The +1.3% is an average over a trade population you
cannot actually take.

**A 1% risk rule with no concurrency cap is an uncapped leverage rule wearing a modest
label.**

---

### H-4 — No equity curve, no drawdown, anywhere

**Where:** all five files. `grep -rin "drawdown\|equity\|sharpe\|sortino"` over
`strategy/v6.4/` returns two Cantonese comments telling you to remember to look at
drawdown (`momentum_pit_backtest.py:32, 303`) and zero lines that compute one.

You are about to add money to a system whose worst-case loss has never been calculated.
The reported statistics are trade count, win rate, average win, average loss, EV, hold
days, best trade, worst trade. Worst *single trade* is not drawdown — a run of eleven
consecutive −8% trades is a −60% account and every one of them looks unremarkable in
that table.

Report in this order, before return and before Sharpe:

1. max drawdown
2. drawdown duration (days underwater — this is what actually makes people quit)
3. worst month
4. 5th-percentile trade and the worst five trades
5. *then* return, *then* Sharpe

**Cheap diagnostic worth running before you buy any data:** compute EV contribution
per ticker. If three or four names carry the whole +1.3%, C-1 is the complete answer
and you can stop the investigation there. `strategy/v6.5/portfolio_sim.py --mode
diagnostics` appears to do exactly this and costs nothing.

---

### H-5 — The sample is almost certainly too small to distinguish +1.3% from zero

Your stated numbers imply a very right-tailed distribution. *Working from your 45% win
rate and +1.3% EV, and assuming an average loss near the 3×ATR stop of about −8%
(substitute your real `avg_loss` from the CSVs):*

```
0.45·W + 0.55·(−8) = 1.3   →   average win ≈ +12.7%
σ ≈ sqrt(0.45·(12.7−1.3)² + 0.55·(−8−1.3)²) ≈ 10.3%
```

For a t-statistic of 2 you need:

```
n ≥ (2 × 10.3 / 1.3)² ≈ 250 trades
```

And that is the requirement for **a single hypothesis tested once.** See H-6 for how
many you actually tested. The code prints a warning when `n < 30`
(`oos_validation.py:314`) — a good instinct, but 30 is off by an order of magnitude for
a distribution this skewed. With this shape, the EV is dominated by a handful of large
winners, and whether those winners are in your sample is close to a coin flip.

---

## MEDIUM findings

### M-1 — Roughly 80 hand-tuned numbers, and the headline change was selected *because* it quadrupled the backtest

Count of researcher degrees of freedom in `mr_score()` alone: 24 threshold boundaries,
25 assigned score values, 6 weights. `trend_score_calc()` adds ~30 more. Then
`MR_SCORE_MIN=0.55`, `TREND_SCORE_MIN=0.65`, `MIN_R=2.0`, `ATR_STOP_MULT=2.0`,
`ATR_TRAIL_MULT=3.0`, `MR_MAX_HOLD=10`, `TREND_MAX_HOLD=60`, `MAX_STOP_PCT=15`, the
12% cap, `TOP_N=50`, `MOMENTUM_LOOKBACK=126`, the 2.0 speculative-stock ratio. **Over
80 free parameters**, all chosen by hand.

Then this comment, at `telegram_swing_bot.py:233` and repeated in the Pine at line 60:

> `V6.2升級：止蝕=結構位與2×ATR取較闊(C臂,回測EV 0.24%→1.10%)`

A single parameter change multiplied backtest EV by 4.6×. That is not a discovered
effect; that is the signature of a fitted parameter. Real edges do not quadruple when
you widen a stop — what quadruples is the fit between your rule and the particular
path your particular 38 stocks happened to take. And the +1.3% you're asking me about
is downstream of that change: it is the number the tuning was steered toward.

**The version numbers are themselves evidence.** V6.2 → V6.4 → V6.5, with "C臂"
implying at least an A and a B arm. You have run many more variants than one, over the
same data, and then run "the" out-of-sample test once.

Which brings us to the core problem with the graduation exam:

> `oos_validation.py:370` — "呢個測試冇任何參數可以調 —— 規則鎖死同V6.4一致。"

The rules are locked *at the moment the test runs*. But they were **chosen** while you
already knew what 2022–2026 looked like, on the same 4 years of data the test then
splits. A temporal split is only out-of-sample if the parameters were fixed before
that data existed. Yours weren't. It is an in-sample test wearing an out-of-sample
label.

**Fix, in order of honesty:** (a) walk-forward — re-fit on each expanding window, test
on the next, report the *distribution* across folds rather than one number; (b) a
deflated Sharpe using the real trial count (be honest: 20+ variants); (c) genuinely
frozen forward paper trading with the pass mark written down first, which you already
know how to do.

### M-2 — Signal and fill on the same bar's close

**Where:** `oos_validation.py:236`, `momentum_pit_backtest.py:263` — `entry = row["Close"]`

Engine 2's entry condition includes `row["High"] >= row["high_20d"]` and a `trend_score`
computed from that bar's close. All of it is known at the close, so this is
*executable* — but only with a market-on-close order, every time, with no hesitation.
It is not the fill you'll get scanning after the close and ordering the next morning,
which is what `daily_strong_signals.py` is built for ("每日收市後跑一次").

The honest default is signal at bar *t*, fill at bar *t+1* open. Given that overnight
gaps in high-ADX momentum names are systematically adverse to breakout entries, I'd
expect this to cost a meaningful fraction of a 1.3% EV. Test it — it's a one-line
change and the delta tells you how much of the edge was living in that assumption.

### M-3 — Regime filter reads forward on non-trading days

**Where:** `momentum_pit_backtest.py:212–214`

```python
idx = spy_bull.index.searchsorted(today)
if idx < len(spy_bull):
    is_bull = bool(spy_bull.iloc[idx])
```
`full_range = pd.bdate_range(...)` includes market holidays. On a holiday `today` is
not in the SPY index and `searchsorted` returns the insertion point — **the next
trading day**. You gate a holiday's decisions on tomorrow's regime. Small (roughly 9
days a year), but it is free to fix: use `method="ffill"` reindexing as
`oos_validation.py:340` already correctly does.

### M-4 — Single data vendor for prices, stops and sizing

Every file sources from yfinance with no cross-check. yfinance silently changes
adjustment behaviour between versions; `auto_adjust=True` is passed in
`momentum_pit_backtest.py` but *not* in the `yf.Ticker(...).history()` calls in
`oos_validation.py` or `telegram_swing_bot.py`. Different adjustment conventions
between the backtest and the live bot means different ATRs, therefore different stops,
therefore different positions — with no error raised anywhere.

---

## Parity — the tested system is not the traded system

This is check 7 and it found more than I expected. You have five artifacts
implementing "V6.4" and they disagree with each other in ways that matter.

| # | Divergence | Where |
|---|---|---|
| P-1 | **The Pine indicator implements Engine 1 only.** No trend engine, no 3×ATR trail, no ADX≥25 route. | `dual_engine_v6_4_tiers.pine` — entire file |
| P-2 | **Stop-width cap has three different values.** Backtest E2: 12%. `trend_plan`: 12%, then a dead 15% check. Pine: 15%. Backtest E1: **no cap at all**. | `oos_validation.py:239`, `telegram_swing_bot.py:49,156`, `.pine:73` |
| P-3 | **Take-profit selection rules differ.** Python picks the *nearest* target with R≥2; Pine prefers `high60`, the *farther* one, with no R filter on the choice. | `telegram_swing_bot.py:255` vs `.pine:66` |
| P-4 | **`COOLDOWN = 10` is declared and never referenced.** The backtest re-enters the same name one bar after an exit. | `oos_validation.py:49` |
| P-5 | **`daily_strong_signals.py` cannot run.** It imports `dual_engine_v6_4`, which does not exist in this repo. | `daily_strong_signals.py:33` |
| P-6 | **Two `trend_score` implementations with different signatures.** The scanner calls `sc, _ = trend_score(row)` expecting a tuple; the bot's returns a float. | `daily_strong_signals.py:124` vs `telegram_swing_bot.py:149` |
| P-7 | **Regime filter differs by market.** Bot uses `^HSI` for HK; Pine always uses `AMEX:SPY` regardless of the charted symbol. | `telegram_swing_bot.py:69` vs `.pine:31` |
| P-8 | Pine file header says "V6.2 三級訊號指標（均值回歸引擎）" in a file named `..._v6_4_tiers.pine`. | `.pine:2` |

**P-1 and P-2 are the ones that cost money.** Engine 2 is the engine you have declared
your main system ("OOS已驗證,主力", `daily_strong_signals.py:145`) — and it has no
representation on your chart at all. Every visual confirmation you have ever taken from
the TradingView indicator was about the engine you've labelled "OOS偏弱,觀察為主".

And in P-2, `run_engine1` has *no* stop-width cap, so the backtested mean-reversion
population includes trades with arbitrarily wide stops that both the bot and the chart
would block. Backtest population ≠ live population.

**Fix:** one file is the source of truth for rules; everything else imports from it.
`strategy/v6.5/rules.py` already does this — port the Pine to match it, or accept that
the chart is decoration and stop reading signals off it.

---

## The sizing incidents — this is a bug, not a discipline failure

The note at the top of `momentum_pit_backtest.py:20–26` says you entered 1888 with 500
shares (11× oversize) on 7/13 and BAC with 300 shares (100× oversize) on 7/18, and
tells you the backtest already assumes you'll follow the 1% rule.

Both halves are true, and the second half matters: a backtest that assumes compliance
is measuring a system nobody is trading. But before concluding indiscipline, check the
tool.

**There is a currency bug in `position_plan()`.** `telegram_swing_bot.py:167–175`:

```python
risk_usd = ACCOUNT_HKD * RISK_PCT / 100 / USD_HKD    # = US$12.82
per_share = entry - stop                              # for 1888.HK this is in HKD
shares = int(risk_usd // per_share)                   # USD ÷ HKD
```

For a HK ticker — which `normalize_ticker()` cheerfully accepts and routes straight
into this function — a **USD** risk budget is divided by an **HKD** per-share risk. The
suggested share count for HK stocks is wrong by a factor of 7.8. The identical bug is
in the Pine at line 79–81 (`riskUSD` divided by a chart-currency `perShareRisk`).

Nothing in the system also checks HK board lots, so on 1888.HK the "correct" answer it
gives you may not even be a placeable order.

So on 7/13 the tool handed you a number that was wrong, in an instrument the tool's own
output tells you not to trade, in a currency the sizing function does not handle. That
is a control-design failure, not a character failure.

The deeper issue: at HK$10,000, a 1% risk rule yields 0 to 3 shares on most US
large-caps. A control that outputs "buy 1 share of BAC" is a control that will be
overridden, because it feels absurd — and the code's response to that is a printed
lecture at the top of a backtest file. **A control that routes through willpower at the
moment of the trade has already failed.** Your bot's POOL check is the right shape: the
software refuses. Build sizing the same way (refuse to display a plan when
`shares < 1`, rather than displaying it with a warning), and note that the real fix is
H-3's finding — the account is below the size where this system's own rules produce
sensible orders.

---

## Verdict and what to do, in order

**REFUTED at your current account size.** Finding C-3 is arithmetic on a commission
schedule, not an opinion about markets. US$1.70 of expected gross profit per trade
against a US$0.94–$25 round trip does not become profitable through better parameters.
You need roughly HK$73,000–208,000 depending on broker before this system can pay for
its own execution.

**UNPROVEN as a strategy, at any size.** Even granting the +1.3%, it was measured on a
hindsight-selected 38-name list with no failures in it (C-1), over an effective window
that is almost entirely a single bull market (H-1), with in-sample and out-of-sample
boundaries handled in opposite directions (H-2), pooled as if trades were independent
(H-3), on a rule set with 80+ hand-tuned parameters whose headline change was selected
for quadrupling the backtest (M-1), with a sample size likely ~5× short of
significance (H-5). Any one of these could produce +1.3% from nothing. I cannot tell
you the strategy doesn't work. I can tell you this evidence doesn't show that it does.

### Ranked by what unblocks the most

1. **Run `strategy/v6.5/portfolio_sim.py --mode diagnostics`.** Free, needs no new data,
   and it answers two questions at once: what does net EV look like after costs, and is
   the EV concentrated in three or four tickers? If it is, C-1 is the whole story and
   you can skip step 3 entirely. *This is the one to do first — it can change the sign
   of the answer, and everything below only refines a number that may well be negative.*

2. **Add max drawdown and drawdown duration to every result you ever look at again.**
   You are sizing an account against a number you have never computed.

3. **Only if 1 and 2 survive:** buy a point-in-time universe with delisted names and
   re-run. This costs real money; do not spend it until steps 1 and 2 say there is
   something worth measuring.

4. **Fix the IS/OOS asymmetry** (H-2) and the SPY MA200 warm-up (H-1) so the in-sample
   window is what the docstring claims, then re-run the graduation exam. Expect the
   in-sample number to fall.

5. **Collapse the five implementations into one rule module** and port the Pine to
   Engine 2, or stop treating the chart as confirmation.

6. **Delete `momentum_pit_backtest.py:309.** A false claim in a print statement is
   more dangerous than a bug, because it survives every rewrite.

### One thing not to do

Do not respond to a disappointing re-run by re-tuning. You already wrote the correct
instruction at `oos_validation.py:371`: *"如果OOS唔合格,正確反應係承認過度擬合,唔係調
參數令佢過關。"* That sentence is the most valuable line in the codebase. It applies to
this report too.

---

*Audit performed by reading `strategy/v6.4/` only; no files were modified. Backtests
were not executed — no market data and the download paths require live network calls.
All cost, ATR-ratio, average-win and volatility figures above are labelled assumptions
derived from your stated statistics and the constants in your code; substitute your
real broker schedule and the real `avg_loss` / `n` from `oos_e2_oos.csv` before acting
on any of them.*
