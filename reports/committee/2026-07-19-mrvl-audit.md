# MRVL (Marvell Technology) — Pre-Committee Audit

**Auditor:** Ai 管理層, AI Audit (Dept. 9 — AI Intelligence) · **Date:** 2026-07-19
**Package audited:** MRVL research pack dated 2026-07-19 (12 reports)
**For:** CEO 皮褸黃 / Investment Committee · **Method:** citation audit (re-fetched via WebSearch), hallucination screen, logic audit, bias audit

---

## Verdicts by report

| Report | Author | Score/Call | Audit verdict |
|---|---|---|---|
| Valuation | 𢦀鳩仔 | 25/100, FV $55–105, MoS −170% | **PASS WITH FLAGS** |
| Risk review | John (CRO) | VETOED, 24/100 | **PASS** (minor inherited flags) |
| Financials | 巴爺爺 | 66/100 (B−) | **PASS** — every sampled number verified |
| **Moat** | **菲比斯** | narrow/eroding | **FAIL — report does not exist on disk** |
| Custom silicon | Elon Musk | OW 55% | PASS WITH FLAGS |
| Management | Peter | B+ | PASS (skim) |
| Macro regime | Peterson | 52/100 | PASS (skim; strong self-audit) |
| Technicals | 老詹 | 34/100 | PASS |
| Structure | Tim Cook | — | PASS |
| Flow | 王老吉 | distribution ~60% | PASS |
| News | 修大哥 | 64/100 | PASS WITH FLAGS |
| Sentiment | 社交媒體官 | net-bullish | PASS |
| Regulatory | The dictator | mild headwind | PASS (skim) |
| Geopolitics | LeBron James | MEDIUM-HIGH | PASS WITH FLAGS (stale price) |

**Package-level: NOT YET FIT for committee** — the decision-driving moat report is missing entirely, and two of John's own binding risk inputs (Mo Peter VaR, Mario stress) plus portfolio data are absent. The *direction* of the recommendation (do-not-buy at $188.68) is robust and verified; the *specific* fair value and the −170% MoS headline are philosophy-conditional and lean on a source document that does not exist. Fix the moat file, then proceed with the flags footnoted.

---

## Claims checked (claim / source / result)

| # | Load-bearing claim | Source cited | Audit result |
|---|---|---|---|
| 1 | Fri 7/17 close **$188.68** | stockanalysis/Yahoo/macrotrends (multi) | **VERIFIED** — consistent across all 12 reports and re-fetched |
| 2 | 52-wk high **$329.88** (Jun 2026); DD **−42.8%** | macrotrends/stockanalysis | **VERIFIED** ($329.80–329.88 intraday, June); DD arithmetic correct |
| 3 | FY26 revenue **$8.195B** (+42%) | Q4/FY26 release | **VERIFIED exactly** (Businesswire/SEC 8-K) |
| 4 | Q1 FY27 rev **$2.418B**, GAAP NI **$34.5M** ($0.04), non-GAAP **$718.0M** ($0.80) | Q1 FY27 release | **VERIFIED exactly** ($18.0M above guide mid; OCF $638.8M record) |
| 5 | FY26 GAAP **$3.07** / non-GAAP **$2.84**; non-GAAP op margin **35.3%** | FY26 release | **VERIFIED exactly** |
| 6 | Infineon auto-ethernet **$2.5B** all-cash, closed **Aug 14, 2025** | PRNewswire | **VERIFIED** (close date + amount) |
| 7 | **$1.8B pre-tax divestiture gain** (Q3 FY26) | 巴爺爺 / Q3 FY26 release | **PARTIAL** — exact gain not independently reconfirmed in re-fetch, but *consistent* with the reported GAAP $2.670B vs non-GAAP $2.466B spread and the "core ex-gain ~$1.0–1.1B" estimate. Accept as sourced; not a red flag |
| 8 | **82%** top-10 customer concentration (FY26) | 10-K | **VERIFIED** (also ~45% via a single distributor) |
| 9 | Four straight GAAP loss years FY22–25 | 巴爺爺 | **VERIFIED for FY23–25** as filed ($(164)M/$(933)M/$(885)M); FY22 not separately re-checked. Note framing: FY26 was GAAP-profitable, so "four loss years FY22–25" then a profitable FY26 |
| 10 | Amazon **Trainium 3 compute die lost to Alchip** | Elon Musk | **SUPPORTED externally** (SemiAnalysis: "Marvell ends up big loser"); Maia 200→GUC less cleanly confirmed. See Flag B |
| 11 | Google **"Merope" LPU win**, up to $12B lifecycle | Elon / KeyBanc | **OVERSTATED as "win"** — primary reporting (The Information, Apr) = *talks, no signed contract*. $12B is a KeyBanc estimate. Used only as bull optionality, so low impact |
| 12 | KeyBanc PT **$400** (raised 7/14) | Benzinga/StockTwits | **VERIFIED** |
| 13 | 200-day SMA **~$128** (corrected from bad ~$270 print) | movingaverages.com 7/13 | **ACCEPTED** — sourced/dated; John's independent ~$132 corroborates; the ~$270 correction is clearly right. Not independently recomputed |
| 14 | Short interest ~28–32M sh (**4.3–4.5% float**); no Burry-style MRVL short | 王老吉 / 社交媒體官 | **VERIFIED as modest**; sentiment desk correctly states there is **no** Burry-equivalent bear on MRVL (that was MU). See Bias note 4 |
| 15 | ROIC **~6–8% < WACC, "never earned cost of capital"** | 菲比斯 (via brief) / 巴爺爺 | **PARTIALLY CONTRADICTED** — 巴爺爺's own non-GAAP ROIC is **~12–13%**, at/above the 11% base WACC. See Flag C |

