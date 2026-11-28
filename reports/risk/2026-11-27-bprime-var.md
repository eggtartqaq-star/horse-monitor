# VaR: 1-day VaR of the maximum-exposure B′ book against the 3% ceiling (gate B-7)

**Author:** Mo Peter, Value-at-Risk Analyst (Dept 6) · **For:** John (CRO); copy to Zac (position sizing) · **Date:** 2026-11-27
**Commission:** CRO ruling `reports/risk/2026-11-24-swing-notional-cap-cro.md` §5 (line 271). Gate B-7 is in `reports/risk/2026-11-24-v66-release-cro-signoff.md` (lines 280 and 387).
**Code used:** `strategy/v6.6/` V6.6.9, fingerprint `2b7b62182068`. It was imported, never modified.
**Data:** Webull read-only daily bars, `strategy/v6.6/data/*.csv`, 38 names + SPY/QQQ. Last stock bar: 2026-11-23.
**Status:** research input for the CRO's B-7 read. This is not a decision. John and the committee act on it.

**Tags used below:**
- **[C]** a cited file;
- **[D]** my run or my arithmetic on cited inputs;
- **[A]** an assumption;
- **[E]** an estimate;
- **[S]** a search-engine extraction (low confidence).

> **VaR is a speedometer, not an airbag.** A 1-day VaR95 of X% means that on about 1 day in 20 the loss is *expected* to exceed X%.
> **VaR says nothing about how large the loss is on those days.** That is why every VaR below sits next to two other figures:
> - Expected Shortfall (ES97.5, the average loss on the worst 2.5% of days);
> - the worst observed day.
>
> None of these figures is a worst case.

---

## 0. Verdict: **CONDITIONAL**

**Headline:** the maximum-exposure B′ book has a 1-day VaR95 of **2.18%** of the account, against the **3%** ceiling, so it is **0.82pp inside the ceiling**.
- That figure is the worst of all 703 two-name pairs (COIN+MSTR), from full-window historical simulation [D].
- Block-bootstrap 90% CI: 2.05–2.35%. In 0 of 2,000 resamples did it exceed 3% [D].

| Method (task 2) | 1-day VaR95 | 1-day ES97.5 | vs 3% |
|---|---|---|---|
| (a) Every 2-name pair at 15% + 15%, full window. **Worst pair: COIN+MSTR** | **2.18%** | 3.78% | **PASS** |
| (a) Same, a random pair (all 703 pairs pooled) | 0.97% | 1.82% | PASS |
| (b) Same-sector pairs only. Worst: COIN+MSTR (crypto). Worst excluding crypto: PLTR+SHOP | 2.18% / 1.70% | 3.78% / 2.64% | PASS |
| (c) The simulated B′ book (`lab.py`, backtest path = live path, invested days) | **0.40%** | 0.69% | PASS |
| *Regime check:* the same max book at **current** volatility (EWMA forecast after the 2026-11-23 close). Worst pair: NVDA+MU | **3.94%** | 5.60% | **FAIL** for 12 of 703 pairs, all semiconductor-linked |

**Why CONDITIONAL, not PASS:**

1. **Regime.**
   - On sample-average volatility, every pair passes.
   - On *current* volatility, 12 pairs (EWMA) or 9 pairs (filtered HS) exceed 3%. Every one of them contains NVDA, MU, AMD or INTC.
   - On 2026-09-30 none did (§4).
   - B-7 is a point-in-time gate, and the regime has moved away from the sample average.
2. **Tail size.**
   - Even on the full window, the worst pair's VaR99 (3.60%) and ES97.5 (3.78%) exceed 3%.
   - Its worst day was −7.77% (2022-05-11).
   - A pass on VaR95 says nothing about those days.
3. **Account base.**
   - Every percentage here is of the HK$10,000 sizing base.
   - The figures hold against real equity only while `account_hkd` ≤ real equity (C-7).
   - For the worst pair to stay ≤ 3% of real equity, equity must be **≥ HK$7,268** [D].

**Conditions I propose for the CRO's B-7 read.** These are proposals; the CRO decides.

- **V-a. Re-run the regime check when B′ is enabled.**
  - On the day the B′ enabling note is drafted, re-run §4's current-volatility check using that day's prices and feasible B′ weights.
  - Do not enable while any feasible pair has an EWMA or FHS VaR95 above 3%.
  - **Today's reading:** a pass, but a narrow one.
    - At 2026-11-23 prices, the B′ price band blocks MU (US$707.70) and AMD (US$453.46) and limits NVDA to one share = 12.87%.
    - The worst feasible pair is NVDA 12.87% + INTC 9.31%, at **2.83%**. 0 of 136 feasible pairs exceed 3% [D].
    - This pass comes from where share prices happen to sit. No risk rule produces it.
