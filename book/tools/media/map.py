#!/usr/bin/env python3
"""Maps from gazetteer.csv + one YAML per map -> media/maps/<file>.pdf (LaTeX) and .svg (Markdown).

  tools/media/.venv/bin/python tools/media/map.py              all maps in tools/media/data/A*.yaml
  tools/media/.venv/bin/python tools/media/map.py A16 A1       just these
  tools/media/.venv/bin/python tools/media/map.py --test       self-check (no drawing)

Map YAML (see data/A16.yaml):
  id, file, width (inches, default 4.5; height follows the extent), extent [lon0, lon1, lat0, lat1], centre [lon, lat],
  projection (lambert | equal_earth, for spans over ~60 degrees of longitude),
  scale (Natural Earth resolution, 10m|50m), graticule (degrees), scale_km, scale_at [lon, lat]
  routes: [{vol: I|II|III, style: stated|inferred|reported, path: [gazetteer id | [lat, lon], ...]}]
          path ids get a marker; [lat, lon] pairs are unmarked sea/land waypoints.
  label:  {id: pos | {pos, text}}   pos = n s e w ne nw se sw; only listed ids are labelled
  places: [id, ...]                 off-route places: marker + label (default pos e)
  text:   [{text, at: [lat, lon], kind: region|sea|note, rotate}]
  markers: all | labelled          (default all; overview maps mark only the labelled places)
  legend: {at: lower left|..., items: [lines, markers, volumes]}
"""
import csv
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent.parent
DATA = HERE / "data"
OUT = BOOK / "media" / "maps"
CACHE = HERE / ".cache"
STYLE = yaml.safe_load((HERE / "style.yaml").read_text())
POS = {"n": (0, 1), "s": (0, -1), "e": (1, 0), "w": (-1, 0),
       "ne": (1, 1), "nw": (-1, 1), "se": (1, -1), "sw": (-1, -1)}


