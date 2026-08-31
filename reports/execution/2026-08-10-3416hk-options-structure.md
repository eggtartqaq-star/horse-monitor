# 3416.HK — Options Structure Report

**C朗, Options Strategist · Department 8 (Trading Operations) · 2026-08-10**

Research and decision support. **Not financial advice.** No agent of this firm places
orders; the Owner executes.

---

## 0. Scope and what this report is not

The Owner's question was **"when should I sell?"** — asked on behalf of an 18-year-old
university student holding roughly **HK$8,000** of 3416.HK.

**This report answers the structural half of that question only.** John (CRO) is running
suitability in parallel and holds the veto. My job is to state, in numbers, what this
product does to a return distribution, so that the horizon judgement is made on
arithmetic rather than on the 18% headline.

I have not re-derived the CEO's interim note (`reports/equity/2026-08-04-3416hk-CEO-INTERIM.md`);
it is assumed read. Where I sharpen or contradict it, I say so explicitly.

**Headline finding, stated up front:** over the fund's life, the plain index appears to have
returned roughly **twice** what the fund returned, while the fund paid a ~15–18% "yield".
The arithmetic is in §4 and §9. It depends on one unverified fund-return figure, and that
dependency is flagged everywhere it matters.

## 1. Strategy and thesis link

Per my mandate, a strategy must serve a thesis. **3416.HK is not a position this desk would
have originated**, and no firm thesis on HSCEI exists on file — Department 3 (Quant) filed
nothing on this name, and no committee review has been held.

The thesis link is therefore inverted: the position already exists in the student's account,
and the question is whether the *implied* market view embedded in the structure matches the
*actual* view and horizon of the holder.

**The view a covered-call index overlay implicitly expresses is:**

> "Over the holding period, HSCEI will move less than the options market is charging for
> that movement, and will not sustain a large upward trend."

That is a **short-volatility, range-bound, income-now** view. It is a perfectly coherent
view. It is not a 40-year growth view, and it is not a view anyone at this firm has
articulated. A holder should own this because they hold that view — not because 18% is a
large number.

## 2. How these funds are really run — the overlay mechanics

### 2.1 What is sourced, and what is not

**Every attempt to open primary fund documentation was refused by the organisation egress
policy.** Hosts denied on this task, in addition to those already logged by the CEO:

| Host | Document sought | Result |
|---|---|---|
| `www.globalxetfs.com.hk` | Fund page, KFS, distribution composition table | **HTTP egress block** |
| `investments.miraeasset.com.hk` | Covered Call Monthly Commentary PDFs (multiple months) | **HTTP egress block** |
| `stockanalysis.com` | 3416 / 2828 quote and return pages | **HTTP egress block** |
| `en.macromicro.me` | HSCEI index history | **HTTP egress block** |
| *(previously logged by CEO)* `hkexnews.hk`, `finance.yahoo.com`, `stooq.com`, `alphavantage.co`, `data.nasdaq.com`, `hsi.com.hk`, `chinaamc.com.hk` | — | **HTTP egress block** |

Per standing instruction I did not retry or route around any denial. **No primary document
was opened by me.** What follows is search-engine extraction *of* those documents — the
snippets are quotations from the issuer's own PDFs, but I could not read the surrounding
context, and that is a real limitation.

`tradingkey.com` is blacklisted firm-wide as price-data-unusable and was not consulted.

### 2.2 What is confirmed

**Options are written on the INDEX, not on single names.** The issuer's own description of
the structure, recovered verbatim:

> "The Funds adopt a covered call strategy by (i) investing in constituent equity securities
> in the Reference Index and the Reference Index ETF and long positions of Reference Index
> Futures, and (ii) **writing call options on the Reference Index**."

— Global X ETFs launch materials / fund documentation, via search extraction; launch
2024-02 (PRNewswire release 302075045; ETFGI, Feb 2024).

Three consequences the marketing does not emphasise:

1. **The overlay is index-level.** There is no dispersion benefit — the fund sells index
   volatility, which is structurally *cheaper* than the average of its constituents'
   volatility because index vol is damped by imperfect correlation. A single-name
   overwriting programme would harvest more premium per unit of upside surrendered. This
   fund chose the lower-premium, lower-tracking-error route. That is a defensible design
   choice, but it means the "yield" is being manufactured from a thinner raw material than
   a US single-name covered-call fund of the same headline yield.
2. **The long leg need not be physical.** The mandate explicitly permits holding the
   *Reference Index ETF* and *long index futures* alongside cash equities. Futures-based
   exposure carries roll cost or benefit that is invisible in the 0.75% TER headline.
   **I have no data on the actual mix and will not guess at it.**
3. **The "53 holdings" figure does not imply full replication.** HSCEI has 50 constituents;
   53 line items is consistent with constituents plus ETF plus futures/cash collateral.

**Distributions may be paid out of capital, at the manager's discretion.** Confirmed
verbatim from the issuer:

> "Distribution may be made out of capital. Payments of distributions out of capital or
> effectively out of capital amounts to a return or withdrawal of part of an investor's
> original investment or from any capital gains attributable to that original investment.
> Any such distributions may result in an immediate reduction in the Net Asset Value per
> Share of the Fund."

This is not a warning the issuer buried — it is the standard SFC-mandated disclosure, and
it is accurate. See §5.

### 2.3 Premium actually earned — hard numbers

This is the best-sourced operational dataset I recovered. Each figure is the fund's own
reported **premium earned from selling index call options**, extracted from the Mirae Asset
/ Global X *Covered Call Monthly Commentary* PDFs for 3416:

| Month | Premium earned (% of notional) | Issuer commentary |
|---|---|---|
| May 2025 | 1.97% | |
| Jun 2025 | 2.05% | |
| Aug 2025 | 1.74% | issuer attributes decline to "decline in market volatility" |
| Dec 2025 | 1.88% | |
| Jan 2026 | 2.03% | |
| Mar 2026 | 1.93% | |

*Source: Mirae Asset, "Covered Call Monthly Commentary — Global X HSCEI Covered Call Active
ETF (3416)", monthly editions 25-06, 26-01, 26-02, 26-05 and others; recovered by search
extraction on 2026-08-10. The PDF host is egress-blocked; I could not open the documents
themselves.*

