#!/usr/bin/env python3
"""Analyze research links for concepts, implications, and business value."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from collections import Counter
from html import unescape
from pathlib import Path
from typing import Iterable


TECH_KEYWORDS = {
    "ai",
    "llm",
    "agent",
    "agentic",
    "model",
    "inference",
    "retrieval",
    "embedding",
    "vector",
    "prompt",
    "context",
    "orchestration",
    "pipeline",
    "latency",
    "accuracy",
    "hallucination",
    "evaluation",
    "fine-tuning",
    "memory",
}

BUSINESS_KEYWORDS = {
    "cost",
    "roi",
    "revenue",
    "margin",
    "value",
    "risk",
    "compliance",
    "productivity",
    "operations",
    "efficiency",
    "growth",
    "pricing",
    "budget",
    "quality",
}

RISK_KEYWORDS = {
    "risk",
    "failure",
    "limitation",
    "tradeoff",
    "constraint",
    "error",
    "hallucination",
    "bias",
    "security",
    "privacy",
}

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9\-]*")


def parse_links(research: dict) -> list[str]:
    links = []
    primary = str(research.get("Link", "")).strip()
    if primary:
        links.append(primary)

    raw_evidence = research.get("Evidence Links", "")
    if isinstance(raw_evidence, list):
        candidates = [str(v).strip() for v in raw_evidence]
    else:
        candidates = [c.strip() for c in re.split(r"[\n,]+", str(raw_evidence))]
    links.extend([c for c in candidates if c])

    deduped: list[str] = []
    seen = set()
    for link in links:
        if link not in seen:
            deduped.append(link)
            seen.add(link)
    return deduped


def fetch_url(url: str, timeout: int, max_chars: int) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; content-writing-os/1.0)"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    text = strip_html(raw)
    return text[:max_chars]


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = unescape(html)
    html = re.sub(r"\s+", " ", html).strip()
    return html


def split_sentences(text: str) -> list[str]:
    return [s.strip() for s in SENTENCE_SPLIT_RE.split(text) if len(s.strip()) > 20]


def score_sentence(sentence: str, keywords: set[str]) -> int:
    lowered = sentence.lower()
    return sum(1 for k in keywords if k in lowered)


def top_sentences(sentences: Iterable[str], keywords: set[str], limit: int) -> list[str]:
    scored = []
    for s in sentences:
        score = score_sentence(s, keywords)
        if score > 0:
            scored.append((score, len(s), s))
    scored.sort(key=lambda t: (-t[0], -t[1]))
    unique = []
    seen = set()
    for _, _, s in scored:
        key = s.lower()
        if key in seen:
            continue
        unique.append(s)
        seen.add(key)
        if len(unique) >= limit:
            break
    return unique


def extract_concepts(text: str, limit: int = 8) -> list[str]:
    words = [w.lower() for w in WORD_RE.findall(text)]
    counter = Counter(w for w in words if w in TECH_KEYWORDS)
    return [w for w, _ in counter.most_common(limit)]


def analyze_source(url: str, text: str) -> dict:
    sentences = split_sentences(text)
    concepts = extract_concepts(text)
    deep = top_sentences(sentences, TECH_KEYWORDS, 6)
    usefulness = top_sentences(sentences, BUSINESS_KEYWORDS, 5)
    implications = top_sentences(sentences, BUSINESS_KEYWORDS | RISK_KEYWORDS, 5)
    risks = top_sentences(sentences, RISK_KEYWORDS, 4)

    value_hypotheses = []
    for s in usefulness[:3]:
        value_hypotheses.append(
            f"If implemented correctly, this can improve business outcomes because: {s}"
        )

    actions = []
    if concepts:
        actions.append(
            f"Run a pilot focused on {concepts[0]} with explicit cost and quality tracking."
        )
    if len(concepts) > 1:
        actions.append(
            f"Define operating guardrails for {concepts[1]} before production rollout."
        )
    if not actions:
        actions.append("Run a scoped pilot and evaluate value vs risk before scaling.")

    confidence = "high" if len(deep) >= 4 and len(usefulness) >= 3 else "medium"
    if len(deep) < 2:
        confidence = "low"

    return {
        "url": url,
        "concepts": concepts,
        "deep_dive_explanation": deep,
        "business_usefulness": usefulness,
        "implications": implications,
        "value_hypotheses": value_hypotheses,
        "limits_and_risks": risks,
        "action_recommendations": actions,
        "confidence": confidence,
    }


def aggregate(sources: list[dict]) -> dict:
    concept_counter = Counter()
    for src in sources:
        concept_counter.update(src.get("concepts", []))

    recurring = [c for c, n in concept_counter.most_common(10) if n >= 2]
    top_value = []
    top_risks = []
    for src in sources:
        top_value.extend(src.get("business_usefulness", [])[:2])
        top_risks.extend(src.get("limits_and_risks", [])[:2])

    return {
        "recurring_concepts": recurring,
        "business_priority_signals": top_value[:6],
        "cross_source_risks": top_risks[:6],
        "decision_guidance": [
            "Start with a narrow use case and define measurable value targets.",
            "Track cost, speed, and quality weekly before scaling.",
            "Adopt controls for reliability and risk from day one.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze research links for deep business insights.")
    parser.add_argument("--research-json", required=True, help="Path to Research Bank JSON")
    parser.add_argument("--output", required=True, help="Output insights JSON path")
    parser.add_argument("--timeout", type=int, default=15, help="HTTP timeout seconds")
    parser.add_argument("--max-chars", type=int, default=30000, help="Max chars per source")
    args = parser.parse_args()

    research = json.loads(Path(args.research_json).read_text(encoding="utf-8-sig"))
    links = parse_links(research)
    if not links:
        raise SystemExit("No links found in research item.")

    analyzed = []
    failed = []
    for url in links:
        try:
            text = fetch_url(url, timeout=args.timeout, max_chars=args.max_chars)
            if not text:
                raise RuntimeError("empty content")
            analyzed.append(analyze_source(url, text))
        except Exception as exc:  # noqa: BLE001
            failed.append({"url": url, "error": str(exc)})

    output = {
        "research_title": research.get("Title", ""),
        "source_count": len(links),
        "analyzed_count": len(analyzed),
        "failed_sources": failed,
        "sources": analyzed,
        "cross_source": aggregate(analyzed) if analyzed else {},
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"wrote: {out_path}")
    if failed:
        print(f"failed_sources: {len(failed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
