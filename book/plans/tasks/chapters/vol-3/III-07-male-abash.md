# III-07 — Male and Female, Scotra, Madeigascar, Zanghibar, Abash

**File:** `vol-3/ch-07-male-abash.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,742 | 46% | — (missing; outline gives [R]) | ok (21/21) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription: 46% of narrative in 7-gram Yule runs (critique 8-gram 42%; threshold ≤ 25%). Fix: paraphrase at least half of each long run. — vol-3 C3 · ch-07

### Factual / fidelity
— see the Ramusio item below

### Dispute handling and Ramusio flags
- The Scotra whale hunt is Ramusian, narrated in the body and flagged only in Note [4]. Fix (W3): inline tag ("Ramusio's text adds…") plus "◇ Ramusio-only". — vol-3 M7 · ch-07:15, :63
- The Ruc: "'Tis said…" frames it, but there is no aside on the legend or the Aepyornis background. Fix: one-line dash aside. — vol-3 m6 · ch-07:27

### Voice and prose
- Formula opener "Marco Polo starts by narrating that…", copied straight from the voice-guide example (same in III-08, III-09). Fix: vary the opener (start on place or action). — vol-3 m14 · ch-07:9
- "Anyway" ×3 (:13, :25, :37) → at most one; "A quick note" (:13). Scorecard: 10 hinges. — vol-3 m14 · ch-07:13, :25, :37
- Recap closer "Thus the western wonder-run from Male and Female stands in this chapter…" with "it is enough that" and "one … breath". Fix: one bridging sentence or delete. — vol-3 M10 · ch-07:51

### Notes and apparatus
- Tag line missing; the outline gives [R]. Fix: add **[R]**. (Also W5: restore tag lines on III-7 to III-9.) — vol-3 M8 · ch-07:5-7
- ★ ×1 in Notes; convert to ✓ ~ ✗ ◇ ?. — vol-3 M9 · ch-07 Notes
- New trailing "**Comparative:**" block format (ch-07 to ch-10), unlike ch-01 to ch-06, which fold comparatives into numbered Notes. — vol-3 §3 rushed signals · ch-07:99

### Naming and gazetteer
- Redundant gloss "Champa (Champa / the Vietnam coast)"; also use the book form *Chamba*. — vol-3 n1 · ch-07:37
- Gazetteer `Abyssinia` vs the book's `Abash`. — vol-3 m4 · ch-07
- (Context only: :13 and Note [2] rightly refuse Male = Maldives; the fix sits in III-F2 and the gazetteer.)

### Length and structure
— none found (2,742 words; scorecard: "Good disputes")

## Media hooks
- **Hero plate:** III-7 *The rukh carrying off an elephant* — **PD**, al-Qazwini, *'Aja'ib al-makhluqat*, portrait; caption: legend; Aepyornis — see `illustration-plan.md`. (Critique §4's ★ pick was a "Ruc feather" at Kublai's court — Ramusian and legendary; caption as a court curiosity.)
- **Secondary plates:** none in plan. Critique §4 options not adopted: Scotra whale hunt (Ramusian detail), the giraffe (not Madagascar)
- **Maps:** none placed here
- **Timelines / diagrams / tables:** critique §5 item 6 proposes a "Madeigascar vs Magadoxo" table (camels, elephants, sheikhs, giraffes, current) — not in the multimedia plan's D list; critique §5 item 2 links the monsoon diagram (C11) to ch-07:25 (Madagascar current: 20 days out, more than 3 months back)
- **Characters appearing:** the Soldan of Aden, the bishop of Abash (unnamed), St Thomas; comparative sources: Niccolò de' Conti, Fra Mauro, Ibn Battuta, Duarte Barbosa

## Gated by spikes
- S-01, S-02, S-03 (tag line, Ramusio flag, ★, Comparative block), S-04 (Abash, Chamba), S-06 (Ramusian whale hunt), S-08, S-09 (only if the C11 / Madeigascar table hooks are adopted), S-11 (PD hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-07.T1` Critical and factual fixes
- `III-07.T2` Ramusio flags and dispute asides
- `III-07.T4` Notes and apparatus normalisation (tag line)
- `III-07.T5` Media placement (figures, captions)
- `III-07.T6` Lint pass and human voice read

### III-07.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #33 (batch 9)
- **Now:** 2,692 words · 46% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 9 · archaisms 4 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :17 (81%), :19 (76%), :43 (83%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, :29, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :13 (94), :25 (127). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :21, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-07.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 17 errors · 2 warnings — failing: archaism, asides, budgets, markers, quote_verify, ramusio, scaffolding, verbatim, you_must_know; warnings: ramusio, recaps
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-07-male-abash.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
