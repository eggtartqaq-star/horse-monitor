# CRO Sign-off — V6.6 release of the Owner's swing system

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-24
**Subject:** Release sign-off for `strategy/v6.6/` against my ruling `reports/risk/2026-11-24-swing-notional-cap-cro.md`
**Status:** FINAL, 2026-11-24. Verdict, conditions and gate owners in §0, §6 and §8.

---

## 0. Verdict

**SIGNED OFF WITH CONDITIONS, for release with cap A (10% flat) live and B′ off.** Scope: fingerprint `69b0780a3d5b` / HEAD `4d0b69e` (§1).

1. **Cap A is structurally enforced; B′ is structurally gated** (§2).
   - A lives in one function and is asserted at 10%.
   - B′ cannot be switched on unless both switches are set, all four gates are marked passed and a CRO note is filled in.
   - B′ sizing matches my definition exactly, at every boundary I probed.
   - All six of my V-2 test cases are in `selftest.py` and pass (47/47).
   - Qualifications: the gates are self-declared, the checks are `assert`s that `python -O` removes, and turning B′ on would not reach the scanner. These are pre-B′ items, not release blockers.
2. **G-1 is MET and recorded** (§4). The Owner's 2026-11-24 decisions align the live list with the validated rules, and the code matches the backtest on 85,120 real-data checks with 0 differences.
3. **The shadow ledger implements my forward test in design** (§3):
   - A, B′ and D sizes are logged for every signal, blocked ones included;
   - S1 to S3 are checked on real fills;
   - review needs 30 closed E2 signals and 6 months;
   - there is no cap comparison at any n.

   **Gaps in it:**
   - The 6-month clock can be contaminated by as-of rows (one 2025-06-16 day read "17.3/6 months") and by partial-bar rows.
   - The S2 detector misses a third position, a self-chosen tighter stop and a stale signal.
   - S4 is a proxy with the wrong consequence.
   - **Earnings-inside-hold is NOT implemented. Only the next earnings date at signal time is stored.**
4. **Two display paths invite trading the retired scanner path** (§5).
   - When selftest fails, the launcher tells the Owner to use the old V6.4.2 scanner.
   - The bot prints a share count for scanner-only signals.
5. **Leverage: V6.6 does nothing about the July CL-1 cash-account issue.**
   - The only Webull account the firm has seen is a margin account with a USD debit (13 Nov).
   - V6.6 sizes off a constant HK$10,000, cannot see the real account, and a margin account would silently fund any shortfall.
   - **Escalated to the CEO and the Owner (third time).** No V6.6 entry may go into a margin account carrying a debit (C-6, restating my 17 Nov ruling).

**Conditions** (full text §8):
- **Pre-switch:** C-1 launcher fallback removed; C-2 bot shows no plan or size off the bt path; C-3 ledger integrity; C-4 complete S2 detector; C-5 sign-off pinned to the fingerprint, with re-verification after Tom's fixes.
- **Standing:** C-6 no margin or debit; C-7 real account base; C-8 limit-order cap at the fill; C-9 system stops recorded and never lowered; C-10 manual monthly breaker.
- **Before B′:** B-1 to B-9.

**Risk score input:** 72 as delivered → 76 after C-1 to C-5. B′ unchanged at 74 conditional (§9).

This is research and decision support, not financial advice. The Owner places every order; no V6.6 code can place one.

## 1. Inputs read and checks run

Reviewed state: **HEAD `4d0b69e`, core fingerprint `69b0780a3d5b`**. `git status` was clean for `strategy/v6.6/`. This sign-off applies to that state only (Condition C-5).

| Input | Status |
|---|---|
| My ruling `reports/risk/2026-11-24-swing-notional-cap-cro.md` (§0, §4.3, §5 gates and forward test, §7) | Re-read; it is the standard for this sign-off |
| Approved plan `/root/.claude/plans/vast-beaming-lynx.md` (Owner decisions; Phases 0–6; Verification) | Read in full |
| `strategy/v6.6/`: `config_v66.py`, `sizing_v66.py`, `signals_v66.py`, `guardrails_v66.py`, `daily_scan_v66.py`, `ledger_v66.py`, `telegram_bot_v66.py`, `selftest.py`, `README.md`, `掃描_v66.bat`; plus `rules_v642.py::position_plan_ccy`, the `lab.py` configs and `simulate`, and the `equivalence_check.py` source | Read |
| `pine/swing_v66.pine` (inputs and sizing lines only) | Grepped for oversizing paths |
| `config/risk-limits.yaml` | Read. It governs the firm book; the swing limits are the Owner's personal limits (ruling §4.3). Unchanged. |
| `config/portfolio-webull-snapshot-2026-11-13.yaml`; my rulings of 16 Nov and 17 Nov (leverage) | Read for CL-1 |
| Tom's release code review `reports/quant/2026-11-24-v66-release-code-review.md` | **Skeleton only, every section `_pending_`.** Tom's review is not done (see C-5). |
| Mo Peter (VaR) / Mario (stress) | Not delivered. These are still the open items commissioned in ruling §5. |

**Checks I ran** (all offline and read-only; scratch output under `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/cro2/`):

