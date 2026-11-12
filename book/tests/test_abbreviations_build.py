"""Exercise the reader-facing abbreviation page through the print pipeline."""

import re
import subprocess
import tempfile
import unittest
from pathlib import Path


BOOK = Path(__file__).resolve().parents[1]


class AbbreviationsBuildTest(unittest.TestCase):
    def test_explains_locator_before_main_text(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            source = output / "fixture.md"
            source.write_text(
                "# Chapter 1\n\n## Fixture\n\n"
                "Main text cites the source [@yc, 1.61] and the addenda "
                "[@ycadd, on 2.23].\n",
                encoding="utf-8",
            )
            subprocess.run(
                ["pandoc", str(source), "-f", "markdown-subscript-superscript", "-t", "latex",
                 "--template", "tools/build/book.latex", "--lua-filter", "tools/build/book.lua",
                 "--top-level-division=chapter", "--biblatex", "--bibliography",
                 "plans/registry/bibliography.bib", "-o", str(output / "fixture.tex")],
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


if __name__ == "__main__":
    unittest.main()
