# CRO: V6.6.8 verification, and rulings on paper fills, the two-source order rule, and the Owner's margin decision

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-26 · **HEAD:** `2491629`
**Scope:** `git diff 4af390d 6fed2fd -- strategy/v6.6`. V6.6.8 is `6fed2fd`, fingerprint **`11b86e31c9cd`**.

**Owner inputs** (as relayed by the CEO, and recorded in `memory/decisions/2026-11-24-swing-v66-release.md`, evening update):
- the 26 Nov verbatim statement;
- the broker answers: withholding yes; cash interest at Futu yes, at Webull no; an attached stop on a DAY limit: no;
- AskUserQuestion: both channels; TradingView or Webull for the open, not Yahoo; C-6 kept for real money.

**Method:** scratch copy (`git archive 6fed2fd`). No broker call, no pip; only this file edited; scratch removed.

**Tags:**
- **[C]** a cited file;
- **[D]** my run;
- **[A]** my assumption.

## 0. Verdicts

**(1) V6.6.8: PARTIAL.** Everything the commit claims checks out, but there is one new gap.
- **N-31 (MEDIUM): the Telegram message has no unclosed-bar guard.**
  - Run during US hours, `notify_v66.py` sends a full ① list (sizes, limit prices, order rules) computed from an **unclosed bar**, with no warning. That bypasses the N-5/N-19 protection that the scanner and the bot both have.
  - The scheduled 06:30 HKT run is safe. But the setup tells the Owner to tick "run as soon as possible after a missed start", so a PC that wakes during the US session sends an intraday list.
  - **N-31 must be fixed before any Telegram message is used to place an order, paper included.**

**Code side of the real-money switch:** CLEAR, subject to N-31 (diff-only re-verification). Risk score 76; B′ OFF.

**Rulings:**
- **R-5:** paper fills go in the main ledger, with a binding switch-day procedure.
- **R-6:** the two-source rule is **approved with amendments**: Telegram is the authority and TradingView a cross-check; stop and shares come from Telegram only; the broker order status decides the open check.
- **R-7:** the Owner's margin waiver is recorded as an Owner override, with my dissent. `leverage: none` and G-3 still bind. G-2 is unchanged; LNW is due by the 3 Dec close.

## 1. V6.6.8 verification

| Check | Result [D] |
|---|---|
| Fingerprint / stamp | `11b86e31c9cd`; `pc_check.stamp()["match"]` True; `selftest.py` hash `64d8ce7dd696`. `notify_v66.py` is in `CORE_FILES`. |
| selftest | **147/147**, normal and `-O`. |
| equivalence / ledger_check | 85,120 / 0; PASS. |
| `lab.py --mode baseline` | Every `results/` file is byte-identical to HEAD. |
| `ORDER_RULES` | The four lines are **identical** to the V6.6.7 text, now shared by scanner ① and the Telegram message. |
| Bear-day ④ | **PASS, and it closes a C-9 gap.** Before this, bear days printed no stops for open positions. Probe (bear 2026-11-23, PFE E1 open): the message shows "熊市…持倉照管" ("bear market… positions still managed"), the ④ line with stop and day count (3/10), and the ⛔ hold line. |
| Telegram safety | - No broker code. Network use is only `api.telegram.org/sendMessage` through `requests`.<br>- Token via `telegram_bot_v66.load_token()` (outside the folder, or an env var).<br>- Sends only to allow-listed chat IDs; errors are redacted.<br>- Under a hold, sizes are hidden (`_size_txt(hide=True)`), and ① is suppressed when slots are full. |
| `.bat` files | CRLF, UTF-8. `notify_v66.bat` runs selftest first and sends the "唔好交易" ("don't trade") alert on failure. The schedule is Tue–Sat 06:30 HKT, after the US close in both DST regimes. |
| Pine | `f_limit` is the closed form of `max_limit`: min(cap/N, stop + risk/N, close × 1.01), E1 R ≥ 2, cent floor. By inspection only; Pine cannot be compiled here. |
| **N-31** | **FAIL.** Probe: real bars to 2026-11-18, clock NY 11:00 (HK 00:00).<br>- The ledger is correctly **not** written.<br>- But `compose_morning` prints sizes, "限價上限 $…" and the order rules, with **no "未收市" ("bar not closed") warning**.<br>- At NY 17:30 the same message is correct.<br>**Fix:** `scan()` returns `partial`. When it is True, `compose_morning` replaces ① with "❌ 未收市 —— 收市後再查" ("❌ bar not closed — check after the close"), with no sizes, limits or rules, as the bot does. Add a selftest case. |

