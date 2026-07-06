# Daily AI Newsletter Research Bank Automation

## Contract Authority

This file is the operating contract for the daily AI newsletter resource review automation.

Do not follow older or separate automation contracts for this run, including prior daily intake or weekly draft production contracts. Use the existing `ai-newsletter-research-bank` skill and `playbook.md` as the workflow sources for this automation.

## Purpose

Run the existing AI newsletter resource review workflow every day at 10:00am Pacific/Auckland time. The automation reviews recent AI newsletter emails, extracts useful resources, scores them, classifies them, writes eligible resources to the Research Bank, and produces newsletter and LinkedIn planning outputs.

## Schedule

- Frequency: daily.
- Local time: 10:00am.
- Timezone: Pacific/Auckland.
- Scheduler: Codex cron automation.

Timezone handling:

- The Codex automation schedule is configured for 10:00am local run time where supported by the Codex automation environment.
- The run prompt must explicitly state Pacific/Auckland as the intended timezone.
- If a future scheduler only supports UTC cron, do not assume a fixed UTC hour because Pacific/Auckland changes with daylight saving time. Use a timezone-aware wrapper or update the UTC schedule seasonally with a documented DST check.

## Required Sources

Use the existing workflow context:

- Skill: `ai-newsletter-research-bank`
- Playbook: `playbook.md`
- Gmail labels: read the live Gmail label inventory first.
- Local label cross-check: `config/newsletter-labels.txt`
- Research Bank data source: `collection://2f45eb94-8864-801b-a248-000b106b02c4`
- Research Bank database URL: `https://app.notion.com/p/pranay-narotam/2f45eb948864801180bafa69e23150f7`

Default audience and business context:

- Audience: B2B AI/automation leaders, operators, and NZ business decision-makers.
- Customer context: practical AI adoption, AI operations, automation, agent workflows, Content OS, customer enablement, and business-facing AI use cases.
- Content context: newsletter sections, LinkedIn posts, thought leadership, practical AI education, and customer-facing insights.

## Daily Run Scope

1. Read the live Gmail label inventory.
2. Identify AI newsletter or AI blog labels using the existing workflow rules.
3. Cross-check with `config/newsletter-labels.txt`.
4. Search the latest unread emails from the last 3 days that match the selected AI newsletter labels.
5. Review up to 10 latest matching emails.
6. Extract useful resources, links, videos, tutorials, tips, cheat sheets, blogs, research papers, white papers, tools, reports, playbooks, and case studies.
7. Exclude unsubscribe links, preference links, tracking-only links, feedback links, generic share links, and non-resource navigation links.
8. Open and review each resource where possible.
9. Score each resource using the six-category scoring method.
10. Classify each resource by Research Type using existing Notion options only.
11. Avoid duplicate processing before writing to Notion.
12. Insert new candidate resources into the Research Bank.
13. Produce newsletter candidate ideas.
14. Produce LinkedIn angles.
15. Append a clear run log to the automation memory file.

Do not search for new resources outside the selected emails unless the user explicitly changes this contract.

## Duplicate Avoidance

Before inserting a resource into Research Bank:

- Check for an existing row with the same `Link`.
- If `Link` is missing, check for a close match on `Title` plus source email/date.
- If a duplicate is found, do not create a new row.
- Record skipped duplicates in the final report and run log.
- If the same resource appears in multiple emails, preserve the additional source evidence in notes where possible.

## Scoring Method

Score each resource from 1 to 5 in each category:

- Audience relevance
- Customer value
- Practical usefulness
- Credibility
- Newsletter relevance
- LinkedIn relevance

Total score:

```text
Audience relevance
+ Customer value
+ Practical usefulness
+ Credibility
+ Newsletter relevance
+ LinkedIn relevance
= Total /30
```

Interpretation:

- `27-30`: Excellent candidate for newsletter, LinkedIn, or client-facing content.
- `23-26`: Useful candidate, may need framing or verification.
- `18-22`: Mixed value; use selectively.
- `<18`: Low priority unless there is a specific reason to use it.

## Research Bank Field Mapping

Populate fields conservatively:

- `Title`: resource name.
- `Link`: direct URL where available.
- `Evidence Links`: URL or source note.
- `Notes`: main idea, score breakdown, total score, reason for score, source email/date, and any access limitation.
- `Content Angle`: main idea or content framing.
- `Status`: `Backlog`.
- `Editorial Decision`: `Candidate`.
- `Last Reviewed`: run date.
- `Research Type`: existing Notion option only.

Research Type guidance:

- `Tool - Hands-on review`: tactical tools, tutorials, prompt packs, practical walkthroughs, hands-on product use.
- `Tool - Stack Pattern`: repeatable workflows, system designs, integration patterns, operating models.
- `Industry Report`: business adoption, market trends, governance, strategy, customer behavior, regional impact, case reports.
- `News - Model / product release`: model launches, product updates, platform releases, robotics/silicon announcements, company news.
- `Frontier paper`: research papers, technical methods, benchmark studies, scientific AI work.
- `Failure / incident`: AI failures, governance incidents, security risks, customer harm, public mistakes.

Do not create new Research Type options without explicit user approval.

## Required Outputs

The automation final report must include:

1. Run date and intended timezone.
2. Gmail labels used.
3. Email search scope.
4. Emails searched and emails read.
5. Resource extraction table.
6. Resource review and scoring table.
7. New Research Bank rows created, with page URLs where available.
8. Duplicate resources skipped.
9. Inaccessible resources or failed link reviews.
10. Newsletter candidate table.
11. LinkedIn angle table.
12. Quality check status.
13. Tool failures, rate limits, or exact error strings.
14. Automation memory append status.

## Output Tables

Email resource extraction table:

```markdown
| Email | Date | Label | Identified Content | Source / URL |
|---|---|---|---|---|
```

Resource review and scoring table:

```markdown
| Resource | Link | Main idea | Audience relevance | Customer value | Practical usefulness | Credibility | Newsletter relevance | LinkedIn relevance | Total /30 | Reason for score |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
```

Newsletter candidate table:

```markdown
| Section | Resource | Link | Why it fits | Reader takeaway | Verification needed |
|---|---|---|---|---|---|
```

LinkedIn angle table:

```markdown
| Resource | Link | Angle | Business implication | Suggested post format | Score rationale |
|---|---|---|---|---|---|
```

## Logging

Append each run to:

```text
C:\Users\Lenovo Thinkbook\.codex\automations\daily-ai-newsletter-research-bank\memory.md
```

If `CODEX_HOME` is set, use:

```text
%CODEX_HOME%\automations\daily-ai-newsletter-research-bank\memory.md
```

Each run log entry must include:

- Run timestamp.
- CWD.
- Labels used.
- Emails searched/read.
- Resources extracted.
- New Research Bank rows created.
- Duplicate skips.
- Failed reads/link evaluations.
- Newsletter candidates.
- LinkedIn candidates.
- Errors or rate limits.
- Final status.

If the memory file or directory does not exist, create it.

## Error Handling

- If Gmail access fails, stop and report the exact error.
- If label inventory cannot be read, stop before searching emails.
- If `config/newsletter-labels.txt` is missing, continue from the live Gmail label inventory and report the missing config as a warning.
- If Notion schema cannot be fetched, do not write rows; return an import-ready table instead.
- If Notion writes fail, report the exact error and keep the scored table in the final output.
- If Notion rate limits verification, report which writes succeeded and which verification could not complete.
- If a resource cannot be opened, mark it as inaccessible and score conservatively from available context.
- If duplicate detection is uncertain, skip automatic insert and report the resource for review.

## Manual Test

To test manually, ask Codex from this repository:

```text
Run the Daily AI Newsletter Research Bank Automation manually.

Read and follow automations/daily-ai-newsletter-research-bank.md.
Use $ai-newsletter-research-bank and playbook.md.
Limit the run to the latest 3 matching unread emails from the last 3 days.
Do not mark emails as read.
Create Research Bank rows only for non-duplicate resources.
Return the final report and append the automation memory.
```

For a dry run, add:

```text
Dry run only: do not write to Notion. Return the import-ready table and duplicate check findings.
```

## Environment And Access Requirements

Required:

- Gmail connector access.
- Notion connector access.
- Access to the Research Bank data source.
- The `ai-newsletter-research-bank` skill installed or available in the Codex skill path.
- Repository path: `C:\workspace\Insyte Technologies\repository\insyte-content-os`.

No new project dependency is required.

## Quality Checks

Before finishing each run:

- [ ] Live Gmail labels were checked.
- [ ] Email scope was explicit.
- [ ] Emails were read-only.
- [ ] Only selected email resources were reviewed.
- [ ] No outside resource search was performed.
- [ ] Every resource has a title.
- [ ] Every resource has a link or source note.
- [ ] Every scored resource has six scores and a total out of 30.
- [ ] Research Type values use only existing Notion options.
- [ ] Duplicate checks ran before inserts.
- [ ] Notion writes were verified where possible.
- [ ] Newsletter and LinkedIn outputs were produced from scored resources.
- [ ] Errors and rate limits were reported clearly.
- [ ] Automation memory was appended.
