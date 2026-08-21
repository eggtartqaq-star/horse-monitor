# MSFT — Microsoft Corporation | Financial Statement Analysis

**Analyst:** 巴爺爺, Financial Statement Analyst (Dept 2 — Equity Research)
**Date:** 2026-08-21
**Ticker:** MSFT (NASDAQ) · **Owner position:** none · **Watchlist sleeve:** `ai:`
**Prior firm coverage:** none — this is the firm's first MSFT report.

> **STATUS: DRAFT v2 — core statements complete, some notes still open. See §12.**

---

## 0. Sourcing caveat (read first)

**Partial success against the egress policy — better than briefed.** The brief warned to
expect that *no* primary filing would be readable. That was too pessimistic:
**`www.microsoft.com/en-us/investor/...` is accessible**, and Microsoft publishes the full
condensed income statement, balance sheet, cash-flow statement and segment tables on its
own IR pages. The FY2026, FY2024 and FY2023 statement lines below were **read off pages I
actually opened**.

| Host | Result |
|---|---|
| `www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast` | **ACCESSIBLE — opened.** Full FY26/FY25 income statement, balance sheet, cash flow, segments. |
| `www.microsoft.com/en-us/investor/earnings/fy-2024-q4/cash-flows` | **ACCESSIBLE — opened.** FY24/FY23 cash flow statement. |
| `www.microsoft.com/investor/reports/ar25/` | **ACCESSIBLE — opened.** FY25/FY24 income statement + segment operating income; no cash-flow or debt-note detail returned. |
| `www.microsoft.com/investor/reports/ar26/index.html` | **HTTP 404.** FY2026 Annual Report not at guessed URL. |
| `.../fy-2026-q4/cash-flows`, `.../performance`, `.../segment-revenues`, `.../irfinancialstatementspopups` | **HTTP 404.** Sub-pages not published for Q4 under these paths. |
| `www.sec.gov` | **EGRESS_BLOCKED** (proxy). Confirmed once, not retried. **No 10-K or 10-Q opened.** |
| `microsoft.gcs-web.com` | **EGRESS_BLOCKED.** |
| `deepquarry.substack.com`, `www.fool.com`, `news.alphastreet.com`, `www.cnbc.com` | **EGRESS_BLOCKED.** |
| `finance.yahoo.com`, `stockanalysis.com`, `businesswire.com` | Blocked in prior sessions; not retried. |
| `tradingkey.com` | Firm-wide blacklist. Appeared in search results; **not used, not cited.** |

**Figure-provenance convention — used on every number in this report:**

- **[P]** = *Primary, document opened.* Read off a `microsoft.com` IR page I fetched.
- **[S]** = *Search extraction.* Returned by WebSearch summarising a page I could **not**
  open. One confidence notch lower — I could not see the surrounding table or footnote.
- **[C]** = *Calculated by me* from [P] inputs. Arithmetic mine, inputs cited.
- **[E]** = *Estimate / inference.* Assumption stated explicitly.

**What this means in practice:** the three statements are solid **[P]**. The **notes** are
not. The useful-life accounting policy text, the debt maturity ladder, the OpenAI equity-
method note and the lease footnote are all **[S]** — reconstructed from transcript
summaries and third-party databases. **Those are exactly the areas where the bear case
lives.** Weight accordingly and see §12.

**Staleness:** FY2026 ended **2026-06-30**; results released **2026-07-29**. Today is
2026-08-21 — data is **~7 weeks past period end, ~3 weeks past release**. Fresh. The
FY2026 **10-K** could not be confirmed as filed or read (SEC blocked); all note-level
detail is unconfirmed against the filed document.

---

## 1. Summary & Grade

### **Grade: A− · Score: 79 / 100**

House calibration: 0100.HK **D+ 48/100**; 6160.HK **A− 82/100** (strongest graded to
date). MSFT lands **just below 6160.HK** — a genuinely excellent set of financial
statements, marked down for reasons that are specific, quantified, and not generic
mega-cap grumbling.

**The operating year was outstanding.** Revenue $331,839m (+17.8%), gross margin
$225,465m, operating income $155,237m (+20.8%), operating margin up **116bp to 46.8%** —
margin *expansion* in the teeth of the largest capex programme in corporate history.
Operating cash flow up **34.3% to $182,935m**. **[P]**

**Three things stop this being an A.**

1. **Free cash flow has now fallen two years running.** FY2024 $74,071m → FY2025 $71,611m
   → FY2026 $66,987m **[C from P]**. That is **−9.6% from the FY2024 peak** while revenue
   rose 35% over the same span. Capex absorbed **63.4%** of operating cash flow in FY2026,
   up from 37.5% in FY2024 **[C]**. This is the number the committee should hold onto.
2. **26.9% of FY2026 EPS growth was a mark, not a business.** Net gains on the OpenAI
   investment added $4,963m / **$0.67** to FY2026; the same line was a **$3,620m / $0.49
   drag** in FY2025 **[P / S]**. The $1.16 swing is **26.9% of the $4.31 of EPS growth**
   **[C]**. Microsoft excludes OpenAI from non-GAAP — correctly — but see §9 for the
   Anthropic gain it apparently does **not** exclude.
3. **The estimate lever has now been pulled a second time.** Effective **FY2027**,
   Microsoft extended the useful life of **data centres and office buildings from 15 to 25
   years**, and is shifting future data-centre leases from finance leases (inside capex,
   fast depreciation) to operating leases (outside capex) **[S]**. This follows the 2022
   extension of server/network equipment from 4 to 6 years **[S]**. §2.2.

**The single best thing I found**, and it cuts hard against the bear case: **Intelligent
Cloud revenue +29.7% for the year with Azure accelerating to +43% in Q4** **[P/S]**, and
**operating margin expanding at the company level despite D&A rising 30.9%** **[P]**. The
"decelerating AI revenue meets depreciation wave" thesis requires deceleration. **In
FY2026 it did not happen — Azure accelerated.** I could not find the deceleration the bear
case needs. That is why this is an A−, not a B.

**Three numbers that matter most:**

| # | Number | Value | Why |
|---|---|---|---|
| 1 | **Free cash flow, FY2026** | **$66,987m, −6.5% YoY, second consecutive decline** **[C from P]** | The whole thesis. If FY2027 FCF falls again on ~$175bn CY26 capex, the compounding story pauses. |
| 2 | **Capex as % of operating cash flow** | **63.4%** (FY24: 37.5%) **[C from P]** | Measures how much of the machine is being reinvested rather than returned. It has nearly doubled in two years. |
| 3 | **Depreciation & amortisation growth vs revenue growth** | **+30.9% vs +17.8%** **[C from P]** | The depreciation tail is already arriving and is outrunning revenue. FY2027 is when the FY26 $115.9bn cohort starts depreciating in full. |

---

## 2. The AI capex cycle and its depreciation tail

This is the central financial question and it gets the most space.

### 2.1 Capex, FY2023 → FY2026

**Cash "additions to property and equipment"** (the cash-flow-statement line; this
**excludes** finance leases):

| FY | Additions to PP&E | YoY | Revenue | Capex / revenue | Op. cash flow | Capex / OCF |
|---|---|---|---|---|---|---|
| FY2023 | **$28,107m** **[P]** | — | $211,915m **[S]** | 13.3% **[C]** | $87,582m **[P]** | 32.1% **[C]** |
| FY2024 | **$44,477m** **[P]** | +58.2% | $245,122m **[S]** | 18.1% **[C]** | $118,548m **[P]** | 37.5% **[C]** |
| FY2025 | **$64,551m** **[P]** | +45.1% | $281,724m **[P]** | 22.9% **[C]** | $136,162m **[P]** | 47.4% **[C]** |
| FY2026 | **$115,948m** **[P]** | **+79.6%** | $331,839m **[P]** | **34.9%** **[C]** | $182,935m **[P]** | **63.4%** **[C]** |

FY2023 and FY2024 revenue are **[S]** — I did not open a page showing them; FY2025 and
FY2026 revenue are **[P]**. The capex and OCF figures are all **[P]**.

**Read this table slowly.** In three years capex went from consuming one-third of
operating cash flow to consuming **nearly two-thirds**. Capex intensity relative to revenue
has **2.6x'd**. This is not a mature software company's cash flow profile any more; it is
closer to a utility or a semiconductor fab, wrapped around a software P&L.

### 2.2 Capex **including finance leases** — and why the definition just changed

Microsoft's headline "capital expenditures including finance leases" is larger than the
cash line because finance leases are non-cash additions.

