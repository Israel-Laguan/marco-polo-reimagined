"""Gazetteer front matter and narrative naming policy."""

import contextlib
import io
import re
import sys
import unittest
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK / "tools"))

import gazetteer
import lint


class PlaceTableTest(unittest.TestCase):
    def test_generated_sections_match_front_matter(self):
        for volume in ("1", "2", "3"):
            with self.subTest(volume=volume):
                path, = (BOOK / "manuscript" / f"vol-{volume}").glob("front-02-*.md")
                section = re.search(
                    r"(?ms)^### Place table .*?(?=^### (?:A few map cautions|Map cautions))",
                    path.read_text(encoding="utf-8"),
                ).group().rstrip()
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(gazetteer.main(["tables", volume]), 0)
                self.assertEqual(output.getvalue().rstrip(), section)
                rows = [r for r in gazetteer.load() if r["volume"] == volume]
                self.assertEqual(
                    len(re.findall(r"^\| (?!Book name \|).+ \|$", section, re.M)),
                    sum(bool(r["latitude"]) for r in rows),
                )
                for row in rows:
                    if not row["latitude"]:
                        self.assertIn(row["book_name"], section.split("*Places without a map fix:* ")[1])

    def test_role_keeps_abbreviations_and_escapes_pipes(self):
        row = {"book_name": "Example", "modern_name": "A | B",
               "notes": "Home c. 1295. Later note."}
        self.assertEqual(gazetteer.place_table_row(row), r"| Example | A \| B | Home c. 1295. |")


class PlaceNamingTest(unittest.TestCase):
    def findings(self, text, path="vol-1/ch-06-tauris-persia.md"):
        doc = lint.Doc(path, text)
        return [(severity, message) for severity, _, message in
                lint.c_name_policy(doc, {"gaz_rows": gazetteer.load()}) if "(S-05)" not in message]

    def test_bare_and_unglossed_forms_are_errors(self):
        findings = self.findings("Tauris stood ahead. They reached Tabriz that night.")
        self.assertEqual([level for level, _ in findings], ["error", "error"])

    def test_first_mention_checks_the_gloss(self):
        self.assertEqual(self.findings("They reached *Tauris* (Tabriz) and stayed in Tauris."), [])
        self.assertEqual(len(self.findings("They reached Tauris (after dusk).")), 1)

    def test_duplicate_book_names_use_chapter_scope(self):
        self.assertEqual(self.findings("Vuju (Jinhua) lay ahead.", "vol-2/ch-14-fuju-zayton.md"), [])
        self.assertEqual(len(self.findings("Vuju (Huzhou) lay ahead.", "vol-2/ch-14-fuju-zayton.md")), 1)

    def test_same_name_places_without_a_map_row(self):
        self.assertEqual(self.findings("They sailed to Tana.", "vol-1/ch-01-genoa-prison.md"), [])
        self.assertEqual(self.findings("They reached Caiju.", "vol-2/ch-10-manzi-sung.md"), [])
        self.assertEqual(len(self.findings("They reached Caiju.", "vol-2/ch-12-kian-suju.md")), 1)

    def test_valid_gloss_can_include_a_name_that_overlaps_another_alias(self):
        self.assertEqual(
            self.findings("They stayed at Samara (Samudera Pasai).", "vol-3/ch-03-java-less-sumatra.md"),
            [],
        )

    def test_exempt_passages(self):
        self.assertEqual(self.findings("> Tabriz.\n\n*“Tabriz.”*\n\n## Notes\n\n[1] Tabriz."), [])
        self.assertEqual(self.findings("Tabriz.", "vol-3/ch-11-afterlives.md"), [])
        self.assertEqual(self.findings("Tabriz.", "vol-1/front-02-maps-outbound.md"), [])
