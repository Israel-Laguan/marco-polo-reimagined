# II-B1 — Trivia and Disputes — Volume II

**File:** `vol-2/back-01-trivia-and-disputes.md` · **Status:** backlog · **Kind:** back

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 876 | n/a | — | ok (7/7) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit · **[W]** content-plan only.

### Critical
- **[C]** Invented epigraph: "All these cities are so great that…" (labelled "The book's habitual gasp before Manzi's numbers") is not in Yule–Cordier. Fix: a verified Kinsay line, e.g. "the city is beyond dispute the finest and the noblest in the world"; alternatively drop the quotation marks and the source label. Observation (not in critique): that Kinsay line sits inside ch-13:4's epigraph. — vol-2 C3 · back-01:4; content plan W1.1

### Factual / fidelity
- — none found

### Dispute handling and Ramusio flags
- **[M]** The "silences" cluster (tea, foot-binding, Great Wall) is filled here (:45) only because II-02's aside (ch-02:51) defers it in one meta sentence. The critique's fix goes in II-02; recheck this entry once II-02 carries the substance, so the two do not diverge. — vol-2 M12 · back-01:45
- **[M]** "Mixed tags in the chapter heads are there on purpose" assumes the reader has been told what the tags mean; no reader-facing page explains them (fix lives in II-F1). — vol-2 M8 · back-01:43

### Voice and prose
- **[m]** Paper money, coal, Ahmad and the two capitals repeat front-01:31–39 and ch-05 almost word for word ("Coal as quiet proof" vs "Coal… quiet corroboration"). Fix: "make back-01 pure dispute shortlist plus trivia, and cut the repeats". Affected here: :15 (two capitals), :17 (paper money), :19 (coal), :21 (Ahmad). — vol-2 m12 · back-01:15–21; content plan W5

### Notes and apparatus
- — none found

### Naming and gazetteer
- — none found
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-B1.T1`.

### Length and structure
- **[m]** Role of back matter (dispute shortlist plus trivia, not re-explanation) is an S-07 decision shared with II-F1; content plan W5 "Front and back matter de-duplication". — vol-2 m12

## Media hooks
- **Hero plate:** — none
- **Secondary plates:** — none
- **Maps:** — none
- **Timelines / diagrams / tables:** Pronunciation and names glossary ("back of each volume": book form → modern form → respelling → gloss), the print substitute for the critique's audio moments (Cambaluc/Khanbaliq, Keshican/keshig, Pul-i-Sangīn, Quinsay/Xingzai, Zayton/Zaitūn, Faghfur, Bayan Chincsan, *Sing/sheng*, Toscaol, Bularguchi, naccara/naqqāra, Aijaruc/Ai-yaruq, Natigai) — `multimedia-plan.md` §E; critique §5 "Audio and pronunciation moments"
- **Characters appearing:** Marco Polo, Niccolò and Maffeo Polo (Saianfu), Ahmad Fanakati, Kublai (as "the Khan")

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (markers in Notes)
- S-04 Gazetteer authority and naming policy (glossary forms)
- S-06 Fact verification sheet (epigraph)
- S-07 Structure and length decisions (front/back roles and de-duplication)
- S-08 LaTeX build pipeline (glossary table)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-B1.T1` Critical fix (epigraph)
- `II-B1.T3` De-duplicate against front-01 and ch-05
- `II-B1.T5` Pronunciation glossary
- `II-B1.T6` Lint pass and human read

### II-B1.T1 — Names to the S-04 policy
- **Status:** backlog · **Depends:** S-04 ✓
- **Now:** bare variants: Shangdu → Chandu ×1, Dadu → Cambaluc ×1, Yangzhou → Yanju ×1, Xiangyang → Saianfu ×1, Hangzhou → Kinsay ×1, Quanzhou → Zayton ×1
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
- **Done when:** `python3 tools/lint.py -v vol-2/back-01-trivia-and-disputes.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names.

### II-B1.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 7 Notes · 0 ★ · 3 without a lead marker
- **Do:**
  - Notes with no lead marker: [1], [6], [7] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-2/back-01-trivia-and-disputes.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-B1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 4 errors · 0 warnings — failing: markers, quote_verify
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/back-01-trivia-and-disputes.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
