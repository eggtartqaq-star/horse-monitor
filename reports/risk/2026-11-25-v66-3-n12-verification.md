# CRO verification of V6.6.3: N-12 (ledger file upgrade), plus N-17 and N-18

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-25
**Scope:** `git diff d0268ce afa3b37 -- strategy/v6.6` only: `ledger_v66.py`, `selftest.py`, `ledger_check.py`, the version bump, README and the release stamp. **HEAD `afa3b37`, fingerprint `d293a03f7dad`**, computed in both the repo and a scratch copy.
- No other core file changed: sizing, signals, rules, guardrails, indicators, lab, scanner, bot and `owner_settings.json` are identical to `d0268ce`.
- Method: scratch copies (`git archive afa3b37` and `7f74e2c`, with `data/` symlinked in).
- No tracked file was modified, there was no broker access and no `pip install`.
- No temp dirs leaked. My scratch files were removed afterwards.

Standard: my V6.6.2 verification (`reports/risk/2026-11-25-v66-2-fix-verification.md`), N-12 option (a).

## Verdict

**N-12: PASS.** **The code side of the switch to A is now CLEAR, with no conditions.** The switch itself still waits on the Owner items, which are unchanged (below). **Risk score: 76**, no longer conditional. B′ stays OFF.

## Checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | My N-12 reproduction: V6.6.1 writes the ledger; V6.6.3 then does `fill open`, a bull-day scan, `show`, `review` and `fill close` | **PASS** | **V6.6.1 (`7f74e2c`)** wrote an as-of scan for 11-17 and `fill open AVGO` (18-column header, no `runs.csv`).<br>**V6.6.3:**<br>- Bull-day scan for 11-18 → **exit 0**. Holdings section ④ shows AVGO; signals and the first heartbeat were written.<br>- `fill open PFE` → "fills.csv 由舊版格式升級(加咗 ['logged_at'])" ("fills.csv upgraded from the old format"), with backup `fills.csv.bak-20261125-044109` (the exact 18-column original). The file now has 19 columns; the AVGO row is kept with `logged_at` blank, and the PFE row has `logged_at` set.<br>- Bull-day scan again → **exit 0**, with ④ listing AVGO and PFE. Dry-run → exit 0.<br>- `show` → exit 0. `review` → exit 0 (lists AVGO's S2; see N-13).<br>- `fill close AVGO` → OK, and `open_fills` = [PFE].<br>At `be74475`, the same sequence gave `ParserError: Expected 18 fields in line 3, saw 19` and scanner exit 1. |
| 2 | `signals.csv` and `runs.csv` take the same path | **PASS** | All three files are written only through `_append_rows`; `append_signals` and `append_run` both call it.<br>- An old-format `signals.csv` (no `partial_bar`) and `runs.csv` (no `n_failed`) were both upgraded by one scanner run, exit 0. Old rows were kept and both got backups.<br>- Column history (`git show` per commit): `SIGNAL_COLS` is unchanged since `3a87f3c` and `runs.csv` is new in V6.6.2. `fills.csv` (18→19) is the only real-world upgrade. |
| 3 | The scanner no longer exits 1 on an upgraded ledger | **PASS** | Exit 0 on bull days (11-18) and on bear days.<br>When a file has an **unknown** column, the scanner exits 1 with "❌ … 有唔識嘅欄位 … 冇改動" ("unknown column, nothing changed") and leaves the file byte-identical. This is intended: it is fail-loud, and the launcher shows "掃描出錯" ("scan error"). |
| 4 | Regression | **PASS** | - `selftest.py` **85/85**, exit 0, under normal, `-O` and `PYTHONOPTIMIZE=2` (scratch), and normal and `-O` in the repo.<br>- `equivalence_check`: 85,120 / 0 differences.<br>- `ledger_check`: PASS, and it **no longer leaks a temp dir** (N-17 closed).<br>- `lab.py --mode baseline`: `baseline.json` sha256 `081a485c231a…`, **byte-identical** (`git diff --no-index --exit-code` → 0; repo `git diff --exit-code` → 0). All `results/` files are identical. |
| 5 | Mutation test (each fix re-broken in a copy) | **PASS** | - `_migrate_header` replaced with a no-op → selftest crashes with the N-12 `ParserError` (exit 1).<br>- Unknown-column refusal skipped → caught.<br>- Backup removed → caught.<br>- Review keeps "off" rows (my M15) → now caught by the N-18 case. **N-18 closed.** |
| 6 | Edge cases | See residuals | - Reordered header → rewritten in canonical order.<br>- Header-only old file → OK.<br>- CRLF old file with no final newline → OK.<br>- Zero-byte file → treated as new. |