def gazetteer():
    with open(BOOK / "gazetteer.csv", newline="", encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def plottable(row):
    return (row["latitude"] and row["id_confidence"] != "unfixed"
            and row["reliability"] in STYLE["reliability"])


def resolve(spec, gaz):
    """Check a map spec against the gazetteer; return (points per route, marked ids). Raises on bad ids."""
    errors, routes, marked = [], [], []
    for r in spec.get("routes", []):
        if r.get("vol") not in STYLE["volume"] or r.get("style") not in STYLE["line"]:
            errors.append(f"route {r.get('path', [])[:1]}: vol/style must be one of "
                          f"{list(STYLE['volume'])} / {list(STYLE['line'])}")
        pts = []
        for p in r.get("path", []):
            if isinstance(p, list):
                pts.append((float(p[1]), float(p[0])))
            elif p not in gaz:
                errors.append(f"unknown gazetteer id: {p}")
            elif not plottable(gaz[p]):
                errors.append(f"{p} has no plottable point (unfixed, blank or legendary)")
            else:
                pts.append((float(gaz[p]["longitude"]), float(gaz[p]["latitude"])))
                if p not in marked:
                    marked.append(p)
        routes.append(pts)
    for p in spec.get("places", []):
        if p not in gaz or not plottable(gaz[p]):
            errors.append(f"place {p}: unknown or not plottable")
        elif p not in marked:
            marked.append(p)
    for p in spec.get("label", {}) or {}:
        if p not in marked:
            errors.append(f"label {p}: not on a route or in places")
    if errors:
        raise ValueError(f"{spec.get('id')}: " + "; ".join(errors))
    return routes, marked


def label_of(pid, how, gaz):
    how = how if isinstance(how, dict) else {"pos": how or "e"}
    text = how.get("text", gaz[pid]["book_name"])
    if gaz[pid]["id_confidence"] == "disputed" and "text" not in how:
        text += STYLE["disputed_suffix"]
    return text, how.get("pos", "e")


def setup_fonts():
    from matplotlib import font_manager, rcParams
    names = {f.name for f in font_manager.fontManager.ttflist}
    family = [n for n in [STYLE["font"], *STYLE["fallback_fonts"]] if n in names]
    if family[:1] != [STYLE["font"]]:
        print(f"map.py: {STYLE['font']} not found; labels fall back to {family[:1]}", file=sys.stderr)
    rcParams.update({"font.family": family, "pdf.fonttype": 42, "svg.fonttype": "path",
                     "axes.linewidth": 0.4, "savefig.dpi": 300, "svg.hashsalt": "book"})


def natural_earth(kind, name, scale, extent, min_rank=None):
    """Natural Earth features cut to the map's extent (+10 degrees), so files carry only what shows."""
    import cartopy.io.shapereader as shp
    from shapely.geometry import box
    lon0, lon1, lat0, lat1 = extent
    window = box(lon0 - 10, max(lat0 - 10, -90), lon1 + 10, min(lat1 + 10, 90))
    reader = shp.Reader(shp.natural_earth(resolution=scale, category=kind, name=name))
    for rec in reader.records():
        if min_rank is None or (rec.attributes.get("scalerank") or 99) <= min_rank:
            g = rec.geometry.intersection(window)
            if not g.is_empty:
                yield g


def draw(spec, gaz):
    import cartopy
    import cartopy.crs as ccrs
    import matplotlib.patheffects as pe
    import matplotlib.pyplot as plt
    from cartopy.geodesic import Geodesic
    from matplotlib.lines import Line2D

    cartopy.config["data_dir"] = str(CACHE / "natural_earth")
    routes, marked = resolve(spec, gaz)
    c, sz = STYLE["colour"], STYLE["size_pt"]
    lon0, lon1, lat0, lat1 = spec["extent"]
    clon, clat = spec.get("centre", [(lon0 + lon1) / 2, (lat0 + lat1) / 2])
    if spec.get("projection", "lambert") == "equal_earth":  # wide maps: straight parallels, honest edge labels
        proj = ccrs.EqualEarth(central_longitude=clon)
    else:  # regional maps: conformal, so coasts and city plans keep their shape
        proj = ccrs.LambertConformal(central_longitude=clon, central_latitude=clat,
                                     standard_parallels=(lat0 + (lat1 - lat0) / 6, lat1 - (lat1 - lat0) / 6),
                                     cutoff=lat0 - 30)
    geo = ccrs.Geodetic()
    # Page width is fixed (the 4.5 in measure); height follows the projected extent, plus room for degree labels.
    width, (ml, mb, mr, mt) = spec.get("width", 4.5), (0.26, 0.17, 0.04, 0.04)
    fig = plt.figure(figsize=(width, 1))
    ax = fig.add_axes([0, 0, 1, 1], projection=proj)
    ax.set_extent(spec["extent"], crs=ccrs.PlateCarree())
    x0, x1, y0, y1 = ax.get_extent()
    height = (width - ml - mr) * (y1 - y0) / (x1 - x0) + mb + mt
    fig.set_size_inches(width, height)
    ax.set_position([ml / width, mb / height, 1 - (ml + mr) / width, 1 - (mb + mt) / height])
    ax.set_facecolor(c["sea"])
    ax.spines["geo"].set(linewidth=0.5, edgecolor=c["ink"])
    scale = spec.get("scale", "10m")
    pc = ccrs.PlateCarree()
    ax.add_geometries(natural_earth("physical", "land", scale, spec["extent"]), pc, facecolor=c["land"],
                      edgecolor=c["coast"], linewidth=0.25, zorder=1)
    ax.add_geometries(natural_earth("physical", "lakes", scale, spec["extent"], spec.get("lake_rank", 3)), pc,
                      facecolor=c["lake"], edgecolor=c["coast"], linewidth=0.2, zorder=1.1)
    ax.add_geometries(natural_earth("physical", "rivers_lake_centerlines", scale, spec["extent"],
                                    spec.get("river_rank", 3)),
                      pc, facecolor="none", edgecolor=c["river"], linewidth=0.35, zorder=1.2)
    gl = ax.gridlines(crs=pc, draw_labels=["left", "bottom"], linewidth=0.25, color=c["graticule"],
                      xlocs=range(-180, 181, spec.get("graticule", 10)),
                      ylocs=range(-90, 91, spec.get("graticule", 10)), x_inline=False, y_inline=False, zorder=1.5)
    gl.xlabel_style = gl.ylabel_style = {"size": sz["graticule"], "color": c["ink_soft"]}
    gl.rotate_labels = False

    halo = [pe.withStroke(linewidth=1.6, foreground=c["land"])]
    for r, pts in zip(spec.get("routes", []), routes):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, transform=geo, color=STYLE["volume"][r["vol"]], lw=STYLE["route_width_pt"],
                ls=STYLE["line"][r["style"]]["dash"], solid_capstyle="round", dash_capstyle="round", zorder=3)
    labels = dict(spec.get("label") or {})
    for pid in spec.get("places", []):
        labels.setdefault(pid, "e")
    shown = marked if spec.get("markers", "all") == "all" else list(labels)  # "labelled": overview maps
    for pid in shown:
        rel = STYLE["reliability"][gaz[pid]["reliability"]]
        ax.plot(float(gaz[pid]["longitude"]), float(gaz[pid]["latitude"]), "o", transform=pc,
                ms=STYLE["marker_pt"], mfc=rel["face"], mec=rel["edge"], mew=0.45, zorder=4)
    for pid, how in labels.items():
        text, pos = label_of(pid, how, gaz)
        dx, dy = POS[pos]
        ax.annotate(text, (float(gaz[pid]["longitude"]), float(gaz[pid]["latitude"])),
                    xycoords=pc._as_mpl_transform(ax), xytext=(dx * 3.2, dy * 3.2), textcoords="offset points",
                    ha={1: "left", -1: "right", 0: "center"}[dx], va={1: "bottom", -1: "top", 0: "center"}[dy],
                    fontsize=sz["label"], color=c["ink"], path_effects=halo, zorder=5)
    for t in spec.get("text", []):
        kind = t.get("kind", "note")
        style = {"region": dict(fontsize=sz["region"], color=c["ink_soft"]),
                 "sea": dict(fontsize=sz["sea"], color=c["ink_soft"], style="italic"),
                 "note": dict(fontsize=sz["note"], color=c["ink"], style="italic")}[kind]
        ax.text(t["at"][1], t["at"][0], t["text"].upper() if kind == "region" else t["text"], transform=pc, ha="center", va="center",
                rotation=t.get("rotate", 0), linespacing=1.15, zorder=4.5,
                path_effects=[] if kind == "sea" else halo, **style)

    if spec.get("scale_km"):  # true length at scale_at, measured along the geodesic east from that point
        km, (slon, slat) = spec["scale_km"], spec["scale_at"]
        elon, elat = Geodesic().direct((slon, slat), 90, km * 1000)[0][:2]
        import numpy as np
        (x0, y0), (x1, _) = proj.transform_points(pc, np.array([slon, elon]), np.array([slat, elat]))[:, :2].tolist()
        ax.plot([x0, x1], [y0, y0], color=c["ink"], lw=0.8, solid_capstyle="butt", zorder=5)
        for x in (x0, (x0 + x1) / 2, x1):
            ax.plot([x, x], [y0, y0 + (x1 - x0) * 0.025], color=c["ink"], lw=0.5, zorder=5)
        ax.text((x0 + x1) / 2, y0 - (x1 - x0) * 0.04, f"{km:,} km", ha="center", va="top",
                fontsize=sz["legend"], color=c["ink"], zorder=5)

    leg = spec.get("legend")
    if leg:
        handles = []
        items = leg.get("items", ["lines", "markers"])
        if "volumes" in items:
            handles += [Line2D([], [], color=col, lw=STYLE["route_width_pt"], label=f"Volume {v}")
                        for v, col in STYLE["volume"].items()]
        if "lines" in items:
            used = {r["style"] for r in spec.get("routes", [])}
            handles += [Line2D([], [], color=c["ink"], lw=STYLE["route_width_pt"], ls=s["dash"], label=s["label"])
                        for k, s in STYLE["line"].items() if k in used]
        if "markers" in items:
            used = {gaz[p]["reliability"] for p in shown}
            handles += [Line2D([], [], ls="", marker="o", ms=STYLE["marker_pt"], mfc=m["face"], mec=m["edge"],
                               mew=0.45, label=m["label"]) for k, m in STYLE["reliability"].items() if k in used]
        lg = ax.legend(handles=handles, loc=leg.get("at", "lower left"), fontsize=sz["legend"], frameon=True,
                       framealpha=0.92, edgecolor=c["coast"], facecolor=c["land"], borderpad=0.6,
                       handlelength=2.6, labelspacing=0.35)
        lg.get_frame().set_linewidth(0.3)
        lg.set_zorder(6)
    return fig


