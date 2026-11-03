# III-08 — Aden, Esher, Dufar, Calatu, Hormos Again

**File:** `vol-3/ch-08-aden-hormos.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,080 | 64% | — (missing; outline gives [R/M]) | ok (21/21) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription: 64% of narrative in 7-gram Yule runs (threshold ≤ 25%). Fix: paraphrase at least half of each long run, **especially ch-08:21–47** (named priority). — vol-3 C3 · ch-08:21-47
- "Soft" label tic ×1: "Soft rise now:" (:27); also Note :97 "Soft hinge out of the Indian Ocean". Fix: strip. — vol-3 C2 · ch-08:27, :97

### Factual / fidelity
- "the book explains … of the stitched ships and the dates-and-fish diet, of the simoom and the turn inland": Yule's text (`yule-vol2.txt:24817`) has none of this list; it is the narrator's gloss inside the Book's speech. — vol-3 n7 · ch-08:45

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- Formula opener "Marco Polo starts by narrating that…" (copied from the voice-guide example). Fix: vary it. — vol-3 m14 · ch-08:9
- "Anyway" ×3 (:13, :19, :33) → at most one; "A quick note on the stages" (:13). Scorecard: 10 hinges. — vol-3 m14 · ch-08:13, :19, :33
- Recap closer "Thus the Indian Ocean book closes upon itself…" with "it is enough that" and "one … breath". Fix: one bridging sentence or delete. — vol-3 M10 · ch-08:51

### Notes and apparatus
- Tag line missing; the outline gives [R/M]. Fix: add **[R/M]**. — vol-3 M8 · ch-08:5-7
- ★ ×7 in Notes (e.g. "Distances inconsistent ★", :97); convert to ✓ ~ ✗ ◇ ?. — vol-3 M9 · ch-08 Notes
- Trailing "**Comparative:**" block format (new in ch-07 to ch-10). — vol-3 §3 rushed signals · ch-08:99

### Naming and gazetteer
- Redundant glosses: "Aden (ʿAdan / Aden)" (:9); "Acre (Acre / ʿAkkā)" (:17). — vol-3 n1 · ch-08:9, :17
- Gazetteer and III-F2 `Kalhat` vs chapter and Yule `Calatu`. — vol-3 m4 · ch-08
- Gazetteer lacks a row for Kis (Qais). — vol-3 m4 · ch-08
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-08.T3`.

### Length and structure
— none found (2,080 words; scorecard: "Accurate")

## Media hooks
- **Hero plate:** III-8 *The wind-catchers of Hormos at noon* — GEN, Baghdad school (al-Wasiti), landscape; old mainland Hormuz; *bād-gīr* towers as a type (surviving towers are later) — see `illustration-plan.md`
- **Secondary plates:** none in plan. Critique §4 options not adopted: cattle fed on dried fish (Hadramawt coast); tapping frankincense at Dufar (*Boswellia*, not fir)
- **Maps:** none placed here
- **Timelines / diagrams / tables:** none. Glossary: *bād-gīr*
- **Characters appearing:** the Soldan of Aden (Rasulid sultan of Yemen), the Soldan of Babylon (Mamluk sultan of Egypt), the Melic of Hormos; Cocachin (mentioned); comparative sources: Ibn Battuta, Duarte Barbosa

## Gated by spikes
- S-01, S-02, S-03 (tag line, ★, Comparative block), S-04 (Calatu, Kis, glosses), S-06 (n7), S-08, S-10

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-08.T1` Critical and factual fixes
- `III-08.T5` Media placement (figures, captions)
- `III-08.T6` Lint pass and human voice read

### III-08.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #29 (batch 8)
- **Now:** 2,055 words · 64% verbatim · "You must know" 0 · "Anyway" 3 · formula hinges 8 · archaisms 4 · Book first person 1 · asides 6
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :11 (95%), :23 (88%), :25 (84%), :37 (92%), :39 (92%), :41 (90%).
  - Asides over 80 words: :13 (86), :27 (89). Trim; move traveller/scholar lists to Notes.
  - Reduce asides from 6 to ≤ 4 (fold corrections into one-clause fixes in the narrative).
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Dhafār → Dufar ×3, Kis → Kisi ×2, Baghdad → Baudas ×1, Hormuz → Hormos ×1; unglossed first mentions: Dufar, Calatu. `python3 tools/lint.py -v vol-3/ch-08-aden-hormos.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: none; unglossed first mentions: Bundukdar (Baibars). The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-08.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-08.T3` (the flags are written during the re-voice pass)
- **Now:** 0 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-08-aden-hormos.md` shows no `ramusio` errors, and the flag count matches the passages found.

### III-08.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-08.T3` (re-voice renumbers Notes)
- **Now:** 21 Notes · 7 ★ · 1 without a lead marker · tag none
- **Do:**
  - Add the missing tag line `**[M]**` under the epigraph (assigned in S-03; confirm against the chapter).
  - 7 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: [10] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-3/ch-08-aden-hormos.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-08.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 21 errors · 0 warnings — failing: archaism, asides, budgets, first_person, markers, quote_verify, scaffolding, tags, verbatim
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-08-aden-hormos.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
