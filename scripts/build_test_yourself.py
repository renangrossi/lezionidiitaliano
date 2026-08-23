#!/usr/bin/env python3
"""
Build levels/{level}/test-yourself.html: every exercise block from every
lesson in that level, grouped under its lesson's heading, on one page —
"more questions, mixed together, with instant feedback," exactly what
each lesson page's own "Test Yourself" call-to-action promises. Generated
directly from curriculum/{level}/*.json (via lesson_nav_map.json for
ordering) rather than hand-authored, so it can never drift out of sync
with the lessons it reviews.

Usage:
    python3 scripts/build_test_yourself.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../../"
LEVELS = [("A1", "a1"), ("A2", "a2"), ("B1", "b1"), ("B2", "b2"), ("C1", "c1"), ("C2", "c2")]


def topic_section(lesson):
    blocks = "".join(
        f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div>'
        for ex in lesson["exercises"]
    )
    slug = lesson["id"].split("-", 1)[1] if "-" in lesson["id"] else lesson["id"]
    return f"""<section id="{slug}" class="section section--tight ty-topic" aria-labelledby="ty-{slug}-heading">
        <div class="section__inner">
            <p class="eyebrow">{lesson['level']}</p>
            <h2 id="ty-{slug}-heading"><a href="{slug}.html">{lesson['title']}</a></h2>
            <p style="color:var(--color-text-muted);max-width:60ch;margin-bottom:var(--space-md);">{lesson['subtitle']}</p>
            {blocks}
        </div>
    </section>"""


def build(level_code, level_slug):
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    lessons_order = nav_map.get(level_slug, [])

    sections = []
    toc_links = []
    for entry in lessons_order:
        lesson_path = REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json"
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        sections.append(topic_section(lesson))
        toc_links.append(f'<a href="#{entry["slug"]}">{lesson["title"]}</a>')

    title = f"{level_code} Test Yourself — Mixed Review — Renan the Teacher"
    description = f"Every {level_code} grammar topic in one mixed review, with instant feedback on every question."
    breadcrumb = (
        f'<li><a href="{REL}index.html">Home</a></li>'
        f'<li aria-current="page">Levels</li>'
        f'<li><a href="../{level_slug}.html">{level_code}</a></li>'
        f'<li aria-current="page">Test Yourself</li>'
    )

    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{level_code} &middot; Mixed Review</p>
                <h1>Test Yourself: {level_code}</h1>
                <p class="page-header__lede">Every exercise from every {level_code} lesson, gathered on one page. Work through as much as you like, in any order.</p>
            </div>
        </div>
    </div>"""
    toc = f'<div class="level-toc"><div class="level-toc__inner">{"".join(toc_links)}</div></div>'

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.extend(sections)
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_dir = REPO_ROOT / "levels" / level_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "test-yourself.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)} ({len(sections)} topics)")


if __name__ == "__main__":
    for code, slug in LEVELS:
        build(code, slug)
