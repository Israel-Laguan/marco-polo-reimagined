"""BLD.T5: cite_audit classifies S-24 epigraph credits as converted."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import cite_audit


class CiteAuditTest(unittest.TestCase):
    def test_s24_credits_are_converted(self):
        for t in ("Marco Polo, Book 2, ch. 12 (Yule–Cordier)", "Marco Polo, Prologue, preamble (Yule–Cordier)",
                  "Jacopo d’Acqui, *Imago mundi* (c. 1330), in Yule–Cordier, Introduction, § 37",
                  "Venetian saying *(tradition)*"):
            self.assertEqual(cite_audit.classify_epigraph(t), "epigraph: converted", t)

    def test_old_forms_are_not(self):
        self.assertEqual(cite_audit.classify_epigraph("Marco Polo, Book II.xii"), "epigraph: Book N.roman")
        self.assertEqual(cite_audit.classify_epigraph("The Book of Marco Polo"), "epigraph: free text")


if __name__ == "__main__":
    unittest.main()
