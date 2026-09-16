# Aribouw, twee websitevoorstellen

Twee uitgewerkte demo's voor Aribouw, het schildersbedrijf van Ahmad Nikzad
uit Westervoort: schilderwerk, behangen en houtreparaties. Beide varianten
delen huisstijl, fotografie en teksten. Het verschil zit in scope en in
designniveau, niet in kwaliteit. Ahmad heeft gekozen voor variant 2, Aflak.

Live: **https://bjornb0316.github.io/aribouw/**

Of open `index.html` lokaal om ze naast elkaar te zien.

---

## Wat waar staat

```
index.html                keuzepagina: beide varianten naast elkaar
assets/img/               gedeelde foto's (WebP)
assets/film/              Higgsfield-films voor Aflak (MP4 + poster)
variant-grondlaag/        Professional, 6 pagina's
variant-aflak/            Performance, 14 pagina's
  assets/css/stijl.css    per variant, uit dezelfde tokens gegenereerd
  assets/js/main.js       per variant
bron/                     ruwe downloads, niet voor de server
bouwscript/               de generator (Python, geen build-stap nodig)
```

```bash
python bouwscript/alles.py        # bouwen
python bouwscript/server.py 8181  # lokaal bekijken
```

De standaard `python -m http.server` kapt op Windows bestanden af op 65280
bytes, vandaar een eigen servertje.

---

## Wat er gecontroleerd en overgenomen is

### Van Ahmad zelf, 15 september 2026

Ahmad heeft zijn gegevens en wensen aangeleverd. Die staan allemaal in
`bouwscript/data.py` en zijn verwerkt:

| wat | waarde |
| --- | --- |
| Eigenaar | Ahmad Nikzad |
| Telefoon en WhatsApp | 06 83 04 41 91 |
| E-mail | aribouw10@gmail.com |
| Adres | Mommenkamp 27, 6932 HT Westervoort |
| KvK en btw | 95128905, NL005131384B93 |
| Werkgebied | Westervoort, Duiven, Zevenaar, Arnhem, Doesburg, Didam, Dieren, Velp, Huissen, Elst, Ede, Nijmegen. Grotere projecten ook daarbuiten |

Wat dat in de site heeft veranderd:

- **Westervoort in plaats van Zevenaar** als vestigingsplaats, overal: titels,
  footer, structuurdata, plaatspagina's. Westervoort heeft nu de eerste
  plaatspagina
- **Diensten volgens zijn eigen lijst**: wanden en plafonds, trappen en kleine
  houtreparaties erbij. De vierde dienst heet nu *Houtreparaties en onderhoud*
  (`dienst-houtwerk.html`, was `dienst-renovatie.html`). Plinten en kitwerk
  staan er niet meer als dienst, want die noemde hij niet
- **Geen stucwerk of egaliseren**: nergens als dienst, "gladmaken" is uit de
  behangtekst, en het staat als vraag in de lijst zodat niemand erop rekent
- **Aannemers en architecten**: een eigen blok op de home met de knop
  *Project voorleggen*. Die opent de aanvraag met `?soort=zakelijk`, waardoor
  de vraag "om hoeveel gaat het" al op *een zakelijk project* staat. Er is een
  vraag over zakelijk werk bij, en het contactformulier heeft die keuze ook
- **Persoonlijke toon**: de teksten staan in de ik-vorm. Ahmad komt kijken en
  doet het werk, dus "ik kom langs" in plaats van "er wordt gekeken". De home
  van Aflak heeft een blok *Over Aribouw* met zijn eigen woorden, licht
  ingekort, en de Over-pagina van Grondlaag is herschreven met hetzelfde verhaal
- **Positionering**: "Aribouw is een schilder, geen algemeen bouwbedrijf", met
  zijn eigen zinnen over voorbereiding, materiaal en netjes werken
