# CRO verification of V6.6.4, and rulings on G-1, G-2, C-6 and C-7 (Webull snapshot of 25 Nov)

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-25
**Scope (code):** `git diff 1a4df80 c25f5ab -- strategy/v6.6` only. **V6.6.4 at `c25f5ab`, fingerprint `0eb54f8e5872`**: recomputed in the repo and in a scratch copy; it matches `results/release_stamp.txt`.
- Concurrent commits up to HEAD `176b0c5` (`0318891`, `b602964`, `91ba609`, `176b0c5`) are research reports. Their only file under `strategy/v6.6` is `電腦待辦清單.md` ("PC to-do checklist"), which is not in `CORE_FILES`, so the fingerprint is unchanged.
- I did not review that checklist, apart from the lines that conflict with my C-7 ruling (§1.4).

**Uncommitted work seen at the end of this verification (not mine, not verified):**
- At 19:14 UTC another session modified `strategy/v6.6/pc_check.py`, `selftest.py` and `電腦檢查_v66.bat` in the working tree. HEAD is now `729d15f` (docs audit).
- **`pc_check.py`** now exits 1 when parity or the dry-run scan ran and failed (audit CD-2). This addresses the second half of my N-28.
- **`selftest.py`** gains 2 checks, so V-2 would expect **112**.
- **`.bat`:** the failure text changed.
- **Fingerprint:** none of the three files is in `CORE_FILES`, so it is still `0eb54f8e5872` in the working tree.
- **Before they are committed,** I re-verify the diff only.
- **Temp dirs:** two `mktemp`-style `/tmp/tmp.*` dirs appeared after my runs. They are not mine.

**Scope (rulings):** G-1, G-2, C-6 and C-7, on the facts in `reports/risk/2026-11-25-webull-readonly-snapshot.md` (CEO, read-only pull, 25 Nov 08:13 UTC).

**Method:**
- Scratch copies were made with `git archive c25f5ab`, `1a4df80` and `7f74e2c`, with `data/` symlinked in. Probes went through the real CLI and the real scanner path. Where I state a cause, it was checked in the code.
- No tracked file was modified, and no broker call of any kind was made.
- There was no `pip install`, and I made no attempt to find a Telegram token.
- The `/tmp` listing is identical before and after (no temp-dir leak), and the scratch copies were removed.

**Standard:**
- my V6.6.2 report (`2026-11-25-v66-2-fix-verification.md`, N-13 to N-19);
- my V6.6.3 report (`2026-11-25-v66-3-n12-verification.md`, N-20 to N-23);
- my 17 Nov ruling (`2026-11-17-mu-skhy-style-cro.md` §5, G-1 to G-3);
- my release sign-off (`2026-11-24-v66-release-cro-signoff.md`, C-6 to C-10).

---

## 0. Verdict

**V6.6.4: PASS, with one PARTIAL (N-15).**
- N-11, N-13, N-16, N-6, N-14, N-19, N-20, N-21, N-23, migration, `pc_check.py` and the regression suite all pass under probe.
- **N-15 is PARTIAL.** `max_limit` is correct, and every cap and risk S2 at the fill price is gone. But the instruction has no floor. A limit order also fills when the open gaps **below the system stop**:
  - K-14: 4 of 1,170 instructed entries;
  - K-7: 1 of 237 fills, and in the simulation that one uncleared S2 then halted every later entry (80 fills).
- **New findings:** N-24 to N-28 (§4). None of them gates the switch.

**The code side of the switch stays CLEAR.**
- N-26, the missing floor, is cured now by amending my standing condition C-8 (§5). The code text follows before the first forward review.

**The switch to live V6.6 is still NOT authorised.** On the 25 Nov facts:
- the only account the Owner has shown is a margin account with a debit (C-6 fails);
- its real equity is about HK$4,497, almost all of it in AVGO (C-7 fails).

**Rulings (§1):**
- **G-1:** NOT MET; the deadline stands, close of **Thu 3 Dec**.
- **G-2:** conditions unchanged. The threshold LNW drops to **≈ US$8,900** at the lower price, but LNW is still undisclosed, so the hold cannot be certified.
- **C-6:** NOT MET, sixth escalation.
- **C-7:** I agree with "dedicated cash account, or no live V6.6", with two corrections:
  - the minimum is **HK$12,500 of settled cash with `account_hkd` held at 10,000**, not HK$10,000;
  - "no live V6.6" means **shadow-only**, not off.

**Risk score: 76** for V6.6.4 at A as code (unchanged). Real-money use in the Webull account as read: **not deployable**. **B′ stays OFF.**

---

## 1. Rulings on the 25 Nov Webull snapshot

