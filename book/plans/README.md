# Planning — *The Book of the Million* refinement

This folder runs the refinement of the manuscript on three fronts: **content**, **multimedia** and **illustrations**. It is the single place to see what is decided, what is open, and what is ready to work on.

## How it works

```mermaid
flowchart LR
  P[Plan<br/>strategy docs] -->|open questions| S[Spikes]
  S -->|findings + decision| F[Feedback:<br/>update plan docs]
  F --> T[Tasks<br/>per chapter + cross-cutting]
  T -->|lint + human read| D[Done]
  T -.new questions.-> S
```

1. **Plan.** The strategy docs say *what* we want and *why*.
2. **Spikes.** A spike is a time-boxed investigation for each question the plan can't answer by assumption. A spike can be a prototype (the voice pilot), a measurement (the lint baseline), research (fact verification) or a decision (conventions).
3. **Feedback.** Closing a spike means writing its **Decision**, updating the plan docs listed in its *Feedback to plan* section, and recording what changed.
4. **Tasks.** Only then are tasks written into the files the spike gates. Until that point, chapter and area files hold a **backlog** of known findings, not tasks.
5. **Done.** A task is done when it meets its *done when* line, which is always the lint gate (S-02) plus a human read for prose.

New questions found during tasks become new spikes, never silent decisions.

## Layout

```
plans/
  README.md                  ← you are here: board, conventions, decisions
  content-revision-plan.md   ← strategy: content (W0–W6)
  multimedia-plan.md         ← strategy: maps, timelines, diagrams, tables
  illustration-style-guide.md← strategy: regional traditions, rules, tech spec
  illustration-plan.md       ← strategy: hero/secondary plates, pilot prompts
  critique/vol-{1,2,3}.md    ← evidence: the critique pass (source of backlogs)
  spikes/S-NN-*.md           ← open questions
  research/README.md         ← phase R: deep-research workflow, trust rules
  research/results/          ← raw deep-research output, pasted untouched
  tasks/chapters/vol-N/*.md  ← one file per manuscript file (49)
  tasks/cross/*.md           ← cross-cutting areas (11)
  registry/                  ← spike outputs: characters, facts, PD sources, conventions,
                               bibliography, scholarship, enrichment, comparanda
  templates/                 ← spike, chapter, cross
```

## Spike board

