"""Gazetteer tooling (spike S-04): schema check, chapters column, name-usage report, and the lint name rule.

usage: python3 tools/gazetteer.py check              validate gazetteer.csv (schema, enums, ranges)
       python3 tools/gazetteer.py chapters           rewrite the `chapters` column from the manuscript
       python3 tools/gazetteer.py report [--md]      name-usage diff: non-canonical forms used per chapter

Policy (gazetteer-readme.md): `book_name` is the Yule form the chapters use; every other spelling lives in
`aliases`. In prose the book form is used throughout; a modern or alternate form may appear only as a gloss
beside the book form (first mention per chapter), never bare.
"""
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
GAZ = BOOK / "gazetteer.csv"
COLUMNS = ("id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,"
           "id_confidence,coord_check,wikipedia,chapters,notes").split(",")
LEGS = {"prologue", "outbound", "china", "maritime", "return", "other"}
RELIABILITY = {"visited", "likely_visited", "reported_only", "uncertain", "legendary"}
ID_CONFIDENCE = {"firm", "probable", "disputed", "unfixed"}
COORD_CHECK = {"wikipedia", "region", "approximate", "none"}

# Rows whose chapters cannot be told apart by form alone (same book_name, different place).
SCOPE = {
    "sinju-1": ("vol-1/",), "sinju-2": ("vol-2/",),
    "vuju-1": ("vol-2/ch-12",), "vuju-2": ("vol-2/ch-14",),
}
# Rows whose book form and modern form are identical in practice: no first-mention gloss required.
SKIP_GLOSS = {"venice", "genoa", "java", "aden", "acre"}
# Region rows are labels, not places to gloss.
SKIP_GLOSS |= {"persia", "cathay", "manzi", "turcomania", "rosia", "greater-hermenia", "lesser-hermenia", "georgiania"}
# Appear in prose as common words or inside longer names; never count a bare match as a variant.
NOT_A_VARIANT = {"Great Desert", "Male", "Lop"}


