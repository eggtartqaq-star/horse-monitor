# 皮褸黃 Capital — AI Investment Firm

A fully integrated AI-powered investment organization built on Claude Code:
~33 specialized AI agents across 10 departments — macro research, equity research,
quantitative research, news & intelligence, technical analysis, risk management,
portfolio management, trading operations, AI governance, and an Investment
Committee — coordinated by a Chief AI Executive (皮褸黃, the main Claude session)
and answering to the human Owner.

## Quick start

Open this repository in Claude Code. The main session automatically becomes the CEO
(see `CLAUDE.md`). Then:

```
/daily-briefing            # morning macro + news + portfolio snapshot
/analyze NVDA              # full research pipeline on a ticker
/committee NVDA            # convene the Investment Committee for a scored verdict
/portfolio-review          # drift vs targets, rebalancing proposals
/post-mortem 2026-07-17-nvda-long   # attribute a closed decision, extract lessons
```

Individual specialists can be dispatched directly, e.g. *"ask Peterson for a Fed
outlook"* or *"have 𢦀鳩仔 build a DCF for AAPL"* — the CEO routes to the right agent
in `.claude/agents/`.

## Layout

| Path | Purpose |
|---|---|
| `CLAUDE.md` | CEO operating manual (loaded automatically) |
| `ORGANIZATION.md` | Full org chart: every agent, mandate, KPIs, reporting lines |
| `.claude/agents/` | The ~33 agent definitions |
| `.claude/commands/` | Firm workflows (`/analyze`, `/committee`, …) |
| `config/` | Portfolio, risk limits, watchlist |
| `reports/` | Department outputs, dated |
| `memory/decisions/` | Decision journal — institutional memory |
| `knowledge/` | Investment philosophy and accumulated research |
| `templates/` | Committee scorecard, research report, decision record |

## Ground rules

- **Research and decision support only — not financial advice.** No agent predicts
  markets reliably; all output is analysis with stated uncertainty.
- **No live trading.** The Execution Trader produces order tickets for the Owner to
  review and place manually (or in a paper-trading account). No broker APIs.
- **The Owner is the final authority.** Committee approval is a recommendation only.
- **Risk has veto power.** Proposals breaching `config/risk-limits.yaml` stop at the CRO.
- **Everything is journaled.** Decisions, rationale, dissent, and outcomes live in
  `memory/decisions/` and feed continuous improvement.
