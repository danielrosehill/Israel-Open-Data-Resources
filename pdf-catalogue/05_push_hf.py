#!/usr/bin/env python3
"""Sync the catalogue snapshot to the HuggingFace dataset.

Layout on the Hub:
  README.md                       (top-level, points at latest snapshot)
  snapshots/<YYYY-MM-DD>/
    catalogue.pdf
    datasets-raw.json
    samples.json
    translations.json
    README.md                     (snapshot-specific notes)
"""
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from huggingface_hub import HfApi, login

REPO_ID = "danielrosehill/Israel-Open-Data-Catalogue"
HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
SAMPLES = HERE / "samples.json"
TRANS = HERE / "translations.json"
CATALOG = HERE / "catalog.json"
PDF = HERE / "catalogue.pdf"
TYP = HERE / "catalogue.typ"


def fmt_size(p):
    n = p.stat().st_size
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def write_snapshot_readme(folder, stats):
    md = f"""# data.gov.il Catalogue — Snapshot {stats['date']}

Bilingual (Hebrew/English) catalogue of every dataset published on
[data.gov.il](https://data.gov.il), captured on **{stats['date']}** via the
public CKAN API.

## Primary artefact

**[`catalog.json`](catalog.json)** ({stats['catalog_size']}) — single merged
file. Each row is one dataset, with the original CKAN fields plus English
translations as `_en` suffixed siblings (e.g. `title` / `title_en`,
`notes` / `notes_en`). Each resource carries its sample row inline.

```python
import json
catalog = json.load(open("catalog.json"))
for ds in catalog["datasets"]:
    print(ds["title"], "→", ds["title_en"])
    for res in ds["resources"]:
        if "sample" in res:
            print(" ", res["format"], res["sample"]["fields"])
```

## Other artefacts

| File | Size | Description |
|---|---|---|
| `catalogue.pdf` | {stats['pdf_size']} | {stats['pages']}-page bilingual PDF, grouped by publishing organisation |
| `_sources/datasets-raw.json` | {stats['raw_size']} | Building block — raw CKAN `package_search` payload |
| `_sources/samples.json` | {stats['samples_size']} | Building block — sample rows keyed by resource id |
| `_sources/translations.json` | {stats['trans_size']} | Building block — translations keyed by dataset slug |

The files in `_sources/` are the inputs that were merged into `catalog.json`;
they are kept for reproducibility and incremental updates but most consumers
should use `catalog.json` directly.

## Snapshot statistics

- **Datasets:** {stats['datasets']}
- **Organisations:** {stats['orgs']}
- **Resources:** {stats['resources']} ({stats['datastore_resources']} DataStore-active)
- **DataStore resources sampled:** {stats['samples_ok']} / {stats['samples_total']}
- **Translations:** {stats['translations']} ({stats['translation_model']})

## Source

CKAN API at `https://data.gov.il/api/3/action/`. No authentication required.
See the source repo for the snapshot pipeline:
<https://github.com/danielrosehill/Israel-Open-Data-Resources>
"""
    (folder / "README.md").write_text(md)


def write_top_readme(stats, all_dates):
    dated_links = "\n".join(f"- [`snapshots/{d}/`](snapshots/{d}/)" for d in sorted(all_dates, reverse=True))
    md = f"""---
license: cc-by-4.0
language:
- he
- en
pretty_name: Israel Open Data Catalogue
tags:
- israel
- open-data
- ckan
- bilingual
- government
- catalogue
size_categories:
- 1K<n<10K
---

# Israel Open Data Catalogue (data.gov.il)

A bilingual (Hebrew/English) snapshot of the **entire** dataset catalogue
published on [data.gov.il](https://data.gov.il), Israel's official open-data
portal.

> The data.gov.il portal is Hebrew-only in its UI. This dataset is intended to
> make the underlying catalogue navigable for non-Hebrew speakers and to give
> researchers a single, durable, date-stamped reference point.

## What's in each snapshot

The primary artefact is **`catalog.json`** — a single merged file where each
row represents one dataset. Hebrew fields keep their CKAN names (`title`,
`notes`, …) and English translations sit beside them with an `_en` suffix
(`title_en`, `notes_en`). Each resource carries its sample row inline.

```python
import json
catalog = json.load(open("catalog.json"))
print(catalog["counts"])
for ds in catalog["datasets"][:3]:
    print(ds["title"], "→", ds["title_en"])
    for res in ds["resources"]:
        if "sample" in res:
            print(" ", res["format"], list(res["sample"]["row"].keys()))
```

Each snapshot folder also contains:
- `catalogue.pdf` — 650+ page bilingual PDF version, grouped by org
- `_sources/` — the building blocks (`datasets-raw.json`, `samples.json`,
  `translations.json`) that were merged to produce `catalog.json`

## Latest snapshot

**{stats['date']}** — {stats['datasets']} datasets across {stats['orgs']}
organisations, {stats['resources']} resources ({stats['samples_ok']} with
sample rows), {stats['translations']} translations.

[Browse latest →](snapshots/{stats['date']}/)

## All snapshots

{dated_links}

## Why a snapshot, not a live mirror?

CKAN metadata (titles, descriptions, last-modified timestamps, resource counts)
shifts daily. A date-stamped snapshot lets researchers, journalists, and tooling
reference an immutable point-in-time view, and lets future snapshots be
diffed cleanly.

## Source code & related

- Snapshot pipeline: <https://github.com/danielrosehill/Israel-Open-Data-Resources>
- Translation mapping (standalone): <https://github.com/danielrosehill/Israel-Open-Data-Catalogue-Translations>

## Licence

The catalogue metadata itself is published by the Government of Israel under
the standard data.gov.il terms. This bilingual repackaging (translations + PDF
layout + merged catalog) is released **CC BY 4.0** — attribution to Daniel
Rosehill is appreciated.
"""
    (HERE / "_hf_readme.md").write_text(md)
    return HERE / "_hf_readme.md"


