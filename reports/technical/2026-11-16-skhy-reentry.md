# SKHY — re-entry analysis after a full exit at $137

> **CORRECTED 2026-11-16 after audit** (`reports/committee/2026-11-16-aapl-skhy-reentry-audit.md` §3).
> S1: the probability model's drift assumption was undisclosed and made low prices look more remote
> than a zero-expected-return model does; both are now shown. S2: an unsupported "never own it
> again" claim is withdrawn. S3: the ADR quota's *current* status was stated as fact; it is not
> known. S4: the ₩850,000 trigger is now derived. S5–S9 reworded. **All of these leaned against
> re-entry — the second SKHY document from the CEO with one-directional hardening.** The verdict
> at today's price is unchanged; the conditional plan's triggers are *more* reachable than first shown.

**皮褸黃 (CEO) · 2026-11-16 · primary bars to the 13 Nov close · audited valuation of 12–13 Nov**

## 0. Where the Owner stands

| | |
|---|---|
| Exit | **$137.00, entire position.** Date NOT DISCLOSED (consistent with 12 Nov) |
| Result | **+$8.00/ADS, +6.20%** on the $129 cost, before costs |
| Versus the firm's hold plan | No firm trigger had fired. Marked at the 13 Nov close of $131.79, the exit **beat holding by $5.21/ADS (+3.95%)** |
| Position now | **Zero.** Tickets T0–T9 are VOID — each was a sell, so placing one now would open a short |
| Last price | $131.79 close 13 Nov; $130.21 after hours |

**A re-entry is a new initiation, not a resumption.** It faces every gate a first purchase faces.

## 1. Verdict

**No re-entry at today's price.** Re-entry is a **conditional plan**: specific levels and events,
written down now, so the decision is not made in the moment.

## 2. The anchoring check — read first

SKHY is now **$5.21 below where you sold**. That makes buying back feel like getting a discount,
but the comparison is meaningless: the market doesn't know your exit price. The only comparisons
that matter are **price against value** ($131.79 is **28.7% above** the $102.40 fair value) and
**price against risk**.

Selling at $137 and buying back at $131 isn't a 3.8% gain. It's a fresh purchase at a price the
firm values below the market.

## 3. The gates a re-entry must clear (firm rules)

| Gate | Requirement | Status today |
|---|---|---|
| Valuation | Price ≤ fair value at minimum; the desk requires a 40% margin of safety | **FAIL** — 28.7% above fair value |
| CRO | Risk score ≥ ~40 for any initiation | **FAIL** — 32/100 (12 Nov) |
| Committee | `committee_approval_required: true` | **Not convened** |
| Instrument | Premium risk sized and accepted | 43–52% premium; current level NOT OBTAINED (no 13 Nov Korean close) |

*The valuation gate's 40% margin of safety is a desk requirement; the CRO and committee gates are firm rules.*

All four must clear. Today none does.

## 4. The instrument question — the most useful re-entry finding

**The risk in the ADS that no stop can protect against is the 43–52% premium.** (It is not the
largest risk: a cycle halving of the ordinary is −49% to −51% at parity, per the 13 Nov audit.)
The premium exists because a Korea Securities Depository quota on ADR issuance was **reported
exhausted as of 23 Jul 2026; its current status is NOT OBTAINED.** John capped the old position at
3% precisely because no stop protects against that premium vanishing.

**Buying the Korean ordinary share (000660.KS) instead removes that risk entirely.** You'd own the
same business at the price the company itself buys back at.

| | ADS (SKHY) | Ordinary (000660.KS) |
|---|---|---|
| Fair value central | $102 (blended), $80 at parity | **₩1,070,000** |
| Premium risk | $300–340 per $1,000 | **none** |
| Price vs fair value | +28.7% | last available ₩1.21–1.30m (10–11 Nov): **+13% to +21%** |
| 40% MoS entry | $61.44 | **₩642,000** |
| Minimum ticket | 1 ADS ≈ $132 | 1 share ≈ ₩1.2–1.3m ≈ US$900–970 |
| Dividend withholding | 22% default / 15% treaty, via the depositary | same Korean rates, paid direct |

The Webull account shows **₩888,241 of KRW buying power**, but that is margin capacity in a
multi-currency account, **not evidence of Korea Exchange access**. Whether any of your brokers can
trade KRX is NOT OBTAINED. **Check that before anything else** — it decides which instrument a
re-entry should use.

Even on the ordinary, price was above fair value at the last Korean print (10–11 Nov). The ordinary removes the premium risk; it
does not make the stock cheap.

## 5. Re-entry triggers — value, plus at least one confirmation

**Value (required):**
- **ADS ≤ $102.40** (or ordinary ≤ ₩1,070,000) — expected value stops being negative. **This
  convenes a committee; it is not a buy signal.**
- **ADS ≤ $61.44** (or ordinary ≤ ₩642,000) — the valuation desk's entry, with its 40% margin of safety.

**Plus at least one confirmation:**

