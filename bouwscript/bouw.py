# -*- coding: utf-8 -*-
"""Bouwstenen die beide varianten delen."""
import hashlib, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
import stijl
import script as JS

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.abspath(os.path.join(HIER, ".."))

FONTS = ('<link rel="preconnect" href="https://api.fontshare.com" crossorigin>'
         '<link rel="stylesheet" href="https://api.fontshare.com/v2/css?'
         'f%5B%5D=supreme@700&f%5B%5D=synonym@400,500,700&display=swap">')

# Het logo van Ahmad: huis en ARIBOUW naast elkaar. Gemaakt door logo.py uit
# bron/logo-aribouw.jpg. De witte variant staat in de donkere voet.
LOGO = ('<img class="merk-logo" src="assets/img/logo-kop.png" width="471" height="120" '
        'alt="Aribouw, schilderen en behangen">')
LOGO_WIT = ('<img class="merk-logo merk-logo--voet" src="assets/img/logo-kop-wit.png" '
            'width="471" height="120" alt="Aribouw" loading="lazy">')

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
    # De voorbeeldbalk en noindex staan er zolang LIVE uit staat. De eigen
    # URL van de pagina kent kop() niet (dienstpagina's geven "diensten.html"
    # mee voor het menu), dus die vult schrijf() in op __PAGINA__.
    robots = "" if D.LIVE else '<meta name="robots" content="noindex,nofollow">\n'
    balk = "" if D.LIVE else """<div class="voorstel">
  <div class="wrap">
    <span><b>Voorbeeldpagina.</b> Voorstel voor Aribouw, gemaakt door Bjorn van Capital BB. Dit is niet de offici&euml;le website.</span>
    <span><a href="https://wa.me/%s">Reageren via WhatsApp</a></span>
  </div>
</div>
""" % D.BJORN_WA
    return """<!doctype html>
<html lang="nl">
<head>
<script>document.documentElement.className+=" js";</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(robots)s<title>%(titel)s</title>
<meta name="description" content="%(omschrijving)s">
<link rel="canonical" href="%(site)s/__PAGINA__">
<meta property="og:title" content="%(titel)s">
<meta property="og:description" content="%(omschrijving)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="Aribouw">
<meta property="og:url" content="%(site)s/__PAGINA__">
<meta property="og:image" content="%(site)s/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F6F4F0">
<link rel="icon" href="assets/favicon-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
%(fonts)s
<link rel="stylesheet" href="assets/css/stijl.css">
%(extra)s
</head>
<body data-wa-bericht="%(wa)s">

%(balk)s
<header class="kop%(kopklasse)s">
  <div class="wrap kop-in">
    <a class="merk" href="index.html">%(mark)s</a>
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
    <a class="merk" href="index.html">%(mark)s</a>
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
           nav_m=nav_m, wa=wa_bericht, tel=D.TEL_TOON, tellink=D.TEL_LINK,
           mark=LOGO, kopklasse=(" " + kopklasse) if kopklasse else "",
           robots=robots, balk=balk, site=D.SITE_URL[variant])


def voet(variant):
    links = "\n".join('        <a href="%s">%s</a>' % (b, n) for b, n in paginas(variant))
    gebied = (", ".join(D.WERKGEBIED_ALLES[:-1]) + " en " + D.WERKGEBIED_ALLES[-1] + ". " +
              D.BUITEN_REGIO)
    return """</main>

<footer class="voet">
  <div class="wrap">
    <div class="voet-in">
      <div>
        <span class="voet-merk">%(logo_wit)s</span>
        <p style="margin-top:.9rem;max-width:34ch">Schilderwerk, behang en houtreparaties.
        Strak afgewerkt, netjes achtergelaten.</p>
        <p style="margin-top:.9rem">%(eigenaar)s<br>%(adres)s<br>%(postcode)s %(plaats)s</p>
        <p style="margin-top:.9rem">KvK %(kvk)s<br>Btw %(btw)s</p>
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
        <p style="max-width:30ch">%(gebied)s</p>
      </div>
    </div>
    <div class="voet-onder">
      <span>Schildersbedrijf uit %(plaats)s. Werken op afspraak, op locatie.</span>
      <span><a class="voet-inline" href="privacy.html">Privacyverklaring</a>%(ontwerp)s</span>
    </div>
  </div>
</footer>

<nav class="balk" aria-label="Snelle acties">
  <a class="knop knop--lijn" href="tel:%(tellink)s">Bellen</a>
  <a class="knop knop--lijn" href="#" data-wa-pagina>WhatsApp</a>
  <a class="knop knop--vol" href="offerte.html">Offerte</a>
