# CHR — Characters

**Status:** complete (2026-11-24). T3 and T6 are done, and T7 is closed best effort under the final access decision. The remaining uncertainties are recorded below. · **Plan doc:** S-05, `registry/characters.md` and `illustration-style-guide.md` § Recurring figures

## Scope
The recurring people of the book, as one source of truth for **text** (names, dates, relationships, titles) and **images** (age, dress, attributes per tradition). Scholars (Yule, Wood…) are out of scope; they belong in the bibliography.

**Authority:** `registry/characters.yaml` (54 people) and `registry/character-cards.yaml` (26 cards, the Polo itinerary, 22 plate scenes). Tooling: `python3 tools/characters.py check | ages | cue | chapters | report`. The lint's `name_policy` reports character-name errors with the *(S-05)* tag.

## Earlier findings and ongoing maintenance
- Findings from the original text review (chapter tasks and registry rows retain the audit trail):
  - Berke vs Hulagu outcome (I-2).
  - Chagatai as "brother" of the Kaan (I-7).
  - Aung Khan's defeat (I-12).
  - Nayan's descent: Otchigin, not Belgutai (II-1).
  - Chingkim's death date (II-2; S-06 still open, hedge "mid-1280s", `registry/facts.md` F-06).
  - Kiacatu / Baidu / Ghazan (II-15); Baidu's 1294 too (S-05).
  - "Po-lo" = Bolad, not Marco (II-5, II-11, III-12; `HOT.3`).
  - Donata Badoer (III-10); Niccolò's sons (III-10, S-05).
  - Maffeo's marital status (I-2): his edited will names Marta as his late wife. See T7 and F-17 for the limits of the evidence.
  - Baibars's dates (I-3, F-39): the registry and Note [10] attribute the reign of 1259–1276 to Yule. The other dates remain unverified in the fact sheet.
  - Argon's death (III-9, S-05): 10 March 1291 in the registry and chapter.
  - Rustichello’s lay or clerical status is unverified (I-1 plate; S-15).
- Visual: cards exist for Marco, Niccolò, Maffeo, Rustichello, Cublay, Chabi, Chinghis, Alaü, the Caliph, Bayan, Nayan, Caidu, Aijaruc, Cocachin, Casan, Tedaldo, Donata, Peter the Tartar and Cepoy, and since 2026-11-19 for Unc Can (Toghrul), Oulatay, Apusca, Coja, Fantina, Bellela and Moreta. Each card has an accepted house sheet in `media/characters/`. Kublai ages from about 50 (I-2) to about **76** (III-9), not 78.
- Co-presence: `tools/characters.py ages` proves no Polos at Xiangyang (II-11), no Chabi after 1281 (II-03), no Argon at the bride's arrival (III-9 secondary). The text, not the itinerary, keeps the Polos off the Nayan field (II-01) and out of Bayan's camp (II-10).

## Gated by spikes
S-05 ✓ (registry) · S-08 ✓ (glossary layout) · S-15 ✓ (family research, best effort) · S-22 ✓ (costume cues)

## Tasks

### CHR.T1 — Registry file
- **Status:** done (in S-05, 2026-10-22)
- **Did:** `registry/characters.yaml` (54 people: book form, gloss, variants, other names, dates, role, relations, `book_says`, `verify`, generated `chapters`); `tools/characters.py`; `name_policy` people rule in `tools/lint.py`; `status/character-name-diff.md`.

### CHR.T2 — Visual cards for plate figures
- **Status:** done for the 26 recurring figures (2026-11-19: the 19 from S-05, plus Toghrul, Oulatay, Apusca, Coja, Fantina, Bellela and Moreta, taken from their accepted sheets; their dress lines are working conventions). Keep extending it with each new plate.
- **Did:** `registry/character-cards.yaml`: likeness, house conventions, attributes, dress by period, per-tradition rendering, avoid-list; the Polo itinerary; 22 scenes.
- **Do next:** when a plate with a person is added to `illustration-plan.md`, add its scene to the cards file and run `tools/characters.py check`.
- **Done when:** every GEN plate showing a recurring person has a scene row, and `ages` reports 0 problems.

### CHR.T3 — Glossary entries for people (with `GLO`)
- **Status:** done (2026-11-24). All 24 registry people with a `gloss` have a checklist row and appear in the glossaries for their assigned volumes, alongside the place and term entries. Abaga now also appears in Volume I, where I-02 names him.
- The glossaries retain GLO's alphabetical layout and selective pronunciation hints. The pronunciation and publication review remains with GLO.

