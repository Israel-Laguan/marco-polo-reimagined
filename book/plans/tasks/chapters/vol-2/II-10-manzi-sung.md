# II-10 — Eastward to Manzi: Canal Cities and the Fall of the Sung

**File:** `vol-2/ch-10-manzi-sung.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,103 | 69% | [M] | 13/13; ★★★ in Note [6]; "Gazetteer:" tooling in [1] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 69%, with 5 of the volume's 38 first-person Book lines. The canal "city strings" are named among the catalogue passages to turn "into modern storyteller summary". Scorecard: 6 hinges, "You must know" ×7. Fix: convert first-person Book lines to reported speech or marked quotation. — vol-2 C2, §3 · ch-10 (whole)

### Factual / fidelity
- **[m]** Bayan's dispatch "in 1268" goes unflagged (Bayan took command in 1273–74). — vol-2 m7 · ch-10:53
- **[N]** Epigraph wording drift: "So when you pass" where Yule has "And when you pass". Fix: quote exactly or mark "(adapted)". — vol-2 N5 · ch-10:4

### Dispute handling and Ramusio flags
- **[m]** :61 crams a 70-word chronology (Duzong 1274, Gong, regent Xie, Lin'an 1276, Yaishan 1279) into the middle of a narrative paragraph. Fix: move it to an em-dash aside or to Note [12] and keep one clause in the body. — vol-2 m7 · ch-10:61

### Voice and prose
- **[M]** Drafting instruction in the prose: "flag it, then resume." Fix: delete, keep only the substance. — vol-2 M3 · ch-10:17; content plan W1.3
- **[M]** Outline-beat list pasted as the closing paragraph ("Thus Book II.lx–lxv has done what it promised…"). Fix: one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-10:73; content plan W1.3
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 2. — vol-2 M4 · ch-10 (whole)
- **[N]** "the cremation formula that will wearisome the reader" → "will weary". — vol-2 N2 · ch-10:17

### Notes and apparatus
- **[M]** Outline star legend in Notes: Note [6] uses ★★★. Fix: convert to ✓/~/✗/◇/?. — vol-2 M7 · ch-10:89
- **[M]** Note [1] leaks tooling ("Gazetteer: Changlu *likely_visited*"). — vol-2 M3 · ch-10:79

### Naming and gazetteer
- **[M]** Gazetteer `book_name` "Ciangu" differs from the chapter's "Changlu" (front-02 follows the gazetteer). — vol-2 M11
- **[M]** Conflicting identification: gazetteer says Cacanfu = "Puyang/Heze, Henan"; ch-10:13 says Hejian (Hebei). — vol-2 M11 · ch-10:13
- **[M]** No gazetteer rows for Chinangli, Tadinfu, Sinjumatu, Linju, Piju, Siju, Coiganju, Caramoran (blocks map A12). — vol-2 M11
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-10.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 5 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Song envoys surrender the seal to Bayan, 1276 — GEN, Southern Song academy (elegiac), portrait 3:4; must get right: Lin'an outskirts, Empress Dowager Xie's envoys; caption: Book compresses events; no "Hundred Eyes" — see `illustration-plan.md`. Anchor ch-10:61 (child emperor Gong was surrendered; loyalists carried other princes to sea).
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates (both "diagram-friendly"): Changlu salt-earth works (:15); Sinjumatu summit split (:33).
- **Maps:** A12 The canal spine (II-10 – II-13: Juju → Cacanfu → Changlu → Chinangli → Tadinfu → Sinjumatu → Linju → Piju → Siju → Caramoran/Coiganju → …; Nanghin and Saianfu dashed).
- **Timelines / diagrams / tables:** B4 The Song endgame, 1268–1279 (II-10 / II-11). Critique §5 also proposes diagrams "Canal summit split at Sinjumatu" and "salt-earth leaching" for ch-10; neither has a C-ID in `multimedia-plan.md`.
- **Characters appearing:** Bayan Chincsan ("Hundred-Eyes"), Faghfur / Facfur (Song emperor Duzong, "Tu Tsong"), the Queen (Empress Dowager Xie, "Siechi"), the child emperor Gong ("Chaohien"), Kublai (the Kaan), Litan (Li Tan), Aguil and Mongotay, Hulagu (mentioned), Marco Polo, Rustichello; traveller discussed: Odoric

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★★★, Gazetteer label)
- S-04 Gazetteer authority and naming policy (Changlu, Cacanfu, missing rows)
- S-05 Character registry (Bayan, Xie, Gong in hero; Song ruler names)
- S-06 Fact verification sheet (Bayan 1268 vs 1273–74; epigraph wording)
- S-08 LaTeX build pipeline (plate, map, timeline)
- S-09 Map and diagram pipeline (A12, B4; unassigned canal/salt diagrams)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-10.T1` Factual fixes (Bayan date, epigraph)
- `II-10.T5` Media placement (hero, A12, B4)
- `II-10.T6` Lint pass and human voice read

### II-10.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #5 (batch 2)
- **Now:** 3,068 words · 69% verbatim · "You must know" 7 · "Anyway" 2 · formula hinges 5 · archaisms 6 · Book first person 1 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (90%), :27 (94%), :43 (86%), :57 (93%), :65 (92%), :71 (95%).
  - Cut the closing recap :73 (122 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :29, :47, :73; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Jinan → Chinangli ×2, Hejian → Cacanfu ×1, Yen-chau → Tadinfu ×1, Hwai-ngan → Coiganju ×1, Yangzhou → Yanju ×1, Xiangyang → Saianfu ×1, Hangzhou → Kinsay ×1; unglossed first mentions: Caramoran, Cacanfu, Chinangli, Tadinfu, Linju, Coiganju, Caiju. `python3 tools/lint.py -v vol-2/ch-10-manzi-sung.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-10.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-10.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-10-manzi-sung.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-10.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-10.T3` (re-voice renumbers Notes)
- **Now:** 13 Notes · 3 ★ · 0 without a lead marker · tag [M]
- **Do:**
  - Tag line `**[M]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - 3 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Run `python3 tools/lint.py -v vol-2/ch-10-manzi-sung.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-10.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 25 errors · 7 warnings — failing: archaism, asides, budgets, first_person, markers, quote_verify, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: names, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-10-manzi-sung.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
