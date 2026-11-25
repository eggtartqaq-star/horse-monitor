# Decision Record — Swing system V6.6 release (tools, not a position) — 2026-11-24

**Status:** OPEN. Released to the repo; the Owner has **not** switched yet. The switch waits on the conditions below.
**Type:** System / process decision. No order, no ticket. Recorded under standing rule 4 by the CEO,
standing in for 腦大裝草.
**This record is append-only.**

## Decisions (Owner, 2026-11-24)

1. **Both paths run and are logged.** The validated path ("bt", E2 needs today's high ≥ the 20-day
   high, as in manual §三 condition 3) is the live trading list. The old `daily_strong_signals` path
   is logged only.
2. **Engine 1 is traded exactly as backtested:** score ≥0.55, R≥2, all tiers. E2 takes slot
   priority. This meets the CRO's G-1.
3. **Delivery:** a new V6.6 package; the old V6.4.2 files are kept as a read-only reference.
4. **Scope:** scanner and safety checks, shadow ledger and review, Pine, Telegram bot.
5. **Cap:** A (10% flat) live. B′ (one E2 share ≤15% when its 1-share risk ≤1%) is off until
   G-1, V-1, V-2, V-3 and a dated CRO note. 20% and no cap were vetoed.

## Evidence at release (V6.6.1, rules fingerprint `c3f24ad80b06`)

- **Equivalence:** scanner rules = backtest rules on 85,120 day × ticker × path checks, 0 differences.
- **Fidelity:** rules match the Owner's V6.4.2 source line by line (Tom).
- **Ledger:** the resolver equals the lab trade for trade (38/38, 21/21, 8/8). Re-runs add no rows.
- **Self-test:** 65/65. Baseline trade-list hashes are unchanged from `results/baseline.json`.
- **As traded at A, 2022-11 → 2026-11:** validated path ≈2.2% CAGR (+US$116); old scanner path
  ≈0.8% (−0.8% in 2025–26). Neither is distinguishable from zero.

## Reviews

| Reviewer | Verdict | File |
|---|---|---|
| Tom, code | VALIDATED WITH CONCERNS for A. One BLOCKER (launcher never ran the scan), fixed in 2c85b90 | `reports/quant/2026-11-24-v66-release-code-review.md` |
| John (CRO) | SIGNED OFF WITH CONDITIONS. Risk score 72, rising to 76 after C-1 to C-5 | `reports/risk/2026-11-24-v66-release-cro-signoff.md` |
| Ai 管理層, audit | README FAIL. Commit messages, plan delivery and lab report PASS WITH CORRECTIONS. Safety claims PASS. README rewritten in V6.6.1 | `reports/committee/2026-11-24-v66-release-audit.md` |

## Dissent and escalations (verbatim in substance)

- **CRO, third escalation:** V6.6 does nothing about July CL-1. The Webull account is a margin account
  with a USD debit (13 Nov). No V6.6 entry may go into a margin account that carries a debit (C-6).
  Account size must be set to real equity (C-7).
- **Tom:** 2-slot portfolio results are path-fragile. A one-bar ADX slip flips OOS CAGR from +2.6% to
  −0.6%. Parity (V-3) must pass on the Owner's PC before any V6.6 number is trusted.
- **Audit:** the gates are flags the Owner sets himself. Structural control stops accidental
  enabling, not deliberate self-certification.

## Conditions to switch (open)

| # | Condition | Owner of task | Status |
|---|---|---|---|
| C-1 | Launcher has no fallback to the old scanner | CEO | Done in V6.6.1, pending CRO re-check |
| C-2 | Bot shows no plan or size for blocked or scanner-only signals | CEO | Done in V6.6.1, pending CRO re-check |
| C-3 | Ledger protected from as-of and partial-bar rows | Tom | Done, pending CRO re-check |
| C-4 | Fill checks: third slot, self-chosen stop, stale signal, blocked signal | Tom | Done, pending CRO re-check |
| C-5 | Re-verify after fixes | CRO | Open |
| V-2 | Self-test on the Owner's PC | Owner | Open |
| C-6 / C-7 | No debit on the margin account; `account_hkd` set to real equity | Owner | Open |

