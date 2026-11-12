# SKHY (SK hynix ADS, Nasdaq) — Technical Analysis & Trading-Plan Inputs

**Analyst:** 老詹, Technical Analysis (Dept 5)
**Date:** 2026-11-11
**Status:** COMPLETE (v1, 2026-11-12). All sections filled; §7 premium shown as FX sensitivity pending a dated USD/KRW
**Nature:** Research only. Inputs for John (CRO) and Zac (sizing). Not a recommendation, not financial advice.

## 0. Honest constraints (read first)

1. **I have no market-data feed and drew no chart.** Direct page fetch is unavailable in
   this environment; every number below is quoted from a web-search snippet with the
   source's own date, or is arithmetic on such numbers (shown). Hosts that did not return
   usable data are listed in §11. `tradingkey.com` is blacklisted firm-wide and is not cited.
2. **This is a four-month chart.** SKHY has traded since 10 Jul 2026 (when-issued, ticker
   SKHYV) / 13 Jul 2026 (SKHY). That is roughly 85 sessions. **There is no 200-day moving
   average. There is no meaningful 50-day moving average until roughly 18 Sep, and even
   now it is a 50-day average of a distribution that includes the IPO pop.** I do not
   fabricate long-period indicators. Where the Korean ordinary (000660.KS) is used for
   structure the ADS lacks, it is labelled PROXY.
3. **Technical analysis does not forecast.** It describes where price has been accepted
   and rejected, and tells you where a view is wrong. Confidence is stated per call.
4. **The Owner's $129.00 entry is sunk.** It is not a support level, it is not a
   reference for "getting back to even", and it does not appear in any level table below
   except as a note on where the position sits. The plan is built off market levels only.
5. **The levels here are inputs for John (CRO) and Zac (sizing), not a recommendation.**
   Research only; not financial advice.

## 1. Price data: sources, conflict, and which series is internally consistent

### The conflict as briefed
- Google Finance / StockTitan: **$127.34 close on Thu 6 Nov 2026**.
- Investing.com: **$143.42 "on 11 Nov"** with a **prior close of $129.66**.

### Resolution (both are consistent; they are different dates)
The two figures are not competing closes for the same day. Search evidence dated 11 Nov:

| Item | Figure | Source (date) |
|---|---|---|
| 5 Nov (Thu) session | SKHY **−13.4%** ("bloodbath" in semis; NAND export-licence and data-centre regulation headlines) | Motley Fool, 5 Nov 2026 |
| 6 Nov (Fri) close | **$127.34** | BRIEF-SUPPLIED (Google Finance/StockTitan); not independently re-sourced |
| 10 Nov (Tue) close | **$129.66** (Yahoo "previous close", Investing.com "prior close") | Yahoo Finance quote page; Investing.com, 11 Nov 2026 |
| 11 Nov (Wed) intraday | **+10.1% to $142.68** (Benzinga movers); day range **$137.49–$144.77**, **+10.99%** (Yahoo); "nearly 9.9% in morning trading" (Investing.com); **$143.42** (Investing.com quote page) | Benzinga 11 Nov; Yahoo 11 Nov; Investing.com 11 Nov |
| 11 Nov catalyst | Memory-sector rally after CoreWeave Q3 beat and raised FY26 guidance; Seoul 000660 +7.2% on 11 Nov; Rosenblatt Street-high $400 PT cited | Benzinga; Investing.com; boerse-express, all 11 Nov |
| 10 Nov Seoul | 000660.KS **+6.69% to ₩1,212,000** regular-session close | Yahoo Finance article, 10 Nov 2026 |

**Verdict on the series:** the $127.34 (6 Nov) → $129.66 (10 Nov) → ~$143 (11 Nov intraday)
path is internally consistent. The 11 Nov print is **intraday / not a confirmed close as of
writing** — the session was open when these snippets were captured. The implied move from
the 10 Nov close is **+10.6% to $143.42** or **+10.1% to $142.68** depending on capture time.
It is real, it is sector-driven (Seoul moved +6.69% on 10 Nov *before* the US session and
+7.2% on 11 Nov), and it is **not** a company announcement — 修大哥 is confirming.

### The 52-week range as briefed ($122.20–$199.86) — partially unsupported
- **High $199.86: NOT SUPPORTED by any source found.** The sourced all-time high is
  **$194.80 intraday on Tue 14 Jul 2026** (O $168.11 / H $194.80 / L $165.50 / C $193.92,
  +27.29%, 72.65M ADS; Benzinga year-range also shows $194.80). A separate aggregator shows
  $193.91. I use **$194.80 / close $193.92** and treat $199.86 as an unverified vendor
  figure (possibly an extended-hours print or a bad tick).
