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

window.abExtra = function (WA) {
  "use strict";

  /* ---- voor-en-na schuiven ----
     Muis, vinger en toetsenbord. Zonder de pijltjestoetsen is de schuif
     niet te bedienen als je geen muis hebt. */
  function schuiven() {
    document.querySelectorAll("[data-schuif]").forEach(function (bak) {
      var greep = bak.querySelector(".schuif-greep");
      if (!greep) return;
      var bezig = false;

      function zet(pct) {
        pct = Math.max(0, Math.min(100, pct));
        bak.style.setProperty("--x", pct + "%");
        greep.setAttribute("aria-valuenow", Math.round(pct));
      }
      function uitPunt(x) {
        var r = bak.getBoundingClientRect();
        zet(((x - r.left) / r.width) * 100);
      }
      greep.addEventListener("pointerdown", function (e) {
        bezig = true;
        if (greep.setPointerCapture && e.pointerId !== undefined)
          greep.setPointerCapture(e.pointerId);
        uitPunt(e.clientX); e.preventDefault();
      });
      bak.addEventListener("pointerdown", function (e) {
        if (e.target === greep || greep.contains(e.target)) return;
        uitPunt(e.clientX);
      });
      window.addEventListener("pointermove", function (e) { if (bezig) uitPunt(e.clientX); });
      window.addEventListener("pointerup", function () { bezig = false; });
      window.addEventListener("pointercancel", function () { bezig = false; });
      greep.addEventListener("keydown", function (e) {
        var nu = parseFloat(greep.getAttribute("aria-valuenow") || "50");
        var stap = e.shiftKey ? 10 : 4;
        if (e.key === "ArrowLeft") { zet(nu - stap); e.preventDefault(); }
        if (e.key === "ArrowRight") { zet(nu + stap); e.preventDefault(); }
        if (e.key === "Home") { zet(0); e.preventDefault(); }
        if (e.key === "End") { zet(100); e.preventDefault(); }
      });
      zet(parseFloat(greep.getAttribute("aria-valuenow") || "50"));
    });
  }

  /* ---- kleurkiezer ----
     Waar mensen bij een schilder het langst over doen is de kleur. Deze
     vraag haalt dat naar voren en zet de richting alvast vast, zodat het
     gesprek daar niet meer bij nul begint. */
  var KLEUR = {
    licht: {
      kop: "Wit en gebroken wit",
      uitleg: "De meest gekozen richting, en meteen de lastigste om goed te krijgen. Gebroken " +
        "wit op een muur die eerst zuiver wit was ziet er vlekkerig uit als de ondergrond niet " +
        "klopt. Daarom besteed ik bij deze kleuren extra tijd aan de voorbereiding.",
      wa: "Hallo, ik denk aan wit of gebroken wit. Kunt u meedenken over de kleur?"
    },
    warm: {
      kop: "Warme tinten",
      uitleg: "Zand, klei, taupe. Warme tinten dekken vaak minder goed dan wit, dus er is meestal " +
        "een laag extra nodig. Dat staat vooraf in de offerte en niet achteraf op de rekening.",
      wa: "Hallo, ik denk aan een warme tint. Kunt u meedenken over de kleur?"
    },
    donker: {
      kop: "Donker en diep",
      uitleg: "Diepe kleuren staan prachtig op een deur of op een enkele wand, maar laten elke " +
        "oneffenheid zien. Op een gladde ondergrond werkt het meteen; op een wand met verleden " +
        "vraagt het eerst herstel.",
      wa: "Hallo, ik denk aan een donkere kleur. Kunt u meedenken over de kleur?"
    },
    weetniet: {
      kop: "Nog geen idee",
      uitleg: "Prima. De meeste mensen weten het pas als er een staal op de muur hangt. Als ik " +
        "kom kijken, denk ik mee over wat past bij het licht in de ruimte en bij wat er al staat.",
      wa: "Hallo, ik weet de kleur nog niet. Kunt u meedenken?"
    }
  };

  function stalen() {
    var bak = document.querySelector("[data-stalen]");
    if (!bak) return;
    var uit = bak.querySelector("[data-stalen-uit]");
    var gekozen = "weetniet";
    /* Het beeld links volgt de richting: bij hover als voorproefje, bij
       klikken blijft het staan. */
    function beeld(naam) {
      bak.querySelectorAll("[data-kleur-beeld]").forEach(function (img) {
        img.setAttribute("data-aan", img.getAttribute("data-kleur-beeld") === naam ? "1" : "0");
      });
    }
    bak.querySelectorAll("[data-staal]").forEach(function (b) {
      b.addEventListener("pointerenter", function (e) {
        if (e.pointerType === "mouse") beeld(b.getAttribute("data-staal"));
      });
      b.addEventListener("pointerleave", function (e) {
        if (e.pointerType === "mouse") beeld(gekozen);
      });
      b.addEventListener("click", function () {
        var k = KLEUR[b.getAttribute("data-staal")];
        if (!k || !uit) return;
        gekozen = b.getAttribute("data-staal");
        beeld(gekozen);
        bak.querySelectorAll("[data-staal]").forEach(function (a) {
          a.setAttribute("aria-pressed", a === b ? "true" : "false");
        });
        uit.querySelector("[data-stalen-kop]").textContent = k.kop;
        uit.querySelector("[data-stalen-uitleg]").textContent = k.uitleg;
        uit.querySelector("[data-stalen-wa]").setAttribute(
          "href", "https://wa.me/" + WA + "?text=" + encodeURIComponent(k.wa));
        var link = uit.querySelector("[data-stalen-link]");
        if (link) link.setAttribute("href",
          "offerte.html?kleur=" + encodeURIComponent(b.getAttribute("data-staal")));
        uit.setAttribute("data-aan", "1");
        uit.setAttribute("tabindex", "-1");
        uit.focus();
      });
    });
  }

  /* ---- aanvraag in stappen ---- */
  function flows() {
    document.querySelectorAll("[data-flow]").forEach(function (bak) {
      var stappen = bak.querySelectorAll("[data-stap]");
      if (!stappen.length) return;
      var klaar = bak.querySelector("[data-klaar]");
      var telling = bak.querySelector("[data-flow-telling]");
      var terug = bak.querySelector("[data-flow-terug]");
      var balk = bak.querySelector("[data-flow-balk]");
      var samen = bak.querySelector("[data-flow-samen]");
      var keuzes = [];
      var nu = 0;

      function toon() {
        for (var i = 0; i < stappen.length; i++)
          stappen[i].setAttribute("data-aan", i === nu ? "1" : "0");
        if (klaar) klaar.setAttribute("data-aan", "0");
        if (telling) telling.textContent = "Stap " + (nu + 1) + " van " + stappen.length;
        if (terug) terug.hidden = nu === 0;
        if (balk) balk.style.width = (nu / stappen.length * 100) + "%";
      }

      /* De klikantwoorden zeggen wat iemand wil, niet wie het is. De
         laatste stap heeft die velden wel, dus die gaan mee. */
      function afzender(stap) {
        function veld(naam) {
          var i = stap.querySelector('[name="' + naam + '"]');
          return i && i.value.trim() ? i.value.trim() : "";
        }
        var naam = veld("naam"), plaats = veld("plaats"), tel = veld("tel");
        var uit = "";
        if (naam) uit += " Ik ben " + naam + (plaats ? " uit " + plaats : "") + ".";
        else if (plaats) uit += " Ik woon in " + plaats + ".";
        if (tel) uit += " Mijn nummer is " + tel + ".";
        return uit;
      }

      function afronden() {
        var laatste = stappen[stappen.length - 1];
        var knop = laatste.querySelector("[data-flow-verstuur]");
        if (knop && knop.disabled) return;
        window.abVerzendfout(laatste, false);
        if (window.abControleer && !window.abControleer(laatste)) return;
        function veld(n) { var i = laatste.querySelector('[name="' + n + '"]'); return i ? i.value.trim() : ""; }
        /* Elke klikvraag met zijn eigen label, zodat de mail leest als een
           ingevuld formulier en niet als een rij losse woorden. */
        var labels = ["werk", "omvang", "kleurrichting", "ondergrond", "wanneer"];
        var gegevens = { _subject: "Offerteaanvraag via de website: " + (keuzes[0] || "onbekend"),
                         naam: veld("naam"), telefoon: veld("tel"), plaats: veld("plaats") };
        for (var n = 0; n < labels.length; n++) gegevens[labels[n]] = keuzes[n] || "";
        window.abBezig(knop, true);
        window.abVerstuur(laatste, gegevens).then(function (ok) {
          window.abBezig(knop, false);
          if (!ok) { window.abVerzendfout(laatste, true); return; }
          toonKlaar(laatste);
        });
      }

      function toonKlaar(laatste) {
        for (var j = 0; j < stappen.length; j++) stappen[j].setAttribute("data-aan", "0");
        if (samen) {
          samen.innerHTML = keuzes.filter(Boolean).map(function (k) {
            return "<span>" + k + "</span>";
          }).join("");
        }
        if (balk) balk.style.width = "100%";
        if (telling) telling.textContent = "Verstuurd";
        if (terug) terug.hidden = true;
        if (klaar) {
          klaar.setAttribute("data-aan", "1");
          klaar.setAttribute("tabindex", "-1");
          klaar.focus();
          var wa = klaar.querySelector("[data-wa]");
          if (wa) {
            var basis = bak.getAttribute("data-flow-bericht") ||
              "Hallo, ik heb een aanvraag gedaan via de site.";
            wa.setAttribute("href", "https://wa.me/" + WA + "?text=" +
              encodeURIComponent(basis + " " + keuzes.filter(Boolean).join(", ") + "." +
                                 afzender(laatste)));
          }
        }
      }

      bak.addEventListener("click", function (e) {
        var knop = e.target.closest("[data-waarde]");
        if (knop && bak.contains(knop)) {
          keuzes[nu] = knop.getAttribute("data-waarde");
          keuzes.length = nu + 1;
          nu++; toon(); return;
        }
        if (e.target.closest("[data-flow-terug]")) {
          e.preventDefault(); nu = Math.max(0, nu - 1); toon(); return;
        }
        if (e.target.closest("[data-flow-verstuur]")) { e.preventDefault(); afronden(); }
      });
      bak.addEventListener("input", function (e) {
        var v = e.target.closest(".veld");
        if (v && e.target.value.trim()) v.removeAttribute("data-fout");
      });
      toon();

      /* Binnenkomen via een dienstpagina of via de kleurkiezer.
         De dienst is stap 1, de kleur is stap 3. Daarom niet alleen naar
         de eerste stap kijken maar naar de stap waar het antwoord in
         staat, en die overslaan zodra de bezoeker daar komt. Wie de
         kleur al heeft gekozen hoeft hem niet nog een keer aan te
         klikken. */
      var p = new URLSearchParams(location.search);
      var vooraf = [p.get("werk"), p.get("kleur"),
                    p.get("soort") === "zakelijk" ? "een zakelijk project" : ""].filter(Boolean);
      var gebruikt = {};
      if (vooraf.length) {
        var oudeToon = toon;
        toon = function () {
          oudeToon();
          for (var i = 0; i < vooraf.length; i++) {
            var w = vooraf[i];
            if (gebruikt[w]) continue;
            var k = stappen[nu] &&
              stappen[nu].querySelector('[data-waarde="' + w + '"]');
            if (k) { gebruikt[w] = true; k.click(); return; }
          }
        };
        toon();
      }
    });
  }

  /* ---- films ----
     Drie soorten: "eenmaal" (de hero: tape eraf en blijven staan op de
     lijn), "lus" (loopt zolang hij in beeld is) en "hover" (dienstkaarten:
     lopen onder de muis, op een aanraakscherm zodra ze in beeld zijn).
     De bron laadt pas bij eerste gebruik. Met minder beweging of met
     databesparing aan blijft de poster staan. */
  function films() {
    var alle = [].slice.call(document.querySelectorAll("video[data-film]"));
    if (!alle.length) return;
    var zuinig = navigator.connection && navigator.connection.saveData;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || zuinig) return;
    var muis = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

    function laad(v) {
      if (v.getAttribute("data-geladen")) return;
      v.setAttribute("data-geladen", "1");
      v.querySelectorAll("source[data-src]").forEach(function (s) {
        s.setAttribute("src", s.getAttribute("data-src"));
      });
      v.load();
    }
    function speel(v) {
      laad(v); v.muted = true;
      var p = v.play();
      if (p && p.catch) p.catch(function () {});
    }

    var kijker = "IntersectionObserver" in window ? new IntersectionObserver(function (rijen) {
      rijen.forEach(function (r) {
        var v = r.target;
        if (r.isIntersecting) {
          if (v.getAttribute("data-film") === "eenmaal" && v.getAttribute("data-klaar")) return;
          speel(v);
        } else if (!v.paused) v.pause();
      });
    }, { threshold: 0.2 }) : null;

    alle.forEach(function (v) {
      var soort = v.getAttribute("data-film");
      if (soort === "eenmaal") {
        v.addEventListener("ended", function () { v.setAttribute("data-klaar", "1"); });
      }
      if (soort === "hover" && muis) {
        var kaart = v.closest(".kaart") || v.parentNode;
        kaart.addEventListener("pointerenter", function () { speel(v); });
        kaart.addEventListener("pointerleave", function () { v.pause(); });
        kaart.addEventListener("focusin", function () { speel(v); });
        kaart.addEventListener("focusout", function () { v.pause(); });
        return;
      }
      if (kijker) kijker.observe(v); else speel(v);
    });
  }

  /* ---- beheer: project toevoegen (voorbeeld voor de correctieronde) ----
     Alles gebeurt in de browser: foto's worden alleen lokaal getoond en er
     wordt niets opgeslagen of verstuurd. De echte versie slaat het project
     op en zet het direct op de site. */
  function beheer() {
    var f = document.querySelector("[data-beheer]");
    if (!f) return;
    var kaart = document.querySelector("[data-beheer-kaart]");
    var gelukt = document.querySelector("[data-beheer-gelukt]");
    var akkoord = f.querySelector("[data-akkoord]");
    var akkoordFout = f.querySelector("[data-akkoord-fout]");

    function w(n) { var i = f.querySelector('[name="' + n + '"]'); return i ? i.value.trim() : ""; }
    function foto(naam, img) {
      var i = f.querySelector('[name="' + naam + '"]');
      var bestand = i && i.files && i.files[0];
      if (bestand) img.src = URL.createObjectURL(bestand);
    }
    function toonKaart() {
      var tonen = f.querySelector('[name="plaatsnaam"]').checked;
      var wat = w("onderdelen");
      var titel = wat.charAt(0).toUpperCase() + wat.slice(1) +
        (tonen && w("plaats") && w("plaats") !== "Andere plaats" ? " in " + w("plaats") : "");
      kaart.querySelector("[data-bk-titel]").textContent = titel;
      kaart.querySelector("[data-bk-situatie]").textContent = w("situatie");
      kaart.querySelector("[data-bk-aanpak]").textContent = w("aanpak");
      var voor = kaart.querySelector("[data-bk-voor]"), na = kaart.querySelector("[data-bk-na]");
      foto("voor", voor); foto("na", na);
      voor.alt = titel + ", voor"; na.alt = titel + ", na";
      kaart.querySelector("[data-bk-links]").textContent =
        "Komt op de werkpagina, als eigen projectpagina, en bij " + w("werk") +
        (tonen && w("plaats") !== "Andere plaats" ? " en " + w("plaats") : "") + ".";
      kaart.hidden = false;
    }
    function klopt(metAkkoord) {
      var ok = window.abControleer ? window.abControleer(f) : true;
      if (metAkkoord) {
        akkoordFout.setAttribute("data-aan", akkoord.checked ? "0" : "1");
        if (!akkoord.checked) ok = false;
      }
      return ok;
    }

    f.querySelector("[data-beheer-voorbeeld]").addEventListener("click", function () {
      if (!klopt(false)) return;
      toonKaart();
      kaart.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!klopt(true)) return;
      toonKaart();
      gelukt.setAttribute("data-aan", "1");
      gelukt.setAttribute("tabindex", "-1");
      gelukt.focus();
    });
    f.addEventListener("input", function (e) {
      var v = e.target.closest(".veld");
      if (v && e.target.value) v.removeAttribute("data-fout");
    });
    akkoord.addEventListener("change", function () {
      if (akkoord.checked) akkoordFout.setAttribute("data-aan", "0");
    });
  }

  schuiven(); stalen(); flows(); films(); beheer();
};
