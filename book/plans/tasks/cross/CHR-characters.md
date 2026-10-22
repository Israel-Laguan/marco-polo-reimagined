# CHR — Characters

**Status:** ready (S-05 closed 2026-10-22) · **Plan doc:** S-05; `registry/characters.md`; `illustration-style-guide.md` § Recurring figures

## Scope
The recurring people of the book, as one source of truth for **text** (names, dates, relationships, titles) and **images** (age, dress, attributes per tradition). Scholars (Yule, Wood…) are out of scope; they belong in the bibliography.

**Authority:** `registry/characters.yaml` (54 people) and `registry/character-cards.yaml` (19 cards, the Polo itinerary, 22 plate scenes). Tooling: `python3 tools/characters.py check | ages | cue | chapters | report`. The lint's `name_policy` warns on people too, tagged *(S-05)*.

## Backlog
- Known text errors on people (each also in its chapter backlog; each registry row's `book_says` lists them):
  - Berke vs Hulagu outcome (I-2).
  - Chagatai as "brother" of the Kaan (I-7).
  - Aung Khan's defeat (I-12).
  - Nayan's descent: Otchigin, not Belgutai (II-1).
  - Chingkim's death date (II-2, unverified).
  - Kiacatu / Baidu / Ghazan (II-15); Baidu's 1294 too (S-05).
  - "Po-lo" = Bolad, not Marco (II-5, II-11, III-12; `HOT.3`).
  - Donata Badoer (III-10); Niccolò's sons (III-10, S-05).
  - Maffeo's marital status (I-2, unverified).
  - Argon's death day, 7 or 10 March 1291 (III-9, S-05).
  - Rustichello is a layman (I-1 plate).
- Visual: cards exist for Marco, Niccolò, Maffeo, Rustichello, Cublay, Chabi, Chinghis, Alaü, the Caliph, Bayan, Nayan, Caidu, Aijaruc, Cocachin, Casan, Tedaldo, Donata, Peter the Tartar and Cepoy. Kublai ages from about 50 (I-2) to about **76** (III-9), not 78.
- Co-presence: `tools/characters.py ages` proves no Polos at Xiangyang (II-11), no Chabi after 1281 (II-03), no Argon at the bride's arrival (III-9 secondary). The text, not the itinerary, keeps the Polos off the Nayan field (II-01) and out of Bayan's camp (II-10).
- Waiting on: costume entries from S-22 (headgear, hair, armour by period) for the `dress` lines; the open facts in `CHR.T7` (library checks; family rows via S-15).

## Gated by spikes
S-05 ✓ (closed and finalized 2026-10-22) · S-15 (family rows of `CHR.T7`) · S-22 (costume, for `CHR.T5`)

## Tasks

### CHR.T1 — Registry file
- **Status:** done (in S-05, 2026-10-22)
- **Did:** `registry/characters.yaml` (54 people: book form, gloss, variants, other names, dates, role, relations, `book_says`, `verify`, generated `chapters`); `tools/characters.py`; `name_policy` people rule in `tools/lint.py`; `status/character-name-diff.md`.

### CHR.T2 — Visual cards for plate figures
- **Status:** done for the first 19 (in S-05); extend with each new plate
- **Did:** `registry/character-cards.yaml`: likeness, house conventions, attributes, dress by period, per-tradition rendering, avoid-list; the Polo itinerary; 22 scenes.
- **Do next:** when a plate with a person is added to `illustration-plan.md`, add its scene to the cards file and run `tools/characters.py check`.
- **Done when:** every GEN plate showing a recurring person has a scene row, and `ages` reports 0 problems.

### CHR.T3 — Glossary entries for people (with `GLO`)
- **Status:** ready · **Depends:** S-08 (layout)
- **Do:** one glossary entry per registry person whose `gloss` is set (book form → modern form → respelling → one-line role from `role`), in volume order of first appearance. Respellings are house suggestions, reviewed by a person (same rule as places).
- **Done when:** `GLO.T1` lists the people beside the places; every `gloss` form has an entry.

### CHR.T4 — Contested facts to verdicts
- **Status:** done (2026-10-22) for everything research could settle
- **Did:** two research runs, graded in `research/results/CHR-people-intake.md` (run 1: leads only) and `CHR-people-2-intake.md` (run 2: claims read against Yule, two DOIs and the Formentin–Schiavon article; 8 of 11 hold). Settled and written into the registry: Argon's death (10 March 1291), Marco's death (8 or 9 Jan 1324), Fantina's marriage and suit, Niccolò's illegitimate sons, Maffeo's 1309 will, the Zhenjiang churches, the Arghun envoys' notice. `verify` cleared on `fantina`; the other pointers stay with the spikes that own those topics (S-14, S-15).
- **Left over:** the facts no search run could settle moved to `CHR.T7`.

### CHR.T5 — Costume refinement from S-22
- **Status:** backlog · **Depends:** S-22 intake
- **Do:** take S-22's costume entries (Mongol court robes, *boqta*, Venetian dress c. 1270–1324, Ilkhanid and Yuan armour) into the cards' `dress` and `avoid` lines. Content only: no actor's or manga character's likeness (S-22 rule 3).
- **Done when:** each card's dress lines cite an S-22 entry or a period source.

### CHR.T7 — Library checks for the open people facts
- **Status:** backlog · **Depends:** library or archive access; the family rows are picked up by **S-15**'s intake (listed in its *Inputs*)
- **Why here:** two research runs could not settle these (`research/results/CHR-people-2-intake.md` § Still open). Each needs a specific book or record seen, not another search run.

  | Row | Open question | Where to look | Owner |
  |---|---|---|---|
  | `chabi` | Birth 1216 or 1227 (age blank until then) | *Yuan shi* 114 (biographies of empresses); Rossabi 1988 | CHR.T7 |
  | `dorji` | Mother (Chabi or another wife); birth year | *Yuan shi* 107 (imperial genealogy) | CHR.T7 |
  | `coja` | Did any envoy survive besides Coja? | Cleaves 1976, full text (JSTOR) | CHR.T7 |
  | `maffeo` | Married? Children? (I-02's "bachelor") | Orlandini 1926 | S-15 |
  | `bellela` | Her husband (Bertuccio Querini is only a lead) | Orlandini 1926; the 1324 will in Moule–Pelliot 1938 I | S-15 |
  | `marco` | The daughter Agnese (b. 1295–99): see the article before III-10 changes; any document for 1254 | Bolognari, *Studi Medievali* 62 (2021) | S-15 |
  | `rustichello` | Was he a layman? (the I-01 plate assumes it) | Larner 1999; scholarship on the Arthurian compilation | S-15 |
  | `peter-the-tartar` | Shelfmark of the will, as seen | Plebani 2019; Marciana catalogue | S-15 |

- **Do:** for each row, see the source, write the verdict into `characters.yaml` (`dates`, `relations`, `book_says`), add the work to `registry/bibliography.bib` as `confirmed`, and update the *Contested facts* table in `registry/characters.md`. Where a verdict changes an age (Chabi, Dorjé), run `tools/characters.py ages` and adjust the cards.
- **Done when:** every row above has a seen source or an agreed hedge in the chapter text.

### CHR.T6 — Consistency sweep and promotion to error
- **Status:** backlog · **Depends:** every narrative chapter's `.T3` (each carries a **People (S-05 ✓)** step)
- **Do:** after each W4 batch, run `tools/characters.py chapters` and `report --md > plans/status/character-name-diff.md`. When the last narrative chapter has had its pass, make the people half of `name_policy` an error, together with `GAZ.T7`.
- **Done when:** the report shows 0 bare variants and 0 unglossed first mentions; the rule is an error.
