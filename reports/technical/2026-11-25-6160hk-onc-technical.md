# 6160.HK / ONC: BeOne Medicines, technical review

**Analyst:** 老詹, Technical Analysis (Dept 5)
**Report date:** 2026-11-25 · **Data as of:** 2026-11-24 US close
**Subject:** Live position. The Owner holds **6160.HK**, cost **HK$219.60**, size NOT DISCLOSED
(`config/portfolio-webull-snapshot-2026-11-13.yaml`).
**Primary series:** ONC (Nasdaq ADS). The Webull bar API has no HK data.
**Supersedes:** `reports/technical/2026-08-14-6160hk-technical.md`. §7 logs what happened to that view.

> **Last price: ONC US$415.62, 2026-11-24 close** (Webull daily bar).
> At FX 7.84 that is equivalent to **HK$250.65** per 6160.HK share. This is arithmetic, not an HK
> print. I could not find an HK close for 23–25 Nov (§6).

---

## 0. Data provenance and checks

| Item | Detail |
|---|---|
| File | `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/research_bars/ONC_daily_webull.csv` |
| Origin | Webull read-only daily bars, pulled by the CEO on 2026-11-25 |
| Span | 260 sessions, 2025-11-12 → 2026-11-24 |
| SHA-256 | `1954744cbd5bb97080eb5672bf21711bdda804f548499b6523bde1c00598e084` (file read only, not modified) |
| Integrity | No duplicate dates, no nulls, no OHLC violations, no zero-volume rows. The 10 missing weekdays are all US exchange holidays: 27 Nov, 25 Dec, 1 Jan, 19 Jan, 16 Feb, 3 Apr, 25 May, 19 Jun, 3 Jul, 7 Sep. |
| Format note | Prices switch between 2 and 6 decimal places from row to row, and sometimes within a row. ONC pays no dividend, so this is not an adjustment artefact. The values pass every check above and the spot checks below, so I read it as API serialisation. |

**Spot checks against independent sources.** Every one matches the file exactly:

| Date | File close | Published | Source |
|---|---|---|---|
| 2025-11-17 | high 385.22 | 52-wk high US$385.22 | MacroTrends, cited in the 2026-08-14 report |
| 2026-08-04 | 323.01 | 323.01 | MacroTrends, cited in the 2026-08-14 report |
| 2026-08-07 | 348.27 | 348.27 | search-surfaced quote, cited in the 2026-08-14 report |
| 2026-10-23 | 377.63 | 377.63 | Yahoo Finance (search extract) |
| 2026-10-30 | 370.33 (−1.23) | 370.33, −1.23 (−0.33%) | Stockanalysis.com (search extract) |
| 2026-11-06 | 406.96 | 406.96 | Investing.com (search extract; page undated, so weak) |

**Not independently confirmed:** the 12 sessions from 9 Nov to 24 Nov. They rest on the Webull pull alone.

**Method.** Computed by me in pandas 3.0 from the CSV:
- SMA 20/50/200 on closes;
- RSI(14) and ATR(14) with Wilder smoothing (α = 1/14);
- MACD as EMA12 − EMA26 with a 9-EMA signal (`adjust=False`);
- swing points as fractal pivots (high or low is the extreme of ±3/5/10 bars).

The 52-week window is the calendar 52 weeks 2025-11-25 → 2026-11-24 (251 sessions). SMA200 is first computable on 2026-08-31.

**Blocked or failed:** direct page fetches of `halo-technologies.com` and `heygotrade.com` both failed (the hosts do not resolve in this session), so I made no further fetch attempts. Every external figure in this report is a search-engine extraction, not an opened page. `tradingkey.com` appeared in one result set; it is blacklisted and is neither used nor cited.

---

## 1. Indicator table (ONC, 2026-11-24 close)

