# MiniMax Group Inc (HKEX: 0100) — Economic Moat Assessment

**Analyst:** 菲比斯, Economic Moat Analyst, Dept. 2 (Equity Research)
**Date:** 2026-07-30
**Ticker:** 0100.HK / SEHK:100
**For:** CIO → Investment Committee

---

## 0. Anti-anchoring disclosure (firm lesson L-003) — READ FIRST

The firm's last five verdicts were negative. I am required to state, **before** giving my
answer, what evidence would have forced a **WIDE** rating, and whether I found it.

**What would have made me rate this moat WIDE:**

| # | Required evidence | Found? |
|---|---|---|
| W1 | ROIC sustainably above cost of capital, or a credible path with gross profit covering R&D | **No.** FY2025 gross profit ≈ US$20.1m (computed: 25.4% × $79.038m) vs R&D US$252.8m. R&D is ~12.6× gross profit. |
| W2 | Demonstrated pricing power — a price increase absorbed without volume/user loss | **No — the opposite.** MiniMax repriced the Coding Plan on 1 Jun 2026 (per-call → per-token) and opened a **refund portal on 2 Jun 2026**, plus compensation quota boosts. A failed pricing test, publicly. |
| W3 | Consumer retention/share durability across a cycle | **No.** Talkie + Xingye MAU reportedly **−60% QoQ in Q4 2025** (36kr / KuCoin, secondary). |
| W4 | A structural cost-per-token advantage vs Chinese peers | **No.** M3 at $0.30/$1.20 per 1M tokens is *more expensive* than DeepSeek V4-Flash ($0.14/$0.28) and Qwen Flash ($0.05 input). |
| W5 | Proprietary, defensible model capability | **No — and negatively.** Anthropic (23 Feb 2026) attributes ~13m distillation exchanges to MiniMax, the largest of three named labs. Models are also open-weighted, giving away what IP exists. |
| W6 | Rising gross margin in the *moat-bearing* segment | **No.** The high-margin segment (Open Platform, 69.4% GM) is the *commoditised* API business; the allegedly moated consumer segment runs **4.7% GM**. |

**I found none of the six.** I did find one genuinely strong bull data point (§2, brand/organic
pull) and I have weighted it explicitly rather than dismissing it. My rating is not a
continuation of the house streak — it is what the six failed tests produce. If W2 or W3
reverse in the FY2026 interim report, this rating should be revisited immediately.

---

## 1. The numbers on the table

All figures sourced and dated. "Computed" = arithmetic on cited figures, not an estimate.

### Income statement (FY2025, reported ~Mar 2026)

| Item | 2023 | 2024 | 2025 | Source |
|---|---|---|---|---|
| Revenue (US$m) | 2.46 | 30.52 | **79.038** (+158.9%) | Prospectus / FY25 results |
| Gross margin | −24.7% | 12.2% | **25.4%** (+13.2pp) | Prospectus / FY25 results |
| — AI-native (consumer) rev | — | 21.8 | **53.1** (+143.4%), 67.2% of total | FY25 annual report |
| — Open Platform (B2B API) rev | — | — | **26.0**, 32.8% of total | FY25 annual report |
| R&D expense (US$m) | — | 189.0 | **252.8** (+33.8%) | FY25 results |
| Selling & distribution (US$m) | — | 87.0 | **51.9** (−40.3%) | FY25 results |
| Adjusted net loss (US$m) | — | 244.2 | **250.9** | FY25 results |
| Net loss (RMB) | — | — | **~1.75bn** | Caixin/Nikkei, Jun–Jul 2026 |

**Segment gross margin, 9M 2025 (prospectus): consumer 4.7% · enterprise 69.4%.**
This single line is the most important fact in the file. It is discussed in §3.1.

**Computed ratios (my arithmetic on the above):**
- FY2025 gross profit ≈ **US$20.1m**
- R&D / gross profit ≈ **12.6×**
- S&D / gross profit ≈ **2.6×**
- (R&D + S&D) / gross profit ≈ **15.2×**
- Consumer segment gross profit, 9M25 ≈ **US$1.7m** (4.7% × 67.7% × $53.44m)

### Operating metrics

