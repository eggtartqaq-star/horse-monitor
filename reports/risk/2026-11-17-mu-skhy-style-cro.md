# CRO Ruling — MU initiation, SKHY re-entry, memory cluster, style allocation, AVGO margin, event blackout

**Author:** John, Chief Risk Officer (Department 6) · **Date:** 2026-11-17 (evening UTC, after NVDA FQ3 print)
**Status:** COMPLETE (v1) · written before the CEO's plan, as instructed
**Binding reference:** `config/risk-limits.yaml` (read 17 Nov 2026; unchanged since 12 Nov). `config/portfolio.yaml` read 17 Nov: `holdings: []`, `cash_balance: 0.00` (still empty — **tenth** escalation).

**Labels.** [C] config file · [R:desk] dated firm report · [D] derived (my arithmetic on cited inputs, formula shown) · [A] assumption. I made **no web fetches**; every market figure comes from the reports listed in §8.4. tradingkey.com not used. Mo Peter (VaR) and Mario (stress) were **not commissioned** — this session cannot dispatch agents; my own scenarios substitute and are labelled. All entries/exits below are **recommendations for the Owner**, not orders. No agent places, modifies or cancels orders (CLAUDE.md rule 1).

## 0. Verdict summary

| # | Question | Verdict | Risk score |
|---|---|---|---|
| 1 | **MU initiation at ~$700–737** (17 Nov close $712.42; AH $737.00) | **VETOED.** Not on survivability (the instrument is clean) but on price, trend/stop geometry, the event calendar and process. **No "trading-sized" exception exists in the limits file.** A pre-registered trend trade (T-path, §1.6) or a value entry (V-path) can lift it | **42 / 100** (July: 38, different method) |
| 2 | **SKHY ADS re-entry** after the $117.40 low and NVDA | **VETO STANDS** (16 Nov, unchanged). The two-way-conversion finding **does not change the cap formula**; marked **UNVERIFIED** (single search-relayed July source). It makes premium compression a *continuous flow* risk rather than only a regulatory jump, which strengthens the "p unmeasured → cap zero" rule | ADS **25** (from 26) · ordinary **40** (unchanged) |
| 3 | **MU vs SKHY vs 000660.KS** | **Order if any: 000660.KS first** (at R1 ≤ ₩1,070,000 with R0 gates), **ADS second** (only with a dated premium), **MU last** (≤ $350 committee level, or T-path). **None today.** Memory = **one cluster/one name**: combined cap **min[Σ tail-risk ≤ 1% of LNW, 5.0% of LNW]** | — |
| 4 | **Style: tech vs KO-type defensives** | Peterson's tilt is **ENDORSED on risk grounds** (it lowers cluster, VaR and drawdown load). KO/PG/XLP at ATH, RSI > 70: **not a risk veto, but no lump sum** — first tranche ≤ ⅓ of intended allocation, stop-sized, outside blackouts, and only after a pipeline/committee (none run on KO/PG/XLP). **AI-complex cluster CRO band ≤ 20% of LNW** (hard limit 40%) — derived from the VaR ceiling in today's volatility | — |
| 5 | **AVGO, 2 sh, Webull margin, USD −$12.06** | **`leverage: none` BREACH on its face — escalated (second time).** Clear the debit **by the close of 3 Dec** (before payrolls / FOMC / AVGO results 9 Dec); otherwise sell AVGO. Hold of AVGO conditional: debit cleared, ≤ 6.6% of LNW through the 9 Dec print, 老詹 stop, retrospective decision record | — |
| 6 | **Event calendar** | **Macro blackout 4–10 Dec** (all new entries, every sleeve). **AI-cluster blackout 4 Dec → first full session after MU's FQ1 print (~17 Dec)**. Existing SK hynix blackout from 24 Dec to the Wuxi licence. No entry on the 18 Nov NVDA gap | — |

**One-paragraph reasoning.** NVDA's beat-and-raise ($115.8bn vs $108bn guide; supply commitments $279bn → $390bn, "primarily … memory supply") is the best demand datum for memory since 30 Sep, and I credit it in the cycle component. It does not change any of the four things that decide a risk ruling: **price** (MU is 2.0× weighted fair value and 1.15× the *bull* case [R:𢦀鳩仔 §1]), **structure** (a confirmed downtrend of lower highs and lower lows, with a stop at $650 sitting ~1 ATR below the close [R:CEO-for-老詹 §2]), **calendar** (payrolls, FOMC + AVGO, CPI, MU's print, all inside 30 days) and **process** (no committee, no decision record, no 老詹 sign-off, and the only visible account is on margin). A one-session after-hours gap is not a trend change; the technical desk's own rule says so [R:tech §5]. Upside is not my department; survival is.

## 1. MU — initiation at ~$700–737

### 1.1 Inputs (all dated)

| Item | Value | Source |
|---|---|---|
| Price | close 16 Nov $719.02; close 17 Nov **$712.42** (intraday low $666.88); AH 17 Nov **$737.00** (+3.5%, thin print) | [R:tech §2, §5] Webull read-only |
| Volatility | 20d **103%**, 60d 72%, 1y 84.5%; 30.6% of days move > 5% | [R:tech §2] |
| ATR(14) | $59.18 = **8.2% / day** | [R:tech §2] |
| Worst / best day (300 sessions) | **−17.5% (5 Nov)** / +19.3% | [R:tech §2] |
| Beta to SPY (60d) | **3.1** (short window) | [R:tech §1] |
| Trend | Lower highs $1,108.55 → $990.00 → **$827.58**; lower lows $1,011.26 → $849.25 → **$650.00**; below MA10/20/50/200 (MA200 $767) | [R:tech §2] |
| Supports | **$650.00** (5 Nov low), **$598** (61.8% retracement) | [R:tech §2] |
| Touch probability of $620 (model, not forecast) | **57–60% in 1 month** (60d vol), 74–78% in 3 months | [R:tech §2] |
| Fair value | **$351** weighted (range $300–425); bear $168 / base $314 / bull $606; MoS −99%; expected return ~**−11%/yr** over 3 years; committee ≤ $350, entry ≤ $210; valuation score 20 | [R:𢦀鳩仔 §1, §10, §12] |
| News score | 42 → **50** after NVDA; "relief bounce until confirmed" (needs MU > $827.58) | [R:修大哥 NVDA §0] |
| Macro | Semis/AI hardware **underweight**; macro score for "buy semis on the dip now" **30** | [R:Peterson §Q3, score] |
| Correlation | MU–SKHY **0.88**, MU–SMH 0.86, MU–SPY 0.58, MU–AAPL −0.11, MU–KO −0.38 (15 Jul–16 Nov) | [R:tech §1] |

### 1.2 Verdict: **VETOED** (formal)

> **CRO VETO, 2026-11-17.** Initiation of MU at ~$700–737 is **VETOED** at any size, in any account. Under standing rule 3 it does not proceed unless the Owner personally overrides in writing; an override is logged as dissent and the §1.4 sizing still binds.

