Added the 2% take profit to `strategy/v6.4/oos_validation.py`. It's wired into both engines.

## What changed

**1. New parameter** (next to the other engine-1 constants):

```python
# ---- 新增:固定2%獲利了結(兩個引擎共用) ----
TAKE_PROFIT_PCT = 2.0          # % —— 設 None 即關閉此出場條件
```

Set it to `None` to turn the exit off and get the old behaviour back, so you can run the before/after comparison without keeping two copies of the file.

**2. Engine 1 (`simulate_mr`)** — take profit is checked each day inside the 10-day hold window:

```python
tp = entry * (1 + TAKE_PROFIT_PCT / 100) if TAKE_PROFIT_PCT else None
...
if r["Low"] <= stop:
    return (stop - entry) / entry * 100, d
if tp is not None and r["High"] >= tp:
    if pd.notna(r["Open"]) and r["Open"] > tp:
        exit_price = r["Open"]
    else:
        exit_price = tp
    return (exit_price - entry) / entry * 100, d
```

**3. Engine 2 (`run_engine2`)** — same check, inserted after the trailing-stop check and before the trail gets updated, so a bar that hits +2% exits that day rather than ratcheting the stop first.

## Two implementation choices worth knowing about

**Exit precedence inside one bar.** Daily bars don't tell you whether the high or the low came first. I kept the existing convention and check the stop before the take profit, so a bar that touches both is booked as a loss. That's the conservative read; flipping it would make the results look better without any evidence they should.

**Gap handling.** If a bar opens above the +2% level, the fill uses the open, not the 2% level — you'd get the gap, not a magic fill at exactly +2%. This matches the gap protection already in engine 2's trailing stop.

## One thing to expect when you re-run it

A 2% cap changes what these two engines are, not just their numbers:

- Engine 1 only takes entries where the target is at least 2R away (`MIN_R = 2.0`), and its stop is 2×ATR — typically well over 2% wide. So the +2% take profit will fire before the real target on nearly every winner. You're effectively converting a 2R system into a sub-1R one: same losers, much smaller winners. Win rate goes up, EV per trade quite likely goes down.
- Engine 2 is a trend follower with a 60-day hold and a 3×ATR trail. Its entire edge is the small number of trades that run a long way. A 2% cap removes those by construction.

None of that is a reason not to run it — it's your test. But if EV drops, that's the take profit doing what it does, not a data problem. Worth running once with `TAKE_PROFIT_PCT = None` and once with `2.0` so you're comparing against the same trade set.

## Separate problem: the file won't run as-is

Unrelated to this change — the file in the repo is truncated at 80 columns. Every line longer than that has had its tail cut off, so Python can't parse it:

```
$ python3 -c "import ast; ast.parse(open('strategy/v6.4/oos_validation.py').read())"
SyntaxError: unterminated string literal (detected at line 304)
```

Affected lines I found (all cut at exactly 81 characters, plus one string cut mid-literal):

| Line | What's cut |
|---|---|
| 64 | `ta.trend.ADXIndicator(..., window=14` — missing `)` and the rest |
| 68 | `ta.volatility.AverageTrueRange(..., wind` |
| 74 | `df["vol_ratio"] = ... .rolling(20).m` |
| 75 | `ta.volume.OnBalanceVolumeIndicator(...).on_balanc` |
| 77 | `df["OBV_Div"] = ... (df["OBV"] > df["OBV"]` |
| 206, 208 | `targets.append((...` — the R multiple expression is cut |
| 259 | `trail = max(trail, highest - ATR_TRAIL_MULT * current_atr` |
| 304, 307, 311 | `print("  ` — unterminated string, this is the one that errors first |
| 368 | `.to_csv(..., encoding="utf-8` |

This looks like a copy-paste or transfer artifact rather than something you wrote — the logic around the cuts is coherent. I didn't reconstruct those lines, because several of them (74, 206, 208) have more than one plausible ending and guessing would silently change what the backtest measures.

If you have the original intact copy, restore it and re-apply the take-profit change (the diff is small and self-contained). If not, send me the missing tails for those lines, or tell me to reconstruct them and I'll flag every line where I had to infer rather than read.