- **Low $122.20: plausible but not dated by any source.** Other vendors show $126.80,
  $128.29, $124.80, and a 30-day range low of **$120.35**. All of these cluster in the
  first week of November after the 5 Nov −13.4% session. I treat the **all-time low zone as
  $120–$123, printed between 5 and 10 Nov 2026**, exact date NOT OBTAINED.

## 2. ADS price history, dated (IPO to today)

All prices USD per ADS (1 ADS = 1/10 ordinary share). Closes unless stated.

| Date | Event / price | Source |
|---|---|---|
| 9 Jul 2026 | Prospectus date. Priced **$149.00**; 177.9M ADS; $26.5bn raised (largest ADS deal on record) | IPOScoop; fnnews; Al Jazeera |
| 10 Jul (Fri) | First trade as **SKHYV** (when-issued). Open **$170**, intraday high **$177**, close **$168.01 (+12.76%)**; Herald shows $168.49. Volume ~107.7M | IPOScoop; Morningstar; Korea Herald; Edaily |
| 13 Jul (Mon) | Permanent ticker **SKHY**. **−9.32%** (profit-taking; Seoul shares post biggest one-day fall in ~two decades, attributed to ADR-event unwind and leverage liquidation). Computed close ≈ **$152.35**. Volume ~57.3M | Asianet; Advisor Perspectives/Bloomberg; Edaily |
| 14 Jul (Tue) | **All-time high.** O $168.11 / H **$194.80** / L $165.50 / C **$193.92 (+27.29%)**, 72.65M ADS. ADR premium to Seoul briefly **52.5%**. After-hours $190.50 (−1.76%) | historicaloptiondata price table; Webull/Benzinga Pro; Edaily |
| 15 Jul | Close **$176.46** (−9.0%). Volume ~76.3M | historicaloptiondata; Edaily |
| 23 Jul | ADR ~30% above domestic shares | Korea Herald |
| 4 Aug | Close **$154.38** | historicaloptiondata |
| 24 Aug | 000660.KS ₩1,759,000 (prev ₩1,730,000) — PROXY | Eulerpool |
| 27 Aug | Close **$161.61** | HDFC Sky |
| 4 Sep | **+8.1% to $177** | search summary (247wallst / webull cluster), 4 Sep |
| two weeks to 30 Sep | Avg volume ~**20M ADS/day**, >$3.5bn/day notional (implies ~$175 average price) ; ADR premium ~**41%** | Asia Times, Oct 2026 |
| 7–8 Oct | **90-day lock-up expiry** (company/affiliates/management) — see §8 | Briefs.co 7 Oct; Barchart via Webull |
| 20 Oct | Close **$139.79**, volume 15.77M ("below average") | Schwab quote, as of 20 Oct |
| 26 Oct | **$142.62** | MarketChameleon, 26 Oct |
| 28 Oct | Q3 2026 record results + ₩20tn buyback (29 Oct–28 Jan 2027). 000660.KS **+10.89% to ₩1,487,000**; KOSPI 6,012 (+6.63%) — PROXY | mt.co.kr 28 Oct; Korea Times 28 Oct |
| 30 Oct | Close **$149.21 (−7.9%)** ⇒ computed 29 Oct close ≈ **$162.0** | debelegger.nl, as of 30 Oct |
| 5 Nov (Thu) | **−13.4%** (semis sell-off; NAND China export-licence hold; data-centre regulation fears; MU −7.0%, SNDK −7.9%, NVDA −3.2% overnight) | Motley Fool 5 Nov; Yonhap 5 Nov |
| 6 Nov (Fri) | Close **$127.34** | BRIEF-SUPPLIED |
| 5–10 Nov | **All-time low zone $120.35–$122.20** (vendor figures; exact date NOT OBTAINED) | multiple aggregators |
| 10 Nov (Tue) | Close **$129.66**. Seoul +6.69% to ₩1,212,000 | Yahoo; Investing.com |
| 11 Nov (Wed) | Intraday **$137.49–$144.77**; last seen **$142.68–$143.42 (+10.1% to +10.99%)**. Session not confirmed closed at time of writing | Benzinga; Yahoo; Investing.com |

