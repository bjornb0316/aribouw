# -*- coding: utf-8 -*-
"""Zet het Higgsfield-materiaal om naar wat de site laadt.

Alleen voor Aflak. De ruwe bestanden (PNG's van 2 tot 8 MB, MP4's tot 15 MB)
staan in bron/higgsfield/ en gaan niet mee in git. Wat eruit komt wel:
WebP-beelden en kleine MP4's zonder geluid, met een poster ernaast.

Waarom deze beelden er zijn, en wat ze NIET zijn:
  Het zijn gegenereerde sfeer- en procesbeelden: handen, tape, een kwast,
  een kamer. Er staat nergens een gezicht in en er wordt nergens beweerd
  dat het een klus van Aribouw is. Alles onder "Werk" blijft eigen foto.

Stills:  Nano Banana Pro (fysiek kloppend: kwast raakt echt het hout)
         en Soul 2.0 (interieur en still life).
Video:   Kling 3.0 Pro, 5 seconden, image-to-video vanaf die stills. De
         hero is een start- en eindbeeld: tape erop, tape eraf.

Draaien vanuit de projectmap:  python bouwscript/film.py
ffmpeg moet op het PATH staan, of zet FFMPEG=pad/naar/ffmpeg.
"""
import io, os, subprocess
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
WORTEL = os.path.abspath(os.path.join(HIER, ".."))
BRON = os.path.join(WORTEL, "bron", "higgsfield")
IMG = os.path.join(WORTEL, "assets", "img")
FILM = os.path.join(WORTEL, "assets", "film")
FFMPEG = os.environ.get("FFMPEG", "ffmpeg")

# (bron, doel, breedte, verhouding of None, wat)
STILLS = [
    ("r51.png", "kleur-licht.webp", 1400, 4 / 3.0, "kamer in gebroken wit"),
    ("s12.png", "kleur-warm.webp", 1400, 4 / 3.0, "kamer in warme zandtint"),
    ("s13.png", "kleur-donker.webp", 1400, 4 / 3.0, "deur in diep blauwgrijs"),
    ("s14.png", "kleur-weetniet.webp", 1400, 4 / 3.0, "kleurwaaier op tafel"),
    ("s21.png", "stap-fotos.webp", 1000, 4 / 3.0, "foto maken van een scheur"),
    ("s22.png", "stap-opname.webp", 1000, 4 / 3.0, "vochtmeter bij kozijn"),
    ("r52.png", "stap-offerte.webp", 1000, 4 / 3.0, "keukentafel met kleurwaaier"),
    ("s24.png", "stap-uitvoeren.webp", 1000, 4 / 3.0, "afgedekte kamer"),
    ("r53.png", "stap-opgeleverd.webp", 1000, 4 / 3.0, "opgeleverde kamer"),
    ("s31.png", "straat-liemers.webp", 1920, 16 / 9.0, "straat met rijtjeshuizen"),
    ("r52.png", "offerte-tafel.webp", 1920, 16 / 9.0, "keukentafel, breed"),
]

# (bron, doel, breedte, crf)
FILMS = [
    ("v71.mp4", "snijlijn", 1600, 21),
    # Binnenschilderwerk: de roller stond in v62 rechtop terwijl de haal
    # verticaal liep, en de verfbaan paste niet bij de rol. v95 is hetzelfde
    # beeld met de rol dwars, en loopt heen en terug zodat de lus niet
    # verspringt. Gemaakt op 23 september 2026.
    ("v95.mp4", "binnen-2", 1280, 23),
    ("v63.mp4", "buiten", 1280, 23),
    ("v64.mp4", "behang", 1280, 23),
    # Houtreparatie: plamuurmes zet houtvuller in een hersteld kozijn. Vervangt
    # de kitwerk-film (v65), die niet over hout ging. Gemaakt op 17 september.
    ("v82.mp4", "houtwerk", 1280, 23),
    # Specialismen, 17 september: lak op een paneeldeur, en een kwast die de
    # lijn tussen wand en plafond trekt.
    ("v93.mp4", "deuren", 1280, 23),
    ("v94.mp4", "wanden", 1280, 23),
    ("v66.mp4", "schemer", 1600, 24),
]


def snij(im, verh):
    b, h = im.size
    if verh is None:
        return im
    if b / float(h) > verh:
        nb = int(h * verh)
        l = (b - nb) // 2
        return im.crop((l, 0, l + nb, h))
    nh = int(b / verh)
    t = (h - nh) // 2
    return im.crop((0, t, b, t + nh))