**Before B′:** V-1 (Webull fee note, then `lab.py --mode feecheck`), V-3 (parity on the Owner's PC),
B-2 to B-9, and a dated CRO note.

## Lesson

A structural control's failure message must never point to the uncontrolled path. The first
launcher told the Owner to fall back to V6.4.2, and it also never ran the scan, because of a batch
parenthesis. Two reviewers passed that block; the third caught it. **Run what you ship.**
Where you cannot run it (Windows batch, Pine), lint it statically and say so.

## Review dates

- First forward review: ≥30 closed E2 trading-path signals **and** ≥6 months of ledger.
- No cap return comparison before 100 trades.

## Update 2026-11-25 — CRO C-5 re-check, V6.6.2/V6.6.3, docs re-audit (append-only)

Recorded by the CEO, standing in for 腦大裝草. Based on the draft in the docs re-audit §6, updated
with the CRO's later results.

- **CRO C-5 re-check** at 7f74e2c / `c3f24ad80b06` (`reports/risk/2026-11-25-v66-c5-recheck.md`): PARTIAL.
  - C-1, C-2 and C-5 PASS. C-3 accepted, with C-3r due before the first review.
  - C-4 NOT closed: a stale fill across bear days was accepted (F1).
  - Pre-switch fixes required: C-4r, N-1 (hermetic selftest), N-5 (bot intraday).
  - B-4 failed: gates written as the string `"false"` passed.
- **V6.6.2** at be74475 / `0b05757d0076`: lands C-4r, N-1, N-5, C-3r, part of B-4 (N-7), B-11 and N-10.
  - CRO verification (`reports/risk/2026-11-25-v66-2-fix-verification.md`): **PASS**, all six items,
    by running the code. One new condition, N-12.
- **V6.6.3** at afa3b37 / `d293a03f7dad`: fixes N-12 (old-format ledger files are upgraded with a
  backup; an unknown column is refused), N-17 and N-18.
  - CRO (`reports/risk/2026-11-25-v66-3-n12-verification.md`): **N-12 PASS. The code side of the
    switch to A is clear, with no conditions. Risk 76. B′ OFF.**
  - selftest 85/85 (also under -O); equivalence 0/85,120; ledger_check PASS;
    `baseline.json` byte-identical. Fingerprint in `strategy/v6.6/results/release_stamp.txt`.
- **Docs re-audit** (Ai 管理層, `reports/committee/2026-11-25-v66-2-docs-reaudit.md`):
  - All four HIGH findings from 11-24 are closed.
  - First pass: README PASS WITH CORRECTIONS (A-1 HIGH: C-6 understated) and release note PASS WITH
    CORRECTIONS.
  - After corrections (20b781d): diff-check **PASS**. README PASS, release note PASS.
- **Canonical switch conditions** (these supersede the open rows of the table above):
  1. CRO code verification — **DONE** (V6.6.3 / `d293a03f7dad`).
  2. On the Owner's PC: the .bat double-click shows a completed scan; selftest 85/85 → V2.
  3. `parity_check` passes → V3.
  4. V-1 contract note, then `lab.py --mode feecheck`: ALL and OOS net EV > 0. Otherwise S4: no
     trading at any cap.
  5. C-6 and C-7:
     - C-6: the swing account must be cash or margin-disabled with no debit, shown by a statement
       or a read-only pull. The account as read on 13 Nov (`INDIVIDUAL_MRGN`, USD −12.06) does not
       qualify. CRO, 5th escalation.
     - C-7: `account_hkd` = real net liquidation value, reconciled monthly; existing positions
       (2 AVGO) recorded with `ledger fill`.
  6. Docs re-audit corrections — **DONE**.

  V-1 and V-3 are pre-switch by the CEO's choice. That is stricter than CRO sign-off §6.1, where
  they are B′ gates.
- **Interim:** the Owner continues V6.4.2 **in paper only**. CRO N-10: acceptable only as paper;
  the instruction is deleted at the switch.
- **Owner decisions pending:**
  - N-11: under A, any S2 → no new entries until explained to the CRO.
  - N-13: a `--legacy` flag for positions recorded under C-7.
  - N-15: print a maximum limit price per signal.
  - CRO 7.6: were orders placed from the 6 or 28 Sep scans?
  - Telegram token revoke.
- **Open before the first forward review (CRO):**
  - N-20: a hand-edited file with no final newline loses its last row on the next append.
  - N-16: the as-of marker is inferred.
  - N-14: unscheduled NYSE closures.
  - N-6: per-row settings recording (also needed before B′).
- **Dissent carried:**
  - CRO N-9: net EV crosses zero at a fixed charge of about US$0.25–0.40 per side. This is an
    estimate from hypothetical fees; the Webull schedule has NOT been obtained.
  - Tom: 2-slot results are path-fragile. A one-bar ADX slip moves OOS CAGR from +2.6% to −0.6%.
- **Observation for the first forward review:** in the 2-slot book, E2 averages −1.03% (49 trades)
  and E1 +1.85% (86 trades), while E2 holds slot priority. Test slot priority on forward data only.
- **Status:** still OPEN. The code and docs gates are closed; the Owner's gates (2–5) are open.
  SPY has been below its MA200 since 19 Nov (722.29 vs 730.47 at the 23 Nov close), so the system
  would not trade in any case.
