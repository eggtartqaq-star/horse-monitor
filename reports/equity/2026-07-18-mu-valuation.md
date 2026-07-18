# MU (Micron Technology) — Valuation

**Analyst:** 𢦀鳩仔, Valuation, Dept. 2 (Equity Research) · **Date:** 2026-07-18 · **Reporting to:** CIO
**Inputs:** 巴爺爺 financials (2026-07-18), 菲比斯 moat (2026-07-18, normalization mandate), Elon Musk memory-industry report, Peterson macro regime. Price context: 2026-07-17 traded $806.67–$849.84; 2026-07-16 close $853.20; ATH close $1,213.37 on 2026-06-25. Diluted shares ~1.145–1.15B.

---

## 1. Fair value range & target price

| | Value |
|---|---|
| **Bear fair value (25%)** | **$134/share** |
| **Base fair value (50%)** | **$266/share** |
| **Bull fair value (25%)** | **$620/share** |
| **Probability-weighted fair value** | **~$320/share** |
| **Fair value range (reported, anti-false-precision)** | **$250 – $400** |
| **Target price (12m)** | **$320** |
| **Entry band meeting 菲比斯's 40–50% MoS** | **$160 – $190** (weighted FV); $133–$159 on base FV |

**Headline: at ~$850 the margin of safety is approximately –165%.** The stock trades at ~2.7x my probability-weighted fair value and ~1.4x even my **bull-case** value. This is not a close call, and it is not a statement that Micron is a bad business — it is a statement about what is already in the price (see §7).

Methodological commitment, stated up front per 菲比斯's explicit instruction: **all terminal/normalized economics use mid-cycle gross margins of 35–47% (anchor: FY2025's ~41%) and normalized ROIC of ~10–15% — never FY2026's 84.9–86% shortage margins.** The near-term contracted "harvest" of peak-cycle cash flow (FQ4-26 through FY2027–28) is explicitly modeled and credited in full. Peak margins are harvested, not capitalized.

---

## 2. Assumptions table (nothing buried)

**Common to all scenarios**

| Assumption | Value | Source / rationale |
|---|---|---|
| Valuation date | 2026-07-18 | — |
| Diluted shares | 1.15B, held flat | FQ3-26 ~1,145M (巴爺爺); ~1%/yr SBC creep historically offset by buybacks |
| Tax rate | 15% | Management FY26 guide (FQ3-26 call, via 巴爺爺) |
| Discount rate (WACC ≈ cost of equity; net-cash firm) | **11.0%** | rf 4.55% (10Y, Peterson 2026-07-15) + beta ~1.4 × ERP ~4.75%; sensitivity 9–13% |
| Own net cash credited | **$6B** (not $24.4B) | 巴爺爺's deposit-adjusted figure: $24.4B reported net cash minus ~$18B refundable SCA customer deposits (financing liability, returned in latter half of agreement terms) |
| FCF build | NOPAT + D&A − capex − ΔWC | shown per year in model; script at scratchpad `mu_val.py`, output reproduced in §4 |
| Discount timing | FQ4-26 t=0.11; FY27–31 mid-year t=0.61…4.61; TV t=5.11 | fiscal years end late Aug |
| FQ4-26 FCF | $20–23B | guide $50B rev / ~86% GM / ~$31 EPS; OCF ~90% of NI; capex ~$10B (巴爺爺) |
| Sustaining capex at normalization | ≈ D&A (~$21B base) | memory treadmill: through-cycle capex ≈ depreciation; D&A steps up hard after $27B FY26 + larger FY27 capex |

**Scenario-specific**

