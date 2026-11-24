# V6.6 lab: independent adversarial review (Tom, Backtesting)

Date: 2026-11-24 · Reviewer: Tom (Dept 3, Backtesting) · Subject: `strategy/v6.6/` lab and CEO report `reports/quant/2026-11-24-v642-real-code-v66-lab.md`

Status: complete. All numbers come from my own re-runs on 2026-11-24 (scripts under the session scratchpad `tom/work/`). None are taken from the CEO report.

## Verdict

| Object | Verdict |
|---|---|
| `strategy/v6.6/lab.py` (as committed in `901d88e`) | **FAIL**, because of the HIGH slot-accounting bug F-1 |
| `strategy/v6.6/lab.py` (with my three fixes; `selftest.py` 16/16) | **PASS WITH CORRECTIONS**. Outstanding: F-3 (scanner path), F-6 (parity metric), F-7 (bootstrap) |
| `rules_v642.py` | **PASS** (identical to the real functions; one false docstring, F-3) |
| `indicators.py` | **PASS WITH CORRECTIONS**: RSI/ATR/OBV match `ta`; ADX parity unverified, and `parity_check.py` is too lax to catch a 1-bar slip (F-6) |
| CEO report `2026-11-24-v642-real-code-v66-lab.md` | **FAIL**: the per-trade sections stand, but the headline and the cap conclusion do not. It must be reissued before John or the Owner rule on the cap |

**In one paragraph.** The rule port is faithful, and every key table in the report reproduces from the committed
code (one side number, M2 −1.9%, does not). That code had a bug: an unaffordable signal reserved one of the two slots and then failed at the open,
so the slot sat empty. Fixing it moves the as-traded result from **0.96% → 2.21% CAGR (+US$50 → +US$116, 88
→ 135 trades)**. It also removes the claim that 10% is worst "in both halves": corrected IS ranks 10% above
20% and no-cap. Across 48 path perturbations, 10% is worst in IS in only 17% of runs. A higher cap
still wins over the whole window and in OOS in every run, so the direction stands, but it rests on
2025–26 alone. Separately, the lab measures the *backtest's* Engine 2 (20-day-breakout gate). The Owner's
daily scanner has no such gate, and its E2 shows +0.17–0.20% OOS per trade, not +0.86%. **Do not take a
cap decision, or any E2-vs-E1 decision, from this lab until it reports the Owner's actual scanner path.**

## Integrity checklist

| Check | Status |
|---|---|
| No look-ahead bias | **PASS**. Signal at the t close, fill at the t+1 open (`as_traded`/`per_trade`); `as_tested` same-close by design. Indicators causal |
| No survivorship bias | **FAIL (known, F-01)**. The 38 names are a 2026 selection; EW38 benchmark inflated |
| Point-in-time data | **PARTIAL**. Prices split- *and* dividend-adjusted; sizing corrected for splits only (dividends lower early prices up to ~5–15%); Webull volume split-adjusted from the wrong date for NVDA/AVGO/WMT (F-8). No earnings dates (guardrail 2 not modelled) |
| Realistic costs and slippage | **ASSUMED**. 10bp/side is not from a contract note; US$1/side minimum turns the result negative (−3.2% CAGR corrected). Messi's execution assumptions were not supplied for this account |
| Splits/dividends handled | **PASS after F-2** (MSTR added). Splits after June 2026 cannot be excluded from my knowledge; no unadjusted steps found in prices |
| No holdout contamination | **FAIL for anything chosen here**. 2025–26 was already used by the Owner's July OOS and by this report's cap curve and 3.6×ATR idea. No untouched sample remains for the cap decision |

## Findings (numbered, severity, file:line, fix)

