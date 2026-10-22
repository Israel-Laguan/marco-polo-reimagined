#!/usr/bin/env python3
"""Convert the manuscript's citations to the S-24 style.

usage: python3 tools/cite_convert.py --pass A [--apply] [files...]   (run from book/)

Pass A (base text):
  * Epigraph attributions -> "Marco Polo, Book 2, ch. 12 (Yule–Cordier)".
    The book and chapter come from finding the epigraph's quotation in Yule's
    main text, not from the old attribution. Epigraphs whose quotation can't be
    found are reported and left alone.
  * Roman locators in the Notes ("Book I.lxi", "Prologue xvii–xviii"):
    used as a citation -> "[@yc, 1.61]"; used as a noun in a sentence -> "YC 1.61".
    Roman locators in the narrative body are reported, not changed: they are recap
    scaffolding for the re-voice to remove.
Without --apply it prints the changes and the report (dry run).
Pass B (scholar names -> citation keys) waits on S-12's name -> key map.
"""
import argparse
import re
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import yule  # noqa: E402

BOOK = yule.BOOK
BOOKS = {"FIRST": 1, "SECOND": 2, "THIRD": 3, "FOURTH": 4, "I": 1, "II": 2, "III": 3, "IV": 4}
ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}


def roman(s):
    s = s.lower()
    return sum(-ROMAN[a] if ROMAN[a] < ROMAN.get(b, 0) else ROMAN[a] for a, b in zip(s, s[1:] + " "))


# ---------------------------------------------------------------- Yule index

@lru_cache(maxsize=None)
def chapters():
    """[(book, chapter, normalised main text, normalised Yule notes)]; book 0 = Prologue."""
    out = []
    for name, (start, end) in yule.MAIN_TEXT.items():
        lines = yule._raw(name).split("\n")[start - 1:end]
        book = 0 if name == "yule-vol1.txt" else 2
        cur = None
        for line in lines:
            s = line.strip()
            m = re.match(r"^BOOK (FIRST|SECOND|THIRD|FOURTH|IV|III|II|I)\b", s)
            if m:
                book = BOOKS[m.group(1)]
                continue
            if s.startswith("PROLOGUE"):
                cur = [0, 0, [], []]  # the unnumbered preamble before Prologue ch. 1
                out.append(cur)
                continue
            m = re.match(r"^CHAPTER ([IVXLC]+)\.$", s)
            if m:
                cur = [book, roman(m.group(1)), [], []]
                out.append(cur)
                continue
            if cur and line:
                cur[2 if not line[0].isspace() else 3].append(line)
    return [(b, c, " " + " ".join(yule.norm(" ".join(t))) + " ", " " + " ".join(yule.norm(" ".join(n))) + " ")
            for b, c, t, n in out]


def locate(quote):
    """Chapters whose main text holds every ≥4-word segment of the quote: (hits, in_notes_only)."""
    quote = re.sub(r"\[[^\]]*\]", " ", quote)
    segs = [" " + " ".join(s) + " " for s in (yule.norm(x) for x in re.split(r"…|\.\.\.", quote)) if len(s) >= 4]
    if not segs:
        return [], False
    hits = sorted({(b, c) for seg in segs for b, c, text, _ in chapters() if seg in text})
    if hits and all(any(seg in t for b, c, t, _ in chapters()) for seg in segs):
        return hits, False
    in_notes = sorted({(b, c) for seg in segs for b, c, _, notes in chapters() if seg in notes})
    return in_notes, bool(in_notes)


def span(hits):
    """'Book 2, ch. 12' / 'Prologue, chs. 17–18' for one book's chapters; None if they straddle books."""
    books = {b for b, _ in hits}
    if len(books) != 1:
        return None
    b = books.pop()
    cs = sorted(c for _, c in hits)
    if b == 0 and cs == [0]:
        return "Prologue, preamble"
    cs = [c for c in cs if c]
    where = "Prologue" if b == 0 else f"Book {b}"
    return f"{where}, ch. {cs[0]}" if cs[0] == cs[-1] else f"{where}, chs. {cs[0]}–{cs[-1]}"


