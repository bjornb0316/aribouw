# -*- coding: utf-8 -*-
"""Home, diensten en werk."""
import bouw as B
import data as D

WA_FOTO = D.wa_link("Hallo, ik stuur wat foto's van de ruimte. Kunt u meedenken?")


def vergelijk(x, paar=None):
    """Een echte voor-en-na, sleepbaar. Standaard het eerste paar uit B.VOORNA."""
    voor, na, titel, onder, alt_voor, alt_na = paar or B.VOORNA[0]
    return """        <div class="vergelijk op" data-schuif style="--x:%s%%">
          <img src="../assets/img/%s" width="1100" height="825" loading="lazy"
               alt="%s">
          <img class="schuif-na" src="../assets/img/%s" width="1100" height="825"
               loading="lazy" alt="%s">
          <span class="schuif-merk schuif-merk--voor">Voor</span>
          <span class="schuif-merk schuif-merk--na">Na</span>
          <div class="schuif-greep" role="slider" tabindex="0" aria-valuemin="0" aria-valuemax="100"
               aria-valuenow="%s" aria-label="Schuif om voor en na te vergelijken: %s"></div>
        </div>
""" % (x, voor, alt_voor, na, alt_na, x, titel.lower())


# =====================================================================
# HOME
# =====================================================================
def index(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "index.html",
              "Schilder in Westervoort, Arnhem en omgeving | Aribouw",
              "Aribouw is het schildersbedrijf van %s uit Westervoort. Binnen- en "
              "buitenschilderwerk, behangen en houtreparaties. %s uit %s reviews op Werkspot."
              % (D.EIGENAAR, D.SCORE, D.AANTAL_REVIEWS),
              "Hallo, ik wil graag een offerte voor schilderwerk.",
              extra=('<script type="application/ld+json">%s</script>' % D.bedrijf_jsonld(variant)) +
                    ('\n<link rel="preload" as="image" href="../assets/film/snijlijn.webp" '
                     'fetchpriority="high">' if aflak else ""))

    # De zoekterm hoort in de h1: "schilder" plus de plaats. De merkzin blijft
    # de grote regel, de zoekterm staat er als label boven, maar binnen
    # dezelfde h1. Zo leest Google "Schilder in Westervoort, Arnhem en
    # omgeving. Strak schilderwerk, tot in de hoek waar niemand kijkt."
    kop = """      <h1 class="hero-h1 op"><span class="label">Schilder in Westervoort, Arnhem en omgeving</span>
      <span class="display">Strak schilderwerk, tot in de hoek waar niemand kijkt.</span></h1>
      <p class="intro op">Binnen- en buitenschilderwerk, behangen en houtreparaties. Persoonlijk
      uitgevoerd door %s.</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%s">Stuur foto&#39;s via WhatsApp</a>
      </div>
""" % (D.EIGENAAR, WA_FOTO)

    if aflak:
        # De snijlijn als film: tape eraf, en wat overblijft is een
        # kaarsrechte rand tussen blauw en wit. Dat is wat een schilder
        # verkoopt. De film speelt een keer en blijft op die lijn staan.
        h += B.filmhero(kop, "snijlijn", klasse="hero--home")
    else:
        # Rustiger: kop op de rail, beeld in een hoge kolom die rechts van
        # het scherm afloopt.
        h += """
  <section class="hero">
    <div class="hero-in">
      <div class="hero-tekst">
%s      </div>
      <div class="hero-beeld op">
        <img src="../assets/img/pui-voetzorg.webp" width="1600" height="1000" fetchpriority="high"
             alt="Geschilderde pui en deur van een praktijkruimte in antraciet">
      </div>
    </div>
  </section>
""" % kop

    if not aflak:
        h += B.gebiedstrip()
        h += diensten_blok(variant)
        h += B.snee(om=True, zand=True)
        h += werk_blok(variant)
        h += B.werkwijze(" sectie--zand")
        h += reviews_blok(variant)
        h += vragen_blok(variant)
        h += B.contactblok(
            "Laat mij eerst even kijken",
            "Aan het langskomen en de offerte zitten geen kosten. Daarna weet u wat er nodig is "
            "en waar de uren in gaan zitten.", variant=variant)
        return h + B.voet(variant)

    # Aflak: eerst overtuigen, dan pas spelen. Hero, vertrouwen, diensten,
    # eigen werk, kleurhulp, werkwijze, Ahmad, reviews, vragen, aanvraag.
    h += B.vertrouwen()
    h += diensten_blok(variant)
    h += B.snee(om=True)
    h += werk_blok(variant)
    h += B.snee()
    h += kleurkiezer()
    h += B.werkwijze(" sectie--vlak", beelden=True)
    h += over_ahmad()
    h += B.snee(om=True)
    h += reviews_blok(variant)
    h += vragen_blok(variant)
    h += B.contactblok(
        "Laat mij eerst even kijken",
        "Aan het langskomen en de offerte zitten geen kosten. Daarna weet u wat er nodig is en "
        "waar de uren in gaan zitten.", variant=variant)
    return h + B.voet(variant)