**Range 1.74%–2.05%; midpoint ~1.9% per month.** Six observations spanning eleven months —
a sample, not the full series, but tight and consistent.

Naive compounding: 1.9%/month = **25.4%/yr of gross option premium**. Note immediately that
this exceeds the ~15–18% distribution yield, which means the fund is **not** distributing
the entire premium. That is a point in the fund's favour and is developed in §5.

### 2.4 Tenor, roll and strike — confirmed, inferred, and unknown

| Parameter | Status | Value / reasoning |
|---|---|---|
| Underlying of option | **Confirmed** | HSCEI index options |
| Tenor | **Inferred, high confidence** | ~1 month. The commentary reports a discrete premium figure *per calendar month*, which only makes sense for a monthly write. HKEX HSCEI index options are standard monthly-expiry contracts. |
| Roll schedule | **Inferred, high confidence** | Around HKEX monthly expiry — the business day preceding the last business day of the month. **Not confirmed from fund documents.** |
| Strike moneyness | **NOT DISCLOSED — inferred below** | |
| Coverage ratio | **NOT DISCLOSED — inferred below** | |

**The fund publishes neither strike nor coverage ratio, and this is the most important gap
in this report.** The word *Active* in the fund's name is doing real work: strike and
coverage are **discretionary and can change month to month without notice**. A holder cannot
know what cap sits on their upside next month. That is a genuine structural risk, and it is
distinct from the risk of the covered-call strategy itself.

**Inference — labelled as inference, with the model shown so it can be checked.**

A one-month at-the-money call is worth approximately `0.4 × IV × √T` of spot. Volatility
context as of 2026-08-10: **VHSI 21.37**, one-month range 17.94–23.92 (Investing.com via
search extraction, 2026-08-10). Note VHSI tracks *HSI* volatility; **HSCEI implied vol
typically prints several points higher** than HSI, so 22–26% is the reasonable working band.

| Assumed 1M implied vol | Theoretical ATM call premium |
|---|---|
| 18% | 2.08% of spot |
| 22% | 2.54% of spot |
| 26% | 3.00% of spot |
| 30% | 3.46% of spot |

Observed premium is ~1.9%. Against a plausible HSCEI 1M implied vol of 22–26%, an ATM call
should fetch 2.5–3.0%. Collecting 1.9% is therefore consistent with **either**:

- **(a)** ~100% coverage at a strike roughly **2–4% out-of-the-money**, or
- **(b)** ~**65–75% coverage** at or near the money, leaving 25–35% of the book uncapped.

**I cannot distinguish between these from public data, and the difference matters greatly to
the holder** — (b) leaves a real slice of upside intact; (a) caps essentially everything.
Modelling in §3 uses **(a) with a 2% OTM strike**, the *less favourable* of the two and
therefore the conservative choice for a risk report. **If the fund is in fact running partial
coverage, true upside capture is better than §3 shows.**

**This is the single highest-value question the Owner could put to Global X investor
relations**, and it is answerable in one email: *what were the average strike moneyness and
average coverage ratio over the last twelve months?*

## 3. The payoff, stated precisely — four regimes

### 3.1 The model

Monthly fund return, before fees, on the conservative assumption set from §2.4(a):

```
fund_return = index_return + premium − max(0, index_return − cap)
premium = 1.90%   (observed midpoint, §2.3 — SOURCED)
cap     = 2.00%   (strike 2% out-of-the-money — INFERRED, not disclosed)
```

Deduct the 0.75%/yr TER (~0.06%/month) from every figure below for the net-of-fee result.

### 3.2 The payoff table — one month

| HSCEI move | Fund return | Difference |
|---|---|---|
| **+20%** (violent rally) | **+3.90%** | **−16.10 pp** |
| **+10%** (sharp rally) | **+3.90%** | **−6.10 pp** |
| +5% | +3.90% | −1.10 pp |
| +2% (grind up) | +3.90% | +1.90 pp |
| **0%** (flat) | **+1.90%** | **+1.90 pp** |
| −2% | −0.10% | +1.90 pp |
| −5% | −3.10% | +1.90 pp |
| **−10%** (sharp fall) | **−8.10%** | **+1.90 pp** |
| **−20%** (crash) | **−18.10%** | **+1.90 pp** |

Read the two ends of that table together. **The upside stops at +3.90% in a month. The
downside does not stop.** In a −20% month the entire benefit of the strategy is 1.9
percentage points of cushion.

### 3.3 The four regimes in words

**Sharp rally — the case buyers misunderstand.** The fund earns +3.9%; the index earns +10%,
+15%, +20%. The fund *still pays its distribution*, and that distribution still looks like
~1.5%/month, so **the holder's statement shows income arriving normally while they fall six
percentage points behind the market in a single month.** Nothing on the statement signals
the shortfall, because the shortfall is a *foregone* gain, and foregone gains are invisible.
This is the core misunderstanding, and it is the regime HSCEI has plausibly been in — §9.

Note the cap **re-strikes each month at the new, higher spot**. A sustained rally is not
capped once and forever: the fund makes +3.9% *per month*, compounding to a theoretical
+58.3%/yr if every month were capped. **The fund is not broken in a rally — it is simply,
reliably, behind**, by roughly (index gain − 3.9%) in every month that runs hot.

**Grind up.** The best regime for the product, and genuinely good. Index +2%/month, fund
+3.9%/month — outperformance of 1.9pp per month, ~25%/yr. This is what the product is
designed for, and it delivers.

**Flat.** Index 0%, fund +1.9%/month. Pure premium harvest. Also excellent.

**Sharp fall.** Index −10%, fund −8.1%. The fund loses slightly less. **It is not a hedge.**
It is long equity with a 1.9%/month rebate. HSCEI fell more than 50% peak-to-trough between
2021 and 2022; a 1.9%/month rebate against that is a rounding error. A holder who believes
the covered call "mitigates downside risk" — the issuer's own phrasing — should understand
that the mitigation is exactly one month's premium, and no more.

