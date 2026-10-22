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


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pass", dest="which", choices=["A"], required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = [Path(p).resolve() for p in a.files] or sorted(BOOK.glob("vol-*/*.md"))
    files = [f for f in files if f.name != "README.md"]
    totals = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        report = []
        convert_epigraph(lines, report)
        convert_locators(lines, report)
        new = "\n".join(lines)
        for kind, ln, old, what in report:
            totals[kind] = totals.get(kind, 0) + 1
            print(f"{f.relative_to(BOOK)}:{ln}  [{kind}]  {old}  →  {what}")
        if a.apply and new != text:
            f.write_text(new, encoding="utf-8")
    print("\n" + " · ".join(f"{k}: {v}" for k, v in sorted(totals.items())))
    if not a.apply:
        print("(dry run; add --apply to write)")


if __name__ == "__main__":
    main()
