# I-01 — In a Genoese Prison: How This Book Was Made

**File:** `vol-1/ch-01-genoa-prison.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,011 | 7% | — (n/a in Vol. I) | ok [1–15] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** the critique calls ch-01 "the model the other chapters should follow": a real retelling at 7% verbatim, capture dispute "handled exactly right" (ch-01:21, Note [5]). It is the W4 voice model. Keep its strengths when touching it.

### Critical
— none found (C3: 7% verbatim, under the ≤25% target; this chapter is the model)

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- Hinge budget: "Anyway" ×2 (0 of them "Anyway, next he…"), over the M6 lint budget of ≤1 per chapter. Fix: at most one "Anyway"; close asides with a plain return. — vol-1 M6 · ch-01:21, :37
- Long academic dash-aside: 157 words. Fix: cap at ~60–80 words, keep one key fact plus a cross-reference to the Note, move lists of names to Notes. — vol-1 M11 · ch-01:21

### Notes and apparatus
— none found

### Naming and gazetteer
- "Venice (Venezia) and Genoa (Genova)": when the book form is the English form, the gloss is noise. — vol-1 nit 1 · ch-01:13
- Gazetteer lacks rows for **Genoa** and **Curzola** (both needed for the ch-01 map). Fix: add rows (M8 gazetteer fix). — vol-1 M8 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-01.T3`.

### Length and structure
— none found

## Media hooks
- **Hero plate:** I-1 Marco dictating to Rustichello — GEN, Italian Gothic illumination, P. Must get right: Rustichello a **layman** (not a monk), loose quires, quill, ink-horn, a civic room not a dungeon, *gonella* and mantle; Marco about 44. Caption: setting is tradition (Palazzo di San Giorgio is tradition only); do not label any figure as Ramusio's "Genoese gentleman". Anchor ch-01:27. Existing `drawing-genoa-dictation.png` has a monk's habit, chains and an anachronistic skyline (critique §4/§5); multimedia plan retires all `drawing-*.png`.
- **Secondary plates:** Dawn at Curzola (illustration plan; anchor ch-01:19): *galee sottili*, lateen rig, ~25 oar banks *alla sensile*, crossbowmen, Genoese red cross / lion of St Mark, no cannon; Marco's presence is inference, do not caption a figure as Marco. Existing `drawing-venetian-galley.png` is **anachronistic** (Salute domes 1631–87, Gothic Doge's Palace façade, Viking-like hull): redraw. Critique-only candidate: Peace and release, 1299 (anchor ch-01:39; San Giovanni Grisostomo courtyard, c. 1300 Venetian-Byzantine fronts).
- **Maps:** critique §5 proposes a ch-01 map (Venice, Genoa, Curzola; Adriatic inset; Doria's raid path). No A-ID in `multimedia-plan.md`.
- **Timelines / diagrams / tables:** D (I-1) Who captured Marco, and where? (preamble vs Jacopo d'Acqui vs Ramusio) + text witnesses F / Pipino / Z / Ramusio / Yule–Cordier. E: Prologue in the original — Rustichello's Franco-Italian opening ("Seignors emperaor et rois…") beside Yule's English, parallel-text box.
- **Characters appearing:** Marco Polo, Rustichello of Pisa, Lamba Doria, Andrea Dandolo, Jacopo d'Acqui, Prince Edward of England; Niccolò and Maffeo Polo (passing)
- **Character check (S-05):** Marco c. 44 (1298); Rustichello older, a **layman** (no habit, no chains). Cards: `plans/registry/character-cards.yaml`.

### Period sources (gap-source ledger, 2026-11-13)
- Genoese civic room and lay dress: draft cues **C43** (counting house, Cocharelli f. 8r, c. 1330–40) and **C45** (consuls in council, Annales Ianuenses p. 231, by the 1230s). Images are in media/references/README.md § Added 2026-11-13; Cocharelli is edit OK outside the UK, the Annales are look only.
- Curzola galleys: Cocharelli f. 5r has galleys and round ships (**C44**); for ships of c. 1270, Pryor's 1268 contracts are text (`pryor1984crusader`).
- Sea-chart prop for the dictation table: **C48** (Carte Pisane crop).
- Register: `registry/visual-references.md § Gap-source ledger`.

## Gated by spikes
- S-01 Voice standard (this chapter is the reference)
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format)
- S-04 Gazetteer authority (Genoa, Curzola rows; nit 1 gloss rule)
- S-05 Character registry (Marco, Rustichello in hero plate)
- S-08 LaTeX build pipeline (D table, parallel-text box, plates)
- S-10 ✓ Image generation pilot (GEN hero, Curzola secondary)
- S-13 ✓ (2026-11-11): `registry/scholarship.md`; items in this file's `.T1`/`.T4`

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-01.T1` Critical and factual fixes
- `I-01.T5` Media placement (figures, tables, captions) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `I-01.T6` Lint pass and human voice read

### I-01.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #26 (batch 7)
- **Now:** 1,982 words · 7% verbatim · "You must know" 0 · "Anyway" 2 · formula hinges 2 · archaisms 1 · Book first person 0 · asides 2
- **Do:**
  - Verbatim already within limit; voice and structure pass only.
  - Asides over 80 words: :21 (159), :37 (106). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :11, :27, :45; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Pagan → Mien ×1; unglossed first mentions: Tana, Trebizond. `python3 tools/lint.py -v vol-1/ch-01-genoa-prison.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: Rusticiano → Rustichello ×2, Rusticien → Rustichello ×1; unglossed first mentions: none. The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-01.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-01.T3` (the flags are written during the re-voice pass)
- **Now:** 0 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-01-genoa-prison.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-01.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-01.T3` (re-voice renumbers Notes)
- **Now:** 15 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-01-genoa-prison.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-12 (2026-11-10):** Note [8] (dictation language, Franco-Italian register) may cite the F text in its modern edition, `eusebi2018devisement` (open access), beside Benedetto.
  - **S-13 ✓ (`registry/scholarship.md` Q1 and § The 2024 anniversary):** Notes on composition: Franco-Italian is settled; F belongs with the thirty-odd French manuscripts copied in Genoa by Pisan prisoners; the Book was then rewritten in Venice in stages (`andreose2024textual`, read). The end of the captivity: a record published in 2026 may put Marco in Venice by October 1298 (`bolognari2026venezia`, read); give it as Bolognari's inference.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-01.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 6 errors · 3 warnings — failing: asides, budgets, quotes; warnings: recaps
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-01-genoa-prison.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.


**S-15 intake → I-01.T1/T4:** Follow `registry/facts.md` S15-F2–F3 and `research/results/S-15-raw.md` #11–15. Attribute Jacopo's 1296 Ayas account and Ramusio's Curzola story; identify Yule/Bolognari's 1294 interpretation as an argument, not a refutation of any possible later skirmish. The exact prison, shared cell, Rustichello's lay status and Meloria capture are unverified; frame composition as collaboration. Cite Bolognari 2024 and Yule for Notes.

**External S-15 check:** Cigni 2017 makes a strong contextual case that Rustichello was among the Meloria prisoners, without an individual capture document. Identify this as Cigni's inference; his article supports identifying the collaborator with the Arthurian compiler. See `research/results/S-15-external-intake.md`.


**S-15 source sweep:** Cigni 2017 discusses named Pisan prison-copyists, including Taddeus's 1288 colophon (`registry/enrichment.md` S15-H6). It is usable as a prison-writing milieu, not an individual document naming Rustichello as a Meloria captive.
