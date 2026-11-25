# CRO verification of V6.6.2: pre-switch fixes C-4r, N-1, N-5, plus C-3r, B-4, B-11 and N-10

**Author:** John, Chief Risk Officer (Dept 6) · **Date:** 2026-11-25
**Scope:** `git diff 7f74e2c be74475 -- strategy/v6.6` only: 8 files, +349/−83, at **HEAD `be74475`, rules fingerprint `0b05757d0076`**. The fingerprint was computed in both the repo and a scratch copy, and it matches `README.md:79,85`.
**Concurrent commits:** while this verification ran, two docs commits landed: `96d06d8` and `20b781d`. They touch `README.md`, the message text in `parity_check.py`, and `results/release_stamp.txt`. None of these is in `CORE_FILES`: at HEAD `20b781d` the fingerprint is still `0b05757d0076` and `baseline.json` is unchanged. I did not review those commits; that is Ai 管理層's scope. The working-tree change to `reports/committee/2026-11-25-v66-2-docs-reaudit.md` is not mine.
**Standard:** my C-5 re-check `reports/risk/2026-11-25-v66-c5-recheck.md` §4: pre-switch C-4r, N-1 and N-5; C-3r before the first review; B-4 and B-11 before B′.
**Method:** I checked the code and ran it. I did not rely on the commit message.
- All probes ran on scratch copies of the package (`git archive be74475`, with the gitignored `data/` symlinked in).
- selftest was also run in the repo itself: 82/82, normal and `-O`.
- `git status` is clean afterwards and no tracked file was modified.
- There was no broker access, no order of any kind and no `pip install`, and no token was read.
- Three temp dirs left in `/tmp` by `ledger_check.py` during my runs were removed (N-17). Pre-existing `/tmp/tmp*` dirs that I did not create were left alone.

---

## 0. Verdict

**V6.6.2 FIX VERIFICATION: PASS.** C-4r, N-1, N-5, C-3r, B-4 (K7/K8), B-11 and the regression suite all pass under probe.

**Code side of the switch to A: CLEAR, with one new condition (N-12).** A `fills.csv` written by V6.6.0 or V6.6.1 has an 18-column header. The first V6.6.2 `fill open` appends a 19-column row to it, and every later read crashes. After that the scanner fails on every **bull** day. Either of these satisfies N-12:
- **(a)** a small migration fix plus a selftest case, which I re-verify with scope limited to that diff (**preferred**: the control should be structural);
- **(b)** the Owner confirms that `ledger\fills.csv` does **not** exist on his PC when V6.6.2 is installed.

**The switch itself is still NOT YET authorised.** The Owner items in §5 are open: V-2, C-6, C-7, V-1 and V-3. Waiting costs nothing: SPY has been below its 200-day MA since 2026-11-19 (`data/SPY.csv`: 722.29 on 2026-11-23, bear per the scanner), so the system lists no trades.

**B′ stays OFF.** B-4's K7/K8 holes are closed. The rest of the B′ list is open (§4).

**Risk score: 76.** This is the score I committed to once C-4r, N-1 and N-5 were verified, and it is conditional on N-12. B′ stays at 74, conditional and OFF.

## 1. Item table

