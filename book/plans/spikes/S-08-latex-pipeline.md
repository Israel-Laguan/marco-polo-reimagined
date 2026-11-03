# S-08 — LaTeX build pipeline

**Status:** open · **Timebox:** 1–2 sessions · **Gates:** `BLD` tasks; the Markdown conventions every chapter task must follow (figures, tables, notes, boxes)

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
- [ ] `tools/build/` with a working build of 3 sample chapters to PDF
- [ ] Markdown conventions doc (`plans/registry/markdown-conventions.md`)
- [ ] Trim size and fonts decided

## Feedback to plan
- `multimedia-plan.md` § Toolchain, § Technical spec in the style guide (plate pixel sizes depend on trim)

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `BLD.T*` (full-book build, front/back matter, index, glossary layout); `.T5` media placement per chapter
