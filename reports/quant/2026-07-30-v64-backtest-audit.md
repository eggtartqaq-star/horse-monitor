# V6.4 Dual Engine — Backtest Methodology Audit

**Author:** Tom, Backtesting Engineer (Dept 3 — Quantitative Research)
**Date:** 2026-07-30
**Subject:** Independent methodology audit of the Owner's V6.4 dual-engine swing system
**Artifacts audited:** `strategy/v6.4/{oos_validation.py, momentum_pit_backtest.py, dual_engine_v6_4_tiers.pine, daily_strong_signals.py, telegram_swing_bot.py}`

---

## 0. Scope, and what I could not do

I read all five files line by line. **I did not run any backtest** — I have no market data
access in this environment, and (see C-5) the committed copies of all four Python files do
not compile. Every conclusion below is derived from the code's logic, not from a rerun.

**Every number in this report that is not a code constant or a citation from a code comment
is labelled `[ILLUSTRATIVE]` and is an assumption used to size an effect, not a measured
result.** I have invented no performance figures. The only performance figures I quote are
the ones the Owner's own code comments claim:

| Claim | Source |
|---|---|
| Engine 2 OOS EV `+1.325%` (2025-26) and `+1.497%` (2018-21) | `momentum_pit_backtest.py:295` |
| Engine 1 EV rose `0.24% → 1.10%` from the V6.2 stop change | `dual_engine_v6_4_tiers.pine:60`, `telegram_swing_bot.py:233` |
| Engine 2 "OOS已驗證,主力"; Engine 1 "OOS偏弱,觀察為主" | `daily_strong_signals.py:145,155` |

---

## 1. VERDICT

# **UNPROVEN**

More precisely, a two-part verdict:

1. **As a gross statistical phenomenon: UNPROVEN.** The evidence presented cannot
   distinguish a real edge from the combination of (a) a survivor-selected universe,
   (b) zero transaction costs, (c) an unfundable number of simultaneous positions, and
   (d) a holdout that is not a holdout. Not one of these four is a matter of opinion;
   each is visible in the code. I am not saying the edge is absent. I am saying this
   evidence cannot tell you either way, and it has been presented as if it can.

2. **As a net-of-cost proposition at a HK$10,000 account: effectively REFUTED until
   proven otherwise.** This is the one calculation I can do without market data, and it
   is decisive. At the Owner's stated account size, the expected gross profit per trade
   is roughly **US$1.70–2.00**, and a realistic round-trip commission is **US$0.70–4.00**.
   In two of three realistic broker scenarios the entire claimed edge is smaller than the
   ticket cost. See C-2 for the arithmetic. **This alone should stop new capital going in
   until a cost model is built.**

The system is not obviously stupid. The design instincts are good — regime gating, an
explicit OOS discipline, guardrails, a written commitment not to fudge the pool. The
*measurement* is what is broken, and it is broken in a way that systematically flatters.

### Firm integrity checklist

| Check | Result | Where |
|---|---|---|
| No lookahead bias | **FAIL** | H-1 (signal-at-close/fill-at-close), C-1 (index-membership look-ahead), M-2 (Engine 1 reads past the IS/OOS boundary) |
| No survivorship bias | **FAIL** | C-1 |
| Point-in-time data | **PARTIAL** | Momentum *ranking* is genuinely PIT and correct. The *universe* is not. |
| Realistic transaction costs / slippage | **FAIL** | C-2 — zero cost modelling anywhere in the codebase (grep-confirmed) |
| Splits / dividends handled | **UNVERIFIABLE** | M-8 — `momentum_pit` is explicit; `oos_validation` relies on an unpinned yfinance default that has changed across versions |
| No holdout contamination | **FAIL** | C-4, M-2 |
| Reproducibility (my addition) | **FAIL** | C-5 |
| Portfolio-level realism (my addition) | **FAIL** | C-3 |

**Zero clean passes out of six on the firm's standard checklist.**

### The ugly numbers first — they do not exist

My mandate is to report max drawdown, drawdown duration, worst month and tail behaviour
before I report Sharpe. **I cannot, because the codebase never computes them.**

```
grep -rni "drawdown|sharpe|equity|sortino|cagr" strategy/v6.4/*.py
→ two Cantonese comments telling the reader to "remember to look at drawdown".
  Zero lines of code that compute one.
```

Neither script builds an equity curve. Neither computes a drawdown, a Sharpe, a Sortino, a
monthly return series, or an exposure profile. The closest thing to a risk statistic in the
entire system is `最差單筆` — worst *single trade* — which is not a portfolio risk measure
and is not the number that makes people stop trading.

**The Owner is trading real money on a system for which no drawdown estimate exists.**
That is the single most important sentence in this report, and it is a structural gap, not
a bug.

---

## 2. FINDINGS — severity ranked

### CRITICAL

---

#### C-1 — The universe is survivor-selected in *both* backtests, and the momentum design amplifies it rather than reducing it

**Where:** `momentum_pit_backtest.py::get_universe()` (L70-84) and `FALLBACK` (L58-69);
`oos_validation.py::TICKERS` (L31-40).

**What is wrong.** `get_universe()` scrapes the **current** S&P 500 constituent list from
Wikipedia and uses it as the candidate set for a backtest running `TEST_START = "2019-01-01"`
to `TEST_END = "2026-06-30"`. The Owner's question was: *is the point-in-time ranking
eliminating look-ahead in the ranking while the universe is still survivor-selected?*

**Answer: yes, exactly that. Confirmed.** The ranking is clean — `sub = df.loc[:today]`
then `sub["mom_126"].iloc[-1]` uses only data at or before `today`, and the 1-year warmup
(`DOWNLOAD_START = "2018-01-01"` vs `TEST_START = "2019-01-01"`) is correct design. Credit
where due. But a clean ranking over a dirty candidate set is a clean ranking over a dirty
candidate set.

**The file contradicts itself in the same file.** The docstring (L28-30) honestly discloses
"呢層仍有輕微生存者偏差" — *slight* survivorship bias. The final line printed to the console
(L309) says **"★ 鐵律:呢個係point-in-time,冇生存者偏差"** — *iron rule: this is
point-in-time, there is no survivorship bias.* The headline claim the Owner reads on screen
is false, and the file's own fine print says so. The disclosure is also wrong in degree: the
bias is not slight.

**Two distinct channels, and the smaller one is the famous one.**

*Channel (i) — deletion / survivorship proper.* Names that went bankrupt, collapsed, or were
removed from the index are absent. **For this specific design this channel is genuinely
small**, and the Owner deserves credit for it: a stock on its way out of the S&P 500 has
terrible 126-day momentum and would essentially never enter a top-50 momentum pool anyway.
The PIT momentum rank partially self-immunises here.

*Channel (ii) — index-inclusion look-ahead. This is the dominant channel and it is aligned
with the strategy like a key in a lock.* A company that entered the S&P 500 in 2023, 2024 or
2025 is **present in the candidate set during 2019-2022** in this backtest. The reason it
was later added is precisely that it delivered enormous returns in that window. So the
backtest holds, in its candidate set, a group of stocks that are *known ex post* to have had
spectacular forward returns — and then ranks them by trailing 6-month momentum, which is the
single best available proxy for "this is one of the stocks that went up". The selection
mechanism and the contamination point in the same direction. This is not survivorship bias
in the textbook sense; it is a look-ahead on index membership, and it is worse.

Names in the code's own `FALLBACK` list that joined the S&P 500 well after `TEST_START`
include TSLA, MRNA, ENPH, ABNB, UBER, CRWD, PLTR, COIN, DDOG. `[ILLUSTRATIVE — approximate
addition dates from memory; the Owner should verify against a constituent-history file, not
against my recollection.]`

**The `oos_validation.py` 38-ticker pool has the same disease, worse, and it is hand-typed.**
`TICKERS` at L31-40 is not an index list at all — it is a manually curated roster of the
2026 mega-cap winners, chosen in 2026, and then backtested over 2022-2026. It contains
**MSTR, COIN, PLTR, NVDA, TSLA, SHOP, UBER**. MSTR in particular is a leveraged bitcoin
proxy that ran roughly 20x during the test window. Selecting MSTR in 2026 and then
backtesting a trend-following system on it over 2022-2026 is the most hindsight-loaded
single ticker choice available in the US market. The same 38-name list is also the *live*
trading pool (`telegram_swing_bot.py::POOL`, L51-56) — so the live system is itself a
standing bet that the 2022-2026 winners keep winning.

**Why it matters in money terms.** `[ILLUSTRATIVE]` The reported statistic is an *unweighted
mean of per-trade percentage returns*. That statistic is extremely sensitive to a handful of
outliers. If six MSTR/COIN/PLTR trades in a 200-trade sample returned +60% each, they
contribute `6 × 60 / 200 = +1.8%` to the mean EV — **more than the entire claimed edge of
+1.325%.** The edge could be, in its entirety, four tickers that the Owner picked in 2026
because he already knew they had gone up.

**Direction and rough magnitude of the bias: upward, and larger than the claimed edge.**
Standard estimates for pure delisting survivorship in a broad US large-cap universe run
0.5-2.0%/yr `[ILLUSTRATIVE — literature range]`. But that number does not apply here,
because channel (ii) dominates and because a top-50 concentration multiplies it. I will not
put a false-precision figure on it. What I will say is this: **the bias is of the same order
of magnitude as, or larger than, the entire claimed edge, and it points the same way.** That
is enough to make the result uninterpretable without fixing it.

**A silent amplifier.** If the Wikipedia scrape fails — and `pd.read_html` against Wikipedia
fails routinely on user-agent and parser-backend issues — the bare `except Exception` at
L80-84 silently falls back to `FALLBACK`, the hand-picked winners list. The output CSVs
record no indication of which universe was used. **The Owner may already have run this and
received the hand-picked-winners version without knowing.**

