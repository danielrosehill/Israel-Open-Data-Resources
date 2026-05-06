#!/usr/bin/env python3
"""Generate English-language index of data.gov.il catalogue snapshot."""
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
data = json.load(open(HERE / "datasets-raw.json"))

# English names for the 61 organizations (Hebrew display_name -> EN)
ORG_EN = {
    "airport_authority": ("Israel Airports Authority", "Aviation"),
    "archives": ("Israel State Archives", "Government"),
    "bank_israel": ("Bank of Israel", "Finance"),
    "beer-sheva": ("Be'er Sheva Municipality", "Municipal"),
    "betihut-drahim": ("National Road Safety Authority", "Transport"),
    "central-election-committee": ("Central Elections Committee (Knesset)", "Elections"),
    "cio": ("National Digital Agency", "Government"),
    "cma": ("Capital Market, Insurance & Savings Authority", "Finance"),
    "culture_and_sports": ("Ministry of Culture & Sport", "Culture"),
    "eca": ("Enforcement & Collection Authority", "Justice"),
    "energy_and_water": ("Ministry of Energy", "Energy"),
    "firefightingcommission": ("Fire & Rescue Commission", "Public Safety"),
    "governmentprocurementadministration": ("Government Procurement Administration", "Government"),
    "gov-il": ("GOV.IL (general)", "Government"),
    "haifa": ("Haifa Municipality", "Municipal"),
    "holocaust_survivors_rights": ("Holocaust Survivors' Rights Authority", "Welfare"),
    "ies": ("Israel Employment Service", "Labour"),
    "interior_affairs": ("Ministry of Interior", "Government"),
    "iplan": ("Planning Administration", "Planning"),
    "israel_mapping_center": ("Survey of Israel (Mapping Center)", "Geospatial"),
    "israel_national_cyber_directorate": ("Israel National Cyber Directorate", "Cyber"),
    "israel-police": ("Israel Police", "Public Safety"),
    "knesset": ("Knesset (Parliament)", "Government"),
    "labor": ("Ministry of Labor", "Labour"),
    "lamas": ("Central Bureau of Statistics (CBS)", "Statistics"),
    "maaleedumim": ("Ma'ale Adumim Municipality", "Municipal"),
    "meteorological_service": ("Israel Meteorological Service", "Weather"),
    "ministry-health": ("Ministry of Health", "Health"),
    "ministry_of_agriculture": ("Ministry of Agriculture & Food Security", "Agriculture"),
    "ministry_of_education": ("Ministry of Education", "Education"),
    "ministry_of_exterior": ("Ministry of Foreign Affairs", "Government"),
    "ministry_of_housing": ("Ministry of Housing & Construction", "Housing"),
    "ministry_of_immigrant_absorption": ("Ministry of Aliyah & Integration", "Immigration"),
    "ministry_of_internal_security": ("Ministry of National Security", "Public Safety"),
    "ministry_of_justice": ("Ministry of Justice", "Justice"),
    "ministry_of_social_affairs": ("Ministry of Welfare & Social Affairs", "Welfare"),
    "ministry_of_the_environment": ("Ministry of Environmental Protection", "Environment"),
    "ministry_of_tourism": ("Ministry of Tourism", "Tourism"),
    "ministry_of_transport": ("Ministry of Transport & Road Safety", "Transport"),
    "mof": ("Ministry of Finance", "Finance"),
    "moital": ("Ministry of Economy & Industry", "Economy"),
    "nativ": ("Nativ (Liaison Bureau)", "Government"),
    "netzivot": ("Civil Service Commission", "Government"),
    "petah-tikva-municipality": ("Petah Tikva Municipality", "Municipal"),
    "pmo": ("Prime Minister's Office", "Government"),
    "population_authority": ("Population & Immigration Authority", "Immigration"),
    "rabanot": ("Chief Rabbinate", "Religion"),
    "rabinical_court": ("Rabbinical Courts", "Religion"),
    "regulatory-authority": ("Regulatory Affairs Authority", "Government"),
    "religion-office": ("Ministry of Religious Services", "Religion"),
    "rural-education": ("Rural Education Administration", "Education"),
    "science-and-technology": ("Ministry of Innovation, Science & Technology", "Science"),
    "social_security": ("National Insurance Institute (Bituah Leumi)", "Welfare"),
    "socialequality": ("Ministry of Social Equality", "Welfare"),
    "synthetic": ("Synthetic / test data", "Other"),
    "taxes-authority": ("Israel Tax Authority", "Finance"),
    "the_israel_lands_administration": ("Israel Land Authority", "Land"),
    "the_judicial_authority": ("Judicial Authority (Courts)", "Justice"),
    "tikshoret": ("Ministry of Communications", "Communications"),
    "volcaniagri": ("Volcani Agricultural Research", "Agriculture"),
    "water_authority": ("Israel Water Authority", "Water"),
}

