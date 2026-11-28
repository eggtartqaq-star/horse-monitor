# CRO vote: V6.6 keep / keep with changes / retire (2026-11-28)

**John, CRO (Dept 6).** Read: the pack, revised [H] and Tom's review of it, [R], [B7], [D], `config/risk-limits.yaml`. No broker call, nothing committed, fingerprint `2b7b62182068` untouched.

## Vote: **KEEP WITH CHANGES, operational only** (no rule change, no new fingerprint). In substance: keep paper until the real fee (V-1) is read, with a pre-registered retire trigger. (Q-1: my (B) answered paper vs real money. This is my keep-vs-retire answer.)

## Reasons
- **There is no edge on file.** Trading −0.18%/yr (E1 +US$81.4, E2 −US$81.7). −1.20%/yr vs T-bills, behind on every day [R:42–46]. The universe picked in 2026 most likely flatters this [R:34].
- **At my estimated fee, every execution version is already S4:** net EV per trade is Lab −0.066%, HK-2 −0.324%, HK-2-slot −0.031% [H:18–21]. But US$0.35 is my own unverified estimate. Retiring on it when the measured fee is one contract note away is the wrong basis. Keeping with no deadline is worse.
- **Capital at risk is nil under all three options.** C-6, C-7, R-3 and V-1 to V-3 still stand between paper and money. This is a question of evidence vs Owner time, not survival, so no option warrants a veto.
- **Forward evidence is slow.** The live path closed 49 E2 trades in 3.98 years (`strategy/v6.6/results/hk_exec/trades_lab.csv`), about 12/yr. So 30 closes take about 29 months and 100 trades about 3 years [E]. With SPY below MA200 since 19 Nov, none are coming now. An open-ended keep becomes a zombie, so it needs dated exits.
- **KEEP's real risk is operational:** a leaked token, a scheduled task on the Owner's PC, and manual paper orders placed beside a real margin account. F-8 exists because a stray second sell can go short in a margin account [D:286].
- **HK-2-slot: declined** (my ruling on [H] finding 2). It is a scanner rule change chosen on data already seen [T:38]. A sell and a buy at the same open leave 3 positions (`MAX_POSITIONS` is 2) if the F-8 sale fails. At −1.06%/yr it changes no verdict.

## Conditions (binding on Zac and 死潘狗; recommendations to the Owner)
- **K-1 (Q-4).** Revoke and regenerate the Telegram token before the next scheduled run. Until then, the Windows task stays disabled [CS:283].
- **K-2.** V-1 (contract note, then `lab.py --mode feecheck --tif open`) by **2026-12-31**, and before any paper order after SPY regains its MA200. The run also reports HK-2 at the real fee, for information. No paper orders until V-1 is read.
- **K-3 (Q-6). If V-1 returns S4: RETIRE exactly as Q-3 defines it, and paper trading stops.** S4 bars trading at any cap at this account size [RM:204]. Paper would rehearse a system with no route to money and invite re-tuning. No re-tuning [I:97], no B′ rescue [B7 J-4], and no other base, cap or variant as a rescue.
- **K-4.** The forward review is judged on the full signal record (the PC scan ledger, cross-checked with the cloud shadow log), never on paper fills alone. A missed paper order is logged as missed. Paper orders go only in the paper account. A V6.6 order in any real account is a breach, reported to me the same day.
- **K-5 (Q-5).** The return review is unchanged [D:71–72]: ≥ 30 closed E2 **and** ≥ 6 months, with no cap comparison before 100 trades. The 6-month clock starts on the first day both the PC scan heartbeat and the shadow log run. The single 2026-11-25 record does not start it. Add a **keep/retire checkpoint on 2027-05-28** (J-2's date). It checks process only, not returns: V-1, record reconciliation, heartbeat gaps, S2s, LNW. If LNW is then below HK$125,000, real money has no route [I:306], and I will recommend RETIRE.
- **K-6 (Q-7).** The 2022-universe test is not worth running now: under S4 it can only confirm the result. Run it only if V-1 passes, and before any real money, with the Owner's network approval for SEC EDGAR or the issuer [R:132]. Also before any real money, the HK-2 row at the real fee must show net EV > 0. This is a real-money gate on top of the README's five; S4 itself is unchanged.
- **K-7.** No rule changes now: HK-2-slot is declined; E1 max-hold ×0.8 is not adopted [R:105]; MOC is withdrawn (F-8); B′ stays OFF [B7]. Any later change goes through a new fingerprint, Tom, my diff review and new gates, and only after V-1 passes.

## Dissent from the CEO's evidence
- **The HK range understates the downside.** Across Tom's 12 start-date shifts, HK-2 trails Lab by 0.37 to 1.17 pp (Tom's [H] review, #8). The pack's −1.57% uses the mildest of these, so "−1.1% to −1.6%" is the best case for the scanner as it counts today. That is also before the F-8 manual slippage, which is not modelled (#11). The direction of the conclusion is unchanged.
- **Stale pack text.** §3 and the §5 MOC row still cite the withdrawn MOC option and the −0.37 pp [H:42]. §8 still lists Tom's [H] review as pending; it is done. Fix both before any Owner-facing version (L-009).
- "The three options are identical today" holds for capital, but not for operational exposure (reason 5).

## Veto
- **No veto on KEEP, KEEP WITH CHANGES (as above) or RETIRE.** RETIRE now is also acceptable on risk grounds, and I would not oppose it.
- **Vetoed:** any variant that changes V6.6's trading rules now (K-7), and any real money in V6.6 before every gate is met.
- **Risk score:** V6.6.9 at A, code: 76, unchanged [B7 §6]. Real money: do not deploy (S4 at the estimated fee; V-1 to V-3, C-6, C-7 and R-3 open).

*Research and decision support, not financial advice. No agent places orders. Figures are from the cited files; [E] marks my estimate.*