**Concrete fix.**
1. *Today, free, 10 minutes, decisive:* add a `ticker` field to the `oos_validation.py`
   trade records (currently `{"ret", "days"}` only, L214 and L264 — **there is no ticker and
   no date, so per-name attribution is impossible from the saved CSVs**), then print EV by
   ticker. Then rerun with MSTR, COIN, PLTR and NVDA removed. **If the edge collapses, you
   are done — there is no system, there is a bet on four stocks.** This is the single
   cheapest test in this report and it should be run before anything else in C-1 is
   attempted.
2. *Properly:* replace the universe with a real point-in-time constituent history that
   includes delisted tickers — Norgate Data (~US$70/mo), Sharadar SEP+TICKERS via Nasdaq
   Data Link (~US$50-150/mo), CRSP, or Polygon's delisted coverage. `yfinance` cannot serve
   delisted tickers reliably, so this cannot be fixed within the current data stack.
3. Make the fallback **fatal**, not silent: if the universe cannot be sourced, abort.
4. Write the universe, its source, and the run timestamp into the output CSV.
5. Delete the false line at L309.

---

#### C-2 — Zero transaction cost modelling, at an account size where fixed ticket costs exceed the entire claimed edge

**Where:** everywhere. Grep for `slip|commission|fee|spread|滑價|手續費|佣金` across all
five files returns **nothing**. Entries are at `Close` (`oos_validation.py` L236, L197;
`momentum_pit_backtest.py` L263). Exits are at the exact stop or exact target.

**What is wrong.** No commission, no bid-ask spread, no slippage, no market impact, no FX
conversion cost, no borrow. The reported EV is a gross, frictionless number presented as a
result.

**Why it matters in money terms — this is the calculation that decides it.**

Account: HK$10,000 at `USD_HKD = 7.8` → **US$1,282**. `RISK_PCT = 1.0` → **US$12.82 risk
per trade**.

Position notional = risk ÷ stop-distance:

| Engine | Typical stop width | Notional per trade |
|---|---|---|
| Engine 2 (3×ATR, capped 12%) | ~10% `[ILLUSTRATIVE]` | **US$128** |
| Engine 1 (min of 10d-low, 2×ATR) | ~7% `[ILLUSTRATIVE]` | **US$183** |

Round-trip friction, three realistic broker scenarios `[ILLUSTRATIVE — commission schedules
from memory; the Owner should substitute his actual broker's rates]`:

| Scenario | Round-trip ticket | as % of US$128 | as % of US$183 |
|---|---|---|---|
| (a) IBKR tiered, US$0.35 min/side | US$0.70 | 0.55% | 0.38% |
| (b) IBKR fixed, US$1.00 min/side | US$2.00 | 1.56% | 1.09% |
| (c) Futu / Tiger (comm + platform, ~US$2/side) | US$4.00 | 3.13% | 2.19% |

Add spread and slippage. Large-cap US spreads are 2-5bp, but Engine 2 enters **on a 20-day
breakout day** — a wide-range, one-directional bar — and both engines decide on the close.
Realistic all-in slippage 5-15bp per side → **0.15-0.35% round trip** `[ILLUSTRATIVE]`.
Add HKD→USD conversion (~US$2 flat at IBKR, or ~0.5% spread at a retail HK broker).

Applying this to the claimed **Engine 2 OOS EV of +1.325%** (`momentum_pit_backtest.py:295`):

| Scenario | Total friction | **Net EV** | Edge destroyed |
|---|---|---|---|
| (a) best case | 0.80% | **+0.53%** | 60% |
| (b) mid case | 1.81% | **−0.49%** | 100%+ |
| (c) typical HK retail | 3.38% | **−2.06%** | 100%+ |

**In dollars, which is the version that should end the argument:** a +1.325% EV on a US$128
position is an expected gross profit of **US$1.70 per trade**. A US$2.00 round-trip
commission is larger than the entire expected profit of the trade. The Owner is running a
strategy whose per-trade edge is smaller than a single ticket.

The same holds for Engine 1: +1.10% on US$183 = **US$2.01 gross per trade.**

**This is not a marginal adjustment. At this account size the strategy is a
commission-generation machine unless executed at scenario (a) rates, and even then it loses
60% of its edge.**

**Concrete fix.**
1. Add an explicit cost function to both backtests, applied to every entry and exit:
   `cost = max(min_commission, rate × notional) + 0.5 × spread_bp × notional + slippage_bp × notional`.
2. Model stop fills pessimistically: a stop-market order fills **at or below** the stop,
   never above. Current code fills at exactly `stop` (Engine 1) — see H-2.
3. Report net EV only. Per the firm mandate, gross results are not reportable.
4. Re-derive the minimum viable account size: solve for the notional at which ticket cost
   falls below, say, 20% of gross EV. At scenario (b) that is roughly
   `US$2.00 / (0.20 × 0.01325) = ` **~US$755 per position**, implying — at 10% stop widths
   and 1% risk — an account of roughly **US$7,500 minimum**, ~6x the current account
   `[ILLUSTRATIVE]`. This number, not the EV, is the one that determines whether the system
   is tradeable by this Owner today.

---

#### C-3 — No portfolio simulation, unlimited concurrency, and `RISK_PCT` is declared but never used — the "1% rule" is not actually in the backtest

**Where:** `momentum_pit_backtest.py::main()`, the `open_positions` dict (L187, L218-270);
`RISK_PCT` declared at L48.

**What is wrong.** `RISK_PCT = 1.0` appears **exactly once in the file: on the line where it
is declared.** It is never referenced in the trade loop. Grep-confirmed. Yet the docstring
(L25-26) states:

> 「呢個回測用嘅係『每筆固定風險%』,已經自動遵守1%規則 —— 即係話,個回測結果本身已經假設咗你會守規。」
> *(This backtest uses a fixed risk % per trade, so it automatically obeys the 1% rule — the
> backtest result already assumes you will follow the rules.)*

**This is factually false.** There is no position sizing in the backtest at all. No share
count, no cash ledger, no account equity, no capital check. The code appends raw percentage
returns and averages them. This is the same class of defect as C-6's dead `COOLDOWN`: a
constant declared to make the file look compliant, doing nothing.

**How many concurrent positions does the code actually permit?** `open_positions` is keyed
by ticker with `if tk in open_positions: continue`, so the hard cap is **one per pool member
= 50 simultaneous positions**. There is no other limit.

**What total portfolio risk does that imply?**

| Measure | Value |
|---|---|
| Max concurrent positions | **50** |
| Total portfolio risk at 1% each | **50% of account at risk simultaneously** |
| Notional at 50 × US$128 | **US$6,400 on a US$1,282 account = 5.0x leverage** |
| Notional at Engine-1-style 7% stops | **US$9,150 = 7.1x leverage** |

Against `config/risk-limits.yaml`, this breaches:

- `leverage: none` — *hard rule*. Breached 5-7x over.
- `max_single_position: 0.10` — a US$128 position is **10.0%** of a US$1,282 account; a
  US$183 position is **14.3%**. Breached on essentially every trade (see H-4).
- `max_correlated_cluster: 0.40` — the pool is the top 50 by 6-month momentum. These names
  are one factor. In a drawdown their pairwise correlation approaches 0.8+. Effective
  cluster exposure is ~100%.
- `max_drawdown: 0.20` — cannot even be assessed, because no drawdown is computed.

**John (CRO) would veto this on the config alone.** I am flagging it for him.

**And the diversification is illusory.** The entry condition is `ADX≥25 and DI+>DI− and new
20-day high and trend_score≥0.65`, applied to names already selected for top-decile 6-month
momentum, gated on `SPY > MA200`. Every one of those conditions is a market-beta condition.
On a breadth-thrust day — the first days off a correction low, or an index breakout — it is
entirely plausible that **10-30 of the 50 pool members trigger on the same day**
`[ILLUSTRATIVE]`. The backtest happily opens all of them. The account can fund about seven.

**Does the per-trade EV statistic mean anything as a portfolio result? No.**

It answers exactly one question: *"if I had infinite capital and could take every signal at
equal risk, what is the arithmetic mean of the return distribution?"* It tells you nothing
about drawdown, drawdown duration, sequence risk, correlation of simultaneous holdings,
time-in-market, capital efficiency, compounding, or return on the account. It cannot be
annualised. It cannot be compared to buy-and-hold. It cannot be used to size anything. It is
the wrong statistic, and it is the *only* statistic the system produces.

Worse: capital rationing does not remove trades at random. Signals cluster at the start of
market up-legs — which is when the best trend trades begin. **A capital-constrained live
account systematically misses the best entries**, so the live distribution is drawn from a
worse subpopulation than the backtest's. Another one-directional gap, and it favours the
backtest.

**Concrete fix.** Replace both scripts with a single event-driven portfolio simulator: cash
ledger, integer share counts, explicit `MAX_CONCURRENT` (I would start at 5), per-ticket
costs, and a daily mark-to-market equity curve. Output max drawdown, drawdown duration,
worst month, monthly return series, exposure %, Sharpe, Sortino, CAGR. See **U-1**.

---

#### C-4 — The holdout is not a holdout, and the "graduation test" passes a worthless strategy about half the time

**Where:** `oos_validation.py` — the whole file, especially `verdict()` (L294-315) and
`DATA_PERIOD = "4y"` (L42).

**What is wrong — three compounding problems.**

**(a) The version number is a count of researcher degrees of freedom.** The system is called
**V6.4**. Six major versions and at least four minor revisions means, conservatively,
**≥20 iterations of the ruleset**, every one of them evaluated on the same 4-year window of
the same 38 stocks. The code even reveals the search structure: `oos_validation.py:48`
comments the 2×ATR stop as **"C臂"** — *arm C* — which means arms A and B existed and C was
chosen. The Pine and bot comments confirm the outcome of that selection: EV `0.24% → 1.10%`.