- Q4 FY2026 capex including finance leases: **~$41bn**, +69% YoY **[S]**, of which cash
  paid for PP&E was **~$35.8bn** **[S]** — implying **~$5.6bn** of Q4 finance leases **[C]**.
- Quarterly finance leases FY2026 as extracted: Q1 **$11.1bn**, Q2 **$6.7bn**,
  Q3 **$4.7bn**, Q4 **$5.6bn** — **~$28.1bn** for the year **[S]**.
- **Therefore FY2026 capex including finance leases ≈ $144bn** **[E]**, against $115.9bn
  on the cash line **[P]**. **I flag this as an estimate**, not a disclosure: I could not
  open a document stating the FY2026 including-leases total, and the four quarterly
  figures are search extractions. **Do not quote $144bn as a company figure.**
- Balance-sheet corroboration: **finance lease liabilities reached $62,304m at
  2026-06-30**, up from $11,750m in 2021 **[S]**. The liability side is consistent with
  very large lease-funded capacity additions.

**The change that matters.** On the Q4 FY2026 call, management stated **[S]**:

- Effective at the start of **FY2027**, the estimated useful life of **data centres and
  office buildings is extended from 15 years to 25 years**.
- More future data-centre leases will shift from **finance leases (counted in capex)** to
  **operating leases (not counted in capex)**.
- The combined effect **restates the calendar-2026 capex expectation to ~$175bn**, down
  from a ~$190bn figure circulating pre-print **[S]**, *with underlying investment plans
  unchanged*.
- Management's characterisation: the change "only affects the timing of future
  depreciation, with a **minimal benefit to FY27 operating income**" **[S]**.

**My assessment, stated plainly.** Three separate things happened at once, and they are
not equivalent:

| Change | Effect on P&L | Effect on reported capex | My read |
|---|---|---|---|
| Buildings/DC life 15y → 25y | **Lowers** future depreciation per year on that asset class | none | Real earnings tailwind, size undisclosed |
| Finance → operating lease shift | Moves cost from D&A + interest into **operating expense**; roughly cost-neutral over life | **Lowers reported capex** | **Optical.** Capex looks smaller; the obligation does not shrink |
| Combined guidance restatement to ~$175bn | — | −$15bn vs prior expectation | **The $15bn "reduction" is definitional, not a spending cut** |

**This is the most important single paragraph in the report.** A reader who sees "Microsoft
cut CY2026 capex guidance from $190bn to $175bn" and infers spending discipline has been
misled. Management said explicitly that **underlying investment plans are unchanged**
**[S]**. The capex line got smaller because the accounting definition changed. Any
committee member modelling capex-to-FCF must model the **operating lease payments** that
now sit outside capex — and I **could not obtain** the operating lease commitment schedule
(§12). **This is the largest unquantified item in the report.**

On the buildings life extension itself: **25 years for a data centre shell is not
aggressive on its face** — the shell genuinely outlives the servers inside it, and 25–40
years is common in REIT and utility practice. My objection is not to the assumption; it is
to **the pattern and the timing**. Microsoft extended server life in 2022 (4y → 6y, a
+$3.3bn FY2023 operating-income benefit was anticipated **[S]**, with a ~$1.1bn benefit in
the first quarter after the change **[S]**). It has now extended building life in 2026.
Both changes were **earnings-favourable**, and both landed in years when the depreciation
line was accelerating. That is a pattern the committee should hold in mind even though
each individual change is defensible.

### 2.3 Has the **server** useful life been revised again? — **NOT ESTABLISHED**

The brief asks specifically whether the 2022 server extension has since been revised. **I
could not resolve this.** What I have:

- The 2022 change (server and network equipment **4 → 6 years**) is well documented **[S]**.
- The FY2027 change is described in every source as covering **data centres and office
  buildings**, i.e. **shells, not servers** **[S]**.
- I found **no** source stating the server/network life has been shortened, lengthened, or
  reaffirmed in FY2026.

**Therefore my working assumption is that server and network equipment remains at 6 years
**[E]**, and I mark this UNVERIFIED.** It requires the FY2026 10-K Property and Equipment
note, which is behind the SEC block. **This is the highest-priority open item (§12).** It
matters because a *shortening* of GPU life toward 4–5 years — which several peers have
been pressured on — would be a large negative EPS event, and a *further lengthening* would
be a significant quality red flag.

### 2.4 The depreciation tail, quantified as far as I can

| FY | D&A and other (cash-flow addback) | YoY | Revenue YoY | D&A as % of revenue |
|---|---|---|---|---|
| FY2023 | **$13,861m** **[P]** | — | — | 6.5% **[C]** |
| FY2024 | **$22,287m** **[P]** | **+60.8%** | +15.7% | 9.1% **[C]** |
| FY2025 | **$29,433m** **[P]** | +32.1% | +15.0% | 10.4% **[C]** |
| FY2026 | **$38,534m** **[P]** | **+30.9%** | +17.8% | 11.6% **[C]** |

Caveat: this line is "**Depreciation, amortization, and other**" — it is **not** pure
depreciation and includes other non-cash items. It is the best proxy available without the
10-K note. **[P] for the values, [E] for treating it as a depreciation proxy.**

**What the trend shows:** D&A has grown faster than revenue in **every one of the last
three years**, and has risen from 6.5% to 11.6% of revenue — a **510bp** structural drag
absorbed while operating margin still *expanded*. That is a genuinely impressive result and
the strongest single argument against the bear case so far.

**But the tail is in front of us, not behind us.** The $115.9bn spent in FY2026 was spent
*through* the year and much of it is not yet in service or is only partially depreciated.
A crude sense of scale: at a 6-year life, a $115.9bn cohort carries **~$19.3bn of annual
depreciation at full run-rate** **[C, illustrative]**. Against FY2026 operating income of
$155.2bn that is **~12.4%** — i.e. roughly **$2.09 of pre-tax EPS**, or **~$1.68 after tax
at the FY26 19.4% rate** **[C, illustrative]**. Microsoft must grow operating profit by
about that much *just to stand still* on the FY26 cohort alone, before the FY2027 cohort.

**I want to be explicit that the above is an illustration, not a forecast.** It assumes the
entire cash capex is 6-year-life equipment, which is wrong — a meaningful share is land and
shells on 25-year lives, which depreciate far more slowly. The true figure is **lower**,
probably materially. Without the 10-K PP&E-by-class table I cannot narrow it. **Marked [E]
and flagged in §12.** I would rather give the committee an honest range than a false
precision.

### 2.5 Verdict on the depreciation-wave bear case

**Partially supported. Not yet vindicated.**

- ✅ **Supported:** capex intensity has 2.6x'd; D&A is compounding at ~31% and outrunning
  revenue; FCF has fallen two years running; the accounting definition of capex was just
  changed in an earnings-favourable direction.
- ❌ **Not supported:** the bear case requires **decelerating AI revenue**. FY2026 delivered
  the opposite — Azure **accelerated** to +43% in Q4 from +40% in Q3 **[S]**, Intelligent
  Cloud revenue +29.7% for the year **[P]**, and company operating margin **expanded**
  116bp **[C from P]**. Revenue is currently absorbing the depreciation comfortably.
- ⚠️ **The real risk is timing, not direction.** Depreciation is contractual and certain;
  Azure growth is not. The bear case does not need Azure to shrink — it only needs Azure to
  decelerate to, say, the mid-20s while D&A keeps compounding at 30%. **FY2027 is the year
  that gets tested.**

---

## 3. Free cash flow after all of that

### 3.1 The FCF bridge, FY2023 → FY2026

| FY | Operating cash flow | Additions to PP&E | **FCF (OCF − capex)** | FCF YoY | FCF margin |
|---|---|---|---|---|---|
| FY2023 | $87,582m **[P]** | $(28,107)m **[P]** | **$59,475m** **[C]** | — | 28.1% **[C]** |
| FY2024 | $118,548m **[P]** | $(44,477)m **[P]** | **$74,071m** **[C]** | **+24.5%** | 30.2% **[C]** |
| FY2025 | $136,162m **[P]** | $(64,551)m **[P]** | **$71,611m** **[C]** | **−3.3%** | 25.4% **[C]** |
| FY2026 | $182,935m **[P]** | $(115,948)m **[P]** | **$66,987m** **[C]** | **−6.5%** | **20.2%** **[C]** |

**Answer to the brief's question, unambiguously: FCF is falling, not flat.** It peaked in
FY2024 and has declined in each of the two years since — **−9.6% cumulative from peak**
while revenue grew **+35.4%** over the same period **[C]**. FCF margin has compressed from
30.2% to **20.2%**, a **1,000bp** collapse in two years.

