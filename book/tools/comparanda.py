#!/usr/bin/env python3
"""Source-aware lookup of non-Yule quotations in refs/ (BLD.T10; sources: plans/registry/comparanda.md).

usage (from book/):
  python3 tools/comparanda.py SOURCE "quotation"     check one quotation against one named source
  python3 tools/comparanda.py --scan [files...]      report every [“…”]{src=SOURCE} span (report only)
  python3 tools/comparanda.py --list                 sources, segment maps and status

A quotation passes only if it occurs, after normalisation, inside one segment that the registry
marks as the named witness's own text: never across a file or segment boundary, never in an editor's
preface or note, another author's text, or Yule. A source without a checked segment map, or whose
rights are not cleared, is refused rather than guessed. The OCR is uncorrected: a pass still needs
a scan check (comparanda.md). The Yule-only quotation check and the 7-gram metric (tools/yule.py,
tools/lint.py) are separate and unchanged.
"""
import re
import sys
from functools import lru_cache
from pathlib import Path

import yule

REFS = yule.REFS
# Segments are 1-based inclusive line ranges, (role, who, first, last); last=None means end of file.
# role "author" is the witness's own (translated) text; anything else never satisfies an attribution.
# segments=None: not yet mapped (notes interleaved in the OCR), so lookups are refused.
SOURCES = {
    "hayton": {"file": "hayton-bedrosian.txt", "witness": "Hayton (tr. Bedrosian)", "cleared": True,
               "segments": [("editor", "Bedrosian, front matter and tables", 1, 548),
                            ("author", "Hayton", 549, 2607),
                            ("other", "Nicholas Falcon, colophon", 2608, None)]},
    "rubruck": {"file": "rubruck-rockhill-1900.txt", "witness": "Rubruck (tr. Rockhill)", "cleared": True,
                "segments": None},  # also holds Carpini's journey and Rockhill's footnotes
    "carpini": {"file": "rubruck-rockhill-1900.txt", "witness": "Carpini (tr. Rockhill)", "cleared": True,
                "segments": None},
    "odoric": {"file": "odoric-yule-cordier-1913.txt", "witness": "Odoric (tr. Yule)", "cleared": True,
               "segments": None},
    "ibnbattuta": {"file": "ibn-battuta-lee-1829.txt", "witness": "Ibn Battuta (tr. Lee)", "cleared": True,
                   "segments": None},
    "rashid": {"file": "cathay-missions-rashid-yule-cordier-1914.txt", "witness": "Rashid al-Din (Cathay III)",
               "cleared": True, "segments": None},  # same volume: Montecorvino, Andrew of Perugia
    "wassaf": {"file": "wassaf-elliot-dowson-1871.txt", "witness": "Wassaf (Elliot–Dowson III)", "cleared": True,
               "segments": None},
    "zhaorugua": {"file": "zhao-rugua-hirth-rockhill-1911.txt", "witness": "Zhao Rugua (tr. Hirth–Rockhill)",
                  "cleared": True, "segments": None},
    "akhbar": {"file": "akhbar-renaudot-1733.txt", "witness": "Akhbar al-Sin wa'l-Hind (1733)", "cleared": False,
               "segments": None},  # excluded until translation rights are checked (BLD.T10)
}
SPAN = re.compile(r"\[[“\"]([^\]]+?)[”\"]\]\{src=([a-z]+)\}")


@lru_cache(maxsize=None)
def _segments(name):
    """[(role, who, normalised text padded with spaces)] for a mapped source."""
    s = SOURCES[name]
    lines = (REFS / s["file"]).read_text(encoding="utf-8").replace("\r", "").split("\n")
    return [(role, who, " " + " ".join(yule.norm(re.sub(r"\[[^\]]*\]", " ", "\n".join(lines[a - 1:b])))) + " ")
            for role, who, a, b in s["segments"]]


def _parts(quote, min_words):
    quote = re.sub(r"\[[^\]]*\]", " ", quote)  # editorial [insertions], as yule.find_quote
    parts = [yule.norm(p) for p in re.split(r"…|\.\.\.", quote)]
    return [" " + " ".join(p) + " " for p in parts if len(p) >= min_words]


def _in_order(parts, text):
    pos = 0
    for p in parts:
        pos = text.find(p, pos)
        if pos < 0:
            return False
        pos += len(p)
    return True


def find(quote, source, min_words=4):
    """(verdict, detail). verdict: found | wrong-source | not-found | short | unmapped | not-cleared | unknown."""
    s = SOURCES.get(source)
    if s is None:
        return "unknown", f"no source “{source}” in the registry"
    if not s["cleared"]:
        return "not-cleared", f"{s['witness']}: translation rights not checked"
    if s["segments"] is None:
        return "unmapped", f"{s['witness']}: no checked segment map for {s['file']}"
    parts = _parts(quote, min_words)
    if not parts:
        return "short", "no part of 4+ words to check"
    for role, who, text in _segments(source):
        if role == "author" and _in_order(parts, text):
            return "found", f"{who}, {s['file']} (OCR: check the scan)"
    elsewhere = [f"{who} ({role}, {SOURCES[n]['file']})" for n in SOURCES if SOURCES[n]["segments"]
                 for role, who, text in _segments(n) if (n != source or role != "author") and _in_order(parts, text)]
    if _in_order(parts, yule.joined()):
        elsewhere.append("Yule–Cordier")
    if elsewhere:
        return "wrong-source", "found only in " + "; ".join(elsewhere)
    authored = " ".join(t for r, _, t in _segments(source) if r == "author")
    have = yule.grams(authored.split(), 5)
    for p in parts:
        w = p.split()
        g = yule.grams(w, 5) or {tuple(w)}
        if p not in authored:
            cov = sum(x in have for x in g) / len(g)
            kind = "misquoted or OCR" if cov >= 0.5 else "not in this source"
            return "not-found", f"{kind} ({cov:.0%} of 5-grams match): “{p.strip()[:50]}”"
    return "not-found", "parts found, but not in order within one segment"


def scan(paths):
    bad = 0
    for path in paths:
        for ln, line in enumerate(Path(path).read_text(encoding="utf-8").split("\n"), 1):
            for m in SPAN.finditer(line):
                verdict, detail = find(m.group(1), m.group(2))
                bad += verdict != "found"
                print(f"{path}:{ln}  {m.group(2)}  {verdict}  {detail}")
    return bad


def main(argv):
    if argv[:1] == ["--list"]:
        for n, s in SOURCES.items():
            state = ("not cleared" if not s["cleared"] else "unmapped" if s["segments"] is None
                     else f"{len(s['segments'])} segments")
            print(f"{n:11} {s['witness']:40} {s['file']:45} {state}")
    elif argv[:1] == ["--scan"]:
        files = argv[1:] or sorted(str(p) for p in yule.BOOK.glob("vol-*/*.md"))
        print(f"{scan(files)} unresolved")
    elif len(argv) == 2:
        verdict, detail = find(argv[1], argv[0])
        print(f"{verdict}: {detail}")
        return verdict != "found"
    else:
        sys.exit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
