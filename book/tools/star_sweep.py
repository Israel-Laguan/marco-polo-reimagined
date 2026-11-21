#!/usr/bin/env python3
"""Produce a review-only inventory of retired stars in manuscript Notes.

Run from any directory: python3 tools/star_sweep.py [--json]
The suggestions are heuristics, not approved changes; the script never edits text.
"""
import argparse
import json
import re
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
STAR = re.compile(r"★+")
NOTE = re.compile(r"^\[(\d+)\]\s*(.*)$")
MARKER = re.compile(r"(?:^|[;.]\s+)(?:[✓✗◇?]|~(?=\s))(?:\s*/\s*[✓~✗◇?])?(?=\s|★)")
WRONG = re.compile(r"\b(?:wrong|erroneous|scrambled|exaggerat\w*|false)\b", re.I)
MARVEL = re.compile(r"\b(?:myth|topos|legend|marvel|wonder-tale)\b", re.I)


def proposals(text):
    """Return one proposal per star group, including the surrounding clause."""
    results = []
    for star in STAR.finditer(text):
        # Sentence/semicolon boundaries provide context, not a semantic verdict.
        start = max(text.rfind(';', 0, star.start()), text.rfind('.', 0, star.start())) + 1
        ends = [i for i in (text.find(';', star.end()), text.find('.', star.end())) if i >= 0]
        end = min(ends) + 1 if ends else len(text)
        clause = text[start:end].strip()
        before = text[start:star.start()].strip()
        existing = bool(MARKER.search(before + '★'))
        if existing:
            replacement, reason = "delete", "existing marker in clause; check it covers this star"
        elif len(star.group()) == 1 and WRONG.search(clause):
            replacement, reason = "✗", "single star; clause describes an error or exaggeration"
        elif len(star.group()) == 1 and MARVEL.search(clause):
            replacement, reason = "◇", "single star; clause describes a marvel or legend"
        else:
            replacement = {1: "?", 2: "~", 3: "✓"}.get(len(star.group()), "manual")
            reason = "star-count rule; check claim and surrounding markers"
        results.append({"stars": star.group(), "column": star.start() + 1,
                        "clause": clause, "proposal": replacement, "reason": reason,
                        "dispute_label": bool(re.search(r"\bDispute:", clause, re.I))})
    return results


def inventory(book=BOOK):
    rows = []
    for path in sorted(book.glob('vol-*/*.md')):
        in_notes = False
        for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if line.startswith('## Notes'):
                in_notes = True
                continue
            if not in_notes:
                continue
            note = NOTE.match(line)
            if not note:
                continue
            for proposal in proposals(note.group(2)):
                rows.append({"file": str(path.relative_to(book)), "line": line_number,
                             "note": int(note.group(1)), "note_text": note.group(2), **proposal})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='output machine-readable inventory')
    args = parser.parse_args()
    rows = inventory()
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    print('# Retired-star review worklist\n')
    print('Suggestions require individual human review against the full Note and facts registry; '
          'they do not authorize application. Drop “Dispute:” where present and review any merge separately.\n')
    print(f'{len(rows)} star groups in {len({row["file"] for row in rows})} files.\n')
    for row in rows:
        print(f'## {row["file"]}:{row["line"]}, Note [{row["note"]}], column {row["column"]}\n')
        print(f'**{row["stars"]} → {row["proposal"]}** — {row["reason"]}.')
        if row['dispute_label']:
            print(' Drop the “Dispute:” label.')
        print(f'\n\nClause: {row["clause"]}\n\nFull Note: {row["note_text"]}\n')


if __name__ == '__main__':
    main()