def build(names):
    import matplotlib
    matplotlib.use("Agg")
    setup_fonts()
    gaz = gazetteer()
    OUT.mkdir(parents=True, exist_ok=True)
    files = [DATA / f"{n}.yaml" for n in names] if names else sorted(DATA.glob("A*.yaml"))
    for f in files:
        spec = yaml.safe_load(f.read_text())
        fig = draw(spec, gaz)
        for ext in ("pdf", "svg"):  # no timestamp, so an unchanged map regenerates byte-identical
            fig.savefig(OUT / f"{spec['file']}.{ext}", metadata={"CreationDate": None} if ext == "pdf" else {"Date": None})
        fig.savefig(CACHE / f"{spec['file']}.png", dpi=200)  # review proof only
        print(f"media/maps/{spec['file']}.pdf|svg")


def self_test():
    gaz = {"a": {"id": "a", "book_name": "A", "latitude": "1", "longitude": "2", "reliability": "visited",
                 "id_confidence": "disputed"},
           "u": {"id": "u", "book_name": "U", "latitude": "", "longitude": "", "reliability": "uncertain",
                 "id_confidence": "unfixed"}}
    routes, marked = resolve({"routes": [{"vol": "I", "style": "stated", "path": ["a", [5, 6]]}],
                              "label": {"a": "n"}}, gaz)
    assert routes == [[(2.0, 1.0), (6.0, 5.0)]] and marked == ["a"]
    assert label_of("a", "n", gaz) == ("A?", "n")
    assert label_of("a", {"text": "Alpha", "pos": "s"}, gaz) == ("Alpha", "s")
    for bad in ({"routes": [{"vol": "I", "style": "stated", "path": ["u"]}]},
                {"routes": [{"vol": "IV", "style": "stated", "path": ["a"]}]},
                {"routes": [{"vol": "I", "style": "stated", "path": ["zz"]}]},
                {"label": {"a": "n"}}):
        try:
            resolve(bad, gaz)
        except ValueError:
            continue
        raise AssertionError(f"accepted {bad}")
    real = gazetteer()
    for f in sorted(DATA.glob("A*.yaml")):
        resolve(yaml.safe_load(f.read_text()), real)
    print("map.py: self-test ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    self_test() if args == ["--test"] else build(args)
