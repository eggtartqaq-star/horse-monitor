# Is the V6.4 edge real?

**Short answer: you cannot tell from this backtest, and the one calculation that *can* be
done without market data says the edge is smaller than your trading costs.**

I read all five files in `strategy/v6.4/` line by line. I did not run anything — the four
Python files don't parse (see §6), so the code in the repo is not the code that produced
`+1.3%`. Everything below is derived from the logic, and every estimate is labelled as one.

I changed nothing under `strategy/`.

---

## 1. The bottom line, in the order that matters

1. **The number is gross.** There is no commission, spread, or slippage anywhere in the
   codebase. At your account size (HK$10,000, from `telegram_swing_bot.py:42`) the expected
   gross profit per trade is roughly **US$2**, and a round-trip ticket at IBKR's fixed tier
   is **US$2**. The edge and the fee are the same size. This alone should stop new money.
2. **The universe is hand-picked 2026 winners.** `oos_validation.py:31-40` is a manually
   typed list containing NVDA, PLTR, COIN, MSTR, TSLA, SHOP. Backtesting a trend system on
   stocks you selected in 2026 *because they went up* over 2022-2026 is not a test.
3. **"Per-trade EV" is not a result.** No equity curve, no drawdown, no position sizing, no
   concurrency limit, no benchmark. You cannot annualise it, compare it to buy-and-hold, or
   size anything with it.
4. **The holdout is not a holdout.** The system is called V6.**4**. Every prior version was
   evaluated on this same window. The last 18 months have been seen many times.
5. **The sample is far too small for the claim**, even before the above. See §5.

None of these is a matter of opinion. Each is visible in the code, and **all of them push
the reported number in the same direction — up.**

---

## 2. The calculation that decides it: cost vs. edge

Using only constants from your own files:

| Input | Value | Source |
|---|---|---|
| Account | HK$10,000 ÷ 7.8 = **US$1,282** | `telegram_swing_bot.py:42,44`; `.pine:20,22` |
| Risk per trade | 1.0% = **US$12.82** | `RISK_PCT`, same files |
| Engine 2 stop | 3×ATR, capped 12% → ~8% typical *[estimate: 14-day ATR on large-caps runs 2-3% of price]* | `trend_plan`, `telegram_swing_bot.py:151-158` |
| **Position notional** | 12.82 ÷ 0.08 = **US$160** | derived |
| **Gross profit per trade at +1.3%** | **US$2.08** | derived |

Now the friction. I'm using the bp figures from your own `v6.5/risk_config.py:57-60`
(2.5bp half-spread + 7bp slippage per side = 0.19% round trip):

| Broker | Round-trip ticket | Ticket as % of $160 | + spread/slip | **Net EV** | **Net $/trade** |
|---|---|---|---|---|---|
| "free" (what V6.4 assumes) | $0.00 | 0.00% | 0.19% | +1.11% | $1.78 |
| IBKR tiered ($0.35 min/side) | $0.70 | 0.44% | 0.19% | **+0.67%** | **$1.07** |
| IBKR fixed ($1.00 min/side) | $2.00 | 1.25% | 0.19% | **−0.14%** | **−$0.22** |
| HK retail (~$2/side) | $4.00 | 2.50% | 0.19% | **−1.39%** | **−$2.22** |

**Best realistic case you keep half the edge. Mid case you have no edge. This is before
any of the other four problems.**

There is also a fifth cost the table doesn't capture: **entry look-ahead.** Every entry is
decided from the closing bar's `Close`, `ADX`, `ATR` and `vol_ratio`, then filled at that
same close (`oos_validation.py:236`, `momentum_pit_backtest.py:263`). To submit a
market-on-close order you must commit before ~15:50 ET, when none of those values exist yet.
For Engine 2 the entry bar is *by construction* a 20-day breakout day — a strong,
one-directional bar that tends to close near its high, so the miss is adverse more often
than not. **Estimate: 0.10-0.30% per trade**, another 8-23% of the claimed edge.

