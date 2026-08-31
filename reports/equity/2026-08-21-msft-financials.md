# MSFT — Microsoft Corporation | Financial Statement Analysis

**Analyst:** 巴爺爺, Financial Statement Analyst (Dept 2 — Equity Research)
**Date:** 2026-08-21
**Ticker:** MSFT (NASDAQ) · **Owner position:** none · **Watchlist sleeve:** `ai:`
**Prior firm coverage:** none — this is the firm's first MSFT report.
**Period analysed:** FY2023 – FY2026 (four fiscal years, FYE 30 June)

> **STATUS: FINAL.** Three statements verified from primary IR pages for FY2023–FY2026.
> Note-level detail (useful lives, debt ladder, OpenAI note) unverified — see §0 and §12.

---

## 0. Sourcing caveat (read first)

**Partial success against the egress policy — materially better than briefed.** The brief
warned to expect that *no* primary filing would be readable. That was too pessimistic:
**`www.microsoft.com/en-us/investor/...` is accessible**, and Microsoft publishes its full
condensed income statement, balance sheet, cash-flow statement and segment tables there.
**The four-year trend tables in this report were read off pages I actually opened.**

| Host / page | Result |
|---|---|
| `.../earnings/fy-2026-q4/press-release-webcast` | **OPENED.** FY26/FY25 income statement, balance sheet, cash flow, segments |
| `.../earnings/fy-2024-q4/cash-flows` | **OPENED.** FY24/FY23 cash flow statement |
| `.../earnings/fy-2024-q4/income-statements` | **OPENED.** FY24/FY23 income statement |
| `.../earnings/fy-2024-q4/balance-sheets` | **OPENED.** FY24/FY23 balance sheet |
| `www.microsoft.com/investor/reports/ar25/` | **OPENED.** FY25/FY24 segment operating income |
| `.../reports/ar26/`, `.../fy-2026-q4/{cash-flows,performance,segment-revenues}` | **HTTP 404** — Q4 sub-pages and FY26 annual report not published at these paths |
| `www.sec.gov` | **EGRESS_BLOCKED.** Confirmed once, not retried. **No 10-K or 10-Q opened.** |
| `microsoft.gcs-web.com`, `www.stock-analysis-on.net`, `www.cnbc.com`, `www.fool.com`, `news.alphastreet.com`, `deepquarry.substack.com`, `www.investing.com` | **EGRESS_BLOCKED** |
| `finance.yahoo.com`, `stockanalysis.com`, `businesswire.com` | Blocked in prior sessions; not retried |
| `tradingkey.com` | **Firm-wide blacklist.** Appeared repeatedly in results. **Not used, not cited.** One figure sourced only to it was discarded — see §11.4 |

**Figure-provenance convention — on every number in this report:**

- **[P]** = *Primary, document opened.* Read off a `microsoft.com` IR page I fetched.
- **[S]** = *Search extraction.* Summarised by WebSearch from a page I could **not** open.
  One confidence notch lower — I could not see the surrounding table or footnote.
- **[C]** = *Calculated by me* from [P] inputs. Arithmetic mine, inputs cited.
- **[E]** = *Estimate / inference.* Assumption stated explicitly.

**What this means:** **the three statements are solid [P] for four years. The notes are
not.** Useful-life accounting policy, the debt maturity ladder, the OpenAI equity-method
note and the lease footnote are **[S]** — reconstructed from transcript summaries and
third-party databases. **Those are exactly the areas where the bear case lives.** Weight
accordingly; see §12.

**Staleness:** FY2026 ended **2026-06-30**; results released **2026-07-29**. Today is
2026-08-21 — **~7 weeks past period end, ~3 weeks past release. Fresh.** The FY2026 **10-K**
could not be confirmed filed or read (SEC blocked); all note-level detail is unconfirmed
against the filed document.

---

## 1. Summary & Grade

### **Grade: A− · Score: 79 / 100**

House calibration: 0100.HK **D+ 48/100**; 6160.HK **A− 82/100** (strongest graded to date).
MSFT lands **just below 6160.HK** — a genuinely excellent set of financial statements,
marked down for reasons that are specific, quantified, and not generic mega-cap grumbling.

**The operating year was outstanding.** Revenue $331,839m (+17.8%), operating income
$155,237m (+20.8%), operating margin up **116bp to 46.8%** — margin *expansion* in the
teeth of the largest capex programme in corporate history. Operating cash flow up **34.3%
to $182,935m**, converting net income at **1.37x**. **[P]/[C]**

**Three things stop this being an A.**

1. **Free cash flow has now fallen two years running.** FY2024 $74,071m → FY2025 $71,611m
   → FY2026 $66,987m **[C from P]** — **−9.6% from the FY2024 peak** while revenue rose
   **+35.4%** over the same span. Capex absorbed **63.4%** of operating cash flow in FY2026,
   up from 32.1% in FY2023 **[C]**. **This is the number the committee should hold onto.**
2. **26.9% of FY2026 EPS growth was a mark, not a business.** Net gains on the OpenAI
   investment added $4,963m / **$0.67** in FY2026; the same line was a **$3,620m / $0.49
   drag** in FY2025 **[P]/[S]**. The $1.16 swing is **26.9% of the $4.31 of EPS growth**
   **[C]**. More broadly, **36.9% of pre-tax income growth came from "other income"** — a
   single non-operating line **[C from P]**.
3. **The estimate lever has now been pulled a second time.** Effective **FY2027**, Microsoft
   extended the useful life of **data centres and office buildings from 15 to 25 years**,
   and is shifting future data-centre leases from finance leases (inside capex) to operating
   leases (outside capex) **[S]**. This follows the 2022 extension of server/network
   equipment from 4 to 6 years **[S]**. §2.2.

**The single best thing I found, and it cuts hard against the bear case:** **Intelligent
Cloud revenue +29.7% with Azure accelerating to +43% in Q4** **[P]/[S]**, while company
operating margin **expanded** 116bp despite D&A rising **+30.9%** **[C from P]**. The
"decelerating AI revenue meets depreciation wave" thesis requires deceleration. **In FY2026
it did not happen — Azure accelerated, and guidance points to further acceleration in H1
FY2027 [S].** I could not find the deceleration the bear case needs. **That is why this is
an A−, not a B.**

**Three numbers that matter most:**

| # | Number | Value | Why |
|---|---|---|---|
| 1 | **Free cash flow, FY2026** | **$66,987m · −6.5% YoY · second consecutive decline · −9.6% from FY24 peak** **[C from P]** | The whole thesis. If FY2027 FCF falls a third time, the compounding story pauses. |
| 2 | **Capex as % of operating cash flow** | **63.4%** (FY23: 32.1%; FY24: 37.5%) **[C from P]** | How much of the machine is reinvested rather than returned. Doubled in three years. |
| 3 | **D&A growth vs revenue growth** | **+30.9% vs +17.8%** **[C from P]** | The depreciation tail is already outrunning revenue — and the FY26 $115.9bn cohort has not yet fully landed. |

---

## 2. The AI capex cycle and its depreciation tail

The central financial question; it gets the most space.

### 2.1 Capex, FY2023 → FY2026 — the intensity has 2.6x'd

**Cash "additions to property and equipment"** (cash-flow-statement line; **excludes**
finance leases). **All inputs [P]; all ratios [C].**

| FY | Additions to PP&E | YoY | Revenue | **Capex / revenue** | Operating cash flow | **Capex / OCF** |
|---|---|---|---|---|---|---|
| FY2023 | **$28,107m** | — | $211,915m | **13.3%** | $87,582m | **32.1%** |
| FY2024 | **$44,477m** | +58.2% | $245,122m | **18.1%** | $118,548m | **37.5%** |
| FY2025 | **$64,551m** | +45.1% | $281,724m | **22.9%** | $136,162m | **47.4%** |
| FY2026 | **$115,948m** | **+79.6%** | $331,839m | **34.9%** | $182,935m | **63.4%** |

**Read this table slowly.** In three years capex went from consuming one-third of operating
cash flow to consuming **nearly two-thirds**. Capex intensity relative to revenue has
**2.6x'd**. Cumulative FY24–FY26 capex is **$224,976m** **[C]** — more than the *entire*
FY2023 revenue base. This is no longer a mature software company's cash-flow profile; it is
closer to a utility or a semiconductor fab wrapped around a software P&L.

### 2.2 Capex **including finance leases** — and why the definition just changed

Microsoft's headline "capex including finance leases" exceeds the cash line because finance
leases are non-cash additions.

- Q4 FY2026 capex incl. finance leases: **~$41bn, +69% YoY** **[S]**; cash paid for PP&E
  ~$35.8bn **[S]** ⇒ **~$5.6bn** of Q4 finance leases **[C]**.
- Quarterly finance leases FY2026 as extracted: Q1 **$11.1bn**, Q2 **$6.7bn**, Q3 **$4.7bn**,
  Q4 **$5.6bn** ⇒ **~$28.1bn** for the year **[S]**.
