# Daily Content OS Research Intake

## Schedule

- Name: `Daily Content OS Research Intake`
- Time: `08:00`
- Timezone: `Pacific/Auckland`
- Workspace: `C:\workspace\Insyte Technologies\repository\insyte-content-os`
- Execution environment: local Codex automation

## Definition Of Done

The automation is complete for a run when it has:

1. Read `AGENTS.md` and `POLICY.md`.
2. Loaded Gmail labels from `config/newsletter-labels.txt`.
3. Read at most the 10 newest total Gmail messages across all configured labels.
4. Extracted and evaluated linked resources from those newsletters.
5. Rejected low-value AI news, hype, duplicate links, and items without practical business value.
6. Fetched the allowlisted Research Bank target before any write.
7. Inserted only candidates scoring `70+` into Research Bank.
8. Reported added, skipped, duplicate, failed, and blocked counts.
9.  For every inserted item, reported page URL or ID, changed fields, SOP compliance status, proof task URL, and proof age in days.

## Prompt Contract

Goal:
- Keep the Content OS Research Bank stocked with practical, content-ready AI resources for newsletters and LinkedIn posts.
- Prefer resources that help non-technical business owners understand what AI can do inside their business.

Inputs:
- Label file: `config/newsletter-labels.txt`
- Gmail connector access
- Notion connector access
- Research Bank database: `https://www.notion.so/2f45eb948864801180bafa69e23150f7`
- Research Bank data source: `collection://2f45eb94-8864-801b-a248-000b106b02c4`
- Inbox task data source for SOP proof: `collection://24cec550-1950-47d4-b00f-16e0809faa54`

Constraints:
- Read the latest 10 total matching emails across all configured labels, not 10 per label.
- Auto-write only curated items that pass the quality threshold.
- Follow `POLICY.md` before every Notion action.
- Before every write, fetch the Research Bank target and confirm it is allowlisted.
- Do not add ordinary AI news unless practical value is clear.
- Do not read or write any Notion object outside the allowlist in `POLICY.md`.
- Do not change Notion schemas or views.

Failure modes:
- Missing label file: stop and report the expected path.
- Empty label file after ignoring comments and blanks: stop and report that labels are required.
- No matching Gmail messages: report no newsletters found and write nothing.
- Email body cannot be read: skip that email and report subject and message ID.
- Candidate link cannot be opened or evaluated: skip it unless the email body gives enough evidence.
- Duplicate Research Bank link: skip it.
- Notion query fails: use Notion search and fetch fallback, and report the exact failure string.

## Operating Steps

1. Read local guardrails:
   - Read `AGENTS.md`.
   - Read `POLICY.md`.
   - Enforce the stricter rule if the two differ.

2. Load newsletter labels:
   - Read `config/newsletter-labels.txt`.
   - Trim whitespace.
   - Ignore blank lines.
   - Ignore lines beginning with `#`.
   - If no labels remain, stop.

3. Search Gmail:
   - For each label, run a Gmail label search for recent messages.
   - Prefer Gmail query syntax: `label:"<label name>"`.
   - Request no more than 10 messages per label at search time.
   - Combine results across labels by received timestamp.
   - Deduplicate message IDs.
   - Keep only the newest 10 total messages.
   - Batch read the selected message bodies.

4. Extract candidates:
   - Extract outbound links from message bodies.
   - Ignore unsubscribe, preference, tracking-only, social-share, login, privacy, terms, and footer links.
   - Normalize common tracking wrappers when the destination URL is visible.
   - Keep source newsletter label, sender, subject, message ID, email date, candidate title, URL, and surrounding context.
   - Deduplicate URLs within the run.

5. Evaluate candidates:
   - Apply hard gates first.
   - Score remaining candidates out of 100.
   - Auto-write only candidates scoring `70+`.
   - Report candidates scoring `55-69` but do not insert them.
   - Ignore candidates below `55` unless needed for the failure summary.

6. Check duplicates against Research Bank:
   - Prefer querying Research Bank by exact `Link` if the Notion query tool works.
   - If query fails, report the exact error and use Notion search within `collection://2f45eb94-8864-801b-a248-000b106b02c4` for the exact URL and normalized URL.
   - Skip a candidate if the same URL is already present.

7. Verify SOP before writing:
   - Search the Inbox task data source for `Editorial Review - Weekly Shortlist`.
   - Fetch the newest matching page.
   - Confirm parent data source is `collection://24cec550-1950-47d4-b00f-16e0809faa54`.
   - Confirm `Status=Done`.
   - Compute proof age in days from the page completion timestamp. If no dedicated completion timestamp exists, use `Last edited time` as the proof timestamp only when the fetched page has `Status=Done`.
   - If proof age is greater than 7 days, stop and write nothing.

