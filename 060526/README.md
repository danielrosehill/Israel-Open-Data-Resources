# data.gov.il — English Catalogue Index
**Snapshot:** 2026-05-06 · **Source:** https://data.gov.il (CKAN portal)
**Coverage:** 1194 datasets across 61 publishing organizations · 3677 resource files · 2019 DataStore-queryable resources.
> Native UI is Hebrew-only; this index is generated from the public CKAN API (no auth, no geo-restriction observed from .il, EU, US testing). Dataset titles are kept in their original Hebrew alongside the URL slug (which is often a transliteration or English keyword) so they can be located in the portal.

## API endpoints
The portal runs CKAN, so all standard CKAN action API endpoints work:

| Endpoint | Purpose |
| --- | --- |
| `GET https://data.gov.il/api/3/action/package_list` | All dataset slugs |
| `GET https://data.gov.il/api/3/action/package_search?q=<query>&rows=1000&start=0` | Paginated dataset search (1000/page) |
| `GET https://data.gov.il/api/3/action/package_show?id=<slug>` | Full metadata for one dataset |
| `GET https://data.gov.il/api/3/action/organization_list?all_fields=true` | All 61 publishing orgs |
| `GET https://data.gov.il/api/3/action/organization_show?id=<slug>&include_datasets=true` | Datasets by org |
| `GET https://data.gov.il/api/3/action/datastore_search?resource_id=<uuid>&limit=100` | Tabular query against a DataStore-active resource |
| `GET https://data.gov.il/api/3/action/datastore_search_sql?sql=<sql>` | SQL query (where enabled) |
| `GET https://data.gov.il/api/3/action/datastore_search?resource_id=<uuid>&q=<term>` | Full-text search inside a resource |

**Quirks noted at snapshot time:**
- `status_show` returns HTTP 403 (otherwise the API is open).
- Per-org `package_count` is null on `organization_list` — counts must be computed from `package_search` results (already done below).
- Both groups (`firstgroup`, `second-group`) are empty placeholders; categorisation is by **organization**, not group.
- Resource URLs follow `https://data.gov.il/dataset/<dataset-uuid>/resource/<resource-uuid>/download/<file>` and are direct downloads.
- Bulk pulls: `package_search?rows=1000` returns up to 1000 records — paginate with `start=`.

**Example: tabular query for live flight data (Israel Airports Authority):**
```
curl 'https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=5'
```

## Catalogue by category

