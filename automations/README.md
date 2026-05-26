# Automations

This folder contains repo-local operating contracts for Codex automations.

## Daily Content OS Research Intake

Prompt file:
- `automations/daily-content-os-research-intake.md`

Config file:
- `config/newsletter-labels.txt`

Schedule:
- Daily at `08:00 Pacific/Auckland`

Purpose:
- Read the newest 10 total Gmail newsletter emails from the configured labels.
- Extract practical AI resources.
- Add only high-value, non-duplicate items to the allowlisted Content OS Research Bank.

Safety:
- The automation must read `AGENTS.md` and `POLICY.md` every run.
- Research Bank writes are allowed only inside `collection://2f45eb94-8864-801b-a248-000b106b02c4`.
- The weekly SOP proof task must be `Done` within the last 7 days.
- Unattended runs stop instead of asking for SOP override.

## Weekly Content OS Draft Production

Prompt file:
- `automations/weekly-content-os-draft-production.md`

Schedule:
- Weekly on Tuesday at `08:00 Pacific/Auckland`

Purpose:
- Select eligible Research Bank items.
- Create 1 newsletter draft and 3 LinkedIn draft posts in Content Library.
- Mark selected research as used.
- Create 1 Inbox review task linking the weekly draft batch.

Safety:
- The automation must read `AGENTS.md` and `POLICY.md` every run.
- All Notion reads/writes must remain inside the allowlisted Content OS objects.
- The weekly SOP proof task must be `Done` within the last 7 days.
- Unattended runs stop instead of asking for SOP override.
