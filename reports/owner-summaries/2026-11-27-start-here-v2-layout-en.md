# Layout (English) v2: 先睇我 as a one-page A4 PDF

排版師, 2026-11-27. Replaces the layout the Owner rejected ("so unclear to read"). Order: 翻譯官 translates, Ai 管理層 checks the CRO lines, the CEO renders the PDF.

## How to read this file

- Each printed line has an ID (L01 to L48). IDs are never printed.
- Anything in square brackets [ ] is a design instruction. It is never printed.
- Text inside << >> is printed in a grey command box, exactly as written, in ASCII.
- Text inside 「 」 is what the Owner's screen shows. Copy it exactly. Do not translate it.
- Everything else on a line is printed, after translation.
- The Owner sees no IDs, codes, file paths, Markdown symbols, arrows, "=" or "≥" signs, and no English in brackets.

## Page spec

- A4 portrait, one page, one column. Margins: 10 mm top and bottom, 12 mm left and right. Content width: 186 mm.
- Chinese font: Noto Sans TC or 思源黑體. Body text 13 pt, line spacing exactly 16 pt.
- Commands: a monospace font (Consolas or Noto Sans Mono), 11 pt, black on light grey #EEEEEE, 0.5 pt #BDBDBD border, 2 mm rounded corners, padding 1 mm by 3 mm.
- Block colours: Block 1 red #C62828. Block 2 slate #37474F. Block 3 dark grey #424242.
- Spacing: 2 mm under each banner, 3.5 mm between blocks, 1.2 mm between steps, 1.5 mm between groups.
- None of these: page header, page number, table grid, emoji, arrows, file paths.

---

## Block 1: Do now: AVGO

Visual:
- Red banner across the full width, about 15 mm high. L01 sits on the left. L02 and L03 sit on the right, stacked and right-aligned.
- L04 sits under the banner in bold black.
- Then a red box: 1.5 pt #C62828 border, fill #FDECEA, padding 3 mm.
  - L05 is the box label. It sits on the top border, in 11 pt bold red, on a white patch.
  - L06 to L11 each get a red filled circle with a white number, 1 to 5, in a 7 mm left gutter. L07 has no circle and lines up under the text of L06.
  - L12 gets a grey tick icon instead of a number, and its text is 12 pt dark grey.
  - Then a thin red divider, 0.5 pt.
  - L13 in bold dark red #B71C1C. L14 in bold black.
- Under the box, a row of three tiles, each 60 mm wide with 3 mm gaps, about 14 mm high: the "big numbers".
  - Tiles 1 and 2: fill #F5F5F5. The label is 11 pt dark grey on top, the number is 18 pt bold black below it.
  - Tile 3: no fill and a 1 pt grey rule on its left. Two lines in 11 pt grey.

Lines:
- L01 [banner, left, 20 pt bold white] Do now: AVGO
- L02 [banner, right, top, 13 pt bold white] Deadline: Thu 3 Dec, 4pm US market close
- L03 [banner, right, bottom, 13 pt bold white] That is Fri 4 Dec, 5am Hong Kong time
- L04 [bold] To keep AVGO through its results on 9 Dec, you need all of these.
- L05 [box label] All of the CRO's conditions
- L06 [circle 1] By the 3 Dec close, tell the AI one number:
- L07 [no circle] your liquid net worth, which is all your brokerage accounts added up.
- L08 [circle 2] AVGO must be no more than 6.6% of that number.
- L09 [circle 3] Before 9 Dec, write down in your own words why you bought AVGO.
- L10 [circle 4] Before 9 Dec, agree to follow 老詹's closing-price stop.
- L11 [circle 5] Don't buy more AVGO.
- L12 [grey tick, grey text] Already done: your Webull debt is repaid, checked 26 Nov. Don't let it come back.
- [red divider]
- L13 [bold dark red] Miss any one, and the CRO recommends selling all your AVGO before its 9 Dec results.
- L14 [bold] You place every order yourself.
- L15 [tile 1, label] Keep 2 shares: your number must be at least
- L16 [tile 1, big number] about US$9,200
- L17 [tile 2, label] Keep 1 share: your number must be at least
- L18 [tile 2, big number] about US$4,600
- L19 [tile 3, line 1] Worked out at the 26 Nov price, US$303.50.
- L20 [tile 3, line 2] Both are estimates.

