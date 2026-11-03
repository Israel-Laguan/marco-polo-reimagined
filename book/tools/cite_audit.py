#!/usr/bin/env python3
"""Audit how the manuscript cites its sources (S-24).

usage: python3 tools/cite_audit.py [--examples N] [files...]   (run from book/)

Counts each citation form that the S-24 style conversion has to touch:
epigraph attributions, base-text locators, mentions of the base text,
scholars named with or without a title or year, and names that are
ambiguous (two different people or a common word).
"""
import argparse
import collections
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent

SCHOLARS = ["Larner", "Vogel", "Haw", "Wood", "Pelliot", "Moule", "Rossabi", "Allsen",
            "Rachewiltz", "Critchley", "Olschki", "Benedetto", "Jackson", "Morgan",
            "Needham", "Franke", "Dutschke", "Bushell", "Baber", "Steinhardt", "Pauthier",
            "Gaubil", "Mailla", "Bretschneider", "Palladius", "Hammer"]
# Same surname, different people or a common word: never convert these by script.
AMBIGUOUS = {
    "Wood": "John Wood (Oxus, 1838/1841) or Frances Wood (1995)",
    "May": "Timothy May, or the month",
    "Jackson": "Peter Jackson (Mongols; Rubruck ed.), or others",
    "Morgan": "David Morgan (The Mongols; Rubruck ed.), or others",
}

EPIGRAPH = re.compile(r"^\s*>\s*[—–-]\s*(.*)$")
LOCATOR = re.compile(r"\bBook (?:I{1,3}|IV)\.[ivxlc]+\b")
BOOK_ONLY = re.compile(r"\bBook (?:I{1,3}|IV)\b(?![.\w])")
PROLOGUE = re.compile(r"\bPrologue(?: [ivxlc]+(?:[–-][ivxlc]+)?)?")
BASE = re.compile(r"\bYule[–-]Cordier\b")
YEAR = re.compile(r"\b1[5-9]\d\d\b|\b20[0-2]\d\b")


def classify_epigraph(text):
    if LOCATOR.search(text):
        return "epigraph: Book N.roman"
    if re.search(r"\bBook (?:I{1,3}|IV),", text):
        return "epigraph: Book N, chapter title"
    if "Prologue" in text:
        return "epigraph: Prologue"
    return "epigraph: free text"


def audit(files, n_examples):
    count = collections.Counter()
    examples = collections.defaultdict(list)
    per_name = collections.Counter()

    def hit(kind, text, f, ln):
        count[kind] += 1
        if len(examples[kind]) < n_examples:
            examples[kind].append(f"{f.relative_to(BOOK)}:{ln}  {text.strip()[:100]}")

    notes = 0
    for f in files:
        in_notes = False
        for ln, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## Notes"):
                in_notes = True
            if in_notes and re.match(r"^\[\d+\]", line):
                notes += 1
            m = EPIGRAPH.match(line)
            if m:
                hit(classify_epigraph(m.group(1)), m.group(1), f, ln)
                continue
            for m in LOCATOR.finditer(line):
                hit("locator: Book N.roman", line[max(0, m.start() - 30):m.end() + 30], f, ln)
            for m in BOOK_ONLY.finditer(line):
                hit("locator: Book N only", line[max(0, m.start() - 30):m.end() + 30], f, ln)
            for m in PROLOGUE.finditer(line):
                hit("locator: Prologue", line[max(0, m.start() - 30):m.end() + 30], f, ln)
            for _ in BASE.finditer(line):
                count["mention: Yule–Cordier"] += 1
            for name in SCHOLARS + list(AMBIGUOUS):
                for m in re.finditer(rf"\b{name}\b", line):
                    after = line[m.end():m.end() + 60]
                    per_name[name] += 1
                    if name in AMBIGUOUS:
                        hit(f"scholar: ambiguous ({name})", line[max(0, m.start() - 20):m.end() + 50], f, ln)
                    elif re.match(r"[,’']?s?\s*\*[^*]+\*", after):
                        hit("scholar: name + italic title", line[m.start():m.end() + 60], f, ln)
                    elif YEAR.match(after.lstrip(" (")):
                        hit("scholar: name + year", line[m.start():m.end() + 20], f, ln)
                    else:
                        count["scholar: name only"] += 1

    print(f"files {len(files)} · notes {notes}\n")
    for kind, n in sorted(count.items()):
        print(f"{n:5}  {kind}")
        for e in examples.get(kind, []):
            print(f"         {e}")
    print("\nmentions per name:")
    for name, n in per_name.most_common():
        flag = f"   ← ambiguous: {AMBIGUOUS[name]}" if name in AMBIGUOUS else ""
        print(f"{n:5}  {name}{flag}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--examples", type=int, default=3)
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = [Path(p).resolve() for p in a.files] or sorted(BOOK.glob("vol-*/*.md"))
    files = [f for f in files if f.name != "README.md"]
    audit(files, a.examples)


if __name__ == "__main__":
    main()
