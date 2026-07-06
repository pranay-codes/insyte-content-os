# AI Newsletter Resource Review and Research Bank Playbook

## 1. Purpose

This workflow turns AI newsletter emails into a structured content research pipeline.

It is designed to identify useful resources from AI newsletters, review and score them consistently, organise them in the Notion Research Bank, and make them reusable for newsletters, LinkedIn posts, customer education, and AI content planning.

The purpose is not simply to collect links. The workflow separates useful signal from newsletter noise, captures why each resource matters, and stores it in a form that can be filtered, selected, and reused later.

## 2. Inputs Required

Required inputs:

- Gmail access.
- The live Gmail label inventory.
- A known or discoverable set of AI newsletter/blog labels.
- A search scope, such as unread emails from the last 3 days.
- The number of emails to review, such as the 10 latest matching emails.
- The user's audience, customer, and business context.
- A Notion database link for the Research Bank.
- The Notion database schema and data source ID.
- The already-identified resources from the email review.

Audience and business context used in this workflow:

- Assumption: the audience is B2B AI/automation leaders, operators, and NZ business decision-makers.
- Customer context: practical AI adoption, AI operations, automation, agent workflows, Content OS, customer enablement, and business-facing AI use cases.
- Content context: resources should support newsletter sections, LinkedIn posts, thought leadership, practical AI education, and customer-facing insights.

Notion Research Bank fields used:

- `Title`
- `Link`
- `Evidence Links`
- `Notes`
- `Content Angle`
- `Status`
- `Editorial Decision`
- `Last Reviewed`
- `Research Type`

## 3. Workflow Overview

The workflow starts by identifying which Gmail labels contain AI newsletters or AI blogs. It then searches the latest unread emails within those labels, reads the selected emails, and extracts useful resources such as links, tutorials, tools, reports, videos, tips, playbooks, research papers, and case studies.

Each resource is reviewed and scored against six criteria: audience relevance, customer value, practical usefulness, credibility, newsletter relevance, and LinkedIn relevance. The total score is calculated out of 30.

The reviewed resources are then inserted into the Notion Research Bank as structured rows. Each row is classified by `Research Type` using the database's existing options, such as `Tool - Hands-on review`, `Tool - Stack Pattern`, `Industry Report`, `News - Model / product release`, or `Frontier paper`.

## 4. Step-by-Step Process

### Step 1: Identify AI Newsletter Labels

Objective:

Find which Gmail labels represent AI newsletters, AI blogs, or relevant AI content sources.

What to do:

- Read the live Gmail label inventory.
- Classify labels by name and relevance.
- Treat shorthand such as "IA" as something to verify against the live label list, not as a literal label assumption.
- Keep strong AI newsletter labels separate from adjacent or ambiguous labels.

Inputs used:

- Gmail label inventory.
- Local newsletter-label config only as a cross-check, where available.

Output produced:

- A list of strong AI newsletter/blog labels.

Quality standard:

- Use live Gmail labels rather than assumptions.
- Do not search message bodies just to identify labels.
- Keep ambiguous labels separate from confirmed AI newsletter labels.

AI/newsletter labels identified in this workflow included:

- `Blogs/AI/AI Corner`
- `Blogs/AI/Staying Ahead AI`
- `Blogs/AI/Superhuman AI`
- `Blogs/AI/What's Up In AI`
- `Blogs/AI Fire`
- `Blogs/8020 AI`
- `Blogs/The Rundown AI`
- `Blogs/AI/AI With Allie`
- `Blogs/AI/AI Collective`
- `Blogs/AI/Towards Data Science`

### Step 2: Search Relevant Emails

Objective:

Find the latest unread newsletter emails that match the selected AI labels.

What to do:

- Search unread emails from the agreed date range.
- Restrict the query to the identified AI newsletter labels.
- Return the latest matching emails.
- Keep the search scope explicit.

Inputs used:

- AI newsletter label list.
- Gmail query filters:
  - unread
  - after the relevant date
  - matching selected labels
  - latest 10 results

Output produced:

- A list of relevant unread emails, including:
  - email ID
  - subject
  - sender or source
  - date
  - label

Quality standard:

- Do not broaden the search after the scope is set.
- Do not modify email state.
- Keep Gmail read-only unless the user explicitly asks for changes.

### Step 3: Read Email Bodies

Objective:

Open the selected emails and extract useful resource references.

What to do:

- Read the full body of each selected email where available.
- Identify links and embedded resource mentions.
- Capture both direct links and useful resources mentioned in the body.
- Preserve source URLs where available.

Inputs used:

- The selected Gmail message IDs.
- Email body text.
- Email labels and dates.

Output produced:

- A resource extraction table grouped by email.

Quality standard:

- Preserve URLs.
- Do not invent missing links.
- If a resource is mentioned without an external link, mark that clearly.

### Step 4: Extract Resources

Objective:

Turn email content into a structured list of reusable resources.

What to do:

- Identify useful content types:
  - links
  - resources
  - videos
  - tutorials
  - tips
  - cheat sheets
  - blogs
  - research papers
  - white papers
  - playbooks
  - tools
  - reports
  - case studies
- Exclude pure newsletter navigation links, unsubscribe links, feedback buttons, and social share links unless they point to content-relevant material.

Inputs used:

- Email body text.
- Markdown links inside emails.
- Email source labels.

Output produced:

- A table with each email, date, label, identified content, and source URLs.

Quality standard:

- Resource title must be understandable.
- Link or source must be included where available.
- Non-resource links should be excluded.

### Step 5: Review Resources

Objective:

Evaluate each already-identified resource for relevance and usefulness.

What to do:

- Review the resource where possible.
- Use only resources already identified in the workflow.
- Do not search for new resources.
- Summarise each resource in 1-2 sentences.
- Score each resource using the agreed scoring categories.

Inputs used:

- Previously extracted resource list.
- Available links and email descriptions.
- Existing audience/customer/business context.

Output produced:

- A scored resource review table.

Quality standard:

- Do not add new resources.
- If context is missing, state the assumption.
- If a link cannot be opened, use the email/source context and be transparent.

### Step 6: Score Resources

Objective:

Rank resources based on how useful they are for the audience and content strategy.

What to do:

- Score each resource from 1 to 5 in six categories.
- Calculate the total score out of 30.
- Add a short reason for the score.

Inputs used:

- Resource summary.
- Audience assumption.
- Customer value judgement.
- Practicality and credibility assessment.

Output produced:

- A scored resource table.

Quality standard:

- Scores should reflect usefulness, not personal interest.
- High curiosity does not equal high customer value.
- Credibility and usefulness are separate.

### Step 7: Insert Resources Into Notion

Objective:

Move the reviewed resource list into the Notion Research Bank.

What to do:

- Fetch the Notion database schema first.
- Use the correct data source ID.
- Create one row per reviewed resource.
- Map fields conservatively.

Inputs used:

- Notion Research Bank database.
- Scored resource table.
- Resource links and summaries.

Output produced:

- 50 imported Research Bank rows.

Fields populated:

- `Title`: resource name
- `Link`: direct URL, where available
- `Evidence Links`: URL or source note
- `Notes`: score breakdown, summary, and reason
- `Content Angle`: main idea where used
- `Status`: `Backlog`
- `Editorial Decision`: `Candidate`
- `Last Reviewed`: `2026-07-06`

Quality standard:

- Do not invent URLs.
- If no direct URL exists, preserve that in `Evidence Links`.
- Verify row count after import where possible.

### Step 8: Add Research Type

Objective:

Classify each imported resource so the Research Bank can be filtered by content type.

What to do:

- Use only existing Notion `Research Type` options.
- Classify each row based on the nature of the resource.
- Update rows in place.

Inputs used:

- The imported Research Bank rows.
- Existing Notion `Research Type` options.

Output produced:

- Research type added to the imported rows.

Research types used:

- `Tool - Hands-on review`
- `Tool - Stack Pattern`
- `Industry Report`
- `News - Model / product release`
- `Frontier paper`

Quality standard:

- Use `Research Type` as classification, not endorsement.
- Keep score in `Notes` as the quality signal.
- Do not create new Notion options unless explicitly requested.

## 5. Resource Scoring Method

Each resource is scored from 1 to 5 across six categories.

### Audience Relevance

High score means:

- Directly relevant to B2B AI, automation, operators, business leaders, or NZ decision-makers.
- Fits the audience's current questions and problems.

Low score means:

- Interesting but too far from the target audience.
- Mostly consumer, science curiosity, or unrelated marketing.

### Customer Value

High score means:

- Helps customers make better decisions.
- Could support client education, advisory, implementation, or strategy.

Low score means:

- Little direct usefulness for customers.
- Mostly entertainment, generic content, or low business relevance.

### Practical Usefulness

High score means:

- Can be applied in workflows, decisions, prompts, operations, or content production.
- Gives a clear method, framework, tool, or example.

Low score means:

- Abstract, speculative, or hard to apply.

### Credibility

High score means:

- Comes from a credible company, research group, recognised source, or strong evidence.
- Claims are specific and verifiable.

Low score means:

- Sponsor-heavy, hype-driven, unclear source, or requires verification.

### Newsletter Relevance

High score means:

- Could become a useful newsletter item, main story, section, or practical takeaway.
- Has enough depth for readers.

Low score means:

- Too thin, too niche, or not useful enough for newsletter readers.

### LinkedIn Relevance

High score means:

- Has a strong angle for a LinkedIn post.
- Can support a concise insight, contrarian take, lesson, or practical tip.

Low score means:

- Not likely to create engagement or useful discussion.

### Total Score

Formula:

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

## 6. Output Tables and Formats

### Email Resource Extraction Table

```markdown
| Email | Date | Label | Identified Content | Source / URL |
|---|---|---|---|---|
| Email subject | Email date | Gmail label | Resource title and short description | Link or source note |
```