- **V-b. Account base.**
  - The pass relies on C-7 (A): ≥ HK$12,500 of settled cash with `account_hkd` 10,000 (`reports/risk/2026-11-25-v66-4-verification.md` line 180) [C].
  - On HK$12,500 the headline is 1.74% of capital [D].
  - C-7 already binds; I am recording the dependency.
- **V-c. Tail.**
  - Mario's three stresses, the other half of B-7, are still required.
  - Nothing here substitutes for them, because VaR does not measure the tail they test.

**Context.** The system's own bull filter has been **OFF since 2026-11-19**. On 2026-11-23, SPY closed at 722.29 against a 200-day MA of 730.47 (−1.12%) [D]. So the system generates no new entries today at any cap.

## 1. The maximum-exposure B′ book: definition and assumptions

**Inputs [C]:**
- `config_v66.py`: `RISK_PCT = 1.0` (l.26), `USD_HKD = 7.8` (l.27), `MAX_POSITIONS = 2` (l.28), `CAP_A_PCT = 10.0` (l.37), `CAP_BPRIME_PCT = 15.0` (l.38).
- `owner_settings.json`: `account_hkd` 10000.
- `sizing_v66.size(mode="B_PRIME")` (l.31–39) sizes in two steps:
  - first under A (≤ 10%, via `position_plan_ccy`);
  - if that gives 0 shares **and** the engine is E2, it allows 1 share, provided the price is ≤ 15% of the account and the 1-share risk is ≤ 1%.

**Derived amounts [D]:** account US$1,282.05; 10% = US$128.21; 15% = US$192.31; 1% = US$12.82.

**Definition.** The book holds two distinct names (`lab.simulate` excludes held tickers, `lab.py` l.426), each at **15.00%** of the account. That is **30% gross and 70% cash**.
- This is the most B′ allows at entry: an E2 one-share exception in each slot.
- Every other B′ position is ≤ 10% at entry.

**Assumptions:**
- **[A1] Any of the 38 names may fill a slot at exactly 15%.**
  - In reality a name qualifies only when its share price is US$128.21–192.31 and its stop distance is ≤ US$12.82.
  - Ignoring that band overstates exposure for most names on most days, so this assumption is conservative.
  - §2.3 gives the version that is feasible at today's prices.
- **[A2] Constant 15% weights at each close.** Drift above 15% is not in the headline.
  - The sizing code applies the cap only at entry; `sizing_v66.py` has no trim rule.
  - In the simulated B′ book, the largest single-position market value was **18.13%** (an exception-tier share that rose). Gross exposure peaked at **32.27%** on 2024-07-09 [D].
  - VaR scales linearly with weight. The worst pair reaches 3% at **20.6% per slot** [D].
- **[A3] Costs and cash.** Cash earns 0 (T-bill interest is ignored, a negligible conservative bias). (a) and (b) carry no costs. (c) carries lab's 10bp/side assumption (V-1 still open).
- **[A4] 1-day P&L = close-to-next-close return × weight.**
  - This includes overnight gaps.
  - It does **not** capture a gap that fills a stop at the open and then recovers by the close (§7, item 5; and the intraday-low proxy in §2.4).

## 2. VaR & ES table

**Conventions:**
- Losses are shown as positive numbers, in % of the HK$10,000 sizing base (US$1,282.05). HS = historical simulation. All figures are [D].
- **(a)/(b):**
  - 1-day: 1,199 daily close-to-close returns, 2022-02-14 → 2026-11-23.
  - 10-day: overlapping 10-day returns of a static book **with no stops**.
- **(c):**
  - 1-day: 907 invested days out of 999 in lab's tradeable window, 2022-11-30 → 2026-11-23.
  - 10-day: the simulated book's actual 10-day P&L, stops included.
- The firm ceiling applies only to 1-day VaR95. The 10-day columns are for information.