### Arithmetic on the path (computed)

| Computation | Result |
|---|---|
| 13 Jul close (168.01 × (1−0.0932)) | ≈ $152.35 |
| 29 Oct close (149.21 ÷ 0.921) | ≈ $162.0 |
| ATH close $193.92 → 10 Nov close $129.66 | **−33.4%** |
| ATH → 11 Nov ~$143.42 | −26.4% |
| IPO $149 → 10 Nov / 11 Nov | −13.0% / −3.7% |
| First-day close $168.01 → 11 Nov | −14.6% |
| Owner entry $129.00 vs ATL $122.20 / $120.35 | entry is **+5.6% / +7.2%** above the low |
| Owner entry vs 11 Nov ~$143.42 | position +11.2% (intraday, unconfirmed) |

**What "within ~6% of the all-time low" means:** the Owner bought near the bottom of a
17-week range, *after* a −33% drawdown from the ATH. **What it does not mean:** that the
low is a floor. A four-month-old listing has no history below $120; there is nothing on the
ADS chart that "should" hold there. The Korean ordinary (§6) is the only place to look for
older support, and that is a proxy.

## 3. Trend verdict and structure

**Primary (weekly, 17 weeks of data — too short for a weekly read of any confidence): DOWNTREND.**
**Intermediate (daily): DOWNTREND with a one-session reversal off the all-time low. Not yet a base.**

Evidence (all from §2):
- **Lower highs:** $194.80 (14 Jul) → ~$177 (4 Sep) → ~$162 (29 Oct).
- **Lower lows:** ~$152 (13 Jul) → ~$140 (20 Oct) → $120–122 (5–10 Nov).
- **Failed breakout at the IPO price:** on 28–29 Oct, record Q3 results and a ₩20tn buyback
  lifted the ADS to ~$162, *above* the $149 IPO price. It was back at $149.21 the next
  session (30 Oct) and lost $149 within days, then printed the ATL on 5–10 Nov. A level
  reclaimed on the best news of the quarter and surrendered inside a week is a **failed
  breakout**, and it marks $149 as supply, not support.
- **11 Nov:** +10% from $129.66 to ~$143, sector-driven (CoreWeave guidance, Seoul +7.2%).
  One session. It has retraced roughly half of the 29 Oct→ATL decline (50% = $142.1,
  computed). It does **not** by itself create a higher low; the first higher low would be a
  pullback that holds above $129.66 and then exceeds the 11 Nov high ($144.77).

**Is it a post-IPO base?** Not yet. A base requires (i) a low that has been re-tested and
held, and (ii) a higher low. We have a low tested once (the 5–10 Nov cluster) and a bounce.
That is the *first condition for* a base, not a base.

**Moving averages:** no 200-day exists. A 50-day (sessions ~1 Sep–11 Nov) would sit roughly
in the $150s given the Sep ~$175 → Oct ~$140–162 → Nov ~$120–143 path — i.e. **price is
below the 50-day and the 20-day** (which spans ~14 Oct–11 Nov, roughly $140–150 average).
Both are **estimates from the dated points in §2, not computed from a full series** — I do
not have one. Direction of travel on both is down.

**What changes the read:**
- **Bearish read invalidated (turns neutral/constructive):** a daily close above **$152.35**
  (13 Jul close; first post-IPO support) — that would mean price is back above the IPO
  price *and* the first-week floor, and the 29 Oct failure is being repaired. Trend reversal
  proper requires a close above **$162** (last lower high).
- **Constructive read (low is in) invalidated:** daily close below **$120.35** — see §4.

## 4. Key levels — support / resistance / invalidation

Fibonacci grids (computed, §2 arithmetic): full range $122.20→$194.80: 23.6% $139.33 ·
38.2% $149.93 · 50% $158.50 · 61.8% $167.07 · 78.6% $179.26. Oct–Nov swing $162.0→$122.20:
38.2% $137.4 · 50% $142.1 · 61.8% $146.8.

