# SKHY — The Memory Cycle: Where We Are, Precisely

**Department 1: Macroeconomic Research · Industry Research**
**Analyst:** Elon Musk, Industry Research Analyst
**Date:** 2026-11-11
**Requested by:** CIO (via CEO)
**Ticker under review:** SKHY (SK hynix ADS, Nasdaq; 0.1 common share per ADS; listed 13 Jul 2026 at $149). **Owner holds at $129.**
**Scope:** The memory cycle, not the company. Financial statements are covered by 巴爺爺 (Dept 2).

> **STATUS: CHECKPOINT 1 — §0, §2, §3, §5.1 filled. Sections marked `[PENDING]` are not yet filled. Do not cite this file until the status line is removed.**

---

## 0. Method, baseline carried forward, and evidentiary standard

**Baseline from `reports/industry/2026-08-21-msft-industry.md` (21 Aug 2026), not re-derived:**
- DRAM pricing tracking **+275–300% 2025→2027** (TrendForce / Introl / tech-insider, as cited there).
- HBM margins **2–3x DDR5**.
- Memory ranked **second on pricing power** behind power/grid equipment.
- Microsoft (29 Apr 2026) and Amazon (30 Jul 2026) both cited memory costs in raising capex guidance.
- Big-four hyperscaler capex **~$732.5bn CY2026E, +78%**, growth rate plateauing near 80%.

This report updates what has moved in the twelve weeks since.

**Confidence tiers:** [A] company disclosure / research house (TrendForce, DRAMeXchange, Gartner, Counterpoint), dated · [B] reputable press reporting a filing or call · [C] secondary aggregator · [UNVERIFIED] widely repeated, no traceable origin.

**Environment:** direct page fetch unavailable; every figure below is from search-result extraction, not full-page retrieval. TrendForce's own monthly contract-price tables are paywalled; where I cite a TrendForce number it is from a TrendForce press release or a TrendForce News item surfaced in search, or from DRAMeXchange data as relayed by TheElec. Blocked hosts in §12. `tradingkey.com` is blacklisted and not cited; it did surface for this name and was discarded.

**Cycle framing used throughout.** A memory cycle turns when **bit supply growth overtakes bit demand growth**, and the turn is visible first in (i) spot falling below contract, (ii) contract-price momentum rolling over while still positive, (iii) customer inventory weeks rising, and (iv) all three majors raising capex guidance in the same window. I score each of these in §6. **Everything else — "sold out through 2029", "shortage through 2030" — is supplier narrative and is treated as such.**

---

## 1. Industry snapshot (Q3 2026 → now)

[PENDING]

---

## 2. Where we are in the cycle — DRAM and NAND contract prices by quarter, 2024 to now

### 2.1 DRAM contract price series (conventional DRAM, TrendForce QoQ, forecast-at-time unless marked realised)

