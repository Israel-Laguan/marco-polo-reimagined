#!/usr/bin/env python3
"""Data charts (DIA C9–C11) -> media/diagrams/<file>.pdf + .svg, on map.py's pattern (matplotlib, style.yaml).

  tools/media/.venv/bin/python tools/media/charts.py           all charts
  tools/media/.venv/bin/python tools/media/charts.py C10       just this one
  tools/media/.venv/bin/python tools/media/charts.py --test    self-check (no drawing)

Charts are drawn at the 4.5 in measure, never taller than 5.4 in. Every value carries its source
(`fact`: a plans/registry/facts.md row id or section); the Book's figures are labelled as the Book's.
"""
import sys

from map import BOOK, CACHE, STYLE, gazetteer, setup_fonts

OUT = BOOK / "media" / "diagrams"
W_IN, MAX_H_IN = 4.5, 5.4
C = STYLE["colour"]
V = STYLE["volume"]
PT = STYLE["size_pt"]

# C9 — silver given for one weight of gold, east to west as the Book travels (Yule's note,
# refs/yule-vol2.txt:5934–5937; the Descent market, 6591–6592). facts.md § Schematic data, C9.
C9 = [
    {"id": "yachi", "where": "Yachi\n(Kunming)", "silver": 8, "fact": "Schematic data C9"},
    {"id": "carajan", "where": "Carajan\n(Dali)", "silver": 6, "fact": "Schematic data C9"},
    {"id": "vochan", "where": "Vochan\n(Zardandan)", "silver": 5, "fact": "Schematic data C9"},
    {"id": None, "where": "market on\nthe Descent", "silver": 5, "fact": "Schematic data C9"},
]
C9_REF = [(10, "Yuan treasury rate, 1287 (Yule)"), (12, "Western Europe, c. 1300 (Yule's estimate)")]

# C10 — the Book's height of the North Star, in cubits, against gazetteer latitude.
# None = "not seen"; ">" = "still higher", no number. facts.md § Schematic data, C10.
C10 = [
    {"id": "samara", "where": "Java the Less (Sumatra)", "cubits": None, "fact": "Schematic data C10"},
    {"id": "comari", "where": "Comari", "cubits": 1, "fact": "Schematic data C10"},
    {"id": "melibar", "where": "Melibar", "cubits": 2, "fact": "Schematic data C10"},
    {"id": "gozurat", "where": "Gozurat", "cubits": 6, "fact": "Schematic data C10"},
    {"id": "cambaet", "where": "Cambaet", "cubits": ">", "fact": "Schematic data C10"},
]

# C11 — monsoon months per basin (S18-F4, a Ming-era source used as analogy) and the fleet's calendar.
# Months are numbered from Jan 1290 = 0. Yule's reconstruction from the Book's intervals (S18-F3), not documented fleet events.
# x = months from 1 January (0 = start of Jan, 12 = end of Dec); spans past 12 wrap into the next year.
C11_MONSOON = {"South China Sea": {"NE": [(9, 15)], "SW": [(4, 8)]},      # NE Oct–Mar, SW May–Aug
               "Indian Ocean": {"NE": [(11, 14)], "SW": [(3.5, 9)]}}      # NE Dec–Feb, SW late Apr–Sep
C11_EVENTS = [
    {"row": "Departure (debated)", "from": 9, "to": 15, "kind": "alt", "label": "Yang: late 1290 or early 1291", "at": "above", "fact": "F-15"},
    {"row": "Departure (debated)", "from": 24, "to": 27, "kind": "alt", "label": "Yule: early 1292", "at": "right", "fact": "F-15"},
    {"row": "Yule's reading", "from": 24, "to": 27, "kind": "leg", "label": "c. 3 months to Sumatra", "at": "above", "fact": "S18-F3"},
    {"row": "Yule's reading", "from": 27, "to": 32, "kind": "stop", "label": "5-month stop", "at": "below", "fact": "S18-F3"},
    {"row": "Yule's reading", "from": 32, "to": 46.5, "kind": "leg", "label": "to Hormuz, c. Nov 1293", "at": "inside", "fact": "S18-F3"},
]
C11_MARKS = [(14.3, "Argon dies, 10 Mar 1291", "F-33")]


def latitude(pid, gaz):
    lat = gaz[pid]["latitude"]
    if not lat:
        raise ValueError(f"{pid}: no latitude in the gazetteer")
    return float(lat)


