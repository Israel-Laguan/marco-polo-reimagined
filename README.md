# The Book of the Million

A formal retelling of Marco Polo's *Description of the World* in three volumes, based on the Yule–Cordier translation (1903), with endnotes that weigh each claim against modern scholarship, plus maps, timelines and illustrated plates.

The manuscript is drafted. It is now being refined (fact-checking, re-voicing, apparatus and media) and is **not yet finished**. For live status, see [`book/plans/README.md`](book/plans/README.md).

## Layout

| Path | What it holds |
|---|---|
| `book/vol-1/`, `vol-2/`, `vol-3/` | The manuscript: 40 chapters plus front and back matter, one Markdown file each |
| `book/VOICE-GUIDE.md` | House style: voice, endnote markers (✓ ~ ✗ ◇ ?), citations |
| `book/plans/` | The refinement project: spike board, tasks, registries (facts, bibliography, characters), research returns and intakes |
| `book/refs/` | Public-domain source texts used for checking, including Yule–Cordier |
| `book/media/` | Maps, timelines, plates and legacy images; credits in `media/ATTRIBUTIONS.md` |
| `book/tools/` | Lint, citation, gazetteer, character and build tools |
| `book/gazetteer.csv` | Place-name authority |
| `input/`, `reports/`, `research_notes/` | Original inputs and early research notes |

## Working on it

Run these from `book/`.

```bash
python3 tools/lint.py                  # acceptance lint, all chapters (the definition of done)
python3 tools/lint.py vol-1/ch-02-house-of-polo.md -v   # one file, every issue
python3 -m unittest discover -s tests -q
tools/build/build.sh                   # sample PDF (Markdown → LaTeX → PDF, into book/build/)
tools/build/build.sh NAME FILE.md...   # build any set of files, in reading order
```

The build needs Pandoc and LuaLaTeX. Map and timeline scripts are in `tools/media/` (see their headers).

## Licence

Apache 2.0 (see `LICENSE`), for the project's own text and code. Images and quoted sources keep their own terms; see `book/media/ATTRIBUTIONS.md` and the headers in `book/refs/`.
