import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import lint  # noqa: E402


class CharacterNameLintTests(unittest.TestCase):
    def test_modern_name_is_allowed_as_a_gloss_and_rejected_bare(self):
        rel = "vol-1/ch-03-second-setting-forth.md"
        ctx = {"gaz_rows": []}
        glossed = lint.Doc(rel, text="Bundukdar (Baibars) marched into Armenia.")
        self.assertEqual(list(lint.c_name_policy(glossed, ctx)), [])

        bare = lint.Doc(rel, text="Baibars marched into Armenia.")
        self.assertEqual(list(lint.c_name_policy(bare, ctx)), [
            ("error", 1, "“Baibars” used bare; the book form for this person is “Bundukdar” (S-05)"),
        ])

    def test_missing_first_gloss_is_an_error_even_when_supplied_later(self):
        doc = lint.Doc("vol-1/ch-03-second-setting-forth.md", text=(
            "Bundukdar led the army.\n\nBundukdar (Baibars) marched into Armenia."
        ))
        self.assertEqual(list(lint.c_name_policy(doc, {"gaz_rows": []})), [
            ("error", 1, "first mention of “Bundukdar” has no gloss (Baibars) (S-05)"),
        ])


class NoteLintTests(unittest.TestCase):
    def test_inline_anchor_pairs_with_one_note(self):
        doc = lint.Doc("vol-2/ch-04-hunt.md", text=(
            "The hawk wears a leg label [1] with two names.\n\n"
            "## Notes\n\n[1] ✓ Polo describes labels naming both the keeper and the owner."
        ))
        self.assertEqual(list(lint.c_citations(doc, {})), [])

    def test_anchor_without_notes_section_is_an_error(self):
        doc = lint.Doc("vol-2/ch-04-hunt.md", text="The hawk wears a leg label [1].")
        self.assertIn(("error", None, "citation [1] has no Note"), lint.c_citations(doc, {}))

    def test_orphaned_and_duplicate_numbers_are_errors(self):
        doc = lint.Doc("vol-2/ch-04-hunt.md", text=(
            "The hawk wears a label [1] with two names [1].\n\n## Notes\n\n"
            "[1] ✓ Polo describes labels naming both the keeper and the owner.\n"
            "[1] ✓ Polo describes labels naming both the keeper and the owner.\n"
            "[2] ~ The source leaves the material of the label unspecified."
        ))
        errors = [message for severity, _, message in lint.c_citations(doc, {}) if severity == "error"]
        self.assertTrue(any("body citations not sequential" in message for message in errors))
        self.assertIn("Note [1] appears 2 times", errors)
        self.assertIn("Note [2] is never cited", errors)

    def test_bold_label_after_verdict_is_an_error(self):
        doc = lint.Doc("vol-2/ch-04-hunt.md", text=(
            "## Notes\n\n[1] ✓ **Lost property.** The Book gives the officer a banner."
        ))
        self.assertTrue(any(severity == "error" and "bold" in message
                            for severity, _, message in lint.c_markers(doc, {})))

    @patch.object(lint, "ramusio_hits", return_value=[0])
    def test_ramusio_provenance_belongs_in_the_anchored_note(self, _hits):
        prose = "The cats approach against the wind [1] so their quarry cannot scent them."
        note = "[1] ~ Ramusio-only. The precaution is familiar to hunters."
        doc = lint.Doc("vol-2/ch-04-hunt.md", text=f"{prose}\n\n## Notes\n\n{note}")
        ctx = {"manifest": {doc.rel: ["example witness passage"]}}
        self.assertEqual(list(lint.c_ramusio(doc, ctx)), [])

        for details in ("", "\n\n## Notes\n\n[1] ~ The precaution is familiar to hunters."):
            with self.subTest(details=details):
                missing = lint.Doc(doc.rel, text=prose + details)
                self.assertEqual(list(lint.c_ramusio(missing, ctx)), [
                    ("error", 1, "Ramusio passage needs a provenance label in an anchored Note")
                ])

        unanchored = lint.Doc(doc.rel, text=prose.replace(" [1]", ""))
        self.assertEqual(list(lint.c_ramusio(unanchored, ctx)), [
            ("warning", 1, "possible Ramusio passage without a note anchor")
        ])
