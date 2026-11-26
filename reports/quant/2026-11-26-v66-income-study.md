# Swing V6.6 as a long-term extra-income source: income study, 2026-11-26 (v2)

**Prepared by:** 皮褸黃 (CEO).
- **Tools:** lab **V6.6.7** (`a496ba4`, fingerprint `fae5fa5a7403`) and `strategy/v6.6/income_study.py` (`887d9c6`).
- **v2 incorporates:**
  - Tom's review (`reports/quant/2026-11-26-v66-income-study-review.md`: VALIDATED WITH CONCERNS, F-1 to F-8);
  - the CRO's rulings R-1 to R-4 and N-29 (`reports/risk/2026-11-26-v66-6-verification.md`).
- **CRO, V6.6.7:** PASS, with a ruling on order duration (§1.4).
- **Audit of the Owner-facing text:** PASS WITH CORRECTIONS, all applied (`reports/committee/2026-11-26-v66-income-audit.md`).

**The Owner's question (2026-11-26):** "evaluate is it possible to run it long-term — although it cannot beat the market I will take this as providing some extra return for my living."

*Research and decision support, not financial advice. Markets cannot be reliably predicted. Every number below comes from `income_study.py` output (`strategy/v6.6/results/income_*.csv`), from `lab.py --mode feecheck`, or from a cited file. Backtest figures are history (2022-11-30 → 2026-11-23), not forecasts.*

---

## 0. The answer

**The right comparison is not the S&P 500. It is the same money sitting in T-bills.** That alternative is almost riskless and needs no work. The system invests at most 20% of its sizing base (2 slots × 10% cap), so most of the account can earn T-bill interest anyway. The question is whether the trades add anything on top.

**Setting:** HK$12,500 capital, HK$10,000 sizing base, live entry rule. Settled cash is kept at 30% of the base (CRO R-1) and the rest sits in T-bills. HK$ per year, full period, out-of-sample (2025-01-01 →) in brackets.

| Fee scenario | Order type (§1.4) | Trading P&L | Interest | **Total** | All in T-bills instead | **System's extra over T-bills** |
|---|---|---|---|---|---|---|
| zero commission + 10 bp/side (`webull0`, assumption) | cancel at open | +169 | +456 | **+625** | +600 | **+26** (+269) |
| zero commission + 10 bp/side | DAY order | +295 | +471 | **+766** | +600 | **+166** (+344) |
| US$0.35 minimum + 10 bp (`real35`, CRO N-9 estimate) | cancel at open | −9 | +441 | **+432** | +600 | **−168** (+74) |
| US$0.35 minimum + 10 bp | DAY order | +104 | +455 | **+559** | +600 | **−41** (+137) |
| US$1 minimum + 10 bp (`min1`, stress) | cancel at open | −340 | +412 | **+72** | +600 | **−528** (−287) |
| US$1 minimum + 10 bp | DAY order | −250 | +424 | **+174** | +600 | **−426** (−247) |

**Plain words:**
- **Where the money comes from.** On HK$12,500, the account would have made about **HK$430–770 a year (HK$36–64 a month)** at the zero-commission and US$0.35 fee levels, across both order types. The lowest is US$0.35 with cancel-at-open, which fails S4; the highest is zero commission with DAY orders. **Most of it is the T-bill interest** (about HK$440–470). The trading itself added **−HK$9 to +HK$295 a year**, or −HK$340 at the US$1 stress fee.
- **Chance of doing worse than plain T-bills over five years** (bootstrap with uncertainty in the mean, §2.5): **28% to 75%**, depending on the fee and order type. That is roughly a coin flip, worse at the CRO's fee estimate. In no case is the average monthly excess statistically different from zero (t between −0.91 and +0.84).
- **The fee gate is decisive, not informative (CRO N-29).** At the CRO's US$0.35 fee estimate, with orders cancelled at the open as C-8 literally reads, the live rule's net expected value per trade is **−0.066%** over the full period. That is **S4: no new entries at any cap.** V-1, a real contract note, decides whether the system may be used at all.
- **Bigger capital does not reliably help** (§2.3). At HK$100,000 the result is −HK$191 to −HK$367 a year with cancel-at-open. With DAY orders it is +HK$401 to +HK$586 over the full period, but −HK$1,318 to −HK$1,521 out of sample.

