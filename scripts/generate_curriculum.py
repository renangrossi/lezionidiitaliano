#!/usr/bin/env python3
"""
Compiles scripts/curriculum_source/{level}.py (hand-authored Python lesson
data — see curriculum/SCHEMA.md for the target shape) into
curriculum/{level}/{lesson-id}.json and curriculum/index.json.

Run this whenever curriculum_source/*.py changes, then re-run
build_nav_map.py, build_lesson.py (on every file), build_test_yourself.py,
build_exercise_index.py and build_search_index.py in that order — or just
run scripts/build_all.py, which does the whole pipeline.

Usage:
    python3 scripts/generate_curriculum.py
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent / "curriculum_source"))

LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]


def main():
    index = {"levels": {}}
    for level_slug in LEVELS:
        mod = __import__(level_slug)
        level_key = level_slug.upper()
        lessons = mod.LESSONS
        out_dir = REPO_ROOT / "curriculum" / level_slug
        out_dir.mkdir(parents=True, exist_ok=True)

        lesson_entries = []
        for lesson in lessons:
            slug = lesson["id"][len(level_slug) + 1:]
            out_path = out_dir / f"{slug}.json"
            out_path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            lesson_entries.append({"id": lesson["id"], "status": "published"})

        index["levels"][level_key] = {
            "overview": mod.OVERVIEW,
            "units": [{"id": "1", "title": f"{level_key} Grammar", "lessons": lesson_entries}],
        }
        print(f"{level_slug}: wrote {len(lessons)} lesson JSON files")

    index_path = REPO_ROOT / "curriculum" / "index.json"
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {index_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
