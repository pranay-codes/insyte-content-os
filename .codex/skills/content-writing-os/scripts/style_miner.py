#!/usr/bin/env python3
"""Extract recurring style and format signals from published markdown content."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
WORD_RE = re.compile(r"[A-Za-z0-9']+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
TRANSITIONS = [
    "therefore",
    "however",
    "in practice",
    "in short",
    "as a result",
    "for example",
]
CTA_PHRASES = [
    "next step",
    "start with",
    "action",
    "decide",
    "pilot",
    "measure",
]


@dataclass
class DocMetrics:
    path: str
    sentence_count: int
    avg_sentence_words: float
    avg_paragraph_words: float
    numeric_sentence_ratio: float
    headings: list[str]
    transitions: dict[str, int]
    cta_hits: dict[str, int]


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def sentence_words(sentence: str) -> int:
    return len(words(sentence))


def mine_doc(path: Path) -> DocMetrics:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    sentences = [s.strip() for s in SENTENCE_RE.split(text) if s.strip()]
    sentence_lengths = [sentence_words(s) for s in sentences if sentence_words(s) > 0]
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    paragraph_lengths = [len(words(p)) for p in paragraphs if len(words(p)) > 0]

    numeric_sentences = 0
    for sentence in sentences:
        if re.search(r"\d", sentence):
            numeric_sentences += 1

    heading_values = [m.group(2).strip() for m in HEADING_RE.finditer(text)]
    transition_hits = {t: lowered.count(t) for t in TRANSITIONS}
    cta_hits = {c: lowered.count(c) for c in CTA_PHRASES}

    avg_sentence = (
        sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0.0
    )
    avg_paragraph = (
        sum(paragraph_lengths) / len(paragraph_lengths) if paragraph_lengths else 0.0
    )
    ratio = (numeric_sentences / len(sentences)) if sentences else 0.0

    return DocMetrics(
        path=str(path),
        sentence_count=len(sentences),
        avg_sentence_words=round(avg_sentence, 2),
        avg_paragraph_words=round(avg_paragraph, 2),
        numeric_sentence_ratio=round(ratio, 3),
        headings=heading_values,
        transitions=transition_hits,
        cta_hits=cta_hits,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Mine style metrics from markdown files.")
    parser.add_argument("--input-dir", required=True, help="Directory containing markdown files")
    parser.add_argument("--output", required=True, help="Output JSON file")
    parser.add_argument(
        "--recurrence-threshold",
        type=float,
        default=0.66,
        help="Fraction of docs where a pattern must appear to be recurring",
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    files = sorted(input_dir.glob("*.md"))
    if not files:
        raise SystemExit("No markdown files found in input directory.")

    docs = [mine_doc(f) for f in files]
    doc_count = len(docs)
    threshold_count = max(1, int(doc_count * args.recurrence_threshold))

    heading_counter = Counter()
    transition_docs = Counter()
    cta_docs = Counter()
    for doc in docs:
        for heading in set(doc.headings):
            heading_counter[heading] += 1
        for name, hits in doc.transitions.items():
            if hits > 0:
                transition_docs[name] += 1
        for name, hits in doc.cta_hits.items():
            if hits > 0:
                cta_docs[name] += 1

    recurring_headings = [
        h for h, count in heading_counter.items() if count >= threshold_count
    ]
    recurring_transitions = [
        t for t, count in transition_docs.items() if count >= threshold_count
    ]
    recurring_cta = [c for c, count in cta_docs.items() if count >= threshold_count]

    summary = {
        "doc_count": doc_count,
        "threshold_count": threshold_count,
        "avg_sentence_words": round(
            sum(d.avg_sentence_words for d in docs) / doc_count, 2
        ),
        "avg_paragraph_words": round(
            sum(d.avg_paragraph_words for d in docs) / doc_count, 2
        ),
        "avg_numeric_sentence_ratio": round(
            sum(d.numeric_sentence_ratio for d in docs) / doc_count, 3
        ),
        "recurring_headings": sorted(recurring_headings),
        "recurring_transitions": sorted(recurring_transitions),
        "recurring_cta_phrases": sorted(recurring_cta),
        "documents": [d.__dict__ for d in docs],
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"wrote: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
