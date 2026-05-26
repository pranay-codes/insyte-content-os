# Weekly Content OS Draft Production

## Schedule

- Name: `Weekly Content OS Draft Production`
- Time: `08:00`
- Timezone: `Pacific/Auckland`
- Workspace: `C:\workspace\Insyte Technologies\repository\insyte-content-os`
- Execution environment: local Codex automation

## Definition Of Done

The automation is complete for a run when it has:

1. Read `AGENTS.md` and `POLICY.md`.
2. Verified weekly SOP proof before any write:
   - Find the most recent Inbox task titled `Editorial Review - Weekly Shortlist`.
   - Verify `Status=Done`.
   - Verify proof age is <= 7 days.
3. Selected eligible Research Bank items using the eligibility and cooldown rules in this contract.
4. Created exactly:
   - 1 Content Library `Newsletter Issue` draft
   - 3 Content Library `Linkedin Post` drafts
5. Updated the selected Research Bank items:
   - `Status=Used`
   - `Selected Week` set to the run date (YYYY-MM-DD)
6. Created exactly 1 Inbox review task linking all 4 draft assets.
7. Reported created/updated URLs, changed fields, skipped candidates with reasons, and SOP compliance details.

## Prompt Contract

Goal:
- Every Tuesday, create a weekly draft batch from eligible Research Bank items:
  - 1 newsletter draft issue
  - 3 LinkedIn draft posts
- Insert the drafts into Content Library and create a single weekly review task in the Content OS Inbox.

Inputs:
- Research Bank data source: `collection://2f45eb94-8864-801b-a248-000b106b02c4`
- Content Library data source: `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`
- Inbox task data source (SOP proof + review task): `collection://24cec550-1950-47d4-b00f-16e0809faa54`
- Content OS root page (Project relation value): `https://www.notion.so/2445eb9488648013a9e7d9300346de18`

Constraints:
- Follow `POLICY.md` before every Notion action.
- Do not read or write any Notion object outside the allowlist in `POLICY.md`.
- Do not change Notion schemas or views.
- Drafting and tasking only. Do not publish, schedule publishing, or mark Content Library items as `Published`.
- Unattended run behavior:
  - If weekly SOP proof is missing or stale, stop and write nothing. Do not ask for override.
  - If there are not enough eligible items to form the fixed batch (1 newsletter + 3 LinkedIn), stop and write nothing.

Failure modes:
- Notion query tool missing:
  - Report the exact error string and use search+fetch fallback only inside the allowlisted data sources.
- SOP proof fails:
  - Report exactly:
    `Weekly SOP compliance is missing (no completed "Editorial Review - Weekly Shortlist" in the last 7 days). Confirm override to continue this write.`
  - Stop without writing.
- Insufficient eligible research:
  - Stop without writing and report which rule(s) eliminated candidates.
- Any Notion write fails:
  - Stop further writes and report the exact error string and the intended target data source.

## Eligibility Rules

Required fields (must be present and non-empty):
- `Title`
- `Link`
- `Why it matters`

Hard rejects:
- `Status=Not Worthy`
- `Editorial Decision=Rejected`
- Missing required fields
- Shallow hype, purely funding/news noise, or unclear business value

Preferred pool:
- Prefer `Status=Backlog` or `Status=Shortlisted`.

Reuse pool:
- Allow `Status=Used` or `Status=Recycle Later` only if:
  - It has not been used in the last 60 days, and
  - It still appears relevant today.

Cooldown rule (two months):
- A research item counts as "used" if any Content Library draft or published asset was created from it.
- If used within the last 60 days, it is ineligible for reuse in this run.

Relevance check (only for reuse candidates older than 60 days):
- Still relevant means the core idea still applies now and is not tied to a past deadline, discontinued feature, or outdated regulatory date.

## Weekly Batch Output (Fixed)

Each run creates:
- 1 newsletter issue draft
- 3 LinkedIn post drafts (1 research item per post)
- 1 Inbox weekly review task linking all drafts

## Newsletter Grouping Rule

For the single newsletter issue:
- If one research item is deep and thorough enough for a full issue, use 1 item.
- Otherwise bundle 2 or 3 related items into one coherent issue.
- Avoid "grab bag" bundles: bundling is only allowed when the items clearly support one shared theme.