| Book | 1d VaR95 | 1d VaR99 | 1d ES97.5 | Worst day | 10d VaR95 | 10d VaR99 | 10d ES97.5 | 1d VaR95 vs 3% |
|---|---|---|---|---|---|---|---|---|
| **(a) worst pair: COIN+MSTR** | **2.18** | 3.60 | 3.78 | −7.77 (2022-05-11) | 6.90 | 10.22 | 10.58 | PASS |
| (a) 90th-percentile pair | 1.40 | 2.26 | 2.36 | | | | | PASS |
| (a) median pair (INTC+COST) | 0.86 | 1.53 | 1.67 | | 2.58 (median across pairs) | | | PASS |
| (a) random pair (703 pooled) | 0.97 | 1.74 | 1.82 | −7.77 | 2.87 | 4.74 | 4.86 | PASS |
| (a) *adversarial bound*: each day's 2 worst of 38 (a hindsight construct, not a tradeable book) | 2.98 | 4.57 | 4.74 | −7.77 | | | | bound only |
| **(b) same-sector worst: COIN+MSTR (crypto)** | **2.18** | 3.60 | 3.78 | −7.77 | 6.90 | 10.22 | 10.58 | PASS |
| (b) same-sector worst excluding crypto: PLTR+SHOP (software) | 1.70 | 2.61 | 2.64 | −4.68 | | | | PASS |
| (b) same-sector random pair (78 pooled) | 1.02 | 1.84 | 1.91 | −7.77 | 3.00 | 4.93 | 5.08 | PASS |
| **(c) simulated B′ book, backtest path (live)** | **0.40** | 0.67 | 0.69 | −1.01 (2024-02-13) | 1.06 | 1.56 | 1.56 | PASS |
| (c) reference: A (10% flat), backtest path | 0.38 | 0.72 | 0.73 | −1.20 | 0.97 | 1.38 | 1.40 | PASS |
| (c) reference: D (15% flat), backtest path | 0.50 | 0.73 | 0.80 | −1.68 | 1.42 | 1.78 | 1.84 | PASS |
| (c) reference: B′ on the scanner path (shadow) | 0.37 | 0.70 | 0.72 | −1.20 | | | | PASS |

**Pair counts over the full window (703 pairs) [D]:**
- VaR95 > 3%: **0**.
- VaR99 > 3%: **2** (COIN+MSTR, TSLA+MSTR).
- ES97.5 > 3%: **6**, every one containing MSTR or COIN: TSLA+MSTR, AMD+MSTR, PLTR+MSTR, SHOP+COIN, SHOP+MSTR, COIN+MSTR.

### 2.1 Same-sector pairs, by sector (b)

Sector grouping: `rules_v642.py` has none (only the ordered ticker list). I used `strategy/v6.5/portfolio_sim.py::SECTOR` verbatim [C]. That file labels the mapping a rough grouping, not GICS. It has 8 groups and yields 78 same-sector pairs.

| Sector (pairs) | VaR95 median / max | VaR99 max | ES97.5 max | Worst day (max) |
|---|---|---|---|---|
| crypto (1) | 2.18 / 2.18 | 3.60 | 3.78 | −7.77 |
| software (15) | 1.30 / 1.70 | 2.61 | 2.64 | −7.27 |
| semi (15) | 1.30 / 1.51 | 2.55 | 2.69 | −5.96 |
| megatech (15) | 0.92 / 1.24 | 2.10 | 2.15 | −4.29 |
| energy_ind (6) | 0.70 / 0.87 | 1.35 | 1.44 | −2.87 |
| fin (10) | 0.63 / 0.77 | 1.31 | 1.34 | −3.04 |
| health (6) | 0.61 / 0.68 | 1.31 | 1.41 | −3.29 |
| consumer (10) | 0.59 / 0.79 | 1.44 | 1.59 | −3.85 |

Same-sector pairing raises the pooled VaR95 only modestly (1.02 vs 0.97). The worst pair is the same in (a) and (b), because the riskiest pair in the universe *is* a same-sector pair.

### 2.2 Bull-regime days only (sensitivity)

The system enters only when SPY > MA200. Held positions can still ride through a regime flip, so the full window is the conservative base.

On the 908 days where SPY was above its MA200 at the prior close [D]:
- random pair: 0.84 / 1.50 / 1.57 (VaR95 / VaR99 / ES97.5);
- COIN+MSTR: 2.02 / 2.82 / 3.10, worst day −5.14 (2025-03-10).

### 2.3 Feasible at today's prices (sensitivity to [A1])

Prices are the 2026-11-23 closes [D].
- **Blocked under B′:** 21 of 38 names, because one share costs more than US$192.31. These are AAPL, MSFT, GOOGL, AMZN, META, TSLA, AVGO, AMD, MU, JPM, GS, V, MA, COST, MCD, UNH, JNJ, LLY, CVX, CAT, ADBE.
- **In the one-share exception band:** 8 names: NVDA, QCOM, WMT, XOM, BA, PLTR, CRM, SHOP.
- **Results on the 136 feasible pairs, at maximum feasible weights:**
  - full-window HS VaR95: max **1.32**;
  - current-volatility EWMA VaR95: max **2.83** (NVDA+INTC); 0 pairs above 3%.

### 2.4 Intraday-low proxy (a conservative stand-in for the stop path; a proxy, not a forecast)

The P&L here uses Low_t / Close_{t−1} − 1 for **both** names at once, as if both stops filled at the day's worst point [D]:
- random pair: VaR95 1.35, VaR99 2.20, ES97.5 2.28;
- worst pair COIN+MSTR: **2.93** / 4.27 / 4.74. This is just inside 3%. 0 pairs have VaR95 > 3%.

