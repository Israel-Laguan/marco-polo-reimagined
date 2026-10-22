# II-07 — Tebet, Caindu, Carajan, Zardandan

**File:** `vol-2/ch-07-tebet-carajan.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,125 | 46% | [M] | 15/15; drift [9]/[10]; ★★★ in Note [7]; "Gazetteer:" tooling in [1], [9], [13] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 46% (critique C2 text prints 47%). Scorecard verdict: "Solid metrology; leaked instruction; outline-list recap". Scorecard: 9 hinges, "You must know" ×0. Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-07 (whole)

### Factual / fidelity
- — none found

### Dispute handling and Ramusio flags
- **[m]** The [M]-tag outline hook "How far Polo rode in person vs Yunnan service reports" never reaches the body; it appears only as a date in Note [9]. Fix: add one aside sentence (Mangala/Essentimur dating, about 1277–80). — vol-2 m4 · ch-07:33, Note [9] ch-07:75

### Voice and prose
- **[M]** Drafting instruction in the prose: "narrate as the Book does, and frame comparatively." Fix: :47 ends "…his share of suffering." and the couvade comparison goes to Note [14]. — vol-2 M3 · ch-07:47; content plan W1.3
- **[M]** Outline-beat list pasted as the closing paragraph ("…has done what Book II.xlv–l promised…"). Fix: replace with one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-07:53; content plan W1.3
- **[M]** Aside exits: the volume-wide "Anyway, next he mentions X" formula; cap one per chapter, vary exits (grep count of "Anyway" in this file: 0, so watch only that the re-voice does not add any). — vol-2 M4 · ch-07 (whole)

### Notes and apparatus
- **[m]** Citation drift: [9] sits on the Essentimur/Yachi paragraph and [10] on the Talifu paragraph, but Note [10] mostly describes Yachi's cowries, brine and lake (:35, which has no citation). Fix: move [10] to :35, add [11] for Talifu, renumber after. — vol-2 m3 · ch-07:33–37; content plan W5
- **[M]** Outline star legend in Notes: Note [7] uses ★★★. Fix: convert to ✓/~/✗/◇/?. — vol-2 M7 · ch-07:71
- **[M]** Notes leak tooling: "Gazetteer: *…*" labels in Notes [1], [9], [13]. — vol-2 M3 · ch-07:59, :75, :83

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Caindu, Brius, Carajan (never glossed as Yunnan in the body), Zardandan. Fix: e.g. "Carajan (Yunnan)". — vol-2 M11 · ch-07 (first mentions)
- **[M]** Gazetteer `book_name` "Tibet" differs from the chapter's "Tebet" (front-02 follows the gazetteer). — vol-2 M11
- **[M]** No gazetteer rows for Caindu, Brius (blocks map A11). — vol-2 M11
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-07.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 12 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Green bamboo exploding in the night camp, Tebet marches — GEN, Dali kingdom scroll, landscape 4:3; must get right: hobbled, hooded horses, Kham forest — see `illustration-plan.md`. Anchor ch-07:15.
- **Secondary plates:** GEN Salt-cake money (plan; anchor :27, merchant weighing gold against moulded salt loaves). Critique §4 candidate: the "serpent" trap (:39; "draw a crocodile, not a two-legged dragon").
- **Maps:** A11 South-west circuit (II-7 – II-9: Sindafu → Tebet → Carajan → Vochan → Mien; reported Bangala, Caugigu, Cuiju). Existing `map-caugigu.jpg` (Yule Itinerary No. V, unused) suggested for ch-07/09 by critique §5; multimedia plan keeps it as a small facsimile, superseded by A11.
- **Timelines / diagrams / tables:** C9 Gold : silver ratio gradient (Yachi 1:8, Talifu 1:6, Zardandan 1:5, Vochan descent 1:5; II-7 / II-8), making Vogel's metrology argument visual.
- **Characters appearing:** Kublai (the Kaan), Möngke (Mongu Kaan), Essentimur (Esen-Temür), Hügechi (Hukaji), Cogachin, Marco Polo

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★★★, Gazetteer labels, renumbering)
- S-04 Gazetteer authority and naming policy (glosses, Tebet, missing rows)
- S-05 Character registry (Essentimur/Mangala dating)
- S-06 Fact verification sheet (1277–80 dating for the new aside)
- S-08 LaTeX build pipeline (plates, map, chart)
- S-09 Map and diagram pipeline (A11, C9)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-07.T5` Media placement (hero, secondary, A11, C9)
- `II-07.T6` Lint pass and human voice read

### II-07.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #12 (batch 3)
- **Now:** 3,082 words · 46% verbatim · "You must know" 0 · "Anyway" 0 · formula hinges 5 · archaisms 8 · Book first person 0 · asides 0
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :13 (78%), :25 (71%), :47 (75%).
  - Cut the closing recap :53 (123 words) to ≤ 1 forward sentence.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Yunnan → Carajan ×2, Chengdu → Sindafu ×1, Tibet → Tebet ×1; unglossed first mentions: Camul, Caindu, Brius, Carajan, Zardandan, Mien. `python3 tools/lint.py -v vol-2/ch-07-tebet-carajan.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-07.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-07.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-07-tebet-carajan.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-07.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-07.T3` (re-voice renumbers Notes)
- **Now:** 15 Notes · 3 ★ · 0 without a lead marker · tag [M]
- **Do:**
  - Tag line `**[M]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - 3 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Run `python3 tools/lint.py -v vol-2/ch-07-tebet-carajan.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-07.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 18 errors · 1 warnings — failing: archaism, budgets, markers, ramusio, recaps, scaffolding, verbatim; warnings: openers
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-07-tebet-carajan.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
