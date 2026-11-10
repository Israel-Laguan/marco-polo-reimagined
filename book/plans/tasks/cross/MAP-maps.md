# MAP — Maps

**Status:** backlog · **Plan doc:** `multimedia-plan.md` § A

## Scope
All geographic maps, generated as vectors from `gazetteer.csv`. City plans count as maps (A9 Dadu). Timelines and diagrams are in `DIA`.

## Backlog
| ID | Map | Placement | Notes from critique |
|---|---|---|---|
| A1 | Series overview (generated) | each F2 | Replaces Wikimedia overview in body; keep PD overview as a facsimile |
| A2 | The world in 1260 | I-F1 | Khanates, Mamluks, Byzantium, Italian posts |
| A3 | The elder voyage | I-2 | Needs Ucaca, Negropont rows |
| A4 | Outbound Ayas → Hormos (two variant lines) | I-4 … I-8 | front-02 and ch-03 disagree on the route (I-m1); show both as reconstructions |
| A5 | Balc → Pein | I-9, I-10 | Reported places dotted |
| A6 | Lop → Chandu | I-11 … I-13 | Needs Sachiu, Chingintalas, Erguiul, Sinju, Egrigaia, Chagannor, Bargu |
| A7 | Kublai's realm c. 1290 | II-F2 | Replaces 556 px `map-china-yuan` |
| ~~A8~~ | Seasonal orbit Dadu ↔ Shangdu ↔ Cachar Modun | II-4 / I-13 | **Moved to DIA as C17** (S-09): Cachar Modun is `unfixed` |
| A9 | Dadu city plan | II-2 | 11 gates (II-2 Note [17] gate dispute); replaces `map-cambaluc.jpg` |
| A10 | West road | II-6 | Cachanfu ≠ Xi'an; Kenjanfu = Xi'an (II-M2) |
| A11 | South-west circuit | II-7 … II-9 | Caugigu ID conflict (Tonkin vs Kiang Hung) |
| A12 | Canal spine | II-10 … II-13 | Nanghin, Saianfu dashed; two Vujus |
| A13 | Fujian road + Zayton | II-14 | Tyunju = Dehua inset |
| A14 | Mongol horizon | II-15 | Land of Darkness dotted |
| A15 | Invasions of Japan 1274/1281 | III-1 | — |
| A16 | Cocachin return | III-9, III-F2 | Solid = Prologue-named; dashed = inferred; needs Abhar, Negropont |
| A17 | Polo's order vs the coast's order | III-5, III-6 | Strip map |
| A18 | Adriatic inset (Venice, Genoa, Curzola) | I-1 | Added in S-09 from the critique candidates |

