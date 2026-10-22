# APP — Apparatus

**Status:** backlog · **Plan doc:** `content-revision-plan.md` § W3, § W5; S-03

## Scope
Series-wide reader apparatus: reliability markers, [V]/[R]/[M] tags, the "How to read this book" box, Ramusio flag convention, Notes hygiene rules, epigraph policy. Per-chapter application happens in each chapter's `.T2`/`.T4`; this file holds the shared decisions and sweeps.

## Backlog
- About 80 ★ ratings in Notes with no legend (II-M7, III-M9); "★ Dispute:" duplicate Notes.
- Undefined compound tags [V/M], [R/M] (II-m10); tags missing in III-7 to III-12 (III-M8).
- No reader-facing explanation of the tags or markers (II-M8).
- About 60 unflagged Ramusio passages (I-M5, II-M1, III-M7). Bracket list in `tools/seed/brackets.txt`.
- Epigraph policy: exact Yule wording, or marked *(adapted)* (II-N5, III-C1).

## Decided (S-03, closed 2026-10-22)
Convention: `VOICE-GUIDE.md` § Apparatus conventions. Markers ✓ ~ ✗ ◇ ?; ★ retired; compound tags fold into [M]; [reception] for III-10 to III-12; Ramusio flag = inline words + "Ramusio-only." Note label (provenance, not a marker). The lint enforces tags, lead markers, "Dispute:" labels and the Ramusio label (`tools/lint.py`).

## Gated by spikes
S-03 ✓ · S-08 (rendering: confirm a font with ✓ ✗ ◇ glyphs; endnotes vs footnotes)

## Tasks
### APP.T1 — "How to read this book" box
- **Status:** backlog · **Depends:** S-03 ✓
- **Do:** add the full box (below, ≈150 words) to the front of `vol-1/front-01-world-before-the-road.md` as `::: howto … :::` after the epigraph rule; add the short form to `vol-2/front-01-yuan-china-context.md` and `vol-3/front-01-indian-ocean-world.md` (the Vol. III form adds `[reception]`). Vol. I's chapters carry no tags, so its box says tags begin in Vol. II.
- **Done when:** the three boxes are in place and the lint still shows no new errors in those files.

**Full form (Vol. I):**

> **How to read this book.** Each chapter retells one stretch of *Il Milione*. Small numbers in the text, like [3], point to the Notes at the end of the chapter, where a claim is checked against other witnesses. Every Note opens with a mark: ✓ corroborated by independent sources · ~ plausible, but a detail is under strain · ✗ probably wrong or exaggerated · ◇ marvel or hearsay, kept as the Book tells it · ? scholars disagree. From Volume II, each chapter also carries a tag: **[V]** mostly what Polo says he saw or did · **[R]** mostly what he heard · **[M]** a mixture. Some passages exist only in Ramusio's sixteenth-century version, or in Pipino's Latin or another later text. The story says so as it goes, and the Note labels them "Ramusio-only." Read them as later layers, not as Polo's earliest words.

**Short form (Vol. II; Vol. III adds "**[reception]** the Book's afterlife"):**

> **Reading the marks.** Notes open with ✓ corroborated · ~ plausible · ✗ probably wrong · ◇ marvel or hearsay · ? contested. Tags: **[V]** seen · **[R]** heard · **[M]** both. "Ramusio-only." labels a passage found only in a later text. Full key: Volume I, front matter.

### APP.T2 — ★ → marker sweep
- **Status:** backlog · **Depends:** S-03 ✓ · **Do first**, before the chapter re-voices
- **Do:** write `tools/star_sweep.py` that lists every ★ in Notes (81 across 19 files at baseline) with its clause and a proposed replacement per the sweep rules in the guide (★★★ → ✓, ★★ → ~, ★ → ?, deleted beside an existing marker, "Dispute:" dropped); a person confirms each; apply one commit per volume.
- **Done when:** `grep -rn "★" vol-*/` finds nothing in Notes, and the lint `markers` check reports no retired-marker errors.

### APP.T3 — Tag lines
- **Status:** backlog · **Depends:** S-03 ✓
- **Do:** apply the assigned tags: II-8, II-14, III-2, III-3, III-4, III-5 → `**[M]**`; III-7 `**[R]**`; III-8 `**[M]**`; III-9 `**[V]**`; III-10, III-11, III-12 `**[reception]**`. Each chapter's `.T4` confirms the tag against its content, so this task may be folded into those.
- **Done when:** the lint `tags` check passes for all 49 files.

### APP.T4 — Ramusio bracket check in the lint (with `BLD`)
- **Status:** partly done · **Depends:** S-02 ✓
- **Done (S-02/S-03):** the lint matches reproduced Ramusio passages, requires an inline flag and a "Ramusio-only." (or Pipino-/Jacopo-/Zelada-only) label in the cited Note.
- **Left:** the lint only sees near-verbatim passages, so paraphrased Ramusio detail escapes it. After the re-voices, compare flag counts with the manifest (already a warning) and spot-check against Yule's brackets (`tools/seed/ramusio-brackets.txt`, rebuilt without `Sidenote:` lines).
