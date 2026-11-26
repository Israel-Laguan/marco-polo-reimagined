# I-F2 — Maps for the Outbound Road

**File:** `vol-1/front-02-maps-outbound.md` · **Status:** completed (2026-11-24) · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 297 | 4% | — (n/a in Vol. I) | ok [1–6] | no |

## Original critique

The references below point to the draft examined in the critique. The task entries record the revisions.

### Critical
- Epigraph is invented or conflated: *"from this city of Lop it is forty days' journey across the desert…"*. In Yule the Lop desert takes **a month** at its narrowest (Y:22928); "forty days" belongs to **Etzina** (Y:24539–24541). Fix: *"And here, where its breadth is least, it takes a month to cross it."* (Book I, Of the City of Lop and the Great Desert). Content plan W1.1. — vol-1 C2 · front-02:4
- Wider risk: the same file teaches the wrong number again ("When a chapter says 'forty days'…"). — vol-1 C2 · front-02:92

### Factual / fidelity
- Overview map caption calls it an "outbound corridor", but the map shows the whole round trip including the return. Fix (critique §5, multimedia plan triage): re-caption as the whole round trip. — vol-1 nit 6 · front-02:27
- Mongol-empire map caption says "Polo's generation"; **S-06 (F-25, inspected):** `map-mongol-empire.gif` and `map-asia-mongol-empire.*` are one 9-frame animation, 1206 → 1294; the 1279 frame is the maximum, the 1294 frames the four khanates, and a static print shows frame 1 (1206). Caption the 1294 frame, "c. 1294". — vol-1 §5 (Fixes to existing media) · front-02:35

### Dispute handling and Ramusio flags
- Hormuz "turning back" stated as Book fact ("Hormuz (Hormos), where the sea plan fails"). It is Yule's inference (Y:5902–5906); the Book only returns the reader to Kerman (ch-07:41). Content plan W2 (I-front-02). — vol-1 M2 · front-02:17
- Outbound route differs from ch-03: front-02 gives Ayas → Anatolian highlands → **Tauris** → Kerman → Hormuz; ch-03:23 gives Yule's Ayas → Sivas → **Mardin → Mosul → Baghdad** → Hormuz (Y:5904); ch-05 [16] and ch-06 [16] leave both open. Fix: present both as reconstructions. — vol-1 m1 · front-02:17
- Ramusian material absorbed unflagged: Badakhshan table row "Marco's recovery in the hills" is Ramusio only. Fix: 3–6-word tag ("Ramusio's text adds") per M5/W3. — vol-1 M5 · front-02:73

### Voice and prose
— none found

### Notes and apparatus
- Production scaffolding: Note [1] gives `/workspace/marco-polo/gazetteer.csv` and `/workspace/marco-polo/media/` paths. Fix: strip the paths. — vol-1 m6 · front-02:100
- Stale placeholder text: "captions below use placeholders until those files are filled" and Note [1] "when files arrive", but the files exist in `media/`. Fix: delete the stale lines. — vol-1 m6 · front-02:9, :100

### Naming and gazetteer
- Place tables follow `gazetteer.csv`, whose book_name column uses modern forms (Bokhara, Mosul, Sivas, Erzincan/Erzurum, Yazd, Balkh, Talikan, Badakhshan, Wakhan, Pamir, Kashgar/Yarkand/Khotan, Pem, Karakorum, Shangdu, Succiu), so front-02 disagrees with every chapter (Bocara, Mausul, Savast, Arzinga/Arziron, Yasdi, Balc, Taican, Badashan, Vocan, Pamier, Cascar/Yarcan/Cotan, Pein, Caracoron, Chandu, Sukchur). Fix: change gazetteer book_name to Yule forms (modern form in modern_name), add the ~25–27 missing Vol. I rows, **regenerate the front-02 tables**. Content plan W5 gazetteer. — vol-1 M8 · front-02 place tables
- Gazetteer error surfaced here: the Badakhshan alias "Balashan" is wrong; Yule's form is Badashan. — vol-1 M8 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-F2.T1`.

### Length and structure
- Outline coverage only partly met: map list has no Venice–Genoa map and no first-journey map (scorecard). — vol-1 §3 scorecard · front-02

## Media hooks
- **Hero plate:** none (map guide)
- **Secondary plates:** none
- **Maps:** A1 series round trip. The index points to A2 in I-F1 and A18, A3, A4, A5 and A6 in their chapters. Legacy maps and credits are covered by `MED.T2`.
- **Tables:** three place tables and the no-fix list from the series gazetteer.

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format, Ramusio flag style)
- S-04 Gazetteer authority and naming policy (M8 tables, Balashan alias)
- S-06 Fact verification sheet (C2 epigraph; map date range F-25)
- S-07 Structure and length (front/back roles: missing Venice–Genoa / first-journey maps)
- S-08 LaTeX build pipeline (tables, map figures)
- S-09 Map and diagram pipeline (A1)
- S-11 ✓ closed for plates only; the kept Shepherd 1911 map and the Wikimedia credits moved to `MED.T2`

## Tasks

### I-F2.T1 — Names to the S-04 policy; facts per S-06
- **Status:** done (2026-11-24) · **Depends:** S-04 ✓, `GAZ.T5` ✓, S-06 ✓
- **Applied:** Kept the exact Yule Lop epigraph. The guide gives the Tauris and Yule routes as reconstructions and treats the return to Kerman as narrative sequence. The abandoned sailing plan is attributed to Yule.
- **Names and tables:** Applied Book forms and first-mention glosses. Updated the gazetteer to attribute the Badashan recovery to Ramusio, remove the invalid alias and supply a complete Sinju description. Regenerated the tables and no-fix list and checked that they match the generator. Checked prose names and glosses separately because front-matter lint omits `name_policy`.
- **F-25:** The 1294 frame is archived under `MED.T2`. I-F2 points to the edition's 1260 map in I-F1.

### I-F2.T3 — De-duplicate to the S-07 role matrix
- **Status:** done (2026-11-24) · **Depends:** S-07 ✓
- **Applied:** The guide keeps the three route summaries, map index, generated tables and identification cautions. The travel-time caution points to III-12's “Famous stress-points” section. The closing recap was cut. The guide is 297 prose words against a target of 500.
- **Human review:** Read against the S-07 role matrix and II-2 for voice.

### I-F2.T4 — Notes and apparatus to the S-03 convention
- **Status:** done (2026-11-24) · **Depends:** S-03 ✓, `APP.T2` ✓
- **Applied:** Six Notes with lead markers and sequential anchors. The route and Hormos dispute have separate anchors. The pointers to I-2, I-3, I-7 and I-9 were checked against the current chapter Notes.
- **Check:** `markers`, `tags` and `citations` pass.

### I-F2.T5 — Media placement
- **Status:** done (2026-11-24) · **Depends:** S-08 ✓, S-09 ✓, `MED.T2` ✓
- **Applied:** A1 stays in the guide with its round-trip caption. The index links to the existing figure and map-heading anchors, including the Adriatic inset and the elder Polos’ first voyage.
- **Check:** Volume I PDF and HTML builds completed. All six index links reach their maps in both builds. Pages xvii–xxiv were proofed, including the figure, tables and Notes. The build reported zero placeholders and zero undersized rasters.

### I-F2.T6 — Lint green and human read
- **Status:** done (2026-11-24; E0 · W0) · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 9 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Checked 2026-11-24:** `python3 tools/lint.py -v vol-1/front-02-maps-outbound.md` reported 0 errors and 0 warnings. `python3 tools/gazetteer.py check` reported 198 rows and 0 problems.
- **Remaining:** Human review of names, Notes and voice.
