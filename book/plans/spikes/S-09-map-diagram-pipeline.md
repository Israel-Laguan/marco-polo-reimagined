# S-09 — Map and diagram pipeline

**Status:** closed 2026-11-10 · **Timebox:** 1–2 sessions · **Gates:** all `MAP` and `DIA` tasks

## Question
Can maps, timelines and diagrams be generated from data into vector files that look like one system and drop into both the Markdown preview and LaTeX?

## Why it matters
The plan calls for 17 maps, 6 timelines and 16 diagrams. Each built ad hoc means inconsistency and no way to regenerate when the gazetteer or the facts change.

## Inputs
- `gazetteer.csv` (after S-04, or the current file for the pilot)
- `multimedia-plan.md` § A, B, C
- S-08 (fonts and trim)

## Method
1. Install matplotlib + cartopy (or geopandas) and Natural Earth 1:10m; TikZ standalone + dvisvgm.
2. Pilot **A1** (series overview), **A16** (Cocachin return; solid/dashed/dotted legend) and **B5** (reception timeline).
3. Fix the visual system: palette, line semantics, marker colours by reliability, label font, scale bar, graticule.
4. Check output in the Markdown preview and in a LaTeX test page.

## Output (definition of done)
- [x] `tools/media/` with `map.py`, timeline TikZ template (`timeline.tex` + `timeline.py`), data YAML format (documented in each script's header; examples `data/A1.yaml`, `data/A16.yaml`, `data/B5.yaml`), shared `style.yaml`
- [x] 3 pilot assets: `media/maps/A1-series-overview`, `media/maps/A16-cocachin-return`, `media/timelines/B5-reception` (`.pdf` + `.svg` each)
- [x] Visual system section added to `multimedia-plan.md`

## Feedback to plan
- `multimedia-plan.md` § Principles, § Toolchain; drop or merge any assets the pilot shows are low-value

## Findings

**S-20 follow-through, 2026-11-13:** the B5 pilot now uses an approximate mid-15th-century span for the surviving Fra Mauro map, distinguishes the 1603 Pamir crossing from Góis’s 1607 death, and labels Columbus-circle notes as undated. The SVG and PDF were regenerated; B5’s later expansion and layout review remain DIA.B5. See [S-20 closure](../research/results/S-20-closure.md). The pilot-era status below is historical.
- **Toolchain.** matplotlib 3.11 + cartopy 0.26 in a local venv (`tools/media/.venv`, pinned in `requirements.txt`; no system packages). Natural Earth downloads on first run into `tools/media/.cache/` (git-ignored). TeX Live, pandoc and latexmk are the system ones S-08 uses; `pdftocairo` (poppler) makes the timeline SVG, so `dvisvgm` is not needed.
- **Font.** The pilot started on Junicode and hit the same wall S-08 did: the Debian Junicode has no italic, so the timeline's italic notes fell back to upright. Both now use **Noto Serif**, the body face S-08 settled on. The maps and timeline embed it (PDF) or outline it (SVG).
- **Projection.** Lambert conic over 114° of longitude curves the parallels so much that the edge labels lie (Venice sat beside "30°N"). Wide maps (A1, A2, A16, A14) use **Equal Earth**; regional maps keep Lambert.
- **Unlabelled markers confuse.** Every gazetteer id on a route gets a marker, so stage-towns nobody labels read as mystery dots. Two fixes, both in the YAML format: sea and land waypoints are `[lat, lon]` pairs (no marker), and overview maps set `markers: labelled`.
- **Sea routes need waypoints.** A straight line between ports crosses the Malay peninsula, Anatolia and the Peloponnese. A16 carries ~25 waypoints; A1 reuses them. A shared waypoints file is not worth it yet (two maps); copy them until a third map needs the same legs.
- **The facts sheet limits B5.** `facts.md` § Timeline data gives B5 nothing after Góis (1603) except the Yule–Cordier edition. Yule's first edition (1871), Benedetto (1928), Moule–Pelliot (1938), Wood (1995) and Vogel (2013) need rows first (S-20). The pilot stops at 1903 and says so in its YAML header.
- **Size.** Uncut Natural Earth made each map 2.3 MB of SVG. Cutting the features to the map's extent (+10°) brings it to ~1 MB SVG / ~0.3 MB PDF. A 1:10m regional map will be larger; check when A9–A13 are made.
- **LaTeX placement.** `book.latex` sets `\includegraphics` to `width=\linewidth, height=0.75\textheight, keepaspectratio`. Maps are made exactly 4.5 in wide, so they land at 100 %. The first B5 was taller than 0.75 × 7.2 in and got shrunk (its type with it); B5 is now 4.5 × 4.9 in and places at 100 %. Rule: **a generated asset is never taller than 5.4 in.** Test page: `tools/build/build.sh s09-test <scratch md>` with the three assets, built clean (vector PDFs swapped in by `book.lua`, no missing glyphs).
- **Markdown preview.** The SVGs render with `rsvg-convert`; text is outlined, so GitHub/VS Code previews need no fonts.
- **Plan feedback.** A8 cannot be a map: Cachar Modun and Chagannor are `unfixed`. A6 also has unfixed places (Chingintalas, Chagannor): name them as text labels, not markers. A11 has Bangala with no point: text label with a dotted arrow.
- **Not done:** "approximate" coordinates (`coord_check = approximate`) get no distinct marker. At book scale it would only add noise; GAZ.T6 checks them before any close-up map.

## Decision
_Closed 2026-11-10._

- **Pipeline.** Maps: `tools/media/.venv/bin/python tools/media/map.py [A…]` → `media/maps/<file>.pdf|svg` from `gazetteer.csv` + `tools/media/data/A*.yaml`. Timelines: `python3 tools/media/timeline.py [B…]` → `media/timelines/` from `data/B*.yaml` through `timeline.tex` (LuaLaTeX). `--test` on either runs its self-check and validates every data file against the gazetteer or the event kinds.
- **Visual system:** `multimedia-plan.md` § Visual system; values in `tools/media/style.yaml`.
- **Data rules.** A map plots only gazetteer ids (map.py refuses unknown, `unfixed` and `legendary` ids); a route segment states `stated | inferred | reported` with a comment giving the reason. A timeline event carries its `facts.md` row id; spans for open dates.
- **Folded or moved (critique candidates and pilot results):**
  - A8 → schematic **C17** (DIA).
  - I-1 Adriatic inset (Venice, Genoa, Curzola) → new **A18**, half-width (`width: 2.2`).
  - I-3 Acre ↔ Jerusalem ↔ Ayas → folded into **A4** (extend it west to Acre).
  - II-1 Nayan theatre → an inset on **A7**.
  - Monsoon reuse in III-1, III-5, III-7 → **C11** reused, no new asset.
  - Reception reuse in III-10 and III-B1 → **B5** reused.
  - Canal summit at Sinjumatu → an inset profile on **A12**.
  - Kinsay revenue metrology → a comparison table in II-13 (§ D), not a diagram.
  - Asbestos processing (I-11) → dropped; the prose carries it.
- **For S-08 (not changed here):** generated assets are made at final size; the figure convention should place `media/maps|timelines|diagrams/` at their natural size rather than the `0.75\textheight` cap. **Done in S-08 (2026-11-10):** figures print at natural size, shrunk only to fit; A1 checked in the sample build.

## Tasks created on close
- [x] `MAP.T01`–`T18` in `tasks/cross/MAP-maps.md` (A1 and A16 done in this spike; A8 retired to DIA).
- [x] `DIA.B1`–`B6`, `DIA.C1`–`C17` in `tasks/cross/DIA-timelines-diagrams.md` (B5 piloted here; it is extended when S-20 adds rows).
- [x] `BLD.T3` media regeneration gets the two commands above.
