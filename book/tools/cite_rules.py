"""Citation-style checks for the lint (spike S-24). Registered by tools/lint.py.

Each check takes (doc, ctx) and yields (severity, line, message), like the checks in lint.py.
"""
import re
from functools import lru_cache
from pathlib import Path

BIB = Path(__file__).resolve().parent.parent / "plans" / "registry" / "bibliography.bib"

CHECKS = ["cite_keys", "roman_locators", "epigraph_credit"]

KEY = re.compile(r"(?<![\w.])-?@([A-Za-z][\w:.#$%&+?<>~/-]*\w)")
ROMAN_LOC = re.compile(r"\bBook (?:I{1,3}|IV)\.[ivxlc]+\b|\bPrologue [ivxlc]+\b")
POLO_CREDIT = re.compile(r"^Marco Polo, (Book [1-4], chs?\. \d+(–\d+)?|Prologue, (chs?\. \d+(–\d+)?|preamble)) \([^)]*\)$")
OTHER_CREDIT = re.compile(r"\(\d{4}\)|\*\((adapted|tradition)\)\*\s*$")


@lru_cache(maxsize=None)
def bib_keys():
    if not BIB.exists():
        return frozenset()
    return frozenset(re.findall(r"^@\w+\{([^,\s]+),", BIB.read_text(encoding="utf-8"), re.M))


def c_cite_keys(doc, ctx):
    keys = bib_keys()
    for i, line in enumerate(doc.lines):
        for m in KEY.finditer(line):
            if m.group(1) not in keys:
                yield "error", i + 1, f"citation key @{m.group(1)} is not in plans/registry/bibliography.bib"


def c_roman_locators(doc, ctx):
    for i, line in enumerate(doc.lines):
        for m in ROMAN_LOC.finditer(line):
            yield "error", i + 1, f"old locator “{m.group(0)}”: use [@yc, 1.61] / YC 1.61 (run tools/cite_convert.py --pass A)"


def c_epigraph_credit(doc, ctx):
    for ln, line in doc.epigraph:
        m = re.match(r"^[—–-]\s*(.*)$", line)
        if m and not (POLO_CREDIT.match(m.group(1)) or OTHER_CREDIT.search(m.group(1))):
            yield "error", ln, ("epigraph credit not in S-24 form (“Marco Polo, Book 2, ch. 12 (Yule–Cordier)”, "
                                "a dated non-Polo source, or *(adapted)* / *(tradition)*)")
