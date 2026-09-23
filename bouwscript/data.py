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

import os

# ---------------------------------------------------------------------
# Livegang. Drie schakelaars, alle drie nog in demostand.
# ---------------------------------------------------------------------
# LIVE = True: voorbeeldbalk bovenin, voetregel van Bjorn, noindex op elke
# pagina en een robots.txt die alles blokkeert. Op True gaat dat allemaal weg.
LIVE = True

# Het adres waar elke variant staat, zonder slash aan het eind. Voor
# canonical, og:url, og:image en de sitemap. Bij livegang: het echte domein
# bij "aflak".
SITE_URL = {
    "aflak": "https://aribouw.nl",
}

# Waar formulieren naartoe gaan. Leeg: demostand, controle en bevestiging
# werken maar er gaat niets de deur uit. Voor livegang bijvoorbeeld
# "https://formsubmit.co/ajax/aribouw10@gmail.com": geen account nodig, de
# eerste aanvraag stuurt Ahmad een activatiemail die hij een keer bevestigt.
# Elk adres dat JSON per POST aanneemt en 2xx teruggeeft werkt. Voor een
# test zonder de code aan te passen: omgevingsvariabele ARIBOUW_FORMULIER.
FORMULIER_ACTIE = os.environ.get("ARIBOUW_FORMULIER", "/api/aanvraag")

NAAM = "Aribouw"
PERSOON = "Ahmad"
EIGENAAR = "Ahmad Nikzad"
PLAATS = "Westervoort"
ADRES = "Mommenkamp 27"
POSTCODE = "6932 HT"

TEL_TOON = "06 83 04 41 91"
TEL_LINK = "+31683044191"
WA = "31683044191"
MAIL = "info@aribouw.nl"

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
# Huissen erbij omdat daar een echte review vandaan komt.
WERKGEBIED = ["Westervoort", "Duiven", "Zevenaar", "Arnhem", "Huissen"]
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