def load():
    with open(GAZ, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def aliases(row):
    return [a.strip() for a in row["aliases"].split(";") if a.strip()]


def plain(s):
    return unicodedata.normalize("NFC", s)


def form_re(form):
    return re.compile(r"(?<![\w’'-])" + re.escape(plain(form)) + r"(?![\w-])")


def chapter_id(rel):
    """vol-2/ch-12-kian-suju.md -> II-12; front-01 -> II-F1; back-01 -> II-B1."""
    vol, name = rel.split("/", 1)
    roman = {"1": "I", "2": "II", "3": "III"}[vol[-1]]
    m = re.match(r"(ch|front|back)-(\d+)", name)
    kind, n = m.groups()
    tail = n if kind == "ch" else ("F" if kind == "front" else "B") + str(int(n))
    return f"{roman}-{tail}"


def manuscript():
    return sorted(p for p in BOOK.glob("vol-*/*.md") if p.name != "README.md")


def body_paras(path):
    """Prose paragraphs before ## Notes, with quoted material removed (same filter the lint uses)."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import lint  # noqa: WPS433
    doc = lint.Doc(path)
    return [(ln, lint.strip_quotes(p)) for ln, p in doc.paras]


def is_gloss(p, start, forms):
    """True when the match at `start` sits in a gloss beside another form of the same place."""
    before = p[:start]
    m = re.search(r"(\(|—|–|/|,)\s*(?:[^()]{0,60}[/,]\s*)?$", before)
    if not m:
        return False
    head = before[:m.start()].rstrip()
    if m.group(1) == "/":  # "Kish / Qays" inside a gloss: look back to the opening bracket
        o = head.rfind("(")
        head = head[:o].rstrip() if o != -1 else head
    return any(head.endswith(f) for f in forms)


# The report and the lint rule cover the narrative chapters. Front/back matter and the modern-reception
# chapters (III-10 to III-12) legitimately use modern forms.
RULE_SKIP = ("vol-3/ch-10", "vol-3/ch-11", "vol-3/ch-12")


def in_rule_scope(rel):
    name = rel.split("/")[1]
    return name.startswith("ch-") and not rel.startswith(RULE_SKIP)


def usage(rows):
    """{row id: {file rel: {"canon": n, "gloss": {form: n}, "bare": {form: [lines]}}}}"""
    paras = {p: body_paras(p) for p in manuscript()}
    out = defaultdict(dict)
    for r in rows:
        forms = [r["book_name"]] + aliases(r)
        res = {f: form_re(f) for f in forms}
        for path, ps in paras.items():
            rel = str(path.relative_to(BOOK))
            if r["id"] in SCOPE and not any(rel.startswith(s) for s in SCOPE[r["id"]]):
                continue
            rec = {"canon": 0, "gloss": defaultdict(int), "bare": defaultdict(list)}
            for ln, p in ps:
                for f, rx in res.items():
                    for m in rx.finditer(plain(p)):
                        if f == r["book_name"]:
                            rec["canon"] += 1
                        elif f in NOT_A_VARIANT:
                            continue
                        elif is_gloss(p, m.start(), forms):
                            rec["gloss"][f] += 1
                        else:
                            rec["bare"][f].append(ln)
            if rec["canon"] or rec["gloss"] or rec["bare"]:
                out[r["id"]][rel] = rec
    return out


def needs_gloss(r):
    first = plain(r["modern_name"]).split(",")[0].split("(")[0].strip().lower()
    return r["id"] not in SKIP_GLOSS and r["modern_name"] and first != r["book_name"].lower()


# ---------------------------------------------------------------- lint hook

_CACHE = {}


def variant_forms():
    """{alias: (book_name, row id)} for forms that must not appear bare in prose (used by tools/lint.py)."""
    if "v" not in _CACHE:
        v = {}
        for r in load():
            for a in aliases(r):
                if a not in NOT_A_VARIANT and a != r["book_name"] and len(a) > 3 and " (wrong)" not in a:
                    v.setdefault(a, (r["book_name"], r["id"]))
        _CACHE["v"] = v
    return _CACHE["v"]


def bare_variants(p, rel=""):
    """Yield (alias, book_name) for non-canonical forms used bare in one prose paragraph."""
    if "rows" not in _CACHE:
        _CACHE["rows"] = {r["id"]: r for r in load()}
    rows = _CACHE["rows"]
    t = plain(p)
    for alias, (book, rid) in variant_forms().items():
        if rid in SCOPE and not any(rel.startswith(s) for s in SCOPE[rid]):
            continue
        r = rows[rid]
        forms = [r["book_name"]] + aliases(r)
        for m in form_re(alias).finditer(t):
            if not is_gloss(t, m.start(), forms):
                yield alias, book


# ---------------------------------------------------------------- commands

def cmd_check():
    rows = load()
    errs = []
    if list(rows[0].keys()) != COLUMNS:
        errs.append(f"columns differ: {list(rows[0].keys())}")
    seen, seqs = set(), set()
    for r in rows:
        i = r["id"]
        if i in seen or not re.fullmatch(r"[a-z0-9-]+", i):
            errs.append(f"{i}: bad or duplicate id")
        seen.add(i)
        if r["leg"] not in LEGS:
            errs.append(f"{i}: leg {r['leg']!r}")
        if r["reliability"] not in RELIABILITY:
            errs.append(f"{i}: reliability {r['reliability']!r}")
        if r["id_confidence"] not in ID_CONFIDENCE:
            errs.append(f"{i}: id_confidence {r['id_confidence']!r}")
        if r["coord_check"] not in COORD_CHECK:
            errs.append(f"{i}: coord_check {r['coord_check']!r}")
        if (r["coord_check"] == "none") != (not r["latitude"]):
            errs.append(f"{i}: coord_check 'none' must match blank coordinates")
        if r["wikipedia"] and not r["wikipedia"].startswith("https://en.wikipedia.org/wiki/"):
            errs.append(f"{i}: wikipedia is not an English Wikipedia URL")
        if r["volume"] not in {"1", "2", "3"}:
            errs.append(f"{i}: volume {r['volume']!r}")
        if r["sequence"] in seqs or not r["sequence"].isdigit():
            errs.append(f"{i}: bad or duplicate sequence")
        seqs.add(r["sequence"])
        la, lo = r["latitude"], r["longitude"]
        if bool(la) != bool(lo):
            errs.append(f"{i}: only one of latitude/longitude set")
        if la and not (-90 <= float(la) <= 90 and -180 <= float(lo) <= 180):
            errs.append(f"{i}: coordinates out of range")
        if not la and r["id_confidence"] not in {"unfixed", "disputed"} and r["reliability"] != "legendary":
            errs.append(f"{i}: no coordinates but id_confidence {r['id_confidence']}")
        if r["id_confidence"] == "unfixed" and la:
            errs.append(f"{i}: unfixed but has coordinates")
        if not r["notes"]:
            errs.append(f"{i}: empty notes")
    by_book = defaultdict(list)
    for r in rows:
        by_book[r["book_name"]].append(r["id"])
    for b, ids in by_book.items():
        if len(ids) > 1 and not all(i[-2] == "-" and i[-1].isdigit() for i in ids):
            errs.append(f"{b}: shared by {ids} (disambiguate with -1/-2 ids)")
    forms = defaultdict(list)
    for r in rows:
        for f in [r["book_name"]] + aliases(r):
            if f != r["book_name"] or len(by_book[r["book_name"]]) == 1:
                forms[f].append(r["id"])
    for f, ids in forms.items():
        if len(set(ids)) > 1:
            errs.append(f"form {f!r} claimed by {sorted(set(ids))}")
    for e in errs:
        print("ERROR", e)
    print(f"{len(rows)} rows, {len(errs)} problems")
    return 1 if errs else 0


def cmd_chapters():
    rows = load()
    use = usage(rows)
    for r in rows:
        files = sorted(use.get(r["id"], {}), key=lambda p: (p[:5], ("front", "ch-", "back").index(p.split("/")[1][:5].rstrip("-") + ("-" if p.split("/")[1].startswith("ch") else "")) if False else p.split("/")[1][:2] != "fr", p.split("/")[1][:2] == "ba", p))
        r["chapters"] = ";".join(chapter_id(p) for p in files if use[r["id"]][p]["canon"] or use[r["id"]][p]["gloss"]
                                 or use[r["id"]][p]["bare"])
    with open(GAZ, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    unused = [r["id"] for r in rows if not r["chapters"]]
    print(f"{len(rows)} rows; no chapter uses: {', '.join(unused) or 'none'}")
    return 0


def cmd_report(md):
    rows = load()
    use = usage(rows)
    bare_total, rows_with_bare, no_gloss = 0, 0, []
    lines = []
    for r in rows:
        files = use.get(r["id"], {})
        agg = defaultdict(list)
        for rel, rec in files.items():
            if not in_rule_scope(rel):
                continue
            for f, lns in rec["bare"].items():
                agg[f].append((chapter_id(rel), len(lns)))
        if agg:
            rows_with_bare += 1
            parts = []
            for f, fs in sorted(agg.items()):
                bare_total += sum(n for _, n in fs)
                parts.append(f"**{f}** — " + ", ".join(f"{c} ×{n}" for c, n in sorted(fs)))
            lines.append((r["book_name"], r["modern_name"] or "—", "; ".join(parts)))
        if needs_gloss(r):
            for rel, rec in files.items():
                if rec["canon"] and not rec["gloss"] and not rec["bare"] and in_rule_scope(rel):
                    no_gloss.append((r["book_name"], chapter_id(rel)))
    unused = [r["book_name"] for r in rows if not use.get(r["id"])]
    if md:
        print("# Name-usage diff (S-04)\n")
        print("`python3 tools/gazetteer.py report --md` · prose only (Notes, quotations, tables excluded). "
              "A *bare variant* is a non-canonical form used outside a gloss beside the book form.\n")
        print(f"**{rows_with_bare} places** have bare variants in the chapters (**{bare_total}** occurrences). "
              f"{len(no_gloss)} chapter-first-mentions of a book form have no gloss at all.\n")
        print("## Bare variants by place\n\n| Book form | Modern | Variants used bare (chapter ×count) |\n|---|---|---|")
        for b, m, t in lines:
            print(f"| {b} | {m} | {t} |")
        print("\n## Book forms in narrative chapters with no gloss anywhere in that chapter\n")
        g = defaultdict(list)
        for b, c in no_gloss:
            g[c].append(b)
        for c, bs in sorted(g.items(), key=lambda x: (x[0].split('-')[0].replace('III', '3').replace('II', '2').replace('I', '1'), x[0])):
            print(f"- **{c}:** {', '.join(sorted(set(bs)))}")
        print(f"\n## Rows no chapter uses\n\n{', '.join(unused) or 'none'}")
    else:
        for b, m, t in lines:
            print(f"{b:18} {t}")
        print(f"\n{rows_with_bare} places, {bare_total} bare variants; {len(no_gloss)} unglossed first mentions; unused rows: {len(unused)}")
    return 0


def main(argv):
    if not argv or argv[0] not in {"check", "chapters", "report"}:
        print(__doc__)
        return 2
    if argv[0] == "check":
        return cmd_check()
    if argv[0] == "chapters":
        return cmd_chapters()
    return cmd_report("--md" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
