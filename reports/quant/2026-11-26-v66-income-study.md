# Swing V6.6 as a long-term extra-income source: income study, 2026-11-26

**Prepared by:** 皮褸黃 (CEO), using lab V6.6.6 (`strategy/v6.6/income_study.py`, commit after cf41d84).

**Reviews:** Tom (backtest fidelity), John (CRO), Ai 管理層 (audit of the Owner-facing text). Their verdicts are appended in §9 when they arrive. **Until the CRO has ruled, nothing here is a recommendation.**

**The Owner's question (2026-11-26):** "evaluate is it possible to run it long-term — although it cannot beat the market I will take this as providing some extra return for my living."

*Research and decision support, not financial advice. Markets cannot be reliably predicted. Every number below comes from `income_study.py` output (`strategy/v6.6/results/income_*.csv`) or a cited file. Backtest figures are history, not forecasts.*

---

## 0. The answer in one table

**The right comparison is not the S&P 500. It is the same money sitting in T-bills.** That alternative is almost riskless and needs no work. The system uses at most 20% of its sizing base (2 slots × 10% cap), so the rest of the account can earn T-bill interest. The question is whether the trades add anything on top.

**Setting:** HK$12,500 capital and a HK$10,000 sizing base (CRO C-7 (A)), live entry rule, 20% of the base kept as cash, the rest in T-bills. Full period 2022-11-30 → 2026-11-23 (4.0 years). HK$ per year.

| Fee scenario | Trading P&L | Interest on idle cash | **Total** | All in T-bills instead | **System's extra over T-bills** |
|---|---|---|---|---|---|
| `webull0`: zero commission + 10 bp/side (assumption) | +169 | +447 | **+616** | +600 | **+16** |
| `real35`: US$0.35 minimum + 10 bp/side (CRO N-9 estimate) | −9 | +432 | **+422** | +600 | **−178** |
| `min1`: US$1 minimum + 10 bp/side (stress) | −340 | +403 | **+63** | +600 | **−537** |

Same setting, **out-of-sample only** (2025-01-01 → 2026-11-23): the extra over T-bills is **+268 / +73 / −289** HK$ a year (`results/income_decomposition.csv`).

**Plain words:**
- On HK$12,500, the account would have made about **HK$420–620 a year, about HK$35–50 a month**. Almost all of it came from the T-bills.
- The trading itself added between **−HK$340 and +HK$170 a year** over four years, depending on fees nobody has yet confirmed (V-1 is still open).
- Over five years, the bootstrap puts the chance that the system leaves the account **behind** plain T-bills at:
  - **≈ 79%** at the CRO's US$0.35 fee estimate;
  - **≈ 39%** at zero commission (§2.5).
- **Scaling up does not fix this.** At HK$100,000 (base 80,000), T-bills alone made ≈ HK$4,800 a year. System plus T-bills made HK$4,250–4,430, so it **trailed by HK$370–550 a year**, and by more out of sample.

**CEO reading (pending CRO):**
- **Can it run long-term without hurting you?** Probably yes. It is small, capped and slow: backtest drawdowns with interest of about −2% to −5% at these sizes, worst month about −1% to −2%.
- **Can it be counted on for living income?** **No.** The income comes from the T-bills. The system is a small add-on whose sign is still unknown.

---

## 1. Question and method

### 1.1 Benchmark
- **Primary: all capital in T-bills,** with the same tax assumption as the system's cash.
- **Secondary:** SPY buy-and-hold, shown for context only. The Owner has already accepted that the system will not beat the market.

