# -*- coding: utf-8 -*-
"""Over, werkgebied, offerte, contact, dienstpagina's en plaatspagina's."""
import bouw as B
import data as D


# =====================================================================
# OVER (alleen Grondlaag)
# =====================================================================
def over(variant):
    h = B.kop(variant, "over.html",
              "Over Aribouw | Schilder in Zevenaar",
              "Aribouw is een schildersbedrijf uit Zevenaar. Schilderwerk, behang en kleine "
              "renovaties, met %s uit %s reviews op Werkspot." % (D.SCORE, D.AANTAL_REVIEWS),
              "Hallo, ik heb een vraag over jullie bedrijf.")

    h += """
  <section class="sectie">
    <div class="wrap">
      <div class="blok op" style="border:0;padding-top:0">
        <div>
          <h1 class="display" style="max-width:16ch">Een schilder die opruimt</h1>
          <p class="intro" style="margin-top:1.2rem">Aribouw zit in Zevenaar en werkt in de
          Liemers en daarbuiten. %s doet het werk zelf, dus u praat met degene die ook de kwast
          vasthoudt.</p>
          <p style="margin-top:1rem;color:var(--inkt-2)">Lees de reviews op Werkspot en er valt
          iets op: het gaat bijna nooit over de verf. Het gaat over afspraken nakomen, netjes
          werken, meedenken en terugkomen voor de laatste punten. Dat is ook precies waar de
          meeste klachten over schilders over gaan, alleen dan andersom.</p>
          <p style="margin-top:1rem;color:var(--inkt-2)">Werk komt via mond-tot-mond en via
          Werkspot. Daar staan de beoordelingen openbaar, inclusief de reacties eronder.</p>
          <div class="knopgroep" style="margin-top:1.7rem">
            <a class="knop knop--lijn" href="%s">Bekijk het Werkspot-profiel</a>
          </div>
        </div>
        <div class="blok-beeld">
          <img src="../assets/img/pui-detail.webp" width="1200" height="900" fetchpriority="high"
               alt="Detail van een strak geschilderd kozijn en de aansluiting op het metselwerk">
        </div>
      </div>
    </div>
  </section>
""" % (D.PERSOON, D.WERKSPOT)

    h += B.gebiedstrip()
    h += B.werkwijze(" sectie--zand")
    h += B.snee(om=True, zand=True)

    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Reviews", "Wat klanten schrijven",
                   "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                   "Letterlijk overgenomen van Werkspot, met naam en datum erbij.")
    h += B.reviews(4)
    h += B.scoreblok()
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Even kennismaken op locatie",
        "Aan het langskomen en de offerte zitten geen kosten, en u zit nergens aan vast.")
    return h + B.voet(variant)


# =====================================================================
# WERKGEBIED (alleen Aflak)
# =====================================================================
def werkgebied(variant):
    h = B.kop(variant, "werkgebied.html",
              "Werkgebied | Aribouw in Zevenaar, Arnhem, Duiven en Westervoort",
              "Aribouw werkt in Zevenaar, Arnhem, Duiven, Westervoort en omgeving. Schilderwerk, "
              "behang en kleine renovaties.",
              "Hallo, komen jullie ook in mijn plaats?")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:16ch">Waar we komen</h1>
      <p class="intro op" style="margin-top:1.1rem">Aribouw werkt vanuit Zevenaar. De reviews op
      Werkspot komen uit Driel, Huissen, Westervoort, Kilder en zelfs Apeldoorn, dus er wordt
      verder gereden dan alleen de Liemers. Staat uw plaats er niet bij, bel dan gerust.</p>
    </div>
  </section>

  <section class="sectie" style="padding-top:0">
    <div class="wrap">
      <div class="regio-lijst op" data-stagger>
