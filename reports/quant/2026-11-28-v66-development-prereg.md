# V6.6 development: pre-registration of hypotheses and pass marks (2026-11-28)

**Why this file exists.**
- The Owner decided on 28 Nov to KEEP AND DEVELOP V6.6, overriding the committee's RETIRE recommendation (decision record, 28 Nov entry).
- Everything tested so far (2022-11 → 2026-11) found no edge after costs, and the same data has been looked at many times.
- To keep "development" from turning into fitting the past, **the hypotheses, tests and pass marks below are fixed before any of them is run.** The git history of this file is the proof. After sign-off, changes are made only by dated addendum, never by editing the marks.

**Author:** CEO (皮褸黃). **Sign-off on the pass marks (required before any run):** Math King (overfitting) and John (CRO); see §5.

## 1. Common rules (apply to every hypothesis)

- **Control:** the current live configuration (`robustness_v66.live_cfg`), run in the same script on the same data. It is reported next to every variant.
- **Execution basis:** HK-2 (`hk_exec_v66.py`: time exits and E1 target at the next open; a slot is freed only when sold), unless the hypothesis is about execution (H4).
- **Fee:** the pass/fail decision uses the **real fee from the Owner's contract note (V-1)**. Until it arrives, results at real35 (US$0.35 + 10 bp, estimate) and webull0 (no minimum + 10 bp) are reported **as brackets only, with no verdict**.
- **Primary metric:** net CAGR minus plain T-bill CAGR on the same capital (`robustness_v66.excess_cagr`), full period.
- **Pass mark: all of these** at the real fee:
  - **P1:** full-period excess > 0.
  - **P2:** excess > 0 in **at least 5 of 7** non-overlapping half-year windows (2023H1 … 2026H1). A strategy with an edge should win most halves, not one lucky year.
  - **P3:** holds on the **2022-fixed universe**: the S&P 100 per the iShares S&P 100 ETF (OEF) N-PORT filing for early 2022 (SEC EDGAR; no Wikipedia), on Webull bars. Full-period excess > 0. Names that cannot be priced are listed, with the bias they leave.
  - **P4:** the worst drawdown is no worse than −10% (the monthly breaker size), and no single month is worse than −5%.
- **No tuning:** every V6.4.2 threshold stays fixed (score minimums, R, ATR multiples, hold days, caps). No parameter sweeps; no picking the best of several variants. Each hypothesis is run once, as written. A failed hypothesis is reported as failed and not re-tried in another form.
- **Multiple testing:** five hypotheses are tested, so some could pass by luck. P3 is the main guard, a different set of names. Anything that passes is still only a **candidate**: it then needs forward evidence (shadow log plus paper) before any real-money gate.
- **Real money:** unchanged. The CRO's veto stands until V-1, V-2, V-3, C-6, C-7 and R-3 are met and he signs in writing. Nothing in this file changes that.

## 2. Hypotheses

| # | Hypothesis | Change tested | Kind | Owner fact needed |
|---|---|---|---|---|
| **H1** | Fee drag shrinks with account size | Sizing base HK$20,000 and HK$40,000 (capital HK$25,000 / HK$50,000, the C-7 ratio), vs the current HK$10,000. Same rules. | Account size, not a rule change. R-3: the sleeve must be ≤ 10% of LNW. | Real fee; LNW |
| **H2** | The reserve's 0% interest is most of the gap | The HK$3,000 settled reserve earns the T-bill rate (a cash account paying about T-bill), vs 0% today. Same rules. | Account choice, not a rule change | Whether a cash account pays near the T-bill rate, and its rate |
| **H3** | Engine 2 adds no value | Engine 1 only (`engines=("E1",)`) | **Rule change** | Real fee |
| **H4** | Slot counting from Hong Kong | A position due to be sold at the next open does not block that night's slot (Tom's HK-2-slot) | **Rule change** (scanner) | Real fee |
| **H5** | The hindsight list is the problem | Replace the 38-name list with the 2022-fixed S&P 100 list. Sizing decides what is affordable, as now. | **Rule change** (universe) | Real fee; Owner's environment edit for SEC |

**Notes:**
- **H1 and H2 need no rule change.** If they pass, they are account decisions for the Owner, gated by R-3 and C-7.
- **H1 is checked on both** the 38 names and the 2022 list (P3).
- **H5 has no separate holdout:** its universe *is* the P3 universe. A pass on H5 is therefore only a candidate for forward testing, never evidence on its own.
- **Combinations:** only H2 may be combined with another hypothesis (H2 + H1, H2 + H3 …), because it is an account choice. No combination of rule changes is tested.

## 3. Tools and checks

- **Research script:** `strategy/v6.6/dev_v66.py`. It reuses `hk_exec_v66.make_simulate`, `robustness_v66.live_cfg` and `excess_cagr`, and `income_study.load`. A guard reproduces `lab.trade_hash` for the control. `lab.py` and every core file are unchanged; the fingerprint stays `2b7b62182068`.
- **Reviews:** Tom reviews every run. Math King writes a short overfitting note on any pass. The CRO reviews the risk on any pass.
- **Order:**
  1. H1/H2 brackets now, at the estimated fees, with no verdict;
  2. pass/fail once V-1 arrives;
  3. H3/H4 likewise;
  4. H5 and every P3 check once the 2022 list exists.

