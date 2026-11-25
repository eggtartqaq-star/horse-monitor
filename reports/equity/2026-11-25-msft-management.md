# MSFT — Microsoft Corporation — Management Quality Review

- **Analyst:** Peter (Management Quality, Dept 2 Equity Research)
- **Date:** 2026-11-25 (as-of date for every judgement below)
- **Context:** Owner holds no position. Watchlist `ai:` sleeve. Closes the gap left by the 2026-08-21 package, which had no management report.
- **Firm inputs used:** `reports/equity/2026-08-21-msft-financials.md` (巴爺爺), `reports/equity/2026-08-21-msft-moat.md` (菲比斯), `reports/news/2026-08-21-msft-news.md` (修大哥). Figures taken from them are tagged **[F]**.

## 0. Sourcing caveat (read first)

- **Primary pages opened [P]:** three `microsoft.com` pages on 2026-11-25:
  - the FY27 Q1 earnings release (2026-10-28);
  - the FY26 Q4 earnings release (2026-07-29);
  - the official 2025 annual-meeting voting results.
- **Unreachable:** one further `microsoft.com` page returned 404. **`www.sec.gov` and `www.boardroomalpha.com` failed DNS (ENOTFOUND).** Per session guidance I stopped trying new hosts after that. **No Form 4, 10-K or DEF 14A was opened directly.**
- **Everything else** is a **search extraction [S]** or an **[F]** figure from the August package. **[C]** = my arithmetic on cited inputs. **[E]** = estimate or inference.
- `tradingkey.com` (firm blacklist) appeared in search results for the Q1 FY27 transcript. **Not used.**

## Management grade: **B** · Score **7.4 / 10** (74/100) *(analyst judgement)*

**Verdict in one line:** a first-rate CEO/CFO pair. They guide conservatively on revenue, are candid about their own misses, and pay themselves in a performance-weighted way. But the AI capex programme they are running has not yet earned its cost of capital on the evidence available, and in 2025–26 their capex guidance and capex definitions moved more than their revenue guidance did.

| Pillar | Weight | Score | Basis |
|---|---|---|---|
| Leadership and track record | 20 | **18** | Nadella's 12-year record: Azure passed $100B in FY2026 [F]; operating margin 46.8% [F]. Docked for the 2026 senior exodus (Gaming, Experiences + Devices, AI Platform) |
| Promise vs delivery | 25 | **18** | Azure guidance beaten three quarters running; FY26 margin guide beaten. But: capacity "catch-up" missed twice; FY26 capex-growth guidance reversed within one quarter; CY2026 capex re-based twice; carbon-negative-2030 pledge off track |
| Capital allocation | 25 | **17** | OpenAI stake financially exceptional; LinkedIn and GitHub sound. Activision is value-destructive so far. FCF has fallen two years and −27% in Q1 FY27. ROIC roughly halved since FY2021. Buybacks mostly offset dilution |
| Insider alignment and compensation | 15 | **10** | Pay >95% performance-based and say-on-pay 91.94%. CEO cut his own cash bonus in 2024 over security failures. Routine 10b5-1 selling, including Nadella's $43.4M (Sep 2026). No open-market buys |
| Governance and integrity | 15 | **11** | 10 of 11 nominees independent; lead independent director; annual elections. Docked for: combined Chair/CEO; the CSRB's 2024 "inadequate" security-culture finding and a root-cause post left uncorrected ~6 months; three directors leaving at the 2026 AGM; OpenAI/Anthropic entanglement under FTC review |
| **Total** | 100 | **74** | |

---

## 1. Leadership and track record

| Person | Role | Tenure facts |
|---|---|---|
| **Satya Nadella** | Chairman and CEO | CEO since February 2014 [S: CNBC, "first decade" piece, 2024-02-04]. Listed as Chair and CEO; Sandra E. Peterson is Lead Independent Director [S: Microsoft board pages; 2026 proxy summary]. Year he became Chair not verified this session |
| **Amy Hood** | EVP and CFO | Listed as EVP and CFO [S: Microsoft leadership page]. *Start year (2013) is analyst recollection, not re-verified; carries no weight* |

