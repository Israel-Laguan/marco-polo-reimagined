"""Regression checks for source choices in citation conversion."""

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import cite_convert


class CitationConversionTest(unittest.TestCase):
    def test_personnel_alone_does_not_select_allsens_textile_book(self):
        row = cite_convert.load_map()["Allsen"]
        key, _ = cite_convert.key_for("Allsen", row, "Allsen on multilingual personnel.")
        self.assertIsNone(key)
        key, _ = cite_convert.key_for("Allsen", row, "Allsen on Mongol textile exchange.")
        self.assertEqual(key, "allsen1997commodity")


if __name__ == "__main__":
    unittest.main()