"""
    for plaats in D.WERKGEBIED:
        h += ('        <a href="regio-%s.html"><b>%s</b><span>Schilderwerk, behang en '
              'afwerking</span></a>\n' % (plaats.lower(), plaats))
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee()
    h += '  <section class="sectie sectie--vlak">\n    <div class="wrap rail">\n'
    h += B.railkop("Reviews", "Uit het hele werkgebied",
                   "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                   "De plaatsnamen onder de reviews laten zien hoe ver het werkgebied echt "
                   "reikt.")
    h += B.reviews(4)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Komen jullie ook bij mij",
        "Geef uw plaats door, dan hoort u meteen of het past.")
    return h + B.voet(variant)


# =====================================================================
# OFFERTE
# =====================================================================
def offerte(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "offerte.html",
              "Offerte aanvragen | Aribouw Zevenaar",
              "Vraag een vrijblijvende offerte aan voor schilderwerk, behang of een kleine "
              "renovatie. Eerst kijken, dan pas een prijs.",
              "Hallo, ik wil graag een offerte aanvragen.")

    if not aflak:
        h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:17ch">Vrijblijvend een prijs</h1>
      <p class="intro op" style="margin-top:1.1rem">Vul in wat er speelt, dan wordt er contact
      opgenomen om langs te komen. Aan het langskomen en de offerte zitten geen kosten.</p>
    </div>
  </section>
"""
        h += B.werkwijze(" sectie--zand")
        h += B.contactblok(
            "Vul in wat er speelt",
            "Hoe meer u kwijt wilt, hoe gerichter er kan worden meegedacht. Foto&#39;s stuurt u "
            "het makkelijkst via WhatsApp.")
        return h + B.voet(variant)

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:18ch">Zes stappen, dan weet u waar u aan toe
      bent</h1>
      <p class="intro op" style="margin-top:1.1rem">Klikken in plaats van typen. Pas op het eind
      drie velden. Daarna staat uw situatie in een WhatsApp-bericht dat alleen nog verzonden hoeft
      te worden.</p>
    </div>
  </section>

  <section class="sectie" style="padding-top:0">
    <div class="wrap" style="max-width:52rem">
      <div class="flow op" data-flow
           data-flow-bericht="Hallo, ik heb via de site een offerte aangevraagd. Mijn situatie:">
        <div class="flow-top">
          <span class="flow-telling" data-flow-telling>Stap 1 van 6</span>
          <button class="flow-terug" type="button" data-flow-terug hidden>Vorige stap</button>
        </div>
        <div class="flow-balk"><i data-flow-balk style="width:0"></i></div>

        <div data-stap data-aan="1">
          <h3 class="display">Wat moet er gebeuren?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="binnenschilderwerk">Binnenschilderwerk<small>Muren, plafonds, deuren</small></button>
            <button class="keuze" type="button" data-waarde="buitenschilderwerk">Buitenschilderwerk<small>Kozijnen, deuren, boeidelen</small></button>
            <button class="keuze" type="button" data-waarde="behang">Behang<small>Aanbrengen of verwijderen</small></button>
            <button class="keuze" type="button" data-waarde="meerdere dingen">Meerdere dingen tegelijk</button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Om hoeveel gaat het ongeveer?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="een ruimte">Een ruimte<small>Of een paar kozijnen</small></button>
            <button class="keuze" type="button" data-waarde="meerdere ruimtes">Meerdere ruimtes</button>
            <button class="keuze" type="button" data-waarde="de hele woning">De hele woning</button>
            <button class="keuze" type="button" data-waarde="een bedrijfspand">Een bedrijfspand</button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Welke kleurrichting?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="licht">Wit of gebroken wit</button>
            <button class="keuze" type="button" data-waarde="warm">Een warme tint</button>
            <button class="keuze" type="button" data-waarde="donker">Donker en diep</button>
            <button class="keuze" type="button" data-waarde="weetniet">Weet ik nog niet</button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Hoe is de ondergrond nu?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="al geschilderd en netjes">Al geschilderd en netjes</button>
            <button class="keuze" type="button" data-waarde="behangen">Nu behangen</button>
            <button class="keuze" type="button" data-waarde="kaal of beschadigd">Kaal of beschadigd</button>
            <button class="keuze" type="button" data-waarde="dat weet ik niet">Dat weet ik niet</button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Wanneer zou het moeten gebeuren?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="zo snel mogelijk">Zo snel mogelijk</button>
            <button class="keuze" type="button" data-waarde="binnen een paar maanden">Binnen een paar maanden</button>
            <button class="keuze" type="button" data-waarde="nog aan het orienteren">Ik ori&euml;nteer me nog</button>
            <button class="keuze" type="button" data-waarde="rond een verhuizing">Rond een verhuizing</button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Waar kunnen we u bereiken?</h3>
          <div class="velden-2">
            <div class="veld"><label for="of-naam">Uw naam</label>
              <input id="of-naam" name="naam" type="text" autocomplete="name" required>
              <span class="fout">Vul uw naam in.</span></div>
            <div class="veld"><label for="of-tel">Telefoonnummer</label>
              <input id="of-tel" name="tel" type="tel" autocomplete="tel" required>
              <span class="fout">Vul een telefoonnummer in.</span></div>
          </div>
          <div class="veld"><label for="of-plaats">Plaats</label>
            <input id="of-plaats" name="plaats" type="text" autocomplete="address-level2" required>
            <span class="fout">Vul uw plaats in.</span></div>
          <button class="knop knop--vol" type="button" data-flow-verstuur>Offerte aanvragen</button>
          <p class="formulier-noot">Vrijblijvend. Foto&#39;s stuurt u daarna het makkelijkst via
          WhatsApp; dat werkt sneller dan uploaden.</p>
        </div>

        <div class="flow-klaar" data-klaar data-aan="0" role="status">
          <b>Aanvraag genoteerd.</b>
          <p>U wordt gebeld om een moment af te spreken. Met de knop hieronder staat uw situatie
          al in een WhatsApp-bericht; u hoeft alleen nog op verzenden te drukken en er eventueel
          foto&#39;s bij te doen.</p>
          <div class="flow-samen" data-flow-samen></div>
          <p class="klein" style="color:var(--licht-3)">In deze voorbeeldpagina gaat er nog niets
          echt de deur uit.</p>
          <div class="knopgroep" style="margin-top:1.2rem">
            <a class="knop knop--vol" data-wa href="#">Bericht openen in WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    h += B.snee()
    h += '  <section class="sectie sectie--vlak">\n    <div class="wrap rail">\n'
    h += B.railkop("Daarna", "Wat er gebeurt na uw aanvraag", "Geen verkooptraject",
                   "Er wordt gekeken, u hoort wat er nodig is, en pas daarna komt er een prijs.")
    h += B.vragen(D.VRAGEN[:4], "na-aanvraag")
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Liever gewoon even bellen",
        "Kan ook. Dan hoort u meteen of het iets is waar Aribouw bij past.")
    return h + B.voet(variant)


