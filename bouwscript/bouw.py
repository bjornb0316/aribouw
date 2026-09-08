# -*- coding: utf-8 -*-
"""Bouwstenen die beide varianten delen."""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
import stijl
import script as JS

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.abspath(os.path.join(HIER, ".."))

FONTS = ('<link rel="preconnect" href="https://api.fontshare.com" crossorigin>'
         '<link rel="stylesheet" href="https://api.fontshare.com/v2/css?'
         'f%5B%5D=supreme@700&f%5B%5D=synonym@400,500,700&display=swap">')

# Een vierkant dat diagonaal is doorgesneden: de snijlijn zelf. Hun echte
# logo is een huis met een verfroller, maar dat bestaat alleen als foto op
# Facebook. Dit staat er tot er een vectorbestand is.
MARK = ('<svg class="merk-mark" viewBox="0 0 28 28" aria-hidden="true" focusable="false">'
        '<rect class="m-inkt" x="0" y="0" width="28" height="28" rx="4" fill="#23262B"/>'
        '<path class="m-blauw" d="M0 28V4a4 4 0 0 1 4-4h24z" fill="#14508C"/>'
        '</svg>')

PIJL = ('<svg viewBox="0 0 14 9" fill="none" aria-hidden="true">'
        '<path d="M0 4.5h12M8.5 1L12 4.5 8.5 8" stroke="currentColor" stroke-width="1.4"/></svg>')


def paginas(variant):
    if variant == "grondlaag":
        return [("index.html", "Home"), ("diensten.html", "Diensten"),
                ("werk.html", "Werk"), ("over.html", "Over Aribouw"),
                ("offerte.html", "Offerte"), ("contact.html", "Contact")]
    return [("index.html", "Home"), ("diensten.html", "Diensten"),
            ("werk.html", "Werk"), ("werkgebied.html", "Werkgebied"),
            ("offerte.html", "Offerte"), ("contact.html", "Contact")]


def kop(variant, actief, titel, omschrijving, wa_bericht, extra="", kopklasse=""):
    nav = "\n".join('        <a href="%s"%s>%s</a>'
                    % (b, ' aria-current="page"' if b == actief else "", n)
                    for b, n in paginas(variant))
    nav_m = "\n".join('      <a href="%s">%s</a>' % (b, n) for b, n in paginas(variant))
    return """<!doctype html>
<html lang="nl">
<head>
<script>document.documentElement.className+=" js";</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>%(titel)s</title>
<meta name="description" content="%(omschrijving)s">
<meta property="og:title" content="%(titel)s">
<meta property="og:description" content="%(omschrijving)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#F6F4F0">
%(fonts)s
<link rel="stylesheet" href="assets/css/stijl.css">
%(extra)s
</head>
<body data-wa-bericht="%(wa)s">

<div class="voorstel">
  <div class="wrap">
    <span><b>Voorbeeldpagina.</b> Voorstel voor Aribouw, gemaakt door Bjorn van Capital BB. Dit is niet de offici&euml;le website.</span>
    <span><a href="https://wa.me/%(bjorn)s">Reageren via WhatsApp</a></span>
  </div>
</div>

<header class="kop%(kopklasse)s">
  <div class="wrap kop-in">
    <a class="merk" href="index.html">
      %(mark)s
      <span><b>ARIBOUW</b><small>Schilderen &middot; behangen</small></span>
    </a>
    <nav class="nav" aria-label="Hoofdmenu">
%(nav)s
    </nav>
    <div class="kop-rechts">
      <a class="kop-tel" href="tel:%(tellink)s">%(tel)s</a>
      <a class="knop knop--vol knop--klein" href="offerte.html">Offerte aanvragen</a>
    </div>
    <button class="menu-knop" aria-label="Menu openen" aria-expanded="false" aria-controls="menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="menu" id="menu" data-open="0">
  <div class="menu-top">
    <a class="merk" href="index.html">%(mark)s<span><b>ARIBOUW</b></span></a>
    <button class="menu-sluit" aria-label="Menu sluiten">&times;</button>
  </div>
  <nav aria-label="Menu">
%(nav_m)s
  </nav>
  <div class="knopgroep">
    <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
    <a class="knop knop--lijn" href="#" data-wa-pagina>WhatsApp</a>
  </div>
</div>

<main>
""" % dict(titel=titel, omschrijving=omschrijving, fonts=FONTS, extra=extra, nav=nav,
           nav_m=nav_m, wa=wa_bericht, bjorn=D.BJORN_WA, tel=D.TEL_TOON, tellink=D.TEL_LINK,
           mark=MARK, kopklasse=(" " + kopklasse) if kopklasse else "")


