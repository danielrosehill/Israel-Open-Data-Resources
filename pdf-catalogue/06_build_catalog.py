#!/usr/bin/env python3
"""Merge raw CKAN, samples, and translations into a single catalog.json.

Schema: a top-level object with snapshot metadata + a `datasets` array.
Each dataset row contains the source CKAN fields plus _en suffixed
translations and per-resource sample data inlined.
"""
import json
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
SAMPLES = HERE / "samples.json"
TRANS = HERE / "translations.json"
OUT = HERE / "catalog.json"


def main():
    raw = json.loads(RAW.read_text())
    samples = json.loads(SAMPLES.read_text())
    trans = json.loads(TRANS.read_text())

    rows = []
    for ds in raw["datasets"]:
        slug = ds["name"]
        t = trans.get(slug, {})

        org_he = ds.get("organization") or {}
        org_slug = org_he.get("name")

        resources_out = []
        for r in ds.get("resources", []):
            rid = r.get("id")
            sample = samples.get(rid) if rid else None
            res = {
                "id": rid,
                "name": r.get("name"),
                "description": r.get("description"),
                "format": r.get("format"),
                "mimetype": r.get("mimetype"),
                "size": r.get("size"),
                "url": r.get("url"),
                "created": r.get("created"),
                "last_modified": r.get("last_modified"),
                "datastore_active": r.get("datastore_active", False),
                "datastore_contains_all_records_of_source_file": r.get(
                    "datastore_contains_all_records_of_source_file"
                ),
                "frequency": r.get("Frequency"),
                "how_update": r.get("how_update"),
                "category": r.get("category"),
            }
            if sample and "error" not in sample:
                res["sample"] = {
                    "fields": sample.get("fields"),
                    "row": sample.get("row"),
                    "total_rows": sample.get("total"),
                }
            elif sample and "error" in sample:
                res["sample_error"] = sample["error"]
            resources_out.append(res)

        rows.append({
            "slug": slug,
            "id": ds.get("id"),
            "title": ds.get("title"),
            "title_en": t.get("english_title") or "",
            "notes": ds.get("notes"),
            "notes_en": t.get("english_description") or "",
            "url": f"https://data.gov.il/dataset/{slug}",
            "organization": {
                "slug": org_slug,
                "title": org_he.get("title"),
                "id": org_he.get("id"),
            },
            "metadata_created": ds.get("metadata_created"),
            "metadata_modified": ds.get("metadata_modified"),
            "frequency": ds.get("Frequency"),
            "update": ds.get("Update"),
            "license_id": ds.get("license_id"),
            "license_title": ds.get("license_title"),
            "author": ds.get("author"),
            "author_email": ds.get("author_email"),
            "maintainer": ds.get("maintainer"),
            "maintainer_email": ds.get("maintainer_email"),
            "num_resources": ds.get("num_resources"),
            "num_tags": ds.get("num_tags"),
            "remark": ds.get("remark"),
            "translation": {
                "model": t.get("model"),
                "translated_at": t.get("translated_at"),
                "source_hash": t.get("source_hash"),
            } if t else None,
            "resources": resources_out,
        })

    rows.sort(key=lambda r: ((r["organization"]["slug"] or "zzz"), r["slug"]))

    out = {
        "snapshot_date": raw.get("fetched_at") or datetime.now().strftime("%Y-%m-%d"),
        "source": "https://data.gov.il (CKAN action API)",
        "license": {
            "metadata": "Government of Israel data.gov.il terms",
            "translations": "CC BY 4.0 (Daniel Rosehill)",
        },
        "translation_model": "google/gemini-2.0-flash-001",
        "counts": {
            "datasets": len(rows),
            "organizations": len({r["organization"]["slug"] for r in rows if r["organization"]["slug"]}),
            "resources": sum(len(r["resources"]) for r in rows),
            "datastore_resources": sum(1 for r in rows for res in r["resources"] if res.get("datastore_active")),
            "sampled_resources": sum(1 for r in rows for res in r["resources"] if "sample" in res),
            "translated_datasets": sum(1 for r in rows if r["title_en"]),
        },
        "datasets": rows,
    }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"wrote {OUT} ({OUT.stat().st_size//1024} KB)")
    print(json.dumps(out["counts"], indent=2))


if __name__ == "__main__":
    main()