| Metric | Value | Date | Source |
|---|---|---|---|
| MAU (AI-native products) | 3.1m → 19.1m → **27.6m** | 2023 / 2024 / 9M25 | Prospectus |
| Talkie + Xingye MAU | **−60% QoQ** | Q4 2025 | 36kr / KuCoin (secondary — *see caveat*) |
| Paying users | **1.7716m** | 9M25 | Prospectus |
| ARPPU | US$6 → **US$15** | 2023 → 9M25 | Prospectus |
| Total users | ~212m (brief) / **236m** (Dealroom) | FY2025 | Dealroom / company |
| ARR | **US$150m** → **>US$300m** | Feb 2026 → ~May 2026 | kr-asia / KuCoin |
| M2-series daily token consumption | **6× Dec-2025 level**; Coding Plan **10×** | Feb 2026 | Company |
| Paying conversion (computed) | **6.4%** (1.77m / 27.6m) | 9M25 | Computed |

### Market data (context, not moat evidence)

| Item | Value | Date |
|---|---|---|
| IPO price | HK$165.00 | 9 Jan 2026 |
| Day-1 close | HK$345 (+109%) | 9 Jan 2026 |
| Intraday peak | HK$1,238 | 18 Mar 2026 |
| Price | HK$451.80 | 10 Jun 2026 |
| Price | **HK$209.40** (prev. close 197.20) | 29 Jul 2026 |
| Drawdown from peak (computed) | **−83%** | — |
| Lock-up release | 153m shares = **48.9% of equity** | 9 Jul 2026 |
| Refinancing | HK$16bn: 35.6m Class A @ HK$268 (HK$9.54bn) + HK$6.5bn zero-coupon CB due 2027 @ HK$335 conv. | 10 Jul 2026 |

> **Data-quality caveats.** (a) Market-cap figures are irreconcilable across sources
> (HK$263.45bn on 29 May per 36kr; HK$61.85bn late Jul per stockanalysis; "HK$410bn → HK$109bn"
> per KuCoin). I do **not** rely on any market-cap number; the price series above is
> internally consistent and sufficient. (b) tradingkey.com excluded per firm blacklist.
> (c) The −60% QoQ MAU figure is **secondary-source only** (36kr, KuCoin); I could not
> confirm it in a primary filing — WebFetch was returning HTTP 403 across essentially all
> domains this session, so all primary PDFs (hkexnews) were **not obtained**. Treat as
> strong-but-unconfirmed. It is corroborated qualitatively by 36kr's "C-end data declined
> significantly" and by the app-store/regulatory events in §4.

---

## 2. The strongest bull argument I found — stated at full strength

**Growth got cheaper, not more expensive.**

Revenue rose **+158.9%** while selling & distribution expense **fell 40.3%**, from
US$87.0m to US$51.9m. The company attributes this to organic growth and user referrals.

Do the arithmetic on the shape of that:
- 2024: S&D was **2.85×** revenue (87.0 / 30.52)
- 2025: S&D was **0.66×** revenue (51.9 / 79.04)

That is a 4.3× improvement in marketing efficiency in one year. This is the single
cleanest counter to the "growth is bought" thesis, and it is a real, audited,
company-reported number — not a narrative. Businesses whose growth is purely bought do not
cut acquisition spend by 40% and triple revenue. Something is pulling users in.

Supporting it: ARR went US$150m (Feb 2026) → >US$300m (May 2026), and M2-series daily token
consumption in Feb 2026 was 6× the Dec 2025 level (Coding Plan 10×). S&P Global Market
Intelligence (Apr 2026) projects revenue of US$219m in 2026 and US$5.8bn by 2030.

**Why I do not convert this into a moat rating.** Cheap growth is evidence of *product-market
fit*, not of *defensibility*. The two are constantly confused in this sector. A moat is
tested by what happens when a competitor attacks price or when you raise yours — and both
of those tests were run in H1 2026, and MiniMax failed both (§3.3, §3.4). Also note the
S&D cut coincides with the Q4-2025 MAU collapse: if you stop buying users and your users
fall 60% QoQ, the efficiency gain may be *arithmetic from a shrinking denominator*, not
earned pull. I cannot resolve which it is without the FY2026 interim segment data.

---

## 3. Evidence by moat source

### 3.1 Switching costs — **NONE** (consumer) / **NONE** (API)