**This is the correct lens and it is why the house rule "cash flow over reported earnings"
matters here.** Reported GAAP EPS grew **+31.6%** in FY2026. Free cash flow **fell 6.5%**.
The two statements are both true and they point in opposite directions. **The committee
should anchor on the second.**

**Two important mitigations, stated fairly:**

1. **FCF here is measured after 100% of growth capex.** Microsoft is not spending $115.9bn
   on maintenance — the overwhelming majority is capacity expansion against contracted
   demand. A company that voluntarily cuts capex to zero would show enormous FCF and no
   future. Declining FCF driven by *discretionary growth investment* is categorically
   different from declining FCF driven by deteriorating operations. **Operating cash flow
   grew 34.3%** — the operating engine is not the problem.
2. **The FY2027 lease reclassification will make FCF look artificially better**, because
   operating-lease payments hit operating cash flow (reducing OCF) but the associated
   capacity no longer appears in capex. Net effect on FCF is roughly neutral-to-positive
   optically while the economic obligation is unchanged. **Watch for an FY2027 "FCF
   recovery" that is definitional.** **[E — my inference from the disclosed mechanics.]**

### 3.2 Stock-based compensation: is FCF flattered? **Yes — by ~$12.4bn.**

| FY | SBC | YoY | % of revenue | % of FCF |
|---|---|---|---|---|
| FY2023 | $9,611m **[P]** | — | 4.5% **[C]** | 16.2% **[C]** |
| FY2024 | $10,734m **[P]** | +11.7% | 4.4% **[C]** | 14.5% **[C]** |
| FY2025 | $11,974m **[P]** | +11.6% | 4.3% **[C]** | 16.7% **[C]** |
| FY2026 | $12,405m **[P]** | **+3.6%** | **3.7%** **[C]** | **18.5%** **[C]** |

**Plainly: yes, FCF is flattered by excluding SBC.** SBC is a non-cash addback inside
operating cash flow, so the $66,987m FCF figure includes $12,405m of compensation paid in
stock. **FCF net of SBC = $54,582m** **[C]** — 18.5% lower, and an FCF margin of **16.4%**
rather than 20.2%.

**However, and this is a genuine positive I want stated at full strength:** SBC grew only
**+3.6%** in FY2026 against **+17.8%** revenue growth, and has fallen from 4.5% to **3.7%**
of revenue since FY2023 **[C from P]**. Microsoft is one of very few large-cap technology
companies where SBC intensity is *declining* while headcount-adjacent AI competition is at
its most intense. On this specific metric Microsoft is materially better-behaved than the
mega-cap peer set. **The SBC-net-of-buyback picture in §8 is less flattering.**

---

## 4. Segment detail

### 4.1 Full-year segments, FY2026 vs FY2025 **[P]**

| Segment | Revenue FY26 | Revenue FY25 | YoY | Op. income FY26 | Op. income FY25 | **Op. margin FY26** | **Op. margin FY25** | Δ |
|---|---|---|---|---|---|---|---|---|
| Productivity & Business Processes | $139,996m | $120,810m | **+15.9%** | $83,879m | $69,773m | **59.9%** | 57.8% | **+215bp** |
| Intelligent Cloud | $137,791m | $106,265m | **+29.7%** | $56,972m | $44,589m | **41.3%** | 42.0% | **−62bp** |
| More Personal Computing | $54,052m | $54,649m | **−1.1%** | $14,386m | $14,166m | **26.6%** | 25.9% | **+69bp** |
| **Total** | **$331,839m** | **$281,724m** | **+17.8%** | **$155,237m** | **$128,528m** | **46.8%** | **45.6%** | **+116bp** |

Revenue and operating income **[P]**; margins and deltas **[C]**.

**Three observations the headline misses:**

1. **Intelligent Cloud is the only segment whose margin went backwards.** Down 62bp to
   41.3% **[C]**. This is exactly where the AI infrastructure depreciation lands, and it is
   the first visible margin evidence of the capex cycle biting. It is a *small* decline —
   but it is the leading indicator to track, and it is going the wrong way while the other
   two segments expand.
2. **Company-level margin expansion is being carried by Productivity & Business
   Processes**, +215bp to a remarkable **59.9%** **[C]**. M365 price/mix and Copilot
   attach are doing the heavy lifting that lets the consolidated margin rise while cloud
   margin falls. **The consolidated margin story is healthier than the cloud margin story.**
3. **More Personal Computing shrank** (−1.1% for the year, **−4% in Q4** **[P/S]**).
   Windows, devices and gaming are in structural decline. At $54bn it is 16% of revenue
   and no longer a growth contributor. This is well understood but should not be ignored.

### 4.2 Q4 FY2026 segments **[P/S]**

| Segment | Q4 revenue | YoY | Q4 op. income | Q4 op. margin |
|---|---|---|---|---|
| Productivity & Business Processes | $37.8bn | +14% | $21.9bn | 57.9% **[C]** |
| Intelligent Cloud | $39.3bn | **+32%** | $15.9bn | 40.5% **[C]** |
| More Personal Computing | $12.9bn | **−4%** | $2.7bn | 20.9% **[C]** |
| **Total** | **$90.0bn** | **+18%** | **$40.6bn** | **45.1%** **[C]** |

**Note the gap between Azure (+43%) and Intelligent Cloud (+32%)** — the non-Azure parts of
Intelligent Cloud (server products, Enterprise & Partner Services) are growing far more
slowly, or shrinking. Azure is doing essentially all the work in that segment.

### 4.3 Azure and the AI attribution — **the disclosure has been withdrawn**

What is disclosed **[P/S]**:

- **Azure and other cloud services revenue surpassed $100bn for the first time in FY2026**,
  the first time Microsoft has given an absolute Azure revenue figure at that granularity.
- Azure grew **+43% in Q4 FY2026**, an **acceleration** from +40% in Q3 **[S]**.
- Azure grew **~+41% for the full fiscal year** **[S]**.
- FY2025 comparison: Azure surpassed **$75bn**, up **34%** **[S]**.

**What the brief asked for — "how much of Azure growth management attributes to AI
services" — is no longer disclosed, and this is a disclosure-quality downgrade.**

In prior years Microsoft quantified AI's contribution to Azure growth in points (e.g. "AI
services contributed X points of growth"). **I could not find that split for any quarter of
FY2026.** What management offered instead on the Q4 call **[S]**:

- Acceleration attributed to **"efficiency gains across CPU and GPU fleet"**, reduced lead
  time to bring capacity online, and monetising those gains within the quarter.
- **Stronger-than-expected GitHub Copilot consumption** following a business-model change.
- **"Nearly 90% of Microsoft Cloud revenue now comes from customers outside the frontier AI
  labs"** — CFO Amy Hood **[S]**.

That last statistic is being used as a *reassurance* (concentration in AI labs is low), and
it is genuinely reassuring on counterparty risk. But note what it is **not**: it is not an
AI-revenue attribution. **A qualitative narrative has replaced a quantitative disclosure.**

One quantified AI metric did surface: an **AI annual revenue run-rate of $37bn as of Q3
FY2026, +123% YoY** **[S]**. I treat this cautiously — it is a search extraction, I could
not see its definition, and "run-rate" metrics are not audited revenue. **Do not put this
in a model without verification.**

**My read:** withdrawing the AI-contribution split at the exact moment the market most
wants it is a **minor negative mark on disclosure quality**, not evidence of concealment.
The most likely benign explanation is that AI and non-AI workloads have become genuinely
inseparable at the infrastructure level. But the committee is entitled to note that the
company stopped publishing the number that would settle the argument.

### 4.4 Copilot: **seat counts and anecdotes. No disclosed revenue.**

The brief asks me to be precise about this difference, so:

**Disclosed [P/S]:**
- **Microsoft 365 Copilot exceeded 30 million paid seats** as of Q4 FY2026, up from
  ~20 million in April 2026 — a 50% increase in one quarter **[S]**.
- GitHub Copilot consumption ran ahead of expectation after a business-model change **[S]**.

**NOT disclosed:**
- **There is no disclosed Copilot revenue line.** None. Not in the press release, not in
  the segment tables, not as a supplemental metric.
- No Copilot ARR, no Copilot gross margin, no Copilot churn or seat-retention rate.
- No disclosed **realised** price per seat.

