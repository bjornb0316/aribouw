# -*- coding: utf-8 -*-
"""De keuzepagina op de wortel.

Twee kolommen die elkaar raken in een schuine snijlijn: hetzelfde motief
als op de site zelf. Geen bedragen, wel het aantal pagina's, want daar
gaat het gesprek over.
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D

WORTEL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

GRONDLAAG = [
    "Zes pagina&#39;s: home, diensten, werk, over, offerte, contact",
    "Gesplitste hero met het beeld dat rechts van het scherm afloopt",
    "Sectielabels op een linkerrail, als het etiket op een verfblik",
    "Diensten als kleurstalen die uit een waaier lijken te liggen",
    "Werkwijze als verticale tijdlijn, niet als rij kolommen",
    "Vier echte Werkspot-reviews met naam, plaats en datum",
    "Contactformulier met veldcontrole en bevestiging in beeld",
]

AFLAK = [
    ("Filmhero en films per dienst",
     "Tape die van de muur gaat en een strakke lijn achterlaat. Elke dienstpagina opent met een "
     "eigen film, gemaakt met Higgsfield."),
    ("Voor-en-na en ruimte voor eigen werk",
     "Sleepbare voor-en-na van eigen klussen. Elk nieuw paar foto&#39;s krijgt vanzelf een eigen "
     "schuif."),
    ("Route voor aannemers en architecten",
     "Een eigen blok en een aanvraag die meteen als zakelijk project begint."),
    ("Kleurkiezer",
     "Vier richtingen. De bezoeker klikt wat hem aanspreekt en leest meteen waar bij die keuze op "
     "gelet moet worden. De keuze gaat mee de aanvraag in."),
    ("Aanvraag in zes stappen",
     "Wat, hoeveel, welke kleur, wat voor ondergrond, wanneer, en pas op het eind drie velden."),
    ("WhatsApp-bericht dat al is ingevuld",
     "Na de aanvraag staat er een bericht klaar met de situatie, de kleurrichting, de naam en het "
     "nummer erin."),
    ("Blauwe kleurvlakken",
     "Waar Grondlaag alles op papier houdt, wisselt Aflak hele secties af in diepblauw. De vlakken "
     "raken elkaar in de schuine snijlijn."),
    ("Vier dienstpagina&#39;s en vier plaatspagina&#39;s",
     "Elk met eigen tekst en eigen vragen. Dat is waar Google op zoekt bij 'schilder Westervoort'."),
]


def bouw():
    html = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Aribouw | Twee voorstellen</title>
<meta name="description" content="Twee uitgewerkte voorstellen voor de website van Aribouw.">
<meta name="theme-color" content="#F6F4F0">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f%%5B%%5D=supreme@700&f%%5B%%5D=synonym@400,500,700&display=swap">
<style>
:root{
  --papier:#F6F4F0; --wit:#FCFBF9; --zand:#E9E4DB; --nacht:#171A1F;
  --inkt:#23262B; --inkt-2:#4C525A; --inkt-3:#616872;
  --blauw:#14508C; --blauw-2:#0E3D6D; --blauw-3:#E4EBF3;
  --lijn:#DFD9CE; --lijn-2:#C9C1B4;
  --licht:#F3F1ED; --licht-2:#B4BAC3; --licht-3:#8B939E;
  --r:4px; --marge:clamp(1.15rem,4vw,4.5rem);
  --soepel:cubic-bezier(.2,.8,.3,1);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%%}
body{background:var(--papier);color:var(--inkt);
  font-family:Synonym,-apple-system,"Segoe UI",Roboto,sans-serif;
  font-size:17px;line-height:1.64;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%%;height:auto;display:block}
ul{list-style:none}
.display{font-family:Supreme,Synonym,sans-serif;font-weight:700;line-height:1.08;
  letter-spacing:-.02em}
.wrap{max-width:1240px;margin-inline:auto;padding-inline:var(--marge)}
:focus-visible{outline:2px solid var(--blauw);outline-offset:3px}

.balk{background:var(--nacht);color:#CBD1D9;font-size:.83rem;padding:.55rem var(--marge);
  display:flex;flex-wrap:wrap;gap:.1rem 1.1rem;justify-content:center;text-align:center}
.balk a{color:#fff;text-decoration:underline;text-underline-offset:3px}
@media (max-width:760px){.balk a{display:inline-flex;align-items:center;min-height:44px}}

.blad{padding:clamp(2.2rem,4.5vw,3.6rem) 0 clamp(1.8rem,3.5vw,2.8rem)}
.merk{display:flex;align-items:center;gap:.65rem;line-height:1}
.merk b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.18rem;letter-spacing:.02em;
  display:block}
.merk small{display:block;font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--inkt-3);margin-top:.2rem;font-weight:500}
.blad h1{font-size:clamp(2rem,4vw,3.1rem);margin-top:1.9rem;max-width:20ch}
.blad p{color:var(--inkt-2);max-width:56ch;margin-top:1.1rem}

/* de snijlijn, hetzelfde motief als op de site */
.snee{height:clamp(48px,6vw,86px);position:relative;overflow:hidden;background:var(--papier)}
.snee::before{content:"";position:absolute;inset:0;background:var(--zand);
  clip-path:polygon(0 0,100%% 0,100%% 22%%,0 100%%)}
.snee::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to bottom right,transparent calc(50%% - 1px),
             var(--blauw) calc(50%% - 1px),var(--blauw) calc(50%% + 1px),
             transparent calc(50%% + 1px));
  clip-path:polygon(0 0,100%% 0,100%% 22%%,0 100%%)}

.paar{display:grid}
@media (min-width:1000px){.paar{grid-template-columns:1fr 1fr}}
.kolom{padding:clamp(2.2rem,4.5vw,4rem) var(--marge) clamp(2.6rem,5vw,4.4rem)}
.kolom--grond{background:var(--zand)}
.kolom--aflak{background:var(--blauw);color:#fff}
@media (min-width:1000px){
  .kolom--grond{padding-left:max(var(--marge),calc((100vw - 1240px) / 2 + var(--marge)))}
  .kolom--aflak{padding-right:max(var(--marge),calc((100vw - 1240px) / 2 + var(--marge)))}
}
.kolom-beeld img{width:100%%;aspect-ratio:16/10;object-fit:cover;border-radius:var(--r)}
.kolom-bij{margin-top:.7rem;font-size:.8rem;color:var(--inkt-3)}
.kolom--aflak .kolom-bij{color:#A9C2DC}
.kolom-kop{display:flex;align-items:baseline;justify-content:space-between;gap:1.4rem;
  flex-wrap:wrap;margin-top:1.8rem;padding-bottom:1rem;border-bottom:1px solid var(--lijn-2)}
.kolom--aflak .kolom-kop{border-color:rgba(255,255,255,.28)}
.kolom-kop h2{font-size:clamp(1.8rem,3.2vw,2.6rem)}
.tier{font-size:.7rem;font-weight:700;letter-spacing:.19em;text-transform:uppercase;
  color:var(--blauw);display:block;margin-bottom:.4rem}
.kolom--aflak .tier{color:#9EC2E4}
.omvang{text-align:right;line-height:1;flex-shrink:0}
.omvang b{font-family:Supreme,sans-serif;font-weight:700;font-size:clamp(1.8rem,3vw,2.5rem);
  letter-spacing:-.03em;display:block}
.omvang span{display:block;margin-top:.35rem;font-size:.66rem;letter-spacing:.19em;
  text-transform:uppercase;font-weight:700;color:var(--inkt-3)}
.kolom--aflak .omvang span{color:#A9C2DC}
.zin{margin-top:1.1rem;color:var(--inkt-2);max-width:46ch}
.kolom--aflak .zin{color:#CFDDEC}

.punten{margin-top:1.5rem;display:grid;gap:.1rem}
.punten li{position:relative;padding:.55rem 0 .55rem 1.2rem;font-size:.92rem;color:var(--inkt-2);
  border-top:1px solid var(--lijn-2)}
.punten li::before{content:"";position:absolute;left:0;top:1.15em;width:8px;height:2px;
  background:var(--blauw)}
.kolom--aflak .punten li{color:#CFDDEC;border-color:rgba(255,255,255,.22)}
.kolom--aflak .punten li::before{background:#fff}
.punten b{display:block;color:var(--inkt);font-family:Supreme,sans-serif;font-weight:700;
  font-size:.97rem;margin-bottom:.15rem}
.kolom--aflak .punten b{color:#fff}

.knopgroep{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:2rem}
.knop{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;min-height:50px;
  padding:.75rem 1.4rem;border-radius:var(--r);font-weight:700;font-size:.96rem;
  border:1.5px solid transparent;transition:background .2s,color .2s,border-color .2s,gap .2s}
.knop svg{width:14px;height:9px}
.knop--vol{background:var(--blauw);color:#fff;border-color:var(--blauw)}
.knop--vol:hover{background:var(--blauw-2);border-color:var(--blauw-2);gap:.8rem}
.knop--lijn{color:var(--inkt);border-color:var(--lijn-2)}
.knop--lijn:hover{border-color:var(--blauw);color:var(--blauw)}
.kolom--aflak .knop--vol{background:#fff;color:var(--blauw);border-color:#fff}
.kolom--aflak .knop--vol:hover{background:var(--licht);border-color:var(--licht)}
.kolom--aflak .knop--lijn{color:#fff;border-color:rgba(255,255,255,.42)}
.kolom--aflak .knop--lijn:hover{border-color:#fff;background:rgba(255,255,255,.1)}

.uitleg{padding:clamp(2.2rem,4vw,3.2rem) 0}
.uitleg h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.2rem}
.uitleg p{margin-top:.9rem;max-width:62ch;color:var(--inkt-2)}

.open{background:var(--zand);padding:clamp(2.2rem,4vw,3.2rem) 0 clamp(3rem,6vw,4.5rem)}
.open-kop{display:flex;align-items:baseline;gap:.9rem;flex-wrap:wrap}
.open-kop h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.15rem}
.open-kop span{font-size:.7rem;letter-spacing:.19em;text-transform:uppercase;font-weight:700;
  color:var(--inkt-3)}
.open ul{margin-top:1.4rem;display:grid;gap:.1rem;
  grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));column-gap:clamp(1.5rem,4vw,3.5rem)}
.open li{position:relative;padding:.7rem 0 .7rem 1.2rem;font-size:.88rem;color:var(--inkt-2);
  border-top:1px solid var(--lijn-2)}
.open li::before{content:"";position:absolute;left:0;top:1.3em;width:8px;height:2px;
  background:var(--lijn-2)}

@media (prefers-reduced-motion:no-preference){
  .op{opacity:0;transform:translateY(15px);animation:op .8s var(--soepel) forwards}
  .op-2{animation-delay:.1s} .op-3{animation-delay:.2s}
  @keyframes op{to{opacity:1;transform:none}}
}
</style>
</head>
<body>

<div class="balk">
  <span>Twee voorstellen voor Aribouw, gemaakt door Bjorn van Capital BB.</span>
  <span><a href="https://wa.me/%(bjorn)s">Reageren via WhatsApp</a></span>
</div>

<header class="blad op">
  <div class="wrap">
    <span class="merk">
      %(mark)s
      <span><b>ARIBOUW</b><small>Schilderen &middot; behangen</small></span>
    </span>
    <h1 class="display">Twee vlakken, dezelfde snijlijn.</h1>
    <p>Allebei met jullie eigen foto&#39;s, jullie eigen blauw en dezelfde zorg voor detail. Het
    verschil zit in hoeveel de site zelf doet voordat de telefoon gaat.</p>
  </div>
</header>

<div class="snee" aria-hidden="true"></div>

<main class="paar">
  <section class="kolom kolom--grond op op-2">
    <div class="kolom-beeld">
      <img src="assets/img/pui-voetzorg.webp" width="1600" height="1000"
           alt="Geschilderde pui en deur van een praktijkruimte">
      <p class="kolom-bij">De hero van Grondlaag.</p>
    </div>
    <div class="kolom-kop">
      <div>
        <span class="tier">Professional</span>
        <h2 class="display">Grondlaag</h2>
      </div>
      <p class="omvang"><b>6</b><span>Pagina&#39;s</span></p>
    </div>
    <p class="zin">De verzorgde bedrijfssite. Rustig, licht en compleet. Een bezoeker weet binnen
    een scherm wat jullie doen, waar en hoe goed het beoordeeld wordt.</p>
    <ul class="punten">
%(grondlaag)s
    </ul>
    <div class="knopgroep">
      <a class="knop knop--vol" href="variant-grondlaag/index.html">Bekijk Grondlaag %(pijl)s</a>
      <a class="knop knop--lijn" href="variant-grondlaag/offerte.html">Naar het formulier</a>
    </div>
  </section>

  <section class="kolom kolom--aflak op op-3">
    <div class="kolom-beeld">
      <img src="assets/film/snijlijn.webp" width="1600" height="893"
           alt="Hand die afplaktape langs een strakke lijn tussen blauw en wit van de muur trekt">
      <p class="kolom-bij">De hero van Aflak: een film die de tape van de muur trekt.</p>
    </div>
    <div class="kolom-kop">
      <div>
        <span class="tier">Performance</span>
        <h2 class="display">Aflak</h2>
      </div>
      <p class="omvang"><b>14</b><span>Pagina&#39;s</span></p>
    </div>
    <p class="zin">Alles uit Grondlaag, plus alles hieronder. De site kwalificeert de aanvraag
    zelf, dus het gesprek begint niet meer bij nul.</p>
    <ul class="punten">
%(aflak)s
    </ul>
    <div class="knopgroep">
      <a class="knop knop--vol" href="variant-aflak/index.html">Bekijk Aflak %(pijl)s</a>
      <a class="knop knop--lijn" href="variant-aflak/offerte.html">Naar de aanvraag</a>
    </div>
  </section>
</main>

<section class="uitleg">
  <div class="wrap">
    <h3>Waar het verschil in zit</h3>
    <p>Grondlaag vertelt goed wie Aribouw is. Aflak neemt werk uit handen: acht pagina&#39;s meer,
    een kleurkiezer die de lastigste vraag naar voren haalt, een aanvraag in stappen en een
    WhatsApp-bericht dat al is ingevuld. Ook het ontwerp is anders: Grondlaag houdt alles op
    papier, Aflak zet hele secties in diepblauw en schuift de kop en het beeld een niveau groter.</p>
    <p>Wat Grondlaag niet minder heeft: dezelfde foto&#39;s, dezelfde typografie, dezelfde
    reviews en dezelfde mobiele navigatie. Wie alleen Grondlaag neemt, krijgt een afgemaakte site.</p>
  </div>
</section>

<section class="open">
  <div class="wrap">
    <div class="open-kop">
      <h3>Wat nog niet ingevuld is</h3>
      <span>Voor livegang</span>
    </div>
    <ul>
%(openstaand)s
    </ul>
  </div>
</section>

</body>
</html>
""" % dict(
        bjorn=D.BJORN_WA,
        mark=('<svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true">'
              '<rect x="0" y="0" width="28" height="28" rx="4" fill="#23262B"/>'
              '<path d="M0 28V4a4 4 0 0 1 4-4h24z" fill="#14508C"/></svg>'),
        pijl=('<svg viewBox="0 0 14 9" fill="none" aria-hidden="true">'
              '<path d="M0 4.5h12M8.5 1L12 4.5 8.5 8" stroke="currentColor" '
              'stroke-width="1.4"/></svg>'),
        grondlaag="\n".join("      <li>%s</li>" % p for p in GRONDLAAG),
        aflak="\n".join("      <li><b>%s</b>%s</li>" % (k, t) for k, t in AFLAK),
        openstaand="\n".join("      <li>%s</li>" % o for o in D.ONBEVESTIGD))

    pad = os.path.join(WORTEL, "index.html")
    io.open(pad, "w", encoding="utf-8").write(html)
    return pad


if __name__ == "__main__":
    print(bouw())