</nav>

<script src="assets/js/main.js"></script>
</body>
</html>
""" % dict(links=links, tel=D.TEL_TOON, tellink=D.TEL_LINK, mail=D.MAIL, kvk=D.KVK,
           werkspot=D.WERKSPOT, gebied=gebied, plaats=D.PLAATS, logo_wit=LOGO_WIT,
           eigenaar=D.EIGENAAR, adres=D.ADRES, postcode=D.POSTCODE, btw=D.BTW,
           ontwerp=' &nbsp;&middot;&nbsp; Website door Jezz-Media' if D.LIVE else (
               ' &nbsp;&middot;&nbsp; Voorbeeldontwerp van Bjorn, Capital BB. <a class="voet-inline" '
               'href="https://wa.me/%s">Reageren</a>' % D.BJORN_WA))


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


def vertrouwen():
    """Direct onder de hero: vier dingen die binnen vijf seconden duidelijk
    moeten zijn. Alleen wat aantoonbaar klopt, geen verzonnen keurmerken."""
    punten = [
        ('<span class="sterren" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
         '<b>%s uit %s reviews</b>' % (D.SCORE, D.AANTAL_REVIEWS),
         '<a href="%s">Openbaar op Werkspot</a>' % D.WERKSPOT),
        ("<b>Eigen werk op de site</b>", '<a href="werk.html">Voor en na bekijken</a>'),
        ("<b>Vrijblijvend langskomen</b>", "Eerst kijken, dan pas een prijs"),
        ("<b>Gevestigd in %s</b>" % D.PLAATS, '<a href="werkgebied.html">Twaalf plaatsen in de regio</a>'),
    ]
    h = '  <section class="vertrouwen" aria-label="Waarom Aribouw">\n    <div class="wrap">\n'
    h += '      <ul class="vertrouwen-in op" data-stagger>\n'
    for boven, onder in punten:
        h += '        <li>%s<span>%s</span></li>\n' % (boven, onder)
    return h + "      </ul>\n    </div>\n  </section>\n"


def ctaregel(tekst, knoppen):
    """Een CTA die past bij wat de bezoeker net heeft gezien. knoppen is een
    lijst van (label, href, "vol" of "lijn")."""
    h = '        <div class="ctaregel op">\n          <p>%s</p>\n          <div class="knopgroep">\n' % tekst
    for label, href, soort in knoppen:
        h += '            <a class="knop knop--%s" href="%s">%s</a>\n' % (soort, href, label)
    return h + "          </div>\n        </div>\n"


def gebiedstrip():
    return """  <section class="gebied">
    <div class="wrap gebied-in">
      <span class="gebied-kop">Werkgebied</span>
%s      <span>en omgeving</span>
    </div>
  </section>
""" % "".join("      <span>%s</span>\n" % p for p in D.WERKGEBIED_ALLES[:8])


# Aflak: welke Higgsfield-film bij welke dienst hoort. Zie film.py.
# De naam van een film is ook zijn adres. Vervang je een film door een
# betere versie onder dezelfde naam, dan houden browsers de oude nog
# uren vast. Daarom krijgt een vervangen film een nieuw nummer.
DIENST_FILM = {"binnenschilderwerk": "binnen-2", "buitenschilderwerk": "buiten",
               "behang": "behang", "houtwerk": "houtwerk",
               # Specialismen met een eigen film.
               "kozijnen-deuren": "deuren", "wanden-plafonds": "wanden"}
# Een beeld in de kop als een dienst (nog) geen film heeft.
DIENST_BEELD = {}


def werkzaamheden(variant, klasse=""):
    """Alles wat Ahmad in de intake opgaf, letterlijk, in een oogopslag.
    In Aflak linkt elke regel naar de pagina die erover gaat."""
    h = '        <div class="werkzaamheden op%s">\n' % ((" " + klasse) if klasse else "")
    h += '          <h3>Alle werkzaamheden</h3>\n          <ul>\n'
    for naam, href in D.WERKZAAMHEDEN:
        if variant == "aflak":
            h += '            <li><a href="%s">%s %s</a></li>\n' % (href, naam, PIJL)
        else:
            h += '            <li>%s</li>\n' % naam
    h += '          </ul>\n          <p>Geen stucwerk of egaliseren: Aribouw is een schilder.</p>\n'
    return h + "        </div>\n"


def film(naam, gedrag="lus", klasse="film"):
    """Een stille film met poster. De bron staat in data-src en wordt pas
    geladen als hij in beeld komt (of bij hover). Zonder JS of met minder
    beweging blijft de poster staan. Decoratief, dus aria-hidden."""
    return ('<div class="%s" aria-hidden="true"><video muted playsinline preload="none"%s '
            'poster="assets/film/%s.webp" data-film="%s">'
            '<source data-src="assets/film/%s.mp4" type="video/mp4"></video></div>'
            % (klasse, "" if gedrag == "eenmaal" else " loop", naam, gedrag, naam))


def filmhero(tekst, filmnaam=None, beeld=None, alt="", klasse=""):
    """Aflak: kop over een film of een beeld over de volle breedte."""
    if filmnaam:
        media = film(filmnaam, "eenmaal" if filmnaam == "snijlijn" else "lus", "film film--hero")
    else:
        media = ('<div class="film film--hero"><img src="assets/img/%s" width="1920" '
                 'height="1080" fetchpriority="high" alt="%s"></div>' % (beeld, alt))
    return """
  <section class="hero--film%s">
    %s
    <div class="wrap">
