# -*- coding: utf-8 -*-
"""Over, werkgebied, offerte, contact, dienstpagina's en plaatspagina's."""
import bouw as B
import data as D


# =====================================================================
# OVER (alleen Grondlaag)
# =====================================================================
def over(variant):
    h = B.kop(variant, "over.html",
              "Over Aribouw | Schilder in Westervoort",
              "Aribouw is het schildersbedrijf van %s uit Westervoort. Schilderwerk, behangen "
              "en houtreparaties, met %s uit %s reviews op Werkspot."
              % (D.EIGENAAR, D.SCORE, D.AANTAL_REVIEWS),
              "Hallo Ahmad, ik heb een vraag.")

    h += """
  <section class="sectie">
    <div class="wrap">
      <div class="blok op" style="border:0;padding-top:0">
        <div>
          <h1 class="display" style="max-width:16ch">Een schilder die opruimt</h1>
          <p class="intro" style="margin-top:1.2rem">Ik ben %s, en Aribouw is mijn
          schildersbedrijf in Westervoort. Ik doe het werk zelf, dus u praat met degene die ook de
          kwast vasthoudt.</p>
          <p style="margin-top:1rem;color:var(--inkt-2)">Ik vind het mooi om met schilderwerk een
          woning of ruimte echt te veranderen. Een nieuwe kleur en een strakke afwerking maken een
          groot verschil. Maar goed schilderwerk gaat niet alleen om schilderen: een goede
          voorbereiding, de juiste materialen en netjes werken zijn minstens zo belangrijk.</p>
          <p style="margin-top:1rem;color:var(--inkt-2)">Ik werk voor particulieren en voor
          aannemers, architecten en andere professionals. Aribouw groeit stap voor stap, met als
          doel om met een goed team ook grotere projecten te doen, zonder de persoonlijke aandacht
          te verliezen.</p>
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
""" % (D.EIGENAAR, D.WERKSPOT)

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
              "Werkgebied | Aribouw, schilder in Westervoort, Arnhem en Nijmegen",
              "Aribouw werkt vanuit Westervoort in %s. Voor grotere projecten ook daarbuiten."
              % (", ".join(D.WERKGEBIED_ALLES[:-1]) + " en " + D.WERKGEBIED_ALLES[-1]),
              "Hallo, komt u ook in mijn plaats?")

    h += B.filmhero("""      <h1 class="display op" style="max-width:16ch">Waar ik kom</h1>
      <p class="intro op">Vanuit Westervoort werk ik in de Liemers, rond Arnhem en tot Ede en
      Nijmegen. %s Staat uw plaats er niet bij, bel dan gerust.</p>
""" % D.BUITEN_REGIO, beeld="straat-liemers.webp",
        alt="Straat met bakstenen rijtjeshuizen en witte kozijnen", klasse="hero--kort")

    # De eerste vier hebben een eigen pagina; de rest staat er als plaats bij.
    h += """
  <section class="sectie">
    <div class="wrap">
      <div class="regio-lijst op" data-stagger>
"""
    for plaats in D.WERKGEBIED_ALLES:
        if plaats in D.WERKGEBIED:
            h += ('        <a href="regio-%s.html"><b>%s %s</b><span>Schilderwerk, behangen en '
                  'houtwerk</span></a>\n' % (plaats.lower(), plaats, B.PIJL))
        else:
            h += ('        <div><b>%s</b><span>Schilderwerk, behangen en houtwerk</span></div>\n'
                  % plaats)
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
        "Komt u ook bij mij",
        "Geef uw plaats door, dan hoort u meteen of het past.", variant=variant)
    return h + B.voet(variant)


# =====================================================================
# OFFERTE
# =====================================================================
def offerte(variant):
    aflak = variant == "aflak"
    h = B.kop(variant, "offerte.html",
              "Offerte aanvragen | Aribouw, schilder in Westervoort",
              "Vraag een vrijblijvende offerte aan voor schilderwerk, behangen of houtreparaties. "
              "Eerst kijken, dan pas een prijs.",
              "Hallo, ik wil graag een offerte aanvragen.")

    if not aflak:
        h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:17ch">Vrijblijvend een prijs</h1>
      <p class="intro op" style="margin-top:1.1rem">Vul in wat er speelt, dan neem ik contact op
      om langs te komen. Aan het langskomen en de offerte zitten geen kosten.</p>
    </div>
  </section>
