---
name: content-writing-os
description: Generate Content OS drafts from Research Bank items and keep writing style current through controlled, biweekly proposal updates. Use when the user asks to create Medium/newsletter/LinkedIn content, map claims to evidence, write content into Content Library, or propose tone/format refinements from published posts.
---

# Content Writing OS

## Overview

Use this skill to produce a full content set from one Research Bank item:
1. Medium deep-dive (`2000-10000 words`)
2. Newsletter (`1000-2000 words`)
3. LinkedIn Post A (`150-300 words`)
4. LinkedIn Post B (`150-300 words`)

Apply strict evidence mapping for factual claims and write outputs into Content Library records inside the allowlisted Content OS scope.
The default tone is technical but clear, with deep-dive explanations of AI, LLM, and Agentic AI concepts translated into business value and fundamentals.

## Workflow

## 1) Generate Content Set From Research Item

1. Load the research item from Research Bank.
2. Validate required fields:
- `Title`
- `Link`
- `Why it matters`
3. Validate weekly SOP gate before any write:
- marker task `Editorial Review - Weekly Shortlist`
- `Status=Done`
- completed within the last 7 days
4. Run link intelligence pass on `Link` and all `Evidence Links`:
- extract key concepts
- explain concepts for business audience
- evaluate business usefulness and implications
- identify value opportunities and risk conditions
5. Generate Medium -> Newsletter -> LinkedIn A/B in that order.
6. Ensure each factual claim has evidence mapping to `Link` or `Evidence Links`.
7. Write drafts into Content Library pages and return created or updated page URLs.

## 2) Enforce Tone and Format

1. Use `references/style_live.md` as active voice guide.
2. Keep style anchored to `references/style_baseline.md` (source: provided Medium article).
3. Follow channel structures and length limits in `references/format_rules.md`.
4. Use templates from `references/output_templates.md`.

## 3) Propose Adaptive Style Updates (No Auto-Apply)

1. Run biweekly style mining from published Content Library pieces only.
2. Require at least 6 new published pieces before proposing updates.
3. Use high drift guard:
- recurring pattern in >=4 pieces
- no conflict with baseline non-negotiables
4. Create proposal only; do not auto-edit live references.
5. Apply updates only after explicit approval.

## References To Load

1. `references/style_baseline.md`
2. `references/style_live.md`
3. `references/format_rules.md`
4. `references/notion_field_map.md`
5. `references/output_templates.md`
6. `references/examples.md`
7. `references/analysis_framework.md`
8. `references/update_proposal_template.md`
9. `references/style_changelog.md`

## Script Entrypoints

1. Draft generation:
```powershell
python scripts/compose_drafts.py --research-json <path> --output-dir <dir>
```

2. Evidence validation:
```powershell
python scripts/validate_evidence.py --input <draft.md>
```

3. Style mining:
```powershell
python scripts/style_miner.py --input-dir <published_markdown_dir> --output <metrics.json>
```

4. Style proposal:
```powershell
python scripts/style_proposal.py --metrics <metrics.json> --output <proposal.md> --style-live references/style_live.md
```

5. Apply approved proposal:
```powershell
python scripts/style_apply.py --proposal <proposal.md> --style-live references/style_live.md --changelog references/style_changelog.md
```

6. Notion payload preview (optional):
```powershell
python scripts/notion_writer.py --research-url <url> --research-title <title> --publish-week <yyyy-mm-dd>
```

7. Link intelligence analysis:
```powershell
python scripts/link_intelligence.py --research-json <path> --output <insights.json>
```

## Failure Handling

1. Missing required research fields:
- stop generation
- return exact missing fields

2. Missing evidence mapping:
- fail validation
- return claims needing sources

3. SOP gate stale:
- warn user
- require explicit override confirmation before writes

4. Style update sample size <6:
- skip proposal
- log `insufficient signal`

5. Link fetch or parsing failures:
- continue with available sources
- report failed URLs explicitly