### Resistance (nearest first)
| Zone | Why it matters | Tested? |
|---|---|---|
| **$144.77** | 11 Nov intraday high | Current session; unconfirmed |
| **$146.8–$149.9** | 61.8% of the Oct–Nov swing + **IPO price $149.00** + 38.2% of the full range + 30 Oct close $149.21 | **Yes — failed from above 30 Oct–early Nov.** Supply: every IPO allottee is flat here. Highest-conviction level on the chart |
| $152.35 | 13 Jul close, first post-IPO low | Was support in Jul; became resistance after it broke (date NOT OBTAINED, between Aug and Oct) |
| $158.5–$162.0 | 50% of full range + 29 Oct post-earnings high close (last lower high) | Rejected 29–30 Oct |
| $167–$168.5 | 61.8% of full range + first-day close ($168.01/$168.49) + 14 Jul open $168.11 | Held as support 15 Jul–Aug (closes $176, $154 — i.e. broke by 4 Aug) |
| $176–$177 | 15 Jul close $176.46; 10 Jul intraday high $177; 4 Sep $177 | Rejected 4 Sep (lower high) |
| $194.80 / $193.92 | ATH intraday / close, 14 Jul | Once |

### Support (nearest first)
| Zone | Why it matters | Tested? |
|---|---|---|
| **$137.4–$139.8** | 38.2% of Oct–Nov swing; 23.6% full range; 20 Oct close $139.79 (prior low that broke); 11 Nov day low $137.49 | Broke as support early Nov; reclaimed 11 Nov intraday. Needs to hold on a close to matter |
| **$127.3–$129.7** | 6 Nov close $127.34 and 10 Nov close $129.66 — the **launch zone of the 11 Nov impulse** | Held once (10 Nov → 11 Nov) |
| **$120.35–$122.20** | All-time low cluster, 5–10 Nov (vendor figures; exact date NOT OBTAINED) | Tested once, held once |
| below $120 | **No ADS history.** Only proxy levels (§6) | — |

### INVALIDATION — pre-committed, not to be revised after the fact
**Level: a daily close below $120.35 (the lowest vendor print of the Nov low cluster).
Early warning: any intraday trade below $122.20.**

**Rationale (same discipline as prior calls — the launch point of the impulse):** the
constructive read is "the ATL zone has held at first test and the 11 Nov impulse launched
from $129.66 off that floor." The impulse's launch area is $127–$130; its floor is the ATL
cluster. If price closes below the lowest print of that cluster, the floor did not hold,
the impulse has been fully retraced, and the ADS is in **price discovery below any level
it has ever traded** — there is no technical argument left to hold against. At that point
I log the view as stopped out in this file and the committee should treat the ADS as
trendless-down with only Korean-proxy levels beneath.

Why not $129.66 (tighter)? Because a 1-day-old close on a +10% gap day is noise-prone; the
11 Nov range alone was $7.28 wide (5.6%). A stop inside normal daily range is a coin flip,
not a level. Why not lower (e.g. a round $115)? Because nothing on the ADS chart exists
there; a stop must sit at a level price has actually respected.

**Confidence in these levels: LOW-TO-MODERATE.** 85 sessions, dated closes only, no full
series, and a vendor-sourced low. $146.8–$149.9 is the one level with high confidence
(three independent reasons plus observed rejection).

## 5. Indicator readings & divergences

**RSI (14-day), MACD: NOT OBTAINED as computed values.** I have no daily series to compute
them and found no dated third-party reading in search results. What the dated closes
support qualitatively:
- A −13.4% day (5 Nov) into a new ATL after a −33% drawdown would have pushed a 14-day RSI
  into oversold territory (<30) on 5–6 Nov; the +10% session of 11 Nov will have snapped it
  back toward the 40s. This is inference from the price path, **not a reading**.
- **Divergence check:** price made a lower low in Nov vs the 20 Oct low ($139.79). Whether
  RSI made a higher low (bullish divergence) is NOT OBTAINED — it would require the series.
  If 修大哥/賭馬狗 can pull a 14-day RSI for 20 Oct vs 6 Nov, a higher RSI low at the lower
  price low would materially strengthen the base case; a lower RSI low would not.
- MACD will be below zero and below signal at the 10 Nov close given a month of lower
  closes; 11 Nov is at most the first up-tick in the histogram. Again inference, not reading.
- A broker-sourced "Soars 5.00% … oversold rebound" headline (iTiger, undated) corroborates
  that at least one vendor's oversold flag was triggered in early Nov; date NOT OBTAINED.

Nothing here contradicts the price read in §3; nothing confirms a reversal either.

## 6. Korean ordinary (000660.KS) as proxy for the history the ADS lacks

Ratio: **1 ADS = 1/10 ordinary share** (prospectus; Korea Times; iTiger). Implied ADS
value = (000660 price ÷ 10) ÷ USD/KRW.

