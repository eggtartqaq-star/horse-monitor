# V6.4 "Dual Engine" Personal Swing System — Risk Architecture Review

**John, Chief Risk Officer — Department 6, Risk Management · 皮褸黃 Capital**
**Reference date: 2026-07-30** · Subject: the Owner's personal swing-trading system, V6.4
**Scope:** risk architecture only — guardrails, sizing, concurrency, correlation, data integrity, governance.
**Not in scope:** whether the alpha is real. That is Quant's question. Mine is what happens when it isn't.

---

## VERDICT: **VETOED** — for live capital at the current configuration

**Risk score (committee input): 22 / 100** *(scale: 0 = do not deploy, 100 = clear at full size; higher is safer. Rises to ~70 with the nine clearance conditions in §7 met.)*

I want to be precise about what I am vetoing, because a blanket "no" would be both unfair and useless here.

**What I am not vetoing.** The research process is better than most retail systems I have reviewed and better than some institutional ones. `oos_validation.py` locks its parameters, splits in-sample/out-of-sample honestly, defines pass/fail thresholds *before* seeing results, warns when n < 30, and ends with an instruction not to tune the parameters until it passes. `momentum_pit_backtest.py` volunteers its own survivorship bias and forbids the point-in-time cheat in writing. That is genuine intellectual discipline and it should not be lost in what follows.

**What I am vetoing** is three specific things:

1. **Running 1%-risk sizing with no notional cap and no concurrency cap.** These two omissions together convert a "1% risk" rule into an uncapped concentration and leverage rule. This is a design defect, not a small-account defect — it is present at any account size (§3, C-1 and C-2).
2. **Deploying real capital while every guardrail is a *display* rather than a *control*.** The system has already been overridden twice in six trading days. A control with a measured failure rate that high is not a control (§3, C-3).
3. **Treating the cited OOS edge (+1.325% / +1.497% per trade) as a portfolio expectation.** It is a per-trade, gross-of-cost, single-position statistic drawn from a book that was never simulated at portfolio level and could not be funded without 4–8x leverage (§3, C-2; §4.1).

The alpha may well be there. The container it is being poured into leaks.

---

## 0. Evidence base and what I could not verify

| Item | Status |
|---|---|
| `telegram_swing_bot.py`, `dual_engine_v6_4_tiers.pine`, `daily_strong_signals.py`, `oos_validation.py`, `momentum_pit_backtest.py` | Read in full; all code claims below verified by direct inspection |
| `config/risk-limits.yaml`, `config/portfolio.yaml` | Read; used as the benchmark standard |
| **`dual_engine_v6_4.py`** | **ABSENT from the repo.** `daily_strong_signals.py` imports its entire logic from it — `TICKERS`, `classify`, `check_guardrails`, `position_plan`, `MR_SCORE_MIN`. **The daily scanner's actual behaviour is unreviewable and unrunnable from this directory.** See H-6. |
| Live prices / ATR / correlation matrix for the 38-name pool | **Could not obtain.** I installed yfinance and attempted the exact data path the system depends on. The organisation's egress proxy returned **HTTP 403 on all 39 symbols**. Per proxy policy I did not route around it. Blocked host: Yahoo Finance. **Consequence for this report: every correlation coefficient below is a labelled scenario, not a measurement.** Consequence for the system: see H-3 — this outage is a live demonstration of the failure mode. |
| Mo Peter (VaR) / Mario (stress) inputs | Not commissioned. Both require the market data above. Commissioned conditionally in §7, CL-5. |
| Broker commission schedule, actual fills for 7/13 and 7/18, actual account balance | Not supplied. Treated as open items; the decisive thresholds are computed so the Owner can check them himself. |

**Jurisdictional note.** `config/risk-limits.yaml` governs the *firm* book. This is the Owner's *personal* capital and he is entitled to set different personal limits. I am measuring against the firm limits because he asked me to and because they are the only written limits that exist. That is itself the point: **his personal risk limits are currently not written down anywhere.** They are implicit in constants scattered across five files, and in three places those constants disagree with each other (§3, H-2). If he wants different limits he should *choose* them, not inherit them from whichever file happened to run.

---

## 1. The governing arithmetic

All figures derive from constants in the source files. No price is assumed.

**Source constants** (`telegram_swing_bot.py` L42–44; identical in the Pine inputs L20–22):
```
ACCOUNT_HKD = 10000 ;  RISK_PCT = 1.0 ;  USD_HKD = 7.8
```

| Quantity | Derivation | Value |
|---|---|---|
| Account, USD | 10,000 / 7.8 | **US$1,282.05** |
| Risk budget per trade @ 1% | 10,000 × 1.0 / 100 / 7.8 | **US$12.8205** |
| Risk budget @ 0.5% (普通 tier) | half of the above | **US$6.4103** |
| Firm single-position cap, 10% | 0.10 × 1,282.05 | **US$128.21** |
| Firm drifted/trim cap, 15% | 0.15 × 1,282.05 | **US$192.31** |

### 1.1 The identity that drives this entire review

`position_plan()` (bot L167–175) sets `shares = int(risk_usd // per_share_risk)`. Ignoring integer truncation for the moment, the resulting **position notional** is:

```
notional        risk_budget       close          RISK_PCT
────────  ≈  ─────────────── ×  ─────────  =  ──────────────
account          per_share       account         stop_pct
```

> **Position size as a percentage of the account equals the risk percentage divided by the stop width.**
> It does not depend on the price of the stock. It does not depend on the size of the account.

| Stop width | Notional as % of account | vs firm 10% single-position cap |
|---:|---:|---|
| 2% | 50.00% | **BREACH — 5.0x** |
| 3% | 33.33% | **BREACH — 3.3x** |
| 4% | 25.00% | **BREACH — 2.5x** |
| 5% | 20.00% | **BREACH — 2.0x** |
| 6% | 16.67% | **BREACH — 1.7x** |
| 7% | 14.29% | **BREACH — 1.4x** |
| 8% | 12.50% | **BREACH — 1.25x** |
| 9% | 11.11% | **BREACH** |
| **10%** | **10.00%** | **exactly at the cap** |
| 12% | 8.33% | pass |
| 15% | 6.67% | pass |

**Read that table again, because it inverts the intuition the system is built on.**

The tighter the stop, the *larger* the position. A 1%-risk rule is only compatible with a 10% concentration cap when the stop is **10% wide or wider**. Every stop tighter than 10% breaches concentration.

And the system's guardrails **select for tight stops**. Engine 2 hard-blocks any stop wider than 12% (`trend_plan()`, L156–157). Engine 1 blocks wider than 15%. Engine 1's stop is `min(10-day-low × 0.995, close − 2×ATR)` — for a liquid large-cap that is typically in the mid-single digits.

> **The guardrails are systematically steering the book into the concentration-breach zone. The stop-width guardrail and the concentration limit are pulling in opposite directions, and only one of them is implemented in code.**

There is **no notional cap anywhere in any file.** I checked: `position_plan()` returns `(shares, cost)`, `cost` is printed to the user (`建議股數: {shares}股 (~${cost})`, bot L392/L426) and written to the scanner CSV as `投入$` — and **is never compared to the account balance.** Nothing in the codebase knows how much money he has to spend, only how much he is willing to lose.

---

## 2. Limit-by-limit check against `config/risk-limits.yaml`

Assessed against the system **as designed and as permitted**, not against a hypothetical well-behaved day.

