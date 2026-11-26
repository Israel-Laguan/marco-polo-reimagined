#!/usr/bin/env bash
# Run from any working directory. All generated files go to build/ by default.
set -euo pipefail
cd "$(dirname "$0")/../.."

if [[ ${1:-} == media ]]; then
    py=tools/media/.venv/bin/python
    if [[ ! -x $py ]]; then
        python3 -m venv tools/media/.venv
        "$py" -m pip install -q -r tools/media/requirements.txt
    fi
    "$py" tools/media/map.py --test
    "$py" tools/media/map.py
    python3 tools/media/timeline.py --test
    python3 tools/media/timeline.py
    exit
fi
if [[ $# == 0 ]]; then
    set -- sample manuscript/vol-2/ch-02-person-palace.md manuscript/vol-2/ch-05-ahmad-paper-coal.md \
        manuscript/vol-1/front-02-maps-outbound.md tools/build/samples/conventions.md
fi

format=latex
case "$1" in
    html|epub|txt) format=$1; shift ;;
esac
name=${1:-}
if [[ ! $name =~ ^[[:alnum:]][[:alnum:]_-]*$ ]]; then
    echo "Usage: $0 [html|epub|txt] vol1|vol2|vol3 or $0 NAME FILE.md..." >&2
    exit 2
fi
shift
volume=
case "$name" in
    vol[123])
        [[ $# == 0 ]] || { echo "A volume takes its reading order from manuscript/edition.json" >&2; exit 2; }
        volume="manuscript/vol-${name#vol}"
        arguments=$(python3 tools/edition.py arguments "$name")
        mapfile -t files <<< "$arguments"
        ;;
    *)
        [[ $format == latex && $# -gt 0 ]] || { echo "Specify a volume or a list of Markdown files" >&2; exit 2; }
        files=()
        for file in "$@"; do
            case "$file" in
                vol-[123]/*) file="manuscript/$file" ;;
            esac
            files+=("$file")
        done
        ;;
esac

out=${BOOK_OUTPUT_DIR:-build}
mkdir -p "$out"
common=(-f markdown-subscript-superscript --lua-filter tools/build/map-links.lua
        --bibliography manuscript/bibliography.bib)
if [[ $format != latex ]]; then
    options=(-s --toc --resource-path="$volume" --lua-filter tools/build/preview.lua
             -M 'reference-section-title=Works cited')
    if [[ $format == html ]]; then
        BOOK_HTML_ASSETS=$(python3 -c 'import os, sys; print(os.path.relpath("manuscript/assets", sys.argv[1]))' "$out")
        export BOOK_HTML_ASSETS
        if [[ $name == vol1 ]]; then
            options+=(--include-in-header tools/build/parallel-text.html)
        fi
    fi
    writer=$format
    if [[ $format == txt ]]; then
        writer=plain
        options+=(--wrap=none)
    fi
    pandoc "${files[@]}" "${common[@]}" "${options[@]}" -t "$writer" -o "$out/$name.$format" \
        2>"$out/$name.$format.log" || { cat "$out/$name.$format.log" >&2; exit 1; }
    if grep -Ei 'citeproc|not found' "$out/$name.$format.log"; then
        echo "$out/$name.$format: unresolved resource or citation" >&2
        exit 1
    fi
    echo "$out/$name.$format"
    exit
fi

pandoc "${files[@]}" "${common[@]}" -t latex --template tools/build/book.latex \
    --lua-filter tools/build/book.lua --top-level-division=chapter --biblatex \
    -o "$out/$name.tex" 2>"$out/$name.pandoc.log" || { cat "$out/$name.pandoc.log" >&2; exit 1; }
latexmk -lualatex -interaction=nonstopmode -halt-on-error -recorder -outdir="$out" "$out/$name.tex" \
    >"$out/$name.build.log" 2>&1 || { tail -60 "$out/$name.build.log" >&2; exit 1; }

echo "$(grep -c 'placeholder for' "$out/$name.pandoc.log" || true) placeholders," \
    "$(grep -c 'px wide' "$out/$name.pandoc.log" || true) undersized rasters," \
    "$(grep -cE 'Overfull .*hbox [(][0-9]{2,}' "$out/$name.log" || true) overfull lines (>= 10pt)," \
    "$(grep -o '[0-9]* pages' "$out/$name.log" | tail -1)"
grep 'book.lua:' "$out/$name.pandoc.log" || true
if grep -E 'Missing character|Citation .+undefined|Reference .+undefined|There were undefined (references|citations)|could not be found in the database' "$out/$name.log"; then
    echo "$out/$name: unresolved citations, references, or glyphs" >&2
    exit 1
fi
if [[ ${BOOK_STRICT:-0} == 1 ]] && grep -E 'placeholder for|px wide' "$out/$name.pandoc.log"; then
    echo "$out/$name: unusable print assets" >&2
    exit 1
fi
if [[ $name == sample ]]; then
    for macro in bookchapter chaptertag 'begin{epigraphq}' 'begin{aside}' 'begin{howto}' \
        scenebreak notemark noteitem 'mk{' figplaceholder includegraphics 'begin{longtable}' autocite; do
        grep -Fq "$macro" "$out/$name.tex" || { echo "Sample check failed for $macro" >&2; exit 1; }
    done
fi
echo "$out/$name.pdf"
