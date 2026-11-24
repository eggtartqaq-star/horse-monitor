# V6.6 release code review — Tom (Backtesting Engineer)

Date: 2026-11-24 · Reviewer: Tom (Dept 3) · Scope: `strategy/v6.6/` at HEAD 4d0b69e (+ fixes listed in §11)
Status: IN PROGRESS — sections are filled one at a time.

## 1. Verdict (per component)

_pending_

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

_pending_

## 5. ledger_v66 (resolve, review S1–S4, fill)

_pending_

## 6. config_v66 structural control and fingerprint

_pending_

## 7. Telegram bot

_pending_

## 8. Pine + golden file

_pending_

## 9. Tests (selftest, equivalence, ledger_check) and the .bat launcher

_pending_

## 10. README accuracy

_pending_

## 11. Changes I made (with re-run results)

_pending_

## 12. What would make this fail live

_pending_
