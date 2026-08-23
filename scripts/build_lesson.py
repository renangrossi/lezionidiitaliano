#!/usr/bin/env python3
"""
Render one curriculum/{level}/{lesson-id}.json into levels/{level}/{lesson-id}.html,
following the same section structure as the English course's lesson pages
(Objectives -> Explanation -> Rules -> Examples -> Common Mistakes -> Practice
-> Summary -> Related), using the shared chrome from site_chrome.py.

All structural UI text (section headings, eyebrows, buttons, badges) is in
Italian — see site_chrome.py's header comment for why. The lesson content
itself (objectives/explanation/rules/examples/mistakes/summary, read from
curriculum/*.json) is untouched here; whatever language it was authored in
is what's rendered.

Usage:
    python3 scripts/build_lesson.py curriculum/b1/imperfetto.json
    python3 scripts/build_lesson.py curriculum/*/*.json   # build everything
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../../"  # levels/{level}/{lesson}.html -> repo root
NAV_MAP_PATH = Path(__file__).resolve().parent / "lesson_nav_map.json"


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def page_header(lesson, lesson_no, lesson_count):
    return f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{lesson['level']} &middot; Lezione {lesson_no} di {lesson_count}</p>
                <h1>{esc(lesson['title'])}</h1>
                <p class="page-header__lede">{esc(lesson['subtitle'])}</p>
            </div>
        </div>
    </div>"""


def toc(present_ids):
    labels = {
        "objectives": "Obiettivi", "explanation": "Spiegazione", "rules": "Regole",
        "examples": "Esempi", "mistakes": "Errori Comuni", "practice": "Pratica",
        "summary": "Riepilogo",
    }
    links = "".join(f'<a href="#{a}">{labels[a]}</a>' for a in labels if a in present_ids)
    links += '<a href="#related">Continua</a>'
    return f'<div class="level-toc"><div class="level-toc__inner">{links}</div></div>'


def objectives_section(lesson):
    items = "".join(f"<li>{site_chrome.CHECK_SVG}<span>{esc(o)}</span></li>" for o in lesson["objectives"])
    return f"""<section id="objectives" class="section section--tight" aria-labelledby="obj-heading">
        <div class="section__inner split">
            <div>
                <p class="eyebrow">Introduzione</p>
                <p style="font-size:var(--step-0);color:var(--color-text-muted);max-width:56ch;">{esc(lesson['content']['intro'])}</p>
            </div>
            <div class="card card--feature">
                <h2 id="obj-heading" style="font-size:var(--step-0);">Al termine di questa lezione saprai&hellip;</h2>
                <ul class="objectives-list">{items}</ul>
            </div>
        </div>
    </section>"""


def explanation_section(lesson):
    c = lesson["content"]
    explanation = c.get("explanation")
    register = f'<div class="notice mt-lg"><strong>Registro</strong><p>{esc(c["registerNote"])}</p></div>' if c.get("registerNote") else ""
    if not explanation and not register:
        return ""
    if explanation:
        inner = explanation if "<" in explanation else f"<p>{esc(explanation)}</p>"
        body = f'<div class="prose">{inner}</div>'
    else:
        body = ""
    return f"""<section id="explanation" class="section section--surface" aria-labelledby="exp-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Spiegazione</p>
            <h2 id="exp-heading" class="visually-hidden">Spiegazione</h2>
            {body}
            {register}
        </div>
    </section>"""


def rules_section(lesson):
    rules = lesson["content"].get("rules") or []
    if not rules:
        return ""
    blocks = "".join(f'<div class="card" style="margin-bottom:var(--space-md);"><h3>{esc(r["heading"])}</h3>{r["body"]}</div>' for r in rules)
    table_html = lesson["content"].get("table", "")
    layout_open = '<div class="split" style="align-items:start;">' if table_html else ""
    layout_close = "</div>" if table_html else ""
    return f"""<section id="rules" class="section section--tight" aria-labelledby="rules-heading">
        <div class="section__inner">
            <p class="eyebrow">Regole Grammaticali</p>
            <h2 id="rules-heading">Le Regole</h2>
            {layout_open}
            {blocks}
            {table_html}
            {layout_close}
        </div>
    </section>"""


def examples_section(lesson):
    items = "".join(
        f'<li><svg class="examples-list__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg><span><strong class="it-example">{esc(e["it"])}</strong><br><span class="en-example">{esc(e["en"])}</span></span></li>'
        for e in lesson["content"]["examples"]
    )
    return f"""<section id="examples" class="section section--surface" aria-labelledby="ex-heading">
        <div class="section__inner">
            <p class="eyebrow">Esempi</p>
            <h2 id="ex-heading">Vediamola in Pratica</h2>
            <ul class="examples-list examples-list--bilingual">{items}</ul>
        </div>
    </section>"""


