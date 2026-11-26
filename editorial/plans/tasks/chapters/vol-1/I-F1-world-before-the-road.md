# I-F1 — The World Before the Road

**File:** `vol-1/front-01-world-before-the-road.md` · **Status:** completed (2026-11-24) · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,070 | 1% | — (n/a in Vol. I) | ok [1–14] | no |

## Original critique findings

The line and Note numbers in this section refer to the critique draft. Current dispositions are recorded under Tasks.

### Critical
- Epigraph is invented: *"Ye must know that in the year of Christ… there were living in Venice two brothers…"* is not in Yule ("there were living in Venice two brothers" has 0 hits). The real Prologue ch. I opening is at Y:12495. Fix: replace with *"It came to pass in the year of Christ 1260, when Baldwin was reigning at Constantinople…"*, attributed "Prologue, ch. I (Yule–Cordier)". Also listed in content plan W1.1. — vol-1 C1 · front-01:4

### Factual / fidelity
- Note [6] credits the Curzola tradition to Jacopo d'Acqui; ch-01:21 and its Note [5] correctly say Jacopo puts the capture **at Ayas**, and Curzola rests on later tradition (Ramusio) plus inference from the year (Yule sidenote Y:7369). Fix: change "(Jacopo d'Acqui and later tradition…)" to "(Ramusio and later tradition; Jacopo names Ayas)". Content plan W1.4. — vol-1 M1 · front-01:74
- "The War of Saint Sabas (1256–1270)": Yule dates the outbreak at Acre to 1255 and gives no end year. **S-06 sweep:** F-38. — front-01:29

### Dispute handling and Ramusio flags
- The Hormuz "turning back" is presented as Book fact (the route summary bends through Hormuz as a failed sea plan). The Book only says "let us return by another road to… Kerman" (ch-07:41); the aborted sea plan is Yule's inference (Y:5902–5906); ch-03:25 handles it correctly. Fix: present it as Yule's inference, not the Book's words. Content plan W2 (I-front-01). — vol-1 M2 · front-01:54

### Voice and prose
- "Anyway, next it helps to name…": the narrative hinge is misused in expository front matter. — vol-1 nit 7 · front-01:25

### Notes and apparatus
- Citations out of order: [11] appears in the body before [10]. Fix: renumber. Content plan W5. — vol-1 m3 · front-01:48–54 Tracked for completion in `APP.T9` (2026-11-17). **Closed (best effort) 2026-11-18 under `APP.T9`:** fixed and lint-clean; human read not completed.
- Production scaffolding in a reader-facing Note: `/workspace/marco-polo/gazetteer.csv` path and visited/reported/uncertain tag language. Fix: strip the path, keep the reliability idea in plain words. — vol-1 m6 · front-01:82 (Note [10])
- Content plan W5 asks for a 150-word "How to read this book" box in Vol. I front matter defining the tags ([V]/[R]/[M], compound forms) and markers; which front file hosts it is open. — content-revision-plan W5 (Tags)

### Naming and gazetteer
— none found
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-F1.T1`.

### Length and structure
- Front matter duplicates ch-02: "Second, necessity… Third, papal…" re-argues ch-02's war and letter beats; the phrase "the conversion pledge… is the weakest clause" appears verbatim here and at ch-02:31 (and as "weak joint" at back-01:37). Fix: front-01 should point forward to ch-02, not pre-empt it. Content plan W5 de-duplication (front frames, chapters narrate). — vol-1 m10 · front-01:39–41

## Media hooks
- **Hero plate:** none. Critique §4 marks front-01 optional: "No scene. Use the political map instead of an illustration." Not in `illustration-plan.md` hero table.
- **Secondary plates:** none
- **Maps:** A2 The world in 1260 (Mongol successor khanates, Mamluks, Byzantium, Venetian and Genoese posts). Replaces `map-asia-mongol-empire.*` / `map-mongol-empire.gif` (a 1206–1294 animation, F-25; see I-F2).
- **Timelines / diagrams / tables:** B1 The Polo family, 1254–1324; B2 Mongol politics, 1206–1295 (critique §5 timelines 1 and 3: "Pair with front-01").
- **Characters appearing:** Niccolò Polo, Maffeo Polo, Marco Polo, Marco the Elder, Cublay, Alaü, Barca, Caidu, Sigatay, Michael Palaeologus, William of Rubruck, John of Plano Carpini, Ramusio and Jacopo d’Acqui (Note [11]), William Buchier (Note [12]).

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format; "How to read this book" box)
- S-04 Gazetteer authority (A2 map hook)
- S-06 Fact verification sheet (C1 epigraph, M1 Curzola, M2 Hormuz)
- S-07 Structure and length (front/back roles and de-duplication, m10)
- S-08 LaTeX build pipeline (A2, B1, B2 figures)
- S-09 Map and diagram pipeline (A2, B1, B2)

## Tasks

### I-F1.T1 — Names to the S-04 policy; facts per S-06
- **Status:** done (2026-11-24) · **Depends:** S-04 ✓, `GAZ.T5` ✓, S-06 ✓
- **Applied:** verified the existing Prologue epigraph. Retained place and person names use book forms with first-use glosses, including Lesser Hermenia in the A2 caption. The scope sentence points to I-F2, which carries Yule’s Hormos inference. The comparison of alternate routes (critique m1) belongs to I-F2.
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - F-34: Note [11] (was [6]) distinguishes Ramusio's Curzola tradition, favoured by Yule, from Jacopo’s Ayas account. It points to I-1, Notes 7–8.
    - F-25: A2 is in place and shows 1260. The older Mongol Empire animation is a separate asset.
    - F-38: the dispute over St Sabba began in 1255 and grew into a war that lasted years (Note [10], YC Introduction §31). The end date remains open in the facts registry.
- **Done when:** `python3 tools/lint.py -v vol-1/front-01-world-before-the-road.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names. The factual items are applied, or hedged as `registry/facts.md` says.

