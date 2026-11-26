import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import edition


class EditionTest(unittest.TestCase):
    def test_manifest_orders_every_manuscript_file(self):
        manifest = edition.load()
        self.assertRegex(manifest["version"], edition.VERSION)
        self.assertEqual([len(volume["files"]) for volume in manifest["volumes"]], [17, 19, 16])
        for volume in manifest["volumes"]:
            self.assertTrue(volume["files"][0].startswith("front-01-"))
            self.assertTrue(volume["files"][-1].startswith("back-02-"))

    def test_signoff_is_bound_to_owner_and_proof_attempt(self):
        candidate = {"run": "734", "attempt": "2", "head": "a" * 40}
        body = "Proof: 734.2 " + candidate["head"] + "\n" + "\n".join(
            f"- [x] {item}" for item in edition.REVIEW_ITEMS
        ) + "\nFindings: None."
        approval = {"user": {"id": 42}, "state": "approved",
                    "environments": [{"name": "book-signoff"}]}
        comment = {"user": {"id": 42}, "body": body}
        self.assertTrue(edition.approved(candidate, 42, [comment], [approval]))
        self.assertFalse(edition.approved({**candidate, "attempt": "3"}, 42, [comment], [approval]))
        self.assertFalse(edition.approved(candidate, 7, [comment], [approval]))
        self.assertFalse(edition.approved(candidate, 42, [
            {**comment, "body": body.replace("- [x]", "- [ ]", 1)}
        ], [approval]))
        self.assertFalse(edition.approved(candidate, 42, [comment], []))


if __name__ == "__main__":
    unittest.main()
