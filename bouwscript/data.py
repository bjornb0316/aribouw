# -*- coding: utf-8 -*-
"""Alle harde gegevens over Aribouw op een plek.

Wat er gecontroleerd is en waar het vandaan komt:

  - Op 15 september 2026 heeft Ahmad Nikzad zelf de gegevens aangeleverd:
    telefoon, e-mail, adres, KvK, btw, werkgebied, werkzaamheden, wat hij
    met de site wil en wat Aribouw volgens hem anders maakt. Dat is de bron
    voor alles hieronder, tenzij er iets anders bij staat.
  - Het Werkspot-profiel is op 8 september 2026 bekeken. Daar stond 5 uit 5
    op basis van 31 reviews, KvK-nummer 95128905 (klopt met wat Ahmad
    opgaf), en de vermeldingen "Geverifieerd door Werkspot" en "Biedt
    garantie".
  - De reviews hieronder staan letterlijk zo op Werkspot, met naam, plaats
    en datum erbij.

Wat Ahmad expliciet vroeg:
  - Duidelijk een schilder, geen algemeen bouwbedrijf.
  - Geen stucwerk of egaliseren. Dat staat er dus nergens als dienst, en
    het staat als vraag in de lijst zodat niemand erop rekent.
  - Ruimte voor eigen projectfoto's en voor-en-na. Die stuurt hij apart.
  - Teksten natuurlijk en persoonlijk, niet commercieel. Daarom in de
    ik-vorm: Ahmad is degene die komt kijken en het werk doet.

Wat er NIET in staat:
  - Het Instagram-account @aribouw uit de eerste briefing. Dat staat op naam
    van "walid aribou", heeft nul volgers en geen posts. Ahmad stuurt zijn
    eigen socialmediapagina's apart.
  - Prijzen. Niet gevraagd, niet getoond.
"""

NAAM = "Aribouw"
PERSOON = "Ahmad"
EIGENAAR = "Ahmad Nikzad"
PLAATS = "Westervoort"
ADRES = "Mommenkamp 27"
POSTCODE = "6932 HT"

TEL_TOON = "06 83 04 41 91"
TEL_LINK = "+31683044191"
WA = "31683044191"
MAIL = "aribouw10@gmail.com"

KVK = "95128905"
BTW = "NL005131384B93"
WERKSPOT = "https://www.werkspot.nl/profiel/aribouw"
FACEBOOK = "https://www.facebook.com/aribouw/?locale=nl_NL"
BJORN_WA = "31614664161"

# Hun eigen zin, van de Facebookpagina.
CLAIM = "Betrouwbaar vakwerk met oog voor detail"

# Op 8 september 2026 van het Werkspot-profiel gehaald.
SCORE = "5,0"
AANTAL_REVIEWS = "31"
SCORE_DATUM = "8 september 2026"

# Het werkgebied zoals Ahmad het opgaf, in zijn volgorde. De eerste vier
# krijgen in Aflak een eigen plaatspagina; meer bijna gelijke pagina's
# helpen niet en lezen als opvulling.
WERKGEBIED_ALLES = ["Westervoort", "Duiven", "Zevenaar", "Arnhem", "Doesburg", "Didam",
                    "Dieren", "Velp", "Huissen", "Elst", "Ede", "Nijmegen"]
WERKGEBIED = WERKGEBIED_ALLES[:4]
BUITEN_REGIO = "Voor grotere projecten ook buiten deze regio."

