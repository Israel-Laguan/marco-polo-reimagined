#!/usr/bin/env python3
"""Maps from gazetteer.csv + one YAML per map -> media/maps/<file>.pdf (LaTeX) and .svg (Markdown).

  tools/media/.venv/bin/python tools/media/map.py              all maps in tools/media/data/A*.yaml
  tools/media/.venv/bin/python tools/media/map.py A16 A1       just these
  tools/media/.venv/bin/python tools/media/map.py --test       self-check (no drawing)

Map YAML (see data/A16.yaml):
  id, file, width (inches, default 4.5; height follows the extent), extent [lon0, lon1, lat0, lat1], centre [lon, lat],
  projection (lambert | equal_earth, for spans over ~60 degrees of longitude),
  scale (Natural Earth resolution, 10m|50m), graticule (degrees or false), scale_km, scale_at [lon, lat]
  basemap: false                   omit Natural Earth for historical city plans
  routes: [{vol: I|II|III, style: stated|inferred|reported, path: [gazetteer id | [lat, lon], ...], arrow}]
          path ids get a marker; [lat, lon] pairs are unmarked sea/land waypoints.
  label:  {id: pos | {pos, text, offset, marker, dispute, reliability}}  offset in pt; reliability is map-specific
  places: [id, ...]                 off-route places: marker + label (default pos e)
  text:   [{text, at: [lat, lon], kind: region|sea|note, rotate}]
  markers: all | labelled          (default all; overview maps mark only the labelled places)
  legend: {at: lower left|..., items: [lines, markers, volumes]}
  areas: [{path: [[lat, lon], ...], source, colour}]  closed, approximate historical polygons
  features: [{kind: wall|reconstructed|water|gate|site, path: [[lat, lon], ...], source}]
  insets: [{bounds: [left, bottom, width, height], map: {...} | profile: {source, stops: [[x, y, label], ...]}}]
          bounds are fractions of the figure. A separate map inset may use file instead of bounds.
  layout: strip                    strip: {source, coast: [id, ...], book: [id, ...]}
          coast lists ordered reference points; book lists the narrative sequence, including unfixed names.
"""
import csv
import filecmp
import io
import math
import re
import sys
from tempfile import NamedTemporaryFile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BOOK = HERE.parent.parent
DATA = BOOK / "materials/figures/data"
OUT = BOOK / "manuscript/assets" / "maps"
CACHE = BOOK / "build/media"
STYLE = yaml.safe_load((BOOK / "materials/figures/style.yaml").read_text())
POS = {"n": (0, 1), "s": (0, -1), "e": (1, 0), "w": (-1, 0),
       "ne": (1, 1), "nw": (-1, 1), "se": (1, -1), "sw": (-1, -1)}
FEATURES = {
    "wall": ("line", "solid", "ink"),
    "reconstructed": ("line", "dashed", "ink_soft"),
    "water": ("area", "solid", "lake"),
    "gate": ("point", "solid", "ink"),
    "site": ("point", "solid", "ink_soft"),
}


