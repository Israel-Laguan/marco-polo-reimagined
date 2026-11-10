# Markdown conventions for the print build (S-08)

Every manuscript file (`vol-*/ch-*.md`, `front-*.md`, `back-*.md`) is converted to LaTeX by `tools/build/book.lua` with no hand work. The filter recognises each element by **one fixed Markdown shape**. Anything written another way prints as plain text, or breaks the build.

Build: `tools/build/build.sh` (S-08 sample) or `tools/build/build.sh vol2 vol-2/front-01-*.md vol-2/front-02-*.md vol-2/ch-*.md vol-2/back-01-*.md` (one PDF per volume, in `book/build/`, git-ignored). The sample build checks that each shape below still reaches its LaTeX macro.

**Lint** column: **yes** = `tools/lint.py` enforces it already; **add** = to add (`BLD.T6`); **build** = the build reports it; **no** = not worth a rule.

| Element | Write exactly | Prints as | Lint |
|---|---|---|---|
| Chapter head | `# Chapter II-2` then `## Title` on the next block | "Chapter II-2" in small caps over the title; contents line "II-2 Title"; running head = title | add (heading pair) |
| Front / back head | `# Front Matter I-2` (or `# Back Matter …`) then `## Title` | title only, no label | add |
| Epigraph | `> *“quotation”*` and, on the next line of the same quote, `> — credit` (S-24 credit form) | small, right-set block; credit on its own line | yes (`epigraph_credit`) |
| Tag line | a paragraph that is only `**[V]**`, `**[R]**`, `**[M]**` or `**[reception]**` | small-caps line under the title | yes (`tags`) |
| Structural rules | `---` under the title block, and `---` directly before `## Notes` | nothing | no |
| Scene break | any other `---` on its own line | centred `* * *` | no |
| Body citation | `[n]` after the sentence, a space before it | superscript n, linked to the Note; the space is dropped | yes (`citations`: sequential 1..n) |
| Referring to a Note in prose | "Note 11", "II-5, Notes 11 and 12": **no brackets** | plain text | yes (a bracketed number breaks the `citations` sequence) |
| Aside | a paragraph opening with `— ` (em dash + space) | indented, smaller block; the dash is dropped | yes (`asides`: length, count) |
| Ramusio flag | ordinary words | ordinary words | yes (`ramusio`) |
| Notes | `## Notes`, then one paragraph per Note opening `[n] ` + marker | numbered list in small type at the chapter's end (endnotes per chapter) | yes (`citations`, `markers`) |
| Markers | ✓ ~ ✗ ◇ ? as **separate words** (`✓ / ~`, never `✓/~`); approximations as "about", never `~60` | DejaVu Sans glyphs; `~` prints as ∼ | yes (`markers`) |
| Source citation | Pandoc keys, S-24 forms: `[@yc, 2.8]`, `Vogel [-@vogel2013marco]` | (YC 2.8), Vogel (2013); *Works cited* and *Abbreviations* generated per volume | yes (`cite_keys`) |
| How-to-read box | `::: howto` … `:::` (Pandoc fenced div); `[3]` inside it is an example and prints unlinked | ruled box; markers as in the Notes | no |
| Figure | `![Caption sentence. *(Credit line.)*](../media/<dir>/<file>)` alone in its paragraph. The bracket text **is** the caption: no separate `*Caption:*` paragraph | float, full text width, numbered caption | add (`*Caption:*` paragraph is an error) |
| Figure file | path from the chapter: `../media/…`. Vector art: put `x.pdf` beside `x.svg`/`x.png` and keep referring to the `.svg`/`.png`; the build swaps in the PDF | PDF if present, else the raster | build |
| Raster size | extension = real file type (PNG or JPEG only); ≥ 1,350 px wide for a full-width figure (300 dpi on the 4.5 in measure; plate sizes in `illustration-style-guide.md`) | a wrong type, GIF or SVG-without-PDF prints as a labelled placeholder box; an undersized raster is a build warning | build |
| Table | pipe table, header row, `|---|---|` separator; no caption line | `booktabs` rules, small type, columns sized to their content; breaks across pages | no |
| Table widths | to set them yourself, make the separator dashes proportional and longer than one line (Pandoc's rule); otherwise the build sizes columns | as written | no |
| Verdict column | a table may carry the five markers, one per cell (`✓`, `~`) | same glyphs as the Notes | no |
| Chinese, Greek, diacritics | type the characters (相, ā, ʿ, ṭ) | Noto Serif; Noto Serif CJK for Chinese | no |
| Inline styles | `*italic*`, `**bold**` only; no raw LaTeX, no HTML, no `~sub~` or `^sup^` | as written | no |

## Not allowed (the filter cannot see it)

- Notes that point to another Note ("see [5]"): merge them (`VOICE-GUIDE.md` § Notes 3).
- Paths to tooling (`/workspace/…`) or file names in the text: the scaffolding rule already bans them.
- Emoji forms of the markers (✔️, ❌): use U+2713, U+2717, U+25C7.

## Layout decided by S-08 (not authoring rules)

Trim 6 × 9 in; text block 4.5 × 7.2 in; 11 pt Noto Serif. Endnotes per chapter, printed under *Notes* at the chapter's end, numbered as in the Markdown. One PDF per volume, so each volume's *Works cited* lists only what it cites, with no `refsection` needed. Details and open points: `spikes/S-08-latex-pipeline.md`.