**Third-party inference to reject:** one search result asserted "30 million paid seats
suggest a **$10 billion annual run rate**" **[S]**. **I will not carry that number.** It
is an outside calculation, apparently list-price × seats. Enterprise Copilot is sold with
E3/E5 bundling, multi-year ramps, and heavy volume discounting; list price is close to
worthless as a revenue proxy. **Marked as an outside estimate, explicitly not adopted.**
A recent report in this firm had to retract an inference built on an assumed input; I am
not repeating that.

**What we can say honestly:** Copilot seat growth is real, fast, and large in absolute
terms. Its revenue contribution is **unquantified by the company and unquantifiable by me**.
The PBP segment's +215bp margin expansion and +15.9% revenue growth **[C from P]** is the
only hard evidence that Copilot monetisation is working — and it is indirect. One
independent write-up characterised the quarter as a **"modest M365 AI revenue harvest"**
**[S, headline only — article not opened]**, which is a fair reflection of the gap between
seat-count enthusiasm and disclosed revenue.

---

## 5. The OpenAI relationship as a financial item

### 5.1 What it did to the P&L — a $8.6bn two-year swing

| FY | Impact on net income | Impact on diluted EPS |
|---|---|---|
| FY2025 | **−$3,620m** (net **losses**) **[S]** | **−$0.49** **[S]** |
| FY2026 | **+$4,963m** (net **gains**) **[P]** | **+$0.67** **[P]** |
| **Swing** | **+$8,583m** **[C]** | **+$1.16** **[C]** |

**Against total FY2026 EPS growth of $4.31** ($17.95 vs $13.64 **[P]**), the OpenAI swing
is **26.9% of the growth** **[C]**. Slightly more than a quarter of Microsoft's headline
EPS growth in FY2026 came from a change in the accounting mark on a private company.

**To Microsoft's credit, it excludes this from non-GAAP.** Non-GAAP FY2026 EPS is
**$17.28** (+22%) **[P]**, which is exactly $17.95 − $0.67 **[C]** — confirming the OpenAI
item is the non-GAAP adjustment. FY2025 non-GAAP equivalent is $13.64 + $0.49 = **$14.13**
**[C]**, giving **+22.3%** growth **[C]**, matching the disclosed +22%. **The non-GAAP
presentation on this item is clean and I have no complaint about it.** That is worth
saying, because it is the opposite of the usual adjusted-earnings abuse.

**Where "other income" sits:** Other income (expense), net was **+$10,697m in FY2026**
versus **−$4,901m in FY2025** **[P]** — a **$15,598m swing** **[C]**. That is far larger
than the OpenAI item alone and is discussed in §9; it is the single biggest quality issue
in the FY2026 income statement.

**Disclosure friction, noted:** third-party reporting states Microsoft has disclosed a
**~$4.7bn "other, net" expense line with no itemised breakdown**, the bulk of which
reflects "net recognized losses on equity method investments" **[S]**, and that in Q1
FY2026 Microsoft's share implied an **~$11.5bn quarterly OpenAI loss** presented inside an
aggregated line **[S, headline-level]**. I could not verify either against the filing. What
I can say with confidence is that **the OpenAI economics are visible only in aggregate,
not as a standalone disclosed line**, which makes the item hard to model. **[S]**

### 5.2 The equity stake, funding commitment and off-balance-sheet exposure

From the October 2025 restructuring **[S]**:

- OpenAI completed its conversion to a for-profit **OpenAI Group PBC**.
- Microsoft holds **~27% on an as-converted basis**, accounted for under the **equity
  method** — down from ~32.5% pre-restructuring, but on a stake reported at roughly
  **$135bn** of value against a cumulative investment of ~**$13.8bn** **[S]**.
- **Total funding commitment $13bn**, of which **$11.8bn funded as of 2026-03-31** **[S]**
  — i.e. **~$1.2bn remaining** committed but unfunded at that date. **[C]**
- OpenAI contracted to purchase an **incremental $250bn of Azure services** **[S]**.
- Microsoft **lost its right of first refusal** to be OpenAI's compute provider **[S]**.
- Microsoft's IP rights to models and products **extended through 2032**, now including
  post-AGI models, with any AGI declaration verified by an **independent expert panel**
  **[S]**.
- The **20% revenue share continues through 2030, subject to a cap** **[S]**. A further
  April 2026 revision reportedly **capped the revenue-share payments** — I could **not**
  open the source (CNBC blocked) and **the cap amount is NOT OBTAINED**. **[S, incomplete]**

### 5.3 What it costs the P&L, what is off balance sheet — my assessment

**On balance sheet / in the P&L:**
- Equity-method share of OpenAI results, running through "other income (expense), net" —
  **−$3,620m FY2025, +$4,963m FY2026 at the net income level** **[P/S]**. Volatile, non-cash,
  non-operating, and **unforecastable**.
- Remaining unfunded commitment **~$1.2bn** at 2026-03-31 **[C from S]** — trivially small
  against $182.9bn of operating cash flow. **The funding commitment is not a balance-sheet
  risk.**

**Off balance sheet — and this is the part that matters:**
- The **$250bn Azure purchase commitment** is a *customer* commitment **to** Microsoft, not
  an obligation **of** Microsoft. It is revenue backlog, not a liability. **But it is also
  a concentration**: a single counterparty, itself deeply lossmaking, contracted for an
  amount equal to **~75% of Microsoft's entire FY2026 revenue**, spread over years.
  Amy Hood's "nearly 90% of Microsoft Cloud revenue is from outside the frontier AI labs"
  **[S]** is precisely the rebuttal, and it is a good one.
- **The genuine asymmetry:** Microsoft is building physical, depreciating, 6-to-25-year
  assets partly against demand from a company whose own solvency depends on continued
  private fundraising. If OpenAI's funding environment tightens, Microsoft keeps the
  depreciation and loses the revenue. **That is the real OpenAI financial risk — not the
  equity method line, and not the $13bn commitment.**

**Net:** I judge the OpenAI relationship, as a *financial statement* item, to be
**earnings-quality-negative and risk-neutral-to-positive**. It injects large unforecastable
swings into EPS (bad for statement quality) while the actual capital at risk is small and
the commercial upside is contractually large.

---

## 6. Profitability — margins, ROE, ROIC

### 6.1 Margin trend **[P for FY25/26 inputs; C for ratios]**

| | FY2025 | FY2026 | Δ |
|---|---|---|---|
| Revenue | $281,724m | $331,839m | +17.8% |
| Gross margin $ | $193,893m | $225,465m | +16.3% |
| **Gross margin %** | **68.8%** | **67.9%** | **−88bp** |
| R&D | $32,488m (11.5%) | $35,562m (10.7%) | −78bp of revenue |
| Sales & marketing | $25,654m (9.1%) | $26,710m (8.0%) | −105bp |
| G&A | $7,223m (2.6%) | $7,956m (2.4%) | −16bp |
| Operating income | $128,528m | $155,237m | +20.8% |
| **Operating margin %** | **45.6%** | **46.8%** | **+116bp** |
| Effective tax rate | 17.6% **[C]** | **19.4%** **[C]** | **+177bp** |
| Net margin | 36.1% **[C]** | 40.3% **[C]** | +418bp |

**The key structural fact: gross margin is falling, operating margin is rising.**

- **Gross margin down 88bp** to 67.9%. Cost of revenue grew **+21.1%** vs revenue +17.8%
  **[C]** — driven by AI infrastructure depreciation and power, partly offset by fleet
  efficiency. Management confirmed Microsoft Cloud gross margin fell to **66%** in Q3
  FY2026 on AI infrastructure investment **[S]**, and company gross margin was **69%** in
  Q1 FY2026, down YoY **[S]**.
- **Operating margin up 116bp anyway**, because **every single opex line grew slower than
  revenue** — R&D +9.5%, S&M +4.1%, G&A +10.1% versus revenue +17.8% **[C]**. Operating
  expense discipline is *funding* the gross margin erosion.

**This is the most important profitability insight in the report.** Microsoft is paying for
the AI capex cycle out of **operating leverage on SG&A and R&D**, not out of pricing. That
works, and it worked well in FY2026. But **it is a finite resource**: you can only take
opex from 23.2% to 21.1% of revenue so many times. Once opex leverage is exhausted, gross
margin erosion flows straight to operating margin. **Watch the gross margin line, not the
operating margin line.**

**Net margin +418bp to 40.3%** overstates the improvement — a large part is the "other
income" swing (§9), not operations.

### 6.2 ROE