| Item | Result | Evidence |
|---|---|---|
| **C-4r (a)** Heartbeat on every non-dry, non-partial run, including bear days; never from an as-of or CSV run into the live ledger | **PASS** | **Code:**<br>- `daily_scan_v66.py:109-120` `_ledger_write`: no write on dry run, on as-of/CSV into the live ledger, or on a partial bar.<br>- `:152`: heartbeat on the bear branch. `:228`: heartbeat after `append_signals` on bull days.<br>- `ledger_v66.py:96`: `append_run` is idempotent per `bar_date`.<br>**As-of scans 17–23 Nov into a test ledger:** 5 heartbeats, 3 of them bear (19, 20, 23 Nov → `bull=False`).<br>**End-to-end simulation** on the real `yf` code path:<br>- clock injected; scans at HK 08:00 every calendar day, weekends and holidays included, plus HK 23:00 on weekdays (NY intraday); 2025-01-01 → 2026-11-24;<br>- 1,188 scanner runs → **476 heartbeats (419 bull / 57 bear)**;<br>- every NYSE session in the window has exactly one heartbeat;<br>- **0 duplicates, 0 heartbeats on non-sessions, 0 written intraday**;<br>- weekend and holiday runs re-see the last session and are no-ops.<br>**As-of/CSV runs into the live ledger:** P1a–P1g were all refused and the live `ledger/` stayed empty (§1 C-3r). The selftest C-3r case also asserts there is no `runs.csv` in the live ledger. |
| **C-4r (b)** `fill open` S2 when the last scanned bar before the fill was bear | **PASS** | `ledger_v66.py:166-172`.<br>**F1 re-run** (PFE live 2026-11-18; bear on 19, 20 and 23 Nov; fill 2026-11-24) → `S2:冇 live 訊號(bear:上次掃描2026-11-23係熊市,系統停手)`. At `7f74e2c` this fill was accepted as `live` with no flag.<br>**Controls:**<br>- the same signal filled 2026-11-19 with heartbeats to 18 Nov → **no flags**;<br>- a fill dated 11-19 in the full ledger (last bar before the fill is 11-18, bull) → no flags. |
| **C-4r (c)** S2 when that bar has no live row for the ticker | **PASS** | `ledger_v66.py:175-181`. On the last bar:<br>- scan-only row → `S2:冇 live 訊號(scan_only)`;<br>- guard-blocked row → `S2:護欄擋咗(財報2日內)`;<br>- ticker seen on an earlier bar only → `stale:上次掃描2026-11-18冇呢隻`;<br>- ticker never seen → `none:…`;<br>- no `runs.csv` at all → `none:冇掃描記錄`. |
| **C-4r (d)** S2 when more than one NYSE session was missed | **PASS** (one documented limitation → N-14) | `ledger_v66.py:105-128,173-174`.<br>**Missed sessions:**<br>- F1b (heartbeat 11-18, fill 11-20) → `漏咗1個交易日`;<br>- F1c (fill 11-24) → `漏咗3個交易日`.<br>**Calendar:** the computed 2025–2028 holidays match NYSE Group's published 2026–2028 calendar:<br>- Juneteenth: Fri 2026-06-19, observed Fri 2027-06-18, Mon 2028-06-19;<br>- July 4: observed Fri 2026-07-03 and Mon 2027-07-05;<br>- Christmas: observed Fri 2027-12-24;<br>- New Year 2028 (a Saturday) is **not** observed on Fri 2027-12-31.<br>**Boundary cases: 18/19 correct**, including:<br>- Thanksgiving Wed→Fri = 0 and Wed→Mon = 1;<br>- Black Friday half-day → Mon = 0;<br>- Christmas 2026; NY 2027; Juneteenth 2026/2027; July 4 2026/2027; Christmas 2027;<br>- NY 2028 = 1; Good Friday 2027; MLK 2027;<br>- weekend; same day; next day.<br>The one miss is the ad hoc closure of 2025-01-09 (national day of mourning), which **over-reports** by one session. This matches the docstring (N-14).<br>Default fill date = NY date (`:143`): in all 237 simulated fills recorded from HK, `open_date` equalled the NY session. |
| **C-4r (e)** Stop tolerance 1¢ | **PASS** | `ledger_v66.py:192` `a.stop > sys_stop + 0.01 + 1e-9`.<br>- **F12** (+1.1¢, 26.781 vs 26.77) → `S2:…自訂收緊`.<br>- +1.0¢ → not flagged (inclusive).<br>- **F13** (+13¢ on $28) → flagged.<br>- A system stop that prints rounded up by up to 0.5¢ (26.7749 → 26.78) → not flagged, so printed stops do not false-alarm. |
| **C-4r (f)** Shares > `size(fill_px, system_stop, live_mode())` → S2 | **PASS** | `ledger_v66.py:195-198`.<br>- **F6** ($20 E1, system stop $17.80, A = 5; 6 shares at a self-chosen $17.899 stop) → `S2:止蝕17.899高過系統止蝕17.8(自訂收緊);S2:股數6多過系統5股`. At `7f74e2c` this fill was accepted.<br>- 6 shares at the system stop → `S2:股數6多過系統5股`.<br>- 5 shares at the system stop → clean.<br>- A fill priced below the system stop → `股數2多過系統0股`.<br>This closes N-3. Side effect at the fill price: N-15. |
| **N-1** Hermetic selftest: no live earnings lookups, no temp-dir leaks | **PASS** | `selftest.py:337-339`: §8c replaces `D.G.get_next_earnings`, points `L.DEFAULT_DIR` at a temp folder, uses one `tmpS` and removes it in `finally` (`:419`).<br>**K-11 re-run** (`guardrails_v66.get_next_earnings` patched to "3 days away"):<br>- one ticker at a time for all 38, plus all at once: **39/39 runs exit 0 with 82/82**;<br>- **0** calls to the lookup outside §8c and **0** socket connects.<br>**Stronger form:** a fake `yfinance` was installed that answers "earnings in 3 days" for every ticker and raises on any price fetch. Result: 82/82, with **zero** `yfinance` calls of any kind.<br>**Temp dirs:** 0 new after more than 60 selftest runs (normal, `-O`, `PYTHONOPTIMIZE=2`, K-11, mutations). |
| **N-5** Bot shows no plan or size on an unclosed bar | **PASS** | `telegram_bot_v66.py:103-108,139-141,159-161`. PFE, bt signal on 2026-11-18, CSV bars cut at that date:<br>- **No plan, "未收市,收市後再查" shown:**<br>&nbsp;&nbsp;- NY 11:00;<br>&nbsp;&nbsp;- NY 15:59;<br>&nbsp;&nbsp;- NY 08:00 pre-market with a today bar;<br>&nbsp;&nbsp;- HK 02:00 Thu (= NY 13:00 Wed).<br>- **Plan shown:**<br>&nbsp;&nbsp;- NY 16:00;<br>&nbsp;&nbsp;- HK 05:30 Thu (= NY 16:30 Wed);<br>&nbsp;&nbsp;- yesterday's bar viewed the next morning;<br>&nbsp;&nbsp;- the real clock.<br>Weekend → not open. The DST weeks of Nov 2026 and Mar 2027 are handled by the tz conversion.<br>Half-day sessions block 13:00–16:00. That is conservative, and it shows "check after close", not S2. |
| **C-3r** As-of guard by realpath/normcase; CSV counts as as-of; `resolve`/`review` exclude `days_er == "off"` | **PASS** (residual N-16) | `daily_scan_v66.py:104-106,132`.<br>**Refused, live ledger untouched, in every case:**<br>- P1a: default;<br>- P1b: `ledger`;<br>- P1c: `./ledger/`;<br>- P1d: `x/../ledger` and `ledger/./../ledger//`;<br>- **P1e: a symlink to the live ledger** (wrote 15 rows at `7f74e2c`);<br>- P1e2: a symlink to the package dir plus `/ledger`;<br>- P1e3: an absolute path from another cwd;<br>- **P1g: `--source csv` without `--asof`** (wrote 121 historical rows at `7f74e2c`), with and without `--ledger ledger`.<br>**Case variants:**<br>- On Linux, `LEDGER` is a different directory, so it is not the live ledger.<br>- On Windows, `ntpath.normcase` maps `C:\Users\…\ledger` and `c:/USERS/…/LEDGER` to the same string. This is by inspection plus a unit check; it was not run on Windows.<br>**Downstream exclusion** (`ledger_v66.py:271-272,307-308`):<br>- An all-as-of ledger → `resolve` returns None ("ledger 未有可計嘅訊號"), and `review` §【2】 is absent.<br>- A mixed ledger → `resolve` uses only the 3 live-type bar dates: 25 result rows, against 72 with `include_asof`. `include_asof` is not exposed on the CLI.<br>CSV as-of rows now carry `days_er = off` (PFE 2026-11-18 row). |
| **B-4** K7 (unlisted note) and K8 (string `"false"` gates) refused | **PASS** for the K7/K8 scope (the N-6 part of B-4 is still open, pre-B′) | `config_v66.py:44` `APPROVED_BPRIME_NOTES = ()`; `:85` `is True`; `:118` `is not True`; `:138-142` `isinstance` checks; `:151` membership check.<br>Settings variants, each identical under normal and `-O`:<br>- K0 as shipped → accepted, mode A.<br>- **K7** (all gates true plus `reports/risk/2099-01-01-fake.md`) → **REFUSED** "唔喺 APPROVED_BPRIME_NOTES".<br>- K7b (correct-format note, not listed) → refused.<br>- **K8** (V gates `"false"`) → **REFUSED** "關卡要寫 true 或 false(唔好加引號)".<br>- Also refused: `"true"` gate, `"false"`/`"true"` `b_prime_enabled`, gates `1/0`, gate `null`, `b_prime_enabled: 1`.<br>For K7 and K8, `selftest.py`, `daily_scan_v66.py` and `ledger_v66.py review` all **exit 1**, so the launcher goes to FAILED. |
| **B-11** `lab.py` fingerprinted | **PASS** | `config_v66.py:94`. Appending one line to `lab.py` changes the fingerprint `0b05757d0076` → `881339245e74`, and restoring it gives `0b05757d0076` again. Consequence for V-2: the Owner must copy the **whole** folder. `fingerprint()` silently skips missing files, so a missing `lab.py` shows up as a fingerprint mismatch (fail-visible). |
| **N-10** items | **PASS** (one hygiene residual, N-17) | - `掃描_v66.bat:15` `if errorlevel 1 goto SCANFAILED`, and `daily_scan_v66.py:304` exits 1 when there is no SPY data or too little MA200 history. The file is CRLF (`i/crlf w/crlf`), has no ASCII parentheses and no BOM.<br>- `fills.csv` has gained `logged_at`.<br>- The R-7 docstring is fixed (`daily_scan_v66.py:3`).<br>- README L3 now says paper only ("唔好落真錢"). **That line must be deleted at the switch.** |
| **Regression** | **PASS** | - `selftest.py` **82/82**, exit 0: normal, `-O` and `PYTHONOPTIMIZE=2` in the scratch copy, and normal and `-O` in the repo.<br>- `equivalence_check.py`: **85,120 comparisons, 0 differences**.<br>- `ledger_check.py`: **PASS**. 187 rows, rerun idempotent; "default resolve excludes as-of rows True"; bt 38/38, scan 21/21 and book 8/8 IDENTICAL; S2 over-cap flagged.<br>- `lab.py --mode baseline` (scratch): `results/baseline.json` sha256 `081a485c231a…`, **byte-identical**. `git diff --no-index --exit-code` → 0, and `git diff --exit-code -- strategy/v6.6/results/baseline.json` in the repo → 0. All 9 `results/` files are byte-identical.<br>- `sizing_v66`, `signals_v66`, `rules_v642`, `guardrails_v66`, `indicators`, `lab` and `owner_settings.json` are **unchanged** from `7f74e2c` to `be74475`. |