- **Ruimte voor eigen foto's**: de voor-en-na paren staan in `VOORNA` in
  `bouwscript/bouw.py`. Elk paar dat erbij komt krijgt op de werkpagina van
  Aflak vanzelf een eigen schuif. Projectfoto's gaan in `WERK`

Er is bewust niets verzonnen over een team: Ahmad schrijft dat hij daar naartoe
wil groeien, en zo staat het er ook.

### Werkspot

Het Werkspot-profiel is op **8 september 2026** bekeken. Daar stond:

- **5,0 uit 31 reviews**
- **KvK 95128905**
- "Geverifieerd door Werkspot", "Biedt garantie", "Ingeschreven bij KvK"
- De dienstenlijst: buitenschilderwerk, binnenschilderwerk, behangen kamer,
  renovlies en glasvezel, behang verwijderen, kitten, plinten

Die zeven diensten zijn teruggebracht tot vier groepen, want de briefing zegt
expliciet: geen klusbedrijf met twintig diensten.

De vier reviews op de site staan letterlijk zo op Werkspot, met naam, plaats en
datum. Ze zijn ingekort tot maximaal drie regels zonder de betekenis te
veranderen.

### Belangrijk: het Instagram-account uit de briefing klopt niet

De eerste briefing noemde `instagram.com/aribouw`. Dat account staat op naam van
**"walid aribou"**, heeft **nul volgers en geen enkele post**. Dat is niet dit
bedrijf. Er wordt daarom nergens naar gelinkt. Ahmad stuurt zijn eigen
socialmediapagina's apart.

---

## De fotografie

Er is weinig, en dat heeft het ontwerp bepaald. Negen bruikbare beelden uit
vier bronbestanden: de Facebookpagina Ari Bouw en het Werkspot-profiel. Geen
site die om een fotogalerij heen is gebouwd, maar een die om kleurvlakken en
typografie heen is gebouwd, met die foto's als de momenten.

Wat er bewust **niet** in zit:

- de tuin met de schommel, voor en na. Mooi werk, maar dat is grondwerk, en de
  briefing zegt juist: positioneer als schilder, niet als klusbedrijf
- de gangkast met jassen erin, een rommelig "before" zonder tegenhanger
- de twee logo-afbeeldingen; dat zijn geen projectfoto's

De voor-en-na van de binnendeur is een echt paar, maar niet vanaf hetzelfde
punt geschoten en met "Before" en "After" in het beeld gebrand. De onderste
dertig procent is eruit gesneden, waardoor die labels wegvallen en de deur bij
allebei op dezelfde plek in beeld staat. Daarna klopt de schuif wel.

De pui hoort bij de review van Cindy uit Westervoort: een voormalige garage die
praktijkruimte werd.

### Aflak: films en sfeerbeelden met Higgsfield

Aflak heeft er gegenereerd beeld bij gekregen. De regel die daarbij is
aangehouden: **gegenereerd beeld laat het vak zien, nooit een klus.** Handen,
tape, een kwast, een kamer. Geen gezichten, geen "dit hebben wij gedaan". Alles
onder Werk en de voor-en-na blijven eigen foto's. In de kleurkiezer staat er
letterlijk onder dat het een sfeerbeeld is.

| wat | waar | model |
| --- | --- | --- |
| Hero-film: tape gaat van de muur, er blijft een kaarsrechte lijn over | home | Kling 3.0 Pro, start- en eindbeeld |
| Vier dienstfilms: roller, kwast op een kozijn, behang, kitwerk | dienstkaarten (lopen bij hover) en de kop van elke dienstpagina | Kling 3.0 Pro vanaf Nano Banana Pro-stills |
| Woning in de schemer | bovenin elk contactblok | Kling 3.0 Pro |
| Vier kamers per kleurrichting | kleurkiezer (wisselt mee bij hover en klik) en als duimnagel in de offerteflow | Soul 2.0 en Nano Banana Pro |
| Vijf procesbeelden | werkwijze, bij elke stap | Soul 2.0 en Nano Banana Pro |
| Straat met rijtjeshuizen, keukentafel | kop van werkgebied, plaatspagina's en offerte | Soul 2.0 en Nano Banana Pro |