"""
        h += B.werkwijze(" sectie--zand")
        h += B.contactblok(
            "Vul in wat er speelt",
            "Hoe meer u kwijt wilt, hoe gerichter ik kan meedenken. Foto&#39;s stuurt u het "
            "makkelijkst via WhatsApp.")
        return h + B.voet(variant)

    h += B.filmhero("""      <h1 class="display op" style="max-width:18ch">Zes stappen, dan weet u waar u aan toe
      bent</h1>
      <p class="intro op">Klikken in plaats van typen. Pas op het eind drie velden. Daarna staat
      uw situatie in een WhatsApp-bericht dat alleen nog verzonden hoeft te worden.</p>
""", beeld="offerte-tafel.webp", alt="Keukentafel met een kleurwaaier, koffie en een offerte",
        klasse="hero--kort")

    h += """
  <section class="sectie sectie--flow">
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
            <button class="keuze" type="button" data-waarde="binnenschilderwerk">Binnenschilderwerk<small>Wanden, plafonds, deuren, trappen</small></button>
            <button class="keuze" type="button" data-waarde="buitenschilderwerk">Buitenschilderwerk<small>Kozijnen, deuren, boeidelen</small></button>
            <button class="keuze" type="button" data-waarde="behang">Behangen<small>Aanbrengen of verwijderen</small></button>
            <button class="keuze" type="button" data-waarde="meerdere dingen">Meerdere dingen tegelijk<small>Ook met houtreparaties</small></button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Om hoeveel gaat het ongeveer?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze" type="button" data-waarde="een ruimte">Een ruimte<small>Of een paar kozijnen</small></button>
            <button class="keuze" type="button" data-waarde="meerdere ruimtes">Meerdere ruimtes</button>
            <button class="keuze" type="button" data-waarde="de hele woning">De hele woning</button>
            <button class="keuze" type="button" data-waarde="een zakelijk project">Een zakelijk project<small>Voor aannemer, architect of bedrijf</small></button>
          </div>
        </div>

        <div data-stap data-aan="0">
          <h3 class="display">Welke kleurrichting?</h3>
          <div class="keuzes keuzes--2">
            <button class="keuze keuze--beeld" type="button" data-waarde="licht"><img src="../assets/img/kleur-licht.webp" width="1400" height="1050" loading="lazy" alt="">Wit of gebroken wit</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="warm"><img src="../assets/img/kleur-warm.webp" width="1400" height="1050" loading="lazy" alt="">Een warme tint</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="donker"><img src="../assets/img/kleur-donker.webp" width="1400" height="1050" loading="lazy" alt="">Donker en diep</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="weetniet"><img src="../assets/img/kleur-weetniet.webp" width="1400" height="1050" loading="lazy" alt="">Weet ik nog niet</button>
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
          <h3 class="display">Waar kan ik u bereiken?</h3>
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
          %(honing)s
          <button class="knop knop--vol" type="button" data-flow-verstuur>Offerte aanvragen</button>
          %(verzendfout)s
          <p class="formulier-noot">Vrijblijvend. Foto&#39;s stuurt u daarna het makkelijkst via
          WhatsApp; dat werkt sneller dan uploaden. Wat ik met uw gegevens doe, staat in de
          <a href="privacy.html">privacyverklaring</a>.</p>
        </div>

        <div class="flow-klaar" data-klaar data-aan="0" role="status">
          <b>Aanvraag verstuurd.</b>
          <p>Ik bel u om een moment af te spreken. Met de knop hieronder staat uw situatie
          ook in een WhatsApp-bericht, handig als u er meteen foto&#39;s bij wilt doen.</p>
          <div class="flow-samen" data-flow-samen></div>
          %(demozin)s
          <div class="knopgroep" style="margin-top:1.2rem">
            <a class="knop knop--vol" data-wa href="#">Bericht openen in WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""" % dict(honing=B.HONING % ("honing-flow", "honing-flow"), verzendfout=B.verzendfout(),
           demozin=('<p class="klein" style="color:var(--licht-3)">%s</p>' % B.demozin().strip())
                   if B.demozin() else "")
    h += B.snee()
    h += '  <section class="sectie sectie--vlak">\n    <div class="wrap rail">\n'
    h += B.railkop("Daarna", "Wat er gebeurt na uw aanvraag", "Geen verkooptraject",
                   "Ik kom kijken, u hoort wat er nodig is, en pas daarna komt er een prijs.")
    h += B.vragen(D.VRAGEN[:4], "na-aanvraag")
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Liever gewoon even bellen",
        "Kan ook. Dan hoort u meteen of het iets is waar ik u mee kan helpen.", variant=variant)
    return h + B.voet(variant)


# =====================================================================
# CONTACT
# =====================================================================
def contact(variant):
    h = B.kop(variant, "contact.html",
              "Contact | Aribouw, schilder in Westervoort",
              "Bel, app of mail Ahmad van Aribouw in Westervoort: %s of %s. Schilderwerk, "
              "behangen en houtreparaties in Westervoort, Arnhem, Nijmegen en omgeving."
              % (D.TEL_TOON, D.MAIL),
              "Hallo, ik heb een vraag.")

    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <h1 class="display op" style="max-width:14ch">Contact</h1>
      <p class="intro op" style="margin-top:1.1rem">Bellen of appen gaat het snelst: <a
      href="tel:%s" style="text-decoration:underline;text-underline-offset:3px">%s</a>. Een paar
      foto&#39;s van de ruimte helpen mij om meteen mee te denken, ook als u nog niets wilt
      afspreken.</p>
    </div>
  </section>
""" % (D.TEL_LINK, D.TEL_TOON)
    h += B.contactblok(
        "Stuur een bericht",
        "Ik reageer zo snel mogelijk. Heeft u haast, bel dan gerust.", variant=variant)

    h += B.snee(om=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Alle vragen en antwoorden", "%d stuks" % len(D.VRAGEN),
                   "Alles wat bij een eerste bezoek aan de keukentafel voorbijkomt, alvast op een "
                   "rij.")
    h += B.vragen(D.VRAGEN, "alle-vragen")
    h += "      </div>\n    </div>\n  </section>\n"
    return h + B.voet(variant)


