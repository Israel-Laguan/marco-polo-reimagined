# I-B1 — Trivia and Disputes — Volume I

**File:** `vol-1/back-01-trivia-and-disputes.md` · **Status:** backlog · **Kind:** back

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,259 | n/a | — (n/a in Vol. I) | ok | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Useful, but repeats errors (Curzola/Jacopo, Hormuz 'fails in the book', 'bad faith') and has an embellished epigraph". back-01:13 promises Ramusian material is "never silently absorbed"; the chapters break that promise (M5, handled per chapter).

### Critical
— none found

### Factual / fidelity
- Curzola misattributed: "strong tradition (Jacopo d'Acqui and later tellings)". ch-01:21 and Note [5] correctly say Jacopo puts the capture **at Ayas**; Curzola is later tradition (Ramusio) plus inference from the year (Yule Y:7369). Fix: "…dictated in Genoa is the book's own claim (1298). Curzola as the battle is later tradition (Ramusio) plus inference from the year; Jacopo d'Acqui, the nearest witness, puts the capture at Ayas." Content plan W1.4. — vol-1 M1 · back-01:33
- Captivity "after Curzola (Korčula), 1298" stated as plain fact. Fix: hedge: "…during a Genoese captivity in 1298, traditionally after Curzola". — vol-1 M1 · back-01:15
- Epigraph embellished: "*…for I knew I would not be believed*" is a popular expansion; Jacopo's notice is that he had not told half of what he saw (as ch-01 Note [14] paraphrases). Calling it "late tradition" also contradicts ch-01, where Jacopo is a near-contemporary. Fix: "*I have not told the half of what I saw.*" attributed to Jacopo d'Acqui, *Imago Mundi* (reported deathbed words). Content plan W1.1. — vol-1 m4 · back-01:4
- Vague scholarship attribution: "de Rachewiltz's" work for the embassy reading. Fix: cite de Rachewiltz, *Papal Envoys to the Great Khans* (1971) by title, no page numbers. — vol-1 m12 · back-01:37
- "one of the first widely read Latin sources": write "Western" (the book was not Latin originally). — vol-1 nit 8 · back-01:21

### Dispute handling and Ramusio flags
- "**Hormuz turned them around.** The outbound plan to take ship at Hormos fails in the book: stitched hulls, deadly summer wind, **bad faith in the haven**." "Bad faith" appears nowhere in the Book; the aborted plan is Yule's inference (Y:5902–5906). Fix: "**Did Hormuz turn them around?** Yule inferred that the Polos meant to sail from Hormuz and gave it up; the book itself only says 'let us return by another road to Kerman.' The stitched ships and the heat make the inference attractive, not certain." Content plan W2 (I-back). — vol-1 M2 · back-01:19
- Great Wall "seed" leaves out the main counter-argument: the masonry Wall at Suzhou/Jiayuguan is **Ming** (Jiayu Pass 1372); in Polo's day the Hexi defences were eroded Han-era earthworks. Fix as at I-11: one clause on the Ming date. — vol-1 M7 · back-01:45

### Voice and prose
— none found

### Notes and apparatus
- Production scaffolding: Note [11] gives the `/workspace/marco-polo/gazetteer.csv` path. Fix: strip the path, keep the reliability idea in plain words. — vol-1 m6 · back-01:83

### Naming and gazetteer
— none found
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-B1.T1`.

### Length and structure
- Triple explanation of the conversion pledge: "weak joint" here echoes front-01:41 and ch-02:31 ("the conversion pledge… is the weakest clause"). Content plan W5: front frames, chapters narrate, back matter gives a dispute shortlist plus trivia. — vol-1 m10 · back-01:37

## Media hooks
- **Hero plate:** none
- **Secondary plates:** none
- **Maps:** none
- **Timelines / diagrams / tables:** B6 Book date vs history (table-timeline): Sack of Baudas 1255 vs 1258 (ch-05); Mountain miracle 1275 / 1225, impossible (ch-05); Hulagu's attack on the Old Man 1252 / 1262 vs 1256 (ch-08); Chinggis made king 1187 vs 1206 (ch-12); Prester John war 1200 vs 1203 (ch-12); Elder voyage begins 1250 vs 1260 (ch-02). Critique: "a high-value sidebar for ch-12 or back-01"; multimedia plan places it here. Multimedia plan E: pronunciation and names glossary at the back of each volume (Cambaluc/Khanbaliq, Chandu/Shangdu, Badashan, Tauris, Zulcarnain, Natigay/Etügen, Kemiz/kumis, Bacsi/bakhshi, Sensin, paiza).
- **Characters appearing:** Marco Polo, Rustichello of Pisa, Niccolò Polo, Maffeo Polo, Jacopo d'Acqui, Berke, the Caliph (Mostas'im), the Old Man of the Mountain, Prester John, King George, Cocachin

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format)
- S-04 Gazetteer authority (pronunciation glossary forms)
- S-06 Fact verification sheet (M1, M2, M7, m4, m12)
- S-07 Structure and length decisions (front/back roles and de-duplication)
- S-08 LaTeX build pipeline (B6 table-timeline, glossary)
- S-09 Map and diagram pipeline (B6)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-B1.T1` Critical and factual fixes
- `I-B1.T3` Re-voice to the S-01 standard (incl. length cuts)
- `I-B1.T5` Media placement (figures, tables, captions) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `I-B1.T6` Lint pass and human voice read

