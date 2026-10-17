// Renders findings.json as an A–Z digest. Build: typst compile findings.typ
#let data = json("findings.json")
#let initial = "Daniel Rosehill (initial index)"

#set document(title: "Israel Open Data Resources — Findings " + data.generated, author: ("Claude Opus 5.5", "Daniel Rosehill"))
#set page(paper: "a4", margin: (x: 18mm, y: 18mm),
  footer: context [#set text(8pt, fill: gray); Israel Open Data Resources · findings #data.generated #h(1fr) #counter(page).display("1 / 1", both: true)])
#set text(font: "Libertinus Serif", size: 9.5pt)
#show link: set text(fill: rgb("#1a5fb4"))

#let kind-label = (repo: "Repository", dataset: "Dataset", api: "API / portal")

#align(center)[
  #text(18pt, weight: "bold")[Israel Open Data Resources]\
  #text(12pt)[Findings digest — #data.generated]
]
#v(4pt)
*Research:* Claude Opus 5.5 · *Initial repositories found by:* Daniel Rosehill\
*Source repository:* #link("https://github.com/danielrosehill/Israel-Open-Data-Resources")

#v(4pt)
#table(columns: 4, stroke: 0.4pt + gray, inset: 5pt,
  [*Entries*], [*From initial index*], [*Added #data.generated*], [*Removed (dead)*],
  [#data.counts.total], [#data.counts.initial], [#data.counts.added], [#data.counts.removed])

#text(8.5pt)[
  Every entry was checked on #data.generated. GitHub repositories: existence, stars, last push and archive status via the GitHub API. Hugging Face datasets: existence and visibility via the Hub API. APIs and portals: an HTTP request to the listed endpoint, with the result recorded under *Findings*. "Last push" is a proxy for maintenance, not proof of it. Entries are sorted alphabetically by name; each is marked #box(fill: rgb("#e8f0fe"), inset: (x: 3pt), outset: (y: 2pt))[NEW] if this pass added it.
]

#line(length: 100%, stroke: 0.5pt + gray)

#for e in data.entries [
  #block(breakable: false, below: 0pt, inset: (y: 5pt), stroke: (bottom: 0.3pt + luma(210)), width: 100%)[
    #text(weight: "bold")[#e.name]
    #if e.source != initial [ #box(fill: rgb("#e8f0fe"), inset: (x: 3pt), outset: (y: 2pt))[#text(7.5pt)[NEW]]]
    #h(1fr) #text(8pt, fill: gray)[#kind-label.at(e.kind) · #e.category]\
    #e.description\
    #text(8pt)[#link(e.url)[#e.url]]\
    #let removed = e.findings.starts-with("REMOVED")
    #text(8.5pt, fill: if removed { rgb("#b00020") } else { black })[*Findings:* #e.findings]
    #h(1fr) #text(7.5pt, fill: gray)[#e.source]
  ]
]