Therefore the "out-of-sample" 18 months at the end of the window **was seen, repeatedly,
during the V1→V6.4 development process.** It is not a holdout. It is training data that the
final model happens not to have been fitted on in the last iteration. The file's closing
line — "呢個測試冇任何參數可以調 —— 規則鎖死同V6.4一致" (*this test has no adjustable
parameters, the rules are locked to V6.4*) — is true of the *script* and false of the
*process*. The parameters were tuned; they were just tuned before this file was written.

**(b) The holdout slides every time you run it.** `DATA_PERIOD = "4y"` is relative to the run
date, and `cutoff = spy.index[-1] - DateOffset(months=18)`. Run the script in August and the
IS/OOS boundary moves, the OOS window slides, and the answer changes. The output CSVs record
no run date. And we know from `momentum_pit_backtest.py:295` — which cites Engine 2 OOS
figures for **both** "2025-26" **and** "2018-21" — that the window has already been changed
between runs, directly contradicting the "no adjustable parameters" claim. **Every rerun on
a moving window is another trial, and no one is counting them.**

**(c) The pass criterion is not a statistical test.** `verdict()` passes if
`oos_ev > 0 and oos_ev >= is_ev * 0.5`. There is no null hypothesis, no confidence interval,
no standard error, no correction for the number of variants tried, and no minimum sample.
The code *prints a warning* when `n < 30` (L314) and then **ignores it and issues the verdict
anyway.**

**Quantifying the false-pass rate** `[ILLUSTRATIVE — assumes per-trade σ = 6%, typical for a
10-60 day equity swing trade with 6-12% stops, and n_oos = 40]`:

SE of the OOS mean = `6% / √40 = 0.95%`.

Under the null that the true edge is **zero**:
- P(the test reports 健康 / "healthy", i.e. `oos_ev ≥ 0.5 × 1.325% = 0.66%`) = P(Z ≥ 0.70) ≈ **24%**
- P(the test reports 警戒 / "exists but fragile", i.e. `oos_ev > 0`) = **50%**

The 警戒 branch's own wording is *"優勢存在但脆弱"* — **"the edge exists but is fragile."**
So:

> **Given a strategy with literally zero edge, this graduation test tells the Owner an edge
> exists roughly 50% of the time, and awards it the top grade roughly 25% of the time.**

That is a coin flip wearing a lab coat. And that is *before* correcting for the ~20 variants
that were tried.

**Deflated Sharpe check.** The expected maximum Sharpe from `N` independent zero-edge trials
is approximately `σ_SR × √(2 ln N)`. With `N = 20` trials and `σ_SR ≈ 0.4` (dispersion of
Sharpe estimates on a ~4-year sample) `[ILLUSTRATIVE]`:

`0.4 × √(2 × ln 20) = 0.4 × 2.45 = ` **0.98**

A backtest Sharpe near 1.0, selected as the best of ~20 variants, is **exactly what pure
noise produces.** You cannot distinguish V6.4 from the luckiest of twenty coin flips using
this evidence.

**Minimum Track Record Length.** To reject "true Sharpe ≤ 0" at 95% confidence for a
strategy whose true Sharpe is 0.5, MinTRL ≈ `(1.645 / 0.5)² ≈ 10.8 years` — before any
skew/kurtosis penalty and before any multiple-testing deflation. **A 4-year window (of which
~3.2 years are tradeable — see M-3) is not remotely enough**, and no amount of clever
splitting of insufficient data creates sufficient data.

**Concrete fix.** See **U-3, U-4, U-5**. Minimum viable version: maintain a `trials.csv`
logging every variant ever evaluated (V1→V6.4, arms A/B/C, every window change), compute the
Deflated Sharpe Ratio with the honest `N`, and replace `verdict()` with a bootstrap
confidence interval on EV plus an explicit statement of statistical power. If the CI crosses
zero, the verdict is "no conclusion", not "fragile edge".

---

#### C-5 — Nothing in this repository is reproducible

**Where:** all four Python files; plus a missing module.

**What is wrong.**

1. **All four `.py` files fail to compile.** Verified:
   ```
   daily_strong_signals.py     SyntaxError line 40   (unterminated string literal)
   momentum_pit_backtest.py    SyntaxError line 73   (unterminated string literal)
   oos_validation.py           SyntaxError line 304  (unterminated string literal)
   telegram_swing_bot.py       SyntaxError line 79   (unterminated string literal)
   ```
   The files are hard-wrapped at ~78-100 characters with content lost mid-expression
   (e.g. `oos_validation.py:64` ends `..., window=14` with an unbalanced paren) and emoji
   stripped, leaving broken literals. **This is most likely a copy/paste transcription
   artifact rather than the Owner's working code** — but the consequence stands: the
   artifact under audit is not the artifact that produced the numbers, and I could not have
   reproduced them even with data access.

2. **The core live engine module is absent.** `daily_strong_signals.py:33` imports
   `calc_indicators, classify, mr_score, mr_plan, trend_score, trend_plan,
   check_guardrails, position_plan, get_days_to_earnings` from **`dual_engine_v6_4.py`**,
   which is not in this repository. The single most important file — the one that defines
   what the Owner actually trades — was not submitted for audit. Everything I say about
   live-vs-backtest divergence below is inferred from the duplicated copies inside
   `telegram_swing_bot.py`.

3. **No dependency pinning.** No `requirements.txt`. Results depend on the installed
   `yfinance` and `ta` versions — see M-8, where this changes whether prices are
   split/dividend-adjusted at all.

4. **No run metadata.** Output CSVs record no run date, no universe, no library versions, no
   parameter set. Combined with the sliding `4y` window (C-4b), **two runs of the same
   script produce different answers with no way to tell them apart afterwards.**

5. **Silent failure modes.** `momentum_pit_backtest.py` contains 5 bare `except Exception`
   blocks; `oos_validation.py`'s main loop swallows per-ticker failures (L348-350) and never
   reports how many tickers actually contributed trades. In `oos_validation.py:340`,
   `bull = spy_bull_raw.reindex(df.index, method="ffill").fillna(False)` — if a ticker's
   index timezone does not match SPY's, the reindex yields NaN → `False` → **that ticker
   silently contributes zero trades and no warning is printed.** The sample can quietly
   shrink from 38 names to a handful.

**Why it matters in money terms.** An unreproducible backtest cannot be audited, cannot be
debugged after a live loss, and cannot be compared against live results for the
attribution work Dept 3 is supposed to do. It also means the Owner cannot tell whether last
month's "+1.325%" and this month's rerun differ because of new data or because of a
different universe fallback.

**Concrete fix.** Commit runnable source; commit `dual_engine_v6_4.py`; add
`requirements.txt` with pinned versions; write a JSON run-manifest (timestamp, git SHA,
universe, parameters, library versions, ticker count contributing) alongside every output
CSV; make every `except` either log loudly or abort.

---

### HIGH

---

#### H-1 — Signal computed from the close, filled at the same close: a one-bar look-ahead on every single trade

**Where:** `oos_validation.py:197` (`close = row["Close"]`), `oos_validation.py:236`
(`entry = row["Close"]`), `momentum_pit_backtest.py:263` (`entry = row["Close"]`).