def diensten_blok(variant):
    aflak = variant == "aflak"
    h = '  <section class="sectie%s">\n    <div class="wrap rail">\n' % (
        "" if aflak else " sectie--zand")
    h += B.railkop("Wat ik doe", "Vier dingen, en die goed",
                   "Schilderen, behangen, houtwerk",
                   "Aribouw is een schilder, geen algemeen bouwbedrijf. Dit is waar ik voor word "
                   "gebeld, en waar de reviews over gaan.")
    h += B.kaarten(variant)
    if aflak:
        h += B.werkzaamheden(variant)
        h += B.ctaregel("Benieuwd wat dit bij uw woning kost? Ik kom vrijblijvend kijken.",
                        [("Offerte aanvragen", "offerte.html", "vol")])
    h += "      </div>\n    </div>\n  </section>\n"
    return h


def werk_blok(variant):
    aflak = variant == "aflak"
    h = '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Werk", "Foto&#39;s van eigen klussen", "Uit de regio",
                   "Wat hier staat is eigen werk, geen ingekocht beeld." +
                   (" Begin bij de deur: sleep de lijn en zie het verschil." if aflak else ""))
    if aflak:
        h += vergelijk("55")
    h += B.werkraster(3)
    if aflak:
        h += B.ctaregel("Een vergelijkbare klus? Stuur een foto, dan zeg ik wat er nodig is.",
                        [("Stuur een foto via WhatsApp",
                          D.wa_link("Hallo, ik heb een vergelijkbare klus. Ik stuur een foto."),
                          "vol"),
                         ("Alle foto&#39;s", "werk.html", "lijn")])
    else:
        h += ('        <p class="klein" style="margin-top:1.6rem"><a href="werk.html" '
              'style="text-decoration:underline;text-underline-offset:3px">Alle foto&#39;s</a></p>\n')
    h += "      </div>\n    </div>\n  </section>\n"
    return h


def reviews_blok(variant):
    aflak = variant == "aflak"
    h = '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Reviews", "Wat klanten op Werkspot schrijven",
                   "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                   "Deze staan er letterlijk zo, met naam en datum erbij. Ze zijn openbaar na te "
                   "lezen.")
    h += B.reviews(4)
    h += B.scoreblok()
    if aflak:
        h += B.ctaregel("Ook uw schilderwerk laten bekijken?",
                        [("Offerte aanvragen", "offerte.html", "vol"),
                         ("Bel %s" % D.TEL_TOON, "tel:" + D.TEL_LINK, "lijn")])
    h += "      </div>\n    </div>\n  </section>\n"
    return h


def vragen_blok(variant):
    h = '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Waar mensen meestal over twijfelen", "Vijf van de %d" % len(D.VRAGEN))
    h += B.vragen(D.VRAGEN[:5])
    h += ('        <p class="klein" style="margin-top:1.5rem"><a href="contact.html" '
          'style="text-decoration:underline;text-underline-offset:3px">Alle vragen en '
          'antwoorden</a></p>\n')
    h += "      </div>\n    </div>\n  </section>\n"
    return h


