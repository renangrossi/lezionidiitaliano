/*!
 * Renan the Teacher — Floating Dictionary Widget (Italian course)
 * A small floating lookup tool (styled like the back-to-top button),
 * available on every page, so a student can check an Italian word
 * without losing their place. This is a *monolingual* Italian
 * dictionary — it queries Italian Wiktionary's REST API (free,
 * keyless, CORS-enabled) and keeps only entries whose language is
 * "Italiano", so both the headword and its definition are in Italian,
 * exactly like a native speaker's dictionary. Pronunciation has no
 * audio clips from this source, so it always falls back straight to
 * the browser's built-in speechSynthesis reading the word aloud with
 * an Italian voice. The outbound dictionary links below the result are
 * always shown too, in the same fixed order as the main Dictionary
 * page, as a second way to check the word.
 */
(function () {
  "use strict";

  var trigger = document.querySelector("[data-dict-widget-toggle]");
  if (!trigger) return;
  var panel = document.querySelector("[data-dict-widget-panel]");
  var input = panel.querySelector("[data-dict-widget-input]");
  var resultBox = panel.querySelector("[data-dict-widget-result]");
  var closeBtn = panel.querySelector("[data-dict-widget-close]");
  var linksBox = panel.querySelector("[data-dict-widget-links]");

  /* ---------------------------------------------------------------
   * Attention hint — "Dizionario" appears next to the button on
   * load, then drifts up and fades away letter by letter after a
   * few seconds, just to point out the button exists.
   * --------------------------------------------------------------- */
  function showHint() {
    var word = "Dizionario";
    var hint = document.createElement("div");
    hint.className = "dict-widget-hint";
    hint.setAttribute("aria-hidden", "true");
    word.split("").forEach(function (ch) {
      var span = document.createElement("span");
      span.textContent = ch;
      hint.appendChild(span);
    });
    trigger.insertAdjacentElement("beforebegin", hint);

    setTimeout(function () {
      var spans = hint.querySelectorAll("span");
      spans.forEach(function (span, i) {
        setTimeout(function () {
          span.classList.add("is-leaving");
        }, i * 40);
      });
      setTimeout(function () {
        if (hint.parentNode) hint.parentNode.removeChild(hint);
      }, spans.length * 40 + 500);
    }, 2600);
  }
  showHint();

  // Locks the page behind the widget on small phones while it's open.
  // window.__rtPanelLock is a shared counter so multiple panels never
  // unlock a page another one is still holding the lock on.
  var lockedBodyScroll = false;
  function lockBodyScrollForPanel() {
    if (!(window.matchMedia && window.matchMedia("(max-width: 640px)").matches)) return;
    window.__rtPanelLock = (window.__rtPanelLock || 0) + 1;
    lockedBodyScroll = true;
    if (window.__rtPanelLock > 1) return;
    window.__rtPanelLockY = window.scrollY || window.pageYOffset || 0;
    var s = document.body.style;
    s.position = "fixed";
    s.top = "-" + window.__rtPanelLockY + "px";
    s.left = "0";
    s.right = "0";
    s.width = "100%";
  }
  function unlockBodyScrollForPanel() {
    if (!lockedBodyScroll) return;
    lockedBodyScroll = false;
    window.__rtPanelLock = Math.max(0, (window.__rtPanelLock || 1) - 1);
    if (window.__rtPanelLock > 0) return;
    var y = window.__rtPanelLockY || 0;
    var s = document.body.style;
    s.position = "";
    s.top = "";
    s.left = "";
    s.right = "";
    s.width = "";
    window.scrollTo(0, y);
  }

  function toggle(open) {
    var willOpen = open !== undefined ? open : panel.hidden;
    panel.hidden = !willOpen;
    trigger.setAttribute("aria-expanded", String(willOpen));
    if (willOpen) {
      lockBodyScrollForPanel();
      input.focus();
    } else {
      unlockBodyScrollForPanel();
    }
  }

  trigger.addEventListener("click", function (e) {
    e.stopPropagation();
    toggle();
  });
  closeBtn.addEventListener("click", function () { toggle(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !panel.hidden) toggle(false);
  });
  // Only closes on a click that both starts and ends outside the panel.
  var pointerDownOutside = false;
  document.addEventListener("pointerdown", function (e) {
    if (panel.hidden) return;
    pointerDownOutside = !(panel.contains(e.target) || trigger.contains(e.target));
  });
  document.addEventListener("click", function (e) {
    if (panel.hidden) return;
    if (panel.contains(e.target) || trigger.contains(e.target)) return;
    if (!pointerDownOutside) return;
    toggle(false);
  });
  panel.addEventListener("click", function (e) { e.stopPropagation(); });

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = String(s || "");
    return d.innerHTML;
  }

  function renderOutboundLinks(word) {
    var encoded = encodeURIComponent(word || "ciao");
    // Same fixed order as the Dictionary page's core cards.
    var sites = [
      ["Treccani", "https://www.treccani.it/vocabolario/ricerca/" + encoded + "/"],
      ["Garzanti", "https://www.garzantilinguistica.it/ricerca/?q=" + encoded],
      ["Wikizionario", "https://it.wiktionary.org/wiki/" + encoded],
      ["Sinonimi", "https://www.sapere.it/sapere/strumenti/dizionario-sinonimi-contrari/ricerca/" + encoded + ".html"],
    ];
    linksBox.innerHTML = sites
      .map(function (s) {
        return '<a class="btn btn--ghost btn--small" target="_blank" rel="noopener" href="' + s[1] + '">' + s[0] + "</a>";
      })
      .join("");
  }

  /* ---------------------------------------------------------------
   * Word lookup — tries several capitalization/apostrophe variants in
   * order, since Wiktionary's REST endpoint is case-sensitive and
   * Italian words are sometimes indexed with an elided apostrophe
   * (e.g. "un'amica") and sometimes without.
   * --------------------------------------------------------------- */
  function titleCase(s) {
    return s.replace(/\w\S*/g, function (t) {
      return t.charAt(0).toUpperCase() + t.slice(1).toLowerCase();
    });
  }

  function candidateWords(word) {
    var seen = {};
    var out = [];
    [word, word.toLowerCase(), word.charAt(0).toUpperCase() + word.slice(1).toLowerCase(), titleCase(word)].forEach(function (w) {
      if (w && !seen[w]) {
        seen[w] = true;
        out.push(w);
      }
    });
    return out;
  }

  /* ---------------------------------------------------------------
   * Italian Wiktionary (Wikizionario) REST definition endpoint,
   * filtered to the "Italiano" language section — see the file header
   * comment. it.wiktionary.org documents both Italian words and
   * foreign loanwords used in Italian (each under its own language
   * name, in Italian — e.g. "Inglese" for an English loanword); only
   * "Italiano" sections are genuine Italian headwords with Italian
   * definitions.
   * --------------------------------------------------------------- */
  function stripHtml(s) {
    return String(s || "")
      .replace(/<[^>]+>/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function normalizeWiktionary(groups, word) {
    return [
      {
        word: word,
        phonetic: "",
        phonetics: [],
        meanings: groups.map(function (g) {
          return {
            partOfSpeech: (g.partOfSpeech || "").toLowerCase(),
            definitions: (g.definitions || []).slice(0, 4).map(function (d) {
              return { definition: stripHtml(d.definition) };
            }),
          };
        }),
      },
    ];
  }

  function fetchWiktionaryDefinition(word) {
    return fetch("https://it.wiktionary.org/api/rest_v1/page/definition/" + encodeURIComponent(word))
      .then(function (res) {
        if (!res.ok) throw new Error("not found: " + word);
        return res.json();
      })
      .then(function (data) {
        // Italian Wiktionary's own content language is "it" — groups
        // within it are labelled by which language the *headword*
        // belongs to. Keep only genuine Italian headwords.
        var groups = ((data && data.it) || []).filter(function (g) {
          return g.language === "Italiano";
        });
        if (!groups.length) throw new Error("no Italian entry: " + word);
        return normalizeWiktionary(groups, word);
      });
  }

  function tryCandidates(candidates, index) {
    index = index || 0;
    if (index >= candidates.length) {
      return Promise.reject(new Error("no candidates matched"));
    }
    return fetchWiktionaryDefinition(candidates[index]).catch(function () {
      return tryCandidates(candidates, index + 1);
    });
  }

  var lookupTimer;
  var lastQuery = "";

  function lookup(word) {
    word = word.trim();
    if (!word) {
      resultBox.innerHTML = '<p class="dict-widget__hint">Digita una parola e premi Invio, oppure aspetta un attimo dopo aver scritto.</p>';
      linksBox.innerHTML = "";
      return;
    }
    if (word !== lastQuery && window.ProgressTracker && typeof window.ProgressTracker.recordDictionaryUse === "function") {
      window.ProgressTracker.recordDictionaryUse();
    }
    renderOutboundLinks(word);
    resultBox.innerHTML = '<p class="dict-widget__hint">Ricerca di &ldquo;' + escapeHtml(word) + '&rdquo;&hellip;</p>';
    lastQuery = word;

    tryCandidates(candidateWords(word))
      .then(function (data) {
        if (lastQuery !== word) return; // a newer query has since started
        renderDefinition(data);
      })
      .catch(function () {
        if (lastQuery !== word) return;
        resultBox.innerHTML =
          '<p class="dict-widget__hint">Pronto a cercare &ldquo;' + escapeHtml(word) + '&rdquo;! Scegli un dizionario qui sotto:</p>';
      });
  }

  var currentUtterance = null;

  // Pronunciation: the browser's own text-to-speech voice, read with an
  // Italian voice when the device has one. This source has no audio
  // clips of its own, so speech synthesis is the only path (not a
  // fallback after a failed clip, as on the English site's widget).
  function speakWord(word, btn) {
    if (!window.speechSynthesis || typeof window.SpeechSynthesisUtterance !== "function") return false;
    try {
      var synth = window.speechSynthesis;
      var utter = new window.SpeechSynthesisUtterance(word);
      utter.lang = "it-IT";
      utter.rate = 0.9;
      currentUtterance = utter;
      if (btn) {
        utter.addEventListener("end", function () { btn.classList.remove("is-playing"); });
        utter.addEventListener("error", function () { btn.classList.remove("is-playing"); });
      }
      if (synth.speaking || synth.pending) {
        synth.cancel();
        setTimeout(function () { synth.speak(utter); }, 50);
      } else {
        synth.speak(utter);
      }
      return true;
    } catch (e) {
      return false;
    }
  }

  function playPronunciation(word, btn) {
    btn.classList.remove("has-error");
    btn.removeAttribute("title");
    if (speakWord(word, btn)) {
      btn.classList.add("is-playing");
      return;
    }
    btn.classList.remove("is-playing");
    btn.classList.add("has-error");
    btn.setAttribute("title", "Questo browser non può leggere l'italiano ad alta voce — prova un dizionario qui sotto.");
  }

  function renderDefinition(data) {
    if (!Array.isArray(data) || !data.length) {
      resultBox.innerHTML = '<p class="dict-widget__hint">Nessuna definizione trovata. Prova un dizionario qui sotto.</p>';
      return;
    }
    var entry = data[0];

    resultBox.innerHTML = "";
    var wordRow = document.createElement("div");
    wordRow.className = "dict-widget__word-row";
    var wordEl = document.createElement("span");
    wordEl.className = "dict-widget__word";
    wordEl.textContent = entry.word;
    wordRow.appendChild(wordEl);
    var audioBtn = document.createElement("button");
    audioBtn.type = "button";
    audioBtn.className = "dict-widget__audio";
    audioBtn.setAttribute("aria-label", "Ascolta la pronuncia italiana");
    audioBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5Z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18 6a9 9 0 0 1 0 12"/></svg>';
    audioBtn.addEventListener("click", function () { playPronunciation(entry.word, audioBtn); });
    wordRow.appendChild(audioBtn);
    resultBox.appendChild(wordRow);

    (entry.meanings || []).slice(0, 3).forEach(function (m) {
      var pos = document.createElement("div");
      pos.className = "dict-widget__pos";
      pos.textContent = m.partOfSpeech;
      resultBox.appendChild(pos);
      var list = document.createElement("ol");
      list.className = "dict-widget__defs";
      (m.definitions || []).slice(0, 2).forEach(function (d) {
        var li = document.createElement("li");
        li.textContent = d.definition;
        list.appendChild(li);
      });
      resultBox.appendChild(list);
    });
  }

  input.addEventListener("input", function () {
    clearTimeout(lookupTimer);
    lookupTimer = setTimeout(function () {
      lookup(input.value);
    }, 500);
  });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      clearTimeout(lookupTimer);
      lookup(input.value);
    }
  });
})();