**What is wrong.** Every entry decision uses information that is only known *at* the close —
`Close`, `RSI14`, `RSI2`, `ADX`, `ATR`, `vol_ratio` (a 5-day average requiring the full
day's volume), `OBV_Div` — and is then filled **at that same close.** In reality the close
is not known until it prints, and by then you cannot trade at it. A market-on-close order
must be submitted before the MOC cutoff (~15:50 ET), at which point the closing price, the
day's ADX, and the day's volume ratio are all still unknown.

To the code's credit, **exits are clean**: `simulate_mr` starts at `j = i + 1` and Engine 2's
loop starts at `d = 1`, so there is no same-bar exit look-ahead. The bias is confined to the
entry, but it is on 100% of trades.

**Why it matters in money terms.** `[ILLUSTRATIVE]` For Engine 2 the entry bar is by
construction a **20-day breakout day** — a strong, one-directional bar that typically closes
near its high. Assuming the decision price at 15:45 is 10-30bp worse than the print, and
that this is adverse on breakout days more often than not, the drag is **0.10-0.30% per
trade** — on top of C-2's costs, and **another 8-23% of the claimed +1.325% EV.**

**Concrete fix.** Either (a) enter at the **next bar's open**, which is honest and
conservative, or (b) evaluate the signal on bar `i` and fill at bar `i`'s close with an
explicit MOC-slippage penalty. Option (a) is the standard and I recommend it; it will reduce
the reported EV and that reduction is real.

---

#### H-2 — Engine 1 has no gap-through-stop modelling; Engine 2 does. The mean-reversion loss tail is fictional.

**Where:** `oos_validation.py::simulate_mr()` L180-181:
```python
if r["Low"] <= stop:
    return (stop - entry) / entry * 100, d
```

**What is wrong.** If the day's low breaches the stop, the trade exits at **exactly the
stop** — regardless of where the stock opened. If a stock gaps from $100 to $84 on an
earnings miss and the stop was $94, this code books a **−6% loss.** The real loss is −16%.

Engine 2 gets this right (`oos_validation.py:249-252` and `momentum_pit_backtest.py:227`:
`if Open < trail: exit_price = Open`). Engine 1 does not. **The two engines are simulated
with different levels of realism, and the less realistic one is the one that buys falling
stocks.**

This compounds with a second omission: **the backtests contain no earnings filter**, while
the live system does (`telegram_swing_bot.py:439`: `if 0 <= days_er <= 5: 唔入`;
`daily_strong_signals.py:61`: `abs(days_er) > 5` required for PREMIUM). So the backtest
holds mean-reversion positions straight through earnings reports — the single largest source
of overnight gaps — **and then assumes exact stop fills on those gaps.** Two optimistic
assumptions stacked on the exact scenario where they are least true.

**Why it matters in money terms.** `[ILLUSTRATIVE]` If 5% of Engine 1 trades gap through the
stop by an average of 6 additional percentage points, the EV is overstated by
`0.05 × 6 = 0.30%` — **27% of the claimed +1.10% Engine 1 EV**, and it lands entirely in the
left tail, which is where the account-destroying outcomes live. The reported `最差單筆`
(worst single trade) is therefore also fictional — it is bounded by the stop distance by
construction, which is precisely the reassurance the Owner should not be given.

**Concrete fix.** One line: mirror Engine 2's logic —
`exit_price = min(stop, r["Open"]) if pd.notna(r["Open"]) else stop`. Then add the earnings
filter to the backtest so it tests the ruleset that is actually traded, and add explicit
stop slippage (a stop-market order fills at or below the stop, never above).

---

#### H-3 — The backtested trade population is not the live trade population, and for Engine 1 it is the wrong tier entirely

**Where:** guardrails exist in `dual_engine_v6_4_tiers.pine` (L73, L84), `telegram_swing_bot.py`
(L49, L156, L176-184, L346, L439) and `daily_strong_signals.py` (L109, L127) — and appear in
**neither backtest.**

**What is wrong.** Live signals must pass filters that the backtest never applies:

| Guardrail | Live | `oos_validation.py` | `momentum_pit_backtest.py` |
|---|---|---|---|
| Stop width cap | 15% (Pine, MR bot) / 12% (trend) | **none for Engine 1**; 12% for Engine 2 | 12% |
| Affordability (`shares ≥ 1`) | blocks the signal | **absent** | **absent** |
| Speculative-stock flag (126d hi/lo ≥ 2x) | warns/blocks | **absent** | **absent** |
| Earnings within 5 days | blocks | **absent** | **absent** |
| Pool membership (38 names) | blocks | n/a | n/a |
| Tier filter (STRONG/PREMIUM only) | Engine 1 trades **only** STRONG/PREMIUM | **absent** | n/a |

**The tier mismatch is the serious one.** `daily_strong_signals.py::classify_mr_tier` (L46-64)
and `telegram_swing_bot.py::classify_tier` (L281-307) both require, for Engine 1,
`score ≥ 0.55 AND R ≥ 2 AND RSI2 < 10 AND R ≥ 3.0` to reach STRONG. The scanner explicitly
prints "只列 強 同 頂級" and only surfaces STRONG/PREMIUM. Meanwhile
`oos_validation.py::run_engine1` (L196, L209) tests **`score ≥ 0.55 AND R ≥ 2`** — that is
the **BASIC** tier, the one the Owner is instructed *not* to trade.

> **The Engine 1 "OOS偏弱" conclusion — which drives the Owner's decision to demote Engine 1
> to observation-only — was measured on a tier he does not trade. It is not a test of the
> live Engine 1 rule at all.** The live rule (RSI2<10 plus R≥3) may be better or worse; the
> evidence is silent, and the Owner has been treating it as informative.

**The affordability guardrail is the most distorting omission.** Live, `position_plan`
(`telegram_swing_bot.py:167-175`) computes `shares = int(12.82 // per_share_risk)` and the
signal is **blocked if `shares < 1`**. For a US$180 stock with a 3×ATR stop of ~9%
(US$16.20/share of risk), `floor(12.82 / 16.20) = 0 shares` → **blocked live, taken in the
backtest.** The names this blocks are systematically the high-priced, high-ATR ones — which
in a momentum system are exactly the leaders. **The backtest trades a universe of signals
the Owner physically cannot execute, and they are disproportionately the good ones.**

**Concrete fix.** Import the live guardrail functions into the backtest rather than
reimplementing the rules. Backtest the STRONG/PREMIUM tier for Engine 1, since that is what
is traded. If the resulting sample is too small to conclude anything, **that is the finding**,
and it should be reported as such rather than substituted with a BASIC-tier proxy.

---

#### H-4 — At HK$10,000, the 1% rule and the 10% concentration limit are mathematically incompatible, and share quantisation makes real risk vary by ±50%

**Where:** `telegram_swing_bot.py::position_plan()` L167-175;
`dual_engine_v6_4_tiers.pine` L79-84; vs `config/risk-limits.yaml`.

**What is wrong.** With US$1,282 of equity and US$12.82 of risk per trade:

| Stock price | Stop width | Risk/share | Shares (floor) | Notional | **% of account** |
|---|---|---|---|---|---|
| $30 | 8% | $2.40 | 5 | $150 | **11.7%** |
| $50 | 7% | $3.50 | 3 | $150 | **11.7%** |
| $100 | 7% | $7.00 | 1 | $100 | **7.8%** |
| $180 | 9% | $16.20 | **0** | — | **blocked** |

Two structural consequences:

1. **The 1% risk rule produces 8-15% position sizes**, breaching
   `config/risk-limits.yaml: max_single_position: 0.10` on most trades. The two rules cannot
   both be satisfied at this account size. The Owner is operating a rule set that is
   internally inconsistent, and no one has told him.

2. **Integer-share quantisation.** When the "correct" size is 1.83 shares and you buy 1, your
   actual risk is **55% of 1%**. When it is 2.4 and you buy 3, it is **125%**. Realised risk
   per trade varies roughly **±50%** around the intended figure. The backtest assumes exact
   fractional 1% risk (in `oos_validation.py`) or no sizing at all (in
   `momentum_pit_backtest.py`, C-3). The realised return distribution is therefore a
   randomly-reweighted version of the tested one.

There is a poignant confirmation of the problem in the Owner's own code. The
`momentum_pit_backtest.py` docstring (L21-24) records that on 7/13 he bought 500 shares of
1888 at **11x** the correct size and on 7/18 bought 300 BAC at **100x**. I would suggest the
cause is not weak discipline — **it is that the correct answer was frequently "0 shares" or
"1 share", which does not feel like trading.** The account is too small for the strategy's
tick size, and the discipline problem is a symptom of that, not the disease.

**Concrete fix.** Either (a) raise the account to the ~US$7,500 implied by C-2, or (b) use a
broker with fractional shares (which fixes quantisation and affordability at once, though
not commissions), or (c) accept a wider risk-per-trade band and a hard concentration cap and
**re-run the backtest with integer-share sizing on the actual account equity** so that the
tested distribution is the tradeable one. Do not proceed on the current inconsistent pair of
rules.

---

#### H-5 — The chart the Owner trades from disagrees with the engine that was backtested (Owner's item 4 — CONFIRMED, with a caveat)

**Where:**
- Python (backtested, and used by both live scanners via `mr_plan`):
  `oos_validation.py:209-211`, `telegram_swing_bot.py:251-255`
  ```python
  valid  = [(p, r) for p, r in targets if r >= MIN_R]
  target = min(valid, key=lambda x: x[0])[0]        # NEAREST valid target
  ```
- Pine (what the Owner looks at): `dual_engine_v6_4_tiers.pine:66`
  ```
  target = high60 > close ? high60 : (ma50 > close ? ma50 : close)   // PREFERS the 60-day high
  ```

**Confirmed — with an important scoping caveat that makes the finding sharper, not weaker.**

The two implementations agree whenever only one target is valid. They **disagree precisely
when both MA50 and the 60-day high sit above the close and both clear the 2R hurdle** — i.e.
on the **deeper-pullback subset**, where price has fallen below MA50. `mr_score`'s bands
(`price_vs_ma20` between −10 and −5 scores 0.8; below −10 scores 0.4) mean this subset is a
real and material fraction of Engine 1 signals, and it is systematically **the higher-risk,
wider-stop trades.** On shallow pullbacks (price still above MA50) the two agree.

**Consequences on the disagreeing subset:**

1. **Tier inflation.** `rVal` on the chart is computed from the *farther* target, so it is
   systematically higher than the Python `r`. `strong` requires `rVal ≥ 3.0`
   (`dual_engine_v6_4_tiers.pine:91`). **The chart therefore promotes to 強/頂級 setups that
   the scanner classifies as 普通.** Same ticker, same day, two answers, from two tools the
   Owner uses side by side. This is directly testable and should be tested today.

2. **Realised R falls.** A farther target against a fixed **10-day** maximum hold
   (`MR_MAX_HOLD = 10`) is far less likely to be touched. Trades that the backtest booked as
   "+2R target hit" become "10-day timeout, exit at whatever the close is". Win rate falls
   sharply; average win rises; **the EV sign is not determinable a priori and the variance
   rises materially.**

3. **The critical point: the Pine variant has never been backtested.** The +1.10% figure
   printed in the comment on line 60 of that very file was produced by the *nearest-target*
   rule. The file displays a different rule and cites the other rule's performance.

**Why it matters in money terms.** The Owner is taking position-sizing and go/no-go decisions
from a chart whose displayed R-multiple, take-profit level, and signal tier can all differ
from the validated engine, on the subset of trades that carry the most risk. **Any live
result from chart-driven trades cannot be attributed to the backtested system.**

**Concrete fix.** Make the Pine target identical to the Python:
```
tgtMa50  = ma50   > close and (ma50   - close)/riskA >= MIN_R ? ma50   : na
tgtHigh60= high60 > close and (high60 - close)/riskA >= MIN_R ? high60 : na
target   = not na(tgtMa50) and not na(tgtHigh60) ? math.min(tgtMa50, tgtHigh60)
           : not na(tgtMa50) ? tgtMa50 : not na(tgtHigh60) ? tgtHigh60 : close
```
Then add a golden-file regression test (**U-6**) asserting Pine and Python produce identical
tier/stop/target on N historical bars. Until they do, **trust the scanner, not the chart.**

---

#### H-6 — `COOLDOWN` is dead code, and it is one of at least five divergences from the rules the file claims to have "locked" (Owner's item 3 — CONFIRMED)

**Where:** `oos_validation.py:49`.

**Confirmed.** `grep -rn "COOLDOWN" strategy/v6.4/` returns **exactly one line: the
declaration.** It is never referenced. The file's closing claim (L370-371) —
*"呢個測試冇任何參數可以調 —— 規則鎖死同V6.4一致"* (*this test has no adjustable parameters,
the rules are locked identical to V6.4*) — is **false as written.**

**Is it a genuine divergence?** That depends on whether live V6.4 enforces a 10-day cooldown.
I cannot verify, because `dual_engine_v6_4.py` is not in the repository (C-5). What the OOS
code *does* enforce is a weaker constraint: `i += max(res[1], 1)` then `i += 1` (L215-216)
prevents re-entry in the same ticker while a trade is open, but permits a new entry the very
next bar after an exit. If live V6.4 blocks re-entry for 10 bars, **the backtest takes a
strictly larger and differently-composed set of trades than the live system** — most
obviously, it can immediately re-enter a name that just stopped out, which is exactly the
sequence a cooldown exists to prevent, and which in a mean-reversion engine is exactly the
falling-knife pattern.

**What else diverges** (each is independently checkable):

1. **Three different stop-width caps.** `oos_validation.py:239` uses 12% for Engine 2 and
   **no cap at all** for Engine 1; `dual_engine_v6_4_tiers.pine:73` uses 15%;
   `telegram_swing_bot.py` uses 15% for Engine 1 (L49, L398) and 12% for Engine 2 (L156).
   Engine 1 trades with 20%+ stops are counted in the backtest and blocked live.
2. **`RISK_PCT` is dead in `momentum_pit_backtest.py`** — declared, never used (C-3).
3. **Every guardrail is missing from both backtests** (H-3).
4. **Engine 1 is backtested at the wrong tier** (H-3).
5. **The Pine file has no Engine 2 at all.** Its header says *"Swing Trade V6.2 三級訊號指標
   （均值回歸引擎）"* — mean-reversion engine only. Yet `daily_strong_signals.py:145` calls
   Engine 2 **"主力"** (the main engine). **The Owner's primary engine has no chart
   representation whatsoever**, so every chart-driven decision he makes is an Engine 1
   decision, taken from the engine his own system labels as OOS-weak and observation-only.
   That is an operational finding as much as a methodological one.
6. **Version drift inside one file:** header says V6.2, `indicator()` name says V6.4
   (`dual_engine_v6_4_tiers.pine` L2 vs L17).

**Concrete fix.** One shared rules module, imported by every consumer. Delete or implement
`COOLDOWN` and `RISK_PCT` — a declared-but-unused constant in a file that advertises "locked
rules" is worse than no constant, because it manufactures false confidence. Reconcile the
three stop-width caps to one number. Build the Engine 2 Pine indicator or stop calling
Engine 2 the main engine.

---

#### H-7 — Trades are treated as independent samples when they are heavily clustered in time; the effective sample size is a fraction of the reported one

**Where:** `oos_validation.py::stats()` L272-285; `momentum_pit_backtest.py` L275-296.

**What is wrong.** Both scripts pool trades across 38-50 tickers into one flat list and take
an unweighted mean. But entries are gated by `SPY > MA200`, by market-wide ADX regime, and
(in the momentum version) by a top-50 momentum pool — all market-wide conditions. **Trades
therefore arrive in bursts, and trades in the same burst share most of their return
variance.**

The standard error of a clustered mean is understated by approximately
`√(1 + (m − 1)ρ)`, where `m` is the average cluster size and `ρ` the intra-cluster
correlation. `[ILLUSTRATIVE]` With `m = 5` concurrent and `ρ = 0.6`: **1.84x**. With
`m = 10`, `ρ = 0.7`: **2.70x**.

> **A "200-trade backtest" has an effective sample size of roughly 27-59.
> A "40-trade OOS" has an effective sample size of roughly 5-12.**

At `n_eff ≈ 8` no statement about EV is supportable in either direction. The code prints
`筆數: 200` and the reader reasonably infers statistical weight that is not there. Note this
compounds directly with C-4: the false-pass rate computed there used `n = 40`; with
`n_eff = 10` it is worse still.

**Concrete fix.** Report EV with a **stationary block bootstrap** confidence interval,
resampling calendar blocks (e.g. 20-day blocks) rather than individual trades, so that
clustering is preserved. Report the CI, never a bare point estimate. Also report the
concurrency histogram — it is the diagnostic that makes this problem visible.

---

### MEDIUM

---

#### M-1 — Engine 2 boundary truncation drops winners: it biases the OOS EV DOWNWARD, and penalises the 18-month OOS window ~1.15x more than the in-sample (Owner's item 2 — CONFIRMED, direction stated confidently)

**Where:** `oos_validation.py::run_engine2()` L244-246:
```python
j = i + d
if j >= end_idx:
    break                    # OOS邊界:未平倉交易棄掉,唔跨段
```
`exit_ret` remains `None`, so the guard at L263 (`if exit_ret is not None`) never fires and
**the trade is silently discarded.**

**Which trades are disproportionately open at any boundary? Winners. Confidently.**

In a trailing-stop trend system the holding period and the return are mechanically coupled:
the 3×ATR trail only ratchets upward, so a losing trade is stopped out within days while a
winning trade survives until the 60-day cap. The distribution of `days` is right-skewed and
positively correlated with `ret`.

Now apply **length-biased sampling**: a trade of duration `D` is open at a randomly chosen
boundary with probability proportional to `D`. Long trades are therefore over-represented
among the discarded set — and long trades are winners.

`[ILLUSTRATIVE — assuming losers average 10 days, winners 45 days, OOS window ≈ 375 bars]`:
- P(a loser is truncated) ≈ 10/375 = **2.7%**
- P(a winner is truncated) ≈ 45/375 = **12.0%** — a **4.5x** differential
- If the base win rate is 40%, the discarded set is roughly **80% winners.**

**Direction of the bias on OOS EV: DOWNWARD. Stated confidently.** The reported Engine 2 OOS
EV is *lower* than the true (gross) figure.

`[ILLUSTRATIVE]` If 8% of trades are dropped and 80% of them are winners, with
`avg_win = +12%`, `avg_loss = −6%`, `EV = +1.3%`:
`0.08 × (0.8 × 12 + 0.2 × (−6) − 1.3) = 0.08 × 7.1 = ` **+0.57% removed from the reported EV.**

**Is the OOS window penalised more than the in-sample? Yes, but modestly — and I want to be
precise rather than dramatic.** `DATA_PERIOD = "4y"` ≈ 1006 bars. The first ~200 are dead
because SPY's own MA200 is NaN → `spy_bull_raw` is False → no trades (see M-3). OOS = 375
bars. So:

| Window | Tradeable bars | 60-bar truncation zone | Fraction affected |
|---|---|---|---|
| In-sample | 1006 − 200 − 375 ≈ **431** | 60 | **13.9%** |
| OOS | **375** | 60 | **16.0%** |

**Ratio: 1.15x**, not the ~1.7x a naive 30-vs-18-month comparison suggests. So the OOS is
penalised somewhat more, but both windows are depressed substantially.

**Why this matters, and it is not what the Owner expects.** This is **the one bias in the
entire system that runs against the strategy.** It means Engine 2's true gross OOS EV is
higher than +1.325%. It does *not* rescue the system — C-1, C-2 and C-3 all push the other
way and are individually larger — but intellectual honesty requires flagging it, and it has
a second-order consequence that does matter (see M-2).

**Concrete fix.** Do not discard. **Assign each trade to the window of its *entry*, and let
the exit simulation run past the boundary using subsequent data.** Using future bars to
*resolve* a trade whose entry decision was already made in-sample is not look-ahead — the
decision used no future information. At the true end of the dataset, mark to market at the
final close and flag the trade as `open_at_end`. This is the standard purged-CV treatment
(**U-3**).

---

#### M-2 — Engine 1 crosses the IS/OOS boundary while Engine 2 does not: holdout contamination, *and* the two engines are not comparably measured

**Where:** `oos_validation.py::simulate_mr()` L176-178:
```python
n = len(df)          # ← the WHOLE dataframe, not end_idx
...
if j >= n: return None
```
compared with `run_engine2`'s `if j >= end_idx: break`.

**What is wrong.** `simulate_mr` is bounded by `len(df)`, **not by `end_idx`.** An Engine 1
trade entered on the last bar of the in-sample window resolves using up to **10 bars of
out-of-sample data.** That is holdout contamination, small in magnitude, and it is precisely
the boundary discipline that Engine 2 (over-)enforces two functions later. The comment on
L246 explicitly claims boundary discipline for the file; only one of the two engines has it.

**The second-order consequence is the one that matters, and it is bigger than the leak
itself.** The two engines are measured under **different boundary rules**:

| | In-sample | OOS |
|---|---|---|
| Engine 1 | complete trades, **contaminated** by up to 10 OOS bars | complete trades |
| Engine 2 | **truncated**, losing ~14% of the window's winners | **truncated**, losing ~16% |

Engine 1's numbers are inflated at the margin; Engine 2's are deflated at the margin. **The
IS→OOS decay ratios of the two engines are therefore not comparable** — yet that comparison
is exactly what produced the conclusion driving live capital allocation: *Engine 2 =
"OOS已驗證,主力"*, *Engine 1 = "OOS偏弱,觀察為主"*
(`daily_strong_signals.py:145,155`).

Combined with H-3 (Engine 1 was tested at the BASIC tier, which is not traded), **the ranking
of the two engines — the most consequential output of the entire validation exercise — rests
on two engines measured with different boundary rules on different signal populations.** It
may still be the right ranking. It is not an evidenced one.

**Concrete fix.** Apply one boundary policy to both engines (the M-1 fix: assign by entry
date, resolve across the boundary, flag open-at-end). Then re-derive the engine ranking, on
matched tiers, with confidence intervals.

---

#### M-3 — Regime coverage: the effective sample is ~3.2 years of one regime, and the OOS is a continuation of the in-sample, not an independent test (Owner's item 7 — CONFIRMED)

**Where:** `oos_validation.py` L42, L325-331; `momentum_pit_backtest.py` L54-56.

**What is wrong.**

**(a) The `4y` window is really ~3.2 tradeable years.** `spy["MA200"]` is NaN for the first
200 bars, so `spy["Close"] > spy["MA200"]` is `False`, so `bull` is `False`, so **no trades
occur in the first ~200 bars (~9.5 months).** The advertised "4 years of data" is ~38 months
of tradeable sample, split roughly **20.5 months IS / 18 months OOS** — a ~53/47 split, not
the 62/38 the docstring implies. The IS estimate is noisier than presented.

**(b) Both windows are the same regime.** Run on 2026-07-30, `DATA_PERIOD = "4y"` covers
roughly 2022-08 → 2026-07. After the warmup, the effective sample begins ~2023-06. So:
- **In-sample ≈ 2023-06 → 2025-01**: the 2023-24 AI-led large-cap bull.
- **OOS ≈ 2025-01 → 2026-07**: the continuation, interrupted by the April 2025 selloff
  (during which the SPY>MA200 gate would have switched the system off).

**Same secular regime, same market leadership, largely the same tickers. The OOS is not a
different regime — it is the next chapter of the same one.** It tests whether the parameters
generalise across *time*; it does not test whether they generalise across *conditions*, and
generalising across conditions is the thing the Owner needs to know before risking capital.

**(c) How much genuine bear/chop is in the sample? Essentially none, by design.** The
`SPY > MA200` gate switches the system off during declines. Over 2019-01 → 2026-06 SPY was
below its 200dma for roughly: Feb-Jun 2020 (COVID), ~Feb 2022-Jan 2023 (the bear), briefly
Aug-Oct 2023, and Apr-May 2025 (tariffs) `[ILLUSTRATIVE — from memory; the Owner must verify]`.
That is on the order of 20-25% of trading days excluded.

This is not a criticism of the filter — a bull-only system *should* stand aside. But it has
two consequences the Owner should internalise:

1. **The backtest cannot bound the drawdown from a bear market**, because it contains almost
   no bear-market trades. The system's genuinely dangerous trades are the ones taken in the
   window between the market topping and the 200dma actually crossing — typically 10-15%
   into a decline. **There are about three such episodes in the whole sample** (Feb 2020,
   Jan 2022, Feb 2025). Three observations cannot characterise a tail.
2. **Sub-period stability, which the firm's methodology requires, cannot be established.**
   The number of independent regime episodes is ~3 over 2019-2026 and ~1-2 in the
   `oos_validation` window. You cannot demonstrate robustness across regimes with one or two
   regimes.

There is also a **structural circularity** worth naming: because the system only ever trades
when SPY > MA200, every parameter has been fitted exclusively on periods where dips
recovered. The V6.2 stop-widening "upgrade" (see M-5) is precisely a bet that dips recover.
**The filter guarantees that the fitting sample always confirms the bet.**

**Concrete fix.** Extend to 2004-2026 with a PIT universe so the sample includes 2008, 2011,
2015-16, 2018 and 2020 — five additional regime episodes. Report EV *conditioned on regime
bucket* (SPY 200dma state, VIX tercile, momentum-factor trailing return) with trade counts per
bucket, so that thin buckets are visibly thin. And add the one-line diagnostic the code
already has the data for but never prints: `print(spy_bull.mean())` — the fraction of days
the system was even allowed to trade.

---

#### M-4 — `trend_score ≥ 0.65` does far less filtering work than it appears to: it largely restates its own entry gate

**Where:** `oos_validation.py::trend_score_calc()` L131-168 (duplicated verbatim in
`momentum_pit_backtest.py` L106-137 and `telegram_swing_bot.py` L115-149).

**What is wrong.** Engine 2's entry gate already requires `ADX ≥ 25`, `DI+ > DI−`, and
`High ≥ high_20d`. Now look at what the score measures on a bar that has already passed that
gate:

| Component | Weight | Value on a bar that passed the gate |
|---|---|---|
| `+0.10` bonus for `High ≥ high_20d` | 0.10 | **always awarded — it *is* the entry gate** |
| ADX bucket | 0.25 | ≥0.6 guaranteed — the gate is `ADX ≥ 25` |
| `dist_60h` proximity | 0.25 | biased low: `high_60d` includes today, and a new 20-day high is often near the 60-day high |
| MA alignment | 0.25 | ≥0.5 near-guaranteed (a 20-day high implies `close > ma20`) |
| Volume ratio | 0.15 | ≥0.4 floor |

Worked cases `[ILLUSTRATIVE]`:
- *Ordinary breakout* — ADX 27, `c>ma20>ma50>ma200`, at the 60-day high, volume ratio 1.05:
  `0.15 + 0.25 + 0.25 + 0.105 + 0.10 = ` **0.855**. Passes comfortably.
- *Marginal* — ADX 26, `c>ma20>ma50` but below MA200, 8% off the 60-day high, volume 0.9:
  `0.15 + 0.20 + 0.0875 + 0.06 + 0.10 = ` **0.598**. Fails.

So the 0.65 threshold binds on essentially one axis: **"is the stock in full MA alignment and
near its 60-day high?"** Three of the five components are mechanically implied by, or a
restatement of, the entry gate. The score has roughly **two independent degrees of freedom
doing real work, wrapped in 36 tuned numeric constants** (counted programmatically).

**Why it matters.** The Owner believes he has a five-factor quality filter. He has a
two-factor one with an elaborate façade. This matters for upgrade decisions: tuning
`TREND_SCORE_MIN` will produce erratic, non-monotone results, because the quantity being
thresholded is mostly redundant with a binary gate. Any sensitivity analysis on that
parameter will look noisy and be misread as "robust".

**Concrete fix.** Report the marginal filtering power of each component: for each, the number
of gate-passing bars it rejects and the EV difference between rejected and accepted. Drop
components with no marginal power. Then re-tune the threshold on what remains.

---

#### M-5 — Overfitting fingerprints: 74 tuned constants in `mr_score` alone, non-monotone by hand, and a 4.5x EV jump from one parameter (Owner's item 8 — CONFIRMED)

**Where:** `oos_validation.py::mr_score()` L84-129 and `trend_score_calc()` L131-168.

**Counted programmatically:**

| Function | Numeric literals |
|---|---|
| `mr_score` | **74** |
| `trend_score_calc` | **36** |

Plus the gates and windows: `MR_SCORE_MIN=0.55`, `MIN_R=2.0`, `MR_MAX_HOLD=10`,
`ATR_STOP_MULT=2.0`, the `0.995` stop buffer, `TREND_SCORE_MIN=0.65`, `ATR_TRAIL_MULT=3.0`,
`TREND_MAX_HOLD=60`, the 12%/15% risk caps, ADX threshold 25, the 10/20/60/126-day windows,
MA 20/50/200, RSI 2/14, `TOP_N=50`, `MOMENTUM_LOOKBACK=126`.

**Total: well over 120 hand-chosen numbers.** The Owner asked whether ~20 thresholds are
embedded in `mr_score`. The true count is roughly **3.5x that**, because every bucket
boundary *and* every bucket score *and* every category weight is a free parameter.

**The non-monotonicity is the clinching diagnostic.** Look at `mr_score`'s RSI14 mapping:

```
35-45 → 1.0      45-55 → 0.8      30-35 → 0.6      55-65 → 0.4      >65 → 0.1      <30 → 0.3
```

A hump in the middle, with the sub-30 bucket (0.3) scoring *above* the 55-65 bucket (0.4)?
No — below it, but above the >65 bucket, while 30-35 scores 0.6. **This function is not
monotone and has no economic story.** A genuine mean-reversion relationship with RSI would be
monotone or smoothly single-peaked with a defensible rationale. A hand-carved piecewise
function with a bump exactly where the sample happened to perform is **the canonical
fingerprint of fitting to in-sample outcomes.** `price_vs_ma20` and `ret_10d` show the same
pattern.

**On the 0.24% → 1.10% jump.** A 4.58x change in EV from one stop-rule change is a very large
effect for one parameter, and the naming — the OOS file calls the 2×ATR stop **"C臂"**, *arm
C* — confirms it was chosen as the best of at least three tested arms.

`[ILLUSTRATIVE — assuming per-trade σ = 6% and n = 200]`: SE of EV = `6/√200 = 0.42%`. So
0.24% is 0.6σ from zero and 1.10% is 2.6σ. The *difference* of 0.86% is ~2σ — but the two
figures are computed on **the same trades** with a different stop, so they are highly
correlated and the difference is not independently significant either. **A gap of this size
between two stop rules on a single sample is comfortably within what noise plus one selection
produces.**

**The deeper problem is that the change is not an edge, it is a regime bet.** Widening a stop
(taking the *wider* of the structural low and 2×ATR) mechanically converts small losses into
either larger losses or recovered winners. **On any sample where dips recover, widening stops
always looks better.** And because of the `SPY > MA200` gate (M-3), the fitting sample is
*guaranteed* to be a sample where dips recovered. The V6.2 "upgrade" is a bet that dips
recover, fitted on data selected to contain only dips that recovered, and then validated on
more data selected the same way. **In 2008, 2018Q4 or 2022 the same change would have been
severely costly, and no window in this backtest can reveal that.**

**Concrete fix.** See **U-4** (log every trial, compute the Deflated Sharpe with the honest
`N`) and **U-10** (replace the hand-bucketed scores with a monotone, low-parameter form —
rank-normalise each raw feature to [0,1] and average — which deletes ~100 tuned constants in
one change and is itself a direct test of whether the buckets were ever doing real work).
Also: run the V6.2 stop change on a 2008-2011 sample before trusting it.

---

#### M-6 — The Pine indicator repaints on the current bar

**Where:** `dual_engine_v6_4_tiers.pine` throughout — `score`, `tier`, `stopL`, `target`,
`rVal` and all three `alertcondition`s are computed from `close`, `ta.rsi`, `ta.dmi`,
`ta.atr` on the developing bar.

**What is wrong.** On the incomplete (current) bar every one of these values updates tick by
tick. A 頂級 label that appears at 11:00 can vanish by 15:59. The backtest assumes a single
decision at the close (and H-1 shows even that is optimistic).

**Why it matters.** This creates the behavioural failure mode the Owner has already
experienced. Intraday, the trader sees a signal that the closing-basis system would never
have generated, acts on it, and then attributes the result to "the system". It also silently
inflates his perceived signal frequency, which erodes the "most days there is no signal"
discipline that `daily_strong_signals.py:18` correctly emphasises.

**Concrete fix.** Gate all labels and alerts on `barstate.isconfirmed`, or evaluate on the
prior bar (`score[1]`, `tier[1]`). Also confirm that `request.security("AMEX:SPY", ...)`
runs with `lookahead_off` (the Pine v6 default, so this part is fine) and note that on
intraday chart resolutions the daily SPY close is still the developing close.

---

#### M-7 — Silent failure modes can shrink the sample without any warning

**Where:** `momentum_pit_backtest.py` (5 bare `except Exception` blocks: L80, L161, L163,
L175, L215); `oos_validation.py:348-350`; `oos_validation.py:340`.

Detailed under C-5(5). The specific one worth restating: at `oos_validation.py:340`,
`bull = spy_bull_raw.reindex(df.index, method="ffill").fillna(False)` — a timezone or
calendar mismatch produces NaN → `False` → **that ticker silently contributes zero trades.**
Neither script ever reports how many of the 38 (or 500) tickers actually produced trades.
**The Owner has no way to know whether his "38-stock backtest" ran on 38 stocks or on 9.**

**Concrete fix.** Print the contributing-ticker count and the per-ticker trade count. Assert
`bull.notna().all()` before use. Replace every bare `except` with either a loud log or an
abort.

---

#### M-8 — Split/dividend adjustment in `oos_validation.py` depends on an unpinned library default that has changed

**Where:** `oos_validation.py:325,336` — `yf.Ticker(tk).history(period=DATA_PERIOD)` with
**no `auto_adjust` argument**, versus `momentum_pit_backtest.py:154,179` which passes
`auto_adjust=True` explicitly.

**What is wrong.** `yfinance` changed the default of `auto_adjust` on `Ticker.history()`
across versions (older releases defaulted to `False`; recent ones to `True`). With no
`requirements.txt` pinning the version, **whether the OOS validation ran on split-adjusted
prices depends on which yfinance happened to be installed.**

**Why it matters in money terms.** If it ran unadjusted, every stock split appears as a
one-day −50% (or −75%) crash. In Engine 1 that manufactures spurious oversold mean-reversion
signals (`ret_10d` deeply negative, RSI2 near zero — the *highest*-scoring configuration) and
spurious stop-outs. In Engine 2 it manufactures spurious trailing-stop exits. NVDA (10:1,
2024), AMZN and GOOGL (20:1, 2022), TSLA (3:1, 2022) all split inside the test window, and
all are in the 38-ticker pool. **This is potentially a large, silent, version-dependent
corruption, and it is unknowable from the artifacts.**

**Concrete fix.** Pass `auto_adjust=True` explicitly everywhere; pin `yfinance` and `ta` in
`requirements.txt`; assert that no single-day return in the loaded data is below −35%
without a corresponding corporate action, and log any that are.

---

### LOW

- **L-1** — `while i < end_idx - 2` (`oos_validation.py` L191, L225): undocumented magic
  constant. Its purpose is unclear and it silently drops the last two bars of each window.
- **L-2** — Dividend back-adjustment means the "10-day low × 0.995" structural stop is
  computed on a price series nobody could trade. Immaterial over a 10-day hold (~0.04%);
  marginally relevant to the 126-day momentum ranking (~0.65%), where it could reorder
  borderline names.
- **L-3** — `momentum_pit_backtest.py:212`: `spy_bull.index.searchsorted(today)` with
  `side='left'` returns the *next* trading day when `today` is a holiday, a one-day
  look-ahead on the bull flag. Immaterial, because `if today not in df.index: continue`
  prevents trading on those days — but it is a latent bug.
- **L-4** — Version drift inside one file: `dual_engine_v6_4_tiers.pine` header says V6.2
  (L2), `indicator()` name says V6.4 (L17), and the file implements Engine 1 only.
- **L-5** — `momentum_pit_backtest.py:197`: `sub = df.loc[:today]` slices the full history
  for every ticker on every rebalance — O(n²) and the stated cause of the 20-30 minute
  runtime. Not a bias; use `.asof()` or a precomputed monthly matrix.
- **L-6** — `telegram_swing_bot.py:37`: `BOT_TOKEN` is a hardcoded literal awaiting a real
  secret in a git-tracked file. Move to an environment variable before a token ever lands
  there.
- **L-7** — No output of run date, universe, parameters or library versions to any CSV
  (folded into C-5).

---

## 3. Net-effect ledger — which way each bias pushes

| Finding | Direction on reported EV | Rough size `[ILLUSTRATIVE]` |
|---|---|---|
| C-1 Survivor/inclusion-selected universe | **Inflates** | ≥ the entire claimed edge |
| C-2 Zero transaction costs | **Inflates** | 0.80% – 3.38% per trade |
| C-3 Unfunded concurrency, no sizing | **Inflates** (and invalidates the statistic) | not expressible as an EV delta |
| C-4 Contaminated holdout, ~20 trials | **Inflates** | Sharpe ~1.0 ≈ noise at N=20 |
| H-1 Signal-at-close / fill-at-close | **Inflates** | 0.10% – 0.30% |
| H-2 Engine 1 no gap modelling, no earnings filter | **Inflates** (left tail especially) | ~0.30% on Engine 1 |
| H-3 Guardrails absent; Engine 1 tested at wrong tier | **Inflates** (population mismatch) | unquantified |
| H-4 Share quantisation, concentration breach | **Inflates** (dispersion ±50%) | unquantified |
| H-7 Clustered trades treated as independent | **Inflates confidence**, not EV | n_eff ≈ n/3.4 to n/7.3 |
| **M-1 Engine 2 boundary truncation** | **DEFLATES** | ~+0.57% understated |
| M-2 Engine 1 crosses the boundary | Inflates Engine 1 vs Engine 2 | small, but distorts the engine ranking |
| M-8 Possible unadjusted splits | **Unknown sign, potentially large** | unquantified |

**One material bias runs in the Owner's favour. Nine or more run against him.** The claimed
+1.325% is a gross number computed on a favourable universe with no costs and no capital
constraint. Adjust for C-2 alone and it is between +0.53% and −2.06%. Adjust for C-1 as well
and there is no basis to assert it is positive.

---

## 4. What would make this fail live

Ranked by how likely I think each is to be the thing that actually hurts:

1. **Commission drag at a US$128-183 notional.** The most likely outcome is not a dramatic
   loss but slow bleed: a win rate close to the backtest, an average win close to the
   backtest, and a net equity curve that drifts down because every round trip costs more
   than the expected profit. This will be very hard to diagnose from the outside, because
   every individual trade will look like it "worked".
2. **The four hindsight tickers stop working.** If the edge is concentrated in
   MSTR/COIN/PLTR/NVDA (C-1), the system stops working the moment those names stop trending,
   and the failure will be attributed to "market conditions" rather than to the selection.
3. **Capital rationing on the best days.** The account funds ~7 positions; the backtest
   assumes up to 50. Live entries will be taken in signal-arrival order, and the best trades
   cluster at the start of up-legs when the account is most likely already full.
4. **Correlated stop-out.** With 5-7 momentum names held simultaneously and no correlation
   limit, a single factor reversal takes every stop in the same week. At 1% risk each that
   is 5-7% of the account in days — and the system has no drawdown estimate to contextualise
   it, so the psychological response is unpredictable.
5. **Chart/scanner disagreement (H-5).** The Owner sizes and enters from a chart that can
   show a different R and a higher tier than the validated engine, on the widest-stop
   trades.
6. **A gap through an Engine 1 stop on earnings.** The backtest has no earnings filter and
   assumes exact stop fills. The first −16% single-trade loss will feel like a system
   failure when it is actually an unmodelled assumption.
7. **The first genuine bear market.** The system has never traded one, by construction. The
   dangerous window is between the market top and the 200dma cross — three observations in
   the entire sample.
8. **The parameters were fitted on dips that recovered** (M-5). The V6.2 stop-widening is a
   bet on mean reversion of the market itself, and no window in this backtest could ever
   falsify it.

---

## 5. UPGRADES — ranked, implementable

### ★ Do this one first

> **U-1 — Build one event-driven portfolio simulator with a cash ledger and a full cost
> model, replacing both scripts.**

**Why this one and not the others.** It is the only upgrade that can **change the sign of the
answer**, it requires **no new data and no new subscription**, and it is roughly a day of
work. Every other upgrade refines a number that may well be negative. There is no point
computing a Deflated Sharpe for a strategy whose gross edge is smaller than its commission,
and no point buying a point-in-time dataset to more accurately measure something that costs
more to trade than it earns. **Establish that a net-of-cost, capital-constrained,
portfolio-level edge exists at all — then spend money on data.**

Specification:
- Daily event loop over a **cash ledger** with real starting equity (US$1,282).
- **Integer share counts** via the live `position_plan`; skip the signal when `shares < 1`.
- Explicit `MAX_CONCURRENT` (start at 5) and a hard total-risk cap; log every signal
  **rejected for insufficient capital** — that rejection log is itself a finding.
- Full cost model per fill: `max(min_commission, rate × notional) + half-spread +
  slippage_bp`, plus FX on conversion, plus pessimistic stop fills.
- Entry at the **next bar's open** (fixes H-1).
- Output: equity curve, **max drawdown, drawdown duration, worst month, monthly return
  table, tail (5th percentile trade, worst 5 trades)**, exposure %, then and only then
  Sharpe / Sortino / CAGR.
- Apply the live guardrails (H-3) so the tested population is the tradeable population.

**Before writing a line of it**, spend 30 free minutes on the diagnostics that may make it
unnecessary: add `ticker` and `entry_date` to `oos_validation.py`'s trade records (L214,
L264), print EV by ticker, print `spy_bull.mean()`, and print the concurrency histogram.
**If EV by ticker shows the edge living in four names, stop — C-1 is the whole story and
nothing else needs building.**

