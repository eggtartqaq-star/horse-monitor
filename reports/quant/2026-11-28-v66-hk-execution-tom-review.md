# V6.6 HK execution test: Tom's review (2026-11-28)

**Reviewed:** `strategy/v6.6/hk_exec_v66.py` (commit `f1447fd`), `strategy/v6.6/results/hk_exec/*.csv`, `reports/quant/2026-11-28-v66-hk-execution.md`.
**Method:** I reran the test myself into a scratch folder. I checked the switched-on behaviour against raw bars, and ran a slot variant and a start-date shift. I did not edit `hk_exec_v66.py`, `lab.py` or any other core file.

## Verdict: PASS WITH CORRECTIONS

**What is right.** The script's mechanics are correct, and the guard is real.

**What is wrong.** The headline is wrong: the −0.37 pp/yr is **not** a cost of selling at the next open.
- **Price effect: about zero.** With the lab's trade path held fixed, moving the exits to the next open changes the result by about +0.08 pp/yr. That is not significant.
- **Where the gap comes from.** The whole gap is a modelling choice: a position marked to exit at the next open still uses up its slot in that evening's scan.
- **Free that slot, and HK-2 beats Lab.** HK-2 then comes out +0.14 pp/yr *above* Lab.

**What still stands.** The overall conclusion is unchanged: V6.6 trails T-bills in every version.

**What must be corrected.** The "costs about 0.4% a year" line and the market-on-close (MOC) option.

## Findings

1. **The rerun reproduces.** All 5 CSVs are byte-identical. Both guard hashes match: `3044c31236e877f0` (`AS_TRADED`) and `5ce22d24b99c6438` (live). The run changed no file in the repo.

2. **All six patches are correct.** I checked this against raw bars, separately from the script:
   - All 63 HK-2 next-open exits fill at the open of that ticker's next bar.
   - Day-10 exits are exactly 10 bars after entry. The day-60 exit is 60 bars after entry.
   - The stop is still checked before the target on the trigger bar. That is the same cautious order the lab uses.

3. **Entry day: correct.** I traced the code path: target touched on the entry bar → exit marked pending in step 1 → step 2 skips the position (`edate == d`) → it closes at the next open. The sample has 0 such cases, so the data never tests this path.

4. **`id(p)` is safe as a key.** A position leaves `open_pos` only through `close_trade`, which pops its key. Two live objects cannot share an id.
   - I added a probe, `assert not hk_pending`, just before `simulate` returns. It passes in Lab, HK-1 and HK-2.
   - Recommendation: add the probe as a seventh patch, so that a later change to `lab.simulate` cannot leave a stale id unnoticed.

5. **Data end: consistent.**
   - A pending exit still open at data end closes at the last close, labelled 數據結束 ("data end"). It is left out of the completed-trade count (2 such trades in each version), and the equity curve already values it at that close.
   - The 130 vs 128 completed trades is a path difference, not a data-end effect.

6. **The guard is real but checks one side only.**
   - **What it proves.** With both options off, the patched copy matches `lab.simulate`. It does so on both entry routes (deviation and limit), and the check that each patch target appears exactly once catches changes to the source.
   - **What it does not test.** The behaviour with the options switched on. Finding 2 covers that.
   - **What the hash leaves out.** `trade_hash` leaves out `shares` and `pnl_usd`. That is fine here, because no patch touches position sizing.

7. **CORRECTION: the price effect is about zero.** I kept the lab's own trade path and moved each lab exit to the next open:

   | Lab exit | n | Mean vs lab exit | t | Worse | US$ |
   |---|---|---|---|---|---|
   | Day 10 | 56 | −0.08% | −0.4 | 33 | −0.1 |
   | E1 target | 6 | +0.83% | +0.8 | 2 | +5.8 |
   | Day 60 | 1 | −0.42% | n/a | 1 | −0.4 |
   | **All** | 63 | | | | **+5.3 ≈ +0.08 pp/yr** |

   - The report's matched table (day 10: −0.31%, 26 of 41 worse) covers only part of these exits. The 15 lab day-10 exits that HK-2 never took averaged about +0.5% (derived).
   - The report's line "Day-10 exits are the main cost" is not supported.

