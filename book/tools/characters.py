"""Character registry tooling (spike S-05): schema check, ages and co-presence per plate, prompt cues, the
chapters field, the name-usage report, and the lint name rule for people.

usage: python3 tools/characters.py check             validate characters.yaml and character-cards.yaml
       python3 tools/characters.py ages [--md]       age of every figure in every plate scene; co-presence check
       python3 tools/characters.py cue <id> <year>   [PERIOD] lines for a plate prompt (card + age + dress)
       python3 tools/characters.py chapters          rewrite each person's `chapters` field from the manuscript
       python3 tools/characters.py report [--md]     name usage: non-canonical forms of people per chapter

Policy (plans/registry/characters.md): `book_name` is the form the prose uses (Yule's form where Polo names the
person, else the modern English form). Variants in `aliases` appear only as a gloss beside the book form, once per
chapter; `also` holds legitimate other names and titles, which are never flagged.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gazetteer  # noqa: E402

BOOK = Path(__file__).resolve().parent.parent
REG = BOOK / "plans" / "registry"
PEOPLE = REG / "characters.yaml"
CARDS = REG / "character-cards.yaml"
FIELDS = "id book_name aliases also gloss born died dates group role relations book_says verify chapters".split()
GROUPS = {"polo", "venice", "church", "levant", "mongol", "yuan", "song", "ilkhanate", "golden-horde", "legend",
          "reception"}
REGIONS = {"europe", "levant", "golden-horde", "central-asia", "ilkhanate", "china", "sea"}
TRADITIONS = {"gothic", "ldm", "ilkhanid", "yuan", "song"}
SPIKES = re.compile(r"S-\d\d")
# Files where a person's form means something else (I-12's *Argons* are a people of Tenduc, not the Ilkhan).
SCOPE_OUT = {"arghun": ("vol-1/ch-12",)}

_CACHE = {}


def in_scope(pid, rel):
    return not any(rel.startswith(s) for s in SCOPE_OUT.get(pid, ()))


def load():
    if "p" not in _CACHE:
        _CACHE["p"] = yaml.safe_load(PEOPLE.read_text(encoding="utf-8"))["people"]
    return _CACHE["p"]


def load_cards():
    return yaml.safe_load(CARDS.read_text(encoding="utf-8"))


def by_id():
    return {p["id"]: p for p in load()}


def years(y):
    return (y, y) if isinstance(y, int) else tuple(y)


# ---------------------------------------------------------------- check

def cmd_check():
    people, data = load(), load_cards()
    errs, ids = [], set()
    for p in people:
        i = p.get("id", "?")
        if list(p) != FIELDS:
            errs.append(f"{i}: fields differ from {FIELDS}")
        if i in ids or not re.fullmatch(r"[a-z0-9-]+", i):
            errs.append(f"{i}: bad or duplicate id")
        ids.add(i)
        if p["group"] not in GROUPS:
            errs.append(f"{i}: group {p['group']!r}")
        for k in ("born", "died"):
            if p[k] is not None and not isinstance(p[k], int):
                errs.append(f"{i}: {k} must be a year or null")
        if p["born"] and p["died"] and p["born"] > p["died"]:
            errs.append(f"{i}: born after died")
        if not p["dates"] or not p["role"]:
            errs.append(f"{i}: empty dates or role")
        for s in p["verify"]:
            if not SPIKES.fullmatch(s):
                errs.append(f"{i}: verify {s!r} is not a spike id")
        if p["book_name"] in p["aliases"] or p["book_name"] in p["also"]:
            errs.append(f"{i}: book_name repeated in aliases/also")
    forms = defaultdict(set)
    for p in people:
        for f in [p["book_name"]] + p["aliases"] + p["also"]:
            forms[f].add(p["id"])
    errs += [f"form {f!r} claimed by {sorted(s)}" for f, s in forms.items() if len(s) > 1]
    places = {f for r in gazetteer.load() for f in [r["book_name"]] + gazetteer.aliases(r)}
    errs += [f"form {f!r} ({sorted(forms[f])[0]}) is also a gazetteer place form" for f in forms if f in places]
    for c in data["cards"]:
        if c["id"] not in ids:
            errs.append(f"card {c['id']}: no such person")
        if set(c["traditions"]) - TRADITIONS:
            errs.append(f"card {c['id']}: unknown tradition {set(c['traditions']) - TRADITIONS}")
        for d in c["dress"]:
            if d["from"] > d["to"]:
                errs.append(f"card {c['id']}: dress range {d['from']}–{d['to']}")
    for who, legs in data["itinerary"].items():
        if who not in ids:
            errs.append(f"itinerary {who}: no such person")
        for a, b, regs in legs:
            if a > b or set(regs) - REGIONS:
                errs.append(f"itinerary {who}: bad leg {a}–{b} {regs}")
    for s in data["scenes"]:
        for f in s["figures"] + s.get("absent", []) + s.get("not_shown", []):
            if f not in ids:
                errs.append(f"scene {s['plate']}: no such person {f}")
        if s["region"] not in REGIONS:
            errs.append(f"scene {s['plate']}: region {s['region']!r}")
    problems = [m for row in scene_rows(data) for m in row["problems"]]
    for e in errs:
        print("ERROR", e)
    for m in problems:
        print("ERROR", m)
    print(f"{len(people)} people, {len(data['cards'])} cards, {len(data['scenes'])} scenes, "
          f"{len(errs) + len(problems)} problems")
    return 1 if errs or problems else 0


# ---------------------------------------------------------------- ages and co-presence

def age(p, y0, y1):
    if not p["born"]:
        return "?"
    a, b = y0 - p["born"], y1 - p["born"]
    return f"c. {a}" if a == b else f"c. {a}–{b}"


def regions_in(itin, y):
    return {r for a, b, regs in itin for r in regs if a <= y <= b}


def could_be_there(p, itin, y, region):
    """True / False / None (unknown) for one year."""
    if (p["born"] and y < p["born"]) or (p["died"] and y > p["died"]):
        return False
    if itin is None:
        return None
    regs = regions_in(itin, y)
    return None if not regs else region in regs


def scene_rows(data=None):
    data = data or load_cards()
    ppl, itin = by_id(), data["itinerary"]
    out = []
    for s in data["scenes"]:
        y0, y1 = years(s["year"])
        span = range(y0, y1 + 1)
        row = {"scene": s, "ages": [], "problems": [], "unproven": []}
        for f in s["figures"]:
            p = ppl[f]
            row["ages"].append((p["book_name"], age(p, y0, y1)))
            verdicts = [could_be_there(p, itin.get(f), y, s["region"]) for y in span]
            if all(v is False for v in verdicts):
                row["problems"].append(f"scene {s['plate']}: {p['book_name']} cannot be in {s['region']} in "
                                       f"{y0}{'' if y0 == y1 else '–' + str(y1)} (dates or itinerary)")
        for f in s.get("absent", []):
            p = ppl[f]
            verdicts = [could_be_there(p, itin.get(f), y, s["region"]) for y in span]
            if any(v is True for v in verdicts):
                row["problems"].append(f"scene {s['plate']}: {p['book_name']} is marked absent but could be there")
            elif any(v is None for v in verdicts):
                row["unproven"].append(p["book_name"])
        out.append(row)
    return out


def cmd_ages(md):
    rows = scene_rows()
    if md:
        print("| Plate | Scene | Src | Year | Figures (age) | Must not show |\n|---|---|---|---|---|---|")
    # "(text)": the person was in the region, but the text does not put them in the scene.
    for r in rows:
        s = r["scene"]
        y0, y1 = years(s["year"])
        yr = str(y0) if y0 == y1 else f"{y0}–{y1}"
        figs = ", ".join(f"{n} ({a})" for n, a in r["ages"]) or "—"
        absent = ", ".join([by_id()[f]["book_name"] for f in s.get("absent", [])]
                           + [by_id()[f]["book_name"] + " (text)" for f in s.get("not_shown", [])]) or "—"
        if md:
            print(f"| {s['plate']} | {s['title']} | {s['src']} | {yr} | {figs} | {absent} |")
        else:
            print(f"{s['plate']:9} {yr:9} {figs}" + (f"   not: {absent}" if absent != "—" else ""))
        for m in r["problems"]:
            print(("> **Problem:** " if md else "  PROBLEM ") + m)
        if r["unproven"] and not md:
            print(f"  note: absence of {', '.join(r['unproven'])} rests on the text, not on the itinerary")
    bad = sum(len(r["problems"]) for r in rows)
    if not md:
        print(f"\n{len(rows)} scenes, {bad} co-presence problems")
    return 1 if bad else 0


def cmd_cue(pid, year):
    data, p = load_cards(), by_id().get(pid)
    card = next((c for c in data["cards"] if c["id"] == pid), None)
    if not p or not card:
        print(f"no card for {pid!r}")
        return 2
    dress = [d for d in card["dress"] if d["from"] <= year <= d["to"]]
    print(f"[PERIOD] {p['book_name']}, {age(p, year, year)} in {year}: {card['house']}.")
    for d in dress:
        print(f"         Dress ({d['where']}): {d['dress']}.")
    for a in card["attributes"]:
        print(f"         {a[0].upper() + a[1:]}.")
    if card["avoid"]:
        print(f"[AVOID]  {'; '.join(card['avoid'])}")
    if not dress:
        print(f"         (no dress line covers {year}: extend the card before prompting)")
    return 0


# ---------------------------------------------------------------- usage in the manuscript

def forms_of(p, kinds=("book_name", "aliases", "also")):
    out = []
    for k in kinds:
        out += [p[k]] if k == "book_name" else p[k]
    return out


def usage():
    """{person id: {rel: {"canon": n, "gloss": n, "bare": {form: [lines]}}}} over prose paragraphs."""
    paras = {p: gazetteer.body_paras(p) for p in gazetteer.manuscript()}
    out = defaultdict(dict)
    for person in load():
        canon = [person["book_name"]] + person["also"]
        res = {f: gazetteer.form_re(f) for f in forms_of(person)}
        for path, ps in paras.items():
            rel = str(path.relative_to(BOOK))
            if not in_scope(person["id"], rel):
                continue
            rec = {"canon": 0, "gloss": 0, "bare": defaultdict(list)}
            for ln, para in ps:
                t = gazetteer.plain(para)
                spans = long_spans(t)
                for f, rx in res.items():
                    for m in rx.finditer(t):
                        if inside(m, f, spans):
                            continue
                        if f in canon:
                            rec["canon"] += 1
                        elif gazetteer.is_gloss(t, m.start(), forms_of(person)):
                            rec["gloss"] += 1
                        else:
                            rec["bare"][f].append(ln)
            if rec["canon"] or rec["gloss"] or rec["bare"]:
                out[person["id"]][rel] = rec
    return out


def cmd_chapters():
    use = usage()
    lines, cur = PEOPLE.read_text(encoding="utf-8").split("\n"), None
    for n, line in enumerate(lines):
        m = re.match(r"- id: (\S+)", line)
        if m:
            cur = m.group(1)
        elif cur and line.startswith("  chapters:"):
            files = sorted(use.get(cur, {}), key=order)
            lines[n] = f'  chapters: "{";".join(gazetteer.chapter_id(f) for f in files)}"'
    PEOPLE.write_text("\n".join(lines), encoding="utf-8")
    unused = [p["id"] for p in load() if not use.get(p["id"])]
    print(f"{len(load())} people; no chapter names: {', '.join(unused) or 'none'}")
    return 0


def order(rel):
    vol, name = rel.split("/")
    return vol, {"fr": 0, "ch": 1, "ba": 2}[name[:2]], name


def cmd_report(md):
    use, rows, no_gloss = usage(), [], []
    for p in load():
        agg = defaultdict(list)
        for rel, rec in sorted(use.get(p["id"], {}).items(), key=lambda x: order(x[0])):
            if not gazetteer.in_rule_scope(rel):
                continue
            for f, lns in rec["bare"].items():
                agg[f].append((gazetteer.chapter_id(rel), len(lns)))
            if p["gloss"] and rec["canon"] and not rec["gloss"] and not rec["bare"]:
                no_gloss.append((gazetteer.chapter_id(rel), p["book_name"]))
        if agg:
            rows.append((p, agg))
    total = sum(n for _, agg in rows for fs in agg.values() for _, n in fs)
    if md:
        print("# Character name-usage diff (S-05)\n")
        print("`python3 tools/characters.py report --md` · prose of the narrative chapters (III-10 to III-12, "
              "front and back matter excluded; Notes, quotations and tables excluded). A *bare variant* is a "
              "non-canonical form used outside a gloss beside the book form.\n")
        print(f"**{len(rows)} people** have bare variants (**{total}** occurrences); {len(no_gloss)} chapter "
              "first mentions of a book form that needs a gloss have none.\n")
        print("## Bare variants by person\n\n| Book form | Gloss | Variants used bare (chapter ×count) |\n|---|---|---|")
        for p, agg in rows:
            parts = [f"**{f}** — " + ", ".join(f"{c} ×{n}" for c, n in fs) for f, fs in agg.items()]
            print(f"| {p['book_name']} | {p['gloss'] or '—'} | {'; '.join(parts)} |")
        print("\n## Book forms with no gloss anywhere in the chapter\n")
        g = defaultdict(list)
        for c, b in no_gloss:
            g[c].append(b)
        for c in sorted(g, key=lambda c: (len(c.split("-")[0]), c)):
            print(f"- **{c}:** {', '.join(sorted(set(g[c])))}")
    else:
        for p, agg in rows:
            print(f"{p['book_name']:12} " + "; ".join(f"{f}: " + ", ".join(f"{c}×{n}" for c, n in fs)
                                                     for f, fs in agg.items()))
        print(f"\n{len(rows)} people, {total} bare variants; {len(no_gloss)} unglossed first mentions")
    return 0


# ---------------------------------------------------------------- lint hook (tools/lint.py c_name_policy)

def long_spans(t):
    """Spans of every multi-word form of every person in `t`, so a short form inside a longer one
    ("Ahmad" in "Ahmad Tegüder", "Acomat" in "Acomat Soldan") is not counted on its own."""
    if "long" not in _CACHE:
        _CACHE["long"] = [(f, gazetteer.form_re(f)) for p in load() for f in forms_of(p) if " " in f]
    return [(m.start(), m.end(), f) for f, rx in _CACHE["long"] for m in rx.finditer(t)]


def inside(m, form, spans):
    return any(s <= m.start() and m.end() <= e and f != form for s, e, f in spans)


def bare_variants(p, rel=""):
    """Yield (alias, book_name) for a person's variant used bare in one prose paragraph."""
    t = gazetteer.plain(p)
    spans = long_spans(t)
    for person in load():
        if not in_scope(person["id"], rel):
            continue
        for a in person["aliases"]:
            for m in gazetteer.form_re(a).finditer(t):
                if not inside(m, a, spans) and not gazetteer.is_gloss(t, m.start(), forms_of(person)):
                    yield a, person["book_name"]


def glossed_at(t, m, person):
    """True when a gloss bracket or dash follows the book form, or a title form that starts with it
    ("Acomat Soldan (Ahmad Tegüder)")."""
    end = max([m.start() + len(f) for f in person["also"] if t.startswith(f, m.start())] + [m.end()])
    return bool(re.match(r"\s*[(—–]", t[end:end + 6]))


def needs_gloss(rel=""):
    return [p for p in load() if p["gloss"] and in_scope(p["id"], rel)]


def main(argv):
    cmds = {"check", "ages", "cue", "chapters", "report"}
    if not argv or argv[0] not in cmds or (argv[0] == "cue" and len(argv) != 3):
        print(__doc__)
        return 2
    if argv[0] == "check":
        return cmd_check()
    if argv[0] == "ages":
        return cmd_ages("--md" in argv)
    if argv[0] == "cue":
        return cmd_cue(argv[1], int(argv[2]))
    if argv[0] == "chapters":
        return cmd_chapters()
    return cmd_report("--md" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
