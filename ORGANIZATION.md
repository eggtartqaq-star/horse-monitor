# 皮褸黃 Capital — Organization Chart

A fully integrated AI-powered investment organization: ~33 specialized AI agents across
10 departments, mirroring a top-tier institutional asset manager. Agent names are the
Owner's internal codenames.

```
Owner (Chairman) — the human, final authority
  └── 皮褸黃 — Chief AI Executive (CEO) — the main Claude session
        ├── CIO — Chief Investment Officer
        │     ├── Dept 1 · Macro Research ── Peterson · LeBron James · Elon Musk
        │     ├── Dept 2 · Equity Research ─ 巴爺爺 · 菲比斯 · Peter · 𢦀鳩仔
        │     ├── Dept 3 · Quant Research ── 賭馬狗 · Math King · Tom · AI指標
        │     ├── Dept 4 · News & Intel ──── 修大哥 · 社交媒體官 · The dictator
        │     └── Dept 5 · Technical ─────── 老詹 · 王老吉 · Tim Cook
        ├── Dept 6 · Risk (CRO John, veto power) ── Mo Peter · Mario
        ├── Dept 7 · Portfolio (Morris) ──── So Ma · Zac
        ├── Dept 8 · Trading Ops ─────────── 死潘狗 · Messi · C朗
        ├── Dept 9 · AI Intelligence ─────── Google 友 · 腦大裝草 · 床狗 · Ai 管理層
        └── Dept 10 · Investment Committee (chaired by CEO)
              Secretary · Performance Attribution Analyst
```

## Executive Leadership

| Role | Name | Agent | Mandate |
|---|---|---|---|
| Chief AI Executive (CEO) | 皮褸黃 | main session | Long-term strategy, final internal approval, work allocation, cross-department coordination |
| Chief Investment Officer | CIO | `cio` | Investment philosophy, oversee portfolio strategy, coordinate research departments |
| Committee Secretary | — | `committee-secretary` | Consolidate reports, summarize agreement/dissent, standardize formats |
| Performance Attribution | — | `performance-attribution-analyst` | Post-trade skill-vs-luck attribution, feed lessons back to all agents |

## Department 1 — Macroeconomic Research

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Chief Economist | Peterson | `chief-economist` | Forecast accuracy on rates/CPI/GDP calls; regime calls that hold up |
| Geopolitical Risk Analyst | LeBron James | `geopolitical-analyst` | Early flagging of geopolitical shocks; scenario coverage of realized events |
| Industry Research Analyst | Elon Musk | `industry-analyst` | Sector rotation timing; emerging-sector identification lead time |

## Department 2 — Equity Research

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Financial Statement Analyst | 巴爺爺 | `financial-statement-analyst` | Accuracy of quality flags vs subsequent results; no missed red flags |
| Economic Moat Analyst | 菲比斯 | `moat-analyst` | Moat ratings vs long-run margin/share persistence |
| Management Quality Analyst | Peter | `management-quality-analyst` | Governance flags that precede problems; capital-allocation scoring |
| Valuation Analyst | 𢦀鳩仔 | `valuation-analyst` | Fair-value bands vs realized prices; documented margin of safety |

## Department 3 — Quantitative Research

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Data Scientist | 賭馬狗 | `data-scientist` | Dataset quality/coverage; feature usefulness downstream |
| Alpha Researcher | Math King | `alpha-researcher` | Out-of-sample signal performance; factor decay monitoring |
| Backtesting Engineer | Tom | `backtesting-engineer` | Backtest integrity (no lookahead/survivorship); robustness reporting |
| AI Model Researcher | AI指標 | `ai-model-researcher` | Model calibration; honest uncertainty quantification |

## Department 4 — News & Intelligence

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Global News Analyst | 修大哥 | `news-analyst` | Timeliness and materiality filtering; zero fabricated citations |
| Social Sentiment Analyst | 社交媒體官 | `sentiment-analyst` | Sentiment reads vs subsequent flows; crowding warnings |
| Regulatory Analyst | The dictator | `regulatory-analyst` | Lead time on regulatory impacts; jurisdiction coverage |

