# POLICY.md - Notion Access Policy for insyte-content-os

## Purpose
Define the allowed Notion access boundary for this repository.

## Authoritative Scope

Only these Notion objects are in scope:

- Content OS root page: `https://www.notion.so/2445eb9488648013a9e7d9300346de18`
- Tasks section database (View of Inbox): `https://www.notion.so/2445eb94886480159d82da7cf00ff99c`
- Tasks data source (Inbox): `collection://24cec550-1950-47d4-b00f-16e0809faa54`
- Research Bank database: `https://www.notion.so/2f45eb948864801180bafa69e23150f7`
- Research Bank data source: `collection://2f45eb94-8864-801b-a248-000b106b02c4`
- Content Library database: `https://www.notion.so/2f45eb948864803eb0a3d2896d5ada35`
- Content Library data source: `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`

Any Notion page, database, or data source not listed above is out of scope.

## Allowed Capabilities

1. Read Content OS and in-scope subpages/subdatabases.
2. Read/write task rows in Inbox.
3. Read/write items in Research Bank.
4. Read/write items in Content Library.

## Prohibited Actions

1. Read/write outside the in-scope objects.
2. Workspace-wide edits not restricted to this scope.
3. Schema/view changes unless explicitly requested in the current turn.
4. Move/trash/archive actions outside the in-scope objects.

## Required Validation Before Writes

1. Run `notion-fetch` on the target.
2. Confirm target URL/ID is in the authoritative scope list.
3. If validation fails, stop and ask for user confirmation.


## Enforcement

`AGENTS.md` in this repo must enforce this policy for every Notion action.