## 2. Checks run (offline, read-only)

| # | Probe | Result |
|---|---|---|
| K-1 | selftest ×3 modes (scratch), ×2 modes (repo) | 82/82, exit 0 |
| K-2 | `equivalence_check.py` | 85,120 / 0 |
| K-3 | `ledger_check.py` | PASS |
| K-4 | `lab.py --mode baseline` + byte compare | identical (`081a485c231a…`) |
| K-5 | F1, F1b–F1d, F6, F6b/c, F12, F12b/c, F13, F13b; S2 source branches | All as in §1 |
| K-6 | `nyse_sessions_between`, 19 boundary cases; 2025–2028 holiday list | 18/19 (ad hoc closure over-reports) |
| K-7 | **End-to-end false-alarm simulation** (real scanner `yf` path, injected clock, CSV bars as "yfinance"):<br>- scans daily at HK 08:00 plus weekdays at HK 23:00;<br>- rank-1 signal bought at the next session's open at the printed size and the 2-dp stop;<br>- fill recorded at NY 09:45 **without `--date`**;<br>- 2025-01-01 → 2026-11-24 | 297 fills, of which 60 were skipped (open more than 1% from the close, where the Owner is told to recompute). **237 instructed fills, with 0 stale, bear or none S2 across every 2025–26 holiday and DST change.** 1 S2 is the fill-price share check (MU 2025-06-09, N-15) |
| K-8 | K-11: 38 + 1 patched runs; fake-`yfinance` run | 39/39 pass, 0 lookups, 0 sockets |
| K-9 | Bot BOT-N5a–h, plus `bar_still_open` edge cases | §1 N-5 |
| K-10 | P1a–P1g and variants; resolve/review exclusion; hardlink | §1 C-3r; hardlink → N-16 |
| K-11 | `owner_settings.json` K0, K7, K7b, K8, K8b–g, normal and `-O`; selftest, scanner and ledger under K7/K8 | §1 B-4 |
| K-12 | **Mutation test:** each fix re-broken in a copy, then selftest run | **13/17 caught by selftest** (M1–M13).<br>- M14 (resolve keeps "off" rows): caught only by `ledger_check`.<br>- M15 (review keeps "off" rows): **not caught**.<br>- M16/M17 (`bool()` again; no `isinstance`): masked by the other layer, and the behaviour still holds (N-18). |
| K-13 | Upgrade path: V6.6.1 `fill open` (AVGO), then V6.6.2 `fill open` | **Crash on every later read** (N-12) |
| K-14 | Gap scan over CSV history: bt live signals (bull, A ≥ 1) whose next open is within ±1% of the close | 13 of 1,112 (1.2%) would be S2 at the fill price (N-15) |

