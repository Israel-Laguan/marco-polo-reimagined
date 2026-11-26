"""Gazetteer tooling: schema check, chapter usage, naming lint, and place tables.

usage: python3 tools/gazetteer.py check              validate gazetteer.csv (schema, enums, ranges)
       python3 tools/gazetteer.py chapters           rewrite the `chapters` column from the manuscript
       python3 tools/gazetteer.py report [--md]      name-usage diff: non-canonical forms used per chapter
       python3 tools/gazetteer.py tables <1|2|3>     print the front-matter place tables for one volume

Policy (gazetteer-readme.md): `book_name` is the Yule form the chapters use; every other spelling lives in
`aliases`. In prose the book form is used throughout; a modern or alternate form may appear only as a gloss
beside the book form (first mention per chapter), never bare.
"""
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from paths import MANUSCRIPT as BOOK, RESEARCH

GAZ = RESEARCH / "gazetteer.csv"
COLUMNS = ("id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,"
           "id_confidence,coord_check,wikipedia,chapters,notes").split(",")
LEGS = {"prologue", "outbound", "china", "maritime", "return", "other"}
RELIABILITY = {"visited", "likely_visited", "reported_only", "uncertain", "legendary"}
ID_CONFIDENCE = {"firm", "probable", "disputed", "unfixed"}
COORD_CHECK = {"wikipedia", "region", "approximate", "none"}

TABLE_GROUPS = {
    "1": (
        "prologue and Black Sea / Volga hinge",
        "outbound from Acre into Persia",
        "deserts, high valleys, Tarim, Tangut, court",
    ),
    "2": (
        "capital approaches and west / southwest circuit",
        "Manzi corridor to the haven",
        "other places in the Book",
    ),
    "3": (
        "island and Southeast Asian road",
        "India, west shores, return hinge",
    ),
}
ROMAN_VOLUMES = {"1": "I", "2": "II", "3": "III"}

# Rows whose chapters cannot be told apart by form alone (same book_name, different place).
SCOPE = {
    "sinju-1": ("vol-1/",), "sinju-2": ("vol-2/",),
    "vuju-1": ("vol-2/ch-12",), "vuju-2": ("vol-2/ch-14",),
    # The similarly named Yellow River and Sea of Azov places have no map rows.
    "caiju": ("vol-2/ch-12",), "tana": ("vol-3/",),
}
# Rows whose book form and modern form are identical in practice: no first-mention gloss required.
SKIP_GLOSS = {"venice", "genoa", "java", "aden", "acre"}
# Region rows are labels, not places to gloss.
SKIP_GLOSS |= {"persia", "cathay", "manzi", "turcomania", "rosia", "greater-hermenia", "lesser-hermenia", "georgiania"}
# Common terms and names of distinct features that appear in their own right.
NOT_A_VARIANT = {"Great Desert", "Male", "Lop", "Jurchen", "Calachan"}


