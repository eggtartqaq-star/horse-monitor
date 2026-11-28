# V6.6 Hong Kong execution test — the backtest vs what the Owner can actually do (2026-11-28, revised)

**Run by:** CEO (皮褸黃). **Review:** Tom, PASS WITH CORRECTIONS (`reports/quant/2026-11-28-v66-hk-execution-tom-review.md`). This revision applies his findings 4, 7, 8, 9 and 11.
**Asked by:** the Owner (28 Nov, "HK reality test"). It was also the item the CRO deferred to Tom "before the first forward review" (decision record, V6.6.9 CRO bullet).
**Script:** `strategy/v6.6/hk_exec_v66.py`. It is a research tool. `lab.py` is not edited, and the rules fingerprint is still `2b7b62182068`.
**Output:** `strategy/v6.6/results/hk_exec/`.
**Settings and data:** identical to the robustness test:
- Webull daily bars, 2022-11-30 → 2026-11-23;
- HK$12,500 capital on a HK$10,000 base;
- fee US$0.35 minimum + 10 bp per side (**estimate**, V-1 unverified);
- limit entry, open-only orders;
- 30% reserve at 0%; the rest in T-bills.

## Verdict: selling at the next open instead of the US close costs about nothing in price. What matters is when a sold position's slot frees up. Either way, V6.6 still trails T-bills (by 1.1–1.6% a year).

| Version | vs T-bills / yr | Since 2025 / yr | Completed trades | Net EV per trade | E1 US$ | E2 US$ | Trading total US$ |
|---|---|---|---|---|---|---|---|
| **Lab** (backtest: E1 target intraday, time exits at the close) | **−1.20%** | +0.55% | 130 | −0.066% | +81.4 | −81.7 | −0.3 |
| **HK-1:** time exits at the next open; target intraday (as if OCO) | −1.64% | +1.24% | 128 | −0.359% | +46.7 | −81.6 | −34.8 |
| **HK-2:** time exits *and* E1 target at the next open (no OCO; how the Owner trades now). A position due to be sold still counts as a used slot in that night's scan. | **−1.57%** | +1.39% | 128 | −0.324% | +52.5 | −82.9 | −30.4 |
| **HK-2-slot:** same as HK-2, but a position due to be sold at the next open does *not* count as a used slot that night | **−1.06%** | +0.76% | 130 | −0.031% | +91.1 | −82.1 | +9.0 |

## What the test shows

1. **Price: about zero** (Tom #7). Tom held the lab's own trades fixed and moved each exit to the next open:
   - all 56 day-10 exits: average −0.08% (t −0.4);
   - 6 E1 targets: +0.83%;
   - in total, about +US$5, or **+0.08 pp a year**: noise.

   The first version of this report said day-10 exits were "the main cost" (−0.31%, 26 of 41 worse). That table covered only the trades both runs took, and the claim is withdrawn.
2. **Slot timing decides the rest** (Tom #8).
   - The system's daily message counts a position as open until it is sold. A position due to be sold at the next open therefore still blocks a slot in that night's scan. That is HK-2, and it **matches how the scanner counts today**.
   - If such a slot counted as free (HK-2-slot), the result would be slightly *better* than the lab, because the Owner sells and buys at the same open.
   - The −0.37 pp for HK-2 is one path's draw: shifting the start date by 0–55 trading days gives HK-2 minus Lab between −0.37 and −1.17 pp, while HK-2-slot minus Lab stays between +0.11 and +0.15 pp (Tom #8).
   - **This is an operating-rule question for the CRO, not a market cost.** Changing how slots are counted would change the scanner (a core file), which means a new fingerprint and new gates. It is not proposed now.
3. **The Owner must be awake at the US open on every exit day,** not only on entry days (Tom #11). Exits are manual under F-8:
   - cancel the stop;
   - sell at market;
   - if the sale does not fill, re-place the stop at once.

   That fills minutes after the official open, and this slippage is not modelled.
4. **E1 targets are rare:** 6 of 130 trades.

## Options

- **Market-on-close orders are not an option** (Tom #9). An MOC sell must be entered before the session, so it would sit beside the broker stop (C-9): two sell orders for the same shares without OCO, which F-8 forbids. Cancelling the stop overnight instead would break C-9. The price gain it would bring is about zero anyway (finding 1).
- **OCO:** HK-1 shows no benefit; the target is rarely hit.
- **Slot counting:** a CRO question (finding 2). Even in the best case (HK-2-slot), V6.6 trails T-bills by about 1.1% a year at the estimated fee.

## Effect on the overall verdict

- **Unchanged:** do not call V6.6 an add-on; T-bills are the income.
- **Realistic range from Hong Kong:** −1.1% to −1.6% a year against plain T-bills at the estimated fee.
- This is input to today's committee review (keep, change or retire V6.6).

## Method and guard

- `hk_exec_v66.py` copies `lab.simulate` in memory and applies eight exact text changes, each asserted to appear once:
  - a pending-exit map;
  - close pending exits at the next bar's open;
  - E1 target → pending (HK-2);
  - day 10 and day 60 → pending;
  - clearing pending when a trade closes;
  - optional slot counting (HK-2-slot);
  - a probe that no pending exit is left at the end (Tom #4).
- **Guard:** with all options off, the copy reproduces `lab.trade_hash` exactly: `3044c31236e877f0` (`AS_TRADED`) and `5ce22d24b99c6438` (live). If `lab.simulate` changes so that a patch no longer applies, the script stops.
- Tom checked all 63 HK-2 next-open exits against the raw bars (#2).
- **Unchanged:** stops (broker stop orders, C-9) and entries (at the open, C-8).

*Research and decision support, not financial advice. No agent of this firm places orders.*
