/* Een projectpagina: /projecten/<slug>
 *
 * Het bouwscript maakt project-sjabloon.html met lege plekken; hier wordt
 * die gevuld met het project uit de database. Zo is een projectpagina
 * gewone HTML met alle tekst erin, en hoeft er niets opnieuw gebouwd te
 * worden als Ahmad een project toevoegt.
 */

function veilig(t) {
  return String(t == null ? "" : t)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

const MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus",
                 "september", "oktober", "november", "december"];

function maand(w) {
  if (!w || !/^\d{4}-\d{2}$/.test(w)) return "";
  const [jaar, m] = w.split("-");
  return `${MAANDEN[Number(m) - 1]} ${jaar}`;
}

export async function onRequest(context) {
  const { params, env, request } = context;
  if (!env.DB) return new Response("Nog niet beschikbaar", { status: 503 });

  const project = await env.DB.prepare(
    "SELECT * FROM projecten WHERE slug = ? AND zichtbaar = 1").bind(params.slug).first();
  if (!project) return Response.redirect(new URL("/werk.html", request.url).toString(), 302);

  const url = new URL(request.url);
  const sjabloon = await env.ASSETS.fetch(new URL("/project-sjabloon.html", url.origin));
  if (!sjabloon.ok) return new Response("Sjabloon ontbreekt", { status: 500 });

  const meta = [project.dienst, project.plaats, maand(project.wanneer)].filter(Boolean).join(" · ");
  const samenvatting = [project.dienst, project.plaats ? "in " + project.plaats : ""]
    .filter(Boolean).join(" ");
  const extra = JSON.parse(project.extra || "[]");
  const tekst = {
    titel: project.titel,
    samenvatting: samenvatting || project.titel,
    meta: meta || "Aribouw",
    situatie: project.situatie || "",
    aanpak: project.aanpak || "",
    resultaat: project.resultaat || "",
  };

  const rewriter = new HTMLRewriter()
    .on("title", { element(el) { el.setInnerContent(`${project.titel} | Aribouw`); } })
    .on('meta[name="description"]', {
      element(el) {
        el.setAttribute("content",
          `${project.titel}. ${(project.situatie || "").slice(0, 110)}`.trim());
      },
    })
    .on('meta[name="robots"]', { element(el) { el.setAttribute("content", "index,follow"); } })
    .on('link[rel="canonical"], meta[property="og:url"]', {
      element(el) {
        const naam = el.tagName === "link" ? "href" : "content";
        el.setAttribute(naam, `${url.origin}/projecten/${project.slug}`);
      },
    })
    .on("[data-p]", {
      element(el) {
        const sleutel = el.getAttribute("data-p");
        const waarde = tekst[sleutel];
        if (waarde) el.setInnerContent(waarde, { html: false });
        else if (sleutel === "resultaat") el.remove();
      },
    })
    .on("[data-p-src]", {
      element(el) {
        const welk = el.getAttribute("data-p-src");
        el.setAttribute("src", `/media/${welk === "voor" ? project.voor : project.na}`);
        el.setAttribute("alt", `${project.titel}, ${welk}`);
      },
    })
    .on("[data-p-extra]", {
      element(el) {
        if (!extra.length) return;
        el.removeAttribute("hidden");
        el.setInnerContent(extra.map((s) =>
          `<figure><img src="/media/${veilig(s)}" loading="lazy" width="1000" height="750" ` +
          `alt="${veilig(project.titel)}, detail"></figure>`).join(""), { html: true });
      },
    })
    .on("[data-p-links]", {
      element(el) {
        const links = [];
        if (project.dienst) {
          links.push(`<a href="/diensten.html">${veilig(project.dienst)}</a>`);
        }
        if (project.plaats) {
          links.push(`<a href="/werkgebied.html">Schilder in ${veilig(project.plaats)}</a>`);
        }
        links.push('<a href="/offerte.html">Offerte aanvragen</a>');
        el.setInnerContent(links.join(" "), { html: true });
      },
    });

  return rewriter.transform(new Response(sjabloon.body, {
    headers: { "content-type": "text/html; charset=utf-8" },
  }));
}
