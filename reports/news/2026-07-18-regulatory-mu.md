# Regulatory Brief — MU (Micron Technology)

**Analyst:** The dictator (Dept. 4 — Regulatory) · **Date:** 2026-07-18 · **Status of name:** Not held; not on watchlist; under `/analyze` review. Adjacent exposure in watchlist: NVDA, AMD, TSM, AVGO, SMH (memory demand/supply chain).

All probabilities below are analyst estimates, not sourced figures. This is investment-impact research, not legal advice.

---

## 1. Section 232 semiconductor tariffs — Phase 1 in force, Phase 2 decision imminent

**Development & source.** Proclamation 11002 (signed 2026-01-14, effective 2026-01-15) imposes a 25% tariff on a *narrow* set of advanced semiconductors defined by TPP and "total DRAM bandwidth" thresholds (per the Annex: logic ICs with total DRAM bandwidth 4,500–5,000 GB/s or 5,800–6,200 GB/s — i.e., H200/MI325X-class AI accelerators and derivatives). Raw DRAM, NAND, and standalone HBM are **not** covered in Phase 1. Exemptions exist for US data-center use, US R&D, repairs, startups, and non-data-center consumer/auto applications. The proclamation directs Commerce to report to the President **by 2026-07-01** on the data-center semiconductor market to inform modification — Phase 2 could extend coverage to DRAM/NAND, semiconductor manufacturing equipment, and derivative products. As of today (2026-07-18) I find **no Phase 2 proclamation or Federal Register scope notice published**; the July 1 report milestone has passed and a decision is live. (White House proclamation; White & Case 2026-01; EY 2026-02; TariffLens Phase 2 guide; Pillsbury.)

**Exposed mechanism for MU.** Two-sided:
- *Cost risk:* Micron fabs most DRAM/HBM in Japan, Taiwan, and Singapore today; a Phase 2 tariff on memory imports would hit COGS on US-bound product until Idaho/NY fabs ramp (first US output late-2020s). Mitigants: exemption architecture in Phase 1 favors companies investing in US manufacturing, and Micron's $200B US plan is the largest memory commitment on record; Japan has a separate tariff understanding.
- *Protection upside:* a memory tariff would burden Samsung/SK hynix imports symmetrically while Micron is the only US-headquartered memory maker building domestic capacity — plausibly net protective, depending on exemption design.

**Timeline & probability.** Phase 2 scope notice plausibly Jul–Aug 2026, effective Sep–Oct 2026 (per practitioner timelines). Probability some Phase 2 expansion occurs: **~60–70% (estimate)**; probability commodity DRAM/NAND is included without a US-manufacturing exemption pathway usable by MU: **~20–25% (estimate)**.

**Tripwires.** (a) Federal Register notice modifying Proclamation 11002 or new proclamation — check weekly; (b) any Commerce statement on the July 1 data-center report; (c) HTSUS annex changes touching 8542 memory lines; (d) exemption criteria referencing domestic-capacity commitments.

---

## 2. US export controls — HBM to China restricted; AI-chip easing is an HBM demand tailwind

**Development & source.** (i) The Dec 2024 BIS rule restricts HBM exports to China (bandwidth density ≥3.3 GB/s/mm²) worldwide via FDPR; impact on Micron was modest since its HBM ships overwhelmingly to non-China customers (NextPlatform 2024-12-02; CSIS). (ii) Effective 2026-01-15, BIS revised its license review policy from presumption-of-denial to **case-by-case** for advanced computing chips below TPP 21,000 and total DRAM bandwidth 6,500 GB/s (NVIDIA H200, AMD MI325X) exported to China, with security conditions, reported per-firm caps (~75K units) and a 25% surcharge on such sales (Federal Register 2026-01-15; Morgan Lewis 2026-01; CNAS; Introl).

**Exposed mechanism.** Direct China HBM revenue for MU is ~nil, so the HBM ban costs little; the H200 easing is an incremental **demand tailwind** — every accelerator licensed into China carries HBM stacks, and Micron's HBM is reported fully committed through 2026. Watchlist read-through: positive for NVDA/AMD China revenue.

**Timeline & probability.** Both measures are **final and in effect**. Risk of re-tightening (Congressional pushback on H200 policy) — **~25–30% within 12 months (estimate)**; risk of *further* HBM-specific tightening hurting MU: low, MU has minimal China HBM exposure either way.

**Tripwires.** BIS press releases on HBM ECCNs (3A090 family); any change to the case-by-case policy or unit caps; Entity List additions naming Micron customers.

---

## 3. VEU revocation for competitors' China fabs — supply-side tailwind for MU

