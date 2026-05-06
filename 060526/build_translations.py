#!/usr/bin/env python3
"""
Build a translation mapping for the data.gov.il catalogue snapshot.

The CKAN API exposes NO English title/description fields:
- `package` has `title` (Hebrew), `notes` (Hebrew, 96% of records), `name` (slug, always ASCII)
- `resource.Language` is either `Hebrew` or null — never `English`
- Only 13/1194 datasets ship a non-Hebrew `title` (driving-test pools in EN/AR/ES)

This script imputes a draft English title in two passes:

  Pass 1 (deterministic, runs by default):
    Convert the URL slug (`name`) into Title Case English.
    `financial-sanctions` -> "Financial Sanctions"
    `waste-information-system` -> "Waste Information System"
    Apply a manual term dictionary (HE->EN) over the Hebrew title for any
    obvious organisational words (משרד -> Ministry, רשות -> Authority, ...).

  Pass 2 (optional, requires Anthropic SDK + ANTHROPIC_API_KEY):
    For every entry where Pass 1 produced a low-confidence imputation
    (slug = pure transliteration, slug = numeric, etc.), call the Claude API
    with the Hebrew title + notes and persist a high-quality translation.

Output: `translations.json`, keyed by dataset slug, structured so future snapshots
can reuse mappings (only re-translating slugs that didn't exist before).

  {
    "<slug>": {
      "hebrew_title": "...",
      "hebrew_notes": "...",
      "english_title": "...",
      "english_notes": "...",
      "confidence": "slug-derived" | "dictionary" | "llm" | "manual",
      "translated_at": "2026-05-06"
    }
  }
"""
import json, re, sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "datasets-raw.json"
OUT = HERE / "translations.json"

# Hebrew->English term dictionary for common government vocabulary.
# Extend as needed. Order matters — longest match first when applying.
HE_EN = {
    "משרד הבריאות": "Ministry of Health",
    "משרד התחבורה": "Ministry of Transport",
    "משרד החינוך": "Ministry of Education",
    "משרד האוצר": "Ministry of Finance",
    "משרד החקלאות": "Ministry of Agriculture",
    "משרד הפנים": "Ministry of Interior",
    "משרד המשפטים": "Ministry of Justice",
    "משרד הכלכלה": "Ministry of Economy",
    "משרד הרווחה": "Ministry of Welfare",
    "משרד התיירות": "Ministry of Tourism",
    "משרד התרבות והספורט": "Ministry of Culture and Sport",
    "משרד הבינוי והשיכון": "Ministry of Construction and Housing",
    "משרד העבודה": "Ministry of Labor",
    "משרד האנרגיה": "Ministry of Energy",
    "המשרד להגנת הסביבה": "Ministry of Environmental Protection",
    "המשרד לשוויון חברתי": "Ministry of Social Equality",
    "הלשכה המרכזית לסטטיסטיקה": "Central Bureau of Statistics",
    "בנק ישראל": "Bank of Israel",
    "רשות שדות התעופה": "Israel Airports Authority",
    "רשות המים": "Water Authority",
    "רשות המסים": "Tax Authority",
    "רשות שוק ההון": "Capital Market Authority",
    "רשות האכיפה והגבייה": "Enforcement and Collection Authority",
    "ביטוח לאומי": "National Insurance",
    "המוסד לביטוח לאומי": "National Insurance Institute",
    "הכנסת": "Knesset",
    "ועדת הבחירות המרכזית": "Central Elections Committee",
    "ארכיון המדינה": "State Archives",
    "מנהל התכנון": "Planning Administration",
    "מינהל התכנון": "Planning Administration",
    "המרכז למיפוי ישראל": "Survey of Israel",
    "השירות המטאורולוגי": "Israel Meteorological Service",
    "משטרת ישראל": "Israel Police",
    "כבאות והצלה": "Fire and Rescue",
    "שירות התעסוקה": "Employment Service",
    "מערך הסייבר": "National Cyber Directorate",
    "מערך הדיגיטל": "National Digital Agency",
    # generic vocabulary
    "משרד": "Ministry",
    "רשות": "Authority",
    "מנהל": "Administration",
    "מינהל": "Administration",
    "מאגר": "Database",
    "רשימת": "List of",
    "רשימה": "List",
    "נתוני": "Data on",
    "נתונים": "Data",
    "דוח": "Report",
    "דו\"ח": "Report",
    "דו״ח": "Report",
    "סטטיסטיקה": "Statistics",
    "מפת": "Map of",
    "מפה": "Map",
    "אזור": "Region",
    "אזורים": "Regions",
    "ישראל": "Israel",
    "ירושלים": "Jerusalem",
    "תל אביב": "Tel Aviv",
    "חיפה": "Haifa",
    "באר שבע": "Beer Sheva",
    "תאונות": "Accidents",
    "טיסות": "Flights",
    "תחבורה": "Transport",
    "בריאות": "Health",
    "חינוך": "Education",
    "סביבה": "Environment",
    "מים": "Water",
    "אנרגיה": "Energy",
    "מס": "Tax",
    "מסים": "Taxes",
    "תקציב": "Budget",
    "בחירות": "Elections",
}


