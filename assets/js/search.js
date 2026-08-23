/*!
 * Renan the Teacher — Site Search (Italian course)
 * ------------------------------------------------------------------
 * Lightweight, static-site-friendly search. Fetches a small prebuilt
 * JSON index (assets/data/search-index.json) once, then filters it
 * entirely in the browser — no backend, no build-time search server,
 * fast even on a few hundred entries.
 */
(function () {
  "use strict";

  var overlay = document.querySelector("[data-search-overlay]");
  if (!overlay) return;
  var modal = overlay.querySelector(".search-modal");
  var input = overlay.querySelector("[data-search-input]");
  var resultsBox = overlay.querySelector("[data-search-results]");
  var closeBtn = overlay.querySelector("[data-search-close]");
  var openBtn = document.querySelector("[data-search-toggle]");
  var indexSrc = modal.getAttribute("data-index-src");
  var root = indexSrc.replace("assets/data/search-index.json", "");

  var indexData = null;
  var indexPromise = null;
  var lastFocused = null;
  var activeIndex = -1;

  var TYPE_LABEL = {
    level: "Livello QCER",
    lesson: "Lezione Interattiva",
    grammar: "Argomento Grammaticale",
    booklet: "Dispensa di Grammatica",
    exercise: "Esercizio / Testo",
    mock: "Esame Simulato",
    extra: "Extra",
  };

  function loadIndex() {
    if (indexPromise) return indexPromise;
    indexPromise = fetch(indexSrc)
      .then(function (res) {
        if (!res.ok) throw new Error("index fetch failed: " + res.status);
        return res.json();
      })
      .then(function (data) {
        indexData = data;
        return data;
      })
      .catch(function (err) {
        indexData = [];
        if (window.console) console.error("Search index failed to load", err);
        resultsBox.innerHTML =
          '<p class="search-modal__hint">Impossibile caricare l\u2019indice di ricerca. Se stai visualizzando questa pagina come file locale ' +
          "(un indirizzo che inizia con <code>file://</code>), \u00e8 normale \u2014 i browser bloccano questo tipo di richiesta per i file locali. " +
          "Avvia un server locale (es. <code>python3 -m http.server</code> nella cartella del sito) oppure visita il sito online.</p>";
        return [];
      });
    return indexPromise;
  }

  function norm(s) {
    return String(s || "").toLowerCase();
  }

  function score(entry, q) {
    var title = norm(entry.title);
    var desc = norm(entry.desc);
    var level = norm(entry.level);
    var type = norm(entry.type);
    if (title === q) return 100;
    if (title.indexOf(q) === 0) return 90;
    if (title.indexOf(q) !== -1) return 70;
    if (level === q) return 60;
    if (type.indexOf(q) !== -1) return 40;
    // Optional curated synonyms/topics an entry doesn't otherwise
    // mention by name in its title (e.g. Extras' "Mirage News Network"
    // is findable via "AI" or "news", not just "mirage") — see
    // assets/data/search-index.json's "keywords" arrays.
    if ((entry.keywords || []).some(function (k) { return norm(k).indexOf(q) !== -1; })) return 35;
    if (desc.indexOf(q) !== -1) return 20;
    return 0;
  }

  function runSearch(query) {
    var q = norm(query).trim();
    if (q.length < 2) {
      resultsBox.innerHTML = '<p class="search-modal__hint">Digita almeno 2 caratteri per cercare in ogni livello, lezione, argomento grammaticale, esercizio ed esame simulato.</p>';
      activeIndex = -1;
      return;
    }
    var scored = (indexData || [])
      .map(function (e) {
        return { entry: e, s: score(e, q) };
      })
      .filter(function (r) {
        return r.s > 0;
      })
      .sort(function (a, b) {
        return b.s - a.s;
      })
      .slice(0, 40);

    if (!scored.length) {
      resultsBox.innerHTML = '<p class="search-modal__hint">Nessun risultato per &ldquo;' + escapeHtml(query) + '&rdquo;. Prova con un\'altra parola, oppure sfoglia i livelli nel menu.</p>';
      activeIndex = -1;
      return;
    }

    var html = '<ul class="search-results" role="listbox">';
    scored.forEach(function (r, i) {
      var e = r.entry;
      var typeLabel = TYPE_LABEL[e.type] || e.type;
      var levelBadge = e.level ? '<span class="search-result__level">' + escapeHtml(e.level) + "</span>" : "";
      html +=
        '<li role="option" id="search-result-' + i + '">' +
        '<a class="search-result" href="' + root + e.url + '">' +
        '<span class="search-result__main">' +
        "<span class=\"search-result__title\">" + highlight(e.title, q) + "</span>" +
        '<span class="search-result__desc">' + escapeHtml(e.desc || "") + "</span>" +
        "</span>" +
        '<span class="search-result__meta">' + levelBadge + '<span class="search-result__type">' + escapeHtml(typeLabel) + "</span></span>" +
        "</a></li>";
    });
    html += "</ul>";
    resultsBox.innerHTML = html;
    activeIndex = -1;
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = String(s || "");
    return d.innerHTML;
  }

  function highlight(title, q) {
    var safe = escapeHtml(title);
    var idx = norm(title).indexOf(q);
    if (idx === -1) return safe;
    var before = escapeHtml(title.slice(0, idx));
    var match = escapeHtml(title.slice(idx, idx + q.length));
    var after = escapeHtml(title.slice(idx + q.length));
    return before + "<mark>" + match + "</mark>" + after;
  }

  function openSearch() {
    lastFocused = document.activeElement;
    overlay.hidden = false;
    document.body.style.overflow = "hidden";
    loadIndex().then(function () {
      input.focus();
    });
  }

  function closeSearch() {
    overlay.hidden = true;
    document.body.style.overflow = "";
    input.value = "";
    resultsBox.innerHTML = '<p class="search-modal__hint">Type at least 2 characters to search across every level, lesson, grammar topic, exercise and mock exam.</p>';
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  function moveActive(delta) {
    var items = resultsBox.querySelectorAll(".search-result");
    if (!items.length) return;
    activeIndex = (activeIndex + delta + items.length) % items.length;
    items.forEach(function (a, i) {
      a.classList.toggle("is-active", i === activeIndex);
      if (i === activeIndex) a.scrollIntoView({ block: "nearest" });
    });
  }

  if (openBtn) openBtn.addEventListener("click", openSearch);
  if (closeBtn) closeBtn.addEventListener("click", closeSearch);
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) closeSearch();
  });

  var debounceTimer;
  input.addEventListener("input", function () {
    clearTimeout(debounceTimer);
    var val = input.value;
    debounceTimer = setTimeout(function () {
      runSearch(val);
    }, 90);
  });

  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); moveActive(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); moveActive(-1); }
    else if (e.key === "Enter") {
      var items = resultsBox.querySelectorAll(".search-result");
      if (activeIndex >= 0 && items[activeIndex]) {
        e.preventDefault();
        window.location.href = items[activeIndex].getAttribute("href");
      }
    }
  });

  document.addEventListener("keydown", function (e) {
    if (!overlay.hidden && e.key === "Escape") closeSearch();
    // "/" opens search from anywhere, unless typing in a field already
    if (overlay.hidden && e.key === "/" && !/input|textarea|select/i.test(document.activeElement.tagName)) {
      e.preventDefault();
      openSearch();
    }
  });
})();