## 3. New findings

**N-12 (MEDIUM; pre-switch, met by fix (a) or check (b)): `fills.csv` schema upgrade breaks the ledger.**
- **Cause.** `FILL_COLS` gained `logged_at` (`ledger_v66.py:47`). `_append_rows` (`:68`) appends to an existing file without checking its header.
- **Reproduction.** I recorded AVGO with V6.6.1, as my own C-7 instruction asks. The first V6.6.2 `fill open` then wrote a 19-field row under the 18-field header. Every later `read` raised `ParserError: Expected 18 fields in line 3, saw 19`.
- **Effect: on any bull day, the scanner exits 1.** `open_fills` runs in the bull branch, so the launcher prints "[X] 掃描出錯 —— 今日唔好交易" every bull day. Bear days pass, so the fault first shows on the **first bull day**, which is the worst moment.
- **Effect: the ledger cannot be used.** `fill open/close`, `show` and `review` all crash, so S2 detection is blind until someone repairs the CSV by hand in Excel. The ledger rules forbid exactly that kind of hand repair.
- **Why it matters.** It is a recurring false alarm that trains bypassing.
- **Fix (a).** When an existing file's header differs from `cols`, migrate it with read + `_rewrite` before appending. Add a selftest case: an 18-column `fills.csv`, then `fill open`, then `read`.
- **Alternative (b).** The Owner confirms there is no V6.6.x `ledger\fills.csv` on the PC.

