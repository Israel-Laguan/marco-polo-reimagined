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
- C12 labels “thirteen” as the Book’s number; the Quanzhou hull’s thirteen compartments are a separate archaeological comparison (F-14), with limber holes qualifying any blanket watertight claim.

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
- **Do:** Axis break between 1206 and 1255 if the decades are empty; Mosul’s surrender may be shown as 1262 (F-02); the death date remains open.

### DIA.B3 — Kublai's reign and the Polo calendar
- **Status:** backlog · **Placement:** II-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Fleet sailing 1291–92 as a span (F-15); Chingkim "mid-1280s" as a span (F-06).

### DIA.B4 — The Song endgame, 1268–1279
- **Status:** backlog · **Placement:** II-10 / II-11 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Xiangyang siege as a span; the last battle unnamed (F-41).

### DIA.B5 — Reception, 1298 onward
- **Status:** piloted (S-09); extension open · **Placement:** III-11 (reused in III-10, III-B1) · **Depends:** S-09 ✓, S-20 ✓ (qualified selection); layout and extension still open
- **Do:** **Piloted in S-09** (`tools/media/data/B5.yaml`, 13 events to 1903). S-20 closed with a [qualified B5 selection](../../research/results/S-20-closure.md); choose later items with source rows and add an axis break if needed. The pilot now marks Fra Mauro approximately mid-15th century, dates Góis’s death separately in its note, and does not date Columbus-circle annotations. Review the rendered layout and citations before production.

### DIA.B6 — Book date vs history
- **Status:** backlog · **Placement:** I-B1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** A paired timeline: each row shows the Book's date and the record's, joined by a line. Needs a `pairs:` mode in timeline.py.

### DIA.C1 — Paper money
- **Status:** backlog · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Bark → sheet → seals → vermilion → circulation; 1287 revaluation sidebar. S17-F1/F3: label the 1 Zhiyuan to 5 Zhongtong *guan* conversion as official; both issues continued circulating. This is one scholarly source: verify a second independent source or the primary passage before printing the number, per the Phase R number rule. CUHK bronze blocks are not dated to 1287 solely by the issue date.

### DIA.C2 — The yam
- **Status:** backlog · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Stations, runner forts, express riders; attribute “ten days in one” to Polo, not a verified travel rate. S17-F2: a museum paiza illustrates a general safe-conduct pass; exact station counts remain unchecked.

### DIA.C3 — Keshig rota
- **Status:** backlog · **Placement:** II-3 · **Depends:** S-09 ✓, schematic build
- **Do:** Polo's 4 × 3,000 vs Palladius's 400.

### DIA.C4 — Mongol decimal army
- **Status:** backlog · **Placement:** I-12 · **Depends:** S-09 ✓, schematic build
- **Do:** *arban → tümen* vs the Book's terms.

### DIA.C5 — Paiza hierarchy
- **Status:** backlog · **Placement:** II-1 / I-2 · **Depends:** S-09 ✓, schematic build
- **Do:** Proposed silver → gerfalcon hierarchy and 1269 script change require independent source checks before the diagram asserts ranks or dates. S17-F2 supplies one dated iron-and-silver paiza, not proof of a hierarchy.

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
  - Still-open dates are drawn as spans or left out, never as points: Chingkim "mid-1280s" (F-06), the fleet's sailing 1291–92 (F-15), Pipino "1310s" (F-18).
  - B5 reception takes print dates (F-21), the Leeu printing with undated Columbus-circle postils (F-19), and the Catalan Atlas without the unsupported Chipangu claim; represent Fra Mauro’s surviving map as mid-15th century and distinguish the disputed 1459 dispatch (F-20). The [S-20 selection](../../research/results/S-20-closure.md) supplies later candidates.
  - B6 "Book date vs history" rows: Baidu and Casan 1294 vs 1295 (F-05); Bayan 1268 vs 1274 (F-29); Alaü's victory vs Hulagu's rout (F-01).
  - A date not in the sheet gets a row there first (S-06 method), then goes on the timeline.
- **Done when:** every event in the B1–B6 YAML has a `facts.md` row id, and no still-open row is drawn as a point.


**S-15 → DIA B1/B5 data:** `registry/facts.md` S15-F1, F4, F6–F8; `research/results/S-15-raw.md`. Plot Marco's c. 1254 birth as inferred, capture as disputed (1296 Jacopo / 1298 Ramusio), 1324 will 9 Jan and death 8 or 9 Jan; inventory 1324, judgment 1366. Mark uncle Maffeo's reported 1309 and 6 Feb 1310 will dates as unresolved and do not join them as one fact. Agnese's 1319 will is documented via report; parentage remains an identification.

**External S-15 check:** For Maffeo's will, Yule reports 6 February 1308 Venetian style = 1309 modern; Gullino's extant will is 6 February 1310 modern. Do not merge them by calendar conversion without comparison. The inventory is probably February 1324, not an exact date established here. Details in `research/results/S-15-external-intake.md`.


**S-15 source sweep → B5:** Bolognari 2024 reports the 1319 *Marco Polo Milion* confraternity entry and discusses a Florence manuscript dated c. 1325–1350 with the title *Milion*. Label byname and book title separately; do not treat 1305's disputed identification as certain or 1319 as necessarily the first usage. `registry/enrichment.md` S15-H3.

## S-17 data handoff (2026-11-11)

Use `registry/facts.md` S17-F1–F6 and the [checked intake](../../research/results/S-17-intake.md). C1: the 1287 **official** conversion was 1 *guan* Zhiyuan = 5 *guan* Zhongtong; both circulated. C2/C5: museum paiza as a dated object, not Polo's own; station numbers remain unchecked. A9: label reconstruction and avoid an invented complete palace plan. II-13 comparison: attribute each number to its textual witness; Mascherpa's Chinese source has not itself been checked. No speculative station totals or ranked paiza hierarchy are authorized by this intake.