| # | Sev | Where | Finding | Fix |
|---|---|---|---|---|
| F-1 | **HIGH** | lab.py:376–386 (committed) | An unaffordable top-ranked candidate takes a slot as a pending order, fails the share check at the next open, and leaves the slot empty while affordable candidates are turned away. The real scanner never lists shares <1. Biases `as_traded` down and the cap comparison against 10%. | **Fixed**: affordability checked at scan time on the signal close (raw-price), as the scanner does. New reject counter `scan_0_shares`; selftest added |
| F-2 | MEDIUM | lab.py:49–54 | MSTR 10-for-1 (2024-08-08) missing from `SPLITS`. No effect on published numbers; would mis-size MSTR once F-1 is fixed | **Fixed**; selftest added |
| F-3 | **HIGH** | lab.py:208, rules_v642.py:176–181 | The lab trades the *bt* E2 (breakout gate) and every R≥2 E1. The Owner's `掃描.bat` → `daily_strong_signals.py` lists E2 without the gate and only strong-tier E1 (RSI2<10, R≥3). The docstring "scan 同 bt 一致" is false. Changes E2 OOS +0.86 → +0.17 and 10%-cap OOS CAGR +2.6 → −0.8 | **Not fixed** (a modelling choice, not an unambiguous bug). Add `--path bt|scan|daily` and report all three; correct the docstring |
| F-4 | LOW | lab.py:398–400 | Forced close at the file's last bar even for IS runs (wrong date and price on excluded rows) | **Fixed** (last bar ≤ period end) |
| F-5 | **HIGH** | CEO report §0, §4, §5, §7 | Headline 0.96% / +US$50 and "10% worst in both halves" are artefacts of F-1. Corrected: 2.21% / +US$116; IS 10% > 20% > none; under perturbation IS 15% beats 10% in only 58% of runs | Reissue §0/§4/§5 with the 4b tables and the §5 perturbation result. Make sure the CRO cap ruling (`reports/risk/2026-11-24-swing-notional-cap-cro.md`) uses the corrected numbers |
| F-6 | MEDIUM | parity_check.py:147–154 | Agreement over all days; a 99% pass allows ~7% of signal days to differ, and a 1-bar ADX slip scores ~95% | Score agreement on the union of signal days (≥98%) and require max |ΔADX|, |ΔDI| < 0.01 after bar 250; also compare `trend_entry_ok` and the lab's `build_signal` path |
| F-7 | MEDIUM | lab.py:409–422 | Block bootstrap: 10-trade blocks (≈1–2 weeks), non-circular, so CIs are too narrow for regime-clustered trades | Calendar-month (or quarter) blocks, circular; report CIs for IS/OOS per engine |
| F-8 | LOW | data (Webull CSVs) | Volume split-adjusted from the wrong date (NVDA ×12 at 2024-03-04, AVGO ×12 at 2024-06-17, WMT ×3.3 at 2023-12-06); prices dividend-adjusted. Measured effect: 1 signal day | Repair volume at load or use yfinance volume; size on unadjusted closes where available |
| F-9 | MEDIUM | CEO report §5 price-band table | Bands use adjusted prices; 28 E2 trades labelled affordable were not | Corrected bands (raw): ≤$128 IS +0.25 (61) / OOS +0.08 (29); $128–250 +2.07 / +3.10; >$250 +1.90 / +0.55 |
| F-10 | MEDIUM | CEO report §1, §2, §4, §6.1 | E1 "+0.220 vs +0.222" presented as reproduction (different window and trade count); E2 cause-in-portfolio claim contradicted by M1; "E1 zero edge" holds only for the non-daily path; M2 −1.9% not reproduced (−2.57%) | Relabel as inference; fix numbers (section 6) |
| F-11 | LOW | strategy/v6.6/__pycache__/*.pyc tracked in git | Every run dirties the tree; a stale `.pyc` is a version-drift risk | `git rm -r --cached strategy/v6.6/__pycache__`; add to `.gitignore` |
| F-12 | LOW | strategy/v6.6/results/*.csv | Produced by the F-1 simulator | Regenerate with the corrected lab (I did not overwrite them) |
| F-13 | LOW | lab.py:268–269, cost model | E1 gap above the target fills at the target (conservative); no FX, SEC/TAF or 30% dividend withholding | Document; add FX bp when the contract note arrives |

## 1. Fidelity: rules_v642.py and lab precompute vs real dual_engine_v6_4.py

The real source was read, not executed. It is `01_每日使用_最新V6.4.2/dual_engine_v6_4.py` (644 lines),
plus `daily_strong_signals.py`, `掃描.bat` and `03_回測及驗證腳本/oos_validation.py`.

**Function-by-function (rules_v642.py vs dual_engine_v6_4.py):**

| Function | Real (line) | Port (line) | Result |
|---|---|---|---|
| constants MIN_R, ATR_TRAIL_MULT, score mins, 12%/15%, 10% cap, HKD 10k, 1%, 7.8 | 64–88 | 16–28 | identical |
| `mr_score` | 125–170 | 41–86 | identical, every branch and weight |
| `mr_plan` (filter R≥2, then nearest) | 173–198 | 89–111 | identical; V6.5 defect fix confirmed correct |
| `trend_score` | 204–260 | 114–151 | identical score; port drops the `detail` dict (returns float, not tuple). Harmless; `parity_check.sig()` handles both |
| `trend_plan` | 263–272 | 154–162 | identical |
| `classify` | 278–286 | 165–173 | identical |
| `position_plan` (USD branch) | 341–377 | 190–204 | identical for whole shares; HKD branch omitted (US-only universe, fine). The `fractional` option is lab-only |
| `calc_indicators` | 94–119 | indicators.py 293–317 | same columns and formulas; `ta` calls replaced (section 2) |

**Lab precompute/build_signal vs the Owner's code paths. Three different "V6.4.2"s exist:**

| Element | `dual_engine bt` / `oos_validation` | `dual_engine run_scan` | `daily_strong_signals.py` (what `掃描.bat` runs daily) | lab |
|---|---|---|---|---|
| E2 entry | ADX≥25, DI+>DI−, **High ≥ 20d high**, score ≥0.65, stop ≤12% | TREND_UP + score ≥0.65 + plan. **No breakout gate** (breakout is only +0.10 in the score) | same as run_scan | **bt gate** (`rules_v642.trend_entry_ok`, lab.py:208) |
| E1 entry | ADX<25, score ≥0.55, plan R≥2. **No 15% check** | + 15% guardrail + earnings guardrail + shares ≥1 | **only STRONG/PREMIUM: RSI2<10 and R≥3**, + guardrails + shares ≥1 | all R≥2 signals + 15% check |
| Affordability | none | shares ≥1 at the signal close, else "blocked" | shares ≥1 at the signal close, else not listed | checked **at fill only** (bug F-1, fixed) |
| Engines | separate runs, so one ticker can be in E1 and E2 at once | | | one position per ticker across engines |

The `rules_v642.py:177` docstring says the trend entry gate is the same in scan and bt ("scan 同 bt 一致"). **That is false.**
The scanner the Owner runs every day has no breakout gate, and it lists only strong-tier E1 signals. Effect,
measured (`tom/work/scan_variant.py`, corrected lab, `per_trade` net EV/trade (n)):

| Variant | E1 IS | E1 OOS | E2 IS | E2 OOS | `as_traded` CAGR all / IS / OOS (10% cap) | (15% cap) |
|---|---|---|---|---|---|---|
| lab (bt gate, all E1) | +0.39 (352) | −0.03 (380) | +1.33 (207) | **+0.86 (137)** | 2.21 / 1.82 / 2.62 | 3.90 / 2.07 / 4.88 |
| scanner E2 (no breakout gate) | +0.37 | −0.00 | +2.03 (241) | **+0.20 (167)** | 2.65 / 1.93 / 2.93 | 4.02 / 1.96 / 5.31 |
| strong-tier E1 only | +0.33 (108) | **+0.65 (105)** | +1.30 | +0.83 | 1.78 / 2.95 / 0.53 | 3.36 / 2.66 / 4.14 |
| **`掃描.bat` as run** (both) | +0.33 (108) | +0.65 (105) | +2.00 (242) | **+0.17 (168)** | **0.82 / 2.30 / −0.82** | 3.16 / 2.43 / 4.08 |

The CEO's headline, "E2's per-trade edge looks real and robust" (OOS +0.86%), holds for the **backtest's**
E2. It does not hold for the E2 the Owner's scanner actually lists (OOS +0.17%). The report's E1
conclusion also flips: the tool the Owner runs shows only strong-tier E1, and that tier is positive OOS.
The report should say which code path it measured, and the lab needs a `scan` mode. Neither variant
changes any V6.4.2 rule. They choose which of the Owner's own code paths is being modelled. Not modelled
anywhere: the earnings guardrail (no historical earnings dates; the CEO report already flags this).

## 2. Indicators vs `ta`

`ta` is not installed here, so I could not run a parity check. What follows comes from reading `indicators.py`, from
my own knowledge of the `ta` 0.10/0.11 source (recalled, **not re-read**), and from tests on the data.

| Indicator | indicators.py | `ta` (recalled) | Assessment |
|---|---|---|---|
| RSI | Wilder EWM, alpha 1/n, `adjust=False`, `min_periods=n`; first diff → 0; avg_loss=0 → 100 | same code pattern (`ewm(com=n-1, …)` is equivalent) | match expected |
| ATR | TR with skip-NaN max (bar 0 = H−L); seed = mean TR[0..n−1] at bar n−1; recursive; zeros before | same | match expected |
| OBV | −vol if close < prev close, else +vol (flat = +) | same | match expected |
| ADX/DI | textbook Wilder sums, seeded at bar n; DX from bar n; ADX seeded as mean DX[n..2n−1] at bar 2n−1 | hand-written numpy loops with array offsets (`_trs[i]` ↔ bar `n+i`, ADX array concatenated after n−1 zeros). Index alignment in this class has been a known source of discrepancies between `ta` and other libraries | **the one real risk** |

**Seeding does not matter after warm-up.** An alternative ADX built with pandas `ewm(alpha=1/14, adjust=False)`
from bar 1 (TradingView/pandas-ta style, no SMA seed) gives |ΔADX| = 0.00 on every tradeable day after
bar 250. It produces 0 route flips and identical results. A seeding difference therefore cannot move ADX
across 25.

**Index alignment does matter.** If `ta`'s ADX/DI were one bar off from the textbook series, either
direction, the effect on these data (`tom/work/adx_alt.py`) would be:

| | |ΔADX| median / p90 / max | Route flips (bull days) | Signal days differing | `per_trade` E2 OOS | `as_traded` CAGR all / IS / OOS |
|---|---|---|---|---|---|
| lab (textbook) | – | – | – | +0.86 (137) | 2.21 / 1.82 / 2.62 |
| ADX one bar early (`lead1`) | 0.73 / 1.70 / 4.20 | 4.85% | 6.7% | +0.77 (145) | 1.74 / 0.62 / 2.19 |
| ADX one bar late (`lag1`) | 0.73 / 1.70 / 4.20 | 4.84% | 6.9% | +0.76 (126) | 0.52 / 1.43 / **−0.62** |

A one-bar slip barely moves the per-trade EVs. It does flip the OOS portfolio CAGR from +2.6% to −0.6%.
That is another sign of how fragile the 2-slot portfolio numbers are (section 5).

I also checked the Owner's own `v6_signals_trend.csv`. It prints last-bar ADX values (UNH 45.6, BAC 41.1), so on his
machine `ta` returns a finite ADX on the scan bar. That rules out at least the last-bar-NaN failure mode.
Beyond that, **parity is unverified**.

**`parity_check.py` is too lax to catch the slip.** It scores agreement over *all* days. Most days have no
signal on either side, so a 99% all-day agreement still allows roughly 7% of *signal* days to differ, since
signal days are ~14.5% of bull days. The one-bar slip above would score ~95% all-day agreement, which
lands in the "⚠️ broadly trustworthy" band. Fix (F-6): report agreement on the union of signal days and
require ≥98%, and require max |ΔADX| < 0.01 after bar 250.

**Data defect, not an indicator defect.** Webull's *volume* is split-adjusted from the wrong date for three
names. Volume steps up ×10–12 on NVDA at 2024-03-04 (split was 2024-06-10), ×10–12 on AVGO at 2024-06-17 (split
2024-07-15), and ×3.3 on WMT at 2023-12-06 (split 2024-02-26). Prices look correctly adjusted. This inflates
`vol_ratio`/OBV for ~20 bars after each step. Repairing it changes 1 signal day and leaves results unchanged.
It should still be fixed at load time (F-8). Prices are also **dividend-adjusted** (SPY 2022-11-30 close is
387.07 in the file vs ~407.7 as printed that day, the latter from my memory, not fetched). That lowers early prices by up to ~5% for SPY-like yields
and more for XOM/CVX/PFE/JNJ, which slightly overstates affordability under the cap in 2022–23.

## 3. Simulator mechanics (lab.simulate, line numbers refer to the committed `901d88e` file)

| Item | Finding |
|---|---|
| Look-ahead | None found. Signals use bar-t close data (rolling and EWM are causal; `high_20d` includes today's high, which is known at the close). `next_open` fills at the t+1 open (`selftest` asserts this). `as_tested` fills at the t close by design, matching V6.4 bt. SPY regime uses the t close. |
| Same-bar ordering | E1 checks stop before target (conservative, as in V6.4 bt). E2 checks the trail, then updates it (as in V6.4 bt 568–582). Entry day is managed with the stop from the signal close. OK. |
| Gap fills | E2 gap below the trail exits at the open (as bt). E1 gap below the stop exits at the open in `as_traded` (bt has no gap rule, `e1_gap_fill=False` in `as_tested`, correct). E1 gap *above* the target fills at the target, not the open. Slightly conservative, as in bt. LOW. |
| Day counting | `next_open` counts the entry day as day 1, so E1 exits at the t+10 close. That is the same calendar exit as bt (entry at the t close, exit at the d=10 close). E2 likewise. OK. |
| Re-entry | `busy_until` blocks a re-signal on the exit day only. This matches bt (`i += exit_day`, then `i += 1`). OK. |
| **Slot accounting with pending orders** | **BUG (F-1, HIGH).** lab.py:376–386 queues the best-ranked candidate as a pending order *before* checking it can be bought. The 10%/whole-share check happens at the next open (lab.py:304–309). If it fails, that slot sits empty for the day, and the next affordable candidate has already been turned away as `no_slot`. E2 ranks first and is usually the expensive name, so the same unaffordable E2 can block a slot day after day. The Owner's scanner never lists a signal with shares <1 (`dual_engine_v6_4.py:419–423`, `daily_strong_signals.py:130–131`). Original run: 611 fill-time "0 shares" rejects and 3,860 `no_slot` rejects. Fixed run: 0 fill-time rejects, 3,494 dropped at scan, 817 `no_slot`. Trades 88 → 135, CAGR 0.96% → 2.21%. Waste is largest at the 10% cap, so the bug also biased the cap comparison against 10%. |
| Max positions | ≤2 holds (`selftest`; equity `n_pos` max = 2; max raw notional per trade US$127.77). |
| Monthly breaker | Realised P&L only, calendar month, checked at scan. **Never fires** (0 rejects in every config). A US$128 monthly loss needs several gap losses at 1% risk. Untested in practice, not wrong. |
| End of data | **BUG (F-4, LOW).** lab.py:398–400 force-closes open positions at the ticker's *last bar in the file*, even in IS runs ending 2024-12-31. The result is wrong exit dates and prices on the "數據結束" rows. Those rows are excluded from the stats and equity is unaffected, so no reported number changes. Fixed to use the last bar ≤ period end. |
| Costs | 10bp/side applied on entry and exit notional. Per-trade mode subtracts a flat 0.20% (dead variable `cost_pct` at lab.py:245, harmless). No FX conversion cost, no SEC/TAF fee, no 30% US dividend withholding (prices are dividend-adjusted, so returns include gross dividends: small upward bias). |
| Equity MTM | Adjusted close × adjusted shares = raw value. P&L identity checked independently: Σ closed P&L + open MTM = equity change (US$49.91 original; US$120.74 − 4.84 = US$116.32 fixed). OK. |
| Split-corrected sizing | `raw_factor` is correct for the table's entries (adjusted × factor = raw). **Missing MSTR 10-for-1, first split-adjusted session 2024-08-08 (F-2).** This comes from my own knowledge. The data cannot show it, because both price and volume are adjusted (close 124.69 on 2024-08-07, 135.99 on 2024-08-08, no step). No pre-split MSTR trade happened in the original run, so the published numbers are unaffected. With F-1 fixed, MSTR would wrongly look affordable before August 2024. Other splits in the 38 names since 2022-11-30, as far as I know: WMT, NVDA, AVGO, NFLX (all in the table). AMZN/GOOGL/TSLA/SHOP split before the tradeable window. **I cannot rule out a split between June and November 2026** (after my knowledge). Scanning the data for unadjusted price steps finds none. The volume series shows wrong split-adjustment dates for NVDA/AVGO/WMT (section 2). |
| E2 price-band table (e) | Reproduced exactly on *adjusted* prices. 28 E2 trades in the "≤$128 (affordable)" band were not affordable (AVGO 8, NFLX 10, NVDA 5, WMT 5). On raw prices: ≤$128 **IS +0.25% (61) / OOS +0.08% (29)**; $128–250 +2.07 (59) / +3.10 (33); >$250 +1.90 (93) / +0.55 (75). The CEO's direction holds, and is in fact stronger in IS. The magnitudes in the published table are wrong. |
| Bootstrap CI | Non-circular moving-block bootstrap, block = 10 trades in entry-date order, percentile 5/95, n=2000. Two weaknesses: (i) block starts are drawn from [0, n−block], so the last trades are under-sampled; (ii) 10 trades ≈ 1–2 weeks of a 1,087-trade book, far shorter than regime-level dependence. The per-trade CIs are therefore too narrow. Use calendar-month blocks or a circular bootstrap with block ≈ n^(1/3) months. MEDIUM (F-7). |
| `as_tested` vs V6.4 bt | Differs in three small ways: lab applies the 15% E1 check (bt has none); one position per ticker across both engines (bt runs engines separately); E1 starts at bar 80 (bt 60). This is fine for its purpose, but it is a reason the "+0.220% vs +0.222%" match is not a validation (section 6). |

## 4. Re-run of the report's key tables

Re-run on 2026-11-24 with the lab as committed (`901d88e`), data = Webull CSVs in the session scratchpad
(38 names + SPY, 2022-02-11 → 2026-11-23), `python3 -I lab.py --mode ab|sens|caps`. `selftest.py`: 14/14 pass.
The lab is deterministic, and the committed code reproduces every number in the CEO report:

| Report claim | Re-run (original code) | Status |
|---|---|---|
| (a) E1 OOS `as_tested` +0.220% (396) | +0.220% (396) | Reproduced |
| E2 IS/OOS `as_tested` +1.650 / +1.015 | +1.650 / +1.015 | Reproduced |
| (b) `per_trade` net E1 IS/OOS +0.39 / −0.03; E2 +1.33 / +0.86 | +0.388 / −0.026; +1.328 / +0.864 | Reproduced |
| `per_trade` ALL net +0.50, CI [0.00, +1.08] | +0.495, [+0.00, +1.08] | Reproduced |
| (c) `as_traded` 88 trades, CAGR 0.96%, +US$50, maxDD −3.9% | 88, 0.964%, +US$49.91, −3.89% | Reproduced |
| (d) caps 10% 0.96/0.94/0.51; 15% 4.28/3.40/5.27 | identical | Reproduced |
| (f) sensitivity E2 range +0.61 to +2.13; E1 OOS −0.06 to +0.90 | E2 0.613 to 2.125; E1 OOS −0.062 to +0.903 | Reproduced |

Reproduction only shows the code does what the report says it does. It does not show the code is
right. Sections 3 and 5 find two defects that move (c) and (d). Corrected numbers are in section 4b.

### 4b. After the two corrections (F-1 slot-waste fix, F-2 MSTR split), same data, same rules

`as_traded` (2 slots, 10% cap, whole shares, next open, 10bp/side):

| | All | IS | OOS |
|---|---|---|---|
| Trades | **135** (was 88) | 67 (47) | 66 (39) |
| CAGR | **2.21%** (was 0.96%) | 1.82% (0.94%) | 2.62% (0.51%) |
| Max drawdown | −4.5% (−3.9%) | −4.5% | −3.5% |
| P&L | **+US$116** (+US$50) | +US$49 | +US$64 |
| Net EV/trade, 90% CI | +0.81% [−0.03, +2.25] | +0.78% | +0.73% |
| E1 / E2 net EV/trade | +1.85% (86) / **−1.03% (49)** | +1.51 / −0.13 | +1.97 / **−2.31** |
| Exposure (days with ≥1 position) | 88% (76%) | 93% | 83% |

Cap curve (`--mode caps`, corrected, CAGR all / IS / OOS):

| Cap, 2 slots | CAGR all / IS / OOS | Net EV/trade | Max DD |
|---|---|---|---|
| 10% | 2.21 / **1.82** / 2.62 | +0.81% | −4.5% |
| 15% | 3.90 / **2.07** / 4.88 | +1.04% | −5.9% |
| 20% | 5.68 / **1.01** / 10.00 | +1.25% | −6.6% |
| none | 2.49 / **−0.01** / 6.01 | +0.38% | −8.9% |

In IS, 10% beats both 20% and no cap. **The claim "10% is the worst setting tested, in both halves" is
false once the slot bug is fixed.** In OOS, 10% is still clearly the worst. The curve is not monotonic
(20% > none in every column), which looks more like slot-allocation noise than a smooth trade-off.

`as_tested` and `per_trade` are unaffected (they have no slots or cap). (a), (b) and (f) stand as reproduced.

(e) Price-band table: reproduced on adjusted prices, but mislabelled. The corrected raw-price bands are in section 3 (row "E2 price-band table") and F-9.

## 5. Statistical honesty and cap-conclusion path dependence

**Sample size.** `as_traded` uses about 135 trades: 67 in IS and 66 in OOS (88/47/39 before the fix). On
each scan day the 2 slots take one of ~30 competing candidates. Across the run, 3,494 candidates were
unaffordable at signal time and 817 were turned away for lack of a slot. Which ~135 trades get taken is
therefore set by tie-breaks and by when each slot frees up. The 90% CI on net EV/trade for the whole
run is [−0.03, +2.25]. The halves are wider still. A ranking of cap settings built on CAGR differences of
1–3 points per year, each from ~65 trades, needs a perturbation test before anyone relies on it.

**Test (script: scratchpad `tom/work/pathdep.py`, corrected lab, signal rules untouched).** 48 runs of the
`as_traded` book, each at caps 10/15/20/none (576 simulations):
- base (1 run);
- start date shifted +1, 2, 3, 5, 8, 13 or 21 trading days (7 runs);
- random tie-break among equal (engine, score) (10 runs);
- random pick *within* each engine. This models the Owner choosing among listed signals, since the scanner says "揀一個" (pick one). 20 runs;
- random pick across all candidates, ignoring E2 priority (10 runs).

| Statistic (48 runs) | IS | OOS | ALL |
|---|---|---|---|
| P(10% is the worst of 10/15/20/none) | **0.17** | 1.00 | 0.90 |
| P(10% is worst in *both* halves) | **0.17** | | |
| P(10% is the best) | 0.08 | 0.00 | |
| CAGR(15%) − CAGR(10%), median [min, max] | **+0.18 [−2.60, +2.79]** | +2.61 [+1.74, +5.81] | +1.69 [+0.24, +3.99] |
| Share of runs where 15% beats 10% | **0.58** | 1.00 | 1.00 |
| Median CAGR 10 / 15 / 20 / none | 1.82 / 1.89 / 1.83 / 0.56 | 2.29 / 4.88 / 8.09 / 6.01 | 2.20 / 3.71 / 5.39 / 2.91 |

Breakdown of "10% worst in IS" by perturbation type: start shift 0/7, tie-break 0/10, within-engine
pick 7/20, any-order pick 1/10.

**What survives.** Over the whole window and in OOS, a cap above 10% beats 10% in every perturbation.
That direction is robust. **What does not survive.** In IS (Dec 2022 → 2024), 15% versus 10% is a coin flip:
15% wins 58% of runs, with a median difference of +0.18 points. Under the Owner's own adoption rule
(better in both halves), the evidence does **not** clear the bar. All of the cap's apparent cost
comes from the 2025–26 OOS window. In that window the mega-cap trend names that a US$128 cap
excludes did very well. That is one regime, not a structural law.

**Same 48 perturbations on the original (uncorrected) lab:**

| Statistic | IS | OOS | ALL |
|---|---|---|---|
| P(10% worst) | 0.77 | 0.94 | 0.94 |
| P(10% worst in both halves) | 0.73 | | |
| CAGR(15%) − CAGR(10%), median [min, max] | +2.45 [−0.31, +5.09] | +4.50 [+0.64, +7.62] | +3.34 [+0.74, +4.60] |
| 10% cap trades, ALL: median [min, max] | | | 92 [86, 122] |

The CEO's "worst in both halves" was stable against path perturbations *inside the buggy simulator*: 73% of runs.
It was produced by the slot bug, not by path luck. With the bug fixed it holds in 17% of runs. Under both
versions, 15% beats 10% over the whole window in 100% of runs. The robust statement is **"over 2022-12 →
2026-11, as a whole, a 15% cap would have earned more than 10%; the IS half alone does not support it."**

**Further fragility evidence.** A one-bar ADX slip turns the OOS `as_traded` CAGR from +2.6% to −0.6% (section 2).
Switching from the bt E2 gate to the Owner's actual scanner turns the 10%-cap OOS CAGR from +2.6% to −0.8%
(section 1). Two-slot portfolio CAGRs from this lab are ±2–3 point quantities. No single number in
the 0–3% range should be quoted to two decimals as "what the system earns".

**20-trade paper sample.** I confirm the CEO's half-widths: per-trade net SD E1 7.01, E2 8.90, so the 90%
half-width for 20 trades is ±2.58 / ±3.27 points. Agreed: a 20-trade paper run tests discipline, not edge.

## 6. Fact vs inference in the CEO report (C8)

| # | Report statement | Status |
|---|---|---|
| 1 | §1 "The implementation reproduces the Owner's numbers… E1 matches almost exactly" | **Inference stated as fact.** The windows differ: Owner = last 18 months to ~July 2026; lab = 2025-01-02 → 2026-11-23. Trade counts differ (299 vs 396). Lab `as_tested` adds the 15% check and cross-engine blocking that `oos_validation.py` lacks. +0.220 vs +0.222 is a coincidence of two different measurements. It does not validate the port. Parity is still unverified (§2). |
| 2 | §0/§5 "The single largest cause is the 10% notional cap"; "10% is the worst setting tested, in both halves" | **False after F-1.** Corrected IS: 10% (1.82%) > 20% (1.01%) > none (−0.01%). Under perturbation, 10% is worst in IS in 17% of runs. |
| 3 | §4 "Inside the portfolio E2 loses… The cause is below" (the cap) | **Causal inference, contradicted by the lab's own M1 row.** With fractional shares (affordability removed, 10% cap kept), E2 inside the portfolio is still +0.02% OOS (38 trades). The corrected lab gives E2 −1.03% vs E1 +1.85%. Slot selection and E2's low win rate in a 2-slot book are at least as plausible as causes. |
| 4 | §0/§2 "Per-trade edge of Engine 2 looks real and robust" | **True for the backtest's E2 only.** The Owner's daily scanner has no breakout gate. Its E2 is +0.17–0.20% OOS (§1). |
| 5 | §2 "E1's realistic edge is zero" | True for *all* R≥2 E1 signals. The tool the Owner runs lists only strong-tier E1, which is +0.65% OOS (105 trades, `per_trade` net). This is untested against the Owner's tier history, but the claim needs that qualifier. |
| 6 | §5 "Drawdown barely moves because the 1% risk-to-stop rule still binds" | Plausible, untested inference. Corrected max DD runs from −4.5% at 10% to −8.9% with no cap, so drawdown *does* move by ~2×. |
| 7 | §6.1 "US$1 minimum per side … −1.9% CAGR" | **Not reproduced.** The committed code gives −2.57% (original) and −3.16% (corrected). The number probably came from an earlier run. Direction unchanged. |
| 8 | §6.6 "pre-V6.4.2 code was in use" (CVX US$209, PFE 8 sh = US$229) | Reasonable inference from screenshots I did not see. It should be labelled as inference. Possible alternatives: a manually computed size, or a different account setting. |
| 9 | §6.8 "All tables here are post-fix" (splits) | Incomplete: MSTR missing (F-2), and the price-band table (§5) uses adjusted prices, so 28 trades are mislabelled. |
| 10 | §5 price-band table | Direction confirmed on raw prices. Published magnitudes are wrong (≤$128 IS +1.49 → +0.25). |
| 11 | §6.3 momentum-pool concentration (58%, +0.17%, 164%, median 11 / max 39) | **Verified** from `momentum_pit_trades.csv` (58.1%, +0.168%, 164%, 11/39). |
| 12 | §6.4 E1 4% target / 64% time exit at +2.9% | **Verified** (`per_trade`: 3.9% / 63.1% / +2.90%). |
| 13 | §6.2 A1/A2 rejections | **Verified**, and they survive the fix (A1 corrected −0.00/0.25/−0.28 vs 2.21/1.82/2.62; A2 1.84/1.37/2.30). Both are still worse in both halves. |
| 14 | §4 benchmarks SPY 17.0% / EW38 34.1% | Verified. EW38 is a 2026-selected universe (PLTR, MSTR, COIN, NVDA): heavily survivorship-inflated, so useful only as an upper bound. |

**Bias direction.**
- The slot bug understated the as-traded system and overstated the cost of the 10% cap.
- Using the bt E2 gate instead of the scanner overstates E2's OOS edge as the Owner actually trades it.
- The 2026-selected universe (F-01) overstates everything, and so do dividend-adjusted affordability in 2022–23 and gross-of-withholding dividends (both small).
- Missing earnings guardrail: direction unknown.
- Net: the report's cap conclusion was biased *towards* raising the cap, and its E2 conclusion was biased *towards* E2.

## Changes made to strategy/v6.6/*.py

No V6.4.2 rule, threshold or parameter was changed. `rules_v642.py`, `indicators.py` and `parity_check.py` are untouched.

1. `lab.py` `SPLITS`: added `"MSTR": [("2024-08-08", 10)]` (F-2).
2. `lab.py` `simulate()` scan loop: before the slot check, compute `position_plan` on the signal close × `raw_factor`. If shares ≤ 0, count `scan_0_shares` and skip, so the candidate does not take a slot (F-1). Added the `scan_0_shares` key to `rejects`.
3. `lab.py` `simulate()` end of data: force-close at the last bar ≤ the period end, not the file end (F-4).
4. `selftest.py`: two new tests, (a) an unaffordable E2 candidate does not block an affordable E1 when 1 slot is free; (b) MSTR split factor. `python3 -I selftest.py`: 16/16 pass.
5. Restored the tracked `__pycache__/*.pyc` to HEAD after running (F-11), so the diff contains only source.

`per_trade`/`as_tested`/sensitivity outputs are bit-identical before and after (checked: `sensitivity.csv` equal).
Only slot-limited modes (`as_traded`, A1, A2, M1–M4, caps) change.

## What would make this fail live

- **Wrong code path.** If the Owner trades from `掃描.bat`, his E2 is the no-gate version (+0.17–0.20% OOS
  per trade here). The +0.86% that "graduated" E2 is not the engine he runs.
- **Indicator drift.** A 1-bar ADX alignment difference vs `ta` changes ~7% of signal days and can flip a
  2-slot year from positive to negative. Until a strict parity check passes on his PC, treat the lab as ±1 bar.
- **Fees.** A US$1 minimum per side turns every configuration negative at this account size.
- **Path luck.** At the 10% cap, the corrected CAGR across 48 equally plausible paths ranges from p10 0.96% to
  p90 2.49% (median 2.20%). At 15%: 2.99% to 4.30%. Add the scanner-path and ADX uncertainty and the honest
  range at 10% is roughly −1% to +2.5% a year. Live results in that
  band are *consistent* with the backtest and prove nothing either way.
- **Regime.** The tradeable window has no bear market (MA200 warm-up consumed 2022). The cap's apparent cost
  comes entirely from the 2025–26 mega-cap trend; a different leadership regime could reverse it.
- **Gap risk at a higher cap.** A 30% overnight gap through the stop costs ~3% of the account at 10%, ~4.5% at 15%.
  This is the CRO's real trade-off, and this lab cannot price it (too few gap events in 4 years).
- **Owner discretion.** The scanner says "pick one". The within-engine random-pick perturbation alone moves
  10%-cap CAGR by several points. How the Owner chooses among signals is itself a parameter.

*Research and decision support only, not financial advice. No agent of this firm places orders. Tom does not
decide the cap; it goes to John (CRO), then the Owner.*
