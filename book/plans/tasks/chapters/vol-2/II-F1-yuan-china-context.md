# II-F1 — Yuan China: The World You Are Entering

**File:** `vol-2/front-01-yuan-china-context.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,016 | n/a | — | ok (9/9) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit · **[W]** content-plan only.

### Critical
- **[C]** Invented epigraph: "Now I have told you of the splendour of Cublay… and I will tell you of the city of Cambaluc…" is not in Yule–Cordier (whitespace-normalised search of both volumes). Fix: replace with "Now am I come to that part of our Book in which I shall tell you of the great and wonderful magnificence of the Great Kaan now reigning" (Bk II.i, verified). Observation (not in critique): ch-01:4 already uses this line as its epigraph, so the swap would duplicate it; decide at T1. — vol-2 C3 · front-01:4; content plan W1.1

### Factual / fidelity
- **[M]** Cachanfu given as Xi'an: "toward Shanxi and Cachanfu (Xi'an)". II-06 (ch-06:29–31, Note [8]) correctly separates Cachanfu (Puzhou/Hezhong at the Yellow River bend) from Kenjanfu (Xi'an). Fix: "…toward Shanxi, the Yellow River crossing at Cachanfu, and Kenjanfu (Xi'an)". — vol-2 M2 · front-01:45; content plan W2 (II-front)

### Dispute handling and Ramusio flags
- **[M]** No note on Ramusio-only chapters or passages, though the outline asks the front matter for one (beat 3). — vol-2 M8 · front-01 (whole)

### Voice and prose
- **[m]** Paper money, coal, Ahmad and the two capitals are each explained three times in near-identical words across front-01:31–39, back-01:15–21 and ch-05 (e.g. "Coal… quiet corroboration" here vs back-01 "Coal as quiet proof"). Fix: keep the context framing **here** in front-01; make back-01 pure dispute shortlist plus trivia; cut the repeats. — vol-2 m12 · front-01:31–39; content plan W5 (front/back de-duplication)
- **[W]** Hinge tic: "Anyway, next it helps to hold one plain fact" (grep count of "Anyway" in file: 1; lint cap ≤ 1). — content plan W0 · front-01:29

### Notes and apparatus
- **[M]** Missing the outline's "How to read the tags and markers" preface: the [V]/[R]/[M] tags appear as bare "**[M]**" lines that no reader-facing page explains, and the reliability legend is not reprinted (outline beats 1 and 3). Fix: add a 150-word "How to read the tags and markers" box to front-01. — vol-2 M8 · front-01 (whole)
- **[m]** Compound tags [V/M] (II-02, II-14) and [R/M] (II-08) are undefined; README and outline define only [V], [R], [M]. Fix option: "define the compounds in front-01" (or use [M] with a one-line gloss in the chapters). Content plan W5 places the full box in Vol. I front matter, "repeated briefly in Vols. II–III". — vol-2 m10; content plan W5

### Naming and gazetteer
- **[M]** Same Cachanfu/Kenjanfu correction must land in the gazetteer (row seq 54) so front-01 and front-02 match II-06. — vol-2 M2 · gazetteer.csv seq 54

### Length and structure
- **[m]** Front/back role split (frame here, narrate in chapters, shortlist plus trivia in back-01) per m12 and content plan W5; S-07 decides the final division. — vol-2 m12

## Media hooks
- **Hero plate:** Vol. II frontispiece: portrait of Kublai, **PD**, Yuan imperial portrait album (NPM Taipei), portrait 3:4 — see `illustration-plan.md` (II-front row). Place in this file.
- **Secondary plates:** — none found
- **Maps:** — none (A7 belongs to II-F2)
- **Timelines / diagrams / tables:** B3 Kublai's reign and the Polo calendar (1260 → 1294), placed at II-front-01 (`multimedia-plan.md`); matches critique §5 timeline (1260 accession … 1294 Kublai dies). Tags-and-markers box (M8).
- **Characters appearing:** Kublai (Cublay), Chinghis (lineage), Ahmad Fanakati, Marco Polo; the Polo family (Saianfu claim, :27)

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (tag box content, marker legend, Ramusio flag style)
- S-04 Gazetteer authority (Cachanfu/Kenjanfu)
- S-05 Character registry (frontispiece Kublai portrait)
- S-06 Fact verification sheet (epigraph replacement, Cachanfu)
- S-07 Structure and length decisions (front/back roles and de-duplication)
- S-08 LaTeX build pipeline (frontispiece, timeline)
- S-09 Map and diagram pipeline (B3)
- S-11 Public-domain artwork sourcing and licensing (frontispiece)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-F1.T1` Critical and factual fixes (epigraph, Cachanfu)
- `II-F1.T2` Ramusio-only note in the reader preface
- `II-F1.T3` De-duplicate against back-01 and ch-05; trim tics
- `II-F1.T4` Tags-and-markers box and legend reprint
- `II-F1.T5` Media placement (frontispiece, B3)
- `II-F1.T6` Lint pass and human voice read

### II-F1.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 1 error · 0 warnings — failing: quote_verify
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/front-01-yuan-china-context.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
