# KLAC Research Package — Pre-Committee Audit

**Auditor:** Ai 管理層 (Dept. 9 — AI Intelligence, Audit)
**Reference date:** 2026-07-19 · **Audit date:** 2026-07-24
**Package:** KLA Corporation (NASDAQ: KLAC), 10 reports · **For:** CEO 皮褸黃 / Investment Committee
**Method:** citation audit (re-fetch / WebSearch), hallucination screen, logic audit, bias audit.
Everything I assert below is tied to a source I checked; blocked fetches are marked.

---

## Verdicts by report

| Report | Author | Verdict |
|---|---|---|
| equity/klac-valuation | 𢦀鳩仔 | **FAIL** (return for bounded correction before committee) |
| risk/klac-risk-review | John | **PASS WITH FLAGS** (re-anchor after valuation fix) |
| equity/klac-financials | 巴爺爺 | **PASS** (exemplary split discipline) |
| equity/klac-moat | 菲比斯 | **PASS** |
| macro/klac-regime | Peterson | **PASS** (handled the multiple correctly — vindicated below) |
| news/klac + sentiment | 修大哥 / 社交媒體官 | **PASS WITH FLAGS** (MS "downgrade" resolved — see §MS) |

**Package fit for committee: NOT AS WRITTEN.** The business-quality half (巴爺爺, 菲比斯,
Peterson, 修大哥) is sound and can proceed. The **valuation report's headline "critical
correction" is factually wrong and contradicts its own cited source**, and it is the
number that drives the firm-wide veto framing (22/100 valuation → 31/100 risk → VETO).
The committee should not vote on the veto rhetoric until §1 is corrected. The *conclusion*
("do not chase at ~60x trailing; wait for a better entry") is still defensible on honest
numbers — this is an overstated argument, not necessarily a wrong verdict.

---

## THE DECISION-CRITICAL ITEM: is it ~42x or ~61x? — RESOLVED: BOTH, and 𢦀鳩仔 mislabeled them

𢦀鳩仔's §1 ("READ THIS FIRST") tells the committee the "~42x forward P/E" other desks
used is **"split-polluted"** and the "real" multiple is **~61x**. **This is a
misdiagnosis. There is no split pollution.** The two numbers are simply *trailing vs
forward*, and both are real:

| Multiple | Value | My verification | Matches |
|---|---|---|---|
| **Trailing GAAP P/E** | **~61–63x** | GuruFocus KLAC trailing P/E **62.92**; market cap ~$284B ÷ TTM NI $4.671B = 60.9x | 𢦀鳩仔's ~61x |
| **Forward P/E (FY27)** | **~42x** | GuruFocus forward P/E **41.74**; FY27 consensus non-GAAP EPS **~$4.98** post-split → 212.75/4.98 = 42.7x | Peterson's & "other desks'" ~42x |

- **The ~42x is the legitimate, standard next-fiscal-year (FY27) forward P/E.** It is
  corroborated by the *same GuruFocus page 𢦀鳩仔 lists in its own sources* (forward P/E
  41.74) and by the FY27 consensus EPS of ~$4.98 (adjusted, +34% YoY). It is **not**
  split-contaminated.
- **𢦀鳩仔 reached "~61x forward" by two moves:** (a) dividing price by **FY26**
  (current, nearly-complete year) non-GAAP EPS ~$3.50 instead of the **FY27** forward
  year, and (b) using its own **FY27 estimate of ~$4.00, which is ~20% below the ~$4.98
  street consensus** (line 37, "+14% est" vs actual +34%). Both moves push the "forward"
  multiple up and are undisclosed as departures.
- **Peterson (macro/klac-regime) got this right** and even flagged the split explicitly:
  "I anchor to the dated gurufocus forward P/E of ~42x … load-bearing point is that it is
  roughly double KLAC's historical average." **𢦀鳩仔 overrode a correct desk with a wrong
  "correction," and accused the correct desk of the error it did not make.**

