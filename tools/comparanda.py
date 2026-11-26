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
# Rockhill ranges stop at page headers and footnotes even when the translation continues.
SOURCES = {
    "hayton": {"file": "hayton-bedrosian.txt", "witness": "Hayton (tr. Bedrosian)", "cleared": True,
               "segments": [("editor", "Bedrosian, front matter and tables", 1, 548),
                            ("author", "Hayton", 549, 2607),
                            ("other", "Nicholas Falcon, colophon", 2608, None)]},
    "rubruck": {"file": "rubruck-rockhill-1900.txt", "witness": "Rubruck (tr. Rockhill)", "cleared": True,
                "partial": True,
                "segments": [
                    ("author", "Rubruck, p. 55", 5821, 5835),
                    ("editor", "Rockhill, notes to p. 55", 5839, 5875),
                    ("author", "Rubruck, p. 66", 6436, 6455),
                    ("editor", "Rockhill, notes to p. 66", 6459, 6481),
                    ("author", "Rubruck, p. 67", 6487, 6508),
                    ("editor", "Rockhill, notes to p. 67", 6512, 6533),
                    ("author", "Rubruck, p. 85", 7461, 7479),
                    ("editor", "Rockhill, notes to p. 85", 7483, 7507),
                    ("author", "Rubruck, p. 207", 13698, 13706),
                    ("author", "Rubruck, p. 207", 13711, 13732),
                    ("editor", "Rockhill, note to p. 207", 13734, 13736),
                    ("author", "Rubruck, p. 208", 13742, 13772),
                    ("editor", "Rockhill, notes to p. 208", 13774, 13779),
                    ("author", "Rubruck, p. 209", 13785, 13786),
                    ("editor", "Rockhill, continued note on p. 209", 13790, 13840),
                ]},
    "carpini": {"file": "rubruck-rockhill-1900.txt", "witness": "Carpini (tr. Rockhill)", "cleared": True,
                "partial": True,
                "segments": [
                    ("author", "Carpini, p. 18", 3979, 4000),
                    ("author", "Carpini, p. 18", 4009, 4013),
                    ("editor", "Rockhill, notes to p. 18", 4017, 4020),
                    ("author", "Carpini, p. 19", 4026, 4056),
                    ("editor", "Rockhill, notes to p. 19", 4060, 4065),
                    ("author", "Carpini, p. 20", 4073, 4101),
                    ("editor", "Rockhill, notes to p. 20", 4103, 4114),
                    ("author", "Carpini, p. 21", 4120, 4132),
                    ("editor", "Rockhill, note to p. 21", 4136, 4171),
                    ("author", "Carpini, p. 22", 4177, 4200),
                    ("editor", "Rockhill, notes to p. 22", 4204, 4218),
                    ("author", "Carpini, p. 23", 4224, 4251),
                    ("editor", "Rockhill, notes to p. 23", 4255, 4267),
                    ("other", "Narrative from Benedict the Pole, p. 38", 4918, 4952),
                    ("editor", "Rockhill, note to p. 38", 4954, 4954),
                ]},
    "odoric": {"file": "odoric-yule-cordier-1913.txt", "witness": "Odoric (tr. Yule)", "cleared": True,
               "partial": True,
               "segments": [
                   ("author", "Odoric, p. 164", 9016, 9020),
                   ("author", "Odoric, p. 164", 9024, 9030),
                   ("editor", "Yule and Cordier, notes to p. 164", 9032, 9069),
                   ("author", "Odoric, p. 192", 10660, 10661),
                   ("editor", "Yule and Cordier, notes on p. 192", 10663, 10713),
               ]},
    "ibnbattuta": {"file": "ibn-battuta-lee-1829.txt", "witness": "Ibn Battuta (tr. Lee)", "cleared": True,
                   "segments": None},
    "rashid": {"file": "cathay-missions-rashid-yule-cordier-1914.txt", "witness": "Rashid al-Din (Cathay III)",
               "cleared": True, "segments": None},  # same volume: Montecorvino, Andrew of Perugia
    "wassaf": {"file": "wassaf-elliot-dowson-1871.txt", "witness": "Wassaf (Elliot–Dowson III)", "cleared": True,
               "partial": True,
               "segments": [
                   ("author", "Wassaf, p. 32", 1856, 1863),
                   ("author", "Wassaf, p. 32", 1867, 1888),
                   ("editor", "Elliot and Dowson, notes to p. 32", 1890, 1898),
               ]},
    "zhaorugua": {"file": "zhao-rugua-hirth-rockhill-1911.txt", "witness": "Zhao Rugua (tr. Hirth–Rockhill)",
                  "cleared": True, "segments": None},
    "akhbar": {"file": "akhbar-renaudot-1733.txt", "witness": "Akhbar al-Sin wa'l-Hind (1733)", "cleared": False,
               "segments": None},  # excluded until translation rights are checked (BLD.T10)
}
SPAN = re.compile(r'\[[“"]((?:[^\[\]\n]|\[[^\[\]\n]*\])+?)[”"]\]\{src=([a-z][a-z0-9_-]*)\}')


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
    if all(len(p) < min_words for p in parts):
        return []
    return [" " + " ".join(p) + " " for p in parts if p]


def _in_order(parts, text):
    pos = 0
    for p in parts:
        pos = text.find(p, pos)
        if pos < 0:
            return False
        pos += len(p) - 1  # adjacent parts share one word-boundary space
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
            if cov < 0.5 and s.get("partial"):
                kind = "not in the checked passages"
            return "not-found", f"{kind} ({cov:.0%} of 5-grams match): “{p.strip()[:50]}”"
    return "not-found", "parts found, but not in order within one segment"


def scan(paths):
    checked = bad = 0
    for path in paths:
        for ln, line in enumerate(Path(path).read_text(encoding="utf-8").split("\n"), 1):
            for m in SPAN.finditer(line):
                verdict, detail = find(m.group(1), m.group(2))
                checked += 1
                bad += verdict != "found"
                print(f"{path}:{ln}  {m.group(2)}  {verdict}  {detail}")
    return checked, bad


def main(argv):
    if argv[:1] == ["--list"]:
        for n, s in SOURCES.items():
            state = ("not cleared" if not s["cleared"] else "unmapped" if s["segments"] is None
                     else f"{len(s['segments'])} segments")
            if s.get("partial"):
                state += " (partial)"
            print(f"{n:11} {s['witness']:40} {s['file']:45} {state}")
    elif argv[:1] == ["--scan"]:
        files = argv[1:] or sorted(str(p) for p in yule.BOOK.glob("vol-*/*.md"))
        checked, bad = scan(files)
        print(f"{checked} tagged quotations, {bad} unresolved")
    elif len(argv) == 2:
        verdict, detail = find(argv[1], argv[0])
        print(f"{verdict}: {detail}")
        return verdict != "found"
    else:
        sys.exit(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
