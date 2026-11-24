# V6.6 Release Audit — Ai 管理層 (AI Auditor, Dept 9)

**Date:** 2026-11-24
**Auditor:** Ai 管理層
**Scope:** `strategy/v6.6/README.md` (Owner-facing); V6.6 phase commit messages; approved plan `/root/.claude/plans/vast-beaming-lynx.md` (delivery deviations); `reports/quant/2026-11-24-v642-real-code-v66-lab.md` (consistency with README and `results/summary.csv` after a46190c).
**Audited state:** branch `claude/ai-agent-management-bw44yc` at `4d0b69e` (`.git/refs/heads/claude/ai-agent-management-bw44yc`).
**Method limits:** I had Read/Grep/Glob only, with no Bash. **I executed no script.** Every result below comes from reading the code statically or from committed result files. Commit **subjects** were read from `.git/logs/HEAD` (lines 48–59) and the last message from `.git/COMMIT_EDITMSG`. Commit **bodies** are zlib-compressed objects that I could not read. I checked body claims as the caller quoted them (see §2).

## 0. Verdicts

| Document | Verdict | Why |
|---|---|---|
| `strategy/v6.6/README.md` | **FAIL** (returned to the CEO; re-audit only the changed sections) | The daily mode-A routine and all four safety claims check out. But there are four HIGH findings. The B′ procedure, followed as written, stops the daily scan and points the Owner back to the unvalidated V6.4.2 scanner (F-1). On day one, the README's own install step changes the fingerprint that §二 tells him to distrust (F-2). The research summary drops the finding that reverses its framing (F-3). The README already tells the Owner to switch, before Tom's review, the CRO sign-off and the decision record exist (F-10). All four are text fixes, about an hour of work. |
| V6.6 commit messages | **PASS WITH CORRECTIONS** | The "50/54 checks" claim is wrong (actual 47). It is already acknowledged in 4d0b69e and is recorded here (F-19). 85,120 and 39,520 check out exactly as arithmetic. The `ledger_check` 38/38, 21/21, 8/8 results and the trade-list hashes are **unverified** (they need execution). The baseline metrics match `summary.csv`. |
| Plan vs delivery | **PASS WITH CORRECTIONS** | Most items were delivered as specified. Three need closure or explicit CRO acceptance. The earnings-inside-hold flag (CRO-mandated) is missing (F-9). S4 was redefined (F-8). Sign-off sequencing was not followed (F-10). |
| `reports/quant/2026-11-24-v642-real-code-v66-lab.md` | **PASS WITH CORRECTIONS** | Its conclusions survive. Scanner-path figures predate a46190c, and the E1 sensitivity range does not match the current `sensitivity.csv` (F-21). The screenshot conclusion is still stated as fact (F-20). |

**Safety claims (all four): PASS.** No broker or order API exists in the package. The token never enters code and is redacted on every print path. B′ is structurally blocked until the config is fully edited. The .bat stops when selftest fails.

**Severity count:** HIGH 4 · MEDIUM 9 · LOW 10.

## 1. README.md — claims checked (claim / source / result)

