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
- Waiting on research: costume entries from S-22 (headgear, hair, armour by period) to refine the `dress` lines; family facts from S-15; dates from S-14.

## Gated by spikes
S-05 ✓ (closed 2026-10-22) · S-06 (verified dates, for `CHR.T4`) · S-15 (family) · S-22 (costume, for `CHR.T5`)

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
- **Status:** backlog · **Depends:** S-06 (and its research S-14), S-15
- **Do:** for each row with `verify`, carry the S-06 / S-15 verdict into `dates`, `relations` and `book_says`, then remove the spike from `verify`. Update the *Contested facts* table in `registry/characters.md`. Where a verdict changes an age (Niccolò's or Maffeo's birth, Donata's marriage), re-run `ages` and adjust the cards.
- **Done when:** no row's `verify` names a closed spike; `check` and `ages` pass.

### CHR.T5 — Costume refinement from S-22
- **Status:** backlog · **Depends:** S-22 intake
- **Do:** take S-22's costume entries (Mongol court robes, *boqta*, Venetian dress c. 1270–1324, Ilkhanid and Yuan armour) into the cards' `dress` and `avoid` lines. Content only: no actor's or manga character's likeness (S-22 rule 3).
- **Done when:** each card's dress lines cite an S-22 entry or a period source.

### CHR.T6 — Consistency sweep and promotion to error
- **Status:** backlog · **Depends:** every narrative chapter's `.T3` (each carries a **People (S-05 ✓)** step)
- **Do:** after each W4 batch, run `tools/characters.py chapters` and `report --md > plans/status/character-name-diff.md`. When the last narrative chapter has had its pass, make the people half of `name_policy` an error, together with `GAZ.T7`.
- **Done when:** the report shows 0 bare variants and 0 unglossed first mentions; the rule is an error.
