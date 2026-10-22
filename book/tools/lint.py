"""Acceptance lint for the manuscript (spike S-02; thresholds from S-01 / VOICE-GUIDE v2).

usage: python3 tools/lint.py [files...] [-v] [--json | --md] [--build-ramusio-manifest]

With no files, lints the 49 manuscript files (vol-*/*.md except the volume READMEs).
Errors are mechanical rule breaks and decide pass/fail; warnings are heuristics
for the human voice read. Exit status 1 when any file has an error.
"""
import argparse
import csv
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import yule  # noqa: E402

BOOK = yule.BOOK
MANIFEST = BOOK / "tools" / "ramusio-manifest.json"
BASELINE_COMMIT = "1204156"  # first-draft import; source for the Ramusio manifest

# Thresholds. PROVISIONAL values wait on S-03 (apparatus) and S-04 (gazetteer).
T = {
    "verbatim_pct": 15, "ngram": 7,
    "anyway": 1, "hinges": 3, "attribution_verb": 4,
    "aside_words": 80, "asides": 4,
    "quote_words": 25, "quotes_chapter": 8, "quotes_paragraph": 2,
    "length": {"narrative": (1800, 3200), "essay": (0, 3500)},
    "avg_sentence": 25,
    "stub_note_words": 6,
    "forbidden_markers": "★☆",      # S-03: allowed set is ✓ ~ ✗ ◇ ?
    "ramusio_note_label": r"(?:Ramusio|Pipino|Jacopo|Zelada)-only",   # S-03: provenance label, not a marker
    "tags": {"V", "R", "M", "reception"},   # S-03: Vols. II-III narrative/essay files only
}

ARCH = r"\b(hath|doth|foison|certes|sundry|whilst|thereof|insomuch|wherein|to wit|existeth|natheless|fain|wot|wist|trowed|gat)\b|[’']tis\b"
FIRST = (r"\b(I will tell|I tell you|I assure you|I can tell you|I can assure|I have been telling|I am going to|"
         r"I will relate|What more shall I say|I should have told|And why should I|I will quit|Now I will|"
         r"I ought to mention|Let me tell you|we will quit|We could tell you)\b")
HINGES = (r"Marco Polo (starts by )?narrat|\bPolo narrates\b|[Aa]ccording to the [Bb]ook|next he mentions|"
          r"Then (Polo|he) describes|Tradition has it")
ATTR_SUBJ = r"\b(?:Polo|Marco|[Hh]e|the [Bb]ook|the text|Ramusio|Yule|Rustichello|Pipino)"
ATTR_VERBS = ("says|explains|adds|insists|notes|tells|describes|mentions|reports|records|claims|"
              "remarks|observes|writes|relates|declares|assures|gives")
ATTR = ATTR_SUBJ + r"\s+(?:also\s+|then\s+|only\s+|simply\s+)?(" + ATTR_VERBS + r")\b(?!\s+nothing)"
RECAP_OPEN = r"^(The Book has|The book has|So far the Book|Having (told|shown))"
RECAP_CLOSE = r"Here the chapter|For the present|has done what|stops short of|the chapter has|This chapter has"
ASIDE_EXIT = (r"\b(Anyway|[Ss]o much for|[Bb]ack to|[Tt]o return|[Rr]eturning to|[Ll]et us return|"
              r"[Ee]nough (of|about)|Now the Book|Now back)\b")
SCAFFOLD = [  # (pattern, flags); searched in the whole file, Notes included
    (r"\bSoft\b[^.:\n]{0,40}:", 0), (r"/workspace", 0), (r"\bdrafter\b", re.I), (r"(^|[.;:]\s+)Narrate\b", 0),
    (r"\b(the|campaign) outline\b|\boutline([’'-]s|-volumes|-summary|\s+[IV]+-\d+|\s+beats?|\s+end matter)", re.I),
    (r"SERIES-STATUS", 0), (r"placeholder", re.I), (r"dispute hook", re.I), (r"first-draft", re.I),
    (r"asides? (has|have) to be honest", re.I), (r"honesty restores", re.I), (r"project gazetteer", re.I),
    (r"\bsoft ID\b", re.I), (r"\bopen questions? \d", re.I),
    (r"\b(likely_visited|reported_only)\b", 0),
    (r"[Gg]azetteer:?[^.;\n]{0,40}\*(visited|likely visited|uncertain|reported only)\*", 0),
]
NAME_STOP = {"Book", "Books", "Notes", "Note", "Polo", "Marco", "Kaan", "Khan", "Great", "Ramusio", "Yule"}