| # | Command / probe | Result |
|---|---|---|
| K-1 | `python3 -I selftest.py` | **47/47 pass, exit 0** |
| K-2 | `python3 -I equivalence_check.py` (Webull CSVs in `strategy/v6.6/data/`) | **85,120 comparisons, 0 differences** between `signals_v66` and `lab.build_signal` across both paths (selftest on synthetic data: 39,520, 0) |
| K-3 | `daily_scan_v66.py --source csv --asof 2025-06-16 --ledger …/cro2/ledger_0616` | Stamp correct (V6.6.0, `69b0780a3d5b`, path bt, cap A, B′ off, gates outstanding V1/V2/V3). 15 ledger rows. Live list: MU #1, 1 share, $120. Scan-only: META. Blocked: 8. |
| K-4 | `ledger_v66.py resolve --source csv` and `review` on K-3's ledger | Ran. Review clock read **17.3/6 months** from one as-of day (§3) |
| K-5 | `probe_cfg.py`: `check_config()` under altered settings, normal and `-O` | Gates hold normally. **Under `python -O` every check passes** (§2) |
| K-6 | `find_scanonly.py`: bot `analyze()` on a scan-only signal (NKE, data to 2025-08-29) | Bot prints a trade plan and "建議股數(上限 A): 1股" before "唔入場" (§5) |
| K-7 | `ledger_v66.py fill open` probes on a copy of K-3's ledger | Five concurrent open positions, a blocked signal with a self-chosen stop, and a stale signal were all accepted with **no flag** (§3, §5) |

Account constants (`config_v66.py`): HK$10,000 ÷ 7.8 = US$1,282.05; 10% = US$128.21; 15% = US$192.31 (exactly 192.3077); 1% = US$12.82 (exactly 12.8205). All derived.

## 2. Ruling 1 — cap A live, B′ structurally gated, B′ sizing, V-2 test cases

### 2.1 Is A (10%) structurally enforced as the live mode? **YES.**

- **The cap lives in one place.** `sizing_v66.size()` → `rules_v642.position_plan_ccy(…, CAP_A_PCT)`: shares = min(⌊US$12.82 ÷ per-share risk⌋, ⌊US$128.21 ÷ price⌋). This is the V6.4.2 formula, and it is the cap my ruling priced.
- **Three of the four front-ends size through it.** The scanner prints `size_A` only (`daily_scan_v66.py` L146, L203/L207) and sends 0-share signals to "③ 被擋" (L172–174). The bot calls `size(…, live_mode())` (L150). `ledger fill` flags any notional above 10% at the fill price as `S2` (L110–114). The fourth, Pine, is outside this rule; see R-5.
- **`check_config()` locks the parameters.** It asserts `CAP_A_PCT == 10.0`, `CAP_BPRIME_PCT <= 15.0`, `MAX_POSITIONS == 2`, `RISK_PCT == 1.0` and `LIVE_PATH == "bt"`. The stamp, `live_mode()`, `ledger main` and the bot all call it. Probe K-5 confirmed it **blocks** CAP_A_PCT = 15, CAP_BPRIME_PCT = 20, MAX_POSITIONS = 5 and LIVE_PATH = "scan".
- **The launcher re-proves it before every scan.** `掃描_v66.bat` runs `selftest.py` first and exits on failure. Selftest asserts `live_mode() == "A"` and that A blocks E2 at $150 with a 7% stop.
- **Any edit is visible.** Every edit to the config or a rule file changes the stamped fingerprint (selftest §5).

### 2.2 Is B′ structurally impossible to enable without G-1, V-1, V-2, V-3 and a CRO note? **YES under normal invocation, with four qualifications.**

`check_config()` under altered settings (K-5):

| Attempt | Result |
|---|---|
| `CAP_MODE="B_PRIME"` only, or `B_PRIME_ENABLED=True` only | BLOCKED ("要一齊改") |
| Both set, gates V1/V2/V3 still False | BLOCKED (lists the outstanding gates) |
| Both set, all four gates True, `B_PRIME_CRO_NOTE=""` | BLOCKED |
| Both set, all four gates True, note = `"x"` | **ACCEPTED** |
| Shadow-only constants: `CAP_D_PCT=50`, `MONTH_BREAKER_PCT=50`, `ACCOUNT_HKD=100000`, `E1_LIVE` anything | ACCEPTED (not asserted) |

**Qualifications:**

1. **The gates are self-declared.** `GATES` holds four booleans the Owner types in. Only V-2 is re-proved by machine on each run: the launcher runs selftest. V-1, V-3 and the CRO note are trusted. Any non-empty string passes as the note; nothing checks that it names a real CRO file or a date. That is acceptable for an Owner's personal limit, since he may override me (CLAUDE.md rule 2). It is a speed bump with an audit trail, not proof. → B-4.
2. **Every check is a Python `assert`, and `python -O` or `PYTHONOPTIMIZE` removes them.** Under `-O`, all eight altered configs in K-5 were ACCEPTED, including CAP_A_PCT = 15 and CAP_BPRIME_PCT = 20.
   - Mitigation: through the launcher, selftest check "關卡未過 → 開 B′ 會被 assert 擋" would then fail, so the launcher would refuse to scan.
   - Not mitigated: running `daily_scan_v66.py` or `telegram_bot_v66.py` directly.
   - → B-3. This is not release-blocking under A, because reaching it takes a deliberate config edit, which changes the fingerprint.
3. **Turning B′ on would not reach the scanner.**
   - The scanner never calls `live_mode()` for sizing. With B′ on, it would still show only A sizes and would still list B′-tier E2 signals as "買唔起". Meanwhile the bot would show 1 share and `ledger fill` would accept it as "B'例外".
   - Three front-ends would disagree. That is safe today, but a B′ switch that does not switch the trade list is not a defined system. → B-2.
4. **`size(mode="B_PRIME")` ignores the flag by design.** It is a pure function, so the shadow ledger can log B′ sizes while B′ is off. That is correct. The gate is `live_mode()`, not `size()`.

### 2.3 Does `sizing_v66.size` implement B′ exactly as I defined it? **YES.**

My definition (ruling §4.3): E2 only; exactly 1 share; only when A gives 0; notional ≤ 15% (US$192.31); that one share's risk to the stop ≤ 1% (US$12.82). Code at L36–39: `if mode == "B_PRIME" and sh == 0 and engine == "E2": if entry <= acct*15/100 and (entry - stop) <= risk_budget: sh = 1`.

Boundary probe (K-5):

