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
| A8 | Seasonal orbit Dadu ↔ Shangdu ↔ Cachar Modun | II-4 / I-13 | Month labels; 28 Aug libation |
| A9 | Dadu city plan | II-2 | 11 gates (II-2 Note [17] gate dispute); replaces `map-cambaluc.jpg` |
| A10 | West road | II-6 | Cachanfu ≠ Xi'an; Kenjanfu = Xi'an (II-M2) |
| A11 | South-west circuit | II-7 … II-9 | Caugigu ID conflict (Tonkin vs Kiang Hung) |
| A12 | Canal spine | II-10 … II-13 | Nanghin, Saianfu dashed; two Vujus |
| A13 | Fujian road + Zayton | II-14 | Tyunju = Dehua inset |
| A14 | Mongol horizon | II-15 | Land of Darkness dotted |
| A15 | Invasions of Japan 1274/1281 | III-1 | — |
| A16 | Cocachin return | III-9, III-F2 | Solid = Prologue-named; dashed = inferred; needs Abhar, Negropont |
| A17 | Polo's order vs the coast's order | III-5, III-6 | Strip map |

- **Candidates without an ID yet** (proposed in the critique, not in the multimedia plan): I-1 Adriatic inset (Venice, Genoa, Curzola; Doria's raid); I-3 Acre ↔ Jerusalem ↔ Ayas, then a reconstructed route to Kemenfu. II-1 Nayan theatre (Cambaluc → Liao/Nonni plain). Decide in S-09 whether to add them or fold them into existing maps.
- **Gazetteer (S-04 ✓, 2026-10-22):** the missing rows exist (Ucaca, Negropont, Sachiu, Chingintalas, Erguiul, Sinju, Egrigaia, Chagannor, Bargu, Abhar, …), so the gazetteer no longer blocks maps; S-09 and S-08 still do. Rules for plotting: skip rows with blank coordinates (14: 12 `unfixed`, plus the `disputed` Bangala and Cuju; e.g. Arbre Sec, Dogana, Male and Female); draw `disputed` rows with a distinct marker and a caption naming the alternative (Caugigu, Nanghin, Anin, Tinju); region rows (Persia, Cathay, Manzi, …) are labels. Coordinates marked `probable` are county-seat precision, fine at book scale.

## Gated by spikes
S-04 (rows, names) · S-09 (pipeline, visual system) · S-08 (sizes, fonts)

## Tasks
_After S-04 and S-09: one task per map, `MAP.T01` … `MAP.T17`._
