/* Het beheerscherm. Vanilla JS, geen bibliotheken.
 *
 * Alles loopt via /api. De server controleert bij elke schrijfactie of er
 * is ingelogd; dit scherm is alleen de bediening. Foto's worden in de
 * browser verkleind voordat ze worden geupload, zodat het ook op 4G snel
 * gaat en de opslag klein blijft. */
(function () {
  "use strict";

  var $ = function (s, b) { return (b || document).querySelector(s); };
  var melding = $("[data-melding]");

  function zeg(tekst, lang) {
    melding.textContent = tekst;
    melding.setAttribute("data-aan", "1");
    clearTimeout(zeg.t);
    zeg.t = setTimeout(function () { melding.setAttribute("data-aan", "0"); }, lang || 2600);
  }

  function api(pad, opties) {
    return fetch("/api" + pad, Object.assign({ headers: {} }, opties || {})).then(function (r) {
      if (r.status === 401) { toon(false); throw new Error("Niet ingelogd"); }
      return r.json().catch(function () { return {}; });
    });
  }
  function stuur(pad, methode, data) {
    return api(pad, {
      method: methode,
      headers: { "content-type": "application/json" },
      body: JSON.stringify(data),
    });
  }
  function veilig(t) {
    return String(t == null ? "" : t).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  /* Dezelfde veldcontrole als op de site: verplichte velden moeten gevuld
     zijn, en het eerste lege veld krijgt de aandacht. */
  function controleer(bak) {
    var ok = true, velden = bak.querySelectorAll(".veld");
    for (var i = 0; i < velden.length; i++) {
      var inv = velden[i].querySelector("input,select,textarea");
      if (!inv || !inv.required) continue;
      if (!inv.value.trim()) { velden[i].setAttribute("data-fout", "1"); ok = false; }
      else velden[i].removeAttribute("data-fout");
    }
    if (!ok) {
      var eerste = bak.querySelector('[data-fout="1"] input, [data-fout="1"] select, [data-fout="1"] textarea');
      if (eerste) eerste.focus();
    }
    return ok;
  }

  /* ---- inloggen ---- */
  function toon(ingelogd) {
    $("[data-inlog]").hidden = ingelogd;
    $("[data-beheer]").hidden = !ingelogd;
    $("[data-uitloggen]").hidden = !ingelogd;
    if (ingelogd) laadAlles();
  }

  $("[data-inlogformulier]").addEventListener("submit", function (e) {
    e.preventDefault();
    var pin = $("#pin").value.trim();
    $("[data-pinfout]").style.display = "none";
    stuur("/login", "POST", { pin: pin }).then(function (r) {
      if (r.ok) { $("#pin").value = ""; toon(true); }
      else $("[data-pinfout]").style.display = "block";
    }).catch(function () { $("[data-pinfout]").style.display = "block"; });
  });

  $("[data-uitloggen]").addEventListener("click", function (e) {
    e.preventDefault();
    stuur("/uitloggen", "POST", {}).then(function () { toon(false); });
  });

  /* ---- tabbladen ---- */
  document.querySelectorAll(".bh-tab").forEach(function (t) {
    t.addEventListener("click", function () {
      document.querySelectorAll(".bh-tab").forEach(function (a) {
        a.setAttribute("aria-selected", a === t ? "true" : "false");
      });
      document.querySelectorAll("[data-paneel]").forEach(function (p) {
        p.hidden = p.getAttribute("data-paneel") !== t.getAttribute("data-tab");
      });
    });
  });

  /* ---- teksten ---- */
  var alleTeksten = {}, aanpassingen = {};

  function tekstenTonen(zoek) {
    var bak = $("[data-teksten]");
    var perPagina = {};
    Object.keys(alleTeksten).forEach(function (sleutel) {
      var regel = alleTeksten[sleutel];
      var tekst = aanpassingen[sleutel] || regel.tekst;
      if (zoek) {
        var z = zoek.toLowerCase();
        var raak = tekst.toLowerCase().indexOf(z) >= 0 ||
          regel.paginas.join(" ").toLowerCase().indexOf(z) >= 0;
        if (!raak) return;
      }
      var pagina = regel.paginas[0] || "overig";
      (perPagina[pagina] = perPagina[pagina] || []).push({ sleutel: sleutel, regel: regel });
    });
    var namen = Object.keys(perPagina).sort(function (a, b) {
      return a === "index.html" ? -1 : b === "index.html" ? 1 : a.localeCompare(b);
    });
    if (!namen.length) { bak.innerHTML = '<p class="klein">Niets gevonden.</p>'; return; }
    bak.innerHTML = namen.map(function (naam) {
      var rijen = perPagina[naam].map(function (r) {
        var aangepast = aanpassingen[r.sleutel];
        var waarde = aangepast || r.regel.tekst;
        var elders = r.regel.paginas.length > 1
          ? ' &middot; staat ook op ' + veilig(r.regel.paginas.slice(1).join(", ")) : "";
        return '<div class="bh-rij">' +
          '<p class="klein">' + (aangepast ? '<span class="bh-bewerkt">Aangepast</span> &middot; ' : "") +
          veilig(naam) + elders + "</p>" +
          '<textarea rows="' + (waarde.length > 120 ? 3 : 2) + '" data-sleutel="' +
          veilig(r.sleutel) + '">' + veilig(waarde) + "</textarea>" +
          (aangepast ? '<div class="bh-acties"><button type="button" data-herstel="' +
            veilig(r.sleutel) + '">Oorspronkelijke tekst terug</button></div>' : "") +
          "</div>";
      }).join("");
      return '<h2 class="bh-groep">' + veilig(naam) + "</h2>" + rijen;
    }).join("");
  }

  document.addEventListener("change", function (e) {
    var t = e.target;
    if (t.tagName === "TEXTAREA" && t.dataset.sleutel) {
      var sleutel = t.dataset.sleutel, waarde = t.value.trim();
      var origineel = alleTeksten[sleutel] ? alleTeksten[sleutel].tekst : "";
      if (waarde === origineel) { waarde = ""; }
      stuur("/teksten", "PUT", { sleutel: sleutel, waarde: waarde }).then(function (r) {
        if (!r.ok) return zeg("Opslaan lukte niet");
        if (waarde) aanpassingen[sleutel] = waarde; else delete aanpassingen[sleutel];
        zeg(waarde ? "Opgeslagen" : "Oorspronkelijke tekst terug");
        tekstenTonen($("[data-zoek]").value.trim());
      });
    }
  });

  document.addEventListener("click", function (e) {
    var h = e.target.closest("[data-herstel]");
    if (h) {
      var sleutel = h.getAttribute("data-herstel");
      stuur("/teksten", "PUT", { sleutel: sleutel, waarde: "" }).then(function () {
        delete aanpassingen[sleutel];
        zeg("Oorspronkelijke tekst terug");
        tekstenTonen($("[data-zoek]").value.trim());
      });
    }
  });

  $("[data-zoek]").addEventListener("input", function (e) {
    tekstenTonen(e.target.value.trim());
  });

  /* ---- foto's verkleinen en uploaden ---- */
  function verklein(bestand, maat) {
    return new Promise(function (klaar, mis) {
      var lezer = new FileReader();
      lezer.onerror = mis;
      lezer.onload = function () {
        var beeld = new Image();
        beeld.onerror = mis;
        beeld.onload = function () {
          var schaal = Math.min(1, maat / Math.max(beeld.width, beeld.height));
          var doek = document.createElement("canvas");
          doek.width = Math.round(beeld.width * schaal);
          doek.height = Math.round(beeld.height * schaal);
          doek.getContext("2d").drawImage(beeld, 0, 0, doek.width, doek.height);
          doek.toBlob(function (blob) { klaar(blob); }, "image/jpeg", 0.82);
        };
        beeld.src = lezer.result;
      };
      lezer.readAsDataURL(bestand);
    });
  }

  function upload(bestand) {
    return verklein(bestand, 1600).then(function (blob) {
      return fetch("/api/upload", {
        method: "POST",
        headers: { "content-type": "image/jpeg" },
        body: blob,
      }).then(function (r) { return r.json(); });
    });
  }

  /* ---- projecten ---- */
  function projectenTonen(lijst) {
    var bak = $("[data-projecten]");
    if (!lijst.length) {
      bak.innerHTML = '<p class="klein">Nog geen projecten toegevoegd.</p>';
      return;
    }
    bak.innerHTML = '<h2 class="bh-groep">Op de site</h2>' + lijst.map(function (p) {
      return '<div class="bh-rij"><div class="bh-kaart">' +
        '<img src="/media/' + veilig(p.na) + '" alt="">' +
        "<div><b>" + veilig(p.titel) + "</b>" +
        '<p class="klein">' + veilig([p.dienst, p.plaats].filter(Boolean).join(", ")) +
        (p.zichtbaar ? "" : " &middot; verborgen") + "</p>" +
        '<div class="bh-acties">' +
        '<button type="button" data-zicht="' + p.id + '">' +
        (p.zichtbaar ? "Verbergen" : "Weer tonen") + "</button>" +
        '<a class="knop knop--lijn knop--klein" href="/projecten/' + veilig(p.slug) +
        '" target="_blank" rel="noopener">Bekijken</a>' +
        '<button type="button" class="weg" data-weg="' + p.id + '">Verwijderen</button>' +
        "</div></div></div></div>";
    }).join("");
  }

  var projecten = [];
  $("[data-projectformulier]").addEventListener("submit", function (e) {
    e.preventDefault();
    var f = e.target;
    if (!controleer(f)) return;
    var akkoord = $("[data-akkoord]", f);
    $("[data-akkoordfout]", f).setAttribute("data-aan", akkoord.checked ? "0" : "1");
    if (!akkoord.checked) return;
    var knop = f.querySelector('[type="submit"]');
    var voortgang = $("[data-voortgang]", f);
    knop.disabled = true;
    voortgang.textContent = "Foto's uploaden...";
    Promise.all([upload($("#pr-voor").files[0]), upload($("#pr-na").files[0])])
      .then(function (r) {
        if (!r[0].ok || !r[1].ok) throw new Error("upload");
        voortgang.textContent = "Project opslaan...";
        return stuur("/projecten", "POST", {
          titel: $("#pr-titel").value.trim(), plaats: $("#pr-plaats").value.trim(),
          dienst: $("#pr-dienst").value, wanneer: $("#pr-wanneer").value,
          situatie: $("#pr-situatie").value.trim(), aanpak: $("#pr-aanpak").value.trim(),
          voor: r[0].sleutel, na: r[1].sleutel,
        });
      })
      .then(function (r) {
        knop.disabled = false; voortgang.textContent = "";
        if (!r.ok) return zeg(r.fout || "Opslaan lukte niet");
        f.reset(); akkoord.checked = false;
        zeg("Project staat op de site");
        laadProjecten();
      })
      .catch(function () {
        knop.disabled = false; voortgang.textContent = "";
        zeg("Er ging iets mis met de foto's. Probeer het opnieuw.", 4000);
      });
  });

  document.addEventListener("click", function (e) {
    var zicht = e.target.closest("[data-zicht]");
    if (zicht) {
      var p = projecten.find(function (x) { return x.id === Number(zicht.dataset.zicht); });
      stuur("/projecten/" + p.id, "PUT", Object.assign({}, p, { zichtbaar: p.zichtbaar ? 0 : 1 }))
        .then(function () { zeg("Aangepast"); laadProjecten(); });
    }
    var weg = e.target.closest("[data-weg]");
    if (weg) {
      if (!confirm("Dit project en de foto's verwijderen?")) return;
      api("/projecten/" + weg.dataset.weg, { method: "DELETE" })
        .then(function () { zeg("Verwijderd"); laadProjecten(); });
    }
    var rweg = e.target.closest("[data-review-weg]");
    if (rweg) {
      if (!confirm("Deze review verwijderen?")) return;
      api("/reviews/" + rweg.dataset.reviewWeg, { method: "DELETE" })
        .then(function () { zeg("Verwijderd"); laadReviews(); });
    }
    var aweg = e.target.closest("[data-aanvraag-weg]");
    if (aweg) {
      api("/aanvragen/" + aweg.dataset.aanvraagWeg, { method: "DELETE" })
        .then(function () { laadAanvragen(); });
    }
  });

  /* ---- reviews ---- */
  $("[data-reviewformulier]").addEventListener("submit", function (e) {
    e.preventDefault();
    var f = e.target;
    if (!controleer(f)) return;
    stuur("/reviews", "POST", {
      tekst: $("#rv-tekst").value.trim(), wie: $("#rv-wie").value.trim(),
      wat: $("#rv-wat").value.trim(),
    }).then(function (r) {
      if (!r.ok) return zeg(r.fout || "Opslaan lukte niet");
      f.reset(); zeg("Review staat op de site"); laadReviews();
    });
  });

  function reviewsTonen(lijst) {
    var bak = $("[data-reviews]");
    bak.innerHTML = lijst.length
      ? '<h2 class="bh-groep">Eigen reviews</h2>' + lijst.map(function (r) {
          return '<div class="bh-rij"><p>' + veilig(r.tekst) + "</p>" +
            '<p class="klein">' + veilig(r.wie) + " &middot; " + veilig(r.wat || "") + "</p>" +
            '<div class="bh-acties"><button type="button" class="weg" data-review-weg="' +
            r.id + '">Verwijderen</button></div></div>';
        }).join("")
      : '<p class="klein">Nog geen eigen reviews. De vier van Werkspot staan al op de site.</p>';
  }

  /* ---- aanvragen ---- */
  function aanvragenTonen(lijst) {
    var bak = $("[data-aanvragen]");
    bak.innerHTML = lijst.length ? lijst.map(function (a) {
      var g = {};
      try { g = JSON.parse(a.gegevens); } catch (e) { g = {}; }
      var regels = Object.keys(g).filter(function (k) { return k[0] !== "_" && g[k]; })
        .map(function (k) { return "<b>" + veilig(k) + ":</b> " + veilig(g[k]); }).join("<br>");
      // Of de mail naar info@aribouw.nl is aangekomen. Mislukt: de aanvraag
      // staat hier wel, maar Ahmad heeft hem niet in zijn mail gekregen.
      var mail = !a.mail ? "" : a.mail === "verstuurd"
        ? " &middot; gemaild"
        : ' &middot; <b style="color:#b3261e">mail niet aangekomen</b> (' + veilig(a.mail.replace(/^mislukt: /, "")) + ")";
      return '<div class="bh-rij"><p class="klein">' + veilig(a.gemaakt.slice(0, 16).replace("T", " ")) +
        " &middot; " + veilig(a.soort) + mail + "</p><p>" + regels + "</p>" +
        '<div class="bh-acties">' +
        (g.telefoon ? '<a class="knop knop--lijn knop--klein" href="tel:' + veilig(g.telefoon) +
          '">Bellen</a>' : "") +
        '<button type="button" class="weg" data-aanvraag-weg="' + a.id + '">Verwijderen</button>' +
        "</div></div>";
    }).join("") : '<p class="klein">Nog geen aanvragen.</p>';
  }

  /* ---- laden ---- */
  function laadProjecten() {
    return api("/projecten").then(function (l) { projecten = l || []; projectenTonen(projecten); });
  }
  function laadReviews() { return api("/reviews").then(function (l) { reviewsTonen(l || []); }); }
  function laadAanvragen() { return api("/aanvragen").then(function (l) { aanvragenTonen(l || []); }); }

  function laadAlles() {
    fetch("assets/teksten.json").then(function (r) { return r.json(); }).then(function (t) {
      alleTeksten = t;
      return api("/teksten");
    }).then(function (a) {
      aanpassingen = a || {};
      tekstenTonen("");
    });
    laadProjecten(); laadReviews(); laadAanvragen();
  }

  api("/status").then(function (r) { toon(!!(r && r.ingelogd)); })
    .catch(function () { toon(false); });
})();