- **⇒ FY2026 capex including finance leases ≈ $144bn** **[E]**, vs $115.9bn on the cash line
  **[P]**. **Flagged as an estimate, not a disclosure** — I could not open a document stating
  the FY2026 including-leases total, and the quarterly inputs are search extractions.
  **Do not quote $144bn as a company figure.**
- Balance-sheet corroboration: **finance lease liabilities reached $62,304m at 2026-06-30**,
  from $11,750m in 2021 **[S]** — a 5.3x build, consistent with very large lease-funded
  capacity additions.

**The change that matters.** On the Q4 FY2026 call management stated **[S]**:

- Effective at the start of **FY2027**, the estimated useful life of **data centres and
  office buildings is extended from 15 to 25 years**.
- More future data-centre leases shift from **finance leases (counted in capex)** to
  **operating leases (not counted in capex)**.
- The combined effect **restates the calendar-2026 capex expectation to ~$175bn**, from a
  ~$190bn figure circulating pre-print **[S]**, with **underlying investment plans unchanged**.
- Management's characterisation: it "only affects the timing of future depreciation, with a
  **minimal benefit to FY27 operating income**" **[S]**.

**Three separate things happened at once, and they are not equivalent:**

| Change | Effect on P&L | Effect on reported capex | My read |
|---|---|---|---|
| Building / DC life 15y → 25y | **Lowers** annual depreciation on that asset class | none | Real earnings tailwind; **size undisclosed** |
| Finance → operating lease shift | Moves cost from D&A + interest into operating expense; ~cost-neutral over life | **Lowers reported capex** | **Optical.** Capex shrinks; the obligation does not |
| Guidance restated to ~$175bn | — | −$15bn vs prior expectation | **Definitional, not a spending cut** |

**This is the most important single paragraph in the report.** A reader who sees "Microsoft
cut CY2026 capex guidance from $190bn to $175bn" and infers spending discipline **has been
misled**. Management said explicitly that **underlying investment plans are unchanged**
**[S]**. The capex line got smaller because the accounting definition changed. Anyone
modelling capex-to-FCF must model the **operating lease payments** that now sit outside
capex — and I **could not obtain the operating lease commitment schedule** (§12). **That is
the largest unquantified item in this report.**

On the extension itself: **25 years for a data-centre shell is not aggressive on its face.**
The shell genuinely outlives the servers inside it, and 25–40 years is ordinary in REIT and
utility practice. **My objection is not to the assumption; it is to the pattern and the
timing.** Microsoft extended server life in 2022 (4y → 6y; an anticipated **+$3.3bn** FY2023
operating-income benefit **[S]**, with ~$1.1bn in the first quarter after the change **[S]**).
It has now extended building life in 2026. Both changes were **earnings-favourable**; both
landed while the depreciation line was accelerating. Each is individually defensible. **The
committee should know the lever exists and has now been used twice.**

### 2.3 Has the **server** useful life been revised again? — **NOT ESTABLISHED**

The brief asks specifically. **I could not resolve it.**

- The 2022 change (server and network equipment **4 → 6 years**) is well documented **[S]**.
- Microsoft's stated policy range for computer equipment is **2–6 years**, with cloud
  servers and networking equipment at **6 years** **[S]**.
- The FY2027 change is described in every source as covering **data centres and office
  buildings** — i.e. **shells, not servers** **[S]**.
- I found **no** source stating the server/network life has been shortened, lengthened or
  reaffirmed in FY2026.

**Working assumption: server and network equipment remains at 6 years [E]. Marked
UNVERIFIED.** It requires the FY2026 10-K Property and Equipment note, behind the SEC block.
**This is the highest-priority open item (§12).** It matters in both directions: a
*shortening* toward 4–5 years — which several peers have faced pressure on — would be a large
negative EPS event; a *further lengthening* would be a significant earnings-quality red flag.

### 2.4 The depreciation tail, quantified as far as I can

| FY | D&A and other | YoY | Revenue YoY | **D&A as % of revenue** |
|---|---|---|---|---|
| FY2023 | **$13,861m** **[P]** | — | — | **6.5%** **[C]** |
| FY2024 | **$22,287m** **[P]** | **+60.8%** | +15.7% | **9.1%** **[C]** |
| FY2025 | **$29,433m** **[P]** | +32.1% | +14.9% | **10.4%** **[C]** |
| FY2026 | **$38,534m** **[P]** | **+30.9%** | +17.8% | **11.6%** **[C]** |

*Caveat:* this line is "**Depreciation, amortization, and other**" — **not pure
depreciation**; it includes other non-cash items. Best proxy available without the 10-K note.
**[P] for values, [E] for treating it as a depreciation proxy.**

**D&A has grown faster than revenue in each of the last three years**, rising from 6.5% to
**11.6%** of revenue — a **510bp structural drag absorbed while operating margin still
expanded**. That is genuinely impressive and the strongest single argument against the bear
case so far.

**But the tail is in front of us, not behind us.** The $115.9bn spent in FY2026 was spent
*through* the year; much is not yet in service or only partly depreciated.

> **Illustrative scale [E], not a forecast:** at a 6-year life the FY2026 $115.9bn cohort
> carries **~$19.3bn of annual depreciation at full run-rate** **[C]** — **~12.4% of FY2026
> operating income**, roughly **$2.59 of pre-tax EPS** or **~$2.09 after tax** at the FY26
> 19.4% rate **[C]**. Microsoft must grow operating profit by about that much *just to stand
> still* on the FY26 cohort alone, before the FY2027 cohort.
>
> **This overstates the true figure and I want that on the record.** It assumes the entire
> cash capex is 6-year-life equipment, which is wrong — a meaningful share is land and shells
> on 25-year lives that depreciate far more slowly, and land is not depreciated at all.
> **The true number is lower, probably materially.** Without the 10-K PP&E-by-asset-class
> table I cannot narrow it. **Marked [E]; logged in §12.** An honest range beats false
> precision.

### 2.5 Verdict on the depreciation-wave bear case

**Setup comprehensively supported. Trigger absent.**

- ✅ **Supported:** capex intensity 2.6x'd; D&A compounding ~31% and outrunning revenue; FCF
  down two years running; the accounting definition of capex just changed in an
  earnings-favourable direction; finance-lease debt up 5.3x since 2021.
- ❌ **Not supported:** the bear case requires **decelerating AI revenue**. FY2026 delivered
  the opposite — Azure **accelerated** to +43% in Q4 from +40% in Q3 **[S]**, Intelligent
  Cloud +29.7% for the year **[P]**, company operating margin **expanded** 116bp **[C]**, and
  management guided to **further Azure acceleration in H1 FY2027** **[S]**.
- ⚠️ **The real risk is timing, not direction.** Depreciation is contractual and certain;
  Azure growth is not. The bear case does not need Azure to shrink — **only to decelerate to
  the mid-20s while D&A keeps compounding at 30%. FY2027–FY2028 is when that gets tested.**

---

## 3. Free cash flow after all of that

### 3.1 The FCF bridge — **falling, not flat**

**All inputs [P]; FCF and ratios [C].**

| FY | Operating cash flow | Additions to PP&E | **FCF** | FCF YoY | **FCF margin** | OCF / net income |
|---|---|---|---|---|---|---|
| FY2023 | $87,582m | $(28,107)m | **$59,475m** | — | **28.1%** | 1.21x |
| FY2024 | $118,548m | $(44,477)m | **$74,071m** | **+24.5%** | **30.2%** | 1.35x |
| FY2025 | $136,162m | $(64,551)m | **$71,611m** | **−3.3%** | **25.4%** | 1.34x |
| FY2026 | $182,935m | $(115,948)m | **$66,987m** | **−6.5%** | **20.2%** | 1.37x |

**Answer to the brief's question, unambiguously: FCF is falling.** It peaked in FY2024 and
has declined in each of the two years since — **−9.6% cumulative from peak** while revenue
grew **+35.4%** **[C]**. FCF margin compressed from 30.2% to **20.2%** — a **1,000bp
collapse in two years**.

**This is why the house rule "cash flow over reported earnings" matters here.** Reported GAAP
EPS grew **+31.6%** in FY2026. Free cash flow **fell 6.5%**. Both statements are true and they
point in opposite directions. **The committee should anchor on the second.**

**Two mitigations, stated fairly and at full strength:**

1. **This is FCF after 100% of growth capex.** Microsoft is not spending $115.9bn on
   maintenance — the overwhelming majority is capacity expansion against contracted, visibly
   materialising demand. Declining FCF driven by *discretionary growth investment* is
   categorically different from declining FCF driven by deteriorating operations. **Operating
   cash flow grew 34.3% and cash conversion improved to 1.37x** — the engine is not the
   problem. A company that could stop building tomorrow and print ~$180bn of FCF does not
   have a cash-flow problem.
