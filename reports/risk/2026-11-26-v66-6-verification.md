# CRO: V6.6.6 verification, and rulings on the income study

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-26 · **HEAD:** `99b2177`
**Scope:**
1. `git diff b102f6b cf41d84 -- strategy/v6.6` (V6.6.6, fingerprint **`943960c97a9b`**);
2. §8 of `reports/quant/2026-11-26-v66-income-study.md` (CEO), with `income_study.py` at `99b2177`.

**Method:**
- A scratch copy (`git archive 99b2177`) with `data/` symlinked in, used read-only. I did not run `income_study.py`, which writes `data/TBILL.csv`. I reproduced its headline numbers by calling `lab.simulate` directly.
- **Kept to the rules:**
  - no broker call;
  - no `pip install`;
  - no tracked file modified;
  - scratch copies removed, no temp-dir leak.

**Tags:**
- **[C]** a cited file;
- **[D]** my run or my arithmetic;
- **[A]** my assumption.

## 0. Verdicts

**(1) V6.6.6: PASS.**
- **What changed:** `entry_rule="limit"`, `capital_hkd`, `cash_yield` and `cash_reserve_pct` are correct, and the defaults reproduce the old behaviour byte for byte.
- **Code side of the switch:** stays **CLEAR**, with **one new condition: N-29**. The S4/V-1 fee gate (`lab.py --mode feecheck`) still tests the **old** entry rule, and under the **live** rule the N-9 fee estimate gives **negative** all-period EV. N-29 must be fixed **before V-1 is judged**.
- **Risk score:** 76 for the code; unchanged.
- **B′:** OFF.

**(2) Income study:** five rulings (§2).
- **In short:** the CEO's reading is right. The sleeve is acceptable only as a small capital-preservation sleeve, and it is **not** an income source.
- **I go further than the CEO:** at the N-9 fee estimate under the live entry rule, the system has **no demonstrated edge** (N-29).
- **(B) shadow-only is my recommendation** until V-1 is in and passes on the live rule.

**G-1 status:** the debit is **CURED** per the CEO's 26 Nov read-only re-pull (USD +0.66; snapshot addendum) [C].
- That means no sell recommendation is triggered.
- **C-6 is still NOT MET:** the account is still `INDIVIDUAL_MRGN`. G-2 still needs LNW by the 3 Dec close (§2, R-3).

## 1. V6.6.6 verification

| Check | Result | Evidence [D] |
|---|---|---|
| Only `lab.py`, `selftest.py`, `config_v66.py` (VERSION/RELEASE_DATE) and the stamp changed | **PASS** | `git diff --stat b102f6b cf41d84` shows 4 files. Sizing, signals, rules, guardrails, indicators, scanner, ledger, bot, `owner_settings.json`, `pc_check.py` and `parity_check.py` show 0 lines changed. `99b2177` adds only `income_study.py` and the `results/income_*.csv` files (not in `CORE_FILES`). |
| Fingerprint and stamp | **PASS** | `943960c97a9b`, the same in scratch and repo. `pc_check.stamp()["match"]` is True. The test hash changed only for `selftest.py` (`11191f51b203`). |
| selftest | **PASS** | **126/126**, exit 0, normal and `-O`, in scratch and in the repo. |
| `equivalence_check` / `ledger_check` | **PASS** | 85,120 / 0 differences; LEDGER CHECK PASS. |
| `lab.py --mode baseline` | **PASS** | All `results/` files are byte-identical to HEAD, including `baseline.json`. Repo `git diff --exit-code` → 0. |
| `entry_rule="limit"` | **PASS** | `_max_limit_adj` equals `sizing_v66.max_limit` on 400 random cases (selftest).<br>**Rule as modelled:**<br>- open > limit → no fill;<br>- open ≤ stop → no buy (C-8 amended / N-26);<br>- otherwise the fill is at the open with the shares sized at the signal close.<br>**Monthly breaker:** still applied at signal time, on the sizing base. |
| `capital_hkd`, `cash_yield`, `cash_reserve_pct` | **PASS** | **Formulas:** idle cash = capital + realised + interest − cost of open positions; interest accrues on the part above the reserve; equity is measured on capital.<br>**Selftest:** checks these formulas in closed form.<br>**Defaults:** reproduce the old equity curve (selftest + `baseline.json`). |
| Reproduction of the study's headline (12.5k / 10k base, 20% reserve) | **PASS** | Extra over T-bills, HK$/yr (full period), exact to the study's figures:<br>- webull0 **+16**;<br>- real35 **−178**;<br>- min1 **−537**.<br>At 100k / 80k: **−370 / −547**.<br>Max drawdown −3.09% / −3.49% / −4.23%.<br>T-bill index growth **19.1%** over 3.98 years (2023 4.93%, 2024 5.14%, 2025 4.13%), consistent with the 1–3 month bill rates of those years. |

