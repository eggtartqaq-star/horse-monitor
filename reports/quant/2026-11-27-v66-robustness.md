# V6.6 robustness test — does the "small add-on" verdict survive? (2026-11-27, revised 2026-11-28)

**Run by:** CEO (皮褸黃). **Reviewed by:** Tom (backtest engineer), PASS WITH CORRECTIONS (`reports/quant/2026-11-27-v66-robustness-tom-review.md`). This revision applies his F-1 to F-10.
**Asked by:** the Owner (27 Nov), who chose the "honest robustness test".

**Script:** `strategy/v6.6/robustness_v66.py`, with Tom's corrections. It is a research tool outside the rules fingerprint; fingerprint `2b7b62182068` is unchanged.
**Output:** `strategy/v6.6/results/robustness/*.csv`.

**Data:**
- `strategy/v6.6/data/*.csv`: Webull read-only daily bars, 38 stocks plus SPY, pulled 2026-11-24.
- T-bill: `data/TBILL.csv`, built from BIL with 4 dividend days corrected (`income_study.py`).
- Window: 2022-11-30 → 2026-11-23.

**Set-up** (identical to income study scenario A, reproduced exactly: 3.29% vs 4.49%, 130 trades):
- capital HK$12,500 on a HK$10,000 sizing base;
- **fees US$0.35 minimum + 10 bp per side (CRO estimate, unverified; gate V-1)**;
- live entry rule;
- open-only orders;
- HK$3,000 settled cash kept at 0% (30% of the sizing base = 24% of capital);
- other idle cash in T-bills.

## Verdict: WEAKER than the 26 Nov wording. Do not call it an add-on; T-bills are the income.

> **At the CRO's estimated fee, from 2022-11 to 2026-11:**
> - The trading itself made about zero: −0.2% a year. Engine 1 made +US$81 and Engine 2 lost −US$82.
> - Keeping HK$3,000 as settled cash at 0% cost about another 1.0% a year.
> - Net: about 1.2% a year (**HK$168 a year**) less than plain T-bills, and **the account was behind the T-bill line on every single day**.
> - With zero commission it would roughly match T-bills (+0.2% a year). That is still not enough to call it an add-on.

**Supporting points:**
- It beat T-bills in **one calendar year of four** (2025). It beat them in 38% of 6-month windows, which amounts to only about 7 independent windows.
- The fee moves the result more than any setting change does. Real fees are unknown until the Owner's contract note (V-1).
- The only positive recent result (+0.55% a year since 2025) turns negative under every change to Engine 1's entry settings. It rests on one year.
- Stock-selection bias (38 names picked in 2026) most likely **flatters** these figures. The true result is more likely below −1.2% than above it.

The 26 Nov study said the system "**might** add a little". This test does not support that wording. The rest of the 26 Nov verdict stands: it is not an income source for living costs, and the income is the T-bill interest. The CRO's recommendation (B), paper only, is unchanged.

## The numbers that matter most (Tom F-3)

| Measure | Value |
|---|---|
| System vs plain T-bills, full period | 3.29% vs 4.49% a year: **−1.20% a year (−HK$168 a year)** |
| … of which: cash reserve earning 0% (same account, no trades) | **−1.03% a year** (since 2025: −0.86%) |
| … of which: the trading itself | **−0.18% a year** (since 2025: +1.40%) |
| Completed-trade P&L (130 trades) | E1 +US$81.4, E2 −US$81.7, net −US$0.3. Gross +US$117.1 against fees US$117.4. Two positions still open at the end: −US$6.2 at market. |
| Days the account was above the T-bill line | **0%** |
| Worst drawdown vs T-bills | **−6.66%** (2024-08-05); ended at about −4.5% |
| Worst absolute drawdown | **−3.49%**: peak 2022-12-14, low 2023-03-13, recovered 2023-09-01 (260 days under water) |
| Monthly excess vs T-bills | t = −0.91 over 49 months; 39% of months positive |