**CRO and CEO reading:**
- **Can it run long-term without serious harm?** The backtest drawdowns are small: about −3% to −4% with interest at 12.5k, −11% at US$1 fees with no interest. But those are backtest figures. The **binding limits** are:
  - the **−10% monthly breaker** (C-10);
  - the **20% drawdown floor** (C-7: account value below HK$10,000 → stop new entries).

  The real risks are **operational**: about 66–70 manual orders a year, and S2 discipline. **It cannot run at all until C-6 is cured.** The Webull account is still a margin account.
- **Can it be counted on for living income?** **No.** The income comes from the T-bills. The system is a small add-on whose sign is unknown and which may not even pass its own fee gate.

---

## 1. Question and method

### 1.1 Benchmark
- **Primary: all capital in T-bills,** with the same tax assumption as the system's cash.
- **Secondary:** SPY buy-and-hold, shown for context only. The Owner has already accepted that the system will not beat the market. Over the period SPY returned 16.96% a year, with a −18.76% maximum drawdown.

### 1.2 Data
- **Stocks:** `strategy/v6.6/data/*.csv`, the 38-name universe plus SPY. Webull read-only daily bars, split- and dividend-adjusted, 2022-02-11 → 2026-11-23, the same files as every V6.6 backtest.
- **Test period:** 2022-11-30 (the first day SPY's 200-day MA exists) → 2026-11-23. Out-of-sample means 2025-01-01 onward.
- **T-bills:** `data/BIL.csv`, BIL (SPDR Bloomberg 1–3 Month T-Bill ETF), Webull read-only API pulled 2026-11-26, adjusted closes 2022-02-15 → 2026-11-25.
  - **Correction (derived data, estimate):** Webull failed to adjust 4 distributions. Those days fall 0.34%–0.40% in one day: 2024-10-01, 2024-11-01, 2024-12-02 and 2024-12-19.
  - `build_tbill()` flags any day more than 0.15 percentage points below its month's median (Tom F-6). It replaces each with the median of that month's other days. It flags exactly those 4 days, and Tom confirmed no smaller missed dates.
  - Corrected calendar-year returns: 2023 **4.94%**, 2024 **5.16%**, 2025 **4.15%**. Over the test period **4.49%** a year; out of sample **3.91%**.
- **Withholding scenario (not a fact).** An HK resident holding a US T-bill ETF may have **30%** of distributions withheld. Whether the broker applies the qualified-interest exemption is **not verified**. The scenario multiplies the daily T-bill return by 0.7, turning 4.49% into **3.12%** a year. It applies to both the system's cash and the benchmark.

### 1.3 What the lab models (V6.6.6 → V6.6.7)
- **Live entry:**
  - at the signal close, the share count and the **maximum limit price** are computed (`sizing_v66.max_limit`; the lab copy agrees in 363/363 random selftest cases);
  - next day, an open above the limit means **no fill**;
  - an open at or below the system stop means **no buy**;
  - otherwise the order fills **at the open** with the close-time share count. This matches C-8 as amended, N-15 and N-26 (Tom: PASS).
- **Capital and base are separate:** `capital_hkd` 12,500 and `account_hkd` 10,000.
- **Cash:**
  - settled cash is kept at **30% of the base**, the CRO R-1 minimum;
  - new positions are paid from it (Tom F-2), so the reserve does not need topping up while two positions are open;
  - everything else earns the T-bill return.
- **Rows labelled "all idle cash in T-bills"** (no reserve) show the upper bound. That arrangement is **not allowed** under R-1.

### 1.4 Order duration: a decision for the CRO (Tom F-3)
- **The problem.** C-8 says "open above the limit → don't buy" and "open at or below the stop → don't buy". A plain limit order does neither by itself. The Owner is in Hong Kong, and the US open is at 21:30 or 22:30 HKT.
  - **Cancel at the open** (C-8 literally) means being awake at the open to cancel.
  - **A DAY order** fills later in the day if the price dips to the limit. If the open gaps below the stop, it fills at once; the protective stop then takes the position out, costing the fees (modelled as buy and sell at the open).
- **The choice changes the answer** (fee gate, `lab.py --mode feecheck --tif …`; net EV per trade on the 10,000 base):

| Fees | Order type | Full period | In-sample | Out-of-sample | Gate (S4 / V-1) |
|---|---|---|---|---|---|
| 0 + 10 bp | cancel at open | +0.651% | +0.060% | +1.151% | pass |
| US$0.35 + 10 bp | cancel at open | **−0.066%** | −0.637% | +0.416% | **fail: S4** |
| 0 + 10 bp | DAY | +1.087% | +0.678% | +1.240% | pass |
| US$0.35 + 10 bp | DAY | +0.367% | −0.020% | +0.501% | pass |

The 0 + 10 bp DAY row is the CEO's feecheck run at `a496ba4` (`python lab.py --mode feecheck --fee-min 0 --fee-bp 10 --tif day`). It is not in committed output and was not reproduced by the CRO. The other three rows are CRO-reproduced (verification §1 and §3.1).

- With a DAY order, the full-period skip count falls from 43 to 7 (`income_scenarios.csv`). The trade path also changes, so these are not the same 43 signals. Holding the cancel-at-open trades fixed, Tom measured 25 of the 43 skips filling intraday at the limit.
- **Caveat on the DAY rows:** on an intraday fill, the lab's E2 trailing-stop update uses the whole day's high, including the part before the fill. That is slightly optimistic.
- **CRO ruling (F-3, 26 Nov):**
  - **(b) DAY is approved, but only with the protective stop attached to the entry order** (OTO / bracket). It is approved on control grounds, not because it passes the fee gate. With an attached stop, the floor and the stop are live the moment the buy fills, awake or not.
  - **If the broker cannot attach a stop to the entry order, (b) is not approved.** The Owner must then watch the open and cancel, which is option (a).
  - **V-1 uses the order type the Owner will actually use, declared in writing before the contract note is read.** `--tif day` only with written confirmation that the broker attaches a stop to a DAY limit buy for US stocks in the C-6 account; otherwise `--tif open`, which at the US$0.35 estimate means S4.
  - **The S4 test is not re-tuned after the fact:** ALL > 0 and OOS > 0.
  - **Before (b) can be used, N-30 must land:** scanner ①, the bot plan and README must print the CRO's 26 Nov C-8 wording (the CRO's 26 Nov C-8, quoted below). Until then, the printed cancel-at-open text governs, **and V-1 is judged with `--tif open`** (CRO §3.2).

    > **C-8 (26 Nov: DAY order with attached stop).**
    > - **Placing the order:** buy only with a **limit order, time-in-force DAY**, at or below the **限價上限 (maximum limit price)** printed by scanner ① or the bot, for the printed number of shares.
    > - **Attached stop:** attach to the **same order** a **sell-stop at the system stop** (OTO / bracket), so it goes live the moment the buy fills. **Never place the buy without the attached stop.**
    > - **No fill:** if the order is not filled by the close, it expires. Do not re-enter it the next day, do not raise the limit, do not add shares.
    > - **Open at or below the system stop:** the buy may fill and the attached stop will sell at once. Record both the same day (`fill open`, `fill close`) and send the S2 to the CRO.
    > - **E2 stop:** raise the broker stop each day to section ④'s stop (C-9). Never lower it.
    > - **No attached stop at your broker:** (b) does not apply. Watch the open, and cancel if the open is above the limit or at or below the system stop. V-1 is then judged with `--tif open`.
  - **The CRO's caution:** the whole difference between failing and passing at US$0.35 comes from 46 trades that fill intraday at the limit after opening above it. They average +1.005% net, while the trades both order types share average −0.012%. There is no live evidence for those 46 fills.