Financials, price, drawdown, and concentration — the factual spine of the pack — are **clean**. 巴爺爺's report in particular survived a full sampling with zero discrepancies.

---

## Flags (with severity)

**Flag A — HIGH — 菲比斯's moat report does not exist on disk, yet is load-bearing across four reports.**
`reports/equity/2026-07-19-mrvl-moat.md` is **not present** (confirmed by directory glob). 𢦀鳩仔 and John both disclose this honestly ("standalone file NOT on disk … carried in the task brief"). But the moat report supplies the *most decision-critical* valuation levers: the **35–40% margin-of-safety demand** (the buy-price gate), the "narrow/eroding moat → no Broadcom multiple," the socket-churn renewal probability (≤50–60%), and the 11% "narrow-moat WACC." Per mandate, an uncited load-bearing input is automatically flagged: these terms trace only to the task brief, not to a filed, sourced document. Some are corroborated elsewhere (ROIC ~6% by 巴爺爺; socket losses by Elon/SemiAnalysis; 82% concentration by 巴爺爺), but the **35–40% MoS demand and the WACC premium have no filed source at all.** *Note: the audit tasking stated "both are on disk now" — that premise is false; I could not reconcile 𢦀鳩仔's inputs against a 菲比斯 report because none exists.*

**Flag B — MEDIUM — unreconciled internal contradiction on the socket-loss claim.**
修大哥 (news) states the Trainium/Alchip loss is "**unresolved**," that Benchmark "walked it back materially," Morningstar called share-loss "overblown," and Murphy rebutted "we didn't lose any business." Elon Musk, 𢦀鳩仔, and John treat the loss as "**verified**" and build the base/bear revenue haircut on it. External re-fetch (SemiAnalysis) actually **supports Elon** on Trainium 3 — so the bearish version is not unfounded — but the package never reconciles the two internal positions, and the bear case escalates further by *assuming a third, undocumented socket loss* caps FY28 at $11.5B. That third loss is speculation presented inside a quantified scenario. Committee should see that the socket-churn haircut rests on two documented losses (defensible) plus one hypothesised one (not).

**Flag C — MEDIUM — "never earned its cost of capital" leans on GAAP ROIC while the firm's stated philosophy uses non-GAAP.**
The bear thesis repeats ROIC "~6–8% < WACC." That is the **GAAP/goodwill-inclusive** figure. 巴爺爺's own **non-GAAP** ROIC estimate is **~12–13%** — at or above the 11% base WACC 𢦀鳩仔 uses. The firm's philosophy (per 巴爺爺 and 𢦀鳩仔 themselves) is "GAAP over-penalizes; use FCF + SBC-adjusted non-GAAP." Applying the *low GAAP* ROIC to justify "never earned cost of capital / no Broadcom multiple," while elsewhere arguing GAAP is too harsh, is selective framing on a load-bearing lever. The honest statement is 巴爺爺's: ROIC "only now approaches cost of capital" — weaker than "has never earned it."

