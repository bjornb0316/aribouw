# -*- coding: utf-8 -*-
"""Home, diensten en werk."""
import bouw as B
import data as D

WA_FOTO = D.wa_link("Hallo, ik stuur wat foto's van de ruimte. Kunt u meedenken?")


# =====================================================================
# HOME
# =====================================================================
def index(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "index.html",
              "Aribouw Zevenaar | Schilderwerk, behang en kleine renovaties",
              "Binnen- en buitenschilderwerk, behang en kleine renovaties in Zevenaar, Arnhem en "
              "omgeving. %s uit %s reviews op Werkspot." % (D.SCORE, D.AANTAL_REVIEWS),
              "Hallo, ik wil graag een offerte voor schilderwerk.",
              extra='<script type="application/ld+json">%s</script>' % D.JSONLD,
              kopklasse="kop--over" if aflak else "")

    if aflak:
        # Hero over de volle breedte, met een echte voor-en-na van dezelfde
        # deur eroverheen. Voor een schilder is de deur het onderwerp, niet
        # de kamer: daar zie je de verandering het scherpst.
        h += """
  <section class="hero--vol">
    <div class="schuif" data-schuif style="--x:58%%">
      <img src="../assets/img/deur-voor.webp" width="1000" height="1250" fetchpriority="high"
           alt="Binnendeur met houtlook, voor het schilderen">
      <img class="schuif-na" src="../assets/img/deur-na.webp" width="1000" height="1250"
           fetchpriority="high" alt="Dezelfde deur na het schilderen, in gebroken wit">
      <span class="schuif-merk schuif-merk--voor">Voor</span>
      <span class="schuif-merk schuif-merk--na">Na</span>
      <div class="schuif-greep" role="slider" tabindex="0" aria-valuemin="0" aria-valuemax="100"
           aria-valuenow="58" aria-label="Schuif om de deur voor en na te vergelijken"></div>
    </div>
    <div class="wrap">
      <p class="label op">Zevenaar &middot; Arnhem &middot; Duiven</p>
      <h1 class="display op">Strak tot in de hoek waar niemand kijkt.</h1>
      <p class="intro op">Binnen- en buitenschilderwerk, behang en kleine renovaties. %s uit %s
      reviews op Werkspot.</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%s">Stuur foto&#39;s via WhatsApp</a>
      </div>
    </div>
  </section>
""" % (D.SCORE, D.AANTAL_REVIEWS, WA_FOTO)
    else:
        # Rustiger: kop op de rail, beeld in een hoge kolom die rechts van
        # het scherm afloopt.
        h += """
  <section class="hero">
    <div class="hero-in">
      <div class="hero-tekst">
        <p class="label op">Zevenaar &middot; Arnhem &middot; Duiven</p>
        <h1 class="display op">Strak tot in de hoek waar niemand kijkt.</h1>
        <p class="intro op">Binnen- en buitenschilderwerk, behang en kleine renovaties. %s uit %s
        reviews op Werkspot.</p>
        <div class="knopgroep op">
          <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
          <a class="knop knop--lijn" href="%s">Stuur foto&#39;s via WhatsApp</a>
        </div>
      </div>
      <div class="hero-beeld op">
        <img src="../assets/img/pui-voetzorg.webp" width="1600" height="1000" fetchpriority="high"
             alt="Geschilderde pui en deur van een praktijkruimte in antraciet">
      </div>
    </div>
  </section>
""" % (D.SCORE, D.AANTAL_REVIEWS, WA_FOTO)

    h += B.gebiedstrip()

    if aflak:
        h += kleurkiezer()
        h += B.snee()

    # ---- diensten als kleurstalen ----
    h += '  <section class="sectie%s">\n    <div class="wrap rail">\n' % (
        "" if aflak else " sectie--zand")
    h += B.railkop("Wat we doen", "Vier dingen, en die goed",
                   "Schilderen, behangen, afwerken",
                   "Geen klusbedrijf met twintig diensten. Dit is waar Aribouw op wordt gebeld, "
                   "en waar de reviews over gaan.")
    h += B.kaarten(variant)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=not aflak)

    # ---- werk ----
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Werk", "Foto&#39;s van eigen klussen", "Uit Zevenaar en omgeving",
                   "Er staan er nog niet veel op. Wat er staat is eigen werk, geen ingekocht "
                   "beeld.")
    h += B.werkraster(3)
    h += ('        <p class="klein" style="margin-top:1.6rem"><a href="werk.html" '
          'style="text-decoration:underline;text-underline-offset:3px">Alle foto&#39;s</a></p>\n')
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.werkwijze(" sectie--vlak" if aflak else " sectie--zand")

    # ---- reviews ----
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Reviews", "Wat klanten op Werkspot schrijven",
                   "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                   "Deze staan er letterlijk zo, met naam en datum erbij. Ze zijn openbaar na te "
                   "lezen.")
    h += B.reviews(4)
    h += B.scoreblok()
    h += "      </div>\n    </div>\n  </section>\n"

    # ---- vragen ----
    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Waar mensen meestal over twijfelen", "Vijf van de negen")
    h += B.vragen(D.VRAGEN[:5])
    h += ('        <p class="klein" style="margin-top:1.5rem"><a href="contact.html" '
          'style="text-decoration:underline;text-underline-offset:3px">Alle vragen en '
          'antwoorden</a></p>\n')
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Laat eerst even iemand kijken",
        "Aan het langskomen en de offerte zitten geen kosten. Daarna weet u wat er nodig is en "
        "waar de uren in gaan zitten.")
    return h + B.voet(variant)