Credit where it's due: **exits are clean.** `simulate_mr` starts at `j = i+1` and Engine 2's
loop starts at `d = 1`. There is no same-bar exit look-ahead. The bias is entry-only, but
it is on 100% of trades.

---

## 3. The universe problem — and the single cheapest test you can run

`oos_validation.py:31-40` is not an index, a screen, or a rule. It is 38 tickers typed by
hand in 2026, including **MSTR** (a leveraged bitcoin proxy that ran roughly 20x in the test
window), **COIN**, **PLTR**, **NVDA**, **TSLA**, **SHOP**. The same list is your live pool
(`telegram_swing_bot.py:51-56`), which means the live system is itself a standing bet that
the 2022-2026 winners keep winning.

**Why this specifically breaks a mean-of-percentage-returns statistic:** an unweighted mean
is dominated by its right tail. *[Illustrative arithmetic]* if six MSTR/COIN/PLTR trades in
a 200-trade sample each returned +60%, they contribute `6 × 60 / 200 = +1.8%` to the mean —
**more than your entire claimed edge of +1.3%.** The edge could be, in its entirety, four
tickers you chose because you already knew the answer.

**And you currently cannot check**, because the trade records don't store the ticker:

```python
# oos_validation.py:214 and :264 — the entire trade record
trades.append({"ret": res[0], "days": res[1]})
```

No ticker. No date. The saved CSVs make per-name attribution impossible.

> ### Run this first, before anything else in this document
> 1. Add `"ticker": tk` and `"entry_date"` to those two `trades.append` calls.
> 2. Print EV grouped by ticker.
> 3. Re-run with MSTR, COIN, PLTR and NVDA removed.
> 4. Separately: sort trades by return, drop the top 5, recompute EV.
>
> **If the edge collapses under either test, you are done — there is no system, there is a
> bet on a handful of stocks, and no amount of further work fixes that.** This costs you
> twenty minutes and it is the highest-information test available.

`momentum_pit_backtest.py` deserves genuine credit: the *ranking* is properly point-in-time
(`sub = df.loc[:today]` then `.iloc[-1]`, with a correct one-year warmup). But the
*candidate set* is the **current** S&P 500 scraped from Wikipedia and applied back to 2019.
The dominant bias there isn't bankruptcies — it's **index-inclusion look-ahead**: companies
added to the index in 2023-25 are present in the 2019-22 candidate set, and the reason they
were added is that they went up enormously. You then rank that set by trailing 6-month
momentum, which is the best available proxy for "this is one of the ones that went up." The
contamination and the selection rule point in the same direction.

The file's docstring (L28-30) honestly calls this "輕微生存者偏差" — *slight* survivorship
bias. But line 309 prints to your screen: **"★ 鐵律:呢個係point-in-time,冇生存者偏差"**
(*iron rule: point-in-time, no survivorship bias*). **The headline you read is false and the
file's own fine print says so.** Delete that line.

One silent amplifier: `pd.read_html` against Wikipedia fails routinely, and the bare
`except Exception` at L80-84 falls back to `FALLBACK` — the hand-picked list — with no record
in the output. **You may already have run the hand-picked version without knowing.** Make
that fallback fatal.

---

## 4. "+1.3% per trade" is the wrong statistic, and the 1% rule isn't in the backtest

```
grep -rniE "drawdown|sharpe|sortino|equity|cagr" strategy/v6.4/*.py
→ two Cantonese comments telling the reader to "remember to look at drawdown".
  Zero lines that compute one.
```

```
grep -n "RISK_PCT" momentum_pit_backtest.py
→ 48:RISK_PCT = 1.0    ← the declaration. That is the only occurrence.
```

The docstring at L25-26 states the backtest "已經自動遵守1%規則" — already automatically
obeys the 1% rule. **It does not.** There is no share count, no cash ledger, no equity, no
capital check anywhere. The code appends raw percentages and averages them. `COOLDOWN = 10`
in `oos_validation.py:49` is likewise declared and never referenced — I grepped both.