**Record, judged on actions:**
- **The cloud pivot delivered.** Azure and other cloud services passed **$100B in FY2026 (+41%)** [F]. Microsoft disclosed Azure revenue in dollars for the first time in Q1 FY27: **~$33.2B, +48%** [S: CNBC/SiliconAngle via search].
- **Operating discipline.** FY2026 operating margin 46.8%, up 116bp, while D&A grew +30.9% [F]. Q1 FY27 operating income **$45.9B, +21%**, on revenue of **$92.3B, +19%** [P].
- **Willingness to cut.** More than 15,000 roles were cut in 2025 [S: NBC/HR Grapevine]. In Nadella's own words, the cuts came amid "the enigma of success in an industry that has no franchise value" [S: memo, Jul 2025, via NBC]. Xbox took ~1,600 more cuts in July 2026, with five studios closing and four being spun out [F].
- **Bench depth is thinning (2026)** [F news §3.6]:
  - Phil Spencer (Gaming CEO) and Sarah Bond left (announced 2026-02-20).
  - Rajesh Jha (EVP Experiences + Devices; owned M365 Copilot, Windows and Office) left, effective 2026-07-01. He was replaced by four EVPs rather than one successor.
  - **Eric Boyd** (President, AI Platform, ~17 years) left to run infrastructure at **Anthropic**.
  - The Microsoft AI CMO left after ~6 months.
  - Most are retirements after long careers. **Boyd's move to a company Microsoft both funds and hosts is the substantive one.**

**Verbatim (primary):**
- Nadella, FY26 Q4 release, 2026-07-29: "We are advancing the frontier on the cost-to-outcome curve, ensuring every customer can turn tokens into business results," [P].
- Nadella, FY27 Q1 release, 2026-10-28: "We are delivering greater capability, choice, control, and cost efficiency for customers across our entire stack," [P].

## 2. Promise-vs-delivery record (guidance credibility)

| Date of guidance | What was guided | Outcome | Kept? |
|---|---|---|---|
| 2025-01-29 (FY25 Q2 call) | Capacity "roughly in line with near-term demand" by FY-end 2025-06-30 [S: Yahoo/DCK] | Still constrained; the timeline was pushed out (next row) | **Missed** |
| Oct 2025 (FY26 Q1 call) | "Therefore, we now expect to be capacity constrained through at least the end of our fiscal year." [S: CIO Dive/Benzinga] | Still short at FY-end. 2026-10-28: "We still have demand that exceeds supply" [S] | **Missed again** |
| 2025-07-30 (FY25 Q4 call) | FY26 capex growth to slow; Q1 FY26 capex "over $30B" [S: CFO Dive] | Q1 FY26 capex **$34.9B** [S]. On 2025-10-29 Hood reversed: "Therefore, total spend will increase sequentially, and we now expect the FY'26 growth rate to be higher than FY'25." [S: CFO Dive]. FY26 cash capex finished **+79.6% vs FY25's +45.1%** [F] | **Reversed in one quarter** |
| 2025-07-30 | FY26 operating margins "relatively unchanged"; ETR 19–20% [S: Motley Fool transcript summary] | Operating margin **+116bp to 46.8%**; ETR 19.4% [F] | **Beat / met** |
| Jan 2026 (FY26 Q2 call) | Q3 Azure +37–38% cc | **+39% cc** (one outlet reports 40%) [S: Futurum; Quartz] | **Beat** |
| Apr 2026 (FY26 Q3 call) | Q4 Azure +39–40% cc | **+43%** [S; F] | **Beat** |
| 2026-07-29 (FY26 Q4 call) | Q1 FY27 Azure ~+45% cc | **+48%** [S] | **Beat** |
| Apr 2026 → Jul 2026 → Oct 2026 | Calendar-2026 capex ~$190B → **~$175B** ("useful life impact" plus the finance-to-operating lease shift; underlying plans "unchanged") → **$170–175B** (sources differ; delayed third-party capacity) [F; S: The Star/Reuters; letsdatascience] | Two re-basings in six months, the first purely definitional | **Metric unstable** |
| 2026-07-29 | Q1 FY27 reported capex ~$50B [S: The Star/Reuters] | **$45.2B incl. finance leases; $39.4B cash** [S; P]. The miss was attributed to delayed third-party capacity [S: Zacks] | Under; explained |
| 2026-07-29 | Remain free-cash-flow positive in FY27 [F] | Q1 FY27 FCF **$18.6B**, down 27% YoY [S: Inside.com.tw; Zacks] | **On track** |
| 2030 pledge (2020 baseline) | Carbon negative by 2030 | Emissions ~13Mt CO2e (2020) → ~20Mt (FY2025), **+25% YoY** in FY2025 [S: GeekWire; Engadget, Jul 2026]. The CSO says the company remains "really... focused around carbon negativity by 2030" [S: GeekWire] | **Off track** |

**Reading the pattern:**
- **Revenue and margin guidance is credible and conservative.** Three consecutive Azure beats, against guides that called for *acceleration* in two of them. Q2 FY27 is guided to **+49–50% cc** and revenue of **$96.0–97.1B** [S].
- **Supply-side and capex guidance is not.**
  - The capacity catch-up date has slipped twice.
  - The FY26 capex-growth direction flipped within three months.
  - The capex number itself has been redefined: DC/building useful life 15 → 25 years from FY27, more leases shifted to operating, and $329.1B of uncommenced leases at 2026-06-30 sitting outside capex [F].
  - **A guided figure that management can lower by changing an accounting estimate is a weaker commitment than a revenue guide.** Valuation and risk work should model total infrastructure commitments, not the capex line.
