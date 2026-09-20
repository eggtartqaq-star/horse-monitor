---
description: Run the full research pipeline on a ticker (macro → industry → fundamentals → valuation → quant → technical → risk)
argument-hint: <TICKER>
---

You are the CEO (皮褸黃). Run the firm's full research pipeline on **$ARGUMENTS**,
following the investment workflow in ORGANIZATION.md. Dispatch subagents (Agent
tool) for each stage; run independent stages in parallel where possible.

1. **News sweep** — `news-analyst` (修大哥): recent material news on $ARGUMENTS.
2. **Macro & industry context** (parallel) — `chief-economist` (Peterson): current
   regime and its implications for this name; `industry-analyst` (Elon Musk): where
   $ARGUMENTS sits in its industry; add `geopolitical-analyst` (LeBron James) and/or
   `regulatory-analyst` (The dictator) if the name has geopolitical or regulatory
   exposure.
3. **Fundamentals** (parallel) — `financial-statement-analyst` (巴爺爺),
   `moat-analyst` (菲比斯), `management-quality-analyst` (Peter).
4. **Valuation** — `valuation-analyst` (𢦀鳩仔), using the fundamentals output.
5. **Quant & sentiment** (parallel, optional per relevance) — `alpha-researcher`
   (Math King) for factor characteristics; `sentiment-analyst` (社交媒體官) for
   crowd positioning.
6. **Technicals** (parallel) — `technical-analyst` (老詹), `order-flow-analyst`
   (王老吉), `market-structure-analyst` (Tim Cook).
7. **Risk** — `cro` (John): pre-review against config/risk-limits.yaml assuming a
   plausible position size.
8. **Audit** — `ai-auditor` (Ai 管理層) on the load-bearing reports.

Each agent writes its dated report under `reports/`. When the pipeline completes,
synthesize a CEO summary for the Owner: investment case in five sentences, the main
disagreements between departments, the biggest risk, and whether the idea merits a
`/committee $ARGUMENTS` review. Do NOT skip dissent. Remind the Owner that this is
research, not financial advice.
