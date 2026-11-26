# Review: V6.6.6 lab entry rule and the income study — Tom (Backtesting Engineer)

**Date:** 2026-11-26 · **Reviewer:** Tom (Dept 3)

**Scope** (HEAD `99b2177`, branch `claude/ai-agent-management-bw44yc`):
- `strategy/v6.6/lab.py` (cf41d84, V6.6.6, fingerprint `943960c97a9b`);
- `selftest.py`;
- `income_study.py`;
- `reports/quant/2026-11-26-v66-income-study.md` (the "report").

**How it was done:** findings only. I did not change any code or the report. Every number below is from my own runs on 2026-11-26 or from `strategy/v6.6/results/income_*.csv` at `99b2177`. All variant runs used a scratch **copy** of `strategy/v6.6`.

## Verdict: **VALIDATED WITH CONCERNS**

**What holds:**
- The code reproduces **byte for byte**.
- `entry_rule="limit"` matches the **written** live rule.
- The interest arithmetic is sound.
- The T-bill fix is correct.
- **Every figure in the report matches the CSVs.**

**The headline conclusion survives every variant I ran:** the income comes from the T-bills, and the trading adds roughly zero, with a sign that depends on the unverified fee. The monthly excess has t = −0.96 at real35 and +0.11 at webull0.

**Three items move the numbers enough that they must be fixed or disclosed before this reaches the Owner:**
1. **F-1:** the bootstrap is biased at the ends. Its 39% headline should be about 47%.
2. **F-2:** the reserve policy double-counts idle cash. That flips the 100k conclusion.
3. **F-3:** order handling (cancel at the open vs. a resting DAY order) is unspecified and is worth about HK$115–126 a year at 12.5k.

§2.3's "path dependence" reading is mostly wrong (F-4).

## What I ran

| Run | Result |
|---|---|
| `income_study.py` in a scratch copy (55 s) | All 4 output CSVs are **byte-identical** to the committed `results/income_*.csv` |
| `selftest.py` | **126/126**, exit 0, including the 9 V6.6.6 checks (lines 18–26 of the output) |
| `lab.py --mode baseline` | Identical to `results/baseline.json` |
| `config_v66.fingerprint()` | `V6.6.6 943960c97a9b` |
| Scratch variants, via switches in a copy of `lab.py` (defaults = original) | DAY-order fills; reserve that covers positions; entry-day exits; non-circular vs circular bootstrap; trade sets by account size |

## (a) Fidelity of `entry_rule="limit"`: **PASS against the written rule; one execution gap (F-3)**

**These match:**
- **The limit price.** `_max_limit_adj` is the same bisection as `sizing_v66.max_limit` (`sizing_v66.py:46-64`): the cents grid, close +1%, E1 limit ≤ (target + 2×stop)/3. It works on raw prices (`× f0`) and the lab's own base, `cfg.account_hkd`. Selftest's 363-case check passes.
- **Fill at the open when open ≤ limit.** A limit buy entered before the open executes at the opening price if that is at or below the limit. Shares stay at the close-time `sh0`, and the cap and risk hold by construction.
- **Floor and skip.** Open ≤ stop means no buy, and open > limit means skip. Both match C-8 as amended (`reports/risk/2026-11-25-v66-4-verification.md` §5) and the scanner text (`daily_scan_v66.py:283`, `README.md:125-127`).
- **Same-day stop on the entry bar.** The order is fill → `manage()` (stop checked first, then the trailing update), which matches "設止蝕單 right after the fill". In the 12.5k/webull0 run, **0 of 132 trades exit on their entry day**, so this assumption has no effect on the results.

**F-3 · MEDIUM · the instruction needs an order duration (TIF), and the lab models perfect compliance.**
- The rule says "open > limit → don't buy" and "open ≤ stop → don't buy". But a limit order placed before the open does neither by itself:
  - a **DAY** order keeps working and fills later at the limit if the price trades down to it;
  - it also fills at once on a gap below the stop.
- The Owner is in HK, and the US open is 21:30–22:30 HKT.
- **Measured** (scratch DAY-order variant, 12.5k, no interest):
  - 25 of the 43 skipped signals would have filled intraday at the limit;
  - the trading line moves from **+169 → +295** HK$/yr at webull0, and from **−9 → +106** at real35.
- That swing is as large as the whole trading line.
- **Fix:**
  - The CRO should specify the order duration: cancel unfilled at 09:31 NY, or let it work all day.
  - The lab should model whichever is chosen.
  - The report should show both rows.
- The floor case is 1 in this window (`income_scenarios.csv` 開市低過止蝕 = 1), so it is immaterial.