**Consumer (Talkie/Xingye — 67.2% of revenue).** In theory this is the best candidate:
users build character relationships and accumulate chat history, which is emotionally and
practically costly to abandon. That is a genuine mechanism.

- *Strongest supporting evidence:* prospectus reports niche characters sustain distinct
  high-retention user groups (NPC popularity does not follow a power law), and ARPPU rose
  US$6 → US$15, consistent with deepening engagement among those who stay.
- *Strongest counter-evidence:* **Talkie + Xingye MAU −60% QoQ in Q4 2025.** A user base
  with real switching costs does not lose 60% in a quarter. Whatever attachment exists is
  weaker than the friction of an app-store removal and a content rectification.
- *Killer detail:* the consumer segment's **4.7% gross margin** means that even the users
  who stay are worth almost nothing gross. Switching costs that cannot be converted into
  margin are not an economic moat; they are a user-experience feature.

**API/Open Platform (32.8% of revenue, 69.4% GM).** Switching costs here are near zero by
construction: the endpoints are OpenAI-compatible, MiniMax distributes through OpenRouter
alongside every competitor, and buyers explicitly benchmark price-per-token. This is the
*only* profitable segment and it is the *least* defensible one. That inversion is the
central problem in the MiniMax case.

### 3.2 Network effects (character / UGC library) — **NARROW, UNPROVEN**

- *Supporting:* the character library is user-generated and cumulative; more creators →
  more niches → higher retention per niche. Talkie was top-3 globally in companion-app
  downloads and hit ~11m MAU in 2024, ~17m downloads in 8M2024.
- *Counter:* Character.AI reached 22m MAU (Aug 2024) with a larger, older English-language
  library; ByteDance's Doubao passed **100m DAU** in Dec 2025. Character libraries are
  trivially re-creatable — a prompt is a few hundred tokens, and models now generate
  characters on demand. The library is content, and content without exclusivity is not a
  network. The top five players hold only 46% of the market: a fragmented, low-concentration
  structure is prima facie evidence that no network effect is binding.
- **Verdict:** the mechanism is real but sub-scale and has never survived a stress test.

### 3.3 Cost advantage — **NONE** (this is a claimed moat that inverts on inspection)

MiniMax's own framing (CEO: "intelligence density and token throughput") is a cost-advantage
claim. The price sheet refutes it:

| Model | Input $/1M | Output $/1M |
|---|---|---|
| **MiniMax M3** | **0.30** | **1.20** (0.60/2.40 above 512k ctx) |
| DeepSeek V4-Flash | 0.14 | 0.28 |
| DeepSeek V4-Pro | 0.435 | 0.87 |
| Qwen Flash | 0.05 | n/o |
| Qwen3.7 Max | 1.25 | 3.75 |

MiniMax is **~2.1× DeepSeek V4-Flash on input and ~4.3× on output**, and DeepSeek's
cache-hit pricing ($0.0028/1M) is an order of magnitude below anything MiniMax offers.
There is a genuine *architectural* efficiency story — M2.7 scores 56.22% on SWE-Bench Pro
with only 10B activated parameters, and it is the fastest model in its class — but
efficiency that does not translate into a lower price to the customer is not a cost
advantage; it is a margin the customer will eventually compete away.

Confirming from the other direction: the 4.7% consumer gross margin *is* the inference bill.
If MiniMax had a cost advantage, the consumer segment would be the place it showed up.
It is not there.

### 3.4 Brand — **NARROW, ERODING** (the only source I rate above zero)

- *Supporting (strongest in the whole file):* revenue +158.9% on S&D −40.3%. Talkie briefly
  became the 4th most-downloaded app in the US in H1 2024, outpacing Character.AI at its
  peak, with 3.8m US downloads. That is a real consumer brand built by a Chinese lab in the
  US market — rare and non-trivial.
- *Counter:* the brand did not survive contact with distribution risk (§4.1) or the pricing
  change. **The June 2026 repricing is the definitive pricing-power test and it failed**:
  MiniMax launched M3 with token-based metering on 1 Jun, and by 2 Jun had opened a refund
  portal and granted a permanent 50% weekly-cap boost to Mar 22–Jun 5 subscribers plus
  doubled 5-hour quotas for all. A brand with pricing power does not refund within 24 hours.