| Case | A | B′ | D (shadow) |
|---|---|---|---|
| E2 $192.30, stop $180 | 0 | **1** (15.0%) | 1 |
| E2 $192.31 (= 15.0002%) | 0 | **0** | 0 |
| E2 $150, risk/sh $12.82 | 0 | **1** (11.7%) | 1 |
| E2 $150, risk/sh $12.83 | 0 | **0** | 0 |
| E2 $128, risk/sh $8 | 1 (9.98%) | 1, rule A10 | 1 |
| E2 $129, risk/sh $9 | 0 | **1** (10.06%) | 1 |
| E2 $40, risk/sh $1 | 3 (9.36%) | **3, rule A10 (no multi-share > 10%)** | 4 (12.48%) |
| E1 $150, stop 7% | 0 | **0** (E1 never gets the exception) | 1 |

The 15% test is strict ("≤ 15.0000%"). My "US$192.31" was 192.3077 rounded, so a share at exactly $192.31 is correctly blocked. **No deviation from my definition.**

One latent note: in `currency="HKD"` mode, B′ would allow "1 share ≤ HK$1,500", which ignores HK board lots. HK tickers are blocked from trading in the bot ("港股…唔做") and are not in the scanner universe, so this is not live. → R-4.

### 2.4 Do the six V-2 test cases in `selftest.py` match my list? **YES, all six, and all pass.**

| My V-2 case (ruling §5) | `selftest.py` L131–133 (mode B_PRIME) | Got |
|---|---|---|
| $200 stock, 2% stop → BLOCK | E2, 200 / 196 → 0 | 0 ✅ |
| E2 $150, 7% stop → 1 share | 150 / 139.5 → 1 | 1 ✅ |
| E1 $150, 7% stop → BLOCK | 150 / 139.5, E1 → 0 | 0 ✅ |
| E2 $195 → BLOCK | 195 / 190 → 0 | 0 ✅ |
| E2 $185, 7.5% stop (1-share risk $13.88) → BLOCK | 185 / 171.125 → 0 | 0 ✅ |
| $60, 5% stop → 2 shares, not 3 | 60 / 57, E2 → 2 | 2 ✅ |

The two cases where my list named no engine are tested as E2, the more permissive engine, so they are the stronger test. Selftest also checks that A blocks E2 at $150 with a 7% stop, that D gives 3 shares at $60, that `live_mode() == "A"`, and that B′ is blocked while gates are outstanding.

**Also confirmed from V-2:**
- The CEO README's `assert E.MAX_POSITION_PCT == 10.0` is replaced, not deleted: `check_config()` now asserts CAP_A_PCT == 10.0 and is called from the stamp.
- The scanner prints its signal path on every run.

**Not covered by selftest:**
- the empty-note case and the mode/flag mismatch, which I probed by hand (K-5);
- the `-O` case.

→ B-3.

## 3. Ruling 2 — shadow ledger vs the pre-registered forward test

**Overall: FAITHFUL IN DESIGN, WITH THREE INTEGRITY DEFECTS AND ONE ITEM NOT IMPLEMENTED.**

| My forward-test requirement (ruling §5) | V6.6 implementation | Ruling |
|---|---|---|
| **Sizes under A, B′ and D logged for every signal, traded or not** | `daily_scan_v66.scan()` builds a row for every path-qualified signal **before** the live/blocked split (L142–168). Each row carries `size_A`, `notional_A`, `size_Bp`, `rule_Bp`, `size_D`, `guard_ok`, `guard_reason` and the version and fingerprint. K-3 (2025-06-16): 15 rows, every blocked signal included, e.g. NVDA E2: A 0 / B′ 1 (`B'1share`) / D 1; JNJ E1: A 0 / B′ 0 / D 1. Signals are keyed (bar date, ticker, path) and written append-only. Repeat signals on a held name are not double-counted, because `lab.simulate` skips held tickers. | **MET** |
| **S1**: an exception-tier position loses > 2.0% of the account | `review()` L268–269: closed fills flagged `B'例外` with P&L after fees < −2% × US$1,282.05. Selftest checks it. Measures closed positions only; open marks are not checked. | **MET** (inert while B′ is off) |
| **S2**: any sizing breach (multi-share > 10%, E1 using the exception, a share > US$192.31) or an unstamped / scanner path | `cmd_fill` L110–130: notional > 10% at the fill price → S2 unless it is a valid B′ exception (E2, 1 share, ≤ 15%, 1-share risk ≤ 1%, B′ enabled); risk > 1.05% → S2; a fill with no prior live-path signal → S2 (K-7: META scan-only → `S2:冇 live 訊號(scan_only)`; CAT 1 share at $128.50 → `S2:名義10.0%超上限`). **Gaps, from probe K-7:**<br>(a) **No concurrency check.** Five open fills were recorded without a flag, against `MAX_POSITIONS = 2`.<br>(b) **A blocked live signal counts as "live".** AMD (signal stop $112.10, 11.3%, A = 0 shares) was recorded with a **self-chosen $116 stop** and no flag. Tightening the stop manufactures a size the system refused. The same path accepts an earnings-blocked signal, because `live == True` regardless of `guard_ok`.<br>(c) **Stale signals are accepted.** A 2025-06-16 MU signal sourced a 2025-08-20 entry with no flag. | **PARTIAL** → C-4 |
| **S3**: the −10% monthly breaker trips while an exception position is open | `review()` L272–281: realized P&L by close month ≤ −10% with an overlapping `B'例外` fill. Selftest checks it. Realized only, no open marks; the scanner itself does not enforce the breaker (§5). | **MET** as a review check (inert while B′ is off) |
| **S4**: V-1 shows net EV ≤ 0 at the real fee | `review()` L284–285 uses a **proxy**: V-1 flag True, ≥ 10 closed fills and realized net ≤ 0. My S4 is the `as_traded` re-run at the real fee (Tom), which the ledger cannot do. The proxy errs toward tripping, which is acceptable as an extra tripwire. The consequence printed is wrong: "返去 A". Under V-1, net EV ≤ 0 means **no new entries at any cap**, not a reversion to A. Fees are recorded on every fill, which builds V-1 evidence. | **PARTIAL** → B-9 |
| **Review horizon: ≥ 30 closed E2 and ≥ 6 months, whichever is later** | `review()` L240–245: `len(e2) >= 30 and months >= 6`. Counts closed live-path E2 **shadow signals** (every signal, unconstrained), not Owner trades. That is the plan's reading and is acceptable, because the forward test is a shadow test. **Defect:** the 6-month clock starts at the earliest `bar_date` in `signals.csv`, so any as-of row moves it. K-4: **one 2025-06-16 as-of day produced "17.3/6 months"**. The plan's own Verification step 4 runs four as-of scans; without `--dry-run` or `--ledger` those rows land in the live ledger (`main()` has no guard). Separately, **partial-bar rows pre-empt the correct close rows**: a run during the US session writes a row flagged `partial_bar`, the idempotent key then rejects the correct post-close row, and `resolve` does not filter `partial_bar`. | **DEFECTIVE** → C-3 |
| **No cap return comparison before 100 forward trades** | `review()` §【2】 prints only the count of B′-only signals (K-4: 1) and the rule text. No A/B′/D return comparison is computed at any n. §【1】 prints per-path/engine means with a "⏳ 未夠,唔好下結論" label; that is a path comparison, not a cap comparison. | **MET** (stricter than required) |
| **Earnings inside the hold logged** for every exception-tier position | **NOT IMPLEMENTED. Only the earnings date is stored.**<br>- `guardrails_v66.check()` stores the **next** earnings date as of the signal day in `signals.csv` (`earnings_date`, `days_er`), and only in live yfinance runs: it is `off` in as-of runs and blank when the lookup fails.<br>- `fills.csv` has no earnings field.<br>- `review()` never compares an earnings date with a hold window.<br>- The plan's line "Earnings inside the hold are flagged" (Phase 2) was not delivered. The README does not claim it.<br>- While A is live there are no exception-tier positions, so the requirement has no live object yet. The input is being captured, so it can be computed retroactively for live-mode rows. | **NOT MET**: required before B′ (B-5) |