| Limit | Config | System's implemented control | Worst case permitted | Pass/Fail |
|---|---|---|---|---|
| `max_risk_per_trade` | 1% | `position_plan()`, integer shares | 1.00% (0.55–1.00% after rounding) | **PASS** — the one limit genuinely enforced |
| `stop_required` | true | Every plan carries a stop; `trend_plan`/`mr_plan` return `None` without one | — | **PASS** |
| `max_single_position` | 10% | **none** | Unbounded as stop → 0; 50% at a 2% stop | **FAIL — CRITICAL** |
| `max_single_position_drifted` | 15% | **none** — no position tracking exists at all | Unbounded | **FAIL** |
| `leverage` | **none** | **none** | 4.2x–8.3x gross at 50 concurrent (§4.1) | **FAIL — CRITICAL** |
| `cash_floor` | 10% | **none** | 0% — system buys until funds exhausted | **FAIL** |
| `max_drawdown` | 20% | **none** | Stated heat 50% = **2.5x the entire budget**; never simulated | **FAIL — CRITICAL** |
| `max_var_95_1d` | 3% | **none** | Not computable — no position ledger exists | **CANNOT ASSESS** |
| `max_sector` | 35% | **none** | Pool is 52.6% tech complex *before any signal fires* (§4.2) | **FAIL** |
| `max_correlated_cluster` | 40% | **none** | Same; momentum filter amplifies it further | **FAIL** |
| `max_adv_participation` | 5% | **none** | Immaterial at this size — 1-share orders | **PASS (by size, not by design)** |
| `live_trading: forbidden` / tickets only | — | Bot emits text; Owner places orders manually | Complies in form | **PASS** — but see C-3 |
| `decision_record_before_ticket` | true | **none** — no journal enforcement; the bot *asks* him to keep one | — | **FAIL (process)** |

**Score: 4 pass, 8 fail, 1 unassessable.** Every failure is an *omission* rather than a wrong value. Nothing here is mis-calibrated; seven controls simply do not exist.

---

## 3. Findings, severity-ranked

### CRITICAL

---

#### **C-1 — The 1%-risk rule has no notional cap, and therefore produces uncapped concentration.**

**Evidence.** `position_plan()` (bot L167–175) and the Pine equivalent (L79–84) size purely on `risk_usd / per_share_risk`. `cost` is computed and displayed but never bounded. Grep confirms no comparison of `cost` against `ACCOUNT_HKD` anywhere in the codebase.

**Quantification.** Per §1.1: notional% = RISK_PCT / stop_pct. Concrete worked example on the account as configured — a US$200 stock with a tight 2% stop (per-share risk US$4.00): `shares = int(12.8205 // 4.00) = 3`, cost = **US$600 = 46.8% of a US$1,282 account, in one name.** The bot displays this as `建議股數: 3股`, tier 強, all guardrails passed, green light. Every guardrail in the system approves a position at 4.7x the firm concentration limit.

This is the single most dangerous line of code in the system, precisely because it is *silent* and *feels conservative*. He believes he is risking 1%. He is risking 1% on the stop and 46.8% on the gap.

**Gap risk is the reason this matters.** A stop is a *plan*, not a *guarantee*. Overnight gaps, halts and earnings do not respect stops. The actual overnight loss on a position is bounded by *notional*, not by stop distance. So the quantity that governs his survivability is exactly the quantity the system does not track.

**Control.** In `position_plan()`, cap shares by notional and return an explicit block, not a silent truncation:
```python
MAX_POS_PCT = 0.10                      # from a personal risk-limits file, not a magic number
acct_usd    = ACCOUNT_HKD / USD_HKD
risk_shares = int(risk_usd // per_share)
cap_shares  = int((MAX_POS_PCT * acct_usd) // entry)
shares      = min(risk_shares, cap_shares)
binding     = "NOTIONAL" if cap_shares < risk_shares else "RISK"
# and surface `binding` to the user — he must SEE which limit bit
```
Surfacing `binding` is not cosmetic. It is how he learns that the concentration cap, not the risk rule, is what actually governs this strategy.

---

#### **C-2 — No cap on concurrent positions; no portfolio-level backtest was ever run; the validated strategy is not fundable.**

**Evidence.** Grep for `len(open_positions)`, `MAX_POS`, `max_positions`, `concurrent` across all five files returns **nothing**. In `momentum_pit_backtest.py` the entry loop (L247–270) iterates the full 50-name `current_pool` with only `if tk in open_positions ... continue` — a duplicate check, not a count check. Theoretical maximum: **50 simultaneous positions.**

**Quantification — stated heat vs the drawdown budget:**

| Concurrent positions | Stated heat (all stops hit) | vs `max_drawdown: 0.20` |
|---:|---:|---|
| 5 | 5% | 0.25x |
| 10 | 10% | 0.50x |
| 20 | 20% | **1.00x — the entire budget in one event** |
| 50 | 50% | **2.50x — the budget consumed 2.5 times over** |

**Quantification — gross exposure, which is the harder finding.** Combining with the §1.1 identity, gross exposure = N × (1% / stop_pct):

| N positions | stop 6% | stop 8% | stop 10% | stop 12% (the widest E2 permits) |
|---:|---:|---:|---:|---:|
| 5 | 83% | 62% | 50% | 42% |
| 10 | **167%** | **125%** | 100% | 83% |
| 20 | **333%** | **250%** | **200%** | **167%** |
| 50 | **833%** | **625%** | **500%** | **417%** |

> **The 50-name momentum backtest is a 4.2x-to-8.3x levered strategy in disguise.** Even at the *widest* stop the system permits, 50 concurrent positions require 417% gross exposure. `config/risk-limits.yaml` says `leverage: none`. The backtest that produced the headline EV **cannot be funded in a cash account at any account size.**

**And no portfolio-level test exists to catch this.** `stats()` in `oos_validation.py` (L272–285) returns `n, win, avg_win, avg_loss, ev, days, worst`. `momentum_pit_backtest.py` reports the same shape. **Neither computes an equity curve, a portfolio drawdown, or a concurrency count.** `worst` is the worst *single trade*, not the worst *portfolio* moment — and the file's closing advice, `記住睇埋逐年最差單筆`, tells him to look at exactly the wrong statistic.

Worse, `oos_validation.py` actively hides concurrency: `i += max(exit_day, 1)` serialises trades *within* one ticker, then pools all tickers' trades into one flat list with no date alignment. Two hundred trades that all happened in the same fortnight look identical to two hundred spread over four years.

> **The 20% max-drawdown limit has never been tested against this strategy, because nothing in the codebase is capable of computing a drawdown.**

**Control.** Three parts, in order:
1. `MAX_OPEN_POSITIONS = 5` and `MAX_PORTFOLIO_HEAT = 5%` as hard blocks, checked before any new entry.
2. Rebuild the portfolio equity curve from `momentum_pit_trades.csv`, which he already generates and which already contains `entry_date` and `exit_date`. The data to answer this exists in his own output folder and has never been read. Compute: max concurrent positions, gross exposure through time, portfolio equity curve, max drawdown.
3. Re-run with the caps applied. If capped max DD > 20%, the caps tighten until it isn't.

---

#### **C-3 — Every guardrail is a display, not a control. Failure rate is measured, not hypothetical.**

**Evidence.** `momentum_pit_backtest.py` L20–26, in his own words:
> 「你7/13入咗1888 500股(超額11倍)、7/18入咗BAC 300股(超額100倍)。」

**This was not one rule broken twice. On 7/13 he broke at least three simultaneously.** `1888` normalises to `1888.HK` (`normalize_ticker`, bot L60–64). Therefore:
- **Guardrail 4 (pool):** `in_pool = (market == "美股" and ticker.upper() in POOL)` — a HK ticker can *never* satisfy this. Blocked.
- **HK prohibition:** `港股:系統以美股回測,未經驗證,唔應該做`. Blocked.
- **Guardrail 3 (sizing):** 11x the suggested size. Blocked.

**Quantification of the sizing breaches:**

| Date | Trade | Stated oversize | Risk taken on that single stop |
|---|---|---:|---:|
| 7/13 | 1888.HK, 500 sh | 11x | US$141.03 = **11.0% of the account** |
| 7/18 | BAC, 300 sh | 100x | US$1,282.05 = **100% of the account** |

The 7/18 trade put **the entire account** on one stop level. Designed risk: US$12.82.

**The leverage finding is assumption-free.** I do not know BAC's price on 7/18 and will not guess. I do not need to:

| BAC price | 300-share notional | vs US$1,282 account |
|---:|---:|---:|
| $10 | $3,000 | 2.34x |
| $30 | $9,000 | 7.02x |
| $50 | $15,000 | 11.70x |

> At *any* plausible price for BAC, 300 shares is a **multiple of the entire account**. This trade could not have been placed in a cash account. It required margin. `leverage: none` is the hardest rule in `config/risk-limits.yaml`, and it was breached by at least 2.3x and plausibly by ~9x.