2. **FY2027 FCF will look artificially better.** Operating-lease payments reduce OCF, but the
   associated capacity no longer appears in capex. The net FCF optic improves while the
   economic obligation is unchanged. **Watch for an FY2027 "FCF recovery" that is
   definitional.** **[E — my inference from the disclosed mechanics.]**

### 3.2 Stock-based compensation: **yes, FCF is flattered — by $12,405m**

| FY | SBC | YoY | % of revenue | % of FCF |
|---|---|---|---|---|
| FY2023 | $9,611m **[P]** | — | 4.5% **[C]** | 16.2% **[C]** |
| FY2024 | $10,734m **[P]** | +11.7% | 4.4% **[C]** | 14.5% **[C]** |
| FY2025 | $11,974m **[P]** | +11.6% | 4.3% **[C]** | 16.7% **[C]** |
| FY2026 | $12,405m **[P]** | **+3.6%** | **3.7%** **[C]** | **18.5%** **[C]** |

**Plainly: yes.** SBC is a non-cash addback inside operating cash flow, so the $66,987m FCF
figure includes **$12,405m of compensation paid in stock**. **FCF net of SBC = $54,582m
[C]** — 18.5% lower, an FCF margin of **16.4%** rather than 20.2%.

**However — and I want this at full strength because it is genuinely unusual:** SBC grew only
**+3.6%** against **+17.8%** revenue growth, and has fallen from **4.5% to 3.7% of revenue**
since FY2023 **[C from P]**. Microsoft is one of very few large-cap technology companies where
**SBC intensity is declining** during the most intense talent competition in the sector's
history. On this specific metric Microsoft is materially better-behaved than its peer set.
**The SBC-versus-buyback picture in §8 is considerably less flattering.**

---

## 4. Segment detail

### 4.1 Full-year segments, FY2026 vs FY2025 **[P]; margins [C]**

| Segment | Revenue FY26 | Revenue FY25 | YoY | Op. income FY26 | Op. income FY25 | **OM FY26** | **OM FY25** | Δ |
|---|---|---|---|---|---|---|---|---|
| Productivity & Business Processes | $139,996m | $120,810m | **+15.9%** | $83,879m | $69,773m | **59.9%** | 57.8% | **+215bp** |
| Intelligent Cloud | $137,791m | $106,265m | **+29.7%** | $56,972m | $44,589m | **41.3%** | 42.0% | **−62bp** |
| More Personal Computing | $54,052m | $54,649m | **−1.1%** | $14,386m | $14,166m | **26.6%** | 25.9% | **+69bp** |
| **Total** | **$331,839m** | **$281,724m** | **+17.8%** | **$155,237m** | **$128,528m** | **46.8%** | **45.6%** | **+116bp** |

Segment operating income FY2024 (restated basis): PBP **$59.7bn**, IC **$37.8bn**, MPC
**$12.0bn** **[P]** — sum $109.5bn ≈ reported $109,433m **[P]**.

**Three observations the headline misses:**

1. **Intelligent Cloud is the only segment whose margin went backwards** — down 62bp to
   **41.3%** **[C]**. This is exactly where AI infrastructure depreciation lands, and it is
   the first visible margin evidence of the capex cycle biting. It is a *small* decline, but
   it is the leading indicator and **it is going the wrong way while the other two segments
   expand.**
2. **Company-level margin expansion is carried by Productivity & Business Processes**,
   +215bp to **59.9%** **[C]**. M365 price/mix and Copilot attach are doing the heavy lifting
   that lets consolidated margin rise while cloud margin falls. **The consolidated margin
   story is healthier than the cloud margin story.**
3. **More Personal Computing is shrinking** — −1.1% for the year, **−4% in Q4** **[P]/[S]**.
   Windows, devices and gaming are in structural decline. At $54bn it is 16% of revenue and
   no longer a growth contributor.

### 4.2 Q4 FY2026 segments **[P]/[S]; margins [C]**

| Segment | Q4 revenue | YoY | Q4 op. income | Q4 op. margin |
|---|---|---|---|---|
| Productivity & Business Processes | $37.8bn | +14% | $21.9bn | 57.9% |
| Intelligent Cloud | $39.3bn | **+32%** | $15.9bn | 40.5% |
| More Personal Computing | $12.9bn | **−4%** | $2.7bn | 20.9% |
| **Total** | **$90.0bn** | **+18%** | **$40.6bn** | **45.1%** |

**Note the gap between Azure (+43%) and Intelligent Cloud (+32%)** — the non-Azure parts of
the segment (server products, Enterprise & Partner Services) are growing far more slowly or
shrinking. **Azure is doing essentially all the work.**

### 4.3 Azure, and the AI attribution — **the disclosure has been withdrawn**

**Disclosed [P]/[S]:**
- **Azure and other cloud services surpassed $100bn of revenue for the first time in FY2026**
  — the first absolute Azure figure at that granularity.
- Azure **+43% in Q4 FY2026**, an **acceleration** from +40% in Q3 **[S]**.
- Azure **~+41% for the full fiscal year** **[S]**.
- FY2025 comparison: Azure surpassed **$75bn**, **+34%** **[S]**.
- **Guided to accelerate further in H1 FY2027**, potentially **~45% in Q1 FY2027** **[S]**.

**What the brief asked for — how much of Azure growth management attributes to AI services —
is no longer disclosed. This is a disclosure-quality downgrade.**

In prior years Microsoft quantified AI's contribution to Azure growth in points. **I could
not find that split for any quarter of FY2026.** What was offered instead on the Q4 call
**[S]**:

- Acceleration attributed to **"efficiency gains across CPU and GPU fleet"**, shorter lead
  times to bring capacity online, and monetising those gains within the quarter.
- **Stronger-than-expected GitHub Copilot consumption** after a business-model change.
- **"Nearly 90% of Microsoft Cloud revenue now comes from customers outside the frontier AI
  labs"** — CFO Amy Hood **[S]**.

That last statistic is used as reassurance on concentration, and it is genuinely reassuring
on counterparty risk. **But note what it is not: it is not an AI-revenue attribution. A
qualitative narrative has replaced a quantitative disclosure.**

One quantified AI metric surfaced: an **AI annual revenue run-rate of $37bn as of Q3 FY2026,
+123% YoY** **[S]**. **Treat cautiously and do not model it** — search extraction, definition
unseen, and "run-rate" is not audited revenue.

**My read:** withdrawing the AI-contribution split at the exact moment the market most wants
it is a **minor negative mark on disclosure quality, not evidence of concealment.** The most
likely benign explanation is that AI and non-AI workloads have become genuinely inseparable
at the infrastructure level, which management's "efficiency gains across CPU and GPU fleet"
framing supports. **But the committee is entitled to note that the company stopped
publishing the number that would settle the argument.**

### 4.4 Copilot: **seat counts and anecdotes. Zero disclosed revenue.**

The brief asks me to be precise about the difference, so:

**Disclosed [P]/[S]:**
- **Microsoft 365 Copilot exceeded 30 million paid seats** at Q4 FY2026, up from ~20 million
  in April 2026 — **+50% in one quarter** **[S]**.
- GitHub Copilot consumption ran ahead of expectation after a business-model change **[S]**.

**NOT disclosed — and this is a complete absence, not a partial one:**
- **No Copilot revenue line. None.** Not in the press release, not in the segment tables, not
  as a supplemental metric.
- No Copilot ARR, gross margin, churn, or seat-retention rate.
- No disclosed **realised** price per seat.

**Third-party inference I explicitly reject:** one search result asserted "30 million paid
seats suggest a **$10 billion annual run rate**" **[S]**. **I will not carry that number.**
It is outside arithmetic, apparently list-price × seats. Enterprise Copilot is sold with
E3/E5 bundling, multi-year ramps and heavy volume discounting; **list price is close to
worthless as a revenue proxy.** A recent report in this firm had to retract an inference
built on an assumed input. I am not repeating that.

**What can be said honestly:** Copilot seat growth is real, fast and large in absolute terms.
**Its revenue contribution is unquantified by the company and unquantifiable by me.** The PBP
segment's **+215bp margin expansion on +15.9% revenue growth [C from P]** is the only hard
evidence that Copilot monetisation is working — and it is **indirect**. One independent
write-up characterised the quarter as a **"modest M365 AI revenue harvest"** **[S, headline
only — article not opened]**, a fair reflection of the gap between seat-count enthusiasm and
disclosed revenue.

---

## 5. The OpenAI relationship as a financial item

### 5.1 What it did to the P&L — an **$8.6bn** two-year swing

| FY | Impact on net income | Impact on diluted EPS |
|---|---|---|
| FY2025 | **−$3,620m** (net **losses**) **[S]** | **−$0.49** **[S]** |
| FY2026 | **+$4,963m** (net **gains**) **[P]** | **+$0.67** **[P]** |
| **Swing** | **+$8,583m** **[C]** | **+$1.16** **[C]** |