# Wat een dienstpagina meer vertelt dan de kaart: de vragen die iemand heeft
# voordat hij een aanvraag doet. Algemene vakkennis, geen verzonnen feiten
# over Aribouw, geen prijzen en geen termijnen.
# reviews: indexen in REVIEWS die echt over dit soort werk gaan.
DIENST_INHOUD = {
    "binnenschilderwerk": {
        "wanneer": [
            ("Muren en plafonds", "Bij vlekken, verkleuring of beschadigingen die met schoonmaken "
             "niet meer weggaan. Of gewoon omdat er een nieuwe kleur moet, bijvoorbeeld bij een "
             "verhuizing."),
            ("Deuren, kozijnen en trappen", "Als de lak dof wordt, afbladdert of versleten is op de "
             "plekken waar veel wordt vastgepakt of gelopen."),
            ("Keuken en badkamer", "Bij loslatende verf of plekjes door vocht. Daar is een verf "
             "nodig die daar tegen kan."),
        ],
        "signalen": ["Verf die loslaat of bladdert", "Gele verkleuring van oude lak op deuren en "
                     "kozijnen", "Doorschijnende of vlekkerige plekken na een eerdere laag",
                     "Vocht- of rookvlekken die door de verf heen blijven komen",
                     "Kleine gaatjes en naden van pluggen of oude schilderijhaken"],
        "materiaal": [
            ("Muurverf", "Voor wanden en plafonds. Mat verbergt oneffenheden het best, een "
             "zijdeglans is makkelijker af te nemen."),
            ("Lak voor houtwerk", "Watergedragen lak vergeelt minder, terpentinegedragen lak vloeit "
             "vaak mooier uit. Welke past, hangt af van de ondergrond en de ruimte."),
            ("Vochtbestendige verf", "Voor keuken en badkamer, waar gewone muurverf het niet lang "
             "volhoudt."),
        ],
        "kosten": ["De oppervlakte van muren en plafonds",
                   "Hoeveel houtwerk erbij komt: deuren, kozijnen, plinten, een trap",
                   "De staat van de ondergrond en hoeveel voorbereiding nodig is",
                   "Het aantal lagen, bijvoorbeeld bij een lichte kleur over een donkere",
                   "Of de ruimte leeg is of eerst alles afgedekt moet worden"],
        "reviews": [1, 0],
        "zie_ook": [("Wanden en plafonds schilderen", "dienst-wanden-plafonds.html"),
                    ("Kozijnen en deuren schilderen", "dienst-kozijnen-deuren.html")],
        # Een trap heeft (nog) geen foto of project, dus een blok hier in
        # plaats van een eigen pagina.
        "extra": {
            "id": "trappen", "label": "Trappen", "titel": "Trappen schilderen",
            "tekst": "Een trap krijgt het zwaarst te verduren van al het houtwerk in huis. Treden, "
                     "stootborden, leuning en spijlen worden grondig geschuurd en krijgen een lak "
                     "die tegen lopen kan. Omdat een trap tijdens het werk niet of maar half te "
                     "gebruiken is, spreken we vooraf af hoe dat gaat.",
            "punten": ["Treden en stootborden", "Leuning, spijlen en trapboom",
                       "Een slijtvaste lak die tegen lopen kan",
                       "Vooraf afspraken over wanneer de trap te gebruiken is"],
        },
    },
    "buitenschilderwerk": {
        "wanneer": [
            ("Het hangt af van de kant van het huis", "De zon- en regenkant heeft het veel zwaarder "
             "dan de kant in de schaduw. Kijk daarom liever naar de signalen hieronder dan naar het "
             "aantal jaren."),
            ("Liever iets te vroeg", "Zolang de verf nog heel is, is opnieuw schilderen vooral "
             "schuren en lakken. Zit er eenmaal water in het hout, dan komt er herstel bij."),
            ("Het seizoen", "Buitenwerk gaat het best bij droog weer en niet te lage temperaturen. "
             "Het voorjaar en de zomer raken daardoor snel vol."),
        ],
        "signalen": ["Verf die bladdert of scheurt, vooral op onderdorpels en in de hoeken",
                     "Hout dat zacht aanvoelt als u er met een schroevendraaier op drukt",
                     "Donkere verkleuring of schimmel in de hoeken van een kozijn",
                     "Open naden tussen het kozijn en het glas of de muur",
                     "Kaal of grijs geworden hout waar de verf weg is"],
        "materiaal": [
            ("Grondverf", "Op kaal of hersteld hout. Zonder grondlaag hecht de lak niet goed en "
             "laat hij sneller los."),
            ("Buitenlak", "Een lak die tegen zon, regen en temperatuurverschil kan, in de glansgraad "
             "die bij het huis past."),
            ("Houtrotvuller of nieuw hout", "Voor aangetaste plekken, voordat er verf op gaat. "
             "Verf over rot hout is weggegooid geld."),
        ],
        "kosten": ["Het aantal kozijnen, deuren en boeidelen",
                   "Hoeveel houtrot er hersteld moet worden",
                   "Of de oude laklaag alleen geschuurd of helemaal verwijderd moet worden",
                   "Hoe goed hoge delen bereikbaar zijn",
                   "Het aantal lagen"],
        "reviews": [0, 2, 3],
        "zie_ook": [("Kozijnen en deuren schilderen", "dienst-kozijnen-deuren.html")],
    },
    "behang": {
        "wanneer": [
            ("Behang", "Voor een patroon of structuur die u met verf niet krijgt."),
            ("Renovlies", "Een glad vlies dat na het behangen wordt geschilderd. Het verbergt "
             "kleine oneffenheden en haarscheurtjes en maakt de wand steviger."),
            ("Glasvezelbehang", "Sterker dan renovlies, met een zichtbare structuur. Handig op "
             "plekken waar vaak iets tegen de muur komt, zoals een gang of trapgat."),
        ],
        "signalen": ["Naden die loslaten of openstaan", "Bobbels of luchtbellen in het behang",
                     "Verkleuring of vlekken die niet meer weggaan",
                     "Scheurtjes waar de wand eronder doorheen komt",
                     "Oud behang waar u liever een geschilderde wand voor terug wilt"],
        "materiaal": [
            ("De juiste lijm", "Vliesbehang, papierbehang en glasvezel vragen elk een andere lijm "
             "en een andere manier van aanbrengen."),
            ("Voorstrijk", "Op een wand die veel vocht opzuigt, zodat het behang goed hecht."),
            ("Muurverf erover", "Renovlies en glasvezel krijgen na het behangen meestal twee lagen "
             "verf."),
        ],
        "kosten": ["Het aantal vierkante meters wand",
                   "Of oud behang eerst verwijderd moet worden",
                   "De staat van de wand eronder",
                   "Het soort behang, en bij patroonbehang het laten doorlopen van het patroon",
                   "Of renovlies of glasvezel daarna nog geschilderd wordt"],
        "reviews": [1, 0],
    },
    "houtwerk": {
        "wanneer": [
            ("Zodra hout zacht wordt", "Hoe eerder houtrot wordt aangepakt, hoe kleiner de reparatie "
             "blijft. Wachten maakt het bijna altijd duurder."),
            ("Als verf steeds op dezelfde plek loslaat", "Dat is vaak een teken dat er vocht in het "
             "hout zit. Opnieuw schilderen zonder te herstellen helpt dan niet lang."),
            ("Samen met het schilderwerk", "Kleine reparaties vallen het minst op als ze in dezelfde "
             "klus worden meegenomen en er meteen verf overheen gaat."),
        ],
        "signalen": ["Een onderdorpel die zacht aanvoelt of waar de verf steeds bladdert",
                     "Houtrot aan de onderkant van een deur of kozijnstijl",
                     "Donker of vochtig hout rond hoeken en naden",
                     "Een deur die klemt of niet meer goed sluit",
                     "Scheuren in het hout waar water in kan lopen"],
        "materiaal": [
            ("Houtrotvuller", "Voor kleine plekken: het rotte hout eruit, vullen, schuren en "
             "schilderen."),
            ("Een nieuw stuk hout", "Als de schade te groot is voor vuller, wordt er een stuk nieuw "
             "hout ingezet."),
            ("Grondverf en lak", "Zodat de reparatie beschermd is en niet opvalt naast de rest van "
             "het kozijn."),
        ],
        "kosten": ["Hoeveel plekken er hersteld moeten worden en hoe groot de schade is",
                   "Vullen of een stuk hout vervangen",
                   "Of het hele kozijn of de hele deur meteen wordt geschilderd",
                   "Hoe goed de plek bereikbaar is"],
        "reviews": [3, 2],
        "zie_ook": [("Kozijnen en deuren schilderen", "dienst-kozijnen-deuren.html")],
    },
    "kozijnen-deuren": {
        "wanneer": [
            ("Buitenkozijnen en voordeuren", "Zodra de lak dof wordt, gaat scheuren of op de "
             "onderdorpels loslaat. Buiten gaat het snel als er eenmaal water achter de verf komt."),
            ("Binnendeuren en kozijnen", "Als de lak geel is geworden, beschadigd is rond de klink, "
             "of als er een andere kleur moet, bijvoorbeeld van houtlook naar wit."),
            ("Bij een verkoop of verhuizing", "Kozijnen en de voordeur ziet iemand als eerste. Nieuwe "
             "lak maakt daar veel verschil."),
        ],
        "signalen": ["Lak die bladdert op onderdorpels en in de hoeken",
                     "Hout dat zacht aanvoelt of donker is verkleurd",
                     "Open naden tussen het kozijn en het glas of de muur",
                     "Gele of doffe lak op binnendeuren en kozijnen",
                     "Een deur die klemt doordat er te veel lagen op zitten"],
        "materiaal": [
            ("Grondverf", "Op kaal of hersteld hout, zodat de lak goed hecht."),
            ("Lak voor binnen en buiten", "Buitenlak moet tegen zon en regen kunnen. Binnen "
             "vergeelt een watergedragen lak minder."),
            ("Houtrotvuller of nieuw hout", "Voor aangetaste plekken in kozijnen en onderdorpels, "
             "voordat er lak op gaat."),
        ],
        "kosten": ["Het aantal kozijnen en deuren",
                   "Binnen of buiten, en hoe goed alles bereikbaar is",
                   "Hoeveel houtrot er hersteld moet worden",
                   "Of de oude lak geschuurd of helemaal verwijderd moet worden",
                   "Een kleurwissel, bijvoorbeeld van donker naar wit, vraagt meer lagen"],
        "reviews": [3, 2],
        "voorna": True,
        "zie_ook": [("Buitenschilderwerk", "dienst-buitenschilderwerk.html"),
                    ("Houtreparaties en onderhoud", "dienst-houtwerk.html")],
    },
    "wanden-plafonds": {
        "wanneer": [
            ("Bij vlekken en verkleuring", "Als vlekken, vingerafdrukken of vergeling niet meer "
             "weggaan met schoonmaken."),
            ("Bij een nieuwe kleur", "Een andere kleur geeft een ruimte een ander gevoel. Van donker "
             "naar licht vraagt vaak een extra laag."),
            ("Na een lekkage of verbouwing", "Waterkringen en reparaties blijven zichtbaar zonder "
             "voorbehandeling. Die plekken krijgen eerst een isolerende grondlaag."),
        ],
        "signalen": ["Waterkringen of gele vlekken op het plafond",
                     "Verf die afbladdert of afgeeft als u eroverheen veegt",
                     "Doorschijnende plekken of een oude kleur die erdoor komt",
                     "Gaatjes en naden van pluggen en leidingen",
                     "Haarscheurtjes in de hoeken"],
        "materiaal": [
            ("Muurverf, mat of zijdeglans", "Mat verbergt oneffenheden het best. Zijdeglans is "
             "beter af te nemen, handig in een hal of kinderkamer."),
            ("Isolerende grondverf", "Op vlekken van water, nicotine of vet, zodat ze niet door "
             "de nieuwe laag heen komen."),
            ("Vochtbestendige verf", "Voor keuken en badkamer, waar gewone muurverf niet lang goed "
             "blijft."),
        ],
        "kosten": ["Het aantal vierkante meters wand en plafond",
                   "De hoogte, bijvoorbeeld een trapgat of een hoog plafond",
                   "Hoeveel voorbereiding de ondergrond nodig heeft",
                   "Het aantal lagen, zeker bij een kleurwissel",
                   "Of de ruimte leeg is of alles afgedekt moet worden"],
        "reviews": [1],
        "zie_ook": [("Binnenschilderwerk", "dienst-binnenschilderwerk.html"),
                    ("Behangen", "dienst-behang.html")],
    },
}

