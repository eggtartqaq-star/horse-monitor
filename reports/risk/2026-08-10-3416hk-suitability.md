# 3416.HK — Risk & Suitability Review · Department 6 (Risk Management)

**John, Chief Risk Officer · 2026-08-10**
**Subject:** Global X HSCEI Components Covered Call Active ETF (HKD counter), ISIN HK0000978954
**Question referred by the Owner:** *"When should I sell 3416?"*
**Holder profile as given:** 18 years old, university student, ~40-year horizon,
no stated income need, position ~HK$8,000, plan to add HK$1,000/month.
**Extends:** `reports/equity/2026-08-04-3416hk-CEO-INTERIM.md` (CEO 皮褸黃). I do not
re-derive what is established there.

---

## 0. Verdict

| Decision in front of the Owner | Verdict |
|---|---|
| **A. Continue the HK$1,000/month accumulation plan into 3416** | **VETOED** |
| **B. Hold the existing ~HK$8,000 as a 40-year core position** | **VETOED** |
| **C. Exit the existing ~HK$8,000** | **APPROVED WITH CONDITIONS** (§7.1) |

**Direct answer to "when should I sell 3416?":**
**The sell decision is administrative, not market-timed. There is no price to wait for
and no date to target.** The product does not match the holder; that mismatch does not
get better or worse with the index level. The correct trigger is *operational
readiness* — a zero- or low-commission broker, and a single whole-position order — not
a level on the HSCEI. Waiting for a "better price" to exit a product you should not own
is a second mistake stacked on the first.

**Two grounds for the veto, and they are independent:**

1. **Structural (established by the CEO, and I concur without reservation).** A
   covered-call overlay systematically sells the right tail of the return distribution.
   The right tail is where multi-decade compounding comes from. An 18-year-old's single
   largest asset is time, and this product's entire mechanism is the monthly sale of
   time's value. This holds regardless of what China equities do next.
2. **Empirical, and new to this report (§6.3).** The overlay has in fact cost more than
   it paid, and the manufacturer says so. Global X's own commentary concedes 3416
   **underperformed HSCEI since launch**. And on the trailing twelve months a vendor
   dataset puts 3416's **total return at −6.43%** against **+7.42%** for the plain
   HSCEI ETF (2828.HK) — a gap of roughly **14 percentage points in one year**, while
   the fund paid a headline ~18% "yield". **A negative total return alongside an 18%
   distribution is the definition of return of capital.** The thesis-breaking trigger
   in §7.2 has therefore **already fired**.

**Risk score: 22 / 100 for this holder** (higher = more acceptable; convention as used
in the BE 18/100 and INTC 28/100 reviews). See §10 — and note the score is *holder-
specific*, not a judgement that the fund is defective.

**A veto is escalated, not overridden.** This goes to the Owner. And per standing rules
this is research and decision support, **not financial advice**.

---

## 1. Formal suitability opinion

### 1.1 The opinion

**3416.HK is UNSUITABLE for this holder.** Not marginally, and not as a matter of
taste — on four of the four axes that define the product's target buyer.

The fund is **not defective**. It does exactly what its documents say. Global X's own
disclosure is admirably blunt: *"monthly distribution is not guaranteed and may be paid
out of capital… Positive distribution does not mean positive return… distributions may
result in an immediate reduction in the Net Asset Value per Share."* Nobody has been
misled by the issuer. The mismatch is entirely between product and holder.

| The product suits someone who… | This holder |
|---|---|
| **needs income now** | No stated income need. 18, at university. **Mismatch** |
| has **low volatility tolerance** | Untested, but irrelevant — see §8; the real risk is forced selling, not volatility per se. **Not established** |
| has a **short horizon** | ~40 years. **Direct opposite** |
| expects the market to trade **sideways** | No such view has been stated, and an 18-year-old should not be expressing a 40-year sideways view. **Mismatch** |

Four out of four. When a product's target-buyer profile is the *photographic negative*
of the actual buyer, that is not a close call requiring a market forecast to settle.

### 1.2 What the 18% actually is — settled, not arguable

The CEO flagged that a distribution yield is not a return. That is now **demonstrated,
not merely warned about**:

- Trailing 12-month distribution: **HK$1.71/unit** — headline yield **~18%**
- Trailing 12-month **total return** (price change *plus* distributions):
  **−6.43%** (stockanalysis, retrieved 2026-08-10)

An investor who held for the last year received about 18% of their capital in cash and
finished with **less total wealth than they started with**. The cash was, in substantial
part, their own money handed back with a 0.75% annual fee charged for the service.

This is the single most important sentence in this report for the Owner to relay:
**the money arriving each month is not, on the last twelve months' evidence, income.
It is largely the holder's own capital.**

### 1.3 The compounding trap — I add a mechanical point the CEO's note implies

The CEO correctly identified that monthly cash distributions must be reinvested to
compound, and that reinvesting costs money. **§4 makes it worse than that.** With a
**500-unit board lot**, a monthly distribution of roughly HK$0.14–0.15/unit on ~900
units is about **HK$130/month**. One board lot costs **HK$4,320–4,833**. The holder
would need to bank **33 to 37 months** of distributions before they could reinvest a
single lot back into the fund.

**In this instrument, at this position size, reinvestment is mechanically impossible on
any sane timescale.** The distributions cannot compound. They can only accumulate as
idle cash or be spent. For a holder whose entire edge is forty years of compounding,
this is not a drawback — it is a disqualification.

---

## 2. Limit-by-limit check against `config/risk-limits.yaml`

### 2.1 A jurisdictional note I must make first

`config/risk-limits.yaml` governs **皮褸黃 Capital's portfolio**. The HK$8,000 in
question is a **third party's personal holding** on which the Owner has sought this
firm's opinion. I do not have enforcement jurisdiction over an account that is not
ours, and I will not pretend otherwise. What follows applies our limits as an
**advisory suitability benchmark** — the standard this firm would hold itself to — not
as enforceable law over that account. The verdict in §0 is a suitability opinion, and
its force comes from its reasoning, not from a claim of authority I do not have.

### 2.2 `config/portfolio.yaml` IS EMPTY — what that forecloses

```
holdings: []
cash_balance: 0.00      # REPLACE WITH REAL DATA
```

**This is the seventh escalation of this defect.** Six prior escalations are on record
without resolution.

**What I therefore CANNOT conclude:**

