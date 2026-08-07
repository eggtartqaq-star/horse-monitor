# MRVL (Marvell Technology) — Valuation

**Analyst:** 𢦀鳩仔, Valuation (Dept. 2 — Equity Research) · **Date:** 2026-07-19
**Verified price:** $188.68 (Fri 2026-07-17 close) · **Shares:** ~883M diluted (creeping)
**Inputs on disk:** `2026-07-19-mrvl-financials.md` (巴爺爺), `2026-07-19-mrvl-management.md` (Peter),
`2026-07-19-mrvl-custom-silicon.md` (Elon Musk), `2026-07-19-mrvl-regime.md` (Peterson).
**Moat input:** 菲比斯's standalone file was NOT on disk (`2026-07-19-mrvl-moat.md` not found — a
visibility limit); his valuation instructions were carried in the task brief and are honored below.

---

## Headline

| Item | Value |
|---|---|
| **Fair-value range (firm-consistent terms)** | **$55 – $105 / share** |
| **Central estimate / target** | **~$70** |
| **Current price** | $188.68 |
| **Margin of safety at $188.68 (vs $70 central)** | **≈ −170%** (price is ~2.7x fair value) |
| **菲比斯's demanded 35–40% MoS** | **NOT met — not remotely** (would need ~$45 vs central; ~$67 even vs the bull case) |
| **Valuation score → committee** | **25 / 100** |

**One line:** After a −43% crash, MRVL is *still* priced for an AVGO-class outcome — the bull revenue
path, ~40% operating margins, a ~9% discount rate, and 5% terminal growth *all at once*. On the firm's
own accounting (SBC as a real cost) and 菲比斯's narrow-moat / socket-churn terms, fair value is roughly
$55–105. There is no margin of safety at $188.68; there is a large negative one.

> **Method note — DCF and multiples do NOT disagree with each other.** Both land at ~$55–105. They
> disagree only with the *market price*. Per mandate I explain that gap rather than average it away (see
> "Method cross-check" and "Reverse-DCF").

---

## Assumptions table (the audit trail)

Shared across scenarios unless overridden:

