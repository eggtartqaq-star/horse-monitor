# AAPL — Apple Inc. — Financial Statement Analysis

**Analyst:** 巴爺爺 (Dept 2, Financial Statements) · **Date:** 2026-11-16 · **Coverage:** first Apple coverage in firm history
**Status:** IN PROGRESS — being filled incrementally.

Context (from caller, Webull 13-Nov-2026 close): price $356.27; P/E 39.7 on TTM EPS $8.98; P/S 10.8; P/B 46.2 (BVPS $7.71); shares outstanding 14.27bn. Owner cost $357.60.

**Data provenance.** sec.gov, apple.com and macrumors.com were all unreachable via WebFetch (DNS-blocked in this session). Every figure below is **search-extracted** (WebSearch summary of the cited page), not read from the filing itself. Treat as Tier-2 until someone with egress verifies against the FY2026 10-K.

## Raw data log (search-extracted)

### Q4 FY2026 (quarter ended 26-Sep-2026; released 2-Nov-2026) — search 1
- Revenue $114.5bn, +12% YoY [S1, S2]
- Gross margin 47.9%, incl. ~1pt favourable from **tariff refunds** [S2]
- Diluted EPS $2.10, +14%, incl. $0.05 from tariff refunds [S2]
- Net income $30.7bn (MacRumors headline) [S1]
- Operating cash flow ~$28bn for the quarter [S2]
- Dividend $0.27/share declared [S2]

### FY2026 full year (FYE 26-Sep-2026; 10-K) — searches 1–3
- Revenue $478.83bn, +15.1% [S4, S5]; net income $132.18bn [S4, S5]; diluted EPS $8.98 vs $7.46 FY2025 (+20.4%) [S5, S6]
- Segments: iPhone $254.1bn (+21%); Services $123.3bn (+13%, advertising & cloud cited); Mac $37.9bn (+13%); Wearables/Home/Acc $35.6bn (flat); iPad $27.9bn (flat) [S3, S4, S7]. Sum = $478.8bn — internally consistent.
- Greater China sales +28% FY2026 [S7]; one secondary source: China $82.4bn / 17.2% of revenue [S8] — basis unclear, low confidence.
- Total gross margin 48.8% (single secondary source) [S7]; Services GM 76% in Q3 FY2026 (quarterly only) [S7]
- Operating cash flow $145.097bn vs $111.482bn FY2025 (+30%) [S6]
- Capex ~ $9.0bn (single low-quality source, KuCoin blog citing 10-K — **unverified**) [S9]
- Buybacks: 297m shares for $85.8bn [S6]; dividends paid $15.7bn [S6]; new $100bn authorization April 2026 [S6]
- Apple dropped its formal "net cash neutral" target [S6]
- Implied diluted weighted shares = $132.18bn / $8.98 = **14.72bn** (derived)

## 1. Summary & grade
_pending_

## 2. Growth vs multiple (FY2022–FY2026)
_pending_

## 3. Profitability — margins, segment mix, ROE, ROIC
_pending_

## 4. The Google payment
_pending_

## 5. Buybacks, share count and EPS decomposition
_pending_

## 6. Cash generation — FCF, capex, conversion
_pending_

## 7. Balance sheet & debt
_pending_

## 8. China
_pending_

## 9. Accounting red flags
_pending_

## 10. Strongest case for / against
_pending_

## 11. Financial score
_pending_

## 12. NOT OBTAINED register
_pending_

## Sources
- [S1] MacRumors, "Apple Reports 4Q 2026 Results: $30.7B Profit on $114.5B Revenue", 2026-11-02 — https://www.macrumors.com/2026/11/02/apple-4q-2026-earnings/
- [S2] Apple Newsroom, "Apple reports fourth quarter results", 2026-11 — https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/ ; SEC 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000024/a8-kex991q4202609262026.htm
- [S3] Vested Finance, "Apple Q4 2026 earnings decoded" — https://vestedfinance.com/blog/us-stocks/apple-q4-2026-earnings-decoded/
- [S4] TradingView News, "Apple FY 2026: Revenue $478.83B, EPS $8.98 — 10-K Summary" — https://www.tradingview.com/news/tradingview:3fa053e38b41a:0-apple-fy-2026-revenue-478-83b-eps-8-98-10-k-summary/
- [S5] StockTitan, "Apple FY2026 profit rises to $132B on $479B sales" (10-K) — https://www.stocktitan.net/sec-filings/AAPL/10-k-apple-inc-files-annual-report-e8799a9bf72c.html
- [S6] MarketScreener, "Apple: Annual Report for Fiscal Year Ending September 26, 2026 (Form 10-K)" — https://www.marketscreener.com/news/apple-annual-report-for-fiscal-year-ending-september-26-2026-form-10-k-ce785fded98fff2d
- [S7] Apple Scoop, "Apple's 2026 annual report: 10 numbers worth knowing" — https://applescoop.org/story/apple-2026-10-k-annual-report-revenue-iphone-employees-key-numbers ; "How Apple makes money" — https://applescoop.org/story/how-apple-makes-money-revenue-by-product-iphone-services
- [S8] MetricsHour, AAPL revenue by country — https://metricshour.com/stocks/aapl/
- [S9] KuCoin blog, "Apple Dividend 2026" — https://www.kucoin.com/blog/apple-dividend-2026-payout-yield-buybacks (low-quality source)

---

<!-- provenance-stamp -->
## Provenance and coverage

*Appended by `scripts/stamp_provenance.py`. Records how this report was
produced, so its weight can be judged later without reconstructing the
conditions from memory.*

**Sourcing — direct page fetch was blocked.** In this environment every
direct page fetch returned HTTP 403 under an organisation egress policy
(verified against the proxy status endpoint; hosts denied included
`hkexnews.hk`, `finance.yahoo.com`, `stooq.com`, `alphavantage.co`,
`data.nasdaq.com`). **No primary filing or factsheet was opened.** Figures
here are search-engine extractions of those documents plus secondary
reporting. Treat structural claims (share structure, fee schedules, exact
line items) as lower confidence than headline financials, which were
generally cross-checked against two or more independent sources.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
