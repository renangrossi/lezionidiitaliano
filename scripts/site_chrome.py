"""
Shared page chrome (head/header/nav/search-overlay/footer) for every page
on the Italian course. This is the sister module to the English course's
scripts/site_chrome.py, adapted in four structural ways beyond the
obvious rebrand:

  1. No AI Teacher panel/button — omitted sitewide (needs a Cloudflare
     Worker + API key the Italian project doesn't have yet).
  2. No Pre-A1 level — this course ships six levels, A1 through C2.
  3. EVERY page on this site (not just generated lesson pages) is built
     through this module, including the homepage and every standalone
     page (exercises, dictionary, extras, placement test, progress,
     today's review, irregular verbs, simulated exams, level hubs). The
     English site hand-duplicated the full header/footer markup into
     nine separate hand-written HTML files, which is real duplication
     risk (nine places to update if the brand or nav ever changes) —
     here every page is generated, so there is exactly one copy of the
     chrome markup, in this file.
  4. The interface language is Italian (lang="it"): every piece of site
     chrome — nav, buttons, search, the dictionary widget, the footer —
     is in Italian, since this is now a fully localized Italian product,
     not an English shell around Italian lesson content. Only the
     lesson/exercise *content* itself stays bilingual where that's
     pedagogically the point (see curriculum_source/*.py).

REL is the relative path prefix from the generated file back to the repo
root, e.g. "" for top-level pages, "levels/" for levels/{level}.html, and
"../../" for levels/{level}/{lesson}.html.
"""

LEVELS = [
    ("A1", "Principiante", "a1"),
    ("A2", "Elementare", "a2"),
    ("B1", "Intermedio", "b1"),
    ("B2", "Intermedio Superiore", "b2"),
    ("C1", "Avanzato", "c1"),
    ("C2", "Padronanza", "c2"),
]

BRAND_MARK_SVG = (
    '<svg class="brand__mark" viewBox="0 0 40 40" aria-hidden="true">'
    '<circle cx="20" cy="20" r="18.4" fill="none" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M13 27c1.6-6.4 3.2-11.6 7-15.8 3.8 4.2 5.4 9.4 7 15.8-2.3-1.7-4.7-2.5-7-2.5s-4.7.8-7 2.5Z" fill="currentColor"/>'
    "</svg>"
)

STAR = '<svg class="stars-row__star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21Z"/></svg>'
STARS_ROW = f'<div class="stars-row stars-row--onlight" aria-hidden="true">{STAR * 11}</div>'
STARS_ROW_GOLD = f'<div class="stars-row stars-row--gold" aria-hidden="true">{STAR * 11}</div>'
CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>'
ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>'


def nav_levels_html(rel, active_level_code):
    items = []
    for code, name, slug in LEVELS:
        current = ' aria-current="page"' if code.upper() == (active_level_code or "").upper() else ""
        items.append(
            f'<li><a href="{rel}levels/{slug}.html"{current}><span>{name}</span>'
            f'<span class="level-code">{code}</span></a></li>'
        )
    return "".join(items)