Against total FY2026 EPS growth of **$4.31** ($17.95 vs $13.64 **[P]**), the OpenAI swing is
**26.9%** **[C]**. **Slightly more than a quarter of Microsoft's headline EPS growth came
from a change in the accounting mark on a private company.**

**To Microsoft's credit, it excludes this from non-GAAP.** Non-GAAP FY2026 EPS is **$17.28**
(+22%) **[P]** = GAAP $17.95 − $0.67 **[C]**, confirming OpenAI is *the* non-GAAP adjustment.
FY2025 equivalent: $13.64 + $0.49 = **$14.13** **[C]** ⇒ **+22.3%** **[C]**, matching the
disclosed +22%. **The non-GAAP presentation on this item is clean and I have no complaint
about it** — worth saying, because it is the opposite of the usual adjusted-earnings abuse.

**Where it sits:** Other income (expense), net was **+$10,697m in FY2026** vs **−$4,901m in
FY2025** **[P]** — a **$15,598m swing** **[C]**, far larger than the OpenAI item alone. See §9;
it is the single biggest quality issue in the FY2026 income statement.

**Disclosure friction, noted:** third-party reporting states Microsoft disclosed a **~$4.7bn
"other, net" expense line with no itemised breakdown**, the bulk reflecting "net recognized
losses on equity method investments" **[S]**, and that in Q1 FY2026 Microsoft's share implied
an **~$11.5bn quarterly OpenAI loss** presented inside an aggregated line **[S,
headline-level]**. **I could not verify either against the filing.** What I can say with
confidence: **the OpenAI economics are visible only in aggregate, never as a standalone
disclosed line, which makes the item effectively unmodellable.** **[S]**

### 5.2 The stake, the commitment, and what is off balance sheet

From the October 2025 restructuring **[S]**:

- OpenAI completed conversion to for-profit **OpenAI Group PBC**.
- Microsoft holds **~27% on an as-converted basis**, **equity method** — down from ~32.5%
  pre-restructuring, on a stake reported at roughly **$135bn** of value against cumulative
  investment of ~**$13.8bn** **[S]**.
- **Total funding commitment $13bn**, of which **$11.8bn funded at 2026-03-31** **[S]** ⇒
  **~$1.2bn remaining committed but unfunded** **[C]**.
- OpenAI contracted to purchase an **incremental $250bn of Azure services** **[S]**.
- Microsoft **lost its right of first refusal** as OpenAI's compute provider **[S]**.
- IP rights to models and products **extended through 2032**, now including post-AGI models;
  any AGI declaration verified by an **independent expert panel** **[S]**.
- The **20% revenue share continues through 2030, subject to a cap** **[S]**. An April 2026
  revision reportedly **capped the revenue-share payments** — source (CNBC) blocked; **the
  cap amount is NOT OBTAINED**.

### 5.3 What it costs, what is exposed — my assessment

**In the P&L / on balance sheet:**
- Equity-method share of OpenAI results through "other income (expense), net" — **−$3,620m
  FY2025, +$4,963m FY2026 at the net income level** **[P]/[S]**. Volatile, non-cash,
  non-operating, **unforecastable**.
- Remaining unfunded commitment **~$1.2bn** **[C from S]** — trivial against $182.9bn of
  operating cash flow. **The funding commitment is not a balance-sheet risk.**

**Off balance sheet — the part that matters:**
- The **$250bn Azure purchase commitment** is a *customer* commitment **to** Microsoft, not an
  obligation **of** Microsoft. It is backlog, not a liability. **But it is a concentration**:
  a single counterparty, itself deeply lossmaking, contracted for an amount equal to **~75% of
  Microsoft's entire FY2026 revenue**, spread over years. Amy Hood's "nearly 90% of Microsoft
  Cloud revenue is from outside the frontier AI labs" **[S]** is precisely the rebuttal, and
  it is a good one.
- **The genuine asymmetry:** Microsoft is building physical, depreciating, 6-to-25-year assets
  partly against demand from a company whose solvency depends on continued private
  fundraising. **If OpenAI's funding environment tightens, Microsoft keeps the depreciation
  and loses the revenue.** That is the real OpenAI financial risk — **not the equity-method
  line and not the $13bn commitment.**

**Net judgement:** as a *financial statement* item, the OpenAI relationship is
**earnings-quality-negative and capital-risk-low**. It injects large unforecastable swings
into EPS (bad for statement quality) while actual capital at risk is small and the commercial
upside is contractually large.

---

## 6. Profitability — margins, ROE, ROIC

### 6.1 Four-year margin trend — **gross margin falling, operating margin rising**

**All inputs [P]; all ratios [C].**

| | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue | $211,915m | $245,122m | $281,724m | $331,839m |
| Revenue growth | — | +15.7% | +14.9% | **+17.8%** |
| Cost of revenue | $65,863m | $74,114m | $87,831m | $106,374m |
| Cost of revenue growth | — | +12.5% | +18.5% | **+21.1%** |
| **Gross margin %** | 68.9% | **69.8%** | 68.8% | **67.9%** |
| **Operating margin %** | 41.8% | 44.6% | 45.6% | **46.8%** |
| Effective tax rate | — | — | 17.6% | **19.4%** |
| **Net margin %** | 34.1% | 36.0% | 36.2% | **40.3%** |

FY2026 opex detail **[P]/[C]**: R&D $35,562m (**10.7%** of revenue, +9.5% YoY);
S&M $26,710m (**8.0%**, +4.1%); G&A $7,956m (**2.4%**, +10.1%).
FY2025: 11.5% / 9.1% / 2.6%. **Total opex fell from 23.2% to 21.1% of revenue [C].**

**The key structural fact, and the most important profitability insight in this report:**

- **Gross margin has fallen 182bp from its FY2024 peak** to 67.9%. Cost of revenue grew
  **+21.1%** against revenue +17.8% **[C]** — AI infrastructure depreciation and power, partly
  offset by fleet efficiency. Management confirmed Microsoft Cloud gross margin fell to
  **66%** in Q3 FY2026 **[S]**, and company gross margin was **69%** in Q1 FY2026, down YoY
  **[S]**.
- **Operating margin rose anyway**, because **every opex line grew slower than revenue.**

**Microsoft is paying for the AI capex cycle out of operating leverage on SG&A and R&D, not
out of pricing.** That worked, and worked well, in FY2026. **But it is a finite resource** —
you can only take opex from 23.2% to 21.1% of revenue so many times. **Once opex leverage is
exhausted, gross margin erosion flows straight through to operating margin. Watch the gross
margin line, not the operating margin line.**

**Net margin +418bp to 40.3% materially overstates the improvement** — a large part is the
"other income" swing (§9), not operations.

### 6.2 ROE — **excellent, but past its peak and the denominator is inflating**

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Net income | $88,136m **[P]** | $101,832m **[P]** | $133,749m **[P]** |
| Equity, period end | $268,477m **[P]** | $343,479m **[P]** | $442,387m **[P]** |
| **ROE (average equity)** | **37.1%** **[C]** | **33.3%** **[C]** | **34.0%** **[C]** |
| ROE (ending equity) | 32.8% **[C]** | 29.7% **[C]** | 30.2% **[C]** |

*(FY2023 equity $206,223m [P] used for the FY2024 average.)*

**ROE peaked in FY2024 at 37.1% and is 310bp lower today** — despite FY2026 being a much
better operating year. **Cause: equity grew +28.8% in FY2026 [C]**, far faster than revenue,
because retained earnings compound much faster than buybacks retire them. **A rising equity
base mechanically suppresses ROE.** 34% remains outstanding in absolute terms, but **do not
read future ROE decline as operational deterioration without checking the denominator.**

### 6.3 ROIC — **26.5%, and structurally compressing**

Method: **NOPAT ÷ (total debt incl. finance leases + equity − cash & short-term
investments)**, ending balances.

| Component | FY2026 |
|---|---|
| Operating income | $155,237m **[P]** |
| Effective tax rate | 19.4% **[C]** |
| **NOPAT** | **$125,121m** **[C]** |
| Total debt + finance lease liabilities | $106,888m **[S]** |
| Total stockholders' equity | $442,387m **[P]** |
| Less cash & equivalents | $(20,935)m **[P]** |
| Less short-term investments | $(55,908)m **[P]** |
| **Invested capital** | **$472,432m** **[C]** |
| **ROIC** | **26.5%** **[C]** |

**Confidence:** the debt figure is the only **[S]** input; everything else **[P]**. A ±$10bn
error in debt moves ROIC by ~±0.6pp, so **the conclusion is robust to that uncertainty.**

**26.5% ROIC is very strong** — roughly 3.5x any plausible cost of capital.

**The direction, stated carefully.** I could **not** compute a comparable FY2025 ROIC because
FY2025 finance lease liabilities were not obtained (§12). From the components I do have:
**total assets +22.5% to $758,376m [C from P], equity +28.8%, finance lease liabilities from
$11.75bn (2021) to $62.3bn (2026) [S] — while NOPAT grew ~21%. Arithmetically, ROIC must be
compressing.** **I state that as an inference from directional components, not a computed
number** — exactly the kind of gap-filling the brief warned against, so it is labelled
inference and the FY2025 ROIC sits in the NOT OBTAINED register.