**Fee is the hinge (Tom F-7).** The same account under the three fee scenarios in `results/income_scenarios.csv`:

| Fee scenario | Full period vs T-bills |
|---|---|
| no minimum commission (webull0) | **+0.18% a year** |
| US$0.35 minimum (real35, CRO estimate) | −1.20% a year |
| US$1 minimum (min1) | −3.92% a year |

## A. Year by year (each year measured from the previous close; Tom F-1)

| Year | System | T-bill | Excess | No-trade account | Trading contribution | SPY | Trades | In-year max drawdown |
|---|---|---|---|---|---|---|---|---|
| 2022 (from 30 Nov) | −0.72% | 0.36% | −1.09% | 0.28% | −1.00 pp | −5.76% | 3 | −0.95% |
| 2023 | 0.94% | 4.94% | **−4.01%** | 3.76% | −2.82 pp | 26.18% | 34 | −2.88% |
| 2024 | 4.58% | 5.16% | **−0.57%** | 3.97% | +0.62 pp | 24.89% | 30 | −2.03% |
| 2025 | 5.81% | 4.15% | **+1.66%** | 3.23% | +2.58 pp | 17.72% | 37 | −1.32% |
| 2026 to 23 Nov | 2.58% | 3.26% | −0.68% | 2.56% | +0.02 pp | 6.75% | 26 | −1.62% |

- Trades add up to 130.
- The first revision reported 2024 as −0.02%. That was wrong: it dropped the first trading day of each year.

## B. Rolling 6-month windows (start each month; rules fixed, no refitting)

| Windows | Beat T-bill | Median excess | Worst | Best |
|---|---|---|---|---|
| 42 (overlapping) | **38%** | −0.33% | −3.85% | +3.57% |

- The windows overlap by 5 of 6 months, so there are only **about 7 independent windows** (Tom F-2).
- The six non-overlapping start phases beat T-bills 4/7, 2/7, 3/7, 2/7, 2/7 and 3/7.
- A real edge would beat T-bills in clearly more than half.

## C. Settings ±20%, one at a time (portfolio level, live settings)

| Setting | Full-period excess / yr | Since 2025 / yr | Trades |
|---|---|---|---|
| **base** | **−1.20%** | **+0.55%** | 130 |
| E2 score min ×0.8 / ×1.2 | −0.58% / −1.31% | +1.52% / +0.47% | 130 / 133 |
| E2 trailing ATR ×0.8 / ×1.2 | −1.87% / −0.97% | +2.18% / +1.76% | 156 / 126 |
| E1 score min ×0.8 / ×1.2 | −2.01% / −1.48% | −0.52% / −1.74% | 152 / 109 |
| E1 minimum R ×0.8 / ×1.2 * | −1.76% / −0.83% | −0.51% / +0.05% | 127 / 125 |
| E1 ATR stop ×0.8 / ×1.2 | −1.06% / −2.20% | −0.52% / −1.24% | 153 / 123 |
| E1 max hold ×0.8 / ×1.2 | **+0.45%** / −1.58% | +3.02% / +1.28% | 139 / 127 |
| E2 max hold ×0.8 / ×1.2 | −1.15% / −1.12% | +0.99% / +0.99% | 131 / 130 |

\* The E1 limit price in `lab.py` keeps a hard-coded R ≥ 2 (it mirrors `sizing_v66.py:55`), so these rows are only half wired. Tom's probe, with the limit following min_r, gives:
- ×0.8: −1.78% / −0.79% / 147 trades;
- ×1.2: −1.89% / −0.54% / 123 trades.

`lab.py` was not changed; it is a core file.

