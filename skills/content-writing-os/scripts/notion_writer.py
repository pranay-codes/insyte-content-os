#!/usr/bin/env python3
"""Build deterministic Notion payloads for Content Library draft creation."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass


CONTENT_LIBRARY_DATA_SOURCE = "2f45eb94-8864-8040-aa3a-000b4dc54386"


@dataclass
class Piece:
    title: str
    asset_role: str
    content_type: str
    parent_asset: str | None = None


def build_piece_properties(
    piece: Piece,
    research_url: str,
    publish_week: str | None,
    owner: str | None,
    status: str,
) -> dict:
    props = {
        "Title": piece.title,
        "Asset Role": piece.asset_role,
        "Content Type": piece.content_type,
        "Status": status,
        "QA Ready": "__NO__",
        "Primary Research": json.dumps([research_url]),
    }
    if publish_week:
        props["date:Publish Week:start"] = publish_week
        props["date:Publish Week:is_datetime"] = 0
    if owner:
        props["Owner"] = owner
    if piece.parent_asset:
        props["Parent Asset"] = json.dumps([piece.parent_asset])
    return props


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Notion payload for content set creation.")
    parser.add_argument("--research-url", required=True, help="Research Bank page URL")
    parser.add_argument("--research-title", required=True, help="Research item title")
    parser.add_argument("--publish-week", help="Week start date YYYY-MM-DD")
    parser.add_argument("--owner", help="Owner name")
    parser.add_argument("--status", default="Not started", help="Initial status")
    parser.add_argument(
        "--output",
        help="Optional output JSON file path. If omitted, prints to stdout.",
    )
    args = parser.parse_args()

    base = args.research_title.strip()
    newsletter_title = f"{base} - Newsletter"
    pieces = [
        Piece(f"{base} - Medium Deep Dive", "Core", "Blog/Medium"),
        Piece(newsletter_title, "Core", "Newsletter Issue"),
        Piece(f"{base} - LinkedIn A", "Derivative", "Linkedin Post", newsletter_title),
        Piece(f"{base} - LinkedIn B", "Derivative", "Linkedin Post", newsletter_title),
    ]

    pages = [
        {
            "properties": build_piece_properties(
                piece=p,
                research_url=args.research_url,
                publish_week=args.publish_week,
                owner=args.owner,
                status=args.status,
            )
        }
        for p in pieces
    ]

    payload = {
        "parent": {"data_source_id": CONTENT_LIBRARY_DATA_SOURCE},
        "pages": pages,
    }

    encoded = json.dumps(payload, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(encoded + "\n")
    else:
        print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
