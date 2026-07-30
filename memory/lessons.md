# Lessons Learned — 皮褸黃 Capital

Maintained by 腦大裝草 (Memory Manager), fed by Performance Attribution. Each lesson
cites the decision records that support it. 床狗 turns recurring lessons into
prompt improvements.

- **L-001 (2026-07-28)** — *No analyst cross-checks another analyst's headline figure.* Bloom Energy's financial report showed a $6M profit when the filed figure was an $87M loss; the correct number sat in another report **in the same package on the same day** and four analysts crossed it. Evidence: `reports/committee/2026-07-19-be-audit.md`. Action: cross-check rule routed to 床狗.
- **L-002 (2026-07-28)** — *Bad market-data vendors must be blacklisted firm-wide, not per-report.* A single vendor print produced a fictitious "dip-buying" event in the MU structure report that never happened. Evidence: `reports/committee/2026-07-18-mu-audit.md`. Action: vendor marked price-data-unusable in every subsequent brief.
- **L-003 (2026-07-28)** — *Consecutive same-direction verdicts breed narrative lock-in.* On KLAC, three independent modelling choices all erred bearish after three prior bear verdicts. Evidence: `reports/committee/2026-07-19-klac-audit.md`. Action: anti-anchoring disclosure is now mandatory in every valuation.
- **L-004 (2026-07-28)** — *A blended score hides the difference between a bad business and a good business at a bad price.* Evidence: `reports/committee/2026-07-28-intc-audit.md`. Action: scorecard rebuilt onto two axes.
- **L-005 (2026-07-28)** — *A CEO commit message is not evidence a file exists.* The MRVL moat report failed to write and was recorded as filed; two downstream reports leaned on it. Evidence: `reports/committee/2026-07-19-mrvl-audit.md`. Action: verify on disk before recording.

## Format

- **L-001 (YYYY-MM-DD)** — <lesson in one sentence>. Evidence:
  `memory/decisions/<...>`, `memory/decisions/<...>`. Action taken: <prompt fix /
  limit change / none yet>.
