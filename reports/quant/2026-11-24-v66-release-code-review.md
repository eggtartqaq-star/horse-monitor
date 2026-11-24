# V6.6 release code review — Tom (Backtesting Engineer)

Date: 2026-11-24 · Reviewer: Tom (Dept 3) · Scope: `strategy/v6.6/` at HEAD 4d0b69e (+ fixes listed in §11)
Status: FINAL, 2026-11-24. Reviewed HEAD 4d0b69e (fingerprint `69b0780a3d5b`); fixes in §11 are in the working tree and WIP commit 8e2517a.

## 1. Verdict (per component)

**Overall: NOT READY TO SHIP until F-1 (the .bat) is fixed. The fix is one line.**
- After that fix, and once the Owner sees one real scan run on the PC: **VALIDATED WITH CONCERNS for mode A (10%), bt path live.**
- **B′ stays off.** Besides V-1 and V-3, it also needs F-8 (S4), F-9 (earnings log), F-10/F-11 (fingerprint scope; asserts) and CRO C-2.

The rules are faithful:
- 0 differences in 85,120 comparisons;
- the baseline is reproduced byte-for-byte;
- the Owner's functions are verbatim at AST level.

The defects were in the plumbing around the rules: the launcher, the ledger's integrity checks and the golden file.

| Component | Verdict | Open items |
|---|---|---|
| `rules_v642` / `signals_v66` / `guardrails_v66` / `sizing_v66` (fidelity, §3) | **PASS** | none |
| `daily_scan_v66.py` (§4) | **PASS WITH CORRECTIONS**: F-2 HIGH, F-5, F-6, F-15 fixed | F-18, F-19 (LOW) |
| `ledger_v66.py` (§5) | **PASS WITH CORRECTIONS**: F-3 HIGH, F-4, F-15 fixed | **F-8, F-9 (gate B′)** |
| `config_v66.py` (§6) | **PASS WITH CORRECTIONS** | **F-10, F-11 (MEDIUM)** |
| `telegram_bot_v66.py` (§7) | **PASS WITH CORRECTIONS**: F-12 fixed | F-13 (= CRO C-2) |
| `pine/swing_v66.pine` (§8) | **PASS WITH CORRECTIONS**. The Owner must still compile it. | F-16 (LOW) |
| `golden_export.py` + `golden_v66.csv` (§8) | was **FAIL** (9/24 false mismatches), now **FIXED** (F-7) | README tier mapping |
| `selftest.py` (§9) | **PASS WITH CORRECTIONS**: now 57 checks, B′-compatible | none |
| `equivalence_check.py` | **PASS** | none |
| `ledger_check.py` | **PASS WITH CORRECTIONS**: F-14 fixed | none |
| **`掃描_v66.bat`** (§9) | **FAIL: F-1 BLOCKER.** An ASCII `)` on line 14 closes the `if` block, so the bat exits before scanning even when selftest passes. | **Fix line 14** (not `.py`, so not edited by me) |
| `README.md` (§10) | **PASS WITH CORRECTIONS** (text) | 47→57; S2 list; S4; golden mapping; fingerprint |

**Findings by severity:**

| Severity | Findings |
|---|---|
| BLOCKER | F-1 (.bat) |
| HIGH | F-2 (partial bar locks wrong ledger rows), F-3 (S2 false negatives); both fixed |
| MEDIUM | F-4, F-5, F-6, F-7 (fixed); F-8, F-9, F-10, F-11 (open) |
| LOW | F-12, F-14, F-15 (fixed); F-13, F-16, F-18, F-19, F-20 (F-20 fixed) |
| INFO | F-17, F-22 |

## 2. What I ran (reproduction)

All runs on this cloud box, `python3 -I`, Python 3.11.18, pandas 3.1.1, Webull CSVs in `strategy/v6.6/data/` (untracked; SPY through 2026-11-23). Scratch: `/tmp/claude-0/-home-user-horse-monitor/54e44e17-7784-559b-835e-2acd5a9d7af1/scratchpad/tom2/`.

| Run | Result (before my fixes) |
|---|---|
| `selftest.py` | 47/47 pass, exit 0 |
| `equivalence_check.py` | 85,120 (day, ticker, path) comparisons, **0 differences**, exit 0 |
| `lab.py --mode baseline --out <scratch>` | **Identical** to `results/baseline.json`: bt 135 trades `3044c31236e877f0` 2.2056% CAGR +US$116.32; scan 96 `1ab4dbb940429ce0` 0.8206% +US$42.39; per_trade_bt 1087 `1b9e39ef519eca38`; per_trade_scan 633 `127cc0c250b65537` |
| `ledger_check.py` | 187 rows logged over 2025-03-03 to 2025-05-30; rerun adds 0; resolve == `lab.simulate` per-trade (bt 38/38, scan 21/21) and 2-slot book (8/8) IDENTICAL; synthetic COST fill flagged S2. **But the script has no asserts and always exits 0** (F-14) |
| `daily_scan_v66.py --source csv --asof 2025-06-16` | Stamp fingerprint `69b0780a3d5b` (= README); 1 live (MU E2, 1 sh), 1 shadow-only (META), 8 blocked on A-size; 15 ledger rows |
| My own scanner-vs-lab script (`scripts/scan_vs_lab.py`) on 2024-08-06, 2025-06-16, 2026-09-28 (+2 bear dates) | Pre-guardrail signals identical to `lab.build_signal` on both paths (31 rows, 0 mismatches); two independent runs give byte-identical ledger rows (excluding `logged_at`) |