def style_axes(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(C["ink_soft"])
    ax.tick_params(colors=C["ink_soft"], labelsize=PT["graticule"] + 0.8, width=0.4, length=2.5)


def note(fig, text, y=0.012):
    fig.text(0.01, y, text, fontsize=PT["note"], style="italic", color=C["ink_soft"], va="bottom", wrap=True)


def c9(plt, gaz):
    fig, ax = plt.subplots(figsize=(W_IN, 2.5))
    xs = range(len(C9))
    ys = [r["silver"] for r in C9]
    ax.plot(xs, ys, color=V["II"], lw=1.1, marker="o", ms=4, zorder=3)
    for x, y in zip(xs, ys):
        ax.annotate(f"{y} : 1", (x, y), xytext=(0, 5), textcoords="offset points", ha="center",
                    fontsize=PT["label"] + 0.5, color=C["ink"], fontweight="bold")
    for y, lab in C9_REF:
        ax.axhline(y, color=C["ink_soft"], lw=0.5, ls=(0, (3, 2)))
        ax.text(-0.35, y + 0.15, lab, fontsize=PT["note"], color=C["ink_soft"], ha="left", va="bottom", style="italic")
    ax.set_xticks(list(xs), [r["where"] for r in C9], fontsize=PT["label"], color=C["ink"])
    ax.set_xlim(-0.4, len(C9) - 0.5)
    ax.set_ylim(0, 13.5)
    ax.set_ylabel("weights of silver for one of gold", fontsize=PT["label"], color=C["ink"])
    ax.set_xlabel("east to west, in the Book's order, toward Mien", fontsize=PT["note"], color=C["ink_soft"], style="italic")
    style_axes(ax)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.97, bottom=0.31)
    note(fig, "The Book's rates. Yule reads the western ones as prices paid to gold-selling hill peoples, not a general exchange.")
    return fig


def c10(plt, gaz):
    fig, ax = plt.subplots(figsize=(W_IN, 2.6))
    pts = [(latitude(r["id"], gaz), r) for r in C10]
    for lat, r in pts:
        if r["cubits"] is None:
            ax.plot(lat, 0, marker="o", mfc="white", mec=V["III"], ms=4.5, mew=0.8, zorder=3)
            ax.annotate(f"{r['where']}: not seen", (lat, 0), xytext=(6, 0), textcoords="offset points",
                        fontsize=PT["label"], color=C["ink"], va="center")
        elif r["cubits"] == ">":
            ax.annotate("", (lat, 7.4), (lat, 6.3), arrowprops={"arrowstyle": "-|>", "color": V["III"], "lw": 0.8})
            ax.annotate(f"{r['where']}: “still higher”", (lat, 7.0), xytext=(-6, 0), textcoords="offset points",
                        fontsize=PT["label"], color=C["ink"], va="center", ha="right")
        else:
            ax.plot(lat, r["cubits"], marker="o", color=V["III"], ms=4.5, zorder=3)
            ax.annotate(f"{r['where']}: {r['cubits']}", (lat, r["cubits"]), xytext=(-6, -2), textcoords="offset points",
                        fontsize=PT["label"], color=C["ink"], ha="right", va="top")
    known = sorted((lat, r["cubits"]) for lat, r in pts if isinstance(r["cubits"], int))
    ax.plot(*zip(*known), color=V["III"], lw=0.6, ls=(0, (2, 2)), zorder=2)
    ax.set_xlim(0, 25)
    ax.set_ylim(-0.6, 8)
    ax.set_xlabel("latitude, degrees north (gazetteer)", fontsize=PT["label"], color=C["ink"])
    ax.set_ylabel("North Star above the sea,\nin the Book's cubits", fontsize=PT["label"], color=C["ink"])
    style_axes(ax)
    fig.subplots_adjust(left=0.13, right=0.98, top=0.97, bottom=0.27)
    note(fig, "The pole's height equals the latitude; the Book's cubits rise with it but are a sailor's rough measure, not a fixed angle.")
    return fig