### 1.2 Data
- **Stocks:** `strategy/v6.6/data/*.csv`, the 38-name universe plus SPY. Webull read-only daily bars, split- and dividend-adjusted, 2022-02-11 → 2026-11-23. These are the same files as every V6.6 backtest.
- **Test period:** 2022-11-30 (the first day SPY's 200-day MA exists) → 2026-11-23. Out-of-sample means 2025-01-01 onward, the split used since V6.6.0.
- **T-bills:** `data/BIL.csv`, BIL (SPDR Bloomberg 1–3 Month T-Bill ETF), Webull read-only API pulled 2026-11-26, adjusted closes 2022-02-15 → 2026-11-25.
  - **Correction (derived data, estimate):** Webull failed to adjust 4 distributions. Those days show one-day drops of −0.34% to −0.40% on 2024-10-01, 2024-11-01, 2024-12-02 and 2024-12-19, which a T-bill fund does not do.
  - `build_tbill()` replaces any daily return below −0.25% with the median of that month's other days. The rebuilt index matches the one used in the CEO's working file exactly (max difference 0.0).
  - Corrected calendar-year returns: 2023 **4.94%**, 2024 **5.16%**, 2025 **4.15%**.
  - Over the test period the T-bill index compounds at **4.49%** a year; out of sample, 3.91%.
- **Withholding scenario (not a fact).** An HK resident holding a US T-bill ETF may have **30%** of distributions withheld. Whether the broker applies the qualified-interest-income exemption has **not been verified**. The scenario multiplies the daily T-bill return by 0.7. That turns 4.49% into **3.12%**, both for the system's cash and for the T-bill benchmark.

### 1.3 What the lab now models (V6.6.6, `entry_rule="limit"`)
The live rules (C-8 amended, N-15, N-26):
- At the signal close, compute the share count and the **maximum limit price** (`sizing_v66.max_limit`; the lab copy agrees in 363/363 random cases in the selftest).
- Next day:
  - open above the limit → **no fill**;
  - open at or below the system stop → **don't buy**;
  - otherwise fill **at the open**, with the share count computed at the close.
- **Capital and base are separate:** `capital_hkd` 12,500 and `account_hkd` 10,000.
- **Interest is paid on cash above the reserve:** cash = capital + realised P&L + interest − cost of open positions.

**Why a 20% reserve.** C-7 (A) requires settled cash to cover each order. A T-bill ETF sold today settles the next business day. Keeping 2 slots × 10% of the base in cash lets a next-open buy be paid with settled cash. Positions are then refilled from T-bills, so the reserve stays at 20%.
- Rows with "all idle cash in T-bills" (0% reserve) show the upper bound.
- Whether **any** T-bill holding is allowed in the swing account is a CRO question (§8). C-7 (A) says the account holds "nothing but the swing sleeve".

### 1.4 Not modelled
- the broker's own interest on uninvested cash (unknown);
- FX cost of converting HKD to USD;
- slippage beyond 10 bp/side;
- missed or late manual orders;
- the Owner's time;
- any tax other than the withholding scenario.

**Fees are the big unknown:** `webull0` is an assumption and `real35` the CRO's estimate. V-1, a real Webull contract note, is still outstanding.

---

## 2. Results

### 2.1 HK$12,500 / base 10,000, live entry: full period (out-of-sample in brackets)

| Fees | Cash | CAGR % | Extra vs T-bills, %/yr | Extra HK$/yr | Max DD % | Worst month % | Months up % |
|---|---|---|---|---|---|---|---|
| webull0 | no interest | 1.33 (2.92) | −3.16 (−0.99) | −431 (−127) | −3.83 | −1.17 | 53 |
| webull0 | 20% reserve, rest T-bills | 4.60 (5.82) | +0.11 (+1.91) | +16 (+249) | −3.09 | −0.80 | 67 |
| webull0 | all idle cash in T-bills | 5.27 (6.34) | +0.78 (+2.43) | +112 (+318) | −2.94 | −0.74 | 67 |
| webull0 | 20% reserve, 30% withholding | 3.59 (4.92) | +0.47 (+2.20) | +65 (+284) | −3.31 | −0.91 | 65 |
| real35 | no interest | −0.07 (1.49) | −4.56 (−2.42) | −609 (−310) | −4.86 | −1.35 | 43 |
| real35 | 20% reserve, rest T-bills | 3.22 (4.45) | −1.27 (+0.54) | −178 (+70) | −3.49 | −0.96 | 65 |
| real35 | all idle cash in T-bills | 3.91 (5.02) | −0.58 (+1.10) | −82 (+144) | −3.33 | −0.89 | 67 |
| real35 | 20% reserve, 30% withholding | 2.21 (3.53) | −0.92 (+0.81) | −124 (+104) | −3.71 | −1.08 | 61 |
| min1 | no interest | −2.84 (−1.47) | −7.33 (−5.38) | −940 (−680) | −10.98 | −1.70 | 35 |
| min1 | 20% reserve, rest T-bills | 0.50 (1.63) | −3.99 (−2.28) | −537 (−292) | −4.23 | −1.29 | 43 |
| min1 | all idle cash in T-bills | 1.25 (2.29) | −3.24 (−1.62) | −441 (−208) | −4.07 | −1.20 | 45 |
| min1 | 20% reserve, 30% withholding | −0.53 (0.67) | −3.65 (−2.05) | −475 (−260) | −5.38 | −1.42 | 43 |

**Notes:**
- 130 closed trades over 4 years, about 33 a year; 63 out of sample.
- At least one position was open on 88% of trading days.
- The live limit rule skipped 43 signals (open above the limit) and 1 (open at or below the stop).
- "Extra HK$/yr" is scaled to the starting HK$12,500 in both periods.
- The withholding rows are compared with T-bills **after** the same 30% withholding.

### 2.2 Where the money comes from (HK$/yr; `results/income_decomposition.csv`)

Splitting into "trades" and "interest" is exact. Position sizing uses the fixed HK$10,000 base, so the trades are identical with or without interest.

| 12.5k, 20% reserve | Trading | Interest earned | All-T-bill alternative | Interest given up | Extra |
|---|---|---|---|---|---|
| webull0, full period | +169 | +447 | +600 | 153 | **+16** |
| webull0, out-of-sample | +370 | +433 | +535 | 102 | **+268** |
| real35, full period | −9 | +432 | +600 | 168 | **−178** |
| real35, out-of-sample | +182 | +411 | +520 | 109 | **+73** |

**The hurdle.** Running the system means giving up about **HK$150–170 a year** of interest at this size, from the reserve plus the money in positions. The trades must earn more than that just to break even with T-bills.
- At about 33 trades a year, that is roughly **HK$5 (≈ US$0.60) of net profit per trade** before the system adds anything.
- At the CRO's US$0.35 fee estimate, the trades netted **−HK$9 a year** over the full period.

The decomposition is in actual HK$ over each window. Its out-of-sample "extra" can differ by a few HK$ from §2.1, which is scaled to the starting capital.

### 2.3 Bigger capital, same rules (20% reserve, rest in T-bills)

| Capital / base (HK$) | Fees | Trading HK$/yr | Interest HK$/yr | All-T-bill HK$/yr | **Extra HK$/yr, full (out-of-sample)** | Max DD % |
|---|---|---|---|---|---|---|
| 12,500 / 10,000 | webull0 | +169 | +447 | +600 | **+16** (+268) | −3.09 |
| 12,500 / 10,000 | real35 | −9 | +432 | +600 | **−178** (+73) | −3.49 |
| 25,000 / 20,000 | webull0 | +491 | +916 | +1,200 | **+207** (+436) | −1.94 |
| 25,000 / 20,000 | real35 | +311 | +902 | +1,200 | **+13** (+227) | −2.27 |
| 50,000 / 40,000 | webull0 | +30 | +1,744 | +2,400 | **−625** (−404) | −2.87 |
| 50,000 / 40,000 | real35 | −144 | +1,730 | +2,400 | **−814** (−591) | −3.07 |
| 100,000 / 80,000 | webull0 | +855 | +3,574 | +4,800 | **−370** (−646) | −2.69 |
| 100,000 / 80,000 | real35 | +692 | +3,561 | +4,800 | **−547** (−825) | −2.79 |

Out-of-sample values in brackets are from `income_decomposition.csv`.

**Reading:**
- **Fixed fees matter less at larger size,** but the interest given up grows in step with capital: HK$1,238 a year at 100k on real35.
- **The trading result is not monotonic in size:** +311 at 25k, −144 at 50k, +692 at 100k. A different base changes which names are affordable and in what order slots fill. That is path dependence, not skill. It is the same fragility Tom found with a one-bar ADX slip.
- **No size in this table reliably beats T-bills.**

### 2.4 Calendar years: 12.5k / real35 / 20% reserve, % (`results/income_yearly.csv`)

| Year | System + T-bills | All T-bills | SPY | Extra |
|---|---|---|---|---|
| 2022 (from 30 Nov) | −0.71 | 0.36 | −5.76 | −1.07 |
| 2023 | 0.81 | 4.94 | 26.18 | **−4.13** |
| 2024 | 4.45 | 5.16 | 24.89 | −0.71 |
| 2025 | 5.82 | 4.15 | 17.72 | **+1.67** |
| 2026 (to 23 Nov) | 2.55 | 3.26 | 6.75 | −0.71 |

- At `webull0`, the yearly extra is −0.94 / −2.68 / +0.62 / +3.15 / +0.40.
- The system trailed T-bills in **4 of 5** calendar periods at the CRO fee estimate, and in **2 of 5** at zero commission.
- One good year (2025) carries most of the out-of-sample result.

### 2.5 How likely is it to trail T-bills? (`results/income_bootstrap.csv`)

**Method:** block bootstrap of the 49 monthly excess returns vs T-bills, in 3-month blocks, 5,000 paths. It assumes the next five years look like a reshuffle of the last four, which is a strong assumption.

| Scenario | P(behind T-bills) after 1 yr | 3 yrs | 5 yrs | Median 5-yr extra | 10th–90th pct 5-yr extra |
|---|---|---|---|---|---|
| 12.5k, real35 | 66% | 75% | **79%** | −4.9% | −11.8% … +2.8% |
| 12.5k, webull0 | 45% | 42% | **39%** | +1.6% | −5.6% … +9.4% |
| 100k, real35 | 50% | 53% | **54%** | −0.5% | −6.9% … +5.9% |

**Monthly excess:**
- 12.5k/real35: mean −0.097% a month, standard deviation 0.708%.
- 12.5k/webull0: +0.011% a month, standard deviation 0.680%.

**In both cases the mean is a small fraction of the noise.**

### 2.6 Live entry rule vs the old backtest entry (12.5k, webull0, no interest)
- **Old 1% deviation rule:**
  - 1.78% CAGR on HK$12,500, which is ≈ 2.2% on the HK$10,000 base and matches the V6.6.5 release note;
  - 135 trades.
- **Live limit rule:**
  - 1.33% CAGR;
  - 130 trades;
  - 43 limit skips.
- The live rule is somewhat **more conservative** than the old backtest, as the CRO expected (N-27). The Owner's real results should be compared with the 1.33% line, not the old ≈2.2%.

### 2.7 Research only, NOT approved: more slots at HK$100,000
`MAX_POSITIONS = 2` is a locked parameter. These rows are a hypothesis, not a proposal.

| | Trading HK$/yr | Extra vs T-bills, full (out-of-sample) | Max DD % |
|---|---|---|---|
| 3 slots, 30% reserve, real35 | +1,718 | −167 (+684) | −3.51 |
| 4 slots, 40% reserve, real35 | +2,462 | −5 (+392) | −4.27 |

More slots earn more from trading but give up more interest. Over the full period the net is still about zero.

---

## 3. Why the system struggles to beat T-bills

1. **By design it is mostly in cash.** At most 20% of the base is invested.
   - At 12.5k/real35, whole-share sizing makes the average position **7.9% of the base**, not 10%.
   - Days with 0 / 1 / 2 positions open: **12% / 30% / 58%**.
   - On average about **12% of the base (≈ 9% of the capital)** is in trades. The rest earns T-bill interest or nothing.
   - When SPY is below its 200-day MA, nothing is invested. As of the 23 Nov close (`data/SPY.csv`), it is below.
2. **Its edge per trade is small.** The V6.6.5 release note reports net expected value of about +1.85% per E1 trade and −1.03% per E2 trade in the 2-slot book. Neither is statistically distinguishable from zero at this size.
3. **Fees eat it.** The CRO estimated net EV per trade crosses zero at about US$0.25–0.40 fixed per side (N-9). This study confirms it at the account level: the trading line is +169 HK$/yr at zero commission and −9 at US$0.35.
4. **Every dollar in a trade stops earning about 4–5%.** That is the HK$150–170/yr hurdle at 12.5k, and HK$1,200+ at 100k.

If T-bill rates fall, the hurdle falls with them. The interest income falls too, though, and the trading result does not improve.

---

## 4. Can it run long-term? Assessment

**What supports running it:**
- The rules are fixed, fingerprinted and tested: selftest 126 checks, equivalence 0/85,120, ledger check, CRO-verified up to V6.6.5.
- Drawdowns at this sizing are small in backtest: about −2% to −5% with interest, worst month about −1% to −2%. With `min1` fees and no interest the drawdown was −11%.
- The SPY 200-day filter takes it out of the market in weak regimes.

**What argues against counting on it:**
- The extra return over T-bills is **indistinguishable from zero**. Its sign depends on a fee that has not been verified (V-1).
- It is **path-fragile.** Results jump with account size (§2.3) and with a one-bar indicator slip.
- **No forward evidence yet.** The firm's own gate is ≥ 30 closed E2 trading-path signals **and** ≥ 6 months of ledger before any forward review, and no cap-level return comparison before 100 trades.
- **Operational load:** about 33 round trips a year means a daily scan and about 66 manual limit orders a year. Each one is a chance for error. CLAUDE.md rule 1: the Owner places every order; no agent can.
- **Unresolved costs:**
  - withholding on the T-bill side, which takes about 1.4 percentage points off the yield in the 30% scenario;
  - the broker's interest on cash;
  - HKD/USD conversion.
- **Alpha decay:** short-horizon technical edges tend to weaken once published or crowded. This is a general observation, not something measured here.

**Verdict (CEO, pending CRO):**
- As a **capital-preservation sleeve that might add a little**, it can run long-term at C-7 (A) size without much risk to the capital.
- As an **income source for living costs**, it does not qualify. Expected extra income is about zero, with a 40–80% chance of trailing plain T-bills over five years, depending on fees.

---

## 5. What the Owner can do instead, or as well (options, not advice)

1. **For the income itself:** the return in every row above comes from the T-bill-like holding. The Owner should check, with the broker and in writing:
   - whether US T-bill ETF distributions to an HK resident are withheld at 30%, or exempted as qualified interest income;
   - whether HK-listed USD/HKD money-market funds, or time deposits, are available and at what yield. **Not verified this session;** no figures are given.
   - whether uninvested cash at the broker earns anything.
2. **For the system:** choose between the two C-7 options the CRO approved (25 Nov):
   - **(A)** a separate **cash** or margin-disabled account holding nothing but the swing sleeve, with **≥ HK$12,500 of settled cash**, `account_hkd` 10,000, and `switch_date` set on the day you start;
   - **(B)** **shadow-only:** scanner and signal ledger, no fills, until (A) is met.

   The CEO's preference, pending CRO: **(B) first, until V-1 (the real fee) and 6 months of ledger exist.** The study shows that (A) at today's evidence is a bet on a fee nobody has confirmed. That choice belongs to the Owner.
3. **Not recommended:** raising slots or the base to chase income. The §2.7 rows are unapproved research, and §2.3 shows size alone does not help.

## 6. What would change this verdict
- **V-1:** a real Webull contract note showing about zero commission and spread near 10 bp. That would move the 12.5k result toward the `webull0` rows: about +HK$16/yr full period, +HK$268/yr out of sample, and P(behind T-bills over 5 years) about 39%.
- **Forward ledger:** ≥ 30 closed E2 trades and ≥ 6 months, with net EV per trade clearly above the ≈ HK$5 hurdle.
- **A CRO-approved rule change** (slots, cap or base). Each needs Tom's rerun and CRO review, as C-7 already requires.

## 7. Reproduce

```
cd strategy/v6.6
python income_study.py   # needs data/*.csv (stocks) and data/BIL.csv; builds data/TBILL.csv
```

- Outputs: `results/income_scenarios.csv`, `income_decomposition.csv`, `income_yearly.csv`, `income_bootstrap.csv`.
- Lab V6.6.6 (fingerprint `943960c97a9b`): `entry_rule`, `capital_hkd`, `cash_yield`, `cash_reserve_pct`. Defaults are unchanged:
  - `results/baseline.json` is identical;
  - 9 new selftest checks (126 total, also under `-O`);
  - 4 mutants were each caught by their check.

## 8. Questions for the CRO
1. May a T-bill ETF or money-market holding sit in the C-7 (A) swing account, given the wording "nothing but the swing sleeve"? If not, where should the interest-earning part sit, and does the 20% settled-cash reserve satisfy "settled cash must cover each order"?
2. C-7 says `account_hkd` is never raised or lowered without Tom's rerun and CRO review. Does §2.3 count as that rerun for any base other than 10,000, or is a separate review needed?
3. "Living income" framing: what limits apply to putting money the Owner needs for living costs into this sleeve?

## 9. Reviews
*(Appended when received.)*