%s    </div>
  </section>
""" % ((" " + klasse) if klasse else "", media, tekst)


def kaart(variant, dienst, meer="Wat dat inhoudt", link=None):
    slug, naam, kort = dienst[0], dienst[1], dienst[2]
    if link is None:
        link = ("dienst-%s.html" % slug) if variant == "aflak" else "diensten.html"
    if variant == "aflak":
        kopje = ('<span class="kaart-media">%s</span><span class="kaart-baan"></span>'
                 % film(DIENST_FILM[slug], "hover", "kaart-film"))
    else:
        kopje = '<span class="kaart-baan"></span>'
    return ('          <a class="kaart" href="%s">%s'
            '<span class="kaart-in"><h3 class="display">%s</h3><p>%s</p>'
            '<span class="meer">%s %s</span></span></a>\n'
            % (link, kopje, naam, kort, meer, PIJL))


def kaarten(variant, hoeveel=4, lijst=None):
    lijst = lijst if lijst is not None else D.DIENSTEN[:hoeveel]
    h = '        <div class="kaarten%s op" data-stagger>\n' % (" kaarten--drie" if len(lijst) == 3 else "")
    for dienst in lijst:
        h += kaart(variant, dienst)
    return h + "        </div>\n"


# Voor-en-na paren van eigen klussen. Nieuwe paren van Ahmad hier
# toevoegen; de werkpagina van Aflak maakt voor elk paar een schuif.
# (voor, na, titel, onder, alt voor, alt na)
VOORNA = [
    ("deur-voor-breed.webp", "deur-na-breed.webp",
     "Een binnendeur in een kantoorpand", "Van houtlook naar gebroken wit",
     "Binnendeur met houtlook voor het schilderen",
     "Dezelfde deur na het schilderen in gebroken wit"),
]

# Eigen projectfoto's. (beeld, titel, onder)
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
    # data-blok: hier komen de projecten die Ahmad toevoegt bovenaan te staan.
    h = '        <div class="werk op" data-stagger data-blok="werk">\n'
    for beeld, titel, onder in WERK[:hoeveel]:
        h += ('          <figure><img src="assets/img/%s" width="1000" height="750" '
              'loading="lazy" alt="%s"><figcaption><h3>%s</h3><p>%s</p></figcaption></figure>\n'
              % (beeld, titel, titel, onder))
    return h + "        </div>\n"


# Aflak: een beeld per stap. Gegenereerde procesbeelden, geen eigen klussen.
STAP_BEELDEN = [
    ("stap-fotos.webp", "Iemand maakt met een telefoon een foto van een scheur in de muur"),
    ("stap-opname.webp", "Vochtmeting onderaan een houten kozijn"),
    ("stap-offerte.webp", "Keukentafel met een kleurwaaier en een offerte"),
    ("stap-uitvoeren.webp", "Kamer afgedekt en afgeplakt voor het schilderen"),
    ("stap-opgeleverd.webp", "Opgeruimde, net geschilderde woonkamer in middaglicht"),
]


def werkwijze(klasse="", beelden=False):
    h = """  <section class="sectie%s">
    <div class="wrap rail">
