# CIO vote: V6.6, keep / keep with changes / retire (2026-11-28)

**From:** CIO, to the Investment Committee (chair 皮褸黃). **Read:** pack [P] `2026-11-28-v66-keep-review-pack.md`; [R]; [H] with Tom's review; [PH] `knowledge/investment-philosophy.md`. Source keys as in [P]. No broker calls; nothing committed.

## Vote: RETIRE (as defined in the chair's Q-3 ruling)

**Reasons**
1. **Goal fit.** The Owner wants "some extra return for my living" [I:11]. V6.6 trails T-bills in every version: lab −1.20%/yr, HK −1.06% to −1.57%/yr [R:42; H:18–21], and it was above the T-bill line on 0% of days [R:46]. Even at a near-zero fee the prize is +HK$26 to +166 a year [I:326]. T-bills are the income [I:275].
2. **No edge, by the firm's own pre-registered test.** The trading alone made −0.18%/yr: E1 +US$81 vs E2 −US$82 [R:44–45]. At the US$0.35 estimate with cancel-at-open it is S4, "no new entries at any cap" [I:35; RM:204]. Philosophy 4 and 6 [PH:16–23]: we grade the process we wrote down, not the hope that 2025 repeats.
3. **The forward test cannot change the answer in useful time.** 49 (lab path) to 62 (scanner path) closed E2 trades in 4 years (`results/hk_exec/trades_lab.csv`, `results/trades_scanner_path.csv`; CIO count, estimate) puts the 30-E2 gate about 2–2.5 years away. The clock has not started (bear regime; shadow log paused [P:33]). A 30-trade E2 review has a CI of about ±3 pp [`2026-11-24-v66-release-code-review.md`:405], against a hurdle of ≈HK$4–5 a trade [I:328], i.e. ≈0.4–0.5% of a HK$1,000 position (derived). It tests discipline, not edge.
4. **Philosophy fit is weak.** [PH:13–15] prefers quality and moats bought with a margin of safety. V6.6 is a ≤60-day technical swing system confined to 17 names priced under ~US$128 [R:118–120], where the US$0.35 minimum alone is ≥0.27% a side (derived). The binding constraint is sleeve size, not signals. The study advises against raising size to chase income [I:322–323], and any other base needs Tom's rerun plus CRO review [I:294].
5. **No real-money route at today's size, whatever the backtest says.** R-3: if LNW < HK$125,000 the answer is (B) "whatever V-1 shows" [I:306]. C-6 is still open [P:123]. KEEP therefore spends Owner time (US open 21:30/22:30 HKT for every entry and exit [I:77; H:36–39]) and usage with no cost figure on file [P:57], on evidence that cannot lead to an income sleeve.
6. **Survival is not the reason.** Paper risks nothing [P:58]. I vote RETIRE because KEEP adds no value, not because it is dangerous.

**Conditions**
- C-1. Q-3 scope as ruled. Q-4: the token is revoked whatever the outcome. 腦大裝草 appends this vote and its dissent to [D] (rule 4).
- C-2. Before the archive tag: a "superseded" banner on the "add-on" wording [I:44, I:267] and on the ≈2.2%/yr text [RM:288–300], so the archive does not carry claims the firm has withdrawn.
- C-3. Pre-register in [D] what counts as new evidence for re-activation, on top of fresh V-2/V-3 and CRO sign-off: V-1 passing S4 with `--tif open`; R-3 met; the 2022-fixed-universe test run. A re-run on the 2022–2026 window or a good month does not count ("2025+ was already seen" [T:38]).
- C-4. The income work moves to where the income is: Morris and Peterson on cash placement under R-3 and R-1.5 [I:282, I:285]. Futu's cash rate is "not provided" [I:367].
- C-5. Owner-facing text goes 排版師 → 翻譯官 → Ai 管理層, with CRO conditions quoted in full or pointed to (L-009).

**Q-5 / Q-6 / Q-7 (CIO view)**
- **Q-5 (if KEEP):** a fixed-date keep/retire review on **2027-05-28**. It covers discipline and Webull-vs-Yahoo parity only (no return comparison before 100 trades [D:72]). The 30-E2 + 6-month gate [D:71] stays the gate for the first *return* review.
- **Q-6: no paper trading under S4.** S4 bars trading "at any cap" [RM:204] and "is not re-tuned after the fact" [I:97]. Paper-trading a system that cannot be traded tests nothing we would act on. Under KEEP, S4 should trigger RETIRE automatically.
- **Q-7:** under RETIRE, not now; it becomes a re-activation precondition (C-3). Under KEEP, run it before 2027-05-28 from a primary source only (the OEF filing on SEC EDGAR or the issuer's dated file [R:132]), with the Owner's network approval.

**Dissent**
- **The strongest case against my vote (Tom):** "That pattern fits "no edge"; it does not show a negative edge." [T:109] RETIRE gives up the only route to forward evidence [R:141], and in today's bear regime KEEP costs the Owner little. My fallback if the committee keeps it: KEEP WITH CHANGES, meaning shadow log only (no paper orders), the 2027-05-28 review, and automatic RETIRE on S4.
- **Mine, against the record:** I do not accept "build forward evidence" as a reason to keep (reason 3). Process note: the chair ran [R], [H], [HC] and [I]; Tom and the CRO are the independent checks, and no Ai 管理層 audit is on file for [R] or [H] [P:128].

**Research agenda changes:** V6.6 leaves the active quant agenda, which frees Tom's time. Add "cash income placement" (Morris, Peterson; rate path per [I:233]). `knowledge/research-agenda.md` does not exist yet; I will create it separately. **Philosophy gap, for the Owner's approval (the document is not edited here):** the philosophy says nothing about short-horizon systems. Proposed line: "A trading system gets a real-money sleeve only if its pre-registered forward test can separate its edge from the cash hurdle within 12 months."

*Research and decision support, not financial advice. Backtest figures are history, not forecasts. No agent of this firm places orders.*
