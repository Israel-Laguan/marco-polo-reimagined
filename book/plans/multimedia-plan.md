# Multimedia Plan — *The Book of the Million*

**Status:** draft v1 (2026-10-21) · **Target:** Markdown now, **LaTeX (print) final**. Everything is static. The audio ideas from the critique become a printed pronunciation glossary.

## Principles

1. **Generated from source, not drawn by hand.** Maps come from `gazetteer.csv`; timelines and charts come from small data files. When a fact changes, regenerate.
2. **Vector for print.** Maps, diagrams, timelines and charts go to PDF (LaTeX) and SVG/PNG (Markdown preview) from the same script.
3. **One visual system.** One map palette, one typeface (matching the book's body font), the same legend conventions everywhere:
   - **solid line** = route the Book states;
   - **dashed** = reconstructed or inferred;
   - **dotted** = reported only, not travelled;
   - place markers coloured by gazetteer `reliability`.
4. **Print resolution.** Raster ≥ 300 dpi at final size. Nothing currently in `media/` passes except `map-marco-polo-overview.png`.

## Existing media triage

| File | Size | Verdict |
|---|---|---|
| `map-marco-polo-overview.png` | 3654×3312 | **Keep.** Series overview. Re-caption as the *whole round trip*. |
| `map-marco-polo-shepherd.jpg` | 1726×1403 | Keep as a historical-cartography curiosity (Shepherd 1911 base). Half page at most. |
| `map-asia-mongol-empire.*`, `map-mongol-empire.gif` | 752×591 | **Replace** with a generated political map. Too small; date range unverified. |
| `map-china-yuan.*`, `map-yuan-1294.png` | 556×537 | **Replace** with a generated map. Too small; three copies of one file. |
| `map-cambaluc.jpg` | 591×780 | **Replace** with a redrawn Dadu plan (shows the 11 gates for the II-2 gate dispute). |
| `map-caugigu.jpg` | 747×1200 | Keep as a facsimile (Yule's Itinerary No. V) at small size; superseded by the SW-circuit map. |
| `map-indian-ocean.*` | 1280×720 | **Drop.** It is a generated image, geographically wrong (Hormuz at Aden), and mis-credited as Wikimedia. |
| `map-hangzhou-kinsay.*` | 1280×720 | **Drop.** It is the West Lake drawing, mislabelled as a map and as Wikimedia. |
| `map-return-route.jpg` | — | **Drop.** Byte-identical stand-in for the overview. |
| `drawing-*.png` (6) | 1280×720 | **Retire.** Wrong style for the new plan, too small, and three have period errors (17th-c. Salute domes, a Renaissance villa at Shangdu, Rustichello in a monk's habit). |

Existing captions in front-02 (all volumes) must be corrected now, whatever happens to the files.

## A. Maps (17) — Python + Natural Earth (public domain) → PDF/SVG

**Prerequisite:** the gazetteer fix (content plan W5) — **satisfied by S-04 (2026-10-22)**: Yule-form names and the missing rows are in `gazetteer.csv`. Plot only rows with coordinates (`id_confidence` ≠ `unfixed`); style disputed and approximate rows distinctly (S-09).

| # | Map | Placement | Content |
|---|---|---|---|
| A1 | Series overview (generated, replaces the Wikimedia one in the book body) | Each volume's front-02 | Whole journey, three volume legs colour-coded |
| A2 | The world in 1260 | I-front-01 | Mongol successor khanates, Mamluks, Byzantium, Venetian and Genoese trading posts |
| A3 | The elder voyage | I-2 | Constantinople → Soldaia → Sarai → Bolghar → Ucaca → Bocara → Kublai → Ayas → Acre → Negropont → Venice |
| A4 | Outbound: Ayas to Hormos | I-4 – I-8 | **Two variant lines** (via Tauris, or via Mausul/Baudas), both dashed: the route is a reconstruction |
| A5 | Balc to Pein | I-9 – I-10 | Reported side-places dotted (Pashai, Keshimur, Samarcand, Bolor) |
| A6 | Lop to Chandu | I-11 – I-13 | Off-route: Camul, Chingintalas, Caracoron, Bargu |
| A7 | Kublai's realm c. 1290 | II-front-02 | Yuan provinces, Dadu/Shangdu, the Grand Canal, the four circuits |
| A8 | Seasonal orbit | II-4 / I-13 | Dadu ↔ Shangdu ↔ Cachar Modun, with month labels and the 28 August libation |
| A9 | Dadu (Cambaluc) city plan | II-2 | Walls, 11 gates, palace city, Taiye lake, bell tower |
| A10 | The west road | II-6 | Cambaluc → Pulisanghin → … → Kenjanfu → Sindafu |
| A11 | South-west circuit | II-7 – II-9 | Sindafu → Tebet → Carajan → Vochan → Mien; reported: Bangala, Caugigu, Cuiju |
| A12 | The canal spine | II-10 – II-13 | Juju → … → Yanju → Suju → Kinsay; Nanghin and Saianfu as dashed side branches |
| A13 | The Fujian road and Zayton | II-14 | Kinsay → … → Fuju → Zayton; Tyunju (Dehua) inset |
| A14 | The Mongol horizon | II-15 | Ilkhanate, Chagatai and Kaidu, Golden Horde, the "Land of Darkness" (dotted) |
| A15 | Invasions of Japan, 1274/1281 | III-1 | Korean and Chinese fleets, Hakata Bay, Takashima |
| A16 | **The Cocachin return** | III-9 + III-front-02 | Zayton → Sumatra (5-month wait) → Seilan → Maabar → Malabar → Hormos → Abhar → Tauris → Trebizond → Venice. Solid for Prologue-named stages, dashed for inferred ones; monsoon season labels |
| A17 | Polo's order vs the coast's order | III-5 / III-6 | Strip map of India's coasts showing where the Book's sequence crosses itself |

## B. Timelines (6) — data YAML → TikZ (native LaTeX, same fonts)

| # | Timeline | Placement |
|---|---|---|
| B1 | The Polo family, 1254–1324 | I-front-01 |
| B2 | Mongol politics, 1206–1295 | I-front-01 |
| B3 | Kublai's reign and the Polo calendar (1260 → 1294) | II-front-01 |
| B4 | The Song endgame, 1268–1279 | II-10 / II-11 |
| B5 | Reception, 1298 → 2013 (manuscripts, print, Columbus, Ramusio, Yule, Wood debate) | III-11 |
| B6 | **Book date vs history** (a table-timeline, e.g. Baudas 1255 vs 1258; Chinghis 1187 vs 1206) | I-back-01 |

## C. Explanatory diagrams (16)

**Schematic diagrams** (TikZ):

| # | Diagram | Ch. |
|---|---|---|
| C1 | Paper money: bark → sheet → seals → vermilion → circulation (with the 1287 revaluation sidebar) | II-5 |
| C2 | The *yam*: stations, runner forts, express riders, scale of "ten days in one" | II-5 |
| C3 | Keshig rota (Polo's 4 × 3,000 vs Palladius's 400) | II-3 |
| C4 | Mongol decimal army (*arban → tümen* vs the Book's terms) | I-12 |
| C5 | Paiza hierarchy (silver → gerfalcon), with the script change in 1269 | II-1 / I-2 |
| C6 | Tutia furnace process | I-8 |
| C7 | Zayton cost stack (duty + freight = "half the investment") | II-14 |
| C8 | Ilkhan succession: the Book vs the record | II-15 |

**Data charts** (Python):

| # | Chart | Ch. |
|---|---|---|
| C9 | Gold : silver ratio gradient (1:8 → 1:5 across Yunnan and Burma) | II-7 / II-8 |
| C10 | Pole Star altitude: the Book's cubits vs real latitude | III-3 / III-6 |
| C11 | Monsoon wind panels (NE Nov–Mar / SW May–Sep) + the Cocachin calendar strip | III-front-01, III-9 |

**Labelled cutaways** (illustrated base from the plate pipeline, with labels overlaid in TikZ, so the labels are typeset rather than generated):

| # | Cutaway | Ch. |
|---|---|---|
| C12 | Seagoing junk: 13 compartments, axial rudder, batten sails | III-1 (preview in II-14) |
| C13 | Sewn-plank ship of Hormos (coir stitching, hide deck with horses) | I-7 |
| C14 | Traction vs counterweight trebuchet | II-11 |
| C15 | Qanat cross-section | I-8 |
| C16 | Cane palace roof (split bamboo tiles) | I-13 |

## D. Comparison tables (14) — plain LaTeX `booktabs`, cheapest and highest value

| Ch. | Table |
|---|---|
| I-1 | Who captured Marco, and where? Text witnesses F / Pipino / Z / Ramusio / Yule |
| I-3 | The four scripts |
| I-5 | How the Caliph died: Polo / Hayton / Rashid / Ibn al-Furat |
| I-6 | Eight kingdoms of Persia, with identification and confidence |
| I-12 | Kaan succession: the Book vs the record |
| I-7 / I-9 / I-11 | Geographic text vs Ramusio, side by side (turns the Ramusio problem into a reader feature) |
| II-1 | Nayan |
| II-5 | Ahmad's murder: Polo vs *Yuan shi* (incl. Bolad) |
| II-8 | Mien battle numbers |
| II-11 | Saianfu, and the Yanju manuscript variants |
| II-13 | Kinsay numbers: Polo / Odoric / Ibn Battuta / Wassaf |
| III-1 | Japan 1274/1281: Polo vs Japanese and Yuan sources |
| III-9 / III-12 | **Cocachin in three sources** (Prologue / Rashid / *Yongle dadian* 1941) |
| III-12 | **Hits, misses and silences ledger** (cross-volume, with markers) |

## E. Print substitutes for the audio ideas

- **Pronunciation and names glossary** (back of each volume): book form → modern form → respelling → one-line gloss. Examples: Cambaluc/Khanbaliq, Keshican/keshig, Quinsay/Xingzai, Sagamoni Borcan, Cocachin/Kököchin.
- **Prologue in the original:** I-1 sets Rustichello's Franco-Italian opening ("Seignors emperaor et rois…") beside Yule's English, as a parallel-text box.

## Toolchain (to install; currently absent)

| Need | Tool |
|---|---|
| Markdown → LaTeX | **pandoc** + a Lua filter that swaps `.svg`/`.png` → `.pdf` for vector assets at LaTeX build |
| Typesetting | **LuaLaTeX** (Unicode: ʿ ā ṭ ü; CJK for Chinese names in tables) + `fontspec`, `booktabs`, `tikz`, `pgfplots` |
| Maps / charts | Python **matplotlib + cartopy** (or geopandas) + Natural Earth 1:10m |
| Timelines / diagrams | TikZ standalone → PDF; `dvisvgm` → SVG for Markdown preview |

Layout:

```
book/media/
  maps/        A*.pdf|svg   (generated)
  timelines/   B*.pdf|svg   (generated)
  diagrams/    C*.pdf|svg   (generated)
  plates/      <vol>-<ch>-<slug>.png + .yaml   (see illustration plan)
  public-domain/  real artworks + license notes
  legacy/      current files kept for reference
book/tools/media/   map.py, charts.py, timelines/*.tex, data/*.yaml
```

## Order of work

1. Fix the existing mis-captions now (cheap, and they are reader-facing errors today).
2. Install the toolchain and build **A1 + A16 + one TikZ timeline (B5)** as the pilot. This proves the vector → LaTeX and → Markdown paths and sets the visual system.
3. Once the gazetteer is fixed (content W5): the remaining maps.
4. Tables (D) are written during each chapter's W4 rewrite, since they draw on the same facts.
5. Diagrams and timelines in volume order.
