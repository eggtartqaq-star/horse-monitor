# Review: V6.6 robustness test (2026-11-27) — Tom (Backtesting Engineer)

**Date:** 2026-11-27 · **Reviewer:** Tom (Dept 3) · **Scope:** HEAD `5435220`
- Script: `strategy/v6.6/robustness_v66.py`
- Report: `reports/quant/2026-11-27-v66-robustness.md` (called "the report" below)
- Output: `strategy/v6.6/results/robustness/*.csv`
- Read for checking: `lab.py`, `income_study.py`, `rules_v642.py`, `sizing_v66.py`

**How it was done:**
- I re-ran the unmodified script to scratch. All 5 CSVs are byte-identical to the committed ones, and the console matches the report.
- I ran my own checks in scratch scripts: anchored windows, drawdowns, trade-hash per variant, a no-trade counterfactual, a min_r limit-cap probe (monkeypatch in memory, `lab.py` untouched), a subset check and per-ticker affordability.
- I then edited `robustness_v66.py`, which the brief allows; see "What I changed". The edited script was re-run to scratch.
- No broker calls, no installs, no commit.

## Verdict: **PASS WITH CORRECTIONS**

**What holds:**
- The base case reproduces exactly: 3.29% vs 4.49%, −1.20%/yr, 130 trades.
- All seven sensitivity settings reach the simulator.
- The winner-removal subset is built correctly.
- The direction of the verdict survives every correction below: do not call it an "add-on"; the T-bill is the income.

**What must be fixed before the Owner sees it:**
- One table number is wrong: 2024 is −0.57%, not −0.02% (F-1).
- The min_r rows are only half wired (F-4).
- Section D gives the wrong reason why the winners don't matter (F-8, F-9).
- The headline "−1.2%/yr" is mostly two assumptions: a reserve that earns 0%, and an unverified US$0.35 fee. It is not a measurement of the trading (F-6, F-7).

## Integrity checklist

| Item | Status |
|---|---|
| Lookahead | **None found.** Signals are computed at the close and filled at the next open. D ranks by full-window rise on purpose (that is the test). |
| Survivorship | **Present, not resolved.** The 38 names were chosen in 2026. D is not a bound on this (F-8). |
| Point-in-time data | Adjusted Webull bars. Share counts use the SPLITS table. |
| Costs | real35 (US$0.35 minimum + 10 bp per side) is a CRO estimate, unverified (V-1). It is the swing factor (F-7). |
| Splits / dividends | Splits handled via `raw_factor`; dividends via the adjusted close. T-bill dividend days corrected (`income_study.py`). |
| Holdout | **Not clean.** 2025+ was already seen in the 26 Nov study. The ±20% grid is scored on it as well. Treat "since 2025" as descriptive only. |

## Findings

**F-1 · MEDIUM · The year-by-year table (A) drops the first trading day of every year.**
- **Cause:** `ret()` divides by the close of the first trading day *inside* the window. It should divide by the previous close.
  - 2024-01-02: system −0.51%, SPY about −0.6%.
  - 2026-01-02: system +0.41%.
- **Corrected figures** (re-run of the edited script; they match `results/income_yearly.csv`):

| Year | System | T-bill | Excess | Report said | SPY | Trades |
|---|---|---|---|---|---|---|
| 2022 (from 30 Nov) | −0.72% | 0.36% | −1.09% | *omitted* | −5.76% | 3 |
| 2023 | 0.94% | 4.94% | −4.01% | −4.00% | 26.18% | 34 |
| 2024 | **4.58%** | 5.16% | **−0.57%** | −0.02% | 24.89% | 30 |
| 2025 | 5.81% | 4.15% | +1.66% | +1.73% | 17.72% | 37 |
| 2026 to 23 Nov | 2.58% | 3.26% | −0.68% | −1.05% | 6.75% | 26 |

- **The trade-count logic is right:** entry date in the year, excluding 數據結束. But the 2022 stub was skipped (the `< 60 days` rule), so the years summed to 127, not 130. That stub was −US$16 on 3 trades.
- **What it changes:** the report calls 2024 −0.02%, which reads as a tie; it was −0.57%. "One year of four" still holds, and is now clearer.

