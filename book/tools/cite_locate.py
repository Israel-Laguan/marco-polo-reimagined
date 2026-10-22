#!/usr/bin/env python3
"""Find where Yule–Cordier cites a writer, for the "via YC" citations (S-24).

usage: python3 tools/cite_locate.py [--worklist plans/status/pass-b-worklist.md] [--out FILE]

For every via-yc row of the pass B worklist, search Yule's text and notes for the
writer's name, first inside the Yule chapters the manuscript chapter covers (from
`outline-volumes.md` "Beats (Book X.a–b)"), then in Yule's Introduction, then anywhere.
Writes the worklist back with three columns added: where (YC locator), scope
(in range / intro / elsewhere / not found) and Yule's own reference text.
"""
import argparse
import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cite_convert as cc  # noqa: E402
import yule  # noqa: E402

BOOK = yule.BOOK
VOL_IDS = {"vol-1": "I", "vol-2": "II", "vol-3": "III"}
# How Yule spells names the Notes write differently.
ALIASES = {
    "Ibn Baṭṭūṭa": ["Ibn Batuta", "Ibn Batutah", "Batuta"], "Ibn Battuta": ["Ibn Batuta", "Batuta"],
    "Rashid": ["Rashiduddin", "Rashid"], "Rashīd": ["Rashiduddin", "Rashid"], "Wassaf": ["Wassáf", "Wassaf"],
    "Hiuen Tsang": ["Hiuen Tsang"], "Fa-hian": ["Fa-hian", "Fahian"], "Makrizi": ["Makrizi", "Makrízí"],
    "Kazwini": ["Kazwini", "Kazwíní"], "Edrisi": ["Edrisi"], "Idrīsī": ["Edrisi"], "Juvaini": ["Juwaini", "Juvaini"],
    "Juvainī": ["Juwaini", "Juvaini"], "Masʿūdī": ["Mas’udi", "Masudi"], "Mas’udi": ["Mas’udi", "Masudi"],
    "Abulfeda": ["Abulfeda"], "Abū’l-Fidā": ["Abulfeda"], "John Wood": ["Wood"], "Wood": ["Wood"],
    "De Mailla": ["De Mailla", "Mailla"], "D’Ohsson": ["D’Ohsson", "d’Ohsson"], "Houtum-Schindler": ["Houtum-Schindler", "Schindler"],
    "De Barros": ["De Barros", "Barros"], "Della Valle": ["Della Valle"], "Plano Carpini": ["Carpini"],
    "Ma Twan-lin": ["Ma Twan-lin"], "’Izzat Ullah": ["’Izzat-Ullah", "Izzat Ullah", "’Izzat Ullah"],
    # Yule's transliterations of Chinese, Mongolian, Arabic and Persian sources
    "Yuan shi": ["Yuen-shi", "Yuen shi", "Yuan-shi", "Yuen Shi"], "Yuan Shi": ["Yuen-shi", "Yuen shi", "Yuan-shi"],
    "Ch’ue keng lu": ["Ch’ue keng lu", "Ch'ue keng lu"], "Ch'ue keng lu": ["Ch’ue keng lu", "Ch'ue keng lu"],
    "Mengliang lu": ["Mêng-liang-lu", "Meng-liang-lu"], "Altan Tobchi": ["Altan tobchi", "Altan Tobchi"],
    "Sanang Sechen": ["Sanang Setzen", "Sanang Sechen"], "al-Bīrūnī": ["Biruni", "Al Biruni", "Al-Biruni"],
    "Yāḳūt": ["Yakut", "Yāqūt"], "Ain-i-Akbari": ["Ain-i-Akbari", "Aín Akbari", "Akbari"],
    "Titsingh": ["Titsingh", "Titsing"], "Pridham": ["Pridham"], "de Sacy": ["De Sacy", "de Sacy"],
    "Tsung tien": ["Tsung tien", "Tsung mao tien"], "Thackston": ["Thackston"], "Boyle": ["Boyle"], "Gibb": ["Gibb"],
    "Book of Prophecies": ["Libro de las Profecías", "Book of Prophecies"], "Marāṣid": ["Marasid", "Marāṣid"],
}


