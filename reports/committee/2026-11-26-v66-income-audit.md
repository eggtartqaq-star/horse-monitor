# Audit: V6.6 income study, Owner-facing text (2026-11-26)

**Auditor:** Ai 管理層 (Dept 9) · **State:** HEAD `605eee8`, as reported to me · **Method:** read-only, static. No code was run, and no file was edited.
**Standard:**
- CRO `reports/risk/2026-11-26-v66-6-verification.md`: R-1 to R-4, N-29, and the §3 addendum (F-3 ruling, C-8, N-30).
- Tom `reports/quant/2026-11-26-v66-income-study-review.md`.
- `strategy/v6.6/results/income_{scenarios,decomposition,yearly,bootstrap}.csv`.
- L-009.

## 0. Verdicts

| Document | Verdict | Blocking (MEDIUM) |
|---|---|---|
| `reports/quant/2026-11-26-v66-income-study.md` (§0, §1.4, §4, §5, §6) | **PASS WITH CORRECTIONS** | S-1, S-2, S-3 |
| `strategy/v6.6/電腦待辦清單.md` B1, B4, D1 | **PASS WITH CORRECTIONS** | K-1, K-2, K-3, K-4 |
| `strategy/v6.6/README.md` banner items 2–3 and V-1 step | **PASS WITH CORRECTIONS** | RM-1, RM-2 |

No HIGH findings.

**The main finding is in all three documents.** The CRO's rule "until N-30 lands … **V-1 is judged with `--tif open`**" (§3.2) has been dropped.
- **What N-30 is:** the code change that makes scanner ① and the bot print the new C-8 wording.
- **Status:** it has **not** landed. `daily_scan_v66.py:283-284` still prints 「開市價高過就唔買」 and 「開市價 ≤ 系統止蝕 → 唔買」.
- **Why it matters:** as written, the Owner could declare DAY, pass V-1 on `--tif day` (+0.367%), and then trade by the printed cancel-at-open text, which fails S4 at US$0.35 (−0.066%). The gate would be testing a different rule from the one traded. That is the N-29 failure mode again, and it points toward permission (L-009).

**What holds:**
- Every number in scope traces to a CSV or the CRO file. The one exception is S-6 (LOW).
- No stale fingerprint or count: 131 and `fae5fa5a7403` match `results/release_stamp.txt:1`. There is no "39%" and no 20% reserve; V6.6.5 is mentioned only as history.
- The R-1 and C-7 (A)/C-6 blocks are quoted faithfully, in both English and Cantonese.
- "(B) recommended by the CRO and CEO", "the choice is yours", "backtest, not forecast" and "not financial advice" are all present.

## 1. Claims checked

| Claim (location) | Source | Result |
|---|---|---|
| §0 table, all 6 rows (trading, interest, total, all-T-bill, extra, OOS) | `income_decomposition.csv:2-25` | VERIFIED |
| §0 "HK$430–770 (36–64/month)"; interest "440–470"; trading "−9 to +295", "−340" | decomposition totals 432/559/625/766; interest 441–471 | VERIFIED; the range mixes 4 scenarios → S-4 |
| "28% to 75%"; "t −0.91 to +0.84" (§0) | `income_bootstrap.csv` 60-month "+mean uncertainty" column 27.6–75.42; t column | VERIFIED |
| 100k: open −191/−367; DAY +401/+586; OOS −1,318/−1,521 (§0, §2.3) | decomposition rows 50-57 | VERIFIED (study). The checklist misstates it → K-3 |
| §1.4 gate table: 3 of 4 rows | CRO §1 N-29 table and §3.1 | VERIFIED |
| §1.4 "0 + 10 bp, DAY: +1.087 / +0.678 / +1.240%" | Not in the CRO file, Tom's file or any CSV | **UNTRACED** → S-6 |
| 43 → 7 skips; 46 trades +1.005% vs −0.012%; Tom's 25 of 43 | scenarios CSV col. 15; CRO §3.2; Tom :55 | VERIFIED |
| §2.1 rows and DAY rows; §2.4 years; "4 of 5 / 3 of 5 / 2 of 5" | scenarios and yearly CSVs | VERIFIED |
| Hurdle HK$130–160/yr; HK$4–5 per trade | decomposition "少收咗嘅利息" 129–159; ÷ 33–35 trades | VERIFIED |
| Drawdowns "−3% to −4%", "−11%"; "66–70 orders/yr" | max DD −2.82 to −4.23; −10.98; 130 and 139 trades ÷ 3.98 yrs × 2 orders | VERIFIED |
| 363-case check; 7.9% average position; 12/30/58%; +1.45 to +1.70% | Tom :44, :143, :155 | VERIFIED (the CRO §1 says "400 random cases"; immaterial) |
| R-1, C-7 (A)/C-6 block, R-3 (study §5; checklist B1, B4) | CRO R-1, R-2 block, R-3 | **Faithful.** Gaps: S-2, K-4, K-7, K-8, RM-2 |
| F-3 ruling (study §1.4; D1; README :10, :83) | CRO §3.2 | **N-30 / `--tif open` qualifier dropped** → S-1, K-1, RM-1. Full C-8 missing → S-3, K-2 |

