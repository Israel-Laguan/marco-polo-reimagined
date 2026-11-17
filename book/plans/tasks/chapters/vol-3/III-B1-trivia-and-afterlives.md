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
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-B1.T1`.

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
- S-13 ✓ (2026-11-11): `registry/scholarship.md`; items in this file's `.T1`/`.T4`

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-B1.T1` Critical and factual fixes
- `III-B1.T5` Media placement (glossary) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `III-B1.T6` Lint pass and human voice read

### III-B1.T1 — Names to the S-04 policy; facts per S-06
- **Status:** in progress (targeted facts applied 2026-11-17; see note at end) · **Depends:** S-04 ✓, S-06 ✓
- **Now:** bare variants: Japan → Chipangu ×1, Sumatra → Java the Less ×1, Andaman → Angamanain ×1, Malabar → Melibar ×1, Madagascar → Madeigascar ×1
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - F-23: Adam's Peak is Muslim and Buddhist "in the Book"; Hindu and Portuguese-Christian claims only as later traditions (Tennent, via Yule).
    - F-15: the Chinese and Persian accounts corroborate an embassy but, as Jackson reports, name no Polos; Yang’s inferred late 1290/early 1291 sailing and Yule’s 1292 remain debated.
  - **S-13 ✓ (`registry/scholarship.md` § The 2024 anniversary):** candidates, each "as reported by Orlando 2025" until the edition is seen: Agnese, a possible daughter (will of July 1319); the inventory's *bocheta* is a jewel, not the Mongol headdress; Pietro the "Tartar" may have been bought at Rialto; Madagascar owes its name to a copyist (`andreose2024textual`, read). Cut any "silver belt of a Tartar knight".
- **Done when:** `python3 tools/lint.py -v vol-3/back-01-trivia-and-afterlives.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names. The factual items are applied, or hedged as `registry/facts.md` says.

### III-B1.T3 — De-duplicate to the S-07 role matrix
- **Status:** backlog · **Depends:** S-07 ✓; after the chapters it points to have their `.T3` (so pointers name real Notes)
- **Do** (matrix in `plans/spikes/S-07-structure-length.md` § 2; roles in `VOICE-GUIDE.md` § Front and back matter):
  - Disputes become a shortlist (one line each, chapter and Note): Chipangu gold (:31), Cocachin with Yang Zhijiu (:33, per F-15).
  - Cut everything III-10, III-11 and III-12 already tell: *Milione* (:23), the book outran the man (:27), personal landings (:35), Columbus (:37), Wood (:39), Great Wall harvest (:41), Ramusio's homecoming (:43), "Afterlives in one breath" (:45–49).
  - Keep sea-book trivia: ships of Manzi (:13), pepper and pearls (:19), the name Madagascar (:21), Trebizond (:25); Adam's Peak (:17) fixed to Muslim and Buddhist (F-23). The Sumatra wait (:15) → cut (III-3, III-F1).
  - One closing sentence at most.
  - Same voice rules as the chapters (no archaisms, ≤ 1 "Anyway", no recaps); no sentence reused from another file.
- **Target:** ~400 words (lint cap 1,200).
- **Done when:** lint `length` passes for this file, and a person has read it against the matrix: every topic here is either its home or a one-line pointer.

### III-B1.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 7 Notes · 0 ★ · 2 without a lead marker
- **Do:**
  - Notes with no lead marker: [1], [4] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-3/back-01-trivia-and-afterlives.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-26 ✓ (2026-11-16):** The citation audit covers original Note(s) [5], [6]; preserve the checked locators, scope and corrections from [the locator registry](../../../registry/locators.md) when rewriting or renumbering. These findings do not complete the wider Notes task. Keep the body and Note aligned: Larner disputes whether Polo’s Book directly shaped Columbus’s westward project; the surviving annotated copy is not proof of pre-1492 use.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-B1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 3 errors · 0 warnings — failing: markers, quote_verify
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/back-01-trivia-and-afterlives.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.


**S-15 source sweep:** For the pasta legend, de Rachewiltz 1997 pp. 61–62 locates the wheat/pasta account in the Ramusian text and distinguishes his reading of *lasagne* from later translation labels (`registry/enrichment.md` S15-H5). This is a source-and-translation note, not evidence that Marco introduced pasta.

**S-20 closed (2026-11-13):** apply the [myth and afterlife decisions](../../../research/results/S-20-closure.md), preserving attributed second-hand accounts and omitting unverified claims. The planned duplicate Columbus/Toscanelli passage is still slated for removal; do not imply the Seville copy was used before 1492.

## S-21 source handoff

S-21 closed 2026-11-13 ([closure](../../../research/results/S-21-closure.md)). Apply in this file's chapter tasks: Trivia: Tennent's Catholic hereditary charmer (S21-E36) and the 1559 floating cask (S21-E33) are checked candidates.

**Targeted continuity pass (2026-11-17), applied to `III-B1.T1`:** F-15 and F-19: the Cocachin entry (:33, Note [3]) now separates the corroborated embassy from the unnamed Polos and gives the debated sailing date; Note [5] drops “the usual view dates most postils before 1492” and attributes the 1497–98 arguments to Larner and Gil. Shortlist and names are not done. Lint shows no new errors for the file; the `.T3` re-voice and `.T6` human read stay open.
