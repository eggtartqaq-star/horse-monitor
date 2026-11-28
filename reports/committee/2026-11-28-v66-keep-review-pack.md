# Strategy review pack: V6.6, keep, keep with changes, or retire (2026-11-28)

**Prepared by:** Investment Committee Secretary (Dept 10) for the chair, 皮褸黃 (CEO). **Asked by:** the Owner, 28 Nov.
**Type:** a strategy review, so there is no ticker scorecard. The Secretary has no vote and takes no side.
**Code under review:** V6.6.9, rules fingerprint `2b7b62182068` [HC:4]. No broker call was made for this pack.
**Minutes (to follow):** `reports/committee/2026-11-28-v66-keep-review-minutes.md`.

**Source keys** (cited as key:line):
- [R] `reports/quant/2026-11-27-v66-robustness.md` (revised 28 Nov) · [T] `reports/quant/2026-11-27-v66-robustness-tom-review.md`
- [H] `reports/quant/2026-11-28-v66-hk-execution.md` · [HC] `reports/quant/2026-11-27-v66-9-health-check.md`
- [I] `reports/quant/2026-11-26-v66-income-study.md` (v2) · [IR] `reports/quant/2026-11-26-v66-income-study-review.md`
- [B7] `reports/risk/2026-11-28-b7-ruling.md` · [S] `reports/quant/2026-11-27-shadow-log-setup.md`
- [D] `memory/decisions/2026-11-24-swing-v66-release.md` · [RM] `strategy/v6.6/README.md`
- [V8] `reports/risk/2026-11-26-v66-8-verification.md` · [CS] `reports/risk/2026-11-24-v66-release-cro-signoff.md` · [FP] `reports/owner-summaries/2026-11-27-start-here-v2-layout-en.md`

## 1. Executive summary