# ---------------------------------------------------------------- parsing

def kind_of(rel):
    name = Path(rel).name
    if name == "README.md":
        return None
    if name.startswith(("front-", "back-")):
        return "frontback"
    return "essay" if "reliability-essay" in name else "narrative"


class Doc:
    def __init__(self, path, text=None):
        self.path = Path(path)
        self.rel = str(self.path.resolve().relative_to(BOOK)) if text is None else str(path)
        self.kind = kind_of(self.rel)
        self.text = self.path.read_text(encoding="utf-8") if text is None else text
        self.lines = self.text.split("\n")
        end = next((i for i, l in enumerate(self.lines) if l.startswith("## Notes")), len(self.lines))
        self.epigraph = [(i + 1, l.lstrip("> ")) for i, l in enumerate(self.lines[:end]) if l.startswith(">")]
        self.paras = []
        for i, l in enumerate(self.lines[:end]):
            s = l.strip()
            if not s or s.startswith(("#", ">", "**[", "---", "|", "!")):
                continue
            self.paras.append((i + 1, re.sub(r"^(- |\d+\. )", "", s)))
        self.notes = {}
        for i, l in enumerate(self.lines[end:], start=end):
            m = re.match(r"^\[(\d+)\]\s*(.*)", l)
            if m:
                self.notes.setdefault(int(m.group(1)), []).append((i + 1, m.group(2)))
        self.has_notes = end < len(self.lines)


def strip_quotes(t):
    t = re.sub(r"^\*[^*].*\*(\s*\[\d+\])?$", " ", t)
    return re.sub(r"\*?“[^”]*”\*?|\*?\"[^\"]*\"\*?", " ", t)


def marked_quotes(p, block=True):
    """Marked Yule quotations in a paragraph: *“…”* spans, or (block=True) the whole paragraph in italics."""
    m = re.match(r"^\*([^*].*[^*])\*(\s*\[\d+\])?$", p)
    if m and block and not p.startswith("*Caption"):
        return [m.group(1).strip("“”\"")]
    return re.findall(r"\*[“\"]([^”\"]+)[”\"]\*", p)


def nwords(t):
    return len(re.findall(r"[\w’'-]+", t))


def sentences(t):
    return [s for s in re.split(r"(?<=[.!?])[”’\")\]]*\s+(?=[A-Z“\"(*—])", t) if nwords(s)]


# ---------------------------------------------------------------- Ramusio

def ramusio_hits(para, passages=None):
    """Ramusio passages a (near-verbatim) paragraph reproduces: >= 3 shared 8-grams,
    or the whole normalised passage as a substring for short (5-9 word) passages."""
    passages = passages or _passage_index()
    w = yule.norm(para)
    pg = yule.grams(w, 8)
    flat = " " + " ".join(w) + " "
    hits = []
    for idx, (text, pw, g8) in enumerate(passages):
        if (len(pw) >= 10 and len(g8 & pg) >= 3) or (5 <= len(pw) < 10 and " " + " ".join(pw) + " " in flat):
            hits.append(idx)
    return hits


_PI = None


def _passage_index():
    global _PI
    if _PI is None:
        _PI = [(t, yule.norm(t), yule.grams(yule.norm(t), 8)) for t in yule.ramusio_passages()]
    return _PI


