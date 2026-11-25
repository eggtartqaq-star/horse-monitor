# CRO verification of V6.6.5 (diff only)

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-25
**Scope:** `git diff c25f5ab 77c713e -- strategy/v6.6`, plus a check that the four named documents match my 25 Nov rulings.
- **Fingerprint:** `847d34621a5f`, recomputed in the repo and in a scratch copy (`git archive 77c713e`); it matches `results/release_stamp.txt` line 1.
- **Core files changed:** `config_v66` (version only), `ledger_v66` (N-24, N-25), and text lines in `daily_scan_v66` and `telegram_bot_v66` (N-26). Sizing, signals, rules, guardrails, indicators and lab are unchanged.

**Rules kept:**
- no tracked file modified;
- no broker call;
- no `pip install`;
- no token search;
- scratch copies removed.

**Concurrent commit:** while I was checking, the CEO landed **`16183fb`** (docs only; the fingerprint is still `847d34621a5f`). I re-checked the four documents at that commit. The doc results below are as of `16183fb`.

## Verdict

**V6.6.5: PASS.** No new code finding.
- **Code side of the switch: stays CLEAR.**
- **Risk score:** 76, unchanged; V-1 is still the ceiling.
- **B′:** OFF.

**Docs at `16183fb`: PASS, with one correction still open:**
- **D-1** remains in the decision record only; the checklist and the release note are fixed.
- **D-2** is fixed.

The switch itself still waits on the Owner items in `reports/risk/2026-11-25-v66-4-verification.md` §7. Those rulings are unchanged.

## Items

| Item | Result | Evidence (scratch copy, real CLI; NY date 2026-11-25) |
|---|---|---|
| **N-24** `--date` must be a real, non-future YYYY-MM-DD date | **PASS** | Refused: `2026/11/20`, `2026-02-30`, `2026-11-26`, `2099-01-01`, and a future date on `fill close`. |
| **N-24** `--legacy` requires `--date` | **PASS** | Refused when `--date` is missing. |
| **N-24** Wall-clock gate | **PASS** | **`switch_date` 2026-11-20 (already reached):** legacy refused at `--date` 11-12, 11-19 and 11-25, so a backdated recording is blocked.<br>**`switch_date` 2026-12-01 (future):** legacy accepted at 11-12, 11-19 and 11-25. |
| **N-24** Null `switch_date` | Open by design until the switch | Still allows `--legacy`, but no longer with future dates. The Owner must set `switch_date` on the day he starts (unchanged item). The structural refusal replaces the review flag I proposed, and is stronger than it. |
| **N-25** `s2-clear` note | **PASS** | For a fill dated 2026-11-24:<br>- refused: a note dated 11-23 (before the fill); `2099-99-99`; `2026-11-26` (future); a path without `.md`;<br>- accepted: a dated `reports/risk/….md`.<br>**Residual:** the check is still self-certified. `reports/risk/2026-11-01-old.md 2026-11-25` passes, because the rule uses the latest date in the note. My detective control stands: at every review I match each clearance to a real file dated on or after the fill. |
| **N-26** Floor text | **PASS** | On real bars to 2026-11-18:<br>- ① prints "開市價 ≤ 系統止蝕 → 唔買。萬一成交咗,即刻沽…S2 交 CRO" ("open ≤ system stop → don't buy; if filled, sell at once… send the S2 to the CRO");<br>- the bot plan prints "開市價 ≤ 止蝕 $26.77 → 唔買" ("open ≤ stop $26.77 → don't buy");<br>- README L127 says the same.<br>Text only is acceptable. Prevention cannot live in code (no broker access), and detection is structural: a fill below the stop is S2 and triggers the hold. |
| **N-28** Test-file hashes | **PASS** | `test_hashes()` equals stamp line 2 (`selftest.py=41e14cc0ae09 parity_check.py=7123f842f1fd pc_check.py=732817026a4d`). Converting `selftest.py` to CRLF leaves its hash unchanged (LF-normalised). `stamp()['match']` needs both lines when line 2 is present. |
| **X-1** Selftest vs Owner settings | **PASS** | **Owner variants:**<br>- `account_hkd` 4,497, 12,000, and gates + `switch_date` set → **117/117**, exit 0;<br>- a quoted `"true"` gate, an unlisted B′ note, or `switch_date` `2026/12/01` → that one check fails (116/117), **exit 1**.<br>**Mutation:** with the pin removed at 4,497 → **12 failures**, as the coordinator reported.<br>`owner_settings.json` is restored byte-identical after each run. |
| **CD-1 / CD-2** | **PASS** | **Harness** (versions faked as installed, dummy `dual_engine_v6_4.py`, `run()` stubbed), parity/scan return codes → `pc_check` exit:<br>- (0, 0) → 0;<br>- (1, 0) → 1;<br>- (0, 1) → 1.<br>"Not run" is `None` and does not fail.<br>**`.bat`:** the failure text now covers every version and keeps existing broker stops. |
| **Regression** | **PASS** | - selftest **117/117**, exit 0: normal, `-O` and `PYTHONOPTIMIZE=2` (scratch); normal and `-O` (repo).<br>- `equivalence_check`: 85,120 / 0.<br>- `ledger_check`: PASS.<br>- `lab.py --mode baseline`: `baseline.json` byte-identical, and every `results/` file identical. |

