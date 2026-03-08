# Examples

## Example Input

Research Bank item:
- Title: `RAG Cost Breakdown for SMB Support`
- Link: `https://example.com/rag-cost-analysis`
- Why it matters: `Most SMBs underestimate serving costs and latency tradeoffs.`
- Evidence Links: `https://example.com/rag-cost-analysis, https://example.com/vector-db-pricing`

## Example Skill Request

`Generate Medium, newsletter, and 2 LinkedIn drafts from research item <url> and write them to Content Library.`

## Expected Output Behavior

1. Run link intelligence analysis on `Link` + `Evidence Links`.
2. Extract concepts, deep-dive explanations, business usefulness, implications, and value hypotheses.
3. Use these insights to draft all outputs.
1. Create or update 4 Content Library records linked to the same `Primary Research`.
2. Medium draft explains architecture and pricing mechanics in business terms.
3. Newsletter summarizes decision implications and action checklist.
4. LinkedIn A/B provide concise, value-driven angles.
5. Return 4 Notion page URLs and SOP compliance metadata.

## Example Evidence Mapping

1. Claim: `RAG serving cost scales with context length and query volume.`
- Source: `https://example.com/rag-cost-analysis`

2. Claim: `Vector storage costs become significant after large corpus ingestion.`
- Source: `https://example.com/vector-db-pricing`