**Flag D — MEDIUM — fair value is an outlier-low even versus published Street bears; must be labelled philosophy-conditional, not objective mispricing.**
𢦀鳩仔's $55–105 sits **below** the external Street *bear* bracket (a published $110 bear case; consensus PT ~$252; bull $385–400). 𢦀鳩仔 discloses this cleanly ("a Street/non-GAAP framework yields $150–250+ … our far-lower number is the deliberate product of the firm's philosophy"). No fabrication — but the "price is 2.7x fair value / MoS −170%" headline that drives both the valuation score *and* John's veto is **conditional on the firm's chosen assumptions** (SBC as real cost, 11% WACC, socket-churn, no Broadcom multiple — several attributed to the missing moat file). The committee must not read −170% as a market-observable mispricing.

**Flag E — LOW — "Merope win" overstates "unsigned talks."** (Bull optionality only; low decision impact — see claim 11.)

**Flag F — LOW — high-price labelling inconsistency.** Peterson: ATH *close* $316.35 / intraday high $329.88; 老詹, Tim Cook, John label $329.88 a "6/18 *close*." LeBron uses $316.43. The **number driving the −42.8% drawdown ($329.88) is consistent and correct**; only the close-vs-intraday label differs. Immaterial to any score.

**Flag G — LOW — LeBron's geopolitics report is stale on price** ($245.77 Jul 15 headline, $316.43 high), not refreshed to the $188.68 close. He acknowledges the 7/16 −8% move and his MEDIUM-HIGH rating is price-independent, so no score impact — but it should be re-timestamped.

**Flag H — MEDIUM (process) — John's own binding conditions are unmet:** no Mo Peter VaR on file, no Mario stress test, `config/portfolio.yaml` empty (`holdings: []`, `cash_balance: 0.00`). John flags all three as binding on any resubmission. Until closed, no name in the pipeline can get an unconditional risk verdict.

---

## Logic audit

- **𢦀鳩仔's $55–105 follows from its stated assumptions.** Arithmetic checks: prob-weighted DCF 0.30×24 + 0.45×55 + 0.25×103 = **$57.7 ≈ $58** (correct); MoS at $70 = (70−188.68)/70 = **−169.5% ≈ −170%** (correct); 188.68/70 = **2.7×** (correct); sensitivity grids top out at **$87** (matches Grid B). The report is transparent that the current price "lives only in the reverse-DCF bull-on-bull corner" outside the grids — an honest disclosure, not a hidden inconsistency. Conclusion-strength = evidence-strength **given the assumptions**; the debate is entirely about the assumptions (Flags A/C/D), not the math. The "central ~$70" is a judgment blend above the prob-weighted $58 — i.e., 𢦀鳩仔 rounded *against* its own bear, which is conservative-of-itself, not a thumb on the scale.
- **John's veto follows from his inputs.** All sizing arithmetic verified (nominal stop 10.4%; 10%×10.4%=1.04%>1% ⇒ illegal even nominal; gap-adjusted 18% ⇒ 5.6%→5.0% cap; VaR ~0.99% at 10%). He correctly declines to "size around" a valuation problem and **routes the valuation-veto to committee/CIO rather than overclaiming it as a risk-limit veto** — process-correct. His veto inherits the philosophy-conditional fair value (Flag D) and the phantom moat terms (Flag A), which he discloses.
- **Robustness check:** even at a *less aggressive* fair value (e.g., the Street bear $110), $188.68 still fails a 35% MoS. So the **directional** conclusion — do not initiate at $188.68 — survives the flags. What does *not* survive unqualified is the specific "−170% / 2.7× fair value" magnitude.

---

## Bias observations

