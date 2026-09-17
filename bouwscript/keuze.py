# -*- coding: utf-8 -*-
"""De wortel van de site.

Eerst stond hier een keuzepagina met twee varianten naast elkaar. Ahmad
heeft voor Aflak gekozen en de andere variant is verwijderd, dus de wortel
stuurt nu direct door naar variant-aflak/.

Bij livegang op een eigen domein komt Aflak zelf in de wortel te staan en
is deze doorverwijzing niet meer nodig.
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D

WORTEL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def bouw():
    doel = "variant-aflak/"
    html = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Aribouw, schilder in Westervoort</title>
<link rel="canonical" href="%(site)s/">
<meta http-equiv="refresh" content="0; url=%(doel)s">
<link rel="icon" href="%(doel)sassets/favicon-48.png" sizes="48x48" type="image/png">
<script>location.replace("%(doel)s" + location.search + location.hash);</script>
<style>body{font-family:system-ui,sans-serif;background:#F6F4F0;color:#23262B;margin:0;
  padding:3rem 1.2rem;text-align:center}a{color:#14508C}</style>
</head>
<body>
<p>U wordt doorgestuurd naar <a href="%(doel)s">de website van Aribouw</a>.</p>
</body>
</html>
""" % dict(doel=doel, site=D.SITE_URL["aflak"])
    pad = os.path.join(WORTEL, "index.html")
    io.open(pad, "w", encoding="utf-8").write(html)
    return pad


if __name__ == "__main__":
    print(bouw())