### 1.5 Not modelled
- **Lab-vs-live gaps (Tom F-7):**
  - the lab has **no earnings guard** (the live scanner blocks 0–5 days before earnings);
  - it does **not** model the N-11 hold (no new entries while an S2 is unexplained);
  - it **enforces** the −10% monthly breaker, which is manual in live use (C-10).
- **Other costs and frictions:**
  - the broker's own interest on uninvested cash (unknown);
  - FX cost of converting HKD to USD;
  - slippage beyond 10 bp a side;
  - missed or late manual orders;
  - the Owner's time;
  - any tax other than the withholding scenario.
- **Fees are the big unknown.** `webull0` is an assumption; `real35` is the CRO's estimate. **V-1 is outstanding.**

---

## 2. Results

### 2.1 HK$12,500 / base 10,000, live entry, cancel-at-open: full period (out-of-sample in brackets)

| Fees | Cash | CAGR % | Extra vs T-bills, %/yr | Extra HK$/yr | Max DD % | Worst month % | Months up % |
|---|---|---|---|---|---|---|---|
| webull0 | no interest | 1.33 (2.92) | −3.16 (−0.99) | −431 (−127) | −3.83 | −1.17 | 53 |
| webull0 | **30% settled cash, rest T-bills (R-1)** | 4.67 (5.82) | +0.18 (+1.91) | **+26** (+249) | −3.10 | −0.79 | 67 |
| webull0 | all idle cash in T-bills (not allowed) | 5.27 (6.34) | +0.78 (+2.43) | +112 (+318) | −2.94 | −0.74 | 67 |
| webull0 | 30% reserve, 30% withholding | 3.64 (4.93) | +0.52 (+2.20) | +71 (+285) | −3.32 | −0.91 | 65 |
| real35 | no interest | −0.07 (1.49) | −4.56 (−2.42) | −609 (−310) | −4.86 | −1.35 | 43 |
| real35 | **30% settled cash, rest T-bills (R-1)** | 3.29 (4.46) | −1.20 (+0.55) | **−168** (+71) | −3.49 | −0.95 | 65 |
| real35 | all idle cash in T-bills (not allowed) | 3.91 (5.02) | −0.58 (+1.10) | −82 (+144) | −3.33 | −0.89 | 67 |
| real35 | 30% reserve, 30% withholding | 2.25 (3.54) | −0.87 (+0.82) | −117 (+105) | −3.71 | −1.07 | 61 |
| min1 | no interest | −2.84 (−1.47) | −7.33 (−5.38) | −940 (−680) | −10.98 | −1.70 | 35 |
| min1 | **30% settled cash, rest T-bills (R-1)** | 0.57 (1.65) | −3.92 (−2.26) | **−528** (−290) | −4.23 | −1.28 | 43 |

