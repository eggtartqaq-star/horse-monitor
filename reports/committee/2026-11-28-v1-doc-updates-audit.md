# Audit: V-1 doc updates (2026-11-28)
**Verdict: PASS WITH CORRECTIONS.** No finding is HIGH and nothing opens real money. Three MEDIUM and three LOW findings need fixing before the package goes out. I edited no files.
**Limit on this audit:** I had no shell, so I could not run `git show`. HEAD is 2e7bcda3 and its parent is db115cf8 (`.git/logs/HEAD:161`). I audited the working-tree copies of both files. Please confirm `git status` is clean for them. Every finding below is on a line that carries 11-28 text.
**Checks that passed:**
- **V1-a to V1-d:** in full and faithful in README :21–26 and checklist :165–170.
- **Switch table:** all 8 rows, the veto sentence (:225) and K-6 (:239) are there. The K-6 wording makes the gate unconditional, which is at least as strict as the ruling.
- **§3:** D-1 to D-4 (:310–319) and "Real money under A" (:320) are in full. The screenshot request at :322 is faithful and includes K-1. K-1 = revoke and regenerate the token (`2026-11-28-v66-keep-vote-cro.md:16`).
- **Numbers:** they match the ruling, and I checked them against the feecheck report (FC :30, :32, :57, :83).
  - 13 − 10.2 = 2.8 bp.
  - D-1 time zones are right: 20:00 EST = 09:00 HKT; 20:00 EDT = 08:00 HKT; 09:30 ET = 22:30 / 21:30 HKT.
  - `bp_per_side: 10.2` does not count the 10 bp twice: `ledger_v66.py:574` subtracts it from gross (`lab.py:308`).
- **Account numbers:** none. A search for 7+ digit strings in `v6.6/*.md` found only the fingerprint.
- **Permission drift:** the false reset is present (README :98, checklist :163), and "passed" is never read as an edge (README :15, checklist :159).
**Findings (exact replacement line under each):**
1. **MEDIUM, checklist :321 (L-009).** The B′ paragraph is labelled CRO 原文翻譯 but is shortened. It drops "NOT MET on present facts", the M-2 quote, and "a DAY stop is not an equivalent". Replace with:
    - **B′(M-2):按而家嘅事實,未符合**(CRO 原文翻譯,同一份 §3)。M-2 要求止蝕單「每次開市都掛緊」,類型係「長期有效(GTC)或者券商嘅同等單」。要每日親手處理嘅「當日有效」止蝕單唔算同等。B′ 照舊關;喺微牛香港,除非書面確認有長期有效(GTC)止蝕單,否則開唔到。
2. **MEDIUM, README :3.** "繼續只做模擬交易" reads as "paper continues now", but §2 says paper resumes only after K-1. The checklist (:322) says this; the README does not. Replace with:
> ## ⛔ 狀態(2026-11-28):**未可以轉用。** 唔好落真錢(V6.4.2 同 V6.6 都只係模擬)。V6.6 模擬盤要等 K-1(作廢舊 Telegram token,整個新嘅)做完先可以恢復(CRO 11-28 裁決 §2)。落真錢要等第三節尾「轉用條件」嘅 8 項全部完成(CRO 11-28 起取代下面五樣)。
3. **MEDIUM, README :98.** The ruling's "may set" has become an instruction. The text also says the settings file needs no citation, which contradicts the ruling ("citing this file") and checklist :163. Replace with:
   **11-28 更新:已經做咗,V-1 過咗**(見頂部方框第 2 點)。你**可以**喺 `owner_settings.json` 填 `"real_fee": {"min_per_side_usd": 0, "bp_per_side": 10.2}`,同埋將 `"V1_真實收費已核"` 改做 `true`,依據係 `reports/risk/2026-11-28-v1-ruling.md` §1(AI 會記入決策紀錄)。**如果 V1-b 或者 V1-d 觸發 S4,要改返做 `false`。** N-30 喺 11-26 已經唔再做:下面講 `--tif day` 等 N-30 嗰句只係歷史,`--tif day` 淨係參考。
4. **LOW, README :232.** 連同 reads as "V1-a to V1-d are met too"; the ruling means "subject to". Replace with:
| 4 | V-1 冇觸發 S4 | **11-28 已符合**,但附帶 V1-a 至 V1-d 條件 |
5. **LOW, checklist :117.** It names only V1-a to V1-d as the remaining step before real money, next to a recommendation that waits on V-1. Replace with:
    **11-28 更新:** 真實收費係佣金 US$0、平台費 US$0。V-1 用 `--tif open` 計過咗,冇觸發 S4(見 D1)。但呢個結果唔證明有優勢。落真錢之前,要做到 V1-a 至 V1-d(全文見 D1),同埋 README 第三節尾「轉用條件」8 項全部完成,包括 CRO 書面簽署。
6. **LOW, checklist :257.** "恢復模擬盤唔使" appears without K-1. Replace with:
| D1(11-28 補) | 美股止蝕單「有效期」選項截圖(真戶口同模擬盤 App;遮住戶口號碼)—— 落真錢之前同開 B′ 要;恢復模擬盤唔使,但恢復模擬盤照要等 K-1 做完 |
**Stale lines I couldn't confirm are in the diff (CEO to decide):**
- Checklist :97 still says "README 頂部方框其餘幾樣", which the 8-row table now replaces.
- README §4 (:244–251) does not mention the new M-2 GTC requirement for B′. Suggest a pointer to checklist G3.
**For 床狗:** two patterns repeat. Text labelled 原文翻譯 gets shortened (finding 1), and a CRO "may" becomes an instruction (finding 3).