def mistakes_section(lesson):
    if not lesson["content"].get("commonMistakes"):
        return ""
    cards = "".join(
        f"""<div class="mistake-card">
            <p class="mistake-card__wrong"><span class="badge badge--pdf" style="margin-right:.5em;">Evita</span>{esc(m['wrong'])}</p>
            <p class="mistake-card__right"><span class="badge badge--doc" style="margin-right:.5em;">Usa invece</span>{esc(m['right'])}</p>
            <p class="mistake-card__why">{esc(m['why'])}</p>
        </div>"""
        for m in lesson["content"]["commonMistakes"]
    )
    return f"""<section id="mistakes" class="section section--tight" aria-labelledby="mist-heading">
        <div class="section__inner">
            <p class="eyebrow">Errori Comuni</p>
            <h2 id="mist-heading">Attenzione a</h2>
            <div class="mistakes-grid">{cards}</div>
        </div>
    </section>"""


def practice_section(lesson):
    blocks = "".join(
        f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div>'
        for ex in lesson["exercises"]
    )
    return f"""<section id="practice" class="section section--surface" aria-labelledby="practice-heading">
        <div class="section__inner">
            <p class="eyebrow">Esercizi Interattivi</p>
            <h2 id="practice-heading">Pratica</h2>
            <p style="color:var(--color-text-muted);margin-bottom:var(--space-md);max-width:60ch;">Completa ogni esercizio, poi clicca su <strong>Invia</strong> per vedere il tuo punteggio e una spiegazione per ogni risposta.</p>
            {blocks}
        </div>
    </section>"""


def summary_section(lesson):
    items = "".join(f"<li>{esc(s)}</li>" for s in lesson["summary"])
    return f"""<section id="summary" class="section section--tight" aria-labelledby="sum-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Riepilogo</p>
            <h2 id="sum-heading">Ripasso</h2>
            <ul class="summary-list">{items}</ul>
        </div>
    </section>"""


def related_section(lesson, level_slug, prev_lesson, next_lesson):
    prev_link = (
        f'<a class="btn btn--ghost" href="{prev_lesson["slug"]}.html">{site_chrome.ARROW_SVG} Precedente: {esc(prev_lesson["title"])}</a>'
        if prev_lesson else ""
    )
    next_link = (
        f'<a class="btn btn--accent" href="{next_lesson["slug"]}.html">Successivo: {esc(next_lesson["title"])} {site_chrome.ARROW_SVG}</a>'
        if next_lesson else ""
    )
    return f"""<section id="related" class="section section--surface" aria-labelledby="rel-heading">
        <div class="section__inner">
            <p class="eyebrow">Continua così</p>
            <h2 id="rel-heading">Prosegui il Tuo Percorso</h2>
            <div class="lesson-nav">
                {prev_link}
                <a class="btn btn--ghost" href="../{level_slug}.html">Torna a {lesson['level']}</a>
                {next_link}
            </div>
        </div>
    </section>"""


def build(lesson_path: Path):
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    level_slug = lesson["level"].lower()
    prefix = level_slug + "-"
    lesson_slug = lesson["id"][len(prefix):] if lesson["id"].startswith(prefix) else lesson["id"]

    title = f"{lesson['title']} — Grammatica Italiana {lesson['level']} — Renan the Teacher"
    description = f"{lesson['title']}: {lesson['subtitle']}"[:300]
    breadcrumb = (
        f'<li><a href="{REL}index.html">Home</a></li>'
        f'<li aria-current="page">Livelli</li>'
        f'<li><a href="../{level_slug}.html">{lesson["level"]}</a></li>'
        f'<li aria-current="page">{esc(lesson["title"])}</li>'
    )

    sections = {
        "objectives": objectives_section(lesson),
        "explanation": explanation_section(lesson),
        "rules": rules_section(lesson),
        "examples": examples_section(lesson),
        "mistakes": mistakes_section(lesson),
        "practice": practice_section(lesson),
        "summary": summary_section(lesson),
    }
    present_ids = [k for k, v in sections.items() if v]

    nav_map = json.loads(NAV_MAP_PATH.read_text(encoding="utf-8")) if NAV_MAP_PATH.exists() else {}
    nav_list = nav_map.get(level_slug, [])
    pos = next((i for i, l in enumerate(nav_list) if l["slug"] == lesson_slug), None)
    prev_lesson = nav_list[pos - 1] if pos is not None and pos > 0 else None
    next_lesson = nav_list[pos + 1] if pos is not None and pos < len(nav_list) - 1 else None
    lesson_no = (pos + 1) if pos is not None else 1
    lesson_count = len(nav_list) or 1

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, lesson["level"], breadcrumb, active_top="levels"))
    out.append(page_header(lesson, lesson_no, lesson_count))
    out.append(toc(present_ids))
    for k in present_ids:
        out.append(sections[k])
    out.append(related_section(lesson, level_slug, prev_lesson, next_lesson))
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_dir = REPO_ROOT / "levels" / level_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{lesson_slug}.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)}")
    return out_path


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        build(Path(arg))
