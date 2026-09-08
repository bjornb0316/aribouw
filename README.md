# Aribouw, twee websitevoorstellen

Twee uitgewerkte demo's voor Aribouw uit Zevenaar: schilderwerk, behang en
kleine renovaties. Beide varianten delen huisstijl, fotografie en teksten. Het
verschil zit in scope en in designniveau, niet in kwaliteit.

Live: **https://bjornb0316.github.io/aribouw/**

Of open `index.html` lokaal om ze naast elkaar te zien.

---

## Wat waar staat

```
index.html                keuzepagina: beide varianten naast elkaar
assets/img/               gedeelde foto's (WebP)
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

De briefing noemt `instagram.com/aribouw`. Dat account staat op naam van
**"walid aribou"**, heeft **nul volgers en geen enkele post**. Dat is niet dit
bedrijf. Er wordt daarom nergens naar gelinkt. Vraag na of er een ander account
is.

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

- **Cinematische hero** met de voor-en-na van dezelfde binnendeur, sleepbaar
  met muis, vinger en toetsenbord (pijltjes, Home en End), met een
  `aria-valuenow` die meeloopt
- **Kleurkiezer**: vier richtingen, met per richting waar op gelet moet worden.
  De keuze gaat mee de aanvraag in
- **Aanvraag in zes stappen**: wat, hoeveel, kleur, ondergrond, wanneer, en pas
  op het eind drie velden
- **Slimme prefill**: wie via de kleurkiezer binnenkomt slaat de kleurvraag
  over, maar de kleur staat wel in het eindbericht. Via een dienstpagina wordt
  de eerste vraag overgeslagen
- **WhatsApp-bericht dat al is ingevuld**: de klikantwoorden plus naam, plaats
  en telefoonnummer
- **Vier dienstpagina's** met eigen tekst, eigen vragen en FAQ-structuurdata
- **Vier plaatspagina's**: Zevenaar, Arnhem, Duiven, Westervoort

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

## Voor livegang vervangen of bevestigen

De demo staat op `noindex,nofollow` en elke pagina heeft bovenin een balk die
zegt dat het een voorstel is. Beide moeten eruit voordat de site echt live gaat.

### Harde blokkers

| wat | waar | opmerking |
| --- | --- | --- |
| `[TELEFOONNUMMER]` en `[E-MAILADRES]` | `bouwscript/data.py` | nergens openbaar gevonden. De WhatsApp-knoppen wijzen nu naar een leeg nummer |
| `[NOG AANVULLEN: garantietermijnen]` | `data.py`, `VRAGEN` | Werkspot vermeldt wel dát er garantie is, niet hoe lang |
| `[NOG AANVULLEN: gebruikelijke doorlooptijden]` | `data.py`, `VRAGEN` | zichtbaar gemarkeerd |
| Het logo | `bouw.py`, constante `MARK` | er staat nu een diagonaal doorgesneden vierkant, het motief van de site. Hun echte logo bestaat alleen als foto op Facebook; een vectorbestand vervangt dit |
| `noindex,nofollow` | `bouw.py`, functie `kop()` | weghalen bij livegang |
| Voorbeeldbalk en voetregel | `bouw.py` | weghalen bij livegang |
| Formulieren gaan nergens heen | `bouwscript/script.py` | controle en bevestiging werken; er is nog geen ontvanger |

### Nog te bevestigen

| wat | opmerking |
| --- | --- |
| Instagram | het account uit de briefing is niet van dit bedrijf, zie hierboven |
| De score | 5,0 uit 31 op 8 september 2026. Dat getal loopt op, voor livegang opnieuw kijken |
| Het werkgebied | de reviews komen uit Driel, Apeldoorn, Kilder, Huissen en Westervoort. Er wordt dus verder gereden dan Zevenaar en Arnhem |
| Adres | alleen de plaats Zevenaar is bekend, er staat nergens een straat |
| Prijzen | bewust nergens genoemd, conform de briefing |