# Lokaal bewijs per plaats. Alleen wat echt uit die plaats komt: een review
# (index in REVIEWS) of een eigen project (beeld uit bouw.WERK). Waar niets
# is, staat niets, en dan tonen we reviews uit de regio met hun eigen plaats.
REGIO = {
    "Westervoort": {
        "intro": "Aribouw is gevestigd aan de Mommenkamp in Westervoort. Binnen- en "
                 "buitenschilderwerk, behangen en houtreparaties, voor woningen en bedrijfspanden.",
        "reviews": [2], "projecten": ["pui-voetzorg.webp"],
        "project_tekst": "De pui hieronder is van een praktijkruimte in Westervoort: een voormalige "
                         "garage. Cindy schreef er de review bij.",
    },
    "Duiven": {
        "intro": "Duiven grenst aan Westervoort, dus u woont vlak bij Aribouw. Binnen- en "
                 "buitenschilderwerk, behangen en houtreparaties.",
        "reviews": [], "projecten": [],
    },
    "Zevenaar": {
        "intro": "Zevenaar ligt net als Westervoort in de Liemers. Binnen- en buitenschilderwerk, "
                 "behangen en houtreparaties.",
        "reviews": [], "projecten": [],
    },
    "Arnhem": {
        "intro": "Arnhem grenst aan Westervoort. Binnen- en buitenschilderwerk, behangen en "
                 "houtreparaties, voor woningen, bedrijfspanden en praktijkruimtes.",
        "reviews": [], "projecten": [],
    },
    "Huissen": {
        "intro": "In Huissen heeft Aribouw deuren en kozijnen hersteld en geschilderd. Binnen- en "
                 "buitenschilderwerk, behangen en houtreparaties.",
        "reviews": [3], "projecten": [],
    },
}

