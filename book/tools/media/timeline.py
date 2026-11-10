#!/usr/bin/env python3
"""Timelines from data/B*.yaml -> TikZ (timeline.tex template) -> media/timelines/<file>.pdf + .svg.

  python3 tools/media/timeline.py            all timelines (needs lualatex; pdftocairo for the SVG)
  python3 tools/media/timeline.py B5         just this one
  python3 tools/media/timeline.py --test     self-check of the layout (no TeX needed)

Timeline YAML (see data/B5.yaml):
  id, file
  axis: {segments: [[y0, y1], ...] (a break between segments), length_cm, tick (years)}
  events: [{date | from+to, kind (style.yaml event_kind), label, note?, date_label?, fact}]
  legend: true|false
Layout is vertical (years run down the page) so a 4.5 in measure can hold the clustered decades.
"""
import shutil
import subprocess
import sys
from pathlib import Path
from string import Template

import yaml

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent.parent
DATA = HERE / "data"
OUT = BOOK / "media" / "timelines"
CACHE = HERE / ".cache"
STYLE = yaml.safe_load((HERE / "style.yaml").read_text())

AXIS_X, LABEL_X = 1.0, 1.55   # cm
MEASURE_CM = 4.5 * 2.54       # the text block width: timelines are drawn at final size, never scaled
BREAK_CM = 0.5                # gap left on the axis at each break
LINE_CM, NOTE_CM, PAD_CM = 0.36, 0.28, 0.05


def scaler(axis):
    """Return year -> y (cm). Segments share length_cm in proportion to their years."""
    segs = axis["segments"]
    years = sum(b - a for a, b in segs)
    k = (axis["length_cm"] - BREAK_CM * (len(segs) - 1)) / years

    def y(year):
        off = 0.0
        for a, b in segs:
            if a <= year <= b:
                return off + (year - a) * k
            off += (b - a) * k + BREAK_CM
        raise ValueError(f"{year} is outside the axis segments {segs}")
    return y


def layout(spec):
    """Each event -> (true y, label y, mark/range). Labels keep time order and never overlap."""
    y = scaler(spec["axis"])
    out, bottom = [], float("-inf")
    for e in spec["events"]:
        if e.get("kind") not in STYLE["event_kind"]:
            raise ValueError(f"{e.get('label')}: kind must be one of {list(STYLE['event_kind'])}")
        if "date" in e:
            y0 = y1 = y(e["date"])
        else:
            y0, y1 = y(e["from"]), y(e["to"])
        true_y = (y0 + y1) / 2
        lab_y = max(true_y, bottom + PAD_CM + LINE_CM / 2)
        bottom = lab_y + LINE_CM / 2 + (NOTE_CM if e.get("note") else 0)
        out.append({"e": e, "y0": y0, "y1": y1, "y": true_y, "lab": lab_y})
    return out


def tex(s):
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                 ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\^{}")):
        s = s.replace(a, b)
    return s.replace("'", "’")


def date_text(e):
    if "date_label" in e:
        return str(e["date_label"])
    if "date" in e:
        return str(e["date"])
    a, b = str(e["from"]), str(e["to"])
    return f"{a}–{b[2:] if a[:2] == b[:2] else b}"


