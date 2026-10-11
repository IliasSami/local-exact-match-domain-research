# Example: US dentist EMD run (live)

Date: 2026-10-12. Method: RDAP (Verisign / PIR), 5 workers + retry pass.
Toolchain: `assets/emd_matrix_run.py` → `assets/build_emd_report.py`.

- Candidates checked: **1,950**
- Available: **508 (26%)**
- Registered: **1,442**
- Unresolved: **0**

Token set: `dentist`, `dentists`, `dental`, `orthodontist`, `cosmeticdentist`,
`emergencydentist`.
Geos: 51 states (incl. D.C.), 61 major cities, 50 popular neighbourhoods/places.
TLD: `.com` (head terms checked on `.com`, `.net`, `.org`).
Orders: `{service}{geo}` and `{geo}{service}`.

This is a **multi-tier** run: every location token carries a `geotype`
(`head` / `state` / `city` / `place`), which is what produces the availability
curve below.

## Availability by location type

| Layer | Available | Total | Open |
|---|---:|---:|---:|
| Head term | 0 | 18 | 0% |
| City | 35 | 720 | 5% |
| State | 205 | 612 | 33% |
| Neighbourhood / place | 268 | 600 | 45% |

Flat head terms are gone. The open opportunity is the **long tail** — and even
inside the "45% open" place tier the generic `dentist` token is mostly taken;
availability concentrates in the `emergency` / `cosmetic` / `orthodontist`
modifiers.

## Availability by service

| Service | Available |
|---|---:|
| emergencydentist | 156 |
| cosmeticdentist | 119 |
| orthodontist | 99 |
| dentists | 60 |
| dental | 49 |
| dentist | 25 |

## Available city EMDs (35)

- `arlingtonemergencydentist.com`
- `buffaloemergencydentist.com`
- `chulavistaemergencydentist.com`
- `coloradospringscosmeticdentist.com`
- `cosmeticdentistfortworth.com`
- `cosmeticdentistfresno.com`
- `cosmeticdentistkansascity.com`
- `cosmeticdentistlouisville.com`
- `cosmeticdentistmesa.com`
- `cosmeticdentistoklahomacity.com`
- `cosmeticdentistrichmond.com`
- `cosmeticdentistsanjose.com`
- `cosmeticdentiststlouis.com`
- `dentalchulavista.com`
- `dentalneworleans.com`
- `dentistsalbuquerque.com`
- `dentistschulavista.com`
- `dentistsfresno.com`
- `dentistskansascity.com`
- `dentistsmesa.com`
- `dentistsoklahomacity.com`
- `dentistsplano.com`
- `dentistsvirginiabeach.com`
- `emergencydentistbuffalo.com`
- `emergencydentistchulavista.com`
- `emergencydentistcincinnati.com`
- `emergencydentistirvine.com`
- `emergencydentistlongbeach.com`
- `kansascitycosmeticdentist.com`
- `oklahomacityemergencydentist.com`
- `orthodontistbuffalo.com`
- `orthodontistoklahomacity.com`
- `orthodontistpittsburgh.com`
- `orthodontistscottsdale.com`
- `stlouisemergencydentist.com`

The canonical, de-duplicated source for every tier is
[`us-dentist-availability.csv`](us-dentist-availability.csv).

## Notable available neighbourhood EMDs

| Place | Available examples |
|---|---|
| SoHo (NYC) | `sohodentists.com`, `dentistssoho.com`, `sohocosmeticdentist.com` |
| Upper East Side (NYC) | `dentistuppereastside.com`, `dentistsuppereastside.com`, `cosmeticdentistuppereastside.com` |
| South Beach (Miami) | `southbeachemergencydentist.com`, `southbeachorthodontist.com`, `dentistssouthbeach.com` |
| Buckhead (Atlanta) | `buckheademergencydentist.com`, `dentistsbuckhead.com` |
| Georgetown (DC) | `georgetowndentists.com`, `dentistsgeorgetown.com` |
| Williamsburg (NYC) | `williamsburgorthodontist.com`, `williamsburgcosmeticdentist.com` |
| Hollywood (LA) | `dentistshollywood.com` |

Famous-neighbourhood + generic `dentist` is almost always taken
(`brooklyndentist.com`, `manhattandentist.com`, `hollywooddentist.com` were all
registered). The leverage is the **modifier** (`emergency-`, `cosmetic-`,
`orthodontist`) or the **less-contested** place.

## The dashboard

`assets/build_emd_report.py` turns the run's JSON into a self-contained HTML
report (no CDN, opens offline): stat cards, availability-by-service and
availability-by-location-type bars, an insight card, the featured city tier, and
a searchable/filterable table of all 1,950 candidates. A rendered copy is in
this folder: [`us-dentist-report.html`](us-dentist-report.html).

## Reproduce it

```bash
# geo.csv has columns: geo,geotype,display
python3 assets/emd_matrix_run.py \
  --service dentist dentists dental orthodontist cosmeticdentist emergencydentist \
  --geo-file geo.csv --tld com \
  --out-csv us-dentist-availability.csv \
  --json-out us-dentist-data.json \
  --title "Dentists in the USA — EMD availability"

python3 assets/build_emd_report.py \
  --input us-dentist-data.json \
  --out us-dentist-report.html \
  --highlight-type city
```

## Caveats

- Availability is **not** quality. Validate local search demand, the local pack,
  domain history/spam and trademarks before buying anything.
- `emergency` and `cosmetic` domains attract higher CPC competition; a
  registered-but-available domain can still be a poor brand or a trademark risk.
- Data reflects the moment of checking and can change at any time.

Full evidence: [`us-dentist-availability.csv`](us-dentist-availability.csv).