# =====================================================================
# PRIVACYVERKLARING (beide varianten)
# =====================================================================
# Verplicht zodra de formulieren echt versturen: ze vragen naam, telefoon
# en plaats. Geschreven voor wat de site nu doet: geen cookies, geen
# analytics, fonts via Fontshare, films en foto's van de eigen server.
# Wat een keuze van Ahmad is en niet uit de wet volgt, staat gemarkeerd.
PRIVACY_DATUM = "15 september 2026"


def privacy(variant):
    h = B.kop(variant, "privacy.html",
              "Privacyverklaring | Aribouw",
              "Welke gegevens Aribouw verzamelt via de website, waarvoor, hoe lang ze bewaard "
              "worden en welke rechten u heeft.",
              "Hallo, ik heb een vraag over mijn gegevens.")
    h += """
  <section class="sectie">
    <div class="wrap">
      <div class="lopend">
        <h1 class="display">Privacyverklaring</h1>
        <p class="intro">Als u via deze website contact opneemt, krijg ik een paar gegevens van u.
        Hieronder staat welke dat zijn, wat ik ermee doe en wat u kunt vragen. Laatst bijgewerkt op
        %(datum)s.</p>

        <h2>Wie ik ben</h2>
        <dl>
          <dt>Bedrijf</dt><dd>Aribouw, %(eigenaar)s</dd>
          <dt>Adres</dt><dd>%(adres)s, %(postcode)s %(plaats)s</dd>
          <dt>KvK</dt><dd>%(kvk)s</dd>
          <dt>E-mail</dt><dd><a href="mailto:%(mail)s">%(mail)s</a></dd>
          <dt>Telefoon</dt><dd><a href="tel:%(tellink)s">%(tel)s</a></dd>
        </dl>
        <p>Aribouw is verantwoordelijk voor de verwerking van de gegevens in deze verklaring.</p>

        <h2>Welke gegevens</h2>
        <p>Via het contactformulier of de offerteaanvraag:</p>
        <ul>
          <li>uw naam, telefoonnummer en woonplaats</li>
          <li>waar de klus over gaat en wat u zelf over uw situatie schrijft</li>
          <li>de keuzes die u in de offerteaanvraag aanklikt, zoals het soort werk, de kleurrichting
          en wanneer het zou moeten gebeuren</li>
        </ul>
        <p>Neemt u contact op via WhatsApp, telefoon of e-mail, dan krijg ik de gegevens die u daar
        zelf meestuurt, zoals foto&#39;s van de ruimte.</p>

        <h2>Waarvoor</h2>
        <ul>
          <li>om u terug te bellen en een afspraak te maken om te komen kijken</li>
          <li>om een offerte te maken</li>
          <li>om de klus uit te voeren en af te rekenen, als u de opdracht geeft</li>
        </ul>
        <p>Dat mag omdat u zelf om contact of een offerte vraagt, en omdat het nodig is om een
        opdracht uit te voeren (artikel 6 lid 1 onder b AVG). Voor de administratie geldt daarnaast
        een wettelijke bewaarplicht. Ik gebruik uw gegevens niet voor nieuwsbrieven of reclame en
        verkoop ze niet.</p>

        <h2>Hoe lang</h2>
        <ul>
          <li>Een aanvraag die niet tot een opdracht leidt, verwijder ik binnen twaalf maanden.</li>
          <li>Gegevens van een opdracht, zoals de offerte en de factuur, bewaar ik zeven jaar. Dat is
          de wettelijke bewaarplicht voor de administratie.</li>
        </ul>

        <h2>Wie er nog meer bij kan</h2>
        <ul>
          <li><b>De formulierdienst.</b> Wat u in een formulier invult, gaat via een formulierdienst
          naar mijn e-mail. %(formulierdienst)s</li>
          <li><b>De hostingpartij</b> waar de website draait. %(hosting)s</li>
          <li><b>WhatsApp</b>, als u zelf kiest om via WhatsApp contact op te nemen. Dan gelden ook
          de voorwaarden van WhatsApp.</li>
          <li><b>Fontshare</b> levert de lettertypen van deze website. Uw browser haalt die op bij
          hun server, waarbij uw IP-adres wordt gezien.</li>
        </ul>
        <p>Verder deel ik uw gegevens alleen als de wet dat verplicht.</p>

        <h2>Cookies</h2>
        <p>Deze website plaatst geen cookies en gebruikt geen programma&#39;s die uw bezoek volgen
        of meten.</p>

        <h2>Beveiliging</h2>
        <p>De website werkt via een beveiligde verbinding (https). Aanvragen komen binnen in mijn
        e-mail, die met een wachtwoord is beveiligd.</p>

        <h2>Uw rechten</h2>
        <p>U mag vragen welke gegevens ik van u heb, ze laten aanpassen of laten verwijderen. U mag
        ook bezwaar maken of vragen om ze aan u over te dragen. Stuur daarvoor een mail naar
        <a href="mailto:%(mail)s">%(mail)s</a> of bel <a href="tel:%(tellink)s">%(tel)s</a>. U krijgt
        binnen vier weken antwoord.</p>
        <p>Bent u het niet eens met hoe ik met uw gegevens omga, dan kunt u een klacht indienen bij
        de <a href="https://autoriteitpersoonsgegevens.nl">Autoriteit Persoonsgegevens</a>.</p>
      </div>
    </div>
  </section>
""" % dict(datum=PRIVACY_DATUM, eigenaar=D.EIGENAAR, adres=D.ADRES, postcode=D.POSTCODE,
           plaats=D.PLAATS, kvk=D.KVK, mail=D.MAIL, tel=D.TEL_TOON, tellink=D.TEL_LINK,
           formulierdienst=B.markeer("[NOG AANVULLEN: naam van de formulierdienst]"),
           hosting=B.markeer("[NOG AANVULLEN: naam van de hostingpartij]"))
    return h + B.voet(variant)


