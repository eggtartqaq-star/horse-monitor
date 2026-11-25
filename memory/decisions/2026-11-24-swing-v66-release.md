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
