# V6.6 keep review: Quant Research vote (Math King, Alpha Researcher, 2026-11-28)

**Vote: RETIRE**, on the chair's Q-3 terms. Source keys as in the pack (`reports/committee/2026-11-28-v66-keep-review-pack.md`). "MK calc" means my own arithmetic on the 130 completed lab trades in `strategy/v6.6/results/hk_exec/trades_lab.csv`. I ran no new backtest, made no broker call and edited no code.

## Reasons
1. **No paid signal at this size.** In three sentences: E1 buys short dips in large caps to earn a reversal (liquidity) premium. E2 rides trends with a trailing stop. Both trade only while SPY is above its MA200, and in S&P 100 names these premia are thin. The average position is about US$101, so costs came to about 0.92% a round trip against a gross of about 0.85% a trade (MK calc). Fees were US$117.4 against a gross of US$117.1 [R:45]. Net EV is −0.066% a trade, t ≈ −0.10 [I:35; MK calc].
2. **No V-1 result makes it worth real money.** At US$0.35 with cancel-at-open it is already S4, "no trading at any cap" [I:35; RM:204]. With no minimum fee it makes +0.18%/yr, "still not enough to call it an add-on" [R:28], and still has a 46% chance of trailing T-bills over 5 years [I:198].
3. **The positives are already seen, and they are fragile.**
   - The since-2025 +0.55% turns negative under 6 of 6 E1 entry changes [R:104].
   - The only positive variant is 1 of 14 and must not be adopted [R:105].
   - The stock-selection bias most likely flatters the result [R:34], and only 17 names were affordable [R:120].
   - E1 made +0.96% a trade (t 1.1) and E2 −1.76% (t −1.9) (MK calc). That is one sample and two engines: a forward-only observation [D:132], not grounds to drop E2.
4. **A forward test cannot settle the question in any useful time** (see Q-5): it would take about 400–1,300 trades, which is 12–40 years at 32 trades a year.
5. **Retiring loses no evidence about the signal.** The rules are frozen (fingerprint `2b7b62182068`) and the 38-name list is fixed. Re-running the archived code later on bars from after the archive date is as out-of-sample as a live shadow log. What is lost is only execution evidence, which matters only for real money, and reasons 1–2 rule real money out.
6. **KEEP costs Owner time exactly when it bites.** In bull markets that means about 66–70 manual orders a year [I:254], and being at the US open on every entry and exit day [H:36–41]. That time would buy evidence that cannot change the decision. RETIRE can be undone: nothing is deleted and `ledger/` is kept (Q-3).

## Conditions on my vote
- **C1.** The archive tag records the fingerprint, the archive date, the 38-name list and the data source. Any later look is then a clean out-of-sample re-run.
- **C2.** The archive period is a one-look holdout. Any re-activation case uses one re-run, registered in advance, no earlier than 100 trades after the archive date (the 100-trade threshold in [D:72]). It also needs fresh V-2/V-3, the real V-1 fee and a CRO sign-off (Q-3).
- **C3.** No re-tuning to rescue it: not the fee, order type, slot counting, caps, or dropping E2. Any such change is a new system with a new hypothesis, fingerprint and gates (Q-2; [I:97]).
- **C4.** Still get the V-1 contract note. It costs the Owner one document, and the fee floor is the limiting constraint on any small-account system this firm builds next.

## Q-5, Q-6, Q-7 (my view under any outcome)
- **Q-5. First forward review under KEEP.**
  - **When:** E2 closed 49 trades in about 4 years, or about 12 a year (MK calc). So "≥ 30 closed E2" [D:71] is about 2.5 bull-market years and about 80 total trades away. SPY has been below its MA200 since 19 Nov, so the count stands at 0.
  - **What 30 trades can show:** the net EV per trade has a standard error of about 1.35% (per-trade sd about 7.4%). The 95% band is ±2.6 pp against a cost of about 0.9 pp, so 30 trades cannot tell an edge from no edge.
  - **What a performance test needs:** to detect the HK$4–5 (about US$0.5–0.6) per-trade hurdle [I:153], with per-trade sd about US$7.3 and a one-sided 5% test, about 400–580 trades give an even chance and about 920–1,320 give 80% power.
  - **What to review instead:** make the first review an **execution check**. Compare each paper fill with the lab fill for the same signal. The difference has an sd of about 1.5% (derived from Tom's #7: n 56, −0.08%, t −0.4), so 30 trades pin it to within about ±0.5 pp.
  - **The clock:** the 6-month clock starts at the first `ledger/` paper fill, and that date is recorded.
  - **A pre-set end date:** at the 100-trade review [D:72], RETIRE unless V-1 has passed S4 and forward net EV per trade is above the HK$4–5 hurdle [I:328].
- **Q-6. Paper under S4: no.** S4 is the system's own fee gate. Agree now, in advance, that a V-1 result of S4 triggers RETIRE on Q-3 terms, with no switch of order type or fee to escape it [I:97]. Paper trading after S4 only practises a system that is not allowed to trade.
- **Q-7. The 2022-universe test.**
  - Under RETIRE: not now. Its expected direction is down [R:34], so it can only confirm RETIRE. Make it a precondition for any re-activation.
  - Under KEEP: run it once, with the Owner's approval, from the primary source (the OEF filing on SEC EDGAR). Read it for the subset priced at or below about US$128 [R:133]. It is a robustness check, not a holdout, because 2022–26 has already been seen [T:38].

## Dissent
- **Mine, against the standing (B) line** [R:138]: "Tests whether 2025 was luck" [R:141] overstates what paper trading can show at 32 trades a year. One forward year is noise: only 1 calendar year of 4 beat T-bills [R:31].
- **The strongest case against my vote (recorded, not accepted):** KEEP costs no money, and almost no Owner time while SPY is below its MA200. It also keeps the paper-execution route ready. I accept the first two points. The third matters only if V-1 passes, and the route can be rebuilt from the archive then.

*Research only, not financial advice. Markets cannot be reliably predicted. No broker call, no code edited, nothing committed.*
