#!/usr/bin/env python3
"""
Builds every top-level standalone page: index.html, exercises.html,
extras.html, dictionary.html, irregular-verbs.html, placement-test.html,
progress.html, today-review.html, simulated-exams.html.

Usage:
    python3 scripts/build_static_pages.py
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = ""

STAR = site_chrome.STAR
STARS_ROW = site_chrome.STARS_ROW
ARROW = site_chrome.ARROW_SVG
CHECK = site_chrome.CHECK_SVG


def esc(s):
    return html.escape(s, quote=False)


def ex_block(data):
    return f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(data, ensure_ascii=False)}</script></div>'


def page_header(eyebrow, h1, lede):
    return f"""<div class="page-header">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{esc(eyebrow)}</p>
                <h1>{h1}</h1>
                <p class="page-header__lede">{lede}</p>
            </div>
        </div>
    </div>"""


def write_page(path, title, description, body_sections, active_top=None, breadcrumb_label=None,
                extra_css=None, extra_scripts=None):
    breadcrumb = None
    if breadcrumb_label:
        breadcrumb = f'<li><a href="{REL}index.html">Home</a></li><li aria-current="page">{breadcrumb_label}</li>'
    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=extra_css))
    out.append(site_chrome.header(REL, None, breadcrumb, active_top=active_top))
    out.extend(body_sections)
    out.append(site_chrome.footer(REL, extra_scripts=extra_scripts))
    (REPO_ROOT / path).write_text("\n".join(out), encoding="utf-8")
    print(f"Built {path}")


# =======================================================================
# INDEX
# =======================================================================
def build_index():
    hero = f"""<section class="hero" id="mission">
        <div class="hero__inner">
            {STARS_ROW}
            <div class="hero__split">
                <div>
                    <p class="eyebrow hero__eyebrow">Benvenuti</p>
                    <h1>Welcome to teacher Renan's Italian Course</h1>
                    <p class="hero__lede">A CEFR-aligned academy of Italian grammar, vocabulary and exercises &mdash; explanations in English, examples in real Italian.<br>Buon lavoro!</p>
                    <div class="hero__actions">
                        <a class="btn btn--accent" href="levels/a1.html">Start with A1 {ARROW}</a>
                        <a class="btn btn--ghost-inverse" href="placement-test.html">What's my level?</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <hr class="rule">"""

    level_grammar = {
        "A1": ["Essere &amp; avere", "Gender &amp; articles", "Present tense (-are/-ere/-ire)", "Questions &amp; c'è/ci sono"],
        "A2": ["Irregular present verbs", "Passato prossimo", "Reflexive verbs", "Direct object pronouns"],
        "B1": ["Imperfetto vs. passato prossimo", "Indirect &amp; combined pronouns", "Futuro &amp; condizionale", "Imperativo, ci &amp; ne"],
        "B2": ["Trapassato prossimo", "Congiuntivo (presente &amp; imperfetto)", "Periodo ipotetico I/II", "Passivo &amp; discorso indiretto"],
        "C1": ["Congiuntivo trapassato", "Periodo ipotetico III", "Gerundio &amp; progressivo", "Registro &amp; connettivi"],
        "C2": ["Sintassi complessa", "Registro letterario", "Sfumature lessicali", "Coesione testuale"],
    }
    cards = []
    for i, (code, topics) in enumerate(level_grammar.items()):
        roman = ["I", "II", "III", "IV", "V", "VI"][i]
        items = "".join(f"<li>{t}</li>" for t in topics)
        name = dict(site_chrome.LEVELS)[code] if False else None
        level_name = {c: n for c, n, s in site_chrome.LEVELS}[code]
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{roman}</span>
            <h3>{code} &mdash; {level_name}</h3>
            <ul style="color:var(--color-text-muted);font-size:var(--step--1);padding-left:1.1em;list-style:disc;display:flex;flex-direction:column;gap:0.25em;">{items}</ul>
            <div class="lesson-card__actions"><a class="btn btn--ghost btn--small" href="levels/{code.lower()}.html">Open {code} {ARROW}</a></div>
        </article>""")

    grammar_section = f"""<section id="grammar" class="section section--surface" aria-labelledby="grammar-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Grammar</p>
                <h2 id="grammar-heading">The Italian grammar roadmap</h2>
                <p>A complete tour of Italian grammar across six CEFR levels, from your first essere/avere to literary register &mdash; open any level to see every topic and start practicing.</p>
            </div>
            <div class="grid">{"".join(cards)}</div>
        </div>
    </section>"""

    ladder_items = []
    ladder_desc = {
        "A1": "Basic phrases and everyday expressions for immediate needs.",
        "A2": "Simple, direct exchanges on familiar topics and routine matters.",
        "B1": "Independent use of Italian for work, study and travel situations.",
        "B2": "Fluent, spontaneous interaction and clear, detailed argument.",
        "C1": "Flexible, effective language use for academic and professional life.",
        "C2": "Precise, nuanced command of Italian in virtually any context.",
    }
    for code, name, slug in site_chrome.LEVELS:
        ladder_items.append(f"""<li class="ladder__rung">
            <span class="ladder__code" aria-hidden="true">{code}</span>
            <div class="ladder__body">
                <h3>{name}</h3>
                <p>{ladder_desc[code]} <a class="ladder__link" href="levels/{slug}.html">Enter the level {ARROW}</a></p>
            </div>
        </li>""")

    cefr_section = f"""<section id="about-cefr" class="section section--surface" aria-labelledby="cefr-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">The Framework &amp; Your Path Through It</p>
                <h2 id="cefr-heading">About the CEFR</h2>
                <p>The <strong>Common European Framework of Reference for Languages (CEFR)</strong> is the international standard for describing language ability. It organizes this course into six levels &mdash; enter any level below.</p>
            </div>
            <ol class="ladder">{"".join(ladder_items)}</ol>
        </div>
    </section>"""

    skills = [
        ("Grammar", "index.html#grammar", "M3 8 4 8v13a1 1 0 0 0 1 1h6", "Structured tenses, forms and rules, organized by CEFR level and cross-referenced with practice exercises.", '<path d="M3 5.5C3 4.7 3.7 4 4.5 4H10a2 2 0 0 1 2 2v14a1.5 1.5 0 0 0-1.5-1.5H4.5A1.5 1.5 0 0 1 3 17V5.5Z"/><path d="M21 5.5c0-.8-.7-1.5-1.5-1.5H14a2 2 0 0 0-2 2v14a1.5 1.5 0 0 1 1.5-1.5h5.5a1.5 1.5 0 0 0 1.5-1.5V5.5Z"/>'),
        ("Vocabulary", None, None, "Themed word lists that build alongside each level's grammar, from first nouns to nuanced collocations.", '<path d="M4 19V6.5A2.5 2.5 0 0 1 6.5 4H8"/><path d="M4 13h4"/><path d="M14 19V6.5A2.5 2.5 0 0 1 16.5 4H20"/><path d="M14 13h4"/>'),
        ("Exercises", "exercises.html", None, "Extra reading and vocabulary practice, independent of level, for any time.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
        ("Reading", "exercises.html", None, "Authentic-style Italian passages and dialogues that put grammar and vocabulary to work in context.", '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/>'),
        ("Listening", "exercises.html", None, "Dialogue and monologue transcripts for developing an ear for natural spoken Italian.", '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3Z"/>'),
        ("Writing", None, None, "Guided writing tasks that grow from single sentences to structured argumentative paragraphs.", '<path d="M2 22c4-1 8-3 10-5"/><path d="M22 2c-8 0-16 4-16 14 0 2 2 4 4 4C20 20 22 10 22 2Z"/>'),
        ("Speaking", None, None, "Conversation prompts for discussion and practice at every level.", '<path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Z"/><path d="M19 11a7 7 0 0 1-14 0"/><path d="M12 18v3"/><path d="M9 21h6"/>'),
        ("Simulated Exams", "simulated-exams.html", None, "CILS/PLIDA-style mock exam sections with answer keys for certification preparation.", '<circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/>'),
    ]
    skill_cards = []
    for name, href, _, desc, icon in skills:
        tag_open = f'<a class="skill-card" href="{href}">' if href else '<div class="skill-card">'
        tag_close = "</a>" if href else "</div>"
        skill_cards.append(f'{tag_open}<svg class="skill-card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg><h3>{name}</h3><p>{desc}</p>{tag_close}')

    skills_section = f"""<section id="skills" class="section" aria-labelledby="skills-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">A Complete Curriculum</p>
                <h2 id="skills-heading">Every skill, covered</h2>
                <p>Each CEFR level works the same core skills so nothing is left to chance.</p>
            </div>
            <div class="grid grid--4">{"".join(skill_cards)}</div>
        </div>
    </section>"""

    why_section = f"""<section id="why-us" class="section section--surface" aria-labelledby="why-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Why Learn With Us</p>
                <h2 id="why-heading">A course built to be trusted</h2>
            </div>
            <div class="grid grid--3" style="max-width:70rem;margin:0 auto;">
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg></span>
                    <h3>Organized by the CEFR</h3>
                    <p>Every lesson is mapped to the Common European Framework, so you always know exactly where you stand and what comes next.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
                    <h3>Learn at your own pace</h3>
                    <p>Work straight through a level or dip into exercises, the dictionary, or today's review whenever you need extra practice.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 4 5.7 4 9s-1.5 6.5-4 9c-2.5-2.5-4-5.7-4-9s1.5-6.5 4-9Z"/></svg></span>
                    <h3>Built from real Italian</h3>
                    <p>Natural examples and dialogues, not contrived textbook filler &mdash; and every point of grammar comes with common mistakes to watch for.</p>
                </div>
            </div>
        </div>
    </section>"""

    cta = f"""<section class="cta-band" aria-labelledby="cta-heading">
        {STARS_ROW}
        <p class="eyebrow" style="justify-content:center;">Pronti quando siete voi</p>
        <h2 id="cta-heading">Enjoy the ride &mdash; start with your level today.</h2>
        <p>Not sure where to begin? Take the placement test, or just start at A1 and build up.</p>
        <div class="hero__actions">
            <a class="btn btn--accent" href="levels/a1.html">Browse all levels {ARROW}</a>
            <a class="btn btn--ghost-inverse" href="placement-test.html">What's my level?</a>
        </div>
    </section>"""

    write_page(
        "index.html",
        "Renan the Teacher — Italian Language Academy",
        "A CEFR-aligned Italian course with grammar, vocabulary, reading, listening, writing, speaking and mock exams, organized level by level from A1 to C2.",
        [hero, grammar_section, cefr_section, skills_section, why_section, cta],
        active_top="home",
        extra_scripts=[],
    )


# =======================================================================
# EXERCISES
# =======================================================================
def build_exercises():
    header = page_header("Independent Practice", "Exercises",
                          "Extra reading and vocabulary practice, independent of level &mdash; dip in any time.")

    items = [
        ("A2", "Un'Email da un'Amica", "<p>Ciao Sara! Come stai? Io sto benissimo. Sabato scorso sono andata al mercato con mia madre e abbiamo comprato tantissima frutta fresca. Poi abbiamo pranzato in un piccolo bar vicino a casa nostra.</p><p>Il weekend prossimo vado al mare con alcune amiche. Non vedo l'ora! Tu cosa fai di bello questo weekend? Scrivimi presto!<br>Un abbraccio,<br>Giulia</p>",
         {"id": "ex-a2-mail", "type": "true-false", "title": "Comprehension Check", "items": [
             {"id": "exa2m1", "statement": "Giulia went to the market with her mother.", "answer": True, "explanation": "\"Sono andata al mercato con mia madre.\""},
             {"id": "exa2m2", "statement": "Giulia is going to the mountains next weekend.", "answer": False, "explanation": "She's going to the seaside (al mare), not the mountains."},
         ]}),
        ("B1", "Un Annuncio di Lavoro", "<p><strong>Cercasi cameriere/a per ristorante nel centro di Bologna.</strong> Richiesta esperienza minima di un anno nel settore della ristorazione. Turni flessibili, anche nei weekend. Buona conoscenza dell'inglese è un plus. Stipendio commisurato all'esperienza. Per candidarsi, inviare il curriculum a info@ristorantebologna.it entro venerdì.</p>",
         {"id": "ex-b1-annuncio", "type": "multiple-choice", "title": "Comprehension Check", "items": [
             {"id": "exb1a1", "prompt": "How much experience is required?", "options": ["No experience needed", "At least one year", "At least five years"], "answerIndex": 1, "explanation": "\"Richiesta esperienza minima di un anno.\""},
             {"id": "exb1a2", "prompt": "What is considered a plus (\"un plus\")?", "options": ["Owning a car", "Speaking English well", "Living nearby"], "answerIndex": 1, "explanation": "\"Buona conoscenza dell'inglese è un plus.\""},
         ]}),
        ("B2", "Una Recensione di Ristorante", "<p>Ero scettico prima di prenotare, visto il gran numero di recensioni contrastanti online. Tuttavia, la mia esperienza è stata decisamente positiva. Il servizio, seppur non impeccabile, è stato cordiale, e i piatti — in particolare i primi — erano preparati con cura e ingredienti di qualità. Unica nota negativa: i tempi di attesa tra una portata e l'altra erano piuttosto lunghi.</p>",
         {"id": "ex-b2-recensione", "type": "true-false", "title": "Comprehension Check", "items": [
             {"id": "exb2r1", "statement": "The reviewer's overall impression was positive.", "answer": True, "explanation": "\"La mia esperienza è stata decisamente positiva.\""},
             {"id": "exb2r2", "statement": "The main course was mentioned as the weakest part of the meal.", "answer": False, "explanation": "The primi (first courses) were praised; the complaint was about wait times between courses."},
         ]}),
        ("C1", "Un Breve Articolo su Firenze", "<p>Firenze, culla del Rinascimento, continua ad attirare ogni anno milioni di visitatori, attratti tanto dal suo inestimabile patrimonio artistico quanto dall'atmosfera unica dei suoi vicoli storici. Nonostante le sfide poste dal turismo di massa — dalla gestione dei flussi alla tutela del centro storico — la città ha saputo, negli ultimi anni, sviluppare politiche di valorizzazione più sostenibili, incoraggiando i visitatori a esplorare anche i quartieri meno battuti.</p>",
         {"id": "ex-c1-firenze", "type": "multiple-choice", "title": "Comprehension Check", "items": [
             {"id": "exc1f1", "prompt": "What challenge does the article mention?", "options": ["Lack of historical monuments", "Mass tourism management", "A shortage of restaurants"], "answerIndex": 1, "explanation": "\"Le sfide poste dal turismo di massa\" is mentioned directly."},
         ]}),
    ]
    sections = [header]
    for level, title, passage, ex in items:
        sections.append(f"""<section class="section section--surface" aria-labelledby="ex-{ex['id']}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="ex-{ex['id']}-heading">{esc(title)}</h2>
                <div class="card"><div class="prose">{passage}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(ex)}</div>
            </div>
        </section>""")

    write_page("exercises.html", "Exercises — Renan the Teacher Italian Course",
               "Extra reading and vocabulary practice in Italian, independent of level, with instant feedback.",
               sections, active_top="exercises", breadcrumb_label="Exercises",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# EXTRAS
# =======================================================================
def build_extras():
    header = page_header("Beyond Grammar", "Extras",
                          "Common expressions, formal vs. informal Italian, everyday situations, and short culture notes.")

    expressions = [
        ("Certo!", "Sure! / Of course!", "A quick, warm way to agree to something."),
        ("Magari!", "If only! / I wish!", "Also a genuine expression of hope, on its own."),
        ("Boh.", "I have no idea. (shrug)", "Extremely common, casual — accompanied by a shrug."),
        ("Dai!", "Come on!", "Encouragement, mild protest, or impatience, depending on tone."),
        ("Che ne so.", "How should I know.", "Casual, mildly dismissive."),
        ("In bocca al lupo!", "Good luck! (lit. \"in the wolf's mouth\")", "The traditional reply is Crepi! (\"may it die\"), never grazie."),
        ("Non vedo l'ora!", "I can't wait!", "Literally \"I don't see the hour.\""),
        ("Fa niente.", "It's nothing / no worries.", "A casual way to dismiss an apology."),
        ("Meno male!", "Thank goodness!", "Relief at an outcome."),
        ("Che macello!", "What a mess! (colloquial)", "Casual register only."),
    ]
    exp_rows = "".join(f"<tr><td><strong>{esc(it)}</strong></td><td>{esc(en)}</td><td>{esc(note)}</td></tr>" for it, en, note in expressions)

    expressions_section = f"""<section id="expressions" class="section section--surface" aria-labelledby="expr-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Sound More Natural</p>
                <h2 id="expr-heading">Common Expressions</h2>
                <p>Small, high-frequency phrases that make your Italian sound native, not textbook.</p>
            </div>
            <div class="table-scroll"><table class="ref-table"><thead><tr><th>Italian</th><th>English</th><th>Note</th></tr></thead><tbody>{exp_rows}</tbody></table></div>
        </div>
    </section>"""

    formal_informal = f"""<section id="formal-informal" class="section section--tight" aria-labelledby="fi-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Register</p>
                <h2 id="fi-heading">Formal vs. Informal Italian</h2>
                <p>Choosing tu or Lei is only the start &mdash; formality runs through vocabulary and phrasing too.</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <h3>Informal (tu)</h3>
                    <ul class="rules-list">
                        <li>Ciao, come stai?</li>
                        <li>Scusa, hai un minuto?</li>
                        <li>Puoi aiutarmi?</li>
                        <li>Ti volevo chiedere una cosa.</li>
                        <li>A presto! / Ci vediamo!</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Formal (Lei)</h3>
                    <ul class="rules-list">
                        <li>Buongiorno, come sta?</li>
                        <li>Mi scusi, avrebbe un minuto?</li>
                        <li>Potrebbe aiutarmi?</li>
                        <li>Volevo chiederLe una cosa.</li>
                        <li>Cordiali saluti / ArrivederLa</li>
                    </ul>
                </div>
            </div>
            <div class="notice mt-lg"><strong>Rule of thumb</strong><p>Use Lei with strangers, anyone older, officials, and any professional context — until they invite you to use tu (<em>diamoci del tu</em>).</p></div>
        </div>
    </section>"""

    everyday = f"""<section id="everyday" class="section section--surface" aria-labelledby="everyday-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Real Situations</p>
                <h2 id="everyday-heading">Everyday Italian</h2>
                <p>Short, practical exchanges for situations you'll actually run into.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>At the bar</h3>
                    <p><em>Un caffè al banco, per favore.</em><br>(A coffee at the counter, please.)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">In many Italian bars, you pay at the register first, then bring your receipt (scontrino) to the counter.</p>
                </div>
                <div class="card">
                    <h3>At the market</h3>
                    <p><em>Quanto costano queste mele?</em><br>(How much do these apples cost?)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">Vendors often let you choose your own produce — just ask first: <em>Posso scegliere io?</em></p>
                </div>
                <div class="card">
                    <h3>Making small talk</h3>
                    <p><em>Che caldo/freddo oggi, eh?</em><br>(It's so hot/cold today, huh?)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">Weather is a safe, universal small-talk opener, just like in English.</p>
                </div>
            </div>
        </div>
    </section>"""

    culture = f"""<section id="culture" class="section section--tight" aria-labelledby="culture-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Cultural Notes</p>
                <h2 id="culture-heading">Italian Culture in Brief</h2>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Coffee rules</h3>
                    <p>Cappuccino is a breakfast drink — ordering one after a meal (especially after noon) will get you a friendly raised eyebrow from most Italians. Espresso, on the other hand, is fine any time.</p>
                </div>
                <div class="card">
                    <h3>Meal times</h3>
                    <p>Lunch (pranzo) is often the main meal, typically 1-2pm; dinner (cena) is usually later than in many other countries, often 8pm or after, especially in the south.</p>
                </div>
                <div class="card">
                    <h3>Regional pride</h3>
                    <p>Italy unified politically only in 1861, and regional identity remains strong: food, dialect, and even the way "the best" pizza or pasta dish is made can be a genuinely spirited local debate.</p>
                </div>
            </div>
        </div>
    </section>"""

    write_page("extras.html", "Extras — Renan the Teacher Italian Course",
               "Common expressions, formal vs. informal Italian, everyday situations, and short Italian culture notes.",
               [header, expressions_section, formal_informal, everyday, culture],
               active_top="extras", breadcrumb_label="Extras", extra_css=["lessons"])


# =======================================================================
# DICTIONARY
# =======================================================================
def dict_card(name, desc, url_tmpl, sample_word, featured=True):
    cls = "card card--feature dict-card" if featured else "card dict-card"
    btn_cls = "btn btn--accent btn--small dict-card__link" if featured else "btn btn--accent btn--small dict-card__link"
    sample_url = url_tmpl.replace("{word}", sample_word)
    return f"""<div class="{cls}" data-url-template="{url_tmpl}">
        <h3>{esc(name)}</h3>
        <p>{esc(desc)}</p>
        <div class="card__foot">
            <a class="{btn_cls}" data-dict-link href="{sample_url}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>Look up</a>
        </div>
    </div>"""


def build_dictionary():
    header = page_header("Dictionary & Reference", "Look Up Any Italian Word",
                          "Type a word once and open it directly in any of these Italian&ndash;English dictionaries, or use the pronunciation tools below.")

    input_section = f"""<section class="section section--surface" aria-labelledby="primary-dict-heading">
        <div class="section__inner">
            <h2 id="primary-dict-heading" class="visually-hidden">Core Dictionaries</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-lg);">
                <label for="dict-word" class="eyebrow" style="margin-bottom:0.6em;display:block;">Your word</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="dict-word" class="dict-input" placeholder="Type a word, e.g. &ldquo;magari&rdquo;" autocomplete="off" data-dict-word>
                </div>
                <p class="notice mt-lg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Every card below updates as you type. Press Enter to jump to a random one of the four core dictionaries.</p>
            </div>
            <div class="grid">
                {dict_card("WordReference", "The most widely used Italian–English dictionary, with a very active forum for tricky idioms.", "https://www.wordreference.com/iten/{word}", "magari")}
                {dict_card("Reverso Context", "See a word or phrase used in real, translated sentences — ideal for natural phrasing.", "https://context.reverso.net/translation/italian-english/{word}", "magari")}
                {dict_card("Treccani", "Italy's authoritative monolingual dictionary and encyclopedia — best for precise Italian definitions.", "https://www.treccani.it/vocabolario/ricerca/{word}/", "magari")}
                {dict_card("Collins Italian–English", "Clear definitions with audio pronunciation and example sentences.", "https://www.collinsdictionary.com/dictionary/italian-english/{word}", "magari")}
            </div>
        </div>
    </section>"""

    more_section = f"""<section class="section" aria-labelledby="more-dict-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">If You Need More</p>
                <h2 id="more-dict-heading">More Dictionaries &amp; Pronunciation</h2>
                <p>For a second opinion, synonyms, or to hear a word spoken by real people.</p>
            </div>
            <div class="grid">
                {dict_card("Linguee", "Bilingual search engine showing translated sentence pairs from real documents.", "https://www.linguee.com/english-italian/search?query={word}", "magari", featured=False)}
                {dict_card("Garzanti Linguistica", "A well-regarded Italian monolingual and bilingual dictionary.", "https://www.garzantilinguistica.it/ricerca/?q={word}", "magari", featured=False)}
                {dict_card("Italian Wiktionary", "Community-maintained, with etymology and regional usage notes.", "https://it.wiktionary.org/wiki/{word}", "magari", featured=False)}
                {dict_card("Forvo", "Crowd-sourced native pronunciations from Italian speakers around the world.", "https://forvo.com/word/{word}/#it", "magari", featured=False)}
                {dict_card("Conjugare.it", "Full conjugation tables for any Italian verb, every tense and mood.", "https://www.conjugare.it/{word}", "parlare", featured=False)}
                {dict_card("Sapere.it Sinonimi", "Italian synonyms and antonyms dictionary.", "https://www.sapere.it/sapere/strumenti/dizionario-sinonimi-contrari/ricerca/{word}.html", "magari", featured=False)}
            </div>
        </div>
    </section>"""

    write_page("dictionary.html", "Dictionary &amp; Reference — Renan the Teacher Italian Course",
               "Look up any Italian word across WordReference, Reverso Context, Treccani, Collins and more, with pronunciation tools.",
               [header, input_section, more_section],
               active_top="dictionary", breadcrumb_label="Dictionary &amp; Reference",
               extra_scripts=["dictionary.js"])


# =======================================================================
# IRREGULAR VERBS
# =======================================================================
IRREGULAR_VERBS = [
    ("essere", "to be", "sono", "stato", "essere"),
    ("avere", "to have", "ho", "avuto", "avere"),
    ("andare", "to go", "vado", "andato", "essere"),
    ("fare", "to do / make", "faccio", "fatto", "avere"),
    ("dire", "to say / tell", "dico", "detto", "avere"),
    ("stare", "to stay / be", "sto", "stato", "essere"),
    ("dare", "to give", "do", "dato", "avere"),
    ("venire", "to come", "vengo", "venuto", "essere"),
    ("uscire", "to go out", "esco", "uscito", "essere"),
    ("volere", "to want", "voglio", "voluto", "avere / essere*"),
    ("potere", "to be able to / can", "posso", "potuto", "avere / essere*"),
    ("dovere", "to have to / must", "devo", "dovuto", "avere / essere*"),
    ("sapere", "to know (facts/how to)", "so", "saputo", "avere"),
    ("bere", "to drink", "bevo", "bevuto", "avere"),
    ("salire", "to go up / get on", "salgo", "salito", "essere"),
    ("scendere", "to go down / get off", "scendo", "sceso", "essere"),
    ("rimanere", "to remain / stay", "rimango", "rimasto", "essere"),
    ("tenere", "to hold / keep", "tengo", "tenuto", "avere"),
    ("tradurre", "to translate", "traduco", "tradotto", "avere"),
    ("porre", "to place / pose", "pongo", "posto", "avere"),
    ("proporre", "to propose", "propongo", "proposto", "avere"),
    ("comporre", "to compose", "compongo", "composto", "avere"),
    ("condurre", "to lead / drive", "conduco", "condotto", "avere"),
    ("produrre", "to produce", "produco", "prodotto", "avere"),
    ("trarre", "to draw / pull", "traggo", "tratto", "avere"),
    ("distrarre", "to distract", "distraggo", "distratto", "avere"),
    ("piacere", "to like / be pleasing", "piaccio", "piaciuto", "essere"),
    ("scegliere", "to choose", "scelgo", "scelto", "avere"),
    ("spegnere", "to turn off", "spengo", "spento", "avere"),
    ("vincere", "to win", "vinco", "vinto", "avere"),
    ("perdere", "to lose", "perdo", "perso", "avere"),
    ("prendere", "to take", "prendo", "preso", "avere"),
    ("mettere", "to put", "metto", "messo", "avere"),
    ("chiudere", "to close", "chiudo", "chiuso", "avere"),
    ("aprire", "to open", "apro", "aperto", "avere"),
    ("scrivere", "to write", "scrivo", "scritto", "avere"),
    ("leggere", "to read", "leggo", "letto", "avere"),
    ("vedere", "to see", "vedo", "visto", "avere"),
    ("chiedere", "to ask", "chiedo", "chiesto", "avere"),
    ("rispondere", "to answer", "rispondo", "risposto", "avere"),
    ("decidere", "to decide", "decido", "deciso", "avere"),
    ("ridere", "to laugh", "rido", "riso", "avere"),
    ("correre", "to run", "corro", "corso", "avere / essere*"),
    ("morire", "to die", "muoio", "morto", "essere"),
    ("nascere", "to be born", "nasco", "nato", "essere"),
    ("crescere", "to grow", "cresco", "cresciuto", "essere / avere*"),
    ("conoscere", "to know (people/places)", "conosco", "conosciuto", "avere"),
    ("piangere", "to cry", "piango", "pianto", "avere"),
    ("rompere", "to break", "rompo", "rotto", "avere"),
    ("succedere", "to happen", "succede", "successo", "essere"),
    ("accendere", "to turn on", "accendo", "acceso", "avere"),
    ("offrire", "to offer", "offro", "offerto", "avere"),
    ("soffrire", "to suffer", "soffro", "sofferto", "avere"),
    ("uccidere", "to kill", "uccido", "ucciso", "avere"),
    ("riuscire", "to succeed / manage", "riesco", "riuscito", "essere"),
]


def build_irregular_verbs():
    header = page_header("Reference", "Italian Irregular Verbs",
                          "The most common irregular verbs, with their present tense (io), past participle, and auxiliary &mdash; type to filter.")

    rows = "".join(
        f"<tr><td><strong>{esc(inf)}</strong></td><td>{esc(meaning)}</td><td>{esc(pres)}</td><td>{esc(part)}</td><td class=\"text-muted\">{esc(aux)}</td></tr>"
        for inf, meaning, pres, part, aux in IRREGULAR_VERBS
    )

    section = f"""<section class="section section--surface" aria-labelledby="verbs-heading">
        <div class="section__inner">
            <h2 id="verbs-heading" class="visually-hidden">Irregular Verbs</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-md);">
                <label for="verb-filter" class="eyebrow" style="margin-bottom:0.6em;display:block;">Filter</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="verb-filter" class="dict-input" placeholder="Type to filter, e.g. &ldquo;prendere&rdquo; or &ldquo;essere&rdquo;" autocomplete="off" data-verb-filter>
                </div>
                <p class="notice mt-lg" data-verb-count><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Showing all {len(IRREGULAR_VERBS)} verbs. Verbs marked with an asterisk (*) take essere or avere depending on whether they're used with a direct object.</p>
                <p class="notice mt-lg" data-verb-empty hidden>No verbs match &ldquo;<span data-verb-empty-term></span>&rdquo;.</p>
            </div>
            <div class="table-scroll">
                <table class="ref-table">
                    <caption>Common Italian irregular verbs</caption>
                    <thead><tr><th>Infinito</th><th>Meaning</th><th>Presente (io)</th><th>Participio Passato</th><th>Ausiliare</th></tr></thead>
                    <tbody data-verb-tbody>{rows}</tbody>
                </table>
            </div>
        </div>
    </section>"""

    write_page("irregular-verbs.html", "Italian Irregular Verbs — Renan the Teacher Italian Course",
               "Reference table of common Italian irregular verbs: present tense, past participle, and auxiliary, with live filtering.",
               [header, section], active_top="extras", breadcrumb_label="Irregular Verbs",
               extra_css=["lessons"], extra_scripts=["irregular-verbs.js"])


# =======================================================================
# PLACEMENT TEST
# =======================================================================
def build_placement_test():
    header = page_header("Find Your Level", "Placement Test",
                          "24 questions, roughly two per level from A1 to C2. Answer as many as you can &mdash; your instinct about where it starts feeling hard is the best guide to your level.")

    blocks = [
        ("A1", [
            {"id": "pt-a1-1", "prompt": "Io ___ italiano.", "options": ["sono", "è", "sei"], "answerIndex": 0, "explanation": "Io + essere = sono."},
            {"id": "pt-a1-2", "prompt": "___ un libro sul tavolo. (there is)", "options": ["C'è", "Ci sono", "È"], "answerIndex": 0, "explanation": "Singular noun → c'è."},
            {"id": "pt-a1-3", "prompt": "Ho ___ anni. (I am 20 years old)", "options": ["sono venti", "venti", "vent'anni"], "answerIndex": 2, "explanation": "Age uses avere + [number] anni."},
            {"id": "pt-a1-4", "prompt": "___ amica (the friend, f.)", "options": ["La", "L'", "Lo"], "answerIndex": 1, "explanation": "Before a vowel, la shortens to l'."},
        ]),
        ("A2", [
            {"id": "pt-a2-1", "prompt": "Ieri ___ (io - mangiare) la pizza.", "options": ["ho mangiato", "mangio", "mangiavo"], "answerIndex": 0, "explanation": "A single completed past event → passato prossimo."},
            {"id": "pt-a2-2", "prompt": "Maria ___ (arrivare) tardi.", "options": ["ha arrivato", "è arrivata", "è arrivato"], "answerIndex": 1, "explanation": "Arrivare takes essere, agreeing with feminine Maria."},
            {"id": "pt-a2-3", "prompt": "Mi ___ (svegliarsi) alle sette.", "options": ["sveglio", "svegli", "mi sveglio"], "answerIndex": 2, "explanation": "Reflexive verb needs the pronoun mi."},
            {"id": "pt-a2-4", "prompt": "Roma è più grande ___ Firenze.", "options": ["che", "di", "come"], "answerIndex": 1, "explanation": "Comparing two nouns → di."},
        ]),
        ("B1", [
            {"id": "pt-b1-1", "prompt": "___ (Piovere) quando siamo usciti.", "options": ["È piovuto", "Pioveva", "Piove"], "answerIndex": 1, "explanation": "Background weather → imperfetto."},
            {"id": "pt-b1-2", "prompt": "___ scrivo un'email a Marco. (to him)", "options": ["Gli", "Le", "Lo"], "answerIndex": 0, "explanation": "Indirect object pronoun for \"to him\" → gli."},
            {"id": "pt-b1-3", "prompt": "___ (Volere - io) un caffè, per favore. (polite)", "options": ["Voglio", "Vorrei", "Volevo"], "answerIndex": 1, "explanation": "The polite conditional is vorrei."},
            {"id": "pt-b1-4", "prompt": "Vai in Italia? Sì, ___ vado domani.", "options": ["ci", "ne", "lo"], "answerIndex": 0, "explanation": "Replacing a place → ci."},
        ]),
        ("B2", [
            {"id": "pt-b2-1", "prompt": "Penso che lui ___ (avere) ragione.", "options": ["ha", "abbia", "avesse"], "answerIndex": 1, "explanation": "Penso che triggers the subjunctive."},
            {"id": "pt-b2-2", "prompt": "Se ___ (io - avere) più tempo, viaggerei di più.", "options": ["ho", "avessi", "avrei"], "answerIndex": 1, "explanation": "Second type hypothetical: se + congiuntivo imperfetto."},
            {"id": "pt-b2-3", "prompt": "La lettera ___ (scrivere) da Marco.", "options": ["è scritto", "è scritta", "ha scritto"], "answerIndex": 1, "explanation": "Passive voice, participle agrees with la lettera."},
            {"id": "pt-b2-4", "prompt": "Il libro ___ ho comprato è ottimo.", "options": ["cui", "che", "il quale"], "answerIndex": 1, "explanation": "Direct object relative pronoun → che."},
        ]),
        ("C1", [
            {"id": "pt-c1-1", "prompt": "Pensavo che tu ___ (essere) già partito.", "options": ["fossi", "sia", "eri"], "answerIndex": 0, "explanation": "Past main clause → congiuntivo trapassato/imperfetto (fossi = imperfect subjunctive of essere)."},
            {"id": "pt-c1-2", "prompt": "Se ___ (io - sapere), ti avrei chiamato.", "options": ["sapevo", "avrei saputo", "avessi saputo"], "answerIndex": 2, "explanation": "Third type hypothetical: se + congiuntivo trapassato."},
            {"id": "pt-c1-3", "prompt": "Sto ___ (leggere) un libro interessante.", "options": ["leggere", "leggendo", "letto"], "answerIndex": 1, "explanation": "Progressive form: stare + gerundio."},
            {"id": "pt-c1-4", "prompt": "Sebbene ___ (essere) tardi, siamo usciti.", "options": ["è", "era", "fosse"], "answerIndex": 2, "explanation": "Sebbene always triggers the subjunctive."},
        ]),
        ("C2", [
            {"id": "pt-c2-1", "prompt": "Which sentence uses inversion for emphasis?", "options": ["Il costo mi preoccupa.", "È il costo che mi preoccupa.", "Mi preoccupa il costo, davvero."], "answerIndex": 1, "explanation": "This is a cleft sentence, fronting il costo for emphasis."},
            {"id": "pt-c2-2", "prompt": "Devo ___ una decisione importante.", "options": ["fare", "prendere", "dare"], "answerIndex": 1, "explanation": "Prendere una decisione is the fixed collocation."},
            {"id": "pt-c2-3", "prompt": "\"Sembra che\" is typically followed by...", "options": ["the indicative", "the subjunctive", "the imperative"], "answerIndex": 1, "explanation": "Sembra che presents something as less than certain, triggering the subjunctive."},
        ]),
    ]
    sections = [header]
    all_items = []
    for level, items in blocks:
        all_items.extend(items)
        sections.append(f"""<section class="section section--tight" aria-labelledby="pt-{level}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="pt-{level}-heading">{level} Questions</h2>
                {ex_block({"id": f"pt-{level.lower()}-block", "type": "multiple-choice", "title": f"{level} Questions", "items": items})}
            </div>
        </section>""")

    guide = f"""<section class="section section--surface" aria-labelledby="pt-guide-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Reading Your Results</p>
            <h2 id="pt-guide-heading">What Your Score Means</h2>
            <ul class="summary-list">
                <li>Comfortable through A1&ndash;A2, struggling from B1 on &rarr; start at <a href="levels/b1.html">B1</a>.</li>
                <li>Comfortable through B1, struggling from B2 on &rarr; start at <a href="levels/b2.html">B2</a>.</li>
                <li>Comfortable through B2, struggling from C1 on &rarr; start at <a href="levels/c1.html">C1</a>.</li>
                <li>Missed several early questions &rarr; start at <a href="levels/a1.html">A1</a> and build a solid foundation &mdash; it goes quickly.</li>
                <li>Got everything right, including C2 &rarr; review the <a href="levels/c2.html">C2</a> lessons for polish, or explore the <a href="extras.html">Extras</a> page.</li>
            </ul>
        </div>
    </section>"""
    sections.append(guide)

    write_page("placement-test.html", "Placement Test — Renan the Teacher Italian Course",
               "A short self-scoring placement test to find out which CEFR level to start your Italian studies at.",
               sections, active_top=None, breadcrumb_label="Placement Test",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# PROGRESS
# =======================================================================
def build_progress():
    header = page_header("Your Journey", "My Progress",
                          "XP, streaks and badges, tracked entirely on this device &mdash; nothing is ever sent anywhere.")

    section = f"""<section class="section section--surface" aria-labelledby="progress-heading">
        <div class="section__inner">
            <h2 id="progress-heading" class="visually-hidden">Progress</h2>
            <div class="progress-panel__summary" id="progress-summary"></div>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-levels-heading">
        <div class="section__inner">
            <p class="eyebrow">By Level</p>
            <h2 id="progress-levels-heading">Progress by Level</h2>
            <div id="progress-levels"></div>
        </div>
    </section>