### CHR.T4 — Contested facts to verdicts
- **Status:** done (2026-10-22) for everything research could settle
- **Did:** two research runs, graded in `research/results/CHR-people-intake.md` (run 1: leads only) and `CHR-people-2-intake.md` (run 2: claims read against Yule, two DOIs and the Formentin–Schiavon article; 8 of 11 hold). Settled and written into the registry: Argon's death (10 March 1291), Marco's death (8 or 9 Jan 1324), Fantina's marriage and suit, Niccolò's illegitimate sons, Yule's report of Maffeo's 1309 will (now qualified by S-15), the Zhenjiang churches, the Arghun envoys' notice. `verify` cleared on `fantina`; the other pointers stay with the spikes that own those topics (S-14, S-15).
- **Left over:** the facts no search run could settle moved to `CHR.T7`.

### CHR.T5 — Costume refinement from S-22
- **Supplement leads:** Met helmet 1999.158 is Mongolian or Tibetan and dated broadly 13th–15th century; the lacing date does not establish manufacture in Polo's years. `chuluun2024reconstruction` concerns a Balar's Khad deel, but its artifact date and methods remain to be checked. See `registry/visual-references.md` § Supplement; do not add either as a card cue yet.
- **Status:** done (2026-11-18) for every dress line a viewed cue or a read report covers · **Depends:** —
- **Also did (2026-11-18):** The S-22 follow-up ran but failed its intake, so nothing from it was used. Venetian dress comes from C39 instead, for `marco` 1296–1324 and `donata`. Armour comes from the Takashima 1281 finds (text, Matsuura Report 4) for `bayan` and `nayan`, and from C37 (c. 1299, late) for `hulagu`. **Left as is:** the young Marco and Niccolò travel dress, Tedaldo, Rustichello, Peter, Cepoy and Chinghis, because no viewed source covers them. The draft Cocharelli cue C43 (c. 1330–40) has not been accepted.
- **Did (2026-11-18):** C1 into `marco` 1275–91 (Niccolò and Maffeo inherit it) and `kublai` court; C2 into `chabi` court and `cocachin` Persia; C3 into `kublai` hunt; C4 as a new `chabi` riding line and into `cocachin` 1290–93 (as a comparison only). The S-22 `[AVOID]` lines (barbarian fur-and-leather dress; loose hair or tiaras) were added to `kublai`, `chabi` and `cocachin`. `characters.py check` and `ages` show 0 problems. The bust portraits in `media/reference/s22/` have still not been examined.
- **Handed over by S-22:** cues C1 (court men), C2 (married court women, *boqta*), C3 (Cublay outdoors, from the 1280 hunting scroll) and C4 (a court woman riding: braids, no *boqta*) in `illustration-plan.md` § S-22 period cues; the images behind them in `media/reference/s22/` (the Khubilai and Chabi bust portraits are there too, not yet looked at closely). **Nothing yet** for Venetian dress or for Ilkhanid and Yuan armour: the follow-up prompt for them ran and failed intake; see Also did.
- **Do:** take S-22's costume entries (Mongol court robes, *boqta*, Venetian dress c. 1270–1324, Ilkhanid and Yuan armour) into the cards' `dress` and `avoid` lines. Content only: no actor's or manga character's likeness (S-22 rule 3).
- **Done when:** each card's dress lines cite an S-22 entry or a period source.

### CHR.T7 — Library checks for the open people facts
- **Status:** done, best effort (2026-11-24), under the [final access closure](../../../../research/investigations/results/FINAL-ACCESS-intake.md). The registry, chapters and cards use the readings and hedges below. The archive and library gaps are recorded for reference.

  | Person | Wording in use | Evidence and limits |
  |---|---|---|
  | Chabi | Birth year and age unspecified. | *Yuan shi* 106 and 114 give no birth year. The 1216 and 1227 leads remain unverified. |
  | Dorjé | Cublay’s eldest son. His mother and birth year are unknown (II-02 Note [11]). | *Yuan shi* 107 gives his rank among the sons. The biography of Chabi in juan 114 names Chinkin as her son. |
  | Coja | Ramusio names him as the sole surviving envoy. The Chinese provisioning notice leaves survival open (III-09). | Cleaves 1976, p. 181, was checked. The rest of the article and the notice itself were unavailable for direct inspection. |
  | Maffeo | The edited 6 February 1310 will names his late wife Marta and two spiritual daughters. His children, if any, are unverified (I-02 Note [3]). | Orlandini 1926, doc. 6, checked in OCR. Yule’s earlier date comes through a separate 1328 proceeding whose record was unavailable. |
  | Bellela | Bertuccio Querini was her husband. Her exact death year remains open (III-10 Note [15]). | Bolognari 2020 cites Gallo’s 1326–27 records. Reconciliation of the dates requires the underlying records. |
  | Marco | Born c. 1254 by inference. Agnese’s identification as his daughter remains possible (III-10 Note [16]). | Moule–Pelliot I for the inferred birth year. Bolognari 2021 and the 1319 will were unavailable for direct inspection. |
  | Rustichello | Lay or clerical status is unspecified. The card labels his dress a convention. | No source seen establishes his status. |
  | Peter the Tartar | The will is Marciana Cod. Lat. V, 58 (=2437), no. 33. | Bartoli Langeli’s 2019 edition was read. The original and live catalogue were uninspected. |

