# S-04 — Gazetteer authority and naming policy

**Status:** open · **Timebox:** 1 session · **Gates:** naming items in chapter backlogs; all `MAP` tasks; front-02 place tables

## Question
What is the naming authority? What schema does the gazetteer need to drive both prose naming and maps, and which rows are missing or wrong?

## Why it matters
- The gazetteer is declared the naming authority, but it uses modern forms (Bokhara, Kashgar) where the chapters use Yule's (Bocara, Cascar).
- About 70 places are missing, which blocks the maps.
- Several identifications conflict with the chapters: Cachanfu, Caugigu, Cacanfu, Nanghin, the two Vujus, Male.

## Inputs
- `gazetteer.csv`, `gazetteer-readme.md`
- Critique: I-M8, II-M2, II-M11, III-m3, III-m4
- Chapter backlogs § Naming

## Method
1. Policy: `book_name` = the Yule form used in the chapters. Modern and other spellings go in a new `aliases` column; add a `chapters` column; split `notes` from `id_confidence`.
2. Extract every place name used in the chapters (script plus review) and diff it against the gazetteer.
3. Add the missing rows with coordinates and reliability. Resolve the conflicting identifications, with a sourced rationale in notes.
4. Decide the gloss rule: book form + modern gloss on first mention *per chapter* (current rule), with a skip list where the forms are identical (Venice, Genoa).

## Output (definition of done)
- [ ] `gazetteer.csv` v2 + updated readme
- [ ] Name-usage diff report (which chapter uses which non-canonical form)
- [ ] Lint rule for names handed to S-02

## Feedback to plan
- `content-revision-plan.md` § W5 gazetteer
- `multimedia-plan.md` § A (map prerequisites satisfied)

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `GAZ.T*` (rows, schema, front-02 tables regen); naming items in each chapter's `.T1`/`.T3`
