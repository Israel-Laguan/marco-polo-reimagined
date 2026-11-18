"""BLD.T6: lint rules for the build conventions (captions, opening headings)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import lint


def run(check, text):
    return [(s, ln) for s, ln, _ in getattr(lint, "c_" + check)(lint.Doc("vol-1/front-02-x.md", text), {})]


class BuildLintTest(unittest.TestCase):
    def test_caption_paragraph_after_figure_is_an_error(self):
        text = "# Front Matter I-2\n## Maps\n\n![Alt](../media/a.jpg)\n\n*Caption:* Words.\n\n*Caption:* not after a figure\n"
        self.assertEqual(run("captions", text), [("error", 6)])

    def test_caption_in_brackets_passes(self):
        self.assertEqual(run("captions", "![Alt with caption](../media/a.jpg)\n\nText.\n"), [])

    def test_opening_headings(self):
        for ok in ("# Chapter I-1\n## Title\n", "# Front Matter II-1\n\n## T\n", "# Back Matter III-1\n## T\n### x\n"):
            self.assertEqual(run("headings", ok), [], ok)
        for bad in ("## Title\n# Chapter I-1\n", "# Chapter I-1\n### Title\n", "# Prologue\n## T\n", "Text only\n"):
            self.assertEqual([s for s, _ in run("headings", bad)], ["warning"], bad)

    def test_registered_in_every_profile(self):
        for profile in lint.PROFILES.values():
            self.assertIn("captions", profile)
            self.assertIn("headings", profile)


if __name__ == "__main__":
    unittest.main()