# ---------------------------------------------------------------- epigraphs

ATTR = re.compile(r"^(>\s*[—–-]\s*)(.*)$")
NEW_ATTR = re.compile(r"^Marco Polo, (Book [1-4], chs?\. \d+(–\d+)?|Prologue, (chs?\. \d+(–\d+)?|preamble)) \([^)]*\)$")


def qualifier(old):
    """Keep a source qualifier such as 'Ramusio' from the old attribution."""
    m = re.search(r"\(([^)]*)\)\s*$", old)
    inner = m.group(1) if m else ""
    extra = [p.strip() for p in re.split(r"[/;]", inner) if re.fullmatch(r"\s*(Ramusio|Pipino|Pauthier|Z|F)\s*", p)]
    return "; ".join(extra + ["Yule–Cordier"])


def convert_epigraph(lines, report):
    quote = []
    for i, line in enumerate(lines):
        if line.startswith("## Notes"):
            break
        m = ATTR.match(line)
        if m and quote:
            old = m.group(2)
            if NEW_ATTR.match(old):
                return
            hits, notes_only = locate(" ".join(quote))
            where = span(hits) if hits and not notes_only else None
            if where:
                lines[i] = f"{m.group(1)}Marco Polo, {where} ({qualifier(old)})"
                report.append(("epigraph", i + 1, old, lines[i][len(m.group(1)):]))
            else:
                why = ("only in Yule's notes " + str(hits)) if notes_only else ("straddles books " + str(hits)) if hits else "quotation not found in Yule's main text"
                report.append(("epigraph: by hand", i + 1, old, why))
            return
        if line.startswith(">"):
            quote.append(line.lstrip("> "))


# ---------------------------------------------------------------- locators

LOC = re.compile(r"(?:Yule[–-]Cordier\s+)?(?:Book (I{1,3}|IV)\.|(Prologue) )([ivxlc]+)(?:[–-]([ivxlc]+))?\b")
PROSE_BEFORE = re.compile(r"\b(of|into|and|from|what|Thus|So|as|to|in|the|after|before|with)\s*$")


def locator_text(m, key):
    book = "Prol. " if m.group(2) else f"{BOOKS[m.group(1)]}."
    a = roman(m.group(3))
    rng = f"{a}–{roman(m.group(4))}" if m.group(4) else f"{a}"
    loc = f"Prol. {rng}" if m.group(2) else f"{book}{rng}"
    return f"[@yc, {loc}]" if key else f"YC {loc}"


def convert_locators(lines, report):
    in_notes = False
    for i, line in enumerate(lines):
        if line.startswith("## Notes"):
            in_notes = True
        if not LOC.search(line) or ATTR.match(line):
            continue
        if not in_notes:
            for m in LOC.finditer(line):
                report.append(("body locator: re-voice", i + 1, m.group(0), line[max(0, m.start() - 40):m.end() + 20].strip()))
            continue

        def sub(m):
            before = line[:m.start()]
            after = line[m.end():]
            cite = (not PROSE_BEFORE.search(before)) and re.match(r"\s*([.;,)]|\(|$)", after)
            new = locator_text(m, cite)
            report.append(("note locator" + ("" if cite else " (prose)"), i + 1, m.group(0), new))
            return new
        lines[i] = LOC.sub(sub, line)


# ---------------------------------------------------------------- pass B: names -> keys