| Assumption | Bear (25%) | Base (50%) | Bull (25%) |
|---|---|---|---|
| FY27 revenue / GM | $130B / 60% — pricing rolls over early (falsifier #1 in industry report triggers) | $185B / 72% — pricing peaks mid-FY27 (deliberately ~15–20% below street, which implies ~$210B+ at $112 EPS) | $210B / 76% — 3Q26 +13–18% QoQ momentum extends |
| FY28 revenue / GM | $60B / 22% (FY2024 replay on a bigger base; CXMT floods legacy, AI capex plateaus into fab wave) | $95B / 40% (price −50%+ from peak as P5/Yongin/M15X/ID1 capacity lands 2H27–28; bits still grow) | $150B / 55% (digestion, not bust — SCA floors enforced) |
| FY29 (trough) revenue / GM | $48B / 15% (EBIT negative; cf. FY23 negative GM) | $70B / 32% | $130B / 47% |
| Normalized (FY30–31) revenue | $65B | **$85B** = FY25's $37.4B grown ~15%/yr for 6 yrs (secular bits + structurally higher HBM mix, spot pricing round-trips) | $150B (structurally larger AI-memory industry) |
| Normalized GM | 35% (bottom of 菲比斯 band; SCAs cosmetic) | **41%** (菲比斯's FY2025 anchor) | 46–47% (top of band; cf. FQ4-25 non-GAAP GM 45.7%; SCAs proven through a downturn) |
| Normalized opex | $12.5B | $13.5B | $15B (mgmt guided +$1B R&D in FY27; scaled thereafter) |
| Implied normalized NOPAT / EPS | $8.7B / ~$7.6 | **$18.1B / ~$15.8** | $45.9B / ~$40 |
| Implied normalized ROIC (NOPAT / ~$120–140B invested capital post-buildout) | ~6–7% | **~13–14%** — inside 菲比斯's 10–15% band ✓ | ~20%+ (above band; this is what makes it the bull case) |
| Terminal growth | 3.5% | 4.0% | 5.0% |
| SCA $100B backlog treatment | renegotiated/cancelled in glut | dampens trough (FY29 GM 32% vs FY23's negative) | fully enforced, floors hold |

---

## 3. Scenario narratives & probabilities

- **Base 50% — "great cycle, still a cycle."** The steepest upcycle on record peaks in FY27 (industry framework: profit peak not before Q4-2027, but equities and prices lead), then the announced 2027–28 capacity wave (Samsung P4/P5, SK Hynix M15X + 8–9x 1c ramp + Yongin, Micron ID1/ID2) meets decelerating price momentum (+93–98% → +58–63% → +13–18% QoQ already). Trough is materially better than FY23 thanks to SCAs and HBM contracts (GM 32% vs negative), then mid-cycle normalizes at FY25-like economics on a bigger base. **FV $266.**
- **Bear 25% — "the vicious version."** AI capex plateaus into the fab wave; CXMT reaches DDR5 yield parity late 2026 and re-commoditizes the ~50–60% of bits with no contract protection; HBM4 tri-sourcing (Samsung at price parity) compresses the premium; SCAs prove renegotiable — the "single biggest trust-me item" (巴爺爺) fails. FY28–29 look like FY23–24. **FV $134.**
- **Bull 25% — "regime change, within honest limits."** SCAs hold through the first downturn, the trough never goes below ~47% GM, HBM repricing in 2027 lands multi-fold (TrendForce), and normalized economics settle at the top of the allowed band (~46% GM, ~20% ROIC) on $150B revenue. **FV $620.** Note carefully: **even this scenario is below today's price.** A value above $850 requires normalized GM of ~55–60%+ in perpetuity — outside 菲比斯's band, i.e., it requires rejecting the moat report's central conclusion. I will not build that scenario into a fair value; that is exactly the assumption-tuning my mandate forbids.

**Weighted: 0.25×134 + 0.50×266 + 0.25×620 = ~$321.**

---

## 4. DCF detail (model output, verbatim)

```
BASE (r=11%, g=4.0%):  FQ4-26 FCF $22B
  FY27: rev $185B GM 72% → NOPAT $103.9B, FCF $73.9B
  FY28: rev $95B  GM 40% → NOPAT $22.1B,  FCF $19.1B
  FY29: rev $70B  GM 32% → NOPAT $8.8B,   FCF $14.8B
  FY30: rev $78B  GM 41% → NOPAT $16.1B,  FCF $17.1B
  FY31: rev $85B  GM 41% → NOPAT $18.1B,  FCF $18.1B
  PV explicit $141B + PV(TV) $158B (TV $270B; 53% of EV) = EV $300B
  + own net cash $6B = equity $306B → $266/share

BULL (r=11%, g=5.0%):  explicit PV $236B + PV(TV) $471B = EV $707B → $620/share
BEAR (r=11%, g=3.5%):  explicit PV $77B  + PV(TV) $71B  = EV $148B → $134/share
```

Structural observation: in the base case, **the entire FY26–29 peak-cycle harvest — roughly $130B of FCF, ~$103/share in PV — is credited in full**, and it still covers only ~1/8 of the current ~$977B market cap. The valuation problem is not the next two years; it is the terminal assumption the price forces you to make.

---

## 5. Method cross-check

| Method | Result | Agreement |
|---|---|---|
| **DCF (base)** | $266 | reference |
| **P/E on normalized EPS**: 12–15x mid-cycle multiple × base normalized EPS $15.8 = $189–237 at FY30 → PV $123–154, **plus** harvest FCF PV $103 + cash | **$230–260** | ✓ consistent |
| **EV/EBITDA on normalized EBITDA**: 5–6x (memory mid-cycle norm) × $42B normalized EBITDA = EV $212–254B ($184–221/sh at FY31, ~$120–145 PV) + harvest $103 + cash | **$230–255** | ✓ consistent |
| **Peak-earnings comps** (see below) | MU ~11.8x FY26E / ~7.6x FY27E street EPS vs Samsung 8.1x/5.9x, SK Hynix 9.2x/6.4x fwd P/E ([SK Securities via Asia Business Daily, 2026-06-26](https://www.asiae.co.kr/en/article/2026062610114999109)) | in line with peers **on peak earnings** — see explanation |
| **Street targets**: consensus ~$1,269–1,486; range $385 (Citi) – $2,000 (Cantor) ([MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/MU/forecast/), [stockanalysis.com](https://stockanalysis.com/stocks/mu/forecast/), [Benzinga](https://www.benzinga.com/quote/MU/analyst-ratings)) | 4–5x my weighted FV | ✗ material disagreement — explained |

**Why DCF and street/peak-comps disagree (mandate rule 3 — explain before averaging; I do not average):**
1. Consensus targets are, mechanically, ~12x FY27 street EPS of $112 ([S&P Global, Jun 2026](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/06/micron-a-look-at-memory-ahead-of-earning); up from $90 in March — estimates chasing spot pricing). That **capitalizes a peak year as if permanent** — precisely the practice 菲比斯's report forbids and the industry report calls "the classic memory trap" (trailing multiples on near-peak earnings; low P/E at the top is how memory stocks look cheapest at the most expensive moment).
2. "In line with Samsung/SK Hynix on forward P/E" does not validate the price: the entire complex is priced off the same peak-earnings base. Peers at 6–9x peak EPS are the *comparison*, not the *justification* — in past cycles the Big 3 all de-rated together. If anything, MU carries a ~30% premium to the Koreans on 2027E P/E (7.6x vs 5.9–6.4x) for its US-listing/HBM-share-gain scarcity.
3. The $385–$2,000 target dispersion (5.2x low-to-high) is itself evidence the market is split on exactly this normalization question. My framework sits with the normalization camp by explicit instruction and by the base-rate evidence (42-year median ROIC ~4%; FY23 negative GM three years ago).

Both normalized-multiple methods land within ~5–15% of the DCF. Methods agree once they share the normalization premise; the only disagreement is with methods that don't normalize. No averaging with those.

---

## 6. Sensitivity (base case): normalized GM × discount rate ($/share)

The two most influential assumptions are the normalized gross margin (drives terminal FCF; TV is 53% of base EV) and the discount rate.

| Normalized GM ↓ / WACC → | 9% | 10% | **11%** | 12% | 13% |
|---|---|---|---|---|---|
| 35% | 287 | 253 | 228 | 210 | 195 |
| 38% | 315 | 275 | 247 | 226 | 209 |
| **41% (anchor)** | 343 | 298 | **266** | 242 | 223 |
| 44% | 370 | 320 | 285 | 258 | 237 |
| 47% | 398 | 343 | 303 | 274 | 251 |

Read: across the **entire honest assumption space** — the full 35–47% normalized-GM band crossed with 9–13% discount rates — base-case fair value spans **$195–$398**. No cell reaches even half of today's ~$850. To "fix" that you must change the premise (peak margins persist), not the parameters. Macro note: Peterson's regime read (hawkish-bias Fed, 10Y ~4.55%) argues the discount-rate risk sits on the *right* side of this table, not the left.

---

## 7. Margin of safety at current price — and what $850 is actually paying for

| Price | MoS vs weighted FV $321 | MoS vs base FV $266 | MoS vs bull FV $620 |
|---|---|---|---|
| $806 (7/17 low print) | **–151%** | –203% | –30% |
| **$850 (~current)** | **–165%** | –220% | –37% |
| $1,213 (6/25 ATH) | –278% | –356% | –96% |

- **菲比斯's demanded 40–50% MoS: NOT MET — not remotely.** The required entry band is **$160–190** (weighted FV) or $133–159 (base FV). Current price is ~4.5–5x that band. Even the ~30% fall from the ATH only unwinds part of 2026's re-rating; it does not create value.
- **Reverse DCF:** at $850 (market cap ~$977B), after crediting the full harvest and net cash, the market requires a terminal value of ~$1.44T at FY31 — i.e., **perpetual normalized FCF of ~$97B/yr, or ~$84/share of normalized EPS forever**, versus my base normalized $15.8 and bull $40. That means the price embeds roughly **today's 85%-GM shortage economics as the permanent state of the memory industry**. 菲比斯's report says exactly this case: "If the market price already embeds peak margins persisting past 2027, the margin of safety is negative regardless of the moat improving."
- **Honest flag on the other side (assumption honesty cuts both ways):** my framework is a *valuation* discipline, not a *timing* tool. The industry desk is tactically OVERWEIGHT (pricing still rising into 3Q26; HBM 2027 repricing catalyst; profit peak possibly late 2027), and memory equities can overshoot intrinsic value violently in both directions — the stock tripled past any normalized anchor this year and may again. If Peterson's "risk #1" (supply stays short into 2027–28) plays out, this valuation will look badly early at the peak, exactly as it would have in mid-2017. That is a momentum/tactical argument for the committee to weigh separately; it is not a margin of safety, and I will not relabel it as one.

---

## 8. Valuation input to committee score: **15 / 100**

Rationale: business quality and near-term contracted cash generation are excellent (巴爺爺: 82/100; clean accounting; $100B SCA backlog), but valuation asks one question — price versus value — and the answer is unambiguous: price ~$850 vs weighted fair value ~$320, MoS ~ –165%, and the price exceeds even the bull case built at the top of the sanctioned normalization band. The stock is priced only under an assumption set (permanent 55–60%+ GM) that our own moat work rejects. Score reserves 15 points for the real possibility (embedded in my 25% bull weight) that SCAs/HBM have structurally raised mid-cycle economics more than I credit.

**Actionable for the committee:** as a *valuation* matter MU is a no-buy at $850 and a re-examine at **$250–$400** (fair-value range) with a full-conviction entry only at **$160–190** (菲比斯-compliant MoS). Tripwires that would force me to *raise* normalized assumptions (and the band): SCAs demonstrably enforced through the first real price downturn; 2027 HBM repricing landing multi-fold *and* sticking; MU HBM share holding ≥20% through the HBM4E re-bid.

---

### Sources
- Internal: `reports/equity/2026-07-18-mu-financials.md` (巴爺爺) · `reports/equity/2026-07-18-mu-moat.md` (菲比斯) · `reports/industry/2026-07-18-mu-memory.md` (Elon Musk) · `reports/macro/2026-07-18-mu-regime.md` (Peterson)
- Price/targets: [Yahoo Finance MU](https://finance.yahoo.com/quote/MU/) (7/17 range $806.67–849.84) · [MarketBeat consensus](https://www.marketbeat.com/stocks/NASDAQ/MU/forecast/) · [stockanalysis.com forecast](https://stockanalysis.com/stocks/mu/forecast/) · [Benzinga analyst ratings](https://www.benzinga.com/quote/MU/analyst-ratings) ($2,000 Cantor high, $385 Citi low)
- FY27 street EPS ~$112: [S&P Global Market Intelligence, "Micron: A look at Memory ahead of earnings" (Jun 2026)](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/06/micron-a-look-at-memory-ahead-of-earning)
- Peer multiples: [SK Securities via Asia Business Daily, 2026-06-26](https://www.asiae.co.kr/en/article/2026062610114999109) (Samsung 8.1x/5.9x, SK Hynix 9.2x/6.4x fwd P/E) · [NAI500 on Samsung/SKH vs TSMC P/E](https://nai500.com/blog/2026/04/samsung-and-sk-hynix-see-profits-soar-why-are-their-p-e-ratios-less-than-half-of-tsmcs/)
- Model: `mu_val.py` in session scratchpad; all arithmetic reproduced in §4/§6.

*Research only. Ranges, not points; the point estimates above are midpoints of stated ranges. Committee and Owner decide.*
