#!/usr/bin/env python3
"""
Build scripts/lesson_nav_map.json: for every level, the ordered list of its
own lessons (slug, title), used by build_lesson.py to render Previous/Next
navigation and the "Lesson N of M" counter on every generated lesson page.

Simpler than the English course's equivalent script: every level here
(including A1) goes through the curriculum/*.json pipeline, and there is
no Test-Yourself-anchor cross-referencing to do (see build_test_yourself.py
for how this course's per-level review pages are generated instead — from
the curriculum data directly, not by hand-authored anchor matching).

Usage:
    python3 scripts/build_nav_map.py
"""
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]


def build_level(level_slug: str) -> list:
    idx = json.loads((REPO_ROOT / "curriculum" / "index.json").read_text(encoding="utf-8"))
    level_key = level_slug.upper()
    units = idx["levels"][level_key]["units"]
    lessons = [entry for unit in units for entry in unit["lessons"]]
    out = []
    for entry in lessons:
        lesson_id = entry["id"]
        prefix = level_slug + "-"
        slug = lesson_id[len(prefix):] if lesson_id.startswith(prefix) else lesson_id
        lesson_json_path = REPO_ROOT / "curriculum" / level_slug / f"{slug}.json"
        title = json.loads(lesson_json_path.read_text(encoding="utf-8"))["title"]
        out.append({"slug": slug, "title": title})
    return out


def main():
    nav_map = {level: build_level(level) for level in LEVELS}
    out_path = REPO_ROOT / "scripts" / "lesson_nav_map.json"
    out_path.write_text(json.dumps(nav_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for lvl, lessons in nav_map.items():
        print(f"{lvl}: {len(lessons)} lessons")


if __name__ == "__main__":
    main()