**N-13 (LOW–MED; pre-existing; before the first review): legacy positions recorded under C-7 carry permanent S2.**
- The 2 AVGO recorded with `fill` get "no live signal" (K-13). At HK$10,000 they are also 53% notional.
- `review` lists every S2 fill, closed ones included. It then prints "★ 有違規 → 即刻返去 A,通知 CRO" on **every** run for the life of the ledger. A banner that is always on gets ignored.
- **Proposal:** `fill open --legacy`, allowed only for an `open_date` before the switch date. It counts toward the 2 slots and is still checked for cap and risk, but its signal provenance is marked "legacy", not S2.
- I am **not** waiving the cap: if the real account base makes AVGO more than 10%, that S2 stays.

**N-14 (LOW; documented): unscheduled NYSE closures are not in the calendar.** Probe: a heartbeat on 2025-01-08 and a fill on 2025-01-10 (NYSE closed 2025-01-09) → `stale…漏咗1個交易日`.
- This is rare, and it errs on the safe side (over-reports).
- **Owner note:** an S2 "stale 1 session" straight after an unscheduled closure is a known false alarm. Send it to me with the date.
- **Optional fix:** a fingerprinted `NYSE_ADHOC_CLOSURES` tuple.

**N-15 (LOW): the scanner's instruction disagrees with the S2 test at the fill price.**
- **The conflict.** The scanner says: if the open is within 1% of the close, do not recompute (`daily_scan_v66.py:257`). But `fill` checks the cap (pre-existing) and now the share count (C-4r) **at the fill price, with no tolerance**.
- **Gap scan.** 13 of 1,112 instructed entries (1.2%) would be S2: cap 6, share count 13, risk above 1.05% 3. None was on a gap-down open.
- **End-to-end.** 1 of 237 (MU 2025-06-09: 1 share at $109.21, stop $96.28; risk US$12.93 against the US$12.82 budget).
- **These are real, small limit breaches, so S2 is correct.** The instruction is what needs fixing.
- **Recommendation (before the first forward review):** the scanner and the bot print a **maximum limit price** for the printed share count, `min(cap_usd/N, stop + risk_budget/N)`. The Owner then uses a limit order at or below it, which makes the breach structurally impossible.