| Measure | Value | Read |
|---|---|---|
| Close (O / H / L) | **415.62** (399.90 / 415.98 / 399.90) | Opened on the low and closed at 97.8% of the day's range |
| SMA20 | 396.75 · price **+4.75%** · +4.72% over 10 sessions | Rising |
| SMA50 | 376.94 · price **+10.26%** · +3.05% over 10 sessions | Rising |
| SMA200 | 329.82 · price **+26.01%** · +0.95% over 10 sessions | Rising; price extended |
| MA stack | price > 20 > 50 > 200 | Fully bullish. SMA50 has stayed above SMA200 since SMA200 became computable (minimum gap 8.63). |
| RSI(14) | **61.5** (pullback low 49.99 on 20 Nov) | Firm, not overbought |
| MACD (12,26,9) | **9.60**, signal 10.58, histogram **−0.98** | Line well above zero. Bearish signal-line cross on 19 Nov; histogram low −1.66 on 23 Nov, now rising. |
| ATR(14) | **12.02 (2.89%)**; simple-average ATR 12.59 | |
| 52-wk range | 253.95 (2026-06-11) → **424.73 (2026-11-10)** | Closing range 260.27 → 424.00 |
| Drawdown from 52-wk high | **−2.14%** (−1.98% vs closing high) | 94.7% of the way up the range; +63.66% above the low |
| Volume | last 403,097 · 20d avg 419,248 · 50d avg 402,173 · 260d avg 319,988 | 20d/50d = 1.04 |
| Up-day vs down-day volume, last 20 sessions | 517,568 vs 320,928 = **1.61×** | Accumulation |
| Realised volatility (annualised) | 20d 40.1% · 60d 33.7% · 252d 34.1% | |
| Returns | 1w +0.57% · 1m +12.07% · 3m +10.60% · 6m +38.54% · YTD +36.80% (from 303.81 on 2025-12-31) | |

---

## 2. Trend verdict

> **UPTREND, on both the weekly and the daily chart.** ONC broke out of a three-month range in
> early November. It has just completed its first pullback, which held, and has resumed.
> Confidence: **moderate-high.**

### Weekly (primary trend)

- **The trend reversed at the June low.** The stock fell from the 2025-11-17 high of 385.22 to 253.95 on 2026-06-11, a decline of 34.1%. Since then it has rallied for five months:

  | Month-end | Close |
  |---|---|
  | Jun | 284.97 |
  | Jul | 316.01 |
  | Aug | 359.58 |
  | Sep | 365.94 |
  | Oct | 370.33 |
  | Nov (to date) | 415.62 |

- **August to October was a range of 336.95 to 388.66.** The lows were 10 Sep and 8 Oct; the highs were 25 Aug, 30 Sep and 21 Oct. The highs went sideways while the lows rose (336.95 → 340.44 → 347.61). That is a constructive base, not a top.
- **The range broke on 4–6 Nov**, the sessions around the Q3 2026 results. Per search extracts of BeOne's 8-K exhibit, the results were reported on 5 Nov 2026 and full-year revenue guidance was raised to US$6.9–7.0bn. The weekly close of **406.96 on 6 Nov** was the first above the range, and the 13 Nov week closed at 416.54.
- **Weekly averages:** 10-week MA 382.05 and 40-week MA 328.77, both rising. The 40-week MA was 323.08 four weeks ago.
- **Weekly indicators:** RSI 64.3. MACD is positive with a histogram of +5.33, and its last signal cross was bullish (3 Jul 2026). These rest on only 54 weekly bars, so the EMAs are not fully converged; treat them as indicative.
- **Conventional range-height projection:** 388.66 + (388.66 − 336.95) = **US$440.37**. This is a reference level, not a forecast.

### Daily (intermediate trend)

- **The 4–10 Nov advance** ran from 355.00 to a 424.00 close in five sessions. Average volume was 739,739.
- **The 11–20 Nov pullback** came on less than half that volume (302,066 average). It reached an intraday low of **385.00 on 20 Nov**, which is the 50% retracement of the 347.61 → 424.73 leg (386.17).
- **The pullback was reversed.** The 23 Nov close was +3.2% and the 24 Nov close +3.0%, the latter a full-range bar from the open (low) to the close (near the high).
- **This is the textbook sequence:** an impulse on high volume, then a pullback on low volume to a 50% retracement, then a resumption. It is also the first higher low *after* the breakout (385.00 > 347.61).