def slug_to_title(slug: str) -> str:
    """`waste-information-system` -> 'Waste Information System'."""
    parts = re.split(r"[-_]+", slug)
    fixed = []
    for p in parts:
        if not p:
            continue
        if p.isdigit():
            fixed.append(p)
        elif len(p) <= 4 and p.upper() == p:
            fixed.append(p.upper())  # acronyms in slug
        else:
            fixed.append(p.capitalize())
    return " ".join(fixed)


def apply_dict(text: str) -> str:
    """Substitute known HE phrases with EN. Longest match first."""
    if not text:
        return ""
    out = text
    for he in sorted(HE_EN.keys(), key=len, reverse=True):
        out = out.replace(he, HE_EN[he])
    return out


def is_pure_hebrew_slug(slug: str) -> bool:
    """True if slug is opaque (UUID, numeric-only) — needs LLM, not deterministic."""
    if re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-.*", slug):
        return True
    if slug.isdigit():
        return True
    return False


def main():
    data = json.load(open(RAW))
    existing = {}
    if OUT.exists():
        existing = json.load(open(OUT))

    today = str(date.today())
    out = {}
    stats = {"slug-derived": 0, "dictionary": 0, "kept-existing": 0, "needs-llm": 0}

    for p in data:
        slug = p["name"]
        he_title = p.get("title") or ""
        he_notes = p.get("notes") or ""

        # Reuse existing high-quality translation if present
        if slug in existing and existing[slug].get("confidence") in ("llm", "manual"):
            out[slug] = existing[slug]
            stats["kept-existing"] += 1
            continue

        if is_pure_hebrew_slug(slug):
            en_title = apply_dict(he_title) or "(needs translation)"
            confidence = "needs-llm"
            stats["needs-llm"] += 1
        else:
            slug_en = slug_to_title(slug)
            dict_en = apply_dict(he_title)
            # Prefer slug-derived when slug looks descriptive (>=2 words),
            # otherwise fall back to dictionary substitution over Hebrew title.
            if len(slug_en.split()) >= 2:
                en_title = slug_en
                confidence = "slug-derived"
                stats["slug-derived"] += 1
            else:
                en_title = dict_en or slug_en
                confidence = "dictionary"
                stats["dictionary"] += 1

        out[slug] = {
            "hebrew_title": he_title,
            "hebrew_notes": he_notes[:500],
            "english_title": en_title,
            "english_notes": apply_dict(he_notes)[:500] if he_notes else "",
            "confidence": confidence,
            "translated_at": today,
        }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT.name} ({len(out)} entries)")
    print("Confidence breakdown:")
    for k, v in stats.items():
        print(f"  {k:>15}: {v}")
    print("\nNext step: pipe entries with confidence='needs-llm' or 'dictionary'")
    print("through Claude/GPT for higher-quality translations, write back with")
    print("confidence='llm', and re-run — existing 'llm'/'manual' rows are preserved.")


if __name__ == "__main__":
    main()
