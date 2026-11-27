# V6.6 robustness test — does the "small add-on" verdict survive? (2026-11-27)

**Run by:** CEO (皮褸黃), with review by Tom (backtest engineer) pending. **Asked by:** the Owner (27 Nov), who chose the "honest robustness test".
**Script:** `strategy/v6.6/robustness_v66.py`. It is a research tool outside the rules fingerprint; fingerprint `2b7b62182068` is unchanged.
**Output:** `strategy/v6.6/results/robustness/*.csv`. A re-run is byte-identical.
**Data:**
- `strategy/v6.6/data/*.csv`: Webull read-only daily bars, 38 stocks plus SPY, pulled 2026-11-24.
- T-bill: `data/TBILL.csv`, built from BIL with 4 dividend days corrected (see `income_study.py`).
- Tradable window: 2022-11-30 → 2026-11-23, after SPY's 200-day average becomes valid.

**Set-up** (identical to income study scenario A, which this reproduces exactly: 3.29% vs 4.49%, 130 trades):
- capital HK$12,500 on a HK$10,000 sizing base;
- fees US$0.35 minimum + 10 bp per side (CRO estimate; the real fee is unverified, gate V-1);
- live entry rule (limit ≤ the maximum limit; no buy if the open is at or below the stop);
- open-only orders (cancel if not filled);
- 30% settled cash kept; other idle cash earns T-bill yield.

## Verdict: WEAKER than the 26 Nov wording. T-bills are the income; the trading part has added nothing over four years.

- **Trading made essentially nothing.** Total trade P&L over 4 years and 130 trades: **US$ −0.3** (estimate, before interest). The system's whole return is the interest on idle cash.
- **It earned less than plain T-bills.** It returned **3.29% a year vs 4.49%** for putting the same HK$12,500 in T-bills: **−1.20% a year**, about HK$150 a year (derived estimate). The cost comes from fees and from the 30% cash that earns no interest.
- **It beat T-bills in one year of four (2025), and in 38% of 6-month windows.**
- **Changing any one setting by ±20% moves the result by up to about ±1% a year.** Only 1 of 14 variants turned the full-period result positive (shorter E1 holding), which looks like noise rather than an edge.
- **Removing the hindsight winners does not change the picture.** The system was not riding them. The stock-selection bias is real, but it is not what decides this verdict.

The 26 Nov study said the system "**might** add a little" as a small sleeve. This test does not support "add": over this sample the expected addition is **zero to negative** against T-bills. The rest of the 26 Nov verdict stands: it is not an income source for living costs, and the income is the T-bill interest.

## A. Year by year (same account, system vs T-bill)

| Year | System | T-bill | Excess | SPY | Trades | Max drawdown |
|---|---|---|---|---|---|---|
| 2023 | 0.93% | 4.93% | **−4.00%** | 26.71% | 34 | −2.88% |
| 2024 | 5.12% | 5.14% | −0.02% | 25.59% | 30 | −2.03% |
| 2025 | 5.86% | 4.13% | **+1.73%** | 18.01% | 37 | −1.32% |
| 2026 to 23 Nov | 2.16% | 3.21% | −1.05% | 6.55% | 26 | −1.62% |

- Risk was small every year: the worst drawdown was under 3%.
- The 2025 gain (the out-of-sample year in the income study) is the only positive year. The out-of-sample figure (+0.55% a year since 2025-01-01) therefore rests on one year.

## B. Rolling 6-month windows (start each month; rules fixed, no refitting)

| Windows | Beat T-bill | Median excess | Worst | Best |
|---|---|---|---|---|
| 42 | **38%** | −0.22% | −3.85% | +3.68% |

The figures are 6-month excess returns, not annualised. A real edge would beat T-bills in clearly more than half the windows.

## C. Settings ±20%, one at a time (portfolio level, live settings)

