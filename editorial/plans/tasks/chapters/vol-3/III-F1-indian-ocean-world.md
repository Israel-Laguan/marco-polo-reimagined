# III-F1 — The Indian Ocean World (and Why a Princess Boards a Ship)

**File:** `vol-3/front-01-indian-ocean-world.md` · **Status:** completed · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 960 | n/a | — | ok (7/7) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Misquoted epigraph: "And when the ships had been made ready…" — Yule has "had been equipt". Fix: restore the exact wording (W1.1 lists front-01 among the 13 epigraph files). — vol-3 C1 · front-01:4

### Factual / fidelity
- "Bent the Atlantic" overstates Columbus's debt to Polo and contradicts ch-11's own caution. Fix: tone it down, in step with the III-11 Columbus fixes (Leeu Latin copy; notes undated; Toscanelli correspondence contested). — vol-3 M4 · front-01:27

### Dispute handling and Ramusio flags
— none found

### Voice and prose
— none found (scorecard: "Good primer"; one "Anyway" at :35 is within the ≤ 1 limit)

### Notes and apparatus
- No ★ legend anywhere in front matter, yet 60 ★ marks appear in ch-01 to ch-11 Notes. Fix option A: add the outline's ★ legend here; option B (preferred by the critique): convert all ★ to ✓ ~ ✗ ◇ ? volume-wide, so no legend is needed. — vol-3 M9 · front-01 (outline coverage "legend ✗")
- Content plan W5: define [V]/[R]/[M] (and decide on [V/M], [R/M], and *[reception]* for III-10 to III-12) in a "How to read this book" box, Vol. I front matter, repeated briefly in Vols. II–III — this file is the Vol. III home for the short version. — content-revision-plan W5 · front-01

### Naming and gazetteer
— none found
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-F1.T1`.

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
- `III-F1.T1` Critical and factual fixes ✅ completed
- `III-F1.T3` De-duplicate to the S-07 role matrix ✅ completed (2026-11-24)
- `III-F1.T4` Notes and apparatus to the S-03 convention ✅ completed (2026-11-24)
- `III-F1.T5` Media placement (C11) · S-08 ✓: ✅ completed (`tools/build/build.sh iii-f1 vol-3/front-01-indian-ocean-world.md`: `0 placeholders, 0 undersized rasters, 0 overfull lines (>= 10pt), 11 pages`)
- `III-F1.T6` Lint pass and human voice read ✅ completed (2026-11-24: `PASS · E0 W0 · 960 w · 1% verbatim`)

### III-F1.T1 — Names to the S-04 policy; facts per S-06
- **Status:** ✅ completed (facts 2026-11-17; names 2026-11-24) · **Depends:** S-04 ✓, `GAZ.T5`, S-06 ✓
- **Now:** first-mention glosses applied in prose (`Chamba (Champa)`, `Java the Less (Sumatra)`, `Seilan (Sri Lanka)`, `Maabar (Coromandel)`, `Melibar (Malabar)`, `Hormos (Hormuz)`); later repeat glosses removed; `lint.py` shows E0 W0 (no `name_policy` warnings).
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - F-19 / S-20: tone "bent the Atlantic" down to match III-11. The Seville Latin copy has notes by Columbus and his circle of uncertain date; do not present it as evidence of pre-1492 use. Omit the Toscanelli link or attribute the disputed correspondence.
- **Done when:** `python3 tools/lint.py -v vol-3/front-01-indian-ocean-world.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names. The factual items are applied, or hedged as `registry/facts.md` says.

### III-F1.T3 — De-duplicate to the S-07 role matrix
- **Status:** ✅ completed (2026-11-24) · **Depends:** S-07 ✓; after the chapters it points to have their `.T3` (so pointers name real Notes)
- **Do** (matrix in `plans/spikes/S-07-structure-length.md` § 2; roles in `VOICE-GUIDE.md` § Front and back matter):
  - Keep as home: monsoon logic; what "India" means; the Ilkhanid politics of the Cocachin errand (:31–33, frame only; the voyage is III-9).
  - Added the preface beat (report-heavy sea book; return in III-9 restores autobiography) and Indian/African name forms (`Maabar`, `Melibar`, `Abash`, `Madeigascar`); the short box with *[reception]* is `APP.T1`. ✅
  - Chipangu (:27): frame only. Cut the Columbus overstatement ("bent the Atlantic", M4); home III-11.
  - Kept "What you are about to read" as the scope paragraph, trimmed the back-matter clause to a one-line pointer; "Anyway" gone. ✅
  - Same voice rules as the chapters (no archaisms, ≤ 1 "Anyway", no recaps); no sentence reused from another file.
- **Target:** ≤ 1,000 words (lint cap 1,200). **Actual:** 960 w.
- **Done when:** lint `length` passes for this file, and a person has read it against the matrix: every topic here is either its home or a one-line pointer.

### III-F1.T4 — Notes and apparatus to the S-03 convention
- **Status:** ✅ completed (2026-11-24) · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 7 Notes · 0 ★ · 0 without a lead marker · Note [1] link fixed to `#fig-c11-monsoon-overview`.
- **Do:**
  - Notes with no lead marker: none — resolved 2026-11-17 under `APP.T9` (lint `markers` clean); a person still reads the new markers.
  - Run `python3 tools/lint.py -v vol-3/front-01-indian-ocean-world.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-F1.T6 — Lint green and human read
- **Status:** ✅ completed (2026-11-24: `PASS · E0 W0 · 960 w · 1% verbatim`) · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 4 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/front-01-indian-ocean-world.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
- **Verified:** All critical and factual fixes applied (epigraph corrected to "had been equipt", Columbus overstatement toned down per S-06). Names policy applied (first-mention glosses: Chamba, Java the Less, Seilan, Maabar, Melibar, Hormos). De-duplication complete per S-07. Notes use ✓~✗?◇ convention with 0 ★. C11 diagram placed and referenced. Voice compliant (0 "Anyway", no archaisms).

