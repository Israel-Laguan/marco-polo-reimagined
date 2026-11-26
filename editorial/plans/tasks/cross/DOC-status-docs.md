# DOC — Status and project docs

**Status:** done 2026-11-21 · **Plan doc:** [W6 status truthfulness](../../content-revision-plan.md#w6--status-truthfulness)

## Scope
Docs that describe the manuscript rather than being part of it: `SERIES-STATUS.md`, `vol-*/README.md`, `FRONT-BACK-MATTER.md`, `outline-*.md`, `media/ATTRIBUTIONS.md`, `gazetteer-readme.md`, repo `README.md`.

## Tasks

- `DOC.T1` **done 2026-11-17.** Replaced the `/workspace` paths with repo-relative ones in SERIES-STATUS, FRONT-BACK-MATTER, outline-summary and the three volume READMEs. The reader-facing Notes (I-F1 [10], I-F2 [1], I-B1 [11], II-F2 [1], III-F2 [1]) were rewritten without tooling paths or placeholder language.
- `DOC.T2` **done 2026-11-17.** SERIES-STATUS rewritten: draft complete, refinement in progress (4/49 files pass lint), pointing to `plans/README.md` for live status.
- `DOC.T3` **done 2026-11-17.** Repo `README.md`: what this is, layout, lint/test/build commands, licence.
- `DOC.T4` **done 2026-11-21.** Reconciled the series and volume status, chapter tags, outline counts, reading order, generated apparatus, media credits, and gazetteer and repository instructions. Checked 40 numbered chapters plus nine companion files, all 27 chapter tags, relative links, figure paths, and the 194-row gazetteer. The lint reports before and after matched at 7/49 passing. MED.T1 had already corrected the legacy generated-image captions.

The F2 caption format and media replacement remain in the [build](BLD-build-tooling.md#bldt4--front-and-back-matter-index-glossary-layout), [map](MAP-maps.md), and [plate tasks](PLT-plates.md). Legacy file retirement and remaining licence checks are tracked in [MED](MED-existing-media.md).
