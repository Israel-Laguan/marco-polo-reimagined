# DOC — Status and project docs

**Status:** backlog · **Plan doc:** `content-revision-plan.md` § W6

## Scope
Docs that describe the manuscript rather than being part of it: `SERIES-STATUS.md`, `vol-*/README.md`, `FRONT-BACK-MATTER.md`, `outline-*.md`, `media/ATTRIBUTIONS.md`, `gazetteer-readme.md`, repo `README.md`.

## Backlog
- SERIES-STATUS claims the storyteller rewrite is "complete" (false: S-01/S-02 baseline) and contradicts itself on media.
- `/workspace/marco-polo/...` paths everywhere.
- The vol-3 README claims a tag convention that III-7 to III-12 don't follow.
- ATTRIBUTIONS lists generated files that the chapters caption as Wikimedia.
- The repo `README.md` is just a title.

## Gated by spikes
None to start. Final wording after S-02 (baseline numbers).

## Tasks
- `DOC.T1` **done 2026-11-17.** Replaced the `/workspace` paths with repo-relative ones in SERIES-STATUS, FRONT-BACK-MATTER, outline-summary and the three volume READMEs. The reader-facing Notes (I-F1 [10], I-F2 [1], I-B1 [11], II-F2 [1], III-F2 [1]) were rewritten without tooling paths or placeholder language. The false status claims in those docs remain `DOC.T2`.
- `DOC.T2` **done 2026-11-17.** SERIES-STATUS rewritten: draft complete, refinement in progress (4/49 files pass lint), pointing to `plans/README.md` for live status.
- `DOC.T3` **done 2026-11-17.** Repo `README.md`: what this is, layout, lint/test/build commands, licence.
