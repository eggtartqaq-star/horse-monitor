# MSFT: Microsoft Corporation. Financial Statement Update to Q1 FY2027

**Analyst:** 巴爺爺 (Dept 2, Equity Research, Financial Statements)
**Date:** 2026-11-25
**Updates:** `reports/equity/2026-08-21-msft-financials.md` (the "August report", which covered FY2023–FY2026)
**Latest reported quarter, verified:** **Q1 FY2027**, the quarter ended **2026-09-30**, released **2026-10-28** [M1]
**Status:** COMPLETE. The statements are primary (Microsoft IR pages opened); notes and 10-Q items are search-extracted.

---

## 0. Sourcing, staleness, provenance key

**Staleness:** 8 weeks past period end, 4 weeks past release. **Current.** Next print (Q2 FY27,
December quarter) is due around late January 2027.

| Tag | Meaning |
|---|---|
| **[P]** | Primary. Read from a `microsoft.com` IR page I opened this session (press release, metrics page, or the earnings-call page). |
| **[S]** | Search extraction from a document I could not open. Mostly the 10-Q on `sec.gov`, which is DNS-blocked this session. |
| **[C]** | My arithmetic on cited inputs |
| **[E]** | Estimate or inference, assumption stated |
| **[CONS]** | Third-party consensus. Not company data. |
| **[Aug]** | Carried forward from the August report ([P] FY2026 annual figures from the FY26 Q4 release) |

**Opened this session [P]:** the FY27 Q1 press release [M1], FY27 Q1 metrics [M2], the FY27 Q1
earnings-call page [M3], and the FY26 Q1, Q2 and Q3 press releases [M4, M5, M6].
**Blocked:** `www.sec.gov` (DNS, ENOTFOUND), so no 10-Q or 10-K was opened. Several other hosts also
failed DNS (see the 6160 update), so I stopped trying new hosts. The shared WebSearch budget ran out at
the end of this session. `tradingkey.com` was not used.

**Trailing-four-quarter method.** Q2–Q3 FY26 and Q1 FY27 come straight from the quarterly releases [P].
**Q4 FY26 is derived** as FY26 [Aug, P] minus Q1–Q3 FY26 [P]. TTM is the sum of the four, and it
cross-checks with FY26 + Q1 FY27 − Q1 FY26.

---

## 1. Summary and grade

### Grade: **B · 70/100**
The August report printed **A− 79**, but its components sum to **73**. See §10.

**The operating story got better. The cash story got worse.**

**Operations:**
- Revenue **$92,279M, +18.8%** [P/C].
- Operating margin **49.8%, +88bp** [C].
- **Azure disclosed in dollars for the first time: $33,165M, +48.2%** [P/C], accelerating from 42% in
  Q4 FY26 [P, recast].
- **Azure was 73.8% of all YoY revenue growth** [C].
- The bear case's trigger, Azure decelerating, **moved further away**.

**Cash:**
- FCF **$18,633M, −27.4% YoY** [C from P].
- Cash capex **$39,367M, +103%** [P/C].
- **TTM FCF is $59,957M**, down from $66,987M in FY26 and $74,071M at the FY24 peak [C].
- Capex is guided **above $50B in Q2** [P].
- The CFO's bar for the year is now that Microsoft "expect[s] to continue to remain **free cash flow
  positive in FY27**" [P, M3]. A company that produced $74bn of FCF two years ago now frames
  "positive" as the target.

**Three things moved the score from the corrected 73 to 70:**
1. **The FCF decline is accelerating:** −9.3% (Q2 FY26), −22.1% (Q3 FY26), −27.4% (Q1 FY27) YoY [C].
   Cash plus short-term investments fell **$37.5B in a year, to $64.5B** [C from P]. TTM shareholder
   payouts now exceed **FCF net of SBC** (101%) [C].
2. **OpenAI is now a quantified concentration.** The 10-Q reports **$10.0B of Q1 revenue from OpenAI
   (10.8% of total)** and **$7.2B of OpenAI receivables**, up from $6.0B at 30 June [S, M10]. That is a
   related party, loss-making, whose equity-method income Microsoft books on a
   **hypothetical-liquidation-at-book-value** basis [S].
3. **Gross margin erosion is now guided into operating margin.** Q1 gross margin was 67.8% (−126bp YoY)
   [C]. Microsoft Cloud gross margin was 66%, guided to ~65% [P]. The Q2 guide implies **gross margin
   down about 170–230bp** and **operating margin "down slightly year-over-year"** [P/C]. That is the
   first guided YoY operating-margin decline since the firm began coverage.

**Offsetting, and real:** Azure dollar disclosure plus OpenAI related-party disclosure is a genuine
**disclosure upgrade** (+1 on that line). The "other income" problem was quiet this quarter: other income
was only **$38M**, so GAAP EPS ($4.92) and non-GAAP EPS ($4.89) are nearly identical [P].

### The 3 numbers that matter most

| # | Number | Value | Why |
|---|---|---|---|
| 1 | **TTM free cash flow** | **$59,957M; FCF margin 17.3%; FCF/net income 0.42x** [C from P] | Down from $74.1B at the FY24 peak. FY27 is on track to be the third straight annual decline, which was my August trigger. |
| 2 | **Azure revenue** | **$33,165M, +48.2%; 73.8% of total revenue growth** [P/C] | This is the entire bull case. As long as it holds above roughly the mid-20s, the depreciation wave is being outrun. |
| 3 | **OpenAI revenue share** | **$10.0B, 10.8% of Q1 revenue; $7.2B receivables** [S] | Concentration in one loss-making related party, sitting against $329B of uncommenced leases [S]. |

