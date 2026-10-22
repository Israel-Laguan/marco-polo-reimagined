"""Yule–Cordier reference corpus: normalised words, n-grams, Ramusio passages, quote lookup.

usage: python3 tools/yule.py --ramusio > tools/seed/ramusio-brackets.txt
"""
import re
import sys
from functools import lru_cache
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
REFS = BOOK / "refs"
CORPUS = ["yule-vol1.txt", "yule-vol2.txt"]
# Main text of the Book (prologue to the end of Book IV), excluding Yule's
# introduction, its sidenotes, and the appendices. 1-based line numbers.
MAIN_TEXT = {"yule-vol1.txt": (12451, None), "yule-vol2.txt": (1351, 26929)}


def norm(text):
    """Lower-case word list; folds curly quotes, drops {n} and [n] note markers."""
    text = text.replace("’", "'").replace("‘", "'")
    text = re.sub(r"\{\d+\}|\[\d+\]", "", text)
    return re.findall(r"[a-z]+", text.lower())


def grams(words, n):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


@lru_cache(maxsize=None)
def _raw(name):
    return (REFS / name).read_text(encoding="utf-8").replace("\r", "")


@lru_cache(maxsize=None)
def words():
    return tuple(w for name in CORPUS for w in norm(_raw(name)))


@lru_cache(maxsize=None)
def ngrams(n):
    return frozenset(grams(words(), n))


@lru_cache(maxsize=None)
def joined():
    """Whole corpus as one space-separated normalised string, padded for word-boundary search."""
    return " " + " ".join(words()) + " "


def coverage(word_list, n):
    """Per-word flags: True where the word sits inside an n-gram shared with Yule."""
    Y = ngrams(n)
    cov = [False] * len(word_list)
    for i in range(len(word_list) - n + 1):
        if tuple(word_list[i:i + n]) in Y:
            cov[i:i + n] = [True] * n
    return cov


@lru_cache(maxsize=None)
def ramusio_passages():
    """Text of every square-bracketed passage in Yule's main text (Ramusio-only additions).

    Main text is the column-0 prose; notes are indented. Drops illustration captions,
    bare numbers, Cordier's editorial brackets ("—H. C.") and passages under 3 words.
    """
    out = []
    for name, (start, end) in MAIN_TEXT.items():
        lines = _raw(name).split("\n")[start - 1:end]
        paras, buf = [], []
        for line in lines + [""]:
            if line and not line[0].isspace():
                buf.append(line)
            elif buf:
                paras.append(" ".join(buf))
                buf = []
        for p in paras:
            for m in re.finditer(r"\[([^\[\]]+)\]", p):
                s = re.sub(r"\{\d+\}", "", m.group(1)).strip()
                if s.startswith(("Illustration", "Sidenote")) or "—H. C." in s:
                    continue
                if len(s.split()) >= 3:
                    out.append(s)
    return tuple(out)


def find_quote(quote, min_words=4):
    """Check a quotation against the corpus.

    Strips [insertions], splits at ellipses, and requires every segment of at least
    `min_words` words to occur verbatim (after normalisation). Returns (verdict, missing, cov):
    verdict is "found", "missing", or "short" (no segment long enough to check); cov is the
    share of the quote's 5-grams found anywhere in Yule (low = invented, high = misquoted).
    """
    quote = re.sub(r"\[[^\]]*\]", " ", quote)
    segs = [norm(s) for s in re.split(r"…|\.\.\.", quote)]
    segs = [s for s in segs if len(s) >= min_words]
    if not segs:
        return "short", [], 1.0
    corpus = joined()
    missing = [" ".join(s) for s in segs if " " + " ".join(s) + " " not in corpus]
    g = [t for s in segs for t in grams(s, 5)] or [tuple(s) for s in segs]
    cov = sum(t in ngrams(5) or len(t) < 5 and " " + " ".join(t) + " " in corpus for t in g) / len(g)
    return ("missing" if missing else "found"), missing, cov


if __name__ == "__main__":
    if sys.argv[1:] == ["--ramusio"]:
        print("\n".join(ramusio_passages()))
    else:
        sys.exit(__doc__)
