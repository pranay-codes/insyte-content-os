#!/usr/bin/env python3
"""Create a proposal to update style references from mined metrics."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_metrics(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_changes(metrics: dict) -> list[str]:
    changes: list[str] = []
    avg_sentence = metrics.get("avg_sentence_words", 0)
    avg_numeric = metrics.get("avg_numeric_sentence_ratio", 0)
    recurring_headings = metrics.get("recurring_headings", [])
    recurring_cta = metrics.get("recurring_cta_phrases", [])

    if avg_sentence > 26:
        changes.append(
            "Reduce average sentence length in long-form drafts to improve business readability."
        )
    if avg_sentence < 14:
        changes.append(
            "Allow more explanatory depth in long-form sections to keep technical rigor."
        )
    if avg_numeric < 0.15:
        changes.append(
            "Increase quantified examples and measurable framing in value sections."
        )
    if recurring_headings:
        changes.append(
            "Promote recurring section headings into preferred structure: "
            + ", ".join(recurring_headings[:5])
        )
    if recurring_cta:
        changes.append(
            "Standardize CTA language around recurring high-signal phrases: "
            + ", ".join(recurring_cta[:4])
        )

    if not changes:
        changes.append("No high-confidence style deltas detected in this cycle.")
    return changes


def render_proposal(metrics: dict, min_docs: int) -> str:
    doc_count = int(metrics.get("doc_count", 0))
    proposal_id = f"style-proposal-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    created_at = utc_now()

    if doc_count < min_docs:
        return f"""# Style Update Proposal

Proposal ID: `{proposal_id}`
Created At: `{created_at}`
Proposal Status: `Proposed`

## Summary
Insufficient signal to propose a style update.

## Metrics Snapshot
- Documents analyzed: {doc_count}
- Required minimum: {min_docs}

## Decision
Do not update style references in this cycle.
"""

    changes = build_changes(metrics)
    lines = "\n".join(f"{i + 1}. {item}" for i, item in enumerate(changes))
    headings = ", ".join(metrics.get("recurring_headings", [])[:8]) or "None"
    transitions = ", ".join(metrics.get("recurring_transitions", [])[:8]) or "None"
    cta = ", ".join(metrics.get("recurring_cta_phrases", [])[:8]) or "None"
    avg_sentence = metrics.get("avg_sentence_words", 0)
    avg_paragraph = metrics.get("avg_paragraph_words", 0)
    avg_numeric = metrics.get("avg_numeric_sentence_ratio", 0)

    return f"""# Style Update Proposal

Proposal ID: `{proposal_id}`
Created At: `{created_at}`
Proposal Status: `Proposed`

## Summary
Biweekly proposal generated from published content sample.

## Metrics Snapshot
- Documents analyzed: {doc_count}
- Average sentence length: {avg_sentence}
- Average paragraph length: {avg_paragraph}
- Numeric sentence ratio: {avg_numeric}
- Recurring headings: {headings}
- Recurring transitions: {transitions}
- Recurring CTA phrases: {cta}

## Proposed Changes
{lines}

## Accepted Changes
Fill this section only when approving the proposal.

1. {{accepted_change_1}}
2. {{accepted_change_2}}

## Approval
- Decision: `Approved | Rejected | Needs edits`
- Reviewer:
- Reviewed At:
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create style update proposal markdown.")
    parser.add_argument("--metrics", required=True, help="Path to style metrics JSON")
    parser.add_argument("--output", required=True, help="Output proposal markdown path")
    parser.add_argument(
        "--min-docs", type=int, default=6, help="Minimum published docs required"
    )
    parser.add_argument(
        "--style-live",
        help="Path to style_live.md (accepted for compatibility; not mutated by this script)",
    )
    args = parser.parse_args()

    metrics_path = Path(args.metrics)
    output_path = Path(args.output)
    metrics = load_metrics(metrics_path)
    proposal = render_proposal(metrics, args.min_docs)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(proposal.strip() + "\n", encoding="utf-8")
    print(f"wrote: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