**The forward test is sound in design.**
- It logs A/B′/D for every live and shadow signal.
- It keeps edge (shadow) and risk (real fills) separate.
- It refuses early cap comparisons.

**Its integrity depends on C-3 and C-4.** A ledger that as-of rows can contaminate, or a breach detector that misses a third position or a self-chosen stop, would let the forward test pass for the wrong reason.

## 4. Ruling 3 — G-1 status

**G-1 is SATISFIED, as of 2026-11-24. Recorded.**

My G-1 (ruling §5): "The Owner decides whether the live scanner is aligned to the validated rules (E2 breakout gate, E1 as backtested) or stays as it is. **Aligned to the backtest path: adopt B′ once V-1 to V-3 pass.**"

**The Owner's decisions (2026-11-24, plan "Owner's decisions" 1–2):**
- The validated **"bt" path is the live list**: E2 requires today's high ≥ the 20-day high.
- The old scanner path is **logged only**.
- **E1 is traded exactly as backtested**: score ≥ 0.55, R ≥ 2, all tiers. E2 has slot priority.

This is the "aligned" branch of G-1, as a decision.

**Evidence that the code implements that decision:**

| Requirement | Evidence | Result |
|---|---|---|
| Live path = bt, enforced | `config_v66.LIVE_PATH = "bt"`, asserted in `check_config()`. K-5: LIVE_PATH = "scan" → BLOCKED | ✅ |
| E2 breakout gate on the live path | `signals_v66.on_path`: `path == "bt" and not breakout → None`. Selftest: no breakout → bt rejects, scan accepts; high = 20-day high → both accept | ✅ |
| E1 all tiers, R ≥ 2, stop ≤ 15% on the live path | `on_path`: the strong-only filter applies to `scan` only; `mr_plan` enforces R ≥ 2; `MAX_STOP_PCT_MR` = 15% | ✅ |
| E2 slot priority, then score | `signals_v66.rank_key` = (E2 first, −score), the same as `lab.simulate`'s candidate sort | ✅ |
| Scanner = backtest, every day, ticker and path | **K-2: 85,120 real-data comparisons, 0 differences**; 39,520 synthetic, 0 | ✅ |
| Path stamped on every run | Stamp line "交易路徑: bt(回測驗證版) 影子路徑: scan(只記錄)" plus fingerprint (K-3) | ✅ |
| Old path cannot be traded silently | Scanner section ② labels it "只記錄,唔交易". `ledger fill` flags S2 on a scan-only source (K-7). **But** the launcher's failure message tells the Owner to fall back to the old V6.4.2 scanner (§5). | **Gap → C-1** |

**Consequences of G-1 being met:**
1. Ruling §5 put B′ on the "aligned" branch. B′ is now waiting only on **V-1, V-3, a B′-ready V-2 (B-2, B-3) and my dated note.** The scanner-path V-0 failure no longer governs the live account, because that path is logged, not traded.
2. **The scanner path's cap is not re-decided here.** If the Owner ever wants to trade the scanner path again, it falls under the pre-registered test in ruling §5: beat 10% flat in at least two-thirds of perturbed runs in each half, with a worst trade no worse than −1.5%, on forward data.
3. **One residual difference from the backtest:** the live list adds the earnings guardrail (blocks entries 0–5 days before earnings), which no backtest has (ruling §3.4). It removes signals, so it cannot add risk.
4. `config_v66.GATES["G1_路徑已定"] = True` is consistent with this record.

**Note: G-1 does not validate the system's return.** Corrected lab, bt path at 10%: 2.21% CAGR ALL / 1.82 IS / 2.62 OOS (ruling §2, `bt/results2/caps.csv`). That is small and, per the README, "同零分唔開". G-1 resolves which system is live; it does not show that the system earns money after real fees. That is V-1.