---

## 2. Latest quarter and trailing four quarters

US$ millions except per-share amounts.

| | Q2 FY26 (Dec-25) | Q3 FY26 (Mar-26) | Q4 FY26 (Jun-26) [C] | **Q1 FY27 (Sep-26)** | **TTM** [C] | *Q1 FY26 (Sep-25)* |
|---|---|---|---|---|---|---|
| Revenue | 81,273 [M5] | 82,886 [M6] | 90,007 | **92,279** [M1] | **346,445** | *77,673* [M1] |
| YoY growth | +16.7% [C] | +18.3% [C] | +18% [Aug, S] | **+18.8%** [C] | — | |
| Gross margin | 68.0% | 67.6% | 67.2% | **67.8%** | **67.7%** | *69.0%* |
| Operating income | 38,275 | 38,398 | 40,603 | **45,915** | **163,191** | *37,961* |
| Operating margin | 47.1% | 46.3% | 45.1% | **49.8%** | **47.1%** | *48.9%* |
| Other income (expense), net | 9,971 | 942 | 3,444 | **38** | **14,395** | *(3,660)* |
| Net income | 38,458 | 31,778 | 35,766 | **36,629** | **142,631** | *27,747* |
| GAAP diluted EPS | $5.16 | $4.27 | ~$4.80 [C] | **$4.92** | **~$19.15** [C] | *$3.72* |
| OpenAI impact on net income | +7,583 | −14 | +480 [C] | **+207** | **+8,256** | *−3,086* |
| Non-GAAP diluted EPS | $4.14 | $4.27 | ~$4.74 [C] | **$4.89** | **~$18.04** [C] | *$4.13* |
| Operating cash flow | 35,758 | 46,679 | 55,441 | **58,000** | **195,878** | *45,057* |
| Additions to PP&E (cash capex) | (29,876) | (30,876) | (35,802) | **(39,367)** | **(135,921)** | *(19,394)* |
| **Free cash flow** [C] | **5,882** | **15,803** | **19,639** | **18,633** | **59,957** | *25,663* |
| FCF margin [C] | 7.2% | 19.1% | 21.8% | **20.2%** | **17.3%** | *33.0%* |
| FCF YoY [C] | −9.3% | −22.1% | n/o | **−27.4%** | — | |
| Stock-based comp | 3,219 | 3,081 | 3,122 | **3,134** | **12,556** | *2,983* |
| D&A and other | 9,198 | 10,167 | 11,022 | **11,744** | **42,131** | *8,147* |
| Wtd. diluted shares (M) | 7,460 | 7,445 | n/o | **7,446** | — | *7,466* |

Sources: [M1, M4, M5, M6]. The Q4 FY26 column is FY26 [Aug] less Q1–Q3. Quarterly EPS does not sum
exactly, so the TTM EPS figures are approximate. The Q2 FY25 and Q3 FY25 comparatives used for the YoY
lines come from the same releases [M5, M6].

**Q1 FY27 line detail [P, M1]:**
- Cost of revenue $29,720M (+23.6% [C]).
- R&D $9,047M (+11.1%), S&M $5,716M (flat), G&A $1,881M (+4.2%). Total opex $16,644M (+6.2%), which
  is **18.0% of revenue vs 20.2%** a year earlier [C].
- Pre-tax income $45,953M. Tax $9,324M, an **effective rate of 20.3%** vs 19.1% [C].
- Weighted shares: basic 7,426M, **diluted 7,446M (−0.27% YoY)** [C].

---

## 3. Segments: the reporting structure changed

### 3.1 What changed

In **September 2026** Microsoft replaced its three segments (Productivity & Business Processes,
Intelligent Cloud, More Personal Computing) with two, and recast prior periods. The company says the
recast is not a restatement [M8, M9 (S); M1 (P) confirms the recast language].
- **Agents and Infra (A&I):** Azure, Microsoft 365 cloud, productivity and server licensing, Industry
  Solutions (incl. Dynamics, LinkedIn Talent/Sales), and frontier and support services.
- **Devices and Consumer (D&C):** Windows OEM and devices, Xbox, and search and advertising (incl.
  LinkedIn Marketing Solutions).
- **Gained:** quarterly **Azure revenue in dollars**.
- **Lost:** the separate Intelligent Cloud margin. In August I identified that line as the leading
  indicator of the capex cycle (−62bp in FY26), and it **can no longer be tracked**. Cloud
  infrastructure margins now sit blended with M365 inside A&I. **The only remaining cloud-margin signal
  is the Microsoft Cloud gross margin KPI.**

### 3.2 Segment results [P, M1; margins C]

| Segment | Q1 FY27 revenue | YoY | Q1 FY27 op. income | YoY | Op. margin | Q1 FY26 op. margin | Δ |
|---|---|---|---|---|---|---|---|
| Agents and Infra | **76,795** | **+24.5%** | **40,558** | +24.0% | **52.8%** | 53.1% | **−24bp** |
| Devices and Consumer | **15,484** | **−3.2%** | **5,357** | +2.2% | **34.6%** | 32.8% | +183bp |
| **Total** | **92,279** | +18.8% | **45,915** | +21.0% | **49.8%** | 48.9% | +88bp |

FY2026 recast [S, M9]: A&I revenue $268,127M and operating income $136,365M (50.9% [C]); D&C
$63,712M and $18,872M (29.6% [C]). These sum exactly to the reported FY26 totals of $331,839M and
$155,237M [Aug], which is good internal validation of the extraction.
**TTM [C]:** A&I revenue $283,250M, operating income $144,205M (50.9%). D&C $63,195M, $18,986M (30.0%).