- **Width: ~1–2 years on the Talkie name, and shortening.**

### 3.5 Intellectual property — **NONE, AND A NET LIABILITY**

This is the source most often claimed for a "foundation-model company," and for MiniMax it
runs negative on all three legs:

1. **They give theirs away.** M-series models are open-weighted. Whatever capability exists
   is legally and practically copyable. The prospectus itself flags that open-source licence
   terms have not been judicially interpreted and may present later risk.
2. **Some of it may not be theirs.** Anthropic's 23 Feb 2026 disclosure attributes ~24,000
   fraudulent accounts and 16m Claude exchanges across three labs, of which **MiniMax was
   the largest at ~13m exchanges, centred on agentic coding and tool orchestration** — i.e.
   precisely the capability driving the 2026 ARR ramp. If the coding franchise is a
   distillate of a rival's model, the R&D spend is not building a proprietary asset; it is
   renting one, and the landlord has now installed locks.
3. **Others' IP is a live liability.** Disney, Lucasfilm, Warner Bros. and DC sued MiniMax,
   Hailuo AI, SXJT and Nanonoble on 16 Sep 2025 (C.D. Cal.). **On 26 May 2026 Judge Stanley
   Blumenfeld denied MiniMax's motion to dismiss** — the case proceeds on the merits. Hailuo
   is ~33% of revenue. Marketing the service as "a Hollywood studio in your pocket" is not
   a helpful fact for the defence.

### 3.6 Data — **NARROW, UNPROVEN**

- *Supporting:* 212–236m users across 200+ countries generating continuous conversational
  data is the most plausible genuinely accumulating asset MiniMax owns. First-mover in the
  Chinese companion market locked in a daily-data stream.
- *Counter:* companion chat is low-value for frontier capability. The decisive test:
  MiniMax's 2026 capability gains were in **agentic coding**, and per Anthropic those gains
  correlate with 13m Claude exchanges, not with 236m users' companion chats. If the
  proprietary data flywheel were working, they would not have needed the distillation.
  The user data also cannot be exported to the API business, where the margin is.

### 3.7 Regulatory barriers — **NEGATIVE**

Regulation is a headwind here, not a barrier protecting incumbency: Talkie pulled from the
US App Store (17 Dec 2024, "technical reasons," amid China-tech data-security scrutiny);
Xingye subject to domestic content rectification; US/China/EU compute and export constraints
flagged in the prospectus as limits on scaling. A Chinese lab earning >70% of revenue
overseas is *structurally short* regulatory optionality.

---

## 4. Distribution risk — is growth bought or earned?

**4.1 App-store dependence is severe and has already been demonstrated, not hypothesised.**
Talkie was removed from the US iOS App Store on 17 Dec 2024 after 3.8m US downloads and a
top-4 AI-chat ranking. It remained on Google Play; existing iOS users retained access. The
majority of the company's revenue at that time depended on Talkie. This is a single point of
failure controlled by a foreign platform owner in a jurisdiction actively hostile to
Chinese-owned consumer apps — and it fired once already. The Q4-2025 MAU collapse is the
delayed P&L consequence.

**4.2 Was growth bought?** Verdict: **it was bought in 2024, and appears earned in 2025 —
but the 2025 evidence is confounded.** S&D fell from 2.85× revenue to 0.66× revenue. That is
the honest bull case (§2). The confound is that the same period ends with a −60% QoQ MAU
print, which is consistent with "we stopped paying and they left." The FY2026 interim is
the resolving datapoint. Until it prints, I mark this **evidence thin**.

**4.3 The pivot changes the question.** ARR US$150m → >US$300m (Feb → May 2026) is being
driven by Coding Plan / API tokens, not companion apps. That moves the business *out* of the
segment with a plausible moat (consumer brand/switching costs) and *into* the segment with
none (price-shopped API tokens sold through aggregators). Management calls this a platform
pivot. Structurally, it is a migration from a defensible-but-unprofitable business to a
profitable-but-undefensible one.

---

## 5. Competitive set — what stops anyone taking this niche?

**Answer: nothing structural.**

