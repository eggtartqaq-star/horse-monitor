# Audit: 先睇我.md front page (2026-11-27)

**Auditor:** Ai 管理層 · **Method:** read-only and static. I compared the page with 排版師's English layout, CRO R-6/R-7 (`reports/risk/2026-11-26-v66-8-verification.md`), CRO 11-25 §1.2 (`reports/risk/2026-11-25-v66-4-verification.md`), checklist G3 and `results/release_stamp.txt`.

## Verdict: **PASS WITH CORRECTIONS**

The layout is short and clear. The translation is faithful, and every number traces to a source.

Three omissions block. All three drop a CRO condition the Owner has to act on, and each makes things look easier (L-009):
- **FP-1:** the page asks for one number, but G-2 also needs the AVGO thesis and 老詹's stop before 9 Dec.
- **FP-2:** the most common open-check outcome, "filled, so place your stop now", is missing.
- **FP-3:** R-7's Webull cash rule is missing.

## Checks

| Check | Result |
|---|---|
| (a) G-2 box (:30-38) | **Faithful and complete** against R-7: 6.6% (1% ÷ 15%); 老詹 close-basis stop before 9 Dec; retrospective record in the Owner's own words; no adds; LNW by the 3 Dec close; "Without it… exit… You place every order". R-7's lead-in sentence ("E-1 also bars adds") is dropped, but harmless, since "唔准加注" covers it. 「冇呢個」 keeps the CRO's ambiguity → FP-1. |
| (b) R-6 lines (:48-50) | **Word for word from G3** (points 2 and 9). Pointing to G3 for the rest is fine for the "few cents" bullet and the at-the-open sentence: both are covered by 「券商張單嘅狀態係準則」, or are informational. **Not fine for the C-8 "place your stop" line** → FP-2. |
| (c) Numbers | All VERIFIED: 3 Dec 16:00 ET = 4 Dec 05:00 HKT (EST +13h; Thu/Fri); US$9,200 ≈ HK$71,800 = 607 ÷ 0.066 and US$4,600 ≈ 303.50 ÷ 0.066, both as in R-7 and marked 估算; 153 and `2b7b62182068` match the stamp, line 1; 06:30 Tue–Sat (`schedule_v66.bat`); 21:30/22:30 (R-6); "about 70 minutes" = 30 + 10 + 10 + 20, labelled as an estimate. |
| (d) Drift toward permission | The ⚠️ line is a prohibition, so no drift there (one LOW addition, FP-4). "Setup has no deadline" is true; no CRO deadline applies. 「冇呢個」 can be read as "LNW alone suffices", which is a drift → FP-1. |
| (e) Top block | 11 lines (12 after FP-1), readable in about a minute. **PASS.** |
| Checklist :3-6, :8 | Faithful to Part B; no CRO text displaced. **PASS.** |
| G3 item 8 (:273) | Keeps the CRO's verbatim "V6.6.8" and adds a labelled CEO note giving the V6.6.9 title. Acceptable, and better for L-009 than editing the CRO's text. **PASS.** |

## Findings and exact fixes

**FP-1 · MEDIUM · `先睇我.md:1, :3-5, after :43`.** The page frames G-2 as "one number". The CRO's binding 11-25 text (§1.2) says the hold is acceptable "only if all three are met": G-1 cured; LNW above the threshold for the size kept; "the stop and the decision record are on file".

- **Replace :1 with:**
  `# V6.6 淨係做模擬交易(paper trading),喺你另一個模擬盤戶口(paper account)做;AVGO 有死線:12 月 3 日前交 LNW,12 月 9 日前補決策紀錄同跟老詹止蝕`
- **Replace :3-5 with:**
  ```
  **你要做**
  1. 將你嘅 LNW(全部流動資產淨值:你所有券商戶口加埋,一個數)傳畀 AI,交畀 CRO —— 12 月 3 日收市(close)前
  2. 想持有 AVGO 過 12 月 9 日業績:9 日之前用你自己嘅說話寫低點解買 AVGO(補決策紀錄),同埋答應跟老詹嘅收市價止蝕 —— 未做齊 → CRO 建議 9 日前賣晒(下面個方框)
  3. 設定電腦、Telegram 同 TradingView,即係下面第 1–5 步 —— 冇死線(大約 70 分鐘)
  ```
- **Insert after the threshold table (:43):**
  `CRO 11-25 裁決(`reports/risk/2026-11-25-v66-4-verification.md` §1.2)講明:要 G-1 已清(已清)、LNW 夠上面個表、老詹止蝕同決策紀錄都齊,先可以持有 AVGO 過 12 月 9 日;LNW 12 月 3 日收市前冇交 → CRO 建議 9 日業績前賣晒。`

**FP-2 · MEDIUM · `先睇我.md`, insert after :50.** Your broker cannot attach a stop to the order, so a missed stop after a normal fill is the main live risk. The C-8 line carried in G3 is needed here. **Insert, word for word from G3:**
`> - (C-8 原有)成交咗、而且高過系統止蝕 → **即刻自己落止蝕單**,價位用 Telegram 嘅系統止蝕;券商冇得附加。`

**FP-3 · MEDIUM · `先睇我.md`, insert after :54.** R-7's binding rule on the real Webull account is absent from 「我唔可以做啲咩?」. The CRO lists "keep Webull cash ≥ 0" as an Owner item (§3). **Insert:**
`- 微牛戶口(開住孖展):任何貨幣現金唔可以變負數 —— 變咗就即時違規,3 個交易日內還清,有欠款期間嗰個戶口唔准開新倉(CRO R-7、G-3;清單 B1)。`

**FP-4 · LOW · `先睇我.md:9`.** At the end of the ⚠️ line, append:
「用你券商嘅落單方法 (a) 加 CRO 估算嘅 US$0.35 收費計係 S4(唔准交易),所以真實收費(V-1,清單 D1)未證明之前,只可以模擬。」

**FP-5 · LOW · `先睇我.md:21`.** The Pine alerts fire only on the daily timeframe (`swing_v66.pine:18`, `timeframe.isdaily`). After 「每個圖表開一個警報(alert)」, insert 「(一定要用日線圖)」. If he misses this, the alert never fires and no order is placed, but he would wrongly conclude there was no signal.

*Static audit, read only. Research and decision support, not financial advice. No agent of this firm places orders.*
