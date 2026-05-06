#!/usr/bin/env python3
"""Generate Typst source for the PDF catalogue, then render to PDF.

Inputs:  datasets-raw.json, samples.json, translations.json
Output:  catalogue.typ, catalogue.pdf
"""
import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
SAMPLES = HERE / "samples.json"
TRANS = HERE / "translations.json"
TYP = HERE / "catalogue.typ"
PDF = HERE / "catalogue.pdf"

# Map org slug -> (English name, category). Built from actual orgs in datasets-raw.json (2026-05-06).
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
    "gov-il": ("GOV.IL (general)", "Government"),
    "governmentprocurementadministration": ("Government Procurement Administration", "Government"),
    "haifa": ("Haifa Municipality", "Municipal"),
    "holocaust_survivors_rights": ("Holocaust Survivors' Rights Authority", "Welfare"),
    "ies": ("Israel Employment Service", "Labour"),
    "interior_affairs": ("Ministry of Interior", "Government"),
    "iplan": ("Planning Administration", "Planning"),
    "israel-police": ("Israel Police", "Public Safety"),
    "israel_mapping_center": ("Survey of Israel (Mapping Center)", "Geospatial"),
    "israel_national_cyber_directorate": ("Israel National Cyber Directorate", "Cyber"),
    "knesset": ("Knesset (Parliament)", "Government"),
    "labor": ("Ministry of Labor", "Labour"),
    "lamas": ("Central Bureau of Statistics (CBS)", "Statistics"),
    "maaleedumim": ("Ma'ale Adumim Municipality", "Municipal"),
    "meteorological_service": ("Israel Meteorological Service", "Weather"),
    "ministry-health": ("Ministry of Health", "Health"),
    "ministry_of_agriculture": ("Ministry of Agriculture & Food Security", "Agriculture"),
    "ministry_of_education": ("Ministry of Education", "Education"),
    "ministry_of_exterior": ("Ministry of Foreign Affairs", "Government"),
    "ministry_of_housing": ("Ministry of Construction & Housing", "Housing"),
    "ministry_of_immigrant_absorption": ("Ministry of Aliyah & Integration", "Government"),
    "ministry_of_internal_security": ("Ministry of National Security", "Public Safety"),
    "ministry_of_justice": ("Ministry of Justice", "Justice"),
    "ministry_of_social_affairs": ("Ministry of Welfare & Social Affairs", "Welfare"),
    "ministry_of_the_environment": ("Ministry of Environmental Protection", "Environment"),
    "ministry_of_tourism": ("Ministry of Tourism", "Tourism"),
    "ministry_of_transport": ("Ministry of Transport & Road Safety", "Transport"),
    "mof": ("Ministry of Finance", "Finance"),
    "moital": ("Ministry of Economy & Industry", "Economy"),
    "nativ": ("Nativ (PMO Liaison Bureau)", "Government"),
    "netzivot": ("Civil Service Commission", "Government"),
    "petah-tikva-municipality": ("Petah Tikva Municipality", "Municipal"),
    "pmo": ("Prime Minister's Office", "Government"),
    "population_authority": ("Population & Immigration Authority", "Government"),
    "rabanot": ("Chief Rabbinate of Israel", "Religion"),
    "rabinical_court": ("Rabbinical Courts", "Justice"),
    "regulatory-authority": ("Regulatory Authority", "Government"),
    "religion-office": ("Ministry of Religious Services", "Religion"),
    "rural-education": ("Rural Education Administration", "Education"),
    "science-and-technology": ("Ministry of Innovation, Science & Technology", "Science"),
    "social_security": ("National Insurance Institute (Bituah Leumi)", "Welfare"),
    "socialequality": ("Ministry of Social Equality", "Welfare"),
    "synthetic": ("Government Synthetic Data", "Other"),
    "taxes-authority": ("Israel Tax Authority", "Finance"),
    "the_israel_lands_administration": ("Israel Land Authority (RMI)", "Land"),
    "the_judicial_authority": ("Judicial Authority (Courts)", "Justice"),
    "tikshoret": ("Ministry of Communications", "Communications"),
    "volcaniagri": ("Volcani Agricultural Research Center", "Agriculture"),
    "water_authority": ("Israel Water Authority", "Water"),
}


def fmt_size(b):
    if not b or not str(b).isdigit():
        return "—"
    n = int(b)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n} {unit}"
        n //= 1024
    return f"{n} PB"


def fmt_date(s):
    if not s:
        return "—"
    try:
        return datetime.fromisoformat(s.split(".")[0]).strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        return s[:10] if isinstance(s, str) else "—"


