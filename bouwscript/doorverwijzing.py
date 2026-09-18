# -*- coding: utf-8 -*-
"""Doorverwijzingen voor de oude adressen onder variant-aflak/.

De site stond eerst in variant-aflak/, naast een tweede variant en een
keuzepagina. Sinds 17 september 2026 staat hij in de hoofdmap. Links die al
gedeeld zijn (met Ahmad, in WhatsApp) blijven werken: elke oude pagina stuurt
door naar dezelfde pagina in de hoofdmap, inclusief querystring en anker.

Bij livegang op een eigen domein is deze map niet meer nodig.
"""
import io, os

WORTEL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def bouw(namen):
    map_ = os.path.join(WORTEL, "variant-aflak")
    os.makedirs(map_, exist_ok=True)
    for naam in namen:
        doel = "../" + ("" if naam == "index.html" else naam[:-5])
        html = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<title>Aribouw</title>
<link rel="canonical" href="%(doel)s">
<meta http-equiv="refresh" content="0; url=%(doel)s">
<script>location.replace("%(doel)s" + location.search + location.hash);</script>
</head>
<body>
<p>Deze pagina is verhuisd: <a href="%(doel)s">ga verder</a>.</p>
</body>
</html>
""" % dict(doel=doel)
        io.open(os.path.join(map_, naam), "w", encoding="utf-8").write(html)
    return len(namen)