**Interim, until N-31 lands:** act only on a message whose header date is the **last completed US session**, received **after 05:00 HKT (winter) / 04:00 HKT (summer)**.

## 2. Rulings

### R-5 (i): paper fills

**Ruling: record paper fills in the main `ledger/`, with `switch_date` null, so that every fill before the switch date is a paper fill.**
- **Why not a separate ledger:** the controls work only in the main ledger. Fill provenance (heartbeats and signals), the N-11 hold, the 2-slot count, and the ④ stops in the scanner and in Telegram all read `ledger/`.
- **What a separate ledger would do:** it has no heartbeats, so every paper fill there would be flagged S2 "none", and Telegram would show no paper positions.
- **S2, the N-11 hold, `s2-clear`, C-9 (stops) and C-10 (monthly breaker)** apply in full to paper as the discipline rehearsal. I clear paper S2s with a periodic dated note in `reports/risk/`.

**C-7 (B) wording, amended:**
> **(B)** No real-money V6.6 orders. The scanner and the signal ledger run every day. Fills in the **paper account** may be recorded with `ledger fill` (paper only) until (A) is met and the switch is made.

**Binding conditions for the Owner:**
1. **Record each paper fill the same day,** at the paper account's **actual** fill price and date. Never adjust it to "what the market did".
2. **Paper results are not V-1 evidence.** Paper fees and fills are not real. The economic gate is still a real contract note (`--tif open`, per the Owner's "no attached stop" answer). Paper fills evidence **discipline**: S2 rate, stops placed, open checks done.
3. **Switch-day procedure, before the first real-money order:**
   - (a) close every paper position in the paper account **and** in the ledger (`fill close`);
   - (b) copy the whole `ledger/` folder to `ledger_paper_YYYY-MM-DD/` (the paper record for the forward review);
   - (c) **move** `fills.csv` and `s2_clearances.csv` out of `ledger/` into that archive; `signals.csv` and `runs.csv` stay;
   - (d) set `switch_date` that day;
   - (e) never record a paper position with `--legacy`.

   A real account must never share `fills.csv` with paper fills: open paper positions would take real slots.

### R-6 (ii): place only orders that are on both the Telegram ① list and a TradingView close alert

**Ruling: APPROVED, with amendments.** The text the Owner acts on:

> **Two-source rule (paper and real).**
> 1. **Telegram ① (Python, fingerprinted, CRO-verified) is the authority.** TradingView (Pine, a manual translation) is a cross-check only. **TradingView alone never authorises an order.**
> 2. Place an order only if the **same ticker and engine for the same bar date** appear on the Telegram ① list (taken from #1 down, within the free slots it states) **and** in a TradingView close alert.
> 3. **Limit:** the **lower** of the two 限價上限 (maximum limit prices).
> 4. **Shares:** Telegram's number. If TradingView shows fewer, use the fewer. **Never more than Telegram.**
> 5. **Stop:** **Telegram's system stop, exactly.** Never TradingView's. A higher stop is an S2 (自訂收緊, "self-tightened").
> 6. **If they disagree** (signal, engine, or a TradingView limit of "—"), do not place that ticker that day. Send both messages to the AI. **No late entry on a later day.**
> 7. **No orders at all that day if:**
>    - Telegram shows ⛔ (uncleared S2) or "倉位已滿" ("slots full");
>    - the selftest or scan alert arrives;
>    - no message arrives;
>    - the header date is not the last completed US session (N-31 interim).
> 8. **Pine settings must match.** Account, cap and risk must equal `owner_settings.json`, and the Pine title must read V6.6.8.
> 9. **Open check (C-8 (a), cancel at the open). The broker's order status is the authority;** the TradingView open alert is the reminder. In the first minutes after the open (21:30 HKT summer / 22:30 HKT winter):
>    - **not filled** → cancel;
>    - **filled at or below the system stop** → sell at once, record `fill open` and `fill close`, and send the S2 to the CRO.
>    - TradingView's real-time US feed may be a single venue, so its "open" can differ by a few cents from the official open. Go by the order status, not the alert price.
>    - **If you cannot be at the screen at the open, do not place the order that day.** If the broker offers an "at the open" time-in-force that cancels automatically, tell the AI.

**Note:** if TradingView alerts cover fewer than all 38 names (plan alert limits; not verified), signals in uncovered names are skipped. That fails safe, but the paper trade set will be smaller than the shadow ledger's.

### R-7 (iii): the Owner's margin decision on the real Webull account

**What I record against G-1:**
- **Debit cure: MET** (26 Nov read-only re-pull, USD +0.66) [C].
- **Structural part** (margin off or a cash account): **WAIVED BY THE OWNER**, 26 Nov, verbatim: "Well margin is allowed I bear the risk of this while paper trading."
  - The Owner is final authority (CLAUDE.md rule 2).
  - **My dissent is recorded:** a margin-enabled account is a behavioural control. Any fee, FX charge or purchase above cash silently borrows.

**What still binds:**
- **`leverage: none` is unchanged.** The Owner has not amended `config/risk-limits.yaml`. Therefore:
  > **Any negative cash balance, in any currency, in that account is a breach on its face.** It is escalated at once and must be cured within **3 sessions**.
  > **G-3 stands:** no new position in that account while any debit exists.
- **Recommendation (not a condition):** keep USD cash at **≥ US$10**. +0.66 is one fee away from a new debit.
- **C-6 for real-money V6.6** is unchanged, and the Owner confirmed it ("Yes"). The waiver covers the existing Webull account, not the future swing account.

**G-2, unchanged and quoted in full.** The 4–10 Dec macro blackout (E-1) also bars adds.

> **G-2. AVGO hold through the 9 Dec print.**
> - AVGO ≤ **6.6% of LNW** (1% ÷ 15% planning gap).
> - **老詹's close-basis stop** on file before 9 Dec.
> - A **retrospective decision record**, with your thesis in your own words.
> - **No adds.**
> - **LNW** (one number: the total of all brokerage accounts) **by the 3 Dec close.**
> - Without it, the CRO recommends **exiting AVGO before the 9 Dec print**. You place every order.

**Thresholds** at the 26 Nov last price of US$303.50 [C: addendum]:
- 2 shares = US$607.00, which fits 6.6% for LNW ≥ **US$9,200 (≈ HK$71,800)** [D];
- 1 share fits for LNW ≥ **US$4,600**.

## 3. Open items

**Owner:**
- **LNW by the 3 Dec close** (G-2);
- 老詹's stop and the AVGO decision record;
- keep Webull cash ≥ 0 (R-7);
- paper rehearsal per R-5 and R-6;
- for real money:
  - V-1 contract note, run with `--tif open`;
  - C-6;
  - C-7 (A);
  - V-2 (147 / `11b86e31c9cd`, or whatever the version after N-31 shows);
  - V-3.

**CEO:**
- N-31 (diff-only re-verification);
- carry R-5 to R-7 verbatim into the README (§6.5), checklist G3, and the decision record.

*Research and decision support, not financial advice. No V6.6 code and no agent of this firm places orders; the Owner places every order, paper included.*

**For 腦大裝草:** `2026-11-26 · CRO V6.6.8 at 6fed2fd / 11b86e31c9cd: PARTIAL. selftest 147 (normal/-O), equivalence 0/85,120, ledger_check PASS, results identical, ORDER_RULES text identical, bear-day ④ fixed, notify no broker / token via load_token / allow-list. N-31 MEDIUM: notify sends a full ① list from an unclosed bar (NY 11:00 probe) — fix before any Telegram-based order; interim: act only on post-close messages with last-session date. R-5 paper fills in main ledger (switch_date null), S2/N-11 apply; switch-day archive procedure; paper ≠ V-1 evidence. R-6 two-source rule approved with amendments (Telegram authority; Telegram stop and shares; lower limit; broker order status decides the open check; no late entries). R-7 G-1 debit MET; structural part WAIVED BY OWNER (dissent logged); leverage:none and G-3 still bind (any debit = breach, cure in 3 sessions); C-6 kept for real money; G-2 unchanged, LNW by 3 Dec close (2 sh ≥ US$9,200).`