# Zijn eigen lijst van werkzaamheden, in vier groepen.
# (slug, naam, kort, lang, beeld, punten)
DIENSTEN = [
    ("binnenschilderwerk", "Binnenschilderwerk",
     "Wanden, plafonds, deuren, kozijnen en trappen. Strak afgeplakt en netjes achtergelaten.",
     "Binnen schilderen is voor een groot deel voorbereiding. Ontvetten, schuren, kleine gaatjes "
     "dichtzetten, afplakken. Dat ziet u later niet terug, maar juist daar zit het verschil tussen "
     "een muur die twee jaar mooi blijft en een die tien jaar mooi blijft. Meubels en vloeren dek "
     "ik af, en aan het eind staat alles weer zoals het stond.",
     "deur-na.webp",
     ["Wand- en plafondschilderwerk",
      "Deuren, kozijnen en ander houtwerk",
      "Trappen en trapgangen",
      "Alles afgedekt, aan het eind weer opgeruimd"]),
    ("buitenschilderwerk", "Buitenschilderwerk",
     "Kozijnen, deuren, boeidelen en ander buitenhout. Eerst het hout in orde, dan pas verf.",
     "Buitenwerk gaat kapot op de plekken waar water blijft staan: onderdorpels, hoeken van "
     "kozijnen, de onderkant van een deur. Verf daaroverheen zetten lost niets op. Aangetast hout "
     "haal ik eerst weg en herstel ik, daarna komen de grondverf en de lak. Anders staat u over "
     "twee jaar weer op dezelfde plek.",
     "kozijn-buiten.webp",
     ["Kozijnen, deuren en boeidelen",
      "Kleine houtreparaties voordat er verf op gaat",
      "Verf die past bij hout dat buiten staat",
      "Woningen, bedrijfspanden en praktijkruimtes"]),
    ("behang", "Behangen",
     "Behang, renovlies en glasvezel. Oud behang gaat er eerst af.",
     "Een goed behangresultaat begint bij de wand. Resten van oud behang of losse plekken zie je "
     "later terug als naden. Oud behang gaat eraf, kleine gaatjes zet ik dicht, en pas dan wordt "
     "er behangen. Bij renovlies en glasvezel komt er daarna nog verf overheen. Stucwerk en "
     "egaliseren doe ik niet; is dat nodig, dan hoort u dat vooraf.",
     "wand-detail.webp",
     ["Behang aanbrengen en verwijderen",
      "Renovlies en glasvezelbehang",
      "Renovlies en glasvezel afwerken met verf",
      "Advies over het soort behang bij uw wand"]),
    ("houtwerk", "Houtreparaties en onderhoud",
     "Houtrot herstellen, een deur die klemt, klein onderhoud. Het werk dat vaak bij schilderwerk "
     "hoort.",
     "Vaak is het niet een grote klus maar een rij kleine dingen: een stuk houtrot in een kozijn, "
     "een dorpel die zacht is geworden, een deur die klemt. Dat los uitbesteden kost meer tijd dan "
     "het werk zelf. Ik neem het mee in dezelfde planning als het schilderwerk.",
     "pui-voetzorg.webp",
     ["Houtrot uithalen en herstellen",
      "Kleine reparaties aan deuren, kozijnen en trappen",
      "Klein renovatie- en onderhoudswerk",
      "In een planning met het schilderwerk"]),
]

# Van eerste bericht tot oplevering. Geen doorlooptijden, want die zijn
# nog niet bevestigd.
STAPPEN = [
    ("01", "U stuurt foto's of belt",
     "Een paar foto's van de ruimte of het kozijn zeggen vaak al genoeg. Zet erbij wat u wilt en "
     "wanneer het ongeveer zou moeten."),
    ("02", "Ik kom langs en kijk",
     "Ik bekijk de ondergrond, de staat van het hout en hoeveel voorbereiding er nodig is. Daar zit "
     "vaak meer werk in dan mensen denken."),
    ("03", "Een offerte met de voorbereiding erin",
     "Op papier staat wat er gebeurt: schuren, gronden, lakken. Zo ziet u waar de uren in gaan "
     "zitten en waarom."),
    ("04", "Uitvoeren",
     "Afdekken, afplakken, schilderen. U hoort vooraf wanneer ik begin en of u thuis moet zijn."),
    ("05", "Opruimen en samen nalopen",
     "Tape eraf, spullen terug, afval mee. Aan het eind lopen we het werk samen na."),
]

# Zo staan ze op Werkspot, met naam, plaats en datum. Ingekort tot maximaal
# drie regels, zonder de betekenis te veranderen.
REVIEWS = [
    ("Verfwerk ziet er strak en netjes uit, heel tevreden. Komt afspraken na, erg vriendelijk. "
     "Rustig aan het werk, konden gewoon de deur uit.",
     "Susanne, Driel", "Buitenschilderwerk, 5 sep 2026"),
    ("Ahmad reageerde snel en dacht goed mee. Bleef wat langer om echt alles af te maken en kwam "
     "nog even terug voor de puntjes op de i.",
     "Joke Tesink, Apeldoorn", "Binnenschilderwerk, 7 aug 2026"),
    ("Ahmad is een vakman. Komt afspraken na en werkt zeer netjes.",
     "Cindy, Westervoort", "Buitenschilderwerk, 13 jun 2026"),
    ("De deuren en kozijnen zijn prachtig hersteld en voorzien van een mooi kleurtje. Aan te "
     "raden.",
     "Klant uit Huissen", "Buitenschilderwerk, 10 jul 2026"),
]