- **Candour is real.** Hood: "We've been short now for many quarters. I thought we were going to catch up – we are not." [S]. She owns the miss rather than blaming suppliers. That is the opposite of blame-shifting, and I credit it.
  - *Date conflict (L-001):* a search extraction (Benzinga URL path `/25/10/`) places this quote on the **October 2025** call. The firm's August news report attributed a near-identical quote to the **2026-07-29** call. **Unresolved without the transcript.** She may have said it twice.
- **Disclosure moves both ways:**
  - **Withdrawn:** AI's contribution to Azure growth, in FY2026 [F].
  - **Added:** Azure revenue in dollars, in Q1 FY27 [S].
  - **Disclosed then withheld:** M365 Copilot paid seats. Microsoft reported "30+ million" at Q4 FY26 [F], then in Q1 FY27 Nadella cited +50% QoQ *usage* growth but **declined to give the paid-seat count** [S: SiliconAngle/Futurum via search]. Switching a KPI off right after a strong print is a mild metric-selection flag.

## 3. Capital allocation scorecard

| Lever | Record (sourced) | Assessment |
|---|---|---|
| **Buybacks** | FY23–FY26: $22.2B / $17.3B / $18.4B / $22.3B [F, from P]. Diluted shares 7,472m → 7,453m (−0.26% over three years) [F]. ~89% of gross buyback offset equity issuance [F, estimate-dependent]. Q4 FY26 purchases at $396.19–$416.81 [F]. **Q1 FY27 repurchases $4.4B** [P, cash-flow statement]. $60B programme approved 2024-09-16, with **$40.6B remaining at 2026-06-30** [S: FY26 10-K via search]. No new authorisation alongside the Sep 2026 dividend [S] | **A dilution-offset programme, not a value-timed one.** No evidence of buying more on weakness. The Q1 FY27 slowdown looks like cash conservation for capex [E] |
| **Dividends** | FY26 $26,445M paid [P]. Q1 FY27 $6.8B [P]. Quarterly rate **$0.91 → $0.98 (+7.7%)** declared 2026-09-15 [S; C], vs +10% in Sep 2024 [S: Fortune] | Never cut; growth is slowing as capex absorbs cash. A sensible priority order |
| **M&A, Nadella era** | Nokia handsets (~$7.2–7.6B, 2014) fully written off in 2015 [S]. Nadella cleaned up an inherited deal quickly. **LinkedIn** $26.2B (2016): revenue still +12% in Q4 FY26 [P]. **GitHub** $7.5B (2018) [S]. **Activision Blizzard**: total purchase price $75.4B [S]. In FY26 Q4, Xbox content and services fell 10% and the release cites "impairment charges in XBOX" [P]. Layoffs and studio closures/spin-outs followed [F] | LinkedIn and GitHub: value-creating. **Activision: the largest deal of the era and, on current evidence, value-destructive.** Management is now cutting rather than doubling down, which is the right response, made late |
| **Strategic AI stakes** | OpenAI: ~$13B commitment ($11.8B funded at 2026-03-31) → ~27% of OpenAI Group PBC, valued ~$135B [F]. FY26 net income +$4,963M (+$0.67 EPS) from OpenAI [P]. Q1 FY27 +$207M (+$0.03), vs −$3.1B (−$0.41) a year earlier [P]. Anthropic: up to $5B (Nov 2025) [F]; $3.2B gain in Q4 FY26 [F] | **Financially exceptional.** Strategically it has turned into a dependency (§6.2). The marks are excluded from non-GAAP, which is clean, but see flag 3 in §7 |
| **AI capex** | FY26 cash capex **$115.9B (+79.6%)** [F]. Q1 FY27 **$39.4B vs $19.4B** (+103%) [P; C]. FCF: FY24 $74.1B → FY25 $71.6B → FY26 $67.0B [F] → **Q1 FY27 $18.6B (−27%)** [S]. ROIC ~45.6% (FY21) → ~20.5–26.1% (FY26) across three vendors [F moat]; 巴爺爺's own FY26 calculation is 26.5% [F]. Uncommenced leases $329.1B [F] | **Revenue response is real** (Azure +48%). **Return on the spend is unproven and trending down.** Still above WACC, but the spread has compressed from ~36pp to ~8–14pp [F moat]. FY2027–28 is the test |

**Net:** the capital-allocation judgement rests on one bet. If AI capex earns >20% incremental ROIC, as Morgan Stanley argues it can [F news §6.2], this team will look prescient. If it does not, the falling FCF and redefined capex metrics will be the record. **I score the bet as unproven, not as wrong.**

