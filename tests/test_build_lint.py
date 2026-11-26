"""BLD.T6: lint rules for the build conventions (captions, opening headings)."""

import shutil
import subprocess
import sys
import unittest
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BOOK / "tools"))
import lint


def run(check, text):
    return [(s, ln) for s, ln, _ in getattr(lint, "c_" + check)(lint.Doc("vol-1/front-02-x.md", text), {})]


class BuildLintTest(unittest.TestCase):
    def test_caption_paragraph_after_figure_is_an_error(self):
        text = "# Front Matter I-2\n## Maps\n\n![Alt](../assets/a.jpg)\n\n*Caption:* Words.\n\n*Caption:* not after a figure\n"
        self.assertEqual(run("captions", text), [("error", 6)])

    def test_caption_in_brackets_passes(self):
        self.assertEqual(run("captions", "![Alt with caption](../assets/a.jpg)\n\nText.\n"), [])

    def test_opening_headings(self):
        for ok in ("# Chapter I-1\n## Title\n", "# Front Matter II-1\n\n## T\n", "# Back Matter III-1\n## T\n### x\n"):
            self.assertEqual(run("headings", ok), [], ok)
        for bad in ("## Title\n# Chapter I-1\n", "# Chapter I-1\n### Title\n", "# Prologue\n## T\n", "Text only\n"):
            self.assertEqual([s for s, _ in run("headings", bad)], ["warning"], bad)

    def test_registered_in_every_profile(self):
        for profile in lint.PROFILES.values():
            self.assertIn("captions", profile)
            self.assertIn("headings", profile)

    @unittest.skipUnless(shutil.which("pandoc"), "requires Pandoc")
    def test_map_link_targets_figure_in_assembled_print(self):
        text = """# Chapter I-3
## The road

See [the map](ch-04-next.md#map-of-the-road).

# Chapter I-4
## Next

### Map of the road

![The stages.](../assets/maps/A1-series-overview.svg)
"""
        latex = subprocess.check_output(
            ["pandoc", "-t", "latex", "--lua-filter", "tools/build/map-links.lua",
             "--lua-filter", "tools/build/book.lua"],
            cwd=BOOK, input=text, text=True,
        )
        self.assertIn(r"\hyperref[map-of-the-road]", latex)
        self.assertIn(r"\caption{\textbf{Map of the road}. The stages.}\label{map-of-the-road}", latex)
        self.assertNotIn(r"\subsubsection{Map of the road}", latex)

    @unittest.skipUnless(shutil.which("pandoc"), "requires Pandoc")
    def test_small_facsimile_warns_only_at_full_width(self):
        asset = "../assets/public-domain/I-02-alt_omont1907-pl3-fol2v-mono.jpg"
        text = (f"![Inset]({asset}){{#fig-omont width=60%}}\n\n"
                f"See [the inset](ch-02-house-of-polo.md#fig-omont).\n\n"
                f"![Full width]({asset})\n")
        result = subprocess.run(
            ["pandoc", "-t", "latex", "--lua-filter", "tools/build/map-links.lua",
             "--lua-filter", "tools/build/book.lua"],
            cwd=BOOK, input=text, text=True, capture_output=True, check=True,
        )
        self.assertEqual(result.stderr.count("px wide"), 1)
        self.assertIn("print needs 1350 px", result.stderr)
        self.assertIn(r"\hyperref[fig-omont]", result.stdout)


if __name__ == "__main__":
    unittest.main()