# Group by org
by_org = defaultdict(list)
for p in data:
    by_org[p["organization"]["name"]].append(p)

# Group orgs by category
by_cat = defaultdict(list)
for slug, (en, cat) in ORG_EN.items():
    if slug in by_org:
        by_cat[cat].append((slug, en, len(by_org[slug])))

CATEGORY_ORDER = [
    "Statistics", "Geospatial", "Transport", "Health", "Environment", "Water",
    "Energy", "Weather", "Finance", "Economy", "Labour", "Welfare", "Education",
    "Science", "Housing", "Land", "Planning", "Justice", "Public Safety", "Cyber",
    "Elections", "Government", "Communications", "Culture", "Tourism", "Agriculture",
    "Immigration", "Religion", "Aviation", "Municipal", "Other",
]

def fmt_resources(p):
    """Compact resource summary: formats + count of datastore-queryable."""
    fmts = sorted({(r.get("format") or "?").upper() for r in p.get("resources", [])})
    ds = sum(1 for r in p.get("resources", []) if r.get("datastore_active"))
    total = len(p.get("resources", []))
    s = "/".join(f for f in fmts if f) or "—"
    if ds:
        s += f" · {ds}/{total} DataStore"
    elif total > 1:
        s += f" · {total} files"
    return s

def first_datastore_id(p):
    for r in p.get("resources", []):
        if r.get("datastore_active"):
            return r["id"]
    return None

# Build markdown
out = []
out.append("# data.gov.il — English Catalogue Index\n")
out.append("**Snapshot:** 2026-05-06 · **Source:** https://data.gov.il (CKAN portal)\n")
out.append(f"**Coverage:** {len(data)} datasets across {len(by_org)} publishing organizations · "
           f"{sum(len(p.get('resources', [])) for p in data)} resource files · "
           f"{sum(1 for p in data for r in p.get('resources', []) if r.get('datastore_active'))} "
           "DataStore-queryable resources.\n")
out.append("> Native UI is Hebrew-only; this index is generated from the public CKAN API "
           "(no auth, no geo-restriction observed from .il, EU, US testing). "
           "Dataset titles are kept in their original Hebrew alongside the URL slug "
           "(which is often a transliteration or English keyword) so they can be located in the portal.\n")

