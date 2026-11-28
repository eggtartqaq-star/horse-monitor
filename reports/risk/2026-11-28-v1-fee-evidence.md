# V-1 evidence: Webull HK real trading costs for US stocks (2026-11-28)

**Source:** screenshots the Owner sent on 2026-11-28: three order-detail screens from the Webull HK app, and the pricing page webull.hk/pricing, tab 「股票、ETF及權證」.
- This session cannot reach www.webull.hk; DNS is blocked.
- Transcribed by the CEO. **No account number is copied** and no image is committed.

## 1. Pricing page (headline, as shown)

| Market | Commission | Platform fee | Quotes |
|---|---|---|---|
| **美國市場**: US stocks and US ETFs | **US$0** | **US$0** | US Level 2 quotes, free on registration |
| 香港市場: HK stocks, HK ETFs, warrants | HK$0 | HK$0 | HK Level 1 real-time streaming, free on registration |
| A股通: Connect stocks and ETFs | RMB0 | RMB15 per order | — |
| 日本市場: Japanese stocks and ETFs | 0 (screenshot cut off) | (cut off) | — |

- **Other tabs, not seen:** 期權, 期貨, 債券, 融資服務, 其他.
- **Not seen:** the 「詳細費用」 detail page (regulatory and pass-through fees).
- **No promotion end date** is visible on the headline.

## 2. Three filled orders (order-detail screens)

| Order | Side and type | Validity | Size and value | Fill | Commission | Platform fee | Regulatory fee (證監會規費) | Total |
|---|---|---|---|---|---|---|---|---|
| CoreWeave, 2026-10-01 | **sell**, stop-market (止損市價單), trigger US$87.00 | **DAY** (當日有效); placed 01:13:27 EDT | 15 sh, US$1,307.78 | avg US$87.185, at 09:31:08 EDT | US$0.00 | US$0.00 | **US$0.03** | US$0.03 |
| AVGO, 2026-10-02 | buy, limit US$353.17, incl. pre/post market | DAY | 4 sh, US$1,412.62 | avg US$353.155, at 10:01:25 EDT | US$0.00 | (row not visible) | (row not visible) | **US$0.00** |
| AVGO, 2026-11-05 | buy, limit US$301.97, all sessions (全時段交易) | DAY | 2 sh, US$603.94 | US$301.97, at 23:50:04 EST (overnight session) | US$0.00 | US$0.00 | **US$0.02** | US$0.02 |

## 3. Reading (CEO; for Tom's fee check and the CRO's V-1 reading)

1. **No minimum fee.**
   - Commission and platform fee are US$0 for US stocks, both on the pricing headline and on all three orders.
   - The firm's planning estimate of a US$0.35 minimum per side (CRO N-9, "real35") is therefore **far above the real cost**.
   - The real cost is cents of regulatory fees, plus the spread and slippage that every model assumes (10 bp per side, an assumption).
2. **Regulatory fee size.**
   - The sell paid US$0.03 on US$1,307.78, about 0.23 bp. That is consistent with the SEC fee on sales (derived; the fee schedule itself was not seen).
   - The regular-hours buy paid nothing.
   - The overnight-session buy paid US$0.02, which is unexpected for a buy. It is recorded as observed and not explained, because the detail page was not seen.
3. **The stop order was DAY, not good-till-cancelled.**
   - The CoreWeave stop was placed overnight (01:13 EDT) as a **DAY** order, and filled at the open, US$0.185 above its trigger.
   - The CRO's M-2 (B′) and the C-9 / F-8 practice assume a broker stop that is **working at every open**.
   - Whether Webull HK offers a good-till-cancelled stop for US stocks is still unknown. It is for the CRO to read.
4. **Status.**
   - The fee for V-1 is **confirmed by the pricing headline and three contract notes**.
   - The detail fee page was not seen. If it shows other pass-through fees, such as FINRA TAF or an overnight-session fee, Tom adds them.

## 4. Next

- **Tom:** `lab.py --mode feecheck --fee-min 0 --fee-bp 10.2 --tif open`, on a scratch copy. That is 10 bp spread and slippage plus about 0.2 bp regulatory fee averaged per side. Also the HK-2 row at the same fee. Output: `reports/quant/2026-11-28-v1-feecheck.md`.
- **CRO:** reads the result and rules V-1 (S4 pass or fail), and rules on the DAY-stop fact.
- **Owner:** a short Cantonese fee sheet from 翻譯官.

*Research and decision support, not financial advice. No agent of this firm places orders.*
