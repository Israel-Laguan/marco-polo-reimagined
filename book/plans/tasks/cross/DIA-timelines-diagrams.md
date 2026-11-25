# DIA — Timelines and diagrams

**Status:** done 2026-11-24. Timelines B1–B6 and diagrams C1–C17 have PDF and SVG editions and manuscript placements. · **Plan doc:** `multimedia-plan.md` § B, § C

**Verified 2026-11-24.** All 23 figures fit the 4.5 × 5.4 in measure, all 60 timeline entries point to fact-sheet rows, and the three volume PDFs build with no placeholders or undersized rasters.

## Scope
Timelines (TikZ from YAML), schematic diagrams (TikZ), data charts (Python), and labelled cutaways (a plate base from `PLT` + TikZ labels).

## Figure inventory
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
  - C5 paiza comparison (II-1, referenced from I-2)
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
S-09 ✓ (pipeline, 2026-11-10) · S-06 ✓ (dates, closed 2026-11-03) · S-10 ✓ (cutaway bases are `PLT.C12`–`C16`) · S-08 ✓ (print build, 2026-11-10)

## Tasks
S-09 closed 2026-11-10. Visual system: `multimedia-plan.md` § Visual system (values in `tools/media/style.yaml`).
- **Timelines:** `tools/media/data/B#.yaml` (format in `tools/media/timeline.py`'s header; copy `B5.yaml`) → `python3 tools/media/timeline.py B#`.
- **Schematics ("schematic build", done 2026-11-19):** a body in `tools/media/diagrams/C#-name.tex` (header comment names sources) → `python3 tools/media/diagram.py C#` (shares `timeline.tex`'s preamble via `timeline.standalone`; prints the size and flags anything over 4.5 × 5.4 in). Sources beyond the Book: facts.md § Schematic data.
- **Charts (done 2026-11-19):** `tools/media/.venv/bin/python tools/media/charts.py C#` (matplotlib, `style.yaml`, `--test`; data inline with a source per row; sources in facts.md § Schematic data). Output in `media/diagrams/`.
- **Done when** (every task): the `.pdf` + `.svg` are in `media/timelines/` or `media/diagrams/` at 4.5 in wide and no taller than 5.4 in, every date carries its `facts.md` row id, and the chapter links the `.svg`.

### DIA.B1 — Polo family, 1254–1324
- **Status:** done 2026-11-19 · `data/B1.yaml` → `media/timelines/B1-polo-family.*`, linked in I-F1. Birth and captivity are spans; Maffeo's 1309 and 1310 wills are two separate marks (F-17); adds Agnese 1319 and the 1324 inventory / 1366 judgment (S15-F6, F8) · **Placement:** I-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Dates from facts.md § Timeline data (B1 row); Pipino as a span.

### DIA.B2 — Mongol politics, 1206–1295
- **Status:** done 2026-11-19 · `B2-mongol-politics.*`, linked in I-F1. Axis 1200–10 / 1255–1300 (starts at Aung Khan 1203, F-03); Baibars and the St Sabas war still left out (F-38, F-39 open) · **Placement:** I-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Axis break between 1206 and 1255 if the decades are empty; Mosul’s surrender may be shown as 1262 (F-02); the death date remains open.

### DIA.B3 — Kublai's reign and the Polo calendar
- **Status:** done 2026-11-19 · `B3-kublai-polo-calendar.*`, linked in II-F1. Fleet span runs late 1290 – early 1292 with both readings in the note (the 2026-11-17 review under C11); Kublai 1260/1294 added to the sheet from `yc` · **Placement:** II-F1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Fleet sailing 1291–92 as a span (F-15); Chingkim "mid-1280s" as a span (F-06).

### DIA.B4 — The Song endgame, 1268–1279
- **Status:** done 2026-11-19 · `B4-song-endgame.*`, linked in II-10 (end of narrative) · **Placement:** II-10 / II-11 · **Depends:** S-09 ✓, DIA.T1
- **Do:** Xiangyang siege as a span; the last battle unnamed (F-41).

### DIA.B5 — Reception, 1298 onward
- **Status:** done 2026-11-24. The 23-event timeline adds the Cépoy colophon (1307), the Venetian roll's “Marco Polo Milion” (1319), and Wood's first edition (1995). Each addition has a fact-sheet row. The figure runs through 2024 with the 1680–1815 break and measures 4.50 × 5.15 in. [Earlier layout review](../../research/results/B5-review-2026-11.md). · **Placement:** III-11, referenced from III-10 and III-B1 · **Depends:** S-09 ✓, S-20 ✓
- **Do:** **Piloted in S-09** (`tools/media/data/B5.yaml`, 13 events to 1903). S-20 closed with a [qualified B5 selection](../../research/results/S-20-closure.md); choose later items with source rows and add an axis break if needed. The pilot now marks Fra Mauro approximately mid-15th century, dates Góis’s death separately in its note, and does not date Columbus-circle annotations. Review the rendered layout and citations before production.

### DIA.B6 — Book date vs history
- **Status:** done 2026-11-19 · `pairs:` mode added to `timeline.py`; `B6-book-vs-history.*`, linked in I-B1. Alaü/Barca row: the Book's 1261 (added to the sheet) against the record's 1262–63 · **Placement:** I-B1 · **Depends:** S-09 ✓, DIA.T1
- **Do:** A paired timeline: each row shows the Book's date and the record's, joined by a line. Needs a `pairs:` mode in timeline.py.

### DIA.C1 — Paper money
- **Status:** done 2026-11-19 · `C1-paper-money.*`, linked in II-5. The 1 : 5 is printed as official: Yule is the second independent source (facts.md § Schematic data) · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Bark → sheet → seals → vermilion → circulation; 1287 revaluation sidebar. S17-F1/F3: label the 1 Zhiyuan to 5 Zhongtong *guan* conversion as official; both issues continued circulating. This is one scholarly source: verify a second independent source or the primary passage before printing the number, per the Phase R number rule. CUHK bronze blocks are not dated to 1287 solely by the issue date.

### DIA.C2 — The yam
- **Status:** done 2026-11-19 · `C2-yam.*`, linked in II-5. All figures labelled as the Book's; no station totals asserted · **Placement:** II-5 · **Depends:** S-09 ✓, schematic build
- **Do:** Stations, runner forts, express riders; attribute “ten days in one” to Polo, not a verified travel rate. S17-F2: a museum paiza illustrates a general safe-conduct pass; exact station counts remain unchecked.

### DIA.C3 — Keshig rota
- **Status:** done 2026-11-19 · `C3-keshig.*`, linked in II-3. Rota ring plus to-scale bars: 3,000 (Book) vs c. 400 and c. 100 (Palladius) · **Placement:** II-3 · **Depends:** S-09 ✓, schematic build
- **Do:** Polo's 4 × 3,000 vs Palladius's 400.

### DIA.C4 — Mongol decimal army
- **Status:** done 2026-11-24 · `C4-decimal-army.*` keeps the Book's Tuc/Toman/Guz, the two gaps and Yule's glosses. The Mongol column uses May's *arban*, *jaghun* and *minggan* and de Rachewiltz's *tümen*. See facts.md § Schematic data. · **Placement:** I-12 · **Depends:** S-09 ✓, schematic build
- **Do:** *arban → tümen* vs the Book's terms.

### DIA.C5 — Paiza hierarchy
- **Status:** done 2026-11-19 · gate settled by the [paiza intake](../../research/results/S-17-paiza-intake.md) (*Yuan shi* 98 / 202 re-read); `C5-paiza.*`, linked in II-1 (not repeated in I-2). Book vs record: 100 and 1,000 agree; the 10,000 lion is a tiger in the record; no record match for the 100,000 tablet; gerfalcon attested 1261–80 for relay riders. Script note: 1269 decree for sealed edicts, one tally re-inscribed 1281 · **Placement:** II-1 / I-2 · **Depends:** S-09 ✓, schematic build
- **Do:** Proposed silver → gerfalcon hierarchy and 1269 script change require independent source checks before the diagram asserts ranks or dates. S17-F2 supplies one dated iron-and-silver paiza, not proof of a hierarchy.

### DIA.C6 — Tutia furnace
- **Status:** done 2026-11-19 · `C6-tutia-furnace.*`, linked in I-8 · **Placement:** I-8 · **Depends:** S-09 ✓, schematic build
- **Do:** Process flow.

### DIA.C7 — Zayton cost stack
- **Status:** done 2026-11-19 · `C7-zayton-cost.*`, linked in II-14. Freight marked as Ramusio's version · **Placement:** II-14 · **Depends:** S-09 ✓, schematic build
- **Do:** Duty + freight = "half the investment", as a stacked bar.

### DIA.C8 — Ilkhan succession: the Book vs the record
- **Status:** done 2026-11-19 · `C8-ilkhan-succession.*`, linked in II-15. Adds the Argon 1286 vs 1284 slip · **Placement:** II-15 · **Depends:** S-09 ✓, schematic build
- **Do:** Two columns, Book and record, with the 1294/1295 slips marked (F-05).

### DIA.C9 — Gold : silver ratio gradient
- **Status:** done 2026-11-19 · `C9-gold-silver.*`, linked in II-8 (not repeated in II-7). Places east to west in the Book's order (the gazetteer sequence lists the Carajan province before Yachi); the Descent market has no gazetteer row; 10 : 1 (1287) and 12 : 1 references from Yule · **Placement:** II-7 / II-8 · **Depends:** S-09 ✓, charts.py
- **Do:** 1:8 → 1:5 across Yunnan and Burma; place axis in gazetteer order.

### DIA.C10 — Pole Star altitude: cubits vs latitude
- **Status:** done 2026-11-19 · `C10-pole-star.*`, linked in III-6 (not repeated in III-3). Sumatra plotted as "not seen", Cambaet as "still higher" with no number; no cubit-to-degree conversion asserted · **Placement:** III-3 / III-6 · **Depends:** S-09 ✓, charts.py
- **Do:** Book's cubits against real latitude from the gazetteer.

### DIA.C11 — Monsoon panels + Cocachin calendar
- **Status:** done 2026-11-24 · `C11-monsoon-cocachin.*` uses per-basin months (S18-F4), both departure readings (F-15), and labels the voyage stages as Yule's reconstruction. · **Placement:** III-F1 and III-9, referenced from III-1, III-3, III-5 and III-7 · **Depends:** S-09 ✓, charts.py
- **Do:** Show the wind seasons separately for the South China Sea and Indian Ocean. Keep the departure alternatives consistent with B3.
- **2026-11-17 review:** F-15 reports a late-1290/early-1291 inference as well as Yule's 1292 reconstruction. Verify and label any range or alternatives in both B3 and C11; do not present the Samara wait or death-before-sailing as independently documented fleet events. [Handoff](../../status/critique-text-media-handoff-2026-11-17.md).

### DIA.C12 — Seagoing junk cutaway
- **Status:** done 2026-11-24 · `C12-seagoing-junk.*` attributes thirteen compartments to Ramusio's text and labels the Quanzhou wreck's independent bulkhead count and limber holes (F-14). · **Placement:** III-1 and the II-14 preview · **Depends:** S-09 ✓, base plate `PLT.C12`
- **Do:** Labels in TikZ over the plate; "thirteen" as the Book's number (F-14).

### DIA.C13 — Sewn-plank ship of Hormos
- **Status:** done 2026-11-23 · `C13-sewn-plank-hormos.*`, linked in I-7 · **Placement:** I-7 · **Depends:** S-09 ✓, base plate `PLT.C13`
- **Editorial review, 2026-11-25:** The diagram’s horse transport and hide cover follow Polo. The I-7 note cites the reused timbers at al-Balīd as regional evidence for sewn construction. The caption and diagram identify the vessel’s shape and steering as conjectural. [S22-E2](../../registry/enrichment.md#s-22-supplement--cross-project-candidates-2026-11-13)

### DIA.C14 — Traction vs counterweight trebuchet
- **Status:** done 2026-11-23 · `C14-trebuchet-comparison.*`, linked in II-11 · **Placement:** II-11 · **Depends:** S-09 ✓, base plate `PLT.C14`
- **Do:** Two machines side by side.

### DIA.C15 — Qanat cross-section
- **Status:** done 2026-11-23 · `C15-qanat.*`, linked in I-8 · **Placement:** I-8 · **Depends:** S-09 ✓, base plate `PLT.C15`
- **Do:** Could be pure TikZ (no plate) if `PLT.C15` is late.

### DIA.C16 — Cane palace roof
- **Status:** done 2026-11-23 · `C16-cane-palace-roof.*`, linked in I-13 · **Placement:** I-13 · **Depends:** S-09 ✓, base plate `PLT.C16`
- **Do:** Split bamboo tiles.

### DIA.C17 — Seasonal orbit (was map A8)
- **Status:** done 2026-11-19 · `C17-seasonal-orbit.*`, linked in II-4 (not repeated in I-13). A ring of the Book's months; Palladius's lunar months in the note · **Placement:** II-4 / I-13 · **Depends:** S-09 ✓, schematic build
- **Do:** Moved from MAP in S-09: Cachar Modun and Chagannor are `unfixed`. Dadu ↔ Shangdu ↔ Cachar Modun as a ring of months; the 28 August libation.


### DIA.T1 — Timeline data for B1–B6 from the fact sheet
- **Status:** done 2026-11-19 (B1–B4, B6; B5 stays with DIA.B5). New dates went into facts.md § Timeline data first. New event kinds `life`, `document`, `rule`, `war` in `style.yaml` · **Depends:** S-06 ✓, S-09 (the YAML schema)
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
