# II-15 — Great Turkey, Caidu's Daughter, and the Wars of the Ponent

**File:** `vol-2/ch-15-great-turkey-ponent.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,143 | 52% | [R] | 10/10; Note [6] mismatches body (1294 vs 1295) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 52%. Scorecard: 7 hinges, "You must know" ×2; verdict "Sensible compression; Kiacatu/Casan slips". Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-15 (whole)

### Factual / fidelity
- **[m]** Kiacatu called "an uncle of his — own brother, the better texts will say, to Abaga", which makes the "better texts" endorse the error, while :35 correctly says Geikhatu was Arghun's *brother*. Fix: "an uncle of his, the Book says — in fact his own brother, Geikhatu". — vol-2 m1 · ch-15:33; content plan W2 (II-15)
- **[m]** Baidu "his uncle" left uncorrected (he was a cousin, grandson of Hülegü through Taraqai). — vol-2 m1 · ch-15 (Baidu passage); content plan W2 (II-15)
- **[m]** :27 compresses Arghun's victory over Baraq (Baraq d. 1271) and Abaqa's death (1282) into "no long time passed". Fix: add a clause. — vol-2 m1 · ch-15:27
- **[N]** "Pharaoh's rat" has no gloss (Yule: a marmot or jerboa type). — vol-2 N7 · ch-15:37
- **[m]** (S-05) Baidu "seized the throne in the year 1294": he took it in spring 1295, after Kiacatu's murder (March 1295), and held it until October; the 1294 date is the same slip as Casan's. Kinship: the body's "his uncle the Great Kaan" (Caidu of Cublay, :13) is the Book's loose usage: Caidu was a grandson of Ögedei, so Cublay was his father's cousin. Gloss once or let stand as the Book's word. — registry `baidu`, `kaidu` · ch-15:13, :33

### Dispute handling and Ramusio flags
- **[M]** Marker mismatch: body says "Casan began to reign in the year 1294", but Note [6] gives "✓ Gházán's victory 1295 sound"; the 1294 figure is never marked ✗ (Ghazan acceded in 1295). — vol-2 M7 · ch-15:33, Note [6] ch-15:67; content plan W2 (II-15)

### Voice and prose
- **[M]** Recap padding: chapter ends with a recap paragraph ("Thus Book IV, compressed, closes Volume II's horizon: …"). Fix: cut to at most one sentence, or remove. — vol-2 M4 · ch-15:51
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-15 (whole)

### Notes and apparatus
- — see M7 (Note [6])

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Lac (Wallachia, per Yule's index). — vol-2 M11, N7 · ch-15:43
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-15.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 11 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Aijaruc throws the prince — GEN, Ilkhanid (*Jami' al-Tawarikh*), landscape 4:3; must get right: Kaidu's court, wagered horses; caption: folkloric; historical name Khutulun — see `illustration-plan.md`. Anchor ch-15:23.
- **Secondary plates:** GEN Dog-sledge post (plan; anchor :39, six dogs to a sledge, bear-skin for the courier). Critique §4 candidate: Land of Darkness raid (:41; legendary geography).
- **Maps:** A14 The Mongol horizon (Ilkhanate, Chagatai and Kaidu, Golden Horde, "Land of Darkness" dotted). Existing `map-asia-mongol-empire.jpg` / `map-mongol-empire.gif` suggested by critique §5; the multimedia plan **replaces** them (too small; date range unverified).
- **Timelines / diagrams / tables:** C8 Ilkhan succession: the Book vs the record (critique timeline: Abaqa d. 1282; Tegüder 1282–84; Arghun 1284–91; Geikhatu 1291–95; Baidu 1295; Ghazan 1295). Critique §5 also lists a "Golden Horde khan list (Book vs actual)" table; it has no D-row in `multimedia-plan.md`.
- **Characters appearing:** Caidu (Kaidu), Aijaruc (Khutulun), Kublai (Cublay), Chinghis Khan, Argon (Arghun), Abaga (Abaqa), Acomat (Tegüder Ahmad), Kiacatu (Geikhatu), Baidu, Casan (Ghazan), Barac (Baraq), Alau (Hülegü), Barca (Berke), Batu, Toctai (Tokhta), Nogai, Conchi, Nomogan (Nomukhan), Cocachin (mentioned), Marco Polo, Rustichello
- **Character check (S-05):** Aijaruc c. 20–30, very tall, unmarried in the scene (braids, no *boqta*); Caidu c. 45–55. Cards: `plans/registry/character-cards.yaml`.

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (✓/✗ on Note [6])
- S-04 Gazetteer authority and naming policy (Lac; A14 places)
- S-05 Character registry (Ilkhan names, kinship, regnal dates; Aijaruc/Khutulun in hero)
- S-06 Fact verification sheet (Kiacatu, Baidu, Ghazan 1295, Baraq/Abaqa dates)
- S-08 LaTeX build pipeline (plates, map, diagram)
- S-09 Map and diagram pipeline (A14, C8)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-15.T1` Factual fixes (Kiacatu, Baidu, Ghazan, Baraq/Abaqa clause, N7)
- `II-15.T5` Media placement (hero, secondary, A14, C8)
- `II-15.T6` Lint pass and human voice read

### II-15.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #11 (batch 3)
- **Now:** 3,099 words · 52% verbatim · "You must know" 2 · "Anyway" 3 · formula hinges 2 · archaisms 3 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :13 (83%), :21 (97%), :23 (84%), :37 (90%), :41 (94%), :43 (73%).
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :25, :35, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Dry Tree → Arbre Sec ×1, Samarcand → Samarcan ×1, Russia → Rosia ×1; unglossed first mentions: Cambaluc, Chipangu. `python3 tools/lint.py -v vol-2/ch-15-great-turkey-ponent.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: Alau → Alaü ×3, Arghun → Argon ×2, Chagatai → Sigatay ×1, Chaghatai → Sigatay ×2, Geikhatu → Kiacatu ×1, Kaidu → Caidu ×1, Kublai → Cublay ×3, Ulatai → Oulatay ×2; unglossed first mentions: Aijaruc (Khutulun), Barca (Berke), Cocachin (Kököchin). The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-15.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-15.T3` (the flags are written during the re-voice pass)
- **Now:** 0 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-15-great-turkey-ponent.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-15.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-15.T3` (re-voice renumbers Notes)
- **Now:** 10 Notes · 0 ★ · 0 without a lead marker · tag [R]
- **Do:**
  - Tag line `**[R]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - Run `python3 tools/lint.py -v vol-2/ch-15-great-turkey-ponent.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-15.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 11 errors · 3 warnings — failing: archaism, asides, budgets, quote_verify, verbatim, you_must_know; warnings: recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-15-great-turkey-ponent.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