## 2. Findings and exact fixes

### MEDIUM

**S-1 · study :96.** The N-30 qualifier is dropped.
- **Replace** "Until then, the printed cancel-at-open text governs." **with:** "Until then, the printed cancel-at-open text governs, **and V-1 is judged with `--tif open`** (CRO §3.2)."

**S-2 · study :257-258.** The verdict lists only three conditions and leaves out R-3: "If LNW is below that, the answer is (B) shadow-only, whatever V-1 shows."
- **Replace :257 with:** "- As a small sleeve that **might** add a little and is unlikely to do serious harm, it can run long-term only once **all** of these hold: C-6 is cured; V-1 passes on the live rule with the order type declared in advance (`--tif open` until N-30 lands); the sleeve is ≤ 10% of LNW (LNW ≥ HK$125,000 at HK$12,500, otherwise (B) whatever V-1 shows; CRO R-3); the other README switch conditions close; and the Owner chooses (A). The CRO and CEO still recommend (B)."
- **At :258,** change "about 30–75%" to "28–75%, depending on fee and order type".

**S-3 · study :96 (parenthetical).** The C-8 summary drops several parts of the rule:
- "Never place the buy without the attached stop";
- "do not raise the limit, do not add shares";
- the printed share count;
- "E2 stop raised daily, never lower".

**Replace the parenthetical with** "(the CRO's 26 Nov C-8, quoted below)", **then insert after :96:**
> **C-8 (26 Nov: DAY order with attached stop).**
> - **Placing the order:** buy only with a **limit order, time-in-force DAY**, at or below the **限價上限 (maximum limit price)** printed by scanner ① or the bot, for the printed number of shares.
> - **Attached stop:** attach to the **same order** a **sell-stop at the system stop** (OTO / bracket), so it goes live the moment the buy fills. **Never place the buy without the attached stop.**
> - **No fill:** if the order is not filled by the close, it expires. Do not re-enter it the next day, do not raise the limit, do not add shares.
> - **Open at or below the system stop:** the buy may fill and the attached stop will sell at once. Record both the same day (`fill open`, `fill close`) and send the S2 to the CRO.
> - **E2 stop:** raise the broker stop each day to section ④'s stop (C-9). Never lower it.
> - **No attached stop at your broker:** (b) does not apply. Watch the open, and cancel if the open is above the limit or at or below the system stop. V-1 is then judged with `--tif open`.

**K-1 · checklist D1 :144-146.** The N-30 qualifier is dropped: D1 lets V-1 use `--tif day` before N-30 lands. **Replace :144-146 with:**
```
    - 你券商**可以**喺美股現金戶口落「限價買入、全日有效(DAY)」**同時附加止蝕賣單**(OTO / bracket),而你書面確認 → 可以揀全日單 (b)。
      **但係要等 AI 將掃描器同 bot 嘅落單寫法改做 CRO 11-26 嘅 C-8 新版(N-30)、CRO 核對完,先可以用全日單,V-1 先可以用 `--tif day` 計。**
      **N-30 未改好之前:照而家嘅寫法落單,V-1 一律用 `--tif open` 計**(CRO 11-26 §3.2)。
```

**K-2 · checklist D1, insert after :146.** The full C-8 for (b) is missing. **Insert:**
```
    - **用全日單 (b) 時嘅 C-8(CRO 11-26 原文翻譯,取代 11-25 版本):**
      - **落單:** 淨係用**限價單、全日有效(DAY)**,限價**唔可以高過**掃描器 ① 或者 bot 印出嚟嘅**限價上限**,股數用印出嚟嗰個。
      - **附加止蝕:** **同一張單**附加一張**止蝕賣單,價位 = 系統止蝕**(OTO / bracket),買入一成交就即刻生效。**冇附加止蝕就永遠唔好落買單。**
      - **冇成交:** 收市前未成交,張單自動失效。**第二日唔好再落、唔好加價、唔好加股。**
      - **開市價 ≤ 系統止蝕:** 買單可能成交,附加止蝕會即刻賣出。當日用 `fill open` 同 `fill close` 記錄兩筆,S2 交 CRO。
      - **引擎二止蝕:** 每日將券商止蝕單調高到 ④ 嘅止蝕位(C-9),**永遠唔好調低**。
      - **你券商冇得附加止蝕:** (b) 唔適用。要睇住開市:開市高過限價上限,或者 ≤ 系統止蝕,就取消張單;V-1 用 `--tif open` 計。
```