### Resource Review and Scoring Table

```markdown
| Resource | Link | Main idea | Audience relevance | Customer value | Practical usefulness | Credibility | Newsletter relevance | LinkedIn relevance | Total /30 | Reason for score |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
```

### Notion Research Bank Row Format

```text
Title: Resource name
Link: Direct URL where available
Evidence Links: URL or note about source
Notes: Score breakdown, main idea, reason for score
Content Angle: Main idea or content framing
Status: Backlog
Editorial Decision: Candidate
Last Reviewed: Review date
Research Type: Existing Notion research type
```

## 7. Newsletter Workflow

Scored resources become newsletter candidates based on:

- Total score.
- Newsletter relevance score.
- Practical usefulness.
- Fit with existing newsletter sections.
- Whether the resource can teach the audience something useful.

Likely newsletter uses:

- Main story: high-scoring strategic or business-impact resource.
- Tool of the Week: practical tool or hands-on AI workflow.
- Research to Reality: frontier paper or research with a practical business implication.
- AI News That Actually Matters: model, platform, market, or governance updates.
- Prompt Pattern of the Week: reusable prompt, framework, or evaluation method.
- Facepalm / Failure: weak AI implementation, hype, governance risk, or cautionary example.

Quality standard:

- Do not pick the highest score automatically.
- Pick based on the section's purpose.
- Verify claims before publishing if the item is newsy, controversial, or sponsor-led.
- Prefer resources with clear customer value and practical implications.

## 8. LinkedIn Workflow

Scored resources become LinkedIn ideas when they have:

- A strong insight or tension.
- A practical lesson.
- A clear business implication.
- A concise takeaway.
- Relevance to AI adoption, automation, agents, content systems, or customer operations.

Strong LinkedIn angles from this workflow include:

- AI advantage is shifting from access to habits.
- Custom AI can beat generic frontier models when the task is specific.
- Your AI stack matters less than your workflow discipline.
- Evaluation beats benchmarks when deploying AI in real work.
- AI content quality fails when teams optimise for volume instead of usefulness.

Quality standard:

- Do not just repost the resource.
- Turn the resource into a point of view.
- Connect the insight to a business problem.
- Use the score and reason to decide whether it deserves a post.

## 9. Quality Control Checklist

- [ ] Gmail labels were read live.
- [ ] AI newsletter labels were selected from actual label names.
- [ ] Email search scope was explicit.
- [ ] Emails were read-only unless write access was requested.
- [ ] Only already-identified resources were reviewed.
- [ ] No new resources were searched or added during scoring.
- [ ] Every resource has a title.
- [ ] Every resource has a link or a clear source note.
- [ ] Every resource has a 1-2 sentence main idea.
- [ ] Every resource has six category scores.
- [ ] Total score is out of 30.
- [ ] Score reason is brief and specific.
- [ ] Audience assumption is stated where needed.
- [ ] Notion database schema was fetched before inserting rows.
- [ ] Rows were inserted into the correct data source.
- [ ] Missing links were not invented.
- [ ] `Status` and `Editorial Decision` were applied consistently.
- [ ] `Research Type` uses only existing Notion options.
- [ ] Final row count was verified where possible.
- [ ] Any rate limits or verification blockers were reported clearly.

## 10. Common Mistakes to Avoid

- Restarting the research process instead of continuing from completed work.
- Searching for new resources when the instruction says not to.
- Treating newsletter share links, feedback links, or unsubscribe links as resources.
- Inventing URLs for resources that only appeared as text.
- Scoring based on novelty instead of customer value.
- Giving high scores to interesting but irrelevant science stories.
- Mixing up credibility with usefulness.
- Using `Research Type` as a quality judgement.
- Creating new Notion options without permission.
- Updating the wrong Notion database or using the database URL instead of the data source ID.
- Forgetting to verify imported row counts.
- Hiding rate limits or tool failures.
- Overwriting unrelated Notion rows.
- Treating sponsored content as automatically credible.
- Turning every resource into a newsletter idea even when the score is weak.

## 11. Final Deliverables

This workflow should produce:

- A confirmed list of AI newsletter/blog Gmail labels.
- A scoped list of the latest relevant unread newsletter emails.
- A table of useful resources extracted from those emails.
- A reviewed resource table with:
  - resource
  - link
  - main idea
  - six category scores
  - total score out of 30
  - reason for score
- Notion Research Bank rows for each reviewed resource.
- Research Bank metadata:
  - status
  - editorial decision
  - last reviewed date
  - evidence links
  - notes with score breakdown
  - research type
- A reusable pool of newsletter candidates.
- A reusable pool of LinkedIn post angles.
- A clear record of assumptions, missing links, and verification limits.

## Core-Level Summary

This playbook turns AI newsletters into a reusable research system. The workflow finds relevant newsletter emails, extracts useful resources, scores them for business and content value, stores them in Notion, and classifies them so they can later become newsletter sections, LinkedIn posts, or customer-facing insights.