| Assumption | Value | Basis |
|---|---|---|
| Valuation date | mid-2026 (Jul) | discount FY27 at 0.5y, FY28 at 1.5y … FY36 at 9.5y |
| Diluted shares (now) | 883M | 巴爺爺; Celestial paid largely in stock |
| Net dilution | +1.25%/yr | SBC issuance > $200M/qtr buyback (巴爺爺 red flag #5) |
| Net debt | $1.12B | debt $4.96B − cash $3.84B (10-Q May 2, 2026) |
| Celestial earnout | −$0.9B to equity | contingent-consideration liability = a real claim |
| Cash tax rate | 15% | non-GAAP tax run-rate |
| Net interest | −$100M/yr | int. exp. $187M less interest income on cash |
| **SBC** | **charged as a real cost** | non-GAAP op margin 35% − SBC ~7–8% rev = **~27% "true" op margin today**. Fades toward ~4–5% of rev at scale (AVGO-like), partly offsetting mix compression |
| Custom-ASIC gross margin | low-40s%, permanent | 菲比斯 haircut; hyperscalers hold pricing power (Elon §3) |
| Terminal value | mostly the optics/interconnect franchise, post-2031 CPO fade | 菲比斯 |

Scenario-specific drivers:

| Driver | Bear | Base | Bull |
|---|---|---|---|
| **FY27 revenue** | $10.5B (+28%) | $11.0B (+34%) | **$11.5B (+40%, mgmt guide)** |
| **FY28 revenue** | $11.5B (+10%) | $13.8B (+25%) | **$16.5B (+43%, mgmt guide)** |
| FY29–FY36 growth | +9%→+2.5% | +16%→+4% | +24%→+5% |
| FY36 revenue | $16.6B | $26.5B | $37.8B |
| Op margin (SBC-adj) path | 24%→25% | 27%→30% | 28%→35% |
| WACC | 12.0% | 11.0% | 10.5% |
| Terminal growth | 2.5% | 3.5% | 4.0% |
| FCF conversion of NOPAT | 72%→86% | 75%→88% | 75%→90% |

*Socket-churn logic (base/bear):* each flagship XPU has ≤50–60% renewal probability per generation
(菲比斯). MRVL already lost the Trainium 3 and Maia 200 *compute dies* to Alchip/GUC (Elon §4). Base
haircuts FY28 to $13.8B (vs $16.5B guide); bear assumes a third compute-die loss caps FY28 at $11.5B.
Bull takes management's guide at face value — Peter documents that Murphy's team has *beaten its own
guidance every quarter* and beat the AI-revenue targets decisively, which earns the bull its 25% weight.

*WACC build (base 11%):* rf 4.55% (10Y) + β~1.5 × ERP 5% = cost of equity ~12%; after-tax cost of debt
~4.5%; ~97% equity-weighted → ~11.7%, rounded to 11.0% base. 菲比斯 argues for conservatism because
goodwill-inclusive ROIC is only ~6–8% (below WACC) — the company has *never* earned its cost of capital.

---

## DCF results

| Scenario | Fair value / sh | EV | TV % of EV | Upside vs $188.68 |
|---|---|---|---|---|
| **Bear** | **$24** | $25B | 45% | −87% |
| **Base** | **$55** | $54B | 57% | −71% |
| **Bull** (mgmt guide) | **$103** | $99B | 63% | −45% |

**Probability weighting — bear 30% / base 45% / bull 25%:**

Prob-weighted DCF value ≈ **$58 / share**.

> Even the *bull* case — which grants management's full $11.5B/$16.5B guide, 35% terminal margins, a
> 10.5% WACC and 4% terminal growth — is worth **$103, i.e., 45% below the current price.** That is the
> single most important sentence in this report.

---

## Method cross-check

**1. Multiples on SBC-adjusted EPS** (the honest earnings anchor; the market pays on non-GAAP):

| Basis (base path) | Value | Implied P/E at $188.68 |
|---|---|---|
| FY27 SBC-adj EPS | $2.73 | 69x |
| FY28 SBC-adj EPS | $3.47 | 54x |
| FY29 SBC-adj EPS | $4.06 | 46x |
| FY27 *non-GAAP* EPS (add back SBC) | ~$3.46 | 55x |
| FY28 *non-GAAP* EPS | ~$4.38 | 43x |

A narrow-moat, sub-WACC-ROIC, 82%-concentration name decelerating to mid-teens growth post-FY28 warrants
a *discount* to Broadcom's ~20–24x forward P/E (AVGO has the wider moat and ~70% custom share). Applying
**18–28x to FY29 SBC-adj EPS ($4.06), discounted 2y @ 11% → $59–92/share.** Midpoint ~$75.

**2. EV/EBITDA.** Current EV/forward-SBC-adj-EBITDA ≈ **38x (FY28), 32x (FY29)** — versus AVGO ~44x
*trailing* (itself rich) and MRVL's own 5-yr history in the mid-teens-to-low-20s. Rich on every internal
and external anchor.

**Conclusion:** DCF ($55–103) and multiples ($59–92) **converge on ~$55–105.** The methods agree. The
gap is entirely versus the *market*, driven by (a) SBC treated as real (−~7 margin pts, −~$0.75–1.00 EPS),
(b) an 11% narrow-moat WACC vs the market's implied ~9%, (c) the socket-churn revenue haircut, and (d)
refusal to extrapolate AVGO-class terminal margins onto a business that has never earned its cost of capital.

**3. Reverse-DCF — what $188.68 actually prices in:**

| Revenue path | Op margin | WACC | Term. growth | Implied FV |
|---|---|---|---|---|
| Base | 45% (flat!) | 11% | 4% | $89 |
| **Bull** | 35% | 9.5% | 4.5% | $136 |
| **Bull** | 40% | 9.0% | 5.0% | **$190 ≈ current** |
| Bull | 45% | 9.0% | 5.0% | $214 |

To justify $188.68 you must simultaneously believe: the **full bull revenue path** ($37.8B by FY36),
**~40% operating margins** (AVGO-class, well above MRVL's SBC-adjusted ~27% today), a **9% discount rate**
(a wide-moat rate), *and* **5% perpetual growth.** That is precisely the "Broadcom-class multiple for
sub-WACC returns" 菲比斯 instructed us not to pay. A mainstream sell-side desk that (i) excludes SBC, (ii)
uses a 9–10% WACC and (iii) trusts the guide gets to $150–250 (KeyBanc PT $400 on the Merope lifecycle) —
that bracket is real, but it is the market's assumptions, not ours.

---

## Sensitivity tables (base revenue path)

**Grid A — normalized (flat) operating margin × WACC** (terminal growth 3.5%):

| op margin \ WACC | 9.5% | 10.5% | 11.5% | 12.5% |
|---|---|---|---|---|
| 22% | $53 | $45 | $39 | $34 |
| 25% | $61 | $51 | $44 | $39 |
| 28% | $68 | $58 | $50 | $44 |
| 31% | $76 | $64 | $56 | $49 |
| 34% | $83 | $71 | $61 | $54 |

**Grid B — normalized op margin × FY28+ revenue trajectory** (WACC 11%, tg 3.5%; columns scale the
whole post-FY27 growth path):

| op margin \ rev path | −30% | −15% | base | +15% | +30% |
|---|---|---|---|---|---|
| 22% | $31 | $36 | $42 | $48 | $56 |
| 25% | $35 | $41 | $48 | $55 | $63 |
| 28% | $40 | $46 | $54 | $62 | $71 |
| 31% | $44 | $51 | $60 | $69 | $79 |
| 34% | $49 | $57 | $65 | $76 | $87 |

**Read:** the *entire* plausible grid — margins 22–34%, WACC 9.5–12.5%, revenue ±30% — tops out at **$87**.
$188.68 is off the top-right corner of both grids. The current price is not inside any conservative
sensitivity cell; it lives only in the reverse-DCF's bull-on-bull corner.

---

## Margin of safety at $188.68

| Reference fair value | MoS = (FV − price)/FV | "Buy" price for 35% MoS |
|---|---|---|
| Central $70 | **−170%** | $45.50 |
| Base $55 | −243% | $35.75 |
| Bull $103 | −83% | $66.95 |
| Prob-weighted $58 | −225% | $37.70 |

菲比斯 demanded a **35–40% margin of safety** for a narrow, partly-eroding moat. It is **not met on any
scenario.** Even measuring against the *bull* case, the firm should not pay above ~$67. Against the base
case, ~$36. The stock would need to fall a further **~45–65%** from $188.68 before it enters the desk's
buy zone on 菲比斯's terms.

---

## Valuation input to committee score: **25 / 100**

- Deep negative margin of safety (−170% vs central FV; price ~2.7x fair value) — the dominant factor.
- Priced for AVGO-class economics MRVL has never earned (ROIC ~6–8% < WACC); reverse-DCF requires
  bull-revenue + 40% margins + 9% WACC + 5% terminal growth together.
- Points *not* zero because: (a) genuine AI inflation and a rebuilt win slate (Merope LPU up to $12B
  lifecycle, Trainium 4 NPO, Maia 300 — Elon §4) give real bull optionality; (b) management's delivery
  record is strong (Peter, B+; beats own guide every quarter); (c) balance sheet is sound (net debt
  ~$1.1B). These support the *business*, not the *price*.
- **This is a valuation verdict, not a trade.** The desk would turn constructive around **$60–70**
  (35% MoS to the bull case / near base-case fair value) and outright attractive **sub-$55**.

**Honesty note:** a Street/non-GAAP framework yields $150–250+. Our far-lower number is the deliberate
product of the firm's philosophy (巴爺爺: use FCF + SBC-adjusted earnings; 菲比斯: narrow-moat, socket-churn,
no Broadcom multiple for sub-WACC returns). No assumption here was reverse-engineered to a target; the
assumptions table is the audit trail, and every conservative lever is 菲比斯's explicit instruction.

**Visibility limits:** egress proxy blocks direct pulls from most finance sites; AVGO/Alchip comps are
indicative (AVGO fwd P/E ~20–24x, trailing EV/EBITDA ~44x; Alchip mkt cap NT$300B+, +~30% YTD). MRVL
consensus non-GAAP FY27 EPS is scattered across vendors ($2.78 Zacks to ~$4+ implied). Arithmetic in
`scratchpad/mrvl_dcf2.py`, `mrvl_x.py`, `mrvl_sens.py`.

## Sources
- Broadcom valuation (indicative): [gurufocus fwd P/E](https://www.gurufocus.com/term/forward-pe-ratio/AVGO) · [valueinvesting.io EV/EBITDA](https://valueinvesting.io/AVGO/valuation/ev_ebitda-multiples) · [stockanalysis AVGO](https://stockanalysis.com/stocks/avgo/statistics/)
- Alchip / Taiwan ASIC houses: [Digitimes tracker](https://www.digitimes.com/news/a20260512VL219/taiwan-monthly-tracker-alchip-faraday-guc-asic-design-revenue-2026.html)
- MRVL consensus EPS (indicative): [ChartMill](https://www.chartmill.com/stock/quote/MRVL/analyst-ratings) · [public.com forecast](https://public.com/stocks/mrvl/forecast-price-target)
- Fundamentals/price/guidance: on-disk reports (巴爺爺, Peter, Elon, Peterson), all primary-sourced therein.

---
*Research and decision support only — not financial advice. Committee and Owner decide.*

---

<!-- provenance-stamp -->
## Provenance and coverage

*Appended by `scripts/stamp_provenance.py`. Records how this report was
produced, so its weight can be judged later without reconstructing the
conditions from memory.*

**Sourcing.** This report predates 2026-07-30, when the environment's
HTTP 403 egress restriction was first observed and verified. Whether
direct page fetch was available when this was written **was not recorded
at the time**, so no claim is made either way — rely on the sourcing
stated in the body of the report itself.

**Coverage gap — no quantitative input.** Department 3 (Quant Research:
賭馬狗, Math King, Tom, AI指標) filed **nothing** on this name. Session
limits forced the pipeline down to a three-agent core and quant was cut
first, without being logged as a gap at the time. Any conclusion here
rests on fundamentals, valuation, news and technicals only.

**Standing rules.** No figure in this report may be invented; every number
should carry a source and a date, and estimates should be marked as
estimates (CLAUDE.md rule 5). Research and decision support only — not
financial advice, and no agent of this firm places orders.
