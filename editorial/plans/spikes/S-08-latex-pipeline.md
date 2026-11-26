# S-08 — LaTeX build pipeline

**Status:** closed (2026-11-10) · **Timebox:** 1–2 sessions · **Gates:** `BLD` tasks; the Markdown conventions every chapter task must follow (figures, tables, notes, boxes)

## Question
How does a Markdown chapter become a print-ready LaTeX chapter, and which Markdown conventions must the chapters follow now so that the conversion stays mechanical?

## Why it matters
Chapter rewrites are about to touch every file. If [n] citations, Notes, epigraphs, tag lines, figures, tables and aside boxes don't follow a convertible pattern, every file gets reworked again at LaTeX time.

## Inputs
- Two or three representative chapters (one with tables, one with the epigraph and tag line, front-02 with images)
- `multimedia-plan.md` § Toolchain
- S-03 (how markers and Notes should render)

## Method
1. Install pandoc + LuaLaTeX (needs user approval for system packages).
2. Prototype: md → tex → pdf for I-1, II-5 and II-F2.
3. Decide:
   - [n] + `## Notes` → endnotes per chapter (probably) or footnotes;
   - epigraph and tag-line markup;
   - figure syntax with vector swap (Lua filter);
   - table style;
   - fonts with Unicode coverage (ʿ ā ṭ ü, CJK in tables);
   - trim size (default 6×9 in).
4. Write the "Markdown conventions" section that chapter tasks must follow.

## Output (definition of done)
- [x] `tools/build/` with a working build of 3 sample chapters to PDF (II-2, II-5, I-F2 + a test sheet; all three volumes also build)
- [x] Markdown conventions doc (`plans/registry/markdown-conventions.md`)
- [x] Trim size and fonts decided

## Feedback to plan
- `multimedia-plan.md` § Toolchain, § Technical spec in the style guide (plate pixel sizes depend on trim)

## Findings

_2026-11-10. Toolchain installed by the user from Debian trixie (`apt-get install --no-install-recommends pandoc texlive-luatex texlive-latex-recommended texlive-latex-extra texlive-bibtex-extra biber latexmk fonts-junicode fonts-noto-cjk`; 298 MB download, 895 MB on disk): pandoc 3.1.11.1, LuaHBTeX 1.18 (TeX Live 2024), biber 2.20, biblatex-chicago._

**Files used.** The spike named I-1, II-5 and II-F2. The run used **II-2** (the S-01 reference: epigraph, tag line, two asides, Ramusio flags, 20 Notes with keys), **II-5** (Chinese in the Notes; a D-table is planned there, `II-05.T5`), **I-F2** (two figures, three place tables) and a test sheet, `tools/build/samples/conventions.md`. The test sheet holds what no manuscript file has yet: the APP.T1 box, a `[reception]` tag line, a table with Chinese and a verdict column, and a scene break. **No chapter has a table today**; all 14 D-tables are still to be written in the `.T5` passes. Then all 49 files were built as three volumes (Vol. II 170 pp., Vol. III 143 pp.).

1. **The conversion is mechanical.** One Lua filter (`tools/build/book.lua`, about 200 lines) and one Pandoc template (`book.latex`) turn every element into a macro. Nothing in any of the 49 files needed a hand edit to build, and the sample build checks itself: `build.sh` fails if any convention stops reaching its macro.
2. **The epigraph is one paragraph.** `> quote` + `> — credit` with no blank line between is a single Pandoc paragraph. The filter splits it at the line break before the dash. No authoring change.
3. **Endnotes, not footnotes.** The Notes are already written at the chapter's end, numbered and sequential (the lint guarantees that). Printing them where they stand, as a numbered list under *Notes*, keeps the Markdown numbers, needs no endnote package, and keeps long multi-marker Notes out of the page bottoms of a 4.5 in measure. Body `[n]` becomes a linked superscript.
4. **Citations:** `pandoc --biblatex` + `biblatex-chicago` authordate works as S-24 decided: "Steinhardt (1990)", "(Larner 1999)". The base text needed two lines in the template. By default the style printed "(YC 1903, 2.8)", and with the date cleared "(YC, n.d., 2.8)". Switching off the list-of-shorthands date mode and the comma for siglum entries gives **"(YC 2.8)"** and "(YC Intro. § 54)". The *Abbreviations* list prints "YC See Polo, Marco."; the full entry is in *Works cited* ("YC (Polo, Marco). 1903. …"). The prose explaining the Roman-to-Arabic locators is for APP's *List of abbreviations*.
5. **Per-volume PDFs replace `refsection`.** Each volume is one build, so its *Works cited* and *Abbreviations* list only what it cites. S-24's "one `refsection` per volume" is not needed.
6. **Fonts.** Debian's `fonts-junicode` 2.211 ships **no italic** (every `*…*` would print upright, 25 font warnings), so Junicode is out unless installed from upstream. **Noto Serif** (already installed) covers every character the manuscript uses (ā 260, ṭ 203, ʿ 23, ḥ, ḳ, Greek), has a true italic, and matches Noto Serif CJK. Missing glyphs fall back through `luaotfload`: DejaVu Sans (✓ ✗ ◇ ≠ ↔) and Noto Serif CJK (相 省 站, II-5). No "Missing character" in any of the 49 files. The five markers are set by one macro in DejaVu Sans, so they look alike whatever the text face.
7. **Tables.** Pipe tables with short dashes get no widths from Pandoc and overflow 4.5 in. The filter sizes each column from its longest cell (capped at 60 characters, floor 10%). I-F2's three place tables then fit; longtable breaks them across pages. Style: `booktabs`, small type, no vertical rules. That settles `TBL.T1`.
8. **Media are not print-ready, and the extensions lie.** Header sniffing: **11 of the 22** legacy files have the wrong extension. All six `drawing-*.png` are JPEGs; `map-hangzhou-kinsay.png` and `map-indian-ocean.png` are JPEGs; both `map-asia-mongol-empire` files are GIFs; `map-china-yuan.jpg` is a PNG. LaTeX trusts the extension and stops on the first one. The filter now sniffs the header, places a labelled placeholder box for a file it cannot place, and warns below 1,350 px (300 dpi on the measure). Only 4 of 22 reach 1,350 px (`map-marco-polo-overview` .jpg 1,355 and .png 3,654; `map-return-route.jpg` 1,355; `map-marco-polo-shepherd.jpg` 1,726); the rest are 556–1,280 px. → `MED.T3`; the replacements come from S-09/S-10/S-11 anyway.
9. **Captions are written twice.** All six figures (the three F2 files) carry alt text and then a separate `*Caption:*` paragraph. The build prints the bracket text as the caption, so the paragraph prints as body text under a short caption. → convention change, F2 `.T5`.
10. **Content debts the build exposes** (already owned by other tasks): the `/workspace/…` paths in I-F2 Note [1] overflow the line (`DOC.T1`/scaffolding); `~25–30 miles` in II-5 Note [12] prints a raised tilde (the `~` rule, `.T4`); an unbreakable name chain in the II-15 closing recap overflows by 35 pt (the recap is cut in `.T3`). Long chapter titles overflowed the running head; the template now truncates them.
11. **The trim holds.** 6 × 9 in with a 4.5 × 7.2 in block, 11 pt: about 400–430 words on a full text page; II-2 runs 8 pages with its Notes, Vol. II 170 pages in all. The plate sizes in `illustration-style-guide.md` stand.
12. **S-09 ran in parallel** and took S-08's face (Noto Serif) for its maps and timeline. It asked for generated assets to print at natural size: the template now sizes every figure at its natural size, shrunk only to fit the 4.5 × 5.4 in maximum. A1 (`media/maps/A1-series-overview.svg`, 4.5 in wide) is in the test sheet, referred to by its SVG, and prints from the PDF beside it.

