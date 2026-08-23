/*!
 * Renan the Teacher — Dictionary word lookup (Italian course)
 * Rewrites every dictionary/reference link on the page to point at
 * whatever word the user has typed, entirely client-side.
 */
(function () {
  "use strict";

  var input = document.querySelector("[data-dict-word]");
  if (!input) return;
  var cards = document.querySelectorAll(".dict-card[data-url-template]");

  function update() {
    var raw = input.value.trim();
    var word = raw || "ciao";
    var encoded = encodeURIComponent(word.toLowerCase());
    cards.forEach(function (card) {
      var tmpl = card.getAttribute("data-url-template");
      var link = card.querySelector("[data-dict-link]");
      if (!link) return;
      link.href = tmpl.replace("{word}", encoded);
      link.textContent = "";
      var icon = link.querySelector("svg");
      if (icon) link.appendChild(icon);
      link.appendChild(document.createTextNode(raw ? "Consulta “" + raw + "”" : "Consulta"));
    });
  }

  input.addEventListener("input", update);
  update();

  // Enter key opens a random one of the four core dictionaries
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      var primaryLinks = document.querySelectorAll(".card--feature.dict-card [data-dict-link]");
      if (!primaryLinks.length) return;
      var pick = primaryLinks[Math.floor(Math.random() * primaryLinks.length)];
      recordDictionaryUse();
      window.open(pick.href, "_blank", "noopener");
    }
  });

  function recordDictionaryUse() {
    if (window.ProgressTracker && typeof window.ProgressTracker.recordDictionaryUse === "function") {
      window.ProgressTracker.recordDictionaryUse();
    }
  }
  document.querySelectorAll(".dict-card[data-url-template] [data-dict-link]").forEach(function (link) {
    link.addEventListener("click", recordDictionaryUse);
  });
})();
