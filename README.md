# Glas & Gras

Voorspelt per uur of de glazen wanden en de baan van een padelbaan droog of nat zijn.
Weerdata komt van Open-Meteo (gratis, geen API-key).

## Bestanden

| Bestand | Wat |
|---|---|
| `padel-template.html` | De bron van de pagina: model, opmaak en code. Pas hier dingen aan. |
| `build_site.py` | Bouwt de losse website/app in `site/`. |
| `build.py` | Bouwt `padel-droog.html` met ingebakken weerdata voor de Claude-pagina. |
| `site/` | De website om online te zetten (PWA): `index.html`, manifest, service worker, iconen. |
| `icon-src/icon.svg` | Bron van het app-icoon. |

Na een wijziging in `padel-template.html`:

```bash
python3 build_site.py
```

## Online zetten

Automatisch via GitHub Actions: bij elke push naar `main` bouwt
`.github/workflows/pages.yml` de site (`python3 build_site.py`) en zet hem op GitHub Pages.
Wijzigen is dus: `padel-template.html` aanpassen, committen en pushen. Een paar minuten
later staat het online. De voortgang zie je onder het tabblad *Actions* van de repository.

Eenmalig: in de repository *Settings → Pages → Source* op **GitHub Actions** zetten.

## Op je telefoon zetten
- **iPhone (Safari):** open de site → deelknop → *Zet op beginscherm*.
- **Android (Chrome):** open de site → menu ⋮ → *App installeren* of *Toevoegen aan startscherm*.

## Waarnemingen
Die worden op het toestel zelf bewaard. Met **Exporteren** (onder "Klopte het?") krijg je een
JSON-bestand; met **Importeren** zet je dat op een ander toestel. Geef de export aan Claude om
het model bij te stellen.

## Na een update
`build_site.py` geeft de service worker bij elke wijziging een nieuwe cacheversie, zodat
geïnstalleerde apps de nieuwe versie vanzelf ophalen (meestal bij de tweede keer openen).