## 5. Ruling 4 — oversizing, scanner-only trades, stop bypass, leverage / margin (CL-1)

### 5.1 Could V6.6 lead the Owner to oversize?

| Path | Finding | Severity → action |
|---|---|---|
| Scanner trade list | Shows **only** the A size and notional (`daily_scan_v66.py` L203/L207). B′ and D sizes are never printed. | None |
| Bot | Shows only the `live_mode()` size (A). B′ and D are not shown. | None |
| `ledger_v66.py show` | Prints the last 30 rows of `signals.csv` with **every** column, so `size_Bp` and `size_D` are visible next to `size_A` with no "shadow" label. | Low → R-1 |
| Fill above the cap at the open | The scanner sizes at the signal close and the fill check measures at the fill price (K-7: CAT, 1 share at $128.50 = 10.02% → S2). This is correct under my S2, and `lab.simulate` also re-sizes at the open. But the README only says to recompute when the open deviates by more than 1%, so a near-cap name can open a few cents high and become a breach. | Medium → C-8 (limit-order rule) |
| Self-chosen tighter stop | Probe K-7: AMD was blocked (system stop 11.3%, so 1-share risk > US$12.82). It was recorded with a tighter stop at $116, accepted, no flag. This is how a refused size gets manufactured. | **High → C-4(b), C-9** |
| Account constant | `ACCOUNT_HKD = 10000` is a constant (not asserted). Every limit is a % of it, and **V6.6 never compares it with actual equity.** If the trading account holds less, every limit loosens in real terms (see 5.4). | **High → C-7** |
| Pine | `MAX_POSITION_PCT` and `RISK_PCT` are `input.float` (L21, L23) and can be edited in TradingView's settings. They are outside the fingerprint, and changing them changes both the share count and whether a signal shows (`sharesE1 >= 1` gates the E1 signal, L87). | Low → R-5 |

### 5.2 Could V6.6 lead the Owner to trade the scanner-only list?

1. **Launcher fallback: HIGH.**
   - When selftest fails, `掃描_v66.bat` prints "臨時可以用返舊版:掃描.bat(V6.4.2)", i.e. "meanwhile you can use the old V6.4.2 scanner".
   - That old scanner runs the **unvalidated scanner path** (no E2 breakout gate, strong-only E1). It is also the scanner whose 6 and 28 Sep output showed CVX ≈ 16% and PFE 8 shares ≈ 18% (ruling §7.6).
   - So at the moment the structural control fires, the launcher tells the Owner to route around it, to the path G-1 just retired. → **C-1**
2. **Bot shows a plan for scan-only signals: MEDIUM.**
   - Probe K-6, NKE, data to 2025-08-29: E2 with "突破20日高: ❌". The bot printed "── 交易計劃 ──", entry, stop and "建議股數(上限 A): 1股 (~75)", then "🚫 唔入場: 只係舊掃描器路徑先有".
   - A share count on a signal the system says not to trade is an invitation. The same applies to HK tickers, where the bot prints an HKD share count (ignoring board lots) and then "港股…唔做". → **C-2**
3. **The scanner does this well.** Section ② lists scan-only names with **no** size or plan, labelled "只記錄,唔交易". `ledger fill` flags S2 if one is traded (K-7: META).

### 5.3 Could V6.6 lead the Owner to bypass a stop?

- **Initial stop.** The system stop is printed, and the README tells the Owner to place the stop order immediately after the fill. `ledger fill` accepts **any** `--stop` and never compares it with the logged signal stop. → C-4(b).
- **E2 trailing stop.** Section ④ computes "今日止蝕" as max(initial stop, highest since entry − 3×ATR), only rising. That matches `lab.simulate`. Two caveats:
  1. It mixes `auto_adjust=True` yfinance bars with the **unadjusted** fill price and stop from `fills.csv`. After an ex-dividend date the adjusted highs fall slightly, so the displayed trail is slightly **loose**. A split during the hold makes it plainly wrong. → R-3
  2. It only appears if the fill was recorded. An unrecorded trade has no trailing stop on screen. → C-9
- **Exit adherence.** Nothing compares an actual exit with the shadow exit for the same signal. A position held through its stop is not detected. → R-2
- **No code path moves a stop down**, and V6.6 has no broker write path (no order placement anywhere; yfinance reads only). CLAUDE.md rule 1 is respected.

### 5.4 Leverage / margin: does V6.6 address the July CL-1 cash-account issue? **NO. Nothing in V6.6 addresses it. Flagged and escalated (third time).**

- **The history.**
  - My July ruling made **CL-1: "Cash-only account, margin disabled… Written broker confirmation on file"** (`2026-07-30-v64-risk-review.md`, CL-1 table), after the 2026-07-18 BAC order that breached `leverage: none` by at least 2.3x.
  - The advice was repeated on 10 Aug (3416 review).
  - On 16 Nov the Webull debit was found to be a breach on its face and escalated. On 17 Nov it was escalated again, with the standing ruling **"No new position of any kind may be opened in the Webull account while it is a margin account with a debit"** (`2026-11-17-mu-skhy-style-cro.md`, item 5 / G-3).
- **What the firm last saw** (`config/portfolio-webull-snapshot-2026-11-13.yaml`, read-only pull 2026-11-13):
  - `account_class: INDIVIDUAL_MRGN`, HKD base;
  - USD cash **−12.06**, HKD cash 0.01;
  - 2 AVGO, `decision_record: NONE`;
  - market value HK$5,396.44, cash balance −HK$94.35.
  - **Status since 13 Nov: NOT OBTAINED.**
