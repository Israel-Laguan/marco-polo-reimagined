#!/usr/bin/env python3
"""Schematics (DIA C*): diagrams/C*.tex (a tikzpicture body) -> timeline.tex preamble -> media/diagrams/<name>.pdf + .svg.

  python3 tools/media/diagram.py             all schematics (needs lualatex and pdftocairo)
  python3 tools/media/diagram.py C3 C8       just these (file name prefix)
  python3 tools/media/diagram.py --test      wrap every body without TeX

A body draws at final size in cm (x right, y DOWN, as in the timelines) and starts with
`\\path (0,0) -- (11.43,0);` so every figure is the 4.5 in measure. Colours: ink, inksoft,
vI/vII/vIII (style.yaml volumes) and k<kind> (event kinds). Each body's header comment names its sources.
"""
import shutil
import subprocess
import sys

from timeline import BOOK, CACHE, HERE, standalone

SRC = HERE / "diagrams"
OUT = BOOK / "media" / "diagrams"
MAX_W_IN, MAX_H_IN = 4.5, 5.4


def size_in(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    w, h = next(l for l in info.splitlines() if l.startswith("Page size")).split()[2:5:2]
    return float(w) / 72, float(h) / 72


def build(names):
    files = [f for f in sorted(SRC.glob("C*.tex")) if not names or f.stem.split("-")[0] in names]
    missing = [t for t in ("lualatex", "pdftocairo", "pdfinfo") if not shutil.which(t)]
    if missing:
        sys.exit(f"diagram.py: {', '.join(missing)} not installed")
    work = CACHE / "tex"
    work.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    for f in files:
        src = work / f.name
        src.write_text(standalone(f.read_text()), encoding="utf-8")
        run = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", src.name],
                             cwd=work, capture_output=True, text=True)
        if run.returncode:
            sys.exit(f"diagram.py: lualatex failed on {f.name}:\n" + run.stdout[-2000:])
        pdf = OUT / f"{f.stem}.pdf"
        shutil.copy(work / pdf.name, pdf)
        subprocess.run(["pdftocairo", "-svg", str(pdf), str(pdf.with_suffix(".svg"))], check=True)
        w, h = size_in(pdf)
        flag = "" if w <= MAX_W_IN + 0.01 and h <= MAX_H_IN + 0.01 else f"  OVER {MAX_W_IN} x {MAX_H_IN} in"
        print(f"media/diagrams/{f.stem}.pdf|svg  {w:.2f} x {h:.2f} in{flag}")


def self_test():
    for f in sorted(SRC.glob("C*.tex")):
        body = f.read_text()
        assert body.lstrip().startswith("%"), f"{f.name}: start with a source comment"
        assert r"\path (0,0) -- (11.43,0);" in body, f"{f.name}: missing the measure path"
        assert "$" not in standalone(body).split(r"\begin{document}")[0], "unfilled template slot"
    print("diagram.py: self-test ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    self_test() if args == ["--test"] else build(args)