**A&I margin edged down 24bp while revenue grew 24.5%.** That is the blended version of the cloud-margin
compression I flagged in August. It is small, and still pointing the wrong way.

### 3.3 Revenue by offering [P, M1; growth and contribution C]

| Offering | Q1 FY27 | Q1 FY26 | YoY | $ change | Share of total growth |
|---|---|---|---|---|---|
| **Azure** | **33,165** | 22,384 | **+48.2%** | +10,781 | **73.8%** |
| Microsoft 365 cloud | 27,778 | 23,694 | +17.2% | +4,084 | 28.0% |
| Productivity and server licensing | 8,407 | 8,678 | −3.1% | −271 | −1.9% |
| Industry solutions | 5,337 | 4,894 | +9.1% | +443 | 3.0% |
| Frontier and support services | 2,108 | 2,022 | +4.3% | +86 | 0.6% |
| Search and advertising | 6,554 | 5,942 | +10.3% | +612 | 4.2% |
| Xbox | 5,379 | 5,508 | −2.3% | −129 | −0.9% |
| Windows OEM and devices | 3,551 | 4,551 | **−22.0%** | −1,000 | −6.8% |
| **Total** | **92,279** | **77,673** | **+18.8%** | **+14,606** | 100% |

**KPIs [P, M2; recast basis]:**

| | Q1 FY26 | Q2 FY26 | Q3 FY26 | Q4 FY26 | **Q1 FY27** |
|---|---|---|---|---|---|
| Azure growth | 40% | 39% | 40% | 42% | **48%** |
| Microsoft Cloud revenue ($B) | 49.1 | 51.5 | 54.5 | 59.3 | **63.9 (+30%)** |
| **Microsoft Cloud gross margin** | 68% | 67% | 66% | 65% | **66%** (Q2 guide ~65% [M3]) |
| Commercial bookings growth | +112% | +230% | −4% | +10% | **−12%** |
| Commercial RPO ($B) | 392 | 625 | 627 | 678 | **677 (+73% YoY; flat QoQ)** |
| M365 commercial seat growth | 7% | 7% | 6% | 7% | **5%** |

- **Azure growth on the recast basis was 42% in Q4 FY26, not the 43% in my August report** [S then; P
  now]. The definition is now "cloud and AI consumption-based services and virtual desktop offerings"
  [M2].
- **RPO has stalled.** It was **flat QoQ at $677B** and bookings fell 12%. The +73% YoY figure is the
  Q2 FY26 step-up from the OpenAI commitment rolling through. About **30% (~$203B [C]) is recognised in
  the next 12 months, +29%**, and the weighted-average duration is **2.3 years** [P, M3].
- **Copilot:** **no seat count was given this quarter.** The CFO said "we did not disclose… an update on
  the Copilot number this quarter" [P, M3]. We got only "customers with more than 50,000 seats up over
  8x YoY" and "millions of paid [premium] seats" [P, M3]. In August the figure was 30M paid seats [S].
  **There is still no Copilot revenue line**, and dropping the seat count is a disclosure step backward.

---

## 4. Profitability

### 4.1 Margins

| | FY24 | FY25 | FY26 | TTM Q1 FY27 | Q1 FY26 | **Q1 FY27** | Q2 FY27 guide [C from M3] |
|---|---|---|---|---|---|---|---|
| Gross margin | 69.8% | 68.8% | 67.9% | 67.7% | 69.0% | **67.8%** | **~65.7–66.3%** (Q2 FY26: 68.0%) |
| Opex / revenue | — | 23.2% | 21.1% | — | 20.2% | **18.0%** | ~19.1–19.4% (Q2 FY26: 20.9%) |
| Operating margin | 44.6% | 45.6% | 46.8% | 47.1% | 48.9% | **49.8%** | **~46.4–47.3%** (Q2 FY26: 47.1%) |

FY columns are from the August report [Aug]. Q2 FY27 implied ranges [C] use revenue of $96.0–97.1B,
COGS of $32.7–32.9B and opex of $18.5–18.6B [P, M3].

**The August thesis is playing out on schedule.** Gross margin keeps eroding and opex leverage is
carrying operating margin. Q1 opex grew only **+6.2%** against +18.8% revenue. In Q2 the guide has COGS
up **26–27%** against revenue **18–19%**, and opex leverage (+9% opex) **no longer fully offsets it**.
Operating margin is guided down slightly. Q2 opex includes an unquantified estimate for the **voluntary
exit offer** (about 60,000 eligible employees, ~27% of the workforce, per AP [S, M13]; the charge was not
disclosed [P, M3]). **Part of the opex leverage in coming quarters will be bought with a restructuring
charge.** Strip it from run-rate margin, but do not ignore it.

**The depreciation tail is heavier than I suggested in August.**
- D&A and other was **$11,744M in Q1, +44.2% YoY** [C from P], **12.7% of revenue** against 10.5% a
  year earlier. That acceleration came **despite** the building useful-life extension (15→25 years)
  taking effect in FY27 [S, M15].
- Management said **"roughly three quarters" of Q1 capex was short-lived assets, mainly CPUs and GPUs**
  [P, M3].
- In August I said my illustrative $19.3bn/yr depreciation figure for the FY26 cohort "overstates the
  true figure, probably materially", because much spend would be long-lived shells and land. **With ~75%
  short-lived in the latest quarter, that caveat was too generous.** The true figure is closer to the
  upper illustration than I implied [E].

### 4.2 ROE and ROIC