**The governance point.** The bot prints `唔可以入場,原因:`. The Pine colours the background red. **Neither can stop an order.** Between the guardrail and the broker sits nothing but the Owner's willpower at the moment of maximum temptation — and the empirical record is two failures in six trading days (13 and 18 July). I do not know the denominator and will not pretend to; if those were the only two trades he took, the failure rate is 100%. For a control whose *designed* failure rate is 0%, two breaches in one month is a control failure, not a discipline anecdote.

**Control — the answer to "what mechanism, not willpower":** see §5. The short version: **the only real mechanism is one his broker enforces.** Everything routed through his own hands at the moment of the trade is willpower wearing a different hat.

---

#### **C-4 — The system has no position ledger. A trailing-stop strategy with no position tracking.**

**Evidence.** No file in `strategy/v6.4/` maintains state between runs. The bot is stateless request/response. The scanner writes `daily_strong_signals.csv` (candidates, not holdings) and exits. `open_positions` exists *only* inside the backtest's simulation loop. There is no holdings file, no open-position list, no reconciliation.

**Why this is critical rather than merely inconvenient.** Engine 2's entire risk model is a **trailing stop** — `移動⽌損: 每⽇收市後 = 最⾼價 − 3×ATR,只升不降` (bot L427). That is a *daily manual task* with no tracker, no reminder, and no record of what the current stop should be. If he does not recompute it by hand every evening, and does not update the resting order at the broker, the position's actual protection silently diverges from its designed protection. The strategy's stated edge depends entirely on a chore that nothing checks was done.

Every portfolio-level control I would otherwise impose — heat, concurrency, cash floor, VaR, drawdown, single-name concentration — is **unimplementable until a position ledger exists.** This is why it is the first code upgrade in §5.

**Control.** `positions.yaml`: ticker, entry date, entry price, shares, initial stop, current trail, highest close since entry, engine, tier, decision note. Plus a `/portfolio` command in the bot returning open count, gross exposure %, total heat %, cash %, and any position whose trail has not been updated in more than one session.

---

### HIGH

---

#### **H-1 — The chart he actually trades from implements only Engine 1 — the engine his own code labels unfit.**

**Evidence.** `dual_engine_v6_4_tiers.pine` is titled "Swing V6.4 三級訊號" and the file is named *dual* engine. It is not dual. Line 38: `isRange = adxVal < 25`. Line 89: `basic = bull and isRange and score >= 0.55 and ...`. The `score` on L59 is built purely from `s1..s5` = RSI14, RSI2, price-vs-MA20, 10-day return, volume ratio — **the mean-reversion score**. There is no ADX≥25 branch, no `trend_score`, no `3×ATR` trailing stop, no Engine 2 anywhere in the 240 lines. I grepped for all four; only `rVal >= 3.0` matches, which is an R-multiple, not the ATR multiplier.

**Why this is HIGH.** His own tooling states the ranking unambiguously and in two places:
- Engine 1: `[OOS偏弱,觀察狀態]` — *OOS weak, observation status* (bot L365)
- Engine 2: `[OOS已驗證,主⼒]` — *OOS validated, the main force* (bot L412, scanner L145)

> **The visual tool he trades from can only ever plot signals from the engine he has himself designated as unfit for capital. Engine 2, his stated main force, is invisible on his charts.**

Every alert (`alertcondition`, L235–240) fires on Engine 1 only. If he trades what he sees, he is trading the deprecated engine — and the trades he *is* taking may be exactly the ones his OOS work told him not to take. This finding alone would explain a live/backtest performance gap without any of the others being true.

**Control.** Either implement the Engine 2 branch in the Pine, or rename the file, the indicator title and the info panel to `Engine 1 (Mean Reversion) — OBSERVATION ONLY, NOT FOR CAPITAL`. Second option is a five-minute fix and I would take it today.

---

#### **H-2 — Stop-width thresholds are fragmented across four values; one is dead code; one guards a rule that was never validated.**

**The complete threshold map**, verified line by line:

| File | Engine | Threshold | Line | Status |
|---|---|---|---|---|
| `dual_engine_v6_4_tiers.pine` | E1 (only engine present) | **15%** | L73 `stopTooWide = riskPctVal > 15` | **LIVE on the chart — but absent from the E1 backtest** |
| `telegram_swing_bot.py` `trend_plan()` | E2 | **12%** | L156 `if risk_pct > 12: return None` | **LIVE and matches both backtests** ✓ |
| `telegram_swing_bot.py` `MAX_STOP_PCT` on E2 | E2 | 15% | L432 | **DEAD CODE — unreachable** |
| `telegram_swing_bot.py` `MAX_STOP_PCT` on E1 | E1 | **15%** | L398 | **LIVE — and unvalidated** |
| `oos_validation.py` `run_engine1()` | E1 | **NONE** | L187–217 | **No stop-width filter of any kind** |
| `oos_validation.py` `run_engine2()` | E2 | **12%** | L239 | Validated ✓ |
| `momentum_pit_backtest.py` | E2 | **12%** | L265 | Validated ✓ |
| `dual_engine_v6_4.py` `check_guardrails()` | ? | **UNKNOWN** | file absent | **Potential fourth value — see H-6** |

**The dead code, proven.** `trend_plan()` returns `None` whenever `risk_pct > 12`. The bot then does `if tplan is None: blocks.append(...)`. So by the time execution reaches L432 — `if tplan["risk_pct"] > MAX_STOP_PCT` — `risk_pct` is guaranteed ≤ 12, and 12 is never > 15. **That branch can never fire.** It is decorative. Harmless in itself, but it means the file *reads* as though Engine 2 is protected at 15% when it is actually protected at 12% somewhere else entirely. Anyone auditing this file — including him, in six months — will draw the wrong conclusion.

**The genuine break, and it runs in both directions.** Engine 1 blocks stops wider than 15% live. `run_engine1()` in the OOS validation applies **no stop-width filter at all** — it accepts any trade with `risk > 0`. Therefore:
- The backtested E1 population **includes** trades with 15%+ stops that live would refuse; and
- The live E1 population is a filtered subset that was **never separately measured**.

> **The E1 EV he is relying on was measured on a different population of trades than the one his system will actually take.** The 15% guardrail is not conservative-but-untested; it is *untested in an unknown direction*. Filtering out the widest-stop trades could improve EV (they are the most volatile) or destroy it (wide-stop trades in a mean-reversion system are often the deepest, highest-payoff reversions). Nobody knows, because the test was never run.

**Control.** One constant, one file, imported everywhere:
```python
# risk_config.py — single source of truth
MAX_STOP_PCT_ENGINE1 = 15.0
MAX_STOP_PCT_ENGINE2 = 12.0
```
Delete the dead branch. Re-run `run_engine1()` **with** the 15% filter applied and compare EV to the unfiltered result. If E1's edge does not survive its own live guardrail, retire E1 — which, given H-1, would also resolve what the Pine should display.

---

#### **H-3 — yfinance is a single point of failure for entry, stop and size simultaneously, with silent failure modes. Demonstrated today.**

**Evidence — the demonstration.** Preparing this review I installed yfinance 1.5.2 and requested one year of daily bars for all 38 pool names plus SPY. **All 39 requests failed** (HTTP 403 at the egress proxy). yfinance reported them as `possibly delisted; no price data found`.

Now trace that same failure through `daily_strong_signals.py`. The per-ticker loop ends:
```python
        except Exception:
            continue
```
**Every one of those 39 failures is swallowed silently.** The summary block counts only *signals*, never *coverage* — there is no `scanned / failed / total` anywhere in the output. The scan would have printed:

> `今⽇無強訊號 —— 唔使交易,閂機做第⼆啲嘢。`
> *(No strong signals today — no need to trade, shut down and go do something else.)*

...and, worse, the reassuring line beneath it: `(⼤部分⽇⼦冇強訊號係正常,唔好焦慮)` — *most days have no strong signals, this is normal, don't be anxious.*

> **A total data-layer outage is indistinguishable from a quiet market, and the system actively reassures him that the silence is normal.** This is the most insidious failure mode in the review: it is invisible, it is comforting, and it looks exactly like correct behaviour. If the scanner covers 6 of 38 names for a month he will never know.

**The other three data defects:**

