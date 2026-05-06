# Israel-Open-Data-Resources

An index of open-source repositories, datasets, and APIs related to Israeli open data — government catalogues, scrapers, parsers, MCP servers, and downstream utilities.

This is a sibling to [Israeli Open Source Projects](https://github.com/danielrosehill/Israeli-Open-Source-Projects). Where that repo casts a wide net across Israeli open-source work, this one focuses specifically on **open data** — government catalogues, statistical APIs, scrapers and parsers for public datasets, and MCP servers that wrap them.

*Last updated: 2026-05-06*

## Contents

- [Catalogue snapshots](#catalogue-snapshots)
- [Government & data.gov.il tooling](#government--datagovil-tooling)
- [Statistics (CBS)](#statistics-cbs)
- [Knesset, Elections & Judicial](#knesset-elections--judicial)
- [Banking & Personal Finance](#banking--personal-finance)
- [Real Estate — Nadlan, Yad2, Madlan](#real-estate--nadlan-yad2-madlan)
- [Mortgages & Housing Calculators](#mortgages--housing-calculators)
- [Supermarket Prices](#supermarket-prices)
- [Health](#health)
- [Energy & Environment](#energy--environment)
- [Transport & Aviation](#transport--aviation)
- [Public Safety & Civil Defence](#public-safety--civil-defence)
- [Geospatial & Land](#geospatial--land)
- [Currency & FX](#currency--fx)
- [Civic & General](#civic--general)
- [Datasets on Hugging Face](#datasets-on-hugging-face)
- [APIs](#apis)
- [Contributing](#contributing)

---

## Catalogue snapshots

Point-in-time imports of the [data.gov.il](https://data.gov.il) CKAN catalogue with an English index, organisation breakdown by category, and a translation mapping (Hebrew → English) keyed by dataset slug. Refresh with `./import-catalogue.sh`.

| Snapshot | Datasets | Orgs | Index |
|---|---:|---:|---|
| [`060526/`](./060526/) (2026-05-06) | 1,194 | 61 | [English README](./060526/README.md) |

---

## Government & data.gov.il tooling

| Project | Description | Stars |
|---|---|---|
| [Datagov MCP](https://github.com/aviveldan/datagov-mcp) | MCP server for data.gov.il | ![](https://img.shields.io/github/stars/aviveldan/datagov-mcp?style=social) |
| [Data.gov.il MCP](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp) | MCP server for data.gov.il | ![](https://img.shields.io/github/stars/DavidOsherdiagnostica/data-gov-il-mcp?style=social) |
| [Data.gov.il MCP](https://github.com/eyalkatzaf/data-gov-il-mcp) | MCP server for data.gov.il | ![](https://img.shields.io/github/stars/eyalkatzaf/data-gov-il-mcp?style=social) |
| [Data Israel](https://github.com/LiorVainer/data-israel) | Israeli data utilities | ![](https://img.shields.io/github/stars/LiorVainer/data-israel?style=social) |
| [Skills-IL MCPs](https://github.com/skills-il/mcps) | MCP servers for Israeli data sources | ![](https://img.shields.io/github/stars/skills-il/mcps?style=social) |
| [Skills-IL Government Services](https://github.com/skills-il/government-services) | Israeli government services skills | ![](https://img.shields.io/github/stars/skills-il/government-services?style=social) |
| [Skills-IL Tax & Finance](https://github.com/skills-il/tax-and-finance) | Israeli tax & finance skills (mas rechisha etc.) | ![](https://img.shields.io/github/stars/skills-il/tax-and-finance?style=social) |
| [Databricks Gov Data App](https://github.com/Shaked-Gal/Databricks-Gov-Data-App) | Databricks app over Israeli government data | ![](https://img.shields.io/github/stars/Shaked-Gal/Databricks-Gov-Data-App?style=social) |
| [UP360 MCP](https://github.com/eliko86/up360mcp) | UP360 MCP server | ![](https://img.shields.io/github/stars/eliko86/up360mcp?style=social) |

## Statistics (CBS)

| Project | Description | Stars |
|---|---|---|
| [Israel Statistics MCP](https://github.com/reuvenaor/israel-statistics-mcp) | CBS data via MCP | ![](https://img.shields.io/github/stars/reuvenaor/israel-statistics-mcp?style=social) |
| [Israeli CBS MCP](https://github.com/amirrosi/israeli-cbs-mcp) | Israeli CBS data MCP server | ![](https://img.shields.io/github/stars/amirrosi/israeli-cbs-mcp?style=social) |
| [Israstat Explorer](https://github.com/romanzarkhin/israstat-explorer) | Israeli statistics explorer | ![](https://img.shields.io/github/stars/romanzarkhin/israstat-explorer?style=social) |
| [il.cbs.muni (R)](https://github.com/cran/il.cbs.muni) | R package for CBS municipal data | ![](https://img.shields.io/github/stars/cran/il.cbs.muni?style=social) |
| [EconFin Functions](https://github.com/107SBakst/econfin_functions) | Israeli econ/finance helper functions | ![](https://img.shields.io/github/stars/107SBakst/econfin_functions?style=social) |
| [Calcala Israel](https://github.com/idanmev/calcala-israel) | Israeli economics content site | ![](https://img.shields.io/github/stars/idanmev/calcala-israel?style=social) |

## Knesset, Elections & Judicial

| Project | Description | Stars |
|---|---|---|
| [Knesset Refactor](https://github.com/AT020993/knesset_refactor) | Knesset (parliament) data refactor | ![](https://img.shields.io/github/stars/AT020993/knesset_refactor?style=social) |
| [Knessy](https://github.com/amnir/knessy) | Knesset data utility | ![](https://img.shields.io/github/stars/amnir/knessy?style=social) |
| [Knesset Data Vote](https://github.com/moshelati/knesset-data-vote) | Knesset voting data | ![](https://img.shields.io/github/stars/moshelati/knesset-data-vote?style=social) |
| [Knesset Committees PM](https://github.com/zomer-g/Knesset_Committees_PM) | Knesset committees project management data | ![](https://img.shields.io/github/stars/zomer-g/Knesset_Committees_PM?style=social) |
| [Supreme Court](https://github.com/zomer-g/Supreme-Court) | Israeli Supreme Court data | ![](https://img.shields.io/github/stars/zomer-g/Supreme-Court?style=social) |
| [ILSC Data](https://github.com/jschler/ILSC_Data) | Israeli Supreme Court data | ![](https://img.shields.io/github/stars/jschler/ILSC_Data?style=social) |
| [Israel Elections Data Analysis](https://github.com/AriehA1995/israel-elections-data-analysis) | Israeli elections data analysis | ![](https://img.shields.io/github/stars/AriehA1995/israel-elections-data-analysis?style=social) |

## Banking & Personal Finance

| Project | Description | Stars |
|---|---|---|
| [Israeli Bank Scrapers](https://github.com/eshaham/israeli-bank-scrapers) | Canonical Israeli bank scrapers (banks + cards) | ![](https://img.shields.io/github/stars/eshaham/israeli-bank-scrapers?style=social) |
| [Israeli Bank Scrapers Modern Schemas](https://github.com/Urigo/israeli-bank-scrapers-modern-schemas) | Modern Bank Hapoalim schemas | ![](https://img.shields.io/github/stars/Urigo/israeli-bank-scrapers-modern-schemas?style=social) |
| [Asher MCP](https://github.com/shlomiuziel/asher-mcp) | MCP over israeli-bank-scrapers | ![](https://img.shields.io/github/stars/shlomiuziel/asher-mcp?style=social) |
| [IL Bank MCP](https://github.com/glekner/il-bank-mcp) | Israeli bank MCP server | ![](https://img.shields.io/github/stars/glekner/il-bank-mcp?style=social) |
| [Israeli Bank MCP](https://github.com/mottibec/israeli-bank-mcp) | Israeli bank MCP server | ![](https://img.shields.io/github/stars/mottibec/israeli-bank-mcp?style=social) |
| [Moneyman](https://github.com/daniel-hauser/moneyman) | Bank-scrape aggregator with pluggable storage | ![](https://img.shields.io/github/stars/daniel-hauser/moneyman?style=social) |
| [Caspion](https://github.com/brafdlog/caspion) | Personal-finance app with bank scrape | ![](https://img.shields.io/github/stars/brafdlog/caspion?style=social) |
| [ShekelSync](https://github.com/AvnerAdda/shekelsync) | Electron desktop finance tracker | ![](https://img.shields.io/github/stars/AvnerAdda/shekelsync?style=social) |
| [Israeli Finance Scraper](https://github.com/orzarchi/israeli-finance-scraper) | Israeli finance scraper | ![](https://img.shields.io/github/stars/orzarchi/israeli-finance-scraper?style=social) |
| [Israeli YNAB Updater](https://github.com/eshaham/israeli-ynab-updater) | YNAB updater for Israeli accounts | ![](https://img.shields.io/github/stars/eshaham/israeli-ynab-updater?style=social) |
| [Israeli Banks → Actual Budget Importer](https://github.com/tomerh2001/israeli-banks-actual-budget-importer) | Actual Budget importer | ![](https://img.shields.io/github/stars/tomerh2001/israeli-banks-actual-budget-importer?style=social) |
| [Israeli Bank Scrapers → Actual Budget](https://github.com/sergienko4/israeli-bank-scrapers-to-actual-budget) | Bank scrapers → Actual Budget | ![](https://img.shields.io/github/stars/sergienko4/israeli-bank-scrapers-to-actual-budget?style=social) |
| [Finparse](https://github.com/shustinm/finparse) | Bank scrapers → Firefly III | ![](https://img.shields.io/github/stars/shustinm/finparse?style=social) |
| [Cheshbeshbon](https://github.com/ohadbarr1/cheshbeshbon) | Israeli bookkeeping | ![](https://img.shields.io/github/stars/ohadbarr1/cheshbeshbon?style=social) |
| [Nudlers](https://github.com/enudler/nudlers) | Personal finance (scope unclear) | ![](https://img.shields.io/github/stars/enudler/nudlers?style=social) |
| [Cashpilot](https://github.com/danielcashpilot/cashpilot) | Generic cashflow tool | ![](https://img.shields.io/github/stars/danielcashpilot/cashpilot?style=social) |

## Real Estate — Nadlan, Yad2, Madlan

| Project | Description | Stars |
|---|---|---|
| [Israel Nadlan Data](https://github.com/AdanimInstitue/israel-nadlan-data) | Israeli real-estate (Nadlan) dataset | ![](https://img.shields.io/github/stars/AdanimInstitue/israel-nadlan-data?style=social) |
| [Israel Nadlan Data Collector](https://github.com/AdanimInstitue/israel-nadlan-data-collector) | Collector for Israeli real-estate (Nadlan) data | ![](https://img.shields.io/github/stars/AdanimInstitue/israel-nadlan-data-collector?style=social) |
| [Nadlan Skill](https://github.com/IsraelZablianov/nadlan-skill) | Wraps nadlan.gov.il transaction history | ![](https://img.shields.io/github/stars/IsraelZablianov/nadlan-skill?style=social) |
| [Nadlan MCP](https://github.com/nitzpo/nadlan-mcp) | MCP server for nadlan.gov.il | ![](https://img.shields.io/github/stars/nitzpo/nadlan-mcp?style=social) |
| [Gov Nadlan Fetcher](https://github.com/jmpfar/gov-nadlan-fetcher) | Wraps nadlan.gov.il internal JSON endpoints | ![](https://img.shields.io/github/stars/jmpfar/gov-nadlan-fetcher?style=social) |
| [NadlanAI](https://github.com/Exitiumverum/NadlanAI) | Nadlan AI tool | ![](https://img.shields.io/github/stars/Exitiumverum/NadlanAI?style=social) |
| [Yad2 Scraper](https://github.com/NivEz/yad2-scraper) | Yad2 listings scraper | ![](https://img.shields.io/github/stars/NivEz/yad2-scraper?style=social) |
| [Yad2 Listings](https://github.com/TamirMa/yad2listings) | Yad2 listings on a graph | ![](https://img.shields.io/github/stars/TamirMa/yad2listings?style=social) |
| [Yad2 RSS](https://github.com/almog/yad2) | RSS feed over yad2.co.il | ![](https://img.shields.io/github/stars/almog/yad2?style=social) |
| [Yad2 Clipboard](https://github.com/dplesh/yad2clipboard) | Copy Yad2 nadlan post to clipboard | ![](https://img.shields.io/github/stars/dplesh/yad2clipboard?style=social) |
| [Yad2 Semantic Search](https://github.com/poovarasan011/yad2-semantic-search) | Semantic search over Yad2 listings | ![](https://img.shields.io/github/stars/poovarasan011/yad2-semantic-search?style=social) |
| [DiraAi](https://github.com/Idantall/DiraAi) | Madlan-style listings browser | ![](https://img.shields.io/github/stars/Idantall/DiraAi?style=social) |
| [Israel Housing Finder](https://github.com/TCyberChef/israel-housing-finder) | Israel housing finder | ![](https://img.shields.io/github/stars/TCyberChef/israel-housing-finder?style=social) |
| [Find Apartments](https://github.com/cxt9/find-apartments) | Apartment finder | ![](https://img.shields.io/github/stars/cxt9/find-apartments?style=social) |
| [Israel Housing Price Prediction](https://github.com/shualilaw1-commits/israel-housing-price-prediction) | Israel housing price prediction | ![](https://img.shields.io/github/stars/shualilaw1-commits/israel-housing-price-prediction?style=social) |
| [Real-Estate Prediction ML](https://github.com/mosegorge/Real-estate-prediction-machine-learning) | Real-estate price prediction ML | ![](https://img.shields.io/github/stars/mosegorge/Real-estate-prediction-machine-learning?style=social) |
| [Hebrew RAG Real-Estate](https://github.com/oshritmau/hebrew-rag-realestate) | Hebrew RAG over real-estate data | ![](https://img.shields.io/github/stars/oshritmau/hebrew-rag-realestate?style=social) |
| [Diralottery](https://github.com/ddark-il/diralottery) | Dira BeHanaha (Mehir Lamishtaken) lottery tracker | ![](https://img.shields.io/github/stars/ddark-il/diralottery?style=social) |

## Mortgages & Housing Calculators

| Project | Description | Stars |
|---|---|---|
| [Mashkanta](https://github.com/ndor/mashkanta) | Israeli mortgage optimisation | ![](https://img.shields.io/github/stars/ndor/mashkanta?style=social) |
| [Rent or Buy](https://github.com/erezs1234/rent-or-buy) | Hebrew rent-vs-mortgage calculator | ![](https://img.shields.io/github/stars/erezs1234/rent-or-buy?style=social) |
| [Israeli Mortgage Calculator](https://github.com/aaron-a-d/israeli-mortgage-calculator) | Israeli mortgage calculator | ![](https://img.shields.io/github/stars/aaron-a-d/israeli-mortgage-calculator?style=social) |
| [MyMortgage](https://github.com/noybi642-yarin/MyMortgage) | Mortgage calculator | ![](https://img.shields.io/github/stars/noybi642-yarin/MyMortgage?style=social) |
| [Mortgage Calculator Site](https://github.com/oados112/mortgage-calculator-site) | Mortgage calculator site | ![](https://img.shields.io/github/stars/oados112/mortgage-calculator-site?style=social) |
| [Mashkanta Pro](https://github.com/tuvalgueta/Mashkanta-Pro) | Israeli mortgage calculator | ![](https://img.shields.io/github/stars/tuvalgueta/Mashkanta-Pro?style=social) |
| [MashkantaAI](https://github.com/Baruchhanya/MashkantaAI) | AI-assisted mortgage tool | ![](https://img.shields.io/github/stars/Baruchhanya/MashkantaAI?style=social) |
| [Mashkanta 2](https://github.com/amitre/Mashkanta2) | Israeli mortgage calculator | ![](https://img.shields.io/github/stars/amitre/Mashkanta2?style=social) |
| [Mashkanta (RGproj)](https://github.com/RGproj/Mashkanta) | Israeli mortgage calculator | ![](https://img.shields.io/github/stars/RGproj/Mashkanta?style=social) |
| [Smart Mortgage Calculator](https://github.com/NISANH66/Smart-Mortgage-Calculator) | Smart mortgage calculator | ![](https://img.shields.io/github/stars/NISANH66/Smart-Mortgage-Calculator?style=social) |
| [Sayeret Calculator](https://github.com/roy-aniccai/Sayeret-Calculator) | Mortgage qualification calculator | ![](https://img.shields.io/github/stars/roy-aniccai/Sayeret-Calculator?style=social) |

## Supermarket Prices

| Project | Description | Stars |
|---|---|---|
| [Israeli Supermarket Scrapers](https://github.com/OpenIsraeliSupermarkets/israeli-supermarket-scarpers) | Scrapers for Israeli supermarket price data | ![](https://img.shields.io/github/stars/OpenIsraeliSupermarkets/israeli-supermarket-scarpers?style=social) |
| [Israeli Supermarket Parsers](https://github.com/OpenIsraeliSupermarkets/israeli-supermarket-parsers) | Parsers for Israeli supermarket price data | ![](https://img.shields.io/github/stars/OpenIsraeliSupermarkets/israeli-supermarket-parsers?style=social) |
| [PricyAPI](https://github.com/tomereliel0/PricyAPI) | Price-data API | ![](https://img.shields.io/github/stars/tomereliel0/PricyAPI?style=social) |

## Health

| Project | Description | Stars |
|---|---|---|
| [Israel Doctor Data](https://github.com/MatanEcon/israel-doctor-data) | Israeli physicians dataset | ![](https://img.shields.io/github/stars/MatanEcon/israel-doctor-data?style=social) |
| [COVID-19 Vaccine Efficacy](https://github.com/ecampau/COVID-19-Vaccine-Efficacy) | COVID-19 vaccine efficacy analysis (incl. Israeli data) | ![](https://img.shields.io/github/stars/ecampau/COVID-19-Vaccine-Efficacy?style=social) |

## Energy & Environment

| Project | Description | Stars |
|---|---|---|
| [Israel Energy Data](https://github.com/nzo-heschel/israel-energy-data) | Israeli energy sector data | ![](https://img.shields.io/github/stars/nzo-heschel/israel-energy-data?style=social) |
| [Land Cover Classification](https://github.com/DeanZigdon/land_cover_classification) | Land cover classification (Israel) | ![](https://img.shields.io/github/stars/DeanZigdon/land_cover_classification?style=social) |

## Transport & Aviation

| Project | Description | Stars |
|---|---|---|
| [Airport Data Pipeline](https://github.com/Ofigu/airport-data-pipeline) | Israeli airport data pipeline | ![](https://img.shields.io/github/stars/Ofigu/airport-data-pipeline?style=social) |
| [Migdal Garage Project](https://github.com/rachelbak/MigdalGarageProject) | Migdal Garage project | ![](https://img.shields.io/github/stars/rachelbak/MigdalGarageProject?style=social) |

## Public Safety & Civil Defence

| Project | Description | Stars |
|---|---|---|
| [Israel Alerts Data](https://github.com/dleshem/israel-alerts-data) | Israeli alerts (Pikud HaOref) historical data | ![](https://img.shields.io/github/stars/dleshem/israel-alerts-data?style=social) |
| [Israel Shelters Database](https://github.com/dev-symbol/Israel-Shelters-Databas) | Israel public shelters database | ![](https://img.shields.io/github/stars/dev-symbol/Israel-Shelters-Databas?style=social) |

## Geospatial & Land

| Project | Description | Stars |
|---|---|---|
| [Israel Geolocation](https://github.com/akivaschiff/israel-geolocation) | Israel geolocation utilities | ![](https://img.shields.io/github/stars/akivaschiff/israel-geolocation?style=social) |
| [Land Hunter](https://github.com/bengurevich1danyel/land-hunter) | Parcel tracking, plan monitoring, spatial | ![](https://img.shields.io/github/stars/bengurevich1danyel/land-hunter?style=social) |

## Currency & FX

| Project | Description | Stars |
|---|---|---|
| [Exchange Rate Tracker](https://github.com/Avigail3648/Exchange-rate-tracker) | Exchange rate tracker | ![](https://img.shields.io/github/stars/Avigail3648/Exchange-rate-tracker?style=social) |
| [Currency Exchange Rates](https://github.com/attogram/currency-exchange-rates) | Currency exchange rates dataset | ![](https://img.shields.io/github/stars/attogram/currency-exchange-rates?style=social) |

## Civic & General

| Project | Description | Stars |
|---|---|---|
| [Ocal](https://github.com/zomer-g/ocal) | Open calendar / civic data | ![](https://img.shields.io/github/stars/zomer-g/ocal?style=social) |
| [Urban Guardian MCP](https://github.com/GaryShnol/urban-guardian-mcp) | Urban / civic MCP (zoning, permits) | ![](https://img.shields.io/github/stars/GaryShnol/urban-guardian-mcp?style=social) |

## Datasets on Hugging Face

| Dataset | Description |
|---|---|
| [danielrosehill/Jerusalem-Air-Quality-Shabbat](https://huggingface.co/datasets/danielrosehill/Jerusalem-Air-Quality-Shabbat) | Jerusalem air-quality readings on Shabbat — derived from Israeli environmental monitoring data. |

## APIs

| API | Description | Endpoint / Notes |
|---|---|---|
| **data.gov.il (CKAN)** | National open-data portal — 1,194 datasets, 61 publishing orgs. No English titles in API; see `060526/` for the English index. | [`/api/3/action/package_search`](https://data.gov.il/api/3/action/package_search?rows=5) · [docs in snapshot](./060526/README.md#api-endpoints) |
| **CBS House Price Index** | Central Bureau of Statistics index catalog | [api.cbs.gov.il/Index/Catalog/Catalog?lang=en](https://api.cbs.gov.il/Index/Catalog/Catalog?lang=en) |
| **Nadlan.gov.il** | Israeli real-estate transactions — no official API; community wrappers exist (see Nadlan repos above) | https://www.nadlan.gov.il/ |

## Contributing

PRs welcome — add additional Israeli open-data repositories, datasets, or APIs to the relevant category above. To refresh the data.gov.il snapshot, run `./import-catalogue.sh`.

---

# Related Indexes

| Index | Description |
|---|---|
| [Israeli Open Source Projects](https://github.com/danielrosehill/Israeli-Open-Source-Projects) | Wider index of Israeli open-source projects — civic tech, finance, careers, real estate, smart home, media. |
| [Israel Projects Index](https://github.com/danielrosehill/Israel-Projects-Index) | Master index of Israel-related repositories, datasets, and Hugging Face spaces. |
| [Israeli AI Tools & Ecosystem](https://github.com/danielrosehill/Israeli-AI-Tools-And-Ecosystem) | AI-native projects: agents, agent skills, MCP servers, Hebrew-language resources, communities, ecosystem map. |