| Metric | FY26 [Aug] | TTM to Q1 FY27 | Basis |
|---|---|---|---|
| ROE (average equity) | 34.0% | **34.2%** [C] | TTM net income $142,631M ÷ avg(equity $363,076M at Sep-25 [M4], $470,509M at Sep-26 [M1]) |
| ROE ex-OpenAI marks | — | **32.2%** [C] | Net income less TTM OpenAI impact of $8,256M |
| ROIC | 26.5% | **~26.0%** [E] | NOPAT $131,070M (TTM operating income × (1 − 19.7% TTM ETR) [C]) ÷ invested capital ~$503.8B (bond debt $35,481M + finance leases $62,304M [S, **30 Jun figure, stale**] + equity $470,509M − cash and STI $64,509M) |

ROIC is drifting down slowly and is still roughly 3x any plausible cost of capital. **It is understated
in the denominator**, because uncommenced and operating leases (§6) sit outside invested capital.

---

## 5. Cash generation and FCF conversion

### 5.1 Conversion trend

| | FY24 | FY25 | FY26 | **TTM Q1 FY27** |
|---|---|---|---|---|
| FCF ($M) | 74,071 | 71,611 | 66,987 | **59,957** |
| FCF margin | 30.2% | 25.4% | 20.2% | **17.3%** |
| **FCF / GAAP net income** | 0.84x | 0.70x | 0.50x | **0.42x** |
| FCF / non-GAAP net income | — | — | 0.52x | **0.45x** |
| OCF / net income | 1.35x | 1.34x | 1.37x | **1.37x** |
| Capex / OCF | 37.5% | 47.4% | 63.4% | **69.4%** |
| Capex / revenue | 18.1% | 22.9% | 34.9% | **39.2%** |

FY figures are [Aug] (P inputs); TTM is [C from P].

**Read the last four rows together.** OCF conversion is **unchanged at 1.37x**, so the earnings are real
cash. **The entire decline in FCF conversion is capex.** In two years FCF has gone from 84% of net income
to 42%.

- **Q1 FY27 capex including finance leases was $45.2B.** Finance leases were $7.4B and cash paid for
  PP&E $39.4B [P, M3]. The gap between $39.4B + $7.4B and $45.2B reflects accrual vs cash timing.
  Management attributed the shortfall against the ~$50B prior guide to **delayed third-party capacity
  deliveries** [P, M3].
- **Calendar-2026 capex is now "approximately $170 billion"**, attributed to those delays [P, M3]. In
  July the figure was ~$175B, itself "restated" from ~$190B by the lease reclassification [Aug, S].
  **This is a timing slip, not a cut.**