| # | README claim (location) | Checked against | Result |
|---|---|---|---|
| 1 | V6.6 no longer needs `ta` (§一.2) | Grep `^\s*(import ta\b\|from ta\b)` over `strategy/v6.6/` returned no hits | **VERIFIED** |
| 2 | Selftest shows 「全部通過」 with 47 items (§一.3) | `selftest.py`: 41 single `check()` sites plus 6 in the CRO V-2 loop (lines 131–136) = **47** when the synthetic run produces trades (5 checks sit under `if len(tr):`, line 69). The pass message is at line 244. | **VERIFIED** (static count) |
| 3 | Parity pass criteria: indicator diff < 0.01; signal-day agreement ≥ 98%, each path separately (§一.4) | `parity_check.py:28-29, 75-77, 87-108`. The ATR criterion is a relative 0.01%. | **VERIFIED** |
| 4 | Parity "證明 V6.6 同你用開嘅 ta 版**每日出一樣嘅訊號**" (§一.4) | The check covers 10 of 38 tickers (`parity_check.py:27`) and compares only which engine fires, not stop, target or score (lines 85–93). It tolerates up to 2% of signal days differing. The "scan" path is the parity script's own re-implementation (`old_paths`, lines 32–52), not the Owner's `daily_strong_signals.py`. | **OVERSTATED** → F-11 |
| 5 | After parity passes, flip `"V3_對照測試"` to True (§一.4) | The key exists (`config_v66.py:43`). But `config_v66.py` is in `CORE_FILES` (lines 46–47), so the edit changes the fingerprint. | **CONTRADICTS §二** → F-2 |
| 6 | Double-click `掃描_v66.bat`; selftest runs first and there is no scan if it fails (§二) | `掃描_v66.bat:10-17` checks `errorlevel 1`. `selftest.py:245` exits 1 on any failure. | **VERIFIED for the .bat path.** Not enforced if `daily_scan_v66.py` is run directly. |
| 7 | Stamp lines and fingerprint `69b0780a3d5b` (§二) | The format matches `daily_scan_v66.py:43-61`. The fingerprint value appears **only** in README:48. There is no committed run output, and I cannot compute SHA-256 without execution. | Format **VERIFIED**; value **UNVERIFIED** → F-2 |
| 8 | "美股開緊市" warning means run again after the close (§二) | The warning is real (`daily_scan_v66.py:64-69`). The run still **continues and writes the ledger** (lines 105, 186–187), and the append is idempotent per key (`ledger_v66.py:82-89`). | **INCOMPLETE** → F-7 |
| 9 | Failed downloads are listed (§二) | `daily_scan_v66.py:80-88, 107-108` | **VERIFIED** |
| 10 | Sections ①–④; ① is ranked E2 first, then by score; ③ shows the block reasons (§二) | `daily_scan_v66.py:169-176, 193-222`. `signals_v66.rank_key` (73–75) uses the same order as `lab.py:391`. | **VERIFIED** |
| 11 | `fill` commands and examples (§二) | The arguments match `ledger_v66.py:301-320`. The examples trigger no flags: PFE 4 × 27.10 = 8.5% notional with US$7.20 risk; NFLX 1 × 69.40 = 5.4% with R = 3.17. | **VERIFIED** |
| 12 | `fill` "即刻檢查...超上限、冇 live 訊號、揀咗排第3或之後" (§二) | Cap breach → S2 (`ledger_v66.py:110-114`) works. The "no live signal" check accepts **any earlier** live row, including stale or guard-blocked ones (117–130). An out-of-order pick is only a 「留意」 note (127–128), not S2. | **PARTIAL** → F-6, F-14 |
| 13 | `review` has "兩部分" (§三) | The code prints 【1】【2】【3】 (`ledger_v66.py:237, 254, 258`) | **WRONG (minor)** → F-13 |
| 14 | First review at ≥30 closed E2 signals **and** 6 months (§三) | `ledger_v66.py:243`. The CRO ruling §5 says "whichever is later". | **VERIFIED** |
| 15 | S1–S3 definitions; "1股 > US$192.31" (§三) | `ledger_v66.py:266-281`. 15% × HK$10,000 / 7.8 = US$192.31. | **VERIFIED** |
| 16 | S4: "扣真實收費後淨盈虧 ≤ 0" (§三) | The code checks realised fill P&L ≤ 0 **only if** the V1 gate is True **and** there are ≥10 closed trades (`ledger_v66.py:284-285`). The CRO's pre-registered S4 is "V-1 shows net EV ≤ 0 at the real fee" (`reports/risk/2026-11-24-swing-notional-cap-cro.md` §5). | **REDEFINED, threshold undisclosed** → F-8 |
| 17 | B′ enable procedure; "少任何一樣,程式會拒絕啟動" (§四) | The refusal is real (`config_v66.py:65-76`), invoked through `stamp()`, ledger `main`, bot `main` and `live_mode()`. **Doing the full procedure makes selftest fail** (`selftest.py:139` expects `live_mode()=="A"`; `selftest.py:142-149` expects B′ to be blocked). The .bat then refuses to scan. ① ignores B′ in any case (`daily_scan_v66.py:146, 172` use A sizes only). | **FALSE AS AN OPERATING PROCEDURE** → F-1 |
| 18 | "20% 同無上限已被否決" (§四) | CRO ruling §4.3. `config_v66.py:69` asserts the B′ cap is ≤ 15. | **VERIFIED** |
| 19 | Token file at `%USERPROFILE%\.swing_bot_token`, never in the folder or a .py file (§五.1) | `telegram_bot_v66.py:45-46, 61-71`. A token file inside the package folder is refused (69–70). | **VERIFIED** |
| 20 | The console prints your chat ID; only that ID gets replies (§五.2–3) | `telegram_bot_v66.py:215-233` | **VERIFIED** |
| 21 | HK stocks are never traded (§五.4) | `telegram_bot_v66.py:141-142` | **VERIFIED** (a deviation from the plan; see F-18) |
| 22 | Pine title 「Swing V6.6.0 雙引擎」 (§六.1) | `pine/swing_v66.pine:17` | **VERIFIED** |
| 23 | Golden check: pick 5 rows and compare score, R, stop %, tier and breakout; scores should match (§六.3) | `golden_v66.csv` has 24 rows (6 E2 trade / 5 E2 log-only / 7 E1 / 6 no-signal). Pine's tier and E2-trade flags also require ≥1 affordable share at 10% (`swing_v66.pine:85-87, 104-106`), and `golden_export.py` does not model that. **6 of 24 rows** are priced above US$128.21 on the signal date, which will show as false mismatches. | **WILL MISFIRE** → F-4 |
| 24 | Pine draws the E2 trailing stop from the entry date (§六.4) | `swing_v66.pine:131-142` starts the trail from the entry bar's close and high. The lab and scanner ④ start from the signal-day stop and the entry price (`lab.py:294-300, 333`; `daily_scan_v66.py:229-239`). | **DIFFERENT NUMBER** → F-5 |
| 25 | `lab.py --mode ab/sens/caps/baseline --path bt/scan --source yf` (§七) | `lab.py:649-655` | **VERIFIED** |
| 26 | Research figures: ~2.2%/yr, +US$116, scanner ~0.8%/yr, −0.8% in 2025–26, E1 OOS −0.16%, E2-only rejected, 3.6×ATR not adopted, every E2 ±20% perturbation positive (§七) | `summary.csv` rows 27, 38, 47, 53, 56; `baseline.json`; `sensitivity.csv` (E2 IS/OOS range +0.61 to +2.13) | **NUMBERS VERIFIED; framing one-sided** → F-3 |
| 27 | File table (§八) | Every listed file exists. The "core" column equals `CORE_FILES` exactly. | **VERIFIED** |
| 28 | `ledger/` and `data/` are not uploaded (§八) | `.gitignore` lines 3–4 | **VERIFIED** |
| 29 | "冇任何程式會落單" (footer) | Grep for broker and order APIs (§5) | **VERIFIED** |
| 30 | Decision box: live path bt; E1 as backtested; E2 has slot priority; cap A (top) | `config_v66.py:26-31`; `signals_v66.py:58-70`; `rank_key` | **VERIFIED** |
| 31 | "V6.6 冇改任何訊號規則、冇改任何鎖死參數" (top) | The `rules_v642.py` constants are unchanged. The **daily list does change**: per-trade E1 is 737 signals on the bt path vs 217 on the scanner path, and E2 is 350 vs 416 (`summary.csv` rows 21/22 vs 30/31). | **TRUE but incomplete** → F-16 |
| 32 | "一套規則,所有工具共用" (top, item 3) | The backtest uses its own path gate, `lab.build_signal` (`lab.py:121-161`), held equal by `equivalence_check.py`. Pine is a hand port. | **OVERSTATED (minor)** → F-17 |