---

## 7. Balance sheet & debt profile

### 7.1 Four-year balance sheet **[P]; changes [C]**

| | 2023-06-30 | 2024-06-30 | 2025-06-30 | 2026-06-30 | FY26 Δ |
|---|---|---|---|---|---|
| Cash & equivalents | $34,704m | $18,315m | $30,242m | **$20,935m** | −30.8% |
| Short-term investments | $76,558m | $57,228m | $64,323m | **$55,908m** | −13.1% |
| **Cash + ST investments** | **$111,262m** | **$75,543m** | **$94,565m** | **$76,843m** | **−18.7%** |
| Accounts receivable, net | $48,688m | $56,924m | $69,905m | **$80,876m** | +15.7% |
| Inventories | — | — | $938m | **$1,397m** | **+48.9%** |
| **Total assets** | **$411,976m** | **$512,163m** | **$619,003m** | **$758,376m** | **+22.5%** |
| Long-term debt | $41,990m | $42,688m | $40,152m | **$31,067m** | **−22.6%** |
| Current portion of LTD | $5,247m | $2,249m | $2,999m | **$9,227m** | **+207.7%** |
| Short-term unearned revenue | $50,901m | $57,582m | $64,555m | **$72,965m** | +13.0% |
| Long-term unearned revenue | $2,912m | $2,602m | $2,710m | **$2,747m** | +1.4% |
| Total liabilities | — | — | $275,524m | **$315,989m** | +14.7% |
| **Total stockholders' equity** | **$206,223m** | **$268,477m** | **$343,479m** | **$442,387m** | **+28.8%** |

### 7.2 The debt profile — **bond debt shrinking, lease debt exploding**

| | 2021 | 2023-06-30 | 2024-06-30 | 2025-06-30 | 2026-06-30 |
|---|---|---|---|---|---|
| Long-term debt (ex-current) | $50,074m **[S]** | $41,990m **[P]** | $42,688m **[P]** | $40,152m **[P]** | **$31,067m** **[P]** |
| Current portion of LTD | — | $5,247m **[P]** | $2,249m **[P]** | $2,999m **[P]** | **$9,227m** **[P]** |
| **Bond debt subtotal** | — | **$47,237m** **[C]** | **$44,937m** **[C]** | **$43,151m** **[C]** | **$40,294m** **[C]** |
| **Finance lease liabilities** | **$11,750m** **[S]** | — | — | not obtained | **$62,304m** **[S]** |
| **Total debt + finance leases** | — | — | — | not obtained | **$106,888m** **[S]** |
| Weighted-avg effective rate on debt + finance leases | — | — | — | — | **4.52%** **[S]** |

**This is the most under-appreciated item on Microsoft's balance sheet.** Anyone reading only
the "long-term debt" line sees it fall from **$41,990m (FY23) to $31,067m (FY26)** **[P]** and
concludes Microsoft is deleveraging. **It is not.** Traditional bond debt is being allowed to
mature and roll off — down **$6,943m over three years [C]** — while **finance lease
liabilities have grown 5.3x since 2021 to $62,304m [S]**. Finance leases are debt in
substance: fixed obligations, secured against specific assets, with an interest component.

**Total debt including finance leases is $106,888m [S], of which finance leases are 58%
[C].** **The composition of Microsoft's leverage has fundamentally changed, and the change is
invisible if you read only the headline debt line.** And after FY2027, a further slice moves
*off* the balance sheet entirely into operating leases (§2.2).

**Coverage and capacity — where Microsoft is genuinely unassailable [C], rate input [S]:**

| Metric | FY2026 |
|---|---|
| Operating income ÷ total debt + leases | $155,237m / $106,888m = **1.45x** — operating income **exceeds** total debt by 45% |
| Total debt + leases ÷ operating cash flow | $106,888m / $182,935m = **0.58x** — **under 7 months of OCF** retires all debt |
| Approx. annual interest at 4.52% | ~$4,831m **[E]** |
| **Interest coverage** | **~32x** **[E]** |
| Net debt (debt + leases − cash & ST inv.) | $106,888m − $76,843m = **$30,045m** |
| **Net debt ÷ operating cash flow** | **0.16x** **[C]** |

**Verdict: the debt is not a risk. This is the A+ section of an A− report.** ~32x interest
coverage **[E]**, net debt at 0.16x operating cash flow, and top-tier credit. Even a doubling
of finance lease liabilities leaves coverage comfortable.

**What I could NOT obtain, and it matters unevenly:** the **maturity schedule** by year, the
**coupon-by-tranche detail**, and the **operating lease commitment schedule**. At ~32x
coverage the maturity ladder is a **low-consequence** gap. **The operating lease schedule is
not** — it is about to become the fastest-growing off-balance-sheet obligation. §12.

### 7.3 The cash buffer is being consumed

Cash + short-term investments fell **18.7% to $76,843m** **[C from P]** and is **31% below the
FY2023 level of $111,262m** **[C]**. Microsoft is funding capex from operating cash flow *and*
the securities portfolio, while returning $48.7bn to shareholders and letting bond debt roll
off. Entirely affordable and internally consistent — **but the flexibility buffer is
shrinking.** If capex rises again in FY2027 as guided, either the balance sheet draws down
further, buybacks moderate, or debt issuance resumes. **Watch for renewed large bond issuance
in FY2027 — it would be the tell that internal funding has reached its limit.** **[E — my
inference.]**

---

## 8. Capital returns: buybacks and dividends vs SBC dilution

| FY | Buybacks | Dividends | Total returned | FCF | Payout of FCF | SBC |
|---|---|---|---|---|---|---|
| FY2023 | $22,245m **[P]** | $19,800m **[P]** | $42,045m **[C]** | $59,475m **[C]** | 70.7% **[C]** | $9,611m **[P]** |
| FY2024 | $17,254m **[P]** | $21,771m **[P]** | $39,025m **[C]** | $74,071m **[C]** | **52.7%** **[C]** | $10,734m **[P]** |
| FY2025 | $18,420m **[P]** | $24,082m **[P]** | $42,502m **[C]** | $71,611m **[C]** | 59.4% **[C]** | $11,974m **[P]** |
| FY2026 | **$22,271m** **[P]** | **$26,445m** **[P]** | **$48,716m** **[C]** | **$66,987m** **[C]** | **72.7%** **[C]** | $12,405m **[P]** |

**Payout of FCF rose from 52.7% to 72.7% in two years [C]** — not because returns grew
aggressively (+24.8% over two years) but **because FCF fell**. Still covered, but the cushion
has thinned considerably. **On FCF net of SBC ($54,582m [C]), the FY2026 payout ratio is
89.3% [C]** — that is the honest number, and it is close to fully distributing cash
generation.

### Share count: the buyback is barely outrunning dilution

| | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Weighted-avg diluted shares **[P]** | 7,472m | 7,469m | 7,465m | **7,453m** |
| Change vs prior year **[C]** | — | −0.04% | −0.05% | **−0.16%** |
| Buyback spend **[P]** | $22,245m | $17,254m | $18,420m | $22,271m |
| SBC expense **[P]** | $9,611m | $10,734m | $11,974m | $12,405m |
| **Buyback net of SBC [C]** | $12,634m | $6,520m | $6,446m | **$9,866m** |

**Over FY2024–FY2026 Microsoft spent $57,945m on buybacks and reduced the diluted share
count by 16m shares — 0.21%.** **[C from P]**

At an illustrative average repurchase price of ~$400 across the three years **[E — Q4 FY26
repurchases were disclosed in a range of $396.19–$416.81 [S]; the full-period average is NOT
OBTAINED]**, $57.9bn retires roughly **145m shares, ~1.94%** of the base **[C, E-input]**. The
count fell 0.21%. **Therefore roughly 89% of the gross buyback over three years was consumed
offsetting equity issuance** **[C, E-input — flagged as dependent on the estimated price].**

**Stated plainly: the buyback is a dilution-offset programme, not a shareholder-return
programme.** In FY2026, **$12.4bn of the $22.3bn is economically employee compensation being
recycled**. The genuine return to shareholders is the **$26,445m dividend** plus **~$9.9bn of
net buyback = ~$36.3bn [C]**, against a $48.7bn headline — **54% of FCF, not 73%.**

**In fairness:** this is the norm across mega-cap technology, Microsoft's SBC intensity is
**falling** (§3.2), the dividend has grown for two decades, and net buyback in FY2026 was the
highest since FY2023. **This is a fair capital-returns programme, not a bad one.** But the
headline overstates economic reality by roughly a third and **the committee should use
$36.3bn.**

---

## 9. Accounting red flags & quality screen

Screened against the standard four: earnings vs operating cash flow, working capital vs
revenue, capitalisation games, adjusted-figure hygiene — over four years, not one quarter.