**Concurrency is unbounded.** `open_positions` is keyed by ticker, so the cap is one per
pool member = **50 simultaneous positions**. At 1% risk each that is 50% of the account at
risk at once, and 50 × US$160 = **US$8,000 of notional on a US$1,282 account — 6x leverage.**
Against `config/risk-limits.yaml` that breaches `leverage: none` (hard rule),
`max_single_position: 0.10` (a US$160 position is 12.5% of your account — breached on
essentially every trade), and `max_correlated_cluster: 0.40` (the pool is one momentum
factor; in a drawdown these names correlate ~0.8+).

**And the diversification is illusory in the way that matters.** Every entry condition —
`SPY > MA200`, `ADX ≥ 25`, `DI+ > DI−`, new 20-day high, top-50 momentum — is a market-beta
condition. On a breadth-thrust day it is entirely plausible that 10-30 of the 50 pool
members trigger simultaneously. The backtest opens all of them. **Your account can fund
about seven.**

That last point is worse than it sounds, because **capital rationing does not remove trades
at random.** Signals cluster at the start of market up-legs, which is exactly when the best
trend trades begin. A capital-constrained live account systematically misses the best
entries, so your live trades are drawn from a *worse* subpopulation than the backtest's.

There is also **no benchmark anywhere** (grep confirmed: no SPY return comparison,
no buy-and-hold). The test window is `SPY > MA200`-gated inside 2019-2026 — nearly all bull
market. A long-only trend system on the strongest mega-caps during that window should make
money. **You have not established that it beats holding SPY, or holding the same stocks.**

---

## 5. The sample is not big enough to support the claim

From your own numbers: 45% win rate, +1.3% EV. Solving `0.45W + 0.55L = 1.3` with a
trailing-stop loss of about −6% gives an average win near **+10%**. That implies a per-trade
standard deviation of **at least 8%** ignoring within-group dispersion, and realistically
**10-12%** for a trend system with a long right tail.

Trades needed for the mean to be distinguishable from zero:

| Standard | σ = 8% (floor) | σ = 11% (realistic) |
|---|---|---|
| Plain 95% (t ≈ 1.96) | **145 trades** | **275 trades** |
| Corrected for ~20 variants tried (V1→V6.4) | **345 trades** | **653 trades** |

Those must be **independent** trades. Yours are not: every entry is gated on market-wide
conditions, so trades arrive in bursts and share most of their return variance. The standard
error of a clustered mean is understated by roughly `√(1 + (m−1)ρ)`; *[illustrative]* with 5
concurrent trades at ρ=0.6 that's **1.8x**, at 10 and ρ=0.7 it's **2.7x**. A nominal
200-trade backtest has an effective sample nearer **30-60**. An 18-month OOS has an
effective sample in the **single digits to low teens.**

The pass criterion makes this concrete. `verdict()` at `oos_validation.py:294-315` passes on
`oos_ev > 0 and oos_ev >= is_ev × 0.5`. No null hypothesis, no confidence interval, no
minimum sample — it *prints* a warning when `n < 30` (L314) and then issues the verdict
anyway. *[Illustrative, σ=6%, n=40]*: **given a strategy with exactly zero edge, this test
reports "an edge exists" about 50% of the time and awards the top grade about 25% of the
time.** That is a coin flip wearing a lab coat, and it's before counting the ~20 variants.

The `DATA_PERIOD = "4y"` window is also **relative to the run date** — the IS/OOS boundary
slides every time you run it, and the outputs record no run date. Your own comment at
`momentum_pit_backtest.py:295` cites Engine 2 OOS figures for *both* "2025-26" *and*
"2018-21", which means the window has already been moved between runs. Every rerun on a
moving window is another trial, and nobody is counting them.

---

## 6. Smaller things that still change the answer

