# DIA — Timelines and diagrams

**Status:** backlog · **Plan doc:** `multimedia-plan.md` § B, § C

## Scope
Timelines (TikZ from YAML), schematic diagrams (TikZ), data charts (Python), and labelled cutaways (a plate base from `PLT` + TikZ labels).

## Backlog
- **Timelines:**
  - B1 Polo family (I-F1)
  - B2 Mongol politics (I-F1)
  - B3 Kublai & Polo calendar (II-F1)
  - B4 Song endgame (II-10/11)
  - B5 Reception 1298 onward (III-11; piloted in S-09)
  - B6 Book date vs history (I-B1)
- **Schematics:**
  - C1 paper money (II-5)
  - C2 yam (II-5)
  - C3 keshig rota (II-3)
  - C4 decimal army (I-12)
  - C5 paiza hierarchy (II-1 / I-2)
  - C6 tutia furnace (I-8)
  - C7 Zayton cost stack (II-14)
  - C8 Ilkhan succession (II-15)
- **Charts:**
  - C9 gold:silver gradient (II-7/8)
  - C10 Pole Star altitude (III-3/6)
  - C11 monsoon panels + Cocachin calendar (III-F1, III-9)
- **Cutaways:**
  - C12 junk with 13 compartments (III-1)
  - C13 sewn-plank ship (I-7)
  - C14 trebuchets (II-11)
  - C15 qanat (I-8)
  - C16 cane palace roof (I-13)
  - C17 seasonal orbit (II-4 / I-13; was map A8)
- **Candidates without an ID yet** (proposed in the critique; **decided in S-09**: asbestos dropped; canal summit → inset on map A12; Kinsay metrology → a § D table in II-13; monsoon reuse → C11; reception reuse → B5):
  - asbestos processing (I-11);
  - canal summit split at Sinjumatu and salt-earth leaching (II-10);
  - Kinsay revenue metrology (II-13);
  - monsoon reuse in III-1, III-5 and III-7 (extend C11);
  - reception timeline reuse in III-10 and III-B1 (extend B5).
- Timeline data must come from the S-06 fact sheet; several dates are corrections (Ghazan 1295, Bayan 1274, etc.). The dates per timeline are in `registry/facts.md` § Timeline data (S-06 ✓).
- C12 labels "thirteen" as the Book's number; the Quanzhou wreck is not a source yet (F-14).

## Gated by spikes
S-09 ✓ (pipeline, 2026-11-10) · S-06 ✓ (dates, closed 2026-11-03) · S-10 ✓ (cutaway bases are `PLT.C12`–`C16`, Akool route) · S-08