## 3. Method comparison, and why the methods diverge

### 3.1 Historical simulation vs parametric normal (same full-window σ) [D]

| Book | HS VaR95 | Normal VaR95 | HS VaR99 | Normal VaR99 | HS ES97.5 | Normal ES97.5 |
|---|---|---|---|---|---|---|
| Random pair (pooled) | 0.97 | 1.05 | 1.74 | 1.49 | 1.82 | 1.50 |
| Median across pairs | 0.86 | 0.92 | 1.48 | 1.32 | 1.57 | 1.32 |
| COIN+MSTR | 2.18 | 2.55 | 3.60 | 3.63 | 3.78 | 3.65 |
| Simulated B′ book | 0.40 | 0.41 | 0.67 | 0.59 | 0.69 | 0.60 |

**Why they diverge:**
- Daily pair P&L is peaked and fat-tailed. The pooled excess kurtosis is 6.5.
- At **95%** the normal overstates VaR: more of the real mass sits near zero than a normal with the same σ allows.
- At **99%**, and for ES, the normal **understates** the tail by 12–21% (pooled: VaR99 1.49 vs 1.74; ES 1.50 vs 1.82).
- COIN+MSTR has thinner relative tails (excess kurtosis 1.8), so the two methods roughly agree at 99%.
- **Practical rule:** at 95% the HS figure is the honest one. At 99% even HS is too low (§6.4).

### 3.2 Full-window vs current volatility (EWMA λ = 0.94, and filtered HS) [D]

| Max-book pairs | Full-window HS | EWMA (now) | FHS (now) |
|---|---|---|---|
| Median VaR95 | 0.86 | 1.20 | 1.16 |
| 90th-percentile VaR95 | 1.40 | 2.26 | 2.21 |
| Maximum VaR95 | 2.18 (COIN+MSTR) | **3.94 (NVDA+MU)** | **3.72 (NVDA+MU)** |
| Pairs with VaR95 > 3% (all 703) | 0 | **12** | **9** |
| Same-sector pairs with VaR95 > 3% (of 78) | 0 | 7 (all semis) | 7 (all semis) |
| Pairs with VaR99 > 3% | 2 | 94 | 152 |
| Pairs with ES97.5 > 3% | 6 | 95 | 171 |

**Volatility multiples and what drives the gap:**
- Current σ ÷ full-window σ, across pairs: median 1.21×, 90th percentile 1.87×, maximum 2.60×.
- Full-window HS answers: "can this construct breach the ceiling in a typical period?" It cannot.
- EWMA and FHS answer: "what would a max book carry into the next session?" For semis pairs, the answer is above the ceiling.
- For limit monitoring, the current estimate is the one to check each morning. That is the source of the CONDITIONAL.

**The 12 EWMA pairs above 3%:** NVDA+TSLA, NVDA+AMD, NVDA+QCOM, NVDA+MU, NVDA+INTC, NVDA+PLTR, NVDA+COIN, NVDA+MSTR, AMD+MU, AMD+INTC, MU+INTC, MU+MSTR.
**The 9 FHS pairs above 3%:** NVDA+TSLA, NVDA+AMD, NVDA+QCOM, NVDA+MU, NVDA+INTC, NVDA+MSTR, AMD+MU, AMD+INTC, MU+INTC. These are the EWMA list minus NVDA+PLTR, NVDA+COIN and MU+MSTR.

### 3.3 Maximum book vs the simulated book (0.40 vs 2.18)

The simulated book shows what B′ *did* on one 4-year path. The maximum book shows what B′ *permits*. The ceiling has to be read against what it permits.

Why the simulated book is so much lower [D]:
- **Exposure:** mean gross market value on invested days was 17.1% (A: 13.6%), against 30%.
- **Names:** the system's 20 exception trades were mostly in lower-volatility names: JNJ ×5, AAPL ×3, JPM ×3, CVX ×3, QCOM ×2, XOM ×2, GOOGL ×1, NVDA ×1.
- **Regime:** lab's window starts 2022-11-30, after most of the 2022 bear market.
- **Stops:** stops cut multi-day losses.

**A vs B′ vs D on the simulated book:** B′ adds 0.02pp of VaR95 over A and lowers VaR99 by 0.04pp. D adds 0.12pp of VaR95. This is consistent with the CRO's finding that B′ is tail-neutral (ruling §3.2).

## 4. Volatility regime: **WARNING (elevated, led by semis, clustering)**

**Realized volatility** (20-day, annualised), 2026-11-23 [D]:

