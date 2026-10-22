# III-02 — Chamba, Java, Locac, Pentam: The Southern Ocean Road

**File:** `vol-3/ch-02-chamba-java.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,814 | 46% | [R/M] | issues: Note [13] placeholder; Notes [4]–[6] overlap | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Misquoted epigraph: "When you leave the port of Zayton…" — Yule has "You must know that on leaving the port of Zayton…". Fix: restore the exact wording. — vol-3 C1 · ch-02:4
- Transcription: 46% of narrative in 7-gram Yule runs (threshold ≤ 25%). Fix: paraphrase at least half of each long run. — vol-3 C3 · ch-02
- "Soft" label tic ×2: "Soft digression now:" (:23), "Soft close here:" (:39); also Note [13] "Soft close toward Java the Less" (:69). Fix: strip the labels. — vol-3 C2 · ch-02:23, :39, :69

### Factual / fidelity
- "Yule leans toward… or the return voyage still ahead": Yule inclines to the Geographic Latin 1288 and the c. 1290 Indian mission (`yule-vol2.txt:14790`) and does not propose the return voyage. — vol-3 n8 · ch-02:21

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- "Anyway" ×3 (:17, :27, :33) → at most one; "A quick note" (:17). Scorecard: 9 hinges. — vol-3 m14 · ch-02:17, :27, :33
- Soft-close variant of the recap closer ("Soft close here: …", with "it is enough that"). Fix: one bridging sentence or delete. — vol-3 M10 · ch-02:39
- Pre-summary and mid-chapter restatement ("Thus Chamba stands…", "Thus the southern Ocean road narrows…"). Fix: cut where an aside already exists. — vol-3 M10 · ch-02:21-23 (also :37)

### Notes and apparatus
- Note [13] is a placeholder that says nothing. Fix: give it content or drop the citation from the body. — vol-3 m9 · ch-02:69
- Notes [4]–[6] overlap (Champa war records / Marco's presence / "★ Dispute: personal presence"). — vol-3 §3 scorecard · ch-02:51-55
- ★ ×3 (incl. Note [6] "★ Dispute"); convert to ✓ ~ ✗ ◇ ? and merge "★ Dispute" into its neighbour. — vol-3 M9 · ch-02:55

### Naming and gazetteer
- Gazetteer lacks a row for Sondur/Condur, which the chapter relies on. — vol-3 m4 · ch-02
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-02.T3`.

### Length and structure
— none found (1,814 words; "Solid and lean")

## Media hooks
- **Hero plate:** III-2 *Junks lift their rudders in the shoal strait* — GEN, Javanese temple relief, landscape; must get right: raisable axial rudders, mangrove coast, Malay perahu — see `illustration-plan.md` (critique §4 anchor: "great ships in passing this channel have to lift their rudders", Bintan coast)
- **Secondary plates:** none in plan. Critique §4 alternative not adopted: Elephant tribute from Chamba (Cham dress, brick *kalan* towers; caution: the pity-tale softens a brutal 1282–85 war)
- **Maps:** none placed here (A16 passes Chamba as "possible")
- **Timelines / diagrams / tables:** none
- **Characters appearing:** Marco Polo, Kublai (Great Kaan), Sagatu (Sogetu), Accambale (king of Chamba), Tughan (Toghan), Rustichello; comparative sources: Odoric, Niccolò de' Conti, Ibn Battuta, Duarte Barbosa

## Gated by spikes
- S-01, S-02, S-03, S-04 (Sondur/Condur row), S-06 (n8), S-08, S-10

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-02.T1` Critical and factual fixes
- `III-02.T5` Media placement (figures, captions)
- `III-02.T6` Lint pass and human voice read

### III-02.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #32 (batch 8)
- **Now:** 1,792 words · 46% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 4 · archaisms 0 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (75%), :19 (76%), :25 (93%), :29 (97%), :31 (96%), :35 (83%).
  - Asides over 80 words: :27 (112), :33 (98). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :21, :37; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Bintan → Pentam ×2, Champa → Chamba ×1, Sumatra → Java the Less ×1; unglossed first mentions: Condur, Locac, Pentam, Malaiur. `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-02.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-02.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` shows no `ramusio` errors, and the flag count matches the passages found.

### III-02.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-02.T3` (re-voice renumbers Notes)
- **Now:** 13 Notes · 3 ★ · 4 without a lead marker · tag [R/M]
- **Do:**
  - Replace tag `[R/M]` with `**[M]**` (compound tags are retired; if the lean matters, say it in one clause of Note [1]).
  - 3 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: [4], [6], [11], [13] (fill, merge or rewrite; none may be a placeholder or pointer).
  - "Dispute" label in Note(s) [6], [11]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-02.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 27 errors · 4 warnings — failing: asides, budgets, length, markers, quote_verify, ramusio, scaffolding, tags, verbatim, you_must_know; warnings: ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