### Then, in order

**U-2 — Point-in-time universe with delisted names.** Norgate (~US$70/mo) or Sharadar
SEP+TICKERS (~US$50-150/mo). Store the constituent set per rebalance date in the output.
This is the only fix for C-1 and it cannot be done within `yfinance`. Second because it
costs money and time, and U-1 may render it moot.

**U-3 — Walk-forward with purging and embargo.** Replace the single 30/18 split with an
anchored walk-forward: fit on `[0, t]`, test on `(t, t+6m]`, roll. **Purge** trades whose
holding window straddles a boundary and **embargo** `max_hold` bars after each test window
(López de Prado). Assign each trade to the window of its **entry** and resolve exits across
the boundary — this fixes M-1 and M-2 together. Report the distribution of out-of-sample EV
across folds, not a single number.

**U-4 — Deflated Sharpe Ratio with an honest trial count.** Create `strategy/v6.4/trials.csv`
and retro-populate it: V1 through V6.4, stop arms A/B/C, every `DATA_PERIOD` change, every
threshold that was moved. Then compute DSR with the real `N`. My prior is that `N ≥ 20` and
that the DSR will not clear zero. That result would be worth more than any further
optimisation.

**U-5 — Minimum Track Record Length + a pre-registered live evaluation plan.** Compute MinTRL
for the claimed Sharpe. Then, *before* trading, write down: how many trades before any
conclusion is drawn, what result triggers a stop, and what result triggers scaling up.
Pre-registration is the only real defence against the hindsight rationalisation that follows
a losing streak.