def voet(variant):
    links = "\n".join('        <a href="%s">%s</a>' % (b, n) for b, n in paginas(variant))
    gebied = "<br>".join(D.WERKGEBIED) + "<br>en omgeving"
    return """</main>

<footer class="voet">
  <div class="wrap">
    <div class="voet-in">
      <div>
        <span class="voet-merk">ARIBOUW</span>
        <p style="margin-top:.9rem;max-width:34ch">Schilderwerk, behang en kleine renovaties.
        Strak afgewerkt, netjes achtergelaten.</p>
        <p style="margin-top:.9rem">KvK %(kvk)s</p>
      </div>
      <div>
        <p class="voet-kop">Pagina&#39;s</p>
%(links)s
      </div>
      <div>
        <p class="voet-kop">Contact</p>
        <a href="tel:%(tellink)s">%(tel)s</a>
        <a href="#" data-wa-pagina>WhatsApp</a>
        <a href="mailto:%(mail)s">%(mail)s</a>
        <a href="%(werkspot)s">Werkspot-profiel</a>
      </div>
      <div>
        <p class="voet-kop">Werkgebied</p>
        <p>%(gebied)s</p>
      </div>
    </div>
    <div class="voet-onder">
      <span>%(plaats)s &nbsp;&middot;&nbsp; Werken op afspraak, op locatie</span>
      <span>Voorbeeldontwerp van Bjorn, Capital BB. <a href="https://wa.me/%(bjorn)s" style="display:inline;text-decoration:underline">Reageren</a></span>
    </div>
  </div>
</footer>

<nav class="balk" aria-label="Snelle acties">
  <a class="knop knop--vol" href="offerte.html">Offerte aanvragen</a>
  <a class="knop knop--lijn" href="#" data-wa-pagina>WhatsApp</a>
</nav>

<script src="assets/js/main.js"></script>
</body>
</html>
""" % dict(links=links, tel=D.TEL_TOON, tellink=D.TEL_LINK, mail=D.MAIL, kvk=D.KVK,
           werkspot=D.WERKSPOT, gebied=gebied, plaats=D.PLAATS, bjorn=D.BJORN_WA)


def snee(om=False, zand=False):
    k = "snee"
    if om:
        k += " snee--om"
    if zand:
        k += " snee--zand"
    return '  <div class="%s" aria-hidden="true"></div>\n' % k


def railkop(label, titel, onder="", intro=""):
    """De sectiekop op de linkerrail: aanduiding links, inhoud rechts."""
    h = '      <div class="rail-kop">\n        <span class="rail-naam">%s</span>\n' % label
    if onder:
        h += '        <p>%s</p>\n' % onder
    h += '      </div>\n      <div class="rail-in">\n'
    h += '        <h2 class="display">%s</h2>\n' % titel
    if intro:
        h += '        <p class="intro" style="margin-top:.9rem">%s</p>\n' % intro
    return h


def gebiedstrip():
    return """  <section class="gebied">
    <div class="wrap gebied-in">
      <span class="gebied-kop">Werkgebied</span>
%s      <span>en omgeving</span>
    </div>
  </section>
""" % "".join("      <span>%s</span>\n" % p for p in D.WERKGEBIED)


def kaarten(variant, hoeveel=4):
    h = '        <div class="kaarten op" data-stagger>\n'
    for slug, naam, kort, lang, beeld, punten in D.DIENSTEN[:hoeveel]:
        link = ("dienst-%s.html" % slug) if variant == "aflak" else "diensten.html"
        h += ('          <a class="kaart" href="%s"><span class="kaart-baan"></span>'
              '<span class="kaart-in"><h3 class="display">%s</h3><p>%s</p>'
              '<span class="meer">Wat dat inhoudt %s</span></span></a>\n'
              % (link, naam, kort, PIJL))
    return h + "        </div>\n"


