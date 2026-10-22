# III-B1 — Trivia, Disputes, and Afterlives — Volume III

**File:** `vol-3/back-01-trivia-and-afterlives.md` · **Status:** backlog · **Kind:** back

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 780 | n/a | — | ok (7/7) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Fake epigraph: *"Because of this book many set forth…"* is a self-confessed "paraphrase" sitting inside quotation marks. Fix: cut it. — vol-3 C1 · back-01:4
- Production meta-text: "Volume III's Venice chapter must not quietly reabsorb it". Fix: delete. — vol-3 C2 · back-01:43

### Factual / fidelity
- Adam's Peak "gathers Muslim, Hindu, and Christian footstep traditions in the book's telling". In the Book it is **Muslim (Adam) and Buddhist (Sagamoni Borcan)** (III-04:27, :39). Fix: "Muslim and Buddhist". — vol-3 m2 · back-01:17
- Cocachin entry repeats the one-sided Rashid corroboration without the Yang Zhijiu 1941 *Yongle dadian* notice (three envoys, 1290) or the fact that neither source names the Polos. — vol-3 M1 · back-01:33

### Dispute handling and Ramusio flags
— none found

### Voice and prose
— none found

### Notes and apparatus
— none found

### Naming and gazetteer
— none found

### Length and structure
- Some duplication with III-11 (scorecard: "acceptable as pointers"); W5 role rule — back matter gives a dispute shortlist plus trivia. Keep the Columbus/Toscanelli pointer (:37) consistent with the III-11 fix. — vol-3 §3 scorecard / content-revision-plan W5 · back-01:27, :37

## Media hooks
- **Hero plate:** none (back matter has no hero slot in `illustration-plan.md`)
- **Secondary plates:** none
- **Maps:** none
- **Timelines / diagrams / tables:** critique §5 item 5 says the reception timeline feeds back-01 (multimedia plan places **B5** at III-11). Multimedia §E: **pronunciation and names glossary** at the back of each volume (book form → modern form → respelling → gloss); Vol. III candidates from critique §5 item 7: Sagamoni Borcan (Śākyamuni Burqan), Cocachin (Kököchin), Kiacatu (Geikhatu), Casan (Ghazan), Abraiaman, *Choiach*, *Pacauta*, *Tembul*, *bād-gīr*, Chipangu (Jih-pên-kuo), *Milione*
- **Characters appearing:** Columbus, Paolo Toscanelli, Fra Mauro, Cocachin, Ramusio, Adam, the Polos

## Gated by spikes
- S-02, S-03 (Notes format), S-06 (Adam's Peak, Cocachin), S-07 (front/back roles and de-duplication), S-08 (glossary table), S-09 (only if B5 is also placed here)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-B1.T1` Critical and factual fixes
- `III-B1.T5` Media placement (glossary)
- `III-B1.T6` Lint pass and human voice read

### III-B1.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 7 Notes · 0 ★ · 2 without a lead marker
- **Do:**
  - Notes with no lead marker: [1], [4] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-3/back-01-trivia-and-afterlives.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-B1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 3 errors · 0 warnings — failing: markers, quote_verify
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/back-01-trivia-and-afterlives.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
