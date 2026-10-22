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
- `I-B1.T2` Ramusio flags and dispute asides
- `I-B1.T3` Re-voice to the S-01 standard (incl. length cuts)
- `I-B1.T4` Notes and apparatus normalisation
- `I-B1.T5` Media placement (figures, tables, captions)
- `I-B1.T6` Lint pass and human voice read

### I-B1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 2 errors · 0 warnings — failing: quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/back-01-trivia-and-disputes.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