**U-6 — One shared rules module + a Pine/Python golden-file regression test.** Extract the
ruleset into a single module imported by the backtest, the scanner and the bot. Export N
historical bars with the expected `tier`/`stop`/`target`/`R` and assert Pine reproduces them.
This closes H-5 and H-6 permanently, and it is the only way to keep them closed.

**U-7 — Block-bootstrap confidence intervals.** Stationary bootstrap on 20-day calendar
blocks so that clustering is preserved (H-7). **Report EV as a CI, never as a point
estimate.** If the CI crosses zero, the verdict is "no conclusion" — that verdict must be
available to `verdict()`, which currently cannot express it.

**U-8 — Regime-conditional reporting.** Bucket by SPY 200dma state, VIX tercile, and
trailing momentum-factor return. Report EV and trade count per bucket so thin buckets are
visibly thin. This is how you make M-3 impossible to overlook.

**U-9 — Full parameter sensitivity surface.** ±20% on every one of `ATR_STOP_MULT`,
`ATR_TRAIL_MULT`, `MR_SCORE_MIN`, `TREND_SCORE_MIN`, `MIN_R`, `MR_MAX_HOLD`,
`TREND_MAX_HOLD`, `TOP_N`, `MOMENTUM_LOOKBACK`. **The standard is that the edge must survive
every single perturbation.** Report the surface, not the peak. A peak that is sharp is not an
edge — it is a coordinate.

