# S-04 — Gazetteer authority and naming policy

**Status:** closed 2026-10-22 · **Timebox:** 1 session · **Gates:** naming items in chapter backlogs; all `MAP` tasks; front-02 place tables

## Question
What is the naming authority? What schema does the gazetteer need to drive both prose naming and maps, and which rows are missing or wrong?

## Why it matters
- The gazetteer is declared the naming authority, but it uses modern forms (Bokhara, Kashgar) where the chapters use Yule's (Bocara, Cascar).
- About 70 places are missing, which blocks the maps.
- Several identifications conflict with the chapters: Cachanfu, Caugigu, Cacanfu, Nanghin, the two Vujus, Male.

## Inputs
- **S-16, S-17, S-18** (deep research): current identifications for the uncertain rows, with sources. *Not available at close: `research/results/` held no output. This spike used Yule–Cordier, the critiques and general reference; `GAZ.T6` re-checks the `probable`/`disputed` rows when each run is taken in.*
- `gazetteer.csv`, `gazetteer-readme.md`
- Critique: I-M8, II-M2, II-M11, III-m3, III-m4
- Chapter backlogs § Naming

## Method
1. Policy: `book_name` = the Yule form used in the chapters. Modern and other spellings go in a new `aliases` column; add a `chapters` column; split `notes` from `id_confidence`.
2. Extract every place name used in the chapters (script plus review) and diff it against the gazetteer.
3. Add the missing rows with coordinates and reliability. Resolve the conflicting identifications, with a sourced rationale in notes.
4. Decide the gloss rule: book form + modern gloss on first mention *per chapter* (current rule), with a skip list where the forms are identical (Venice, Genoa).

## Output (definition of done)
- [x] `gazetteer.csv` v2 + updated readme
- [x] Name-usage diff report (which chapter uses which non-canonical form): `plans/status/gazetteer-name-diff.md`
- [x] Lint rule for names handed to S-02: `name_policy` in `tools/lint.py`

## Feedback to plan
- `content-revision-plan.md` § W5 gazetteer
- `multimedia-plan.md` § A (map prerequisites satisfied)

## Findings
_2026-10-22. Method: the prose of all 49 files read through `tools/lint.py`'s own paragraph filter (Notes, quotations and tables excluded), Yule's chapter headings and notes in `refs/`, and the three critiques._

1. **The authority was backwards.** The old `book_name` held modern forms for about 25 places and Yule forms for the rest, so neither the prose nor the maps could use it as a lookup. Yule's chapter headings (Books I–III contents) are a complete, citable list of Polo's own forms and settle every "which spelling" question.
2. **The chapters do not agree with each other either.** Prose mixes Tauris/Tabriz, Hormos/Hormuz, Chandu/Shangdu, Kinsay/Quinsay, Zayton/Zaiton, Kisi/Kish/Kis, Layas/Ayas/Lajazzo. 86 places have a bare non-canonical form in a narrative chapter (245 occurrences; `plans/status/gazetteer-name-diff.md`), and 103 first mentions of a book form carry no gloss. A policy that only changes the gazetteer would leave the series inconsistent.
3. **"Visited" and "where is it" were one column.** The old `reliability` also carried identification doubt (`uncertain`), and `notes` mixed aliases, tradition and caveats. Two columns now: `reliability` (did Polo go?) and `id_confidence` (firm / probable / disputed / unfixed).
4. **A single `book_name` cannot be a key.** Two places share *Sinju* (Xining in Vol. I, Yizheng in Vol. II) and two share *Vuju* (Huzhou, Jinhua), so rows need an `id`, with `-1` / `-2` suffixes where forms clash.
5. **Coordinates existed for things that have none.** The Arbre Sec centroid (Dasht-e Kavir) and the Maldives for Male were placeholders a map would have shown as fact. They are blank now.
6. **The conflicts, resolved from Yule** (table and sources in `tasks/cross/GAZ-gazetteer.md`):
   - Cachanfu is Puzhou/Hezhong on the Yellow River; the old row's Xi'an is Kenjanfu. The unused "Pazanjin / Hezhong" row was the same place and is merged.
   - Cacanfu is Hejian (Hebei), not Puyang/Heze.
   - Caugigu: Yule reads the *description* as Upper Laos (Kiang Hung) and the *name* as Rashid's Tonkin (Kiaochi). The chapters and `map-caugigu.jpg` follow Kiang Hung, so the row does too, `disputed`.
   - Nanghin: Yule (note 1, ch. LXIX) prefers Ngan-king (Anqing) because Nan-king did not bear that name in Polo's time. The chapter follows Yule; Nanjing becomes an alias.
   - Male and Female is a legendary pair the chapter refuses to equate with the Maldives (III-m3).
   - Badakhshan's alias "Balashan" is not Polo's name; the form is Badashan (I-M8).