**N-29 (MEDIUM; must land before V-1 is judged): the S4 fee gate tests the wrong entry rule.**
- **The problem:** `run_feecheck` simulates `AS_TRADED`, whose default is still `entry_rule="deviation"` (the old 1% re-compute). The live entry since 25 Nov is the limit rule (C-8 amended, N-15, N-26).
- **Per-trade net EV** [D] (`lab.simulate`, 10 bp/side + minimum per side):

| Minimum per side | Old rule: ALL / IS / OOS | **Live limit rule: ALL / IS / OOS** |
|---|---|---|
| US$0 | +0.806 / +0.778 / +0.734% | +0.651 / **+0.060** / +1.151% |
| **US$0.35 (N-9)** | +0.088 / +0.070 / +0.008% → "✅ S4 OK" | **−0.066 / −0.637 / +0.416% → S4 would trigger** (ALL ≤ 0) |
| US$1 | −1.245 / … | −1.397 / −1.931 / −0.951% |

- **What this means:** as shipped, the gate would **pass a fee level that, on the live rule, fails S4**.
- **The in-sample half:** under the live rule, in-sample EV is about zero even at a zero minimum fee (+0.060%). N-27's skipped entries cost in-sample edge; the OOS edge is higher, on 63 trades.
- **Fix:** `run_feecheck` (and any S4 reading) uses `entry_rule="limit"`, plus a selftest case asserting it. My re-verification is then diff-only.
- **Gating:** this does not gate the switch by itself, but **V-1 cannot be judged until it lands.**

## 2. Rulings on the income study (§8 Q1–Q4)

### R-1 (Q1): T-bills or money-market funds inside the C-7 (A) account

**Ruling: PERMITTED, as a cash equivalent and not as "another holding", under all of these conditions.**

1. **Allowed instruments only:**
   - US Treasury bills, or a T-bill ETF holding bills of ≤ 3 months (a BIL-type fund);
   - a **government** money-market fund (HKD or USD) investing in paper of ≤ 1 year.
   - **Not allowed:** bond funds beyond 1 year, credit, leveraged or derivative "income" ETFs, covered-call ETFs (for example 3416.HK), or anything with an equity leg.
   - This is the same definition I proposed for `cash_equivalents:` on 17 Nov, and it is how I already count the P-1 cash floor.
2. **The account must still meet C-6.** It must be a cash account or have margin disabled. A T-bill ETF in a margin account becomes buying power.
3. **It is not a swing position.** It is not recorded with `ledger fill`, takes no slot, and is outside the scanner. It **does** count in NLV for the C-7 check (NLV ≥ `account_hkd`), at market, with no borrowing.
4. **Settled-cash reserve: ≥ 30% of `account_hkd`** (HK$3,000 at a base of 10,000) held as **settled cash**, checked before every order.
   - The C-6 rule still applies in full: "settled cash ≥ the order".
   - **The T-bill ETF never counts as settled cash for that test.**
   - Top up the reserve by selling T-bills **on a day with no pending order**, and count the proceeds only once they have settled (US T+1).
   - **Never buy a swing position with unsettled proceeds.** In a cash account, a stop can sell the position the next day, which risks a good-faith violation.
