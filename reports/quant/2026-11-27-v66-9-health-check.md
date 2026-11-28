# V6.6.9 health check — tests, mutation sweep, Pine golden file (2026-11-27)

**Run by:** CEO (皮褸黃) in the cloud. The Owner asked (27 Nov): "Is there any things that you can do in current for upgrading or testing the system?" and chose the health check.
**Code under test:** V6.6.9. Rules fingerprint `2b7b62182068` is unchanged before and after. No core file (`config_v66.CORE_FILES`) was touched.

## Verdict: PASS. Ten test gaps were found and closed; no code bug was found.

- Every existing test passes.
- The first mutation sweep showed the self-test missed **10 of 23** deliberately planted bugs. All 10 were gaps in the tests; the trading code is correct.
- Ten new checks (`selftest_extra.py`) now catch **23 of 23**.
- The Pine golden file now keeps every row at least one scoring step away from a threshold.

## 1. Existing tests

| Test | Result |
|---|---|
| `selftest.py` | 153 ✅, 0 ❌, "全部通過" (about 12 s) |
| `selftest.py` under `python -O` | "全部通過" |
| `equivalence_check.py` | 85,120 comparisons, 0 differences |
| `ledger_check.py` | LEDGER CHECK PASS. The two S2 breaches it prints are the expected test fixtures. |
| `config_v66.fingerprint()` | `2b7b62182068`, matches `results/release_stamp.txt` |
| `golden_export.py`, scratch copy | Reproduces the committed `pine/golden_v66.csv` byte for byte |

**Can't run here:** `parity_check.py` (gate V-3). It needs `yfinance`, `ta` and the Owner's `dual_engine_v6_4.py`; `pip install` is not allowed in this session, and Yahoo is unreachable from the cloud. It stays an Owner PC step.

## 2. Mutation sweep

**Method.** Each mutant is a one-line change to decision-critical code in a scratch copy of the package. The self-test must then fail. Harness: `scratchpad/mut70/run.py`, 4 in parallel. Results are below.

| # | Mutant (file) | selftest.py alone | + selftest_extra.py | Check that catches it |
|---|---|---|---|---|
| M01 | B′ one-share rule also applies to E1 (`sizing_v66`) | killed | killed | CRO V-2 B′ E1 block |
| M02 | B′ one-share skips the risk check (`sizing_v66`) | killed | killed | CRO V-2 B′ E2 $185 |
| M03 | Limit cap close + 2% instead of + 1% (`sizing_v66`) | killed | killed | N-15, lab == sizing (7 checks) |
| M04 | E1 limit allows R ≥ 1.5 instead of 2 (`sizing_v66`) | killed | killed | N-15 E1 R ≥ 2 |
| **M05** | Limit skips the "can still buy at the close" test (`sizing_v66`) | **survived** | killed | **X01** |
| M06 | No notional cap in the position plan (`rules_v642`) | killed | killed | B′ and limit checks (10) |
| M07 | One extra share by risk (`rules_v642`) | killed | killed | fill S2 shares, limit parity |
| M08 | Bear gate off (`signals_v66`) | killed | killed | bear → no signal |
| **M09** | E1 stop cap 15% → 20% in `on_path` (`signals_v66`) | **survived** | killed | **X02** |
| M10 | E2 score threshold −0.05 (`signals_v66`) | killed | killed | signals == lab |
| M11 | E1 score threshold −0.05 (`signals_v66`) | killed | killed | signals == lab |
| **M12** | Earnings blackout 3 days instead of 5 (`guardrails_v66`) | **survived** | killed | **X03** |
| M13 | N-11 hold ignored for free slots (`notify_v66`) | killed | killed | Tom F-5 |
| **M14** | One extra free slot (`notify_v66`) | **survived** | killed | **X04** |
| M15 | Ledger allows a 3rd position (`ledger_v66`) | killed | killed | fill: 2 open → S2 |
| **M16** | Ledger notional cap × 1.5 (`ledger_v66`) | **survived** | killed | **X05** |
| **M17** | Ledger risk tolerance × 2 (`ledger_v66`) | **survived** | killed | **X06** |
| **M18** | Scanner calls bull if SPY > 97% of its MA200 (`daily_scan_v66`) | **survived** | killed | **X07** |
| **M19** | Scanner uses MA150 instead of MA200 (`daily_scan_v66`) | **survived** | killed | **X08** |
| **M20** | E2 stop cap 15% instead of 12% (`rules_v642`) | **survived** | killed | **X09** |
| **M21** | Open-check text drops "not filled → cancel" (`notify_v66`) | **survived** | killed | **X10** |
| M22 | Monthly breaker 20% (`config_v66`) | killed | killed | review S3 |
| M23 | Notional cap A 15% (`config_v66`) | killed | killed | settings self-check and 5 others |
| | **Total** | **13 / 23** | **23 / 23** | |

