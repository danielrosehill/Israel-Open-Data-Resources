#!/usr/bin/env python3
"""Translate dataset titles + descriptions via Claude Haiku.

Idempotent: skips entries whose Hebrew source hash matches the cached translation.
Output: translations.json (keyed by dataset slug/name).
"""
import hashlib
import json
import os
import sys
import time
from pathlib import Path

from anthropic import Anthropic

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
OUT = HERE / "translations.json"

MODEL = "claude-haiku-4-5-20251001"
BATCH = 10
SYSTEM = (
    "You translate Hebrew government dataset metadata into clear, professional English. "
    "Output only valid JSON matching the requested shape. No commentary. "
    "Translate idiomatically — do NOT leave Hebrew words mixed into English. "
    "Preserve technical terms (e.g. CKAN, GIS, NIS) as-is. Keep translations concise."
)


def src_hash(title, notes):
    return hashlib.sha256(((title or "") + "|" + (notes or "")).encode("utf-8")).hexdigest()[:16]


def translate_batch(client, items):
    """items: list of {slug, title, notes}. Returns dict slug -> {title_en, notes_en}."""
    payload = [{"slug": i["slug"], "hebrew_title": i["title"], "hebrew_description": i["notes"][:1500] if i["notes"] else ""} for i in items]
    user = (
        "Translate each Hebrew dataset entry to English. Return ONLY a JSON array, one object per input, "
        "in the same order, with keys: slug, english_title, english_description. "
        "If the Hebrew description is empty, return english_description as an empty string. "
        "Keep the description under 400 characters when possible.\n\n"
        f"Input:\n{json.dumps(payload, ensure_ascii=False)}"
    )
    for attempt in range(4):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=4096,
                system=SYSTEM,
                messages=[{"role": "user", "content": user}],
            )
            text = resp.content[0].text.strip()
            # strip code fences if present
            if text.startswith("```"):
                text = text.split("```", 2)[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip()
            arr = json.loads(text)
            out = {}
            for r in arr:
                out[r["slug"]] = {"english_title": r.get("english_title", ""), "english_description": r.get("english_description", "")}
            return out, resp.usage
        except Exception as e:
            print(f"  batch retry {attempt+1}: {e}", file=sys.stderr)
            time.sleep(2 * (attempt + 1))
    return {}, None


def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

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

    print(f"to translate: {len(todo)} (cached: {len(cache)})")

    client = Anthropic()
    total_in = 0
    total_out = 0
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i+BATCH]
        result, usage = translate_batch(client, chunk)
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
        if usage:
            total_in += usage.input_tokens
            total_out += usage.output_tokens
        if (i // BATCH) % 5 == 0:
            done = min(i + BATCH, len(todo))
            print(f"  {done}/{len(todo)} | tokens in={total_in} out={total_out}")
            OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=2))

    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
    cost = (total_in / 1_000_000) * 1.0 + (total_out / 1_000_000) * 5.0
    print(f"done. tokens in={total_in} out={total_out} approx_cost=${cost:.2f}")


if __name__ == "__main__":
    main()
