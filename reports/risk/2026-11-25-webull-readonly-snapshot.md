# Webull read-only snapshot — 2026-11-25

**Prepared by:** 皮褸黃 (CEO), on the Owner's instruction of 2026-11-25. Scope: refresh the facts behind CRO
conditions C-6 / C-7 (V6.6) and G-1 (AVGO margin debit, deadline the 3 Dec 2026 close).

**Source:** Webull MCP, read-only, pulled 2026-11-25 08:13 UTC (16:13 HKT; 03:13 ET, before the US open).
Calls made:
- `get_account_list`
- `get_account_balance`
- `get_account_positions`

No other endpoint was called. Nothing was placed, modified or cancelled (CLAUDE.md rule 1).
`config/portfolio.yaml` and `strategy/v6.6/owner_settings.json` were **not** changed.

## 1. Accounts

| Account | Type / class | Note |
|---|---|---|
| …1311 (redacted) | `MRGN` / `INDIVIDUAL_MRGN` ("Individual Mrgn") | The only account the API lists |

## 2. Balances (as returned; `total_asset_currency` = HKD)

| Field | Value |
|---|---|
| total_market_value | HK$4,590.91 |
| total_cash_balance | HK$−94.25 |
| total_unrealized_profit_loss | HK$−929.55 |
| init_margin | HK$2,368.14 |

**By currency:**

| Currency | cash_balance | settled_cash | market_value | unrealized P/L | interests_unpaid | init_margin |
|---|---|---|---|---|---|---|
| USD | **−12.06** | −12.06 | 587.38 | −118.93 | 0.00 | 302.99 |
| HKD | 0.01 | 0.01 | 0.00 | 0.00 | 0.00 | 0.00 |
| KRW, JPY, CNH | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

## 3. Positions

| Ticker | Qty | Cost price | Total cost | Last price (as returned) | Unrealized P/L |
|---|---|---|---|---|---|
| AVGO | 2 | US$353.16 | US$706.31 | US$293.69 | US$−118.93 |

The pull was made before the US open. Treat `last_price` as the most recent price the API returned
(most likely the 24 Nov close). It is not a live quote.

## 4. Derived (CEO arithmetic; USD/HKD 7.8 as in `config_v66.USD_HKD`)

- **Net liquidation value:** 4,590.91 − 94.25 = **HK$4,496.66 ≈ US$576.49**. This is an estimate,
  computed from the two totals above.
- **AVGO:** 2 × 293.69 = US$587.38, about **101.9%** of net liquidation. The position is carried
  partly on margin.
- **AVGO from cost:** −16.8%.

## 5. What this means for the open conditions

### G-1: margin debit cure, deadline the 3 Dec 2026 close (`reports/risk/2026-11-17-mu-skhy-style-cro.md` §5)

**NOT MET.**
- The account is still a margin account.
- The USD cash is still −12.06, the same figure as the 13 Nov reading.
- The CRO's remedies (any one):
  - deposit or convert currency to clear the debit;
  - sell 1 AVGO;
  - sell both shares;
  - **in addition**, disable margin or convert the account to cash.
- If the debit is not cured by the 3 Dec close, the CRO recommends selling AVGO before its 9 Dec
  results.
- 4–10 Dec is a blackout on **new** positions. Fixing a limit breach is never blacked out.

### C-6: V6.6 swing account must be cash or margin-disabled with no debit

**NOT MET** for this account. See the CRO's wording in `reports/risk/2026-11-25-v66-c5-recheck.md`
§5.2. This read-only pull is the evidence; it shows a margin account with a debit.

### C-7: `account_hkd` must equal the swing account's real net liquidation value

**Material finding.** If this Webull account is the swing account, the real `account_hkd` is about
**HK$4,497**, not the HK$10,000 now in `owner_settings.json`. At that size:

| | At HK$10,000 (current setting) | At ≈ HK$4,497 (real) |
|---|---|---|
| 10% notional cap | US$128.21 | **US$57.65** |
| 1% risk budget | US$12.82 | **US$5.76** |
| Universe names affordable for 1 share at the 23 Nov close (`strategy/v6.6/data/`) | 9 of 38 | **3 of 38** (BAC, NKE, PFE) |

- The V6.6 backtest assumed HK$10,000.
- At ≈ HK$4,497 the system can buy almost nothing. It would also not be the system that was
  tested.
- This does not change any rule. It is an Owner decision:

> **Owner decision needed:** either name and fund a dedicated swing **cash** account with real net
> liquidation ≥ HK$10,000 (and set `account_hkd` to its real value), or do not run V6.6 live.

Suggested `account_hkd`, **not applied**: the real net liquidation value of whichever account the
Owner names. For this Webull account today that is ≈ 4,497.

## 6. Not covered

- **Other brokers:** this pull covers Webull only. Holdings elsewhere are still undisclosed: AAPL,
  3416.HK, 6160.HK, the SKHY sale proceeds, any ETFs (CRO 11-17 §8.6).
- **Margin interest:** whether interest accrues on the USD debit is not shown;
  `interests_unpaid` = 0.00.
- **HKD netting:** whether the HKD side nets the USD debit is not determined. The HKD cash is
  0.01, so it cannot.

*Research and decision support, not financial advice. No agent of this firm places orders.*

---

## Addendum: 2026-11-26 read-only re-pull (G-1 debit cured)

**Source:** Webull MCP, read-only, 2026-11-26 about 15:45 UTC. Calls: `get_account_list`,
`get_account_balance` and `get_account_positions` only. This follows the Owner's statement that
he had cleared all debt.

| Field | 25 Nov | 26 Nov |
|---|---|---|
| Account class | `INDIVIDUAL_MRGN` | **`INDIVIDUAL_MRGN`** (unchanged) |
| USD cash_balance / settled | −12.06 / −12.06 | **+0.66 / +0.66** |
| HKD cash | 0.01 | 0.00 |
| total_market_value (HKD) | 4,590.91 | 4,743.96 |
| total_cash_balance (HKD) | −94.25 | +5.16 |
| AVGO | 2 @ last 293.69 | 2 @ last **303.50** (unrealized −US$99.31) |

**Net liquidation** ≈ 4,743.96 + 5.16 = **HK$4,749** (CEO arithmetic, estimate).

**Status:**
- **G-1 debit: CURED.** USD cash is ≥ 0, before the 3 Dec deadline, so the CRO's sell
  recommendation (triggered only by an uncured debit) does not apply.
- **G-1 structural part / C-6: NOT MET.** The account is still a margin account; margin has not
  been turned off and the account has not been converted to cash. It therefore remains
  **ineligible for V6.6** (CRO 25 Nov §1.1).
- **G-2 (holding AVGO through 9 Dec):** still needs LNW by the 3 Dec close, 老詹's stop, a decision
  record and no adds.
