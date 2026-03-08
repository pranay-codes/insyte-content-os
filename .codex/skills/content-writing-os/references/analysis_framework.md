# Link Intelligence Framework

Use this framework when analyzing `Link` and `Evidence Links` from a Research Bank item.

## Objective

Go beyond extraction and summarization. For each source, answer:
1. What concept does this explain?
2. Why does that concept matter for a business owner?
3. What does it imply for decisions, cost, risk, and growth?
4. What value can be captured and under what assumptions?

## Per-Source Analysis Schema

For each URL, produce:
1. `concepts`
- core technical concepts introduced by the source
2. `deep_dive_explanation`
- mechanism-level explanation in clear language
- include architecture, flow, tradeoffs, and failure modes
3. `business_usefulness`
- where this concept creates practical business leverage
4. `implications`
- what changes for budgeting, operations, quality, and risk
5. `value_hypotheses`
- plausible value outcomes with assumptions
6. `limits_and_risks`
- where advice does not generalize or may fail
7. `action_recommendations`
- concrete next actions for a business operator

## Cross-Source Synthesis

After per-source analysis, synthesize:
1. recurring concepts across sources
2. conflicting claims and why they differ
3. prioritized decisions for business owners
4. implementation sequence:
- now
- next
- later

## Quality Bar

1. No unsupported claims.
2. No vague "AI will transform everything" language.
3. Every recommendation tied to mechanism and business impact.
4. Explicitly separate:
- fact
- interpretation
- recommendation