**The question:** KEEP V6.6 as a paper forward test, KEEP WITH CHANGES, or RETIRE it (archive it, end paper trading, keep the money in T-bills or the broker's cash interest).

**Evidence on file.** Backtest 2022-11-30 → 2026-11-23; HK$12,500 on a HK$10,000 base; at the CRO's **estimated** fee of US$0.35 minimum + 10 bp per side, which is unverified (V-1) [R:9–20]:
- **The trading made about zero:** −0.18%/yr. E1 made +US$81.4 and E2 lost −US$81.7 [R:44–45].
- **−1.2%/yr against T-bills** (−HK$168/yr): 3.29% vs 4.49%. Of that, −1.03 pp is the HK$3,000 reserve held at 0% [R:42–43].
- **Behind the T-bill line on every day** (0% of days above). Ahead in 1 calendar year of 4 (2025) [R:27, R:31, R:46].
- **The fee is the hinge:** with no minimum, +0.18%/yr; at US$0.35, −1.20%; at US$1, −3.92% [R:51–57]. At US$0.35 with cancel-at-open, net EV per trade is −0.066%, which is S4 [I:35].
- **HK execution** (*updated by the CEO after Tom's review, `reports/quant/2026-11-28-v66-hk-execution-tom-review.md`*):
  - Selling at the next open instead of the US close costs **about nothing in price** (+0.08 pp/yr).
  - What matters is whether a position due to be sold still blocks a slot in that night's scan:
    - as the scanner counts today (HK-2): −1.57%/yr vs T-bills;
    - if that slot counted as free (HK-2-slot, a CRO rule question): −1.06%/yr.
  - Realistic range from HK: **−1.1% to −1.6%/yr** vs T-bills [H, revised].
  - MOC exits are **not** an option: they conflict with F-8.
- **Code:** correct against its tests. After 10 new checks the mutation sweep catches 23/23; "no code bug was found" [HC:6–10]. Parity with the Owner's old engine (V-3) cannot run in the cloud [HC:24].
- **Forward evidence: none.** The shadow log has one record (2026-11-25, bear) and is paused until the Owner attaches Webull [S:5, S:21]. SPY has been below its 200-day average since 19 Nov, so the system would not trade now [D:134; RM:5].

**Standing recommendation on file:** CRO and CEO, (B) paper only, unchanged after the robustness test [R:138; I:317]. It predates today's question. No department has written on keep vs retire as such.

**Money:** the three options are identical today, because no capital is in V6.6 under any of them. They differ in Owner time, usage, and whether forward evidence builds up.

## 2. Income study (26 Nov, v2) and Tom's review

- **Verdict:** V6.6 does not qualify as a source of living income: "The income is the T-bill interest" [I:275]. The study's line that it "**might** add a little" [I:267] is superseded: the robustness test "does not support that wording" [R:36].
- **Bootstrap** (5 years, with uncertainty in the mean):
  - P(behind T-bills) is 28–75% across fee and order type; t lies between −0.91 and +0.84 [I:34].
  - For the configuration that now applies (US$0.35 estimate, cancel-at-open, because the broker cannot attach a stop [I:369]): **75%**, with a median 5-year extra of −5.6%. At no minimum fee: 46% [I:197–198].
  - Tom's circular re-run gives 75.9% [IR:124]. Tom: the headline "survives every variant I ran" [IR:22].
- **(A) vs (B):**
  - (A) is a dedicated cash or margin-disabled account with ≥ HK$12,500 settled and `account_hkd` 10,000 [I:290–294]. (B) is shadow-only [I:315].
  - The CRO and CEO recommend (B) [I:317]. If LNW is below HK$125,000, "the answer is (B) shadow-only, whatever V-1 shows" [I:306].
  - The Owner chose paper trading in a separate paper account, in effect (B) plus paper fills [D:254].

## 3. The three options and their costs

| | **KEEP** (paper, as now) | **KEEP WITH CHANGES** | **RETIRE** |
|---|---|---|---|
| What it is | Paper continues: separate paper account, Telegram + TradingView messages, paper fills in the ledger per R-5 [D:251–254, D:270]. Rules unchanged. | Paper continues with named changes. Only one is named in the sources without being a rule change: MOC sells for day-10 and day-60 exits, if the broker accepts them [H:42]. Exit-at-next-open is a rule change and "not proposed" [H:44]. | Archive V6.6, end paper trading, hold the money in T-bills or broker cash interest. |
| Owner's time | While SPY is below its MA200: little, since the scan runs from Task Scheduler at 06:30 HKT Tue–Sat [RM:232]. In bull regimes: about 66–70 manual orders a year plus stops [I:254]; being at the US open (21:30/22:30 HKT) for every entry, with no order if not at the screen [I:77; D:285]; a same-day `ledger fill` [RM:147]; a 5-minute weekly review [RM:181–185]. One-off: the PC check for V-2 and V-3 [RM:7–10], the V-1 contract note [RM:82–83], and the Webull connector [S:28–32]. | As KEEP, plus each change. (MOC is withdrawn: it conflicts with F-8 [H, revised].) A rule change brings a new fingerprint, CRO review and new gates [H:44], and a new package and stamp for the Owner's PC [HC:64–67]. | One-off: archiving, turning off the PC schedule set up by `schedule_v66.bat` [RM:235], and choosing where the cash sits. After that, none for V6.6. |
| Usage (AI) | Once re-enabled, the shadow log runs one fresh cloud session per run, Tue–Sat 07:10 HKT [S:15], plus review sessions. **No cost figure on file.** | As KEEP, plus a build, Tom's review, a CRO diff check and an audit per change (the pattern in [D:259–288]). **No cost figure on file.** | One archive session and the decision record. Then none. |
| Money at risk | **None on paper.** Real money only after every switch condition (§4) and the Owner choosing (A). Then a HK$12,500 sleeve, with the −10% monthly breaker and a stop on new entries once NLV falls below HK$10,000 [I:39–43, I:290–294]. Backtest worst drawdown: −3.49% [R:48]. | Same as KEEP. | **None.** |
| Cash return (reference) | The idle cash earns interest under all three options. | Same. | T-bills: 4.49%/yr over the window [I:60]. A T-bill ETF nets about 70% of that after 30% withholding (3.12%) [I:61, I:363–364]. Futu's cash rate: "**not provided**" [I:367]. |
| What it gives up | Owner time and usage for a system whose backtest trails T-bills at the estimated fee. | As KEEP. Also, any change picked on this sample has no clean holdout: "2025+ was already seen" [T:38]. | The only route to forward evidence, paper plus the shadow log [R:141]. No source says what re-activation would require (Q-3). |

## 4. What each option would need

- **KEEP.** Nothing new is needed to continue paper trading. For the paper record to count as evidence:
  - the shadow log is resumed after the Owner attaches Webull [S:28–34];
  - the daily scan heartbeat is kept [RM:119–120].
- **KEEP, before any real money:** the README's five switch conditions [RM:3–33]:
  1. V-2 and V-3 on the Owner's PC: **OPEN** [B7:294–295].
  2. V-1, read with `--tif open`; ALL and OOS net EV must both be > 0, otherwise S4 [RM:11; I:96–97]: **OPEN**.
  3. CRO code check: **DONE** through V6.6.9 [RM:12–18].
  4. C-6, C-7 (A) and R-3: **OPEN** [RM:19–30].
  5. Audit: **DONE** [RM:31].
  - The first forward review needs ≥ 30 closed E2 trading-path signals **and** ≥ 6 months of ledger. No cap comparison before 100 trades [D:71–72].
- **KEEP WITH CHANGES.** Each change has to be named and routed:
  - MOC: the broker's written answer [H:42].
  - A rule change: new fingerprint, CRO review, new gates [H:44].
  - Another base: Tom's rerun and CRO review [I:294].
  - **B′:** needs V-1, V-2, V-3, the open B-items and a dated CRO enabling note [B7:33–42, B7:290–300]. The CRO's view: "spend no engineering on M-3, B-2 or B-6 until V-1 is in and A clears S4" [B7:337]. Under J-4, S4 is judged on A: "A B′ pass does not cure an A fail" [B7:227].
  - Tom's review of [H]: done, PASS WITH CORRECTIONS. Applied in the revised [H]; the −0.37 pp headline is withdrawn.
- **RETIRE.**
  - A decision-record update by 腦大裝草 (rule 4).
  - Where the cash sits. CRO R-3: "Living-cost money for the next 12 months goes in this sleeve at 0%, and in no risk asset at all" [I:282]. R-1.5 prefers cash earning close to the T-bill rate over a T-bill ETF [I:366].
  - The archive scope (code, the Owner's `ledger/`, the PC schedule, paused trigger `trig_01SyUEo4RbQgSLndoGEqjRxa` [S:15]) is **not specified in any source**.

## 5. Evidence that would change the answer

| Evidence | Status | What the sources say it would do |
|---|---|---|
| **V-1 real fee** (contract note → `lab.py --mode feecheck --tif open`) | OPEN | No minimum: about level with T-bills (+0.18%/yr), "still not enough to call it an add-on" [R:28]. US$0.35 minimum: S4, no trading at any cap at this account size [I:35; RM:204]. US$1: −3.92%/yr [R:57]. Read with `--tif open` because the broker cannot attach a stop [I:369]. "The S4 test is not re-tuned after the fact" [I:97]. |
| **Forward results** (paper + shadow log) | None yet | Tests whether 2025 was luck [R:141]. Needs net EV per trade clearly above the ≈ HK$4–5 hurdle [I:328]. The since-2025 +0.55% turns negative under 6 of 6 E1 entry changes [R:104]. |
| Interest on the reserve | Rate not provided | Most of the −1.03 pp would go; the trading is still about −0.2%/yr, "still no add-on" [R:142]. A C-7 (A) account cannot be the Futu account that holds 6160/3416 [I:366]. |
| The broker accepts MOC orders placed in the HK evening | Not verified | Removes most of the −0.37 pp [H:42]. |
| A universe fixed in early 2022 (OEF holdings on SEC EDGAR, or the issuer's file) | Not run; needs the Owner's approval for network access | The bias "most likely **flatters**"; the true figure is more likely below −1.2% [R:34, R:130–133]. |
| V-3 parity; Webull vs Yahoo cross-check | OPEN; not done | Tom: parity must pass "before any V6.6 number is trusted" [D:43]. [R:148; S:39]. |

## 6. Agreement and disagreement

**Agreement:** every reviewer on file (CEO, Tom, CRO) agrees that V6.6 is not an add-on, that T-bills are the income, and that no real money should go into V6.6 now [R:22, R:138; T:21; I:275; B7:323–324]. **Unanimity is noted.** No reviewer on file claims an edge, and none has written on keep vs retire.

| Who | On what | Wording (verbatim) | Status |
|---|---|---|---|
| Tom vs the 27 Nov headline | What −1.2% measures | "The headline "−1.2%/yr" is mostly two assumptions: a reserve that earns 0%, and an unverified US$0.35 fee. It is not a measurement of the trading" [T:27] | Applied: the headline now splits the reserve from the trading [R:24–28] |
| Tom | No edge vs a negative edge | "That pattern fits "no edge"; it does not show a negative edge." [T:109] | Carried in [R:103] |
| Robustness test vs income study v2 | The "add-on" wording | "This test does not support that wording." [R:36] | The income study file still reads "might add a little" [I:267] |
| Tom (carried since 24 Nov) | Path fragility | "2-slot results are path-fragile. A one-bar ADX slip moves OOS CAGR from +2.6% to −0.6%." [D:130] | Open until V-3 |
| CRO on B′ | The only cap whose trading is positive | B′ trading +0.72%/yr vs A −0.18%, yet still −0.31%/yr vs T-bills [B7:313–314]. "B′ is a refinement of a system that has not yet shown it beats cash." [B7:324] "If V-1 fails S4: B′ falls with the system." [B7:338] | Binding under J-4 [B7:225–228] |
| HK test | The HK rows look better since 2025 | "it is not a reason to prefer them" [H:38] | Descriptive only |
| CRO vs Owner | Margin waiver on the real Webull account | "the margin decision is recorded as the Owner's override of the CRO's structural recommendation. The CRO's dissent stands." [D:276] | Independent of this decision |

## 7. Open Owner items independent of the decision

1. **AVGO / LNW by the 3 Dec close** (16:00 ET Thu 3 Dec = 05:00 HKT Fri 4 Dec [H:25]). G-2, quoted in full [V8:116–122]:
   > **G-2. AVGO hold through the 9 Dec print.**
   > - AVGO ≤ **6.6% of LNW** (1% ÷ 15% planning gap).
   > - **老詹's close-basis stop** on file before 9 Dec.
   > - A **retrospective decision record**, with your thesis in your own words.
   > - **No adds.**
   > - **LNW** (one number: the total of all brokerage accounts) **by the 3 Dec close.**
   > - Without it, the CRO recommends **exiting AVGO before the 9 Dec print**. You place every order.
   - The 4–10 Dec blackout also bars adds [V8:114]. Keep Webull cash ≥ 0 (R-7) [V8:133].
   - **Cross-link:** LNW also decides R-3, since (A) needs LNW ≥ HK$125,000 [I:306]. The item is not wholly independent.
2. **Telegram token: revoke and regenerate.** "The old token leaked" [FP:82]. CRO: "Revoke and regenerate before the bot runs" [CS:283]. Steps in checklist E1 (`strategy/v6.6/電腦待辦清單.md:199–207`). See Q-4.
3. **C-6, for real money only.** The Owner confirmed "Yes" [D:252, D:256]. In full: "**C-6.** Shown by a broker statement or a read-only pull (**a screenshot does not count**). Settled cash ≥ each order." [I:296]. The Webull account is still `INDIVIDUAL_MRGN` [D:216–217]. C-6 does not block paper trading.

## 8. Missing or stale inputs

- **Not yet reviewed:** Tom's review of [H] is pending [H:2].
- **No Ai 管理層 audit on file** for [R] (as revised), [H], [B7] or [S]: there is no 27–28 Nov audit in `reports/committee/`. Owner-facing text built from them needs one (L-009).
- **[HC] has no recorded independent reviewer.** It was run by the CEO [HC:3].
- **For the record, authorship:** the chair ran [R], [H], [HC] and [I]. The independent checks are Tom on [R] and [I], and the CRO on [I] and [B7].
- **Not obtained:** the V-1 fee [R:16]; Futu's cash rate [I:367]; whether MOC orders are accepted [H:42]; whether the standalone stop persists overnight [B7:163]; any AI usage cost for any option.
- **No forward data.** One shadow record (bear), paused. No paper-account results are on file.
- **Not consulted:** the CIO (philosophy fit), Morris (portfolio fit) and Peterson (T-bill rate path; [I:233] notes that a falling rate lowers both the hurdle and the income).
- **Stale text:**
  - [I:44] and [I:267] still carry the "add-on" wording that [R:36–37] supersedes.
  - The README's research conclusions [RM:288–300] still quote ≈ 2.2%/yr from the 24 Nov lab, which [I:209] says not to compare against. Routed to the CEO.
- **CSV check:** Tom flagged `results/robustness/yearly.csv` and `rolling6m.csv` as stale [T:220]. The Secretary checked `yearly.csv`: it now matches [R:61–67]. `rolling6m.csv` was not checked. `hk_exec/summary.csv` matches [H:17–19].

## 9. Open questions for the chair

- **Q-1.** Is the CRO's standing (B) [R:138] his answer to keep vs retire, or should he be asked directly?
- **Q-2.** KEEP WITH CHANGES: which change, exactly? MOC exits are the only one named that is not a rule change [H:42–44].
- **Q-3.** RETIRE: what is archived (code, the Owner's `ledger/`, the PC schedule, the paused trigger), and what would re-activation require (fresh V-2/V-3?)? No source covers this.
- **Q-4.** Is the leaked token revoked whatever the outcome? The CRO ties it to "before the bot runs" [CS:283].
- **Q-5.** KEEP: when is the first forward review? No source estimates how often E2 signals close, and the start date of the 6-month clock is not recorded.
- **Q-6.** If V-1 returns S4, does paper trading continue? S4 bars trading "at any cap" [RM:204]; no source addresses paper under S4.
- **Q-7.** Does the 2022-universe test go ahead (the Owner's network approval) under every option [R:132]?

**After the session:** minutes to `reports/committee/2026-11-28-v66-keep-review-minutes.md`. The decision goes to 腦大裝草 for an append to [D]. The Owner-facing version goes through 排版師 → 翻譯官 → Ai 管理層 (CRO text quoted in full or pointed to, L-009).

*Research and decision support, not financial advice. Markets cannot be reliably predicted. No agent of this firm places orders. All figures are from the cited files; backtest figures are history, not forecasts.*
