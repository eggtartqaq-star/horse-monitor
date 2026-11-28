# Stress test: B′ vs A at maximum exposure, three commissioned scenarios plus a reverse stress (gate B-7)

**Author:** Mario, Stress Testing Analyst (Dept 6) · **For:** John (CRO) · **Date:** 2026-11-27
**Commission:** CRO ruling `reports/risk/2026-11-24-swing-notional-cap-cro.md` §5, lines 271–276. Gate B-7 is in `reports/risk/2026-11-24-v66-release-cro-signoff.md`, lines 280 and 387.
**Code used:** `strategy/v6.6/` V6.6.9, fingerprint `2b7b62182068`. It was imported and never modified. No run wrote to `strategy/v6.6/results/`.
**Data:** Webull read-only daily bars in `strategy/v6.6/data/*.csv`: 38 names plus SPY, 2022-02-11 to 2026-11-23.
**Status:** research input for the CRO's B-7 read. It is not a decision; John and the committee act on it.

**Tags:**
- **[C]** a cited file;
- **[D]** my run, or my arithmetic on cited inputs;
- **[A]** an assumption;
- **[E]** an estimate.

**Units:**
- Every percentage is of the HK$10,000 sizing base, which is US$1,282.05 at 7.8 (`owner_settings.json` `account_hkd`; `config_v66.py:27`) [C].
- 1R = the 1% risk budget = US$12.82 (`config_v66.py:26`) [C].

