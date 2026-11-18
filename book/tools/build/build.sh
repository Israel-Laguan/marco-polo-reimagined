#!/bin/sh
# Markdown -> LaTeX -> PDF (S-08). Run from anywhere; output goes to book/build/.
#   tools/build/build.sh                     the S-08 sample (II-2, II-5, I-F2, test sheet)
#   tools/build/build.sh media               regenerate all maps and timelines (BLD.T3)
#   tools/build/build.sh vol1|vol2|vol3      one volume in reading order -> build/volN.pdf (BLD.T2)
#   tools/build/build.sh html|epub vol1      preview / EPUB via citeproc -> build/vol1.html|epub (BLD.T9)
#   tools/build/build.sh NAME FILE.md...     any set of files, in reading order (paths from book/)
set -eu
cd "$(dirname "$0")/../.."
if [ "${1:-}" = media ]; then # BLD.T3: self-tests, then every map and timeline; stop on first failure
  py=tools/media/.venv/bin/python
  [ -x $py ] || { python3 -m venv tools/media/.venv && $py -m pip install -q -r tools/media/requirements.txt; }
  $py tools/media/map.py --test
  $py tools/media/map.py
  python3 tools/media/timeline.py --test
  python3 tools/media/timeline.py
  exit
fi
if [ $# -eq 0 ]; then
  set -- sample vol-2/ch-02-person-palace.md vol-2/ch-05-ahmad-paper-coal.md \
    vol-1/front-02-maps-outbound.md tools/build/samples/conventions.md
fi
fmt=
case "$1" in html|epub) fmt=$1; shift
  case "${1:-}" in vol[123]) ;; *) echo "usage: $0 $fmt vol1|vol2|vol3"; exit 2;; esac;;
esac
meta=
case "$1" in vol[123])
  [ $# -eq 1 ] || { echo "usage: $0 $1 (no file list)"; exit 2; }
  n=${1#vol}; r=$(echo I II III | cut -d' ' -f$n)
  set -- "$1" vol-$n/front-*.md vol-$n/ch-*.md vol-$n/back-*.md
  vtitle=$(sed -n "s/^# VOLUME $r — //p" outline-volumes.md)
  series=$(sed -n 's/^\*\*Working title (series):\*\* \*\(.*\)\*$/\1/p' outline-volumes.md)
  meta="volume=Volume $r|title=$vtitle|series=$series";;
esac
name=$1; shift
mkdir -p build
sample=no; [ "$name" = sample ] && sample=yes
IFS='|'; set -f # one -M per volume field; titles contain spaces
for kv in $meta; do set -- "$@" -M "$kv"; done
unset IFS; set +f
if [ -n "$fmt" ]; then # citeproc with pandoc's built-in CSL (Chicago 17th author-date); sigla via preview.lua
  pandoc "$@" -f markdown-subscript-superscript -s --toc --resource-path="vol-$n" \
    --lua-filter tools/build/preview.lua --bibliography plans/registry/bibliography.bib \
    -M reference-section-title="Works cited" -o "build/$name.$fmt" 2>"build/$name.$fmt.log" \
    || { cat "build/$name.$fmt.log"; exit 1; }
  grep -i 'citeproc\|not found' "build/$name.$fmt.log" && { echo "build/$name.$fmt: FAILED"; exit 1; }
  echo "build/$name.$fmt"; exit
fi
pandoc "$@" -f markdown-subscript-superscript -t latex \
  --template tools/build/book.latex --lua-filter tools/build/book.lua \
  --top-level-division=chapter --biblatex --bibliography plans/registry/bibliography.bib \
  -o "build/$name.tex" 2>"build/$name.pandoc.log" || { cat "build/$name.pandoc.log"; exit 1; }
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build "build/$name.tex" >"build/$name.build.log" 2>&1 \
  || { tail -40 "build/$name.build.log"; exit 1; }
# summary, not the log: placeholders and low-res rasters (book.lua), overfull lines >= 10pt
echo "$(grep -c 'placeholder for' "build/$name.pandoc.log") placeholders, $(grep -c 'px wide' "build/$name.pandoc.log") undersized rasters," \
  "$(grep -cE 'Overfull \\hbox \([0-9]{2,}' "build/$name.log") overfull lines (>= 10pt), $(grep -o '[0-9]* pages' "build/$name.log" | tail -1)"
grep -h 'book.lua:' "build/$name.pandoc.log" | sed 's/^book.lua: /  /' | sort -u | head -10
# fatal: a glyph the fonts lack, or a citation key biber could not resolve (final pass only)
bad=$(grep -E "Missing character|Citation '[^']*' .*undefined|could not be found in the database" "build/$name.log" | sort | uniq -c | sort -rn)
[ -z "$bad" ] || { echo "build/$name: FAILED"; echo "$bad" | head -20; exit 1; }
if [ $sample = yes ]; then # self-check: every convention still reaches its macro
  for m in bookchapter chaptertag 'begin{epigraphq}' 'begin{aside}' 'begin{howto}' scenebreak \
      notemark noteitem 'mk{' figplaceholder includegraphics 'begin{longtable}' 'autocite'; do
    grep -q "$m" "build/$name.tex" || { echo "sample check failed: no $m in build/$name.tex"; exit 1; }
  done
fi
echo "build/$name.pdf"
