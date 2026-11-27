# Layout (English): 先睇我 front page and checklist front block

*排版師 · 2026-11-27 · for 翻譯官, then Ai 管理層, then the CEO · standard: `templates/owner-brief.md`*

- **Part A** becomes `strategy/v6.6/先睇我.md`.
- **Part B** goes at the top of `strategy/v6.6/電腦待辦清單.md`, directly under its title line.
- Only the text between the BEGIN and END markers reaches the Owner. The notes at the end are for 翻譯官 and Ai 管理層.

---

## Part A: `strategy/v6.6/先睇我.md`

<!-- BEGIN PART A -->

# V6.6 is paper trading only, in your separate paper account; one number is due to the CRO by 3 Dec

**You do**
1. Send the AI your LNW (total liquid net worth: all your brokerage accounts added up, one number) for the CRO — by the 3 Dec close
2. Set up the PC, Telegram and TradingView, steps 1–5 below — no deadline (about 70 minutes)

**Deadline:** Thu 3 Dec, 16:00 New York close = Fri 4 Dec, 05:00 Hong Kong time. It is for keeping AVGO through its 9 Dec results; all the CRO's conditions are in the box below.

⚠️ No real-money V6.6 or V6.4.2 orders before the switch to real money (all five items in the README top box, then checklist G4); the CRO's account rule still applies before any real money (C-6, checklist D2).

Detail: `電腦待辦清單.md` (every step, in full) · `README.md` (how the system works)

---

## What do I set up, and in what order?

1. Put the `strategy/v6.6` folder from the ZIP at `桌面\v6.6`. Keep the old V6.4.2 files and, if you already have v6.6, your own `owner_settings.json` and `ledger` folder. In CMD: `pip install yfinance pandas numpy requests ta`. Copy `dual_engine_v6_4.py` in from your V6.4.2 folder; don't edit it. (C1–C3)
2. Double-click `電腦檢查_v66.bat` (it runs 3–8 minutes) and send the AI `pc_report_….txt`. If it differs from the table, change nothing and send it. Then double-click `掃描_v66.bat` once and send a photo of the window and `selftest_last.log`. When the AI says it passed, do C6. (C4–C6)
3. Telegram, as in E1: a new token from @BotFather (`/revoke`), saved outside the v6.6 folder and never sent to the AI; then your chat ID. In the v6.6 folder run `python notify_v66.py --test`; you should get 「✅ 測試訊息」. (E1, G1)
4. Double-click `schedule_v66.bat`. In Task Scheduler (工作排程器), on `SwingV66Morning`, tick 「喚醒電腦以執行此工作」 and 「錯過排程時間之後盡快執行」. (G2)
5. TradingView, as in E2: paste `pine/swing_v66.pine`, set 「短線資金(HKD)」, and compare with `pine/golden_v66.csv`. Then add one alert per chart, condition 「Any alert() function call」, notification to the phone app. (E2, G3)

| What | You should see | Source |
|---|---|---|
| PC report, parts 【5】 and 【2】 | 153 passed, 0 failed; fingerprint `2b7b62182068`, 「✅ 一致」 | checklist C4; `results/release_stamp.txt` |
| TradingView | title 「Swing V6.6.9 雙引擎」; 「短線資金(HKD)」 = 10000, the same as `account_hkd` | checklist E2, G3; `owner_settings.json` |

## Why 3 Dec, and what else does the CRO need for AVGO?

> **CRO text, in full (G-2; `reports/risk/2026-11-26-v66-8-verification.md` R-7):**
> **G-2. AVGO hold through the 9 Dec print.**
> - AVGO ≤ **6.6% of LNW** (1% ÷ 15% planning gap).
> - **老詹's close-basis stop** on file before 9 Dec.
> - A **retrospective decision record**, with your thesis in your own words.
> - **No adds.**
> - **LNW** (one number: the total of all brokerage accounts) **by the 3 Dec close.**
> - Without it, the CRO recommends **exiting AVGO before the 9 Dec print**. You place every order.

| At the 26 Nov last price of US$303.50 | LNW needed | Source |
|---|---|---|
| Keep 2 shares | ≥ about US$9,200 (≈ HK$71,800) | CRO R-7 |
| Keep 1 share | ≥ about US$4,600 | CRO R-7 |

