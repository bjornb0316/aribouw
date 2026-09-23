-- Database achter het beheerscherm (Cloudflare D1).
-- Aanmaken:  npx wrangler d1 execute aribouw --remote --file=schema.sql

-- Aangepaste teksten. De sleutel is het label uit assets/teksten.json.
-- Staat een tekst hier niet in, dan toont de site de oorspronkelijke tekst.
CREATE TABLE IF NOT EXISTS teksten (
  sleutel     TEXT PRIMARY KEY,
  waarde      TEXT NOT NULL,
  bijgewerkt  TEXT NOT NULL
);

-- Projecten die Ahmad toevoegt.
CREATE TABLE IF NOT EXISTS projecten (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  slug        TEXT UNIQUE NOT NULL,
  titel       TEXT NOT NULL,
  plaats      TEXT,
  dienst      TEXT,
  wanneer     TEXT,
  situatie    TEXT,
  aanpak      TEXT,
  resultaat   TEXT,
  voor        TEXT,          -- sleutel in R2
  na          TEXT,
  extra       TEXT,          -- JSON-lijst met extra sleutels
  zichtbaar   INTEGER NOT NULL DEFAULT 1,
  gemaakt     TEXT NOT NULL
);

-- Reviews die Ahmad zelf toevoegt. De vier van Werkspot staan in de site
-- zelf; deze komen daarbij.
CREATE TABLE IF NOT EXISTS reviews (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  tekst       TEXT NOT NULL,
  wie         TEXT NOT NULL,
  wat         TEXT,
  zichtbaar   INTEGER NOT NULL DEFAULT 1,
  gemaakt     TEXT NOT NULL
);

-- Binnengekomen aanvragen van het contactformulier en de offerteflow.
CREATE TABLE IF NOT EXISTS aanvragen (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  soort       TEXT NOT NULL,
  gegevens    TEXT NOT NULL,  -- JSON
  gelezen     INTEGER NOT NULL DEFAULT 0,
  gemaakt     TEXT NOT NULL,
  mail        TEXT            -- "verstuurd", "mislukt: <reden>" of leeg
);
-- Een database van vóór de kolom mail krijgt hem zo (eenmalig):
--   ALTER TABLE aanvragen ADD COLUMN mail TEXT;