### 3.4 The round-trip trap — the part almost nobody models

Regimes do not arrive one at a time. What determines the outcome is **whether realised moves
stay inside the cap**. Two consecutive months, index ending roughly flat:

| Path | Index net | Fund net | Gap |
|---|---|---|---|
| +2% then −2% | −0.04% | **+3.80%** | **+3.84 pp** |
| +5% then −5% | −0.25% | +0.68% | +0.93 pp |
| **+10% then −10%** | **−1.00%** | **−4.52%** | **−3.52 pp** |
| **+20% then −20%** | **−4.00%** | **−14.91%** | **−10.91 pp** |

**The index goes essentially nowhere in all four paths. The fund's outcome ranges from +3.8%
to −14.9%.**

This is the honest description of what the holder owns: **not an income product, but a short
position in realised volatility.** The fund wins when HSCEI's realised monthly moves stay
inside the ~3.9% cap and loses — asymmetrically — when they do not. The distribution is paid
identically in every one of those four paths, which is precisely why the distribution tells
the holder nothing about how they are doing.

**HSCEI is among the highest-volatility major equity indices in the world.** That is exactly
the underlying on which a monthly cap gets breached most often.

## 4. Distribution yield versus total return — the crux

### 4.1 The two numbers are not comparable, and only one is a return

- **Distribution yield** = cash paid out ÷ price. It says nothing about whether the cash
  came from profits or from the investor's own capital.
- **Total return** = change in NAV **plus** distributions. This is the only number that
  measures whether the holder got richer.

A fund can pay 18% forever while its NAV bleeds, and the holder can lose money the entire
time. **Nothing on a brokerage statement distinguishes the two cases.**

### 4.2 The figures on file

| Metric | Value | Source / status |
|---|---|---|
| Annual distribution per unit | HK$1.69 | Stock Events, retrieved 2026-08-10 |
| Trailing-12m distribution per unit | HK$1.71 | stockanalysis, via CEO interim 2026-08-04 |
| Latest monthly distribution | HK$0.15, ex-date 2026-05-29, pay 2026-06-04 | Stock Events, retrieved 2026-08-10 |
| Current monthly distribution | HK$0.14 | Stock Events, retrieved 2026-08-10 |
| Headline distribution yield | 17.96% | Stock Events, retrieved 2026-08-10 |
| Alternative yield quote | 15.56% | vendor extraction, undated |
| **Avg annual total return since inception** | **10.50%** | **single source, UNVERIFIED** |
| Total return 2024-02-29 → 2025-07-31 | +35.60%, of which 29.45pp dividends | vendor extraction, undated retrieval |
| "Total return past year incl. dividends" | **−6.43%** | vendor extraction, **undated — see §4.4** |
| "NAV return, one year" | **+6.86%** | vendor extraction, **undated — contradicts the line above** |
| Gross option premium collected | ~25.4%/yr (1.9%/mo compounded) | derived from issuer monthly commentary, §2.3 |

### 4.3 The gap, in one line

**~18% is being paid out. ~10.5%/yr is being earned. The difference is roughly 7.5
percentage points a year of the holder's own capital being handed back to them.**

That is the entire question, and it is the reason a monthly cheque from this product feels
better than it is.

### 4.4 Two vendor figures directly contradict each other

`−6.43%` total return over "the past year" and `+6.86%` NAV return over "a year" cannot both
be true. Both were retrieved undated. **I am not choosing between them and neither should
anyone downstream.** They are recorded here so nobody rediscovers them and treats one as
fact. Neither is used in any conclusion below.

### 4.5 Reconciling the premium with the payout — this part is genuinely favourable

The fund collects ~25.4%/yr in gross option premium (§2.3) and distributes ~18%. Those are
consistent: **the fund is not distributing more premium than it collects.** The shortfall in
*total return* is therefore **not** an unfunded distribution in the crude sense.

The shortfall comes from somewhere else, and it is worth naming precisely: **the fund pays
out the premium in cash but absorbs the capped upside as a permanent NAV loss.** The premium
is real income. The foregone appreciation is a real cost. Only the first one is visible, and
only the first one is distributed. Over a rising market, NAV is systematically ratcheted
down relative to where an unencumbered index holding would have been, and the difference is
mailed out monthly as "yield."

**That is the mechanism.** It is not a scandal, it is not mis-selling, and the issuer
discloses it. But it is why 18% and 10.5% can coexist.

## 5. Return of capital

### 5.1 What is confirmed

The fund **may** pay distributions out of capital at the manager's discretion, and does
disclose the split. The issuer publishes, per distribution, a breakdown of:

- "Dividend Paid Out of Net Distribution Income", and
- "Dividend Paid Out Of Capital"

*Source: Global X ETFs Hong Kong fund page description, via search extraction 2026-08-10.
**The table itself is behind an egress-blocked host and I could not read a single row of
it.***

### 5.2 What must be labelled inference

**NOT OBTAINED: the actual month-by-month income/capital split.** I will not invent it.

What can be said from arithmetic, **explicitly as inference, not data**:

- Gross option premium ≈ 25.4%/yr (§2.3, sourced) exceeds the ~18% distributed. On a cash
  basis the distribution *is* coverable from premium.
- Therefore the honest inference is **not** "most of the distribution is return of capital."
  A cruder version of this report would have said that, and it would have been wrong.
- The more accurate inference: **the distribution is largely funded by option premium, but
  the premium itself is partly compensation for capital the fund is simultaneously
  surrendering via the cap.** Economically the holder is being paid with money that was
  going to be theirs anyway in the form of appreciation. Accounting-wise it may well be
  classified as income; economically, in a rising market, it functions as return of capital.
- HK accounting classification and economic substance can diverge here, and **the classified
  split — whatever it says — will understate the economic capital return in a bull market.**

**This distinction is the most important thing in this report and I want it stated plainly:
the fund is probably NOT paying you your own money back in the accounting sense. It IS
paying you your own money back in the economic sense, whenever the index rises more than
the cap.**

## 6. The price / NAV conflict — RESOLVED, with the working shown