| Competitor | Threat vector | Why MiniMax cannot block it |
|---|---|---|
| **DeepSeek** | Price. V4-Flash at $0.14/$0.28 undercuts M3 by 2–4×; V4-Flash scores 78 vs M2.7's 41 on the cited coding tier | No cost advantage to defend with (§3.3) |
| **Alibaba Qwen** | Price floor ($0.05 input) + cloud distribution + **Alibaba holds 13.66% of MiniMax indirectly** — the largest shareholder is also the largest price competitor | Conflicted cap table; cannot out-spend Alibaba on compute |
| **Moonshot (Kimi)** | Capability. K2.6 at 80.2% SWE-Bench Verified vs M2.7's 56.22% SWE-Bench Pro | Benchmark gap is widening, not closing |
| **Zhipu / GLM** | Enterprise + state channel; GLM-5.2 at 753B params/1M ctx | MiniMax has no B2B relationship depth |
| **ByteDance Doubao** | **Distribution. >100m DAU (Dec 2025).** Owns the recommendation surface (Douyin/TikTok) that Talkie must buy access to | This is the existential one. ByteDance can bundle a companion product at zero CAC |
| **OpenAI / Google** | Own the overseas markets that are >70% of MiniMax revenue, and own the app-store relationship MiniMax lost | Cannot compete on trust/regulatory standing in the US |

The market structure itself is the evidence: top-five share is only 46%, and MiniMax's own
model sits in the middle tier on capability and the middle tier on price. Being neither the
cheapest nor the best in a market with zero switching costs is the textbook definition of no
moat.

---

## 6. Model half-life — is R&D an asset or a treadmill?

**Treadmill. Decisively.**

Observed release cadence: M1 → M2 → M2.1 → M2.5 → M2.7 → **M3 (1 Jun 2026)** — multiple
generations inside ~18 months, against DeepSeek V4, Kimi K2.5/K2.6/K2.7, Qwen 3.6/3.7 and
GLM 5.1/5.2 on the same clock. One commentator's framing is apt: M3's *headline benchmark
was already out of date* at launch.

The accounting test settles it. If R&D were building an accumulating asset, gross profit
would grow faster than R&D and the R&D/gross-profit ratio would compress. Instead:

- R&D **+33.8%** ($189.0m → $252.8m) in 2025
- Gross profit ≈ $20.1m (computed)
- **R&D / gross profit ≈ 12.6×**

And the forward commitment confirms it: of the HK$16bn raised on 10 Jul 2026, **80%
(~HK$12.77bn) goes to AI infrastructure and model R&D**. That is not the capital allocation
of a company harvesting a moat; it is the ante to stay at the table for one more hand. Add
the CB (HK$6.5bn, conv. HK$335) and placement (35.6m shares @ HK$268, ~10% dilution;
up to ~15% fully converted) and the shareholder is funding a treadmill with dilution.

A model whose edge decays in months is an **expense**, not an intangible asset. Twelve years
of Coca-Cola's ad spend compounds into brand. Twelve months of MiniMax's R&D spend compounds
into a superseded checkpoint that is, by their own choice, open-weighted and free.

---

## 7. Rating

> ## Moat: **NONE** — trajectory **ERODING**
> ## Moat score: **18 / 100**
> ## Width in years: **0–1 year** on the model; **1–2 years** on the Talkie consumer brand

**Scoring detail (100 = Coca-Cola/Visa-class):**

| Source | Rating | Score contribution (max) |
|---|---|---|
| Switching costs — consumer | None | 3 / 20 |
| Switching costs — API | None | 0 / 10 |
| Network effects (UGC library) | Narrow, unproven | 4 / 15 |
| Cost advantage | None (inverts) | 0 / 15 |
| Brand | Narrow, eroding | 7 / 15 |
| Intellectual property | None / liability | 0 / 15 |
| Data | Narrow, unproven | 4 / 10 |
| **Total** | | **18 / 100** |

**Firm rule compliance:** *"No moat without ROIC evidence."* MiniMax's ROIC is
structurally negative — adjusted net loss US$250.9m on revenue of US$79.0m, gross profit of
~US$20.1m against R&D of US$252.8m, and cumulative losses reported around RMB 16bn. Under
the firm's own standing rule, **no moat rating above "None" is admissible here regardless of
narrative.** 212–236m users is popularity. Popularity is not a moat.