Dated proxy points found (closes, ₩):
| Date | 000660.KS | Note |
|---|---|---|
| 24 Aug 2026 | 1,759,000 (prev 1,730,000) | Eulerpool |
| 28 Oct 2026 | 1,487,000 (+10.89%) | Q3 record results; mt.co.kr |
| 9 Nov 2026 | ≈ 1,136,000 (computed: 1,212,000 ÷ 1.0669) | — |
| 10 Nov 2026 | 1,212,000 (+6.69%) | Yahoo Finance article |
| 11 Nov 2026 | +7.2% intraday/close ⇒ ≈ 1,299,000 (computed) | boerse-express |

Proxy drawdown 24 Aug → 10 Nov: **−31.1%** (computed). The ordinary fell *more* than the
ADS over the same window (ADS 27 Aug $161.61 → 10 Nov $129.66 = −19.8%). **The ADS has
been the stronger leg, not the weaker one** — see §7 on premium.

Longer-dated 000660 structure (ATH date/level, 200-day MA, multi-year supports in ₩):
**NOT OBTAINED** in this session — search snippets returned conflicting undated quotes
(₩331k to ₩1.85m) which I will not use. Morgan Stanley cut its target to ₩1.6m (11 Nov);
that is a broker target, not a technical level. The ₩20tn buyback (29 Oct 2026 – 28 Jan
2027) is a **dated demand programme** on the ordinary; it supports the proxy's downside
mechanically but says nothing about the ADS premium.

## 7. Volume and the ADR–ordinary relationship

### Volume (ADS, dated)
| Date | Volume | Source |
|---|---|---|
| 10 Jul | ~107.7M | Edaily |
| 13 / 14 / 15 Jul | 57.3M / 72.65M / 76.3M | Edaily; price table |
| two weeks to 30 Sep | ~20M/day average (>$3.5bn notional/day) | Asia Times |
| 20 Oct | 15.77M, "below average" | Schwab |
| Nov (incl. 5 Nov −13.4% and 11 Nov +10%) | **NOT OBTAINED** | — |

Volume decayed from ~100M to ~20M to ~16M/day over three months — normal post-IPO decay,
but it means the Nov moves happened on a thinner book than the Jul moves. Whether 5 Nov
and 11 Nov were high-volume (climactic/confirming) days is exactly the datum I most want and
do not have.

### ADR premium to the ordinary (the question the coordinator asked)
Premium = SKHY × USDKRW ÷ (000660 ÷ 10) − 1. Dated figures from sources: **52.5%** (14 Jul,
peak); ~30% (23 Jul); ~33% (undated, Jul/Aug); **~41%** (late Sep, Asia Times "Americans pay
41% more"). ADS conversion quota reported exhausted (Webull/KSD), which is why the premium
does not arbitrage away.

**Computed premium at the 10 Nov close under a USD/KRW sensitivity (FX NOT OBTAINED):**

| USD/KRW assumed | Premium at 10 Nov close (SKHY $129.66 vs ₩121,200/ADS) | Premium late Aug (SKHY $161.61 vs ₩175,900/ADS, 24–27 Aug) |
|---|---|---|
| 1,350 | 44.4% | 24.0% |
| 1,380 | 47.6% | 26.8% |
| 1,400 | 49.8% | 28.6% |
| 1,430 | 53.0% | 31.4% |
| 1,460 | 56.2% | 34.1% |

**Finding: the premium has NOT compressed. Under any plausible FX it is ~44–56% at the
10 Nov close, versus ~41% in late September and ~24–34% in late August.** The late-Aug
row reproduces the sourced "~30%" figure, which gives me some confidence the method is
right. Therefore **premium compression does not explain the ADS drop from ~$162 to $127;
the ordinary fell further (−31% from 24 Aug) and the ADS fell less (−20%).** The decline is
Korea-side / sector-side, not an ADR-structure unwind. The corollary is the uncomfortable
one: **the premium is a latent supply overhang of ~45–55% that the ADS has not yet paid**
— if the KSD conversion quota reopens, or if Seoul rallies faster than New York, the ADS
can underperform the ordinary by that margin without any change in fundamentals. That is a
structural risk John should price, and it is the strongest argument against treating the
ADS as a clean proxy for the business.

### Does the ADS lead or follow Seoul?
Evidence is mixed and I will not over-read it:
- 10 Jul debut pop (+12.8%) **led** Seoul's 13 Jul record one-day fall (the "ADR event"
  unwind) — the ADS led on that occasion.