<section class="section section--surface" aria-labelledby="progress-badges-heading">
        <div class="section__inner">
            <p class="eyebrow">Achievements</p>
            <h2 id="progress-badges-heading">Badges</h2>
            <ul class="badge-grid" id="progress-badges"></ul>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-reset-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Start Over</p>
            <h2 id="progress-reset-heading">Reset Progress</h2>
            <p style="color:var(--color-text-muted);">This wipes your XP, streak and badges on this device. Your spaced-repetition review history (Today's Review) is stored separately and isn't affected.</p>
            <button type="button" class="btn btn--ghost" id="progress-reset-btn">Reset XP &amp; Badges</button>
        </div>
    </section>"""

    write_page("progress.html", "My Progress — Renan the Teacher Italian Course",
               "Track your XP, streak, and badges across the Italian course, stored privately on your device.",
               [header, section], active_top=None, breadcrumb_label="My Progress")


# =======================================================================
# TODAY'S REVIEW
# =======================================================================
def build_today_review():
    header = page_header("Spaced Repetition", "Today's Review",
                          "A short, daily review of exercise items you've gotten wrong before &mdash; pulled automatically from your own history.")

    section = f"""<section class="section section--surface" aria-labelledby="review-heading">
        <div class="section__inner">
            <h2 id="review-heading" class="visually-hidden">Review</h2>
            <div id="review-status-box" class="notice"><p>Loading your review queue&hellip;</p></div>
            <div id="review-blocks" style="margin-top:var(--space-md);"></div>
        </div>
    </section>"""

    write_page("today-review.html", "Today's Review — Renan the Teacher Italian Course",
               "A daily spaced-repetition review of Italian exercises you've gotten wrong before, generated automatically from your own history.",
               [header, section], active_top=None, breadcrumb_label="Today's Review",
               extra_css=["exercises"], extra_scripts=["exercises.js", "mastery.js", "today-review.js"])


# =======================================================================
# SIMULATED EXAMS
# =======================================================================
def build_simulated_exams():
    header = page_header("Exam Practice", "Simulated Exams",
                          "Practice sections in the style of Italy's official certification exams &mdash; CILS, CELI and PLIDA &mdash; with answer keys.")

    intro = f"""<section class="section section--tight" aria-labelledby="exams-intro-heading">
        <div class="section__inner section__inner--narrow">
            <h2 id="exams-intro-heading" class="visually-hidden">About These Exams</h2>
            <p style="color:var(--color-text-muted);">Italy has three main official Italian-as-a-foreign-language certifications: <strong>CILS</strong> (Università per Stranieri di Siena), <strong>CELI</strong> (Università per Stranieri di Perugia), and <strong>PLIDA</strong> (Società Dante Alighieri). All test the same four skills &mdash; reading, listening, writing, speaking &mdash; at CEFR levels A1 through C2. The sections below are practice in that style, not official past papers.</p>
        </div>
    </section>"""

    b1_reading = ("<p>Negli ultimi anni, sempre più italiani scelgono di lavorare da casa almeno un paio di giorni "
                  "alla settimana. Secondo un recente sondaggio, la maggior parte dei lavoratori si dichiara più "
                  "soddisfatta rispetto a prima, soprattutto grazie al tempo risparmiato negli spostamenti. Tuttavia, "
                  "alcuni intervistati segnalano difficoltà a separare vita privata e lavoro, lamentando giornate "
                  "lavorative più lunghe del solito.</p>")
    b1_reading_ex = {"id": "sim-b1-reading", "type": "true-false", "title": "CILS/PLIDA-Style Reading — B1", "items": [
        {"id": "simb1r1", "statement": "Most surveyed workers report being more satisfied working from home.", "answer": True, "explanation": "\"La maggior parte dei lavoratori si dichiara più soddisfatta.\""},
        {"id": "simb1r2", "statement": "No one reported any downsides to working from home.", "answer": False, "explanation": "Some reported trouble separating work and personal life, and longer workdays."},
    ]}
    b1_grammar_ex = {"id": "sim-b1-grammar", "type": "fill-blank", "title": "CILS/PLIDA-Style Grammar — B1",
                      "instructions": "Complete each sentence.",
                      "items": [
                          {"id": "simb1g1", "prompt": "Da bambino, ___ (io - giocare) sempre fuori.", "answers": [["giocavo"]], "explanation": "Habitual past action → imperfetto."},
                          {"id": "simb1g2", "prompt": "Domani ___ (noi - partire) presto.", "answers": [["partiremo"]], "explanation": "Future plan → futuro semplice."},
                          {"id": "simb1g3", "prompt": "___ (Potere - Lei) aiutarmi, per favore? (formal)", "answers": [["Potrebbe"]], "explanation": "Polite formal request → condizionale."},
                      ]}

    b2_reading = ("<p>Il dibattito sull'intelligenza artificiale nel mondo del lavoro continua a dividere esperti e opinione "
                  "pubblica. Se da un lato si sottolineano i vantaggi in termini di efficienza, dall'altro cresce la "
                  "preoccupazione per la perdita di posti di lavoro in alcuni settori. Gli economisti concordano, "
                  "tuttavia, sul fatto che la formazione continua sarà determinante per affrontare questa transizione.</p>")
    b2_reading_ex = {"id": "sim-b2-reading", "type": "multiple-choice", "title": "CILS/CELI-Style Reading — B2", "items": [
        {"id": "simb2r1", "prompt": "What do economists agree on?", "options": ["AI should be banned", "Ongoing training will be key", "Job losses are exaggerated"], "answerIndex": 1, "explanation": "\"La formazione continua sarà determinante.\""},
    ]}
    b2_grammar_ex = {"id": "sim-b2-grammar", "type": "fill-blank", "title": "CILS/CELI-Style Grammar — B2",
                      "instructions": "Complete each sentence.",
                      "items": [
                          {"id": "simb2g1", "prompt": "Se ___ (io - avere) più tempo, studierei di più.", "answers": [["avessi"]], "explanation": "Second type hypothetical: congiuntivo imperfetto."},
                          {"id": "simb2g2", "prompt": "Dubito che loro ___ (arrivare) in tempo.", "answers": [["arrivino"]], "explanation": "Dubito che → congiuntivo presente."},
                      ]}

    exam_sections = []
    for level, reading, reading_ex, grammar_ex in [("B1", b1_reading, b1_reading_ex, b1_grammar_ex), ("B2", b2_reading, b2_reading_ex, b2_grammar_ex)]:
        exam_sections.append(f"""<section class="section section--surface" aria-labelledby="sim-{level}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level} &middot; Comprensione della Lettura</p>
                <h2 id="sim-{level}-heading">Simulated {level} Exam</h2>
                <div class="card"><div class="prose">{reading}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(reading_ex)}</div>
                <div style="margin-top:var(--space-md);">{ex_block(grammar_ex)}</div>
            </div>
        </section>""")

    write_page("simulated-exams.html", "Simulated Exams — Renan the Teacher Italian Course",
               "CILS/CELI/PLIDA-style practice exam sections in Italian, with reading comprehension and grammar, plus answer keys.",
               [header, intro] + exam_sections, active_top="exams", breadcrumb_label="Simulated Exams",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


if __name__ == "__main__":
    build_index()
    build_exercises()
    build_extras()
    build_dictionary()
    build_irregular_verbs()
    build_placement_test()
    build_progress()
    build_today_review()
    build_simulated_exams()