### Possible record-high context (secondary source, lower confidence)

Search extracts of MacroTrends and CompaniesMarketCap put ONC's previous record **closing** high at **US$403.14 on 2021-09-17**, when the stock traded as BGNE. I could not open either page.

If that figure is right:
- the November breakout took the stock to record territory;
- the 19–20 Nov closes (399.70, 390.94) were a two-day dip back under the old record;
- 23 Nov (403.36) reclaimed it.

That would be a classic breakout-and-retest. The ~400 support in §3 does **not** depend on this number, because the in-file lows of 398.54 (19 Nov) and 399.90 (24 Nov) mark it independently.

---

## 3. Key levels

### Resistance

| Level (US$) | HK$ equivalent at 7.84 | Basis |
|---|---|---|
| **415.98** | 250.9 | 24 Nov high (price closed 0.36 below it) |
| **417.14 – 424.73** | 251.6 – 256.1 | 13 Nov high, up to the **52-week high of 424.73 on 10 Nov**. Closing high 424.00. Five sessions (9–13 Nov) of supply sit here. |
| 440.37 | 265.6 | Range-height projection (§2); reference only |

### Support

| Level (US$) | HK$ equivalent | Basis | Strength |
|---|---|---|---|
| **395.3 – 400** | 238.4 – 241.2 | 38.2% retracement of 347.61 → 424.73 (395.27); SMA20 396.75; 19 Nov low 398.54; 24 Nov low 399.90; possibly the 2021 record close of 403.14 (secondary) | Moderate |
| **383.0 – 386.5** | 231.0 – 233.1 | **20 Nov swing low 385.00**; 50% retracement 386.17; 23.6% retracement of the whole 253.95 → 424.73 swing (384.43); unfilled gap 383.00 – 385.00, which is the remainder of the 4→5 Nov gap of 383.00 – 386.45 | **Strong: four independent reasons** |
| **376.9 – 377.8** | 227.3 – 227.8 | SMA50 376.94; 61.8% retracement 377.07; 4 Nov close 377.78 | Strong |
| 357.5 – 368.4 | 215.6 – 222.2 | Unfilled 3→4 Nov breakout gap (3 Nov high 357.535 / 4 Nov low 368.37) | Gap magnet, if it gets there |
| **347.61** | 209.6 | 3 Nov swing low: the last higher low before the breakout | Primary-trend line |
| 329.82 | 198.9 | SMA200 | |

### Invalidation

> **A daily close below US$385.00 invalidates the "breakout is holding" read.** That close would
> undercut the retest low, the 50% retracement and the November gap top all at once. It would
> turn the November move into a failed breakout.
>
> **A daily close below US$347.61 invalidates the primary uptrend.** It would break the sequence of
> higher lows that began in June.

I am stating both now so I cannot move them later.

---

## 4. Indicators and divergences

- **No bearish divergence at the high.** Price made a higher high on 10 Nov (424.73) versus 21 Oct (388.66). RSI also made a higher high (72.8 vs 66.5), and so did the MACD line (11.40 vs 5.26). Momentum **confirmed** the breakout.
- **There is a minor MACD lower high against August.** The MACD line peaked at 16.38 (21 Aug) in August and 14.24 (13 Nov) in November. RSI also peaked lower: 76.9 (11 Aug) against 72.8 (10 Nov).
  - Price, however, is 11.8% higher than at the August highs (424.73 vs 380.00).
  - MACD is measured in price units and captures the *slope* of the trend. The August impulse was steeper.
  - I log this as a **mild momentum divergence on the bigger swing. It is not a sell signal.** It would only matter if price failed at 424.73 and then broke 385.
