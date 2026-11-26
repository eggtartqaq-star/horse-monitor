# CRO pre-review: 6160.HK (BeOne, held) and MSFT (not held)

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-26 (US closed for Thanksgiving; HK open) · **HEAD:** `1b0507f`
**Stage 3 of `/analyze`.**

**Inputs (all on disk):**
- the 25 Nov valuation, financials, management, news and technical reports for both names;
- `config/risk-limits.yaml` (unchanged since 2026-07-17);
- `config/portfolio.yaml` (empty);
- `config/portfolio-webull-snapshot-2026-11-13.yaml`;
- `reports/risk/2026-11-25-webull-readonly-snapshot.md`;
- my 17 Nov ruling `reports/risk/2026-11-17-mu-skhy-style-cro.md` (§4.3 tiers, §4.4 bands, §6.2 E-1 to E-7);
- `strategy/v6.6/data/MSFT.csv` for the MSFT tail.

**Rules kept:** no broker call, no `pip install`, no tracked file modified.

**Tags:**
- **[C]** a cited file;
- **[D]** my arithmetic;
- **[A]** my assumption.

**Not obtained:**
- the Owner's LNW, and therefore every "% of LNW" below;
- the 6160 share count and the broker's account type;
- the ONC 1-year worst day;
- Mo Peter's VaR and Mario's stress results. I did not commission them, because this session cannot dispatch agents. My planning gaps stand in.

## 0. Verdicts

| Name | Ruling | Risk score |
|---|---|---|
| **6160.HK** | **HOLD — APPROVED WITH CONDITIONS (interim)** (§1.5): no adds; 老詹's stop binds, close basis, on the **ONC** line; size ≤ **4.7% of LNW** at market through 18 Dec (2.0% if no stop commitment); excess trimmed; decision record; committee before 11 Dec. | **35** as is (size unknown, no stop committed, no record) → **55** with conditions met |
| **MSFT** | **No entry this year in practice.**<br>- **Value path:** ≤ US$320, which needs a −35.5% fall from US$496.13.<br>- **Trade path:** not approvable now. There is no compliant account and no LNW, and the windows are short.<br>- Tier B confirmed; E-1 and E-2 apply. | **25** for initiation at US$496 |
| **Committee** | **6160: YES, before 11 Dec** (ideally by 3 Dec). **MSFT: NO**. Park it with re-trigger alerts. | — |

## 1. 6160.HK (BeOne Medicines)

### 1.1 Where the HK$219.60 cost comes from

**It is an Owner disclosure. It has never been verified against a broker record.**
- **First appearance:** the August package (`reports/equity/2026-08-14-6160hk-financials.md` L6, "Owner position: bought HK$219.60"; commits `e7f6c82`/`fe6b987`, 20–21 Aug).
- **Carried into** `config/portfolio-webull-snapshot-2026-11-13.yaml` L10/L52 as "disclosed by the Owner", held at another broker (Futu, per the Owner), "size NOT DISCLOSED".
- **Every 25 Nov report** copies it from there. The news refresh says "from config, not re-verified".
- **There is no decision record for 6160** in `memory/decisions/`.

**What the figure is used for here.** The cost has no bearing on valuation (L-003). It does matter for one limit: `max_single_position` is measured "at cost".

### 1.2 Price facts and one cross-check correction

- **ONC:** US$415.62 at the 24 Nov close (Webull bar) [C: 老詹 L10]. ADS = 13 ordinary shares (verified, 老詹 §6).
- **HK-share equivalent:** HK$250.65 at 7.84 [C].
- **Last HK print on file:** HK$230.80 on **20 Nov**, single unconfirmed source [C: 老詹 L202].
- **Correction (LOW, for 𢦀鳩仔).** The valuation pairs US$415.62 (24 Nov) with HK$230.80 (20 Nov) as if they were simultaneous.
  - HK MoS of −82% against HK$127 is the stale figure. At the HK$250.65 equivalent it is **−97%** [D]: the same picture as the ADS (−98%).
  - Mark-to-market against cost is **+14.1%** on the equivalent, not +5.1% (the 20 Nov figure) [D].
  - The verdict does not change.

### 1.3 Valuation, TRIM zone, and what risk does with it

**Valuation:**
- Central US$210/ADS = HK$127 (range HK$106–154); buy-below HK$89; score 20.
- At HK$250.65 equivalent, the price is 2.0× central and 63% above the top of the range [C].

**My reading:**
- **The TRIM signal is a valuation argument, not a limit.** Overvaluation alone does not threaten survival, and I do not veto a hold on it.
- **What it does change:**
  - **No adds.** The price is 2.8× the buy-below.
  - **Size rather than return is what has to be defended:** a held-through de-rating to central fair value is about **−49%** [D: 127 ÷ 250.65 − 1].