## Decision
_Closed 2026-11-10._

1. **Pipeline:** Markdown → `pandoc` + `tools/build/book.lua` + `tools/build/book.latex` → LuaLaTeX + biber via `latexmk`. One PDF per volume: `tools/build/build.sh <name> <files…>`; `tools/build/build.sh` alone builds and checks the S-08 sample. Output in `build/` (git-ignored).
2. **Notes: endnotes per chapter**, printed at the chapter's end under *Notes*, numbered as in the Markdown, body marks as linked superscripts.
3. **Trim 6 × 9 in, text block 4.5 × 7.2 in, 11 pt.** Text face **Noto Serif**; markers and symbols **DejaVu Sans**; Chinese **Noto Serif CJK SC**; all three already on the machine. Junicode 2 from upstream (it has italics) stays an option if a more medieval face is wanted: one line in the template, but it needs your approval to install (`BLD.T7`).
4. **Citations:** biblatex-chicago authordate; the base text prints as "(YC 2.8)"; per-volume *Abbreviations* and *Works cited* come from the volume build.
5. **Markdown conventions:** `plans/registry/markdown-conventions.md`, with the changes recorded in `VOICE-GUIDE.md` § How the apparatus survives into LaTeX. Changed: captions inside the image brackets; no bracketed Note numbers in prose; media type, size and vector rules; `---` inside a chapter is a scene break; markers allowed in a table's verdict column.
6. **Lint:** the bracketed-number rule is already enforced (`citations`). To add (`BLD.T6`): `*Caption:*` paragraph = error; heading pair = warning. Media checks stay in the build.

## Changed in plan docs
- `VOICE-GUIDE.md` § How the apparatus survives into LaTeX: table rewritten for the decisions; six convention items with their lint status.
- `plans/registry/markdown-conventions.md`: new.
- `multimedia-plan.md` § Toolchain: installed; build layout; vector-swap and size rules.
- `illustration-style-guide.md` § Technical spec: trim confirmed; build check named.
- `tasks/cross/BLD-build-tooling.md`: backlog updated; `BLD.T2`, `BLD.T4`, `BLD.T6`, `BLD.T7` written.
- `tasks/cross/TBL-tables.md`: `TBL.T1` (shared style) done by S-08; markers in tables answered.
- `tasks/cross/MED-existing-media.md`: `MED.T3` (mis-typed and undersized files).
- `tasks/cross/GLO-glossary.md`: layout moves to `BLD.T4`.
- `S-24`: Works cited and Abbreviations wired into the build.
- `S-07` § Front/back roles and `VOICE-GUIDE.md` § Front and back matter: the B1 pointer is written "see II-11, Note 4" (no brackets).
- `S-09`: its request (natural-size figures) marked done.
- Every chapter file's `.T5` (49): follows the conventions doc, done when the build places its figures with no placeholder or warning; the three F2 files also move their captions.
- `README.md`: board, decision log.

## Tasks to create on close
- [x] `BLD.T2` full-book build per volume · `BLD.T4` front/back matter, index, glossary layout · `BLD.T6` lint rules for the build conventions · `BLD.T7` text face (Junicode option): in `tasks/cross/BLD-build-tooling.md`.
- [x] `MED.T3`: in `tasks/cross/MED-existing-media.md`.
- [x] `.T5` in all 49 chapter files: conventions line added; F2 files: caption move.
