# Israel-Open-Data-Resources

An index of open-source repositories, datasets, and APIs related to Israeli open data — government catalogues, scrapers, parsers, MCP servers, and downstream utilities.

This is a sibling to [Israeli Open Source Projects](https://github.com/danielrosehill/Israeli-Open-Source-Projects). Where that repo casts a wide net across Israeli open-source work, this one focuses specifically on **open data** — government catalogues, statistical APIs, scrapers and parsers for public datasets, and MCP servers that wrap them.

*Last updated: 2026-10-17*

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
- [Budget & Public Spending](#budget--public-spending)
- [Weather & Climate](#weather--climate)
- [Datasets on Hugging Face](#datasets-on-hugging-face)
- [APIs](#apis)
- [Research reports](#research-reports)
- [Contributing](#contributing)

---

## Catalogue snapshots

Point-in-time imports of the [data.gov.il](https://data.gov.il) CKAN catalogue with an English index, organisation breakdown by category, and a translation mapping (Hebrew → English) keyed by dataset slug. Refresh with `./import-catalogue.sh`.

| Snapshot | Datasets | Orgs | Index |
|---|---:|---:|---|
| [`060526/`](./060526/) (2026-05-06) | 1,194 | 61 | [English README](./060526/README.md) |
| [`pdf-catalogue/`](./pdf-catalogue/) (2026-05-06) | 1,194 | 60 | 659-page bilingual PDF + raw JSON + sample rows |

### Companion artefacts

| Artefact | Where | Notes |
|---|---|---|
| Bilingual PDF catalogue | [HuggingFace dataset](https://huggingface.co/datasets/danielrosehill/Israel-Open-Data-Catalogue) | Date-stamped snapshot folders with PDF, raw CKAN JSON, samples, and translations |
| Translation mapping (HE↔EN) | [Israel-Open-Data-Catalogue-Translations](https://github.com/danielrosehill/Israel-Open-Data-Catalogue-Translations) | Standalone repo — drop-in `translations.json` keyed by dataset slug, MIT-licensed |
| GitHub release with all assets | [snapshot-2026-05-06](https://github.com/danielrosehill/Israel-Open-Data-Resources/releases/tag/snapshot-2026-05-06) | PDF + JSON downloads attached |
| Addition history by month | [Israel-Open-Data-Changelog](https://github.com/danielrosehill/Israel-Open-Data-Changelog) | What the portal added and when, reconstructed from `metadata_created` — one folder per month, 2015-12 onward. Where snapshots here are point-in-time, that repo is the diff over time |

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
| [DataCity CKAN DGP](https://github.com/hasadna/datacity-ckan-dgp) | Automation loading Israeli municipal datasets into DataCity CKAN | ![](https://img.shields.io/github/stars/hasadna/datacity-ckan-dgp?style=social) |
| [GovScraper (Letz HaMimshal)](https://github.com/zomer-g/letz-hamimshal-extension) | Browser extension bulk-downloading open datasets from gov.il | ![](https://img.shields.io/github/stars/zomer-g/letz-hamimshal-extension?style=social) |

## Statistics (CBS)

| Project | Description | Stars |
|---|---|---|
| [Israel Statistics MCP](https://github.com/reuvenaor/israel-statistics-mcp) | CBS data via MCP | ![](https://img.shields.io/github/stars/reuvenaor/israel-statistics-mcp?style=social) |
| [Israeli CBS MCP](https://github.com/amirrosi/israeli-cbs-mcp) | Israeli CBS data MCP server | ![](https://img.shields.io/github/stars/amirrosi/israeli-cbs-mcp?style=social) |
| [Israstat Explorer](https://github.com/romanzarkhin/israstat-explorer) | Israeli statistics explorer | ![](https://img.shields.io/github/stars/romanzarkhin/israstat-explorer?style=social) |
| [il.cbs.muni (R)](https://github.com/cran/il.cbs.muni) | R package for CBS municipal data | ![](https://img.shields.io/github/stars/cran/il.cbs.muni?style=social) |
| [EconFin Functions](https://github.com/107SBakst/econfin_functions) | Israeli econ/finance helper functions | ![](https://img.shields.io/github/stars/107SBakst/econfin_functions?style=social) |

## Knesset, Elections & Judicial

| Project | Description | Stars |
|---|---|---|
| [Knessy](https://github.com/amnir/knessy) | Knesset data utility | ![](https://img.shields.io/github/stars/amnir/knessy?style=social) |
| [Knesset Data Vote](https://github.com/moshelati/knesset-data-vote) | Knesset voting data | ![](https://img.shields.io/github/stars/moshelati/knesset-data-vote?style=social) |
| [Knesset Committees PM](https://github.com/zomer-g/Knesset_Committees_PM) | Knesset committees project management data | ![](https://img.shields.io/github/stars/zomer-g/Knesset_Committees_PM?style=social) |
| [Supreme Court](https://github.com/zomer-g/Supreme-Court) | Israeli Supreme Court data | ![](https://img.shields.io/github/stars/zomer-g/Supreme-Court?style=social) |
| [ILSC Data](https://github.com/jschler/ILSC_Data) | Israeli Supreme Court data | ![](https://img.shields.io/github/stars/jschler/ILSC_Data?style=social) |
| [Israel Elections Data Analysis](https://github.com/AriehA1995/israel-elections-data-analysis) | Israeli elections data analysis | ![](https://img.shields.io/github/stars/AriehA1995/israel-elections-data-analysis?style=social) |
| [Knesset Data Pipelines](https://github.com/hasadna/knesset-data-pipelines) | Open Knesset's main scrapers and processing pipelines | ![](https://img.shields.io/github/stars/hasadna/knesset-data-pipelines?style=social) |
| [knesset-data-python](https://github.com/hasadna/knesset-data-python) | Python module for API access to Knesset data | ![](https://img.shields.io/github/stars/hasadna/knesset-data-python?style=social) |
| [Knesset MCP](https://github.com/zohar/knesset-mcp) | MCP server over the Knesset OData API | ![](https://img.shields.io/github/stars/zohar/knesset-mcp?style=social) |
| [Knesset Corpus](https://github.com/HaifaCLG/KnessetCorpus) | Annotated corpus of Knesset committee and plenum protocols | ![](https://img.shields.io/github/stars/HaifaCLG/KnessetCorpus?style=social) |
| [OpenLaw Bot](https://github.com/hasadna/openlaw-bot) | Hasadna bot maintaining an up-to-date open book of Israeli laws | ![](https://img.shields.io/github/stars/hasadna/openlaw-bot?style=social) |
| [Israeli Elections Analyzer](https://github.com/amiram/Elections) | Knesset election results by ballot box and locality | ![](https://img.shields.io/github/stars/amiram/Elections?style=social) |

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
| [Open Pension](https://github.com/hasadna/open_pension) | Parses and exposes Israeli pension-fund holdings | ![](https://img.shields.io/github/stars/hasadna/open_pension?style=social) |
| [Israeli Bank Scrapers Desktop](https://github.com/baruchiro/israeli-bank-scrapers-desktop) | Desktop app fetching Israeli bank and card transactions | ![](https://img.shields.io/github/stars/baruchiro/israeli-bank-scrapers-desktop?style=social) |
| [Scipio](https://github.com/t0mer/scipio) | Self-hosted REST API around israeli-bank-scrapers | ![](https://img.shields.io/github/stars/t0mer/scipio?style=social) |
| [Israeli Banks SimpleFIN Bridge](https://github.com/tomerh2001/israeli-banks-simplefin-bridge) | SimpleFIN bridge feeding Israeli bank data into budgeting apps | ![](https://img.shields.io/github/stars/tomerh2001/israeli-banks-simplefin-bridge?style=social) |

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
| [DiraAi](https://github.com/Idantall/DiraAi) | Madlan-style listings browser | ![](https://img.shields.io/github/stars/Idantall/DiraAi?style=social) |
| [Israel Housing Finder](https://github.com/TCyberChef/israel-housing-finder) | Israel housing finder | ![](https://img.shields.io/github/stars/TCyberChef/israel-housing-finder?style=social) |
| [Find Apartments](https://github.com/cxt9/find-apartments) | Apartment finder | ![](https://img.shields.io/github/stars/cxt9/find-apartments?style=social) |
| [Israel Housing Price Prediction](https://github.com/shualilaw1-commits/israel-housing-price-prediction) | Israel housing price prediction | ![](https://img.shields.io/github/stars/shualilaw1-commits/israel-housing-price-prediction?style=social) |
| [Real-Estate Prediction ML](https://github.com/mosegorge/Real-estate-prediction-machine-learning) | Real-estate price prediction ML | ![](https://img.shields.io/github/stars/mosegorge/Real-estate-prediction-machine-learning?style=social) |
| [Hebrew RAG Real-Estate](https://github.com/oshritmau/hebrew-rag-realestate) | Hebrew RAG over real-estate data | ![](https://img.shields.io/github/stars/oshritmau/hebrew-rag-realestate?style=social) |
| [Diralottery](https://github.com/ddark-il/diralottery) | Dira BeHanaha (Mehir Lamishtaken) lottery tracker | ![](https://img.shields.io/github/stars/ddark-il/diralottery?style=social) |
| [Mitar Urban Renewal Israel](https://github.com/AlonDrilich/mitar-urban-renewal-israel) | Urban renewal (pinui-binui, TAMA 38) by city: projects, approvals and planned units from Planning Administration and Urban Renewal Authority records, CC BY 4.0 | ![](https://img.shields.io/github/stars/AlonDrilich/mitar-urban-renewal-israel?style=social) |

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
| [Israeli Supermarket Data](https://github.com/AKorets/israeli-supermarket-data) | Collected supermarket price-transparency data | ![](https://img.shields.io/github/stars/AKorets/israeli-supermarket-data?style=social) |
| [fluhus/prices](https://github.com/fluhus/prices) | Go tool collecting and parsing supermarket price files | ![](https://img.shields.io/github/stars/fluhus/prices?style=social) |

## Health

| Project | Description | Stars |
|---|---|---|
| [Israel Doctor Data](https://github.com/MatanEcon/israel-doctor-data) | Israeli physicians dataset | ![](https://img.shields.io/github/stars/MatanEcon/israel-doctor-data?style=social) |
| [COVID-19 Vaccine Efficacy](https://github.com/ecampau/COVID-19-Vaccine-Efficacy) | COVID-19 vaccine efficacy analysis (incl. Israeli data) | ![](https://img.shields.io/github/stars/ecampau/COVID-19-Vaccine-Efficacy?style=social) |
| [Israel COVID-19 Data](https://github.com/idandrd/israel-covid19-data) | Charts and data on COVID-19 spread in Israel | ![](https://img.shields.io/github/stars/idandrd/israel-covid19-data?style=social) |

## Energy & Environment

| Project | Description | Stars |
|---|---|---|
| [Israel Energy Data](https://github.com/nzo-heschel/israel-energy-data) | Israeli energy sector data | ![](https://img.shields.io/github/stars/nzo-heschel/israel-energy-data?style=social) |
| [Land Cover Classification](https://github.com/DeanZigdon/land_cover_classification) | Land cover classification (Israel) | ![](https://img.shields.io/github/stars/DeanZigdon/land_cover_classification?style=social) |
| [WAQI Stations Israel](https://github.com/danielrosehill/WAQI-Stations-Israel) | Static snapshot of WAQI air-quality reporting points in Israel | ![](https://img.shields.io/github/stars/danielrosehill/WAQI-Stations-Israel?style=social) |
| [Israel Municipal Waste Dashboard](https://github.com/adina-paley/waste-dashboard) | Per-authority recycling and landfill figures | ![](https://img.shields.io/github/stars/adina-paley/waste-dashboard?style=social) |

## Transport & Aviation

| Project | Description | Stars |
|---|---|---|
| [Airport Data Pipeline](https://github.com/Ofigu/airport-data-pipeline) | Israeli airport data pipeline | ![](https://img.shields.io/github/stars/Ofigu/airport-data-pipeline?style=social) |
| [Migdal Garage Project](https://github.com/rachelbak/MigdalGarageProject) | Migdal Garage project | ![](https://img.shields.io/github/stars/rachelbak/MigdalGarageProject?style=social) |
| [Open Bus Map Search](https://github.com/hasadna/open-bus-map-search) | Hasadna site showing Israeli bus performance, gaps and routes from SIRI/GTFS data | ![](https://img.shields.io/github/stars/hasadna/open-bus-map-search?style=social) |
| [Open Bus](https://github.com/hasadna/open-bus) | Hasadna's original analysis of Israel's public transport data | ![](https://img.shields.io/github/stars/hasadna/open-bus?style=social) |
| [Open Bus Pipelines](https://github.com/hasadna/open-bus-pipelines) | Airflow pipelines collecting Israeli bus SIRI/GTFS data for Stride | ![](https://img.shields.io/github/stars/hasadna/open-bus-pipelines?style=social) |
| [Open Bus Stride API](https://github.com/hasadna/open-bus-stride-api) | REST API serving Stride's historical Israeli public-transport data | ![](https://img.shields.io/github/stars/hasadna/open-bus-stride-api?style=social) |
| [Open Bus Stride Client](https://github.com/hasadna/open-bus-stride-client) | Python client and notebooks for the Stride bus-data API | ![](https://img.shields.io/github/stars/hasadna/open-bus-stride-client?style=social) |
| [OpenTrain Community](https://github.com/hasadna/OpenTrainCommunity) | Community analysis of Israel Railways train delay data | ![](https://img.shields.io/github/stars/hasadna/OpenTrainCommunity?style=social) |
| [Better Rail](https://github.com/better-rail/app) | Open-source alternative client for Israel Railways timetables and live data | ![](https://img.shields.io/github/stars/better-rail/app?style=social) |
| [ANYWAY](https://github.com/data-for-change/anyway) | Road accidents and fatalities map and platform (originally a Hasadna project) | ![](https://img.shields.io/github/stars/data-for-change/anyway?style=social) |
| [Israel Public Transport API](https://github.com/benyaming/israel-public-transport-api) | Python wrapper for Ministry of Transport real-time SIRI data | ![](https://img.shields.io/github/stars/benyaming/israel-public-transport-api?style=social) |
| [NextTrain Israel Tooling](https://github.com/sergenes/next-train-israel-tooling) | SQLite database of Israel Railways timetable data and build tooling | ![](https://img.shields.io/github/stars/sergenes/next-train-israel-tooling?style=social) |

## Public Safety & Civil Defence

| Project | Description | Stars |
|---|---|---|
| [Israel Alerts Data](https://github.com/dleshem/israel-alerts-data) | Israeli alerts (Pikud HaOref) historical data | ![](https://img.shields.io/github/stars/dleshem/israel-alerts-data?style=social) |
| [Israel Shelters Database](https://github.com/dev-symbol/Israel-Shelters-Databas) | Israel public shelters database | ![](https://img.shields.io/github/stars/dev-symbol/Israel-Shelters-Databas?style=social) |
| [Oref Alert (Home Assistant)](https://github.com/amitfin/oref_alert) | Home Assistant integration for Pikud HaOref alerts | ![](https://img.shields.io/github/stars/amitfin/oref_alert?style=social) |
| [pikud-haoref-api](https://github.com/eladnava/pikud-haoref-api) | Node.js wrapper for Pikud HaOref's unofficial alert API | ![](https://img.shields.io/github/stars/eladnava/pikud-haoref-api?style=social) |
| [python-red-alert](https://github.com/Zontex/python-red-alert) | Python client for the Pikud HaOref alert API | ![](https://img.shields.io/github/stars/Zontex/python-red-alert?style=social) |
| [Redalert (MQTT)](https://github.com/t0mer/Redalert) | Red alert monitor publishing Pikud HaOref alerts to MQTT | ![](https://img.shields.io/github/stars/t0mer/Redalert?style=social) |
| [Oref Alerts Proxy](https://github.com/dmatik/oref-alerts-proxy-ms) | Spring Boot microservice proxying Pikud HaOref alerts | ![](https://img.shields.io/github/stars/dmatik/oref-alerts-proxy-ms?style=social) |
| [Pikud HaOref GraphQL API](https://github.com/TuvalSimha/pikud-haoref-api-graphql) | GraphQL API over Pikud HaOref alert history | ![](https://img.shields.io/github/stars/TuvalSimha/pikud-haoref-api-graphql?style=social) |
| [Awesome Red Alerts](https://github.com/danielrosehill/Awesome-Red-Alerts) | Curated list of red alert (Tzeva Adom) notification projects | ![](https://img.shields.io/github/stars/danielrosehill/Awesome-Red-Alerts?style=social) |
| [Miklat MCP Data](https://github.com/danielrosehill/Miklat-MCP-Data) | Data pipeline for the Miklat (shelters) MCP server | ![](https://img.shields.io/github/stars/danielrosehill/Miklat-MCP-Data?style=social) |
| [JLM Shelters Data](https://github.com/danielrosehill/jlm-shelters-data) | Community dataset of Jerusalem public bomb shelters (jlmshelters.com) | ![](https://img.shields.io/github/stars/danielrosehill/jlm-shelters-data?style=social) |
| [Iran–Israel War 2026 OSINT Data](https://github.com/danielrosehill/Iran-Israel-War-2026-OSINT-Data) | Structured data on Iranian aerial attacks on Israel and others, 2024–present | ![](https://img.shields.io/github/stars/danielrosehill/Iran-Israel-War-2026-OSINT-Data?style=social) |

## Geospatial & Land

| Project | Description | Stars |
|---|---|---|
| [Israel Geolocation](https://github.com/akivaschiff/israel-geolocation) | Israel geolocation utilities | ![](https://img.shields.io/github/stars/akivaschiff/israel-geolocation?style=social) |
| [Land Hunter](https://github.com/bengurevich1danyel/land-hunter) | Parcel tracking, plan monitoring, spatial | ![](https://img.shields.io/github/stars/bengurevich1danyel/land-hunter?style=social) |
| [QGIS Israeli Open Data](https://github.com/KaplanOpenSource/qgis-open-data) | QGIS plugin adding Israeli open spatial data layers | ![](https://img.shields.io/github/stars/KaplanOpenSource/qgis-open-data?style=social) |
| [Israel Municipalities Polygons](https://github.com/idoivri/israel-municipalities-polygons) | GeoJSON boundary polygons for Israeli municipalities | ![](https://img.shields.io/github/stars/idoivri/israel-municipalities-polygons?style=social) |
| [Israeli Cities and Streets List](https://github.com/GabMic/israeli-cities-and-streets-list) | JSON list of every Israeli city and street name | ![](https://img.shields.io/github/stars/GabMic/israeli-cities-and-streets-list?style=social) |

## Currency & FX

| Project | Description | Stars |
|---|---|---|
| [Exchange Rate Tracker](https://github.com/Avigail3648/Exchange-rate-tracker) | Exchange rate tracker | ![](https://img.shields.io/github/stars/Avigail3648/Exchange-rate-tracker?style=social) |
| [Currency Exchange Rates](https://github.com/attogram/currency-exchange-rates) | Currency exchange rates dataset | ![](https://img.shields.io/github/stars/attogram/currency-exchange-rates?style=social) |
| [BOI Exchange Rates](https://github.com/Gugulator/boi_exchange_rates) | Home Assistant integration for Bank of Israel exchange rates | ![](https://img.shields.io/github/stars/Gugulator/boi_exchange_rates?style=social) |

## Civic & General

| Project | Description | Stars |
|---|---|---|
| [Ocal](https://github.com/zomer-g/ocal) | Open calendar / civic data | ![](https://img.shields.io/github/stars/zomer-g/ocal?style=social) |
| [Urban Guardian MCP](https://github.com/GaryShnol/urban-guardian-mcp) | Urban / civic MCP (zoning, permits) | ![](https://img.shields.io/github/stars/GaryShnol/urban-guardian-mcp?style=social) |

## Budget & Public Spending

| Project | Description | Stars |
|---|---|---|
| [BudgetKey (Open Budget)](https://github.com/OpenBudget/BudgetKey) | Main repo of the Open Budget project opening the Israeli state budget | ![](https://img.shields.io/github/stars/OpenBudget/BudgetKey?style=social) |
| [BudgetKey Data Pipelines](https://github.com/OpenBudget/budgetkey-data-pipelines) | Pipelines ingesting budget, procurement, supports and entity data | ![](https://img.shields.io/github/stars/OpenBudget/budgetkey-data-pipelines?style=social) |
| [BudgetKey MCP](https://github.com/OpenBudget/budgetkey-mcp) | MCP server exposing Open Budget data to LLM agents | ![](https://img.shields.io/github/stars/OpenBudget/budgetkey-mcp?style=social) |
| [OpenMuni Budgets](https://github.com/hasadna/openmuni-budgets) | Web app and API for comparing Israeli municipal budgets | ![](https://img.shields.io/github/stars/hasadna/openmuni-budgets?style=social) |
| [Arnona Israel](https://github.com/mikey641/arnona-israel) | Dataset, API and scraper of municipal Arnona (property tax) rates per m² | ![](https://img.shields.io/github/stars/mikey641/arnona-israel?style=social) |

## Weather & Climate

| Project | Description | Stars |
|---|---|---|
| [IMS Home Assistant Component](https://github.com/GuyKh/ims-custom-component) | Israel Meteorological Service integration for Home Assistant | ![](https://img.shields.io/github/stars/GuyKh/ims-custom-component?style=social) |
| [py-weatheril](https://github.com/t0mer/py-weatheril) | Python wrapper for IMS current weather, forecasts and radar | ![](https://img.shields.io/github/stars/t0mer/py-weatheril?style=social) |
| [israel-weather-rs](https://github.com/barakplasma/israel-weather-rs) | Rust parser turning IMS forecast XML into structs and JSON | ![](https://img.shields.io/github/stars/barakplasma/israel-weather-rs?style=social) |

## Datasets on Hugging Face

| Dataset | Description |
|---|---|
| [danielrosehill/Jerusalem-Air-Quality-Shabbat](https://huggingface.co/datasets/danielrosehill/Jerusalem-Air-Quality-Shabbat) | Jerusalem air-quality readings on Shabbat — derived from Israeli environmental monitoring data. |
| [HaifaCLGroup/KnessetCorpus](https://huggingface.co/datasets/HaifaCLGroup/KnessetCorpus) | Annotated Knesset plenum and committee protocols with metadata |
| [ZeAlenu/knesset-data](https://huggingface.co/datasets/ZeAlenu/knesset-data) | Knesset OData API tables exported to sharded JSONL, CC-BY-SA |
| [ivrit-ai/knesset-plenums](https://huggingface.co/datasets/ivrit-ai/knesset-plenums) | Plenum audio/video aligned with official protocols (ivrit.ai) (gated (auto-approve)) |
| [LevMuchnik/SupremeCourtOfIsrael](https://huggingface.co/datasets/LevMuchnik/SupremeCourtOfIsrael) | 2022 snapshot of Supreme Court public verdicts with metadata |
| [gkour/israeli_law](https://huggingface.co/datasets/gkour/israeli_law) | Statutes, regulations and orders from Hebrew Wikisource |
| [kjhq/Israel-Stock-Symbols-and-Metadata](https://huggingface.co/datasets/kjhq/Israel-Stock-Symbols-and-Metadata) | Symbols and metadata for TASE-listed companies |
| [gtfintechlab/bank_of_israel](https://huggingface.co/datasets/gtfintechlab/bank_of_israel) | Annotated BOI monetary-policy communications (hawkish/dovish) |
| [danielrosehill/Israel-Alerting-Zones](https://huggingface.co/datasets/danielrosehill/Israel-Alerting-Zones) | Pikud HaOref alerting zones (Hebrew names as used by the HFC) |
| [danielrosehill/Jerusalem-Emergency-Shelters-0925](https://huggingface.co/datasets/danielrosehill/Jerusalem-Emergency-Shelters-0925) | Jerusalem public shelter locations, September 2025 |
| [danielrosehill/Iran-Israel-War-2026](https://huggingface.co/datasets/danielrosehill/Iran-Israel-War-2026) | OSINT dataset of Iranian missile and drone attack waves |

## APIs

| API | Description | Endpoint / Notes |
|---|---|---|
| **data.gov.il (CKAN)** | National open-data portal — 1,194 datasets, 61 publishing orgs. No English titles in API; see `060526/` for the English index. | [`/api/3/action/package_search`](https://data.gov.il/api/3/action/package_search?rows=5) · [docs in snapshot](./060526/README.md#api-endpoints) |
| **CBS House Price Index** | Central Bureau of Statistics index catalog | [api.cbs.gov.il/Index/Catalog/Catalog?lang=en](https://api.cbs.gov.il/Index/Catalog/Catalog?lang=en) |
| **Nadlan.gov.il** | Israeli real-estate transactions — no official API; community wrappers exist (see Nadlan repos above) | https://www.nadlan.gov.il/ |
| **Bank of Israel Series Database (SDMX)** | BOI statistical series (FX, interest, etc.) via SDMX v2 REST; CSV/XML | [`edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BO…`](https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/EXR/1.0/RER_USD_ILS?startperiod=2026-10-01&format=csv) |
| **Bank of Israel Public API — exchange rates** | Current representative exchange rates, JSON | [`boi.org.il/PublicApi/GetExchangeRates`](https://boi.org.il/PublicApi/GetExchangeRates) |
| **CBS Series API** | CBS time-series catalogue and data (population, trade, energy…), JSON/XML | [`apis.cbs.gov.il/series/catalog/level?id=1&format=json&dow…`](https://apis.cbs.gov.il/series/catalog/level?id=1&format=json&download=false) |
| **CBS Price Index data API** | CPI and other price-index values by index code, JSON | [`api.cbs.gov.il/index/data/price?id=120010&format=json&dow…`](https://api.cbs.gov.il/index/data/price?id=120010&format=json&download=false&last=1) |
| **Knesset OData API (v4)** | Knesset KNS_* tables (MKs, bills, committees, votes), JSON | [`knesset.gov.il/OdataV4/ParliamentInfo/KNS_KnessetDates?$t…`](https://knesset.gov.il/OdataV4/ParliamentInfo/KNS_KnessetDates?$top=1) |
| **Ministry of Transport GTFS** | National static GTFS feed plus tariff and zone files | [`gtfs.mot.gov.il/gtfsfiles/`](https://gtfs.mot.gov.il/gtfsfiles/) |
| **Ministry of Transport SIRI (real-time)** | Real-time bus arrivals, SIRI Stop Monitoring; registration required | [`www.gov.il/he/Departments/General/real_time_information_siri`](https://www.gov.il/he/Departments/General/real_time_information_siri) |
| **Open Bus Stride API (Hasadna)** | Historical SIRI + GTFS archive with REST API (NGO-run) | [`open-bus-stride-api.hasadna.org.il/docs`](https://open-bus-stride-api.hasadna.org.il/docs) |
| **IMS city forecasts (XML)** | Israel Meteorological Service city forecast feed, no token | [`ims.gov.il/sites/default/files/ims_data/xml_files/isr_cit…`](https://ims.gov.il/sites/default/files/ims_data/xml_files/isr_cities.xml) |
| **IMS Envista observations API** | 10-minute station observations; token from IMS | [`api.ims.gov.il/v1/envista/stations`](https://api.ims.gov.il/v1/envista/stations) |
| **MoEP air quality (Envista) API** | Air-monitoring stations and readings; token required | [`air-api.sviva.gov.il/v1/envista/stations`](https://air-api.sviva.gov.il/v1/envista/stations) |
| **Pikud HaOref live alerts** | Home Front Command current-alert JSON | [`www.oref.org.il/WarningMessages/alert/alerts.json`](https://www.oref.org.il/WarningMessages/alert/alerts.json) |
| **Pikud HaOref alert history** | Historical alerts by locality, JSON | [`alerts-history.oref.org.il/Shared/Ajax/GetAlarmsHistory.a…`](https://alerts-history.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx?lang=he&mode=3) |
| **GovMap API** | National map portal API: JS/URL functions, search, layer IDs | [`api.govmap.gov.il/docs/intro`](https://api.govmap.gov.il/docs/intro) |
| **iplan ArcGIS REST** | Planning Administration public planning layers | [`ags.iplan.gov.il/arcgisiplan/rest/services?f=json`](https://ags.iplan.gov.il/arcgisiplan/rest/services?f=json) |
| **Israel Land Authority tenders (Michrazim)** | Land tender search API behind the Michrazim site | [`apps.land.gov.il/MichrazimSite/api/SearchApi/Search`](https://apps.land.gov.il/MichrazimSite/api/SearchApi/Search) |
| **Open Budget SQL API** | State budget, procurement and supports via SQL query, JSON/CSV | [`next.obudget.org/api/query?query=select%20count(*)%20from…`](https://next.obudget.org/api/query?query=select%20count(*)%20from%20budget) |
| **Noga (Israel ISO) consumption data** | Annual and hourly national electricity consumption downloads | [`www.noga-iso.co.il/en/statistics/annual-hourly-consumptio…`](https://www.noga-iso.co.il/en/statistics/annual-hourly-consumption-data/) |
| **TASE Data Hub** | Tel Aviv Stock Exchange market-data API (API key; some free endpoints) | [`datahub.tase.co.il/`](https://datahub.tase.co.il/) |
| **Tel Aviv-Yafo Open Data** | Municipal open-data catalogue; managed APIs need a developer key | [`opendata.tel-aviv.gov.il/`](https://opendata.tel-aviv.gov.il/) |
| **Tel Aviv GIS (ArcGIS REST)** | Municipal GIS layers (IView2 MapServer) | [`gisn.tel-aviv.gov.il/arcgis/rest/services/IView2/MapServe…`](https://gisn.tel-aviv.gov.il/arcgis/rest/services/IView2/MapServer?f=json) |
| **Haifa Open Data (CKAN)** | Haifa municipal CKAN: accidents, budget, businesses… | [`opendata.haifa.muni.il/api/3/action/package_list`](https://opendata.haifa.muni.il/api/3/action/package_list) |
| **Jerusalem DataCity (CKAN)** | Jerusalem municipal datasets on Hasadna's DataCity platform | [`jerusalem.datacity.org.il/api/3/action/package_list`](https://jerusalem.datacity.org.il/api/3/action/package_list) |
| **Midaat LaAm / odata.org.il (CKAN)** | Civil-society CKAN of FOI and NGO-sourced public data | [`www.odata.org.il/api/3/action/organization_list`](https://www.odata.org.il/api/3/action/organization_list) |
| **Ministry of Health data dashboard** | MoH dashboards (corona and others) | [`datadashboard.health.gov.il/portal/dashboard/corona`](https://datadashboard.health.gov.il/portal/dashboard/corona) |
| **Reshumot (official gazette)** | Ministry of Justice official publications | [`reshumot.justice.gov.il/`](https://reshumot.justice.gov.il/) |

## Research reports

| Date | Report | Notes |
|---|---|---|
| 2026-10-17 | [`reports/171026/findings.pdf`](./reports/171026/findings.pdf) · [JSON](./reports/171026/findings.json) | Every entry A–Z with description, link and verification findings. Research by Claude Opus 5.5; initial repositories found by Daniel Rosehill. Three dead repos removed; CBS APIs refused all routes on the day. |

## Contributing

PRs welcome — add additional Israeli open-data repositories, datasets, or APIs to the relevant category above. To refresh the data.gov.il snapshot, run `./import-catalogue.sh`.

---

# Related Indexes

| Index | Description |
|---|---|
| [Israeli Open Source Projects](https://github.com/danielrosehill/Israeli-Open-Source-Projects) | Wider index of Israeli open-source projects — civic tech, finance, careers, real estate, smart home, media. |
| [Israel Projects Index](https://github.com/danielrosehill/Israel-Projects-Index) | Master index of Israel-related repositories, datasets, and Hugging Face spaces. |
| [Israeli AI Tools & Ecosystem](https://github.com/danielrosehill/Israeli-AI-Tools-And-Ecosystem) | AI-native projects: agents, agent skills, MCP servers, Hebrew-language resources, communities, ecosystem map. |