5. **If the broker pays interest on uninvested cash** at close to the T-bill rate, leaving it as cash is preferred. It is simpler, always settled, and adds no extra trades.
6. **Withholding:** the Owner checks, in writing with the broker, whether T-bill ETF distributions to him are withheld at 30% or are exempt as qualified interest. Until then, read the study's 30% row as possible. This is **not verified**.

**Answer to the sub-question: the 20% reserve does NOT satisfy "settled cash must cover each order".**
- 20% of base = 2 slots × the 10% notional cap at entry: exactly enough for two full positions and nothing more.
- The first realised loss or fee leaves the second slot unfundable from settled cash.
- **30% is the minimum.** In my re-run it costs about **HK$48 a year** at 12.5k (HK$422 → HK$374, real35) [D]. That changes no conclusion.

### R-2 (Q2): does §2.3 count as "Tom's rerun" for other bases?

**No.** §2.3 is admissible evidence for such a review. It is not the review.
- It was run by the CEO, not Tom. C-7 names Tom's rerun and my review.
- It reports income versus T-bills. It does not report what the review needs for each base:
  - IS/OOS EV on the live rule;
  - the S4 check (N-29);
  - rejects;
  - overlap of the trade set with the reviewed 10,000 base;
  - per-name concentration.
- **§2.3 itself shows why each base needs its own review:** trading results jump from +311 (25k) to −144 (50k) to +692 (100k) HK$/yr. The study calls this path dependence.

**What is allowed without a review:** funding **more capital** while keeping `account_hkd` at **10,000**. C-7 forbids `account_hkd` above NLV, not below it. The extra money is reserve or T-bills under R-1.

**The conditions, in full:**

> **C-7 (A), as ruled 25 Nov and amended here.** A separate account (Webull or another broker) that is a **cash account or has margin disabled**, holding **nothing but the swing sleeve** (plus, from today, cash equivalents per R-1). It is funded with **≥ HK$12,500 of settled cash**.
> - Set `account_hkd` to **10,000** and set `switch_date` on the day you start.
> - Reconcile real NLV (no borrowed money) **monthly and after every withdrawal**. It must stay **≥ `account_hkd` (10,000)**.
> - A fall below 10,000 is a 20% drawdown: **stop new entries**; CRO de-risk review.
> - Any other `account_hkd`, higher or lower, needs Tom's rerun at that base **and** my review **before** the setting changes.
>
> **C-6.** Shown by a broker statement or a read-only pull (**a screenshot does not count**). Settled cash ≥ each order.

### R-3 (Q3): money the Owner needs for living costs

1. **Living-cost money for the next 12 months goes in this sleeve at 0%,** and in no risk asset at all [A: 12 months is my floor; the Owner may choose longer].
   - It belongs in cash, time deposits, T-bills or a government money-market fund, **in an account separate from any trading account**.
   - That money then earns the T-bill-like return directly, which is where the study shows the income comes from anyway.
2. **Cap: swing-sleeve capital ≤ 10% of LNW.**
   - With that cap, the sleeve's whole 20% drawdown budget costs at most **2% of LNW**.
   - At HK$12,500 the cap needs LNW ≥ **HK$125,000** [D].
   - **If LNW is below that, the answer is (B) shadow-only,** whatever V-1 shows.
3. **Withdrawals:**
   - none may be planned from the sleeve to pay living costs;
   - any withdrawal triggers the C-7 reconciliation;
   - a withdrawal that takes NLV below HK$12,500 or below `account_hkd` stops new entries.
4. **Firm blackouts bind V6.6 entries too, once it is live.** This is my restatement under L-009.
   - E-1 ("all sleeves", 4–10 Dec) applies to every V6.6 entry.
   - E-2 applies to V6.6 signals in Tier A/B names: NVDA, AMD, MU, INTC, AVGO, QCOM, META, MSFT, GOOGL, AMZN, PLTR.
   - This is moot today (SPY < 200-day MA; not switched).