**Gaps between lab and live that are not new but feed this study (disclose them in §1.4):**
- The lab has no earnings guard. The live list blocks 0–5 days before earnings.
- The lab does not model the N-11 hold (stop new entries after an unexplained S2).
- The lab enforces the −10% monthly breaker, which is manual live (C-10).

**One edge case, INFO:**
- Shares are `sh0_raw × raw_factor(entry date)`. That is wrong only if a split falls between the signal and the entry. In that case it should be `× f0`, the factor at the signal date.

## (b) Interest accrual: **arithmetic PASS; reserve policy F-2**

- **Entry fee booked at exit.** Cash is overstated by about one side's fee while a trade is open. That is about US$0.48 at real35, so the interest effect is a fraction of a cent per trade. **Immaterial.**
- **Date alignment.** `cy_ret[d]` is BIL's return from d−1 to d. It is applied to the cash at the end of d. Effects:
  - the entry day loses one overnight accrual;
  - the exit day gains one.
  - Net about 0.
- There are **0 dates missing** on either side (T-bill vs. simulation dates over the window).
- Sizing uses the fixed base, so the trades are identical with and without interest, and the trading/interest split is exact.

**F-2 · MEDIUM · the reserve logic double-counts idle cash.**
- Code: `interest += max(0, cap + realized + interest − cost_basis − reserve) × r`. The report's §1.3 policy is "refill the reserve from T-bills after each buy".
- So when both slots are open, about 40% of the base sits idle. But each fill is ≤ 10% of the base (the limit guarantees that), so 2 slots never need more than the 20% reserve.
- Positions can therefore be paid from the reserve with settled cash and no refill: `interest base = cap + realized + interest − max(reserve, cost_basis)`.
- **Measured** (extra vs. T-bills, full period, HK$/yr; study → covered):

| Capital | webull0 | real35 |
|---|---|---|
| 12.5k | +16 → **+74** | −178 → **−120** |
| 25k | +207 → **+333** | +13 → **+139** |
| 100k | −370 → **+193** | −547 → **+17** |

- That **reverses §0's "scaling up does not fix this… trailed by HK$370–550"** and §3.4's "HK$1,200+ at 100k" hurdle. At 100k/real35, the interest given up falls from 1,238 to about 674.
- **Fix:** adopt the "covered" formula, or show both rows and label the refill policy as conservative.

## (c) T-bill correction and withholding: **PASS**

**The correction:**
- Exactly 4 BIL days fall below −0.25%: 2024-10-01 −0.379%, 11-01 −0.345%, 12-02 −0.336%, 12-19 −0.402%.
- **No** day sits between −0.25% and −0.03%, so there is no smaller missed ex-date.
- Replacing a missed ex-date with the same month's median daily return gives the correct total return for that day. BIL's price accrues between distributions.
- After the fix, the monthly T-bill returns (Jan 2023 – Oct 2026) range from 0.267% to 0.496%, with no outliers.

**Robustness, LOW:**
- A fixed −0.25% threshold will miss future un-adjusted distributions once the monthly payout falls below about 0.25%, i.e. at yields under about 3%.
- **Fix:** flag a day if its return is more than 0.15pp below that month's median.

**Withholding × 0.7:**
- This is reasonable as a labelled, unverified scenario: an HK resident has no US treaty rate, and the QII exemption is unconfirmed.
- It is applied fairly, to both the system's cash and the benchmark.

## (d) Bootstrap validity: **NOT VALID as reported (F-1)**

**F-1 · HIGH (it changes a headline number).**
- `boot()` draws block starts uniformly from `[0, n−3]`. That is a non-circular moving-block bootstrap, so the first and last 2 of the 49 months are under-sampled.
- **Measured:** the average monthly excess along the 60-month paths is +0.029% vs. the sample's +0.011% (webull0), and −0.079% vs. −0.097% (real35).
- **The result is biased upward.** The path mean sits above the sample mean, which implies the under-sampled end months are below average.
- 5-year P(behind T-bills), 5,000 paths:

| Fee | Non-circular (as shipped) | Circular | Circular + uncertainty in the mean (shift ~ N(0, sd/√49)) |
|---|---|---|---|
| webull0 | 38.9% | **46.6%** | **47.8%** |
| real35 | 80.6% | 84.4% | **75.9%** |

**Other limits:**
- Lag-1 autocorrelation is 0.06, so the 3-month blocks barely matter.
- The 60-month horizon is longer than the n = 49 sample.
- The standard error of the mean (0.10%/month) is about as large as the mean itself (−0.097 / +0.011%).

**Fix:**
- Make the blocks circular (wrap the series) and add uncertainty in the mean.
- **Change "≈ 39%" to "≈ 47%"** in §0, §2.5 and §6, and change "40–80%" in §4 to **"about 50–80%"**.
- State that both numbers are close to a coin flip, or worse.