## What do I do when the morning message comes (about 06:30 Hong Kong time, Tue–Sat)?

**Two-source rule (paper and real), CRO R-6: three lines, word for word. Limit, shares, stop and the other points are only in checklist G3; read all 9 before your first paper order.**
> - (point 2) Place an order only if the **same ticker and engine for the same bar date** appear on the Telegram ① list (taken from #1 down, within the free slots it states) **and** in a TradingView close alert.
> - (point 9) **Open check (C-8 (a), cancel at the open). The broker's order status is the authority;** the TradingView open alert is the reminder. In the first minutes after the open (21:30 HKT summer / 22:30 HKT winter): **not filled** → cancel; **filled at or below the system stop** → sell at once, record `fill open` and `fill close`, and send the S2 to the CRO.
> - (point 9) **If you cannot be at the screen at the open, do not place the order that day.**

## What must I not do?

- Rules that always apply, including the AAPL stop and how to record trades: checklist F.
- No-order days, the stop after a fill, and take-profit: checklist G3. Paper records and the switch-day steps: checklist G4.
- Dated limits on new positions from 4 Dec: checklist A2.

---

*Research and decision support, not investment advice. The AI places no orders; you place every order yourself.*

<!-- END PART A -->

---

## Part B: front block for `strategy/v6.6/電腦待辦清單.md`

*Insert directly under line 1 (the title), above 「由上而下做。」*

<!-- BEGIN PART B -->

> **Start here: `先睇我.md`.** One page: what to do, in what order, and the one deadline.
> **In this file:** A dated items · B questions for you · C PC install and updates · D account proof and real fees · E Telegram and TradingView · F rules that always apply · table after F: what to send the AI · G daily message (paper).
> **Deadline:** Thu 3 Dec, 16:00 New York close = Fri 4 Dec, 05:00 Hong Kong time: your LNW, one number, to the CRO. Full conditions: A1.
> The CRO texts below stay in full in their own sections; this block replaces none of them.

<!-- END PART B -->

---

## Notes for 翻譯官 and Ai 管理層 (not for the Owner)

1. **Copy, don't translate:** every 「…」 string and every Windows or TradingView label (they are what the Owner's screen shows), plus commands, paths, numbers and the fingerprint.
2. **CRO quotes:**
   - R-6 (Part A, morning section): use the Cantonese already in checklist G3, points 2 and 9, word for word.
   - G-2: translate R-7's English in full and label it 「CRO 原文翻譯」. Checklist A1 has a version mixed in with the thresholds, so don't reuse that as it stands.
3. **Terms:** "print" = 業績公佈; "close-basis stop" = 收市價止蝕; LNW = 流動資產淨值(LNW); paper account = 模擬盤; switch = 轉用 (glossary).
4. **Budget:** top block ≤ 12 lines; page about 40. If the Cantonese runs long, tell the CEO; never cut the G-2 box or the R-6 lines.

| Number on the page | Source |
|---|---|
| Thu 3 Dec 16:00 New York = Fri 4 Dec 05:00 HKT | `strategy/v6.6/電腦待辦清單.md` A1 |
| AVGO results 9 Dec; 6.6%; 1% ÷ 15% | `reports/risk/2026-11-26-v66-8-verification.md` R-7 (G-2 box) |
| US$303.50 (26 Nov); US$9,200 (≈ HK$71,800); US$4,600 | same file, R-7 thresholds; the checklist (A1) marks US$4,600 as an estimate |
| 153 passed, 0 failed | checklist C4; CRO V6.6.9 addendum §3.1 (153/153) |
| `2b7b62182068`; V6.6.9 | `strategy/v6.6/results/release_stamp.txt`; Pine title at `pine/swing_v66.pine` line 23 |
| 短線資金(HKD) 10000 | `strategy/v6.6/owner_settings.json` (`account_hkd`); Pine default at line 26; checklist E2 |
| 3–8 minutes | checklist C4 |
| about 70 minutes | sum of the checklist's estimates: C 30 + E 10 + 10 + G 20 |
| 06:30 HKT, Tue–Sat | checklist G2; `schedule_v66.bat` |
| 21:30 / 22:30 HKT | CRO R-6 point 9 |
| five items in the README top box | `strategy/v6.6/README.md` line 3 |
| from 4 Dec | checklist A2 |
