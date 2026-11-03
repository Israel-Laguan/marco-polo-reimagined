"""Per-chapter re-voice targets against the S-01 / VOICE-GUIDE v2 thresholds.

usage: python3 revoice_targets.py <yule-all.txt> <brackets.txt> <chapter.md> [...]
Prints one JSON object per chapter (line numbers are 1-based file lines).
Seed for S-02's tools/lint.py.
"""
import json, re, sys

N = 7
ARCH = r"\b(hath|doth|foison|certes|sundry|whilst|thereof|insomuch|wherein|to wit|existeth|natheless|fain|wot|wist|trowed|gat)\b|’tis"
FIRST = r"\b(I will tell|I tell you|I assure you|I can tell you|I can assure|I have been telling|I am going to|I will relate|What more shall I say|I should have told|And why should I|I will quit|Now I will|I ought to mention|Let me tell you|we will quit|We could tell you)\b"
HINGES = r"Marco Polo (starts by )?narrat|\bPolo narrates\b|[Aa]ccording to the [Bb]ook|next he mentions|Then (Polo|he) describes|Tradition has it"
RECAP_OPEN = r"^(The Book has|The book has|So far the Book|Having (told|shown))"
RECAP_CLOSE = r"Here the chapter|For the present|has done what|stops short of|the chapter has|This chapter has"


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = re.sub(r"\{\d+\}", "", t)
    return re.findall(r"[a-z]+", t.lower())


def grams(words, n):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def strip_quotes(t):
    return re.sub(r"\*“[^”]*”\*|“[^”]*”", " ", t)


def main():
    yule = norm(open(sys.argv[1], encoding="utf-8").read())
    Y = grams(yule, N)
    brackets = [norm(l) for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
    B8 = [grams(b, 8) for b in brackets if len(b) >= 10]
    for path in sys.argv[3:]:
        lines = open(path, encoding="utf-8").read().split("\n")
        end = next((i for i, l in enumerate(lines) if l.startswith("## Notes")), len(lines))
        paras = [(i + 1, l) for i, l in enumerate(lines[:end])
                 if l.strip() and not l.startswith(("#", ">", "**[", "---"))]
        allw, cov_total = 0, 0
        worst, asides, restate, unflagged = [], [], [], []
        for ln, p in paras:
            w = norm(p)
            cov = [0] * len(w)
            for i in range(len(w) - N + 1):
                if tuple(w[i:i + N]) in Y:
                    cov[i:i + N] = [1] * N
            allw += len(w); cov_total += sum(cov)
            pct = 100 * sum(cov) / max(1, len(w))
            if len(w) >= 60 and pct >= 70:
                worst.append((ln, round(pct), len(w)))
            if p.startswith("—") and len(w) > 80:
                asides.append((ln, len(w)))
            if re.match(r"^(So|Thus) ", p):
                restate.append(ln)
            if "Ramus" not in p:
                pg = grams(w, 8)
                hits = sum(1 for b in B8 if len(b & pg) >= 3)
                if hits:
                    unflagged.append(ln)
        body = "\n".join(p for _, p in paras)
        unq = strip_quotes(body)
        out = {
            "file": path,
            "words": len(re.findall(r"[\w’'-]+", body)),
            "verbatim": round(100 * cov_total / max(1, allw)),
            "worst": sorted(worst, key=lambda x: -x[1] * x[2])[:6],
            "ymk": len(re.findall(r"[Yy]ou must know", unq)),
            "anyway": len(re.findall(r"\bAnyway\b", unq)),
            "hinges": len(re.findall(HINGES, unq)),
            "arch": len(re.findall(ARCH, unq, re.I)),
            "first": len(re.findall(FIRST, unq)),
            "asides_long": asides,
            "asides": sum(1 for _, p in paras if p.startswith("—")),
            "recap_open": paras[0][0] if paras and re.search(RECAP_OPEN, paras[0][1]) else None,
            "recap_close": [(ln, len(p.split())) for ln, p in paras[-2:] if re.search(RECAP_CLOSE, p)],
            "restate": restate,
            "ramusio_unflagged": unflagged,
        }
        print(json.dumps(out))


if __name__ == "__main__":
    main()
