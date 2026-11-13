# SKHY — Position Sizing Memo

**Analyst:** Zac, Position Sizing (Dept 7) · **To:** Morris (PM); copies John (CRO), 死潘狗 (Execution)
**Date:** 2026-11-13 · **Instrument:** SK hynix ADS (Nasdaq: SKHY), 1 ADS = 0.1 ordinary (000660.KS)
**Owner's position:** cost **US$129.00/ADS**; **ADS count and liquid net worth (LNW) NOT DISCLOSED**. Not held at Webull (§1.6); presumed at Futu — NOT CONFIRMED.
**Current price:** **US$131.07** (live read-only Webull pull, 19:50 UTC 13 Nov 2026, via coordinator; −4.82% on the day; 12 Nov close $137.71; day range $129.18–$135.76). Owner is **+$2.07/ADS = +1.6%**.
**Inputs (all on disk or coordinator-supplied; no web searches this session):**
`reports/risk/2026-11-12-skhy-cro-review.md` (John — binding) · `reports/equity/2026-11-12-skhy-valuation.md` (𢦀鳩仔) ·
`reports/technical/2026-11-11-skhy-technical.md` §9 (老詹) · `reports/committee/2026-11-12-skhy-ceo-synthesis.md` (CEO) · `config/risk-limits.yaml` · Webull read-only pull (coordinator message, 13 Nov).
**Status:** COMPLETE. All sections filled 2026-11-13; no `[PENDING]` markers remain.

> Research and decision support, not financial advice. I size; 死潘狗 tickets; the Owner places. No agent of this firm places orders.

---

## 0. Summary