5. **LNW is still undisclosed and is due by the 3 Dec close** (G-2 for AVGO).
   - At AVGO's last price of US$303.50, 2 shares fit the 6.6% band for LNW ≥ **US$9,200 (≈ HK$71,800)** [D: 607.00 ÷ 0.066].
   - Without LNW, my recommendation stands: exit AVGO before the 9 Dec print.

### R-4 (Q4): the Owner-facing text (§0, §4, §5)

The CEO's direction is right. These corrections are needed before the study goes to the Owner (L-009):

1. **§0 and §4, "Can it run long-term without hurting you? Probably yes … drawdowns about −2% to −5%".** These are **backtest** drawdowns. Add:
   - the binding limits are the **−10% monthly breaker (C-10)** and the **20% drawdown floor (C-7)**;
   - the real risks are operational: about 66 manual orders a year, and the S2 discipline.
   - And: "**it cannot run at all until C-6 is cured.** The Webull account is still a margin account."
2. **§0 "extra +16 / −178 / −537" and §6:** add the N-29 result. At the N-9 fee estimate, on the live rule, **per-trade EV is negative over the full period (−0.066%), and S4 would apply: no new entries at any cap.** V-1 is decisive, not just informative.
3. **§5 item 2 restates C-7 (A) incompletely.** It omits:
   - the monthly and post-withdrawal NLV reconciliation, and the < 10,000 stop;
   - the C-6 evidence standard (no screenshots);
   - settled cash ≥ each order.
   
   Quote the block in R-2 in full. Also add R-1 (cash equivalents allowed, 30% settled reserve) and R-3 (12-month living reserve outside; sleeve ≤ 10% of LNW).
4. **§5 item 2, preference:** state it as **CRO and CEO**. (B) shadow-only until **V-1 passes on the live rule (N-29)** **and** ≥ 6 months of ledger. If V-1 confirms a minimum of about US$0.35 a side or more, it is **S4: no trading at any cap**, not "(A) later".
5. **§4 "CRO-verified up to V6.6.5":** now V6.6.6 (this report).
   - **V-2 expectation for the Owner's PC:** **126** checks, fingerprint **`943960c97a9b`**, test hash `selftest.py=11191f51b203`.

## 3. Open items

**Owner:**
- LNW by the 3 Dec close;
- the C-6 cure (margin off or a cash account), shown by statement or read-only pull;
- choose (A) or (B) (CRO and CEO recommend (B));
- V-1 contract note;
- V-2 (126 / `943960c97a9b`);
- V-3;
- withholding and cash-interest answers from the broker (R-1.5, R-1.6);
- AVGO G-2 items (stop, record, no adds);
- 6160 items from my 26 Nov pre-review.

**CEO / Tom:**
- N-29 (feecheck on the live rule) before V-1 is judged;
- R-4 corrections to the study before it reaches the Owner.

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No V6.6 code and no agent of this firm can place an order.*

**For 腦大裝草:** `2026-11-26 · CRO V6.6.6 at cf41d84 / 943960c97a9b: PASS (lab-only diff; selftest 126 normal/-O; equivalence 85,120/0; ledger_check PASS; baseline identical; stamp match; study headline reproduced exactly). New N-29 MEDIUM: feecheck still uses the old entry rule; on the live limit rule at US$0.35+10bp ALL EV −0.066% (IS −0.637, OOS +0.416) → S4 would trigger; fix before V-1 is judged. Code side CLEAR subject to N-29. Income rulings: R-1 T-bill ETF/gov MMF ≤1y allowed in the C-7(A) cash account as cash equivalent, not a slot; settled reserve ≥30% of base (20% insufficient); R-2 §2.3 is not Tom's rerun; more capital at base 10,000 needs no review; R-3 12-month living money 0% in sleeve, sleeve ≤10% LNW (needs LNW ≥ HK$125k at 12.5k), E-1/E-2 bind V6.6 once live; R-4 §0/§4/§5 corrections incl. full C-7(A)/C-6 text and S4. CRO+CEO recommend (B) shadow-only. G-1 debit cured (USD +0.66), C-6 open, LNW due 3 Dec.`