# =====================================================================
# KLEURKIEZER (alleen Aflak)
# =====================================================================
def kleurkiezer():
    return """
  <section class="sectie">
    <div class="wrap rail">
      <div class="rail-kop">
        <span class="rail-naam">Kleur</span>
        <p>Vier richtingen</p>
      </div>
      <div class="rail-in">
        <h2 class="display">Waar denkt u aan?</h2>
        <p class="intro" style="margin-top:.9rem">De kleur is bijna altijd het langste gesprek.
        Klik op de richting die u het meest aanspreekt, dan leest u waar bij die keuze op gelet
        moet worden. Het gaat mee in de aanvraag, zodat het gesprek daar niet meer bij nul
        begint.</p>

        <div data-stalen style="margin-top:2rem">
          <div class="stalen op" data-stagger>
            <button class="staal" type="button" data-staal="licht" aria-pressed="false">
              <span class="staal-vlak" style="background:#EFEBE3"></span>
              <span class="staal-in"><b>Wit en gebroken wit</b><small>Het meest gekozen</small></span>
            </button>
            <button class="staal" type="button" data-staal="warm" aria-pressed="false">
              <span class="staal-vlak" style="background:#C9B79C"></span>
              <span class="staal-in"><b>Warme tinten</b><small>Zand, klei, taupe</small></span>
            </button>
            <button class="staal" type="button" data-staal="donker" aria-pressed="false">
              <span class="staal-vlak" style="background:#2F3A44"></span>
              <span class="staal-in"><b>Donker en diep</b><small>Op een deur of een wand</small></span>
            </button>
            <button class="staal" type="button" data-staal="weetniet" aria-pressed="false">
              <span class="staal-vlak" style="background:linear-gradient(135deg,#EFEBE3 0 33%,#C9B79C 33% 66%,#2F3A44 66% 100%)"></span>
              <span class="staal-in"><b>Nog geen idee</b><small>Ook prima</small></span>
            </button>
          </div>

          <div class="stalen-uit" data-stalen-uit data-aan="0" role="status">
            <b data-stalen-kop></b>
            <p data-stalen-uitleg></p>
            <div class="knopgroep">
              <a class="knop knop--vol" data-stalen-link href="offerte.html">Verder met deze richting</a>
              <a class="knop knop--lijn" data-stalen-wa href="#">Even overleggen via WhatsApp</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""


# =====================================================================
# DIENSTEN
# =====================================================================
def diensten(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "diensten.html",
              "Diensten | Aribouw Zevenaar",
              "Binnenschilderwerk, buitenschilderwerk, behang en kleine renovaties. Wat elk van "
              "die vier inhoudt en waar de uren in gaan zitten.",
              "Hallo, ik heb een vraag over jullie diensten.")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:17ch">Het voorwerk is het werk</h1>
      <p class="intro op" style="margin-top:1.1rem">Verf kopen kan iedereen. Het verschil zit in
      wat eraan voorafgaat: ontvetten, schuren, plamuren, aftapen. Daar gaan de uren in zitten en
      daar wordt een klus later op afgerekend.</p>
    </div>
  </section>
"""

    # Twee blokken met beeld, daarna de rest als stalen. Nooit meer dan
    # twee beeld-tekst-splits achter elkaar.
    h += '  <section class="sectie sectie--zand">\n    <div class="wrap">\n'
    for i, (slug, naam, kort, lang, beeld, punten) in enumerate(D.DIENSTEN[:2]):
        link = ("dienst-%s.html" % slug) if aflak else "offerte.html"
        knop = ("Meer over %s" % naam.lower()) if aflak else "Offerte aanvragen"
        om = " blok--om" if i == 1 else ""
        h += """      <div class="blok%s op">
        <div class="blok-beeld">
          <img src="../assets/img/%s" width="1000" height="750" loading="lazy" alt="%s">
        </div>
        <div>
          <h2 class="display">%s</h2>
          <p class="intro" style="margin-top:.9rem">%s</p>
          <ul class="punten">%s</ul>
          <div class="knopgroep" style="margin-top:1.6rem">
            <a class="knop knop--lijn knop--klein" href="%s">%s</a>
          </div>
        </div>
      </div>
""" % (om, beeld, kort, naam, lang, "".join("<li>%s</li>" % p for p in punten), link, knop)
    h += "    </div>\n  </section>\n"

    h += B.snee(zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("En verder", "Behang en de kleine dingen", "Twee van de vier",
                   "Los te doen, en meestal onderdeel van dezelfde planning.")
    h += '        <div class="kaarten kaarten--twee op" data-stagger>\n'
    for slug, naam, kort, lang, beeld, punten in D.DIENSTEN[2:]:
        link = ("dienst-%s.html" % slug) if aflak else "offerte.html"
        h += ('          <a class="kaart" href="%s"><span class="kaart-baan"></span>'
              '<span class="kaart-in"><h3 class="display">%s</h3><p>%s</p>'
              '<span class="meer">%s %s</span></span></a>\n'
              % (link, naam, kort, "Wat dat inhoudt" if aflak else "Offerte aanvragen", B.PIJL))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Niet zeker wat u nodig heeft",
        "Dat hoeft ook niet. Stuur een paar foto&#39;s of laat er iemand langskomen, dan hoort u "
        "wat er nodig is en wat kan blijven.")
    return h + B.voet(variant)


