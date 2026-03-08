#!/usr/bin/env python3
"""Generate draft markdown files from one Research Bank item."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_FIELDS = ("Title", "Link", "Why it matters")


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    return cleaned.strip("-") or "research-item"


def parse_evidence_links(raw_value) -> list[str]:
    if raw_value is None:
        return []
    if isinstance(raw_value, list):
        return [str(v).strip() for v in raw_value if str(v).strip()]
    chunks = re.split(r"[\n,]+", str(raw_value))
    return [c.strip() for c in chunks if c.strip()]


def require_fields(payload: dict) -> None:
    missing = [f for f in REQUIRED_FIELDS if not str(payload.get(f, "")).strip()]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def load_insights(path: str | None) -> dict:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def pick_lines(insights: dict, key: str, limit: int) -> list[str]:
    lines: list[str] = []
    for src in insights.get("sources", []):
        for item in src.get(key, []):
            item = str(item).strip()
            if item and item not in lines:
                lines.append(item)
                if len(lines) >= limit:
                    return lines
    return lines


def pick_concepts(insights: dict, limit: int) -> list[str]:
    values: list[str] = []
    for src in insights.get("sources", []):
        for concept in src.get("concepts", []):
            concept = str(concept).strip()
            if concept and concept not in values:
                values.append(concept)
                if len(values) >= limit:
                    return values
    return values


def pick_recurring_concepts(insights: dict, limit: int) -> list[str]:
    values = []
    cross = insights.get("cross_source", {})
    for concept in cross.get("recurring_concepts", []):
        concept = str(concept).strip()
        if concept and concept not in values:
            values.append(concept)
            if len(values) >= limit:
                return values
    return values


def build_searchable_key_phrases(payload: dict, insights: dict) -> list[str]:
    title = payload.get("Title", "AI")
    concepts = pick_concepts(insights, 6)
    recurring = pick_recurring_concepts(insights, 6)

    candidates: list[str] = []
    for concept in concepts + recurring:
        phrase = f"{concept} for business owners"
        phrase = " ".join(phrase.split())
        if phrase not in candidates:
            candidates.append(phrase)

    fallback = [
        f"{title} business impact",
        "AI fundamentals for business owners",
        "LLM fundamentals for business",
        "Agentic AI for business operations",
        "AI value and ROI framework",
        "AI risk and governance for SMEs",
        "Technical AI concepts in plain language",
    ]

    for phrase in fallback:
        if phrase not in candidates:
            candidates.append(phrase)

    return candidates[:5]


def bullet_block(items: list[str], fallback: list[str], limit: int) -> str:
    picked = items[:limit] if items else fallback[:limit]
    return "\n".join(f"{i + 1}. {v}" for i, v in enumerate(picked))


def build_medium(payload: dict, evidence: list[str], insights: dict) -> str:
    title = payload["Title"]
    link = payload["Link"]
    why = payload["Why it matters"]
    hook = payload.get("Hook", "")
    angle = payload.get("Content Angle", "")
    source_1 = evidence[0] if evidence else link
    source_2 = evidence[1] if len(evidence) > 1 else link
    source_3 = evidence[2] if len(evidence) > 2 else link

    concepts = pick_concepts(insights, 6)
    deep = pick_lines(insights, "deep_dive_explanation", 6)
    usefulness = pick_lines(insights, "business_usefulness", 5)
    implications = pick_lines(insights, "implications", 5)
    value = pick_lines(insights, "value_hypotheses", 4)
    risks = pick_lines(insights, "limits_and_risks", 4)
    actions = pick_lines(insights, "action_recommendations", 4)

    concept_text = (
        ", ".join(concepts)
        if concepts
        else "Define AI, LLM, and Agentic AI concepts clearly for business owners."
    )

    return f"""# {title} - Deep Dive

## Why this matters now
{why}

## Core concepts in plain language
{angle or concept_text}

## How it works (technical deep dive)
{bullet_block(deep, [
    "Explain architecture and data flow.",
    "Explain operational tradeoffs and failure modes.",
    "Explain implementation constraints.",
], 6)}

## What this means for business owners
{bullet_block(usefulness, [
    "Translate technical mechanics into business decisions.",
    "Connect architecture choices to cost, speed, quality, and risk.",
], 5)}

## Value achieved and value at risk
{bullet_block(value, [
    "Define near-term value with explicit assumptions.",
    "Define medium-term scale value and constraints.",
], 4)}

## Implications and decision guidance
{bullet_block(implications, [
    "Clarify budget and operating model implications.",
    "Clarify adoption sequence and capability requirements.",
], 5)}

