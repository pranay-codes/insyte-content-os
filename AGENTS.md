# AGENTS.md - insyte-content-os Notion Scope Policy

## Objective
Constrain all Notion operations in this repository to the Content OS system only.

## Policy Enforcement

`POLICY.md` is mandatory and must be enforced on every Notion action.

1. Read `POLICY.md` first for scope and constraints.
2. If this file and `POLICY.md` differ, follow the stricter rule.
3. Never execute a Notion read/write that violates `POLICY.md`.

## Allowed Scope (Only)

- Content OS root page: `https://www.notion.so/2445eb9488648013a9e7d9300346de18`
- Tasks section database (View of Inbox): `https://www.notion.so/2445eb94886480159d82da7cf00ff99c`
- Tasks data source (Inbox): `collection://24cec550-1950-47d4-b00f-16e0809faa54`
- Research Bank database: `https://www.notion.so/2f45eb948864801180bafa69e23150f7`
- Research Bank data source: `collection://2f45eb94-8864-801b-a248-000b106b02c4`
- Content Library database: `https://www.notion.so/2f45eb948864803eb0a3d2896d5ada35`
- Content Library data source: `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`

No other Notion pages, databases, or data sources may be read or modified.

## Allowed Operations

1. Read Content OS and its direct subpages/subdatabases inside the allowed scope.
2. Read/write task rows in Inbox (Tasks section).
3. Read/write items in Research Bank.
4. Read/write items in Content Library.

## Hard Guardrails

1. Before any write, run `notion-fetch` on the target.
2. Verify the target is one of the allowlisted IDs/URLs above.
3. If not allowlisted, stop and ask the user.
4. Do not perform schema changes (database properties/views) unless explicitly requested in the current turn.
5. Do not run workspace-wide edits or move/trash operations outside the allowed scope.

## Weekly SOP Enforcement

Before any write to Tasks, Research Bank, or Content Library:

1. Find the most recent Inbox task titled `Editorial Review - Weekly Shortlist`.
2. Verify both conditions:
- `Status=Done`
- completion age is less than or equal to 7 days
3. If both conditions pass, proceed with write (`SOP compliance: pass`).
4. If either condition fails:
- warn the user with: `Weekly SOP compliance is missing (no completed "Editorial Review - Weekly Shortlist" in the last 7 days). Confirm override to continue this write.`
- ask for explicit user confirmation before continuing
- if confirmed, proceed only for that turn and mark response as `SOP compliance: override`
- if not confirmed, do not perform the write

## Task Handling Rules (Inbox)

- Create tasks as pages in `collection://24cec550-1950-47d4-b00f-16e0809faa54`.
- Use exact property names from schema.
- Minimum create payload:
  - `Actions/Tasks` (title)
  - `Status` (default `Not started`)
  - `Project` includes `https://www.notion.so/2445eb9488648013a9e7d9300346de18`
- Prefer row-level database updates; avoid replacing entire page content for task management.

## Research Bank Rules

- Add/update only in `collection://2f45eb94-8864-801b-a248-000b106b02c4`.
- Title is required. Optional fields include `Link`, `Research Type`, `Proposed Section`, `Horizon`, `Why it matters`, `Notes`, `Status`, `Owner`.

## Content Library Rules

- Add/update only in `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`.
- Title is required. Optional fields include `Content Type`, `Status`, `Channel`, `Owner`, `Final Link`, `Published Date`, `Primary Research`, `Research`.

## Verification Standard

- Never claim a Notion write succeeded without tool success output.
- Report touched object URL/ID and fields changed after each write.
- Report `SOP compliance: pass|override` after each write.
- Report `Proof task URL` after each write (or `N/A` if override).
- Report `Proof age` in days after each write.
