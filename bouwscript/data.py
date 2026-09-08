# -*- coding: utf-8 -*-
"""Alle harde gegevens over Aribouw op een plek.

Wat er gecontroleerd is en waar het vandaan komt:

  - Het Werkspot-profiel is op 8 september 2026 bekeken. Daar stond 5 uit 5
    op basis van 31 reviews, KvK-nummer 95128905, en de vermeldingen
    "Geverifieerd door Werkspot" en "Biedt garantie".
  - De dienstenlijst is hun eigen lijst van dat profiel, samengevoegd tot
    vier groepen zodat het geen klusbedrijf met twintig diensten wordt.
  - De reviews hieronder staan letterlijk zo op Werkspot, met naam, plaats
    en datum erbij.
  - Hun eigen omschrijving en hun eigen zin over vakwerk komen van het
    Werkspot-profiel en de Facebookpagina.

Wat er NIET in staat:
  - Telefoonnummer, e-mailadres en adres. Die waren nergens openbaar te
    vinden, dus er staan zichtbare placeholders.
  - Het Instagram-account @aribouw uit de briefing. Dat staat op naam van
    "walid aribou", heeft nul volgers en geen posts. Er wordt dus nergens
    naar gelinkt.
  - Prijzen. De klant wil ze niet tonen.
"""

NAAM = "Aribouw"
ONDERTITEL = "Schilderen &middot; behangen &middot; renovatie"
PERSOON = "Ahmad"
PLAATS = "Zevenaar"

# Nog niet openbaar gevonden. Zichtbaar als placeholder laten staan.
TEL_TOON = "[TELEFOONNUMMER]"
TEL_LINK = "+31600000000"
WA = "31600000000"
MAIL = "[E-MAILADRES]"

KVK = "95128905"
WERKSPOT = "https://www.werkspot.nl/profiel/aribouw"
FACEBOOK = "https://www.facebook.com/aribouw/?locale=nl_NL"
BJORN_WA = "31614664161"

# Hun eigen zin, van de Facebookpagina.
CLAIM = "Betrouwbaar vakwerk met oog voor detail"

# Op 8 september 2026 van het Werkspot-profiel gehaald.
SCORE = "5,0"
AANTAL_REVIEWS = "31"
SCORE_DATUM = "8 september 2026"

WERKGEBIED = ["Zevenaar", "Arnhem", "Duiven", "Westervoort"]

# De zeven diensten van hun Werkspot-profiel, teruggebracht tot vier groepen.
# (slug, naam, kort, lang, beeld, punten)
DIENSTEN = [
    ("binnenschilderwerk", "Binnenschilderwerk",
     "Muren, plafonds, deuren, kozijnen en trappen. Strak afgeplakt, netjes achtergelaten.",
     "Binnen schilderen is vooral voorwerk. Ontvetten, schuren, plamuren, aftapen. Dat deel ziet "
     "niemand terug, en juist daar zit het verschil tussen een muur die er twee jaar goed uitziet "
     "en een die er tien jaar goed uitziet. Meubels worden afgedekt en aan het eind gaat alles "
     "terug zoals het stond.",
     "deur-na.webp",
     ["Muren, plafonds en wanden",
      "Deuren, kozijnen en plinten",
      "Trapgangen en overlopen",
      "Alles afgedekt, aan het eind weer opgeruimd"]),
    ("buitenschilderwerk", "Buitenschilderwerk",
     "Kozijnen, deuren, boeidelen en buitenhout. Eerst het houtwerk herstellen, dan pas verf.",
     "Buitenwerk gaat kapot op de plekken waar water blijft staan: onderdorpels, hoeken van "
     "kozijnen, de onderkant van een deur. Verf daaroverheen zetten lost niets op. Eerst het "
     "aangetaste hout eruit en herstellen, dan gronden en aflakken. Anders staat u over twee jaar "
     "weer op dezelfde plek.",
     "kozijn-buiten.webp",
     ["Kozijnen, deuren en boeidelen",
      "Houtherstel voordat er verf op gaat",
      "Kitwerk langs beglazing vernieuwen",
      "Ook bedrijfspanden en praktijkruimtes"]),
    ("behang", "Behang en wandafwerking",
     "Behangen, renovlies en glasvezel. Ook het oude behang eraf en de wand weer glad.",
     "De helft van een goed behangresultaat zit in de ondergrond. Een wand met resten oud behang, "
     "gaatjes of losse plekken geeft altijd naden die je later ziet. Oud behang eraf, wand "
     "herstellen, en pas dan behangen. Bij renovlies en glasvezel komt daar nog een laag verf "
     "overheen.",
     "wand-detail.webp",
     ["Behang aanbrengen en verwijderen",
      "Renovlies en glasvezelbehang",
      "Wanden herstellen en gladmaken",
      "Advies over materiaal bij uw ondergrond"]),
    ("renovatie", "Kleine renovaties",
     "Plinten, kitwerk, houtherstel en de afwerking waar andere partijen niet aan toekomen.",
     "Vaak is het niet een grote klus maar een rij kleine dingen: plinten die vervangen moeten, "
     "kitwerk dat zwart is geworden, een deur die klemt, een stuk houtrot. Los besteden bij vier "
     "partijen kost meer tijd dan het werk zelf. Dat kan in een keer mee.",
     "pui-voetzorg.webp",
     ["Plinten plaatsen of vervangen",
      "Kitwerk in keuken, badkamer en langs kozijnen",
      "Houtherstel en kleine reparaties",
      "Meerdere klussen in een keer"]),
]

