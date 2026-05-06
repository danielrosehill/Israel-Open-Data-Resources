#!/usr/bin/env python3
"""Fetch full data.gov.il CKAN catalogue → datasets-raw.json."""
import json
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

HERE = Path(__file__).parent
OUT = HERE / "datasets-raw.json"
BASE = "https://data.gov.il/api/3/action"
PAGE = 1000


def get(url, retries=3):
    for i in range(retries):
        try:
            req = Request(url, headers={"User-Agent": "israel-open-data-catalogue/1.0"})
            with urlopen(req, timeout=60) as r:
                return json.load(r)
        except (URLError, HTTPError, TimeoutError) as e:
            if i == retries - 1:
                raise
            print(f"  retry {i+1}: {e}", file=sys.stderr)
            time.sleep(2 * (i + 1))


def main():
    all_pkgs = []
    start = 0
    while True:
        url = f"{BASE}/package_search?rows={PAGE}&start={start}"
        print(f"fetch start={start}")
        d = get(url)
        results = d["result"]["results"]
        total = d["result"]["count"]
        all_pkgs.extend(results)
        start += len(results)
        if start >= total or not results:
            break
    print(f"total: {len(all_pkgs)}")

    # Also fetch organization metadata
    orgs = get(f"{BASE}/organization_list?all_fields=true")["result"]
    print(f"orgs: {len(orgs)}")

    OUT.write_text(json.dumps({"datasets": all_pkgs, "organizations": orgs, "fetched_at": time.strftime("%Y-%m-%d")}, ensure_ascii=False, indent=2))
    print(f"wrote {OUT} ({OUT.stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