NAME_MAP = BOOK / "plans" / "registry" / "name-keys.csv"
# Names that always need a title or year nearby, or that are common words.
LIST_ONLY = {"Hall"}
# Context resolvers for the names whose key depends on the Note (rule "context").
CONTEXT = {
    "Frances Wood": [(r"", "wood1995did")],
    "Moule": [(r"Quinsai|Kinsay|Hangzhou|Phoenix|palace|Palace", "moule1957quinsai"),
              (r"Christian|Nestorian|Mar Sar|Zhenjiang|Chinkiang", "moule1930christians")],
    "Allsen": [(r"hunt", "allsen2006royal"), (r"textile|commodit|nasīj|nasij|brocade|personnel", "allsen1997commodity")],
    "de Rachewiltz": [(r"Secret History", "derachewiltz2004secret"), (r"Wood|presence|silence|debate|repl", "derachewiltz1997marco")],
    "Morgan": [(r"Rubruck|edition", "jackson1990mission"), (r"survey", "morgan1986mongols")],
    "Jackson": [(r"Rubruck|edition", "jackson1990mission"), (r"Mongols and the West", "jackson2005mongols")],
}
WOOD_EXPLORER = re.compile(r"18[34]\d|Oxus|Badash|Pamir|Wakhan|lapis|Vocan|Bolor|Gordon|Trotter|Elphinstone|Moorcroft")
WOOD_DEBATE = re.compile(r"Frances|Did Marco Polo|debate|scepti|Wood vs|Wood’s (case|thesis|questions)|sceptic|1995|silence")


def load_map():
    import csv
    rows = list(csv.DictReader(NAME_MAP.open(encoding="utf-8")))
    return {r["name_as_cited"]: r for r in rows}


EXPLORER_FILES = ("ch-09-balc-badashan", "ch-10-pamier-cotan")
CURRENT = {"file": ""}


def key_for(name, row, note):
    if name == "Wood":
        if CURRENT["file"].startswith(EXPLORER_FILES) or WOOD_EXPLORER.search(note):
            return None, "VIA:wood1841personal"
        if WOOD_DEBATE.search(note):
            return "wood1995did", None
        return None, "Wood: explorer (via YC, wood1841personal) or Frances Wood — decide"
    if row["rule"] == "key":
        return row["keys"], None
    if row["rule"] == "context" and name in CONTEXT:
        for pat, key in CONTEXT[name]:
            if re.search(pat, note):
                return key, None
        return None, f"{name}: context not matched ({row['keys']})"
    return None, None


def name_rx(name):
    return re.compile(r"(?<![\w–-])" + re.escape(name) + r"(?![\w–-])")


def convert_names(lines, report, names):
    in_notes = False
    order = sorted(names, key=len, reverse=True)
    for i, line in enumerate(lines):
        if line.startswith("## Notes"):
            in_notes = True
            continue
        if not in_notes or not re.match(r"^\[\d+\]", line):
            continue
        done, taken = set(), []          # keys cited in this Note; character spans already used

        def free(a, b):
            return all(b <= x or a >= y for x, y in taken)

        # 1. parenthetical groups made only of convertible names -> [@a; @b]
        def group(m):
            items = [x.strip() for x in m.group(1).split(";")]
            keys = []
            for it in items:
                name = next((n for n in order if it == n or it == n + "’s"), None)
                k = key_for(name, names[name], line)[0] if name else None
                if not k or (name in LIST_ONLY and len(items) < 2):
                    return m.group(0)
                keys.append(k)
            done.update(keys)
            report.append(("names: group", i + 1, m.group(0), "[" + "; ".join("@" + k for k in keys) + "]"))
            return "[" + "; ".join("@" + k for k in keys) + "]"
        line = re.sub(r"\(([^()\[\]]+;[^()\[\]]+)\)", group, line)
        for m in re.finditer(r"\[@[^\]]+\]", line):
            taken.append(m.span())
        # 2. remaining mentions: Name [-@key] after the first mention in the Note
        out, pos = [], 0
        hits = []
        for name in order:
            if name == "Wood" and "Frances Wood" in names:
                pass
            for m in name_rx(name).finditer(line):
                if name == "Wood" and line[m.end():].startswith(" detail"):
                    continue  # timber, not John or Frances Wood
                if free(*m.span()):
                    hits.append((m.start(), m.end(), name)); taken.append(m.span())
        for a, b, name in sorted(hits):
            row = names[name]
            key, why = key_for(name, row, line)
            if why and why.startswith("VIA:"):
                report.append(("names: via-yc", i + 1, name, why[4:])); continue
            if why:
                report.append(("names: by hand", i + 1, name, why)); continue
            if not key:
                if row["rule"] in ("via-yc", "needs-edition"):
                    report.append((f"names: {row['rule']}", i + 1, name, row["keys"] or row["note"]))
                continue
            if name in LIST_ONLY and not re.search(r"[;(]\s*$", line[:a]) and not re.match(r"\s*[;)]", line[b:]):
                continue
            if key in done:
                continue
            end = b
            m = re.match(r"’s", line[end:])
            if m:
                end += 2
            title = re.match(r",? (\(\*[^*]+\*\)|\*[^*]+\*)", line[end:])
            if title:
                end += title.end()
            if re.match(r"\s*\[-?@", line[end:]):
                done.add(key); continue
            out.append(line[pos:end - (title.end() if title else 0)] + f" [-@{key}]")
            pos = end
            done.add(key)
            report.append(("names: key", i + 1, line[a:end], f"{name} [-@{key}]"))
        lines[i] = "".join(out) + line[pos:]