def esc(s):
    """Escape for Typst content."""
    if s is None:
        return ""
    s = str(s)
    # Typst special chars: \ # @ * _ $ < > = / [ ] { } ` ~ -
    repl = {
        "\\": "\\\\",
        "#": "\\#",
        "@": "\\@",
        "*": "\\*",
        "_": "\\_",
        "$": "\\$",
        "<": "\\<",
        ">": "\\>",
        "=": "\\=",
        "[": "\\[",
        "]": "\\]",
        "{": "\\{",
        "}": "\\}",
        "`": "\\`",
        "~": "\\~",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def truncate(s, n):
    if not s:
        return ""
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0] + "…"


def main():
    raw = json.loads(RAW.read_text())
    samples = json.loads(SAMPLES.read_text()) if SAMPLES.exists() else {}
    trans = json.loads(TRANS.read_text()) if TRANS.exists() else {}

    by_org = defaultdict(list)
    for ds in raw["datasets"]:
        org_slug = ds["organization"]["name"] if ds.get("organization") else "unknown"
        by_org[org_slug].append(ds)

    for org_datasets in by_org.values():
        org_datasets.sort(key=lambda d: d.get("title") or d["name"])

    # Sort orgs by category, then English name
    org_order = sorted(by_org.keys(), key=lambda s: (ORG_EN.get(s, (s, "ZZZ"))[1], ORG_EN.get(s, (s, ""))[0].lower()))

    out = []
    out.append('#set document(title: "data.gov.il Catalogue", author: "Israel Open Data Resources")')
    out.append('#set page(paper: "a4", margin: (x: 1.6cm, y: 2cm), numbering: "1 / 1", header: align(right)[#text(size: 8pt, fill: gray)[data.gov.il catalogue]])')
    out.append('#set text(font: ("Noto Sans", "Liberation Sans"), size: 9pt, lang: "en")')
    out.append('#set heading(numbering: none)')
    out.append('#show heading.where(level: 1): it => [#pagebreak(weak: true)#block(below: 1em)[#text(size: 22pt, weight: "bold")[#it.body]]]')
    out.append('#show heading.where(level: 2): it => block(above: 1.4em, below: 0.6em)[#text(size: 14pt, weight: "bold", fill: rgb("#1a4480"))[#it.body]]')
    out.append('#show heading.where(level: 3): it => block(above: 0.8em, below: 0.3em)[#text(size: 11pt, weight: "bold")[#it.body]]')
    out.append('#let hebrew(body) = text(font: ("Noto Sans Hebrew", "DejaVu Sans"), dir: rtl, lang: "he")[#body]')
    out.append('#let kv(label, value) = grid(columns: (auto, 1fr), column-gutter: 0.6em, text(weight: "bold", fill: gray)[#label], value)')
    out.append('#let chip(t, c) = box(inset: (x: 4pt, y: 1pt), radius: 2pt, fill: c, text(size: 7pt, fill: white, weight: "bold")[#t])')
    out.append('')
    # Title page
    out.append('#align(center + horizon)[')
    out.append('  #text(size: 32pt, weight: "bold")[data.gov.il]\\')
    out.append('  #v(0.5em)')
    out.append('  #text(size: 18pt)[Bilingual Catalogue]\\')
    out.append('  #v(0.4em)')
    out.append(f'  #text(size: 12pt, fill: gray)[Snapshot: {datetime.now().strftime("%Y-%m-%d")}]\\')
    out.append(f'  #v(0.2em)')
    out.append(f'  #text(size: 11pt)[{len(raw["datasets"])} datasets · {len(by_org)} organizations]')
    out.append(']')
    out.append('#pagebreak()')
    out.append('')
    out.append('#outline(title: [Contents], depth: 2, indent: auto)')
    out.append('#pagebreak()')

    # Group orgs by category for the contents pages
    by_cat = defaultdict(list)
    for slug in org_order:
        cat = ORG_EN.get(slug, (slug, "Other"))[1]
        by_cat[cat].append(slug)

    # Index by category
    out.append('= Index by Category')
    out.append('')
    for cat in sorted(by_cat.keys()):
        out.append(f'== {esc(cat)}')
        out.append('#table(columns: (1fr, auto), stroke: 0.4pt + gray, inset: 6pt,')
        out.append('  table.header(text(weight: "bold")[Organization], text(weight: "bold")[Datasets]),')
        rows = []
        for slug in by_cat[cat]:
            en_name, _ = ORG_EN.get(slug, (slug, "Other"))
            rows.append(f'  [#link(label("org-{slug}"))[{esc(en_name)}] #text(size: 7pt, fill: gray)[({slug})]], [{len(by_org[slug])}]')
        out.append(',\n'.join(rows))
        out.append(')')
        out.append('')

    # Per-org sections
    for slug in org_order:
        en_name, cat = ORG_EN.get(slug, (slug, "Other"))
        org_datasets = by_org[slug]
        # Hebrew name from first dataset's organization metadata
        he_name = org_datasets[0]["organization"].get("title", "") if org_datasets and org_datasets[0].get("organization") else ""
        out.append(f'= {esc(en_name)} <org-{slug}>')
        out.append(f'#text(size: 10pt, fill: gray)[Slug: `{slug}` · Category: {esc(cat)} · {len(org_datasets)} datasets]\\')
        if he_name:
            out.append(f'#hebrew[#text(size: 11pt)[{esc(he_name)}]]')
        out.append('')

        for ds in org_datasets:
            slug_ds = ds["name"]
            he_title = ds.get("title") or ""
            he_notes = ds.get("notes") or ""
            t = trans.get(slug_ds, {})
            en_title = t.get("english_title") or slug_ds.replace("-", " ").replace("_", " ").title()
            en_desc = t.get("english_description") or ""

            out.append(f'== {esc(en_title)}')
            if he_title:
                out.append(f'#hebrew[{esc(he_title)}]\\')
            out.append('')
            out.append(f'#kv("Slug", raw("{slug_ds}"))')
            out.append(f'#kv("Updated", [{fmt_date(ds.get("metadata_modified"))}])')
            out.append(f'#kv("Frequency", [{esc(ds.get("Frequency") or "—")}])')
            out.append(f'#kv("Resources", [{ds.get("num_resources", 0)}])')
            url = f"https://data.gov.il/dataset/{slug_ds}"
            out.append(f'#kv("URL", link("{url}")[{url}])')
            out.append('')

            if en_desc:
                out.append('=== Description (EN)')
                out.append(esc(truncate(en_desc, 1200)))
                out.append('')
            if he_notes:
                out.append('=== תיאור (HE)')
                out.append(f'#hebrew[{esc(truncate(he_notes, 1200))}]')
                out.append('')

            # Resources
            resources = ds.get("resources", [])
            if resources:
                out.append('=== Resources')
                # Resources table
                out.append('#table(columns: (auto, auto, auto, auto, 1fr), stroke: 0.3pt + gray, inset: 5pt, align: left + horizon,')
                out.append('  table.header(text(weight: "bold")[Format], text(weight: "bold")[Size], text(weight: "bold")[Modified], text(weight: "bold")[DataStore], text(weight: "bold")[Name]),')
                rrows = []
                for r in resources[:20]:
                    fmt = (r.get("format") or "?").upper()
                    size = fmt_size(r.get("size"))
                    mod = fmt_date(r.get("last_modified") or r.get("metadata_modified"))
                    ds_active = "yes" if r.get("datastore_active") else "—"
                    rname = esc(truncate(r.get("name") or r.get("description") or r.get("id", "")[:8], 60))
                    rrows.append(f'  [{esc(fmt)}], [{size}], [{mod}], [{ds_active}], [{rname}]')
                out.append(',\n'.join(rrows))
                out.append(')')
                if len(resources) > 20:
                    out.append(f'#text(size: 8pt, fill: gray)[+ {len(resources)-20} more resources]')
                out.append('')

                # Sample row from first datastore-active resource
                for r in resources:
                    if r.get("datastore_active") and r["id"] in samples:
                        s = samples[r["id"]]
                        if "row" in s and s["row"]:
                            fields = s.get("fields", [])[:6]  # first 6 fields
                            row = s["row"]
                            total = s.get("total")
                            out.append('=== Sample row')
                            out.append(f'#text(size: 8pt, fill: gray)[Resource: `{r["id"]}` · Total rows: {total if total is not None else "?"}]\\')
                            out.append('#table(columns: (auto, 1fr), stroke: 0.3pt + gray, inset: 4pt,')
                            srows = []
                            for f in fields:
                                v = row.get(f, "")
                                v = esc(truncate(str(v), 200))
                                srows.append(f'  [#text(size: 8pt, weight: "bold")[{esc(f)}]], [#text(size: 8pt)[{v}]]')
                            out.append(',\n'.join(srows))
                            out.append(')')
                            out.append('')
                            break

            out.append('#line(length: 100%, stroke: 0.2pt + gray)')
            out.append('')

    TYP.write_text('\n'.join(out))
    print(f"wrote {TYP} ({TYP.stat().st_size//1024} KB)")

    print("rendering PDF...")
    r = subprocess.run(["typst", "compile", str(TYP), str(PDF)], capture_output=True, text=True)
    if r.returncode != 0:
        print("STDOUT:", r.stdout)
        print("STDERR:", r.stderr)
        raise SystemExit(r.returncode)
    print(f"wrote {PDF} ({PDF.stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