- **Why this matters for V6.6 specifically.**
  - V6.6 sizes against a constant HK$10,000. It has no idea of real cash, equity or account type, and by design it has no broker access.
  - In a margin account the broker funds any shortfall without asking, so V6.6's "1% risk, 10% notional" could be placed on borrowed money with no error anywhere.
  - V-1 asks for a *Webull* contract note, which implies the swing system trades at Webull. The Owner has not confirmed which account it uses.
- **If the swing system trades in that account** (an assumption, to be confirmed):
  - Equity on 13 Nov was about HK$5,302.09 (HK$5,396.44 − HK$94.35; derived, accrued interest NOT OBTAINED).
  - So V6.6's 1% (HK$100) would be about **1.89%** of real equity (derived).
  - Any new buy would deepen a USD debit.
  - The AVGO position (2 × US$344.87 = US$689.74 = 53.8% of the configured US$1,282.05; derived) is not in the ledger, so V6.6's 2-slot count and "持倉中" tags cannot see it.
- **What the remedy has to be.** Under CLAUDE.md, controls must be "structural, not behavioural". The control is broker-side: a cash account, or margin disabled in writing. A line printed by the scanner would be behavioural. → **C-6, C-7; B-8 before B′.**

## 6. Ruling 5 — remaining gates, owners, and the conditions for enabling B′

### 6.1 Gate register

| Gate | What closes it | Owner | Status (2026-11-24) |
|---|---|---|---|
| **G-1** Path defined | Owner's decision + code evidence (§4) | Owner | **MET**, recorded here |
| **V-1** Real costs | One Webull contract note (commission, platform fee, SEC/TAF, FX) → Tom re-runs `as_traded` at that fee → net EV > 0 → CRO reads | Owner (note); Tom (re-run); John (read) | **OPEN** |
| **V-2** Code tests | Selftest passes in the cloud (K-1: 47/47 at `69b0780a3d5b`) **and on the Owner's PC**. For B′ it must also include B-2/B-3 tests. | Owner (PC run); Tom (tests) | **PARTIAL**: cloud pass; PC run and B′-ready tests outstanding |
| **V-3** Parity | `parity_check.py` passes on the Owner's PC with Tom's F-6 metric (≥ 98% on signal days per path; \|ΔADX\|, \|ΔDI\| < 0.01 after bar 250) | Owner (run); Tom (read output) | **OPEN** |
| Tom's release code review | `reports/quant/2026-11-24-v66-release-code-review.md` completed and committed | Tom | **OPEN** (skeleton only) |
| Docs audit | Plan Phase 5 | Ai 管理層 | **NOT SEEN** |
| Pre-switch fixes C-1 to C-4 | §8; each with a selftest case | CEO / Tom (code); John (verify) | **OPEN** |
| VaR / stress | Mo Peter: 1-day VaR95 of the maximum-exposure B′ book vs 3%. Mario: replay of 2024-08-05 at maximum B′ exposure; −40% single-name gap (assumption); −10% index gap with both slots in one sector | Dept 6 (Mo Peter, Mario); John | **OPEN** (commissioned in ruling §5) |
| CL-1 cash account | Broker confirmation of cash / margin disabled for the account the swing system trades; no debit | Owner | **OPEN since 2026-07-30**; escalated 16 Nov, 17 Nov, and here |
| CRO 7.6 | Owner confirms whether any order was placed from the 6 / 28 Sep scans | Owner | **OPEN** |
| Telegram token | Revoke and regenerate before the bot runs (plan Phase 0) | Owner | **OPEN** |
| Decision record | `memory/decisions/` entry (CLAUDE.md rule 4) | 腦大裝草 | **OPEN**: 5-line summary in §10 |

**The Owner may switch to V6.6 with A live** once:
- C-1 to C-5 are closed and verified;
- Tom's review and the audit are committed (plan Verification 9);
- the Owner's PC passes selftest.

V-1 and V-3 do **not** block the switch to A. They gate B′, and V-1 also gates whether the system should trade at all (S4).

**Real-money entries are additionally governed by C-6.**

### 6.2 Conditions for enabling B′ later (all required; the order does not matter)

B′ is enabled by editing `config_v66.py` (`CAP_MODE = "B_PRIME"`, `B_PRIME_ENABLED = True`, all four `GATES`, `B_PRIME_CRO_NOTE`). That edit is permitted **only** after:

1. **G-1** ✅ (§4).
2. **V-1** passed: net EV > 0 at the real fee in Tom's re-run. I note the interaction from ruling §7.4: a fixed fee costs more in % terms on a smaller notional.
3. **V-2** passed on the Owner's PC, **including B-2 and B-3**.
4. **V-3** passed on the Owner's PC.
5. **B-2 to B-9** (§8) closed.
6. **My dated CRO note** (`reports/risk/YYYY-MM-DD-bprime-enable-cro.md`), written after reading the V-1 re-run and the V-3 output. The note's path goes in `B_PRIME_CRO_NOTE`.

After enabling:
- S1 to S4 apply as pre-registered (ruling §5). Any one reverts the account to A immediately, with no re-argument inside the test.
- No raise beyond 15%, and no E1 exception, may be argued on data before 2026-11-24.

## 7. Limit-by-limit check (limit / current / post-release / pass-fail)

These are the swing account's operative limits: the V6.4.2 constants as re-ruled on 2026-11-24. `config/risk-limits.yaml` is shown as the firm reference. "Before" = V6.4.2 tools (old scanner path). "Post-release" = V6.6 at A, as reviewed.