# =====================================================================
# WERK
# =====================================================================
def werk(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "werk.html",
              "Werk | Aribouw Zevenaar",
              "Foto's van eigen klussen: schilderwerk binnen en buiten, in Zevenaar en omgeving.",
              "Hallo, ik zag jullie werk. Kunnen jullie iets soortgelijks doen?")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:15ch">Eigen werk, eerlijk aantal</h1>
      <p class="intro op" style="margin-top:1.1rem">Er staan er nog niet veel op. Wat er staat is
      van eigen klussen, geen ingekocht beeld. Meer werk is te zien op het Werkspot-profiel, waar
      ook de reviews staan.</p>
    </div>
  </section>
"""

    h += '  <section class="sectie sectie--zand" style="padding-top:clamp(2rem,4vw,3rem)">\n'
    h += '    <div class="wrap rail">\n'
    h += B.railkop("Voor en na", "Een binnendeur in een kantoorpand",
                   "Van houtlook naar gebroken wit",
                   "Dezelfde deur, voor en na. Bij een deur zie je het verschil het scherpst: het "
                   "vlak is groot en er is geen meubel dat de aandacht wegtrekt.")
    if aflak:
        h += """        <div class="vergelijk op" data-schuif style="--x:55%">
          <img src="../assets/img/deur-voor-breed.webp" width="1100" height="825" loading="lazy"
               alt="Binnendeur met houtlook voor het schilderen">
          <img class="schuif-na" src="../assets/img/deur-na-breed.webp" width="1100" height="825"
               loading="lazy" alt="Dezelfde deur na het schilderen in gebroken wit">
          <span class="schuif-merk schuif-merk--voor">Voor</span>
          <span class="schuif-merk schuif-merk--na">Na</span>
          <div class="schuif-greep" role="slider" tabindex="0" aria-valuemin="0" aria-valuemax="100"
               aria-valuenow="55" aria-label="Schuif om voor en na te vergelijken"></div>
        </div>
"""
    else:
        h += """        <div class="voorna op">
          <figure>
            <img src="../assets/img/deur-voor-breed.webp" width="1100" height="825" loading="lazy"
                 alt="Binnendeur met houtlook voor het schilderen">
            <figcaption>Voor</figcaption>
          </figure>
          <figure>
            <img src="../assets/img/deur-na-breed.webp" width="1100" height="825" loading="lazy"
                 alt="Dezelfde deur na het schilderen in gebroken wit">
            <figcaption>Na</figcaption>
          </figure>
        </div>
"""
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Alle foto&#39;s", "Binnen, buiten en de details",
                   "Zes beelden",
                   "De pui hieronder hoort bij de review van Cindy uit Westervoort: een "
                   "voormalige garage die praktijkruimte werd.")
    h += B.werkraster(6)
    h += ('        <p class="klein" style="margin-top:1.8rem">Meer werk en alle reviews staan op '
          'het <a href="%s" style="text-decoration:underline;text-underline-offset:3px">'
          'Werkspot-profiel</a>.</p>\n' % D.WERKSPOT)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Zoiets voor uw woning",
        "Stuur een foto van de ruimte of het kozijn, dan hoort u wat er nodig is.")
    return h + B.voet(variant)