Elke still is bekeken voordat hij erin ging. Afgekeurd: een roller zonder
rol, een verfblik met een verzonnen merknaam, een "afgewerkte" muur met een
scheur erin, en een offerte met nephandschrift. Die zijn opnieuw gemaakt.

De films laden pas als ze in beeld komen, spelen zonder geluid en staan stil
bij `prefers-reduced-motion` of databesparing; dan blijft de poster staan.
Samen zijn de zes films ongeveer 4 MB.

De eerste hero-poging is ook bewaard (`bron/higgsfield/v61.mp4`): mooi, maar de
tape kwam nauwelijks los. Daarom is de uiteindelijke versie gemaakt met een
begin- en eindbeeld.

```bash
python bouwscript/film.py         # ruwe Higgsfield-bestanden omzetten
```

De ruwe bestanden (ruim 150 MB) staan in `bron/higgsfield/` en gaan niet mee
in git. `film.py` heeft ffmpeg nodig, of `FFMPEG=pad/naar/ffmpeg`.

---

## Het ontwerp

Waar een schilder op wordt afgerekend is **de snijlijn**: de overgang waar twee
vlakken elkaar raken. Strak afgeplakt, geen verf op het glas. Dat is de
layoutlogica geworden.

- Secties raken elkaar in een schuine, kaarsrechte kleurrand. Dat is het enige
  scheidingsteken dat de site heeft
- De sectiekop staat op een **linkerrail**, zoals het etiket op een verfblik:
  aanduiding links, inhoud rechts
- De diensten liggen als **kleurstalen uit een waaier**, licht gedraaid, en
  gaan rechtliggen als je erover gaat
- De werkwijze is een **verticale tijdlijn** met de stappen om en om, geen rij
  van vijf kolommen. Een klus is een volgorde, geen raster
- Radius 4px, want binnenwerk is glad afgewerkt

| token | waarde | rol |
| --- | --- | --- |
| `--papier` | `#F6F4F0` | de grond |
| `--zand` | `#E9E4DB` | afwisselende secties |
| `--blauw` | `#14508C` | het accent, hun eigen blauw |
| `--nacht` | `#171A1F` | de donkere grond onderaan |
| `--r` | `4px` | het enige radius-systeem |

Het accent is niet gekozen maar overgenomen: het blauw uit hun eigen logo op
Facebook, iets dieper gezet zodat wit erop 7,9 haalt.

Fonts: Supreme 700 voor koppen, Synonym 400/500/700 voor de rest, via
Fontshare.

---

## Het verschil tussen de twee

### Grondlaag (Professional), 6 pagina's

Home, diensten, werk, over Aribouw, offerte, contact.

- Gesplitste hero met het beeld dat rechts van het scherm afloopt
- Alle vier de diensten op één pagina, twee beeld-tekst-blokken en een raster
- Voor en na naast elkaar
- Vier echte Werkspot-reviews met naam, plaats en datum
- Contactformulier met veldcontrole en bevestiging in beeld

### Aflak (Performance), 14 pagina's

Geen Grondlaag met extra pagina's, maar een andere uitvoering.

**Ander designniveau**

- Waar Grondlaag alles op papier houdt, zet Aflak hele secties in **diepblauw**.
  De vlakken raken elkaar in dezelfde schuine snijlijn
- Groter zetwerk: de kop loopt tot 4,2rem in plaats van 3,4rem
- Meer lucht tussen de secties

**En wat er functioneel bij komt**

- **Filmhero**: tape die van de muur gaat, speelt een keer en blijft op de
  strakke lijn staan. Elke dienstpagina opent met een eigen film
- **Voor-en-na** van dezelfde binnendeur op home en werk, sleepbaar met muis,
  vinger en toetsenbord (pijltjes, Home en End), met een `aria-valuenow` die
  meeloopt