| Item | Figure | Source |
|---|---|---|
| **Hard cap (John, binding)** | **3.0% of LNW at market** | CRO §9, Condition 1 |
| **Conviction-scaled recommended size (mine, inside John's cap)** | **≤ 1.5% of LNW now** — the 20 Jan 2027 level, reached now rather than later (§6) | my method step 3 applied to desk scores 25 / 32 / 35 |
| **If the Webull account (~US$690) is the whole LNW** | **3% cap = $20.70 < one ADS ($131.07). Any SKHY holding at all is over the cap → John's "hold at ≤3%" converts to "reduce to zero."** The Owner must disclose the denominator before this reading can be dismissed (§5.3) | Webull pull; arithmetic §5.3 |
| New position at $131 | **Pass — zero.** MoS fails on every central construction (§6) | 𢦀鳩仔 §8.4 |
| Add | **Vetoed.** No add-tranche schedule exists | CRO §0 B/C, Condition 5 |
| Stop | daily close **< $120.35** → sell 100% at next open. **Not** a resting intraday order | 老詹 §9(c); CRO §4 |
| Risk at the stop | from cost: **$8.65/ADS = 6.71% = $67 per $1,000**; from market $131.07: **$10.72 = 8.18% = $82 per $1,000**. At 3.0% size: **0.20–0.25% of LNW** (a fifth to a quarter of the 1% budget) | arithmetic §4 |
| Which constraint binds | **The premium (no stop) → 3.0%.** The stop alone would allow 7.5% (gap-sized) / 10% (position cap). The stop is not the binding constraint | CRO §9; §4 below |
| Mandatory trims | ≥ ⅓ at any print **$146.8–149.9**; another ⅓ at **$158.5–162.0** | 老詹 §9(b); CRO Condition 8 |
| Reduce-before | ≤ **1.5%** of LNW by **20 Jan 2027** (≤ 3.0% if 老詹 logs a daily close > $152.35) | CRO Condition 7 |
| Wuxi tripwire | no 2027 US tool licence reported by **24 Dec 2026** → halve at next open | CRO Condition 6 |
| Premium monitor | premium < 25% with Seoul flat/up → sell half; any KSD/FSC/depositary quota widening → sell all | CRO Condition 4 |
| **Margin flag** | the one account we can see is a **margin account carrying negative USD cash (−$12.06)**. John's Condition 3 (unmargined) is **unverified for the SKHY account and breached in form at Webull**. No ticket may be placed on margin (§7) | Webull pull |

**Everything below is in scalable form (per $1,000 of position, per 100 ADS, per 1% of LNW) because the two numbers that would make it concrete are not disclosed.** The Owner needs to supply *either* the ADS count and LNW, *or* the position as a percentage, and §2 converts in one line.

---

## 1. Inputs

### 1.1 Prices used

| Reference | Price | Source / status |
|---|---|---|
| Owner's cost | **$129.00** | brief; CRO header |
| **Current (used everywhere as "market")** | **$131.07** | Webull read-only pull 19:50 UTC 13 Nov (coordinator) |
| 12 Nov close | $137.71 | same pull |
| 13 Nov day range | $129.18–$135.76 | same pull; **the day's low ($129.18) was 7 cents above cost and inside 老詹's launch zone** |
| 10 Nov derived close | ~$129.66 | 老詹 §2 — **superseded** by the live print; shown for reconciliation with John's §9 translation only |
| 11 Nov intraday | $142.68–$143.42 | 老詹 §11 (close NOT OBTAINED) |

Stop-distance arithmetic is run from **both** cost ($129.00, the brief's instruction) and market ($131.07, where the position actually is). The cap is measured **at market**, so every "% of LNW" figure uses $131.07.

### 1.2 Levels (老詹 §9, logged 11 Nov, "will not be moved lower")

| Level | Price | Distance from $131.07 | Role |
|---|---|---|---|
| Early warning | intraday < $122.20 | −6.8% | watch only — not a trigger |
| **Hard stop** | **daily close < $120.35** | **−8.2%** | sell 100% next open |
| Add zone | $127.3–$130.0 | −2.9% to −0.8% | **vetoed by CRO — not used.** The 13 Nov low $129.18 was inside it |
| Do-not-chase | > ~$140 | +6.8% | no buy tickets at any price regardless |
| **Reduce 1** | **$146.8–$149.9** | **+12.0% to +14.4%** | trim ≥ ⅓ |
| Range-read confirmation | daily close > $152.35 | +16.2% | relaxes the 20 Jan target from 1.5% to 3.0% |
| **Reduce 2** | **$158.5–$162.0** | **+20.9% to +23.6%** | trim another ⅓ |
| Trend reversal | daily close > $162.0 *and* higher low > $129.66 | — | informational |

### 1.3 Budget and caps (`config/risk-limits.yaml`, read 13 Nov)

| Parameter | Value | Use here |
|---|---|---|
| `per_trade.max_risk_per_trade` | **0.01** of portfolio | the risk budget; John measures it on LNW |
| `concentration.max_single_position` | 0.10 at cost | ceiling on the stop-only construction |
| `concentration.max_single_position_drifted` | 0.15 | not binding at +1.6% |
| `per_trade.max_adv_participation` | 0.05 | Tim Cook has not run — see §2.4 |
| `per_trade.stop_required` | true | satisfied in writing by 老詹 |
| `portfolio.leverage` | **none — hard rule** | **Webull account is a margin account with negative USD cash (§1.6)** |
| `concentration.max_sector` / `max_correlated_cluster` | 0.35 / 0.40 | NOT COMPUTABLE — `portfolio.yaml` empty (CRO §2, eighth escalation). AVGO at Webull is in the same AI-capex cluster as SKHY |

### 1.4 John's sizing derivation, restated (CRO §9) — I do not re-derive it

Premium ≈ 50% → premium component = 1 − 1/1.50 = **33% of price**, with no stop under it. 1% budget ÷ 0.33 = **3.0% of LNW**. Sensitivity: 44% premium → 3.3%; 56% → 2.8%. John uses 3.0%. If the Owner formally overrides the premium treatment: stop-by-gap ceiling 1% ÷ 13.4% = **7.5%**, logged as dissent (§8). (Premium at $131.07 vs Seoul: NOT COMPUTABLE this session — 13 Nov 000660 close and USD/KRW not on disk.)

### 1.5 Valuation inputs (𢦀鳩仔 §0, §8)

| Construction | ADS value | MoS at $129 (𢦀鳩仔) | MoS at $131.07 (my arithmetic, same FVs) | 40%-MoS entry price |
|---|---|---|---|---|
| Parity, central (cap lifted) | $80.0 | −61% | −64% | $48 |
| Probability-weighted, central (30% lift in 12m) | $102.4 | −26% | −28% | $61 |
| Premium persists, central (× 1.40) | $112.0 | −15% | −17% | $67 |
| Probability-weighted, high | $129.4 | 0% | −1% | $78 |
| Scenario (c) × 1.40 — the one construction that passes | $150.7 | +14% | +13% | — |

Valuation score for the ADS at $129: **25/100**. Technical score: **35/100** (老詹 §10). Risk score: **32/100** (CRO §10). **Committee score: NOT OBTAINED** — committee has not convened.

### 1.6 What the Webull pull tells us about the denominator (coordinator, 19:50 UTC 13 Nov; read-only)

| Fact | Value | Bearing on sizing |
|---|---|---|
| Account type | **individual MARGIN, HKD base** | `leverage: none` is a hard rule; John's Condition 3 requires the ADS to be unmargined. This account cannot hold SKHY compliantly as it stands |
| SKHY held at Webull | **none** | the position sits at another broker (Futu; Longbridge attempted) — **NOT CONFIRMED** |
| Holdings | **2 AVGO at $353.16 cost** (= $706.32 at cost) | same AI-capex cluster as SKHY (CRO §7) — thickens, does not diversify |
| Total market value | **HK$5,396 ≈ US$690** (implied ~7.82 HKD/USD) | if this is the whole LNW, see §5.3 case (a) |
| USD cash | **−$12.06** | the account is already **partly on margin** |

This does **not** tell us the Owner's LNW — Futu may hold far more. It tells us the *floor* on what we can see is ~US$690, and that one account is leveraged.

---

## 2. Sizing table — current size vs cap

### 2.1 The test the Owner runs (thirty seconds)

```
position % of LNW   =  ADS held × 131.07 ÷ LNW × 100
above the cap?      =  ADS held × 131.07  >  0.03 × LNW
max ADS at the cap  =  0.03 × LNW ÷ 131.07      =  LNW ÷ 4,369
excess to sell now  =  ADS held − (LNW ÷ 4,369)                  [if positive]
fraction to sell    =  1 − 3.0 ÷ (position %)                    [if position % > 3.0]
```

John's Condition 1: if above 3.0%, the excess is sold **in the next session, not at a level** — "the excess is regulatory premium, not a trade."

### 2.2 Scalable conversion table (at $131.07)

| Per … | ADS | $ |
|---|---|---|
| **$1,000 of position** | **7.63 ADS** | $1,000 |
| **100 ADS** | 100 | **$13,107** |
| **1% of LNW**, per $100,000 LNW | 7.63 ADS | $1,000 |
| **3.0% cap**, per $100,000 LNW | **22.9 → 22 ADS** | **$3,000** |
| **1.5%** (20 Jan target / my recommended size), per $100,000 LNW | **11.4 → 11 ADS** | **$1,500** |
| 7.5% (override case only), per $100,000 LNW | 57.2 → 57 ADS | $7,500 |

Arithmetic: ADS = $ ÷ 131.07; e.g. 3,000 ÷ 131.07 = 22.89. Round **down** to whole ADS (rounding up breaches the cap). Multiply the per-$100k rows by (LNW ÷ 100,000). John's "23 ADS at $129.66 per $100,000" (CRO §9) becomes **22 ADS at $131.07** — the cap is in dollars, so a higher price buys fewer ADS.

### 2.3 Current size → cap → excess, by case

| If the Owner's position is … | Status vs John's cap | Action now (Condition 1) | My recommended size (§6) |
|---|---|---|---|
| **> 3.0% of LNW at $131.07** | **over cap** | **sell the excess next session**: fraction = 1 − 3.0 ÷ position% (at 4.0% sell 25%; at 5.0% sell 40%; at 6.0% sell 50%; at 19% — one ADS on a $690 LNW — sell 100%) | then continue to 1.5% |
| **1.5% – 3.0%** | inside cap | hold approved with conditions; no mandatory sale today | reduce to ≤ 1.5% now rather than by 20 Jan |
| **≤ 1.5%** | inside cap, already at the 20 Jan level | hold with conditions | hold; nothing to do before the ladder fires |
| any size, if the Owner **overrides** the premium treatment in writing | cap 7.5% | sell excess over 7.5% next session; 20 Jan target hardens to ≤ 3.75% | logged as dissent (§8) |
| **any size, if the LNW is the ~US$690 we can see** | **over cap by construction** | **sell 100%** — see §5.3(a) | — |

**Mark-to-market drift.** A position that is exactly 3.0% at $131.07 becomes 3.15% at $137.71 (yesterday's close), 3.36% at $146.80, 3.43% at $149.90 (3.0 × price ÷ 131.07). The Owner does not need to chase this: the first mandatory trim fires at $146.80 and takes a 3.36% position to 2.24% (× ⅔). Between $131 and $146.8 the drift is at most +0.36 points and I treat it as inside tolerance; Condition 1 is about the size *today*.

### 2.4 Caps checked

| Cap | Result |
|---|---|
| `max_risk_per_trade` 1% — stop from cost (6.71%) | 1% ÷ 6.71% = 14.9% → PASS at any size ≤ 10% |
| `max_risk_per_trade` 1% — stop from market (8.18%) | 1% ÷ 8.18% = 12.2% → PASS at any size ≤ 10% |
| `max_risk_per_trade` 1% — gap construction (−13.4%) | 1% ÷ 13.4% = **7.46%** → PASS at ≤ 7.5% |
| `max_risk_per_trade` 1% — premium-to-parity construction (−33%) | 1% ÷ 0.33 = **3.0%** → **binding** (John) |
| `max_single_position` 10% at cost | PASS at 3.0%; does not bind even in the override case (7.5% < 10%) |
| `max_single_position_drifted` 15% | not binding at +1.6% |
| `leverage: none` | **FLAG.** Webull: margin account, USD cash −$12.06. SKHY account: NOT OBTAINED. Condition 3 unverified |
| `max_sector` 35% / `max_correlated_cluster` 40% | **NOT COMPUTABLE** — `portfolio.yaml` empty. Known cluster members now: SKHY (size undisclosed) + 2 AVGO (~$690). Each 1% of LNW in SKHY consumes 1 point of whichever cluster budget the Owner adopts |
| `max_adv_participation` 5% (Tim Cook) | **NOT RUN — inference only.** 老詹 §12 cites 15.77M ADS on 20 Oct and "20M/day" in October. 15.77M × $131 ≈ $2.1bn/day; 5% ≈ $100M. Any size this memo contemplates is orders of magnitude inside. Nov volume NOT OBTAINED |

---

## 3. Trim ladder — one table to read against a quote

All fractions are of the **then-current** position (John's wording), so the ladder compounds. "ADS per 100 held" means per 100 ADS held **at the moment the trigger fires**. Whole-ADS rounding: for "at least one-third" and for halvings round **up**; for cap-derived holdings round **down**.

| # | Trigger (Owner reads against a quote) | Direction | Fraction of then-current | Per 100 ADS held now, no earlier trigger fired | Residual (per 100 at start) | Residual as % of LNW if started at 3.0% at $131.07 | Order type (for 死潘狗) |
|---|---|---|---|---|---|---|---|
| **L1** | **Any daily print $146.80–$149.90** | SELL | **≥ ⅓** | sell **34** (33.3 rounded up) | **66** (66.7) | 2.00% at $131.07 → 2.24–2.29% at the band | resting **limit sell $146.80 GTC** — a limit at the band floor is the exact implementation of "any daily print" |
| **L2** | **Any daily print $158.50–$162.00** | SELL | **⅓** of what remains (66.7) | sell **23** (22.2 rounded up) | **44** (44.4) | 1.33% at $131.07 → 1.61–1.65% at the band | resting **limit sell $158.50 GTC**, sized after L1 fills |
| **D1** | **24 Dec 2026**: no 2027 US tool licence covering Wuxi reported | SELL | **½** of then-current | if no trims yet: sell 50 → 50 · after L1: sell 33 → 33 · after L1+L2: sell 22 → 22 | — | 1.50% / 1.00% / 0.67% at $131.07 | market or marketable limit **at next open** |
| **D2** | **By 20 Jan 2027 close**: position ≤ **1.5% of LNW** at market — unless 老詹 has logged a daily close > $152.35, then ≤ 3.0% | SELL down to target | ADS to sell = ADS held − (0.015 × LNW ÷ price on the day) | no trims, started at 3.0%: sell **50** → 50 · after L1 only: sell **17** → 50 · after L1+L2 at $131: **0** (44.4 ADS = 1.33%) | ≤ 1.5% | — | market or limit, dated before 20 Jan; **formula ticket, not fixed quantity** |
| **M1** | **Friday premium check**: premium < 25% while 000660 flat-or-up on the week | SELL | **½** of then-current | sell 50 | 50 | 1.5% | market **at next open** |
| **M2** | **Any KSD / FSC / depositary announcement** widening or lifting the ADS quota | SELL | **100%** | sell 100 | 0 | 0 | market **at next open** |
| **S** | **Daily close < $120.35** | SELL | **100%** | sell 100 | 0 | 0 | **NO resting stop order.** Owner checks the close; if below $120.35, market sell **at next open** (CRO §4: "pick the gap, not the wick") |

**Order of operations if several fire together (CRO §8):** S and M2 are sell-everything and override the trims; D1 and M1 are sell-half; L1/L2 are trims. **Take the largest reduction that any fired condition demands, once** — do not stack L1 on top of a D1 halving in the same session.

**Price-dependence of D2.** At 20 Jan the test is at *market*: a position that is 1.33% at $131.07 after both trims is 1.61% at $158.50 (1.33 × 158.5 ÷ 131.07) and needs ~7% more sold — unless the >$152.35 close has been logged, in which case the target is 3.0% and nothing is sold. 死潘狗 cuts D2 as a formula (§7).

**Proceeds, per 100 ADS held at start:** L1 sells 33.3 ADS at $146.80–149.90 = **$4,893–$4,997**; L2 sells 22.2 ADS at $158.50–162.00 = **$3,522–$3,600**. Cumulative after both: 55.6% of ADS sold, residual 44.4%.

**No add tranche.** John vetoed the add (Condition 5); 老詹's $127.3–130.0 zone — which the 13 Nov low of $129.18 touched — appears in §1.2 for the record only. This ladder has sell rungs only.

---

## 4. Risk per trade at the stop

**Method (my mandate):** risk = size × distance to stop; size = budget ÷ per-share risk. Stop is 老詹's ($120.35 close), budget is John's (1% of LNW). I combine them.

### 4.1 Per-unit arithmetic

| | From cost $129.00 | From market $131.07 |
|---|---|---|
| Distance to $120.35 | 129.00 − 120.35 = **$8.65** | 131.07 − 120.35 = **$10.72** |
| As % | 8.65 ÷ 129.00 = **6.71%** | 10.72 ÷ 131.07 = **8.18%** |
| Loss **per ADS** | **$8.65** | **$10.72** |
| Loss **per 100 ADS** | **$865** | **$1,072** |
| Loss **per $1,000** of position | 1,000 × 8.65 ÷ 129 = **$67** | 1,000 × 10.72 ÷ 131.07 = **$82** |
| Loss **per 1% of LNW** held | 0.0671% of LNW | 0.0818% of LNW |

The cost-basis figure is what the Owner *loses from break-even*; the market figure is what the position *drops from here*. Both are inside one day's range on this instrument (CRO §4: 5–13% daily ranges), which is why John calls it "a good thesis-stop and a poor loss-stop."

### 4.2 Size that keeps the stop-loss inside `max_risk_per_trade`

```
size_max = 1% ÷ distance
  from cost:    1% ÷ 6.71%  = 14.9% of LNW  → capped at 10% by max_single_position
  from market:  1% ÷ 8.18%  = 12.2% of LNW  → capped at 10%
  by gap −13.4%: 1% ÷ 13.4% =  7.5% of LNW  (John's stop-derived ceiling)
```

### 4.3 Reconciliation with John's 3.0% cap — which binds

| Construction | Ceiling | Risk at John's 3.0% cap | Share of the 1% budget used |
|---|---|---|---|
| Stop by trade, from cost | 14.9% → 10% | 3.0% × 6.71% = **0.20% of LNW** | 20% |
| Stop by trade, from market | 12.2% → 10% | 3.0% × 8.18% = **0.25% of LNW** | 25% |
| Stop by gap (−13.4%) | 7.5% | 3.0% × 13.4% = **0.40% of LNW** | 40% |
| **Premium to parity, no stop (−33%)** | **3.0%** | 3.0% × 33% = **1.00% of LNW** | **100% — this is the binding row** |

**The stop does not bind. The premium does.** At John's cap the trade-stop consumes only a fifth to a quarter of the per-trade budget, and the gap-stop 40%. The 3.0% is set entirely by the ~33% of price that has no stop under it (CRO §3, §9). Were the Owner to override the premium treatment (§8), the gap-stop becomes binding at 7.5% and the trade-stop at that size would be 0.50–0.61% of LNW.

**Kelly cross-check (informational only; full Kelly forbidden by mandate).** Path trade: +15% to the middle of Reduce 1 ($148.35 from $129) against John's E[loss | stop hit] of −9.3% gives odds b = 1.61 and a break-even win rate of 38%. At an *assumed* 45–50% win rate full Kelly would be 11–19% and **quarter-Kelly 2.7–4.7%** — bracketing John's 3.0% from a different direction. This excludes the premium gap entirely (Kelly on a bet with an unstoppable −33% leg at unknown probability is not computable honestly), so it is a sanity check, not a size. Win rate is **ASSUMED**, not measured.

---

## 5. The gap case

John flagged (CRO §4) that a ~7–8% stop on an instrument with 10% daily ranges "will usually be hit by a gap." The loss is then not the stop distance but the gap size. Sized from **market $131.07** (where the position is), with cost shown where it differs.

### 5.1 Loss per unit

| Scenario | Exit ≈ (from $131.07) | Loss % | Per $1,000 at market | Per 100 ADS | Per 1% of LNW held |
|---|---|---|---|---|---|
| Stop fills at the level | $120.35 | −8.2% (−6.7% from cost) | **$82** ($67 from cost) | $1,072 ($865) | 0.082% of LNW |
| John's E[loss \| stop hit] | ~$118.9 | −9.3% (assumed weights) | $93 | $1,219 | 0.093% |
| **−13.4% gap (5 Nov precedent)** | **$113.51** | **−13.4%** | **$134** | **$1,756** | **0.134%** |
| **Parity (−35%; premium gone, Seoul unchanged)** | **$85.20** | **−35%** | **$350** | **$4,587** | **0.35%** |
| Premium gone + ordinary halved (held through the stop) | $60.29 | −54% | $540 | $7,078 | 0.54% |

### 5.2 Size that makes each survivable (loss ≤ 1% of LNW)

```
size_max = 1% ÷ loss
  −13.4% gap:   1% ÷ 0.134 = 7.46%  → 7.5% of LNW   (John's stop-derived ceiling)
  −35% parity:  1% ÷ 0.35  = 2.86%  → John rounds to 3.0% using the 50%-premium figure (−33%);
                                       at the 56%-premium end (−35.6%) it is 2.8%. I carry 3.0% as instructed
  −54% combined: 1% ÷ 0.54 = 1.85%  → not used as a cap — it is the cost of breaking Condition 2 (CRO §9)
```

**At John's 3.0% cap:** a −13.4% gap costs **0.40% of LNW**; parity costs **1.05%** (fractionally over the 1% line on the −35% construction — John accepts this via his 33% figure; I note it and do not re-litigate); the combined scenario **1.62%**. All inside the 20% drawdown budget (CRO §5).
**At my recommended 1.5%:** 0.20% / 0.53% / 0.81% respectively — the parity gap is then inside the per-trade budget on every premium measurement, which is a second reason for 1.5% now (§6).
**At the 7.5% override size:** 1.00% / 2.63% / 4.05% — the parity gap alone is 2.6× the per-trade budget. That is what the override buys.

### 5.3 The 3% cap, three ways — because of what the Webull pull shows

The only account the firm can see holds **~US$690** (2 AVGO), is a **margin** account, and holds **no SKHY**. The SKHY position sits at a broker we cannot read. LNW remains NOT DISCLOSED, but the cap must now be read against three denominators, not one:

| Case | LNW assumed | 3.0% cap | Whole ADS at $131.07 | 1.5% level | Reading |
|---|---|---|---|---|---|
| **(a) Webull is the whole liquid net worth** | **US$690** | **$20.70** | **0** (one ADS = $131.07 = **19.0% of LNW**) | $10.35 → 0 ADS | **Any SKHY holding at all is over the cap by at least 6×. John's "hold at ≤ 3%" converts, by his own Condition 1, to "reduce to zero in the next session."** The 1% risk budget is $6.90; the stop-loss on a single ADS ($8.65–10.72) exceeds it on its own, before the premium. **Under (a) the position is a "pass" in my mandate's sense — too small a budget to hold even one share — and the correct size is zero** |
| **(b) LNW is 10× Webull** | US$6,900 | $207.00 | **1 ADS** (= 1.90% of LNW) | $103.50 → **0 ADS** | One ADS is inside John's cap; **zero** is the only whole-ADS size inside my 1.5% recommendation and the 20 Jan target. Two ADS (3.8%) is over cap. A −35% parity gap on one ADS = $45.87 = 0.66% of LNW — survivable; the trim ladder is meaningless at one share (a "third" of one ADS cannot be sold), so under (b) the ladder collapses to: hold 1 ADS, sell it at the first of L1 / D1 / D2 / S / M1 / M2 to fire |
| **(c) per 1% of LNW (general, as before)** | any | 3 × (1% of LNW) | LNW ÷ 4,369 | LNW ÷ 8,738 | §2.2 and the ladder in §3 apply as written. At LNW = $69,000 (100× Webull): cap = $2,070 = **15 ADS**; 1.5% = **7 ADS** |

**Said plainly:** under reading (a), the Owner is over the cap by construction and John's approval to hold does not exist — it is a reduce-to-zero. **The Owner must disclose the denominator (LNW, or at minimum the Futu account value) before reading (a) can be dismissed.** Until then I report (a), (b) and (c) side by side and recommend nothing that presumes (c). I do not assume the Futu account is large; "he has another broker" is not a number.

### 5.4 Illustrative worked example — **ILLUSTRATIVE, not the Owner's numbers**

Assume LNW **$500,000** (illustrative) and a position at John's cap.

```
3.0% cap        = $15,000 ÷ 131.07 = 114.4 → 114 ADS  = $14,942 (2.99% of LNW)
1.5% target     =  $7,500 ÷ 131.07 =  57.2 →  57 ADS  =  $7,471
Stop from cost  = 114 × $8.65  =   $986   = 0.20% of LNW
−13.4% gap      = 114 × 131.07 × 0.134 = $2,002 = 0.40% of LNW
−35% parity     = 114 × 131.07 × 0.35  = $5,230 = 1.05% of LNW
Ladder: L1 sell 38 (⅓ of 114, rounded up) → 76 held; L2 sell 26 (⅓ of 76) → 50 held
        50 ADS at $158.50 = $7,925 = 1.59% → D2 (if no >$152.35 close logged) sells 3 more → 47 ADS = 1.49%
        D1 (24 Dec, if fired before L1): sell 57 → 57 held = 1.5%
```

Over cap example: if the Owner holds 150 ADS on the same $500,000 (3.93%), Condition 1 sells 150 − 114 = **36 ADS next session**; my recommendation then takes it to 57.

---

## 6. What the 40% margin-of-safety failure means for size

**For a new position: zero.** 𢦀鳩仔 requires a 40% MoS; the price that satisfies it is $48 (parity central), $61 (probability-weighted central) or $67 (premium-persists central). At $131.07 the MoS is −64% / −28% / −17%. The one construction that passes (+13%) is scenario (c) at 35% probability multiplied by the premium persisting at ~70% — one branch of a tree, not a central case. No committee has convened, John would veto an initiation at any size (CRO §10: "I would not approve *initiating* SKHY ADS at $129 under any sizing"), and my own rule says "pass" when the sized position is too small to matter. **A buy ticket does not exist in this memo.**

**For the existing position at +1.6%, the question is how MoS interacts with John's cap.** They measure different things: the MoS is a statement about *expected return* (the price is above every central value); John's 3.0% is a statement about *loss tolerance* (how much can go wrong before the 1% budget is breached). A negative MoS does not change the loss arithmetic, so it cannot move the cap. What it moves is **conviction**, and under my method (step 3) conviction scales size *within* the budget: high-scored ideas toward the cap, marginal ones at half.

**Scores on disk:** valuation 25/100, risk 32/100, technical 35/100; committee NOT CONVENED. Every desk that has scored this is below 40. On my own scale that is not "marginal" — it is below the line where I would size anything *up* toward a cap. The conviction-scaled size for a held position with these scores is **half the cap: 1.5% of LNW** — which happens to be the level John already requires by 20 Jan 2027 (Condition 7).

**Does that argue for 1.5% now rather than by 20 Jan? Yes, on three grounds, with one honest counter-argument.**

1. **The MoS failure is a today fact, not a January fact.** Condition 7 is dated to events (4Q26 print, buyback end, capex round). The valuation says the position is over-priced on every central construction *now*; waiting for the calendar to force a reduction is holding a negative-expected-return exposure for ten weeks for no stated reason.
2. **The gap maths in §5.2.** At 1.5% the parity gap (−35%) costs 0.53% of LNW — inside the 1% per-trade budget on every premium measurement (44–56%). At 3.0% it is 1.05%, marginally outside on the −35% construction. Half the cap is where the unstoppable leg is inside the budget without rounding.
3. **John's own observation (CRO §3.4):** "the exit cost of this risk is currently zero and will not be zero after the announcement." At +1.6% the Owner can sell the premium at a small gain. Every week of waiting is a week in which that may stop being true, and the 13 Nov low ($129.18) was 7 cents from cost.

**The counter-argument, stated fairly:** selling half at $131 forgoes the chance to trim that half at $146.8–149.9 (+12–14%) under Condition 8. On 100 ADS that is 33 ADS × ~$16 = **~$530 of foregone gain per 100 ADS** if the band is reached. Against that: the cost of carrying the extra 1.5% through a −13.4% gap is 0.20% of LNW (per 100 ADS at 3%: ~$880); through parity, 0.53% of LNW. **The trade-off is ~$530 of conditional upside per 100 ADS against ~$880–$2,300 of conditional loss per 100 ADS.** It is not a close call on the numbers, but it is a *judgment* call on probabilities nobody has measured, so I record it as a recommendation inside John's cap, not as a condition. John's conditions stand either way.

**My recommendation:** reduce to **≤ 1.5% of LNW now** (sell half of a cap-sized position; sell 1 − 1.5 ÷ position% of anything larger), keep the full ladder in §3 on the residual, and do not wait for 20 Jan. Under denominator reading (a) in §5.3 the recommended size is **zero**; under (b) it is zero at 1.5% and one ADS at the 3.0% cap.

---

## 7. Hand-off to 死潘狗 — ticket list, in order

**Global constraints on every ticket (read before cutting any):**
- **SELL tickets only.** No BUY ticket exists for SKHY at any price (CRO Condition 5).
- **No ticket may be placed on margin, and no ticket may be placed in a margin account.** The Webull account seen on 13 Nov is an individual margin account already carrying **negative USD cash (−$12.06)**; it holds no SKHY, so no SKHY ticket goes to it. The SKHY account (presumed Futu — NOT CONFIRMED) must be confirmed cash/unmargined before the first ticket is cut (CRO Condition 3; `leverage: none`). Proceeds of every sale settle to cash; nothing is redeployed by this memo.
- **Quantities are formulas** where marked, because ADS count and LNW are not disclosed. 死潘狗 fills the formula with the Owner's numbers; he does not pick a number.
- **Order of operations if several fire together:** T0 and T6/T7 (sell-all) override everything; T4/T5/T8 (sell-half) override trims; take the largest single reduction once (CRO §8).
- **Stop type:** T6 is a **close-basis** rule executed at the next open. **Do not** place a resting intraday stop at $120.35 (CRO §4, §11 item 4).

| # | Ticket | Trigger | Direction | Quantity | Order type | Timing | Source |
|---|---|---|---|---|---|---|---|
| **T0** | **Denominator gate** | before any other ticket: Owner supplies ADS count and LNW (or confirms Futu account value) | — | — | — | **now** | §5.3; CRO Condition 1, 10 |
| **T1** | **Cap compliance** | ADS × 131.07 > 0.03 × LNW | SELL | ADS held − floor(0.03 × LNW ÷ price) · **if LNW ≈ $690 (reading a): 100%** | market at open, or marketable limit ≤ 0.5% below last | **next session**, not at a level | CRO Condition 1 |
| **T2** | **Conviction reduction (Zac's recommendation — Owner's choice, not a CRO condition)** | Owner accepts §6 | SELL | ADS held − floor(0.015 × LNW ÷ price); for a cap-sized position, **50%** | limit at or near last; not urgent intraday | next session, after T1 | §6 |
| **T3** | **Trim 1** | any daily print $146.80–$149.90 | SELL | **≥ ⅓ of then-current** (round up; 34 per 100) | **resting limit sell $146.80, GTC** | place now; sits until filled | 老詹 §9(b); CRO Condition 8 |
| **T4** | **Trim 2** | any daily print $158.50–$162.00 | SELL | **⅓ of then-current after T3** (round up; 23 per 100 original) | **resting limit sell $158.50, GTC**; re-size after T3 fills | place after T3 fills | same |
| **T5** | **Wuxi tripwire** | **24 Dec 2026**: no dated report of a 2027 US tool licence covering Wuxi in `reports/news/` | SELL | **½ of then-current** (round up) | market or marketable limit **at next open** | 26 Dec open (first session after 24 Dec; check holiday calendar) | CRO Condition 6 |
| **T6** | **Hard stop** | **daily close < $120.35** | SELL | **100%** | **market at next open — NOT a resting stop order** | the session after the qualifying close | 老詹 §9(c); CRO Condition 2 |
| **T7** | **Quota announcement** | any KSD / FSC / depositary announcement widening or lifting the ADS conversion quota (修大哥 watch) | SELL | **100%** | market at next open | the session after the announcement | CRO Condition 4 |
| **T8** | **Premium collapse** | Friday check: premium < 25% while 000660 flat-or-up on the week | SELL | **½ of then-current** | market at next open | Monday open after the qualifying Friday | CRO Condition 4 |
| **T9** | **Reduce-before** | by **20 Jan 2027** close | SELL | **ADS held − floor(0.015 × LNW ÷ price on the day)**; if 老詹 has logged a daily close > $152.35, use 0.03 instead of 0.015 | limit near last or market at close | any session ≤ 20 Jan 2027; **formula ticket** | CRO Condition 7 |

**Ticket arithmetic 死潘狗 can verify:** at $131.07, floor(0.03 × LNW ÷ 131.07) = floor(LNW ÷ 4,369) and floor(0.015 × LNW ÷ 131.07) = floor(LNW ÷ 8,738). For LNW $100,000: 22 and 11 ADS. For LNW $690: 0 and 0 — every ticket is "sell all".

**Record-keeping before the first ticket (CRO Conditions 9, 10; CLAUDE.md rule 4):** 腦大裝草 logs the $129 purchase retrospectively to `memory/decisions/` with this memo and John's review as dissent; the Owner populates `config/portfolio.yaml` with the SKHY line (ADS count, cost 129.00, broker, margin status) *and* the 2 AVGO at Webull. The firm now has a confirmed holding it can write into the file for the first time.

---

## 8. Dissent / overrides

| Item | Position |
|---|---|
| **Premium-treatment override** (Owner elects stop-only sizing) | Cap becomes **7.5%** of LNW; T9 target hardens to **≤ 3.75%** by 20 Jan 2027; `max_single_position` 10% still passes. **John logs the override as dissent; I concur with John.** At 7.5% the parity gap is 2.63% of LNW — 2.6× the per-trade budget with no stop under it (§5.2). I would not size there |
| **Zac vs John on timing** | None on the numbers. I recommend reaching the 1.5% level **now**; John requires it **by 20 Jan 2027**. Mine is inside his cap and is a recommendation; his is a condition. If the Owner holds at 3.0% until 20 Jan he is compliant with John and has declined my recommendation — that is his right, and it should be logged as such |
| **Zac vs 𢦀鳩仔** | None. The MoS test fails for a new position; for the held position I translate the failure into conviction (half the cap), not into a different cap |
| **Zac vs 老詹** | None. The 13 Nov low ($129.18) sits inside his add zone; the add is vetoed regardless |
| **Rounding** | John's "23 ADS per $100,000" was at $129.66; at $131.07 it is 22. Round cap-derived holdings down, trim quantities up |

---

## 9. NOT OBTAINED register

| Item | Status |
|---|---|
| **Owner's SKHY position** (ADS count / $ / % of LNW) | **NOT DISCLOSED** — all sizing given per $1,000, per 100 ADS, per 1% of LNW, and against three denominators (§5.3) |
| **Liquid net worth / portfolio value** | **NOT DISCLOSED** — floor of what is visible: ~US$690 at Webull (2 AVGO). `config/portfolio.yaml` still empty (eighth escalation stands) |
| **Which broker holds SKHY** and whether that account is **cash or margin** | NOT OBTAINED — not Webull; Futu presumed; Condition 3 (unmargined) **unverified**; Webull account *is* margin with USD cash −$12.06 |
| **Futu / Longbridge account values** | NOT OBTAINED |
| Other AI-capex cluster holdings beyond 2 AVGO | NOT OBTAINED — cluster and sector limits NOT COMPUTABLE |
| **Committee score** | NOT OBTAINED — committee has not convened; desk scores 25 / 32 / 35 used as conviction proxies |
| **13 Nov close** | NOT OBTAINED — $131.07 is a 19:50 UTC live print, not the close; the stop rule is a close rule |
| **000660.KS 12–13 Nov close; USD/KRW 10–13 Nov** | NOT OBTAINED — premium at $131.07 NOT COMPUTABLE this session; John's 50%-premium figure carried |
| **Current KSD conversion-quota status** (any change since 23 Jul) | NOT OBTAINED (per CRO §13) |
| **Wuxi 2027 licence status; exact 2026 expiry** | NOT OBTAINED — "31 Dec" DERIVED (CRO §6) |
| **Tim Cook liquidity check** (`max_adv_participation`) | NOT RUN — October vendor volume (15.77M / "20M per day") used as an inference only; Nov volume NOT OBTAINED |
| Mo Peter VaR; Mario stress test | NOT COMMISSIONED (CRO §13) |
| Daily OHLCV series; empirical frequency of ≥ 8% down days | NOT OBTAINED — gap probabilities are John's ASSUMED weights; Kelly win-rate in §4.3 is ASSUMED |
| 4Q26 results date; hyperscaler guidance dates | NOT OBTAINED — "late Jan 2027" per desks; 20 Jan 2027 is John's chosen reduce-before date |
| Whether the Owner has a stop rule in place and how | NOT OBTAINED (CRO §12 Q2) |
| HKD/USD rate used for "HK$5,396 ≈ US$690" | coordinator's conversion (~7.82 implied); not independently sourced |

**Searches used: 0 of 0 permitted.** Every figure above traces to one of the four input files, `config/risk-limits.yaml`, the coordinator's 13 Nov Webull read-only pull, or arithmetic shown in this memo. Illustrative sizes (§5.4) are labelled as such.

---
*Research and decision support, not financial advice. Recommendations only; the Owner executes. No agent of this firm places orders, and no SKHY buy ticket exists.*

---

## Corrections logged by the CEO after execution review (2026-11-13)

死潘狗 found three defects while implementing §7. Recorded here rather than silently
edited, consistent with house practice.

1. **T5 date.** "26 Dec 2026" is a Saturday; 25 Dec is the exchange holiday. **Corrected to
   Mon 28 Dec 2026** in the ticket file. The Owner should confirm against the exchange calendar.
2. **T4 per-100-ADS example.** §3 shows 23; whole-ADS arithmetic ⌈⅓ × 66⌉ = **22**. The ticket
   file uses 22.
3. **Order-of-operations bullet** describes T4 as "sell-half"; it is a **⅓ trim** of the
   remainder. Typo; the ladder table in §3 is correct.

CEO provisional rulings on questions referred to the CRO (John is unavailable until the
Fable model limit resets 19 Nov; these stand until he confirms or overrides):

- **Gap through both trim bands in one session:** **both T3 and T4 fill.** They are
  independent conditions on different levels, and a gap through both is precisely the
  strength the trims exist to sell into.
- **T7 (quota announcement) timing:** **next open, as written.** A same-session sale into a
  headline risks the worst fill of the day for no gain in protection.
- **T2 (Zac's 1.5%-now recommendation):** **OWNER'S CHOICE, withheld pending committee.**
  It carries neither a CRO condition nor a committee score.
