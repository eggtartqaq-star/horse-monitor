# ORDER TICKETS — SKHY — 2026-11-13

> **FOR OWNER REVIEW — NOT AN ORDER. NO TRADE OCCURS UNTIL THE OWNER PLACES IT.**
> (Placed manually by the Owner with his broker, or in a paper-trading account. No agent of this firm connects to a broker to transmit, modify or cancel anything. The Webull connector was not touched for this file.)

**Prepared by:** 死潘狗, Execution Trader (Dept 8) · **For:** the Owner, via 皮褸黃 (CEO)
**Instrument:** SK hynix Inc. ADS, Nasdaq **SKHY** (1 ADS = 0.1 ordinary 000660.KS)
**Reference price:** **$131.07** (live read-only Webull print, 19:50 UTC 13 Nov 2026, via coordinator; 12 Nov close $137.71; 13 Nov range $129.18–$135.76). **This is not the 13 Nov close.** The 13 Nov close is NOT OBTAINED.
**Owner's cost:** $129.00/ADS. **ADS held, liquid net worth (LNW), and which broker holds SKHY: NOT DISCLOSED.**
**Source of truth:** Zac, `reports/portfolio/2026-11-13-skhy-sizing.md` §7 (T0–T9). I implement those tickets as written. I do not re-size. Where I found an arithmetic or calendar problem, I flag it in §7 below and do not quietly change it.

---

## 0. Approval chain (verified by 死潘狗 before cutting)

| Item | Status | File |
|---|---|---|
| Committee scorecard | **NOT PRESENT. The committee has not convened.** On file are the CEO synthesis (verdict: "Hold at current size with the tripwires above. Do not add.") and the audit, which is **in progress** (checkpoint C1–C2 complete, C3–C8 pending) | `reports/committee/2026-11-12-skhy-ceo-synthesis.md` · `reports/committee/2026-11-13-skhy-audit.md` |
| Decision record | **PRESENT.** It is a retrospective record (CRO Condition 9) | `memory/decisions/2026-11-13-skhy-retrospective.md` |
| Sizing memo (Zac) | **PRESENT**, §7 ticket list | `reports/portfolio/2026-11-13-skhy-sizing.md` |
| CRO conditions attached | **YES.** John §8 has **ten** conditions. The brief says nine; Condition 10 is the `portfolio.yaml` escalation | `reports/risk/2026-11-12-skhy-cro-review.md` |
| Technical levels | **PRESENT.** 老詹 §9 | `reports/technical/2026-11-11-skhy-technical.md` |
| Messi cost analysis / Tim Cook structure notes | **NOT ON FILE** for SKHY. Limit rationales below rest on Zac and 老詹 only | — |

**Why I am cutting these tickets with no committee scorecard (an exception, escalated in §7):** every ticket here is a **sell** that **reduces** an exposure the Owner already holds. T1 and T3–T9 each carry out a binding CRO condition, and those bind with or without a committee vote. CRO §1 row 13 marks committee approval "n/a for the hold". **T2 is the exception.** It is Zac's recommendation and is not a CRO condition, so it is marked **OWNER'S CHOICE**. No buy ticket exists, and no buy ticket could be cut on this paperwork.

---

## 1. Global constraints (read before placing any ticket)

### 1.1 Zac §7, verbatim

> - **SELL tickets only.** No BUY ticket exists for SKHY at any price (CRO Condition 5).
> - **No ticket may be placed on margin, and no ticket may be placed in a margin account.** The Webull account seen on 13 Nov is an individual margin account already carrying **negative USD cash (−$12.06)**; it holds no SKHY, so no SKHY ticket goes to it. The SKHY account (presumed Futu — NOT CONFIRMED) must be confirmed cash/unmargined before the first ticket is cut (CRO Condition 3; `leverage: none`). Proceeds of every sale settle to cash; nothing is redeployed by this memo.
> - **Quantities are formulas** where marked, because ADS count and LNW are not disclosed. 死潘狗 fills the formula with the Owner's numbers; he does not pick a number.
> - **Order of operations if several fire together:** T0 and T6/T7 (sell-all) override everything; T4/T5/T8 (sell-half) override trims; take the largest single reduction once (CRO §8).
> - **Stop type:** T6 is a **close-basis** rule executed at the next open. **Do not** place a resting intraday stop at $120.35 (CRO §4, §11 item 4).

