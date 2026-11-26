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
        self.assertEqual(verdict("The kingdom of Cathay is considered … the richest"), "found")
        self.assertEqual(verdict("The kingdom of Cathay is considered … banana empire"), "not-found")

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
        self.assertEqual(verdict("any words at all here", "ibnbattuta"), "unmapped")
        self.assertEqual(verdict("any words at all here", "akhbar"), "not-cleared")
        self.assertEqual(verdict("any words at all here", "nobody"), "unknown")

    def test_rubruck_only_passes_in_verified_translation(self):
        quote = "a great silver tree, and at its roots are four lions"
        self.assertEqual(verdict(quote, "rubruck"), "found")
        self.assertEqual(verdict(quote, "carpini"), "wrong-source")
        note = "Similar works of art and mechanical contrivances were often seen"
        result, detail = comparanda.find(note, "rubruck")
        self.assertEqual(result, "wrong-source")
        self.assertIn("Rockhill, notes to p. 208", detail)
        self.assertEqual(verdict("the butlers draw it … " + note, "rubruck"), "not-found")
        self.assertEqual(verdict("the men and women Similar works of art", "rubruck"), "not-found")

    def test_carpini_is_separate_from_rubruck_and_benedict(self):
        quote = "when they began drinking mare's milk"
        self.assertEqual(verdict(quote, "carpini"), "found")
        self.assertEqual(verdict(quote, "rubruck"), "wrong-source")
        result, detail = comparanda.find("four separate flights of steps led up to the platform", "carpini")
        self.assertEqual(result, "wrong-source")
        self.assertIn("Benedict the Pole", detail)
        result, detail = comparanda.find("they placed a gilded seat in their midst", "carpini")
        self.assertEqual(result, "wrong-source")
        self.assertIn("Rockhill, note to p. 21", detail)

    def test_odoric_distinguishes_champa_translation_from_editorial_comparison(self):
        self.assertEqual(verdict("a good two hundred children", "odoric"), "found")
        result, detail = comparanda.find("Above is Paradise, but Su-chau and Hang-chau are here below", "odoric")
        self.assertEqual(result, "wrong-source")
        self.assertIn("notes on p. 192", detail)

    def test_wassaf_distinguishes_maabar_translation_from_footnote(self):
        self.assertEqual(verdict("so situated as to be the key of Hind", "wassaf"), "found")
        result, detail = comparanda.find("was a common name among the Pandya Dynasty", "wassaf")
        self.assertEqual(result, "wrong-source")
        self.assertIn("Elliot and Dowson", detail)

    def test_scan_syntax(self):
        m = comparanda.SPAN.search("He wrote [“The kingdom of Cathay is considered the richest”]{src=hayton} once.")
        self.assertEqual(m.groups(), ("The kingdom of Cathay is considered the richest", "hayton"))
        m = comparanda.SPAN.search("[“The kingdom of Cathay [China] is considered the richest”]{src=hayton}")
        self.assertEqual(verdict(*m.groups()), "found")

    def test_yule_only_lookup_unchanged(self):
        self.assertEqual(yule.CORPUS, ["yule-vol1.txt", "yule-vol2.txt"])
        self.assertEqual(yule.find_quote("The kingdom of Cathay is considered the richest and most noble realm")[0], "missing")


if __name__ == "__main__":
    unittest.main()