| Setting | Full-period excess / yr | Since 2025 / yr | Trades |
|---|---|---|---|
| **base** | **−1.20%** | **+0.55%** | 130 |
| E2 score min ×0.8 / ×1.2 | −0.58% / −1.31% | +1.52% / +0.47% | 130 / 133 |
| E2 trailing ATR ×0.8 / ×1.2 | −1.87% / −0.97% | +2.18% / +1.76% | 156 / 126 |
| E1 score min ×0.8 / ×1.2 | −2.01% / −1.48% | −0.52% / −1.74% | 152 / 109 |
| E1 minimum R ×0.8 / ×1.2 | −1.76% / −0.83% | −0.51% / +0.05% | 127 / 125 |
| E1 ATR stop ×0.8 / ×1.2 | −1.06% / −2.20% | −0.52% / −1.24% | 153 / 123 |
| E1 max hold ×0.8 / ×1.2 | **+0.45%** / −1.58% | +3.02% / +1.28% | 139 / 127 |
| E2 max hold ×0.8 / ×1.2 | −1.15% / −1.12% | +0.99% / +0.99% | 131 / 130 |

- **Full period:** 13 of 14 variants stay negative.
- **Since 2025:** the results scatter on both sides of zero, which is what noise looks like.
- **Do not adopt the one positive variant (E1 max hold ×0.8).** Picking the best of 14 variants after the fact is exactly the overfitting the firm's audits warn about (V6.4 audit, U-9).

## D. Hindsight-winner test (a proxy for stock-selection bias)

The 38 names were chosen in 2026 (Tom 11-24, F-01). The proxy removes the names that rose most over the window and re-runs.

| Removed | Names | Full-period excess / yr | Since 2025 / yr | Trades |
|---|---|---|---|---|
| none (38) | — | −1.20% | +0.55% | 130 |
| top 5 risers | PLTR MU NVDA AVGO AMD | −1.91% | +0.80% | 135 |
| top 10 risers | + META MSTR LLY SHOP GOOGL | −1.04% | +0.16% | 136 |

- **Top-10 rises over the window:** PLTR +2025%, MU +1149%, NVDA +879%, AVGO +503%, AMD +484%, META +411%, MSTR +326%, LLY +279%, SHOP +229%, GOOGL +182%.
- **Who made and lost money:**
  - best: INTC +US$51.0, AMD +19.5, MU +18.8, XOM +15.2, WMT +12.1;
  - worst: NFLX −38.3, NKE −17.9, PFE −14.5.
  - Several big risers made almost nothing for the system.
- **Reading:** the result barely depends on the hindsight winners, because the system trades short swings and does not hold trends. This is a harsh bound, not an estimate of the bias.
- **Still to do:** the proper test, a universe fixed in January 2022 (the S&P 100 as listed then). This session's network blocks Wikipedia.
  - A personal environment, "horse-monitor", was created today with `en.wikipedia.org` allowed. It is unused so far.
  - Starting a helper session on it was refused by this session's permission check. The test can run in the Owner's next session on that environment.

## What this changes

1. **Owner-facing wording:**
   - The 26 Nov study said "a small add-on that might add a little". It should now read: "**over 2022-11 to 2026-11 the trading added nothing; with fees and the 30% cash buffer it earned about 1.2% a year less than plain T-bills**".
   - The 5-year bootstrap (28–75% chance of trailing T-bills) is consistent with this; this test points to the high end of that range.
2. **Nothing changes in the rules or the package.** The CRO's recommendation (B) stands: paper only, and no real money in V6.6.
3. **Paper trading still has value as a forward test.**
   - These four years are the only evidence so far.
   - Forward paper results, and the cloud shadow log (item 3 of today's plan), are the only way to learn whether 2025 was the start of something or luck.
   - Today SPY is below its 200-day average, so the system is idle.
4. **For living income:** the T-bill (or the broker's cash interest, which the Owner says Futu pays) is the income. This test adds weight to that.

## Limits

- The sample covers about 4 years and 130 trades; confidence intervals are wide (income study §3).
- The fee is an estimate until V-1 (contract note).
- Data comes from Webull, while the live system uses Yahoo. The two have not yet been cross-checked; the shadow log will do it.
- T-bill withholding tax is not applied in the base case. A 30% withholding scenario is in the income study.
- The −40% gap and other tails are covered by Mario's stress work, not here.

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders.*