**Net:** KLA is ~61–63x **trailing** and ~42x **forward (FY27)** — both elevated vs its
~20–25x history. The bearish *direction* survives (GuruFocus flags "significantly
overvalued"; ~42x ≈ 2x history). But the specific claim that the multiple is "really 61x,
not 42x" is false, and it materially inflates the veto case.

---

## Claims checked (claim / source / result)

| # | Load-bearing claim | Source checked | Result |
|---|---|---|---|
| 1 | 10-for-1 forward split, effective open **Jun 12, 2026** | SEC 8-K; KLA IR; PRNewswire; OCC info-memo #58941 | **CONFIRMED** (3+ independent) |
| 2 | **$212.75** is a post-split close (Jul 17) | WebSearch: KLAC $217.56 on Jul 21 (+4.8%); stockanalysis $212.92 | **CONFIRMED** consistent |
| 3 | Market cap **~$284B**; shares ~1.337B | $212.75 × 1.337B = $284.4B | **CONFIRMED** (arithmetic + split-invariant derivation valid) |
| 4 | TTM GAAP net income **$4.671B** (to Mar-26) | Macrotrends (+26.4% YoY); Simply Wall St ~$4.7B on $13.1B rev | **CONFIRMED** |
| 5 | **Trailing P/E ~61x** | GuruFocus trailing 62.92; $284.4B/$4.671B=60.9x | **CONFIRMED** |
| 6 | **"~42x is split-polluted, real ~61x"** (𢦀鳩仔 §1) | GuruFocus forward 41.74; FY27 EPS ~$4.98; Peterson | **FALSE — misdiagnosis** (see above) |
| 7 | "KLA at 53–61x is a **premium even to peers**" | GuruFocus: ASML fwd 49.65, AMAT fwd ~48x, KLAC fwd 41.74 | **CONTRADICTED** — on a consistent forward basis KLA (~42x) is **below** ASML and ~in line with AMAT, i.e. a **discount**, not a premium |
| 8 | FY27 non-GAAP EPS input **~$4.00** | Street consensus **~$4.98** (+34% YoY) | **BELOW CONSENSUS by ~20%**, undisclosed; depresses DCF/FV and inflates fwd multiple |
| 9 | FQ3 FY26 revenue **$3.415B**, +11% YoY | IndexBox; PRNewswire; beat $3.378B est | **CONFIRMED** |
| 10 | Gross margin **~62%**; FQ4 guide GM 61.75% | 巴爺爺 vs KLA release | **CONFIRMED** consistent |
| 11 | ROIC **~42–43%**; trough ~25% | GuruFocus ROIC; stock-analysis-on.net | **CONFIRMED** (third-party); trough figure plausible, not independently re-derived |
| 12 | Advanced packaging **~$1B in 2026** (from ~$635M 2025) | TIKR / BigGo — CEO on Apr 29 call | **CONFIRMED** |
| 13 | WFE **">$140B"** | KLA mgmt raised outlook to $140B+ on Apr 29 call; independent SEMI ~$135B for 2026 | **CONFIRMED as KLA guidance**; note it is *more bullish* than SEMI (~$130–135B) — attribute to company, not consensus |
| 14 | ATH **$307.37** Jun 30, 2026; **−31%** drawdown | WebSearch confirms $307.37; 307.37→212.75 = −30.8% | **CONFIRMED** |
| 15 | Jul 28 earnings date | KLA IR (cited); MarketBeat "Q4 earnings" corroborates late-Jul | **CONFIRMED** |
| 16 | John's MoS −188% / 2.9x FV | 212.75/74 = 2.87x; (74−212.75)/74 = −188% | **arithmetic CONSISTENT** with 𢦀鳩仔's $74 input (which is itself conservative — claim 8) |

---

## Flags with severity

**[HIGH] Split-pollution misdiagnosis (valuation §1, the "READ THIS FIRST" claim).**
The forward multiple is not split-polluted; ~42x is the correct FY27 forward P/E,
corroborated by 𢦀鳩仔's *own* cited GuruFocus page (41.74). Presenting ~61x as the
"forward" number is a trailing-vs-forward conflation dressed as a data-quality
correction. Because this is the explicitly-flagged driver of the veto framing and was
propagated verbatim into John's review ("~61x … ~2.5x its own history"), it is
load-bearing and must be corrected before committee.

**[HIGH] Below-consensus forward EPS, undisclosed (valuation).** 𢦀鳩仔 uses FY27
non-GAAP ~$4.00 vs street ~$4.98 (~20% low) and never tests $4.98 in the sensitivity
grid (§5b tops out at $4.50). Every forward multiple and every exit-multiple DCF cell is
mechanically depressed by this. At 26x × $4.98 the base exit-multiple lands ~$129 vs the
report's $88 — i.e., the whole FV range is sensitive to a single undisclosed sub-consensus
input. A through-cycle haircut is legitimate, but it must be *labeled* as a haircut to
consensus, not presented as "+14% est."

**[MEDIUM-HIGH] Apples-to-oranges peer comparison (valuation §1).** Comparing KLA's
trailing/current-year 53–61x against peers' *forward* 48–52x manufactures a "premium to
peers." On a consistent forward basis KLA (~42x) is **cheaper than ASML (~49x)** and ~in
line with AMAT (~48x). The claim that KLA is priced "at a premium even to its already-
extended peers" is backwards and should be struck or reworked.

**[MEDIUM] Sell-side divergence not steel-manned (valuation / package).** Street targets
cluster **$240 (UBS Neutral) – $274 (MS EW) – $275 (Susquehanna) – $325 (Cantor)**, all
*above* the ~$213 price; the *most bearish* major shop (UBS) sits 2.5x 𢦀鳩仔's $95 base
FV and 3x the $79 prob-weighted FV. Dismissing the entire street as "bubble/momentum" is a
defensible philosophy but the magnitude of the gap warrants an explicit rebuttal, not a
one-line dismissal.

**[LOW-MEDIUM] WFE ">$140B" attribution.** Correct as KLA *management* guidance (Apr 29
call), but independent SEMI 2026 estimates are ~$130–135B. Should read ">$140B (KLA
guidance; above SEMI's ~$135B)" so the committee does not treat it as consensus.

**[LOW] ROIC-trough and operating-margin precision.** 巴爺爺 self-flags exact FY operating
income as unverified-to-the-dollar; 菲比斯's ~25% trough ROIC is plausible but third-party,
not re-derived. Both appropriately hedged — not defects, noted for completeness.

---

## Morgan Stanley "downgrade" — RESOLVED (was UNVERIFIED in 修大哥's note)

修大哥 flagged an "unverifiable July MS downgrade" (Yahoo article body 403) and routed it
to Dept 2. **Resolution:** there is **no July 2026 MS downgrade.** On **Jul 6, 2026 MS
RAISED its PT to $274 from $190 and MAINTAINED Equal Weight** (Insider Monkey; MarketScreener;
confirmed via my WebSearch). The actual MS *downgrade* (Overweight → Equal-weight) was
**Sept 22, 2025** — a stale, pre-split event ($1,093 PT). The sentiment desk
(社交媒體官) already had this right ($274 EW, raised Jul 6). **Action:** 修大哥 should close
the item as *misattributed/stale* and drop the "downgrade" framing. Note the direction:
the resolved fact (MS *raised* its target, EW at $274) cuts **against** the package's bear
tilt and reinforces the §MEDIUM sell-side-divergence flag.

---

## Bias observations

- **Narrative lock-in / anchoring (the CEO's specific concern): PARTIALLY CONFIRMED.**
  KLAC is the **third consecutive "wonderful business, wrong price" veto** (MU 6.5%-capped,
  MRVL vetoed, now KLAC vetoed). The *core* bearish input is genuinely evidence-driven —
  trailing 62.9x and forward ~42x are both ~2–2.5x KLA's own history, and GuruFocus
  independently flags "significantly overvalued." **But the *degree* of bearishness is
  inflated by three self-reinforcing choices that all point the same way:** the
  split-pollution "correction" to 61x, the ~20%-below-consensus FY27 EPS, and the
  apples-to-oranges peer comparison. When three independent modeling choices all err toward
  "more expensive," and a correct desk (Peterson) is overridden to get there, that is the
  signature of confirmation bias / narrative momentum, not coincidence.
- **Steel-man of the bull case: THIN.** A 25% bull scenario ($142) exists and the report
  concedes KLA is the best business in coverage, but the genuine bull thesis — a
  ~43%-ROIC wide-moat compounder with a secular advanced-packaging ramp (~$1B, nearly
  doubling) growing FCF, cheaper than ASML on forward, with the whole street at $240–325 —
  is capped at 40x and framed as "leaving the realm of discipline." The disconfirming
  evidence (Peterson's 42x, the street targets, the MS PT *raise*) is dismissed rather than
  engaged. The bull case did **not** get a steel-man commensurate with the bear case.
- **Groupthink check — dissent DOES exist and was overridden.** Healthy sign: Peterson's
  correct ~42x. Unhealthy sign: it was overridden by 𢦀鳩仔 and not reconciled, and John
  then adopted 𢦀鳩仔's framing. The dissent existed but was silenced rather than debated.
- **John's process is sound.** He correctly routes the valuation call to committee/CIO
  (not a hard risk breach), correctly states it is not curable by sizing, and correctly
  flags missing Mo Peter VaR / Mario stress as binding. His flag is inheritance: the
  "~61x / 2.5x history" language and the −188% MoS are stated as settled fact and must be
  re-anchored to the corrected multiples/EPS.

---

## Required fixes for the FAIL (valuation) — bounded, before committee

1. **Correct §1.** State plainly: trailing ~61–63x, **forward (FY27) ~42x** (GuruFocus
   41.74; consensus EPS ~$4.98). Remove the "split-polluted / real number is 61x" claim.
   Acknowledge Peterson's ~42x was correct.
2. **Fix the peer comparison.** On a consistent forward basis KLA (~42x) is *at a discount*
   to ASML (~49x) and ~in line with AMAT (~48x). Rework or strike "premium even to peers."
3. **Disclose the EPS haircut.** Label FY27 ~$4.00 as a deliberate ~20% haircut to the
   ~$4.98 consensus, and add a $4.98 row to the §5b sensitivity grid so the committee sees
   the FV under consensus (base exit-multiple ~$129 at 26x).
4. **Steel-man the bull / street.** One honest paragraph on why $240–325 street targets and
   the compound-into-the-multiple thesis are wrong, beyond "it's a bubble."
5. **Re-score.** The 22/100 entry score is anchored to a mischaracterized 61x-forward. On
   honest numbers (forward 42x, cheaper than ASML, street 2.5–3x the FV) the "expensive vs
   own history / wait for the pullback" conclusion may well survive, but the *score* and the
   *rhetoric* must reflect the corrected multiples. **John re-anchors §VETOED language once
   this lands** — the veto may stand, but on honest inputs.

---

## What I did NOT find (to keep my own flags honest)

- No fabricated corporate action: the split is real and correctly dated everywhere.
- No hallucinated financials: FQ3 revenue, TTM NI, ROIC, advanced-packaging, ATH, and the
  drawdown all check out. 巴爺爺's split handling is the model the rest of the desk should
  copy.
- The bearish *conclusion* is not "wrong for being bearish." KLA is objectively richly
  valued vs its own history. My FAIL is on the **argument** — a false load-bearing claim,
  an undisclosed sub-consensus input, and a backwards peer comparison — not on the verdict.

*Sources checked: SEC 8-K & KLA IR (split); GuruFocus forward/trailing P/E KLAC, ASML, AMAT;
Macrotrends & Simply Wall St (TTM NI); IndexBox/PRNewswire (FQ3 rev); TIKR/BigGo (advanced
packaging, WFE); Insider Monkey/MarketScreener (MS $274 EW, Jul 6); WebSearch (ATH $307.37,
FY27 EPS ~$4.98). stockanalysis.com and gurufocus term pages returned 403 on direct fetch —
same proxy limit the desks hit; figures triangulated via WebSearch snippets from 2+ sources.
Research and decision support only — committee and Owner decide.*

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
