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
                    <h1>Benvenuti al corso d'italiano del maestro Renan</h1>
                    <p class="hero__lede">Un'accademia di grammatica, vocabolario ed esercizi d'italiano allineata al QCER &mdash; spiegazioni in inglese, esempi in vero italiano.<br>Buon lavoro!</p>
                    <div class="hero__actions">
                        <a class="btn btn--accent" href="levels/a1.html">Inizia con A1 {ARROW}</a>
                        <a class="btn btn--ghost-inverse" href="placement-test.html">Qual è il mio livello?</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <hr class="rule">"""

    level_grammar = {
        "A1": ["Essere &amp; avere", "Genere &amp; articoli", "Presente indicativo (-are/-ere/-ire)", "Domande &amp; c'è/ci sono"],
        "A2": ["Verbi irregolari al presente", "Passato prossimo", "Verbi riflessivi", "Pronomi diretti"],
        "B1": ["Imperfetto vs. passato prossimo", "Pronomi indiretti &amp; combinati", "Futuro &amp; condizionale", "Imperativo, ci &amp; ne"],
        "B2": ["Trapassato prossimo", "Congiuntivo (presente &amp; imperfetto)", "Periodo ipotetico I/II", "Passivo &amp; discorso indiretto"],
        "C1": ["Congiuntivo trapassato", "Periodo ipotetico III", "Gerundio &amp; progressivo", "Registro &amp; connettivi"],
        "C2": ["Sintassi complessa", "Registro letterario", "Sfumature lessicali", "Coesione testuale"],
    }
    cards = []
    for i, (code, topics) in enumerate(level_grammar.items()):
        roman = ["I", "II", "III", "IV", "V", "VI"][i]
        items = "".join(f"<li>{t}</li>" for t in topics)
        level_name = {c: n for c, n, s in site_chrome.LEVELS}[code]
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{roman}</span>
            <h3>{code} &mdash; {level_name}</h3>
            <ul style="color:var(--color-text-muted);font-size:var(--step--1);padding-left:1.1em;list-style:disc;display:flex;flex-direction:column;gap:0.25em;">{items}</ul>
            <div class="lesson-card__actions"><a class="btn btn--ghost btn--small" href="levels/{code.lower()}.html">Apri {code} {ARROW}</a></div>
        </article>""")

    grammar_section = f"""<section id="grammar" class="section section--surface" aria-labelledby="grammar-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Grammatica</p>
                <h2 id="grammar-heading">Il percorso di grammatica italiana</h2>
                <p>Un percorso completo nella grammatica italiana attraverso sei livelli del QCER, dal tuo primo essere/avere al registro letterario &mdash; apri qualsiasi livello per vedere ogni argomento e iniziare a esercitarti.</p>
            </div>
            <div class="grid">{"".join(cards)}</div>
        </div>
    </section>"""

    ladder_items = []
    ladder_desc = {
        "A1": "Frasi di base ed espressioni quotidiane per i bisogni immediati.",
        "A2": "Scambi semplici e diretti su argomenti familiari e questioni di routine.",
        "B1": "Uso autonomo dell'italiano per il lavoro, lo studio e i viaggi.",
        "B2": "Interazione fluente e spontanea, con argomentazioni chiare e dettagliate.",
        "C1": "Uso flessibile ed efficace della lingua per la vita accademica e professionale.",
        "C2": "Padronanza precisa e sfumata dell'italiano in qualsiasi contesto.",
    }
    for code, name, slug in site_chrome.LEVELS:
        ladder_items.append(f"""<li class="ladder__rung">
            <span class="ladder__code" aria-hidden="true">{code}</span>
            <div class="ladder__body">
                <h3>{name}</h3>
                <p>{ladder_desc[code]} <a class="ladder__link" href="levels/{slug}.html">Entra nel livello {ARROW}</a></p>
            </div>
        </li>""")

    cefr_section = f"""<section id="about-cefr" class="section section--surface" aria-labelledby="cefr-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Il Quadro e il Tuo Percorso</p>
                <h2 id="cefr-heading">Cos'è il QCER</h2>
                <p>Il <strong>Quadro Comune Europeo di Riferimento per le lingue (QCER)</strong> è lo standard internazionale per descrivere la competenza linguistica. Organizza questo corso in sei livelli &mdash; entra in uno qualsiasi qui sotto.</p>
            </div>
            <ol class="ladder">{"".join(ladder_items)}</ol>
        </div>
    </section>"""

    skills = [
        ("Grammatica", "index.html#grammar", None, "Tempi, forme e regole strutturate, organizzate per livello del QCER e collegate a esercizi di pratica.", '<path d="M3 5.5C3 4.7 3.7 4 4.5 4H10a2 2 0 0 1 2 2v14a1.5 1.5 0 0 0-1.5-1.5H4.5A1.5 1.5 0 0 1 3 17V5.5Z"/><path d="M21 5.5c0-.8-.7-1.5-1.5-1.5H14a2 2 0 0 0-2 2v14a1.5 1.5 0 0 1 1.5-1.5h5.5a1.5 1.5 0 0 0 1.5-1.5V5.5Z"/>'),
        ("Vocabolario", None, None, "Liste di parole per argomento che si sviluppano insieme alla grammatica di ogni livello, dai primi sostantivi alle collocazioni più sfumate.", '<path d="M4 19V6.5A2.5 2.5 0 0 1 6.5 4H8"/><path d="M4 13h4"/><path d="M14 19V6.5A2.5 2.5 0 0 1 16.5 4H20"/><path d="M14 13h4"/>'),
        ("Esercizi", "exercises.html", None, "Pratica extra di lettura e vocabolario, indipendente dal livello, per qualsiasi momento.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
        ("Lettura", "exercises.html", None, "Brani e dialoghi in stile autentico che mettono in pratica grammatica e vocabolario nel contesto.", '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/>'),
        ("Ascolto", "exercises.html", None, "Trascrizioni di dialoghi e monologhi per sviluppare l'orecchio per l'italiano parlato naturale.", '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3Z"/>'),
        ("Scrittura", None, None, "Attività di scrittura guidata che crescono da semplici frasi a paragrafi argomentativi strutturati.", '<path d="M2 22c4-1 8-3 10-5"/><path d="M22 2c-8 0-16 4-16 14 0 2 2 4 4 4C20 20 22 10 22 2Z"/>'),
        ("Parlato", None, None, "Spunti di conversazione per la discussione e la pratica a ogni livello.", '<path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Z"/><path d="M19 11a7 7 0 0 1-14 0"/><path d="M12 18v3"/><path d="M9 21h6"/>'),
        ("Esami Simulati", "simulated-exams.html", None, "Sezioni di esami simulati in stile CILS/PLIDA con soluzioni, per la preparazione alle certificazioni.", '<circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/>'),
    ]
    skill_cards = []
    for name, href, _, desc, icon in skills:
        tag_open = f'<a class="skill-card" href="{href}">' if href else '<div class="skill-card">'
        tag_close = "</a>" if href else "</div>"
        skill_cards.append(f'{tag_open}<svg class="skill-card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg><h3>{name}</h3><p>{desc}</p>{tag_close}')

    skills_section = f"""<section id="skills" class="section" aria-labelledby="skills-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Un Percorso Completo</p>
                <h2 id="skills-heading">Ogni abilità, coperta</h2>
                <p>Ogni livello del QCER lavora sulle stesse abilità fondamentali, così niente è lasciato al caso.</p>
            </div>
            <div class="grid grid--4">{"".join(skill_cards)}</div>
        </div>
    </section>"""

    why_section = f"""<section id="why-us" class="section section--surface" aria-labelledby="why-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Perché Studiare con Noi</p>
                <h2 id="why-heading">Un corso costruito per essere affidabile</h2>
            </div>
            <div class="grid grid--3" style="max-width:70rem;margin:0 auto;">
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg></span>
                    <h3>Organizzato secondo il QCER</h3>
                    <p>Ogni lezione è mappata sul Quadro Comune Europeo, così sai sempre esattamente a che punto sei e cosa viene dopo.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
                    <h3>Impara al tuo ritmo</h3>
                    <p>Procedi in un livello oppure passa a esercizi, dizionario o al ripasso di oggi quando ti serve pratica extra.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 4 5.7 4 9s-1.5 6.5-4 9c-2.5-2.5-4-5.7-4-9s1.5-6.5 4-9Z"/></svg></span>
                    <h3>Costruito con italiano reale</h3>
                    <p>Esempi e dialoghi naturali, non riempitivi da manuale &mdash; e ogni punto di grammatica include gli errori più comuni a cui fare attenzione.</p>
                </div>
            </div>
        </div>
    </section>"""

    cta = f"""<section class="cta-band" aria-labelledby="cta-heading">
        {STARS_ROW}
        <p class="eyebrow" style="justify-content:center;">Pronti quando siete voi</p>
        <h2 id="cta-heading">Buon divertimento &mdash; inizia oggi con il tuo livello.</h2>
        <p>Non sai da dove cominciare? Fai il test di livello, oppure inizia semplicemente da A1 e costruisci le tue basi.</p>
        <div class="hero__actions">
            <a class="btn btn--accent" href="levels/a1.html">Esplora tutti i livelli {ARROW}</a>
            <a class="btn btn--ghost-inverse" href="placement-test.html">Qual è il mio livello?</a>
        </div>
    </section>"""

    write_page(
        "index.html",
        "Renan the Teacher — Accademia di Italiano",
        "Un corso d'italiano allineato al QCER con grammatica, vocabolario, lettura, ascolto, scrittura, parlato ed esami simulati, organizzato livello per livello da A1 a C2.",
        [hero, grammar_section, cefr_section, skills_section, why_section, cta],
        active_top="home",
        extra_scripts=[],
    )


# =======================================================================
# EXERCISES
# =======================================================================
def build_exercises():
    header = page_header("Pratica Libera", "Esercizi",
                          "Pratica extra di lettura e vocabolario, indipendente dal livello &mdash; utile in qualsiasi momento.")

    items = [
        ("A2", "Un'Email da un'Amica", "<p>Ciao Sara! Come stai? Io sto benissimo. Sabato scorso sono andata al mercato con mia madre e abbiamo comprato tantissima frutta fresca. Poi abbiamo pranzato in un piccolo bar vicino a casa nostra.</p><p>Il weekend prossimo vado al mare con alcune amiche. Non vedo l'ora! Tu cosa fai di bello questo weekend? Scrivimi presto!<br>Un abbraccio,<br>Giulia</p>",
         {"id": "ex-a2-mail", "type": "true-false", "title": "Verifica di Comprensione", "items": [
             {"id": "exa2m1", "statement": "Giulia è andata al mercato con sua madre.", "answer": True, "explanation": "«Sono andata al mercato con mia madre.»"},
             {"id": "exa2m2", "statement": "Giulia va in montagna il prossimo weekend.", "answer": False, "explanation": "Va al mare, non in montagna."},
         ]}),
        ("B1", "Un Annuncio di Lavoro", "<p><strong>Cercasi cameriere/a per ristorante nel centro di Bologna.</strong> Richiesta esperienza minima di un anno nel settore della ristorazione. Turni flessibili, anche nei weekend. Buona conoscenza dell'inglese è un plus. Stipendio commisurato all'esperienza. Per candidarsi, inviare il curriculum a info@ristorantebologna.it entro venerdì.</p>",
         {"id": "ex-b1-annuncio", "type": "multiple-choice", "title": "Verifica di Comprensione", "items": [
             {"id": "exb1a1", "prompt": "Quanta esperienza è richiesta?", "options": ["Nessuna esperienza necessaria", "Almeno un anno", "Almeno cinque anni"], "answerIndex": 1, "explanation": "«Richiesta esperienza minima di un anno.»"},
             {"id": "exb1a2", "prompt": "Cosa è considerato «un plus»?", "options": ["Avere un'automobile", "Parlare bene inglese", "Abitare vicino"], "answerIndex": 1, "explanation": "«Buona conoscenza dell'inglese è un plus.»"},
         ]}),
        ("B2", "Una Recensione di Ristorante", "<p>Ero scettico prima di prenotare, visto il gran numero di recensioni contrastanti online. Tuttavia, la mia esperienza è stata decisamente positiva. Il servizio, seppur non impeccabile, è stato cordiale, e i piatti — in particolare i primi — erano preparati con cura e ingredienti di qualità. Unica nota negativa: i tempi di attesa tra una portata e l'altra erano piuttosto lunghi.</p>",
         {"id": "ex-b2-recensione", "type": "true-false", "title": "Verifica di Comprensione", "items": [
             {"id": "exb2r1", "statement": "L'impressione generale del recensore è stata positiva.", "answer": True, "explanation": "«La mia esperienza è stata decisamente positiva.»"},
             {"id": "exb2r2", "statement": "I primi piatti sono stati indicati come il punto debole del pasto.", "answer": False, "explanation": "I primi sono stati elogiati; la critica riguardava i tempi di attesa tra le portate."},
         ]}),
        ("C1", "Un Breve Articolo su Firenze", "<p>Firenze, culla del Rinascimento, continua ad attirare ogni anno milioni di visitatori, attratti tanto dal suo inestimabile patrimonio artistico quanto dall'atmosfera unica dei suoi vicoli storici. Nonostante le sfide poste dal turismo di massa — dalla gestione dei flussi alla tutela del centro storico — la città ha saputo, negli ultimi anni, sviluppare politiche di valorizzazione più sostenibili, incoraggiando i visitatori a esplorare anche i quartieri meno battuti.</p>",
         {"id": "ex-c1-firenze", "type": "multiple-choice", "title": "Verifica di Comprensione", "items": [
             {"id": "exc1f1", "prompt": "Quale sfida menziona l'articolo?", "options": ["La mancanza di monumenti storici", "La gestione del turismo di massa", "La carenza di ristoranti"], "answerIndex": 1, "explanation": "«Le sfide poste dal turismo di massa» viene menzionato direttamente."},
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

    write_page("exercises.html", "Esercizi — Corso d'Italiano di Renan the Teacher",
               "Pratica extra di lettura e vocabolario in italiano, indipendente dal livello, con correzione immediata.",
               sections, active_top="exercises", breadcrumb_label="Esercizi",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# EXTRAS
# =======================================================================
def build_extras():
    header = page_header("Oltre la Grammatica", "Extra",
                          "Espressioni comuni, italiano formale e informale, situazioni quotidiane e brevi note di cultura.")

    expressions = [
        ("Certo!", "Sure! / Of course!", "Un modo rapido e cordiale per dire di essere d'accordo."),
        ("Magari!", "If only! / I wish!", "Anche come genuina espressione di speranza, usata da sola."),
        ("Boh.", "I have no idea. (shrug)", "Molto comune e informale — accompagnata da un'alzata di spalle."),
        ("Dai!", "Come on!", "Incoraggiamento, lieve protesta o impazienza, a seconda del tono."),
        ("Che ne so.", "How should I know.", "Informale, leggermente sbrigativa."),
        ("In bocca al lupo!", "Good luck! (lett. \"in bocca al lupo\")", "La risposta tradizionale è Crepi!, mai grazie."),
        ("Non vedo l'ora!", "I can't wait!", "Letteralmente \"non vedo l'ora [che arrivi]\"."),
        ("Fa niente.", "It's nothing / no worries.", "Un modo informale per minimizzare una scusa."),
        ("Meno male!", "Thank goodness!", "Sollievo per come sono andate le cose."),
        ("Che macello!", "What a mess! (colloquial)", "Solo registro informale."),
    ]
    exp_rows = "".join(f"<tr><td><strong>{esc(it)}</strong></td><td>{esc(en)}</td><td>{esc(note)}</td></tr>" for it, en, note in expressions)

    expressions_section = f"""<section id="expressions" class="section section--surface" aria-labelledby="expr-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Per Suonare Più Naturale</p>
                <h2 id="expr-heading">Espressioni Comuni</h2>
                <p>Frasi brevi e frequenti che fanno suonare il tuo italiano naturale, non da manuale.</p>
            </div>
            <div class="table-scroll"><table class="ref-table"><thead><tr><th>Italiano</th><th>Inglese</th><th>Nota</th></tr></thead><tbody>{exp_rows}</tbody></table></div>
        </div>
    </section>"""

    formal_informal = f"""<section id="formal-informal" class="section section--tight" aria-labelledby="fi-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Registro</p>
                <h2 id="fi-heading">Italiano Formale e Informale</h2>
                <p>Scegliere tra tu e Lei è solo l'inizio &mdash; la formalità attraversa anche il vocabolario e le espressioni.</p>
            </div>
            <div class="grid grid--2">
                <div class="card">
                    <h3>Informale (tu)</h3>
                    <ul class="rules-list">
                        <li>Ciao, come stai?</li>
                        <li>Scusa, hai un minuto?</li>
                        <li>Puoi aiutarmi?</li>
                        <li>Ti volevo chiedere una cosa.</li>
                        <li>A presto! / Ci vediamo!</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Formale (Lei)</h3>
                    <ul class="rules-list">
                        <li>Buongiorno, come sta?</li>
                        <li>Mi scusi, avrebbe un minuto?</li>
                        <li>Potrebbe aiutarmi?</li>
                        <li>Volevo chiederLe una cosa.</li>
                        <li>Cordiali saluti / ArrivederLa</li>
                    </ul>
                </div>
            </div>
            <div class="notice mt-lg"><strong>Regola pratica</strong><p>Usa Lei con sconosciuti, persone più anziane, funzionari e in qualsiasi contesto professionale — finché non ti invitano a passare al tu (<em>diamoci del tu</em>).</p></div>
        </div>
    </section>"""

    everyday = f"""<section id="everyday" class="section section--surface" aria-labelledby="everyday-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Situazioni Reali</p>
                <h2 id="everyday-heading">Italiano di Tutti i Giorni</h2>
                <p>Scambi brevi e pratici per situazioni che incontrerai davvero.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Al bar</h3>
                    <p><em>Un caffè al banco, per favore.</em><br>(A coffee at the counter, please.)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">In molti bar italiani si paga prima alla cassa, poi si porta lo scontrino al bancone.</p>
                </div>
                <div class="card">
                    <h3>Al mercato</h3>
                    <p><em>Quanto costano queste mele?</em><br>(How much do these apples cost?)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">I venditori spesso ti lasciano scegliere da solo/a la merce — basta chiedere prima: <em>Posso scegliere io?</em></p>
                </div>
                <div class="card">
                    <h3>Fare quattro chiacchiere</h3>
                    <p><em>Che caldo/freddo oggi, eh?</em><br>(It's so hot/cold today, huh?)</p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">Il tempo atmosferico è un argomento sicuro e universale per rompere il ghiaccio, proprio come in inglese.</p>
                </div>
            </div>
        </div>
    </section>"""

    culture = f"""<section id="culture" class="section section--tight" aria-labelledby="culture-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Note Culturali</p>
                <h2 id="culture-heading">La Cultura Italiana in Breve</h2>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Le regole del caffè</h3>
                    <p>Il cappuccino è una bevanda da colazione — ordinarne uno dopo un pasto (specialmente dopo mezzogiorno) susciterà uno sguardo perplesso ma bonario dalla maggior parte degli italiani. L'espresso, invece, va bene in qualsiasi momento.</p>
                </div>
                <div class="card">
                    <h3>Gli orari dei pasti</h3>
                    <p>Il pranzo è spesso il pasto principale, di solito tra l'una e le due; la cena è generalmente più tardi che in molti altri paesi, spesso dalle otto in poi, specialmente al sud.</p>
                </div>
                <div class="card">
                    <h3>L'orgoglio regionale</h3>
                    <p>L'Italia si è unificata politicamente solo nel 1861, e l'identità regionale resta forte: il cibo, il dialetto e persino il modo in cui si prepara "la vera" pizza o "il vero" piatto di pasta possono essere oggetto di un dibattito locale davvero acceso.</p>
                </div>
            </div>
        </div>
    </section>"""

    write_page("extras.html", "Extra — Corso d'Italiano di Renan the Teacher",
               "Espressioni comuni, italiano formale e informale, situazioni quotidiane e brevi note di cultura italiana.",
               [header, expressions_section, formal_informal, everyday, culture],
               active_top="extras", breadcrumb_label="Extra", extra_css=["lessons"])


# =======================================================================
# DICTIONARY — monolingual Italian (definitions of Italian words, in
# Italian). No Italian<->English bilingual sources here on purpose: see
# assets/js/dict-widget.js and dictionary.js for the live lookup, which
# queries Italian Wiktionary (it.wiktionary.org) rather than an
# Italian-English one, for the same reason.
# =======================================================================
def dict_card(name, desc, url_tmpl, sample_word, featured=True):
    cls = "card card--feature dict-card" if featured else "card dict-card"
    btn_cls = "btn btn--accent btn--small dict-card__link" if featured else "btn btn--accent btn--small dict-card__link"
    sample_url = url_tmpl.replace("{word}", sample_word)
    return f"""<div class="{cls}" data-url-template="{url_tmpl}">
        <h3>{esc(name)}</h3>
        <p>{esc(desc)}</p>
        <div class="card__foot">
            <a class="{btn_cls}" data-dict-link href="{sample_url}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>Consulta</a>
        </div>
    </div>"""


def build_dictionary():
    header = page_header("Dizionario e Riferimenti", "Cerca Qualsiasi Parola Italiana",
                          "Digita una parola e aprila direttamente in uno di questi dizionari monolingui italiani, oppure usa gli strumenti di pronuncia qui sotto.")

    input_section = f"""<section class="section section--surface" aria-labelledby="primary-dict-heading">
        <div class="section__inner">
            <h2 id="primary-dict-heading" class="visually-hidden">Dizionari Principali</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-lg);">
                <label for="dict-word" class="eyebrow" style="margin-bottom:0.6em;display:block;">La tua parola</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="dict-word" class="dict-input" placeholder="Digita una parola, es. &ldquo;magari&rdquo;" autocomplete="off" data-dict-word>
                </div>
                <p class="notice mt-lg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Ogni scheda qui sotto si aggiorna mentre digiti. Premi Invio per aprire a caso uno dei quattro dizionari principali.</p>
            </div>
            <div class="grid">
                {dict_card("Treccani — Vocabolario", "Il dizionario monolingue ed enciclopedia più autorevole d'Italia — ideale per definizioni precise in italiano.", "https://www.treccani.it/vocabolario/ricerca/{word}/", "magari")}
                {dict_card("Garzanti Linguistica", "Un dizionario italiano affidabile e diffuso, con definizioni chiare in italiano.", "https://www.garzantilinguistica.it/ricerca/?q={word}", "magari")}
                {dict_card("Wikizionario", "L'edizione italiana di Wiktionary — definizioni in italiano, etimologia e note d'uso regionali.", "https://it.wiktionary.org/wiki/{word}", "magari")}
                {dict_card("Sapere.it — Sinonimi e Contrari", "Dizionario italiano di sinonimi e contrari, utile per ampliare il tuo vocabolario.", "https://www.sapere.it/sapere/strumenti/dizionario-sinonimi-contrari/ricerca/{word}.html", "magari")}
            </div>
        </div>
    </section>"""

    more_section = f"""<section class="section" aria-labelledby="more-dict-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Se Ti Serve di Più</p>
                <h2 id="more-dict-heading">Altri Strumenti e Pronuncia</h2>
                <p>Per sentire una parola pronunciata da madrelingua o consultare le coniugazioni verbali complete.</p>
            </div>
            <div class="grid">
                {dict_card("Forvo", "Pronunce di madrelingua italiani, raccolte dalla community di tutto il mondo.", "https://forvo.com/word/{word}/#it", "magari", featured=False)}
                {dict_card("Conjugare.it", "Tabelle di coniugazione complete per qualsiasi verbo italiano, in ogni tempo e modo.", "https://www.conjugare.it/{word}", "parlare", featured=False)}
            </div>
        </div>
    </section>"""

    write_page("dictionary.html", "Dizionario e Riferimenti — Corso d'Italiano di Renan the Teacher",
               "Cerca qualsiasi parola italiana su Treccani, Garzanti, Wikizionario e altri dizionari monolingui, con strumenti di pronuncia.",
               [header, input_section, more_section],
               active_top="dictionary", breadcrumb_label="Dizionario e Riferimenti",
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
    header = page_header("Riferimenti", "Verbi Irregolari Italiani",
                          "I verbi irregolari più comuni, con presente indicativo (io), participio passato e ausiliare &mdash; digita per filtrare.")

    rows = "".join(
        f"<tr><td><strong>{esc(inf)}</strong></td><td>{esc(meaning)}</td><td>{esc(pres)}</td><td>{esc(part)}</td><td class=\"text-muted\">{esc(aux)}</td></tr>"
        for inf, meaning, pres, part, aux in IRREGULAR_VERBS
    )

    section = f"""<section class="section section--surface" aria-labelledby="verbs-heading">
        <div class="section__inner">
            <h2 id="verbs-heading" class="visually-hidden">Verbi Irregolari</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-md);">
                <label for="verb-filter" class="eyebrow" style="margin-bottom:0.6em;display:block;">Filtra</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="verb-filter" class="dict-input" placeholder="Digita per filtrare, es. &ldquo;prendere&rdquo; o &ldquo;essere&rdquo;" autocomplete="off" data-verb-filter>
                </div>
                <p class="notice mt-lg" data-verb-count><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Mostrati tutti i {len(IRREGULAR_VERBS)} verbi. I verbi con un asterisco (*) prendono essere o avere a seconda che siano usati con un complemento oggetto diretto.</p>
                <p class="notice mt-lg" data-verb-empty hidden>Nessun verbo corrisponde a &ldquo;<span data-verb-empty-term></span>&rdquo;.</p>
            </div>
            <div class="table-scroll">
                <table class="ref-table">
                    <caption>Verbi irregolari italiani comuni</caption>
                    <thead><tr><th>Infinito</th><th>Significato</th><th>Presente (io)</th><th>Participio Passato</th><th>Ausiliare</th></tr></thead>
                    <tbody data-verb-tbody>{rows}</tbody>
                </table>
            </div>
        </div>
    </section>"""

    write_page("irregular-verbs.html", "Verbi Irregolari Italiani — Corso d'Italiano di Renan the Teacher",
               "Tabella di riferimento dei verbi irregolari italiani più comuni: presente, participio passato e ausiliare, con filtro in tempo reale.",
               [header, section], active_top="extras", breadcrumb_label="Verbi Irregolari",
               extra_css=["lessons"], extra_scripts=["irregular-verbs.js"])


# =======================================================================
# PLACEMENT TEST
# =======================================================================
def build_placement_test():
    header = page_header("Trova il Tuo Livello", "Test di Livello",
                          "24 domande, circa due per livello da A1 a C2. Rispondi a quante più puoi &mdash; il tuo istinto su dove inizia a diventare difficile è la migliore guida per il tuo livello.")

    blocks = [
        ("A1", [
            {"id": "pt-a1-1", "prompt": "Io ___ italiano.", "options": ["sono", "è", "sei"], "answerIndex": 0, "explanation": "Io + essere = sono."},
            {"id": "pt-a1-2", "prompt": "___ un libro sul tavolo. (c'è)", "options": ["C'è", "Ci sono", "È"], "answerIndex": 0, "explanation": "Sostantivo singolare → c'è."},
            {"id": "pt-a1-3", "prompt": "Ho ___ anni. (ho vent'anni)", "options": ["sono venti", "venti", "vent'anni"], "answerIndex": 2, "explanation": "L'età si esprime con avere + [numero] anni."},
            {"id": "pt-a1-4", "prompt": "___ amica (l'amica, f.)", "options": ["La", "L'", "Lo"], "answerIndex": 1, "explanation": "Davanti a una vocale, la si accorcia in l'."},
        ]),
        ("A2", [
            {"id": "pt-a2-1", "prompt": "Ieri ___ (io - mangiare) la pizza.", "options": ["ho mangiato", "mangio", "mangiavo"], "answerIndex": 0, "explanation": "Un singolo evento passato concluso → passato prossimo."},
            {"id": "pt-a2-2", "prompt": "Maria ___ (arrivare) tardi.", "options": ["ha arrivato", "è arrivata", "è arrivato"], "answerIndex": 1, "explanation": "Arrivare prende essere, con accordo al femminile per Maria."},
            {"id": "pt-a2-3", "prompt": "Mi ___ (svegliarsi) alle sette.", "options": ["sveglio", "svegli", "mi sveglio"], "answerIndex": 2, "explanation": "Il verbo riflessivo richiede il pronome mi."},
            {"id": "pt-a2-4", "prompt": "Roma è più grande ___ Firenze.", "options": ["che", "di", "come"], "answerIndex": 1, "explanation": "Nel confronto tra due sostantivi si usa di."},
        ]),
        ("B1", [
            {"id": "pt-b1-1", "prompt": "___ (Piovere) quando siamo usciti.", "options": ["È piovuto", "Pioveva", "Piove"], "answerIndex": 1, "explanation": "Sfondo meteorologico → imperfetto."},
            {"id": "pt-b1-2", "prompt": "___ scrivo un'email a Marco. (a lui)", "options": ["Gli", "Le", "Lo"], "answerIndex": 0, "explanation": "Pronome indiretto per «a lui» → gli."},
            {"id": "pt-b1-3", "prompt": "___ (Volere - io) un caffè, per favore. (forma cortese)", "options": ["Voglio", "Vorrei", "Volevo"], "answerIndex": 1, "explanation": "Il condizionale di cortesia è vorrei."},
            {"id": "pt-b1-4", "prompt": "Vai in Italia? Sì, ___ vado domani.", "options": ["ci", "ne", "lo"], "answerIndex": 0, "explanation": "Sostituisce un luogo → ci."},
        ]),
        ("B2", [
            {"id": "pt-b2-1", "prompt": "Penso che lui ___ (avere) ragione.", "options": ["ha", "abbia", "avesse"], "answerIndex": 1, "explanation": "Penso che richiede il congiuntivo."},
            {"id": "pt-b2-2", "prompt": "Se ___ (io - avere) più tempo, viaggerei di più.", "options": ["ho", "avessi", "avrei"], "answerIndex": 1, "explanation": "Periodo ipotetico di secondo tipo: se + congiuntivo imperfetto."},
            {"id": "pt-b2-3", "prompt": "La lettera ___ (scrivere) da Marco.", "options": ["è scritto", "è scritta", "ha scritto"], "answerIndex": 1, "explanation": "Forma passiva, il participio concorda con la lettera."},
            {"id": "pt-b2-4", "prompt": "Il libro ___ ho comprato è ottimo.", "options": ["cui", "che", "il quale"], "answerIndex": 1, "explanation": "Pronome relativo di complemento oggetto diretto → che."},
        ]),
        ("C1", [
            {"id": "pt-c1-1", "prompt": "Pensavo che tu ___ (essere) già partito.", "options": ["fossi", "sia", "eri"], "answerIndex": 0, "explanation": "Reggente al passato → congiuntivo imperfetto/trapassato (fossi = congiuntivo imperfetto di essere)."},
            {"id": "pt-c1-2", "prompt": "Se ___ (io - sapere), ti avrei chiamato.", "options": ["sapevo", "avrei saputo", "avessi saputo"], "answerIndex": 2, "explanation": "Periodo ipotetico di terzo tipo: se + congiuntivo trapassato."},
            {"id": "pt-c1-3", "prompt": "Sto ___ (leggere) un libro interessante.", "options": ["leggere", "leggendo", "letto"], "answerIndex": 1, "explanation": "Forma progressiva: stare + gerundio."},
            {"id": "pt-c1-4", "prompt": "Sebbene ___ (essere) tardi, siamo usciti.", "options": ["è", "era", "fosse"], "answerIndex": 2, "explanation": "Sebbene richiede sempre il congiuntivo."},
        ]),
        ("C2", [
            {"id": "pt-c2-1", "prompt": "Quale frase usa l'inversione per dare enfasi?", "options": ["Il costo mi preoccupa.", "È il costo che mi preoccupa.", "Mi preoccupa il costo, davvero."], "answerIndex": 1, "explanation": "Questa è una frase scissa, che pone in rilievo il costo."},
            {"id": "pt-c2-2", "prompt": "Devo ___ una decisione importante.", "options": ["fare", "prendere", "dare"], "answerIndex": 1, "explanation": "Prendere una decisione è la collocazione fissa."},
            {"id": "pt-c2-3", "prompt": "«Sembra che» è tipicamente seguito da...", "options": ["l'indicativo", "il congiuntivo", "l'imperativo"], "answerIndex": 1, "explanation": "Sembra che presenta qualcosa come non del tutto certo, e richiede il congiuntivo."},
        ]),
    ]
    sections = [header]
    all_items = []
    for level, items in blocks:
        all_items.extend(items)
        sections.append(f"""<section class="section section--tight" aria-labelledby="pt-{level}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="pt-{level}-heading">Domande {level}</h2>
                {ex_block({"id": f"pt-{level.lower()}-block", "type": "multiple-choice", "title": f"Domande {level}", "items": items})}
            </div>
        </section>""")

    guide = f"""<section class="section section--surface" aria-labelledby="pt-guide-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Leggere i Risultati</p>
            <h2 id="pt-guide-heading">Cosa Significa il Tuo Punteggio</h2>
            <ul class="summary-list">
                <li>A tuo agio fino ad A1&ndash;A2, in difficoltà da B1 in poi &rarr; inizia da <a href="levels/b1.html">B1</a>.</li>
                <li>A tuo agio fino a B1, in difficoltà da B2 in poi &rarr; inizia da <a href="levels/b2.html">B2</a>.</li>
                <li>A tuo agio fino a B2, in difficoltà da C1 in poi &rarr; inizia da <a href="levels/c1.html">C1</a>.</li>
                <li>Hai sbagliato diverse domande iniziali &rarr; inizia da <a href="levels/a1.html">A1</a> e costruisci basi solide &mdash; si procede velocemente.</li>
                <li>Hai risposto correttamente a tutto, incluso C2 &rarr; ripassa le lezioni di <a href="levels/c2.html">C2</a> per rifinire, oppure esplora la pagina <a href="extras.html">Extra</a>.</li>
            </ul>
        </div>
    </section>"""
    sections.append(guide)

    write_page("placement-test.html", "Test di Livello — Corso d'Italiano di Renan the Teacher",
               "Un breve test di livello autocorretto per scoprire da quale livello del QCER iniziare il tuo percorso d'italiano.",
               sections, active_top=None, breadcrumb_label="Test di Livello",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# PROGRESS
# =======================================================================
def build_progress():
    header = page_header("Il Tuo Percorso", "I Miei Progressi",
                          "XP, serie di giorni e badge, tracciati interamente su questo dispositivo &mdash; non viene mai inviato nulla altrove.")

    section = f"""<section class="section section--surface" aria-labelledby="progress-heading">
        <div class="section__inner">
            <h2 id="progress-heading" class="visually-hidden">Progressi</h2>
            <div class="progress-panel__summary" id="progress-summary"></div>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-levels-heading">
        <div class="section__inner">
            <p class="eyebrow">Per Livello</p>
            <h2 id="progress-levels-heading">Progressi per Livello</h2>
            <div id="progress-levels"></div>
        </div>
    </section>
<section class="section section--surface" aria-labelledby="progress-badges-heading">
        <div class="section__inner">
            <p class="eyebrow">Traguardi</p>
            <h2 id="progress-badges-heading">Badge</h2>
            <ul class="badge-grid" id="progress-badges"></ul>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-reset-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Ricomincia</p>
            <h2 id="progress-reset-heading">Azzera i Progressi</h2>
            <p style="color:var(--color-text-muted);">Questo cancella i tuoi XP, la serie di giorni e i badge su questo dispositivo. Lo storico del ripasso a ripetizione dilazionata (Ripasso di Oggi) è salvato separatamente e non viene toccato.</p>
            <button type="button" class="btn btn--ghost" id="progress-reset-btn">Azzera XP e Badge</button>
        </div>
    </section>"""

    write_page("progress.html", "I Miei Progressi — Corso d'Italiano di Renan the Teacher",
               "Tieni traccia dei tuoi XP, della serie di giorni e dei badge nel corso d'italiano, salvati privatamente sul tuo dispositivo.",
               [header, section], active_top=None, breadcrumb_label="I Miei Progressi")


# =======================================================================
# TODAY'S REVIEW
# =======================================================================
def build_today_review():
    header = page_header("Ripetizione Dilazionata", "Ripasso di Oggi",
                          "Un breve ripasso quotidiano degli esercizi che hai sbagliato in passato &mdash; generato automaticamente dal tuo storico.")

    section = f"""<section class="section section--surface" aria-labelledby="review-heading">
        <div class="section__inner">
            <h2 id="review-heading" class="visually-hidden">Ripasso</h2>
            <div id="review-status-box" class="notice"><p>Caricamento del tuo ripasso in corso&hellip;</p></div>
            <div id="review-blocks" style="margin-top:var(--space-md);"></div>
        </div>
    </section>"""

    write_page("today-review.html", "Ripasso di Oggi — Corso d'Italiano di Renan the Teacher",
               "Un ripasso quotidiano a ripetizione dilazionata degli esercizi d'italiano che hai sbagliato in passato, generato automaticamente dal tuo storico.",
               [header, section], active_top=None, breadcrumb_label="Ripasso di Oggi",
               extra_css=["exercises"], extra_scripts=["exercises.js", "mastery.js", "today-review.js"])


# =======================================================================
# SIMULATED EXAMS
# =======================================================================
def build_simulated_exams():
    header = page_header("Pratica d'Esame", "Esami Simulati",
                          "Sezioni di pratica in stile degli esami di certificazione ufficiali italiani &mdash; CILS, CELI e PLIDA &mdash; con soluzioni.")

    intro = f"""<section class="section section--tight" aria-labelledby="exams-intro-heading">
        <div class="section__inner section__inner--narrow">
            <h2 id="exams-intro-heading" class="visually-hidden">Informazioni su Questi Esami</h2>
            <p style="color:var(--color-text-muted);">L'Italia ha tre principali certificazioni ufficiali di italiano come lingua straniera: <strong>CILS</strong> (Università per Stranieri di Siena), <strong>CELI</strong> (Università per Stranieri di Perugia) e <strong>PLIDA</strong> (Società Dante Alighieri). Tutte testano le stesse quattro abilità &mdash; lettura, ascolto, scrittura, parlato &mdash; ai livelli del QCER da A1 a C2. Le sezioni qui sotto sono pratica in quello stile, non prove ufficiali d'esame.</p>
        </div>
    </section>"""

    b1_reading = ("<p>Negli ultimi anni, sempre più italiani scelgono di lavorare da casa almeno un paio di giorni "
                  "alla settimana. Secondo un recente sondaggio, la maggior parte dei lavoratori si dichiara più "
                  "soddisfatta rispetto a prima, soprattutto grazie al tempo risparmiato negli spostamenti. Tuttavia, "
                  "alcuni intervistati segnalano difficoltà a separare vita privata e lavoro, lamentando giornate "
                  "lavorative più lunghe del solito.</p>")
    b1_reading_ex = {"id": "sim-b1-reading", "type": "true-false", "title": "Lettura in Stile CILS/PLIDA — B1", "items": [
        {"id": "simb1r1", "statement": "La maggior parte dei lavoratori intervistati si dichiara più soddisfatta lavorando da casa.", "answer": True, "explanation": "«La maggior parte dei lavoratori si dichiara più soddisfatta.»"},
        {"id": "simb1r2", "statement": "Nessuno ha segnalato svantaggi nel lavorare da casa.", "answer": False, "explanation": "Alcuni hanno segnalato difficoltà a separare vita privata e lavoro, e giornate lavorative più lunghe."},
    ]}
    b1_grammar_ex = {"id": "sim-b1-grammar", "type": "fill-blank", "title": "Grammatica in Stile CILS/PLIDA — B1",
                      "instructions": "Completa ogni frase.",
                      "items": [
                          {"id": "simb1g1", "prompt": "Da bambino, ___ (io - giocare) sempre fuori.", "answers": [["giocavo"]], "explanation": "Azione abituale al passato → imperfetto."},
                          {"id": "simb1g2", "prompt": "Domani ___ (noi - partire) presto.", "answers": [["partiremo"]], "explanation": "Programma futuro → futuro semplice."},
                          {"id": "simb1g3", "prompt": "___ (Potere - Lei) aiutarmi, per favore? (forma formale)", "answers": [["Potrebbe"]], "explanation": "Richiesta formale e cortese → condizionale."},
                      ]}

    b2_reading = ("<p>Il dibattito sull'intelligenza artificiale nel mondo del lavoro continua a dividere esperti e opinione "
                  "pubblica. Se da un lato si sottolineano i vantaggi in termini di efficienza, dall'altro cresce la "
                  "preoccupazione per la perdita di posti di lavoro in alcuni settori. Gli economisti concordano, "
                  "tuttavia, sul fatto che la formazione continua sarà determinante per affrontare questa transizione.</p>")
    b2_reading_ex = {"id": "sim-b2-reading", "type": "multiple-choice", "title": "Lettura in Stile CILS/CELI — B2", "items": [
        {"id": "simb2r1", "prompt": "Su cosa concordano gli economisti?", "options": ["L'IA dovrebbe essere vietata", "La formazione continua sarà determinante", "La perdita di posti di lavoro è esagerata"], "answerIndex": 1, "explanation": "«La formazione continua sarà determinante.»"},
    ]}
    b2_grammar_ex = {"id": "sim-b2-grammar", "type": "fill-blank", "title": "Grammatica in Stile CILS/CELI — B2",
                      "instructions": "Completa ogni frase.",
                      "items": [
                          {"id": "simb2g1", "prompt": "Se ___ (io - avere) più tempo, studierei di più.", "answers": [["avessi"]], "explanation": "Periodo ipotetico di secondo tipo: congiuntivo imperfetto."},
                          {"id": "simb2g2", "prompt": "Dubito che loro ___ (arrivare) in tempo.", "answers": [["arrivino"]], "explanation": "Dubito che → congiuntivo presente."},
                      ]}

    exam_sections = []
    for level, reading, reading_ex, grammar_ex in [("B1", b1_reading, b1_reading_ex, b1_grammar_ex), ("B2", b2_reading, b2_reading_ex, b2_grammar_ex)]:
        exam_sections.append(f"""<section class="section section--surface" aria-labelledby="sim-{level}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level} &middot; Comprensione della Lettura</p>
                <h2 id="sim-{level}-heading">Esame Simulato {level}</h2>
                <div class="card"><div class="prose">{reading}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(reading_ex)}</div>
                <div style="margin-top:var(--space-md);">{ex_block(grammar_ex)}</div>
            </div>
        </section>""")

    write_page("simulated-exams.html", "Esami Simulati — Corso d'Italiano di Renan the Teacher",
               "Sezioni di esami simulati in stile CILS/CELI/PLIDA in italiano, con comprensione della lettura e grammatica, più soluzioni.",
               [header, intro] + exam_sections, active_top="exams", breadcrumb_label="Esami Simulati",
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
