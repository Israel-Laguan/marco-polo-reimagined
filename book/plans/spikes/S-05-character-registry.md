# S-05 — Character registry

**Status:** closed and **finalized** 2026-10-22 (research intake done) · **Timebox:** 1–2 sessions · **Gates:** `CHR` tasks; character consistency in chapter tasks; every plate showing a recurring person (`PLT`)

## Question
Who are the recurring people of the book? What are their canonical names (book form / modern form), key dates, ages at each depicted event, and roles? And how should each be drawn consistently across very different art traditions?

## Why it matters
- **Text:** errors already cluster on people. Nayan's descent, Kiacatu and Arghun, Baidu, Chingkim's death date, Donata Badoer, Maffeo's marriage, Rustichello as a layman.
- **Images:** Marco appears in plates painted in Gothic, Persian, Yuan and Venetian idioms. Without visual anchors (age, dress, attributes) he becomes a different man in each. Kublai ages from about 50 to about 78 across the plates.

## Inputs
- Chapter backlogs § Media hooks → "Characters appearing"
- Critique period notes (dress, ages); Yule's Introduction; S-06 fact sheet

## Method
1. Compile the cast from the chapter backlogs and rank by number of appearances.
2. For each recurring figure (expected ~25): book name / modern name; dates; title(s); relationship; chapters; contested facts (link S-06).
3. Visual spec for figures that appear in plates: age at each depicted event; dress by period and place; fixed attributes (e.g. Marco's merchant's purse and paiza after 1275; Kublai's white fur robe from the NPM portrait); how each tradition renders them.
4. A timeline of who is where when, to catch impossible co-presence (e.g. no Polos at Xiangyang).

## Output (definition of done)
- [x] `plans/registry/characters.yaml` (scripts read it: `tools/characters.py`, the lint) + method note `plans/registry/characters.md`
- [x] Per-figure visual cards for plate prompts: `plans/registry/character-cards.yaml` (19 cards, itinerary, 22 scenes)
- [x] List of text inconsistencies found → chapter backlogs (factual items; a **People (S-05 ✓)** step in every narrative `.T3`; `plans/status/character-name-diff.md`)

## Feedback to plan
- `illustration-style-guide.md`: add a "recurring figures" section
- `illustration-plan.md`: plate prompts reference the character cards

## Findings
_2026-10-22. Method: every "Characters appearing" line in the chapter backlogs; the prose of all 49 files through the lint's own paragraph filter (Notes, quotations and tables excluded); Polo's text in `refs/` (unindented lines, i.e. not Yule's notes) for the forms; the three critiques' period notes. S-06, S-14 and S-15 are still open, so dates come from Yule–Cordier and standard reference, and every contested one carries a `verify` pointer instead of a verdict._

1. **People have the problem places had before S-04, only worse.** The prose names Kublai as *Kublai* 57 times and *Cublay* 40; Hulagu as *Hulagu*, *Hülegü*, *Alau* and *Alaü*; Chinggis three ways. Chapters switch form inside a paragraph. At close, 26 people have bare variants in the narrative chapters (120 occurrences), and 12 first mentions lack a gloss. Even the reference chapter II-2 glosses *Chinkin (Chingkim)* and then uses *Chingkim* bare twice.
2. **The policy already existed, implicitly.** The voice guide's example opener is "Cublay Kaan is not drawn as a giant", and II-2 writes *Chinkin (Chingkim)*. So people follow the S-04 rule: Yule's form where Polo names the person, a gloss on first mention, no bare variant. The new piece is what to do where Polo names nobody (Chabi, Bolad): use the modern form. Europeans keep their modern forms (*Niccolò*, not Yule's *Nicolas*/*Nicolo*; *Rustichello*, not *Rusticiano*), as Venice and Genoa do.
3. **Names collide.** *Bayan* the general and *Baian* the huntsman are two men. *Ahmad* is both Achmath and Acomat (Tegüder Ahmad). I-12's *Argons* are a people. *Prester John* was already a legendary gazetteer row. The tool keeps one form per person, ignores a short form inside a longer one, and has a per-file exclusion (`SCOPE_OUT`). *Prester John* stays with the gazetteer.
4. **The cast is smaller than it looks.** 54 people are worth a registry row; only about 25 recur (two or more files). Marco is in 48 files, Cublay 19, Rustichello 13, Niccolò and Maffeo 12, Cocachin 10, Chinghis and Alaü 9. Everyone else is in seven or fewer. Ramusio (164 mentions) and Pipino are sources, not characters, and stay in the bibliography.
5. **Ages, computed rather than guessed.** Marco is 17 at Layas, 21 at Kemenfu, 37 at the 1291 departure, 44 in Genoa and about 69–70 at the will. Cublay is about 50 at the brothers' audience and 60 at Marco's arrival (the plan's figure is right), 72 at the Nayan battle (right), and about **75–76** at the III-9 departure, not the 78 the CHR backlog assumed. Niccolò's and Maffeo's birth years are unknown, so their cards carry an apparent age.
6. **Co-presence can be checked, not just remembered.** A coarse itinerary (regions by year) proves the important absences: the Polos were still on the road when Xiangyang fell (March 1273); Chabi died in 1281, before any White Feast set later; Argon died before the bride sailed. Absences that rest only on the text (no Polos on the Nayan field or in Bayan's camp, no Donata at the 1295 homecoming) are recorded as `not_shown`.
7. **One plate entry was wrong.** The III-9 hero put Cocachin in a *boqta*. The *boqta* is a married woman's headdress, and Cocachin was still a bride at Cambaluc and Zayton. She marries Casan only in Persia (1293/94). Corrected in `illustration-plan.md`; the farewell secondary keeps it.
8. **No Polo has an authentic likeness.** The Doria Pamphilj portrait and the 1477 woodcut are inventions. So the cards fix *attributes* rather than faces: the youngest of three Latins, the belt-purse, a paiza only after 1275, Cublay carried after 1280. Each card also says how each tradition draws the figure: a Frank in Ilkhanid painting, a western foreigner in Yuan painting, a French gentleman in the LdM lens. Those attributes are what hold a figure together across idioms.
9. **New text items** (in the chapter backlogs, tagged S-05): Baidu's 1294 (II-15); Caidu's "uncle the Great Kaan" (loose kinship); Argon's death day (III-9); Niccolò's sons and Maffeo's dates (III-10). The ten people errors the critiques found are each now attached to a registry row (`book_says`).

## Decision
_Closed 2026-10-22._

- **Authority:** `plans/registry/characters.yaml` for names and dates; `plans/registry/character-cards.yaml` for cards, itinerary and plate scenes; method note `plans/registry/characters.md`. YAML, because scripts read it.
- **Naming:** the S-04 rule applied to people. Book form = Yule's form of Polo's text where he names the person, else the modern English form; Europeans in their modern form. Gloss once per chapter on first mention (none where the forms coincide or differ only by a diacritic). No bare variants in narrative prose; `also` names (titles, the pope's two names) are never variants. Same exemptions as places: front/back matter and III-10 to III-12.
- **Lint:** `name_policy` checks people too (`tools/characters.py` hook), as **warnings** tagged *(S-05)*, until every narrative chapter has had its pass (`CHR.T6`, with `GAZ.T7`). Pass/fail unchanged: 1/49.
- **Plates:** every prompt with a recurring figure takes its `[PERIOD]`/`[AVOID]` lines from `tools/characters.py cue <id> <year>`; every such plate has a scene row that `tools/characters.py ages` must pass. Cards fix attributes and per-tradition rendering, not faces; `house` conventions are never captioned.
- **Facts:** the registry records dates and relations with a `verify` pointer; it does not settle contested facts. That stays with S-06/S-14/S-15 (`CHR.T4`).

**Feedback applied:** `illustration-style-guide.md` § Recurring figures (new) and the prompt template's `[PERIOD]` slot; `illustration-plan.md` (cards note, pipeline step, III-9 *boqta* fix, Pilot 1 prompt with the Polos' card lines); `VOICE-GUIDE.md` § Naming (people); `content-revision-plan.md` (lint note; W5 People); `GLO`, `PLT`, `CHR` task files; README board and decision log.

## After close: research intake (finalized 2026-10-22)
A search-based run on the 28 `verify` claims came back and was graded as leads, not sources (`research/results/CHR-people-raw.md`, `CHR-people-intake.md`): 48 bibliography entries, all site pages; two of seven spot-checked claims failed (Maffeo's "daughter Fiordelisa" is Niccolò's wife; a death on 8 January contradicts a will of 9 January). The registry took only marked leads, and Chabi's age is now blank (birth 1216 or 1227). A stricter prompt for 12 open rows is in the intake note.

Run 2 (`CHR-people-2-intake.md`) cited real works and was checked claim by claim against Yule, two DOIs and the Formentin–Schiavon article: 8 of 11 claims hold. It settled Argon's death (10 March 1291), Marco's (8 or 9 January 1324), Fantina's marriage, Niccolò's illegitimate sons and Maffeo's 1309 will, and turned up a fourth daughter, Agnese (2021 find, not yet seen). `CHR.T4` is done. **The facts still open need a library, not a search run: they moved to `CHR.T7`, with the family rows handed to S-15.** Nothing further is pending in this spike.

## Tasks created on close
- [x] `CHR.T1` registry and `CHR.T2` first 19 cards: **done in this spike**. `CHR.T3` glossary entries (with `GLO`), `CHR.T4` contested facts to verdicts (after S-06/S-15), `CHR.T5` costume refinement (after S-22), `CHR.T6` consistency sweep and promotion to error: in `tasks/cross/CHR-characters.md`.
- [x] **People (S-05 ✓)** step in every narrative chapter's `.T3` (37 files, with that file's bare variants and unglossed first mentions; the two reception chapters get the exemption note).
- [x] Character fixes in the chapter backlogs' *Factual / fidelity* (II-15, III-9, III-10) and **Character check** lines in the Media hooks of I-01, I-03, II-01, II-03, II-11, II-15, III-09, for each chapter's `.T1` and `.T5` when those are written.