""" % (" " + klasse if klasse else "")
    h += railkop("Werkwijze", "Het meeste werk zit in wat u later niet ziet",
                 "Vijf stappen", "Goed schilderwerk begint bij een goede ondergrond. Schuren, "
                 "gaatjes dichtzetten en afplakken kosten de meeste uren, en precies daar zit het "
                 "verschil tussen twee jaar mooi en tien jaar mooi.")
    h += '        <div class="stappen%s op" data-stagger>\n' % (" stappen--beeld" if beelden else "")
    for i, (nr, titel, tekst) in enumerate(D.STAPPEN):
        beeld = ""
        if beelden:
            b, alt = STAP_BEELDEN[i]
            beeld = ('<img class="stap-beeld" src="assets/img/%s" width="1000" height="750" '
                     'loading="lazy" alt="%s">' % (b, alt))
        h += ('          <div class="stap">%s<b>%s</b><h3>%s</h3><p>%s</p></div>\n'
              % (beeld, nr, titel, tekst))
    h += "        </div>\n      </div>\n    </div>\n  </section>\n"
    return h


def reviews(hoeveel=4, klasse="", indexen=None):
    lijst = [D.REVIEWS[i] for i in indexen] if indexen is not None else D.REVIEWS[:hoeveel]
    # data-blok: hier zet het beheerscherm de reviews in die Ahmad toevoegt.
    h = ('        <div class="reviews%s op" data-stagger data-blok="reviews">\n'
         % (" reviews--een" if len(lijst) == 1 else ""))
    for tekst, wie, wat in lijst:
        h += ('          <blockquote class="review"><p>%s</p>'
              '<div class="review-onder"><b>%s</b><span>%s</span></div></blockquote>\n'
              % (tekst, wie, wat))
    return h + "        </div>\n"


def scoreblok():
    return ('        <p class="score op" style="margin-top:1.6rem"><b>%s</b> '
            '<span>uit %s reviews op Werkspot, stand %s</span></p>\n'
            % (D.SCORE, D.AANTAL_REVIEWS, D.SCORE_DATUM))


def markeer(tekst):
    """[NOG AANVULLEN: iets] wordt een zichtbare markering op de pagina."""
    import re
    return re.sub(r"\[NOG AANVULLEN: ([^\]]+)\]",
                  lambda m: '<span class="markering">Nog aanvullen: %s</span>' % m.group(1), tekst)


# ---- formulieren ----
# Een verborgen veld dat mensen niet zien en spambots wel invullen.
HONING = ('<div class="honing" aria-hidden="true"><label for="%s">Laat dit veld leeg</label>'
          '<input id="%s" name="_honey" type="text" tabindex="-1" autocomplete="off"></div>')


def verzendfout():
    """Als versturen mislukt, is er altijd nog bellen of appen."""
    return ('<p class="verzendfout" data-verzendfout role="alert">Versturen lukte niet. Bel of app '
            'mij op <a href="tel:%s">%s</a>, dan kijk ik er meteen naar.</p>'
            % (D.TEL_LINK, D.TEL_TOON))


def demozin():
    """Zolang er geen ontvanger is ingesteld, zegt de bevestiging dat eerlijk."""
    return "" if D.FORMULIER_ACTIE else " In deze voorbeeldpagina gaat er nog niets echt de deur uit."


def vragen(lijst, kop_id="vragen"):
    h = '        <div class="vragen op" id="%s">\n' % kop_id
    for v, a in lijst:
        a = markeer(a.replace("[NOG AANVULLEN: gebruikelijke doorlooptijden]",
                              "[NOG AANVULLEN: doorlooptijden]"))
        h += ('          <div class="vraag" data-open="0">\n'
              '            <button type="button" aria-expanded="false">'
              '<span>%s</span><span class="vraag-teken" aria-hidden="true"></span></button>\n'
              '            <div class="vraag-antwoord"><p>%s</p></div>\n'
              '          </div>\n' % (v, a))
    return h + "        </div>\n"


def contactblok(titel, intro, onderwerpen=None, variant=None):
    keuzes = onderwerpen or ["Binnenschilderwerk", "Buitenschilderwerk", "Behangen",
                             "Houtreparatie of onderhoud", "Meerdere dingen tegelijk",
                             "Project voor aannemer of architect"]
    opties = ('              <option value="" disabled selected>Maak een keuze</option>\n' +
              "\n".join('              <option>%s</option>' % k for k in keuzes))
    # Aflak: het contactblok opent met een woning in de schemer, die in het
    # donker van de sectie overloopt.
    extra, filmpje = "", ""
    if variant == "aflak":
        extra = " sectie--film"
        filmpje = "    " + film("schemer", "lus", "film film--contact") + "\n"
    return """
  <section class="sectie sectie--nacht%(extra)s" id="contact">