- **The pullback had bull-market character.** RSI bottomed at 49.99 on 20 Nov and turned up. In an uptrend, RSI holding the 40–50 zone on pullbacks is the expected behaviour.
- **The MACD histogram is negative (−0.98) but rising.** The 19 Nov bearish signal cross happened with the MACD line at +11.6, far above zero: momentum cooled, the trend did not reverse.
  - If price holds ~400, a bullish re-cross is likely within a few sessions. That is an estimate from the histogram's slope, not a reading.
  - A re-cross would be the momentum confirmation of the resumption.
- **Daily MACD zero line:** last crossed up on 15 Oct (374.08). The line has been positive since.

---

## 5. Volume

- **The trend in volume is rising.** Monthly average volume bottomed at 205,022 in April. It was 405,651 in August and is 443,970 in November to date. The 20-day average (419,248) is 1.31× the 260-day average (319,988).
- **Volume has favoured buyers over the last 20 sessions.** Up days averaged 517,568 shares and down days 320,928, a ratio of **1.61×**. OBV rose by about 1.97m shares over the same 20 sessions (from −1,724,613 to +241,787).
- **The breakout had volume; the pullback did not.** 5 Nov (959,820) and 6 Nov (941,742) were the 2nd- and 3rd-heaviest sessions of the last 60. The 11–20 Nov pullback averaged 302,066, and 16 Nov (160,894) was the lightest session since 7 Oct.
- **One caution:** 5 Nov, the earnings-gap day, opened +5.6% and closed at 4.3% of its range, near the low. The first reaction to the results was sold. The next session (6 Nov, +5.1% on 941,742) reversed that decisively, so I treat it as resolved.
- **The 24 Nov rally (+3.0%) came on 403,097 shares**, 0.96× the 20-day average. That is ordinary, not a volume confirmation. The confirmation I want is in §8.

---

## 6. 6160.HK against ONC: ratio, FX and divergence

### ADS ratio: verified

**1 ONC ADS = 13 ordinary shares (6160.HK).**
- The cover page of BeOne's Form 8-K dated 2026-04-14 lists the Nasdaq ADSs as "American Depositary Shares, each representing 13 Ordinary Shares, par value $0.0001 per share". I read this through a search extract of the Boardroom Alpha mirror of the SEC filing.
- Form 4 footnotes from June 2026 (StreetInsider) state the same ratio.
- **Independent arithmetic check.** A June 2026 HKEX announcement priced an option grant at US$270.52 per ADS, "about HK$163.14 per ordinary share" (10jqka, search extract). 163.14 × 13 ÷ 270.52 gives an implied FX of **7.840**, inside the HKD peg band. That is consistent with 13:1.

### FX used

**7.84 HKD per USD.**
- 7.84696, observed 17 Nov 2026 (therighttrader.com mid-market reference, search extract);
- 7.84 on 6 Nov 2026 (MarketXLS, search extract).

The 24 Nov rate was NOT OBTAINED. A ±0.01 error in FX moves any HK equivalent by about ±0.13%.

### HK prints I could find

All three come from search snippets. I could not open any of the pages.

| HK date | 6160.HK | Source |
|---|---|---|
| 12 Nov 2026 | **HK$255.80**, +4.00 (+1.589%) | etnet quote snapshot timestamped "12/11/2026 16:33" (after the close) |
| 19 Nov 2026 | **HK$242.60** | Derived: the 20 Nov print plus its stated HK$11.80 fall |
| 20 Nov 2026 | **HK$230.80**, −11.80 (−4.9%) | Halo Technologies quote page. The page fetch failed, so I could not confirm it against a second source. |

**Excluded as unreliable:**
- Investing.com's "HK$244.20 on 8 Nov 2026": 8 Nov 2026 is a Sunday.
- Investing.com's "52-week range 153.00 – 251.80": undated, and inconsistent with the 255.80 etnet print.

### Divergence

The HK close (16:00 HKT) is at 03:00 ET. That is **after** the previous ONC close and 6.5 hours **before** the next ONC open. The fair comparison is therefore against the next ONC open. The comparison against the previous close shows how much news the HK session absorbed first.