| Series | 20d vol | Percentile of its own 20d history (window) | vs full-window vol |
|---|---|---|---|
| SPY | 31.9% | 97th | 1.82× (full 17.5%); 60d 20.0% |
| QQQ | 48.0% | 98th | 2.04× |
| 38-name equal-weight basket | 36.1% | 94th | window max 61.2% (2025-04-25) |
| NVDA / INTC / AMD / MU | 136.9 / 142.8 / 133.0 / 131.8% | 100 / 100 / 100 / 99.7th | 2.5 / 2.4 / 2.2 / 2.2× |
| AVGO / QCOM | 84.6 / 81.1% | 96.9 / 96.4th | 1.8 / 1.9× |

**Breadth:** 12 of 38 names are at or above the 90th percentile of their own 20-day vol, and 31 of 38 are above their full-window vol.

**The last two sessions (close-to-close) [D]:**
- 2026-11-20: SPY −3.64%, QQQ −5.67%, NVDA −14.01%, MU −13.89%, AMD −13.25%, AVGO −12.19%.
- 2026-11-23: SPY +4.71%, QQQ +7.00%, NVDA +31.48%, MU +19.04%, INTC +16.34%.

**Correlation rising inside the hot clusters (full window → last 60 days) [D]:**
- COIN–MSTR 0.74 → 0.89;
- NVDA–MU 0.56 → 0.75;
- AMD–MU 0.61 → 0.77.

Market-wide it is not rising: the median pair correlation went 0.29 → 0.26. The stress is concentrated, which is exactly the 2-slot same-cluster risk.

**How the warning built up.** Count of max-book pairs with EWMA VaR95 above 3% [D]:

| Close | Pairs > 3% | Highest pair |
|---|---|---|
| 2026-09-30 | 0 | 2.53 (COIN+MSTR) |
| 2026-10-29 | 0 | 2.01 (COIN+MSTR) |
| 2026-10-30 (INTC −28.6% that day) | 0 | 2.96 (AMD+INTC) |
| 2026-11-05 | 2 | 3.24 (AMD+INTC) |
| 2026-11-13 | 2 | 3.23 (AMD+INTC) |
| 2026-11-19 | 0 | 2.97 (AMD+INTC) |
| 2026-11-20 | 2 | 3.20 (AMD+MU) |
| **2026-11-23** | **12** | **3.94 (NVDA+MU)** |

**Volatility clustering [D]:**
- Lag-1 autocorrelation of squared returns: SPY 0.19, basket 0.16, median pair 0.10. It is positive for 99.9% of pairs.
- Autocorrelation of absolute returns is still 0.16 at lag 10.
- So shocks persist. Expect the current regime to last longer than a few sessions [E].