| Limit | Value | Before (V6.4.2) | Post-release (V6.6, A) | Pass / Fail |
|---|---|---|---|---|
| Single position, multi-share | 10% (US$128.21) | Cap in code; Sep scans showed ~16–18% (ruling §7.6) | One sizing function; asserted; S2 at fill (K-5, K-7) | **PASS** |
| Single position, single share | 10% (A); 15% only under B′ | Same as A | B′ off; `live_mode() == "A"`; B′ sizes logged only | **PASS** |
| Max risk per trade | 1% (US$12.82) | In code | Asserted `RISK_PCT == 1.0`; S2 at fill above 1.05% (5% slippage tolerance, disclosed) | **PASS**, but a self-chosen stop evades it (C-4b) |
| Concurrent positions | 2 | Manual | Asserted constant; scanner text says "最多 2 倉"; **not checked at fill** (K-7: 5 accepted) | **PASS in design / GAP in detection** → C-4a |
| Gross exposure / cash floor | ≤ 20% gross at A; cash ≥ 10% | Same | Same (2 × 10%) | **PASS** (software) |
| Leverage | none (CL-1; firm `leverage: none`) | Margin account; BAC 2026-07-18 breach | **Not addressed by V6.6.** Webull margin account with a USD debit as of 13 Nov | **FAIL ON FACE (account, not code)**, escalated → C-6 |
| Account base for % limits | Actual swing equity | Constant HK$10,000 | Constant HK$10,000, never reconciled | **UNVERIFIED** → C-7 |
| Monthly circuit breaker | −10% | Manual | Backtest enforces it (`AS_TRADED.month_breaker_pct = 10`); **scanner does not**; review reports it | **PARTIAL** → C-10, B-6 |
| Drawdown budget | 20% | — | Unchanged from ruling §8 (corrected lab, bt path, A: base −4.49%) | **PASS** |
| Max initial stop width | E2 12% / E1 15% | In code | `trend_plan` / `on_path` / guardrails; equivalence 0 diffs (K-2) | **PASS** |
| Stop discipline (never lowered) | — | Manual | Trail display only rises; no code path lowers it; exit adherence not checked | **PASS** (R-2, R-3) |
| Signal path defined and stamped | bt live; scan logged | **NO** (F-3) | Asserted `LIVE_PATH == "bt"`; stamped; 85,120 / 0 diffs | **PASS** (G-1 met), except launcher fallback → C-1 |
| Version / fingerprint | Stamp on every run | None | `69b0780a3d5b` on scanner, bot, ledger review, every ledger row | **PASS** |
| Broker write path | None (CLAUDE.md rule 1) | — | None; yfinance reads only | **PASS** |
| Cost gate (V-1) | Net EV > 0 at the real fee | Unverified | Unverified; fees now recorded per fill | **OPEN** |
| Firm limits (`config/risk-limits.yaml`) | — | Unchanged | Unchanged | n/a: no change proposed |

## 8. Conditions (numbered, binding)

These are recommendations to the Owner, who is the final authority and places every order. They bind **Zac and 死潘狗** for any ticket or sizing they produce from V6.6. Each code fix lands with a selftest case. I verify C-1 to C-5 before the README tells the Owner to switch.

### A. Pre-switch: before the Owner trades from V6.6 (code/doc; owner CEO/Tom; verifier John)

- **C-1. Remove the launcher's fallback to the old scanner.**
  - Replace "臨時可以用返舊版:掃描.bat(V6.4.2)" in `掃描_v66.bat` with: no new entries today; existing broker stops stand; send `selftest_last.log` to the firm.
  - The old V6.4.2 scanner is never a trading fallback (G-1).
- **C-2. Bot: no trade plan or share count unless the bt path has the signal and it is tradeable.**
  - For scan-only signals, show "只記錄" with no entry, stop or size.
  - Do the same for HK tickers and for blocked signals.
- **C-3. Ledger integrity.**
  - (a) `--asof` runs must not write to the default ledger. Refuse unless `--dry-run` or a non-default `--ledger` is given.
  - (b) Partial-bar runs must not write, or must be superseded by the post-close run.
  - (c) `review()` must start its 6-month clock at the first live-mode row dated on or after 2026-11-24, and exclude rows marked as-of (`days_er == "off"`) or partial-bar from every count.
  - (d) The README's Verification step for as-of scans must say `--dry-run`.
- **C-4. Complete the S2 detector in `ledger fill`.** Flag S2 if:
  - (a) open positions would exceed `MAX_POSITIONS` (2);
  - (b) the source live signal was blocked (`guard_ok` False, or 0 shares under `live_mode()`), **or** the entered stop is tighter than the logged signal stop (tolerance: 1 cent after rescaling);
  - (c) the source signal is not from the last logged bar before the fill date.
- **C-5. Sign-off pinned to fingerprint `69b0780a3d5b` (HEAD `4d0b69e`).**
  - Tom's review may land fixes. Any change to `config_v66.py`, `sizing_v66.py`, `signals_v66.py`, `daily_scan_v66.py`, `ledger_v66.py`, `telegram_bot_v66.py` or the launcher needs three things: selftest passes, equivalence shows 0 differences, and I re-check the sizing, config and fill code.
  - The README's quoted fingerprint must match the released one.

### B. Standing: from the first real-money entry, for as long as V6.6 is live

- **C-6. Leverage (CL-1).**
  - No V6.6 entry may be placed in a margin account carrying a debit. This restates my 17 Nov ruling.
  - Before the first real-money entry, the Owner names the account the swing system trades and shows, from a broker statement or a read-only pull, that it is a cash account or has margin disabled, with settled cash ≥ the order.
  - The Webull account as last read (13 Nov: `INDIVIDUAL_MRGN`, USD −12.06) does **not** qualify. **Escalated to the CEO and the Owner, third time.** Remediation options are unchanged: convert to cash or disable margin (preferred, structural); or clear the debit and fund the swing sleeve in settled cash (behavioural, interim).
- **C-7. The account base must be real.**
  - `ACCOUNT_HKD` must not exceed the swing account's actual net liquidation value, with no borrowed money. Reconcile monthly and after any withdrawal.
  - Any position already in that account is declared to the firm and recorded with `ledger fill`, so the 2-slot count can see it.
- **C-8. Cap at the fill price.**
  - Enter with a limit order where limit × shares ≤ US$128.21 and (limit − system stop) × shares ≤ US$12.82.
  - If the open is above the limit, skip the trade. Do not resize upward.