def gazetteer():
    with open(BOOK / "research/gazetteer.csv", newline="", encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def plottable(row):
    return (row["latitude"] and row["longitude"] and row["id_confidence"] != "unfixed"
            and row["reliability"] in STYLE["reliability"])


def geographic_point(point):
    lat, lon = map(float, point)
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError(f"invalid geographic point: {point}")
    return lon, lat


def resolve(spec, gaz):
    """Check a map spec against the gazetteer; return (points per route, marked ids). Raises on bad ids."""
    errors, routes, marked = [], [], []
    for r in spec.get("routes", []):
        if r.get("vol") not in STYLE["volume"] or r.get("style") not in STYLE["line"]:
            errors.append(f"route {r.get('path', [])[:1]}: vol/style must be one of "
                          f"{list(STYLE['volume'])} / {list(STYLE['line'])}")
        if len(r.get("path", [])) < 2:
            errors.append("a route needs at least two points")
        pts = []
        for p in r.get("path", []):
            if isinstance(p, list):
                pts.append(geographic_point(p))
            elif p not in gaz:
                errors.append(f"unknown gazetteer id: {p}")
            elif not plottable(gaz[p]):
                errors.append(f"{p} has no plottable point (unfixed, blank or legendary)")
            else:
                pts.append(geographic_point([gaz[p]["latitude"], gaz[p]["longitude"]]))
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
    if how.get("dispute", gaz[pid]["id_confidence"] == "disputed") and "?" not in text:
        text += STYLE["disputed_suffix"]
    return text, how.get("pos", "e")


def marker_of(row, how=None):
    return "D" if (how or {}).get("dispute", row["id_confidence"] == "disputed") else "o"


def sourced_path(item, shape):
    if not item.get("source", "").strip():
        raise ValueError("historical geometry requires a source locator")
    points = [geographic_point(p) for p in item["path"]]
    if shape == "area":
        from shapely.geometry import Polygon
        if len(points) < 4 or points[0] != points[-1] or not Polygon(points).is_valid:
            raise ValueError("area requires a valid closed ring")
    elif shape == "line" and len(set(points)) < 2:
        raise ValueError("feature line requires two distinct points")
    elif shape == "point" and len(points) != 1:
        raise ValueError("point feature requires one point")
    return points


def validate(spec, gaz, *, panel=False):
    if not panel and spec.get("width", 4.5) not in (2.2, 4.5):
        raise ValueError("map width must be 2.2 or 4.5 in")
    if spec.get("layout") == "strip":
        strip = spec["strip"]
        coast, book = strip["coast"], strip["book"]
        if (not strip.get("source") or not coast or len(set(coast)) != len(coast)
                or len(set(book)) != len(book) or not set(coast) <= set(book)
                or not all(p in gaz and plottable(gaz[p]) for p in coast)
                or not all(p in gaz for p in book)):
            raise ValueError("strip requires sourced, distinct gazetteer IDs in coast and book order")
        return
    west, east, south, north = spec["extent"]
    if not (-180 <= west < east <= 180 and -90 <= south < north <= 90):
        raise ValueError("invalid extent")
    resolve(spec, gaz)
    for pid, how in (spec.get("label") or {}).items():
        if label_of(pid, how, gaz)[1] not in POS:
            raise ValueError(f"invalid label position for {pid}")
        if isinstance(how, dict) and how.get("reliability", gaz[pid]["reliability"]) not in STYLE["reliability"]:
            raise ValueError(f"invalid map reliability for {pid}")
    for area in spec.get("areas", []):
        sourced_path(area, "area")
    for feature in spec.get("features", []):
        if feature["kind"] not in FEATURES:
            raise ValueError(f"unknown feature kind: {feature['kind']}")
        sourced_path(feature, FEATURES[feature["kind"]][0])
    for inset in spec.get("insets", []):
        if ("map" in inset) == ("profile" in inset) or ("bounds" in inset) == ("file" in inset):
            raise ValueError("inset needs a map or profile and bounds or a separate output file")
        if "bounds" in inset:
            left, bottom, width, height = inset["bounds"]
            if not (0 <= left < left + width <= 1 and 0 <= bottom < bottom + height <= 1):
                raise ValueError("inset bounds must fit within the figure")
        if "map" in inset:
            child = inset["map"]
            if child.get("layout") == "strip" or child.get("insets"):
                raise ValueError("map insets must be geographic and cannot contain insets")
            validate(child, gaz, panel="bounds" in inset)
        else:
            profile = inset["profile"]
            stops = profile["stops"]
            if ("file" in inset or not profile.get("source") or len(stops) < 2
                    or any(not (math.isfinite(x) and math.isfinite(y)) for x, y, _ in stops)
                    or any(a[0] >= b[0] for a, b in zip(stops, stops[1:]))):
                raise ValueError("inset profile requires sourced, ordered stops and figure bounds")


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


def map_projection(spec):
    import cartopy.crs as ccrs

    lon0, lon1, lat0, lat1 = spec["extent"]
    clon, clat = spec.get("centre", [(lon0 + lon1) / 2, (lat0 + lat1) / 2])
    if spec.get("projection", "lambert") == "equal_earth":
        return ccrs.EqualEarth(central_longitude=clon)
    return ccrs.LambertConformal(central_longitude=clon, central_latitude=clat,
                                standard_parallels=(lat0 + (lat1 - lat0) / 6, lat1 - (lat1 - lat0) / 6),
                                cutoff=lat0 - 30)


def draw_geographic(ax, spec, gaz):
    import cartopy.crs as ccrs
    import matplotlib.patheffects as pe
    from cartopy.geodesic import Geodesic
    from matplotlib.lines import Line2D
    from shapely import union_all
    from shapely.geometry import Polygon

    routes, marked = resolve(spec, gaz)
    c, sz = STYLE["colour"], STYLE["size_pt"]
    proj = ax.projection
    geo = ccrs.Geodetic()
    ax.set_facecolor(c["sea"] if spec.get("basemap", True) else c["land"])
    ax.spines["geo"].set(linewidth=0.5, edgecolor=c["ink"])
    scale = spec.get("scale", "10m")
    pc = ccrs.PlateCarree()
    areas = spec.get("areas", [])
    land_mask = None
    if spec.get("basemap", True):
        land = list(natural_earth("physical", "land", scale, spec["extent"]))
        if areas:
            land_mask = union_all(land)
        ax.add_geometries(land, pc, facecolor=c["land"],
                          edgecolor=c["coast"], linewidth=0.25, zorder=1)
        ax.add_geometries(natural_earth("physical", "lakes", scale, spec["extent"], spec.get("lake_rank", 3)), pc,
                          facecolor=c["lake"], edgecolor=c["coast"], linewidth=0.2, zorder=1.1)
        ax.add_geometries(natural_earth("physical", "rivers_lake_centerlines", scale, spec["extent"],
                                        spec.get("river_rank", 3)),
                          pc, facecolor="none", edgecolor=c["river"], linewidth=0.35, zorder=1.2)
    for area in areas:
        polygon = Polygon(sourced_path(area, "area"))
        if land_mask is not None:
            polygon = polygon.intersection(land_mask)
        ax.add_geometries([polygon], pc, facecolor=area.get("colour", c["ink_soft"]),
                          edgecolor=c["ink_soft"], alpha=0.26, linestyle="dashed", linewidth=0.6, zorder=1.05)
    grid = spec.get("graticule", 10)
    if grid:
        gl = ax.gridlines(crs=pc, draw_labels=["left", "bottom"], linewidth=0.25, color=c["graticule"],
                          xlocs=range(-180, 181, grid), ylocs=range(-90, 91, grid),
                          x_inline=False, y_inline=False, zorder=1.5)
        gl.xlabel_style = gl.ylabel_style = {"size": sz["graticule"], "color": c["ink_soft"]}
        gl.rotate_labels = False
    for feature in spec.get("features", []):
        shape, dash, colour = FEATURES[feature["kind"]]
        points = sourced_path(feature, shape)
        xs, ys = zip(*points)
        if shape == "area":
            ax.add_geometries([Polygon(points)], pc, facecolor=c[colour],
                              edgecolor=c["river"], linewidth=0.6, zorder=2)
        elif shape == "line":
            ax.plot(xs, ys, transform=pc, color=c[colour], ls=dash, lw=0.85, zorder=2)
        else:
            ax.plot(xs, ys, "s" if feature["kind"] == "gate" else "o", transform=pc,
                    ms=3, mfc=c["land"], mec=c[colour], mew=0.6, zorder=4)

    halo = [pe.withStroke(linewidth=1.6, foreground=c["land"])]
    for r, pts in zip(spec.get("routes", []), routes):
        xs, ys = zip(*pts)
        colour = STYLE["volume"][r["vol"]]
        ax.plot(xs, ys, transform=geo, color=colour, lw=STYLE["route_width_pt"],
                ls=STYLE["line"][r["style"]]["dash"], solid_capstyle="round", dash_capstyle="round", zorder=3)
        if r.get("arrow"):
            end = tuple(b + (a - b) * 0.25 for a, b in zip(pts[-2], pts[-1]))
            ax.annotate("", xy=pts[-1], xytext=end, xycoords=pc._as_mpl_transform(ax),
                        arrowprops={"arrowstyle": "->", "lw": 0.9, "color": colour,
                                    "shrinkA": 0, "shrinkB": 0}, zorder=3)
    labels = dict(spec.get("label") or {})
    for pid in spec.get("places", []):
        labels.setdefault(pid, "e")
    shown = marked if spec.get("markers", "all") == "all" else list(labels)  # "labelled": overview maps
    visible = {p: labels[p] if isinstance(labels.get(p), dict) else {} for p in shown}
    visible = {p: how for p, how in visible.items() if how.get("marker", True)}
    reliability = {p: how.get("reliability", gaz[p]["reliability"]) for p, how in visible.items()}
    for pid, how in visible.items():
        rel = STYLE["reliability"][reliability[pid]]
        ax.plot(float(gaz[pid]["longitude"]), float(gaz[pid]["latitude"]), marker_of(gaz[pid], how), transform=pc,
                ms=STYLE["marker_pt"], mfc=rel["face"], mec=rel["edge"], mew=0.45, zorder=4)
    for pid, how in labels.items():
        text, pos = label_of(pid, how, gaz)
        dx, dy = POS[pos]
        offset = how.get("offset", 3.2) if isinstance(how, dict) else 3.2
        shift = (dx * offset, dy * offset) if isinstance(offset, (float, int)) else offset
        ax.annotate(text, (float(gaz[pid]["longitude"]), float(gaz[pid]["latitude"])),
                    xycoords=pc._as_mpl_transform(ax), xytext=shift, textcoords="offset points",
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
            used = set(reliability.values())
            handles += [Line2D([], [], ls="", marker="o", ms=STYLE["marker_pt"], mfc=m["face"], mec=m["edge"],
                               mew=0.45, label=m["label"]) for k, m in STYLE["reliability"].items() if k in used]
            if any(marker_of(gaz[p], how) == "D" for p, how in visible.items()):
                handles += [Line2D([], [], ls="", marker="D", ms=STYLE["marker_pt"],
                                   mfc=c["land"], mec=c["ink"], mew=0.45, label="disputed identification")]
        lg = ax.legend(handles=handles, loc=leg.get("at", "lower left"), fontsize=sz["legend"], frameon=True,
                       framealpha=0.92, edgecolor=c["coast"], facecolor=c["land"], borderpad=0.6,
                       handlelength=2.6, labelspacing=0.35)
        lg.get_frame().set_linewidth(0.3)
        lg.set_zorder(6)


def draw_profile(ax, profile):
    colour = STYLE["colour"]
    x, y, labels = zip(*profile["stops"])
    ax.set_facecolor(colour["land"])
    ax.plot(x, y, color=colour["river"], lw=1.4)
    ax.fill_between(x, y, min(y), color=colour["lake"])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.margins(x=0.24, y=0.55)
    ax.text(0.5, 0.93, profile.get("title", "Schematic profile"), transform=ax.transAxes,
            ha="center", va="top", fontsize=STYLE["size_pt"]["note"], color=colour["ink"])
    for i, (dx, dy, label) in enumerate(zip(x, y, labels)):
        ax.annotate(label, (dx, dy), xytext=(0, 3 if i in (0, len(x) - 1) else -5),
                    textcoords="offset points", va="bottom" if i in (0, len(x) - 1) else "top",
                    ha="center", fontsize=STYLE["size_pt"]["graticule"], color=colour["ink"])


def draw_strip(spec, gaz):
    import matplotlib.pyplot as plt

    strip = spec["strip"]
    coast, book = strip["coast"], strip["book"]
    colour, size = STYLE["colour"], STYLE["size_pt"]
    positions = {pid: i for i, pid in enumerate(coast)}
    numbers = {pid: i + 1 for i, pid in enumerate(book)}
    fig = plt.figure(figsize=(spec.get("width", 4.5), 3.2))
    ax = fig.add_axes([0.04, 0.11, 0.92, 0.83])
    ax.set_xlim(-0.8, len(coast) - 0.2)
    ax.set_ylim(-0.72, 1.0)
    ax.set_axis_off()
    ax.plot([0, len(coast) - 1], [0, 0], color=colour["coast"], lw=1.1)
    for i, pid in enumerate(coast):
        name = label_of(pid, "e", gaz)[0]
        ax.plot(i, 0, marker_of(gaz[pid]), color=colour["ink"], ms=2.7)
        ax.annotate(name, (i, 0), xytext=(0, -6 - 12 * (i % 2)), textcoords="offset points",
                    ha="right", va="top", rotation=46, fontsize=size["label"], color=colour["ink"])
        ax.annotate(str(numbers[pid]), (i, 0), xytext=(0, 5), textcoords="offset points",
                    ha="center", fontsize=size["label"], color=colour["ink"])
    for start, stop in zip(book, book[1:]):
        if start not in positions or stop not in positions:
            continue
        left, right = positions[start], positions[stop]
        bend = min(1.65, 0.25 + abs(right - left) * 0.19)
        ax.annotate("", xy=(right, 0.16), xytext=(left, 0.16),
                    arrowprops={"arrowstyle": "->", "connectionstyle": f"arc3,rad={-bend if right > left else bend}",
                                "color": STYLE["volume"]["III"], "lw": 0.75, "shrinkA": 2, "shrinkB": 2})
    ax.text(0.01, 0.98, "Numbers and arrows follow the Book", transform=ax.transAxes,
            va="top", fontsize=size["note"], color=colour["ink"])
    ax.text(0.01, 0.14, "Coastal order · east coast, around Cape Comorin, up the west coast",
            transform=ax.transAxes, fontsize=size["note"], color=colour["ink"])
    unplaced = [f"{numbers[pid]} {gaz[pid]['book_name']}" for pid in book if pid not in positions]
    if unplaced:
        ax.text(0.01, 0.04, "Unplaced · " + ", ".join(unplaced), transform=ax.transAxes,
                fontsize=size["note"], color=colour["ink"])
    return fig


def draw(spec, gaz):
    import cartopy
    import cartopy.crs as ccrs
    import matplotlib.pyplot as plt

    cartopy.config["data_dir"] = str(CACHE / "natural_earth")
    if spec.get("layout") == "strip":
        return draw_strip(spec, gaz)
    width = spec.get("width", 4.5)
    ml, mb, mr, mt = (0.26, 0.17, 0.055, 0.05) if spec.get("graticule", 10) else (0.055,) * 4
    fig = plt.figure(figsize=(width, 1))
    ax = fig.add_axes([0, 0, 1, 1], projection=map_projection(spec))
    ax.set_extent(spec["extent"], crs=ccrs.PlateCarree())
    x0, x1, y0, y1 = ax.get_extent()
    plot_width = width - ml - mr
    plot_height = plot_width * (y1 - y0) / (x1 - x0)
    height = plot_height + mb + mt
    if height > 5.4:
        raise ValueError(f"{spec['file']}: {height:.2f} in exceeds the 5.4 in limit")
    fig.set_size_inches(width, height)
    ax.set_position([ml / width, mb / height, plot_width / width, plot_height / height])
    draw_geographic(ax, spec, gaz)
    for inset in spec.get("insets", []):
        if "bounds" not in inset:
            continue
        if "map" in inset:
            panel = inset["map"]
            inset_ax = fig.add_axes(inset["bounds"], projection=map_projection(panel))
            inset_ax.set_extent(panel["extent"], crs=ccrs.PlateCarree())
            draw_geographic(inset_ax, panel, gaz)
        else:
            draw_profile(fig.add_axes(inset["bounds"]), inset["profile"])
    return fig


def save_vector(fig, target):
    # A simultaneous book build should always find a complete PDF or SVG.
    with NamedTemporaryFile(dir=target.parent, delete=False) as stream:
        pending = Path(stream.name)
        try:
            if target.suffix == ".pdf":
                fig.savefig(stream, format="pdf", metadata={"CreationDate": None})
            else:
                svg = io.BytesIO()
                fig.savefig(svg, format="svg", metadata={"Date": None})
                stream.write(re.sub(rb"[ \t]+(?=\n)", b"", svg.getvalue()))
            stream.flush()
            if target.is_file() and filecmp.cmp(pending, target, shallow=False):
                return
            pending.chmod(0o644)
            pending.replace(target)
        finally:
            pending.unlink(missing_ok=True)


def build(names):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    setup_fonts()
    gaz = gazetteer()
    OUT.mkdir(parents=True, exist_ok=True)
    files = [DATA / f"{n}.yaml" for n in names] if names else sorted(DATA.glob("A*.yaml"))
    for f in files:
        spec = yaml.safe_load(f.read_text())
        validate(spec, gaz)
        outputs = [spec, *({**i["map"], "file": i["file"]} for i in spec.get("insets", []) if "file" in i)]
        for output in outputs:
            name = output["file"]
            fig = draw(output, gaz)
            save_vector(fig, OUT / f"{name}.pdf")
            save_vector(fig, OUT / f"{name}.svg")
            fig.savefig(CACHE / f"{name}.png", dpi=200)
            plt.close(fig)
            print(f"media/maps/{name}.pdf|svg")


def self_test():
    gaz = {"a": {"id": "a", "book_name": "A", "latitude": "1", "longitude": "2", "reliability": "visited",
                 "id_confidence": "disputed"},
           "u": {"id": "u", "book_name": "U", "latitude": "", "longitude": "", "reliability": "uncertain",
                 "id_confidence": "unfixed"}}
    routes, marked = resolve({"routes": [{"vol": "I", "style": "stated", "path": ["a", [5, 6]]}],
                              "label": {"a": "n"}}, gaz)
    assert routes == [[(2.0, 1.0), (6.0, 5.0)]] and marked == ["a"]
    assert label_of("a", "n", gaz) == ("A?", "n")
    assert label_of("a", {"text": "Alpha", "pos": "s"}, gaz) == ("Alpha?", "s")
    assert marker_of(gaz["a"]) == "D"
    validate({"id": "test", "file": "test", "extent": [0, 8, 0, 8],
              "areas": [{"path": [[1, 1], [1, 2], [2, 2], [1, 1]], "source": "Figure 1"}],
              "insets": [{"profile": {"source": "Figure 2", "stops": [[0, 0, "A"], [1, 1, "B"]]},
                          "bounds": [0.1, 0.1, 0.4, 0.3]}]}, gaz)
    validate({"id": "strip", "file": "strip", "layout": "strip",
              "strip": {"coast": ["a"], "book": ["u", "a"], "source": "Chapter 1"}}, gaz)
    for invalid in (
        {"areas": [{"path": [[1, 1], [1, 2], [2, 2], [1, 1]]}]},
        {"areas": [{"path": [[1, 1], [1, 2], [1, 3], [1, 1]], "source": "Figure 1"}]},
        {"features": [{"kind": "gate", "path": [[100, 4]], "source": "Plate 3"}]},
        {"insets": [{"map": {"extent": [0, 2, 0, 2], "places": ["u"]},
                     "bounds": [0.1, 0.1, 0.4, 0.3]}]},
    ):
        try:
            validate({"id": "test", "file": "test", "extent": [0, 8, 0, 8], **invalid}, gaz)
        except ValueError:
            continue
        raise AssertionError(f"accepted {invalid}")
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
        try:
            validate(yaml.safe_load(f.read_text()), real)
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"{f.name}: {error}") from error
    print("map.py: self-test ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    self_test() if args == ["--test"] else build(args)