**DAY-order rows** (same layout, 30% reserve): webull0 5.63% (6.28), extra **+166** (+310); real35 4.20% (4.89), extra **−41** (+127); min1 1.36% (2.02), extra **−426** (−243).

**Notes:**
- Cancel-at-open: 130 closed trades over 4 years (about 33 a year), 63 of them out of sample. At least one position was open on 88% of trading days. Over the full period, 43 signals were skipped because the open was above the limit, and 1 because the open was at or below the stop.
- DAY orders: 139 trades, 7 skips.
- The "Extra HK$/yr" column is scaled to the starting HK$12,500. The §0 table is in actual HK$ over each window, so out-of-sample values can differ by a few HK$.

### 2.2 The hurdle: interest given up by running the system

The split into trading and interest is exact: sizing uses the fixed HK$10,000 base, so the trades are identical with or without interest.
- At 12.5k with the 30% reserve, running the system gives up about **HK$130–160 a year** of interest (`income_decomposition.csv`, "少收咗嘅利息").
- At about 33–35 trades a year, the trades must net roughly **HK$4–5 (≈ US$0.5–0.6) per trade** just to match T-bills.
- At the CRO's US$0.35 fee estimate, the trades netted **−HK$9 a year** (cancel at open) or **+HK$104** (DAY) over the full period.