---

## §3 V6.6.7 addendum (2026-11-26): N-29 fix, Tom F-2/F-3/F-8, and the order-duration ruling

**Scope:** `git diff cf41d84 a496ba4 -- strategy/v6.6`. V6.6.7 is `a496ba4`, fingerprint **`fae5fa5a7403`**; HEAD is `887d9c6`.
- **Code:** only `lab.py`, `selftest.py`, `config_v66.py` (version) and the stamp. Scanner, ledger, bot, sizing, signals, rules and guardrails are unchanged.
- **Also in the range:** README and checklist edits, plus `income_study.py` and its results files (not in `CORE_FILES`).

**Method:** scratch copy (`git archive a496ba4`); no broker call, no pip; only this file edited.

### 3.1 Verdict: **PASS** (one docs item, D-3)

| Check | Result [D] |
|---|---|
| Fingerprint / stamp | `fae5fa5a7403`; `pc_check.stamp()["match"]` True; `selftest.py` hash `d814e7469b69`. |
| selftest | **131/131**, normal and `-O`. |
| equivalence / ledger_check | 85,120 / 0; PASS. |
| `lab.py --mode baseline` | `baseline.json` and every rules result are byte-identical. Only the `income_*.csv` files differ, and those were regenerated at `887d9c6` by design. |
| **N-29** | **CLOSED.** `run_feecheck` uses `entry_rule="limit"` and `--tif`. At US$0.35 + 10 bp:<br>- **open:** ALL −0.066 / IS −0.637 / OOS +0.416% → **S4 ❌**;<br>- **day:** ALL +0.367 / IS −0.020 / OOS +0.501% → ✅.<br>Both reproduce the coordinator's figures exactly. |
| **F-2** reserve | Correct. The interest base is total − max(reserve, cost). At my 30% (HK$3,000), the reserve always covers two positions at cost (≤ HK$2,000). |
| **F-3** `entry_tif` | Correct as modelled.<br>- **Same-day stop:** checked on the fill day (`manage` runs on entry).<br>- **Floor under DAY:** buy at the open and exit at the open (1 case in 4 years).<br>- **Tom's "fill-day high" optimism is immaterial.** My probe ignores the fill-day high for intraday fills and requires the price to trade 1¢ **through** the limit. Result at US$0.35: ALL **+0.367** / IS **−0.020** / OOS **+0.499%**, unchanged to the third decimal. |
| **F-8** split factor | Correct: shares = signal-close shares × signal-date factor. |

**D-3 (LOW–MED): CLOSED by `9f40e35`, which landed during this check. README and checklist now cite `fae5fa5a7403` and 131. Originally:** the docs were one version behind. README L7, L64, L101 and L107, and checklist L90–91, still say **V6.6.6 / 126 checks / `943960c97a9b`**. The code is **V6.6.7 / 131 / `fae5fa5a7403`**. The README itself tells the Owner that a different fingerprint means "代碼唔係呢個版本 → 先問清楚" ("the code is not this version; ask first").

### 3.2 Ruling F-3: order duration

**What the DAY numbers rest on** [D, US$0.35, full period]:
- DAY adds **46 trades** that fill intraday at the limit after the open was above it. Those trades average **+1.005% net**.
- The trades common to both rules average **−0.012%**.
- **The whole difference between "S4 ❌" and "S4 ✅" comes from those 46 order-mechanics fills.** No forward evidence exists for them.

**Ruling: (b) DAY, approved for live use, but only with the protective stop attached to the entry order (OTO / bracket).**
- **The reason is control, not the fee result.** An attached stop makes both the C-8 floor and the C-9 stop **structural**: they go live the instant the buy fills, whether or not the Owner is awake.
  - (a) depends on the Owner watching every open at 21:30/22:30 HKT and cancelling correctly. That is a behavioural control the lab assumes is executed perfectly.
  - (a) does not enforce the floor by itself either. Any limit buy, including a limit-on-open, fills when the open is at or below the stop.
