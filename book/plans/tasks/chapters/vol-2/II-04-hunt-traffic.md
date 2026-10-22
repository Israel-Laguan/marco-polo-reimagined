# II-04 — Hunt, Hounds, Litter, and the Traffic of a Million

**File:** `vol-2/ch-04-hunt-traffic.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,113 | 72% | [V] | 21/21; Notes [7], [21] empty stubs; [20] unqualified | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 72%. Scorecard verdict: "Good linguistic asides; leaked instruction :17; Ramusio unflagged". Keep Yule only as short marked quotations, one or two per scene; "Sire! Look out for Cranes!" is the critique's own example of a quotation worth keeping. Scorecard: 7 hinges, "You must know" ×3. — vol-2 C2, §3 · ch-04 (whole), :33

### Factual / fidelity
- **[m]** Note [20] presents *Milione*'s "double life (wealth vs 'million lies')" without qualification. Vol. III ch-10 says "'million lies' insult — popular later reading; not the archival sense" and gives the house-name theory. Fix: align with III-10. — vol-2 m11 · ch-04:99

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged: :15 approach the game against the wind; :23 the Two Brothers' thousand-head tenure (only Note [6] says "Ramusio"); :47 nation-sorted hostelries; :51 night patrols and beatings. Fix: two-to-four-word inline tag per paragraph plus "◇ Ramusio-only" in the matching Note; model ch-13:53. — vol-2 M1 · ch-04:15, :23, :47, :51; content plan W3

### Voice and prose
- **[M]** Drafting instruction left in the prose: "Narrate 'lion' as the Book says; gloss tiger without flattening the medieval lexicon." Fix: delete the instruction, keep only the substance. — vol-2 M3 · ch-04:17; content plan W1.3
- **[M]** Recap padding: opens with "The Book has shown…" (:11) and closes with "Here the chapter stops short of… For the present it has shown…" (:55). Fix: cut closing recap to at most one sentence or remove; drop the opening recap. — vol-2 M4 · ch-04:11, :55
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-04 (whole)

### Notes and apparatus
- **[M]** Notes [7] and [21] leak tooling ("Soft transition to the imperial tour"; "Soft landing to II-5"). — vol-2 M3 · ch-04:73, :101
- **[m]** Notes [7] and [21] add nothing (cross-reference / transition stubs). Fix: merge into neighbouring Notes and drop the citations. — vol-2 m9 · ch-04:73, :101; content plan W5

### Naming and gazetteer
- **[M]** Cachar Modun (hunting camp) has no gazetteer row; this blocks map A8. — vol-2 M11 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-04.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 3 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Kublai hunting — **PD**, Liu Guandao, *Khubilai Khan Hunting* (1280), handscroll — see `illustration-plan.md`.
- **Secondary plates:** GEN "Sire! Look out for Cranes!" from the elephant litter (plan's Vol. II secondaries; critique §4 ★ scene, anchor :33: roof of the timber chamber thrown open, gerfalcon cast, Toscaol watchers in pairs; spring marshes south-east of Dadu). Critique §4 further candidates: red and blue hound corps (:21; caution: 10,000 men per brother inflated); tiger hunt (:15; "label it a tiger").
- **Maps:** A8 Seasonal orbit (Dadu ↔ Shangdu ↔ Cachar Modun, month labels, 28 August libation; II-4 / I-13).
- **Timelines / diagrams / tables:** — none assigned. Existing `drawing-chandu-palace.png` is suggested for ch-04 by critique §5 ("if not already used in Vol. I ch-13"), but the multimedia plan retires all `drawing-*.png` (wrong style, too small; period errors include "a Renaissance villa at Shangdu").
- **Characters appearing:** Kublai (the Great Kaan), Baian and Mingan (the two brother Masters of the hounds), Marco Polo, Achmath / Ahmad (mentioned)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (stub Notes, Ramusio flag style)
- S-04 Gazetteer authority (Cachar Modun; A8)
- S-05 Character registry (Kublai in PD hero and GEN secondary)
- S-06 Fact verification sheet (*Milione* name reading, aligned with III-10)
- S-08 LaTeX build pipeline (plates, map)
- S-09 Map and diagram pipeline (A8)
- S-10 Image generation pilot (GEN secondary)
- S-11 Public-domain artwork sourcing and licensing (Liu Guandao)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-04.T1` Factual fix (*Milione* Note [20])
- `II-04.T5` Media placement (PD hero, cranes secondary, A8)
- `II-04.T6` Lint pass and human voice read

### II-04.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #3 (batch 1)
- **Now:** 3,141 words · 71% verbatim · "You must know" 2 · "Anyway" 3 · formula hinges 4 · archaisms 15 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :21 (90%), :27 (96%), :33 (97%), :35 (96%), :47 (90%), :49 (99%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, :23, :33, :47, plus any listed under *Dispute handling* above.
  - Drop the opening recap (:11).
  - Cut the closing recap :55 (92 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :15; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Peking → Cambaluc ×1; unglossed first mentions: none. `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-04.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-04.T3` (the flags are written during the re-voice pass)
- **Now:** 5 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-04.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-04.T3` (re-voice renumbers Notes)
- **Now:** 21 Notes · 0 ★ · 4 without a lead marker · tag [V]
- **Do:**
  - Tag line `**[V]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - Notes with no lead marker: [7], [10], [14], [21] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-04.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 40 errors · 4 warnings — failing: archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: openers, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