## 4. Insider activity

| Insider | Date | Transaction | Size | Plan / notes | Source |
|---|---|---|---|---|---|
| **Satya Nadella** (Chair, CEO) | **2026-09-01** | Sale | **86,525 shares at w.a. $501.46 = ~$43.4M** | 10b5-1 plan adopted Mar 2026 (one source: 2026-03-08). **15.09% of his direct holding.** 486,763 shares direct afterwards; 431,464 indirect via GRATs (single source) | InsiderTrades 2026-09-03; TechStory [S] |
| **Amy Hood** (CFO) | Oct 2026 | Sales | Aggregators ~$24.7M across two filings. Line items do not reconcile | 10b5-1 plan adopted **2026-06-10** | Form 4 summary via search [S] |
| Brad Smith (Vice Chair, President) | Date not obtained | Sale | 38,500 shares at ~$518.64 (~$20M) | — | Simply Wall St [S] |
| Judson Althoff | Jun 2026 | Sale | 15,500 shares at ~$461 (~$7.15M); 110,477 shares held afterwards | — | InsiderTrades 2026-06-03 [S] |
| All insiders | Trailing 12 months | Open-market sales | **~$114.6M**; no open-market purchases found | — | Aggregator via search [S] |

**Nadella's stake:** 486,763 direct + 431,464 indirect = **918,227 shares** [C]. At $501.46 that is **~$460M** [E]. The September sale was **~8.6% of his total pre-sale stake** [E — the indirect figure is single-sourced].

**Signal assessment: neutral.**
- Pre-scheduled 10b5-1 sales by executives whose wealth is concentrated in the stock are routine. The sizes are modest against holdings, and nothing clusters before bad news.
- **No open-market purchases by any insider were found.** That is normal for a $3.6T company but gives no positive signal.
- A TipRanks headline cites a separate "$75M" Nadella sale. Date not obtained; not used.

## 5. Compensation alignment

| Item | FY2026 | Source |
|---|---|---|
| Nadella total | **$90,628,977** (FY2025: $96,496,790; −6%) | 2026 proxy filed 2026-10-21, via FourWeekMBA / The Register [S] |
| — salary / stock / cash incentive / other | $2.5M / **$77,570,774** (85.6% [C]) / $10.3M / $259,203 | same [S] |
| Target performance stock award | **$50M, "unchanged since fiscal year 2022"** | proxy text quoted via search [S] |
| Performance-based share | ">95% of Mr. Nadella's annual total target compensation opportunity was performance-based" | proxy text quoted via search [S] |
| CEO pay ratio | ~421:1 (median employee $215,057) | Analytics Insight [S] |
| Hood total | **$33.7M** (single secondary source, Panabee). FY2025: $29,481,551 | [S] |
| Say-on-pay, Dec 2025 AGM | **91.94% for** | Microsoft voting results [P] |
| Accountability precedent | For FY2024, at Nadella's request, the board cut his cash incentive to **$5.2M (>50% below formula)**, tied to security failures. Security has been a pay metric since then | GeekWire 2024; 2024 proxy [S] |

**Assessment:**
- **The structure is good.** Pay is equity-heavy and performance-weighted, the target has been flat for five years, and shareholder support is solid.
- The CEO voluntarily cut his own pay over the security failures. That is the strongest single integrity signal in this file.
- **Not obtained:** the PSA metric mix (relative TSR vs operating metrics), and whether any metric penalises capital intensity or FCF. **If none does, the plan rewards growth regardless of what the capex costs.** That matters for this capex cycle and should be checked in the proxy.

## 6. Governance flags

### 6.1 Board independence
- **2026 AGM: 2026-12-08 (virtual).** The original proxy (2026-10-21) listed 12 nominees, 11 independent [S: Quartr summary].
- **Supplement dated 2026-11-09:** **Emma Walmsley withdrew** from re-election, citing no disagreement, and votes for her will not be counted. The board falls to **11 nominees, 10 independent** [S: Quartr summary]. She won 99.46% in 2025 [P].
- **Reid Hoffman and Hugh Johnston** are reported as leaving at the 2026 AGM [S: Quartr summary; **not corroborated elsewhere**]. Carmine Di Sibio joined in May 2026 [S]. The nominee count does not reconcile cleanly across summaries (12 − 2 + 1 ≠ 12). **Verify against the DEF 14A.**
- **Chair and CEO combined (Nadella).** Lead Independent Director: **Sandra E. Peterson** (96.78% in 2025 [P]). A shareholder proposal to **separate the Chair and CEO roles** is on the 2026 ballot; the board recommends against [S].
- **2025 support levels [P]:**
  - Nadella 93.46% (the second-lowest).
  - Johnston 91.53% (the lowest).
  - Human-rights due-diligence proposal 26.34%; data operations in human-rights hotspots 27.48%. These are material protest votes.