# =====================================================================
# DIENSTPAGINA (alleen Aflak)
# =====================================================================
def dienstpagina(variant, dienst):
    slug, naam, kort, lang, beeld, punten = dienst
    andere = [d for d in D.DIENSTEN if d[0] != slug]
    vraagset = [D.VRAGEN[i] for i in D.DIENST_VRAGEN[slug]]

    h = B.kop(variant, "diensten.html",
              "%s in Westervoort, Arnhem en Nijmegen | Aribouw" % naam,
              "%s Werkgebied Westervoort, Duiven, Zevenaar, Arnhem, Nijmegen en omgeving." % kort,
              "Hallo, ik heb een vraag over %s." % naam.lower(),
              extra='<script type="application/ld+json">%s</script>' % D.vraag_jsonld(vraagset))

    werk = slug if slug in ("binnenschilderwerk", "buitenschilderwerk", "behang") else "meerdere dingen"
    h += B.filmhero("""      <p class="label op"><a href="diensten.html">Diensten</a></p>
      <h1 class="display op" style="max-width:16ch">%(naam)s</h1>
      <p class="intro op">%(kort)s</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="offerte.html?werk=%(werk)s">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%(wa)s">Foto sturen via WhatsApp</a>
      </div>
""" % dict(naam=naam, kort=kort, werk=werk,
           wa=D.wa_link("Hallo, ik stuur een foto voor %s." % naam.lower())),
        B.DIENST_FILM[slug], klasse="hero--dienst")

    h += """
  <section class="sectie sectie--zand">
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
""" % dict(kort=kort, lang=lang, beeld=beeld,
           punten="".join("<li>%s</li>" % p for p in punten))

    h += B.werkwijze(" sectie--vlak", beelden=True)
    h += B.snee()

    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Vragen over %s" % naam.lower(), "Vier stuks")
    h += B.vragen(vraagset, "vragen-" + slug)
    h += "      </div>\n    </div>\n  </section>\n"

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("En verder", "Vaak in dezelfde klus", "Drie andere diensten")
    h += B.kaarten(variant, lijst=andere)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Laat mij er even naar kijken",
        "Aan het langskomen en de offerte zitten geen kosten. U hoort wat er nodig is en wat kan "
        "blijven.", variant=variant)
    return h + B.voet(variant)