def c11(plt, gaz):
    from matplotlib.patches import Rectangle
    fig, (top, cal) = plt.subplots(2, 1, figsize=(W_IN, 3.3), height_ratios=[1, 1.25])
    # panels: one year, both basins
    for i, (basin, winds) in enumerate(C11_MONSOON.items()):
        y = 1 - i
        for wind, spans in winds.items():
            col = V["III"] if wind == "SW" else C["ink_soft"]
            for a, b in spans:
                for lo, hi in ((a, min(b, 12)), (0, b - 12)) if b > 12 else ((a, b),):
                    if hi > lo:
                        top.add_patch(Rectangle((lo, y - 0.32), hi - lo, 0.64, color=col, alpha=0.85 if wind == "SW" else 0.55, lw=0))
                        top.text((lo + hi) / 2, y, wind, ha="center", va="center", fontsize=PT["label"], color="white", fontweight="bold")
        top.text(-0.15, y, basin, ha="right", va="center", fontsize=PT["label"], color=C["ink"])
    top.set_xlim(0, 12)
    top.set_ylim(-0.6, 1.6)
    top.set_xticks([m + 0.5 for m in range(12)], list("JFMAMJJASOND"), fontsize=PT["graticule"] + 0.8)
    top.set_yticks([])
    top.set_title("Monsoon months (a Ming-era account, by analogy)", fontsize=PT["label"] + 0.6, color=C["ink"], loc="left", pad=3)
    style_axes(top)
    top.spines["left"].set_visible(False)
    # calendar strip, Jan 1290 – Dec 1293
    rows = list(dict.fromkeys(e["row"] for e in C11_EVENTS))
    for yr in range(4):  # SW monsoon (Indian Ocean) shading, every year
        cal.axvspan(12 * yr + 3.5, 12 * yr + 9, color=V["III"], alpha=0.10, lw=0)
    for e in C11_EVENTS:
        y = len(rows) - 1 - rows.index(e["row"])
        face = {"alt": "white", "leg": V["III"], "stop": V["II"]}[e["kind"]]
        cal.add_patch(Rectangle((e["from"], y - 0.25), e["to"] - e["from"], 0.5, facecolor=face, edgecolor=V["III"],
                                hatch="////" if e["kind"] == "alt" else None, lw=0.6))
        x, va, ha, dy = {"above": (e["from"], "bottom", "left", 0.3), "below": (e["from"], "top", "left", -0.3),
                         "right": (e["to"] + 0.4, "center", "left", 0), "inside": ((e["from"] + e["to"]) / 2, "center", "center", 0)}[e["at"]]
        cal.text(x, y + dy, e["label"], fontsize=PT["note"], va=va, ha=ha, color="white" if e["at"] == "inside" else C["ink"])
    for x, lab, _ in C11_MARKS:
        cal.axvline(x, color=V["I"], lw=0.7)
        cal.text(x + 0.3, -0.8, lab, fontsize=PT["note"], color=V["I"], va="center")
    cal.set_yticks(range(len(rows)), rows[::-1], fontsize=PT["label"], color=C["ink"])
    cal.set_xlim(0, 48)
    cal.set_ylim(-1.05, len(rows) - 0.1)
    cal.set_xticks([0, 12, 24, 36, 48], ["1290", "1291", "1292", "1293", "1294"], fontsize=PT["graticule"] + 0.8)
    cal.set_title("Cocachin's fleet: the debated start and Yule's reading of the Book's intervals",
                  fontsize=PT["label"] + 0.6, color=C["ink"], loc="left", pad=3)
    style_axes(cal)
    fig.subplots_adjust(left=0.22, right=0.98, top=0.93, bottom=0.12, hspace=0.75)
    note(fig, "Pale band: SW monsoon in the Indian Ocean. The stop and arrival are Yule's inferences, not documented fleet events.")
    return fig


CHARTS = {"C9": ("C9-gold-silver", c9), "C10": ("C10-pole-star", c10), "C11": ("C11-monsoon-cocachin", c11)}


def build(names):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    setup_fonts()
    gaz = gazetteer()
    OUT.mkdir(parents=True, exist_ok=True)
    CACHE.mkdir(parents=True, exist_ok=True)
    for key in names or CHARTS:
        file, draw = CHARTS[key]
        fig = draw(plt, gaz)
        w, h = fig.get_size_inches()
        assert w <= W_IN + 1e-6 and h <= MAX_H_IN + 1e-6, f"{key}: {w} x {h} in"
        for ext in ("pdf", "svg"):  # no timestamp, so an unchanged chart regenerates byte-identical
            fig.savefig(OUT / f"{file}.{ext}", metadata={"CreationDate": None} if ext == "pdf" else {"Date": None})
        fig.savefig(CACHE / f"{file}.png", dpi=200)  # review proof only
        plt.close(fig)
        print(f"media/diagrams/{file}.pdf|svg  {w:.2f} x {h:.2f} in")


def self_test():
    gaz = gazetteer()
    for rows in (C9, C10):
        for r in rows:
            assert r.get("fact"), r
            if r["id"]:
                assert r["id"] in gaz, f"unknown gazetteer id {r['id']}"
    lats = [latitude(r["id"], gaz) for r in C10]
    assert lats == sorted(lats), "C10 rows must run south to north"
    cubits = [r["cubits"] for r in C10 if isinstance(r["cubits"], int)]
    assert cubits == sorted(cubits)
    assert [r["silver"] for r in C9] == sorted((r["silver"] for r in C9), reverse=True)
    for e in C11_EVENTS:
        assert 0 <= e["from"] < e["to"] <= 48 and e["fact"], e
    assert all(fact for *_, fact in C11_MARKS)
    print("charts.py: self-test ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    self_test() if args == ["--test"] else build(args)