### 2.3 Bigger capital, same rules (30% settled cash, rest in T-bills). Extra over T-bills, HK$/yr, full period (out-of-sample)

| Capital / base (HK$) | webull0, cancel at open | real35, cancel at open | webull0, DAY | real35, DAY |
|---|---|---|---|---|
| 12,500 / 10,000 | +26 (+269) | −168 (+74) | +166 (+344) | −41 (+137) |
| 25,000 / 20,000 | +237 (+454) | +43 (+246) | +286 (+615) | +90 (+407) |
| 50,000 / 40,000 | −551 (−353) | −739 (−540) | −312 (−186) | −500 (−376) |
| 100,000 / 80,000 | −191 (−512) | −367 (−691) | +586 (−1,318) | +401 (−1,521) |

**Reading (corrected per Tom F-4):**
- **A larger base admits pricier names, so it is a different trade set,** not a scaled-up version of the 12.5k account.
  - At a HK$10,000 base, only names under about US$128 can be bought.
  - At bases of 20k / 40k / 80k, only 31 / 18 / 11 trades are shared with the 10k run.
  - The trades in names above US$128 earned a steady +1.45% to +1.70% of base a year in Tom's run (real35, no interest).
  - The swings in the totals come from the cheaper remainder, where slot competition reshuffles which trades happen.
- **Do not read this as a case for a bigger base.** The figures are in-sample history, and the 100k DAY row flips from +586 to −1,318 out of sample.
- **Under C-7 / R-2, any base other than 10,000 needs Tom's rerun and the CRO's review before the setting changes.** This table is evidence for such a review, not the review.
- **Allowed without review:** adding more capital while keeping `account_hkd` at 10,000. The extra money sits in the reserve or in T-bills (R-1, R-2).

### 2.4 Calendar years, 12.5k, 30% reserve: extra over T-bills, percentage points (`results/income_yearly.csv`)

| Year | real35, cancel at open | webull0, cancel at open | real35, DAY | webull0, DAY | All T-bills % | SPY % |
|---|---|---|---|---|---|---|
| 2022 (from 30 Nov) | −1.08 | −0.95 | −1.08 | −0.95 | 0.36 | −5.76 |
| 2023 | **−4.00** | −2.55 | −1.86 | −0.28 | 4.94 | 26.18 |
| 2024 | −0.58 | +0.75 | +0.06 | +1.44 | 5.16 | 24.89 |
| 2025 | +1.66 | +3.14 | +2.62 | +4.11 | 4.15 | 17.72 |
| 2026 (to 23 Nov) | −0.68 | +0.42 | −0.80 | +0.34 | 3.26 | 6.75 |

- Behind T-bills in **4 of 5** periods at real35 with cancel-at-open, and **3 of 5** with DAY orders. At webull0, 2 of 5 for either order type.
- 2023 was the worst year in every variant. 2025 carries most of the out-of-sample result.

### 2.5 How likely is it to trail T-bills? (`results/income_bootstrap.csv`)

**Method:**
- circular block bootstrap of the 49 monthly excess returns vs T-bills, 3-month blocks, wrapped end to end (Tom F-1), 5,000 paths;
- the right-hand columns also add uncertainty about the true mean (a per-path shift drawn from N(0, sd/√49));
- it assumes the next five years look like a reshuffle of the last four, which is a strong assumption.

| Scenario | P(behind T-bills), 1 yr | 3 yrs | 5 yrs | 5 yrs + uncertainty in the mean | Median 5-yr extra (with mean uncertainty) | t (monthly mean) |
|---|---|---|---|---|---|---|
| 12.5k, real35, cancel at open | 67% | 77% | 84% | **75%** | −5.6% | −0.91 |
| 12.5k, webull0, cancel at open | 48% | 45% | 44% | **46%** | +0.8% | +0.17 |
| 12.5k, real35, DAY | 54% | 56% | 59% | **56%** | −1.4% | −0.17 |
| 12.5k, webull0, DAY | 35% | 25% | 19% | **28%** | +5.5% | +0.84 |
| 100k, real35, cancel at open | 53% | 57% | 59% | **57%** | −1.5% | −0.21 |