# =====================================================================
# CONTACT
# =====================================================================
def contact(variant):
    h = B.kop(variant, "contact.html",
              "Contact | Aribouw Zevenaar",
              "Bel, app of mail Aribouw in Zevenaar. Schilderwerk, behang en kleine renovaties in "
              "Zevenaar, Arnhem en omgeving.",
              "Hallo, ik heb een vraag.")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:14ch">Contact</h1>
      <p class="intro op" style="margin-top:1.1rem">Bellen of appen gaat het snelst. Een paar
      foto&#39;s van de ruimte helpen om meteen mee te denken, ook als u nog niets wilt
      afspreken.</p>
    </div>
  </section>
"""
    h += B.contactblok(
        "Stuur een bericht",
        "Er wordt zo snel mogelijk gereageerd. Heeft u haast, bel dan gerust.")

    h += B.snee(om=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Alle vragen en antwoorden", "Negen stuks",
                   "Alles wat bij een eerste bezoek aan de keukentafel voorbijkomt, alvast op een "
                   "rij.")
    h += B.vragen(D.VRAGEN, "alle-vragen")
    h += "      </div>\n    </div>\n  </section>\n"
    return h + B.voet(variant)


# =====================================================================
# DIENSTPAGINA (alleen Aflak)
# =====================================================================
def dienstpagina(variant, dienst):
    slug, naam, kort, lang, beeld, punten = dienst
    andere = [d for d in D.DIENSTEN if d[0] != slug]
    vraagset = D.VRAGEN[:4] if slug in ("binnenschilderwerk", "behang") else D.VRAGEN[4:8]

    h = B.kop(variant, "diensten.html",
              "%s in Zevenaar en omgeving | Aribouw" % naam,
              "%s Werkgebied Zevenaar, Arnhem, Duiven en Westervoort." % kort,
              "Hallo, ik heb een vraag over %s." % naam.lower(),
              extra='<script type="application/ld+json">%s</script>' % D.vraag_jsonld(vraagset))

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <p class="label op"><a href="diensten.html">Diensten</a></p>
      <h1 class="display op" style="margin-top:.8rem;max-width:16ch">%(naam)s</h1>
      <p class="intro op" style="margin-top:1.1rem">%(kort)s</p>
      <div class="knopgroep op" style="margin-top:1.7rem">
        <a class="knop knop--vol" href="offerte.html?werk=%(werk)s">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%(wa)s">Foto sturen via WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="sectie sectie--zand" style="padding-top:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <div class="blok op" style="border:0;padding-top:0">
        <div class="blok-beeld">
          <img src="../assets/img/%(beeld)s" width="1000" height="750" fetchpriority="high"
               alt="%(kort)s">
        </div>
        <div>
          <h2 class="display">Waar de uren in gaan zitten</h2>
          <p class="intro" style="margin-top:.9rem">%(lang)s</p>
          <ul class="punten">%(punten)s</ul>
        </div>
      </div>
    </div>
  </section>
""" % dict(naam=naam, kort=kort, lang=lang, beeld=beeld,
           punten="".join("<li>%s</li>" % p for p in punten),
           werk=slug if slug in ("binnenschilderwerk", "buitenschilderwerk", "behang")
                else "meerdere dingen",
           wa=D.wa_link("Hallo, ik stuur een foto voor %s." % naam.lower()))

    h += B.werkwijze(" sectie--vlak")
    h += B.snee()

    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Vragen over %s" % naam.lower(), "Vier stuks")
    h += B.vragen(vraagset, "vragen-" + slug)
    h += "      </div>\n    </div>\n  </section>\n"

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("En verder", "Vaak in dezelfde klus", "Drie andere diensten")
    h += '        <div class="kaarten op" data-stagger>\n'
    for s2, n2, k2, l2, b2, p2 in andere:
        h += ('          <a class="kaart" href="dienst-%s.html"><span class="kaart-baan"></span>'
              '<span class="kaart-in"><h3 class="display">%s</h3><p>%s</p>'
              '<span class="meer">Wat dat inhoudt %s</span></span></a>\n'
              % (s2, n2, k2, B.PIJL))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Laat er iemand naar kijken",
        "Aan het langskomen en de offerte zitten geen kosten. U hoort wat er nodig is en wat kan "
        "blijven.")
    return h + B.voet(variant)