def webp(im, pad, q=80):
    im.save(pad, "WEBP", quality=q, method=6)
    return os.path.getsize(pad)


def deelbeeld():
    """De afbeelding die WhatsApp, Facebook en LinkedIn tonen bij een gedeelde
    link: het eindbeeld van de hero, de strakke lijn, met de naam erop.
    1200 bij 630. alles.py kopieert hem naar elke variant als assets/og.jpg."""
    from PIL import ImageDraw, ImageFont
    bp = os.path.join(BRON, "e70.png")
    if not os.path.exists(bp):
        print("  mist: e70.png")
        return
    im = snij(Image.open(bp).convert("RGB"), 1200 / 630.0).resize((1200, 630), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    # Supreme staat niet op elke machine; Segoe UI Bold wel op Windows.
    def lettertype(namen, grootte):
        for n in namen:
            try:
                return ImageFont.truetype(n, grootte)
            except OSError:
                continue
        return ImageFont.load_default()
    klein = lettertype(["segoeui.ttf", "DejaVuSans.ttf", "arial.ttf"], 36)
    # Het logo van Ahmad in kleur op het witte deel rechtsboven: op het blauw
    # valt zijn blauwe huis weg. De regel staat linksonder op het blauw.
    logo = os.path.join(IMG, "logo-kop.png")
    if os.path.exists(logo):
        l = Image.open(logo).convert("RGBA")
        l = l.resize((int(l.width * 104 / float(l.height)), 104), Image.LANCZOS)
        im.paste(l, (1200 - l.width - 150, 64), l)
    else:
        groot = lettertype(["segoeuib.ttf", "DejaVuSans-Bold.ttf", "arialbd.ttf"], 86)
        d.text((70, 420), "ARIBOUW", font=groot, fill="#FFFFFF")
    groot2 = lettertype(["segoeuib.ttf", "DejaVuSans-Bold.ttf", "arialbd.ttf"], 58)
    d.text((70, 450), "Schilder in Westervoort", font=groot2, fill="#FFFFFF")
    d.text((72, 530), "Binnen, buiten, behangen en houtwerk", font=klein, fill="#DCE6F2")
    pad = os.path.join(IMG, "og-aribouw.jpg")
    im.save(pad, "JPEG", quality=84, optimize=True, progressive=True)
    print("  %-24s 1200x630   %6.1f kB  deelafbeelding" % ("og-aribouw.jpg", os.path.getsize(pad) / 1024.0))


def main():
    os.makedirs(IMG, exist_ok=True)
    os.makedirs(FILM, exist_ok=True)
    for bron, doel, breedte, verh, wat in STILLS:
        bp = os.path.join(BRON, bron)
        if not os.path.exists(bp):
            print("  mist: %s" % bron)
            continue
        im = snij(Image.open(bp).convert("RGB"), verh)
        if im.width > breedte:
            im = im.resize((breedte, int(im.height * breedte / float(im.width))), Image.LANCZOS)
        kb = webp(im, os.path.join(IMG, doel), 78) / 1024.0
        print("  %-24s %4dx%-4d %6.1f kB  %s" % (doel, im.width, im.height, kb, wat))

    deelbeeld()

    for bron, doel, breedte, crf in FILMS:
        bp = os.path.join(BRON, bron)
        if not os.path.exists(bp):
            print("  mist: %s" % bron)
            continue
        mp4 = os.path.join(FILM, doel + ".mp4")
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", bp, "-an",
                        "-vf", "scale=%d:-2:flags=lanczos,format=yuv420p" % breedte,
                        "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
                        "-profile:v", "high", "-movflags", "+faststart", mp4], check=True)
        # De poster is het eerste beeld, zodat er niets verspringt als de
        # film begint. Zonder JS of met minder beweging blijft dit staan.
        tmp = os.path.join(FILM, doel + "-poster.png")
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", bp,
                        "-vf", "scale=%d:-2:flags=lanczos" % breedte, "-frames:v", "1", tmp],
                       check=True)
        kb = webp(Image.open(tmp).convert("RGB"), os.path.join(FILM, doel + ".webp"), 76) / 1024.0
        os.remove(tmp)
        print("  %-24s %6.1f kB film, %5.1f kB poster"
              % (doel + ".mp4", os.path.getsize(mp4) / 1024.0, kb))


if __name__ == "__main__":
    main()