- **If the broker cannot attach a stop to the entry order, (b) is NOT approved.** The Owner must then use (a), watching the open and cancelling.
- **I do not accept choosing an order type because it passes the gate.** (b) is approved on the control argument. Its gate result is reported with the 46-trade caveat above.

**How the floor is enforced under (b):**
- **Structurally:** by the attached stop.
- **Procedurally:** a fill at or below the system stop is sold by that stop at once. The Owner records `fill open` and `fill close` the same day and sends me the S2.
- **My clearance:** I clear it on the broker record showing that the attached stop executed. Expect about one in four years.

**Which `--tif` the V-1 feecheck must use: the one the Owner will use live, declared before the contract note is read.**
- **`--tif day`** only if the Owner confirms in writing that his broker attaches a stop to a DAY limit buy (OTO/bracket) for US stocks in the C-6 account.
- **Otherwise `--tif open`.** At the N-9 estimate that is S4: no trading at any cap.
- **The S4 criterion is unchanged:** ALL > 0 and OOS > 0. It is not to be re-tuned after the fact.

**C-8, exact wording for the Owner under (b)** (it replaces the 25 Nov amended text):

> **C-8 (26 Nov: DAY order with attached stop).**
> - **Placing the order:** buy only with a **limit order, time-in-force DAY**, at or below the **限價上限 (maximum limit price)** printed by scanner ① or the bot, for the printed number of shares.
> - **Attached stop:** attach to the **same order** a **sell-stop at the system stop** (OTO / bracket), so it goes live the moment the buy fills. **Never place the buy without the attached stop.**
> - **No fill:** if the order is not filled by the close, it expires. Do not re-enter it the next day, do not raise the limit, do not add shares.
> - **Open at or below the system stop:** the buy may fill and the attached stop will sell at once. Record both the same day (`fill open`, `fill close`) and send the S2 to the CRO.
> - **E2 stop:** raise the broker stop each day to section ④'s stop (C-9). Never lower it.
> - **No attached stop at your broker:** (b) does not apply. Watch the open, and cancel if the open is above the limit or at or below the system stop. V-1 is then judged with `--tif open`.

**Code before (b) can be used (N-30, diff-only re-verification):**
- **What is wrong today:** scanner ① (`daily_scan_v66.py`), the bot plan and README still print the **(a)** wording: "開市價高過就唔買" ("open above the limit → don't buy") and "開市價 ≤ 系統止蝕 → 唔買" ("open ≤ system stop → don't buy").
- **What to print:** the C-8 text above.
- **Until it lands:** the printed (a) text governs, and V-1 is judged with `--tif open`.
- These files are in `CORE_FILES`, so the change moves the fingerprint.

**Recommendation unchanged: (B) shadow-only.** Even with DAY:
- at US$0.35, IS EV is −0.020% and the edge rests on 46 intraday fills;
- P(behind T-bills over 5 years) is 56% at real35;
- at 100k, DAY is negative out of sample (−1,318 / −1,521 HK$/yr).

V-1 (the real fee) and the declared order type decide. Size does not.

**For 腦大裝草:** `2026-11-26 · CRO V6.6.7 at a496ba4 / fae5fa5a7403: PASS (lab-only; selftest 131 normal/-O; equivalence 0/85,120; ledger_check PASS; baseline identical; stamp match). N-29 CLOSED (feecheck on live rule; open S4 ❌ / day ✅ at US$0.35). Tom F-3 day-fill optimism immaterial (probe: +0.367/−0.020/+0.499%). D-3 docs lag closed by 9f40e35. RULING F-3: (b) DAY approved ONLY with stop attached to the entry order (OTO/bracket) — control argument, not gate result; DAY's edge = 46 intraday fills (+1.005% vs −0.012% common). No attachable stop → (a), V-1 on --tif open. V-1 tif declared before the contract note; S4 criterion unchanged. C-8 reworded (above); N-30 scanner/bot/README text change required before (b) is used. Recommendation (B) shadow-only stands.`