def main():
    if not all(p.exists() for p in (RAW, SAMPLES, TRANS, PDF, CATALOG)):
        missing = [p.name for p in (RAW, SAMPLES, TRANS, PDF, CATALOG) if not p.exists()]
        print(f"missing: {missing}", file=sys.stderr)
        sys.exit(1)

    raw = json.loads(RAW.read_text())
    samples = json.loads(SAMPLES.read_text())
    trans = json.loads(TRANS.read_text())
    catalog = json.loads(CATALOG.read_text())

    pages = subprocess.run(["pdfinfo", str(PDF)], capture_output=True, text=True).stdout
    page_count = next((l.split()[1] for l in pages.splitlines() if l.startswith("Pages:")), "?")

    date = datetime.now().strftime("%Y-%m-%d")
    stats = {
        "date": date,
        "datasets": catalog["counts"]["datasets"],
        "orgs": catalog["counts"]["organizations"],
        "resources": catalog["counts"]["resources"],
        "datastore_resources": catalog["counts"]["datastore_resources"],
        "samples_ok": catalog["counts"]["sampled_resources"],
        "samples_total": len(samples),
        "translations": catalog["counts"]["translated_datasets"],
        "translation_model": next(iter(trans.values())).get("model", "unknown") if trans else "n/a",
        "pages": page_count,
        "pdf_size": fmt_size(PDF),
        "catalog_size": fmt_size(CATALOG),
        "raw_size": fmt_size(RAW),
        "samples_size": fmt_size(SAMPLES),
        "trans_size": fmt_size(TRANS),
    }

    api = HfApi()

    try:
        api.repo_info(repo_id=REPO_ID, repo_type="dataset")
        print(f"repo exists: {REPO_ID}")
    except Exception:
        print(f"creating repo: {REPO_ID}")
        api.create_repo(repo_id=REPO_ID, repo_type="dataset", private=False, exist_ok=True)

    # Build snapshot folder locally, then upload it
    staging = HERE / "_hf_staging" / "snapshots" / date
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    # Primary artefacts at snapshot root
    shutil.copy2(CATALOG, staging / CATALOG.name)
    shutil.copy2(PDF, staging / PDF.name)
    # Building blocks under _sources/
    sources = staging / "_sources"
    sources.mkdir()
    for src in (RAW, SAMPLES, TRANS):
        shutil.copy2(src, sources / src.name)
    write_snapshot_readme(staging, stats)

    # Existing snapshot dates from the hub
    try:
        listing = api.list_repo_files(repo_id=REPO_ID, repo_type="dataset")
        dates = sorted({p.split("/")[1] for p in listing if p.startswith("snapshots/") and len(p.split("/")) >= 3})
    except Exception:
        dates = []
    if date not in dates:
        dates.append(date)

    top_readme = write_top_readme(stats, dates)

    # If a previous push used the old flat layout, drop those stale files
    try:
        listing = api.list_repo_files(repo_id=REPO_ID, repo_type="dataset")
        prefix = f"snapshots/{date}/"
        stale = [
            p for p in listing
            if p.startswith(prefix)
            and p.split("/")[-1] in {"datasets-raw.json", "samples.json", "translations.json"}
            and "_sources" not in p
        ]
        for p in stale:
            print(f"  removing stale flat-layout file: {p}")
            api.delete_file(path_in_repo=p, repo_id=REPO_ID, repo_type="dataset",
                            commit_message=f"Remove flat-layout {p.split('/')[-1]}")
    except Exception as e:
        print(f"  (cleanup skipped: {e})")

    print(f"uploading snapshot folder snapshots/{date}/ ...")
    api.upload_folder(
        folder_path=str(staging),
        path_in_repo=f"snapshots/{date}",
        repo_id=REPO_ID,
        repo_type="dataset",
        commit_message=f"Snapshot {date} — merged catalog.json layout ({stats['datasets']} datasets)",
    )

    print("uploading top-level README ...")
    api.upload_file(
        path_or_fileobj=str(top_readme),
        path_in_repo="README.md",
        repo_id=REPO_ID,
        repo_type="dataset",
        commit_message=f"Update top README for snapshot {date}",
    )

    print(f"done. https://huggingface.co/datasets/{REPO_ID}")


if __name__ == "__main__":
    main()
