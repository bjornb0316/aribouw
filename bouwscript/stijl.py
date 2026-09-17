# -*- coding: utf-8 -*-
"""Het design system.

Waar een schilder op wordt afgerekend is de snijlijn: de overgang waar
twee vlakken elkaar raken. Strak afgeplakt, geen verf op het glas, geen
uitgelopen rand. Dat is hier de layoutlogica geworden:

  - secties raken elkaar in een harde kleurrand, zonder lijntje ertussen
  - de tapelijn is het enige scheidingsteken dat er wel is
  - dienstkaarten hebben een kleurbaan bovenaan, als een kleurstaal
  - radius 4px, want binnenwerk is glad afgewerkt, niet scherp

Het accent is hun eigen blauw uit het logo, iets dieper gezet zodat wit
erop 7,9 haalt.
"""

BASIS = r"""/* =====================================================================
   Aribouw, schilderen en behangen
   Voorbeeldontwerp, Bjorn van Capital BB
   ===================================================================== */

:root{
  --papier:  #F6F4F0;  /* de grond van de site */
  --wit:     #FCFBF9;  /* panelen en formulieren */
  --zand:    #E9E4DB;  /* afwisselende secties */
  --nacht:   #171A1F;  /* de donkere grond onderaan */

  --inkt:    #23262B;  /* lopende tekst, 13,6 op papier */
  --inkt-2:  #4C525A;  /* rustige tekst, 7,1 */
  --inkt-3:  #5A6069;  /* bijschriften, 5,0 op zand */

  --blauw:   #14508C;  /* hun eigen blauw, wit erop haalt 7,9 */
  --blauw-2: #0E3D6D;
  --blauw-3: #E4EBF3;  /* lichte tint voor vlakken */
  --lijn:    #DFD9CE;
  --lijn-2:  #C9C1B4;

  --licht:   #F3F1ED;
  --licht-2: #B4BAC3;
  --licht-3: #8B939E;

  --r: 4px;            /* glad afgewerkt, niet scherp */
  --marge: clamp(1.15rem,4vw,4.5rem);
  --lucht: clamp(4rem,8vw,7.5rem);
  --max: 1240px;
  --soepel: cubic-bezier(.2,.8,.3,1);
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}

body{
  background:var(--papier);color:var(--inkt);
  font-family:Synonym,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:17px;line-height:1.64;-webkit-font-smoothing:antialiased;overflow-x:hidden;
}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
ul{list-style:none}
:focus-visible{outline:2px solid var(--blauw);outline-offset:3px}

.wrap{max-width:var(--max);margin-inline:auto;padding-inline:var(--marge)}

/* ---------- typografie ---------- */
.display{font-family:Supreme,Synonym,sans-serif;font-weight:700;line-height:1.08;
  letter-spacing:-.02em}
h1.display{font-size:clamp(2.1rem,4.2vw,3.4rem)}
h2.display{font-size:clamp(1.75rem,3.3vw,2.6rem)}
h3.display{font-size:clamp(1.1rem,1.6vw,1.3rem);font-weight:700}
.intro{color:var(--inkt-2);font-size:clamp(1.02rem,1.35vw,1.12rem);max-width:56ch}
.klein{font-size:.88rem;color:var(--inkt-3)}
.label{font-size:.7rem;font-weight:700;letter-spacing:.19em;text-transform:uppercase;
  color:var(--blauw)}

/* ---------- de snijlijn ----------
   Twee vlakken die elkaar raken in een schuine, kaarsrechte rand. Dat is
   letterlijk waar een schilder op wordt afgerekend, en het is meteen het
   enige scheidingsteken dat de site heeft. */
.snee{height:clamp(48px,6vw,86px);position:relative;overflow:hidden;background:var(--papier)}
.snee::before{content:"";position:absolute;inset:0;background:var(--zand);
  clip-path:polygon(0 0,100% 0,100% 22%,0 100%)}
.snee::after{content:"";position:absolute;inset:0;
  background:linear-gradient(to bottom right,transparent calc(50% - 1px),
             var(--blauw) calc(50% - 1px),var(--blauw) calc(50% + 1px),
             transparent calc(50% + 1px));
  clip-path:polygon(0 0,100% 0,100% 22%,0 100%)}
.snee--om::before,.snee--om::after{clip-path:polygon(0 0,100% 100%,100% 0)}
.snee--zand{background:var(--zand)}
.snee--zand::before{background:var(--papier)}

/* ---------- kop ---------- */
.voorstel{background:var(--nacht);color:#CBD1D9;font-size:.82rem;padding:.5rem 0}
.voorstel .wrap{display:flex;flex-wrap:wrap;gap:.1rem 1.1rem;justify-content:center;
  text-align:center}
.voorstel a{color:#fff;text-decoration:underline;text-underline-offset:3px}

.kop{position:sticky;top:0;z-index:40;background:rgba(246,244,240,.93);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--lijn)}
.kop-in{height:74px;display:flex;align-items:center;gap:clamp(1rem,3vw,2.4rem)}
@media (max-width:900px){.kop-in{height:62px}}

.merk{flex-shrink:0;display:flex;align-items:center;gap:.65rem;line-height:1}
.merk-logo{height:30px;width:auto;display:block}
@media (max-width:900px){.merk-logo{height:26px}}
.voet-merk .merk-logo{height:30px}
.merk b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.18rem;
  letter-spacing:.02em;display:block}
.merk small{display:block;font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--inkt-3);margin-top:.2rem;font-weight:500}
@media (max-width:900px){.merk small{display:none}}

.nav{display:flex;gap:clamp(.8rem,1.6vw,1.6rem);margin-left:auto;font-size:.93rem;
  white-space:nowrap}
.nav a{padding-block:.35rem;color:var(--inkt-2);border-bottom:2px solid transparent;
  transition:color .18s,border-color .18s}
.nav a:hover{color:var(--inkt);border-bottom-color:var(--blauw)}
.nav a[aria-current="page"]{color:var(--inkt);border-bottom-color:var(--blauw)}
.kop-rechts{display:flex;align-items:center;gap:1rem;margin-left:1rem}
.kop-tel{font-weight:700;font-size:.95rem;white-space:nowrap}
@media (max-width:1120px){.nav,.kop-rechts{display:none}}

.menu-knop{display:none;margin-left:auto;width:44px;height:44px;border:1px solid var(--lijn-2);
  border-radius:var(--r);flex-direction:column;justify-content:center;align-items:center;gap:5px}
.menu-knop span{display:block;width:18px;height:1.5px;background:var(--inkt)}
@media (max-width:1120px){.menu-knop{display:flex}}

.menu{position:fixed;inset:0;z-index:60;background:var(--papier);
  padding:1.1rem var(--marge) 2rem;display:none;flex-direction:column}
.menu[data-open="1"]{display:flex}
.menu-top{display:flex;align-items:center;justify-content:space-between;height:62px;
  margin-bottom:1.4rem;border-bottom:1px solid var(--lijn)}
.menu-sluit{font-size:2rem;line-height:1;width:44px;height:44px}
.menu nav{display:flex;flex-direction:column}
.menu nav a{font-family:Supreme,sans-serif;font-weight:700;font-size:1.6rem;
  letter-spacing:-.015em;padding:.65rem 0;border-bottom:1px solid var(--lijn)}
.menu .knopgroep{margin-top:auto;padding-top:2rem;flex-direction:column}
.menu .knop{width:100%;min-height:50px}

/* ---------- knoppen ---------- */
.knopgroep{display:flex;flex-wrap:wrap;gap:.6rem}
.knop{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;
  min-height:50px;padding:.75rem 1.4rem;border-radius:var(--r);
  font-weight:700;font-size:.96rem;text-align:center;
  border:1.5px solid transparent;transition:background .2s,color .2s,border-color .2s}
.knop--vol{background:var(--blauw);color:#fff;border-color:var(--blauw)}
.knop--vol:hover{background:var(--blauw-2);border-color:var(--blauw-2)}
.knop--lijn{color:var(--inkt);border-color:var(--lijn-2)}
.knop--lijn:hover{border-color:var(--blauw);color:var(--blauw)}
.knop--klein{min-height:42px;padding:.5rem 1rem;font-size:.88rem}
@media (max-width:760px){.knop{min-height:48px}}

/* ---------- secties ---------- */
.sectie{padding-block:var(--lucht)}
.sectie--zand{background:var(--zand)}
.sectie--blauwlicht{background:var(--blauw-3)}
.sectie--nacht{background:var(--nacht);color:var(--licht)}
.sectie--nacht .intro{color:var(--licht-2)}
.sectie--nacht .klein{color:var(--licht-3)}
.sectie--nacht .label{color:#7FA9D6}
.sectie--nacht .veld label{color:var(--licht)}
.sectie--nacht .veld .hulp,.sectie--nacht .formulier-noot{color:var(--licht-3)}
.sectie--nacht .knop--lijn{color:var(--licht);border-color:rgba(243,241,237,.34)}
.sectie--nacht .knop--lijn:hover{color:#fff;border-color:var(--licht);
  background:rgba(243,241,237,.08)}

/* De sectiekop staat op een smalle linkerrail, zoals het etiket op een
   verfblik: aanduiding links, inhoud rechts. Dat loopt door over de hele
   site en geeft elke sectie dezelfde leesrichting. */
.sectie-kop{margin-bottom:clamp(2rem,3.6vw,3.2rem)}
.sectie-kop .intro{margin-top:.95rem}
.sectie-kop .display{max-width:22ch}
@media (min-width:1000px){
  .rail{display:grid;grid-template-columns:11rem minmax(0,1fr);
    gap:0 clamp(2rem,4vw,3.6rem);align-items:start}
  .rail > .rail-kop{position:sticky;top:6.5rem;padding-top:.3rem;
    border-top:2px solid var(--blauw)}
  .rail-kop p{font-size:.85rem;color:var(--inkt-3);margin-top:.4rem}
}
.rail-kop{margin-bottom:1.6rem;padding-top:.3rem;border-top:2px solid var(--blauw)}
.rail-naam{display:block;font-family:Supreme,sans-serif;font-weight:700;font-size:.95rem;
  color:var(--inkt)}
@media (min-width:1000px){.rail-kop{margin-bottom:0}}
.sectie-kop--rij{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;
  gap:1.2rem;max-width:none}

/* ---------- hero van Grondlaag ----------
   Tekst links binnen de marge, beeld in een hoge kolom die aan de
   rechterkant van het scherm afloopt. Geen kader eromheen, want de foto
   is het vlak. */
.hero{padding-top:clamp(2.2rem,4.5vw,3.6rem);padding-bottom:0;overflow:hidden}
.hero-in{display:grid;gap:clamp(1.8rem,4vw,3rem)}
@media (min-width:960px){
  .hero-in{grid-template-columns:minmax(0,1fr) minmax(0,1.02fr);align-items:center;
    max-width:var(--max);margin-inline:auto;padding-left:var(--marge)}
  .hero-tekst{padding-block:clamp(2rem,5vw,4.5rem)}
}
@media (max-width:959px){.hero-in{padding-inline:var(--marge)}}
.hero-tekst h1{margin-top:.85rem;max-width:15ch}
.hero-tekst .intro{margin-top:1.15rem}
.hero-tekst .knopgroep{margin-top:1.8rem}
.hero-beeld img{width:100%;aspect-ratio:16/11;object-fit:cover;border-radius:var(--r)}
@media (min-width:960px){
  .hero-beeld{margin-right:calc((100vw - var(--max)) / -2 - var(--marge))}
  .hero-beeld img{aspect-ratio:4/3;border-radius:var(--r) 0 0 var(--r);max-height:32rem}
}

/* ---------- werkgebiedstrip ---------- */
/* De h1 van de home: zoekterm als label, merkzin als grote regel. */
.hero-h1 .label{display:block;margin-bottom:.85rem}
.hero-h1 .display{display:block;font-size:clamp(2.1rem,4.2vw,3.4rem)}

/* ---------- vertrouwen onder de hero ---------- */
.vertrouwen{background:var(--wit);border-bottom:1px solid var(--lijn)}
.vertrouwen-in{display:grid;grid-template-columns:1fr 1fr;list-style:none}
@media (min-width:900px){.vertrouwen-in{grid-template-columns:repeat(4,1fr)}}
.vertrouwen-in li{padding:1.05rem 1rem 1.1rem 0;display:flex;flex-direction:column;gap:.15rem;
  font-size:.86rem;color:var(--inkt-3)}
@media (min-width:900px){.vertrouwen-in li + li{padding-left:1.4rem;border-left:1px solid var(--lijn)}}
@media (max-width:899px){.vertrouwen-in li:nth-child(even){padding-left:1rem;
  border-left:1px solid var(--lijn)}
  .vertrouwen-in li:nth-child(n+3){border-top:1px solid var(--lijn)}}
.vertrouwen-in b{font-family:Supreme,sans-serif;font-weight:700;font-size:1rem;color:var(--inkt)}
.vertrouwen-in a{text-decoration:underline;text-underline-offset:3px}
.sterren{color:#B7791F;letter-spacing:.08em;font-size:.95rem;line-height:1}

/* ---------- CTA die past bij de sectie ---------- */
.ctaregel{margin-top:clamp(1.8rem,3vw,2.4rem);padding-top:1.4rem;border-top:1px solid var(--lijn);
  display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem 1.6rem}
.ctaregel p{font-family:Supreme,sans-serif;font-weight:700;font-size:1.08rem;max-width:40ch}
.sectie--vlak .ctaregel{border-color:rgba(255,255,255,.2)}

.gebied{background:var(--wit);border-bottom:1px solid var(--lijn);padding:.95rem 0}
.gebied-in{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem 1.5rem;font-size:.92rem;
  color:var(--inkt-2)}
.gebied-kop{font-weight:700;color:var(--inkt)}
.gebied-in span:not(.gebied-kop){position:relative;padding-left:.95rem}
.gebied-in span:not(.gebied-kop)::before{content:"";position:absolute;left:0;top:.7em;
  width:7px;height:2px;background:var(--blauw)}

/* ---------- kleurkaarten ----------
   Elke dienst is een staal: een kleurbaan bovenaan, tekst eronder. */
.kaarten{display:grid;gap:clamp(1rem,2vw,1.5rem)}
@media (min-width:760px){.kaarten{grid-template-columns:1fr 1fr}}
@media (min-width:1080px){
  .kaarten{grid-template-columns:repeat(4,1fr)}
  .kaarten--twee{grid-template-columns:1fr 1fr}
}
/* De kaarten liggen als kleurstalen uit een waaier: iets verschoven en
   iets gekanteld, en ze gaan rechtliggen als je erover gaat. */
.kaart{display:flex;flex-direction:column;background:var(--wit);border-radius:var(--r);
  overflow:hidden;border:1px solid var(--lijn);
  transition:transform .35s var(--soepel),box-shadow .35s var(--soepel)}
/* Alleen een lichte draai, geen hoogteverschil: met vier kaarten van
   ongelijke tekstlengte gaat verspringen eruitzien als scheve uitlijning
   in plaats van als een waaier. */
@media (min-width:1080px) and (prefers-reduced-motion:no-preference){
  .kaarten .kaart:nth-child(1){transform:rotate(-.7deg)}
  .kaarten .kaart:nth-child(2){transform:rotate(.45deg)}
  .kaarten .kaart:nth-child(3){transform:rotate(-.35deg)}
  .kaarten .kaart:nth-child(4){transform:rotate(.6deg)}
  .kaarten .kaart:hover{transform:rotate(0) translateY(-5px);z-index:2}
}
.kaart:hover{box-shadow:0 14px 32px rgba(35,38,43,.12)}
.kaart-baan{height:88px;background:var(--blauw);position:relative}
.kaart:nth-child(2) .kaart-baan{background:#2E6DA8}
.kaart:nth-child(3) .kaart-baan{background:#4E7F94}
.kaart:nth-child(4) .kaart-baan{background:#6B7A86}
.kaart-in{padding:1.3rem 1.35rem 1.5rem;display:flex;flex-direction:column;flex:1}
.kaart h3{margin-bottom:.5rem}
.kaart p{color:var(--inkt-2);font-size:.93rem}
.kaart .meer{margin-top:auto;padding-top:1.3rem;font-weight:700;font-size:.9rem;
  color:var(--blauw);display:inline-flex;align-items:center;gap:.45rem}
.kaart:hover .meer{gap:.75rem}
.kaart .meer svg{width:14px;height:9px;transition:transform .25s var(--soepel)}

/* ---------- beeld en tekst ---------- */
.blok{display:grid;gap:clamp(1.5rem,3.5vw,3rem);align-items:center;
  padding-block:clamp(1.6rem,3vw,2.6rem)}
.blok + .blok{border-top:1px solid var(--lijn)}
@media (min-width:900px){
  .blok{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .blok--om .blok-beeld{order:2}
}
.blok-beeld img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--r)}
.punten{margin-top:1.4rem;display:grid;gap:.1rem}
.punten li{position:relative;padding:.45rem 0 .45rem 1.2rem;font-size:.93rem;
  color:var(--inkt-2);border-top:1px solid var(--lijn)}
.punten li::before{content:"";position:absolute;left:0;top:1.1em;width:8px;height:2px;
  background:var(--blauw)}

/* ---------- projecten ---------- */
.werk{display:grid;gap:clamp(1rem,2vw,1.5rem)}
@media (min-width:820px){.werk{grid-template-columns:repeat(3,1fr)}}
.werk figure{border-radius:var(--r);overflow:hidden;background:var(--wit);
  border:1px solid var(--lijn)}
.werk img{width:100%;aspect-ratio:4/3;object-fit:cover}
.werk figcaption{padding:1rem 1.15rem 1.25rem}
.werk h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.02rem}
.werk p{font-size:.89rem;color:var(--inkt-3);margin-top:.2rem}

/* voor en na naast elkaar */
.voorna{display:grid;gap:.9rem}
@media (min-width:700px){.voorna{grid-template-columns:1fr 1fr}}
.voorna img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--r)}
.voorna figcaption{margin-top:.6rem;font-size:.7rem;font-weight:700;letter-spacing:.19em;
  text-transform:uppercase;color:var(--inkt-3)}

/* ---------- werkwijze ---------- */
/* Geen rij van vijf kolommen maar een lopende lijn naar beneden, met
   de stappen om en om aan weerszijden. Een klus is een volgorde, geen
   raster. */
.stappen{position:relative;display:grid;gap:0}
.stappen::before{content:"";position:absolute;left:11px;top:.7rem;bottom:.7rem;width:2px;
  background:var(--lijn-2)}
@media (min-width:900px){.stappen::before{left:50%;transform:translateX(-1px)}}
.stap{position:relative;padding:0 0 2.2rem 2.6rem}
.stap:last-child{padding-bottom:0}
.stap::before{content:"";position:absolute;left:4px;top:.45rem;width:16px;height:16px;
  border-radius:50%;background:var(--papier);border:3px solid var(--blauw)}
@media (min-width:900px){
  .stappen{grid-template-columns:1fr 1fr;column-gap:4rem}
  .stap{padding:0 0 2.6rem}
  .stap:nth-child(odd){grid-column:1;text-align:right;padding-right:2.6rem}
  .stap:nth-child(even){grid-column:2;padding-left:2.6rem;margin-top:5rem}
  .stap::before{left:auto;right:-8px;top:.5rem}
  .stap:nth-child(even)::before{left:-8px;right:auto}
}
.stap b{font-family:Supreme,sans-serif;font-weight:700;font-size:.8rem;letter-spacing:.14em;
  color:var(--blauw);display:block;margin-bottom:.5rem}
.stap h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.05rem;margin-bottom:.35rem}
.stap p{font-size:.92rem;color:var(--inkt-2);max-width:38ch}
@media (min-width:900px){.stap:nth-child(odd) p{margin-left:auto}}

/* ---------- reviews ---------- */
.reviews{display:grid;gap:clamp(1rem,2vw,1.4rem)}
@media (min-width:820px){.reviews{grid-template-columns:repeat(2,1fr)}}
.review{background:var(--wit);border:1px solid var(--lijn);border-radius:var(--r);
  padding:1.5rem 1.5rem 1.6rem;position:relative}
.review::before{content:"";position:absolute;left:0;top:1.5rem;bottom:1.5rem;width:3px;
  background:var(--blauw);border-radius:0 var(--r) var(--r) 0}
.review p{font-size:.98rem}
.review-onder{margin-top:1rem;font-size:.85rem}
.review-onder b{display:block;font-weight:700}
.review-onder span{color:var(--inkt-3)}
.score{display:inline-flex;align-items:baseline;gap:.5rem;background:var(--wit);
  border:1px solid var(--lijn);border-radius:var(--r);padding:.55rem .95rem;font-size:.88rem;
  color:var(--inkt-2)}
.score b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.25rem;color:var(--inkt)}

/* ---------- vragen ---------- */
.vragen{border-top:1px solid var(--lijn)}
.vraag{border-bottom:1px solid var(--lijn)}
.vraag button{width:100%;display:flex;align-items:flex-start;justify-content:space-between;
  gap:1.4rem;padding:1.15rem 0;text-align:left;font-family:Supreme,sans-serif;
  font-weight:700;font-size:1.02rem;line-height:1.35}
.vraag-teken{flex-shrink:0;width:20px;height:20px;position:relative;margin-top:.28rem}
.vraag-teken::before,.vraag-teken::after{content:"";position:absolute;background:var(--blauw);
  transition:transform .25s var(--soepel)}
.vraag-teken::before{left:0;right:0;top:9px;height:2px}
.vraag-teken::after{top:0;bottom:0;left:9px;width:2px}
.vraag[data-open="1"] .vraag-teken::after{transform:scaleY(0)}
.vraag-antwoord{display:none;padding-bottom:1.3rem;color:var(--inkt-2);max-width:66ch}
.vraag[data-open="1"] .vraag-antwoord{display:block}
.markering{background:rgba(20,80,140,.12);color:var(--blauw-2);font-weight:700;
  padding:.05rem .35rem;border-radius:2px;font-size:.86rem}

/* ---------- formulier ---------- */
.velden-2{display:grid;gap:1rem}
@media (min-width:640px){.velden-2{grid-template-columns:1fr 1fr}}
.veld{display:flex;flex-direction:column;gap:.4rem;margin-bottom:1rem}
.veld label{font-size:.86rem;font-weight:700}
.veld input,.veld select,.veld textarea{font:inherit;font-size:.98rem;padding:.75rem .9rem;
  background:var(--wit);border:1px solid var(--lijn-2);border-radius:var(--r);
  color:var(--inkt);width:100%}
.veld textarea{resize:vertical;min-height:6.5rem}
.veld input:focus,.veld select:focus,.veld textarea:focus{outline:2px solid var(--blauw);
  outline-offset:-1px;border-color:var(--blauw)}
.veld .hulp{font-size:.82rem;color:var(--inkt-3)}
.veld .fout{display:none;font-size:.84rem;color:#A32718;font-weight:700}
.veld[data-fout="1"] input,.veld[data-fout="1"] select,.veld[data-fout="1"] textarea{
  border-color:#A32718}
.veld[data-fout="1"] .fout{display:block}
.formulier-noot{font-size:.84rem;color:var(--inkt-3);margin-top:.9rem;max-width:52ch}
.gelukt{display:none;background:var(--wit);border:1px solid var(--lijn-2);border-radius:var(--r);
  padding:clamp(1.4rem,3vw,2rem)}
.gelukt[data-aan="1"]{display:block}
.gelukt b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.2rem;display:block;
  margin-bottom:.5rem}
.sectie--nacht .gelukt{background:#20242A;border-color:#31363E}
/* Versturen mislukt: dit staat pas in beeld als het nodig is. */
.verzendfout{display:none;margin-top:.9rem;font-size:.9rem;font-weight:700;color:#A32718;
  max-width:52ch}
.verzendfout[data-aan="1"]{display:block}
.verzendfout a{text-decoration:underline;text-underline-offset:3px}
.sectie--nacht .verzendfout{color:#FFB4A8}
.knop:disabled{opacity:.7;cursor:progress}
.formulier-noot a{text-decoration:underline;text-underline-offset:3px}
/* Het lokveld voor spambots: buiten beeld, niet te bereiken met tab. */
.honing{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.voet-inline{display:inline !important;padding:0 !important;text-decoration:underline;
  text-underline-offset:3px}

/* ---------- lopende tekst (privacyverklaring) ---------- */
.lopend{max-width:46rem}
.lopend h2{font-family:Supreme,sans-serif;font-weight:700;font-size:1.3rem;margin-top:2.4rem;
  letter-spacing:-.01em}
.lopend p,.lopend ul{margin-top:.8rem;color:var(--inkt-2)}
.lopend ul{list-style:disc;padding-left:1.2rem}
.lopend li{margin-top:.35rem}
.lopend a{color:var(--blauw);text-decoration:underline;text-underline-offset:3px}
.lopend dl{margin-top:.8rem;display:grid;grid-template-columns:max-content 1fr;gap:.3rem 1.2rem;
  color:var(--inkt-2)}
.lopend dt{font-weight:700;color:var(--inkt)}

/* ---------- contactblok ---------- */
.contact{display:grid;gap:clamp(2rem,4vw,3.5rem)}
@media (min-width:940px){.contact{grid-template-columns:1.15fr .85fr}}
.contactrij{display:flex;gap:1rem;padding:.7rem 0;border-bottom:1px solid rgba(243,241,237,.14)}
.contactrij dt{flex:0 0 7.5rem;color:var(--licht-3);font-size:.9rem}
.contactrij dd{font-weight:700}
.contactrij a:hover{color:#7FA9D6}

/* ---------- voet ---------- */
.voet{background:var(--nacht);color:var(--licht-2);padding-block:clamp(3rem,5vw,4.5rem) 2rem;
  font-size:.92rem}
.voet-in{display:grid;gap:2.2rem}
@media (min-width:820px){.voet-in{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.voet-merk{font-family:Supreme,sans-serif;font-weight:700;font-size:1.15rem;color:var(--licht);
  display:block}
.voet-kop{font-weight:700;color:var(--licht);margin-bottom:.7rem;font-size:.9rem}
.voet a{display:block;padding:.22rem 0}
.voet a:hover{color:#7FA9D6}
.voet-onder{margin-top:2.6rem;padding-top:1.3rem;border-top:1px solid rgba(243,241,237,.14);
  display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;justify-content:space-between;font-size:.84rem;
  color:var(--licht-3)}

/* ---------- mobiele balk ---------- */
.balk{position:fixed;left:0;right:0;bottom:0;z-index:45;display:none;gap:.5rem;
  padding:.6rem var(--marge);background:rgba(246,244,240,.96);backdrop-filter:blur(10px);
  border-top:1px solid var(--lijn)}
.balk .knop{flex:1;min-height:48px;padding-inline:.4rem;font-size:.92rem}
@media (max-width:760px){
  .balk{display:flex}body{padding-bottom:5.2rem}
  .contactrij dd a,.klein a,.voorstel a,.voet-onder a,.merk{min-height:44px;
    display:inline-flex;align-items:center}
}

/* ---------- binnenkomen bij scrollen ---------- */
@media (prefers-reduced-motion:no-preference){
  html.js .op{opacity:0;transform:translateY(16px)}
  html.js .op.in{opacity:1;transform:none;
    transition:opacity .7s var(--soepel),transform .7s var(--soepel)}
  html.js [data-stagger]>*{transition-delay:calc(var(--i,0) * 70ms)}
}
"""


