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
  tasks/chapters/vol-N/*.md  ← one file per manuscript file (49)
  tasks/cross/*.md           ← cross-cutting areas (11)
  registry/                  ← spike outputs: characters, facts, PD sources, conventions
  templates/                 ← spike, chapter, cross
```

## Spike board

| ID | Spike | Status | Depends on | Gates |
|---|---|---|---|---|
| [S-01](spikes/S-01-voice-standard.md) | Voice standard (pilot re-voice of II-2) | open | S-03, S-06 (for II-2's facts), S-08 conventions | `.T3` in every narrative chapter |
| [S-02](spikes/S-02-acceptance-lint.md) | Acceptance lint and thresholds | open | — (thresholds finalised with S-01, S-03) | `.T6` everywhere; the definition of done |
| [S-03](spikes/S-03-apparatus-conventions.md) | Apparatus conventions (markers, tags, Notes, Ramusio flags) | open | — | `.T2`, `.T4`; `APP` |
| [S-04](spikes/S-04-gazetteer-naming.md) | Gazetteer authority and naming | open | — | `GAZ`, `MAP`, naming items |
| [S-05](spikes/S-05-character-registry.md) | Character registry (text + visual) | open | chapter backlogs, S-06 | `CHR`, `PLT`, character items |
| [S-06](spikes/S-06-fact-verification.md) | Fact verification sheet | open | — | factual `.T1` items; `DIA` timelines |
| [S-07](spikes/S-07-structure-length.md) | Structure and length (I-12 split, front/back roles, III-10 to III-12) | open | S-01 | the affected files |
| [S-08](spikes/S-08-latex-pipeline.md) | LaTeX build pipeline and Markdown conventions | open | toolchain install (needs approval) | `BLD`; `.T5` |
| [S-09](spikes/S-09-map-diagram-pipeline.md) | Map and diagram pipeline | open | S-08 (fonts, trim); S-04 for full maps | `MAP`, `DIA` |
| [S-10](spikes/S-10-image-generation-pilot.md) | Image generation pilot | open | generator choice; S-05 cards; S-08 sizes | `PLT` (GEN) |
| [S-11](spikes/S-11-public-domain-sourcing.md) | Public-domain sourcing and licensing | open | — | `PLT` (PD) |

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
| `HOT.1` | Replace the invented or misquoted epigraphs. The critique gives verified Yule replacements with line numbers (content plan W1.1). **Check each replacement against the existing chapter epigraphs.** Three of the Vol. II suggestions duplicate the ch-01, ch-10 and ch-13 epigraphs, so pick other verified lines for those. |
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

## Definition of done (provisional; finalised by S-02)

A manuscript file is **done** when:
- the lint is green: verbatim Yule ≤ 25%; no Book first person or archaisms outside quotes; hinge budgets met; no scaffolding; citations 1:1; quotations verified; markers in the ✓~✗◇? set; length in range; names canonical;
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
