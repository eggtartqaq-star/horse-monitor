# How the two axis scores in the Owner PDFs were derived

**Author:** 皮褸黃 (CEO). **Raised by code review 2026-07-28:** the Quality and Price
scores driving the quadrant chart appeared only inside the generator, uncited —
a breach of CLAUDE.md rule 5. This file is the citation.

They are **CEO composites of the department scores already filed in `reports/`**, not
new measurements. Judgement weightings are mine and are stated so they can be argued with.

## Axis A — Business Quality
Composite of: Financial score (巴爺爺) · moat rating (菲比斯, mapped none=10 / narrow-eroding=30
/ narrow=50 / narrow-widening=65 / wide=90) · management grade (Peter, A=90…F=10) ·
industry call (Elon Musk, overweight=70 / neutral=50 / underweight=30). Equal-ish weight,
financials and moat carrying most.

| | Fin | Moat | Mgmt | Industry | **Composite** |
|---|---|---|---|---|---|
| KLAC | 91 | wide/widening 90 | A− 85 | o/w 70 | **88** |
| MU | 82 | narrow/widening 65 | A− 85 | o/w 70 | **70** |
| MRVL | 66 | narrow/eroding 30 | B+ 75 | o/w 55 | **52** |
| INTC | 55 | narrow-eroding + none 25 | not filed | neutral 45 | **45** |
| BE | 45 | narrow/eroding 30 | not filed | o/w-mod 55 | **35** |

## Axis B — Price Attractiveness
Composite of: valuation score (𢦀鳩仔) · margin of safety delivered vs the moat-adjusted
requirement · technical entry location (老詹) where filed.

| | Valuation | MoS delivered vs required | Technical | **Composite** |
|---|---|---|---|---|
| KLAC | 33 | −126% vs 25–30% req. | 58 | **38** |
| MU | 15 | −165% vs 40–50% req. | 45 | **20** |
| MRVL | 25 | −170% vs 35–40% req. | 34 | **26** |
| INTC | 12 | −178% vs 50% req. | not filed | **14** |
| BE | 8 | −649% vs 60% req. | not filed | **10** |

**Known limitation:** INTC and BE ran on a reduced 3-agent core because of session
limits, so they have no management or technical report. Their Axis A and B scores are
built on fewer inputs and should be read as lower-confidence than KLAC/MU/MRVL.