## LinkedIn Selection Rule

For the 3 LinkedIn drafts:
- Exactly 1 research item per LinkedIn post.
- A research item can be used for both the newsletter and a LinkedIn post in the same run when it has a strong standalone LinkedIn angle.
- Prefer variety across the 3 LinkedIn posts.

## Operating Steps

1. Read local guardrails:
   - Read `AGENTS.md`.
   - Read `POLICY.md`.
   - Enforce the stricter rule if they differ.

2. Verify SOP proof (before any write):
   - Search within Inbox data source `collection://24cec550-1950-47d4-b00f-16e0809faa54` for the newest task with title `Editorial Review - Weekly Shortlist`.
   - Fetch the newest matching page.
   - Confirm it is inside the Inbox data source.
   - Confirm `Status=Done`.
   - Compute proof age in days from completion timestamp when available, otherwise use `Last edited time` only when `Status=Done`.
   - If proof age > 7 days, stop and write nothing.

3. Fetch Notion targets before writing:
   - Fetch Research Bank data source `collection://2f45eb94-8864-801b-a248-000b106b02c4`.
   - Fetch Content Library data source `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`.
   - Fetch Inbox data source `collection://24cec550-1950-47d4-b00f-16e0809faa54`.
   - Confirm all targets match `POLICY.md`.

4. Build a candidate list (search+fetch fallback only):
   - Search inside Research Bank data source for candidate items using broad terms (e.g., recent additions, "Shortlisted", high-signal topics).
   - Fetch each candidate page to read properties.
   - Apply eligibility rules to produce an eligible set.
   - Derive "recently used" by checking `Selected Week` and/or any linked Content Library assets created in the last 60 days (search+fetch).

5. Select the weekly batch deterministically:
   - Use `skills/content-writing-os/scripts/weekly_selector.py` with a JSON candidate list to select:
     - newsletter plan (single or bundle of 2-3)
     - 3 LinkedIn research items
     - skip reasons
   - If selection cannot produce a full batch, stop and write nothing.

6. Draft content (must follow channel guides):
   - Newsletter: follow `skills/content-writing-os/references/channel_newsletter.md`.
   - LinkedIn: follow `skills/content-writing-os/references/channel_linkedin.md`.
   - No em dashes in any output.
   - Include evidence mapping for factual claims.

7. Create Content Library draft pages:
   - Parent: `data_source_id=2f45eb94-8864-8040-aa3a-000b4dc54386`
   - All created pages must set:
     - `Status=Drafting`
     - `QA Ready=__NO__`
     - `date:Publish Week:start` = run date (YYYY-MM-DD)
     - `date:Publish Week:is_datetime=0`

   Newsletter page:
   - `Content Type=Newsletter Issue`
   - `Asset Role=Core`
   - `Primary Research` = anchor research URL
   - `Research` = JSON array of all research URLs used in newsletter (1-3)

   LinkedIn pages (3):
   - `Content Type=Linkedin Post`
   - `Asset Role=Derivative`
   - `Primary Research` = that post's research URL
   - `Parent Asset` = newsletter page URL only when intentionally derived from the newsletter

8. Update Research Bank items:
   - For every selected research URL:
     - set `Status=Used`
     - set `date:Selected Week:start` = run date
     - set `date:Selected Week:is_datetime=0`

9. Create the weekly review Inbox task:
   - Parent: `data_source_id=24cec550-1950-47d4-b00f-16e0809faa54`
   - Properties:
     - `Actions/Tasks`: `Editorial Review - Weekly Drafts - YYYY-MM-DD`
     - `Status=Not started`
     - `date:Date:start` = run date
     - `date:Date:is_datetime=0`
     - `Project` must include the Content OS root page URL:
       - `https://www.notion.so/2445eb9488648013a9e7d9300346de18`
   - Content:
     - Link the newsletter and the three LinkedIn drafts.
     - Short "why these items" summary plus any reuse decisions.

10. Final report:
   - Run timestamp and timezone.
   - SOP compliance:
     - `pass` or `blocked`
     - proof task URL and proof age in days (when pass)
   - Created Content Library pages: title, URL, and key properties.
   - Updated Research Bank items: URL and fields changed.
   - Created Inbox task: URL and fields set.
   - Skipped candidates with reasons.
   - Any tool failures with exact error strings.