**Grounds** (1 and 2 are each sufficient alone; 3–5 are additional):
1. **Price above the bull case.** $737 is 2.1× the $351 weighted value and 1.22× the $606 bull case [D]. Held through to fair value the loss is **−52%** from $737; to the bear case −77% [D: 1 − 351/737; 1 − 168/737]. This is the same class of initiation veto as MRVL (~2.7× fair value) and KLAC (valuation-only veto) [C: watchlist notes]. It is a *downside-if-wrong* finding, not a return argument.
2. **The stop geometry is a coin flip in a confirmed downtrend.** Entry is mid-range between support $650 and resistance $827.58. A close-basis stop at $650 is 8.8% below the close — **1.07 ATR**, and *half* the worst day on file. The model touch probability of $620, which is below the stop, is 57–60% within a month [R:tech §2]. A stop that is more likely than not to fire within a month is a thesis stop, not a loss stop. Buying here pays the full gap tail (§1.4) to own a position the trend is still selling.
3. **Calendar.** Payrolls 4 Dec, FOMC 9 Dec (Peterson: ~75% hike), AVGO results 9 Dec, CPI 10 Dec, MU FQ1 ~16 Dec (unconfirmed) [R:Peterson catalysts; R:修大哥 §6]. A position opened now carries two name-relevant binaries and one macro binary inside 30 days on a beta-3.1 stock (§6).
4. **Process.** `committee_approval_required` not met; `decision_record_before_ticket` not met; `stop_required` cannot be met because the technical report is a **CEO stand-in with no 老詹 sign-off** [R:tech header].
5. **Leverage.** The only account the firm can see is an individual **margin** account carrying a USD debit (§5). No new position may be opened into it.

### 1.3 Fresh risk score: **42 / 100**

*Same six-component method as AAPL (57) and SKHY (26) on 16 Nov. Higher = more survivable. Below ~40 = veto on survivability alone; above 40 is not an approval.*

| Component | Weight | Score | Note |
|---|---|---|---|
| Instrument structure | 30% | **90** | Plain US common, deep liquidity, no basis/premium/conversion. Not 100: a reported Taiwan plant pause (C-tier) [R:𢦀鳩仔 §11] and undisclosed account type |
| Stop quality vs volatility | 15% | **20** | $650 stop ≈ 1.07 ATR; worst day 2× the stop distance; >57% one-month touch probability below it; no 老詹 sign-off |
| Valuation / cycle (downside if wrong) | 20% | **5** | Above the bull case; −99% MoS; 8/12 cycle indicators; PC OEM inventory rising, NAND wafer spot −13% in two weeks [R:修大哥 §4]. Not zero: ~$38bn own net cash, no solvency tail [R:𢦀鳩仔 §2.1]; NVDA's $390bn memory commitments credited here |
| Dated / event risk | 10% | **25** | FOMC + AVGO 9 Dec, CPI 10 Dec, MU ~16 Dec; 5 Nov −17.5% precedent; NVDA SEC civil probe at the largest HBM buyer (unpriced per 修大哥) |
| Correlation / concentration | 10% | **30** | 0.88 with SKHY, 0.86 with SMH, beta 3.1; AVGO already held; book undisclosed |
| Measurability | 15% | **35** | Primary bars (+); LNW, holdings, account type undisclosed; portfolio file empty (10th); VaR/stress not run; technicals unaudited |
| **Weighted** | | **42** | 0.30×90 + 0.15×20 + 0.20×5 + 0.10×25 + 0.10×30 + 0.15×35 = 27.0 + 3.0 + 1.0 + 2.5 + 3.0 + 5.25 = **41.75 → 42** [D] |

**Why 42 and a veto are consistent.** The score asks "can the book survive this at the capped size?" — yes, narrowly, because MU is a clean, liquid instrument and the cap is small. The veto asks "should it be opened now?" — no, on grounds 1–5. **Why it is up from July's 38** although price, trend and calendar are no better: July's score was holistic; this one uses the 16 Nov component method, whose 30% instrument weight rewards MU's clean structure. I am **not** treating +4 as an improvement in the risk. On the July method I would score it lower than 38.

**What moves it:** 老詹 confirms levels and a daily close > $827.58 with a higher low above $650 → stop component 20 → ~45, total ~46. MU print passed without a guide cut → event 25 → 45. LNW disclosed, portfolio populated, cash account confirmed → measurability 35 → 55. Close below $598 → valuation unchanged, trend worse, stop component → 10.

### 1.4 Stop logic and cap per 1% risk budget (103% vol, 8.2% ATR)

**Method (16 Nov, A.4, now standard):** plan on the expected loss, **size for the tail**. Tail exit = stop × (1 − worst day), worst day = 17.5% (5 Nov). Cap = 1% ÷ (1 − tail/entry). Close-basis stop, exit at the next open. [D throughout]

| Entry | Stop (daily close below) | Distance to stop | Naive cap (1% ÷ distance) | Tail exit | Tail loss | **Cap (% of LNW)** |
|---|---|---|---|---|---|---|
| $712.42 (17 Nov close) | **$650** | 8.8% | 11.4% → 10% limit | $536.25 | 24.7% | **4.0%** |
| $737.00 (AH) | **$650** | 11.8% | 8.5% | $536.25 | 27.2% | **3.6%** |
| $712.42 | **$598** | 16.1% | 6.2% | $493.35 | 30.8% | **3.2%** |
| $737.00 | **$598** | 18.9% | 5.3% | $493.35 | 33.1% | **3.0%** |

**If the Owner will not commit to the stop**, the cap is set by the held-through loss, as for AAPL: to fair value $351 from $737 → 1% ÷ 52.4% = **1.9%**; to bear $168 → **1.3%** [D].

**What the table shows.**
- The naive cap (1% ÷ stop distance) is **2.4–3× too large** at every row. On a stock that has moved > 5% on 30.6% of days, the stop distance is not the loss.
- A wider stop ($598) does **not** buy a much larger position; it buys a lower probability of whipsaw at a smaller size (3.0–3.2% vs 3.6–4.0%).
- **VaR check:** daily σ ≈ 103% ÷ √252 = 6.5%; 95% 1-day VaR ≈ 10.7% of position [D]. At 4.0% of LNW that is 0.43% of LNW — well inside `max_var_95_1d` 0.03 on a single name. VaR does not bind; the gap tail does.
- **These caps are what the law would allow if every gate were open. They are not an approval.** §1.2 stands.

### 1.5 Is ANY speculative / trading-sized position permissible under the limits file?

**Not today. And the file has no "speculative" or "trading" carve-out — I will not invent one.**

| Rule [C] | What it means for a "trade" |
|---|---|
| `committee_approval_required: true` | Applies to **every** new position, whatever its holding period or size. A trade is a proposal; the committee must approve it *as a trade* |
| `decision_record_before_ticket: true` | A trade gets a decision record, with its exit rules, **before** 死潘狗 cuts a ticket |
| `stop_required: true` | Stop set by 老詹, close basis. A CEO stand-in level does not satisfy it |
| `max_risk_per_trade: 0.01` | Size × tail loss ≤ 1% of LNW (§1.4) — combined with any SKHY/000660 holding, because they are one cluster (§3) |
| `leverage: none` | Cash account, no debit. The Webull margin account is ineligible until §5 is cured |
| `cash_floor: 0.10` | Must hold after the trade |
| `live_trading: forbidden` | Ticket only; the Owner places it |

A "small" position does not escape any of these. 1% of LNW is the ceiling *at risk*; "only 1–2% in size" is not a reason to skip the committee.

### 1.6 What lifts the veto — two pre-registered paths (the "trading plan" risk accepts)

