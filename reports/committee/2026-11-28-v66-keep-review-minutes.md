# Investment Committee minutes: V6.6, keep / keep with changes / retire (2026-11-28)

**Chair:** 皮褸黃 (CEO). **Asked by:** the Owner, 28 Nov ("Committee: keep V6.6?").
**Type:** strategy review; no ticker scorecard.
**Pack:** `reports/committee/2026-11-28-v66-keep-review-pack.md`. Stale MOC and HK lines were corrected by the CEO after Tom's review.
**Votes:** `reports/committee/2026-11-28-v66-keep-vote-{cio,cro,mathking,pm}.md`.
**Code:** V6.6.9, fingerprint `2b7b62182068`; selftest 153. No broker call was made.

## 1. Evidence (all on file, all at the CRO's *estimated* fee of US$0.35 minimum + 10 bp per side; the real fee, V-1, is not yet known)

- **Backtest, 2022-11-30 → 2026-11-23:**
  - the trading made about zero (−0.18%/yr): E1 +US$81.4, E2 −US$81.7;
  - −1.20%/yr vs plain T-bills, and behind the T-bill line on every day;
  - ahead in 1 calendar year of 4 (`reports/quant/2026-11-27-v66-robustness.md`).
- **From Hong Kong:**
  - selling at the next open costs about nothing in price;
  - slot timing puts the result at −1.06% to −1.57%/yr vs T-bills;
  - the CRO notes the downside reaches further, since across Tom's start-date shifts HK-2 trails the lab by 0.37–1.17 pp (`reports/quant/2026-11-28-v66-hk-execution.md`, Tom's review #8).
- **The fee is the hinge:**
  - with no minimum: +0.18%/yr, about level with T-bills;
  - at US$0.35: net EV per trade −0.066% (S4, so no trading at any cap).
- **Code:** correct against its tests: 23/23 planted bugs are caught (`reports/quant/2026-11-27-v66-9-health-check.md`).
- **Forward evidence:** none yet. SPY has been below its 200-day average since 19 Nov, so the system is idle.
- **Capital at risk today:** none under any option (paper only; C-6, C-7, R-3 and V-1 to V-3 all stand before real money).

## 2. Votes

| Member | Vote | Core reason | Second choice / dissent |
|---|---|---|---|
| CIO | **RETIRE** | Trails T-bills in every version; no route to real money at today's size (R-3: LNW < HK$125,000; C-6); forward test too slow; T-bills are the income | Fallback: keep with the shadow log only, no paper orders |
| Morris (PM) | **RETIRE** | No portfolio fit; the best case only matches T-bills; the Owner's time (about 48 late nights a year at the US open in bull markets, his estimate) is the real cost | Second choice: shadow-only (B), with automatic retire if V-1 = S4 |
| Math King (Quant) | **RETIRE** | No signal: fees (US$117.4) took the whole gross (US$117.1); a useful forward test needs about 400–1,300 trades (12–40 years); retiring loses no signal evidence, since the frozen rules can be re-run later on new bars | Departs from the standing (B) recommendation |
| John (CRO) | **KEEP WITH CHANGES, operational only** | No edge on file, but retiring on his own *estimated* fee when one contract note settles it is the wrong basis | **No veto on any option; "RETIRE now is also acceptable on risk grounds"**. Vetoes any rule change now, and any real money before every gate |

**The CRO's conditions K-1 to K-7** are quoted in full in his vote file and are not restated here (L-009). In short, they cover: the token, no paper orders until V-1 is read, retire if S4, the review basis, dates, the 2022 test, and no rule changes.

## 3. Where all four agree

1. **No paper orders from now** (RETIRE stops them; CRO K-2: "No paper orders until V-1 is read").
2. **Revoke and regenerate the leaked Telegram token, whatever the outcome.** The Windows scheduled task stays off until then (CRO K-1; chair's Q-4).
3. **No rule changes now:** HK-2-slot declined, E1 max-hold ×0.8 not adopted, MOC withdrawn, B′ OFF.
4. **No real money in V6.6.** T-bills, or broker cash interest, are the income.
5. **The 2022-universe test is not run now.** It can only confirm a negative result, so it becomes a precondition for any re-activation (CIO, Math King; CRO K-6: only if V-1 passes).
6. **If V-1 returns S4, RETIRE automatically:** no re-tuning, no B′ rescue, no variant (CRO K-3; CIO, Math King, Morris Q-6).

## 4. Chair's verdict: RECOMMEND RETIRE (3 of 4). Offer the CRO's fee check as the Owner's alternative.

**The two paths differ only in timing:**
- **RETIRE now.** Q-3 terms, as defined by the chair:
  - code tagged archived (nothing deleted);
  - Windows task removed; paper orders stopped;
  - the Owner's `ledger/` kept;
  - the paused cloud shadow-log task deleted;
  - money in T-bills or broker cash interest.
  - **Re-activation** needs fresh V-2 and V-3, a CRO sign-off, and the evidence written down now: V-1 passing S4, R-3 met, and the 2022-universe test. A re-run on the same 2022–26 window, or a good month, does not count.
- **PAUSE until the real fee (CRO).**
  - No paper orders.
  - The Owner sends one Webull contract note by **2026-12-31**. Any past trade's note shows the fee, e.g. the AVGO purchase.
  - Tom runs `lab.py --mode feecheck --tif open`.
  - **S4 → RETIRE** as above. **Pass** → the committee looks again; no real money, and every gate still applies.

**Why the chair recommends RETIRE now.**
- Even the best fee case only roughly matches T-bills.
- R-3 blocks real money at today's size whatever the fee shows.
- RETIRE can be undone.

The CRO's point, that a measured fee is a better basis than an estimate, is recorded as dissent and offered to the Owner as the alternative.

**Not affected by this decision:**
- **AVGO.** The CRO's G-2 conditions and the 3 Dec close deadline stand; see `strategy/v6.6/先睇我.pdf`, block 1.
- **6160:** CRO conditions, committee review before 11 Dec.

**Consequences for today's other open work:**
- The **next PC package is not built** (no point under either path).
- The **SEC 2022 test is deferred** (point 5 above).
- The **shadow-log task stays paused.** It would be deleted under RETIRE.

## 5. Next steps

1. 腦大裝草 appends this recommendation to `memory/decisions/2026-11-24-swing-v66-release.md`.
2. **Owner brief:** a one-page Cantonese PDF (排版師 → 翻譯官 → Ai 管理層). The Owner chooses RETIRE or PAUSE.
3. After the Owner's choice:
   - carry out Q-3 (RETIRE), or K-1 to K-7 (PAUSE);
   - put a "superseded" banner on the old "add-on" and "≈2.2%/yr" wording (CIO condition);
   - move income work to cash placement (Morris, Peterson).

*Research and decision support, not financial advice. Markets cannot be reliably predicted. Nothing changes until the Owner decides; no agent places orders.*
