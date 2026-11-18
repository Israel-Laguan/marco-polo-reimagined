"""BLD.T10: source-aware lookup of comparative quotations (tools/comparanda.py)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import comparanda
import yule


def verdict(quote, source="hayton"):
    return comparanda.find(quote, source)[0]


class ComparandaTest(unittest.TestCase):
    def test_exact_and_ellipsis(self):
        self.assertEqual(verdict("The kingdom of Cathay is considered the richest and most noble realm in the world"), "found")
        self.assertEqual(verdict("The kingdom of Cathay is considered … no one has visited all of them"), "found")
        self.assertEqual(verdict("no one has visited all of them … The kingdom of Cathay is considered"), "not-found")

    def test_other_author_editor_or_yule_never_passes(self):
        colophon = verdict("first wrote down this book in French, as the aforementioned Brother Haiton dictated it")
        preface = comparanda.find("Het'um's History enters the ranks of Crusader literature", "hayton")
        yule_text = comparanda.find("so much knowledge and experience of the divers parts of the World", "hayton")
        self.assertEqual(colophon, "wrong-source")
        self.assertEqual(preface[0], "wrong-source")
        self.assertIn("Bedrosian", preface[1])
        self.assertEqual(yule_text, ("wrong-source", "found only in Yule–Cordier"))

    def test_ocr_or_misquote_is_reported_not_passed(self):
        v, detail = comparanda.find("The kingdom of Cathay is considered the wealthiest and most noble realm in the world", "hayton")
        self.assertEqual(v, "not-found")
        self.assertIn("misquoted or OCR", detail)
        self.assertIn("wealthiest", detail)

    def test_quote_across_a_segment_boundary_fails(self):
        self.assertNotEqual(verdict("in saecula saeculorum Amen Here ends the book Flower of Histories"), "found")

    def test_unmapped_uncleared_unknown_are_refused(self):
        self.assertEqual(verdict("a silver tree with four pipes", "rubruck"), "unmapped")
        self.assertEqual(verdict("any words at all here", "akhbar"), "not-cleared")
        self.assertEqual(verdict("any words at all here", "nobody"), "unknown")

    def test_scan_syntax(self):
        m = comparanda.SPAN.search("He wrote [“The kingdom of Cathay is considered the richest”]{src=hayton} once.")
        self.assertEqual(m.groups(), ("The kingdom of Cathay is considered the richest", "hayton"))

    def test_yule_only_lookup_unchanged(self):
        self.assertEqual(yule.CORPUS, ["yule-vol1.txt", "yule-vol2.txt"])
        self.assertEqual(yule.find_quote("The kingdom of Cathay is considered the richest and most noble realm")[0], "missing")


if __name__ == "__main__":
    unittest.main()
