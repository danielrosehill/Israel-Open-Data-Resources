# PDF catalogue of CKAN data.gov.il

**Date:** 2026-05-06
**Status:** chosen

## Context
Need a readable bilingual (HE/EN) PDF catalogue of all data.gov.il datasets, grouped by organisation, with metadata (sizes, last updated, formats) and one sample row per resource where DataStore is enabled.

## Options considered
- **Scope** — translations-only / metadata-only / full + samples → **full + samples** chosen for completeness.
- **Translation** — keep messy auto-translations / Hebrew-only / LLM re-translate → **Haiku 4.5 re-translate** (~$2 one-time, idempotent on re-runs).
- **PDF tooling** — WeasyPrint / Pandoc / ReportLab / Typst → **Typst** chosen (clean RTL handling, fast, single-binary).

## Decision
- Re-fetch CKAN metadata into `datasets-raw.json` (paginated `package_search`).
- For each DataStore-active resource, fetch 1 sample row → `samples.json`.
- Translate titles + descriptions via Claude Haiku 4.5, batched ~10 per call, write to `translations.json` keyed by slug. Re-runs skip entries whose Hebrew source hash is unchanged.
- Generate Typst source → render `catalogue.pdf`.

## Consequences
- One-time API spend ~$1.50–$2.50.
- `translations.json` becomes the durable artefact; future snapshots diff against it and only re-translate changed/new datasets.
- PDF will be large (1194 datasets); table-of-contents per org keeps it navigable.
