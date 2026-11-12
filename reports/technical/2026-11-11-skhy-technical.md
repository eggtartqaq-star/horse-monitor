# SKHY (SK hynix ADS, Nasdaq) — Technical Analysis & Trading-Plan Inputs

**Analyst:** 老詹, Technical Analysis (Dept 5)
**Date:** 2026-11-11
**Status:** DRAFT — skeleton on disk; sections filled incrementally (checkpointed)
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
PENDING-ARITHMETIC

## 3. Trend verdict and structure
PENDING

## 4. Key levels — support / resistance / invalidation
PENDING

## 5. Indicator readings & divergences
PENDING

## 6. Korean ordinary (000660.KS) as proxy for the history the ADS lacks
PENDING

## 7. Volume and the ADR–ordinary relationship
PENDING

## 8. Lock-up expiry as a dated supply event
PENDING

## 9. Trading-plan inputs for John and Zac
PENDING

## 10. Technical score (0–100) input to committee
PENDING

## 11. NOT OBTAINED register
PENDING

## 12. Sources
PENDING