| | FY2025 | FY2026 |
|---|---|---|
| Net income | $101,832m **[P]** | $133,749m **[P]** |
| Total stockholders' equity (period end) | $343,479m **[P]** | $442,387m **[P]** |
| **ROE (ending equity)** | **29.6%** **[C]** | **30.2%** **[C]** |
| **ROE (average equity)** | n/a — FY2024 equity NOT OBTAINED | **34.0%** **[C]** |

Average-equity ROE for FY2026 uses average of $343,479m and $442,387m = $392,933m **[C]**.
I could **not** verify FY2024 total stockholders' equity from an opened page, so the FY2025
average-equity ROE is not computed. **[NOT OBTAINED — §12]**

**Caveat that matters:** equity grew **+28.8%** in FY2026 **[C]** — far faster than the
+18% revenue — because retained earnings are compounding much faster than buybacks are
retiring them. **A rising equity base mechanically suppresses future ROE.** ROE of 30%+ is
excellent in absolute terms, but the denominator is inflating and this ratio will drift
down even if the business performs perfectly. Do not read future ROE decline as
deterioration without checking the denominator.

### 6.3 ROIC

Method: **NOPAT ÷ (total debt incl. finance leases + total equity − cash and short-term
investments)**, ending balances.

| Component | FY2026 |
|---|---|
| Operating income | $155,237m **[P]** |
| Effective tax rate | 19.4% **[C]** |
| **NOPAT** | **$125,121m** **[C]** |
| Total debt + finance lease liabilities | $106,888m **[S]** |
| Total stockholders' equity | $442,387m **[P]** |
| Less: cash & equivalents | $(20,935)m **[P]** |
| Less: short-term investments | $(55,908)m **[P]** |
| **Invested capital** | **$472,432m** **[C]** |
| **ROIC** | **26.5%** **[C]** |

**Confidence note:** the debt figure is **[S]** from a third-party database I could not
cross-check against the filing; everything else is **[P]**. ROIC is therefore **[C] built
on one [S] input** — a ±$10bn error in debt moves ROIC by only ~±0.6pp, so the conclusion
is robust to that uncertainty.

**26.5% ROIC is a very strong number** — roughly 3.5x any plausible cost of capital.

**But the direction is what matters, and I want to be careful here.** I could **not**
compute a comparable FY2025 ROIC because FY2025 finance lease liabilities were not
obtained (§12). What I can say from the components: **invested capital is growing far
faster than NOPAT.** Total assets rose **+22.5%** to $758,376m **[C from P]**, equity
**+28.8%**, finance lease liabilities from $11.75bn (2021) to $62.3bn (2026) **[S]** —
while NOPAT grew ~21%. **Arithmetically, ROIC must be compressing.** I state that as an
**inference from directional components, not as a computed number** — it is exactly the
kind of gap-filling the brief warned against, so it is labelled as inference and the
FY2025 ROIC sits in the NOT OBTAINED register.

---

## 7. Balance sheet & debt profile

### 7.1 The balance sheet **[P unless marked]**

| | 2025-06-30 | 2026-06-30 | Δ |
|---|---|---|---|
| Cash & equivalents | $30,242m | **$20,935m** | −30.8% **[C]** |
| Short-term investments | $64,323m | **$55,908m** | −13.1% **[C]** |
| **Cash + ST investments** | **$94,565m** | **$76,843m** | **−18.7%** **[C]** |
| Accounts receivable | $69,905m | $80,876m | +15.7% **[C]** |
| Inventories | $938m | $1,397m | **+48.9%** **[C]** |
| Total current assets | $191,131m | $207,710m | +8.7% **[C]** |
| **Total assets** | **$619,003m** | **$758,376m** | **+22.5%** **[C]** |
| Current portion of long-term debt | $2,999m | **$9,227m** | **+207.7%** **[C]** |
| Long-term debt | $40,152m | **$31,067m** | **−22.6%** **[C]** |
| Short-term unearned revenue | $64,555m | $72,965m | +13.0% **[C]** |
| Long-term unearned revenue | $2,710m | $2,747m | +1.4% **[C]** |
| **Total liabilities** | **$275,524m** | **$315,989m** | +14.7% **[C]** |
| **Total stockholders' equity** | **$343,479m** | **$442,387m** | **+28.8%** **[C]** |

### 7.2 The debt profile — **the bond debt is shrinking; the lease debt is exploding**

| | 2021 | 2025-06-30 | 2026-06-30 |
|---|---|---|---|
| Long-term debt (ex-current) | $50,074m **[S]** | $40,152m **[P]** | **$31,067m** **[P]** |
| Current portion of LTD | — | $2,999m **[P]** | **$9,227m** **[P]** |
| **Finance lease liabilities** | **$11,750m** **[S]** | not obtained | **$62,304m** **[S]** |
| **Total debt + finance leases** | — | not obtained | **$106,888m** **[S]** |
| Weighted-average effective rate on debt + finance leases | — | — | **4.52%** **[S]** |

**This is the most under-appreciated item on Microsoft's balance sheet and I want it stated
clearly.** Anyone looking at "long-term debt down from $40.2bn to $31.1bn" **[P]** would
conclude Microsoft is deleveraging. **It is not.** Traditional bond debt is being allowed
to mature and roll off, while **finance lease liabilities have grown 5.3x since 2021 to
$62.3bn** **[S]** — and finance leases are debt in substance: fixed obligations, secured
against specific assets, with an interest component.

**Total debt including finance leases is $106,888m [S], of which finance leases are 58%.**
The composition of Microsoft's leverage has fundamentally changed and the change is
invisible if you read only the "long-term debt" line.

**Coverage and capacity — this is where Microsoft is genuinely unassailable:**

| Metric | FY2026 | **[C]** |
|---|---|---|
| Operating income / total debt+leases | $155,237m / $106,888m = **1.45x** | Operating income **exceeds** total debt by 45% |
| Total debt+leases / operating cash flow | $106,888m / $182,935m = **0.58x** | **Under 7 months of OCF** retires all debt |
| Approx. annual interest at 4.52% | ~$4,831m | **[E]** — rate is [S], applied to total balance |
| **Interest coverage (op. income / est. interest)** | **~32x** | **[E]** |
| Net debt (debt+leases − cash & ST inv.) | $106,888m − $76,843m = **$30,045m** | Net debt / OCF = **0.16x** **[C]** |

**Verdict on the debt: not a risk.** ~32x interest coverage **[E]**, net debt at 0.16x
operating cash flow, and an AAA/Aaa-tier credit. Even if finance lease liabilities doubled
again, coverage would remain comfortable. **The debt profile is an A+ within an A− report.**

**What I could NOT obtain and it is a real gap:** the **maturity schedule** (how much is due
in FY27, FY28, FY29+), the **coupon-by-tranche detail**, and the **operating lease
commitment schedule** — which, after the FY2027 finance-to-operating reclassification, is
about to become the *fastest-growing* off-balance-sheet obligation. **§12.** Given coverage
of ~32x, the maturity ladder is a low-consequence gap; the operating lease schedule is not.

### 7.3 The cash balance is falling — worth noting

Cash + short-term investments fell **18.7% to $76,843m** **[C from P]**. Microsoft is
funding the capex programme out of operating cash flow *and* the securities portfolio,
while still returning $48.7bn to shareholders and letting bond debt roll off. That is
internally consistent and entirely affordable. But it does mean **the flexibility buffer is
being consumed**, and if capex rises again in FY2027 as guided (~$175bn CY26 **[S]**),
either the balance sheet draws down further, buybacks moderate, or debt issuance resumes.
**Watch for renewed bond issuance in FY2027 — it would be the tell that internal funding
has reached its limit.** **[E — my inference.]**

---

## 8. Capital returns: buybacks and dividends vs SBC dilution

| FY | Buybacks | Dividends | Total returned | FCF | Payout of FCF | SBC |
|---|---|---|---|---|---|---|
| FY2023 | $22,245m **[P]** | $19,800m **[P]** | $42,045m **[C]** | $59,475m **[C]** | 70.7% **[C]** | $9,611m **[P]** |
| FY2024 | $17,254m **[P]** | $21,771m **[P]** | $39,025m **[C]** | $74,071m **[C]** | 52.7% **[C]** | $10,734m **[P]** |
| FY2025 | $18,420m **[P]** | $24,082m **[P]** | $42,502m **[C]** | $71,611m **[C]** | 59.4% **[C]** | $11,974m **[P]** |
| FY2026 | **$22,271m** **[P]** | **$26,445m** **[P]** | **$48,716m** **[C]** | **$66,987m** **[C]** | **72.7%** **[C]** | $12,405m **[P]** |