- **Assessment:** independence is strong on paper. **Losing up to three of twelve 2025 directors in one cycle, one of them by a mid-proxy withdrawal, is unusual for this board.** No disagreement is disclosed, and I read it as refresh, not revolt [E]. Watch the 8-K after the 2026-12-08 meeting.

### 6.2 OpenAI relationship governance
| Date | Event | Source |
|---|---|---|
| Nov 2023 | Microsoft takes a **non-voting observer** seat on OpenAI's board after Altman's reinstatement | Reuters via Yahoo [S] |
| 2024-07-09/10 | **Microsoft relinquishes the seat** amid US and UK antitrust scrutiny. OpenAI ends board observers | Axios; ABC/AP [S] |
| 2025-10-28 | OpenAI Group PBC formed. Microsoft holds ~27% (~$135B). IP rights through 2032, including post-AGI models. AGI to be verified by an independent expert panel. **Right of first refusal on compute lost.** OpenAI commits an incremental $250B to Azure | [F news §3.1] |
| 2026-02-16 | FTC probe covers cloud licensing, AI bundling **and the OpenAI partnership** | [F news §3.2] |
| 2026-02-27 | Joint statement: terms set in Oct 2025 unchanged | Microsoft blog [S] |
| 2026-04-27 | **Exclusivity ended.** OpenAI may sell on any cloud. Microsoft stops paying a revenue share. OpenAI's revenue share to Microsoft continues through 2030 under a cap (US$38B per the firm's news report) | Microsoft blog; OpenAI; The Register [S]; [F] |

**Assessment:**
- **Microsoft has no board seat, no observer and no exclusivity** at a company that is its largest single equity-method investee and the source of most of the +84% RPO headline (ex-OpenAI RPO was +25%) [F moat].
- **Governance tools are now contractual only.** The equity-method marks swing GAAP EPS (+$0.67 in FY26 [P]), but management excludes them from non-GAAP. That is clean, and I credit it.
- **Anthropic** is a second investee-customer: up to $5B invested, $30B committed to Azure [F]. It has now hired Microsoft's former AI Platform president.
- **The OpenAI + Anthropic web is a related-party-like concentration, even though it is not related-party in the legal sense.** The board's oversight of it is not disclosed in anything I could read.

### 6.3 Security culture: integrity screen
- The DHS Cyber Safety Review Board (report dated 2024-03-20, released 2024-04-02) found the 2023 Storm-0558 intrusion **preventable**. It called Microsoft's security culture **inadequate** and requiring an overhaul [S: DHS; GeekWire; Windows Central].
- **Microsoft acknowledged in November 2023 that its 2023-09-06 root-cause blog post was inaccurate. It did not update the post until 2024-03-12** [S: CSRB report via search].
- Management's response: the Secure Future Initiative, a security metric in executive pay, and the CEO's self-requested bonus cut (§5).
- **Assessment:** a real candour lapse (about six months uncorrected), followed by real accountability. **Historic, not current.** I found no repeat.

## 7. Red flags (ranked)

1. **Capex guidance and definitions are moving targets** (§2). FY26 direction reversed. CY2026 re-based twice. DC useful life 15 → 25 years. Operating-lease shift. $329.1B of uncommenced leases [F].
2. **FCF falling under a capex programme with unproven returns** (§3). FY24 → FY26 −9.6% [F]; Q1 FY27 −27% [S]. ROIC roughly halved [F].
3. **Selective KPI disclosure.** AI attribution withdrawn. Copilot seats disclosed then withheld. OpenAI economics visible only in aggregate. 巴爺爺 inferred that **the $3.2B Anthropic gain appears to remain inside non-GAAP EPS** while OpenAI gains are excluded [F, inference, unverified]. If confirmed, that is an inconsistent adjustment policy and should be raised with IR.
4. **Concentrated, circular AI counterparty exposure** with no governance seat (§6.2), under an FTC probe.
5. **Leadership and board churn in 2026** (§1, §6.1).
6. **Activision**: the era's largest deal, now impaired and shrinking (§3).
7. **Carbon-negative-2030 pledge off track** (§2). Strategic promises are slipping as AI capex grows.

**Integrity screen:**
- No restatement found.
- No abrupt CFO departure.
- No blame-shifting found; Hood's capacity admissions are self-attributing.
- OpenAI marks are excluded from non-GAAP.
- The one historic candour lapse is the uncorrected Storm-0558 root-cause post (§6.3).

## 8. What this management team would do in a downturn *(inference from the record, not a forecast)*

