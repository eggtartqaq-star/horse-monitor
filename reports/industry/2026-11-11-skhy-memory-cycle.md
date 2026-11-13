# SKHY — The Memory Cycle: Where We Are, Precisely

**Department 1: Macroeconomic Research · Industry Research**
**Analyst:** Elon Musk, Industry Research Analyst
**Date:** 2026-11-11 (completed 2026-11-12 after two rate-limit interruptions)
**Requested by:** CIO (via CEO)
**Ticker under review:** SKHY (SK hynix ADS, Nasdaq; 0.1 common share per ADS; listed 13 Jul 2026 at $149). **Owner holds at $129.**
**Scope:** The memory cycle, not the company. Financial statements are covered by 巴爺爺 (Dept 2).

---

## 0. Method, baseline carried forward, and evidentiary standard

**Baseline from `reports/industry/2026-08-21-msft-industry.md` (21 Aug 2026), not re-derived:**
- DRAM pricing tracking **+275–300% 2025→2027** (TrendForce / Introl / tech-insider, as cited there).
- HBM margins **2–3x DDR5**.
> ⚠️ **RETRACTION (CEO, 2026-11-13, per audit C5).** The line above carries the 21 Aug baseline "HBM margins 2–3x DDR5" as live. It is retired: 巴爺爺's financials report cites TrendForce (22 Jul 2026) placing HBM *per-wafer profitability* **below** 64GB DDR5 RDIMM as of 1Q26. The audit notes per-wafer profitability and a margin multiple are different metrics and the retirement rests on one estimate — so the correct status is **UNRESOLVED, do not reuse the 2–3x figure**, not "reversed."
- Memory ranked **second on pricing power** behind power/grid equipment.
- Microsoft (29 Apr 2026) and Amazon (30 Jul 2026) both cited memory costs in raising capex guidance.
- Big-four hyperscaler capex **~$732.5bn CY2026E, +78%**, growth rate plateauing near 80%.

This report updates what has moved in the twelve weeks since.

**Confidence tiers:** [A] company disclosure / research house (TrendForce, DRAMeXchange, Gartner, Counterpoint, Bloomberg Intelligence), dated · [B] reputable press reporting a filing or call · [C] secondary aggregator · [UNVERIFIED] widely repeated, no traceable origin.

**Environment:** direct page fetch unavailable; every figure below is from search-result extraction, not full-page retrieval. TrendForce's monthly contract-price tables are paywalled; where I cite a TrendForce number it is from a TrendForce press release or TrendForce News item surfaced in search, or from DRAMeXchange data as relayed by TheElec. Blocked hosts in §12. `tradingkey.com` is blacklisted and not cited; it surfaced for this name and was discarded. The session was cut twice by rate limits; the file was checkpointed between cuts and nothing was re-derived.

**Cycle framing used throughout.** A memory cycle turns when **bit supply growth overtakes bit demand growth**, and the turn is visible first in (i) spot falling below contract, (ii) contract-price momentum rolling over while still positive, (iii) customer inventory weeks rising, and (iv) all three majors raising capex guidance in the same window. I score each in §6. **"Sold out through 2029" and "shortage through 2030" are supplier narrative and are treated as such.**

---

## 1. Industry snapshot (Q3 2026 → 11 Nov 2026)