**Payout of FCF has risen from 52.7% to 72.7% in two years** **[C]** — not because returns
grew aggressively (+24.8% over two years) but because **FCF fell**. Still comfortably
covered, but the cushion has thinned considerably. **On FCF net of SBC ($54,582m [C]), the
FY2026 payout ratio is 89.3% [C]** — that is the honest number, and it is close to fully
distributing cash generation.

### Share count: the buyback is barely outrunning dilution

| | FY2025 | FY2026 | Δ |
|---|---|---|---|
| Weighted-avg diluted shares | 7,465m **[P]** | **7,453m** **[P]** | **−0.16%** **[C]** |
| Weighted-avg basic shares | 7,433m **[P]** | 7,429m **[P]** | −0.05% **[C]** |
| Buyback spend | $18,420m **[P]** | $22,271m **[P]** | +20.9% **[C]** |
| SBC expense | $11,974m **[P]** | $12,405m **[P]** | +3.6% **[C]** |
| **Buyback net of SBC** | $6,446m **[C]** | **$9,866m** **[C]** | — |

**Microsoft spent $22.3bn on buybacks and reduced the diluted share count by 0.16%.**
**[C from P]** At an illustrative average repurchase price of ~$420 **[E — Q4 FY26
repurchases were disclosed in a range of $396.19–$416.81 [S]; full-year average not
obtained]**, $22.3bn retires roughly **53m shares, or ~0.71%** of the base **[C, E-input]**.
The share count fell only 0.16%. **Therefore roughly three-quarters of the gross buyback
was consumed offsetting equity issuance** **[C, E-input — flagged as dependent on the
estimated average price]**.

**Stated plainly: the buyback is a dilution-offset programme, not a shareholder-return
programme.** **$12.4bn of the $22.3bn is economically employee compensation being
recycled.** The genuine return to shareholders in FY2026 is the **$26,445m dividend** plus
**~$9.9bn of net buyback** = **~$36.3bn** **[C]**, against $48.7bn headline. That is **54%
of FCF**, not 73%.

**In fairness:** this is the norm across mega-cap technology, Microsoft's SBC intensity is
*falling* (§3.2), and the dividend has grown for two decades. This is a **fair** capital
returns programme, not a bad one. But the headline "$48.7bn returned to shareholders"
overstates economic reality by roughly a third, and the committee should use $36.3bn.

---

## 9. Accounting red flags & quality screen

Screened against the standard four: earnings vs OCF divergence, working-capital growth vs
revenue, capitalisation games, and adjusted-figure hygiene.

### 🟢 CLEAN — Earnings vs operating cash flow
Net income **+31.3%**, operating cash flow **+34.3%** **[C from P]**. **OCF grew faster
than earnings.** Cash conversion (OCF / net income) was **1.37x in FY2026** vs 1.34x in
FY2025 **[C]** — stable and well above 1.0x. **There is no earnings-quality divergence at
the operating-cash-flow line.** This is the single most reassuring test in the whole
screen, and Microsoft passes it cleanly.

### 🟢 CLEAN — Receivables
AR **+15.7%** vs revenue **+18%** **[C from P]**. Receivables grew **slower** than revenue.
DSO improved from 90.6 days to **89.0 days** **[C]**. **No channel-stuffing or
revenue-pull-forward signature.** Given the volume of AI contracting, this is a genuinely
good result.

### 🟡 MINOR — Inventories
Inventories **+48.9%** to $1,397m vs revenue +18% **[C from P]**. Growing 2.7x faster than
revenue. **At 0.42% of revenue this is immaterial in absolute terms** and most likely
reflects AI hardware and device components. Flagged for completeness, not for concern.
Would only matter if it persists for several more quarters.

### 🟡 WATCH — Deferred (unearned) revenue growing slower than revenue
Short-term unearned revenue **+13.0%** vs revenue **+18%** **[C from P]**. Long-term
unearned revenue essentially flat at **+1.4%** **[C from P]**.

**Deferred revenue is a leading indicator; revenue is a lagging one.** Deferred revenue
growing 500bp slower than reported revenue means the *invoiced-and-unrecognised* pipeline
is building more slowly than the recognised P&L. **[E — my read:]** the most likely benign
explanation is **mix**: Azure consumption revenue is recognised as used and does not sit in
unearned revenue the way a prepaid M365 licence does, so a mix shift toward consumption
mechanically depresses this ratio. That explanation fits the facts and I find it more
likely than deterioration.

**But I am flagging it as WATCH rather than CLEAN** because I could **not** obtain the
**commercial bookings growth** or the **commercial remaining performance obligation (RPO)**
figures — the two disclosures that would settle it. **[§12].** RPO in particular is the
number that would confirm or refute the "$250bn OpenAI Azure commitment plus enterprise
backlog" story. **Its absence from this report is a real limitation.**

### 🔴 **FLAG — "Other income (expense), net" is doing far too much work**

| | FY2025 | FY2026 | Swing |
|---|---|---|---|
| Operating income | $128,528m | $155,237m | +$26,709m |
| **Other income (expense), net** | **$(4,901)m** | **+$10,697m** | **+$15,598m** |
| Income before tax | $123,627m | $165,934m | +$42,307m |

**[P] for all inputs; [C] for the swing.**

**36.9% of the growth in pre-tax income came from a single non-operating line** **[C]**.
Pre-tax income grew **+34.2%** while operating income grew **+20.8%** **[C]**. That gap is
entirely "other income".

Within it we know of: **OpenAI net gains** (+$4,963m at the *net income* level **[P]**) and
a **$3.2bn gain on the Anthropic investment in Q4** **[P]**. These are **unrealised marks
on private-company equity stakes**. They are non-cash, non-operating, non-recurring in any
meaningful sense, and can reverse — as OpenAI itself demonstrated by swinging from −$3,620m
to +$4,963m in twelve months.

**The sub-flag that concerns me most, and I want it labelled honestly as inference:**

> Microsoft's non-GAAP EPS of **$17.28** is GAAP **$17.95** less the **$0.67** OpenAI item
> **[P/C]** — that is the *only* stated adjustment. **The $3.2bn Anthropic gain therefore
> appears to remain inside non-GAAP EPS.** At the FY26 effective tax rate of 19.4%, $3.2bn
> pre-tax is ~$2.58bn after tax, or **~$0.35 per diluted share — roughly 2% of non-GAAP
> EPS** **[C]**.
>
> **This is [E] — inference, not disclosure.** I am inferring the exclusion list from the
> arithmetic reconciliation, not from an accounting policy note I read. It is possible
> Anthropic is handled differently, or that the $3.2bn figure is post-tax, or that
> offsetting items exist. **Someone with 10-K access must confirm before this is used.**
> If confirmed, it is a genuine inconsistency: **excluding one private-company mark from
> non-GAAP while including another.**

### 🟡 WATCH — Two earnings-favourable estimate changes in four years
Covered in §2.2. Server/network life 4y → 6y (2022); data centre and office building life
15y → 25y (FY2027) **[S]**. **Each is individually defensible.** The pattern, and the fact
that both landed while depreciation was accelerating, is a legitimate watch item. **I am
not calling this a red flag** — 25-year building lives are ordinary — but I am recording it
because the brief specifically asked and because the committee should know the lever exists
and has been used twice.

### 🟡 WATCH — Capex definition change reduces reported capex without reducing spending
Covered in §2.2. The finance-to-operating lease shift lowers **reported** capex by moving
obligations off the capex line, contributing to the CY2026 guidance restatement to ~$175bn
**[S]** with **underlying investment plans unchanged** **[S]**. **This is not a capitalisation
game in the classic sense** — nothing improper is happening, and the treatment follows the
lease standard. But it **will make FY2027 capex and FCF optically better than the economics**,
and anyone comparing FY2027 capex to FY2026 capex without adjusting is comparing different
things. **[E for the forward effect.]**

### 🟢 CLEAN — Share count creep
Diluted shares **fell** 0.16% **[C from P]**. SBC growth **+3.6%** vs revenue +17.8%. No
creep. **See §8 for the caveat that the buyback is mostly funding the offset** — that is a
capital-allocation observation, not an accounting flag.

### 🟢 CLEAN — Tax
Effective rate **rose** from 17.6% to 19.4% **[C from P]**. Earnings growth was achieved
**despite** a 177bp tax headwind, not with the help of a tax tailwind. **No tax-rate
management signature.**

### Screen summary

