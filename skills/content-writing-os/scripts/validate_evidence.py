#!/usr/bin/env python3
"""Validate that draft files contain evidence mapping."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EVIDENCE_SECTION_RE = re.compile(r"(^## Evidence Map$|^Evidence:$)", re.MULTILINE)
SOURCE_RE = re.compile(r"https?://")


def validate_file(path: Path, min_entries: int) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    if not EVIDENCE_SECTION_RE.search(text):
        return False, "missing evidence section"

    evidence_lines = []
    for line in text.splitlines():
        striped = line.strip()
        if "source:" in striped.lower() or "->" in striped:
            evidence_lines.append(striped)

    if len(evidence_lines) < min_entries:
        return False, f"only {len(evidence_lines)} evidence entries (min {min_entries})"

    for line in evidence_lines:
        if not SOURCE_RE.search(line):
            return False, f"evidence line missing URL: {line}"

    return True, f"{len(evidence_lines)} evidence entries"


def expand_inputs(raw_inputs: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in raw_inputs:
        p = Path(raw)
        if p.is_dir():
            paths.extend(sorted(p.glob("*.md")))
        else:
            paths.append(p)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate evidence mapping in drafts.")
    parser.add_argument(
        "--input",
        nargs="+",
        required=True,
        help="One or more markdown files or directories",
    )
    parser.add_argument("--min-entries", type=int, default=1, help="Minimum evidence lines")
    args = parser.parse_args()

    files = expand_inputs(args.input)
    if not files:
        print("No markdown files found.")
        return 1

    failures = 0
    for file_path in files:
        ok, msg = validate_file(file_path, args.min_entries)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {file_path}: {msg}")
        if not ok:
            failures += 1

    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