def head(rel, title, description, extra_css=None):
    extra = "".join(f'<link rel="stylesheet" href="{rel}assets/css/{c}.css">' for c in (extra_css or []))
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Renan the Teacher — Accademia di Italiano">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="icon" href="{rel}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/css/tokens.css">
<link rel="stylesheet" href="{rel}assets/css/base.css">
<link rel="stylesheet" href="{rel}assets/css/components.css">
<link rel="stylesheet" href="{rel}assets/css/layout.css">
<link rel="stylesheet" href="{rel}assets/css/dark-mode.css">
<link rel="stylesheet" href="{rel}assets/css/search.css">{extra}
<script>
(function(){{try{{var t=localStorage.getItem('theme');if(!t){{t=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}}document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();
</script>
</head>"""


def header(rel, active_level_code, breadcrumb_html=None, active_top=None):
    breadcrumb = (
        f"""<nav class="breadcrumbs" aria-label="Percorso di navigazione">
        <ol>
        {breadcrumb_html}
        </ol>
    </nav>"""
        if breadcrumb_html
        else ""
    )

    def top(label, href_suffix, id_=None):
        current = ' aria-current="page"' if id_ and id_ == active_top else ""
        return f'<li><a href="{rel}{href_suffix}"{current}>{label}</a></li>'

    return f"""<body class="" data-level-code="{active_level_code or ''}">
    <a class="skip-link" href="#main-content">Vai al contenuto</a>
    <header class="site-header">
        <div class="site-header__bar">
            <a class="brand" href="{rel}index.html">
                {BRAND_MARK_SVG}
                <span class="brand__text">
                    <span class="brand__name">Renan the Teacher</span>
                    <span class="brand__tagline">Accademia di Italiano</span>
                </span>
            </a>
            <nav class="primary-nav" id="primary-nav" role="navigation" aria-label="Navigazione principale">
                <ul class="primary-nav__list">
                {top("Home", "index.html", "home")}
                {top("Grammatica", "index.html#grammar", "grammar")}
                <li class="nav-drop">
                    <button type="button" class="nav-drop__toggle" aria-haspopup="true" aria-expanded="false">
                        Livelli <span class="nav-drop__caret" aria-hidden="true"></span>
                    </button>
                    <ul class="nav-drop__menu" role="menu">
                    {nav_levels_html(rel, active_level_code)}
                    </ul>
                </li>
                {top("Esercizi", "exercises.html", "exercises")}
                {top("Esami Simulati", "simulated-exams.html", "exams")}
                {top("Extra", "extras.html", "extras")}
                {top("Dizionario", "dictionary.html", "dictionary")}
                </ul>
            </nav>
            <div class="nav-utility">
                <button type="button" class="theme-toggle" data-search-toggle aria-label="Cerca nel sito" aria-haspopup="dialog">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                </button>
                <button type="button" class="theme-toggle" data-theme-toggle aria-label="Passa alla modalità scura">
                    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
                    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
                </button>
                <button type="button" class="nav-toggle" data-nav-toggle aria-label="Apri il menu" aria-expanded="false" aria-controls="primary-nav">
                    <span class="nav-toggle__icon"></span>
                </button>
            </div>
        </div>
    </header>
    <div class="search-overlay" data-search-overlay hidden>
        <div class="search-modal" role="dialog" aria-modal="true" aria-label="Ricerca nel sito" data-index-src="{rel}assets/data/search-index.json">
            <div class="search-modal__bar">
                <svg class="search-modal__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                <input type="search" class="search-modal__input" data-search-input placeholder="Cerca lezioni, grammatica, vocabolario, esercizi&hellip;" aria-label="Cerca">
                <button type="button" class="search-modal__close" data-search-close aria-label="Chiudi la ricerca"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg></button>
            </div>
            <div class="search-modal__results" data-search-results>
                <p class="search-modal__hint">Digita almeno 2 caratteri per cercare in ogni livello, lezione, argomento grammaticale ed esercizio.</p>
            </div>
        </div>
    </div>
    {breadcrumb}
    <main id="main-content" class="site-main">"""


def footer(rel, extra_scripts=None):
    extra = "".join(f'<script src="{rel}assets/js/{s}"></script>' for s in (extra_scripts or []))
    return f"""<button type="button" class="dict-widget-toggle" data-dict-widget-toggle aria-label="Apri il dizionario rapido" aria-expanded="false" aria-haspopup="dialog">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/></svg>
    </button>
    <div class="dict-widget-panel" data-dict-widget-panel hidden>
        <div class="dict-widget__bar">
            <input type="text" data-dict-widget-input placeholder="Cerca una parola italiana…" aria-label="Cerca una parola italiana">
            <button type="button" class="dict-widget__close" data-dict-widget-close aria-label="Chiudi il dizionario"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg></button>
        </div>
        <div class="dict-widget__result" data-dict-widget-result>
            <p class="dict-widget__hint">Digita una parola italiana per vederne il significato senza lasciare questa pagina.</p>
        </div>
        <div class="dict-widget__links" data-dict-widget-links></div>
    </div>
    </main>
    <footer class="site-footer">
        <div class="site-footer__inner">
            <div>
                <a class="brand" href="{rel}index.html">
                    {BRAND_MARK_SVG}
                    <span class="brand__text">
                        <span class="brand__name">Renan the Teacher</span>
                        <span class="brand__tagline">Accademia di Italiano</span>
                    </span>
                </a>
                <p class="site-footer__blurb">Un corso d'italiano allineato al QCER, costruito una lezione onesta e curata alla volta &mdash; dal tuo primo &ldquo;ciao&rdquo; alla vera fluidità.</p>
            </div>
            <div class="footer-col">
                <h4>Livelli</h4>
                <ul>
                    <li><a href="{rel}levels/a1.html">A1 &mdash; Principiante</a></li>
                    <li><a href="{rel}levels/a2.html">A2 &mdash; Elementare</a></li>
                    <li><a href="{rel}levels/b1.html">B1 &mdash; Intermedio</a></li>
                    <li><a href="{rel}levels/b2.html">B2 &mdash; Intermedio Superiore</a></li>
                    <li><a href="{rel}levels/c1.html">C1 &mdash; Avanzato</a></li>
                    <li><a href="{rel}levels/c2.html">C2 &mdash; Padronanza</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Esercitati</h4>
                <ul>
                    <li><a href="{rel}index.html#grammar">Percorso di Grammatica</a></li>
                    <li><a href="{rel}exercises.html">Lettura ed Esercizi</a></li>
                    <li><a href="{rel}simulated-exams.html">Esami Simulati</a></li>
                    <li><a href="{rel}dictionary.html">Dizionario e Riferimenti</a></li>
                    <li><a href="{rel}irregular-verbs.html">Verbi Irregolari</a></li>
                    <li><a href="{rel}extras.html">Extra</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>I Tuoi Progressi</h4>
                <ul>
                    <li><a href="{rel}placement-test.html">Test di Livello</a></li>
                    <li><a href="{rel}progress.html">I Miei Progressi</a></li>
                    <li><a href="{rel}today-review.html">Ripasso di Oggi</a></li>
                    <li><a href="{rel}index.html#about-cefr">Cos'è il QCER?</a></li>
                </ul>
            </div>
        </div>
        <div class="site-footer__bottom">
            <p>&copy; 2026 Renan the Teacher &mdash; Corso d'Italiano. Tutti i diritti riservati.</p>
        </div>
    </footer>
    <button type="button" class="back-to-top back-to-top--with-dict" data-back-to-top aria-label="Torna su">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>
    </button>
    <script src="{rel}assets/js/main.js"></script>
    <script src="{rel}assets/js/search.js"></script>
    <script src="{rel}assets/js/dict-widget.js"></script>
    <script src="{rel}assets/js/progress.js"></script>{extra}
</body>
</html>
"""