> **Severity bias, stated up front.** I chose severe settings throughout. Where the CRO's stop conditions S1–S4 are meant, I write "stop condition S1"; my scenarios are named Sc1–Sc3.
> - The headline figures use the **worst-path** framing. The position has already slid to just above its stop before the gap.
> - Gap fills carry a **2% liquidity haircut** below the open [A].
> - Every pair moves with **correlation 1**.
> - Recovery times use the **10%-cap** backtest return, not B′'s.
> - The "fresh-entry" framing (the convention in the CRO's §3.3 table) is shown beside the headline, so the two can be compared.

---

## 0. Verdict

**B-7, Mario's part: DELIVERED.**

**On stress, B′ passes all three commissioned scenarios on the exposure its rules can actually reach.** Two of them pass with thin headroom to the −10% monthly breaker (0.6–1.2pp at worst). B′ fails one test: the literal Sc3, two 15% shares in the highest-beta cluster (MSTR+COIN). **That book cannot be built under B′'s own rules.** B′ adds tail risk in exactly one place: **two exception shares from the same correlated cluster.** That is the kill scenario (§2).

| Scenario | A (10% flat): one-night loss | B′: one-night loss | Worst B′ position (× the 1R budget) | Headroom to the −10% breaker (B′) | Verdict A / B′ |
|---|---|---|---|---|---|
| **Sc1** 2024-08-02 and 08-05 replay, lab B′ path (2 slots, both entry rules, 60 start shifts) | −0.86% realized (−0.79% mark-to-market) | −0.86% realized (−0.97% mark-to-market) | BAC E1 −0.56% (0.6R) | 9.0pp | **PASS / PASS** |
| **Sc1** at maximum exposure (every name at its maximum size, loosest legal stop) | −3.70% (broker stop) / −3.67% (manual close-basis) | −3.70% (broker stop) / **−5.07%** (manual close-basis) | AMZN 1 share: −1.35% (1.35R) with a broker stop; **−2.33% (2.3R) manual: stop condition S1 fires** | 4.9pp | **PASS / PASS** |
| **Sc2** −40% single-name gap [A] | −4.0% fresh; −4.7% worst-path | −6.0% fresh; **−6.8% worst-path**; −9.4% if the other slot also gaps −10% [A] | the exception share, 6.8R; stop condition S1 fires | 3.2pp (0.6pp with the sympathy gap) | **PASS / PASS (marginal)** |
| **Sc3** −10% index gap [A], both slots in one sector. Highest-beta GICS pair that B′ can reach: NVDA+AMD (semis) | −6.4% base beta / −6.6% severe beta | **−8.8% / −9.1%** | NVDA 15%: −4.9% (4.9R) | 0.9–1.2pp | **PASS / PASS (marginal)** |
| **Sc3 as literally specified.** Highest-beta pair in the data: MSTR+COIN (crypto cluster), each at its cap | −7.3% base / **−10.4% severe** | −10.3% / −15.0% at 15% + 15%. **Not reachable under B′:** at reachable weights, B′ = A | 5.2R–8.4R (hypothetical) | breached | **PASS (FAIL on severe beta) / FAIL, unreachable** |
| **Reverse.** The single-night two-name gap that uses up the whole breaker | 43.3% on each name | **27.1% on each name** (2 × 15%) | — | — | Not reached in sample: worst single gap −27.4% (MSTR, 2024-08-05) |

**Everything above holds only if `account_hkd` ≤ real equity (C-7).**
- The signoff (§5.4, line 261) puts the Webull account's equity on 13 Nov at about HK$5,302.09; whether the swing system trades there is unconfirmed.
- If that is the real base, multiply every loss by 1.886 [D].
- **Sc2 for B′ then becomes −12.8%, a breaker FAIL in one night**, and the reverse-stress threshold falls to a 10.0% two-name gap.

**Recommendation to the CRO.**
1. Close B-7's stress item as delivered.
2. On stress grounds, B′ is acceptable on the backtest path, under the existing gates plus four conditions:
   - **M-1, zero cost, structural:** C-7 is cured *before* B′.
   - **M-2, zero cost:** a broker stop (C-9) on every position is a **precondition** for B′. Close-basis manual stops are not acceptable under B′.
   - **M-3, costs 0.00–0.34pp CAGR on the base path:** at most **one exception-tier share in the AI complex** at a time.
   - **M-4, monitoring only:** the shadow ledger records the drifted notional of each exception share.
3. Not recommended:
   - index puts (not feasible at this account size);
   - a 12.5% exception ceiling (it removes B′'s benefit);
   - a flat "one exception at a time" rule (it costs more than M-3 and worsens drawdown on the limit-entry path).
4. **If you want no scenario inside 2pp of the breaker, keep A.** On the base path that costs 1.45pp CAGR (as_traded) or 0.95pp (live limit entry) [D].

---

## 1. Kill scenario analysis

**Kill scenario: an AI-complex derating gap that hits a full B′ book.**
- **The setup.** Both slots hold exception shares from the AI complex, at up to 15% each. On a down day both close just above their stops. Then an overnight sector shock (export control, a Taiwan-strait event or an earnings cascade) gaps both names together.

**Why this is the one that matters:**
- **It is the only configuration in which B′ carries materially more tail than A.** In every other configuration at least one slot is A-tier (≤ 10%), or B′ cannot hold the names at all (§3.3).
- **The B′ path has already reached it.** On the as_traded backtest path, B′ held **AAPL + GOOGL**, both exception shares and both AI complex, for **36 nights (2024-05-17 to 2024-07-10)**, at 14.71% + 12.27% at cost [D].
  - AAPL then drifted to a peak of **18.13%** on 2024-07-16 [D]. That matches Mo Peter's largest single-position value: 18.13%, `2026-11-27-bprime-var.md`:96 [C].
  - Mo Peter puts gross exposure at its peak of 32.27% on 2024-07-09 [C].
  - No large gap arrived while the pair was held.
- **Same structure as Mo Peter's regime warning.** His current-volatility check fails only for semiconductor-linked pairs [C, var report line 490].

**What it costs (worst path, 2% liquidity haircut, both names gapping by the same amount) [D]:**

| Two-name overnight gap | B′, 15% + 15% | B′ with M-3 (15% + 10%) | A, 10% + 10% | B′ if the base is HK$5,302 (C-7 fails) | Time to recover, B′ / A [E] |
|---|---|---|---|---|---|
| −20% | 8.05% | 6.97% | 5.89% | 15.2% | 3.8–5.1 y / 2.8–3.7 y |
| **−27.1%** | **10.00%: breaker used up** | 8.57% | 7.14% | 18.9% | 4.8–6.4 y / 3.4–4.5 y |
| −30% | **10.79%: FAIL** | 9.22% | 7.65% | 20.4% | 5.2–7.0 y / 3.6–4.9 y |
| −40% (my library's "AI derating −40%") | **13.54%: FAIL** | **11.48%: FAIL** | 9.42% | 25.5% | 6.7–8.9 y / 4.5–6.0 y |

Arithmetic, per name: loss = r + (E − r) × [1 − (1 − g)(1 − h)].
- r = 1%, E = 15%, h = 2%.
- At g = 30%: 1% + 14% × (1 − 0.70 × 0.98) = 1% + 14% × 0.314 = 5.40%. Two names: 10.79%.

**How plausible is it?**
- **In sample: never.**
  - In the 3,356 name-days on which a name qualified for the exception tier, the worst next-day gap was −7.67% (GOOGL, 2023-10-24) [D].
  - No gap ≤ −28.6% occurred in any name in 37,962 name-days. That reproduces the CRO census: worst gap −27.4%, worst pair −24.06%, on 2024-08-05 [D/C].
- **Why the sample understates it:**
  - The sample is survivor-selected (F-01).
  - On 2024-08-05 NVDA gapped 3.55 times SPY's gap and AAPL 2.38 times [D]. Scaled to a −10% index gap, that is −35.5% and −23.8%.
  - A "can't happen" gap is the one to model.

**What blunts it, in order of cost per unit of protection:**
1. **M-3:** at most one exception share in the AI complex. It raises the breaker-exhausting gap from 27.1% to 33.5%. Cost: 0.00pp (live limit entry) to 0.34pp (as_traded) of CAGR on the base path (§5).
2. **M-1 (C-7 cure):** costs nothing. It prevents the 1.886× amplifier, which by itself turns a −10% two-name gap into a breaker breach.
3. **Keep A:** threshold 43.3%. Cost: 0.95–1.45pp CAGR.

**Coordination gap, disclosed.** LeBron James's geopolitical scenario set (Taiwan strait) was not available in this session. The −20% to −40% AI-complex gaps above stand in for it and should be reconciled with his set before the committee reads this.

---

## 2. Scenario results

### 2.1 Method

**Harness.** No file under `strategy/v6.6/` was changed.
- A scratch module imports the shipped `lab.py` and `sizing_v66.py`.
- It replaces `rules_v642.position_plan` **in memory only** with a wrapper that calls the shipped `sizing_v66.size(entry, stop, engine, mode)`. The engine is read from the caller's signal dict.
- **Parity:** in mode A the wrapper reproduces the shipped lab exactly.
  - Trade hash `3044c31236e877f0` (137 trades), the same as `results/baseline.json` `bt` [C].
  - The same holds under the limit entry rule (`5ce22d24b99c6438`, 132 trades), with identical equity curves [D].
- **B′ check:** in mode B′ it reproduces the CRO's B′ figures exactly (ruling line 166): CAGR 3.66 / 2.31 / 5.09, max DD −4.20, worst trade −0.84 [C/D].

**Stop handling in the lab (verified).** A gap through the stop fills at the open, which is worse than the stop:
- E2 always: `lab.py:327`, `px = o if o < p.stop else p.stop`.
- E1 when `e1_gap_fill=True`, which is the as_traded default: `lab.py:104` and `lab.py:318` [C].

The lab triggers stops on the intraday low, which is equivalent to a resting broker stop. **It does not model a close-basis manual stop.** I added two such mechanics. So every position is run under three exit mechanics [D]:
1. **Broker stop:** fill at min(open, stop) once the low ≤ stop. This is the lab's rule and C-9.
2. **Manual, close-basis, sold at the close:** exit at the close of the first day that closes ≤ stop.
3. **Manual, close-basis, sold at the next open:** the Owner sees the close below the stop after the US close and sells at the next open. In a two-night event this is the cascade case.

**Two loss framings for the hypothetical scenarios [D]:**
- **Fresh entry:** the prior close equals the entry; loss = E × g. This is the CRO §3.3 convention.
- **Worst path:** the position has already slid to just above its stop on a close basis, so its planned risk r is gone; then the gap g runs from the stop. Loss = r + (E − r) × [1 − (1 − g)(1 − h)], with h = 2% [A].
  - The headline uses this framing.
  - It is the Aug-2024 shape: a down day, then a gap.

**What the −10% breaker can and cannot do.**
- It is **month-to-date realized** P&L. The code is `lab.py:305` and `lab.py:451`; the manual rule is C-10 (signoff line 375); scanner enforcement is B-6 (line 386) [C].
- It only blocks *new entries afterwards*. It cannot cap a one-night loss.
- "PASS" therefore means **the night's loss alone, in a month that started flat, does not use up the month's −10% budget.**
- Losses on positions the gap did not stop out are mark-to-market only, and the breaker does not see them.
- Correction to the brief: the −10% breaker is **not** in `config/risk-limits.yaml`. It is `MONTH_BREAKER_PCT = 10.0` (`config_v66.py:29`) plus C-10 [C].

**Recovery time [E]:** T = ln(1/(1 − L)) / ln(1 + CAGR). The CAGR is A's backtest-path figure:
- 2.21% (`results/baseline.json`, 2.2056);
- to 1.65% (A with the live limit-entry rule; my run, `costs.csv`).

This is not a forecast. The CRO ruled that higher-cap CAGRs must not be quoted as expectations (ruling line 223).

### 2.2 Sc1: replay of 2024-08-02 and 2024-08-05 at maximum B′ exposure

**The bars [D, from `data/*.csv`].** "Price" is the 08-01 close in actual shares: split-unadjusted with the lab's `SPLITS`, but still dividend-adjusted (§6).

| Name | Gap 08-02 | Gap 08-05 | Price 08-01 | Status under the caps on 08-01 |
|---|---|---|---|---|
| MSTR | −1.72% | **−27.37%** | US$1,511.81 | 1 share = 117.9% of account: blocked under A and B′ |
| COIN | +0.23% | **−20.75%** | US$212.64 | 1 share = 16.6% > 15%: blocked under A and B′ |
| INTC | **−24.48%** | −5.96% | US$28.87 | A-tier (multi-share ≤ 10%) |
| AMZN | −9.41% | −8.15% | US$184.07 | B′ exception band (1 share = 14.36%) |
| NVDA | −4.99% | −14.18% | US$108.91 | A-tier (1 share = 8.49%) |
| AVGO | −3.47% | −9.88% | US$144.04 | B′ band (11.24%) |
| GOOGL | −2.53% | −6.70% | US$169.34 | B′ band (13.21%) |
| SHOP / PLTR | −6.12% / −5.10% | −10.74% / −12.13% | US$58.17 / US$26.08 | A-tier |
| SPY | −1.34% | −3.99% | — | — |

**(a) The lab's B′ simulation holds positions in this window, but none in the exception tier.**
- **Setup:** backtest path (live), 2 slots. Two entry rules: as_traded (1% deviation) and the live limit rule. **60 start shifts.**
- **The book:**
  - Every run, for A and for B′, holds the same two positions into the 08-02 open: **BAC E1, 3 shares (8.99% at entry), and PFE E2, 4 shares (8.10%).**
  - BAC gapped through its stop on 08-02: −0.56%.
  - PFE gapped through its trailing stop on 08-05: −0.30% under as_traded, −0.45% under the limit rule [D].
- **Losses:**
  - Realized loss for August to 08-05: **−0.86%** (as_traded) / −1.01% (limit), the same for A and B′.
  - Mark-to-market from the 08-01 close to the 08-05 close: A −0.79%, B′ −0.97%. B′'s extra −0.18pp is a JNJ share bought at the 08-05 open, an intraday loss rather than a gap.
- Gross exposure was 17%, far below the B′ maximum, so I built the book outward in (b) and (c).

**(b) Which positions could B′ have held under the rules?**
- **Method:** every backtest-path signal from 2024-04-15 to 08-02, entered independently at the next open (both entry rules), sized by `sizing_v66.size`, and managed by a replica of `lab.manage()`. The replica's broker-stop exits match the lab's to the cent [D].
- **Held into the event:** SHOP E1 (several signals, 1–2 shares, ≤ 9.61%), UBER E1, BAC E1, PFE E2 (4 shares) and **JNJ E2, the only exception share (1 share, 11.7%)**.
- **JNJ gained** through the event: +0.09% / +0.11%.
- **Worst rule-feasible pair, identical under A and B′:**
  - SHOP + UBER, **−1.96%** with broker stops;
  - BAC + SHOP, **−3.10%** under manual close-basis selling at the next open (SHOP −2.03% = 2.0R, because it is caught by both gaps).
- Under the limit rule: PFE + SHOP, −1.66% (broker stop).

**(c) Maximum-exposure construction, the commissioned case [D].**
- **Why a construction was needed.** On 08-01 the E2 3×ATR stops were too wide for most B′-band names: the 1-share risk exceeded US$12.82, so `size()` blocks them. Only GOOGL, CVX and JNJ qualified.
- **The construction removes that protection:**
  - Every name is held at the largest size its cap allows (A: ⌊US$128.21 / price⌋ shares; B′: that, or else 1 share if the price ≤ US$192.31).
  - Each has the **loosest legal stop**: risk exactly US$12.82, capped at the 12% E2 maximum.
  - Entry is at the 08-01 close (facing both gaps) or the 08-02 close (facing 08-05 only).
  - This is equivalent to positions opened earlier, when volatility was lower, and still held.

| Exit mechanic | A: worst pair (gross) | B′: worst pair (gross) | B′: worst pair of two exception shares | Worst exception share |
|---|---|---|---|---|
| Broker stop | INTC + SHOP **−3.70%** (18.1%) | INTC + SHOP **−3.70%**; AMZN + INTC −3.56% (23.4%) | AMZN + AVGO −2.68% (25.6%) | AMZN −1.35% (1.35R) |
| Manual, sold at the close | INTC + SHOP −3.27% | AMZN + INTC −3.61% | AMZN + GOOGL −2.15% (27.6%) | AMZN −1.26% |
| Manual, sold at the next open | INTC + SHOP −3.67% | **AMZN + INTC −5.07%** | AMZN + GOOGL −3.22% | **AMZN −2.33% (2.3R): stop condition S1 fires** |

**(d) The CRO's census pair cannot be held.**
- MSTR + COIN at 15% each, the ruling's "7.2% max" (line 143), **could not be held under A or B′**: both prices were above US$192.31 on 08-01 and 08-02 (COIN's 08-02 close was US$204.43) [D].
- So the CRO's 7.2% is a conservative bound, not a reachable loss.
- The reachable maximum is **3.6–3.7% with broker stops and 5.1% with manual close-basis stops.** I treat that pair as a cluster stress in Sc3.

**Limits:**
- Breaker: PASS (worst −5.07%).
- 15% drift: PASS (largest position before the gap 14.36%, AMZN).
- Cash floor: PASS (gross ≤ 27.6%; cash ≥ 72%).
- 20% drawdown: PASS.
- Time to recover: −3.70% takes 1.7–2.3 y; −5.07% takes 2.4–3.2 y [E].
- If C-7 fails: −5.07% × 1.886 = **−9.56%**, inside the breaker by 0.4pp.

**Verdict: Sc1 PASS for A and B′.** What B′ adds over A appears only under manual close-basis execution: −5.07% vs −3.67%, and an exception share that trips stop condition S1. → **M-2.**

### 2.3 Sc2: −40% single-name gap [A]

**Why −40%.**
- −40% is larger than any gap in the sample: the worst is −27.4% [C, ruling line 108].
- For names that qualify for the exception tier it is 5.2× the worst in-sample gap (−7.67%) [D].
- It stands for fraud, a halt, or a failed trial. The universe was selected in 2026, which hides the names that suffered such events (F-01).
- Maximum exposure: the A cap is 10% (US$128.21); the B′ exception share is 15% (US$192.31) [C].

| Book | Fresh | Worst path | Worst path + liquidity | × 1R | Other slot also gaps −10% [A], worst path + liquidity | Recovery time [E] | If C-7 fails (× 1.886) |
|---|---|---|---|---|---|---|---|
| A (10%) | 4.00% | 4.60% | **4.71%** | 4.0–4.7× | 6.77% | 2.2–2.9 y | 8.88% |
| B′ (15% share) | 6.00% | 6.60% | **6.77%** | **6.0–6.8×** | **9.42%** | 3.2–4.3 y (with the other slot: 4.5–6.0 y) | **12.76%: FAIL** |

Arithmetic, B′: 1% + 14% × (1 − 0.60 × 0.98) = 1% + 14% × 0.412 = 6.77%. Other slot: 1% + 14% × (1 − 0.90 × 0.98) = 2.65%.

**Drift.**
- Exception shares do drift above 15%: on the as_traded B′ path, 2 of 22 did (AAPL to a peak of 18.13%, CVX to 16.05%) [D]. A-tier positions never exceeded 11.9%.
- A −40% gap on the drifted AAPL share costs **7.25% mark-to-market** from the prior close.
- The realized loss against entry is only −3.83%. The gain cushion protects the breaker, which counts realized loss, but not the drawdown.

**Limits:**
- Breaker: PASS. Headroom is 3.2pp alone, or 0.6pp with the sympathy gap. With the sympathy gap, any month already at −1% realized fails.
- **Stop condition S1 fires** (the exception share loses more than 2.0%). The revert to A is automatic, as designed (ruling line 263).
- The 1R budget is exceeded 6.8× ex post; A is exceeded 4.7×. This is inherent in any gap, and the 1% rule is an ex-ante sizing rule.
- 15% drift: at entry exactly at the limit (zero headroom); breached by drift on 9% of exception trades.
- Cash floor and drawdown: PASS.

**Verdict: Sc2 PASS for A; PASS (marginal) for B′.** The marginal rating is because one more −10% name, or a month already at −1%, would exhaust the breaker.

### 2.4 Sc3: −10% index gap [A], both slots in one sector

**Size of the shock.** −10% is 2.5× the worst SPY overnight gap in the data: −3.99% on 2024-08-05; the next worst is −3.44% on 2025-04-03 [D].

**Sector mapping (mine, GICS-style, not fetched) [A]:**

| Group | Names |
|---|---|
| Semiconductors | NVDA, AVGO, AMD, QCOM, MU, INTC |
| Software | MSFT, CRM, ADBE, PLTR, SHOP |
| Hardware | AAPL |
| Communication services | GOOGL, META, NFLX |
| Consumer discretionary | AMZN, TSLA, NKE, SBUX, MCD |
| Consumer staples | COST, WMT |
| Financials | JPM, BAC, GS, V, MA |
| Health care | UNH, JNJ, PFE, LLY |
| Energy | XOM, CVX |
| Industrials | CAT, BA, UBER |
| **Crypto-linked cluster** | **MSTR** (GICS IT) and **COIN** (GICS Financials) |

The crypto pair is not a GICS sector. I treat it as a correlated cluster, as the firm's `max_correlated_cluster` does, and as the CRO did (§7.10).

**Betas to SPY [D].**
- Data: 1,199 daily observations.
- Measures:
  - close-to-close daily;
  - overnight gap (Open/prior Close − 1), the base measure;
  - "severe" = the larger of the base beta and the gap beta estimated only on the 67 nights SPY gapped ≤ −1%. That sample is small and the estimate is noisy.
- Highest same-group pairs, by close-to-close / gap beta:
  - **MSTR + COIN, 2.70 / 2.82;**
  - NVDA + AMD (semis), 2.19 / 2.27: **highest-beta GICS pair**;
  - PLTR + SHOP, 2.17 / 2.22;
  - AMD + MU, 2.11 / 2.22.

**Whether B′ can actually hold each pair at the exception tier.** Share of bull-regime days on which the name qualifies at the E2 3×ATR stop [D]:

| Name | 1-share exception tier | E2 stop > 12% (blocked) |
|---|---|---|
| MSTR | 0% | 98.8% |
| COIN | 0% | 99.8% |
| NVDA | 4.1% | — |
| AMD | 0.2% | — |
| QCOM | 27.8% | — |
| CVX | 81.5% | — |
| JNJ | 73.5% | — |

- **Why the exception tier is confined.** It needs a price ≥ US$128.21, 1-share risk ≤ US$12.82, and an E2 stop ≤ 12% (`sizing_v66.py:37–39`; `rules_v642` `MAX_STOP_PCT_TREND`) [C]. So it is structurally limited to names with ATR ≤ about 2.2–3.3% [D].
- **MSTR and COIN never qualified.** COIN was held only through E1, at ≤ 6.33% [D].

| Pair | Betas used (base / severe) | A, 10% + 10%: fresh / worst-path + liquidity | B′, 15% + 15%: fresh / worst-path + liquidity | Can B′ reach it? | Index gap that uses up the breaker (B′ / A, worst-path + liquidity) |
|---|---|---|---|---|---|
| MSTR + COIN | 2.84 & 2.79 / 5.17 & 3.92 | 5.64% / **7.33%**; severe 9.09% / **10.38%** | 8.46% / **10.29%**; severe 13.63% / **15.03%** | **No.** At reachable weights (E1, ≤ 10%) B′ = A | 9.6% / 15.4% |
| **NVDA + AMD** | 2.42 & 2.12 / 2.67 & 2.12 | 4.54% / **6.36%**; severe 4.79% / 6.59% | 6.81% / **8.79%**; severe 7.19% / **9.14%** | Yes, rarely (AMD's exception tier is on 0.2% of days); 15% + 10% is more typical | 11.9% / 19.1% |
| NVDA + QCOM (highest-beta pair with *both* names eligible for the exception) | 2.42 & 1.61 / 2.67 & 1.61 | 4.03% / 5.91% | 6.04% / **8.09%**; severe 8.43% | Yes | 13.5% / 21.5% |
| CVX + XOM (the only same-sector pair of exception shares held concurrently in the 99-slot superset run: 20 nights, March 2026; never on the 2-slot path) | 0.28 & 0.23 / 0.96 & 0.91 | 0.51% / 2.81% | 0.77% / 3.26%; severe 5.13% | Yes | not reachable by an index gap |

**Crisis-ratio sensitivity [D].** Scaling the 2024-08-05 gap ratios to a −10% index gap (NVDA 3.55× SPY, AMD 1.96×) gives NVDA + AMD at B′ 15% + 15% = **10.12% (FAIL)**; A = 7.22%.

**Limits:**
- Breaker: B′ passes on reachable pairs, with 0.9–1.9pp headroom, and fails only under the crisis-ratio sensitivity and on the unreachable MSTR + COIN.
- Worst position: NVDA, 4.9R. Stop condition S1 fires.
- 15% drift, cash floor and drawdown: PASS.
- Recovery time: NVDA + AMD severe, B′ 4.4–5.9 y / A 3.1–4.2 y [E].
- If C-7 fails: B′ 16.6–17.2%, a FAIL.

**Verdict: Sc3 PASS for A (FAIL on severe beta for the literal MSTR + COIN pair). PASS (marginal) for B′ on reachable exposure.**
- The literal 15% + 15% MSTR + COIN book **fails, but B′'s rules cannot build it**.
- The protection is structural: E2-only exception, 1-share risk ≤ 1%, E2 stop ≤ 12%. It holds only while those three conditions stay in code; selftest's V-2 B′ cases cover the first two.

### 2.5 Reverse stress: what single-night gap on a two-name book uses up the −10% breaker?

| Book | Month already at 0% | at −2% realized | at −4% realized | If C-7 fails (base HK$10,000 vs HK$5,302), month at 0% |
|---|---|---|---|---|
| **B′, 15% + 15%** | fresh 33.3% · worst path 28.6% · **+ liquidity 27.1%** | 26.7% · 21.4% · **19.8%** | 20.0% · 14.3% · 12.5% | fresh 17.7% · **worst path + liquidity 10.0%** |
| B′, 15% + 10% (M-3 or one exception) | 40.0% · 34.8% · **33.5%** | 32.0% · 26.1% · 24.6% | 24.0% · 17.4% · 15.7% | 21.2% · 12.6% |
| A, 10% + 10% | 50.0% · 44.4% · **43.3%** | 40.0% · 33.3% · 32.0% | 30.0% · 22.2% · 20.6% | 26.5% · 16.7% |

Arithmetic, worst path + liquidity, B′ 15 + 15, month at 0%:
- 2% + 28% × [1 − (1 − g)(0.98)] = 10% → 1 − (1 − g)(0.98) = 0.2857 → g = 27.1%.

In index terms (base gap betas), B′ uses up the breaker at a −11.9% index gap on NVDA + AMD and −13.5% on NVDA + QCOM.

**In sample [D]:**
- Gaps ≤ −28.6%: 0 single, 0 pairs.
- ≤ −21.4%: 3 single, 0 pairs.
- ≤ −20%: 4 single, 1 same-night pair (2024-08-05).
- The observed worst pair (−24.06% average) would use up B′'s budget **only in a month already at −2% realized, under the worst-path framing**, and B′ cannot hold that pair.

---

## 3. Limit breaches under stress (B′ book; A in brackets)

| Limit | Value [C] | Sc1 (maximum exposure) | Sc2 | Sc3 (reachable) | Kill (−30%) | Status |
|---|---|---|---|---|---|---|
| Monthly breaker, realized (`config_v66.py:29`, C-10) | −10% | −3.70% to −5.07% [−3.70%] | −6.77% (−9.42% with sympathy gap) [−4.71%] | −8.79% to −9.14% [−6.4% to −6.6%] | **−10.79%** [−7.65%] | **PASS / PASS / PASS (marginal) / FAIL** |
| Single position, drifted (`risk-limits.yaml` firm reference) | 15% | 14.36% before the gap | 15.00% at entry; drift to 18.13% observed | 15% | 15% | At the limit by design; **breached by drift on 9% of exception trades** (A: never, max 11.9%) |
| Risk per trade, ex ante (`risk-limits.yaml`, `config_v66.py:26`) | 1% | ≤ 1% | ≤ 1% | ≤ 1% | ≤ 1% | PASS ex ante |
| Same, realized, as a multiple of 1R | — | 1.35R (broker stop) / 2.33R (manual) [2.2R / 2.7R INTC] | **6.8R** [4.7R] | 4.9R [3.5R] | 5.4R [3.8R] | **Exceeded ex post in every scenario, both caps.** Inherent to gaps |
| Stop condition S1: exception share loses > 2.0% (ruling line 263) | 2.0% | fires only under manual close-basis stops | **fires** | **fires** | **fires** | Works as the revert trigger. It fires at a gap ≥ 7.1% (worst path) or ≥ 13.3% (fresh) [D] |
| Cash floor (`risk-limits.yaml`) | ≥ 10% | ≥ 72% | ≥ 70% | ≥ 70% | ≥ 70% | PASS (needs C-6: no margin) |
| Drawdown budget (`risk-limits.yaml`) | 20% | 5.1% | 9.4% | 9.1% | 10.8% (13.5% at −40%) | PASS. **Fails at −40% if C-7 fails (25.5%)** |
| Account base = real equity (C-7, signoff line 364) | base ≤ net liquidation value | — | — | — | — | **OPEN.** Every PASS above is conditional on it |

---

## 4. Hedging and trim options, with costs

**How the costs were measured:**
- Each cost is the change in the lab outcome on the backtest path, base path only, for the two entry rules [D, `costs.csv`].
- Path dispersion is large: the CRO's perturbations give P(B′ beats A in-sample) = 0.61 (ruling line 178). So read the costs as **indicative, single-path**.
- Worst trade is −0.84% to −0.97% in every variant.

| Option | What it blunts | CAGR ALL / IS / OOS, as_traded | CAGR ALL / IS / OOS, live limit entry | Max DD (as_traded / limit) | Cost vs B′ | Recommendation |
|---|---|---|---|---|---|---|
| B′ as ruled (reference) | — | 3.66 / 2.31 / 5.09 | 2.60 / 0.15 / 5.07 | −4.20 / −4.22 | — | — |
| **M-1: cure C-7 (base ≤ real equity)** | the 1.886× amplifier in every scenario | unchanged | unchanged | unchanged | **0** | **Required before B′** |
| **M-2: broker stop on every position from the fill, no close-basis manual stops** | the Sc1 cascade (B′ −5.07% → −3.56%; AMZN 2.33R → 1.35R; stop condition S1 not tripped) | unchanged (the lab already assumes it) | unchanged | unchanged | **0** | **Required before B′.** If the broker cannot hold a resting stop on the position (README line 18: no stop attached to the entry order), B′ should not be enabled |
| **M-3: at most one exception share in the AI complex** (my list: NVDA, AVGO, AMD, QCOM, MU, INTC, AAPL, MSFT, GOOGL, META, AMZN, PLTR) [A] | the kill scenario: threshold 27.1% → 33.5%. Would have blocked AAPL + GOOGL in May–Jul 2024 | 3.32 / 1.61 / 5.09 | 2.60 / 0.15 / 5.07 | −4.20 / −4.22 | **−0.34pp / 0.00pp** | **Recommended** |
| One exception share at a time (any sector) | as M-3, for every cluster | 3.06 / 1.58 / 4.55 | 1.87 / −0.78 / 4.47 | −4.20 / **−6.09** | −0.60 / −0.73pp; DD worse on the limit path | Not recommended (costs more than M-3, for little extra) |
| One position per sector, all positions | Sc3 same-sector form | 2.84 / 0.81 / 4.71 | 2.42 / 0.28 / 4.35 | −4.79 / −5.18 | −0.82 / −0.18pp; DD worse | Not recommended (does not stop cross-sector AI pairs) |
| AI complex: at most one position of any kind | kill and Sc3 | 2.96 / 0.53 / 5.46 | 2.54 / −0.09 / 5.19 | −4.68 / −4.71 | −0.70 / −0.06pp | Weaker than M-3 per unit of cost |
| Exception ceiling 12.5% instead of 15% | Sc2 single-name loss 6.8% → about 5.7% [D] | 2.21 / 0.18 / 4.18 | 1.96 / −0.01 / 3.86 | −4.59 / −4.20 | **−1.45 / −0.64pp** | Not recommended (as_traded return falls back to A's) |
| Keep A (no B′) | everything B′ adds: Sc2 6.8% → 4.7%; reverse threshold 27.1% → 43.3% | 2.21 / 1.82 / 2.62 | 1.65 / −0.08 / 3.47 | −4.49 / −4.79 | **−1.45 / −0.95pp** | The fallback if no thin margin is acceptable |
| Index or sector puts | Sc3, kill | — | — | — | — | **Not feasible.** One SPY contract = 100 × US$722.29 (2026-11-23 close in the data) = **US$72,229, 56× the account** and 188× the maximum B′ gross. The firm's premium cap (2% = US$25.64, `risk-limits.yaml`) cannot buy a proportional hedge. It needs an options account outside V6.6. C朗 may confirm |
| Exit exception shares before earnings | Sc2 (most extreme single-name gaps in the census were earnings nights, e.g. INTC and AMZN on 2024-08-02 [D]) | not costed: earnings dates not in data (NOT OBTAINED) | — | — | unknown | Test via the B-5 log first |

---

## 5. Assumption disclosure

1. **The stress is biased severe on purpose.**
   - The headline uses the worst-path framing, a 2% liquidity haircut and correlation 1.
   - Maximum exposure uses the loosest legal stop.
   - Recovery uses A's CAGR.
   - Fresh-entry figures are shown beside every headline so the bias is visible.
2. **Assumptions [A]:**
   - the −40% single-name gap;
   - the −10% index gap;
   - the −10% sympathy gap in Sc2;
   - the −20% to −40% AI-complex gaps (the kill scenario);
   - the 2% liquidity haircut on gap fills;
   - the sector mapping and the AI-complex list (mine, GICS-style, not fetched).
3. **Betas** come from Webull bars, 2022-02-11 to 2026-11-23 (1,199 daily observations).
   - The "severe" gap beta rests on 67 nights and is noisy.
   - Calm-period betas understate crisis betas. On 2024-08-05, NVDA's gap was 3.55× SPY's against a full-sample beta of 2.42 [D].
4. **Prices.**
   - The bars are split-adjusted and, by inference, dividend-adjusted. README line 264 warns not to compare prices with TradingView "because TradingView does not adjust for dividends" [C].
   - The lab restores splits only (`SPLITS`). So band membership for high-yield names (CVX, XOM, JNJ, JPM) is approximate: their actual prices were higher than shown.
   - Gap percentages are unaffected.
5. **Survivorship.** The 2026-chosen universe (F-01) hides the names that failed. That is why the −40% row exists.
6. **Coverage.**
   - The data cannot replay 2008, March 2020, the 2022 rate shock or the dot-com unwind: the bars start 2022-02-11 and the tradeable window starts 2022-11-30, after the MA200 warm-up.
   - **Those crises are not covered by this report.**
   - Earnings dates: NOT OBTAINED.
7. **Lab and harness.**
   - The lab's stop fill at the open (`lab.py:318`, `:327`) assumes the opening print is achievable; the 2% haircut covers the auction.
   - Lab costs are 10bp per side; my stress arithmetic excludes commissions.
   - The breaker in the lab and in C-10 counts realized P&L only.
   - The Sc1 superset treats any two concurrently valid signals as a holdable pair; it ignores which slot was free when.
8. **Not mine.**
   - VaR is Mo Peter's: `reports/risk/2026-11-27-bprime-var.md`, CONDITIONAL. It is consistent with this report on C-7 (his break-even equity is HK$7,268) and on the semiconductor cluster.
   - Geopolitical scenarios: LeBron James, not consulted (not available in this session).
9. **Account base.** HK$10,000 / 7.8 = US$1,282.05 [C].
   - If capital is HK$12,500 on a HK$10,000 base (the lab's C-7 note), losses as % of capital are ×0.8.
   - If real equity is HK$5,302.09, they are ×1.886.

## 6. Reproduction

Scratch directory: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/stress_bprime/`

| Script | What it does |
|---|---|
| `bphook.py` | in-memory B′ wrapper |
| `check_hook.py` | parity check |
| `bars.py` | event bars |
| `replay.py`, `peek.py` | Sc1 (a) |
| `s1_enum.py`, `s1_signals.py`, `s1_pairs.py` | Sc1 (b) |
| `s1_maxbook.py`, `s1_loosest.py` | Sc1 (c) |
| `s3_beta.py`, `s3_feas.py`, `s3_crypto.py` | Sc3 |
| `s_crisis.py` | crisis ratios and the exception-tier gap census |
| `calc.py` | Sc2, Sc3, reverse stress, recovery times |
| `costs.py` | option costs |

Outputs are the `*.csv` files beside the scripts.

## 7. For 腦大裝草 (5 lines)

```
2026-11-27 · Mario (Dept 6) · B′ stress for gate B-7 (CRO ruling 2026-11-24 §5): DELIVERED. Lab untouched (fp 2b7b62182068); B′ harness reproduces the CRO's B′ figures exactly.
Sc1 2024-08-02/05: lab B′ path = A (BAC+PFE, −0.86% realized); max-exposure −3.70% broker stops / −5.07% manual close-basis (AMZN share 2.3R, stop condition S1). MSTR+COIN could not be held (US$1,512 / US$213).
Sc2 −40% single name: A −4.7%, B′ −6.8% (6.8R; −9.4% with a −10% second slot). Sc3 −10% index, semis pair: A −6.6%, B′ −9.1%. MSTR+COIN at 15%+15% fails (−10.3%) but is unreachable under B′.
Reverse: a 2×15% B′ book uses up the −10% breaker at a 27.1% two-name gap (A: 43.3%); never seen in sample. Kill = two AI-complex exception shares (AAPL+GOOGL held 36 nights in 2024). C-7 failure ×1.886 flips Sc2 to FAIL.
Recommend: B′ acceptable on stress with M-1 C-7 cured, M-2 broker stops mandatory, M-3 ≤1 AI-complex exception share (cost 0–0.34pp CAGR), M-4 drift logging; else keep A (cost 0.95–1.45pp CAGR).
```

---

*Research and decision support only. This is not financial advice, and no agent of this firm places orders. Figures are from cited files or my runs on them, dated as above. Estimates and assumptions are tagged.*
