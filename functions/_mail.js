/* Een aanvraag uit de formulieren als mail naar Ahmad.
 *
 * Via Resend (omgevingsvariabele RESEND_KEY). De aanvraag staat al in de
 * database voordat deze mail vertrekt: gaat het mailen mis, dan is er niets
 * kwijt, en het beheerscherm laat zien dat de mail niet is aangekomen.
 *
 * De formulieren vragen geen e-mailadres, alleen een telefoonnummer. Daarom
 * staan bovenaan de mail knoppen om te bellen en te appen.
 */
import { AANVRAAG_AAN, AANVRAAG_VAN, SITE } from "./_site.js";

// Volgorde en namen zoals Ahmad ze in de mail wil lezen.
const LABELS = [
  ["naam", "Naam"], ["telefoon", "Telefoon"], ["plaats", "Plaats"],
  ["werk", "Soort werk"], ["onderwerp", "Waarover"], ["omvang", "Omvang"],
  ["kleurrichting", "Kleurrichting"], ["ondergrond", "Ondergrond"],
  ["wanneer", "Wanneer"], ["situatie", "Bericht"], ["pagina", "Verstuurd vanaf"],
];

function veilig(t) {
  return String(t == null ? "" : t)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// 06 12 34 56 78 -> 31612345678, voor een wa.me-link.
function waNummer(tel) {
  let n = String(tel || "").replace(/[^\d+]/g, "");
  if (n.startsWith("+")) n = n.slice(1);
  else if (n.startsWith("00")) n = n.slice(2);
  else if (n.startsWith("0")) n = "31" + n.slice(1);
  return n.length >= 10 ? n : "";
}

function regels(g) {
  const bekend = LABELS.filter(([k]) => g[k]).map(([k, label]) => [label, g[k]]);
  // Velden die (nog) niet in de lijst staan, toch meesturen.
  const rest = Object.keys(g)
    .filter((k) => k[0] !== "_" && g[k] && !LABELS.some(([l]) => l === k))
    .map((k) => [k, g[k]]);
  return bekend.concat(rest);
}

export function onderwerp(g) {
  const basis = String(g._subject || "Nieuwe aanvraag via de website").replace(/\s+/g, " ").slice(0, 120);
  const wie = [g.naam, g.plaats].filter(Boolean).join(", ");
  return wie ? `${basis} (${wie})`.slice(0, 180) : basis;
}

function html(g) {
  const tel = String(g.telefoon || "").trim();
  const wa = waNummer(tel);
  const knop = (href, tekst, vol) =>
    `<a href="${veilig(href)}" style="display:inline-block;padding:12px 20px;margin:0 8px 8px 0;` +
    `border-radius:6px;font-weight:600;text-decoration:none;` +
    (vol ? "background:#12305b;color:#ffffff;" : "border:1px solid #12305b;color:#12305b;") +
    `">${tekst}</a>`;
  const knoppen = (tel ? knop(`tel:${tel.replace(/\s/g, "")}`, `Bellen: ${veilig(tel)}`, true) : "") +
    (wa ? knop(`https://wa.me/${wa}`, "WhatsApp", false) : "");
  const rijen = regels(g).map(([label, waarde]) =>
    `<tr><td style="padding:8px 16px 8px 0;color:#5b6472;vertical-align:top;white-space:nowrap">` +
    `${veilig(label)}</td><td style="padding:8px 0;vertical-align:top">` +
    `${veilig(waarde).replace(/\n/g, "<br>")}</td></tr>`).join("");
  return `<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.5;color:#1b2330;max-width:560px">
<p style="margin:0 0 4px;font-size:13px;color:#5b6472">Via ${veilig(SITE.replace("https://", ""))}</p>
<h2 style="margin:0 0 16px;font-size:20px">${veilig(onderwerp(g))}</h2>
${knoppen ? `<p style="margin:0 0 16px">${knoppen}</p>` : ""}
<table style="border-collapse:collapse;width:100%;border-top:1px solid #e3e6ea">${rijen}</table>
<p style="margin:20px 0 0;font-size:13px;color:#5b6472">Deze aanvraag staat ook in het beheerscherm:
<a href="${SITE}/beheer" style="color:#12305b">${veilig(SITE.replace("https://", ""))}/beheer</a></p>
</div>`;
}

function tekst(g) {
  return onderwerp(g) + "\n\n" +
    regels(g).map(([label, waarde]) => `${label}: ${waarde}`).join("\n") +
    `\n\nOok in het beheerscherm: ${SITE}/beheer\n`;
}

/* Verstuurt de mail. Geeft terug wat er in het beheerscherm komt te staan:
 * "verstuurd", of "mislukt: <reden>". Zonder sleutel: null (niet ingesteld). */
export async function mailAanvraag(env, g) {
  // In Cloudflare staat de sleutel als resend_key; beide spellingen werken.
  const sleutel = env.RESEND_KEY || env.resend_key;
  if (!sleutel) return null;
  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        authorization: `Bearer ${String(sleutel).trim()}`,
        "content-type": "application/json",
      },
      body: JSON.stringify({
        from: AANVRAAG_VAN,
        to: [env.AANVRAAG_AAN || AANVRAAG_AAN],
        subject: onderwerp(g),
        html: html(g),
        text: tekst(g),
      }),
    });
    if (r.ok) return "verstuurd";
    let reden = `status ${r.status}`;
    try { const j = await r.json(); if (j && j.message) reden = j.message; } catch (e) { /* geen json */ }
    return `mislukt: ${reden}`.slice(0, 300);
  } catch (e) {
    return `mislukt: ${String(e && e.message || e)}`.slice(0, 300);
  }
}