def write_report(path, log):
    """Worklist for the per-chapter .T4 pass: every mention pass B did not convert."""
    todo = [r for r in log if r[2] not in ("names: key", "names: group")]
    out = ["# Pass B worklist (S-24)", "",
           "Generated by `tools/cite_convert.py --pass B --report`. Mentions in the Notes that pass B did not convert,",
           "by file. **via-yc**: cite as reported in Yule (`Name [-@key], in [@yc, n.n]`, or `Name, in [@yc, n.n]` with no key);",
           "find the YC chapter by searching `refs/`. **needs-edition** / **by hand**: choose the work first.", ""]
    by_file = {}
    for f, ln, kind, old, what in todo:
        by_file.setdefault(f, []).append((ln, kind.replace("names: ", ""), old, what))
    for f in sorted(by_file):
        out += [f"## {f}", "", "| Line | Kind | Name | Key or note |", "|---|---|---|---|"]
        out += [f"| {ln} | {k} | {o} | {w} |" for ln, k, o, w in sorted(by_file[f])]
        out.append("")
    path.write_text("\n".join(out), encoding="utf-8")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pass", dest="which", choices=["A", "B"], required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--report", help="pass B: write the by-hand worklist to this Markdown file")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    log = []
    files = [Path(p).resolve() for p in a.files] or sorted(BOOK.glob("vol-*/*.md"))
    files = [f for f in files if f.name != "README.md"]
    names = load_map() if a.which == "B" else None
    if names:
        names["Wood"] = {"rule": "context", "keys": "wood1995did;wood1841personal", "note": ""}
    totals = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        report = []
        if a.which == "A":
            convert_epigraph(lines, report)
            convert_locators(lines, report)
        else:
            CURRENT["file"] = f.name
            convert_names(lines, report, names)
        new = "\n".join(lines)
        for kind, ln, old, what in report:
            totals[kind] = totals.get(kind, 0) + 1
            log.append((str(f.relative_to(BOOK)), ln, kind, old, what))
            print(f"{f.relative_to(BOOK)}:{ln}  [{kind}]  {old}  →  {what}")
        if a.apply and new != text:
            f.write_text(new, encoding="utf-8")
    if a.which == "B" and a.report:
        write_report(Path(a.report), log)
    print("\n" + " · ".join(f"{k}: {v}" for k, v in sorted(totals.items())))
    if not a.apply:
        print("(dry run; add --apply to write)")


if __name__ == "__main__":
    main()