| HK date | HK close | ONC-implied HK, from the previous ONC close | HK vs that | ONC-implied HK, from the next ONC open | HK vs that |
|---|---|---|---|---|---|
| 12 Nov | 255.80 | 253.28 (11 Nov close 419.98) | +0.99% | 253.86 (12 Nov open 420.94) | **+0.76%** |
| 19 Nov | 242.60 | 243.40 (18 Nov close 403.60) | −0.33% | 242.93 (19 Nov open 402.81) | **−0.13%** |
| 20 Nov | 230.80 | 241.05 (19 Nov close 399.70) | **−4.25%** | 233.24 (20 Nov open 386.75) | **−1.05%** |

**Reading:**
- **Time-aligned, the two lines agree within about ±1%.** There is no persistent HK premium or discount. That is what a fungible 13:1 ADS should show.
- **20 Nov shows the HK line moving first.** HK fell 4.9% during its session. ONC then opened −3.24% (399.70 → 386.75), traded down to 385.00 and **closed at 390.94**, back above its own low.
- Against the 19 Nov ONC close, the HK line was briefly 4.25% "cheap". That gap was ONC catching up later, not a mispricing.
- **Practical consequence:** an HK close can print below a level that ONC holds the same day. This matters for where the HK stop goes (§8).

---

## 7. Log of the 2026-08-14 view

**(a) Invalidation (a daily close below HK$199.50): not known to have triggered, but not confirmed.**
- ONC-equivalent of HK$199.50: **US$330.5 – 333.4** at FX 7.78 – 7.847.
- ONC's lowest close since 14 Aug: **341.80 on 10 Sep** (lowest intraday 336.95, same day).
- At 7.84 that close is equivalent to HK$206.13, **3.32% above** HK$199.50.
- In §6 the HK line printed as much as 4.25% below the previous ONC close on a news day. So I **cannot rule out** a 6160.HK close below 199.50 around 10 Sep, and I have no HK closes for that window.

**Action:** if the Owner's broker history shows a 6160.HK close below HK$199.50 at any point since 14 Aug, that view was stopped out, and I will record it as such. I am not claiming a clean pass I cannot evidence.

**(b) Breakout trigger (a weekly close above HK$229.40): met, on the evidence available.**
- ONC weekly closes of 406.96 (6 Nov) and 416.54 (13 Nov) are equivalent to HK$245.43 and HK$251.21.
- The HK line itself printed HK$255.80 on 12 Nov.
- I did not obtain an HK *weekly* close directly.
- The August report said a confirmed break would turn the regime from range to trend, and that the correct response would be the opposite of trimming. That is what the chart now shows.

**(c) Correction: the ONC jump was on 7 Aug, not 6 Aug.**
- The August report put "ONC +5.46%" on 6 Aug.
- The Webull bars show 6 Aug +0.69% (327.53 → 329.80) and **7 Aug +5.60%** (→ 348.27).
- The cited US$347.80 is exactly +5.46% on 329.80, so it was almost certainly a 7 Aug intraday quote with the wrong date.

**(d) Correction: the one-way lead–lag claim is withdrawn.**
- The August report said ONC is the price-setting venue and that the 14 Aug HK drop (−3.74%) was "HK catching down to a weak ONC session on 13 August".
- The bars show ONC's 13 Aug session was **−0.85%** (359.05 → 356.01), not weak. ONC fell **−2.40%** only on 14 Aug, *after* the HK session.
- 20 Nov shows the same pattern (§6).
- The data support co-movement, with whichever session trades first absorbing the news. **They do not support "check ONC first, treat HK as follow-through" as a rule.**
- Caveat: the 14 Aug HK move was itself brief-supplied and unverified in August.

---

## 8. Stop, and what confirms or breaks the trend

### Suggested stop (close basis)

> **Stop: a daily close in ONC below US$385.00. Act in Hong Kong at the next HK session.**
>
> - Distance from the 24 Nov close: **30.62 = 2.55 × ATR(14)** (ATR = 12.02), or **−7.37%**.
> - A mechanical 2.5 × ATR stop would sit at 385.56, which lands on the same structure.

