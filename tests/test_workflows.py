"""Keep the release approval off commits' staging proof runs."""

from pathlib import Path
import unittest

import yaml


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github/workflows"


def workflow(name):
    return yaml.load((WORKFLOWS / name).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


class WorkflowTest(unittest.TestCase):
    def test_signoff_lives_only_on_release_pull_requests(self):
        release = workflow("book-checks.yml")
        self.assertEqual(set(release["on"]), {"pull_request"})
        self.assertEqual(release["on"]["pull_request"]["branches"], ["main"])
        self.assertEqual(release["jobs"]["signoff"]["environment"], "book-signoff")

        staging = workflow("staging-proofs.yml")
        for trigger in ("pull_request", "push"):
            self.assertEqual(staging["on"][trigger]["branches"], ["staging"])
        signoff_name = release["jobs"]["signoff"]["name"]
        for job in staging["jobs"].values():
            self.assertNotIn("environment", job)
            self.assertNotEqual(job.get("name"), signoff_name)


if __name__ == "__main__":
    unittest.main()