| ID | Spike | Status | Depends on | Gates |
|---|---|---|---|---|
| [S-01](spikes/S-01-voice-standard.md) | Voice standard (pilot re-voice of II-2) | **closed** 2026-10-21 | S-03, S-06 (for II-2's facts), S-08 conventions | `.T3` in every narrative chapter |
| [S-02](spikes/S-02-acceptance-lint.md) | Acceptance lint and thresholds | **closed** 2026-10-21 (`tools/lint.py`; S-03/S-04 rules provisional) | — | `.T6` everywhere; the definition of done |
| [S-03](spikes/S-03-apparatus-conventions.md) | Apparatus conventions (markers, tags, Notes, Ramusio flags) | **closed** 2026-10-22 (`VOICE-GUIDE.md` § Apparatus conventions) | — | `.T2`, `.T4`; `APP` |
| [S-04](spikes/S-04-gazetteer-naming.md) | Gazetteer authority and naming | **closed** 2026-10-22 (`gazetteer.csv` v2, `tools/gazetteer.py`) | — | `GAZ.T5`–`T6`, `MAP`, naming items |
| [S-05](spikes/S-05-character-registry.md) | Character registry (text + visual) | open | chapter backlogs, S-06 | `CHR`, `PLT`, character items |
| [S-06](spikes/S-06-fact-verification.md) | Fact verification sheet | open | — | factual `.T1` items; `DIA` timelines |
| [S-07](spikes/S-07-structure-length.md) | Structure and length (I-12 split, front/back roles, III-10 to III-12) | open | S-01 | the affected files |
| [S-08](spikes/S-08-latex-pipeline.md) | LaTeX build pipeline and Markdown conventions | open | toolchain install (needs approval) | `BLD`; `.T5` |
| [S-09](spikes/S-09-map-diagram-pipeline.md) | Map and diagram pipeline | open | S-08 (fonts, trim); S-04 for full maps | `MAP`, `DIA` |
| [S-10](spikes/S-10-image-generation-pilot.md) | Image generation pilot | open | generator choice; S-05 cards; S-08 sizes | `PLT` (GEN) |
| [S-11](spikes/S-11-public-domain-sourcing.md) | Public-domain sourcing and licensing | open | — | `PLT` (PD) |
| [S-24](spikes/S-24-citation-style.md) | Citation and bibliography style (Chicago author-date, base-text sigla, conversion of ~700 Notes) | **decided** 2026-10-22 (Chicago author-date; pass A applied, pass B after S-12) | S-12 (pass B), S-08 | every Note's citations; epigraphs; Works cited; lint rules |

### Phase R — references and enrichment (deep research)

Twelve spikes whose research step runs **outside** this repo. Each holds a paste-ready prompt: run it in a deep-research tool, paste the raw output into `research/results/`, then run an intake session here. Workflow, trust rules and output contract: [research/README.md](research/README.md).

| ID | Spike | Status | Feeds | Gates |
|---|---|---|---|---|
| [S-12](spikes/S-12-bibliography-editions.md) | Master bibliography, editions, translations | open | all R spikes (bib keys) | `registry/bibliography.bib`; citation policy; `BLD` biblatex |
| [S-13](spikes/S-13-scholarship-update.md) | State of the field 2013–2026 (incl. 2024 anniversary) | open | — | III-12, III-11, III-B1, I-01 |
| [S-14](spikes/S-14-fact-verification-sweep.md) | Fact verification sweep (25 claims) | open | **S-06** | factual `.T1` in 17 files |
| [S-15](spikes/S-15-venice-genoa-family.md) | Venice, Genoa and the Polo family record | open | S-05 | I-01, I-02, III-10; `CHR` |
| [S-16](spikes/S-16-overland-route.md) | Overland route: archaeology, identifications (Vol. I) | open | S-04 | Vol. I enrichment; `MAP` A3–A6 |
| [S-17](spikes/S-17-yuan-china.md) | Yuan China: institutions, cities (Vol. II) | open | S-04 | Vol. II enrichment; `DIA`, `TBL` |
| [S-18](spikes/S-18-maritime-return.md) | Maritime Asia and the return voyage (Vol. III) | open | S-04 | Vol. III enrichment; `MAP` A15–A17; `DIA` |
| [S-19](spikes/S-19-primary-comparanda.md) | Comparative primary sources: translations, passages | open | S-02 (lint corpus) | Comparative clauses; `refs/` additions |
| [S-20](spikes/S-20-reception-afterlives.md) | Reception, print, maps, myths | open | S-11 (PD candidates) | III-11, all trivia files; `DIA` B5 |
| [S-21](spikes/S-21-natural-history-marvels.md) | Natural history, commodities, marvels | open | — | asides, trivia, captions; `TBL` |
| [S-22](spikes/S-22-media-visual-references.md) | Visual references from modern media (manga, film, games, reconstruction art) | open | S-05, S-10 | plate `[PERIOD]` cues; costume cards. Used for content, never for style |
| [S-23](spikes/S-23-media-scouting.md) | Scouting more media references: all languages, all media, by hero scene; plus a per-work deep-dive template | open | S-22, S-10 | shortlist for deep dives; scene coverage for the 34 GEN plates |

All twelve prompts can be run at once (S-23 is best after S-22). Intake S-12 first (bibliography keys), then S-14 (it closes S-06). Bring each volume's enrichment spike (S-16/17/18) in **before that volume's W4 re-voice batch**.

**Suggested waves**

| Wave | Spikes | Notes |
|---|---|---|
| 1 | S-02, S-03, S-04, S-06, S-11, S-08 | No dependencies; can run in parallel. S-08 needs install approval. |
| 2 | S-01, S-05, S-09 | S-01 is the most important spike: it unlocks the bulk of the work. |
| 3 | S-07, S-10 | |

## Ready now (no spike needed)

These are reader-facing errors with concrete fixes already in the critique. Safe to do before any spike closes:

| Task | What |
|---|---|
| `MED.T1` | Correct the mis-captioned images in I-F2, II-F2, III-F2 ([MED](tasks/cross/MED-existing-media.md)) |
| `DOC.T1` | Replace `/workspace/...` paths ([DOC](tasks/cross/DOC-status-docs.md)) |
| `HOT.1` | Replace the invented or misquoted epigraphs. The critique gives verified Yule replacements with line numbers (content plan W1.1). **Check each replacement against the existing chapter epigraphs.** Three of the Vol. II suggestions duplicate the ch-01, ch-10 and ch-13 epigraphs, so pick other verified lines for those. After fixing a quotation, run `python3 tools/cite_convert.py --pass A --apply <file>`: the credit is set from where the quotation sits in Yule (S-24). |
| `HOT.2` | Strip the scaffolding leaks: "Soft …:" labels, instructions to self, pasted outline lists, meta lines (W1.3) |
| `HOT.3` | Fix "Po-lo" = Bolad in II-5, II-11 and III-12. The correction is in Yule–Cordier's own addenda, so S-06 is not needed (W1.2). |

The re-voice will later rewrite these chapters anyway. The hotfixes are worth it because they remove errors a reader could quote, and they keep later diffs clean.

## Task index

### Chapters (49 files)

| Vol. | Files |
|---|---|
| I | [tasks/chapters/vol-1/](tasks/chapters/vol-1/): I-F1, I-F2, I-01 … I-13, I-B1 |
| II | [tasks/chapters/vol-2/](tasks/chapters/vol-2/): II-F1, II-F2, II-01 … II-15, II-B1 |
| III | [tasks/chapters/vol-3/](tasks/chapters/vol-3/): III-F1, III-F2, III-01 … III-12, III-B1 |

Each chapter file holds: header metrics, the backlog by category (with critique refs), media hooks (plates, maps, diagrams, tables, characters), the spikes that gate it, and its tasks once they are created. Standard task shapes: `.T1` facts and criticals · `.T2` Ramusio and disputes · `.T3` re-voice · `.T4` Notes and apparatus · `.T5` media placement · `.T6` lint and human read.

### Cross-cutting areas (11 files)

| Code | Area | Main gate |
|---|---|---|
| [MAP](tasks/cross/MAP-maps.md) | Maps A1–A17 | S-04, S-09 |
| [CHR](tasks/cross/CHR-characters.md) | Characters: registry + visual cards | S-05 |
| [PLT](tasks/cross/PLT-plates.md) | Drawings: 34 GEN + 7 PD heroes, secondaries, legacy retirement | S-10, S-11 |
| [DIA](tasks/cross/DIA-timelines-diagrams.md) | Timelines B1–B6, diagrams C1–C16 | S-09 |
| [TBL](tasks/cross/TBL-tables.md) | Comparison tables D | S-08 |
| [GAZ](tasks/cross/GAZ-gazetteer.md) | Gazetteer | S-04 |
| [APP](tasks/cross/APP-apparatus.md) | Markers, tags, how-to-read box | S-03 |
| [GLO](tasks/cross/GLO-glossary.md) | Names and pronunciation glossary | S-04, S-05 |
| [BLD](tasks/cross/BLD-build-tooling.md) | Lint, LaTeX build, media scripts | S-02, S-08, S-09 |
| [MED](tasks/cross/MED-existing-media.md) | Existing media triage | none (T1 ready) |
| [DOC](tasks/cross/DOC-status-docs.md) | Status and project docs | none (T1 ready) |

## Conventions

**IDs**
- Spikes: `S-NN`.
- Chapter files: `I-07`, `II-F1`, `III-B1`. Their tasks: `I-07.T3`.
- Cross areas: `MAP`, `CHR`…; their tasks: `MAP.T05`, `PLT.II-13`.
- Hotfixes: `HOT.n`.

**Statuses**
- Spikes: `open → in-progress → closed`.
- Files and tasks: `backlog → ready → in-progress → review → done`.
- A chapter file becomes `ready` when all its gating spikes are closed and its tasks are written.

**Writing a task** (inside its chapter or area file, under `## Tasks`):

```markdown
### I-07.T3 — Re-voice
- **Status:** ready · **Depends:** S-01, I-07.T1
- **Do:** <specific targets: worst blocks, recaps to cut, length target>
- **Done when:** lint green (S-02 thresholds) + human voice read
```

**Commits**
- One task per commit where practical, with the task ID first: `I-07.T3: re-voice Kerman–Hormos chapter`.
- Spike closures: `S-04: close — gazetteer naming policy`.

**Closing a spike** (checklist):
1. Fill in **Findings** and **Decision**, with the date.
2. Edit every plan doc listed under *Feedback to plan*, and record the change in the spike.
3. Write the tasks into every gated file and set those files to `ready`.
4. Update the spike board above and the decision log below.

## Definition of done (S-02)

A manuscript file is **done** when:
- **the lint is green:** `python3 tools/lint.py <file>` (run from `book/`) exits 0, with no errors. The thresholds below are the values in `tools/lint.py`:

  | Check | Narrative | Essay (III-12) | Front/back |
  |---|---|---|---|
  | Verbatim Yule, 7-gram, incl. epigraph and marked quotes | ≤ 15% | ≤ 15% | ≤ 15% |
  | Book first person / archaisms / "You must know", outside quotes | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
  | "Anyway" / formula hinges / any single attribution verb | ≤ 1 / ≤ 3 / ≤ 4 | — | — |
  | Asides: words each / per chapter; no exit formula, no announced return | ≤ 80 / ≤ 4 | — | — |
  | Marked quotations: words each / per paragraph / per chapter | ≤ 25 / ≤ 2 / ≤ 8 | — | — |
  | Epigraph found in `refs/` (segments split at "…"), or marked *(adapted)* | yes | yes | yes |
  | Marked quotations found in `refs/` | error | warning | warning |
  | Opening recap / closing-recap phrases | 0 / 0 | — | — |
  | Narrative words | 1,800–3,200 | ≤ 3,500 | — |
  | Scaffolding strings (Soft labels, `/workspace`, outline/drafter/SERIES-STATUS refs, placeholders, gazetteer labels, drafting notes) | 0 | 0 | 0 |
  | Citations: body sequential 1..n, Notes 1:1, no duplicates | yes | yes | yes |
  | Retired marker ★ in Notes; every Note opens with a marker; no "Dispute:" label *(S-03)* | 0 | 0 | 0 |
  | Tag line: exactly one of `**[V]**` `**[R]**` `**[M]**` `**[reception]**` in Vol. II–III narrative/essay files; none elsewhere *(S-03)* | yes | yes | none |
  | Ramusio passage reproduced in a paragraph → inline "Ramus…" flag + "Ramusio-only." label in a cited Note *(S-03)* | yes | — | — |
  | Place names: book form from `gazetteer.csv`, modern/alternate form only as a first-mention gloss (`name_policy`, warning until every chapter has had its pass) *(S-04)* | warning | — | — |

- **every lint warning has been looked at during the human read.** Warnings are heuristics: "So/Thus" restatements, repeated paragraph openers, stub Notes, average sentence > 25 words, fewer Ramusio flags than the first draft carried (`tools/ramusio-manifest.json`), name spellings close to a gazetteer name, bare non-canonical place names and unglossed first mentions (S-04, `name_policy`). Marked quotations in the essay and front/back may cite non-Yule sources, so for those files a missing match is a warning, not an error;
- every backlog item is resolved or explicitly deferred with a reason;
- its media hooks are placed or deferred;
- a human has read it for voice.

## Decision log

| Date | Decision | Source |
|---|---|---|
| 2026-10-21 | Markdown now, LaTeX for the final print version; multimedia is static | user |
| 2026-10-21 | Illustrations in regional period styles; real public-domain artworks preferred over generated imitations | user; illustration plan |
| 2026-10-21 | Edition lives in tracked `book/`; `input/` stays the pristine original; branch `refine-edition` | user |
| 2026-10-21 | No nybo for this repo; plan in Markdown | user |
| 2026-10-21 | Scoped workflow: plan → spikes → feedback → tasks per chapter + cross-cutting areas | user |
| 2026-10-21 | Voice standard = `VOICE-GUIDE.md` v2 with II-2 as reference; verbatim ≤ 15%; re-voice before cutting length; W4 in batches of 3–4 | S-01 (pilot approved by user) |
| 2026-10-21 | Definition of done = `tools/lint.py` exits 0 (errors gate; warnings go to the human read); 7-gram verbatim confirmed; baseline 1/49 files pass | S-02 |
| 2026-10-22 | Phase R: references and enrichment via external deep research (S-12 … S-23); results are leads, verified at intake before use | user |
| 2026-10-22 | Citation style: Chicago author-date (18th ed.) in the Notes, Pandoc keys, base text cited as YC (1903/1920 print edition; Gutenberg is only the access route); epigraph credit `— Marco Polo, Book 2, ch. 12 (Yule–Cordier)`; Works cited per volume | user (S-24) |
