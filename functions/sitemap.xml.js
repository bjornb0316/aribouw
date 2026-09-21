/* De sitemap: de vaste pagina's uit het bouwscript plus de projecten die
 * Ahmad zelf heeft toegevoegd. */
import { SITE } from "./_site.js";

export async function onRequest({ request, env }) {
  const url = new URL(request.url);
  const vast = await env.ASSETS.fetch(new URL("/sitemap.xml", url.origin));
  let xml = await vast.text();

  if (env.DB) {
    try {
      const { results } = await env.DB.prepare(
        "SELECT slug, gemaakt FROM projecten WHERE zichtbaar = 1 ORDER BY id DESC").all();
      const extra = (results || []).map((p) =>
        `  <url><loc>${SITE}/projecten/${p.slug}</loc>` +
        `<lastmod>${(p.gemaakt || "").slice(0, 10)}</lastmod><priority>0.6</priority></url>`
      ).join("\n");
      if (extra) xml = xml.replace("</urlset>", extra + "\n</urlset>");
    } catch (e) { /* zonder database gewoon de vaste sitemap */ }
  }
  return new Response(xml, { headers: { "content-type": "application/xml; charset=utf-8" } });
}
