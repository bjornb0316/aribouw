# -*- coding: utf-8 -*-
"""Snijdt het beschikbare materiaal tot bruikbare beelden.

Er is weinig, en dat bepaalt het ontwerp. Vier bruikbare foto's, dus geen
site die om een fotogalerij heen is gebouwd, maar een die om kleurvlakken
en typografie heen is gebouwd, met die vier foto's als de momenten.

Elke foto is bekeken. Wat er bewust niet in zit:
  - de tuin met de schommel, voor en na. Mooi werk, maar dat is grondwerk,
    en de briefing zegt juist: geen algemeen klusbedrijf
  - de gangkast met jassen erin, een rommelig "before" zonder tegenhanger
  - de twee logo-afbeeldingen; die zijn geen projectfoto

De voor-en-na van de deur is een echt paar, maar niet vanaf hetzelfde punt
geschoten en met "Before" en "After" in het beeld gebrand. Door beide tot
alleen het deurvlak te snijden vallen die labels weg en komt de deur bij
allebei even groot in beeld. Dan klopt de schuif wel.

Draaien vanuit de projectmap:  python bouwscript/beelden.py
"""
import io, os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.abspath(os.path.join(HIER, ".."))
BRON = os.path.join(WORTEL, "bron")
UIT = os.path.join(WORTEL, "assets", "img")
GRENS = 205000

# (bron, uitsnede in pixels of None, doel, verhouding, breedte, fx, fy, wat)
TAKEN = [
    # Het paar voor de hero. Liggend en met de omgeving erbij, anders is
    # het op schermbreedte alleen nog een bruin vlak en herken je de deur
    # niet meer. De onderste 30 procent blijft eruit; daar staat het
    # ingebrande "Before" en "After".
    ("fb-03.jpg", (0, 150, 1536, 1014), "deur-voor.webp", 16 / 9.0, 1500, .5, .5,
     "houten deur met kozijn en raam, voor het schilderen"),
    ("fb-04.jpg", (0, 110, 1536, 974), "deur-na.webp", 16 / 9.0, 1500, .5, .5,
     "dezelfde deur na het schilderen"),
    # Dezelfde twee, liggend, voor de projectenpagina.
    ("fb-03.jpg", (455, 110, 1170, 760), "deur-voor-breed.webp", 4 / 3.0, 1100, .5, .5,
     "houten deur voor het schilderen"),
    ("fb-04.jpg", (395, 70, 1050, 660), "deur-na-breed.webp", 4 / 3.0, 1100, .5, .5,
     "dezelfde deur na het schilderen"),
    # De pui van een praktijkruimte. Scherp, en er hoort een review bij.
    ("ws-pui.jpg", None, "pui-voetzorg.webp", 16 / 10.0, 1600, .5, .55,
     "geschilderde pui en deur van een praktijkruimte"),
    ("ws-pui.jpg", (1800, 900, 4400, 3400), "pui-detail.webp", 4 / 3.0, 1200, .5, .5,
     "detail van de geschilderde pui"),
    # Buitenkozijnen, wit, scherp.
    ("fb-09.jpg", None, "kozijn-buiten.webp", 4 / 3.0, 1200, .5, .5,
     "wit geschilderde buitenkozijnen"),
    ("fb-09.jpg", (300, 250, 1150, 1100), "wand-detail.webp", 1 / 1.0, 900, .5, .5,
     "detail van een strak afgewerkt kozijn"),
    # Een gladde geschilderde deur, van dichtbij.
    ("fb-07.jpg", (0, 0, 900, 760), "vlak-detail.webp", 16 / 10.0, 1100, .5, .45,
     "vlak van een geschilderde deur"),
]


def snij_verhouding(im, verh, fx, fy):
    if verh is None:
        return im
    b, h = im.size
    doel_h = b / verh
    if doel_h <= h:
        top = int((h - doel_h) * fy)
        return im.crop((0, top, b, int(top + doel_h)))
    doel_b = h * verh
    links = int((b - doel_b) * fx)
    return im.crop((links, 0, int(links + doel_b), h))


def schrijf(im, pad):
    for q in (84, 80, 76, 72, 66):
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() <= GRENS or q == 66:
            with open(pad, "wb") as f:
                f.write(buf.getvalue())
            return q, buf.tell()


def main():
    os.makedirs(UIT, exist_ok=True)
    for bron, doos, doel, verh, breedte, fx, fy, wat in TAKEN:
        bp = os.path.join(BRON, bron)
        if not os.path.exists(bp):
            print("  mist: %s" % bron)
            continue
        im = Image.open(bp).convert("RGB")
        if doos:
            im = im.crop(doos)
        im = snij_verhouding(im, verh, fx, fy)
        if im.width > breedte:
            im = im.resize((breedte, int(im.height * breedte / float(im.width))), Image.LANCZOS)
        q, grootte = schrijf(im, os.path.join(UIT, doel))
        print("  %-24s %4dx%-4d q%-3d %6.1f kB  %s"
              % (doel, im.width, im.height, q, grootte / 1024.0, wat))


if __name__ == "__main__":
    main()
