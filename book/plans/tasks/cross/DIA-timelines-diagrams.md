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
  - B5 Reception 1298–2013 (III-11)
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
- **Candidates without an ID yet** (proposed in the critique; decide in S-09):
  - asbestos processing (I-11);
  - canal summit split at Sinjumatu and salt-earth leaching (II-10);
  - Kinsay revenue metrology (II-13);
  - monsoon reuse in III-1, III-5 and III-7 (extend C11);
  - reception timeline reuse in III-10 and III-B1 (extend B5).
- Timeline data must come from the S-06 fact sheet; several dates are corrections (Ghazan 1295, Bayan 1274, etc.). The dates per timeline are in `registry/facts.md` § Timeline data (S-06 ✓).
- C12 labels "thirteen" as the Book's number; the Quanzhou wreck is not a source yet (F-14).

## Gated by spikes
S-09 (pipeline) · S-06 ✓ (dates, closed 2026-11-03) · S-10 (cutaway bases) · S-08

## Tasks
_After S-09:_ one task per asset, `DIA.B1` … `DIA.C16`.

### DIA.T1 — Timeline data for B1–B6 from the fact sheet
- **Status:** backlog · **Depends:** S-06 ✓, S-09 (the YAML schema)
- **Do:**
  - Write each timeline's YAML from `registry/facts.md` § Timeline data only; each event carries its row id (`F-07`) as its source.
  - Still-open dates are drawn as spans or left out, never as points: Chingkim "mid-1280s" (F-06), the fleet's sailing 1291–92 (F-15), Pipino "1310s" (F-18), Mosul only as "1261 (Yule)" (F-02).
  - B5 reception takes the print dates (F-21), the Leeu copy and postils (F-19), the Catalan Atlas 1375 with no Chipangu, and Fra Mauro 1459 (F-20); S-20 adds the later rows.
  - B6 "Book date vs history" rows: Baidu and Casan 1294 vs 1295 (F-05); Bayan 1268 vs 1274 (F-29); Alaü's victory vs Hulagu's rout (F-01).
  - A date not in the sheet gets a row there first (S-06 method), then goes on the timeline.
- **Done when:** every event in the B1–B6 YAML has a `facts.md` row id, and no still-open row is drawn as a point.