Reading-only (cannot run here: no `yfinance`/`requests`/`ta`, no Pine compiler): live yfinance paths in the scanner, guardrails, bot polling loop, Pine.

## 3. Fidelity: signals / guardrails / sizing vs the Owner's V6.4.2

**Verdict: PASS.** No rule or threshold change found.

**Method.** I parsed the Owner's upload with `ast` only; it was never executed or imported. I then diffed the function bodies against `rules_v642.py` (`scripts/ast_diff.py`):

| Owner function | V6.6 | Diff |
|---|---|---|
| `mr_score`, `mr_plan`, `trend_plan`, `classify` | `rules_v642` | **Identical bodies** |
| `trend_score` | `rules_v642.trend_score` | Only the `detail` dict and the tuple return are removed. Score arithmetic is identical. |
| `position_plan(entry, stop, currency)` | `position_plan_ccy` | Module constants become parameters. Defaults are equal. The HKD branch (D-05) is preserved. Returns `round(shares*entry, 0)` as before. |
| `daily_strong_signals.classify_mr_tier` | `rules_v642.classify_mr_tier` | **Verbatim** except that `get_days_to_earnings(ticker)` becomes a `days_er` argument |
| `check_guardrails` / `get_days_to_earnings` | `guardrails_v66.check` / `get_next_earnings` + `days_to` | Same order: stop > 15% blocks; speculative flag; earnings 0–5 days blocks; unknown shows "?". `days_to` normalises the earnings timestamp. I checked that this gives the same integer as the Owner's un-normalised `(ed - today).days` for positive and negative offsets. The calendar lookup handles both yfinance formats. |