8. **CORRECTION: the gap comes from slot timing.** Variant HK-2-slot: a position already marked to exit at the next open does not count towards `max_positions` in that evening's scan. The reasoning is that the Owner knows the exit is due when the scan runs, and can sell and buy at the same open.

   | Version | vs T-bills / yr | Since 2025 | Trading US$ | Max DD |
   |---|---|---|---|---|
   | Lab | −1.20 | +0.55 | −0.3 | −3.49% |
   | HK-2 (as reported) | −1.57 | +1.39 | −30.4 | −3.49% |
   | HK-2-slot | −1.06 | +0.76 | +9.0 | −3.49% |

   - **This is an operating-rule question.** Whether the slot frees at the scan or at the fill is for the CRO to decide. It is not a market cost.
   - **The −0.37 is one path's draw.** I moved the start date forward 0–55 trading days, in steps of 5 (12 runs). HK-2 minus Lab ranged from −0.37 to −1.17 pp. HK-2-slot minus Lab stayed between +0.11 and +0.15 pp.
   - Patch used, applied after the report's six patches. Old line:
     `if not unlimited and len(open_pos) + len(pending) >= cfg.max_positions:`
     New line:
     `if not unlimited and len([q for q in open_pos if id(q) not in hk_pending]) + len(pending) >= cfg.max_positions:`

9. **CORRECTION: Option 1 (MOC) conflicts with F-8.**
   - **Why it conflicts.** An MOC sell must be entered before the closing-auction cutoff, so it waits all session next to the C-9 stop. That makes two sell orders for the same shares without OCO, which F-8 forbids (`memory/decisions/2026-11-24-swing-v66-release.md`, F-8 ruling).
   - **The workaround is also barred.** Cancelling the stop before bed breaks C-9.
   - **What would make it possible.** MOC is only possible if the broker links the MOC and the stop as OCO. That is not verified for Webull or Futu.
   - **There is little to gain anyway.** By finding 7, the price effect it would remove is about zero.

10. **The stop at the day-10 open: no change needed.** If the open is below the stop, the stop fills at about the open anyway: `e1_gap_fill` is on for E1, and E2 always fills a gap at the open. The price is the same either way; only the label differs.

11. **Realism the test does not model (minor; entries have the same gap).**
    - **Fill price.** Exits fill at the official open price. Under F-8 the real sequence is manual: cancel the stop, sell at market, and re-place the stop if the sale does not fill. That fills minutes later, and the slippage is not modelled.
    - **Owner's hours.** HK-2 needs the Owner awake at the US open on every exit day, not only on entry days. The report should state this.

12. **Integrity checklist** (scope: this patch only).
    - **No lookahead:** PASS. Each decision uses bar d and acts at the d+1 open.
    - **No holdout contamination:** PASS. No parameters are fitted.
    - **Costs:** the US$0.35 + 10 bp estimate is carried over; the actual fee (CRO item V-1) is still unverified.
    - **Survivorship, point-in-time data, splits:** taken from `lab.py` as is; not reviewed again here.

## Corrections required in the CEO report

- **Headline.** Replace the verdict line and "HK-2 vs Lab costs −0.37 pp a year" with findings 7–8: the next-open timing has no measurable price cost, and the −0.37 pp comes from slot timing and path noise.
- **Day-10 claim.** Withdraw "Day-10 exits are the main cost."
- **Option 1 (MOC).** Mark it as conflicting with F-8 and C-9.
- **Effect on the overall verdict.** State that V6.6 trails T-bills by 1.1–1.6% a year, depending on how slots are handled (Lab: 1.2%). The conclusion is unchanged.

*Research only. No broker calls. Nothing committed.*