**In every case the average monthly excess is a small fraction of its noise** (standard deviation about 0.7% a month).

### 2.6 Live entry rule vs the old backtest entry (12.5k, webull0, no interest)
- **Old 1% deviation rule:** 1.78% CAGR on HK$12,500 (≈ 2.2% on the HK$10,000 base, matching the V6.6.5 release note), 135 trades.
- **Live rule, cancel at open:** 1.33%, 130 trades, 43 skips.
- **Live rule, DAY order:** 2.28%, 139 trades.
- The Owner's real results should be compared with the live-rule lines, not the old ≈ 2.2%.

### 2.7 Research only, NOT approved: more slots at HK$100,000
`MAX_POSITIONS = 2` is a locked parameter. These rows are a hypothesis for a possible future review by Tom and the CRO, not a proposal. Settings: real35, cancel at open, reserve = slots × 10% + 10%.

| | Trading HK$/yr | Extra vs T-bills, full (out-of-sample) | Max DD % |
|---|---|---|---|
| 3 slots, 40% reserve | +1,718 | +289 (+1,048) | −3.41 |
| 4 slots, 50% reserve | +2,462 | +724 (+967) | −4.17 |

---

## 3. Why the system struggles to beat T-bills

1. **By design it is mostly in cash.** At 12.5k/real35 with whole-share sizing:
   - the average position is **7.9% of the base**, not 10%;
   - days with 0 / 1 / 2 positions open: **12% / 30% / 58%**;
   - on average about **12% of the base (≈ 9% of capital)** is in trades.

   When SPY is below its 200-day MA, nothing is invested. As of the 23 Nov close (`data/SPY.csv`), it is below.
2. **Its edge per trade is small.** The V6.6.5 release note reports net EV of about +1.85% per E1 trade and −1.03% per E2 trade in the 2-slot book. Neither is statistically distinguishable from zero at this size.
3. **Fees eat it.** On the live rule with cancel-at-open, net EV per trade is +0.651% at zero commission and −0.066% at US$0.35 (§1.4).
4. **The settled-cash reserve and the money in trades earn nothing.** That is the HK$130–160 a year hurdle at 12.5k (§2.2).

If T-bill rates fall, the hurdle falls with them. The interest income falls too, though, and the trading result does not improve.

---

## 4. Can it run long-term? Assessment (CEO; CRO rulings applied)

**What supports running it:**
- **Tested code.** The rules are fixed, fingerprinted and tested:
  - selftest 131 checks;
  - equivalence 0/85,120;
  - ledger check;
  - CRO-verified through V6.6.7 (`reports/risk/2026-11-26-v66-6-verification.md` §1, §3).
- **Small backtest drawdowns at this sizing:** about −3% to −4% with interest, worst month about −1%; −11% at US$1 fees with no interest.
  - These are backtest figures. **The binding limits are the −10% monthly breaker (C-10) and the 20% drawdown floor (C-7).**
- The SPY 200-day filter keeps it out of the market in weak regimes.

**What argues against counting on it:**
- The extra return over T-bills is **indistinguishable from zero** (t between −0.91 and +0.84).
- **At the CRO's fee estimate it may fail its own gate.** With cancel-at-open orders, S4 applies (N-29). The answer depends on V-1 and on the order type, neither of which is settled.
- **No forward evidence yet.** The firm's own gate: ≥ 30 closed E2 trading-path signals **and** ≥ 6 months of ledger before any forward review, and no cap-level return comparison before 100 trades.
- **Operational load:**
  - about 66–70 manual limit orders a year, plus protective stops;
  - the S2 discipline;
  - with cancel-at-open, being awake at the US open.

  The Owner places every order; no agent can (CLAUDE.md rule 1).
- **Unresolved costs:**
  - withholding on the T-bill side, worth about 1.4 percentage points of yield in the 30% scenario;
  - the broker's interest on cash;
  - HKD/USD conversion.