**Paths.**
- `signals_v66.on_path("scan")` reproduces `daily_strong_signals`:
  - E1 requires strong tier (RSI2 < 10 and the **rounded** `plan["r"]` ≥ 3, exactly as the Owner's code).
  - E2 has no breakout gate.
- `on_path("bt")` reproduces `run_trend_backtest`'s E2 entry condition (`High >= high_20d`, today included) and E1 as backtested (all tiers).
- E1's 15% stop width is applied in `on_path` on both paths. The Owner applies it in `check_guardrails`, so the result is the same; only the display differs (F-17).
- `equivalence_check.py` shows 0 differences in 85,120 comparisons against `lab.build_signal`. My own `--asof` replays on 3 bull dates match the lab on both paths.

**The bt path is the lab's validated path.** `lab.py --mode baseline` reproduces the committed `results/baseline.json` byte-for-byte on all four hashes.

**Sizing (`sizing_v66.size`).**
- **A:** `position_plan_ccy` at 10%.
- **B′:** applies only when A gives 0 shares and the engine is E2. It gives 1 share if the price is ≤ 15% of the account and the 1-share risk is ≤ 1%. This is the CRO §4.3 text.
- **D:** 15% flat.
- All six CRO V-2 cases pass. HKD is supported in all modes.
- The cap lives only here. Exception: Pine and `lab.position_plan` carry their own 10% copies, which is by design (Pine cannot import; the lab is the reference).

**Rule changes sneaking in: none found.** The only behavioural differences from the Owner's tools are intended:
- the breakout gate on the live list (G-1);
- E1 at all tiers (Owner decision 2);
- earnings check off in `--asof`;
- HK always blocked in the bot. The Owner's bot also blocked HK, via the pool check.

## 4. daily_scan_v66

**Verdict: PASS WITH CORRECTIONS. The corrections are applied (F-2, F-5, F-6, F-15).**

**What is right**
- **No look-ahead in `--asof`.**
  - Every series is truncated to `index <= asof` before the indicators are computed (`load()`).
  - `bar_date` is SPY's last bar ≤ asof.
  - Any ticker whose last bar differs from SPY's last bar is skipped, with a warning.
  - The indicators are causal, so truncated and full-history values are identical. This is confirmed by 0 mismatches against the lab on 3 dates.
- **Split-corrected sizing only in csv mode.** `raw_factor()` returns 1.0 unless `source == "csv"`. That is correct, because live yfinance prices for today are real prices.
- **Earnings check is off in `--asof` runs** and is stamped "off".
- **Live yfinance path (read only).**
  - It uses `history(period="2y", auto_adjust=True)`.
  - Empty frames and exceptions go into a printed `failed` list. There is no silent `continue`.
  - The index has its timezone stripped (NY wall dates).
  - The partial-bar test covers Mon–Fri 09:30–16:00 New York time. It ignores holidays, which can only cause a false warning.
- **Ranking matches the lab:** E2 first, then score descending (`signals_v66.rank_key` = `lab.simulate` cands sort). 0-share and guard-blocked signals do not take a rank, as in the lab's `scan_0_shares`.
- **What is shown.**
  - Only the live-mode size is on screen. **B′ and D sizes are not printed**; they go to the ledger only.
  - Sections ② (scan-only, "只記錄,唔交易") and ③ (blocked) are present.
  - `--dry-run` never writes.

**Findings**

| # | Sev | Where | Finding | Status |
|---|---|---|---|---|
| F-2 | **HIGH** | `daily_scan_v66.py` (write step); `ledger_v66.append_signals` | The ledger key (bar_date, ticker, path) is **first-write-wins**. A run during the US session writes partial-bar rows (`partial_bar=True`), and the correct post-close rows for the same key are then **silently rejected forever**. Intraday phantoms stay in the ledger, and `resolve` included them. | **FIXED:** a partial run does not write. `resolve` also drops legacy `partial_bar=True` rows. |
| F-5 | MEDIUM | `scan()` live list | Held tickers were ranked: in my probe, a held MU took **#1** ahead of NKE/INTC. `lab.simulate` skips held tickers, so on-screen ranks ≠ lab ordering, and the fill-time rank check was off by one. | **FIXED:** held signals are printed unranked ("持倉中,唔計排名,唔好加注"). Ledger rows are unchanged; for non-held cases they are byte-identical to the pre-fix rows (verified). |
| F-6 | MEDIUM | `scan()` | The live list was **hard-wired to A sizing**. Enabling B′ in config would change the stamp to "B′ 開" while sizing and blocking stayed at A, so the config and the screen would disagree. | **FIXED:** uses `sizing_v66.live_mode()`. While A is live, output is identical. Note: enabling B′ also needs the selftest fix in §9 (F-20). |
| F-15 | LOW | `scan()` / `review()` | `--asof` without `--ledger` wrote into the **live** ledger. Its old `bar_date`s then started the 6-month review clock early (CRO probe K-4: "17.3/6 months"). | **FIXED:** `--asof` refuses the default ledger and prints how to use `--ledger`. `review` measures months from the first `logged_at`. |
| F-18 | LOW | `trailing_line()` | The open-position stop is computed on auto-adjusted bars against real fill prices. A **split during the hold** would mis-state the stop by the split ratio; dividends shift it slightly lower. It also does not say when the stop has already been hit (Low ≤ stop since entry). Display only. | Open (recommend: scale by split factor and print "已觸發" when breached) |
| F-19 | LOW | `scan()` | The −10% monthly breaker is not checked. The lab enforces it; CRO C-10 makes it manual. Month-to-date realised P&L is available from `fills.csv`. | Open (recommend: print MTD P&L and suppress ① at ≤ −10%) |
| F-17 | INFO | `signals_v66.on_path` | An E1 stop wider than 15% is dropped silently. The Owner's `run_scan` listed it under "blocked". Trading outcome is the same. | Accept |

## 5. ledger_v66 (fill, resolve, review S1–S4)

**Verdict: PASS WITH CORRECTIONS.**
- Applied: F-3, F-4, F-14, F-15.
- Open, and they gate **B′** (not A): **F-8** (S4) and **F-9** (earnings log).

**What is right**
- **Idempotence key** (bar_date, ticker, path): ledger_check reruns add 0 rows. Two independent runs give identical rows.
- **BOM** is written once, on new-file creation only. `_rewrite` replaces the whole file, so there is still exactly one BOM. Selftest covers this.
- **Resolve rescaling is correct.**
  - E1 stop and target are multiplied by fresh close ÷ stored close. That is exact under multiplicative back-adjustment.
  - The E2 stop is recomputed as fresh close − 3×fresh ATR. Every bar up to the signal bar is scaled by the same factor when a later dividend or split is applied, so ATR scales exactly. The recomputed stop therefore equals the stop the Owner saw × scale, to rounding.
  - The 2y (live) vs 5y (resolve) Wilder-seed difference decays as (13/14)^500 and is negligible.
  - The 15%/12% re-checks are scale-invariant.
- **Dedup via `lab.simulate`.** Per-trade (`PER_TRADE`, unlimited) skips tickers already held or pending in the simulated book, so a repeated E2 signal is not double-counted. ledger_check: per-trade bt 38/38 and scan 21/21, and book 8/8, are identical to `lab.simulate` on the same signals.
- **Fill-time B′ exception logic matches CRO §4.3.**
  - It requires B′ enabled, E2, exactly 1 share, ≤ 15%, and 1-share risk ≤ US$12.82.
  - With B′ off, any position above 10% is S2.
  - Multi-share above 10%, E1 using the exception, and a share above US$192.31 all fall through to S2. This covers all of CRO S2's sizing clauses.
- **S1** (exception position realised loss > 2% of the account) and **S3** (month realised ≤ −10% with an exception position open in that month) are correct at month granularity. S3 errs toward tripping. Both have selftest coverage.

**Findings**

| # | Sev | Where | Finding | Status |
|---|---|---|---|---|
| F-3 | **HIGH** | `cmd_fill` source detection | **S2 false negatives.** "Source" was the latest bar *on which this ticker had any row*, not the bar of the last scan. Consequences:<br>• A weeks-old live signal let a trade with no current signal pass. In ledger_check's **own** synthetic WMT fill on 2025-05-20, WMT had no row in May and the fill passed unflagged.<br>• A live-path row blocked by **earnings/stop width** or with **A = 0 shares** counted as "live".<br>• A **self-chosen tighter stop** could manufacture a size the system refused (CRO probe: AMD $116 vs system $112.10).<br>• There was **no 2-position check** (CRO probe: 5 open fills accepted). | **FIXED:**<br>• Source = the ticker's row on the **last scanned bar before the fill date** (all tickers). Otherwise "stale" → S2.<br>• New S2 flags: guard-blocked; A = 0 (unless a valid B′ exception); stop more than max(1¢, 0.5%) above the system stop; ≥ 2 open positions.<br>• The out-of-order note now compares rank with free slots (positions opened before today). Overlaps CRO C-4. |
| F-4 | MEDIUM | `cmd_fill` | The default fill date was the **local (HK) date**, but `bar_date` is the NY date. A fill recorded on HK Wednesday morning for a NY Tuesday open got `open_date` = Wednesday. Effects: the trailing stop skips the entry-day high, and source detection reads the fill-day bar. | **FIXED:** the default is now the New York date. |
| F-8 | MEDIUM | `review` S4 | S4 is implemented as realised fill P&L ≤ 0 after ≥ 10 closed fills (with V1 = True). CRO §5 S4 is "V-1 shows net EV ≤ 0 at the real fee": a one-off re-run of `as_traded` at the verified fee. Ten trades are noise: E2 per-trade SD is about 8.9pp. The printed consequence ("返去 A") is also wrong: the CRO says no entries at **any** cap. | Open. Proposed fix: add `V1_NET_EV_PCT` (the `lab` re-run at the real fee) to config; S4 = that value ≤ 0 → "停止所有新倉". Keep the realised-P&L check as a labelled note, not as S4. Needs a CRO word. |
| F-9 | MEDIUM | `review` | **The earnings-inside-hold log (CRO §5; plan Phase 2) is not implemented.** `signals.csv` stores `earnings_date`, but `review` never compares it with the fill `open_date`/`close_date`. | Open. **Required before B′.** Implement in `review`: for each fill, look up the source row's `earnings_date` and flag `open_date ≤ ED ≤ close_date` (or today if still open). |
| F-14 | LOW | `ledger_check.py` | No asserts: the script printed DIFF and still exited 0, so it could not fail. | **FIXED:** exits 1 on any DIFF, a changed rerun count, or a missing S2. Prints `LEDGER CHECK PASS`. |
| F-22 | INFO | `resolve` book_2slot | The 2-slot book sizes with `lab.SPLITS`, a static table. A split after 2025-11 would mis-size the book (not the per-trade edge). | Add new splits to `lab.SPLITS` as they occur |
| — | INFO | `resolve` | The edge sample excludes `guard_ok=False` signals, mostly earnings blocks. The backtest has no earnings guard. The ledger edge is therefore "tradeable signals", not like-for-like with the lab. That is acceptable, but `review` should say so. | Note |

## 6. config_v66: structural control and fingerprint

**Verdict: PASS WITH CORRECTIONS.** The control works as designed. Two design gaps are open.

**Can B′ be enabled without the gates? No, short of a deliberate multi-line edit.**
- `check_config()` refuses unless **all** of the following hold: `CAP_MODE == "B_PRIME"`, `B_PRIME_ENABLED`, all four `GATES` True, and a non-empty `B_PRIME_CRO_NOTE`.
- It also pins `CAP_A_PCT == 10`, `CAP_BPRIME_PCT ≤ 15`, `MAX_POSITIONS == 2`, `RISK_PCT == 1` and `LIVE_PATH == "bt"`.
- It runs in `stamp()`, in `live_mode()` (which the scanner live list now calls, F-6), in ledger `main` and in bot `main`.
- The gates are self-attested booleans. That is acceptable: the Owner is final authority, and the README asks for a dated CRO note.

| # | Sev | Where | Finding | Status |
|---|---|---|---|---|
| F-10 | MEDIUM | `config_v66.py:46-47` `CORE_FILES` | **The fingerprint does not cover the files that decide what the Owner sees and what S2 checks.** `daily_scan_v66.py` (sizing mode, ranking, guard application, blocked list), `ledger_v66.py` (S1–S4) and `lab.py` (imported by both) are all outside it. Proof: every fix in §11 changed scanner and ledger behaviour, and the stamp still reads `69b0780a3d5b`. CRO S2's "scanner running an unstamped path" therefore cannot be detected. Conversely, `config_v66.py` is **inside**, so every gate flip changes the fingerprint (audit F-2). | Open. Recommend **two stamps**: a *code* fingerprint (rules, indicators, signals, sizing, guardrails, daily_scan, ledger, lab) and a *config* fingerprint. Or move `GATES`/B′ to a separate file. Until then, the CRO's C-5 pin should name a **git commit**, not just the fingerprint. |
| F-11 | MEDIUM | `config_v66.py:67-75` | The control is built from `assert`. Under `python -O` or `PYTHONOPTIMIZE=1` every check disappears, including the B′ gate and `LIVE_PATH == "bt"`. Then the structural control depends on how Python was launched. | Open (core file, so it changes the fingerprint). Fix: replace each `assert` with `if not …: raise SystemExit(msg)`, and make selftest catch `SystemExit`. |
| — | INFO | `selftest.py` | Selftest asserted `live_mode() == "A"` and relied on gates being outstanding, so **following the README's B′ procedure would make selftest fail** and the .bat refuse to scan (audit F-1). | **FIXED** in selftest. It expects A unless B′ is fully authorised, and tests the gate and CRO-note refusals on a temporary config. |

## 7. Telegram bot

**Verdict: PASS WITH CORRECTIONS. F-12 is applied; F-13 is open as a CRO condition.**

**What is right**
- **Token source.** The token comes from `SWING_BOT_TOKEN` or `%USERPROFILE%\.swing_bot_token`, never from code. The placeholder token is refused, and selftest covers that refusal.
- **Allow-list.** Only allow-listed chat IDs get replies. With an empty list the bot runs in setup mode: it prints chat IDs and replies to nobody.
- **Error output.** Every printed `{e}` and every API error dict passes through `redact()`. There is no print of `api` or `token`.
- **No write path to a broker.** The only outbound write is `sendMessage`.
- **HK handling.** `700` → `0700.HK`; the regime check uses ^HSI; sizing uses HKD (`position_plan_ccy` with `currency="HKD"`). HK is always blocked, which matches the Owner's bot (HK was outside the pool).
- **Offline analysis** runs through the shared core, and selftest covers it.

| # | Sev | Where | Finding | Status |
|---|---|---|---|---|
| F-12 | LOW | `telegram_bot_v66.py` main loop, `_TOKEN_RE`, `load_token` | **Three gaps in the redaction:**<br>(a) **Leak through chained tracebacks.** Say a network error is caught, and the Owner presses Ctrl+C during the `time.sleep(5)` inside the `except` handler. Python then prints "During handling of the above exception…" together with the original `ConnectionError`, which contains `/bot<token>/getUpdates`. I reproduced this: the raw traceback contains the token.<br>(b) The regex missed a URL-encoded colon (`%3A`).<br>(c) A token file in a **sub**folder of the package (e.g. `ledger/`) was accepted. | **FIXED:** a `sys.excepthook` redacts every uncaught or chained traceback; the regex accepts `:` or `%3A`; the token-file check uses `commonpath`. Two selftest cases added. |
| F-13 | LOW/MED | `analyze()` | The bot prints a full trade plan and a share count for **scan-only** signals and for HK tickers, and only then says "唔入場". This is CRO condition C-2. | Open (display design; CRO pre-switch condition). Fix: print the plan and size only when `sig["bt"]` exists and no "❌" block applies. |
| — | INFO | `analyze()` | If fetching the regime index raises (not merely returns None), the exception escapes to the handler. It is redacted, but the Owner's bot degraded gracefully ("無法取得"). | Note |

## 8. Pine (`pine/swing_v66.pine`) and the golden file

**Verdict: PASS WITH CORRECTIONS. The golden file was the defect (F-7, fixed). Pine has one LOW display issue (F-16).**

**Line-by-line against Python**

| Item | Pine | Python | Match |
|---|---|---|---|
| E1 score s1–s5, OBV +0.10, cap 1.0 | l.65-70 | `mr_score` | **Verbatim from the Owner's V6.4.2 Pine** (I diffed l.52-57 of the upload). The only difference is rounding to 4 dp, which matters at the threshold alone. |
| E1 stop / target / R | l.72-82 | `mr_plan` (filter R ≥ 2, then lowest price) | Verbatim F-02 logic. R is unrounded in Pine but rounded to 2 dp in Python; the strong-tier `R ≥ 3` can differ only within 0.005 of 3. |
| E1 15% / A-size gate / tiers | l.84-90 | `on_path` + `size("A")` + tier | Same as the Owner's Pine (`not posTooExpensive`). Premium = strong + OBV; earnings are manual. |
| E2 score | l.95-101 | `trend_score` | Same weights and bands. NaN handling differs during warm-up only. |
| Breakout | l.100 `high >= ta.highest(high, 20)` | `High >= High.rolling(20).max()` | **Same; today is included** |
| ADX / DI | `ta.dmi(14, 14)` | Wilder (`indicators.adx_wilder`) | Same definition; seeds converge (parity V-3 covers the Python side) |
| E2 stop 3×ATR ≤ 12%, A-size | l.102-105 | `trend_plan` + `size("A")` | Match |
| Paths | `e2Trade` = base + breakout; `e2Shadow` = base without breakout | `on_path("bt"/"scan")` | Match, except that Pine also gates on A ≥ 1 share |
| Risk text | "倉位一律1%" | manual | Match (the old "普通 0.5%" is gone) |

**Compile risk (Pine v6).** I see no blockers:
- No int/float used as bool, no `transp`/`when`, ternaries are typed.
- `t.cell()` method syntax already compiles in the Owner's V6.4.2 Pine.
- `ta.obv` and `ta.dmi` exist in v6.
- Least certain: `timestamp("2000-01-01")` (a date-only ISO string). The docs list it as valid. If it errors, use `timestamp("01 Jan 2000 00:00 +0000")`.

| # | Sev | Where | Finding | Status |
|---|---|---|---|---|
| F-7 | MEDIUM | `golden_export.py`, `pine/golden_v66.csv` | **The golden file would have failed in Pine on 9 of 24 rows, with no bug in Pine.**<br>• Pine's tier and E2 flags require ≥ 1 share at 10%, and the export ignored that. JPM $324, NVDA $202–216 (4 rows), XOM $177/$186, MSFT $532 and WMT $128.41/$129.17 all show **0** in Pine.<br>• WMT 11-13 at $128.09 sat 0.09% under the cap.<br>• The export's "強" can legitimately read 3 in Pine (strong + OBV).<br>• Checked with my replica of Pine's gate (`scripts/golden_pine_expect.py`).<br>• The audit counted 6; I add the three E2 scan-only rows, because Pine's `e2Shadow` is also gated. | **FIXED:**<br>• Rows that carry a signal must be affordable at A with a 3% margin (price ≤ 97% of US$128.21 and 1-share risk ≤ 97% of US$12.82).<br>• New column `A股數`.<br>• E1_tier now reads 頂級 (strong + OBV) / 強 / 普通, as Pine does.<br>• A guaranteed "E1強" bucket (2 rows). The window is widened to 250 bars to find one.<br>• Regenerated: 0 of 24 rows disagree. **The README §六 must add: 普通 = 1, 強 = 2, 頂級 = 3; rows with `A股數` blank are no-signal rows.** |
| F-16 | LOW | `swing_v66.pine:135-141` | On the entry bar, the optional trailing stop starts at `close − 3×ATR`. The lab and `trailing_line` use `max(signal-day stop, max(entry, high) − 3×ATR)`, so Pine's first-day stop is lower and catches up from day 2. Display only. | Open (I did not edit Pine; there is no compiler here). Fix: `trailHigh := high`, `trailStop := math.max(close[1] - 3.0*atrVal[1], high - 3.0*atrVal)`. |
| — | INFO | golden fairness | The golden file compares scores, R, stop %, tier and breakout, not prices, which is right because TradingView prices are unadjusted. The ADX bands (±1.5/0.7), the score (±0.03), R (±0.2 around 2 and 3), RSI2 (±2) and stop width (±0.5pp) margins are adequate. One weakness: a 0.03 score margin is smaller than one E2 component step (0.0375 for dist_60h, 0.045 for vol). Every E2 row in the regenerated file sits ≥ 0.035 from 0.65. | Note |

## 9. Tests (selftest, equivalence, ledger_check) and the .bat launcher

**Verdicts:**
- **`掃描_v66.bat`: FAIL (F-1, BLOCKER, not fixed by me; it is not a `.py` file).**
- **`selftest.py`: PASS WITH CORRECTIONS** (applied).
- **`equivalence_check.py`: PASS.**
- **`ledger_check.py`: PASS WITH CORRECTIONS** (applied, F-14).

### F-1 · BLOCKER · `掃描_v66.bat:14`: the launcher never scans, even when selftest passes

Line 14 sits inside the `if errorlevel 1 ( … )` block and contains **ASCII** parentheses:

```
  echo     臨時可以用返舊版:掃描.bat(V6.4.2)
```

1. In cmd.exe, an unescaped `)` inside a parenthesised block closes the block. That is the well-known `echo …)` inside `if (…)` trap; the `(` in argument position is literal and does not nest.
2. So the `if` ends at `V6.4.2)`.
3. Lines 15–16 (`pause`, `exit /b 1`) then run **unconditionally**. The stray `)` on line 17 is ignored.

**Effect:**
- After a **passing** selftest, the Owner sees the banner, then "Press any key…", and the window closes with exit code 1. `daily_scan_v66.py` is never reached.
- The failing path still blocks, so the control is fail-safe. But the daily routine is dead on day one.
- The natural reaction is to run the old `掃描.bat`, which is the unvalidated scanner path that G-1 retired.

**The audit and the CRO sign-off both read this block as working** (audit row 6, "VERIFIED"; CRO "the launcher re-proves it"). Neither noticed the parenthesis.

**Fix** (also satisfies CRO C-1, which removes the fallback):
- Replace line 14 with text containing **no ASCII `(` or `)`**, for example `echo     今日唔好開新倉;已有嘅止蝕單照舊;將 selftest_last.log 畀 AI 睇。`
- Alternatively, escape the parentheses as `^(`/`^)`.
- Any future text inside that block must follow the same rule.
- Line 8 and line 22 are outside any block and are fine.
- Keep CRLF and no BOM.
- **The Owner must double-click it once on the PC and see the scan run** before switching.

**Other .bat checks:**
- **Line endings:** CRLF on all 23 lines, no BOM, and `.gitattributes *.bat -text` is in effect (`git check-attr` shows `text: unset`).
- **errorlevel:** `if errorlevel 1` is true for any exit code ≥ 1, including selftest failure (`sys.exit(1)`), an uncaught exception (1) and python missing (9009). A negative exit code would slip through, but Python does not produce one in normal operation.
- **Code page:** `chcp 65001` with Chinese `echo` lines and no BOM is the same pattern as the Owner's working V6.4.2 `掃描.bat`, so it is acceptable.
- **Encoding:** `PYTHONUTF8`/`PYTHONIOENCODING` make the redirected `selftest_last.log` UTF-8.

### selftest.py: are the 47 checks meaningful?

Mostly yes. They cover:
- the real V6.4.2 `mr_plan` case;
- the position_plan cap;
- simulator invariants (next-open fill, fill = open, ≤ 2 concurrent positions, notional ≤ US$128.21, net ≤ gross);
- the F-1 slot-reservation regression;
- the MSTR split;
- equivalence on synthetic data;
- the breakout path;
- all six CRO V-2 cases;
- the structural B′ refusal;
- the fingerprint, including CRLF invariance;
- the guardrails, the tier and a synthetic trade-list hash;
- ledger idempotence and BOM;
- S1/S3;
- token redaction and placeholder refusal.

Weak or near-tautological:

| Check | Problem |
|---|---|
| "RSI/ADX 喺 0–100" | Sanity only |
| "設定自檢通過" | `check_config()` either returns True or raises |
| "bot:離線分析有版本指紋同兩條路徑" | "舊掃描器路徑" is printed unconditionally (`telegram_bot_v66.py`, last line of `analyze`), so half the check cannot fail |

**Coverage gaps (F-20):**
- No test of `cmd_fill` S2, the scanner's partial-bar or held logic, or S4.
- B′-incompatible asserts (see §6).

**Added: 10 new checks (47 → 57) and 1 rewritten check:**
1. live mode is A unless B′ is fully authorised;
2. a missing CRO note blocks B′;
3. a fill with a live signal → no S2;
4. a stale signal → S2;
5. a guard-blocked signal → S2;
6. A = 0 with a self-tightened stop → S2;
7. a 3rd position → S2;
8. the synthetic scanner finds a live day (precondition);
9. a partial bar writes no ledger rows;
10. a held ticker is not ranked;

plus the `%3A` redaction check.

**Mutation check:** run against the pre-fix `daily_scan_v66.py`, `ledger_v66.py` and `telegram_bot_v66.py` (commit 4d0b69e), **7 of the new checks fail**, so they test the fixes rather than restate them. The synthetic regression hash `c76849eb6539` is unchanged.

**The README's "47 項" must become 57.**

### equivalence_check.py / ledger_check.py
- **equivalence_check:** a meaningful test. It compares engine, stop, target and score on every (day, ticker, path) over the Webull window: 85,120 comparisons with 0 differences. It exits non-zero on any difference.
- **ledger_check** (F-14): printed IDENTICAL/DIFF but **always exited 0**. Fixed: it now exits 1 on any difference.
- **ledger_check after the fix:** its synthetic WMT fill is now correctly flagged as stale (see F-3).

## 10. README accuracy (`strategy/v6.6/README.md`, Cantonese)

**Verdict: PASS WITH CORRECTIONS.** These are text edits for the CEO; I did not edit the README. This overlaps the audit (F-1/F-2/F-4/F-8), which already returned it as FAIL.

**Verified true:**
- Every command line parses against the argparse definitions.
- The fingerprint `69b0780a3d5b` matches the stamp, both at 4d0b69e and after my fixes (none touched `CORE_FILES`).
- The research figures match: ~2.2%/yr and +US$116 = `baseline.json` bt 2.2056% / +US$116.32; scanner ~0.8% = 0.8206%.
- `reports/quant/2026-11-24-v642-real-code-v66-lab.md` exists.
- The file table matches `CORE_FILES`.
- The B′ procedure matches `check_config`.

| README | Problem | Correction |
|---|---|---|
| §一.3 "(47 項)" | Now **57** after my selftest additions | Change to 57 |
| §一.4 `copy ..\dual_engine_v6_4.py .` | Assumes the old engine sits in the parent folder. The Owner's package keeps it in `01_每日使用_最新V6.4.2\`. The step also edits `config_v66.py`, which changes the fingerprint that §二 says to distrust (audit F-2). | Give the real path. Fix the fingerprint scope (F-10) or list the expected fingerprints. |
| §二 launcher | "雙擊 掃描_v66.bat" is the routine, but the .bat never scans (F-1) | Fix the .bat first |
| §二 "記錄嗰陣會即刻檢查…超上限、冇 live 訊號、揀咗排第3或之後" | Checks are now: over cap, no or **stale** live signal, **guard-blocked**, **A = 0**, **stop tighter than the system's**, **> 2 positions** (all S2); the rank note compares with **free slots** | Update the list. Add: "唔係當日記錄就加 `--date`(紐約成交日)" |
| §二 partial-bar bullet | The scanner now also refuses to write the ledger during the session | Add "唔會寫記錄簿" |
| §三 S4 "扣真實收費後淨盈虧 ≤ 0" | Not the CRO's S4, and the consequence is wrong (F-8) | Use the CRO wording after the code change |
| §三 | The earnings-inside-hold log (CRO §5) is not mentioned or implemented (F-9) | Add it once implemented |
| §四 | Correct per `check_config`. After my fixes, enabling B′ no longer breaks selftest (§6) and the live list now uses B′ sizing (F-6). Still changes the fingerprint (F-10). | Mention the fingerprint change |
| §六.3 golden | No tier mapping; Pine shows 0 for unaffordable names | Add "普通 = 1、強 = 2、頂級 = 3;`A股數` 空白 = 冇訊號行". The regenerated file has no unaffordable signal rows (F-7). |

## 11. Changes I made (re-run after all changes)

**Scope of the changes:**
- Only `strategy/v6.6/*.py`, plus the regenerated `pine/golden_v66.csv`, which is the output of the fixed `golden_export.py`.
- **No V6.4.2 rule, threshold, lab code or config gate value was changed.**
- **No `CORE_FILES` file was touched**, so the fingerprint stays `69b0780a3d5b`. That itself illustrates F-10.
- **`results/baseline.json` is unchanged:** all four hashes were reproduced after the changes.

| File | Change | Finding |
|---|---|---|
| `daily_scan_v66.py` | The live list sizes and blocks with `sizing_v66.live_mode()` (A today; previously hard-coded A). Ledger columns are unchanged; `size_live`/`notional_live` are display-only keys. | F-6 |
| | Held tickers are excluded from ranking and printed unranked as "持倉中(唔計排名,唔好加注)". The return dict gains `held_signals`. | F-5 |
| | A partial-bar (in-session) run does not write the ledger. | F-2 |
| | `--asof` refuses to write the default (live) ledger. | F-15 |
| `ledger_v66.py` | The default fill date is the New York date. | F-4 |
| | Source = the ticker's row on the **last scanned bar before the fill date**; otherwise "stale" → S2. | F-3 |
| | New S2 flags: guard-blocked live signal; A = 0 (unless a valid B′ exception); stop more than max(1¢, 0.5%) above the system stop; ≥ 2 open positions. | F-3 / CRO C-4 |
| | The out-of-order note compares rank with free slots. | F-5 |
| | `resolve` drops `partial_bar=True` rows. | F-2 |
| | The `review` 6-month clock starts at the first `logged_at`. | F-15 |
| `telegram_bot_v66.py` | A redacting `sys.excepthook`, the `%3A` regex and the `commonpath` token-file check | F-12 |
| `ledger_check.py` | Asserts; exits 1 on failure; prints `LEDGER CHECK PASS` | F-14 |
| `golden_export.py` → `pine/golden_v66.csv` | Rows with a signal must be affordable at A with a 3% margin; adds an `A股數` column; E1 tiers 頂級/強/普通 as in Pine; an E1強 bucket; a 250-bar window. Regenerated with 24 rows, 0 disagreeing with my Pine-logic replica. | F-7 |
| `selftest.py` | B′-compatible structural tests (tests on a temporary config; live mode expected A unless fully authorised); 10 new checks: 47 → **57** | F-20, §6 |

**Re-run after all changes:**

| Check | Result |
|---|---|
| `selftest` | 57/57, exit 0. Mutation: 7 new checks fail on the 4d0b69e code. |
| `equivalence_check` | 85,120 / 0 differences |
| `ledger_check` | `LEDGER CHECK PASS`, exit 0 |
| `lab --mode baseline` | Identical to `results/baseline.json` |
| `daily_scan --asof 2025-06-16` | Ledger rows byte-identical to the pre-fix run (excluding `logged_at`) |
| Scanner vs lab | 3 dates, 0 mismatches |

**Not changed by me:**
- `掃描_v66.bat` (F-1), `README.md`, Pine (F-16) and core files (F-10, F-11): these are outside my edit scope or alter the fingerprint.
- S4 semantics (F-8) and the earnings log (F-9) need CRO wording.
- Bot display (F-13) is a CRO condition, left to the CEO.

**Commit status:** a WIP commit `8e2517a` by the CEO captured part of these changes. The rest are uncommitted in the working tree.

## 12. What would make this fail live

1. **Launcher dead on day one (F-1).** The Owner falls back to the old `掃描.bat`, the unvalidated scanner path (−0.82% CAGR OOS at 10%). **Fix it, then watch one real run on the PC** before switching.
2. **Parity (V-3) not yet run.** The pandas ADX/RSI/ATR stand in for `ta`. Near the thresholds (ADX 25, score 0.55/0.65), small differences flip signals. The ≥ 98% agreement on signal days was not measured on the Owner's machine. Until then, the "live list = validated path" claim holds against the lab, not against his `ta` install.
3. **Costs (V-1).** The lab assumes 10bp per side and zero commission. At a US$1/side minimum (M2), `as_traded` over the full window turns from **+0.81% per trade and 2.21% CAGR** to **−1.24% per trade and −3.16% CAGR**. Source: `results/summary.csv`, ALL period, 135 trades; I re-read the file today. On a US$128 position, a US$1 fee is about 0.8% per side, as large as the book's entire per-trade net EV.
4. **Silent degradation of the earnings guard.**
   - If yfinance's `.calendar` breaks, every ticker shows "?" and **nothing is blocked**.
   - The scanner does not count the "?" results.
   - Recommendation: print "財報查唔到: N/38" in the stamp and treat N > 5 as a warning.
5. **Execution drift from the simulated rules.**
   - The lab re-checks R and risk when the next open deviates more than 1% from the signal price, and enters on the open. The Owner does both by hand.
   - Trailing stops are updated manually each night (the "④" section helps, with the F-18 caveats).
   - The −10% monthly breaker is manual (F-19).
6. **Unstamped tool edits (F-10).** Any edit to `daily_scan_v66.py` or `ledger_v66.py` leaves the fingerprint unchanged. The stamp proves only that the rules are intact, not the tools.
7. **Small edge, short history.**
   - The 2-slot bt book earns about 2.2%/yr (+US$116 over 4 years) in a survivor-selected, bull-dominated window. Most of the gain is in 2025–26.
   - **Inside that book, E2 trades average −1.03% net (49 trades) and E1 trades +1.85% (86 trades)** (`summary.csv`, ALL period). The per-signal E2 edge does not survive slot competition and integer sizing in this sample. A 30-trade E2 review has a CI of about ±3pp. **Read the forward ledger as a discipline and risk test, not a return test, before 100 trades**, as the CRO ruled.
8. **Ledger hygiene.** Ledger hygiene now depends on Owner habits that the code can only partly enforce:
   - Run the scan after the US close (the code now refuses to log intraday).
   - Record every fill with the NY date.
   - Never edit the CSVs by hand.
   - Never run `--asof` into the live ledger (now refused).
