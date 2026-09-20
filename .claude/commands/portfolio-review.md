---
description: Full portfolio review — allocation vs targets, drift, risk posture, and rebalancing proposals
---

You are the CEO (皮褸黃). Run a full portfolio review.

1. Dispatch in parallel:
   - `rebalancing-analyst` (So Ma): full drift table vs `config/portfolio.yaml`
     targets with fresh prices; rebalance proposal if any band is breached.
   - `var-analyst` (Mo Peter): current portfolio VaR/ES and component risk.
   - `stress-testing-analyst` (Mario): stress results if the book changed
     materially since the last run (check `reports/risk/`); otherwise cite the
     latest.
2. Dispatch `cro` (John): limit-by-limit compliance check with the outputs above.
3. Dispatch `portfolio-manager` (Morris): allocation assessment — are the targets
   still right given Peterson's latest regime read and the firm's philosophy?
   Proposed changes (if any) as a written proposal, alternatives considered.
4. Synthesize for the Owner:
   - **Health check**: in/out of limits, drift status, risk posture in one
     paragraph.
   - **Proposals** (if any): rebalance trades and/or target changes, with costs
     and rationale — clearly marked as recommendations requiring Owner approval.
   - **Open decisions**: status of open positions vs their pre-registered exit
     criteria in `memory/decisions/` — flag any where exit criteria have triggered.

Config files are only updated after the Owner approves. Recommendations, not
advice; the Owner executes.