## 4. What happens next

- **Any hypothesis that passes P1–P4:**
  - becomes a V6.7 candidate: core change, new fingerprint, selftest additions, CRO diff review, Ai 管理層 audit;
  - then the Owner's PC gates (V-2/V-3);
  - then forward shadow and paper evidence, before any real-money gate.
- **If all five fail:** the firm reports that plainly, and recommends returning to the committee's RETIRE recommendation. The Owner decides.

## 5. Sign-off (pass marks fixed before any run)

*(Math King and John append their sign-off, or their requested amendments, below. The CEO decides on any amendment before the runs, and records it here.)*

### Math King, 2026-11-28

**SIGNED WITH AMENDMENTS.** Short answers: P1–P4 are too loose. Under zero edge, P1 and P2 together pass about 21% of runs (MK calc on synthetic noise; monthly sd 0.77%, derived from the robustness report's "t = −0.91 over 49 months"). P3 shares the period and many names, so it is not independent. P4 does not bind at this size (worst −3.49%). "5 of 7" is a weak sign test. H5 needs its own guard. A significance gate and a trade floor are missing.

1. **Family closed:** the verdict tests are H1, H3, H4 and H5 (m = 4). H1 is one test and passes only if both sizes pass. H2 and every combination are account arithmetic, not tests (A2). The "H2 + H3 …" list in §2 is closed. No other run is cited as evidence.
2. **Account facts are inputs:** before any verdict run, the Owner names in writing the account he will use, which fixes the fee schedule and the reserve rate (0% unless documented). Control and variants use the same facts. H2's effect is reported as arithmetic and cannot move a rule change from fail to pass. Changing account afterwards is a new registration.
3. **V-1 is in** (US$0 commission, no minimum; `reports/risk/2026-11-28-v1-fee-evidence.md`): cost per side = V-1 regulatory fee (about 0.2 bp) + Messi's written slippage estimate (10 bp until he issues one). Each verdict runs once at that cost: no brackets, no breakeven-fee search.
4. **H1:** with no minimum fee, H1's stated mechanism is gone. Any gain can only come from affordability (NVDA, AVGO, META, LLY become buyable on the hindsight list). I recommend withdrawing H1 before any run (then m = 3). If it is kept, it is judged on the 2022 list only.
5. **Already seen:** H4 is Tom's HK-2-slot (−1.06%/yr at real35, with HK-2-slot minus Lab of +0.11 to +0.15 pp; HK-execution report). H3's E1 +US$81 / E2 −US$82 split is in the robustness report. Their 38-name runs are descriptive only, and the verdict rests on the 2022-list run. Tom's V-1 check carries the Lab and HK-2 control rows only; any H1–H5 row in it is declared seen.
6. **P5 (new):** on the 2022-list run, the one-sided p-value for mean monthly excess > 0 (Newey–West SE, 3 lags, to cover the 60-day holds) passes Holm at family α = 0.05 (smallest p ≤ 0.05/m). Also report the deflated Sharpe with N = rows of `strategy/v6.6/results/trials.csv` (every variant run on 2022-11 → 2026-11 data, filled before the first run). DSR is disclosed, not gated, because the spread of trial Sharpes on 4 years is itself too noisy.
7. **Power, stated now:** P5 needs about +2.8 to +3.0%/yr excess (annual SE ≈ 1.33%). That exceeds the system's entire gross trading return (≈ 1.8%/yr: US$117.1 over 4 years on HK$12,500 at 7.8; MK calc). Pass chance: ≈ 24% at a true +2%/yr, ≈ 7% at +1%/yr. Expected result: all fail P5. That is the data's lack of power, and it is not grounds for a retry or a relaxed mark.
8. **P2 stays at 5 of 7** as a consistency check, not a guard. Under zero edge it passes 23% of runs, and 43% at +1%/yr; 6 of 7 would cut the latter to 17%. Each half is measured from the previous half's last close. Dec 2022 and Jul–Nov 2026 count in P1 only. A half with excess ≤ 0, or fewer than 5 entries, is not a win.
9. **P3 needs new names:** in the same 2022-list run, net completed-trade P&L must be > 0 over ≥ 30 trades on names outside the 38, and the overlap share is reported. For H5 this is its only partial holdout, so H5 cannot pass without it.
10. **Trade floor:** each verdict run needs ≥ 100 completed trades (the firm's 100-trade threshold, decision record "Review dates"). Fewer is "not evaluable" and counts as a fail.
11. **Concentration:** P1 must still hold with the best single ticker's completed-trade P&L removed from final equity. In the base case INTC made +US$51.0 against a trading total of −US$0.3.
12. **One look at the 2022 list:** before any run, commit the list (OEF N-PORT accession number), extend `SPLITS` to every name from issuer or exchange records, and repeat Tom's check for unadjusted price steps. Then run every verdict in one batch and commit the outputs before writing the report. No exploratory run on the list.
13. **P4 defined:** absolute drawdown of whole-account equity at daily closes, and calendar-month returns. Drawdown against the T-bill line is also reported. P4 is a risk check, not an overfitting guard.
14. **H5 and addenda:** a pass on H5 is evidence about the baseline, not a development gain. It is a live rule only once the live universe is fixed as "S&P 100 per the latest OEF N-PORT, refreshed on a set annual date". No addendum may loosen any mark once a verdict run exists.