## Tasks
S-09 closed 2026-11-10. Visual system: `multimedia-plan.md` § Visual system (values in `tools/media/style.yaml`).
- **Timelines:** `tools/media/data/B#.yaml` (format in `tools/media/timeline.py`'s header; copy `B5.yaml`) → `python3 tools/media/timeline.py B#`.
- **Schematics ("schematic build"):** the first C task adds `tools/media/diagrams/C#.tex` and a build step that compiles them with `timeline.tex`'s preamble (same font, colours, `pdftocairo -svg`).
- **Charts:** the first chart task adds `tools/media/charts.py` on `map.py`'s pattern (matplotlib, `style.yaml`, `--test`).
- **Done when** (every task): the `.pdf` + `.svg` are in `media/timelines/` or `media/diagrams/` at 4.5 in wide and no taller than 5.4 in, every date carries its `facts.md` row id, and the chapter links the `.svg`.

### DIA.B1 — Polo family, 1254–1324
- **Status:** backlog · **Placement:** I-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Dates from facts.md § Timeline data (B1 row); Pipino as a span.

### DIA.B2 — Mongol politics, 1206–1295
- **Status:** backlog · **Placement:** I-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Axis break between 1206 and 1255 if the decades are empty; Mosul only as "1261 (Yule)".

### DIA.B3 — Kublai's reign and the Polo calendar
- **Status:** backlog · **Placement:** II-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Fleet sailing 1291–92 as a span (F-15); Chingkim "mid-1280s" as a span (F-06).

### DIA.B4 — The Song endgame, 1268–1279
- **Status:** backlog · **Placement:** II-10 / II-11 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Xiangyang siege as a span; the last battle unnamed (F-41).

### DIA.B5 — Reception, 1298 onward
- **Status:** piloted (S-09); extension open · **Placement:** III-11 (reused in III-10, III-B1) · **Depends:** S-09 ✓, S-20 for the post-1603 rows
- **Do:** **Piloted in S-09** (`data/B5.yaml`, 13 events to 1903). Extend when S-20 adds facts rows for Yule 1871, Benedetto 1928, Moule–Pelliot 1938, Wood 1995, Vogel 2013; then add a second axis break.

### DIA.B6 — Book date vs history
- **Status:** backlog · **Placement:** I-B1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** A paired timeline: each row shows the Book's date and the record's, joined by a line. Needs a `pairs:` mode in timeline.py.

### DIA.C1 — Paper money
- **Status:** backlog · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Bark → sheet → seals → vermilion → circulation; 1287 revaluation sidebar.

### DIA.C2 — The yam
- **Status:** backlog · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Stations, runner forts, express riders; "ten days in one" to scale.

### DIA.C3 — Keshig rota
- **Status:** backlog · **Placement:** II-3 · **Depends:** S-09 ✓, schematic build
- **Do:** Polo's 4 × 3,000 vs Palladius's 400.

### DIA.C4 — Mongol decimal army
- **Status:** backlog · **Placement:** I-12 · **Depends:** S-09 ✓, schematic build
- **Do:** *arban → tümen* vs the Book's terms.

### DIA.C5 — Paiza hierarchy
- **Status:** backlog · **Placement:** II-1 / I-2 · **Depends:** S-09 ✓, schematic build
- **Do:** Silver → gerfalcon; the 1269 script change.

### DIA.C6 — Tutia furnace
- **Status:** backlog · **Placement:** I-8 · **Depends:** S-09 ✓, schematic build
- **Do:** Process flow.

### DIA.C7 — Zayton cost stack
- **Status:** backlog · **Placement:** II-14 · **Depends:** S-09 ✓, schematic build
- **Do:** Duty + freight = "half the investment", as a stacked bar.

### DIA.C8 — Ilkhan succession: the Book vs the record
- **Status:** backlog · **Placement:** II-15 · **Depends:** S-09 ✓, schematic build
- **Do:** Two columns, Book and record, with the 1294/1295 slips marked (F-05).

### DIA.C9 — Gold : silver ratio gradient
- **Status:** backlog · **Placement:** II-7 / II-8 · **Depends:** S-09 ✓, charts.py
- **Do:** 1:8 → 1:5 across Yunnan and Burma; place axis in gazetteer order.

### DIA.C10 — Pole Star altitude: cubits vs latitude
- **Status:** backlog · **Placement:** III-3 / III-6 · **Depends:** S-09 ✓, charts.py
- **Do:** Book's cubits against real latitude from the gazetteer.

### DIA.C11 — Monsoon panels + Cocachin calendar
- **Status:** backlog · **Placement:** III-F1, III-9 (reused in III-1, III-5, III-7) · **Depends:** S-09 ✓, charts.py or a map variant of A16
- **Do:** NE Nov–Mar / SW May–Sep; the calendar strip uses the same 1291/1292 span as B3.

### DIA.C12 — Seagoing junk cutaway
- **Status:** backlog · **Placement:** III-1 (preview II-14) · **Depends:** S-09 ✓, base plate `PLT.C12`
- **Do:** Labels in TikZ over the plate; "thirteen" as the Book's number (F-14).

### DIA.C13 — Sewn-plank ship of Hormos
- **Status:** backlog · **Placement:** I-7 · **Depends:** S-09 ✓, base plate `PLT.C13`
- **Do:** Coir stitching, hide deck with horses.

### DIA.C14 — Traction vs counterweight trebuchet
- **Status:** backlog · **Placement:** II-11 · **Depends:** S-09 ✓, base plate `PLT.C14`
- **Do:** Two machines side by side.

### DIA.C15 — Qanat cross-section
- **Status:** backlog · **Placement:** I-8 · **Depends:** S-09 ✓, base plate `PLT.C15`
- **Do:** Could be pure TikZ (no plate) if `PLT.C15` is late.

### DIA.C16 — Cane palace roof
- **Status:** backlog · **Placement:** I-13 · **Depends:** S-09 ✓, base plate `PLT.C16`
- **Do:** Split bamboo tiles.

### DIA.C17 — Seasonal orbit (was map A8)
- **Status:** backlog · **Placement:** II-4 / I-13 · **Depends:** S-09 ✓, schematic build
- **Do:** Moved from MAP in S-09: Cachar Modun and Chagannor are `unfixed`. Dadu ↔ Shangdu ↔ Cachar Modun as a ring of months; the 28 August libation.


### DIA.T1 — Timeline data for B1–B6 from the fact sheet
- **Status:** backlog · **Depends:** S-06 ✓, S-09 (the YAML schema)
- **Do:**
  - Write each timeline's YAML from `registry/facts.md` § Timeline data only; each event carries its row id (`F-07`) as its source.
  - Still-open dates are drawn as spans or left out, never as points: Chingkim "mid-1280s" (F-06), the fleet's sailing 1291–92 (F-15), Pipino "1310s" (F-18), Mosul only as "1261 (Yule)" (F-02).
  - B5 reception takes the print dates (F-21), the Leeu copy and postils (F-19), the Catalan Atlas 1375 with no Chipangu, and Fra Mauro 1459 (F-20); S-20 adds the later rows.
  - B6 "Book date vs history" rows: Baidu and Casan 1294 vs 1295 (F-05); Bayan 1268 vs 1274 (F-29); Alaü's victory vs Hulagu's rout (F-01).
  - A date not in the sheet gets a row there first (S-06 method), then goes on the timeline.
- **Done when:** every event in the B1–B6 YAML has a `facts.md` row id, and no still-open row is drawn as a point.
