# GLO — Names and pronunciation glossary

**Status:** draft implemented, awaiting pronunciation and page review · **Plan doc:** `multimedia-plan.md` § E

## Scope
The print replacement for the audio ideas is a back-of-volume glossary of places, people, titles and terms. Each entry gives the book form, the modern form where applicable, and a short gloss. A pronunciation hint appears where it helps with an unfamiliar form. The task also covers the I-1 parallel-text box (Franco-Italian Prologue opening beside Yule's English).

## Backlog
- Candidate entries from the critiques' audio sections:
  - Cambaluc/Khanbaliq, Chandu/Shangdu, Keshican/keshig, Quinsay/Xingzai, Zayton/Zaitūn;
  - Sagamoni Borcan, Cocachin/Kököchin, Kiacatu/Geikhatu, Casan/Ghazan;
  - paiza, kumis, bakhshi, Natigay;
  - Toscaol, Bularguchi, naqqāra, bād-gīr, *Milione*, and others.
  - *Milione*: document the name and attribute competing explanations; do not define it as “million lies” or assert a chronology for that interpretation (S20-E27/E43; [closure](../../research/results/S-20-closure.md)).
- Characters' name forms come from `CHR`: `registry/characters.yaml` `book_name` → `gloss` (S-05 ✓), one entry per person with a gloss (`CHR.T3`).

- **Decided 2026-10-22:** place entries are book form → modern form → respelling → origin line → Wikipedia link (`gazetteer.csv` `wikipedia`). Respellings are house suggestions reviewed by a person (draft in `research/results/GAZ-names-raw.md`; rejected origin lines listed in `GAZ-intake.md`). Offer both an anglicised and an Italian reading where the Yule form is Italianate.

## Gated by spikes
S-04 ✓ (place forms: `book_name` → `modern_name`, `aliases`; closed 2026-10-22) · S-05 ✓ (people: `registry/characters.yaml`; closed 2026-10-22) · S-08 ✓ (closed 2026-11-10; the glossary's page layout is `BLD.T4`)

## Tasks

- **GLO.T1 — Entry lists.** Volumes I, II and III have 121, 121 and 112 entries. The [review checklist](../../registry/glossary-review.md) records 194 places, 24 people and 17 terms across the series. The volume assignments start with the registry chapter fields. The manuscript audit also checked Notes, tables, captions, maps and diagrams. The Volume I overview map, for example, brings in Kenjanfu, Sindafu and Talifu under their modern labels.
- **GLO.T2 — Respellings.** The glossary includes draft pronunciation hints for less familiar names and terms. Record each human decision in the checklist as **Approved** or **Omit**, then regenerate with `python3 tools/glossary.py --write` from `book/`. Keep the task in review until the readings and pages have been signed off.
- **How to read this book.** The [opening guide](../../../vol-1/front-01-world-before-the-road.md) points readers to the glossary and Wikipedia’s pronunciation respelling key.
- **GLO.T3 — I-1 parallel text.** The box pairs excerpts from the opening address through the invitation to have the Book read aloud, with an ellipsis in each panel. The wording was checked against the [publisher’s PDF, p. 35](https://doi.org/10.30687/978-88-6969-223-9/002) and the [local Yule–Cordier Prologue](../../../refs/yule-vol1.txt). Note [10] remains linked from the introduction.

## Proof checks — 2026-11-21

- PDF, HTML and EPUB built for all three volumes. Each contents link opens its glossary. The formats preserve entry order and place links. The Wikipedia API resolved all 174 distinct article URLs.
- The print glossary starts on PDF page 165 in Volume I, 187 in Volume II and 155 in Volume III. The I-1 box sits side by side on PDF page 30, and stacks at narrow browser widths. Visual review covered the glossary pages and the Prologue box. The builds reported zero missing glyphs and unresolved citations.
- All three glossaries pass lint. The full manuscript lint still reports existing issues. All 42 automated tests passed.
