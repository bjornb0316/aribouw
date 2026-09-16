(function () {
  "use strict";
  var WA = "31683044191";

  /* ---- binnenkomen bij scrollen ----
     Met drie vangnetten, want een reveal die niet vuurt laat een lege
     pagina achter: alles zichtbaar zonder JS, overslaan in een verborgen
     tab, en na drie seconden hoe dan ook aanzetten. */
  function binnenkomen() {
    var el = [].slice.call(document.querySelectorAll(".op"));
    if (!el.length) return;
    var beweegt = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function alles() {
      for (var i = 0; i < el.length; i++) el[i].classList.add("in");
    }
    if (!beweegt || !("IntersectionObserver" in window) || document.hidden) {
      alles(); return;
    }
    document.querySelectorAll("[data-stagger]").forEach(function (bak) {
      [].slice.call(bak.children).forEach(function (k, i) {
        k.style.setProperty("--i", i);
      });
    });
    var kijker = new IntersectionObserver(function (rijen) {
      rijen.forEach(function (r) {
        if (r.isIntersecting) { r.target.classList.add("in"); kijker.unobserve(r.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    el.forEach(function (e) { kijker.observe(e); });
    setTimeout(alles, 3000);
  }

  /* ---- kop die vast wordt ---- */
  function kop() {
    var k = document.querySelector(".kop");
    if (!k) return;
    var wacht = false;
    function meten() {
      k.classList.toggle("vast", window.scrollY > 60);
      wacht = false;
    }
    window.addEventListener("scroll", function () {
      if (!wacht) { wacht = true; window.requestAnimationFrame(meten); }
    }, { passive: true });
    meten();
  }

  /* ---- mobiel menu ---- */
  function menu() {
    var knop = document.querySelector(".menu-knop");
    var bak = document.querySelector(".menu");
    if (!knop || !bak) return;
    function zet(open) {
      bak.setAttribute("data-open", open ? "1" : "0");
      knop.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    }
    knop.addEventListener("click", function () {
      zet(bak.getAttribute("data-open") !== "1");
    });
    var sluit = bak.querySelector(".menu-sluit");
    if (sluit) sluit.addEventListener("click", function () { zet(false); });
    bak.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { zet(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") zet(false);
    });
  }

  /* ---- vragen open en dicht ---- */
  function vragen() {
    document.querySelectorAll(".vraag button").forEach(function (b) {
      b.addEventListener("click", function () {
        var v = b.closest(".vraag");
        var open = v.getAttribute("data-open") === "1";
        v.setAttribute("data-open", open ? "0" : "1");
        b.setAttribute("aria-expanded", open ? "false" : "true");
      });
    });
  }

  /* ---- WhatsApp met de tekst van deze pagina er al in ---- */
  function whatsapp() {
    var bericht = document.body.getAttribute("data-wa-bericht") ||
      "Hallo, ik heb een vraag naar aanleiding van de website.";
    document.querySelectorAll("[data-wa-pagina]").forEach(function (a) {
      a.setAttribute("href", "https://wa.me/" + WA + "?text=" + encodeURIComponent(bericht));
    });
  }

  /* ---- versturen ----
     ACTIE is het adres uit bouwscript/data.py (FORMULIER_ACTIE). Leeg is
     de demostand: dan telt het als gelukt zonder dat er iets weggaat. Het
     verborgen veld _honey vullen alleen spambots in; die krijgen een
     bevestiging, maar er wordt niets verstuurd. */
  var ACTIE = "";
  function verstuur(bak, gegevens) {
    var honing = bak.querySelector('[name="_honey"]');
    if (!ACTIE || (honing && honing.value)) return Promise.resolve(true);
    gegevens._template = "table";
    gegevens._captcha = "false";
    gegevens.pagina = location.pathname;
    return fetch(ACTIE, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(gegevens)
    }).then(function (r) { return r.ok; }).catch(function () { return false; });
  }

  /* De knop laat zien dat er iets gebeurt, en een tweede klik tijdens het
     versturen doet niets. Mislukt het, dan blijft alles staan wat is
     ingevuld en staat eronder hoe het wel lukt. */
  function bezig(knop, aan) {
    if (!knop) return;
    if (aan) { knop.setAttribute("data-tekst", knop.textContent); knop.textContent = "Versturen..."; }
    else if (knop.getAttribute("data-tekst")) knop.textContent = knop.getAttribute("data-tekst");
    knop.disabled = aan;
    knop.setAttribute("aria-busy", aan ? "true" : "false");
  }
  function verzendfout(bak, aan) {
    var f = bak.querySelector("[data-verzendfout]");
    if (f) f.setAttribute("data-aan", aan ? "1" : "0");
  }
  window.abVerstuur = verstuur;
  window.abBezig = bezig;
  window.abVerzendfout = verzendfout;

  /* ---- veldcontrole ---- */
  function controleer(bak) {
    var ok = true;
    var velden = bak.querySelectorAll(".veld");
    for (var i = 0; i < velden.length; i++) {
      var inv = velden[i].querySelector("input,select,textarea");
      if (!inv || !inv.required) continue;
      var leeg = !inv.value.trim();
      var mailfout = inv.type === "email" && inv.value &&
        !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inv.value);
      if (leeg || mailfout) { velden[i].setAttribute("data-fout", "1"); ok = false; }
      else velden[i].removeAttribute("data-fout");
    }
    if (!ok) {
      var eerste = bak.querySelector('[data-fout="1"] input, [data-fout="1"] select, [data-fout="1"] textarea');
      if (eerste) eerste.focus();
    }
    return ok;
  }
  window.abControleer = controleer;

  function formulieren() {
    document.querySelectorAll("[data-formulier]").forEach(function (f) {
      var gelukt = f.parentElement.querySelector("[data-gelukt]") ||
                   document.querySelector("[data-gelukt]");
      f.addEventListener("submit", function (e) {
        e.preventDefault();
        var knop = f.querySelector('[type="submit"]');
        if (knop && knop.disabled) return;
        verzendfout(f, false);
        if (!controleer(f)) return;
        function waarde(n) { var i = f.querySelector('[name="' + n + '"]'); return i ? i.value.trim() : ""; }
        var gegevens = {
          _subject: "Aanvraag via de website: " + (waarde("wat") || "contactformulier"),
          naam: waarde("naam"), telefoon: waarde("tel"), plaats: waarde("plaats"),
          onderwerp: waarde("wat"), situatie: waarde("bericht")
        };
        bezig(knop, true);
        verstuur(f, gegevens).then(function (ok) {
          bezig(knop, false);
          if (!ok) { verzendfout(f, true); return; }
          f.style.display = "none";
          if (gelukt) {
            gelukt.setAttribute("data-aan", "1");
            gelukt.setAttribute("tabindex", "-1");
            gelukt.focus();
          }
        });
      });
      f.addEventListener("input", function (e) {
        var v = e.target.closest(".veld");
        if (v && e.target.value.trim()) v.removeAttribute("data-fout");
      });
    });
  }

  function start() {
    binnenkomen(); kop(); menu(); vragen(); whatsapp(); formulieren();
    if (window.abExtra) window.abExtra(WA);
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", start);
  else start();
})();
