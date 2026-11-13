# SKHY — Position Sizing Memo

**Analyst:** Zac, Position Sizing (Dept 7) · **To:** Morris (PM); copies John (CRO), 死潘狗 (Execution)
**Date:** 2026-11-13 · **Instrument:** SK hynix ADS (Nasdaq: SKHY), 1 ADS = 0.1 ordinary (000660.KS)
**Owner's position:** cost **US$129.00/ADS**; **ADS count and liquid net worth (LNW) NOT DISCLOSED**
**Inputs (all on disk; no web searches this session):**
`reports/risk/2026-11-12-skhy-cro-review.md` (John — binding) · `reports/equity/2026-11-12-skhy-valuation.md` (𢦀鳩仔) ·
`reports/technical/2026-11-11-skhy-technical.md` §9 (老詹) · `reports/committee/2026-11-12-skhy-ceo-synthesis.md` (CEO) · `config/risk-limits.yaml`
**Status:** §0–§3 complete; §4–§9 being filled.

> Research and decision support, not financial advice. I size; 死潘狗 tickets; the Owner places. No agent of this firm places orders.

---

## 0. Summary

| Item | Figure | Source |
|---|---|---|
| **Hard cap (John, binding)** | **3.0% of LNW at market** | CRO §9, Condition 1 |
| **Conviction-scaled recommended size (mine, inside John's cap)** | **≤ 1.5% of LNW now** — i.e. the 20 Jan 2027 level, reached now rather than later (§6) | my method step 3 applied to desk scores 25 / 32 / 35 |
| New position at $129 | **Pass — zero.** MoS fails on every central construction (§6) | 𢦀鳩仔 §8.4 |
| Add | **Vetoed.** No add-tranche schedule exists | CRO §0 B/C, Condition 5 |
| Stop | daily close **< $120.35** → sell 100% at next open. **Not** a resting intraday order | 老詹 §9(c); CRO §4 |
| Risk at the stop, from $129 | **$8.65/ADS = 6.71% = $67 per $1,000**; at 3.0% size = **0.20% of LNW** (20% of the 1% budget) | arithmetic §4 |
| Which constraint binds | **The premium (no stop) → 3.0%.** The stop alone would allow 7.5% (gap-sized) / 10% (position cap). The stop is not the binding constraint | CRO §9; §4 below |
| Mandatory trims | ≥ ⅓ at any print **$146.8–149.9**; another ⅓ at **$158.5–162.0** | 老詹 §9(b); CRO Condition 8 |
| Reduce-before | ≤ **1.5%** of LNW by **20 Jan 2027** (≤ 3.0% if 老詹 logs a daily close > $152.35) | CRO Condition 7 |
| Wuxi tripwire | no 2027 US tool licence reported by **24 Dec 2026** → halve at next open | CRO Condition 6 |
| Premium monitor | premium < 25% with Seoul flat/up → sell half; any KSD/FSC/depositary quota widening → sell all | CRO Condition 4 |

**Everything below is in scalable form (per $1,000 of position, per 100 ADS, per 1% of LNW) because the two numbers that would make it concrete are not disclosed.** The Owner needs to supply *either* the ADS count and LNW, *or* the position as a percentage, and §2 converts in one line.

---

## 1. Inputs

### 1.1 Prices used

| Reference | Price | Source / status |
|---|---|---|
| Owner's cost | **$129.00** | brief; CRO header |
| Last confirmed daily close | **$129.66** (10 Nov 2026, derived) | 老詹 §2; CRO §4 |
| 11 Nov intraday | $142.68–$143.42 | 老詹 §11 (close NOT OBTAINED) |
| 12–13 Nov closes | **NOT OBTAINED** — no feed; no search permitted this session | — |

The risk arithmetic is run from **$129.00** (the brief's instruction: "from entry $129"). Where "at market" matters (John's cap is measured at market), I give the formula so the Owner plugs in the live quote; I also show $129.66 and $142.68 as the two dated reference points on disk. At break-even cost and market coincide to within 0.5%.

### 1.2 Levels (老詹 §9, logged 11 Nov, "will not be moved lower")

| Level | Price | Role |
|---|---|---|
| Early warning | intraday < $122.20 | watch only — not a trigger |
| **Hard stop** | **daily close < $120.35** | sell 100% next open |
| Add zone | $127.3–$130.0 | **vetoed by CRO — not used** |
| Do-not-chase | > ~$140 | no buy tickets at any price regardless |
| **Reduce 1** | **$146.8–$149.9** | trim ≥ ⅓ |
| Range-read confirmation | daily close > $152.35 | relaxes the 20 Jan target from 1.5% to 3.0% |
| **Reduce 2** | **$158.5–$162.0** | trim another ⅓ |
| Trend reversal | daily close > $162.0 *and* higher low > $129.66 | informational for this memo |

### 1.3 Budget and caps (`config/risk-limits.yaml`, read 13 Nov)

| Parameter | Value | Use here |
|---|---|---|
| `per_trade.max_risk_per_trade` | **0.01** of portfolio | the risk budget; John measures it on LNW |
| `concentration.max_single_position` | 0.10 at cost | ceiling on the stop-only construction |
| `concentration.max_single_position_drifted` | 0.15 | not binding at break-even |
| `per_trade.max_adv_participation` | 0.05 | Tim Cook has not run — see §2.4 |
| `per_trade.stop_required` | true | satisfied in writing by 老詹 |
| `concentration.max_sector` / `max_correlated_cluster` | 0.35 / 0.40 | NOT COMPUTABLE — `portfolio.yaml` empty (CRO §2, eighth escalation) |

### 1.4 John's sizing derivation, restated (CRO §9) — I do not re-derive it

Premium ≈ 50% → premium component = 1 − 1/1.50 = **33% of price**, with no stop under it. 1% budget ÷ 0.33 = **3.0% of LNW**. Sensitivity: 44% premium → 3.3%; 56% → 2.8%. John uses 3.0%. If the Owner formally overrides the premium treatment: stop-by-gap ceiling 1% ÷ 13.4% = **7.5%**, logged as dissent (§8).

### 1.5 Valuation inputs (𢦀鳩仔 §0, §8)

| Construction | ADS value | MoS at $129 | 40%-MoS entry price |
|---|---|---|---|
| Parity, central (cap lifted) | $80.0 | −61% | $48 |
| Probability-weighted, central (30% lift in 12m) | $102.4 | −26% | $61 |
| Premium persists, central (× 1.40) | $112.0 | −15% | $67 |
| Probability-weighted, high | $129.4 | 0% | $78 |
| Scenario (c) × 1.40 — the one construction that passes | $150.7 | +14% | — |

Valuation score for the ADS at $129: **25/100**. Technical score: **35/100** (老詹 §10). Risk score: **32/100** (CRO §10). **Committee score: NOT OBTAINED** — committee has not convened.

---

## 2. Sizing table — current size vs cap

### 2.1 The test the Owner runs (thirty seconds)

```
position % of LNW   =  ADS held × last close ÷ LNW × 100
above the cap?      =  ADS held × last close  >  0.03 × LNW
max ADS at the cap  =  0.03 × LNW ÷ last close
excess to sell now  =  ADS held − (0.03 × LNW ÷ last close)      [if positive]
fraction to sell    =  1 − 3.0 ÷ (position %)                    [if position % > 3.0]
```

John's Condition 1: if above 3.0%, the excess is sold **in the next session, not at a level** — "the excess is regulatory premium, not a trade."

### 2.2 Scalable conversion table

| Per … | At $129.00 (cost) | At $129.66 (10 Nov close) | At $142.68 (11 Nov intraday) |
|---|---|---|---|
| **$1,000 of position** = ADS | 7.75 ADS | 7.71 ADS | 7.01 ADS |
| **100 ADS** = $ | $12,900 | $12,966 | $14,268 |
| **1% of LNW** per $100,000 LNW = ADS | 7.75 ADS ($1,000) | 7.71 ADS | 7.01 ADS |
| **3.0% cap** per $100,000 LNW | **$3,000 = 23.3 ADS** | **$3,000 = 23.1 ADS** | **$3,000 = 21.0 ADS** |
| **1.5%** (20 Jan target / my recommended size) per $100,000 LNW | **$1,500 = 11.6 ADS** | $1,500 = 11.6 ADS | $1,500 = 10.5 ADS |
| 7.5% (override case only) per $100,000 LNW | $7,500 = 58.1 ADS | $7,500 = 57.8 ADS | $7,500 = 52.6 ADS |

Arithmetic: ADS = $ ÷ price; e.g. 3,000 ÷ 129.66 = 23.14. Multiply the per-$100k row by (LNW ÷ 100,000). John's own translation ("23 ADS at $129.66 per $100,000 of LNW", CRO §9) reconciles.

### 2.3 Current size → cap → excess, by case

| If the Owner's position is … | Status vs John's cap | Action now (Condition 1) | My recommended size (§6) |
|---|---|---|---|
| **> 3.0% of LNW at market** | **over cap** | **sell the excess next session**: fraction = 1 − 3.0 ÷ position% (e.g. at 4.0% sell 25%; at 5.0% sell 40%; at 6.0% sell 50%) | then continue to 1.5% |
| **1.5% – 3.0%** | inside cap | hold approved with conditions; no mandatory sale today | reduce to ≤ 1.5% now rather than by 20 Jan |
| **≤ 1.5%** | inside cap, already at the 20 Jan level | hold with conditions | hold; nothing to do before the ladder fires |
| any size, if the Owner **overrides** the premium treatment in writing | cap 7.5% | sell excess over 7.5% next session; 20 Jan target hardens to ≤ 3.75% | logged as dissent (§8) |

**Mark-to-market drift matters because the cap is measured at market.** A position that is exactly 3.0% at $129 becomes 3.32% at $142.68, 3.41% at $146.80, 3.49% at $149.90 (3.0 × price ÷ 129). The Owner does not need to chase this: the first mandatory trim fires at $146.80 and takes a 3.41% position to 2.27% (3.41 × ⅔). Between $129 and $146.8 the drift is at most +0.4 points and I treat it as inside tolerance; John's Condition 1 is about the size *today*, not about a rally pushing the mark over 3.0% on the way to the trim band.

### 2.4 Caps checked

| Cap | Result |
|---|---|
| `max_risk_per_trade` 1% — stop construction | 1% ÷ 6.71% = 14.9% → PASS at any size ≤ 10% |
| `max_risk_per_trade` 1% — gap construction (−13.4%) | 1% ÷ 13.4% = **7.46%** → PASS at ≤ 7.5% |
| `max_risk_per_trade` 1% — premium-to-parity construction (−33%) | 1% ÷ 0.33 = **3.0%** → **binding** (John) |
| `max_single_position` 10% at cost | PASS at 3.0%; would bind only in the override case above 7.5% — it does not, 7.5% < 10% |
| `max_single_position_drifted` 15% | not binding at break-even |
| `max_sector` 35% / `max_correlated_cluster` 40% | **NOT COMPUTABLE** — `portfolio.yaml` empty. SKHY is a pure AI-capex cluster member (CRO §7); each 1% of LNW in SKHY consumes 1 point of whichever cluster budget the Owner adopts |
| `max_adv_participation` 5% (Tim Cook) | **NOT RUN — inference only.** 老詹 §12 cites a vendor print of 15.77M ADS on 20 Oct and "20M/day" in October. 15.77M × $129 ≈ $2.0bn/day; 5% ≈ $100M. A 3.0%-of-LNW retail position is orders of magnitude inside this. Nov volume NOT OBTAINED; the liquidity constraint does not bind at any size this memo contemplates, but that is an inference, not a check |

---

## 3. Trim ladder — one table to read against a quote

All fractions are of the **then-current** position (John's wording), so the ladder compounds. "ADS per 100 held" means per 100 ADS held **at the moment the trigger fires**, not per 100 at the start. Whole-ADS rounding: for "at least one-third" round **up** (34 of 100, 23 of 67); for the halving round up.

| # | Trigger (Owner reads against a quote) | Direction | Fraction of then-current | Per 100 ADS held now, no earlier trigger fired | Residual (per 100 at start) | Residual as % of LNW if started at 3.0% (constant $129 price) | Order type (for 死潘狗) |
|---|---|---|---|---|---|---|---|
| **L1** | **Any daily print $146.80–$149.90** | SELL | **≥ ⅓** | sell **34** (33.3 rounded up) | **66** (66.7) | 2.00% at $129 → 2.27–2.32% at the band | resting **limit sell $146.80 GTC** — a limit at the band floor is the exact implementation of "any daily print" |
| **L2** | **Any daily print $158.50–$162.00** | SELL | **⅓** of what remains (66.7) | sell **23** (22.2 rounded up) | **44** (44.4) | 1.33% at $129 → 1.64–1.67% at the band | resting **limit sell $158.50 GTC**, sized after L1 fills |
| **D1** | **24 Dec 2026**: no 2027 US tool licence covering Wuxi reported | SELL | **½** of then-current | if no trims yet: sell 50 → 50 · if after L1: sell 34 → 33 · if after L1+L2: sell 23 → 22 | — | 1.50% / 1.00% / 0.67% at $129 | market or marketable limit **at next open** |
| **D2** | **By 20 Jan 2027 close**: position must be ≤ **1.5% of LNW** at market — unless 老詹 has logged a daily close > $152.35, then ≤ 3.0% | SELL down to target | ADS to sell = ADS held − (0.015 × LNW ÷ price) | if no trims and started at 3.0%: sell **50** → 50 · if after L1 only: sell **17** → 50 · if after L1+L2 at $129: **0** (44.4 ADS = 1.33%, already under) | ≤ 1.5% | — | market or limit at the close/open the Owner chooses, dated before 20 Jan |
| **M1** | **Friday premium check**: premium < 25% while 000660 flat-or-up on the week | SELL | **½** of then-current | sell 50 | 50 | 1.5% | market **at next open** |
| **M2** | **Any KSD / FSC / depositary announcement** widening or lifting the ADS quota | SELL | **100%** | sell 100 | 0 | 0 | market **at next open** |
| **S** | **Daily close < $120.35** | SELL | **100%** | sell 100 | 0 | 0 | **NO resting stop order.** Owner checks the close; if below $120.35, market sell **at next open** (CRO §4: "pick the gap, not the wick") |

**Order of operations if several fire together (CRO §8):** S and M2 are sell-everything and override the trims; D1 and M1 are sell-half; L1/L2 are trims. **Take the largest reduction that any fired condition demands, once** — do not stack L1 on top of a D1 halving in the same session.

**Price-dependence of D2.** At 20 Jan the test is at *market*, so a position that is 1.33% at $129 after both trims is 1.63% at $158.50 (1.33 × 158.5 ÷ 129) and would need ~8% more sold — unless the >$152.35 close has been logged, in which case the target is 3.0% and nothing is sold. 死潘狗 should cut D2 as a formula ticket, not a fixed quantity (§7).

**Proceeds, per 100 ADS held at start (for the Owner's cash planning):** L1 sells 33.3 ADS at $146.80–149.90 = **$4,893–$4,997**; L2 sells 22.2 ADS at $158.50–162.00 = **$3,522–$3,600**. Cumulative after both: 55.6% of ADS sold, residual 44.4%.

**No add tranche.** John vetoed the add (Condition 5); 老詹's $127.3–130.0 zone appears in §1.2 for the record only. This ladder has sell rungs only.

[PENDING: §4 risk at the stop · §5 gap case · §6 MoS and size · §7 tickets · §8 dissent · §9 NOT OBTAINED]