# Twee specialismen met een eigen pagina, onder de hoofddiensten. Geen eigen
# dienstkaart en geen eigen film: ze hangen onder Diensten en worden bereikt
# via het overzicht en de links op de hoofdpagina's.
# (slug, naam, kort, lang, beeld, punten)
SUBDIENSTEN = [
    ("kozijnen-deuren", "Kozijnen en deuren schilderen",
     "Buitenkozijnen, voordeuren, binnendeuren en ander houtwerk. Eerst het hout in orde, dan een "
     "strakke laklaag.",
     "Bij kozijnen en deuren ziet u elk foutje: een druppel, een streep, verf op het glas of op het "
     "beslag. Daarom gaat de meeste tijd naar de voorbereiding: oude lak schuren of verwijderen, "
     "beschadigingen herstellen, glas en beslag strak afplakken. Buiten komt daar houtrot bij, dat "
     "eerst hersteld wordt. Pas dan gaan de grondverf en de lak erop.",
     "kozijn-buiten.webp",
     ["Buitenkozijnen, ramen en boeidelen",
      "Voordeuren, achterdeuren en binnendeuren",
      "Houtrot herstellen voordat er lak op gaat",
      "Glas en beslag strak afgeplakt"]),
    ("wanden-plafonds", "Wanden en plafonds schilderen",
     "Wanden en plafonds strak geschilderd, zonder strepen of vlekken. Meubels en vloeren afgedekt.",
     "Een muur of plafond schilderen lijkt simpel, maar juist op een groot vlak ziet u elke "
     "oneffenheid, elke overgang en elke streep. Gaatjes en naden zet ik eerst dicht, vlekken "
     "worden voorbehandeld, en plafonds en kozijnen strak afgeplakt. Stucwerk en egaliseren doe ik "
     "niet; is een wand daarvoor te slecht, dan hoort u dat vooraf.",
     "stap-uitvoeren.webp",
     ["Wanden in woonkamer, slaapkamer, hal en trapgat",
      "Plafonds, ook met vlekken of verkleuring",
      "Keuken en badkamer met vochtbestendige verf",
      "Strakke lijnen tussen wand, plafond en kozijn"]),
]
# Onder welke hoofddienst een specialisme hangt, voor de terugverwijzing.
SUB_OUDER = {"kozijnen-deuren": "buitenschilderwerk", "wanden-plafonds": "binnenschilderwerk"}