- **Candidates without an ID yet** (proposed in the critique, not in the multimedia plan): I-1 Adriatic inset (Venice, Genoa, Curzola; Doria's raid); I-3 Acre ↔ Jerusalem ↔ Ayas, then a reconstructed route to Kemenfu. II-1 Nayan theatre (Cambaluc → Liao/Nonni plain). **S-09:** I-1 → A18; I-3 folded into A4; II-1 → an inset on A7.
- **Gazetteer (S-04 ✓, 2026-10-22):** the missing rows exist (Ucaca, Negropont, Sachiu, Chingintalas, Erguiul, Sinju, Egrigaia, Chagannor, Bargu, Abhar, …), so the gazetteer no longer blocks maps; S-09 and S-08 still do. Rules for plotting: skip rows with blank coordinates (14: 12 `unfixed`, plus the `disputed` Bangala and Cuju; e.g. Arbre Sec, Dogana, Male and Female); draw `disputed` rows with a distinct marker and a caption naming the alternative (Caugigu, Nanghin, Anin, Tinju); region rows (Persia, Cathay, Manzi, …) are labels. Coordinates marked `probable` are county-seat precision, fine at book scale.

## Gated by spikes
S-04 ✓ (rows, names) · S-09 ✓ (pipeline, visual system, 2026-11-10) · S-08 (sizes, fonts)

## Tasks
S-09 closed 2026-11-10. Every task: write `tools/media/data/<A#>.yaml` (format in `tools/media/map.py`'s header; copy `A16.yaml`), give each route segment `stated | inferred | reported` with a comment saying why, run `map.py --test` then `map.py <A#>`, proof the PNG in `tools/media/.cache/`, then link the `.svg` from the chapter with a caption that names every disputed alternative. **Done when:** the asset is in `media/maps/` at 4.5 in (or 2.2 in) wide and no taller than 5.4 in, the chapter links it, and `--test` passes. A8 moved to DIA as C17 (its places are `unfixed`).

### MAP.T01 — A1 Series overview
- **Status:** asset **done** (S-09 pilot); placement open · **Placement:** each F2 · **Depends:** S-09 ✓
- **Do:** Placed in each volume's front-02 replacing `map-marco-polo-overview.png` in the body (keep that as a facsimile); caption: the whole round trip, by volume.

### MAP.T02 — A2 The world in 1260
- **Status:** backlog · **Placement:** I-F1 · **Depends:** S-09 ✓; Political shapes for khanates, Mamluks, Byzantium are not in Natural Earth: hand-drawn polygons in YAML (new `areas:` key), sourced in comments
- **Do:** Equal Earth, 1:50m. Italian posts (Soldaia, Constantinople, Acre, Ayas) as markers.

### MAP.T03 — A3 The elder voyage
- **Status:** backlog · **Placement:** I-2 · **Depends:** S-09 ✓
- **Do:** Constantinople → Soldaia → Sarai → Bolghar → Ucaca → Bocara → Kublai → Ayas → Acre → Negropont → Venice; the Kublai leg to Chandu/Cambaluc is inferred.

### MAP.T04 — A4 Outbound: Acre and Ayas to Hormos
- **Status:** backlog · **Placement:** I-3 … I-8 · **Depends:** S-09 ✓
- **Do:** **Two variant lines**, both dashed (via Tauris; via Mausul/Baudas). Extended west to Acre and Jerusalem (critique candidate I-3, folded in S-09). Canosalmi is `unfixed`: text label only.

### MAP.T05 — A5 Balc to Pein
- **Status:** backlog · **Placement:** I-9, I-10 · **Depends:** S-09 ✓
- **Do:** Reported side-places dotted (Pashai, Keshimur, Samarcan, Bolor). Dogana is `unfixed`: text label. Pein is disputed (label *Pein?*).

### MAP.T06 — A6 Lop to Chandu
- **Status:** backlog · **Placement:** I-11 … I-13 · **Depends:** S-09 ✓
- **Do:** Off-route Camul, Caracoron, Bargu dotted. Chingintalas and Chagannor are `unfixed`: text labels, no markers.

### MAP.T07 — A7 Kublai's realm c. 1290
- **Status:** backlog · **Placement:** II-F2 · **Depends:** S-09 ✓; Province shapes as `areas:` (as A2)
- **Do:** Dadu/Shangdu, the Grand Canal, the four circuits; **inset: the Nayan theatre** (II-1, critique candidate folded in S-09).

### MAP.T09 — A9 Dadu (Cambaluc) city plan
- **Status:** backlog · **Placement:** II-2 · **Depends:** S-09 ✓; Wall and gate coordinates from a cited plan (S-17), not from Natural Earth
- **Do:** Lambert, no graticule; 11 gates (II-2 Note [17] gate dispute), palace city, Taiye lake, bell tower. Replaces `map-cambaluc.jpg`.

### MAP.T10 — A10 The west road
- **Status:** backlog · **Placement:** II-6 · **Depends:** S-09 ✓
- **Do:** Cambaluc → Pulisanghin → … → Kenjanfu → Sindafu. Cachanfu ≠ Xi'an; Kenjanfu = Xi'an (II-M2). Caichu is `unfixed`: text label.

### MAP.T11 — A11 South-west circuit
- **Status:** backlog · **Placement:** II-7 … II-9 · **Depends:** S-09 ✓
- **Do:** Sindafu → Tebet → Carajan → Vochan → Mien; reported Bangala (no point: text label with a dotted arrow), Caugigu? (caption: Tonkin vs Kiang Hung), Cuiju?.

### MAP.T12 — A12 The canal spine
- **Status:** backlog · **Placement:** II-10 … II-13 · **Depends:** S-09 ✓
- **Do:** Juju → … → Yanju → Suju → Kinsay; Nanghin and Saianfu as dashed side branches; the two Vujus (`vuju-1`, `vuju-2`). **Inset: canal summit profile at Sinjumatu** (critique candidate folded in S-09).

### MAP.T13 — A13 The Fujian road and Zayton
- **Status:** backlog · **Placement:** II-14 · **Depends:** S-09 ✓
- **Do:** Kinsay → … → Fuju → Zayton; Tyunju (Dehua) inset (a second, half-width map: `width: 2.2`). Cuju has no point: text label.

### MAP.T14 — A14 The Mongol horizon
- **Status:** backlog · **Placement:** II-15 · **Depends:** S-09 ✓; `areas:` as A2
- **Do:** Equal Earth. Ilkhanate, Chagatai and Kaidu, Golden Horde; the Land of Darkness dotted (not in the gazetteer: text label).

### MAP.T15 — A15 Invasions of Japan, 1274/1281
- **Status:** backlog · **Placement:** III-1 · **Depends:** S-09 ✓; Fleet routes and landing places need gazetteer rows (Hakata Bay, Takashima, Happo/Masan)
- **Do:** Korean and Chinese fleets, both in the volume's indigo, told apart by labels; dates on the lines.

### MAP.T16 — A16 The Cocachin return
- **Status:** asset **done** (S-09 pilot); placement open · **Placement:** III-9, III-F2 · **Depends:** S-09 ✓
- **Do:** Placed in III-9 and III-front-02 (replacing the dropped `map-indian-ocean.jpg` and `map-return-route.jpg`); caption gives the 1291/1292 debate (F-15) and says which stages are inferred.

### MAP.T17 — A17 Polo's order vs the coast's order
- **Status:** backlog · **Placement:** III-5, III-6 · **Depends:** S-09 ✓; A strip-map layout (one coastline unrolled): a new `layout: strip` mode in map.py, or a TikZ schematic if that is simpler
- **Do:** Numbers the Book's sequence along India's coasts so the crossings show.

### MAP.T18 — A18 Adriatic inset: Venice, Genoa, Curzola
- **Status:** backlog · **Placement:** I-1 · **Depends:** S-09 ✓
- **Do:** New in S-09 (critique candidate). Half-width (`width: 2.2`), Lambert, 1:10m. Curzola is `reported_only` (Ramusio's setting, F-34); Doria's raid as a dashed line.