# (beeld, titel, onder)
WERK = [
    ("pui-voetzorg.webp", "Pui van een praktijkruimte",
     "Voormalige garage, kozijnen en deur in antraciet"),
    ("deur-na-breed.webp", "Binnendeur opnieuw gelakt",
     "Van houtlook naar strak gebroken wit"),
    ("kozijn-buiten.webp", "Buitenkozijnen",
     "Houtwerk hersteld, daarna gegrond en afgelakt"),
    ("pui-detail.webp", "Detail van de pui",
     "Aansluiting tussen kozijn, glas en metselwerk"),
    ("vlak-detail.webp", "Vlak van een deur",
     "Geen strepen, geen stof in de lak"),
    ("wand-detail.webp", "Kozijndetail",
     "Strakke overgang tussen hout en muur"),
]


def werkraster(hoeveel=6):
    h = '        <div class="werk op" data-stagger>\n'
    for beeld, titel, onder in WERK[:hoeveel]:
        h += ('          <figure><img src="../assets/img/%s" width="1000" height="750" '
              'loading="lazy" alt="%s"><figcaption><h3>%s</h3><p>%s</p></figcaption></figure>\n'
              % (beeld, titel, titel, onder))
    return h + "        </div>\n"


def werkwijze(klasse=""):
    h = """  <section class="sectie%s">
    <div class="wrap rail">
""" % (" " + klasse if klasse else "")
    h += railkop("Werkwijze", "Het meeste werk zit in wat u later niet ziet",
                 "Vijf stappen", "Schuren, plamuren en aftapen kosten de meeste uren. Precies "
                 "daar zit het verschil tussen twee jaar mooi en tien jaar mooi.")
    h += '        <div class="stappen op" data-stagger>\n'
    for nr, titel, tekst in D.STAPPEN:
        h += ('          <div class="stap"><b>%s</b><h3>%s</h3><p>%s</p></div>\n'
              % (nr, titel, tekst))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"
    return h


def reviews(hoeveel=4, klasse=""):
    h = '        <div class="reviews op" data-stagger>\n'
    for tekst, wie, wat in D.REVIEWS[:hoeveel]:
        h += ('          <blockquote class="review"><p>%s</p>'
              '<div class="review-onder"><b>%s</b><span>%s</span></div></blockquote>\n'
              % (tekst, wie, wat))
    return h + "        </div>\n"


def scoreblok():
    return ('        <p class="score op" style="margin-top:1.6rem"><b>%s</b> '
            '<span>uit %s reviews op Werkspot, stand %s</span></p>\n'
            % (D.SCORE, D.AANTAL_REVIEWS, D.SCORE_DATUM))


def vragen(lijst, kop_id="vragen"):
    h = '        <div class="vragen op" id="%s">\n' % kop_id
    for v, a in lijst:
        a = (a.replace("[NOG AANVULLEN: garantietermijnen]",
                       '<span class="markering">Nog aanvullen: garantietermijnen</span>')
              .replace("[NOG AANVULLEN: gebruikelijke doorlooptijden]",
                       '<span class="markering">Nog aanvullen: doorlooptijden</span>'))
        h += ('          <div class="vraag" data-open="0">\n'
              '            <button type="button" aria-expanded="false">'
              '<span>%s</span><span class="vraag-teken" aria-hidden="true"></span></button>\n'
              '            <div class="vraag-antwoord"><p>%s</p></div>\n'
              '          </div>\n' % (v, a))
    return h + "        </div>\n"


