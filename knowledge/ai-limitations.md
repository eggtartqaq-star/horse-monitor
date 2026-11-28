# What this firm's AI cannot do: read before relying on any output

*Owner-approved, 2026-11-28. The Owner asked: "What do you think about your current limitations?", then "Write them into the firm" after seeing this draft.*

1. **It cannot predict markets.** It can test whether a rule had an edge in the past. V6.6's tests found none after costs (2022–26; `reports/quant/2026-11-27-v66-robustness.md`).
2. **The agents are not independent.** All 35 are the same model with different instructions. Agent reviews catch many errors, but they share blind spots. Independent checks are the Owner, broker documents and real forward data.
3. **It makes mistakes.** Recent examples:
   - a wrong yearly figure;
   - an overstated cost;
   - a suggestion that broke a CRO rule.

   Every figure needs a source, and the reviewer's corrections are published.
4. **Its reach is limited.**
   - **By design:** read-only broker access, and no editable sources (CLAUDE.md rules 1 and 5).
   - **By environment:** some websites are blocked, and it cannot run anything on the Owner's PC or in TradingView.
   - **Facts only the Owner can supply:** the real fee, total net worth, and broker features (GTC stops, OCO).
5. **Its memory is fragile.** Only what is written in this repository survives sessions, restarts and usage limits. Anything decided must be logged (`memory/decisions/`).
6. **Keep the process proportionate.** Effort should match the money at stake. Owner documents stay short (`templates/owner-brief.md`).
7. **It is not a financial adviser.** It does not know the Owner's full finances, taxes or risk tolerance. It gives options and evidence; the Owner decides.

**Every agent:**
- state the relevant limit when it affects an answer;
- never present a backtest as a forecast;
- never present an agent review as an independent check.