**Where the evidence is thin (stated plainly):**
- The −60% QoQ MAU figure is secondary-source; I could not obtain primary filings (all
  WebFetch calls returned HTTP 403 this session). Primary hkexnews PDFs: **not obtained.**
- FY2026 interim segment revenue and segment gross margin: **not obtained** (not yet
  reported). This is the datapoint that resolves §4.2.
- Current market capitalisation: **not obtained reliably** — sources irreconcilable.
- Cost per token of MiniMax's own inference (as opposed to list price): **not obtained.**
- Talkie 2026 MAU/DAU from an independent panel (Sensor Tower): **not obtained.**

---

## 8. Threat assessment — top 2 credible threats

**Threat 1 — ByteDance bundling (probability: high; timeframe: now).**
Doubao passed 100m DAU in Dec 2025. ByteDance owns the recommendation surface through which
consumer AI is discovered and can offer companion functionality at zero customer-acquisition
cost, cross-subsidised indefinitely. MiniMax's only defence was S&D spend, which it has just
cut 40%. There is no switching cost to slow the migration and no price umbrella to hide
under, because the consumer segment already earns 4.7% gross margin.

**Threat 2 — commoditisation of the API tier by DeepSeek/Qwen (probability: high; timeframe:
0–12 months).** MiniMax's entire 2026 growth story (ARR $150m → $300m) sits in the API/coding
tier, priced 2–4× above DeepSeek V4-Flash while scoring materially below it and below Kimi
K2.6 on published benchmarks. Alibaba — MiniMax's own 13.66% indirect shareholder — sets the
price floor at $0.05 input. There is no version of this where MiniMax holds 69.4% gross
margins in that segment through 2027.

**Named runners-up (not scored):** (i) an adverse ruling in *Disney v. MiniMax* — motion to
dismiss already denied, 26 May 2026 — impairing Hailuo (~33% of revenue) and, worse,
establishing training-data liability for the whole model estate; (ii) Anthropic and other
frontier labs hardening against distillation, which per §3.5 may remove the actual input to
MiniMax's coding capability; (iii) a second app-store removal event.

---

## 9. Ten-year test

**What must stay true for MiniMax to be a stronger business in 2036?**

1. Frontier model capability must **stop being copyable within months.** If open weights and
   distillation continue to collapse the gap, no lab that is not the cost leader survives on
   models alone. *Current evidence: false.*
2. The platform pivot must generate **switching costs that today do not exist** — agent
   orchestration, memory, workflow lock-in deep enough that swapping the endpoint is
   painful. *Current evidence: absent; distribution is via OpenRouter, which exists
   precisely to make swapping painless.*
3. MiniMax must become the **cost leader**, not the mid-priced option. *Current evidence:
   false — priced above DeepSeek and Qwen.*
4. The consumer franchise must **stabilise** and convert its 4.7% gross margin toward
   something that funds R&D. *Current evidence: MAU falling; margin near zero.*
5. The company must retain **overseas market access** for >70% of revenue through a decade of
   US–China technology decoupling. *Current evidence: already failed once (Dec 2024).*
6. R&D must **stop consuming 12.6× gross profit** without a dilution treadmill. *Current
   evidence: false — HK$16bn raised in July 2026, 80% to R&D and infrastructure.*

**Six conditions; zero currently satisfied.** I can construct a world where MiniMax is a
larger business in ten years — S&P Global models US$5.8bn revenue by 2030 — but I cannot
construct one where it is a *better-defended* business, because every growth path identified
leads into a more commoditised segment than the one it left.

---

## 10. Implication for the margin of safety 𢦀鳩仔 should demand

Handing to Valuation with the following constraints:

1. **No terminal-value moat premium.** Fade operating margins to the industry's marginal
   cost of capital by year 5, not year 10. A "None/eroding" rating means no economic-profit
   annuity may be capitalised into terminal value. If the DCF's terminal value exceeds ~40%
   of enterprise value, the model is assuming a moat that this report finds no evidence for.
2. **Model the API segment at commodity margins.** Do not extrapolate the 69.4% Open Platform
   gross margin. DeepSeek and Qwen price below MiniMax today; assume that margin compresses
   toward 30–40% by 2028. The consumer segment's 4.7% should be held flat or faded, not
   improved, absent evidence.