def build_manifest(rels):
    """Per file: the Ramusio passages its first draft (BASELINE_COMMIT) reproduces."""
    out = {}
    for rel in rels:
        try:
            src = subprocess.run(["git", "show", f"{BASELINE_COMMIT}:book/{rel}"], cwd=BOOK,
                                 capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            continue
        doc = Doc(rel, text=src)
        found = sorted({h for _, p in doc.paras for h in ramusio_hits(p)})
        if found:
            out[rel] = [yule.ramusio_passages()[h][:80] for h in found]
    MANIFEST.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


# ---------------------------------------------------------------- checks
# Each check takes (doc, ctx) and yields (severity, line, message); ctx collects metrics.

def c_verbatim(doc, ctx):
    w, worst = [], []
    for ln, p in doc.epigraph + doc.paras:
        pw = yule.norm(p)
        cov = yule.coverage(pw, T["ngram"])
        w += cov
        if len(pw) >= 60 and sum(cov) / len(pw) >= 0.7:
            worst.append(f"L{ln} {100 * sum(cov) // len(pw)}%")
    pct = round(100 * sum(w) / max(1, len(w)))
    ctx["verbatim"] = pct
    if pct > T["verbatim_pct"]:
        yield "error", None, f"verbatim Yule {pct}% (> {T['verbatim_pct']}%); worst: {', '.join(worst[:5]) or '—'}"


def _per_line(doc, pattern, flags=0):
    for ln, p in doc.paras:
        for m in re.finditer(pattern, strip_quotes(p), flags):
            yield ln, m.group(0)


def c_first_person(doc, ctx):
    for ln, m in _per_line(doc, FIRST):
        yield "error", ln, f"Book first person outside quotes: “{m}”"


def c_archaism(doc, ctx):
    for ln, m in _per_line(doc, ARCH, re.I):
        yield "error", ln, f"archaism outside quotes: “{m}”"


def c_you_must_know(doc, ctx):
    for ln, m in _per_line(doc, r"[Yy]ou must know"):
        yield "error", ln, "“You must know” outside quotes"


def c_budgets(doc, ctx):
    anyway = list(_per_line(doc, r"\bAnyway\b"))
    if len(anyway) > T["anyway"]:
        yield "error", anyway[0][0], f"“Anyway” ×{len(anyway)} (> {T['anyway']}) at L{', L'.join(str(l) for l, _ in anyway)}"
    hinges = list(_per_line(doc, HINGES))
    if len(hinges) > T["hinges"]:
        yield "error", hinges[0][0], f"formula hinges ×{len(hinges)} (> {T['hinges']})"
    verbs = {}
    for ln, m in _per_line(doc, ATTR):
        v = m.split()[-1]
        verbs.setdefault(v, []).append(ln)
    for v, lns in sorted(verbs.items()):
        if len(lns) > T["attribution_verb"]:
            yield "error", lns[0], f"attribution verb “{v}” ×{len(lns)} (> {T['attribution_verb']})"


def c_asides(doc, ctx):
    asides = [(i, ln, p) for i, (ln, p) in enumerate(doc.paras) if p.startswith("—")]
    ctx["asides"] = len(asides)
    if len(asides) > T["asides"]:
        yield "error", asides[0][1], f"{len(asides)} asides (> {T['asides']})"
    for i, ln, p in asides:
        n = nwords(re.sub(r"\[\d+\]", "", p))
        if n > T["aside_words"]:
            yield "error", ln, f"aside {n} words (> {T['aside_words']})"
        last = (sentences(p) or [p])[-1]
        if re.search(ASIDE_EXIT, strip_quotes(last)):
            yield "error", ln, "aside ends in an exit formula"
        if i + 1 < len(doc.paras) and re.match(r"(" + ASIDE_EXIT + r")", doc.paras[i + 1][1]):
            yield "error", doc.paras[i + 1][0], "paragraph after an aside announces the return"


def c_quotes(doc, ctx):
    total = 0
    for ln, p in doc.paras:
        qs = marked_quotes(p)
        total += len(qs)
        if len(qs) > T["quotes_paragraph"]:
            yield "error", ln, f"{len(qs)} marked quotations in one paragraph (> {T['quotes_paragraph']})"
        for q in qs:
            if nwords(q) > T["quote_words"]:
                yield "error", ln, f"marked quotation {nwords(q)} words (> {T['quote_words']}): “{q[:40]}…”"
    ctx["quotes"] = total
    if total > T["quotes_chapter"]:
        yield "error", None, f"{total} marked quotations (> {T['quotes_chapter']})"


def c_quote_verify(doc, ctx):
    body_sev = "error" if doc.kind == "narrative" else "warning"
    items = [(ln, q, "error", "epigraph") for ln, l in doc.epigraph for q in re.findall(r"[“\"]([^”\"]+)[”\"]", l)]
    items += [(ln, q, body_sev, "quotation") for ln, p in doc.paras
              for q in marked_quotes(p, block=doc.kind != "frontback")]
    for ln, q, sev, what in items:
        verdict, missing, cov = yule.find_quote(q)
        if verdict == "missing":
            line = doc.lines[ln - 1] + (doc.lines[ln] if ln < len(doc.lines) else "")
            if "(adapted)" in line:
                continue
            kind = "invented?" if cov < 0.5 else "misquoted"
            yield sev, ln, f"{what} not found in refs/ ({kind}, {cov:.0%} of 5-grams match): “{missing[0][:50]}”"


def c_recaps(doc, ctx):
    if doc.paras and re.search(RECAP_OPEN, doc.paras[0][1]):
        yield "error", doc.paras[0][0], "opening recap"
    for ln, p in doc.paras[-2:]:
        if re.search(RECAP_CLOSE, p):
            yield "error", ln, f"closing recap ({nwords(p)} words)"
    for ln, p in doc.paras[1:-1]:
        if re.match(r"(So|Thus)[ ,]", p):
            yield "warning", ln, "“So/Thus …” restatement paragraph?"


def c_openers(doc, ctx):
    prev = None
    for ln, p in doc.paras:
        two = " ".join(p.split()[:2]).lower()
        if two == prev and not p.startswith("—"):
            yield "warning", ln, f"consecutive paragraphs open with “{two}”"
        prev = two


def c_length(doc, ctx):
    words = sum(nwords(re.sub(r"\[\d+\]", "", p)) for _, p in doc.paras)
    ctx["words"] = words
    lo, hi = T["length"][doc.kind]
    if not lo <= words <= hi:
        yield "error", None, f"narrative {words} words (outside {lo}–{hi})"


def c_sentence(doc, ctx):
    ss = [s for _, p in doc.paras for s in sentences(p)]
    avg = sum(map(nwords, ss)) / max(1, len(ss))
    ctx["avg_sentence"] = round(avg, 1)
    if avg > T["avg_sentence"]:
        yield "warning", None, f"average sentence {avg:.1f} words (> {T['avg_sentence']})"


def c_scaffolding(doc, ctx):
    for i, l in enumerate(doc.lines):
        for pat, flags in SCAFFOLD:
            for m in re.finditer(pat, l, flags):
                yield "error", i + 1, f"scaffolding: “{m.group(0)[:40]}”"


def c_citations(doc, ctx):
    if not doc.has_notes:
        return
    body = [int(x) for _, p in doc.epigraph + doc.paras for x in re.findall(r"\[(\d+)\]", p)]
    notes = sorted(doc.notes)
    if body != list(range(1, len(body) + 1)):
        yield "error", None, f"body citations not sequential 1..n: {body[:12]}{'…' if len(body) > 12 else ''}"
    for n in sorted(set(body) - set(notes)):
        yield "error", None, f"citation [{n}] has no Note"
    for n in sorted(set(notes) - set(body)):
        yield "error", doc.notes[n][0][0], f"Note [{n}] is never cited"
    for n, entries in doc.notes.items():
        if len(entries) > 1:
            yield "error", entries[1][0], f"Note [{n}] appears {len(entries)} times"
        text = re.sub(r"[✓~✗◇?/★☆]", " ", entries[0][1])
        if nwords(text) < T["stub_note_words"]:
            yield "warning", entries[0][0], f"stub Note [{n}] ({nwords(text)} words)"


LEAD = re.compile(r"[✓~✗◇?](\s*/\s*[✓~✗◇?])?\s")


def c_markers(doc, ctx):
    for n, entries in doc.notes.items():
        for ln, t in entries:
            bad = [ch for ch in T["forbidden_markers"] if ch in t]
            if bad:
                yield "error", ln, f"Note [{n}] uses retired marker {''.join(bad)}"
            if not LEAD.match(t):
                yield "error", ln, f"Note [{n}] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)"
            if re.search(r"\bDispute( hook| stance)?:", t):
                yield "error", ln, f"Note [{n}] uses a retired “Dispute:” label (use ? and say what is contested)"


def c_tags(doc, ctx):
    """S-03: Vols. II-III narrative/essay files carry exactly one tag line; nothing else carries one."""
    head = next((i for i, l in enumerate(doc.lines) if l.startswith("---")), len(doc.lines))
    tags = [(i + 1, l.strip()) for i, l in enumerate(doc.lines[:head]) if l.startswith("**[")]
    needs = doc.kind in ("narrative", "essay") and doc.rel.startswith(("vol-2/", "vol-3/"))
    if not needs:
        for ln, l in tags:
            yield "error", ln, f"tag line {l} not allowed here (Vols. II-III chapters only)"
        return
    if len(tags) != 1:
        yield "error", None, f"expected exactly one tag line ([V] [R] [M] [reception]), found {len(tags)}"
        return
    ln, l = tags[0]
    m = re.fullmatch(r"\*\*\[(\w+)\]\*\*", l)
    if not m or m.group(1) not in T["tags"]:
        yield "error", ln, f"tag line {l} is not one of **[V]** **[R]** **[M]** **[reception]**"


def c_ramusio(doc, ctx):
    flagged = 0
    for ln, p in doc.paras:
        has_flag = "Ramus" in p
        flagged += has_flag
        if not ramusio_hits(p):
            continue
        if not has_flag:
            yield "error", ln, "Ramusio-only passage without an inline flag"
        cites = [int(x) for x in re.findall(r"\[(\d+)\]", p)]
        if cites and not any(re.search(T["ramusio_note_label"], t) for c in cites for _, t in doc.notes.get(c, [])):
            yield "error", ln, f"Ramusio-only passage: no “Ramusio-only.” label in Notes {cites}"
    expected = ctx["manifest"].get(doc.rel, [])
    ctx["ramusio"] = f"{flagged}/{len(expected)}"
    if flagged < len(expected):
        yield "warning", None, (f"first draft carried {len(expected)} Ramusio passages; {flagged} paragraphs "
                                f"flag Ramusio (check: {'; '.join(e[:30] for e in expected[:3])}…)")


def c_names(doc, ctx):
    names = ctx["gazetteer"]
    seen = set()
    for ln, p in doc.paras:
        for w in re.findall(r"\b[A-Z][a-z]{4,}\b", strip_quotes(p)):
            if w in names or w in NAME_STOP or w in seen:
                continue
            close = difflib.get_close_matches(w, names, n=1, cutoff=0.86)
            if close and not (w.startswith(close[0]) or close[0].startswith(w)):
                seen.add(w)
                yield "warning", ln, f"“{w}” is close to gazetteer name “{close[0]}” (variant spelling?)"


ALL = ("verbatim first_person archaism you_must_know budgets asides quotes quote_verify recaps openers "
       "length sentence scaffolding citations markers tags ramusio names").split()
PROFILES = {
    "narrative": ALL,
    "essay": "verbatim first_person archaism you_must_know quote_verify length sentence scaffolding citations markers tags names".split(),
    "frontback": "verbatim first_person archaism you_must_know quote_verify scaffolding citations markers tags names".split(),
}


# S-24 citation style: checks live in tools/cite_rules.py.
import cite_rules  # noqa: E402
for _checks in PROFILES.values():
    _checks.extend(cite_rules.CHECKS)
globals().update({"c_" + n: getattr(cite_rules, "c_" + n) for n in cite_rules.CHECKS})


def lint(doc, ctx):
    issues = []
    for name in PROFILES[doc.kind]:
        for sev, ln, msg in globals()["c_" + name](doc, ctx):
            issues.append({"check": name, "severity": sev, "line": ln, "message": msg})
    return issues


# ---------------------------------------------------------------- output

def load_gazetteer():
    with open(BOOK / "gazetteer.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return sorted({w for r in rows for col in ("book_name", "modern_name") for w in re.findall(r"[A-Z][a-z]{4,}", r[col])})


def default_files():
    return sorted(p for p in BOOK.glob("vol-*/*.md") if kind_of(p.name))


def run(paths):
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    gaz = load_gazetteer()
    results = []
    for path in paths:
        doc = Doc(path)
        if not doc.kind:
            continue
        ctx = {"manifest": manifest, "gazetteer": gaz}
        issues = lint(doc, ctx)
        metrics = {k: v for k, v in ctx.items() if k not in ("manifest", "gazetteer")}
        results.append({"file": doc.rel, "kind": doc.kind, "metrics": metrics, "issues": issues,
                        "errors": sum(i["severity"] == "error" for i in issues),
                        "warnings": sum(i["severity"] == "warning" for i in issues)})
    return results


def summary(results):
    checks = {}
    for r in results:
        for sev in ("error", "warning"):
            for c in {i["check"] for i in r["issues"] if i["severity"] == sev}:
                checks.setdefault(c, {"error": 0, "warning": 0})[sev] += 1
    return {"files": len(results), "passing": sum(r["errors"] == 0 for r in results), "checks": checks}


def fmt_metrics(m):
    order = [("words", "{:,} w"), ("verbatim", "{}% verbatim"), ("quotes", "{} quotes"),
             ("asides", "{} asides"), ("ramusio", "Ramusio {}")]
    return " · ".join(f.format(m[k]) for k, f in order if k in m)


def print_text(results, verbose):
    for r in results:
        status = "PASS" if not r["errors"] else "FAIL"
        print(f"{status}  {r['file']:44} E{r['errors']:<3} W{r['warnings']:<3} {fmt_metrics(r['metrics'])}")
        if verbose:
            for i in r["issues"]:
                where = f"L{i['line']}" if i["line"] else "—"
                print(f"      {i['severity']:7} {where:>5}  {i['check']:13} {i['message']}")
    s = summary(results)
    print(f"\n{s['passing']}/{s['files']} files pass.  Files failing per check (errors / warnings):")
    for c in ALL:
        if c in s["checks"]:
            print(f"  {c:14} {s['checks'][c]['error']:3} / {s['checks'][c]['warning']}")


def print_md(results):
    s = summary(results)
    print(f"# Lint baseline\n\n`python3 tools/lint.py --md` · {s['passing']}/{s['files']} files pass. "
          "Errors decide pass/fail; warnings are prompts for the human read.\n")
    print("## Summary by check\n\n| Check | Files with errors | Files with warnings |\n|---|---|---|")
    for c in ALL:
        if c in s["checks"]:
            print(f"| {c} | {s['checks'][c]['error']} | {s['checks'][c]['warning']} |")
    print("\n## Per file\n\n| File | Kind | Errors | Warnings | Words | Verbatim | Quotes | Asides | Ramusio flagged/expected | Failing checks |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        m = r["metrics"]
        failing = sorted({i["check"] for i in r["issues"] if i["severity"] == "error"})
        print(f"| {r['file']} | {r['kind']} | {r['errors']} | {r['warnings']} | {m.get('words', '')} | "
              f"{m['verbatim']}% | {m.get('quotes', '')} | {m.get('asides', '')} | {m.get('ramusio', '')} | "
              f"{', '.join(failing) or '—'} |")
    print("\n## Issues\n")
    for r in results:
        if not r["issues"]:
            continue
        print(f"### {r['file']}\n")
        for i in r["issues"]:
            where = f"L{i['line']}" if i["line"] else "—"
            print(f"- **{i['severity']}** {where} `{i['check']}` {i['message']}")
        print()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*")
    ap.add_argument("-v", "--verbose", action="store_true", help="list every issue")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--md", action="store_true", help="Markdown report (baseline format)")
    ap.add_argument("--build-ramusio-manifest", action="store_true",
                    help=f"rebuild {MANIFEST.name} from the first draft ({BASELINE_COMMIT})")
    a = ap.parse_args()
    paths = [Path(f) for f in a.files] or default_files()
    if a.build_ramusio_manifest:
        m = build_manifest([str(p.resolve().relative_to(BOOK)) for p in default_files()])
        print(f"{MANIFEST.relative_to(BOOK)}: {sum(map(len, m.values()))} passages in {len(m)} files")
        return 0
    results = run(paths)
    if a.json:
        print(json.dumps({"summary": summary(results), "files": results}, indent=1, ensure_ascii=False))
    elif a.md:
        print_md(results)
    else:
        print_text(results, a.verbose)
    return 1 if any(r["errors"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
