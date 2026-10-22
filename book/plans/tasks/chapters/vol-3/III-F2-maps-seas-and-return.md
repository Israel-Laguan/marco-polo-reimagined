# III-F2 — Maps for the Seas and the Return

**File:** `vol-3/front-02-maps-seas-and-return.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 790 | n/a | — | ok (3/3) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Invented epigraph: "And from Zayton they sailed…", labelled a "Book III itinerary hinge". It does not exist in Yule; the Prologue never names Zayton (III-09 Note [8] concedes as much). Fix: use Prologue xviii, "They put forth to sea, and after sailing for some three months they arrived at a certain Island towards the South…" (`yule-vol1.txt`). — vol-3 C1 · front-02:4
- "Soft" label tic: 1 in the place table ("Soft peninsula ID", :39), plus Note [3] "Soft and legendary toponyms" (:90). Fix: strip the label. — vol-3 C2 · front-02:39, :90
- Scaffolding: "Image paths point at `../media/` placeholders" (:9) and Note [1] "media placeholders" (:86) — stale "placeholder" text, caught by the W0 scaffolding check. — content-revision-plan W1.3 / W0 · front-02:9, :86

### Factual / fidelity
- Generated "map" is geographically wrong and mis-credited: `media/map-indian-ocean.jpg` captioned "(Wikimedia Commons — credit in media/ATTRIBUTIONS.md)", but `ATTRIBUTIONS.md` lists it as a *generated* plate (byte-identical in size to `drawing-indian-ocean-schematic.png`). Errors: "Hormuz" at the southern tip of Arabia (the Aden position); "SINAE" over Persia; China north-east of India with an overland route across the Himalaya; Ceylon on the wrong side of the peninsula; post-1500 three-masted European ships. Fix: replace, or caption "decorative plate — not a map" (credit: generated). Multimedia plan verdict: **Drop**. — vol-3 M12 · front-02:19-21
- `map-return-route.jpg` is byte-identical to `map-marco-polo-overview.jpg` (checked with `cmp`), though its caption describes a dedicated return schematic; caption also credits Wikimedia. Fix: replace with the real return-route map (A16 / critique §5 item 1). Multimedia plan: front-02 captions "must be corrected now". — vol-3 M12 · front-02:27-29
- Place table equates Polo's Male with the Maldives ("Male / Maldives | Maldives | Cowries and ambergris"), as does the gazetteer row. III-07:13 and its Note [2] explicitly refuse that collapse, and Polo mentions no cowries there. Fix: list "Male and Female Isles — legendary (no fix)" and rename or annotate the gazetteer row. — vol-3 m3 · front-02:62

### Dispute handling and Ramusio flags
— none found

### Voice and prose
— none found (one "Anyway" at :80, within the ≤ 1 limit)

### Notes and apparatus
— none found beyond the Soft/placeholder items above

### Naming and gazetteer
- Gazetteer forms instead of the book's Yule forms: `Sememant` (ch-06 and Yule: *Semenat*, :23) and `Kalhat` (ch-08 and Yule: *Calatu*, :68). Scorecard also flags "non-gazetteer names". Fix: W5 switches gazetteer `book_name` to the Yule forms and regenerates the front-02 place tables from it. — vol-3 m4 · front-02:23, :68

### Length and structure
- Front/back de-duplication per W5 (front matter frames; chapters narrate). — content-revision-plan W5 · front-02

## Media hooks
- **Hero plate:** none (front matter)
- **Secondary plates:** none
- **Maps:** **A1** series overview (generated; each volume's front-02); **A16** the Cocachin return (III-9 + III-front-02). Critique §5 item 1 plotting order: Cambaluc → Zayton [inferred] → Chamba [possible] → Pentam → Samara / Java the Less [certain] → Necuveran → Seilan → Maabar / Cail → Coilum → Comari → Eli → Melibar → [Gozurat / Cambaet optional] → Kesmacoran → Hormos [inferred] → Kerman → Abhar → Tauris → Trebizond → Constantinople → Negropont → Venice; solid for Prologue-named stages, dashed for inferred; seasonal labels; inset of Ilkhanate/Yuan borders c. 1294. Prerequisite: gazetteer rows for Abhar and Negropont.
- **Existing media:** `map-marco-polo-overview.png` keep, re-caption as the whole round trip; `map-indian-ocean.*` drop; `map-return-route.jpg` drop (multimedia triage)
- **Timelines / diagrams / tables:** the two existing place tables (:33, :50), to be regenerated from the gazetteer
- **Characters appearing:** Cocachin, the Polos, Columbus

## Gated by spikes
- S-02, S-03 (Notes format), S-04 (gazetteer authority; Male/Maldives; Yule forms), S-06 (map and Male corrections), S-07 (front/back roles), S-08 (tables, figures), S-09 (A1, A16)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-F2.T1` Critical and factual fixes (epigraph, captions now)
- `III-F2.T4` Notes and apparatus normalisation; place tables from gazetteer
- `III-F2.T5` Media placement (A1, A16)
- `III-F2.T6` Lint pass and human voice read

### III-F2.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 3 errors · 0 warnings — failing: quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/front-02-maps-seas-and-return.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