- **Whether to trim for valuation is the committee's call (§3).** Trimming to my band (§1.5) is a risk condition, not a valuation call.

### 1.4 Stop: close basis, on which line

**Ruling: 老詹's stop binds as a close-basis exit on the ONC line.**
- **Trigger:** a **daily ONC close below US$385.00** [C: 老詹 §8].
- **Action:** sell the 6160.HK position at the **next HK session**. ONC closes at 05:00 HKT, before the HK open.
- **ONC rather than HK, for three reasons:**
  1. **Auditable:** the firm has ONC daily bars (Webull). It has no reliable HK series; the only late-November HK print is one unconfirmed quote page.
  2. **Observable before the action:** an ONC trigger is known before the HK open.
  3. **No whipsaw:** on 20 Nov the HK line fell 4.9% while ONC held its 385.00 low and closed at 390.94 [C: 老詹 §6]. An HK-line stop fires on moves that ONC later rejects.
- **HK$229.40 is an alert, not a stop.** An HK close below it means "check ONC that night".
- **Holidays:** if ONC does not trade (US holiday), the stop is evaluated at the next ONC close.
- **Stops are never moved down, and risk reduction is never blacked out (E-6).**
- **Distance:** US$30.62 = 2.55 × ATR(14), −7.37% [C].
- **Behavioural.** No broker stop exists on a close basis. **The Owner must commit to it in writing.** If he will not, the size cap falls to 2.0% (§1.5).

### 1.5 Size bands (LNW unknown; bands in % of LNW)

**Hard limits** (`config/risk-limits.yaml`) [C]:
- **≤ 10% of LNW at cost.** That is ≈ 11.4% at market, at +14.1% over cost [D].
- **Trim trigger:** > 15% at market.
- **Sector:** healthcare ≤ 35%.
- **Stop required:** true.
- **Leverage:** none.

**CRO operating band through 18 Dec.** The method is my 16 Nov tail formula: tail exit = stop × (1 − gap), cap = 1% ÷ loss to the tail exit.

| Case | Assumption | Loss to tail exit | **Cap, % of LNW at market** |
|---|---|---|---|
| **Stop committed** (ONC 385), planning gap 15% [A] | Tail exit 385 × 0.85 = 327.25 | 21.3% [D] | **4.7%** ← the binding band |
| Stress: gap 25% [A] (a BIOSECURE naming-type shock) | 288.75 | 30.5% [D] | 3.3% (stress, not the band) |
| **No stop commitment** | Held through to central fair value | 49.3% [D] | **2.0%** |
| Hard single-name limit | — | — | 10% at cost / 15% at market |

- **Why a 15% planning gap.** The ONC worst day is NOT OBTAINED. Realised volatility is 34.1% a year, about 2.1% a day [C: 老詹 L68], so 15% is about 7σ, which is conservative. It is the same planning gap I used for AVGO.
- **Mario** should stress a BIOSECURE naming and an HK policy shock before the committee meets.
- **Binding:** if the position is above the band, the excess is trimmed. Risk reduction is permitted on any day.
- **Correlation.** 6160 is **outside** the AI cluster (§4.3). Its relevant factor is **China/HK policy**, which it shares with **3416.HK** (HSCEI covered-call ETF, about HK$8,000, Owner-stated).
  - There is no country limit in the law. My 17 Nov proposal (d) for a country/FX line is still unadopted.
  - Until it is adopted I treat **6160 + 3416.HK** as one China-policy exposure for the committee. I set no number of my own.

### 1.6 Policy tail risk

- **BIOSECURE, OMB list due 18 Dec 2026** (statutory; it may slip):
  - **no source names BeOne**;
  - prohibitions apply only after the FAR revision, about 2028 on secondary estimates [C: news A-table L235].
  - **The risk is a sentiment gap on the list date, not a revenue event.** The 4.7% band is sized for it.
  - **WuXi AppTec's removal from 1260H on 10 Nov** is a mildly positive precedent, and "without prejudice to relisting" [C: L236].
- **Treasury COINS biotech outbound rule** (proposed 22 Oct; comments 7 Dec; final by 13 Mar 2027):
  - it governs **US persons' investments**;
  - the listed-securities exception likely carries forward; whether it covers an **HKEX** line, and whether BeOne is a "covered foreign person", is **NOT ESTABLISHED** [C: L237].
  - **New point, Owner fact needed:** if the Owner is **not a US person**, the rule's direct effect on him is nil, and only the market effect (US holders selling ONC) remains. His status is **NOT OBTAINED**.
  - **Re-rule** when the final text lands, or by 13 Mar 2027.
- **Nearer binaries:**
  - **ASH 12–14 Dec** (24 zanubrutinib, 8 sonrotoclax and 5 tacabrutideg abstracts);
  - CMS IPAY 2029 selection by 1 Feb 2027;
  - FY26 results about late Feb (unconfirmed) [C].
  - **E-3** (own-earnings blackout) applies to any add before the FY26 results; adds are barred anyway.
