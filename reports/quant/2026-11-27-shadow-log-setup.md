# Cloud shadow log: setup and test (2026-11-27 / 28)

**Owner request (27 Nov):** chose "Cloud shadow log" from the options the CEO offered:
> A scheduled cloud check after each US close, using Webull read-only prices. It records what the system would trade, so we build real forward evidence and can cross-check your Telegram.

**Status: built and tested; the scheduled task is PAUSED.** The Owner's choice (28 Nov) was "Pause until I add Webull".

## What was built

| Item | Detail |
|---|---|
| `strategy/v6.6/shadow_run.py` | Research tool, not in `CORE_FILES`; fingerprint `2b7b62182068` unchanged. Flow: Webull `get_stock_bars` JSON → CSV in a temp dir → `daily_scan_v66.scan("csv", …)` into `shadow/ledger/` → `notify_v66.compose_morning()` for the text only. It writes `shadow/YYYY-MM-DD.txt` and one row per bar date in `shadow/shadow_log.csv`, and skips a repeated bar date (holidays). |
| Self-audit (CLAUDE.md rule 1, structural) | Before anything else, the script reads its own source. It refuses to run (exit 2) if it contains `place_order`, `modify_order`, `cancel_order`, `unlock_trade`, `send_message`, `send_text`, `load_token`, `sendMessage`, `api.telegram.org`, `requests.post` or `urlopen`. **Tested:** a copy with `N.send_message("x")` appended exits 2 with "自我審計失敗". |
| Ledger guard | Refuses if the shadow ledger resolves to the Owner's `ledger/` (`daily_scan_v66._same_dir`). |
| Scheduled task `trig_01SyUEo4RbQgSLndoGEqjRxa` | "V6.6 cloud shadow log (Webull read-only)". `CRON_TZ=Asia/Hong_Kong 10 7 * * 2-6`; fresh session per run, environment "horse-monitor". The prompt allows only Webull `get_stock_bars`, never write tools, no Telegram, changes only under `strategy/v6.6/shadow/`, and pushes only to `claude/ai-agent-management-bw44yc`. **Enabled: false.** |

## Tests

| Test | Result |
|---|---|
| Real run on Webull bars pulled 2026-11-27 (39 symbols, 400 bars each, read-only) | Bar 2026-11-25: **bear**, SPY −1.93% vs its 200-day average, no trade list. Files written; committed as the first record. |
| Bull path: `data/` truncated at 2025-06-02, 07-15, 09-10, 10-01 and 05-14 (scratch) | Correct bull/bear and gap. On 2025-05-14: **PFE E1, 6 shares, limit ≤ $20.13, stop $18.70**. The message matches the Telegram format, with the open-check and order rules. |
| Data consistency | Webull bars are split-adjusted (NFLX across the 2025-11-17 10:1 split is continuous). They are identical to the stored `data/` CSVs on overlapping dates (SPY 2026-11-20/23; NFLX 2025-11-13…19). |
| Self-audit | Refuses on a planted send call (above). |

## Blocker and the Owner's step

`create_trigger` in this organization refuses the `connectors` parameter. Sessions fired by the scheduled task therefore have no Webull tools and would only report "Webull not available". The fix is one Owner step in claude.ai:
1. Open Scheduled tasks.
2. Choose "V6.6 cloud shadow log (Webull read-only)".
3. Add the Webull connector.
4. Tell the CEO.

The CEO then re-enables the task and fires it once with `fire_trigger`, checking that a shadow commit lands. The same steps are in `strategy/v6.6/shadow/README.md` (Cantonese).

## Differences from the Owner's Telegram (by design)

- **Earnings check off.** CSV mode has no Yahoo, so a name the Owner's Telegram blocks for earnings can appear here.
- **Data source.** Webull here, Yahoo on the PC. A mismatch on the same bar date is a finding worth reporting: it is the data-source check the Owner asked for on 26 Nov.

*Research record only. No agent of this firm places orders.*