3. **Fund the treadmill explicitly.** R&D at 12.6× gross profit is not a normalising expense
   — it is the cost of remaining in business. Model R&D as a permanent charge growing with
   compute prices, and model **recurring dilution**: HK$16bn was raised in July 2026 alone
   (~10% immediate, up to ~15% fully converted). Assume further raises.
4. **Discount rate: top of the firm's range**, reflecting (a) unresolved US litigation with
   Disney/WB/DC touching 33% of revenue, (b) demonstrated single-point app-store distribution
   risk, (c) VIE/WVR structure, (d) 48.9% of equity now free-floating post-lockup, (e) an
   unresolved distillation allegation from a frontier lab that could impair the input to the
   growth engine.
5. **Required margin of safety: 60%+ to intrinsic value**, versus the firm's standard
   ~30% for a narrow-moat compounder. Rationale: this is a price-to-sales asset in a sector
   where the multiple has already de-rated ~83% from peak in four months, with negative
   ROIC and no demonstrated pricing power. The equity is an option on the platform pivot,
   and options should be bought at option prices.
6. **Explicit re-rating trigger for the Committee.** Upgrade to **Narrow** if, and only if,
   the FY2026 interim shows *either* (a) consumer segment gross margin above 20% with stable
   MAU, *or* (b) Open Platform gross margin holding above 60% while volume grows >100% —
   i.e. price held under competitive attack. Either would satisfy test W2 or W3 above. I will
   re-run this file on the interim print.

---

### Sources