**K-3 · checklist B4 :83.** The HK$100k figures are misstated.
- The full-period range drops the worse number: −367 (real35, cancel-at-open).
- The "after 2025" figures are DAY-order only; cancel-at-open was −512/−691.

**Replace :83 with:**
```
    - 加大本金唔幫到手:HK$100,000 每年 **−HK$367 至 +HK$586**(開市取消單 −HK$191 至 −HK$367;全日單 +HK$401 至 +HK$586)。2025 年之後:開市取消單 −HK$512 至 −HK$691,全日單 −HK$1,318 至 −HK$1,521。
```

**K-4 · checklist B4 :85.** The conclusion leaves out R-3 (LNW) and N-30. **Replace :85 with:**
```
  - **結論(CRO 同 CEO):** 可以當一個細嘅附加部分長期跑,但要**全部**做到:C-6;V-1 用實盤規則、預先講明嘅落單方法過關(N-30 未改好之前用 `--tif open`);短線戶口 ≤ 你 LNW 嘅 10%(LNW ≥ HK$125,000,唔夠就只可以揀 (B),見下面 R-3 第 2 點);README 頂部方框其餘幾樣完成;你揀 (A)。**唔可以當生活費收入**,真正嘅收入係 T-bill。
```

**RM-1 · README :10 and :83.** The N-30 qualifier is dropped, and the S4 test is under-stated.
- **:10, replace** "再跑 `lab.py --mode feecheck --tif open/day`(用實盤入場規則,CRO N-29)。淨 EV ≤ 0(S4)" **with:** "再跑 `lab.py --mode feecheck --tif open/day`(用實盤入場規則,CRO N-29;**N-30 未改好之前一律用 `--tif open`**)。全期或者樣本外淨 EV ≤ 0(S4)"
- **:83, replace** "`--tif day` 淨係喺你書面確認券商可以「全日限價單附加止蝕」之後先用(CRO 11-26 F-3)。)" **with:** "`--tif day` 淨係喺你書面確認券商可以「全日限價單附加止蝕」**而且** N-30(掃描器同 bot 改印 C-8 新版)已經改好、CRO 核對完之後先用;之前一律用 `--tif open`(CRO 11-26 F-3)。)"

**RM-2 · README banner item 4 (:19-25).** The banner contradicts checklist B1 and is missing R-3.
- **The contradiction:** :20 says 「冇其他持倉」 with no exception, while B1 :49-50 allows R-1 cash equivalents.
- **The gap:** the banner has no R-3 (the 10% of LNW cap).
- **Changes:**
  - **:19:** change 「(CRO 11-25 裁決,`reports/risk/2026-11-25-v66-4-verification.md`)」 to 「(CRO 11-25 裁決、11-26 修訂,`reports/risk/2026-11-26-v66-6-verification.md` R-1 至 R-3)」.
  - **:20:** after 「冇其他持倉」 insert 「(11-26 起准許 CRO R-1 嘅現金等價物,例如短期 T-bill;見 `電腦待辦清單.md` B4)」.
  - **Insert after :25:**
    > `>    - **R-3(11-26):** 短線戶口 ≤ 你流動資產淨值(LNW)嘅 10%;HK$12,500 即 LNW ≥ HK$125,000。唔夠 → 只可以揀 (B),V-1 結果點都一樣。未來最少 12 個月生活費唔好放落任何交易戶口。`

### LOW

- **S-4 · study :33.** After "at the zero-commission and US$0.35 fee levels", add: ", across both order types (lowest: US$0.35 with cancel-at-open, which fails S4; highest: zero commission with DAY orders)".
- **S-5 · study §4 :258.** Make it consistent with §0. This is covered by S-2.
- **S-6 · study :86.** Append to the table note: "(The 0 + 10 bp DAY row is the CEO's feecheck run at `a496ba4`; it is not in committed output and was not reproduced by the CRO. The other three rows are CRO-reproduced, verification §1 and §3.1.)"
- **S-7 · study :300.** After "that is S4: no trading at any cap", insert "(with `--tif open`; with a DAY order and an attached stop the US$0.35 estimate passes, subject to the 46-trade caveat below)".
- **K-5 · checklist B4 :104.** It contradicts D1 after the F-3 ruling. **Replace with:**
  ```
      V-1 確認每邊最低收費大約 US$0.35 或以上,而用「開市冇成交就取消」(`--tif open`)計 → **S4,用咩上限都唔准交易**,唔係「遲啲揀 (A)」。用全日單 (b) 加附加止蝕計會過關,但 CRO 提醒:成個分別嚟自 46 筆盤中成交,冇實盤證據,CRO 照建議 (B)。決定係你嘅。
  ```
