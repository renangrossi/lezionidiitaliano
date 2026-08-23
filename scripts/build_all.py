#!/usr/bin/env python3
"""
Runs the full build pipeline in order. Run this after editing anything in
scripts/curriculum_source/*.py or the static-page generators.

Usage:
    python3 scripts/build_all.py
"""
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
STEPS = [
    "generate_curriculum.py",
    "build_nav_map.py",
    "build_level_pages.py",
    "build_test_yourself.py",
    "build_exercise_index.py",
    "build_search_index.py",
    "build_static_pages.py",
]


def main():
    for step in STEPS:
        print(f"\n=== {step} ===")
        subprocess.run([sys.executable, str(SCRIPTS_DIR / step)], check=True)
        if step == "build_nav_map.py":
            # Build every lesson page too (glob can't be passed as a single
            # arg to subprocess without shell=True, so expand it here) --
            # computed only now, after generate_curriculum.py has actually
            # written curriculum/*/*.json.
            lesson_files = sorted((SCRIPTS_DIR.parent / "curriculum").glob("*/*.json"))
            print("\n=== build_lesson.py (all lessons) ===")
            subprocess.run([sys.executable, str(SCRIPTS_DIR / "build_lesson.py")] + [str(f) for f in lesson_files], check=True)

    print("\nBuild complete.")


if __name__ == "__main__":
    main()
