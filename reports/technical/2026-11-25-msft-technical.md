# MSFT: Microsoft, technical review

**Analyst:** 老詹, Technical Analysis (Dept 5)
**Report date:** 2026-11-25 · **Data as of:** 2026-11-24 US close
**Subject:** Watchlist name (`config/watchlist.yaml`), not held. Input to `/analyze MSFT`.
**Prior technical report:** none. Fundamentals on file: `reports/equity/2026-08-21-msft-*.md`.

> **Last price: US$496.13, 2026-11-24 close** (Webull daily bar).

---

## 0. Data provenance and checks

| Item | Detail |
|---|---|
| File | `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/research_bars/MSFT_daily_webull.csv` |
| Origin | Webull read-only daily bars, pulled by the CEO on 2026-11-25 |
| Span | 260 sessions, 2025-11-12 → 2026-11-24 |
| SHA-256 | `6f135e4400fd1b76c5cd42c277926608177bba27de3e4df2cf55d34ee36d9bc8` (file read only, not modified) |
| Integrity | No duplicate dates, no nulls, no OHLC violations, no zero-volume rows. The 10 missing weekdays are all US exchange holidays: 27 Nov, 25 Dec, 1 Jan, 19 Jan, 16 Feb, 3 Apr, 25 May, 19 Jun, 3 Jul, 7 Sep. |

### The series is dividend-adjusted

The decimal format changes on the 18 Nov row. I traced the cause; it is benign.

- **The dividend.** Microsoft declared a **US$0.98** quarterly dividend with an **ex-date of 19 Nov 2026**. Sources: Microsoft's release as reported by 247 Wall St, and Market Chameleon (search extracts).
- **The adjustment.** Every row before 19 Nov has been multiplied by **0.998072 = 1 − 0.98 / 508.29**, where 508.29 is the unadjusted 18 Nov close.
  - That is why the 18 Nov close prints as 507.31: it is exactly 508.29 − 0.98.
  - Rows from 19 Nov onward are unadjusted.
- **Internal cross-check.** An earlier Webull pull of the same symbol (`…/scratchpad/mkt/closes.csv`, ending 16 Nov) overlaps this file for 254 sessions. The ratio between the two is a constant 0.998072, with a standard deviation of 8.7e-10. There is no other difference between the pulls.
- **External spot checks.** Each published figure below matches the file exactly once the factor is removed:

  | Date | File (adjusted) | ÷ 0.998072 | Published | Source |
  |---|---|---|---|---|
  | 4 Nov | 554.73 | 555.80 | 555.80, +6.7% | Gotrade (search extract) |
  | 10 Nov | 532.13 | 533.16 | 533.16, −2.20% | Gotrade (search extract) |
  | 13 Nov | 522.87 | 523.88 | 523.88 | Gotrade (search extract) |
  | 17 Nov | 505.26 (low 495.55) | 506.24 (low 496.51) | 506.24; low 496.51 | Benzinga / MarketBeat / Coinotag (search extracts) |
  | 18 Nov | 507.31 | 508.29 | 508.29, +0.40% | Gotrade (search extract) |

- **Not independently confirmed:** 19, 20, 23 and 24 Nov. They rest on the Webull pull alone.

**Consequence for levels.** Everything in this report uses the adjusted series, which is correct for technicals because the dividend is not a price move. Levels set before 19 Nov read **0.19% higher on an unadjusted chart**:
- 52-week high: 558.07 adjusted, 559.15 unadjusted;
- August low: 475.34 adjusted, 476.26 unadjusted;
- gap: 465.06–473.19 adjusted, 465.96–474.10 unadjusted.

The stop in §7 is set off the 24 Nov close, so it is the same on either chart.

**Method.** Computed by me in pandas 3.0 from the CSV:
- SMA 20/50/200 on closes;
- RSI(14) and ATR(14) with Wilder smoothing;
- MACD as EMA12 − EMA26 with a 9-EMA signal (`adjust=False`);
- swing points as fractal pivots (±3/5/10 bars).

The 52-week window is 2025-11-25 → 2026-11-24 (251 sessions). SMA200 is first computable on 2026-08-31.