**Implied volatility [S]:**
- The data folder has no VIX series. FRED is outside this session's allowed network domains, so the series could not be fetched directly; it would have to be allowed in the session's network settings.
- Search-engine extraction (low confidence):
  - FRED VIXCLS: 28.18 (2026-11-05), 25.64 (11-06), 19.92 (11-09), 19.30 (11-13) — [FRED VIXCLS](https://fred.stlouisfed.org/series/VIXCLS);
  - Ad-hoc News: 24.52 on 18 Nov — [Ad-hoc News](https://www.ad-hoc-news.de/boerse/news/marktberichte/vix-ends-november-18-at-24-52-down-3-69-percent/70533036). The year is not independently confirmed.
- SPY 20-day realized vol on the same dates [D]: 20.1, 19.9, 22.0, 22.1, 22.9. So implied and realized were roughly in line through 18 Nov.
- **VIX for 11-20 and 11-23: NOT OBTAINED.** No implied-vol signal can be stated for the two sessions that drive this warning.

**Data note: unverified outlier.** I cannot check the NVDA +31.48% bar on 2026-11-23 against a second source. The conclusion does not depend on it:
- at the 2026-11-20 close, before that bar, 2 pairs were already above 3% (AMD+MU 3.20%);
- on 11-23, 4 of the 12 pairs above 3% do not contain NVDA.

## 5. Component VaR by position (for John and Zac)

### 5.1 Maximum book: risk by name, at 15% [D]

"Share of pair ES" is the fraction of a pair's ES97.5 that comes from this name, averaged over the name's 37 pairs. Above 50% means the name dominates its pairs' tail.

| Name | Sector | Stand-alone VaR95 | Stand-alone ES97.5 | EWMA VaR95 now | Share of pair ES |
|---|---|---|---|---|---|
| MSTR | crypto | 1.23 | 2.15 | 1.41 | 77% |
| COIN | crypto | 1.20 | 1.94 | 1.15 | 74% |
| SHOP | software | 0.93 | 1.68 | 1.05 | 72% |
| PLTR | software | 0.92 | 1.53 | 1.10 | 68% |
| MU | semi | 0.77 | 1.50 | **1.91** | 68% |
| INTC | semi | 0.80 | 1.49 | **1.85** | 66% |
| TSLA | megatech | 0.87 | 1.48 | 1.10 | 67% |
| AMD | semi | 0.85 | 1.43 | **1.78** | 65% |
| NVDA | semi | 0.72 | 1.23 | **2.21** | 61% |
| QCOM | semi | 0.62 | 1.21 | 1.13 | 60% |
| … | | | | | |
| PFE | health | 0.35 | 0.58 | 0.33 | 30% |
| MCD | consumer | 0.26 | 0.47 | 0.40 | 24% |
| JNJ | health | 0.26 | 0.44 | 0.40 | 21% |

**Reading:**
- Over the full window, the tail sits in crypto (MSTR, COIN), then high-beta software.
- At current volatility it sits in **semis**: NVDA alone, at 15%, carries an EWMA VaR95 of 2.21%.
- How often each name appears in the 12 current pairs above 3%: NVDA 8, MU 4, AMD 3, INTC 3, MSTR 2, TSLA 1, QCOM 1, PLTR 1, COIN 1.
- Full table: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/names_component.csv`.

### 5.2 Simulated B′ book (backtest path): who causes the tail days [D]

The tail days are the worst 5% of invested days: 46 days, with a mean loss of 0.58%.

| Tier | Contribution to the mean tail-day loss | Share |
|---|---|---|
| E2 ≤ 10% | 0.29pp | 50% |
| B′ exception (1 share, 10–15%) | 0.15pp | 25% |
| E1 ≤ 10% | 0.14pp | 25% |

**Findings:**
- **Top tickers on tail days:** NKE 0.067pp, MU 0.049, INTC 0.047, AAPL 0.044, PLTR 0.043, PFE 0.041, SHOP 0.037.
- **Exposure time:** an exception-tier position was open at the close on 405 of the 907 invested days.
- **Exception tier's worst day:** −0.69%, CVX on 2026-03-31.
- **Exception trades:** 20 in total, with entry notional 10.8–14.7%. Results ranged from −0.74% (XOM, Aug 2026) to +2.85% (CVX, Jan–Mar 2026) of the account.
- **Conclusion:** the exception tier does not drive the tail. This is consistent with CRO ruling §3.2.

### 5.3 For Zac (information, not a rule proposal)

In B′, the extra risk depends on **where the second slot goes**.
- The configuration that maximises VaR is two exception shares in the same hot cluster: crypto over the full window, semis today.
- Putting the second same-cluster name at 10% instead of 15% cuts that leg's exposure by a third.
- Whether that becomes a rule is the CRO's call. The ruling bars further changes argued on pre-2026-11-24 data.

## 6. Model calibration record

### 6.1 Prior record

There is no previous Mo Peter VaR on this book in `reports/risk/` (checked 2026-11-27). This report opens the record.

### 6.2 The CRO's interim figures vs this run

The interim figures are in `reports/risk/2026-11-24-swing-notional-cap-cro.md` line 147 [C]. They were computed on the pre-correction simulator and labelled indicative only.

| Construct | Interim VaR95 / VaR99 (pre-correction sim) | This run (corrected lab, V6.6.9) |
|---|---|---|
| A, 10% flat | 0.31 / 0.65 | 0.38 / 0.72 |
| B′ column | 0.36 / 0.68, **computed on construct B (both engines)** | B′: 0.40 / 0.67 |
| D, 15% flat | 0.41 / 0.73 | 0.50 / 0.73 |
| F, 20% flat | 0.51 / 0.92 | not run (vetoed) |

**Reading:**
- The interim figures understated VaR95 by 0.04–0.09pp. The order of magnitude and the conclusion are unchanged.
- **A correction to the CEO's brief:** the brief quotes 0.41% / 0.73% as the interim B′ figure.
  - In the ruling, those numbers are the **15% flat (D)** column.
  - The B′ column showed 0.36% / 0.68%, and that was computed on construct B.

### 6.3 Reproduction of the simulator under my B′ hook [D]

- `lab.py` was imported unmodified. B′ sizing was injected by wrapping `R.position_plan` so that it calls the production `sizing_v66.size(mode="B_PRIME")`.
- **Backtest path:** results match the CRO's `cro/f3_base.csv` exactly:
  - A: 2.21% CAGR / −4.49% DD / US$116.32;
  - B′: 3.66% / −4.20% / US$197.17;
  - D: 3.90% / −5.86% / US$210.70.
- **Scanner path:** B′ and D match. A gives 0.82% / US$42.39 against the ruling's 0.81% / US$42.10. The lab has changed since 11-24 (V6.6.x fidelity fixes). The difference is immaterial, and this is the shadow path.
- **Sizing check:** 10,027 B′ sizing calls, with **0 mismatches** between production `size()` and my independent re-implementation. 624 calls granted the exception.
- **P&L reconstruction:** per-position daily P&L matches lab's equity changes on every day except the last. On 2026-11-23 the residual is US$0.42, the exit costs of the forced end-of-data close, which lab books after its final equity mark.

### 6.4 Backtests: honest reading

The rolling backtest uses a 250-day window and predicts 1 day ahead. It covers 703 pair books over 949 out-of-sample days (2023-02-13 → 2026-11-23) [D].

| Model | Expected rate | Observed (pooled) | Pairs failing Kupiec at 5% | P(breach \| breach the previous day) |
|---|---|---|---|---|
| HS VaR95 | 5.0% | **5.20%** | 1.8% | 8.7% |
| HS VaR99 | 1.0% | **1.43%** | 13.8% (all too many breaches) | 6.4% |
| EWMA-normal VaR95 | 5.0% | 4.70% | 2.1% (none too many) | 6.4% |
| EWMA-normal VaR99 | 1.0% | **1.72%** | 49.1% | 4.0% |

**Subsets:**
- Same-sector pairs: HS95 5.30% (6.4% of pairs fail); HS99 1.46% (21.8% fail); EWMA99 1.84% (67.9% fail).
- COIN+MSTR:
  - HS95: 47 / 949 = 4.95% (p 0.95);
  - HS99: 13 / 949 = 1.37% (p 0.28);
  - EWMA95: 3.69% (p 0.05, too few breaches);
  - EWMA99: 0.42% (p 0.04, too few breaches).
- **The simulated B′ book** (rolling 250-day HS, minimum 60 days; 847 days, 2023-03-24 → 2026-11-23):
  - 45 breaches of VaR95 = **5.31%** (Kupiec p 0.68);
  - 11 breaches of VaR99 = **1.30%** (p 0.40);
  - **calibrated**.

**Where the model is right and where it is wrong:**
- **VaR95 is well calibrated** by HS on these books. The 3% test relies on that model.
- **VaR99 is too low under both models.**
  - HS99 is breached 43% more often than it should be (1.43% vs 1.0%), and normal-EWMA99 72% more often.
  - Treat every 99% figure in this report as **understated** [E].
- **Breaches cluster under HS** (8.7% vs 5%). HS adapts slowly when volatility jumps, which is the mechanism behind §4.

### 6.5 Sampling error

Block bootstrap with 10-day blocks and 2,000 draws; 90% CIs [D]:
- COIN+MSTR: VaR95 2.05–2.35; VaR99 2.96–4.37; ES97.5 3.20–4.44.
- Median pair (INTC+COST): VaR95 0.81–0.92.

### 6.6 Forward check (proposal)

On the shadow ledger, count the days the live book loses more than its then-current VaR95. Expect about 5% of invested days, and report the count at the 6-month review (ruling §5).

## 7. Caveats and model limits

**VaR assumes markets will resemble the sample. Crises do not.**

1. **Survivorship.**
   - The 38 names are a 2026 selection (F-01). Names that collapsed during 2022–26 are absent by construction, so **every tail estimate here is biased downward** [E: the direction is known, the size is not].
   - The largest single-name day in the sample is NFLX −35.1% (2022-04-20) [D].
   - A −40% single-name day, which is an assumption, at 15% = −6.0% of the account (CRO §3.3 arithmetic).
2. **Sample length.**
   - 1,199 days. A 99% VaR rests on about 12 tail observations per pair, and ES97.5 on about 30.
   - The worst pair's VaR99 has a 90% range of 2.96–4.37.
   - The live system has only 907 invested days.
3. **Fat tails the sample does not contain.**
   - The window covers:
     - the 2022 bear market (data from 2022-02-11);
     - the April 2025 shock (SPY's worst day, −5.85% on 2025-04-04);
     - the November 2026 episode.
   - It has **no 2008- or 2020-type crash, no trading halt and no fraud collapse**.
   - HS cannot produce a loss larger than the worst day in its sample.
4. **Correlation breaks in stress.** Correlations are rising inside the hot clusters (§4). That is when a 2-slot same-cluster book does the most damage, and a full-sample correlation understates it.
5. **Close-to-close vs the stop path.**
   - On 2024-08-05, COIN and MSTR closed −7.32% and −9.60% (pair −2.54% at 15% / 15%) [D]. But they opened −20.8% and −27.4% (CRO ruling §3.1) [C].
   - A stop filled at the open realises the larger loss: 7.2% for the pair at maximum B′ (ruling §3.3) [C].
   - The intraday-low proxy (§2.4) puts the worst pair at 2.93%.
   - **Mario's 2024-08-05 replay is the right tool for this, not VaR.**
6. **Static book.**
   - At 1 day this is fine.
   - The 10-day figures for (a)/(b) ignore stops, which overstates ordinary losses and understates gap-through-stop losses.
   - (c) includes stops, but it is one path.
7. **Weights.**
   - The 15% cap applies at entry, with no trim.
   - Drift reached 18.13% in the simulation.
   - The worst pair reaches 3% at 20.6% per slot. An exception share held while it rises 40% would sit at 21% [D].
8. **Account base.**
   - Every figure is in % of HK$10,000.
   - If real equity falls below the base, scale by base ÷ equity (C-7).
   - Break-even for the worst pair: HK$7,268.
9. **Sector mapping.** The grouping is rough (v6.5, not GICS). TSLA and AMZN sit in "megatech", and crypto has only one pair.
10. **Data.**
    - The bars are Webull read-only and split-adjusted; I have not verified them independently.
    - The NVDA +31.48% bar on 2026-11-23 is unverified (§4). No conclusion here depends on it.
11. **Price-band eligibility.** It is ignored in (a)/(b), which is conservative. See §2.3 for the feasible-today version.
12. **Costs.**
    - None in (a)/(b).
    - (c) uses lab's 10bp/side, which is an unverified assumption (V-1 is open).
13. **Not checked here:** earnings inside holds (B-5). Halts and fraud are left to Mario's stress.

## 8. Reproduction

**Rules followed:**
- No file under `strategy/v6.6/` was modified. Lab was imported with bytecode writing disabled.
- No broker call, no pip install.
- The fingerprint was `2b7b62182068` (V6.6.9) when I ran.

**Scripts:**
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/common.py`: data loader, sector map, VaR/ES and Kupiec helpers.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_maxbook.py`: (a) and (b), historical and parametric, bull-only subset, adversarial bound.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_extra.py`: EWMA and FHS current-vol VaR, 10-day, rolling backtests.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_regime.py`: realized vol, EWMA timeline, clustering.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_component.py`: per-name components, feasible-today book, bull filter.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_sim.py`: (c), the B′ hook into unmodified `lab.simulate`, components, sim backtest.
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_sim10.py`, `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_expo.py`, `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_boot.py`, `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/var_checks.py`, `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/recon_check.py`: 10-day sim, exposure, bootstrap, intraday-low proxy, reconstruction check.

**Main outputs:**
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/pairs_var.csv`
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/pairs_currentvol.csv`
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/pairs_backtest.csv`
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/sim_summary.json`
- `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/var_bprime/trades_bt_Bprime.csv`

**Housekeeping note for the CEO:** during this session another process created and removed untracked files under `strategy/v6.6/`.
- `selftest_extra.py` (and a `selftest` bytecode file) appeared at 20:53 UTC on 2026-11-27. It was gone by 21:07 UTC.
- `shadow_run.py` and `shadow/` (containing `2026-11-25.txt` and `ledger/`) appeared at 21:03 UTC and were still present at 21:07 UTC.
- I did not create, read or run any of them.
- None is in `CORE_FILES`. The fingerprint was `2b7b62182068` both before and after my runs, and `git diff` shows no change to tracked files under `strategy/`.

## 9. Five-line summary for `memory/decisions/`

```
2026-11-27 · Mo Peter (VaR) for CRO gate B-7 · max-exposure B′ book = 2 slots × 15% (E2 one-share exception) = 30% gross, any of 38 names (conservative: price band ignored).
1-day VaR95 vs 3% ceiling: (a) every pair, full-window HS: worst COIN+MSTR 2.18% (90% CI 2.05–2.35), random pair 0.97%; (b) same-sector worst 2.18% (ex-crypto 1.70%); (c) simulated B′ book 0.40% (A 0.38%, D 0.50%). All PASS.
ES97.5: worst pair 3.78%, VaR99 3.60%, worst day −7.77%. VaR says nothing about losses beyond it. VaR99 is under-covered in backtest (1.43% vs 1%); VaR95 is calibrated (5.20% pairs, 5.31% sim book).
Regime WARNING: at 2026-11-23 volatility (EWMA), 12/703 pairs exceed 3% (max NVDA+MU 3.94%), all semis-linked; 0 did on 2026-09-30. Feasible at today's prices: max 2.83%. Bull filter OFF since 2026-11-19.
VERDICT CONDITIONAL: PASS on sample; proposed V-a (re-run current-vol check on enable day; no enable while any feasible pair > 3%), V-b (C-7 base; break-even equity HK$7,268), V-c (Mario's stresses still required).
```

---

*Research and decision support only, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders. The provenance stamp (`scripts/stamp_provenance.py`) was not run on this file; that is left to the CEO's commit step.*
