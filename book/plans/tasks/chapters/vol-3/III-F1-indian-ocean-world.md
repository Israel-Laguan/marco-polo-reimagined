# III-F1 — The Indian Ocean World (and Why a Princess Boards a Ship)

**File:** `vol-3/front-01-indian-ocean-world.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 838 | n/a | — | ok (8/8) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Misquoted epigraph: "And when the ships had been made ready…" — Yule has "had been equipt". Fix: restore the exact wording (W1.1 lists front-01 among the 13 epigraph files). — vol-3 C1 · front-01:4

### Factual / fidelity
- "Bent the Atlantic" overstates Columbus's debt to Polo and contradicts ch-11's own caution. Fix: tone it down, in step with the III-11 Columbus fixes (Leeu Latin copy, Toscanelli 1474, annotation dating debated). — vol-3 M4 · front-01:27

### Dispute handling and Ramusio flags
— none found

### Voice and prose
— none found (scorecard: "Good primer"; one "Anyway" at :35 is within the ≤ 1 limit)

### Notes and apparatus
- No ★ legend anywhere in front matter, yet 60 ★ marks appear in ch-01 to ch-11 Notes. Fix option A: add the outline's ★ legend here; option B (preferred by the critique): convert all ★ to ✓ ~ ✗ ◇ ? volume-wide, so no legend is needed. — vol-3 M9 · front-01 (outline coverage "legend ✗")
- Content plan W5: define [V]/[R]/[M] (and decide on [V/M], [R/M], and *[reception]* for III-10 to III-12) in a "How to read this book" box, Vol. I front matter, repeated briefly in Vols. II–III — this file is the Vol. III home for the short version. — content-revision-plan W5 · front-01

### Naming and gazetteer
— none found

### Length and structure
- Outline coverage: map list only partial (Preface ✓; legend ✗; map list partial). — vol-3 §3 scorecard · front-01
- Front/back role: W5 rule "front matter frames, chapters narrate, back matter gives a dispute shortlist plus trivia"; check this file against III-F2 and III-B1 for repeated explanations. — content-revision-plan W5 · front-01

## Media hooks
- **Hero plate:** none (front matter has no hero slot in `illustration-plan.md`)
- **Secondary plates:** none
- **Maps:** none placed here (A1/A16 sit in III-F2)
- **Timelines / diagrams / tables:** **C11** monsoon wind panels (NE Nov–Mar / SW May–Sep) + Cocachin calendar strip (placement III-front-01, III-9); critique §5 item 2 ("Monsoon and season diagram… feeds front-01")
- **Characters appearing:** Cocachin, Arghun, the Polos (Marco, Niccolò, Maffeo), Columbus; comparative sources named: Ibn Battuta, Duarte Barbosa

## Gated by spikes
- S-02 (acceptance lint), S-03 (★ vs ✓~✗◇?, tag legend), S-06 (Columbus correction), S-07 (front/back roles and de-duplication), S-08 (figure C11), S-09 (C11 pipeline)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-F1.T1` Critical and factual fixes
- `III-F1.T5` Media placement (C11)
- `III-F1.T6` Lint pass and human voice read

### III-F1.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 8 Notes · 0 ★ · 2 without a lead marker
- **Do:**
  - Notes with no lead marker: [1], [3] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-3/front-01-indian-ocean-world.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-F1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 4 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/front-01-indian-ocean-world.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