1. **No staleness check.** Grep for `index[-1]`, `datetime.now`, date validation in the *signal path*: nothing. Every decision uses `df.iloc[-1]` with **no verification that the last bar is recent.** On a holiday, a partial feed, or a cached response, the bot will price a trade off a stale bar and print a stop level with full confidence and no warning.
2. **No sanity band.** No check that today's close is within a plausible distance of yesterday's, that ATR is non-degenerate, or that the price is positive-and-sane. A single bad print sets **entry, stop and share count all at once** — and because share count is `risk_budget / (entry − stop)`, a corrupted stop produces a corrupted *position size*, not just a corrupted display. **This is firm lesson L-002 exactly** (a bad vendor print produced a fictitious event in the MU report). We blacklisted that vendor firm-wide. This system has a single unvalidated vendor and no cross-check.
3. **No dependency pinning.** No `requirements.txt`, no `pyproject.toml`, no lockfile anywhere in the repo. The `ta` library's ADX and ATR implementations have changed across versions. **A silent `pip install --upgrade` changes every ATR, therefore every stop, therefore every share count, therefore every position size — with no error and no diff.**

**Control.** A data-integrity gate that every signal must pass before a plan is rendered:
```
assert last_bar_date >= last_expected_session      # staleness
assert 0 < close < 10 * median(close[-20:])        # sanity band
assert atr > 0 and atr < 0.5 * close               # degenerate ATR
print(f"scanned {ok}/{len(TICKERS)}, failed: {failed}")   # coverage — never silent
if ok < 0.9 * len(TICKERS): print("⚠️ DATA INCOMPLETE — TODAY'S SCAN IS NOT VALID")
```
Plus: pin every dependency, and cross-check the last close against a second free source (Stooq is adequate) before any plan is rendered. Reject on a disagreement wider than 1%.

---

#### **H-4 — Correlation: the pool breaches the correlated-cluster limit before a single signal fires, and momentum selection makes it worse.**

**Composition of the 38-name pool** (`telegram_swing_bot.py` L51–56, counted exactly):

| Cluster | Names | Count |
|---|---|---:|
| Semiconductors | NVDA, AVGO, AMD, QCOM, MU, INTC | 6 |
| Mega-cap tech platforms | AAPL, MSFT, GOOGL, AMZN, META, TSLA | 6 |
| Software / internet | PLTR, CRM, ADBE, NFLX, SHOP, UBER | 6 |
| Crypto-beta | COIN, MSTR | 2 |
| **Tech-and-crypto complex** | | **20 / 38 = 52.6%** |
| Financials / payments | JPM, BAC, GS, V, MA | 5 |
| Consumer | COST, WMT, MCD, NKE, SBUX | 5 |
| Healthcare | UNH, JNJ, PFE, LLY | 4 |
| Energy | XOM, CVX | 2 |
| Industrials | CAT, BA | 2 |

> **A uniformly random draw from this pool has an expected tech-complex weight of 52.6%, against `max_sector: 0.35` and `max_correlated_cluster: 0.40`. The universe breaches the concentration limits before any signal logic runs.** Counting V and MA as payments-technology takes it to 57.9%.

**And the selection mechanism amplifies it — this is the part the "1% per trade" framing hides.** Engine 2 requires `ADX ≥ 25`, `DI+ > DI−`, a fresh 20-day high, and scores maximum when `close > MA20 > MA50 > MA200` and price is within 1% of its 60-day high. That is not a stock filter; **it is a leadership filter.** The set of names satisfying "breaking to new highs with a strong trend, in a bull tape" is, by construction, whatever factor is currently leading the market. Signals therefore do not arrive independently — they **arrive in clusters, all from the same factor, on the same days.**

> Nominal diversification across ten correlated names is concentration in disguise. The system counts positions; the market counts factors.

**Effective independent bets.** For N equicorrelated positions, N_eff = N / (1 + (N−1)ρ):

| N positions | ρ=0.0 | ρ=0.3 | ρ=0.5 | ρ=0.65 | ρ=0.8 |
|---:|---:|---:|---:|---:|---:|
| 3 | 3.00 | 1.88 | 1.50 | 1.30 | 1.15 |
| 5 | 5.00 | 2.27 | 1.67 | 1.39 | 1.19 |
| **10** | 10.00 | **2.70** | **1.82** | **1.46** | **1.22** |
| 20 | 20.00 | 2.99 | 1.90 | 1.50 | 1.23 |

**⚠️ ASSUMPTION LABEL: ρ is a scenario, not a measurement.** I could not compute the pool's actual correlation matrix — the egress block in §0 prevented it. The correct ρ for *this* pool under *stress* is an open item and is commissioned in §7 (CL-5). What I can state without measurement is the structural fact: these are the same six semiconductor names, the same six mega-cap platforms, and two crypto proxies, and in a drawdown they de-rate on one narrative.

**How the 1% rule misleads — portfolio loss dispersion** = 1% × √(N + N(N−1)ρ):

| N | independent (ρ=0) | ρ=0.3 | ρ=0.5 | ρ=0.65 | ρ=0.8 | all stops hit |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 2.24% | 3.32% | 3.87% | 4.24% | 4.58% | 5% |
| **10** | **3.16%** | 6.08% | 7.42% | 8.28% | **9.06%** | **10%** |
| 20 | 4.47% | 11.58% | 14.49% | 16.34% | **18.00%** | **20%** |

> **This is the punchline.** With ten positions he *feels* diversified and the arithmetic of independence says 3.16%. At ρ=0.8 — entirely plausible for six semis in a semi drawdown — those ten positions behave like **1.22 independent bets**, and the "diversification" reduces his worst case from 10% only to **9.06%**. He has taken on ten positions' worth of commission, ten positions' worth of monitoring burden, and ten positions' worth of trailing-stop chores, in exchange for **9% of one position's worth of risk reduction.**

At N=20 and ρ=0.8 the loss dispersion is **18%**, against a 20% total drawdown budget — a single bad fortnight consumes essentially the whole budget.

**Control.** A cluster cap enforced at entry, requiring the position ledger from C-4: `max 2 open positions per cluster`, `max 40% of gross exposure in the tech-and-crypto complex`. And measure the actual stressed ρ before setting the final numbers.

---

#### **H-5 — The bear filter blocks new entries but does not reduce existing exposure. That is opportunity control, not risk control.**

**Evidence.** `SPY > MA200` is evaluated **only at entry**. In `run_engine2()` (oos L227) and in `momentum_pit_backtest.py` (L247, `if is_bull:` wraps *only* the new-entry loop), the bull flag never reappears in the position-management block above it. Open positions are managed **solely** by the 3×ATR trailing stop.

**Consequences, in order of severity:**

1. **Existing risk is untouched by the "standstill".** `熊市停⼿` means *stop trading in a bear market*, and he reasonably reads that as protection. It is not. It stops him *buying*. Everything he already owns rides into the bear market on a trailing stop.
2. **`TREND_MAX_HOLD = 60`.** A position opened the session before SPY breaks its MA200 can be held for **60 more trading days — roughly three months — deep into a bear market**, by a system he believes has "stood down".
3. **The asymmetry is exactly backwards.** The filter removes 100% of the upside (no re-entries) while removing 0% of the existing downside. Of the four possible designs, this is the worst one.
4. **Re-entry is doubly delayed.** After a whipsaw, Engine 2 needs a *fresh 20-day high* to re-enter. Following a sharp shakeout no pool name may print one for weeks. So the cost of a whipsaw is not the crossing — it is the crossing **plus** the 20-day-high re-arming lag, during the sharpest part of the recovery.

**Is the filter timely? Structurally, no — and this is definitional, not empirical.** SPY crosses below its MA200 precisely when the index falls to the *mean of the prior 200 sessions*. In any market that rose over those 200 sessions, the index must **already have given back that entire advance** before the filter fires. The filter cannot warn; it can only confirm. It is a lagging indicator by construction, used here as though it were a leading one. There is also **no buffer and no confirmation period** — a single close either side toggles the entire system on and off, so a market oscillating around its 200-day average (which is exactly what markets do at inflection points) maximises the flip count at the worst possible moment.

**⚠️ ASSUMPTION LABEL:** I have deliberately not stated a whipsaw *cost* in percent. That number must be measured, not asserted, and the egress block prevented me from measuring it. The measurement is fully specified in §5, item 9, and uses data `momentum_pit_backtest.py` already downloads.

