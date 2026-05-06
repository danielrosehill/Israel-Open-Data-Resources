#!/usr/bin/env python3
"""Fetch one sample row per DataStore-active resource → samples.json."""
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
OUT = HERE / "samples.json"
BASE = "https://data.gov.il/api/3/action"


def fetch(rid):
    url = f"{BASE}/datastore_search?resource_id={rid}&limit=1"
    try:
        req = Request(url, headers={"User-Agent": "israel-open-data-catalogue/1.0"})
        with urlopen(req, timeout=30) as r:
            d = json.load(r)
        if d.get("success"):
            res = d["result"]
            fields = [f["id"] for f in res.get("fields", []) if not f["id"].startswith("_")]
            records = res.get("records", [])
            row = records[0] if records else None
            return rid, {"fields": fields, "row": row, "total": res.get("total")}
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError) as e:
        return rid, {"error": str(e)[:120]}
    return rid, {"error": "unsuccessful"}


def main():
    raw = json.loads(RAW.read_text())
    rids = []
    for ds in raw["datasets"]:
        for r in ds.get("resources", []):
            if r.get("datastore_active"):
                rids.append(r["id"])
    rids = list(set(rids))
    print(f"resources to sample: {len(rids)}")

    existing = {}
    if OUT.exists():
        existing = json.loads(OUT.read_text())
        rids = [r for r in rids if r not in existing]
        print(f"already cached: {len(existing)}; remaining: {len(rids)}")

    results = dict(existing)
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch, r): r for r in rids}
        for f in as_completed(futs):
            rid, data = f.result()
            results[rid] = data
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(rids)}")
                OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2))

    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2))
    ok = sum(1 for v in results.values() if "error" not in v)
    print(f"done: {ok} ok, {len(results)-ok} errors, total {len(results)}")


if __name__ == "__main__":
    main()