- 10 Nov: Seoul +6.69% in its session; SKHY closed only $129.66 (vs $127.34 on 6 Nov; 9 Nov
  close NOT OBTAINED). 11 Nov: Seoul +7.2%, then SKHY +10% — Seoul **led** on this pair.
- With ADS volume at ~16–20M/day (~$2–3bn notional) versus the ordinary's position as >20%
  of KOSPI, the Korean session is the price-setter for value and the ADS adds a US-tech-
  session overlay (CoreWeave, MU, NVDA). Practical rule: **check 000660's close before the
  US open; the ADS rarely fights it, but it adds a sector beta on top.**

## 8. Lock-up expiry — a dated supply event that is BEHIND us, not ahead

**Correction to the brief:** sources consistently describe a **90-day** lock-up (company,
affiliates, management; subject to exceptions) from the **9 Jul 2026 prospectus date**,
expiring **Wed 7 Oct / Thu 8 Oct 2026** (Briefs.co 7 Oct: "expires Wednesday"; Barchart via
Webull: 8 Oct). I found no source supporting 180 days / 9 Jan 2027. The exact day should be
confirmed against the 424(b)(4) — flagged to 修大哥 — but the quarter is not in doubt.

**What the tape did into and through it (dated points only):**
| Date | ADS | Note |
|---|---|---|
| 4 Sep | ~$177 | post-Aug high |
| two weeks to 30 Sep | ~$175 avg (implied from $3.5bn/20M) | still elevated, premium ~41% |
| 7–8 Oct | expiry | price on the day NOT OBTAINED |
| 20 Oct | $139.79, vol 15.8M "below average" | **−20% from late Sep** in ~3 weeks |
| 26 Oct | $142.62 | |

Reading: the ADS lost roughly a fifth of its value across the expiry window, on *declining*
volume. That pattern (price down, volume not expanding) is more consistent with **buyers
stepping back ahead of expected supply** than with heavy insider selling actually hitting
the tape — but I cannot distinguish the two without daily volume for 1–15 Oct, and the
Korean ordinary was also weak in the period (24 Aug ₩1.76m → 28 Oct ₩1.49m pre-earnings
bounce). I do not attribute the Oct decline to the lock-up alone.

**Is there a later tranche?** NOT OBTAINED. No source mentions a second lock-up date. Two
*other* dated supply/demand items are relevant instead:
1. **ADS conversion quota (KSD):** reported exhausted. If re-opened or enlarged, arbitrage
   supply hits the ADS and the ~45–55% premium compresses. **No date; the single largest
   structural risk to the ADS specifically.**
2. **₩20tn treasury-share buyback, 29 Oct 2026 – 28 Jan 2027:** dated demand on the
   *ordinary*. Supports the proxy; does not touch the ADS premium.

**Positioning rule now that expiry is behind us:** there is no calendar supply cliff to
trade around in Q4; the risk is event-driven (quota) rather than dated. Treat any sudden
*narrowing* of the premium without a Seoul rally as the signal that the conversion valve
has opened — that is a reduce trigger for the ADS specifically, regardless of chart level.

## 9. Trading-plan inputs for John (CRO) and Zac (sizing)

**These are inputs, not a recommendation. Whether to add, reduce or hold is a committee
and Owner decision; sizing is Zac's; limit compliance is John's.** The $129.00 cost basis
does not appear in any level below by design.

### (a) Where an add (average-down) has a technical justification — and where it does not
- **Justified zone: $127.3–$130.0**, i.e. a pullback to the launch zone of the 11 Nov impulse
  (6 Nov close $127.34, 10 Nov close $129.66), **provided the pullback holds above $122.20
  intraday**. Risk to the invalidation close ($120.35) from $128.50 is ~6.3% — a defined,
  modest stop distance for a name with 5–13% daily ranges. This is where risk/reward is
  asymmetric: ~6% to invalidation vs ~15% to the first serious resistance ($147–150).
- **Not justified: chasing at $140–145** after a +10% session into the $146.8–$149.9
  supply zone; stop distance to $120.35 is ~16%, reward to the same resistance is ~4%.
- **Not justified: below $120.35.** That is the invalidation, not a bargain. An add there
  is averaging into a failed base — the classic averaging-down error.
- Confidence that the $127–130 zone holds on a re-test: **moderate-low** (one prior test).