### I-B1.T1 — Names to the S-04 policy; facts per S-06
- **Status:** in progress (targeted facts applied 2026-11-17; see note at end) · **Depends:** S-04 ✓, S-06 ✓
- **Now:** bare variants: Pamir → Pamier ×4, Hormuz → Hormos ×2, Baghdad → Baudas ×1, Old Hormuz → Hormos ×1, Dry Tree → Arbre Sec ×1, Alamut → Old Man of the Mountain ×1, Balkh → Balc ×1, Badakhshan → Badashan ×1 (+1 more)
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - F-34: "during a Genoese captivity in 1298, traditionally after Curzola"; Jacopo d'Acqui puts the capture at Ayas, Curzola is Ramusio's tradition.
- **Done when:** `python3 tools/lint.py -v vol-1/back-01-trivia-and-disputes.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names. The factual items are applied, or hedged as `registry/facts.md` says.

### I-B1.T3 — De-duplicate to the S-07 role matrix
- **Status:** backlog · **Depends:** S-07 ✓; after the chapters it points to have their `.T3` (so pointers name real Notes)
- **Do** (matrix in `plans/spikes/S-07-structure-length.md` § 2; roles in `VOICE-GUIDE.md` § Front and back matter):
  - Disputes become a shortlist: one line each (verdict + chapter and Note), ≤ 40 words: Curzola (:33, per F-34), the "1250" date (:35), the conversion pledge (:37, without "weak joint"), Baudas mountain (:39), Assassins (:41), Arbre Sec (:43), Pipino's first meeting (:51).
  - Cut: Great Wall silence (:45; home III-12 §4), visited vs reported (:47; the tags say it), numbers and days' journeys (:49; III-12 §5).
  - Trivia: "the book has many books" (:13) → one pointer sentence (home III-12 §2); keep the rest only where the chapter body does not already tell it.
  - Cut "How to use this back matter" (:55–57) to one sentence.
  - Same voice rules as the chapters (no archaisms, ≤ 1 "Anyway", no recaps); no sentence reused from another file.
- **Target:** ~700 words (lint cap 1,200).
- **Done when:** lint `length` passes for this file, and a person has read it against the matrix: every topic here is either its home or a one-line pointer.

### I-B1.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 10 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Notes with no lead marker: none — resolved 2026-11-17 under `APP.T9` (lint `markers` clean); a person still reads the new markers.
  - Run `python3 tools/lint.py -v vol-1/back-01-trivia-and-disputes.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-26 ✓ (2026-11-16):** The citation audit covers original Note(s) [3], [10]; preserve the checked locators, scope and corrections from [the locator registry](../../../registry/locators.md) when rewriting or renumbering. These findings do not complete the wider Notes task.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-B1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 4 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/back-01-trivia-and-disputes.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.


## S-16 handoff — T1 / trivia

- **Status:** backlog. Choose from S16-E9/E12/E15/E17 or the Hormuz route dispute, with attribution and without duplicating chapter notes. See [S-16 closeout](../../../research/results/S-16-closeout.md).

## S-21 source handoff

S-21 closed 2026-11-13 ([closure](../../../research/results/S-21-closure.md)). Apply in this file's chapter tasks: Trivia: use only checked S21-E rows; L items optional.

**Targeted continuity pass (2026-11-17), applied to `I-B1.T1`:** F-34 and M2: :15 hedged (“traditionally after Curzola”); :33 and Note [4] separate Jacopo d’Acqui’s Ayas (under 1296) from Ramusio’s Curzola, after I-01 [5]; :19 is now “Did Hormuz turn them around?” with the plan as Yule’s inference and no “bad faith”. The shortlist rewrite and names are not done. Lint shows no new errors for the file; the `.T3` re-voice and `.T6` human read stay open.