# =====================================================================
# PLAATSPAGINA (alleen Aflak)
# =====================================================================
def regiopagina(variant, plaats):
    anderen = [p for p in D.WERKGEBIED if p != plaats]
    h = B.kop(variant, "werkgebied.html",
              "Schilder in %s | Aribouw" % plaats,
              "Schilderwerk, behang en kleine renovaties in %s. Aribouw zit in Zevenaar en werkt "
              "in de hele regio." % plaats,
              "Hallo, ik woon in %s en heb een vraag." % plaats)

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <p class="label op"><a href="werkgebied.html">Werkgebied</a></p>
      <h1 class="display op" style="margin-top:.8rem;max-width:16ch">Schilder in %(plaats)s</h1>
      <p class="intro op" style="margin-top:1.1rem">Aribouw werkt vanuit Zevenaar, dus %(plaats)s
      ligt in de buurt. Binnen- en buitenschilderwerk, behang en de kleine dingen die erbij horen,
      met %(score)s uit %(aantal)s reviews op Werkspot.</p>
      <div class="knopgroep op" style="margin-top:1.7rem">
        <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="werk.html">Bekijk eerder werk</a>
      </div>
    </div>
  </section>
""" % dict(plaats=plaats, score=D.SCORE, aantal=D.AANTAL_REVIEWS)

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Wat we doen", "In %s ook" % plaats, "Vier diensten",
                   "Dezelfde vier dingen als in de rest van het werkgebied.")
    h += B.kaarten(variant)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("In de buurt", "Ook hier", "Drie plaatsen")
    h += '        <div class="regio-lijst op" data-stagger>\n'
    for p in anderen:
        h += ('          <a href="regio-%s.html"><b>%s</b><span>Schilderwerk, behang en '
              'afwerking</span></a>\n' % (p.lower(), p))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Een afspraak in %s" % plaats,
        "Geef door wat er speelt, dan wordt er gebeld om een moment af te spreken.")
    return h + B.voet(variant)
