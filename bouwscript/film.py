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
    ("v62.mp4", "binnen", 1280, 23),
    ("v63.mp4", "buiten", 1280, 23),
    ("v64.mp4", "behang", 1280, 23),
    ("v65.mp4", "kitwerk", 1280, 23),
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
