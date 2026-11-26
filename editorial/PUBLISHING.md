# Publishing the book

## Prepare a proof

1. Branch from `staging` and edit the canonical Markdown. Use [the edition manifest](../manuscript/edition.json) to add or reorder manuscript files. Place artwork cleared for print under `manuscript/assets/` and update its [credit](../manuscript/assets/ATTRIBUTIONS.md).
2. Open a PR to `staging`. Review the checks and download the proof from the Actions run. The proof contains PDF and TXT files, per-volume LanguageTool and ChkTeX reports, and typesetting logs.
3. Merge after addressing the findings that affect your change. The staging branch gets a new integrated proof.

Manuscript lint is a required check. The print build also fails for LaTeX errors, unresolved citations or references, missing glyphs, missing figures, and undersized rasters. Review grammar suggestions, TeX lint messages, and overfull boxes against the text and the rendered pages.

## Sign off on an edition

1. Set the next version in the manifest through a PR to `staging`. Use `1.0.0-rc.1` for the first public prerelease and `1.0.0` for the first stable edition. If another candidate is needed before the stable edition, use `1.0.0-rc.2`.
2. Open a PR from this repository’s `staging` to `main` using the [release template](../.github/PULL_REQUEST_TEMPLATE/release.md). Describe the reader-facing changes.
3. Download the proof from that PR’s **Book checks and proofs** run. Use the identifier in the run summary to post the completed checklist as the repository owner. Include the rationale for any findings you accept.
4. In that run, select **Review deployments**, choose `book-signoff`, and approve. The check validates both the owner’s checklist and the environment review. For an updated candidate or a failed sign-off, rerun all jobs and use the new proof identifier.
5. When the release PR has passed both checks, use **Create a merge commit**. GitHub Actions rebuilds and compares the rendered pages and text to the approved proof before uploading the release.

The final job stages the uploads in a draft and checks their SHA-256 digests. Rerun failed jobs from the same merge run to retry delivery. Check **Releases** for the completed edition.

After publication, open a PR from `main` to `staging` and use a merge commit to synchronize the release history before starting the next edition. A sync PR runs the same manuscript checks as an ordinary contribution.

## GitHub configuration

The `staging` ruleset requires a PR and **Manuscript checks and proof**. The `main` ruleset requires a PR, a merge commit, an up-to-date branch, **Manuscript checks and proof**, and **Book release sign-off**. Both branches block deletion and force pushes. The `book-signoff` environment requires the repository owner as reviewer, permits owner self-review, and disallows bypassing the environment approval.
