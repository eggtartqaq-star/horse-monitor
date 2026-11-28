# Audit: Webull fee sheet (2026-11-28)

**Verdict: FAIL, fixable with line replacements.** Every number and label matches the evidence file (sheet lines 2–3, 8, 10–11, 17, 25–26 against evidence sections 1–2). The session labels also match the fill times: 正常時段 filled at 10:01:25 EDT, 夜盤 at 23:50:04 EST. The sheet has no account number, no Markdown and no internal codes. V6.6 and CRO are fine, because the Owner's own decision sheet uses them. Lines 13, 14, 21 and 22 are correct. The failures are lines that state unknown or derived things as fact, and one stop line that drifts toward permission.

1. **Line 9, High (check 2).** It states the SEC meaning as fact. Evidence line 35 says "derived; the fee schedule itself was not seen". The evidence table also puts the overnight **buy's** US$0.02 under the same 證監會規費 column, and a fee charged on sells does not explain that. Replace with: `G	單據寫「證監會規費」。似係美國證監會對賣出收嘅費,但未核實。`
2. **Line 23, High (checks 3 and 4, L-009).** "再作決定" makes it look as if a day-only stop could still be accepted. Ruling lines 154–155 and 165 already settle this: the stop must be good-till-cancelled or the broker's equivalent, and if the broker only offers day stops, B′ is not enabled. The line also leaves out the Owner's own task in ruling line 164: confirming in writing. Replace with: `G	要你書面確認:止蝕單類型,同埋佢過夜係咪仍然有效。`
3. **Line 24, Medium (check 3).** The pointer gives no section, but the ruling holds many conditions. `templates/owner-brief.md` line 13 requires a plain section name. Replace with: `G	CRO 嘅止蝕條件全文:見11月28日 CRO 裁決入面「券商止蝕單係前提」嗰部分。`
4. **Line 4, Medium (check 2).** "淨係" says there are no other fees, but nobody has seen the detail fee page (evidence lines 17 and 44). The sheet's own line 14 says the same. Replace with: `T	單據上剩低嘅係規費,得幾仙;詳細收費頁未睇到。`
5. **Lines 18–19, Medium (check 4).** Yes, this over-promises. Evidence line 33 defines the real cost as cents of fees **plus** spread and slippage at 10 bp per side, which is an assumption. My arithmetic: 10 bp on the US$1,307.78 sell is about US$1.31, more than the old US$0.35 estimate. Replace with: `T	三張單據嘅收費低好多:每張 US$0.00 至 US$0.03。` and `G	但買賣差價同滑價仍然係成本,照舊按每次買或賣 0.1% 嘅假設計入。`
6. **Line 1, Low (check 4).** The headline repeats the "淨係幾仙" certainty. Replace with: `B1	微牛美股:佣金同平台費 US$0 | 根據收費頁同你三張成交單據`
7. **Line 12, Low.** "買入都收咗費" generalises from one buy; the regular-hours buy paid US$0.00. Replace with: `T	夜盤買入都收咗費,AI 冇預計到;正常時段買入就冇收。`
8. **Line 20, Low.** "做緊" can't be verified: `/home/user/horse-monitor/reports/quant/2026-11-28-v1-feecheck.md` does not exist yet, and the evidence lists that run under "Next". Replace with: `S	新計算未有結果,有結果再話你知。`

**Also:**
- `/home/user/horse-monitor/reports/owner-summaries/2026-11-28-webull-fees.html` has already been rendered from the old text (old line 24 is at html line 73). Re-render it after the fixes.
- For 床狗 and 翻譯官, the root cause of item 1: `/home/user/horse-monitor/knowledge/owner-glossary-yue.md` line 111 records "SEC fee on sells" as fact. It should be marked as derived.
- Item 2 is the same L-009 drift toward permission that has happened before.
- Limit: I checked against the CEO's transcription only. I did not see the Owner's screenshots.