**F-2 · LOW · The rolling windows (B) have the same one-day omission.**
- **Corrected:**
  - 16 of 42 windows beat T-bills, still **38%**;
  - median −0.33% (report said −0.22%);
  - best +3.57% (report said +3.68%);
  - worst −3.85% (unchanged).
- **The T-bill comparison is like for like:** same dates, same anchor, indices aligned (999 of 999 days).
- **The windows overlap by 5 of 6 months**, so there are only about 7 independent windows. The six non-overlapping start phases beat T-bills 4/7, 2/7, 3/7, 2/7, 2/7 and 3/7.
- **Fix:** say "about 7 independent windows". The 38% is a fair average, but it is not 42 data points.

**F-3 · MEDIUM · The ugly numbers are missing, and "worst drawdown under 3%" understates the drawdown.**
- **Why:** the per-year drawdown resets the peak every 1 January.
- **Full period:**
  - **−3.49%**: peak 2022-12-14, trough 2023-03-13, recovered 2023-09-01. That is **260 days** under water. The same −3.49% is in `income_scenarios.csv`.
  - The worst month was −0.95% (July 2025).
  - Monthly excess: t = −0.91 over 49 months; 39% of months were positive.
- **Against T-bills, the benchmark that matters here:**
  - the account was **below the T-bill line on every day after day 1**;
  - the relative drawdown reached **−6.66%** (2024-08-05) and ended at −4.5%.
- **Fix:** put these first in the report.

**F-4 · MEDIUM · The sensitivity overrides (C) reach the simulator, except that min_r does not reach the E1 limit price.**
- **What is wired correctly:**
  - `build_signal` reads `trend_score_min`, `trail_mult`, `mr_score_min`, `min_r` and `mr_atr_mult`. `manage` reads `trail_mult`, `mr_max_hold` and `trend_max_hold`.
  - All 14 variant trade lists hash differently from the base (`5ce22d24b99c6438`).
  - The observed maximum holds are E1 8/12 days and E2 48/61 days, as expected.
- **`precompute` hard-codes nothing for these fields.**
  - It stores raw fields for every MR and TREND_UP day.
  - The built-in R ≥ 2 and 2×ATR in `R.mr_plan` are bypassed whenever min_r or mr_atr_mult change (`lab.py:133-146`).
  - The fixed thresholds that remain are not in the grid, and that is fine: ADX < 25 routing, the 15%/12% stop caps and the 80-bar warm-up.
- **The leak:** the E1 limit price hard-codes R ≥ 2, mirroring `sizing_v66.py:55`:
  ```python
  hi = min(hi, int((s["target"] * f + 2 * stop) / 3 * 100))   # lab.py:257
  ```
  - **At ×0.8 (min_r 1.6):** signals with R 1.6–2 are generated and hold a slot overnight, then fail the limit. Limit rejects rise from 43 to 117, and there are *fewer* trades than base (127 vs 130).
  - **At ×1.2 (min_r 2.4):** fills are still allowed down to R = 2.
- **Probe with the cap following min_r**, i.e. limit ≤ (target + m·stop)/(1+m). The base hash is unchanged by the patch.

| Variant | Full period | Since 2025 | Trades | Report said |
|---|---|---|---|---|
| min_r ×0.8 | −1.78% | −0.79% | 147 | −1.76% / −0.51% / 127 |
| min_r ×1.2 | **−1.89%** | **−0.54%** | 123 | −0.83% / +0.05% / 125 |

- **Do not edit `lab.py`:** it is a CORE_FILE, so an edit would change the fingerprint.
- **Fix:** footnote the min_r rows, or quote these numbers as Tom's probe. The count of variants that flip stays at 1 of 14.

**F-5 · LOW · "1 of 14 flips" is fair; "up to about ±1% a year" is not.**
- **The actual moves against base:**
  - full period: **−1.00 to +1.65 pp**;
  - since 2025: **−2.29 to +2.47 pp**.