8. Fetch Research Bank target before writing:
   - Fetch `collection://2f45eb94-8864-801b-a248-000b106b02c4`.
   - Confirm the target matches `POLICY.md`.
   - Confirm the properties used below exist.

9. Create Research Bank pages:
   - Parent: `data_source_id=2f45eb94-8864-801b-a248-000b106b02c4`
   - Properties:
     - `Title`
     - `Link`
     - `Research Type`
     - `Proposed Section`
     - `Status=Backlog`
     - `Why it matters`
     - `Evidence Links`, when available
     - `Notes`
     - `date:Last Reviewed:start` set to the run date
     - `date:Last Reviewed:is_datetime=0`

10. Final report:
    - Search scope and labels used.
    - Number of emails searched and read.
    - Number of candidates extracted.
    - Added items with page URL or ID and changed fields.
    - Skipped duplicates.
    - Skipped low-score items.
    - Failed email reads or failed link evaluations.
    - Proof task URL and proof age in days when a write occurred.

## Quality Threshold

Use hard gates first, then a 100-point score. Auto-insert only if the item scores `80+`.

Hard reject if:
- No credible source link exists.
- The item is only hype, funding news, generic launch news, or insider commentary.
- The business value is vague.
- It cannot be explained clearly to a non-technical business owner.
- It duplicates an existing Research Bank link.
- It is interesting to AI insiders but not useful to the target audience.

Scoring:
- Practical business usefulness: `30`
- Content potential for newsletter or LinkedIn: `20`
- Evidence strength: `20`
- Relevance to AI adoption, workflows, tools, risk, or operations: `15`
- Novelty or signal value: `15`

Decision bands:
- `90-100`: Strong insert, likely newsletter-worthy.
- `70-89`: Insert as Research Bank backlog.
- `55-69`: Report only, do not insert.
- `<55`: Ignore.

The core test is: could this help a business owner understand, decide, improve, avoid a mistake, or try something practical in their business?

## Accepted Article Types

Accepted:
- Practical AI tool
- Tool review or walkthrough
- Workflow pattern
- Stack pattern
- Prompt pattern
- Model or product release with clear business impact
- Industry report
- Research paper with practical translation
- Frontier paper with clear business implication
- Failure or incident
- Case study
- AI adoption or operating model article
- Customer experience example
- Automation opportunity article

Best-fit Research Bank categories:
- Workflow pattern
- Practical AI tool
- Prompt pattern
- Stack pattern
- Industry report
- Case study
- Failure or incident

Reject by default:
- Funding announcements
- Generic launch news
- AI hype pieces
- Opinion-only commentary
- Technical benchmark-only posts
- Speculative AI market commentary
- Shallow top-tools listicles
- Repeated model leaderboard updates

## Classification Mapping

- Practical tool or hands-on walkthrough:
  - Research Type: fetched option containing `Tool` and `Hands-on review`
  - Proposed Section: fetched option named `Tool of the Week`
- Stack or workflow pattern:
  - Research Type: fetched option containing `Tool` and `Stack Pattern`
  - Proposed Section: fetched option containing `Research` and `Reality`
- Prompt pattern:
  - Research Type: fetched option containing `Tool` and `Stack Pattern`
  - Proposed Section: fetched option named `Prompt Pattern of the Week`
- Model or product release with business impact:
  - Research Type: fetched option containing `News`, `Model`, and `product release`
  - Proposed Section: fetched option named `AI News That Actually Matters`
- Industry report:
  - Research Type: fetched option named `Industry Report`
  - Proposed Section: fetched option containing `Research` and `Reality`
- Research or frontier paper:
  - Research Type: fetched option named `Frontier paper`
  - Proposed Section: fetched option containing `Research` and `Reality`
- Failure or incident:
  - Research Type: fetched option containing `Failure` and `incident`
  - Proposed Section: fetched option named `Facepalm / Failure`

Use exact Notion option strings from the fetched Research Bank schema for the final write. Do not write ASCII approximations if the schema label uses different punctuation.

## Insert Content Standards

`Why it matters` must be brief and business-facing:
- One to three sentences.
- Plain English.
- Explain the practical business implication.
- Avoid hype.

`Notes` must include:
- Source newsletter label.
- Email subject.
- Email date.
- Candidate score.
- Selection reason.
- Any risk or limitation worth knowing.

`Evidence Links` should include supporting URLs when the email provides more than one useful source for the same candidate.
