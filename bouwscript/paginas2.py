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
          <img src="assets/img/pui-detail.webp" width="1200" height="900" fetchpriority="high"
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
            <button class="keuze keuze--beeld" type="button" data-waarde="licht"><img src="assets/img/kleur-licht.webp" width="1400" height="1050" loading="lazy" alt="">Wit of gebroken wit</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="warm"><img src="assets/img/kleur-warm.webp" width="1400" height="1050" loading="lazy" alt="">Een warme tint</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="donker"><img src="assets/img/kleur-donker.webp" width="1400" height="1050" loading="lazy" alt="">Donker en diep</button>
            <button class="keuze keuze--beeld" type="button" data-waarde="weetniet"><img src="assets/img/kleur-weetniet.webp" width="1400" height="1050" loading="lazy" alt="">Weet ik nog niet</button>
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
           # Categorieën van ontvangers volstaan voor de AVG. Namen kunnen erbij
           # zodra hosting en formulierdienst vastliggen (zie data.py).
           formulierdienst="", hosting="")
    return h + B.voet(variant)


# =====================================================================
# DIENSTPAGINA (alleen Aflak)
# =====================================================================
# =====================================================================
# BEHEER: PROJECT TOEVOEGEN (alleen Aflak, niet in menu of sitemap)
# =====================================================================
# Voorbeeld voor de correctieronde van het beheerscherm waarmee Ahmad straks
# zelf projecten op de site zet. Het formulier, de foto's kiezen, de
# voorbeeldweergave en de knop Publiceren werken in de browser, maar er wordt
# niets opgeslagen of verstuurd. De echte versie (inloggen met pincode,
# opslag, projectpagina's) komt na goedkeuring.
def beheer(variant):
    h = B.kop(variant, "", "Project toevoegen | Beheer Aribouw",
              "Beheer: een project op de website van Aribouw zetten.",
              "Hallo Bjorn, ik heb een vraag over het beheerscherm.",
              extra='<meta name="robots" content="noindex,nofollow">' if D.LIVE else "")
    diensten = "\n".join('              <option>%s</option>' % d[1] for d in D.DIENSTEN + D.SUBDIENSTEN)
    plaatsen = "\n".join('              <option>%s</option>' % p for p in D.WERKGEBIED_ALLES)
    h += """
  <section class="sectie beheer">
    <div class="wrap" style="max-width:48rem">
      <p class="beheer-voorbeeld op"><b>Voorbeeld voor de correctieronde.</b> Zo zet je straks zelf
      een project op de site, nadat je bent ingelogd met je pincode. In deze versie wordt nog niets
      opgeslagen of gepubliceerd; probeer het gerust uit.</p>

      <h1 class="display op">Project toevoegen</h1>
      <p class="intro op" style="margin-top:.9rem">Na een klus, vijf minuten. Het project komt op de
      werkpagina en op de pagina&#39;s van de dienst en de plaats. Dat is wat nieuwe klanten
      overtuigt, en waar Google op zoekt.</p>

      <div class="signalen op">
        <h3 class="display">Zo maak je de foto&#39;s</h3>
        <ul>
          <li>Voor en na vanaf dezelfde plek en in dezelfde hoek</li>
          <li>Bij daglicht, liggend, zonder flits</li>
          <li>Ook een foto van een detail: een hoek, een naad, een dorpel</li>
          <li>Geen mensen, kentekens of huisnummers in beeld</li>
          <li>Eerst de klant vragen of de foto&#39;s online mogen</li>
          <li>Na afloop de klant om een Google-review vragen</li>
        </ul>
      </div>

      <form class="flow op" style="margin-top:2rem" data-beheer novalidate>
        <div class="velden-2">
          <div class="veld">
            <label for="bh-werk">Soort werk</label>
            <select id="bh-werk" name="werk" required>
              <option value="" disabled selected>Maak een keuze</option>
%(diensten)s
            </select>
            <span class="fout">Kies het soort werk.</span>
          </div>
          <div class="veld">
            <label for="bh-plaats">Plaats</label>
            <select id="bh-plaats" name="plaats" required>
              <option value="" disabled selected>Maak een keuze</option>
%(plaatsen)s
              <option>Andere plaats</option>
            </select>
            <span class="fout">Kies de plaats.</span>
          </div>
        </div>
        <div class="velden-2">
          <div class="veld">
            <label for="bh-onderdelen">Wat is er gedaan</label>
            <input id="bh-onderdelen" name="onderdelen" type="text" required
                   placeholder="Bijvoorbeeld: vier buitenkozijnen en de voordeur">
            <span class="fout">Vul in wat er is gedaan.</span>
          </div>
          <div class="veld">
            <label for="bh-wanneer">Wanneer</label>
            <input id="bh-wanneer" name="wanneer" type="month">
            <span class="hulp">Maand is genoeg.</span>
          </div>
        </div>
        <div class="veld">
          <label for="bh-situatie">Hoe was het ervoor</label>
          <textarea id="bh-situatie" name="situatie" rows="3" required
                    placeholder="Bijvoorbeeld: lak bladderde op de onderdorpels, houtrot in twee hoeken"></textarea>
          <span class="fout">Beschrijf hoe het ervoor was.</span>
        </div>
        <div class="veld">
          <label for="bh-aanpak">Wat heb je gedaan</label>
          <textarea id="bh-aanpak" name="aanpak" rows="3" required
                    placeholder="Bijvoorbeeld: rot hout eruit, gevuld, geschuurd, gegrond en twee keer gelakt"></textarea>
          <span class="fout">Beschrijf de aanpak.</span>
        </div>
        <div class="velden-2">
          <div class="veld">
            <label for="bh-voor">Foto voor</label>
            <input id="bh-voor" name="voor" type="file" accept="image/*" required>
            <span class="fout">Kies een foto van voor.</span>
          </div>
          <div class="veld">
            <label for="bh-na">Foto na</label>
            <input id="bh-na" name="na" type="file" accept="image/*" required>
            <span class="fout">Kies een foto van na.</span>
          </div>
        </div>
        <div class="veld">
          <label for="bh-extra">Extra foto&#39;s</label>
          <input id="bh-extra" name="extra" type="file" accept="image/*" multiple>
          <span class="hulp">Niet verplicht. Bijvoorbeeld een detail.</span>
        </div>
        <label class="vink"><input type="checkbox" name="akkoord" data-akkoord> De klant vindt het goed
        dat deze foto&#39;s online komen</label>
        <p class="vink-fout" data-akkoord-fout>Vink dit aan voordat je publiceert.</p>
        <label class="vink"><input type="checkbox" name="plaatsnaam" checked> Plaatsnaam tonen</label>

        <div class="knopgroep" style="margin-top:1.4rem">
          <button class="knop knop--lijn" type="button" data-beheer-voorbeeld>Voorbeeld bekijken</button>
          <button class="knop knop--vol" type="submit">Publiceren</button>
        </div>
      </form>

      <div class="beheer-kaart" data-beheer-kaart hidden>
        <p class="label">Zo komt het op de site</p>
        <h2 class="display" data-bk-titel></h2>
        <div class="beheer-fotos">
          <figure><img data-bk-voor alt=""><figcaption>Voor</figcaption></figure>
          <figure><img data-bk-na alt=""><figcaption>Na</figcaption></figure>
        </div>
        <h3>Situatie</h3><p data-bk-situatie></p>
        <h3>Aanpak</h3><p data-bk-aanpak></p>
        <p class="klein" data-bk-links></p>
      </div>

      <div class="gelukt" data-beheer-gelukt role="status">
        <b>Klaar, in het voorbeeld.</b>
        <p>In de echte versie staat het project nu op de site: op de werkpagina, als eigen pagina, en
        gelinkt vanaf de dienst en de plaats. In deze voorbeeldversie is er niets opgeslagen.</p>
      </div>
    </div>
  </section>
""" % dict(diensten=diensten, plaatsen=plaatsen)
    return h + B.voet(variant)