- **Alpha decay:** short-horizon technical edges tend to weaken. This is a general observation, not measured here.
- **It cannot run at all until C-6 is cured.** The Webull account is still a margin account (2026-11-26 read-only pull).

**Verdict:**
- As a small sleeve that **might** add a little and is unlikely to do serious harm, it can run long-term only once **all** of these hold:
  - C-6 is cured;
  - V-1 passes on the live rule, with the order type declared in advance (`--tif open` until N-30 lands);
  - the sleeve is ≤ 10% of LNW (LNW ≥ HK$125,000 at HK$12,500; otherwise (B), whatever V-1 shows; CRO R-3);
  - the other README switch conditions close;
  - the Owner chooses (A).

  The CRO and CEO still recommend (B).
- As an **income source for living costs**, it does **not** qualify. The income is the T-bill interest. The system's expected addition is about zero, and the chance of trailing plain T-bills over five years is 28–75%, depending on fee and order type.

---

## 5. What the Owner can do (options, not advice)

### 5.1 For the income itself (CRO R-3, quoted from `reports/risk/2026-11-26-v66-6-verification.md`)
- "Living-cost money for the next 12 months goes in this sleeve at 0%, and in no risk asset at all." It belongs in cash, time deposits, T-bills or a government money-market fund, in an account separate from any trading account. "That money then earns the T-bill-like return directly, which is where the study shows the income comes from anyway."
- **Questions for the broker, in writing:**
  - whether US T-bill ETF distributions are withheld at 30% or exempt as qualified interest (R-1.6);
  - whether uninvested cash earns interest (R-1.5: if it earns close to the T-bill rate, leaving it as cash is preferred);
  - which HK-listed USD/HKD government money-market funds or time deposits are available, and at what yield. **Not verified this session;** no figures are given.

### 5.2 For the system: the CRO's conditions, in full

> **C-7 (A), as ruled 25 Nov and amended here.** A separate account (Webull or another broker) that is a **cash account or has margin disabled**, holding **nothing but the swing sleeve** (plus, from today, cash equivalents per R-1). It is funded with **≥ HK$12,500 of settled cash**.
> - Set `account_hkd` to **10,000** and set `switch_date` on the day you start.
> - Reconcile real NLV (no borrowed money) **monthly and after every withdrawal**. It must stay **≥ `account_hkd` (10,000)**.
> - A fall below 10,000 is a 20% drawdown: **stop new entries**; CRO de-risk review.
> - Any other `account_hkd`, higher or lower, needs Tom's rerun at that base **and** my review **before** the setting changes.
>
> **C-6.** Shown by a broker statement or a read-only pull (**a screenshot does not count**). Settled cash ≥ each order.

**R-1, cash equivalents inside that account:**
- **Allowed:** US T-bills, a T-bill ETF holding bills of ≤ 3 months, or a government money-market fund (≤ 1 year paper).
- **Not allowed:** bond funds beyond 1 year, credit, leveraged or "income" ETFs, covered-call ETFs (for example 3416.HK), or anything with an equity leg.
- **They are not swing positions:** no `ledger fill`, no slot. They do count in NLV.
- **Keep ≥ 30% of `account_hkd` (HK$3,000) as settled cash,** checked before every order. The T-bill ETF never counts as settled cash.
- **Top-ups:** top up only on a day with no pending order, and count the proceeds only once settled (T+1). **Never buy with unsettled proceeds.**

**R-3, size and withdrawals:**
- **Sleeve capital ≤ 10% of liquid net worth (LNW).** At HK$12,500 that needs LNW ≥ HK$125,000. **If LNW is below that, the answer is (B) shadow-only, whatever V-1 shows.**
- **Withdrawals:**
  - none may be planned from the sleeve to pay living costs;
  - any withdrawal triggers the C-7 reconciliation;
  - one that takes NLV below HK$12,500 or below `account_hkd` stops new entries.
- **Blackouts:** firm blackouts (E-1 4–10 Dec; E-2 for Tier A/B names) bind V6.6 entries once it is live.