| Quarter | Conventional DRAM contract QoQ | Note | Tier | Source |
|---|---|---|---|---|
| 1Q24 | **+13–18%** | mobile DRAM led | A (forecast) | [TrendForce via iconnect007](https://iconnect007.com/article/139167/dram-contract-prices-projected-to-increase-1318-in-1q24-as-price-surge-continues/139164/,,) |
| 2Q24 | **+3–8%** | increase narrowed, uncertain demand | A (forecast) | [TrendForce via iconnect007](https://iconnect007.com/article/140106/suppliers-aim-to-raise-contract-prices-but-with-uncertain-demand-2q24-dram-price-increase-expected-to-narrow-to-38/140103/ein) |
| 3Q24 | **+8–13%** (revised up ~5pp) | | A (forecast) | [TrendForce via iconnect007](https://iconnect007.com/article/141927/dram-industry-revenue-surges-248-in-2q24-upward-revision-of-contract-price-increase-for-q3/141924/pcb) |
| 4Q24 | **reversed downward** across most applications; server DDR5 the exception | no blended % surfaced | A | [TrendForce press, 27 Feb 2025](https://www.trendforce.com/presscenter/news/20250227-12492.html) |
| 1Q25 | **down**: DDR4 −10–15%, DDR3 −3–8%, LPDDR4X −8–13%, LPDDR5X −3–8% | "passive buyer strategies" | A (forecast) | [TrendForce press, 30 Dec 2024](https://trendforce.com/presscenter/news/20241230-12424.html) |
| 2Q25 | decline eased | no % surfaced | A | TrendForce headline, [search](https://iconnect007.com/article/143054/weak-demand-outlook-and-rising-inventory-and-supply-pressure-dram-prices-down-for-2025/143051/smt) |
| 3Q25 | **sharp rise, legacy-led**: consumer DDR4 +85–90%, LPDDR4X +38–43%, LPDDR5X +10–15% | DDR4 EOL squeeze | A (forecast) | [TrendForce via iconnect007](https://iconnect007.com/article/146462/ddr4-lpddr4-supply-tightens-sharply-in-2h25-as-structural-shortage-drives-strong-price-surge/146459/ein) |
| 4Q25 – 2Q26 | **[PENDING — realised prints not yet obtained]** | | | |
| 3Q26 | **+13–18%** | | A/C (cited second-hand) | [TrendForce via xenospectrum](https://xenospectrum.com/en/memory-spot-q4-demand-divide/) |
| **4Q26 (forecast, 30 Sep 2026)** | **+10–15%** | "AI server demand drives gains, consumer pressure persists" | **A** | [TrendForce press 30 Sep 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html), [evertiq](https://evertiq.com/news/2026-10-02-ai-keeps-memory-prices-climbing-in-q4-as-consumer-demand-weakens) |
| 4Q26 (later item, 20 Oct 2026) | "**~+20% QoQ despite slower gains**" | unclear whether blended conventional or server-weighted | A/UNRESOLVED | [TrendForce News 20 Oct 2026](https://www.trendforce.com/news/2026-10-20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/) |
| 4Q26 (secondary) | +8–13% | untraceable to a TrendForce document | **C — not used** | [hwbusters](https://hwbusters.com/?p=112680) |
| **1Q27** | **No numeric TrendForce forecast found.** Qualitative: "gradual quarterly increases next year"; "bullish momentum for the next three quarters" | | A (qualitative) | [TrendForce News 30 Oct 2026](https://www.trendforce.com/news/?p=51212), [TrendForce press 2 Jun 2026](https://www.trendforce.com/presscenter/news/20260602-13074.html) |

**Monthly fixed-price prints (DRAMeXchange via TheElec):** DDR4 8Gb PC DRAM average fixed transaction price **$27.50 in October 2026, +5.77% MoM, a record** (from $26.00 in September) ([fourweekmba relaying TheElec/DRAMeXchange](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/), [tech-insider](https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/)). [B]

**Reading of the table.** The series shows **two distinct up-legs**: a 2024 recovery that stalled by 4Q24 and turned negative in 1Q25 (the classic short cycle), and then a second, far larger up-leg from 3Q25 that was *legacy-led* at first (DDR4 EOL) and became *AI-server-led* through 2026. The forward curve beyond 4Q26 is **qualitative only** — TrendForce has not published a 1Q27 percentage that I could surface. **That absence is itself information: the research house that has called every quarter since 2024 has, as of 30 Oct 2026, downgraded its language from percentages to "gradual quarterly increases."**

### 2.2 NAND contract price series

| Period | NAND contract | Tier | Source |
|---|---|---|---|
| Jan 2025 → Sep 2026 | **21 consecutive months of increases** (128Gb MLC benchmark) | B | [TheElec/DRAMeXchange via fourweekmba](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/) |
| **4Q26 forecast (30 Sep 2026)** | **overall NAND +15–20% QoQ; enterprise SSD +23–28% QoQ** (hyperscalers raising QLC eSSD orders for KV cache); consumer segments small increases | A | [TrendForce press 30 Sep 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html) |
| **October 2026 realised** | **128Gb MLC NAND unchanged at $30.61 — first flat month in 21.** TrendForce's own October wafer report: MLC, TLC and QLC wafer contract prices **all flat**; "weak consumer demand and elevated wafer costs stopping the upward run and buyers' purchasing interest falling" | **A/B** | [TrendForce NAND wafer contract Oct 2026 (paywalled title)](https://www.trendforce.com/research/download/RP261030YB), [fourweekmba/TheElec](https://fourweekmba.com/ai-dram-prices-hit-a-record-as-nands-21-month-rally-stalls/), [tech-insider](https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/) |
| 1Q27 | TrendForce listing: "off-season prices plateau as MLC faces heavier cuts" (eMMC/UFS) | A (title only) | [TrendForce research tag](https://www.trendforce.com/research-tags/dram?page=12&tab=reports) |

**This is the first hard cycle datum in the report.** NAND contract momentum **rolled over in October 2026** — flat, not down, and in the consumer/wafer benchmark rather than enterprise SSD — four weeks after TrendForce forecast +15–20% for the quarter. One flat print is not a turn; module-maker inventory digestion is the benign explanation offered. But §6 item (ii) is "contract-price momentum rolling over while still positive," and for NAND it has now happened. **DRAM has not** — DDR4 fixed price made a record in the same month.

### 2.3 Spot vs contract

| Indicator | Reading | Date | Tier | Source |
|---|---|---|---|---|
| DDR4 1Gx8 3200 spot | **$46.82, −0.09% WoW — flat**; spot "remained above suppliers' official quotes despite weak demand, fueling correction expectations" | 3 Nov 2026 | A | [TrendForce News](https://www.trendforce.com/news/?p=66203) |
| DDR5 spot | "supply tight"; delivery pressure prompting buyers to raise target prices; one vendor: DDR5 chip spot **+13% since 2 Sep** | 21 Oct / early Nov 2026 | A/C | [TrendForce News 21 Oct 2026](https://www.trendforce.com/news/2026-10-21/insights-memory-spot-price-update-ddr5-supply-tight-ddr4-trading-subdued-despite-0-84-gain-in-mainstream-prices), [servermonkey](https://www.servermonkey.com/blog/october-2026-enterprise-it-market-update.html) |
| DDR4 spot vs contract direction | DDR4 spot fell for the first time in nearly a year as Chinese channel inventory cleared (earlier in 2026) | 2026, undated in snippet | B | [Tom's Hardware](https://www.tomshardware.com/tech-industry/ddr4-spot-prices-fall-for-first-time-in-nearly-a-year-as-chinese-channel-inventory-clears) |
| Retail 32GB DDR5 kit (lowest tracked, Amazon) | **$479.99** (vs $392 cited in my Aug report and $110–140 in Q3 2025) | 2 Nov 2026 | C | [pcserverandparts](https://pcserverandparts.com/news/when-will-ram-prices-go-down-2026/) |

**Reading.** Spot is **still above contract** for DDR4 (TrendForce's own words), and DDR5 spot is still rising. The cycle-turn signature — spot falling *below* contract — **is not present as of 3 Nov 2026.** But the DDR4 spot premium is now described by TrendForce as being sustained "despite weak demand" with "correction expectations" — that is the language used in the two or three months before a spot roll-over, not the language of an accelerating market. **DDR4 is a legacy product being EOL'd by the majors; its spot behaviour is a channel signal, not an AI-demand signal.** DDR5 spot tightness is the better read on the server-driven market and it is still tight.

### 2.4 Rate of change — accelerating, plateauing, or rolling over?

**DRAM: plateauing at a high positive rate. NAND: rolled over in October.**

- DRAM conventional contract QoQ: 3Q26 +13–18% → 4Q26 forecast +10–15% (or ~+20% on the 20 Oct server-weighted item). The headline direction is **"gains narrowing"** — TrendForce's own 30 Oct 2026 phrase for PC DRAM ([TrendForce News](https://www.trendforce.com/news/?p=51212)). The **second derivative is negative; the first derivative is still strongly positive.**
- TrendForce explicitly warned that "if consumer inventory digestion continues to fall short of expectations, market prices face a heightened risk of a downward pull-back" ([TrendForce 30 Sep 2026 via evertiq](https://evertiq.com/news/2026-10-02-ai-keeps-memory-prices-climbing-in-q4-as-consumer-demand-weakens)).
- The bifurcation is the whole story: **server/HBM/eSSD prices still rising double digits; consumer DRAM "flat to slight increases"; mobile DRAM 4Q26 "flat to slightly higher"** ([TrendForce 4Q26 mobile DRAM note via search](https://www.trendforce.com/news/?p=65534)). Consumer has already peaked in rate-of-change terms. The question is only whether AI-server demand is large enough to keep the blended index rising when consumer rolls.

**Verdict on §2: the blended DRAM contract index is in its late up-leg — still rising, rate of increase decelerating, with the consumer sub-index already at plateau and NAND already flat. This is not the peak of the cycle, but it is the first quarter in which a peak is visible from the data rather than only from the bear narrative.**

### 2.5 Supply growth — wafer starts and bit growth by maker

| Maker | Current capacity / supply growth | Planned additions | Tier | Source |
|---|---|---|---|---|
| **Industry (Micron view)** | DRAM bit shipment growth **low-20% range in each of CY2027 and CY2028**, "supply still constrained"; NAND mid-20% | — | A (Micron FQ4'26 call, 30 Sep 2026) | [guru3d](https://www.guru3d.com/story/micron-expects-dram-and-nand-supply-to-tighten-further-through-2028/), [MarketBeat transcript](https://www.marketbeat.com/instant-alerts/transcript-micron-technology-q4-earnings-call-highlights-2026-09-30/) |
| **SK hynix** | **~550k DRAM wafers/month** (incl. ~200k Wuxi, China) | Target **~1m/month by 2030** (Chey Tae-won, Computex Jun 2026 — "double within five years"); **M15X** ~40k wpm 2H26 → ~80k 2027 (TrendForce) *or* 50k in 2027 (Korea Times) — **conflict, unresolved**; **Yongin** first tool-in pulled forward to Feb 2027 from May 2027; 2027 fab plans accelerated by three months | A/B | [TrendForce News 5 Jun 2026](https://www.trendforce.com/news/2026/06/05/news-sk-hynix-reportedly-to-double-dram-capacity-to-1m-monthly-wafers-by-2030-speeds-yongin-expansion/), [Korea Times 30 Jun 2026](https://www.koreatimes.co.kr/business/companies/20260630/samsung-sk-chip-investment-timelines-leave-room-for-adjustment), [PC Gamer](https://pcgamer.com/hardware/memory/to-meet-tremendous-and-humongous-demand-from-ai-customers-sk-hynix-accelerates-2027-fab-plans-by-three-months-with-an-even-fresher-fab-beginning-wafer-production-next-month/) |
| **Samsung** | HBM wafer input ~**180k/month 2026 → ~250k 2027 (+~40%)** | **P5 Pyeongtaek** operational by 2028; POs from 2Q27 possibly supporting ~150k wpm-equivalent investment in 2027; long-term KRW 2,100tn through 2040 | B/C | [DCD](https://www.datacenterdynamics.com/en/news/samsung-and-sk-hynix-to-scale-up-memory-production-capacity-in-2026-to-meet-ai-demand), [sammyfans](https://www.sammyfans.com/2026/09/22/samsung-and-sk-hynix-accelerate-hbm-production/amp/) |
| **Micron** | FY26 capex **~$27.4bn**; **~$25bn in 1H FY27, 2H higher**, mostly construction for clean-room availability late CY2028+; HBM wafers reportedly +60k to ~100k/month by end-2026 | **ID1 Idaho mid-2027; ID2 late 2028; Singapore NAND 2H28; New York ~2030** | A/B | [Micron FQ4'26 call via storagenewsletter](https://www.storagenewsletter.com/?p=305727), [TrendForce News 4 Sep 2026](https://www.trendforce.com/news/2026/09/04/news-micron-reportedly-to-add-60k-hbm-wafersm-reaching-100k-by-year-end-to-narrow-gap-with-samsung-sk-hynix/) |
| **CXMT** | ~**300k wspm** now (Hefei x2 + Beijing); est. **~350k end-2026**, 420k end-2027, 500k end-2028 (one forecast); quarterly wafer throughput +~70% YoY (Omdia) | Second Beijing DRAM fab planned | C — see §4 | [tweaktown](https://tweaktown.com/news/112680/chinas-cxmt-is-on-track-to-nearly-match-microns-dram-production-capacity-by-the-end-of-2026/index.html), [xenospectrum](https://xenospectrum.com/en/cxmt-2026-dram-wafer-capacity-micron-350k-wspm/), [Tom's Hardware](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-and-ymtc-to-expand-memory-output) |

**What the supply numbers say about timing.** The three majors' *greenfield* capacity is **2027–2028-loaded**: M15X (2H26–2027), Micron ID1 (mid-2027), Yongin (tool-in 2027, output 2027–28), Samsung P5 (2028), Micron ID2 (late 2028). Micron's own "low-20%" bit growth for 2027 and 2028 is **below** its mid-20s view of CY2026 and is a *supplier's* number — suppliers under-forecast their own bit growth at every prior peak. **The structural point: the capex now being committed (SK hynix doubling wafers by 2030; Samsung KRW 2,100tn; Micron $38bn of US fabs) is the capex that ends this cycle. It lands 2027–2029. It does not land in the next two quarters.** The Korea Herald's framing — "supply, not demand, will define next memory cycle" ([Korea Herald](https://www.koreaherald.com/article/10805993)) — is the correct one.

**Not obtained:** a single-source, consistent wafer-start figure for Samsung total DRAM; realised bit-growth for CY2026 by maker; SK hynix 2027 capex in won (the Q3 call language was obtained second-hand).

---

## 3. HBM

### 3.1 HBM3E → HBM4 transition timing

- **SK hynix: HBM4 expected to become the mainstream HBM product in 4Q26, with shipment volume and revenue surpassing HBM3E** — Q3 2026 results, 28 Oct 2026 [A/B] ([sammyfans](https://www.sammyfans.com/2026/10/28/sk-hynix-q3-margin-hits-record-80-secures-14-ltas-with-memory-supply-booked-to-2029/amp/), [technews.tw](https://finance.technews.tw/2026/10/28/sk-hynixs-third-quarter-revenue-hit-a-record-high-of-over-100-trillion-won/)).
- **Samsung: cited "strong HBM4 sales" in Q3 2026 results, 29 Oct 2026** [A] ([Samsung Newsroom](https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2026-results)).
- Nvidia Rubin HBM4 shipments reportedly began Feb–Mar 2026 (Samsung first) ([TrendForce News 9 Mar 2026](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%e2%80%afhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)).
- **2027 HBM blended ASP: TrendForce projects +121% as HBM4/HBM4E mix shifts** (6 Oct 2026 item) [A via C] ([siliconanalysts](https://siliconanalysts.com/market/trendforce-2027-hbm-blended-asp-to-jump-121-as-hbm4-hbm4e-mix-shifts-2026-10-06)); TrendForce range elsewhere **+70–140% HBM contract prices in 2027** ([Korea Herald](https://biz.heraldcorp.com/article/10852833), [itiger](https://www-web.itiger.com/news/1142333916)).

**The transition is now, not next year.** HBM4 crosses over HBM3E in the current quarter at SK hynix. That is the single most important mix fact for 2027 revenue.

### 3.2 Share at Nvidia; Samsung qualification

| Claim | Figure | Date | Tier | Source |
|---|---|---|---|---|
| Samsung passed Nvidia HBM4 qualification (10 and 11 Gb/s tiers) | yes | ~Feb 2026 | B | [fintool](https://fintool.com/news/samsung-hbm4-nvidia-breakthrough) |
| Nvidia Vera Rubin HBM4 allocation to SK hynix | **~two-thirds** | Jan 2026 (Yonhap) | B | [TrendForce News 28 Jan 2026](https://www.trendforce.com/news/2026/01/28/news-sk-hynix-reportedly-to-supply-about-two-thirds-of-nvidia-hbm4-samsung-targets-early-delivery/) |
| 2026 HBM4 share | **SK hynix 54% / Samsung 28%** (Counterpoint) | 1H26 | A (research house) | [fintool](https://fintool.com/news/samsung-hbm4-nvidia-vera-rubin) |
| SK hynix share of Nvidia *total* HBM 2026 (incl. HBM3E) | ">half"; Samsung "to lead Rubin-specific HBM4" per one Hankyung report | Mar 2026 | B — conflicts with above | [TrendForce News 9 Mar 2026](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%e2%80%afhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/) |
| HBM4 pricing between the two | "comparable prices" | Mar 2026 | B | same |

**Read:** Samsung **has qualified and is shipping HBM4 to Nvidia** — the 2024–25 "Samsung can't qualify" premise is dead. SK hynix is still the majority supplier (54–67% depending on source and denominator), but **it has gone from near-monopoly on HBM3E at Nvidia to a ~55/30/15 three-way split on HBM4.** That is share loss at the margin, by construction, and it is the mechanism by which HBM pricing power erodes before HBM *volume* does. **Not obtained: any post-June-2026 share update.** I could not surface a dated Q3/Q4 2026 allocation figure; the search returned only Jan–Mar 2026 reporting.

### 3.3 HBM share of DRAM wafer capacity

| Metric | 2025 | 2026 | 2027 | Tier | Source |
|---|---|---|---|---|---|
| HBM share of total DRAM **wafer input**, top-3 suppliers (TrendForce) | ~18% | ~22% | **~30%** | A | [TrendForce press 25 Aug 2026](https://www.trendforce.com/presscenter/news/20260825-13198.html), [TrendForce News](https://www.trendforce.com/news/?p=64643) |
| Same, Samsung EVP Kim Taewoo framing ("wafer capacity") | — | ~20% | ~30% | B (via Reuters) | [TrendForce News](https://www.trendforce.com/news/?p=63636) |
| HBM share of total DRAM **bit supply** (TrendForce) | ~8% | ~9% | **~13%** | A | same |
| HBM + server RDIMM share of DRAM bit supply, 2026 | — | **51%** | — | A | same |
| Wafer area per bit, HBM vs conventional | ~3x | | | A/C (ijiwei via TrendForce) | same |

**This is the arithmetic that holds commodity DRAM prices up.** 30% of wafers in 2027 producing 13% of bits means **~17 points of wafer capacity are "lost" to HBM's area penalty** relative to a conventional-only fab. That loss is larger than the entire greenfield addition of the three majors in 2027. **As long as HBM demand holds, the HBM wafer drain is the supply constraint on commodity DRAM — and it is the reason the majors can exit DDR4 and starve PC/mobile without losing revenue.** The corollary is the bear case: if HBM demand disappoints, those wafers revert to commodity DRAM and the flood is immediate, because they are *already built*. **HBM's wafer drain is the cycle's load-bearing wall.**

### 3.4 Sold out through 2027? On what terms — locked or renegotiable?

**Sold-out claims (supplier statements, [A/B]):**
- SK hynix Q3 2026 (28 Oct 2026): DRAM and HBM volumes "effectively all sold out for the next three years, through 2029"; **14 long-term agreements** covering **more than half of 2027 and 2028 production capacity**; shortage expected to persist through 2030 ([sammyfans](https://www.sammyfans.com/2026/10/28/sk-hynix-q3-margin-hits-record-80-secures-14-ltas-with-memory-supply-booked-to-2029/amp/), [iphonewired](https://iphonewired.com/industry/1200227/), [guru3d](https://www.guru3d.com/story/sk-hynix-posts-record-quarter-and-expects-memory-shortage-through-2030/), [xenospectrum](https://xenospectrum.com/en/sk-hynix-earnings-supply-contracts/)).
- Samsung CFO (29 Oct 2026): memory demand next year "far exceed[s] supply due to robust AI investment" ([Light Reading](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter)).
- Micron (30 Sep 2026): supply tightens further through 2028 ([guru3d](https://www.guru3d.com/story/micron-expects-dram-and-nand-supply-to-tighten-further-through-2028/)).

**Terms — the part that matters:**
- **SK hynix: "2027 HBM supply talks with major customers are complete, with pricing set to reflect value"** — Q3 call, 28 Oct 2026 ([mt.co.kr](https://www.mt.co.kr/en/industry/2026/10/28/2026102809242617566)). No price disclosed. In July 2026 SK hynix had said it was still negotiating 2027 volumes and prices and that **HBM pricing does not simply track conventional DRAM** ([digitaltoday](https://www.digitaltoday.co.kr/en/view/86830/sk-hynix-wraps-up-lta-talks-with-about-10-customers-including-core-clients-negotiating-2027-volumes-and-prices)).
- **Those talks were stuck from 2Q26 until at least mid-August 2026** per a TrendForce HBM bulletin (17 Aug 2026) ([TrendForce RP260817WP3](https://www.trendforce.com/research/download/RP260817WP3)). A multi-month stall over price with the dominant buyer is not what "sold out, price-taker customer" looks like.
- **Samsung sought "more than double" current HBM prices for 2027 from Nvidia and Broadcom; talks in final stage** as of 6 Oct 2026 ([sammyfans](https://www.sammyfans.com/2026/10/06/samsung-hbm4-price-talks-enter-final-stage/amp/)). **Micron reportedly contracted most of its 2027 HBM volume earlier and at higher prices** ([it-daily.net](https://www.it-daily.net/?p=189921)).
- **Price ceilings exist.** TrendForce: "some long-term agreements signed after 2Q26 include **price ceilings**," while still projecting HBM contract prices +70–140% in 2027 ([Korea Herald](https://biz.heraldcorp.com/article/10852833)). **This is the closest thing to an answer on "locked vs renegotiable": the newer LTAs are capped on the upside for the supplier — i.e. locked in the customer's favour at the top, not the supplier's.**
- 2026 HBM4 unit price to Nvidia was reported at ~$560, >50% above HBM3E ([digitimes](https://www.digitimes.com/news/a20251106PD236.html)) — [B], 2026 supply only.
- Nvidia reportedly raised server prices ~15% (Aug 2026), read by TrendForce as creating room for HBM +50% in 2027 ([TrendForce News 25 Aug 2026](https://www.trendforce.com/news/2026/08/25/news-nvidias-reported-15-server-hike-boosts-samsung-sk-hynix-with-hbm-prices-potentially-up-50-in-2027/)).

**My reading on terms.** HBM is **volume-locked** for 2027 (talks complete; LTAs covering >50% of 2027–28). It is **not price-locked in the sense the Owner should want**: (a) HBM prices are set annually, (b) the newer LTAs carry *ceilings*, (c) the 2027 talks stalled for a quarter over price, and (d) Samsung and Micron are now both qualified at Nvidia, so Nvidia has a credible second and third source for the first time. **"Sold out through 2029" is a statement about volume commitments; volume commitments in a three-supplier market with annual pricing are precisely the structure under which price, not volume, absorbs the next downturn.** I could find **no evidence of take-or-pay or price-floor provisions in any of the 14 LTAs**; that is recorded in §12 as not obtained and is the question I would most want 巴爺爺 or Peter to put to management.

---

## 4. The CXMT question

[PENDING]

---

## 5. Demand-side durability

### 5.1 DRAM bit demand mix — AI server vs PC / mobile

| Metric | Figure | Date | Tier | Source |
|---|---|---|---|---|
| Server share of DRAM **bits**, 2026 | **~40%** | Gartner 2Q26 forecast | A | [Gartner](https://www.gartner.com/en/documents/8042733) |
| Server share of DRAM **revenue**, 2026 | **~47%** | same | A | same |
| HBM + server RDIMM share of DRAM bit supply, 2026 | **51%** | TrendForce | A | [TrendForce News](https://www.trendforce.com/news/?p=64643) |
| Impact on smartphone and PC production from wafer reallocation to AI memory | **~12%** reduction | Gartner 2Q26 | A | same Gartner |
| Enterprise SSD bit demand growth 2026 | **>80% YoY** | TrendForce | A | [TrendForce via search](https://www.trendforce.com/news/?p=49679) |
| Hypothetical: unconstrained text-only inference | would approach 30–35% of 2026 global DRAM supply | Creative Strategies model, **not a forecast** | C | [Creative Strategies](https://creativestrategies.com/research/memorys-200b-inflection/) |

**Not obtained:** a PC or mobile percentage of 2026 DRAM bits from a research house. The server figure (40% bits / 47% revenue, Gartner) is the anchor; the residual ~60% of bits is PC, mobile, consumer, auto and industrial combined, and **that residual is the part of the market that is already flat-to-rolling in price.**

### 5.2 If hyperscaler capex plateaus
[PENDING]

---

## 6. The cycle-turn checklist — observable, dated indicators

[PENDING]

---

## 7. Peers and relative positioning — SK hynix vs Samsung vs Micron

[PENDING]

---

## 8. Life-cycle stage & evidence

[PENDING]

---

## 9. Competitive map

[PENDING]

---

## 10. The industry bear case at full strength

[PENDING]

---

## 11. Where SK hynix (SKHY) sits · Sector view · Falsifiers

### 11.1 Where the company sits
[PENDING]

### 11.2 Sector view (overweight / neutral / underweight, confidence /10)
[PENDING]

### 11.3 Explicit falsifiers
[PENDING]

---

## 12. NOT OBTAINED register

[PENDING]
