#!/bin/sh
# Markdown -> LaTeX -> PDF (S-08). Run from anywhere; output goes to book/build/.
#   tools/build/build.sh                     the S-08 sample (II-2, II-5, I-F2, test sheet)
#   tools/build/build.sh NAME FILE.md...     any set of files, in reading order (paths from book/)
set -eu
cd "$(dirname "$0")/../.."
if [ $# -eq 0 ]; then
  set -- sample vol-2/ch-02-person-palace.md vol-2/ch-05-ahmad-paper-coal.md \
    vol-1/front-02-maps-outbound.md tools/build/samples/conventions.md
fi
name=$1; shift
mkdir -p build
sample=no; [ "$name" = sample ] && sample=yes
pandoc "$@" -f markdown-subscript-superscript -t latex \
  --template tools/build/book.latex --lua-filter tools/build/book.lua \
  --top-level-division=chapter --biblatex --bibliography plans/registry/bibliography.bib \
  -o "build/$name.tex"
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build "build/$name.tex" >"build/$name.build.log" 2>&1 \
  || { tail -40 "build/$name.build.log"; exit 1; }
grep -E 'Missing character|undefined|Overfull \\hbox \([0-9]{2,}' "build/$name.log" | sort | uniq -c | sort -rn | head -20 || true
if [ $sample = yes ]; then # self-check: every convention still reaches its macro
  for m in bookchapter chaptertag 'begin{epigraphq}' 'begin{aside}' 'begin{howto}' scenebreak \
      notemark noteitem 'mk{' figplaceholder includegraphics 'begin{longtable}' 'autocite'; do
    grep -q "$m" "build/$name.tex" || { echo "sample check failed: no $m in build/$name.tex"; exit 1; }
  done
fi
echo "build/$name.pdf"
