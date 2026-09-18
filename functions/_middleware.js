/* Zet de aanpassingen uit het beheerscherm in de pagina's.
 *
 * De site blijft statisch: het bouwscript maakt gewone HTML, en deze laag
 * vervangt onderweg alleen wat Ahmad heeft aangepast. Dat betekent dat de
 * volledige tekst in de HTML staat (goed voor Google en snel), terwijl een
 * wijziging meteen zichtbaar is.
 *
 *   [data-tekst="sleutel"]   vervangen door de aangepaste tekst
 *   [data-blok="reviews"]    eigen reviews erbij
 *   [data-blok="werk"]       eigen projecten erbij, nieuwste eerst
 */

function veilig(t) {
  return String(t == null ? "" : t)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function reviewKaart(r) {
  return `<blockquote class="review"><p>${veilig(r.tekst)}</p>` +
    `<div class="review-onder"><b>${veilig(r.wie)}</b><span>${veilig(r.wat || "")}</span></div>` +
    `</blockquote>`;
}

function projectKaart(p) {
  const titel = veilig(p.titel);
  const onder = veilig([p.dienst, p.plaats].filter(Boolean).join(", "));
  return `<figure><a href="/projecten/${veilig(p.slug)}">` +
    `<img src="/media/${veilig(p.na)}" width="1000" height="750" loading="lazy" alt="${titel}">` +
    `</a><figcaption><h3><a href="/projecten/${veilig(p.slug)}">${titel}</a></h3>` +
    `<p>${onder}</p></figcaption></figure>`;
}

export async function onRequest(context) {
  const { request, next, env } = context;
  const url = new URL(request.url);

  // Foto's uit de opslag.
  if (url.pathname.startsWith("/media/") && env.MEDIA) {
    const sleutel = decodeURIComponent(url.pathname.slice("/media/".length));
    const object = await env.MEDIA.get(sleutel);
    if (!object) return new Response("Niet gevonden", { status: 404 });
    return new Response(object.body, {
      headers: {
        "content-type": object.httpMetadata?.contentType || "image/jpeg",
        "cache-control": "public, max-age=31536000, immutable",
      },
    });
  }

  const antwoord = await next();
  const type = antwoord.headers.get("content-type") || "";
  if (!type.includes("text/html") || !env.DB) return antwoord;
  if (url.pathname === "/beheer.html" || url.pathname === "/beheer") return antwoord;

  let teksten = {}, reviews = [], projecten = [];
  try {
    const [t, r, p] = await Promise.all([
      env.DB.prepare("SELECT sleutel, waarde FROM teksten").all(),
      env.DB.prepare("SELECT * FROM reviews WHERE zichtbaar = 1 ORDER BY id DESC LIMIT 12").all(),
      env.DB.prepare("SELECT * FROM projecten WHERE zichtbaar = 1 ORDER BY id DESC LIMIT 24").all(),
    ]);
    for (const rij of t.results || []) teksten[rij.sleutel] = rij.waarde;
    reviews = r.results || [];
    projecten = p.results || [];
  } catch (e) {
    return antwoord; // database nog niet klaar: gewoon de gemaakte pagina tonen
  }

  const rewriter = new HTMLRewriter()
    .on("[data-tekst]", {
      element(el) {
        const sleutel = el.getAttribute("data-tekst");
        if (teksten[sleutel]) el.setInnerContent(teksten[sleutel], { html: false });
      },
    })
    .on('[data-blok="reviews"]', {
      element(el) {
        if (reviews.length) el.prepend(reviews.map(reviewKaart).join(""), { html: true });
      },
    })
    .on('[data-blok="werk"]', {
      element(el) {
        if (projecten.length) el.prepend(projecten.map(projectKaart).join(""), { html: true });
      },
    });

  return rewriter.transform(new Response(antwoord.body, antwoord));
}