- **K-6 · checklist B4 :80, :82, :84.** Ranges that mix scenarios, plus jargon.
  - **:80:** after 「(每月 HK$36–64」 add 「;最低係 US$0.35 收費加開市取消單,最高係零佣金加全日單」.
  - **:82:** after 「**−HK$168 至 +HK$166**」 add 「(零佣金或者 US$0.35 收費、兩種落單方法;US$1 壓力情境係 −HK$426 至 −HK$528)」.
  - **:84:** change 「每筆淨 EV」 to 「每筆淨 EV(每筆交易扣晒收費之後平均賺幾多)」.
- **K-7 · checklist B4 :87, :90.** The R-3 floor and the E-2 window are missing.
  - **:87:** change 「未來 12 個月嘅生活費」 to 「未來**最少** 12 個月嘅生活費(你可以揀更長)」.
  - **:90:** append 「E-2 由 12 月 4 日開市起,直至 MU 業績後第一個完整交易日收市(大約 12 月 17 日)。」
- **K-8 · checklist B1 :50.** Append: 「**(A) 另外要符合 CRO R-3:短線戶口 ≤ 你 LNW 嘅 10%(HK$12,500 即 LNW ≥ HK$125,000);唔夠就只可以揀 (B)(見 B4)。**」
- **RM-3 · README :15.** Change 「代碼方面可以轉用。✅」 to 「代碼方面可以轉用(用全日單 (b) 之前仲要 N-30:掃描器同 bot 改印 C-8 新版,CRO 再核對)。✅」
- **RM-4 · README :78.** Change 「feecheck 過咗(淨 EV > 0)」 to 「feecheck 過咗(全期**同埋**樣本外淨 EV 都 > 0)」.

## 3. Checklist (a)–(e)

| Check | Result |
|---|---|
| (a) L-009 | R-1: faithful (B4 :91-98; study :281-286). C-7 (A)/C-6: faithful (B1 :48-57; study :273-279). R-3: faithful in B4 :86-90, but missing from the conclusions and the README (S-2, K-4, K-8, RM-2). **F-3: the N-30 / `--tif open` qualifier is dropped in all three documents (S-1, K-1, RM-1), and the full C-8 is missing (S-3, K-2).** |
| (b) Numbers | All traced except S-6. Mixed-scenario ranges: S-4, K-6. One misstatement: K-3. |
| (c) Overclaiming | Clean: "backtest, not forecast" (:13, B4 :79); "cannot be counted on" (:44, B4 :85); (B) recommended by the CRO and CEO, Owner's choice preserved (:300-303, B4 :103-104); not advice (:13). Weak spot: "can run long-term" is stated with incomplete conditions (S-2, K-4). |
| (d) Clarity and consistency | The Cantonese is plain. Contradictions: README banner vs B1 on cash equivalents (RM-2); B4 :104 vs D1 on US$0.35 under DAY (K-5). |
| (e) Stale items | None. 131 / `fae5fa5a7403` match the stamp; no 39%; no 20% reserve. |

## 4. Bias observations

1. **L-009 recurred, in one direction.** The dropped qualifiers all made trading easier:
   - V-1 on `--tif open` until N-30;
   - "never without the attached stop";
   - "don't raise the limit or add shares";
   - the R-3 LNW condition in the conclusions;
   - the worse 100k figure (−367) and the cancel-at-open out-of-sample figures (−512/−691).

   **Counter-evidence:**
   - the R-1 and C-7 translations are complete, including the reasons;
   - the study puts N-29 and S4 in §0;
   - the 46-trade caveat reaches the Owner.
2. **No groupthink.** Tom's concerns (F-1 to F-8) and the CRO's stricter reading (N-29, "no demonstrated edge") are both carried through, and the CRO and CEO converge on (B) for stated reasons.
3. **For 床狗:** when the CRO attaches an "until X lands" clause to a ruling, the Owner-facing text must carry that clause wherever the ruling is restated. Grep for the ruling's identifier (here N-30 and `--tif`) in every Owner file.

*Static audit: no code executed. Research and decision support, not financial advice. No agent of this firm places orders.*