def load():
    with open(GAZ, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def aliases(row):
    return [a.strip() for a in row["aliases"].split(";") if a.strip()]


def plain(s):
    return unicodedata.normalize("NFC", s)


def form_re(form):
    return re.compile(r"(?<![\w’'-])" + re.escape(plain(form)) + r"(?![\w-])")


def canonical_rel(rel):
    rel = rel.removeprefix("proposed-voice/")
    if rel.endswith("/proposed.md"):
        rel = rel[:-len("/proposed.md")] + ".md"
    if rel == "vol-3/colophon-and-closing.md":
        rel = "vol-3/ch-12-reliability-essay.md"
    return rel


def in_place_scope(row, rel):
    rel = canonical_rel(rel)
    prefixes = SCOPE.get(row["id"])
    return prefixes is None or rel.startswith(prefixes)


def chapter_id(rel):
    """vol-2/ch-12-kian-suju.md -> II-12; front-01 -> II-F1; back-01 -> II-B1."""
    vol, name = rel.split("/", 1)
    roman = ROMAN_VOLUMES[vol[-1]]
    m = re.match(r"(ch|front|back)-(\d+)", name)
    kind, n = m.groups()
    tail = n if kind == "ch" else ("F" if kind == "front" else "B") + str(int(n))
    return f"{roman}-{tail}"


def manuscript():
    return sorted(p for p in BOOK.glob("vol-*/*.md")
                  if p.name not in {"README.md", "back-02-glossary.md"})


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
    rel = canonical_rel(rel)
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
            if not in_place_scope(r, rel):
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


def place_prose(paragraph):
    """Expose names inside Markdown emphasis while preserving their boundaries."""
    return plain(paragraph).replace("*", " ")


def gloss_window(text, end):
    possessive = re.match(r"[’']s\b", text[end:])
    if possessive:
        end += possessive.end()
    following = re.match(
        r"[ \t]*\(([^()]*(?:\([^()]*\)[^()]*)*)\)"
        r"|[ \t]*[—–][ \t]*([^.!?;—–]*)"
        r"|[ \t]*,[ \t]*([^,.!?;—–]*)",
        text[end:],
    )
    if following:
        group = following.lastindex
        return end + following.start(group), end + following.end(group)
    return end, end


def gloss_forms(row):
    modern = re.split(r"\s*[,(/]| at ", row["modern_name"], maxsplit=1)[0].strip()
    qualifiers = re.findall(r"\(([^()]+)\)", row["modern_name"])
    return {form for form in [modern, *qualifiers, *aliases(row)] if form and form != row["book_name"]}


def gloss_key(text):
    text = unicodedata.normalize("NFD", text).replace("’", "'")
    return "".join(c for c in text if not unicodedata.combining(c)).casefold()


def valid_gloss(text, row):
    key = gloss_key(text)
    return any(form_re(gloss_key(form)).search(key) for form in gloss_forms(row))


def book_mentions(text, name):
    for match in form_re(name).finditer(text):
        desert = (text[:match.start()].endswith("Desert of ")
                  or text[match.end():].casefold().startswith(" desert"))
        if name != "Lop" or not desert:
            yield match


def missing_glosses(rows, rel, paragraphs):
    """Yield the first unglossed mention of each applicable place in a chapter."""
    prepared = [(ln, place_prose(p)) for ln, p in paragraphs]
    for row in rows:
        if not in_place_scope(row, rel) or not needs_gloss(row):
            continue
        name = row["book_name"]
        for ln, paragraph in prepared:
            match = next(book_mentions(paragraph, name), None)
            if not match:
                continue
            start, end = gloss_window(paragraph, match.end())
            if not valid_gloss(paragraph[start:end], row):
                yield ln, row
            break


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
    t = place_prose(p)
    nested = None
    for alias, (book, rid) in variant_forms().items():
        if not in_place_scope(rows[rid], rel):
            continue
        for match in bare_alias_matches(t, alias, book):
            if nested is None:
                nested = place_gloss_spans(t, rows.values(), rel)
            if not any(start <= match.start() and match.end() <= end for start, end in nested):
                yield alias, book


def place_gloss_spans(text, rows, rel):
    spans = []
    for row in rows:
        if not in_place_scope(row, rel):
            continue
        for match in book_mentions(text, row["book_name"]):
            start, end = gloss_window(text, match.end())
            if start < end and valid_gloss(text[start:end], row):
                spans.append((start, end))
    return spans


def bare_alias_matches(text, alias, book):
    matches = list(form_re(alias).finditer(text))
    if not matches:
        return
    heads = list(form_re(book).finditer(text))
    allowed = [head.span() for head in heads]
    allowed.extend(gloss_window(text, head.end()) for head in heads)
    for match in matches:
        if not any(start <= match.start() and match.end() <= end for start, end in allowed):
            yield match


# ---------------------------------------------------------------- commands

def table_group(row):
    if row["volume"] == "1":
        if row["leg"] == "prologue":
            return 0
        return 1 if int(row["sequence"]) <= 400 else 2
    if row["volume"] == "2":
        if row["id"] in {"rosia", "cauly", "chorcha", "cachar-modun"}:
            return 2
        if row["id"] == "manzi":
            return 1
        return 0 if int(row["sequence"]) <= 1070 else 1
    return 0 if int(row["sequence"]) <= 1670 else 1


def place_table_row(row):
    # Use sentence punctuation followed by a new sentence, so "c. 1295" and
    # lower-case abbreviations within the opening sentence survive.
    role = re.split(r"(?<!\bc)(?<!\bvol)(?<!\bpp)(?<!\bv)\.(?=\s+[A-Z])",
                    row["notes"], maxsplit=1)
    fields = [row["book_name"], row["modern_name"] or "—", role[0] + ("." if len(role) > 1 else "")]
    return "| " + " | ".join(field.replace("|", r"\|") for field in fields) + " |"


def cmd_tables(volume):
    rows = sorted((row for row in load() if row["volume"] == volume),
                  key=lambda row: int(row["sequence"]))
    blocks = []
    for group, heading in enumerate(TABLE_GROUPS[volume]):
        entries = [place_table_row(row) for row in rows if row["latitude"] and table_group(row) == group]
        if entries:
            blocks.append("\n".join([
                f"### Place table — {heading}",
                "",
                f"| Book name | Modern | Role in Vol. {ROMAN_VOLUMES[volume]} |",
                "|-----------------|-------------------------|----------------------------------------|",
                *entries,
            ]))
    unfixed = [row["book_name"] for row in rows if not row["latitude"]]
    if unfixed:
        blocks.append("*Places without a map fix:* " + ", ".join(unfixed) + ".")
    print("\n\n".join(blocks))
    return 0

def cmd_check():
    rows = load()
    errs = []
    if not rows:
        print("ERROR gazetteer is empty")
        return 1
    if list(rows[0].keys()) != COLUMNS:
        errs.append(f"columns differ: {list(rows[0].keys())}")
    seen, seqs = set(), set()
    for r in rows:
        if None in r or None in r.values():
            errs.append(f"{r['id']}: wrong number of columns")
            continue
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
    complete = [r for r in rows if None not in r and None not in r.values()]
    for r in complete:
        by_book[r["book_name"]].append(r["id"])
    for b, ids in by_book.items():
        if len(ids) > 1 and not all(i[-2] == "-" and i[-1].isdigit() for i in ids):
            errs.append(f"{b}: shared by {ids} (disambiguate with -1/-2 ids)")
    forms = defaultdict(list)
    for r in complete:
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
    hits = defaultdict(lambda: defaultdict(Counter))
    no_gloss = []
    for path in manuscript():
        rel = str(path.relative_to(BOOK))
        if not in_rule_scope(rel):
            continue
        chapter = chapter_id(rel)
        paragraphs = body_paras(path)
        for _, paragraph in paragraphs:
            for alias, _ in bare_variants(paragraph, rel):
                row_id = variant_forms()[alias][1]
                hits[row_id][alias][chapter] += 1
        no_gloss.extend((row["book_name"], chapter) for _, row in missing_glosses(rows, rel, paragraphs))

    bare_total = 0
    lines = []
    for r in rows:
        variants = hits.get(r["id"])
        if variants:
            parts = []
            for form, by_chapter in sorted(variants.items()):
                bare_total += sum(by_chapter.values())
                parts.append(f"**{form}** — " + ", ".join(f"{c} ×{n}" for c, n in sorted(by_chapter.items())))
            lines.append((r["book_name"], r["modern_name"] or "—", "; ".join(parts)))
    rows_with_bare = len(lines)
    use = usage(rows)
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
        print("\n## First mentions without a gloss\n")
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
    if not argv or argv[0] not in {"check", "chapters", "report", "tables"}:
        print(__doc__)
        return 2
    if argv[0] == "check":
        return cmd_check()
    if argv[0] == "chapters":
        return cmd_chapters()
    if argv[0] == "tables":
        if len(argv) != 2 or argv[1] not in TABLE_GROUPS:
            print("usage: gazetteer.py tables <1|2|3>", file=sys.stderr)
            return 2
        return cmd_tables(argv[1])
    return cmd_report("--md" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