- Any position-as-%-of-portfolio figure. `max_single_position` (0.10),
  `max_single_position_drifted` (0.15), `max_sector` (0.35) and
  `max_correlated_cluster` (0.40) are all **ratios with an unknown denominator**. They
  cannot be evaluated. Not "probably fine" — **not computable**.
- `cash_floor` (0.10) — no cash balance on file.
- `max_drawdown` (0.20) — no peak-to-trough series exists for an empty portfolio.
- `max_var_95_1d` (0.03) — a portfolio VaR of an empty portfolio is undefined. I did
  **not** commission Mo Peter, because there is nothing for him to compute. Likewise
  Mario's stress testing: a single-line HK$8,000 third-party holding against a null
  portfolio produces a stress number with no meaning. **I am recording these as
  deliberately not run, with reasons — not as an oversight.** If the Owner populates
  `portfolio.yaml`, I will commission both within the hour.
- `max_adv_participation` (0.05) — plausibly satisfied given the fund's size, but I do
  not hold 3416's average daily volume and will not assert a pass I cannot show.

**What I CAN conclude without it** is everything in §0, §1, §3, §4, §6 and §7. The
suitability verdict does **not** depend on the missing portfolio file. That is worth
stating plainly so the empty file is not used as a reason to defer the decision.

### 2.3 The limits that CAN be assessed

| Limit | Value | Assessment for 3416.HK | Result |
|---|---|---|---|
| `leverage` | `none` | The fund writes calls **covered by held stock**, not on borrowed money. No margin borrowing identified. **Caveat: the prospectus was NOT opened** (egress-blocked), so gearing via derivatives is unverified. | **PASS, unverified** |
| `options.naked_short_options` | `forbidden` | The fund's short calls are covered by the underlying constituents. This is a covered-call fund by construction. | **PASS** |
| `options.covered_only` | `true` | Same. On a look-through basis the fund is compliant with our own options policy. | **PASS** |
| `options.max_options_premium_at_risk` | `0.02` | Caps **aggregate long premium**. This fund is **net short** premium. The limit does not bind. **See §2.4 — that is a hole in the limits file, not a pass.** | **N/A** |
| `per_trade.stop_required` | `true` | No invalidation level has been set by 老詹 for this holding. If this were a firm position it would be a process breach. | **NOT MET** (advisory) |
| `process.live_trading` | `forbidden` | This report is an opinion. No order is transmitted. The Owner executes. | **PASS** |
| `process.committee_approval_required` | `true` | No committee has convened on 3416. See §11. | **OPEN** |

### 2.4 A genuine defect in `risk-limits.yaml` that this name exposes

`options.max_options_premium_at_risk: 0.02` caps **long** premium. **The file contains
no cap at all on short-option exposure acquired indirectly through a fund.**

A portfolio could hold 100% covered-call ETFs — systematically short the right tail of
every asset it owns — and breach nothing in this file. That is precisely the exposure
under review today, and our limits are silent on it.