**Why that level:**
- **385.00 is the retest low.** It is also the 50% retracement of the breakout leg, the 23.6% retracement of the whole June–November swing, and the top of the unfilled 383.00 – 386.45 gap.
- **A close below it means the post-breakout retest failed**, and price would be back inside the gap.
- **It sits outside the noise band.** The 2.0 × ATR level (391.57) is above the 20 Nov close (390.94). It lies *inside* a pullback the market has just shown it can make without breaking the trend. That is why I use 2.5 ×, not 2 ×.

**If an HK-line trigger is required:** use a **6160.HK close below HK$229.40**, not the arithmetic equivalent of HK$232.18.
- The equivalent would already have fired on 20 Nov (HK$230.80) on a timing gap that ONC recovered the same day (§6).
- HK$229.40 is the November 2025 52-week high, so it is the old breakout line. It sits 0.6% under the only late-November HK low I could find.
- In ONC terms it is US$380.38 (2.93 × ATR).

**Wider alternative, if the Committee prefers a trend stop over a swing stop:** a close below **US$376.9** (SMA50 / 61.8% retracement). That is **3.22 × ATR, −9.31%**.

**Not recommended: a stop near the Owner's cost of HK$219.60** (US$364.13 equivalent). Cost basis is not a chart level (L-003 logic; see the 2026-08-14 report §8).

**Sizing arithmetic for Zac:** at the 385.00 stop, 1% portfolio risk (`config/risk-limits.yaml` `max_risk_per_trade: 0.01`) allows at most about **13.6% of portfolio notional**. That is before the concentration limits, which are Zac's and John's to apply.

### Confirms the trend

1. A **daily close above 424.73** (the 52-week high), on volume above the 20-day average (about 419k shares).
2. The MACD histogram crossing back above zero.
3. RSI holding above 50 on any further dip.

Items 2 and 3 can happen first. Item 1 is the decisive one.

### Weakens it, without breaking it

A rejection at 417–425 (a high-volume reversal bar), then a close below 395 (SMA20 / 38.2%). That would set up a re-test of 385.

### Breaks it

- A close below **385.00**: the stop.
- A close below **376.9**: the medium-term trend is in question.
- A close below **347.61**: the primary uptrend is over.

---

## 9. Suggested zones for Zac

The position exists, so the question is add, hold or trim. **Technicals support HOLD.** Adds are only for the case where the Committee wants more of this name on fundamentals.

| Zone | ONC (US$) | 6160.HK equivalent at 7.84 | Rationale | Risk to the 385 stop | Conviction |
|---|---|---|---|---|---|
| **A1: pullback to support** | **395 – 400** | HK$238.2 – 241.2 | SMA20, 38.2% retracement, the 19/24 Nov lows | 2.5% – 3.8% | **Highest** |
| A2: retest low | 385 – 387 | HK$232.2 – 233.4 | Buy the *reaction*, meaning a close back above the prior day's high, never the approach | <1% (prone to whipsaw) | Low |
| B: breakout add | close > 424.73 on volume > 419k | > HK$256.1 | Confirmed continuation. Then raise the stop to a close below 400 | ~5.8%, measured to the raised 400 stop | Moderate |
| **Do not add** | 415 – 425 | HK$251 – 256 | Directly beneath the 52-week high; supply from 9–13 Nov | — | — |

**Trim:** no technical trim signal while the trend holds. If Risk wants a partial reduction, the place is a *failed* test of 424.73: a reversal bar on above-average volume. Do not trim pre-emptively.

**Position status at the equivalent level:** ONC 415.62 ≈ HK$250.65, which is **+14.1%** against the Owner's HK$219.60 cost. Against the last HK print I found (HK$230.80, 20 Nov) it is +5.1%.

---

## 10. Technical score: **75 / 100** (input to committee)

