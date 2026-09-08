# -*- coding: utf-8 -*-
"""Haalt het beschikbare beeldmateriaal op naar bron/.

Let op wat er NIET bij zit. Het Instagram-account @aribouw uit de briefing
is niet van dit bedrijf: het staat op naam van "walid aribou", heeft nul
volgers en geen enkele post. Daar is dus niets vandaan gehaald.

Wat er wel is:
  - een projectfoto van het Werkspot-profiel, op volle resolutie
  - de foto's van de Facebookpagina Ari Bouw

Downloaden gaat via curl omdat Python's SSL hier struikelt over de
virusscanner.
"""
import os, subprocess, sys

HIER = os.path.dirname(os.path.abspath(__file__))
BRON = os.path.join(os.path.abspath(os.path.join(HIER, "..")), "bron")

# Werkspot serveert het origineel onder /images/sr/original/.
WERKSPOT = [
    ("ws-pui.jpg",
     "https://www.werkspot.nl/images/sr/original/245c525c-3f5d-4509-8ab9-e459ce5092f6.jpg"),
]

# De miniaturen op Facebook zijn bijgesneden via de stp-parameter. Zonder
# die parameter komt het hele beeld terug.
FB = [
    ("fb-01.jpg", "492222675_122124854930708649_209408239024483148_n.jpg"),
    ("fb-02.jpg", "547511508_122141603738708649_2936865559861236875_n.jpg"),
    ("fb-03.jpg", "500241006_122129258756708649_3095975410401274166_n.jpg"),
    ("fb-04.jpg", "500130350_122129258762708649_966872052990934389_n.jpg"),
    ("fb-05.jpg", "500451285_122129146868708649_943295435503359167_n.jpg"),
    ("fb-06.jpg", "500309819_122129146856708649_4577339505748295469_n.jpg"),
    ("fb-07.jpg", "494207952_122125488134708649_9180968035135140104_n.jpg"),
    ("fb-08.jpg", "494133749_122125488128708649_5234365818851797350_n.jpg"),
    ("fb-09.jpg", "492230093_122124856802708649_3149876230425362338_n.jpg"),
]
FB_BASIS = "https://scontent-ams2-1.xx.fbcdn.net/v/t39.30808-6/%s"


def haal(naam, url):
    pad = os.path.join(BRON, naam)
    subprocess.run(["curl", "-sS", "-L", "-o", pad, url], capture_output=True)
    maat = os.path.getsize(pad) if os.path.exists(pad) else 0
    print("  %-14s %8.1f kB" % (naam, maat / 1024.0))


def main():
    os.makedirs(BRON, exist_ok=True)
    for naam, url in WERKSPOT:
        haal(naam, url)
    for naam, bestand in FB:
        haal(naam, FB_BASIS % bestand)


if __name__ == "__main__":
    main()
