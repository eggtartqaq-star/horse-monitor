# 3416.HK — Risk & Suitability Review · Department 6 (Risk Management)

**John, Chief Risk Officer · 2026-08-10**
**Subject:** Global X HSCEI Components Covered Call Active ETF (HKD counter), ISIN HK0000978954
**Question referred by the Owner:** *"When should I sell 3416?"*
**Holder profile as given:** 18 years old, university student, ~40-year horizon,
no stated income need, position ~HK$8,000, plan to add HK$1,000/month.

> **STATUS: IN PROGRESS.** Written incrementally to disk by design — four prior
> reports on this name were lost to session limits. Sections marked *(pending)* are
> not yet written; everything else is final.

---

## 0. Verdict

*(pending)*

## 1. Formal suitability opinion

*(pending)*

## 2. Limit-by-limit check against `config/risk-limits.yaml`

*(pending)*

## 3. The cost arithmetic, completed

*(pending)*

## 4. Board lot and the odd-lot problem — **RESOLVED: 500 units**

### 4.1 The board lot is 500 units

**Board lot = 500 shares/units.** Source: search-engine extraction of the fund's
**Key Facts Statement** (`investments.miraeasset.com.hk/docs/ETF/3416_eKFS.pdf`),
retrieved 2026-08-10, which states *"trade lot size of 500 Shares"* alongside other
KFS fields that independently match our verified facts table (Manager: Mirae Asset
Global Investments (Hong Kong) Limited; base and trading currency HKD; ongoing charges
estimated **0.75%**; distribution **monthly at the Manager's discretion**).

Those three corroborating fields all match figures we already hold from independent
sources, which is why I treat this extraction as **good confidence** rather than
moderate. **The PDF itself was NOT opened** — `investments.miraeasset.com.hk` returned
`EGRESS_BLOCKED` from the egress proxy on direct fetch. Add it to the blocked-host
register. This is a search-engine extraction of a primary document, not the primary
document. *The Owner can confirm it in thirty seconds on any HK broker app; worth doing.*

This **confirms my pre-termination moderate-confidence figure of 500**, and it is
mechanically decisive in two directions.

### 4.2 Consequence 1 — the HK$1,000/month plan is not executable as designed

| Price case | Board lot | Cost of one lot | HK$1,000/month buys |
|---|---|---|---|
| HK$8.64 (last hard NAV, 23 Jul 2026) | 500 | **HK$4,320** | **0 lots** |
| HK$9.665 (disputed vendor price, undated) | 500 | **HK$4,833** | **0 lots** |

**Under either price, HK$1,000 does not buy one board lot.** The student would have to
accumulate **4.3 to 4.8 months** of contributions before a single lot is purchasable.
The plan as stated — "add HK$1,000 per month" — cannot be run monthly in this
instrument. It is structurally a **quarterly-to-five-monthly** plan, or it is an odd-lot
plan (§4.3).

This is not a preference or a market view. It is arithmetic, and it disposes of the
plan *as written* regardless of anyone's opinion on Chinese equities.

### 4.3 Consequence 2 — the odd-lot problem on the existing HK$8,000

The holding is **not a whole number of board lots** under either price:

| Price case | Units held (≈HK$8,000) | Whole board lots | **Odd-lot remainder stranded** |
|---|---|---|---|
| HK$8.64 | ~926 | 1 (500 units) | **~426 units ≈ HK$3,681 — 46% of the position** |
| HK$9.665 | ~828 | 1 (500 units) | **~328 units ≈ HK$3,170 — 40% of the position** |

So roughly **40–46% of the position already sits in an odd lot** in either case.

**Why this costs money in Hong Kong.** HKEX runs odd lots on a **separate odd-lot /
special-lot board**, not the main continuous auto-matching order book. Odd-lot orders do
not match against board-lot liquidity; they match only against other odd-lot interest,
which for a single mid-sized ETF is thin. In practice a retail seller of an odd lot
either (a) waits, possibly days, for a counterparty, or (b) sells to a broker/dealer who
bids *below* the board-lot market to compensate for the inventory risk of assembling a
full lot.

**Quantification — ESTIMATE ONLY, NOT SOURCED.** I tried to source a measured odd-lot
discount for HK ETFs and **could not**. The venues that would carry it (`hkexnews.hk`,
`hsi.com.hk`, and now `investments.miraeasset.com.hk`) are egress-blocked, and I will not
manufacture a number. What I can state with confidence is the **direction and mechanism**:
the odd lot transacts at or below the board-lot bid, never above, and the shortfall is a
real, non-recoverable cost borne entirely by the holder. Logged in the NOT OBTAINED
register as an unquantified cost on 40–46% of the position.

### 4.4 The decisive point: a *partial* sale is the worst available action

Any partial sale creates a *new* odd lot, and a smaller odd lot is harder to sell than a
larger one. The holder today has one clean board lot plus one odd lot. If the decision is
to exit, exiting **in a single order for the full holding** lets the 500-unit lot cross on
the main board and leaves the existing odd-lot problem to be solved once, rather than
manufacturing a second one.

**Binding condition (§7): no partial sale. Exit is all-or-nothing.**

## 5. Concentration and correlation assessment

*(pending)*

## 6. The price conflict — HK$8.64 vs HK$9.63

*(pending)*

## 7. Sell triggers to pre-commit to

*(pending)*

## 8. The gating question — is HK$8,000 most of the savings?

*(pending)*

## 9. Ranking the decisions by materiality

*(pending)*

## 10. Risk score (0–100) — input to committee

*(pending)*

## 11. Escalations to the Owner

*(pending)*

## 12. NOT OBTAINED register

*(pending)*

---

Research and decision support. **Not financial advice.** Markets cannot be reliably
predicted. No agent of this firm places orders; the Owner executes.