**Reading:**
- The moves against base range from −1.00 to +1.65 pp over the full period, and from −2.29 to +2.47 pp since 2025.
- Only 1 of 14 variants turns the full period positive. That hurdle includes the ~1%/yr reserve cost: measured on the trading alone, 3–4 of 14 are positive. That pattern fits **no edge**, not a negative edge.
- **Since 2025, every E1 entry change, in either direction, turns +0.55% negative** (6 of 6 after Tom's probe). The recent gain sits on a narrow peak.
- **Do not adopt the one positive variant (E1 max hold ×0.8).** Picking the best of 14 after the fact is overfitting (V6.4 audit, U-9). The "since 2025" figures were already seen in the 26 Nov study, so they are descriptive only, not a clean holdout.

## D. Winner-dependence check (not a bound; Tom F-8, F-9)

The 38 names were chosen in 2026. This check removes the names that rose most over the window and re-runs.

| Removed | Names | Full-period excess / yr | Since 2025 / yr | Trades |
|---|---|---|---|---|
| none (38) | — | −1.20% | +0.55% | 130 |
| top 5 risers | PLTR MU NVDA AVGO AMD | −1.91% | +0.80% | 135 |
| top 10 risers | + META MSTR LLY SHOP GOOGL | −1.04% | +0.16% | 136 |

**Why so little changes: affordability, not holding period.**
- The 10% cap on a HK$10,000 base is about US$128 per position, so **21 of the 38 names never completed a trade**.
- Of the 10 removed names, NVDA, AVGO, META, MSTR and LLY had 0 trades. Their price was above the cap on almost every signal day (affordable on 1/131, 0/148, 0/159, 1/45 and 0/152 signal days).
- The effective universe was **17 lower-priced names**.

**Where the system could afford a riser, it made money from it:**
- AMD +US$19.5 and MU +US$18.8 are the #2 and #3 contributors.
- The top-5 risers made +US$32.7 in total.
- Removing them costs 0.71 pp a year (−1.20% → −1.91%).
- The best contributor overall was INTC (+US$51.0); the worst were NFLX −US$38.3, NKE −17.9 and PFE −14.5.

**Why it is not a bound.** A list fixed in January 2022 would also include names that later fell out of the index. Removing winners cannot capture that, and Engine 1 buys dips, which is exactly where those names do damage. The bias most likely flatters the result.

**Still to do: the proper test,** on a universe fixed in early 2022.
- **Wikipedia is not used** (Owner, 2026-11-28: the public can edit it; CLAUDE.md rule 5). No Wikipedia data entered this test: every attempt to fetch it was blocked by the network.
- **Primary-source route.** The S&P 100 holdings of the iShares S&P 100 ETF (OEF), as reported in the fund's regulatory filing on SEC EDGAR for a quarter-end in early 2022, or the issuer's own dated holdings file. Either needs the Owner's approval for network access to that host.
- It should be read for the affordable subset (prices ≤ about US$128).

## What this changes

1. **Owner-facing wording.** Replace "a small add-on that might add a little" with the quoted verdict above.
2. **Nothing changes in the rules or the package.** CRO recommendation (B) stands: paper only, no real money in V6.6.
3. **What could change the verdict:**
   - a real fee near zero (V-1). Even then it is only about level with T-bills.
   - forward evidence that 2025 was not luck: paper trading plus the cloud shadow log. The shadow log is paused until the Webull connector is attached.
   - cash interest on the reserve. The Owner says Futu pays interest on cash; this is not modelled. If the reserve earned the T-bill rate, most of the −1.03% would disappear, leaving the trading at about −0.2% a year: still no add-on.
4. **For living income:** T-bills, or the broker's cash interest, are the income.

## Limits

- About 4 years and 130 trades; wide confidence intervals (income study §3). The bootstrap's 28–75% chance of trailing T-bills over 5 years is at its high end (75%) for this fee.
- Webull data here; the live system uses Yahoo. The two have not been cross-checked yet.
- T-bill withholding tax is not applied in the base case (see the income study).
- Tails (gaps, −40% names) are covered by Mario's stress work, not here.

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders.*