- **All four Python files fail to parse.** Verified with `ast.parse`: unterminated string
  literals at `daily_strong_signals.py:40`, `momentum_pit_backtest.py:73`,
  `oos_validation.py:304`, `telegram_swing_bot.py:79`. Looks like a copy/paste
  transcription artifact (hard-wrapped at ~78 chars, content lost mid-expression), but the
  consequence stands: **the artifact I audited is not the artifact that produced +1.3%,**
  and it isn't reproducible. `dual_engine_v6_4.py` — the module `daily_strong_signals.py:33`
  imports the live logic from — isn't in the repo at all.

- **Engine 1 has no gap-through-stop modelling; Engine 2 does.** `simulate_mr` L180-181
  returns *exactly* the stop price whenever `Low <= stop`. If a stock gaps $100 → $84 with a
  stop at $94, this books −6%; the real loss is −16%. Engine 2 handles this correctly
  (`if Open < trail: exit_price = Open`). Compounding it: **neither backtest has an earnings
  filter, but the live system does** (`telegram_swing_bot.py:439`). So the backtest holds
  mean-reversion positions straight through earnings — the single largest source of overnight
  gaps — and then assumes perfect stop fills on them. The reported "worst single trade" is
  bounded by the stop distance *by construction*, which is precisely the reassurance you
  should not be given. One-line fix: `exit_price = min(stop, r["Open"])`.

- **The 0.65 trend threshold is really 0.55.** `run_engine2` requires
  `row["High"] >= row["high_20d"]` as an entry gate — and then `trend_score_calc` awards
  `+0.10` for that same condition (`oos_validation.py:166-167`,
  `momentum_pit_backtest.py:135-136`). Since `high_20d` is a rolling max *including* today,
  every candidate that reaches the scoring function has already satisfied it. **The bonus is
  a constant, not a discriminator**, so `TREND_SCORE_MIN = 0.65` is effectively 0.55 on the
  four components that actually vary. Not fatal, but the threshold you think you tuned isn't
  the one operating.

- **Engine 1 was measured at a tier you don't trade.** Live, Engine 1 requires
  `score ≥ 0.55 AND R ≥ 2 AND RSI2 < 10 AND R ≥ 3.0` to reach STRONG
  (`daily_strong_signals.py:57-64`), and the scanner only surfaces STRONG/PREMIUM. But
  `run_engine1` (L196, L209) tests `score ≥ 0.55 AND R ≥ 2` — the **BASIC** tier, the one
  you're told not to trade. **The "Engine 1 是 OOS偏弱" conclusion that demoted it to
  observation-only was measured on a different rule.**

- **The chart disagrees with the engine.** Python takes the *nearest* valid target
  (`target = min(valid, key=lambda x: x[0])[0]`, `oos_validation.py:209-211`); the Pine you
  look at *prefers the 60-day high* (`.pine:66`). They diverge exactly when both MA50 and
  the 60-day high clear 2R — the deeper-pullback, wider-stop trades. On that subset the chart
  shows a **higher R**, so it promotes to 強/頂級 setups the scanner calls 普通. Same ticker,
  same day, two answers. The `+1.10%` figure printed in the comment on line 60 of that very
  file was produced by the *nearest-target* rule. Until they're reconciled, **trust the
  scanner, not the chart.**

- **The Pine file has no Engine 2 at all.** Its header says "均值回歸引擎" — mean-reversion
  only. Yet `daily_strong_signals.py:145` calls Engine 2 「主力」, the main engine. **Your
  primary engine has no chart representation**, so every chart-driven decision you make is an
  Engine 1 decision — taken from the engine your own system labels OOS-weak.

