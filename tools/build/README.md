# Book tooling

Run builds from the repo root or invoke the script by its absolute path.

| Command | Output |
|---|---|
| `tools/build/build.sh vol1` | Volume I PDF and generated LaTeX in `build/` |
| `tools/build/build.sh txt vol2` | Volume II UTF-8 text with notes and works cited |
| `tools/build/build.sh html vol3` | Volume III HTML preview |
| `tools/build/build.sh epub vol3` | Volume III EPUB preview |
| `tools/build/build.sh NAME FILE.md...` | A proof of the files in the supplied order |
| `tools/build/build.sh` | The typographic sample |
| `tools/build/build.sh media` | Refresh the manuscript’s maps and timelines |

Install Pandoc, latexmk, LuaLaTeX, Biber, biblatex-chicago, Noto Serif, Noto Serif CJK, and DejaVu Sans for a local build. The [CI Dockerfile](../ci/Dockerfile) pins the Debian distribution and package snapshot and also installs LanguageTool and ChkTeX. Run `tools/ci/run.sh proof` with Docker to use that environment locally. Set `BOOK_STRICT=1` on a local print build to require print-ready figures.

## Pre-commit checks

Use `tools/pre-commit` as the Git pre-commit hook, or run it directly from the repository root. To install alongside an existing hook, add an invocation to that hook. To install in the default hook location when it is free, run:

```sh
hook=$(git rev-parse --git-path hooks/pre-commit)
test ! -e "$hook" && test ! -L "$hook" && install -m 755 tools/pre-commit "$hook"
```

The hook checks staged manuscript changes in an isolated snapshot. It compares lint errors to the tracked baseline and checks that the generated source index agrees with a staged bibliography. Run `python3 tools/sources_index.py` to regenerate the index and stage `research/registry/sources.md`.