# Wat er gebeurt, van eerste bericht tot oplevering. Geen doorlooptijden,
# want die zijn niet bevestigd.
STAPPEN = [
    ("01", "U stuurt foto's of belt",
     "Een paar foto's van de ruimte of het kozijn zeggen vaak al genoeg. Vermeld erbij wat u wilt "
     "en wanneer het ongeveer zou moeten."),
    ("02", "Langskomen en opmeten",
     "Er wordt gekeken naar de ondergrond, de staat van het hout en wat er aan voorwerk nodig is. "
     "Daar zit vaak meer werk in dan mensen denken."),
    ("03", "Offerte met het voorwerk erin",
     "Op papier staat wat er gebeurt: schuren, plamuren, gronden, aflakken. Zo is te zien waar de "
     "uren in gaan zitten en waarom."),
    ("04", "Uitvoeren",
     "Afdekken, afplakken, werken. U hoort vooraf wanneer er wordt begonnen en of u thuis moet "
     "zijn."),
    ("05", "Opruimen en samen nalopen",
     "Tape eraf, spullen terug, afvalmateriaal mee. Aan het eind wordt het werk samen "
     "doorgelopen."),
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

# De bezwaren uit de briefing, eerlijk beantwoord.
VRAGEN = [
    ("Wat gaat het kosten?",
     "Dat hangt af van de oppervlakte, de staat van de ondergrond en hoeveel voorwerk er nodig "
     "is. Twee kamers van dezelfde maat kunnen een factor twee schelen, puur door wat eronder "
     "zit. Daarom komt er eerst iemand kijken en pas daarna een prijs."),
    ("Wordt mijn woning netjes achtergelaten?",
     "Meubels worden afgedekt en vloeren beschermd. Tape gaat er aan het eind af, spullen gaan "
     "terug zoals ze stonden en het afvalmateriaal gaat mee. Op Werkspot is dat het punt dat het "
     "vaakst terugkomt in de reviews."),
    ("Hoe lang duurt het?",
     "Dat verschilt te veel per klus om er hier een getal aan te hangen. Bij de offerte hoort een "
     "planning: wanneer er wordt begonnen, hoeveel dagen het ongeveer duurt en of u thuis moet "
     "zijn. [NOG AANVULLEN: gebruikelijke doorlooptijden]"),
    ("Welke verf of welk behang is geschikt?",
     "Dat hangt af van de ruimte en de ondergrond. In een badkamer of keuken is een andere lak "
     "nodig dan in een slaapkamer, en op een wand met scheurtjes werkt renovlies beter dan "
     "gewoon behang. U krijgt advies, en de keuze blijft aan u."),
    ("Moet ik zelf verf of behang regelen?",
     "Dat mag, en het hoeft niet. Koopt u zelf, dan hoort u vooraf hoeveel er nodig is en welk "
     "type past. Wordt het meegenomen, dan staat het als post in de offerte."),
    ("Wordt beschadigd hout eerst hersteld?",
     "Ja. Verf over rot hout is weggegooid geld. Aangetast hout wordt uitgehaald en hersteld "
     "voordat er gegrond wordt. Zit er te veel in, dan hoort u dat bij de opname en niet pas als "
     "het werk al loopt."),
    ("Kan hij verschillende werkzaamheden combineren?",
     "Ja, dat is juist waar Aribouw handig in is. Schilderwerk, behang, plinten en kitwerk in een "
     "planning scheelt tijd en gedoe met meerdere partijen."),
    ("Heb ik garantie op de afwerking?",
     "Op het Werkspot-profiel staat dat Aribouw garantie biedt. De precieze termijn en waar hij "
     "op geldt hoort bij de offerte. [NOG AANVULLEN: garantietermijnen]"),
    ("Hoe weet ik dat het goed komt?",
     "Op Werkspot staan %s reviews met een gemiddelde van %s. Die zijn openbaar, inclusief de "
     "reacties eronder. Vraag bij de opname gerust naar een adres van een klus in de buurt."
     % (AANTAL_REVIEWS, SCORE)),
]

ONBEVESTIGD = [
    "Telefoonnummer, e-mailadres en adres. Nergens openbaar gevonden; er staan zichtbare "
    "placeholders in de site en de WhatsApp-knoppen wijzen naar een leeg nummer.",
    "Het Instagram-account @aribouw uit de briefing is niet van dit bedrijf. Het staat op naam "
    "van 'walid aribou', heeft nul volgers en geen enkele post. Er wordt nergens naar gelinkt. "
    "Vraag na of er een ander account is.",
    "De score van %s uit %s reviews is op %s van Werkspot gehaald. Dat getal loopt op, dus voor "
    "livegang even opnieuw kijken." % (SCORE, AANTAL_REVIEWS, SCORE_DATUM),
    "Garantietermijnen en gebruikelijke doorlooptijden: zichtbaar gemarkeerd in de vragenlijst.",
    "Werkgebied: de reviews komen uit Driel, Apeldoorn, Kilder, Huissen en Westervoort. Er wordt "
    "dus verder gereden dan Zevenaar en Arnhem. Even vaststellen wat het werkgebied echt is.",
    "Prijzen: bewust nergens genoemd, conform de briefing.",
    "Het logo is overgenomen van een foto op Facebook. Voor livegang is een vectorbestand nodig.",
]

JSONLD = """{
  "@context": "https://schema.org",
  "@type": "HousePainter",
  "name": "Aribouw",
  "description": "Schilderwerk, behang en kleine renovaties in Zevenaar, Arnhem en omgeving.",
  "address": {"@type": "PostalAddress", "addressLocality": "Zevenaar", "addressCountry": "NL"},
  "areaServed": ["Zevenaar", "Arnhem", "Duiven", "Westervoort"],
  "sameAs": ["https://www.werkspot.nl/profiel/aribouw"]
}"""


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