- **Tariff tail:** removed by the 31 Aug Section 232 exemption. Its term and the MFN/GENEROUS cost are undisclosed [C].

## 2. MSFT

### 2.1 Tier and blackouts

- **Tier B, counted 100% in the AI cluster: confirmed.** It is listed by name in my §4.3 table (`2026-11-17-mu-skhy-style-cro.md` L272), and the watchlist places it in the `ai` sleeve. It also counts 100% in **Info Tech** (≤ 35%; CRO headroom about 8.6pp after AAPL ≤ 6.4% and AI ≤ 20%).
- **E-1 (all sleeves):** no new position from the open of **Fri 4 Dec** to the close of **Thu 10 Dec**.
- **E-2 (Tier A/B):** from the open of **4 Dec** to the close of the **first full session after MU's FQ1 report** (~17 Dec). If MU's date is still unconfirmed on 9 Dec, it runs to the second session after the actual report.
- **E-3:** MSFT's own results are about late January. Not this year.
- **Windows left in 2026:**
  - **Fri 27 Nov (early close) to the close of Thu 3 Dec:** 5 sessions;
  - **about 18 Dec to 31 Dec.**

### 2.2 Is any entry allowed this year?

**Value path** (the valuation's own rule): **buy-below US$320** = 0.80 × US$400 [C].
- That is **−35.5%** from US$496.13 [D]. In 12 months of `data/MSFT.csv` the worst close was −9.99% (29 Jan 2026, the results reaction), and no other day was worse than −4.95% [D].
- **A 35% fall inside the two windows is not a planning case.** If it happened, it would happen *through* a broken 老詹 stop, so a fresh technical stop and a CRO re-score would be required at that time.
- **Conditions:**
  - committee;
  - CRO re-score;
  - decision record;
  - a new close-basis stop;
  - sized by the tail formula;
  - AI cluster ≤ 20% of LNW;
  - a cash (or margin-disabled) account;
  - LNW disclosed.

**Trade path** (老詹's E1 zone, 475–482, stop: close below 462.69). This is the MU T-path pattern; it is not proposed by anyone.
- **Tail-formula cap** [D], with the worst day 10.0% (29 Jan 2026) and tail exit 462.69 × 0.90 = 416.42:
  - **7.7% of LNW** at a 478 entry;
  - **6.2%** at 496.13;
  - both inside the cluster band, which is shared with AVGO.
- **Not approvable now, regardless of size:**
  - **(a)** valuation score 38, "do not initiate", price 24% above central;
  - **(b)** no account is known to qualify:
    - the Webull account is margin with a debit (G-3 bars any new position there);
    - Futu's account type is undisclosed;
  - **(c)** LNW is undisclosed, so no % can be turned into shares;
  - **(d)** the only pre-blackout window is 5 sessions, with an FOMC (Peterson: hike ~75%) after it.
- **Earliest admissible: after E-2 ends (~18 Dec)**, and only with:
  - a Morris proposal and committee approval **as a trade**, with 𢦀鳩仔's dissent recorded;
  - (b) and (c) cured;
  - a decision record with a time stop.

## 3. Committee

- **6160: convene before 11 Dec (ASH 12 Dec); by 3 Dec if possible.** It is a live position with:
  - no decision record;
  - an undisclosed size;
  - a TRIM-zone valuation (score 20);
  - three dated binaries inside 12 weeks.

  **Agenda:** hold vs valuation trim; the Owner's written stop commitment; size against §1.5; the retrospective decision record, with the thesis in the Owner's own words. A trim or exit can be executed on any day; a committee is not needed to *reduce* risk.
- **MSFT: do not convene now.** There is nothing to approve; the valuation itself says do not initiate. **Re-trigger** if either happens:
  - **(a)** a close ≤ US$320;
  - **(b)** a Morris trade proposal after E-2 ends.

  Until then it is watchlist only.

## 4. Cross-check of the key risk numbers

| Figure | Report | My check | Result |
|---|---|---|---|
| **6160 net cash** | US$4.8bn base / US$3.7bn conservative | 5,781.1 − 882.2 (LT debt, **Jun**) − 121.2 (ST debt, **Sep**) = **4,777.7**. 5,781.1 − 2,050 (aggregator total debt, probably incl. leases) = **3,731** [D] | **Arithmetic correct. Mixed dates, debt ladder not obtained, ST-debt column order inferred.** Immaterial: US$41/ADS is 10% of the price, and the bear uses 3.7. |
| 6160 equity value and MoS | US$49.0bn; −98% | 415.62 × 118M = 49.04bn; (210 − 415.62)/210 = −97.9% [D] | Correct. HK MoS restated as −97% (§1.2). |
| **MSFT lease-as-debt** | US$298bn = 62.3 finance + 21.7 operating + 65% × 329.1 uncommenced | 62.3 + 21.7 + 213.9 = **297.9**; ÷ 7.45bn shares = US$40.0/share [D] | **Arithmetic correct. One open methodology question (below).** |
| MSFT net cash ex-leases | US$29.0bn | 64,509 − 35,481 = **29,028** [D] | Correct |
| MSFT MoS and buy-below | −24%; US$320 | (400 − 496.13)/400 = −24.0%; 0.8 × 400 = 320 [D] | Correct |
| MSFT stop distance | 462.69 = 2.0 × ATR, −6.74% | 496.13 − 2 × 16.72 = 462.69 [D] | Correct |

**MSFT lease-as-debt, the open question.** It does not change the verdict.
- **The valuation's defence:** charging the US$329bn of signed-but-uncommenced leases as debt is consistent because EBITDA excludes their future **rent** (§4.2). That covers the **operating-lease** part.
- **The gap:** when the **finance-lease** part commences (FY27–FY33), it enters "capex incl. finance leases" (A5). FY27 FCFF already carries about US$28bn of finance leases. If those commencements come out of the US$329bn pool, the finance-lease share is **counted twice**: once as debt today, and again as capex when it commences.
- **Size of the effect:** at most the uncommenced deduction of **US$28.7/share** (+8% on the US$346 base DCF) [D].
- **Direction:** conservative, so fair value is if anything understated.
- **Verdict:** unchanged. Central FV plus the full US$29 stays below US$496, and the buy-below would move from US$320 to at most about US$343 [D: 0.8 × (400 + 28.7)].
- **For 𢦀鳩仔:** state whether A5 excludes commencements from the pool. If it does not, deduct only the operating-lease share.

## 5. Limits table

| Limit [C] | Hard | 6160.HK (held) | MSFT (not held) |
|---|---|---|---|
| Single position | 10% at cost; trim > 15% drifted | **UNVERIFIED** (size undisclosed); CRO band 4.7% (2.0% with no stop) | n/a; a trade-path cap would be 6.2–7.7% |
| Sector | 35% | Healthcare: only known name; UNVERIFIED | Info Tech: with AVGO and AAPL; headroom ~8.6pp (CRO) |
| AI cluster | 40% (CRO band 20%; new entries 0 from 4 Dec to ~17 Dec) | Outside | **Tier B, 100%**; E-2 applies |
| Per-trade risk | 1% | Satisfied by the band if the stop is committed | Satisfied by the tail cap |
| Stop required | true | **FAIL until the Owner commits** to ONC < 385 (close) | 462.69 for any trade path |
| Leverage | none | Futu account type **UNVERIFIED**; Webull breach on its face (G-1, deadline 3 Dec) | No compliant account known → no ticket |
| Cash floor | 10% (CRO ≥ 30%) | Not computable | Not computable |
| 1-day VaR 95% | 3% | Not computed (Mo Peter) | Not computed |
| Country / China policy | **none in the law** (17 Nov proposal (d)) | 6160 + 3416.HK flagged to the committee | — |
| Firm book | — | `config/portfolio.yaml` empty: **I cannot certify "inside all limits"** (escalated again) | — |

## 6. What the Owner must provide

1. **6160:**
   - share count (to place the position against the bands);
   - broker and account type (cash or margin);
   - a written commitment to the ONC close-below-385 stop;
   - the thesis in his own words (decision record);
   - **US-person status** (COINS).
2. **LNW** (one number). This is also needed by **3 Dec** for G-2 (AVGO).
3. **The G-1 cure** by the 3 Dec close. This is unchanged and comes first.

**For 腦大裝草:** `2026-11-26 · CRO pre-review 6160.HK + MSFT. 6160: HOLD WITH CONDITIONS — no adds; stop = ONC daily close < US$385 → sell 6160 next HK session (HK$229.40 = alert only); band ≤ 4.7% LNW at market thru 18 Dec (15% gap [A]), 2.0% if no stop commitment; trim excess; decision record (none exists); committee before 11 Dec. Cost HK$219.60 = Owner disclosure (Aug pack), unverified; HK MoS restated −97% (HK$230.80 was a 20 Nov print vs ONC 24 Nov). COINS: Owner US-person status needed. Risk 35 → 55. MSFT: Tier B confirmed; E-1 4–10 Dec, E-2 4 Dec–~17 Dec; value entry ≤ $320 (−35.5%) not a planning case; trade path not approvable (no compliant account, no LNW); no committee now; risk 25. Cross-checks: 6160 net cash 4,777.7 (mixed dates) ✓; MSFT leases 297.9 ✓, possible finance-lease double count (≤ $28.7/sh, conservative).`

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders; every trim or exit above is a recommendation for the Owner to execute himself.*