- **C-9. Stops.**
  - Place a broker stop at the **system** stop immediately after the fill. Never set it tighter to make a size fit, and never lower it.
  - Record every fill with `ledger fill` the same day.
  - For E2, raise the broker stop each day to section ④'s figure.
  - An unrecorded trade is an S2.
- **C-10. Monthly breaker.**
  - The Owner applies the −10% month-to-date realized breaker by hand until the scanner enforces it (B-6).
  - Once tripped, no new entries until the next calendar month.

### C. Before B′ may be enabled (in addition to the gates in §6.2)

- **B-1.** V-1, V-2 (on the PC) and V-3 passed; my dated note issued (§6.2).
- **B-2.** The scanner sizes and filters the live list through `live_mode()` and prints the rule used (`A10` / `B'1share`). Selftest asserts that the scanner, the bot and `ledger fill` agree on the live mode.
- **B-3.** `check_config()` uses explicit `raise SystemExit`, not `assert`. Selftest covers: mode/flag mismatch, empty note, gates outstanding, and a run under `python -O`.
- **B-4.** `B_PRIME_CRO_NOTE` must match `reports/risk/YYYY-MM-DD-*.md`. The V-1 and V-3 flags each carry an evidence reference: the contract-note date, and a hash of the parity output.
- **B-5.** Earnings-inside-hold implemented. For every fill and every B′-tier shadow signal, flag whether an earnings date fell between entry and exit, and show it in `review()`.
- **B-6.** The scanner enforces the monthly breaker from `fills.csv`, suppressing the live list once the month is at −10%. S3 depends on it.
- **B-7.** Mo Peter's VaR and Mario's three stresses delivered and read by me.
- **B-8.** CL-1 cured (C-6 structurally, not behaviourally). If the account is still in the July CL-8 paper phase, B′ runs in paper first.
- **B-9.** S4 corrected. If V-1 (or the ledger proxy) shows net EV ≤ 0 at the real fee, **no new entries at any cap** pending Tom's re-run, not "返去 A". The review text must say so.

### D. Recommendations (not conditions)

- **R-1.** `ledger show`: hide `size_Bp` and `size_D`, or label them "影子—唔准用".
- **R-2.** `review()`: compare each real exit with the resolved shadow exit of its source signal, and flag holds past a stop.
- **R-3.** Section ④ trail: compute on unadjusted prices, or rescale the fill price and stop by the adjustment factor, so ex-dividend and split days do not loosen or distort it.
- **R-4.** HK: suppress HKD share counts (board lots are ignored) while HK is untradeable.
- **R-5.** Pine: make the cap and risk % constants, or show a red warning when they are not 10 / 1.
- **R-6.** Rank numbering in the live list: exclude held tickers, as `lab.simulate` does, so "揀咗第N名" means what it says.

## 9. Risk score input

Scale as in July and in ruling §9: 0 = do not deploy, 100 = clear at full size; higher is safer. These are **risk** scores; upside is not scored.

| Item | Score | Basis |
|---|---|---|
| V6.6 at A, **as delivered** (`69b0780a3d5b`) | **72** | Up from 70 (ruling §9, 10% on the undefined scanner path). The path is now defined, asserted, stamped and equivalent (85,120 / 0); the cap sits in one function; B′ is gated. Held down by the launcher fallback (C-1), the bot's scan-only plan (C-2), ledger contamination (C-3) and S2 blind spots (C-4). |
| V6.6 at A, **after C-1 to C-5** | **76** | Remaining risk: unverified costs (V-1), a small edge (2.21% CAGR, bt path, A), and survivor-sample tails (ruling §3.3) |
| Real-money entries in a margin account carrying a debit | **Not deployable**: standing 17 Nov ruling, C-6 | `leverage: none` is a hard rule; V6.6 cannot see the account |
| B′ | **74, conditional** (unchanged); about 80 once B-1 to B-9 close | Ruling §9. G-1 now met; V-1, V-3 and the B′-ready V-2 are outstanding |

**Committee input:**
- **72 / 100 for the V6.6 release at A, rising to 76 when C-1 to C-5 are verified.**
- **B′ stays off**: 74, conditional.
- Conditions C-6 to C-10 are binding on Zac and 死潘狗 for any tickets.

## 10. Decision summary for `memory/decisions/` (5 lines)

```
2026-11-24 · V6.6 release (swing system) · CRO John: SIGNED OFF WITH CONDITIONS at fingerprint 69b0780a3d5b (HEAD 4d0b69e); risk score 72 → 76 after C-1–C-5.
Owner decisions recorded: bt path (E2 needs 20-day breakout) is the live list; old scanner path logged only; E1 traded as backtested (score≥0.55, R≥2, all tiers; E2 slot priority) → CRO G-1 MET. Cap A (10% flat) live; B′ off.
Evidence: selftest 47/47; signals_v66 = lab on 85,120 real-data checks, 0 diffs; A asserted and enforced in one function; B′ sizing exactly as ruled; six V-2 cases pass. Gaps: launcher falls back to old scanner; bot shows a size on scan-only signals; as-of/partial-bar rows can contaminate the ledger clock; fill misses 3rd slot / self-chosen stop / stale signal; earnings-inside-hold NOT implemented (date only stored); asserts vanish under python -O.
Before switching: C-1–C-5 (code fixes + re-verification; Tom's review, which is still pending). Before B′: V-1 (Webull fee note + rerun), V-2 on Owner PC, V-3 parity, B-2–B-9, dated CRO note. Standing: C-6–C-10.
Dissent/escalation: V6.6 does nothing about CL-1. Webull is a margin account with a USD debit (13 Nov), so no V6.6 entry may go into a margin account with a debit (third escalation, Owner). Lesson: a structural control's failure message must not point to the uncontrolled path.
```