**N-16 (LOW; defence in depth): the as-of marker is inferred, and fill trusts any heartbeat.**
- Exclusion is keyed on `days_er == "off"`. But a guard row with a stop wider than 15% returns before the as-of branch, so it carries `"?"`: `G.check(…, 20.0, asof_mode=True)["days_er"]` → None.
- **Hardlink probe:** with the live `runs.csv` hardlinked into another folder, an as-of CSV run to that folder appended a historical heartbeat (`2026-11-18, source csv`) into the live file. This takes a deliberate act.
- **Fix:** an explicit as-of/source column on signals, and `fill` ignores heartbeats whose `source != "yf"`. Accepted for the switch.

**N-17 (LOW, hygiene):** `ledger_check.py:13` creates a temp dir with `mkdtemp` and never removes it, so it leaks one dir per run. This is pre-existing and outside N-1's selftest scope.

**N-18 (LOW, test gap):**
- No test covers review's "off" exclusion (M15).
- Resolve's exclusion is tested only in `ledger_check` (M14), which the Owner does not run.
- The two B-4 layers (`is True` and `isinstance`) are each untested on their own (M16/M17). The behaviour is still enforced, because each layer covers the other.
- Fix: add a review-exclusion case to selftest.

**N-19 (LOW; pre-existing; not verified offline because `yfinance` is not installed here):** the scanner and the bot use different rules for an unclosed bar.
- The scanner treats a bar as partial by clock alone, 09:30–16:00 NY (`daily_scan_v66.py:66`). The bot uses "last bar is today's NY date, weekday, before 16:00".
- If `yfinance` ever returns a pre-market row for today, the scanner would write it. Because the ledger keeps the first write for each (date, ticker, path), that row would never be corrected.
- Recommendation: align the scanner with the bot's rule. This is strictly safer.

## 4. Code side of the switch, conditions, risk score

**Code side of the switch to A: CLEAR once N-12 is met by (a) or (b).** C-4r, N-1 and N-5 were the three pre-switch code items in my C-5 re-check, and all three are verified. C-3r, which was due before the first forward review, is also closed.

**Before the first forward review** (not gating the switch):
- N-13 (legacy flag);
- N-15 (limit price printed);
- N-18 (review test);
- N-16 and N-19 when convenient.

**Before B′** (unchanged except where noted):
- **B-4:** the K7/K8 part **passes**. The N-6 part is **open**: `SIGNAL_COLS` and `FILL_COLS` do not yet record `account_hkd`, the live mode or the gate states.
- **B-5:** shadow tiers, and a "財報日不明" flag. Open.
- **B-2:** rule label printed, plus a three-way agreement test. Open.
- **B-3:** the `-O` subprocess case has been **added** (`selftest` "python -O 之下…"). The mode/flag mismatch case is not in this diff.
- **Other gates:** V-1, V-2 and V-3 on the PC; B-6 to B-9; my dated note **plus** its entry in `APPROVED_BPRIME_NOTES`. That entry is a code change, which changes the fingerprint and needs my re-verification.

**Risk score** (input to committee; 0 = do not deploy, 100 = clear at full size):

| Item | Score | Basis |
|---|---|---|
| V6.6.2 at A, code as verified | **76** (conditional on N-12) | As committed in the C-5 re-check.<br>- Both stale-fill routes are closed: across bear days (F1) and across skipped scans (F1b/F1c).<br>- The self-tightened-stop route to an extra share is closed (F6, F12, F13).<br>- The selftest is hermetic.<br>- The bot cannot show a plan on an open bar.<br>- 0 false stale S2 over 23 months of simulated use.<br>Held at 76, not higher, because V-1 is still unverified and N-9 shows the edge is fee-fragile. |
| Real-money entries in a margin account with a debit | **Not deployable** | C-6. Unchanged since 13 Nov (`INDIVIDUAL_MRGN`, USD −12.06). No newer read: NOT OBTAINED. `config/portfolio.yaml` is unchanged since 2026-07-17 (`cash_balance: REPLACE WITH REAL DATA`). |
| B′ | **74 conditional; OFF** | See "Before B′" above. |

**Limits touched** (`config/risk-limits.yaml`, unchanged since 2026-07-17):

