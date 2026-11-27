# Audit: Owner front page v2 PDF (2026-11-27)

**Auditor:** Ai 管理層 · **Method:** read-only and static. I read `reports/owner-summaries/2026-11-27-start-here-v2.txt` against:
- CRO R-6 and R-7 (`reports/risk/2026-11-26-v66-8-verification.md`);
- CRO 25 Nov §1.2 (`reports/risk/2026-11-25-v66-4-verification.md:110-122`);
- checklist C1/C3/C4/G2/G3 (`strategy/v6.6/電腦待辦清單.md:120-136, :259, :272, :279`);
- `results/release_stamp.txt` (V6.6.9, `2b7b62182068`);
- `scripts/owner_pdf.py` and `scripts/owner_pdf_render.js`.

I did not render the PDF.

## Verdict: **PASS WITH CORRECTIONS**

The page is plain and has no codes or English in brackets. The AVGO box, the Webull rule and the open-check outcomes are faithful. Five items must change:
- **L13** over-generalises the consequence and contradicts the 1-share tile (F-1).
- The page has **no "no message / ⛔ / slots full → no order"** line (F-2).
- **L23's install step** does not produce the `Desktop\v6.6` folder that L29b's command needs (F-3).
- **6160's act-now items** are missing (F-4).
- The **builder can clip lines silently** (B-1).

## Checks