def fold(s):
    s = unicodedata.normalize("NFKD", s.replace("’", "'"))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


@lru_cache(maxsize=None)
def chapter_texts():
    """[(book, chapter, folded raw text incl. notes, raw text)] in reading order."""
    out = []
    for name, (start, end) in yule.MAIN_TEXT.items():
        lines = yule._raw(name).split("\n")[start - 1:end]
        book = 0 if name == "yule-vol1.txt" else 2
        cur = None
        for line in lines:
            s = line.strip()
            m = re.match(r"^BOOK (FIRST|SECOND|THIRD|FOURTH|IV|III|II|I)\b", s)
            if m:
                book = cc.BOOKS[m.group(1)]
                continue
            if s.startswith("PROLOGUE"):
                cur = [0, 0, []]; out.append(cur); continue
            m = re.match(r"^CHAPTER ([IVXLC]+)\.$", s)
            if m:
                cur = [book, cc.roman(m.group(1)), []]; out.append(cur); continue
            if cur is not None:
                cur[2].append(line)
    return [(b, c, fold(" ".join(t)), re.sub(r"\s+", " ", " ".join(t))) for b, c, t in out]


@lru_cache(maxsize=None)
def intro_sections():
    """Yule's Introduction (vol. 1, before the Prologue), split at its numbered paragraphs."""
    lines = yule._raw("yule-vol1.txt").split("\n")[5100:yule.MAIN_TEXT["yule-vol1.txt"][0] - 1]
    out, cur = [], None
    for line in lines:
        m = re.match(r"^ ?(\d{1,3})\. [A-Z]", line)
        if m:
            cur = [int(m.group(1)), []]; out.append(cur)
        if cur:
            cur[1].append(line)
    return [(n, fold(" ".join(t)), re.sub(r"\s+", " ", " ".join(t))) for n, t in out]


