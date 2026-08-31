# MiniMax Group Inc (0100.HK) — Financial Statement Review

**巴爺爺, Financial Statement Analyst, Dept 2 Equity Research · 2026-07-30**

> Filing note (CEO): this report was returned inline by the analyst and persisted to disk
> by the CEO on 2026-07-30. Content is verbatim from the analyst. See firm lesson L-005.

## Summary & Grade

**Grade: D+ · Financial Score 48/100**

MiniMax is a pre-scale, cash-burning foundation-model company whose *reported* FY2025 net
loss of US$1.872bn is ~85% a non-cash preferred-share remeasurement that permanently
disappeared at the January 2026 IPO. The real economics are: **US$79.0m revenue, 25.4%
gross margin, ~US$321m operating loss, ~US$209m of operating cash burn in 9M2025**, funded
by a genuinely fortress-like ~US$3.7bn liquidity stack. The accounts are not manipulative —
but they are thin, immature, and carry one material unresolved question: a shareholder
(Alibaba, 13.66%) is also the dominant compute supplier, at a scale that in 9M2025
*exceeded total company revenue*.

**Data staleness: 7 months.** Last reported financials are FY2025 (31 Dec 2025), published
2 Mar 2026. No quarterly reporting; 1H2026 interims are due by 30 Sep 2026. Two material
post-balance-sheet events (IPO Jan-2026; HK$16.0bn placement + CB Jul-2026) are not in any
audited statement.

### The three numbers that matter

1. **US$250.9m adjusted net loss (FY2025) vs US$244.2m (FY2024)** — cash-basis loss is
   *flat* while revenue grew 158.9%. This is the single most important fact in the file,
   and it is the opposite of what the US$1.872bn headline implies.
2. **25.4% gross margin (FY2025, +13.2pp YoY)** — still catastrophically low for
   "software," and its durability is unverified because the compute is bought from a
   shareholder.
3. **~US$3.7bn total liquidity vs ~US$27.9m/month disclosed burn** — solvency is not the
   risk here; dilution and burn *escalation* are.

---

## 1. Revenue: lines, geography, trajectory

| US$m | FY2023 | FY2024 | 9M2024 | 9M2025 | FY2025 |
|---|---|---|---|---|---|
| Revenue | 2.460¹ | 30.523 | 19.45 | 53.437 | 79.038 |
| YoY | — | +1,141% | — | +175% | +158.9% |

