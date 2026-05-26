#!/usr/bin/env python3
"""
Deterministically select a weekly Content OS draft batch from Research Bank candidates.

This script is designed to be called by a Codex automation run. It does not call Notion.
It takes a JSON list of candidate snapshots and returns a JSON selection plan:
- 1 newsletter (single item or 2-3 item bundle)
- 3 LinkedIn posts (1 research item per post)

Selection policy is intentionally simple and explainable:
- Prefer Backlog/Shortlisted.
- Avoid items used in the last 60 days (as indicated by selected_week_days_ago or used_within_60_days).
- Avoid Not Worthy / Rejected / missing required fields.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any


ALLOWED_STATUS_PREFERRED = {"Backlog", "Shortlisted"}
ALLOWED_STATUS_REUSE = {"Used", "Recycle Later"}
HARD_REJECT_STATUS = {"Not Worthy"}
HARD_REJECT_EDITORIAL = {"Rejected"}


@dataclass(frozen=True)
class Candidate:
    url: str
    title: str
    link: str
    why: str
    status: str | None
    editorial_decision: str | None
    score: float | None
    used_within_60_days: bool
    selected_week_days_ago: int | None
    thoroughness: str | None  # "deep" | "light" | None
    theme: str | None
    linkedin_strength: str | None  # "strong" | "weak" | None


def _norm_str(v: Any) -> str:
    return str(v or "").strip()


def _as_float(v: Any) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except Exception:
        return None


def parse_candidate(obj: dict) -> Candidate:
    url = _norm_str(obj.get("url"))
    title = _norm_str(obj.get("Title") or obj.get("title"))
    link = _norm_str(obj.get("Link") or obj.get("link"))
    why = _norm_str(obj.get("Why it matters") or obj.get("why"))
    status = _norm_str(obj.get("Status") or obj.get("status")) or None
    editorial = _norm_str(obj.get("Editorial Decision") or obj.get("editorial_decision")) or None
    score = _as_float(obj.get("Score") if "Score" in obj else obj.get("score"))

    used_within_60_days = bool(obj.get("used_within_60_days") is True)
    days_ago = obj.get("selected_week_days_ago")
    if isinstance(days_ago, str) and days_ago.strip().isdigit():
        days_ago = int(days_ago.strip())
    if not isinstance(days_ago, int):
        days_ago = None

    thoroughness = _norm_str(obj.get("thoroughness")) or None
    theme = _norm_str(obj.get("theme")) or None
    linkedin_strength = _norm_str(obj.get("linkedin_strength")) or None

    return Candidate(
        url=url,
        title=title,
        link=link,
        why=why,
        status=status,
        editorial_decision=editorial,
        score=score,
        used_within_60_days=used_within_60_days,
        selected_week_days_ago=days_ago,
        thoroughness=thoroughness,
        theme=theme,
        linkedin_strength=linkedin_strength,
    )


def required_fields_present(c: Candidate) -> bool:
    return bool(c.url and c.title and c.link and c.why)


def hard_reject_reason(c: Candidate) -> str | None:
    if not required_fields_present(c):
        return "missing required fields (Title/Link/Why it matters)"
    if c.status in HARD_REJECT_STATUS:
        return f"Status={c.status}"
    if c.editorial_decision in HARD_REJECT_EDITORIAL:
        return f"Editorial Decision={c.editorial_decision}"
    if c.used_within_60_days:
        return "used within last 60 days"
    if c.selected_week_days_ago is not None and c.selected_week_days_ago < 60:
        return "Selected Week within last 60 days"
    return None


def pool_rank(c: Candidate) -> int:
    """
    Lower is better.
    0: preferred pool (Backlog/Shortlisted)
    1: reuse pool (Used/Recycle Later)
    2: unknown status
    """
    if c.status in ALLOWED_STATUS_PREFERRED:
        return 0
    if c.status in ALLOWED_STATUS_REUSE:
        return 1
    return 2


def score_rank(c: Candidate) -> float:
    # Higher is better, but we sort ascending, so invert.
    # Missing score is treated as low.
    s = c.score if c.score is not None else -1.0
    return -s


def sort_key(c: Candidate) -> tuple:
    return (
        pool_rank(c),
        score_rank(c),
        (0 if (c.thoroughness or "").lower() == "deep" else 1),
        c.title.lower(),
    )


def pick_newsletter(eligible: list[Candidate]) -> tuple[list[Candidate], str]:
    """
    Returns (newsletter_items, mode).
    mode is "single" or "bundle".
    """
    if not eligible:
        return ([], "single")

    # Prefer a single "deep" item for the newsletter if available.
    deep = [c for c in eligible if (c.thoroughness or "").lower() == "deep"]
    if deep:
        deep_sorted = sorted(deep, key=sort_key)
        return ([deep_sorted[0]], "single")

    # Otherwise bundle 2-3 related items.
    # If a theme is provided, bundle within the best theme; otherwise just take the top 2.
    by_theme: dict[str, list[Candidate]] = {}
    for c in eligible:
        t = (c.theme or "").strip()
        if t:
            by_theme.setdefault(t, []).append(c)

    if by_theme:
        best_theme = None
        best_list: list[Candidate] = []
        for t, items in by_theme.items():
            items_sorted = sorted(items, key=sort_key)
            if not best_theme or len(items_sorted) > len(best_list):
                best_theme = t
                best_list = items_sorted
            elif len(items_sorted) == len(best_list) and items_sorted and best_list:
                # tie-break on top candidate rank
                if sort_key(items_sorted[0]) < sort_key(best_list[0]):
                    best_theme = t
                    best_list = items_sorted
        picked = best_list[:3] if len(best_list) >= 3 else best_list[:2]
        return (picked, "bundle")

    eligible_sorted = sorted(eligible, key=sort_key)
    picked = eligible_sorted[:3] if len(eligible_sorted) >= 3 else eligible_sorted[:2]
    return (picked, "bundle")


def pick_linkedin(
    eligible: list[Candidate],
    newsletter_items: list[Candidate],
) -> list[dict]:
    """
    Returns list of 3 dicts: {research_url, parent_newsletter}
    Overlap when strong: allow a newsletter item to be used for LinkedIn if linkedin_strength == "strong".
    """
    newsletter_urls = {c.url for c in newsletter_items}
    strong_overlap = [c for c in newsletter_items if (c.linkedin_strength or "").lower() == "strong"]

    chosen: list[Candidate] = []
    if strong_overlap:
        # Pick at most one overlap item to avoid over-indexing.
        chosen.append(sorted(strong_overlap, key=sort_key)[0])

    remaining = [c for c in eligible if c.url not in {x.url for x in chosen}]
    remaining_sorted = sorted(remaining, key=sort_key)

    for c in remaining_sorted:
        if len(chosen) >= 3:
            break
        chosen.append(c)

    plan: list[dict] = []
    for c in chosen[:3]:
        plan.append(
            {
                "research_url": c.url,
                "parent_newsletter": (c.url in newsletter_urls),
            }
        )
    return plan


def build_selection(candidates: list[Candidate]) -> dict:
    skips: list[dict] = []
    eligible: list[Candidate] = []
    for c in candidates:
        reason = hard_reject_reason(c)
        if reason:
            skips.append({"research_url": c.url or "(missing url)", "reason": reason})
            continue
        eligible.append(c)

    eligible_sorted = sorted(eligible, key=sort_key)
    newsletter_items, mode = pick_newsletter(eligible_sorted)

    # Ensure LinkedIn selection can be formed (3 items).
    linkedin_plan = pick_linkedin(eligible_sorted, newsletter_items)
    if len(linkedin_plan) < 3:
        return {
            "error": "insufficient eligible items to form 3 LinkedIn posts",
            "newsletter": {"mode": mode, "research_urls": [c.url for c in newsletter_items], "lead_research_url": (newsletter_items[0].url if newsletter_items else None)},
            "linkedin": linkedin_plan,
            "research_updates": [],
            "skips": skips,
        }

    used_urls = set([c.url for c in newsletter_items] + [x["research_url"] for x in linkedin_plan])
    updates = [{"research_url": u, "set_status": "Used"} for u in sorted(used_urls)]

    return {
        "newsletter": {
            "mode": mode,
            "research_urls": [c.url for c in newsletter_items],
            "lead_research_url": (newsletter_items[0].url if newsletter_items else None),
        },
        "linkedin": linkedin_plan,
        "research_updates": updates,
        "skips": skips,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Select weekly Content OS draft batch.")
    parser.add_argument("--input", required=True, help="Path to JSON candidates file")
    parser.add_argument("--output", help="Optional output path for selection JSON (defaults to stdout)")
    args = parser.parse_args()

    raw = json.loads(open(args.input, "r", encoding="utf-8-sig").read())
    if not isinstance(raw, list):
        raise SystemExit("Input JSON must be a list of candidate objects.")

    candidates = [parse_candidate(obj) for obj in raw if isinstance(obj, dict)]
    result = build_selection(candidates)

    encoded = json.dumps(result, indent=2, ensure_ascii=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(encoded + "\n")
    else:
        print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

