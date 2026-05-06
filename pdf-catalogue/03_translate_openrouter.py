#!/usr/bin/env python3
"""Translate dataset titles + descriptions via OpenRouter (cheap model).

Idempotent: skips entries whose Hebrew source hash matches the cached translation.
Output: translations.json (keyed by dataset slug/name).
"""
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from openai import OpenAI

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
OUT = HERE / "translations.json"

MODEL = os.getenv("OR_MODEL", "google/gemini-2.0-flash-001")
BATCH = 12
WORKERS = 8

SYSTEM = (
    "You translate Hebrew government dataset metadata into clear, professional English. "
    "Output only valid JSON. No commentary, no markdown fences. "
    "Translate idiomatically — never leave Hebrew words mixed inside English text. "
    "Preserve technical terms (CKAN, GIS, NIS, GTFS, etc.). Keep translations concise."
)


def src_hash(title, notes):
    return hashlib.sha256(((title or "") + "|" + (notes or "")).encode("utf-8")).hexdigest()[:16]


def translate_batch(client, items):
    payload = [
        {
            "slug": i["slug"],
            "hebrew_title": i["title"],
            "hebrew_description": (i["notes"] or "")[:1500],
        }
        for i in items
    ]
    user = (
        "Translate each Hebrew dataset entry to English. Return ONLY a JSON array (no markdown, no prose), "
        "one object per input, in the same order, with keys: "
        "slug, english_title, english_description. "
        "If the Hebrew description is empty, return english_description as an empty string. "
        "Keep english_description under 400 characters when possible.\n\n"
        f"Input: {json.dumps(payload, ensure_ascii=False)}"
    )
    last_err = None
    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": user},
                ],
                temperature=0.1,
                max_tokens=4000,
                response_format={"type": "json_object"} if "gemini" not in MODEL else None,
            )
            text = resp.choices[0].message.content.strip()
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            # gemini sometimes wraps in {"results": [...]}
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                for k in ("results", "translations", "data", "items"):
                    if k in parsed and isinstance(parsed[k], list):
                        parsed = parsed[k]
                        break
            if not isinstance(parsed, list):
                raise ValueError(f"expected list, got {type(parsed).__name__}")
            out = {}
            for r in parsed:
                if "slug" in r:
                    out[r["slug"]] = {
                        "english_title": r.get("english_title", ""),
                        "english_description": r.get("english_description", ""),
                    }
            usage = resp.usage
            return out, (usage.prompt_tokens if usage else 0, usage.completion_tokens if usage else 0)
        except Exception as e:
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    print(f"  batch failed after retries: {last_err}", file=sys.stderr)
    return {}, (0, 0)


def main():
    key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OR_API_KEY")
    if not key:
        print("ERROR: OPENROUTER_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key,
        default_headers={
            "HTTP-Referer": "https://github.com/danielrosehill/Israel-Open-Data-Resources",
            "X-Title": "Israel Open Data Catalogue",
        },
    )

    raw = json.loads(RAW.read_text())
    cache = {}
    if OUT.exists():
        try:
            cache = json.loads(OUT.read_text())
        except json.JSONDecodeError:
            cache = {}

    todo = []
    for ds in raw["datasets"]:
        slug = ds["name"]
        title = ds.get("title") or ""
        notes = ds.get("notes") or ""
        h = src_hash(title, notes)
        prev = cache.get(slug)
        if prev and prev.get("source_hash") == h and prev.get("english_title"):
            continue
        todo.append({"slug": slug, "title": title, "notes": notes, "hash": h})

    print(f"model: {MODEL}")
    print(f"to translate: {len(todo)} (cached: {len(cache)})")

    batches = [todo[i : i + BATCH] for i in range(0, len(todo), BATCH)]
    total_in = total_out = 0
    completed_batches = 0

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(translate_batch, client, b): b for b in batches}
        for f in as_completed(futs):
            chunk = futs[f]
            result, (tin, tout) = f.result()
            total_in += tin
            total_out += tout
            for item in chunk:
                r = result.get(item["slug"])
                if not r:
                    continue
                cache[item["slug"]] = {
                    "hebrew_title": item["title"],
                    "hebrew_notes": item["notes"],
                    "english_title": r["english_title"],
                    "english_description": r["english_description"],
                    "source_hash": item["hash"],
                    "model": MODEL,
                    "translated_at": time.strftime("%Y-%m-%d"),
                }
            completed_batches += 1
            if completed_batches % 5 == 0 or completed_batches == len(batches):
                done_items = sum(len(b) for b in batches[:completed_batches])
                print(
                    f"  {completed_batches}/{len(batches)} batches "
                    f"(~{done_items} datasets) | tokens in={total_in} out={total_out}"
                )
                OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=2))

    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
    # Gemini 2.0 Flash via OpenRouter: ~$0.10/M in, $0.40/M out (approx)
    cost = (total_in / 1_000_000) * 0.10 + (total_out / 1_000_000) * 0.40
    print(f"done. tokens in={total_in} out={total_out} approx_cost=${cost:.3f}")


if __name__ == "__main__":
    main()