- **The 1 of 14 hurdle includes a fixed reserve cost of about 1.03%/yr (F-6).** Measured as the trading's own contribution, 3 to 4 of the 14 variants are positive. That pattern fits "no edge"; it does not show a negative edge.
- **The since-2025 +0.55% sits on a peak.**
  - Every E1 entry setting (score minimum, minimum R, ATR stop), moved in either direction, turns it negative: **6 of 6** after the F-4 fix.
  - This strengthens the report's own "rests on one year". "Scatter = noise" is right, but incomplete.

**F-6 · MEDIUM · Most of the −1.20%/yr is the cash reserve, not the trading.**
- **The test:** the same account with both engines off, holding HK$3,000 of settled cash at 0% and the rest in T-bills.
  - That account trails T-bills by **−1.03%/yr** (since 2025: −0.86%).
  - So the trading's own contribution is **−0.18%/yr** (since 2025: **+1.40%**).
- **Trading contribution by year:** 2022 stub −1.00, 2023 −2.82, 2024 +0.62, 2025 +2.58, 2026 +0.02.
- **The cost is mechanical.**
  - Positions are capped at 2 × 10% of HK$10,000, so they never exceed the HK$3,000 reserve.
  - The reserve is 30% of the sizing base, but **24% of the capital**. The report's "30% cash" should say so.
- **The near-zero trading total hides two offsetting engines:**
  - **E1 +US$81.4, E2 −US$81.7**;
  - fees of US$117.4 against gross trade P&L of +US$117.1.
- **The −1.2% assumes the reserve earns nothing.** The report itself notes that the Owner says Futu pays cash interest; this is not modelled.
- **Fix:** show the split (reserve cost vs trading) in the headline. As written, A and B mostly measure trading against a hurdle of about 1%/yr.

**F-7 · MEDIUM · The fee is the hinge, and the headline does not say so.**
- **A–D run only at real35.** For the same account, `income_scenarios.csv` gives:

| Fee scenario | Full period | Since 2025 |
|---|---|---|
| webull0 (no minimum) | **+0.18%/yr** | +1.91% |
| real35 (CRO estimate) | −1.20%/yr | |
| min1 | −3.92%/yr | |

- The fee moves the result more than any ±20% setting change.
- It does not rescue "add-on": at best the account roughly matches T-bills.
- **Fix:** "−1.2%/yr" must be labelled "at the CRO's estimated US$0.35 minimum fee (unverified, V-1)".

**F-8 · MEDIUM · Winner removal (D) is built correctly, but it is milder than it looks and it is not a bound.**
- **Mechanics check (`precompute(sub)`):**
  - SPY is kept;
  - the bull mask is identical (`Series.equals`);
  - the trading-date union is identical;
  - the remaining names' indicator frames are identical.
- **Why it is milder:** the notional cap is 10% of HK$10,000, about US$128. At that cap, **21 of the 38 names never completed a trade.**
  - Of the 10 names removed, **NVDA, AVGO, META, MSTR and LLY had 0 trades**. Their affordable signal days were 1/131, 0/148, 0/159, 1/45 and 0/152, so removing them changes nothing.
  - "Top 5" therefore removes 3 traded names; "top 10" removes 5.
- **Why it is not a bound:**
  - a January-2022 list would also include names that later fell out, and a 2026 list leaves them out;
  - removing winners cannot bound that;
  - E1 buys dips, which is exactly where names that later fell out of the index do damage.
- **Fix:** call D a "winner-dependence check", not a bound. Add the direction argument: the bias most likely flatters the result, so the true figure is more likely below −1.2% than above it. On this count the verdict is conservative.

**F-9 · MEDIUM · "The system does not ride winners because it trades short swings" is not supported.**
- **The mechanism is affordability (the notional cap), not holding period.**
- **Among the risers it could afford, it did make money:**
  - AMD (+US$19.5) and MU (+US$18.8) are the #2 and #3 contributors in `pnl_by_ticker.csv`;
  - the top-5 risers made **+US$32.7** against a total of −US$0.3;
  - removing them costs **0.71 pp/yr** (−1.20% → −1.91%), the largest effect in D.