*(Note on the fourth bullet: in Zac's own table T4 is a ⅓ trim and the sell-half tickets are T5 and T8. I read "T4/T5/T8 (sell-half)" as "T5/T8 (sell-half)" and flag the slip in §7 item 6. The rule itself is unaffected: take the largest single reduction once.)*

### 1.2 Additional constraints in the CEO's dispatch, 13 Nov (these bind as well)

- **Sell-only.**
- **No ticket may be placed in a margin account or on margin.** Webull is a margin account with negative USD cash and holds no SKHY. **The SKHY broker must be confirmed as a cash account before T3 onward is placed. If it is margin, T1 becomes "switch account to cash or transfer position" before anything else.**
- **T6 (the $120.35 stop) is a close rule, executed market-on-open the next session. It is NOT a resting stop order.**
- **T0 is the denominator gate.** No cap-compliance ticket (T1) can be sized until the Owner discloses LNW or the SKHY account value. Under Zac's reading (a), where Webull's ~$690 is the whole LNW, T1 is "sell 100%".

*Where 1.1 and 1.2 differ:* Zac requires cash confirmation "before the first ticket is cut". The CEO's wording requires it "before T3 onward". **I apply the stricter of the two, Zac's: no SKHY ticket is placed until the account is confirmed cash.** The one exception is the CEO's own: if the account is margin, T1 becomes the account-switch or transfer instruction. The conflict this creates with Condition 1's "next session" deadline is escalated in §7 item 3.

### 1.3 Ticket-wide mechanics (my execution rules, applying the above)

- **Rounding (Zac §3, §8):** trims and halvings round **up**, written ⌈ ⌉. Cap-derived holdings round **down**, written ⌊ ⌋.
- **"Then-current" means ADS held at the moment the trigger fires**, after every earlier fill. Any fill on any ticket changes the quantities on every later ticket.
- **Resting sell quantity must never exceed ADS held.** In a margin account, a resting sell larger than the holding can fill as a **short sale**. In a cash account the broker should reject it. That is one more reason the account must be cash. **Before placing any sell-all ticket (T1 at 100%, T6, T7), first cancel every resting SKHY order (T3/T4).**
- **Price checks use regular-session prints.** I recommend regular-trading-hours only on resting limits, because extended-hours books are thinner. This is my execution judgement, not a level from Zac or 老詹.

---

## 2. Tickets, in Zac's order

Notation: **H** = ADS held at the moment the ticket is placed. **P** = SKHY price on the day. **LNW** = liquid net worth in USD.
Every "worked example" uses **100 ADS** and is **ILLUSTRATIVE ONLY. These are not the Owner's numbers.** Illustrative LNW figures ($100,000; $500,000) come from Zac §2.2 and §5.4. The $690 and $6,900 figures are Zac's readings (a) and (b) in §5.3.

---

### T0 — Denominator gate and account gate (no order)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T0** |
| Trigger | **Now.** Every other ticket waits on this one |
| Direction | — (information, not an order) |
| Quantity | — |
| Order type | — |
| Satisfies | CRO **Condition 1** (needs a denominator) · **Condition 3** (unmargined) · **Condition 10** (populate `config/portfolio.yaml`) |
| Source | Zac §5.3, §7 T0; CEO dispatch |

**The Owner must supply, in writing:**
1. **H**, the ADS count held.
2. **LNW**, or at minimum the value of the account that holds SKHY.
3. **The broker and account that hold SKHY** (Futu is presumed but NOT CONFIRMED).
4. **Whether that account is cash or margin.** The evidence is a broker statement showing account type and a margin/debit balance of 0.

**Gate outcomes:**
- **Account is margin:** T1 becomes **T1-M** (below) and is done first. No other SKHY sell is placed until T1-M is complete, subject to the conflict escalated in §7 item 3.
- **Account is cash:** go to T1.
- **LNW not disclosed:** T1 cannot be sized. Zac's reading (a) cannot be dismissed (Zac §5.3: "I do not assume the Futu account is large").

**Record after:** 腦大裝草 appends H, LNW, broker, account type and date to the decision record's *Updates* and *Execution → Owner fills* block. The Owner populates `config/portfolio.yaml` (Condition 10).

---

### T1 — Cap compliance (CRO Condition 1)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T1** |
| Trigger | H × P > 0.03 × LNW, i.e. position over **3.0% of LNW at market** (CRO §9; Zac §2.1) |
| Direction | **SELL** |
| Quantity | **H − ⌊0.03 × LNW ÷ P⌋**. At P = $131.07 this is **H − ⌊LNW ÷ 4,369⌋** (Zac §7). If the result is ≤ 0, T1 does not fire |
| Order type | **Market at the open**, or a **marketable DAY limit no more than 0.5% below last** (Zac §7). At $131.07 the limit is ≥ $130.42 (131.07 × 0.995 = 130.414, rounded **up** to stay inside 0.5%). Recompute from the live last price on the day |
| Time in force | DAY. **Next session after T0 resolves.** It is not tied to a price level. John: "the excess is regulatory premium, not a trade" |
| Satisfies | CRO **Condition 1** |

**All three denominator readings (Zac §5.3), shown with 100 ADS (ILLUSTRATIVE):**

| Reading | LNW | Cap ⌊0.03 × LNW ÷ 131.07⌋ | 100 ADS as % of LNW | **T1 sells** | Then |
|---|---|---|---|---|---|
| **(a) Webull is the whole LNW** | $690 | **0 ADS** ($20.70 < one ADS) | 1,900% (one ADS alone = 19.0%) | **100 ADS = sell 100%** | **Every other ticket is void.** Position closed |
| **(b) LNW is 10× Webull** | $6,900 | **1 ADS** | 190% | **99 ADS** | 1 ADS held (1.90%). The ladder collapses: sell that 1 ADS at the first of T2/T3/T5/T6/T7/T8/T9 to fire (Zac §5.3(b)) |
| **(c) general, per LNW** | e.g. $100,000 (illus.) | 22 ADS | 13.1% | **78 ADS** | 22 held → T2 onward |
| (c) | e.g. $500,000 (illus.) | 114 ADS | 2.62% | **0, T1 does not fire** | 100 held → T2 onward |

**T1-M (replaces T1 if T0 shows the SKHY account is margin):** the instruction is **"switch the account to cash (margin disabled), or transfer the SKHY position to a cash account"**, and it comes before any sale. This is not an order. It is an account action the Owner takes with his broker. After that, run T1 as above.

**Owner verifies before placing:** (i) T0 complete. (ii) Account confirmed cash. (iii) **H and LNW recomputed at the live price P on the day**, not $131.07. (iv) No resting SKHY orders are open. (v) If T1 is 100%, nothing else is placed afterwards.
**Record after fill:** fill date and time, ADS sold, fill price, order type (market or limit, and the limit), reference price for slippage (prior close and last at decision), ADS remaining, LNW used, and which reading (a)/(b)/(c) applied. Append to the decision record under *Updates*.

---

### T2 — Conviction reduction to ≤ 1.5% (OWNER'S CHOICE: Zac's recommendation, not a CRO condition)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T2** |
| Trigger | The Owner **accepts** Zac §6 (reach the 20 Jan level now rather than by 20 Jan) |
| Direction | **SELL** |
| Quantity | **H − ⌊0.015 × LNW ÷ P⌋**. At $131.07 this is **H − ⌊LNW ÷ 8,738⌋** (Zac §7). For a position sitting exactly at the cap, this is **50%** |
| Order type | **DAY limit at or near last** (Zac §7: "not urgent intraday"). Place at last traded price. If unfilled, re-place next session at the new last |
| Time in force | DAY. Re-cut daily |
| Validity | Next session after T1, through **20 Jan 2027**. On that date it merges into T9 |
| Satisfies | **None of John's conditions.** It satisfies Condition 7 early. Zac §6, §8: "a recommendation inside John's cap, not a condition" |

**Worked example (ILLUSTRATIVE), 100 ADS:**
- LNW $500,000: target ⌊7,500 ÷ 131.07⌋ = **57** → **sell 43**.
- LNW $100,000 after T1 (22 held): target ⌊1,500 ÷ 131.07⌋ = 11 → **sell 11**.
- Reading (b), 1 ADS held: target 0 → **sell 1**.
- Reading (a): already zero after T1.

**Owner verifies:** that he is choosing this. If he declines, 腦大裝草 logs "declined Zac's recommendation; compliant with John" (Zac §8). Also verify the account is cash, H and LNW at live P, and T1 is done.
**Record after fill:** as T1, plus "Owner elected T2 (date)". If declined, record the declination.

---

### T3 — Trim 1 into the $146.80–$149.90 band (CRO Condition 8)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T3** |
| Trigger | **Any daily print in $146.80–$149.90** (老詹 §9(b): 61.8% Oct–Nov retrace + $149 IPO price + 38.2% full range + 30 Oct failure point) |
| Direction | **SELL** |
| Quantity | **⌈⅓ × H⌉**, at least one-third of then-current (CRO §8 Condition 8) |
| Order type | **Resting LIMIT SELL at $146.80** (Zac §7). A limit at the band floor is how "any daily print" is implemented. A gap open above $146.80 fills at the better open price |
| Time in force | **GTC.** Regular-session only (recommended, §1.3) |
| Validity | Placed **after T0 and the cash-account check, and after T1/T2 resolve**. It rests until filled or cancelled. **Owner must confirm his broker's GTC expiry.** If GTC lapses before 20 Jan 2027, re-place it at expiry |
| Satisfies | CRO **Condition 8** (trim 1) |

**Worked example (ILLUSTRATIVE):** 100 ADS held, no earlier fills → ⌈33.3⌉ = **34 ADS** at ≥ $146.80 (proceeds ≥ $4,991.20) → 66 held. If T2 already took the position to 57 → ⌈19.0⌉ = **19** → 38 held.

**Execution note:** a print at $146.80 does **not** guarantee a fill, because of queue priority at the limit. **If the band printed and T3 did not fill, Condition 8 has still fired.** In the next session, sell ⌈⅓ × H⌉ with a marketable limit.
**Must be amended:** after **any** fill on T1, T2, T5, T8 or T9, re-size T3 to ⌈⅓ × new H⌉. **Cancel it** before placing T6, T7 or a 100% T1.
**Owner verifies:** cash account; quantity ≤ H; no other resting SKHY sell whose combined quantity with T3 exceeds H.
**Record after fill:** fill date, price and quantity; whether it filled at the limit or on a gap above it; H remaining; the session's high print (evidence the band traded). Append to the decision record.

---

### T4 — Trim 2 into the $158.50–$162.00 band (CRO Condition 8)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T4** |
| Trigger | **Any daily print in $158.50–$162.00** (老詹 §9(b): 50% of full range + 29 Oct last lower high) |
| Direction | **SELL** |
| Quantity | **⌈⅓ × H⌉**, where H is the holding **after T3 has filled** |
| Order type | **Resting LIMIT SELL at $158.50**, re-sized after T3 fills (Zac §7) |
| Time in force | **GTC.** Regular-session only (recommended) |
| Validity | **Place only after T3 fills** (Zac §7). Rests until filled, cancelled, or GTC expiry (re-place) |
| Satisfies | CRO **Condition 8** (trim 2) |

**Worked example (ILLUSTRATIVE):** after T3 on 100 → 66 held → ⌈22.0⌉ = **22 ADS** at ≥ $158.50 (≥ $3,487.00) → 44 held. *Zac's table shows 23 per 100. He computed ⅓ of a fractional 66.7. With whole ADS the holding is 66, and ⌈⅓ × 66⌉ = 22. Both satisfy "another third". Flagged in §7 item 5.*
**Same-session gap through both bands:** if one session prints from below $146.80 to ≥ $158.50, T3 fills and T4 is placed straight after (Zac: "place after T3 fills"). If price is still ≥ $158.50, T4 fills too. Whether John's "largest reduction once" rule should merge L1 and L2 here is escalated in §7 item 4.
**Must be amended / cancelled:** same rules as T3.
**Owner verifies / records:** same as T3.

---

### T5 — Wuxi licence tripwire (CRO Condition 6)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T5** |
| Trigger | **By 24 Dec 2026 (Thursday)**, no dated report of a 2027 US tool licence covering **Wuxi** filed in `reports/news/` (CRO §8 Condition 6; Zac §7) |
| Direction | **SELL** |
| Quantity | **⌈½ × H⌉** |
| Order type | **Market, or marketable limit, at the next open** (Zac §7) |
| Time in force | DAY, first session after the trigger date |
| Validity | **Monday 28 Dec 2026 open.** *Zac's §7 says "26 Dec open". 26 Dec 2026 is a Saturday. 25 Dec (Fri) is the Christmas market holiday and 26–27 Dec is a weekend, so the first session after 24 Dec is Mon 28 Dec.* **Owner to confirm against the exchange holiday calendar.** 24 Dec may also be an early-close session; confirm that too. Flagged in §7 item 2 |
| Satisfies | CRO **Condition 6** |

**Worked example (ILLUSTRATIVE):** 100 held, no trims → **sell 50** → 50. After T3 (66) → **33** → 33. After T3 + T4 (44) → **22** → 22.
**Cancel / amend:** if a Wuxi 2027 licence is reported (dated source in `reports/news/`) by 24 Dec, T5 is **void**. If T5 fills, re-size T3/T4 to ⌈⅓ × new H⌉.
**Owner verifies:** that 修大哥 or The dictator have checked `reports/news/` as of the 24 Dec close. Absence of a report must be a checked absence, not an unchecked one.
**Record after fill:** fill date, price and quantity; the news search result relied on (or "none found as of 24 Dec"); H remaining.

---

### T6 — Hard stop: close-basis, executed market-on-open (CRO Condition 2)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T6** |
| Trigger | **A regular-session daily CLOSE below $120.35** (老詹 §9(c), "will not be moved lower"). An intraday trade below $122.20 is an **early warning only**, not a trigger |
| Direction | **SELL** |
| Quantity | **100% of H** |
| Order type | **MARKET-ON-OPEN, next session.** If the broker offers no MOO order for US equities, use a market order placed before the open for the regular session. **Owner to confirm which his broker supports** |
| Time in force | The session after the qualifying close |
| Satisfies | CRO **Condition 2** ("Daily close < $120.35 → sell the full position at the next open. No resting intraday stop order. No averaging down through it, ever.") |

**Why this is NOT a resting stop order:**
1. **The level is a close level.** 老詹 set a *daily close* below $120.35 as the invalidation. A resting intraday stop fires on a *print*, not a close, so it carries out a different rule from the one the desk set.
2. **The stop sits inside one day's range.** The stop is **8.18% below $131.07** (Zac §4.1). The 13 Nov range alone was $129.18–$135.76 ($6.58, 5.0% of $131.07). John records 5–13% daily ranges and a −13.4% day on 5 Nov (CRO §4). A resting stop-market order at $120.35 would be swept by an intraday wick that recovers by the close: **a gap-fill invitation**.
3. **A resting stop does not protect against a gap either.** A stop-market order on a gap-down open fills at the gap price anyway. A stop-limit may not fill at all. CRO §4: "a resting stop costs the wick" while the close rule "costs the overnight gap. Pick the gap."
4. **The premium is unaffected.** A KSD announcement gaps the ADS toward parity with no path through $120.35 (CRO §3.4: "The stop at $120.35 does nothing here"). T7 covers that, not T6.

**Worked example (ILLUSTRATIVE):** 100 ADS. Fill at $120.35 → −$1,072 versus $131.07 (Zac §4.1). Fill on a −13.4% gap at $113.51 → −$1,756 (Zac §5.1).
**Before placing: cancel T3 and T4** so that no resting sell survives a zero position. T6 overrides T1, T2, T3, T4, T5, T8 and T9.
**Owner verifies:** the official close (not an after-hours print) is below $120.35; resting orders are cancelled; the account is cash.
**Record after fill:** the qualifying close and its date; the open print and the fill price (slippage measured against the close **and** against $120.35); quantity; H = 0. 老詹 logs the stop-out in his file (老詹 §9(c)). 腦大裝草 completes *Close-out* in the decision record (criterion 1 triggered).

---

### T7 — Quota announcement: sell all (CRO Condition 4, second limb)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T7** |
| Trigger | **Any KSD / FSC / depositary (Citi) announcement widening or lifting the ADS conversion quota** (CRO §8 Condition 4; 修大哥 runs the watch) |
| Direction | **SELL** |
| Quantity | **100% of H** |
| Order type | **Market at the next open** (Zac §7) |
| Time in force | The session after the announcement |
| Satisfies | CRO **Condition 4** (announcement limb) |

**Worked example (ILLUSTRATIVE):** 100 → **sell 100** → 0. Zac §5.1 puts parity (−35%) at ~$85.20, a loss of $4,587 per 100 ADS against $131.07. That is the gap this ticket cannot avoid. It can only avoid holding through a second leg.
**Before placing: cancel T3 and T4.** T7 overrides every other ticket.
**Timing question escalated (§7 item 7):** if an announcement lands **during** a US session, Zac and John both say "next open". I implement that as written. Whether to sell in the same session is John's call, not mine.
**Owner verifies:** the announcement is primary or dated (KSD/FSC/depositary notice, or Reuters/Yonhap with a date) and it widens or lifts the quota. A rumour does not qualify.
**Record after fill:** the announcement source and timestamp; the open and fill prices; quantity; H = 0; *Close-out* (criterion 2).

---

### T8 — Premium collapse: sell half (CRO Condition 4, first limb)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T8** |
| Trigger | **Friday check:** premium = SKHY close × USDKRW ÷ (000660 close ÷ 10) − 1 **< 25%**, **while 000660 is flat or up on the week** (CRO §8 Condition 4) |
| Direction | **SELL** |
| Quantity | **⌈½ × H⌉** |
| Order type | **Market at the next open** (Zac §7) |
| Time in force | **Monday open** after the qualifying Friday (or the next session if Monday is a holiday) |
| Satisfies | CRO **Condition 4** (premium limb) |

**Worked example (ILLUSTRATIVE):** 100 → **sell 50** → 50 (after T3: 66 → 33).
**Cancel / amend:** after a fill, re-size T3/T4 to ⌈⅓ × new H⌉.
**Owner verifies:** the dated weekly row in `reports/risk/skhy-premium-log.md` (or his own sheet): date, SKHY close, USDKRW, 000660 close, premium %. **The premium at $131.07 is NOT COMPUTABLE this session**, because the 13 Nov 000660 close and USD/KRW are not on disk (Zac §1.4). The first Friday row is therefore still owed.
**Record after fill:** the qualifying Friday row; open and fill prices; quantity; H remaining.

---

### T9 — Reduce-before window, by 20 Jan 2027 (CRO Condition 7)

| Field | Value |
|---|---|
| Ticket ID | **SKHY-2026-11-13-T9** |
| Trigger | **Calendar.** Position must be ≤ **1.5% of LNW at market** by the **20 Jan 2027 close** (Wednesday), **or ≤ 3.0%** if 老詹 has logged a daily close > **$152.35** (CRO Condition 7; Zac §7) |
| Direction | **SELL** |
| Quantity | **H − ⌊0.015 × LNW ÷ P⌋**, using **0.03** in place of 0.015 if the >$152.35 close is logged. **Formula ticket: P is the price on the day, not $131.07.** If ≤ 0, T9 does not fire |
| Order type | **DAY limit near last**, or **market-on-close** (Zac §7). My recommendation (execution judgement): begin with DAY limits at last in the sessions before 20 Jan, and use market-on-close on 20 Jan only if still unfilled |
| Validity | Any session up to and including **Wed 20 Jan 2027**. **If the 4Q26 results date (NOT OBTAINED) falls before 20 Jan, T9 must be complete before the results** (CRO §6) |
| Satisfies | CRO **Condition 7** |

**Worked example (ILLUSTRATIVE), LNW $500,000, 100 ADS, no earlier fills:**
- At P = $131.07, no >$152.35 close logged: target ⌊7,500 ÷ 131.07⌋ = 57 → **sell 43**.
- At P = $158.50 reached on an intraday print, with no daily *close* above $152.35 logged: target ⌊7,500 ÷ 158.50⌋ = ⌊47.3⌋ = 47 → **sell 53**. The price is higher, so the dollar target buys fewer ADS. (In practice T3 would already have fired on the way up.)
- With the >$152.35 close logged, at P = $131.07: target ⌊15,000 ÷ 131.07⌋ = 114 → sell 0.

**Mark-to-market drift:** a position at 1.33% after both trims becomes 1.61% at $158.50 (Zac §3). That is why T9 is computed on the day.
**Owner verifies:** H, LNW and P on the day; whether 老詹's >$152.35 close note exists and is dated; the 4Q26 date if it has become known.
**Record after fill:** the target % used and why (1.5 or 3.0); LNW and P used; fill and quantity; resulting %.

---

## 3. Execution-cost note

**One line:** SKHY traded **12.7M ADS today at ~$131** (coordinator, 13 Nov; the read was taken at 19:50 UTC, before the close, so the full-day figure is likely higher). **A 100-ADS limit order (~$13,107) is about 0.0008% of that volume and is not a liquidity event.** It becomes one at the firm's `max_adv_participation` limit of **5%**, about **635,000 ADS ≈ $83M** on today's volume. Long before that, a market or MOO order **large relative to the displayed opening book** could move the open print. That threshold is NOT KNOWN, because no depth data exists and Tim Cook has not run. On T6, T7 and T8 the real cost is the **overnight gap**, not the spread.

---

## 4. Sequence diagram (text)

```
GATE ───────────────────────────────────────────────────────────────────────────────
 T0  Owner discloses H, LNW, SKHY broker, cash/margin
      ├─ margin  → T1-M (switch to cash / transfer) ─┐
      └─ cash    ────────────────────────────────────┴─► continue
                                       (no SKHY ticket in Webull, ever)

ONE-OFF, NEXT SESSION ──────────────────────────────────────────────────────────────
 T1  cap compliance  (fires only if H×P > 3% LNW)
      └─ reading (a) / any 100% result → POSITION CLOSED → nothing below is placed
 T2  conviction reduction to ≤1.5%  (OWNER'S CHOICE; after T1)

RESTING (at most ONE resting SKHY order at any time) ───────────────────────────────
 T3  LIMIT SELL ⌈⅓H⌉ @146.80 GTC  ── placed after T0/T1/T2 resolve
      └─ on fill → place T4
 T4  LIMIT SELL ⌈⅓H⌉ @158.50 GTC  ── placed only after T3 fills

CONDITIONAL WATCHES (not resting; Owner checks, then places at next open) ─────────
 T6  daily close < 120.35            → MOO sell 100%         [checked every close]
 T7  KSD/FSC/depositary quota news   → market sell 100%      [修大哥 watch]
 T8  Friday premium < 25%, 000660≥   → market sell ⌈½H⌉      [every Friday]
 T5  no Wuxi licence by 24 Dec 2026  → market sell ⌈½H⌉      [Mon 28 Dec open]
 T9  by 20 Jan 2027 close            → sell to ≤1.5% (3.0%)  [formula, on the day]

WHAT CANCELS / AMENDS WHAT ────────────────────────────────────────────────────────
 T1 at 100%  → cancels T2–T9 (all void)
 T6 fill     → cancel T3, T4 FIRST; voids T5, T7, T8, T9           (sell-all)
 T7 fill     → cancel T3, T4 FIRST; voids T5, T6, T8, T9           (sell-all)
 T5 / T8 fill→ re-size resting T3 (or T4) to ⌈⅓ × new H⌉
 T1/T2/T9 fill (partial) → re-size resting T3 (or T4) to ⌈⅓ × new H⌉
 T3 fill     → place T4 sized ⌈⅓ × new H⌉
 T4 fill     → ladder complete; T5/T6/T7/T8/T9 still live on residual
 Wuxi licence reported by 24 Dec → T5 void
 老詹 logs close > 152.35         → T9 target changes 1.5% → 3.0%

SAME-SESSION COLLISIONS (CRO §8) ──────────────────────────────────────────────────
 Several fire together → take the LARGEST single reduction ONCE:
   sell-all (T6, T7, T1@100%)  >  sell-half (T5, T8)  >  trims (T3, T4)
   Do not stack T3 on top of a T5/T8 halving in the same session.
```

---

## 5. Do-not list

1. **No BUY**, on any ticket, at any price (CRO Condition 5; Zac §6: "A buy ticket does not exist").
2. **No add.** That includes the $127.3–$130.0 zone, which the 13 Nov low of $129.18 touched. It is **vetoed** (CRO §0 B/C).
3. **No averaging down**, ever, and especially not below $120.35 (CRO Condition 2; 老詹 §9(a)).
4. **No resting stop order** at $120.35 or anywhere else. Not stop-market, not stop-limit, not trailing (§2 T6; CRO §4, §11 item 4).
5. **No margin.** No ticket placed on margin or in a margin account. No sell larger than H (a short sale in a margin account).
6. **No ticket in Webull.** It holds no SKHY, it is a margin account, and its USD cash is −$12.06.
7. **No redeployment of proceeds** by this file. Proceeds settle to cash (Zac §7).
8. **No agent places, modifies or cancels anything.** The Owner does every step by hand (CLAUDE.md rule 1).
9. **No ticket sized off $131.07 on the day.** Every formula uses H, LNW and P **as of the session it is placed**.

---

## 6. After fills: what 腦大裝草 records in `memory/decisions/2026-11-13-skhy-retrospective.md`

The record is append-only. Every fill goes under **Updates** as a dated line, and the cumulative state goes under **Execution**:

| Field | Why |
|---|---|
| Ticket ID (T1…T9), date, time (ET) | ties the fill to the condition that caused it |
| Trigger evidence: the close (T6), the band high print (T3/T4), the news source (T5/T7), the Friday premium row (T8), LNW/P/target % (T1/T2/T9) | proves the condition fired; post-mortem grades it |
| Order type actually used (MOO / market / limit at $X / GTC) | Messi: order-type effect |
| Quantity sold, average fill price | P&L; Messi: slippage |
| **Reference price for slippage:** limit price (T3/T4); prior close **and** the open print (T5–T8); last at decision (T1/T2/T9) | Messi's measurement baseline |
| Broker, account, account type (cash) | Condition 3 evidence |
| H remaining; % of LNW remaining | next ticket's input; Condition 1/7 tracking |
| Resting orders amended or cancelled as a result | audit trail for §4 |
| On H = 0: complete **Close-out** (exit date/price, P&L vs $129.00, which pre-registered criterion fired) | attribution |

The Owner reports fills to the CEO. I write the dated fill line for 腦大裝草 to append.

---

## 7. Escalations to the CEO

1. **Approval chain incomplete.** No committee scorecard exists (committee not convened) and the audit is pending (C3–C8). I cut sell-only tickets because each carries out a binding CRO condition on an existing holding. **T2 has no CRO basis and no committee basis.** It is the Owner's choice on Zac's recommendation. If the CEO prefers I withhold T2 until the committee meets, it comes out.
2. **Zac's T5 date is a Saturday.** "26 Dec open" → corrected to **Mon 28 Dec 2026** (25 Dec holiday, 26–27 Dec weekend). Calendar arithmetic only. The Owner should confirm the holiday calendar.
3. **Margin-account conflict with Condition 1.** If T0 shows SKHY in a **margin** account **and** the position is over cap, two binding rules collide. Condition 1 says sell the excess *next session*. The global constraint says no ticket in a margin account, so T1 becomes switch or transfer first. Switching or transferring may take longer than one session. A sell of a fully-paid long adds no leverage, but the rule as written forbids it. **This is the Owner's decision, not mine.** I have not waived the constraint.
4. **Same-session gap through both trim bands.** It is unclear whether T3 and T4 both execute, or whether "largest reduction once" applies. Following Zac literally, both execute (T4 is placed after T3 fills). John should rule.
5. **T4 per-100 quantity.** Zac shows 23. Whole-ADS arithmetic (⌈⅓ × 66⌉) gives 22. The formula governs. Either satisfies "another third".
6. **Zac §7 order-of-operations bullet** calls T4 "sell-half". T4 is a ⅓ trim. The sell-half tickets are T5 and T8. My guess is a typo. The rule is unaffected.
7. **T7 intraday timing.** If a quota announcement lands during a US session, both Zac and John say "next open". John may want same-session discretion. Not my call.
8. **Webull (outside SKHY scope, recorded so it is not lost):** margin account, USD −$12.06, 2 AVGO with **no decision record**. The 10 Aug 3416 advice to switch to cash was not acted on (snapshot header).
9. **Messi and Tim Cook have not run on SKHY.** The limit placements rest on Zac and 老詹 levels only. No cost or depth analysis supports them.

---

## 8. NOT OBTAINED register

| Item | Status |
|---|---|
| **Position size (H, ADS held)** | **NOT DISCLOSED.** Every quantity is a formula; 100-ADS examples are illustrative |
| **Liquid net worth (LNW)** | **NOT DISCLOSED.** Visible floor ~US$690 (Webull, coordinator's HKD/USD ~7.82 conversion). Readings (a)/(b)/(c) all open |
| **Broker holding SKHY** | **NOT CONFIRMED.** Not Webull; Futu presumed |
| **Margin status of the SKHY account** | **NOT OBTAINED.** Condition 3 unverified. Webull (the only account seen) is margin with USD −$12.06 |
| SKHY account value (Futu / Longbridge) | NOT OBTAINED |
| **13 Nov close** | NOT OBTAINED. $131.07 is a 19:50 UTC print; the T6 rule needs closes |
| 13 Nov full-session volume | NOT OBTAINED. 12.7M is the coordinator's figure as of the 19:50 UTC read |
| Nov ADV; order-book depth at the open | NOT OBTAINED (Tim Cook not run) |
| 000660 13 Nov close; USD/KRW | NOT OBTAINED. Premium at $131.07 NOT COMPUTABLE; first T8 Friday row owed |
| Whether the Owner already has a stop order resting, and of what type | NOT OBTAINED (CRO §12 Q2). **If a resting stop exists, the Owner should cancel it in favour of T6** |
| Broker's GTC expiry; MOO availability for US equities | NOT OBTAINED. Owner to confirm |
| Exchange holiday / early-close calendar for 24–28 Dec 2026 | Not on disk; Owner to confirm |
| 4Q26 results date | NOT OBTAINED. T9 must be done before it if it falls ≤ 20 Jan |
| FOMC / other macro event dates in the window | NOT ON DISK, not checked. No ticket here is timed to a discretionary entry; T2/T9 timing is the only place it could matter |
| KSD quota status since 23 Jul; Wuxi 2027 licence status | NOT OBTAINED (CRO §13) |
| Committee scorecard | NOT OBTAINED. Committee not convened |
| Messi cost analysis; Tim Cook structure notes | NOT ON FILE |

**Searches used: 0.** All figures trace to Zac (§1–§8), John (§3, §4, §6, §8, §9), 老詹 (§4, §9), the Webull snapshot `config/portfolio-webull-snapshot-2026-11-13.yaml`, the CEO's 13 Nov dispatch, or arithmetic shown inline. Illustrative quantities are labelled.

---
*Research and decision support, not financial advice. Markets cannot be reliably predicted. These are tickets for the Owner's review. No trade occurs until the Owner places it, and no agent of this firm places, modifies or cancels orders.*