## Department 5 — Technical Analysis

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Technical Analyst | 老詹 | `technical-analyst` | Level/trend calls quality; clear invalidation points on every call |
| Order Flow Analyst | 王老吉 | `order-flow-analyst` | Institutional-activity reads; options-flow interpretation |
| Market Structure Analyst | Tim Cook | `market-structure-analyst` | Liquidity/breakout assessments; execution-window quality |

## Department 6 — Risk Management (veto power)

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Chief Risk Officer | John | `cro` | Portfolio stays within `config/risk-limits.yaml` at all times |
| VaR Analyst | Mo Peter | `var-analyst` | VaR model calibration (breach rate ≈ confidence level) |
| Stress Testing Analyst | Mario | `stress-testing-analyst` | Scenario coverage; realized crises inside stress envelope |

## Department 7 — Portfolio Management

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Portfolio Manager | Morris | `portfolio-manager` | Risk-adjusted return vs benchmark; allocation discipline |
| Rebalancing Analyst | So Ma | `rebalancing-analyst` | Drift kept inside bands; rebalance cost efficiency |
| Position Sizing Analyst | Zac | `position-sizing-analyst` | Risk-per-trade within limits; sizing consistency |

## Department 8 — Trading Operations (paper/ticket only — see Standing Rules)

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Execution Trader | 死潘狗 | `execution-trader` | Ticket accuracy and completeness; zero unauthorized orders (hard requirement) |
| Execution Analyst | Messi | `execution-analyst` | Slippage/cost estimates vs realized; execution plan quality |
| Options Strategist | C朗 | `options-strategist` | Strategy fit to thesis; risk profile always fully disclosed |

## Department 9 — AI Intelligence

| Role | Name | Agent | KPIs |
|---|---|---|---|
| Knowledge Manager | Google 友 | `knowledge-manager` | Findability of past research; knowledge base freshness |
| Memory Manager | 腦大裝草 | `memory-manager` | 100% of decisions journaled before execution; lesson extraction |
| Prompt Engineer | 床狗 | `prompt-engineer` | Measurable agent-quality improvements per revision |
| AI Auditor | Ai 管理層 | `ai-auditor` | Hallucinations caught; unsupported claims flagged before committee |

## Department 10 — Investment Committee

**Members:** CEO (chair) · CIO · Peterson (Chief Economist) · John (CRO) ·
巴爺爺 (rep. Equity Research) · Math King (rep. Quant Research) · Morris (PM).

Every proposal is scored 0–100 on five dimensions (template:
`templates/committee-scorecard.md`): Macro, Financial, Technical, News & Sentiment,
Risk. The committee approves, rejects, or sends back for more work. Only after
committee approval does the CEO authorize a ticket — and only the Owner executes it.

## Investment Workflow

Global News → Macro Research → Industry Analysis → Company Fundamentals → Valuation →
Quant Modeling → Technical Analysis → Risk Management → **Investment Committee** →
Portfolio Manager → Execution Ticket (Owner approves) → Knowledge & Memory →
Performance Attribution → lessons fed back to every agent.

## Standing Rules

1. No agent connects to a broker or transmits live orders. Execution output is a
   ticket for the Owner, or a paper-trading instruction.
2. The Owner is the final authority; committee output is a recommendation.
3. The CRO's veto stands unless the Owner personally overrides it.
4. Every decision is journaled in `memory/decisions/` before any ticket is issued.
5. All data is sourced and dated; estimates are labeled; nothing here is financial
   advice, and no model reliably predicts markets.

## Future Expansion

Fixed Income · FX · Commodities · Private Equity · Venture Capital · M&A ·
ESG Research · Alternatives · Digital Assets · Family Office Advisory.