**Blocked or failed:** direct page fetches of `halo-technologies.com` and `heygotrade.com` both failed (the hosts do not resolve in this session), so I made no further fetch attempts. External figures are search-engine extractions. `tradingkey.com` appeared in result sets; it is blacklisted and is neither used nor cited.

---

## 1. Indicator table (MSFT, 2026-11-24 close)

| Measure | Value | Read |
|---|---|---|
| Close (O / H / L) | **496.13** (490.13 / 501.82 / 488.43) | Inside the prior day's range; closed at 57.5% of the day's range |
| SMA20 | 518.38 · price **−4.29%** · −2.21% over 10 sessions | Falling |
| SMA50 | 518.63 · price **−4.34%** · +0.36% over 10 sessions | Flat |
| SMA200 | 442.83 · price **+12.04%** · +0.93% over 10 sessions | Rising |
| MA stack | 200 < price < 20 ≈ 50 | **SMA20 crossed below SMA50 on 24 Nov** (518.38 vs 518.63), the first such cross since 22 Jun 2026. Price has closed below SMA50 for 7 straight sessions (since 16 Nov). |
| RSI(14) | **41.3** (low 35.0 on 20 Nov) | Weak; never reached oversold |
| MACD (12,26,9) | **−7.53**, signal −3.10, histogram **−4.44** | Signal cross down 10 Nov; zero-line cross down 17 Nov. Histogram low −5.17 on 20 Nov, now narrowing. |
| ATR(14) | **16.72 (3.37%)**; simple-average ATR 17.47 | Elevated: 20-day realised volatility 38.7% vs 28.5% over 60 days |
| 52-wk range | 347.87 (2026-06-25) → **558.07 (2026-11-04)** | Closing range 351.49 → 554.73 |
| Drawdown from 52-wk high | **−11.10%** (−10.56% vs closing high) | 70.5% of the way up the range; +42.62% above the low |
| Volume | last 23,104,459 · 20d avg 30,755,726 · 50d avg 25,112,719 · 260d avg 32,031,912 | 20d/50d = **1.22**; last/20d = 0.75 |
| Up-day vs down-day volume, last 20 sessions | 8 up days at 27,068,451 vs 12 down days at 33,213,910 = **0.81×** (by total volume, 0.54) | Distribution |
| Returns | 1w −1.81% · 1m −6.67% · 3m +0.14% · 6m +20.68% · YTD +3.44% (from 479.64 on 2025-12-31) | |

---

## 2. Trend verdict

> **Weekly: uptrend, damaged but not broken. Daily: downtrend.** Net: **a correction inside a
> primary uptrend**, now sitting about 4% above the floor of a three-month range. The daily
> trend is down and both momentum and volume agree with it. Whether this is a correction or a
> top is decided at 475 / 463, not here. Confidence: **moderate.**

### Weekly (primary trend)

- **The move off the June low was large.** MSFT rose from 347.87 (25 Jun) to 558.07 (4 Nov), **+60.4%**. The largest single step was the gap of 30 Jul: +15.5% on 110.2m shares, the third-heaviest session of 2026.
- **From August to November the stock rose in a band of 475.34 to 558.07.**
  - Highs rose: 511.78 (10 Aug) → 516.78 (28 Aug) → 550.09 (13 Oct) → 558.07 (4 Nov).
  - Lows rose: 475.34 (18 Aug) → 485.06 (10 Sep) → 503.99 (2 Nov).
- **The damage.** The 20 Nov low of **481.03** undercut the September and early-November lows. It held above the **August low of 475.34**, which is the last structural support of the band.
- **Weekly averages:** price is below the 10-week MA (517.13) and above the 40-week MA (445.55), which is still rising (435.16 four weeks ago).
- **Weekly momentum has rolled over.** Weekly RSI is 51.2. Weekly MACD made a **bearish signal cross in the week ending 20 Nov**, the first since its bullish cross of 24 Apr 2026. That rests on 54 weekly bars, so treat it as indicative.

### Daily (intermediate trend)