- **Kleurkiezer met beeld**: vier richtingen, bij elke richting een kamer in
  die kleur en waar op gelet moet worden. De keuze gaat mee de aanvraag in
- **Werkwijze in beeld** en een contactblok dat opent met een woning in de schemer
- **Over Aribouw en een route voor aannemers en architecten** op de home
- **Aanvraag in zes stappen**: wat, hoeveel, kleur, ondergrond, wanneer, en pas
  op het eind drie velden
- **Slimme prefill**: wie via de kleurkiezer binnenkomt slaat de kleurvraag
  over, maar de kleur staat wel in het eindbericht. Via een dienstpagina wordt
  de eerste vraag overgeslagen, via *Project voorleggen* de tweede
- **WhatsApp-bericht dat al is ingevuld**: de klikantwoorden plus naam, plaats
  en telefoonnummer
- **Vier dienstpagina's** met eigen tekst, eigen vragen en FAQ-structuurdata
- **Vier plaatspagina's**: Westervoort, Duiven, Zevenaar, Arnhem. De werkgebiedpagina
  noemt alle twaalf plaatsen; meer bijna gelijke plaatspagina's lezen als opvulling

Wat Grondlaag niet minder heeft: dezelfde foto's, dezelfde typografie, dezelfde
reviews en dezelfde mobiele navigatie.

---

## Wat er gecontroleerd is

- 34 unieke adressen op de lokale server, allemaal 200, nul dode interne links
- 21 pagina's geladen: nul console-errors, precies één `h1` per pagina, elke
  `img` met `alt`, `width` en `height`, geen dode `href="#"`
- Geen em-dashes in de hele site
- Geen horizontale overflow op 1440 en op 375
- Contrast nagemeten: 149 tekstelementen op de home van Aflak, alle boven de
  WCAG AA-drempel. Vijf fouten gevonden en opgelost, allemaal op de blauwe en
  donkere vlakken: de railkop stond in donkere inkt op blauw, de stapnummers
  haalden 4,42, de bijschriften 4,44 op zand, en de lijnknop op de donkere
  sectie stond in donkere inkt op donker
- Voor-en-na schuif getest met toetsenbord en met slepen
- Kleurkiezer: alle vier de richtingen geven de juiste uitleg, de juiste link
  en de juiste WhatsApp-tekst
- Zesstapsflow doorgeklikt met `?kleur=donker`: de kleurvraag wordt
  overgeslagen en de kleur staat toch in het eindbericht. Leeg versturen
  blokkeert op drie velden
- Grondlaag-formulier: blokkeert leeg versturen op alle vier de verplichte
  velden, daarna bevestiging
- Mobiel menu: openen, sluiten, `aria-expanded`, scrollvergrendeling
- Alle teksten nagelezen; overal "u", nergens een prijs of een levertijd

---

## Verbeterplan: wat er staat

**Home.** De h1 bevat "Schilder in Westervoort, Arnhem en omgeving" plus de merkzin.
Direct onder de hero een vertrouwensstrook: 5,0 uit 31 Werkspot-reviews, eigen werk,
vrijblijvend langskomen, gevestigd in Westervoort. Volgorde: hero, vertrouwen,
diensten, eigen werk, kleurhulp, werkwijze, Ahmad, reviews, vragen, aanvraag. Bij
diensten, werk en reviews een CTA die past bij wat de bezoeker net zag. Mobiel
onderaan Bellen, WhatsApp en Offerte.

**Dienstpagina's** (`DIENST_INHOUD` in `data.py`). Elke dienst heeft nu: waar de uren
in gaan zitten, wanneer het tijd is, waar u zelf op kunt letten, welk materiaal en
waarom, waar de prijs van afhangt, de werkwijze, alleen de reviews die over dat soort
werk gaan, vragen, andere diensten. Algemene vakkennis; geen prijzen, geen termijnen,
geen verzonnen feiten over Aribouw.