## Residuals (none blocks the switch)

- **N-20 (LOW–MED, pre-existing; before the first forward review): appending to a current-format file that lacks a final newline silently loses a row.** Probe: a `fills.csv` with the current header whose last row (AVGO) had no trailing newline. After one append, `read` returned only the new row. AVGO vanished from `open_fills`, so the 2-slot count went blind with **no error**.
  - Code-written files always end in a newline, so this needs a hand edit, which the ledger rules already forbid.
  - The same append logic has been in place since `3a87f3c`.
  - Fix: before appending, write `\n` if the last byte is not one, and add a selftest case.
- **N-21 (LOW):** a file that is not empty but has no header (BOM-only, or a blank line) crashes the upgrade path with `EmptyDataError`. `read()` already crashed on such a file, so this is pre-existing and fails loudly.
- **N-22 (LOW):** a file that V6.6.2 had **already** mixed (an 18-column header with 19-column rows) is not repaired. The upgrade path raises the same `ParserError` and leaves one `.bak` per attempt. This only matters if V6.6.2 ran `fill open` on a V6.6.x ledger on the Owner's PC. V6.6.2 was never authorised for use and V-2 has not been run, so the exposure is about nil, and the failure is loud.
- **N-23 (cosmetic):** a reordered header prints "加咗 []" ("added []"). With an unknown column in `runs.csv` on a bull day, the signals are written but the heartbeat is refused. That is fail-safe: exit 1, and fills would be flagged stale.

## Owner items (unchanged; these now gate the switch alone)

1. **V-2:** copy the whole folder. Double-click `掃描_v66.bat`, run `python selftest.py` and expect **85**, with fingerprint **`d293a03f7dad`**. Send the log, then set `"V2_代碼測試": true` without quotes. An existing V6.6.0 or V6.6.1 `ledger\fills.csv` is now upgraded automatically, with a backup.
2. **C-6, 5th escalation:** the swing account must be cash or margin-disabled with no debit. Webull as last read (`INDIVIDUAL_MRGN`, USD −12.06) does not qualify.
3. **C-7:** set `account_hkd` to the real net liquidation value, and record existing positions with `ledger fill`. They will carry S2 until N-13 lands.
4. **V-1:** one Webull contract note, then `feecheck` (N-9 / S4).
5. **V-3:** `parity_check.py` output.
6. **Decisions:** N-11, N-13 and N-15. Telegram token revoke. CRO 7.6. Delete README L3's paper-trading line at the switch.
7. **Firm side, before B′:** Mo Peter's VaR and Mario's stress results (B-7).

This is research and decision support, not financial advice. No V6.6 code can place an order; the Owner places every order.

**For 腦大裝草:** `2026-11-25 · CRO N-12 verification at afa3b37 / d293a03f7dad: PASS. V6.6.1 fills.csv → V6.6.3 fill/scan/show/review/close all OK (auto-upgrade + .bak); signals/runs same path; scanner exit 0; selftest 85 (normal/-O), equivalence 85,120/0, ledger_check PASS (N-17 closed), baseline byte-identical; N-18 closed. Code side of switch to A CLEAR, no conditions. Residual N-20 (no-final-newline append drops a row; pre-existing) before first review. Switch gated on Owner items V-2, C-6, C-7, V-1, V-3. Risk 76. B′ OFF.`