| # | Item | Result |
|---|---|---|
| 1 | AVGO L04–L13 | **Complete:** LNW by the 3 Dec close (L06–L07), 6.6% (L08), thesis before 9 Dec (L09), 老詹's close-basis stop before 9 Dec (L10), no adds (L11). **L12 is correct:** debt cured, USD +0.66 on the 26 Nov re-pull (R-7 :102). **Deadline correct:** Thu 3 Dec 16:00 ET = Fri 4 Dec 05:00 HKT (EST, UTC−5). **L13 reading:** correct for LNW (explicit: "exit before the print") and for the stop and record (§1.2: the hold is acceptable "only if all three are met"). **Not correct for the size item:** if LNW covers 1 share but not 2, the CRO's option is "(2) sell 1 share" (§1.2), not sell all → F-1. |
| 2 | Tiles L15–L20 | VERIFIED: US$607 ÷ 0.066 ≈ US$9,200 and US$303.50 ÷ 0.066 ≈ US$4,600 (R-7 :124-126); priced at 26 Nov; L20 says both are estimates. Dropping HK$71,800 is acceptable. |
| 3 | Webull L34–L36 | **Faithful** to R-7 :108-110: any currency below zero is a breach; tell the AI at once (the escalation goes through the AI); cure within 3 trading days; no new positions until cured. |
| 4 | Trading L38–L47 | **Faithful** to G3 and C-8:<br>- two-source rule (L40–L41);<br>- 9:30pm / 10:30pm (L42);<br>- broker status decides; stop always from Telegram (L43);<br>- not filled (L44); filled at or below the stop (L45); filled above the stop, place your own stop at once (L46);<br>- can't watch the open → no order (L47).<br>Pointing to the 9 rules (L38) is acceptable, **except** for point 7 (no-order days) → F-2. |
| 5 | Setup L23–L31 | Both commands are exact (L24, L29b–c). 153 matches checklist :136, and 「一致」 replaces the fingerprint correctly. 06:30 Tue–Sat is correct. **L23** → F-3. **L30** states the 06:30 message as certain → F-2. |
| 6 | Drift and leftovers | No English in brackets and no internal codes (CRO, AI, CMD and token are allowed by the layout's note 2). Lines over 25 characters: L12, L13, L22, L30, L37, L43, L48. Not blocking. |
| 7 | Builder | `build()` emits every ID: L01–L48 plus L29a–d (the L29 "cmd" branch uses a–d). The HTML drops nothing. **But** `.page { height: 297mm; overflow: hidden }` clips any overflow silently, and `owner_pdf_render.js` only logs the metrics → B-1. A missing line only prints a warning (`owner_pdf.py:135-136`) → B-2. |

## Findings and exact replacements

**F-1 · MEDIUM · L13.** It contradicts tile L17–L18, and so the CRO's §1.2 option (2).
Keep L13 and **add L13b** directly under it:
「例外:你個數淨係夠留1股,就賣1股、留1股。」

**F-2 · MEDIUM · L30, and after L41.** R-6 point 7 (no-order days) is an every-morning rule the Owner acts on, and the checklist (:259) treats "no message" as an error. L30 also states the 06:30 message as certain, although the scheduler cannot be tested here.
- **L30, replace with:** 「雙擊 schedule_v66.bat。之後星期二至六,香港時間朝早6:30應該有訊息。」
- **Add L30b:** 「朝早冇收到訊息,就當出錯:當日唔好落單。」
- **Add L41b (in the panel, after L41):** 「Telegram 寫「停開新倉」或者「倉位已滿」:當日唔好買。」

**F-3 · MEDIUM · L23.** "Unzip to the Desktop" produces a nested repository folder, not `Desktop\v6.6`, so L29b's `cd` fails. The engine file is also unnamed, and the ledger-keep rule is missing (checklist C1 :122-125, C3 :130).
- **L23, replace with:** 「將 ZIP 入面嘅 v6.6 資料夾搬去桌面。」
- **Add L23b:** 「由 V6.4.2 資料夾複製 dual_engine_v6_4.py 入去,唔好改佢。」
- **Add L23c (grey sub-line):** 「之前裝過 v6.6:唔好覆蓋 owner_settings.json 同 ledger。」

**F-4 · MEDIUM · L37.** 6160 has dated Owner actions: the committee meets before 11 Dec, and the Owner must give the share count, broker and account type, and a written stop commitment (CRO pre-review §3, §6; checklist B3). L37 points only to "stops".
- **L37, replace with:** 「仲有效:AAPL 同 6160 嘅止蝕,同12月4日起嘅禁買日。」
- **Add L37b:** 「6160:12月11日前要交資料同書面答應止蝕,見清單「要你決定」。」

**F-5 · LOW · L27.** 「記錄檔」 can be misread as the ledger. Replace with: 「然後雙擊一次掃描_v66.bat。將相片同 selftest_last.log 傳畀 AI。」

**F-6 · LOW · L29a.** The `cd` command makes the location irrelevant. Replace with: 「喺 CMD 打:」

**F-7 · LOW · L28.** 「舊 token 洩漏咗」 is not verified in any source I read. Replace with: 「Telegram:先作廢舊 token,整個新嘅,永遠唔好傳畀 AI。」

**F-8 · LOW · L31.** The Pine account setting must match (R-6 point 8). **Add L31b:** 「設定入面「短線資金(HKD)」填 10000。」 It is screen text, so it is copied exactly.

**B-1 · MEDIUM · builder.** Overflow is clipped silently, and the new lines from F-1 to F-4 and F-8 add about 8 lines (≈ 45 mm) against about 6 mm of spare space (layout fit check).
- **The CEO must re-fit the page.** Use the layout's own order (banner padding, then Block 2 size), then move Block 2 detail to the checklist. Never cut Block 1, L34–L36 or L40–L47.
- **`scripts/owner_pdf_render.js`, insert before `await b.close();`:**
  ```js
  if (!(m.lastBlockBottom <= m.footerTop && m.footerBottom <= 1123)) { console.error('OVERFLOW: content clipped'); await b.close(); process.exit(1); }
  ```
- **`scripts/owner_pdf.py:136`, after the `print("missing lines:", missing)` line, add:** `sys.exit(1)`
- **Update `build()`** to emit the new IDs: L13b, L23b, L23c, L30b, L31b, L37b, L41b. It hard-codes IDs, so new lines would otherwise be dropped.

**B-2 · LOW.** Covered by the `sys.exit(1)` above.

## Your two questions to the auditor (layout notes)
- **L13 "Miss any one":** acceptable, with F-1's exception added.
- **L35 「即刻話 AI 知」 for "escalated at once":** acceptable. The escalation runs through the AI.

*Static audit: no rendering done. Research and decision support, not financial advice. No agent of this firm places orders.*

---

## CEO disposition (added by the CEO after the audit; the text above is the auditor's reply, verbatim)

I checked each finding against its source before acting.

| Finding | Disposition | Source checked |
|---|---|---|
| F-1 | **Applied**, L13b verbatim. | CRO 11-25 §1.2, option (2) "Sell 1 share" |
| F-2 | **Applied.** L30 verbatim and L41b verbatim. L30b is widened to 「冇收到訊息,或者訊息寫出錯:當日唔好落單。」, so it also covers the self-test / scan-error warning. | Checklist G2 (:259) and G3 point 7; Telegram strings in `notify_v66.py:77, :96` (「停開新倉」, 「倉位已滿」) |
| F-3 | **Applied**, L23, L23b and L23c verbatim. | The delivered zip's root is `v6.6/`. Windows "Extract All" adds a folder named after the zip, so L29b's `cd` would fail. Checklist C1 and C3. |
| F-4 | **Applied**, L37 and L37b verbatim. | Checklist F (AAPL stop $325.08) and B3; CRO 6160 pre-review (committee before 11 Dec); section B title 「要你決定」 |
| F-5 | **Applied.** | `掃描_v66.bat:10` writes `selftest_last.log` |
| F-6 | **Applied.** | n/a |
| F-7 | **Applied.** | Checklist E (:200), `/revoke` |
| F-8 | **Not applied.** The Pine default for 「短線資金(HKD)」 is already 10000 (`pine/*.pine:26`) and equals `owner_settings.json` `account_hkd: 10000`. A freshly pasted indicator matches, and checklist G3 point 8 keeps the full rule. Space on the one-page PDF the Owner chose was the deciding factor. | n/a |
| B-1 | **Applied.** `owner_pdf_render.js` exits 1 when the content does not fit one A4 page. The page was re-fitted: body 12.5pt, setup 11.5pt, the Telegram test on one row, tighter spacing. Nothing was cut from the AVGO box, the Webull rule or the trading lines. Final fit: last block 1099 px, footer 1108–1121 px, A4 = 1123 px, 1 page. | n/a |
| B-2 | **Applied.** `owner_pdf.py` exits 1 on a missing line, and also on a line that `build()` does not place. | n/a |

The rendered text was checked: no internal codes (only on-screen version names V6.6 and V6.4.2), no Markdown symbols, and no missing glyphs.
