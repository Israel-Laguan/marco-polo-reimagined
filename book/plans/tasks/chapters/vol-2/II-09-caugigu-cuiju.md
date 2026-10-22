# II-09 — Caugigu, Anin, Coloman, Cuiju — and Back

**File:** `vol-2/ch-09-caugigu-cuiju.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,050 | 55% | [R] | 9/9; "★ / ★★" in Note [1]; "Gazetteer:" tooling in [1] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 55%. Scorecard: 6 hinges, "You must know" ×3. Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-09 (whole)

### Factual / fidelity
- **[N]** Epigraph wording drift: "seventy days" where Yule has "70 days" (and "which have been already particularly spoken of in our Book"). Fix: quote exactly or mark "(adapted)". — vol-2 N5 · ch-09:4

### Dispute handling and Ramusio flags
- — none found

### Voice and prose
- **[M]** Outline text pasted as the closing paragraph: "What Book II.lvi–lix promised after Bangala is done: mainland Southeast ethnography of the Laos–Guizhou orbit; natural fortresses; cloths; tigers; dogs; silk…", the outline beat list almost verbatim. Fix: one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-09:49; content plan W1.3
- **[M]** Mid-chapter "So/Thus [place]…" restatements re-list the previous paragraph. Fix: merge their identification content into the Notes. — vol-2 M4 · ch-09:15, :21, :29
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 1. — vol-2 M4 · ch-09 (whole)
- **[N]** Missing subject: "All these provinces that have been speaking of". Fix: "that the Book has been speaking of". — vol-2 N1 · ch-09:27

### Notes and apparatus
- **[M]** Outline star legend in Notes: Note [1] "★ / ★★". Fix: convert to ✓/~/✗/◇/?. — vol-2 M7 · ch-09:55
- **[M]** Note [1] leaks tooling ("Gazetteer: Caugigu, Anin, Coloman, Cuiju all *uncertain*"). — vol-2 M3 · ch-09:55

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Caugigu, Anin, Coloman, Cuiju, Fungul, Cacanfu. — vol-2 M11 · ch-09 (first mentions)
- **[M]** Conflicting identification: gazetteer and front-02 say Caugigu = Tonkin; ch-09:15 and `map-caugigu.jpg` put it at Kiang Hung, on the Lao side. Resolve to one authority. — vol-2 M11 · ch-09:15; content plan W5

### Length and structure
- **[m]** Momentum: three 100–130-word interpretive paragraphs (:15, :21, :29) in a 2,050-word chapter retell the ethnography a second time; recaps total about 435 words. Fix: fold the IDs (Kiang Hung, Ho-nhi, Kolo-man) into Notes [3]–[6]. "The chapter can stay short." — vol-2 m14, §3 · ch-09:15, :21, :29
- W4 re-voice order: Vol. II batch position 10 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Two great dogs hold a tiger at bay on the Cuiju road — GEN, Dali kingdom scroll, landscape 4:3; must get right: a **tiger** (the Book says "lion") — see `illustration-plan.md`. Anchor ch-09:37.
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: Coloman cave burials (:25; cliff-hung burials of south-west China; ethnic identification uncertain); Caugigu tattooing (:13; Tai/Shan tattoo traditions).
- **Maps:** A11 South-west circuit (reported: Bangala, Caugigu, Anin, Coloman, Cuiju/Fungul → Sindafu). Existing `map-caugigu.jpg` (Yule Itinerary No. V) suggested for ch-07/09 (critique §5); kept as small facsimile, superseded by A11.
- **Timelines / diagrams / tables:** — none assigned
- **Characters appearing:** Marco Polo, Rustichello (as scribe)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★, Gazetteer label)
- S-04 Gazetteer authority and naming policy (glosses, Caugigu conflict)
- S-06 Fact verification sheet (epigraph wording)
- S-08 LaTeX build pipeline (plate, map)
- S-09 Map and diagram pipeline (A11)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-09.T1` Epigraph fix (N5)
- `II-09.T4` Notes and apparatus normalisation (IDs folded into Notes [3]–[6])
- `II-09.T5` Media placement (hero, A11 / facsimile)
- `II-09.T6` Lint pass and human voice read

### II-09.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #10 (batch 3)
- **Now:** 2,039 words · 55% verbatim · "You must know" 2 · "Anyway" 1 · formula hinges 5 · archaisms 4 · Book first person 0 · asides 1
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :13 (95%), :17 (98%), :23 (94%), :27 (88%), :35 (100%), :37 (100%).
  - Asides over 80 words: :41 (138). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :15, :21, :49; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-09.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 13 errors · 4 warnings — failing: archaism, asides, budgets, markers, quote_verify, scaffolding, verbatim, you_must_know; warnings: names, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-09-caugigu-cuiju.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
