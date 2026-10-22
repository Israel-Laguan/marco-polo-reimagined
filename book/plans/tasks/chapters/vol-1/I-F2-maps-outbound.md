# I-F2 — Maps for the Outbound Road

**File:** `vol-1/front-02-maps-outbound.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,067 | n/a | — (n/a in Vol. I) | ok | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Epigraph is invented or conflated: *"from this city of Lop it is forty days' journey across the desert…"*. In Yule the Lop desert takes **a month** at its narrowest (Y:22928); "forty days" belongs to **Etzina** (Y:24539–24541). Fix: *"And here, where its breadth is least, it takes a month to cross it."* (Book I, Of the City of Lop and the Great Desert). Content plan W1.1. — vol-1 C2 · front-02:4
- Wider risk: the same file teaches the wrong number again ("When a chapter says 'forty days'…"). — vol-1 C2 · front-02:92

### Factual / fidelity
- Overview map caption calls it an "outbound corridor", but the map shows the whole round trip including the return. Fix (critique §5, multimedia plan triage): re-caption as the whole round trip. — vol-1 nit 6 · front-02:27
- Mongol-empire map caption says "Polo's generation"; whether `map-mongol-empire.gif` / `map-asia-mongol-empire.*` shows c. 1260–1295 boundaries or the 1279 maximum is **(unverified)**; check before captioning. — vol-1 §5 (Fixes to existing media) · front-02:35

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

### Length and structure
- Outline coverage only partly met: map list has no Venice–Genoa map and no first-journey map (scorecard). — vol-1 §3 scorecard · front-02

## Media hooks
- **Hero plate:** none (map guide)
- **Secondary plates:** none
- **Maps:** A1 Series overview (generated; "Each volume's front-02"). Existing: `map-marco-polo-overview.*` keep, re-caption as the whole round trip; `map-marco-polo-shepherd.jpg` keep as a historical-cartography curiosity (Shepherd 1911 base), half page at most; `map-asia-mongol-empire.*` replace with generated political map (A2, placed at I-F1). Critique §5: the two existing overview maps suit front-02 only; per-chapter maps need the M8 gazetteer fix first.
- **Timelines / diagrams / tables:** place tables (regenerate from fixed gazetteer)
- **Characters appearing:** Marco Polo, the elder Polo brothers (unnamed here), Tedaldo Visconti / Gregory X, the Great Khan (Kublai, unnamed); Prester John and King George (via Tenduc's "legends")

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format, Ramusio flag style)
- S-04 Gazetteer authority and naming policy (M8 tables, Balashan alias)
- S-06 Fact verification sheet (C2 epigraph, unverified map date range)
- S-07 Structure and length (front/back roles: missing Venice–Genoa / first-journey maps)
- S-08 LaTeX build pipeline (tables, map figures)
- S-09 Map and diagram pipeline (A1)
- S-11 Public-domain artwork sourcing and licensing (kept Shepherd 1911 map; Wikimedia credits)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-F2.T1` Critical and factual fixes
- `I-F2.T3` Re-voice to the S-01 standard (incl. length cuts)
- `I-F2.T5` Media placement (figures, tables, captions)
- `I-F2.T6` Lint pass and human voice read

### I-F2.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 5 Notes · 0 ★ · 1 without a lead marker
- **Do:**
  - Notes with no lead marker: [1] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-1/front-02-maps-outbound.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-F2.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 9 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/front-02-maps-outbound.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