# =====================================================================
# PLAATSPAGINA (alleen Aflak)
# =====================================================================
def regiopagina(variant, plaats):
    anderen = [p for p in D.WERKGEBIED if p != plaats]
    h = B.kop(variant, "werkgebied.html",
              "Schilder in %s | Aribouw" % plaats,
              "Schilderwerk, behangen en houtreparaties in %s. Aribouw zit in Westervoort en "
              "werkt in de hele regio." % plaats,
              "Hallo, ik woon in %s en heb een vraag." % plaats)

    if plaats == D.PLAATS:
        waar = "Aribouw zit in %s zelf, aan de Mommenkamp." % plaats
    else:
        waar = "Aribouw zit in Westervoort, dus %s ligt in de buurt." % plaats
    h += B.filmhero("""      <p class="label op"><a href="werkgebied.html">Werkgebied</a></p>
      <h1 class="display op" style="max-width:16ch">Schilder in %(plaats)s</h1>
      <p class="intro op">%(waar)s %(score)s uit %(aantal)s reviews op Werkspot.</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="werk.html">Bekijk eerder werk</a>
      </div>
""" % dict(plaats=plaats, waar=waar, score=D.SCORE, aantal=D.AANTAL_REVIEWS),
        beeld="straat-liemers.webp", alt="Straat met bakstenen rijtjeshuizen en witte kozijnen",
        klasse="hero--kort")

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Wat ik doe", "In %s ook" % plaats, "Vier diensten",
                   "Dezelfde vier dingen als in de rest van het werkgebied.")
    h += B.kaarten(variant)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("In de buurt", "Ook hier", "Drie plaatsen")
    h += '        <div class="regio-lijst op" data-stagger>\n'
    for p in anderen:
        h += ('          <a href="regio-%s.html"><b>%s %s</b><span>Schilderwerk, behangen en '
              'houtwerk</span></a>\n' % (p.lower(), p, B.PIJL))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    h += B.contactblok(
        "Een afspraak in %s" % plaats,
        "Geef door wat er speelt, dan bel ik om een moment af te spreken.",
        variant=variant)
    return h + B.voet(variant)