**What the survivors meant.**
- Before today, these could have changed with no test failing: the earnings blackout, the bull/bear switch, the E1/E2 stop caps, the 10% notional and 1% risk checks at fill time, the free-slot count, and the open-check instruction text.
- Today's code has all of them right; the new checks prove it, because they pass on the unchanged code.
- Parity on the Owner's PC (V-3) would catch M20 against the old engine. The rest had no guard at all.

## 3. Why the new tests are in a separate file

- `selftest.py` is part of the test fingerprint in `results/release_stamp.txt` (`selftest.py=da356fb483a3`). The Owner's PC check compares against that stamp.
- Changing `selftest.py` now would break the "153 項過" and the fingerprint match shown on the Owner's front page (`先睇我.pdf`) and in checklist C4, for the package the Owner already holds.
- So the ten checks live in `strategy/v6.6/selftest_extra.py`. It runs in the cloud, uses synthetic data only, and writes only to temporary folders, never to the Owner's `ledger/`.
- They will be merged into `selftest.py` at the next release, together with a new release stamp.
- The Owner does not need to run anything new.

## 4. Pine golden file

- **Finding (Tom 11-24 code review, INFO).** The golden rows were chosen at least 0.03 away from the score thresholds. One E2 scoring step is 0.0375 or 0.045, so a small TradingView data difference could flip one component and push a row across a threshold: a false mismatch.
- **Fix.** `golden_export.py` now requires a distance > 0.05 for both the E1 (0.55) and E2 (0.65) thresholds. `golden_export.py` is not a core file.
- **Result.**
  - Still 24 rows, with the same bucket mix (6 no-signal, 6 E2 trade, 5 E2 log-only, 5 E1, 2 E1 strong).
  - The minimum distance to a threshold rose from 0.035 to 0.07 (E1) and 0.073 (E2).
  - Four rows changed:
    - out: WMT 06-30, UBER 10-23, WMT 10-26, WMT 10-27;
    - in: WMT 06-29, PFE 09-28, NFLX 10-21, WMT 10-22.
- **The Owner's copy.** The golden file in the Owner's V6.6.9 package is still valid; it is just less robust. The new file ships with the next package.
- **Automated Pine run.** Still not possible: no Pine compiler outside TradingView. The 5-row manual check (checklist E2) remains.
- Tom's replica (`scratchpad/tom2/scripts/golden_pine_expect.py`) models Pine's share-size gate, which `golden_export.py` already applies (the A股數 column). So I did not commit it as a separate tool.

## 5. Files changed

| File | Change |
|---|---|
| `strategy/v6.6/selftest_extra.py` | new (X01–X10) |
| `strategy/v6.6/golden_export.py` | margin 0.03 → 0.05, with a comment |
| `strategy/v6.6/pine/golden_v66.csv` | regenerated |
| `strategy/v6.6/README.md` | tool list |

No CORE_FILES were changed, and the fingerprint is `2b7b62182068`.

*Research and decision support, not financial advice. No agent of this firm places orders.*

---

## Addendum, 2026-11-28: merged into `selftest.py`

- **Why now:** the Owner chose to keep and develop V6.6 and asked for the next PC package.
- **What changed:**
  - X01–X10 now live in `selftest.py` (function `_extra_checks_1128`), and `selftest_extra.py` is removed;
  - `selftest.py` passes **163** checks, normally and under `-O`.
- **Mutation sweep, re-run with `selftest.py` alone:** **23 / 23 caught** (`scratchpad/mut70/out_merged.txt`).
- **What is unchanged:** the rules fingerprint `2b7b62182068`.
- **Updated to match:**
  - `results/release_stamp.txt`, tests line: `selftest.py=c87d5b143531`;
  - the README, checklist C4 and `先睇我.pdf` now say 163.
