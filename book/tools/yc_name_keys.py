#!/usr/bin/env python3
"""Attach bibliography keys to names in "As cited in Yule:" sentences, only where safe (APP.T6).

usage: python3 tools/yc_name_keys.py [--apply] [--log FILE]   (run from book/)

For each name in an "As cited in Yule: Name, Name [@yc, loc]" group, take its candidate keys
from `plans/registry/name-keys.csv` and read Yule's own reference at `loc`. A key is attached
(`Name [-@key]`) only when exactly one candidate qualifies:
  * Yule's text near the name carries a distinctive word of that work's title, or
  * the work is the edition Yule himself used, as decided in S-12 (EDITION_YULE_USED).
Modern translations ("use only if the Note relies on it"), shared surnames and every other
case are refused and logged. Without --apply it is a dry run; the log is always written.
"""
import argparse
import csv
import re
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cite_locate as cl  # noqa: E402

BOOK = cl.BOOK
BIB = BOOK / "plans/registry/bibliography.bib"
NAMES = BOOK / "plans/registry/name-keys.csv"
# S-12 (2026-11-10): the edition Yule used for these writers (APP.T6 entry in APP-apparatus.md).
EDITION_YULE_USED = {"Bushell": "bushell1874notes", "Gaubil": "gaubil1739histoire",
                     "De Mailla": "demailla1777histoire", "Wassaf": "hammer1856geschichte"}
SHARED = {"Baber", "Major", "Wood", "Hammer"}  # two people or two works: title word required
GENERIC = set("travels travel history histoire notes account voyage voyages journey journal report "
              "description being chinese china persian india general narrative through their about "
              "western eastern great among years other early modern geschichte dinastie ancient mongols mongol world north studien system chine marco polo generale".split())
WHY = {}
GROUP = re.compile(r"([^;]*?)\s*\[@yc, ([^\]]+)\]")


@lru_cache(maxsize=None)
def bib():
    text = BIB.read_text(encoding="utf-8")
    out = {}
    for key, body in re.findall(r"@\w+\{([^,]+),(.*?)\n\}", text, re.S):
        t = re.search(r"title\s*=\s*\{(.*?)\},?\n", body, re.S)
        out[key] = t.group(1) if t else ""
    return out


@lru_cache(maxsize=None)
def candidates():
    with NAMES.open(encoding="utf-8") as f:
        return {r["name_as_cited"]: r for r in csv.DictReader(f)}


def title_words(key):
    words = re.findall(r"[A-Za-zÀ-ÿ]{5,}", cl.fold(re.sub(r"[{}\\]", "", bib().get(key, ""))))
    return {w[:6] for w in words if w[:6] not in {g[:6] for g in GENERIC}}


def yule_text(loc):
    """Folded Yule text (main text and notes) at a locator such as '2.18', 'Prol. 17' or 'Intro. § 37'."""
    m = re.match(r"Intro\. § (\d+)", loc)
    if m:
        return next((f for n, f, _ in cl.intro_sections() if n == int(m.group(1))), "")
    m = re.match(r"(Prol\.|\d)\.?\s*(\d+)", loc)
    if not m:
        return ""
    b = 0 if m.group(1) == "Prol." else int(m.group(1))
    return next((f for bb, c, f, _ in cl.chapter_texts() if (bb, c) == (b, int(m.group(2)))), "")


def decide(name, loc):
    row = candidates().get(name)
    if not row or not row["keys"]:
        return None, "no candidate key"
    if "modern translation" in row["note"]:
        return None, "key is a modern translation; the Note relies on Yule"
    # Yule–Cordier (1903) can only cite works published by then.
    keys = [k for k in row["keys"].split(";") if k in bib() and int(re.search(r"\d{4}", k).group()) <= 1903]
    text = yule_text(loc)
    folded = cl.fold(name)
    near = " ".join(text[max(0, m.start() - 40):m.end() + 160] for m in re.finditer(re.escape(folded), text))
    if not near:
        return None, f"name not found in Yule at {loc}"
    # A title word that is the writer's own name proves nothing about which work is meant.
    words = {k: [w for w in title_words(k) if w != folded[:6] and re.search(r"\b" + w, near)] for k in keys}
    hits = [k for k in keys if words[k]]
    WHY.update(words)
    if len(hits) == 1:
        return hits[0], f"title word “{'/'.join(WHY[hits[0]])}” of {hits[0]} in Yule's reference"
    if len(hits) > 1:
        return None, "several candidate works match"
    if name in EDITION_YULE_USED and name not in SHARED and EDITION_YULE_USED[name] in keys:
        return EDITION_YULE_USED[name], "edition Yule used (S-12)"
    return None, "Yule's reference names no title matching the candidate"


def convert(line, log, where):
    i = line.find("As cited in Yule:")
    if i < 0:
        return line
    head, tail = line[:i + len("As cited in Yule:")], line[i + len("As cited in Yule:"):]

    def group(m):
        names, loc = m.group(1), m.group(2)
        parts = []
        for raw in names.split(","):
            name = raw.strip()
            if not name:
                parts.append(raw); continue
            done = re.match(r"(.+?) \[-@([^\]]+)\]$", name)
            if done:  # attached on an earlier run: keep it in the log
                log.append((where, done.group(1), loc, done.group(2), "attached (earlier run)"))
                parts.append(raw); continue
            key, why = decide(name, loc)
            log.append((where, name, loc, key or "—", why))
            parts.append(raw.replace(name, f"{name} [-@{key}]") if key else raw)
        return ",".join(parts) + f" [@yc, {loc}]"
    return head + GROUP.sub(group, tail)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--log", default="plans/status/app-t6-name-keys.md")
    a = ap.parse_args()
    log = []
    for path in sorted(BOOK.glob("vol-*/*.md")):
        lines = path.read_text(encoding="utf-8").split("\n")
        new = [convert(l, log, f"{path.relative_to(BOOK)}:{n}") for n, l in enumerate(lines, 1)]
        if a.apply and new != lines:
            path.write_text("\n".join(new), encoding="utf-8")
    attached = sum(1 for r in log if r[3] != "—")
    out = ["# APP.T6 — keys for names cited through Yule", "",
           "Generated by `tools/yc_name_keys.py`. Each row is one name in an \"As cited in Yule\" group: "
           "the key attached, or `—` with the reason it was refused.", "",
           f"**{attached} attached, {len(log) - attached} refused.**", "",
           "| Where | Name | YC | Key | Reason |", "|---|---|---|---|---|"]
    out += [f"| {w} | {n} | {loc} | {k} | {why} |" for w, n, loc, k, why in log]
    (BOOK / a.log).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{attached} attached, {len(log) - attached} refused")


if __name__ == "__main__":
    main()