| Test | Result |
|---|---|
| Earnings vs operating cash flow | 🟢 CLEAN (OCF grew faster) |
| Receivables vs revenue | 🟢 CLEAN (grew slower; DSO improved) |
| Inventories vs revenue | 🟡 MINOR (immaterial at 0.42% of revenue) |
| Deferred revenue vs revenue | 🟡 WATCH (500bp slower; RPO not obtained) |
| **"Other income" quality** | 🔴 **FLAG (36.9% of pre-tax growth from marks)** |
| Adjusted-figure hygiene | 🟡 WATCH (Anthropic gain apparently not excluded — **[E]**) |
| Estimate changes | 🟡 WATCH (two earnings-favourable in four years) |
| Capex definition | 🟡 WATCH (optical reduction, spending unchanged) |
| Share count creep | 🟢 CLEAN |
| Tax rate management | 🟢 CLEAN |

**One red flag, five watch items, four clean.** **The core operating statements are honest.**
Every issue I found sits either **below the operating income line** (marks, other income) or
**in the notes and forward guidance** (estimates, lease definitions). **Nothing I found
casts doubt on the $155,237m of operating income or the $182,935m of operating cash flow.**
That distinction is what keeps this an A− rather than a B.

---

## 10. Anti-anchoring (L-003): both cases at full strength

The house has graded one Chinese small-cap at D+ and one at A−. Neither has any bearing on
Microsoft. I have tried to build both cases from the numbers and then say which I found.

### The bull case at full strength — **and I found most of it**

> A company growing revenue 17.8% at $332bn scale, **expanding operating margin 116bp to
> 46.8% while simultaneously absorbing a 510bp increase in D&A intensity**, converting net
> income to operating cash flow at **1.37x**, running **26.5% ROIC** and **34% ROE**, with
> **~32x interest coverage** and **net debt of 0.16x operating cash flow** — and whose
> largest business unit **accelerated** from 40% to 43% growth in the most recent quarter,
> passing $100bn of annualised revenue. Receivables grew slower than revenue. SBC intensity
> is *falling*. The tax rate *rose*. Cash flow grew faster than earnings.
>
> The capex is not a bug: capex is being deployed against demand that is visibly
> materialising, and the proof is that the segment absorbing the depreciation is *growing
> faster*, not slower. FCF is down because the company is choosing to build. Any company
> that could stop building tomorrow and show $180bn of FCF is not a company with a cash
> flow problem.

**How much did I find? Almost all of it.** Every figure in that paragraph is **[P]** or
**[C] from [P]** except the Azure growth rates **[S]** and the interest rate **[S]**. **The
bull case is well supported by the audited-equivalent statements.** This is the strongest
set of financials I have examined for this firm, and I want that on the record before the
bear paragraph, because it is the more evidenced of the two.

### The bear case at full strength — **and I found the setup, not the event**

> Capex has gone from 13.3% of revenue to **34.9%** in three years and from 32.1% to
> **63.4%** of operating cash flow. **Free cash flow has fallen two years running** and is
> **9.6% below its FY2024 peak** while revenue grew 35%. FCF margin collapsed 1,000bp to
> 20.2%, and on an SBC-adjusted basis Microsoft is distributing **89% of cash generation**.
> **Gross margin is falling** and only opex leverage — a finite resource — is holding the
> operating margin up. **Intelligent Cloud, the segment doing all the growing, is the one
> segment whose margin went backwards.**
>
> Meanwhile **26.9% of EPS growth and 36.9% of pre-tax income growth came from
> non-operating marks** on private AI companies, one of which swung $8.6bn in a year.
> Finance lease debt has grown **5.3x since 2021** while the headline debt line falls,
> disguising the leverage build. The company has **withdrawn the disclosure** that
> quantified AI's contribution to Azure growth, **discloses no Copilot revenue at all**
> after three years of promotion, has **extended depreciable lives twice in four years** in
> earnings-favourable directions, and has just **redefined capex** so that FY2027 will look
> better than the economics warrant.

**How much did I find? The setup, comprehensively. The trigger, not at all.** Every capex,
FCF, margin and disclosure item above is verified **[P]/[C]**. **What is missing is the
deceleration.** The bear case is an argument about what happens when a 30%-compounding
depreciation base meets a decelerating revenue line — **and in FY2026 the revenue line
accelerated.** Until Azure growth breaks below roughly the mid-20s, the bear case is a
loaded gun that has not been fired.

**My honest position: the bear case is a well-constructed FY2027–FY2028 risk, not an FY2026
diagnosis.** I am not going to grade the company down today for a deterioration I could not
find in the statements. Nor will I pretend the FCF trend is fine — it is the clearest
warning signal in the accounts and it has now printed twice.

**What would change my mind, specifically:**

| Trigger | Reading |
|---|---|
| Azure growth < 25% for two consecutive quarters | Bear case activates — depreciation outruns revenue |
| Intelligent Cloud margin down >200bp YoY | Depreciation is winning |
| FY2027 FCF falls a **third** consecutive year | Structural, not cyclical |
| Gross margin down >150bp with opex ratio flat | Opex leverage exhausted |
| Server/network life extended **beyond 6 years** | Serious earnings-quality red flag |
| Renewed large bond issuance | Internal funding limit reached |
| FY2027 FCF "recovers" while operating leases balloon | Definitional, not real — do not credit it |

---

## 11. Financial score: **79 / 100 — Grade A−**

| Component | Weight | Score | Rationale |
|---|---|---|---|
| **Profitability & margin trend** | 20 | **17/20** | 46.8% operating margin, +116bp; 67.9% gross margin. **−3** for gross margin down 88bp and Intelligent Cloud margin down 62bp — the erosion is real and located exactly where the capex is. |
| **Cash generation** | 25 | **16/25** | OCF +34.3% and 1.37x conversion are excellent. **−9** because **FCF fell for the second consecutive year** to $66,987m, FCF margin collapsed 1,000bp to 20.2%, and the SBC-adjusted payout is 89%. This is the largest single deduction and it is deliberate. |
| **Returns on capital** | 15 | **13/15** | 26.5% ROIC, 34.0% ROE (avg equity) are outstanding. **−2** for an invested-capital base compounding faster than NOPAT, and because FY2025 ROIC could not be computed for comparison. |
| **Balance sheet & debt** | 15 | **14/15** | Net debt 0.16x OCF, ~32x interest coverage, operating income exceeds total debt. **−1** for the finance-lease build (5.3x since 2021) being invisible in the headline debt line, and for the unobtained maturity/operating-lease schedules. |
| **Earnings quality & accounting** | 20 | **13/20** | Core operating statements clean: OCF > net income, AR slower than revenue, no share creep, tax rate rose. **−7** for the "other income" red flag (36.9% of pre-tax growth from marks), the apparent non-exclusion of the Anthropic gain from non-GAAP **[E]**, two earnings-favourable estimate changes, and the capex redefinition. |
| **Disclosure quality** | 5 | **3/5** | Statements are clear and IR publishes them accessibly. **−2** for withdrawing the AI-contribution-to-Azure split and for **zero disclosed Copilot revenue** after three years of promotion. |
| **Data completeness penalty** | — | **3** | No 10-K/10-Q opened (SEC blocked). Useful-life note, RPO/bookings, maturity ladder, operating lease schedule all unobtained. A modest deduction is honest: I graded the statements, not the notes. |
| **TOTAL** | **100** | **79** | **A−** |

**Calibration check.** 0100.HK D+ 48/100; 6160.HK A− 82/100. MSFT at **79** sits **just
below 6160.HK** and far above 0100.HK. I considered 84 — the profitability, returns and
balance sheet arguably justify it. **I held at 79 for one reason: a company whose free cash
flow has now declined two years in a row, and where over a quarter of EPS growth came from
marking private equity stakes, cannot score above a name whose cash generation was
unambiguous.** The FCF trend and the "other income" flag are the two things that cost
MSFT the A.

**If the FY2026 10-K confirms (a) server/network life unchanged at 6 years and (b) the
Anthropic gain is in fact excluded from non-GAAP, I would move this to 83–84 (A−/A).**
**If it shows a further life extension or an aggressive capitalisation policy, 72–74 (B).**

### The three numbers that matter most

1. **FCF $66,987m — down 6.5%, second consecutive annual decline, −9.6% from FY2024 peak
   [C from P].** The thesis lives or dies here.
2. **Capex 63.4% of operating cash flow [C from P]** (FY2024: 37.5%). How much of the
   machine is being reinvested instead of returned — nearly doubled in two years.
3. **D&A +30.9% vs revenue +17.8% [C from P].** The depreciation tail is already
   outrunning revenue, and the FY2026 $115.9bn cohort has not yet fully landed.