### Statistics
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Central Bureau of Statistics (CBS)](#lamas)** (`lamas`) | 14 | הלשכה המרכזית לסטטיסטיקה |

### Geospatial
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Survey of Israel (Mapping Center)](#israel_mapping_center)** (`israel_mapping_center`) | 116 | המרכז למיפוי ישראל |

### Transport
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Transport & Road Safety](#ministry_of_transport)** (`ministry_of_transport`) | 180 | משרד התחבורה והבטיחות בדרכים |
| **[National Road Safety Authority](#betihut-drahim)** (`betihut-drahim`) | 1 | הרשות הלאומית לבטיחות בדרכים |

### Health
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Health](#ministry-health)** (`ministry-health`) | 56 | משרד הבריאות |

### Environment
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Environmental Protection](#ministry_of_the_environment)** (`ministry_of_the_environment`) | 85 | המשרד להגנת הסביבה |

### Water
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Israel Water Authority](#water_authority)** (`water_authority`) | 49 | הרשות הממשלתית למים ולביוב |

### Energy
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Energy](#energy_and_water)** (`energy_and_water`) | 7 | משרד האנרגיה  |

### Weather
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Israel Meteorological Service](#meteorological_service)** (`meteorological_service`) | 5 | השירות המטאורולוגי |

### Finance
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Finance](#mof)** (`mof`) | 60 | משרד האוצר |
| **[Bank of Israel](#bank_israel)** (`bank_israel`) | 30 | בנק ישראל |
| **[Capital Market, Insurance & Savings Authority](#cma)** (`cma`) | 9 | רשות שוק ההון, ביטוח וחיסכון |
| **[Israel Tax Authority](#taxes-authority)** (`taxes-authority`) | 5 | רשות המסים בישראל |

### Economy
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Economy & Industry](#moital)** (`moital`) | 17 | משרד הכלכלה והתעשייה |

### Labour
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Labor](#labor)** (`labor`) | 18 | משרד העבודה |
| **[Israel Employment Service](#ies)** (`ies`) | 7 | שירות התעסוקה |

### Welfare
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Welfare & Social Affairs](#ministry_of_social_affairs)** (`ministry_of_social_affairs`) | 40 | משרד הרווחה והביטחון החברתי |
| **[National Insurance Institute (Bituah Leumi)](#social_security)** (`social_security`) | 21 | המוסד לביטוח לאומי |
| **[Ministry of Social Equality](#socialequality)** (`socialequality`) | 8 | המשרד לשוויון חברתי |
| **[Holocaust Survivors' Rights Authority](#holocaust_survivors_rights)** (`holocaust_survivors_rights`) | 5 | הרשות לזכויות ניצולי השואה |

### Education
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Education](#ministry_of_education)** (`ministry_of_education`) | 24 | משרד החינוך |
| **[Rural Education Administration](#rural-education)** (`rural-education`) | 2 | המינהל לחינוך התיישבותי |

### Science
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Innovation, Science & Technology](#science-and-technology)** (`science-and-technology`) | 29 | משרד החדשנות, המדע והטכנולוגיה |

### Housing
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Housing & Construction](#ministry_of_housing)** (`ministry_of_housing`) | 12 | משרד הבינוי והשיכון |

### Land
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Israel Land Authority](#the_israel_lands_administration)** (`the_israel_lands_administration`) | 3 | רשות מקרקעי ישראל |

### Planning
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Planning Administration](#iplan)** (`iplan`) | 13 | מינהל התכנון  |

### Justice
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Justice](#ministry_of_justice)** (`ministry_of_justice`) | 82 | משרד המשפטים |
| **[Enforcement & Collection Authority](#eca)** (`eca`) | 4 | רשות האכיפה והגבייה |
| **[Judicial Authority (Courts)](#the_judicial_authority)** (`the_judicial_authority`) | 3 | הרשות השופטת |

### Public Safety
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Fire & Rescue Commission](#firefightingcommission)** (`firefightingcommission`) | 9 | כבאות והצלה לישראל |
| **[Israel Police](#israel-police)** (`israel-police`) | 4 | משטרת ישראל |
| **[Ministry of National Security](#ministry_of_internal_security)** (`ministry_of_internal_security`) | 3 | המשרד לביטחון הפנים |

### Cyber
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Israel National Cyber Directorate](#israel_national_cyber_directorate)** (`israel_national_cyber_directorate`) | 1 | מערך הסייבר הלאומי |

### Elections
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Central Elections Committee (Knesset)](#central-election-committee)** (`central-election-committee`) | 2 | ועדת הבחירות המרכזית לכנסת |

### Government
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Interior](#interior_affairs)** (`interior_affairs`) | 13 | משרד הפנים |
| **[Ministry of Foreign Affairs](#ministry_of_exterior)** (`ministry_of_exterior`) | 10 | משרד החוץ |
| **[Prime Minister's Office](#pmo)** (`pmo`) | 10 | משרד ראש הממשלה  |
| **[National Digital Agency](#cio)** (`cio`) | 8 | מערך הדיגיטל הלאומי |
| **[Knesset (Parliament)](#knesset)** (`knesset`) | 8 | הכנסת |
| **[Israel State Archives](#archives)** (`archives`) | 2 | ארכיון המדינה |
| **[Government Procurement Administration](#governmentprocurementadministration)** (`governmentprocurementadministration`) | 2 | מינהל הרכש הממשלתי |
| **[GOV.IL (general)](#gov-il)** (`gov-il`) | 2 | GOV |
| **[Civil Service Commission](#netzivot)** (`netzivot`) | 2 | נציבות שירות המדינה |
| **[Regulatory Affairs Authority](#regulatory-authority)** (`regulatory-authority`) | 2 | רשות האסדרה |
| **[Nativ (Liaison Bureau)](#nativ)** (`nativ`) | 1 | משרד ראש הממשלה, "נתיב" |

### Communications
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Communications](#tikshoret)** (`tikshoret`) | 11 | משרד התקשורת |

### Culture
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Culture & Sport](#culture_and_sports)** (`culture_and_sports`) | 32 | משרד התרבות והספורט |

### Tourism
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Tourism](#ministry_of_tourism)** (`ministry_of_tourism`) | 11 | משרד התיירות |

### Agriculture
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Agriculture & Food Security](#ministry_of_agriculture)** (`ministry_of_agriculture`) | 18 | משרד החקלאות וביטחון המזון |
| **[Volcani Agricultural Research](#volcaniagri)** (`volcaniagri`) | 3 | מינהל המחקר החקלאי - מרכז וולקני |

### Immigration
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Aliyah & Integration](#ministry_of_immigrant_absorption)** (`ministry_of_immigrant_absorption`) | 17 | משרד העלייה והקליטה |
| **[Population & Immigration Authority](#population_authority)** (`population_authority`) | 9 | רשות האוכלוסין וההגירה |

### Religion
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Ministry of Religious Services](#religion-office)** (`religion-office`) | 12 | המשרד לשירותי דת |
| **[Rabbinical Courts](#rabinical_court)** (`rabinical_court`) | 9 | בתי הדין הרבניים |
| **[Chief Rabbinate](#rabanot)** (`rabanot`) | 5 | הרבנות הראשית לישראל |

### Aviation
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Israel Airports Authority](#airport_authority)** (`airport_authority`) | 4 | רשות שדות התעופה |

### Municipal
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Be'er Sheva Municipality](#beer-sheva)** (`beer-sheva`) | 44 | עיריית באר שבע |
| **[Ma'ale Adumim Municipality](#maaleedumim)** (`maaleedumim`) | 20 | עיריית מעלה אדומים |
| **[Haifa Municipality](#haifa)** (`haifa`) | 9 | עיריית חיפה |
| **[Petah Tikva Municipality](#petah-tikva-municipality)** (`petah-tikva-municipality`) | 4 | עיריית פתח תקוה |

### Other
| Org | Datasets | Hebrew name |
| --- | ---: | --- |
| **[Synthetic / test data](#synthetic)** (`synthetic`) | 2 | מידע סינתטי ממשלתי |

---

## Datasets by organization

### Ministry of Transport & Road Safety
<a id="ministry_of_transport"></a>
**Slug:** `ministry_of_transport` · **Hebrew:** משרד התחבורה והבטיחות בדרכים · **Category:** Transport · **Datasets:** 180

- Org page: https://data.gov.il/organization/ministry_of_transport
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_transport&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2010-2019`](https://data.gov.il/dataset/2010-2019) | קובץ אחוד ארצי של סקרי הרגלי נסיעה 2010-2019 | PDF/ZIP · 3 files | — |
| 2 | [`2030`](https://data.gov.il/dataset/2030) | צפיפות מקומות עבודה לשנת 2030 | CSV/PDF/ZIP · 1/4 DataStore | `11eb5ea7-8e3c-4c16-bb24-aaad5e16756f` |
| 3 | [`257`](https://data.gov.il/dataset/257) | פרסום מידע תעופתי פנים ארצי | RSS | — |
| 4 | [`258`](https://data.gov.il/dataset/258) | מאגר דוחות חקירה בטיחותיים | RSS | — |
| 5 | [`a3`](https://data.gov.il/dataset/a3) | database of questions and answers for a dedicated theoretical test for electric bicycle vehicles | XLSX · 1/1 DataStore | `76d032de-222b-4c27-9bf6-5229d41ed379` |
| 6 | [`a3-fr`](https://data.gov.il/dataset/a3-fr) | מאגר השאלות והתשובות הרשמי למבחן עיוני ייעודי לרוכבי אופניים חשמליים (A3) בשפה הצרפתית | XLSX · 1/1 DataStore | `cbd353f3-94e4-41d6-9bbd-4c0751fa0a4b` |
| 7 | [`a3-ru`](https://data.gov.il/dataset/a3-ru) | מאגר השאלות והתשובות הרשמי למבחן עיוני ייעודי לרוכבי אופניים חשמליים (A3) בשפה הרוסית | XLSX · 1/1 DataStore | `96c18b29-a098-43d6-9ca7-1787711e089b` |
| 8 | [`a3_aa`](https://data.gov.il/dataset/a3_aa) | מאגר השאלות והתשובות הרשמי למבחן עיוני ייעודי לרוכבי אופניים חשמליים (A3) בשפה האמהרית | XLSX · 1/1 DataStore | `25619d6d-37f0-4163-87cc-78e142ae0ebd` |
| 9 | [`a3_sp`](https://data.gov.il/dataset/a3_sp) | מאגר השאלות והתשובות הרשמי למבחן עיוני ייעודי לרוכבי אופניים חשמליים (A3) בשפה הספרדית | XLSX · 1/1 DataStore | `b61c8402-a846-4943-8f08-7d45a36ce541` |
| 10 | [`accid_taz`](https://data.gov.il/dataset/accid_taz) | תאונות דרכים לפי אזורי תנועה | CSV/XLSX/ZIP · 2/4 DataStore | `57c5aef9-70f9-4b71-82fa-52304cfbd031` |
| 11 | [`accidents_municipal`](https://data.gov.il/dataset/accidents_municipal) | תאונות דרכים לפי רשות מוניציפלית | CSV/XLSX/ZIP · 2/4 DataStore | `b17b1634-c001-4d37-96c6-a661b2ecd98c` |
| 12 | [`agg_charge_stations`](https://data.gov.il/dataset/agg_charge_stations) | עמדות טעינה לרכב חשמלי | CSV/XLSX/ZIP · 2/4 DataStore | `528482f2-d410-4d62-8b17-566ab23a1c52` |
| 13 | [`aircraft_data_il`](https://data.gov.il/dataset/aircraft_data_il) | נתוני כלי טיס ישראליים | CSV · 1/1 DataStore | `bc00ed41-75d0-4d0f-9eca-3cd0a2c332cc` |
| 14 | [`airport`](https://data.gov.il/dataset/airport) | שדות תעופה אזרחיים | CSV/PDF/ZIP · 1/4 DataStore | `1176fc86-c40e-4b9c-ade2-ed3829d3dd0f` |
| 15 | [`airstrip`](https://data.gov.il/dataset/airstrip) | מנחתים | CSV/PDF/XLSX/ZIP · 2/5 DataStore | `c39a02e2-3956-4b09-9a45-d3a1486f07bc` |
| 16 | [`alhakav`](https://data.gov.il/dataset/alhakav) | מרכזי שירות ומידע על-הקו | XLSX · 1/1 DataStore | `3322791c-0450-404a-9e19-416fc9693537` |
| 17 | [`amount_monthly_closures_vehicles`](https://data.gov.il/dataset/amount_monthly_closures_vehicles) | כמות כלי רכב חדשים בעלי קוד דגם העולים על הכביש בכל חודש | CSV · 1/1 DataStore | `602ac32d-19c0-4b41-88e0-e3ce8a7e80b7` |
| 18 | [`area_authority`](https://data.gov.il/dataset/area_authority) | רשות תמרור מתחמים | CSV/XLSX/ZIP · 2/4 DataStore | `5056917d-fc31-4b0e-b40b-203958b8dbd9` |
| 19 | [`arrivaltostationdayandhours`](https://data.gov.il/dataset/arrivaltostationdayandhours) | מאגר זמני הגעה לתחנה VM ברמת יום ושעה | CSV · 4/4 DataStore | `e3673768-3dc2-4e62-b0ea-cf763c07a037` |
| 20 | [`arrivaltostationhours`](https://data.gov.il/dataset/arrivaltostationhours) | זמני הגעה לתחנה VM ברמת שעה | CSV · 4/4 DataStore | `ad60edd5-33f8-47e9-9407-f70be4a7dcdd` |
| 21 | [`ashdod_metro_bus`](https://data.gov.il/dataset/ashdod_metro_bus) | אשדוד מטרו בס | CSV/XLSX/ZIP · 2/4 DataStore | `dadb68b2-ed9f-45e6-b41b-80b23f72ec20` |
| 22 | [`ayalontrafficcounts`](https://data.gov.il/dataset/ayalontrafficcounts) | ספירות תנועה תקופתיות בדרך 20 (נתיבי איילון) | PDF/ZIP · 4 files | — |
| 23 | [`batei-esek`](https://data.gov.il/dataset/batei-esek) | סחר, יבוא וייצור מוצרי תעבורה | CSV · 1/1 DataStore | `42e73a60-7acc-4c5d-b4ec-b0e468a73c51` |
| 24 | [`bicycle_jer_2019`](https://data.gov.il/dataset/bicycle_jer_2019) | שבילי אופניים בירושלים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `6b58e84b-1e34-46e1-b6cc-90068ddc0162` |
| 25 | [`bike_net_center`](https://data.gov.il/dataset/bike_net_center) | רשת רכיבה מחוז מרכז | CSV/PDF/ZIP · 1/4 DataStore | `af8f8d15-fa17-4a83-9c82-02604a7a52a3` |
| 26 | [`bike_net_tlv`](https://data.gov.il/dataset/bike_net_tlv) | רשת רכיבה מחוז תל אביב | CSV/PDF/ZIP · 1/5 DataStore | `d45559c9-2c81-483c-9b86-4ebde6c646b2` |
| 27 | [`bitzua_bus_trip`](https://data.gov.il/dataset/bitzua_bus_trip) | תכנון מול ביצוע נסיעות אוטובוסים ברמת נסיעה בודדת | CSV · 2/2 DataStore | `084b8e33-e359-47aa-95f7-26782e52c9af` |
| 28 | [`bph_infra_exist`](https://data.gov.il/dataset/bph_infra_exist) | שבילי אופניים - תשתית רכיבה קיימת | CSV/XLSX/ZIP · 1/4 DataStore | `6c6f191a-0839-411d-ac4f-59abe36a3593` |
| 29 | [`bph_infra_plan`](https://data.gov.il/dataset/bph_infra_plan) | שבילי אופניים - תשתית רכיבה מתוכננת | CSV/XLSX/ZIP · 1/4 DataStore | `560aff58-62b2-4853-b8c8-bab0069a736f` |
| 30 | [`brt_line`](https://data.gov.il/dataset/brt_line) | קווי תכנון נתיבים לתעבורת אוטובוסים מהירה BRT | CSV/XLSX/ZIP · 2/4 DataStore | `1859ef16-1f1e-45d1-8265-297e8be40fde` |
| 31 | [`bus_fleet`](https://data.gov.il/dataset/bus_fleet) | ציי רכב אוטובוסים | CSV · 1/1 DataStore | `91d298ed-a260-4f93-9d50-d5e3c5b82ce1` |
| 32 | [`bus_rishui_bitzua_2021`](https://data.gov.il/dataset/bus_rishui_bitzua_2021) | תכנון וביצוע אוטובוסים | CSV · 7/7 DataStore | `588dfec1-b95c-495b-a1f4-e1ca4278be5d` |
| 33 | [`bus_speed`](https://data.gov.il/dataset/bus_speed) | אוטובוסים - מהירות נסיעה | CSV/KMZ/PDF/SHP/XLSX · 1/5 DataStore | `ccea1923-e1b2-4b64-a334-968235adc415` |
| 34 | [`bus_stops`](https://data.gov.il/dataset/bus_stops) | תחנות תחבורה ציבורית | CSV · 1/1 DataStore | `e873e6a2-66c1-494f-a677-f5e77348edb0` |
| 35 | [`bus_terminal_fcl`](https://data.gov.il/dataset/bus_terminal_fcl) | מסופים ומתקני תשתית תח"צ | CSV/XLSX/ZIP · 2/4 DataStore | `15e4d0e2-f961-4083-adbd-f93dcb14dde7` |
| 36 | [`bus_terminal_strat`](https://data.gov.il/dataset/bus_terminal_strat) | תכנית אסטרטגית למסופים ומתקני תשתית | CSV/XLSX/ZIP · 2/4 DataStore | `dd629faf-aad2-4778-9111-45545cea6f44` |
| 37 | [`busterminal`](https://data.gov.il/dataset/busterminal) | מסופי אוטובוסים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `680dfd9f-42a0-45b1-a418-a1cd6cff7417` |
| 38 | [`cong_tax_rings`](https://data.gov.il/dataset/cong_tax_rings) | טבעות סל גודש | CSV/PDF/ZIP · 1/4 DataStore | `2e727979-7555-48f4-a5d8-3da29b392ffc` |
| 39 | [`construction_equipment`](https://data.gov.il/dataset/construction_equipment) | כלי צמ"ה (ציוד מכני הנדסי) | CSV · 1/1 DataStore | `58dc4654-16b1-42ed-8170-98fadec153ea` |
| 40 | [`cvfr`](https://data.gov.il/dataset/cvfr) | נתיבי טיסה | CSV/XLSX/ZIP · 2/4 DataStore | `3811ad6d-ee91-4d18-87b4-c2f672f03a6a` |
| 41 | [`degem-rechev-wltp`](https://data.gov.il/dataset/degem-rechev-wltp) | תוצרים ודגמים של כלי רכב פרטי ומסחרי | CSV · 2/2 DataStore | `142afde2-6228-49f9-8a29-9b6c3a0cbe40` |
| 42 | [`depo_lrt_metro`](https://data.gov.il/dataset/depo_lrt_metro) | דיפו רכבת קלה ומטרו | CSV/XLSX/ZIP · 1/4 DataStore | `1373a7ca-3ef8-48d4-9e11-24c80755bdd9` |
| 43 | [`discountpublictransportation`](https://data.gov.il/dataset/discountpublictransportation) | זכאות להנחה בתחבורה ציבורית | CSV/PDF · 1/2 DataStore | `8c344502-e294-436a-84e2-00a40b318d8b` |
| 44 | [`driving_license_ranks`](https://data.gov.il/dataset/driving_license_ranks) | דרגות והיתרי רישיון נהיגה | XLSX · 1/1 DataStore | `c680ada6-9af1-47ab-9acf-d6585df6ad47` |
| 45 | [`driving_shcool`](https://data.gov.il/dataset/driving_shcool) | בתי ספר לנהיגה | CSV · 1/1 DataStore | `3f06e2f2-e2ad-41ac-9665-37d0625537f2` |
| 46 | [`employment`](https://data.gov.il/dataset/employment) | מוקדי תעסוקה - נוהל שותפים לדרך | CSV/XLSX/ZIP · 2/4 DataStore | `24cfb983-b621-4f9c-a5f0-28c1da1218a5` |
| 47 | [`fast_lane_gate`](https://data.gov.il/dataset/fast_lane_gate) | נתיבים מהירים - שערים | CSV/XLSX/ZIP · 2/4 DataStore | `54707a2b-6e5c-41b5-8f5b-81c7d1c94f4d` |
| 48 | [`fast_lanes`](https://data.gov.il/dataset/fast_lanes) | נתיבים מהירים | CSV/XLSX/ZIP · 2/4 DataStore | `3d816e5a-3018-4d67-a1cc-2781fcdbe0a5` |
| 49 | [`functional_areas`](https://data.gov.il/dataset/functional_areas) | אזורי תפקוד מינהל התכנון | CSV/XLSX/ZIP · 2/4 DataStore | `1ad4ce45-aacd-47a1-8216-39c67544242d` |
| 50 | [`hagbalat_recall`](https://data.gov.il/dataset/hagbalat_recall) | כלי רכב שלא ביצעו ריקול (קריאת שירות) | CSV · 1/1 DataStore | `36bf1404-0be4-49d2-82dc-2f1ead4a8b93` |
| 51 | [`hatkana_nekudat_igun`](https://data.gov.il/dataset/hatkana_nekudat_igun) | כלי רכב המחויבים בהתקנת נקודות עיגון לאבטחת מטענים | CSV · 1/1 DataStore | `786b33b5-75c4-42a3-a241-b1af3c9ca487` |
| 52 | [`heavy-truck`](https://data.gov.il/dataset/heavy-truck) | כלי רכב מעל 3 וחצי טון וכלי רכב חסרי קוד דגם | CSV · 1/1 DataStore | `cd3acc5c-03c3-4c89-9c54-d40f93c0d790` |
| 53 | [`helipad`](https://data.gov.il/dataset/helipad) | מנחתי בתי חולים | CSV/XLSX/ZIP · 2/4 DataStore | `d848ff09-3b60-4db9-a932-740e3ec73389` |
| 54 | [`hov_2024`](https://data.gov.il/dataset/hov_2024) | HOV נתיבים רבי תפוסה | CSV/PDF/XLSX/ZIP · 1/6 DataStore | `432e48d2-efb2-48f5-8751-24febe51f93e` |
| 55 | [`hoze_zhut`](https://data.gov.il/dataset/hoze_zhut) | חוצה ישראל - זכות דרך | CSV/XLSX/ZIP · 2/4 DataStore | `fa247fb4-e9e9-4b12-860d-326b93e860c2` |
| 56 | [`ims_stat`](https://data.gov.il/dataset/ims_stat) | תחנות מטאורולוגיות - מגבלות בניה | CSV/KMZ/PDF/SHP · 1/4 DataStore | `d5b0c0f4-f2a1-49e7-af7d-0720a935399a` |
| 57 | [`industrial`](https://data.gov.il/dataset/industrial) | תחום אזורי תעשיה תעסוקה | CSV/KMZ/PDF/SHP · 1/4 DataStore | `71799e72-7a1f-45cf-9d81-5cd1d5f3b201` |
| 58 | [`interchange_areas`](https://data.gov.il/dataset/interchange_areas) | שטחים כלואים במחלפים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `85bfda85-7221-4e46-a7cd-5eb499a688d5` |
| 59 | [`kamut_sgirot_hodshi_rechev_blikoddegem`](https://data.gov.il/dataset/kamut_sgirot_hodshi_rechev_blikoddegem) | כמות כלי רכב חדשים (מסירות) חסרי קוד דגם העולים לכביש בחודש | CSV · 1/1 DataStore | `c967097c-3c74-4adf-a732-0fdd2fda56d9` |
| 60 | [`kav_ratzif_surveys`](https://data.gov.il/dataset/kav_ratzif_surveys) | נתוני סקרי פרויקט קו רציף (שילובים) | PDF/ZIP · 2 files | — |
| 61 | [`kishuriyut_metronit`](https://data.gov.il/dataset/kishuriyut_metronit) | קישוריות לתחנות מטרונית | CSV/XLSX/ZIP · 2/4 DataStore | `8548cdbc-97ec-4a2a-ac97-82872e971acd` |
| 62 | [`kishuriyut_nofit`](https://data.gov.il/dataset/kishuriyut_nofit) | קישוריות - רק"ל נופית | CSV/XLSX/ZIP · 2/4 DataStore | `9e2893d2-3eef-4240-abad-76255678d4ba` |
| 63 | [`kishuriyut_prj`](https://data.gov.il/dataset/kishuriyut_prj) | פרויקט קישוריות | CSV/XLSX/ZIP · 2/4 DataStore | `70ec3f9c-0e6f-4b0c-98b7-628728470a3c` |
| 64 | [`kli_rechev_ciburiim`](https://data.gov.il/dataset/kli_rechev_ciburiim) | מספרי רישוי של כלי הרכב הציבוריים הפעילים | CSV · 1/1 DataStore | `cf29862d-ca25-4691-84f6-1be60dcb4a1e` |
| 65 | [`levelseparation`](https://data.gov.il/dataset/levelseparation) | הפרדות מפלסיות רכבת ישראל | CSV/XLSX/ZIP · 2/4 DataStore | `58612e24-148a-443a-932a-e4d695396535` |
| 66 | [`licensing_bus_system`](https://data.gov.il/dataset/licensing_bus_system) | רישוי מערך האוטובוסים | CSV/PDF · 10/11 DataStore | `58593e9b-2d71-4c39-8663-b34ab29607ab` |
| 67 | [`light-mobility-parking-calculator`](https://data.gov.il/dataset/light-mobility-parking-calculator) | מחשבון חניות תחבורה קלה במוקדי תחבורה ציבורית | ZIP | — |
| 68 | [`lines-reliabilty`](https://data.gov.il/dataset/lines-reliabilty) | אמינות קווים | CSV/PDF · 1/2 DataStore | `6032ad57-3667-401e-9561-11f7e3b88581` |
| 69 | [`lrt_line`](https://data.gov.il/dataset/lrt_line) | קווי רכבת קלה | CSV/XLSX/ZIP · 1/4 DataStore | `ddd624b1-b244-4184-a94a-3629927cea0b` |
| 70 | [`lrt_stat`](https://data.gov.il/dataset/lrt_stat) | תחנות רכבת קלה | CSV/XLSX/ZIP · 1/4 DataStore | `b2ca8ac5-d7ea-41a5-8119-a30e98cf71e0` |
| 71 | [`mahirlair_city`](https://data.gov.il/dataset/mahirlair_city) | מהיר לעיר עירוני | CSV/XLSX/ZIP · 2/4 DataStore | `aefa18aa-e4fb-4356-b484-4706c7bd4f81` |
| 72 | [`mataan_ashkelon`](https://data.gov.il/dataset/mataan_ashkelon) | אסטרטגית למתע"ן בנפת אשקלון 2040 | CSV/XLSX/ZIP · 2/4 DataStore | `06980e45-e0a9-4f12-912c-ea4ae8392f30` |
| 73 | [`mataan_ashkelon_app`](https://data.gov.il/dataset/mataan_ashkelon_app) | בדיקת ישימות למתע"ן בנפת אשקלון 2050 | CSV/XLSX/ZIP · 2/4 DataStore | `d2c09ef5-2f8c-4c16-9be3-2a94d75e4d08` |
| 74 | [`mataan_brshva`](https://data.gov.il/dataset/mataan_brshva) | הסעת המונים מטרופולין באר שבע - 2050 | CSV/XLSX/ZIP · 2/4 DataStore | `cbceb2be-59fa-48bd-859c-cacbd18ad4a9` |
| 75 | [`mataan_haifa`](https://data.gov.il/dataset/mataan_haifa) | אסטרטגית למתע"ן מטרופולין חיפה 2040 | CSV/XLSX/ZIP · 2/4 DataStore | `b9c0d3b2-2660-4bb9-b253-76b15f1e3d7b` |
| 76 | [`mataan_hdr_ntn`](https://data.gov.il/dataset/mataan_hdr_ntn) | אסטרטגית למתע"ן חדרה נתניה 2050 | CSV/XLSX/ZIP · 2/4 DataStore | `03bcb366-0468-4cbe-8f89-eac1e7866356` |
| 77 | [`mataan_jlm`](https://data.gov.il/dataset/mataan_jlm) | הסעת המונים מטרופולין ירושלים - 2050 | CSV/XLSX/ZIP · 1/4 DataStore | `2a4ebc87-c35d-4ba0-a58f-383975a69ae2` |
| 78 | [`mataan_ntn_app`](https://data.gov.il/dataset/mataan_ntn_app) | בדיקת ישימות למתע"ן במרחב נתניה 2050 | CSV/XLSX/ZIP · 2/4 DataStore | `e380fd05-848c-43cc-a87d-af7bab4272a5` |
| 79 | [`mataan_tlv`](https://data.gov.il/dataset/mataan_tlv) | הסעת המונים מטרופולין ת"א - 2050 | CSV/XLSX/ZIP · 1/4 DataStore | `bd11e899-65c0-43aa-8264-c07434da22aa` |
| 80 | [`mehir_yevuan`](https://data.gov.il/dataset/mehir_yevuan) | יבואנים ומחירוני רכב חדש | CSV · 1/1 DataStore | `39f455bf-6db0-4926-859d-017f34eacbcb` |
| 81 | [`merhavironi`](https://data.gov.il/dataset/merhavironi) | מרחבים עירוניים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `8ff4b8e8-e412-42dd-b593-8072e303631d` |
| 82 | [`metro_line`](https://data.gov.il/dataset/metro_line) | קווי מטרו | CSV/XLSX/ZIP · 1/5 DataStore | `438c4cc5-a3aa-4db1-b203-525c52535259` |
| 83 | [`metro_stat`](https://data.gov.il/dataset/metro_stat) | תחנות מטרו | CSV/PDF/XLSX/ZIP · 1/5 DataStore | `aaea25c0-1478-4ae6-9c61-1cce3cff5ae7` |
| 84 | [`metrofan`](https://data.gov.il/dataset/metrofan) | מטרופן | CSV/PDF/ZIP · 1/4 DataStore | `6ac4334d-808a-4ee6-8ef8-6a2f129256ea` |
| 85 | [`metronit`](https://data.gov.il/dataset/metronit) | מטרונית | CSV/XLSX/ZIP · 2/4 DataStore | `94cf10b7-6f84-4563-b917-e42ab8e94472` |
| 86 | [`mile_post`](https://data.gov.il/dataset/mile_post) | אבני קילומטר | CSV/PDF/ZIP · 1/4 DataStore | `29511ef7-59ba-45bf-aed4-4be1f71ad834` |
| 87 | [`mimshakim_2023`](https://data.gov.il/dataset/mimshakim_2023) | ממשקים אגף תכנון 2023 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `376d2bcb-8815-4a64-a5c4-ed7be94b3816` |
| 88 | [`mimshakim_2030`](https://data.gov.il/dataset/mimshakim_2030) | ממשקים אגף תכנון 2030 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `883a9b18-9384-479e-8793-b8d3c3e1fa7f` |
| 89 | [`miutim_poi`](https://data.gov.il/dataset/miutim_poi) | מוקדי משיכה בישובי החברה הערבית | CSV/XLSX/ZIP · 2/4 DataStore | `16fe2c79-7c8c-4465-b043-c09179728d3b` |
| 90 | [`miutim_prj`](https://data.gov.il/dataset/miutim_prj) | פרויקטי תשתית בישובי החברה הערבית | CSV/XLSX/ZIP · 2/4 DataStore | `c6973571-70b3-4e07-abd7-f590a8bea275` |
| 91 | [`miutim_risk`](https://data.gov.il/dataset/miutim_risk) | מוקדי סיכון בישובי החברה הערבית | CSV/XLSX/ZIP · 2/4 DataStore | `f2aa6490-c051-4888-a245-f9730e4430cb` |
| 92 | [`motorcycle`](https://data.gov.il/dataset/motorcycle) | מספרי רישוי של כלי רכב דו גלגליים | CSV · 1/1 DataStore | `bf9df4e2-d90d-4c0a-a400-19e15af8e95f` |
| 93 | [`musachim`](https://data.gov.il/dataset/musachim) | מוסכים ומכוני רישוי | CSV · 1/1 DataStore | `bb68386a-a331-4bbc-b668-bba2766d517d` |
| 94 | [`n2r`](https://data.gov.il/dataset/n2r) | הודעות למשיטים | ? | — |
| 95 | [`nataz_completion`](https://data.gov.il/dataset/nataz_completion) | השלמת נתיבי העדפה | CSV/KMZ/PDF/SHP · 1/4 DataStore | `88b82600-c43a-4b31-a20c-0ff7d63a7c6d` |
| 96 | [`nataz_kayam`](https://data.gov.il/dataset/nataz_kayam) | נתיבי העדפה קיימים | CSV/XLSX/ZIP · 2/4 DataStore | `a853e465-b435-445c-b38b-26fadd795df5` |
| 97 | [`nataz_planned`](https://data.gov.il/dataset/nataz_planned) | נתיבי העדפה מתוכננים | CSV/XLSX/ZIP · 2/4 DataStore | `a3952398-2aed-4d0e-bcd8-253d32fe9975` |
| 98 | [`nataz_strategic`](https://data.gov.il/dataset/nataz_strategic) | נתיבי העדפה עתידיים | CSV/PDF/ZIP · 1/4 DataStore | `42b50aba-414b-41f2-be8b-9609780cba54` |
| 99 | [`nti_taba`](https://data.gov.il/dataset/nti_taba) | תכניות בניין עיר של נתיבי ישראל | CSV/KMZ/PDF/SHP · 1/4 DataStore | `93323f17-0856-499f-b04b-c4590b61454c` |
| 100 | [`nti_zhut_dereh`](https://data.gov.il/dataset/nti_zhut_dereh) | נתיבי ישראל - זכות דרך | CSV/XLSX/ZIP · 2/4 DataStore | `25a1c308-353a-4fda-800b-4ae13e82d61a` |
| 101 | [`obbusta2013`](https://data.gov.il/dataset/obbusta2013) | סקר נוסעים באוטובוסים במטרופולין תל אביב 2013 | PDF/ZIP · 2 files | — |
| 102 | [`obrailta_2013`](https://data.gov.il/dataset/obrailta_2013) | סקר נוסעים בתחנות רכבת במטרופולין תל אביב 2013 | PDF/ZIP · 1/2 DataStore | `9410afcf-73fe-437d-8f98-fc3fc46c5d3e` |
| 103 | [`ofneidan`](https://data.gov.il/dataset/ofneidan) | אופנידן | CSV/XLSX/ZIP · 2/4 DataStore | `94c34998-b8fe-414b-94d8-23e92299ed4a` |
| 104 | [`onboard_bsh_2019`](https://data.gov.il/dataset/onboard_bsh_2019) | סקר נוסעים באוטובוסים במטרופולין באר-שבע 2019 | PDF/ZIP · 2 files | — |
| 105 | [`onboardbusta2022peima1`](https://data.gov.il/dataset/onboardbusta2022peima1) | סקר נוסעים באוטובוסים במטרופולין תל אביב 2020-2022– פעימה ראשונה | ?/ZIP · 2 files | — |
| 106 | [`opercraft_tq`](https://data.gov.il/dataset/opercraft_tq) | שאלות ותשובות למבחן עיוני למשטים | PDF/XLS · 1/3 DataStore | `d99b5fcb-b906-461e-a386-dcaffa13f9ac` |
| 107 | [`park_n_ride`](https://data.gov.il/dataset/park_n_ride) | חניוני חנה וסע | CSV/XLSX/ZIP · 1/4 DataStore | `e1666064-8b58-41ec-b770-c909a5075134` |
| 108 | [`personal_import_vehicles`](https://data.gov.il/dataset/personal_import_vehicles) | כלי רכב ביבוא אישי | CSV · 1/1 DataStore | `03adc637-b6fe-402b-9937-7c3d3afc9140` |
| 109 | [`principal-investigator-posts`](https://data.gov.il/dataset/principal-investigator-posts) | הודעות החוקר הראשי | ? | — |
| 110 | [`private-and-commercial-vehicles`](https://data.gov.il/dataset/private-and-commercial-vehicles) | מספרי רישוי של כלי רכב פרטיים ומסחריים | CSV · 2/2 DataStore | `053cea08-09bc-40ec-8f7a-156f0677aff3` |
| 111 | [`rail_flow_2040`](https://data.gov.il/dataset/rail_flow_2040) | רכבת כבדה - מספר נוסעים בשנת 2040 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `87cf8b7a-94d8-481c-bc56-ed40a40fd01e` |
| 112 | [`rail_freq_2018`](https://data.gov.il/dataset/rail_freq_2018) | רכבת כבדה - תדירות שעתית 2018 | CSV/ZIP · 1/3 DataStore | `3691808b-1c2e-4e7f-96c4-1d268cc5ad79` |
| 113 | [`rail_freq_2019`](https://data.gov.il/dataset/rail_freq_2019) | רכבת כבדה - תדירות שעתית 2019 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `301af368-558f-462d-a287-03354823adf8` |
| 114 | [`rail_freq_2020`](https://data.gov.il/dataset/rail_freq_2020) | רכבת כבדה - תדירות שעתית 2020 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `740e3550-f15d-4198-a75a-55f50e06f26b` |
| 115 | [`rail_freq_2023`](https://data.gov.il/dataset/rail_freq_2023) | רכבת כבדה - תדירות שעתית 2023 | CSV/KMZ/PDF/SHP · 1/4 DataStore | `24a68c2d-2f6f-4cac-9662-6cd07b3b21c3` |
| 116 | [`rail_freq_2040`](https://data.gov.il/dataset/rail_freq_2040) | רכבת כבדה - תדירות שעתית 2040 | CSV/PDF/ZIP · 1/4 DataStore | `9b389932-b81b-4cfc-9449-aa9dd267454b` |
| 117 | [`rail_stat`](https://data.gov.il/dataset/rail_stat) | רכבת כבדה - תחנות נוסעים | CSV/XLSX/ZIP · 2/4 DataStore | `b6685ecf-2f87-4602-823e-af9790fd6aba` |
| 118 | [`rail_stat_onoff_month`](https://data.gov.il/dataset/rail_stat_onoff_month) | רכבת כבדה - ספירת נוסעים בתחנות | CSV/KMZ/PDF/SHP · 1/4 DataStore | `0f772fd8-0010-46be-9f40-28a6229fe682` |
| 119 | [`rail_strat_station`](https://data.gov.il/dataset/rail_strat_station) | רכבת כבדה - תכנית אסטרטגית - תחנות | CSV/KMZ/PDF/SHP · 1/4 DataStore | `f527e357-4847-4565-9dc4-b55f21d6c3b6` |
| 120 | [`rail_strategic`](https://data.gov.il/dataset/rail_strategic) | רכבת כבדה - תכנית אסטרטגית - מסילות | CSV/KMZ/PDF/SHP · 1/4 DataStore | `786456ec-3e97-42d7-839b-a2df1020034f` |
| 121 | [`recall`](https://data.gov.il/dataset/recall) | הודעות יצרני הרכב RECALL | CSV · 1/1 DataStore | `2c33523f-87aa-44ec-a736-edbb0a82975e` |
| 122 | [`rechavim_hashmalim`](https://data.gov.il/dataset/rechavim_hashmalim) | כמות כלי רכב חשמליים לפי נפה | CSV · 1/1 DataStore | `07421a4e-5b12-4444-9173-5ca297b31f79` |
| 123 | [`rechev-tag-nachim`](https://data.gov.il/dataset/rechev-tag-nachim) | כלי רכב עם תג חניה לנכה | CSV · 1/1 DataStore | `c8b9f9c8-4612-4068-934f-d4acd2e3c06e` |
| 124 | [`rechev_le_pail_with_degem`](https://data.gov.il/dataset/rechev_le_pail_with_degem) | מספרי רישוי של כלי רכב לא פעילים עם קוד דגם | CSV · 1/1 DataStore | `f6efe89a-fb3d-43a4-bb61-9bf12a9b9099` |
| 125 | [`rechev_le_pail_without-degem`](https://data.gov.il/dataset/rechev_le_pail_without-degem) | מספרי רישוי של כלי רכב לא פעילים וחסרי קוד דגם | CSV · 1/1 DataStore | `6f6acd03-f351-4a8f-8ecf-df792f4f573a` |
| 126 | [`reshev_bitul_sofi`](https://data.gov.il/dataset/reshev_bitul_sofi) | כלי רכב שירדו מהכביש ובסטטוס ביטול סופי | CSV · 3/3 DataStore | `851ecab1-0622-4dbe-a6c7-f950cf82abf9` |
| 127 | [`ridership`](https://data.gov.il/dataset/ridership) | נסועה בקווי אוטובוס | CSV/PDF · 5/6 DataStore | `7b126b6d-3411-4438-89c3-8eceea61c2db` |
| 128 | [`road_strat_2030`](https://data.gov.il/dataset/road_strat_2030) | אסטרטגית לדרכים 2030 | CSV/XLSX/ZIP · 2/4 DataStore | `f6f88fa4-877a-41f1-b27a-52559672ab72` |
| 129 | [`road_strat_2050`](https://data.gov.il/dataset/road_strat_2050) | אסטרטגית לדרכים 2050 | CSV/XLSX/ZIP · 2/4 DataStore | `ebe1e138-6288-40ee-8afc-b41c09018c56` |
| 130 | [`roadauthority`](https://data.gov.il/dataset/roadauthority) | רשות תמרור בכבישים | CSV/XLSX/ZIP · 2/4 DataStore | `a3cd6318-68fc-4e18-bd30-395acba5f001` |
| 131 | [`roadnumber_tma`](https://data.gov.il/dataset/roadnumber_tma) | מספור דרכים בתמ"א | CSV/XLSX/ZIP · 2/4 DataStore | `5a4d20d7-b16c-4d77-83aa-f6648ec14982` |
| 132 | [`roadnumbers`](https://data.gov.il/dataset/roadnumbers) | מספרי דרכים ארציות | CSV/XLSX/ZIP · 2/4 DataStore | `0476bc99-21c2-4e26-b353-94a7782ea90b` |
| 133 | [`roundabout`](https://data.gov.il/dataset/roundabout) | מעגלי תנועה | CSV/XLSX/ZIP · 2/4 DataStore | `81697c44-0bce-4eeb-80b0-994616a47c83` |
| 134 | [`sfirot`](https://data.gov.il/dataset/sfirot) | ספירות תנועה | CSV/XLSX/ZIP · 2/4 DataStore | `cb930bf3-388f-48da-b501-a69038ea959a` |
| 135 | [`shamaim_rechev`](https://data.gov.il/dataset/shamaim_rechev) | שמאי רכב | CSV · 1/1 DataStore | `4a434d65-3ca2-45e5-8026-5d9819c3f95c` |
| 136 | [`shinui_mivne`](https://data.gov.il/dataset/shinui_mivne) | היסטוריית כלי רכב פרטיים | CSV · 2/2 DataStore | `56063a99-8a3e-4ff4-912e-5966c0279bad` |
| 137 | [`socharim`](https://data.gov.il/dataset/socharim) | סוחרי רכב | CSV · 1/1 DataStore | `eb74ad8c-ffcd-43bb-949c-2244fc8a8651` |
| 138 | [`speed_survey_2022`](https://data.gov.il/dataset/speed_survey_2022) | סקר ארצי של מהירויות נסיעה בישראל 2022 | CSV/PDF/XLSX/ZIP · 1/7 DataStore | `3e7c5be6-aab9-4d45-abbb-acc7e1904838` |
| 139 | [`strat_border`](https://data.gov.il/dataset/strat_border) | גבולות תכניות אסטרטגיות | CSV/XLSX/ZIP · 1/4 DataStore | `e9c9b934-ae9b-49c5-9bd6-527b8fbc39a5` |
| 140 | [`tahaz_clusters`](https://data.gov.il/dataset/tahaz_clusters) | אשכולות תח"צ | CSV/PDF/ZIP · 1/4 DataStore | `7b6171ba-bbe7-471f-8a03-ec49ac8ad7a4` |
| 141 | [`tavlat-simlei-averot`](https://data.gov.il/dataset/tavlat-simlei-averot) | טבלת סמלי עבירות | XLSX · 1/1 DataStore | `a2dd714b-e012-46e4-a996-6307f8b46fc5` |
| 142 | [`taz_jer_pop_type`](https://data.gov.il/dataset/taz_jer_pop_type) | סוג אוכלוסיה בירושלים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `a44710d4-60ea-43e3-80e3-3be4a7f83646` |
| 143 | [`taz_mot_rate_2040`](https://data.gov.il/dataset/taz_mot_rate_2040) | רמת מינוע לשנת 2040 | CSV/PDF/ZIP · 1/4 DataStore | `1f935a0b-fa66-42c3-9415-5ec0afeb6506` |
| 144 | [`taz_north_popdens_2016`](https://data.gov.il/dataset/taz_north_popdens_2016) | צפיפות אוכלוסיה לקילומטר רבוע בצפון הארץ | CSV/KMZ/PDF/SHP · 1/4 DataStore | `8f64389b-cbb9-4279-abd7-27991ea47901` |
| 145 | [`taz_ta_popdens_2017`](https://data.gov.il/dataset/taz_ta_popdens_2017) | צפיפות אוכלוסיה במטרופולין תל אביב | CSV/PDF/ZIP · 1/4 DataStore | `98d177d7-d34d-4f8b-a9b6-358199869ba1` |
| 146 | [`tikufim-2021`](https://data.gov.il/dataset/tikufim-2021) | תיקופי מסלקה בתחבורה ציבורית | CSV/PDF · 8/9 DataStore | `ef42a264-9da2-41ad-9120-822064fb5433` |
| 147 | [`tikufim_station_2022`](https://data.gov.il/dataset/tikufim_station_2022) | תיקופי מסלקה לתחנה | CSV · 7/7 DataStore | `3ad014c3-e0a6-4ba0-9b2b-12a29d273512` |
| 148 | [`tma_23`](https://data.gov.il/dataset/tma_23) | תמא 23 - קומפילציית מסילות ברזל | CSV/PDF/ZIP · 1/4 DataStore | `1d421a2a-c7cd-4216-830c-c56419378d0e` |
| 149 | [`tma_23a4_dipo`](https://data.gov.il/dataset/tma_23a4_dipo) | תמ"א 23-א-4 - דיפו | CSV/PDF/ZIP · 1/4 DataStore | `f4ed636a-79db-49a9-a322-dbcacf0a5652` |
| 150 | [`tma_23a4_lines`](https://data.gov.il/dataset/tma_23a4_lines) | תמ"א 23_א_4 - קווי מתע"ן | CSV/PDF/ZIP · 1/4 DataStore | `556cb2f9-5b71-4041-a460-922bf05b91b1` |
| 151 | [`tma_3`](https://data.gov.il/dataset/tma_3) | תמא 3 - קומפילציית דרכים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `643dc6f9-1f78-4a57-9e84-c4ba8809c044` |
| 152 | [`tma_3_plans`](https://data.gov.il/dataset/tma_3_plans) | תמא 31_א - תכניות מפורטות לדרכים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `fc05dee5-d30a-4915-bfba-b828f91b7f63` |
| 153 | [`tma_3_points`](https://data.gov.il/dataset/tma_3_points) | תמ"א 3 - מחלפים | CSV/KMZ/PDF/SHP · 1/4 DataStore | `cc777f34-02cd-4ff8-b28a-944fd072117c` |
| 154 | [`tma_42`](https://data.gov.il/dataset/tma_42) | תמ"א 42 | CSV/KMZ/PDF/SHP · 9/36 DataStore | `546fa19a-e575-4473-ab24-1f07e708598c` |
| 155 | [`tourism1617`](https://data.gov.il/dataset/tourism1617) | סקר הרגלי נסיעה של תיירים 2016-2017 | ZIP | — |
| 156 | [`tozeret`](https://data.gov.il/dataset/tozeret) | תוצרים של כלי הרכב הפעילים | CSV · 1/1 DataStore | `d00812f4-58c5-4ce8-b16c-ac13ae52f9d8` |
| 157 | [`tq_he_a3`](https://data.gov.il/dataset/tq_he_a3) | מאגר השאלות והתשובות למבחן עיוני ייעודי לרוכבי אופניים חשמליים A3 | XLSX/XML · 1/2 DataStore | `14da4d4b-74f7-4fb1-a2f9-e8cc8696a3c0` |
| 158 | [`tqar`](https://data.gov.il/dataset/tqar) | بنك أسئلة امتحان السياقة النظري | XLSX/XML · 1/2 DataStore | `fe998a65-83a3-45e5-b4b7-3e0ce86ae072` |
| 159 | [`tqar_a3`](https://data.gov.il/dataset/tqar_a3) | بنك الأسئلة والأجوبة الرسمي للاختبار النظري المخصص لراكبي الدراجات الكهربائية (A3) | XLSX · 1/1 DataStore | `5364b173-851a-4722-9c1f-563bbd919f48` |
| 160 | [`tqen`](https://data.gov.il/dataset/tqen) | The complete pool of questions and answers for the computerized driving theory test | XLSX/XML · 1/2 DataStore | `9a197011-adf9-45a2-81b9-d17dabdf990b` |
| 161 | [`tqes`](https://data.gov.il/dataset/tqes) | Banco de preguntas del examen teórico a tomarse en el Ministerio de Transporte para y renovar licencias de conducción | XLSX/XML · 1/2 DataStore | `e8da3b53-cdd0-4ef9-ae19-ff78c773e882` |
| 162 | [`tqfr`](https://data.gov.il/dataset/tqfr) | Questions et réponses de l'examen de conduite théorique informatisé | XLSX/XML · 1/2 DataStore | `a106ea08-ff97-4971-8720-c85bdd3d2264` |
| 163 | [`tqhe`](https://data.gov.il/dataset/tqhe) | מאגר השאלות והתשובות הרשמי למבחן נהיגה עיוני ממוחשב | XLSX/XML · 2/2 DataStore | `8c0f314f-583d-48b6-9f5f-4483d95f6848` |
| 164 | [`tqru`](https://data.gov.il/dataset/tqru) | Вопросы и ответы квалификационного экзамена на знание Правил Дорожного Движения | XLSX/XML · 1/2 DataStore | `ca264280-1669-45ce-a96f-a4c9ed71e812` |
| 165 | [`traffic_authority`](https://data.gov.il/dataset/traffic_authority) | רשימת רשויות תמרור מקומיות | CSV · 1/1 DataStore | `8db59260-64fd-4f15-a264-3c47c1bc76df` |
| 166 | [`traffic_light_junction`](https://data.gov.il/dataset/traffic_light_junction) | צמתים מרומזרים | CSV/XLSX/ZIP · 2/4 DataStore | `77c61c20-8bcb-45d9-98b3-5623375e5b33` |
| 167 | [`train_safety`](https://data.gov.il/dataset/train_safety) | בטיחות ברכבת | CSV/PDF · 1/2 DataStore | `5e57b0f2-60ce-4c69-9312-9aba3a56a52a` |
| 168 | [`train_station`](https://data.gov.il/dataset/train_station) | רכבת לו"ז | CSV · 1/1 DataStore | `1ebbbb91-1d44-4f41-a85c-4a93a35e32d6` |
| 169 | [`train_trip`](https://data.gov.il/dataset/train_trip) | רכבת תכנון מול ביצוע | CSV/PDF · 1/2 DataStore | `6cf35ec2-c0eb-4ef0-a904-f093dab0abfd` |
| 170 | [`tripscelular_1819`](https://data.gov.il/dataset/tripscelular_1819) | מידע על תנועות ארציות של נוסעים לפי נתוני טלפונים סלולריים 2018-19 | PDF/ZIP · 2 files | — |
| 171 | [`truck_survey_2017`](https://data.gov.il/dataset/truck_survey_2017) | סקר משאיות ארצי 2017 | PDF/ZIP · 2 files | — |
| 172 | [`ttl_transport`](https://data.gov.il/dataset/ttl_transport) | תכניות תשתית לאומית - תחבורה | CSV/XLSX/ZIP · 2/4 DataStore | `1f2d023b-da8e-4afd-b478-5f01f5865f77` |
| 173 | [`tunnels`](https://data.gov.il/dataset/tunnels) | מנהרות | CSV/XLSX/ZIP · 2/4 DataStore | `a3907f72-ebec-4ca9-8b7f-6a0a524f84c1` |
| 174 | [`vehicle_counts`](https://data.gov.il/dataset/vehicle_counts) | נתוני ספירות תנועה מזדמנות (אד-הוק) | PDF/ZIP · 1/8 DataStore | `e32d4418-f2fc-42dc-8abb-9ef352c2b756` |
| 175 | [`vehicles_filters_reduce_emissions`](https://data.gov.il/dataset/vehicles_filters_reduce_emissions) | כלי רכב שמותקנים בהם מסננים לצמצום פליטת מזהמים | CSV · 1/1 DataStore | `7cb2bd95-bf2e-49b6-aea1-fcb5ff6f0473` |
| 176 | [`vor`](https://data.gov.il/dataset/vor) | מתקני עזר לניווט | CSV/PDF/XLSX/ZIP · 2/5 DataStore | `80f36b6a-68ce-43d9-9773-e88085cac0cc` |
| 177 | [`workplan`](https://data.gov.il/dataset/workplan) | פרויקטי תשתית תחבורה | CSV/PDF/XLSX/ZIP · 5/20 DataStore | `c7921041-21de-4027-83a0-d14135bbe81f` |
| 178 | [`wplan_muni`](https://data.gov.il/dataset/wplan_muni) | שותפים לדרך - השתתפות במימון פרויקטי תחבורה ברשויות מקומיות | CSV/XLSX/ZIP · 2/4 DataStore | `b3192505-5175-4a5a-abfb-d1beb2febeaa` |
| 179 | [`zakaut-hatkana`](https://data.gov.il/dataset/zakaut-hatkana) | מערכת בטיחות ברכב | CSV · 1/1 DataStore | `83bfb278-7be1-4dab-ae2d-40125a923da1` |
| 180 | [`zmt_names`](https://data.gov.il/dataset/zmt_names) | שמות צמתים ומחלפים | CSV/XLSX/ZIP · 2/4 DataStore | `09bbc3b7-7289-4beb-97c7-a10ebc4973c6` |

### Survey of Israel (Mapping Center)
<a id="israel_mapping_center"></a>
**Slug:** `israel_mapping_center` · **Hebrew:** המרכז למיפוי ישראל · **Category:** Geospatial · **Datasets:** 116

- Org page: https://data.gov.il/organization/israel_mapping_center
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:israel_mapping_center&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`1997`](https://data.gov.il/dataset/1997) | ספר השמות הגיאוגרפיים בישראל משנת 1997 | ZIP | — |
| 2 | [`826`](https://data.gov.il/dataset/826) | מטה דאטה על שכבות | XLS | — |
| 3 | [`827`](https://data.gov.il/dataset/827) | לוח מרחקי הדרך הרשמי עפ"י תכם | XLS · 1/1 DataStore | `d9e0d816-6fb5-49a6-8b8c-9a7e76eef06b` |
| 4 | [`830`](https://data.gov.il/dataset/830) | תחנות GPS | XML | — |
| 5 | [`831`](https://data.gov.il/dataset/831) | מפתח מפות 25,000 | ?/XML · 2 files | — |
| 6 | [`832`](https://data.gov.il/dataset/832) | מפתח מפות 50,000 | ?/XML · 2 files | — |
| 7 | [`833`](https://data.gov.il/dataset/833) | מפתח מפות 100,000 | GEOJSON/XML · 2 files | — |
| 8 | [`926`](https://data.gov.il/dataset/926) | שדות תעופה אזרחיים | XML | — |
| 9 | [`928`](https://data.gov.il/dataset/928) | שכבת נמלי פריקה והטענה | XML | — |
| 10 | [`930`](https://data.gov.il/dataset/930) | שכבת נמלים ימיים | XML · 2 files | — |
| 11 | [`931`](https://data.gov.il/dataset/931) | שכבת דרכים | XML | — |
| 12 | [`932`](https://data.gov.il/dataset/932) | שכבת מסילות ברזל | XML | — |
| 13 | [`933`](https://data.gov.il/dataset/933) | שכבת נחלים | XML | — |
| 14 | [`academic`](https://data.gov.il/dataset/academic) | מוסדות אקדמאיים | CSV · 1/1 DataStore | `b2970446-98e0-483a-86c1-7ec00170b386` |
| 15 | [`afq`](https://data.gov.il/dataset/afq) | תצלום אויר 2015 2 מטר - גליון אפיקים | ZIP | — |
| 16 | [`arb`](https://data.gov.il/dataset/arb) | תצלום אויר 2015 2 מטר - גליון ארבל | ZIP | — |
| 17 | [`ard`](https://data.gov.il/dataset/ard) | תצלום אויר 2015 2 מטר - גליון ערד | ZIP | — |
| 18 | [`arl`](https://data.gov.il/dataset/arl) | תצלום אויר 2015 2 מטר - גליון אריאל | ZIP | — |
| 19 | [`asd`](https://data.gov.il/dataset/asd) | תצלום אויר 2015 2 מטר - גליון אשדוד | ZIP | — |
| 20 | [`asq`](https://data.gov.il/dataset/asq) | תצלום אויר 2015 2 מטר - גליון אשקלון | ZIP | — |
| 21 | [`atl`](https://data.gov.il/dataset/atl) | תצלום אויר 2015 2 מטר - גליון עתלית | ZIP | — |
| 22 | [`bgv`](https://data.gov.il/dataset/bgv) | תצלום אויר 2015 2 מטר - גליון בית גוברין | ZIP | — |
| 23 | [`bod`](https://data.gov.il/dataset/bod) | תצלום אויר 2015 2 מטר - גליון בארות עודד | ZIP | — |
| 24 | [`bor`](https://data.gov.il/dataset/bor) | תצלום אויר 2015 2 מטר - גליון באר אורה | ZIP | — |
| 25 | [`bord-tazar`](https://data.gov.il/dataset/bord-tazar) | גבולות תצ"ר | ZIP · 1/2 DataStore | `4cfdb058-4943-4377-8199-ed6c26f4ad84` |
| 26 | [`bqt`](https://data.gov.il/dataset/bqt) | תצלום אויר 2015 2 מטר - גליון בקעות | ZIP | — |
| 27 | [`bsh`](https://data.gov.il/dataset/bsh) | תצלום אויר 2015 2 מטר - גליון בית שאן | ZIP | — |
| 28 | [`bsm`](https://data.gov.il/dataset/bsm) | תצלום אויר 2015 2 מטר - גליון בית שמש | ZIP | — |
| 29 | [`bsv`](https://data.gov.il/dataset/bsv) | תצלום אויר 2015 2 מטר - גליון באר שבע | ZIP | — |
| 30 | [`distance`](https://data.gov.il/dataset/distance) | מרחקים בין ישובים וצמתים | ZIP · 3/4 DataStore | `bc5293d3-1023-4d9e-bdbe-082b58f93b65` |
| 31 | [`dmn`](https://data.gov.il/dataset/dmn) | תצלום אויר 2015 2 מטר - גליון דימונה | ZIP | — |
| 32 | [`e-data-gov-il`](https://data.gov.il/dataset/e-data-gov-il) | שכבת גושי שומה | ZIP | — |
| 33 | [`e-new-data-gov-il`](https://data.gov.il/dataset/e-new-data-gov-il) | שכבת חלקות שומה | ZIP | — |
| 34 | [`egd`](https://data.gov.il/dataset/egd) | תצלום אויר 2015 2 מטר - גליון עין גדי | ZIP | — |
| 35 | [`elt`](https://data.gov.il/dataset/elt) | תצלום אויר 2015 2 מטר - גליון אילת | ZIP | — |
| 36 | [`est`](https://data.gov.il/dataset/est) | תצלום אויר 2015 2 מטר - גליון אשתמוע | ZIP | — |
| 37 | [`eyv`](https://data.gov.il/dataset/eyv) | תצלום אויר 2015 2 מטר - גליון עין יהב | ZIP | — |
| 38 | [`ezv`](https://data.gov.il/dataset/ezv) | תצלום אויר 2015 2 מטר - גליון עין זיון | ZIP | — |
| 39 | [`fieldschools`](https://data.gov.il/dataset/fieldschools) | בתי-ספר שדה | CSV · 1/1 DataStore | `016c3f10-fd7d-4f34-a08a-178f93472f00` |
| 40 | [`frn`](https://data.gov.il/dataset/frn) | תצלום אויר 2015 2 מטר - גליון פארן | ZIP | — |
| 41 | [`gdr`](https://data.gov.il/dataset/gdr) | תצלום אויר 2015 2 מטר - גליון גדרה | ZIP | — |
| 42 | [`hag`](https://data.gov.il/dataset/hag) | תצלום אויר 2015 2 מטר - גליון חולות עגור | ZIP | — |
| 43 | [`hdr`](https://data.gov.il/dataset/hdr) | תצלום אויר 2015 2 מטר - גליון חדרה | ZIP | — |
| 44 | [`hef`](https://data.gov.il/dataset/hef) | תצלום אויר 2015 2 מטר - גליון חיפה | ZIP | — |
| 45 | [`highwayparkinglots`](https://data.gov.il/dataset/highwayparkinglots) | חניוני דרכים | CSV · 1/1 DataStore | `29a0b37e-65d6-4860-9d01-2d8bcc60682a` |
| 46 | [`hkr`](https://data.gov.il/dataset/hkr) | תצלום אויר 2015 2 מטר - גליון הר כרכם | ZIP | — |
| 47 | [`hlz`](https://data.gov.il/dataset/hlz) | תצלום אויר 2015 2 מטר - גליון הר לוץ | ZIP | — |
| 48 | [`hmr`](https://data.gov.il/dataset/hmr) | תצלום אויר 2015 2 מטר - גליון הר חמרן | ZIP | — |
| 49 | [`hrd`](https://data.gov.il/dataset/hrd) | תצלום אויר 2015 2 מטר - גליון הר ארדון | ZIP | — |
| 50 | [`hsg`](https://data.gov.il/dataset/hsg) | תצלום אויר 2015 2 מטר - גליון הר שגיא | ZIP | — |
| 51 | [`hsv`](https://data.gov.il/dataset/hsv) | תצלום אויר 2015 2 מטר - גליון הר שגוב | ZIP | — |
| 52 | [`hvr`](https://data.gov.il/dataset/hvr) | תצלום אויר 2015 2 מטר - גליון חברון | ZIP | — |
| 53 | [`hzf`](https://data.gov.il/dataset/hzf) | תצלום אויר 2015 2 מטר - גליון הר צניפים | ZIP | — |
| 54 | [`hzr`](https://data.gov.il/dataset/hzr) | תצלום אויר 2015 2 מטר - גליון | ZIP | — |
| 55 | [`kadaster`](https://data.gov.il/dataset/kadaster) | הודעת עדכון קדסטר לרשויות | ZIP · 1/1 DataStore | `cd43d8af-1e20-43e9-92aa-efc89c5f44a0` |
| 56 | [`kavi-hof`](https://data.gov.il/dataset/kavi-hof) | קווי שמירת הסביבה החופית | ZIP | — |
| 57 | [`kindergarten`](https://data.gov.il/dataset/kindergarten) | גני ילדים | CSV · 1/1 DataStore | `75d2d6a7-edc9-4615-8e06-fc0940e384ce` |
| 58 | [`ksb`](https://data.gov.il/dataset/ksb) | תצלום אויר 2015 2 מטר - גליון כפר סבא | ZIP | — |
| 59 | [`lod`](https://data.gov.il/dataset/lod) | תצלום אויר 2015 2 מטר - גליון לוד | ZIP | — |
| 60 | [`mef`](https://data.gov.il/dataset/mef) | תצלום אויר 2015 2 מטר - גליון מעלה אפרים | ZIP | — |
| 61 | [`mgl`](https://data.gov.il/dataset/mgl) | תצלום אויר 2015 2 מטר - גליון מרום גולן | ZIP | — |
| 62 | [`mkt`](https://data.gov.il/dataset/mkt) | תצלום אויר 2015 2 מטר - גליון המכתש הקטן | ZIP | — |
| 63 | [`mng`](https://data.gov.il/dataset/mng) | תצלום אויר 2015 2 מטר - גליון משמר הנגב | ZIP | — |
| 64 | [`modedim`](https://data.gov.il/dataset/modedim) | רשימת המודדים | CSV · 1/1 DataStore | `096e5fba-420c-4822-8172-78be54767cef` |
| 65 | [`msh`](https://data.gov.il/dataset/msh) | תצלום אויר 2015 2 מטר - גליון מצפה שלם | ZIP | — |
| 66 | [`msr`](https://data.gov.il/dataset/msr) | תצלום אויר 2015 2 מטר - גליון מצפה סיירים | ZIP | — |
| 67 | [`mtl`](https://data.gov.il/dataset/mtl) | תצלום אויר 2015 2 מטר - גליון מטולה | ZIP | — |
| 68 | [`mzr`](https://data.gov.il/dataset/mzr) | תצלום אויר 2015 2 מטר - גליון מצפה רמון | ZIP | — |
| 69 | [`nationalcanopytrees`](https://data.gov.il/dataset/nationalcanopytrees) | מיפוי חופות עצים - מאגר גיאוגרפי לאומי | ZIP | — |
| 70 | [`nhr`](https://data.gov.il/dataset/nhr) | תצלום אויר 2015 2 מטר - גליון נהריה | ZIP | — |
| 71 | [`nkr`](https://data.gov.il/dataset/nkr) | תצלום אויר 2015 2 מטר - גליון נאות הכיכר | ZIP | — |
| 72 | [`nrm`](https://data.gov.il/dataset/nrm) | תצלום אויר 2015 2 מטר - גליון נירים | ZIP | — |
| 73 | [`ntn`](https://data.gov.il/dataset/ntn) | תצלום אויר 2015 2 מטר - גליון נתניה | ZIP | — |
| 74 | [`ntv`](https://data.gov.il/dataset/ntv) | תצלום אויר 2015 2 מטר - גליון נתיבות | ZIP | — |
| 75 | [`nvz`](https://data.gov.il/dataset/nvz) | תצלום אויר 2015 2 מטר - גליון נוה זוהר | ZIP | — |
| 76 | [`nyz`](https://data.gov.il/dataset/nyz) | תצלום אויר 2015 2 מטר - גליון ניר יצחק | ZIP | — |
| 77 | [`nzl`](https://data.gov.il/dataset/nzl) | תצלום אויר 2015 2 מטר - גליון נצרת עלית | ZIP | — |
| 78 | [`nzn`](https://data.gov.il/dataset/nzn) | תצלום אויר 2015 2 מטר - גליון נצנה | ZIP | — |
| 79 | [`nzr`](https://data.gov.il/dataset/nzr) | תצלום אויר 2015 2 מטר - גליון נצרת | ZIP | — |
| 80 | [`orn`](https://data.gov.il/dataset/orn) | תצלום אויר 2015 2 מטר - גליון אורון | ZIP | — |
| 81 | [`parkinglots`](https://data.gov.il/dataset/parkinglots) | מגרשי חניה | CSV · 1/1 DataStore | `34729a10-299b-448d-a223-5d7533e8f147` |
| 82 | [`presentation-of-sea-level-rise-scenarios`](https://data.gov.il/dataset/presentation-of-sea-level-rise-scenarios) | Presentation of sea level rise scenarios | ZIP · 2 files | — |
| 83 | [`qgt`](https://data.gov.il/dataset/qgt) | תצלום אויר 2015 2 מטר - גליון קרית גת | ZIP | — |
| 84 | [`qly`](https://data.gov.il/dataset/qly) | תצלום אויר 2015 2 מטר - גליון קליה | ZIP | — |
| 85 | [`researchinstitute`](https://data.gov.il/dataset/researchinstitute) | מכוני מחקר | CSV · 1/1 DataStore | `2b1e7c72-4709-4971-83f4-dd549e0c20ca` |
| 86 | [`rivers`](https://data.gov.il/dataset/rivers) | נחלים shape | ZIP | — |
| 87 | [`rmg`](https://data.gov.il/dataset/rmg) | תצלום אויר 2015 2 מטר - גליון רמת מגשימים | ZIP | — |
| 88 | [`rml`](https://data.gov.il/dataset/rml) | תצלום אויר 2015 2 מטר - גליון רמאללה | ZIP | — |
| 89 | [`rng`](https://data.gov.il/dataset/rng) | תצלום אויר 2015 2 מטר - גליון רחובות בנגב | ZIP | — |
| 90 | [`rpn`](https://data.gov.il/dataset/rpn) | תצלום אויר 2015 2 מטר - גליון ראש פינה | ZIP | — |
| 91 | [`rsh`](https://data.gov.il/dataset/rsh) | תצלום אויר 2015 2 מטר - גליון ראשון לציון | ZIP | — |
| 92 | [`rvm`](https://data.gov.il/dataset/rvm) | תצלום אויר 2015 2 מטר - גליון רביבים | ZIP | — |
| 93 | [`school`](https://data.gov.il/dataset/school) | בתי ספר | CSV · 1/1 DataStore | `99b92311-9675-4351-85cd-9ed5ee69a787` |
| 94 | [`sdb`](https://data.gov.il/dataset/sdb) | תצלום אויר 2015 2 מטר - גליון שדה בוקר | ZIP | — |
| 95 | [`sdm`](https://data.gov.il/dataset/sdm) | תצלום אויר 2015 2 מטר - גליון סדום | ZIP | — |
| 96 | [`setl-mid-point`](https://data.gov.il/dataset/setl-mid-point) | שכבת מרכזי ישובים | CSV · 1/1 DataStore | `70ba1705-3b25-416f-939c-985999f87f35` |
| 97 | [`shape`](https://data.gov.il/dataset/shape) | חלקות shape | ZIP · 4 files | — |
| 98 | [`sheetkshape`](https://data.gov.il/dataset/sheetkshape) | מפתחות גושים shape | ZIP | — |
| 99 | [`shf`](https://data.gov.il/dataset/shf) | תצלום אויר 2015 2 מטר - גליון שפרעם | ZIP | — |
| 100 | [`shk`](https://data.gov.il/dataset/shk) | תצלום אויר 2015 2 מטר - גליון שכם | ZIP | — |
| 101 | [`subgushallshape`](https://data.gov.il/dataset/subgushallshape) | גושים shape | ZIP | — |
| 102 | [`svt`](https://data.gov.il/dataset/svt) | תצלום אויר 2015 2 מטר - גליון שבטה | ZIP | — |
| 103 | [`talmudiccollege`](https://data.gov.il/dataset/talmudiccollege) | ישיבות | CSV · 1/1 DataStore | `d6865026-2535-4310-99ec-413b2b7fdda0` |
| 104 | [`tatag`](https://data.gov.il/dataset/tatag) | גבולות תת"ג | ZIP · 1/2 DataStore | `2c8b7b73-828a-4f83-8dce-fd2bc18babab` |
| 105 | [`tly`](https://data.gov.il/dataset/tly) | תצלום אויר 2015 2 מטר - גליון תל אביב | ZIP | — |
| 106 | [`tmt`](https://data.gov.il/dataset/tmt) | תצלום אויר 2015 2 מטר - גליון תל מלחתה | ZIP | — |
| 107 | [`tvr`](https://data.gov.il/dataset/tvr) | תצלום אויר 2015 2 מטר - גליון טבריה | ZIP | — |
| 108 | [`ufh`](https://data.gov.il/dataset/ufh) | תצלום אויר 2015 2 מטר - גליון אום אל פאחם | ZIP | — |
| 109 | [`universities`](https://data.gov.il/dataset/universities) | אוניברסיטאות | CSV · 1/1 DataStore | `1c53badd-f3e3-47c8-b89d-6024ef2e84d3` |
| 110 | [`yhl`](https://data.gov.il/dataset/yhl) | תצלום אויר 2015 2 מטר - גליון יהל | ZIP | — |
| 111 | [`yrh`](https://data.gov.il/dataset/yrh) | תצלום אויר 2015 2 מטר - גליון יריחו | ZIP | — |
| 112 | [`yrs`](https://data.gov.il/dataset/yrs) | תצלום אויר 2015 2 מטר - גליון ירושלים | ZIP | — |
| 113 | [`ytv`](https://data.gov.il/dataset/ytv) | תצלום אויר 2015 2 מטר - גליון יטבתה | ZIP | — |
| 114 | [`zfr`](https://data.gov.il/dataset/zfr) | תצלום אויר 2015 2 מטר - גליון צופר | ZIP | — |
| 115 | [`zft`](https://data.gov.il/dataset/zft) | תצלום אויר 2015 2 מטר - גליון צפת | ZIP | — |
| 116 | [`zlm`](https://data.gov.il/dataset/zlm) | תצלום אויר 2015 2 מטר - גליון צאלים | ZIP | — |

### Ministry of Environmental Protection
<a id="ministry_of_the_environment"></a>
**Slug:** `ministry_of_the_environment` · **Hebrew:** המשרד להגנת הסביבה · **Category:** Environment · **Datasets:** 85

- Org page: https://data.gov.il/organization/ministry_of_the_environment
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_the_environment&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`206`](https://data.gov.il/dataset/206) | מדד חוף נקי | XLSX · 1/1 DataStore | `b9c5393a-430f-457e-b5c7-93139186024f` |
| 2 | [`209`](https://data.gov.il/dataset/209) | עמותות וארגונים למען בעלי חיים | XLS · 1/1 DataStore | `de991a4e-65d9-4f83-bac9-1090a74cd062` |
| 3 | [`557`](https://data.gov.il/dataset/557) | בעלי היתר לביצוע מדידות קרינה בלתי מייננת | XLSX · 1/1 DataStore | `1a2b459d-2685-4fe3-ac0b-ebaca7f3aee0` |
| 4 | [`air-stations`](https://data.gov.il/dataset/air-stations) | תחנות ניטור איכות אוויר | CSV/XLSX · 2/2 DataStore | `9e6daaea-fd72-4ee2-882b-38a5eee135f0` |
| 5 | [`ambrosia`](https://data.gov.il/dataset/ambrosia) | מוקדי אמברוסיה | CSV | — |
| 6 | [`antenna_hakama`](https://data.gov.il/dataset/antenna_hakama) | אנטנות סלולריות בהקמה | XLSX · 1/1 DataStore | `ff398c7e-c522-4ee8-a53a-312b188a573d` |
| 7 | [`antennaactive`](https://data.gov.il/dataset/antennaactive) | אנטנות סלולריות פעילות | CSV · 1/1 DataStore | `8935c8e5-ec77-421f-af86-d970583195f8` |
| 8 | [`ap`](https://data.gov.il/dataset/ap) | חשיפה לרעש משדות תעופה | ZIP | — |
| 9 | [`aquifer-sensitivity`](https://data.gov.il/dataset/aquifer-sensitivity) | אזורי סכנה למקורות מים מזיהום דלק | XML | — |
| 10 | [`archivesfreedomofinformationforzover`](https://data.gov.il/dataset/archivesfreedomofinformationforzover) | מאגר חופש המידע (ארכיון) | CSV · 1/1 DataStore | `a94b346f-f832-4200-afbd-13b396673576` |
| 11 | [`archivespermissiontostreamforzover`](https://data.gov.il/dataset/archivespermissiontostreamforzover) | מאגר צווי הרשאה להזרמה לנחלים (ארכיון) | CSV · 1/1 DataStore | `f359fa80-c9c1-452b-b8ff-a69853048cdb` |
| 12 | [`archivespermitflowingtoseaforzover-csv`](https://data.gov.il/dataset/archivespermitflowingtoseaforzover-csv) | מאגר היתרי הזרמה הטלה לים (ארכיון) | CSV · 1/1 DataStore | `f0afd6e0-ca3b-4621-91f9-6cf70b0cf2c8` |
| 13 | [`asbest`](https://data.gov.il/dataset/asbest) | מרשם העוסקים באסבסט | CSV · 1/1 DataStore | `512d916e-07f0-4774-b84a-3a989e45e7eb` |
| 14 | [`asbest-permit-03-2016`](https://data.gov.il/dataset/asbest-permit-03-2016) | היתרים לעבודות אסבסט | CSV | — |
| 15 | [`asbest-waste-sites`](https://data.gov.il/dataset/asbest-waste-sites) | אתרי פסולת אסבסט | CSV · 1/1 DataStore | `193b86b7-14e0-4866-8410-86ae013c3f0c` |
| 16 | [`asbestos-lab`](https://data.gov.il/dataset/asbestos-lab) | מעבדות אסבסט | XLSX · 1/1 DataStore | `e854dc1d-a9dc-4dd5-b73b-995f7ed5da98` |
| 17 | [`asbestoslandfills`](https://data.gov.il/dataset/asbestoslandfills) | מטמנות אסבסט | XLSX · 1/1 DataStore | `fdb667e6-9217-4eae-9261-367cb0e0cf34` |
| 18 | [`asbestsamplinganalysis`](https://data.gov.il/dataset/asbestsamplinganalysis) | מרשם מעבדות דיגום ואנליזה אסבסט | XLSX · 1/1 DataStore | `022e3947-c8cf-403f-896f-5f0e76acfa20` |
| 19 | [`atarim-leumim`](https://data.gov.il/dataset/atarim-leumim) | אתרים לאומיים | XML | — |
| 20 | [`carbon-monoxide`](https://data.gov.il/dataset/carbon-monoxide) | פחמן חד חמצני | XML | — |
| 21 | [`cf-output`](https://data.gov.il/dataset/cf-output) | תחזית חצי-יומית למזהמי אוויר | XLSX · 1/1 DataStore | `a976089d-e8e5-4013-8f3d-777b8551c684` |
| 22 | [`citiedistricts`](https://data.gov.il/dataset/citiedistricts) | ישובים ומחוזות | CSV · 1/1 DataStore | `b6ca0817-187e-470f-be34-4561c2e404b2` |
| 23 | [`cleanasbestos`](https://data.gov.il/dataset/cleanasbestos) | פרויקט ניקוי קרקעות מאסבסט פריך בגליל המערבי | XML | — |
| 24 | [`cleanliness`](https://data.gov.il/dataset/cleanliness) | מדידות הניקיון במרחב הציבורי | XLSX · 4/4 DataStore | `3436bb7f-8b67-49be-94a4-3c34c9cc1e7a` |
| 25 | [`coast-sensitivity`](https://data.gov.il/dataset/coast-sensitivity) | רגישות חופי הים לזיהומי שמן | XML | — |
| 26 | [`contaminated_land_tlv`](https://data.gov.il/dataset/contaminated_land_tlv) | שיקום קרקעות מזוהמות - מחוז ת"א | CSV · 1/1 DataStore | `54aa9ff1-2d89-4899-bb57-bf2a749ff4b3` |
| 27 | [`contaminatedterrains`](https://data.gov.il/dataset/contaminatedterrains) | קרקעות מזוהמות | XLSX · 1/1 DataStore | `cbb2ed28-310d-4389-a1ec-64bb538fc090` |
| 28 | [`dargat_ziuhum_cley_tzama`](https://data.gov.il/dataset/dargat_ziuhum_cley_tzama) | דרגת זיהום אוויר של כלי צמ"ה | XLSX · 1/1 DataStore | `f2e130e8-bc94-4443-91bd-3ba3353b1494` |
| 29 | [`digumi_arubut`](https://data.gov.il/dataset/digumi_arubut) | מאגר זיהום אוויר מארובות | CSV · 1/1 DataStore | `d8b6d9dd-12b3-4f79-b900-5e171debdf51` |
| 30 | [`domestic_pesticides`](https://data.gov.il/dataset/domestic_pesticides) | תכשירי הדברה מורשים לשימוש | CSV · 1/1 DataStore | `2d741cd4-9c54-492c-8607-933deddb3094` |
| 31 | [`ecological-mapping-for-mosquito-controle`](https://data.gov.il/dataset/ecological-mapping-for-mosquito-controle) | מיפוי אקולוגי להדברת יתושים | ZIP | — |
| 32 | [`environmental_impact_index`](https://data.gov.il/dataset/environmental_impact_index) | מאגר מדד השפעה הסביבתית | CSV · 1/1 DataStore | `fb5159d5-07dd-4b99-87f8-ca4561bc764d` |
| 33 | [`factory`](https://data.gov.il/dataset/factory) | מפעלים | CSV · 1/1 DataStore | `88d1883c-3b7a-4580-9be9-6d54659666c3` |
| 34 | [`financial-sanctions`](https://data.gov.il/dataset/financial-sanctions) | עיצומים כספיים | CSV · 2/2 DataStore | `f7e02b92-4a18-4306-954a-4ea701655fd1` |
| 35 | [`fireant`](https://data.gov.il/dataset/fireant) | ניטור נמלת האש הקטנה במשתלות | XLSX · 1/1 DataStore | `e32a5b9b-cc03-45a0-ae67-f4c3b7242140` |
| 36 | [`freedom-of-info`](https://data.gov.il/dataset/freedom-of-info) | מאגר חופש המידע | CSV/XLSX · 2/2 DataStore | `958b011c-3a10-4dd0-bd09-dbf04cd2cace` |
| 37 | [`greenbuildings`](https://data.gov.il/dataset/greenbuildings) | מבנים ירוקים | CSV · 1/1 DataStore | `7f467a30-58cd-44b5-86f0-d570cc7d25ad` |
| 38 | [`greenkd`](https://data.gov.il/dataset/greenkd) | גנים ירוקים | XLS/XLSX · 2/2 DataStore | `57064159-d2d1-48a0-9fb1-b3439a1ae2b0` |
| 39 | [`greenschools`](https://data.gov.il/dataset/greenschools) | בתי ספר ירוקים | CSV · 1/1 DataStore | `08b04a94-8c4d-48a3-a2e4-64957adbfe3f` |
| 40 | [`hafradat-psolet`](https://data.gov.il/dataset/hafradat-psolet) | הפרדת פסולת ברשויות המקומיות | XML | — |
| 41 | [`hamidrach_products_lca_environmental_impact_reports`](https://data.gov.il/dataset/hamidrach_products_lca_environmental_impact_reports) | המדרך דיווחי השפעות סביבתיות מדודות ממוצרים | CSV/PDF · 1/2 DataStore | `cd20b024-bbcb-4a4c-a5c3-542a590fa3a0` |
| 42 | [`hativot-nof`](https://data.gov.il/dataset/hativot-nof) | חטיבות נוף | ZIP | — |
| 43 | [`hof-naki`](https://data.gov.il/dataset/hof-naki) | מדד הניקיון בחופי ישראל | XML | — |
| 44 | [`industrialareas`](https://data.gov.il/dataset/industrialareas) | אזורי תעשייה הנדרשים בביצוע סקר קרקע | ?/XML · 2 files | — |
| 45 | [`installed-filters`](https://data.gov.il/dataset/installed-filters) | מסנני חלקיקים מותקנים בכלי רכב | CSV/XLSX · 1/2 DataStore | `14c0c07b-69e9-4eaf-affc-ff01b2d0def4` |
| 46 | [`legislation`](https://data.gov.il/dataset/legislation) | חוקים ותקנות | CSV/XLS · 2/2 DataStore | `4abe2a61-9e94-482d-8a9b-19d5af3b3bef` |
| 47 | [`licences_per_missions_facilities`](https://data.gov.il/dataset/licences_per_missions_facilities) | רישיונות עסק והיתרים מסוגים שונים למפעלים | CSV · 1/1 DataStore | `e9ecedbd-8f93-437e-9a2f-4ff908daf210` |
| 48 | [`madbirim`](https://data.gov.il/dataset/madbirim) | מדבירים מורשים | CSV · 1/1 DataStore | `4941fd97-9f9f-4e45-b117-9f71735e9845` |
| 49 | [`maflasmultiannual`](https://data.gov.il/dataset/maflasmultiannual) | מפל"ס - נתונים רב שנתיים | CSV · 1/1 DataStore | `87c88ab8-3076-4422-a8fb-27bc57ce4b76` |
| 50 | [`maflasmultiannualforzover`](https://data.gov.il/dataset/maflasmultiannualforzover) | מפל"ס - רשימת מפעלים | CSV · 1/1 DataStore | `7ad8ddc7-87f4-45f9-84e4-d7f972662153` |
| 51 | [`mahozot`](https://data.gov.il/dataset/mahozot) | מחוזות המשרד להגנת הסביבה | GDB/XML · 2 files | — |
| 52 | [`matash`](https://data.gov.il/dataset/matash) | מכוני טיהור שפכים - מט"ש | XLSX · 1/1 DataStore | `50fc7ac9-4da1-46a6-99da-1c211e31959f` |
| 53 | [`matmenot-binyan`](https://data.gov.il/dataset/matmenot-binyan) | מטמנות לפסולת בנין | XLSX · 1/1 DataStore | `beae591b-cc75-414c-976a-f898ff46c989` |
| 54 | [`matmenot-psolet-mixed`](https://data.gov.il/dataset/matmenot-psolet-mixed) | מטמנות לפסולת מעורבת | XLSX · 1/1 DataStore | `261b9c27-58ad-496e-b8c4-6f2687301a09` |
| 55 | [`miflas2012`](https://data.gov.il/dataset/miflas2012) | מפל"ס 2012 | CSV/XLSX/XML · 3 files | — |
| 56 | [`miflas2013`](https://data.gov.il/dataset/miflas2013) | מפל"ס 2013 | CSV/XLSX/XML · 3 files | — |
| 57 | [`miflas2014`](https://data.gov.il/dataset/miflas2014) | מפל"ס 2014 | CSV/XLSX/XML · 3 files | — |
| 58 | [`miflas2015`](https://data.gov.il/dataset/miflas2015) | מפל"ס 2015 | CSV/XLSX/XML · 3 files | — |
| 59 | [`miflas2016`](https://data.gov.il/dataset/miflas2016) | מפל"ס 2016 | CSV/XLSX/XML · 1/3 DataStore | `a09cfbdd-688b-40ad-a396-9d4a69fcac11` |
| 60 | [`miflas2017`](https://data.gov.il/dataset/miflas2017) | מפל"ס 2017 | CSV/XLSX/XML · 4 files | — |
| 61 | [`nitrogen_oxides`](https://data.gov.il/dataset/nitrogen_oxides) | תחמוצות חנקן | XML | — |
| 62 | [`nitur-yamit`](https://data.gov.il/dataset/nitur-yamit) | תוכניות ניטור ימיות | XLSX/XML · 1/2 DataStore | `50999800-8320-46e3-92ae-b5dd77bbbcda` |
| 63 | [`nmvoc`](https://data.gov.il/dataset/nmvoc) | תרכובות אורגניות נדיפות | XML | — |
| 64 | [`noise-duration`](https://data.gov.il/dataset/noise-duration) | מפלסי רעש מותרים בחוק | XLSX · 1/1 DataStore | `08d825a2-49fd-42df-bbcb-5cc407701d9d` |
| 65 | [`open-area-sens`](https://data.gov.il/dataset/open-area-sens) | רגישות שטחים פתוחים | XML | — |
| 66 | [`open-call`](https://data.gov.il/dataset/open-call) | קול קורא - משרד להגנת הסביבה | CSV/XLSX · 2/2 DataStore | `e16017d1-d7dd-4ddb-a8e4-b6deb7220a22` |
| 67 | [`permitemissionforzovar`](https://data.gov.il/dataset/permitemissionforzovar) | מאגר היתרי פליטה לאוויר | CSV · 1/1 DataStore | `c84b4fa4-9102-4fb8-93ff-c21ecd37566f` |
| 68 | [`pm-10`](https://data.gov.il/dataset/pm-10) | חומר חלקקי PM10 | XML | — |
| 69 | [`pm2-5`](https://data.gov.il/dataset/pm2-5) | חומר חלקקי PM2.5 | XML | — |
| 70 | [`pollute-diesel-vehicles`](https://data.gov.il/dataset/pollute-diesel-vehicles) | רכבי דיזל מזהמים | CSV/XLSX · 2 files | — |
| 71 | [`publictakalot`](https://data.gov.il/dataset/publictakalot) | דיווח על תקלה לידיעת הציבור | CSV · 1/1 DataStore | `84c67bf9-dbd6-4f1d-86f5-a69c092a945d` |
| 72 | [`radon`](https://data.gov.il/dataset/radon) | סקר ראדון | XML | — |
| 73 | [`radon-lab-practitioners`](https://data.gov.il/dataset/radon-lab-practitioners) | מעבדות לבדיקת גז ראדון ותכולת חומרים רדיואקטיביים | CSV · 1/1 DataStore | `e1524397-c09b-41db-915d-8d5a1ed77b72` |
| 74 | [`radon-practitioners`](https://data.gov.il/dataset/radon-practitioners) | בעלי היתר לשירותי בדיקת גז ראדון | CSV · 1/1 DataStore | `a27ff810-d54a-45f7-ae21-173c1d374aa3` |
| 75 | [`researches`](https://data.gov.il/dataset/researches) | מחקרי המדען הראשי | CSV · 1/1 DataStore | `b06cb217-6465-4b42-b9e2-cd4b08fe7b07` |
| 76 | [`river-permits`](https://data.gov.il/dataset/river-permits) | צווי הרשאה להזרמה לנחלים | XLSX | — |
| 77 | [`roads`](https://data.gov.il/dataset/roads) | פליטות מזהמים מכבישים | XML | — |
| 78 | [`stream-monitoring`](https://data.gov.il/dataset/stream-monitoring) | תוצאות ניטור כימי של נחלי ישראל | XLSX · 1/1 DataStore | `97bfde19-81cd-4ff4-98d2-2480c47fd5b6` |
| 79 | [`sulfur-oxides`](https://data.gov.il/dataset/sulfur-oxides) | תחמוצות גופרית | XML | — |
| 80 | [`support`](https://data.gov.il/dataset/support) | תמיכות | CSV/XLSX · 2/2 DataStore | `17eee225-6431-44ba-9967-fa61c5794b5e` |
| 81 | [`svivaniturmifal`](https://data.gov.il/dataset/svivaniturmifal) | פליטות ממפעלים | CSV · 1/1 DataStore | `8f909c24-c120-43a9-a720-de5c27f12d06` |
| 82 | [`waste-information-system`](https://data.gov.il/dataset/waste-information-system) | מערכת מידע פסולת - נספחים | CSV/XLSX · 12/12 DataStore | `ca71e149-49f1-48a2-b319-b27be21e3e21` |
| 83 | [`wide-approval`](https://data.gov.il/dataset/wide-approval) | מפעלים בעלי אישור רוחבי | CSV | — |
| 84 | [`world-environmental-days`](https://data.gov.il/dataset/world-environmental-days) | ימי סביבה עולמיים | XLSX · 1/1 DataStore | `49b7a8ef-447d-41dc-bfc4-2fa4bd30db86` |
| 85 | [`yehidot`](https://data.gov.il/dataset/yehidot) | יחידות סביבתיות ואיגודי ערים לאיכות הסביבה | XLSX | — |

### Ministry of Justice
<a id="ministry_of_justice"></a>
**Slug:** `ministry_of_justice` · **Hebrew:** משרד המשפטים · **Category:** Justice · **Datasets:** 82

- Org page: https://data.gov.il/organization/ministry_of_justice
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_justice&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2021`](https://data.gov.il/dataset/2021) | היחידה לחופש המידע - דוח שנתי 2021 | CSV/PDF · 1/2 DataStore | `b1cd57b3-e176-47bc-b3d8-4b57932fb60c` |
| 2 | [`813`](https://data.gov.il/dataset/813) | רשימת הממונים ברשויות הציבוריות מכח חוק חופש המידע, התשנ"ח-1998 פרטי המאגר | XLSX · 1/1 DataStore | `0340becb-132a-4e2d-864b-562b8c17da42` |
| 3 | [`814`](https://data.gov.il/dataset/814) | תשובות לבקשות חופש מידע | XML | — |
| 4 | [`Housingpropertyportfolios`](https://data.gov.il/dataset/Housingpropertyportfolios) | תיקי נכסי דיור  של משרד המשפטים | CSV/PDF · 1/2 DataStore | `3934203a-70f9-45da-8c76-0594a7363872` |
| 5 | [`accessibilityorders`](https://data.gov.il/dataset/accessibilityorders) | תיקי פיקוח חדשים עם תוצאה תקינה - נציבות שוויון זכויות לאנשים עם מוגבלות | CSV/PDF · 1/2 DataStore | `f3fd5657-1b75-46ef-9a10-9f434b326aa7` |
| 6 | [`ararim`](https://data.gov.il/dataset/ararim) | מאגר החלטות בית הדין לעררים | CSV/PDF · 1/2 DataStore | `b9580b33-6b41-4ca3-b6e1-eb4bbf96a318` |
| 7 | [`atirot`](https://data.gov.il/dataset/atirot) | היחידה לחופש המידע - מאגר עתירות | CSV/PDF · 1/2 DataStore | `28b9da01-bef5-4c89-bffd-ff79d85bf48f` |
| 8 | [`bakashot_cpc`](https://data.gov.il/dataset/bakashot_cpc) | סיווגי CPC לבקשות פטנט | CSV/PDF · 1/2 DataStore | `b2c59e21-c345-4b02-b071-2890a3d431d6` |
| 9 | [`bakashot_ipc`](https://data.gov.il/dataset/bakashot_ipc) | סיווגי IPC לבקשות פטנט | CSV/PDF · 1/2 DataStore | `3343e150-79b5-4927-adad-50ebe14925b5` |
| 10 | [`bakashot_patents`](https://data.gov.il/dataset/bakashot_patents) | בקשות לפטנטים | CSV/PDF · 1/2 DataStore | `adca9a88-bf91-462a-8a49-62381af9b588` |
| 11 | [`britzugiyut`](https://data.gov.il/dataset/britzugiyut) | מרשם ברית הזוגיות | CSV · 2/2 DataStore | `aa86b074-58c2-4e36-a2bb-a61dd6f87117` |
| 12 | [`chiyuvim`](https://data.gov.il/dataset/chiyuvim) | הכנסות וגבייה משרד המשפטים | CSV/PDF · 8/9 DataStore | `69adb272-de96-4db0-bb3c-19477e3014f8` |
| 13 | [`chovotpirsum_iriot`](https://data.gov.il/dataset/chovotpirsum_iriot) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי האינטרנט של הרשויות המקומיות-עיריות | CSV · 1/1 DataStore | `8be11226-18b4-42f3-94c1-e2f54a4e94f6` |
| 14 | [`chovotpirsum_moatzotezoriyot_kavyark`](https://data.gov.il/dataset/chovotpirsum_moatzotezoriyot_kavyark) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי הרשויות המקומיות-מועצות אזוריות מעבר לקו הירוק | CSV · 1/1 DataStore | `4e42f167-bd5c-404d-b096-5c3255580b90` |
| 15 | [`chovotpirsum_moatzotezoryot`](https://data.gov.il/dataset/chovotpirsum_moatzotezoryot) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי הרשויות המקומיות-מועצות אזוריות | CSV · 1/1 DataStore | `63835719-8b17-4524-8c98-8a6069467a3e` |
| 16 | [`chovotpirsum_moatzotmekomyot`](https://data.gov.il/dataset/chovotpirsum_moatzotmekomyot) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי האינטרנט של הרשויות המקומיות-מועצות מקומיות | CSV · 1/1 DataStore | `de35de46-132b-407a-8d61-5feba0b9e503` |
| 17 | [`chovotpirsum_moatzotmekomyotkavyarok`](https://data.gov.il/dataset/chovotpirsum_moatzotmekomyotkavyarok) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי הרשויות המקומיות-מועצות מקומיות מעבר לקו הירוק | CSV · 1/1 DataStore | `0807a39f-d9e1-402d-a82f-9630f0849b3d` |
| 18 | [`chovotpirsum_vaadamekomitletichnunuvnia`](https://data.gov.il/dataset/chovotpirsum_vaadamekomitletichnunuvnia) | היחידה הממשלתית לחופש המידע-חובות הפרסום באתרי הרשויות המקומיות-ועדה מקומית לתכנון ובניה בעירייה | CSV · 1/1 DataStore | `78fbedda-2435-4d04-aaa2-7a2727c60fb7` |
| 19 | [`companiespersonscleansing20200`](https://data.gov.il/dataset/companiespersonscleansing20200) | רשימת החברות בהן בוצע תיקון מחשובי לבעלי התפקידים בהם | CSV · 1/1 DataStore | `4013dda7-be38-4ab8-8822-5afe733b429b` |
| 20 | [`continuing_education`](https://data.gov.il/dataset/continuing_education) | המכון להשתלמות פרקליטים ויועצים משפטיים – תכנית השתלמויות שנתית | XLSX · 1/1 DataStore | `b288cf2c-2bd0-4bba-bcd1-493458435edc` |
| 21 | [`cpalist`](https://data.gov.il/dataset/cpalist) | מאגר רואי החשבון | CSV/PDF · 1/2 DataStore | `7e86def9-0899-45f4-8942-d6fe38482b1a` |
| 22 | [`cpc`](https://data.gov.il/dataset/cpc) | סיווגי CPC | CSV/PDF · 1/2 DataStore | `cf8ed236-6bb2-4df4-91b9-4881102daec0` |
| 23 | [`data-gov-il-dataset-designs`](https://data.gov.il/dataset/data-gov-il-dataset-designs) | עיצובים(מדגמים) | CSV/PDF · 1/2 DataStore | `56e2bfbd-7c6b-461a-aee6-c9de4a10e498` |
| 24 | [`druzim`](https://data.gov.il/dataset/druzim) | בתי הדין הדרוזים - תיקים וחוזי נישואין | CSV/PDF · 2/3 DataStore | `a5c62922-0f26-4104-9445-da6d8ce47aa5` |
| 25 | [`druzim_kadim`](https://data.gov.il/dataset/druzim_kadim) | בתי הדין הדרוזים - קאדים | CSV/PDF · 1/2 DataStore | `3c255886-3a49-4aad-b56a-d432c693717c` |
| 26 | [`employeetravel`](https://data.gov.il/dataset/employeetravel) | מאגר נסיעות עובדים | XLSX · 7/7 DataStore | `483e6415-0ff8-460a-a9c8-63c0faf3a639` |
| 27 | [`ezvonot2018`](https://data.gov.il/dataset/ezvonot2018) | מאגר עזבונות לטובת המדינה | CSV/PDF · 5/6 DataStore | `4dc59d4d-26ea-49c6-b83c-b019addc6ec9` |
| 28 | [`gizanut`](https://data.gov.il/dataset/gizanut) | ממונים משרדיים למניעת גזענות | XLSX · 1/1 DataStore | `ff07a3d4-134a-490e-8264-1cd821e437be` |
| 29 | [`government_advertising`](https://data.gov.il/dataset/government_advertising) | חובות הפרסום באתרי משרדי הממשלה | XLSX · 1/1 DataStore | `df12ff2e-67ea-4d03-9ae5-fc198daa591d` |
| 30 | [`hakirot`](https://data.gov.il/dataset/hakirot) | רשימת משרד חקירות | CSV · 1/1 DataStore | `dcf4d85b-66ab-47b8-bd16-7cc79360fc96` |
| 31 | [`halicim_bateydin`](https://data.gov.il/dataset/halicim_bateydin) | הליכי בתי הדין ברשות הפטנטים | CSV/PDF · 1/2 DataStore | `df6abde0-8746-48c4-b09a-d9b20a7c6f9c` |
| 32 | [`hasmachottoveim`](https://data.gov.il/dataset/hasmachottoveim) | רשימת התובעים בעלי הסמכה מאת היועץ המשפטי לממשלה | CSV/PDF · 1/2 DataStore | `19ea0497-654a-4417-aa7a-0426a99ef946` |
| 33 | [`hekdeshot`](https://data.gov.il/dataset/hekdeshot) | רשות התאגידים - רשם ההקדשות | CSV/PDF · 3/4 DataStore | `f70898aa-9d47-47b2-b1bc-ec736b76bfe2` |
| 34 | [`hofesh`](https://data.gov.il/dataset/hofesh) | רשימת הרשויות הציבוריות מתוקף חוק חופש המידע | XLSX · 1/1 DataStore | `e6429707-50d0-4682-880a-4f11431b5da4` |
| 35 | [`hofesh_hameida`](https://data.gov.il/dataset/hofesh_hameida) | מאגר תלונות חופש המידע | CSV/PDF/XLSX · 2/3 DataStore | `b460e022-0f7c-48c6-ba64-ce16e1340056` |
| 36 | [`hokrim`](https://data.gov.il/dataset/hokrim) | רשימת חוקרים פרטיים | XLSX · 1/1 DataStore | `a9ddb445-825f-4635-a573-fe82d2a95bf0` |
| 37 | [`housingcontractfiles`](https://data.gov.il/dataset/housingcontractfiles) | תיקי חוזי דיור של משרד המשפטים | CSV/PDF · 1/2 DataStore | `e279e48c-4118-4b7e-aa18-9443040cffdf` |
| 38 | [`ica-changes`](https://data.gov.il/dataset/ica-changes) | פרטי שינויים בחברות ושותפויות | CSV/PDF · 1/3 DataStore | `28780ab5-3ef1-44c7-8377-da82c0aa6781` |
| 39 | [`ica-deletion`](https://data.gov.il/dataset/ica-deletion) | מאגר החברות המיועדות למחיקה | CSV · 1/1 DataStore | `0fd312bb-68c9-4647-b186-60c3e7b4f6f7` |
| 40 | [`ica_companies`](https://data.gov.il/dataset/ica_companies) | מאגר חברות - רשם החברות | CSV/PDF · 1/2 DataStore | `f004176c-b85f-4542-8901-7b3176f9a054` |
| 41 | [`ica_partnerships`](https://data.gov.il/dataset/ica_partnerships) | מאגר שותפויות - רשם החברות | CSV/PDF · 1/2 DataStore | `139aa193-fabb-4f6b-a71b-0bb40fd73eb2` |
| 42 | [`ipc`](https://data.gov.il/dataset/ipc) | סיווגי IPC | CSV/PDF · 1/2 DataStore | `78c52e4e-8e49-4531-b2f2-edc766cbbd64` |
| 43 | [`judgments`](https://data.gov.il/dataset/judgments) | היחידה לחופש המידע - מאגר פסקי דין | CSV/PDF · 1/2 DataStore | `6a469006-3844-476f-84e8-960a8fd9df22` |
| 44 | [`justice-miflagot`](https://data.gov.il/dataset/justice-miflagot) | מאגר רשם המפלגות | CSV/PDF · 1/2 DataStore | `1dbfc053-e92f-4354-92d6-1b99aadb20d7` |
| 45 | [`justice-patent-attorneys`](https://data.gov.il/dataset/justice-patent-attorneys) | מאגר עורכי פטנטים | CSV/PDF · 1/2 DataStore | `0ff306c2-1ad9-4974-a2be-0420acf35685` |
| 46 | [`kinuyeymakor`](https://data.gov.il/dataset/kinuyeymakor) | כינויי מקור | CSV/PDF · 1/2 DataStore | `defdbacf-de63-425e-962c-569b6f643292` |
| 47 | [`maale`](https://data.gov.il/dataset/maale) | מאגר החלטות בית הדין לעניין שירות התעסוקה-קורונה | XLSX · 1/1 DataStore | `e987099e-ac4d-4b9e-8317-4829a8c205f2` |
| 48 | [`mamtziim_patents`](https://data.gov.il/dataset/mamtziim_patents) | ממציאים לבקשות פטנטים | CSV/PDF · 1/2 DataStore | `abd0e8c3-0b0d-4581-9166-923a3b21bdda` |
| 49 | [`mashkonot`](https://data.gov.il/dataset/mashkonot) | רשם המשכונות | CSV/PDF · 1/2 DataStore | `e7266a9c-fed6-40e4-a28e-8cddc9f44842` |
| 50 | [`membership-in-liquidation`](https://data.gov.il/dataset/membership-in-liquidation) | חברות בפרוק מרצון בהליך מזורז | CSV/PDF · 1/2 DataStore | `6f3f0df3-5968-4135-81c5-8dd76bf89410` |
| 51 | [`metavhim`](https://data.gov.il/dataset/metavhim) | מאגר מתווכים פעילים | CSV/PDF · 2/3 DataStore | `a0f56034-88db-4132-8803-854bcdb01ca1` |
| 52 | [`mevakshimpatents`](https://data.gov.il/dataset/mevakshimpatents) | מבקשים לבקשות פטנט | CSV/PDF · 1/2 DataStore | `b2b87f6c-832c-410d-a753-c52ec15cd793` |
| 53 | [`mishmoret`](https://data.gov.il/dataset/mishmoret) | מאגר החלטות בתי הדין למשמורת | CSV/PDF · 1/2 DataStore | `ee9cc077-763f-44da-aea6-235ffaf72d3a` |
| 54 | [`misradei_hakirot`](https://data.gov.il/dataset/misradei_hakirot) | רשימת תאגידי חוקרים פרטיים | CSV · 1/1 DataStore | `94722051-b0c7-4f73-b543-c558c6c2c660` |
| 55 | [`moj-amutot`](https://data.gov.il/dataset/moj-amutot) | מאגר עמותות וחברות לתועלת הציבור | CSV/PDF · 4/5 DataStore | `be5b7935-3922-45d4-9638-08871b17ec95` |
| 56 | [`my-dataset`](https://data.gov.il/dataset/my-dataset) | אפוטרופוס הכללי-נכסים עזובים-רשימת נעדרים | CSV · 1/1 DataStore | `9df52159-af92-4ede-885f-5461b8bb4611` |
| 57 | [`notary`](https://data.gov.il/dataset/notary) | מאגר הנוטריונים | CSV/PDF · 1/2 DataStore | `3ead5fae-3513-46f8-a458-959ea3e035ae` |
| 58 | [`ofreedom-of-information-report`](https://data.gov.il/dataset/ofreedom-of-information-report) | דוח חופש המידע | CSV/PDF · 2 files | — |
| 59 | [`pdo`](https://data.gov.il/dataset/pdo) | פנקס הסניגורים הציבוריים - הסנגוריה הציבורית | CSV/PDF · 7/8 DataStore | `c0938e1a-259a-41c3-a225-94e477264137` |
| 60 | [`pinkas`](https://data.gov.il/dataset/pinkas) | מאגר פנקס מאגרי המידע | CSV/PDF · 1/3 DataStore | `fd56bf5b-7918-4906-99e4-b0e5102ae268` |
| 61 | [`pr2018`](https://data.gov.il/dataset/pr2018) | מאגר הכונס הרשמי | CSV/PDF · 3/4 DataStore | `d8715392-287f-49b7-9ae3-f21ec5bf55f3` |
| 62 | [`saharbneiadam`](https://data.gov.il/dataset/saharbneiadam) | תיקים בטיפול היחידה לתיאום המאבק בסחר בבני אדם | CSV/PDF · 1/2 DataStore | `329b3f63-fa09-44e7-bddf-286c7f8e3999` |
| 63 | [`samay-dataset`](https://data.gov.il/dataset/samay-dataset) | מאגר נתוני שמאות מכריעה | CSV · 1/1 DataStore | `c4e178ff-9038-45f4-9dd1-fe7aeea6f70c` |
| 64 | [`sekerhashpaotcorona`](https://data.gov.il/dataset/sekerhashpaotcorona) | סקר בנושא שכירות למגורים בתקופת הקורונה  (אוגוסט 2020) – השפעות הקורונה על קיום חוזים | XLSX | — |
| 65 | [`shamaiim`](https://data.gov.il/dataset/shamaiim) | רשימת השמאים המכריעים | CSV/PDF · 1/2 DataStore | `a0839273-c03b-489b-ad51-e5280624ab00` |
| 66 | [`shamaim`](https://data.gov.il/dataset/shamaim) | מאגר שמאי מקרקעין | CSV/PDF · 3/4 DataStore | `8540534a-eccd-4568-a677-652d589ed172` |
| 67 | [`sharaiim_kadim`](https://data.gov.il/dataset/sharaiim_kadim) | בתי הדין השרעיים - קאדים | CSV/PDF · 1/2 DataStore | `10ffbeeb-7496-49b9-b45b-38657b645cfd` |
| 68 | [`sharaim`](https://data.gov.il/dataset/sharaim) | בתי הדין השרעיים - תיקים וחוזי נישואין | CSV/PDF · 2/3 DataStore | `4a566ecb-8d03-4f66-8278-b8d2b4b354ff` |
| 69 | [`sharaim_names`](https://data.gov.il/dataset/sharaim_names) | רשימת הרשמים  בבתי הדין השרעיים - בערבית | CSV · 1/1 DataStore | `52d4950e-8ce3-499c-aac5-f7722dce1b8e` |
| 70 | [`simaneymisahr`](https://data.gov.il/dataset/simaneymisahr) | סימני מסחר | CSV/PDF · 6/7 DataStore | `6284d4a9-fdd4-45c9-a1d6-58143c7d8127` |
| 71 | [`siyua`](https://data.gov.il/dataset/siyua) | סיוע משפטי | CSV/PDF · 4/6 DataStore | `39c7ba4e-499d-476a-9ff9-c1736ec3323a` |
| 72 | [`stateengagementwithlawyers`](https://data.gov.il/dataset/stateengagementwithlawyers) | התקשרות המדינה עם עורכי דין של הוועדה להעסקת עורכי דין חיצוניים | CSV/PDF · 1/2 DataStore | `81108843-f82c-4d35-92fe-ddb9e9aad405` |
| 73 | [`studyapplications`](https://data.gov.il/dataset/studyapplications) | מאגר בקשות לימודים שאושרו על ידי ועדת ההשתלמות המשרדית במשרד המשפטים | PDF/XLSX · 1/2 DataStore | `b32e442a-02b1-448e-aa2e-3f087de40682` |
| 74 | [`supervisionfiles`](https://data.gov.il/dataset/supervisionfiles) | צווי נגישות שנשלחו לחייבים - נציבות שוויון זכויות לאנשים עם מוגבלות | CSV/PDF · 1/2 DataStore | `d5f96487-c776-4382-8498-bfb81aa38c05` |
| 75 | [`tabu_asset`](https://data.gov.il/dataset/tabu_asset) | סוג בעלות בנכסים הרשומים בפנקסי המקרקעין | CSV/PDF · 1/2 DataStore | `a1a91496-d692-4420-bc21-3487600b71a5` |
| 76 | [`takanot_hayerusha-batei_hadin_hadruzim`](https://data.gov.il/dataset/takanot_hayerusha-batei_hadin_hadruzim) | תקנות הירושה – בתי הדין הדרוזים – בשפה הערבית | CSV · 1/1 DataStore | `af0bb999-3773-4c10-aa3c-b22c488f9275` |
| 77 | [`takanot_hayerusha-batei_hadin_hasharaim`](https://data.gov.il/dataset/takanot_hayerusha-batei_hadin_hasharaim) | תקנות הירושה – בתי הדין השרעיים – בשפה הערבית | CSV · 1/1 DataStore | `6a629020-760c-4015-9f27-ebaa896c9794` |
| 78 | [`tlzgizanut`](https://data.gov.il/dataset/tlzgizanut) | מאגר תלונות הציבור ליחידה הממשלתית לתיאום המאבק בגזענות | XLSX · 1/1 DataStore | `575d7272-ed40-4956-ae56-97f1529b2d3c` |
| 79 | [`tovin`](https://data.gov.il/dataset/tovin) | מנהל הטובין | CSV/PDF · 1/2 DataStore | `b7c4b1fb-6e3c-4d6a-92a9-4546dfa0112e` |
| 80 | [`trademarks_nice`](https://data.gov.il/dataset/trademarks_nice) | סימני מסחר - סיווגים | CSV/PDF · 2/3 DataStore | `bc9b55dc-a0c6-4b52-a925-5dabc7ef7979` |
| 81 | [`vaadatezvonot`](https://data.gov.il/dataset/vaadatezvonot) | וועדת העזבונות | CSV/PDF · 1/2 DataStore | `891ae797-bc4e-4222-ad91-eaeb8e765700` |
| 82 | [`yerusha`](https://data.gov.il/dataset/yerusha) | רשם הירושה | CSV/PDF · 1/2 DataStore | `7691b4a2-fe1d-44ec-9f1b-9f2f0a15381b` |

### Ministry of Finance
<a id="mof"></a>
**Slug:** `mof` · **Hebrew:** משרד האוצר · **Category:** Finance · **Datasets:** 60

- Org page: https://data.gov.il/organization/mof
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:mof&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`062019`](https://data.gov.il/dataset/062019) | ביצוע תקציב על שינוייו יוני 2019 לא מבוקר | XLSX | — |
| 2 | [`2004-1997`](https://data.gov.il/dataset/2004-1997) | תקציב וביצוע 2004-1997 כולל יתרת התחיבויות | XLSX · 1/1 DataStore | `d373fc09-a088-4d4e-817a-161f943b03c5` |
| 3 | [`2005`](https://data.gov.il/dataset/2005) | שינויי תקציב 2005 | XLSX/ZIP · 1/2 DataStore | `d93bd241-d6d2-4062-bb6e-42690ce0c5ac` |
| 4 | [`2005-2008`](https://data.gov.il/dataset/2005-2008) | תקציב וביצוע 2005-2008 | XLSX | — |
| 5 | [`2005-2011`](https://data.gov.il/dataset/2005-2011) | שינויי תקציב 2005-2011 | XLSX · 1/1 DataStore | `20facf80-a166-46c9-812a-10c7c65e94cf` |
| 6 | [`2006`](https://data.gov.il/dataset/2006) | שינויי תקציב 2006 | XLSX/ZIP · 1/2 DataStore | `c8325ebc-0d09-4051-bcb1-90ed8d75acc7` |
| 7 | [`2007`](https://data.gov.il/dataset/2007) | שינויי תקציב 2007 | XLSX/ZIP · 1/2 DataStore | `be634955-fce4-4733-ab88-29e59d9392d0` |
| 8 | [`2008`](https://data.gov.il/dataset/2008) | שינויי תקציב 2008 | XLSX/ZIP · 1/2 DataStore | `c8fc2904-0f0d-4327-8a61-2265a9992218` |
| 9 | [`2009`](https://data.gov.il/dataset/2009) | שינויי תקציב 2009 | XLSX/ZIP · 2 files | — |
| 10 | [`2009-2011`](https://data.gov.il/dataset/2009-2011) | תקציב וביצוע 2009-2011 | XLSX | — |
| 11 | [`2010`](https://data.gov.il/dataset/2010) | שינויי תקציב 2010 | XLSX/ZIP · 1/2 DataStore | `7ad38911-ea56-4ab1-bcae-2b4e6d2a83ab` |
| 12 | [`2011`](https://data.gov.il/dataset/2011) | שינויי תקציב 2011 | ?/CSV · 1/2 DataStore | `b202bd3f-f06b-43d0-bfee-a8a250f10851` |
| 13 | [`2012-2005`](https://data.gov.il/dataset/2012-2005) | תקציב וביצוע 2012-2005 כולל יתרת התחיבויות | XLSX · 1/1 DataStore | `3995b82f-8713-4185-a0ee-26a8c79ca561` |
| 14 | [`2015-2013`](https://data.gov.il/dataset/2015-2013) | תקציב וביצוע 2015-2013 כולל יתרת התחיבויות | XLSX · 1/1 DataStore | `a1b33128-ed29-496a-93a6-d87a788bb681` |
| 15 | [`2017-2018`](https://data.gov.il/dataset/2017-2018) | הצעת תקציב לשנים 2017-2018 | XLSX · 1/1 DataStore | `0785388c-eb39-46b0-bb9c-ecf53b5f6339` |
| 16 | [`2018-2017`](https://data.gov.il/dataset/2018-2017) | תקציב מקורי 2018-2017 | XLSX · 1/1 DataStore | `01d99090-aee0-45e8-8817-de404371d636` |
| 17 | [`30-2021`](https://data.gov.il/dataset/30-2021) | אומדן ביצוע ליום 30 ביוני2021 - לא מבוקר | XLSX | — |
| 18 | [`30-6-2022`](https://data.gov.il/dataset/30-6-2022) | אומדן תקציב וביצוע ליום 30-6-2022 לא מבוקר | XLSX · 1/1 DataStore | `2abb4d0f-2e27-4ef3-876c-ef828c34ef78` |
| 19 | [`30-6-2023`](https://data.gov.il/dataset/30-6-2023) | אומדן ביצוע ליום 30-6-2023 לא מבוקר | XLSX · 1/1 DataStore | `8ac26fbb-0cfb-496b-8bbd-3b1093a00811` |
| 20 | [`30-6-2024`](https://data.gov.il/dataset/30-6-2024) | אומדן ביצוע ליום 30-6-2024 לא מבוקר | XLSX · 1/1 DataStore | `f8075922-f2a1-4f5f-a65f-0a6964530480` |
| 21 | [`30-6-2025`](https://data.gov.il/dataset/30-6-2025) | אומדן ביצוע ליום 30-6-2025 | XLSX · 1/1 DataStore | `ae57077c-3c53-42c0-8e29-e618c5fc8c30` |
| 22 | [`30-9-2021`](https://data.gov.il/dataset/30-9-2021) | אומדן ביצוע ליום 30 בספטמבר 2021 - לא מבוקר | XLSX | — |
| 23 | [`30-9-2022`](https://data.gov.il/dataset/30-9-2022) | אומדן תקציב וביצוע ליום 30-9-2022 לא מבוקר | XLSX · 2/2 DataStore | `d6091f75-e6f1-4d72-9b04-2211f876c25f` |
| 24 | [`30-9-2023`](https://data.gov.il/dataset/30-9-2023) | אומדן ביצוע ליום 30-9-2023 לא מבוקר | XLSX · 1/1 DataStore | `087ff227-cd67-489c-a32b-830c6e40a7eb` |
| 25 | [`30-9-2024`](https://data.gov.il/dataset/30-9-2024) | אומדן ביצוע ליום 30-9-2024 לא מבוקר | XLSX · 1/1 DataStore | `0a82e97f-a9dc-4c6d-9351-8ad24c78129c` |
| 26 | [`31-2021`](https://data.gov.il/dataset/31-2021) | אומדן ביצוע ליום 31 למרץ 2021 - לא מבוקר | XLSX · 1/1 DataStore | `4a0f3ffe-16cc-464e-bda3-f5ef4d4f0bf9` |
| 27 | [`31-2022`](https://data.gov.il/dataset/31-2022) | אומדן תקציב וביצוע ליום 31 במרץ 2022 - לא מבוקר | XLSX · 1/1 DataStore | `ea213c4e-a3a2-4704-8567-297c8c251868` |
| 28 | [`31-3-2023`](https://data.gov.il/dataset/31-3-2023) | אומדן ביצוע ליום 31-3-2023 לא מבוקר | XLSX · 1/1 DataStore | `89e841d7-c1f0-420f-bd2b-a4cda16c5676` |
| 29 | [`31-3-2024`](https://data.gov.il/dataset/31-3-2024) | אומדן ביצוע ליום 31-3-2024 לא מבוקר | XLSX · 1/1 DataStore | `c0836cfb-a6f0-4015-9e8b-35fed05b2326` |
| 30 | [`31-3-2025`](https://data.gov.il/dataset/31-3-2025) | אומדן ביצוע ליום 31-3-2025 לא מבוקר | XLSX · 1/1 DataStore | `404fdbfd-9df7-476f-91be-13a81fdf5bd1` |
| 31 | [`531`](https://data.gov.il/dataset/531) | שינויי תקציב 2012 | XLSX · 1/1 DataStore | `4ad61e9b-59f8-4013-a404-c02349dbede1` |
| 32 | [`534`](https://data.gov.il/dataset/534) | תקציב וביצוע 2012 | XLSX | — |
| 33 | [`564`](https://data.gov.il/dataset/564) | תקציב מקורי 2013-2014 | XLS | — |
| 34 | [`711`](https://data.gov.il/dataset/711) | שינויי תקציב 2013 | XLS/ZIP · 1/2 DataStore | `fefd1ab1-c9d6-43f1-888f-0076dab1194b` |
| 35 | [`808`](https://data.gov.il/dataset/808) | תקציב וביצוע 2013 | XLSX | — |
| 36 | [`953`](https://data.gov.il/dataset/953) | תקציב מאושר 2014 | XLSX | — |
| 37 | [`961`](https://data.gov.il/dataset/961) | תקציב וביצוע 2014 | XLSX | — |
| 38 | [`969`](https://data.gov.il/dataset/969) | תקציב וביצוע 2015 | XLSX · 1/1 DataStore | `b64266ab-ac48-4f17-afeb-4bec445b64cc` |
| 39 | [`982`](https://data.gov.il/dataset/982) | קבצי תקציב וביצוע מעודכנים לשנים 2005-2014, כולל מיון כלכלי | XLSX · 10/10 DataStore | `fe142285-301a-496b-ab23-673930d8f96a` |
| 40 | [`991`](https://data.gov.il/dataset/991) | תקציב מקורי 2016 ברמת תקנה | XLS · 1/1 DataStore | `68602baa-6fee-4988-8a70-dc1491ae5e25` |
| 41 | [`a2016`](https://data.gov.il/dataset/a2016) | תקציב מקורי ומאושר 2016 | XLSX · 1/1 DataStore | `c59d89ca-f38e-4a6a-b542-4f91054ccdc1` |
| 42 | [`accountantgeneralinterest`](https://data.gov.il/dataset/accountantgeneralinterest) | ריביות החשב הכללי | CSV · 1/1 DataStore | `d1cdadd7-f6b6-40a2-aab9-73230d5fe294` |
| 43 | [`assb122019`](https://data.gov.il/dataset/assb122019) | תקציב מול ביצוע ברוטו, כולל מפעלים עסקיים לשנת 2019 | XLSX | — |
| 44 | [`assb32018`](https://data.gov.il/dataset/assb32018) | ביצוע תקציב על שינוייו מרץ 2018 לא מבוקר | XLS · 1/1 DataStore | `97f002b9-91b8-4dcc-b846-7cde43027b17` |
| 45 | [`assb32019`](https://data.gov.il/dataset/assb32019) | ביצוע תקציב על שינוייו מרץ 2019 לא מבוקר | XLSX · 1/1 DataStore | `053eeabf-7cb3-4b90-b553-5a5d1f01c605` |
| 46 | [`assb32020`](https://data.gov.il/dataset/assb32020) | ביצוע תקציב על שינוייו  31 במרץ 2020 -  לא מבוקר | XLSX | — |
| 47 | [`assb62017`](https://data.gov.il/dataset/assb62017) | ביצוע תקציב על שינוייו יוני 2017 לא מבוקר | XLS · 1/1 DataStore | `ecfa85a4-387d-4c62-aba6-6a7f63b69d5f` |
| 48 | [`assb62018`](https://data.gov.il/dataset/assb62018) | ביצוע תקציב על שינוייו יוני 2018 לא מבוקר | XLSX · 1/1 DataStore | `111e2bd0-4b7c-4d33-807c-26119816d190` |
| 49 | [`assb62020`](https://data.gov.il/dataset/assb62020) | אומדן ביצוע תקציב על שינוייו  30 ביוני 2020 -  לא מבוקר | XLSX | — |
| 50 | [`assb92017`](https://data.gov.il/dataset/assb92017) | ביצוע תקציב על שינוייו ספטמבר 2017 לא מבוקר | XLS | — |
| 51 | [`assb92018`](https://data.gov.il/dataset/assb92018) | ביצוע תקציב על שינוייו ספטמבר 2018 לא מבוקר | XLSX · 1/1 DataStore | `c69a69e6-cb44-4c4b-8157-bcad8b3a11b7` |
| 52 | [`assb92019`](https://data.gov.il/dataset/assb92019) | ביצוע תקציב על שינוייו ספטמבר 2019 לא מבוקר | XLSX | — |
| 53 | [`assb92020`](https://data.gov.il/dataset/assb92020) | אומדן ביצוע ליום 30 בספטמבר 2020 לא מבוקר | XLSX | — |
| 54 | [`budget-changes-2014`](https://data.gov.il/dataset/budget-changes-2014) | שינויים תקציביים מאושרים לשנת 2014 | CSV/ZIP · 2 files | — |
| 55 | [`budget-changes-2015`](https://data.gov.il/dataset/budget-changes-2015) | שינויים תקציביים מאושרים לשנת 2015 | CSV/ZIP · 2 files | — |
| 56 | [`budget-changes-2016`](https://data.gov.il/dataset/budget-changes-2016) | שינויים תקציביים מאושרים לשנת 2016 | CSV/ZIP · 2 files | — |
| 57 | [`budget2020`](https://data.gov.il/dataset/budget2020) | ביצוע תקציב המשכי והתוכנית הכלכלית - שנת 2020 - לא מבוקר | XLSX | — |
| 58 | [`goverment-domesticdebt`](https://data.gov.il/dataset/goverment-domesticdebt) | נתוני החוב הממשלתי המקומי | CSV · 8/8 DataStore | `c92fdda2-0939-4110-8ebc-edfcf35e8723` |
| 59 | [`gsa`](https://data.gov.il/dataset/gsa) | רשימת חברות ממשלתיות ודירקטורים מכהנים | CSV · 2/2 DataStore | `2d5abbad-4809-4900-b74f-b2f8b40bcfb8` |
| 60 | [`savingsplaninterest`](https://data.gov.il/dataset/savingsplaninterest) | ריביות של פיקדונות חסכון לכל ילד - עדכון יומי | CSV · 2/2 DataStore | `a737b311-c6d8-4084-9ac9-c40d0fd01125` |

### Ministry of Health
<a id="ministry-health"></a>
**Slug:** `ministry-health` · **Hebrew:** משרד הבריאות · **Category:** Health · **Datasets:** 56

- Org page: https://data.gov.il/organization/ministry-health
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry-health&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`ballancing-homes`](https://data.gov.il/dataset/ballancing-homes) | רשימת בתים מאזנים למניעת אשפוז פסיכיאטרי בפיקוח משרד הבריאות | XLSX · 1/1 DataStore | `b91ac631-742b-44d3-b499-60f456203fd1` |
| 2 | [`bichildrengrowth2016`](https://data.gov.il/dataset/bichildrengrowth2016) | נתוני הערכת גדילה של תלמידים בישראל - משרד הבריאות | XLSX | — |
| 3 | [`birth-data`](https://data.gov.il/dataset/birth-data) | מאגר לידות חי | CSV/PDF · 1/3 DataStore | `0290f6eb-e0fa-4b26-ab27-d02a9d362b77` |
| 4 | [`bureaus-of-health`](https://data.gov.il/dataset/bureaus-of-health) | לשכות הבריאות - משרד הבריאות | XLSX · 1/1 DataStore | `e01d86f2-e89f-4305-90e8-74cb88866092` |
| 5 | [`cannabis_certified_physicians`](https://data.gov.il/dataset/cannabis_certified_physicians) | רופאים המוסמכים להנפיק רישיון לקנביס רפואי | XLSX · 1/1 DataStore | `37f14c29-47af-4b6c-b38e-e08a15e15b5b` |
| 6 | [`cannabis_licensed_workers`](https://data.gov.il/dataset/cannabis_licensed_workers) | בעלי רישיון עיסוק בקנביס | XLSX · 1/1 DataStore | `c05fc5e0-c292-4633-8b06-e4f8b635d2a0` |
| 7 | [`cannabis_pharmacies`](https://data.gov.il/dataset/cannabis_pharmacies) | בתי מרקחת המורשים למכור קנביס רפואי | XLSX · 1/1 DataStore | `f635f611-5b6d-4b21-9cd3-ce7b14da6c11` |
| 8 | [`companies-training-emergency-medicine-medics`](https://data.gov.il/dataset/companies-training-emergency-medicine-medics) | חברות להכשרת חובשי רפואת חירום | CSV · 1/1 DataStore | `06a0faf1-0fac-4a1a-b3e4-ff2bab60dc1e` |
| 9 | [`cord-blood-banks`](https://data.gov.il/dataset/cord-blood-banks) | בנקי דם טבורי - משרד הבריאות | XLSX | — |
| 10 | [`covid-19`](https://data.gov.il/dataset/covid-19) | מאגר COVID-19 | CSV/PDF/XLSX · 24/48 DataStore | `a9588029-8dd6-4c6f-b4ff-e8ca6413642f` |
| 11 | [`database-of-doctors-licenses-moh`](https://data.gov.il/dataset/database-of-doctors-licenses-moh) | מאגר רישיונות רופאים משרד הבריאות | CSV · 1/1 DataStore | `9c64c522-bbc2-48fe-96fb-3b2a8626f59e` |
| 12 | [`drugs-rehab`](https://data.gov.il/dataset/drugs-rehab) | אשפוזיות לגמילה מסמים ומאלכוהול | CSV · 1/1 DataStore | `2b197f80-e3c9-4ac8-a734-b1a1625770ed` |
| 13 | [`environmental-health-professionals-certified`](https://data.gov.il/dataset/environmental-health-professionals-certified) | רשימת בעלי הכשרות בבריאות הסביבה | XLSX · 1/1 DataStore | `6bf142d3-3fcc-45e9-8637-abcf3fc52c1a` |
| 14 | [`fcs-importers`](https://data.gov.il/dataset/fcs-importers) | יבואני מזון בעלי תעודות רישום יבואן בתוקף | CSV · 1/1 DataStore | `31c36cee-80e1-482e-9661-7539c4b27c1b` |
| 15 | [`fcs-manufacturer`](https://data.gov.il/dataset/fcs-manufacturer) | יצרני ועסקי מזון בעלי רישיון יצרן | CSV · 1/1 DataStore | `9c55a7dd-3b92-4141-811c-5e30cc74a8a4` |
| 16 | [`food-fabs-lists`](https://data.gov.il/dataset/food-fabs-lists) | רשימת מעבדות מזון | XLSX · 1/1 DataStore | `59cf6470-94b1-4cd0-8c7e-b292a24c51b4` |
| 17 | [`health-organizations`](https://data.gov.il/dataset/health-organizations) | אוגדן ארגונים ועמותות מתחום הבריאות בישראל | XLSX · 1/1 DataStore | `422972e3-f68f-4d26-bed2-e6b4fb0282a2` |
| 18 | [`health-quality-measurement-family-care-center`](https://data.gov.il/dataset/health-quality-measurement-family-care-center) | התכנית הלאומית למדדי איכות של משרד הבריאות - טיפות חלב | CSV · 13/13 DataStore | `0e91ec84-846a-46ab-bbb0-0d315104abe3` |
| 19 | [`health-quality-measurement-general-hospitalization`](https://data.gov.il/dataset/health-quality-measurement-general-hospitalization) | התכנית הלאומית למדדי איכות של משרד הבריאות - אשפוז כללי | CSV · 21/21 DataStore | `6e0fce9f-9f58-47a9-a356-861cba135225` |
| 20 | [`health-quality-measurement-geriatric`](https://data.gov.il/dataset/health-quality-measurement-geriatric) | התכנית הלאומית למדדי איכות של משרד הבריאות - גריאטריה | CSV · 13/13 DataStore | `ee66e534-601f-4c2b-b1df-7eb1b4a72e0a` |
| 21 | [`health-quality-measurement-mental-health`](https://data.gov.il/dataset/health-quality-measurement-mental-health) | התכנית הלאומית למדדי איכות של משרד הבריאות - בריאות הנפש | CSV · 9/9 DataStore | `3c678810-8079-457a-a923-67b7e7661cae` |
| 22 | [`health-quality-measurement-pre-hospital`](https://data.gov.il/dataset/health-quality-measurement-pre-hospital) | התכנית הלאומית למדדי איכות של משרד הבריאות - פרה הוספיטל | CSV · 7/7 DataStore | `11af0fc1-900a-4373-b32e-dd3331304890` |
| 23 | [`hiv`](https://data.gov.il/dataset/hiv) | מרפאות ומעבדות מוכרות לאבחון נשאות HIV | XLSX · 2/2 DataStore | `7364cf75-5eb4-4f55-8e8b-c30508e5ce0d` |
| 24 | [`hospitals_psyc`](https://data.gov.il/dataset/hospitals_psyc) | בתי חולים פסיכיאטריים ומחלקות פסיכיאטריות בבתי חולים כלליים | XLSX · 1/1 DataStore | `5b4dfe37-ca97-4973-9752-5f1950939832` |
| 25 | [`housing-social-workers`](https://data.gov.il/dataset/housing-social-workers) | עובדות סוציאליות להתאמות דיור לאנשים עם מוגבלויות | XLS · 1/1 DataStore | `59549db7-e1a4-40f2-9311-daaa75781529` |
| 26 | [`intershiplabs`](https://data.gov.il/dataset/intershiplabs) | מעבדות מוכרות לסטאז' - משרד הבריאות | XLS | — |
| 27 | [`ivf`](https://data.gov.il/dataset/ivf) | רישוי יחידות להפריה חוץ גופית IVF - משרד הבריאות | XLSX · 1/1 DataStore | `00bf4829-ddcd-4d7c-b1e3-b727e877d7e9` |
| 28 | [`ivflist`](https://data.gov.il/dataset/ivflist) | רשימת יחידות להפריה חוץ גופית - IVF | XLSX · 1/1 DataStore | `4fb49082-e09e-456b-b40b-22b746bf8321` |
| 29 | [`labs-list`](https://data.gov.il/dataset/labs-list) | מעבדות רפואיות | XLSX · 1/1 DataStore | `23be5eed-ec17-40fc-a8ab-f8df7fc36125` |
| 30 | [`list-measles-vaccination-stations`](https://data.gov.il/dataset/list-measles-vaccination-stations) | תחנות התחסנות כנגד חצבת | CSV · 1/1 DataStore | `54533763-9edb-4fff-bc9b-1952f1ae66d0` |
| 31 | [`measlescoverage`](https://data.gov.il/dataset/measlescoverage) | כיסוי חיסוני החצבת | XLSX · 1/1 DataStore | `1ed79571-04e9-46dc-8b55-566ee78bf9da` |
| 32 | [`medical-tourism-agent-list`](https://data.gov.il/dataset/medical-tourism-agent-list) | רשימת סוכני תיירות מרפא | XLSX · 4/4 DataStore | `2ccc36ae-b6e3-4592-969e-80fc22f48a40` |
| 33 | [`mental-health-institutions-emergency-health-unit`](https://data.gov.il/dataset/mental-health-institutions-emergency-health-unit) | רשימת מסגרות לבריאות הנפש (הוסטלים) של הרווחה - אגף לשעת חירום | XLSX · 1/1 DataStore | `95e53c1e-aa71-432d-8c38-34a13b3b3b33` |
| 34 | [`mentalhealthclinics`](https://data.gov.il/dataset/mentalhealthclinics) | מרפאות בריאות הנפש - משרד הבריאות | XLSX · 1/1 DataStore | `f7a7b061-db5b-4e19-b1bf-2d7525af52ca` |
| 35 | [`mtl-families-centers`](https://data.gov.il/dataset/mtl-families-centers) | מרכזי יעוץ למשפחות של נפגעי נפש | CSV · 1/1 DataStore | `cef1c51a-452f-484d-8834-6bd77f696ad8` |
| 36 | [`multilingual-signage-db`](https://data.gov.il/dataset/multilingual-signage-db) | מונחון רב-לשוני לשמות יחידות בריאות | XLSX · 1/1 DataStore | `32355e02-f72a-4b9a-a327-1e12b5ea83f1` |
| 37 | [`nutrition-database`](https://data.gov.il/dataset/nutrition-database) | מאגר התזונה הלאומי הישראלי | CSV/XLSX · 8/8 DataStore | `c3cb0630-0650-46c1-a068-82d575c094b2` |
| 38 | [`permit-pharm`](https://data.gov.il/dataset/permit-pharm) | רוקחים בעלי הרשאה אישית | XLSX · 1/1 DataStore | `73df1b93-9735-4bc0-b84d-aa5f6bcbfb92` |
| 39 | [`prescription-drug-addiction-treatment-clinics`](https://data.gov.il/dataset/prescription-drug-addiction-treatment-clinics) | מרפאות לטיפול בהתמכרות לתרופות מרשם | CSV · 1/1 DataStore | `a05837e9-8e0f-421b-af29-3ec8d9d6c704` |
| 40 | [`private-covid-test`](https://data.gov.il/dataset/private-covid-test) | בתי חולים המבצעים בדיקות קורונה פרטיות | XLSX · 4/4 DataStore | `7861f609-3f8b-4f7f-9c8d-eaf5007f7466` |
| 41 | [`psychiatric-hospitals-emergency-health-unit`](https://data.gov.il/dataset/psychiatric-hospitals-emergency-health-unit) | רשימת בתי חולים פסיכיאטריים ממשלתי וכללית - האגף לשעת חירום | XLSX · 1/1 DataStore | `23be69ef-4f35-4785-90c0-1d2fcab35586` |
| 42 | [`rare-diseases-list`](https://data.gov.il/dataset/rare-diseases-list) | אוגדן מחלות נדירות | XLSX · 1/1 DataStore | `926899e6-079b-48e4-a4f9-515d8940a419` |
| 43 | [`reg-green-countries-he`](https://data.gov.il/dataset/reg-green-countries-he) | רשימת יעדים מסוכנים ואזהרות מסע (קורונה) לתקופת הקורונה | XLSX · 4/4 DataStore | `486e0319-e667-4904-b930-7d6d892496ca` |
| 44 | [`resilience-centers`](https://data.gov.il/dataset/resilience-centers) | מרכזי חוסן | CSV · 1/1 DataStore | `457673b2-c3c4-4cb5-909c-03b29d8ce1ff` |
| 45 | [`satisfaction-hosp-general2014`](https://data.gov.il/dataset/satisfaction-hosp-general2014) | סקר חוויית המטופל מהטיפול בבתי חולים כלליים 2014 | XLSX · 1/1 DataStore | `cbb2e19a-a419-453c-a2e0-1b0d887ee7b0` |
| 46 | [`satisfaction-hosp-general2016`](https://data.gov.il/dataset/satisfaction-hosp-general2016) | סקר חוויית המטופל מהטיפול בבתי חולים כלליים 2016 - משרד הבריאות | XLS · 1/1 DataStore | `ac080ca8-48d0-41c5-a9c5-6f46023ef56e` |
| 47 | [`satisfaction-hosp-psychiatry-2015`](https://data.gov.il/dataset/satisfaction-hosp-psychiatry-2015) | סקר חוויית המטופל מהטיפול בבתי חולים פסיכיאטריים 2015 - משרד הבריאות | XLSX | — |
| 48 | [`satisfaction-hosp-psychiatry-2017`](https://data.gov.il/dataset/satisfaction-hosp-psychiatry-2017) | סקר חוויית המטופל מהטיפול בבתי חולים פסיכיאטריים 2017 - משרד הבריאות | XLSX | — |
| 49 | [`satisfaction-malrad-2015`](https://data.gov.il/dataset/satisfaction-malrad-2015) | סקר חווית המטופל מהטיפול במלר"ד 2015 - משרד הבריאות | XLSX · 1/1 DataStore | `be05956c-68e9-4330-8ecd-69f6959c9569` |
| 50 | [`serologiclabs`](https://data.gov.il/dataset/serologiclabs) | serologiclabs | XLSX · 4/4 DataStore | `b3c89abc-8e86-4abd-a4f3-a33ebee9fc07` |
| 51 | [`staj`](https://data.gov.il/dataset/staj) | נתוני הגרלות סטאזרים לרפואה | XLSX · 1/1 DataStore | `24273aa9-4abb-44b5-bd08-641c2ecd517f` |
| 52 | [`trauma-centers`](https://data.gov.il/dataset/trauma-centers) | מרכזי טראומה | CSV · 1/1 DataStore | `dd974a58-fb15-43bb-9038-fa8cfe7cce31` |
| 53 | [`vaccine-codes-lot-nachlieli`](https://data.gov.il/dataset/vaccine-codes-lot-nachlieli) | קטלוג חיסונים ואצוות לפנקס החיסונים הדיגיטלי - נחליאלי | CSV · 4/4 DataStore | `2d4cec2c-d153-4bf9-95c6-256860d7857e` |
| 54 | [`vaccines-abroad-price-list`](https://data.gov.il/dataset/vaccines-abroad-price-list) | מחירון חיסונים לנוסעים לחו"ל - משרד הבריאות | XLSX · 1/1 DataStore | `51601719-96ed-4bca-b925-6f8afb075ac3` |
| 55 | [`vacseffect`](https://data.gov.il/dataset/vacseffect) | תופעות לאחר חיסוני קורונה | PDF/XLSX · 3/7 DataStore | `0e804f1f-2b9e-4e97-8ac5-cefb6aecf730` |
| 56 | [`water-fabs-lists`](https://data.gov.il/dataset/water-fabs-lists) | רשימת מעבדות מים | XLSX · 1/1 DataStore | `318941c3-a2a3-489e-83d9-efb87ed01dc9` |

### Israel Water Authority
<a id="water_authority"></a>
**Slug:** `water_authority` · **Hebrew:** הרשות הממשלתית למים ולביוב · **Category:** Water · **Datasets:** 49

- Org page: https://data.gov.il/organization/water_authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:water_authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`6b1c032a-fdc1-4f92-bee1-14d6bf6af910`](https://data.gov.il/dataset/6b1c032a-fdc1-4f92-bee1-14d6bf6af910) | קידוחים מטוייבים | CSV · 1/1 DataStore | `6b1c032a-fdc1-4f92-bee1-14d6bf6af910` |
| 2 | [`acquifer`](https://data.gov.il/dataset/acquifer) | רשימת אקוויפרים | CSV · 1/1 DataStore | `01dd3a60-b536-49e8-8cc7-dffae2933ab5` |
| 3 | [`aquifer_level_history`](https://data.gov.il/dataset/aquifer_level_history) | מפלס מי תהום היסטורי | ZIP | — |
| 4 | [`basic_domes`](https://data.gov.il/dataset/basic_domes) | כמות מוכרת לבעלי רישיון אספקה החל משנת 2018 | CSV · 1/1 DataStore | `f6cbfff2-a7ba-4639-bd5d-b284651274e7` |
| 5 | [`beneficiary_recipients`](https://data.gov.il/dataset/beneficiary_recipients) | מקבלי הטבה לפי ספק | XLSX · 3/3 DataStore | `375a0352-081d-49e4-ab47-680ee917da45` |
| 6 | [`bor_depth`](https://data.gov.il/dataset/bor_depth) | עומק בקידוחים | CSV · 1/1 DataStore | `32df47bd-b4d0-4a55-b344-e59743aef9b0` |
| 7 | [`bor_perfor`](https://data.gov.il/dataset/bor_perfor) | רשימת מסננות בקידוחים | CSV · 1/1 DataStore | `82424fcd-eaf9-43a7-86a7-35a45c420f8a` |
| 8 | [`borehole_level`](https://data.gov.il/dataset/borehole_level) | מפלסי קידוחים | CSV · 2/2 DataStore | `f2d9436d-2352-442a-9d2e-10cd693c28d1` |
| 9 | [`borehole_quality_history`](https://data.gov.il/dataset/borehole_quality_history) | הסטוריית נתוני איכות מים בקידוחים | CSV · 9/9 DataStore | `0f1a5a02-ba94-4ad9-b011-33723256e23f` |
| 10 | [`borehole_refpoint`](https://data.gov.il/dataset/borehole_refpoint) | נקודת יחס אחרונה בקידוחים | CSV · 1/1 DataStore | `5bae3e98-2689-4f84-a3cc-f2412e2125d1` |
| 11 | [`borehole_wq_params`](https://data.gov.il/dataset/borehole_wq_params) | נתון אחרון - איכות מים בקידוחים | CSV · 1/1 DataStore | `61dd012f-0523-41b3-9c0e-ad4de7b3ce8c` |
| 12 | [`boreholes`](https://data.gov.il/dataset/boreholes) | קידוחי רשות המים | CSV · 1/1 DataStore | `71090141-46a0-42b7-aed8-c71322b25c6d` |
| 13 | [`cell_subbasin`](https://data.gov.il/dataset/cell_subbasin) | רשימת תאי דיווח | CSV · 1/1 DataStore | `10a4ef9c-35ab-43d8-bb80-5278e497a56e` |
| 14 | [`costalaquifer_rechrge`](https://data.gov.il/dataset/costalaquifer_rechrge) | סדרות העשרה לאקוויפר החוף | XLSX/ZIP · 2/3 DataStore | `f27d9310-cd41-4cf9-99b7-06aa0869bd47` |
| 15 | [`desalination`](https://data.gov.il/dataset/desalination) | כמויות מים ממתקני התפלה | CSV · 4/4 DataStore | `f4481461-0877-4be8-88b8-ee5a42ff3d00` |
| 16 | [`dynamic_wl_cl`](https://data.gov.il/dataset/dynamic_wl_cl) | מפות מפלסים ומליחות באקוויפרים השונים במדינת ישראל | ZIP · 4 files | — |
| 17 | [`effluent_recovery_projects`](https://data.gov.il/dataset/effluent_recovery_projects) | פרויקטים להקמת תשתיות השבת קולחים | XLSX · 1/1 DataStore | `1e66388e-415a-4acc-bf5d-bac426e3c74d` |
| 18 | [`geology_models`](https://data.gov.il/dataset/geology_models) | מודלים גיאולוגיים (סטרטיגרפיה וליתולוגיה) של תת הקרקע באגני מי התהום בישראל | ZIP · 9 files | — |
| 19 | [`hidrograph`](https://data.gov.il/dataset/hidrograph) | ספיקה רגעית בתחנות הידרומטריות - הידרוגרף | CSV · 4/4 DataStore | `8c513de9-a9b0-48f7-a893-ad0330b3c4fa` |
| 20 | [`hisoricalmaxdischarge`](https://data.gov.il/dataset/hisoricalmaxdischarge) | תחנות- ספיקות שיא היסטוריות | CSV · 1/1 DataStore | `d60e5849-5d6e-468c-afe0-cf5b5a2fb987` |
| 21 | [`https-www-data-gov-il-dataset-682`](https://data.gov.il/dataset/https-www-data-gov-il-dataset-682) | מפלס כנרת | CSV · 1/1 DataStore | `2de7b543-e13d-4e7e-b4c8-56071bc4d3c8` |
| 22 | [`https-www-data-gov-il-dataset-683`](https://data.gov.il/dataset/https-www-data-gov-il-dataset-683) | מפלס ים המלח | CSV · 1/1 DataStore | `823479b4-4771-43d8-9189-6a2a1dcaaf10` |
| 23 | [`hydro_station`](https://data.gov.il/dataset/hydro_station) | רשימת תחנות הידרומטריות | CSV · 1/1 DataStore | `a0522b41-00ad-4367-a00a-2d97b050ec1d` |
| 24 | [`jordan_hury_water_quality`](https://data.gov.il/dataset/jordan_hury_water_quality) | דוח תוצאות ניטור של איכות מים בנהר הירדן בתחנת גשר הפקק | CSV · 1/1 DataStore | `2d834439-3f88-45ef-bf6e-9924c2f7e8f9` |
| 25 | [`kinneret_cl`](https://data.gov.il/dataset/kinneret_cl) | נתוני כלוריד בכנרת | CSV · 1/1 DataStore | `b1d290c4-220b-494d-8376-0465789e972b` |
| 26 | [`level_discharge`](https://data.gov.il/dataset/level_discharge) | נפחים יומיים וספיקה יומית ממוצעת בתחנות | CSV · 8/8 DataStore | `bb596622-12f3-43bb-8730-cf7d5fb734e2` |
| 27 | [`lic_consumers`](https://data.gov.il/dataset/lic_consumers) | בעלי רישיונות רשות המים | CSV · 1/1 DataStore | `6e9f0bfa-5e87-4fb1-9fe4-1e523bf93fa8` |
| 28 | [`max_discharge_recurrence_periods`](https://data.gov.il/dataset/max_discharge_recurrence_periods) | ספיקות שיא מחושבות לתקופות חזרה שונות | PDF | — |
| 29 | [`maxdischarge_yearlyvolume`](https://data.gov.il/dataset/maxdischarge_yearlyvolume) | תחנות - ספיקות שיא ונפחים שנתיים | CSV · 1/1 DataStore | `fe88ac88-8c30-4b33-9ea8-ea6a050e0951` |
| 30 | [`mekorot_development_plan`](https://data.gov.il/dataset/mekorot_development_plan) | תכנית הפיתוח של חברת מקורות (מערכת מים ארצית) | XLSX | — |
| 31 | [`penetration`](https://data.gov.il/dataset/penetration) | החדרה בשנה הידרולוגית | CSV · 1/1 DataStore | `a72dea24-3865-4b70-98ee-4f6705b1e76a` |
| 32 | [`production`](https://data.gov.il/dataset/production) | הפקת מים בישראל | CSV · 1/1 DataStore | `dc69ead9-5510-407b-b16f-5293eaac8611` |
| 33 | [`qual_per_hydro_station`](https://data.gov.il/dataset/qual_per_hydro_station) | תחנות - דיגום איכות מים | CSV · 1/1 DataStore | `eea54e96-d51e-4def-b975-bd409eda7c64` |
| 34 | [`reservoirs`](https://data.gov.il/dataset/reservoirs) | מאגרי המים העיליים בישראל | CSV · 1/1 DataStore | `90bcf5e0-8a57-41f2-b67b-e2030fd6cdea` |
| 35 | [`runoff_recharge_prioritization_areas`](https://data.gov.il/dataset/runoff_recharge_prioritization_areas) | אזורי עדיפות להחדרה | PDF/ZIP · 2 files | — |
| 36 | [`sewage_budgeting`](https://data.gov.il/dataset/sewage_budgeting) | תקצוב ביצוע פרויקטים מבוצעים ע"י גופים זכאים לסיוע ממשלתי – מענקים והלוואות | XLSX | — |
| 37 | [`sewage_donor`](https://data.gov.il/dataset/sewage_donor) | תורמי ביוב | CSV · 1/1 DataStore | `746bd9f9-4a8e-4330-b8ad-8e71d45361ce` |
| 38 | [`sewage_infrastructure_projects`](https://data.gov.il/dataset/sewage_infrastructure_projects) | פרויקטים לביצוע תשתיות ביוב עירוניות, אזוריות ומט"שים | XLSX · 1/1 DataStore | `8f0e5d1c-d167-4592-aa2f-d8047936d783` |
| 39 | [`sewage_owners`](https://data.gov.il/dataset/sewage_owners) | רשימת מט"שים | CSV · 1/1 DataStore | `d7dacdf1-a16d-4272-90d0-52f152ae66b3` |
| 40 | [`special_populations`](https://data.gov.il/dataset/special_populations) | הטבה במים לאוכלוסיות מיוחדות | CSV · 1/1 DataStore | `9a93c1dc-7ea1-4cfc-a0a6-0127b6a84a9d` |
| 41 | [`spring_discharge`](https://data.gov.il/dataset/spring_discharge) | מעיינות - ספיקה מדודה | CSV · 1/1 DataStore | `26d650da-9d47-4dd5-8cbe-2f7d6955110b` |
| 42 | [`spring_monthly_volume`](https://data.gov.il/dataset/spring_monthly_volume) | מעיינות - נפחים חודשיים | CSV · 1/1 DataStore | `b09e2524-daa4-4ba6-8658-d76860d7bc60` |
| 43 | [`spring_quality`](https://data.gov.il/dataset/spring_quality) | מדידות איכות במעיינות | CSV · 1/1 DataStore | `63e978d1-51e0-4f24-94cb-fc8396d961ab` |
| 44 | [`spring_yearly_volume`](https://data.gov.il/dataset/spring_yearly_volume) | מעיינות - נפחים שנתיים | CSV · 1/1 DataStore | `09e057c4-d7dc-485a-bfcf-aeed674f7a36` |
| 45 | [`springs`](https://data.gov.il/dataset/springs) | דוח קטלוג מעיינות | CSV · 1/1 DataStore | `e0f10edd-2780-4221-97dc-3ac9d2f62cd0` |
| 46 | [`streams`](https://data.gov.il/dataset/streams) | נתונים קבועים של נחלים בישראל | CSV · 1/1 DataStore | `b6b421ce-c8ad-4582-bdf2-765b5fb4fed5` |
| 47 | [`treated_waste_cons`](https://data.gov.il/dataset/treated_waste_cons) | צרכני קולחין | CSV · 1/1 DataStore | `613885d9-d9ba-454d-89c3-3133d0855e05` |
| 48 | [`water_factory`](https://data.gov.il/dataset/water_factory) | מכוני מים בישראל | CSV · 1/1 DataStore | `412d4161-4130-4294-88ed-967f88923632` |
| 49 | [`western_galilee_geology`](https://data.gov.il/dataset/western_galilee_geology) | מודל סטרטיגרפי - גליל מערבי, שכבות חבורת יהודה | ZIP · 3 files | — |

### Be'er Sheva Municipality
<a id="beer-sheva"></a>
**Slug:** `beer-sheva` · **Hebrew:** עיריית באר שבע · **Category:** Municipal · **Datasets:** 44

- Org page: https://data.gov.il/organization/beer-sheva
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:beer-sheva&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`addresses-br7`](https://data.gov.il/dataset/addresses-br7) | מספרי בתים ושמות הרחובות | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/16 DataStore | `66755b06-bf71-4e4e-989b-e6ee98cffb68` |
| 2 | [`beer-sheva-municipality-budget-7`](https://data.gov.il/dataset/beer-sheva-municipality-budget-7) | תקציב עיריית באר-שבע | CSV/JSON/XLSX/XML · 10/20 DataStore | `2d66eb8f-a3cd-45c8-8cfe-39f48d833e72` |
| 3 | [`bicycle_track-br7`](https://data.gov.il/dataset/bicycle_track-br7) | שבילי אופניים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `f81bd6b4-de24-4c89-b3da-4c52c4d2a37b` |
| 4 | [`bicycles-parking-br7`](https://data.gov.il/dataset/bicycles-parking-br7) | מתקני עגינת אופניים בבאר-שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `bbfc918c-21d5-4084-860f-3f01f31bb9d4` |
| 5 | [`br7-zoning`](https://data.gov.il/dataset/br7-zoning) | ייעודי קרקע | CSV/GEOJSON/JPEG/KML/XLSX/XML/ZIP · 2/10 DataStore | `60bedb3c-1520-4475-86a1-44de38f9d284` |
| 6 | [`buildings-br7`](https://data.gov.il/dataset/buildings-br7) | מבנים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `676cfeb1-d257-4870-9d93-26c1aeced98b` |
| 7 | [`buildings-preservation-br7`](https://data.gov.il/dataset/buildings-preservation-br7) | מבנים לשימור | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 16/60 DataStore | `6b01d4ce-5f08-4a2b-82f8-10e0faa3283b` |
| 8 | [`business-licensing-br7`](https://data.gov.il/dataset/business-licensing-br7) | רישוי עסקים | CSV/JSON/XLSX/XML · 2/4 DataStore | `7d4c61e2-2416-453e-8efb-bd02ec89db35` |
| 9 | [`businesscenters-br7`](https://data.gov.il/dataset/businesscenters-br7) | מתחמי מרכזים מסחריים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `3c5f8d70-b04d-49e0-acb8-e56231ef9d26` |
| 10 | [`cameras-br7`](https://data.gov.il/dataset/cameras-br7) | מצלמות אבטחה באר-שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `3c7e0a98-312e-476a-8083-877773400137` |
| 11 | [`city-plans-br7`](https://data.gov.il/dataset/city-plans-br7) | תכניות בניין עיר (תב"עות) | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `201436f4-5699-494e-a67d-efe8acfd19fc` |
| 12 | [`community-centers-br7`](https://data.gov.il/dataset/community-centers-br7) | מרכזים קהילתיים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `8e08e632-a903-4f85-9260-f145ab2530e7` |
| 13 | [`daycares-br7`](https://data.gov.il/dataset/daycares-br7) | מעונות יום | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `8a9c6e64-fda8-499c-887c-4e7b3eb82332` |
| 14 | [`defi`](https://data.gov.il/dataset/defi) | איפה דפי - מיפוי דפיברילטורים חברתי | CSV/GEOJSON · 1/2 DataStore | `3f60d2fa-ca4c-49b7-84b2-34ddf1cf9206` |
| 15 | [`demand_survey_2019-br7`](https://data.gov.il/dataset/demand_survey_2019-br7) | סקר ביקושים לעסקים 2019 | CSV/JSON/XLSX/XML · 2/4 DataStore | `d245414c-5231-4e86-a9d9-d2cf724b4be0` |
| 16 | [`demographics-br7`](https://data.gov.il/dataset/demographics-br7) | מרשם אוכלוסין | CSV/JSON/XLSX/XML · 5/12 DataStore | `b6ee8e0f-b16e-4b66-b258-7714bd40440f` |
| 17 | [`dog-gardens-br7`](https://data.gov.il/dataset/dog-gardens-br7) | גינות כלבים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `4b6e3408-afbe-4ea3-8b69-11d98233ffe7` |
| 18 | [`education-br7`](https://data.gov.il/dataset/education-br7) | מבני חינוך | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `97eaf0c4-fd2e-4d9c-bb6d-6e34a83049d0` |
| 19 | [`elderly-social-clubs-br7`](https://data.gov.il/dataset/elderly-social-clubs-br7) | מועדונים חברתיים לקשיש | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 3/15 DataStore | `68a292ca-0647-472e-9900-695293d819e1` |
| 20 | [`fire_hydrants-br7`](https://data.gov.il/dataset/fire_hydrants-br7) | ברזי כיבוי אש (הידרנטים) | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `0a3c2907-f093-4821-876c-6e8034eb53e4` |
| 21 | [`garbage-bins-br7`](https://data.gov.il/dataset/garbage-bins-br7) | פחי אשפה טמונים (טמוני קרקע) | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `53271cdd-4efb-4554-91b3-a3fa54fbc25f` |
| 22 | [`gas-stations-br7`](https://data.gov.il/dataset/gas-stations-br7) | תחנות דלק | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 3/15 DataStore | `c595a623-cbd1-45d8-9308-3fd71dfd7a5c` |
| 23 | [`gis_shiput-br7`](https://data.gov.il/dataset/gis_shiput-br7) | שכבת שטח השיפוט המוניציפלי | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 5/15 DataStore | `0bb7256a-6b60-4c38-95ed-3fdd8f724e27` |
| 24 | [`health-br7`](https://data.gov.il/dataset/health-br7) | מרכזי בריאות | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 6/19 DataStore | `e9195086-fea3-4be4-ad50-026b9d48e1be` |
| 25 | [`jobs-br7`](https://data.gov.il/dataset/jobs-br7) | דרושים | CSV/JSON/XLSX/XML · 2/4 DataStore | `1afa2973-2d77-480b-855f-7703f94a783c` |
| 26 | [`light-traffics-br7`](https://data.gov.il/dataset/light-traffics-br7) | רמזורים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `289eb9f6-93c9-4add-b96f-99ffa88c5a55` |
| 27 | [`mizrakot_maim-br7`](https://data.gov.il/dataset/mizrakot_maim-br7) | מזרקות העיר | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `49c7aa6d-ef48-419d-8d5f-03aea139f94d` |
| 28 | [`pharmacy-duty-br7`](https://data.gov.il/dataset/pharmacy-duty-br7) | תורנות בתי מרקחת | CSV/JSON/XLSX/XML · 2/4 DataStore | `edf3a5f6-713c-4166-ad75-427f47496e39` |
| 29 | [`playground-datagov-br7`](https://data.gov.il/dataset/playground-datagov-br7) | מתקני משחקים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `64129aff-845c-4792-a479-1792c1ab9b0a` |
| 30 | [`roads-br7`](https://data.gov.il/dataset/roads-br7) | דרכים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `a50b5e05-970c-4847-a18b-ec446f2c9642` |
| 31 | [`shelters-br7`](https://data.gov.il/dataset/shelters-br7) | מקלטים בעיר באר שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `6ab1c602-873c-4c1f-b046-60505af1bacd` |
| 32 | [`sirens-br7`](https://data.gov.il/dataset/sirens-br7) | צופרים בעיר באר שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `a37d0e59-af78-4e8c-b580-43a85f242468` |
| 33 | [`sport-br7`](https://data.gov.il/dataset/sport-br7) | מתקני ספורט בבאר-שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `ac12e904-be38-4011-9306-bc4820eb7f41` |
| 34 | [`startups-br7`](https://data.gov.il/dataset/startups-br7) | סטארט-אפים מהדרום 2017 | CSV/JSON/XLSX/XML · 2/4 DataStore | `57e8792e-dccf-4fb5-8f2a-30bcad896e83` |
| 35 | [`stat_n-hoods_table-br7`](https://data.gov.il/dataset/stat_n-hoods_table-br7) | טבלת המרה שכונות - אזורים סטטיסטיים | XLSX · 1/1 DataStore | `dac7a88f-d627-46be-93e8-4901ac8242fb` |
| 36 | [`street-light-br7`](https://data.gov.il/dataset/street-light-br7) | עמודי תאורה | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 5/16 DataStore | `e40306c7-ee78-4c93-82e8-65d747e80865` |
| 37 | [`streets-of-the-city-br7`](https://data.gov.il/dataset/streets-of-the-city-br7) | שמות הרחובות בעיר | CSV/JSON/XLSX/XML · 2/4 DataStore | `84fb7cca-7643-4438-bcc2-d4144ad7f95f` |
| 38 | [`synagogues-br7`](https://data.gov.il/dataset/synagogues-br7) | בתי כנסת בעיר באר-שבע | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `40de91c6-1eb3-4f12-9cea-5c44484377d7` |
| 39 | [`tavsagol-br7`](https://data.gov.il/dataset/tavsagol-br7) | התו הסגול | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `9aa90ee8-2c88-4b98-9448-233de0dba6b3` |
| 40 | [`taxi-stations-br7`](https://data.gov.il/dataset/taxi-stations-br7) | תחנות מוניות | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `a323d256-e6fe-4804-a4ff-f2b87289cb53` |
| 41 | [`tender-br7`](https://data.gov.il/dataset/tender-br7) | מכרזים בעיר באר שבע | CSV/JSON/XLSX/XML · 2/4 DataStore | `6a281768-6327-420b-a1c5-fb84af1fa8ae` |
| 42 | [`trees-br7`](https://data.gov.il/dataset/trees-br7) | עצים | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `b7bfe395-a977-452a-8429-e258b71c5b10` |
| 43 | [`unified_businesses-br7`](https://data.gov.il/dataset/unified_businesses-br7) | מאגר עסקים קולטי קהל | CSV/JSON/XLSX/XML · 2/4 DataStore | `5f4f8927-b890-42ed-bb25-58d48b5f180f` |
| 44 | [`urban-nature-br7`](https://data.gov.il/dataset/urban-nature-br7) | אתרי טבע עירוני | CSV/GEOJSON/JSON/KML/XLSX/XML/ZIP · 4/15 DataStore | `e68db127-f8a1-4a05-845c-e1c82c2bacc3` |

### Ministry of Welfare & Social Affairs
<a id="ministry_of_social_affairs"></a>
**Slug:** `ministry_of_social_affairs` · **Hebrew:** משרד הרווחה והביטחון החברתי · **Category:** Welfare · **Datasets:** 40

- Org page: https://data.gov.il/organization/ministry_of_social_affairs
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_social_affairs&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`applying-to-social-services-departments`](https://data.gov.il/dataset/applying-to-social-services-departments) | מאגר נתוני יסוד | CSV/PDF · 7/14 DataStore | `b6dcbb4c-4102-43d2-a5a1-8e049457fe7a` |
| 2 | [`assistance-and-intervention`](https://data.gov.il/dataset/assistance-and-intervention) | תיק התערבות | CSV/PDF · 4/5 DataStore | `3b5313f3-af65-4c77-8a2a-4dacb1cd368e` |
| 3 | [`children-investigation`](https://data.gov.il/dataset/children-investigation) | חקירות ילדים | CSV/PDF · 2/3 DataStore | `47c4c100-c549-4882-8021-8f36541893d7` |
| 4 | [`court_specialists`](https://data.gov.il/dataset/court_specialists) | רשימת מומחים לבתי משפט | CSV/PDF · 1/2 DataStore | `ebe7b0fa-42c8-4195-8b40-b0b0e73cc494` |
| 5 | [`defensecenters`](https://data.gov.il/dataset/defensecenters) | מרכזי הגנה לנפגעי תקיפה מינית או אלימות | CSV/PDF · 1/2 DataStore | `288c4eeb-7883-4941-9265-714c2feb2d66` |
| 6 | [`disabilities-centers`](https://data.gov.il/dataset/disabilities-centers) | מרכזי אבחון לאנשים עם מוגבלות שכלית התפתחותית | CSV/PDF · 1/2 DataStore | `6b0a3096-969d-4a9f-8d98-4ebd04033f9f` |
| 7 | [`disabilities-centers-ar`](https://data.gov.il/dataset/disabilities-centers-ar) | מרכזי אבחון לאנשים עם מוגבלות שכלית התפתחותית مراكز التشخيص للأشخاص ذوي الإعاقة العقلية والتطورية | XLSX · 1/1 DataStore | `d27652b3-ef30-44f8-811d-8f720ebfa00b` |
| 8 | [`familycenters`](https://data.gov.il/dataset/familycenters) | מרכזים למשפחות לילדים עם מוגבלות | CSV/PDF · 1/2 DataStore | `e02335b2-3297-486c-a9e0-92794336529b` |
| 9 | [`molsa-addictions-treatment-frames`](https://data.gov.il/dataset/molsa-addictions-treatment-frames) | מסגרות לטיפול בהתמכרויות | CSV/PDF · 1/2 DataStore | `cb68a64a-a0d5-4f08-a2a5-75ce95d880a6` |
| 10 | [`molsa-addictions-treatment-frames-ar`](https://data.gov.il/dataset/molsa-addictions-treatment-frames-ar) | מסגרות לטיפול בהתמכרויות وحدات علاج البالغين ضحايا الإدمان | PDF/XLS · 1/2 DataStore | `e8e490c8-6951-4621-ba2c-b3068e3fb09c` |
| 11 | [`molsa-court-assiatance-units`](https://data.gov.il/dataset/molsa-court-assiatance-units) | יחידות הסיוע | CSV/PDF · 4/5 DataStore | `5192821d-0de7-4c72-9929-5413f0b9fd08` |
| 12 | [`molsa-homeless-units`](https://data.gov.il/dataset/molsa-homeless-units) | דרי רחוב - יחידות | CSV/PDF · 1/2 DataStore | `112378c8-3d0c-41b3-bb2c-c3761622d723` |
| 13 | [`molsa-homeless-units-ar`](https://data.gov.il/dataset/molsa-homeless-units-ar) | דרי רחוב - יחידות مراكز الخدمة للمشردين | XLSX · 1/1 DataStore | `82fa6941-910a-4e2b-a37d-6fe109fb93d9` |
| 14 | [`molsa-outerhomes-elderly-ar`](https://data.gov.il/dataset/molsa-outerhomes-elderly-ar) | רשימת בתי אבות بيوت المسنين | PDF/XLSX · 1/2 DataStore | `68787d48-3ca8-48d5-ab25-75890d5535ed` |
| 15 | [`molsa-outerhomes-elderly-vacation`](https://data.gov.il/dataset/molsa-outerhomes-elderly-vacation) | נופשונים לאזרחים ותיקים | PDF/XLSX · 1/2 DataStore | `d1f41850-0cae-47bc-9c32-ae80e0ed0994` |
| 16 | [`molsa-outerhomes-elderly-vacation-ar`](https://data.gov.il/dataset/molsa-outerhomes-elderly-vacation-ar) | נופשונים לאזרחים ותיקים أطر الإسكان المؤقت للمواطنين المسنين | PDF/XLSX · 1/2 DataStore | `7255103c-6f5b-435b-9aa4-2ecbcfc57bc2` |
| 17 | [`molsa-populations-divorce-expert-ar`](https://data.gov.il/dataset/molsa-populations-divorce-expert-ar) | רשימת מומחים לבתי משפט قائمة خبراء محكمة شؤون الأسرة (العائلة) | PDF/XLSX · 1/2 DataStore | `cffc8d26-38f8-41d3-8705-d1f1f16212de` |
| 18 | [`molsa-protected-houses-list-ar`](https://data.gov.il/dataset/molsa-protected-houses-list-ar) | בתי דיור מוגן بيوت الإسكان المحمي | PDF/XLSX · 1/2 DataStore | `7f3b5887-bacd-4f49-b220-4cae2a417cdb` |
| 19 | [`molsa-social-and-welfare-magazin-publications`](https://data.gov.il/dataset/molsa-social-and-welfare-magazin-publications) | כתב העת חברה ורווחה | CSV/PDF · 1/2 DataStore | `091db2ee-cc23-4c94-b5ba-a4c2eb06dd5d` |
| 20 | [`molsa-social-departmentsd-list-ar`](https://data.gov.il/dataset/molsa-social-departmentsd-list-ar) | המחלקות לשירותים חברתיים أقسام الخدمات الاجتماعية | PDF/XLSX · 1/2 DataStore | `ff5a820a-eae2-460e-8800-7cd64d38bc08` |
| 21 | [`molsa-social-sorkers-abroainstitutes`](https://data.gov.il/dataset/molsa-social-sorkers-abroainstitutes) | מוסדות ותכניות לימודי עבודה סוציאלית בחו"ל | XLSX · 7/7 DataStore | `5be1db4c-7fe8-4d07-9bd3-57d34901f2b2` |
| 22 | [`molsa-units-adult-probation-service`](https://data.gov.il/dataset/molsa-units-adult-probation-service) | שירות המבחן למבוגרים | CSV/PDF · 12/13 DataStore | `b6869d0d-c08d-4ef8-a9ec-6e511c2369d7` |
| 23 | [`molsa-volunteering-coordinators`](https://data.gov.il/dataset/molsa-volunteering-coordinators) | רכזי ההתנדבות ברשויות המקומיות | CSV/PDF · 1/2 DataStore | `1c00198b-0e63-4cef-8e25-2aa345f069f8` |
| 24 | [`noshmim-lervacha`](https://data.gov.il/dataset/noshmim-lervacha) | נושמים לרווחה | CSV/PDF · 7/8 DataStore | `8cd4279a-397a-49af-a98c-996d965f32f5` |
| 25 | [`outerhomes-homeless-ar`](https://data.gov.il/dataset/outerhomes-homeless-ar) | דרי רחוב - מרכזי שירות مراكز الخدمة للمشردين | CSV · 1/1 DataStore | `41edf481-96a4-4317-bf88-86c3e186fc79` |
| 26 | [`outerhomes_homeless`](https://data.gov.il/dataset/outerhomes_homeless) | דרי רחוב - מרכזי שירות | CSV/PDF · 1/2 DataStore | `03166af6-23f3-4491-8ec0-cbd13bea84dd` |
| 27 | [`payments-to-welfare-frameworks`](https://data.gov.il/dataset/payments-to-welfare-frameworks) | מאגר תשלומים | CSV/PDF · 10/14 DataStore | `1a2e0815-b381-4ed8-a1c2-8fb35f3d94d7` |
| 28 | [`people-with-blindness-and-visual-impairment`](https://data.gov.il/dataset/people-with-blindness-and-visual-impairment) | אנשים עם עיוורון ולקות ראייה | CSV/PDF · 3/8 DataStore | `87cd15c6-8e3f-4ad4-87f7-e4b004a3115c` |
| 29 | [`people-with-deafness-and-hearing-impairments`](https://data.gov.il/dataset/people-with-deafness-and-hearing-impairments) | אנשים חירשים וכבדי שמיעה | CSV/PDF · 1/3 DataStore | `8ba2c9c0-94a5-46d0-a707-5b0bcad29567` |
| 30 | [`personnel-welfare-authorities`](https://data.gov.il/dataset/personnel-welfare-authorities) | מאגר כוח אדם ברשויות הרווחה | CSV/PDF · 1/2 DataStore | `e3bfbd23-ca72-4359-a095-4e40757eea65` |
| 31 | [`protectedhouseslist`](https://data.gov.il/dataset/protectedhouseslist) | בתי דיור מוגן | CSV/PDF · 1/2 DataStore | `7c390473-42b8-4fd2-a72d-07fa126ffeee` |
| 32 | [`sherut-mivhan-lanoar`](https://data.gov.il/dataset/sherut-mivhan-lanoar) | שירות המבחן לנוער | CSV/PDF · 13/14 DataStore | `806f7b05-c14c-4468-ae9f-a4cbcd3743d8` |
| 33 | [`shil-leshachot`](https://data.gov.il/dataset/shil-leshachot) | תחנות שי"ל (שירות ייעוץ לאזרח) | XLSX · 1/1 DataStore | `1687655a-79ac-4858-bb35-dac71377b2e0` |
| 34 | [`social-departments`](https://data.gov.il/dataset/social-departments) | המחלקות לשירותים חברתיים | CSV/PDF · 1/2 DataStore | `8213a3be-c367-4c2f-a123-385be6fd66da` |
| 35 | [`social-sorkers-abroainstitutes-ar`](https://data.gov.il/dataset/social-sorkers-abroainstitutes-ar) | مؤسسات دراسة برامج العمل الاجتماعي في الخارج - מוסדות ותכניות לימודי עבודה סוציאלית בחו"ל (ערבית) | XLSX · 1/1 DataStore | `8b368153-956f-40ae-a4ba-665a6d5af63a` |
| 36 | [`social-work-study-institutions-and-programs-abroad`](https://data.gov.il/dataset/social-work-study-institutions-and-programs-abroad) | Social work study institutions and programs abroad מוסדות ותכניות לימודי עבודה סוציאלית בחו"ל | XLSX · 1/1 DataStore | `1d950706-2099-4f33-9b47-693ca84aa85e` |
| 37 | [`social-workers-registration`](https://data.gov.il/dataset/social-workers-registration) | פנקס העובדים הסוציאליים | CSV/PDF · 1/2 DataStore | `0f25d8f5-eecc-4d63-8914-38d59f19925b` |
| 38 | [`society-and-welfare-journal`](https://data.gov.il/dataset/society-and-welfare-journal) | כתב העת חברה ורווחה - Society and Welfare journal | CSV/PDF · 1/2 DataStore | `3058868b-9138-4aeb-bfb9-020cf823ddeb` |
| 39 | [`welfare-frames`](https://data.gov.il/dataset/welfare-frames) | מסגרות הרווחה שבפיקוח משרד הרווחה והביטחון החברתי | CSV/PDF · 1/2 DataStore | `de069ddf-bcbc-4754-bda0-84873a353f7b` |
| 40 | [`yated2022`](https://data.gov.il/dataset/yated2022) | תוכנית יתד במשרד הרווחה | CSV/PDF · 4/5 DataStore | `71af5b5c-0233-4bcc-9778-f30c73cdbc59` |

### Ministry of Culture & Sport
<a id="culture_and_sports"></a>
**Slug:** `culture_and_sports` · **Hebrew:** משרד התרבות והספורט · **Category:** Culture · **Datasets:** 32

- Org page: https://data.gov.il/organization/culture_and_sports
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:culture_and_sports&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`408`](https://data.gov.il/dataset/408) | מתקני ספורט בישראל | CSV/XLSX · 2/2 DataStore | `f8dbd3ed-2c62-4d0e-bbaa-b6a15a0e5f7d` |
| 2 | [`502`](https://data.gov.il/dataset/502) | רשימת מרכזי צלילה | CSV · 1/1 DataStore | `c2093eeb-6139-4ad3-9f9f-26d11d708549` |
| 3 | [`502-2`](https://data.gov.il/dataset/502-2) | רשימת מרכזי צלילה באילת | CSV · 1/1 DataStore | `8efa5992-db41-40ba-ab86-05dad100e593` |
| 4 | [`503`](https://data.gov.il/dataset/503) | פריטים מוזאליים | ? | — |
| 5 | [`504`](https://data.gov.il/dataset/504) | סרטים | ? · 2 files | — |
| 6 | [`506-1`](https://data.gov.il/dataset/506-1) | רשימת בוחנים בתחום מכוניות - נהיגה ספורטיבית | XLSX | — |
| 7 | [`506-2`](https://data.gov.il/dataset/506-2) | רשימת בוחנים בתחום אופנועים וטרקטורונים - נהיגה ספורטיבית | XLSX · 1/1 DataStore | `fe6734f9-c120-4387-91f8-b42ba9aae68a` |
| 8 | [`508`](https://data.gov.il/dataset/508) | דרגות רישיון נהיגה ספורטיבית | CSV · 1/1 DataStore | `4b947b0a-811c-472e-9e16-637202a80f50` |
| 9 | [`510`](https://data.gov.il/dataset/510) | מוזאונים מוכרים | XLSX · 1/1 DataStore | `0309ee10-21a0-4ee9-8094-8fb474ca208a` |
| 10 | [`517`](https://data.gov.il/dataset/517) | רשימת הקורסים והמוסדות המאושרים על פי החוק | XLSX · 1/1 DataStore | `d879e91b-419a-4e63-8e20-2ff798a234c1` |
| 11 | [`518`](https://data.gov.il/dataset/518) | מידעונים למוסדות הכשרה | CSV · 1/1 DataStore | `16448c01-61a2-4c62-9273-42ff9b4d3ec1` |
| 12 | [`519`](https://data.gov.il/dataset/519) | תוכניות לימודית להכשרת מדריכים | ?/CSV · 1/2 DataStore | `e90b6ff7-53fb-4379-b0df-5c63fdc1af80` |
| 13 | [`520`](https://data.gov.il/dataset/520) | תוכניות לימודית להכשרת מאמנים | CSV · 1/1 DataStore | `5212bf7c-e866-48b7-9357-8f6e51d273c1` |
| 14 | [`521`](https://data.gov.il/dataset/521) | הכשרת מאמנים - ענפי קרב מוכרים | CSV · 1/1 DataStore | `7e2c3301-6190-466d-babc-bf5efb5c7ef9` |
| 15 | [`532`](https://data.gov.il/dataset/532) | סל הספורט - מנהלי מחלקות ספורט ברשויות המקומיות | CSV | — |
| 16 | [`535`](https://data.gov.il/dataset/535) | סל הספורט - סוגי מתקנים | CSV · 1/1 DataStore | `228ea2d3-c8ce-4e12-ba80-047bdb8518b5` |
| 17 | [`536`](https://data.gov.il/dataset/536) | ספורט הישגי - גיל ספורטאים פעילים בענפי הספורט | CSV | — |
| 18 | [`538-1`](https://data.gov.il/dataset/538-1) | נהיגה ספורטיבית - מחירי אגרות רישוי כלי תחרותי | XLSX | — |
| 19 | [`541`](https://data.gov.il/dataset/541) | מוזאונים - רשימת מומחי שימור | CSV | — |
| 20 | [`551`](https://data.gov.il/dataset/551) | המועצה לספריות ציבוריות - חברי המועצה | CSV · 1/1 DataStore | `f95f4729-31e4-4206-ba8f-90dff42ab956` |
| 21 | [`552`](https://data.gov.il/dataset/552) | המועצה הישראלית לקולנוע - חברי מועצה | CSV | — |
| 22 | [`558`](https://data.gov.il/dataset/558) | המועצה למניעת אלימות בספורט - חברי מועצה | CSV · 1/1 DataStore | `3e657d72-028f-4873-847f-8ad1e0d98c75` |
| 23 | [`559`](https://data.gov.il/dataset/559) | המועצה לקידום ספורט נשים - חברי מועצה | CSV · 1/1 DataStore | `2bef8f8b-6f85-4011-9db3-426f5809762f` |
| 24 | [`566`](https://data.gov.il/dataset/566) | מאגר יועצים משפטיים | CSV · 1/1 DataStore | `bd249845-aacf-451c-a576-fd41f28bdd21` |
| 25 | [`568`](https://data.gov.il/dataset/568) | נהיגה ספורטיבית - מחירי אגרות רישוי לנהג | XLSX · 1/1 DataStore | `2326052f-46c9-404b-9f3a-585e85bdb13d` |
| 26 | [`609`](https://data.gov.il/dataset/609) | התאחדויות נהיגה ספורטיבית | ? | — |
| 27 | [`642`](https://data.gov.il/dataset/642) | ספריות - רשימת הספריות הציבוריות | CSV · 1/1 DataStore | `daea8017-f845-49db-ac7b-7823bf9a4135` |
| 28 | [`643`](https://data.gov.il/dataset/643) | המועצה לביקורת סרטים - חברי מועצה | CSV | — |
| 29 | [`650`](https://data.gov.il/dataset/650) | המועצה לביקורת סרטים - סיווג גיל לסרטי קולנוע | CSV · 1/1 DataStore | `e3efaeee-e066-4ac5-80c9-c58c3dae8ff1` |
| 30 | [`igudim_2024`](https://data.gov.il/dataset/igudim_2024) | מודל איגודים מאושר לשנת 2024 – קובץ לפרסום להערות הציבור | CSV · 1/1 DataStore | `851a1e2c-0e74-485a-a70d-9d6dd001a9f9` |
| 31 | [`most-537`](https://data.gov.il/dataset/most-537) | נהיגה ספורטיבית - כללים לאירוע נהיגה ספורטיבית | CSV · 1/1 DataStore | `9c82b7c1-f7c1-46bd-ac6c-afe2934b8297` |
| 32 | [`my-dataset5`](https://data.gov.il/dataset/my-dataset5) | מאמנים - ענפים, דרגות ותחומים | XLSX · 1/1 DataStore | `7a05d4e6-25be-4a71-996b-5c5a03010cfa` |

### Bank of Israel
<a id="bank_israel"></a>
**Slug:** `bank_israel` · **Hebrew:** בנק ישראל · **Category:** Finance · **Datasets:** 30

- Org page: https://data.gov.il/organization/bank_israel
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:bank_israel&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`348`](https://data.gov.il/dataset/348) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 1977 - 1981 | XLS | — |
| 2 | [`350`](https://data.gov.il/dataset/350) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 1982 - 1986 | ZIP | — |
| 3 | [`351`](https://data.gov.il/dataset/351) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 1987 - 1991 | ZIP | — |
| 4 | [`352`](https://data.gov.il/dataset/352) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 1992 - 1996 | ZIP | — |
| 5 | [`353`](https://data.gov.il/dataset/353) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 1997 - 2000 | ZIP | — |
| 6 | [`354new`](https://data.gov.il/dataset/354new) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 2001 - 2006 | ZIP | — |
| 7 | [`355new`](https://data.gov.il/dataset/355new) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 2007 - 2012 | ZIP | — |
| 8 | [`356`](https://data.gov.il/dataset/356) | שערים ממוצעים לכל המטבעות היציגים - 2012 | XLS | — |
| 9 | [`357`](https://data.gov.il/dataset/357) | שערים ממוצעים לכל המטבעות היציגים - 2011 פרטי המאגר | XLS | — |
| 10 | [`358`](https://data.gov.il/dataset/358) | שערים ממוצעים לכל המטבעות היציגים - 2010 | XLS | — |
| 11 | [`360`](https://data.gov.il/dataset/360) | שערים ממוצעים לכל המטבעות היציגים - 2008 | XLS | — |
| 12 | [`361`](https://data.gov.il/dataset/361) | שערים ממוצעים לכל המטבעות היציגים - 2007 | XLS | — |
| 13 | [`362`](https://data.gov.il/dataset/362) | שערים ממוצעים לכל המטבעות היציגים - 2006 | XLS · 1/1 DataStore | `4811a303-97a1-404a-b6d5-01726001870b` |
| 14 | [`363`](https://data.gov.il/dataset/363) | שערים ממוצעים לכל המטבעות היציגים - 2005 | XLS | — |
| 15 | [`364`](https://data.gov.il/dataset/364) | שערים ממוצעים לכל המטבעות היציגים - 2004 | XLS | — |
| 16 | [`365`](https://data.gov.il/dataset/365) | שערים ממוצעים לכל המטבעות היציגים - 2003 | XLS | — |
| 17 | [`366`](https://data.gov.il/dataset/366) | שערים ממוצעים לכל המטבעות היציגים - 2002 | XLS | — |
| 18 | [`367`](https://data.gov.il/dataset/367) | שערים ממוצעים לכל המטבעות היציגים - 2001 | XLS | — |
| 19 | [`371`](https://data.gov.il/dataset/371) | הריבית הממוצעת על משכנתאות צמודות למדד ומחשבון לחישוב עמלת פירעון מוקדם | XLS · 1/1 DataStore | `96ba107d-cc15-41cf-b223-5bb592e14666` |
| 20 | [`374`](https://data.gov.il/dataset/374) | הריבית הקבועה הממוצעת על משכנתאות במיגזר השיקלי הלא-צמוד | XLS | — |
| 21 | [`375`](https://data.gov.il/dataset/375) | רשימת תאגידים בנקאיים בישראל - כתובות וקישורים | CSV · 2/2 DataStore | `ebb61778-e34c-4e67-8fcf-0e643d9cf8c2` |
| 22 | [`377`](https://data.gov.il/dataset/377) | קובץ חשבונות מוגבלים של תאגידים | PDF/ZIP · 2 files | — |
| 23 | [`379`](https://data.gov.il/dataset/379) | נתונים חודשיים ושיעורי שינוי במדד המשולב | PDF/XLS · 2 files | — |
| 24 | [`381`](https://data.gov.il/dataset/381) | תשואות לפדיון על מק"מ | ? | — |
| 25 | [`651`](https://data.gov.il/dataset/651) | שערי חליפין בקובץ XML | XML | — |
| 26 | [`652`](https://data.gov.il/dataset/652) | שערי חליפין יציגים ל- 24 מטבעות, כולל סל המטבעות (נתונים יומיים) 2013 ואילך | XLS · 1/1 DataStore | `626dc624-277d-4c06-9efe-d282adfabb28` |
| 27 | [`653`](https://data.gov.il/dataset/653) | שערים ממוצעים לכל המטבעות היציגים - 2013 | XLS | — |
| 28 | [`automated-devices`](https://data.gov.il/dataset/automated-devices) | מכשירים אוטומטיים – ATMs | CSV · 1/1 DataStore | `21fde05f-62e3-401b-81cf-5c385862026d` |
| 29 | [`branches`](https://data.gov.il/dataset/branches) | סניפים בנקים | CSV · 2/2 DataStore | `2202bada-4baf-45f5-aa61-8c5bad9646d3` |
| 30 | [`branches_for_payments`](https://data.gov.il/dataset/branches_for_payments) | סניפים לסליקה | CSV · 2/2 DataStore | `b3f7616d-1c65-497d-afd5-d5ba972bfc1d` |

### Ministry of Innovation, Science & Technology
<a id="science-and-technology"></a>
**Slug:** `science-and-technology` · **Hebrew:** משרד החדשנות, המדע והטכנולוגיה · **Category:** Science · **Datasets:** 29

- Org page: https://data.gov.il/organization/science-and-technology
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:science-and-technology&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`02`](https://data.gov.il/dataset/02) | מחקרים ממומנים | CSV · 1/1 DataStore | `5a99a36e-1222-4ca9-b881-37409c67fd79` |
| 2 | [`03`](https://data.gov.il/dataset/03) | ארגונים בינלאומיים בתחום המדע שבהם נציגות ישראלית | XLSX · 1/1 DataStore | `5ac4b32b-f67b-46ff-a936-8916cc5292c2` |
| 3 | [`04`](https://data.gov.il/dataset/04) | הסכמי שיתוף פעולה בינלאומיים בתחום המדע | CSV · 1/1 DataStore | `96c792d5-d33c-472d-8bf3-ef6d59dfc4c8` |
| 4 | [`05`](https://data.gov.il/dataset/05) | מדינות עימן חתמה ישראל על הסכמי שיתוף פעולה מדעי דו-לאומי | XLSX · 1/1 DataStore | `e78841f7-aeb5-413a-a609-5842897f9b0a` |
| 5 | [`06`](https://data.gov.il/dataset/06) | חברי המועצה לקידום נשים במדע ובטכנולוגיה | XLSX · 1/1 DataStore | `c9ae96f3-1cbe-46ff-a759-fe938edea56c` |
| 6 | [`14`](https://data.gov.il/dataset/14) | מלגות עידוד לנשים ללימודי הנדסת אלקטרואופטיקה וביואינפורמטיקה | CSV · 1/1 DataStore | `55a7aba5-49b7-49a3-a1b0-4abdccf0135a` |
| 7 | [`17`](https://data.gov.il/dataset/17) | מרכזי להב"ה | XLSX · 1/1 DataStore | `83bead53-7e53-441b-9567-c9bc76e91e78` |
| 8 | [`18`](https://data.gov.il/dataset/18) | מרכז מחקר ופיתוח | XLSX | — |
| 9 | [`19`](https://data.gov.il/dataset/19) | חוגי מדע | XLSX · 1/1 DataStore | `34c19798-754e-42ba-b877-6ce782b1439e` |
| 10 | [`20`](https://data.gov.il/dataset/20) | חוגי מדע - דרכי התקשרות עם מפעילי החוגים | XLSX · 1/1 DataStore | `a59f548a-cbc6-4bf4-85d6-c889e2f5ff6e` |
| 11 | [`21`](https://data.gov.il/dataset/21) | מרכזי חונכות ללימודי מדעים | XLSX · 1/1 DataStore | `ac596ca9-43d3-4321-a6a7-2f0f66560921` |
| 12 | [`29`](https://data.gov.il/dataset/29) | קייטנות מדע קיץ | CSV · 1/1 DataStore | `9a9e7385-6c02-495f-b7ac-1be25d46bb5e` |
| 13 | [`30`](https://data.gov.il/dataset/30) | וועדות לאומיות מולמו"פ | XLSX · 1/1 DataStore | `4ba730c5-d16b-475c-a846-c3e2f59be1f1` |
| 14 | [`46`](https://data.gov.il/dataset/46) | חברי פורום מדענים ראשיים | CSV · 1/1 DataStore | `db41ea48-8983-46b2-9f4a-41cedef36ed9` |
| 15 | [`48`](https://data.gov.il/dataset/48) | סל מדע לרשויות המקומיות | XLSX · 1/1 DataStore | `479641a6-885c-48dd-81d1-f76ade5095ee` |
| 16 | [`49`](https://data.gov.il/dataset/49) | תמיכות במשלחות | XLSX · 1/1 DataStore | `dcf4471f-2605-4440-bb46-4b079c0dcdc1` |
| 17 | [`50`](https://data.gov.il/dataset/50) | תמיכה מצפים ציבוריים 2018 | XLSX | — |
| 18 | [`51`](https://data.gov.il/dataset/51) | סל מדע פרוט לפי חוגים תשעז | XLSX · 1/1 DataStore | `7da4616f-7437-4835-b87b-cca12c7d5e78` |
| 19 | [`52`](https://data.gov.il/dataset/52) | ההיסטוריה של משרד המדע והטכנולוגיה | XLSX · 1/1 DataStore | `b7d66c69-dc54-4dd7-a239-b9c2acf604d8` |
| 20 | [`53`](https://data.gov.il/dataset/53) | מנכ"לי משרד המדע לדורותיהם | XLSX · 1/1 DataStore | `a353ee97-a141-4644-ae2c-87a6a5617478` |
| 21 | [`54`](https://data.gov.il/dataset/54) | ארגונים ומוסדות הפועלים בישראל לקידום נשים במדע ובטכנולוגיה | XLSX | — |
| 22 | [`56`](https://data.gov.il/dataset/56) | ארגונים ומוסדות הפועלים בעולם לקידום נשים במדע ובטכנולוגיה | XLSX · 1/1 DataStore | `d2e082da-6aa5-4f83-97c7-c78e19b44b75` |
| 23 | [`591`](https://data.gov.il/dataset/591) | מועצת המוזיאונים - חברי מועצה | CSV · 1/1 DataStore | `c78d6c91-ba2f-4f00-a6a2-8d953bdb33f5` |
| 24 | [`61`](https://data.gov.il/dataset/61) | תחומי מחקר של משרד המדע | XLSX | — |
| 25 | [`62`](https://data.gov.il/dataset/62) | שרי משרד המדע לדורותיהם | XLSX · 1/1 DataStore | `e4030e8a-e013-42bc-ab10-21825aea97be` |
| 26 | [`my-dataest`](https://data.gov.il/dataset/my-dataest) | בעלי תפקידים | XLSX · 1/1 DataStore | `1fe8684b-da41-4148-84ac-e996ae1b624c` |
| 27 | [`my-dataset2`](https://data.gov.il/dataset/my-dataset2) | מלגות לנשים בתחומי המדע והטכנולוגיה | XLSX · 1/1 DataStore | `c95990f0-1195-47fe-a369-8b6be2650e7f` |
| 28 | [`my-dataset3`](https://data.gov.il/dataset/my-dataset3) | קולות קוראים  משרד המדע והטכנולוגיה | XLSX · 1/1 DataStore | `347114f1-1bd7-49b3-848a-582efc46f888` |
| 29 | [`my-dataset4`](https://data.gov.il/dataset/my-dataset4) | חוקרים | XLSX · 1/1 DataStore | `86e3496b-3864-436d-a530-2232c9e32826` |

### Ministry of Education
<a id="ministry_of_education"></a>
**Slug:** `ministry_of_education` · **Hebrew:** משרד החינוך · **Category:** Education · **Datasets:** 24

- Org page: https://data.gov.il/organization/ministry_of_education
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_education&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`425`](https://data.gov.il/dataset/425) | רשימת מאגרי משרד החינוך | DOC | — |
| 2 | [`coordinates`](https://data.gov.il/dataset/coordinates) | קואורדינטות מוסדות החינוך | CSV · 1/1 DataStore | `5c5d6bb0-755d-470d-84b6-d7dd3135ba9c` |
| 3 | [`excellenceframework-2016`](https://data.gov.il/dataset/excellenceframework-2016) | תמונה חינוכית ארצית תשע"ו | XLS | — |
| 4 | [`excellenceframework-district-2016`](https://data.gov.il/dataset/excellenceframework-district-2016) | תמונה חינוכית מחוזות תשע"ו | XLS · 2 files | — |
| 5 | [`excellenceframework-loacal-2016`](https://data.gov.il/dataset/excellenceframework-loacal-2016) | תמונה חינוכית רשויות תשע"ו | XLS · 2 files | — |
| 6 | [`excellenceframework-school-2016`](https://data.gov.il/dataset/excellenceframework-school-2016) | תמונה חינוכית מוסדות תשע"ו | XLS | — |
| 7 | [`excellenceframework-service-2016`](https://data.gov.il/dataset/excellenceframework-service-2016) | תמונה חינוכית גיוס והתנדבות ברשויות תשע"ו | XLS · 1/1 DataStore | `98610232-8233-4319-b9d8-550064149e26` |
| 8 | [`kitot`](https://data.gov.il/dataset/kitot) | קובץ המכיל רשימת הכיתות במוסדות החינוך בפיקוח משרד החינוך | XLSX · 1/1 DataStore | `7e854745-89c5-4d74-85a1-f430b8f8c8f3` |
| 9 | [`mosdot`](https://data.gov.il/dataset/mosdot) | מאפייני מוסדות חינוך בפיקוח משרד החינוך | XLSX | — |
| 10 | [`rama-tnufa`](https://data.gov.il/dataset/rama-tnufa) | ראמ"ה תנופה | CSV/PDF/XLSX · 3/6 DataStore | `6f0e211c-7385-4d45-8cbe-4cb3d9bf6776` |
| 11 | [`rama_meitzav`](https://data.gov.il/dataset/rama_meitzav) | ראמ"ה מיצ"ב | CSV/PDF · 7/8 DataStore | `b81f0760-2562-4a27-9db7-699542d071a0` |
| 12 | [`shkifut-2015`](https://data.gov.il/dataset/shkifut-2015) | shkifut_2015 | XLSX · 2 files | — |
| 13 | [`shkifut-budget-boarding-2016`](https://data.gov.il/dataset/shkifut-budget-boarding-2016) | שקיפות תקציבית פנימיות תשע"ו | XLS | — |
| 14 | [`shkifut-budget-cluster-2016`](https://data.gov.il/dataset/shkifut-budget-cluster-2016) | שקיפות תקציבית אשכול למ"ס תשע"ו | XLS | — |
| 15 | [`shkifut-budget-cluster-kindergarten-2016`](https://data.gov.il/dataset/shkifut-budget-cluster-kindergarten-2016) | שקיפות תקציבית גני ילדים לפי אשכול למ"ס תשע"ו | XLS | — |
| 16 | [`shkifut-budget-highschool-2016`](https://data.gov.il/dataset/shkifut-budget-highschool-2016) | שיקפות תקציבית חטיבות עליונות רגילות תשע"ו | XLS | — |
| 17 | [`shkifut-budget-kindergarten-2016`](https://data.gov.il/dataset/shkifut-budget-kindergarten-2016) | שקיפות תקציבית גני ילדים לפי רשויות תשע"ו | XLS | — |
| 18 | [`shkifut-budget-legal-2016`](https://data.gov.il/dataset/shkifut-budget-legal-2016) | שקיפות תקציבית מעמד משפטי תשע"ו | XLS | — |
| 19 | [`shkifut-budget-local-2016`](https://data.gov.il/dataset/shkifut-budget-local-2016) | שקיפות תקציבית רשויות תשע"ו | XLS | — |
| 20 | [`shkifut-budget-middleschool-2016`](https://data.gov.il/dataset/shkifut-budget-middleschool-2016) | שקיפות תקציבית חטיבות ביניים רגילות תשע"ו | XLS | — |
| 21 | [`shkifut-budget-school-2016`](https://data.gov.il/dataset/shkifut-budget-school-2016) | שקיפות תקציבית מוסדות תשע"ו | XLS | — |
| 22 | [`shkifut-budget-sector-2016`](https://data.gov.il/dataset/shkifut-budget-sector-2016) | שקיפות תקציבית מגזר תשע"ו | XLS | — |
| 23 | [`shkifut-budget-supervision-2016`](https://data.gov.il/dataset/shkifut-budget-supervision-2016) | שקיפות תקציבית סוג פיקוח תשע"ו | XLS | — |
| 24 | [`tochniyot`](https://data.gov.il/dataset/tochniyot) | מאגר תוכניות חינוכיות | XLSX · 1/1 DataStore | `b04578f3-2ece-47ce-a457-66a00a9d1eac` |

### National Insurance Institute (Bituah Leumi)
<a id="social_security"></a>
**Slug:** `social_security` · **Hebrew:** המוסד לביטוח לאומי · **Category:** Welfare · **Datasets:** 21

- Org page: https://data.gov.il/organization/social_security
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:social_security&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2013`](https://data.gov.il/dataset/2013) | אוכלוסייה ומקבלי גמלאות לפי יישוב - שנת 2013 | PDF/XLS · 25 files | — |
| 2 | [`2014`](https://data.gov.il/dataset/2014) | אוכלוסייה ומקבלי גמלאות לפי יישוב - שנת 2014 | PDF/XLS · 24 files | — |
| 3 | [`285`](https://data.gov.il/dataset/285) | רשימת סניפי ביטוח לאומי | XLS | — |
| 4 | [`287`](https://data.gov.il/dataset/287) | הסכום הבסיסי לחישוב קיצבאות | XLS · 1/1 DataStore | `62635bdd-3ffd-4ae5-90ca-ebf492aa661f` |
| 5 | [`288`](https://data.gov.il/dataset/288) | שכר מינימום | XLSX | — |
| 6 | [`289`](https://data.gov.il/dataset/289) | שיעור דמי הביטוח כאחוז מההכנסה - שכיר בגיל הביטוח | XLS | — |
| 7 | [`290`](https://data.gov.il/dataset/290) | שיעור דמי הביטוח כאחוז מההכנסה - עצמאי בגיל הביטוח | XLS | — |
| 8 | [`291`](https://data.gov.il/dataset/291) | שיעור דמי הביטוח כאחוז מההכנסה - לא עובד שכיר ולא עובד עצמאי בגיל הביטוח | XLS | — |
| 9 | [`292`](https://data.gov.il/dataset/292) | הכנסה מזערית ומרבית לחישוב דמי ביטוח ותקרת הכנסה לשיעור מופחת - עובד שכיר ומעסיק | XLS | — |
| 10 | [`293`](https://data.gov.il/dataset/293) | הכנסה מזערית ומרבית לחישוב דמי ביטוח ותקרת הכנסה לשיעור מופחת - עובד עצמאי | XLS | — |
| 11 | [`294`](https://data.gov.il/dataset/294) | הכנסה מזערית ומרבית לחישוב דמי ביטוח ותקרת הכנסה לשיעור מופחת - לא עובד ולא עצמאי | XLS | — |
| 12 | [`958`](https://data.gov.il/dataset/958) | נתוני אוכלוסיה בישובים בהם מעל 2000 תושבים | XML | — |
| 13 | [`average-salary`](https://data.gov.il/dataset/average-salary) | שכר ממוצע במשק | XLS | — |
| 14 | [`hmo-companies`](https://data.gov.il/dataset/hmo-companies) | חברות בקופת חולים - שנת 2013 | PDF/XLS · 2 files | — |
| 15 | [`hmo_companies2014`](https://data.gov.il/dataset/hmo_companies2014) | חברות בקופת חולים - שנת 2014 | PDF/XLS · 1/2 DataStore | `facda008-6064-4846-a4e6-d8c79f224fe6` |
| 16 | [`monthly-statistics`](https://data.gov.il/dataset/monthly-statistics) | ירחון סטטיסטי | PDF | — |
| 17 | [`population-and-recipients-of-benefits-under-settlement-2010`](https://data.gov.il/dataset/population-and-recipients-of-benefits-under-settlement-2010) | אוכלוסייה ומקבלי גמלאות לפי יישוב - שנת 2010 | PDF/XLS/XLSX · 25 files | — |
| 18 | [`population-and-recipients-of-benefits-under-settlement-2012`](https://data.gov.il/dataset/population-and-recipients-of-benefits-under-settlement-2012) | אוכלוסייה ומקבלי גמלאות לפי יישוב - שנת 2012 | PDF/XLS · 25 files | — |
| 19 | [`population_and_recipients_of_benefits_under_settlement_2011`](https://data.gov.il/dataset/population_and_recipients_of_benefits_under_settlement_2011) | אוכלוסייה ומקבלי גמלאות לפי יישוב - שנת 2011 | PDF/XLS · 24 files | — |
| 20 | [`wages-and-labor-income-by-locality`](https://data.gov.il/dataset/wages-and-labor-income-by-locality) | שכר והכנסות מעבודה לפי יישוב ומשתנים כלכליים שונים - שנת 2009 | PDF/XLS · 2 files | — |
| 21 | [`wages-and-labor-income-by-locality2013`](https://data.gov.il/dataset/wages-and-labor-income-by-locality2013) | שכר והכנסות מעבודה לפי יישוב ומשתנים כלכליים שונים - שנת 2013 | PDF/XLS · 2 files | — |

### Ma'ale Adumim Municipality
<a id="maaleedumim"></a>
**Slug:** `maaleedumim` · **Hebrew:** עיריית מעלה אדומים · **Category:** Municipal · **Datasets:** 20

- Org page: https://data.gov.il/organization/maaleedumim
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:maaleedumim&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`azakamaaleadumim`](https://data.gov.il/dataset/azakamaaleadumim) | צופרי אזעקה | CSV · 1/1 DataStore | `c1d99179-49fc-440a-8835-36a7affe95f7` |
| 2 | [`emergencywatertanks`](https://data.gov.il/dataset/emergencywatertanks) | מיכלי מים בשעת חירום | CSV · 1/1 DataStore | `3402ff6e-8b0e-4d96-b6e7-0f4ff4b8e74e` |
| 3 | [`garbagecontainers`](https://data.gov.il/dataset/garbagecontainers) | מכולות אשפה | CSV · 1/1 DataStore | `f328027c-ea72-4fe1-a0ae-d01a5983f040` |
| 4 | [`hmomaaleadumim`](https://data.gov.il/dataset/hmomaaleadumim) | קופות חולים | CSV · 1/1 DataStore | `a48e7587-554e-4fe5-ba65-973a77f53653` |
| 5 | [`kindergartensmaaleadumim`](https://data.gov.il/dataset/kindergartensmaaleadumim) | גני ילדים | CSV · 1/1 DataStore | `a9d88815-83b1-47f5-86c9-0a5227566950` |
| 6 | [`klitamaaleadumim`](https://data.gov.il/dataset/klitamaaleadumim) | מרכזי קליטה | CSV · 1/1 DataStore | `f03cb415-7df9-4ecd-a4f6-23de70623400` |
| 7 | [`maaleadumimpublicbuildings`](https://data.gov.il/dataset/maaleadumimpublicbuildings) | מיבני ציבור | CSV · 1/1 DataStore | `3a66e7b0-66a4-435c-a093-fb0e6aa59857` |
| 8 | [`mactzavot`](https://data.gov.il/dataset/mactzavot) | מחצבות | CSV · 1/1 DataStore | `688a5f1d-75d1-46a6-829d-57a3125ab97a` |
| 9 | [`meonotyommaaleadumim`](https://data.gov.il/dataset/meonotyommaaleadumim) | מעונות יום | CSV · 1/1 DataStore | `93b07b08-9234-4502-bee0-a054110dd0a3` |
| 10 | [`moadoniot`](https://data.gov.il/dataset/moadoniot) | מועדוניות | CSV · 1/1 DataStore | `09fa0468-204b-483d-ad1c-2c93e062c71e` |
| 11 | [`nature-reservesmaaleadumim`](https://data.gov.il/dataset/nature-reservesmaaleadumim) | שמורות טבע | CSV · 1/1 DataStore | `fbf5d8cf-624f-475d-9f57-fd5a23964414` |
| 12 | [`pharmacy`](https://data.gov.il/dataset/pharmacy) | בתי מרקחת | CSV · 1/1 DataStore | `d65660ac-f895-463e-a8ed-3cdecc5d2c1b` |
| 13 | [`publicbuildings`](https://data.gov.il/dataset/publicbuildings) | מגרשים מבני ציבור | CSV · 1/1 DataStore | `7245186b-8e21-4466-b249-02f1f7d11b44` |
| 14 | [`recyclingfacilitiesmaaleadumim`](https://data.gov.il/dataset/recyclingfacilitiesmaaleadumim) | מתקני מיחזור | CSV · 1/1 DataStore | `4006d6c4-e688-47ee-a680-91deef50592c` |
| 15 | [`schoolsmaaleadumim`](https://data.gov.il/dataset/schoolsmaaleadumim) | בתי ספר | CSV · 1/1 DataStore | `1a6d0069-6311-44f7-80ad-a06aadb2ec69` |
| 16 | [`sheltersmaaleadumim`](https://data.gov.il/dataset/sheltersmaaleadumim) | מקלטים | CSV · 1/1 DataStore | `d35945fa-eb3c-4802-a956-73b6273017f6` |
| 17 | [`special-education-kindergartensmaaleadumim`](https://data.gov.il/dataset/special-education-kindergartensmaaleadumim) | רשימת גני ילדים חינוך מיוחד | CSV · 1/1 DataStore | `00ef7ec7-eed6-4047-93f0-2785930101ea` |
| 18 | [`street-namesmaaleadumim`](https://data.gov.il/dataset/street-namesmaaleadumim) | שמות רחובות | CSV · 1/1 DataStore | `6656e423-84b0-4f1e-923d-62c2c096cda0` |
| 19 | [`tipathlav`](https://data.gov.il/dataset/tipathlav) | טיפת חלב | CSV · 1/1 DataStore | `37aeb5a1-4a8a-4950-b32f-a44570474c41` |
| 20 | [`undergroundcarparksmaaleadumim`](https://data.gov.il/dataset/undergroundcarparksmaaleadumim) | חניונים תת קרקעיים | CSV · 1/1 DataStore | `7aed7347-8629-445f-8b5f-ef45384593e5` |

### Ministry of Agriculture & Food Security
<a id="ministry_of_agriculture"></a>
**Slug:** `ministry_of_agriculture` · **Hebrew:** משרד החקלאות וביטחון המזון · **Category:** Agriculture · **Datasets:** 18

- Org page: https://data.gov.il/organization/ministry_of_agriculture
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_agriculture&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`345`](https://data.gov.il/dataset/345) | רופאים וטרינרים בישראל | CSV · 1/1 DataStore | `14339de6-278c-49ed-a6c1-307044aaee3f` |
| 2 | [`500`](https://data.gov.il/dataset/500) | מאגר תעודות זהות פירות וירקות | CSV · 1/1 DataStore | `f3697dd1-77dd-4628-9c3c-79e5cb84b32e` |
| 3 | [`671`](https://data.gov.il/dataset/671) | מאגר מחלות בעלי חיים | CSV · 1/1 DataStore | `08e21f2a-e635-4b17-92b6-72ef87e2ae72` |
| 4 | [`673`](https://data.gov.il/dataset/673) | מאגר חומרי הדברה | CSV · 2/2 DataStore | `cffe0c50-6856-4187-9315-51bc113cb718` |
| 5 | [`avian-influenza-events`](https://data.gov.il/dataset/avian-influenza-events) | אירועי שפעת העופות | CSV · 1/1 DataStore | `a5dc0714-f945-4e52-a61e-1f7d727b7b4e` |
| 6 | [`database-of-plant-pests-in-israel`](https://data.gov.il/dataset/database-of-plant-pests-in-israel) | מאגר לאומי לנוכחות נגעים בישראל | CSV · 1/1 DataStore | `8f890276-e5e3-478e-a772-17553d2cb10f` |
| 7 | [`gis`](https://data.gov.il/dataset/gis) | מידע גיאוגרפי פתוח לציבור | LINK | — |
| 8 | [`moag-district`](https://data.gov.il/dataset/moag-district) | איתור מחוזות לפי ישובים | CSV · 1/1 DataStore | `1bf27e56-364c-4b61-8b6b-efa9933da677` |
| 9 | [`mrl`](https://data.gov.il/dataset/mrl) | מאגר שאריות חומרי הדברה | CSV · 1/1 DataStore | `3ee1cd66-6176-4c1f-8d38-8f36a1461426` |
| 10 | [`rabies-occurrence`](https://data.gov.il/dataset/rabies-occurrence) | אירועי מחלת הכלבת בישראל | CSV · 1/1 DataStore | `85cd1c27-7824-45ff-9982-22da0285fafb` |
| 11 | [`rashuty`](https://data.gov.il/dataset/rashuty) | רופאים וטרינריים רשותיים | CSV · 1/1 DataStore | `4ea86e61-2b54-4a01-81e4-27dc6cd2c00c` |
| 12 | [`registered_veterinary_vaccines`](https://data.gov.il/dataset/registered_veterinary_vaccines) | מאגר תרכיבים וטרינריים רשומים | CSV · 1/1 DataStore | `016246f4-e7ba-4e1b-b993-dadbbd96da32` |
| 13 | [`rishayon_srifat_gazam`](https://data.gov.il/dataset/rishayon_srifat_gazam) | היתרי שריפת גזם חקלאי | CSV · 2/2 DataStore | `7cfee2aa-1ab3-41f6-aedb-e0eb92f5ad3b` |
| 14 | [`soil_groups`](https://data.gov.il/dataset/soil_groups) | חבורות קרקע | ZIP | — |
| 15 | [`street-trees`](https://data.gov.il/dataset/street-trees) | מאגר אילנות רחוב | CSV · 1/1 DataStore | `f2a07ca4-b7e4-40fe-a7be-6d3c2d0a58f8` |
| 16 | [`vaccine-yard-birds`](https://data.gov.il/dataset/vaccine-yard-birds) | מאגר מחסני עופות חצר ופינות חי | CSV · 1/1 DataStore | `64eb055d-0887-4e26-b3c3-cdb2331d6abc` |
| 17 | [`veterinary_chambers`](https://data.gov.il/dataset/veterinary_chambers) | איתור לשכות וטרינריות לפי ישובים | CSV · 1/1 DataStore | `13750688-f463-48fd-a8f1-ad9a85d394d4` |
| 18 | [`water-efficient-plants`](https://data.gov.il/dataset/water-efficient-plants) | מאגר צמחים חסכניים במים לאנשי המקצוע ולגינה הביתית | CSV · 1/1 DataStore | `94b22c64-5c80-4eb4-b5e5-79cc9bb89814` |

### Ministry of Labor
<a id="labor"></a>
**Slug:** `labor` · **Hebrew:** משרד העבודה · **Category:** Labour · **Datasets:** 18

- Org page: https://data.gov.il/organization/labor
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:labor&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`243fe1ce-b2ae-4c26-9e5e-ce306a602040`](https://data.gov.il/dataset/243fe1ce-b2ae-4c26-9e5e-ce306a602040) | מאגר קבלני כ"א ועגורנים | CSV · 1/1 DataStore | `243fe1ce-b2ae-4c26-9e5e-ce306a602040` |
| 2 | [`5a04dcff-c30c-4c5f-ac85-1018d8014b81`](https://data.gov.il/dataset/5a04dcff-c30c-4c5f-ac85-1018d8014b81) | בודקי שכר מוסמכים | XLSX · 1/1 DataStore | `5a04dcff-c30c-4c5f-ac85-1018d8014b81` |
| 3 | [`b072e36c-a53b-49e1-be08-4a608fcf4638`](https://data.gov.il/dataset/b072e36c-a53b-49e1-be08-4a608fcf4638) | אתרי בנייה פעילים | CSV/PDF · 1/2 DataStore | `b072e36c-a53b-49e1-be08-4a608fcf4638` |
| 4 | [`closed-construction-sites`](https://data.gov.il/dataset/closed-construction-sites) | אתרי בניה שנסגרו | CSV · 1/1 DataStore | `b9257d8f-f93a-4c7d-84dd-e4b0838eadaa` |
| 5 | [`daycare-centers`](https://data.gov.il/dataset/daycare-centers) | מאגר מעונות יום | CSV · 1/1 DataStore | `0f67a263-d9f4-44d4-9816-c96e9dfbc7e5` |
| 6 | [`district-locator`](https://data.gov.il/dataset/district-locator) | איתור מחוז לפי יישוב | XLSX · 1/1 DataStore | `75c2333e-c3d5-41ac-b144-f5f16d820981` |
| 7 | [`employers-financial-sanctions`](https://data.gov.il/dataset/employers-financial-sanctions) | עיצומים כספיים למעסיקים - הפרת חוקי עבודה | XLSX · 1/1 DataStore | `b033f289-4143-4a9d-9612-da6e8cc2f380` |
| 8 | [`hayalim`](https://data.gov.il/dataset/hayalim) | איתור קורסים מאושרים למוסדות - חיילים משוחררים | CSV · 1/1 DataStore | `a0bdb3c2-d3ac-494f-a193-811791066f01` |
| 9 | [`itzumim`](https://data.gov.il/dataset/itzumim) | עיצומים כספיים על ליקויי בטיחות | CSV · 1/1 DataStore | `16d8510b-aee9-4223-aa26-263d2b7ca83a` |
| 10 | [`manpowerconstructors`](https://data.gov.il/dataset/manpowerconstructors) | רשימת קבלני כח אדם מורשים | CSV · 1/1 DataStore | `5938933b-35ce-4a73-9026-59ea377ee1b0` |
| 11 | [`manpowercrane`](https://data.gov.il/dataset/manpowercrane) | קבלני כוח אדם בעלי היתר להעסקת עגורנאי צריח | CSV · 1/1 DataStore | `74cfb7ef-202a-409b-be08-33fb499b77de` |
| 12 | [`permit-license`](https://data.gov.il/dataset/permit-license) | מורשה היתרים | CSV · 1/1 DataStore | `799142ee-3d03-4450-a7f7-0c75098aa97b` |
| 13 | [`private-chambers`](https://data.gov.il/dataset/private-chambers) | רשימת לשכות פרטיות מורשות לתיווך עבודה (עובדים ישראלים בלבד) | CSV · 1/1 DataStore | `00a3819e-7e15-4603-85ea-bdacbc71084c` |
| 14 | [`safetyorderslist`](https://data.gov.il/dataset/safetyorderslist) | רשימת צווי בטיחות | CSV/PDF · 1/2 DataStore | `264cec97-c8f8-496f-84e5-052a63fdea3f` |
| 15 | [`servicecontractors`](https://data.gov.il/dataset/servicecontractors) | רשימת קבלני שירות - שמירה, אבטחה וניקיון | CSV · 1/1 DataStore | `8d13ebff-f4f2-41e6-a39d-663f1c96c196` |
| 16 | [`supervised-schools`](https://data.gov.il/dataset/supervised-schools) | בתי ספר מפוקחים - שמאות רכוש | XLSX · 1/1 DataStore | `39ba77de-887b-4ae8-b4eb-ca4b78e828eb` |
| 17 | [`training-centers`](https://data.gov.il/dataset/training-centers) | מרכזי הכשרה | CSV · 1/1 DataStore | `55d1c36c-dc86-4401-9336-e309965f692b` |
| 18 | [`workshops-training-emergency`](https://data.gov.il/dataset/workshops-training-emergency) | סדנאות והכשרות בחירום | XLSX · 1/1 DataStore | `2e9ae3b7-35df-4461-b8f2-2a3ad5780562` |

### Ministry of Economy & Industry
<a id="moital"></a>
**Slug:** `moital` · **Hebrew:** משרד הכלכלה והתעשייה · **Category:** Economy · **Datasets:** 17

- Org page: https://data.gov.il/organization/moital
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:moital&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`aidtools`](https://data.gov.il/dataset/aidtools) | כלי סיוע של משרד הכלכלה והתעשייה | CSV · 1/1 DataStore | `5c38981d-15be-4721-9ffd-041010f4a16b` |
| 2 | [`cooperative`](https://data.gov.il/dataset/cooperative) | רשימת האגודות השיתופיות | CSV · 1/1 DataStore | `cad6bb66-5560-4cf4-a39c-92518f3f18ef` |
| 3 | [`diamonds`](https://data.gov.il/dataset/diamonds) | מינהל יהלומים | CSV · 1/1 DataStore | `7a0727d5-17cf-4457-a5e2-ff6e07234347` |
| 4 | [`economic-attaches`](https://data.gov.il/dataset/economic-attaches) | רשימת נספחויות כלכליות | CSV · 1/1 DataStore | `bf01b488-c341-41b9-8b3f-257dda11bd43` |
| 5 | [`emergency`](https://data.gov.il/dataset/emergency) | פעילות משק חיוני בענפי מסחר ותעשייה בשעת חירום | CSV · 1/1 DataStore | `3d9d6275-1d84-43b8-ba95-5156a25c31af` |
| 6 | [`ica`](https://data.gov.il/dataset/ica) | ספקי חוץ המחויבים ברכש גומלין | CSV · 1/1 DataStore | `0d9e07a6-cb81-4021-ba72-251e34fc0b38` |
| 7 | [`import_quotas`](https://data.gov.il/dataset/import_quotas) | נקודות מכירה ומחירים מרביים של מוצרי מזון מיובאים | CSV · 1/1 DataStore | `ef2bc38d-321a-4162-a4d2-ce806cf3f298` |
| 8 | [`industrial-zones-info`](https://data.gov.il/dataset/industrial-zones-info) | רשימת איזורי תעשייה | CSV · 1/1 DataStore | `30af8da4-7586-4b00-ac88-c5ee75251632` |
| 9 | [`iron-branches`](https://data.gov.il/dataset/iron-branches) | סניפי ברזל | CSV · 1/1 DataStore | `f7d9c47e-3414-4524-a187-a0f0e057b08a` |
| 10 | [`israel-sal`](https://data.gov.il/dataset/israel-sal) | סניפי הסל של ישראל | CSV · 1/1 DataStore | `71020b9d-03d9-43c7-b4c9-dc69ac179b3a` |
| 11 | [`license_import_chemicals`](https://data.gov.il/dataset/license_import_chemicals) | מאגר פריטים המחייבים רישיון יבוא כימיקלים | CSV · 1/1 DataStore | `76be9404-9ba2-480d-b728-9801aec0a8bc` |
| 12 | [`mandatory-standards`](https://data.gov.il/dataset/mandatory-standards) | מאגר תקנים רשמיים | CSV · 5/5 DataStore | `1a4d94e2-369a-488d-a223-eb1020612fbd` |
| 13 | [`metrology`](https://data.gov.il/dataset/metrology) | משקלות ומידות | CSV · 1/1 DataStore | `5cc7cc5b-9e38-42bd-bc77-f70297c10a1f` |
| 14 | [`price_controlled_consumer_products`](https://data.gov.il/dataset/price_controlled_consumer_products) | מחירי מוצרי צריכה בפיקוח | CSV · 1/1 DataStore | `0a760550-0426-4eb7-acf6-2ee919bf12e7` |
| 15 | [`priority-areas`](https://data.gov.il/dataset/priority-areas) | אזורי עדיפות לאומית ואזורי פיתוח | CSV · 3/3 DataStore | `d0cfa550-51a5-438c-9336-7b117ed174f6` |
| 16 | [`producercode`](https://data.gov.il/dataset/producercode) | רשימת יצרנים שקיבלו אישור לסימון של מזון ארוז מראש בקוד יצרן | CSV · 1/1 DataStore | `40f7e258-86e3-4fce-b663-bde0645616b2` |
| 17 | [`ransom`](https://data.gov.il/dataset/ransom) | החלטות ועדת כופר | CSV · 1/1 DataStore | `cc89067d-a1b0-4ca5-843d-9af1673c6a1d` |

### Ministry of Aliyah & Integration
<a id="ministry_of_immigrant_absorption"></a>
**Slug:** `ministry_of_immigrant_absorption` · **Hebrew:** משרד העלייה והקליטה · **Category:** Immigration · **Datasets:** 17

- Org page: https://data.gov.il/organization/ministry_of_immigrant_absorption
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_immigrant_absorption&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`343`](https://data.gov.il/dataset/343) | רשימת מוסדות ציבור וארגונים מקבלי סיוע מעזבונות לטובת המדינה | XLS · 3 files | — |
| 2 | [`local_aliyah_coordinators`](https://data.gov.il/dataset/local_aliyah_coordinators) | פרוייקטורים - מלווי עולים ברשויות המקומיות | CSV · 2/2 DataStore | `52ddda08-3205-40ee-bc37-bf203a1cf0b2` |
| 3 | [`new-olim-by-cities`](https://data.gov.il/dataset/new-olim-by-cities) | עולים חדשים לפי יישוב קולט | CSV · 2/2 DataStore | `d735ad06-8bde-41aa-8350-a15a36bac18f` |
| 4 | [`new-olim-by-month`](https://data.gov.il/dataset/new-olim-by-month) | עולים חדשים לפי חודש ושנה | CSV · 1/1 DataStore | `99a3db09-aa88-4af1-81d2-ecf3c791002a` |
| 5 | [`new-olim-by-years`](https://data.gov.il/dataset/new-olim-by-years) | עולים חדשים לפי שנים | CSV · 11/11 DataStore | `4db16035-7e85-42c0-8cd6-f4db0f3e96ac` |
| 6 | [`olim-1989-2015-age`](https://data.gov.il/dataset/olim-1989-2015-age) | עולים משנת 1989 עד 2015 - לפי גיל | XLS | — |
| 7 | [`olim-1989-2015-continent`](https://data.gov.il/dataset/olim-1989-2015-continent) | עולים מ 1989 עד 2015 - לפי יבשת | XLS | — |
| 8 | [`olim-1989-2015-district`](https://data.gov.il/dataset/olim-1989-2015-district) | עולים מ 1989 עד 2015 - לפי מחוז | XLS | — |
| 9 | [`olim-1989-2015-gender`](https://data.gov.il/dataset/olim-1989-2015-gender) | עולים מ 1989 עד 2015 - מגדר | XLS | — |
| 10 | [`olim-1989-2015-main`](https://data.gov.il/dataset/olim-1989-2015-main) | עולים מ 1989 עד 2015 - ארצות עיקריות | XLS | — |
| 11 | [`olim-1989-2015-profession`](https://data.gov.il/dataset/olim-1989-2015-profession) | עולים מ 1989 עד 2015 - לפי מקצועות | XLS | — |
| 12 | [`olim-1989-2015-town-county`](https://data.gov.il/dataset/olim-1989-2015-town-county) | עולים מ 1989 עד 2015 לפי ישובים ומועצות | XLS | — |
| 13 | [`olim-1989-2015-year-month`](https://data.gov.il/dataset/olim-1989-2015-year-month) | עולים מ 1989 עד 2015 - לפי חודש ושנה | XLS | — |
| 14 | [`returning-residents-2006-2015`](https://data.gov.il/dataset/returning-residents-2006-2015) | תושבים חוזרים מ 2006 עד 2015 | XLS · 5 files | — |
| 15 | [`siua_kaspi_2017`](https://data.gov.il/dataset/siua_kaspi_2017) | סיוע כספי לעולים שניתן בשנת 2017 | XLS · 1/1 DataStore | `07a2142c-12c3-41d7-8061-ecf855aafb51` |
| 16 | [`tashlumim_2018`](https://data.gov.il/dataset/tashlumim_2018) | תשלומים - סיועים ששולמו לעולים בשנת 2018 | XLSX · 1/1 DataStore | `28f1ce41-c9b7-475d-81c2-6c78ee708114` |
| 17 | [`tashlumim_hozrim_2018`](https://data.gov.il/dataset/tashlumim_hozrim_2018) | תשלומים ששולמו לתושבים חוזרים בשנת 2018 | XLSX · 1/1 DataStore | `db9f1595-c5e5-442f-8686-c180b19d6f01` |

### Central Bureau of Statistics (CBS)
<a id="lamas"></a>
**Slug:** `lamas` · **Hebrew:** הלשכה המרכזית לסטטיסטיקה · **Category:** Statistics · **Datasets:** 14

- Org page: https://data.gov.il/organization/lamas
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:lamas&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2018-puf`](https://data.gov.il/dataset/2018-puf) | תאונות דרכים עם נפגעים - 2018 - PUF מקוצר | ?/CSV/XLSX · 3/6 DataStore | `0cd3917b-6601-4b48-aacf-48b9923fc6fd` |
| 2 | [`2020-puf`](https://data.gov.il/dataset/2020-puf) | תאונות דרכים עם נפגעים - 2020 - PUF מקוצר | ?/CSV/XLSX · 3/6 DataStore | `6790e967-1eee-4223-af88-91f32ed2f02e` |
| 3 | [`2021-puf`](https://data.gov.il/dataset/2021-puf) | תאונות דרכים עם נפגעים - 2021 - PUF מקוצר | ?/CSV/XLSX · 3/6 DataStore | `4150f91e-b2c2-4d28-9d9b-456a40373b27` |
| 4 | [`2022`](https://data.gov.il/dataset/2022) | מפקד האוכלוסין והדיור 2022 | CSV · 3/3 DataStore | `5474c592-3faa-4298-8783-a8da9acc040f` |
| 5 | [`2023-puf`](https://data.gov.il/dataset/2023-puf) | תאונות דרכים עם נפגעים - 2024-2020 - PUF | ?/CSV/DOCX/XLSX · 15/18 DataStore | `16e2b661-2c27-4dee-a068-f664ba8602ec` |
| 6 | [`dictionaries`](https://data.gov.il/dataset/dictionaries) | מילוני מאסטר (Code Lists) | XLSX · 17/17 DataStore | `cd175110-4e71-4fa5-a828-591df6ff0871` |
| 7 | [`localities-in-israel`](https://data.gov.il/dataset/localities-in-israel) | יישובים בישראל - קובצי יישובים | XLS/XLSX · 8/8 DataStore | `d47a54ff-87f0-44b3-b33a-f284c0c38e5a` |
| 8 | [`mokdey_teunot-drachim_2018`](https://data.gov.il/dataset/mokdey_teunot-drachim_2018) | מוקדי תאונות דרכים עם נפגעים 2018 | XLS | — |
| 9 | [`sfirot_tnua_2019`](https://data.gov.il/dataset/sfirot_tnua_2019) | ספירות תנועה 2019 | ?/ZIP · 3 files | — |
| 10 | [`statistical-area-2008`](https://data.gov.il/dataset/statistical-area-2008) | קובץ השכבה הארצית של האזורים הסטטיסטיים ממפקד 2008 | ZIP | — |
| 11 | [`teunot2019`](https://data.gov.il/dataset/teunot2019) | תאונות דרכים עם נפגעים - 2019 - PUF מקוצר | ?/CSV/XLSX · 3/6 DataStore | `0ecf4fd2-7fa0-473d-bbb6-92fe9eed4a98` |
| 12 | [`teunot2022`](https://data.gov.il/dataset/teunot2022) | תאונות דרכים עם נפגעים - 2022 - PUF מקוצר | ?/CSV/XLSX · 3/6 DataStore | `47b2443b-e423-41d6-acda-5f729d1a7018` |
| 13 | [`teunot_2017`](https://data.gov.il/dataset/teunot_2017) | תאונות דרכים עם נפגעים - 2017 - PUF מקוצר | ZIP | — |
| 14 | [`traffic-counts`](https://data.gov.il/dataset/traffic-counts) | ספירות תנועה 2018 | ZIP | — |

### Ministry of Interior
<a id="interior_affairs"></a>
**Slug:** `interior_affairs` · **Hebrew:** משרד הפנים · **Category:** Government · **Datasets:** 13

- Org page: https://data.gov.il/organization/interior_affairs
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:interior_affairs&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`audit-cities`](https://data.gov.il/dataset/audit-cities) | דוחות כספיים מבוקרים עיריות | CSV/XLSX · 9/9 DataStore | `93ec8816-eb41-43d5-bc69-12b8307a17b2` |
| 2 | [`beach`](https://data.gov.il/dataset/beach) | חופים ותחנות הצלה | XLSX · 1/1 DataStore | `48cbb4b2-4492-4a33-93f9-b615e37d8eb5` |
| 3 | [`corpo-list`](https://data.gov.il/dataset/corpo-list) | חברי הנהלת תאגיד (דירקטוריון) עובדים נציגי ציבור שאושרו על ידי הוועדה | XLSX · 1/1 DataStore | `c4c7f2ee-d4eb-47da-9f92-b6934dd035f6` |
| 4 | [`local-authorities`](https://data.gov.il/dataset/local-authorities) | דוחות מבוקרים של הרשויות המקומיות לפי שנים | CSV/XLSX · 4/4 DataStore | `1618b871-9b3d-4bc5-acc0-c1fbe939a3b1` |
| 5 | [`local-council-1`](https://data.gov.il/dataset/local-council-1) | דוחות כספיים מבוקרים - מועצות מקומיות | CSV/XLSX · 13/13 DataStore | `a001d2a7-f941-4ea9-beab-8065f549994f` |
| 6 | [`local_council`](https://data.gov.il/dataset/local_council) | דוחות כספיים מבוקרים - מועצות אזוריות | CSV/XLSX · 10/10 DataStore | `9759f4a9-fa40-40b2-820a-29f8e45edf2e` |
| 7 | [`manager-elections-2023`](https://data.gov.il/dataset/manager-elections-2023) | פרטי קשר עם מנהלי הבחירות | XLSX · 1/1 DataStore | `986a8917-4a5a-4c96-b359-6c206800b423` |
| 8 | [`misgadim`](https://data.gov.il/dataset/misgadim) | רשימת מסגדים | XLSX · 1/1 DataStore | `42f1d4b0-ce70-4e60-898f-38dd91f83cc5` |
| 9 | [`municipal-corporations`](https://data.gov.il/dataset/municipal-corporations) | תאגידים עירוניים | XLSX · 1/1 DataStore | `4d7e9bb8-2457-46f9-9eb3-0c0acf5cd766` |
| 10 | [`payment`](https://data.gov.il/dataset/payment) | תשלומי משרד הפנים שהועברו | XLSX · 1/1 DataStore | `702f9bd7-c97b-4cff-92c8-0383d95e5955` |
| 11 | [`pollingvote2023`](https://data.gov.il/dataset/pollingvote2023) | קלפיות נגישות להצבעת בוחרים המוגבלים בניידות | CSV · 1/1 DataStore | `d12632aa-1c0b-4162-8584-58dd6f404a6c` |
| 12 | [`specialpoll2025`](https://data.gov.il/dataset/specialpoll2025) | בחירות לרשויות המקומיות - קלפיות מיוחדות בפריסה ארצית | XLSX · 1/1 DataStore | `ec097015-b3a0-4b2d-aaa9-da343bdf3b90` |
| 13 | [`tabbar`](https://data.gov.il/dataset/tabbar) | אישורי תקציב בלתי רגיל לגוף מוניציפאלי | XLSX · 1/1 DataStore | `9a830f1b-543d-4f5d-9302-787885b36624` |

### Planning Administration
<a id="iplan"></a>
**Slug:** `iplan` · **Hebrew:** מינהל התכנון  · **Category:** Planning · **Datasets:** 13

- Org page: https://data.gov.il/organization/iplan
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:iplan&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`ezoriyut_str`](https://data.gov.il/dataset/ezoriyut_str) | שכבת רצף אזורי תפקוד מפרק אזוריות בתכנית האסטרטגית המרחבית | ZIP | — |
| 2 | [`iplan-itur-tochnit`](https://data.gov.il/dataset/iplan-itur-tochnit) | מידע תכנוני של מינהל התכנון (אתר הצפייה) | ? | — |
| 3 | [`israel_rain_areas_for_planning`](https://data.gov.il/dataset/israel_rain_areas_for_planning) | אזורי גשם לתכנון | ZIP | — |
| 4 | [`merchav_tichnun`](https://data.gov.il/dataset/merchav_tichnun) | מרחבי תכנון | ? | — |
| 5 | [`planresearchers`](https://data.gov.il/dataset/planresearchers) | חוקרים לשמיעת התנגדויות - מינהל התכנון | XLSX · 1/1 DataStore | `55acb9b5-5437-44f5-a84a-f96c4577dd4d` |
| 6 | [`tatal`](https://data.gov.il/dataset/tatal) | תכניות תשתיות לאומיות | ? | — |
| 7 | [`tma`](https://data.gov.il/dataset/tma) | תכניות מתאר ארציות | ? | — |
| 8 | [`tmm`](https://data.gov.il/dataset/tmm) | תכניות מתאר מחוזיות | ? | — |
| 9 | [`valkachshap`](https://data.gov.il/dataset/valkachshap) | גיליונות ולקחש"פ | ? | — |
| 10 | [`vatmal`](https://data.gov.il/dataset/vatmal) | הוועדה הארצית לתכנון ולבניה של מתחמים מועדפים לדיור (ותמל) - מתחמים מוכרזים | WEB-SERVICE | — |
| 11 | [`xplan`](https://data.gov.il/dataset/xplan) | XPLAN - מה חל במקום שלי | ? | — |
| 12 | [`xplan2`](https://data.gov.il/dataset/xplan2) | תוכניות מקוונות | ZIP · 2 files | — |
| 13 | [`xplan_services`](https://data.gov.il/dataset/xplan_services) | שירותי מפה תכנוניים מקוונים - סרביסים | ?/DOCX · 2 files | — |

### Ministry of Housing & Construction
<a id="ministry_of_housing"></a>
**Slug:** `ministry_of_housing` · **Hebrew:** משרד הבינוי והשיכון · **Category:** Housing · **Datasets:** 12

- Org page: https://data.gov.il/organization/ministry_of_housing
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_housing&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`aluyot-pituach`](https://data.gov.il/dataset/aluyot-pituach) | עלויות פיתוח בבניה העירונית | CSV · 1/1 DataStore | `bf164a03-55c7-4bea-8740-66ce60a51a2c` |
| 2 | [`diurtziburi`](https://data.gov.il/dataset/diurtziburi) | דירות הדיור הציבורי | CSV/PDF · 3/4 DataStore | `c3a68837-9b7a-4ee7-bd92-130678dc8ae3` |
| 3 | [`gis-_`](https://data.gov.il/dataset/gis-_) | שכבות מידע גיאוגרפי (GIS) של משרד הבינוי והשיכון | DOCX/ZIP · 5 files | — |
| 4 | [`gis_urban_renewal`](https://data.gov.il/dataset/gis_urban_renewal) | שכבות מידע גיאוגרפי (GIS) - התחדשות ערונית | ZIP · 2 files | — |
| 5 | [`hitkadmuthabnia`](https://data.gov.il/dataset/hitkadmuthabnia) | התקדמות הבניה | CSV · 1/1 DataStore | `1ec45809-5927-430a-9b30-77f77f528ce3` |
| 6 | [`hostelsgis`](https://data.gov.il/dataset/hostelsgis) | בתי דיור | CSV/ZIP · 1/2 DataStore | `0c6fa0a9-a0ef-4860-aa42-ba4d4c78caa4` |
| 7 | [`mechir-lamishtaken`](https://data.gov.il/dataset/mechir-lamishtaken) | נתונים תקופתיים - תכנית דירה בהנחה | CSV · 2/2 DataStore | `7c8255d0-49ef-49db-8904-4cf917586031` |
| 8 | [`metachnenim`](https://data.gov.il/dataset/metachnenim) | רשימת מתכננים ומודדים | CSV · 1/1 DataStore | `a8ca5203-7adc-4bc1-a0ed-3fd4eaa74dcc` |
| 9 | [`pinkashakablanim`](https://data.gov.il/dataset/pinkashakablanim) | פנקס הקבלנים הרשומים | CSV · 1/1 DataStore | `4eb61bd6-18cf-4e7c-9f9c-e166dfa0a2d8` |
| 10 | [`shikumshchunot`](https://data.gov.il/dataset/shikumshchunot) | שיקום שכונות | CSV · 3/3 DataStore | `a66f8a88-9c7a-440e-b206-0c0d84ce9b7a` |
| 11 | [`tichnun-pituah`](https://data.gov.il/dataset/tichnun-pituah) | פיתוח ותשתית | CSV · 2/2 DataStore | `04e375ef-08a6-4327-8044-7bd595c4d106` |
| 12 | [`urban_renewal`](https://data.gov.il/dataset/urban_renewal) | התחדשות עירונית | CSV · 1/1 DataStore | `f65a0daf-f737-49c5-9424-d378d52104f5` |

### Ministry of Religious Services
<a id="religion-office"></a>
**Slug:** `religion-office` · **Hebrew:** המשרד לשירותי דת · **Category:** Religion · **Datasets:** 12

- Org page: https://data.gov.il/organization/religion-office
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:religion-office&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2018`](https://data.gov.il/dataset/2018) | מקוואות טהרה 2018 | XLS · 1/1 DataStore | `9a939c58-d149-4c07-b37f-77dbf0d50e35` |
| 2 | [`2025`](https://data.gov.il/dataset/2025) | תעריפי חלקות קבר מחיים 2025 | XLSX · 1/1 DataStore | `04f046d0-643b-47ea-8a72-e9c079cd67d2` |
| 3 | [`councils`](https://data.gov.il/dataset/councils) | מועצות דתיות וראשיהן | XLS · 1/1 DataStore | `80822f1d-ad3e-437c-b799-92c57aa06477` |
| 4 | [`dat-gov-il`](https://data.gov.il/dataset/dat-gov-il) | זמני הדלקת נרות שבת וחג לשנת התש"ף | XLS · 1/1 DataStore | `fc678ba7-0668-47ba-94af-1a69d049226f` |
| 5 | [`ethiopianrav`](https://data.gov.il/dataset/ethiopianrav) | רבני העדה האתיופית | XLSX · 1/1 DataStore | `cd9f47b3-e4fa-42c9-ad6b-97410c78725b` |
| 6 | [`http-dat-gov-il-forms-data-shabat-5777-xls`](https://data.gov.il/dataset/http-dat-gov-il-forms-data-shabat-5777-xls) | זמני הדלקת נרות שבת וחג לשנת התשע"ז | XLS | — |
| 7 | [`http-dat-gov-il-forms-data-shabat-5778-xls`](https://data.gov.il/dataset/http-dat-gov-il-forms-data-shabat-5778-xls) | זמני הדלקת נרות שבת וחג לשנת התשע"ח | XLS · 1/1 DataStore | `eb5ad08d-38f5-446d-8f3a-3f47fc5ee5ce` |
| 8 | [`https-shirathayam-m-datit-org-il-pirsumnisuin`](https://data.gov.il/dataset/https-shirathayam-m-datit-org-il-pirsumnisuin) | לרשימת הנרשמים לנישואין | ? | — |
| 9 | [`kosherbusiness`](https://data.gov.il/dataset/kosherbusiness) | בתי עסק המחזיקים בתעודת כשרות | CSV · 1/1 DataStore | `c54032cb-5306-4be9-a20d-a0be0ba49cc1` |
| 10 | [`mikve`](https://data.gov.il/dataset/mikve) | מקוואות טהרה | CSV · 1/1 DataStore | `e80a5e59-3b0f-4be9-983a-dc0971907626` |
| 11 | [`my_dataset`](https://data.gov.il/dataset/my_dataset) | זמני הדלקת נרות שבת וחג לשנים התש"ף-התשפ"ו | XLSX · 1/1 DataStore | `cfe1dd76-a7f8-453a-aa42-88e5db30d567` |
| 12 | [`www-dat-gov-il`](https://data.gov.il/dataset/www-dat-gov-il) | זמני הדלקת נרות שבת וחג לשנת התשע"ט | XLS · 1/1 DataStore | `90925e82-7fa1-4d1f-a733-45ce870ca1a1` |

### Ministry of Tourism
<a id="ministry_of_tourism"></a>
**Slug:** `ministry_of_tourism` · **Hebrew:** משרד התיירות · **Category:** Tourism · **Datasets:** 11

- Org page: https://data.gov.il/organization/ministry_of_tourism
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_tourism&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`emergency_phones`](https://data.gov.il/dataset/emergency_phones) | טלפונים למצבי חירום | XLSX · 2/2 DataStore | `d0f0a13e-7e92-4baf-9293-e8db6d5caf81` |
| 2 | [`holidaysinisrael`](https://data.gov.il/dataset/holidaysinisrael) | חגים בישראל - Holidays in Israel | DOCX/XLSX · 2/3 DataStore | `38a82e1f-2800-452f-bf70-20c1f4439924` |
| 3 | [`lishkot-tayarut`](https://data.gov.il/dataset/lishkot-tayarut) | לשכות תיירות חו"ל - Tourism Offices Abroad | XLSX · 2/2 DataStore | `5d34967a-bf66-4239-95e5-26a4551b2d57` |
| 4 | [`lishkot-tayarut-eng`](https://data.gov.il/dataset/lishkot-tayarut-eng) | לשכות מידע - Tourist Information | XLSX · 2/2 DataStore | `967a8a23-c08c-4c47-b39d-ce350537821b` |
| 5 | [`moreh-dereh-eng`](https://data.gov.il/dataset/moreh-dereh-eng) | מורי דרך - Tour Guides | XLS · 2/2 DataStore | `8c1775ab-ca3c-4891-85f7-43ee24c585df` |
| 6 | [`picture-gallery-eng`](https://data.gov.il/dataset/picture-gallery-eng) | גלריית תמונות - Picture Gallery | DOCX/XLS/XLSX · 11/12 DataStore | `07f57519-193d-458e-9cf3-fe3edd3a34cc` |
| 7 | [`press`](https://data.gov.il/dataset/press) | פרסומים בעיתונות - Official Press Publications | DOCX/XLS · 2/3 DataStore | `457cb173-75a9-4623-96cc-cef273d49d20` |
| 8 | [`professionallibrary`](https://data.gov.il/dataset/professionallibrary) | ספרייה מקצועית - Professional Library | XLS · 1/1 DataStore | `d08657a8-9adc-45e7-9c53-9dcf200ea0e3` |
| 9 | [`training-courses`](https://data.gov.il/dataset/training-courses) | השתלמויות למורי דרך | CSV/XLSX · 7/7 DataStore | `5343c53e-f49b-4cd4-a9f6-1fd62379ab51` |
| 10 | [`vat-refund-stores`](https://data.gov.il/dataset/vat-refund-stores) | עסקים במסגרת החזר מעמ לתייר - VAT Refund Stores | CSV/DOCX/XLSX · 4/5 DataStore | `5555edc5-532d-46b5-8415-01a54d5a5b73` |
| 11 | [`vod`](https://data.gov.il/dataset/vod) | VOD | DOCX/XLS/XLSX · 11/12 DataStore | `e07b1a46-e5cf-4ae5-84fe-45096a61023c` |

### Ministry of Communications
<a id="tikshoret"></a>
**Slug:** `tikshoret` · **Hebrew:** משרד התקשורת · **Category:** Communications · **Datasets:** 11

- Org page: https://data.gov.il/organization/tikshoret
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:tikshoret&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`approved-items-by-personal-import`](https://data.gov.il/dataset/approved-items-by-personal-import) | ציוד אלחוטי - פריטים ביבוא אישי שקיבלו אישור ממשרד התקשורת | CSV/XLSX · 2/2 DataStore | `fe229457-3864-49fc-b22f-1e8386ec304c` |
| 2 | [`bilateral-communications-agreements`](https://data.gov.il/dataset/bilateral-communications-agreements) | הסכמי תקשורת בילטרליים עם מדינות | CSV/XLSX · 2/2 DataStore | `929010ba-b920-4d54-9360-12e19330eb95` |
| 3 | [`israel-dialing-plan`](https://data.gov.il/dataset/israel-dialing-plan) | Israel Dialing Plan – Within Israel - רשימת מספרי טלפון לשירותים ארציים | CSV/XLSX · 2/2 DataStore | `da86f974-f009-496e-b0ce-a92251603291` |
| 4 | [`israel-numbering-plan`](https://data.gov.il/dataset/israel-numbering-plan) | Israel Numbering Plan | CSV/XLSX · 2/2 DataStore | `74b44725-d8cc-4ae9-ba08-2c40a61ab68e` |
| 5 | [`items-appproved-by-personal-import`](https://data.gov.il/dataset/items-appproved-by-personal-import) | רשימת פריטים ליבוא מסחרי שאישורם בתוקף לצורך הגשת אישור על סמך אישור | CSV/XLS · 2/2 DataStore | `78a1a14d-8f30-43e5-b0d7-00e737ec9346` |
| 6 | [`items-that-not-approved-by-personal-import`](https://data.gov.il/dataset/items-that-not-approved-by-personal-import) | ציוד אלחוטי - פריטים ביבוא אישי שלא קיבלו אישור משרד התקשורת | CSV/XLSX · 2/2 DataStore | `b4dff6d1-7864-4d19-a24b-f4d1115c9760` |
| 7 | [`list-of-emergency-phone-numbers-should-not-be-blocked`](https://data.gov.il/dataset/list-of-emergency-phone-numbers-should-not-be-blocked) | רשימת מוקדי חירום וסיוע שלא ניתן לחסום את החיוג אליהם | CSV/XLSX · 2/2 DataStore | `199eb131-6808-4321-95a3-9b57cdc729da` |
| 8 | [`lists-permit-holders-for-the-provision-of-large-scale-post`](https://data.gov.il/dataset/lists-permit-holders-for-the-provision-of-large-scale-post) | רשימות בעלי היתרים למתן שירותי דואר כמותי | CSV/PDF/XLSX · 2/3 DataStore | `140d8dfa-8f45-469f-b645-7d349f8fa906` |
| 9 | [`permitholders`](https://data.gov.il/dataset/permitholders) | רשימת בעלי היתר כללי לאיסוף , העברה או מסירה של מכתבים | CSV/XLSX · 2/2 DataStore | `03eb376c-6130-40de-8753-6935714d11fd` |
| 10 | [`plmn-codes-in-israel`](https://data.gov.il/dataset/plmn-codes-in-israel) | PLMN codes in Israel | CSV/XLSX · 2/2 DataStore | `d6b9480c-f09e-471c-a9a7-46494d221d27` |
| 11 | [`public-inquiry-officials-in-communications-companies`](https://data.gov.il/dataset/public-inquiry-officials-in-communications-companies) | רשימת האחראים לפניות הציבור בחברות | CSV/XLSX · 5/5 DataStore | `c027a835-aa60-4698-9667-837b3f985692` |

### Ministry of Foreign Affairs
<a id="ministry_of_exterior"></a>
**Slug:** `ministry_of_exterior` · **Hebrew:** משרד החוץ · **Category:** Government · **Datasets:** 10

- Org page: https://data.gov.il/organization/ministry_of_exterior
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_exterior&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`foreignntz`](https://data.gov.il/dataset/foreignntz) | נציגויות זרות | CSV · 2/2 DataStore | `95ce3d91-34fb-42d2-bcb7-fefdf54cee42` |
| 2 | [`honoraryconsuls`](https://data.gov.il/dataset/honoraryconsuls) | קונסולי כבוד של מדינת ישראל | CSV · 4/4 DataStore | `06bd9490-bcdd-402a-8eaa-2c67b25b69ed` |
| 3 | [`idea`](https://data.gov.il/dataset/idea) | כותרים בספריית משרד החוץ | XLSX | — |
| 4 | [`mdn-status`](https://data.gov.il/dataset/mdn-status) | רשימת מדינות | XLSX · 1/1 DataStore | `b1fdc757-07e3-4875-a023-99e59ac44f24` |
| 5 | [`mfa_un`](https://data.gov.il/dataset/mfa_un) | החלטות האומות המאוחדות | XLSX · 2/2 DataStore | `ab6f76ef-9024-4618-8af2-f07654f0f3c8` |
| 6 | [`mfaamanot`](https://data.gov.il/dataset/mfaamanot) | אמנות משרד החוץ | XLSX · 1/1 DataStore | `5c98ccc0-5462-41e9-b335-786cf617c314` |
| 7 | [`ntz-mail`](https://data.gov.il/dataset/ntz-mail) | נציגויות בעולם - דרכי התקשרות | XLSX · 1/1 DataStore | `45aaab9e-0e16-4c85-b980-59bd4a837a34` |
| 8 | [`ntz-short`](https://data.gov.il/dataset/ntz-short) | רשימת נציגויות ישראל בעולם | CSV · 2/2 DataStore | `6fc859cb-8a6f-458b-bd5a-9bd0cfbfce11` |
| 9 | [`tableconsularservices`](https://data.gov.il/dataset/tableconsularservices) | טבלת אגרות לשירותים קונסולריים | XLSX · 1/1 DataStore | `abf80622-209d-43aa-9283-47a749d8a889` |
| 10 | [`visa_to_israel`](https://data.gov.il/dataset/visa_to_israel) | אשרות כניסה לזרים לישראל באשרות ב-2 | XLSX · 1/1 DataStore | `6c801ecf-019e-47d6-95be-b5fcb60cf87d` |

### Prime Minister's Office
<a id="pmo"></a>
**Slug:** `pmo` · **Hebrew:** משרד ראש הממשלה  · **Category:** Government · **Datasets:** 10

- Org page: https://data.gov.il/organization/pmo
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:pmo&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2017`](https://data.gov.il/dataset/2017) | דוח מסכם 2017 - דיווחי ביצוע על החלטות ממשלה | XLSX | — |
| 2 | [`2019infrastructure`](https://data.gov.il/dataset/2019infrastructure) | תשתית לצמיחה 2019 - התכנית הרב שנתית לפיתוח תשתיות | XLSX | — |
| 3 | [`2020`](https://data.gov.il/dataset/2020) | תשתית לצמיחה 2020 - התכנית הרב שנתית לפיתוח תשתיות | XLSX | — |
| 4 | [`2023`](https://data.gov.il/dataset/2023) | מעקב אחר ביצוע משימות החלטות ממשלה לשנת 2023 | XLSX · 2/2 DataStore | `5b6cd1b1-c553-4838-af7e-c1132e7234f1` |
| 5 | [`govdecisions2016`](https://data.gov.il/dataset/govdecisions2016) | דוח מסכם 2016 - דיווחי ביצוע על החלטות ממשלה | XLSX | — |
| 6 | [`infrastructures2017`](https://data.gov.il/dataset/infrastructures2017) | תשתית לצמיחה 2017 - התכנית הרב שנתית לפיתוח תשתיות | XLSX | — |
| 7 | [`municipal_indices`](https://data.gov.il/dataset/municipal_indices) | מדדים מוניצפלים | CSV · 1/1 DataStore | `169820f7-c235-49c0-ba3c-0561778ae063` |
| 8 | [`plan2023`](https://data.gov.il/dataset/plan2023) | מעקב אחר ביצוע תוכניות העבודה הממשלתיות לשנת 2023 | PDF/XLSX · 2/3 DataStore | `513e540a-4e16-4f32-b44a-e4c71545e87f` |
| 9 | [`plan2024`](https://data.gov.il/dataset/plan2024) | ספר תוכניות העבודה לשנת 2024 | XLSX · 2/2 DataStore | `7bb18dfa-b8e3-419d-ada8-ced8d9deb973` |
| 10 | [`plan2024-1`](https://data.gov.il/dataset/plan2024-1) | דוח ביצוע תוכניות העבודה הממשלתיות לשנת 2024 | PDF/XLSX · 2/3 DataStore | `1a022f23-08f4-4ce8-92ca-7657aafcd3bf` |

### Fire & Rescue Commission
<a id="firefightingcommission"></a>
**Slug:** `firefightingcommission` · **Hebrew:** כבאות והצלה לישראל · **Category:** Public Safety · **Datasets:** 9

- Org page: https://data.gov.il/organization/firefightingcommission
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:firefightingcommission&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`authorized-official`](https://data.gov.il/dataset/authorized-official) | גורמים מוסמכים לביצוע בדיקת משטר הפעלות (אינטגרציה) | CSV · 1/1 DataStore | `0b945270-3d37-4ff5-8440-133820ecc3da` |
| 2 | [`businessreq`](https://data.gov.il/dataset/businessreq) | דרישות בטיחות אש לרישוי עסקים | CSV/PDF/XLS · 37/39 DataStore | `5b75ab27-d01c-4f76-8e6e-b75d803ea065` |
| 3 | [`certified_laboratories`](https://data.gov.il/dataset/certified_laboratories) | מעבדות מוכרות לביצוע בדיקות בתחום מערכות גילוי וכיבוי אש וציוד כיבוי אש | CSV · 1/1 DataStore | `bfab076e-827a-4fc4-b5ba-9c27c9fc884c` |
| 4 | [`eventsdistrict`](https://data.gov.il/dataset/eventsdistrict) | אירועים לפי מחוז | CSV/PDF/XLSX · 33/35 DataStore | `0f971ff1-3aba-4fe3-9695-246d01ee1531` |
| 5 | [`firefightingfees`](https://data.gov.il/dataset/firefightingfees) | אגרות כבאות והצלה | CSV/XLSX · 10/10 DataStore | `8b336205-fe67-476b-a367-582ce6203c6b` |
| 6 | [`inspectors_fire_extinguishers`](https://data.gov.il/dataset/inspectors_fire_extinguishers) | רשימת מבקרים ותחזוקאי מטפים מורשים | CSV · 1/1 DataStore | `ea004fd2-251e-4ea1-9b03-0eefb51b8f74` |
| 7 | [`israel_fire_rescue_stations`](https://data.gov.il/dataset/israel_fire_rescue_stations) | תחנות כיבוי | CSV · 6/6 DataStore | `7f3009dd-b299-462c-8a6d-9c645b68059f` |
| 8 | [`isreal_fire_rescue_gis`](https://data.gov.il/dataset/isreal_fire_rescue_gis) | כבאות והצלה - גבולות מחוזות ותחנות אזוריות | PDF/ZIP · 5 files | — |
| 9 | [`prvbuildingquirement`](https://data.gov.il/dataset/prvbuildingquirement) | דרישות בטיחות אש להיתרי בניה | CSV/PDF/XLS · 36/38 DataStore | `eeb73fe0-bf1a-4c7f-b2f2-22c5717afa6d` |

### Capital Market, Insurance & Savings Authority
<a id="cma"></a>
**Slug:** `cma` · **Hebrew:** רשות שוק ההון, ביטוח וחיסכון · **Category:** Finance · **Datasets:** 9

- Org page: https://data.gov.il/organization/cma
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:cma&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`gemelnet`](https://data.gov.il/dataset/gemelnet) | גמל-נט | CSV/XLSX · 4/4 DataStore | `91c849ed-ddc4-472b-bd09-0f5486cea35c` |
| 2 | [`insurance`](https://data.gov.il/dataset/insurance) | ביטוח-נט | CSV/XLSX · 4/4 DataStore | `584e6b69-174f-46c9-b8db-03925b4c68c6` |
| 3 | [`mishtatef`](https://data.gov.il/dataset/mishtatef) | רשימות נכסים - גופים מוסדיים | RAR/ZIP · 6 files | — |
| 4 | [`nechasimb`](https://data.gov.il/dataset/nechasimb) | רשימות נכסים - תיק משתתף חברות הביטוח | ZIP · 5 files | — |
| 5 | [`nechasimg`](https://data.gov.il/dataset/nechasimg) | רשימות נכסים - קופות גמל | ZIP · 5 files | — |
| 6 | [`nechasimp`](https://data.gov.il/dataset/nechasimp) | רשימות נכסים - קרנות הפנסיה | ZIP · 5 files | — |
| 7 | [`pensia-net`](https://data.gov.il/dataset/pensia-net) | פנסיה-נט | CSV/XLSX · 4/4 DataStore | `a66926f3-e396-4984-a4db-75486751c2f7` |
| 8 | [`serviceindex`](https://data.gov.il/dataset/serviceindex) | נתוני מדד שירות – חברות ביטוח | DOCX/XLSX · 4 files | — |
| 9 | [`transfer_bank`](https://data.gov.il/dataset/transfer_bank) | פרטי קופות לצורך העברת כספים בין גופים מוסדיים | CSV · 1/1 DataStore | `b5223cbc-e1b2-4503-a499-97cdcd7190d2` |

### Population & Immigration Authority
<a id="population_authority"></a>
**Slug:** `population_authority` · **Hebrew:** רשות האוכלוסין וההגירה · **Category:** Immigration · **Datasets:** 9

- Org page: https://data.gov.il/organization/population_authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:population_authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`321`](https://data.gov.il/dataset/321) | רשימת רחובות ישראל | CSV/XLSX/XML · 12/23 DataStore | `9ad3862c-8391-4b2f-84a4-2d4c68625f4b` |
| 2 | [`citiesandsettelments`](https://data.gov.il/dataset/citiesandsettelments) | רשימת ישובים בישראל | CSV/XML · 12/23 DataStore | `5c78e9fa-c2e2-4771-93ff-7f400a12f7ba` |
| 3 | [`countries`](https://data.gov.il/dataset/countries) | רשימת ארצות מוכרות ע"י מדינת ישראל | CSV/XML · 11/22 DataStore | `c84082e9-7d45-4853-9a95-e7eaad7f66d5` |
| 4 | [`firs-name`](https://data.gov.il/dataset/firs-name) | שמות פרטיים בישראל | CSV · 1/1 DataStore | `c4fb2685-381f-4e99-a88e-b9b7ed703117` |
| 5 | [`israel-streets-synom`](https://data.gov.il/dataset/israel-streets-synom) | רשימת רחובות בישראל - קובץ עם סינונימיים | CSV/XML · 11/22 DataStore | `bf185c7f-1a4e-4662-88c5-fa118a244bda` |
| 6 | [`residents_in_israel_by_communities_and_age_groups`](https://data.gov.il/dataset/residents_in_israel_by_communities_and_age_groups) | תושבים בישראל לפי ישובים וקבוצות גיל | CSV/XML · 11/22 DataStore | `64edd0ee-3d5d-43ce-8562-c336c24dbc1f` |
| 7 | [`stats_rish`](https://data.gov.il/dataset/stats_rish) | סטטיסטיקת הנפקת רשיונות לזרים | CSV/XML · 7/14 DataStore | `1e3474eb-970f-49cc-9cbf-ed85d4533b8f` |
| 8 | [`voting-polls`](https://data.gov.il/dataset/voting-polls) | קלפיות | XLS · 1/1 DataStore | `68c4d7e8-2218-48ee-996f-2db2f72b2395` |
| 9 | [`young_residents_in_israel_by_settlements`](https://data.gov.il/dataset/young_residents_in_israel_by_settlements) | תושבים צעירים בישראל לפי ישובים | CSV/XML · 1/2 DataStore | `b8112650-a2f8-41f2-9c05-a9b9483fb4c0` |

### Rabbinical Courts
<a id="rabinical_court"></a>
**Slug:** `rabinical_court` · **Hebrew:** בתי הדין הרבניים · **Category:** Religion · **Datasets:** 9

- Org page: https://data.gov.il/organization/rabinical_court
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:rabinical_court&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`860`](https://data.gov.il/dataset/860) | תעריפי אגרות של בתי הדין הרבניים | CSV · 1/1 DataStore | `87969ef3-ac7e-4597-8909-995c8df422bf` |
| 2 | [`861`](https://data.gov.il/dataset/861) | רשימת בתי דין | CSV · 1/1 DataStore | `de9b13c6-1850-4714-9e21-390d48e4d582` |
| 3 | [`862`](https://data.gov.il/dataset/862) | פסק דין לגירושין לפי שנים | CSV · 1/1 DataStore | `30035b4c-1bea-467f-a368-b1453d540fd0` |
| 4 | [`863`](https://data.gov.il/dataset/863) | מספר זוגות שהתגרשו לפי מקום מגורים של הזוג | CSV · 1/1 DataStore | `524aaf1e-7e4f-423b-9e0a-d40bbbacd2bc` |
| 5 | [`864`](https://data.gov.il/dataset/864) | אזורי שיפוט (בית דין ליישוב) | CSV · 1/1 DataStore | `b8b4755a-d34a-4fc9-8242-fe6eaa763021` |
| 6 | [`865`](https://data.gov.il/dataset/865) | סוגי תיקים שנפתחו לפי שנים | CSV · 1/1 DataStore | `37daddc6-2ad4-4453-b1ca-0c9bb1d4b034` |
| 7 | [`983`](https://data.gov.il/dataset/983) | סנקציות על פי חוק כפיית ציות | CSV · 1/1 DataStore | `a5986bdd-a920-408e-aef0-56d7b485f2e8` |
| 8 | [`hekdeshot1`](https://data.gov.il/dataset/hekdeshot1) | רשימת הקדשות | XLSX · 1/1 DataStore | `9b430249-d387-47f7-a544-4d0328bff163` |
| 9 | [`toanim`](https://data.gov.il/dataset/toanim) | רשימת טוענים רבניים | XLSX · 1/1 DataStore | `97df96d1-0c8c-43c1-944b-c5bf1561eb6d` |

### Haifa Municipality
<a id="haifa"></a>
**Slug:** `haifa` · **Hebrew:** עיריית חיפה · **Category:** Municipal · **Datasets:** 9

- Org page: https://data.gov.il/organization/haifa
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:haifa&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`943`](https://data.gov.il/dataset/943) | בתי כנסת בחיפה | XLS · 1/1 DataStore | `29b0e043-706d-47d3-b1b4-b6d57c27c450` |
| 2 | [`944`](https://data.gov.il/dataset/944) | רחובות בחיפה לפי תתי רובע ואזורים סטטיסטיים | XLS · 1/1 DataStore | `260b34b8-0b9d-4c64-99be-0f54634c5bff` |
| 3 | [`945`](https://data.gov.il/dataset/945) | מרכזים קהילתיים בחיפה | XLS · 1/1 DataStore | `691ddc93-07e9-46b7-aadd-76fb4317b034` |
| 4 | [`946`](https://data.gov.il/dataset/946) | גני ילדים עירוניים בחיפה | XLS · 1/1 DataStore | `e0d2197e-fe2e-4a3e-be34-359c0c540367` |
| 5 | [`947`](https://data.gov.il/dataset/947) | בתי מרקחת בחיפה | XLS · 1/1 DataStore | `b4057de6-ece0-4dff-84a5-f9b8ef904434` |
| 6 | [`https-goo-gl-u7v4qv`](https://data.gov.il/dataset/https-goo-gl-u7v4qv) | מיפוי מתקני ספורט בחיפה | XLS · 1/1 DataStore | `32933de9-1e33-4ae5-a99c-699839c8d674` |
| 7 | [`https-www-haifa-muni-il-informationcity-documents-20-20-20-20-20-20-xls`](https://data.gov.il/dataset/https-www-haifa-muni-il-informationcity-documents-20-20-20-20-20-20-xls) | רשימת מדחנים בחיפה לפי רחובות עם חניה יומית/שעתית | XLS | — |
| 8 | [`https-www-haifa-muni-il-informationcity-documents-20-20-20-20-excel-xls`](https://data.gov.il/dataset/https-www-haifa-muni-il-informationcity-documents-20-20-20-20-excel-xls) | אזורי שומה בארנונה חיפה | XLS · 1/1 DataStore | `640536b1-1429-4f44-8678-5c167d3fbd07` |
| 9 | [`https-www-haifa-muni-il-informationcity-pages-databasespublic-aspx`](https://data.gov.il/dataset/https-www-haifa-muni-il-informationcity-pages-databasespublic-aspx) | בתי מלון בחיפה | XLS · 1/1 DataStore | `cd63d130-fcd5-470d-8b86-a39ac1b66bd6` |

### National Digital Agency
<a id="cio"></a>
**Slug:** `cio` · **Hebrew:** מערך הדיגיטל הלאומי · **Category:** Government · **Datasets:** 8

- Org page: https://data.gov.il/organization/cio
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:cio&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`corpus`](https://data.gov.il/dataset/corpus) | קורפוס השפה העברית - תיוג מורפולוגי | CSV · 2/2 DataStore | `10a77ebc-5992-4a5d-b65c-e3a6932d9a0f` |
| 2 | [`datasetlist`](https://data.gov.il/dataset/datasetlist) | מיפוי מאגרי מידע במשרדי הממשלה | CSV/PDF · 1/2 DataStore | `63717ee6-90db-4627-86fe-026a24933249` |
| 3 | [`itgovernance`](https://data.gov.il/dataset/itgovernance) | מבט על תקשוב - תשומות אגפי טכנולוגיות דיגיטליות מידע בממשלה | XLSX · 3/3 DataStore | `f888f077-c85b-471c-b2de-794e446f8813` |
| 4 | [`kiosk`](https://data.gov.il/dataset/kiosk) | עמדות שירות עצמי | CSV · 1/1 DataStore | `11a1072e-d441-4eed-9d3a-f80e6bdb8ca3` |
| 5 | [`labcorpus`](https://data.gov.il/dataset/labcorpus) | תוצרי פיילוט (מעבדה) קורפוס השפה העברית - תיוג מורפולוגי | ?/DOCX/TXT/XLS · 3/8 DataStore | `e857e994-98c8-4b1e-a8cb-9148cae299c0` |
| 6 | [`municipal-authorities`](https://data.gov.il/dataset/municipal-authorities) | רשימה של הרשויות המוניציפאליות - מאוחד | CSV · 1/1 DataStore | `c4916937-f5d3-4295-a22e-88a1af5cde6a` |
| 7 | [`social_economic_cluster`](https://data.gov.il/dataset/social_economic_cluster) | אשכול כלכלי חברתי של מועצות מקומיות ויישובים לשנת 2019 | CSV · 1/1 DataStore | `7c860e04-9f8d-41c2-9f24-6249958d2081` |
| 8 | [`unified`](https://data.gov.il/dataset/unified) | יישובים ומדינות (עברית, אנגלית, ערבית ורוסית) | CSV · 2/2 DataStore | `e9701dcb-9f1c-43bb-bd44-eb380ade542f` |

### Knesset (Parliament)
<a id="knesset"></a>
**Slug:** `knesset` · **Hebrew:** הכנסת · **Category:** Government · **Datasets:** 8

- Org page: https://data.gov.il/organization/knesset
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:knesset&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`547`](https://data.gov.il/dataset/547) | הצעות חוק בכנסת העשרים | — | — |
| 2 | [`548`](https://data.gov.il/dataset/548) | החוקים כפי שנחקקו | — | — |
| 3 | [`549`](https://data.gov.il/dataset/549) | חברי כנסת, ממשלות וסיעות | — | — |
| 4 | [`https-main-knesset-gov-il-activity-legislation-laws-pages-lawlaws-aspx-t-lawlaws-st-lawlaws`](https://data.gov.il/dataset/https-main-knesset-gov-il-activity-legislation-laws-pages-lawlaws-aspx-t-lawlaws-st-lawlaws) | חוקי מדינת ישראל | ? | — |
| 5 | [`my-bills`](https://data.gov.il/dataset/my-bills) | כל הצעות החוק | ? | — |
| 6 | [`odata`](https://data.gov.il/dataset/odata) | מאגר פרלמנטרי נגיש - ODATA | ? | — |
| 7 | [`questions`](https://data.gov.il/dataset/questions) | שאילתות | ? | — |
| 8 | [`vote`](https://data.gov.il/dataset/vote) | הצבעות חברי הכנסת במליאה | — | — |

### Ministry of Social Equality
<a id="socialequality"></a>
**Slug:** `socialequality` · **Hebrew:** המשרד לשוויון חברתי · **Category:** Welfare · **Datasets:** 8

- Org page: https://data.gov.il/organization/socialequality
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:socialequality&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`callkorekitotvatikim`](https://data.gov.il/dataset/callkorekitotvatikim) | קול קורא - כיתות ותיקים | XLSX · 1/1 DataStore | `574ad85f-cb06-4419-8d34-3b5f36e898f4` |
| 2 | [`callkoreyoung`](https://data.gov.il/dataset/callkoreyoung) | קול קורא - רשות הצעירים - תכנית למעורבות חברתית במרכזי צעירים | XLSX | — |
| 3 | [`idg-platform`](https://data.gov.il/dataset/idg-platform) | ישראל דיגיטלית - קול קורא - פלטפורמות רוחביות (תמיכות ברשויות המקומיות) - תקצוב רשויות | XLSX · 1/1 DataStore | `71569373-010c-4519-be01-feefe78fedc1` |
| 4 | [`mhamad-hahisha`](https://data.gov.il/dataset/mhamad-hahisha) | קול קורא - מעמד האישה | XLSX · 1/1 DataStore | `9465b706-33d7-4be3-9528-79a3e7f0bf10` |
| 5 | [`segula`](https://data.gov.il/dataset/segula) | יחידות סגולה - ביקורי מתנדבים והצגת זכויות | XLSX | — |
| 6 | [`senior_card`](https://data.gov.il/dataset/senior_card) | תעודת אזרח ותיק - סך הנפקות | XLSX · 1/1 DataStore | `bca8d6bb-09bb-486e-a494-593c83071ec9` |
| 7 | [`simcha-2017`](https://data.gov.il/dataset/simcha-2017) | מיזם שמחה 2017 - תקצוב רשויות ומספר משתתפים | XLSX · 1/1 DataStore | `109a7312-96dc-407c-93ad-5f275f07b0ea` |
| 8 | [`vatikim`](https://data.gov.il/dataset/vatikim) | קול קורא - וותיקים | XLSX | — |

### Ministry of Energy
<a id="energy_and_water"></a>
**Slug:** `energy_and_water` · **Hebrew:** משרד האנרגיה  · **Category:** Energy · **Datasets:** 7

- Org page: https://data.gov.il/organization/energy_and_water
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:energy_and_water&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`excise`](https://data.gov.il/dataset/excise) | מיסי הדלק (בלו) | XLSX · 1/1 DataStore | `bdce45e7-9fe9-473e-bd51-cef1d787a951` |
| 2 | [`fuelstationbynumber`](https://data.gov.il/dataset/fuelstationbynumber) | מאגר תחנות הדלק | XLSX · 1/1 DataStore | `ff3b653c-d268-4eb7-a86b-6de69e77043a` |
| 3 | [`gas-station`](https://data.gov.il/dataset/gas-station) | רשימת תחנות הדלק הציבוריות כולל מידע גאוגרפי (קואורדינטות במערכת הארצית והעולמית) | XLSX · 1/1 DataStore | `5537a0ef-3eeb-449c-90c8-51e27564f0cb` |
| 4 | [`kriahaziva`](https://data.gov.il/dataset/kriahaziva) | אתרי כרייה וחציבה בישראל | XLSX · 1/1 DataStore | `bcc719c8-3c4d-4ac0-b72a-c26145fe9b08` |
| 5 | [`orl`](https://data.gov.il/dataset/orl) | מחירים תיאורטיים של מוצרי דלק שאינם בפיקוח | XLSX · 1/1 DataStore | `157689c0-69fb-4923-8b27-c780ed64199d` |
| 6 | [`orl-prices`](https://data.gov.il/dataset/orl-prices) | מחירים מחושבים לפי צו פיקוח על מחירי מצרכים ושירותים (מחירים מרביים למוצרי נפט בשער בית זיקוק) | XLSX · 1/1 DataStore | `aaa40832-ac82-4c86-bac6-0d05c83f576f` |
| 7 | [`raw-material-deposits`](https://data.gov.il/dataset/raw-material-deposits) | מרבצי חומרי גלם | ?/DOCX · 2 files | — |

### Israel Employment Service
<a id="ies"></a>
**Slug:** `ies` · **Hebrew:** שירות התעסוקה · **Category:** Labour · **Datasets:** 7

- Org page: https://data.gov.il/organization/ies
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ies&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`e-data-gov-il-dataset-yeshuvmoatzadata`](https://data.gov.il/dataset/e-data-gov-il-dataset-yeshuvmoatzadata) | נתונים חודשיים ברמת יישוב ומועצה אזורית | XLSX · 1/1 DataStore | `08f36575-d5f9-4c99-842c-e3516f34c31c` |
| 2 | [`jobmarketpulse`](https://data.gov.il/dataset/jobmarketpulse) | נתוני דופק שוק העבודה | XLSX · 1/1 DataStore | `50a32c08-be13-4c73-a067-58c47dc41776` |
| 3 | [`jobseekersdata`](https://data.gov.il/dataset/jobseekersdata) | נתוני דורשי עבודה | XLSX · 1/1 DataStore | `3739f4af-9e4b-4502-a904-c7bc14ffa7db` |
| 4 | [`lishkahebrew`](https://data.gov.il/dataset/lishkahebrew) | רשימת לשכות בשירות התעסוקה | XLSX · 2/2 DataStore | `2c499e31-cc80-4415-a6d0-71003305c5bb` |
| 5 | [`populations`](https://data.gov.il/dataset/populations) | נתוני קשת האוכלוסיות | XLSX · 1/1 DataStore | `51fa2ef4-ebd1-463a-923e-63c45a17d71c` |
| 6 | [`statisticsassigningperformance`](https://data.gov.il/dataset/statisticsassigningperformance) | ביצועי שירות התעסוקה - השמות | XLSX · 1/1 DataStore | `1ceed2a7-6e16-49ce-bb22-f2c90def190c` |
| 7 | [`statisticsjobsperformance`](https://data.gov.il/dataset/statisticsjobsperformance) | ביצועי שירות התעסוקה - משרות | XLSX · 1/1 DataStore | `5611e8ec-4688-4635-9582-f6fc778decca` |

### Israel Tax Authority
<a id="taxes-authority"></a>
**Slug:** `taxes-authority` · **Hebrew:** רשות המסים בישראל · **Category:** Finance · **Datasets:** 5

- Org page: https://data.gov.il/organization/taxes-authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:taxes-authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`customs_import_statistics_data`](https://data.gov.il/dataset/customs_import_statistics_data) | נתונים סטטיסטים על יבוא טובין לישראל | CSV · 4/4 DataStore | `80c1e38e-06b9-4a67-b2a4-cc1a76374ee9` |
| 2 | [`customsbook`](https://data.gov.il/dataset/customsbook) | ספר סיווג טובין ביבוא - Israel Customs Book for import | CSV/XLSX · 4/4 DataStore | `c96d99fe-fd3a-4e86-a767-4119dd8b723e` |
| 3 | [`customsbookexport`](https://data.gov.il/dataset/customsbookexport) | ספר סיווג טובין ביצוא - Israel Customs Book for export | XLSX · 2/2 DataStore | `aa292a26-c102-41f9-9ab2-f289298acf37` |
| 4 | [`regularityrequirement`](https://data.gov.il/dataset/regularityrequirement) | דרישות חוקיות - יבוא ויצוא טובין | CSV/JSON · 4/5 DataStore | `a36db570-09f2-4521-8e3d-0290eb839c68` |
| 5 | [`releasespeed`](https://data.gov.il/dataset/releasespeed) | דו"ח מהירות השחרור | CSV · 1/1 DataStore | `761c11e2-4047-4956-89a7-c3b3131aff2b` |

### Israel Meteorological Service
<a id="meteorological_service"></a>
**Slug:** `meteorological_service` · **Hebrew:** השירות המטאורולוגי · **Category:** Weather · **Datasets:** 5

- Org page: https://data.gov.il/organization/meteorological_service
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:meteorological_service&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`1minrain`](https://data.gov.il/dataset/1minrain) | גשם דקתי | CSV/PDF · 84/85 DataStore | `4bf14a6e-a767-41f6-8d66-7d40e17b2e6d` |
| 2 | [`481`](https://data.gov.il/dataset/481) | ארכיון נתונים מטאורולוגיים | CSV/PDF · 7/14 DataStore | `83841660-b9c4-4ecc-a403-d435b3e8c92f` |
| 3 | [`longtermforecast_rain`](https://data.gov.il/dataset/longtermforecast_rain) | נתונים חזויים- גשם | CSV/DOCX · 60/61 DataStore | `4211a220-b991-4c5e-9b65-5f55a5906d5f` |
| 4 | [`max_min_longtermforecast`](https://data.gov.il/dataset/max_min_longtermforecast) | נתונים חזויים- טמפרטורות מינימום ומקסימום | CSV/DOCX · 26/27 DataStore | `25fdc3df-fa72-4fe2-80f7-05ca0f35611e` |
| 5 | [`metadata`](https://data.gov.il/dataset/metadata) | מערך נתונים הומוגניים | CSV/PDF · 3/4 DataStore | `08259129-e1ec-45f2-be1e-f60c2878ddf3` |

### Chief Rabbinate
<a id="rabanot"></a>
**Slug:** `rabanot` · **Hebrew:** הרבנות הראשית לישראל · **Category:** Religion · **Datasets:** 5

- Org page: https://data.gov.il/organization/rabanot
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:rabanot&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`list_of_rabbis_for_kidushin`](https://data.gov.il/dataset/list_of_rabbis_for_kidushin) | רשימת רבנים מוסמכים לעריכת חופות וקידושין | CSV · 1/1 DataStore | `4ed4984a-15c7-4fea-9568-c5183506a418` |
| 2 | [`mazon`](https://data.gov.il/dataset/mazon) | רשימת מוצרי מזון וחומרי גלם מיובאים | CSV · 1/1 DataStore | `4cc6c561-5975-4bac-904f-c06489ceeb6d` |
| 3 | [`mohalim-list`](https://data.gov.il/dataset/mohalim-list) | רשימת מוהלים ארצית | CSV · 1/1 DataStore | `0e526e20-ca57-4ca8-ad6f-2bc5b520824b` |
| 4 | [`orla`](https://data.gov.il/dataset/orla) | רשימת חקלאים ללא חשש פרי ערלה | CSV · 1/1 DataStore | `fff644c8-82de-4642-b343-7802cfb174d9` |
| 5 | [`shovim`](https://data.gov.il/dataset/shovim) | רשימת שוחטים ובודקים | CSV · 1/1 DataStore | `0fc0f3d0-267c-4606-abb9-c53a2aa1afd9` |

### Holocaust Survivors' Rights Authority
<a id="holocaust_survivors_rights"></a>
**Slug:** `holocaust_survivors_rights` · **Hebrew:** הרשות לזכויות ניצולי השואה · **Category:** Welfare · **Datasets:** 5

- Org page: https://data.gov.il/organization/holocaust_survivors_rights
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:holocaust_survivors_rights&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`2024_2025`](https://data.gov.il/dataset/2024_2025) | מועדי מרכזי שירות של הרשות לזכויות ניצולי השואה לחודשים ספטמבר 2024 עד מרץ 2025 | CSV · 1/1 DataStore | `2114d0b8-3af6-4c39-8126-26fbe7f1e1cc` |
| 2 | [`2025-2026`](https://data.gov.il/dataset/2025-2026) | מועדי מרכזי שירות של הרשות לזכויות ניצולי השואה לחודשים אוגוסט 2025 עד מרץ 2026 | CSV · 1/1 DataStore | `b6908861-4f4a-45ea-a9a0-484cb8f68f7f` |
| 3 | [`3-9-2025`](https://data.gov.il/dataset/3-9-2025) | מועדי מרכזי שירות של הרשות לזכויות ניצולי השואה לחודשים מרץ-ספטמבר 2025 | CSV · 1/1 DataStore | `7585710f-fd19-4b51-875f-b55c5ed0a124` |
| 4 | [`bureaus3-9-2024`](https://data.gov.il/dataset/bureaus3-9-2024) | מועדי מרכזי מידע ניידים עדכניים לחודשים מרץ-ספטמבר 2024 | CSV/XLSX · 2/2 DataStore | `82e3db45-51ef-49b5-89cd-50331be3fb7b` |
| 5 | [`holocaust-survivors-right-bureaus`](https://data.gov.il/dataset/holocaust-survivors-right-bureaus) | מרכזי מידע לקבלת קהל - הרשות לזכויות ניצולי השואה | CSV · 1/1 DataStore | `1c7024a4-f24f-4ab0-a012-0477aac27925` |

### Israel Airports Authority
<a id="airport_authority"></a>
**Slug:** `airport_authority` · **Hebrew:** רשות שדות התעופה · **Category:** Aviation · **Datasets:** 4

- Org page: https://data.gov.il/organization/airport_authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:airport_authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`276`](https://data.gov.il/dataset/276) | חנויות ומסעדות בנתב"ג | CSV · 1/1 DataStore | `9cc1be06-79e0-4f9b-b7a6-ad9af1293cc0` |
| 2 | [`278`](https://data.gov.il/dataset/278) | כתובות של שדות תעופה ומעברי גבול | CSV · 1/1 DataStore | `4e8e8c11-5c97-4412-a3fd-1eb862eed668` |
| 3 | [`280`](https://data.gov.il/dataset/280) | סטטיסטיקה מעברי גבול | CSV · 1/1 DataStore | `30663d4f-3f1d-4579-b08e-e72d00650798` |
| 4 | [`flydata`](https://data.gov.il/dataset/flydata) | מאגר טיסות | CSV · 1/1 DataStore | `e83f763b-b7d7-479e-b172-ae981ddc6de5` |

### Israel Police
<a id="israel-police"></a>
**Slug:** `israel-police` · **Hebrew:** משטרת ישראל · **Category:** Public Safety · **Datasets:** 4

- Org page: https://data.gov.il/organization/israel-police
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:israel-police&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`crime_records_data`](https://data.gov.il/dataset/crime_records_data) | נתוני פשיעה | CSV/XLSX · 6/6 DataStore | `b53b64f8-57ed-4213-9191-a7401c0cf436` |
| 2 | [`police_boundaries`](https://data.gov.il/dataset/police_boundaries) | הגבולות המשטרתיים | ZIP | — |
| 3 | [`police_receptions`](https://data.gov.il/dataset/police_receptions) | יחידות מקבלות קהל של משטרת ישראל | CSV · 1/1 DataStore | `848b57bf-362f-4eda-993a-3c74b1feef44` |
| 4 | [`yeshuv_by_station`](https://data.gov.il/dataset/yeshuv_by_station) | שיוך ישובים לתחנות המשטרה | CSV · 1/1 DataStore | `ea5c58c9-5031-4c5e-aed7-f521872f2852` |

### Petah Tikva Municipality
<a id="petah-tikva-municipality"></a>
**Slug:** `petah-tikva-municipality` · **Hebrew:** עיריית פתח תקוה · **Category:** Municipal · **Datasets:** 4

- Org page: https://data.gov.il/organization/petah-tikva-municipality
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:petah-tikva-municipality&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`ownership-of-historic-sites-in-the-city`](https://data.gov.il/dataset/ownership-of-historic-sites-in-the-city) | בעלות על אתרים היסטוריים בעיר פתח תקווה | XLSX | — |
| 2 | [`report-assignment-streets-regions`](https://data.gov.il/dataset/report-assignment-streets-regions) | דו''ח שיוך רחובות לאזורים עיריית פתח תקווה | XLS · 1/1 DataStore | `4cfb39a3-9124-4af3-8719-777e8abc945c` |
| 3 | [`schools`](https://data.gov.il/dataset/schools) | בתי ספר בעיר פתח תקווה | XLSX | — |
| 4 | [`synagogues`](https://data.gov.il/dataset/synagogues) | בתי כנסת בעיר פתח תקווה | XLSX · 1/1 DataStore | `b10bb9e1-7100-464e-a6cf-b2115d20f709` |

### Enforcement & Collection Authority
<a id="eca"></a>
**Slug:** `eca` · **Hebrew:** רשות האכיפה והגבייה · **Category:** Justice · **Datasets:** 4

- Org page: https://data.gov.il/organization/eca
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:eca&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`stat2017`](https://data.gov.il/dataset/stat2017) | דו"ח שנתי 2017 | CSV · 10/23 DataStore | `0f09f420-5bec-44af-b29d-d23026d36c78` |
| 2 | [`stat2018`](https://data.gov.il/dataset/stat2018) | דו"ח שנתי 2018 | CSV · 1/1 DataStore | `d593216b-6c1c-43d7-bae6-9620af2cf47d` |
| 3 | [`statreport2016-eca`](https://data.gov.il/dataset/statreport2016-eca) | דו"ח שנתי 2016 | XLSX · 17/24 DataStore | `6ee77f09-2096-464a-a951-354abb05eba2` |
| 4 | [`tables`](https://data.gov.il/dataset/tables) | טבלאות של רשות האכיפה והגביה | CSV · 17/17 DataStore | `3e0dfe1e-6b69-4bb7-8e33-0f8f58a00f5b` |

### Judicial Authority (Courts)
<a id="the_judicial_authority"></a>
**Slug:** `the_judicial_authority` · **Hebrew:** הרשות השופטת · **Category:** Justice · **Datasets:** 3

- Org page: https://data.gov.il/organization/the_judicial_authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:the_judicial_authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`city-court`](https://data.gov.il/dataset/city-court) | רשימת יישובים בחלוקה למחוזות שיפוט | XLSX · 1/1 DataStore | `d80b564a-91d1-4b4c-9fe3-c4023f754031` |
| 2 | [`court-lost`](https://data.gov.il/dataset/court-lost) | מאגר בתי משפט ובתי דין לעבודה | XLSX · 1/1 DataStore | `5f8cff43-30fb-449b-96b1-280b2aafb2c3` |
| 3 | [`magistrate-court-list`](https://data.gov.il/dataset/magistrate-court-list) | בתי משפט השלום בחלוקה למחוזות | XLSX · 1/1 DataStore | `fe80edf2-991f-4e38-b132-55091d5fb70d` |

### Israel Land Authority
<a id="the_israel_lands_administration"></a>
**Slug:** `the_israel_lands_administration` · **Hebrew:** רשות מקרקעי ישראל · **Category:** Land · **Datasets:** 3

- Org page: https://data.gov.il/organization/the_israel_lands_administration
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:the_israel_lands_administration&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`housingunits-planning-inventory`](https://data.gov.il/dataset/housingunits-planning-inventory) | מלאי תכנוני למגורים | DOCX/XLS/ZIP · 1/3 DataStore | `99aad98f-2b54-4eea-834d-650b56389bf3` |
| 2 | [`service-space`](https://data.gov.il/dataset/service-space) | מרחבי השירות של רשות מקרקעי ישראל | XLSX · 1/1 DataStore | `fd84b0cb-8f7a-4321-ae00-a6c8daa79707` |
| 3 | [`surveyers`](https://data.gov.il/dataset/surveyers) | מאגר מודדים | XLSX · 1/1 DataStore | `ae20b319-e45e-4702-88be-3a2f4773cdf3` |

### Ministry of National Security
<a id="ministry_of_internal_security"></a>
**Slug:** `ministry_of_internal_security` · **Hebrew:** המשרד לביטחון הפנים · **Category:** Public Safety · **Datasets:** 3

- Org page: https://data.gov.il/organization/ministry_of_internal_security
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:ministry_of_internal_security&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`https-www-gov-il-he-departments-general-traffic-enforcement-cameras`](https://data.gov.il/dataset/https-www-gov-il-he-departments-general-traffic-enforcement-cameras) | מצלמות אכיפה (א-3) | ?/XLSX · 2 files | — |
| 2 | [`https-www-gov-il-he-departments-guides-police-vehicle-confiscation-chapterindex-2`](https://data.gov.il/dataset/https-www-gov-il-he-departments-guides-police-vehicle-confiscation-chapterindex-2) | מגרשי החנייה לרכבים מושבתים | XLSX · 1/1 DataStore | `bc95a2c9-f734-47c5-8b7d-a6490481dd1f` |
| 3 | [`mops-gov-il`](https://data.gov.il/dataset/mops-gov-il) | מחקרי המדען הראשי | XLSX | — |

### Volcani Agricultural Research
<a id="volcaniagri"></a>
**Slug:** `volcaniagri` · **Hebrew:** מינהל המחקר החקלאי - מרכז וולקני · **Category:** Agriculture · **Datasets:** 3

- Org page: https://data.gov.il/organization/volcaniagri
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:volcaniagri&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`pathogenicity`](https://data.gov.il/dataset/pathogenicity) | רשימת פתוגנים המועברים ע"י זרעים (פטריות, חיידקים ווירוסים) הנבדקים במעבדה | XLS · 1/1 DataStore | `3aa9c756-db7e-4148-b1c9-0f4d020a5e99` |
| 2 | [`plants-garden`](https://data.gov.il/dataset/plants-garden) | צמחי גן ונוי | ? | — |
| 3 | [`species`](https://data.gov.il/dataset/species) | רשימת הזנים המורשים למכירה | PDF | — |

### GOV.IL (general)
<a id="gov-il"></a>
**Slug:** `gov-il` · **Hebrew:** GOV · **Category:** Government · **Datasets:** 2

- Org page: https://data.gov.il/organization/gov-il
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:gov-il&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`internallist`](https://data.gov.il/dataset/internallist) | רשימה פנימית | XLSX · 1/1 DataStore | `40023209-2964-4874-bc32-bd7fb1a40f35` |
| 2 | [`travelwarnings`](https://data.gov.il/dataset/travelwarnings) | אזהרות מסע | XLSX · 1/1 DataStore | `2a01d234-b2b0-4d46-baa0-cec05c401e7d` |

### Civil Service Commission
<a id="netzivot"></a>
**Slug:** `netzivot` · **Hebrew:** נציבות שירות המדינה · **Category:** Government · **Datasets:** 2

- Org page: https://data.gov.il/organization/netzivot
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:netzivot&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`ogdan-education`](https://data.gov.il/dataset/ogdan-education) | אוגדן השכלות  - לצורך בדיקת תנאי סף השכלה במכרזי כ"א בשירות המדינה | CSV · 1/1 DataStore | `9d656232-3329-4e41-bd6f-a793644b4ea6` |
| 2 | [`recruitment`](https://data.gov.il/dataset/recruitment) | נתוני גיוס עובדים לשירות המדינה | XLSX · 1/1 DataStore | `009fd03b-17fd-4958-83a9-25f256ca3fb6` |

### Regulatory Affairs Authority
<a id="regulatory-authority"></a>
**Slug:** `regulatory-authority` · **Hebrew:** רשות האסדרה · **Category:** Government · **Datasets:** 2

- Org page: https://data.gov.il/organization/regulatory-authority
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:regulatory-authority&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`ease-of-regulation`](https://data.gov.il/dataset/ease-of-regulation) | חרבות ברזל - הקלות והתאמות ברגולציה ממשרדי הממשלה | XLSX · 1/1 DataStore | `5e228e05-59bf-4153-8ae8-20bec420c575` |
| 2 | [`regulationdatabase`](https://data.gov.il/dataset/regulationdatabase) | מאגר האסדרה- Regulation Database | XLSX · 1/1 DataStore | `929b4c60-ce43-4f5b-9960-f6146ba33eed` |

### Rural Education Administration
<a id="rural-education"></a>
**Slug:** `rural-education` · **Hebrew:** המינהל לחינוך התיישבותי · **Category:** Education · **Datasets:** 2

- Org page: https://data.gov.il/organization/rural-education
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:rural-education&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`mchp-boarding-schools`](https://data.gov.il/dataset/mchp-boarding-schools) | פנימיות חינוכיות במינהל לחינוך התיישבותי | CSV · 4/4 DataStore | `4771ed41-9a28-46fb-8ced-f0846cc88b19` |
| 2 | [`mchp-regional-schools`](https://data.gov.il/dataset/mchp-regional-schools) | בתי ספר איזוריים בפיקוח המינהל לחינוך התיישבותי | CSV · 4/4 DataStore | `cf910eda-c929-46d6-b98b-7da531a41db1` |

### Synthetic / test data
<a id="synthetic"></a>
**Slug:** `synthetic` · **Hebrew:** מידע סינתטי ממשלתי · **Category:** Other · **Datasets:** 2

- Org page: https://data.gov.il/organization/synthetic
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:synthetic&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`bankconfirmation`](https://data.gov.il/dataset/bankconfirmation) | מאגר דוגמאות סינתטיות של אישורי ניהול חשבון בנק | ZIP · 10 files | — |
| 2 | [`paycheck`](https://data.gov.il/dataset/paycheck) | מאגר דוגמאות של תלושי שכר סינתטים | ZIP · 60 files | — |

### Central Elections Committee (Knesset)
<a id="central-election-committee"></a>
**Slug:** `central-election-committee` · **Hebrew:** ועדת הבחירות המרכזית לכנסת · **Category:** Elections · **Datasets:** 2

- Org page: https://data.gov.il/organization/central-election-committee
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:central-election-committee&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`candidates-lists`](https://data.gov.il/dataset/candidates-lists) | רשימות המועמדים לכנסת - ועדת הבחירות המרכזית לכנסת | XLSX · 6/6 DataStore | `9162e35c-8834-422c-9202-ed42faf4a9f9` |
| 2 | [`votes-knesset`](https://data.gov.il/dataset/votes-knesset) | תוצאות בחירות - ועדת הבחירות המרכזית לכנסת | CSV/XLS · 17/17 DataStore | `b392b8ee-ba45-4ea0-bfed-f03a1a36e99c` |

### Israel State Archives
<a id="archives"></a>
**Slug:** `archives` · **Hebrew:** ארכיון המדינה · **Category:** Government · **Datasets:** 2

- Org page: https://data.gov.il/organization/archives
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:archives&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`archives-yco`](https://data.gov.il/dataset/archives-yco) | ארכיון פרשת ילדי תימן ואחרים | DOCX/XLSX/ZIP · 2/4 DataStore | `a2d230db-83d7-4fd9-9ffe-5f5924f29d1f` |
| 2 | [`israel-state-archives-catalog`](https://data.gov.il/dataset/israel-state-archives-catalog) | קטלוג התיקים של ארכיון המדינה | CSV · 1/1 DataStore | `1296c3cd-0cb6-47a3-8ca9-e3af6e774681` |

### Government Procurement Administration
<a id="governmentprocurementadministration"></a>
**Slug:** `governmentprocurementadministration` · **Hebrew:** מינהל הרכש הממשלתי · **Category:** Government · **Datasets:** 2

- Org page: https://data.gov.il/organization/governmentprocurementadministration
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:governmentprocurementadministration&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`exemptions`](https://data.gov.il/dataset/exemptions) | דוח התקשרויות בפטור והליכים תחרותיים | CSV · 1/1 DataStore | `65c8fced-c50c-400e-94fb-ef1a208c43e5` |
| 2 | [`tenders`](https://data.gov.il/dataset/tenders) | דוח מכרזים | CSV · 1/1 DataStore | `7038b3e6-a74d-442e-b16b-466c8196124a` |

### Nativ (Liaison Bureau)
<a id="nativ"></a>
**Slug:** `nativ` · **Hebrew:** משרד ראש הממשלה, "נתיב" · **Category:** Government · **Datasets:** 1

- Org page: https://data.gov.il/organization/nativ
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:nativ&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`nativ`](https://data.gov.il/dataset/nativ) | יחידות של משרד ראש הממשלה - נתיב | CSV · 1/1 DataStore | `14e40280-fea8-421c-96f7-e3f1a6949dbf` |

### Israel National Cyber Directorate
<a id="israel_national_cyber_directorate"></a>
**Slug:** `israel_national_cyber_directorate` · **Hebrew:** מערך הסייבר הלאומי · **Category:** Cyber · **Datasets:** 1

- Org page: https://data.gov.il/organization/israel_national_cyber_directorate
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:israel_national_cyber_directorate&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`cybermarketplace`](https://data.gov.il/dataset/cybermarketplace) | מרקטפלייס - פתרונות הגנת סייבר | CSV · 1/1 DataStore | `338b04a0-82d2-4366-9877-22e6d2698f10` |

### National Road Safety Authority
<a id="betihut-drahim"></a>
**Slug:** `betihut-drahim` · **Hebrew:** הרשות הלאומית לבטיחות בדרכים · **Category:** Transport · **Datasets:** 1

- Org page: https://data.gov.il/organization/betihut-drahim
- API list: `https://data.gov.il/api/3/action/package_search?fq=organization:betihut-drahim&rows=1000`

| # | Dataset (slug) | Hebrew title | Resources | DataStore resource id (first) |
| ---: | --- | --- | --- | --- |
| 1 | [`486`](https://data.gov.il/dataset/486) | מגמות בבטיחות בדרכים 2005-2011 | XLS/XLSX · 4/9 DataStore | `519d46d5-7d82-4b6b-b838-1e9e427541ca` |

---

## Notes & caveats
- **Language:** Dataset titles, descriptions, tags, and column headers in resource files are predominantly Hebrew. URL slugs are usually English transliterations or keywords. There is no official English catalogue — this index is a third-party derivation.
- **Geo-restriction:** Many `*.gov.il` *web* properties geo-fence outside Israel, but the `data.gov.il` CKAN API and the `download/datafile.csv` resource URLs were directly reachable during this snapshot from .il. If blocked elsewhere, route via an Israeli egress (Cloudflare WARP set to IL, an IL VPS, or `claude-in-chrome`/Playwright with an IL session).
- **Staleness:** This snapshot is point-in-time. The catalogue grows ~weekly. Re-pull with the script in this folder to refresh; resource UUIDs are stable but new resources/datasets are added.
- **Licensing:** Most datasets are published under the Israeli government open-data terms — verify per-dataset (`license_id`, `license_title` in `package_show`) before redistribution.