# De vragen die bij een eerste bezoek aan de keukentafel voorbijkomen.
VRAGEN = [
    ("Wat gaat het kosten?",
     "Dat hangt af van de oppervlakte, de staat van de ondergrond en hoeveel voorbereiding er "
     "nodig is. Twee kamers van dezelfde maat kunnen flink verschillen, puur door wat eronder zit. "
     "Daarom kom ik eerst kijken en noem ik pas daarna een prijs."),
    ("Wordt mijn woning netjes achtergelaten?",
     "Meubels dek ik af en vloeren bescherm ik. Aan het eind gaat de tape eraf, gaan spullen terug "
     "zoals ze stonden en neem ik het afval mee. Op Werkspot is dat het punt dat het vaakst "
     "terugkomt in de reviews."),
    ("Hoe lang duurt het?",
     "Dat verschilt te veel per klus om er hier een getal aan te hangen. Bij de offerte hoort een "
     "planning: wanneer ik begin, hoeveel dagen het ongeveer duurt en of u thuis moet zijn. "
     "[NOG AANVULLEN: gebruikelijke doorlooptijden]"),
    ("Welke verf of welk behang is geschikt?",
     "Dat hangt af van de ruimte en de ondergrond. In een badkamer of keuken is een andere verf "
     "nodig dan in een slaapkamer. Ik denk mee over materiaal en kleur, de keuze blijft aan u."),
    ("Moet ik zelf verf of behang regelen?",
     "Dat mag, en het hoeft niet. Koopt u zelf, dan hoort u vooraf hoeveel er nodig is en welk "
     "type past. Neem ik het mee, dan staat het als post in de offerte."),
    ("Wordt beschadigd hout eerst hersteld?",
     "Ja. Verf over rot hout is weggegooid geld. Aangetast hout haal ik weg en herstel ik voordat "
     "er gegrond wordt. Zit er te veel in, dan hoort u dat bij het kijken en niet pas als het werk "
     "al loopt."),
    ("Kunt u verschillende klussen combineren?",
     "Ja. Schilderwerk, behang en kleine houtreparaties in een planning scheelt tijd en gedoe met "
     "meerdere partijen."),
    ("Heb ik garantie op de afwerking?",
     "Op het Werkspot-profiel staat dat Aribouw garantie biedt. De precieze termijn en waar hij "
     "op geldt hoort bij de offerte. [NOG AANVULLEN: garantietermijnen]"),
    ("Hoe weet ik dat het goed komt?",
     "Op Werkspot staan %s reviews met een gemiddelde van %s. Die zijn openbaar, inclusief de "
     "reacties eronder. Vraag gerust naar een adres van een klus bij u in de buurt."
     % (AANTAL_REVIEWS, SCORE)),
    ("Doet u ook stucwerk of egaliseren?",
     "Nee. Kleine gaatjes en naden zet ik dicht voordat er geschilderd of behangen wordt, maar "
     "stucwerk en egaliseren doe ik niet. Is dat nodig, dan hoort u dat bij het kijken, zodat u "
     "het op tijd kunt regelen."),
    ("Werkt u ook voor aannemers en architecten?",
     "Ja. Ik werk voor particulieren en voor aannemers, architecten en andere professionals, met "
     "duidelijke afspraken over planning, materiaal en oplevering. Voor grotere projecten kan ik "
     "ook buiten de regio werken."),
]

# Welke vragen bij welke dienstpagina horen (indexen in VRAGEN).
DIENST_VRAGEN = {
    "binnenschilderwerk": [0, 1, 3, 4],
    "buitenschilderwerk": [5, 0, 7, 10],
    "behang": [9, 3, 4, 1],
    "houtwerk": [5, 6, 0, 10],
}

ONBEVESTIGD = [
    "Eigen projectfoto's en voor-en-nafoto's: Ahmad stuurt ze apart. De site heeft er ruimte "
    "voor; nu staan er negen beelden van Facebook en Werkspot.",
    "Het logo als vectorbestand. Er staat nu een eigen merkteken als tijdelijke oplossing.",
    "Garantietermijnen en gebruikelijke doorlooptijden: zichtbaar gemarkeerd in de vragenlijst.",
    "Certificaten en extra reviews: stuurt Ahmad apart.",
    "Socialmediapagina's: stuurt Ahmad apart. Het Instagram-account uit de eerste briefing is "
    "niet van dit bedrijf.",
    "De score van %s uit %s reviews is op %s van Werkspot gehaald. Dat getal loopt op, dus voor "
    "livegang even opnieuw kijken." % (SCORE, AANTAL_REVIEWS, SCORE_DATUM),
    "Formulieren hebben nog geen ontvanger. De WhatsApp-knoppen werken wel, met het echte nummer.",
]

JSONLD = """{
  "@context": "https://schema.org",
  "@type": "HousePainter",
  "name": "Aribouw",
  "founder": {"@type": "Person", "name": "%s"},
  "description": "Schildersbedrijf voor binnen- en buitenschilderwerk, behangen en kleine houtreparaties in Westervoort, Arnhem, Nijmegen en omgeving.",
  "telephone": "%s",
  "email": "%s",
  "vatID": "%s",
  "address": {"@type": "PostalAddress", "streetAddress": "%s", "postalCode": "%s",
              "addressLocality": "%s", "addressCountry": "NL"},
  "areaServed": [%s],
  "sameAs": ["https://www.werkspot.nl/profiel/aribouw"]
}""" % (EIGENAAR, TEL_LINK, MAIL, BTW, ADRES, POSTCODE, PLAATS,
        ", ".join('"%s"' % p for p in WERKGEBIED_ALLES))


def wa_link(bericht):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (WA, quote(bericht))


def vraag_jsonld(vragen):
    import json, re
    items = [{"@type": "Question", "name": v,
              "acceptedAnswer": {"@type": "Answer",
                                 "text": re.sub(r"\[NOG AANVULLEN:[^\]]*\]", "", a).strip()}}
             for v, a in vragen]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                       "mainEntity": items}, ensure_ascii=False, indent=2)