def body(spec):
    y, rows, lines = scaler(spec["axis"]), layout(spec), [rf"\path (0,0) -- ({MEASURE_CM:.2f},0);"]
    segs, tick = spec["axis"]["segments"], spec["axis"]["tick"]
    for i, (a, b) in enumerate(segs):
        lines.append(rf"\draw[tl-axis] ({AXIS_X},{y(a):.3f}) -- ({AXIS_X},{y(b):.3f});")
        for t in range(-(-a // tick) * tick, b + 1, tick):
            lines.append(rf"\draw[tl-tick] ({AXIS_X - 0.1},{y(t):.3f}) -- ({AXIS_X},{y(t):.3f}) "
                         rf"node[tl-year, xshift=-0.1cm] {{{t}}};")
        if i:  # break mark: two short slashes in the gap
            g = y(a) - BREAK_CM / 2
            for d in (-0.07, 0.07):
                lines.append(rf"\draw[tl-tick] ({AXIS_X - 0.12},{g + d + 0.05:.3f}) -- ({AXIS_X + 0.12},{g + d - 0.05:.3f});")
    for r in rows:
        e = r["e"]
        kind = f"kind-{e['kind']}"
        if r["y0"] != r["y1"]:
            lines.append(rf"\draw[tl-range, k{e['kind']}] ({AXIS_X},{r['y0']:.3f}) -- ({AXIS_X},{r['y1']:.3f});")
        else:
            lines.append(rf"\node[{kind}] at ({AXIS_X},{r['y']:.3f}) {{}};")
        lines.append(rf"\draw[tl-leader] ({AXIS_X + 0.13},{r['y']:.3f}) -- ({AXIS_X + 0.28},{r['y']:.3f}) -- "
                     rf"({LABEL_X - 0.06},{r['lab']:.3f});")
        lines.append(rf"\node[tl-label] at ({LABEL_X},{r['lab']:.3f}) {{\tldate{{{date_text(e)}}}{tex(e['label'])}}};")
        if e.get("note"):
            lines.append(rf"\node[tl-note] at ({LABEL_X},{r['lab'] + LINE_CM / 2:.3f}) {{{tex(e['note'])}}};")
    if spec.get("legend"):
        used = [k for k in STYLE["event_kind"] if any(r["e"]["kind"] == k for r in rows)]
        ly, prev = max(r["lab"] for r in rows) + 0.9, None
        for i, k in enumerate(used):  # each item placed after the previous one's text
            at = f"(0.2,{ly:.3f})" if prev is None else f"([xshift=0.4cm]{prev}.east)"
            lines.append(rf"\node[kind-{k}] (lgm{i}) at {at} {{}};")
            lines.append(rf"\node[tl-note, anchor=west] (lgt{i}) at ([xshift=0.12cm]lgm{i}.east) "
                         rf"{{{tex(STYLE['event_kind'][k]['label'])}}};")
            prev = f"lgt{i}"
    return "\n".join(lines)


def render(spec):
    c = STYLE["colour"]
    colours = [rf"\definecolor{{ink}}{{HTML}}{{{c['ink'][1:]}}}", rf"\definecolor{{inksoft}}{{HTML}}{{{c['ink_soft'][1:]}}}"]
    kinds = []
    for k, v in STYLE["event_kind"].items():
        name = k.replace(" ", "-")
        colours.append(rf"\definecolor{{k{k}}}{{HTML}}{{{v['colour'][1:]}}}")
        extra = {"rectangle": "minimum size=3.8pt", "diamond": "minimum size=5pt",
                 "isosceles triangle": "shape border rotate=90, isosceles triangle apex angle=60, minimum size=4.4pt"
                 }.get(v["shape"], "")
        kinds.append(f"  kind-{name}/.style={{tl-mark, shape={v['shape']}, fill=k{k}, {extra}}},")
    return Template((HERE / "timeline.tex").read_text()).substitute(
        font=STYLE["font"], colours="\n".join(colours), kinds="\n".join(kinds), body=body(spec))


def build(names):
    files = [DATA / f"{n}.yaml" for n in names] if names else sorted(DATA.glob("B*.yaml"))
    work = CACHE / "tex"
    work.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    missing = [t for t in ("lualatex", "pdftocairo") if not shutil.which(t)]
    for f in files:
        spec = yaml.safe_load(f.read_text())
        src = work / f"{spec['file']}.tex"
        src.write_text(render(spec), encoding="utf-8")
        if missing:
            print(f"timeline.py: {', '.join(missing)} not installed; wrote {src.relative_to(BOOK)} only", file=sys.stderr)
            continue
        run = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", src.name],
                             cwd=work, capture_output=True, text=True)
        if run.returncode:
            sys.exit(f"timeline.py: lualatex failed on {src.name}:\n" + run.stdout[-2000:])
        shutil.copy(work / f"{spec['file']}.pdf", OUT / f"{spec['file']}.pdf")
        subprocess.run(["pdftocairo", "-svg", str(OUT / f"{spec['file']}.pdf"), str(OUT / f"{spec['file']}.svg")],
                       check=True)
        print(f"media/timelines/{spec['file']}.pdf|svg")
    if missing:
        sys.exit(1)


def self_test():
    axis = {"segments": [[1300, 1400], [1900, 1910]], "length_cm": 11.5, "tick": 50}
    y = scaler(axis)
    assert abs(y(1300)) < 1e-9 and abs(y(1400) - 10) < 1e-9 and abs(y(1900) - 10.5) < 1e-9 and abs(y(1910) - 11.5) < 1e-9
    rows = layout({"axis": axis, "events": [{"date": 1350, "kind": "text", "label": "a", "note": "n"},
                                            {"date": 1351, "kind": "print", "label": "b"},
                                            {"from": 1360, "to": 1380, "kind": "map", "label": "c"}]})
    assert rows[0]["lab"] == rows[0]["y"] and rows[1]["lab"] > rows[1]["y"]           # pushed down
    assert rows[1]["lab"] - rows[0]["lab"] >= LINE_CM + NOTE_CM + PAD_CM - 1e-9      # no overlap
    assert rows[2]["y"] == y(1370) and rows[2]["y0"] == y(1360)
    assert date_text({"from": 1483, "to": 1484}) == "1483–84" and date_text({"date": 1298}) == "1298"
    for bad in ({"date": 1500, "kind": "text"}, {"date": 1350, "kind": "film"}):
        try:
            layout({"axis": axis, "events": [bad]})
        except ValueError:
            continue
        raise AssertionError(f"accepted {bad}")
    for f in sorted(DATA.glob("B*.yaml")):
        render(yaml.safe_load(f.read_text()))
    print("timeline.py: self-test ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    self_test() if args == ["--test"] else build(args)