| Limit | Value | Status at `be74475` | Pass / fail |
|---|---|---|---|
| Single position | 10% (US$128.21 at HK$10,000) | S2 at fill on notional; now also on share count at the fill price | PASS (N-15 is an instruction fix) |
| Risk per trade | 1% (US$12.82) | S2 above 1.05%; share count at the fill price closes the self-tightened-stop route (N-3) | PASS |
| Concurrent positions | 2 | Unchanged (F3b in the C-5 re-check) | PASS (C-7: unrecorded positions stay invisible) |
| Regime filter (no longs below SPY MA200) | — | A fill after a bear-day scan is now S2 (F1) | **PASS** (was GAP) |
| Leverage | none | Account-side; V6.6 cannot see it | **FAIL ON FACE (account)**, C-6, **5th escalation** |
| Account base | Real net liquidation value | `owner_settings.json:account_hkd`, range-checked only | UNVERIFIED → C-7 |
| Monthly breaker | −10% | Manual | PARTIAL → C-10 |

## 5. Owner items still open

1. **V-2: selftest on your PC. You can run it now; N-1 is verified.**
   - Copy the **whole** `v6.6` folder, `lab.py` included (it is now in the fingerprint).
   - **Before the first run, check whether `ledger\fills.csv` exists. If it does, tell me (N-12).**
   - Double-click `掃描_v66.bat`, then run `python selftest.py` and expect **82** checks passing. Send me `selftest_last.log` and the fingerprint line, which should read `0b05757d0076`.
   - Then set `"V2_代碼測試": true` **without quotes**. With quotes, everything refuses to start (by design, B-4).
2. **C-6: margin and debit, fifth escalation.**
   - Name the account the swing system trades in.
   - Show, from a statement or a read-only pull, that it is a cash account or has margin disabled, with no debit.
   - The Webull account as last read (13 Nov: `INDIVIDUAL_MRGN`, USD −12.06) **does not qualify**. Until this is cured, no V6.6 entry may go into it.
3. **C-7: `account_hkd`.**
   - Set it to the swing account's real net liquidation value, with no borrowed money.
   - Record existing positions such as the 2 AVGO with V6.6.2 `ledger fill`, **only after N-12 is met**.
   - Expect those rows to carry S2 until N-13 lands.
4. **V-1: one Webull contract note** (commission, platform fee, SEC/TAF, FX). N-9: a fixed charge of about US$0.3–0.4 per side (estimate) would make net EV ≤ 0, which is S4: no trading at any cap.
5. **V-3:** run `parity_check.py` on your PC and send the output.
6. **Decisions and carry-overs:**
   - N-11: under A, any S2 → no new entries until explained to the CRO;
   - N-13: a `--legacy` fill flag;
   - N-15: the limit-price instruction;
   - Telegram token revoke/regenerate (Phase 0);
   - CRO 7.6: were orders placed from the 6/28 Sep scans?;
   - README audit re-check (Ai 管理層, CEO to commission). README L3's paper-trading line must be deleted at the switch.
7. **Firm side, before B′:** Mo Peter VaR and Mario stress (B-7) are still not delivered.

**Standing (binding on Zac and 死潘狗 for any ticket):** C-6 to C-10 are unchanged. No V6.6 code can place an order; the Owner places every order. This is research and decision support, not financial advice.

**Source for the NYSE calendar check:** NYSE Group, "NYSE Group Announces 2026, 2027 and 2028 Holiday and Early Closings Calendar" (2025-12-23).
- https://www.businesswire.com/news/home/20251223981478/en/NYSE-Group-Announces-2026-2027-and-2028-Holiday-and-Early-Closings-Calendar
- https://ir.theice.com/press/news-details/2025/NYSE-Group-Announces-2026-2027-and-2028-Holiday-and-Early-Closings-Calendar/default.aspx

These were read through a web-search summary; `nyse.com` itself was not reachable from this session.

---

**For 腦大裝草 (`memory/decisions/2026-11-24-swing-v66-release.md`, V6.6.2 row):**
`2026-11-25 · CRO V6.6.2 fix verification at be74475 / 0b05757d0076: PASS. C-4r (F1/F6/F12/F13 now S2; heartbeat incl. bear days; NYSE calendar incl. holidays), N-1 (K-11 39/39, 0 lookups, 0 temp leaks), N-5, C-3r (P1e/P1g refused), B-4 K7/K8 refused, B-11; selftest 82, equivalence 85,120/0, ledger_check PASS, baseline.json byte-identical. Code side of switch to A CLEAR subject to N-12 (fills.csv 18→19-col upgrade crash; fix or confirm no V6.6.x fills.csv). Switch still blocked on Owner items V-2, C-6 (5th escalation), C-7, V-1, V-3. B′ OFF. Risk 76.`
