# PM vote: V6.6, keep, keep with changes, or retire (2026-11-28)

**Voter:** Morris, Portfolio Manager (Dept 7), for the Investment Committee chaired by 皮褸黃 (CEO). **Pack:** `reports/committee/2026-11-28-v66-keep-review-pack.md` [pack].

**Sources** (key:line):
- [R] `reports/quant/2026-11-27-v66-robustness.md` (revised) · [H] `reports/quant/2026-11-28-v66-hk-execution.md` (revised) · [T] `reports/quant/2026-11-27-v66-robustness-tom-review.md`
- [I] `reports/quant/2026-11-26-v66-income-study.md` · [D] `memory/decisions/2026-11-24-swing-v66-release.md` · [S] `reports/quant/2026-11-27-shadow-log-setup.md` · [RM] `strategy/v6.6/README.md`
- [R3] `reports/risk/2026-11-26-v66-6-verification.md` · [VaR] `reports/risk/2026-11-27-bprime-var.md` · [P] `config/portfolio.yaml` · [L] `config/risk-limits.yaml`

No broker call was made. "(est.)" marks my own arithmetic on cited inputs.

## Vote: RETIRE, on the chair's Q-3 terms

1. **Portfolio fit: V6.6 has nowhere to go.** The targets have no sleeve for it (AI 30, Technology 20, ETFs 20, Cash 30 [P:10–14]), so real money would come out of strategic cash. That swaps cash at 4.49%/yr for a system that made 3.29% in the backtest [R:42] and trails T-bills by 1.06–1.57%/yr when traded from HK [H:20–21]. It also adds drawdown: −3.49% absolute, −6.66% vs T-bills [R:47–48]. The result is lower return with more risk. Its universe includes NVDA, AVGO, AMD, MU and PLTR [R:114], so it would count against the 40% AI-cluster cap [L:15]. No portfolio-level component VaR exists, because the config holds no real positions (`holdings: []` [P:27]). Mo Peter's only V6.6 figure covers the sleeve alone (B′ book, 1-day VaR95 2.18% of the account [VaR:27]).

2. **Even the best case only matches T-bills, so more testing buys little.** With no minimum fee the system makes +0.18%/yr over T-bills, "still not enough to call it an add-on" [R:28, R:55]. At the estimated US$0.35 fee it is S4: no trading at any cap [I:317; RM:204]. The best calendar year (2025, +1.66% [R:66]) was worth about HK$208 on HK$12,500 (est.). R-3 caps the sleeve at 10% of LNW [R3:121]. Retiring can be undone: the code is archived, `ledger/` is kept, and Q-3 sets the route back.

3. **The Owner's time is the real cost of KEEP.** A bull market means about 66–70 manual orders a year [I:254]. The Owner must be at the screen at the US open (21:30 HKT in US summer, 22:30 HKT in winter) for every entry, or no order is placed (R-6 [D:271]). The same applies to every exit: cancel the stop, sell, and re-place the stop if the sale does not fill [H:36–39]. The HK-2 test had 128 entries and 63 next-open exits in about 4 years [H:20, H:67]. That is about 48 late nights a year (est.), and cancelled entries add more. Paper trading costs the same nights as real money and earns nothing. The cost is near zero today because SPY has been below its 200-day average since 19 Nov [pack:33], but it returns with the next bull market.

4. **If retired, where the HK$12,500 could sit (options, not advice):**
   - **(a) Futu cash interest.** Futu pays interest and Webull does not (Owner, 26 Nov [D:251]). The rate was "not provided" [I:367], and the tax treatment has not been obtained [D:275]. There are no trades and no ETF withholding. It beats (b) if its rate is above about 70% of the T-bill yield at the time, before the ETF's fees and FX costs (est.).
   - **(b) T-bill ETF.** Bills of up to 3 months are allowed under R-1. It earned 4.49% gross over the window, about 3.12% after 30% withholding [I:61, I:364], less two commissions and an HKD/USD conversion cost that is not quantified [I:259–262].
   - **(c) Time deposit or government money-market fund.** R-3 also names these; no yields are on file [I:286].
   - **Leaving it in Webull cash** earns 0%: the −1.03 pp reserve drag in [R:43].
   - **If this is living-cost money for the next 12 months,** R-3 puts it "in an account separate from any trading account" [R3:119]. The Futu account holding 6160/3416 is a trading account.

5. **Conditions:**
   - Q-3 is carried out in full, and Q-4 applies whatever the vote. 腦大裝草 records the decision before anything is archived (rule 4).
   - `config/portfolio.yaml` does not change: V6.6 never had a sleeve, so So Ma, Zac and 死潘狗 have no task.
   - **Re-activation:** on top of Q-3, I would propose a sleeve only on a fresh run that beats T-bills on the HK-2 basis, at the real V-1 fee, on a universe fixed in early 2022 [R:130–133], inside the R-3 cap [R3:121] and the AI-cluster cap [L:15].
   - **Q-7:** the 2022-universe test waits for a re-activation request.

6. **Dissent against my vote:** KEEP costs no money [pack:37] and almost no time while SPY is below its 200-day average. Paper trading plus the shadow log is the only route to forward evidence [R:141]. Tom reads the record as "no edge", not a negative edge [T:109]. The standing CRO and CEO recommendation is (B), shadow-only [I:315–317].
   - **My second choice is KEEP WITH CHANGES:** (B) shadow-only with no paper orders, so the Owner spends no nights at the open.
   - It would retire automatically if V-1 shows S4, which is my answer to Q-6.
   - It still needs the Owner to add the Webull connector [S:28–32], and no AI usage cost is on file [pack:57].

*Research and decision support, not financial advice. Markets cannot be reliably predicted. Backtest figures are history, not forecasts. No agent of this firm places orders.*