| Metric | Value | Date | Tier | Source |
|---|---|---|---|---|
| Global DRAM revenue, Q3 2026 | **~$200bn, +369% YoY**; **bit shipments only ~+4% YoY**; ASP ~$1.9/Gb | Q3 2026 (pub. 5 Nov 2026) | A | [Counterpoint](https://counterpointresearch.com/cn/insights/dram-super-cycle-nears-dollar-200b), [Counterpoint share tracker](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share) |
| DRAM revenue share, Q3 2026 | **Samsung 38% / SK hynix 29% (from 33% YoY) / Micron 21% (from 26%) / CXMT 9%** | Q3 2026 | A | [Counterpoint via sammyfans](https://www.sammyfans.com/2026/11/05/samsung-sk-hynix-global-dram-q3-2026-counterpoint-research/amp/) |
| SK hynix Q3 2026 | Revenue **KRW 104.6tn** (consensus ~98.2tn), OP **KRW 83.3tn** (consensus ~77.0tn), **OP margin 80%**; **net profit 39.8tn vs FnGuide 61.3tn — missed on KRW 32.6tn of net non-operating losses**; KRW 100tn shareholder-return plan | 28 Oct 2026 | A/B | [Korea Times](https://www.koreatimes.co.kr/business/companies/20261028/sk-hynix-logs-record-q3-operating-profit-of-628-bil), [investinglive](https://investinglive.com/stocks/sk-hynix-q3-operating-profit-beats-at-83tn-won-unveils-100tn-won-shareholder-payout-plan/), [Korea Herald](https://mbiz.heraldcorp.com/article/10890162) |
| Samsung Q3 2026 | OP **KRW 107.4tn** on revenue 195.3tn; DS division OP **106.5tn (~99% of group)**, margin ~72%; **slight miss vs 107.66tn consensus** (CNBC, relayed) | 29 Oct 2026 | A/C | [Samsung Newsroom](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results), [Light Reading](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter), [tech-insider](https://tech-insider.org/samsung-q3-2026-chip-profit-miss-107-44-trillion-won-ai-hbm4/) |
| Micron FQ4 2026 (to 3 Sep) | Revenue **$54.2bn**; FY26 **$133.2bn**, DRAM >$100bn; FQ1'27 guide **$61.5bn** | 30 Sep 2026 | A/B | [storagenewsletter](https://www.storagenewsletter.com/?p=305727), [blocksandfiles](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445) |
| Big-four hyperscaler capex, Q3 2026 | **$201.9bn, +108% YoY, +22% QoQ** (Amazon 77.3 / Alphabet 51.4 / Microsoft 39.4 / Meta 33.9) | Q3 2026 (10-Q-derived tracker) | B/C | [Walnut](https://walnutinvest.com/stats/ai-capex-statistics) |
| 2026 capex guidance after the October round | Amazon ~$220bn (held) · Alphabet $195–205bn (**held, not raised**; 2027 "significantly" higher) · Microsoft **~$170bn CY2026** (vs ~$175bn in my Aug report) · Meta **$135–145bn** (floor +$5bn) | 28–30 Oct 2026 | B | [Walnut](https://walnutinvest.com/stats/ai-capex-statistics), [paasa](https://paasa.com/blog/the-capex-verdict-what-fy-2027-guidance-signals-about-ai-margins) |

**Three things in this table matter more than the rest.** First, **Q3 DRAM bits grew ~4% while revenue grew 369%** — this cycle is almost entirely price, which is the signature of a supply-constrained peak rather than a demand-volume boom. Second, **SK hynix lost four points of DRAM revenue share YoY in the quarter it printed an 80% margin** — the price-taker/share trade-off is already visible. Third, **the October hyperscaler round was the first since this cycle began in which no one raised 2026 guidance materially**; against my August figure of ~$732.5bn, the midpoint sum is now Amazon 220 + Alphabet 200 + Microsoft 170 + Meta 140 = **~$730bn — flat**. Dollars are still rising violently (+108% YoY in Q3); the *guidance-raise cadence* has stopped. That is a demand-side second-derivative signal for memory and it is dated 28–30 Oct 2026.

---

## 2. Where we are in the cycle — DRAM and NAND contract prices by quarter, 2024 to now

### 2.1 DRAM contract price series (conventional DRAM, TrendForce QoQ; forecast-at-time unless marked realised)

| Quarter | Conventional DRAM contract QoQ | Note | Tier | Source |
|---|---|---|---|---|
| 1Q24 | **+13–18%** | mobile-led | A (fcst) | [TrendForce/iconnect007](https://iconnect007.com/article/139167/dram-contract-prices-projected-to-increase-1318-in-1q24-as-price-surge-continues/139164/,,) |
| 2Q24 | **+3–8%** | narrowing | A (fcst) | [TrendForce/iconnect007](https://iconnect007.com/article/140106/suppliers-aim-to-raise-contract-prices-but-with-uncertain-demand-2q24-dram-price-increase-expected-to-narrow-to-38/140103/ein) |
| 3Q24 | **+8–13%** (revised up ~5pp) | | A (fcst) | [TrendForce/iconnect007](https://iconnect007.com/article/141927/dram-industry-revenue-surges-248-in-2q24-upward-revision-of-contract-price-increase-for-q3/141924/pcb) |
| 4Q24 | **reversed downward** across most applications; server DDR5 the exception | no blended % | A | [TrendForce 27 Feb 2025](https://www.trendforce.com/presscenter/news/20250227-12492.html) |
| 1Q25 | **down**: DDR4 −10–15%, DDR3 −3–8%, LPDDR4X −8–13%, LPDDR5X −3–8% | "passive buyer strategies" | A (fcst) | [TrendForce 30 Dec 2024](https://trendforce.com/presscenter/news/20241230-12424.html) |
| 2Q25 | decline eased | no % | A | [TrendForce headline](https://iconnect007.com/article/143054/weak-demand-outlook-and-rising-inventory-and-supply-pressure-dram-prices-down-for-2025/143051/smt) |
| 3Q25 | **sharp rise, legacy-led**: consumer DDR4 +85–90%, LPDDR4X +38–43%, LPDDR5X +10–15% | DDR4 EOL | A (fcst) | [TrendForce/iconnect007](https://iconnect007.com/article/146462/ddr4-lpddr4-supply-tightens-sharply-in-2h25-as-structural-shortage-drives-strong-price-surge/146459/ein) |
| 4Q25 | **+45–50%** (realised, Feb 2026 report); blended incl. HBM +50–55%; had been forecast +8–13% then +18–23% in Oct 2025 | industry revenue $53.6bn, +29.4% QoQ | A | [TrendForce 26 Feb 2026](https://www.trendforce.com/presscenter/news/20260226-12937.html), [evertiq](https://evertiq.com/news/2026-02-26-price-rally-lifts-4q25-dram-revenue-294-qoq) |
| 1Q26 | **+93–98%** (realised, Jun 2026 report); forecast had gone 55–60% (Jan) → 90–95% (Feb) | industry revenue +81% QoQ to $97bn | A | [TrendForce 1 Jun 2026](https://www.trendforce.com/presscenter/news/20260601-13070.html), [evertiq](https://evertiq.com/news/2026-06-08-dram-prices-surge-industry-revenue-up-81-in-a-single-quarter) |
| 2Q26 | **+58–63%** (forecast, Jun 2026) | CSPs accepting higher prices; others followed | A (fcst) | same |
| 3Q26 | **+13–18%** | | A/C (second-hand) | [TrendForce via xenospectrum](https://xenospectrum.com/en/memory-spot-q4-demand-divide/) |
| **4Q26 (fcst, 30 Sep 2026)** | **+10–15%** | "AI server demand drives gains, consumer pressure persists" | **A** | [TrendForce 30 Sep 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), [evertiq](https://evertiq.com/news/2026-10-02-ai-keeps-memory-prices-climbing-in-q4-as-consumer-demand-weakens) |
| 4Q26 (20 Oct item) | "**~+20% QoQ despite slower gains**" | unclear if blended or server-weighted | A/UNRESOLVED | [TrendForce News 20 Oct 2026](https://www.trendforce.com/news/2026-10-20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/) |
| 4Q26 (secondary) | +8–13% | untraceable to a TrendForce document | C — not used | [hwbusters](https://hwbusters.com/?p=112680) |
| **1Q27** | **No numeric forecast found.** Qualitative: PC DRAM "gains narrowing" in 4Q26; "gradual quarterly increases next year"; "bullish momentum for the next three quarters" | | A (qualitative) | [TrendForce News 30 Oct 2026](https://www.trendforce.com/news/?p=51212), [TrendForce 2 Jun 2026](https://www.trendforce.com/presscenter/news/20260602-13074.html) |

**Monthly fixed-price print (DRAMeXchange via TheElec):** DDR4 8Gb PC DRAM **$27.50 in October 2026, +5.77% MoM, a record** (from $26.00) ([fourweekmba/TheElec](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/), [tech-insider](https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/)). [B]

**Reading the series.** Quarterly momentum: **4Q25 +45–50% → 1Q26 +93–98% → 2Q26 +58–63% → 3Q26 +13–18% → 4Q26 +10–15%.** The peak *rate* of increase was **1Q26**. The index has been decelerating for three consecutive quarters and is still rising. TrendForce's forward language has been downgraded from percentages to "gradual." This is the textbook late up-leg profile. Note also the forecasting pattern: every quarter from 4Q25 to 1Q26 was revised *up* repeatedly; 4Q26 is the first in which the two TrendForce items (10–15% vs ~20%) point in different directions and the secondary market carries a *lower* number (8–13%).

### 2.2 NAND contract price series

| Period | NAND contract | Tier | Source |
|---|---|---|---|
| Jan 2025 → Sep 2026 | **21 consecutive months of increases** (128Gb MLC benchmark) | B | [TheElec/DRAMeXchange via fourweekmba](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/) |
| **4Q26 fcst (30 Sep 2026)** | overall NAND **+15–20% QoQ; enterprise SSD +23–28%** (QLC eSSD for KV cache); consumer small increases | A | [TrendForce 30 Sep 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html) |
| **October 2026 realised** | **128Gb MLC unchanged at $30.61 — first flat month in 21.** TrendForce October wafer report: MLC, TLC, QLC wafer contract prices **all flat**; "weak consumer demand and elevated wafer costs stopping the upward run; buyers' purchasing interest falling" | A/B | [TrendForce RP261030YB (title/abstract)](https://www.trendforce.com/research/download/RP261030YB), [fourweekmba/TheElec](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/) |
| 1Q27 | TrendForce listing: "off-season prices plateau as MLC faces heavier cuts" (eMMC/UFS) | A (title only) | [TrendForce tag page](https://www.trendforce.com/research-tags/dram?page=12&tab=reports) |

**First hard cycle datum.** NAND contract momentum **rolled over in October 2026** — flat, in the consumer/wafer benchmark, four weeks after a +15–20% quarterly forecast. One flat print is not a turn and module-maker digestion is the benign reading. But it is checklist item (ii) and for NAND it has happened. DRAM has not: DDR4 fixed price made a record in the same month.

### 2.3 Spot vs contract

| Indicator | Reading | Date | Tier | Source |
|---|---|---|---|---|
| DDR4 1Gx8 3200 spot | **$46.82, −0.09% WoW — flat**; spot "remained above suppliers' official quotes despite weak demand, fueling correction expectations" | 3 Nov 2026 | A | [TrendForce News](https://www.trendforce.com/news/?p=66203) |
| DDR5 spot | "supply tight"; buyers raising target prices on delivery pressure; vendor: DDR5 chip spot +13% since 2 Sep | 21 Oct / early Nov 2026 | A/C | [TrendForce News 21 Oct](https://www.trendforce.com/news/2026-10-21/insights-memory-spot-price-update-ddr5-supply-tight-ddr4-trading-subdued-despite-0-84-gain-in-mainstream-prices), [servermonkey](https://www.servermonkey.com/blog/october-2026-enterprise-it-market-update.html) |
| Retail 32GB DDR5 kit, lowest tracked | **$479.99** (vs $392 in my Aug report; $110–140 Q3 2025) | 2 Nov 2026 | C | [pcserverandparts](https://pcserverandparts.com/news/when-will-ram-prices-go-down-2026/) |

**Reading.** Spot is still **above** contract for DDR4 and DDR5 spot is still rising. The turn signature — spot below contract — **is not present as of 3 Nov 2026.** But TrendForce's language ("despite weak demand," "correction expectations") is pre-roll-over language. DDR4 is an EOL legacy product; its spot is a channel signal. DDR5 spot is the server-relevant read and it is still tight.

### 2.4 Rate of change — accelerating, plateauing, or rolling over?

**DRAM: decelerating for three quarters at a still-high positive rate. NAND: rolled over in October. Consumer and mobile DRAM: already at plateau ("flat to slightly higher" 4Q26 mobile DRAM; "flat-to-slight increases" consumer).**

TrendForce's own warning (30 Sep 2026): "if consumer inventory digestion continues to fall short of expectations, market prices face a heightened risk of a downward pull-back" ([evertiq](https://evertiq.com/news/2026-10-02-ai-keeps-memory-prices-climbing-in-q4-as-consumer-demand-weakens)).

**Verdict on §2: the blended DRAM index is in its late up-leg — peak rate of increase was 1Q26; still rising; consumer sub-index at plateau; NAND flat. Not the peak of the cycle, but the first quarter in which a peak is visible from the data rather than only from the bear narrative.**

### 2.5 Supply growth — wafer starts and bit growth by maker

| Maker | Current / growth | Planned additions | Tier | Source |
|---|---|---|---|---|
| **Industry (Micron view)** | DRAM bit shipments **low-20% growth in each of CY2027 and CY2028**; NAND mid-20%; "supply still constrained" | — | A (FQ4'26 call, 30 Sep 2026) | [guru3d](https://www.guru3d.com/story/micron-expects-dram-and-nand-supply-to-tighten-further-through-2028/), [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-micron-technology-q4-earnings-call-highlights-2026-09-30/) |
| **Industry (Counterpoint, realised)** | Q3 2026 DRAM bits **~+4% YoY** | — | A | [Counterpoint](https://counterpointresearch.com/cn/insights/dram-super-cycle-nears-dollar-200b) |
| **SK hynix** | ~**550k DRAM wafers/month** (incl. ~200k Wuxi); Q3 PP&E spend KRW 12.7tn (12% of revenue) | **2027 capex "will rise significantly from 2026"** — leading-edge capacity, first Yongin fab ramp, infrastructure; no figure, due January; target **~1m wafers/month by 2030**; M15X ~40k wpm 2H26 → ~80k 2027 (TrendForce) *or* 50k in 2027 (Korea Times) — **unresolved**; Yongin first tool-in pulled to Feb 2027; shells built fast, clean rooms opened in phases | A/B | [Q3 call via stockhub](https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call), [finsee](https://finsee.ai/earnings/skhy/2026/q3/en/), [TrendForce 5 Jun 2026](https://www.trendforce.com/news/2026/06/05/news-sk-hynix-reportedly-to-double-dram-capacity-to-1m-monthly-wafers-by-2030-speeds-yongin-expansion/), [Korea Times](https://www.koreatimes.co.kr/business/companies/20260630/samsung-sk-chip-investment-timelines-leave-room-for-adjustment) |
| **Samsung** | HBM wafer input ~**180k/month 2026 → ~250k 2027 (+~40%)** | P5 Pyeongtaek operational 2028; POs from 2Q27 (~150k wpm-equivalent); KRW 2,100tn through 2040 | B/C | [DCD](https://www.datacenterdynamics.com/en/news/samsung-and-sk-hynix-to-scale-up-memory-production-capacity-in-2026-to-meet-ai-demand), [sammyfans](https://www.sammyfans.com/2026/09/22/samsung-and-sk-hynix-accelerate-hbm-production/amp/) |
| **Micron** | FY26 capex **~$27.4bn**; **~$25bn in 1H FY27, 2H higher**, mostly construction for clean rooms late CY2028+; HBM wafers reportedly +60k to ~100k/month by end-2026 | ID1 Idaho mid-2027; ID2 late 2028; Singapore NAND 2H28; New York ~2030 | A/B | [storagenewsletter](https://www.storagenewsletter.com/?p=305727), [TrendForce 4 Sep 2026](https://www.trendforce.com/news/2026/09/04/news-micron-reportedly-to-add-60k-hbm-wafersm-reaching-100k-by-year-end-to-narrow-gap-with-samsung-sk-hynix/) |
| **CXMT** | ~**300k wspm** now; est. ~350k end-2026, 420k end-2027, 500k end-2028; throughput +~70% YoY (Omdia) | second Beijing DRAM fab | C — §4 | [tweaktown](https://tweaktown.com/news/112680/chinas-cxmt-is-on-track-to-nearly-match-microns-dram-production-capacity-by-the-end-of-2026/index.html), [xenospectrum](https://xenospectrum.com/en/cxmt-2026-dram-wafer-capacity-micron-350k-wspm/) |

**Timing.** Greenfield capacity is **2027–2028-loaded**: M15X (2H26–27), Micron ID1 (mid-2027), Yongin (2027–28), Samsung P5 (2028), Micron ID2 (late 2028). Micron's low-20% bit growth for 2027–28 is a *supplier's* number; suppliers under-forecast their own bit growth at every prior peak. **The capex now being committed is the capex that ends this cycle. It lands 2027–2029, not in the next two quarters.** The Korea Herald framing — "supply, not demand, will define the next memory cycle" ([Korea Herald](https://www.koreaherald.com/article/10805993)) — is correct.

---

## 3. HBM

### 3.1 HBM3E → HBM4 transition timing

- **SK hynix: HBM4 becomes the mainstream HBM product in 4Q26, shipments and revenue surpassing HBM3E** (28 Oct 2026) [A/B] ([sammyfans](https://www.sammyfans.com/2026/10/28/sk-hynix-q3-margin-hits-record-80-secures-14-ltas-with-memory-supply-booked-to-2029/amp/), [technews.tw](https://finance.technews.tw/2026/10/28/sk-hynixs-third-quarter-revenue-hit-a-record-high-of-over-100-trillion-won/)).
- **Samsung: "strong HBM4 sales" cited in Q3 2026 results** (29 Oct 2026) [A] ([Samsung Newsroom](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results)).
- Rubin HBM4 shipments began Feb–Mar 2026, Samsung first ([TrendForce 9 Mar 2026](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%e2%80%afhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)).
- **2027 HBM blended ASP +121% (TrendForce, 6 Oct 2026, via C)** ([siliconanalysts](https://siliconanalysts.com/market/trendforce-2027-hbm-blended-asp-to-jump-121-as-hbm4-hbm4e-mix-shifts-2026-10-06)); TrendForce range **+70–140%** ([Korea Herald](https://biz.heraldcorp.com/article/10852833)).

**The transition is now.** HBM4 crosses HBM3E in the current quarter at SK hynix.

### 3.2 Share at Nvidia; Samsung qualification

| Claim | Figure | Date | Tier | Source |
|---|---|---|---|---|
| Samsung passed Nvidia HBM4 qualification (10 and 11 Gb/s tiers) | yes | ~Feb 2026 | B | [fintool](https://fintool.com/news/samsung-hbm4-nvidia-breakthrough) |
| Nvidia Vera Rubin HBM4 allocation to SK hynix | ~two-thirds | Jan 2026 (Yonhap) | B | [TrendForce 28 Jan 2026](https://www.trendforce.com/news/2026/01/28/news-sk-hynix-reportedly-to-supply-about-two-thirds-of-nvidia-hbm4-samsung-targets-early-delivery/) |
| 2026 HBM4 share | **SK hynix 54% / Samsung 28%** | 1H26 | A (Counterpoint) | [fintool](https://fintool.com/news/samsung-hbm4-nvidia-vera-rubin) |
| 2027 HBM leadership | **Counterpoint expects Samsung to lead HBM next year**, citing HBM4 reception | 5 Nov 2026 | A | [Counterpoint via sammyfans](https://www.sammyfans.com/2026/11/05/samsung-sk-hynix-global-dram-q3-2026-counterpoint-research/amp/) |
| HBM4 pricing between the two | "comparable" | Mar 2026 | B | [TrendForce 9 Mar 2026](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%e2%80%afhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/) |

**Read:** Samsung **has qualified and is shipping HBM4 to Nvidia**; the 2024–25 "Samsung can't qualify" premise is dead, and as of 5 Nov 2026 a research house expects Samsung to *lead* HBM in 2027. SK hynix has gone from near-monopoly on HBM3E to a roughly 55/30/15 split on HBM4. **That is share loss at the margin, by construction, and it is the mechanism by which HBM pricing power erodes before HBM volume does.** Not obtained: a dated Q3/Q4 2026 Nvidia allocation figure.

### 3.3 HBM share of DRAM wafer capacity

| Metric | 2025 | 2026 | 2027 | Tier | Source |
|---|---|---|---|---|---|
| HBM share of total DRAM **wafer input**, top-3 (TrendForce) | ~18% | ~22% | **~30%** | A | [TrendForce 25 Aug 2026](https://www.trendforce.com/presscenter/news/20260825-13198.html), [TrendForce News](https://www.trendforce.com/news/?p=64643) |
| Same, Samsung EVP Kim Taewoo ("wafer capacity") | — | ~20% | ~30% | B (via Reuters) | [TrendForce News](https://www.trendforce.com/news/?p=63636) |
| HBM share of DRAM **bit supply** (TrendForce) | ~8% | ~9% | **~13%** | A | same |
| HBM + server RDIMM share of DRAM bits, 2026 | — | **51%** | — | A | same |
| Wafer area per bit, HBM vs conventional | ~3x | | | A/C | same |

**This arithmetic holds commodity DRAM up.** 30% of wafers producing 13% of bits in 2027 means ~17 points of wafer capacity are "lost" to HBM's area penalty — larger than the three majors' entire 2027 greenfield. **HBM's wafer drain is the cycle's load-bearing wall.** If HBM demand disappoints, those wafers revert to commodity DRAM and the flood is immediate because they are already built.

### 3.4 Sold out through 2027? On what terms — locked or renegotiable?

**Sold-out claims (supplier statements):**
- SK hynix (28 Oct 2026): DRAM and HBM "effectively all sold out for the next three years, through 2029"; **14 LTAs covering >50% of 2027 and 2028 capacity**; shortage through 2030 ([sammyfans](https://www.sammyfans.com/2026/10/28/sk-hynix-q3-margin-hits-record-80-secures-14-ltas-with-memory-supply-booked-to-2029/amp/), [guru3d](https://www.guru3d.com/story/sk-hynix-posts-record-quarter-and-expects-memory-shortage-through-2030/), [xenospectrum](https://xenospectrum.com/en/sk-hynix-earnings-supply-contracts/)).
- Samsung CFO (29 Oct 2026): 2027 memory demand "far exceed[s] supply" ([Light Reading](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter)).
- Micron (30 Sep 2026): tightness through 2028 ([guru3d](https://www.guru3d.com/story/micron-expects-dram-and-nand-supply-to-tighten-further-through-2028/)).

**Terms:**
- **SK hynix: "2027 HBM supply talks with major customers are complete, with pricing set to reflect value"** (28 Oct 2026) — no price disclosed ([mt.co.kr](https://www.mt.co.kr/en/industry/2026/10/28/2026102809242617566)). In July it was still negotiating and said HBM pricing "does not simply track conventional DRAM" ([digitaltoday](https://www.digitaltoday.co.kr/en/view/86830/sk-hynix-wraps-up-lta-talks-with-about-10-customers-including-core-clients-negotiating-2027-volumes-and-prices)).
- **Those talks were stuck from 2Q26 to at least mid-August 2026** (TrendForce HBM bulletin, 17 Aug 2026) ([TrendForce RP260817WP3](https://www.trendforce.com/research/download/RP260817WP3)). A quarter-long stall with the dominant buyer is not what a price-taker customer looks like.
- **Samsung sought "more than double" current HBM prices for 2027 from Nvidia and Broadcom; final stage 6 Oct 2026** ([sammyfans](https://www.sammyfans.com/2026/10/06/samsung-hbm4-price-talks-enter-final-stage/amp/)). **Micron contracted most 2027 HBM earlier, at higher prices** ([it-daily](https://www.it-daily.net/?p=189921)).
- **Price ceilings exist: "some long-term agreements signed after 2Q26 include price ceilings"** (TrendForce) while still projecting HBM +70–140% in 2027 ([Korea Herald](https://biz.heraldcorp.com/article/10852833)).
- 2026 HBM4 unit price to Nvidia ~$560, >50% above HBM3E ([digitimes](https://www.digitimes.com/news/a20251106PD236.html)) [B]. Nvidia's reported ~15% server price rise (Aug 2026) read as room for HBM +50% in 2027 ([TrendForce 25 Aug 2026](https://www.trendforce.com/news/2026/08/25/news-nvidias-reported-15-server-hike-boosts-samsung-sk-hynix-with-hbm-prices-potentially-up-50-in-2027/)).

**Answer.** HBM is **volume-locked** for 2027 (talks complete; LTAs >50% of 2027–28). It is **not price-locked in the Owner's favour**: (a) HBM is priced annually; (b) post-2Q26 LTAs carry *ceilings* — capped upside for the supplier; (c) the 2027 talks stalled a quarter over price; (d) Nvidia now has three qualified sources. **"Sold out through 2029" is a volume statement; in a three-supplier market with annual pricing, price, not volume, absorbs the downturn.** I found **no evidence of take-or-pay or price floors in any of the 14 LTAs** (§12). That is the question for 巴爺爺 / Peter to put to management.

---

## 4. The CXMT question

**Caution applied.** This firm blacklisted a source for mis-reporting a CXMT-related MU price print. Every CXMT figure below is tiered and most are [C]. Nothing from `tradingkey.com`.

| Item | Finding | Date | Tier | Source |
|---|---|---|---|---|
| Revenue share | **9.5% of global DRAM revenue 2Q26** (from 7.6% 1Q26), 4th (TrendForce); **9% in 3Q26, down from 10%** (Counterpoint) | 2Q–3Q26 | A | [Korea Herald/TrendForce](https://biz.heraldcorp.com/article/10866656), [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share) |
| Bit share 2026 | **6.7% of global DRAM bit supply** (Hanwha Securities); 11.3% of the year's *net increase* in bits — a different metric | 2026E | B | [xenospectrum relaying Hanwha](https://xenospectrum.com/en/cxmt-dram-supply-growth-2027/) |
| Capacity | ~300k wspm now (Hefei x2 + Beijing); ~350k end-2026; 420k end-2027; 500k end-2028 | est. | C | [tweaktown](https://tweaktown.com/news/112680/chinas-cxmt-is-on-track-to-nearly-match-microns-dram-production-capacity-by-the-end-of-2026/index.html), [Tom's Hardware](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-and-ymtc-to-expand-memory-output) |
| Node / product | DUV multi-patterning, no EUV; DDR5 reportedly >9,000 MT/s on an AMD platform | Aug 2026 | B | [TrendForce 18 Aug 2026](https://www.trendforce.com/news/2026/08/18/news-cxmt-ddr5-reportedly-tops-9000-mts-on-amd-platform-narrowing-performance-gap-with-global-leaders/) |
| HBM | HBM3 8-high on 16nm, **yields ~25%**; mass production targeted end-2026; "20% of capacity (~60k wafers) to HBM3" — **single secondary citation**; **IPO prospectus contained no HBM project** | 2026 | C / B (prospectus point) | [kucoin](https://www.kucoin.com/news/flash/cxmt-begins-hbm3-production-for-ai-processors-targets-2026-mass-production), [igorslab](https://www.igorslab.de/en/cxmt-shifts-20-percent-of-dram-capacity-to-hbm3-chinas-ai-strategy-gets-a-memory-upgrade/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/cxmt-closes-up-466-percent-in-shanghai-debut-with-no-hbm-project-in-its-ipo-prospectus) |
| IPO | **Listed Shanghai STAR 27 Jul 2026 (688825)**; raised **RMB 57.92bn (~$8.5bn)** at RMB 8.66; **+466% day one**; largest A-share IPO of 2026 | 27 Jul 2026 | B | [euronews](https://euronews.com/business/2026/07/27/china-memory-chipmaker-cxmts-shares-soar-in-blockbuster-listing), [TrendForce datatrack](https://datatrack.trendforce.com/blog/content/61608/cxmt-lists-on-the-star-market-as-chinas-dram-localization-enters-a-capital-intensive-expansion-phase) |
| Export controls | **Not on the Entity List as of mid-2026**; interagency approved listing in 2025 but Commerce did not publish; BIS added 52 Chinese entities 21 Jul 2026 — **unclear if CXMT included**; Affiliates Rule effective date pushed to **10 Nov 2026** (yesterday) — status unverified; MATCH Act pending; tools limited to DUV | mid-2026 | B | [Malay Mail/Reuters](https://www.malaymail.com/news/world/2026/06/18/deepseek-cxmt-among-chinese-firms-awaiting-us-entity-list-action-as-washington-weighs-trade-risks/224127), [Miller & Chevalier](https://www.millerchevalier.com/publication/bis-export-controls-2025-year-review-and-2026-mid-year-update), [CSIS](https://www.csis.org/analysis/entity-list-additions-cool-their-slowest-pace-2008) |
| 2028 forecasts | **Counterpoint base case 11% bit share (9% revenue) by 2028; 20% bit share ~2035**; **Nomura 18% by end-2028** | 2026 | A/B | [Counterpoint](https://counterpointresearch.com/cn/insights/cxmt-stock-market-big-three-memory-club), [xenospectrum](https://xenospectrum.com/en/cxmt-dram-share-q3-2026/) |
| "Dan Niles: CXMT 20% by 2028" | **Could not trace to Niles.** The 20% figure matches Counterpoint's ~2035 milestone, not 2028. **[UNVERIFIED] — do not use** | — | UNVERIFIED | [TIKR](https://www.tikr.com/blog/microns-real-risk-chinas-cxmt-targets-20-by-2028-warns-dan-niles) |
| Absorption | TrendForce/Counterpoint: China's AI and cloud boom could soak up CXMT/YMTC new supply through 2027; HBM4 mix shift to pressure CXMT revenue share from 4Q26 | 2026 | A | [TrendForce News](https://www.trendforce.com/news/?p=64555) |

**Assessment.** CXMT is a **commodity-DRAM** threat with a 2027–28 fuse and **not an HBM threat on any horizon that matters to SKHY**: DUV-only, 25% HBM3 yields, no HBM in its own prospectus, and HBM3 is two generations behind HBM4. Its ~9% revenue / ~7% bit share is real and growing, and its ~$8.5bn IPO funds the 350k→500k wspm plan. **The export-control position is unresolved rather than tightening**: approved-but-unpublished Entity List action, and an Affiliates Rule whose effective date was yesterday. For the cycle, CXMT matters as the **marginal bit supplier into the DDR4/LPDDR4X/consumer segment that is already at price plateau** — it accelerates the commodity roll-over, it does not cause it.

---

## 5. Demand-side durability

### 5.1 DRAM bit demand mix — AI server vs PC / mobile

| Metric | Figure | Date | Tier | Source |
|---|---|---|---|---|
| Server share of DRAM **bits**, 2026 | **~40%** | Gartner 2Q26 | A | [Gartner](https://www.gartner.com/en/documents/8042733) |
| Server share of DRAM **revenue**, 2026 | **~47%** | same | A | same |
| HBM + server RDIMM share of DRAM bits, 2026 | **51%** | TrendForce | A | [TrendForce News](https://www.trendforce.com/news/?p=64643) |
| PC/smartphone production impact from wafer reallocation | **~12% reduction** | Gartner 2Q26 | A | same Gartner |
| 2026 PC shipments | **−11.3%** (IDC; from −2.4% in Nov 2025); Gartner −10.4% | Mar 2026 | A | [IDC via Tom's Hardware](https://www.tomshardware.com/desktops/gaming-pcs/idc-slashes-2026-pc-shipment-forecast-amid-memory-shortages-total-pc-market-value-to-nonetheless-increase-to-usd274-billion-due-to-ongoing-price-hikes), [mactech](https://www.mactech.com/2026/03/12/idc-cuts-2026-pc-outlook-to-11-3-as-memory-shortages-and-supply-chain-disruptions-persist-into-2027) |
| 2026 smartphone shipments | **−12.9% (IDC); −12%, steepest on record, <1.1bn units, lowest since 2013 (Counterpoint)**; sub-$50 phones "could cease to exist" | Feb–Mar 2026 | A | [ictbusiness](https://new.ictbusiness.biz/analysis/smartphone-shipments-in-2026-to-see-sharpest-decline-on-record), [The Register](https://www.theregister.com/2026/02/27/memory_drought_pcs_phones_suck/) |
| Enterprise SSD bit demand 2026 | **>80% YoY** | TrendForce | A | [TrendForce](https://www.trendforce.com/news/?p=49679) |

**Not obtained:** PC and mobile bit percentages individually. The residual ~60% of bits outside server is the part of the market **already in unit decline of 10–13%** and already at price plateau.

### 5.2 If hyperscaler capex plateaus

Three facts, then the inference.

1. **The cycle is price, not volume.** Q3 2026 DRAM bits +4% YoY, revenue +369% (Counterpoint). Industry bit growth guided low-20s for 2027 (Micron).
2. **Hyperscaler capex dollars are still accelerating (+108% YoY, +22% QoQ in Q3) but the guidance-raise cadence stopped in October** (§1). My August finding was growth plateauing near 80%; the October round confirms the plateau in *rate* and, for the first time, in *2026 guidance level* (~$730bn then, ~$730bn now). Alphabet alone has signalled 2027 "significantly" higher.
3. **A share of capex is memory price, not memory units.** One source attributes $25bn of Microsoft's earlier $190bn figure to component pricing ([paasa](https://paasa.com/blog/the-capex-verdict-what-fy-2027-guidance-signals-about-ai-margins)) [C]; two hyperscalers cited memory costs in raising capex (August baseline).

**Inference (mine, not sourced):** if 2027 hyperscaler capex is flat in dollars and memory prices rise another 50% as TrendForce projects for HBM, hyperscalers buy **fewer memory units**, not more — price inflation self-corrects demand. The suppliers' "demand far exceeds supply" is therefore conditional on capex dollars *continuing to rise*, and Alphabet is the only one of four to have said so for 2027. Memory *bit* demand growth would not collapse on a capex plateau — server bits are ~40% and growing — but **price growth would**, and price is ~99% of this cycle's revenue growth. **The thesis that memory is a secular rather than cyclical story rests on bits; the earnings rest on price.** That distinction is the whole of the SKHY risk.

---

## 6. The cycle-turn checklist — observable, dated indicators

Each indicator has preceded prior memory-cycle peaks. Status as of 11 Nov 2026.

| # | Indicator | Current reading | Date | Status |
|---|---|---|---|---|
| 1 | **Spot falls below contract** | DDR4 spot $46.82 still *above* official quotes; DDR5 spot rising; TrendForce flags "correction expectations" | 3 Nov 2026 | **NOT FLASHING** (amber language) |
| 2a | **DRAM contract momentum rolls over while positive** | 1Q26 +93–98% → 2Q26 +58–63% → 3Q26 +13–18% → 4Q26 +10–15%; three quarters of deceleration; consumer/mobile at "flat to slightly higher"; no 1Q27 number published | 30 Sep / 30 Oct 2026 | **FLASHING for consumer & mobile; DECELERATING (not rolled) for blended** |
| 2b | **NAND contract momentum rolls over** | October 2026 flat after 21 months; all wafer grades flat | 30 Oct 2026 | **FLASHING** |
| 3 | **Customer inventory build** | PC/consumer: "customer inventories are growing, notebook shipments sluggish" (TrendForce); hyperscaler/server inventory weeks: no figure found | 30 Oct 2026 | **FLASHING for consumer; NOT OBTAINABLE for hyperscalers** |
| 4 | **All three majors raise capex guidance in the same window** | Micron FY27 ~$25bn 1H + higher 2H, record (30 Sep); SK hynix 2027 "will rise significantly" (28 Oct); Samsung HBM wafers +40% 2027, P5 (29 Oct); plus SK hynix 550k→1m wafers by 2030 and CXMT ~$8.5bn IPO proceeds | 30 Sep–29 Oct 2026 | **FLASHING** |
| 5 | **Bit supply growth > bit demand growth** | Q3 bits +4% YoY vs supply guided low-20s for 2027; greenfield lands 2027–28 | — | **NOT FLASHING YET — scheduled for 2H27–2028** (BI: balance 4Q27, oversupply 2028) |
| 6 | **Hyperscaler capex guidance-raise cadence stops** | October 2026 round: Alphabet held, Microsoft ~$170bn (lower print), Amazon held, Meta floor +$5bn; aggregate ~$730bn flat vs August | 28–30 Oct 2026 | **FLASHING (first time this cycle)** |
| 7 | **Second-source qualification at the dominant HBM buyer** | Samsung qualified HBM4 at Nvidia (Feb 2026); Counterpoint expects Samsung to lead HBM 2027 (5 Nov) | Feb / Nov 2026 | **FLASHING** |
| 8 | **Price ceilings / buyer-favourable terms in LTAs** | TrendForce: post-2Q26 LTAs include price ceilings; 2027 HBM talks stalled a quarter | Aug–Oct 2026 | **FLASHING (structural)** |
| 9 | **End-market demand destruction** | PC −11.3%, smartphones −12 to −13% in 2026 | Mar 2026 | **FLASHING** |
| 10 | **Research-house turn** | Bloomberg Intelligence (Jul 2026): shortage peaked 2Q26, balance 4Q27, oversupply 2028; Citi: peak 2Q27 (compiled table); TrendForce language softened to "gradual" | Jul–Oct 2026 | **FLASHING (partial)** |
| 11 | **Stocks sell off on record prints** | SK hynix ordinary 1,526,000 → 1,132,000 won, **−25.8%** 29 Oct→6 Nov; SKHY ~$164.70 (28 Oct) → ~$124–127 (5–6 Nov); Samsung/SK hynix lost ~KRW 193tn on 5 Nov alone | 29 Oct–6 Nov 2026 | **FLASHING** — see §6.1 |
| 12 | **Supplier share loss while margins peak** | SK hynix DRAM revenue share 33% → 29% YoY in the 80%-margin quarter | 5 Nov 2026 | **FLASHING** |

**Scorecard.** Of the four classical indicators (1, 2, 3, 4): **one fully flashing (4), two partially (2, 3), one not (1).** Of the twelve: **eight flashing or partially, two not, one scheduled, one not obtainable.** This is more amber than at any prior point in the cycle. It is **not** the configuration of a peak already passed — at a peak, indicator 1 has flipped and indicator 5 is realised. It **is** the configuration of the two to four quarters before one, and the market has started pricing it (indicator 11).

### 6.1 The 29 Oct–6 Nov drawdown, dated — what moved and what did not

The technical desk asked whether the 20%+ post-print selloff reflected a sector datum. **Answer: nothing in the memory supply/price data turned in that window; the drawdown is explained by four dated events, three of them demand-side or policy-side, one a share print.**

| Date | Event | Effect | Source |
|---|---|---|---|
| 28 Oct | SK hynix Q3: OP beat (83.3 vs 77.0tn), **net profit missed by a third on KRW 32.6tn non-operating losses**; 2027 capex "significantly" higher; ordinary **+10.89%** on the day | peak of the move | [Korea Times](https://www.koreatimes.co.kr/business/companies/20261028/sk-hynix-logs-record-q3-operating-profit-of-628-bil), [Korea Herald](https://mbiz.heraldcorp.com/article/10890162) |
| 28–30 Oct | Hyperscaler Q3 round: Alphabet **held** 2026 capex; Microsoft **~$170bn**; Amazon held; Meta floor +$5bn — first round without a broad raise | demand-side second derivative | [Walnut](https://walnutinvest.com/stats/ai-capex-statistics) |
| 29 Oct | Samsung Q3: OP **107.44tn vs 107.66tn consensus — slight miss**; Bloomberg headline "chip profit misses estimates" | SKHY **−7.9% on 30 Oct** to $149.21 | [tech-insider](https://tech-insider.org/samsung-q3-2026-chip-profit-miss-107-44-trillion-won-ai-hbm4/), [fourweekmba](https://fourweekmba.com/ai-samsungs-chips-earned-99-of-its-record-107-4t-won-profit/), [debelegger](https://www.debelegger.nl/en/stock/SKHY.US) |
| ~30 Oct | **NAND October contract flat** after 21 months (TheElec/DRAMeXchange) | first memory-price roll-over datum | [fourweekmba](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/) |
| 3 Nov | KOSPI −2.5% open; Samsung/SK hynix −5% early on "AI profitability concerns" | | [fourweekmba](https://fourweekmba.com/ai-samsung-sk-hynix-lose-118b-by-midday-as-kospi-slides-4/) |
| 4 Nov (US) | Micron −7%, SanDisk −8% on "slowing memory demand concerns" (Yonhap); **no Micron guide or datum found behind it** | SKHY −5.12% to $143.07 | [Yonhap via fourweekmba](https://fourweekmba.com/ai-samsung-sk-hynix-lose-144b-as-kospi-closes-down-5-3/), [chartrow](https://chartrow.com/quote/skhy/weekly-returns) |
| 5 Nov | **US midterms: Democratic sweep → fears of data-centre restrictions**; SOX −3.1% to six-month low; Texas Governor-elect: "we need to stop what we are doing with data centers"; KOSPI **−5.3%**, SK hynix **−9.5% to −10.4%** to 1,132,000 won, Samsung −7.6%; **SKHY −13.4%** (~$124); Counterpoint publishes Q3 share: **SK hynix 29% (from 33%)**, Samsung to lead HBM 2027; Counterpoint also says prices still rising | the bulk of the move | [Motley Fool 5 Nov](https://www.fool.com/investing/2026/11/05/why-sk-hynix-plunged-today/), [Korea Herald](https://biz.heraldcorp.com/article/10928173), [Yonhap via stockhub](https://stockhub.kr/en/news/news_8f5d58b1c032), [Counterpoint via sammyfans](https://www.sammyfans.com/2026/11/05/samsung-sk-hynix-global-dram-q3-2026-counterpoint-research/amp/) |
| 6 Nov | Further slide; ordinary closes **1,132,000 won = −25.8% from 29 Oct**; ADS ~$127 (technical desk) | | [tikr](https://www.tikr.com/blog/sk-hynix-is-down-57-from-its-high-with-half-of-2027-and-2028-capacity-already-contracted) |

**What did *not* happen in the window:** no DRAM contract-price print rolled over (DDR4 fixed price made a record in October); no new Samsung qualification (that was February); no Micron guide (next is December); no CXMT headline (CXMT listed 27 July). **The "China competition" attribution in some coverage is stale colour, not a dated event.**

**Interpretation.** Roughly half the move (30 Oct, 3 Nov) is **the market re-rating the demand side** — a Samsung miss and a hyperscaler round that stopped raising — and half (5 Nov) is **a policy shock** that may reverse. Neither is a supply-side cycle datum. But the pattern — a memory stock falling 26% in six sessions after an 80%-margin record quarter — is itself the classic indicator 11: the market is pricing the peak before the data confirms it. **I weight it as a genuine cycle signal with a political overlay, not as noise.** Note also that SK hynix is described as the most crowded, most leveraged proxy for the AI-memory trade ([HL](https://www.hl.co.uk/news/samsung-sk-hynix-slide-amid-nvidia-financing-worries-china-competition)); crowding amplifies but does not create the signal.

---

## 7. Peers and relative positioning — SK hynix vs Samsung vs Micron

| | SK hynix | Samsung (DS) | Micron |
|---|---|---|---|
| **Latest quarter OP margin** | **80%** (Q3 2026) | ~72% (DS, Q3 2026) | FQ4'26 non-GAAP EPS $33.42 on $54.2bn; margin not extracted |
| **DRAM revenue share Q3 2026** | 29% (−4pp YoY) | **38%** | 21% (−5pp YoY) |
| **HBM4 share 2026 (Counterpoint)** | **54%** | 28% | remainder (~18%) |
| **2027 HBM outlook** | majority supplier, volume-locked, talks complete | **Counterpoint expects to lead** | most 2027 volume contracted early |
| **2027 pricing lock** | ceilings in newer LTAs; annual pricing | seeking >2x; final stage | contracted higher |
| **Supply response** | 550k→1m wafers by 2030; 2027 capex "significantly" up; Yongin Feb 2027 | KRW 2,100tn to 2040; P5 2028; HBM wafers +40% 2027 | ~$25bn 1H FY27, higher 2H; ID1 mid-2027 |
| **Forward P/E (pre-selloff snapshots)** | ~6x (Aug); ~5–5.5x on consensus, ~4x on 2028E (Oct, Creative Strategies) | 4.8x 12m-fwd (Jul, LS Securities); ~5x normalised | ~6x (Aug) |
| **Post-selloff** | ordinary −25.8% in six sessions; **ADS at ~$124–127 vs Owner's $129 and $149 IPO** | — | — |

Sources: [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share), [Motley Fool Aug](https://www.fool.com/investing/2026/08/16/sk-hynixs-stock-trades-at-around-5-times-next-year/), [Creative Strategies](https://www.thediligencestack.com/p/bet-on-bits-part-2-what-the-memory), [Korea Herald/LS Securities](https://mbiz.heraldcorp.com/article/10804171), [cryptobriefing](https://cryptobriefing.com/micron-6x-earnings-38-billion-capacity-2028/). **No November 2026 multiple obtained** (§12); after a ~26% fall, the SK hynix multiple on unchanged consensus would be roughly **4–4.5x** — **estimate, mine**.

**Is SKHY the cheap or expensive way to own the cycle?**
- **On headline multiple:** all three sit at 4–6x forward, a steep discount to the S&P's ~20x — and all three are at that multiple *because* the market assumes the "E" is peak. **A 5x multiple on 80% margins is not cheap; it is the market saying the margins are not durable.** Samsung's 12-month forward PER (4.8x) was the lowest of the three in the last dated comparison.
- **On cycle exposure:** SKHY is the **purest and highest-margin** play — 80% OP margin, majority HBM4 share, HBM4 crossing over this quarter. It is therefore the **highest-beta** way to own the cycle, which the last six sessions demonstrated. Samsung is the **cheaper, lower-beta** way with share momentum (38% DRAM, expected HBM leader 2027) but a foundry/System LSI drag. Micron is the **US-listed** proxy with the largest relative capex wave ahead.
- **Verdict:** SKHY is the **expensive way on a risk-adjusted basis** — it carries the most margin to lose, the most share to lose at Nvidia, and the heaviest crowding — and the **cheap way only if the Owner believes HBM demand and pricing hold through 2028.** The Owner's $129 cost is at the current price; there is no embedded cushion.

---

## 8. Life-cycle stage & evidence

| Sub-industry | Stage | Evidence |
|---|---|---|
| **DRAM (overall)** | **Mature cyclical, late up-leg** | Peak rate of price increase 1Q26 (+93–98%); three quarters of deceleration; bits +4% YoY; supply response committed for 2027–29 |
| **HBM** | **Growth segment inside a mature industry** | Bit share 9%→13%, wafer share 22%→30% (2026→27); HBM4 crossover 4Q26; 2027 ASP +70–140%; but three qualified suppliers and price ceilings — growth segment entering its competitive phase |
| **Conventional server DRAM (RDIMM)** | **Cyclical peak zone, structurally tightened by HBM wafer drain** | HBM+RDIMM = 51% of bits; server contract still rising (TrendForce 4 Nov) |
| **Consumer / mobile DRAM** | **Already at plateau** | "flat to slightly higher" 4Q26; PC −11%, phones −12–13%; CXMT marginal supplier here |
| **NAND** | **Mature; momentum rolled** | October flat after 21 months; eSSD the exception |

**Cyclical or secular?** The **bit** story (AI servers 40% of bits and rising; HBM wafer drain) is secular. The **price** story — which is 99% of this cycle's revenue growth — is cyclical and is at its late stage. **My thesis rests on the cyclical layer being closer to its end than its beginning; the bull thesis rests on the secular layer carrying price for two more years.** The August report called memory "cyclical up-leg inside a secular growth trend." That still holds; what has changed is that the up-leg's deceleration is now three quarters old.

---

## 9. Competitive map

- **Leaders / pricing power:** Samsung (38% DRAM share, expected 2027 HBM leader, lowest multiple) and SK hynix (HBM4 majority, 80% margin, losing commodity share). Pricing power peaked in 1H26 when talks stalled and ceilings entered LTAs.
- **Challenger:** Micron (21% DRAM share, HBM wafers to ~100k/month, largest relative greenfield).
- **Disruptor (commodity):** CXMT (9% revenue share, DDR5 at 9,000 MT/s, 350k→500k wspm, no HBM path).
- **Buyers with rising leverage:** Nvidia (three qualified HBM4 sources, annual pricing, reported ~15% server price rise); hyperscalers (LTAs >50% of 2027–28 capacity — which is *their* lock on volume as much as the supplier's lock on demand).
- **Pricing-power ranking update vs August:** memory was #2 behind power/grid. **It stays #2 for the next two quarters on the data, but the direction is now down, not up.** Power/grid remains #1 and is not decelerating.

---

## 10. The industry bear case at full strength

1. **The cycle is price, not volume.** Q3 2026 DRAM bits +4% YoY, revenue +369% ([Counterpoint](https://counterpointresearch.com/cn/insights/dram-super-cycle-nears-dollar-200b)). When price stops rising, revenue growth collapses to bit growth (~20%) and margins mean-revert from 80%.
2. **The peak of the shortage is already behind us** per Bloomberg Intelligence (Jul 2026): peaked 2Q26, balance 4Q27, oversupply 2028 ([247wallst](https://247wallst.com/investing/2026/07/06/wait-michael-burry-is-right-about-the-memory-boom-ending-this-analyst-says-yes/)). TrendForce's own quarterly series agrees on the *rate* peak (1Q26).
3. **The supply response is committed and funded.** SK hynix 550k→1m wafers, 2027 capex "significantly" up; Samsung KRW 2,100tn; Micron record FY27 capex; CXMT ~$8.5bn IPO. All three majors raised in a six-week window — the classic peak marker.
4. **HBM pricing power is eroding before volume.** Samsung qualified and expected to lead 2027 (Counterpoint); 2027 talks stalled a quarter; price ceilings in post-2Q26 LTAs; SK hynix HBM4 share 54%, down from near-monopoly.
5. **NAND has already rolled over** (October flat after 21 months) and consumer/mobile DRAM is at plateau; **60% of DRAM bits sit in markets with 10–13% unit declines.**
6. **The demand side stopped raising.** October hyperscaler round flat at ~$730bn; capex now partly memory-price inflation that self-corrects unit demand (§5.2); secondary reporting (NYT via [tech-insider](https://tech-insider.org/big-tech-720-billion-data-center-spending-free-cash-flow-2026/)) that every big-four name except Microsoft is now FCF-negative — **[UNVERIFIED] against filings**.
7. **Policy shock.** Post-midterm data-centre regulation fears took the SOX to a six-month low on 5 Nov; no rule proposed yet, but the political direction changed.
8. **Share loss at peak margin.** SK hynix −4pp DRAM share YoY; Micron −5pp. Samsung is taking share while the others take price.
9. **Technology risk to memory intensity.** Google compression research cut Micron 7% in March 2026 ([MarketBeat](https://www.marketbeat.com/instant-alerts/micron-technology-nasdaqmu-shares-down-7-heres-why-2026-03-26/)); KV-cache offload to QLC SSD is already shifting demand from DRAM to NAND.
10. **CXMT** adds 50k–100k wspm a year into exactly the commodity segments already rolling, with export controls unresolved rather than tightening.
11. **The non-operating hole.** SK hynix's KRW 32.6tn net non-operating loss in Q3 — a third of operating profit — is unexplained in anything I could retrieve. **Handed to 巴爺爺.**
12. **Market reaction function.** −26% in six sessions on a record print, in the most crowded proxy for the trade. In prior cycles memory equities peaked before contract prices did — **analyst recollection, not sourced here; treat as context, not evidence.**

---

## 11. Where SK hynix (SKHY) sits · Sector view · Falsifiers

### 11.1 Where the company sits

SK hynix is the **highest-quality, highest-beta** position in a late-up-leg cyclical: 80% operating margin, majority HBM4 supplier, HBM4 crossing over this quarter, 2027 volume locked under 14 LTAs, 2027 capex rising significantly. Against that: DRAM share 33%→29% YoY; HBM4 share ~54% vs near-monopoly on HBM3E; Samsung expected to lead HBM in 2027; price ceilings in its newer contracts; a KRW 32.6tn non-operating loss; and a share price that fell 26% in six sessions on the record print. **Structural tailwind: the HBM wafer drain (§3.3). Structural headwind: three qualified HBM suppliers with annual pricing.** Relative growth: Counterpoint has it growing faster than Micron, slower than Samsung in Q3.

### 11.2 Sector view

**Memory: NEUTRAL (downgraded from the implicit overweight in the 21 Aug report). Confidence 6/10.**

Reasoning: the price data say two more quarters of rising DRAM contract prices (4Q26 +10–15%, 1Q27 "gradual"); HBM4 crossover and +70–140% HBM ASPs in 2027 are real; spot has not flipped. Against that, eight of twelve cycle indicators are flashing or partial, NAND has rolled, the demand side stopped raising, the supply response is funded, and the market has begun pricing the peak. **Neutral means: the sector is no longer a place to add, and not yet a place the data say to exit.** Within memory, Samsung screens as the lower-risk expression; SKHY as the highest-beta. For the Owner's $129 position, this is a **hold-with-tripwires** industry view, not a buy — the committee and Owner decide.

Why not underweight: indicator 1 (spot < contract) and indicator 5 (realised bit oversupply) have not fired, and a 5 Nov policy scare is not a fundamental datum. Why not overweight: a 5x multiple on 80% margins with three capex plans rising simultaneously is the configuration that has punished holders at every prior peak.

### 11.3 Explicit falsifiers

**Would move me to UNDERWEIGHT (any two):**
1. DDR5 spot falls below contract on a TrendForce weekly — not DDR4, DDR5.
2. TrendForce publishes a 1Q27 conventional DRAM forecast of **≤+5% QoQ**, or any negative sub-segment other than consumer/mobile.
3. A hyperscaler cuts 2027 capex guidance in dollars, or Alphabet's "significantly" becomes a number below +30%.
4. Nvidia's 2027 HBM4 allocation to SK hynix drops below 50% in a dated research-house estimate.
5. A second consecutive flat-or-down NAND monthly print and any flat DRAM monthly fixed-price print.

**Would move me back to OVERWEIGHT (any two):**
1. TrendForce 1Q27 conventional DRAM forecast **≥+15% QoQ** with consumer segments re-accelerating.
2. Disclosure that SK hynix's 2027 LTAs carry price floors or take-or-pay, not ceilings.
3. Hyperscaler 2027 guidance round (Jan–Feb 2027) in aggregate ≥+40% YoY.
4. Q4 2026 DRAM bit shipments growing ≥+10% YoY per Counterpoint/TrendForce (i.e. volume joining price).
5. SK hynix HBM4 share at Nvidia confirmed ≥60% for 2027 by a research house.

---

## 12. NOT OBTAINED register

**Blocked / unavailable in this environment (direct fetch unavailable; recorded, not retried):**
- `sec.gov` — SK hynix Form DRS/A (surfaced in search, not opened); Micron 10-K.
- `trendforce.com/research/download/*` — all monthly DRAM/NAND contract-price tables and the 4Q26 Memory Price Forecast (paywalled; titles/abstracts only).
- `reuters.com`, `bloomberg.com`, `barrons.com`, `investors.com` — refused to the search user agent (as in August).
- `counterpointresearch.com` share tables — headline figures via secondary relay only.
- `news.samsung.com` Q3 release — headline only; no DRAM/HBM split.
- Nasdaq/stockanalysis SKHY price history — **no 6 Nov close obtained**; $124–127 range is from two conflicting trackers and the technical desk.

**Firm-blacklisted, deliberately not used:** `tradingkey.com` (surfaced for SKHY earnings coverage; discarded).

**Figures not obtained and not asserted:**
1. **Realised 2Q26 and 3Q26 conventional DRAM contract changes** — 2Q26 is the June forecast (+58–63%); 3Q26 (+13–18%) is second-hand.
2. **A numeric 1Q27 DRAM contract forecast.** None published that I could surface.
3. **Hyperscaler DRAM inventory weeks.** Not disclosed; not estimated by any research house I could reach.
4. **PC and mobile shares of 2026 DRAM bits** individually (server 40% from Gartner is the only anchor).
5. **Terms of SK hynix's 14 LTAs** — price floors, take-or-pay, ceilings. Only TrendForce's generic "some include price ceilings."
6. **2027 HBM4 price agreed by SK hynix.** "Reflect value" is all that was said.
7. **Post-June-2026 Nvidia HBM4 allocation by supplier.**
8. **SK hynix 2027 capex in won** — "significantly higher"; figure due January 2027.
9. **Samsung total DRAM wafer starts** from a single consistent source; realised CY2026 bit growth by maker.
10. **November 2026 forward P/E for any of the three** — the ~4–4.5x for SK hynix is my arithmetic on pre-selloff consensus.
11. **Composition of SK hynix's KRW 32.6tn Q3 non-operating loss.**
12. **CXMT Entity List status after 21 Jul 2026** and the Affiliates Rule's status after 10 Nov 2026.
13. **The "Dan Niles: CXMT 20% by 2028" claim** — could not be traced to Niles; conflicts with Counterpoint (11% by 2028). **Do not use.**
14. **The "$25bn of Microsoft capex is component pricing" figure** — single [C] source.
15. **The NYT "all but Microsoft FCF-negative" claim** — not verified against filings.
16. **Whether the 20 Oct TrendForce "+20% QoQ 4Q26" item is a revision of the 30 Sep +10–15% or a server-weighted sub-index.** Unresolved; I use +10–15%.
17. **The cause of Micron's −7% on 4 Nov** beyond Yonhap's "slowing memory demand concerns" — no datum behind it was found.

---

*Research only. This is industry analysis in support of the Investment Committee; the committee and the Owner decide. Markets cannot be reliably predicted; every forward figure above is a third party's forecast or is marked as my estimate.*

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