**V-path (investment).** Price ≤ **$350** (𢦀鳩仔's committee level) → committee convenes; required entry ≤ **$210** (40% MoS) [R:𢦀鳩仔 §10]. Plus my re-score ≥ 40 at that price, a 老詹 stop, and the §1.5 gates. Size by the §1.4 formula at that time.

**T-path (trend trade — this is the only form of "trading plan" I will sign).** All of:
1. **Trigger:** a daily **close above $827.58** (the 11 Nov lower high), preferably after a higher low has formed above $650. Not an intraday print, not an after-hours print, not a single gap day [R:tech §5; 16 Nov B.4 "what does NOT qualify"].
2. **老詹 sets the stop** from the new structure (a close below the new higher low, or below MA200 ~$767 if he prefers). Illustrative caps at an ~$830 entry [D, tail method]: stop $767 → **4.2%**; $750 → 3.9%; $700 → 3.3%; $650 → 2.8%.
3. **Outside the blackouts in §6** — in practice either before the close of 3 Dec or after the first full session following MU's FQ1 print (~17 Dec).
4. **Committee approves it as a trade against valuation**, with the dissent of 𢦀鳩仔 recorded. The decision record carries: the stop; a **time stop** (exit if no close above $990, the 28 Oct lower high, within 30 sessions) [A: horizon is my judgement]; and **no averaging down**.
5. **Size = min[§1.4 formula at the actual stop, 4.0% of LNW, the memory-cluster headroom in §3].** No add to a trade unless 老詹 raises the stop so that aggregate tail risk stays ≤ 1%.
6. **Cash account confirmed** (§5) and LNW disclosed.

**Explicitly not permitted:** buying the touch of $650 or $598 ("catching the knife"); buying the 18 Nov open on the NVDA gap; selling puts or any naked short option for "income" on MU (`naked_short_options: forbidden` [C]); averaging down through a stop.

## 2. SKHY — re-entry veto review

### 2.1 What changed since 16 Nov

| Item | 16 Nov ruling | 17 Nov | Source |
|---|---|---|---|
| ADS price | $131.79 (13 Nov close) | close **$122.61**; intraday **new all-time low $117.40**; AH $127.91 (+4.3%) | [R:tech §3, §5] |
| Trend repair condition ("higher low above $122.20") | open | **FAILED** (broke intraday; closed back above) — void until 老詹 restates it from a new base | [R:tech §3]; [R:修大哥 §7] |
| Ordinary 000660.KS | ₩1.21–1.30m (10–11 Nov) | last dated **₩1,250,000 (12 Nov)**; 16–17 Nov close **NOT OBTAINED** | [R:修大哥 §3.1] |
| ADS premium | 43–52% (last range), current NOT OBTAINED | still **NOT OBTAINED**; direction "very likely narrowed since 6 Nov" (inference, no FX) | [R:修大哥 §3.2] |
| KSD quota | "exhausted 23 Jul, conversion one-way" | **"Two-way conversion permitted from 29 Jul 2026, only within the cap"** — quota recycles, not expanded | [R:修大哥 §3.2], edaily / mt.co.kr (July), search-relayed |
| Largest customer | Nvidia | beat-and-raise; $390bn supply commitments "primarily … memory"; **SEC civil probe** reported; no permanent CEO | [R:修大哥 NVDA §0] |
| China licences | Wuxi 2027 licence due ~31 Dec | **Dalian tool approvals held up** (Reuters, 3 Nov); 2027 authorisation not yet issued | [R:修大哥 §3.3] |
| Valuation | ADS FV $102.40 blended / $80 parity; ordinary ₩1,070,000 | unchanged; ADS score 30, ordinary 50 | [R:𢦀鳩仔 §12] |
| News score (ADS) | — | 33 → **40** post-NVDA | [R:修大哥 NVDA §6] |

### 2.2 Ruling: **VETO STANDS** — ADS and ordinary, at today's prices

Nothing in 2.1 lifts a ground of the 16 Nov veto. Ground by ground:
1. **Score below the line.** ADS re-scored **25** (§2.4). 
2. **Premium unmeasured.** Still no dated 000660 close with a dated FX rate. **Cap = 0 by rule B-2.**
3. **Value.** $122.61 is 20% above the $102.40 blended value and 52% above parity value [D: 122.61/102.40; 122.61/80.45].
4. **Process.** No committee, no decision record.
5. **Leverage.** Webull margin debit unresolved (§5).
6. **Ordinary.** KRX access unconfirmed; no KRX bars; no 老詹 KRW stop; last dated print ₩1,250,000 is 17% above R1 ₩1,070,000 [D].

**On the new low and NVDA.** A new low with the trend-repair condition failed makes the case *weaker*, not stronger. The NVDA gap (+4.3% AH) is exactly the "single gap-up day" that the re-entry plan excludes. It does not count.

### 2.3 The two-way conversion finding — does it change my premium formula?

**Ruling: NO change to the formula. The fact itself is marked UNVERIFIED.**

**Why the formula is unchanged.** The B-2 cap is 1% ÷ [1 − 1/(1 + p)]. It sizes the position so that a **complete collapse of the premium to parity** costs ≤ 1% of LNW. It is **mechanism-agnostic**: it does not care whether the premium goes to zero because the KSD lifts the cap, because conversion recycles, or because US demand evaporates. A change in the *mechanism* changes the *probability and speed* of compression, not the *size* of the loss if it happens. The formula sizes for the size.

**What the finding does change — and it cuts against re-entry, not for it.**
- *Under the old reading* (quota frozen, one-way), the premium could only collapse on a regulatory decision: a discrete, dated, reportable event that the firm's news desk could watch for.
- *Under the new reading* (quota recycles), any ADS holder who cancels into the ordinary frees quota that an arbitrageur can immediately refill by converting ordinary → ADS and selling the ADS. That is a **continuous leak** on the premium, driven by flows, that needs no announcement. The ADS making a new low while the last ordinary print was ~10% above its 6 Nov low [R:修大哥 §3] is consistent with exactly this — although it is unproven without a dated premium.
- **Consequence:** premium compression is a **live, unannounced** risk, not a tail that waits for a headline. That **strengthens** three existing rules: "p not measured → cap zero" (B-2); the weekly premium monitor (B-8); and the 12 Nov reduce-trigger (a narrowing of > 10 points while the ordinary is flat or up).
- **The downside floor** (a discount below parity) was already bounded by cancellation. The finding does not move it.

**Why UNVERIFIED.** It reaches the firm as a search-engine extraction of Korean outlets (edaily, mt.co.kr, July 2026), not a KSD or depositary notice; no primary document was opened [R:修大哥 §3.2, sourcing note]. It contradicts the four-desk "one-way" finding recorded in the watchlist. **The watchlist line "conversion is one-way" should be annotated "reported two-way within the cap since 29 Jul (UNVERIFIED)"** — not deleted until The dictator confirms from a primary source.

**Illustration only — not admissible for a ticket.** Using the 17 Nov ADS close ($122.61), the 12 Nov ordinary (₩1,250,000) and the 13 Nov intraday USD/KRW (~1,330), the premium would be ~30% [D: 122.61 × 10 × 1,330 ÷ 1,250,000 − 1]; at 1,380 it would be ~35%. The inputs are from three different days, one of them five sessions stale, so this fails the one-session rule. If a properly dated reading came in at 30%, cap (i) would be **4.3%** [D: 1% ÷ (1 − 1/1.30)] — still subject to the stop, value and committee gates.

### 2.4 Re-scores

| Component | Weight | ADS 16 Nov | **ADS 17 Nov** | Ordinary 16 Nov | **Ordinary 17 Nov** | Why it moved |
|---|---|---|---|---|---|---|
| Instrument | 30% | 5 | **8** | 60 | 60 | ADS: premium likely narrower and a recycling valve reported — but unmeasured and unverified |
| Stop quality | 15% | 35 | **25** | 30 | 30 | ADS: $120.35 stop level broken intraday; new low; no valid structural stop until 老詹 restates |
| Cycle | 20% | 30 | **35** | 30 | **35** | NVDA $390bn memory commitments (+), PC OEM inventory up and NAND spot falling (−); net small + |
| Event | 10% | 40 | **35** | 40 | **35** | Dalian approvals held; SEC probe at largest customer; MU print 16 Dec read-across |
| Correlation | 10% | 40 | **35** | 40 | **35** | Confirmed 0.88 with MU (one cluster); AVGO held |
| Measurability | 15% | 35 | 35 | 25 | 25 | No change |
| **Weighted** | | 26 | **25** | 40 | **40** | ADS: 2.4 + 3.75 + 7.0 + 3.5 + 3.5 + 5.25 = 25.4 → **25**. Ordinary: 18.0 + 4.5 + 7.0 + 3.5 + 3.5 + 3.75 = 40.25 → **40** [D] |

The ordinary stays **at** the line, not above it. It remains the closest SK hynix exposure to approvable, and it still fails its gates today.

### 2.5 Amendments to the 16 Nov SKHY conditions
- **B-4 trend repair:** the "$122.20 higher low" condition is **void**. 老詹 restates trend repair from the post-$117.40 structure, in KRW for the ordinary.
- **R2 confirmed at ₩856,000** (20% MoS on ₩1,070,000), replacing the undocumented ₩850,000 in my 16 Nov text, as the CEO's audit note proposed.
- All other B-conditions carry forward unchanged.

## 3. MU vs SKHY vs 000660.KS — order of approval and combined memory cap

### 3.1 They are one position

Daily-return correlation **MU–SKHY 0.88** (15 Jul–16 Nov) [R:tech §1]: R² ≈ 77% [D]. SKHY and 000660 are the same company. For every limit in the file I therefore treat **MU + SKHY ADS + 000660.KS as one memory position**:
- `max_single_position` (0.10) — applied to the **sum**.
- `max_risk_per_trade` (0.01) — **Σ (size × tail loss) ≤ 1% of LNW across all three.**
- `max_correlated_cluster` (0.40) and `max_sector` (0.35, Info Tech) — all three count in full.

"Diversifying" between MU and SK hynix is concentration in disguise. Owning both is one memory bet with two sets of idiosyncratic risk (US/Taiwan for MU; Korea/KRW/China fabs/ADS premium for SK hynix).

### 3.2 Combined memory cap

> **Memory cluster cap = min[ Σ size_i × tail_loss_i ≤ 1.0% of LNW ; 5.0% of LNW at market ]**

- **5.0%** is the provisional 000660 ceiling I derived on 16 Nov [1% ÷ (6.7% + 13.4%) ≈ 5.0%] and is now applied to the cluster as a whole. MU's own tail caps (3.0–4.0%, §1.4) and the ADS premium cap (2.9–3.3% at 43–52%) all sit inside it.
- A position in one name uses up the budget for the others. Example [D]: MU at 2.0% with a $650 stop from $712.42 uses 2.0% × 24.7% = 0.49% of the 1% budget; the remaining 0.51% allows at most ~2.5% of 000660 with a 20% tail loss [A: illustrative tail].
- **Today's permitted memory exposure: 0%** (§1.2, §2.2).

### 3.3 Which first, and at what level

| Rank | Instrument | Why this rank (risk) | Level at which I would **consider** approval | Gates |
|---|---|---|---|---|
| **1** | **000660.KS ordinary** | No premium; same business; lowest mid-cycle multiple (~15–17× vs MU ~32×) [R:𢦀鳩仔 §11]; risk score 40 | **R1 ≤ ₩1,070,000** (fair value) for the committee; R2 ≤ ₩856,000; R3 ≤ ₩642,000 | R0 (16 Nov B-5): LNW disclosed, **KRX access in a cash account**, Webull debit cleared, decision record, committee, 老詹 KRW stop, CRO re-score ≥ 40 (would reach ~48 with KRX bars and a stop); value + one cycle/trend confirmation; outside the 24 Dec–Wuxi blackout and 5 sessions before 4Q26 results |
| **2** | **SKHY ADS** | Same business; a third of the price was a regulatory rent; score 25 | Only via the ordinary-equivalent at R1/R2/R3 **and** a dated premium p | B-2 cap; if p unmeasured, zero. Prefer the ordinary if KRX access exists |
| **3** | **MU** | Cleanest instrument but most expensive (2× weighted FV, above bull); score 42 | **V-path ≤ $350** committee / ≤ $210 entry; or **T-path** close > $827.58 (§1.6) | §1.5 gates; §6 blackouts |

**Approve first: nothing today.** If one memory instrument reaches its gates first, it gets the budget; the others are sized from what remains (§3.2).

## 4. Style allocation — tech vs defensives

### 4.1 Peterson's tilt: **ENDORSED on risk grounds**

Peterson: overweight T-bills/cash, equal-weight and (modestly) financials; neutral staples/healthcare (stage in on pullbacks) and quality mega-cap tech; underweight semis/AI hardware and long Treasuries [R:Peterson §Q3]. Risk does not rule on which style will *return* more. It rules on whether the tilt keeps the book inside the limits with room to spare. It does:

| Risk measure | Effect of the tilt | Evidence |
|---|---|---|
| `max_var_95_1d` (3%) | Shifts weight from the 67–103% vol bucket (SMH v20 67.3%, MU 103%) to 18–28% vol buckets (RSP 18.1%, XLP 23.8%, KO 20.5%, PG 28.1%) | [R:Peterson table A] |
| `max_drawdown` (20%) | Semis just showed a −31% drawdown (SMH from 22 Jun); RSP is −2.4% from its high | [R:tech §4] |
| `max_correlated_cluster` (40%) | Underweight semis keeps the AI cluster far from the limit | §4.3 |
| `cash_floor` (10%) | Overweight cash/T-bills keeps a wide margin over the floor through four dated binaries | [C]; [R:Peterson catalysts] |
| `leverage` | Unaffected — must remain none | [C] |

**Three risk caveats the Owner should hear with the endorsement.**
1. **No hedge credit for staples.** KO/XLP vs semis at −0.4 to −0.5 [R:tech §1] is a four-month, single-regime statistic. Peterson's own read is that the staples bid is *flow out of AI*, not a bond trade, and that if the 10y pushes toward 5.40% while semis stabilise, both legs can fall together [R:Peterson §Regime, Q3 table]. Gold and long bonds have already failed as hedges in this regime [R:tech §4]. So: **staples may not be used to justify a larger AI position**, and the AI cluster is sized on its own (same principle as 16 Nov B.5).
2. **Defensives are crowded too.** October was the biggest tech→staples rotation since 2001; XLP's best month since 1998; KO fell on a beat [R:修大哥 §5]. A crowded defensive is a de-rating risk, not a crash risk — slow, low-vol and stoppable — which is why it gets staging rather than a veto.
3. **Quality mega-cap tech "neutral" does not mean add AAPL.** AAPL remains capped at ≤ 6.4% of LNW with the $325.08 stop and no adds above $245 (16 Nov). Its look-through in any QQQ/SPY holding counts toward that.

### 4.2 Buying KO / PG / XLP at all-time highs with RSI > 70

**Ruling: not a risk veto — but no lump sum, and not approvable today for process reasons.**

| | KO | PG | XLP |
|---|---|---|---|
| Price | $98.79 (17 Nov close) | ~$173.0 [D: 154.2 × 1.122] | $91.46 (17 Nov close) |
| RSI14 / vs MA50 | 74.1 / +9.3% | 73.1 / +12.2% | 66.1 / n.a. |
| v20 | 20.5% | 28.1% | 23.8% |
| MA50 (derived by Peterson) | ≈ **$91.0** | ≈ **$154.2** | not obtained |
| Distance to MA50 | −7.9% [D] | −10.9% [D] | — |
| P/E · dividend yield | 29.2× · 2.1% | 26.0× · 2.5% | — |

[R:tech §5; R:Peterson table A and Q2]

**Why not a veto.** The downside here is a reversion to the MA50 (−8% to −11%) or a de-rating as the rotation exhausts: slow, low-volatility and path-dependent, so a stop can intercept it. That is the AAPL case (25% vol, stoppable), not the MU case (103% vol, stop inside one ATR).

**Why not a lump sum.** Entering in full at an RSI > 70 all-time high puts the whole allocation at the point of maximum crowding, with the FOMC (a direct hit on bond proxies) three weeks away. Staging costs little if the trend continues and saves a lot if it reverts.

**Binding conditions on any defensive entry (S-1 to S-5):**
- **S-1 Staging.** At least three tranches. **Tranche 1 ≤ ⅓ of the intended allocation**; tranches 2–3 only on a pullback toward the MA50 or on a consolidation level 老詹 defines. No tranche inside the macro blackout (§6, 4–10 Dec).
- **S-2 Stop.** Each single-name tranche carries a close-basis stop from 老詹 (Peterson's falsifier — a close below MA50 while semis do *not* rally — is a natural candidate).
- **S-3 Size.** Single name ≤ min[10% (`max_single_position`), 1% ÷ (1 − stop × (1 − w)/price)], w = the name's one-year worst day — **NOT OBTAINED** for KO/PG/XLP. *Illustration only:* KO from $98.79 with a $91.0 stop and an assumed w = 5% [A] gives a cap of **8.0%** [D]. 老詹 must compute w before a ticket.
- **S-4 Sector.** Consumer staples (KO, PG, PEP and the full XLP line) ≤ 35% of LNW; healthcare (XLV) ≤ 35%. Diversified ETF lines count 100% to their sector.
- **S-5 Process.** KO, PG and XLP are **not on the watchlist and have had no pipeline, valuation or committee.** `committee_approval_required` applies to ETFs and staples exactly as to MU. Nothing is approvable until that is done.

### 4.3 What counts as the AI-complex cluster

`max_correlated_cluster: 0.40 — "e.g. total AI-complex exposure across sleeves"` [C]. My definition (binding until the Owner amends the file):

| Tier | Members | Counted | Why |
|---|---|---|---|
| **A: AI hardware / semis** | **AVGO** (held), **MU**, **SKHY / 000660.KS**, NVDA, AMD, TSM, MRVL, KLAC, INTC; **SMH / SOXX** (whole line) | **100%** | Revenue and multiple driven by AI capex; MU–SMH 0.86, MU–SKHY 0.88 [R:tech §1] |
| **B: AI platforms / hyperscalers** | MSFT, GOOGL, META, AMZN, PLTR | **100%** | The watchlist places MSFT, GOOGL and PLTR in the `ai` sleeve [C: watchlist]; their 2026 drawdowns moved with AI-capex sentiment. Conservative until a measured correlation says otherwise |
| **Index look-through** | QQQ, SPY, RSP, XLK | AI-name weight within the fund — **NOT OBTAINED**; **QQQ and XLK counted 100%** until the look-through is supplied; SPY/RSP counted at look-through only once obtained (0% meanwhile, flagged) | Conservative default for tech-heavy funds |
| **Outside** | **AAPL**, staples, healthcare, financials, energy, T-bills | 0% | AAPL: 16 Nov ruling (rents its model; ρ to MU −0.11) [R:tech §1] |

**Today's known cluster:** AVGO 2 shares (~$690 at 13 Nov) [C: Webull snapshot]. As a share of LNW: **NOT COMPUTABLE**.

### 4.4 Allocation bands as a function of liquid net worth

*All bands in % of LNW at market. "Hard" = `config/risk-limits.yaml`. "CRO band" = my recommended operating range for the current regime, valid until the first full session after MU's FQ1 print (~17 Dec), then re-ruled. The Owner allocates; this is the risk envelope, not an allocation.*

| Bucket | Hard limit [C] | Config target [C] | **CRO band now** | Basis |
|---|---|---|---|---|
| **Cash + T-bills ≤ 1 yr** (and government money funds) | ≥ 10% | 30% | **≥ 30%** | Config target; Peterson overweight; four binaries in 23 days. Counting T-bills ≤ 1 yr as cash is my interpretation — the Owner may overrule |
| **AI-complex cluster** (Tiers A+B, §4.3) | ≤ 40% | `ai` 30% (+ `technology` 20% — see 4.5) | **≤ 20%** · **new entries 0 until ~17 Dec** | **VaR:** SMH-like vol (v20 67.3%) → daily σ 4.24%, 95% VaR 7.0% of position; keeping the cluster to half the 3% VaR ceiling → 1.5% ÷ 7.0% = 21% → **20%**. At 40% the cluster alone would use 2.8% of the 3.0% ceiling [D]. **Drawdown:** a repeat of SMH's −31.2% at 20% = 6.2% of LNW (~⅓ of the 20% budget); at 40% = 12.5% [D] |
| — of which **memory** (MU + SKHY + 000660) | one name ≤ 10% | — | **≤ 5%**, Σ tail risk ≤ 1% · **0% today** | §3.2 |
| **Info Tech sector** (AAPL + Tier A + MSFT etc.) | ≤ 35% | — | ≤ 35%; AAPL ≤ 6.4% + AI ≤ 20% = 26.4% leaves ~8.6pp headroom [D] | AAPL cap from 16 Nov |
| **Consumer staples** (KO, PG, PEP, XLP) | ≤ 35% | — | up to 35%, **staged ≥ 3 tranches** (S-1 to S-5) | §4.2 |
| **Healthcare** (XLV etc.) | ≤ 35% | — | up to 35%, staged; XLV +17.8% over MA200, RSI 64 [R:Peterson] | same logic |
| **Financials** (XLF) | ≤ 35% | — | no risk objection; staged | Peterson modest overweight |
| **Equal-weight / broad index ETFs** | see 4.5 | `etf` 20% | no risk objection; sector look-through applies | lowest vol in the table (RSP 18.1%) |
| **Long Treasuries (TLT)** | — | — | not cash; no risk objection; Peterson underweight | TLT −9.6% from high |
| **Leverage** | **none** | — | **none** — margin disabled is the structural form | [C] |

**Worked example [D, illustrative LNW = $100,000 — not the Owner's figure]:** cash/T-bills ≥ $30,000; AI cluster ≤ $20,000 (of which memory ≤ $5,000, and $0 today); AAPL ≤ $6,400; staples ≤ $35,000 entered in ≥ 3 tranches; each single name ≤ $10,000. **Scaling:** every figure is that % × LNW. At LNW below ~$7,400, one MU share at $737 already exceeds 10% [D: 737 ÷ 0.10]; at LNW below ~$18,400 it exceeds the 4.0% MU cap [D: 737 ÷ 0.04]. Below those levels the answer for MU is "none", whatever the setup.

### 4.5 Ambiguities I will not resolve silently (Owner to rule)

1. **The 0.40-vs-0.50 contradiction** (tenth time of asking). `targets: ai 0.30 + technology 0.20 = 0.50` [C: portfolio] cannot be met if `technology` names are AI-cluster members, because the cluster limit is 0.40. Today it does not bind (the CRO band is 20%).
2. **Is a diversified ETF a "name" for `max_single_position`?** The file says "10% of portfolio per name". Until the Owner rules, I apply the **conservative reading: each ETF line ≤ 10%**. This makes the `etf: 0.20` target need at least two lines. I propose the 12 Nov `measure_at: look_through` clarification for broad diversified funds.
3. **T-bills as cash** for the floor (above).

## 5. AVGO on margin (Webull)

### 5.1 Facts

| Item | Value | Source |
|---|---|---|
| Account | Webull, **INDIVIDUAL_MRGN** (margin), HKD base | [C: `config/portfolio-webull-snapshot-2026-11-13.yaml`] |
| Position | **2 AVGO**, cost $353.16, last $344.87 (13 Nov), market ≈ $689.74 [D] | same |
| Cash | **USD −$12.06**, HKD +0.01; total cash HKD −94.35; initial margin in use HKD 2,698.22 | same |
| Decision record | **NONE** — bought outside the process | same; `memory/decisions/` |
| Event | **AVGO FQ4 results 9 Dec after the close** — the same day as the FOMC decision | [R:修大哥 §6] (Broadcom release 9 Nov) |
| Precedent move | **−15% in one session** in the early-November selloff (single source; date not pinned) | [R:修大哥 §1.1] (channelchek) |

### 5.2 Ruling

1. **`leverage: none` BREACH on its face — second escalation** (first: 16 Nov A.6). It is uncured four days later. The debit is 1.7% of the position [D: 12.06 ÷ 689.74] — trivial in dollars, but a negative cash balance in a margin account is borrowed money, and the rule is a **hard rule** with no de-minimis exception [C]. I will not create one silently.
2. **Deadline: the close of Thursday 3 Dec 2026** — before payrolls (4 Dec) and the FOMC/AVGO day (9 Dec). Remediation, any one of:
   - (a) deposit HKD and convert at least the USD debit (plus any accrued interest) so USD cash ≥ 0;
   - (b) sell **1 AVGO share** (~$345 at 13 Nov) — clears the debit and leaves 1 share;
   - (c) sell both shares.
   **Plus, structurally:** disable margin or convert the account to a cash account. That was first recommended on 10 Aug (3416 review) and never acted on [C: snapshot note]. CLAUDE.md requires controls to be "structural, not behavioural"; a margin account that the Owner chooses not to draw on is a behavioural control.
3. **If the debit is not cured by the close of 3 Dec**, my recommendation to the Owner is to **sell AVGO before the 9 Dec print**. I cannot place that order and do not; this is escalated to the CEO and Owner.
4. **Hold of AVGO after the cure — APPROVED WITH CONDITIONS (interim).**
   - **Size through the 9 Dec print ≤ 6.6% of LNW**: no stop exists, so the cap is set by a held-through gap at the −15% precedent: 1% ÷ 15% = 6.67% → **6.6%** [D]. The ~$690 position is within 6.6% for any LNW ≥ ~$10,450 [D: 689.74 ÷ 0.066].
   - **老詹 sets a close-basis stop** before 9 Dec; then the cap is recomputed with the tail formula.
   - **Retrospective decision record** (腦大裝草), with the Owner's thesis in his own words.
   - **No adds** (committee required; inside the AI-cluster blackout from 4 Dec in any case).
   - AVGO counts **100%** in the AI cluster (Tier A) and in Info Tech.
5. **No new position of any kind may be opened in the Webull account** while it is a margin account with a debit — including KRW using Webull's "KRW buying power", which is margin capacity (16 Nov B-3).

## 6. Event-risk calendar and blackout rules

### 6.1 Calendar (dates as reported; unconfirmed items marked)

| Date (2026) | Event | Names hit | Source |
|---|---|---|---|
| Wed 18 Nov | First session after NVDA FQ3 (AH: NVDA +4.0%, MU +3.5%, SKHY +4.3%); Korea session tests the move | AI cluster | [R:tech §5; R:修大哥 NVDA §5.4] |
| Thu 19 Nov | P&G Investor Day (single source) | PG, staples | [R:修大哥 §6] |
| Wed 25 Nov | Q3 GDP 2nd estimate | macro | [R:Peterson] |
| **Thu 3 Dec, close** | **AVGO margin-debit cure deadline** (§5) | AVGO | this ruling |
| **Fri 4 Dec** | **November payrolls** | all | [R:Peterson] |
| **Wed 9 Dec** | **FOMC decision 2 pm ET** (Peterson ~75% hike) · **AVGO FQ4 after the close** · MU capital-return step-up | all; AVGO; MU | [R:Peterson; R:修大哥 §6] |
| **Thu 10 Dec** | **November CPI** | all | [R:Peterson] |
| Tue 15 Dec | November PPI | macro | [R:Peterson] |
| **~Wed 16 Dec (unconfirmed)** | **MU FQ1 FY27** (guide $61.5bn ± $1.5bn) | MU, SK hynix, memory | [R:Peterson; R:修大哥 §6] (third-party estimate; 𢦀鳩仔 cites 15 Dec) |
| 24–31 Dec | SK hynix 2027 China tool licence (Wuxi/Dalian) due; not yet issued | SKHY / 000660 | [R:修大哥 §3.3] |
| 20 Jan 2027 | AAPL trim deadline (16 Nov A-5) | AAPL | 16 Nov ruling |
| Late Jan 2027 | SK hynix 4Q26 results; ₩20tn buyback ends 28 Jan; AAPL FQ1-27 | SKHY, AAPL | 16 Nov ruling |

### 6.2 Blackout rules (binding on Zac and 死潘狗)

| # | Rule | Window |
|---|---|---|
| **E-1** | **Macro blackout — all sleeves.** No new position and no add in any risk asset (equities, ETFs, options) | **open of Fri 4 Dec → close of Thu 10 Dec** (payrolls, FOMC, CPI) |
| **E-2** | **AI-cluster blackout.** No new position or add in any Tier A/B name (§4.3) | **open of Fri 4 Dec → close of the first full session after MU's FQ1 report** (~17 Dec). If MU's date is still unconfirmed on 9 Dec, the window runs to the close of the second session after the actual report |
| **E-3** | **Own-earnings blackout.** No initiation or add in a name in the 5 sessions before its earnings, on the report day, or before the close of the first full session after | every name; for MU this begins ~9 Dec, already inside E-2 |
| **E-4** | **Gap rule.** No entry in a session where the name opened > 1 ATR from the prior close (MU: > 8.2%); wait for a close. Limit orders only; no market orders at the open | always |
| **E-5** | **SK hynix blackout** (16 Nov B-6): from 24 Dec until a 2027 Wuxi licence is reported or refused; and the 5 sessions before 4Q26 results | SKHY / 000660 |
| **E-6** | **Risk reduction is never blacked out.** Stops are honoured; trims, exits and limit cures (the AVGO debit) are permitted at any time | always |
| **E-7** | **The NVDA gap does not qualify.** No AI-cluster entry on 18 Nov on the after-hours move; 修大哥's confirmation tests (NVDA holds > $155.46, SMH reclaims ~$540, MU > $827.58) need 2–3 sessions | 18–20 Nov at minimum |

**Practical effect for the Owner.** Even if every other gate opened, the windows in which a **new AI/semis position** could be placed this year are roughly **21 Nov – 3 Dec** and **after ~17 Dec** (until 24 Dec for SK hynix). For **defensives**, everything except **4–10 Dec**. This is why the T-path for MU (§1.6) is written to work in either window.

## 7. Limit-by-limit check

**MU — hypothetical post-trade at the maximum legal size** (4.0% of LNW, entry $712.42, close-basis stop $650, tail $536.25). LNW and holdings are undisclosed, so ratio limits are shown per % of LNW.

| # | Limit [C] | Value | Current | MU post-trade (4.0%, hypothetical) | Pass / Fail |
|---|---|---|---|---|---|
| 1 | `max_single_position` (at cost) | 0.10 | MU 0% | 4.0% (memory cluster total ≤ 5%) | PASS (hypothetical) |
| 2 | `max_single_position_drifted` | 0.15 | — | n/a | n/a |
| 3 | `max_sector` (Info Tech) | 0.35 | AAPL (size undisclosed, cap 6.4%) + AVGO 2 sh | +4.0% | **NOT COMPUTABLE** |
| 4 | `max_correlated_cluster` (AI complex) | 0.40 | AVGO only known | +4.0%; CRO band 20% | **NOT COMPUTABLE** |
| 5 | `cash_floor` | 0.10 | `cash_balance: 0.00` placeholder | −4.0% of cash | **NOT COMPUTABLE** |
| 6 | `leverage` | none | **Webull margin, USD −$12.06** | must be a cash purchase | **FAIL on face (Webull)** → §5 |
| 7 | `max_var_95_1d` | 0.03 | portfolio undefined | name VaR 10.7% × 4.0% = **0.43% of LNW** [D] | PASS (name) · portfolio NOT COMPUTABLE |
| 8 | `max_drawdown` budget | 0.20 | no series | stop tail 0.99%; held through to $351: 2.0%; to bear $168: 3.1% of LNW [D] | PASS at ≤ 4.0% |
| 9 | `max_risk_per_trade` | 0.01 | — | tail 24.7% × 4.0% = **0.99%**; naive 8.8% basis would allow 11.4% | **PASS at ≤ 4.0% ($650 stop) / ≤ 3.2% ($598) · FAIL above** |
| 10 | `stop_required` | true | levels from a CEO stand-in; **no 老詹 sign-off** | — | **FAIL** |
| 11 | `max_adv_participation` | 0.05 | not run (Tim Cook) | MU market value ~$789.5bn [R:𢦀鳩仔 §2.1]; a retail order cannot approach 5% of ADV | PASS on inference |
| 12 | options limits | covered only; no naked shorts | none | cash-secured/naked puts on MU not proposed and **not permitted** as a back door to entry | n/a |
| 13 | `committee_approval_required` | true | not convened | — | **FAIL** |
| 14 | `decision_record_before_ticket` | true | none | — | **FAIL** |
| 15 | `live_trading` | forbidden | no agent orders | — | PASS |

**Result:** MU fails #6, #10, #13 and #14 today, and is vetoed on the §1.2 grounds in addition. **SKHY/000660:** the 16 Nov table stands, with #9 at **cap zero** (premium unmeasured) and #10 failed (trend-repair void, no KRW stop). **AVGO (held):** #6 FAIL; #10 FAIL (no stop); #14 FAIL (no record); #1 PASS for any LNW ≥ ~$6,900 [D: 689.74 ÷ 0.10].

**Risk scores to the committee:** MU initiation **42** · SKHY ADS re-entry **25** · 000660.KS **40** · AAPL hold 57 (16 Nov, unchanged). No score is given for KO/PG/XLP: no pipeline has run on them.

## 8. Conditions (binding), escalations, NOT OBTAINED, Owner disclosures

### 8.1 Binding conditions (on Zac and 死潘狗; every entry is a recommendation the Owner executes himself)

| # | Condition | Owner verifies by |
|---|---|---|
| **M-1** | **MU initiation at ~$700–737 VETOED**, every account, every size | no MU buy ticket |
| **M-2** | Any future MU size = min[1% ÷ (1 − stop × 0.825 / entry), 10%], combined with memory (C-1). Close-basis stop from 老詹; next-open exit; never lowered. **If the Owner will not commit to the stop: cap = 1% ÷ (1 − 351/entry)** (1.9% at $737) | the formula on the ticket |
| **M-3** | **T-path only** for a trade: daily close > $827.58 (preferably after a higher low above $650) + 老詹 stop + committee approval as a trade, with 𢦀鳩仔's dissent recorded + decision record with a 30-session time stop (no close > $990 → exit) + outside E-1/E-2 + cash account + LNW disclosed | committee minutes; decision record |
| **M-4** | **V-path**: committee at ≤ $350; entry ≤ $210; CRO re-score at that time | valuation note + re-score |
| **M-5** | No knife-catching at $650/$598; no entry on the 18 Nov gap; no naked or cash-secured puts as a back-door entry; no averaging down through a stop | no such ticket |
| **H-1** | **SKHY ADS and 000660.KS re-entry: VETO STANDS** (16 Nov), re-scored ADS 25 / ordinary 40 | no ticket |
| **H-2** | ADS cap formula **unchanged**: min[1% ÷ (1 − 1/(1+p)), stop-tail cap, 5.0%, 10%]; **p unmeasured → 0**; weekly premium monitor if held | dated premium on the ticket |
| **H-3** | Watchlist annotation: "two-way conversion within the cap since 29 Jul reported (UNVERIFIED)". The dictator to confirm from a primary KSD/depositary source | watchlist edit by 腦大裝草 / CIO |
| **H-4** | The "$122.20 higher low" trend-repair condition is **void**; 老詹 restates it from the post-$117.40 base (KRW for the ordinary). R2 = **₩856,000** | technical note |
| **C-1** | **Memory = one name.** MU + SKHY + 000660: Σ size × tail ≤ 1% of LNW **and** ≤ 5.0% of LNW at market. Priority if gates open: 000660 → ADS → MU | position table |
| **A-1** | **AI-complex cluster** per §4.3 (Tier A + B at 100%; QQQ/XLK 100% until look-through; AAPL outside). **CRO band ≤ 20% of LNW**; hard limit 40% | cluster sum in `config/portfolio.yaml` |
| **P-1** | **Cash + T-bills ≤ 1 yr ≥ 30% of LNW** through ~17 Dec (hard floor 10%) | account statements |
| **S-1–S-5** | Defensives: ≥ 3 tranches, tranche 1 ≤ ⅓; close-basis stop per single name; size by the stop-tail formula with a computed worst day; sector ≤ 35%; **pipeline + committee first** (KO/PG/XLP have none) | committee minutes; tickets |
| **G-1** | **Webull USD debit cured by the close of 3 Dec 2026** (deposit/convert, sell 1 AVGO, or sell both); margin disabled or account converted to cash | Webull statement: USD ≥ 0; account class |
| **G-2** | AVGO hold: ≤ 6.6% of LNW through 9 Dec; 老詹 stop before 9 Dec; retrospective decision record; no adds. Not cured by 3 Dec → recommendation to sell before 9 Dec | statement; record |
| **G-3** | No new position in the Webull account while it is a margin account with a debit (including KRW "buying power") | — |
| **E-1–E-7** | Blackouts per §6.2: macro 4–10 Dec (all sleeves); AI cluster 4 Dec → first full session after MU's print; own-earnings 5 sessions before; gap rule; SK hynix 24 Dec → Wuxi; **risk reduction never blacked out** | calendar |
| **R-1** | Before any memory ticket: **Mo Peter** (VaR on the sized position and on the cluster) and **Mario** (stress: memory down-cycle −50%; Taiwan; FOMC hike + 10y 5.40%) filed in `reports/risk/` | the two files |

### 8.2 Escalations to the CEO and the Owner (made by this report)

1. **Webull margin debit — `leverage: none` breach on its face, second escalation, uncured since 13 Nov.** Deadline 3 Dec (G-1).
2. **`config/portfolio.yaml` empty — tenth escalation.** I cannot certify the KPI "portfolio inside all limits at all times" and do not report it.
3. **0.40-vs-0.50 cluster/target contradiction — tenth time of asking.**
4. **ETF-as-"name" ambiguity** — conservative reading applied (each ETF line ≤ 10%) pending the Owner's ruling.
5. **Technical inputs are a CEO stand-in without 老詹 sign-off** for MU, SKHY and the defensives. Every stop in this report is provisional until he confirms.

### 8.3 Proposed config changes (NOT applied; the Owner's approval required)

- (a) the `instrument:` block of 12 Nov (`max_basis_premium`, `measure_at: look_through`, `premium_monitor`);
- (b) `per_trade.stop_type: close | intraday`;
- (c) `per_trade.gap_allowance: worst_day` — formalising risk at stop = stop × (1 − one-year worst day);
- (d) a country/FX line for non-USD single names (line proposed, number left to the Owner);
- (e) **new:** `clusters: ai_complex:` listing Tier A/B members and the look-through rule of §4.3, so the cluster is defined in the law, not in my reports;
- (f) **new:** `cash_equivalents:` (T-bills ≤ 1 yr, government money funds);
- (g) **new:** `events: blackout_macro_days` and `blackout_earnings_sessions: 5`, making §6 structural.

### 8.4 Sources read (all on disk, 17 Nov unless stated)

`config/risk-limits.yaml`, `config/portfolio.yaml`, `config/watchlist.yaml`, `config/portfolio-webull-snapshot-2026-11-13.yaml` · `reports/risk/2026-11-16-aapl-and-skhy-reentry-cro.md`, `reports/risk/2026-07-18-mu-risk-review.md`, `reports/risk/2026-11-12-skhy-cro-review.md` (formula sections) · `reports/equity/2026-11-17-mu-valuation-refresh-vs-skhy.md` (𢦀鳩仔) · `reports/macro/2026-11-17-market-regime-tech-vs-defensive.md` (Peterson) · `reports/news/2026-11-17-mu-skhy-semis-staples-news.md` and `reports/news/2026-11-17-nvda-earnings.md` (修大哥) · `reports/technical/2026-11-17-mu-skhy-defensives-technical.md` (CEO for 老詹, unaudited) · `reports/committee/2026-11-16-aapl-ceo-summary.md`.

### 8.5 NOT OBTAINED

1. **Owner's liquid net worth**; all holdings and brokers; account types — the denominator for every cap here. `config/portfolio.yaml` empty.
2. **老詹's sign-off** on any level in this report (MU $650/$598/$827.58; SKHY structure; KO/PG MA50 levels).
3. **Mo Peter VaR and Mario stress** — not commissioned (this session cannot dispatch agents); my scenarios substitute.
4. **MU FQ1 FY27 date** — ~16 Dec (third-party estimate; 𢦀鳩仔 cites 15 Dec); not company-confirmed.
5. **MU earnings-day reaction history** (the −17.5% worst day was 5 Nov, a macro day, not an earnings day).
6. **000660.KS closes 13–17 Nov, a dated USD/KRW, and therefore any admissible ADS premium.**
7. **Primary confirmation of two-way KSD conversion within the cap** (search-relayed July Korean outlets only).
8. **KRX access** at any of the Owner's brokers, and whether that account is cash.
9. **KO / PG / XLP one-year worst day**, valuation and any pipeline; none are on the watchlist.
10. **AI-name look-through weights** in QQQ, XLK, SPY, RSP.
11. **AVGO** volatility, ATR, a dated worst day from primary bars (the −15% is single-source, date not pinned); a 老詹 stop; whether the Webull HKD side nets the USD debit and whether interest accrues.
12. **NVDA SEC civil-probe scope** (WSJ via Axios; not read directly).
13. **Regular-session confirmation** of the NVDA after-hours move (18 Nov) and the 18 Nov Korea session.
14. A mid-November CME FedWatch reading (latest secondary: ~80% on 9 Nov; "~90%" relayed ~13 Nov).

### 8.6 What the Owner must disclose or decide

1. **Liquid net worth** (or at least the total of all brokerage accounts). Below ~$18,400, one MU share at $737 exceeds the 4.0% cap; below ~$7,400 it exceeds 10% [D].
2. **Every holding and broker**: AAPL share count; where the SKHY sale proceeds sit; 3416.HK; 6160.HK; any QQQ/SPY/XLK (look-through for the cluster).
3. **Cash or margin for each account.** Cure the Webull USD −$12.06 by 3 Dec, and disable margin.
4. **KRX access** in a cash account — this decides whether 000660.KS, the cleanest memory instrument, is available at all.
5. **Does the Owner want memory exposure, and in which form?** The T-path (a trend trade, stop-bound, committee-approved) or the V-path (value, ≤ $350/≤ $210). Will he commit to a close-basis stop? If not, MU's cap is 1.9%, not 3.6–4.0%.
6. **AVGO thesis** in his own words, for the retrospective decision record.
7. **Rulings on the ambiguities in §4.5**: the 0.40-vs-0.50 conflict; ETF lines as "names"; T-bills as cash.
8. **Any override of the MU or SK hynix vetoes must be in writing.** I log dissent, and the sizing conditions above still bind.

---

*John, Chief Risk Officer. This is research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places, modifies or cancels orders; every entry, trim or sale above is a recommendation for the Owner to execute himself.*
