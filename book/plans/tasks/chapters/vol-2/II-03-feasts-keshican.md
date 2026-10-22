# II-03 — Feasts, Robes, and the Twelve Thousand Keshican

**File:** `vol-2/ch-03-feasts-keshican.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,082 | 80% | [V] | 15/15; ★★★ in Note [15] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 80%. Scorecard verdict: "Strong asides (13 robes, keshig 400); body is Yule catalogue". The feasts are named among the catalogue passages to turn "into modern storyteller summary". Keep Yule only as short marked quotations, one or two per scene. Scorecard: 5 hinges, "You must know" ×7 (epigraph itself opens "You must know… hath"). — vol-2 C2, §3 · ch-03 (whole)

### Factual / fidelity
- — none found

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged: :17 soldiers eat on the carpets; :19 gilt buffet details; :21 barons who seat foreigners, and the giant door-wardens. Fix: two-to-four-word inline tag per paragraph ("— Ramusio's version adds —") plus "◇ Ramusio-only" in the matching Note; model ch-13:53. — vol-2 M1 · ch-03:17, :19, :21; content plan W3

### Voice and prose
- **[M]** Recap padding: opens with "The Book has shown…" (:11) and closes with "Here the chapter stops short of… For the present it has shown…" (:43). Fix: cut closing recap to at most one sentence or remove; drop the opening recap. — vol-2 M4 · ch-03:11, :43
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 2. — vol-2 M4 · ch-03 (whole)

### Notes and apparatus
- **[M]** Outline star legend in Notes: Note [15] uses ★★★, against the voice guide's ✓ ~ ✗ ◇ ? set. Fix: convert to ✓/~/✗/◇/?. — vol-2 M7 · ch-03:77; content plan W5

### Naming and gazetteer
- — none found

### Length and structure
- W4 re-voice order: Vol. II batch position 1 of 14 (first after the II-2 pilot). — content plan W4

## Media hooks
- **Hero plate:** The White Feast procession — GEN, Yuan court painting, handscroll 3:1; must get right: everyone in white, tribute in nines, a *handful* of elephants and camels; caption: "5,000 elephants" inflated — see `illustration-plan.md`. Anchor ch-03:35 (Mongol *Chaghan sar*; Daming Hall terrace).
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: "Threshold guards" (:21; giants with staves coaching a foreign envoy; *Chuogeng lu*-type guardsmen); "Muffled cupbearers" (:23; Liu Guandao court style for costume).
- **Maps:** — none assigned
- **Timelines / diagrams / tables:** C3 Keshig rota (Polo's 4 × 3,000 × 3-day cycle vs Palladius's 400-man watch, reduced to 100 in 1330).
- **Characters appearing:** Kublai (the Great Kaan), Marco Polo, Möngke and Güyük (earlier khans, mentioned); travellers discussed: Rubruck, Carpini, Odoric

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★ → markers; Ramusio flag style)
- S-05 Character registry (Kublai in feast plate)
- S-08 LaTeX build pipeline (plate, C3)
- S-09 Map and diagram pipeline (C3)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-03.T2` Ramusio flags (three passages)
- `II-03.T4` Notes and apparatus normalisation (★★★)
- `II-03.T5` Media placement (hero, C3)
- `II-03.T6` Lint pass and human voice read

### II-03.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #1 (batch 1)
- **Now:** 3,101 words · 80% verbatim · "You must know" 6 · "Anyway" 2 · formula hinges 4 · archaisms 10 · Book first person 0 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :19 (100%), :23 (99%), :29 (99%), :33 (94%), :37 (98%), :39 (81%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :17, :19, :21, :33, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :15 (82). Trim; move traveller/scholar lists to Notes.
  - Drop the opening recap (:11).
  - Cut the closing recap :43 (113 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :25; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-03.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 35 errors · 3 warnings — failing: archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-03-feasts-keshican.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
