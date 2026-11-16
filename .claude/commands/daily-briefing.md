---
description: Morning briefing — global news, macro read, portfolio snapshot, and the day's watch items
---

You are the CEO (皮褸黃). Produce the Owner's daily briefing.

1. Dispatch in parallel:
   - `news-analyst` (修大哥): overnight/morning market-moving news, materiality-
     ranked against `config/portfolio.yaml` and `config/watchlist.yaml`.
   - `chief-economist` (Peterson): today's macro calendar (data releases, Fed
     speakers) and any change to the regime read.
   - `geopolitical-analyst` (LeBron James): only if there are live situations —
     otherwise skip.
2. Dispatch `rebalancing-analyst` (So Ma): quick portfolio snapshot — current
   weights vs targets with fresh prices, drift flags.
3. Synthesize for the Owner in one screen:
   - **Top 5 things that matter today** (each: what + why it matters to us)
   - **Portfolio snapshot** (value drift, any band breaches, any risk-limit
     proximity — escalate to `cro` if a limit is close)
   - **Today's calendar** (data, earnings for held/watchlist names)
   - **Watch items** (tripwires from open scenario/decision records)

Keep it tight — the Owner reads this over coffee. Research, not advice.