# =====================================================================
# OVER AHMAD EN ZAKELIJK (alleen Aflak, op de home)
# =====================================================================
def over_ahmad():
    # Zijn eigen woorden uit de intake van 15 september, licht ingekort.
    # Links wie er komt, rechts de route voor aannemers en architecten:
    # die wil Ahmad nadrukkelijk ook bereiken.
    return """
  <section class="sectie">
    <div class="wrap rail">
      <div class="rail-kop">
        <span class="rail-naam">Over Aribouw</span>
        <p>%(eigenaar)s</p>
      </div>
      <div class="rail-in">
        <div class="over">
          <div class="over-tekst op">
            <h2 class="display">Een nieuwe kleur en een strakke afwerking maken het verschil</h2>
            <p class="intro">Ik ben %(persoon)s. Ik vind het mooi om met schilderwerk een woning of
            ruimte echt te veranderen. Maar goed schilderwerk gaat niet alleen om schilderen: een
            goede voorbereiding, de juiste materialen en netjes werken zijn minstens zo
            belangrijk.</p>
            <p>Ik werk persoonlijk met mijn klanten, maak duidelijke afspraken en denk mee over de
            aanpak, de materialen en de kleur. Aribouw groeit stap voor stap. Het doel is om met
            een goed team ook grotere projecten te doen, met dezelfde persoonlijke aandacht.</p>
            <p class="over-naam">%(eigenaar)s, Aribouw</p>
          </div>
          <aside class="zakelijk op">
            <h3 class="display">Voor aannemers en architecten</h3>
            <p>Ook voor professionals werk ik met duidelijke afspraken over planning, materiaal en
            oplevering. Voor grotere projecten kan ik buiten de regio werken.</p>
            <ul class="punten">
              <li>Een vaste aanspreekpersoon, van opname tot oplevering</li>
              <li>Binnen- en buitenschilderwerk, behangen en houtwerk</li>
              <li>Woningen, bedrijfspanden en praktijkruimtes</li>
            </ul>
            <div class="knopgroep">
              <a class="knop knop--vol" href="offerte.html?soort=zakelijk">Project voorleggen</a>
              <a class="knop knop--lijn" href="tel:%(tellink)s">%(tel)s</a>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </section>
""" % dict(persoon=D.PERSOON, eigenaar=D.EIGENAAR, tel=D.TEL_TOON, tellink=D.TEL_LINK)


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

        <div class="kiezer" data-stalen style="margin-top:2rem">
          <figure class="kiezer-beeld op">
            <div class="kiezer-vlak">
            <img data-kleur-beeld="weetniet" data-aan="1" src="../assets/img/kleur-weetniet.webp"
                 width="1400" height="1050" loading="lazy" alt="Kleurwaaier en drie proefplankjes op een eiken tafel">
            <img data-kleur-beeld="licht" data-aan="0" src="../assets/img/kleur-licht.webp"
                 width="1400" height="1050" loading="lazy" alt="Kamer met muren in gebroken wit">
            <img data-kleur-beeld="warm" data-aan="0" src="../assets/img/kleur-warm.webp"
                 width="1400" height="1050" loading="lazy" alt="Kamer met muren in een warme zandtint">
            <img data-kleur-beeld="donker" data-aan="0" src="../assets/img/kleur-donker.webp"
                 width="1400" height="1050" loading="lazy" alt="Binnendeur in diep blauwgrijs gelakt">
            </div>
            <figcaption>Sfeerbeeld bij de richting, geen klus van Aribouw.</figcaption>
          </figure>
          <div class="kiezer-rechts">
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
    </div>
  </section>