**Control.** Three changes:
1. **Add an exit side.** On a bear flip: no new entries (as now) **and** tighten all trails from 3×ATR to 1.5×ATR, **and** cut `TREND_MAX_HOLD` to 10 sessions for open positions. Now "standstill" means something.
2. **Add a buffer.** Require `SPY < MA200 × 0.98` to turn off and `SPY > MA200 × 1.02` to turn back on, or require 3 consecutive closes. Kills single-day whipsaws.
3. **Measure it** before trusting it (§5.9).

---

#### **H-6 — The daily scanner's core logic lives in a file that does not exist in the repo, and has a confirmed signature divergence from the bot.**

**Evidence.** `daily_strong_signals.py` L31–44 imports `TICKERS`, `calc_indicators`, `classify`, `mr_score`, `mr_plan`, `trend_score`, `trend_plan`, `check_guardrails`, `position_plan`, `get_days_to_earnings`, `MR_SCORE_MIN`, `TREND_SCORE_MIN`, `MIN_R` from `dual_engine_v6_4`. **That module is not in the repository.** The scanner cannot run from this directory and its true behaviour cannot be audited.

**The divergence is already provable from what is here.** In `telegram_swing_bot.py` L115–149, `trend_score(row)` returns a **scalar** (`return round(min(score, 1.0), 4)`). In `daily_strong_signals.py` L124 it is unpacked as a **tuple**: `sc, _ = trend_score(row)`.

> These are two different functions with the same name and incompatible signatures. **The candidate generator and the confirmation tool are running different code.** The scanner tells him what to look at; the bot tells him whether to take it. If they disagree, nothing detects it.

Similarly, `check_guardrails(tk, df, risk_pct)` exists only in the missing module — so there is a **fourth, unknown stop-width threshold** in the live signal path (H-2). And `classify` vs the bot's `classify_route` is another name mismatch. The file header claims `直接引⽤ V6.4 嘅邏輯(確保完全⼀致,改V6.4呢度⾃動跟)` — *directly imports V6.4's logic so they're guaranteed identical.* The signature mismatch proves they are not.

**Control.** Bring `dual_engine_v6_4.py` under review and into the repo. Then invert the dependency: **the bot and the scanner must both import from one shared engine module.** Neither should define its own copy of `trend_score`. Add a startup assertion that the two agree on a fixed test row.

---

#### **H-7 — The bot renders a complete, actionable trade plan for instruments it is simultaneously prohibiting — with a currency-corrupted share count.**

**Evidence — the flow.** For a HK ticker the bot computes indicators, route, score, stop, target, R-value **and** `建議股數`, appending all of it to `lines` (L370–392), *then separately* appends the prohibitions to `blocks`. Both are printed. The user sees a fully specified, professional-looking trade plan with a specific share count, followed by the reasons he must not take it.

**Evidence — the currency bug.** `position_plan()` (L167–175) has **no currency awareness**:
```python
risk_usd = ACCOUNT_HKD * RISK_PCT / 100 / USD_HKD   # = 12.82 USD
shares   = int(risk_usd // per_share)               # per_share is in the QUOTE currency
```
For a `.HK` ticker, `entry` and `stop` come from Yahoo in **HKD**, so `per_share` is in **HKD** while `risk_usd` is in **USD**. The division mixes currencies. **HK positions are under-sized by a factor of 7.8.**

**Why this matters beyond the (blocked) HK path — it contaminates the behavioural record.** The 7/13 trade was `1888.HK`. If the "11x oversize" figure was measured against a suggestion produced by this code path, that suggestion was **7.8x too small**:

- Buggy suggestion ≈ 500 / 11 ≈ **45 shares**
- Currency-correct suggestion ≈ 45 × 7.8 ≈ **354 shares**
- Actual 500 shares vs a correct suggestion ≈ **1.4x oversize, not 11x**

**⚠️ ASSUMPTION LABEL:** this holds *conditional on* the 7/13 suggestion having been generated by `position_plan()` on a `.HK` ticker. I cannot verify that; he can, in seconds.

> If that condition holds, then **one of the two breaches he has been reproaching himself for was substantially a code defect wearing the costume of an indiscipline problem.** 1.4x oversize on a prohibited instrument is still a breach — the pool guardrail and the HK prohibition were both real and both overridden. But "11x" is not the right number, and a risk function that lets a false self-indictment stand is not doing its job. The 7/18 BAC breach (100x, US-listed, correct currency) is entirely real and is unaffected by this.

**Control.** Two changes: (1) make `position_plan()` currency-aware, or refuse to size any non-USD instrument; (2) **when an instrument is prohibited, print the prohibition and nothing else.** Do not render a stop, a target, an R-value or a share count for something the system has refused. A complete trade plan is an invitation; printing one under a "you may not do this" header manufactures exactly the temptation the guardrail exists to remove.

---

### MEDIUM

---

#### **M-1 — Transaction costs are entirely unmodelled, and at this account size they are decisive.**

**Evidence.** Grep for `commission`, `slippage`, `fee`, `spread` across all five files: **no matches.** `run_engine2()` returns `(exit_price - entry) / entry * 100`; `momentum_pit_backtest.py` is identical. **Every reported EV — +1.325%, +1.497% — is gross of commission, slippage and spread.**

**Quantification.** Using the cited +1.325% gross EV, breakeven commission is EV × notional ÷ 2 legs:

| Position notional | Gross EV per trade | **Breakeven commission, per side** |
|---:|---:|---:|
| $50 | $0.66 | **$0.33** |
| $100 | $1.32 | **$0.66** |
| $128 (the 10% cap) | $1.70 | **$0.85** |
| $200 | $2.65 | **$1.32** |

> **If he pays more than roughly US$0.66–1.00 per side, the strategy has no edge at this account size.** Not a reduced edge — no edge. This is the single most consequential unknown in the review and it is a five-minute check against his broker's schedule.

