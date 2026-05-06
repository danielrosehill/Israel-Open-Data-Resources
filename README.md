# Israel-Open-Data-Resources

A curated index of open-source repositories, datasets, and APIs related to Israeli open data — government catalogues, scrapers, parsers, MCP servers, and downstream utilities.

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

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [aviveldan/datagov-mcp](https://github.com/aviveldan/datagov-mcp) | MCP server for data.gov.il | ![Stars](https://img.shields.io/github/stars/aviveldan/datagov-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/aviveldan/datagov-mcp) |
| [DavidOsherdiagnostica/data-gov-il-mcp](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp) | MCP server for data.gov.il | ![Stars](https://img.shields.io/github/stars/DavidOsherdiagnostica/data-gov-il-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/DavidOsherdiagnostica/data-gov-il-mcp) |
| [eyalkatzaf/data-gov-il-mcp](https://github.com/eyalkatzaf/data-gov-il-mcp) | MCP server for data.gov.il | ![Stars](https://img.shields.io/github/stars/eyalkatzaf/data-gov-il-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/eyalkatzaf/data-gov-il-mcp) |
| [LiorVainer/data-israel](https://github.com/LiorVainer/data-israel) | Israeli data utilities | ![Stars](https://img.shields.io/github/stars/LiorVainer/data-israel?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/LiorVainer/data-israel) |
| [skills-il/mcps](https://github.com/skills-il/mcps) | MCP servers for Israeli data sources | ![Stars](https://img.shields.io/github/stars/skills-il/mcps?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/skills-il/mcps) |
| [skills-il/government-services](https://github.com/skills-il/government-services) | Israeli government services skills | ![Stars](https://img.shields.io/github/stars/skills-il/government-services?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/skills-il/government-services) |
| [skills-il/tax-and-finance](https://github.com/skills-il/tax-and-finance) | Israeli tax & finance skills (mas rechisha etc.) | ![Stars](https://img.shields.io/github/stars/skills-il/tax-and-finance?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/skills-il/tax-and-finance) |
| [Shaked-Gal/Databricks-Gov-Data-App](https://github.com/Shaked-Gal/Databricks-Gov-Data-App) | Databricks app over Israeli government data | ![Stars](https://img.shields.io/github/stars/Shaked-Gal/Databricks-Gov-Data-App?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Shaked-Gal/Databricks-Gov-Data-App) |
| [eliko86/up360mcp](https://github.com/eliko86/up360mcp) | UP360 MCP server | ![Stars](https://img.shields.io/github/stars/eliko86/up360mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/eliko86/up360mcp) |

## Statistics (CBS)

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [reuvenaor/israel-statistics-mcp](https://github.com/reuvenaor/israel-statistics-mcp) | CBS data via MCP | ![Stars](https://img.shields.io/github/stars/reuvenaor/israel-statistics-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/reuvenaor/israel-statistics-mcp) |
| [amirrosi/israeli-cbs-mcp](https://github.com/amirrosi/israeli-cbs-mcp) | Israeli CBS data MCP server | ![Stars](https://img.shields.io/github/stars/amirrosi/israeli-cbs-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/amirrosi/israeli-cbs-mcp) |
| [romanzarkhin/israstat-explorer](https://github.com/romanzarkhin/israstat-explorer) | Israeli statistics explorer | ![Stars](https://img.shields.io/github/stars/romanzarkhin/israstat-explorer?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/romanzarkhin/israstat-explorer) |
| [cran/il.cbs.muni](https://github.com/cran/il.cbs.muni) | R package for CBS municipal data | ![Stars](https://img.shields.io/github/stars/cran/il.cbs.muni?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/cran/il.cbs.muni) |
| [107SBakst/econfin_functions](https://github.com/107SBakst/econfin_functions) | Israeli econ/finance helper functions | ![Stars](https://img.shields.io/github/stars/107SBakst/econfin_functions?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/107SBakst/econfin_functions) |
| [idanmev/calcala-israel](https://github.com/idanmev/calcala-israel) | Israeli economics content site | ![Stars](https://img.shields.io/github/stars/idanmev/calcala-israel?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/idanmev/calcala-israel) |

## Knesset, Elections & Judicial

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [AT020993/knesset_refactor](https://github.com/AT020993/knesset_refactor) | Knesset (parliament) data refactor | ![Stars](https://img.shields.io/github/stars/AT020993/knesset_refactor?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/AT020993/knesset_refactor) |
| [amnir/knessy](https://github.com/amnir/knessy) | Knesset data utility | ![Stars](https://img.shields.io/github/stars/amnir/knessy?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/amnir/knessy) |
| [moshelati/knesset-data-vote](https://github.com/moshelati/knesset-data-vote) | Knesset voting data | ![Stars](https://img.shields.io/github/stars/moshelati/knesset-data-vote?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/moshelati/knesset-data-vote) |
| [zomer-g/Knesset_Committees_PM](https://github.com/zomer-g/Knesset_Committees_PM) | Knesset committees project management data | ![Stars](https://img.shields.io/github/stars/zomer-g/Knesset_Committees_PM?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/zomer-g/Knesset_Committees_PM) |
| [zomer-g/Supreme-Court](https://github.com/zomer-g/Supreme-Court) | Israeli Supreme Court data | ![Stars](https://img.shields.io/github/stars/zomer-g/Supreme-Court?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/zomer-g/Supreme-Court) |
| [jschler/ILSC_Data](https://github.com/jschler/ILSC_Data) | Israeli Supreme Court data | ![Stars](https://img.shields.io/github/stars/jschler/ILSC_Data?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/jschler/ILSC_Data) |
| [AriehA1995/israel-elections-data-analysis](https://github.com/AriehA1995/israel-elections-data-analysis) | Israeli elections data analysis | ![Stars](https://img.shields.io/github/stars/AriehA1995/israel-elections-data-analysis?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/AriehA1995/israel-elections-data-analysis) |

## Banking & Personal Finance

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [eshaham/israeli-bank-scrapers](https://github.com/eshaham/israeli-bank-scrapers) | Canonical Israeli bank scrapers (banks + cards) | ![Stars](https://img.shields.io/github/stars/eshaham/israeli-bank-scrapers?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/eshaham/israeli-bank-scrapers) |
| [Urigo/israeli-bank-scrapers-modern-schemas](https://github.com/Urigo/israeli-bank-scrapers-modern-schemas) | Modern Bank Hapoalim schemas | ![Stars](https://img.shields.io/github/stars/Urigo/israeli-bank-scrapers-modern-schemas?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Urigo/israeli-bank-scrapers-modern-schemas) |
| [shlomiuziel/asher-mcp](https://github.com/shlomiuziel/asher-mcp) | MCP over israeli-bank-scrapers | ![Stars](https://img.shields.io/github/stars/shlomiuziel/asher-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/shlomiuziel/asher-mcp) |
| [glekner/il-bank-mcp](https://github.com/glekner/il-bank-mcp) | Israeli bank MCP server | ![Stars](https://img.shields.io/github/stars/glekner/il-bank-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/glekner/il-bank-mcp) |
| [mottibec/israeli-bank-mcp](https://github.com/mottibec/israeli-bank-mcp) | Israeli bank MCP server | ![Stars](https://img.shields.io/github/stars/mottibec/israeli-bank-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/mottibec/israeli-bank-mcp) |
| [daniel-hauser/moneyman](https://github.com/daniel-hauser/moneyman) | Bank-scrape aggregator with pluggable storage | ![Stars](https://img.shields.io/github/stars/daniel-hauser/moneyman?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/daniel-hauser/moneyman) |
| [brafdlog/caspion](https://github.com/brafdlog/caspion) | Personal-finance app with bank scrape | ![Stars](https://img.shields.io/github/stars/brafdlog/caspion?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/brafdlog/caspion) |
| [AvnerAdda/shekelsync](https://github.com/AvnerAdda/shekelsync) | Electron desktop finance tracker | ![Stars](https://img.shields.io/github/stars/AvnerAdda/shekelsync?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/AvnerAdda/shekelsync) |
| [orzarchi/israeli-finance-scraper](https://github.com/orzarchi/israeli-finance-scraper) | Israeli finance scraper | ![Stars](https://img.shields.io/github/stars/orzarchi/israeli-finance-scraper?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/orzarchi/israeli-finance-scraper) |
| [eshaham/israeli-ynab-updater](https://github.com/eshaham/israeli-ynab-updater) | YNAB updater for Israeli accounts | ![Stars](https://img.shields.io/github/stars/eshaham/israeli-ynab-updater?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/eshaham/israeli-ynab-updater) |
| [tomerh2001/israeli-banks-actual-budget-importer](https://github.com/tomerh2001/israeli-banks-actual-budget-importer) | Actual Budget importer | ![Stars](https://img.shields.io/github/stars/tomerh2001/israeli-banks-actual-budget-importer?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/tomerh2001/israeli-banks-actual-budget-importer) |
| [sergienko4/israeli-bank-scrapers-to-actual-budget](https://github.com/sergienko4/israeli-bank-scrapers-to-actual-budget) | Bank scrapers → Actual Budget | ![Stars](https://img.shields.io/github/stars/sergienko4/israeli-bank-scrapers-to-actual-budget?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/sergienko4/israeli-bank-scrapers-to-actual-budget) |
| [shustinm/finparse](https://github.com/shustinm/finparse) | Bank scrapers → Firefly III | ![Stars](https://img.shields.io/github/stars/shustinm/finparse?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/shustinm/finparse) |
| [ohadbarr1/cheshbeshbon](https://github.com/ohadbarr1/cheshbeshbon) | Israeli bookkeeping | ![Stars](https://img.shields.io/github/stars/ohadbarr1/cheshbeshbon?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/ohadbarr1/cheshbeshbon) |
| [enudler/nudlers](https://github.com/enudler/nudlers) | Personal finance (scope unclear) | ![Stars](https://img.shields.io/github/stars/enudler/nudlers?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/enudler/nudlers) |
| [danielcashpilot/cashpilot](https://github.com/danielcashpilot/cashpilot) | Generic cashflow tool | ![Stars](https://img.shields.io/github/stars/danielcashpilot/cashpilot?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/danielcashpilot/cashpilot) |

## Real Estate — Nadlan, Yad2, Madlan

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [AdanimInstitue/israel-nadlan-data](https://github.com/AdanimInstitue/israel-nadlan-data) | Israeli real-estate (Nadlan) dataset | ![Stars](https://img.shields.io/github/stars/AdanimInstitue/israel-nadlan-data?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/AdanimInstitue/israel-nadlan-data) |
| [AdanimInstitue/israel-nadlan-data-collector](https://github.com/AdanimInstitue/israel-nadlan-data-collector) | Collector for Israeli real-estate (Nadlan) data | ![Stars](https://img.shields.io/github/stars/AdanimInstitue/israel-nadlan-data-collector?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/AdanimInstitue/israel-nadlan-data-collector) |
| [IsraelZablianov/nadlan-skill](https://github.com/IsraelZablianov/nadlan-skill) | Wraps nadlan.gov.il transaction history | ![Stars](https://img.shields.io/github/stars/IsraelZablianov/nadlan-skill?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/IsraelZablianov/nadlan-skill) |
| [nitzpo/nadlan-mcp](https://github.com/nitzpo/nadlan-mcp) | MCP server for nadlan.gov.il | ![Stars](https://img.shields.io/github/stars/nitzpo/nadlan-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/nitzpo/nadlan-mcp) |
| [jmpfar/gov-nadlan-fetcher](https://github.com/jmpfar/gov-nadlan-fetcher) | Wraps nadlan.gov.il internal JSON endpoints | ![Stars](https://img.shields.io/github/stars/jmpfar/gov-nadlan-fetcher?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/jmpfar/gov-nadlan-fetcher) |
| [Exitiumverum/NadlanAI](https://github.com/Exitiumverum/NadlanAI) | Nadlan AI tool | ![Stars](https://img.shields.io/github/stars/Exitiumverum/NadlanAI?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Exitiumverum/NadlanAI) |
| [NivEz/yad2-scraper](https://github.com/NivEz/yad2-scraper) | Yad2 listings scraper | ![Stars](https://img.shields.io/github/stars/NivEz/yad2-scraper?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/NivEz/yad2-scraper) |
| [TamirMa/yad2listings](https://github.com/TamirMa/yad2listings) | Yad2 listings on a graph | ![Stars](https://img.shields.io/github/stars/TamirMa/yad2listings?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/TamirMa/yad2listings) |
| [almog/yad2](https://github.com/almog/yad2) | RSS feed over yad2.co.il | ![Stars](https://img.shields.io/github/stars/almog/yad2?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/almog/yad2) |
| [dplesh/yad2clipboard](https://github.com/dplesh/yad2clipboard) | Copy Yad2 nadlan post to clipboard | ![Stars](https://img.shields.io/github/stars/dplesh/yad2clipboard?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/dplesh/yad2clipboard) |
| [poovarasan011/yad2-semantic-search](https://github.com/poovarasan011/yad2-semantic-search) | Semantic search over Yad2 listings | ![Stars](https://img.shields.io/github/stars/poovarasan011/yad2-semantic-search?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/poovarasan011/yad2-semantic-search) |
| [Idantall/DiraAi](https://github.com/Idantall/DiraAi) | Madlan-style listings browser | ![Stars](https://img.shields.io/github/stars/Idantall/DiraAi?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Idantall/DiraAi) |
| [TCyberChef/israel-housing-finder](https://github.com/TCyberChef/israel-housing-finder) | Israel housing finder | ![Stars](https://img.shields.io/github/stars/TCyberChef/israel-housing-finder?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/TCyberChef/israel-housing-finder) |
| [cxt9/find-apartments](https://github.com/cxt9/find-apartments) | Apartment finder | ![Stars](https://img.shields.io/github/stars/cxt9/find-apartments?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/cxt9/find-apartments) |
| [shualilaw1-commits/israel-housing-price-prediction](https://github.com/shualilaw1-commits/israel-housing-price-prediction) | Israel housing price prediction | ![Stars](https://img.shields.io/github/stars/shualilaw1-commits/israel-housing-price-prediction?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/shualilaw1-commits/israel-housing-price-prediction) |
| [mosegorge/Real-estate-prediction-machine-learning](https://github.com/mosegorge/Real-estate-prediction-machine-learning) | Real-estate price prediction ML | ![Stars](https://img.shields.io/github/stars/mosegorge/Real-estate-prediction-machine-learning?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/mosegorge/Real-estate-prediction-machine-learning) |
| [oshritmau/hebrew-rag-realestate](https://github.com/oshritmau/hebrew-rag-realestate) | Hebrew RAG over real-estate data | ![Stars](https://img.shields.io/github/stars/oshritmau/hebrew-rag-realestate?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/oshritmau/hebrew-rag-realestate) |
| [ddark-il/diralottery](https://github.com/ddark-il/diralottery) | Dira BeHanaha (Mehir Lamishtaken) lottery tracker | ![Stars](https://img.shields.io/github/stars/ddark-il/diralottery?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/ddark-il/diralottery) |

## Mortgages & Housing Calculators

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [ndor/mashkanta](https://github.com/ndor/mashkanta) | Israeli mortgage optimisation | ![Stars](https://img.shields.io/github/stars/ndor/mashkanta?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/ndor/mashkanta) |
| [erezs1234/rent-or-buy](https://github.com/erezs1234/rent-or-buy) | Hebrew rent-vs-mortgage calculator | ![Stars](https://img.shields.io/github/stars/erezs1234/rent-or-buy?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/erezs1234/rent-or-buy) |
| [aaron-a-d/israeli-mortgage-calculator](https://github.com/aaron-a-d/israeli-mortgage-calculator) | Israeli mortgage calculator | ![Stars](https://img.shields.io/github/stars/aaron-a-d/israeli-mortgage-calculator?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/aaron-a-d/israeli-mortgage-calculator) |
| [noybi642-yarin/MyMortgage](https://github.com/noybi642-yarin/MyMortgage) | Mortgage calculator | ![Stars](https://img.shields.io/github/stars/noybi642-yarin/MyMortgage?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/noybi642-yarin/MyMortgage) |
| [oados112/mortgage-calculator-site](https://github.com/oados112/mortgage-calculator-site) | Mortgage calculator site | ![Stars](https://img.shields.io/github/stars/oados112/mortgage-calculator-site?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/oados112/mortgage-calculator-site) |
| [tuvalgueta/Mashkanta-Pro](https://github.com/tuvalgueta/Mashkanta-Pro) | Israeli mortgage calculator | ![Stars](https://img.shields.io/github/stars/tuvalgueta/Mashkanta-Pro?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/tuvalgueta/Mashkanta-Pro) |
| [Baruchhanya/MashkantaAI](https://github.com/Baruchhanya/MashkantaAI) | AI-assisted mortgage tool | ![Stars](https://img.shields.io/github/stars/Baruchhanya/MashkantaAI?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Baruchhanya/MashkantaAI) |
| [amitre/Mashkanta2](https://github.com/amitre/Mashkanta2) | Israeli mortgage calculator | ![Stars](https://img.shields.io/github/stars/amitre/Mashkanta2?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/amitre/Mashkanta2) |
| [RGproj/Mashkanta](https://github.com/RGproj/Mashkanta) | Israeli mortgage calculator | ![Stars](https://img.shields.io/github/stars/RGproj/Mashkanta?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/RGproj/Mashkanta) |
| [NISANH66/Smart-Mortgage-Calculator](https://github.com/NISANH66/Smart-Mortgage-Calculator) | Smart mortgage calculator | ![Stars](https://img.shields.io/github/stars/NISANH66/Smart-Mortgage-Calculator?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/NISANH66/Smart-Mortgage-Calculator) |
| [roy-aniccai/Sayeret-Calculator](https://github.com/roy-aniccai/Sayeret-Calculator) | Mortgage qualification calculator | ![Stars](https://img.shields.io/github/stars/roy-aniccai/Sayeret-Calculator?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/roy-aniccai/Sayeret-Calculator) |

## Supermarket Prices

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [OpenIsraeliSupermarkets/israeli-supermarket-scarpers](https://github.com/OpenIsraeliSupermarkets/israeli-supermarket-scarpers) | Scrapers for Israeli supermarket price data | ![Stars](https://img.shields.io/github/stars/OpenIsraeliSupermarkets/israeli-supermarket-scarpers?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/OpenIsraeliSupermarkets/israeli-supermarket-scarpers) |
| [OpenIsraeliSupermarkets/israeli-supermarket-parsers](https://github.com/OpenIsraeliSupermarkets/israeli-supermarket-parsers) | Parsers for Israeli supermarket price data | ![Stars](https://img.shields.io/github/stars/OpenIsraeliSupermarkets/israeli-supermarket-parsers?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/OpenIsraeliSupermarkets/israeli-supermarket-parsers) |
| [tomereliel0/PricyAPI](https://github.com/tomereliel0/PricyAPI) | Price-data API | ![Stars](https://img.shields.io/github/stars/tomereliel0/PricyAPI?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/tomereliel0/PricyAPI) |

## Health

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [MatanEcon/israel-doctor-data](https://github.com/MatanEcon/israel-doctor-data) | Israeli physicians dataset | ![Stars](https://img.shields.io/github/stars/MatanEcon/israel-doctor-data?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/MatanEcon/israel-doctor-data) |
| [ecampau/COVID-19-Vaccine-Efficacy](https://github.com/ecampau/COVID-19-Vaccine-Efficacy) | COVID-19 vaccine efficacy analysis (incl. Israeli data) | ![Stars](https://img.shields.io/github/stars/ecampau/COVID-19-Vaccine-Efficacy?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/ecampau/COVID-19-Vaccine-Efficacy) |

## Energy & Environment

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [nzo-heschel/israel-energy-data](https://github.com/nzo-heschel/israel-energy-data) | Israeli energy sector data | ![Stars](https://img.shields.io/github/stars/nzo-heschel/israel-energy-data?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/nzo-heschel/israel-energy-data) |
| [DeanZigdon/land_cover_classification](https://github.com/DeanZigdon/land_cover_classification) | Land cover classification (Israel) | ![Stars](https://img.shields.io/github/stars/DeanZigdon/land_cover_classification?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/DeanZigdon/land_cover_classification) |

## Transport & Aviation

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [Ofigu/airport-data-pipeline](https://github.com/Ofigu/airport-data-pipeline) | Israeli airport data pipeline | ![Stars](https://img.shields.io/github/stars/Ofigu/airport-data-pipeline?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Ofigu/airport-data-pipeline) |
| [rachelbak/MigdalGarageProject](https://github.com/rachelbak/MigdalGarageProject) | Migdal Garage project | ![Stars](https://img.shields.io/github/stars/rachelbak/MigdalGarageProject?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/rachelbak/MigdalGarageProject) |

## Public Safety & Civil Defence

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [dleshem/israel-alerts-data](https://github.com/dleshem/israel-alerts-data) | Israeli alerts (Pikud HaOref) historical data | ![Stars](https://img.shields.io/github/stars/dleshem/israel-alerts-data?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/dleshem/israel-alerts-data) |
| [dev-symbol/Israel-Shelters-Databas](https://github.com/dev-symbol/Israel-Shelters-Databas) | Israel public shelters database | ![Stars](https://img.shields.io/github/stars/dev-symbol/Israel-Shelters-Databas?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/dev-symbol/Israel-Shelters-Databas) |

## Geospatial & Land

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [akivaschiff/israel-geolocation](https://github.com/akivaschiff/israel-geolocation) | Israel geolocation utilities | ![Stars](https://img.shields.io/github/stars/akivaschiff/israel-geolocation?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/akivaschiff/israel-geolocation) |
| [bengurevich1danyel/land-hunter](https://github.com/bengurevich1danyel/land-hunter) | Parcel tracking, plan monitoring, spatial | ![Stars](https://img.shields.io/github/stars/bengurevich1danyel/land-hunter?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/bengurevich1danyel/land-hunter) |

## Currency & FX

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [Avigail3648/Exchange-rate-tracker](https://github.com/Avigail3648/Exchange-rate-tracker) | Exchange rate tracker | ![Stars](https://img.shields.io/github/stars/Avigail3648/Exchange-rate-tracker?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/Avigail3648/Exchange-rate-tracker) |
| [attogram/currency-exchange-rates](https://github.com/attogram/currency-exchange-rates) | Currency exchange rates dataset | ![Stars](https://img.shields.io/github/stars/attogram/currency-exchange-rates?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/attogram/currency-exchange-rates) |

## Civic & General

| Repository | Description | Stars | Last Updated |
|---|---|---|---|
| [zomer-g/ocal](https://github.com/zomer-g/ocal) | Open calendar / civic data | ![Stars](https://img.shields.io/github/stars/zomer-g/ocal?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/zomer-g/ocal) |
| [GaryShnol/urban-guardian-mcp](https://github.com/GaryShnol/urban-guardian-mcp) | Urban / civic MCP (zoning, permits) | ![Stars](https://img.shields.io/github/stars/GaryShnol/urban-guardian-mcp?style=flat) | ![Last Commit](https://img.shields.io/github/last-commit/GaryShnol/urban-guardian-mcp) |

## Datasets on Hugging Face

| Dataset | Description |
|---|---|
| [danielrosehill/Jerusalem-Air-Quality-Shabbat](https://huggingface.co/datasets/danielrosehill/Jerusalem-Air-Quality-Shabbat) | Jerusalem air-quality readings on Shabbat — derived from Israeli environmental monitoring data. |

## APIs

| API | Description | Endpoint / Notes |
|---|---|---|
| **data.gov.il (CKAN)** | National open-data portal — 1,194 datasets, 61 publishing orgs. No English titles in API; see `060526/` for the curated English index. | [`/api/3/action/package_search`](https://data.gov.il/api/3/action/package_search?rows=5) · [docs in snapshot](./060526/README.md#api-endpoints) |
| **CBS House Price Index** | Central Bureau of Statistics index catalog | [api.cbs.gov.il/Index/Catalog/Catalog?lang=en](https://api.cbs.gov.il/Index/Catalog/Catalog?lang=en) |
| **Nadlan.gov.il** | Israeli real-estate transactions — no official API; community wrappers exist (see Nadlan repos above) | https://www.nadlan.gov.il/ |

## Contributing

PRs welcome — add additional Israeli open-data repositories, datasets, or APIs to the relevant category above. To refresh the data.gov.il snapshot, run `./import-catalogue.sh`.