# Zijn eigen lijst van werkzaamheden uit de intake, letterlijk, met waar
# elke regel op de site over gaat.
WERKZAAMHEDEN = [
    ("Binnenschilderwerk", "dienst-binnenschilderwerk.html"),
    ("Buitenschilderwerk", "dienst-buitenschilderwerk.html"),
    ("Wand- en plafondschilderwerk", "dienst-wanden-plafonds.html"),
    ("Behangen", "dienst-behang.html"),
    ("Deuren, kozijnen en ander houtwerk schilderen", "dienst-kozijnen-deuren.html"),
    ("Trappen schilderen", "dienst-binnenschilderwerk.html#trappen"),
    ("Kleine houtreparaties", "dienst-houtwerk.html"),
    ("Klein renovatie- en onderhoudswerk", "dienst-houtwerk.html"),
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
     "planning: wanneer ik begin, hoeveel dagen het ongeveer duurt en of u thuis moet zijn."),
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
     "Op het Werkspot-profiel staat dat Aribouw garantie biedt. Hoe lang en waarop precies, "
     "staat in de offerte, zodat u het vooraf zwart op wit heeft."),
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
    "kozijnen-deuren": [5, 0, 3, 7],
    "wanden-plafonds": [0, 9, 3, 1],
}

ONBEVESTIGD = [
    "Eigen projectfoto's en voor-en-nafoto's: Ahmad stuurt ze apart. De site heeft er ruimte "
    "voor; nu staan er negen beelden van Facebook en Werkspot.",
    "Het logo als vectorbestand. Het logo van Ahmad staat er nu in, gemaakt uit een JPG; een SVG "
    "of PDF maakt het nog scherper.",
    "Garantietermijnen en gebruikelijke doorlooptijden: zichtbaar gemarkeerd in de vragenlijst.",
    "Certificaten en extra reviews: stuurt Ahmad apart.",
    "Socialmediapagina's: stuurt Ahmad apart. Het Instagram-account uit de eerste briefing is "
    "niet van dit bedrijf.",
    "De score van %s uit %s reviews is op %s van Werkspot gehaald. Dat getal loopt op, dus voor "
    "livegang even opnieuw kijken." % (SCORE, AANTAL_REVIEWS, SCORE_DATUM),
    "Formulieren hebben nog geen ontvanger. De WhatsApp-knoppen werken wel, met het echte nummer.",
]