### 🟢 CLEAN — Earnings vs operating cash flow
Net income **+31.3%**, operating cash flow **+34.3%** **[C from P]**. **OCF grew faster than
earnings.** Cash conversion (OCF ÷ net income): **1.21x → 1.35x → 1.34x → 1.37x** across
FY2023–FY2026 **[C]** — stable, improving, and well above 1.0x throughout. **There is no
earnings-quality divergence at the operating-cash-flow line.** This is the most reassuring
test in the screen and Microsoft passes it cleanly across four years.

### 🟡 WATCH — Receivables (a FY2025 divergence that FY2026 corrected)

| FY | AR | AR growth | Revenue growth | **DSO** **[C]** |
|---|---|---|---|---|
| FY2023 | $48,688m | — | — | **83.9d** |
| FY2024 | $56,924m | +16.9% | +15.7% | **84.8d** |
| FY2025 | $69,905m | **+22.8%** | **+14.9%** | **90.6d** |
| FY2026 | $80,876m | +15.7% | **+17.8%** | **89.0d** |

**In FY2025 receivables outgrew revenue by ~790bp and DSO deteriorated 5.8 days [C].** That
is a real divergence and it would have been a flag had this report been written a year ago.
**FY2026 partially corrected it** — AR grew *slower* than revenue and DSO improved 1.6 days.

**But DSO is still ~5 days worse than FY2023 [C]**, i.e. roughly **$4.7bn of revenue [C,
illustrative]** now sits in receivables that would not have under the FY2023 collection
profile. Most likely explanation is mix toward large multi-year enterprise AI contracts with
longer billing cycles — benign, and consistent with the deferred-revenue pattern below.
**Flagged WATCH rather than CLEAN because the FY2023 level has not been recovered.** I would
not have caught this from a single year, which is why the four-year view matters.

### 🟡 MINOR — Inventories
**+48.9% to $1,397m vs revenue +18%** **[C from P]** — growing 2.7x faster than revenue. **At
0.42% of revenue this is immaterial in absolute terms**, most likely AI hardware and device
components. Flagged for completeness, not concern. Only matters if it persists several more
quarters.

### 🟢 CLEAN (downgraded from WATCH on four-year evidence) — Deferred revenue

| FY | Short-term unearned revenue | Growth | Revenue growth | Gap |
|---|---|---|---|---|
| FY2024 | $57,582m | +13.1% | +15.7% | −260bp |
| FY2025 | $64,555m | +12.1% | +14.9% | −280bp |
| FY2026 | $72,965m | +13.0% | +17.8% | −480bp |

Deferred revenue has grown slower than revenue **for three consecutive years [C from P]**.
**That consistency is what makes it benign.** A sudden one-year divergence would signal
weakening forward commitments; a stable three-year pattern is a **structural mix effect** —
Azure consumption revenue is recognised as used and never sits in unearned revenue the way a
prepaid M365 licence does, so a steady mix shift toward consumption mechanically depresses
this ratio every year. **The FY2026 gap did widen to 480bp**, which is why I note it, but
against three years of the same directional pattern I do not treat it as deterioration.

**Caveat that keeps this from being fully settled:** I could **not** obtain **commercial
bookings growth** or **commercial remaining performance obligation (RPO)** — the two
disclosures that would confirm it, and the ones that would size the $250bn OpenAI Azure
commitment. **Their absence is a real limitation of this report. §12.**

### 🔴 **FLAG — "Other income (expense), net" is doing far too much work**

| | FY2025 | FY2026 | Swing |
|---|---|---|---|
| Operating income | $128,528m | $155,237m | +$26,709m (**+20.8%**) |
| **Other income (expense), net** | **$(4,901)m** | **+$10,697m** | **+$15,598m** |
| Income before income taxes | $123,627m | $165,934m | +$42,307m (**+34.2%**) |

**[P] inputs; [C] swings.**

**36.9% of the growth in pre-tax income came from a single non-operating line [C].** Pre-tax
income grew **+34.2%** while operating income grew **+20.8%**. That entire gap is "other
income".

Known contents: **OpenAI net gains** (+$4,963m at the net-income level **[P]**) and a **$3.2bn
gain on the Anthropic investment in Q4** **[P]**. These are **unrealised marks on
private-company equity stakes** — non-cash, non-operating, and demonstrably reversible: OpenAI
itself swung from −$3,620m to +$4,963m in twelve months.

**The sub-flag that concerns me most — labelled honestly as inference:**

> Microsoft's non-GAAP EPS of **$17.28** is GAAP **$17.95** less the **$0.67** OpenAI item
> **[P]/[C]** — that is the *only* stated adjustment. **The $3.2bn Anthropic gain therefore
> appears to remain inside non-GAAP EPS.** At the FY26 effective rate of 19.4%, $3.2bn pre-tax
> is ~$2.58bn after tax ≈ **$0.35 per diluted share, ~2% of non-GAAP EPS** **[C]**.
>
> **This is [E] — inference from an arithmetic reconciliation, not from an accounting policy
> note I read.** It is possible Anthropic is handled differently, that the $3.2bn is
> post-tax, or that offsetting items exist. **Someone with 10-K access must confirm before
> this is used.** If confirmed, it is a genuine inconsistency: **excluding one
> private-company mark from non-GAAP while including another.**

### 🟡 WATCH — Two earnings-favourable estimate changes in four years
Server/network life 4y → 6y (2022); data centre and office building life 15y → 25y (FY2027)
**[S]**. §2.2. **Each is individually defensible** — 25-year building lives are ordinary.
**I am not calling this a red flag.** I record it because the brief asked, because both
changes were earnings-favourable, and because both landed while depreciation was accelerating.

### 🟡 WATCH — Capex redefinition reduces reported capex without reducing spending
§2.2. **Nothing improper is happening** — the treatment follows the lease standard. But it
**will make FY2027 capex and FCF optically better than the economics**, and anyone comparing
FY2027 capex to FY2026 capex without adjusting is comparing different things. **[E] for the
forward effect.**

### 🟢 CLEAN — Share count creep
Diluted shares **fell** in each of the last three years **[P]**. SBC growth +3.6% vs revenue
+17.8% **[C]**. **No creep.** (§8's point that the buyback largely *funds* the offset is a
capital-allocation observation, not an accounting flag.)

### 🟢 CLEAN — Tax
Effective rate **rose** from 17.6% to 19.4% **[C from P]**. Earnings growth was achieved
**despite** a 177bp tax headwind. **No tax-rate management signature.**

### Screen summary

| Test | Result |
|---|---|
| Earnings vs operating cash flow (4yr) | 🟢 **CLEAN** — OCF grew faster; conversion 1.21x→1.37x |
| Receivables vs revenue (4yr) | 🟡 **WATCH** — FY25 divergence, FY26 corrected, DSO still +5d vs FY23 |
| Inventories vs revenue | 🟡 MINOR — immaterial at 0.42% of revenue |
| Deferred revenue vs revenue (3yr) | 🟢 CLEAN — consistent 3-year mix effect, not deterioration |
| **"Other income" quality** | 🔴 **FLAG — 36.9% of pre-tax growth from marks** |
| Adjusted-figure hygiene | 🟡 WATCH — Anthropic gain apparently not excluded **[E]** |
| Estimate changes | 🟡 WATCH — two earnings-favourable in four years |
| Capex definition | 🟡 WATCH — optical reduction, spending unchanged |
| Share count creep | 🟢 CLEAN |
| Tax rate management | 🟢 CLEAN |

**One red flag, four watch items, four clean, one minor.** **The core operating statements
are honest.** Every issue sits either **below the operating income line** (marks, other
income) or **in the notes and forward guidance** (estimates, lease definitions). **Nothing I
found casts doubt on the $155,237m of operating income or the $182,935m of operating cash
flow.** That distinction keeps this an A− rather than a B.

---

## 10. Anti-anchoring (L-003): both cases at full strength

The house has graded one Chinese small-cap D+ and one A−. **Neither has any bearing on
Microsoft.** I built both cases from the numbers and then asked which one the evidence
supports.

### The bull case at full strength — **and I found nearly all of it**

> A company growing revenue **17.8% at $332bn scale**, **expanding operating margin 116bp to
> 46.8% while simultaneously absorbing a 510bp increase in D&A intensity**, converting net
> income to operating cash flow at **1.37x** (improving four years running), earning **26.5%
> ROIC** and **34% ROE**, with **~32x interest coverage**, **net debt of 0.16x operating cash
> flow**, and operating income that **exceeds total debt including finance leases by 45%**.
> Receivables grew slower than revenue. SBC intensity is *falling*. The tax rate *rose*. The
> share count fell. Cash flow grew faster than earnings in every year examined.
>
> The largest business unit **accelerated** from 40% to 43% growth in the most recent quarter,
> passed **$100bn** of annual revenue, and is guided to accelerate again. **The capex is not a
> bug** — it is being deployed against demand that is visibly materialising, and the proof is
> that the segment absorbing the depreciation is *growing faster*, not slower. FCF is down
> because the company is choosing to build. **Any company that could stop building tomorrow
> and print ~$180bn of FCF does not have a cash-flow problem.**