**Plaatspagina's** (`REGIO` in `data.py`). Westervoort, Duiven, Zevenaar, Arnhem en
Huissen. Alleen echt lokaal bewijs: Westervoort toont de pui van de praktijkruimte met
Cindy's review, Huissen de review over de herstelde deuren en kozijnen. Waar nog niets
uit die plaats is, staat dat er eerlijk: reviews uit de regio, met de plaats erbij.
Zodra er een project of review uit een plaats is, gaat die in `REGIO`.

**Project doorgeven** (`project-doorgeven.html`, niet in menu of sitemap). Voor Ahmad,
na elke klus op zijn telefoon: plaats, maand, soort werk, wat er gedaan is, hoe het
ervoor was, de aanpak, het resultaat en of de foto's online mogen. De knop zet alles in
een WhatsApp-bericht naar Bjorn; de foto's gaan in hetzelfde gesprek. Daaruit worden de
projectpagina's gemaakt.

**Structured data.** Een entiteit met `@id`: `HousePainter` met eigenaar, KvK, btw,
diensten en alle twaalf plaatsen, plus `WebSite`. Elke dienstpagina een `Service`,
elke subpagina een `BreadcrumbList`. Bewust geen `aggregateRating`: de reviews staan
op Werkspot, niet op deze site.

**Nog niet gedaan, en waarom:**

- Nieuwe URL's (`/binnenschilderwerk/`, `/schilder-westervoort/`): samen met de
  verhuizing naar het eigen domein, anders gaan alle links twee keer om
- Aparte pagina's voor kozijnen, deuren en renovlies: pas met echte foto's en
  projecten, anders worden het bijna gelijke pagina's
- Projectpagina's: wachten op de eerste projecten via het formulier
- Google Bedrijfsprofiel, Search Console, Bing: na het domein, door Ahmad
- Analytics: kies iets zonder cookies (Cloudflare Web Analytics of Plausible), dan
  blijft de privacyverklaring kloppen

## Klaar voor livegang: drie schakelaars

Bovenin `bouwscript/data.py` staan drie instellingen. Alle drie staan nog in
demostand; bij livegang zet je ze om en draai je `python bouwscript/alles.py`.

| schakelaar | nu | bij livegang |
| --- | --- | --- |
| `LIVE` | `False`: voorbeeldbalk, voetregel van Bjorn, `noindex` op elke pagina, `robots.txt` blokkeert alles | `True`: dat gaat allemaal weg, `robots.txt` wijst naar de sitemap |
| `SITE_URL["aflak"]` | de GitHub Pages-map | het echte domein, zonder slash aan het eind |
| `FORMULIER_ACTIE` | leeg: formulieren controleren en bevestigen, maar versturen niets | bijvoorbeeld `https://formsubmit.co/ajax/aribouw10@gmail.com` |

### Formulieren

Het contactformulier en de offerteflow sturen hun gegevens als JSON naar
`FORMULIER_ACTIE`. Elke dienst die JSON per POST aanneemt en 2xx teruggeeft,
werkt. FormSubmit heeft geen account nodig: de eerste aanvraag stuurt Ahmad een
activatiemail die hij een keer bevestigt. Daarna komen aanvragen binnen als
nette tabel met onderwerpregel.

- De offerteflow stuurt elke klikvraag met een eigen label: werk, omvang,
  kleurrichting, ondergrond, wanneer, plus naam, telefoon en plaats
- Tijdens versturen staat er "Versturen..." op de knop en werkt een tweede
  klik niet
- Mislukt het, dan blijft alles ingevuld staan en staat eronder: bel of app
  mij op 06 83 04 41 91
- Een verborgen lokveld houdt spambots tegen: die krijgen een bevestiging,
  maar er gaat niets weg
- In demostand zegt de bevestiging eerlijk dat er nog niets de deur uit gaat.
  Met een ontvanger valt die zin vanzelf weg