- **Lower highs:** 558.07 (4 Nov) → 547.22 (9 Nov) → 526.49 (19 Nov) → 509.15 (23 Nov).
- **Lower lows:** 503.99 (2 Nov) → 495.55 (17 Nov) → 481.03 (20 Nov).
- **Moving averages:** price is below a falling SMA20 and a flat SMA50, and the two have just crossed. That is a daily downtrend by definition.
- **Two failed gap-ups in four sessions. This is the most important price-action fact in the report:**

  | Session | Open gap | Close vs open | Close position in day's range |
  |---|---|---|---|
  | 19 Nov | **+2.40%** (519.50) | −4.08% | **0.5%** (closed on the low) |
  | 23 Nov | **+4.44%** (506.06) | −2.68% | **2.8%** (closed on the low) |

  Twice, buyers opened the stock higher and sellers took it to the low by the close. Supply is meeting strength. That does not reverse in a day.

- **Between those, 20 Nov fell −2.8% on 47.2m shares**, closing at 15.3% of its range. The selling climax of the leg, if there was one, was that day. The 24 Nov bounce (+0.7%) came on just 23.1m shares, 0.75× the 20-day average: a pause, not a turn.

---

## 3. Key levels

### Fibonacci grids

| Swing | 23.6% | 38.2% | 50% | 61.8% | 78.6% |
|---|---|---|---|---|---|
| June–Nov: 347.87 → 558.07 | **508.46** | **477.77** | 452.97 | 428.17 | 392.85 |
| Aug–Nov: 475.34 → 558.07 | 538.55 | **526.47** | **516.71** | **506.94** | 493.04 |

Price (496.13) has retraced 74.9% of the Aug–Nov leg and 29.5% of the June–Nov swing.

### Resistance

| Level | Basis | Strength |
|---|---|---|
| 501.82 | 24 Nov high | Minor |
| **504.0 – 509.2** | 2 Nov swing low (503.99, broken support now overhead); 61.8% Aug–Nov retracement (506.94); 23.6% June–Nov retracement (508.46); 23 Nov failed-gap high (509.15) | **Strong: four reasons, and already rejected once** |
| **516.7 – 518.6** | 50% Aug–Nov retracement (516.71); SMA20 (518.38); SMA50 (518.63) | **Strong** |
| 526.5 | 19 Nov reversal high (526.49); 38.2% retracement (526.47) | Strong |
| 550.1 – 558.1 | 13 Oct and 4 Nov highs; 52-week high | Major |

### Support

| Level | Basis | Strength |
|---|---|---|
| 488.43 | 24 Nov low | Minor |
| 481.03 | 20 Nov low (the climax-volume day) | Moderate |
| **475.3 – 477.8** | **18 Aug swing low (475.34), the floor of the Aug–Nov band**; 38.2% June–Nov retracement (477.77) | **Strong: the level that decides correction vs top** |
| **465.06 – 473.19** | Unfilled gap between the 31 Jul high and the 3 Aug low | Gap magnet. If 475 breaks, expect it to be filled. |
| 452.97 / 442.83 | 50% June–Nov retracement / SMA200 (rising about 0.09% a day) | Primary-trend support |
| 399.72 – 430.80 | Unfilled 29→30 Jul earnings gap | Deep. Only relevant if the primary trend fails. |

### Invalidation

> **A daily close below US$462.69 invalidates my read** that this is a correction inside a
> primary uptrend. That close would put price below the August floor *and* below the unfilled
> August gap. The next real support would then be SMA200 / 50% retracement at 443–453, and the
> Aug–Nov band would be a completed top.
>
> **A close below 475.34 is the warning.** It breaks the band's floor, but leaves room for a
> gap-fill undercut that recovers. Do not add below it.

---

## 4. Indicators and divergences

- **A persistent bearish divergence ran through the whole autumn advance, and it has now resolved downward.** Each of four successive higher price highs came with *lower* momentum:

  | High | Price | RSI(14) | MACD line |
  |---|---|---|---|
  | 10 Aug | 511.78 | 79.2 | 29.28 |
  | 28 Aug | 516.78 | 73.5 | 18.93 |
  | 13 Oct | 550.09 | 70.8 | 12.37 |
  | 4 Nov | **558.07** | **64.3** | **4.52** |

  Price kept rising on fading momentum: the textbook warning. The 17–20 Nov breakdown is that warning being paid. I did not have a desk view at the time, so this is described after the fact, not claimed as a call.