**Facts used** (snapshot §2–§4; I checked the arithmetic):
- Account …1311 `INDIVIDUAL_MRGN`. USD cash −12.06 and settled −12.06, the same as on 13 Nov. HKD cash 0.01. `interests_unpaid` 0.00.
- AVGO: 2 shares, cost US$353.16, last US$293.69 (most likely the 24 Nov close), market value US$587.38, −16.8% from cost.
- Net liquidation: HK$4,590.91 − 94.25 = **HK$4,496.66**, which is CEO arithmetic and an estimate. That is about US$576.49 at 7.8. AVGO is **≈ 102%** of it.

**AVGO tail, from `data/AVGO.csv`** (split-adjusted, last bar 2026-11-23, close 313.55):
- Worst close-to-close days in the past 12 months:
  - −12.59% on 2026-06-04 (that day's **open gap was −14.66%**);
  - **−12.19% on 2026-11-20**;
  - −11.43% on 2025-12-12;
  - **−10.43% on 2026-11-05**.
- That is four down days of 10% or more in a year, two of them this month.
- The −15% gap I used on 17 Nov is therefore still the right planning number. I am not loosening it.
- Whether 2025-12-12 and 2026-06-04 were post-results sessions is **not confirmed here**.

### 1.1 G-1: Webull USD debit and margin, deadline the close of Thu 3 Dec 2026

**Status: NOT MET.** The debit has been open since 13 Nov, 12 days. It is a `leverage: none` breach on its face. This is the **sixth escalation** to the CEO and the Owner.

**Ruling: the deadline is unchanged, 16:00 ET Thu 3 Dec.**
- Six US sessions remain, counting 25 Nov: 25 Nov, Fri 27 Nov (early close), 30 Nov, 1, 2 and 3 Dec. Thu 26 Nov is closed.
- **Cure (any one):**
  - **(a)** deposit HKD and convert at least US$12.06, plus any interest, so that USD cash is ≥ 0. This is about HK$94 at the API's implied rate, so deposit **≥ HK$100**. Start it **by Mon 30 Nov** to allow for transfer time.
  - **(b)** sell 1 AVGO. This clears the debit and leaves 1 share.
  - **(c)** sell both.
- **Plus, structurally:** disable margin or convert the account to cash.
- **What triggers the sell recommendation.** Only the debit does: if it is still uncured at the 3 Dec close, I recommend selling AVGO before the 9 Dec print. If the debit is cleared but margin is still enabled, the leverage breach is cured and G-2 can run. The account still fails C-6 (§1.3) and stays ineligible for V6.6.
- **Evidence:** a read-only pull or statement after the cure, showing USD cash ≥ 0 and the account class.
- **G-3 stands:** no new position of any kind in this account while it is a margin account with a debit.

### 1.2 G-2: holding AVGO through 9 Dec at the lower price

**Ruling: the conditions are unchanged, and none is evidenced yet.** The conditions are:
- AVGO ≤ **6.6% of LNW** through the 9 Dec print (1% ÷ 15% gap);
- 老詹's close-basis stop on file before 9 Dec;
- a retrospective decision record (there is none in `memory/decisions/`);
- no adds.

**What the lower price changes:**
- 2 shares at US$293.69 = US$587.38. That fits 6.6% for any LNW ≥ **US$8,900 (≈ HK$69,400)**. On 13 Nov the threshold was about US$10,450.
- 1 share fits for any LNW ≥ **US$4,450 (≈ HK$34,700)**.
- LNW is still undisclosed, 11 days after I asked for it.
- The Webull account alone is a lower bound, and against it AVGO is ≈ 102%. A −15% gap would cost US$88.11, which is **15.3% of that account** in one print, against a 1% per-trade budget.

**What the lower price does not change:**
- The −16.8% loss from cost is not a reason to hold, and not a reason to sell. The only question is whether the position fits the limits through the print.

**Binding text.** Through the 9 Dec close, the hold is acceptable only if all three of these are met:
- G-1 is cured;
- the Owner discloses an LNW (or the total of all brokerage accounts) above the threshold for the size he keeps;
- the stop and the decision record are on file.

**If LNW is not disclosed by the 3 Dec close,** I cannot certify the 6.6% condition. My recommendation is then the same as for an uncured debit: **exit AVGO before the 9 Dec print.**
- I place no order. The Owner decides.
- Reducing risk is never blacked out, including during 4–10 Dec.

**Owner's options**, cheapest first:
- **(1) Keep 2 shares:** deposit and convert, request margin off, give the LNW figure, get 老詹's stop, record the thesis.
- **(2) Sell 1 share:** this cures G-1 by itself, halves the event exposure, and needs LNW ≥ US$4,450.
- **(3) Sell both.**

### 1.3 C-6: the V6.6 swing account must be a cash account, or margin-disabled, with no debit

**Status: NOT MET.** The only account the API lists is a margin account with a debit. This is the **sixth escalation**.

**Ruling: unchanged, and stated without any interim route.**
- **What qualifies.** V6.6 live entries need a **cash account, or one with margin disabled**, with USD cash ≥ 0 and settled cash ≥ the order. Clearing the debit (G-1) alone does **not** satisfy C-6.
- **The 24 Nov "behavioural interim" no longer applies to V6.6.** That option was to clear the debit and fund in settled cash. My 25 Nov wording already superseded it.
- **Why.** V6.6 cannot see the account. A margin account silently funds any shortfall, and CLAUDE.md requires the control to be structural.
- **Evidence:** a statement or read-only pull showing the account class or margin status, the cash, and the settled cash.

### 1.4 C-7: real account base. The Owner's choice

The CEO's framing was "a dedicated swing cash account of ≥ HK$10,000, or no live V6.6".

**I agree in substance: there is no third option of running V6.6 live in the Webull account as it is.** I set the terms differently in two places.

**1. The minimum is HK$12,500 of settled cash, with `account_hkd` held at 10,000.**
- C-7 requires `account_hkd` ≤ real NLV at every monthly reconciliation.
- **Funded at exactly HK$10,000, the first realised loss puts the account in breach.** The only way back into compliance is to lower `account_hkd`, which moves the system off the only base anyone has reviewed.
- **The arithmetic:** HK$12,500 = 10,000 ÷ (1 − 0.20), using `portfolio.max_drawdown: 0.20` from `config/risk-limits.yaml`. With that funding, `account_hkd` = 10,000 stays ≤ NLV across the whole drawdown budget.
- **The floor:** if NLV falls below HK$10,000, that is a −20% drawdown, so a max-drawdown breach. New entries stop and a de-risk review follows. That is already the law.
- **Per-trade risk** is then 1% of HK$10,000 = 0.8% of the funded account, which is conservative.
- **Any other base,** whether above or below 10,000, needs Tom's re-run at that base and my review **before** the setting changes.

**2. "Dedicated" means no other holdings in that account. AVGO cannot be in it.**
- **The probe.** I recorded AVGO with `fill open --legacy` (2 shares @ 353.16, the Owner's stop 270):
  - at HK$4,497 it is flagged `S2:名義122.5%超上限;S2:風險>1%` ("notional 122.5% over cap; risk > 1%");
  - at HK$10,000 it is flagged at 55.1%;
  - either way, the next normal fill gets `S2:未解釋 S2 期間開新倉` ("new entry while an S2 is uncleared").
- **Consequence under N-11:** a legacy AVGO stops **all** new V6.6 entries until it is cleared.
- **I will not clear a standing cap breach as "explained".** It is cured by reducing the position, not by a note. AVGO also takes one of the two slots.

**3. "No live V6.6" should mean shadow-only.**
- The scanner keeps running every day and writing signals and heartbeats. Only fills stop.
- That builds the forward record the first review needs, with no capital at risk.

**4. Running at HK$4,497 is not approved, and will not be approved by editing a number.**
- **Method.** I ran `lab.simulate`, as traded, at HK$4,496.66 in a scratch copy. The lab has its own `Cfg.account_hkd` and does not read `owner_settings.json`.

| | HK$10,000 (reviewed) | HK$4,497 (real Webull NLV) |
|---|---|---|
| Trades, 2022-11-30 → 2026-11-23 (OOS) | 135 (66) | **102 (38)** |
| Tickers traded | 17 | **8** (PFE 33, INTC 23, BAC 22, PLTR 10, UBER 7, NKE 5) |
| Entries in common | 38 | 38 |
| Entries unique to this base | 99 | 66 |
| Per-trade EV, lab cost model, all (OOS) | +0.806% (+0.734%) | +2.204% (+3.041%) |
| Per-trade EV, **estimated** US$0.35 minimum + 10 bp per side, all (OOS) | **+0.088% (+0.008%)** | +0.556% (+1.469%) |
| Names affordable for 1 share at the 23 Nov close (`data/`) | 9 of 38 | 3 of 38 (BAC, NKE, PFE) |

- **It is a different system.** Only 38 entries are shared, and the book collapses into three cheap names.
- **Its higher EV** comes from 38 OOS trades selected by share price. I treat that as selection on a small sample, **not as evidence**, and it is not a reason to run small.
- **The fee row is my estimate,** within the N-9 range. It shows that the reviewed base is about **break-even OOS** at a realistic minimum ticket. **V-1, one real Webull contract note, is the economic gate.** If it confirms, it is S4: no trading at any cap.
- **CEO correction.** The snapshot and `電腦待辦清單.md` L33 say that at HK$4,497 the system "can buy almost nothing". Historically it trades about 76% as often, in a different, concentrated set of names. Please change the wording to "a different, untested system".

**The Owner's choice, as I would put it:**

> **(A)** Name a separate account, at Webull or another broker, that is a **cash account or has margin disabled**, holds **nothing but the swing sleeve**, and is funded with **≥ HK$12,500 of settled cash**. Set `account_hkd` to **10,000**, and set `switch_date` the day you start. **Or**
> **(B)** V6.6 runs **shadow-only**: scanner and signal ledger, no fills, until (A) is met.

**For the CEO:** `電腦待辦清單.md` lines 35 and 79–86 currently say:
- "≥ HK$10,000";
- "`account_hkd` = real NLV";
- record AVGO with `--legacy` and `s2-clear` it.

All three conflict with this ruling. Please correct them before the Owner acts on the checklist. I did not edit it, because it is a tracked file.

---

## 2. Item table: V6.6.4

| Item | Result | Evidence |
|---|---|---|
| **N-11 (a)** A fill during a hold is S2 | **PASS** | **CLI:** a PFE fill with no scan → S2. A BAC fill the next day → `S2:未解釋 S2 期間開新倉(2026-11-24_PFE(PFE))` ("new entry while an S2 is uncleared").<br>**`ledger_check`:** COST is flagged the same way.<br>**Legacy fills are exempt:** a KO legacy fill recorded during the AVGO hold was flagged only `legacy`. |
| **N-11 (b)** `s2-clear` validates the note | **PASS as specified** (see self-certification below, N-25) | **Refused:**<br>- `explained to John`;<br>- `reports/risk/ no date`;<br>- `2026-11-26 no path`;<br>- a second clear of the same fill;<br>- an unknown `fill_id`;<br>- a fill without S2 (selftest).<br>**Accepted:** `reports/risk/2099-99-99-fake.md 2099-99-99`, an impossible date and a file that does not exist.<br>**Record:** `s2_clearances.csv` is append-only and carries `cleared_at`, version and fingerprint. The S2 flag itself is never removed. |
| **N-11 (c)** `review` lists cleared S2s as notes and uncleared ones as breaches | **PASS** | - Cleared → `ℹ️ S2(已向 CRO 解釋):PFE …` ("explained to the CRO").<br>- Uncleared → `🔴 S2:BAC …`.<br>- Banner: `★ 有違規 → 停開新倉 … s2-clear` ("breach → no new entries"). Under A, the no-op "返去 A" ("go back to A") is gone.<br>- `show` prints the uncleared list. |
| **N-11 (d)** Scanner ① and bot hide sizes and limit prices; signals still logged | **PASS** | Real scanner path, real bars to 2026-11-18:<br>- **No hold:** `#1 引擎一 PFE … 股數 4($112) 限價上限 $28.17` ("4 shares, max limit $28.17"). The limit is the E1 R ≥ 2 bound, (30.99 + 2×26.77)/3 = 28.176, taken down to the cent.<br>- **Hold:** `⛔ … 停開新倉` and `#1 … 股數 —(停開新倉)` ("shares — (no new entries)"), with no limit shown.<br>- `signals.csv` gained 13 rows in both runs, with `size_A`.<br>- **Bot (PFE):** with no hold it shows the plan and the limit; under a hold it shows no plan and the hold message. Held-position rows are always hidden. |
| **N-11** Self-certification | **ACCEPTED, with a binding detective control** | See §3. |
| **N-13 (a)** Legacy fills count toward the 2 slots | **PASS** | AVGO legacy + KO legacy, then PFE → `S2:已有2倉(最多2)` ("already 2 positions, max 2"). |
| **N-13 (b)** Cap and risk still checked | **PASS** | AVGO 2 @ 353.16, stop 270 → `S2:名義55.1%超上限;S2:風險>1%;legacy` at HK$10,000 (122.5% at HK$4,497). A small legacy fill → `legacy` only. Section ④ shows "舊倉(唔屬於系統)" ("legacy position, not part of the system") with no system trailing stop (selftest). |
| **N-13 (c)** `switch_date` gate; null until the switch | **PASS as specified; residual N-24** | - `switch_date` "2026-11-20" + legacy at the default date (25 Nov) → refused.<br>- **`--date 2026-11-19` → accepted.** `logged_at` reads 2026-11-25 19:06, so backdating gets around the gate, and only `logged_at` shows it.<br>- **`null` + legacy dated 2027-03-01 → accepted** (a future date).<br>- `"20261120"` → `ConfigError` in selftest and ledger (fails loudly).<br>Null is acceptable until the switch, subject to N-24 and Owner item 3. |
| **N-13 (d)** Legacy exempt from the hold | **PASS, agreed** | Recording a position the Owner already holds is not opening a new one. The legacy row's **own** cap or risk S2 still triggers the hold for later entries, which is correct. |
| **N-15 (a)** `max_limit` | **PASS** | Binary search over cents.<br>- **Monotonic:** shares are non-increasing in price under both the cap and risk legs.<br>- **Bounds:** ≤ close +1%; E1 ≤ (target + 2×stop)/3.<br>- **Inputs:** the scanner passes real prices (`×f`) and the live mode.<br>- **Selftest:** grid of 24 combinations + an at-limit vs +1¢ fill. |
| **N-15 (b)** K-14 re-run with the limit | **PARTIAL** | Over the CSV history: 1,426 `bt` live signals (bull, A ≥ 1).<br>**Old instruction** (open within ±1%): 1,112 entries, **13 S2**. This reproduces my K-14 exactly.<br>**Limit** (open ≤ `max_limit`): 1,170 entries, **4 S2**, all with **open ≤ system stop**:<br>- NKE 2023-08-22: 90.15 vs stop 90.27;<br>- SHOP 2024-02-12: 77.80 vs 79.43;<br>- SHOP 2024-08-02: 48.59 vs 49.04;<br>- NFLX 2026-04-16: 96.37 vs 99.48.<br>Signal dates. Cap and risk S2s: **0**.<br>**With a floor** (open ≤ stop → skip): **0 S2**. The lab already rejects these (`if px <= stop`). → N-26 |
| **N-15 (c)** K-7 end-to-end with the limit | **PARTIAL → 0 with the floor** | Real scanner path (CSV bars injected), one scan per session, 2025-01-01 → 2026-11-23. **474 heartbeats.** The rank-1 signal is bought at the next open at the printed size and the 2-dp stop through `cmd_fill`.<br>**Limit only:** 296 candidates, 59 skipped (open > limit), 237 filled.<br>- **1 S2:** NFLX 2026-04-17, open 96.37 ≤ stop 99.48 → `股數1多過系統0股` ("1 share, system allows 0").<br>- Left uncleared, it flagged **all 80 later fills**.<br>- MU 2025-06-09, the old fill-price S2, no longer occurs.<br>**Limit + floor:** 236 filled, **0 S2, 0 holds.** |
| **N-16** source/asof; `fill` trusts only live yf heartbeats | **PASS** | **Hardlink probe** (live `runs.csv`/`signals.csv` hardlinked elsewhere, as-of CSV scan for 11-18 into the link):<br>- **V6.6.3:** a historical heartbeat `2026-11-18 True csv` lands in the live file, and PFE filled 11-19 is accepted **clean**.<br>- **V6.6.4:** the same row lands as `csv True`, but the fill gets `S2:…stale:上次掃描2026-11-17,之後漏咗1個交易日` ("stale: last scan 2026-11-17, 1 session missed").<br>`resolve`/`review` exclude `asof == "True"` (code, selftest). |
| **N-6** Settings on every row | **PASS** (B-4's N-6 part closed) | Signals, runs and fills carry `account_hkd`, `cap_mode` and `gates` (`10000.0`, `A`, `G1=1;V1=0;V2=0;V3=0`). Migrated old rows are blank, which is correct: unknown. |
| **N-14** `NYSE_ADHOC_CLOSURES` | **PASS** | - Heartbeat 2025-01-08 → INTC fill 2025-01-10 (6 @ 19.88, stop 18.42) → **no flags**. At V6.6.2 this was "stale 1".<br>- **Control:** heartbeat 01-07 → `stale…漏咗1個交易日` ("stale: 1 session missed").<br>- `data/SPY.csv`: 1,200 sessions, 2022-02-11 → 2026-11-23. The only calendar session missing is 2025-01-09, and no SPY session falls outside the calendar. |
| **N-19** Scanner uses the bot's unclosed-bar rule | **PASS** | Last bar 2026-11-23:<br>- **NY 08:00 (pre-market):** "最後一條 bar 係今日…未收市" ("last bar is today… not closed"); **no ledger file written**.<br>- **09:45:** clock rule; nothing written.<br>- **16:30:** `runs.csv` written.<br>- **V6.6.3 at 08:00:** wrote the pre-market heartbeat. |
| **N-20** No final newline | **PASS** | A current-format `fills.csv` whose AVGO row has no trailing newline, then `fill open PFE` → `open_fills` = [AVGO, PFE]. |
| **N-21** BOM-only or header-less file | **PASS** | BOM + CRLF only → `show` exit 0; `fill` exit 0 with a `.bak`. |
| **N-23** Message for a reordered header | **PASS** | "重新排列欄位" ("columns reordered"), no longer "加咗 []" ("added []"). |
| **Migration** of V6.6.3- and V6.6.1-format files | **PASS** | **V6.6.3 ledger** (30/8/19 columns) with an AVGO fill:<br>- V6.6.4 scan → exit OK;<br>- `fill` PFE (hold flag only), `show` 0, `review` 0;<br>- `s2-clear` on the old row OK; `fill close` OK;<br>- 35/12/22 columns, 3 backups, old rows kept.<br>**V6.6.1 ledger** (18-column fills, no `runs.csv`): same result, 2 backups. |
| **`pc_check.py`** No token, no settings edit, no broker | **PASS** | Run under an audit hook inherited by its subprocesses:<br>- **0 network events**;<br>- **no token file opened**;<br>- `owner_settings.json` opened read-only, sha256 unchanged;<br>- only non-temp write: `pc_report_*.txt` (gitignored, `.gitignore:8`);<br>- subprocesses: `selftest.py` and selftest's own `-O` case.<br>`parity_check.py` and the dry-run scan were skipped here (no `yfinance`/`ta`, no `dual_engine_v6_4.py`). By inspection they use market data only, with no token or broker code. |
| **`pc_check.py`** Runs selftest/parity/scan; report redacted | **PASS** (N-28 notes) | Report: fingerprint ✅ match, selftest ✅ 110, parity "未做" ("not run"), scan "未做".<br>Home path → `~`; token-like strings → `<TOKEN>` (selftest).<br>`.bat`: CRLF, no ASCII parentheses, `if errorlevel 1 goto FAILED`. |
| **`pc_check.py`** Outside `CORE_FILES` | **AGREED** | It changes no signal, size, stop or ledger row. `selftest.py` and `parity_check.py` are outside too. Putting it inside would force a fingerprint change and a V-2 re-run for every report-format edit. Condition: N-28. |
| **Regression** | **PASS** | - `selftest.py` **110/110**, exit 0: normal, `-O` and `PYTHONOPTIMIZE=2` (scratch); normal and `-O` (repo).<br>- `equivalence_check`: **85,120 / 0**.<br>- `ledger_check`: **PASS** (187 rows, idempotent; bt 38/38, scan 21/21, book 8/8 IDENTICAL).<br>- `lab.py --mode baseline` (scratch): `baseline.json` sha256 `081a485c231a…`, **byte-identical** (`git diff --no-index` exit 0). All 10 `results/` files identical. Repo `git diff --exit-code -- strategy/v6.6/results/baseline.json` → 0.<br>- The commit's 23 mutations were **not** repeated this round. |

## 3. Self-certification of S2 clearance: my ruling

**The weakness.** The Owner can type any note. The check is lexical: a date-like string plus `reports/risk/`. I proved that by clearing with a nonexistent file dated 2099-99-99.

**Ruling: acceptable without a B′-style structural step**, for three reasons:
1. **B′ widens risk; a clearance does not.** B′ moves risk beyond the reviewed configuration, which justifies a code change and a new fingerprint. An S2 clearance only lets A resume, and A is the reviewed baseline. The control can be lighter.
2. **A per-clearance code change would backfire.** Every S2 would change the fingerprint and force a V-2 re-run. Friction like that trains bypassing.
3. **There is an audit trail.** The clearance is append-only, the S2 flag is never deleted, and every note path can be checked against `reports/risk/` in the repo.

**Binding detective control:**
- At every forward review, I reconcile each `s2_clearances.csv` row against an existing `reports/risk/` file **dated on or after the fill**.
- A clearance with no matching CRO file is a **process breach**: it is escalated to the Owner, and the hold is treated as never lifted.
- N-25 tightens the lexical check.

## 4. New findings

**N-24 (LOW–MED; before the first forward review): `--legacy` is open-ended.**
- **What can happen:**
  - with `switch_date` null, any fill can be recorded as legacy;
  - with it set, a backdated `--date` passes the gate;
  - a **future** `open_date` is accepted.
- **Why it matters.** A legacy row escapes both the "no live signal" S2 and the N-11 hold. That is exactly the route by which a discretionary buy could be laundered. Cap and risk are still checked.
- **Fix:**
  - refuse `open_date > today`;
  - `review` lists every legacy row with `logged_at` and flags as S2 any legacy row logged on or after `switch_date`;
  - optionally, a normal `fill open` while `switch_date` is null prints "switch_date 未設" ("switch_date not set").
- **Owner side:** set `switch_date` on the day of the switch (§7 item 3).

**N-25 (LOW): the `s2-clear` note check is lexical.**
- It accepts an impossible date and a nonexistent file, and it does not require the note date to be ≥ the fill's `open_date`.
- `pc_report` shows only the count of clearances.
- **Fix:** parse a real date ≥ `open_date`, and list each clearance (fill_id and note) in `pc_report`.
- §3's reconciliation is the binding control meanwhile.

**N-26 (LOW–MED; cured now by the C-8 amendment in §5; code text before the first forward review): the limit instruction has no floor.**
- **The gap.** A limit order also fills when the open gaps through the system stop:
  - K-14: 4 of 1,170 (0.34%);
  - K-7: 1 of 237.
- **Why it matters.** The fill is S2 (system shares = 0). Under N-11, one uncleared case halts all entries; in K-7 that was 80 later fills.
- **Overstated text.** README L120 ("股數一定過", "the share count always passes") overstates the guarantee.
- **Fix:** the scanner, the bot and the README add "開市價 ≤ 系統止蝕 → 唔買;已成交就即刻沽,記錄 fill open + close,S2 交 CRO" ("open at or below the system stop → do not buy; if filled, sell at once, record the fill open and close, and send the S2 to the CRO").
- It is fail-visible either way, so it does not gate the switch.

**N-27 (LOW; Tom): live entries are now more conservative than the tested ones.**
- 88 of the 1,112 entries that the old ±1% instruction took (7.9%) are now skipped: their open is ≤ close +1% but above the limit.
- At the open, 83 of those 88 still size to ≥ 1 share, and `lab.simulate` (which re-sizes at the open) takes them.
- The direction is safe (fewer or smaller trades, never larger), but the live trade set drifts from the tested one.
- **Tom:** quantify it with a "skip if open > limit" lab mode, or the scanner prints a second limit for N−1 shares.

**N-28 (LOW): tie the `pc_check` evidence to the released test code.**
- The V-2 evidence now reaches me as `pc_check`'s own summary, and neither `pc_check.py` nor `selftest.py` is fingerprinted.
- **Fix:** the report prints sha256[:12] of `selftest.py`, `pc_check.py` and `parity_check.py`, and the release stamp lists them.
- Also, `pc_check` exits 0 (so the `.bat` says "完成", "done") when V-2 and the fingerprint pass even if parity or the dry-run scan fails. The report marks ❌, so this is visible when sent. Acceptable.

## 5. Code side of the switch, and the C-8 amendment

**Code side of the switch to A: stays CLEAR.** N-24 to N-28 do not gate it.

**C-8 amended, effective now** (binding on Zac and 死潘狗, and on any ticket for the Owner):
- Enter with a limit order at or below the printed **限價上限** ("maximum limit price").
- **If the open is at or below the system stop, do not buy.**
- If a fill happens anyway, sell at once, record `fill open` and `fill close`, and send me the S2.
- If the open is above the limit, skip. Never resize upward.

**Bundling.** If the CEO can land N-24 and N-26 (and N-25 and N-28 if convenient) as one V6.6.5 **before** the Owner's PC session, the Owner runs V-2 once. Otherwise V-2 on V6.6.4 now is fine, with one re-run after. In either case I re-verify the diff only.

## 6. Risk score and limits

| Item | Score | Basis |
|---|---|---|
| V6.6.4 at A, as code | **76** (unchanged) | - Process gaps closed: S2 hold, legacy, limit price, provenance, ad hoc closures, pre-market bar.<br>- The ceiling is unchanged: **V-1 is unverified**, and my estimate run puts OOS net EV at **+0.008%/trade** at a US$0.35 minimum, which is S4 territory. |
| Real-money V6.6 in the Webull account as read | **Not deployable** | C-6 (margin, debit) and C-7 (≈ HK$4,497; AVGO ≈ 102% of it). |
| AVGO hold through 9 Dec, as is | **25** | - Leverage breach uncured.<br>- No stop, no decision record, LNW unknown.<br>- ≈ 102% of the account.<br>- Binary print on 9 Dec, after two days of −10% or worse in November.<br>Re-scored on the cure. |
| B′ | **74 conditional; OFF** | B-4 is now complete (N-6 PASS). B-2, the mode/flag case in B-3, B-5 to B-9, and V-1 to V-3 are open. |

**Limits** (`config/risk-limits.yaml`, unchanged since 2026-07-17):

| Limit | Value | Current (25 Nov) | Status |
|---|---|---|---|
| Leverage | none | Webull USD −12.06, margin account | **FAIL on its face**, 6th escalation (G-1, C-6) |
| Single position | 10% at cost | AVGO ≈ 102% of the Webull account; % of LNW unknown | **UNVERIFIED** (LNW undisclosed); within the swing sleeve it would be a breach → C-7 "dedicated" |
| Stop required | true | AVGO has no stop | **FAIL** until 老詹's stop is filed (G-2) |
| Per-trade risk | 1% | V6.6: S2 at the fill; the limit makes cap and risk S2 structurally impossible except on a gap-down (N-26, C-8 amended) | PASS (code) |
| Max drawdown | 20% | Used to derive the HK$12,500 minimum (§1.4) | — |
| Cluster (AI) | 40% (CRO band 20%) | AVGO counts 100%; LNW unknown | UNVERIFIED |
| Firm book | — | `config/portfolio.yaml` still empty (`cash_balance: REPLACE WITH REAL DATA`) | **Escalated again.** I cannot certify "inside all limits". |

## 7. Owner's open items (in deadline order)

1. **G-1, by 16:00 ET Thu 3 Dec.**
   - Clear the USD debit: deposit ≥ HK$100 and convert, **or** sell 1 AVGO, **or** sell both. Start any deposit by Mon 30 Nov.
   - Request margin off or cash conversion.
   - Send a read-only pull or statement afterwards.
2. **G-2, before 9 Dec.**
   - One number: your LNW, or the total of all brokerage accounts. 2 shares need ≥ US$8,900; 1 share needs ≥ US$4,450.
   - 老詹's close-basis stop.
   - Your AVGO thesis in your own words, for 腦大裝草's record.
   - No adds.
   - If LNW is not disclosed or the debit is not cured, my recommendation is to **exit before the 9 Dec print.**
3. **C-6 / C-7 decision.**
   - **(A)** A dedicated cash (or margin-disabled) account with no other holdings, funded with **≥ HK$12,500** of settled cash, `account_hkd` **10,000**, and `switch_date` set on the day; **or**
   - **(B)** V6.6 runs shadow-only.
   - Not the Webull account as it is.
4. **V-1 (the economic gate):** one Webull contract note → `lab.py --mode feecheck`.
5. **V-2:**
   - Double-click `電腦檢查_v66.bat`.
   - Expect **110** and fingerprint **`0eb54f8e5872`**. If the uncommitted CD-2 work is committed first, expect **112**; V6.6.5 would change both numbers.
   - Send me the `pc_report`.
   - Set `"V2_代碼測試": true` (no quotes) only after I confirm.
6. **V-3:** copy `dual_engine_v6_4.py` in, `pip install ta` on **your** PC, and run `pc_check` again.
7. **Carry-overs:**
   - Telegram token revoke;
   - CRO 7.6 (orders from the 6/28 Sep scans?);
   - delete README L3's paper-trading line at the switch;
   - fill in `config/portfolio.yaml`.
8. **CEO:** correct `電腦待辦清單.md` lines 33, 35 and 79–86 to match §1.4. Commission N-24 to N-28. Firm side before B′: Mo Peter's VaR and Mario's stress (B-7).

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No V6.6 code and no agent of this firm can place, modify or cancel an order; every trade above is a recommendation for the Owner to execute himself.*

---

**For 腦大裝草 (`memory/decisions/2026-11-24-swing-v66-release.md`, V6.6.4 row):**
`2026-11-25 · CRO V6.6.4 verification at c25f5ab / 0eb54f8e5872: PASS, N-15 PARTIAL. N-11 hold (fill S2, s2-clear, review split, scanner/bot hide; self-certification accepted w/ CRO reconciliation each review), N-13 legacy (slots, cap/risk kept; switch_date null OK till switch → N-24 backdate/future-date gap), N-15 max_limit correct; K-14 13→4 S2, K-7 1 S2 (NFLX 2026-04-17), all gap-downs through stop → C-8 amended (open ≤ stop: don't buy) → 0. N-16 hardlink, N-6, N-14, N-19 pre-market, N-20/21/23, migration 6.6.1/6.6.3 PASS. pc_check: 0 network, no token, settings untouched; outside CORE_FILES agreed (N-28). selftest 110 (normal/-O/-OO), equivalence 85,120/0, ledger_check PASS, baseline byte-identical. Code side CLEAR. Rulings: G-1 NOT MET, deadline 3 Dec close stands; G-2 unchanged, threshold LNW US$8,900 (1 sh US$4,450), LNW undisclosed → exit before 9 Dec print if not certified; C-6 NOT MET (6th escalation; cash/margin-off only); C-7 dedicated cash account ≥ HK$12,500 settled with account_hkd 10,000, no AVGO in it, else shadow-only; HK$4,497 run = different system (102 trades, 38 in common). Risk 76 (code); not deployable in Webull; AVGO hold as-is 25; B′ OFF.`