**The choice:**
- **(A)** above;
- **(B) shadow-only:** scanner and signal ledger, no fills, until (A) is met.

**CRO and CEO recommendation: (B)** until **V-1 passes on the live rule (N-29)** **and** there are ≥ 6 months of ledger. If V-1 confirms a minimum fee of about US$0.35 a side or more, **that is S4: no trading at any cap** (with `--tif open`; with a DAY order and an attached stop, the US$0.35 estimate passes, subject to the 46-trade caveat below), not "(A) later" (CRO R-4.4).
- The one exception the CRO allows for the order type: a DAY limit with an attached stop, if the broker supports it in writing and after N-30 (§1.4).
- Even then the CRO still recommends (B): at US$0.35, in-sample EV is −0.020% and the edge rests on the 46 intraday fills.
- The choice remains the Owner's.

### 5.3 Not recommended
Raising slots or the base to chase income. The §2.7 rows are unapproved research, and §2.3 shows that size alone does not reliably help.

## 6. What would change this verdict
- **V-1:** a real Webull contract note. About zero commission with spread near 10 bp would put the 12.5k result near the `webull0` rows: +26 to +166 HK$ a year over T-bills, with a 28–46% chance of trailing over 5 years. A minimum of about US$0.35 or more with cancel-at-open is S4.
- **The Owner's written answer on attached stops** (OTO / bracket for a DAY limit buy). It decides which `--tif` V-1 uses (§1.4).
- **Forward ledger:** ≥ 30 closed E2 trades and ≥ 6 months, with net EV per trade clearly above the ≈ HK$4–5 hurdle.
- **A CRO-approved rule change** (slots, cap or base). Each needs Tom's rerun and CRO review (C-7, R-2).

## 7. Reproduce

```
cd strategy/v6.6
python income_study.py                                          # needs data/*.csv and data/BIL.csv; builds data/TBILL.csv
python lab.py --mode feecheck --fee-min 0.35 --fee-bp 10 --tif open   # --tif day only after N-30 lands and the broker confirms an attached stop in writing
```

**Lab V6.6.7 (fingerprint `fae5fa5a7403`):**
- `entry_rule`;
- `entry_tif`;
- `capital_hkd`;
- `cash_yield`;
- `cash_reserve_pct` (positions are paid from the reserve);
- the share count uses the signal-date split factor.

**Defaults are unchanged:** `results/baseline.json` and every tracked results file are byte-identical. Selftest has 131 checks (also under `-O`); 9 mutants were each caught.

## 8. Questions answered by the CRO (`reports/risk/2026-11-26-v66-6-verification.md`)
- **R-1:** T-bills or government money-market funds are allowed in the C-7 (A) account as cash equivalents, with a 30% settled-cash reserve. The 20% reserve is not enough.
- **R-2:** §2.3 is evidence for a review at another base, not the review itself.
- **R-3:** 12 months of living money stays outside any risk asset; sleeve ≤ 10% of LNW; no planned withdrawals.
- **R-4:** corrections to this text. Applied in v2: §0, §4, §5 and §6.
- **N-29:** the fee gate now uses the live rule (V6.6.7).

## 9. Reviews
- **Tom (2026-11-26):** VALIDATED WITH CONCERNS. F-1 to F-8 are applied in V6.6.7 and v2 (F-1 bootstrap, F-2 reserve, F-3 order type, F-4 wording, F-5 counts, F-6 threshold, F-7 gaps, F-8 split factor).
- **John, CRO (2026-11-26):** V6.6.6 PASS with N-29; R-1 to R-4. **V6.6.7 PASS** (N-29 closed). F-3 ruling: DAY only with an attached stop, else cancel-at-open; N-30 before DAY can be used; recommendation still (B).
- **Ai 管理層 (2026-11-26):** PASS WITH CORRECTIONS; no HIGH findings. S-1 to S-7 applied here; K-1 to K-8 in the checklist; RM-1 to RM-4 in the README (`reports/committee/2026-11-26-v66-income-audit.md`).