---

## Block 2: When you have time: set up the computer

Visual:
- Slate banner across the full width, one row, about 9 mm high. L21 on the left, L22 on the right.
- Five steps. Each gets a slate circled number, 1 to 5, in a 7 mm left gutter. Sub-lines have no number and line up with the step text.
- File names the Owner double-clicks are printed in bold, in the body font, with no quote marks.
- The two grey command boxes sit inline, after their lead words.
- L26 gets a small green tick icon, and L26 and the end of L29 are in 12 pt dark grey.

Lines:
- L21 [banner, left, 15 pt bold white] When you have time: set up the computer
- L22 [banner, right, 11.5 pt white] About 70 minutes. No deadline. Every step in full: 電腦待辦清單.
- L23 [step 1] Unzip to your Desktop, then copy in the old engine file from your V6.4.2 folder.
- L24 [sub-line] Then, in CMD, type: <<pip install yfinance pandas numpy requests ta>>
- L25 [step 2] Double-click [bold]電腦檢查_v66.bat, then send the AI its report.
- L26 [sub-line, tick, grey] You should see: 153 passed, 0 failed, and 「一致」.
- L27 [sub-line] Then double-click [bold]掃描_v66.bat once. Send the AI a photo and the log.
- L28 [step 3] Telegram: the old token leaked. Make a new one, and never send it to the AI.
- L29 [sub-line] In the v6.6 folder, type: <<python notify_v66.py --test>> [12 pt grey] You should get a test message.
- L30 [step 4] Double-click [bold]schedule_v66.bat. Messages then come Tue to Sat, 6:30am.
- L31 [step 5] TradingView: paste in the indicator. One alert per chart, on the daily chart.

---

## Block 3: Remember

