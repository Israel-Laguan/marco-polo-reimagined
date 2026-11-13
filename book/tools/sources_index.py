#!/usr/bin/env python3
"""Write plans/registry/sources.md from plans/registry/bibliography.bib (S-12).

One row per entry: key, citation, status (from the % comment block directly above
the entry), access link (url or DOI), and the manuscript files that cite the key.
Run from book/:  python3 tools/sources_index.py
"""
import re
from collections import Counter
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
BIB = BOOK / "plans/registry/bibliography.bib"
OUT = BOOK / "plans/registry/sources.md"
ENTRY = re.compile(r"((?:^%[^\n]*\n)*)^@(\w+)\{([^,\s]+),\n(.*?)^\}", re.M | re.S)
FIELD = re.compile(r"^\s*(\w+)\s*=\s*\{(.*)\},?\s*$", re.M)
CLASS = {"confirmed": "confirmed", "verified": "confirmed", "dated": "confirmed",
         "unconfirmed": "unconfirmed", "claimed": "unconfirmed", "known": "known"}


def tex(s):
    s = s.replace(r"\&", "&").replace("``", "“").replace("''", "”").replace("--", "–")
    return re.sub(r"[{}]", "", s)


def names(s):
    return "; ".join(p.strip() for p in tex(s).split(" and "))


def cite(t, f):
    who = names(f["author"]) if "author" in f else ""
    for role, tag in (("editor", "ed."), ("translator", "trans.")):
        if role in f:
            who += ("; " if who else "") + f"{names(f[role])} ({tag})"
    title = tex(f.get("title", "")) + (": " + tex(f["subtitle"]) if "subtitle" in f else "")
    title = f"“{title}”" if t in ("article", "incollection") else f"*{title}*"
    parts = [who.rstrip("."), tex(f.get("date", "n.d.")), title]
    if "maintitle" in f:
        parts.append(f"In *{tex(f['maintitle'])}*, vol. {f.get('volume', '')}" + (f", pt. {f['part']}" if "part" in f else ""))
    if "journaltitle" in f:
        parts.append(f"*{tex(f['journaltitle'])}* {f.get('volume', f.get('number', ''))}".strip()
                     + (f": {tex(f['pages'])}" if "pages" in f else ""))
    if "booktitle" in f:
        parts.append(f"In *{tex(f['booktitle'])}*")
    pub = ": ".join(tex(f[k]) for k in ("location", "publisher") if k in f)
    return ". ".join(p for p in parts + [pub] if p) + "."


def chapter_ids():
    ids = {}
    for p in sorted(BOOK.glob("vol-*/*.md")):
        m = re.match(r"(ch|front|back)-(\d+)", p.name)
        if m:
            v = "I" * int(p.parent.name[-1])
            ids[p] = f"{v}-" + (m.group(2) if m.group(1) == "ch" else m.group(1)[0].upper() + str(int(m.group(2))))
    return ids


def main():
    text = BIB.read_text(encoding="utf-8")
    ids = chapter_ids()
    used = {}
    for p, cid in ids.items():
        for k in set(re.findall(r"@([\w:-]+)", p.read_text(encoding="utf-8"))):
            used.setdefault(k, []).append(cid)
    rows, counts = [], Counter()
    group, prev = "", 0
    for m in ENTRY.finditer(text):
        # a "% ---- section ----" divider ends the previous group note; skip it as a status
        if re.search(r"^%\s*-", text[prev:m.end(1)], re.M):
            group = ""
        prev = m.end()
        own = " ".join(c for l in m.group(1).splitlines() if not (c := l.lstrip("% ").strip()).startswith("-"))
        # an entry without its own comment inherits the note above the first entry of its group
        group = own or group
        comment = own or (group and f"(group note) {group}") or "no status comment"
        cls = CLASS.get(re.match(r"\(?(\w+)", comment).group(1).lower(), "see note")
        counts[cls] += 1
        f = {k: v for k, v in FIELD.findall(m.group(4))}
        link = f.get("url") or (f"https://doi.org/{f['doi']}" if "doi" in f else "")
        first, _, rest = comment.partition(" ")
        rest = rest if first.rstrip(":").lower() == cls else comment
        rows.append(f"| `{m.group(3)}` | {cite(m.group(2), f)} | **{cls}**{' · ' + rest.replace('|', '/') if rest else ''} | "
                    f"{f'[link]({link})' if link else ''} | {', '.join(used.get(m.group(3), [])) or '—'} |")
    keys = re.findall(r"^@\w+\{([^,\s]+),", text, re.M)
    assert len(rows) == len(keys), f"parsed {len(rows)} of {len(keys)} entries"
    head = ["# Sources", "",
            "Generated from `registry/bibliography.bib` by `tools/sources_index.py`; do not edit by hand. "
            "Rerun after any change to the `.bib` (run from `book/`).", "",
            "Status is the comment above each entry: **confirmed** (a record was opened: catalogue, DOI, publisher page or the text), "
            "**unconfirmed** (claimed, not checked), **known** (standard work, no record opened). "
            "Trust rules: `research/README.md`. Name → key map: `registry/name-keys.csv`.", "",
            "Totals: " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f" · **{len(rows)} entries**", "",
            "| Key | Citation | Status | Access | Cited in |", "|---|---|---|---|---|"]
    OUT.write_text("\n".join(head + sorted(rows)) + "\n", encoding="utf-8")
    print(f"{OUT.relative_to(BOOK)}: {len(rows)} entries ({dict(counts)})")


if __name__ == "__main__":
    main()
