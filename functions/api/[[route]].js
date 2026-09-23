/* De API achter het beheerscherm.
 *
 * Alles wat Ahmad aanpast loopt hierlangs: teksten, reviews, projecten,
 * foto's en de aanvragen die binnenkomen. Inloggen gaat met een pincode
 * (omgevingsvariabele BEHEER_PIN); daarna staat er een ondertekend koekje
 * in de browser. De server is de waarheid: elke schrijfactie controleert
 * dat koekje opnieuw.
 *
 * Bindings die Pages moet hebben: DB (D1), MEDIA (R2).
 */

import { mailAanvraag } from "../_mail.js";

const JSON_KOP ={ "content-type": "application/json; charset=utf-8" };

function antwoord(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), { status, headers: { ...JSON_KOP, ...extra } });
}

/* ---- sessie ---- */
async function handtekening(waarde, geheim) {
  const sleutel = await crypto.subtle.importKey(
    "raw", new TextEncoder().encode(geheim),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const ruw = await crypto.subtle.sign("HMAC", sleutel, new TextEncoder().encode(waarde));
  return [...new Uint8Array(ruw)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function maakKoekje(env) {
  const tot = Date.now() + 30 * 24 * 60 * 60 * 1000;
  const waarde = String(tot);
  const sig = await handtekening(waarde, env.SESSIE_GEHEIM || env.BEHEER_PIN || "geheim");
  return `ab_sessie=${waarde}.${sig}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${30 * 24 * 60 * 60}`;
}

export async function ingelogd(request, env) {
  const koek = (request.headers.get("cookie") || "")
    .split(";").map((s) => s.trim()).find((s) => s.startsWith("ab_sessie="));
  if (!koek) return false;
  const [waarde, sig] = koek.slice("ab_sessie=".length).split(".");
  if (!waarde || !sig) return false;
  if (Number(waarde) < Date.now()) return false;
  const juist = await handtekening(waarde, env.SESSIE_GEHEIM || env.BEHEER_PIN || "geheim");
  // Vergelijking in vaste tijd, zodat gokken niets oplevert.
  if (sig.length !== juist.length) return false;
  let verschil = 0;
  for (let i = 0; i < sig.length; i++) verschil |= sig.charCodeAt(i) ^ juist.charCodeAt(i);
  return verschil === 0;
}

/* ---- hulp ---- */
function slugify(t) {
  return (t || "project").toLowerCase()
    .replace(/[àáâä]/g, "a").replace(/[èéêë]/g, "e").replace(/[ìíîï]/g, "i")
    .replace(/[òóôö]/g, "o").replace(/[ùúûü]/g, "u").replace(/ij/g, "ij")
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "project";
}

async function vrijeSlug(db, basis, id) {
  let slug = basis, n = 2;
  while (true) {
    const rij = await db.prepare("SELECT id FROM projecten WHERE slug = ?").bind(slug).first();
    if (!rij || (id && rij.id === id)) return slug;
    slug = `${basis}-${n++}`;
  }
}

const nu = () => new Date().toISOString();

export async function onRequest(context) {
  const { request, env, params } = context;
  const pad = "/" + (Array.isArray(params.route) ? params.route.join("/") : params.route || "");
  const methode = request.method;
  const db = env.DB;

  const publiek = pad === "/login" || pad === "/status" || pad === "/aanvraag";
  if (!publiek && !(await ingelogd(request, env))) {
    return antwoord({ fout: "Niet ingelogd" }, 401);
  }

  try {
    /* ---- inloggen ---- */
    if (pad === "/login" && methode === "POST") {
      const { pin } = await request.json();
      // trim(): een pincode die via de opdrachtregel is ingesteld kan een
      // regeleinde meekrijgen.
      const juist = String(env.BEHEER_PIN || "").trim();
      if (!juist || String(pin || "").trim() !== juist) {
        // Even wachten, zodat proberen traag wordt.
        await new Promise((r) => setTimeout(r, 700));
        return antwoord({ fout: "Verkeerde pincode" }, 401);
      }
      return antwoord({ ok: true }, 200, { "set-cookie": await maakKoekje(env) });
    }
    if (pad === "/uitloggen" && methode === "POST") {
      return antwoord({ ok: true }, 200, {
        "set-cookie": "ab_sessie=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0",
      });
    }
    if (pad === "/status") {
      return antwoord({ ingelogd: await ingelogd(request, env) });
    }

    /* ---- teksten ---- */
    if (pad === "/teksten" && methode === "GET") {
      const { results } = await db.prepare("SELECT sleutel, waarde FROM teksten").all();
      const uit = {};
      for (const r of results || []) uit[r.sleutel] = r.waarde;
      return antwoord(uit);
    }
    if (pad === "/teksten" && methode === "PUT") {
      const { sleutel, waarde } = await request.json();
      if (!sleutel) return antwoord({ fout: "Sleutel ontbreekt" }, 400);
      if (!waarde || !String(waarde).trim()) {
        await db.prepare("DELETE FROM teksten WHERE sleutel = ?").bind(sleutel).run();
        return antwoord({ ok: true, hersteld: true });
      }
      await db.prepare(
        "INSERT INTO teksten (sleutel, waarde, bijgewerkt) VALUES (?, ?, ?) " +
        "ON CONFLICT(sleutel) DO UPDATE SET waarde = excluded.waarde, bijgewerkt = excluded.bijgewerkt"
      ).bind(sleutel, String(waarde).trim(), nu()).run();
      return antwoord({ ok: true });
    }

    /* ---- reviews ---- */
    if (pad === "/reviews" && methode === "GET") {
      const { results } = await db.prepare(
        "SELECT * FROM reviews ORDER BY id DESC").all();
      return antwoord(results || []);
    }
    if (pad === "/reviews" && methode === "POST") {
      const r = await request.json();
      if (!r.tekst || !r.wie) return antwoord({ fout: "Tekst en naam zijn nodig" }, 400);
      await db.prepare(
        "INSERT INTO reviews (tekst, wie, wat, zichtbaar, gemaakt) VALUES (?, ?, ?, 1, ?)"
      ).bind(r.tekst.trim(), r.wie.trim(), (r.wat || "").trim(), nu()).run();
      return antwoord({ ok: true });
    }
    if (pad.startsWith("/reviews/") && methode === "PUT") {
      const id = Number(pad.split("/")[2]);
      const r = await request.json();
      await db.prepare(
        "UPDATE reviews SET tekst = ?, wie = ?, wat = ?, zichtbaar = ? WHERE id = ?"
      ).bind(r.tekst, r.wie, r.wat || "", r.zichtbaar ? 1 : 0, id).run();
      return antwoord({ ok: true });
    }
    if (pad.startsWith("/reviews/") && methode === "DELETE") {
      await db.prepare("DELETE FROM reviews WHERE id = ?").bind(Number(pad.split("/")[2])).run();
      return antwoord({ ok: true });
    }

    /* ---- projecten ---- */
    if (pad === "/projecten" && methode === "GET") {
      const { results } = await db.prepare("SELECT * FROM projecten ORDER BY id DESC").all();
      return antwoord(results || []);
    }
    if (pad === "/projecten" && methode === "POST") {
      const p = await request.json();
      if (!p.titel || !p.voor || !p.na) {
        return antwoord({ fout: "Titel en twee foto's zijn nodig" }, 400);
      }
      const slug = await vrijeSlug(db, slugify(`${p.titel} ${p.plaats || ""}`), null);
      await db.prepare(
        "INSERT INTO projecten (slug, titel, plaats, dienst, wanneer, situatie, aanpak, resultaat," +
        " voor, na, extra, zichtbaar, gemaakt) VALUES (?,?,?,?,?,?,?,?,?,?,?,1,?)"
      ).bind(slug, p.titel.trim(), p.plaats || "", p.dienst || "", p.wanneer || "",
             p.situatie || "", p.aanpak || "", p.resultaat || "", p.voor, p.na,
             JSON.stringify(p.extra || []), nu()).run();
      return antwoord({ ok: true, slug });
    }
    if (pad.startsWith("/projecten/") && methode === "PUT") {
      const id = Number(pad.split("/")[2]);
      const p = await request.json();
      const slug = await vrijeSlug(db, slugify(`${p.titel} ${p.plaats || ""}`), id);
      await db.prepare(
        "UPDATE projecten SET slug=?, titel=?, plaats=?, dienst=?, wanneer=?, situatie=?, aanpak=?," +
        " resultaat=?, zichtbaar=? WHERE id = ?"
      ).bind(slug, p.titel, p.plaats || "", p.dienst || "", p.wanneer || "", p.situatie || "",
             p.aanpak || "", p.resultaat || "", p.zichtbaar ? 1 : 0, id).run();
      return antwoord({ ok: true, slug });
    }
    if (pad.startsWith("/projecten/") && methode === "DELETE") {
      const id = Number(pad.split("/")[2]);
      const rij = await db.prepare("SELECT voor, na, extra FROM projecten WHERE id = ?")
        .bind(id).first();
      if (rij && env.MEDIA) {
        const sleutels = [rij.voor, rij.na, ...(JSON.parse(rij.extra || "[]"))].filter(Boolean);
        for (const s of sleutels) await env.MEDIA.delete(s);
      }
      await db.prepare("DELETE FROM projecten WHERE id = ?").bind(id).run();
      return antwoord({ ok: true });
    }

    /* ---- foto's ---- */
    if (pad === "/upload" && methode === "POST") {
      const type = request.headers.get("content-type") || "";
      if (!type.startsWith("image/")) return antwoord({ fout: "Alleen afbeeldingen" }, 400);
      const bytes = await request.arrayBuffer();
      if (bytes.byteLength > 6 * 1024 * 1024) return antwoord({ fout: "Foto te groot" }, 413);
      const ext = type.includes("png") ? "png" : type.includes("webp") ? "webp" : "jpg";
      const sleutel = `projecten/${Date.now()}-${Math.random().toString(36).slice(2, 8)}.${ext}`;
      await env.MEDIA.put(sleutel, bytes, { httpMetadata: { contentType: type } });
      return antwoord({ ok: true, sleutel, url: `/media/${sleutel}` });
    }

    /* ---- aanvragen ---- */
    if (pad === "/aanvraag" && methode === "POST") {
      const gegevens = await request.json();
      if (gegevens._honey) return antwoord({ ok: true }); // spambot
      // Eerst opslaan: wat er daarna ook misgaat, de aanvraag is binnen.
      const rij = await db.prepare(
        "INSERT INTO aanvragen (soort, gegevens, gemaakt) VALUES (?, ?, ?) RETURNING id"
      ).bind(gegevens._soort || "contact", JSON.stringify(gegevens), nu()).first();
      // Dan de mail naar Ahmad, op de achtergrond: de bezoeker krijgt meteen
      // zijn bevestiging. Of het lukte, komt bij de aanvraag te staan.
      context.waitUntil((async () => {
        const status = await mailAanvraag(env, gegevens);
        if (status && rij) {
          await db.prepare("UPDATE aanvragen SET mail = ? WHERE id = ?").bind(status, rij.id).run();
        }
      })().catch(() => {}));
      return antwoord({ ok: true });
    }
    if (pad === "/aanvragen" && methode === "GET") {
      const { results } = await db.prepare(
        "SELECT * FROM aanvragen ORDER BY id DESC LIMIT 100").all();
      return antwoord(results || []);
    }
    if (pad.startsWith("/aanvragen/") && methode === "DELETE") {
      await db.prepare("DELETE FROM aanvragen WHERE id = ?").bind(Number(pad.split("/")[2])).run();
      return antwoord({ ok: true });
    }

    return antwoord({ fout: "Onbekend adres" }, 404);
  } catch (e) {
    return antwoord({ fout: String(e && e.message || e) }, 500);
  }
}