- **Protect the dividend; let buybacks flex.** The dividend has never been cut, and raises slowed to +7.7% this year. Buybacks fell to $4.4B in Q1 FY27 [P] at a high share price. In a downturn, expect buybacks to shrink further toward the dilution-offset floor, not to rise counter-cyclically.
- **Pace infrastructure through leases, not cancellations of owned assets.** In 2025 the company paced and adjusted leases ("While we may strategically pace or adjust our infrastructure in some areas, we will continue to grow strongly in all regions" [F]). Hood said spending can be reined in if demand changes [S: Stocktwits headline]. The operating-lease shift *increases* that flexibility. Expect capex cuts to show up first as deferred lease commencements.
- **Cut headcount early in non-core units.** The 2025 cuts (>15,000) came at record profitability [S], and the Xbox cuts came under a margin target [F]. This team does not wait for a downturn to restructure, so a downturn would accelerate cuts in Gaming and Devices.
- **Keep funding Azure/AI and its own MAI models.** "Set free" from OpenAI to pursue frontier research (Suleyman [F]), management would likely defend the AI roadmap over near-term margin.
- **Guide conservatively on revenue, and expect capex definitions to keep evolving.** Model total infrastructure commitments (capex plus operating leases plus uncommenced leases), not the headline capex guide.

## 9. Cross-checks against the August package (L-001)

| Item | August report | This review |
|---|---|---|
| FY26 shareholder returns | $48.7B [F fin., news] | Confirmed from the primary FY26 Q4 release: dividends $26,445M + repurchases $22,271M = $48,716M [P; C] |
| Buyback authorisation | News §3.7: no 2025/26 authorisation found; "do not state 2024 is current" | The FY26 10-K extraction says the **2024-09-16 $60B programme is current, with $40.6B remaining at 2026-06-30** [S] |
| Hood "short... catch up" quote | Dated to the 2026-07-29 call [F news] | A search places a near-identical quote on the Oct 2025 call. **Unresolved** |
| "Remain FCF positive in FY27" | Guided 2026-07-29 [F] | Q1 FY27 FCF $18.6B positive (−27% YoY) [S] |
| Q1 FY27 Azure guide ~45% | [F news §2a] | Delivered 48% [S] |

## 10. NOT OBTAINED