%(filmpje)s    <div class="wrap">
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
            %(honing)s
            <button class="knop knop--vol" type="submit">Offerte aanvragen</button>
            %(verzendfout)s
            <p class="formulier-noot">Vrijblijvend. Ik kom eerst kijken, daarna pas een prijs.
            Foto&#39;s stuurt u het makkelijkst via WhatsApp. Wat ik met uw gegevens doe, staat in
            de <a href="privacy.html">privacyverklaring</a>.</p>
          </form>
          <div class="gelukt op" data-gelukt role="status">
            <b>Aanvraag verstuurd.</b>
            <p>Ik bel u om een moment af te spreken. Stuur gerust alvast een paar foto&#39;s van de
            ruimte, dan kan ik meteen meedenken.%(demozin)s</p>
            <div class="knopgroep" style="margin-top:1.1rem">
              <a class="knop knop--lijn knop--klein" href="#" data-wa-pagina>Foto&#39;s sturen</a>
            </div>
          </div>
        </div>
        <div class="op">
          <h3 class="display" style="color:#fff">Liever meteen contact</h3>
          <p style="margin-bottom:1.2rem;color:var(--licht-2)">Bel of app mij gerust. Een paar
          foto&#39;s van de ruimte zeggen vaak al genoeg om te weten waar het over gaat.</p>
          <dl>
            <div class="contactrij"><dt>Telefoon</dt><dd><a href="tel:%(tellink)s">%(tel)s</a></dd></div>
            <div class="contactrij"><dt>WhatsApp</dt><dd><a href="#" data-wa-pagina>%(tel)s</a></dd></div>
            <div class="contactrij"><dt>E-mail</dt><dd><a href="mailto:%(mail)s">%(mail)s</a></dd></div>
            <div class="contactrij"><dt>Adres</dt><dd>%(adres)s, %(postcode)s %(plaats)s</dd></div>
            <div class="contactrij"><dt>Werkgebied</dt><dd>%(plaats)s, Arnhem, Nijmegen en omgeving</dd></div>
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
           mail=D.MAIL, plaats=D.PLAATS, werkspot=D.WERKSPOT, score=D.SCORE,
           extra=extra, filmpje=filmpje, adres=D.ADRES, postcode=D.POSTCODE,
           honing=HONING % ("honing-contact", "honing-contact"), verzendfout=verzendfout(),
           demozin=demozin())


def stijlbladen():
    import shutil
    for variant in ("aflak",):
        for soort, inhoud, naam in (("css", stijl.blad(variant), "stijl.css"),
                                    ("js", JS.blad(variant, D.WA, D.FORMULIER_ACTIE), "main.js")):
            map_ = os.path.join(WORTEL, "assets", soort)
            os.makedirs(map_, exist_ok=True)
            io.open(os.path.join(map_, naam), "w", encoding="utf-8").write(inhoud)
        assets = os.path.join(WORTEL, "assets")
        # Favicons uit het logo (logo.py). Ze moeten naast de pagina staan:
        # browsers zoeken ze relatief aan de site.
        img = os.path.join(WORTEL, "assets", "img")
        for f, doel in (("favicon-32.png", "favicon-32.png"), ("favicon-48.png", "favicon-48.png"),
                        ("apple-touch-icon.png", "apple-touch-icon.png"),
                        ("logo-aribouw.png", "logo.png")):
            if os.path.exists(os.path.join(img, f)):
                shutil.copyfile(os.path.join(img, f), os.path.join(assets, doel))
        oud = os.path.join(assets, "favicon.svg")
        if os.path.exists(oud):
            os.remove(oud)
        # De deelafbeelding voor WhatsApp, Facebook en LinkedIn. Gemaakt
        # door film.py; hier alleen naar de variant gekopieerd.
        og = os.path.join(WORTEL, "assets", "img", "og-aribouw.jpg")
        if os.path.exists(og):
            shutil.copyfile(og, os.path.join(assets, "og.jpg"))


# ---------------------------------------------------------------------
# Bewerkbare teksten
# ---------------------------------------------------------------------
# Elke losse zin krijgt een label, zodat het beheerscherm hem kan
# vervangen. Het label is een hash van de oorspronkelijke tekst: staat
# dezelfde zin op meerdere pagina's (zoals het contactblok), dan hoeft
# Ahmad hem maar een keer aan te passen. Verandert de tekst in het
# bouwscript, dan vervalt de aanpassing en staat de nieuwe tekst er weer:
# dat is veiliger dan een aanpassing op de verkeerde plek plakken.
BEWERKBAAR = re.compile(r"<(h1|h2|h3|h4|p|li|small|span|b|a)(\s[^>]*)?>([^<>]{3,}?)</\1>")
TEKSTEN = {}