---

## 12. NOT OBTAINED register

Explicit list of everything I could not verify. **Nothing below was filled from memory.**

### Blocking cause
`www.sec.gov`, `microsoft.gcs-web.com`, `www.fool.com`, `news.alphastreet.com`,
`www.cnbc.com`, `deepquarry.substack.com` — **all EGRESS_BLOCKED**. `finance.yahoo.com`,
`stockanalysis.com`, `businesswire.com` blocked in prior sessions. `tradingkey.com`
blacklisted. **No 10-K or 10-Q was opened.** FY26 Annual Report URL returned 404.

### Priority 1 — would change the grade

| Item | Why it matters | Status |
|---|---|---|
| **Server & network equipment useful life in the FY2026 10-K** | Directly asked in the brief. Working assumption of 6 years is **[E]**. A change either way is material. | **UNVERIFIED** |
| **Quantified P&L effect of the FY2027 15y→25y building life extension** | Management says "minimal benefit to FY27 operating income" **[S]**. I could not verify or size it. | **NOT OBTAINED** |
| **Operating lease commitment schedule (post-reclassification)** | The fastest-growing off-balance-sheet obligation from FY2027. Largest unquantified item in the report. | **NOT OBTAINED** |
| **Whether the $3.2bn Anthropic gain is excluded from non-GAAP EPS** | §9 red-flag sub-item rests on inference **[E]**. | **INFERRED, UNVERIFIED** |

### Priority 2 — would improve precision

| Item | Status |
|---|---|
| Commercial bookings growth and **commercial RPO / backlog** for FY2026 | **NOT OBTAINED** — would settle the deferred-revenue WATCH flag and size the $250bn OpenAI commitment |
| Debt **maturity ladder** by year and coupon-by-tranche | **NOT OBTAINED** (low consequence at ~32x coverage) |
| FY2025 finance lease liabilities → prevents a computed FY2025 ROIC comparison | **NOT OBTAINED** |
| FY2024 total stockholders' equity → prevents FY2025 average-equity ROE | **NOT OBTAINED** |
| Official FY2026 **"capex including finance leases"** total (my ~$144bn is **[E]**) | **NOT OBTAINED** |
| Full-year average share repurchase price (only a Q4 range $396.19–$416.81 **[S]**) | **NOT OBTAINED** |
| PP&E gross/net **by asset class** — needed to size the depreciation tail properly | **NOT OBTAINED** |
| Azure absolute quarterly revenue (only the ">$100bn annual" milestone) | **NOT DISCLOSED by company** |
| **AI-services contribution to Azure growth, in points** | **NOT DISCLOSED by company in FY2026** — withdrawn disclosure |
| **Copilot revenue, ARR, ChR or realised ASP** | **NOT DISCLOSED by company** — seats only |
| Segment revenue for FY2024 on the restated basis | **NOT OBTAINED** |
| FY2027 guidance detail (revenue, margin, capex by quarter) | **NOT OBTAINED** |
| Cap amount on the OpenAI revenue share (April 2026 revision) | **NOT OBTAINED** — CNBC blocked |
| Gross margin % by segment / Microsoft Cloud GM% for Q4 FY2026 | **NOT OBTAINED** (Q1 69%, Q3 MS Cloud 66% are **[S]**) |

### Figures deliberately **rejected**, not adopted

- **"30m Copilot seats ⇒ ~$10bn ARR"** **[S]** — third-party list-price arithmetic.
  Rejected; enterprise discounting and bundling make it unreliable (§4.4).
- **"AI annual revenue run-rate $37bn, +123% YoY (Q3 FY26)"** **[S]** — quoted with an
  explicit warning; definition unseen, not audited revenue. **Do not model.**
- **Anything from `tradingkey.com`** — appeared in search results; firm-wide blacklist.

---

## Research-only notice

This is a financial-statement analysis. **It contains no recommendation, target price or
position sizing.** Valuation is 𢦀鳩仔's mandate; the moat question is 菲比斯's; management
quality is Peter's. The Investment Committee and the Owner decide.

---

## Sources

**Primary (pages actually opened) — [P]:**
- [Microsoft FY26 Q4 Press Release & Webcast — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) — FY2026/FY2025 income statement, balance sheet, cash flow, segments
- [Microsoft FY24 Q4 Cash Flows — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2024-q4/cash-flows) — FY2024/FY2023 cash flow statement
- [Microsoft 2025 Annual Report](https://www.microsoft.com/investor/reports/ar25/index.html) — FY2025/FY2024 income statement and segment operating income

**Search extractions (pages not opened) — [S]:**
- [Microsoft Cloud and AI strength fuels fourth quarter results — Microsoft Source](https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/)
- [Microsoft Fiscal Year 2026 Fourth Quarter Earnings Conference Call — Investor Relations](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- [Microsoft FY26 Q3 Press Release — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast)
- [Microsoft holds the line on AI spending plans — CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/)
- [Microsoft Capex Tracker — Hallucination Yield](https://www.hallucinationyield.com/research/microsoft-capex/)
- [Microsoft anticipates $3.3bn savings by extending server life — Computer Weekly](https://www.computerweekly.com/news/252523221/Microsoft-anticipates-33bn-savings-by-extending-server-life)
- [Accounting policy changes boost tech earnings — Hudson Labs](https://www.hudson-labs.com/blog/accounting-policy-changes-boost-tech-earnings)
- [Microsoft's recent $68 billion in physical assets additions — Epoch AI](https://epoch.ai/data-insights/microsoft-ppe-breakdown)
- [Microsoft Corp. — Analysis of Debt — Stock Analysis on Net](https://www.stock-analysis-on.net/NASDAQ/Company/Microsoft-Corp/Analysis/Debt)
- [Microsoft gets 27% stake in OpenAI, and a $250B Azure commitment — GeekWire](https://www.geekwire.com/2025/microsoft-secures-27-stake-in-openai-in-new-deal-with-commitment-for-250b-in-azure-usage/)
- [The next chapter of the Microsoft–OpenAI partnership — Official Microsoft Blog](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
- [OpenAI completes for-profit move, Microsoft given 27% stake — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/openai-completes-for-profit-move-microsoft-given-27-stake-and-250bn-azure-contract-but-no-longer-has-cloud-right-of-first-refusal/)
- [Microsoft and Its OpenAI Losses — Calcbench](https://www.calcbench.com/blog/post/blogger7889213530921195705/Microsoft-and-Its-OpenAI-Losses)
- [Microsoft obscures OpenAI's $11.5 billion loss — Windows Central](https://www.windowscentral.com/artificial-intelligence/openai-chatgpt/microsoft-obscures-openais-usd11-5-billion-loss)
- [Microsoft Q4 FY2026: AI Demand Accelerates Azure and Enterprise Growth — Futurum](https://futurumgroup.com/insights/microsoft-q4-fy-2026-ai-demand-accelerates-azure-and-enterprise-growth/)
- [Microsoft's cloud brings rain of revenue but modest M365 AI revenue harvest — The Register](https://www.theregister.com/software/2026/07/30/microsoft-earnings-q4-26-cloud-brings-revenue-rain/5280798)
- [Microsoft spent $11.1bn on data center leases alone in Q1 2026 — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/microsoft-spent-111bn-on-data-center-leases-alone-in-q1-2026/)
- [Microsoft Q3 FY2026: The $190B Capex Plan That Repriced AI — Global Data Center Hub](https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex)
- [Microsoft (MSFT) spent $4.627 billion on share buybacks during Q3 2026 — Shacknews](https://www.shacknews.com/article/148917/microsoft-msft-stock-buybacks-q3-2026)
- [Microsoft Stock-Based Compensation — Eulerpool](https://eulerpool.com/stock/Microsoft-Stock-US5949181045/stock-basedcompensation)
- [MICROSOFT FCF $66,987 Mil — GuruFocus](https://www.gurufocus.com/term/total-free-cash-flow/MSFT)

**Blocked / not opened:** `www.sec.gov`, `microsoft.gcs-web.com`, `www.cnbc.com`,
`www.fool.com`, `news.alphastreet.com`, `deepquarry.substack.com`, `finance.yahoo.com`,
`stockanalysis.com`, `businesswire.com`. **`tradingkey.com` — blacklisted, not cited.**

---
*巴爺爺 · Financial Statement Analyst · Department 2, Equity Research · 皮褸黃 Capital*
*Report ID: 2026-08-21-MSFT-FIN · Research only — the Committee and the Owner decide.*