# ---------------------------------------------------------------------
# Structured data. Aribouw als een entiteit met een vast @id, zodat Google
# en AI-zoekmachines de home, de dienstpagina's en de plaatspagina's aan
# hetzelfde bedrijf koppelen. Alleen wat aantoonbaar klopt: geen
# aggregateRating, want de reviews staan op Werkspot en niet op deze site.
# ---------------------------------------------------------------------
def bedrijf_id(variant="aflak"):
    return SITE_URL[variant] + "/#aribouw"


def bedrijf_jsonld(variant="aflak"):
    import json
    site = SITE_URL[variant]
    diensten = [{"@type": "Offer", "itemOffered": {
                    "@type": "Service", "name": d[1], "description": d[2],
                    "url": "%s/dienst-%s.html" % (site, d[0]) if variant == "aflak" else site + "/diensten.html"}}
                for d in (DIENSTEN + SUBDIENSTEN if variant == "aflak" else DIENSTEN)]
    graaf = [
        {"@type": "HousePainter", "@id": bedrijf_id(variant), "name": NAAM,
         "url": site + "/", "image": site + "/assets/og.jpg",
         "logo": {"@type": "ImageObject", "url": site + "/assets/logo.png",
                  "width": 630, "height": 600},
         "description": "Schildersbedrijf uit Westervoort voor binnen- en buitenschilderwerk, "
                        "behangen en houtreparaties, voor particulieren en professionals.",
         "founder": {"@type": "Person", "@id": site + "/#ahmad", "name": EIGENAAR,
                     "jobTitle": "Schilder en eigenaar"},
         "telephone": TEL_LINK, "email": MAIL, "vatID": BTW,
         "identifier": {"@type": "PropertyValue", "propertyID": "KvK", "value": KVK},
         "address": {"@type": "PostalAddress", "streetAddress": ADRES, "postalCode": POSTCODE,
                     "addressLocality": PLAATS, "addressCountry": "NL"},
         "areaServed": [{"@type": "City", "name": p} for p in WERKGEBIED_ALLES],
         "knowsAbout": ["binnenschilderwerk", "buitenschilderwerk", "behangen", "renovlies",
                        "glasvezelbehang", "houtrot herstellen", "kozijnen schilderen",
                        "deuren schilderen", "trappen schilderen"],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Diensten van Aribouw",
                             "itemListElement": diensten},
         "sameAs": [WERKSPOT]},
        {"@type": "WebSite", "@id": site + "/#website", "url": site + "/", "name": NAAM,
         "inLanguage": "nl-NL", "publisher": {"@id": bedrijf_id(variant)}},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graaf},
                      ensure_ascii=False, indent=2)


def dienst_jsonld(variant, dienst):
    import json
    slug, naam, kort = dienst[0], dienst[1], dienst[2]
    return json.dumps({
        "@context": "https://schema.org", "@type": "Service",
        "@id": "%s/dienst-%s.html#dienst" % (SITE_URL[variant], slug),
        "name": naam, "serviceType": naam, "description": kort,
        "provider": {"@id": bedrijf_id(variant)},
        "areaServed": [{"@type": "City", "name": p} for p in WERKGEBIED_ALLES],
        "url": "%s/dienst-%s.html" % (SITE_URL[variant], slug),
    }, ensure_ascii=False, indent=2)


JSONLD = bedrijf_jsonld("aflak")


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