| Family | Confirmation | Source |
|---|---|---|
| **Premium** | ADS premium below ~20% on a dated Korean close and FX, **or** re-entry via the ordinary | regulatory / news desks |
| **Cycle** (any two of Elon Musk's falsifier list, memory-cycle report §11.3) | TrendForce 1Q27 conventional DRAM contract ≥ +15% QoQ with consumer re-accelerating; LTAs shown to carry price floors; Jan–Feb 2027 hyperscaler capex guidance ≥ +40%; Q4 DRAM bits ≥ +10% YoY; SK hynix HBM4 share ≥ 60% confirmed | industry desk |
| **Trend repair** | a higher low holds above $122.20, **then** a daily close above **$145.79** (the 11 Nov lower high); a close above $162 confirms reversal | primary bars |

**What does NOT qualify:** price below your $137 exit; a single gap-up day like 11 Nov (+9.7%,
rejected at $145.79); analyst targets (consensus mean $259.50 has not absorbed the firm's
premium analysis).

## 6. Statistics — how often does SKHY reach these levels?

Probability of the ADS **touching** a level at least once, from $131.79, under a random walk at
constant realised volatility. **This is a model, not a forecast.** It ignores mean reversion and
regime change, and volatility itself may fall.

**Two versions, because at ~100% volatility the drift assumption matters:**
- **Zero drift in log price** (the version first published). At 101% volatility this quietly
  implies an expected *price* gain of about **+29% over six months** — it makes low prices look
  more remote than they are.
- **Zero expected price change** (a fair-game price; log drift −σ²/2). The more neutral choice.

Realised volatility: **101%** over the last 20 sessions; 76% over 60; 99% over its life.

| From $131.79 | $122.20 (ATL) | **$102.40 (fair value)** | $80 (parity) | **$61.44 (40% MoS)** |
|---|---|---|---|---|
| 1 month — log-driftless | 73–80% | 25–39% | 2–9% | 0–1% |
| 1 month — zero expected change | 76–82% | 28–44% | 3–11% | 0–1% |
| 3 months — log-driftless | 84–88% | 51–62% | 19–32% | 4–13% |
| **3 months — zero expected change** | 87–91% | **57–69%** | 24–41% | **6–19%** |
| 6 months — log-driftless | 89–92% | 64–72% | 35–48% | 15–29% |
| **6 months — zero expected change** | 92–95% | **72–81%** | 44–61% | **22–40%** |

Ranges span the 60-day, 20-day and life volatilities (1 month: 60-day and 20-day).

**What follows.** Waiting for fair value isn't waiting for a fantasy: at this volatility, $102 is
more likely than not within a quarter on either model. The $61 margin-of-safety level is the long
shot — **roughly 15–40% within six months** depending on the model — and on a longer horizon the
model's touch probability keeps rising. *(The first version said "you will most likely never own
SKHY again". That was a claim about an unbounded horizon drawn from a six-month model, and is
withdrawn.)*

## 7. The re-entry plan, if the gates clear

| Stage | Trigger | Size (fraction of the maximum John approves) | Note |
|---|---|---|---|
| **R0** | Confirm KRX access; disclose liquid net worth | — | Decides the instrument and the cap |
| **R1** | ≤ $102.40 / ₩1,070,000 **and** one confirmation | **⅓** | Convene committee first; John re-runs the risk score |
| **R2** | ≤ $80 / ≤ ₩856,000 **and** the confirmation still holding | **⅓** | Re-check the premium. At $80 the move may be the premium collapsing, not the business falling — **they mean different things** |
| **R3** | ≤ $61.44 / ₩642,000 | **⅓** | Full margin of safety |

**Deriving the KRW triggers.** For the ordinary, each stage is set on the ordinary's own fair value
(₩1,070,000), not translated from the ADS: R1 = fair value; **R2 = 20% margin of safety =
₩856,000** (1,070,000 × 0.8; the first version said "≈₩850,000" with no derivation); R3 = 40% =
₩642,000. The ADS and KRW columns are therefore *not* the same price in two currencies: ADS $80 is
parity fair value, which in the ordinary is ₩1,070,000 — R1, not R2.

**The cap:** John's 3% of liquid net worth came from the ADS premium, not the price. It applies to
an ADS re-entry at any price until he re-rules. On the ordinary, the premium component falls away;
the cap would then be set by the stop and the cycle, and **John must rule on it**. Zac's stop-only
ceiling was 7.5–10%.

**The stop:** set by 老詹 from the structure at the time of entry. A re-entry at $102 means the
$122.20 low has already broken, so today's structure won't exist. Placeholder until he does: a
daily close below the base's low, executed at next open — never a resting stop on an instrument
with a 7.7% daily range.

**Timing:** avoid re-entering in the week before **4Q26 results (late January)** unless already in
the value zone. A memory stock reporting near a cycle peak can gap 10–15% either way.

## 8. Calendar

| Date | Event | Why it matters for re-entry |
|---|---|---|
| By ~24 Dec 2026 (per the 13 Nov tickets) | Watch for the 2027 US tool licence for the Wuxi fab | Absence is a negative catalyst; a grant removes one bear point |
| 31 Dec 2026 | Wuxi licence expiry (derived, not stated in any source) | ~⅓ of DRAM wafer output |
| Late Jan 2027 | 4Q26 results | First quarter that may show the cycle turn |
| 28 Jan 2027 | ₩20tn buyback ends | Support for the ordinary is gone |
| Jan–Feb 2027 | Hyperscaler 2027 capex guidance | Cycle confirmation, either way |

## 9. Do-not list

- Don't buy because the price is under your $137 exit.
- Don't use margin. The Webull account is a margin account carrying negative cash.
- Don't buy the ADS without a dated premium reading.
- Don't place any of the void T0–T9 tickets.

## NOT OBTAINED

1. Sale date (12 Nov consistent with the price; unconfirmed).
2. ADS premium at the 13 Nov close — no dated Korean close or FX on disk.
3. Whether any of the Owner's brokers offers Korea Exchange access.
4. Liquid net worth — needed for any cap.
5. A CRO ruling specific to re-entry and to the ordinary. **Requested in wave two.**

*Research and decision support, not financial advice. No agent of this firm places orders.*

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
