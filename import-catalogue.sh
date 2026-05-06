#!/usr/bin/env bash
# import-catalogue.sh
#
# Pulls a fresh point-in-time snapshot of the data.gov.il CKAN catalogue
# into a timestamped folder (DDMMYY) at the repo root, then regenerates
# the English-language index and translation mapping.
#
# Folder convention:
#   ./<DDMMYY>/                       # snapshot root, e.g. ./060526/
#   ./<DDMMYY>/datasets-raw.json      # full package_search dump (paginated)
#   ./<DDMMYY>/README.md              # generated English catalogue index
#   ./<DDMMYY>/translations.json      # HE->EN mapping keyed by dataset slug
#   ./<DDMMYY>/build_index.py         # generator (committed alongside output)
#   ./<DDMMYY>/build_translations.py  # translation builder
#
# Why a per-snapshot folder rather than overwriting in place:
#   The catalogue mutates (new datasets, retired datasets, slug renames).
#   Keeping snapshots side-by-side gives a reproducible diff trail and lets
#   downstream consumers pin to a known state. Translation mappings carry
#   forward — `build_translations.py` reads the previous snapshot's
#   `translations.json` and reuses any entry already marked confidence=llm
#   or confidence=manual, so high-quality translations only need to be done
#   once.
#
# API notes (true at time of writing):
#   - data.gov.il is CKAN. The action API is open (no auth, no geo-block
#     observed from .il / EU / US during 2026-05-06 testing). The Hebrew
#     web UI is what's geo-restricted; the JSON API is not.
#   - `package_search?rows=1000` is the max page size. Paginate via `start=`.
#   - `status_show` returns 403; that's the only endpoint that's blocked.
#   - Resources flagged `datastore_active=true` are queryable as tables via
#     `datastore_search?resource_id=<uuid>` — no need to download the CSV.
#   - There are NO English title/description fields in the API. Every
#     translation has to be produced client-side; see build_translations.py
#     for the slug-derived + dictionary + LLM hybrid we use.
#
# Usage:
#   ./import-catalogue.sh                  # snapshot to today's DDMMYY folder
#   ./import-catalogue.sh 010126           # snapshot into a specific folder name
#
# Requirements: bash, curl, python3 (stdlib only).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
STAMP="${1:-$(date +%d%m%y)}"
DEST="$REPO_ROOT/$STAMP"
API="https://data.gov.il/api/3/action"

echo "==> Snapshot folder: $DEST"
mkdir -p "$DEST"
cd "$DEST"

# 1. Paginated dump of package_search (1000 rows/page until exhausted).
echo "==> Fetching catalogue (paginated package_search)..."
python3 - <<'PY'
import json, urllib.request, sys
API = "https://data.gov.il/api/3/action/package_search"
all_results = []
start = 0
while True:
    url = f"{API}?rows=1000&start={start}"
    with urllib.request.urlopen(url, timeout=60) as r:
        page = json.load(r)["result"]
    all_results += page["results"]
    print(f"   pulled {len(all_results)}/{page['count']}", file=sys.stderr)
    if len(all_results) >= page["count"]:
        break
    start += 1000
json.dump(all_results, open("datasets-raw.json", "w"), ensure_ascii=False)
print(f"   wrote datasets-raw.json ({len(all_results)} datasets)", file=sys.stderr)
PY

# 2. Copy the generator scripts forward from the most recent prior snapshot
#    so each folder is self-contained. (Edit them in place per snapshot if
#    the API surface changes.)
PRIOR=$(ls -d "$REPO_ROOT"/[0-9][0-9][0-9][0-9][0-9][0-9] 2>/dev/null \
        | grep -v "$DEST" | sort | tail -1 || true)
if [ -n "$PRIOR" ] && [ -d "$PRIOR" ]; then
    for f in build_index.py build_translations.py; do
        if [ ! -f "$DEST/$f" ] && [ -f "$PRIOR/$f" ]; then
            cp "$PRIOR/$f" "$DEST/$f"
            echo "==> Carried $f forward from $(basename "$PRIOR")"
        fi
    done
    # Reuse prior translations.json as a starting point so confidence=llm
    # / confidence=manual rows survive untouched.
    if [ ! -f "$DEST/translations.json" ] && [ -f "$PRIOR/translations.json" ]; then
        cp "$PRIOR/translations.json" "$DEST/translations.json"
        echo "==> Seeded translations.json from $(basename "$PRIOR")"
    fi
fi

# 3. Regenerate the English README index.
if [ -f "$DEST/build_index.py" ]; then
    echo "==> Building README.md..."
    python3 "$DEST/build_index.py"
fi

# 4. Refresh translation mapping (slug-derived + dictionary; LLM pass is manual).
if [ -f "$DEST/build_translations.py" ]; then
    echo "==> Building translations.json..."
    python3 "$DEST/build_translations.py"
fi

echo
echo "==> Done. Snapshot at $DEST"
ls -lh "$DEST"
