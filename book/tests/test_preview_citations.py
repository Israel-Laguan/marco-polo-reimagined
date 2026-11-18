"""BLD.T9: HTML / EPUB citations print the YC sigla like the PDF (tools/build/preview.lua)."""

import re
import subprocess
import unittest
from pathlib import Path

BOOK = Path(__file__).resolve().parents[1]


def render(md, format="plain"):
    out = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", format, "--wrap=none", "--lua-filter", "tools/build/preview.lua",
         "--bibliography", "plans/registry/bibliography.bib", "-M", "reference-section-title=Works cited"],
        input=md, cwd=BOOK, check=True, capture_output=True, text=True)
    return out.stdout.replace("\xa0", " "), out.stderr


class PreviewCitationTest(unittest.TestCase):
    def test_sigla_locators_and_works_cited(self):
        text, err = render("A [@yc, 1.61]. B [@ycadd, on 2.23]. C [see @yc, 2.8; @larner1999marco, 12]. "
                           "D [@rossabi1988khubilai, ch. 6; @yc, 3.3].\n")
        self.assertEqual(err, "")
        for s in ("(YC 1.61)", "(YC Add. on 2.23)", "(see YC 2.8; Larner 1999, 12)",
                  "(Rossabi 1988, ch. 6; YC 3.3)", "YC (Polo, Marco). 1903.", "YC Add. (Cordier, Henri). 1920."):
            self.assertIn(s, text)
        self.assertNotIn("Polo 1903", text)
        self.assertLess(text.index("Abbreviations"), text.index("(YC 1.61)"))
        cited = text[text.index("Works cited"):]
        self.assertEqual(len(re.findall(r"^\S.*\d{4}\. ", cited, re.M)), 4)  # only what is cited

    def test_no_sigla_no_abbreviations_page(self):
        text, _ = render("A [@larner1999marco, 12].\n")
        self.assertNotIn("Abbreviations", text)
        self.assertIn("(Larner 1999, 12)", text)

    def test_unknown_key_warns(self):
        _, err = render("A [@nosuchkey2099].\n")
        self.assertIn("not found", err)

    def test_comparative_quote_prints_without_source_attribute(self):
        text, err = render('[“Quoted words from another work”]{src=hayton} [@bedrosianhayton].\n', "html")
        self.assertEqual(err, "")
        self.assertIn("“Quoted words from another work”", text)
        self.assertNotIn('src="hayton"', text)
        self.assertIn('id="ref-bedrosianhayton"', text)


if __name__ == "__main__":
    unittest.main()
