from contextlib import redirect_stdout
from io import StringIO
import os
from pathlib import Path
from subprocess import CalledProcessError
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools/ci"))
import github_release


class ReleaseDeliveryTest(unittest.TestCase):
    def test_upload_failure_leaves_a_retryable_draft(self):
        version, sha = "1.0.0-rc.1", "a" * 40
        draft = None
        assets = []
        interrupted = False
        publications = 0

        def catalog():
            return [{**draft, "assets": assets.copy()}] if draft else []

        def api(endpoint, data=None):
            nonlocal draft
            if endpoint == "releases":
                draft = {**data, "id": 1, "assets": []}
                return draft
            self.assertEqual(endpoint, "releases/1")
            return {**draft, "assets": assets.copy()}

        def command(*args, **kwargs):
            nonlocal interrupted, publications
            if args[:3] == ("gh", "release", "upload"):
                path = Path(args[-1])
                if assets and not interrupted:
                    interrupted = True
                    assets.append({"name": path.name, "id": 99, "state": "starter", "size": 0})
                    raise CalledProcessError(1, args)
                assets.append({"name": path.name, "state": "uploaded", "size": path.stat().st_size,
                               "digest": f"sha256:{github_release.sha256(path)}"})
            elif args[:4] == ("gh", "api", "--method", "DELETE"):
                self.assertEqual(args[-1], "repos/owner/book/releases/assets/99")
                assets[:] = [asset for asset in assets if asset.get("id") != 99]
            else:
                self.assertEqual(args[:4], ("gh", "api", "--method", "PATCH"))
                self.assertEqual(len(assets), 8)
                draft["draft"] = False
                publications += 1

        with TemporaryDirectory() as tmp:
            directory = Path(tmp)
            prefix = f"the-book-of-the-million-v{version}"
            names = ["SHA256SUMS", f"{prefix}-latex.zip"] + [
                f"{prefix}-vol{i}.{suffix}" for i in range(1, 4) for suffix in ("pdf", "txt")
            ]
            for name in names:
                (directory / name).write_text(name)
            with patch.dict(os.environ, GITHUB_REPOSITORY="owner/book"), \
                    patch.object(github_release, "releases", catalog), \
                    patch.object(github_release, "api", api), \
                    patch.object(github_release, "execute", command), redirect_stdout(StringIO()):
                with self.assertRaises(CalledProcessError):
                    github_release.publish(directory, version, sha)
                self.assertTrue(draft["draft"])
                self.assertEqual(publications, 0)
                github_release.publish(directory, version, sha)
                github_release.publish(directory, version, sha)
                self.assertEqual(publications, 1)


if __name__ == "__main__":
    unittest.main()
