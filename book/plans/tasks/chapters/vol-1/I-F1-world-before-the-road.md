# I-F1 — The World Before the Road

**File:** `vol-1/front-01-world-before-the-road.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,467 | n/a | — (n/a in Vol. I) | [10]/[11] out of order | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Epigraph is invented: *"Ye must know that in the year of Christ… there were living in Venice two brothers…"* is not in Yule ("there were living in Venice two brothers" has 0 hits). The real Prologue ch. I opening is at Y:12495. Fix: replace with *"It came to pass in the year of Christ 1260, when Baldwin was reigning at Constantinople…"*, attributed "Prologue, ch. I (Yule–Cordier)". Also listed in content plan W1.1. — vol-1 C1 · front-01:4

### Factual / fidelity
- Note [6] credits the Curzola tradition to Jacopo d'Acqui; ch-01:21 and its Note [5] correctly say Jacopo puts the capture **at Ayas**, and Curzola rests on later tradition (Ramusio) plus inference from the year (Yule sidenote Y:7369). Fix: change "(Jacopo d'Acqui and later tradition…)" to "(Ramusio and later tradition; Jacopo names Ayas)". Content plan W1.4. — vol-1 M1 · front-01:74

### Dispute handling and Ramusio flags
- The Hormuz "turning back" is presented as Book fact (the route summary bends through Hormuz as a failed sea plan). The Book only says "let us return by another road to… Kerman" (ch-07:41); the aborted sea plan is Yule's inference (Y:5902–5906); ch-03:25 handles it correctly. Fix: present it as Yule's inference, not the Book's words. Content plan W2 (I-front-01). — vol-1 M2 · front-01:54

### Voice and prose
- "Anyway, next it helps to name…": the narrative hinge is misused in expository front matter. — vol-1 nit 7 · front-01:25

### Notes and apparatus
- Citations out of order: [11] appears in the body before [10]. Fix: renumber. Content plan W5. — vol-1 m3 · front-01:48–54
- Production scaffolding in a reader-facing Note: `/workspace/marco-polo/gazetteer.csv` path and visited/reported/uncertain tag language. Fix: strip the path, keep the reliability idea in plain words. — vol-1 m6 · front-01:82 (Note [10])
- Content plan W5 asks for a 150-word "How to read this book" box in Vol. I front matter defining the tags ([V]/[R]/[M], compound forms) and markers; which front file hosts it is open. — content-revision-plan W5 (Tags)

### Naming and gazetteer
— none found

### Length and structure
- Front matter duplicates ch-02: "Second, necessity… Third, papal…" re-argues ch-02's war and letter beats; the phrase "the conversion pledge… is the weakest clause" appears verbatim here and at ch-02:31 (and as "weak joint" at back-01:37). Fix: front-01 should point forward to ch-02, not pre-empt it. Content plan W5 de-duplication (front frames, chapters narrate). — vol-1 m10 · front-01:39–41

## Media hooks
- **Hero plate:** none. Critique §4 marks front-01 optional: "No scene. Use the political map instead of an illustration." Not in `illustration-plan.md` hero table.
- **Secondary plates:** none
- **Maps:** A2 The world in 1260 (Mongol successor khanates, Mamluks, Byzantium, Venetian and Genoese posts). Replaces `map-asia-mongol-empire.*` / `map-mongol-empire.gif` (date range **unverified**, see I-F2).
- **Timelines / diagrams / tables:** B1 The Polo family, 1254–1324; B2 Mongol politics, 1206–1295 (critique §5 timelines 1 and 3: "Pair with front-01").
- **Characters appearing:** Niccolò Polo, Maffeo Polo, Marco Polo, Rustichello (via preamble), Kublai, Hulagu, Berke, Kaidu, Michael Palaeologus, William of Rubruck, John of Plano Carpini, Jacopo d'Acqui (Note [6]); Prester John (legendary)

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format; "How to read this book" box)
- S-04 Gazetteer authority (A2 map hook)
- S-06 Fact verification sheet (C1 epigraph, M1 Curzola, M2 Hormuz)
- S-07 Structure and length (front/back roles and de-duplication, m10)
- S-08 LaTeX build pipeline (A2, B1, B2 figures)
- S-09 Map and diagram pipeline (A2, B1, B2)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-F1.T1` Critical and factual fixes
- `I-F1.T2` Ramusio flags and dispute asides
- `I-F1.T3` Re-voice to the S-01 standard (incl. length cuts)
- `I-F1.T4` Notes and apparatus normalisation
- `I-F1.T5` Media placement (figures, tables, captions)
- `I-F1.T6` Lint pass and human voice read
