# GLO — Glossary

**Status:** done 2026-11-24 · Pronunciation approved and proofs reviewed · **Plan doc:** `multimedia-plan.md` § E

## Scope
The print replacement for the audio ideas is a back-of-volume glossary of places, people, titles and terms. Each entry gives the book form, the modern form where applicable, and a short gloss. A pronunciation hint appears where it helps with an unfamiliar form. The task also covers the I-1 parallel-text box (Franco-Italian Prologue opening beside Yule's English).

## Editorial inputs
- Candidate entries from the critiques' audio sections:
  - Cambaluc/Khanbaliq, Chandu/Shangdu, Keshican/keshig, Quinsay/Xingzai, Zayton/Zaitūn;
  - Sagamoni Borcan, Cocachin/Kököchin, Kiacatu/Geikhatu, Casan/Ghazan;
  - paiza, kumis, bakhshi, Natigay;
  - Toscaol, Bularguchi, naqqāra, bād-gīr, *Milione*, and others.
  - *Milione*: document the name and attribute competing explanations; do not define it as “million lies” or assert a chronology for that interpretation (S20-E27/E43; [closure](../../../../research/investigations/results/S-20-closure.md)).
- Characters' name forms come from `CHR`: `registry/characters.yaml` `book_name` → `gloss` (S-05 ✓), one entry per person with a gloss (`CHR.T3`).

- The place entries use the gazetteer's modern forms and Wikipedia links, with a sourced origin line where available. Pronunciation hints are house suggestions: give a single default reading for the English reader, and include a second reading only when it explains a distinct spelling variant named in the gloss (*Chandu* / *Ciandu*, *Juju* / *Giogiu*, *Kinsay* / *Quinsay*) or the Italian book title *Milione*. The drafts draw on `research/results/GAZ-names-raw.md`, and `GAZ-intake.md` records rejected origin lines.

## Gated by spikes
S-04 ✓ (place forms: `book_name` → `modern_name`, `aliases`; closed 2026-10-22) · S-05 ✓ (people: `registry/characters.yaml`; closed 2026-10-22) · S-08 ✓ (closed 2026-11-10; the glossary's page layout is `BLD.T4`)

## Tasks

- **GLO.T1 — Entry lists.** The section is titled **Glossary** in each volume and its contents. Volumes I, II and III have 125, 126 and 119 entries. The [review checklist](../../../../research/registry/glossary-review.md) records 198 places, 24 people and 17 terms across the series. The volume assignments start with the registry chapter fields and reflect appearances in the prose, Notes, tables, captions, maps and diagrams. The final audit added ten volume assignments for eight places. The shared route-map caption brings Chamba and Samara into Volumes I and II and Java the Less into Volume II. Derbend and Mausul also appear in Volume II, and Bangala, Fuju and Sarai in Volume III. [CHR.T3](CHR-characters.md#chrt3--glossary-entries-for-people-with-glo) verified coverage of all 24 people, including Abaga in Volume I.
- **GLO.T2 — Respellings.** The editor approved the current readings and house style on 2026-11-24. The checklist records 211 entries with a hint and 28 that omit one. The hints give an English reading for unfamiliar forms and isolate the unfamiliar part of a compound where applicable, as in **Desert of Lop (Pronounced LOP)**. The second readings cover *Ciandu*, *Giogiu*, *Quinsay* and the Italian pronunciation of *Milione*. The final pass clarified the alternate spellings in their glosses and made the vowel explicit in *Soer*, *Vocan* and *Vochan*. Regenerate with `python3 tools/glossary.py --write` from `book/`.
- **How to read this book.** The [Volume I opening guide](../../../../manuscript/vol-1/front-01-world-before-the-road.md) points readers to each volume’s glossary and [Wikipedia’s pronunciation respelling key](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key).
- **GLO.T3 — I-1 parallel text.** The box pairs excerpts from the opening address through the invitation to have the Book read aloud, with an ellipsis in each panel. The wording matches [Eusebi’s edition, p. 35](https://edizionicafoscari.it/media/pdf/books/978-88-6969-224-6/978-88-6969-224-6_69TdyXc.pdf) and the [local Yule–Cordier Prologue](../../../../research/refs/yule-vol1.txt). The lead-in cites Note 14. Its print link runs from PDF page 28 to page 34.

## Proof checks — 2026-11-24

- PDF, HTML and EPUB built for all three volumes. Each contents link opens its glossary, and all formats preserve the entry order and Wikipedia links. The Wikipedia API resolved all 178 distinct article URLs.
- Visual review covered every two-column glossary page. The print entry spacing was tightened to keep Zayton on the final two-column glossary page in Volume I. The I-1 box sits side by side on PDF page 30 and stacks at narrow browser widths. The Volume I reading guide links to the respelling key on PDF page 9 and in the digital editions.
- `tools/glossary.py --check` passed. The three PDFs report zero missing glyphs, unresolved citations, or line overruns of 10 pt or more. All 52 manuscript files passed lint, with one existing name-proximity warning in the Volume I reading guide. All 51 automated tests passed.

| Volume | Glossary folios | PDF pages |
|---|---:|---:|
| I | 143–149 | 167–173 |
| II | 193–200 | 217–224 |
| III | 161–167 | 183–189 |