### I-F1.T3 — De-duplicate to the S-07 role matrix
- **Status:** done (2026-11-24) · **Depends:** S-07 ✓; I-1 and I-2 `.T3` ✓
- **Applied:** added a series preface under 60 words linked to III-12, kept the historical framing and reader’s key, and reduced the treatment of the detour and papal commission to one I-2 pointer. The scope sentence links to I-F2. The silences and repeated reliability advice were cut.
- **Do** (matrix in `plans/spikes/S-07-structure-length.md` § 2; roles in `VOICE-GUIDE.md` § Front and back matter):
  - Keep as home: Mediterranean trade and Venice–Genoa rivalry; Mongol successor realms; name and date conventions (:56).
  - Add a series preface of ≤ 60 words (purpose; the rules themselves live in III-12 §8). The full *How to read this book* box is `APP.T1`.
  - *Why Latins went east* (:37–43): keep "opportunity" and "information hunger"; cut "necessity" and "papal politics" (:39–41) to one forward sentence to I-2 (m10). Don't reuse "weakest clause".
  - Cut the silences sentence (:50); home is III-12 §4.
  - Cut the route summary (:54) to one scope sentence; the route lives in I-F2.
  - Cut the closing paragraph (:58) to one sentence; "Anyway" (:25) goes.
  - Same voice rules as the chapters (no archaisms, ≤ 1 "Anyway", no recaps); no sentence reused from another file.
- **Target:** ~1,150 (with the APP.T1 box) words (lint cap 1,200).
- **Done when:** lint `length` passes for this file, and a person has read it against the matrix: every topic here is either its home or a one-line pointer.

### I-F1.T4 — Notes and apparatus to the S-03 convention
- **Status:** done (2026-11-24) · **Depends:** S-03 ✓, `APP.T2` ✓
- **Now:** 14 claim anchors and 14 matching Notes in sequence, 0 ★, 0 without a lead marker. The audited locators and scope of Note [1] are intact. The reader’s key is in place and the old workspace-path Note has been superseded.
- **Do:**
  - Notes with no lead marker: none — resolved 2026-11-17 under `APP.T9` (lint `markers` clean); a person still reads the new markers.
  - Run `python3 tools/lint.py -v vol-1/front-01-world-before-the-road.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-26 ✓ (2026-11-16):** The citation audit covers original Note(s) [1]; preserve the checked locators, scope and corrections from [the locator registry](../../../../../research/registry/locators.md) when rewriting or renumbering. These findings do not complete the wider Notes task.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-F1.T5 — Figures and captions

- **Status:** done 2026-11-24 · **Depends:** S-08 ✓, S-09 ✓
- **Verified:** `tools/build/build.sh i-f1-check vol-1/front-01-world-before-the-road.md` built A2, B2 and B1 with zero placeholders, undersized rasters or overfull lines at or above 10 pt. The three rendered captions and the reader’s key were visually checked. I-F2’s incoming map link still matches the heading.

### I-F1.T6 — Lint green and human read
- **Status:** done (2026-11-24; E0 · W0) · **Depends:** every other task in this file · S-02 ✓
- **Current lint:** 1,070 words, 1% Yule overlap, 0 errors, 0 warnings (`Mongolica` in *Pax Mongolica* added to `NAME_STOP` in `tools/lint.py`).
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 5 errors · 1 warning — failing: citations, markers, quote_verify, scaffolding; warnings: names
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/front-01-world-before-the-road.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.

**Earlier continuity pass (2026-11-17):** F-34 and M2 corrected the capture attribution and labelled the Hormos sea plan as Yule’s inference. `APP.T9` restored citation order before the current revision.
