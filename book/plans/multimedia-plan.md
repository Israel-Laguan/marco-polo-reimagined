# Multimedia Plan — *The Book of the Million*

**Status:** complete, 2026-11-25 · **Editions:** Markdown source, LuaLaTeX print, HTML and EPUB. The assets are static. Pronunciation guidance appears in each volume’s glossary.

## Principles

1. **Generated from source, not drawn by hand.** Maps come from `gazetteer.csv`; timelines and charts come from small data files. When a fact changes, regenerate.
2. **Vector for print.** Maps, diagrams, timelines and charts go to PDF (LaTeX) and SVG/PNG (Markdown preview) from the same script.
3. **One visual system.** One map palette, one typeface (the book's body font), the same legend conventions everywhere (fixed in § Visual system):
   - **solid line** = route the Book states;
   - **dashed** = reconstructed or inferred;
   - **dotted** = reported only, not travelled;
   - place markers coloured by gazetteer `reliability`.
4. **Print resolution.** Raster ≥ 300 dpi at final size.
5. **Drawn at final size.** Maps and timelines are generated at the 4.5 in measure, so LaTeX places them at 100 % and their type matches the page; never scale a generated asset up or down.

## Visual system (S-09 ✓)

One file holds it: `tools/media/style.yaml`, shared by the map, timeline, diagram and chart generators. Change a value there and regenerate; never restyle an asset by hand.

| Element | Rule |
|---|---|
| Typeface | **Noto Serif**, the body face (`tools/build/book.latex`). Map labels 6 pt; region names 5.4 pt capitals in soft ink; seas 6 pt italic; legend 5.6 pt. Timelines use the page sizes (`\footnotesize` labels, `\scriptsize` italic notes). |
| Palette | Land parchment `#F1EBDD`, sea `#E3ECEF`, coast `#8C8A84` (0.25 pt), rivers `#9FBACB` (major only, Natural Earth `scalerank ≤ 3`). Ink `#2B2A28`, soft ink `#6E6B66`. |
| Volume colours | Route lines and accents: **I** madder `#A8432B` (the road), **II** ochre `#B7871F` (Cathay and Manzi), **III** indigo `#1F5A85` (the seas). A leg map uses its volume's colour; A1 uses all three. |
| Line semantics | **solid** = the Book states it; **dashed** = reconstructed or inferred; **dotted** = reported only, not travelled. 1.1 pt. Every route segment in a map's YAML names one of the three, with a comment saying why. |
| Place markers | A grey ramp by gazetteer `reliability`, so markers never compete with route colours and survive greyscale: visited = black, probably visited = grey, reported only = white with black ring, uncertain = white with grey ring. `legendary` and `unfixed` rows are never plotted (map.py refuses them). Approximate regional reference pins carry an explicit area label and caption; **Hormos? (Minab area)** uses Minab as a proxy, not the archaeological site. |
| Disputed places | `id_confidence = disputed` adds **?** to the label (*Pein?*); the caption names the alternative. |
| Base map | Natural Earth (public domain) land, lakes, rivers: 1:50m for overviews (A1, A2, A16), 1:10m for regional maps and A3. **No modern borders**: they are anachronistic on a 13th-century route; regions are labels. |
| Projection | Equal Earth for spans over ~60° of longitude (straight parallels, honest edge labels); Lambert conformal conic for regional maps and the Dadu plan. |
| Furniture | 10° graticule (5° on regional maps) labelled left and bottom; a scale bar measured along the geodesic at a stated point; legend in available space, listing the line styles and markers where needed. |
| Timelines | Vertical (years run down), one axis, breaks shown as a double slash; event kinds by marker shape: manuscript ● ink, print ■ indigo, map ◆ ochre, journey ▲ madder. Spans (Pipino's "1310s", the 1291–92 sailing) are bars, never points. Every event carries its `facts.md` row id. |
| Files | `media/maps/` and `media/timelines/`, each asset as `.pdf` + `.svg`. Markdown links the `.svg`; the LaTeX filter (`book.lua`) swaps in the `.pdf`. SVG text is outlined, so the preview needs no fonts. Unchanged map sources regenerate byte-identically. |

## Existing media triage

The 14 surviving files are archived in `media/legacy/`. The three front-02 sections use the edition maps. See the [media credits](../media/ATTRIBUTIONS.md) for sources and reuse terms.

| File | Size | Disposition |
|---|---|---|
| `map-marco-polo-overview.png` | 3654×3312 | Earlier round-trip map reproduced as a facsimile in I-B1. |
| `map-marco-polo-overview.jpg` | 1355×692 | Chumwa’s round-trip map, archived after A1 took over the front-matter placement. |
| `map-marco-polo-shepherd.jpg` | 1726×1403 | Chumwa’s route overlay on Shepherd’s 1911 map, archived for reference. |
| `map-asia-mongol-empire.png`, `map-mongol-empire.gif` | 752×591 | 1294 still and animated master, superseded by A2 and A14. |
| `map-china-yuan.png` | 556×537 | Yuan map superseded by A7. The two duplicate copies were removed. |
| `map-cambaluc.jpg` | 591×780 | Dadu plan superseded by A9, which shows the 11 gates for the II-2 gate dispute. |
| `map-caugigu.jpg` | 747×1200 | Yule’s Itinerary No. V facsimile, archived for reference. A11 covers the southwest circuit. |
| `map-indian-ocean.jpg` | 1280×720 | Retired generated illustration. It places Hormuz at Aden. A16 covers the embassy return. |
| `map-hangzhou-kinsay.jpg` | 1280×720 | Retired generated illustration of the West Lake. A7 covers the regional geography and plate II-13 depicts the lake. |
| `map-return-route.jpg` | — | Removed as a byte-identical copy of Chumwa’s overview JPEG. |
| `drawing-*.jpg` (4) | 1280×720 | Retired generated illustrations. Period errors include the Salute domes, a Renaissance villa at Shangdu and Rustichello in a monk’s habit. |

## A. Maps (17 maps, 18 PDF/SVG pairs)

The [map ledger](tasks/cross/MAP-maps.md) records placements and sources. The maps use the S-04 gazetteer, with disputed and approximate identifications distinguished. Unfixed places may appear as unpinned text.

| # | Map | Placement | Content |
|---|---|---|---|
| A1 | Series overview (generated, replaces the Wikimedia one in the book body) | Each volume's front-02 | Whole journey, three volume legs colour-coded |
| A2 | The world in 1260 | I-front-01 | Mongol successor khanates, Mamluks, Byzantium, Venetian and Genoese trading posts |
| A3 | The elder voyage | I-2 | Constantinople → Soldaia → Sarai → Bolghar → Ucaca → Bocara → Kublai → Ayas → Acre → Negropont → Venice |
| A4 | Outbound: Acre and Ayas to Hormos | I-3, referenced in I-4 through I-8 | The Jerusalem errand and two dashed reconstructions east of Ayas, via Tauris or via Mausul and Baudas. The Hormos detour is conjectural. |
| A5 | Balc to Pein | I-9, referenced in I-10 | Reported side-places dotted (Pashai, Keshimur, Samarcand, Bolor); Pein? follows the disputed Uzun-tatïr point, with Keriya as alternative in caption. |
| A6 | Lop to Chandu | I-11, referenced in I-12 and I-13 | Dotted routes to reported side-places. Chingintalas and Chagannor are unfixed. |
| A7 | Kublai's realm c. 1290 | II-front-02, referenced in II-1 | Approximate cores of Yuan administrative zones, Dadu and Shangdu, the Grand Canal, four circuits, and a regional inset for Nayan’s revolt. |
| A8 | Seasonal orbit | See C17 | Delivered as a schematic because Cachar Modun and Chagannor are unfixed. |
| A9 | Dadu (Cambaluc) city plan | II-2 | Walls, 11 gates, palace city, Taiye lake, bell tower |
| A10 | The west road | II-6 | Cambaluc → Pulisanghin → … → Kenjanfu → Sindafu |
| A11 | South-west circuit | II-7, referenced in II-8 and II-9 | Reconstructed onward route to Vochan with dotted reports for Mien, Bangala and the southwestern side circuit. |
| A12 | The canal spine | II-10, referenced in II-11 through II-13 | Canal corridor, dashed side branches to Nanghin and Saianfu, and a qualitative watershed inset at Sinjumatu. |
| A13 | The Fujian road and Zayton | II-14 | Kinsay through Fuju to Zayton. A separate half-width Tyunju inset shows Dehua and the Tingzhou or Changting alternative. |
| A14 | The Mongol horizon | II-15 | Ilkhanate, Chagatai and Kaidu, Golden Horde, the "Land of Darkness" (dotted) |
| A15 | Invasions of Japan, 1274/1281 | III-1 | Korean and Chinese fleets, Hakata Bay, Takashima |
| A16 | **The Cocachin return** | III-9 + III-front-02 | A reconstructed route with the Prologue's “Java” and named western sequence distinguished from inferred identifications and stops. The Samara identification and the application of the five-month wait to the embassy follow an editorial reconstruction. Abhar marks the marriage attested by Rashid al-Din. See the [text and media handoff](status/critique-text-media-handoff-2026-11-17.md). |
| A17 | Polo’s order vs the coast’s order | III-5, referenced in III-6 | Strip map comparing the Book’s sequence with geographic order around Cape Comorin. |
| A18 | Adriatic inset | I-1 | Venice, Genoa and Curzola, with the reconstructed approach of Doria’s fleet. |

**Map caption rule (S-16):** On every map showing Hormos, say “Hormos? marks the Minab area; the exact site of Old Hormuz is uncertain.” The point is modern Minab, not a measured ruin. A1, A4 and A16 carry the same warning. A6 treats Caracoron and Bargu as reported side-places, not personal visits. Tonocain and Tenduc are regional references; do not imply precise boundaries.

## B. Timelines (6) — data YAML → TikZ (native LaTeX, same fonts)

| # | Timeline | Placement |
|---|---|---|
| B1 | The Polo family, c. 1254–1366 | I-front-01 |
| B2 | Mongol politics, 1203–1295 | I-front-01 |
| B3 | Kublai's reign and the Polo calendar (1260 → 1294) | II-front-01 |
| B4 | The Song endgame, 1268–1279 | II-10, referenced in II-11 |
| B5 | Reception, 1298–2024 (manuscripts, print, maps and later responses), based on the [S-20 selection](research/results/S-20-closure.md) | III-11, with references in III-10 and III-B1 |
| B6 | **Book date vs history** (a table-timeline, e.g. Baudas 1255 vs 1258; Chinghis 1187 vs 1206) | I-back-01 |

## C. Explanatory diagrams and charts (17)

**Schematic diagrams** (TikZ):

| # | Diagram | Ch. |
|---|---|---|
| C1 | Paper money: bark → sheet → seals → vermilion → circulation (with the 1287 revaluation sidebar) | II-5 |
| C2 | The *yam*: stations, runner forts, express riders; "ten days in one" attributed to the Book | II-5 |
| C3 | Keshig rota (Polo's 4 × 3,000 vs Palladius's 400) | II-3 |
| C4 | Mongol decimal army (*arban → tümen* vs the Book's terms) | I-12 |
| C5 | Paiza: the Book’s ranks alongside the *Yuan shi*, with a surviving relay tablet for comparison | II-1, referenced in I-2 |
| C6 | Tutia furnace process | I-8 |
| C7 | Zayton cost stack (duty + freight = "half the investment") | II-14 |
| C8 | Ilkhan succession: the Book vs the record | II-15 |
| C17 | Seasonal orbit (was map A8): Dadu ↔ Shangdu ↔ Cachar Modun as a ring of months, with the 28 August libation | II-4, referenced in I-13 |

**Data charts** (Python):

| # | Chart | Ch. |
|---|---|---|
| C9 | Gold : silver ratio gradient (1:8 → 1:5 across Yunnan and Burma) | II-8, referenced in II-7 |
| C10 | Pole Star altitude: the Book's cubits vs real latitude | III-6, referenced in III-3 |
| C11 | South China Sea and Indian Ocean wind seasons (S18-F4), with a Cocachin calendar strip showing the two departure readings (F-15) | III-F1, III-9, with references in III-1, III-3, III-5 and III-7 |

**Cutaways and sections** (TikZ labels over illustrated bases for C12, C13, C14 and C16. C15 is drawn entirely in TikZ.)

| # | Cutaway | Ch. |
|---|---|---|
| C12 | Seagoing junk: Ramusio’s compartment count and the Quanzhou wreck’s bulkheads, limber holes and rudder-stock socket | III-1 (preview in II-14) |
| C13 | Conjectural sewn-plank ship of Hormos, with horses above hide-covered cargo in Polo’s account | I-7 |
| C14 | Traction vs counterweight trebuchet | II-11 |
| C15 | Qanat cross-section | I-8 |
| C16 | Cane palace roof (split bamboo tiles) | I-13 |

**C13 source check (S22-E2).** Reused timbers from al-Balīd provide regional evidence for sewn construction. The hide cover and horse transport follow Polo’s account. The hull shape and steering arrangement are conjectural. See the [research ledger](registry/enrichment.md#s-22-supplement--cross-project-candidates-2026-11-13).

## D. Comparison tables (14 topics)

The manuscript uses Markdown tables rendered with LaTeX `booktabs`. The [table ledger](tasks/cross/TBL-tables.md) records the chapter placements and evidence limits.

| Ch. | Table |
|---|---|
| I-1 | Who captured Marco, and where? Witness F, Jacopo d’Acqui, Pipino, Ramusio and Yule–Cordier |
| I-3 | The four scripts |
| I-5 | How the Caliph died: Polo / Hayton / Rashid / Ibn al-Furat |
| I-6 | Eight kingdoms of Persia, with identification and confidence |
| I-12 | Kaan succession: the Book vs the record |
| I-7 / I-9 / I-11 | Geographic text vs Ramusio, side by side (turns the Ramusio problem into a reader feature) |
| II-1 | Nayan |
| II-5 | Ahmad's murder: Polo vs *Yuan shi* (incl. Bolad) |
| II-8 | Mien battle numbers |
| II-11 | Saianfu, and the Yanju manuscript variants |
| II-13 | Kinsay numbers: Polo, Odoric, Ibn Baṭṭūṭa, Waṣṣāf and the figures reported by Mascherpa |
| III-1 | Japan 1274/1281: Polo vs Japanese and Yuan sources |
| III-9, summarized in the III-12 ledger | **Cocachin in three sources** (Prologue / Rashid / *Yongle dadian* 1941) |
| III-12 | **Hits, misses and silences ledger** (cross-volume, with markers) |

## E. Print substitutes for the audio ideas

- Each volume closes with a glossary of Book forms, modern forms where applicable, short glosses and pronunciation hints for unfamiliar names. See the [glossary ledger](tasks/cross/GLO-glossary.md).
- I-1 places the Franco-Italian opening from witness F beside Yule’s English in a parallel-text box. Both excerpts identify their editions.

## Toolchain (S-08 and S-09)

| Need | Tool |
|---|---|
| Markdown → LaTeX | **pandoc** 3.1 + `tools/build/book.lua` (S-08): swaps `x.svg`/`x.png` → `x.pdf` when the PDF sits beside it; places figures at natural size, shrunk only to fit; checks each raster's real type and width (≥ 1,350 px at full width) and prints a placeholder box for a file it cannot place. Build: `tools/build/build.sh`; authoring shapes: `registry/markdown-conventions.md` |
| HTML and EPUB | Pandoc, citeproc and `tools/build/preview.lua`. The EPUB filter puts figure anchors on their enclosing blocks so links work across split chapters. |
| Typesetting | **LuaLaTeX** (TeX Live 2024) + biber/`biblatex-chicago`; 6×9 in trim, 4.5×7.2 in text block; Noto Serif, DejaVu Sans for the markers, Noto Serif CJK for Chinese (S-08); `booktabs`, `tikz`, `pgfplots` |
| Maps / charts | Python **matplotlib + cartopy** in a local venv (`tools/media/requirements.txt`, pinned) + Natural Earth 1:50m / 1:10m, downloaded on first run to `tools/media/.cache/` |
| Timelines / diagrams | TikZ standalone (LuaLaTeX) → PDF; `pdftocairo -svg` → SVG for Markdown preview (no `dvisvgm` needed) |

Layout:

```
book/media/
  maps/        A*.pdf|svg   (generated)
  timelines/   B*.pdf|svg   (generated)
  diagrams/    C*.pdf|svg   (generated)
  plates/      <vol>-<ch>-<slug>.png + .yaml   (see illustration plan)
  public-domain/  real artworks + license notes (S-11)
  references/  period references for GEN plates, not printed (S-11)
  legacy/      current files kept for reference
book/tools/media/   style.yaml, map.py, timeline.py + timeline.tex, diagram.py, charts.py
                    data/A*.yaml (maps), data/B*.yaml (timelines), diagrams/C*.tex (TikZ)
```

## Evidence limits in the delivered edition

- C1 identifies the 1287 rate as official and shows both issues in circulation. Guan and Yule support the rate in the [fact registry](registry/facts.md#schematic-data-for-dia-c1c17).
- C2 attributes postal distances and speeds to the Book. C5 identifies the museum object as a surviving relay tablet and distinguishes the script decree from evidence about individual tablets.
- A9 identifies Fu Xinian’s Dadu plan as a reconstruction and marks eleven gates. The lake outline and bell tower location are approximate. II-13 attributes city measurements and bridge counts to their individual witnesses.

## Completion checks (2026-11-25)

- Reviewed all 21 printed map placements against their captions and source data. The 41 PDF/SVG pairs occupy 46 placements across the three volumes and fit the 4.5 × 5.4 in figure measure.
- Built each volume as PDF, HTML and EPUB. Verified the figure placements and links, the 17 tables covering § D, the three glossaries and the parallel-text Prologue. All embedded print rasters measured at least 322 ppi. The print builds reported zero placeholders, undersized rasters, unresolved citations or line overruns of 10 pt or more.
- All 52 manuscript files passed lint, and all 52 automated tests passed, including the EPUB cross-chapter figure link regression test. The media generator self-tests, gazetteer validation and glossary check also passed.
