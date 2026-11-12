"""Checks for missing unambiguous modern-scholar citations in Notes."""

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import cite_rules
import lint


class ScholarCitationLintTest(unittest.TestCase):
    def issues(self, notes):
        doc = lint.Doc("vol-1/ch-01-example.md", "# Chapter 1\n\n## Notes\n\n" + notes)
        return list(cite_rules.c_unkeyed_scholars(doc, {}))

    def test_errors_per_note_only_for_unkeyed_unambiguous_modern_scholars(self):
        issues = self.issues(
            "[1] Larner and Vogel offer different readings; Larner returns to this point.\n"
            "[2] Larner [-@larner1999marco] and Vogel [@vogel2013marco].\n"
            "[3] Larner [-@larner1999marco] and Vogel disagree.\n"
            "[4] Rubruck is reported by Yule [@yc, 1.61]. In May the Hall was empty.\n"
        )
        self.assertEqual([(severity, line) for severity, line, _ in issues],
                         [("error", 5), ("error", 5), ("error", 7)])
        self.assertIn("Larner", issues[0][2])
        self.assertIn("Vogel", issues[1][2])
        self.assertIn("Vogel", issues[2][2])

    def test_check_is_registered_for_all_manuscript_profiles(self):
        for profile in lint.PROFILES.values():
            self.assertIn("unkeyed_scholars", profile)
            self.assertEqual(profile.count("unkeyed_scholars"), 1)

    def test_flags_context_and_missing_editions_without_guessing_a_work(self):
        issues = self.issues(
            "[1] Allsen and Elverskog are named without works.\n"
            "[2] Allsen [-@allsen2001culture] discusses movement of specialists.\n"
            "[3] Needham’s series includes astronomy by Needham [-@needham1959mathematics].\n"
            "[4] Rubruck and Rashid are reported by Yule [@yc, 1.61].\n"
        )
        self.assertEqual([(severity, line) for severity, line, _ in issues],
                         [("error", 5), ("error", 5)])
        self.assertIn("Allsen", issues[0][2])
        self.assertIn("Elverskog", issues[1][2])
        self.assertNotIn("@allsen1997commodity", issues[0][2])


if __name__ == "__main__":
    unittest.main()
