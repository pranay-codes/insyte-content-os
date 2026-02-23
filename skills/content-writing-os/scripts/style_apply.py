#!/usr/bin/env python3
"""Apply an approved style proposal to style_live and changelog."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


STATUS_RE = re.compile(r"^Proposal Status:\s*`([^`]+)`\s*$", re.MULTILINE)
VERSION_RE = re.compile(r"^(Style-Version:\s*)(\d+)\.(\d+)\.(\d+)\s*$", re.MULTILINE)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_accepted_changes(proposal_text: str) -> list[str]:
    section_header = "## Accepted Changes"
    if section_header not in proposal_text:
        return []
    tail = proposal_text.split(section_header, 1)[1]
    stop_markers = ["## Approval", "\n## "]
    cut = len(tail)
    for marker in stop_markers:
        idx = tail.find(marker)
        if idx != -1:
            cut = min(cut, idx)
    section = tail[:cut]

    changes: list[str] = []
    for line in section.splitlines():
        striped = line.strip()
        if re.match(r"^\d+\.\s+", striped):
            value = re.sub(r"^\d+\.\s+", "", striped).strip()
            if value and not value.startswith("{"):
                changes.append(value)
    return changes


def bump_patch_version(style_text: str) -> tuple[str, str]:
    match = VERSION_RE.search(style_text)
    if not match:
        raise ValueError("Could not find Style-Version in style_live.md")
    major = int(match.group(2))
    minor = int(match.group(3))
    patch = int(match.group(4)) + 1
    new_version = f"{major}.{minor}.{patch}"
    replaced = VERSION_RE.sub(rf"\g<1>{new_version}", style_text, count=1)
    return replaced, new_version


def append_style_update(style_text: str, changes: list[str], version: str) -> str:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(changes))
    block = (
        f"\n## Accepted Adaptations - {date} (v{version})\n\n"
        f"{lines}\n"
    )
    return style_text.rstrip() + block + "\n"


def append_changelog(changelog_text: str, changes: list[str], version: str) -> str:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(changes))
    entry = f"\n## {date} - v{version}\n\n{lines}\n"
    return changelog_text.rstrip() + entry + "\n"


def mark_proposal_applied(proposal_text: str) -> str:
    return STATUS_RE.sub("Proposal Status: `Applied`", proposal_text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply approved style update proposal.")
    parser.add_argument("--proposal", required=True, help="Proposal markdown path")
    parser.add_argument("--style-live", required=True, help="Path to style_live.md")
    parser.add_argument("--changelog", required=True, help="Path to style_changelog.md")
    args = parser.parse_args()

    proposal_path = Path(args.proposal)
    style_path = Path(args.style_live)
    changelog_path = Path(args.changelog)

    proposal_text = proposal_path.read_text(encoding="utf-8")
    status_match = STATUS_RE.search(proposal_text)
    if not status_match:
        raise SystemExit("Proposal status not found.")
    if status_match.group(1).strip().lower() != "approved":
        raise SystemExit("Proposal is not approved. Set `Proposal Status: `Approved`` first.")

    changes = extract_accepted_changes(proposal_text)
    if not changes:
        raise SystemExit("No accepted changes found in proposal.")

    style_text = style_path.read_text(encoding="utf-8")
    style_text, new_version = bump_patch_version(style_text)
    style_text = append_style_update(style_text, changes, new_version)
    style_path.write_text(style_text, encoding="utf-8")

    changelog_text = changelog_path.read_text(encoding="utf-8")
    changelog_text = append_changelog(changelog_text, changes, new_version)
    changelog_path.write_text(changelog_text, encoding="utf-8")

    proposal_text = mark_proposal_applied(proposal_text)
    proposal_text = proposal_text.rstrip() + f"\n\nApplied At: `{utc_now()}`\n"
    proposal_path.write_text(proposal_text, encoding="utf-8")

    print(f"applied version: {new_version}")
    print(f"updated: {style_path}")
    print(f"updated: {changelog_path}")
    print(f"updated: {proposal_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
