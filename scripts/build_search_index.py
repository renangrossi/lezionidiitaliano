#!/usr/bin/env python3
"""
Build assets/data/search-index.json: the flat array assets/js/search.js
fetches once and filters entirely client-side. Entry shape:
{ type, level, title, desc, url, keywords[] } — see search.js's
TYPE_LABEL map for valid `type` values (level, lesson, grammar, exercise,
mock, extra).

Usage:
    python3 scripts/build_search_index.py
"""
import json
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LEVEL_ENTRIES = [
    ("A1", "a1", "Beginner", "Essere, avere, articles and gender, present tense, everyday greetings."),
    ("A2", "a2", "Elementary", "Irregular present-tense verbs, passato prossimo, reflexive verbs, direct pronouns."),
    ("B1", "b1", "Intermediate", "Imperfetto, indirect and combined pronouns, futuro, condizionale, imperativo."),
    ("B2", "b2", "Upper Intermediate", "Trapassato prossimo, congiuntivo, periodo ipotetico, passive voice, reported speech."),
    ("C1", "c1", "Advanced", "Congiuntivo trapassato, gerundio, pronominal verbs, formal register."),
    ("C2", "c2", "Proficient", "Complex syntax, literary register, lexical nuance, discourse cohesion."),
]

STATIC_ENTRIES = [
    {"type": "extra", "level": "", "title": "Exercises", "desc": "Extra reading and vocabulary practice, independent of level.",
     "url": "exercises.html", "keywords": ["reading", "practice", "vocabulary"]},
    {"type": "mock", "level": "", "title": "Simulated Exams", "desc": "CILS/PLIDA-style mock exam sections with answer keys.",
     "url": "simulated-exams.html", "keywords": ["cils", "plida", "celi", "exam", "test"]},
    {"type": "extra", "level": "", "title": "Extras", "desc": "Italian culture, everyday expressions, and formal vs informal usage.",
     "url": "extras.html", "keywords": ["culture", "expressions", "tu", "lei", "formal", "informal"]},
    {"type": "grammar", "level": "", "title": "Dictionary & Reference", "desc": "Look up any Italian word across multiple dictionaries.",
     "url": "dictionary.html", "keywords": ["wordreference", "reverso", "treccani"]},
    {"type": "grammar", "level": "", "title": "Irregular Verbs", "desc": "Reference table of common Italian irregular verbs.",
     "url": "irregular-verbs.html", "keywords": ["essere", "avere", "andare", "fare", "conjugation"]},
    {"type": "extra", "level": "", "title": "Placement Test", "desc": "A short test to find out which CEFR level to start at.",
     "url": "placement-test.html", "keywords": ["level test", "what's my level"]},
    {"type": "extra", "level": "", "title": "Today's Review", "desc": "Spaced-repetition review of items you've gotten wrong before.",
     "url": "today-review.html", "keywords": ["spaced repetition", "review", "mastery"]},
]


def main():
    entries = []
    for code, slug, name, desc in LEVEL_ENTRIES:
        entries.append({
            "type": "level", "level": code, "title": f"{code} — {name}",
            "desc": desc, "url": f"levels/{slug}.html", "keywords": [name.lower()],
        })
        entries.append({
            "type": "grammar", "level": code, "title": f"{code} Test Yourself",
            "desc": f"Mixed review of every {code} grammar topic, with instant feedback.",
            "url": f"levels/{slug}/test-yourself.html", "keywords": ["review", "quiz"],
        })

    files = sorted(glob.glob(str(REPO_ROOT / "curriculum" / "*" / "*.json")))
    for fpath in files:
        lesson = json.loads(Path(fpath).read_text(encoding="utf-8"))
        level = lesson.get("level", "")
        slug = level.lower()
        prefix = slug + "-"
        lesson_id = lesson.get("id", "")
        file_slug = lesson_id[len(prefix):] if lesson_id.startswith(prefix) else lesson_id
        entries.append({
            "type": "lesson",
            "level": level,
            "title": lesson.get("title", ""),
            "desc": lesson.get("subtitle", ""),
            "url": f"levels/{slug}/{file_slug}.html",
            "keywords": [lesson.get("strand", ""), lesson.get("skill", "")],
        })

    entries.extend(STATIC_ENTRIES)

    out_path = REPO_ROOT / "assets" / "data" / "search-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {len(entries)} search entries -> {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