Zero-commission US-equity brokers (Webull/moomoo/Futu — and `微⽜模擬倉` in the scanner's output suggests Webull) clear this comfortably. Any broker with a fixed minimum ticket does not: a HK$15 minimum ≈ US$1.92 per side ≈ **2.9x the entire gross edge on a $100 position.**

**Control.** Add a `COMMISSION_PER_SIDE` constant and a `SLIPPAGE_BPS` constant to both backtests, populate them from his actual schedule, and re-read the OOS verdict net. If net EV ≤ 0 the system does not trade, regardless of what the gross number says.

---

#### **M-2 — Integer rounding silently discards up to 45% of the risk budget, and therefore up to 45% of the edge.**

**Evidence.** `shares = int(risk_usd // per_share)` — floor division on a US$12.82 budget. At this account size the quantisation is severe:

| Per-share risk | Shares | Risk actually taken | % of account | **Budget utilised** |
|---:|---:|---:|---:|---:|
| $6.41 | 2 | $12.82 | 1.00% | 100.0% |
| $7.00 | 1 | $7.00 | **0.55%** | **54.6%** |
| $8.00 | 1 | $8.00 | 0.62% | 62.4% |
| $10.00 | 1 | $10.00 | 0.78% | 78.0% |
| $12.82 | 1 | $12.82 | 1.00% | 100.0% |
| **$12.83** | **0** | **$0** | — | **BLOCKED** |

Realised risk oscillates between **0.55% and 1.00%** purely on rounding — invisible to him, uncorrelated with conviction, and driven by nothing but where the ATR happens to land.

**Direction of the error is safe; the consequence is not.** It always errs *small*, so it never breaches the risk limit. But the backtests assume exact fixed-fractional 1% deployment. **Live, average budget utilisation is materially below 100%, so the realised portfolio return is a corresponding fraction of the backtested return — while the volatility of outcomes rises**, because he is holding fewer, lumpier positions than the smooth model assumes.

**Control.** No fix at this account size — it is arithmetic. Two responses: (1) report realised risk % alongside the share count so he can *see* the utilisation (`建議股數: 1股 — 實際風險 0.55%,預算用了 55%`); (2) recognise it as a genuine argument for a larger account (§4.3), which is a capital decision for the Owner, not a code change.

---

#### **M-3 — The speculative-stock guardrail is enforced in the bot, cosmetic on the chart, worded as a suggestion, and the pool contains names it exists to exclude.**

**Evidence — inconsistent enforcement.**
- Bot (L444–448): `if is_spec: blocks.append(...)` — a **hard block**.
- Pine (L77, L225): `isSpec` is computed and rendered into the info-panel table at `t.cell(1,10)`. It **does not appear in the `basic`/`strong`/`premium` booleans** (L89–92). On the chart it is **decoration**.

> The tool he trades from (H-1) does not enforce this guardrail at all.

**Evidence — the wording.** The block reads `投機股標記 → 加倍⼩⼼或跳過` — *speculative flag → be doubly careful **or** skip.* That is a hard block wearing the language of a suggestion. It offers "be careful" as a compliant alternative to "skip". Given C-3, guardrail text that supplies its own opt-out is a defect, not a nicety.

**Evidence — the pool contradicts the guardrail.** `check_spec()` flags any name whose 126-day high/low ratio ≥ 2.0. **MSTR and COIN are both in the 38-name pool** and both are structurally likely to trip it. The universe deliberately includes names the guardrail is designed to exclude — so the system's routine state is "signal generated, then blocked", training him to read the speculative block as noise.

**Control.** Make `isSpec` a genuine gate in the Pine (add `and not isSpec` to `basic`). Change the wording to `投機股 → 跳過` — one instruction, no alternative. Then decide deliberately: either remove MSTR/COIN from the pool, or exempt them explicitly with a written rationale. Do not leave the contradiction to be resolved in the moment.

---

#### **M-4 — A data outage is reported to the user as a bear market.**

**Evidence.** `check_market_regime()` returns `None, "無法取得...數據"` on any exception (L80–81) and on insufficient data (L75–76). The caller does `is_bull, regime_msg = check_market_regime(market)` then `if not is_bull: blocks.append("熊市環境 → 系統停⼿")`. **`None` is falsy**, so a network failure, a rate-limit, or a short SPY series is rendered to the user as **"BEAR MARKET → SYSTEM STANDS DOWN"**.

**Assessment.** Fail-*safe* in direction — it blocks rather than permits, which is correct. But it is fail-*confusing* in content, and that has a behavioural cost: he will occasionally see "bear market" on a day he knows perfectly well the market is up. **The lesson he learns is that the bear-market block is unreliable** — and that is precisely the block that must retain its authority when it fires for real.

Related fragility: both the bot (L72) and the scanner (L75) fetch `period="1y"` (~251 sessions) and then compute `rolling(200)`, leaving only ~52 valid MA200 values. Functional, but with almost no margin — a slightly short return silently degrades to the `None` path above. `momentum_pit_backtest.py` downloads from 2018 and `oos_validation.py` uses `4y`. **Three different regime-history windows across four files.**

**Control.** Return a three-state regime — `BULL` / `BEAR` / `UNKNOWN` — and give `UNKNOWN` its own distinct message: `⚠️ 無法確認大市環境(數據問題)→ 今日唔做`. Still blocks; no longer lies about why. Fetch `period="2y"` for the MA200 in both live scripts.

---

#### **M-5 — Residual survivorship bias, with a silent degradation path.**

**Evidence.** `get_universe()` reads **today's** S&P 500 constituents from Wikipedia and applies them across 2019–2026. The file discloses this honestly (L28–30) and I credit that. But the fallback is the problem:
```python
    except Exception as e:
        print(f"  ⚠ ⽤後備名單 {len(FALLBACK)} 隻（{e}）\n")
        return FALLBACK
```
`FALLBACK` is a **hand-picked 120-name list of today's known winners** — the single most survivorship-biased universe possible, and materially worse than the S&P 500 constituent list it replaces.

The warning prints once and is immediately buried under `下載歷史數據(可能要幾分鐘)...` and hundreds of progress lines. **Nothing in the final results block records which universe was used.** And under the network conditions I observed today, the Wikipedia fetch would fail — meaning the fallback path is not hypothetical.

**Control.** Record the universe source in the results header and in the output CSV. Better: **abort** rather than fall back — a backtest silently run on a winners-only universe is worse than no backtest, because it produces a confident number.

---

#### **M-6 — The 10% cash floor is unenforced, and the system will invest to zero cash.**

**Evidence.** No file reads or tracks a cash balance. With no concurrency cap (C-2) and no notional cap (C-1), entries continue until orders stop filling.

**Quantification** — where the account actually runs out, from the §1.1 identity:

| Stop width | Notional each | Max positions before cash < 10% |
|---:|---:|---:|
| 4% | 25.0% | **3** |
| 6% | 16.7% | **5** |
| 8% | 12.5% | **7** |
| 10% | 10.0% | **9** |
| 12% | 8.3% | **10** |

> The system self-limits to roughly **3–10 positions — but only because it runs out of money, not because any rule says stop.** "Bounded by insolvency" is not a risk control. And note this bound is far below the 50 the backtest assumes (C-2).

**Control.** Enforce the cash floor explicitly in the entry gate, which requires the C-4 ledger.

---

### LOW

| ID | Finding | Evidence | Control |
|---|---|---|---|
| **L-1** | `BOT_TOKEN = "在這裡貼上你的TOKEN"` is a placeholder, so **the reviewed file is not the running file.** I cannot certify what actually executes, and every fix must be hand-applied to a divergent local copy. Compounding: **the repo has no `.gitignore`**, so once the real token is pasted, a commit publishes a live bot credential. | bot L37; repo root | Move the token to an environment variable (`os.environ["BOT_TOKEN"]`); add `.gitignore`; bring the running file under version control so review and live are the same artefact. |
| **L-2** | **No authorisation on `chat_id`.** The bot replies to anyone who messages it. Telegram bots are discoverable by username. Financial risk is low (it computes from public data) but it leaks his risk budget — `建議股數` back-solves to his account size — and is a free rate-limit exhaustion vector. | bot L507–529 | `if chat_id != MY_CHAT_ID: continue` |
| **L-3** | `USD_HKD = 7.8` hardcoded. The peg band is 7.75–7.85, so the maximum sizing error is ~1.3% — immaterial today, silently wrong if the peg is ever revised. Note also the account is denominated in HKD while all risk is taken in USD: unhedged, but bounded by the peg. | bot L44; Pine L22 | Acceptable as-is. Add a comment stating the peg-band assumption so it is a decision, not an accident. |
| **L-4** | **Guardrail numbering is inconsistent within a single file:** `check_spec` is "護欄3" (L177), `position_plan` is "護欄4" (L168), the pool check is "護欄6" (L345), and `MAX_STOP_PCT` is unnumbered (L49). There is no guardrail 1, 2 or 5. | bot, four locations | Renumber once, in one place. He cannot audit "did every guardrail run" against a list that does not exist. |
| **L-5** | Bot runs only while the PC is on (`關電腦=bot離線`). For a *query* tool this is fail-safe — no answer means no trade. The real exposure is the absence of stop *monitoring*, captured in C-4. | bot L24–26 | Covered by C-4. Do not host this in the cloud until the guardrails are real; a 24/7 signal source attached to unenforced limits increases risk. |

---

## 4. Direct answers to the seven questions

### 4.1 Concurrent position risk

**No cap exists in any file** (grep-verified). The momentum backtest permits up to **50 simultaneous positions** from its 50-name pool.

- **Stated worst-case heat:** 50 × 1% = **50% of the account** — **2.5x the entire 20% drawdown budget**, in a single simultaneous-stop event.
- **Implied gross exposure:** 417% (at the widest 12% stop) to 833% (at a 6% stop) — **4.2x to 8.3x leverage**, against `leverage: none`.
- **Therefore the backtest is not fundable in a cash account at any account size.** Its per-trade EV may be sound; any *portfolio* return inferred from it is not achievable without margin.
- **And it is not merely a theoretical maximum.** Momentum entries cluster by construction (H-4) — they all require a 20-day high in a bull tape — so simultaneity is *positively correlated with the factor*, arriving exactly when correlation is highest and diversification is worth least.
- **Realistically**, capital exhaustion caps him at 3–10 positions (M-6), i.e. 3–10% heat. Tolerable — but achieved by accident, and it means his live book will look nothing like the backtested one.

### 4.2 Correlation and effective bets

The pool is **52.6% tech-and-crypto complex by name count** (20/38), against `max_sector: 0.35` and `max_correlated_cluster: 0.40`. **The universe breaches both limits before any signal fires.** Engine 2's leadership filter (ADX≥25 + 20-day high + full MA stack) concentrates it further, because it selects whatever factor is currently leading.

At ten positions and ρ=0.8, **N_eff = 1.22** — ten positions, one-and-a-fifth bets. The "1% risk per trade" rule misleads because it is a *per-position* statement being read as a *portfolio* statement. Ten positions promise 10 × 1% spread across ten outcomes; at high ρ they deliver something very close to 10% arriving as **one** outcome. The diversification benefit at ρ=0.8 shrinks the worst case from 10% to 9.06% — a 9% reduction in risk for a 10x increase in positions, commissions and daily trailing-stop chores.

**ρ is a labelled scenario throughout, not a measurement** (§0). Measuring it is CL-5.

### 4.3 Is the system operable at HK$10,000? — the plain answer

**Yes, it is mathematically operable — but only inside a narrow band, and it cannot express the strategy it is validating.** Three separate constraints:

**(a) Price ceiling.** Maximum share price at which `shares ≥ 1`, by stop width:

| Stop width | @1% risk ($12.82) | @0.5% risk ($6.41) |
|---:|---:|---:|
| 5% | $256.41 | $128.21 |
| 7% | $183.15 | $91.58 |
| 8% | $160.26 | $80.13 |
| 10% | $128.21 | $64.10 |
| 12% (E2 cap) | $106.84 | $53.42 |

**(b) But the binding constraint is concentration, not affordability.** A single share of *any* stock above **US$128.21** is already more than 10% of the account. So above $128.21 the system says "buy 1" while firm policy says "buy 0" — and the system has no idea the conflict exists (C-1). The affordability guardrail he built (`買唔起` at `sharesCanBuy < 1`) fires at $183 on a 7% stop; **the concentration limit should have fired at $128.21.** His guardrail is roughly 43% too permissive, in the dimension that governs gap risk.

**(c) The rounding tax.** Up to 45% of the risk budget is discarded to integer truncation (M-2), so realised deployment — and therefore realised return — is materially below the modelled 1%.

**So, plainly:**

> The account is **not too small to be safe**. It is too small to be **efficient**, and far too small to **replicate what was validated**. The design assumes a portfolio of many small concurrent momentum positions averaging toward a +1.3%/trade expectancy. The capital supports 3–7 positions, ~55–100% budget utilisation, and a price-restricted subset of the pool.
>
> **At this size the account gets the strategy's volatility without the strategy's averaging.** Single-name outcomes will dominate, and the large-sample EV he is relying on is a number he cannot reach a large sample of quickly — at 3–7 concurrent positions and holds up to 60 sessions, plausibly 30–60 trades a year, so ~2 years to reach 100 trades. His own code already flags this: `if oos_stats["n"] < 30: 統計說服⼒有限`.

That is not an argument to abandon the system. It is an argument to (i) stop expecting the backtest's smoothness, (ii) treat this as a **process-validation** account rather than a return-generating one, and (iii) recognise that the honest fix is more capital — **but only after the controls in §7 exist. Adding capital to an uncontrolled system multiplies the exposure created by the 7/18 event; it does not dilute it.** Controls first, capital second. That ordering is not negotiable.

### 4.4 The 15% vs 12% inconsistency

Full map in H-2. Summary:

- **Live and validated:** 12% on Engine 2 (`trend_plan()` — matches both backtests). ✓
- **Live and UNVALIDATED:** 15% on Engine 1 in the bot and in the Pine. `run_engine1()` in the OOS validation applies **no stop-width filter at all**.
- **Dead code:** the 15% check on Engine 2 in the bot is unreachable — `trend_plan()` already returned `None` at 12%.
- **Unknown:** `check_guardrails()` in the missing `dual_engine_v6_4.py` — a possible fourth value in the live scanner path (H-6).

**What breaks:** the E1 population that was backtested ≠ the E1 population that will trade. The backtest included wide-stop trades that live will refuse, and the filtered subset was never separately measured. **The E1 edge is unvalidated in an unknown direction** — filtering out the widest stops might improve EV or might remove the deepest, highest-payoff reversions. Given H-1 (the chart plots *only* Engine 1), this is the engine he is most likely to actually trade.

### 4.5 Bear-market standstill

**It is opportunity control, not risk control.** See H-5. Entry-only; existing positions ride into the bear on a 3×ATR trail for up to 60 more sessions. It removes 100% of the upside and 0% of the existing downside.

**On timeliness:** an MA200 cross is a lagging confirmation *by construction* — the index must fall to the mean of the prior 200 sessions before it fires, so in any prior uptrend the advance is already surrendered. There is no buffer and no confirmation period; a single close toggles the system, so an index oscillating around its 200-day average maximises flips at exactly the worst moment. Whipsaw cost is **not stated here because it must be measured** (§5.9).

### 4.6 Behavioural risk — the mechanism

See C-3 and §5. The governing principle:

> **Any control that routes through his own hands at the moment of the trade is willpower wearing a different hat.** The two breaches happened *after* the bot had already told him no. Adding a louder warning, a bigger red font, or another written promise adds another instance of the thing that has already failed twice.

The mechanism must be **external and prior**: a cash-only brokerage account with margin disabled. In a cash account, 300 shares of BAC at ~9x the balance is not a decision he declines — it is an order the broker **rejects**. One phone call, no code, immediate effect, and it addresses the single largest realised risk in this system, which is not the strategy but the 9x-leverage event that has already occurred.

Note also H-7: part of the 7/13 self-reproach may be a currency bug, not indiscipline. Fix the code before drawing further conclusions about the man.

### 4.7 Single points of failure

| SPOF | Severity | Assessment |
|---|---|---|
| **No position ledger / no stop monitoring** | **CRITICAL (C-4)** | The real SPOF. A trailing-stop strategy whose stop updates are an untracked manual chore. |
| **yfinance sole source** | **HIGH (H-3)** | Sets entry, stop *and size* from one unvalidated feed. No staleness check, no sanity band, no coverage count, no cross-check, no version pins. Silent failure demonstrated today: 39/39 tickers failed and the scanner would have reported "no signals, this is normal". |
| **Missing `dual_engine_v6_4.py`** | **HIGH (H-6)** | Scanner logic unreviewable; signature divergence already proven. |
| **BOT_TOKEN placeholder / no `.gitignore`** | LOW (L-1) | Review-vs-live divergence; credential-in-source once populated. |
| **PC-on dependency** | LOW (L-5) | Fail-safe for a query tool. Do **not** move to the cloud until the guardrails are real. |

---

## 5. UPGRADES — ranked by risk-reduction impact

> **Do #1 first. It is not code, it takes one phone call, and it is the only item on this list that cannot be overridden in the moment.**

| # | Upgrade | Fixes | Effort | Impact |
|---|---|---|---|---|
| **1** | **Cash-only brokerage account, margin disabled in writing.** Segregate the trading capital from all other funds. In a cash account the 7/18 BAC order is *physically impossible* — the broker rejects it. | **C-3** | One phone call | **Highest. Nothing else on this list is a mechanism; they are all still controls he administers himself.** |
| **2** | **Position ledger** — `positions.yaml` + a `/portfolio` command reporting open count, gross exposure %, total heat %, cash %, and any stale trailing stop. | **C-4**, enables 3/4/9 | Half a day | **Highest among code changes.** Every portfolio control is blocked on this. |
| **3** | **Hard caps in `position_plan()`**: notional ≤ 10% of account (return an explicit BLOCK, and surface which limit bound); `MAX_OPEN_POSITIONS = 5`; `MAX_PORTFOLIO_HEAT = 5%`; cluster cap ≤ 2 per sector. Read from **one** `risk_config.py`. | **C-1, C-2, H-4, M-6, H-2** | A few hours | Very high — closes the largest quantified gap. |
| **4** | **Portfolio-level backtest.** Rebuild the equity curve from the `momentum_pit_trades.csv` he already generates: max concurrency, gross exposure through time, portfolio max drawdown. Re-run with #3's caps applied. | **C-2** | A day | Very high — the only way the 20% drawdown limit can ever be certified. |
| **5** | **Data-integrity gate:** staleness assertion, sanity band, degenerate-ATR check, coverage counter (`scanned N/38, failed: [...]`), second-source cross-check, pinned `requirements.txt`. | **H-3, M-4, M-5** | A day | High — removes a failure mode that is currently invisible *and* reassuring. |
| **6** | **Reconcile the stop-width thresholds** to one constant; delete the dead branch; **re-run `run_engine1()` with the 15% filter applied** and compare. Retire E1 if its edge does not survive its own live guardrail. | **H-2** | Hours + a backtest run | High — may retire an entire engine, which would also resolve #7. |
| **7** | **Fix or rename the Pine.** Either implement Engine 2, or retitle it `Engine 1 (Mean Reversion) — OBSERVATION ONLY`. | **H-1** | 5 minutes (rename) | High per unit effort — he is currently trading from a chart that can only show the engine he deprecated. |
| **8** | **Commission and slippage in both backtests.** Populate from his actual schedule; re-read the OOS verdict net. | **M-1** | An hour | High — may determine there is no edge at this size at all. Cheapest decisive test on the list. |
| **9** | **Bear filter: add an exit side and a buffer, then measure.** On a bear flip, tighten all trails 3×ATR → 1.5×ATR and cut `TREND_MAX_HOLD` to 10. Require a 2% band or 3 consecutive closes. Then measure, using data `momentum_pit_backtest.py` already downloads: (a) count SPY MA200 crossings 2019–2026; (b) count round-trip flips within 20 sessions; (c) SPY drawdown from peak at the moment of each bear flip; (d) Engine 2 EV in the 60 sessions after each flip. | **H-5** | A day | Medium-high — converts an untested assumption into a measured control. |
| **10** | **Currency-aware sizing + suppress trade plans for prohibited instruments.** Print the prohibition and nothing else — no stop, no target, no share count. | **H-7, M-3** | Hours | Medium — removes manufactured temptation and repairs the behavioural record. |
| **11** | **Write down personal risk limits.** One `risk_config.py`, imported by every script. Today they are scattered across five files and disagree in three places. | **Governance** | An hour | Medium — but it is the precondition for ever detecting a breach. |
| **12** | Secrets to environment variables; add `.gitignore`; `chat_id` allow-list. | L-1, L-2 | An hour | Low financial, non-zero security. |

---

## 6. Correlation and concentration assessment (formal)

| Dimension | Assessment |
|---|---|
| **Nominal diversification** | 38 names across 8 sectors — appears well diversified. |
| **Structural concentration** | **52.6% of the universe is one factor** (tech + crypto complex). Expected cluster weight breaches `max_correlated_cluster: 0.40` on a random draw, before any signal logic. |
| **Selection-induced concentration** | Engine 2's leadership filter (ADX≥25, 20-day high, full MA stack) selects the *currently leading factor*, so realised concentration materially exceeds the nominal 52.6%. Signals arrive **in clusters, on the same days, from the same factor**. |
| **Effective bets** | At N=10, ρ=0.8: **N_eff = 1.22**. At ρ=0.5: 1.82. **ρ is a labelled scenario — unmeasured (§0), commissioned in CL-5.** |
| **Diversification benefit** | At N=10, ρ=0.8 the worst case falls only from 10% to 9.06% — a **9% risk reduction for a 10x increase in positions, costs and daily monitoring burden.** |
| **Is this a factor bet in disguise?** | **Yes.** Six semis, six mega-cap platforms, six software/internet, two crypto proxies. In a drawdown these de-rate on one narrative. The book counts positions; the market counts factors. |
| **Verdict** | **Concentration is the dominant risk in this system, it is entirely unmeasured, and no control anywhere addresses it.** |

---

## 7. Formal risk opinion and conditions for clearance

**Would I clear this system to run at its current size and configuration?**

**No. VETOED.**

Not because the strategy is bad — I have no view on that and it is not my department. Because **the container has no walls in seven of the thirteen dimensions I am required to check**, and because the one enforcement mechanism the system does rely on — the Owner's own discipline at the moment of the trade — has a documented failure rate of two breaches in six trading days, one of which put **100% of the account on a single stop** and required **at least 2.3x and plausibly ~9x leverage** against a `leverage: none` rule.

I want to be equally clear about what this veto is *not*. It is not a judgement on the Owner's discipline, and it is not a judgement on the research. The research is genuinely good. And per H-7, one of the two breaches he has been reproaching himself over may be substantially a currency bug in his own sizing function rather than a failure of will. **A system that requires perfect discipline to be safe is a badly designed system, and that is a finding against the architecture, not against the man.** My job is to make the guardrails hold without requiring him to be perfect — because nobody is, and the two breaches are simply the evidence arriving on schedule.

### Conditions for clearance (binding on Zac and 死潘狗; each must be verifiable, not asserted)

| # | Condition | Verification |
|---|---|---|
| **CL-1** | **Cash-only account, margin disabled.** No exception, no waiver, no "just for this one". | Written broker confirmation on file. |
| **CL-2** | Position ledger exists and is populated; `/portfolio` reports open count, gross exposure, heat, cash, stale trails. | Live demo. |
| **CL-3** | `position_plan()` hard-blocks notional > 10% of account; `MAX_OPEN_POSITIONS = 5`; `MAX_PORTFOLIO_HEAT = 5%`; cluster cap ≤ 2 per sector. All from one `risk_config.py`. | Unit tests, including the §3 C-1 worked example ($200 stock, 2% stop → must BLOCK, not return 3 shares). |
| **CL-4** | One stop-width constant per engine; dead branch deleted; **E1 re-validated OOS with its live 15% filter applied**, or E1 retired. | Backtest output + diff. |
| **CL-5** | **Portfolio-level backtest** with an equity curve and max DD **≤ 20%** under CL-3's caps. Mo Peter to produce a 1-day 95% VaR on the capped book (≤3%); Mario to stress it against a semiconductor-complex drawdown using the **measured** pool correlation matrix. *Both are formally commissioned by this review and both are blocked on market-data access being restored — see §0.* | Reports filed in `reports/risk/`. |
| **CL-6** | Data-integrity gate live: staleness, sanity band, coverage counter, second-source cross-check, pinned dependencies. | Code review + a deliberate failure-injection test. |
| **CL-7** | Actual commission schedule documented; **net** EV > 0 after commission and slippage at his real fee. | Broker schedule + re-run backtest. If net EV ≤ 0, the system does not trade at this size. |
| **CL-8** | **20 consecutive paper trades with zero sizing breaches**, logged, before any real capital. Any breach resets the counter to zero. | Trade log reconciled against ticket file. |
| **CL-9** | Pine either implements Engine 2 or is renamed to state it is Engine 1, observation only. | File inspection. |

**On account size:** I am **not** conditioning clearance on more capital. The account is operable (§4.3), merely inefficient. But the Owner should understand he is running a **process-validation account, not a return-generating one**, and should judge it on breach count and rule adherence rather than on P&L for at least the first 20 trades. **And if he does add capital, CL-1 through CL-3 must be in place first** — adding capital to an uncontrolled system multiplies the 7/18 exposure rather than diluting it.

**Standing firm rule reaffirmed:** no agent of this firm connects to a broker or transmits an order. Everything above produces tickets and configuration recommendations for the Owner to action himself.

### Escalation

Per my mandate I am escalating two items to the CEO and the Owner immediately:

1. **A realised breach of `leverage: none` on 2026-07-18** (BAC, ≥2.3x, plausibly ~9x). Remediation: CL-1, actionable today at zero cost.
2. **`config/risk-limits.yaml` does not currently govern the Owner's personal account, and no written personal limits exist.** Recommendation: adopt a personal limits file. My proposed starting values, for the Owner's decision — max 5 concurrent positions, 5% total heat, 10% single-position notional, 40% correlated-cluster cap, 10% cash floor, 20% drawdown budget, leverage none. **These are proposals for the Owner to set deliberately. I will not have limits arrive by accident of whichever file happened to run.**

---

**John**
Chief Risk Officer, Department 6 — Risk Management
皮褸黃 Capital · 2026-07-30

*Upside is not my department. Survival is.*
