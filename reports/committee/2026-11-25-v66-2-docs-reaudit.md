# V6.6.2 docs re-audit: README and release note (Ai 管理層, AI Auditor, Dept 9)

**Date:** 2026-11-25
**Auditor:** Ai 管理層
**Scope:**
- `strategy/v6.6/README.md` (Cantonese; the Owner's manual)
- `reports/quant/2026-11-25-v66-release.md` (English; the Owner-facing release note)
- Consistency with `memory/decisions/2026-11-24-swing-v66-release.md` (append-only; **not edited**)

**Audited state:** branch `claude/ai-agent-management-bw44yc` at `be74475` (`.git/logs/HEAD:68`; message in `.git/COMMIT_EDITMSG`). Both documents are in the index.

**Prior audit:** `reports/committee/2026-11-24-v66-release-audit.md` (README FAIL, HIGH F-1, F-2, F-3, F-10).

**Method limits:**
- I had Read, Grep and Glob only. No shell, and **I executed no code.**
- The selftest count is static: I counted `check(` call sites and loop multiplicity.
- I computed the SPY 200-day MA by hand from `data/SPY.csv`, rows 1002–1201. The sum of (close − 730) over the 200 closes is +94.27, so MA200 = 730.47. I re-added every group pairwise to check the arithmetic.
- I could not compute SHA-256. The fingerprint, the 82/82 pass result, equivalence 0/85,120 at V6.6.2, ledger_check, and "baseline unchanged" are therefore **claims by the author (CEO run)**. The CRO's V6.6.2 re-check is still pending.

---

## 0. Verdicts

| Document | Verdict | Why |
|---|---|---|
| `strategy/v6.6/README.md` | **PASS WITH CORRECTIONS.** A-1 (HIGH), A-2, A-3 and X-1 (MEDIUM) **block banner removal.** I will diff-check them; no full re-audit is needed. | **All four HIGH findings from 11-24 are closed** (§1). The safety framing holds: the banner says do not switch, the .bat and scanner failure texts say "today don't trade", and nothing points to V6.4.2 as a fallback. One new HIGH remains, a text defect: **the banner's leverage condition (C-6) is weaker than the CRO's binding wording.** Following the README, the Owner could close banner item 4 by repaying a US$12 debit and keep trading in a margin account. The CRO's 11-25 ruling and the release note both say that account does not qualify. |
| `reports/quant/2026-11-25-v66-release.md` | **PASS WITH CORRECTIONS** | Every number checks out against `summary.csv`, `baseline.json`, the CRO reports, Tom's reviews and `data/SPY.csv`. Estimates are labelled. The CRO's dissent (N-9, C-6 4th escalation, N-11) and Tom's fragility finding reach the Owner here. Corrections:<br>- Its switch criterion ("until the open items in §4 close") differs from the README's and the decision record's (X-1).<br>- The audit row implies the README FAIL is resolved.<br>- It understates the CRO conditions ("C-1…C-7").<br>- Two wording overstatements. |
| `memory/decisions/2026-11-24-swing-v66-release.md` | Not graded (append-only, not edited) | Its last state is V6.6.1 (`c3f24ad80b06`, 65/65, C-5 "Open", "third escalation"). Text to append is in §6. |

**Severity count:** HIGH 1 · MEDIUM 3 · LOW 15.

**Direction of the residual errors:** the material ones understate a constraint (C-6, C-7, C-8, the CRO condition list) or overstate validation ("穩陣"/"robust", "one code base", author-run re-verification labelled "Re-verified"). That is the same lean as on 11-24, but much smaller. Counter-evidence: the README is **stricter** than the CRO on V-1 and V-3, which it makes pre-switch.

---

## 1. The four HIGH findings from 11-24: closure

| # | Old finding (quoted from `2026-11-24-v66-release-audit.md`) | New text and code | Status |
|---|---|---|---|
| **F-1** | "The B′ switch-on procedure, done exactly as written, disables the daily scan … The .bat then refuses to scan and tells the Owner to use the V6.4.2 `掃描.bat` … Separately, ① and ③ size from A only." | - `selftest.py:139-142` is now mode-aware: it expects `B_PRIME` when `authorised`, otherwise `A`.<br>- `selftest.py:144-189` tests every refusal on a temporary config and restores it in `finally`.<br>- `selftest.py:191-196` runs the `-O` case in a subprocess with an unapproved note, so it is still refused in the authorised state.<br>- `掃描_v66.bat:21-26`: 「自我測試失敗 —— 今日唔好交易 … 修好之前唔好用任何版本落單」, with no V6.4.2 reference. `selftest.py:202-205` lints that "V6.4" is absent.<br>- `daily_scan_v66.py:158, 203-211`: ① and ③ size with `Z.live_mode()`.<br>- README §四 lines 164-171 give the procedure through `owner_settings.json` plus the CRO's code change at line 161-162.<br>- I walked selftest statically in both the fully authorised state and the half-configured state (gates true, note filled, B′ off). Every check still passes, including the fill S2 cases (`size(…, live_mode())` gives the same 2 / 5 shares under B′) and the S4 pending check. | **CLOSED.** Residual LOW in A-11: the note must match `APPROVED_BPRIME_NOTES` exactly, and the B′ list is shorter than the CRO's. |
| **F-2** | "Step 4 has the Owner edit `config_v66.py` (V3 → True). That file is fingerprinted, so on day one the stamp no longer shows `69b0780a3d5b` … regenerate the fingerprint from a real `--dry-run` and commit that output." | - Gates, B′ switches, `account_hkd` and `real_fee` moved to `owner_settings.json` (`config_v66.py:23, 47-59, 66-88`; `owner_settings.json:3-16`).<br>- `CORE_FILES` (`config_v66.py:92-94`) excludes it, and `selftest.py:200` asserts that.<br>- README lines 49, 58 and 70 point to `owner_settings.json`.<br>- README §四 lines 161-162 disclose the one deliberate fingerprint change (the CRO's approval edit). | **CLOSED for the mechanism.** Two residuals:<br>- **A-3 (MEDIUM):** `parity_check.py:15,115` still tells the Owner to edit `config_v66.py`.<br>- **X-2 (LOW):** no committed stamp output, so `0b05757d0076` is author-asserted. |
| **F-3** | "The summary keeps the per-trade framing and drops the result that reverses it … Change 「細但穩陣」 to 「細、對參數唔敏感,但 OOS 統計上未同零分開」." | README lines 210-213: 「但喺你真正嘅 2 倉組合入面,情況倒轉:引擎二每筆平均 −1.03%(49 筆),引擎一 +1.85%(86 筆)。原因未確定 …」. Line 217: 「兩者都同零分唔開」. These match `summary.csv` rows 39-40. The cause wording matches lab report §4 (M1 E2 OOS +0.02%, `summary.csv:82`). | **CLOSED in substance.** Residual LOW in X-3: 「細但穩陣」 is still at line 208, and the release note says "the robust one". |
| **F-10** | "Put a top banner in the README, 「未正式發佈:等 Tom 審核、CRO 簽署、決策記錄」, and remove it only when all three are committed." | - README lines 3-16: 「⛔ … 未可以轉用 … 四樣都完成之後,呢個方框會刪除,並寫入決策紀錄」.<br>- Tom's review is FINAL (`2026-11-24-v66-release-code-review.md:4`).<br>- The CRO sign-off is FINAL, and the C-5 re-check is committed.<br>- The decision record exists.<br>- The Owner summary exists (the release note, in the index). | **CLOSED.** Residual MEDIUM in X-1: three different switch lists, and the docs re-audit (a CRO §6.1 precondition) is missing from the banner. |

**Other 11-24 findings (brief):**
- **Closed:**
  - F-4: README §六.3 mapping, plus the regenerated golden file with `A股數`.
  - F-5: README lines 100 and 195.
  - F-6, F-7 and F-8: the CRO recheck shows B-9 PASS.
  - F-11, apart from A-6.
  - F-12 and F-13.
  - F-14: now stated as a note, but see A-4.
  - F-15: it is in the release note §4.8, though not in the README.
  - F-18: Tom §7 says the Owner's bot also blocked HK.
- **Partial:**
  - F-9: B-5 is partial per the CRO.
  - F-16: the decision box says 「所有級別」.
  - F-22: see A-11.
- **Open (LOW):**
  - F-17: X-4.
  - F-23: A-12.
- **Outside scope, noted:** the lab report that README line 207 cites still says "parity … ≥99%" and "selftest (16/16)", and has the screenshot inference at §6.7 (`2026-11-24-v642-real-code-v66-lab.md:153, 157, 170`).

---

## 2. Claims checked (claim / source / result)

### 2.1 README

| # | Claim (line) | Checked against | Result |
|---|---|---|---|
| 1 | Version V6.6.2 (1, 79) | `config_v66.py:20-21` | VERIFIED |
| 2 | SPY below its 200-day line since 2026-11-19 (4) | `data/SPY.csv:1198-1201`. Hand MA200 on 11-23 = **730.47**; derived MA200 on 11-18 ≈ 730.02, 11-19 ≈ 730.20, 11-20 ≈ 730.29. Closes: 11-18 730.20 (above by +0.02%), 11-19 715.87, 11-20 689.81, 11-23 722.29 (all below). | **VERIFIED.** The 11-18 margin is only +0.18 points. The line is undated and "等都冇損失" is unconditional → A-9 |
| 3 | 「82 項」 (6, 49) | `selftest.py`: Grep `^\s*check\(` = **77** sites. Line 136 sits in a 6-case loop (cases at 131-133): 77 + 5 = **82**. The 5 checks at 70-84 (`if len(tr):`) and the 6 at 357-414 (`if found:`) both run on any passing run. | **VERIFIED (static).** The 82/82 pass is UNVERIFIED (author-run) |
| 4 | Settings live in `owner_settings.json`; editing it does not change the fingerprint (8, 49, 58, 70) | `config_v66.py:23, 66-88, 92-94`; `selftest.py:200` | VERIFIED. Contradicted by tool output → A-3 |
| 5 | CRO C-5 PARTIAL; C-4r, N-1 and N-5 required (10) | `2026-11-25-v66-c5-recheck.md` §0 and §4 | VERIFIED |
| 6 | "V6.6.2 已經修好,等 CRO 確認" (11) | Static presence:<br>- C-4r: `ledger_v66.py:162-198`; `daily_scan_v66.py:151-152, 226-228`.<br>- N-1: `selftest.py:337-339`, which `guardrails_v66.py:71` honours through a global lookup; temp dirs are removed at 226, 274, 331, 419 and 493.<br>- N-5: `telegram_bot_v66.py:103-108, 139-161`. | PRESENT in code. "Awaiting CRO" is stated correctly |
| 7 | C-6: 「孖展戶口有欠款 → 唔准開新倉」 (13); 「如果有負現金 / 欠款,先還清先開新倉」 (67) | CRO recheck §5.2: "show … that it is a cash account or has margin disabled, with no debit. The Webull account as last read … **does not qualify**". Sign-off C-6 (`…cro-signoff.md:360-363`). Release note lines 109-113. | **UNDERSTATED / CONTRADICTS the release note** → **A-1** |
| 8 | E2 needs 「今日高 ≥ 20日高」 (20) | `signals_v66.on_path`; Tom §3 | VERIFIED |
| 9 | PFE and CVX E2 signals in the 6 and 28 Sep screenshots had no breakout on recompute; values matched "to the decimal" (22-23) | `data/CVX.csv:1127-1161`: High 208.13 on 09-04 vs 20-day max 211.44 (09-03); 204.84 on 09-25 and 206.53 on 09-28 vs 215.99 (09-15). `data/PFE.csv:1127-1161`: 28.28 on 09-04 and 09-25, 28.45 on 09-28, vs 28.79 (09-03). | "No breakout" is **VERIFIED from data**. "吻合到小數位" is **UNSOURCED**: no screenshot or recompute output is committed → A-7 |
| 10 | 「一套規則,所有工具共用 … 回測都用同一套代碼」 (25-26) | `lab.py:37-38` imports `rules_v642` but **not** `signals_v66`. Its path gate `build_signal` is separate and held equal by `equivalence_check.py`. | OVERSTATED → X-4 |
| 11 | `ta` is still needed for parity (43) | `parity_check.py:3, 57` | VERIFIED. No install command → A-12 |
| 12 | Parity: 10 stocks, 3 years, both paths; indicator diff < 0.01; signal-day agreement ≥ 98% (55, 57) | `parity_check.py:27-29, 63, 71-77, 87-108` | VERIFIED (ATR uses a relative 0.01%) |
| 13 | 「嗰部分由 `equivalence_check.py` 同離線掃描測試處理」, referring to `daily_strong_signals.py`'s flow (56) | `equivalence_check.py:16-36` compares `signals_v66` with `lab.build_signal`; neither is the Owner's `daily_strong_signals.py`. Selftest 8c tests `daily_scan_v66`. | **MISATTRIBUTED** → A-6 |
| 14 | `lab.py --mode feecheck --fee-min … --fee-bp …` (62) | `lab.py:667-669, 690-691`. Pass rule: ALL **and** OOS net EV > 0 (`lab.py:637`). | VERIFIED |
| 15 | Stamp lines (78-82) | `daily_scan_v66.py:52-58`; `config_v66.py:111-114`. The real stamp also prints 未過關卡 and Python versions (59-60). | VERIFIED (excerpt) |
| 16 | Fingerprint `0b05757d0076` (79, 85) | Appears only in README:79, 85, release note:6 and `COMMIT_EDITMSG:27`. No committed tool output. | **UNVERIFIED** → X-2 |
| 17 | 「美股開緊市」 → no ledger write (86) | `daily_scan_v66.py:116-119, 133`; `selftest.py:357-359` | VERIFIED |
| 18 | 「[X] 掃描出錯」 → don't trade (88) | `掃描_v66.bat:15, 28-33`; `daily_scan_v66.py:304` | VERIFIED. L-008 compliant |
| 19 | Heartbeat on every run; one missed day makes earlier signals stale (90-91) | `daily_scan_v66.py:151-152, 226-228`; `ledger_v66.py:166-174`. "Every run" means every non-dry, post-close, live-data run. | VERIFIED |
| 20 | Sections ①–④ and ranking (95-100) | `daily_scan_v66.py:158-222, 246-291` | VERIFIED |
| 21 | `fill` commands (107-111) | `ledger_v66.py:431-450` | VERIFIED |
| 22 | S2 list (113-123), against `cmd_fill` | Each bullet maps to code:<br>- 2 positions: `ledger_v66.py:150-151`<br>- over cap: 154-158<br>- risk: 159-160<br>- no live / scan-only: 181, 205-206<br>- stale / bear / missed session: 169-179<br>- no `runs.csv`: 169-170<br>- guard-blocked: 183-185<br>- A = 0: 188-189<br>- stop more than 1¢ tighter: 192-193<br>- shares above system size: 195-198 | **VERIFIED, 10/10.** The risk threshold is 1.05×, not 1% → A-5 |
| 23 | 「留意 … review 會列出」 (125) | The note is written at `ledger_v66.py:203-204`, but `review()` reads flags only for S1 and S2 (353-358) and its notes are 月熔斷 and 財報 only (366, 376) | **FALSE** → A-4 |
| 24 | Review has three parts (134-138) | `ledger_v66.py:320, 341, 345, 371-384` | VERIFIED (closes F-13) |
| 25 | Review at ≥30 closed E2 **and** 6 months (140) | `ledger_v66.py:330` | VERIFIED |
| 26 | S1–S4 and their consequences (145-150) | `ledger_v66.py:355-368, 380-393`; CRO B-9 PASS | VERIFIED. Under A, the S2 consequence 「返去 A」 is a no-op (CRO N-11) → A-10 |
| 27 | B′ procedure (156-171) | `config_v66.py:125-155`; selftest walk in §1 | VERIFIED. Exact-match requirement and CRO B-2…B-11 missing → A-11 |
| 28 | After B′ is enabled, the list uses B′ sizing (171) | `daily_scan_v66.py:158, 203` | VERIFIED |
| 29 | Bot behaviour, including intraday (175-182) | `telegram_bot_v66.py:139-161, 196-210`; `selftest.py:461-480` | VERIFIED |
| 30 | Pine title 「Swing V6.6.0 雙引擎」 (186) | `pine/swing_v66.pine:17` | VERIFIED |
| 31 | Golden mapping 3/2/1/0 (193); 「`A股數` 欄係 0 嘅行」 (194) | `pine/golden_v66.csv`: no row has `A股數` = 0. The 7 no-signal rows are **blank**; every signal row is ≥ 1 (Tom F-7). | Mapping VERIFIED; the "0" rows **do not exist** → A-8 |
| 32 | `lab.py` modes and paths (201) | `lab.py:664-671` | VERIFIED |
| 33 | Research figures (208-218):<br>- 49 trades −1.03%; 86 trades +1.85%<br>- 2.2%/yr, +US$116<br>- 0.8%/yr, −0.8% in 2025-26<br>- E1 OOS −0.16% | `summary.csv` rows 40, 39, 38, 47, 53 and 27; `baseline.json` (bt 135 / 2.2056 / 116.32; scan 96 / 0.8206). IS ends 2024-12-31 (`lab.py:666`). | VERIFIED. 「穩陣」 → X-3 |
| 34 | File table (224-227) | Equals `CORE_FILES` (10 files) | VERIFIED |
| 35 | `ledger/` and `data/` are not uploaded (229) | `.gitignore:3-4` | VERIFIED (`owner_settings.json` **is** tracked → A-12) |
| 36 | 「冇任何程式會落單」 (231) | Re-grepped at be74475 (case-insensitive) for broker, order and HTTP-write APIs over `*.py/*.bat/*.pine`. The only write is Telegram `sendMessage` (`telegram_bot_v66.py:267`). `webull` hits are cost-model labels (`lab.py:84, 97, 506, 516`). The new `subprocess` call (`selftest.py:190-196`) runs only a fixed `config_v66` check. | VERIFIED |

### 2.2 Release note

| # | Claim (line) | Checked against | Result |
|---|---|---|---|
| 1 | "NOT yet cleared for use. Keep paper trading on V6.4.2 until the open items in §4 close" (3-4) | README banner (4 items); decision record 47-57; CRO sign-off §6.1 | **INCONSISTENT** across the three documents → X-1 |
| 2 | Fingerprint `0b05757d0076`; `lab.py` now included (6) | `config_v66.py:92-94` includes `lab.py` ✓. Value: see README #16. | Inclusion VERIFIED; value UNVERIFIED → X-2 |
| 3 | SPY below MA200 on 19, 20 and 23 Nov (722.29 vs 730.47) (7-8) | Hand computation (README #2) | **VERIFIED.** "Right now" is undated → B-3 |
| 4 | Decision record path (10) | Exists | VERIFIED |
| 5 | `daily_strong_signals.py` lacks the breakout and lists strong-tier E1 only (15-16) | Tom review §3 | VERIFIED |
| 6 | "The scanner, ledger, Telegram bot and lab all import the same `rules_v642.py` / `signals_v66.py`" (19-20) | `lab.py:37-38` and `ledger_v66.py:35-37` do not import `signals_v66` | **FALSE in part** → X-4 |
| 7 | 85,120 checks, 0 differences (21) | 38 tickers (`rules_v642.py:30-38`) × (1,200 − 80) (Grep: all 41 CSVs have 1,200 rows) × 2 = 85,120 ✓. Zero differences: CRO K-2 at V6.6.1 and Tom; author-run at V6.6.2. | Count VERIFIED; V6.6.2 result UNVERIFIED |
| 8 | B′: `check_config()` raises unless every gate is set and a dated CRO note exists (23-25) | `config_v66.py:143-152`. It also requires the note to be in `APPROVED_BPRIME_NOTES`, stated at line 86. | VERIFIED |
| 9 | Ledger and `fill` S2 list (26-31) | README #22 | VERIFIED (summary) |
| 10 | Launcher runs the 82-check selftest; no fallback (33-34) | `掃描_v66.bat`; README #3 | VERIFIED |
| 11 | Bot behaviour; token handling (35-38) | `telegram_bot_v66.py`; CRO C-2 PASS; Tom F-12 | VERIFIED |
| 12 | Pine golden checklist has 24 rows (39-40) | `golden_v66.csv`: 24 data rows | VERIFIED |
| 13 | Window 2022-11-30 → 2026-11-23 (42) | `baseline.json:2-5` | VERIFIED |
| 14 | Table: 135 / 96 trades; ≈2.2% (+US$116) / ≈0.8%, −0.8% in 2025-26; E1/E2 +1.85% (86) / −1.03% (49) and +1.54% (35) / −0.14% (61) (44-48) | `summary.csv` rows 38, 39, 40, 47, 48, 49, 53; `baseline.json` | **VERIFIED, all 13 figures** |
| 15 | Neither path is distinguishable from zero (50) | CIs [−0.03, +2.25] and [−0.77, +2.15] (rows 38, 47) | VERIFIED |
| 16 | "E2's edge is the robust one"; E1 OOS −0.16% (51-52) | Row 27 ✓. E2 per-signal OOS CI [−0.02, +2.27] (row 28). | Number VERIFIED; "robust" → X-3 |
| 17 | One-bar ADX slip: OOS CAGR +2.6% → −0.6% (53-54) | `2026-11-24-v66-lab-tom-review.md:125-127` (−0.62) | VERIFIED |
| 18 | N-9: "about US$0.25–0.40 per side", labelled an estimate from hypothetical fees (55-59) | `2026-11-25-v66-c5-recheck.md:57, 71` (K-12: +0.293% at US$0.25, −0.014% at US$0.40) | VERIFIED and properly labelled (rule 5 ✓) |
| 19 | Reviews table (63-69) | Tom ✓; CRO "C-1…C-7" vs sign-off C-1…C-10 plus B-1…B-9; audit row "README FAIL → rewritten" with no re-audit status | → B-1, X-1 |
| 20 | V6.6.2 fix list (71-90) | Static presence (README #6). `config_v66.py:41-44, 138-152`; `CORE_FILES` includes `lab.py`; `掃描_v66.bat:15, 28-33`; `FILL_COLS` includes `logged_at` (`ledger_v66.py:47, 211`) | PRESENT. B-4 is only partly done → B-2 |
| 21 | "Re-verified in the cloud on V6.6.2: self-test 82/82 … baseline unchanged" (92-96) | Commit message only; author-run | UNVERIFIED → X-2 |
| 22 | Owner steps 1–8 (100-123) | CRO recheck §5 items 1–6; C-6 wording at 111-113 is complete; N-11 at 115-117 is accurate | VERIFIED |
| 23 | B′ prerequisites (125-126) | CRO recheck §4 and §5.7; sign-off §6.2 | VERIFIED |
| 24 | Not done: the .bat is linted statically, Pine not compiled (130-132) | L-008 ("say so") | VERIFIED; compliant |

---

## 3. Findings: severity, location, exact fix

### HIGH

**A-1 · HIGH · `strategy/v6.6/README.md:12-14` and `:67`. The leverage condition C-6 is understated and contradicts the release note.**
- **What the README says:**
  - The banner, item 4: 「孖展戶口有欠款 → 唔准開新倉」.
  - §一.6: 「如果有負現金 / 欠款,先還清先開新倉(CRO 條件 C-6)」.
- **What the CRO says** (11-25 re-check §5.2, the latest ruling): "Show, from a statement or a read-only pull, that it is a cash account or has margin disabled, with no debit. The Webull account as last read (13 Nov: `INDIVIDUAL_MRGN`, USD −12.06) **does not qualify**. Until this is cured, no V6.6 entry may go into it." The release note (lines 109-113) says the same. Firm limit: `leverage: none`.
- **Consequence:** following the README, the Owner can tick banner item 4 by repaying US$12.06 while staying in a margin account. That is the uncured CL-1 state, escalated four times.
- **Caveat:** the 11-24 sign-off (`…cro-signoff.md:363`) also lists "clear the debit and fund the swing sleeve in settled cash (behavioural, interim)" as a remediation option. If John still accepts that, he must say so in writing, and the README must then quote his wording, including the settled-cash and evidence parts. Until then the 11-25 wording binds.
- **Fix, README lines 12-14 (replace):**
  ```
  > 4. **戶口(CRO 條件 C-6 / C-7):**
  >    - 講明短線用邊個戶口,用月結單或者唯讀截圖證明佢係**現金戶口(或者已經關咗孖展)而且冇欠款**。
  >      11 月 13 日讀到嘅微牛孖展戶口(USD −12.06)**唔合格**,淨係還清欠款唔夠。未證明之前,V6.6 唔准開任何新倉;
  >    - `owner_settings.json` 嘅 `account_hkd` 改做嗰個戶口**真正**嘅淨值(唔計借貸),每月同每次提款後再核對;
  >    - 戶口入面現有嘅持倉(例如 2 股 AVGO)要記入記錄簿(點樣記由 AI 話你知;會被標 S2,係預期)。
  ```
- **Fix, README line 67 (replace):**
  `   - **孖展(CRO 條件 C-6):** 要係現金戶口,或者已經關咗孖展,而且冇欠款 —— 用月結單或唯讀截圖證明畀 CRO 睇。你 11 月 13 日嘅微牛孖展戶口(USD −12.06)唔合格,淨係還錢唔夠。`

### MEDIUM

**X-1 · MEDIUM · README `:3, :8-16`; release note `:3-4, :67`; decision record `:47-57`. Three different switch criteria, and the docs-audit precondition is missing.**
- **The four lists:**
  - README banner: V-2 + V-3 (item 1), V-1 (item 2), CRO V6.6.2 confirmation (item 3), C-6/C-7 (item 4).
  - Release note: "until the open items in §4 close". That is 8 items, including the Pine compile, the Telegram token, the Sep-scan question and the N-11 decision.
  - Decision record: C-1 to C-5, V-2 and C-6/C-7. It has no V-1 or V-3, which it lists as "Before B′".
  - CRO sign-off §6.1 (`…cro-signoff.md:286-293`): C-1 to C-5 verified, **"Tom's review and the audit are committed"**, and the PC selftest. V-1 and V-3 are B′ gates there, and C-6 governs real money.
- **The audit status:**
  - The CRO's 11-25 §5.6 lists "the README is still at audit FAIL, re-audit … not seen" as open.
  - The release note row "README FAIL → rewritten in V6.6.1" implies that item is closed.
  - Making V-1 and V-3 pre-switch is stricter and acceptable. But it is a CEO/Owner choice and must be recorded as one.
- **Fix, README line 3:** change 「直到下面四樣全部完成」 to 「直到下面五樣全部完成」.
- **Fix, README line 16:** change 「四樣都完成之後」 to 「五樣都完成之後」.
- **Fix, README:** insert after line 14:
  ```
  > 5. **AI 審計:** 2026-11-25 文件重新審計(`reports/committee/2026-11-25-v66-2-docs-reaudit.md`)要求嘅修正全部落實。
  ```
- **Fix, README line 9 (replace):**
  ```
  > 2. **微牛成交單據(關卡 V-1):** 確認真實收費,再跑 `lab.py --mode feecheck`。淨 EV ≤ 0(S4)→ 呢個戶口規模下唔好用呢個系統。
  ```
- **Fix, release note lines 3-4 (replace):**
  "**Status: released to the repo, NOT yet cleared for use.** Keep paper trading on V6.4.2 until the five switch conditions in the README banner close: CRO verification of V6.6.2; V-2 and V-3 on your PC; V-1 (with S4 not triggered); C-6/C-7; and the docs re-audit corrections. Items 5–8 in §4 are needed but do not block the switch. This note is research tooling, not financial advice."
- **Fix, release note line 67 (replace):**
  "| Ai 管理層 (audit) | 11-24: README FAIL. 11-25 re-audit of V6.6.2: README PASS WITH CORRECTIONS (A-1 HIGH blocking), release note PASS WITH CORRECTIONS | `reports/committee/2026-11-24-v66-release-audit.md`, `reports/committee/2026-11-25-v66-2-docs-reaudit.md` |"
- **Decision record:** append the canonical list (§6).

**A-2 · MEDIUM · `strategy/v6.6/README.md:12-14, :66`. C-7 is incomplete: existing positions and reconciliation are missing.**
- **What the CRO requires:** sign-off C-7 (`…cro-signoff.md:364-366`) and the recheck §5.3 require two things:
  - "Record any existing position there, such as the 2 AVGO, with `ledger fill`, so the 2-slot count can see it";
  - "Reconcile monthly and after any withdrawal".
- **What the documents say:**
  - The release note has the first (line 114).
  - The README has neither.
  - Without it, `cmd_fill`'s 2-position check (`ledger_v66.py:149-151`) cannot see AVGO, so a 3rd concurrent position goes undetected.
- **Fix:** covered by the A-1 banner text (bullets 2 and 3).
- **Fix, README line 66 (replace):**
  `   - **金額(C-7):** `owner_settings.json` 嘅 `account_hkd` 填短線戶口**真正**嘅淨值(唔計借貸),每月同每次提款後再核對。戶口入面已有嘅持倉(例如 2 股 AVGO)要用 `ledger_v66.py fill open` 記錄,等「最多 2 倉」睇到佢(點樣填由 AI 話你知;會被標 S2,係預期)。`
- **Note to Tom:** `--engine` accepts only E1 and E2 (`ledger_v66.py:438`). A legacy position therefore gets a fabricated exit rule in ④ (`daily_scan_v66.py:272-291`). Decide how legacy positions are recorded.

**A-3 · MEDIUM · `strategy/v6.6/parity_check.py:15, :115` (with README `:58`). The V-3 tool output re-introduces F-2.**
- **What the tool prints:** after a pass, 「✅ V-3 過關 —— 可以將 config_v66.py 入面 GATES["V3_對照測試"] 改做 True」. The docstring at line 15 says the same.
- **Why it matters:** `config_v66.py` is fingerprinted, and `GATES` is no longer a literal there. The Owner would edit `DEFAULT_SETTINGS["gates"]` (line 56). Two things then go wrong:
  - **The fingerprint changes,** and README line 85 says 「先問清楚先好交易」.
  - **The gate stays false,** because `owner_settings.json` overrides the default (`config_v66.py:72-73`).
- So the README's own V-3 step contradicts the tool it runs. Fail-safe, but it teaches the Owner to distrust the fingerprint, which was the old F-2 failure. `parity_check.py` is not in `CORE_FILES`, so the fix does not move the fingerprint.
- **Fix, `parity_check.py:15` (replace):**
  `全部過關 → 喺 owner_settings.json 將 "V3_對照測試" 改做 true(唔好加引號),並將輸出畀 AI / CRO 睇。唔好改 config_v66.py(會改規則指紋)。`
- **Fix, `parity_check.py:115` (replace):**
  `print('\n✅ V-3 過關 —— 喺 owner_settings.json 將 "V3_對照測試" 改做 true(唔好加引號)。唔好改 config_v66.py。')`
- **If the code fix is deferred, append to README line 58:**
  「(如果 parity_check 嘅輸出叫你改 config_v66.py,唔好跟 —— 改 owner_settings.json。)」

### LOW

**X-2 · LOW · README `:79, :85`; release note `:6, :92-96`. The fingerprint and the V6.6.2 re-verification are author-asserted.**
- **The fingerprint:**
  - `0b05757d0076` appears only in these two documents and in the commit message (`COMMIT_EDITMSG:27`).
  - No tool output was committed. My 11-24 F-2 fix asked for `results/release_stamp.txt`.
  - If the value is wrong, the result is a false alarm (fail-safe). But the CRO's V6.6.2 check must repeat K-6.
- **Fix, run at be74475 and commit:** `strategy/v6.6/results/release_stamp.txt` with the output of `python -c "import config_v66 as C; print(C.VERSION, C.RELEASE_DATE, C.fingerprint())"`.
- **Fix, release note line 92 (replace):**
  "Re-run in the cloud by the CEO (author) on V6.6.2; the CRO's independent re-check is pending:"

**X-3 · LOW · README `:208`; release note `:51-52`. "穩陣" / "robust" overstates (residual of F-3).**
- E2's per-signal edge keeps its sign under ±20% perturbations. Its OOS 90% CI is [−0.02, +2.27] (`summary.csv:28`).
- **Fix, README line 208 (replace):**
  `- **引擎二每筆有細嘅優勢,對參數唔敏感:** 每個鎖死參數 ±20% 都仲係正數(每個訊號都做嘅量度);但 OOS 90% 區間 [−0.02%, +2.27%],統計上未同零分開。`
- **Fix, release note lines 51-52 (replace):**
  "Per signal, without slot limits, E2's edge is the one that survives ±20% parameter changes, although its OOS 90% CI [−0.02, +2.27] touches zero. E1 has none on its own (OOS −0.16%). Inside a 2-slot book it reverses, as the table shows."

**X-4 · LOW · README `:25-26`; release note `:19-21`. "One code base" is overstated (open from F-17).**
- **Fix, README lines 25-26 (replace):**
  `3. **同一套規則函數,所有工具共用。** 掃描器同 Telegram bot 直接用 `rules_v642.py` / `signals_v66.py`;回測(`lab.py`)有自己一份路徑判斷,用 `equivalence_check.py` 逐日核對一致(85,120 次,0 差異);記錄簿用 `lab.py` 計結果。Pine 係人手翻譯,要用 golden 檔對照。每次開機都會印出版本同「規則指紋」。`
- **Fix, release note lines 19-21 (replace):**
  "**One rules core.** The scanner and bot import `rules_v642.py` and `signals_v66.py`. The lab imports `rules_v642.py` and keeps its own path gate (`lab.build_signal`), held equal by `equivalence_check.py`: 85,120 day × ticker × path checks, 0 differences. The ledger resolves through `lab.simulate`."

**A-4 · LOW · `README.md:125`.** 「(唔算違規,但 review 會列出)」 is false. `review()` reads flags only for S1 and S2 (`ledger_v66.py:353-358`).
- **Fix (replace the parenthesis):** `(唔算違規;`review` 唔會列出,要睇就用 `python ledger_v66.py show`)`

**A-5 · LOW · `README.md:116`.** The code flags risk only above 1.05% (`ledger_v66.py:159`). The CRO sign-off discloses this as a 5% slippage tolerance.
- **Fix:** `- 每筆風險 > 1%(容許 5% 滑價:超過戶口 1.05% 先標)`

**A-6 · LOW · `README.md:56`.** Nothing tests `daily_strong_signals.py`'s flow. The fidelity of the shadow "scan" path rests on Tom's AST and line-by-line comparison (`…release-code-review.md` §3) and on two screenshot days.
- **Fix:** `- **佢唔測咩:** `daily_strong_signals.py` 個掃描流程本身 —— 冇自動測試覆蓋。V6.6 嘅「舊掃描器路徑」係 Tom 逐行對照你源碼重寫(AST 比對),加 9 月兩日截圖核對。`equivalence_check.py` 只證明 V6.6 掃描器 = V6.6 回測。`

**A-7 · LOW · `README.md:23`.** 「數值同截圖吻合到小數位」 has no committed source. I verified the no-breakout part from data (§2.1 #9).
- **Fix:** `(用 `data/` 嘅 Webull 數據重算:CVX、PFE 喺 9 月 4、25、28 日嘅最高價都低過 20 日高。截圖冇存入 repo,而且只係兩日樣本。)`

**A-8 · LOW · `README.md:194`.** The golden file has no `A股數` = 0 rows. No-signal rows are blank, and every signal row is affordable (Tom F-7).
- **Fix:** `- **冇訊號行:** `A股數` 欄空白嘅行(bucket「冇訊號」),Pine 嘅 `G_` 訊號數值應該係 0。有 `A股數`(≥1)嘅行全部買得起,Pine 應該出訊號;唔出就影相畀 AI。`

**A-9 · LOW · `README.md:4`.** The SPY statement is undated, and 「等都冇損失」 holds only while SPY stays below its 200-day line. On 11-18 SPY was above it by +0.02%.
- **Fix:** `> 截至 2026-11-23 收市(`data/SPY.csv`),SPY 722.29 低過 200 日線 730.47(11-19 起),系統本身都停手,而家等唔會錯過訊號。SPY 一返上 200 日線就會再出訊號 —— 到時一樣要等下面幾樣完成。`

**A-10 · LOW · `README.md:103, :148`. Standing CRO conditions are under-stated.**
- C-8's price ceiling (`…cro-signoff.md:367-369`) is missing.
- Under A, S2's 「返去 A」 is a no-op, and N-11 is pending with the Owner (release note 115-117).
- **Fix, line 103 (replace):** `- 聽日開市落,用**限價單**(CRO C-8):限價 × 股數 ≤ 戶口 10%(HK$10,000 即 US$128.21),而且(限價 − 系統止蝕)× 股數 ≤ 戶口 1%(US$12.82)。開市價高過限價 → 唔買,唔好加價、唔好加股。開市價偏離收市超過 1% → 重計 R值/風險,唔達標就放棄。`
- **Fix, line 148 (replace the row):** `| S2 | 上面任何一個記錄時違規 | 通知 CRO。而家係 A,「返去 A」冇作用;CRO 建議有 S2 就停開新倉,直至向 CRO 解釋清楚(N-11,等你決定) |`

**A-11 · LOW · `README.md:156-168`. The B′ list is shorter than the CRO's and the release note's, and the exact-match rule is not stated.**
- **Fix, insert after line 162:** `6. CRO 其他 B′ 條件(B-2 至 B-11):包括 Mo Peter 嘅 VaR、Mario 嘅壓力測試、現金戶口(B-8;如果仲喺 CL-8 模擬期,B′ 要先用模擬)。`
- **Fix, line 167 (replace):** `- `"b_prime_cro_note": "<CRO 喺 APPROVED_BPRIME_NOTES 加嗰一行,一字不差>"``

**A-12 · LOW · `README.md:38-68, :72, :106-111, :175`. Operational omissions (including the open items from F-23).**
- **Fix, line 72 (append to the heading):** `—— 轉用之後先照做;未轉用之前可以跑掃描(記錄簿會開始累積),但唔好按 ① 落真錢單`
- **Fix, insert after line 111:**
  `- 模擬交易唔好用 `fill` 記錄(`fills.csv` 只記真錢交易)。`
  `- 唔係成交當日記錄,要加 `--date YYYY-MM-DD`(紐約成交日)。`
- **Fix, line 60 (replace):** `   AI 會話你 `real_fee` 填咩數;你喺 `owner_settings.json` 填好,feecheck 過咗(淨 EV > 0)先將 `"V1_真實收費已核"` 改做 `true`:`
- **Fix, line 38 (append):** `以後更新 V6.6,**保留你自己嘅 `owner_settings.json`**(唔好畀新版覆蓋;覆蓋咗戶口金額會變返 HK$10,000)。`
- **Fix, line 52 (replace):** `   copy "<你 V6.4.2 資料夾>\dual_engine_v6_4.py" .` and add `(例如 `01_每日使用_最新V6.4.2\dual_engine_v6_4.py`;未有 `ta` 就先 `pip install ta`)`
- **Fix, line 175 (append):** `用 `notepad "%USERPROFILE%\.swing_bot_token"` 開(問開新檔揀「是」;存檔類型揀「所有檔案」,唔好變 .txt)。`

**B-1 · LOW · release note `:66`.** "Signed off with conditions C-1…C-7" omits C-8 to C-10 (standing) and B-1 to B-9.
- **Fix:** `| John (CRO) | Signed off with conditions: C-1…C-5 pre-switch, C-6…C-10 standing, B-1…B-9 before B′ | `reports/risk/2026-11-24-v66-release-cro-signoff.md` |`

**B-2 · LOW · release note `:84-86`.** B-4 is presented as fixed. The CRO's strengthened B-4 also requires that every signal and fill row record `account_hkd`, the live mode and the gate states (N-6). That is not in `SIGNAL_COLS` or `FILL_COLS` (`ledger_v66.py:41-47`).
- **Fix:** change "**B-4 (B′ only):**" to "**B-4 (B′ only, partial):**" and add the bullet "Still open (CRO N-6): every signal and fill row must record `account_hkd`, the live mode and the gate states."

**B-3 · LOW · release note `:7-8`.** "Right now" is undated.
- **Fix:** "As of the 23 Nov close (the latest bar in `data/SPY.csv`), the system would not trade anyway: SPY closed below its 200-day MA on 19, 20 and 23 Nov (722.29 vs 730.47 on 23 Nov). This changes as soon as SPY closes back above it."

---

## 4. Safety framing (task item 3)

| Question | Finding |
|---|---|
| Does anything tell the Owner to switch, or to trade real money, before the banner conditions close? | **No direct instruction.**<br>- README line 3: 「未可以轉用 … 唔好落真錢」. Release note line 3: "NOT yet cleared for use".<br>- Neither the release note's "next steps" (§4) nor any README section says to switch.<br>- Two indirect risks:<br>  - §二 is written in the imperative with no "after switching" qualifier (A-12).<br>  - **Banner item 4 can be closed on a weaker C-6 than the CRO's (A-1, HIGH).**<br>- The interim instruction "paper trade V6.4.2" was accepted by the CRO "only as paper; delete at the switch" (N-10). The banner deletion clause (line 16) satisfies that. |
| Does any failure message point the Owner to an uncontrolled path (L-008)? | **No.**<br>- `掃描_v66.bat:23-24, 30-31`: 「今日唔好交易 … 修好之前唔好用任何版本落單」; selftest lints the absence of "V6.4" (`selftest.py:204`).<br>- `daily_scan_v66.py:139, 145, 304` → SCANFAILED. Fingerprint mismatch (README 85) → 「先問清楚」.<br>- Parity failure (`parity_check.py:117`): 「唔好信 V6.6 … 畀 AI 睇」.<br>- Config errors fail closed with no fallback text.<br>- `daily_scan_v66.py:3` now reads 「唔好再用嚟揀股」 (CRO R-7 fixed).<br>- **One adjacent defect:** the parity *success* message routes the Owner to a fingerprinted file (A-3). It is not an uncontrolled path, but it is a control-defeating instruction of the same family. |
| Are estimates marked as estimates (rule 5)? | **Mostly yes.**<br>- N-9 is labelled "John's estimate … from hypothetical fees" (release note 57-58).<br>- "≈2.2%", "≈0.8%" and 「大約」 are used throughout; backtest figures are sourced to `summary.csv` and `baseline.json`.<br>- Exceptions:<br>  - The SPY state and 「等都冇損失」 are undated and unconditional (A-9, B-3).<br>  - 「吻合到小數位」 is unsourced (A-7).<br>  - The V6.6.2 re-verification is presented as fact but is author-run (X-2). |

---

## 5. Consistency (task item 4)

| Topic | README | Release note | Decision record (V6.6.1 state) | Status |
|---|---|---|---|---|
| Switch conditions | 4 banner items (V-1 and V-3 included) | "all §4 items" (8) | C-1…C-5, V-2, C-6/C-7; V-1 and V-3 "Before B′" | **Inconsistent** → X-1 |
| C-6 leverage | 「有欠款 → 唔准開新倉」 | Cash or margin disabled, no debit; account as read does not qualify | "No V6.6 entry … into a margin account that carries a debit" (11-24 wording) | **README weaker** → A-1. Record needs the 11-25 wording |
| C-7 existing positions | Absent | "Record any existing positions (e.g. AVGO)" | Absent | → A-2 |
| Fingerprint | `0b05757d0076` | `0b05757d0076` | `c3f24ad80b06` (V6.6.1) | Historical; append |
| Selftest | 82 | 82 | 65/65 | Historical; append |
| Audit status | Not mentioned | "README FAIL → rewritten in V6.6.1" | "README rewritten in V6.6.1" | → X-1 |
| CRO C-5 re-check | Banner item 3 ✓ | Row ✓ | C-5 "Open" | Append |
| CRO escalation count | — | "4th escalation" | "third escalation" | Append |
| B′ prerequisites | G1, V1 (+S4), V2, V3, CRO note in code | V-1…V-3, B-2…B-11, VaR, stress, CRO note in code | V-1, V-3, B-2…B-9, dated CRO note | README shortest → A-11. Record append |
| Performance figures | 2.2%, +US$116, 0.8%, −0.8%, −1.03%/+1.85% | Same, plus scanner E1/E2 | ≈2.2%, +US$116, ≈0.8%, −0.8% | **Consistent** |
| Review horizon | 30 E2 and 6 months; no cap comparison before 100 | Same | Same | **Consistent** |

---

## 6. What the decision record should say (append only; I have not edited it)

Text for 腦大裝草 to append to `memory/decisions/2026-11-24-swing-v66-release.md`:

```
## Update 2026-11-25 — CRO C-5 re-check, V6.6.2, docs re-audit (append-only)

- CRO C-5 re-check at 7f74e2c / c3f24ad80b06 (reports/risk/2026-11-25-v66-c5-recheck.md):
  PARTIAL. C-1, C-2, C-5 PASS; C-3 accepted (C-3r before first review); C-4 NOT closed
  (stale fill across bear days, F1). Pre-switch: C-4r, N-1 (hermetic selftest), N-5 (bot
  intraday). B′ OFF; B-4 failed ("false" strings). Risk 75 → 76 once verified. C-6 escalated
  a 4th time: the account as read on 13 Nov (INDIVIDUAL_MRGN, USD −12.06) does not qualify;
  no V6.6 entry until it is a cash account (or margin disabled) with no debit, shown by
  statement or read-only pull.
- V6.6.2 at be74475, rules fingerprint 0b05757d0076 (CEO run; CRO K-6 confirmation pending).
  Lands C-4r, N-1, N-5, C-3r, B-4 (N-7 part only; N-6 row recording still open), B-11
  (lab.py fingerprinted), N-10. Author-run: selftest 82/82 (also -O), equivalence 0/85,120,
  ledger_check PASS, baseline.json unchanged. CRO verification of V6.6.2: PENDING.
- Docs re-audit (Ai 管理層, reports/committee/2026-11-25-v66-2-docs-reaudit.md): all four
  11-24 HIGH findings closed. README PASS WITH CORRECTIONS (A-1 HIGH: C-6 understated;
  blocking banner removal), release note PASS WITH CORRECTIONS.
- Canonical switch conditions (supersede the open rows of the table above):
  (1) CRO verifies V6.6.2 at a stated fingerprint; (2) Owner PC: .bat double-click shows a
  completed scan, selftest 82/82 → V2; (3) parity_check passes → V3; (4) V-1 contract note
  → lab.py --mode feecheck, ALL and OOS net EV > 0 (else S4: no trading at any cap);
  (5) C-6 as above, C-7 account_hkd = real equity and existing positions (2 AVGO) recorded
  with ledger fill; (6) docs re-audit corrections landed.
  V-1 and V-3 are pre-switch by CEO choice, stricter than CRO sign-off §6.1 (B′ gates there).
- Interim: Owner continues V6.4.2 in paper only (CRO N-10: acceptable only as paper; the
  instruction is deleted at the switch).
- Owner decision pending: N-11 (under A, any S2 → no new entries until explained to the CRO).
- Dissent carried: CRO N-9 — net EV crosses zero at a fixed charge of about US$0.25–0.40 per
  side (estimate from hypothetical fees; Webull schedule NOT OBTAINED). Tom — 2-slot results
  are path-fragile (one-bar ADX slip: OOS CAGR +2.6% → −0.6%).
- Observation for the first forward review: in the 2-slot book E2 averages −1.03% (49) and
  E1 +1.85% (86) while E2 holds slot priority; test slot priority on forward data only.
```

---

## 7. Bias observations

1. **Paraphrase drift on constraints.** Each time a CRO condition was paraphrased into the Cantonese manual, a qualifying clause dropped out:
   - C-6 lost "cash or margin disabled, shown by evidence";
   - C-7 lost "existing positions" and "reconcile";
   - C-8 lost the price ceiling;
   - the B′ list lost B-2 to B-11.

   The English release note kept them. The Owner reads the README daily. The error runs one way: each omission makes trading look easier.
2. **The lean is smaller than on 11-24 and not uniform.**
   - The README now carries the as-traded E2 reversal, 「兩者都同零分唔開」, the CRO's PARTIAL and the "paper only" instruction.
   - It is **stricter** than the CRO on V-1 and V-3.
   - The 11-24 observation "dissent exists but does not reach the Owner" is largely resolved. N-9, Tom's fragility, the 4th C-6 escalation and N-11 all reach him through the release note.
3. **Self-verification.**
   - Every V6.6.2 number (82/82, 0/85,120, ledger_check, the fingerprint) comes from the author's run.
   - The release note marks the CRO row as `_pending_`, which is good, but labels its own run "Re-verified" (X-2).
   - Until the CRO's V6.6.2 check lands, this static audit and the CEO's run are the only reads of V6.6.2.
4. **Narrative lock-in on E2 priority.** The README now says plainly that inside the 2-slot book E2 loses (−1.03%, 49 trades) and E1 wins (+1.85%, 86 trades), yet the configuration gives E2 slot priority.
   - Changing it on this data would be in-sample selection, which is forbidden by the Owner's rule 5. So the priority is not a defect.
   - It should be an explicit question for the first forward review (§6, last line).
5. **Recency.**
   - "The system would not trade anyway" rests on 3 sessions below MA200.
   - On 11-18, SPY was above by +0.18 points (+0.02%; derived).
   - That makes it a reason not to rush, not a structural fact (A-9, B-3).

**Recurring patterns for 床狗 (prompt fixes):**
- **(a)** Owner-facing restatements of a CRO condition must quote the CRO's **latest** wording verbatim, with its source and date, and translate it in full; never summarise. (A-1, A-2, A-10, A-11)
- **(b)** When a control moves (here, gates moved from `config_v66.py` to `owner_settings.json`), grep **every printed string and docstring** in the package for the old location before release. (A-3)
- **(c)** Keep one canonical gating list, in the decision record. The README and release note reference it rather than restate it. (X-1)
- **(d)** A fingerprint or count quoted in a document must be pasted from committed tool output. This repeats the 11-24 F-19 pattern. (X-2)
- **(e)** "Re-verified" is reserved for independent runs. Use "re-run by the author" otherwise. (X-2)

---

## 8. Required fixes, in order

**Before the banner comes down (blocking; text only, plus two strings in a file outside the fingerprint):**
1. **A-1 (HIGH):** README banner item 4 and §一.6 must carry C-6 in the CRO's 11-25 wording. Alternatively, the CRO confirms in writing that the 11-24 interim option still stands, and the README quotes it.
2. **A-2:** C-7 existing positions and reconciliation.
3. **A-3:** fix `parity_check.py:15, 115`. Outside `CORE_FILES`, so the fingerprint is unchanged.
4. **X-1:** one switch list across the README, the release note and the decision record append; the release note audit row.

**With the same edit (LOW):** X-2 to X-4, A-4 to A-12, B-1 to B-3.

**Firm side:**
- the CRO's V6.6.2 re-check, including K-6 (the fingerprint);
- 腦大裝草 appends §6 to the decision record.

I will diff-check items 1–4 when they land. No full re-audit is needed unless the text changes beyond these fixes.

*Static audit only: I executed no code. Research and decision support; not financial advice. No agent of this firm places orders.*
