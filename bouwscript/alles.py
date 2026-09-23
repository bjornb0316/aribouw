# -*- coding: utf-8 -*-
"""Bouwt de site van Aribouw.

  *.html, assets/     de site in de hoofdmap: films, kleurkiezer, voor-en-na,
                      aanvraag in stappen, dienst- en plaatspagina's
  variant-aflak/      doorverwijzingen voor de oude adressen

Er was ook een variant Grondlaag (Professional). Ahmad koos Aflak; Grondlaag
is op 17 september 2026 verwijderd. De code in paginas.py en paginas2.py kent
de variant nog, maar hij wordt niet meer gebouwd.

Draaien vanuit de projectmap:  python bouwscript/alles.py
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bouw as B
import data as D
import paginas as P1
import paginas2 as P2
import doorverwijzing


def main():
    B.stijlbladen()
    totaal = 0

    pagina = [
        ("index.html", P1.index("aflak")),
        ("diensten.html", P1.diensten("aflak")),
        ("werk.html", P1.werk("aflak")),
        ("werkgebied.html", P2.werkgebied("aflak")),
        ("offerte.html", P2.offerte("aflak")),
        ("contact.html", P2.contact("aflak")),
    ]
    for dienst in D.DIENSTEN + D.SUBDIENSTEN:
        pagina.append(("dienst-%s.html" % dienst[0], P2.dienstpagina("aflak", dienst)))
    for plaats in D.WERKGEBIED:
        pagina.append(("regio-%s.html" % plaats.lower(), P2.regiopagina("aflak", plaats)))
    pagina.append(("privacy.html", P2.privacy("aflak")))
    # Alleen voor Ahmad: niet in het menu en niet in de sitemap.
    # beheer.html staat als los bestand in de map: dat is geen sitepagina
    # maar het scherm waarmee Ahmad de site bijwerkt.
    # Sjabloon voor projectpagina's: de server vult hem met een project uit
    # de database. Zelf niet in het menu en niet in de sitemap.
    pagina.append(("project-sjabloon.html", P2.projectsjabloon("aflak")))
    # Cloudflare Pages serveert dit bestand met status 404 bij een adres dat
    # niet bestaat. Zonder 404.html kreeg elk verkeerd adres de homepage met
    # status 200. Zelf niet in de sitemap en niet in de doorverwijzingen.
    pagina.append(("404.html", P2.nietgevonden("aflak")))
    buiten = ("project-sjabloon.html", "404.html")
    for naam, inhoud in pagina:
        B.schrijf("aflak", naam, inhoud)
    B.zoekbestanden("aflak", [n for n, _ in pagina if n not in buiten])
    print("hoofdmap            %2d pagina's" % len(pagina))
    totaal += len(pagina)

    print("teksten             %2d bewerkbare zinnen" % B.tekstenlijst())
    n = doorverwijzing.bouw([n for n, _ in pagina if n not in buiten])
    print("variant-aflak/      %2d doorverwijzingen naar de hoofdmap" % n)

    print("\n%d pagina's geschreven" % totaal)


if __name__ == "__main__":
    main()