¹ **Discrepancy flagged.** Two sources render FY2023 revenue as US$2.46m
([Tiger Brokers prospectus summary](https://www.itiger.com/news/1126099864);
[cnfol prospectus breakdown](http://mp.cnfol.com/57306/article/1767250809-142195116.html));
one Chinese source renders it 346萬美元 (US$3.46m). I use **US$2.46m** and mark the FY2023
base as *low confidence*. It does not affect the thesis.

**By line** (prospectus, via
[cnfol](http://mp.cnfol.com/57306/article/1767250809-142195116.html)):

- AI-native products (Talkie/星野, Hailuo AI, MiniMax app — subscriptions + in-app top-ups
  + ads): **71.4% of FY2024**, **71.1% of 9M2025**.
- Open platform / enterprise (API calls, dedicated deployment): 28.6% FY2024, ~28.9% 9M2025.

This is a **consumer-prepaid revenue model**, not enterprise contracts. Positive for
accounting quality: cash-up-front, minimal receivables risk, no channel-stuffing vector.
Negative: high churn sensitivity, app-store take rates embedded in COGS.

**By geography — the >70% overseas claim is VERIFIED:**

- Overseas share: **19.2% (FY2023) → 69.8% (FY2024) → 73.1% (9M2025)**; FY2025 stated as
  ">70%" ([prospectus via cnfol](http://mp.cnfol.com/57306/article/1767250809-142195116.html);
  [FY2025 release](https://www.minimaxi.com/news/minimax%E5%8F%91%E5%B8%83-2025-%E5%B9%B4%E5%85%A8%E5%B9%B4%E4%B8%9A%E7%BB%A9)).
- 9M2025 top markets: **Singapore 24.3%**, **United States 20.4%** of total revenue.
- **Analyst caveat (analytical, not filed):** a 24.3% "Singapore" share for a consumer app
  business almost certainly reflects billing-entity/app-store settlement routing rather than
  end-user location. Treat the country mix as a *booking* geography, not a demand geography.
  Unverified.

**Post-year-end operating datapoint:** ARR crossed **US$150m by February 2026**; M2-series
daily token consumption in Feb-2026 >6× Dec-2025
([FY2025 release commentary](https://www.minimax.io/news/minimax-global-announces-full-year-2025-financial-results),
via search extraction). Sell-side consensus per
[S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/minimax-revenue-seen-rising-to-usd219m-in-2026-reaching-usd6b-by-2030)
is US$219m FY2026. Both are *company/consensus* figures, not audited.

---

## 2. Profitability — margins, ROE, ROIC

| US$m | FY2023 | FY2024 | 9M2025 | FY2025 |
|---|---|---|---|---|
| Revenue | 2.460 | 30.523 | 53.437 | 79.038 |
| Gross profit | (0.61)ᶜ | 3.72ᶜ | n/o | **20.079** |
| **Gross margin** | **-24.7%** | **12.2%** | **23.3%** | **25.4%** |
| Cost of revenue | 3.07ᶜ | 26.80ᶜ | n/o | 58.96ᶜ |
| R&D | n/o | **189.0** | n/o | **252.8** (+33.8%) |
| Selling & distribution | n/o | **87.0** | n/o | **51.9** (-40.3%) |
| Administrative | n/o | **14.4** | n/o | **36.8** (+155.9%) |
| **Operating loss** | n/o | **(286.7)ᶜ** | n/o | **(321.4)ᶜ** |
| **Operating margin** | n/o | **-939%ᶜ** | n/o | **-407%ᶜ** |

ᶜ = **computed by the analyst** from disclosed margin percentages and expense lines; not a
filed line item. n/o = not obtained.
Sources: [FY2025 results release (Chinese)](https://www.minimaxi.com/news/minimax%E5%8F%91%E5%B8%83-2025-%E5%B9%B4%E5%85%A8%E5%B9%B4%E4%B8%9A%E7%BB%A9);
[PR Newswire English release](https://www.prnewswire.com/apac/news-releases/minimax-announces-full-year-2025-financial-results-302700878.html);
expense detail via [prnasia](https://www.prnasia.com/story/523613-1.shtml).

**Gross margin drivers.** Management attributes the +13.2pp to "model and system efficiency
improvements and optimised infrastructure allocation." A supporting hard datapoint:
**inference compute cost per million tokens for the M2 text series fell >50% between
Dec-2025 and Feb-2026**; Hailuo video inference latency -30%
([21jingji](https://www.21jingji.com/article/20260303/herald/6399e1c53a43c2d492ea39579d7e1395.html)).
Direction is credible. **But 25.4% is a hardware-reseller margin, not a software margin** —
every incremental dollar of consumer revenue still costs ~75 cents of GPU time.

**Cost-structure observation that matters:** MiniMax had only **428 full-time employees at
31 Dec 2025** with total employee cost (incl. share-based payment) of **US$84.3m**
([FY2025 release](https://www.prnewswire.com/apac/news-releases/minimax-announces-full-year-2025-financial-results-302700878.html)).
Against R&D of US$252.8m, this means **R&D is overwhelmingly cloud/training compute, not
payroll** — the release itself attributes the R&D increase "primarily to increased cloud
service costs related to model training." Implication: R&D is genuinely period expense, and
the risk of aggressive R&D capitalisation is structurally *low*. That is a point in the
company's favour.

**ROE / ROIC: not meaningful, and the analyst declines to compute them.**

- Pre-IPO the convertible redeemable preferred shares (US$2.321bn at 30 Sep 2025) sat in
  *current liabilities*, producing large negative book equity — any ROE would be a
  mathematical artefact.
- Post-IPO conversion, equity is dominated by fresh capital (IPO + July raise), and NOPAT is
  deeply negative. ROIC is negative on any definition.
- **Filed equity and invested-capital balances at 31 Dec 2025: not obtained.** Do not let
  the committee use a placeholder ROE.

**EPS trajectory: not obtained.** Basic/diluted loss per share for FY2025 was not
recoverable from accessible sources. Note that any reported FY2025 loss-per-share is
corrupted by the US$1.59bn preferred remeasurement and is **not** a forward-comparable
figure. Share-count creep is now the live issue instead — see §5.

---

## 3. Accounting loss vs cash loss — separating the two

| US$m | FY2024 | FY2025 | Δ |
|---|---|---|---|
| **Reported net loss** | (465.2) | **(1,872.0)** | +302.3% |
| add back: FV loss on financial liabilities (preferred shares) | 210 | **~1,590** | |
| add back: listing expenses | — | **6.9** | |
| add back: share-based payment | n/o | **~24.2 (derived)** | |
| **Adjusted net loss (non-IFRS)** | **(244.2)** | **(250.9)** | **+2.7%** |

Sources: net loss and FV loss — [Jiemian](https://www.jiemian.com/article/14058847.html)
and [中新经纬 V观财报](https://www.jwview.com/jingwei/html/m/03-02/661095.shtml); adjusted loss
— [FY2025 release](https://www.minimaxi.com/news/minimax%E5%8F%91%E5%B8%83-2025-%E5%B9%B4%E5%85%A8%E5%B9%B4%E4%B8%9A%E7%BB%A9);
Reuters independently reports US$1.87bn net / US$251m adjusted
([via Yahoo Finance](https://finance.yahoo.com/news/chinas-minimax-reports-strong-revenue-growth-144558497.html)).

**Cross-check (L-001 compliance):** revenue US$79.0m, net loss US$1.872bn and cash
US$1,050.3m were each verified against **two independent sources** — (a) the company's own
results release on minimaxi.com / PR Newswire, and (b) Reuters (via Yahoo Finance) and
中新经纬/界面新闻. **They agree on all three.** There is no profit anywhere in this file; the
company is loss-making on every basis including adjusted.

**Reading of the distortion.** The US$1.59bn is a textbook, non-cash, **non-recurring**
IFRS 9 remeasurement: redeemable preferred shares are carried as financial liabilities at
FVTPL, so a *rising* valuation into the IPO mechanically generates a loss. It converted to
equity at listing and **will not recur in FY2026**. This is not a red flag — it is the
correct accounting. The red flag would be an analyst quoting the US$1.87bn as an operating
result.

**The adjustment definition is conservative and the analyst accepts it.** Only three
addbacks — SBC, preferred FV loss, listing expenses — all standard and all genuinely
non-cash or one-off. There are no "restructuring," "transformation" or "strategic
initiative" addbacks. Compares favourably with typical recent-IPO Chinese non-IFRS
constructions.

**Derived SBC ≈ US$24.2m (30.6% of revenue).** This is the analyst's plug from the
reconciliation (1,872.0 − 1,590 − 6.9 − 250.9), not a disclosed line. The US$1.59bn is a
rounded press figure, so the derivation carries roughly ±US$10m error. **The filed
share-based payment expense line was not obtained.** As a % of revenue this is high (~31%);
in absolute terms (~US$24m) it is immaterial to dilution today. Flag for re-check at the
1H2026 interims.

**Coherence check (analyst's):** computed operating loss US$321.4m − SBC ~24.2 − listing 6.9
= ~US$290m; adjusted net loss is US$250.9m. The ~US$39m gap is consistent with
finance/investment income on a ~US$1bn cash pile. The numbers hang together. No unexplained
residual.

---

## 4. Cash generation, burn and runway

| US$m — net cash used in operating activities | FY2022 | FY2023 | FY2024 | 9M2025 |
|---|---|---|---|---|
| | (11.0) | (64.5) | (258) | (209) |

Source: prospectus, via [Sohu](https://www.sohu.com/a/971727988_122014422) /
[Tencent News](https://news.qq.com/rain/a/20260101A02U1900). **Period labelling is the
analyst's inference** from a four-figure series in a track-record-period disclosure (HK
three-year + stub). FY2025 full-year operating cash flow was **not obtained**.

**Sanity check:** FY2024 operating outflow US$258m vs FY2024 adjusted net loss US$244.2m — a
**1.06× cash-to-adjusted-loss ratio**. That is a *clean* relationship: there is no
divergence between the adjusted earnings story and the cash story. This is the strongest
accounting-quality signal in the file.

**Free cash flow: negative on any definition. Capex (compute/servers) was not obtained** for
any period — a genuine gap given that the July 2026 raise earmarks 80% for "AI
infrastructure, including deploying new-generation AI accelerators and high-bandwidth
networks." Whether MiniMax shifts from *renting* compute (opex, hits R&D/COGS) to *owning*
it (capex, depreciated) is the single biggest swing factor for FY2026-27 reported margins.
**Watch this at the interims — a jump in owned compute would flatter gross margin and R&D
while gutting FCF.** Treat any such margin improvement as non-organic.

**Liquidity stack:**

| Item | Amount | Date | Source |
|---|---|---|---|
| Cash balance | **US$1,050.3m** | 31 Dec 2025 | [FY2025 release](https://www.prnewswire.com/apac/news-releases/minimax-announces-full-year-2025-financial-results-302700878.html) |
| (prior year) | US$880.6m | 31 Dec 2024 | same |
| IPO gross proceeds | **HK$4.8bn (~US$614m)** base deal | 9 Jan 2026 | [Reuters via Yahoo](https://finance.yahoo.com/news/chinas-minimax-reports-strong-revenue-growth-144558497.html) |
| — full-greenshoe scenario | HK$5.54bn (33.58m sh @ HK$165) | Jan 2026 | [uSMART/HKET coverage](https://inews.hket.com/article/4060986/minimax-100-ipo-2026) |
| Placement + CB, **net** | **HK$15,957m (~US$2,040m)** | Jul 2026 | [Caixin Global](https://www.caixinglobal.com/2026-07-10/chinese-ai-developer-minimax-raises-hk16-billion-from-equity-convertible-bond-sale-102462841.html) |
| **Approx. total available** | **~US$3.7bn** | est. Jul 2026 | computed |

⚠ **The HK$5.54bn figure in circulation is the full-greenshoe gross scenario.** Reuters
reports the actual raise as **HK$4.8bn / US$614m**. IPO *net* proceeds at the HK$165 strike
were **not obtained** (the prospectus only gave HK$3.818bn net at a HK$158 midpoint with no
over-allotment). Use ~US$0.6bn, not HK$5.54bn, for cash-build purposes.

**Definitional warning on "cash balance."** In the prospectus, MiniMax's stated 30 Sep 2025
"cash balance" of US$1,046m was built as: cash & equivalents **US$363m** + current-portion
FVTPL financial assets **US$644m** + **undrawn bank facilities US$39.4m**
([Sohu](https://www.sohu.com/a/971727988_122014422)). **Including undrawn credit lines
inside a "cash balance" headline is a presentational flag.** The FY2025 US$1,050.3m figure is
almost certainly constructed the same way, meaning *true* cash and equivalents at 31 Dec
2025 may be materially below US$1.0bn. **Unverified — resolve at the interims.**

**Runway.** Disclosed expected monthly cash consumption as at 31 Dec 2025: **US$27.9m/month**
(~US$84m/quarter).

| Scenario | Quarterly burn | Runway from ~US$3.7bn |
|---|---|---|
| Disclosed Dec-25 run-rate | US$84m | ~44 quarters |
| 3× step-up (infra build) | US$250m | ~15 quarters |
| 5× step-up | US$420m | ~9 quarters |

**Read: solvency is not a near-term risk.** But a company with a >40-quarter runway does not
raise US$2bn at a 9.89% discount the day after lock-up expiry. **The raise itself is the
disclosure** — management is telegraphing a multi-fold burn escalation. Model the 3-5×
scenarios, not the disclosed run-rate. Even so, runway is comfortably >2 years.

**Inference (analyst's, not filed):** cash rose US$169.7m during 2025 while burning ~US$280m+
— implying roughly **US$450m of private financing raised during FY2025** ahead of the IPO.
Not separately disclosed in accessible sources.

---

## 5. Balance sheet, debt and structure

**At 30 Sep 2025 (prospectus, pre-IPO):**

- Convertible redeemable preferred shares: **US$2,321m, classified as current liabilities**
  → converted to equity at the Jan-2026 IPO.
- Total current liabilities **US$2,434m**; **net current liabilities US$1,382m**. Both
  figures are now historical artefacts of the preferred-share classification.
- Cash & equivalents US$363m; current FVTPL financial assets US$644m; undrawn bank facilities
  US$39.4m.
- **Bank borrowings outstanding: not obtained** (only the undrawn US$39.4m facility was
  disclosed). Pre-IPO leverage appears immaterial.
- Source: [Sohu](https://www.sohu.com/a/971727988_122014422),
  [Tencent News](https://news.qq.com/rain/a/20260101A02U1900).

**Post-listing debt — the only real debt in the structure:**

- **HK$6,500m (~US$831m) zero-coupon convertible bonds, maturing 2027**, initial conversion
  price **HK$335/share** (12.64% premium to the 9 Jul 2026 close of HK$297.4), convertible
  into ~19.403m Class A shares. Issuance **completed 16 July 2026**.
  ([Caixin](https://www.caixinglobal.com/2026-07-10/chinese-ai-developer-minimax-raises-hk16-billion-from-equity-convertible-bond-sale-102462841.html);
  [e-Digest](https://www.edigest.hk/%e6%9c%80%e6%96%b0%e8%b2%a1%e7%b6%93%e6%b6%88%e6%81%af/%e7%a8%80%e5%ae%87%e7%a7%91%e6%8a%80minimax%e9%85%8d%e8%82%a1%e7%99%bc%e5%82%b5%e5%85%b1%e7%b1%8c160%e5%84%84-%e8%a7%a3%e7%a6%81%e7%bf%8c%e6%97%a5%e8%82%a1%e5%83%b9%e6%80%a5%e6%8c%ab-2021007/))
- One secondary source describes the bonds as **"secured"**
  ([KuCoin](https://www.kucoin.com/news/flash/minimax-to-raise-over-hkd-16-billion-via-share-placement-and-bond-issuance))
  — **unverified against the announcement**. If true it is unusual for a cash-rich issuer and
  would matter for structural subordination. **Flag for verification.**
- Concurrent equity placement: **35.6m new Class A shares at HK$268** (9.89% discount),
  ~HK$9,541m.

**Debt profile assessment:**

- **Maturity wall: 100% of debt matures in 2027.** A single ~US$831m bullet.
- **Rate: 0%.** No cash interest cost; interest coverage is undefined (EBIT negative) but
  also irrelevant while the coupon is zero.
- **The real exposure is equity-price-dependent:** if 0100.HK trades below HK$335 into 2027,
  the bonds are redeemed in **cash** — an ~US$831m call on liquidity. Against ~US$3.7bn of
  liquidity that is survivable, but it converts a "no-debt" story into a real 2027 obligation
  if the stock de-rates.

**Dilution / share-count creep:** post-raise and assuming full CB conversion, the controlling
shareholder's stake falls **25.22% → 21.46%**; placees ~9.66%; CB holders ~5.26%
([e-Digest](https://www.edigest.hk/%e6%9c%80%e6%96%b0%e8%b2%a1%e7%b6%93%e6%b6%88%e6%81%af/%e7%a8%80%e5%ae%87%e7%a7%91%e6%8a%80minimax%e9%85%8d%e8%82%a1%e7%99%bc%e5%82%b5%e5%85%b1%e7%b1%8c160%e5%84%84-%e8%a7%a3%e7%a6%81%e7%bf%8c%e6%97%a5%e8%82%a1%e5%83%b9%e6%80%a5%e6%8c%ab-2021007/)).
**~15% dilution within six months of listing.** Share-count creep is therefore a live,
quantified issue — not from SBC, but from capital markets activity.

**Structure:** Cayman Islands holding company with **weighted voting rights (WVR)**,
operating through PRC entity 上海稀宇极智科技有限公司, with CSRC overseas-listing filing
completed ([CSRC notice](https://www.csrc.gov.cn/csrc/c105984/c7603849/content.shtml)).
Search extraction of the prospectus indicates a **VIE / contractual-arrangement structure**;
however that extraction reads partly as generic boilerplate and the prospectus could not be
opened. **The VIE structure is marked REPORTED BUT UNVERIFIED against the primary
document.** Consequence if true: shareholders hold contractual rights, not equity, in the
PRC operating entity; WVR further limits minority influence. Dept 4 (The dictator) should
confirm.

---

## 6. Accounting quality — red flags

**FLAG 1 (MATERIAL) — Related-party compute: Alibaba is both shareholder and dominant
supplier.**

| Purchases from Alibaba Cloud (US$) | FY2022 | FY2023 | FY2024 | 9M2025 | Cap 2026 | Cap 2027 | Cap 2028 |
|---|---|---|---|---|---|---|---|
| | ~0.04m | 3.1m | 10.0m | **58.4m** | 115m | 125m | 135m |

Source: prospectus via
[Sina Finance](https://finance.sina.com.cn/roll/2025-12-22/doc-inhcruir8012619.shtml) /
[21jingji](https://www.21jingji.com/article/20251222/herald/1333ef3ac52f1ced683514afd670018f.html).

Alibaba holds **13.66% indirect economic interest / 3.64% voting** as at 15 Dec 2025 and was
also an **IPO cornerstone investor**. In 9M2025 MiniMax bought **US$58.4m of cloud from
Alibaba against US$53.4m of total revenue** — the related-party supplier bill exceeded the
entire top line. For reference, FY2025 cost of revenue computes to **US$59.0m**.

**Why this is the #1 issue:** the 13.2pp gross-margin expansion is the centrepiece of the
equity story, and it cannot be verified how much is engineering efficiency versus favourable
pricing from a shareholder-supplier. The disclosed split of Alibaba spend between cost of
revenue and R&D was **not obtained**. A shareholder with an incentive to see a successful
listing subsidising the COGS line would produce exactly the observed pattern.
**Unresolved. Highest-priority follow-up.**

**FLAG 2 (MINOR, DISMISSED) — Related-party revenue.** MiniMax also *sells* API to Alibaba:
~US$0 (2022), **US$41.4k (2023)**, **US$33.3k (2024)**, **US$233k (9M2025)**; caps
US$0.65m/1.0m/1.5m for 2026-28
([Sina](https://finance.sina.com.cn/roll/2025-12-22/doc-inhcruir8012619.shtml)). At **~0.4%
of 9M2025 revenue this is immaterial**. There is **no evidence of revenue round-tripping**.
The relationship is one-directional in economic substance: MiniMax is Alibaba's customer,
not the reverse. Flag cleared.

**FLAG 3 (PRESENTATIONAL) — "Cash balance" includes undrawn facilities.** See §4. Undrawn
credit lines are not cash. Adjust down when modelling.

**FLAG 4 (STRUCTURAL) — Reduced disclosure cadence.** HKEX requires only semi-annual
reporting. Between 2 Mar 2026 and ~Sep 2026 the market has had **no audited financial data**
— only management-supplied operating metrics (ARR, token growth) that are not subject to
audit and not defined in the filings. **We are currently 7 months stale and relying on
unaudited management colour.**

**CLEARED — Earnings vs cash flow divergence.** FY2024 operating outflow US$258m vs adjusted
net loss US$244.2m (1.06×). No divergence. Good.

**CLEARED — Receivables/inventory.** Consumer prepaid model; no inventory. Receivables
balance not obtained, but the revenue model structurally limits the risk. **Contract
liabilities / deferred revenue: not obtained** — worth checking, as deferred revenue growth
would be a *positive* leading indicator.

**CLEARED (provisionally) — Capitalised R&D.** No evidence of development-cost
capitalisation obtained. 428 employees against US$252.8m R&D means R&D is compute, which is
naturally expensed. Low structural risk. **Balance of internally-generated intangibles: not
obtained.**

**NOT A FLAG — the US$1.59bn FV loss.** Correct IFRS treatment, non-cash, non-recurring,
already reversed.

**NOT OBTAINED (gaps that could not be closed):** filed SBC line; FY2025 operating cash flow;
capex any period; customer concentration / top-5 customer share; contract liabilities;
receivables; intangibles; total equity; EPS; IPO net proceeds at strike; auditor and audit
opinion; whether the July CB is secured.

---

## 7. Financial Score — 48/100 (Grade D+)

| Component | Weight | Score | Rationale |
|---|---|---|---|
| Revenue growth & quality | 20% | **72** | +158.9% FY2025, +175% 9M2025; ARR US$150m by Feb-26; consumer-prepaid cash revenue; overseas 73.1% verified; no meaningful related-party revenue. Docked for a tiny absolute base (US$79m), unverified customer concentration, and booking-geography opacity. |
| Margins & profitability | 20% | **25** | GM 25.4% is a hardware margin, not software. Operating margin -407% (computed). ROE/ROIC negative and not meaningfully computable. Credit given only for genuine trajectory (GM -24.7% → 12.2% → 25.4%; op margin -939% → -407%). |
| Cash generation | 20% | **20** | FCF deeply negative; ~US$209m operating outflow in 9M2025; capex entirely undisclosed. Sole credit: adjusted loss flat YoY (US$244.2m → US$250.9m) on 159% revenue growth, and 1.06× cash-to-adjusted-loss coherence. |
| Balance sheet & debt | 20% | **78** | ~US$3.7bn liquidity; only debt is a zero-coupon CB; no cash interest burden. Docked for a single ~US$831m 2027 bullet maturity that turns into a cash call if the stock breaks HK$335, ~15% dilution in six months, and pre-IPO net current liabilities of US$1.38bn. |
| Accounting quality & disclosure | 20% | **55** | Conservative three-item non-IFRS definition; clean cash/earnings relationship; no round-tripping; low R&D-capitalisation risk. Heavily docked for the Alibaba shareholder-supplier scale, the "cash balance" presentation, VIE/WVR structure unverified, semi-annual reporting, and a long list of unobtained line items. |
| **Weighted total** | **100%** | **48** | **Grade D+** |

**Grade interpretation.** D+ reflects the *current state of the accounts*, not the equity's
prospects. This is a company with two years of meaningful revenue history, no profit on any
basis, no positive cash flow, no computable returns on capital, and a fortress balance sheet
built entirely from external capital. The trajectory is genuinely improving and the
accounting is honest — which is why it is D+ and not F.

**What would move the grade:**

- **To C/C+:** FY2026 gross margin >35% with disclosed COGS/R&D split of Alibaba spend;
  adjusted net loss falling in absolute terms; contract liabilities growing faster than
  revenue.
- **To F / thesis-break:** gross margin expansion revealed to depend on below-market
  related-party compute pricing; a shift to owned compute that flatters gross margin while
  FCF deteriorates; adjusted net loss re-accelerating past US$400m; or any re-definition of
  the non-IFRS addback list.

**Committee guidance from Dept 2 (Financials):** at 48/100 this is a **speculative-quality
balance sheet with a venture-stage income statement**. Position sizing should be governed by
Dept 6's rules for pre-profit names, not by conventional valuation multiples — there is no E
in the P/E and no positive FCF to yield on. Recommend **no committee decision on financials
alone until the 1H2026 interims (due by 30 Sep 2026)**, which will be the first data point
that (a) is post-preferred-share distortion, (b) reveals capex intent, and (c) shows whether
the July 2026 raise has already multiplied the burn.

---

## Coverage & confidence limitations

- **WebFetch was blocked by egress policy (HTTP 403) on all attempted hosts**, including
  hkexnews.hk, prnewswire.com, minimax.io, finance.yahoo.com, morningstar.com,
  streetinsider.com, beancount.io and hdinresearch.com. **The prospectus and the FY2025
  announcement PDFs could not be read directly.** All figures are search-engine extractions
  of those primary documents plus secondary press. Confidence in headline figures (revenue,
  gross margin, losses, cash, opex lines) is **high** — each cross-checked against ≥2
  independent sources. Confidence in structural items (VIE, security on the CB, cash-balance
  composition) is **low to moderate**.
- **No full financial statements, notes, or cash flow statement were obtained.** Ratios
  marked ᶜ are computations, not filed figures.
- **Sell-side coverage is thin** (listed <7 months; one Guosen note and one S&P Global
  consensus piece located). Consensus estimates should carry a wide error band.
- tradingkey.com was not used, per firm blacklist.

**Sources:**
[MiniMax FY2025 results (Chinese)](https://www.minimaxi.com/news/minimax%E5%8F%91%E5%B8%83-2025-%E5%B9%B4%E5%85%A8%E5%B9%B4%E4%B8%9A%E7%BB%A9) ·
[PR Newswire English release](https://www.prnewswire.com/apac/news-releases/minimax-announces-full-year-2025-financial-results-302700878.html) ·
[prnasia expense detail](https://www.prnasia.com/story/523613-1.shtml) ·
[Reuters via Yahoo Finance](https://finance.yahoo.com/news/chinas-minimax-reports-strong-revenue-growth-144558497.html) ·
[SCMP](https://www.scmp.com/tech/article/3345116/chinese-ai-firm-minimaxs-revenue-jumps-159-us79-million-strong-demand) ·
[Jiemian](https://www.jiemian.com/article/14058847.html) ·
[中新经纬](https://www.jwview.com/jingwei/html/m/03-02/661095.shtml) ·
[21jingji (annual report)](https://www.21jingji.com/article/20260303/herald/6399e1c53a43c2d492ea39579d7e1395.html) ·
[Sina — Alibaba related-party detail](https://finance.sina.com.cn/roll/2025-12-22/doc-inhcruir8012619.shtml) ·
[21jingji — Alibaba stake](https://www.21jingji.com/article/20251222/herald/1333ef3ac52f1ced683514afd670018f.html) ·
[cnfol — prospectus segment/geography breakdown](http://mp.cnfol.com/57306/article/1767250809-142195116.html) ·
[Tiger Brokers — prospectus summary](https://www.itiger.com/news/1126099864) ·
[Sohu — balance sheet & cash burn](https://www.sohu.com/a/971727988_122014422) ·
[Tencent News — same](https://news.qq.com/rain/a/20260101A02U1900) ·
[Caixin Global — July 2026 raise](https://www.caixinglobal.com/2026-07-10/chinese-ai-developer-minimax-raises-hk16-billion-from-equity-convertible-bond-sale-102462841.html) ·
[e-Digest — placement/CB terms](https://www.edigest.hk/%e6%9c%80%e6%96%b0%e8%b2%a1%e7%b6%93%e6%b6%88%e6%81%af/%e7%a8%80%e5%ae%87%e7%a7%91%e6%8a%80minimax%e9%85%8d%e8%82%a1%e7%99%bc%e5%82%b5%e5%85%b1%e7%b1%8c160%e5%84%84-%e8%a7%a3%e7%a6%81%e7%bf%8c%e6%97%a5%e8%82%a1%e5%83%b9%e6%80%a5%e6%8c%ab-2021007/) ·
[KuCoin — CB completion](https://www.kucoin.com/news/flash/minimax-to-raise-over-hkd-16-billion-via-share-placement-and-bond-issuance) ·
[HKET — IPO cornerstones](https://inews.hket.com/article/4060986/minimax-100-ipo-2026) ·
[Eastmoney — IPO proceeds](https://finance.eastmoney.com/a/202512313606369690.html) ·
[CSRC filing notice](https://www.csrc.gov.cn/csrc/c105984/c7603849/content.shtml) ·
[S&P Global — consensus](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/minimax-revenue-seen-rising-to-usd219m-in-2026-reaching-usd6b-by-2030)

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

**Coverage gap — no quantitative input.** Department 3 (Quant Research:
賭馬狗, Math King, Tom, AI指標) filed **nothing** on this name. Session
limits forced the pipeline down to a three-agent core and quant was cut
first, without being logged as a gap at the time. Any conclusion here
rests on fundamentals, valuation, news and technicals only.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