## Risks and limits
{bullet_block(risks, [
    "State failure conditions and mitigation options.",
    "State where recommendations do not generalize.",
], 4)}

## Next actions
{hook or "Define one immediate next step for decision makers."}

{bullet_block(actions, [
    "Start with a scoped pilot and clear success metrics.",
    "Measure cost, latency, and quality before scaling.",
], 4)}

## Evidence Map
- claim: Core mechanism and assumptions | source: {source_1}
- claim: Cost or performance implication | source: {source_2}
- claim: Value realization path | source: {source_3}
"""


def build_newsletter(payload: dict, evidence: list[str], insights: dict) -> str:
    title = payload["Title"]
    link = payload["Link"]
    why = payload["Why it matters"]
    hook = str(payload.get("Hook", "")).strip()
    angle = str(payload.get("Content Angle", "")).strip()
    source_1 = evidence[0] if evidence else link
    source_2 = evidence[1] if len(evidence) > 1 else link

    deep = pick_lines(insights, "deep_dive_explanation", 3)
    value = pick_lines(insights, "business_usefulness", 3)
    implications = pick_lines(insights, "implications", 3)
    key_phrases = build_searchable_key_phrases(payload, insights)
    subheading = (
        angle
        if angle
        else "A technical concept explained clearly for operators and business owners."
    )
    hook_line = (
        hook
        if hook
        else "If you cannot explain the business value of your AI system in plain language, you are not ready to scale it."
    )

    return f"""# {title} - Newsletter

## Subheading
{subheading}

## Hook
{hook_line}

## Searchable Key Phrases
1. {key_phrases[0]}
2. {key_phrases[1]}
3. {key_phrases[2]}
4. {key_phrases[3]}
5. {key_phrases[4]}

## This week's insight
{why}

## Technical concept, clearly explained
{bullet_block(deep, [
    "Explain one core concept in business-accessible language with technical accuracy.",
], 3)}

## Why business owners should care
{bullet_block(value, [
    "Translate concept into financial and operational implications.",
], 3)}

## What it means in practice
{bullet_block(implications, [
    "State the implementation implication for budget, team, and process.",
], 3)}

## Action checklist
1. Identify current baseline
2. Choose one pilot use case
3. Track value and risk from week one

## CTA
Decide one next implementation step and assign an owner.

## Evidence Map
- claim: Concept framing and context | source: {source_1}
- claim: Business impact or benchmark | source: {source_2}
"""


def build_linkedin(payload: dict, evidence: list[str], insights: dict, variant: str) -> str:
    title = payload["Title"]
    link = payload["Link"]
    source_1 = evidence[0] if evidence else link
    deep = pick_lines(insights, "deep_dive_explanation", 2)
    value = pick_lines(insights, "business_usefulness", 2)
    actions = pick_lines(insights, "action_recommendations", 1)

    angle = (
        "Business-first angle: outcomes and operating impact."
        if variant == "a"
        else "Execution-first angle: implementation and tradeoffs."
    )
    technical_line = deep[0] if deep else "One technical idea explained clearly."
    value_line = value[0] if value else "Tie the concept to cost, speed, quality, or risk."
    action_line = actions[0] if actions else "Run a small pilot and measure value weekly."

    return f"""{title}

{angle}

{technical_line}

Business implication:
{value_line}

Action:
{action_line}

Evidence:
- core claim -> {source_1}
"""


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose draft markdown files.")
    parser.add_argument("--research-json", required=True, help="Path to research item JSON")
    parser.add_argument("--output-dir", required=True, help="Output directory for draft files")
    parser.add_argument("--prefix", help="Filename prefix override")
    parser.add_argument(
        "--insights-json",
        help="Optional link intelligence JSON from scripts/link_intelligence.py",
    )
    args = parser.parse_args()

    payload_path = Path(args.research_json)
    output_dir = Path(args.output_dir)
    payload = json.loads(payload_path.read_text(encoding="utf-8-sig"))
    require_fields(payload)
    evidence = parse_evidence_links(payload.get("Evidence Links"))
    insights = load_insights(args.insights_json)

    prefix = args.prefix or slugify(payload["Title"])
    files = {
        f"{prefix}-medium.md": build_medium(payload, evidence, insights),
        f"{prefix}-newsletter.md": build_newsletter(payload, evidence, insights),
        f"{prefix}-linkedin-a.md": build_linkedin(payload, evidence, insights, "a"),
        f"{prefix}-linkedin-b.md": build_linkedin(payload, evidence, insights, "b"),
    }

    for filename, content in files.items():
        write_file(output_dir / filename, content)
        print(f"wrote: {output_dir / filename}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
