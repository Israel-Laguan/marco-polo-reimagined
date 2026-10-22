# II-08 — Mien and Bangala: Elephants, Battle, Towers of Gold and Silver

**File:** `vol-2/ch-08-mien-bangala.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,909 | 77% | [R/M] (undefined) | ok (11/11); "Gazetteer:" tooling in [1] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 77%; "Battle is near-verbatim Yule". Example :29 "Then might you see swashing blows dealt and taken from sword and mace… God might have thundered". The battle is named among the catalogue passages to turn "into modern storyteller summary". Scorecard: 9 hinges, "You must know" ×4. — vol-2 C2, §3 · ch-08:29

### Factual / fidelity
- **[m]** Unflagged marvel: "great woods abounding in elephants and unicorns" has no gloss. Fix: add "(rhinoceroses, as Polo himself later realises in Java)" or move it to a Note. — vol-2 m5 · ch-08:37

### Dispute handling and Ramusio flags
- — none found (scorecard: "good Yuan/Burmese synchronism")

### Voice and prose
- **[m]** Clunky: "The ponies of the Mongol host, pitched and tied among the trees when the elephant-towers unhorsed the charge, become in the telling the hinge…" is hard to parse, and the camel digression answers an outline error, not the text. Fix: "The hinge of the day is the Tartars' choice to dismount and fight as archers; the elephants broke under the arrows, not under any trick of camels." — vol-2 m6 · ch-08:33
- **[M]** Outline-beat list pasted as the closing paragraph ("what Book II.li–lv promised after Zardandan:"). Fix: one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-08:51; content plan W1.3
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 1. — vol-2 M4 · ch-08 (whole)

### Notes and apparatus
- **[M]** Note [1] leaks tooling ("Gazetteer: Mien *reported_only*"). — vol-2 M3 · ch-08:57
- **[m]** Tag [R/M] undefined (README and outline define only [V], [R], [M]). Fix: use [M] with a one-line gloss, or define compounds in front-01. — vol-2 m10 · ch-08:7

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Vochan, Mien (never glossed as Burma), Bangala. Fix: e.g. "Mien (Burma)". — vol-2 M11 · ch-08 (first mentions)
- **[M]** No gazetteer row for Vochan (also named in ch-07); blocks map A11. — vol-2 M11

### Length and structure
- W4 re-voice order: Vol. II batch position 2 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Battle of Vochan: dismounted archers vs war elephants — GEN, **Pagan temple murals**, landscape 4:3; must get right: howdah castles breaking into the trees, dozens of elephants not 2,000; caption: numbers inflated — see `illustration-plan.md`. Anchor ch-08:25 (1277 Yongchang plain).
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: Pagan towers (:41; gilded brick stupas with *hti* bell-canopies; plating "a finger thick" is rhetoric); gold-for-silver market on the long descent (:35).
- **Maps:** A11 South-west circuit (II-7 – II-9).
- **Timelines / diagrams / tables:** C9 Gold : silver ratio gradient (II-7 / II-8; Vochan descent 1:5); D table II-8 Mien battle numbers (2,000 vs about 800 elephants, 12,000 vs about 700 men, 1272 vs 1277).
- **Characters appearing:** Kublai (the Kaan), Nescradin (Nasruddin), Sentemur (Esen-Temür), the King of Mien (Narathihapade in the file; Narathihapate), Prince Singtur, Marco Polo

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (compound tag, Gazetteer label)
- S-04 Gazetteer authority and naming policy (glosses, Vochan row)
- S-06 Fact verification sheet (unicorn gloss)
- S-08 LaTeX build pipeline (plate, map, chart, D table)
- S-09 Map and diagram pipeline (A11, C9)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-08.T1` Factual fix (unicorn gloss)
- `II-08.T5` Media placement (hero, A11, C9, Mien table)
- `II-08.T6` Lint pass and human voice read

### II-08.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #2 (batch 1)
- **Now:** 2,887 words · 77% verbatim · "You must know" 3 · "Anyway" 1 · formula hinges 5 · archaisms 9 · Book first person 0 · asides 1
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :21 (99%), :29 (100%), :31 (97%), :35 (87%), :41 (87%), :43 (93%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :41, plus any listed under *Dispute handling* above.
  - Cut the closing recap :51 (124 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :17, :29, :33; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-08.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-08.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-08-mien-bangala.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-08.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-08.T3` (re-voice renumbers Notes)
- **Now:** 11 Notes · 0 ★ · 0 without a lead marker · tag [R/M]
- **Do:**
  - Replace tag `[R/M]` with `**[M]**` (compound tags are retired; if the lean matters, say it in one clause of Note [1]).
  - Run `python3 tools/lint.py -v vol-2/ch-08-mien-bangala.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-08.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 20 errors · 5 warnings — failing: archaism, asides, budgets, ramusio, recaps, scaffolding, tags, verbatim, you_must_know; warnings: ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-08-mien-bangala.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
