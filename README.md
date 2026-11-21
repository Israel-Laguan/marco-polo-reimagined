# The Book of the Million

A three-volume retelling of *Le Devisement dou monde* (*The Description of the World*), Marco Polo's travel account as written down by Rustichello da Pisa. It follows the 1903 Yule–Cordier translation and includes endnotes, maps, timelines and illustrated plates.

The first draft is complete. Fact-checking, re-voicing, apparatus and media work are in progress. For live status, see the [planning board](book/plans/README.md).

## Layout

| Path | What it holds |
|---|---|
| `book/vol-1/`, `book/vol-2/`, `book/vol-3/` | 40 chapters, including the closing essay, plus nine front and back matter files |
| `book/VOICE-GUIDE.md` | House style: voice, endnote markers (✓ ~ ✗ ◇ ?), citations |
| `book/plans/` | The refinement project: spike board, tasks, registries (facts, bibliography, characters), research returns and intakes |
| `book/refs/` | Public-domain source texts used for checking, including Yule–Cordier |
| `book/media/` | Maps, timelines, diagrams, plates and legacy images ([credits](book/media/ATTRIBUTIONS.md)) |
| `book/tools/` | Lint, citation, gazetteer, character and build tools |
| `book/gazetteer.csv` | Place-name authority |
| `input/`, `reports/`, `research_notes/` | Original inputs and early research notes |

## Working on it

Run these from `book/`.

```bash
python3 tools/lint.py                  # acceptance lint for all 49 manuscript files
python3 tools/lint.py vol-1/ch-02-house-of-polo.md -v   # one file, every issue
python3 -m unittest discover -s tests -q
tools/build/build.sh                   # sample PDF (Markdown → LaTeX → PDF, into book/build/)
tools/build/build.sh NAME FILE.md...   # build any set of files, in reading order
```

The PDF build uses Pandoc, latexmk, LuaLaTeX, Biber, biblatex-chicago, and the Noto Serif, Noto Serif CJK, and DejaVu Sans fonts. Media scripts are in `tools/media/`. Manuscript acceptance also includes a human read. See the [definition of done](book/plans/README.md#definition-of-done-s-02).

## Licence

The project's own text and code use the [Apache 2.0 licence](LICENSE). Images and quoted sources keep their own terms. See the [media credits](book/media/ATTRIBUTIONS.md) and the headers in `book/refs/`.
