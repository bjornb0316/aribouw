/* Vaste gegevens voor de serverkant.
 *
 * De site is op twee namen bereikbaar (aribouw.nl en www.aribouw.nl) en
 * daarnaast op aribouw.pages.dev. Google moet er één kiezen, anders ziet hij
 * dezelfde pagina op drie adressen. SITE is dat ene adres: het staat in
 * elke canonical, in de sitemap en in de doorverwijzing van www.
 *
 * Verandert het domein, dan hoeft alleen dit bestand mee (en SITE_URL in
 * bouwscript/data.py, waar hetzelfde adres staat voor de vaste pagina's).
 */
export const SITE = "https://aribouw.nl";

/* Waar aanvragen uit de formulieren heen gaan, en van welk adres ze komen.
 * Het afzendadres moet op een domein staan dat bij Resend is geverifieerd. */
export const AANVRAAG_AAN = "info@aribouw.nl";
export const AANVRAAG_VAN = "Website Aribouw <aanvraag@aribouw.nl>";

/* Van de naam van een dienst, zoals die in het beheerscherm wordt gekozen,
 * naar de pagina erover. Staat een dienst er niet bij, dan wijst de link
 * naar het overzicht. */
export const DIENSTPAGINA = {
  "Binnenschilderwerk": "/dienst-binnenschilderwerk",
  "Buitenschilderwerk": "/dienst-buitenschilderwerk",
  "Behangen": "/dienst-behang",
  "Houtreparaties en onderhoud": "/dienst-houtwerk",
  "Kozijnen en deuren schilderen": "/dienst-kozijnen-deuren",
  "Wanden en plafonds schilderen": "/dienst-wanden-plafonds",
};

/* Plaatsen met een eigen pagina. */
export const PLAATSPAGINA = {
  "Westervoort": "/regio-westervoort",
  "Duiven": "/regio-duiven",
  "Zevenaar": "/regio-zevenaar",
  "Arnhem": "/regio-arnhem",
  "Huissen": "/regio-huissen",
};