### (b) Where to reduce
- **First reduce zone: $146.8–$149.9** (61.8% of the Oct–Nov swing + IPO price + 38.2% of
  the full range + the 30 Oct failure point). Highest-confidence level on the chart. Unless
  and until there is a **daily close above $152.35**, this zone is where a tactical trim of a
  position bought near the lows has the best evidence behind it.
- **Second reduce zone: $158.5–$162.0** (50% of full range + 29 Oct last lower high). A
  close above $162 is the trend-reversal line; *below* it, this zone is still a sell-the-rip
  level in a downtrend.
- **Event trigger (level-independent):** ADR premium narrowing sharply while Seoul is flat
  or up — see §8 item 1 — is a reduce signal for the ADS leg specifically.

### (c) The stop
- **Hard: daily close below $120.35.** Warning: intraday below $122.20.
- Logged here on 2026-11-11/12 and will not be moved lower. If hit, I record the stop-out in
  this file and the base thesis is dead until a new low is established and re-tested.

### (d) What a re-test of $149 would and would not prove
- **Would prove:** the ADS has retraced ~62% of the Oct–Nov decline; the Nov low has, for
  now, functioned as a floor; the IPO cohort's break-even is being tested from below.
  A **daily close above $152.35** on that attempt would prove the 30 Oct failure is repaired
  and would flip my read from downtrend to range ($122–$162).
- **Would NOT prove:** that the primary downtrend has reversed (needs close >$162 *and* a
  higher low above $129.66); that the premium overhang has gone (§7); that Seoul agrees
  (check 000660 vs its own 28 Oct level ₩1,487,000 — if the ADS re-tests $149 while the
  ordinary is still well below ₩1.49m, the move is premium expansion, which is fragile).
- A re-test that **fails** at $147–150 for a second time, after the 30 Oct failure, would
  establish a confirmed lower-high sequence and raise the odds of a re-test of $120–122.

### Summary table for Zac
| Input | Level | Basis |
|---|---|---|
| Add zone (if committee wants to add at all) | $127.3–$130.0, holding >$122.20 | Impulse launch zone |
| Do-not-chase line | above ~$140 | <4% to resistance, >16% to stop |
| Reduce 1 | $146.8–$149.9 | IPO price + fib confluence + Oct failure |
| Reduce 2 | $158.5–$162.0 | 50% fib + last lower high |
| Hard stop | daily close < $120.35 | ATL cluster floor |
| Trend-reversal confirmation | daily close > $162.0 | Last lower high |
| Range-read confirmation | daily close > $152.35 | 13 Jul floor reclaimed |

## 10. Technical score (0–100) input to committee

**Score: 35 / 100. Confidence in the score: LOW-TO-MODERATE.**

| Component | Read | Contribution |
|---|---|---|
| Primary trend | Down (lower highs 194.8→177→162; lower lows 152→140→121) | strongly negative |
| Position vs MAs | Below estimated 20d and 50d; no 200d exists | negative |
| Structure | Failed breakout of IPO price on best news of the quarter (29–30 Oct) | negative |
| Setup | ATL held at first test; +10% impulse off $129.66; ~50% retrace of Oct–Nov leg | positive, one session only |
| Proxy | Ordinary −31% from 24 Aug; ₩20tn buyback live to 28 Jan | mixed; buyback mildly positive |
| ADR structure | Premium ~45–55%, not compressing; quota shut | negative overhang |
| Volume | Decaying; Nov volume unknown | cannot confirm either way |
| Data quality | Dated closes, no series, vendor-sourced low | discount applied |

Score of 35 means: the chart does not support initiating here on technicals alone (which
this firm does not do anyway); it supports *holding an existing fundamentally-justified
position with a hard stop at the ATL floor and trimming into $147–150*. A close above
$152.35 would move the score to ~50; above $162 to ~60; a close below $120.35 to ≤20 and
the view is logged as stopped out.

## 11. NOT OBTAINED register