- **Q2 FY27 capex is guided at "over $50 billion"** [P, M3]. Illustratively, if Q2 OCF grows in line with
  Q1 (+29% on Q2 FY26's $35,758M ≈ $46B [E]) and finance leases run near Q1's $7B, **Q2 FCF could be
  close to zero** [E]. Q2 is seasonally the weakest OCF quarter: Q2 FY26 FCF was only $5,882M [C]. That
  is the context for the CFO's "remain free cash flow positive in FY27".

### 5.2 SBC and capital returns

- **SBC** was $3,134M in Q1 (+5.1%; 3.4% of revenue) [C from P]. TTM SBC is $12,556M, **3.6% of
  revenue**. SBC intensity is still falling, as it was in August.
- **TTM returns:** buybacks $21,000M plus dividends $27,033M = **$48,033M** [C from P]. That is **80% of
  FCF** and **101% of FCF net of SBC ($47,401M)** [C]. **Microsoft is now returning more than its
  SBC-adjusted free cash flow.** The difference is funded from the securities portfolio.
- In Q1 Microsoft said it returned "$10.2 billion" [P, M1]. The cash-flow statement shows **$11,136M**
  (buybacks $4,379M plus dividends $6,757M) [P]. The difference is presumably accrual timing; the release
  does not explain it.

---

## 6. Balance sheet and debt

| [P] unless marked | 30 Sep 2025 [M4] | 30 Jun 2026 [M1] | **30 Sep 2026** [M1] | YoY |
|---|---|---|---|---|
| Cash and equivalents | 28,849 | 20,935 | **20,281** | −29.7% |
| Short-term investments | 73,163 | 55,908 | **44,228** | −39.5% |
| **Cash + STI** | **102,012** | 76,843 | **64,509** | **−36.8% (−$37.5B)** |
| Accounts receivable, net | 52,894 | 80,876 | **62,084** | +17.4% |
| Inventories | 1,130 | 1,397 | **1,835** | +62.4% |
| PP&E, net | 230,861 | 313,076 | **346,844** | **+50.2%** |
| Operating lease ROU assets | n/o | 24,177 | **30,178** | +24.8% QoQ |
| Total assets | 636,351 | 758,376 | **779,403** | +22.5% |
| Current portion of LTD | 7,832 | 9,227 | **4,391** | |
| Long-term debt | 35,376 | 31,067 | **31,090** | |
| **Bond debt total** [C] | **43,208** | 40,294 | **35,481** | −17.9% |
| Short-term unearned revenue | 58,987 | 72,965 | **66,866** | +13.4% |
| Operating lease liabilities (LT) | 17,348 | 16,532 | **21,719** | **+31.4% QoQ** |
| Finance lease liabilities | n/o | **62,304** [S, Aug] | **n/o** | — |
| Total stockholders' equity | 363,076 | 442,387 | **470,509** | +29.6% |

**Net position at 30 Sep 2026:**
- **Ex-leases: net cash of $29,028M** [C] (cash + STI $64,509M − bonds $35,481M). It was $58,804M a
  year earlier, so **it has halved in 12 months**.
- **Including finance leases: net debt of about $33.3B** [E]. That uses the 30 June finance-lease
  figure, which is stale and very likely higher by September given $7.4B of new finance leases in Q1.

**Off-balance-sheet and lease build-up, the largest unquantified item (as it was in August):**
- Operating lease liabilities rose **$5.2B in one quarter** and ROU assets **$6.0B** [C from P]. The
  finance-to-operating-lease shift announced in July is now visible on the balance sheet.
- **Leases signed but not yet commenced were $329.1B at 30 Jun 2026**, per the FY26 10-K [S, M11]. They
  are mostly data centres, commence FY27–FY33, and run 1–20 years; some are subject to conditions. The
  prior-year comparator is **conflicting in the sources ($196.6B vs $92.7B)** and is unresolved.
  **$329B is 2.4x TTM cash capex.** Under the new lease classification, much of it will reach the P&L as
  operating lease cost and **will never appear in "capex"**.

**Debt service is still not a risk.** Bonds fell further: Microsoft **repaid $4,850M in Q1** [P] and
issued no new bonds. TTM operating income of $163.2B is about 4.6x bonds and 1.7x bonds plus June
finance leases [C]. **My August tell (renewed bond issuance) has not happened.** But the liquidity buffer
is being consumed at about $12B a quarter: −$12.3B in Q1 [C].

---

## 7. OpenAI accounting, updated

| Item | Value | Source |
|---|---|---|
| Accounting | Equity method, using **hypothetical liquidation at book value (HLBV)**, because Microsoft's liquidation rights differ from its ownership interest | [S, M10, 10-Q via secondary] |
| Stake | **~24% as-converted** (was ~27% after the Oct 2025 restructuring) | [S, M10; one source, wording unconfirmed] |
| Q1 FY27 P&L impact | **Net gains of $272M pre-tax** [S]; **+$207M net income, +$0.03 EPS** [P, M1] | |
| Q1 FY26 P&L impact | Net losses of ~$4.1B pre-tax [S]; −$3,086M net income [P] | |
| TTM net-income impact | **+$8,256M (~$1.11/share)** [C from P] | |
| Funding | **$13.0B committed, $12.0B funded** at 30 Sep 2026 (Aug: $11.8B at 31 Mar) | [S, M10] |
| **Revenue from OpenAI** | **$10.0B in Q1 FY27, including revenue-share payments; 10.8% of revenue** [C] | [S, M10] |
| **Receivables from OpenAI** | **$7.2B at 30 Sep** (vs $6.0B at 30 Jun), **11.6% of AR** [C] | [S, M10] |

**Assessment:**
1. **HLBV explains why the equity-method line does not track OpenAI's operating losses.** It measures
   Microsoft's claim in a hypothetical liquidation of OpenAI's book value. New capital raised by OpenAI
   can therefore produce gains even in loss-making periods, as in Q2 FY26 (+$7.6B). **The line remains
   unforecastable. Value MSFT on non-GAAP EPS or operating income.**
2. **The revenue disclosure is the bigger news.** About one dollar in nine of Microsoft revenue comes
   from a single related-party counterparty that depends on outside fundraising. Two points sharpen it:
   - OpenAI receivables **rose 20% QoQ while every other receivable was seasonally collected.** Ex-OpenAI
     AR fell from about $74.9B to $54.9B [C].
   - OpenAI's DSO is about 66 days [C: 7.2/10.0 × 92], close to the company average, so this is **not**
     a collection problem today.
   It is still the line to watch. **Q1 FY26 OpenAI revenue was not obtained**, so I cannot say how much
   of Azure's acceleration is OpenAI.
3. In August, CFO Amy Hood said "nearly 90% of Microsoft Cloud revenue" comes from customers outside the
   frontier labs [Aug, S]. That is **broadly consistent** with OpenAI at 10.8% of total revenue. The two
   denominators differ, so this is not a reconciliation.

---

## 8. Accounting red flags and August trigger check

### 8.1 Screen

| Test | Result | Change since August |
|---|---|---|
| Earnings vs operating cash flow | **CLEAN.** OCF/net income 1.58x in Q1 and 1.37x TTM [C]. | Unchanged |
| Receivables vs revenue | **CLEAN** at the total level: AR +17.4% vs revenue +18.8%; seasonal DSO 61.9d vs 62.6d [C]. **WATCH** the OpenAI receivable (§7). | Improved; new sub-item |
| Deferred revenue | **CLEAN.** Short-term unearned +13.4% vs revenue +18.8% [C], the same structural consumption-mix pattern as August. | Unchanged |
| Inventories | **MINOR.** +62.4% YoY, but only $1.8B. | Unchanged |
| "Other income" doing the work | **Quiet this quarter** ($38M). But TTM other income of $14,395M is still **8.1% of TTM pre-tax income** [C]. | Better in Q1, not in TTM |
| Anthropic gain inside non-GAAP | **Unresolved.** Non-GAAP still excludes only OpenAI [P, M1]. Ex-OpenAI other income was −$234M in Q1 [P, M3], so no Anthropic mark this quarter. | Unchanged |
| Estimate changes | **WATCH.** The building life extension (15→25 years) is now in effect [S]. **Server and network life is still unverified** (10-K blocked). Gross servers, networking and software reportedly $215.87B at FY26 vs $132.84B [S, M16]. | Unchanged |
| Capex definition | **WATCH, now visible.** Operating lease liabilities +31% QoQ; $329.1B of uncommenced leases [S]. | Worse (more evidence) |
| **Revenue concentration (OpenAI)** | **WATCH, new.** 10.8% of revenue, related party [S]. | New |
| Restructuring | **WATCH, new.** Voluntary exit offer cost is embedded in Q2 guidance and not quantified [P/S]. | New |
| Share-count creep | **CLEAN.** Diluted shares −0.27% YoY [C]. | Unchanged |
| Tax | **CLEAN.** Q1 ETR 20.3%, Q2 guide ~20% [P]. | Unchanged |

### 8.2 Status of the August "what would change my mind" triggers

| August trigger | Status |
|---|---|
| Azure < 25% for two quarters | **Not triggered.** 48% and accelerating; Q2 guide 49–50% cc [P]. |
| Intelligent Cloud margin down >200bp YoY | **No longer measurable** (segment retired). Successor A&I margin −24bp [C]; Microsoft Cloud GM 68%→66% YoY [P]. |
| FY27 FCF falls a third consecutive year | **On track to trigger.** Q1 −27.4%, TTM −10.5% vs FY26 [C]. Management frames the bar as "FCF positive". |
| Gross margin down >150bp with opex ratio flat | **Close.** Q1 −126bp with opex ratio −213bp. **The Q2 guide implies GM −170 to −230bp with opex ratio −150 to −190bp** [C]. |
| Server life extended beyond 6 years | **Unverified.** |
| DSO toward 95d+ | Not triggered. |
| Renewed large bond issuance | **Not triggered.** Debt repaid; the buffer is being drawn down instead. |
| FY27 FCF "recovers" while operating leases balloon | FCF is **not** recovering. Operating leases are ballooning (+31% QoQ). **Watch both.** |

---

## 9. Guidance (from the Q1 FY27 call, 2026-10-28) [P, M3]

| Item | Q2 FY27 guide |
|---|---|
| Revenue | **$96.0–97.1B (+18–19%)** |
| Agents and Infra | $80.1–80.7B (+24–25%) |
| Devices and Consumer | $15.9–16.4B |
| Azure growth | **49–50% constant currency** |
| Microsoft Cloud gross margin | **~65%** |
| COGS | $32.7–32.9B (+26–27%) |
| Opex | $18.5–18.6B (+9%), including a voluntary-exit-offer estimate |
| Operating margin | **"down slightly year-over-year"** |
| Other income (ex-OpenAI) | ~−$300M |
| Effective tax rate | ~20% |
| Capex | **"over $50 billion"** |
| Calendar-2026 capex | **~$170B** (delays at third-party capacity providers) |
| FY27 | Management said only "we expect to continue to remain **free cash flow positive** in FY27". **No full-year operating-margin guide** was given in the call excerpts I obtained. |

The tension I recorded in August between two FY27 operating-margin statements was **not resolved**.
Neither statement was repeated in what I obtained.

---

## 10. What changed since the August report

| # | August | Now | Effect |
|---|---|---|---|
| **1** | FCF down two years; "watch for a third" | **The decline is accelerating:** Q1 −27.4%, TTM $60.0B, FCF/net income 0.42x, cash + STI −$37.5B YoY, payouts > SBC-adjusted FCF, management bar "FCF positive" | **Negative.** The central bear datapoint strengthened. |
| **2** | Disclosure downgrade: no AI split, no Copilot revenue | **Overhaul.** New A&I and D&C segments; **Azure in dollars ($33.2B)**; **OpenAI related-party revenue ($10.0B) and receivables ($7.2B)**; HLBV method; stake ~24%. Lost: Intelligent Cloud margin; Copilot seat count withheld. | Net **disclosure improvement**, which exposed a **new concentration** |
| **3** | Gross margin eroding, opex leverage carrying operating margin | **Guide now has operating margin down slightly YoY in Q2.** D&A +44%. ~75% of capex short-lived. | The "finite opex leverage" point is arriving |
| 4 | Azure +43% Q4 (old basis) | 42% recast Q4 → **48% Q1** → 49–50% guide | **Positive.** The bear trigger is further away. |
| 5 | Other income 36.9% of FY26 pre-tax growth | $38M in Q1; GAAP ≈ non-GAAP | Quieter; still 8.1% of TTM pre-tax |
| 6 | Uncommenced leases not obtained | **$329.1B** at 30 Jun 2026 [S] | Sizes the off-balance-sheet obligation for the first time |
| 7 | Server useful life unverified | Still unverified | — |
| **8** | **Score printed as 79** | **Its components (17+16+13+14+13+3−3) sum to 73.** The 79 was an addition error in my own report. | **Correction of record.** Any committee scorecard that used 79 should use 73. |

**On item 8:** the August text said "I considered 84… held at 79". The component table does not support
79. I cannot reconstruct which number was intended, so the arithmetic of the published components
governs. This update scores 70 on the same component framework, with each line explained.

---

## 11. Financial score: **70 / 100, grade B**

| Component | Weight | Aug (as scored) | **Now** | Rationale |
|---|---|---|---|---|
| Profitability and margin trend | 20 | 17 | **16** | Q1 operating margin 49.8% (+88bp) and TTM 47.1% are excellent. −1 because gross margin is down 126bp, Microsoft Cloud GM is guided to ~65%, and **Q2 operating margin is guided down YoY**. |
| Cash generation | 25 | 16 | **14** | OCF +28.7% with 1.37x conversion. −2 more: FCF decline accelerating (−27.4% Q1), TTM FCF/net income 0.42x, capex/OCF 69%, and management's own bar is now "positive". |
| Returns on capital | 15 | 13 | **13** | ROE 34.2%, ROIC ~26% [E]. Unchanged. |
| Balance sheet and debt | 15 | 14 | **13** | Still net cash ex-leases ($29.0B) with no refinancing risk. −1: the buffer halved YoY, payouts exceed SBC-adjusted FCF, operating leases are up 31% QoQ, and $329B of leases are uncommenced. |
| Earnings quality and accounting | 20 | 13 | **13** | Better: other income quiet, GAAP ≈ non-GAAP, AR clean. Worse: OpenAI is 10.8% of revenue as a related party, HLBV is opaque, restructuring is embedded in guidance, D&A +44%. Net unchanged. |
| Disclosure quality | 5 | 3 | **4** | Azure dollars and OpenAI revenue disclosed (+). Intelligent Cloud margin lost and Copilot seat count withheld (−). Net +1. |
| Data-completeness deduction | — | −3 | **−3** | 10-Q not opened (SEC blocked): finance leases at 30 Sep, server life, lease schedule and share count are still open. |
| **Total** | 100 | **73** (printed 79) | **70** | **B** |

Arithmetic check: 16 + 14 + 13 + 13 + 13 + 4 − 3 = 70.

**What would move this:**
- **Up to about 75:** Q2 FCF clearly positive with cash capex below about $45B, and Microsoft Cloud gross
  margin holding at 66% or better.
- **Down to 65 or below:** Q2 FCF negative; a server-life extension beyond 6 years; OpenAI receivables
  growing faster than OpenAI revenue for a second quarter; or bond issuance to fund buybacks.

---

## 12. Valuation inputs (for 𢦀鳩仔)

| Input | Value | Period / date | Source |
|---|---|---|---|
| Revenue | **$92,279M (+18.8%)** · TTM **$346,445M** | Q1 FY27 · to 30 Sep 2026 | [P, M1; C] |
| Revenue guide | $96.0–97.1B | Q2 FY27 | [P, M3] |
| Gross margin | **67.8%** Q1 · **67.7%** TTM | | [C from P] |
| Operating margin | **49.8%** Q1 · **47.1%** TTM | | [C from P] |
| GAAP diluted EPS | **$4.92** Q1 · **~$19.15** TTM | | [P; C] |
| Non-GAAP diluted EPS (ex-OpenAI) | **$4.89** Q1 · **~$18.04** TTM | | [P; C] |
| Operating cash flow, TTM | **$195,878M** | | [C from P] |
| Cash capex, TTM | **$135,921M** (Q1 incl. finance leases: $45.2B) | | [C from P; P, M3] |
| **FCF, TTM** | **$59,957M (17.3%)** | | [C from P] |
| SBC, TTM | $12,556M · FCF − SBC **$47,401M** | | [C from P] |
| Cash + short-term investments | **$64,509M** | 30 Sep 2026 | [P, M1] |
| Bond debt | **$35,481M** | 30 Sep 2026 | [C from P] |
| **Net cash ex-leases** | **$29,028M** | 30 Sep 2026 | [C] |
| Finance lease liabilities | $62,304M (**30 Jun 2026**; Sep not obtained) | | [S, Aug] |
| Net debt incl. finance leases | **~$33.3B** | 30 Sep 2026 (stale lease input) | [E] |
| Operating lease liabilities (LT) | $21,719M | 30 Sep 2026 | [P, M1] |
| Leases not yet commenced | **$329.1B** | 30 Jun 2026 | [S, M11] |
| Diluted weighted shares | **7,446M** (basic 7,426M) | Q1 FY27 | [P, M1] |
| Period-end shares outstanding | **not obtained** (10-Q cover blocked) | | — |
| Equity | $470,509M | 30 Sep 2026 | [P, M1] |
| TTM effective tax rate | 19.7%; Q2 guide ~20% | | [C; P] |
| Consensus, Q1 FY27 (pre-print) | EPS ~$4.71–4.73; revenue ~$90.7B; Azure $32.3–32.8B | Oct 2026 | [CONS, S, M14] |
| Consensus, Q2 FY27 | EPS $4.97; revenue $98.5B (**above the company guide of $96.0–97.1B, so treat with suspicion**) | Chartmill, ~Nov 2026 | [CONS, S, M14] |
| Consensus, FY27 | **EPS ~$19.5–20.4; revenue ~$383–391B.** Sources conflict: $19.53/$382.9B (51 analysts), $19.64/$390.7B (48), $20.39 (64; 2026-11-07), revenue $391B (Visible Alpha, 2026-08-06) | | [CONS, S, M14] |
| Consensus, FY28 | **not found** | | — |

**Cautions for valuation:**
1. **Use non-GAAP EPS or operating income.** GAAP includes HLBV-driven OpenAI marks: +$1.11/share TTM.
2. **Treat operating-lease payments as capex-equivalent.** Reported capex will understate the spend from
   FY27 onward, and $329B of uncommenced leases is the pipeline.
3. **Q2 FY27 FCF may be near zero** [E]. Do not annualise Q1's $18.6B.
4. **Do not use the August report's "~$144bn FY26 capex including finance leases".** It was an [E]
   built on quarterly finance-lease extractions, and the "$11.1bn Q1" input may have been calendar Q1
   2026 (fiscal Q3) rather than fiscal Q1. I could not re-verify this before the search budget ran out.
   The official FY26 figure including finance leases remains **not obtained**.

---

## 13. NOT OBTAINED register

1. **The Q1 FY27 10-Q** (`sec.gov` DNS-blocked): finance lease liabilities at 30 Sep 2026, lease
   maturity schedule, period-end share count, OpenAI note detail (carrying value; exact stake wording).
2. **Server and network equipment useful life** in the FY26 10-K. Still the highest-priority open item.
3. **The P&L effect of the 15→25-year building-life change** in Q1 FY27.
4. **Voluntary exit offer charge amount.**
5. **OpenAI revenue for Q1 FY26** (needed to size OpenAI's contribution to Azure acceleration), and
   the OpenAI share of RPO.
6. **The prior-year comparator for uncommenced leases** ($196.6B vs $92.7B; conflicting).
7. **The official FY26 capex-including-finance-leases total.**
8. **A full-year FY27 operating-margin guide**, if one exists.
9. **Copilot seats or revenue** (withheld by the company this quarter).
10. **Whether the Q4 FY26 $3.2B Anthropic gain sits inside non-GAAP.** Still inference only.
11. **FY28 consensus.**

---

## Sources

| Key | Document | Date | URL |
|---|---|---|---|
| M1 | **[P]** Microsoft FY27 Q1 press release, with income statement, balance sheet, cash flows, segments, revenue by offering, non-GAAP reconciliation | released 2026-10-28; period ended 2026-09-30 | [microsoft.com](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) |
| M2 | **[P]** FY27 Q1 metrics (recast KPI history) | 2026-10-28 | [microsoft.com](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/metrics) |
| M3 | **[P]** FY27 Q1 earnings call (CFO and CEO commentary, guidance) | 2026-10-28 | [microsoft.com](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1) |
| M4 | **[P]** FY26 Q1 press release (balance sheet at 30 Sep 2025) | period ended 2025-09-30 | [microsoft.com](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q1/press-release-webcast) |
| M5 | **[P]** FY26 Q2 press release | period ended 2025-12-31 | [microsoft.com](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q2/press-release-webcast) |
| M6 | **[P]** FY26 Q3 press release | period ended 2026-03-31 | [microsoft.com](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast) |
| Aug | August report (FY26 annual [P] from the FY26 Q4 release) | 2026-08-21 | `reports/equity/2026-08-21-msft-financials.md` · [FY26 Q4 release](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) |
| M8 | [S] Segment change announcement coverage | 2026-09-02/03 | [Northeast Times](https://northeasttimes.com/2026/09/03/microsoft-overhauls-financial-reporting-will-disclose-azure-revenue-each-quarter/) · [MediaPost](https://www.mediapost.com/publications/article/417648/microsoft-changes-reporting-structure-to-reflect-s.html) · [Windows Report](https://windowsreport.com/microsoft-is-reshaping-its-financial-reporting-as-ai-blurs-product-lines/) |
| M9 | [S] Recast FY26 segment figures and recast 8-K summary | 2026-09/10 | [remio.ai](https://www.remio.ai/post/microsoft-recasts-fy27-around-ai-but-its-two-segments-tell-different-stories) · [Autobound 8-K summary](https://www.autobound.ai/companies/microsoft/8-k/microsoft-reorganized-financial-segments-into-agents-a47d05bb) |
| M10 | [S] Q1 FY27 10-Q OpenAI disclosures (revenue, receivables, HLBV, stake, funding) | 2026-10-28/29 | [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526436133/msft-20260930.htm) (blocked) · [MediaPost](https://www.mediapost.com/publications/article/419080/microsoft-generated-10b-in-revenue-from-openai.html) · [24/7 Wall St](https://247wallst.com/investing/2026/10/29/openai-now-makes-up-11-of-microsofts-revenue/) · [FinanceFeeds](https://financefeeds.com/microsoft-banks-10-billion-from-openai/) · [The Next Web](https://thenextweb.com/news/microsoft-openai-revenue-10bn-quarter) |
| M11 | [S] FY26 10-K: leases not yet commenced, $329.1B | 2026-07-29/31 | [BTW Media](https://btw.media/en/microsoft-329-1bn-uncommenced-datacentre-leases) · [The Star](https://www.thestar.com.my/business/business-news/2026/07/31/microsoft-sees-strong-cash-flow-lower-capex) |
| M12 | [S] Q1 FY27 capex incl. finance leases (cross-check of M3) | 2026-10-29 | [Zacks](https://www.zacks.com/stock/news/3018768/microsoft-q1-earnings-beat-estimates-as-cloud-accelerates) |
| M13 | [S] Voluntary exit offer (AP) | 2026-10-26 | [ABC7/AP](https://abc7news.com/19981967/) |
| M14 | [CONS, S] Consensus | Oct–Nov 2026; Aug 2026 | [Zacks](https://www.zacks.com/stock/news/3018768/microsoft-q1-earnings-beat-estimates-as-cloud-accelerates) · [SiliconANGLE](https://siliconangle.com/?p=852356) · [Reuters via Digg](https://digg.com/tech/mon7nzhs) · [Chartmill](https://www.chartmill.com/stock/quote/MSF.DE/estimates) · [Simply Wall St](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-corporation-just-beat-analyst-forecasts-and-analys) · [S&P Global / Visible Alpha](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/microsoft-postq-azure-usd100b-milestone-as-ai-demand-lifts-earnings-and-outlook) |
| M15 | [S] Useful-life change (15→25 years) | 2026-07-29/30 | [CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/) · [PYMNTS](https://www.pymnts.com/earnings/2026/microsoft-extends-data-center-lifespans-to-soften-ai-buildout-costs/) |
| M16 | [S] FY26 gross servers, networking and software ($215.87B vs $132.84B); attribution to a specific outlet uncertain | 2026-07/08 | [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/microsoft-brought-88-data-centers-online-in-fy2026/) |

**Not used:** `tradingkey.com` (firm blacklist). **DNS-blocked this session:** `www.sec.gov`.

---

*Research only. It contains no recommendation, target price or position sizing. The Committee and the
Owner decide. Historical financial statements do not predict future results.*