@lru_cache(maxsize=None)
def ranges():
    """Manuscript chapter id (e.g. 'II-6') -> list of (book, chapter) it covers."""
    text = (BOOK / "outline-volumes.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"### Ch\. ([IV]+-\d+)[^\n]*\n\*\*Beats \(Book ([IV]+)\.([ivxlc]+)(?:[–-]([ivxlc]+))?", text):
        cid, book, a, b = m.groups()
        bk = cc.BOOKS[book]
        out[cid] = [(bk, c) for c in range(cc.roman(a), cc.roman(b or a) + 1)]
    out.update({"I-1": [(0, 0)], "I-2": [(0, c) for c in range(1, 10)], "I-3": [(0, c) for c in range(10, 19)],
                "III-9": [(0, 17), (0, 18)], "II-15": [(4, c) for c in range(1, 40)]})
    return out


def chapter_id(path):
    vol = VOL_IDS[path.parent.name]
    m = re.match(r"ch-(\d+)", path.name)
    return f"{vol}-{int(m.group(1))}" if m else None


def _pats(name):
    """Case-sensitive, word-bounded: names are capitalised in Yule's notes, common words are not."""
    return [re.compile(r"(?<![\w])" + re.escape(a) + r"(?![\w])") for a in ALIASES.get(name, [name])]


def locate(name, path):
    pats = _pats(name)
    want = ranges().get(chapter_id(path) or "", [])

    def snippet(raw, m):
        return raw[max(0, m.start() - 60):m.start() + 110].strip()
    for b, c, folded, raw in chapter_texts():
        if (b, c) in want:
            for p in pats:
                m = p.search(raw)
                if m:
                    return cc.locator_text_for(b, c), "in range", snippet(raw, m)
    for n, folded, raw in intro_sections():
        for p in pats:
            m = p.search(raw)
            if m:
                return f"YC Intro. § {n}", "intro", snippet(raw, m)
    for b, c, folded, raw in chapter_texts():
        for p in pats:
            m = p.search(raw)
            if m:
                return cc.locator_text_for(b, c), "elsewhere", snippet(raw, m)
    return "", "not found", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", default=str(BOOK / "plans" / "status" / "pass-b-worklist.md"))
    ap.add_argument("--out")
    a = ap.parse_args()
    src = Path(a.worklist)
    out, path, counts = [], None, {}
    for line in src.read_text(encoding="utf-8").split("\n"):
        if line.startswith("## "):
            path = BOOK / line[3:].strip()
        if line.startswith("| Line | Kind | Name | Key or note |"):
            line += " Where in YC | Scope | Yule's reference |"
        elif line.startswith("|---|---|---|---|") and not line.endswith("---|---|---|---|---|---|---|"):
            line += "---|---|---|"
        elif re.match(r"^\| \d+ \| ", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells[1] == "via-yc":
                loc, scope, ref = locate(cells[2], path)
            else:
                loc, scope, ref = "", "—", ""
            counts[scope] = counts.get(scope, 0) + 1
            line = "| " + " | ".join(cells[:4] + [loc, scope, ref.replace("|", "/")]) + " |"
        out.append(line)
    Path(a.out or src).write_text("\n".join(out), encoding="utf-8")
    print(counts)


if __name__ == "__main__" and "--apply-via-yc" not in sys.argv:
    main()


# ---------------------------------------------------------------- pass C: add "As cited in Yule" sentences

# Locator hits checked by hand and found to be ordinary words or other people.
FALSE_HITS = {("vol-2/ch-07-tebet-carajan.md", "Salt"), ("vol-3/ch-01-ships-chipangu.md", "Major")}
NO_HIT_NAMES = {"Relations"}          # the Arab Relations: Yule's hits are a French book title
# Primary sources whose key is a modern translation the Notes do not rely on.
PRIMARY = {"Rubruck", "Ibn Baṭṭūṭa", "Ibn Battuta", "Pegolotti", "Juvaini", "Juvainī", "Ma Huan",
           "Hiuen Tsang", "Odoric", "Marignolli", "Montecorvino", "Duhalde"}


def yc_cite(loc):
    return "[@yc, " + loc[len("YC "):] + "]"


def apply_via_yc(worklist, write):
    import csv
    keys = {r["name_as_cited"]: r["keys"] for r in csv.DictReader((BOOK / "plans/registry/name-keys.csv").open(encoding="utf-8"))}
    todo, path = {}, None
    for line in Path(worklist).read_text(encoding="utf-8").split("\n"):
        if line.startswith("## "):
            path = line[3:].strip()
        m = re.match(r"^\| (\d+) \| via-yc \| ([^|]+) \| [^|]* \| ([^|]+) \| (in range|intro) \|", line)
        if m and (path, m.group(2).strip()) not in FALSE_HITS and m.group(2).strip() not in NO_HIT_NAMES:
            todo.setdefault(path, {}).setdefault(int(m.group(1)), []).append((m.group(2).strip(), m.group(3).strip()))
    changed = 0
    for rel, by_line in sorted(todo.items()):
        f = BOOK / rel
        lines = f.read_text(encoding="utf-8").split("\n")
        for ln, items in by_line.items():
            text = lines[ln - 1]
            if not re.match(r"^\[\d+\]", text) or "As cited in Yule:" in text:
                continue
            seen, groups = set(), {}
            for name, loc in sorted(items, key=lambda x: text.find(x[0])):
                if name in seen:
                    continue
                seen.add(name)
                # Names only: one surname can be two people (Baber = the emperor Babur in Vol. I,
                # E. C. Baber in Vol. II), so per-work keys are added at each chapter's .T4.
                groups.setdefault(loc, []).append(name)
            parts = [", ".join(names) + " " + yc_cite(loc) for loc, names in groups.items()]
            new = text.rstrip() + (" " if text.rstrip().endswith((".", ")", "]")) else ". ") + "As cited in Yule: " + "; ".join(parts) + "."
            if write:
                lines[ln - 1] = new
            else:
                print(f"{rel}:{ln}\n   + As cited in Yule: {'; '.join(parts)}.")
            changed += 1
        if write:
            f.write_text("\n".join(lines), encoding="utf-8")
    print(f"{changed} Note lines {'changed' if write else 'to change'}")


if __name__ == "__main__" and "--apply-via-yc" in sys.argv:
    apply_via_yc(BOOK / "plans/status/pass-b-worklist.md", "--write" in sys.argv)
