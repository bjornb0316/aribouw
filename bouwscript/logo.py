# -*- coding: utf-8 -*-
"""Maakt uit het logo van Ahmad alles wat de site nodig heeft.

Bron: bron/logo-aribouw.jpg, aangeleverd op 16 september 2026. Een JPG op
wit, geen vector. Het wit wordt transparant gemaakt ("kleur naar alfa"),
zodat de randen zacht blijven en er geen witte rand om het logo staat.

Wat eruit komt, in assets/img/:
  logo-kop.png        huis en ARIBOUW naast elkaar, voor de kop
  logo-kop-wit.png    idem met het zwart wit gemaakt, voor de donkere voet
  logo-aribouw.png    het volledige logo, voor structured data
  favicon-32.png      het huis, 32 pixels
  favicon-48.png      het huis, 48 pixels
  apple-touch-icon.png  het huis op wit, 180 pixels

In de kop staat bewust niet de regel "schilderen | behangen | renovatie":
die is op 40 pixels hoog onleesbaar, en de site legt de nadruk op
schilderwerk. Het volledige logo met die regel blijft beschikbaar.

Voor livegang blijft een vectorbestand beter; dit is een nette oplossing
tot dat er is.

Draaien vanuit de projectmap:  python bouwscript/logo.py
"""
import os
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.abspath(os.path.join(HIER, ".."))
BRON = os.path.join(WORTEL, "bron", "logo-aribouw.jpg")
UIT = os.path.join(WORTEL, "assets", "img")

# Uitsneden in de bron, gemeten op de rijen en kolommen met inkt.
HUIS = (170, 0, 1026, 746)
NAAM = (0, 843, 1170, 1003)


def naar_alfa(im):
    """Wit wordt transparant. Voor elke pixel: hoe ver is hij van wit
    verwijderd, dat is de dekking; de kleur wordt daarvoor gecorrigeerd."""
    im = im.convert("RGB")
    uit = []
    for r, g, b in im.getdata():
        a = 255 - min(r, g, b)
        if a < 14:
            uit.append((0, 0, 0, 0))
            continue
        if a > 240:
            uit.append((r, g, b, 255))
            continue
        f = 255.0 / a
        uit.append((max(0, min(255, int(round((r - (255 - a)) * f)))),
                    max(0, min(255, int(round((g - (255 - a)) * f)))),
                    max(0, min(255, int(round((b - (255 - a)) * f)))), a))
    nieuw = Image.new("RGBA", im.size)
    nieuw.putdata(uit)
    return nieuw


def wit_van_zwart(im):
    """Zwart en donkergrijs worden wit, het blauw blijft blauw."""
    uit = []
    for r, g, b, a in im.getdata():
        if a and max(r, g, b) < 90 and abs(r - b) < 40:
            uit.append((246, 244, 240, a))
        else:
            uit.append((r, g, b, a))
    nieuw = Image.new("RGBA", im.size)
    nieuw.putdata(uit)
    return nieuw


def schaal(im, hoogte):
    return im.resize((int(round(im.width * hoogte / float(im.height))), hoogte), Image.LANCZOS)


def vierkant(im, marge=0.0, achtergrond=(0, 0, 0, 0)):
    z = int(max(im.size) * (1 + 2 * marge))
    doek = Image.new("RGBA", (z, z), achtergrond)
    doek.alpha_composite(im, ((z - im.width) // 2, (z - im.height) // 2))
    return doek


def main():
    os.makedirs(UIT, exist_ok=True)
    logo = naar_alfa(Image.open(BRON))
    huis = logo.crop(HUIS)
    naam = logo.crop(NAAM)

    # De kop: huis 120 hoog, naam op ongeveer twee vijfde daarvan, verticaal
    # gecentreerd. Getoond op 40 pixels, dus scherp op een retinascherm.
    H = 120
    h_huis = schaal(huis, H)
    h_naam = schaal(naam, 42)
    gat = 26
    kop = Image.new("RGBA", (h_huis.width + gat + h_naam.width, H), (0, 0, 0, 0))
    kop.alpha_composite(h_huis, (0, 0))
    kop.alpha_composite(h_naam, (h_huis.width + gat, (H - h_naam.height) // 2 + 4))
    kop.save(os.path.join(UIT, "logo-kop.png"), optimize=True)
    wit_van_zwart(kop).save(os.path.join(UIT, "logo-kop-wit.png"), optimize=True)
    print("  logo-kop.png          %dx%d" % kop.size)

    volledig = schaal(logo, 600)
    volledig.save(os.path.join(UIT, "logo-aribouw.png"), optimize=True)
    print("  logo-aribouw.png      %dx%d" % volledig.size)

    icoon = vierkant(huis, 0.04)
    for maat in (32, 48):
        icoon.resize((maat, maat), Image.LANCZOS).save(
            os.path.join(UIT, "favicon-%d.png" % maat), optimize=True)
    # iOS rondt zelf af en zet transparant op zwart: dus een witte grond.
    appel = vierkant(huis, 0.14, (255, 255, 255, 255)).resize((180, 180), Image.LANCZOS)
    appel.convert("RGB").save(os.path.join(UIT, "apple-touch-icon.png"), optimize=True)
    print("  favicons en apple-touch-icon")


if __name__ == "__main__":
    main()
