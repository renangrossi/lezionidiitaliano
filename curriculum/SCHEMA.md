# Curriculum data schema

Single source of truth for lesson content. Each lesson is one JSON file at
`curriculum/{level}/{lesson-id}.json`, generated from the hand-authored
Python data in `scripts/curriculum_source/{level}.py` by
`scripts/generate_curriculum.py` — edit the Python, not the JSON directly
(a regeneration will overwrite it). `curriculum/index.json` lists every
level's lessons in order and is also generated, not hand-edited.

This is the sister schema to the English course's `curriculum/SCHEMA.md`,
with three deliberate differences: examples are bilingual objects
(`{"it": ..., "en": ...}`) instead of a single string, since this course's
whole point is Italian examples with English glosses; there is no
`prerequisites`/`related`/`sourceMaterial` (no docx/pdf source material
exists for this course — every lesson was authored directly); and every
level (including A1) goes through this same pipeline — there is no
hand-authored-HTML exception.

## Lesson JSON shape

```jsonc
{
  "id": "b1-imperfetto",              // matches the generated filename
  "level": "B1",
  "unit": "1",                        // curriculum/index.json unit this belongs to (currently always "1" — one unit per level)
  "order": 1,                         // position within the level
  "skill": "grammar",                 // grammar | vocabulary | pronunciation | reading
                                       // | listening | speaking | writing | functional
  "strand": "past-tenses",            // free-text grouping, informational only
  "title": "L'Imperfetto",
  "subtitle": "Italian's other past tense — for background, habits, and descriptions.",
  "objectives": ["...", "..."],
  "content": {
    "intro": "One short paragraph, shown next to the objectives card.",
    "explanation": "<p>...</p>",      // optional; inline HTML (strong/em/p), rendered raw (trusted)
    "rules": [ { "heading": "a) ...", "body": "<p>...</p> or <ul>...</ul>" }, ... ],  // rendered raw (trusted)
    "table": "<div class=\"table-scroll\">...</div>",  // optional, a full ref-table block, rendered raw
    "examples": [ { "it": "Italian sentence.", "en": "English gloss." }, ... ],  // both fields HTML-escaped
    "commonMistakes": [ { "wrong": "...", "right": "...", "why": "..." }, ... ]
  },
  "exercises": [ /* verbatim assets/js/exercises.js exercise-data objects — see that file's header comment for the full item schema per type */ ],
  "summary": ["One-line takeaway", "..."]
}
```

`rules[].body`, `content.explanation` and `content.table` are trusted raw
HTML (not escaped) — only put content you wrote yourself there, matching
the tags exercises.js/lessons.css already style (`<p>`, `<ul>/<li>`,
`<strong>`, `<em>`, `<div class="table-scroll"><table class="ref-table">`).
Everything else (title, subtitle, objectives, examples, commonMistakes,
summary) is HTML-escaped automatically by `scripts/build_lesson.py` — use
plain text there, including literal Unicode characters like `→` or `—`
rather than HTML entities such as `&rarr;`/`&mdash;` (an entity in an
escaped field would double-encode and show up literally as `&rarr;` on
the page).

## `curriculum/index.json` shape

```jsonc
{
  "levels": {
    "B1": {
      "overview": "One paragraph shown on the B1 level hub page.",
      "units": [
        { "id": "1", "title": "B1 Grammar", "lessons": [ { "id": "b1-imperfetto", "status": "published" }, ... ] }
      ]
    }
  }
}
```

## Build

```bash
python3 scripts/build_all.py
```

Runs the full pipeline in order: `generate_curriculum.py` (Python →
JSON) → `build_nav_map.py` → `build_lesson.py` (every lesson JSON → its
HTML page, reusing the shared chrome in `scripts/site_chrome.py`) →
`build_level_pages.py` (the six level hub pages) →
`build_test_yourself.py` (per-level mixed-review pages) →
`build_exercise_index.py` (spaced-repetition item lookup) →
`build_search_index.py` (site search) → `build_static_pages.py` (home,
exercises, extras, dictionary, irregular verbs, placement test, progress,
today's review, simulated exams).
