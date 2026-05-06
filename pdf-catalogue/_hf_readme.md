---
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
portal. Each snapshot contains:

- A 600-page PDF catalogue grouped by publishing organisation, with metadata,
  resource lists, and one sample row per DataStore-active resource.
- The raw CKAN payload (every `package_show` field for every dataset).
- An English translation layer for titles + descriptions, produced by
  Gemini 2.0 Flash.
- One sample row per DataStore-active resource, fetched live at snapshot time.

> The data.gov.il portal is Hebrew-only in its UI. This dataset is intended to
> make the underlying catalogue navigable for non-Hebrew speakers and to give
> researchers a single, durable, date-stamped reference point.

## Latest snapshot

**2026-05-06** — 1194 datasets across 61
organisations · 2017 sampled resources.

[Browse latest →](snapshots/2026-05-06/)

## All snapshots

- [`snapshots/2026-05-06/`](snapshots/2026-05-06/)

## Why a snapshot, not a live mirror?

CKAN metadata (titles, descriptions, last-modified timestamps, resource counts)
shifts daily. A date-stamped snapshot lets researchers, journalists, and tooling
reference an immutable point-in-time view, and lets future snapshots be
diffed cleanly.

## Source code

Snapshot pipeline (CKAN fetch → samples → translation → Typst PDF → Hub push):
<https://github.com/danielrosehill/Israel-Open-Data-Resources>

## Licence

The catalogue metadata itself is published by the Government of Israel under
the standard data.gov.il terms. This bilingual repackaging (translations + PDF
layout) is released **CC BY 4.0** — attribution to Daniel Rosehill is
appreciated.