Visual:
- Dark grey banner across the full width, one row, about 9 mm high. L32 on the left, L33 on the right.
- Group A (L34 to L36): a 3 pt amber bar #F9A825 down the left side, with the text indented 4 mm.
- L37 in normal 13 pt. L38 in bold.
- Then a light grey panel (#F5F5F5, no border, padding 2 mm). L39 is its label, top-left, in 11 pt bold grey. L40 to L47 sit inside the panel.
  - L40 and L41 are one item: no gap between them.
  - L44 to L46 are indented 4 mm under L43. Only their lead words are bold: "Not filled", "Filled at or below the stop" and "Filled above the stop".
  - L47 in bold.
- No bullets and no numbers in this panel, so it can't be confused with the checklist's numbered rules.

Lines:
- L32 [banner, left, 15 pt bold white] Remember: paper trading only
- L33 [banner, right, 12 pt bold white] No real-money orders, for V6.6 or the old V6.4.2.
- L34 [group A] Your real Webull account: cash must never go below zero, in any currency.
- L35 [group A] If it does, it's a breach: tell the AI at once, and repay within 3 trading days.
- L36 [group A] Until it is repaid, no new positions in that account.
- L37 Also still in force: stops on stocks you hold, and dates with no buying from 4 Dec. Both are in the checklist.
- L38 [bold] Before your first paper order, read all 9 rules in the checklist's 「每日訊息」 part.
- L39 [panel label] The key ones:
- L40 Buy only if a stock is on the Telegram list and also has a TradingView close alert,
- L41 with the same stock, the same engine and the same closing day.
- L42 US open, Hong Kong time: 9:30pm in US summer time, 10:30pm otherwise.
- L43 At the open, your broker's order status decides. The stop is always Telegram's.
- L44 [indent, bold lead] Not filled: cancel the order.
- L45 [indent, bold lead] Filled at or below the stop: sell at once, record both trades, tell the AI.
- L46 [indent, bold lead] Filled above the stop: place a stop order yourself at once, at that stop price.
- L47 [bold] Can't watch the open? Then don't place the order that day.

---

## Footer

- Visual: 8.5 pt grey, centred, in the bottom margin, 6 mm from the page edge.
- L48 27 Nov 2026. Research and decision support, not investment advice. The AI places no orders. Everything in full: 電腦待辦清單.

---

## Notes for 翻譯官 (never printed)

1. The Owner's 27 Nov rules override the glossary in three places:
   - Add no English in brackets, not even on first use. Write 流動資產淨值 without "(LNW)".
   - Put no source path on the page.
   - L05 is 「CRO 嘅全部條件」, not 「CRO 原文翻譯」. The lines are complete plain-word versions of the CRO's conditions, not a word-for-word translation. Ai 管理層 checks them against the sources.
2. Copy exactly, untranslated: file names, both commands, 「一致」, 「每日訊息」, Telegram, TradingView, AVGO, CMD, token, V6.6, V6.4.2, v6.6, 老詹, every number, 電腦待辦清單.
3. Terms:
   - closing-price stop = 收市價止蝕
   - liquid net worth = 流動資產淨值
   - breach = 違規
   - no new positions = 唔准開新倉
   - paper order = 模擬盤單
   - close alert = 收市提示
   - order status = 張單狀態
   - results = 業績
   - trading days = 交易日
   - For L11 use the strong form, e.g. 「唔准再買 AVGO」.
   - Dates: 12月3日(星期四). Times: 朝早5點, 晚上9:30.
4. Length: aim for about 25 characters a line or fewer.
   - At the limit already: L28, L35, L37, L38, L42, L43.
   - If any line runs past about 27, tell the CEO.
   - Never drop words from L06 to L14, L34 to L36, or L40 to L47. Shorten other lines first.
5. No symbols: no arrows, no "=" or "≥", no Markdown. Use full-width punctuation. Chinese brackets may hold Chinese text only.
6. Do not add 「(估算)」 to the big numbers. They won't fit in the tile, and tile 3 already says both are estimates.

## Notes for Ai 管理層: CRO text mapping (never printed)

Quoted in full on the page, as plain lines:
- G-2 box (`reports/risk/2026-11-26-v66-8-verification.md`, R-7, lines 116 to 122):
  - "AVGO ≤ 6.6% of LNW" is L08. Its reason, "1% ÷ 15% planning gap", is a rationale, not a condition, and is left out.
  - "老詹's close-basis stop on file before 9 Dec" is L10.
  - "retrospective decision record, thesis in your own words" is L09.
  - "No adds" is L11.
  - "LNW, one number, total of all brokerage accounts, by the 3 Dec close" is L06 and L07.
  - "Without it, the CRO recommends exiting AVGO before the 9 Dec print" is L13.
  - "You place every order" is L14.
- §1.2 binding text (`reports/risk/2026-11-25-v66-4-verification.md`, lines 110 to 116), "only if all three are met":
  - "G-1 is cured" is L12. It is met, per R-7 line 102.
  - "LNW above the threshold for the size kept" is L08 and L15 to L20.
  - "stop and decision record on file" is L09 and L10.
  - "If LNW is not disclosed by the 3 Dec close, exit before the print" is L13.
  - "I place no order. The Owner decides." is L14 and L48.
- R-7 thresholds (lines 124 to 126) are L15 to L20. HK$71,800 is left out because the source gives no HK$ figure for 1 share.
- R-7 "what still binds" (lines 108 to 110) is L34 to L36: any negative cash in any currency is a breach, it is escalated at once, it must be cured within 3 sessions, and G-3 means no new position while any debit exists.

Please confirm two readings:
- L13 says "Miss any one". The G-2 box ties the exit recommendation to the missing LNW. §1.2 makes the hold acceptable only if all three conditions are met. The CEO's brief combines the two into "not all done".
- L35 says "tell the AI at once". The source says "escalated at once". Checklist B1 renders that as 「要即刻上報」.

Partly on the page; the rest is a pointer (L38 to the checklist's 「每日訊息」 part, which holds all 9 rules):
- R-6 point 2 is L40 and L41. Pointer only: "taken from #1 down, within the free slots it states".
- R-6 point 5: "Telegram's stop" is in L43. Pointer only: "never TradingView's; a higher stop is self-tightening".
- R-6 point 9 is L42 to L45 and L47. Pointer only: the TradingView feed may differ by cents, and the "at the open" order type should be reported to the AI.
- The checklist G3 line that begins 「C-8 原有」 is L46. Pointer only: the reason, that the broker can't attach a stop.
- L39 calls these "the key ones", not the full rules.

Pointer only:
- R-6 points 1, 3, 4, 6, 7 and 8: L38.
- Checklist A2 and CRO E-1/E-2 (dated no-buy periods) and checklist F (AAPL stop) and B3 (6160 stop): L37.
- R-7's US$10 cash buffer (a recommendation, not a condition): the checklist's 「要你決定」 part, through L48.
- The take-profit rule (F-8) and paper-trade records (R-5): L38 and L48.

## Number sources (never printed)

- Thu 3 Dec 4pm US close, Fri 4 Dec 5am Hong Kong: `strategy/v6.6/電腦待辦清單.md` A1, line 15.
- 9 Dec results, 6.6%: `reports/risk/2026-11-26-v66-8-verification.md` R-7 G-2 box, lines 116 to 117; `reports/risk/2026-11-25-v66-4-verification.md` §1.2, line 96.
- Debt repaid, checked 26 Nov: same R-7 file, line 102; checklist A1, line 16.
- 2 shares and 1 share: the Owner holds 2 (`reports/risk/2026-11-25-webull-readonly-snapshot.md`, line 124).
- US$303.50 on 26 Nov, about US$9,200, about US$4,600: R-7, lines 124 to 126. These are derived figures, tagged [D] in R-7, and the checklist (A1, line 30) marks them 估算.
- About 70 minutes: the checklist's own estimates added up, C 30 (line 118), E 10 + 10 (line 197) and G 20 (line 248).
- 153 passed, 0 failed, 「一致」: checklist C4, lines 136 to 137; CRO V6.6.9 addendum §3.1, R-7 file, line 165.
- Tue to Sat, 6:30am: checklist G2, line 256.
- 3 trading days: R-7, line 109 ("3 sessions"); checklist B1, line 51.
- 4 Dec: checklist A2, line 38.
- 9 rules: checklist G3, lines 266 to 278.
- 9:30pm and 10:30pm: R-6 point 9, R-7 file, line 91; checklist G3, line 274.
- V6.6 and V6.4.2 paper only: checklist F, line 218.

## Fit check (never printed)

- Body lines: Block 1 has 12 (L04, L06 to L14, plus the 2-line tile row). Block 2 has 9. Block 3 has 13. That is 34 in total.
- At 13 pt with 16 pt spacing (5.73 mm a line), 34 lines take about 195 mm.
- Banners, boxes, tiles, panels and gaps take about 76 mm of the 277 mm usable height, which leaves about 201 mm.
- Spare: about 6 mm, roughly one line. With 1.3 line spacing or wider, the page overflows by about 1.5 mm.
- If the Cantonese runs long, fix it in this order:
  1. Trim banner padding by 1 mm each.
  2. Set Block 2's body to 12 pt.
  3. Tell the CEO.
  - Never shrink or cut Block 1, L34 to L36, or L40 to L47.
