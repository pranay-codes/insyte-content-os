# Insyte Content OS

This repository defines an operational Content OS for turning Research Bank items into publish-ready content with a consistent style, strict evidence mapping, and policy guardrails.

## What This Does

From one Research Bank item, the workflow generates:

1. Medium deep-dive post (`2000-10000 words`)
2. Newsletter (`1000-2000 words`)
3. LinkedIn Post A (`150-300 words`)
4. LinkedIn Post B (`150-300 words`)

The system is designed to explain technical concepts (AI, LLM, Agentic AI) in business-clear language and translate technical details into business value.

## Core Workflow

1. `Research input`
- Start with one Research Bank item containing:
  - `Title`
  - `Link`
  - `Why it matters`
- Optional but useful:
  - `Evidence Links`
  - `Content Angle`
  - `Hook`

2. `Link intelligence`
- Analyze `Link` and `Evidence Links`.
- Extract:
  - key technical concepts
  - deep-dive mechanism explanations
  - business usefulness
  - implications (cost, risk, operations, quality)
  - value hypotheses
  - action recommendations

3. `Draft generation`
- Generate 4 channel-specific drafts:
  - Medium
  - Newsletter
  - LinkedIn A
  - LinkedIn B

4. `Evidence validation`
- Validate that factual claims include source mapping.

5. `Write to Content Library`
- Create/update Content Library pages and return links.

## Skill Package

Skill location:
- `skills/content-writing-os/`

Key files:

1. `skills/content-writing-os/SKILL.md`
- Skill behavior, workflow, and command entrypoints.

2. `skills/content-writing-os/references/style_baseline.md`
- Baseline style anchor.

3. `skills/content-writing-os/references/style_live.md`
- Active style rules used during generation.

4. `skills/content-writing-os/references/format_rules.md`
- Output structures and length targets.

5. `skills/content-writing-os/references/analysis_framework.md`
- How usefulness, meaning, and deep-dive concept analysis are done.

6. `skills/content-writing-os/scripts/`
- Deterministic scripts for generation, validation, and adaptive updates.

## Commands

## 1) Analyze source links

```powershell
python skills/content-writing-os/scripts/link_intelligence.py --research-json research.json --output insights.json
```

## 2) Generate drafts using insights

```powershell
python skills/content-writing-os/scripts/compose_drafts.py --research-json research.json --insights-json insights.json --output-dir drafts
```

## 3) Validate evidence mapping

```powershell
python skills/content-writing-os/scripts/validate_evidence.py --input drafts --min-entries 1
```

## 4) Build Notion payload (optional utility)

```powershell
python skills/content-writing-os/scripts/notion_writer.py --research-url <url> --research-title "<title>" --publish-week YYYY-MM-DD
```

## Adaptive Style Updates

Tone and format can evolve over time without uncontrolled drift.

Process:

1. Mine published content patterns:

```powershell
python skills/content-writing-os/scripts/style_miner.py --input-dir published_markdown --output metrics.json
```

2. Create proposal (no auto-apply):

```powershell
python skills/content-writing-os/scripts/style_proposal.py --metrics metrics.json --output proposal.md --min-docs 6
```

3. Apply only after explicit approval:

```powershell
python skills/content-writing-os/scripts/style_apply.py --proposal proposal.md --style-live skills/content-writing-os/references/style_live.md --changelog skills/content-writing-os/references/style_changelog.md
```

## What This Achieves

1. Faster content production
- One research item becomes a complete multi-channel content set.

2. Better quality and trust
- Strict evidence mapping reduces unsupported claims.

3. Business-relevant technical content
- Technical depth is translated into practical business decisions.

4. Repeatable operating system
- Same structure and standards every week.

5. Controlled improvement
- Style adapts from published content via approval-based proposals.

## Governance and Safety

Repository policy is enforced by:

1. `AGENTS.md`
2. `POLICY.md`

Key controls include:

1. Notion scope restrictions to Content OS objects only.
2. SOP compliance checks before writes.
3. Explicit override behavior when SOP proof is stale.

## Prompt Example

```text
Use $content-writing-os to take this Research Bank item: <RESEARCH_ITEM_URL>. Research all links in Link + Evidence Links, extract deep technical concepts, explain them for business owners, evaluate usefulness/implications/value, then generate and write 4 drafts to Content Library (Medium deep dive, Newsletter, LinkedIn A, LinkedIn B) with strict evidence mapping. Return the 4 Notion page links plus SOP compliance status.
```