- **One bias runs the other way, and I want to flag it for fairness.** `run_engine2` drops
  any trade still open at the window boundary (`if j >= end_idx: break`, L244-246 — `exit_ret`
  stays `None` and the trade silently vanishes). In a trailing-stop system, duration and
  return are mechanically coupled: losers stop out in days, winners run to the 60-day cap. By
  length-biased sampling, **the discarded trades are disproportionately winners**, so the true
  gross Engine 2 EV is *higher* than +1.325%. This does not rescue the system — §2, §3 and §4
  are each individually larger — but it's real. Fix: assign trades to the window of their
  *entry* and let the exit resolve past the boundary. That is not look-ahead; the entry
  decision used no future data. (Note the inverse defect in Engine 1: `simulate_mr` is bounded
  by `len(df)`, not `end_idx`, so in-sample trades resolve using up to 10 bars of OOS data.
  **The two engines are measured under different boundary rules — which makes the IS→OOS
  decay comparison between them, the thing that drove your capital allocation, not
  comparable.**)

---

## 7. So: should you put more money in?

**No — not yet, and the reason is arithmetic rather than judgement.** At HK$10,000 with a
US$1-2 round-trip ticket, the strategy is a commission-generation machine even if the edge
is entirely real. Fixing the account size and fixing the measurement are two different
problems and you should not conflate them.

In order, cheapest and most decisive first:

1. **Add `ticker` to the trade records and re-run without MSTR/COIN/PLTR/NVDA. Also drop the
   top 5 trades and recompute.** Twenty minutes. If the edge collapses, stop here.
2. **You have already built the fix for the rest of it.** `strategy/v6.5/` has
   `portfolio_sim.py` (cash ledger, integer shares, `MAX_OPEN_POSITIONS`, per-ticket costs,
   equity curve, max drawdown), `risk_config.py` (four broker cost models), and `rules.py`
   as a single source of truth — with the scoring functions carried over from V6.4 unchanged,
   which is the right call. **Run it:**
   ```
   python selftest.py
   python portfolio_sim.py --mode diagnostics
   python portfolio_sim.py --mode compare
   ```
   The `--mode compare` output puts "free" (V6.4's implicit assumption) next to the real
   broker scenarios. **The gap between those two columns is the money you didn't know you
   were paying.**
3. **Read max drawdown before you read anything else.** You are currently trading a system
   for which no drawdown estimate exists — that's the single most important sentence here.
   `config/risk-limits.yaml` gives you a 20% budget; if the simulator exceeds it, the sizing
   question is settled regardless of EV.
4. **Look at the rejection log** V6.5 keeps. If most rejections are "can't afford" and
   "concentration breach", your problem is account size, not strategy — a completely
   different problem with a different fix. (I'd note your own docstring at
   `momentum_pit_backtest.py:21-24` records buying 500 shares of 1888 at 11x correct size and
   300 BAC at 100x. I don't read that as weak discipline. I read it as: the correct answer
   was frequently "0 shares" or "1 share", which doesn't feel like trading. The account is
   too small for the strategy's tick size, and the discipline problem is a symptom.)
5. **Only then** spend money on point-in-time constituent data with delisted tickers
   (Norgate ~US$70/mo, Sharadar ~US$50-150/mo). `yfinance` cannot serve delisted names, so
   the universe problem cannot be fixed inside your current data stack. Do this *after* you
   know there's a surviving net-of-cost edge worth paying to verify.
6. **Fix the falsehoods in the files themselves**, because they're what you'll read at 7am
   six months from now: delete `momentum_pit_backtest.py:309`, delete or implement
   `RISK_PCT` and `COOLDOWN`, and reconcile the three different stop-width caps
   (15% / 12% / none, depending on which file you open).

---

## What I'd actually say about the design

The instincts here are good, and I don't want the finding to obscure that. Regime gating, an
explicit OOS discipline you wrote *before* seeing the answer, guardrails on stop width and
affordability, a written commitment not to fudge the pool, honest disclosure of survivorship
in the docstring, correct point-in-time momentum ranking, gap protection in Engine 2, and
exits that don't peek. That is a more disciplined build than most retail systems.

**What's broken is the measurement layer, not the idea** — and it's broken in a way that
systematically flatters. That's also the good news: measurement is fixable without touching
what you buy, which is exactly what V6.5 sets out to do. Do the ticker-attribution test
today. It's twenty minutes and it may save you the other five steps.
