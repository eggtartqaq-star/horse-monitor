# V6.6 Hong Kong execution test — the backtest vs what the Owner can actually do (2026-11-28)

**Run by:** CEO (皮褸黃). **Review:** Tom (pending). **Asked by:** the Owner (28 Nov, "HK reality test"). It was also the item the CRO deferred to Tom "before the first forward review" (decision record, V6.6.9 CRO bullet).
**Script:** `strategy/v6.6/hk_exec_v66.py`. It is a research tool. `lab.py` is not edited, and the rules fingerprint is still `2b7b62182068`.
**Output:** `strategy/v6.6/results/hk_exec/`. A re-run is byte-identical.
**Settings and data:** identical to the robustness test (`reports/quant/2026-11-27-v66-robustness.md`):
- Webull daily bars, 2022-11-30 → 2026-11-23;
- HK$12,500 capital on a HK$10,000 base;
- fee US$0.35 minimum + 10 bp per side (**estimate**, V-1 unverified);
- limit entry, open-only orders;
- 30% reserve at 0%; the rest in T-bills.

## Verdict: trading the way the Owner can from Hong Kong costs about another 0.4% a year. It does not change the overall conclusion.

| Version | System CAGR | vs T-bills / yr | Since 2025 / yr | Completed trades | Net EV per trade | E1 US$ | E2 US$ | Trading total US$ |
|---|---|---|---|---|---|---|---|---|
| **Lab** (backtest as tested) | 3.29% | **−1.20%** | +0.55% | 130 | −0.066% | +81.4 | −81.7 | −0.3 |
| **HK-1:** time exits at the next open; target intraday (as if the broker had OCO) | 2.85% | −1.64% | +1.24% | 128 | −0.359% | +46.7 | −81.6 | −34.8 |
| **HK-2:** time exits *and* E1 target at the next open (no OCO; **how the Owner trades now**) | 2.92% | **−1.57%** | +1.39% | 128 | −0.324% | +52.5 | −82.9 | −30.4 |

Over 4 years, HK-2 vs Lab costs **−0.37 pp a year**, or about **US$30 less trading P&L** (derived estimate). The worst drawdown is unchanged, at −3.49%.

## Why: the exits the Owner cannot take at the US close

The lab exits E1 at the **close of day 10**. 56 of 130 trades end that way; it is the most common exit. From Hong Kong the US close is at 05:00 HKT in winter (04:00 in summer), and the Owner sells at the next open instead.

For trades that exist in both runs (`next_open_vs_lab.csv`):

| HK exit | Matched trades | Average price vs Lab exit | Median | Worse than Lab | P&L difference |
|---|---|---|---|---|---|
| Day 10 → next open | 41 | **−0.31%** | −0.16% | 26 of 41 | −US$9.9 |
| E1 target → next open | 5 | +1.64% | +2.05% | 1 of 5 | +US$10.0 |
| Day 60 → next open | 1 | −0.42% | −0.42% | 1 of 1 | −US$0.4 |

- **Day-10 exits are the main cost.** Selling at the next open was worse than the close in about 2 of 3 cases.
- **The E1 target is rarely hit:** 6 times in 130 trades. Selling the morning after was slightly *better* in 4 of 5 matched cases, because prices kept rising after the target. Five cases is far too few to rely on.
- **The rest of the gap is path dependence.** A slot freed one day later changes which later signals get taken: E1 total +US$81 → +US$52.
- **Since 2025, both HK versions look better** than Lab (+1.24% and +1.39% vs +0.55%). This is the same path effect on a one-year sample, and it is not a reason to prefer them (see the robustness report §C: the since-2025 figures are a narrow peak).

## What could be done (options; nothing changes without the CRO and the Owner)

1. **Market-on-close (MOC) sell for day-10 and day-60 exits.** If the Owner's broker accepts MOC orders placed in the HK evening, the lab's close exit becomes executable, removing most of the −0.37 pp. This is not verified for Webull or Futu; it is a question for the Owner.
2. **OCO, if the broker supports it** (CRO F-8 allows a second sell only as OCO). HK-1 shows this does not help here, because the target is rarely hit.
3. **Change the rule to exit at the next open.** That would be a rule change: a new fingerprint, CRO review and new gates. It is not proposed; the effect is small and the system has no edge to protect.

## Effect on the overall verdict

- At the estimated fee, the realistic HK version trails plain T-bills by about **1.6% a year**, against the lab's 1.2%.
- This strengthens the robustness verdict: do not call it an add-on; T-bills are the income.
- It is input to today's committee review (keep, change or retire V6.6).

## Method and guard

- `hk_exec_v66.py` copies `lab.simulate` in memory and applies six exact text changes, each asserted to appear once:
  - a pending-exit map;
  - close pending exits at the next bar's open;
  - E1 target → pending (HK-2);
  - day 10 and day 60 → pending (HK-1 and HK-2);
  - clearing pending when a trade closes by another route.
- **Guard:** with both options off, the copy reproduces `lab.trade_hash` exactly, for `lab.AS_TRADED` (`3044c31236e877f0`) and for the live config (`5ce22d24b99c6438`). If `lab.simulate` changes so that a patch no longer applies, the script stops.
- **Unchanged:** stops (broker stop orders work at any hour, C-9) and entries (at the open, which the Owner must watch anyway under C-8).

*Research and decision support, not financial advice. No agent of this firm places orders.*
