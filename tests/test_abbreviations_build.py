"""Exercise front matter, running heads and figure numbering in print."""

import re
import subprocess
import tempfile
import unittest
from pathlib import Path


BOOK = Path(__file__).resolve().parents[1]


class AbbreviationsBuildTest(unittest.TestCase):
    def test_contents_running_heads_and_plate_captions(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            source = output / "fixture.md"
            source.write_text(
                "# Front Matter II-2\n\n## Map guide\n\n"
                "### Heading for the map\n\n"
                "![Old alt text](../assets/maps/A1-series-overview.svg)\n\n"
                "*Caption:* Expanded caption with *credit*.\n\n"
                "# Chapter II-1\n\n## Fixture title {short=\"Routes & ports\"}\n\n"
                "Main text cites the source [@yc, 1.61] and the addenda "
                "[@ycadd, on 2.23].\n\n"
                "![A second plate](../assets/maps/A16-cocachin-return.svg)\n\n"
                + "The fixture continues to a second page.\n\n" * 40
                + ":::: parallel-text\n\n"
                "::: witness\n**First witness**\n\nFirst excerpt.\n:::\n\n"
                "::: witness\n**Second witness**\n\nSecond excerpt.\n:::\n\n"
                "::::\n\n"
                "# Back Matter II-2\n## Glossary {#names-and-pronunciation}\n\n"
                "::: glossary\n\n"
                "- [**Vuju**]{#place-vuju-1} · Huzhou.\n"
                "- [**Vuju**]{#place-vuju-2} · Jinhua.\n\n"
                ":::\n",
                encoding="utf-8",
            )
            subprocess.run(
                ["pandoc", str(source), "-f", "markdown-subscript-superscript", "-t", "latex",
                 "--template", "tools/build/book.latex", "--lua-filter", "tools/build/book.lua",
                 "--top-level-division=chapter", "--biblatex", "--bibliography",
                 "manuscript/bibliography.bib", "-M", "volume-id=II", "-o", str(output / "fixture.tex")],
                cwd=BOOK, check=True, capture_output=True, text=True,
            )
            subprocess.run(
                ["latexmk", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                 f"-outdir={output}", str(output / "fixture.tex")],
                cwd=BOOK, check=True, capture_output=True, text=True,
            )
            pdf_text = subprocess.run(
                ["pdftotext", "-layout", str(output / "fixture.pdf"), "-"],
                check=True, capture_output=True, text=True,
            ).stdout
            text = re.sub(r"\s+", " ", pdf_text)
            abbreviations = text.index("Abbreviations")
            main_text = text.index("Main text cites the source")
            front_matter = text[abbreviations:main_text]
            self.assertIn("YC 1.61", front_matter)
            self.assertIn("Book I, Chapter LXI", front_matter)
            self.assertIn("Prologue", front_matter)
            self.assertIn("YC Add.", front_matter)
            self.assertIn("1903", front_matter)
            self.assertIn("1920", front_matter)
            self.assertIn("Plate II.1: Heading for the map. Expanded caption with credit.", text)
            self.assertIn("Plate II.2: A second plate", text)
            self.assertNotIn("Old alt text", text)
            self.assertIn("Routes & ports", text)
            self.assertRegex(pdf_text, r"First witness[ \t]+Second witness")
            self.assertRegex(pdf_text, r"Vuju · Huzhou\.[ \t]+Vuju · Jinhua\.")
            self.assertIn(r"\bookchapter{II-1}{Fixture title}{Routes \& ports}",
                          (output / "fixture.tex").read_text())
            toc = (output / "fixture.toc").read_text()
            entries = re.findall(r"\\contentsline \{chapter\}\{(.*?)\}\{.*?\}\{(.*?)\}", toc)
            self.assertEqual([title for title, _ in entries],
                             ["Abbreviations", "Map guide", r"II-1\hskip 1em\relax Fixture title",
                              "Glossary", "Works cited"])
            self.assertEqual(len({anchor for _, anchor in entries}), len(entries))


if __name__ == "__main__":
    unittest.main()
