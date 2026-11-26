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

## Update 2026-11-25 (evening) — Owner decisions, V6.6.4/V6.6.5, Webull snapshot, CRO rulings (append-only)

Recorded by the CEO, standing in for 腦大裝草. Supersedes the "Owner decisions pending" line and
switch condition 1 in the previous update.

- **Owner decisions** (2026-11-25, in-session AskUserQuestion; the Owner's selections, verbatim):
  - Work to continue: "One-click PC check + fixes (Recommended), Refresh Webull account
    (read-only), Finish 6160.HK / MSFT research".
  - **N-11:** "Stop new entries (Recommended)". Any uncleared S2 stops new entries until the trade
    is explained to the CRO.
  - **N-13 and N-15:** "--legacy flag (N-13), Max limit price (N-15)".
  - To-do list format: "Cantonese checklist file". The file is `strategy/v6.6/電腦待辦清單.md`.
- **V6.6.4** (c25f5ab / `0eb54f8e5872`):
  - Implements N-11, N-13 and N-15, plus N-6, N-14, N-16, N-19, N-20 and N-21, and `pc_check.py`.
  - **CRO: PASS** (`reports/risk/2026-11-25-v66-4-verification.md`). N-15 was partial.
  - The CRO **amended C-8**: if the open is at or below the system stop, do not buy.
  - Risk score 76.
- **V6.6.5** (77c713e / `847d34621a5f`):
  - CRO items N-24, N-25, N-26 and N-28.
  - Audit X-1: the selftest was coupled to the account size; it now checks the Owner's settings,
    then tests on defaults. CD-1 and CD-2.
  - Author run: selftest 117/117; equivalence 0/85,120; ledger_check PASS; baseline unchanged.
  - **CRO verification of the V6.6.5 diff: PENDING.**
- **Webull read-only snapshot, 2026-11-25** (`reports/risk/2026-11-25-webull-readonly-snapshot.md`):
  - one margin account; USD −12.06, unchanged since 13 Nov;
  - net liquidation ≈ HK$4,497 (estimate);
  - AVGO 2 shares, ≈ 102% of NLV.
- **CRO rulings, 25 Nov:**
  - **G-1 NOT MET:** deadline 16:00 ET Thu 3 Dec. Cure the debit **and** turn margin off or convert
    to cash. If uncured, the CRO recommends selling AVGO before 9 Dec.
  - **G-2:** conditions unchanged:
    - AVGO ≤ 6.6% of LNW;
    - 老詹's stop;
    - a decision record;
    - no adds.

    Without LNW by the 3 Dec close, the CRO recommends exiting before 9 Dec. Risk score for the AVGO
    hold as it stands: 25.
  - **C-6 NOT MET.** The 24 Nov interim option no longer applies to V6.6.
  - **C-7:** HK$4,497 is not approved; it would be a different, untested system. The Owner chooses:
    - **(A)** a separate cash or margin-disabled account, holding only the swing sleeve, funded with
      ≥ HK$12,500 of settled cash, with `account_hkd` 10,000 and `switch_date` set on the day; or
    - **(B)** shadow-only.
  - **N-11 self-certification:** accepted. The CRO matches each clearance against a real
    `reports/risk/` file at every review. An unmatched clearance counts as a process breach, and the
    hold is treated as never lifted.
- **Docs audit of V6.6.4** (`reports/committee/2026-11-25-v66-4-docs-audit.md`):
  - checklist and README: PASS WITH CORRECTIONS; HIGH findings X-1 and Q-1;
  - release note: FAIL.
  - All corrections are applied in 77c713e; the release note is rewritten. **Auditor diff-check
    PENDING.**
- **Canonical switch conditions** (these supersede the previous list):
  1. CRO verifies the code: V6.6.4 PASS; **V6.6.5 diff pending**.
  2. V-2 on the Owner's PC.
  3. V-3.
  4. V-1, without S4 triggered.
  5. C-6 and C-7 per the 25 Nov ruling.
  6. The docs-audit diff-check.
- **Interim:** no real-money orders from V6.6 or V6.4.2. V6.4.2 is paper only; V6.6 is scan and log
  only.
- **Dissent carried:**
  - CRO N-27: limit-price entries are more conservative than the backtest. The lab takes 83 of the
    88 entries the new rule skips.
  - CRO: at a US$0.35 minimum fee per side, OOS net EV is about +0.008% per trade. This is an
    estimate; V-1 is the economic gate.

**Correction 2026-11-25 (CRO D-1; append-only, so the line above stays):**
- The G-1 line above ("Cure the debit **and** turn margin off or convert to cash. If uncured, the
  CRO recommends selling AVGO before 9 Dec") is ambiguous.
- Per the CRO's ruling, **only a USD debit still uncured at the 16:00 ET close on 3 Dec triggers
  the recommendation to sell AVGO before 9 Dec.**
- Turning margin off or converting to cash is required for the account to be eligible for V6.6
  (C-6). It is not a sell trigger.
- **V6.6.5 CRO verification:** PASS, no new code findings. Code side of the switch clear; risk 76;
  B′ OFF (`reports/risk/2026-11-25-v66-5-verification.md`). Switch condition 1 is therefore
  **DONE** for V6.6.5 / `847d34621a5f`.

**Update 2026-11-26:** the Owner reported that he had cleared all debt. A read-only re-pull
(snapshot addendum) confirms it: USD cash is +0.66, so the **G-1 debit is cured**. The account is
still `INDIVIDUAL_MRGN`, so **C-6 is not met** and the account is not eligible for V6.6. G-2 is
unchanged: LNW is still due by the 3 Dec close. The Owner also asked whether V6.6 can run long
term as a source of "some extra return" (not market-beating). An income study was commissioned
(`reports/quant/2026-11-26-v66-income-study.md`).

**Update 2026-11-26 (later): V6.6.6 → V6.6.7, and the income study answered.**
- **Owner question (verbatim):** "evaluate is it possible to run it long-term although it cannot beat the market I will take this as providing some extra return for my living".
- **Code:**
  - V6.6.6 (`cf41d84`, `943960c97a9b`) added the live entry rule and idle-cash interest to the lab. CRO: PASS, with N-29.
  - V6.6.7 (`a496ba4`, `fae5fa5a7403`) made the fee gate use the live rule (N-29) and applied Tom's F-2, F-3 and F-8. CRO: **PASS**.
  - Selftest 131, 9 mutants caught, baseline byte-identical. Scanner, ledger and bot are unchanged.
- **Result** (`reports/quant/2026-11-26-v66-income-study.md` v2; HK$12,500 capital, 10,000 base, 30% settled cash, rest in T-bills; backtest 2022-11-30 → 2026-11-23):
  - The account makes about HK$430–770 a year, mostly T-bill interest (about HK$440–470).
  - The system's extra over all-in-T-bills is −HK$168 to +HK$166 a year (fee × order type); P(trailing T-bills over 5 years) is 28–75%; t between −0.91 and +0.84.
  - At the CRO's US$0.35 estimate with cancel-at-open orders, net EV per trade is −0.066%, which is **S4**.
  - HK$100k does not fix it.
- **Verdict (CRO and CEO):** the system can run long-term as a small sleeve once C-6, V-1 and (A) are met. It is **not** a living-income source; the income is the T-bills.
- **CRO rulings** (`reports/risk/2026-11-26-v66-6-verification.md`):
  - **R-1:** T-bill / government money-market funds allowed in the C-7 (A) account as cash equivalents, with ≥ 30% of `account_hkd` held as settled cash. The T-bill ETF is never counted as settled cash.
  - **R-2:** another base needs Tom's rerun and CRO review. Adding more capital at a 10,000 base is allowed.
  - **R-3:** 12 months of living money outside any risk asset; sleeve ≤ 10% of LNW (≥ HK$125,000 at 12.5k, else (B)); no planned withdrawals.
  - **R-4:** text corrections, applied.
  - **F-3:** a DAY limit is allowed only with an attached stop (OTO / bracket); otherwise cancel at the open. `--tif` is declared before V-1, and S4 will not be re-tuned. N-30 (scanner and bot print the 26 Nov C-8 wording) is required before DAY can be used.
- **Recommendation (CRO and CEO): (B) shadow-only** until V-1 passes on the live rule and there are ≥ 6 months of ledger. The choice is the Owner's.
- **Dissent / caution carried:**
  - **Tom F-4:** larger bases trade a different, pricier set of names (only 11–31 trades shared with the 10k run); not a case for a bigger base.
  - **CRO:** the DAY pass at US$0.35 rests entirely on 46 intraday fills with no live evidence.
- **Lesson:** L-012.
- **Audit 2026-11-26** (`reports/committee/2026-11-26-v66-income-audit.md`): PASS WITH CORRECTIONS on the study, checklist and README; no HIGH findings.
  - **Main finding:** the CRO's "until N-30 lands, V-1 is judged with `--tif open`" clause had been dropped in all three documents, along with parts of C-8 and R-3. Every drop pointed toward permission. **L-009 recurred.**
  - **Corrections applied:** S-1 to S-7, K-1 to K-8 and RM-1 to RM-4. The README's stale 25 Nov debit line was also updated.
  - **Routed to 床狗:** when a CRO ruling carries an "until X lands" clause, grep every Owner file for the ruling's identifiers (here N-30 and `--tif`) and carry the clause wherever the ruling is restated.

**Update 2026-11-26 (evening): Owner decisions and V6.6.8.**
- **Owner (verbatim):** "Well margin is allowed I bear the risk of this while paper trading please find a way to tell me through messages in trading view or python daily scan. I got another account for paper trading."
  - Broker answers: (1) T-bill ETF withholding: "Yes there is"; (2) cash interest: "Yes in futu, no in webull"; (3) attached stop on a DAY limit: "No".
  - AskUserQuestion: messages via **both** Telegram (Python) and TradingView. Open check: yes, but "yahoo finance is not a good way to get information. Either get it from webull or trading view". C-6 still applies for real money: **"Yes"**.
- **Recorded:**
  - **Paper trading.** V6.6 is paper-traded in a separate paper account; this is in effect B1 (B) plus paper fills, and the CRO is asked how to record the fills.
  - **Margin.** Margin stays on the real Webull account by the Owner's choice ("I bear the risk"). The G-1 structural requirement (margin off) is waived by the Owner for that account; the debit itself was cured on 26 Nov. G-2 is unchanged: LNW is still due by the 3 Dec close for holding AVGO through the 9 Dec results.
  - **C-6** still gates any real-money V6.6 trade.
  - **F-3:** the broker cannot attach a stop, so **(a) cancel-at-open governs**; V-1 uses `--tif open`; **N-30 is dropped**.
  - **Cash:** idle cash stays at Futu (interest), per R-1.5. A T-bill ETF nets about 70% of the T-bill rate after withholding.
- **V6.6.8** (`6fed2fd`, fingerprint `11b86e31c9cd`):
  - `notify_v66.py`: after-close Telegram message from the validated scan;
  - `notify_v66.bat` and `schedule_v66.bat`: Task Scheduler, TUE–SAT 06:30 HKT;
  - the scanner now shows positions on bear days (a gap found while reading the code);
  - Pine: max limit price, a close alert, and an open-check alert on TradingView data.
  - **Tests:** selftest 147; 9 mutants caught; results byte-identical.
  - **Not testable in the cloud:** schtasks, Telegram delivery, Pine compilation, live alert timing.
- **Proposed rule, for CRO confirmation:** place only orders that appear on **both** the Telegram ① list and a TradingView close alert. If the limits differ, use the lower one. If the two disagree, don't place, and ask the AI.
- **Reviews of V6.6.8, 2026-11-26:**
  - **CRO:** PARTIAL, with N-31.
  - **CRO rulings:**
    - **R-5:** paper fills go in the main `ledger/` before `switch_date`, with a switch-day archive procedure. Real and paper fills never share `fills.csv`.
    - **R-6:** the two-source rule is approved with amendments. Telegram is authoritative; the broker's order status governs at the open; no order if the Owner cannot be at the open.
    - **R-7:** the margin waiver is recorded with the CRO's dissent. `leverage: none` still binds, so any negative cash is a breach to cure within 3 sessions. G-3 stands. Keeping USD cash ≥ US$10 is recommended.
  - **Tom:** VALIDATED WITH CONCERNS (F-1 to F-11).
  - **Audit:** PASS WITH CORRECTIONS (H-1, M-1 to M-7, L-1 to L-5).
  - **Correction to the line above** (append-only), audit M-7: "Cash" means that if a future dedicated swing account is at Futu and its cash rate is close to the T-bill rate, idle cash stays as cash. That account must be separate from the Futu account holding 6160/3416. Rate and tax treatment were not obtained.
  - **Audit M-6:** the margin decision is recorded as the Owner's override of the CRO's structural recommendation. The CRO's dissent stands.
- **V6.6.9** (fingerprint `2b7b62182068`) fixes:
  - N-31;
  - Tom F-2 to F-8 and F-11;
  - audit M-1 to M-5 and L-1.

  Selftest 153; mutants caught; results byte-identical. CRO diff verification pending.