- **There is no bullish divergence yet at the low.** The 20 Nov low (481.03, RSI 35.0) was a lower low than the 2 Nov low (503.99, RSI 40.1) in **both** price and RSI. Momentum confirmed the decline.
  - The setup to watch: a test of **475–481 with RSI above 35.0** would be a positive divergence. That is the condition for the E1 zone in §8.
- **MACD is negative and below its signal**, but the histogram has narrowed from −5.17 (20 Nov) to −4.44. Selling momentum is slowing, not reversing.
- **RSI 41.3** sits in the 40–60 zone that tends to cap rallies in a downtrend. On the bounces, RSI 57.5 (9 Nov) and 42.9 (18 Nov) both failed below 60.

---

## 5. Volume

- **Volume is expanding into the decline.** The 20-day average (30.76m) is 1.22× the 50-day average (25.11m). Monthly averages were 21.3m in September and 21.7m in October; November to date is **30.1m**.
- **Sellers have controlled the tape.** Over the last 20 sessions there were 12 down days averaging 33.2m shares against 8 up days averaging 27.1m. OBV fell by 182.0m shares (229.3m → 47.2m).
- **The heavy days were mostly down days.** Of the six heaviest sessions since 26 Oct, five were down days: 20 Nov (−2.8%, 47.2m), 5 Nov (−3.6%, 42.5m), 29 Oct (−0.2%, 39.3m), 30 Oct (−1.6%, 35.7m) and 2 Nov (−2.8%, 34.7m). The exception was the 4 Nov rally day (+6.7%, 50.8m), and that gain was fully given back within two weeks.
- **20 Nov was a distribution day at the low**: 47.2m shares, 1.67× the 20-day average, closing near the low. It could also turn out to be a selling climax. That will only be known if 481 holds on lower volume.

---

## 6. Weekly / daily summary

| Timeframe | State | Evidence |
|---|---|---|
| Weekly | **Uptrend, damaged** | Above the rising 40-week MA; the August floor (475.34) holds; weekly MACD has made a bearish cross |
| Daily | **Downtrend** | Lower highs and lower lows since 4 Nov; SMA20 has crossed below SMA50; two failed gap-ups; distribution volume |
| Setup | **None yet** | Price is between support (475–481) and resistance (504–509), with negative momentum and volume. No edge in the middle. |

---

## 7. Stop, and what confirms or breaks the trend

### Suggested stop (close basis)

> **Stop: a daily close below US$462.69.**
>
> - That is **2.0 × ATR(14)** below the 24 Nov close: 496.13 − 2 × 16.72. Distance **−6.74%**.

**Why that level:**
- **It sits below both supports.** The 475.34 band floor and the 465.06–473.19 August gap are both above it. A stop inside the gap (for example 1.5 × ATR = 471.05, or "floor minus 0.5 × ATR" = 467) would be taken out by an ordinary gap-fill. Gap-fills are what price tends to do once a range floor breaks.
- **2 × ATR suits the current volatility.** 20-day realised volatility is 38.7%. A tighter stop at the floor itself (475, only 1.26 × ATR) would fire on one bad session's noise.

**It only matters for a position someone holds.** MSFT is not held. For a new entry, the stop applies to the E1 zone in §8, where the risk shrinks to 2.6–4.0%.

### Confirms resumption of the uptrend

1. A **close above 509.2**, clearing the failed-gap high and the broken 2 Nov low.
2. Then a **close above 518.6** (SMA20 / SMA50), on up-day volume above the 20-day average.
3. The MACD histogram crossing above zero and RSI rising above 50.

Only all three together would make the 17–20 Nov break a shakeout rather than a top.

### Constructive, but short of confirmation

A test of **475–481** that holds, with RSI above 35 (the bullish divergence in §4) and with selling volume below 20 Nov's 47.2m. A close back above the prior session's high would mark it.

### Breaks it

- A close below **475.34**: the warning. The Aug–Nov band has failed, and a gap-fill to about 465 is likely.
- A close below **462.69**: the stop and the invalidation. The correction is reclassified as a top, with SMA200 (442.83) and the 50% retracement (452.97) next.

---