**U-10 — Delete ~100 tuned constants.** Replace the hand-bucketed `mr_score` and
`trend_score_calc` with a monotone, low-parameter form: rank-normalise each raw feature to
[0,1] over a trailing window and average with equal weights. If performance is materially
unchanged, the buckets were never doing anything and 110 degrees of freedom vanish. If
performance collapses, that is strong evidence the buckets were fitted to noise. **Either
outcome is informative, which is what makes this a good test.**

---

## 6. Answers to the eight specific questions

| # | Question | Answer |
|---|---|---|
| 1 | Universe survivorship in `momentum_pit_backtest.py`? | **CONFIRMED — the most important finding.** The ranking is genuinely PIT; the universe is not. The dominant channel is **index-inclusion look-ahead**, not deletion survivorship, and it is aligned with the momentum selection. Direction: **upward**. Magnitude: **of the same order as, or larger than, the claimed edge.** The file's console output ("冇生存者偏差") contradicts its own docstring. `oos_validation.py`'s hand-picked 38-name pool has the same disease, worse. → **C-1** |
| 2 | Engine 2 boundary truncation? | **CONFIRMED.** Truncated trades are **disproportionately winners** (length-biased sampling × duration-return coupling in a trailing-stop system; ~4.5x differential). Bias direction: **the OOS EV is understated, not overstated.** The OOS window is penalised **~1.15x** more than the IS (16.0% vs 13.9% of tradeable bars) — not the 1.7x a naive month-count suggests. This is the one bias in the Owner's favour. → **M-1** |
| 3 | Is `COOLDOWN` a genuine divergence? | **CONFIRMED dead code** — one occurrence, the declaration. The "rules locked to V6.4" claim is false as written. Whether live V6.4 enforces a cooldown is unverifiable because `dual_engine_v6_4.py` is absent. **Five further divergences:** `RISK_PCT` also dead; three different stop-width caps (12/15/none); all guardrails absent from both backtests; Engine 1 backtested at the BASIC tier which is not traded; **the Pine file contains no Engine 2 at all** despite Engine 2 being the declared main engine. → **H-6, H-3, C-5** |
| 4 | Target-selection divergence? | **CONFIRMED**, scoped: the two disagree **only when both MA50 and the 60-day high are valid ≥2R targets** — i.e. on the deeper-pullback, widest-stop subset. On that subset the chart shows a **higher R**, promoting signals to 強/頂級 that the scanner rates 普通, and pushes the exit farther against a fixed 10-day clock (lower hit rate, higher variance). **The Pine variant has never been backtested**, yet the file quotes the other variant's +1.10%. → **H-5** |
| 5 | No transaction costs? | **CONFIRMED — zero cost modelling anywhere.** At a US$1,282 account the expected gross profit per trade is **US$1.70-2.01** against a **US$0.70-4.00** round trip. Best case cuts the +1.325% EV to **+0.53%** (−60%); mid and typical HK-retail cases take it to **−0.49%** and **−2.06%**. → **C-2** |
| 6 | Concurrency and capital? | **CONFIRMED — 50 concurrent positions permitted**, implying **50% of the account at risk simultaneously** and **5-7x leverage**, breaching `leverage: none`, `max_single_position: 0.10` and `max_correlated_cluster: 0.40` in `config/risk-limits.yaml`. `RISK_PCT` is **declared and never used**, so the docstring's claim that the backtest "automatically obeys the 1% rule" is false. **The per-trade EV means nothing as a portfolio result** — no equity curve, no drawdown, no compounding, no correlation. → **C-3** |
| 7 | Regime coverage? | **CONFIRMED.** ~20-25% of days are excluded by the `SPY>MA200` gate, so there are **almost no bear-market trades by design**. Worse, the `4y` window loses its first ~200 bars to MA200 warmup, so the effective sample is **~20.5 months IS / 18 months OOS**, both inside the **same post-2022 AI-led bull**. **The OOS tests the same regime — it is a continuation, not an independent test.** Independent regime episodes: ~1-2 in `oos_validation`, ~3 in `momentum_pit`. Sub-period stability cannot be established. → **M-3** |
| 8 | Multiple testing? | **CONFIRMED and worse than stated.** `mr_score` contains **74** numeric literals (not ~20) and `trend_score_calc` **36**; total system DoF **>120**. The scores are **non-monotone hand-carved piecewise functions** — a textbook overfit fingerprint. The 0.24%→1.10% jump came from selecting **"arm C"** of ≥3 tested stop rules, and the difference is within noise for a plausible σ. Structurally, **widening stops always wins on a sample gated to exclude declines** — the filter guarantees the fitting sample confirms the bet. At `N≈20` trials, the expected best-of-noise Sharpe is **~0.98**. → **C-4, M-5** |