"""


# =====================================================================
# DIENSTEN
# =====================================================================
def diensten(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "diensten.html",
              "Diensten | Aribouw, schilder in Westervoort",
              "Binnen- en buitenschilderwerk, wanden en plafonds, kozijnen en deuren, trappen, "
              "behangen en houtreparaties. Wat elk inhoudt en waar de uren in gaan zitten.",
              "Hallo, ik heb een vraag over uw diensten.")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:17ch">Het voorwerk is het werk</h1>
      <p class="intro op" style="margin-top:1.1rem">Verf kopen kan iedereen. Het verschil zit in
      wat eraan voorafgaat: ontvetten, schuren, gaatjes dichtzetten, afplakken. Daar gaan de uren
      in zitten en daar wordt een klus later op afgerekend.</p>
%s    </div>
  </section>
""" % B.werkzaamheden(variant, "werkzaamheden--intro")

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
    h += B.railkop("En verder", "Behangen en houtwerk", "Twee van de vier",
                   "Los te doen, en vaak onderdeel van dezelfde planning.")
    h += '        <div class="kaarten kaarten--twee op" data-stagger>\n'
    for dienst in D.DIENSTEN[2:]:
        link = ("dienst-%s.html" % dienst[0]) if aflak else "offerte.html"
        h += B.kaart(variant, dienst, "Wat dat inhoudt" if aflak else "Offerte aanvragen", link)
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    if aflak:
        # De specialismen met een eigen pagina.
        beelden = {"kozijnen-deuren": ("kozijn-buiten.webp", "Wit geschilderde buitenkozijnen"),
                   "wanden-plafonds": ("kleur-licht.webp", "Kamer met strak geschilderde wanden")}
        h += B.snee(om=True, zand=True)
        h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
        h += B.railkop("Specifiek", "Kozijnen, deuren, wanden en plafonds", "Veel gevraagd",
                       "Onderdelen van binnen- en buitenschilderwerk waar mensen vaak specifiek "
                       "naar zoeken, met een eigen uitleg.")
        h += '        <div class="speci op" data-stagger>\n'
        for slug, naam, kort, lang, beeld, punten in D.SUBDIENSTEN:
            src, alt = beelden[slug]
            h += ('          <a class="speci-kaart" href="dienst-%s.html"><img src="../assets/img/%s" '
                  'width="1000" height="750" loading="lazy" alt="%s"><span><h3 class="display">%s'
                  '</h3><p>%s</p><span class="meer">Wat dat inhoudt %s</span></span></a>\n'
                  % (slug, src, alt, naam, kort, B.PIJL))
        h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Niet zeker wat u nodig heeft",
        "Dat hoeft ook niet. Stuur een paar foto&#39;s of laat mij even langskomen, dan hoort u "
        "wat er nodig is en wat kan blijven.", variant=variant)
    return h + B.voet(variant)


# =====================================================================
# WERK
# =====================================================================
def werk(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "werk.html",
              "Werk | Aribouw, schilder in Westervoort",
              "Foto's van eigen klussen: schilderwerk binnen en buiten, in Westervoort, Arnhem, "
              "Nijmegen en omgeving.",
              "Hallo, ik zag uw werk op de site. Kunt u iets soortgelijks doen?")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:15ch">Eigen werk, voor en na</h1>
      <p class="intro op" style="margin-top:1.1rem">Alles op deze pagina is van eigen klussen, geen
      ingekocht of gegenereerd beeld. Meer werk en alle reviews staan op het
      Werkspot-profiel.</p>
    </div>
  </section>
"""

    h += '  <section class="sectie sectie--zand" style="padding-top:clamp(2rem,4vw,3rem)">\n'
    h += '    <div class="wrap rail">\n'
    h += B.railkop("Voor en na", B.VOORNA[0][2], B.VOORNA[0][3],
                   "Dezelfde plek, voor en na. Sleep de lijn om het verschil te zien." if aflak else
                   "Dezelfde deur, voor en na. Bij een deur zie je het verschil het scherpst: het "
                   "vlak is groot en er is geen meubel dat de aandacht wegtrekt.")
    if aflak:
        # Elk paar uit B.VOORNA krijgt een eigen schuif. Nu is dat er een;
        # de foto's die Ahmad nog stuurt komen er gewoon onder.
        for i, paar in enumerate(B.VOORNA):
            if i:
                h += ('        <h3 class="display voorna-kop op">%s</h3>\n'
                      '        <p class="klein">%s</p>\n' % (paar[2], paar[3]))
            h += vergelijk("55", paar)
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
                   "%d beelden" % len(B.WERK),
                   "De pui hieronder hoort bij de review van Cindy uit Westervoort: een "
                   "voormalige garage die praktijkruimte werd.")
    h += B.werkraster(6)
    h += ('        <p class="klein" style="margin-top:1.8rem">Meer werk en alle reviews staan op '
          'het <a href="%s" style="text-decoration:underline;text-underline-offset:3px">'
          'Werkspot-profiel</a>.</p>\n' % D.WERKSPOT)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Zoiets voor uw woning",
        "Stuur een foto van de ruimte of het kozijn, dan hoort u wat er nodig is.", variant=variant)
    return h + B.voet(variant)