7. **About 86 rows were missing, not 70** (Vol. I 34, Vol. II 41, Vol. III 11; five of them region labels such as Persia, Cathay, Manzi). Every one is used by at least one chapter. Names with no identification stay in as `unfixed` with blank coordinates (12 rows), so a map skips them instead of faking a point.
8. **Not every identification is settled.** 58 rows are `probable` (Yule's reading, or a county-seat point) and 23 are `disputed`. Nothing was checked against a second source beyond Yule/Cordier and general reference, and the S-16/17/18 research had not been run, so verification is left to `GAZ.T6`.
9. **Where Yule and the chapters differ,** the form both the chapters and Yule's heading use won: Yanju, Ganfu, Kinsay. Yangiu, Ganpu and Quinsay stay as aliases. Kisi (Yule's text) was chosen over Kish, which the chapters use more often, because Kish is the modern gloss.
10. **A possible chapter slip found on the way:** ch-11 mentions a "little Caiju" opposite Coiganju; Yule has a single Caiju, at Kwa-chau (ch-12). Logged in `GAZ`.

## Decision
_Closed 2026-10-22._

- **Authority:** `gazetteer.csv` v2. `book_name` = Yule's form as used in the chapters; `aliases` (`;`-separated) = every other spelling; `modern_name` = the gloss. Schema `id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,id_confidence,chapters,notes`; `chapters` is generated by `tools/gazetteer.py chapters`.
- **Rows:** 112 → 195. Region labels are rows but not points. `unfixed` rows have no coordinates and are not plotted; `disputed` rows carry the chapters' reading, with candidates in `notes`.
- **Gloss rule:** book form + modern gloss on first mention per chapter; then the book form only. No gloss for Venice, Genoa, Java, Aden, Acre or region labels. Bare non-canonical forms are not allowed in narrative prose; quotations, Notes and tables are exempt.
- **Exemptions:** front/back matter and the reception chapters (III-10 to III-12) may use modern forms in prose; Polo's own places there still take the book form on first mention. Front-02 tables are generated (`GAZ.T5`), never hand-edited.
- **Lint:** `name_policy` (narrative profile, `tools/lint.py`) warns on a bare non-canonical form and on a first mention with no gloss. It is a **warning** until each chapter has had its naming pass, then an error (`GAZ.T7`). The older `names` spelling-closeness check stays, now seeded with aliases. Pass/fail is unchanged: baseline is still 1/49.
- **For S-02:** `gazetteer.variant_forms()` and `bare_variants()` are what the lint calls; its thresholds block needs nothing else.

## Tasks created on close
- [x] `GAZ.T1`–`T4` (schema, Yule forms and aliases, missing rows, conflicts) are **done in this spike**. `GAZ.T5` front-02 tables regeneration, `GAZ.T6` coordinate and identification verification (after S-16/17/18 intake), `GAZ.T7` promote `name_policy` to an error: in `tasks/cross/GAZ-gazetteer.md`.
- [x] Naming item in every chapter's task file: the narrative chapters' `.T3` (re-voice) carries a **Naming (S-04 ✓)** step with that file's bare variants and unglossed first mentions; the front/back files and the essay (no `.T3`) get a new `<ID>.T1 — Names to the S-04 policy`. Each *Naming and gazetteer* backlog section links to it.
- [x] `MAP` and `GLO` task files note that S-04 no longer gates them (S-08/S-09 still do).