out.append("\n## API endpoints\n")
out.append("""\
The portal runs CKAN, so all standard CKAN action API endpoints work:

| Endpoint | Purpose |
| --- | --- |
| `GET https://data.gov.il/api/3/action/package_list` | All dataset slugs |
| `GET https://data.gov.il/api/3/action/package_search?q=<query>&rows=1000&start=0` | Paginated dataset search (1000/page) |
| `GET https://data.gov.il/api/3/action/package_show?id=<slug>` | Full metadata for one dataset |
| `GET https://data.gov.il/api/3/action/organization_list?all_fields=true` | All 61 publishing orgs |
| `GET https://data.gov.il/api/3/action/organization_show?id=<slug>&include_datasets=true` | Datasets by org |
| `GET https://data.gov.il/api/3/action/datastore_search?resource_id=<uuid>&limit=100` | Tabular query against a DataStore-active resource |
| `GET https://data.gov.il/api/3/action/datastore_search_sql?sql=<sql>` | SQL query (where enabled) |
| `GET https://data.gov.il/api/3/action/datastore_search?resource_id=<uuid>&q=<term>` | Full-text search inside a resource |

**Quirks noted at snapshot time:**
- `status_show` returns HTTP 403 (otherwise the API is open).
- Per-org `package_count` is null on `organization_list` — counts must be computed from `package_search` results (already done below).
- Both groups (`firstgroup`, `second-group`) are empty placeholders; categorisation is by **organization**, not group.
- Resource URLs follow `https://data.gov.il/dataset/<dataset-uuid>/resource/<resource-uuid>/download/<file>` and are direct downloads.
- Bulk pulls: `package_search?rows=1000` returns up to 1000 records — paginate with `start=`.

**Example: tabular query for live flight data (Israel Airports Authority):**
```
curl 'https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5'
```
""")

out.append("\n## Catalogue by category\n")
for cat in CATEGORY_ORDER:
    if cat not in by_cat:
        continue
    out.append(f"\n### {cat}\n")
    out.append("| Org | Datasets | Hebrew name |")
    out.append("\n| --- | ---: | --- |\n")
    for slug, en, n in sorted(by_cat[cat], key=lambda x: -x[2]):
        heb = by_org[slug][0]["organization"].get("title", "")
        out.append(f"| **[{en}](#{slug})** (`{slug}`) | {n} | {heb} |\n")

out.append("\n---\n\n## Datasets by organization\n")

# Sort orgs by count desc within each category, but list all
ordered = sorted(by_org.keys(), key=lambda k: -len(by_org[k]))
for slug in ordered:
    en, cat = ORG_EN.get(slug, (slug, "Other"))
    pkgs = by_org[slug]
    heb = pkgs[0]["organization"].get("title", "")
    out.append(f"\n### {en}\n")
    out.append(f"<a id=\"{slug}\"></a>\n")
    out.append(f"**Slug:** `{slug}` · **Hebrew:** {heb} · **Category:** {cat} · "
               f"**Datasets:** {len(pkgs)}\n\n")
    out.append(f"- Org page: https://data.gov.il/organization/{slug}\n")
    out.append(f"- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:{slug}&rows=1000`\n\n")
    out.append("| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |\n")
    out.append("| ---: | --- | --- | --- | --- |\n")
    for i, p in enumerate(sorted(pkgs, key=lambda x: x["name"]), 1):
        ds_id = first_datastore_id(p) or ""
        title = (p.get("title") or "").replace("|", "\\|").replace("\n", " ")
        url = f"https://data.gov.il/dataset/{p['name']}"
        out.append(f"| {i} | [`{p['name']}`]({url}) | {title} | {fmt_resources(p)} | "
                   f"{'`'+ds_id+'`' if ds_id else '—'} |\n")

out.append("\n---\n\n## Notes & caveats\n")
out.append("""\
- **Language:** Dataset titles, descriptions, tags, and column headers in resource files are predominantly Hebrew. URL slugs are usually English transliterations or keywords. There is no official English catalogue — this index is a third-party derivation.
- **Geo-restriction:** Many `*.gov.il` *web* properties geo-fence outside Israel, but the `data.gov.il` CKAN API and the `download/datafile.csv` resource URLs were directly reachable during this snapshot from .il. If blocked elsewhere, route via an Israeli egress (Cloudflare WARP set to IL, an IL VPS, or `claude-in-chrome`/Playwright with an IL session).
- **Staleness:** This snapshot is point-in-time. The catalogue grows ~weekly. Re-pull with the script in this folder to refresh; resource UUIDs are stable but new resources/datasets are added.
- **Licensing:** Most datasets are published under the Israeli government open-data terms — verify per-dataset (`license_id`, `license_title` in `package_show`) before redistribution.
""")

(HERE / "README.md").write_text("".join(out), encoding="utf-8")
print(f"Wrote README.md ({len(''.join(out))} bytes)")