| Component | Weight | Score | Basis |
|---|---|---|---|
| Trend structure (weekly + daily, MA stack) | 40 | **36** | Both timeframes up; every MA rising; range breakout with a held retest |
| Momentum (RSI, MACD) | 20 | **13** | RSI 61.5 is healthy. The MACD histogram is negative after the 19 Nov cross, and there is a mild MACD/RSI lower high against August. |
| Volume | 20 | **16** | Up/down 1.61×, rising OBV, low-volume pullback. The 24 Nov rally was not volume-confirmed. |
| Location / risk-reward | 20 | **10** | 2% under the 52-week high (resistance); 26% above SMA200 (extended); the stop is 7.4% away |
| **Total** | 100 | **75** | |

**Confidence: moderate-high on direction, moderate on levels.**

What lowers it:
- this is a single-name biotech with 34% realised volatility, exposed to binary trial and regulatory news;
- the last 12 sessions are not independently verified;
- the HK line has three snippet prints and no series.

Charts describe probabilities, not certainties.

---

## 11. NOT OBTAINED register

- **6160.HK daily OHLCV series.** Webull has no HK bars. I have three snippet-level prints only (§6).
- **6160.HK closes for 23–25 Nov 2026**, and for Aug–Oct 2026. The latter are needed to close §7(a).
- **USD/HKD for 24 Nov 2026.** I used 7.84.
- **Independent confirmation of ONC closes, 9–24 Nov 2026.**
- **First-hand confirmation of the 2021 record close (US$403.14).** Secondary only.
- **Intraday data and volume-at-price.** Not available. Every stop here is close-basis by design.

---

## Sources

- Webull read-only daily bars, ONC, pulled 2026-11-25 (CSV path and hash in §0).
- [BeOne Q3 2026 results, SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001651308/000162828026070469/exhibit991-q32026earningsr.htm) (search extract; report date 5 Nov 2026, guidance US$6.9–7.0bn)
- [BeOne Form 8-K, 2026-04-14 (Boardroom Alpha mirror)](https://www.boardroomalpha.com/sec/onc-8-k-2026-04-14-0001651308-26-000008) (ADS = 13 ordinary shares)
- [Form 4, BeOne, June 2026 (StreetInsider)](https://www.streetinsider.com/SEC+Filings/Form++4++++++++++BeOne+Medicines+Ltd.++++++For:+Jun+08++Filed+by:+Wu+Xiaobin/26630946.html) (ratio footnote)
- [10jqka, HKEX announcement on the option grant, June 2026](https://stock.10jqka.com.cn/hks//20260621/c677595701.shtml) (US$270.52/ADS ≈ HK$163.14/share)
- [etnet 6160 quote](https://www.etnet.com.hk/www/sc/stocks/realtime/quote.php?code=6160) (HK$255.80, 12/11/2026 16:33, search snippet)
- [Halo Technologies 6160](https://www.halo-technologies.com/markets/shares/hkg/6160/) (HK$230.80, 20 Nov 2026, search snippet; fetch failed)
- [therighttrader.com USD/HKD](https://therighttrader.com/convert/usd-to-hkd) (7.84696, 17 Nov 2026); [MarketXLS USD/HKD](https://marketxls.com/indicators/usd-to-hkd-exchange-rate) (7.84, 6 Nov 2026)
- [Stockanalysis ONC](https://stockanalysis.com/stocks/onc/) (370.33, 30 Oct 2026); [Yahoo ONC](https://finance.yahoo.com/quote/ONC) (377.63, 23 Oct); [Investing.com ONC](https://uk.investing.com/equities/beigene) (406.96, undated)
- [MacroTrends ONC history](https://www.macrotrends.net/stocks/charts/ONC/beigene/stock-price-history), [CompaniesMarketCap](https://companiesmarketcap.com/beigene/stock-price-history/) (record close 403.14 on 2021-09-17, search extract)
- Prior firm report: `reports/technical/2026-08-14-6160hk-technical.md`

*Research and decision support only, not financial advice. No orders placed or proposed for
execution by this desk; the Owner alone executes (standing rules 1–2).*