## (e) Do the conclusions follow? Figure check

**All figures match the CSVs.** I checked every cited number against `results/income_*.csv`:
- §0 (both tables and the bullets);
- §1.2 (4.49%, 3.91%, 3.12%, 4.94/5.16/4.15%);
- all 12 rows of §2.1 and its notes (130 / 63 trades, 87.9%, 43 / 1);
- §2.2, §2.3 (all 8 rows), §2.4 (both fee lines, 4/5 and 2/5), §2.5, §2.6 (1.78 / 135 vs 1.33 / 130) and §2.7;
- §3.1: I recomputed 7.89% average position, days with 0/1/2 positions at 12.1 / 29.6 / 58.3%, and ≈ 11.5% of the base invested;
- the one-bar ADX citation is in `2026-11-24-v642-real-code-v66-lab.md:156`.

**F-4 · MEDIUM · the §2.3 "path dependence, not skill" reading is mostly wrong.**
- At larger bases the **universe changes.** A HK$10,000 base can only trade names under US$128.21, so the bigger accounts run a mostly different trade set:

| Base | Trades shared with the 10k run | Trades in names above US$128.21 |
|---|---|---|
| 20k | 31 of 132 | 72 |
| 40k | 18 of 129 | 90 |
| 80k | 11 of 120 | 91 |

- Those above-cap trades earned a **stable** +1.45 / +1.50 / +1.70% of base a year (real35, no interest, including the 2 trades still open at the end).
- The non-monotonic total comes from the cheaper remainder, where slot competition reshuffles the trades.
- **Fix:** reword as "a larger base admits pricier names, a different trade set; the rest is slot-order noise". Add that the 12.5k result is **not** a scaled-down version of any larger account. Do not read the above-cap trades' figure as a case for a bigger base: it is in-sample, and C-7 governs.

**F-5 · LOW · wording:**
- §0 gives "HK$420–620 a year", which covers webull0 and real35 only. The trading range quoted next to it (−340…+170) includes min1. Say so.
- In `income_scenarios.csv`, the 限價冇成交 and 開市低過止蝕 counts on the **out-of-sample** rows are full-period counts (43 / 1). Either relabel them or compute them for the out-of-sample window only.

**Conclusions that stand after F-1 to F-3:**
- **"Can't be counted on for living income" stands under every variant.** The best combination I ran, webull0 + DAY order + covered reserve, gives +214 HK$/yr over T-bills at 12.5k. At real35 it gives +9. Both are small next to the ≈ HK$600/yr of T-bill income and the noise.
- **"Small drawdowns" stands.** Maximum drawdown is −1.9% to −5.4% across the interest rows.

## Findings and exact fixes

| # | Sev | Where | Fix |
|---|---|---|---|
| F-1 | HIGH | `income_study.py:98-110` `boot()`; report §0, §2.5, §4, §6 | Circular blocks. In `boot`, set `xx = np.concatenate([x, x[:block]])` and draw `st = rng.integers(0, len(x), (n, nb))`, slicing `xx`. Add a per-path mean shift drawn from N(0, sd/√n). Restate as ≈ 47% (webull0) and ≈ 76–84% (real35). |
| F-2 | MEDIUM | `lab.py` interest line in `simulate` (step 4); report §0, §1.3, §2.3, §3.4 | Interest base `cap + realized + interest − max(reserve, cost_basis)` (positions are paid from the reserve, which needs no refill at ≤ 2×10%). Or show both. The 100k rows turn +193 / +17. |
| F-3 | MEDIUM | C-8 wording (CRO); `lab.open_position` limit branch; report §1.3/§1.4 | The CRO sets the order duration. If it is DAY, model "open > limit and low ≤ limit → fill at the limit", and model the floor as "fill at the open, exit at the open". Report both: trading line +169 / −9 vs. +295 / +106. |
| F-4 | MEDIUM | Report §2.3, §4 "path-fragile" bullet | Reword per (e) |
| F-5 | LOW | Report §0; `income_study.py:156` | Fee-scope wording. Compute the reject counts per window, or label them full-period. |
| F-6 | LOW | `income_study.py:46` `BAD_DAY` | Flag relative to the month's median, not a fixed −0.25% |
| F-7 | LOW | Report §1.4 | Add the remaining lab-vs-live gaps: no earnings guard, no N-11 hold, breaker enforced in the lab (manual live) |
| F-8 | INFO | `lab.open_position` limit branch | On a split day between signal and entry, use `sh0_raw × f0` |

**Scratch artefacts:**
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/tom3/scripts/checks.py`
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/tom3/scripts/sizes.py`
- the log: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/tom3/checks.log`

*Research review, not financial advice. Backtest figures are history over 2022-11-30 → 2026-11-23, not forecasts.*