## 8. Suggested zones for Zac

Technicals do not originate positions at this firm. These zones only apply if the fundamental pipeline (`/analyze`) and the Committee want MSFT exposure.

| Zone | Price | Condition | Stop | Risk to stop | Conviction |
|---|---|---|---|---|---|
| **E1: test of the floor** | **475 – 482** | A hold, plus a reversal close (above the prior day's high), ideally with RSI above 35.0 | close < 462.69 | **2.6% – 4.0%** | **Preferred** |
| E2: confirmation | close > 518.6 | Reclaim of SMA20/50 with volume | close below 2 × ATR under the entry close, recomputed on the day (about 485 at today's ATR) | about 6.4% | Moderate; costs about 4.5% of upside versus today |
| **Do not buy** | 496 – 510 | Middle of nowhere, beneath a resistance band that has already rejected two gap-ups | — | — | — |

**My recommendation to the Committee on timing: wait.** Today's price offers neither the risk/reward of E1 nor the confirmation of E2.

---

## 9. Technical score: **40 / 100** (input to committee)

| Component | Weight | Score | Basis |
|---|---|---|---|
| Trend structure | 40 | **18** | Weekly up and above a rising SMA200, but the daily trend is down: lower highs and lows, SMA20 below SMA50, below both |
| Momentum | 20 | **6** | RSI 41; MACD below zero and below its signal; a four-peak bearish divergence that has resolved down. Partial credit for the narrowing histogram. |
| Volume | 20 | **5** | Down-day volume 1.23× up-day volume, OBV −182m, a distribution day at the low, a light-volume bounce |
| Location / risk-reward | 20 | **11** | 4% above strong support (good for E1), 12% above SMA200, a clear stop. But the immediate overhead has already rejected price twice. |
| **Total** | 100 | **40** | |

**Confidence: moderate.**
- It would rise to 55–60 on a successful 475–481 test with a positive RSI divergence.
- It would fall to 25 or below on a close under 475.34.
- The last four sessions are not independently verified (§0).

Charts describe probabilities, not certainties.

---

## 10. NOT OBTAINED register

- **Independent confirmation of the 19, 20, 23 and 24 Nov bars.**
- **Intraday data, volume-at-price, and the opening and closing auction volumes.** Not available. The stop is close-basis by design.
- **The cause of the 19 and 23 Nov gap-ups.** Not researched. Out of scope for this desk; refer to 修大哥 (Global News).

---

## Sources

- Webull read-only daily bars, MSFT, pulled 2026-11-25 (CSV path and hash in §0). Earlier Webull pull used for the internal cross-check: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/mkt/closes.csv`.
- [247 Wall St, "Microsoft Goes Ex-Dividend Nov 19 … $0.98 Payout" (13 Nov 2026)](https://247wallst.com/investing/2026/11/13/microsoft-goes-ex-dividend-nov-19-heres-what-backs-the-0-98-payout/); [Market Chameleon, MSFT dividends](https://marketchameleon.com/Overview/MSFT/Dividends)
- [Gotrade, MSFT 18 Nov close 508.29](https://www.heygotrade.com/en/news/microsoft-msft-stock-news-november-19-2026/); [Gotrade, 13 Nov 523.88](https://www.heygotrade.com/en/news/microsoft-msft-stock-news-november-16-2026/); [Gotrade, 10 Nov 533.16](https://www.heygotrade.com/en/news/microsoft-msft-stock-news-november-11-2026/); [Gotrade, 4 Nov +6.7%](https://www.heygotrade.com/en/news/microsoft-msft-stock-news-november-5-2026/) (all search extracts)
- [Benzinga MSFT](https://www.benzinga.com/quote/MSFT/charts) (17 Nov close 506.24); [MarketBeat, 17 Nov 2026](https://www.marketbeat.com/instant-alerts/price-microsoft-nasdaq-msft-stock-falls-23-heres-why-2026-11-17/); [Coinotag, low 496.51](https://en.coinotag.com/microsoft-msft-stock-496-51-low-ai-cost-doubts) (search extracts)

*Research and decision support only, not financial advice. MSFT is not held; nothing here is an
order. The Owner alone executes (standing rules 1–2).*