1. **2026 DEF 14A text**: PSA metric mix, Hood's pay from the filing itself, beneficial-ownership table, the nominee list after the supplement, and the reason for Hoffman's and Johnston's departures.
2. **Form 4s read directly.** Hood's October 2026 totals do not reconcile. The date of Smith's sale. The date and size of the "$75M" Nadella sale.
3. **FY26 Q4 and FY27 Q1 call transcripts.** Exact Azure guidance wording and the cc vs reported basis for every quarter; the date of the "catch up" quote.
4. **Average repurchase price for FY24–FY26.** Whether buyback pace responds to price.
5. **Activision impairment amount** and the goodwill-vs-intangible split.
6. **Board oversight disclosure** for OpenAI/Anthropic exposure. Status of the FTC probe after Feb 2026.
7. **Whether the Anthropic gain is inside non-GAAP** (巴爺爺's inference).
8. **Year Nadella became Chair and Hood's CFO start date** (not re-verified this session).

## Calibration vs firm files

| Report | Grade | Score |
|---|---|---|
| reports/equity/2026-07-18-mu-management.md | A− | none recorded |
| reports/equity/2026-07-19-klac-management.md | A− | none recorded |
| reports/equity/2026-07-19-mrvl-management.md | B+ | none recorded |
| reports/equity/2026-11-16-aapl-management.md | B | 72/100 |
| reports/equity/2026-11-25-6160hk-management.md | C+ | 68/100 (6.8/10) |
| **This report (MSFT)** | **B** | **74/100 (7.4/10)** |

**Why MSFT sits two points above AAPL:**
- Microsoft's AI execution is delivering revenue (Azure +48%), while Apple's flagship AI promise slipped twice.
- Its board is more independent (no executive chair predecessor).
- The CEO has a documented act of pay accountability.

**Why MSFT is not higher:** capex guidance credibility, falling FCF and ROIC, and selective KPI disclosure.

## Sources

- [Microsoft FY27 Q1 earnings release (primary, opened)](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) · [Microsoft FY26 Q4 earnings release (primary, opened)](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) · [Microsoft 2025 voting results (primary, opened)](https://www.microsoft.com/en-us/investor/corporate-governance/votingresults.aspx)
- [Zacks, Q1 FY27](https://www.zacks.com/stock/news/3018768/microsoft-q1-earnings-beat-estimates-as-cloud-accelerates) · [SiliconAngle](https://siliconangle.com/?p=852356) · [AI Weekly](https://aiweekly.co/alerts/microsoft-q1-revenue-hits-923b-azure-up-48-as-capex-jumps-to-394b-with-175b) · [247 Wall St](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb) · [Inside.com.tw, FCF −27%](https://www.inside.com.tw/article/42759-microsoft-fy2027-q1-earnings-azure-48-percent-capex-free-cash-flow) · [Redmond Mag](https://redmondmag.com/articles/2026/10/30/microsoft-revenue-jumps-as-azure-and-ai-demand--fuel-growth.aspx?admgarea=BDNA) · [Futurum, Q1 FY27](https://futurumgroup.com/?p=97413) · [FourWeekMBA, Q2 guide](https://fourweekmba.com/ai-microsoft-sees-azure-growing-up-to-50-as-revenue-nears-97b/) · [letsdatascience, $170B](https://letsdatascience.com/news/microsoft-cuts-2026-capex-forecast-to-170-billion-on-delayed-741510fe) · [The Star, Reuters, 2026-07-31](https://www.thestar.com.my/business/business-news/2026/07/31/microsoft-sees-strong-cash-flow-lower-capex)
- [CFO Dive, capex reversal, Oct 2025](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/) · [SiliconAngle, 2025-10-29](https://siliconangle.com/2025/10/29/microsofts-stock-falls-ai-spending-concerns-lack-clarity-openai/) · [Benzinga, Hood on capacity, Oct 2025](https://benzinga.com/markets/tech/25/10/48518415/microsoft-cfo-amy-hood-says-cloud-revenue-figures-could-be-higher-but-azure-is-short-on-capacity-as-ai-demand-soars) · [CIO Dive](https://www.ciodive.com/news/microsoft-AI-cloud-growth-earnings-Q1/804338) · [Data Center Knowledge, Jan 2025](https://datacenterknowledge.com/cloud/microsoft-cloud-growth-constrained-by-data-center-shortage) · [Motley Fool, FY25 Q4 transcript](https://www.fool.com/earnings/call-transcripts/2025/08/05/microsoft-msft-q4-2025-earnings-call-transcript) · [Futurum, Q3 FY26](https://www.futurumgroup.com/insights/microsoft-q3-fy-2026-earnings-show-cloud-growth-with-capacity-still-tight/) · [Quartz, Q4 FY26](https://qz.com/microsoft-earnings-azure-100-billion-cloud-073026) · [Fierce Network](https://www.fierce-network.com/cloud/microsoft-azure-crosses-100b-mark-growth-hits-four-year-high)
- [InsiderTrades, Nadella $43.4M, 2026-09-03](https://www.insidertrades.com/alerts/nasdaq-msft-insider-buying-and-selling-2026-09-03/) · [TechStory](https://techstory.in/microsoft-ceo-satya-nadella-sells-43-million-of-stock/) · [InsiderTrades, Althoff, 2026-06-03](https://www.insidertrades.com/alerts/nasdaq-msft-insider-buying-and-selling-2026-06-03/) · [Simply Wall St, insider sale](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/this-insider-has-just-sold-shares-in-microsoft-3) · [Massive.com MSFT insider page](https://massive.com/quote/msft/insider-trading) · [TipRanks, $75M headline (not used)](https://www.tipranks.com/news/msft-insider-trade-alert-ceo-satya-nadella-sells-75m-in-stock)
- [SEC DEF 14A FY2026 (not opened)](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526427849/d61756ddef14a.htm) · [FourWeekMBA, Nadella pay](https://fourweekmba.com/ai-microsoft-ceo-nadellas-pay-falls-6-to-90-6-million/) · [The Register](https://www.theregister.com/a/5305737) · [Analytics Insight, pay ratio](https://www.analyticsinsight.net/ampstories/business/microsoft-ceo-earns-421-times-more-than-the-median-employee) · [Panabee, exec comp](https://www.panabee.com/news/microsoft-executive-compensation-2026) · [Fox Business, FY25 pay](https://foxbusiness.com/technology/microsoft-ceo-satya-nadellas-annual-pay-climbs-96-5m) · [GeekWire 2024, bonus cut](https://www.geekwire.com/2024/microsoft-ceo-satya-nadellas-comp-tops-79m-as-stock-soars-cash-bonus-cut-in-half-on-security-woes/) · [TechRadar, security-linked pay](https://techradar.com/pro/security/microsoft-is-tying-executive-pay-to-security-performance-so-if-it-gets-hacked-no-bonuses-for-anyone)
- [Quartr proxy summary](https://quartr.com/events/microsoft-corporation-msft-proxy-filing_3s18prv1) · [Quartr, Nov 9 supplement](https://quartr.com/events/microsoft-corporation-msft-proxy-filing_3s18pfxi) · [Quartr 3](https://quartr.com/events/microsoft-corporation-msft-proxy-filing_3s18prvR) · [Microsoft annual meeting page](https://www.microsoft.com/en-us/investor/annual-meeting.aspx)
- [Financebuzz, dividend hike](https://financebuzz.com/news/microsoft-dividend-hike-ai-spending) · [Blockonomi, +8%](https://blockonomi.com/microsoft-msft-stock-dividend-rises-8-as-ai-spending-soars-to-145b/) · [Fortune, Sep 2024 $60B buyback](https://fortune.com/2024/09/16/microsoft-60-billion-stock-buyback-10-percent-dividend-increase/) · [SEC 10-K FY2026 (not opened)](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm) · [Equibles buybacks](https://equibles.com/stocks/msft/buybacks)
- [Axios, observer seat, 2024-07-10](https://www.axios.com/2024/07/10/microsoft-openai-board-seat-observer) · [Reuters via Yahoo](https://ca.finance.yahoo.com/news/microsoft-ditches-openai-board-observer-050715476.html) · [ABC/AP](https://abcnews.go.com/amp/US/wireStory/microsoft-quits-openai-board-seat-antitrust-scrutiny-ai-111803838) · [Microsoft blog, 2026-04-27](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/) · [Microsoft blog, 2026-02-27](https://blogs.microsoft.com/blog/2026/02/27/microsoft-and-openai-joint-statement-on-continuing-partnership/) · [The Register, 2026-04-27](https://www.theregister.com/2026/04/27/microsofts_and_openai_change_relationship/)
- [DHS, CSRB release, 2024-04-02](https://dhs.gov/news/2024/04/02/cyber-safety-review-board-releases-report-microsoft-online-exchange-incident-summer) · [CSRB report PDF](https://www.cisa.gov/sites/default/files/2024-04/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf) · [GeekWire 2024](https://www.geekwire.com/2024/cyber-safety-review-board-finds-microsoft-security-culture-inadequate-calls-for-internal-accountability/) · [Windows Central](https://www.windowscentral.com/microsoft/microsofts-security-culture-was-inadequate-and-requires-an-overhaul-says-cyber-safety-review-board-following-a-cascade-of-security-failures)
- [GeekWire, emissions +25%, 2026](https://www.geekwire.com/2026/microsofts-carbon-emissions-climb-25-as-tech-giants-grapple-with-ais-energy-toll/) · [Engadget](https://engadget.com/2212136/microsoft-ai-drive-carbon-emissions-grow-25-percent-2025) · [The Next Web](https://thenextweb.com/news/microsoft-emissions-25-percent-ai-data-centres)
- [NBC News, Nadella layoffs memo](https://www.nbcnews.com/business/business-news/microsofts-satya-nadella-says-job-cuts-weighing-heavily-rcna220879) · [HR Grapevine, 15,000 cuts](https://www.hrgrapevine.com/us/content/article/2025-07-28-microsoft-cuts-15000-jobs-despite-ai-led-profits-boom) · [CNBC, Nadella first decade](https://www.cnbc.com/amp/2024/02/04/microsoft-ceo-satya-nadella-hits-10-year-anniversary.html)
- [Fortune, Nokia/aQuantive write-offs](https://fortune.com/2016/06/15/microsoft-linkedin-deal-mas-fail/) · [Business Insider, M&A record](https://www.businessinsider.in/Microsoft-has-a-spotty-record-with-big-acquisitions-heres-a-rundown/11-On-December-31st-1997-Microsoft-bought-Hotmail-one-of-the-very-first-browser-based-e-mail-services-for-an-estimated-400-million-Hotmail-stuck-around-until-2012-or-so-when-Microsoft-started-transitioning-users-to-its-newer-Outlook-com-/slideshow/53103054.cms) · [CNBC, Nadella vs Ballmer M&A](https://www.cnbc.com/2018/06/04/microsoft-ma-nadella-vs-ballmer.html) · [GamesBeat, Xbox impairment](https://gamesbeat.com/microsoft-reports-strong-q2-results-amid-big-xbox-layoffs/) · [TweakTown, Xbox impairment](https://www.tweaktown.com/news/109962/xbox-margins-hit-by-mysterious-impairment-charge/index.html) · [ChannelNews, Activision purchase price](https://www.channelnews.com.au/microsofts-a121-billion-xbox-gamble-unravels-as-more-jobs-axed-and-studios-closed/) · [Stocktwits, Hood on reining in spend](https://stocktwits.com/news-articles/markets/equity/msft-stock-soars-after-results-cfo-dismisses-ai-overcapacity-narrative-says-can-rein-in-spending-if-demand-changes/cZNPZxzRJTH)

---
*Research and decision support only, not financial advice. The Committee and the Owner decide.*
