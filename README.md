# Renan the Teacher — Italian Language Academy

A CEFR-aligned Italian course (A1–C2), sister site to the
[English course](https://renangrossi.github.io/englishclasses/). Static
HTML/CSS/JS, no framework, no build step to view — deployable as-is to
GitHub Pages or any static host.

## Running locally

From the project root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/`. A plain `file://` open mostly works
too, except site search and the exercise/search index fetches, which
browsers block for local files — use the server for full functionality.

## Editing content

Every page is generated from Python — there is no hand-edited HTML.
Lesson content lives in `scripts/curriculum_source/{level}.py` (plain
Python data, not hand-escaped JSON, so prose with apostrophes like
*c'è* or *dell'acqua* reads naturally). After editing, rebuild
everything with:

```bash
python3 scripts/build_all.py
```

This regenerates `curriculum/*/*.json`, every `levels/**/*.html` page,
the per-level Test Yourself pages, the search index, the spaced-repetition
exercise index, and all nine top-level pages (home, exercises, extras,
dictionary, irregular verbs, placement test, progress, today's review,
simulated exams). See `curriculum/SCHEMA.md` for the lesson JSON shape,
and `scripts/site_chrome.py` for the shared page chrome every generated
page uses.

## What's deliberately not included yet

- **AI Teacher chat** — the English site's Cloudflare-Worker-backed chat
  assistant isn't included; it needs its own Worker + API key.
- **Real audio** — listening sections are dialogue/monologue transcripts,
  not recorded MP3s (the UI has no audio player to wire up yet).

## Deployment

This is a static site — any static host works. For GitHub Pages: push to
a repo, enable Pages on the `main` branch root, and the included
`.nojekyll` file (already present) stops Jekyll from mangling anything
starting with an underscore.