## 2. Commit messages — claims checked

V6.6 commits in scope, from `.git/logs/HEAD` lines 48–59: 451b11e, a068781, e07f219, 9141e85, 7064ded, a46190c, d361dc3, 3a87f3c, 3ab4556, 56293b2, 471c290, 4d0b69e.

| Claim (as quoted in the brief or in the subject) | Checked against | Result |
|---|---|---|
| Selftest has "50 checks" / "54 checks" (earlier V6.6 phase commit bodies) | Static count of `check()` sites in `selftest.py` = **47** (see §1 #2). The CEO's own correction commit 4d0b69e (`.git/COMMIT_EDITMSG` line 1) says "earlier commit messages said 50/54 - wrong". | **ERROR, recorded.** History is immutable, so 4d0b69e is the erratum of record. See F-19. |
| Equivalence: **85,120** comparisons, 0 differences (Webull data) | `equivalence_check.py:23-30` iterates `range(80, len(df))` × 2 paths per ticker. All 38 universe CSVs have exactly **1,200** rows (Grep count over `data/`). 38 × 1,120 × 2 = **85,120**. | **Count VERIFIED arithmetically. The zero-difference result is UNVERIFIED (not run).** See caveat C-2 below. |
| Equivalence: **39,520** comparisons (synthetic, in selftest) | `selftest.py:107-117` uses `synth(n=600)` over 38 tickers: 38 × 520 × 2 = **39,520** | **Count VERIFIED arithmetically** |
| `ledger_check`: **38/38** (bt per-trade), **21/21** (scan per-trade), **8/8** (2-slot book) identical | `ledger_check.py:33-46` prints `ref N resolve N IDENTICAL` in exactly this shape. The window is 2025-03-03 → 2025-05-30 (line 15). | **Shape consistent; values UNVERIFIED (not run).** Caveat: both sides call `lab.simulate`, so this tests the ledger round-trip (serialisation and price rescaling), not the exit logic. |
| Baseline hashes vs `results/baseline.json` | `baseline.json` matches `summary.csv` on every metric: bt 135 / EV 0.8061 / CAGR 2.2056 / US$116.32 (row 38); scan 96 / 0.4734 / 0.8206 / US$42.39 (row 47); per-trade bt 1,087 / 0.3954 (row 20); per-trade scan 633 / 0.9111 (row 29). It also matches `caps.csv` rows 2 and 32. | **Metrics VERIFIED.** The hashes (`3044c31236e877f0`, `1ab4dbb940429ce0`, `1b9e39ef519eca38`, `127cc0c250b65537`) cannot be recomputed without execution, and the commit-body text was unreadable, so they are **UNVERIFIED**. |
| a46190c moved the scanner path: CAGR 0.815 → 0.821%, per-trade scan 631 → 633 | The post-state is confirmed: `baseline.json` scan CAGR 0.8206 and per-trade scan 633. The pre-state cannot be checked without `git show`. | **Post-state VERIFIED.** The lab report was not refreshed (§4). |
| Screenshot cross-check: CVX US$209; PFE 8 shares = US$229 (6 and 28 Sep scans) | Webull adjusted closes: CVX 2026-09-04 $206.88 and 09-28 $204.67 (`data/CVX.csv:1146,1161`); PFE 09-25/28 $28.26–28.31 (`data/PFE.csv:1160-1161`), so 8 × ~$28.6 ≈ $229. Raw prices sit slightly above adjusted ones. | **Prices plausible.** The conclusion "so pre-V6.4.2 code was running" is **inference stated as fact** → F-20 |

**Caveat C-2 (evidence inflation).** The 85,120 and 39,520 figures count every (day, ticker, path) cell. Most of those cells have no signal on either side and agree trivially. Both sides also call the same `rules_v642` functions on the same indicator rows (`lab.precompute` at `lab.py:216-229`; `signals_v66.evaluate` at `signals_v66.py:23-52`). The test therefore proves that the **path-gating wrapper** agrees. It does not prove the rules or the indicators correct; that is V-3's job. Any commit text that cites 85,120 as validation strength should say this.

## 3. Plan vs delivery — deviations

| # | Plan item (vast-beaming-lynx.md) | Delivered | Assessment |
|---|---|---|---|
| P-1 | Phase 2 `review`: "**Earnings** inside the hold are flagged". The CRO ruling §5 also requires an "Earnings log" for every exception-tier position. | `earnings_date` is logged (`ledger_v66.py:41`; `daily_scan_v66.py:163`), but `review()` never reads it (Grep for `earning\|財報` in `ledger_v66.py` finds only line 41) | **NOT DELIVERED.** CRO-mandated. Must exist before B′ → F-9 |
| P-2 | Phase 4 Pine: "The trailing-stop plot is **deferred**; use an optional `input.time` entry date" | A trailing-stop plot was shipped (`swing_v66.pine:131-142`), initialised differently from the lab and scanner | **Delivered differently** (scope added, with divergence) → F-5 |
| P-3 | Phase 2 S2 includes an "**out-of-order** ... trade" | Out-of-order is a 「留意」 note and never counts as a breach (`ledger_v66.py:127-128`; review counts only `"S2" in flags`, line 270) | **Weakened** → F-14 |
| P-4 | S4 is "the fee gate fails" (plan); CRO: "V-1 shows net EV ≤ 0 at the real fee" | Realised fill P&L ≤ 0 after ≥10 closed trades, and only with V1=True (`ledger_v66.py:284-285`) | **Redefined** → F-8 |
| P-5 | Repeat E2 signals for a held **or logged** ticker are "flagged, not double-counted" | Only Owner-held tickers are flagged (`held`, `daily_scan_v66.py:165`). Double-counting is prevented by `lab.simulate` skipping open tickers (`lab.py:370-381`). | **Partial** (LOW) |
| P-6 | Cap return comparison suppressed until n ≥ 100 | No comparison exists; `review` prints a count and a reminder (`ledger_v66.py:249-255`) | Acceptable |
| P-7 | Verification 5: `review` flags **synthetic S1–S4** breaches | Selftest covers S1 and S3 (`selftest.py:218-219`); `ledger_check` exercises S2 via `fill`; **S4 is untested** | **Partial** (LOW) |
| P-8 | Phase 0 Owner action: confirm whether any order was placed from the 6/28 Sep scans (CRO 7.6) | Missing from README §一 | **Omitted** → F-15 |
| P-9 | Phase 5: Tom's review, the audit and the CRO sign-off are committed **before** the README tells the Owner to switch. 腦大裝草 records the decision. Owner summary `reports/quant/2026-11-xx-v66-release.md`. | Tom's release review (`reports/quant/2026-11-24-v66-release-code-review.md`) is a skeleton with every section `_pending_`. The CRO sign-off (`reports/risk/2026-11-24-v66-release-cro-signoff.md`) is "DRAFT", all `_pending_`. `memory/decisions/2026-11-2*` has no files. There is no Owner summary file. The README has instructed the switch since 471c290. | **Sequencing violated** → F-10 |
| P-10 | Phase 3 bot "keeps ... HK ticker support" | HK is analysed but always blocked; tickers outside the 38-name universe are blocked (`telegram_bot_v66.py:139-142`) | Sensible, but a new restriction that is **not recorded as an Owner decision** → F-18 |
| P-11 | Phase 4 golden: rows "well away from thresholds" | Thresholds on score, R, RSI2, stop and ADX are respected (`golden_export.py:47, 59-64`). The **affordability threshold that Pine gates on** is not. | **Gap** → F-4 |
| P-12 | Delivered as planned (spot-checked) | Config flags and `check_config`; fingerprint with CRLF normalisation (`config_v66.py:50-58`; `selftest.py:165-171`); the CRO V-2 six cases verbatim (`selftest.py:131-136` = CRO ruling §5); `.bat` with CRLF on 23/23 lines, no BOM, and `.gitattributes` `*.bat -text`; `data/` and `ledger/` gitignored; stamp shows versions and path; `--asof`/`--source csv`/`--dry-run`; partial-bar and failed-download warnings; BOM written once; rescaling resolve; bot token handling; the a46190c R-from-`plan["r"]` fix landed as its own commit with a new baseline | **OK** |

## 4. Lab report vs README vs results/summary.csv

The README's 「研究結論」 numbers agree with `summary.csv` and `baseline.json`; F-3 concerns their framing. The lab report was **not refreshed after a46190c or after the Phase 0 re-run of `sensitivity.csv`**:

| Lab report location | Report says | Current results file says | Result |
|---|---|---|---|
| §2 table, per_trade scanner path | 631 trades, gross +1.12, net +0.92, CI [+0.22, +1.75] | `summary.csv` row 29: **633**, +1.11, **+0.91**, **[+0.23, +1.72]** | STALE |
| §2 table, as_traded scanner path | gross +0.71, net +0.51, CI [−0.72, +2.19] | row 47: **+0.67**, **+0.47**, **[−0.77, +2.15]** | STALE |
| §2 engine table, E1 scanner IS | +0.15% | row 33: **+0.13%** | STALE |
| §2 engine table, E2 scanner IS/OOS; E1/E2 bt | +2.00/+0.17; +0.23/−0.16; +1.33/+0.86 | rows 34/37, 24/27, 25/28 | OK |
| §4 and §5, scanner CAGR all/IS/OOS at 10% | 0.81 / 2.29 / −0.82 | rows 47/50/53 and `caps.csv` 32–34: **0.82 / 2.30** / −0.82 | STALE (rounding-level) |
| §4, scanner E1/E2 net EV (all) | +1.83% / −0.22% | rows 48/49: **+1.54% / −0.14%** | STALE (0.3pp on E1) |
| §4, backtest-path E1/E2 | +1.85% / −1.03% | rows 39/40 | OK |
| §5 cap curve, bt and other scanner rows | as printed | `caps.csv` rows 8–31 and 38–58 | OK (scan 15% DD −3.45 printed as −3.5; borderline) |
| §3, E2 ±20% range | +0.61% to +2.13% | `sensitivity.csv` rows 23 and 29 | OK |
| §3, "E1 ... OOS (**−0.06% to +0.90%**)" | — | `sensitivity.csv` OOS E1: **−0.20%** (row 12) to **+0.77%** (row 66) | **WRONG / pre-9141e85** → F-21 |
| §6.8, "parity_check.py must pass at **≥99%** ... tightening is open" | — | Tom F-6 and `parity_check.py:29`: **≥98% on signal days**, and the tightening is shipped | STALE |
| §7, "`selftest.py` (16/16)"; breakout gate and stamp "Recommended, Owner applies" | — | 47 checks; V6.6 ships both | STALE (superseded by the release) |
| §6.7, "so pre-V6.4.2 code was running" | — | Tom's lab review row 8 (`2026-11-24-v66-lab-tom-review.md:287`) asked for this to be labelled inference. Not done. | **Inference-as-fact** → F-20 |

**Do the conclusions survive?** Yes. Every stale figure moves by ≤0.3pp, and none changes a sign, a ranking or a recommendation. The README cites this report as its source, so the report must be current. The CRO cap ruling also quotes pre-fidelity figures ("631 signals", scanner 0.81). That file is outside this audit, but it is noted for the CRO's sign-off.

## 5. Owner-facing safety claims

| Claim | Evidence | Verdict |
|---|---|---|
| **Token handling** | Token comes from env `SWING_BOT_TOKEN` or `%USERPROFILE%\.swing_bot_token` (`telegram_bot_v66.py:45-46, 61-65`). The placeholder is refused (66–68). A token file in the package folder is refused (69–70). Only allow-listed chat IDs get replies (231–233). Every exception and status print goes through `redact()`, which removes the literal token plus a regex for the token shape (54–58, 210, 214, 223, 240, 245). The token is never passed to `analyze()`. Selftest covers `redact` and the placeholder refusal (`selftest.py:225-238`). | **PASS.** Residual (LOW): the folder check matches only the exact package folder, not its subfolders. The README does not say how to create a dot-file with no extension on Windows (F-23; fails closed). |
| **"Won't scan if selftest fails"** | `掃描_v66.bat:10-17` with `selftest.py:244-245`. Import errors and crashes also return non-zero. | **PASS for the .bat path.** Caveats: running `python daily_scan_v66.py` directly bypasses it. The failure message sends the Owner to the old V6.4.2 scanner (F-12). Enabling B′ per README makes it fail (F-1). |
| **"B′ cannot be enabled without gates"** | `config_v66.py:65-76`: B′ needs `CAP_MODE` and `B_PRIME_ENABLED` changed together, no outstanding gate, and a non-empty CRO note. It runs from `stamp()`, ledger `main`, bot `main` and `live_mode()`. The ledger's exception path needs `B_PRIME_ENABLED` (`ledger_v66.py:111`). | **PASS as stated.** The gates are booleans that the Owner sets himself, and the CRO note accepts any non-empty string. The control proves deliberate edits, not that V-1 to V-3 actually passed (F-22). |
| **"No broker write path"** | Grep (case-insensitive) over `strategy/v6.6/` for `futu\|webull\|moomoo\|ib_insync\|ibapi\|alpaca\|place_order\|placeorder\|modify_order\|cancel_order\|unlock_trade\|OpenSecTradeContext\|TradeContext\|requests\.(post\|put\|delete\|patch)\|urllib\|http\.client\|socket\|subprocess\|os\.system`. The only outbound write is Telegram `sendMessage` (`telegram_bot_v66.py:241`). The `webull` hits are a cost-model label (`lab.py:84, 97, 506, 516`) and a README note. A second Grep for `order\|trade(\|buy(\|sell(\|submit` in `*.py/*.pine/*.bat` returned nothing. Market data comes only from yfinance reads. | **PASS.** Out of scope: `parity_check.py` imports the Owner's own `dual_engine_v6_4.py`, which I have not seen. |

## 6. Findings (numbered, severity, location, correction)

### HIGH

**F-1 · HIGH · README §四 (lines 112–114), `selftest.py:139, 142-149`, `daily_scan_v66.py:146, 172`, `掃描_v66.bat:14`.**
The B′ switch-on procedure, done exactly as written, disables the daily scan.
- With `CAP_MODE="B_PRIME"`, `B_PRIME_ENABLED=True`, every gate True and a CRO note filled, `live_mode()` returns `"B_PRIME"`, so selftest check 「現行 live 模式 = A」 fails.
- 「關卡未過 → 開 B′ 會被 assert 擋」 also fails, because `check_config()` now passes. The same failure occurs if the gates are True and the note is filled while B′ is still off.
- The .bat then refuses to scan and tells the Owner to use the V6.4.2 `掃描.bat`, the unvalidated scanner (F-3 of Tom).
- Separately, ① and ③ size from A only. Even a working B′ would never appear on the trade list, while the bot does size by `live_mode()` (`telegram_bot_v66.py:150`). The tools would disagree.
- It fails closed today, because B′ is off.
- **Correction (now):** README §四 should say: 「B′ 開關未完成 —— 未有新版之前唔好改 `config_v66.py`」.
- **Correction (code, before B′):**
  - Make the selftest checks mode-aware: test `check_config` against a copy with gates forced False, and assert that `live_mode()` equals the configured mode.
  - Show the B′ size in ① when `live_mode()=="B_PRIME"`.
  - Add a selftest case for the enabled state.

**F-2 · HIGH · README §一.4 vs §二 (lines 35, 48, 54); `config_v66.py:39-47`.**
The install steps contradict the fingerprint check.
- Step 4 has the Owner edit `config_v66.py` (V3 → True). That file is fingerprinted, so on day one the stamp no longer shows `69b0780a3d5b`.
- §二 tells him that a different fingerprint means 「有人改過規則或設定 → 先問清楚先好交易」. Every later gate flip does the same.
- The doc teaches the Owner to explain away mismatches, which defeats the control.
- The value `69b0780a3d5b` itself appears nowhere but the README, with no committed scan output. Tom's in-progress review may still change core files (`v66-release-code-review.md` line 3: "+ fixes listed in §11").
- **Correction:** either move `GATES` (and the B′ switches) into a non-fingerprinted file that the stamp prints separately, or list the expected fingerprint per gate state. After Tom's fixes, regenerate the fingerprint from a real `--dry-run` and commit that output, for example as `results/release_stamp.txt`.

**F-3 · HIGH · README §七 「研究結論」 (lines 145–148).**
The summary keeps the per-trade framing and drops the result that reverses it in the way the Owner actually trades.
- `summary.csv` rows 39–40 (as_traded, bt): E1 is **+1.85%/trade** over 86 trades, CI [+0.94, +3.58]; this is the only as-traded CI that excludes zero. E2 is **−1.03%** over 49 trades, CI [−2.26, +0.94]. OOS E2 is −2.31% over 19 trades (row 46).
- The lab report §4 says this plainly ("E2 loses money on both paths and E1 makes it: the reverse of the per-trade picture"). The README turns it into 「引擎一...填空檔有幫助」.
- 「穩陣」 overstates the evidence. The robustness shown is that the point estimate keeps its sign under ±20% changes (`sensitivity.csv`). OOS per-trade E2 has CI [−0.02, +2.27] (row 28), which does not exclude zero.
- This bears directly on 「引擎二優先佔倉位」.
- **Correction:** add 「以你嘅方式交易(2倉、10%、整數股),引擎二每筆 −1.03%、引擎一 +1.85% —— 同每筆睇法相反,原因未確定(名額競爭/10%上限都有可能)」. Change 「細但穩陣」 to 「細、對參數唔敏感,但 OOS 統計上未同零分開」.

**F-10 · HIGH · README as a whole; plan Verification 9 and Phase 5.**
- The README has told the Owner to install and switch since 471c290. Meanwhile:
  - Tom's release review is an empty skeleton (`reports/quant/2026-11-24-v66-release-code-review.md`, all `_pending_`).
  - The CRO sign-off is an empty DRAFT (`reports/risk/2026-11-24-v66-release-cro-signoff.md`).
  - There is no `memory/decisions/` entry (CLAUDE.md rule 4).
  - The Owner summary (`reports/quant/2026-11-xx-v66-release.md`) does not exist.
- **Correction:** put a top banner in the README, 「未正式發佈:等 Tom 審核、CRO 簽署、決策記錄」, and remove it only when all three are committed.

### MEDIUM

**F-4 · MEDIUM · README §六.3; `pine/swing_v66.pine:85-87, 104-106`; `golden_export.py`; `pine/golden_v66.csv`.**
Pine's tier and E2-trade flags require ≥1 share affordable at 10%; the golden file ignores affordability.
- Closes from `data/*.csv` on the golden dates: JPM 11-18 $324.11; NVDA 10-26 $216.00 and 11-02 $202.06 (10-28 similar); XOM 10-30 ≈$180; WMT 11-04 $129.17. All are above US$128.21.
- So **6 of 24 rows**, including 4 of the 7 E1 rows, will show `G_E1級別 = 0` or `G_E2交易路徑 = 0` against golden 「普通/強」 or 「E2交易」.
- Golden 「強」 can also legitimately read 2 or 3 in Pine (3 = strong plus OBV divergence). The README gives no mapping.
- **Correction:** add an `affordable_10pct` column (or drop those rows) in `golden_export.py`. Add a README mapping: 普通 = 1, 強 = 2 or 3; when a share is unaffordable, Pine shows 0.

**F-5 · MEDIUM · README §六.4; `swing_v66.pine:131-142` vs `lab.py:294-300, 333`, `daily_scan_v66.py:229-239`.**
- The Pine trail starts at entry-bar close − 3×ATR, with the entry-bar high. The backtest and ④ start from the signal-day stop and the entry price, then ratchet. Early in a trade, Pine's stop can be **lower** (looser) than ④.
- The plan had deferred this plot.
- **Correction:** README: 「圖表止損只供參考,以掃描器④為準」. Alternatively, give Pine an "initial stop" input.

**F-6 · MEDIUM · README §二 line 75; `ledger_v66.py:117-130`; `daily_scan_v66.py:156`.**
The "no live signal" check passes on any earlier live row for the ticker, however old. Live rows are logged with `live=True` even when guard-blocked (earnings ≤5 days, stop too wide) or unaffordable. Buying a stale or earnings-blocked signal is therefore **not** S2.
- **Correction:** require all three of the following, otherwise flag S2:
  - `bar_date` is the last NY session before the fill;
  - `guard_ok=True`;
  - `size_A ≥ 1`.

**F-7 · MEDIUM · `daily_scan_v66.py:105, 186-187`; `ledger_v66.py:82-89, 193`.**
- An intraday run writes partial-bar signals.
- Idempotent keys stop the post-close run from correcting them, and `resolve` does not filter `partial_bar`.
- This corrupts the shadow ledger that the 30-signal review and the B′ evidence rely on.
- **Correction:** skip ledger writes when `partial` is set, or let post-close rows supersede them. The README should say 「開市期間跑唔會寫記錄簿」 once that is fixed.

**F-8 · MEDIUM · README §三 S4; `ledger_v66.py:284-285`; CRO ruling §5.**
- S4 is implemented as realised fill P&L ≤ 0 after ≥10 closed trades, with V1=True. The threshold is undisclosed.
- The CRO pre-registered "V-1 shows net EV ≤ 0 at the real fee", i.e. re-running `as_traded` at the real fee.
- A 10-trade realised-P&L trigger is a different and very noisy test. Changing a pre-registered stop condition needs the CRO.
- **Correction:** John should state which definition binds; then align the README and the code.

**F-9 · MEDIUM · `ledger_v66.py` `review()`; plan Phase 2; CRO ruling §5 "Earnings log".**
- The earnings-inside-hold flag is not implemented. `earnings_date` is logged but never used.
- **Correction:** implement it before B′ can be enabled, or have the CRO waive it in writing.

**F-11 · MEDIUM · README §一.4; `parity_check.py:27, 32-52, 85-93`.**
- 「證明...每日出一樣嘅訊號」 overstates what V-3 checks: 10 of 38 tickers, engine identity only, ≥98% of signal days, and a re-implemented old scanner path.
- Tom showed that a 7% signal-day shift can flip OOS CAGR (lab report §6.8). "一樣" is not the right word for a 98% gate.
- **Correction:** 「證明 10 隻股、有訊號嘅日子 ≥98% 出同一個引擎;止蝕/止盈數值唔喺呢個測試入面」.

**F-12 · MEDIUM · `掃描_v66.bat:13-14`; README §一.2; `selftest.py:20, 189`.**
- On a selftest failure the launcher advises 「臨時可以用返舊版:掃描.bat(V6.4.2)」, which is the scanner V6.6 exists to replace.
- Failures are more likely than they look:
  - F-1;
  - the synthetic trade-list hash depends on numpy and pandas numerics, and the README's `pip install` pins no versions.
- **Correction:** 「今日唔好交易;將 selftest_last.log 畀 AI 睇」. Record the tested pandas and numpy versions in the README.

**F-21 · MEDIUM · Lab report §2–§5, §3, §6.8, §7.**
- The figures are stale after a46190c and the Phase 0 re-run (table in §4). The E1 OOS sensitivity range "−0.06% to +0.90%" matches no row of the current `sensitivity.csv`, which gives −0.20% to +0.77%.
- **Correction:**
  - Regenerate the tables from `results/*.csv` and stamp them with the source commit.
  - Fix the E1 range.
  - Point §6.8 and §7 to the release.

### LOW

**F-13 · LOW · README §三 line 84:** 「分兩部分」 should read 「分三部分」 (【2】 is the cap shadow count).

**F-14 · LOW · README §二 line 75; `ledger_v66.py:127-128`; plan P-3.**
- An out-of-order pick is a 「留意」 note, not S2. Ranks also count already-held tickers (`daily_scan_v66.py:176`), so "#3" can be legitimate.
- **Correction:** state it as a note, or rank excluding held tickers and make it S2 as the plan specified.

**F-15 · LOW · README §一:** the CRO 7.6 / plan Phase 0 request (did any order follow the 6 or 28 Sep scans?) is not in the Owner's checklist. Add it as step 7.

**F-16 · LOW · README top:** 「冇改任何訊號規則」 is true of the rule definitions, but the Owner's list will now include BASIC-tier E1 (bt per-trade E1 737 vs 217 on the scanner path, `summary.csv` rows 21/30, about 3.4×), and E2 will need a breakout. Say so, so that the larger E1 list is not a surprise.

**F-17 · LOW · README top item 3:** 「一套規則」. The backtest's path gate is a second implementation (`lab.build_signal`) kept equal by `equivalence_check.py`, and Pine is a hand port. Suggested wording: 「同一套規則函數;回測同掃描器經等價測試確認一致」.

**F-18 · LOW · `telegram_bot_v66.py:139-142`:** blocking HK and non-universe tickers is a new restriction. Record it as an Owner decision in the decision log.

**F-19 · LOW (recorded) · V6.6 phase commit bodies:** "50/54 checks" vs the actual 47. The erratum is 4d0b69e. For 床狗: commit-message counts must be pasted from tool output, not written in advance.

**F-20 · LOW · Lab report §6.7:** "so pre-V6.4.2 code was running" is an inference. The prices fit the data, and the V6.4 scanner sizes through the imported `position_plan` (`strategy/v6.4/daily_strong_signals.py:36, 110, 128`), but Tom's alternatives (manual sizing, a different account setting) are not excluded. Label it "inferred".

**F-22 · LOW · README §四 lines 105–114; `config_v66.py:39-44, 74`.**
- The gates are flags the Owner sets himself, and any non-empty note satisfies the CRO check.
- The README never says when to flip V1 or V2.
- It omits the CRO's own preconditions: Mo Peter's VaR and Mario's stress test "before any real-capital change", and "paper first" if CL-8 still applies.
- 「將四個 GATES 改做 True」 is wrong: G1 is already True.
- **Correction:** state these points explicitly.

**F-23 · LOW · README §一 and §五:**
- `copy ..\dual_engine_v6_4.py .` assumes the old files sit in v6.6's parent folder.
- `%USERPROFILE%\Desktop` may be OneDrive-redirected.
- Parity needs `ta`, but no install command is given.
- Creating `.swing_bot_token` in Notepad can produce `.txt`.
- **Correction:** give explicit commands, e.g. `notepad "%USERPROFILE%\.swing_bot_token"`.

## 7. Checklist C1–C10

| # | Check | Result |
|---|---|---|
| C1 | Load-bearing numbers traceable to a file or source | README figures → `summary.csv`/`baseline.json` ✔. Fingerprint `69b0780a3d5b` ✘ (F-2) |
| C2 | Hallucinated files, functions or events | None found. Every file, flag, CLI option and function named in the README exists |
| C3 | Internal contradictions | F-1 (B′ procedure vs selftest), F-2 (step 4 vs §二), F-13 (two vs three parts) |
| C4 | Inference stated as fact | F-20 (screenshots → old code); F-11 (parity "一樣") |
| C5 | Unbounded claims | 「每日出一樣嘅訊號」 (F-11); 「穩陣」 (F-3); 「一套規則」 (F-17). 「唔過關就唔會掃描」 is properly scoped to the .bat ✔ |
| C6 | Desk-convenient inputs or tests | Equivalence counts dominated by no-signal cells (C-2); golden rows ignore affordability (F-4); parity on 10 of 38 names (F-11); S4 needs ≥10 closed trades (F-8) |
| C7 | Conclusion strength > evidence strength | README 「研究結論」 (F-3) |
| C8 | Staleness after re-baselining | Lab report (F-21); CRO cap ruling quotes pre-fidelity 631 / 0.81 (outside scope; noted) |
| C9 | Commit-message accuracy | 50/54 vs 47 (F-19). The rest is arithmetically consistent or unverifiable without execution |
| C10 | Direction of bias | Every documentary error found makes V6.6 or E2 look **more validated** than the evidence shows (F-3, F-11, C-2, F-21's E1 range is the exception: it overstates E1). The code's safety controls err **conservative** (fail closed). See §8 |

## 8. Bias observations

1. **Narrative lock-in on "E2 has the edge".** The framing runs from the lab report §0 to the plan Context §2 to the README §七. The as-traded reversal is disclosed once (lab §4) and then lost downstream. The decision 「引擎二優先佔倉位」 sits on the per-trade view only.
2. **Dissent exists but does not reach the Owner.** Tom failed the first lab version, and the CRO's own V-0 test failed B′ on the scanner path. Neither caveat appears in the Owner-facing README. The firm is not short of dissent; the problem is that the README does not carry it.
3. **The author reviews his own work.** The CEO wrote the lab report ("standing in for Tom"), the plan, the code and the README. Tom's release review and the CRO sign-off, the two independent checks, are empty. Until they land, this audit is the only external read of the release code, and it is static only.
4. **Recency.** The cap and B′ evidence rests mostly on 2025–26 (CRO §5 discloses this). The README's 「2025–26 係 −0.8%」 is a single-regime number. That is fine as stated, but it should not be read as a structural result.
5. **Direction of the errors.** The pro-release errors (F-3, F-11, C-2) all point toward readiness. That is a systematic lean, not noise, and the reason this audit should precede the switch.

**Recurring patterns for 床狗 (prompt fixes):**
- (a) Tables must be regenerated from the results files after any re-baseline commit, stamped "figures from `<file>` @ `<commit>`" (F-21).
- (b) Count claims in commit messages must be pasted from tool output (F-19).
- (c) Owner-facing summaries must carry every material contrary finding from the source report, one line each (F-3).
- (d) Any doc that tells the Owner to edit a fingerprinted file must state the expected fingerprint change (F-2).

## 9. Required fixes before the Owner switches

**Blocking (README re-audit required; text-only, about an hour):**
1. F-10: a "not yet released" banner until Tom's review, the CRO sign-off and the `memory/decisions/` entry are committed.
2. F-1: replace README §四's procedure with 「B′ 開關未完成,唔好改」.
3. F-2: take the gates out of the fingerprint, or document the expected change. Regenerate `69b0780a3d5b` from a real `--dry-run` after Tom's fixes and commit the stamp output.
4. F-3: add the as-traded engine reversal and soften 「穩陣」.
5. F-12: the .bat failure text must not route the Owner to V6.4.2.
6. F-4 and F-5: add the golden-file and Pine-trail caveats to README §六.

**Before the ledger is used as evidence, or before B′:**
- Code fixes: F-6 (fill check), F-7 (partial-bar writes), F-9 (earnings-in-hold).
- CRO rulings: F-8 (S4 definition) and F-22 (VaR, stress and paper preconditions).
- Wording: F-11 (parity).
- Code: the F-1 changes (selftest and ①).

**Lab report:** F-21 (regenerate the tables; fix the E1 range) and F-20 (label the inference).

**Recorded, no action:** F-19.

*Static audit only: I executed no code. The values I could not verify (fingerprint, trade-list hashes, ledger_check 38/21/8, equivalence zero-diff) need Tom's execution log before CRO sign-off. Research and decision support; not financial advice. No agent of this firm places orders.*