### 6.1 The conflict as handed to me

| Source | NAV | Price | Date |
|---|---|---|---|
| Last hard print on file | **HK$8.64** | — | 2026-07-23 |
| Vendor page queried 2026-08-10 | **HK$9.63** | HK$9.665 | **undated** |
| Vendor extraction, this task, 2026-08-10 | **HK$8.64** | **HK$10.570** (+0.48%) | undated; 52-wk range 8.23–10.97 |

Three different pictures. Note that **the third pair is internally impossible**: a NAV of
8.64 against a price of 10.57 is a **22% premium to NAV**. A HK$22bn ETF with appointed
market makers does not trade at a 22% premium — arbitrage closes that to well under 1%.
So at least one field in that pair is a stale value carried alongside a live one. The same
logic says the 9.63/9.665 pair (0.4% premium) is *internally* coherent, which is presumably
why it was believed.

### 6.2 Independent triangulation — which NAV is real

Rather than pick, I tested both against a figure neither vendor's NAV field feeds into: the
**reported 10.50%/yr since-inception total return**.

Assumptions, both labelled: launch NAV **HK$10.00** (market convention for HK ETFs —
**assumption, not sourced**, as the CEO correctly refused to treat it as fact); cumulative
distributions since inception ≈ **HK$4.00** (≈28 monthly payments at the observed HK$0.14–0.15
run-rate — **estimate**).

| Assumed current NAV | Implied cumulative TR | Implied annualised TR |
|---|---|---|
| **HK$8.64** | +26.4% | **+10.06%/yr** |
| HK$9.63 | +36.3% | +13.51%/yr |

**Reported: 10.50%/yr.**

**HK$8.64 reproduces the reported since-inception return to within 0.44 percentage points.
HK$9.63 misses it by 3.0 points.** Two independent chains — a NAV print and a return
statistic — agree on 8.64 and disagree on 9.63.

### 6.3 Verdict on the conflict

**HK$8.64 is very likely the correct NAV; HK$9.63 is very likely stale**, consistent with the
earlier correction the firm already made. The 9.63 figure appears to be resurfacing from
vendor caches and should be treated as a known-bad value.

**Confidence: moderate-to-high, but this is triangulation, not a primary print.** It rests on
an unsourced HK$10.00 launch NAV and an estimated distribution total. **It should not be
recorded as a verified NAV.** The only thing that settles it is the issuer's own daily NAV
page or an HKEX ETP quote, both egress-blocked here.

### 6.4 Which conclusions depend on it — and which do not

| Conclusion | Depends on NAV? |
|---|---|
| The payoff structure and regime analysis (§3) | **No** — pure structure |
| The distribution-vs-total-return gap exists (§4) | **No** — holds at either NAV |
| *Size* of the gap (7.5pp/yr vs ~4.5pp/yr) | **Yes** |
| The fund trailed the index (§9) | **No** — see §9.4; holds under both NAVs |
| Any per-unit valuation of the student's HK$8,000 | **Yes — do not compute one from vendor data** |

**The load-bearing conclusion of this report survives the conflict.** Under the *most
favourable* reading (NAV 9.63 → 13.5%/yr) the fund still trails HSCEI by ~6 percentage
points a year.

## 7. Path dependence and the compounding trap

### 7.1 The mechanical problem

On a HK$8,000 holding at the ~18% headline yield, the student receives roughly **HK$120 per
month** in cash (HK$103/month at the alternative 15.55% yield quote). Twelve times a year,
a small amount of cash lands and must be redeployed or it stops compounding.

**Reinvestment drag, by broker minimum commission, on a HK$120 monthly distribution:**

| One-way broker minimum | % of each distribution consumed | Drag on the HK$8,000 |
|---|---|---|
| HK$0 (zero-commission app brokers) | 0.0% | 0.00%/yr |
| HK$15 | 12.5% | **2.25%/yr** |
| HK$30 | 25.0% | **4.50%/yr** |
| HK$50 | 41.7% | **7.50%/yr** |
| HK$100 (typical bank) | **83.3%** | **15.00%/yr** |

*Illustrative brackets, consistent with the CEO's interim note. Substitute the student's
actual schedule — only the Owner can supply it.*

**At a traditional bank's minimum, reinvesting the monthly distribution costs 83% of the
distribution.** The product's entire headline advantage is destroyed by the act of trying to
compound it.

### 7.2 Batching fixes most of it

| Reinvestment frequency | HK$30 min | HK$50 min | HK$100 min |
|---|---|---|---|
| Monthly (12×/yr) | 4.50%/yr | 7.50%/yr | 15.00%/yr |
| Quarterly (4×/yr) | 1.50%/yr | 2.50%/yr | 5.00%/yr |
| **Annually (1×/yr)** | **0.38%/yr** | **0.62%/yr** | **1.25%/yr** |

Batching to annual reinvestment cuts the drag by ~92%. **If the holding is retained, annual
batching is the single highest-value operational change available**, and it costs nothing.
The trade-off is up to twelve months of cash drag on an average of ~HK$720 idle — small
relative to the commission saved at any minimum above ~HK$15.

### 7.3 The board lot problem, which may be worse than the commission

**BOARD LOT SIZE: NOT OBTAINED.** It was not recoverable from any reachable source, and it
was already flagged as unobtained in the CEO's 2026-08-04 note. Sensitivity:

| Board lot | Cost of one lot @ HK$8.64 | @ HK$10.57 | Months of distribution needed to buy one lot |
|---|---|---|---|
| 100 units | HK$864 | HK$1,057 | **7–9 months** |
| 200 units | HK$1,728 | HK$2,114 | 14–18 months |
| 500 units | HK$4,320 | HK$5,285 | **36–44 months** |

**Under every plausible board lot, the monthly distribution cannot buy even one lot.** At a
100-unit lot the student must accumulate for seven to nine months before reinvestment is
even *possible*; at 500 units, three to four years. The "monthly income" is monthly in name
only — as a compounding mechanism it is, at best, annual.