def dienstpagina(variant, dienst):
    slug, naam, kort, lang, beeld, punten = dienst
    andere = [d for d in D.DIENSTEN if d[0] != slug]
    vraagset = [D.VRAGEN[i] for i in D.DIENST_VRAGEN[slug]]
    inhoud = D.DIENST_INHOUD[slug]

    h = B.kop(variant, "diensten.html",
              "%s in Westervoort, Arnhem en omgeving | Aribouw" % naam,
              "%s Waar u op let, welk materiaal en waar de prijs van afhangt. Aribouw, schilder in "
              "Westervoort." % kort,
              "Hallo, ik heb een vraag over %s." % naam.lower(),
              extra=('<script type="application/ld+json">%s</script>\n'
                     '<script type="application/ld+json">%s</script>'
                     % (D.dienst_jsonld(variant, dienst), D.vraag_jsonld(vraagset))))

    # Welke eerste vraag in de offerteflow al beantwoord is. Kozijnen kunnen
    # binnen en buiten zijn, dus daar vraagt de flow het gewoon.
    werk = {"binnenschilderwerk": "binnenschilderwerk", "buitenschilderwerk": "buitenschilderwerk",
            "behang": "behang", "houtwerk": "meerdere dingen",
            "wanden-plafonds": "binnenschilderwerk"}.get(slug, "")
    offerte = "offerte.html" + ("?werk=%s" % werk if werk else "")
    wa = D.wa_link("Hallo, ik stuur een foto voor %s." % naam.lower())
    tekst = """      <p class="label op"><a href="diensten.html">Diensten</a></p>
      <h1 class="display op" style="max-width:18ch">%(naam)s in Westervoort en omgeving</h1>
      <p class="intro op">%(kort)s</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="%(offerte)s">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%(wa)s">Foto sturen via WhatsApp</a>
      </div>
""" % dict(naam=naam, kort=kort, offerte=offerte, wa=wa)
    if slug in B.DIENST_FILM:
        h += B.filmhero(tekst, B.DIENST_FILM[slug], klasse="hero--dienst")
    else:
        heldbeeld, heldalt = B.DIENST_BEELD[slug]
        h += B.filmhero(tekst, beeld=heldbeeld, alt=heldalt, klasse="hero--dienst")

    zie_ook = ""
    if inhoud.get("zie_ook"):
        zie_ook = ('          <p class="zie-ook">Zie ook: %s</p>\n'
                   % " ".join('<a href="%s">%s %s</a>' % (href, label, B.PIJL)
                              for label, href in inhoud["zie_ook"]))

    # Waar de uren in gaan zitten, met een eigen foto.
    h += """
  <section class="sectie sectie--zand">
    <div class="wrap">
      <div class="blok op" style="border:0;padding-top:0">
        <div class="blok-beeld">
          <img src="assets/img/%(beeld)s" width="1000" height="750" loading="lazy"
               alt="%(kort)s">
        </div>
        <div>
          <h2 class="display">Waar de uren in gaan zitten</h2>
          <p class="intro" style="margin-top:.9rem">%(lang)s</p>
          <ul class="punten">%(punten)s</ul>
%(zie_ook)s        </div>
      </div>
    </div>
  </section>
""" % dict(kort=kort, lang=lang, beeld=beeld, zie_ook=zie_ook,
           punten="".join("<li>%s</li>" % p for p in punten))

    # Bij kozijnen en deuren: de echte voor-en-na van de binnendeur.
    if inhoud.get("voorna"):
        import paginas as P1
        h += '  <section class="sectie">\n    <div class="wrap rail">\n'
        h += B.railkop("Voor en na", "Een binnendeur, voor en na", "Eigen werk",
                       "Van houtlook naar strak gebroken wit. Sleep de lijn om het verschil te zien.")
        h += P1.vergelijk("55")
        h += "      </div>\n    </div>\n  </section>\n"

    # Wanneer, waar u op let, welk materiaal: de vragen voor de aanvraag.
    h += B.snee(om=True, zand=not inhoud.get("voorna"))
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    wanneer_titel = {"kozijnen-deuren": "Wanneer is het tijd voor nieuwe lak?",
                     "wanden-plafonds": "Wanneer is het tijd voor een nieuwe laag?"}.get(
                         slug, "Wanneer is het tijd voor %s?" % naam.lower())
    h += B.railkop("Wanneer", wanneer_titel, "Voor de aanvraag")
    h += '        <div class="kennis op" data-stagger>\n'
    for titel, tekst in inhoud["wanneer"]:
        h += '          <div><h3>%s</h3><p>%s</p></div>\n' % (titel, tekst)
    h += "        </div>\n"
    h += ('        <div class="signalen op">\n          <h3 class="display">Waar u zelf op kunt '
          'letten</h3>\n          <ul>%s</ul>\n        </div>\n'
          % "".join("<li>%s</li>" % s for s in inhoud["signalen"]))
    h += B.ctaregel("Herkent u iets hiervan? Stuur een foto, dan zeg ik wat er nodig is.",
                    [("Foto sturen via WhatsApp", wa, "vol")])
    h += "      </div>\n    </div>\n  </section>\n"

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Materiaal", "Welk materiaal, en waarom", "Advies bij het kijken",
                   "Welke verf of welk behang het wordt, hangt af van de ruimte en de ondergrond. "
                   "Dit zijn de keuzes die meestal voorbijkomen.")
    h += '        <div class="materiaal op" data-stagger>\n'
    for titel, tekst in inhoud["materiaal"]:
        h += '          <div><h3>%s</h3><p>%s</p></div>\n' % (titel, tekst)
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"

    # Geen prijzen, wel eerlijk waar de prijs van afhangt.
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("Kosten", "Waar de prijs van afhangt", "Geen prijslijst",
                   "Een prijs noemen zonder te kijken zou gokken zijn. Dit zijn de dingen die het "
                   "verschil maken.")
    h += ('        <ol class="kosten op">%s</ol>\n'
          % "".join("<li>%s</li>" % k for k in inhoud["kosten"]))
    h += B.ctaregel("Benieuwd wat dit bij uw woning kost? Ik kom vrijblijvend kijken.",
                    [("Offerte aanvragen", offerte, "vol")])
    h += "      </div>\n    </div>\n  </section>\n"

    # Een onderdeel dat (nog) geen eigen pagina heeft, zoals trappen.
    extra = inhoud.get("extra")
    if extra:
        h += '  <section class="sectie sectie--zand" id="%s">\n    <div class="wrap rail">\n' % extra["id"]
        h += B.railkop(extra["label"], extra["titel"], "Onderdeel van %s" % naam.lower(),
                       extra["tekst"])
        h += ('        <ul class="punten punten--twee op">%s</ul>\n'
              % "".join("<li>%s</li>" % p for p in extra["punten"]))
        h += B.ctaregel("Een trap laten schilderen? Stuur een foto van de treden en de leuning.",
                        [("Foto sturen via WhatsApp",
                          D.wa_link("Hallo, ik wil mijn trap laten schilderen. Ik stuur een foto."),
                          "vol")])
        h += "      </div>\n    </div>\n  </section>\n"

    h += B.werkwijze(" sectie--vlak", beelden=True)
    h += B.snee()

    if inhoud["reviews"]:
        h += '  <section class="sectie">\n    <div class="wrap rail">\n'
        h += B.railkop("Reviews", "Wat klanten op Werkspot schrijven",
                       "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                       "Letterlijk overgenomen, met het soort werk en de plaats erbij.")
        h += B.reviews(indexen=inhoud["reviews"])
        h += "      </div>\n    </div>\n  </section>\n"

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Vragen", "Vragen over %s" % naam.lower(), "%d stuks" % len(vraagset))
    h += B.vragen(vraagset, "vragen-" + slug)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("En verder", "Vaak in dezelfde klus", "%d andere diensten" % len(andere))
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
    regio = D.REGIO[plaats]
    h = B.kop(variant, "werkgebied.html",
              "Schilder in %s | Aribouw" % plaats,
              "Schilder in %s: binnen- en buitenschilderwerk, behangen en houtreparaties door "
              "Aribouw uit Westervoort. %s uit %s reviews op Werkspot."
              % (plaats, D.SCORE, D.AANTAL_REVIEWS),
              "Hallo, ik woon in %s en heb een vraag." % plaats)

    h += B.filmhero("""      <p class="label op"><a href="werkgebied.html">Werkgebied</a></p>
      <h1 class="display op" style="max-width:16ch">Schilder in %(plaats)s</h1>
      <p class="intro op">%(intro)s</p>
      <div class="knopgroep op">
        <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
        <a class="knop knop--lijn" href="%(wa)s">Stuur foto&#39;s via WhatsApp</a>
      </div>
""" % dict(plaats=plaats, intro=regio["intro"],
           wa=D.wa_link("Hallo, ik woon in %s en stuur wat foto's." % plaats)),
        beeld="straat-liemers.webp", alt="Straat met bakstenen rijtjeshuizen en witte kozijnen",
        klasse="hero--kort")

    # Lokaal bewijs, alleen als het er echt is.
    if regio["projecten"] or regio["reviews"]:
        h += '  <section class="sectie">\n    <div class="wrap rail">\n'
        h += B.railkop("Uit %s" % plaats, "Werk en reviews uit %s" % plaats, "Eigen werk",
                       regio.get("project_tekst", ""))
        if regio["projecten"]:
            werk = [w for w in B.WERK if w[0] in regio["projecten"]]
            h += '        <div class="werk werk--lokaal op" data-stagger>\n'
            for beeld, titel, onder in werk:
                h += ('          <figure><img src="assets/img/%s" width="1000" height="750" '
                      'loading="lazy" alt="%s in %s"><figcaption><h3>%s</h3><p>%s</p></figcaption>'
                      '</figure>\n' % (beeld, titel, plaats, titel, onder))
            h += "        </div>\n"
        if regio["reviews"]:
            h += B.reviews(indexen=regio["reviews"])
        h += "      </div>\n    </div>\n  </section>\n"
        h += B.snee(zand=False)
    else:
        h += '  <section class="sectie">\n    <div class="wrap rail">\n'
        h += B.railkop("Reviews", "Reviews uit de regio", "%s uit %s" % (D.SCORE, D.AANTAL_REVIEWS),
                       "Uit %s staat er nog geen review op Werkspot. Dit zijn reviews uit de "
                       "regio, met de plaats erbij." % plaats)
        h += B.reviews(indexen=[2, 3])
        h += "      </div>\n    </div>\n  </section>\n"
        h += B.snee(zand=False)

    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("Wat ik doe", "Diensten in %s" % plaats, "Vier diensten")
    h += B.kaarten(variant)
    h += "      </div>\n    </div>\n  </section>\n"

    h += B.snee(om=True, zand=True)
    h += '  <section class="sectie">\n    <div class="wrap rail">\n'
    h += B.railkop("In de buurt", "Ook in deze plaatsen", "%d plaatsen" % len(anderen),
                   "Het hele werkgebied staat op de <a href=\"werkgebied.html\">werkgebiedpagina</a>.")
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


# =====================================================================
# PROJECTSJABLOON (server vult dit met een project uit de database)
# =====================================================================
def projectsjabloon(variant):
    h = B.kop(variant, "werk.html", "Project | Aribouw",
              "Een uitgevoerd project van Aribouw.",
              "Hallo, ik heb een vraag over dit project.",
              extra='<meta name="robots" content="noindex">')
    h += """
  <section class="sectie" style="padding-bottom:clamp(2rem,4vw,3rem)">
    <div class="wrap">
      <p class="label op"><a href="werk.html">Werk</a></p>
      <h1 class="display op" style="max-width:20ch" data-p="titel">Project</h1>
      <p class="intro op" data-p="samenvatting">Uitgevoerd werk van Aribouw.</p>
    </div>
  </section>

  <section class="sectie" style="padding-top:0">
    <div class="wrap rail">
      <div class="rail-kop">
        <span class="rail-naam">Voor en na</span>
        <p data-p="meta">Aribouw</p>
      </div>
      <div class="rail-in">
        <div class="vergelijk op" data-schuif style="--x:55%">
          <img data-p-src="voor" src="assets/img/deur-voor-breed.webp" width="1100" height="825"
               alt="Voor het werk">
          <img class="schuif-na" data-p-src="na" src="assets/img/deur-na-breed.webp" width="1100"
               height="825" alt="Na het werk">
          <span class="schuif-merk schuif-merk--voor">Voor</span>
          <span class="schuif-merk schuif-merk--na">Na</span>
          <div class="schuif-greep" role="slider" tabindex="0" aria-valuemin="0" aria-valuemax="100"
               aria-valuenow="55" aria-label="Schuif om voor en na te vergelijken"></div>
        </div>
        <div class="projecttekst op">
          <h2 class="display">Hoe het ervoor was</h2>
          <p data-p="situatie">Situatie.</p>
          <h2 class="display">Wat ik heb gedaan</h2>
          <p data-p="aanpak">Aanpak.</p>
          <p data-p="resultaat" class="klein"></p>
        </div>
        <div class="projectfotos op" data-p-extra hidden></div>
      </div>
    </div>
  </section>
"""
    h += B.snee(om=True)
    h += '  <section class="sectie sectie--zand">\n    <div class="wrap rail">\n'
    h += B.railkop("En verder", "Meer werk en dezelfde aanpak", "Alle projecten",
                   'Alle foto&#39;s staan op de <a href="werk.html">werkpagina</a>.')
    h += '        <p class="zie-ook" data-p-links></p>\n'
    h += "      </div>\n    </div>\n  </section>\n"
    h += B.contactblok(
        "Zoiets voor uw woning",
        "Stuur een foto van de ruimte of het kozijn, dan hoort u wat er nodig is.", variant=variant)
    return h + B.voet(variant)