def labels(inhoud, naam):
    def vervang(m):
        tag, attrs, tekst = m.group(1), m.group(2) or "", m.group(3)
        if "data-tekst" in attrs or not tekst.strip():
            return m.group(0)
        sleutel = hashlib.sha1(tekst.strip().encode("utf-8")).hexdigest()[:10]
        regel = TEKSTEN.setdefault(sleutel, {"tekst": tekst.strip(), "paginas": []})
        if naam not in regel["paginas"]:
            regel["paginas"].append(naam)
        return '<%s%s data-tekst="%s">%s</%s>' % (tag, attrs, sleutel, tekst, tag)
    return BEWERKBAAR.sub(vervang, inhoud)


def tekstenlijst():
    """assets/teksten.json: wat het beheerscherm laat zien om te bewerken."""
    import json
    pad = os.path.join(WORTEL, "assets", "teksten.json")
    io.open(pad, "w", encoding="utf-8").write(
        json.dumps(TEKSTEN, ensure_ascii=False, indent=1, sort_keys=True))
    return len(TEKSTEN)


def kortelinks(inhoud):
    """Cloudflare serveert diensten.html op /diensten en stuurt .html door.
    Daarom staan de links meteen zonder .html: scheelt bij elke klik een
    omleiding. De bestanden zelf houden gewoon hun .html-naam."""
    inhoud = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: 'href="/%s"' % (m.group(1) or ""),
                    inhoud)
    return re.sub(r'href="([a-z0-9\-]+)\.html(#[^"]*)?"',
                  lambda m: 'href="%s%s"' % (m.group(1), m.group(2) or ""), inhoud)


def schrijf(variant, naam, inhoud):
    map_ = WORTEL
    os.makedirs(map_, exist_ok=True)
    kort = "" if naam == "index.html" else naam[:-5] if naam.endswith(".html") else naam
    inhoud = kortelinks(inhoud).replace("__PAGINA__", kort)
    if naam != "beheer.html":
        inhoud = labels(inhoud, naam)
    if naam != "index.html":
        inhoud = inhoud.replace("</head>", kruimels(variant, naam, inhoud) + "\n</head>", 1)
    io.open(os.path.join(map_, naam), "w", encoding="utf-8").write(inhoud)


def kruimels(variant, naam, inhoud):
    """BreadcrumbList voor elke subpagina. De naam komt uit de h1 van de
    pagina zelf; dienst- en plaatspagina's hangen onder hun overzicht."""
    import json, re, html
    site = D.SITE_URL[variant]
    m = re.search(r"<h1[^>]*>(.*?)</h1>", inhoud, re.S)
    titel = html.unescape(re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip()) if m else naam
    titel = re.sub(r"\s+", " ", titel)
    pad = [("Home", site + "/")]
    if naam.startswith("dienst-"):
        pad.append(("Diensten", site + "/diensten.html"))
    elif naam.startswith("regio-"):
        pad.append(("Werkgebied", site + "/werkgebied.html"))
    pad.append((titel, "%s/%s" % (site, naam)))
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(pad)]}
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)


def zoekbestanden(variant, namen):
    """sitemap.xml en robots.txt. Zolang LIVE uit staat, blokkeert robots.txt
    alles; de pagina's hebben dan ook noindex."""
    import datetime
    site = D.SITE_URL[variant]
    vandaag = datetime.date.today().isoformat()
    regels = []
    for n in namen:
        pad = "" if n == "index.html" else (n[:-5] if n.endswith(".html") else n)
        prio = "1.0" if n == "index.html" else ("0.3" if n == "privacy.html" else "0.7")
        regels.append("  <url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
                      % (site, pad, vandaag, prio))
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
               % "\n".join(regels))
    if D.LIVE:
        robots = "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % site
    else:
        robots = "# Demo: niet indexeren. Bij livegang LIVE = True in bouwscript/data.py.\nUser-agent: *\nDisallow: /\n"
    map_ = WORTEL
    io.open(os.path.join(map_, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)
    io.open(os.path.join(map_, "robots.txt"), "w", encoding="utf-8").write(robots)