**This is the decisive practical finding of §7:** the product's monthly distribution
frequency, marketed as a feature, is operationally unusable at this account size. The cash
will sit idle or be spent. For a holder whose entire objective is not to touch the money for
decades, **a structure that forcibly converts 18% of the position into spendable cash every
year is working directly against the objective.**

### 7.4 Behavioural path dependence

Worth stating because it is real and not quantifiable: a monthly cash payment into an
18-year-old's account is a monthly invitation to spend it. The compounding maths above
assumes 100% reinvestment. Empirically that assumption fails most often precisely in the
population this product is being sold to.

## 8. The honest case FOR the product

*Filed under anti-anchoring rule **L-003**. This firm's recent verdicts have been uniformly
negative, which is exactly the condition under which a real opportunity gets missed. What
follows is stated at full strength and I mean it.*

### 8.1 The product is not defective — it is honest

3416 does precisely what its documentation says. The issuer discloses the capital-distribution
risk in plain language, publishes the income/capital split, publishes monthly premium earned,
and named the fund "Covered Call" so that nobody could mistake the mechanism. **There is no
mis-selling here.** Every criticism in this report is a criticism of *fit*, not of the
product's integrity, and the distinction matters.

At **0.75%/yr**, the fee is reasonable for an actively managed options overlay. Running a
disciplined monthly index-option writing programme yourself would cost far more in spreads,
margin, and error — and would be impossible at HK$8,000. **The fund delivers genuine
operational value: it makes an institutional options strategy accessible at retail size.**
That is not nothing, and the HK$22.37bn AUM says the market agrees.

### 8.2 The strategy is genuinely superior in specific, common regimes

This is not a consolation prize. From §3.2 and §3.4:

- **Flat market:** fund +1.9%/month vs index 0%. Roughly **+25%/yr of outperformance.**
- **Grind-up market (≤2%/month):** fund +3.9%/month vs index +2%. Again ~25%/yr ahead.
- **Choppy, small-amplitude market (±2%):** over a round trip the index does −0.04% and the
  fund does **+3.80%.**

Hong Kong equities have spent long stretches of the last fifteen years in exactly these
regimes. **An investor who correctly forecasts a range-bound HSCEI should own this fund
rather than the index, and would have been substantially right to do so.** The strategy is
not a tax on returns; it is a *transfer* of returns from the right tail into the middle of
the distribution, and if the distribution's realised shape is fat in the middle, that
transfer is pure profit.

### 8.3 Who this genuinely suits — stated at full strength

- **A retiree or anyone drawing income now.** Someone spending the distribution rather than
  reinvesting it suffers none of §7's drag — the "trap" only exists for a compounder. For a
  drawdown investor, monthly cash from a diversified equity portfolio *without selling units*
  is a real and valuable service, and 18% is a very high withdrawal rate to support.
- **An investor with an explicit range-bound view on Chinese equities.** This is the correct
  instrument for that view. Not a substitute — the correct one.
- **An investor with genuinely low volatility tolerance** who would otherwise panic-sell an
  index fund. Receiving visible monthly cash demonstrably helps some people hold risk assets
  through drawdowns. A slightly worse strategy actually held beats a better strategy
  abandoned at the bottom.
- **A short-to-medium horizon holder (say 3–7 years)** for whom the right-tail argument in
  §8.5 has much less force, because there is not enough time for the tail to matter.
- **Anyone who wants Chinese equity beta with modestly lower volatility.** The overlay does
  reduce realised volatility. That is a real risk-adjusted benefit and it shows up in
  Sharpe-type measures even when it costs total return.

### 8.4 The strongest argument I can make for the student holding it

Stated properly, because it deserves to be:

> The student is 18, this is likely their first investment, and the greatest risk to a
> 40-year compounding plan is **not** suboptimal instrument selection — it is **quitting**.
> A product that pays visible cash every month and is 20–25% less volatile than the index
> may well be the product that keeps a first-time investor invested through their first
> −30% China drawdown. **Compounding at 10.5% for forty years beats compounding at 19.5%
> for four years and then selling in a panic and never returning.** Instrument optimality is
> worth less than participation.

That argument is real and I do not dismiss it. It is the best case for holding, and if the
Owner's judgement is that the student's risk of abandoning equities is high, it may be
decisive.

### 8.5 Where the case for it nonetheless runs out

Two things bound it, and I state them because a fair case requires its own limits:

1. The behavioural benefit can be obtained from a plain index fund plus a rule ("do not
   look at it"), at zero cost in expected return. Paying ~6–9 percentage points a year for a
   commitment device is a very expensive commitment device.
2. Long-run equity returns are dominated by a small number of large upward moves. §3.2 shows
   this strategy sells precisely those months, every month, by construction. Over one year
   that is a fair trade for premium. **Over forty years it is a systematic sale of the part
   of the distribution that produces most of the compounding** — and unlike a market view,
   this argument does not depend on any forecast being right.

## 9. The alternative — what plain HSCEI exposure delivered

*This is the number the brief identified as highest-value and which defeated two previous
attempts. I have it, and I show the full chain so it can be audited.*

### 9.1 The anchors

| Anchor | Value | Source |
|---|---|---|
| HSCEI close, **2024-02-29** | **5,677.88** (−10.58 pts, −0.19% that day) | Business Standard capital-market report, article 124022900874, dated 2024-02-29 |
| HSCEI level, August 2026 (quote A) | **8,136.73** | Investing.com via search extraction, 2026-08-10; **undated within August** |
| HSCEI level, August 2026 (quote B) | **8,498.73** (−1.22% on the day) | search extraction, 2026-08-10; **undated within August** |
| HSCEI dividend yield | **3.14%** | Hang Seng Indexes HSCEI factsheet, **June 2026** |

Fund inception is 2024-02-28 and my index anchor is 2024-02-29 — one trading day later, a
−0.19% day. **The mismatch is immaterial** (it makes the index comparison marginally
*conservative*).

I could not resolve quote A against quote B; both were retrieved on 2026-08-10 and neither
carried a precise date. **I therefore report the comparison as a range rather than a point,**
and note that the conclusion is unchanged across the whole range.

### 9.2 HSCEI return since fund inception

| Measure | Using 8,136.73 | Using 8,498.73 |
|---|---|---|
| Price return, cumulative | +43.3% | +49.7% |
| Price return, annualised | +15.86%/yr | +17.94%/yr |
| **Total return, cumulative** | **+54.6%** | **+61.4%** |
| **Total return, annualised** | **+19.50%/yr** | **+21.65%/yr** |

*Price return is arithmetic on two sourced index levels. **Total return applies the 3.14%
dividend yield as a constant across the whole period — this is an ESTIMATE**, not a
computed total-return index. The true figure will differ modestly. The HSCEI Total Return
Index exists (HKEX publishes it) but every host carrying its history was egress-blocked.*

Cross-check, independent of my arithmetic: the plain HSCEI index ETF **2828.HK** reportedly
returned **+30.45% in calendar 2024** and **+29.93% over "the past year"** (vendor
extractions, undated retrieval). Those are consistent with an index compounding in the high
teens to low twenties annually over this window. **The direction and magnitude corroborate.**

### 9.3 The comparison — what the overlay cost

| | Annualised | Cumulative since 2024-02-28 | HK$8,000 would now be |
|---|---|---|---|
| **3416.HK** (reported, unverified) | **10.50%/yr** | **+27.6%** | **HK$10,211** |
| 3416.HK (best case, if NAV 9.63 were right) | 13.50%/yr | +36.6% | HK$10,902 |
| **HSCEI total return** (low estimate) | **19.50%/yr** | **+54.6%** | **HK$12,364** |
| HSCEI total return (high estimate) | 21.65%/yr | +61.4% | HK$13,058 |

**The overlay cost between 6 and 11 percentage points a year.** Central estimate: the fund
returned **10.5%/yr against roughly 19.5%/yr for the index it holds — it captured a little
over half the return of its own portfolio**, while paying a distribution yield of ~18%.

On HK$8,000, the shortfall to date is roughly **HK$2,150 (central)** — around **27% of the
entire position** — and it is entirely invisible on a statement that has shown ~HK$120
landing every month.

### 9.4 Why this conclusion is robust

It survives every open dispute in this report:

- **NAV conflict (§6):** under the *most favourable* NAV assumption the fund still trails by
  ~6pp/yr. Under the better-supported one, ~9pp/yr.
- **Index level ambiguity:** the gap is 6–11pp/yr across the full 8,137–8,499 range.
- **Dividend-yield estimate:** even at a 0% dividend assumption, HSCEI price return alone
  (15.9–17.9%/yr) exceeds the fund's total return by 5–7pp/yr.
- **Coverage-ratio uncertainty (§2.4):** partial coverage would *narrow* the gap, but the
  10.50% figure is an observed outcome, not a modelled one, so this changes nothing.

**Every path leads to the same conclusion: the covered-call overlay cost materially more
than it paid over this window.** That is not a criticism of the manager — §3 shows this is
exactly what the structure does when the index trends up, and HSCEI has trended up hard.
The strategy was not broken. **It was in the wrong regime, and the holder was told they were
earning 18% throughout.**

### 9.5 The long-horizon extrapolation — read the caveat

**ILLUSTRATIVE ARITHMETIC, NOT A FORECAST.** Nobody can predict 40 years of returns and this
firm does not pretend to. The point is only to show what a persistent annual gap does:

| Compounding rate | HK$8,000 after 40 years |
|---|---|
| 10.5%/yr | HK$434,000 |
| 13.5%/yr | HK$1,267,000 |
| 19.5%/yr | HK$9,950,000 |

The top rate will not persist for forty years — no equity market does that. **The relevant
observation is the shape, not the level:** a gap of 6–9 percentage points a year, sustained,
does not cost a fraction of the outcome. It costs an order of magnitude. This is the
quantified version of the CEO's structural argument, and the structural argument is correct.

## 10. Full risk profile — mandatory disclosure

*Department 8 standing rule: max loss is stated in dollars on every proposal, always.
This is a held position rather than a proposal, but the disclosure standard is identical.*

**Position modelled: HK$8,000 of 3416.HK.**

### 10.1 Loss, gain, breakeven

| Measure | Value | Notes |
|---|---|---|
| **MAXIMUM LOSS** | **HK$8,000 — the entire position, less distributions already received** | If HSCEI went to zero. The covered call provides ~1.9%/month of cushion and **nothing more**. There is no floor, no protection, and no put. |
| Realistic severe-drawdown loss | **HK$2,400–HK$3,200 (−30% to −40%)** | HSCEI fell >50% peak-to-trough 2021–2022. A repeat, less ~1.9%/month premium, lands in this band. |
| **MAXIMUM GAIN, per month** | **+HK$312 (+3.90%)** | Hard structural cap = strike distance (2%, inferred) + premium (1.9%, sourced). |
| Maximum gain, theoretical annual | +58.3% | Only if *every* month is capped and none falls. Has never happened and will not. |
| Monthly premium income | ~HK$152 (1.9%) | Gross, before fees |
| **Monthly breakeven** | **HSCEI ≥ −1.90%** | Below a 1.9% monthly index fall, the position loses money. |
| Annual fee drag | HK$60/yr (0.75%) | Deducted from NAV, not from the distribution |
| **Reinvestment drag** | **HK$0–HK$1,200/yr** | Entirely determined by broker minimum — §7. At a bank minimum this is the largest single cost in the table. |
| **Realised opportunity cost to date** | **~HK$2,150 vs holding plain HSCEI** | §9.3, central estimate |

### 10.2 Assignment risk — the good news, stated clearly

**There is no assignment risk to the ETF holder, and this is a genuine structural advantage
of the index-option design.**

HSCEI index options are **cash-settled European-style** contracts. They cannot be exercised
early and they never deliver stock. Consequences:

- The fund is **never forced to sell its underlying holdings** to meet an exercise. It settles
  the option's intrinsic value in cash and retains the portfolio.
- There is no early-assignment risk around ex-dividend dates — the classic hazard of
  single-name American-style covered calls, and a real one in high-dividend Chinese financials
  such as CCB and ICBC, which are large HSCEI weights.
- The holder of 3416 cannot be assigned anything. They hold ETF units.

**No naked short options are present.** The fund's short calls are covered by its long index
exposure (physical constituents, the index ETF, and/or long index futures). This complies
with the firm's prohibition on naked short options in `config/risk-limits.yaml` — though
note that a covered call on an *index* against a *basket* carries basis risk that a
single-name covered call does not, if the basket ever diverges from the index it is written
against.

### 10.3 Greeks

Calibrated Black-Scholes, 1-month HSCEI index call, 24% implied vol, 2% out-of-the-money:

| Greek | Value | Interpretation |
|---|---|---|
| Short call delta | **0.40** | |
| **Net position delta** | **~0.60** | 100% coverage assumed. **The holder has roughly 60% of the equity exposure they think they have, right after each monthly roll.** |
| Delta drift within the month | 0.60 → 1.00 if index falls; 0.60 → 0.00 if index rallies through the strike | **Delta shrinks exactly when the market rises and expands exactly when it falls.** This is the negative-gamma signature and it is the mathematical core of §3.4. |
| **Gamma** | **NEGATIVE** | The position gets shorter into rallies and longer into declines — the opposite of what a long-horizon compounder wants. |
| **Theta** | **POSITIVE, ~+HK$7.2/day** | The only Greek working in the holder's favour. This is the entire economic engine. |
| **Vega** | **NEGATIVE, ~−HK$8.9 per +1 vol point** | A volatility spike hurts the mark, though it raises *future* premium. |

**Calibration note, and it is a good one:** a 1-month call struck 2% out-of-the-money at 24%
implied volatility prices at **exactly 1.90%** — the observed premium midpoint from §2.3.
Assumption (a) in §2.4 therefore reproduces the fund's actual reported premium to two decimal
places at a plausible HSCEI implied vol. **This materially raises confidence that the fund
runs approximately full coverage at approximately 2% OTM on a one-month tenor**, and
correspondingly lowers the probability of the more benign partial-coverage reading (b).
It remains an inference — a different (coverage, moneyness, vol) triple could produce the
same premium — but it is now a well-supported one.

### 10.4 Volatility context — is the fund selling cheap or expensive vol?

Per my mandate: selling cheap vol and buying expensive vol are both errors.

| Measure | Value | Source / date |
|---|---|---|
| VHSI (HSI 30-day implied vol) | **21.37** | Investing.com via search extraction, 2026-08-10 |
| VHSI 1-month range | 17.94 – 23.92 | same |
| HSCEI implied vol (working estimate) | **22–26%** | **INFERRED** — HSCEI implied typically prints above HSI implied |
| **IV percentile vs history** | **NOT OBTAINED** | VHSCEI history is on `hsi.com.hk` — egress-blocked |

**This is a real gap and I will not paper over it.** Without an IV percentile I cannot say
whether the fund is currently selling rich or cheap volatility. What I can say:

- VHSI at ~21 is **not** an elevated reading by Hong Kong standards. Chinese equity implied
  vol has spent much of the last decade in the 20s and spikes well above 40 in stress.
- The issuer's own August 2025 commentary attributes the drop to 1.74% premium to "decline in
  market volatility" — confirming the fund is a **price-taker on volatility**, not a
  timer of it. It writes every month regardless of whether vol is rich or cheap.
- **Mechanically writing calls monthly without regard to the vol level is, by my department's
  standards, an error of process** — it guarantees selling cheap vol in quiet regimes.
  A discretionary manager *could* stand down when premium is poor; the observed data show
  premium collected in every reported month, so it appears they do not.

The variance risk premium (implied minus subsequent realised) is genuinely positive on
average in most equity markets, which is the strategy's real edge. **But §9 shows that over
this particular window that edge was overwhelmed by the trend the calls were sold against.**

## 11. Exit / roll plan — addressing "when should I sell?"

**Structural framing only. John (CRO) holds suitability and the veto; the Owner decides and
the Owner executes.** I make no recommendation to buy, hold, or sell.

### 11.1 The honest answer to the timing question

**There is no market-timing answer to "when should I sell?", and looking for one is the wrong
frame.** This is not a position with a thesis that will be proven or disproven by a price
level. It is a structural mismatch — or not — between an instrument and a horizon. That
question has the same answer today, next month, and after the next rally.

**If the instrument is wrong for a 40-year horizon, it is wrong at any price**, and waiting
for a better exit price adds a market-timing bet on top of an already-questionable structure.
Conversely, if the behavioural argument in §8.4 governs, no price level should trigger a sale.

### 11.2 What genuinely does affect timing

| Consideration | Effect |
|---|---|
| **Costs are the binding constraint, not price.** A round trip at a HK$100 bank minimum costs HK$200 = 2.5% of the position. | Argues for **one decision, executed once** — not staged exits. |
| **HK ETFs are exempt from the 0.1% stamp duty.** | Removes the largest statutory charge. Cost is broker minimum only. |
| **Ex-distribution dates.** Latest observed ex-date 2026-05-29 for a HK$0.15 payment. | **Immaterial.** Selling before an ex-date forfeits nothing — NAV drops by the distribution. Do **not** hold on to "capture" a distribution; that is the same money either way. |
| **Board lot (NOT OBTAINED).** | May force a partial position to be sold whole, or block a partial sale entirely. **Check before planning any partial exit.** |
| **Concentration.** HK$8,000 in a single China-equity product is presumably a large share of this student's net worth. | A concentration question for Zac (Position Sizing) and John, not for me. |

### 11.3 Conditions that would change my structural read

Stated in advance so this report can be scored later:

1. **Coverage ratio confirmed materially below ~80%** (one email to Global X IR, §2.4).
   The upside cap would be far less binding and the §9 gap should narrow going forward.
2. **A verified since-inception total return materially above 10.5%.** The whole §9 case
   rests on one unverified figure; a real one from the fund's own factsheet could move it.
   Note the §6.2 triangulation independently supports ~10%, so this is unlikely but possible.
3. **A regime change to a range-bound HSCEI.** If the index goes sideways for years, this
   fund beats it — materially — and §8.2 becomes the operative section.
4. **HSCEI implied vol moving to a genuinely high percentile.** Selling expensive vol is a
   real edge; selling cheap vol is not. **Currently unmeasurable — see §10.4.**

### 11.4 If the position is retained

Two operational changes cost nothing and are worth real money:

1. **Batch reinvestment annually, not monthly.** Saves 0.4–14 percentage points a year
   depending on broker minimum (§7.2). This is the highest-return action available.
2. **Track total return, never distribution yield.** The correct measure is
   `(NAV change + distributions received) ÷ amount invested`. The 18% number should never be
   used to judge how the position is doing, in either direction.

## 12. Risk-review status

| Item | Status |
|---|---|
| Submitted to John (CRO) for risk review | **NOT YET — this report is the input to that review** |
| Suitability opinion | **John, running in parallel. Not mine to issue.** |
| Naked short options present | **No.** All short calls are covered by long index exposure (§10.2). Compliant with `config/risk-limits.yaml`. |
| Committee review held | **No.** No `/committee` has convened on this name. |
| Decision logged to `memory/decisions/` | **No.** Nothing to log — no decision has been made. |
| Quant Research (Dept 3) input | **None filed.** Gap carried forward from the CEO's 2026-08-04 note. |
| Live trading | **None.** No agent of this firm has connected to any broker. |

**No verdict is issued by this report.** It is a structural analysis intended to inform John's
suitability opinion and the Owner's decision.

## 13. NOT OBTAINED register

Explicit and complete. A short honest report beats a long one that papers over gaps.

### 13.1 Blocked by organisation egress policy (HTTP 403 / EGRESS_BLOCKED)

Every one of these was attempted once and not retried, per standing instruction:

- `www.globalxetfs.com.hk` — fund page, KFS, **distribution income/capital split table**
- `investments.miraeasset.com.hk` — Covered Call Monthly Commentary PDFs (all months)
- `stockanalysis.com` — 3416 and 2828 quote/return/dividend pages
- `en.macromicro.me` — HSCEI history
- Previously logged: `hkexnews.hk`, `finance.yahoo.com`, `stooq.com`, `alphavantage.co`,
  `data.nasdaq.com`, `hsi.com.hk`, `chinaamc.com.hk`

`tradingkey.com` is firm-blacklisted as price-data-unusable and was deliberately not consulted.

### 13.2 Material facts NOT OBTAINED

| # | Missing fact | Why it matters | How to get it |
|---|---|---|---|
| 1 | **Coverage ratio** | Determines how much upside is actually capped. §10.3 calibration favours ~100%, but this is inference. | One email to Global X HK investor relations |
| 2 | **Strike moneyness policy** | Sets the monthly cap. Inferred ~2% OTM; not disclosed. | Same email |
| 3 | **Distribution income/capital split** | The formal return-of-capital answer. §5 gives only an inference. | Monthly factsheet, host blocked |
| 4 | **BOARD LOT SIZE** | May make partial sales or reinvestment impossible (§7.3). Unobtained since 2026-08-04. | **Any HK broker app, thirty seconds — Owner can settle this** |
| 5 | **Verified since-inception total return** | §9 rests on one unverified figure (triangulated in §6.2 but not verified). | Fund factsheet, host blocked |
| 6 | **Precise current NAV and date** | §6 resolves this by inference to HK$8.64, not by a primary print. | Issuer daily NAV page or HKEX ETP quote, both blocked |
| 7 | **HSCEI Total Return Index history** | Would replace my 3.14%-constant dividend estimate with a computed figure. | HKEX / Hang Seng Indexes, blocked |
| 8 | **VHSCEI history / IV percentile** | Cannot say whether the fund sells rich or cheap vol (§10.4). | `hsi.com.hk`, blocked |
| 9 | **Student's actual broker minimum** | Swings the answer by up to 15%/yr (§7.1). | **Owner only** |
| 10 | **Physical vs futures vs ETF mix in the long leg** | Hidden roll cost outside the 0.75% TER. | Fund holdings disclosure, blocked |
| 11 | **Exact date of the August 2026 HSCEI level** | Two undated quotes (8,136.73 / 8,498.73); handled as a range in §9. | Any dated index print |

### 13.3 Figures explicitly marked as estimate or inference

- HSCEI **total** return (§9.2) — applies a constant 3.14% dividend yield. **ESTIMATE.**
- Launch NAV HK$10.00 (§6.2) — market convention. **ASSUMPTION, not sourced.**
- Cumulative distributions since inception ≈ HK$4.00 (§6.2) — from observed run-rate. **ESTIMATE.**
- Strike 2% OTM / ~100% coverage (§2.4, §3.1) — **INFERENCE**, strongly supported by the
  §10.3 premium calibration but not disclosed by the fund.
- HSCEI implied vol 22–26% (§10.4) — **INFERRED** from VHSI plus a typical HSCEI/HSI spread.
- One-month tenor and month-end roll (§2.4) — **INFERRED**, high confidence.
- 40-year projections (§9.5) — **ILLUSTRATIVE ARITHMETIC, NOT A FORECAST.**

### 13.4 Unresolved contradictions, recorded so they are not rediscovered as fact

1. **NAV HK$8.64 vs HK$9.63.** Resolved *by triangulation* to 8.64 (§6.2). **Not verified.**
2. **NAV 8.64 alongside price 10.570** from one vendor — a 22% premium to NAV, which is
   **internally impossible** for a HK$22bn market-made ETF. At least one field is stale.
3. **"−6.43% total return past year" vs "+6.86% NAV return in a year"** — mutually
   contradictory, both undated. **Neither is used anywhere in this report.**
4. **Distribution yield 17.96% vs 15.56%**; annual distribution HK$1.69 vs HK$1.71.
   Minor, and immaterial to every conclusion.
5. **HSCEI August 2026 level: 8,136.73 vs 8,498.73.** Handled as a range; conclusions hold
   across the whole range (§9.4).

---

**Prepared by C朗, Options Strategist, Department 8 — Trading Operations.**
Recommendations only; the Owner executes. Research and decision support, **not financial
advice**, and markets cannot be reliably predicted.

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
