# S-09 — Map and diagram pipeline

**Status:** open · **Timebox:** 1–2 sessions · **Gates:** all `MAP` and `DIA` tasks

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
- [ ] `tools/media/` with `map.py`, timeline TikZ template, data YAML format
- [ ] 3 pilot assets in `media/maps|timelines/`
- [ ] Visual system section added to `multimedia-plan.md`

## Feedback to plan
- `multimedia-plan.md` § Principles, § Toolchain; drop or merge any assets the pilot shows are low-value

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `MAP.T*` one per map; `DIA.T*` one per timeline or diagram