## Docs against my 25 Nov rulings

| Document | Result | Note |
|---|---|---|
| `電腦待辦清單.md` **A1** | **PASS** (D-1 fixed at `16183fb`) | Deadline (16:00 ET 3 Dec = HKT 05:00 Fri 4 Dec), cures, HK$100 by 30 Nov, G-2 with US$8,900 and LNW by 3 Dec, G-3.<br>L20 now reads "3 日收市前 USD 欠款仲未清 → 建議賣晒" ("USD debit still uncleared at the 3rd close → sell all"). |
| `電腦待辦清單.md` **B1** | **PASS** | (A) and (B) match: HK$12,500, `account_hkd` 10,000, `switch_date`, no other holdings, cash or margin-off, HK$4,497 not approved. |
| `電腦待辦清單.md` **D3** | **PASS** (D-2 fixed, L114) | `account_hkd` 10,000; NLV ≥ 10,000 monthly; below that, stop and de-risk; AVGO not recorded. |
| README banner item 4 | **PASS** | Matches §1.3–1.4 of my V6.6.4 report. |
| README step 6 | **PASS** (D-2 fixed, L85–86, L167–168) | A standing legacy breach is cleared by reducing first; legacy positions only from before the switch date. |
| `reports/quant/2026-11-25-v66-release.md` §1 | **PASS** (D-1 fixed at `16183fb`) | "If the **debit** is still uncured at the 3 Dec close, the CRO recommends selling". |
| `memory/decisions/2026-11-24-swing-v66-release.md`, last section | **Correct D-1** (forward entry; append-only) | "Cure the debit **and** turn margin off… If uncured, the CRO recommends selling". Everything else is accurate: C-8 amended, risk 76, N-27 and the fee dissent carried. |

**D-1 (MEDIUM; open in the decision record only; fix before Mon 30 Nov): the docs overstate the sell trigger.**
- **What my ruling says:** **only an uncured USD debit** triggers the recommendation to sell AVGO before 9 Dec. Turning margin off is required, but it is not a sell trigger.
- **If the debit is cleared but margin is still on,** the leverage breach is cured and G-2 can run. The account stays ineligible for V6.6 (C-6).
- **Why it matters:** as written, an Owner who deposits HK$100 on time, while Webull is still processing the margin change, would read the docs as telling him to sell AVGO.
- **Fix:** split the sentence: "USD 欠款 3 日收市前未還清 → 建議 9 日前賣晒;孖展未關 → V6.6 唔准用(C-6),但唔使因此賣" ("debit not cleared by the 3rd close → sell before the 9th; margin still on → no V6.6 (C-6), but no need to sell for that").
- **Where:** at `16183fb` the checklist (A1, L20) and the release note (§1) are fixed. **Still open:** the decision record, L165–166 ("Cure the debit **and** turn margin off… If uncured…"). Append a correction line; the record is append-only, so do not edit the original.

**D-2 (LOW; FIXED at `16183fb`): the legacy S2 text said it clears once "CRO writes a document and you s2-clear".**
- **What my ruling says:** a standing cap or risk breach is **not** cleared by a note. The position is first reduced within the limits, or closed, and only then do I write the note.
- **Also missing:** that `--legacy` must be recorded **before** `switch_date`, because the code refuses it afterwards.
- **Where:** checklist D3 and README step 6.

**Cosmetic:** README L126 still says "股數一定過" ("the share count always passes"). L127 now qualifies it, so I accept it as is.

## Open items (unchanged from my V6.6.4 report §7, except as noted)

**Owner:**
- G-1 by 16:00 ET 3 Dec;
- G-2 LNW by 3 Dec;
- C-6/C-7 choice (A) or (B);
- V-1;
- V-2: expect **117** and fingerprint **`847d34621a5f`**, with the stamp's test hashes;
- V-3;
- carry-overs.

**CEO:**
- D-1 (the decision record only) before 30 Nov;
- auditor diff-check;
- B-7.

*Research and decision support, not financial advice. No V6.6 code and no agent of this firm can place, modify or cancel an order.*

**For 腦大裝草 (append to `memory/decisions/2026-11-24-swing-v66-release.md`):**
`2026-11-25 · CRO V6.6.5 diff verification at 77c713e / 847d34621a5f: PASS. N-24 (real non-future dates; --legacy needs --date; wall-clock switch_date gate blocks backdating), N-25 (note needs reports/risk/*.md + real date in [open_date, today]; self-certified, CRO reconciliation stands), N-26 floor text in scanner ①/bot/README, N-28 test hashes = stamp line 2 (LF-normalised), X-1 (117/117 at 4,497/12,000; bad settings → exit 1; pin removed → 12 fails), CD-2 exit codes; selftest 117 (normal/-O/-OO), equivalence 85,120/0, ledger_check PASS, baseline identical. Code side CLEAR; risk 76; B′ OFF. Docs at 16183fb: PASS except D-1 MEDIUM, open in this decision record only (L165-166) — the sell trigger is the uncured USD debit only, not margin-off; checklist A1 and release note §1 already fixed; D-2 fixed.`