### CHR.T6 — Consistency sweep and promotion to error
- **Status:** done (2026-11-24). The naming sweep covered all 37 in-scope narrative chapters. Updated the registry's chapter references, added Baibars to the aliases for Bundukdar, and regenerated the [naming report](../../status/character-name-diff.md). The report and lint share the first-mention check.
- **Verified:** 0 bare variants, 0 missing first-mention glosses, and both findings now fail `name_policy` with the *(S-05)* tag. The separate human voice read remains with each chapter.


### CHR.T8 — Reference list per card
- **Status:** done (2026-11-19). Every one of the 26 cards has a `references:` list with `cue`, `source`, `use` (`own sheet` / `edit OK` / `look only` / `not saved` / `text`), `seen` and `for`. `characters.py check` fails on a card without references, on a bad `use`, or on a saved file missing from `media/`. `cue` prints the files, `[INPUT]` for those that may be attached and `[LOOK]` for the rest. Sources not yet examined closely are marked so in `seen`, not left out: the NPM busts and Or.MS 20.
- **Why:** a card's `likeness` is one line of prose. The sources behind a figure are spread across `media/references/README.md`, `registry/visual-references.md` (cues C1–C50) and the S-22 and S-23 intakes. A prompt writer has to find them again for every plate.
- **Do:** give each card in `registry/character-cards.yaml` a `references:` list. Each entry holds `cue` (a C-number, or none), `source` (a local file under `media/references/` or `media/reference/s22/`, or a URL), `use` (`edit OK` / `look only`, as in the references README), `seen` (viewed / text only / not seen) and `for` (face, court dress, hunt dress, armour, idiom). Only list sources that are viewed or read; a lead goes in `verify`, not here. Teach `tools/characters.py check` to fail on a local path that does not exist, and have `cue` print the list under `[PERIOD]`.
- **Done when:** every one of the 19 cards has a list, an empty list states why (for example "no period image: Polo"), and `check` shows 0 problems.

### CHR.T9 — Character reference sheets (images)
- **Status:** done (2026-11-18): 23 sheets accepted by the user. That is the 19 cards, plus Toghrul, Arghun's envoys and the Polo daughters, which have no cards yet. Each card's `likeness` now names its sheet. Four sheets (Donata, Chabi, Peter, Nayan) were re-made once, and their v1 files are kept. Sidecars and `media/ATTRIBUTIONS.md` § Character reference sheets record the prompts, inputs and reviews. The agent prompts are `media/characters/AGENT-PROMPT.md` and `CORRECTIONS-2026-11-18.md`.
- **What a sheet is:** a working reference that keeps a figure consistent from plate to plate, drawn in the figure's main tradition (Yuan for the court, Gothic for Venice, Ilkhanid for Persia). Each sheet shows the figure in one or two dated dress lines from the card, on a plain ground. **It is never printed as a plate** and never captioned as a likeness.
- **Do:** for each of the 19 cards, in this order: Cublay, Chabi, Marco (1275 and 1296), Niccolò and Maffeo (one sheet), Cocachin, Bayan, Nayan, Alaü, Casan, then the rest:
  1. Write `media/characters/prompts/<id>-<year>.txt` from `tools/characters.py cue <id> <year>` and the style-guide template. Put the avoid lines in the prompt's "Do not include" line. Attach the card's `edit OK` references (rule 9), never a `look only` file.
  2. Generate, then review against the style-guide checklist, items 1–3 and 5. Faces must match the card's `house` line.
  3. Save `media/characters/<id>-<year>-sheet.<ext>` with a sidecar `.yaml`: prompt, model, date, tradition, the reference files used, and one review line per item.
  4. When a sheet is accepted, cite it in the card's `likeness` as the house reference for later plates (an image input to an edit is allowed for our own sheets).
- **Done when:** every card whose figure appears in a GEN plate has an accepted sheet. Polo-family sheets say "house convention, no authentic likeness" in the sidecar.
- **Settled (2026-11-18):** style-guide rule 9 now allows `edit OK` reference files and our own accepted sheets as image inputs; `look only` files never. List every attached file in the sidecar.

The [S-15 intake](../../../../research/investigations/results/S-15-external-intake.md) also records Moreta’s second marriage per Gullino, Andrea’s name in Ramusio, and the uncertainty over Donata’s marriage year. See [F-17](../../../../research/registry/facts.md#s-14-claims) for the updated Maffeo evidence.