# =====================================================================
# Alleen Aflak. Geen Grondlaag met extra pagina's, maar een andere
# uitvoering: kleurvlakken in plaats van een licht papier, groter
# zetwerk, en eigen componenten.
# =====================================================================
AFLAK = r"""
/* =====================================================================
   Aflak zet de snijlijn op paginaformaat. Waar Grondlaag alles op een
   rustig papier houdt, wisselt Aflak grote kleurvlakken af met papier,
   en raken die vlakken elkaar in een harde rand. Dat is precies wat een
   schilder verkoopt: de overgang.
   ===================================================================== */
h1.display{font-size:clamp(2.4rem,5vw,4.2rem);letter-spacing:-.03em}
h2.display{font-size:clamp(2rem,4vw,3.2rem);letter-spacing:-.025em}
.intro{font-size:clamp(1.05rem,1.45vw,1.2rem)}
:root{--lucht:clamp(4.5rem,8.5vw,8.5rem)}

/* Het blauwe vlak. Een hele sectie in kleur, zonder rand eromheen. */
.sectie--vlak{background:var(--blauw);color:#fff}
.sectie--vlak .intro{color:#CFDDEC}
.sectie--vlak .klein{color:#A9C2DC}
.sectie--vlak .label{color:#9EC2E4}
.sectie--vlak .display{color:#fff}
.sectie--vlak .knop--vol{background:#fff;color:var(--blauw);border-color:#fff}
.sectie--vlak .knop--vol:hover{background:var(--licht);border-color:var(--licht)}
.sectie--vlak .knop--lijn{color:#fff;border-color:rgba(255,255,255,.42)}
.sectie--vlak .knop--lijn:hover{border-color:#fff;background:rgba(255,255,255,.1)}
.sectie--vlak .punten li{color:#CFDDEC;border-color:rgba(255,255,255,.2)}
.sectie--vlak .punten li::before{background:#fff}
.sectie--vlak .vragen,.sectie--vlak .vraag{border-color:rgba(255,255,255,.2)}
.sectie--vlak .vraag-antwoord{color:#CFDDEC}
.sectie--vlak .vraag-teken::before,.sectie--vlak .vraag-teken::after{background:#fff}
.sectie--vlak .markering{background:rgba(255,255,255,.18);color:#fff}
.sectie--vlak .rail-kop{border-top-color:#fff}
.sectie--vlak .rail-naam{color:#fff}
.sectie--vlak .rail-kop p{color:#C4DAF0}
.sectie--vlak .stappen::before{background:rgba(255,255,255,.3)}
.sectie--vlak .stap::before{background:var(--blauw);border-color:#fff}
.sectie--vlak .stap b{color:#C4DAF0}
.sectie--vlak .stap h3{color:#fff}
.sectie--vlak .stap p{color:#CFDDEC}
.sectie--vlak .review{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.2)}
.sectie--vlak .review p{color:#fff}
.sectie--vlak .review::before{background:#fff}
.sectie--vlak .review-onder span{color:#A9C2DC}
.sectie--vlak .score{background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.24);
  color:#CFDDEC}
.sectie--vlak .score b{color:#fff}
.tape{background:var(--blauw);border-bottom-color:var(--blauw)}

/* ---------- films en beelden over de volle breedte ----------
   De Higgsfield-films. Een poster staat er altijd; de film zelf laadt
   pas als hij in beeld komt, en met minder beweging blijft de poster. */
.film{position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--nacht)}
.film video,.film img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}

.hero--film{position:relative;min-height:min(86svh,48rem);display:flex;align-items:flex-end;
  overflow:hidden;padding-block:clamp(3rem,6vw,5rem);background:var(--nacht);isolation:isolate}
.hero--film .wrap{position:relative;z-index:3;width:100%}
.hero--film::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(0deg,rgba(12,16,22,.82) 0%,rgba(12,16,22,.38) 38%,rgba(12,16,22,0) 64%),
    linear-gradient(90deg,rgba(12,16,22,.62) 0%,rgba(12,16,22,.18) 52%,rgba(12,16,22,0) 78%)}
.hero--film h1{color:#fff;margin-top:.8rem;max-width:16ch;
  text-shadow:0 2px 30px rgba(10,14,20,.45)}
.hero--film .intro{margin-top:1.1rem;max-width:44ch;color:#E4E8ED;
  text-shadow:0 1px 16px rgba(10,14,20,.5)}
.hero--film .label{color:#B5D2EE}
.hero--film .label a{border-bottom:1px solid currentColor}
.hero--film .knopgroep{margin-top:1.8rem}
.hero--film .knop--vol{background:#fff;color:var(--blauw);border-color:#fff}
.hero--film .knop--vol:hover{background:var(--licht);border-color:var(--licht)}
.hero--film .knop--lijn{color:#fff;border-color:rgba(255,255,255,.55);
  background:rgba(10,14,20,.28);backdrop-filter:blur(3px)}
.hero--film .knop--lijn:hover{border-color:#fff;background:rgba(10,14,20,.45)}

/* De home: de blauwe helft van de muur moet blauw blijven, dus alleen
   onderaan een lichte waas voor de knoppen. Op mobiel valt de witte helft
   achter de tekst, daar is de waas steviger. */
.hero--home{min-height:min(90svh,52rem)}
.hero--home::after{background:
    linear-gradient(0deg,rgba(9,28,50,.7) 0%,rgba(9,28,50,.2) 34%,rgba(9,28,50,0) 58%),
    linear-gradient(90deg,rgba(9,28,50,.35) 0%,rgba(9,28,50,0) 46%)}
@media (max-width:760px){
  .hero--home .film video,.hero--home .film img{object-position:30% 50%}
  .hero--home::after{background:
    linear-gradient(0deg,rgba(9,28,50,.92) 0%,rgba(9,28,50,.7) 42%,rgba(9,28,50,.1) 72%)}
}
.hero--film .hero-h1{max-width:none}
.hero--film .hero-h1 .display{font-size:clamp(2.3rem,4.4vw,3.7rem);max-width:21ch;color:#fff}
.hero--kort{min-height:min(62svh,34rem)}
.hero--dienst{min-height:min(78svh,42rem)}
/* Op een telefoon moeten de knoppen in beeld staan zonder te scrollen. */
@media (max-width:760px){.hero--film,.hero--home,.hero--dienst{min-height:68svh}
  .hero--kort{min-height:52svh}}

/* Heel licht inzoomen terwijl de kop wegscrolt: diepte, geen spektakel. */
@supports (animation-timeline:view()){
  @media (prefers-reduced-motion:no-preference){
    .film--hero video,.film--hero img{animation:filmzoom linear both;
      animation-timeline:view();animation-range:exit 0% exit 100%}
    @keyframes filmzoom{to{transform:scale(1.08)}}
  }
}

/* ---------- de voor-en-na schuif ---------- */
.schuif-na{clip-path:inset(0 0 0 var(--x,50%))}
.schuif-greep{position:absolute;top:0;bottom:0;z-index:4;width:2px;background:rgba(255,255,255,.9);
  left:var(--x,50%);transform:translateX(-1px);cursor:ew-resize;touch-action:none}
.schuif-greep::after{content:"";position:absolute;top:50%;left:50%;width:46px;height:46px;
  transform:translate(-50%,-50%);border:2px solid rgba(255,255,255,.9);border-radius:50%;
  background:rgba(12,16,22,.32);backdrop-filter:blur(3px)}
.schuif-greep::before{content:"";position:absolute;top:50%;left:50%;width:16px;height:8px;
  transform:translate(-50%,-50%);z-index:1;
  background:linear-gradient(90deg,#fff 0 2px,transparent 2px 6px,#fff 6px 8px,
             transparent 8px 10px,#fff 10px 12px,transparent 12px 14px,#fff 14px 16px)}
.schuif-merk{position:absolute;z-index:4;top:calc(50% + 44px);font-size:.68rem;font-weight:700;
  letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.94);
  text-shadow:0 1px 8px rgba(0,0,0,.75);pointer-events:none}
.schuif-merk--voor{left:1.2rem}
.schuif-merk--na{right:1.2rem}
@media (max-width:760px){.schuif-merk{top:calc(50% + 38px);font-size:.62rem}}
.vergelijk{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--zand);
  border-radius:var(--r);touch-action:pan-y}
.vergelijk img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}

/* ---------- kleurkiezer ----------
   Waar mensen bij een schilder over twijfelen is de kleur. Klikken zet
   de richting vast en die gaat mee in de aanvraag. */
.stalen{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--lijn);
  border:1px solid var(--lijn);border-radius:var(--r);overflow:hidden}
@media (min-width:700px){.stalen{grid-template-columns:repeat(4,1fr)}}
.staal{position:relative;display:block;width:100%;text-align:left;background:var(--wit);
  transition:background .2s}
.staal:hover{background:var(--papier)}
.staal-vlak{height:120px;display:block}
.staal-in{padding:.9rem 1.05rem 1.2rem}
.staal b{display:block;font-family:Supreme,sans-serif;font-weight:700;font-size:.98rem}
.staal small{display:block;font-size:.85rem;color:var(--inkt-3);margin-top:.15rem}
.staal[aria-pressed="true"]{background:var(--papier)}
.staal[aria-pressed="true"]::after{content:"";position:absolute;inset:0;
  border:3px solid var(--blauw);border-radius:var(--r);pointer-events:none}
.stalen-uit{display:none;margin-top:1.5rem;background:var(--nacht);color:var(--licht);
  border-radius:var(--r);padding:clamp(1.4rem,3vw,2.1rem)}
.stalen-uit[data-aan="1"]{display:block}
.stalen-uit b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.2rem;color:#fff;
  display:block;margin-bottom:.5rem}
.stalen-uit p{color:var(--licht-2);max-width:58ch}
.stalen-uit .knopgroep{margin-top:1.3rem}
.stalen-uit .knop--vol{background:#fff;color:var(--nacht);border-color:#fff}
.stalen-uit .knop--lijn{color:#fff;border-color:rgba(255,255,255,.4)}

/* ---------- stappenflow ---------- */
.flow{background:var(--wit);border:1px solid var(--lijn-2);border-radius:var(--r);
  padding:clamp(1.4rem,3vw,2.2rem)}
.flow-top{display:flex;align-items:center;justify-content:space-between;gap:1rem;
  margin-bottom:.9rem}
.flow-telling{font-size:.78rem;color:var(--inkt-3);font-variant-numeric:tabular-nums;
  font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.flow-terug{font-size:.86rem;color:var(--inkt-2);text-decoration:underline;
  text-underline-offset:3px;min-height:32px}
.flow-terug[hidden]{display:none}
.flow-balk{height:3px;background:var(--lijn);margin-bottom:1.5rem;border-radius:2px}
.flow-balk i{display:block;height:100%;background:var(--blauw);border-radius:2px;
  transition:width .35s var(--soepel)}
[data-stap]{display:none}
[data-stap][data-aan="1"]{display:block}
[data-stap] h3{margin-bottom:1.1rem}
.keuzes{display:grid;gap:.5rem}
@media (min-width:600px){.keuzes--2{grid-template-columns:1fr 1fr}}
.keuze{display:block;width:100%;text-align:left;padding:.9rem 1.1rem;background:var(--papier);
  border:1px solid var(--lijn-2);border-radius:var(--r);font-weight:700;font-size:.95rem;
  min-height:50px;transition:border-color .18s,background .18s}
.keuze:hover{border-color:var(--blauw);background:var(--blauw-3)}
.keuze small{display:block;margin-top:.15rem;font-size:.83rem;font-weight:400;
  color:var(--inkt-3)}
.flow-klaar{display:none;background:var(--nacht);color:var(--licht);margin:-1px;
  border-radius:var(--r);padding:clamp(1.5rem,3vw,2.2rem)}
.flow-klaar[data-aan="1"]{display:block}
.flow-klaar b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.22rem;color:#fff;
  display:block;margin-bottom:.5rem}
.flow-klaar p{color:var(--licht-2)}
.flow-klaar .knop--vol{background:#fff;color:var(--nacht);border-color:#fff}
.flow-samen{margin:1rem 0 1.2rem;display:flex;flex-wrap:wrap;gap:.4rem}
.flow-samen span{border:1px solid rgba(243,241,237,.3);border-radius:2px;padding:.28rem .7rem;
  font-size:.85rem;color:var(--licht)}

/* ---------- regio ---------- */
.regio-lijst{display:grid;gap:1px;background:var(--lijn);border:1px solid var(--lijn);
  border-radius:var(--r);overflow:hidden}
@media (min-width:640px){.regio-lijst{grid-template-columns:1fr 1fr}}
@media (min-width:1000px){.regio-lijst{grid-template-columns:repeat(4,1fr)}}
.regio-lijst a{background:var(--wit);padding:1.3rem;transition:background .2s}
.regio-lijst a:hover{background:var(--blauw-3)}
.regio-lijst b{font-family:Supreme,sans-serif;font-weight:700;font-size:1.08rem;display:block;
  margin-bottom:.3rem}
.regio-lijst span{font-size:.88rem;color:var(--inkt-3)}

/* ---------- dienstkaarten met film ----------
   De kleurbaan wordt een smalle staalstreep onder een filmpje dat gaat
   lopen als je erover gaat. Op een telefoon loopt het als het in beeld is. */
/* Met een film erin zijn vier kolommen naast de rail te smal: dan twee
   bij twee, en drie naast elkaar alleen als het er precies drie zijn. */
@media (min-width:1080px){
  .kaarten{grid-template-columns:1fr 1fr}
  .kaarten--drie{grid-template-columns:repeat(3,1fr)}
}
.kaart-media{position:relative;display:block;aspect-ratio:16/9;overflow:hidden;
  background:var(--nacht)}
.rail-in > .vergelijk{margin-top:clamp(1.6rem,3vw,2.4rem)}
.vergelijk + .werk{margin-top:clamp(1rem,2vw,1.5rem)}
.kaart-film{position:absolute;inset:0}
.kaart-film video{width:100%;height:100%;object-fit:cover;display:block;
  transition:transform .9s var(--soepel)}
.kaart:hover .kaart-film video{transform:scale(1.045)}
.kaart-media + .kaart-baan{height:6px}

/* ---------- kleurkiezer met beeld ---------- */
.kiezer{display:grid;gap:clamp(1.2rem,2.6vw,2.2rem)}
@media (min-width:900px){.kiezer{grid-template-columns:minmax(0,1.08fr) minmax(0,1fr);
  align-items:start}}
.kiezer-vlak{position:relative;aspect-ratio:4/3;border-radius:var(--r);overflow:hidden;
  background:var(--zand)}
.kiezer-vlak img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;
  transform:scale(1.035);transition:opacity .55s var(--soepel),transform 1.4s var(--soepel)}
.kiezer-vlak img[data-aan="1"]{opacity:1;transform:none}
.kiezer-beeld figcaption{font-size:.8rem;color:var(--inkt-3);margin-top:.55rem}
@media (min-width:900px){.kiezer-beeld{position:sticky;top:6.5rem}}
.kiezer .stalen{grid-template-columns:repeat(2,1fr)}
.kiezer .staal-vlak{height:92px}
.kiezer .stalen-uit{margin-top:1rem}

/* ---------- werkwijze met beelden ---------- */
.stap-beeld{width:100%;max-width:24rem;aspect-ratio:4/3;object-fit:cover;
  border-radius:var(--r);margin-bottom:1.1rem;box-shadow:0 18px 40px rgba(6,22,40,.28)}
@media (min-width:900px){
  .stappen--beeld .stap:nth-child(odd) .stap-beeld{margin-left:auto}
  .stappen--beeld .stap:nth-child(even){margin-top:9rem}
  .stappen--beeld .stap{padding-bottom:3.2rem}
}

/* ---------- contactblok met film ----------
   Een woning in de schemer die in het donker van de sectie overloopt. */
.sectie--film{position:relative;overflow:hidden;isolation:isolate;
  padding-top:clamp(15rem,34vw,28rem)}
.film--contact{bottom:auto;height:clamp(24rem,50vw,42rem)}
.film--contact::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(23,26,31,.1) 0%,rgba(23,26,31,.3) 45%,
             rgba(23,26,31,.85) 80%,var(--nacht) 100%)}
.sectie--film > .wrap{position:relative;z-index:2}
.sectie--film .sectie-kop .display{color:#fff;text-shadow:0 2px 24px rgba(10,14,20,.5)}

/* ---------- beheer: project toevoegen ---------- */
.beheer-voorbeeld{background:var(--blauw-3);border-left:4px solid var(--blauw);color:var(--inkt);
  padding:.9rem 1.1rem;border-radius:var(--r);font-size:.93rem;margin-bottom:1.8rem}
.vink{display:flex;align-items:flex-start;gap:.65rem;margin-top:.9rem;font-size:.95rem;
  cursor:pointer;min-height:44px}
.vink input{width:1.2rem;height:1.2rem;margin-top:.15rem;accent-color:var(--blauw);flex-shrink:0}
.vink-fout{display:none;font-size:.84rem;color:#A32718;font-weight:700;margin-top:.1rem}
.vink-fout[data-aan="1"]{display:block}
.veld input[type="file"]{padding:.6rem;background:var(--papier)}
.beheer-kaart{margin-top:2rem;background:var(--wit);border:1px solid var(--lijn);
  border-radius:var(--r);padding:clamp(1.3rem,3vw,2rem)}
.beheer-kaart h2{font-size:clamp(1.5rem,3vw,2.1rem);margin-top:.5rem}
.beheer-kaart h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1rem;margin-top:1.3rem}
.beheer-kaart p{color:var(--inkt-2);margin-top:.3rem}
.beheer-fotos{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-top:1.2rem}
.beheer-fotos img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--r);
  background:var(--zand)}
.beheer-fotos figcaption{font-size:.7rem;font-weight:700;letter-spacing:.19em;
  text-transform:uppercase;color:var(--inkt-3);margin-top:.4rem}
.beheer .gelukt{margin-top:1.4rem}

/* ---------- alle werkzaamheden in een oogopslag ---------- */
.werkzaamheden{margin-top:clamp(1.6rem,3vw,2.2rem);background:var(--wit);border:1px solid var(--lijn);
  border-radius:var(--r);padding:clamp(1.2rem,2.6vw,1.7rem)}
.werkzaamheden h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.05rem}
.werkzaamheden ul{margin-top:.8rem;display:grid;gap:0 1.6rem}
@media (min-width:640px){.werkzaamheden ul{grid-template-columns:1fr 1fr}}
.werkzaamheden li{border-top:1px solid var(--lijn)}
.werkzaamheden li a,.werkzaamheden li:not(:has(a)){display:flex;align-items:center;
  justify-content:space-between;gap:.8rem;padding:.6rem 0;font-size:.95rem;font-weight:500}
.werkzaamheden li a{color:var(--inkt)}
.werkzaamheden li a svg{width:14px;height:9px;flex-shrink:0;color:var(--blauw);
  transition:transform .25s var(--soepel)}
.werkzaamheden li a:hover{color:var(--blauw)}
.werkzaamheden li a:hover svg{transform:translateX(3px)}
.werkzaamheden p{margin-top:.8rem;font-size:.85rem;color:var(--inkt-3)}
.werkzaamheden--intro{max-width:52rem}

/* ---------- specialismen op de dienstenpagina ---------- */
.speci{display:grid;gap:clamp(1rem,2vw,1.5rem);margin-top:clamp(1.4rem,3vw,2rem)}
@media (min-width:760px){.speci{grid-template-columns:1fr 1fr}}
.speci-kaart{display:flex;flex-direction:column;background:var(--wit);border:1px solid var(--lijn);
  border-radius:var(--r);overflow:hidden;transition:box-shadow .35s var(--soepel)}
.speci-kaart:hover{box-shadow:0 14px 32px rgba(35,38,43,.12)}
.speci-kaart img{width:100%;aspect-ratio:16/9;object-fit:cover}
.speci-kaart > span{padding:1.2rem 1.3rem 1.4rem;display:flex;flex-direction:column;gap:.45rem}
.speci-kaart p{color:var(--inkt-2);font-size:.93rem}
.speci-kaart .meer{font-weight:700;font-size:.9rem;color:var(--blauw);display:inline-flex;
  align-items:center;gap:.45rem;margin-top:.4rem}
.speci-kaart .meer svg{width:14px;height:9px}
.zie-ook{margin-top:1.3rem;font-size:.92rem;color:var(--inkt-3);display:flex;flex-wrap:wrap;
  gap:.3rem 1.2rem;align-items:center}
.zie-ook a{color:var(--blauw);font-weight:700;display:inline-flex;align-items:center;gap:.4rem}
.zie-ook a svg{width:14px;height:9px}
.punten--twee{display:grid;margin-top:clamp(1.2rem,2.5vw,1.6rem)}
@media (min-width:760px){.punten--twee{grid-template-columns:1fr 1fr;column-gap:2rem}}

/* ---------- dienstpagina: kennis voor de aanvraag ----------
   Drie vormen, zodat de pagina niet een rij gelijke blokken wordt:
   wanneer als drie kolommen met een blauwe streep, signalen als
   afvinklijst op wit, materiaal als genummerde rij op zand, kosten als
   genummerde lijst. */
.kennis{display:grid;gap:clamp(1.2rem,2.5vw,2rem);margin-top:clamp(1.6rem,3vw,2.2rem)}
@media (min-width:820px){.kennis{grid-template-columns:repeat(3,1fr)}}
.kennis > div{border-top:3px solid var(--blauw);padding-top:1rem}
.kennis h3,.materiaal h3{font-family:Supreme,sans-serif;font-weight:700;font-size:1.05rem}
.kennis p,.materiaal p{color:var(--inkt-2);font-size:.95rem;margin-top:.4rem}
.signalen{margin-top:clamp(1.8rem,3vw,2.4rem);background:var(--wit);border:1px solid var(--lijn);
  border-radius:var(--r);padding:clamp(1.3rem,3vw,2rem)}
.signalen h3{font-size:clamp(1.15rem,1.8vw,1.35rem)}
.signalen ul{margin-top:1rem;display:grid;gap:.55rem}
@media (min-width:820px){.signalen ul{grid-template-columns:1fr 1fr;column-gap:2rem}}
.signalen li{position:relative;padding-left:1.7rem;color:var(--inkt-2);font-size:.95rem}
.signalen li::before{content:"";position:absolute;left:.3rem;top:.12em;width:.5rem;height:.9rem;
  border:solid var(--blauw);border-width:0 2px 2px 0;transform:rotate(45deg)}
.materiaal{display:grid;gap:1px;background:var(--lijn-2);border:1px solid var(--lijn-2);
  border-radius:var(--r);overflow:hidden;margin-top:clamp(1.6rem,3vw,2.2rem);counter-reset:m}
@media (min-width:820px){.materiaal{grid-template-columns:repeat(3,1fr)}}
.materiaal > div{background:var(--zand);padding:1.3rem 1.3rem 1.5rem;counter-increment:m}
.materiaal > div::before{content:counter(m, decimal-leading-zero);display:block;
  font-family:Supreme,sans-serif;font-weight:700;color:var(--blauw);font-size:.85rem;
  letter-spacing:.1em;margin-bottom:.6rem}
.kosten{margin-top:clamp(1.4rem,3vw,2rem);counter-reset:k;display:grid;gap:0;max-width:44rem}
.kosten li{counter-increment:k;display:grid;grid-template-columns:2.6rem 1fr;align-items:baseline;
  padding:.8rem 0;border-bottom:1px solid var(--lijn);color:var(--inkt)}
.kosten li::before{content:counter(k);font-family:Supreme,sans-serif;font-weight:700;
  font-size:1.35rem;color:var(--blauw)}
.reviews--een{max-width:34rem;grid-template-columns:1fr !important}
.werk--lokaal{margin-block:clamp(1.4rem,3vw,2rem) clamp(1.2rem,2.5vw,1.8rem)}
@media (min-width:820px){.werk--lokaal{grid-template-columns:minmax(0,26rem)}}

/* ---------- over Ahmad en zakelijk ----------
   Links wie er komt, rechts een wit paneel voor aannemers en architecten. */
.over{display:grid;gap:clamp(1.8rem,4vw,3.4rem)}
@media (min-width:1000px){.over{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);
  align-items:start}}
.over-tekst h2.display{font-size:clamp(1.8rem,2.9vw,2.45rem);max-width:20ch}
.over-tekst p{margin-top:1rem;color:var(--inkt-2);max-width:58ch}
.over-tekst .intro{margin-top:1.1rem;color:var(--inkt)}
.over-naam{font-family:Supreme,sans-serif;font-weight:700;color:var(--inkt) !important;
  padding-top:.9rem;border-top:2px solid var(--blauw);display:inline-block}
.zakelijk{background:var(--wit);border:1px solid var(--lijn);border-radius:var(--r);
  padding:clamp(1.4rem,3vw,2rem);position:relative;overflow:hidden}
.zakelijk::before{content:"";position:absolute;left:0;right:0;top:0;height:6px;
  background:var(--blauw)}
.zakelijk p{color:var(--inkt-2);margin-top:.6rem;font-size:.95rem}
.zakelijk .knopgroep{margin-top:1.4rem}
.regio-lijst div{background:var(--wit);padding:1.3rem}
/* Plaatsen met een eigen pagina herken je aan de blauwe naam en de pijl. */
.regio-lijst a b{color:var(--blauw);display:flex;align-items:center;gap:.45rem}
.regio-lijst a b svg{width:14px;height:9px;transition:transform .25s var(--soepel)}
.regio-lijst a:hover b svg{transform:translateX(3px)}
.voorna-kop{margin-top:clamp(2.4rem,4vw,3.2rem)}
.voorna-kop + .klein{margin-top:.25rem}

/* ---------- offerte: kaart over de kop heen ---------- */
.hero--kort{padding-bottom:clamp(4rem,7vw,6rem)}
.sectie--flow{padding-top:0;margin-top:clamp(-3.5rem,-4vw,-2rem);position:relative;z-index:4}
.sectie--flow .flow{box-shadow:0 24px 60px rgba(23,26,31,.16)}
.keuze--beeld{display:grid;grid-template-columns:4.4rem minmax(0,1fr);align-items:center;
  gap:.95rem;padding:.45rem 1rem .45rem .45rem}
.keuze--beeld img{width:4.4rem;height:3.3rem;object-fit:cover;border-radius:2px}
"""


def blad(variant):
    css = BASIS
    if variant == "aflak":
        css += AFLAK
    return css