| Item | Status |
|---|---|
| Daily OHLCV series for SKHY (any window) | NOT OBTAINED — no feed; fetch blocked |
| Confirmed **11 Nov close** | NOT OBTAINED at time of writing (intraday $142.68–$143.42 only) |
| **9 Nov close** | NOT OBTAINED |
| Exact **date and intraday value of the all-time low** ($120.35 / $122.20 / $124.80 / $126.80 / $128.29 vendor conflict) | NOT OBTAINED |
| Independent confirmation of **$127.34 (6 Nov)** | NOT OBTAINED — brief-supplied only |
| Source for **$199.86** high | NOT OBTAINED — unsupported; $194.80 (14 Jul) used |
| **USD/KRW** on 10–11 Nov 2026 | NOT OBTAINED — premium shown as FX sensitivity |
| SKHY price and volume on **7–8 Oct** (lock-up expiry) and daily volume 1–15 Oct | NOT OBTAINED |
| **Any later lock-up tranche** | NOT OBTAINED — none mentioned in any source |
| Exact lock-up day (7 vs 8 Oct) per 424(b)(4) | NOT OBTAINED — 修大哥 confirming |
| **Nov daily volume** (5 Nov, 11 Nov especially) | NOT OBTAINED |
| **Computed RSI(14), MACD**, 20d/50d MA values | NOT OBTAINED — MA levels given are estimates from dated closes |
| RSI divergence 20 Oct vs 6 Nov | NOT OBTAINED |
| 000660.KS ATH date/level, 200-day MA, multi-year ₩ supports | NOT OBTAINED — conflicting undated quotes rejected |
| Date the ADS first closed below $149 (stockhub.kr headline exists; date not captured) | NOT OBTAINED |
| KSD conversion-quota size (2.5% vs 25% figures conflict) and any re-opening date | NOT OBTAINED |
| TIKR "down 57% from high" (8 Nov) — does not reconcile with either ADS or ordinary path | UNRECONCILED; not used |
| Order-flow / short interest / options skew | NOT OBTAINED — 王老吉 / C朗 scope |

### Blocked / unusable hosts this session
Direct page fetch unavailable for all hosts (environment constraint; not attempted around).
`tradingkey.com` — blacklisted, not cited. Price pages that surfaced but returned only
undated or mutually-contradictory snapshots and were **not relied on**: valueresearchonline,
chartmill, upstox, eulerpool (except the dated 24 Aug quote), stockopedia, tradersunion,
halo-technologies, stock-screener.org, wallstreetnumbers, metirai.

## 12. Sources
IPO pricing / first day: iposcoop.com (The IPO Buzz, 10 Jul 2026); morningstar.com "SK Hynix stock surges in US IPO"; koreaherald.com/article/10804704; en.fnnews.com 202607121534305943; aljazeera.com 10 Jul 2026; en.edaily.co.kr eda202607095506 (lock-up 90 days, prospectus 9 Jul). ·
ATH / Jul path: historicaloptiondata.com (SKHY price table, 14–15 Jul, 4 Aug); kr.benzinga.com/quote/SKHY/report (year range $128.29–$194.80); webull.com news (after-hours $190.50); newsable.asianetnews.com (−9.32% 13 Jul); advisorperspectives.com 13 Jul 2026 (Seoul record plunge). ·
Aug–Oct: hdfcsky.com (27 Aug $161.61; 52w $124.80–$194.80); asiatimes.com Oct 2026 ("41% more", 20M/day); schwab.wallst.com SKHY (20 Oct $139.79, 15.77M); marketchameleon.com/Overview/SKHY (26 Oct $142.62); debelegger.nl SKHY.US (30 Oct $149.21 −7.9%); briefs.co/?p=24801 (7 Oct lock-up); webull.com/news/15702155852596224 (Barchart, 8 Oct). ·
Earnings / Seoul: mt.co.kr 28 Oct 2026 (₩1,487,000 +10.89%); koreatimes.co.kr 28 Oct 2026 (KOSPI 6,012; ₩20tn buyback dates); eulerpool.com 000660 (24 Aug ₩1,759,000). ·
Nov: fool.com 5 Nov 2026 ("Why SK hynix plunged today", −13.4%); Yonhap via communicationstoday (5 Nov); finance.yahoo.com article (10 Nov, ₩1,212,000 +6.69%); benzinga.com movers 11 Nov 2026 (+10.1% to $142.68); finance.yahoo.com/quote/SKHY (day range, prev close $129.66); investing.com/equities/sk-hynix-adr and "Why is SK hynix stock surging today" (11 Nov); boerse-express.com 11 Nov (Seoul +7.2%; MS target ₩1.6m); tikr.com blog (8 Nov, unreconciled). ·
ADR structure: koreatimes.co.kr 14 Jul 2026 (premium narrowing; 1/10 ratio); itiger.com/news/2654305994 (premium mechanics); webull.com/news/15275858794718208 (conversion quota exhausted); biz.heraldcorp.com/article/10817183 (30% premium, custody limit).
