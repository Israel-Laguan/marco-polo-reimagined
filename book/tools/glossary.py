"""Render the three manuscript glossaries from the editorial review checklist."""

import argparse
import re
import unicodedata

import characters
import gazetteer

BOOK = gazetteer.BOOK
CHECKLIST = BOOK / "plans" / "registry" / "glossary-review.md"
KINDS = {"place", "person", "term"}
VOLUMES = gazetteer.ROMAN_VOLUMES


def checklist_rows():
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] in KINDS:
            yield cells


def read_entries():
    places = {row["id"]: row for row in gazetteer.load()}
    people = {row["id"]: row for row in characters.load() if row["gloss"]}
    authority = {"place": places, "person": people}
    seen = set()

    for kind, ident, where, name, modern, reading, gloss, origin, review in checklist_rows():
        key = kind, ident
        volumes = where.split()
        if key in seen or not re.fullmatch(r"[a-z0-9-]+", ident):
            raise ValueError(f"duplicate or invalid glossary ID: {kind} {ident}")
        if not volumes or set(volumes) - set(VOLUMES.values()):
            raise ValueError(f"invalid glossary volume for {ident}: {where}")
        if review not in {"Pending", "Approved", "Omit"} or (not reading and review != "Omit"):
            raise ValueError(f"missing reading or invalid review status for {ident}")
        if not name or not gloss:
            raise ValueError(f"missing headword or gloss for {ident}")
        seen.add(key)

        link = ""
        if kind in authority:
            row = authority[kind][ident]
            if row["book_name"] != name:
                raise ValueError(f"update glossary headword for {ident} to {row['book_name']}")
            registered = {ref.split("-")[0] for ref in row["chapters"].split(";") if ref}
            if registered - set(volumes):
                raise ValueError(f"add glossary volumes for {ident}: {sorted(registered - set(volumes))}")
            modern = row["gloss"] if kind == "person" else row["modern_name"]
            if kind == "place":
                link = row["wikipedia"]
                confidence = row["id_confidence"]
                if confidence == "unfixed" and not modern and ident != "prester-john":
                    modern = "No fixed modern identification"
                elif confidence == "disputed":
                    gloss = f"{gloss} Identification disputed." if modern else gloss
                    modern = modern or "Modern identification disputed"
                elif confidence == "probable" and not modern.endswith(" (provisional)"):
                    modern = f"{modern} (provisional)"

        head = f"[**{name}**]{{#{kind}-{ident}}}"
        if review == "Omit":
            reading = ""
        if reading.startswith("(") and reading.endswith(")"):
            head = f"{head} {reading}"
            reading = ""
        text = " · ".join(item for item in (head, modern, reading) if item)
        text += f". {gloss}"
        if origin:
            text += f" {origin}"
        if link:
            text += f" [Wikipedia]({link})"
        yield volumes, name, ident, text, review

    missing = sorted((kind, ident) for kind, rows in authority.items()
                     for ident, row in rows.items() if row["chapters"] and (kind, ident) not in seen)
    if missing:
        raise ValueError(f"glossary checklist is missing registry entries: {missing}")


def alphabetic(entry):
    _, name, ident, _, _ = entry
    name = unicodedata.normalize("NFKD", name.casefold())
    return "".join(c for c in name if not unicodedata.combining(c)), ident


def render(volume, entries):
    entries = sorted((entry for entry in entries if volume in entry[0]), key=alphabetic)
    draft = "draft " if any(entry[4] == "Pending" for entry in entries) else ""
    return "\n".join([
        f"# Back Matter {volume}-2",
        "## Glossary {#names-and-pronunciation}",
        "",
        f"Some entries include a {draft}pronunciation hint. "
        "Capital letters mark the stressed syllable.",
        "",
        "::: glossary",
        "",
        *(f"- {entry[3]}" for entry in entries),
        "",
        ":::",
        "",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="regenerate the manuscript files")
    action.add_argument("--check", action="store_true", help="check the files against the checklist")
    args = parser.parse_args()
    entries = list(read_entries())
    stale = []
    for number, volume in VOLUMES.items():
        path = BOOK / f"vol-{number}" / "back-02-glossary.md"
        expected = render(volume, entries)
        if args.write:
            path.write_text(expected, encoding="utf-8")
        elif not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(str(path.relative_to(BOOK)))
        print(f"Volume {volume}: {sum(volume in entry[0] for entry in entries)} entries")
    if stale:
        parser.exit(1, f"Regenerate stale glossary files: {', '.join(stale)}\n")


if __name__ == "__main__":
    main()