**How much did I find? Almost all of it.** Every figure above is **[P]** or **[C] from [P]**
except Azure growth rates and the interest rate **[S]**. **The bull case is well supported by
the audited-equivalent statements.** This is the strongest set of financials I have examined
for this firm, and it belongs on the record **before** the bear paragraph, because it is the
better-evidenced of the two.

### The bear case at full strength — **and I found the setup, not the event**

> Capex has gone from **13.3% of revenue to 34.9%** in three years and from **32.1% to 63.4%
> of operating cash flow**. **Free cash flow has fallen two years running** and is **9.6%
> below its FY2024 peak** while revenue grew 35%. FCF margin collapsed **1,000bp to 20.2%**,
> and on an SBC-adjusted basis Microsoft distributes **89% of cash generation**. **Gross
> margin has fallen 182bp from peak** and only opex leverage — a finite resource, already
> down 210bp — holds the operating margin up. **Intelligent Cloud, the segment doing all the
> growing, is the one segment whose margin went backwards.**
>
> Meanwhile **26.9% of EPS growth and 36.9% of pre-tax income growth came from non-operating
> marks** on private AI companies, one of which swung **$8.6bn** in a year. **Finance-lease
> debt has grown 5.3x since 2021** while the headline debt line falls, disguising the leverage
> build. The company has **withdrawn the disclosure** quantifying AI's contribution to Azure
> growth, **discloses no Copilot revenue at all** after three years of promotion, has
> **extended depreciable lives twice in four years** in earnings-favourable directions, and
> has just **redefined capex** so FY2027 will look better than the economics warrant.