def contactblok(titel, intro, onderwerpen=None):
    keuzes = onderwerpen or ["Binnenschilderwerk", "Buitenschilderwerk", "Behang",
                             "Kleine renovatie", "Meerdere dingen tegelijk"]
    opties = ('              <option value="" disabled selected>Maak een keuze</option>\n' +
              "\n".join('              <option>%s</option>' % k for k in keuzes))
    return """
  <section class="sectie sectie--nacht" id="contact">
    <div class="wrap">
      <div class="sectie-kop op">
        <h2 class="display">%(titel)s</h2>
        <p class="intro">%(intro)s</p>
      </div>
      <div class="contact">
        <div>
          <form class="op" data-formulier novalidate>
            <div class="velden-2">
              <div class="veld">
                <label for="naam">Uw naam</label>
                <input id="naam" name="naam" type="text" autocomplete="name" required>
                <span class="fout">Vul uw naam in.</span>
              </div>
              <div class="veld">
                <label for="tel">Telefoonnummer</label>
                <input id="tel" name="tel" type="tel" autocomplete="tel" required>
                <span class="hulp">Bellen gaat meestal het snelst.</span>
                <span class="fout">Vul een telefoonnummer in.</span>
              </div>
            </div>
            <div class="velden-2">
              <div class="veld">
                <label for="plaats">Plaats</label>
                <input id="plaats" name="plaats" type="text" autocomplete="address-level2" required>
                <span class="fout">Vul uw plaats in.</span>
              </div>
              <div class="veld">
                <label for="wat">Waar gaat het over</label>
                <select id="wat" name="wat" required>
%(opties)s
                </select>
                <span class="fout">Kies waar het over gaat.</span>
              </div>
            </div>
            <div class="veld">
              <label for="bericht">Uw situatie</label>
              <textarea id="bericht" name="bericht" rows="4" placeholder="Bijvoorbeeld: woonkamer en gang schilderen, muren zijn nu behangen, plafond mag mee."></textarea>
              <span class="hulp">Niet verplicht. Hoe meer u kwijt wilt, hoe gerichter het antwoord.</span>
            </div>
            <button class="knop knop--vol" type="submit">Offerte aanvragen</button>
            <p class="formulier-noot">Vrijblijvend. Er wordt eerst gekeken en pas daarna komt er
            een prijs. Foto&#39;s stuurt u het makkelijkst via WhatsApp.</p>
          </form>
          <div class="gelukt op" data-gelukt role="status">
            <b>Aanvraag genoteerd.</b>
            <p>U wordt gebeld om een moment af te spreken. Stuur gerust alvast een paar foto&#39;s
            van de ruimte, dan kan er meteen worden meegedacht. In deze voorbeeldpagina gaat er
            nog niets echt de deur uit.</p>
            <div class="knopgroep" style="margin-top:1.1rem">
              <a class="knop knop--lijn knop--klein" href="#" data-wa-pagina>Foto&#39;s sturen</a>
            </div>
          </div>
        </div>
        <div class="op">
          <h3 class="display" style="color:#fff">Liever meteen contact</h3>
          <p style="margin-bottom:1.2rem;color:var(--licht-2)">Bellen of appen kan altijd. Een paar
          foto&#39;s van de ruimte zeggen vaak al genoeg om te weten waar het over gaat.</p>
          <dl>
            <div class="contactrij"><dt>Telefoon</dt><dd><a href="tel:%(tellink)s">%(tel)s</a></dd></div>
            <div class="contactrij"><dt>WhatsApp</dt><dd><a href="#" data-wa-pagina>%(tel)s</a></dd></div>
            <div class="contactrij"><dt>E-mail</dt><dd><a href="mailto:%(mail)s">%(mail)s</a></dd></div>
            <div class="contactrij"><dt>Werkgebied</dt><dd>%(plaats)s en omgeving</dd></div>
            <div class="contactrij"><dt>Reviews</dt><dd><a href="%(werkspot)s">%(score)s op Werkspot</a></dd></div>
          </dl>
          <div class="knopgroep" style="margin-top:1.4rem">
            <a class="knop knop--vol knop--klein" href="tel:%(tellink)s">Bellen</a>
            <a class="knop knop--lijn knop--klein" href="#" data-wa-pagina>WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""" % dict(titel=titel, intro=intro, opties=opties, tel=D.TEL_TOON, tellink=D.TEL_LINK,
           mail=D.MAIL, plaats=D.PLAATS, werkspot=D.WERKSPOT, score=D.SCORE)


def stijlbladen():
    for variant in ("grondlaag", "aflak"):
        for soort, inhoud, naam in (("css", stijl.blad(variant), "stijl.css"),
                                    ("js", JS.blad(variant, D.WA), "main.js")):
            map_ = os.path.join(WORTEL, "variant-" + variant, "assets", soort)
            os.makedirs(map_, exist_ok=True)
            io.open(os.path.join(map_, naam), "w", encoding="utf-8").write(inhoud)


def schrijf(variant, naam, inhoud):
    map_ = os.path.join(WORTEL, "variant-" + variant)
    os.makedirs(map_, exist_ok=True)
    io.open(os.path.join(map_, naam), "w", encoding="utf-8").write(inhoud)
