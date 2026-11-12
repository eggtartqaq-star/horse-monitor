# SKHY (SK hynix Inc. ADS) — Financial Statement Analysis

**Analyst:** 巴爺爺, Financial Statements, Dept. 2 (Equity Research)
**Date:** 2026-11-11 (completed 2026-11-12 after two session interruptions)
**Status:** COMPLETE. No `[PENDING]` markers remain.
**Instrument:** SKHY (Nasdaq ADS, 1 ADS = 0.1 common share of 000660.KS; 10 ADS = 1 share). Priced 2026-07-09 at US$149/ADS, first trade 2026-07-10. Owner cost basis US$129/ADS.
**Latest data:** 3Q26 (quarter ended 2026-09-30), preliminary results released 2026-10-28. **Data is 15 days stale.** The 3Q26 quarterly report (분기보고서 / 6-K) with full balance sheet and cash-flow statement was **not located**; balance-sheet detail below is therefore 1H26 (as of 2026-06-30, ~4.5 months stale) except where the 3Q26 release gave a figure. 4Q26 results expected late Jan 2027.
**Sourcing note:** Direct page fetch unavailable this session; sec.gov, finance.yahoo.com, stockanalysis.com blocked; tradingkey.com blacklisted and not cited. **No primary filing (F-1, 424B4, 6-K, DART report, IR deck) was readable.** Every figure below is a **search-result extraction** from company press releases as relayed by the financial press, or from earnings-call summaries. Items I could not confirm are marked **unverified**. USD conversions, where given, use **₩1,523.5/US$ — the rate used in 29 Jul 2026 press conversions of 2Q26 results ([Quartz](https://qz.com/sk-hynix-q2-2026-earnings-record-profit-misses-estimates-072926)); the Nov 2026 rate was not obtained.** Treat all USD figures as approximate.

**Existing firm coverage used:** `reports/industry/2026-08-21-msft-industry.md` (DRAM pricing +275–300% 2025→2027; HBM margins 2–3x DDR5 — **the second claim is now contradicted, see §2**); `reports/equity/2026-07-18-mu-financials.md` (MU graded B+; same cycle, same measurement problems).

---

## Summary & Grade

SK hynix is reporting numbers that have no precedent in memory history: **3Q26 revenue ₩104.6tn, operating profit ₩83.3tn, operating margin 80%** ([SK hynix newsroom, 2026-10-28](https://news.skhynix.com/en/q3-2026-business-results/)). Nine-month 2026 operating profit (~₩181.5tn, my sum of the three preliminary releases) is **3.8x all of 2025 and 8.7x the 2018 record year**. The balance sheet is pristine — **₩114.5tn cash, ₩15.8tn borrowings, ₩98.7tn net cash** at 30 Sep 2026 ([Korean Center/Yonhap](https://www.koreancenter.or.kr/news/articleView.html?idxno=1430914)) — capex has been held near 55% of operating cash flow, operating cash flow exceeds net income, and the company is returning ~₩100tn to shareholders in 2026.

The problem is not the quality of the statements. It is what the statements measure. The company's own history says that **13% of peak operating profit survived the 2018→2019 downturn, and less than zero survived 2021/22→2023** (§8). The current 80% margin is being driven primarily by **commodity DRAM pricing, not by HBM** — TrendForce estimates HBM per-wafer profitability actually fell *below* 64GB DDR5 RDIMM in 1Q26 ([TrendForce](https://www.trendforce.com/news/2026/07/22/news-sk-hynix-set-to-post-record-operating-margin-in-q2-as-hbm-mix-weighs-on-asp-growth-and-ltas-gain-focus/)). That makes today's margin *more* cyclical than the HBM narrative implies, not less. Long-term agreements (LTAs) with deposits covering >50% of 2027–28 capacity are the structural mitigant; their floor prices are undisclosed.

**Fundamentals quality grade: B+ (72/100).** Current statements in isolation: A− (~88). Cycle-position haircut: −16. **Roughly 60% of what makes these statements look excellent today is price (cycle position), not structure.** If the next trough resembles 2023, the forward grade is C; if it resembles 2019 with LTA floors holding, B.

**The 3 numbers that matter:**
1. **13% and <0%** — the share of peak operating profit that survived the last two troughs (2018→19: ₩20.84tn → ₩2.7tn; 2021→23: ₩12.41tn → –₩7.73tn). The holder at $129 is underwriting that this time the floor is higher. Nothing in the historical record proves it; the LTAs are the only new evidence.
2. **80% → 49% → 35%** — 3Q26 operating margin vs FY2025 vs FY2024. Most of the increment above ~50% is commodity DRAM ASP (3Q26 DRAM ASP +high-20s% q/q on only ~10% bit growth per call summaries), and TrendForce has HBM per-wafer profitability *below* DDR5 RDIMM as of 1Q26.
3. **₩98.7tn net cash, capex ≈ 55% of OCF (2024–25), inventory +25.9% in 1H26** — the balance sheet can absorb a 2023-style trough and still fund the ₩1,100tn multi-year fab plan; inventory is the line to watch and it has started to rise in won terms, though not yet relative to sales.

---

## 1. The cycle — quarterly revenue, operating profit, operating margin (KRW)

All figures KRW trillion, K-IFRS consolidated, from company quarterly releases as relayed by press. Quarterly figures are preliminary at release; annual figures from the January release of the following year.

| Quarter | Revenue (₩tn) | Operating profit (₩tn) | OP margin | Note / source |
|---|---|---|---|---|
| 4Q21 | — | 4.22 | — | prior-cycle quarterly peak ([storagenewsletter 4Q21](https://www.storagenewsletter.com/2022/02/02/sk-hynix-fiscal-4q21-financial-results/)) |
| 1Q22 | — | 2.86 | 24% | ([storagenewsletter 1Q22](https://www.storagenewsletter.com/2022/04/29/sk-hynix-fiscal-1q22-financial-results/)) |
| 3Q22 | — | 1.66 | — | ([startuprecipe/PRN 4Q22](https://en.startuprecipe.co.kr/archives/pr-newswire/sk-hynix-reports-2022-and-fourth-quarter-financial-results)) |
| 4Q22 | — | **–1.70** | neg | first quarterly loss since 3Q12 ([ajudaily](https://ajudaily.com/view/20230201144326847)) |
| 1Q23 | — | **–3.40** | neg | trough quarter ([KED, 2023-04-26](https://amp.kedglobal.com/newsAmp/ked202304260009)) |
| 2Q23 | 7.31 | –2.88 | –39% | ([MarketScreener](https://uk.marketscreener.com/quote/stock/SK-HYNIX-INC-6494929/news/SK-hynix-Reports-Second-Quarter-2023-Financial-Results-44417153)) |
| 3Q23 | — | loss (**unverified** size) | neg | net loss ₩2.2tn ([daum/Yonhap](https://v.daum.net/v/20231026084651600)) |
| 4Q23 | 11.31 | +0.35 | 3% | first profit in 5 quarters ([storagenewsletter](https://www.storagenewsletter.com/2024/01/29/sk-hynix-fiscal-4q23-financial-results/)) |
| 1Q24 | ~12.4 (**derived**) | ~2.9 (**derived**) | ~23% | FY24 minus 2Q–4Q; not a reported figure |
| 2Q24 | 16.42 | 5.47 | 33% | ([quartr](https://quartr.com/events/sk-hynix-inc-000660-q2-2024_F9ecrl9d)) |
| 3Q24 | 17.57 | 7.03 | 40% | ([storagenewsletter](https://www.storagenewsletter.com/2024/10/29/sk-hynix-fiscal-3q24-financial-results/)) |
| 4Q24 | 19.77 | 8.08 | 41% | ([Korea Times](https://www.koreatimes.co.kr/amp/business/tech-science/20250123/sk-hynix-becomes-most-profitable-korean-company-in-q4-2024)) |
| 1Q25 | 17.64 | 7.44 | 42% | ([Asia Economy](https://www.asiae.co.kr/en/article/2025042408302490928)) |
| 2Q25 | 22.23 | 9.21 | 41% | ([startuprecipe/PRN](https://en.startuprecipe.co.kr/archives/pr-newswire/sk-hynix-announces-2q25-financial-results)) |
| 3Q25 | 24.45 | 11.38 | 47% | ([tirto/PRN](https://tirto.id/sk-hynix-announces-3q25-financial-results-hkBy)) |
| 4Q25 | 32.83 | 19.17 | 58% | ([storagenewsletter](https://www.storagenewsletter.com/2026/02/10/sk-hynix-fiscal-4q25-and-fy25-financial-results/)) |
| 1Q26 | 52.58 | 37.61 | 72% | NI 40.35 ([barchart/PRN](https://www.barchart.com/story/news/1462801/sk-hynix-announces-1q26-financial-results)); rev/OP slightly below consensus ([Newsquawk](https://www.newsquawk.com/headlines/sk-hynix-000660-ks-q1-2026-krw-net-profit-403tln-exp-304tln-revenue-526tln-exp-536tln-operating-profit-376tln-exp-379tln-sees-q2-dram-shipments-to-rise-high-single-digits-and-nand-shipments-to-rise-by-mid-teens-qq)) |
| 2Q26 | 79.32 | 60.54 | 76% | NI 93.92 (inflated, §7); ~5% below consensus, stock –9.6% ([edaily](https://en.edaily.co.kr/news/eda202607295090/), [Webull/PRN](https://www.webull.com/news/15307406136009728)) |
| **3Q26** | **104.62** | **83.33** | **80% (79.7%)** | NI 39.78 (depressed, §7); beat consensus ~8–10% ([SK hynix newsroom](https://news.skhynix.com/en/q3-2026-business-results/), [Seoul Economic Daily](https://en.sedaily.com/finance/2026/10/28/sk-hynix-posts-record-797-percent-operating-margin-in-third)) |

Annual anchors:

| Year | Revenue | Operating profit | OP margin | Net income | Source |
|---|---|---|---|---|---|
| 2018 | — | **20.84** | 52% | — | ([storagenewsletter 4Q18](https://www.storagenewsletter.com/?p=197547), [cdrinfo](https://cdrinfo.com/d7/content/sk-hynix%E2%80%99s-2019-operating-profit-declined-87-percent)) |
| 2019 | — | **2.7** | 10% | — | –87% y/y; 4Q19 OP ₩236bn, net loss ₩118bn ([techpowerup/PRN](https://techpowerup.com/263446/sk-hynix-inc-reports-fiscal-year-2019-and-fourth-quarter-results), [Asia Times](https://asiatimes.com/2020/01/chipmaker-sk-hynix-posts-95-q4-profit-plunge/)) |
| 2021 | 43.00 | **12.41** | 29% | — | ([storagenewsletter 4Q21](https://www.storagenewsletter.com/2022/02/02/sk-hynix-fiscal-4q21-financial-results/)) |
| 2022 | — | 7.01 (release) / 6.81 (later K-IFRS table) | — | 2.24 | sources differ ([startuprecipe/PRN](https://en.startuprecipe.co.kr/archives/pr-newswire/sk-hynix-reports-2022-and-fourth-quarter-financial-results), [Digitimes](https://digitimes.com/news/a20240125PR200.html?chid=9)) |
| 2023 | 32.77 | **–7.73** | –24% | **–9.14** | ([Digitimes](https://digitimes.com/news/a20240125PR200.html?chid=9), [Statista/DART](https://www.statista.com/statistics/960293/sk-hynix-operating-profit-south-korea/)) |
| 2024 | 66.19 | 23.47 | 35% | 19.80 | ([Korea Times](https://www.koreatimes.co.kr/amp/business/tech-science/20250123/sk-hynix-becomes-most-profitable-korean-company-in-q4-2024)) |
| 2025 | 97.15 | 47.21 | 49% | 42.9 | ([technode/PRN](https://technode.global/prnasia/sk-hynix-announces-fy25-financial-results-posts-record-high-results-and-delivers-highest-shareholder-returns/)) |
| 2026 9M (sum) | **236.5** | **181.5** | 77% | 174.0 | my arithmetic from the three preliminary releases |

**Shape of the cycle.** Trough 1Q23 (OP –₩3.4tn) → breakeven 4Q23 → 2024 recovery (₩23.5tn, 35%) → 2025 (₩47.2tn, 49%) → 2026 vertical. 3Q26 alone (₩83.3tn) is **4x the 2018 full-year record**. No memory maker has ever sustained an 80% operating margin; SK hynix's own prior peak-year margin was 52% (2018). Whatever one believes about structural change, the margin is at a level with zero historical support.

**Where we are in the cycle.** Eight consecutive quarters of record operating profit, seven consecutive quarters of margin expansion, revenue up 3.2x in 12 months. Management says DRAM and HBM are "effectively sold out through 2029" counting LTAs plus deals under discussion, forecasts 2027 DRAM demand growth in the mid-20s% and shortage through 2030 ([Zacks call highlights](https://www.zacks.com/stock/news/3018441/skhy-q3-earnings-call-highlights-ai-demand-and-hbm4-expansion), [guru3d](https://www.guru3d.com/story/sk-hynix-posts-record-quarter-and-expects-memory-shortage-through-2030/)). Note that in 3Q26 DRAM bit shipments rose only ~10% q/q while DRAM ASP rose high-20s% q/q (Korean call summary via [bizwatch](https://news.bizwatch.co.kr/article/industry/2026/10/28/0011/)) — **the growth is now ~75% price, ~25% volume.** Price-led growth is the kind that reverses fastest.

**Consensus pattern:** 1Q26 and 2Q26 each came in slightly *below* consensus (2Q26 by ~5%, stock –9.6% on the day); 3Q26 beat by ~8–10%. The misses were on ASP, which TrendForce attributed to HBM mix weighing on blended ASP growth ([TrendForce, 2026-07-22](https://www.trendforce.com/news/2026/07/22/news-sk-hynix-set-to-post-record-operating-margin-in-q2-as-hbm-mix-weighs-on-asp-growth-and-ltas-gain-focus/)) — i.e., *more* HBM meant *lower* blended ASP growth. Read that twice; it is the hinge of §2.

**Profitability metrics (mandate items):**
- **Gross margin:** not disclosed in the releases I could reach; **not obtained**. Operating margin is the disclosed line.
- **ROE / ROIC:** total equity at 30 Sep 2026 **not obtained**, so I cannot compute these honestly. Directionally: FY2025 net income ₩42.9tn on a year-end-2025 equity that aggregators put well above ₩100tn would be a 30–40% ROE (**unverified**); 2026 annualised is >100% on any plausible equity base. As with MU, these are peak-cycle artefacts; through-cycle ROE 2019–2023 averaged low-single-digits-to-negative.
- **EPS trajectory (per common share, my arithmetic):** FY2025 ≈ ₩42.9tn / ~728M shares ≈ **₩58,900/share** (≈ ₩5,890 per ADS ≈ US$3.9/ADS at ₩1,523.5). 2026 9M net ≈ ₩174.0tn / ~720M avg shares ≈ **₩241,700/share** (≈ ₩24,170/ADS ≈ US$15.9/ADS) — but 9M net income includes a ~₩63tn one-off gain and a ~₩33tn one-off loss (§7); on operating profit, annualised 3Q26 OP of ~₩333tn less ~25% tax ≈ ₩250tn / ~706M shares ≈ ₩354,000/share ≈ US$23/ADS run-rate. **These are illustrative, not forecasts, and the share count is approximate (§5).**

## 2. HBM share and margin

**What the company discloses:** not HBM revenue, not HBM share of DRAM, not HBM margin. The 3Q26 release gives revenue, OP, NI, cash and borrowings only ([Webull/PRN](https://www.webull.com/news/15822865136734208)). Call commentary: HBM4 will overtake HBM3E in both volume and revenue share in 4Q26; DRAM was ~75% of total revenue in 3Q26, up from ~73% in 2Q26 (one earnings-review site, [finsee](https://finsee.ai/earnings/skhy/2026/q3/en/) — **secondary, unverified**); 14 LTAs signed with supply booked to 2029 ([sammyfans](https://www.sammyfans.com/2026/10/28/sk-hynix-q3-margin-hits-record-80-secures-14-ltas-with-memory-supply-booked-to-2029/amp/)); LTAs cover more than half of 2027–28 capacity and "include deposits" ([Longport call transcript summary](https://longportapp.cn/news/294135299)).

**HBM share of DRAM revenue — best available, all third-party:**
- **~40% of DRAM revenue in 2025 / by 3Q25** — Substack estimate and a Chosun Biz-sourced figure; the two sources use different bases (DRAM revenue vs total revenue), so treat as "roughly 40% of DRAM" at best ([longyield](https://longyield.substack.com/p/sk-hynix-the-memory-bottleneck-powering)).
- **HBM ~20%-something of DRAM *bit shipments* in 2025** (Korean press at 3Q25 results, [heraldk](https://www.heraldk.com/article/2025102817444133439)). Revenue share far above bit share is exactly what a premium product should show.
- **2026: no figure found.** Given HBM4 ramp and the 3Q26 DRAM ASP jump being commodity-led, HBM's revenue share may have *fallen* in 2026 even as HBM revenue grew. Unknown.
- SK hynix's share of the global HBM market: 56–58% in 1Q26 (IDC via one source; [Counterpoint](https://counterpointresearch.com/insights/global-dram-and-hbm-market-share)).

**HBM margin vs commodity DRAM — the thesis is inverted right now:**
- The firm's own `2026-08-21-msft-industry.md` §4.1 carried "HBM margins 2–3x DDR5" (Introl). **That was true in 2024–25 and is not true now.** TrendForce estimates that **HBM revenue and profitability per wafer fell below 64GB DDR5 RDIMM in 1Q26**, because HBM is sold under annual/LTA pricing while commodity DDR5 contract prices more than doubled ([TrendForce](https://www.trendforce.com/news/2026/07/22/news-sk-hynix-set-to-post-record-operating-margin-in-q2-as-hbm-mix-weighs-on-asp-growth-and-ltas-gain-focus/); DDR5 price data in the MSFT industry report). Consistent with that, SK hynix said it would prioritise general-purpose DDR5 output ([wccftech](https://wccftech.com/after-earning-major-profits-from-hbm-sk-hynix-now-plans-to-prioritize-ddr5-dram-production/amp/)). One analyst construction uses 65% HBM vs 90% DDR5 margins ([liveinthefuture](https://liveinthefuture.org/stories/ddr5-golden-cross-90-margin-beats-nvidia-apple.html) — **low-quality source, directional only**).
- **Implication for the bull thesis.** The bull case is "HBM is a structurally higher-margin, LTA-protected, non-commodity product, so SK hynix's margins should hold through the cycle." Today's 80% margin is *not* evidence for that case — it is evidence of a commodity price spike that HBM is partially *missing*. The correct reading is two-layered: (i) the HBM layer (maybe 35–45% of DRAM revenue) is contracted, deposit-backed and probably earns a healthy but not extreme margin, with price locked for 2027 and partly 2028; (ii) the commodity layer (the other ~55–65% of DRAM plus NAND) is earning unprecedented spot-driven margins that history says will mean-revert hard. **The trough will be set by layer (ii) collapsing and layer (i) holding. How much of the LTA book has floor prices, and at what level, is undisclosed — NOT OBTAINED.**

## 3. Capex and free cash flow

| Year | OCF (₩tn) | Capex (₩tn) | FCF (₩tn, my arithmetic) | Capex/OCF | Capex/Revenue | Source |
|---|---|---|---|---|---|---|
| 2024 | 29.8 | 16.7 | 13.1 | 56% | 25% | OCF: aggregator; capex: tracker citing SEC cash-flow statements ([tickerleague](https://tickerleague.com/companies/SKHY/financials/capex)) — **both third-party, unverified against DART** |
| 2025 | 53.4 | 28.6 | 24.8 | 54% | 29% | same sources; OCF +79% y/y; FY25 net income 42.9 → **OCF > NI**, healthy |
| TTM to 1Q26 | 70.7 | 30.0 | 40.7 | 42% | — | ([stockhub](https://stockhub.kr/en/insights/view_1793147160696_n22qss3o1)) |
| 2Q26 | ~65.7 (CFO) | — | 77.4 per S&P (definition **unverified**; exceeds CFO so almost certainly includes Kioxia disposal proceeds) | — | — | ([S&P Global, 2026-08-05](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/sk-hynix-postq-profit-beat-offsets-revenue-miss), [INDmoney](https://www.indmoney.com/blog/us-stocks/why-sk-hynix-skhy-stock-falling-q2-earnings-analysis)) |
| 1H26 | — | ≈US$12.0bn (+73% y/y) ≈ ₩18tn | — | — | — | ([sec-api.io](https://sec-api.io/insights/financial-analysis-of-sk-hynix-august-2026); conversion mine) |
| 3Q26 | **not obtained** | **not obtained** | — | — | — | release gave cash/borrowings only; D&A ₩4.3tn, EBITDA ₩87.7tn per call summary ([stockhub](https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call)) |

*A Korean report of "1H operating cash flow ₩18.19tn, +65% y/y" surfaced in search but is inconsistent with 2Q26 CFO of ~₩65.7tn; it is almost certainly 1H25 data mis-dated. Not used.*

**Is FCF positive at current spend? Overwhelmingly yes.** Even if 2026 capex doubles 2025's to ~₩55–60tn, 2026 OCF is tracking well above ₩200tn. Cash rose ₩26.5tn in 3Q26 *after* funding most of a ₩40tn buyback and ₩2.8tn of debt reduction ([Korean Center/Yonhap](https://www.koreancenter.or.kr/news/articleView.html?idxno=1430914)).

**Capex discipline — the record is good, the forward plan is the risk:**
- Stated policy (two formulations found, not reconciled): capex "around the mid-30% level of sales on a three-year moving average" ([TrendForce](https://www.trendforce.com/news/?p=47478)) and "capped at 30% of [operating cash flow]" (discipline introduced end-2024; [daum, 2026-07-01](https://v.daum.net/v/20260701090610353), snippet truncated). Actual 2024–25 ran 54–56% of OCF and 25–29% of sales — i.e., below the sales-based ceiling.
- **2026 capex guidance: none given.** One analyst inference put 2026 capex near ₩110tn on the basis of the ₩100tn net-cash target ([daum](https://v.daum.net/v/20260701090610353)) — the 1H26 run-rate (~₩18tn) does not support that; treat as **unverified and probably high**.
- **2027: "investment will rise significantly"** with Yongin Fab 1 entering full operation; amount undisclosed ([stockhub call summary](https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call)).
- **Multi-year plan: ₩1,100tn (≈US$712bn)** — Yongin ₩600tn, Cheongju ₩100tn, new southwestern site ₩400tn; phased, no annual schedule ([daum](https://v.daum.net/v/20260701090610353); US$38bn near-term fab tranche per [HotHardware](https://hothardware.com/news/sk-hynix-bets-38b-new-fabs-lock-in-ai-memory-dominance)).
- **The depreciation trap.** 3Q26 D&A was ~₩4.3tn (~₩17tn annualised) against 2025 capex of ₩28.6tn and a rising 2026–27 run-rate. D&A is only ~4% of revenue today *because revenue is inflated*. If capex steps to ₩50–80tn/yr through 2027–28, D&A heads toward ₩30–40tn/yr by 2029. At a trough revenue of, say, ₩60tn (2024's level), that is 50–65% of revenue in depreciation alone before wafer costs. **This is the mechanism by which memory companies go from 80% margins to losses: the cost base added at the peak depreciates into the trough.** SK hynix's own 2023 (–₩7.7tn OP) followed its 2021–22 capex peak.

## 4. Balance sheet, debt, IPO proceeds (primary vs secondary)

**Net cash position, KRW tn:**

| Date | Cash & equivalents | Borrowings | Net cash | Source |
|---|---|---|---|---|
| 31 Dec 2023 | — | ~32.5 (peak) | net debt | ([tickerleague](https://tickerleague.com/companies/SKHY/financials/total-debt)) |
| 30 Sep 2025 | — | 24.1 | +3.8 | ([digitimes/PRN 3Q25](https://www.digitimes.com/news/a20251029PR200.html?chid=9)) |
| 31 Dec 2025 | — | ~24.8 | +12.69 | ([TrendForce](https://www.trendforce.com/news/2026/03/25/news-sk-hynix-aims-to-secure-%E2%82%A9100t-in-net-cash-to-support-long-term-investment-adr-eyed-for-2h26/)) |
| 31 Mar 2026 | — | — | +35.0 | ([mt.co.kr](https://www.mt.co.kr/en/stock/2026/08/20/2026081918452174148)) |
| 30 Jun 2026 | 88.0 | 18.6–21.1 (aggregators differ) | +69.4 | ([Webull/PRN 2Q26](https://www.webull.com/news/15307406136009728), [mt.co.kr](https://www.mt.co.kr/en/stock/2026/08/20/2026081918452174148)) |
| **30 Sep 2026** | **114.5** | **15.8** (–2.8 q/q) | **+98.7** | ([Korean Center/Yonhap](https://www.koreancenter.or.kr/news/articleView.html?idxno=1430914)) |

Net cash went from ₩3.8tn to ₩98.7tn in twelve months. The ₩100tn net-cash target set by CEO Kwak in March 2026 ([TrendForce](https://www.trendforce.com/news/2026/03/25/news-sk-hynix-aims-to-secure-%E2%82%A9100t-in-net-cash-to-support-long-term-investment-adr-eyed-for-2h26/)) was effectively reached in two quarters.

**Interest coverage:** FY2025 interest expense ≈ ₩0.92tn (aggregator, **unverified**; 2024 ≈ ₩1.35tn), so FY2025 OP/interest ≈ **51x**; on 3Q26 annualised OP it is >300x. Interest income (~₩1.4tn FY25) already exceeded interest expense. **Debt maturity ladder and coupon detail: NOT OBTAINED.** With ₩15.8tn of borrowings against ₩114.5tn cash, maturities are not a risk item.

**Caveat on the cash:** LTAs "include deposits" (2Q26 call). As with Micron's SCAs (see MU report, where $22bn of "net cash" was refundable customer deposits), **some portion of the ₩114.5tn is customer prepayments, not earned cash. The amount is NOT OBTAINED.**

**The IPO — 100% primary, general corporate purposes:**
- **Structure:** 177.9M ADS = **17.79M newly issued common shares**, ~2.4–2.5% of shares outstanding. No selling shareholders. **Primary, not secondary** ([The Tech Capital](https://thetechcapital.com/sk-hynix-raises-26-5-billion-in-nasdaq-ads-offering/), [Motley Fool](https://www.fool.com/investing/2026/07/08/sk-hynixs-28-billion-nasdaq-listing-would-be-the-s/)).
- **Price and size:** US$149/ADS (below the US$158.14 assumed price in the F-1/A); gross ≈ US$26.5bn; **net ≈ US$26.2bn per the final 424B4** ≈ ₩39.9tn at ₩1,523.5; >7x oversubscribed ([Tech Capital](https://thetechcapital.com/sk-hynix-raises-26-5-billion-in-nasdaq-ads-offering/), [Investing.com](https://www.investing.com/analysis/sk-hynix-ipo-everything-you-need-to-know-about-sk-hynix-200683722)). Second-largest equity raise ever.
- **Use of proceeds:** the prospectus says **"general corporate purposes"**; press coverage cites Korean fab expansion and EUV scanner purchases ([Tech Capital](https://thetechcapital.com/sk-hynix-raises-26-5-billion-in-nasdaq-ads-offering/)). There was no debt-paydown rationale and no need for one: borrowings were already below cash. Not a cent went to insiders.
- **What it means:** (i) **Dilution was ~2.4%, and it has already been more than reversed by cancellations (§5).** (ii) **Because no insider sold at IPO, the 8 Oct 2026 lock-up expiry released nothing that had been "cashed out" — it only freed the company, affiliates and management from selling restrictions** ([Briefs](https://www.briefs.co/?p=24801), [Webull](https://www.webull.com/news/15702155852596224)). SK Square (20.07% holder) is legally bound to stay ≥20% under Korea's holding-company rules ([Korea Times, 2026-11-02](https://www.koreatimes.co.kr/business/companies/20261102/sk-square-plans-32-bil-shareholder-payout-from-sk-hynix-dividends)), so it cannot be a seller. **The lock-up expiry is a technical, not a fundamental overhang.** One outlet attributed a –5.7% day to it ([TickerSpark](https://tickerspark.ai/market/sk-hynix-inc-skhy-drops-5-7-after-lockup-expiry-1791479186417)).
- **The capital-allocation oddity.** A company with ₩69tn net cash and ~₩65tn of quarterly CFO raised US$26bn of primary equity in July, then within six weeks authorised ₩40tn (Aug 19) and later ₩20tn (Oct 28) of buybacks — i.e., **it issued ~₩40tn of stock and bought back ~₩60tn of stock in the same half-year.** The round trip is accretive to continuing holders only if the repurchase price is below the issue price — see §5, where the arithmetic suggests it was, by a wide margin, in KRW terms. The stated purpose of the US listing was to close the "AI-era valuation gap" versus US peers ([daum](https://v.daum.net/v/Wvtf0xkLmK)); the proceeds were, in effect, surplus.

## 5. Share count and dilution

Reconstructed share-count bridge (all approximate; **no primary DART disclosure of the post-cancellation total was retrievable**):

| Event | Date | Shares (M) | Source |
|---|---|---|---|
| Outstanding before Jan-2026 cancellation | Jan 2026 | ~728 | ([Asia Economy](https://www.asiae.co.kr/en/article/2026012914510475098)) |
| Cancel 15.3M treasury shares (~₩12.2tn, 2.1%) | Jan–Mar 2026 | → ~712.7 | ([rallies](https://rallies.ai/news/sk-hynix-reports-record-971-trillion-won-revenue-and-cancels-153m-shares)); cross-check: May-2026 market cap ₩1,624tn ÷ ₩2.28M record price ≈ 712M ([Semafor](https://www.semafor.com/article/05/27/2026/ai-chipmaker-sk-hynix-hits-1t-in-market-capitalization)) |
| + IPO: 17.79M new shares (177.9M ADS) | 14 Jul 2026 | → ~730.5 | "about 730 million outstanding" in Aug ([Korea Times](https://www.koreatimes.co.kr/business/companies/20260819/sk-hynix-to-buy-back-286-mil-worth-of-shares-in-3-months-before-cancellation)) |
| – ₩40tn buyback, 24.07M shares, **100% cancelled**, completed ~1 month early (mid-Oct vs 19 Nov plan) | 20 Aug–~mid-Oct 2026 | → ~706.4 | ([Korea Times](https://www.koreatimes.co.kr/business/companies/20260819/sk-hynix-to-buy-back-286-mil-worth-of-shares-in-3-months-before-cancellation), [smarttoday](https://www.smarttoday.co.kr/ko-kr/articles/113190)) |
| – ₩20tn buyback, **50% cancelled / 50% to employee compensation** | 29 Oct 2026–28 Jan 2027 | → ~699–700 after cancellation of ~₩10tn (≈6.5–7M shares at ₩1.4–1.5M) | ([GuruFocus](https://www.gurufocus.com/news/9147639/sk-hynix-stocks-rally-1089-with-buyback-cancellation-split-in-focus), [Seoul Economic Daily](https://en.sedaily.com/finance/2026/10/28/sk-hynix-says-shares-undervalued-expects-buybacks-to-lift)) |

**Net 2026 effect: ~728M → ~700M, a ~4% reduction despite a 2.4% primary IPO.** Per-share metrics are *helped*, not hurt, by 2026's corporate actions. ADS outstanding: 177.9M at IPO (plus any subsequent conversions, **not obtained**) = ~2.5% of the equity.

**The ₩20tn buyback as a capital-allocation item (coordinator request):**
- **Size vs market cap:** ordinary closed ₩1,487,000 on 28 Oct 2026 (+10.9% on results) ([GuruFocus](https://www.gurufocus.com/news/9147639/sk-hynix-stocks-rally-1089-with-buyback-cancellation-split-in-focus)). × ~706M shares ≈ **₩1,050tn market cap (estimate)**. ₩20tn ≈ **1.9%** of market cap; but only ₩10tn is cancelled (**≈0.9%**). The earlier ₩40tn programme was ≈3.3% and fully cancelled.
- **Cancellation vs treasury:** 50/50. The ₩10tn employee tranche is **not** shareholder return — it is compensation. Market commentators flagged the drop in cancellation ratio from 100% to 50% as the negative in the announcement ([GuruFocus](https://www.gurufocus.com/news/9147639/sk-hynix-stocks-rally-1089-with-buyback-cancellation-split-in-focus)). **Accounting watch:** a ₩10tn share grant equals ~12% of 3Q26 operating profit; whether and when it is expensed through P&L (K-IFRS share-based payment) is **not obtained**. If spread over vesting years it depresses future reported OP; if granted outright it is a one-quarter hit. Either way it is a real cost that the "₩100tn shareholder return" headline conceals.
- **ADS/ordinary interaction:** buybacks execute on KRX in ordinary shares (ADS repurchase: not indicated anywhere; **unverified**). ADS holders benefit pro rata through the reduced share count. **Arithmetic flag for Valuation (𢦀鳩仔):** at ₩1,487,000/share, one ADS-equivalent of ordinary stock is ₩148,700 ≈ **US$98 at ₩1,523.5/US$**, while SKHY traded at **US$142.62 on 26 Oct 2026** ([CoinGecko snapshot](https://www.coingecko.com/en/stocks/sk-hynix)). Unless the won has appreciated to ~₩1,040/US$ (it has not, as far as search indicates), **the ADS was trading at a 40%+ premium to the ordinary line.** One analysis site carries the title "SKHY ADR premium valuation" ([INDmoney](https://www.indmoney.com/blog/us-stocks/sk-hynix-stock-analysis-skhy-adr-premium-valuation-outlook)). This is either (a) an extraction error in one of the price points, (b) a genuine, non-arbitraged premium because ADS↔ordinary conversion is restricted, or (c) a stale snapshot. **I could not resolve it and it is material: if (b), the Owner's US$129 cost basis is well above the KRW-equivalent price at which the company itself is repurchasing, and the ADS carries premium-collapse risk independent of the memory cycle.** Listed first in the NOT OBTAINED register.
- **Total 2026 returns:** ~₩100tn = ₩40tn + ₩20tn buybacks + dividends including a 3Q26 dividend of ₩20,000/share (≈₩14tn, of which ₩10,000/share is a special dividend passing through Kioxia disposal proceeds) ([Korean Center](https://www.koreancenter.or.kr/news/articleView.html?idxno=1430893)). Policy: "50% or more" of cumulative FCF ([smarttoday](https://www.smarttoday.co.kr/ko-kr/articles/110612)). Parent SK Square plans a US$3.2bn payout funded by SK hynix dividends ([Korea Times](https://www.koreatimes.co.kr/business/companies/20261102/sk-square-plans-32-bil-shareholder-payout-from-sk-hynix-dividends)) — the controlling holder has a structural appetite for dividends that will not disappear in a downturn.

## 6. Inventory — the cycle-turn signal

| Date | Inventories (₩tn) | Change | Valuation allowance | Source |
|---|---|---|---|---|
| 31 Dec 2025 | 14.29 | — | ₩494.9bn (3.35%) | ([fnnews/Yonhap, 2026-09-07](https://en.fnnews.com/news/202609071524180869)) |
| 30 Jun 2026 | **17.99** | **+25.9% / +₩3.70tn** in 6 months; WIP +₩1.87tn = 50.6% of the increase | ₩413.4bn (2.25%), –16.5% | same |
| 30 Sep 2026 | **NOT OBTAINED** | — | — | quarterly report not located |

**Days of inventory — two measurements, opposite readings:**
- **On revenue:** ₩17.99tn / ₩79.3tn 2Q26 revenue × 91 ≈ **21 days** — consistent with a Shinhan note describing memory inventory at "just a 3-week level" (30 Jul 2026, [edaily headline](https://en.edaily.co.kr/news/eda202607305090/); methodology unknown). On this basis inventory is at a record low relative to sales and the signal is green.
- **On cost of goods sold (my estimate — COGS is not disclosed in the releases I reached):** at a 76% OP margin, COGS + opex ≈ ₩19tn in 2Q26; assuming opex ~₩4–5tn, COGS ≈ ₩14–15tn, so DIO ≈ **~110 days**, versus ~120 days at end-2025 by the same method. Flat to slightly down.
- **In absolute won:** up 26% in six months while quarterly revenue rose 142%. WIP-led (consistent with HBM4 ramp, which has long cycle times and high value per wafer), finished-goods split **not obtained**.

**Verdict:** no cycle-turn signal in inventory as of 30 Jun 2026. But the measurement problem is the point: at 80% margins, DIO on COGS tells you nothing (a 30% price fall would push DIO from 110 to ~160 days with zero change in physical units), and DIO on revenue flatters by construction. **Watch absolute won, the finished-goods line, and the valuation allowance ratio** — the allowance *fell* to 2.25%, meaning prior write-downs are being reversed into margin (small, ~₩81bn, but the direction will flip first when prices turn). The 30 Sep figure is the single most important balance-sheet datum I could not obtain.

## 7. Accounting quality

1. **Net income is not usable; use operating profit and cash.** 2Q26 net income ₩93.9tn vs OP ₩60.5tn: non-operating net **+₩62.2tn**, of which **₩63.3tn "asset disposal/revaluation"** attributed by analysts to the completed sale of the Kioxia stake — **the company did not name the asset in its results package** ([mt.co.kr](https://www.mt.co.kr/en/industry/2026/07/30/2026072920125523331), [Nasdaq call highlights](https://www.nasdaq.com/articles/sk-hynix-q2-earnings-call-highlights)). 3Q26 net income ₩39.8tn vs OP ₩83.3tn: **net non-operating expense ≈ ₩32.6tn** per a call summary ([stockhub](https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call)); one search extraction decomposed it as ~₩22.9tn investment-asset valuation loss + ~₩11.6tn FX loss, **which I could not confirm in a second pass — unverified.** A ₩96tn swing in non-operating items across two quarters is a reason to ignore reported EPS entirely for 2026. Headline "net profit –58% q/q" is noise; OP +38% q/q is signal.
2. **Earnings vs OCF:** FY2025 OCF ₩53.4tn > NI ₩42.9tn; 2Q26 CFO ~₩65.7tn ≈ OP ₩60.5tn. No divergence. Good.
3. **Receivables:** **not obtained.** With LTAs including customer deposits, deferred revenue/contract liabilities should be rising — also not obtained.
4. **Depreciation policy:** straight-line over estimated useful lives, table in F-1/A **not retrieved**; depreciation starts when the asset is "available for intended use", a judgement the 2022 auditor flagged as a Key Audit Matter because the P&L effect is significant ([F-1/A via search](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526295501/d32785df1a.htm)). **No evidence found of a useful-life extension** of the Microsoft/Meta kind. The lever that *does* exist is the ready-for-use date on ₩28tn+/yr of new equipment — deferring it defers depreciation. Not alleged; flagged for the 20-F.
5. **Related-party transactions with SK Group:** the 424B4 has a "Certain Relationships and Related Party Transactions" section at p.129 — **content not retrievable.** Known structure: SK Square 20.07% (must hold ≥20%); SK Inc. above it; SK Telecom and other affiliates as counterparties. **Governance inference (mine, unverified):** 17.79M new IPO shares would have pushed SK Square to ~19.6–20.0% of the enlarged count, at or below its statutory floor; the immediate 24.07M-share cancellation restores it to ~20.2%. The sequencing of a primary issue followed within six weeks by a full-cancellation buyback larger than the issue is consistent with managing the holding-company threshold. If true, it means future buybacks are partly structural (parent-driven), which is favourable for per-share metrics but means the ₩10tn employee tranche is where the discretion went.
6. **Share-count creep:** none; net reduction (§5). But **₩10tn of share-based employee compensation** in one authorisation is a cost; its P&L treatment is **not obtained**.
7. **Special dividend from asset sale:** ₩10,000/share of the 3Q26 dividend is Kioxia proceeds pass-through — correctly labelled as special by the company. Fine.
8. **Capitalisation games:** nothing found; R&D ~US$4.4bn in 2025 per Korea Times ([Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260315/sk-hynix-spends-44-bil-on-rd-last-year-amid-hbm-boom-data)); capitalised development costs **not obtained**.
9. **Adjusted figures:** SK hynix reports K-IFRS only; no "adjusted" series to game. A genuine plus versus US peers.

**Net:** the statements themselves are clean. The red flags are opacity (HBM, related parties, LTA deposits, 3Q26 balance sheet), not manipulation.

## 8. Peak-to-trough earnings — what survives

Company's own history, operating profit, ₩tn (sources in §1):

| Cycle | Peak | Trough | **Trough / peak** | Quarterly extreme |
|---|---|---|---|---|
| 2018 → 2019 (annual) | 20.84 (52% margin) | 2.7 (10% margin) | **13% survived (–87%)** | 4Q18 ₩4.4tn → 4Q19 ₩0.236tn = **5% survived**; 4Q19 net loss |
| 2021 → 2023 (annual) | 12.41 (29% margin) | –7.73 (–24% margin) | **less than zero (–162%)** | 4Q21 ₩4.22tn → 1Q23 **–₩3.40tn** in five quarters |
| 2022 → 2023 (as the coordinator framed it) | 7.01 / 6.81 | –7.73 | **less than zero** | — |

**Time from peak quarter to trough quarter: 4–5 quarters in both cycles.** In both, the company went from record to loss faster than consensus forecast at the time (4Q19 missed a ₩433bn consensus by 45%, [Asia Times](https://asiatimes.com/2020/01/chipmaker-sk-hynix-posts-95-q4-profit-plunge/)).

**Applied to today — illustrative arithmetic, not a forecast.** Take 3Q26 annualised OP (~₩333tn) as the peak:
- *2018–19 template (13% survives):* trough-year OP ≈ **₩43tn** — roughly FY2025's ₩47tn, above FY2024's ₩23.5tn. At ~700M shares and 25% tax that is still ~₩46,000/share ≈ ₩4,600/ADS ≈ US$3/ADS of trough EPS. A holder at US$129 would be paying ~40x trough earnings — survivable if the trough is short.
- *2021–23 template (<0% survives):* trough-year OP **negative**, net loss, no EPS. The share price at the 2023 trough was ~₩75,000–90,000 (pre-rally); the stock fell ~50% peak-to-trough in 2022 ([ajudaily](https://ajudaily.com/view/20230201144326847) context) and ~40% in 2018–19.

**Which template?** Three things are genuinely different from 2018 and 2021: (i) LTAs with deposits covering >50% of 2027–28 capacity; (ii) ₩98.7tn net cash versus net debt at both prior peaks; (iii) HBM is a custom, qualified product with a 12–18 month design-in lead, not a spot commodity. Two things are the same: (iv) the industry is adding capacity at the fastest rate in its history (₩1,100tn plan here, Samsung and Micron similar), and (v) the marginal buyer is a small set of hyperscalers whose capex is now being priced by *their* shareholders as a cost (MSFT industry report §1, §2). **The evidence supports the 2018–19 template as the base case *for the HBM layer* and something closer to 2022–23 *for the commodity layer* — i.e., a blended trough materially above zero but far below 2025, arriving 4–5 quarters after the peak quarter, whenever that is.** The data does not let me say the peak quarter has been reached; 3Q26 beat and 4Q26 guidance (HBM4 crossover, ASP still rising) point higher. It also does not let me rule out 2023.

## 9. For and against (L-003 anti-anchoring)

**Strongest case FOR the statements (bull):**
- Eight consecutive record quarters; 3Q26 beat consensus by ~8–10% after two small misses, and the beat was on margin.
- ₩98.7tn net cash, ₩15.8tn debt, interest coverage >50x even on 2025 numbers — the company can fund a ₩1,100tn programme and a 2023-style trough simultaneously without issuing equity or debt.
- OCF > NI; capex/OCF ~55%; no adjusted-earnings games; K-IFRS only.
- LTAs with deposits through 2029; management's "sold out through 2029" with mid-20s% 2027 DRAM demand growth; HBM4 crossover in 4Q26 extends the HBM product cycle; 56–58% global HBM share.
- Share count falling ~4% in 2026 despite the IPO; the company repurchased in KRW at prices far below the US$149 ADS issue price-equivalent — accretive to continuing holders.

**Strongest case AGAINST (bear):**
- An 80% operating margin at a memory company has never existed; the company's own peak-year margin was 52%, and 13% / <0% of peak OP survived the last two troughs within 4–5 quarters.
- The margin is commodity-led, not HBM-led: TrendForce has HBM per-wafer profitability *below* DDR5 RDIMM in 1Q26; 3Q26 growth was ~75% price / ~25% volume; HBM share, margin and LTA floor prices are all undisclosed.
- Capex "rises significantly" in 2027 against a ₩1,100tn plan; D&A at ~4% of revenue today will be 50%+ of trough revenue — the exact mechanism of 2023.
- Inventory +26% in won in 1H26; 3Q26 balance sheet not published in any source I could reach; the valuation allowance is being released, which reverses first.
- Net income swung by ~₩96tn on non-operating items in two quarters; related-party section unread; ₩10tn of the "shareholder return" is employee compensation; an unexplained apparent 40%+ ADS premium to the ordinary line (§5).
- The hyperscaler customer base is itself under shareholder pressure on capex (MSFT industry report); Alphabet's FCF turned negative in 2Q26.

**Which does the evidence support?** On the *statements as filed*: the bull case — they are clean, over-capitalised and cash-generative. On *what the statements will look like in eight quarters*: the bear case has the entire historical record on its side and the bull case has one new instrument (deposit-backed LTAs) whose terms are secret. I weight the historical record. **The grade below is a B+ because the balance sheet earns it; it is not an A because the margin does not.**

## Financial score (0–100) and rationale

**Score: 72 / 100 — Grade B+.**

| Component | Weight | Score | Rationale |
|---|---|---|---|
| Balance sheet & liquidity | 25 | 24 | ₩98.7tn net cash, debt ₩15.8tn, coverage >50x; only deduction is undisclosed LTA deposits inside cash |
| Cash generation & capex discipline | 20 | 17 | OCF > NI, FCF strongly positive, capex/OCF ~55%; deduction for undisclosed 2026–27 capex and the ₩1,100tn plan |
| Profitability — level | 15 | 15 | 80% OP margin; nothing to deduct on the number itself |
| Profitability — durability (cycle-adjusted) | 20 | 6 | 13% / <0% trough survival; margin commodity-led; HBM per-wafer economics currently below DDR5; D&A trap |
| Accounting quality & disclosure | 20 | 10 | Clean K-IFRS, no adjusted games, OCF ≈ OP; but no HBM/segment/GM disclosure, related parties unread, net income distorted ±₩60tn, ₩10tn employee share grant, 3Q26 balance sheet unavailable |
| **Total** | **100** | **72** | |

**How much of the grade is cycle position:** the same statements scored on current-period metrics alone are ~88 (A−). The 16-point haircut is entirely the durability line. Put differently, **~60% of what makes these statements look excellent is cycle position (price), ~40% is structural (balance sheet, capital discipline, HBM franchise).** Calibration: 6160.HK A− 82 and MSFT A− 79 have far more durable earnings and weaker balance sheets; 0100.HK D+ 48 has neither. MU (B+, Jul 2026) is the right comparable: same cycle, same peak-margin problem, and SK hynix has the stronger balance sheet and the cleaner (K-IFRS-only) reporting but worse disclosure.

**What would move the grade:** *Up to A−:* 3Q26/4Q26 inventory flat in won with finished goods falling; disclosure of LTA floor prices or HBM segment margin; 2027 capex guided below ₩60tn. *Down to B−/C+:* inventory +15% q/q in won with allowance rising; DRAM contract price declines in TrendForce data; capex guide >₩80tn; any useful-life extension; ADS premium confirmed and unexplained.

**For the committee scorecard:** financial score **72**; data staleness 15 days (P&L), ~4.5 months (balance-sheet detail); confidence in the score: medium — every figure is a press extraction of a company release, none is a filing read.

## NOT OBTAINED register

Ranked by materiality to a holder at US$129/ADS.

1. **ADS vs ordinary price parity and conversion mechanics.** Arithmetic in §5 implies a 40%+ ADS premium at 26–28 Oct 2026 prices unless an extracted price is wrong. Conversion restrictions, ADS outstanding after conversions, and the current USD/KRW rate were all not obtained. **Valuation (𢦀鳩仔) must resolve this before any sizing decision.**
2. **3Q26 balance sheet and cash-flow statement** — inventory, receivables, contract liabilities (LTA deposits), OCF, capex, equity. Only cash, borrowings and net cash were released. Quarterly report on DART not located.
3. **HBM share of DRAM revenue (2026) and HBM margin** — company does not disclose; third-party estimates are 2025-dated and inconsistent.
4. **LTA terms** — floor prices, take-or-pay status, deposit amounts, share of 2027–29 volume. "Include deposits" and ">50% of 2027–28 capacity" are the only data points.
5. **2026 and 2027 capex guidance in won**; whether the capex cap is 30% of OCF or mid-30s% of sales; annual phasing of the ₩1,100tn plan.
6. **Useful-life table and any change** (F-1/A table exists but was not retrieved); capitalised development costs.
7. **Related-party transactions** (424B4 p.129) — volumes with SK Telecom, SK Inc., SK Square, brand-royalty payments; whether the IPO/cancellation sequencing was threshold-driven.
8. **Decomposition of 3Q26 ₩32.6tn net non-operating expense** (the ₩22.9tn valuation loss / ₩11.6tn FX loss split is unverified); the Kioxia gain attribution in 2Q26 is analyst inference, not company statement.
9. **P&L treatment and vesting of the ₩10tn employee share tranche.**
10. **Debt maturity ladder and coupons**; FY2025 interest expense (₩0.92tn) is an aggregator figure.
11. **Gross margin, total equity, ROE/ROIC inputs** for any period.
12. **Post-cancellation issued share count** from DART; final count of shares cancelled under the ₩40tn programme (24.07M was the plan).
13. **Current SKHY and 000660.KS prices (Nov 2026)**; latest dated quote found was US$142.62 (26 Oct) and ₩1,487,000 (28 Oct). One source gives a 52-week ADS range of US$124.80–194.80 — the Owner's US$129 is near the low.
14. **2Q22 operating profit; 3Q18 operating profit (₩6.47tn widely cited, not confirmed); 1Q24 and 3Q23 reported figures** (1Q24 derived; 3Q23 size unverified).
15. **Primary filings of any kind.** F-1, F-1/A, 424B4, 6-Ks, 20-F, DART 분기보고서 — all surfaced in search, none readable. Every number in this report should be re-verified against them when access is restored.

---
*Research only. Committee and Owner decide. This is not a forecast; memory pricing cannot be reliably predicted and the company's own history is the best evidence that it cannot.*

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