- **Wording fixes:**
  - Keep "does not change the verdict": both runs stay negative.
  - Drop "barely depends".
  - Replace "made almost nothing" with "five of the ten were never traded: their price was above the ~US$128 cap".
- **The effective universe is 17 lower-priced names** (INTC +US$51.0, PFE, NKE, BAC, SBUX and others). The January-2022 list test should be read for that subset.

**F-10 · LOW · Traceability.**
- **Verified against the CSVs or console:**
  - 3.29 / 4.49 / −1.20 / 130 and +0.55;
  - 42 windows / 38% / −3.85;
  - all 15 rows of C and the whole D table;
  - the top-10 rises, and the best and worst names by P&L;
  - −US$0.3;
  - bootstrap 28–75% (27.60–75.42 at 60 months, `income_bootstrap.csv`), with real35 at the high end (75.42);
  - the fingerprint `2b7b62182068`;
  - "re-run is byte-identical";
  - SPY below its 200-day average on 2026-11-23 (722.29 vs 730.47).
- **Needs a fix:**
  - "about HK$150 a year": the CSV says **−HK$168/yr** (`超額HKD/年`).
  - "−US$0.3" leaves out two positions still open on 2026-11-23 (PFE and BAC, −US$6.2 at market).
  - "2024 −0.02%", "median −0.22%" and "best +3.68%": see F-1 and F-2.
  - "±1%": see F-5.
- **Note:** every run of the script rewrites `data/TBILL.csv` (through `IS.load`). The content is identical (md5 unchanged).

## Is the verdict fair?

**Directionally, yes.**
- **Too strong:** it presents "added nothing, −1.2%/yr" without conditions, yet about 1.03 of the 1.20 comes from a reserve assumed to earn 0%, and the fee is unverified.
- **Too weak:** it leaves out three things:
  - the account never got above the T-bill line in four years;
  - the since-2025 +0.55% breaks under every E1 entry change;
  - E2 lost US$81.7.

**Suggested headline:**
> At the CRO's estimated fee, from 2022-11 to 2026-11 the trading itself made about zero (−0.2%/yr; E1 +US$81, E2 −US$82). Keeping HK$3,000 as settled cash at 0% cost about another 1.0%/yr. Net: about 1.2%/yr (HK$168/yr) less than plain T-bills, and the account was behind the T-bill line on every day. With zero commission it would roughly match T-bills (+0.2%/yr), which is still not enough to call it an add-on.

## What I changed

**`strategy/v6.6/robustness_v66.py` only** (61 lines added, 9 removed; not a CORE_FILE, fingerprint still `2b7b62182068`):
- **R-1:** `anchored()` and `ret(..., floor)` measure every window from the previous close.
- **The 2022 stub row is now included,** so the yearly trades add up to 130.
- **New yearly columns:**
  - `冇交易戶口%` (the no-trade account);
  - `交易貢獻%` (the trading contribution);
  - `年內最大回撤%` (renamed from `最大回撤%`).
- **New console lines:**
  - the reserve vs trading split;
  - E1/E2 P&L and the positions open at the end;
  - full-period drawdown with dates, and the drawdown against T-bills;
  - the B non-overlapping phases;
  - D trade counts and affordable signal days for the removed names.

**Re-run to scratch:**
- The base case reproduces: 3.29 / 4.49 / −1.20 / 130.
- `sensitivity_live.csv`, `drop_winners.csv` and `pnl_by_ticker.csv` are **byte-identical**.
- `yearly.csv` and `rolling6m.csv` change as intended.

**For the CEO:**
- The committed `results/robustness/yearly.csv` and `rolling6m.csv` are now **stale**. Re-run `python robustness_v66.py` before committing.
- Then update §A, §B, the headline and the D reading (F-1 to F-9).
- Footnote the min_r rows (F-4).

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders.*
