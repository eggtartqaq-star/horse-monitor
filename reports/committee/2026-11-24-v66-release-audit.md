# V6.6 Release Audit — Ai 管理層 (AI Auditor, Dept 9)

**Date:** 2026-11-24
**Auditor:** Ai 管理層
**Scope:** `strategy/v6.6/README.md` (Owner-facing); V6.6 phase commit messages; approved plan `/root/.claude/plans/vast-beaming-lynx.md` (delivery deviations); `reports/quant/2026-11-24-v642-real-code-v66-lab.md` (consistency with README and `results/summary.csv` after a46190c).
**Audited state:** branch `claude/ai-agent-management-bw44yc` at `4d0b69e` (`.git/refs/heads/claude/ai-agent-management-bw44yc`).
**Method limits:** I had Read/Grep/Glob only, with no Bash. **I executed no script.** Every result below comes from reading the code statically or from committed result files. Commit **subjects** were read from `.git/logs/HEAD` (lines 48–59) and the last message from `.git/COMMIT_EDITMSG`. Commit **bodies** are zlib-compressed objects that I could not read. I checked body claims as the caller quoted them (see §2).

## 0. Verdicts

_(pending — filled last)_

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
| **Token handling** | Token comes from env `SWING_BOT_TOKEN` or `%USERPROFILE%\.swing_bot_token` (`telegram_bot_v66.py:45-46, 61-65`). The placeholder is refused (66–68). A token file in the package folder is refused (69–70). Only allow-listed chat IDs get replies (231–233). Every exception and status print goes through `redact()`, which removes the literal token plus a regex for the token shape (54–58, 210, 214, 223, 240, 245). The token is never passed to `analyze()`. Selftest covers `redact` and the placeholder refusal (`selftest.py:225-238`). | **PASS.** Residual (LOW): the folder check matches only the exact package folder, not its subfolders. The README does not say how to create a dot-file with no extension on Windows (Notepad may append `.txt`; this fails closed). |
| **"Won't scan if selftest fails"** | `掃描_v66.bat:10-17` with `selftest.py:244-245`. Import errors and crashes also return non-zero. | **PASS for the .bat path.** Caveats: running `python daily_scan_v66.py` directly bypasses it. The failure message sends the Owner to the old V6.4.2 scanner (F-12). Enabling B′ per README makes it fail (F-1). |
| **"B′ cannot be enabled without gates"** | `config_v66.py:65-76`: B′ needs `CAP_MODE` and `B_PRIME_ENABLED` changed together, no outstanding gate, and a non-empty CRO note. It runs from `stamp()`, ledger `main`, bot `main` and `live_mode()`. The ledger's exception path needs `B_PRIME_ENABLED` (`ledger_v66.py:111`). | **PASS as stated.** The gates are booleans that the Owner sets himself, and the CRO note accepts any non-empty string. The control proves deliberate edits, not that V-1 to V-3 actually passed (F-11b). |
| **"No broker write path"** | Grep (case-insensitive) over `strategy/v6.6/` for `futu\|webull\|moomoo\|ib_insync\|ibapi\|alpaca\|place_order\|placeorder\|modify_order\|cancel_order\|unlock_trade\|OpenSecTradeContext\|TradeContext\|requests\.(post\|put\|delete\|patch)\|urllib\|http\.client\|socket\|subprocess\|os\.system`. The only outbound write is Telegram `sendMessage` (`telegram_bot_v66.py:241`). The `webull` hits are a cost-model label (`lab.py:84, 97, 506, 516`) and a README note. A second Grep for `order\|trade(\|buy(\|sell(\|submit` in `*.py/*.pine/*.bat` returned nothing. Market data comes only from yfinance reads. | **PASS.** Out of scope: `parity_check.py` imports the Owner's own `dual_engine_v6_4.py`, which I have not seen. |

## 6. Findings (numbered, severity, location, correction)

_(pending)_

## 7. Checklist C1–C10

_(pending)_

## 8. Bias observations

_(pending)_

## 9. Required fixes before the Owner switches

_(pending)_