1. **Narrative lock-in / import from the MU run (2026-07-18): MODERATE.** Every report cross-references MU and frames MRVL "vs MU"; the Taiwan-tail, capex-deceleration, and "bearish-on-price/bullish-on-business" frame are inherited wholesale. This is partly legitimate (shared TSMC/capex factor) and Peterson explicitly self-audits for the "mirror error" of over-rewarding a drawdown — good discipline. But the committee should note the entire pack is anchored to a frame set on a *different name* the day before.
2. **Bull case is represented but subordinated.** Elon OW 55%, Peter B+, Peterson 52, 修大哥 64, sentiment net-bullish, KeyBanc $400 — the bull thesis is present and 𢦀鳩仔 grants it 25% weight ($103) with John acknowledging it. But the two decision-driving scores (val 25, risk-veto 24) dominate, and both rest on the same conservative philosophy + the missing moat file. Steel-man exists; it was not given the chance to move the verdict.
3. **Confirmation bias on the socket loss** (Flag B): the bear-friendly "verified loss" reading is adopted for the quantified haircut while the news desk's "unresolved" reading is left unreconciled.
4. **"Burry-style bear positioning" is an MU import, not an MRVL fact.** The sentiment desk correctly states MRVL has *no* celebrity-bear/narrative-liftoff and short interest is modest (~4.3–4.5% of float, ~1.4 days to cover). Any committee framing of MRVL as a "heavily-shorted / Burry-style" name would be a hallucinated carry-over from the MU analysis — the reports themselves do **not** make this error, and I flag it so the committee doesn't introduce it.
5. **Groupthink check — dissent DOES exist in the pack.** Elon (OW), Peter (B+), Peterson (52, above MU's 40), sentiment (net-bullish) provide genuine constructive voices against the valuation/risk bear. The package is not monolithic; the bear simply owns the two highest-weighted seats.

---

## Required fixes

**For the FAIL (菲比斯 moat):**
1. File the actual `reports/equity/2026-07-19-mrvl-moat.md` with **sourced** figures for: ROIC vs WACC (state GAAP *and* SBC-adjusted, per Flag C), socket-renewal probability basis, and the rationale for the **35–40% MoS demand**. These currently exist only in a task brief.
2. Once filed, 𢦀鳩仔 must confirm its carried inputs match the filed report, or re-derive the WACC/MoS levers directly from 巴爺爺 + Elon and stop attributing them to a phantom file.

**Before committee (whole package):**
3. Reconcile the socket-loss framing (Flag B): state plainly "two documented compute-die losses (Trainium 3, Maia 200); a third is a *scenario assumption*, not a fact." Update 修大哥's "unresolved" line against the SemiAnalysis evidence.
4. Re-label the valuation headline for committee: "$55–105 is a *firm-philosophy* fair value below the Street bear case; the do-not-buy conclusion holds even at Street-bear assumptions" (Flag D). Do not present −170% MoS as market-observable.
5. Close John's binding gaps: Mo Peter 1-day 95% VaR, Mario joint MU+MRVL Taiwan-shock, and Owner-populated `config/portfolio.yaml` (Flag H).
6. Fix Flag C wording firm-wide: "ROIC only now approaches cost of capital," not "never earned it," unless the GAAP-only basis is explicitly stated as the chosen lens.

**Housekeeping:** re-timestamp LeBron's price context (Flag G); harmonise the close-vs-intraday label on $329.88 (Flag F).

---

## Feedback to 床狗 (recurring patterns)
- **Missing-input-worked-from-brief** recurs (moat file here; also MU pack). Add a pre-flight check: any report citing a peer report must confirm the peer file exists on disk before using its figures; if absent, mark the derived levers "UNSOURCED — brief only," not just note it in prose.
- **Cross-name frame import** (MU→MRVL): prompt authors to state, per score, which assumptions are name-specific vs inherited.
- **GAAP/non-GAAP lens-switching** on ROIC: require a single stated lens for any "earns/doesn't earn cost of capital" claim.

---

*Audit is decision-support, not a valuation opinion. I audit the argument, not the conclusion. Numbers I verified are cited above; re-fetches via WebSearch (MRVL FY26/Q1-FY27 releases, 52-wk high, 82% concentration, Trainium/Alchip). Sources: Marvell Q1 FY27 release (Businesswire/SEC 8-K, 2026-05-27); Q4/FY26 release (2026-03-05); Infineon completion (PRNewswire, 2025-08-14); macrotrends/stockanalysis price history; SemiAnalysis/TipRanks Trainium 3.*