Getest met een lokaal nep-endpoint (niets naar Ahmad gestuurd): beide
formulieren kwamen compleet binnen, een serverfout geeft de foutmelding met
behoud van de invoer, en het lokveld verstuurt niets. Test zelf zonder de code
aan te passen met de omgevingsvariabele `ARIBOUW_FORMULIER`.

### Privacyverklaring

`privacy.html` in beide varianten, gelinkt vanuit de footer en onder elk
formulier. Geschreven voor wat de site echt doet: geen cookies, geen
analytics, lettertypen via Fontshare. Drie punten zijn een keuze en geen wet,
dus even met Ahmad bevestigen:

- aanvragen zonder opdracht verwijderen **binnen twaalf maanden** (de zeven
  jaar voor opdrachten is de wettelijke bewaarplicht)
- de naam van de formulierdienst (gemarkeerd op de pagina)
- de naam van de hostingpartij (gemarkeerd op de pagina)

Komt er ooit Google Analytics of een pixel bij, dan moet de verklaring mee en
is er een cookiemelding nodig.

### SEO-basis

- `sitemap.xml` en `robots.txt` per variant, gegenereerd bij elke build
- Canonical en `og:url` op elke pagina, met de eigen URL van die pagina
- Favicon (het merkteken als SVG) en een `apple-touch-icon`
- Deelafbeelding van 1200 bij 630 voor WhatsApp, Facebook en LinkedIn: de
  strakke lijn uit de hero met ARIBOUW erop (`film.py`, functie `deelbeeld`)
- Structuurdata van de home met url, afbeelding, adres, telefoon, e-mail, btw
  en alle twaalf plaatsen

## Voor livegang vervangen of bevestigen

Naast de drie schakelaars hierboven:

### Harde blokkers

| wat | waar | opmerking |
| --- | --- | --- |
| Eigen projectfoto's en voor-en-na | `bron/`, dan `VOORNA` en `WERK` in `bouw.py` | Ahmad stuurt ze apart. Nu staan er negen beelden van Facebook en Werkspot |
| `[NOG AANVULLEN: garantietermijnen]` | `data.py`, `VRAGEN` | Werkspot vermeldt wel dát er garantie is, niet hoe lang |
| `[NOG AANVULLEN: gebruikelijke doorlooptijden]` | `data.py`, `VRAGEN` | zichtbaar gemarkeerd |
| Het logo | `bouw.py`, constante `MARK` | er staat nu een diagonaal doorgesneden vierkant, het motief van de site. Ahmad stuurt het logo apart; een vectorbestand vervangt dit |
| Alleen Aflak overhouden | keuzepagina, `variant-grondlaag/` | Ahmad koos Aflak: die naar de hoofdmap, de rest eruit. De paden `../assets/` gaan dan mee |
| Houtwerkfilm | `bouw.py`, `DIENST_FILM["houtwerk"]` | nu de kitwerk-film, die niet over hout gaat. Het Higgsfield-tegoed was op (0,97 credits); een nieuwe film kost ongeveer 11 credits |

### Nog te ontvangen of te bevestigen

| wat | opmerking |
| --- | --- |
| Socialmediapagina's | stuurt Ahmad apart. Het Instagram-account uit de eerste briefing is niet van dit bedrijf |
| Certificaten en extra reviews | stuurt Ahmad apart |
| De score | 5,0 uit 31 op 8 september 2026. Dat getal loopt op, voor livegang opnieuw kijken |
| Adres op de site | Mommenkamp 27 staat nu in de footer, het contactblok, de privacyverklaring en de structuurdata. Even checken of Ahmad dat woonadres openbaar wil hebben |
| Bewaartermijn aanvragen | twaalf maanden in de privacyverklaring, zie hierboven |
| Domein | heeft Ahmad er al een? Nodig voor `SITE_URL` |
| Prijzen | bewust nergens genoemd |

Opgelost met de gegevens van 15 september: telefoonnummer, e-mail, adres,
btw-nummer en werkgebied.
