#!/usr/bin/env python3
"""Retry samples that errored, with backoff."""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

HERE = Path(__file__).parent
OUT = HERE / "samples.json"
BASE = "https://data.gov.il/api/3/action"


def fetch(rid, retries=4):
    url = f"{BASE}/datastore_search?resource_id={rid}&limit=1"
    for i in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "israel-open-data-catalogue/1.0"})
            with urlopen(req, timeout=45) as r:
                d = json.load(r)
            if d.get("success"):
                res = d["result"]
                fields = [f["id"] for f in res.get("fields", []) if not f["id"].startswith("_")]
                records = res.get("records", [])
                row = records[0] if records else None
                return rid, {"fields": fields, "row": row, "total": res.get("total")}
            return rid, {"error": "unsuccessful"}
        except HTTPError as e:
            if e.code == 503 and i < retries - 1:
                time.sleep(3 * (i + 1))
                continue
            return rid, {"error": f"HTTP {e.code}"}
        except (URLError, TimeoutError, json.JSONDecodeError) as e:
            if i < retries - 1:
                time.sleep(2 * (i + 1))
                continue
            return rid, {"error": str(e)[:120]}


def main():
    data = json.loads(OUT.read_text())
    todo = [r for r, v in data.items() if "error" in v]
    print(f"retrying {len(todo)}")
    done = 0
    with ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(fetch, r): r for r in todo}
        for f in as_completed(futs):
            rid, d = f.result()
            data[rid] = d
            done += 1
            if done % 100 == 0:
                ok = sum(1 for v in data.values() if "error" not in v)
                print(f"  {done}/{len(todo)} (total ok: {ok})")
                OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    ok = sum(1 for v in data.values() if "error" not in v)
    print(f"final: {ok}/{len(data)} ok")


if __name__ == "__main__":
    main()