**Development & source.** BIS revoked Validated End-User authorizations for Samsung China Semiconductor, SK hynix Semiconductor (China), and Intel Dalian (Federal Register 2025-09-02, effective 2025-12-31). BIS grants annual licenses for these fabs to **operate existing capacity** but states it will **not license capacity expansion or technology upgrades** in China; 2026 annual licenses were issued (BIS press release; ArentFox Schiff; Tom's Hardware).

**Exposed mechanism.** SK hynix and Samsung produce a large share of legacy/mid-node DRAM and NAND in China; freezing their China node migration and capacity structurally tightens global memory supply and slows competitor cost curves — a medium-term **tailwind** to memory pricing and MU margins. Offset: accelerates CXMT/YMTC import substitution inside China.

**Timeline & probability.** Final rule, in effect. Probability the freeze holds through 2027: **~75% (estimate)** — it is a plausible bargaining chip in US–Korea or US–China negotiations.

**Tripwires.** Annual license renewal terms (next cycle late 2026); any BIS carve-out permitting node upgrades; Korean government lobbying outcomes.

---

## 4. China posture — CAC ban consummated in market exit; residual retaliation risk

**Development & source.** CAC failed Micron's cybersecurity review 2023-05-21, barring critical-infrastructure operators from buying its products. Per Reuters (2025-10-17, via multiple outlets), Micron is **exiting China's server/data-center memory market** — the business never recovered; it retains mobile and automotive customers in China and serves Lenovo's largely offshore data-center operations. Mainland China was ~$3.4B / ~12% of revenue in the last fiscal year cited. Separately, MOFCOM opened an anti-dumping probe into US **analog** ICs (initiated 2025-09-13, due 2026-09-13, extendable) — memory is **not** in scope — plus an "anti-discrimination" probe of US semiconductor measures.

**Exposed mechanism.** The China data-center downside is now largely **realized and disclosed** (revenue restriction, not a new shock). Residual risks: (a) extension of retaliation to mobile/auto memory sales in China (customs friction, "reliable supplier" procurement guidance); (b) structural share loss to CXMT in commodity DRAM as Beijing subsidizes domestic memory; (c) rare-earth/gallium input controls in any renewed escalation.

**Timeline & probability.** Ban is permanent-until-lifted; probability of CAC reversal in 12 months: **<10% (estimate)**. Probability China formally targets memory/Micron with a new trade action in 12 months: **~15–20% (estimate)**, rising if US Phase 2 tariffs or new export controls land.

**Tripwires.** MOFCOM/CAC announcements naming memory or Micron; analog AD final determination (2026-09-13) as an escalation barometer; CXMT HBM qualification by Chinese AI players; Chinese procurement directives on domestic DRAM content.

---

## 5. CHIPS Act — awards binding, no equity demanded, disbursements milestone-based

**Development & source.** Commerce finalized binding awards of **$6.165B** (Clay, NY and Boise, ID) in Dec 2024 plus up to **$275M** for Manassas, VA — total up to ~$6.4B (Commerce/NIST; SDxCentral; MeriTalk). In June 2025 Micron expanded its US investment commitment to ~**$200B** (Manufacturing Dive 2025-06). In Aug 2025 the White House said it would **not seek equity stakes** in Micron or TSMC (unlike Intel's 10% conversion), because both expanded investments beyond original commitments (Tom's Hardware / WSJ-sourced 2025-08-22; CNBC 2025-08-20).

**Exposed mechanism.** Grants defray US fab capex (compliance conditions, milestone-based disbursement; clawback/upside-sharing provisions standard). No dilution/equity overhang — a differentiator vs Intel. Complementary foreign support: Japan METI up to **¥500B** for the Hiroshima HBM fab (construction started July 2026, shipments ~2028; Taipei Times 2026-07-06; Digitimes) and a **$318M** Taiwan HBM R&D subsidy (Tom's Hardware).

**Timeline & probability.** Agreements signed and in effect; disbursements tied to construction milestones. Probability of material adverse renegotiation (equity demand revived): **~10–15% (estimate)** — administration has publicly exempted MU but policy has reversed before.

**Tripwires.** Commerce statements on CHIPS "restructuring"/equity for remaining recipients; disbursement disclosures in MU 10-Qs; NY/ID construction milestone slippage.

---

## 6. EU / antitrust / trade-remedy housekeeping

No EU regulatory action specific to Micron identified this cycle; EU exposure is demand-side, not compliance-side (low materiality). No pending antitrust or merger reviews involving MU found. No active US or EU trade-remedy case *in memory products* found; China's active AD probe covers analog ICs only. I will keep DRAM under standing watch given the industry's price-fixing litigation history — currently **no open matter identified**.

---

## Net regulatory read for a LONG thesis: **mild net tailwind**, with one live binary

US policy is aligned behind Micron (CHIPS cash without equity, competitor China-fab freeze, H200 easing feeding HBM demand); the China downside is largely realized and out of the numbers going forward. The open binary is the Section 232 **Phase 2** scope decision (memory inclusion and exemption design), due imminently — monitor weekly until resolved.

## Sources

- [White House — Proclamation: Adjusting Imports of Semiconductors (Jan 2026)](https://www.whitehouse.gov/presidential-actions/2026/01/adjusting-imports-of-semiconductors-semiconductor-manufacturing-equipment-and-their-derivative-products-into-the-united-states/)
- [White & Case — 25% Section 232 tariff on certain advanced semiconductors](https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced)
- [EY — US Section 232 proclamation imposes 25% tariff](https://globaltaxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors)
- [TariffLens — July 1 semiconductor tariff review / Phase 2 guide](https://www.tarifflens.ai/blog/section-232-semiconductor-tariff-july-2026-phase-2-guide)
- [Pillsbury — Trump admin targets advanced AI semiconductors, defers broader tariffs](https://www.pillsburylaw.com/en/news-and-insights/trump-advanced-ai-semiconductors-actions.html)
- [Federal Register — Revision to License Review Policy for Advanced Computing Commodities (2026-01-15)](https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities)
- [Morgan Lewis — BIS revises export review policy for advanced AI chips to China](https://www.morganlewis.com/pubs/2026/01/bis-revises-export-review-policy-for-advanced-ai-chips-destined-for-china-and-macau)
- [CNAS — Unpacking the H200 export policy](https://www.cnas.org/publications/commentary/cnas-insights-unpacking-the-h200-export-policy)
- [NextPlatform — US curbs HBM exports to China (Dec 2024)](https://www.nextplatform.com/2024/12/02/us-curbs-hbm-exports-to-china-more-for-the-rest-of-us/)
- [BIS — Commerce strengthens export controls (HBM/SME rule)](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- [Federal Register — Revocation of VEU authorizations in the PRC (2025-09-02)](https://www.federalregister.gov/documents/2025/09/02/2025-16735/revocation-of-validated-end-user-authorizations-in-the-peoples-republic-of-china)
- [BIS — Commerce closes export controls loophole for foreign-owned fabs in China](https://www.bis.gov/press-release/department-commerce-closes-export-controls-loophole-foreign-owned-semiconductor-fabs-china)
- [Tom's Hardware — US grants Samsung and SK hynix 2026 licenses for China tool shipments](https://www.tomshardware.com/tech-industry/us-grants-samsung-and-sk-hynix-2026-licenses-for-chipmaking-tool-shipments-to-china)
- [Seeking Alpha — Micron to exit server chips business in China (report)](https://seekingalpha.com/news/4505086-micron-to-exit-server-chips-business-in-china-report)
- [SCMP — Micron to cease supply of server memory chips to China data centres](https://www.scmp.com/tech/tech-war/article/3329379/micron-cease-supply-server-memory-chips-data-centres-china-after-ban-sources)
- [TrendForce — Micron reportedly exits China server chips](https://www.trendforce.com/news/2025/10/17/news-micron-reportedly-exits-china-server-chips-samsung-sk-hynix-and-local-makers-stand-to-gain/)
- [Xinhua — China launches anti-dumping probe into certain US analog IC chips](https://english.news.cn/20250914/0d9b6f3974ac42f0bddb5f7051f4abf2/c.html)
- [NIST — Micron (New York) CHIPS award page](https://www.nist.gov/chips/micron-new-york-clay)
- [SDxCentral — Micron to receive $6.2bn in direct CHIPS Act funding](https://www.sdxcentral.com/news/micron-to-receive-62bn-in-direct-chips-act-funding/)
- [MeriTalk — Commerce awarding Micron $275M of CHIPS funding](https://www.meritalk.com/articles/commerce-awarding-micron-tech-275m-of-chips-funding/)
- [Manufacturing Dive — Micron expands US manufacturing commitment to $200B](https://www.manufacturingdive.com/news/micron-technology-semiconductor-investment-idaho-new-york-virginia-chips-funding/750555/)
- [Tom's Hardware — White House won't ask for ownership stake in TSMC or Micron](https://www.tomshardware.com/tech-industry/semiconductors/white-house-wont-ask-for-ownership-stake-in-tsmc-or-micron-in-exchange-for-chips-act-funds-companies-already-investing-more-in-the-us-expected-to-be-exempt)
- [CNBC — Trump eyes US government stakes in other CHIPS recipients](https://www.cnbc.com/2025/08/20/trump-eyes-us-government-stakes-in-other-chip-makers-that-received-chips-act-funds-reuters.html)
- [Taipei Times — Micron starts Japan chip expansion (2026-07-06)](https://www.taipeitimes.com/News/biz/archives/2026/07/06/2003860277)
- [Tom's Hardware — Micron secures $318M Taiwanese subsidy for HBM R&D](https://www.tomshardware.com/tech-industry/micron-secures-318-million-taiwanese-subsidy-for-hbm-rd-as-ai-memory-arms-race-intensifies)