---

## 7. Recommendation to the Investment Committee

1. **No new capital into V6.4 until U-1 is complete.** Not because the strategy is proven
   bad — it is not — but because at this account size the cost arithmetic alone plausibly
   makes it negative, and that question is answerable in a day with no new data.
2. **Run the free diagnostic today** (EV by ticker, `oos_validation.py` L214/L264 + one
   print). It may resolve the entire question in half an hour.
3. **Refer C-3 to John (CRO).** The momentum backtest models a portfolio that breaches four
   hard limits in `config/risk-limits.yaml`, including `leverage: none`. That is his call,
   not mine.
4. **Correct the three false claims in the code**, because they are actively misleading the
   Owner every time he runs it: `momentum_pit_backtest.py:309` ("冇生存者偏差"),
   `momentum_pit_backtest.py:25-26` ("已自動遵守1%規則"), and `oos_validation.py:370`
   ("冇任何參數可以調").
5. **Stop describing Engine 2 as "OOS已驗證".** On the evidence available it is not
   validated; it is untested against costs, untested against capital constraints, and tested
   on a survivor-selected universe over one regime, using a boundary rule different from the
   engine it is being compared against.

The Owner has built something with genuinely good instincts — regime gating, an explicit OOS
discipline, guardrails, and written commitments against self-deception. That last one is
rarer than the rest and it is why this audit is worth acting on rather than resenting. The
measurement layer has not kept up with the design layer. Fix the measurement and you will
find out what you actually have.

---

*Tom — Backtesting Engineer, Department 3. Research only; the Committee and the Owner decide.
I did not run these backtests and I have invented no performance figures; every non-code
number above is labelled `[ILLUSTRATIVE]`.*
