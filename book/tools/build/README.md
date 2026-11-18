# Book tooling

## Pre-commit checks

From the repository root, copy `book/tools/pre-commit` to Git's hook directory
as `pre-commit` and make it executable. For a checkout using Git's default hook
directory, run:

```sh
hook=$(git rev-parse --git-path hooks/pre-commit)
if [ -e "$hook" ] || [ -L "$hook" ]; then
  printf '%s\n' "Existing hook at $hook. Add book/tools/pre-commit to that hook."
else
  mkdir -p "$(dirname "$hook")"
  install -m 755 book/tools/pre-commit "$hook"
fi
```

If you configured `core.hooksPath`, use that directory. To check what is staged
without installing a hook, run `book/tools/pre-commit` from the repository root.
Update the installed copy after changing the script.

The hook checks staged versions of manuscript files against
`book/plans/status/lint-baseline.md`. It rejects a file above its baseline error
count and any new scaffolding, citation, or quotation error even if other errors
were fixed. It compares messages and their counts so line moves are harmless.
The three F2 files have allowances of 2, 2, and 1 for caption errors surfaced by
a rule added after the baseline was generated. The Ramusio manifest is read as-is.

When the bibliography is staged, the hook regenerates the source index in a
temporary copy using the staged manuscript and compares it with the staged
index. If they differ, run `python3 tools/sources_index.py` from `book/` and
stage the generated index. If chapter files contain unrelated unstaged edits,
generate the index in a clean checkout of the intended contents.