- [MiniMax FY2025 results (PR Newswire)](https://www.prnewswire.com/news-releases/minimax-announces-full-year-2025-financial-results-302700868.html) · [PR Newswire APAC](https://en.prnasia.com/releases/apac/minimax-announces-full-year-2025-financial-results-523616.shtml) · [company IR](https://www.minimax.io/news/minimax-global-announces-full-year-2025-financial-results)
- [MiniMax 2025 annual report detail (Gate News)](https://www.gate.com/news/detail/19135703) · [BigGo — annual report / CEO on intelligence density](https://finance.biggo.com/news/kMRbs5wBvbjfYyet4tI4)
- [GLOBAL OFFERING prospectus, HKEXnews](https://www1.hkexnews.hk/listedco/listconews/sehk/2025/1231/2025123100025.pdf) *(not obtained — 403)* · [Allotment results](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0111/2026011100015.pdf) *(not obtained — 403)*
- [Futu — prospectus analysis, MiniMax C-end vs Zhipu B-end](https://news.futunn.com/en/post/66478828/in-depth-analysis-of-the-unicorn-ai-large-model-prospectus) · [Futu — FY25 adjusted net loss](https://news.futunn.com/en/post/69458056/overseas-markets-surged-with-minimax-s-revenue-in-2025-increasing)
- [36kr — From $41 Billion to $10 Billion: What Happened to MiniMax?](https://eu.36kr.com/en/p/3883460428034313) · [36kr — 10 Truths from the Zhipu/MiniMax prospectuses](https://eu.36kr.com/en/p/3609403248542466) · [36kr — Why is the market scrambling for MiniMax?](https://eu.36kr.com/en/p/3631961200722951)
- [KuCoin — market cap decline and Q4-2025 MAU](https://www.kucoin.com/news/flash/minimax-s-market-cap-plummets-from-41b-to-10b-hkd-in-six-months) · [KuCoin — A-share filing, ARR >$300m](https://www.kucoin.com/news/flash/minimax-submits-a-share-ipo-filing-arr-surpasses-300m)
- [CNBC — MiniMax doubles in Hong Kong debut](https://www.cnbc.com/2026/01/09/minimax-hong-kong-ipo-ai-tigers-zhipu.html) · [Davis Polk — HK$4.8bn IPO](https://www.davispolk.com/experience/minimax-group-hk-4-8-billion-ipo)
- [Anthropic — Detecting and preventing distillation attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks) · [CNBC — Anthropic accuses DeepSeek, Moonshot, MiniMax](https://www.cnbc.com/2026/02/24/anthropic-openai-china-firms-distillation-deepseek.html) · [Digital Applied — per-lab exchange breakdown](https://www.digitalapplied.com/blog/anthropic-distillation-attacks-deepseek-moonshot-minimax)
- [Loeb & Loeb — Disney Enterprises, Inc. v. MiniMax](https://www.loeb.com/en/insights/publications/2026/06/disney-enterprises-inc-v-minimax) · [Offit Kurman — studios challenge MiniMax over Hailuo](https://www.offitkurman.com/offit-kurman-blogs/ai-copyright-lawsuit-minimax-hailuo-studios) · [AI Law Wiki](https://ailawwiki.com/Disney_Enterprises_v_MiniMax)
- [SCMP — Character.ai rival vanishes from US App Store](https://www.scmp.com/tech/tech-trends/article/3291715/chinese-owned-characterai-rival-vanishes-us-app-store) · [CTOL — Talkie pulled from US App Store](https://www.ctol.digital/news/talkie-ai-chat-app-pulled-us-app-store/) · [SCMP — Talkie scores big in US](https://www.scmp.com/tech/tech-trends/article/3284511/chinese-ai-unicorn-minimax-scores-big-us-talkie-chatbot-entertainment-app)
- [Caixin — AI stocks slide as lock-ups near](https://www.caixinglobal.com/2026-06-12/ai-stocks-zhipu-minimax-slide-as-lock-up-expirations-near-102453785.html) · [Caixin — HK$16bn equity and CB raise](https://www.caixinglobal.com/2026-07-10/chinese-ai-developer-minimax-raises-hk16-billion-from-equity-convertible-bond-sale-102462841.html) · [Maples Group — placement and CB terms](https://www.mondaq.com/pressrelease/203770/maples-group-advises-minimax-group-on-hk$16-billion-share-placement-and-convertible-bond-offering)
- [China Biz Insider — pricing backlash, 4.7% consumer GM, lock-up](https://chinabizinsider.com/minimax-faces-triple-threat-pricing-backlash-benchmark-doubts-and-a-july-unlock/) · [x-cmd — M3 pricing overhaul and refund portal](https://www.x-cmd.com/blog/260602/) · [Bloomberg — JPMorgan cuts target](https://www.bloomberg.com/news/articles/2026-07-13/minimax-shares-slump-after-jpmorgan-cuts-target-further)
- [Nikkei Asia — Zhipu soars, MiniMax stumbles](https://asia.nikkei.com/business/technology/artificial-intelligence/zhipu-soars-and-minimax-stumbles-as-china-s-ai-stocks-diverge) · [Bamboo Works — China's AI valuation reset](https://thebambooworks.com/from-scarcity-to-execution-chinas-ai-valuation-reset/)
- [kr-asia — ARR tops $150m, platform pivot](https://kr-asia.com/minimaxs-arr-tops-usd-150-million-as-it-pivots-toward-an-ai-platform-model) · [kr-asia — Talkie traction and risks](https://kr-asia.com/talkies-global-traction-puts-minimax-in-ais-top-tier-but-risks-loom) · [Pandaily — first post-IPO results](https://pandaily.com/mini-max-s-first-post-ipo-results-beat-expectations-arr-exceeds-150-million-transitioning-to-ai-platform-company)
- [Atlas Cloud — Kimi K2.6 vs GLM 5.1 vs Qwen 3.6 vs MiniMax M2.7](https://www.atlascloud.ai/blog/guides/kimi-k2-6-vs-glm-5-1-vs-qwen-3-6-plus-vs-minimax-m2-7-coding-2026) · [BenchLM — best Chinese models July 2026](https://benchlm.ai/best/chinese-models) · [pricepertoken — MiniMax M3](https://pricepertoken.com/pricing-page/model/minimax-minimax-m3) · [DeepSeek pricing](https://deepseek.ai/pricing) · [OpenRouter — MiniMax M3](https://openrouter.ai/minimax/minimax-m3)
- [S&P Global Market Intelligence — MiniMax revenue forecast](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/minimax-revenue-seen-rising-to-usd219m-in-2026-reaching-usd6b-by-2030) · [Dealroom — 236m users](https://app.dealroom.co/news/feed/minimax-revenue-surges-159-to-79m-with-236m-users-across-200-countries) · [Tiger Brokers — Alibaba 13.66% indirect stake](https://www.itiger.com/news/1126099864)

*Research only. Committee and Owner decide. No investment advice.*
