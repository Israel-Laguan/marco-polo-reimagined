# MAP — Maps

**Status:** 17 maps placed · editorial read pending · **Plan doc:** `multimedia-plan.md` § A

## Scope
All geographic maps, generated as vectors from `gazetteer.csv`. City plans count as maps (A9 Dadu). Timelines and diagrams are in `DIA`.

## Backlog
| ID | Map | Placement | Notes from critique |
|---|---|---|---|
| A1 | Series overview (generated) | each F2 | Replaces the Wikimedia JPEG in the body; the CC BY-SA PNG appears as a facsimile in I-B1 |
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
| A13 | Fujian road + Zayton | II-14 | Tyunju = Dehua? inset; identification provisional |
| A14 | Mongol horizon | II-15 | Land of Darkness dotted |
| A15 | Invasions of Japan 1274/1281 | III-1 | — |
| A16 | Cocachin return | III-9, III-F2 | Solid western sequence from the Prologue; dashed reconstruction through the Indian Ocean; Abhar marked as embassy evidence |
| A17 | Polo's order vs the coast's order | III-5, III-6 | Strip map |
| A18 | Adriatic inset (Venice, Genoa, Curzola) | I-1 | Added in S-09 from the critique candidates |

- **Candidates without an ID yet** (proposed in the critique, not in the multimedia plan): I-1 Adriatic inset (Venice, Genoa, Curzola; Doria's raid); I-3 Acre ↔ Jerusalem ↔ Ayas, then a reconstructed route to Kemenfu. II-1 Nayan theatre (Cambaluc → Liao/Nonni plain). **S-09:** I-1 → A18; I-3 folded into A4; II-1 → an inset on A7.
- **Gazetteer (S-04 ✓, 2026-10-22):** the missing rows exist (Ucaca, Negropont, Sachiu, Chingintalas, Erguiul, Sinju, Egrigaia, Chagannor, Bargu, Abhar, …), so the gazetteer, S-08 and S-09 have cleared their gates. Rules for plotting: skip rows with blank coordinates (14: 12 `unfixed`, plus the `disputed` Bangala and Cuju; e.g. Arbre Sec, Dogana, Male and Female); draw `disputed` rows with a distinct marker and a caption naming the alternative (Caugigu, Nanghin, Anin, Tinju); region rows (Persia, Cathay, Manzi, …) are labels. Coordinates marked `probable` are county-seat precision, fine at book scale.

## Gated by spikes
S-04 ✓ (rows, names) · S-09 ✓ (pipeline, visual system, 2026-11-10) · S-08 ✓ (sizes, fonts)

## Tasks
S-09 closed 2026-11-10. Every task: write `tools/media/data/<A#>.yaml` (format in `tools/media/map.py`'s header; copy `A16.yaml`), give each route segment `stated | inferred | reported` with a comment saying why, run `map.py --test` then `map.py <A#>`, proof the PNG in `tools/media/.cache/`, then link the `.svg` from the chapter with a caption that names every disputed alternative. **Done when:** the asset is in `media/maps/` at 4.5 in (or 2.2 in) wide and no taller than 5.4 in, the chapter links it, and `--test` passes. A8 moved to DIA as C17 (its places are `unfixed`).

### MAP.T01 — A1 Series overview
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** each F2 · **Depends:** S-09 ✓
- **Delivered:** The same generated overview appears in each F2. I-F2 previously used the Wikimedia JPEG. The credited PNG appears in I-B1 as a facsimile.

### MAP.T02 — A2 The world in 1260
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-F1 · **Depends:** S-09 ✓; Political shapes for khanates, Mamluks, Byzantium are not in Natural Earth: hand-drawn polygons in YAML (new `areas:` key), sourced in comments
- **Do:** Equal Earth, 1:50m. Italian posts (Soldaia, Constantinople, Acre, Ayas) as markers.

### MAP.T03 — A3 The elder voyage
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-2 · **Depends:** S-09 ✓
- **Do:** Constantinople → Soldaia → Sarai → Bolghar → Ucaca → Bocara → Kublai → Ayas → Acre → Negropont → Venice; the Kublai leg to Chandu/Cambaluc is inferred.

### MAP.T04 — A4 Outbound: Acre and Ayas to Hormos
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-3, referenced in I-4 … I-8 · **Depends:** S-09 ✓
- **Do:** **Two variant lines**, both dashed (via Tauris; via Mausul/Baudas). Extended west to Acre and Jerusalem (critique candidate I-3, folded in S-09). Canosalmi is `unfixed`: text label only.

### MAP.T05 — A5 Balc to Pein
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-9, referenced in I-10 · **Depends:** S-09 ✓
- **Do:** Reported side-places dotted (Pashai, Keshimur, Samarcan, Bolor). Dogana is `unfixed`: text label. Pein is disputed (label *Pein?*).

### MAP.T06 — A6 Lop to Chandu
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-11, referenced in I-12 and I-13 · **Depends:** S-09 ✓
- **Do:** Off-route Camul, Caracoron, Bargu dotted. Chingintalas and Chagannor are `unfixed`: text labels, no markers.

### MAP.T07 — A7 Kublai's realm c. 1290
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-F2, referenced in II-1 · **Depends:** S-09 ✓
- **Do:** Dadu/Shangdu, the Grand Canal, the four circuits; **inset: the Nayan theatre** (II-1, critique candidate folded in S-09).

### MAP.T09 — A9 Dadu (Cambaluc) city plan
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-2 · **Depends:** S-09 ✓; S-17 best-effort intake ✓
- **Delivered:** Lambert city plan with eleven gates, using Fu Xinian’s published reconstruction in Funo 2017, fig. 24a, for relative geometry. The YAML documents approximate geographic registration. The surviving north earthwork, reconstructed enclosures, approximate Taiye lake and proposed bell tower are distinguished. The 2024 excavation report’s plates were not used.

### MAP.T10 — A10 The west road
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-6 · **Depends:** S-09 ✓
- **Do:** Cambaluc → Pulisanghin → … → Kenjanfu → Sindafu. Cachanfu ≠ Xi'an; Kenjanfu = Xi'an (II-M2). Caichu is `unfixed`: text label.

### MAP.T11 — A11 South-west circuit
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-7, referenced in II-8 and II-9 · **Depends:** S-09 ✓
- **Do:** Sindafu → Tebet → Carajan → Vochan → Mien; reported Bangala (no point: text label with a dotted arrow). Caugigu? is a disputed regional reference: attribute Yule's Kiang Hung reading and Pelliot's different Upper Red River interpretation in the caption. Anin and Coloman points also reflect one disputed regional interpretation, not confirmed sites; Cuiju? is a Guizhou regional hypothesis, not a proven Guiyang city identification. See S17-F4.

### MAP.T12 — A12 The canal spine
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-10, referenced in II-11 … II-13 · **Depends:** S-09 ✓
- **Do:** Juju → … → Yanju → Suju → Kinsay; Nanghin and Saianfu as dashed side branches; the two Vujus (`vuju-1`, `vuju-2`). **Inset: canal summit profile at Sinjumatu** (critique candidate folded in S-09).

### MAP.T13 — A13 The Fujian road and Zayton
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-14 · **Depends:** S-09 ✓
- **Do:** Kinsay → … → Fuju → Zayton; Tyunju (Dehua?) inset (a second, half-width map: `width: 2.2`). The inset presents Dehua and Tingzhou/Changting as competing references. Kiln evidence attests production without establishing the name. Cuju has no point: text label.

### MAP.T14 — A14 The Mongol horizon
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** II-15 · **Depends:** S-09 ✓; `areas:` as A2
- **Do:** Equal Earth. Ilkhanate, Chagatai and Kaidu, Golden Horde; the Land of Darkness dotted (not in the gazetteer: text label).

### MAP.T15 — A15 Invasions of Japan, 1274/1281
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** III-1 · **Depends:** S-09 ✓; historical campaign references and three new gazetteer rows ✓
- **Do:** Korean and Chinese fleets, both in the volume's indigo, told apart by labels; dates on the lines.

### MAP.T16 — A16 The Cocachin return
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** III-9, III-F2 · **Depends:** S-09 ✓
- **Delivered:** III-9 and III-F2 show the reconstructed stages and the two attributed departure estimates in F-15. Both A16 and A1 now use a dashed Chamba–Samara segment. Captions describe the named western sequence and its illustrative course, following the [text and media handoff](../../status/critique-text-media-handoff-2026-11-17.md).

### MAP.T17 — A17 Polo's order vs the coast's order
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** III-5, referenced in III-6 · **Depends:** S-09 ✓; `layout: strip` implemented in map.py
- **Do:** Numbers the Book's sequence along India's coasts so the crossings show.

### MAP.T18 — A18 Adriatic inset: Venice, Genoa, Curzola
- **Status:** generated, proofed and placed · editorial read pending · **Placement:** I-1 · **Depends:** S-09 ✓
- **Do:** New in S-09 (critique candidate). Half-width (`width: 2.2`), Lambert, 1:10m. Curzola is `reported_only` (Ramusio's setting, F-34); Doria's raid as a dashed line.


## Production closeout (2026-11-21)

- Generated 18 PDF/SVG pairs for 17 maps, counting the separate half-width A13 inset. All figures and shared chapter references are in the manuscript. A8 remains the C17 schematic.
- Regeneration reproduced all vector files byte for byte. Colour and greyscale proofs, the three print and HTML builds, the map and gazetteer checks, and 43 book tests passed. Manuscript lint cleared all five map-guide caption errors and added no errors against the working baseline.
- Sources and limits are recorded in the [media credits](../../../media/ATTRIBUTIONS.md), the captions and each YAML. A2, A7 and A14 show generalized political geography. A7 leaves the Nayan battlefield unpinned; A12 uses a qualitative profile with no period elevations. A9 uses a published plan with approximate registration, and A13 presents the porcelain identification as disputed.
- Editorial read remains pending for all MAP tasks.

## S-16 best-effort map handoff (2026-11-11)

- **A1 / A4 / A16:** Hormos? is an uncertain regional pin at modern Minab, not the archaeological site. The A1 and A16 pilots now use that label; when placing them, include the caption: “Hormos? marks the Minab area; the exact site of Old Hormuz is uncertain.” Draw the outbound Hormos detour as reconstructed; the return landfall is a separate claim.
- **A5:** Pein? plots the provisional Uzun-tatïr candidate and its caption names Keriya as an alternative. **A6:** Tenduc is a regional reference and Caracoron/Bargu are reported side-places; do not imply personal visits. **A4:** Tonocain's Qaen reference is not a provincial boundary, and the Dry Tree has no plotted point.
- Full source and uncertainty decisions: [S-16 closeout](../../research/results/S-16-closeout.md). These cautions do not block map production.