**How much did I find? The setup, comprehensively. The trigger, not at all.** Every capex,
FCF, margin, leverage and disclosure item above is verified **[P]**/**[C]**. **What is missing
is the deceleration.** The bear case is an argument about a 30%-compounding depreciation base
meeting a decelerating revenue line — **and in FY2026 the revenue line accelerated.** Until
Azure growth breaks below roughly the mid-20s, **the bear case is a loaded gun that has not
been fired.**

**My honest position: this is a well-constructed FY2027–FY2028 risk, not an FY2026
diagnosis.** I will not grade the company down today for a deterioration I could not find in
the statements. **Nor will I pretend the FCF trend is fine — it is the clearest warning signal
in the accounts and it has now printed twice.**

**What would change my mind, specifically:**

| Trigger | Reading |
|---|---|
| Azure growth < 25% for two consecutive quarters | **Bear case activates** — depreciation outruns revenue |
| Intelligent Cloud margin down >200bp YoY | Depreciation is winning |
| FY2027 FCF falls a **third** consecutive year | Structural, not cyclical |
| Gross margin down >150bp with opex ratio flat | **Opex leverage exhausted** — erosion hits operating margin |
| Server/network life extended **beyond 6 years** | Serious earnings-quality red flag |
| DSO deteriorating again toward 95d+ | FY2025 receivables divergence was not a one-off |
| Renewed large bond issuance | Internal funding limit reached |
| FY2027 FCF "recovers" while operating leases balloon | **Definitional — do not credit it** |

---

## 11. Financial score: **79 / 100 — Grade A−**

### 11.1 Scorecard

| Component | Weight | Score | Rationale |
|---|---|---|---|
| **Profitability & margin trend** | 20 | **17** | 46.8% operating margin, +116bp; four straight years of operating-margin expansion. **−3** for gross margin down 182bp from peak and Intelligent Cloud margin down 62bp — the erosion is real and located exactly where the capex is. |
| **Cash generation** | 25 | **16** | OCF +34.3%, conversion 1.37x and improving four years running — excellent. **−9** because **FCF fell for the second consecutive year** to $66,987m, FCF margin collapsed 1,000bp to 20.2%, and SBC-adjusted payout is 89%. **Largest single deduction, and deliberate.** |
| **Returns on capital** | 15 | **13** | 26.5% ROIC, 34.0% ROE — outstanding. **−2** for ROE 310bp below its FY2024 peak, an invested-capital base compounding faster than NOPAT, and FY2025 ROIC not computable for comparison. |
| **Balance sheet & debt** | 15 | **14** | Net debt 0.16x OCF, ~32x coverage, operating income exceeds total debt by 45%. **−1** for the finance-lease build (5.3x since 2021) being invisible in the headline debt line, and the unobtained maturity and operating-lease schedules. |
| **Earnings quality & accounting** | 20 | **13** | Core statements clean over four years: OCF > net income throughout, no share creep, tax rate rose, deferred-revenue pattern benign. **−7** for the "other income" red flag (36.9% of pre-tax growth from marks), the apparent non-exclusion of the Anthropic gain from non-GAAP **[E]**, the FY2025 receivables divergence, two earnings-favourable estimate changes, and the capex redefinition. |
| **Disclosure quality** | 5 | **3** | Statements clear and IR publishes them accessibly — genuinely better than most. **−2** for withdrawing the AI-contribution-to-Azure split and **zero disclosed Copilot revenue** after three years of promotion. |
| **Data-completeness deduction** | — | **−3** | No 10-K/10-Q opened (SEC blocked). Useful-life note, RPO/bookings, maturity ladder and operating-lease schedule unobtained. **I graded the statements, not the notes**, and an honest deduction reflects that. |
| **TOTAL** | **100** | **79** | **A−** |

### 11.2 Calibration

0100.HK **D+ 48**; 6160.HK **A− 82** (house best). **MSFT at 79 sits just below 6160.HK** and
far above 0100.HK. **I considered 84** — profitability, returns and the balance sheet arguably
justify it. **I held at 79 for one reason: a company whose free cash flow has declined two
years in a row, and where over a quarter of EPS growth came from marking private equity
stakes, cannot outscore a name whose cash generation was unambiguous.** The FCF trend and the
"other income" flag are precisely what cost MSFT the A.

**Conditional revisions:**
- If the FY2026 10-K confirms **(a)** server/network life unchanged at 6 years **and (b)** the
  Anthropic gain *is* excluded from non-GAAP → **83–84 (A−/A)**.
- If it shows **a further life extension**, an aggressive capitalisation policy, or a
  materially larger unquantified operating-lease commitment → **72–74 (B)**.

### 11.3 The three numbers that matter most

1. **FCF $66,987m — −6.5%, second consecutive annual decline, −9.6% from the FY2024 peak
   [C from P].** The thesis lives or dies here.
2. **Capex at 63.4% of operating cash flow [C from P]** (FY2023: 32.1%). How much of the
   machine is being reinvested rather than returned — it has doubled in three years.
3. **D&A +30.9% vs revenue +17.8% [C from P].** The depreciation tail is already outrunning
   revenue, and the FY2026 $115.9bn cohort has not yet fully landed.

### 11.4 Forward guidance — recorded with a warning

For context only, all **[S]**, none verified against a document I opened:

- **Q1 FY2027 revenue guidance ~$89.85–90.95bn**.
- **Azure guided to accelerate further in H1 FY2027, potentially ~45% in Q1 FY2027**.
- **Calendar-2026 capex maintained at ~$175bn** (post-reclassification).
- FY2027 operating margin guided **~1 point higher than FY2026**, with commentary elsewhere
  suggesting margins decline slightly as AI infrastructure and R&D investment continues.
  **These two statements are in tension in the extracts I have and I could not reconcile them
  — do not rely on either.**

> **Discarded figure — recorded for audit.** A widely-repeated "**FY2027 capex guidance of
> $255–260bn**" appeared in my search results **sourced only to `tradingkey.com`**, which is
> **blacklisted firm-wide**. **I have not adopted it and it is not cited.** It is also
> internally inconsistent with the ~$175bn calendar-2026 figure without a reconciliation I
> could not obtain. **If any committee member encounters that number elsewhere, it did not
> come from this report and it is unverified.**

---

## 12. NOT OBTAINED register

Explicit list of everything I could not verify. **Nothing below was filled from memory.**

### Blocking cause
`www.sec.gov`, `microsoft.gcs-web.com`, `www.stock-analysis-on.net`, `www.cnbc.com`,
`www.fool.com`, `news.alphastreet.com`, `deepquarry.substack.com`, `www.investing.com` — **all
EGRESS_BLOCKED**. `finance.yahoo.com`, `stockanalysis.com`, `businesswire.com` blocked in
prior sessions. `tradingkey.com` blacklisted. **No 10-K or 10-Q was opened.** The FY2026
Annual Report URL returned 404.

### Priority 1 — would change the grade

| Item | Why it matters | Status |
|---|---|---|
| **Server & network equipment useful life in the FY2026 10-K** | Directly asked in the brief. My 6-year working assumption is **[E]**. A change in either direction is material to EPS and to the quality grade. | **UNVERIFIED — highest priority** |
| **Quantified P&L effect of the FY2027 15y→25y building-life extension** | Management says "minimal benefit to FY27 operating income" **[S]**; I could neither verify nor size it. | **NOT OBTAINED** |
| **Operating lease commitment schedule (post-reclassification)** | Becomes the fastest-growing off-balance-sheet obligation from FY2027. **The largest unquantified item in this report.** | **NOT OBTAINED** |
| **Whether the $3.2bn Anthropic gain is excluded from non-GAAP EPS** | The §9 red-flag sub-item rests entirely on inference **[E]**. | **INFERRED, UNVERIFIED** |

### Priority 2 — would improve precision

| Item | Status |
|---|---|
| Commercial bookings growth and **commercial RPO / backlog**, FY2026 | **NOT OBTAINED** — would settle the deferred-revenue question and size the $250bn OpenAI commitment |
| Debt **maturity ladder** by year; coupon by tranche | **NOT OBTAINED** (low consequence at ~32x coverage) |
| FY2025 finance lease liabilities → blocks a computed FY2025 ROIC comparison | **NOT OBTAINED** |
| Official FY2026 **"capex including finance leases"** total (my ~$144bn is **[E]**) | **NOT OBTAINED** |
| Full-period average share repurchase price (only a Q4 FY26 range $396.19–$416.81 **[S]**) | **NOT OBTAINED** — §8's "~89% of buyback offsets dilution" depends on this estimate |
| **PP&E gross/net by asset class** — needed to size the depreciation tail properly | **NOT OBTAINED** — forces §2.4 to remain illustrative |
| Azure absolute quarterly revenue (only the ">$100bn annual" milestone) | **NOT DISCLOSED by company** |
| **AI-services contribution to Azure growth, in points** | **NOT DISCLOSED by company in FY2026** — withdrawn disclosure |
| **Copilot revenue, ARR, churn or realised ASP** | **NOT DISCLOSED by company** — seat counts only |
| FY2024 segment *revenue* on the restated basis (operating income obtained) | **NOT OBTAINED** |
| Cap amount on the OpenAI revenue share (April 2026 revision) | **NOT OBTAINED** — CNBC blocked |
| Microsoft Cloud gross margin % for Q4 FY2026 (Q1 69%, Q3 66% are **[S]**) | **NOT OBTAINED** |
| Reconciliation of the two conflicting FY2027 operating-margin statements | **NOT OBTAINED** — §11.4 |

### Figures deliberately **rejected**, not adopted

- **"30m Copilot seats ⇒ ~$10bn ARR"** **[S]** — third-party list-price arithmetic; enterprise
  bundling and discounting make it unreliable (§4.4). **Rejected.**
- **"FY2027 capex $255–260bn"** — sourced only to **blacklisted `tradingkey.com`**.
  **Rejected and recorded (§11.4).**
- **"AI annual revenue run-rate $37bn, +123% YoY (Q3 FY26)"** **[S]** — quoted with an explicit
  warning; definition unseen, not audited revenue. **Do not model.**

---

## Research-only notice

This is a financial-statement analysis. **It contains no recommendation, target price or
position sizing.** Valuation is 𢦀鳩仔's mandate; the moat question is 菲比斯's; management
quality is Peter's. **The Investment Committee and the Owner decide.**

---

## Sources

**Primary — pages actually opened [P]:**
- [Microsoft FY26 Q4 Press Release & Webcast — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) — FY2026/FY2025 income statement, balance sheet, cash flow, segments
- [Microsoft FY24 Q4 Income Statements — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2024-q4/income-statements) — FY2024/FY2023 income statement
- [Microsoft FY24 Q4 Balance Sheets — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2024-q4/balance-sheets) — FY2024/FY2023 balance sheet
- [Microsoft FY24 Q4 Cash Flows — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2024-q4/cash-flows) — FY2024/FY2023 cash flow statement
- [Microsoft 2025 Annual Report](https://www.microsoft.com/investor/reports/ar25/index.html) — FY2025/FY2024 segment operating income

**Search extractions — pages not opened [S]:**
- [Microsoft Cloud and AI strength fuels fourth quarter results — Microsoft Source](https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/)
- [Microsoft FY2026 Q4 Earnings Conference Call — Investor Relations](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- [Microsoft FY26 Q3 Press Release — Investor Relations](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast)
- [Microsoft holds the line on AI spending plans — CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/)
- [Microsoft Capex Tracker — Hallucination Yield](https://www.hallucinationyield.com/research/microsoft-capex/)
- [Microsoft anticipates $3.3bn savings by extending server life — Computer Weekly](https://www.computerweekly.com/news/252523221/Microsoft-anticipates-33bn-savings-by-extending-server-life)
- [Accounting policy changes boost tech earnings — Hudson Labs](https://www.hudson-labs.com/blog/accounting-policy-changes-boost-tech-earnings)
- [Microsoft's recent $68 billion in physical assets additions — Epoch AI](https://epoch.ai/data-insights/microsoft-ppe-breakdown)
- [The Useful Life Question — Shitty Situations](https://shittysits.substack.com/p/the-useful-life-question)
- [Microsoft Corp. — Analysis of Debt — Stock Analysis on Net](https://www.stock-analysis-on.net/NASDAQ/Company/Microsoft-Corp/Analysis/Debt) *(search extraction only — domain blocked on fetch)*
- [Microsoft gets 27% stake in OpenAI, and a $250B Azure commitment — GeekWire](https://www.geekwire.com/2025/microsoft-secures-27-stake-in-openai-in-new-deal-with-commitment-for-250b-in-azure-usage/)
- [The next chapter of the Microsoft–OpenAI partnership — Official Microsoft Blog](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
- [OpenAI completes for-profit move, Microsoft given 27% stake — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/openai-completes-for-profit-move-microsoft-given-27-stake-and-250bn-azure-contract-but-no-longer-has-cloud-right-of-first-refusal/)
- [Microsoft and Its OpenAI Losses — Calcbench](https://www.calcbench.com/blog/post/blogger7889213530921195705/Microsoft-and-Its-OpenAI-Losses)
- [Microsoft obscures OpenAI's $11.5 billion loss — Windows Central](https://www.windowscentral.com/artificial-intelligence/openai-chatgpt/microsoft-obscures-openais-usd11-5-billion-loss)
- [Microsoft Q4 FY2026: AI Demand Accelerates Azure and Enterprise Growth — Futurum](https://futurumgroup.com/insights/microsoft-q4-fy-2026-ai-demand-accelerates-azure-and-enterprise-growth/)
- [Microsoft's cloud brings rain of revenue but modest M365 AI revenue harvest — The Register](https://www.theregister.com/software/2026/07/30/microsoft-earnings-q4-26-cloud-brings-revenue-rain/5280798)
- [Microsoft spent $11.1bn on data center leases alone in Q1 2026 — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/microsoft-spent-111bn-on-data-center-leases-alone-in-q1-2026/)
- [Microsoft Q3 FY2026: The $190B Capex Plan That Repriced AI — Global Data Center Hub](https://www.globaldatacenterhub.com/p/microsoft-q3-fy2026-the-190b-capex)
- [Microsoft: Expect Capacity Constraints, CapEx Acceleration to Continue — Directions on Microsoft](https://www.directionsonmicrosoft.com/microsoft-expect-capacity-constraints-capex-acceleration-to-continue/)
- [Microsoft earnings preview: AI spending, cloud margins — GeekWire](https://www.geekwire.com/2026/microsoft-earnings-preview-record-ai-spending-and-a-stock-near-a-one-year-low/)
- [Microsoft (MSFT) spent $4.627 billion on share buybacks during Q3 2026 — Shacknews](https://www.shacknews.com/article/148917/microsoft-msft-stock-buybacks-q3-2026)
- [Microsoft Stock-Based Compensation — Eulerpool](https://eulerpool.com/stock/Microsoft-Stock-US5949181045/stock-basedcompensation)
- [MICROSOFT Free Cash Flow $66,987 Mil — GuruFocus](https://www.gurufocus.com/term/total-free-cash-flow/MSFT)
- [Microsoft FY26 Q4: Copilot Momentum and Capex Optics — Digital Applied](https://www.digitalapplied.com/blog/microsoft-fy26-q4-earnings-copilot-arr)

**Blocked / not opened:** `www.sec.gov`, `microsoft.gcs-web.com`, `www.stock-analysis-on.net`,
`www.cnbc.com`, `www.fool.com`, `news.alphastreet.com`, `deepquarry.substack.com`,
`www.investing.com`, `finance.yahoo.com`, `stockanalysis.com`, `businesswire.com`.
**`tradingkey.com` — blacklisted firm-wide, not cited; one figure sourced only to it was
discarded (§11.4).**

---
*巴爺爺 · Financial Statement Analyst · Department 2, Equity Research · 皮褸黃 Capital*
*Report ID: 2026-08-21-MSFT-FIN · Research only — the Committee and the Owner decide.*

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