**Recommendation to the Owner (new, #7):** add a look-through limit, e.g.
`max_short_premium_strategies: 0.10` — no more than 10% of the portfolio in funds whose
primary return driver is selling optionality. I propose it; I do not adopt it silently.

### 2.5 The known unresolved defect — I will not resolve it silently

`max_correlated_cluster: 0.40` versus sleeve targets **AI 0.30 + technology 0.20 =
0.50**. The config is internally inconsistent: the target allocation, if achieved,
breaches the concentration limit by 10 percentage points on day one. **Escalated six
times without resolution. This is the seventh.**

**How it bears on this opinion — honestly:**

- **It does not change the verdict.** 3416 is Chinese financials and consumer internet
  (CCB 7.1%, ICBC 4.9%, Alibaba 8.2%, Tencent 7.4%, Xiaomi 5.9%). It sits in neither
  the `ai` nor the `technology` sleeve as this firm defines them. The 0.40-vs-0.50
  contradiction is not the binding constraint here.
- **It would matter on a look-through basis** if the same person also held our AI/tech
  sleeves — Alibaba, Tencent and Xiaomi are ~21.5% of the fund and are technology
  businesses by any sensible taxonomy, even if not "AI" as the sleeve intends. With
  `portfolio.yaml` empty, that look-through is **not computable**.
- **I decline to pick a side.** Either the cluster limit rises to ≥0.50, or the sleeve
  targets fall to sum ≤0.40. Both are defensible. **It is the Owner's call, not mine**,
  and every day it stays unresolved, every concentration statement this department
  makes carries an asterisk.

---

## 3. The cost arithmetic, completed

### 3.1 What stamp-duty exemption leaves behind

The CEO established that **HK ETFs are exempt from the 0.1% stamp duty** — that is the
largest statutory charge, and it is gone (saving ~HK$8 on HK$8,000). What remains:

| Charge | Standard rate | On HK$8,000 |
|---|---|---|
| HK stamp duty | **EXEMPT for ETFs** | **HK$0** |
| SFC transaction levy | ~0.0027% | ~HK$0.22 |
| AFRC transaction levy | ~0.00015% | ~HK$0.01 |
| HKEX trading fee | ~0.00565% | ~HK$0.45 |
| HKEX trading tariff | ~HK$0.50/trade | ~HK$0.50 |
| CCASS settlement fee | ~0.002%, **min HK$2** | **HK$2.00** (minimum binds) |
| **Statutory + exchange subtotal** | | **≈ HK$3.20 (0.04%)** |

> **UNVERIFIED — flagged.** These statutory rates are **general knowledge, not fetched
> today**; `hkex.com.hk` was not reachable through this environment's egress policy and
> I did not obtain a current schedule. Treat every figure in this sub-table as an
> **ESTIMATE**. **The conclusion below does not depend on them**, because they total
> under HK$4 and are dominated by the brokerage minimum by one to two orders of
> magnitude. That insensitivity is why I am comfortable publishing despite the gap.

### 3.2 One-way and round-trip cost of exiting HK$8,000

"Round trip" here = **sell 3416 + buy the replacement**, which is the transaction the
Owner is actually contemplating.

| Broker minimum (one-way) | One-way total | % of HK$8,000 | **Round trip** | **% of HK$8,000** |
|---|---|---|---|---|
| **HK$0** (Futu, Longbridge — zero-commission HK stocks, 2026) | ~HK$3 | **0.04%** | ~HK$6 | **0.08%** |
| HK$15 | ~HK$18 | 0.23% | ~HK$36 | 0.45% |
| HK$24 (IBKR HK, ~0.08% with low minimum) | ~HK$27 | 0.34% | ~HK$54 | 0.68% |
| HK$30 | ~HK$33 | 0.41% | ~HK$66 | 0.83% |
| HK$50 | ~HK$53 | 0.66% | ~HK$106 | 1.33% |
| **HK$100** (typical retail bank) | ~HK$103 | **1.29%** | ~HK$206 | **2.57%** |

*Broker brackets are illustrative except where named. Futu and Longbridge advertise
HK$0 commission on HK stocks and IBKR HK ~0.08% (search-extracted, 2026-08-10);
**platform fees at some brokers can erase the zero-commission advantage** and were not
verified for this holder's account.*

### 3.3 The conclusion the Owner needs from this table

**Exiting is cheap. Staying is expensive.**

- **Worst realistic case, a bank at HK$100 minimum: 1.29% one-way, 2.57% round trip.**
- The fund's TER alone is **0.75% per year, forever**. So even the worst-case round
  trip costs about **3.4 years of TER** — and is repaid in **ten weeks** against the
  ~14pp/yr total-return gap to the plain index observed over the trailing twelve months
  (§6.3).
- At a zero-commission broker the round trip costs about **HK$6**, which is **0.08%**.

**"It's not worth selling because of the costs" is not an available argument here.** On
these numbers, transaction cost is not a material input to the decision. Anyone
advancing it is looking for a reason not to act.

**Two costs are NOT in the table and both are real:**

1. **Bid-ask spread** — NOT OBTAINED. Add roughly one half-spread each way.
2. **The odd-lot discount on 40–46% of the position** — §4.3. Unquantified, and
   potentially larger than every line item above combined. **This, not commission, is
   the real cost of exiting**, and it is the reason for the binding condition in §7.1.

### 3.4 And on the *forward* plan, the cost problem is fatal on its own

At a HK$100 bank minimum, **10% of every HK$1,000 monthly deposit is consumed before
the market opens** (CEO's table, which I endorse). That alone kills a monthly plan in
any instrument. But §4.2 kills it here even at **zero** commission: HK$1,000 cannot buy
a board lot at any price this fund has traded at.

---

## 4. Board lot and the odd-lot problem — **RESOLVED: 500 units**

### 4.1 The board lot is 500 units

**Board lot = 500 shares/units.** Source: search-engine extraction of the fund's **Key
Facts Statement** (`investments.miraeasset.com.hk/docs/ETF/3416_eKFS.pdf`), retrieved
2026-08-10, which states a *"trade lot size of 500 Shares"* alongside other KFS fields
that independently match our verified facts table (Manager: Mirae Asset Global
Investments (Hong Kong) Limited; base and trading currency HKD; ongoing charges
estimated **0.75%**; distribution **monthly at the Manager's discretion**).

Those corroborating fields all match figures already held from independent sources,
which is why I treat this as **good confidence** rather than moderate. **The PDF itself
was NOT opened** — `investments.miraeasset.com.hk` returned `EGRESS_BLOCKED` on direct
fetch. This is a search-engine extraction of a primary document, not the primary
document. *The Owner can confirm it in thirty seconds on any HK broker app; worth doing.*

This **confirms my pre-termination moderate-confidence figure of 500**, and it is
mechanically decisive in two directions.

### 4.2 Consequence 1 — the HK$1,000/month plan is not executable as designed

| Price case | Board lot | Cost of one lot | HK$1,000/month buys |
|---|---|---|---|
| HK$8.64 (last hard NAV, 23 Jul 2026) | 500 | **HK$4,320** | **0 lots** |
| HK$9.665 (disputed vendor price, undated) | 500 | **HK$4,833** | **0 lots** |

**Under either price, HK$1,000 does not buy one board lot.** The student would have to
bank **4.3 to 4.8 months** of contributions before a single lot is purchasable. The plan
as stated — "add HK$1,000 per month" — **cannot be run monthly in this instrument.** It
is structurally a quarterly-to-five-monthly plan, or it is an odd-lot plan (§4.3).

This is not a preference or a market view. It is arithmetic, and it disposes of the plan
*as written* regardless of anyone's opinion on Chinese equities. **This single fact,
which cost thirty seconds to check and took this firm two sessions to obtain, decides
the forward half of the question on its own.**

### 4.3 Consequence 2 — the odd-lot problem on the existing HK$8,000

The holding is **not a whole number of board lots** under either price:

| Price case | Units held (≈HK$8,000) | Whole board lots | **Odd-lot remainder stranded** |
|---|---|---|---|
| HK$8.64 | ~926 | 1 (500 units) | **~426 units ≈ HK$3,681 — 46% of the position** |
| HK$9.665 | ~828 | 1 (500 units) | **~328 units ≈ HK$3,170 — 40% of the position** |

So roughly **40–46% of the position already sits in an odd lot** under either price.
**The price conflict does not change this conclusion** — it is robust across both cases,
which is a useful property given §6.

**Why this costs money in Hong Kong.** HKEX runs odd lots on a **separate odd-lot /
special-lot board**, not the main continuous auto-matching order book. Odd-lot orders do
not match against board-lot liquidity; they match only against other odd-lot interest,
which for a single ETF is thin. In practice a retail seller either (a) waits, possibly
days, for a counterparty, or (b) sells to a broker/dealer who bids *below* the board-lot
market to compensate for the inventory risk of assembling a full lot.

**Quantification — ESTIMATE ONLY, NOT SOURCED.** I tried to source a measured odd-lot
discount for HK ETFs and **could not**. The venues that would carry it (`hkexnews.hk`,
`hsi.com.hk`, `investments.miraeasset.com.hk`) are egress-blocked, and **I will not
manufacture a number.** What I can state with confidence is the **direction and
mechanism**: the odd lot transacts at or below the board-lot bid, never above, and the
shortfall is real, non-recoverable, and borne entirely by the holder. Logged in §12 as
an unquantified cost on 40–46% of the position.

### 4.4 The decisive point: a *partial* sale is the worst available action

Any partial sale creates a *new* odd lot, and a smaller odd lot is harder to sell than a
larger one. The holder today has one clean board lot plus one odd lot. If the decision
is to exit, exiting **in a single order for the full holding** lets the 500-unit lot
cross on the main board and leaves the existing odd-lot problem to be solved once,
rather than manufacturing a second one.

**BINDING CONDITION: no partial sale. Exit is all-or-nothing.** This is the one
condition in this report that is mechanical rather than judgemental, and it is the one
most likely to be violated by instinct ("I'll sell half and see").

---

## 5. Concentration and correlation assessment

### 5.1 "53 holdings" is diversification theatre

| Measure | Value | Comment |
|---|---|---|
| Number of holdings | 53 | Sounds diversified |
| Top 5 weight | **~33.5%** | Alibaba 8.2 + Tencent 7.4 + CCB 7.1 + Xiaomi 5.9 + ICBC 4.9 |
| Countries | **1** (China/HK) | Single-country |
| Listing venue | **1** (HKEX) | Single-market, single-currency (HKD/CNY-linked) |
| Regulatory regime | **1** (PRC) | Single-jurisdiction policy risk |

**Nominal diversification across correlated names is concentration in disguise.** That
is this department's standing position and it applies squarely here. Fifty-three
Chinese large caps listed on one exchange, exposed to one government's policy cycle,
one currency regime, and one geopolitical relationship, are **not** 53 independent bets.
In a PRC policy shock or a US–China escalation they move together, and the option
overlay provides essentially **no** downside protection beyond the premium received —
the fund keeps substantially the entire downside (CEO's structural note, which I endorse).

### 5.2 Against the limits — what binds and what cannot be evaluated

| Limit | Threshold | Assessment | Result |
|---|---|---|---|
| `max_single_position` | 0.10 | **Denominator unknown** (§2.2). If the HK$8,000 is most of the person's savings, this is **~100% of portfolio in one line — a ~10× breach.** If it is 5% of savings, it passes comfortably. | **NOT COMPUTABLE — branches on §8** |
| `max_sector` | 0.35 | Look-through: financials (CCB + ICBC ≈ 12% of top five alone, plus other H-share banks) and consumer internet are both large. Full sector breakdown NOT OBTAINED. | **NOT COMPUTABLE** |
| `max_correlated_cluster` | 0.40 | The fund is internally ~100% one correlated cluster ("China large-cap equity"). As a *share of the person's portfolio*, unknown. | **NOT COMPUTABLE — but see below** |
| Single-country exposure | *no limit exists* | The file has **no** geographic concentration limit. | **GAP** |

### 5.3 Two more gaps in `risk-limits.yaml` this name exposes

**Recommendation #8 to the Owner:** `risk-limits.yaml` has **no single-country or
single-currency concentration limit**. A portfolio could be 100% one emerging market and
breach nothing. Propose `max_single_country_ex_home: 0.25`.

**Recommendation #9:** there is no limit on **top-5 weight within a single fund**, so a
"diversified ETF" with 33.5% in five names satisfies `max_single_position` on a
line-item basis while being a concentrated bet on look-through. Propose that
`max_single_position` be applied **on a look-through basis** to fund holdings.

Combined with §2.4, that is **three structural gaps** this one review surfaced. I put
them to the Owner as proposals. **I have changed nothing.**

### 5.4 The correlation point that actually matters for this holder

Set the firm's limits aside for a moment. This person is an **18-year-old university
student, presumably in Hong Kong**. Their human capital — future earnings, job
prospects, rent, currency of expenditure — is **already a leveraged long position on
the Hong Kong and Chinese economy.**

Putting their financial savings into 53 Chinese large caps listed in Hong Kong does not
diversify that. **It doubles it.** In the scenario that hurts most — a serious Chinese
downturn — the graduate job market and the portfolio fall together, and that is exactly
the scenario in which they would be forced to sell.

**This is the single largest concentration risk in the case, and no line in
`risk-limits.yaml` captures it**, because our limits were written for a firm balance
sheet, not for a person with human capital. I flag it because ignoring it would be a
failure of the mandate even though no limit is breached.

---

## 6. The price conflict — HK$8.64 vs HK$9.63 · **RESOLVED in favour of HK$8.64**

### 6.1 The conflict as referred to me

- **HK$8.64** — last hard NAV print, **23 July 2026** (CEO).
- **HK$9.63 NAV / HK$9.665 price** — vendor page queried 2026-08-10, **no trustworthy
  date**. HK$9.63 is precisely the figure previously identified as stale and corrected
  down to HK$8.64. The two differ by ~12%.

### 6.2 How I resolved it — an internal-consistency test, not a new price print

I could not obtain a fresh authoritative print (every primary venue is egress-blocked).
So instead I tested whether HK$9.63 is **arithmetically compatible** with the other
figures in the same vendor dataset. It is not.

From stockanalysis (all retrieved 2026-08-10, all from the same dataset, so mutually
consistent by construction):

- 52-week range: **HK$8.230 – HK$10.970**
- Trailing 12-month distribution: **HK$1.71/unit**
- Trailing 12-month **total return: −6.43%**

Total return ≈ (P₁ − P₀ + D) / P₀. Solving for the price one year ago (P₀) given
D = 1.71 and total return = −6.43%:

| Assumed current price P₁ | Implied price one year ago P₀ | Consistent with 52-wk high of HK$10.97? |
|---|---|---|
| **HK$8.64** | (8.64 + 1.71) / 0.9357 = **HK$11.06** | ~0.8% over the high — **within approximation error. PLAUSIBLE** |
| **HK$9.63** | (9.63 + 1.71) / 0.9357 = **HK$12.12** | **10.5% ABOVE the 52-week high. IMPOSSIBLE** |

*(Approximation: treats twelve monthly distributions as a single lump. That biases P₀
slightly high in both rows and does not affect the ranking.)*

**HK$9.63 cannot be reconciled with the fund's own 52-week range.** HK$8.64 can.

**Corroborating signal.** The vendor page reporting NAV 9.63 also reports *"+1.71% over
the past month"* — and **1.71 is exactly the trailing-12-month distribution per unit in
HKD**. A percentage field carrying the numeric value of an unrelated currency field is a
classic scraper field-collision. That page's numbers should not be relied on.

### 6.3 The number that actually answers the central question

The CEO identified the **HSCEI total return since 2024-02-28** as the highest-value
number obtainable, because it settles whether the overlay cost more than it paid. The
HSCEI factsheet PDF on `hsi.com.hk` remains unreachable. **But I got the answer by
another route — two, in fact, and they agree.**

**Route 1 — the manufacturer's own admission (strongest evidence available).**
Global X's own published commentary states that **3416 underperformed its underlying
HSCEI Index since launch**, attributing it to the September 2024 China rally (HSCEI
+20% in that single month). Their defence: *excluding* the September 2024 rally, 3416
outperformed HSCEI on a total-return basis.

**That defence is the CEO's structural thesis stated in the issuer's own words.**
"Excluding the largest upward move, the strategy that sells large upward moves did
better" is not a mitigating argument — **it is the mechanism.** Right-tail months are
not anomalies to be excluded from the record; over forty years they *are* the record.
Long-run equity returns are overwhelmingly delivered by a small number of very large
up-moves, and this product's design is to sell them. The manufacturer has confirmed the
diagnosis while presenting it as a defence.

**Route 2 — a plain-index proxy (ESTIMATE, and I show the working).**
Direct HSCEI total-return data is blocked, so I used **2828.HK (Hang Seng China
Enterprises Index ETF)**, an unlevered plain-vanilla tracker, as a proxy:

| Period | 2828.HK (plain HSCEI) | 3416.HK (covered call) |
|---|---|---|
| Calendar 2024 | **+30.45%** | — |
| Calendar 2025 | **+25.06%** | — |
| **Trailing 12m to Aug 2026** | **+7.42%** | **−6.43%** |
| Avg annual since 2024-02-28 | not directly obtained | **+10.50%** (single source, UNVERIFIED) |

2024 × 2025 compounded for the plain index: 1.3045 × 1.2506 = **+63.2%** over two
calendar years, ≈ **+27.7% annualised**. 3416's reported +10.50% average annual since
inception is **roughly two-fifths of that**, over an overlapping period.

> **Caveats, stated plainly.** 2828.HK is a proxy, not HSCEI itself, and carries its own
> fee. Calendar-year figures do not align with 3416's 2024-02-28 inception. 3416's
> +10.50% is a single unverified source. **I therefore do not assert a precise
> underperformance figure.** What survives every caveat: **the direction is not in
> doubt, the magnitude is large, and the issuer concedes it.**

**The trailing-twelve-month comparison is the cleanest and needs no proxy caveat about
periods: +7.42% for the plain index versus −6.43% for the covered-call version. A gap
of roughly 14 percentage points, in one year, in exchange for an 18% "yield" that was
not income.**

### 6.4 Which of my conclusions depend on the price, and which do not

| Conclusion | Depends on resolving HK$8.64 vs HK$9.63? |
|---|---|
| §0 verdict — unsuitable, veto the monthly plan | **NO** — structural + empirical |
| §4.2 HK$1,000 cannot buy a board lot | **NO** — true at both prices |
| §4.3 40–46% of the position is an odd lot | **NO** — true at both prices |
| §3 exit costs are immaterial | **NO** — the notional is ~HK$8,000 either way |
| §7 sell triggers | **NO** — none are price-based, by design |
| Exact unit count (926 vs 828) | **YES** — use 8.64 → ~926 units, pending broker confirmation |
| Exact HKD value of the position | **YES** — but only ±12%, which changes nothing |

**Every load-bearing conclusion in this report is invariant to the price conflict.**
That is not luck; I structured the analysis so that it would be, precisely because the
price could not be independently verified. **The Owner should read the actual unit count
off the broker statement** — that is authoritative and takes ten seconds, and it makes
this entire section moot.

---

## 7. Sell triggers to pre-commit to

The Owner asked "when should I sell." Below are **conditions**, not dates or price
targets, split as instructed into administrative and thesis-breaking. **Pre-commit to
them in writing before acting** — the whole value of a pre-commitment is that it is made
before the emotion of the moment.

### 7.1 ADMINISTRATIVE — product mismatch → exit when cheapest (these are BINDING)

The mismatch is established. These govern *how*, not *whether*.

| # | Condition | Rationale |
|---|---|---|
| **A1** | **NO PARTIAL SALE. One order, whole position.** | §4.4. A partial sale manufactures a second, smaller, harder-to-sell odd lot. This is the most important operational instruction in the report. |
| **A2** | **Confirm the board lot and the exact unit count on the broker statement first.** | §4.1, §6.4. Ten seconds; makes the price conflict irrelevant and confirms the 500 figure from a primary source. |
| **A3** | **Execute at a zero- or low-commission broker if one is already held.** Do **not** open a new account just to save HK$100. | §3.2. The saving is real but small; account-opening friction is a classic reason plans die unexecuted. Do not let cost optimisation become procrastination. |
| **A4** | **Trade during the continuous session, not the closing auction.** Use a **limit order**, never market. | Thin books punish market orders. A limit order near the prevailing bid costs patience, not money. |
| **A5** | **Expect the odd-lot portion to take longer and fill worse.** Do not panic-cut the price on the odd lot. | §4.3. Unquantified but directionally certain. A broker's odd-lot desk may quote it as a single transaction — ask. |
| **A6** | **There is NO tax reason to delay.** Hong Kong levies no capital gains tax on individuals and no dividend withholding for residents, and ETFs are stamp-duty exempt. | Removes the usual "don't sell, tax lock-in" objection entirely. It does not apply here. |
| **A7** | **Do not wait for a price.** No level on the HSCEI makes this product suitable for a 40-year horizon. | §0. Waiting for a "better price" to exit a product you should not own is a second mistake stacked on the first. |

### 7.2 THESIS-BREAKING — conditions that would justify exit even for a holder the product DOES suit

| # | Trigger | Status |
|---|---|---|
| **T1** | **Distribution is largely return of capital** — i.e. trailing 12m *total* return is negative or far below the distribution yield. | **⚠ ALREADY FIRED.** Trailing 12m total return **−6.43%** against an ~18% headline yield (§1.2, §6.3). This is the trigger the CEO named as the thesis-breaker, and **it has fired.** |
| **T2** | **Sustained underperformance of the plain index** on a total-return basis. | **⚠ ALREADY FIRED.** The issuer itself concedes underperformance since launch (§6.3), and the trailing-12m gap to 2828.HK is ~14pp. |
| **T3** | **NAV makes successive new lows while distribution per unit is maintained** — the classic ROC signature: paying out of a shrinking pot. | **Monitor.** 52-week low HK$8.230 and NAV ~HK$8.64 versus a likely ~HK$10.00 launch NAV (unconfirmed). |
| **T4** | **Distribution per unit is cut.** | **⚠ APPEARS TO HAVE FIRED.** Secondary sources indicate HK$0.15/unit (Jul 2025) → HK$0.14/unit (Nov 2025), a ~6.7% cut. **Search-extracted, single-source, NOT VERIFIED.** |
| **T5** | **Manager changes the option-writing policy** — deeper in-the-money strikes, higher coverage ratio, different tenor. | **Monitor.** Would change the product without changing its name. Disclosed in the monthly commentary. |
| **T6** | **Persistent premium/discount to NAV beyond ~1%**, or a visible widening of the bid-ask. | **NOT OBTAINED** — no spread data. |
| **T7** | **Strategy capacity strain.** AUM appears to have grown very fast (~HK$1.46bn May 2025 → ~HK$7.3bn Nov 2025 → HK$22.37bn on file). A covered-call fund's returns depend on HSCEI index-option liquidity; rapid asset growth can force worse strikes or worse fills. | **Monitor — and note these AUM figures come from three different secondary sources and may not be comparable.** Rapid growth is not itself a problem; it is a reason to watch T5. |

**The material finding: T1, T2 and probably T4 have already fired.** The Owner is not
being asked to *anticipate* a thesis break and decide pre-emptively. **The thesis has
already broken on the available evidence.** That, rather than the horizon argument
alone, is what converts my opinion from "unsuitable, consider exiting in due course" to
"unsuitable, and the empirical case for holding has also failed."

### 7.3 What NOT to pre-commit to

- **Not** a price target. There isn't one.
- **Not** "sell when it recovers to what I paid." That is the disposition effect, and it
  is how a small mistake becomes a long one. The purchase price is not a fact about the
  fund.
- **Not** "sell after the next distribution." A distribution reduces NAV by
  approximately its own amount. Total wealth is unchanged. There is nothing to capture
  by waiting, and HK's tax treatment (A6) removes even the second-order reason.

---

## 8. The gating question — is HK$8,000 most of that person's savings?

**Asked three times. Still unanswered. I am not blocking on it.** Here is my opinion in
both branches, so it is usable the moment the Owner supplies the answer.

### BRANCH A — the HK$8,000 is MOST of their savings (say, >50%)

**Verdict hardens. This becomes urgent, and the problem changes character.**

- `max_single_position` (0.10) is breached by roughly **10×**. `cash_floor` (0.10) is
  breached — there is effectively no cash. `max_correlated_cluster` (0.40) is breached
  at ~100%. On our own standards this is not a portfolio; it is a **single leveraged bet
  on China, held by someone with no reserve.**
- **The problem is no longer product selection. It is that this money should not be in
  equities at all.** The CEO's fifth point is the governing one: *money that might be
  needed within five years does not belong in equities*, and **the real risk for a
  student is being forced to sell at a bottom to pay for something.**
- Compounding §5.4: their savings and their job prospects are the same bet. A China
  downturn hits the portfolio and the graduate job market simultaneously — the exact
  moment they would be forced to liquidate.
- **My recommendation in Branch A:** exit per §7.1, and the proceeds go to **cash /
  a deposit as an emergency reserve first**, not into a different equity fund. Build
  three to six months of living costs. Only the surplus above that reserve should be
  invested at all, and only then does the "which vehicle" question become live.
- **The urgency rises but the method does not change** — §7.1 still binds. Urgent does
  not mean careless, and A1 (no partial sale) still holds.

### BRANCH B — the HK$8,000 is a SMALL part of their savings (say, <20%), with a real cash reserve behind it

**Verdict stands, urgency drops substantially.**

- No limit breach is demonstrable, though still not computable without `portfolio.yaml`.
- 3416 remains **unsuitable** for the reasons in §1 and §6.3 — those are structural and
  empirical, not portfolio-weight-dependent — but it is now a **wealth-optimisation
  question, not a safety question.**
- **My recommendation in Branch B:** exit per §7.1 at leisure, with the operational
  conditions strictly observed. Redeploy into a broad, low-cost, **accumulating** (not
  distributing) global equity fund with **no option overlay** — the exact opposite
  profile on the one axis that matters at 18: keep the right tail, and let distributions
  reinvest automatically rather than requiring 33 months of saved cash to buy a lot
  (§1.3). **Naming a specific replacement is outside my mandate** — that is Morris
  (PM) / Zac (sizing), and it needs a committee.

### What is common to both branches

The forward plan is **VETOED either way** (§4.2 is mechanical). The **existing HK$8,000
should be exited either way.** The branches differ only in **urgency** and in **where
the proceeds go** — emergency cash reserve (A) versus a better long-horizon equity
vehicle (B).

**That is the practically important finding: the Owner does not need the answer to the
gating question in order to act on either decision.** They need it to decide *where the
money goes next*. So the gating question should be asked a fourth time — but it must not
be allowed to delay §7.1 for a seventh week.

---

## 9. Ranking the decisions by materiality — testing the CEO's 15× claim

**The CEO's standing view:** where the future monthly HK$1,000 goes is worth roughly
**15×** the HK$8,000 exit decision. **I tested it independently. I agree with the
ranking; my arithmetic puts the multiple at ~12×, not 15×.**

### 9.1 The arithmetic

**Assumptions (stated as assumptions, not forecasts — I am not predicting markets):**
- Horizon 40 years.
- A **3 percentage point** annual return difference between a suitable vehicle and an
  unsuitable one — **deliberately conservative**, well below the ~14pp trailing-12m gap
  observed in §6.3, because one year is not a forward estimate and I will not extrapolate it.
- Illustrative rates: 10%/yr (suitable) versus 7%/yr (unsuitable).
- HK$1,000/month ≈ HK$12,000/yr, contributed annually in arrears for simplicity.

**Decision 1 — the existing HK$8,000, held 40 years:**
- At 10%: 8,000 × 1.10⁴⁰ = 8,000 × 45.26 = **HK$362,100**
- At 7%: 8,000 × 1.07⁴⁰ = 8,000 × 14.97 = **HK$119,800**
- **Value at stake ≈ HK$242,300**

**Decision 2 — the future HK$12,000/yr for 40 years:**
- At 10%: 12,000 × [(1.10⁴⁰ − 1)/0.10] = 12,000 × 442.59 = **HK$5,311,000**
- At 7%: 12,000 × [(1.07⁴⁰ − 1)/0.07] = 12,000 × 199.64 = **HK$2,395,700**
- **Value at stake ≈ HK$2,915,300**

**Ratio: 2,915,300 / 242,300 ≈ 12.0×**

### 9.2 Verdict on the claim — **AGREE, with a refinement**

**The CEO's ranking is correct and the order of magnitude is right.** My 12.0× versus
his 15× is not a disagreement worth having: the ratio is mildly sensitive to the assumed
return gap and to contribution timing (monthly rather than annual contributions raise
it slightly), and it lands in a **~10× to 14×** band under any reasonable assumption
set. It is emphatically **not 1×** and **not 100×**.

**Note the two competing effects, since the naive answer is wrong in both directions.**
On contributed capital alone the ratio looks like 60× (HK$480,000 of future
contributions versus HK$8,000 today). Time-weighting cuts that hard, because the
HK$8,000 compounds for the full 40 years while the average future contribution compounds
for only about 20. **60× on capital becomes ~12× on outcome.** Anyone quoting either
60× or 1× has done half the arithmetic.

### 9.3 The resulting ranking of decisions

| Rank | Decision | Value at stake | Effort | Status |
|---|---|---|---|---|
| **1** | **Where the future HK$1,000/month goes** (and whether it is HK$1,000, and whether it starts at all) | **~HK$2.9m** | Moderate — needs a committee | **VETOED into 3416** (§4.2). Replacement not yet chosen. |
| **2** | **Whether an emergency cash reserve exists before any of this** (§8 Branch A) | Potentially the whole plan — a forced sale at a bottom destroys the compounding permanently | Low | **BLOCKED on the unanswered gating question** |
| **3** | **Exit the existing HK$8,000** | **~HK$242k** | Low — one order | **APPROVED WITH CONDITIONS** (§7.1) |
| **4** | **Execution mechanics** — broker choice, lot handling, commission | ~HK$200 one-off (§3.2), plus the unquantified odd-lot cost (§4.3) | Low | Conditions binding (§7.1) |
| **5** | **Timing the exit** | **≈ zero** | — | **Do not spend time here.** §7.3. |

**The practical implication, and the reason this ranking is in the report:** the firm has
now spent two sessions and four lost reports on decision #3, which is worth about
one-twelfth of decision #1 — and decision #1 has not been started. **That is a
misallocation of the firm's attention, and it is mine to name.**

**One qualification I will not let the 12× hide.** Decision #2 — the emergency reserve —
is not a return-optimisation question and does not belong on the same axis. If the
HK$8,000 is most of this person's savings, **a forced liquidation at a market bottom
does not cost 3 percentage points a year; it can end the forty-year compounding
altogether.** Ranked by expected value it sits third. Ranked by *survival*, which is
this department's actual mandate, **it is first.** Upside is not my department.

---

## 10. Risk score — input to committee

### **22 / 100 for this holder**

*Convention: higher = more acceptable, consistent with the BE (18/100) and INTC (28/100)
reviews in `config/watchlist.yaml`. Scores below ~40 carry a CRO veto.*

| Component | Score | Weight | Note |
|---|---|---|---|
| Horizon fit | **5/100** | 30% | ~40-year horizon against a product that sells the right tail monthly. The worst possible pairing. |
| Empirical performance vs plain index | **15/100** | 25% | Issuer concedes underperformance since launch; −6.43% vs +7.42% trailing 12m (§6.3). |
| Distribution quality | **15/100** | 15% | Negative total return alongside an ~18% yield = substantial return of capital (§1.2). |
| Executability of the stated plan | **0/100** | 10% | HK$1,000 cannot buy a 500-unit board lot at any price this fund has traded (§4.2). |
| Concentration | **25/100** | 10% | Top 5 ~33.5%, single-country, single-market, and correlated with the holder's own human capital (§5.4). |
| Product integrity / issuer disclosure | **75/100** | 5% | **The fund is not defective.** Disclosure is clear and candid, TER 0.75% is fair for an active overlay, AUM is substantial. Credit where due. |
| Cost of exiting | **85/100** | 5% | Cheap (§3.2). Not an obstacle. |

**Weighted ≈ 22/100.**

### The score is about the pairing, not the product

**As a product for its intended buyer** — an income-seeking holder with a short horizon,
low volatility tolerance and a sideways view — **I would score 3416 around 60/100**: it
does what it says, discloses candidly, charges fairly, and has real scale. The 38-point
gap between 60 and 22 **is the suitability mismatch, and it is the entire finding of
this report.**

I record this deliberately. A veto that reads as "bad fund" invites the reply "but look
at the yield." A veto that reads as **"good fund, wrong owner"** cannot be argued with
on return grounds — **and return arguments are not my department in any case. Survival
is.**

---

## 11. Escalations to the Owner

Per standing rules, a CRO veto is escalated, not overridden. Escalating now:

1. **VETO on the HK$1,000/month plan into 3416.HK** (§0, §4.2). Mechanically
   impossible as designed *and* structurally wrong for the horizon.
2. **VETO on holding 3416.HK as a 40-year core position** (§0, §1).
3. **`config/portfolio.yaml` IS STILL EMPTY — seventh escalation.** Four
   concentration limits, the cash floor, the drawdown budget and the VaR ceiling are
   **all uncomputable**. Mo Peter (VaR) and Mario (stress) were **deliberately not
   commissioned** because there is no portfolio to compute against — recorded as a
   reasoned omission, not an oversight (§2.2). **This department cannot certify
   "portfolio inside all limits at all times" while its primary state file is empty.
   That KPI is currently unmeasurable and I decline to report it as met.**
4. **`max_correlated_cluster: 0.40` vs sleeve targets summing to 0.50 — seventh
   escalation.** Does not change today's verdict (§2.5). Still needs a decision: raise
   the cluster limit to ≥0.50, or cut the sleeve targets to ≤0.40. **I will not pick
   one silently.**
5. **NEW — three gaps in `risk-limits.yaml` surfaced by this review** (§2.4, §5.3).
   Proposed, not adopted:
   - `max_short_premium_strategies: 0.10` — the file caps long option premium at 2% but
     has **no** limit on short-optionality funds.
   - `max_single_country_ex_home: 0.25` — the file has **no** geographic concentration limit.
   - Apply `max_single_position` **on a look-through basis** into funds — a "53-holding
     ETF" with 33.5% in five names currently passes trivially.
6. **The gating question is unanswered after three requests** (§8). **Asking a fourth
   time — but it must not delay §7.1 again.** Both branches point to exit; they differ
   only in urgency and destination.
7. **Committee.** `process.committee_approval_required: true`. My recommendation:
   **do not convene a committee on 3416** — the veto is clear, both grounds are
   independent, and this is a third-party personal holding, not a firm position.
   **Convene one on decision #1 instead** — the replacement vehicle for the monthly
   contributions, which §9 shows is worth ~12× more and has not been started.
8. **Egress policy.** Every primary document remains unreachable (§12). **This firm has
   now produced a formal opinion on this security without opening a single primary
   document.** That is a standing institutional risk, not a 3416 problem. **The
   board-lot figure — mechanically decisive, obtainable free in thirty seconds on a
   broker app — cost this firm two sessions.** Cheap human verification of a few
   decisive facts would outperform any amount of agent time under this egress policy.

---

## 12. NOT OBTAINED register

### Resolved since the CEO's interim note (2026-08-04)

| Item | Status |
|---|---|
| **Board lot size** | **RESOLVED — 500 units.** KFS extraction, good confidence; PDF not opened (§4.1). |
| **Whether the overlay cost more than it paid** | **RESOLVED, directionally.** Issuer concedes underperformance since launch; −6.43% vs +7.42% trailing 12m vs 2828.HK (§6.3). Precise magnitude still estimated. |
| **Distribution composition (income vs return of capital)** | **RESOLVED by inference, not by disclosure.** A −6.43% total return alongside an ~18% distribution is only possible if much of the distribution is capital. **The manager's actual line-item breakdown is still NOT OBTAINED.** |
| **Price conflict HK$8.64 vs HK$9.63** | **RESOLVED in favour of HK$8.64** by internal-consistency test against the 52-week range (§6.2). Not a fresh authoritative print. |
| **Realistic broker minimums** | **PARTIALLY RESOLVED.** Futu/Longbridge HK$0 on HK stocks, IBKR HK ~0.08% (2026 search extraction). **This holder's actual broker: still unknown.** |

### Still NOT OBTAINED

| # | Item | Why it matters | Blocker |
|---|---|---|---|
| 1 | **Odd-lot discount, quantified** | Directly costs 40–46% of the position on exit (§4.3). Direction certain, magnitude unknown. | All venues egress-blocked |
| 2 | **HSCEI total return since 2024-02-28, precisely** | Would replace the 2828.HK proxy estimate | `hsi.com.hk` PDF blocked |
| 3 | **Distribution composition, per the manager's own line-item disclosure** | Would convert §1.2 from inference to fact | Monthly factsheet PDF blocked |
| 4 | **NAV at inception** (likely HK$10.00 — *"typically" is not a source*) | Would fix cumulative return exactly | Blocked |
| 5 | **This holder's actual broker and its minimum** | Swings exit cost from HK$6 to HK$206 (§3.2) | **Only the Owner can supply** |
| 6 | **Is the HK$8,000 most of their savings?** | Branches urgency and destination (§8) | **Only the Owner can supply — asked 4×** |
| 7 | **Bid-ask spread / premium-discount to NAV** | Second unquantified exit cost | No market-depth source |
| 8 | **Average daily volume** | `max_adv_participation` (0.05) untestable | No source |
| 9 | **Full sector breakdown of the 53 holdings** | `max_sector` (0.35) untestable on look-through | Only top-5 obtained |
| 10 | **Portfolio context — `portfolio.yaml` is empty** | Four concentration limits, cash floor, drawdown, VaR all uncomputable (§2.2) | **Owner — escalated 7×** |
| 11 | **Confirmation the fund uses no gearing** | `leverage: none` marked PASS-unverified (§2.3) | Prospectus blocked |
| 12 | **Current HKEX/SFC statutory fee schedule** | §3.1 rates are general knowledge, not fetched. **Conclusion insensitive — they total <HK$4.** | Not reachable |
| 13 | **Distribution cut HK$0.15 → HK$0.14 (T4)** | Single secondary source, unverified | Factsheet blocked |
| 14 | **AUM reconciliation** | Three sources give HK$1.46bn (May 25) / HK$7.3bn (Nov 25) / HK$22.37bn. Plausible as growth, but **not verified as a comparable series** | Blocked |

### Blocked hosts (egress policy — HTTP 403 / EGRESS_BLOCKED)

`hkexnews.hk` · `finance.yahoo.com` · `stooq.com` · `alphavantage.co` ·
`data.nasdaq.com` · `hsi.com.hk` · `chinaamc.com.hk` ·
**`investments.miraeasset.com.hk` (NEWLY CONFIRMED BLOCKED, 2026-08-10 — the issuer's
own KFS, factsheets and monthly commentaries all live here)**

`tradingkey.com` is **blacklisted firm-wide** as price-data-unusable and is not cited.

**Not a single primary document was opened for this review.** Every figure is a
search-engine extraction or a secondary source, dated 2026-08-10 unless stated. Per
standing rule 5, **no figure here is invented**, and every estimate is marked as one.

---

## Sourcing

All retrieved **2026-08-10** via WebSearch; **WebFetch was blocked on every attempt.**

- Board lot 500 / KFS fields — search extraction of `investments.miraeasset.com.hk/docs/ETF/3416_eKFS.pdf`
- Issuer admission of underperformance vs HSCEI since launch — Global X ETFs HK research
  ("Covered Call ETF 2024 Review") and Mirae Asset covered-call monthly commentaries
- 3416 trailing-12m total return −6.43%, 52-week range HK$8.230–10.970, NAV HK$8.64,
  TER 0.75%, holdings/top-5 — stockanalysis.com
- 2828.HK 2024 +30.45%, 2025 +25.06%, trailing 12m +7.42% — stockanalysis / Yahoo extraction
- Return-of-capital disclosure language — globalxetfs.com.hk fund and campaign pages
- Broker commission landscape 2026 — futuhk.com, longbridge.com, interactivebrokers.com.hk,
  moneysmart.hk (search extraction)
- Distribution HK$0.15 (Jul 2025) / HK$0.14 (Nov 2025), AUM waypoints — talkmoney.com.hk,
  25y-retirement.com (secondary, unverified)

---

**John, Chief Risk Officer · Department 6 · 皮褸黃 Capital**

Research and decision support. **Not financial advice.** Markets cannot be reliably
predicted. No agent of this firm places orders; the Owner executes.

*A veto is escalated to the Owner, never overridden. I cannot be argued out of it with
return arguments — upside is not my department. Survival is.*
