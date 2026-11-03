# S-03 — Apparatus conventions

**Status:** closed 2026-10-22 · **Timebox:** 1 session · **Gates:** `.T2` (Ramusio flags) and `.T4` (Notes/apparatus) in every file; `APP` cross tasks

## Question
What is the single convention for reliability markers, [V]/[R]/[M] tags, Notes format, and the Ramusio flag? And how does each survive into LaTeX?

## Why it matters
- Three marker systems are in use today: ✓~✗◇?, ★★★, and "★ Dispute:" notes.
- Compound tags [V/M] and [R/M] are undefined, and no reader-facing page explains any tag.
- About 60 Ramusio-only passages are unflagged.
Every chapter task touches these, so the convention must be settled first or every chapter gets redone.

## Inputs
- `VOICE-GUIDE.md` § Citations and Notes; outline legend (★)
- Critique: I-M5, I-m5; II-M1, II-M7, II-m10; III-M7, III-M8, III-M9
- S-08 for how [n] and markers render in LaTeX (footnotes vs endnotes)

## Method
1. Decide the marker set: recommend ✓ ~ ✗ ◇ ?, retire ★, and give a ★ → marker mapping.
2. Decide the tags: keep [V]/[R]/[M] and either define the compounds or fold them into [M]; *[reception]* for III-10 to III-12.
3. Ramusio flag wording (2–3 approved variants) and Note suffix ("◇ Ramusio-only").
4. Notes rules: no placeholder Notes, no duplicate "Dispute" Notes, one claim per Note.
5. Draft the 150-word "How to read this book" box.

## Output (definition of done)
- [x] Convention section added to `VOICE-GUIDE.md`
- [x] "How to read this book" box text (goes to I-F1, short form in II-F1 and III-F1): in `tasks/cross/APP-apparatus.md` § APP.T1
- [x] Lint rules handed to S-02: implemented in `tools/lint.py` (tags, lead marker, "Dispute:" label, Ramusio label)

## Feedback to plan
- `content-revision-plan.md` § W3, § W5

## Findings
_2026-10-22, from a read of all 49 files (695 Notes) and the three critiques._

1. **Three marker systems, not one.** ✓ ~ ✗ ◇ ? (the Notes' real working set: 812 ✓, 247 ✗, 225 ◇ plus ~ and ?), ★★★/★★/★ (81 uses in 19 files, defined only in the outline legend) and "★ Dispute:" (16 Notes, 12 of them whole-Note duplicates). The outline legend maps ★★★ = corroborated, ★★ = plausible, ★ = contested, ◇ = wonder-tale, so the mapping to ✓ ~ ? ◇ is direct. But a ★ often sits beside a marker that already says the same thing ("✓ … ★★★ Vogel"), and "★★★ Dispute: horse-breeding… independently corroborated" shows the word *Dispute* was a label, not a verdict.
2. **◇ had two meanings.** The outline legend and 225 Note uses make it *marvel or hearsay*. VOICE-GUIDE v2 and the pilot (II-2) made it *Ramusio-only*. But Ramusian detail can be ✓ (Kinsay's markets) or a marvel, so provenance and reliability are separate questions. Decision: ◇ keeps its original meaning; Ramusio is a word label.
3. **Compound markers are the house style (562 uses)**, mostly "✓ / ~" (265): a lead pair summarising the clauses that follow. Banning them would rewrite most Notes for no reader gain. Kept as "core / detail" pairs, max two.
4. **`~` collides with "about"** ("~60 miles"). A marker is `~` followed by a space; approximations use "about" or "c.".
5. **Tags in use:** [V] 19, [R] 18, [M] 18, [R/M] 10, [V/M] 6, none on III-7 to III-9 and III-10 to III-12 (the Vol. III README uses *[reception]*). The outline defines only V/R/M and applies them to Vols. II–III; Vol. I has no tags. [M] already means "both", so compounds add no category.
6. **Notes without a lead marker: 35**, mostly scaffolding, stubs and pointer Notes (front/back matter included).
7. **The Ramusio manifest** (152 reproduced passages, 29 files) bounds what a lint can see. One flag anywhere in a paragraph used to hide every other Ramusian detail in it, so the flag now covers one contiguous passage.
8. **LaTeX:** everything is a fixed Markdown shape (marker glyphs at clause start, one tag paragraph, `[n]` + `## Notes`, plain-word flags), so the filter is mechanical. Open for S-08: a font with ✓ ✗ ◇ glyphs, and endnotes vs footnotes.

## Decision
_Closed 2026-10-22. Full text: `VOICE-GUIDE.md` § Apparatus conventions._

- **Markers:** ✓ corroborated · ~ plausible · ✗ probably wrong/exaggerated · ◇ marvel or hearsay · ? contested. **★ retired**: ★★★ → ✓, ★★ → ~, ★ → ?, with ✗/◇ where the clause says wrong or myth, deleted beside an existing marker, "Dispute:" always dropped.
- **Tags:** [V] seen · [R] heard · [M] both · **[reception]** (III-10 to III-12). Compounds fold into [M]. Vols. II–III narrative/essay files only. Assigned: II-8, II-14, III-2, III-3, III-4, III-5 → [M]; III-7 [R]; III-8 [M]; III-9 [V].
- **Ramusio flag:** a 3–6-word inline flag per contiguous passage ("Ramusio's text adds…" / "In Ramusio's version…" / "(…, Ramusio adds)", plus "in another Ramusian passage" for continuations), and the Note label **"Ramusio-only."** (or Pipino-, Jacopo-, Zelada-only) after the lead marker. It replaces "◇ Ramusio-only".
- **Notes:** one Note per citation; lead marker or "core / detail" pair; ≤ 4 marker clauses; no placeholders, no duplicate "Dispute" Notes, no scaffolding.
- **How-to-read box:** 141 words, in `tasks/cross/APP-apparatus.md` (APP.T1), with a short form for Vols. II–III.
- **Pilot impact:** II-2 needed one edit (Note [4]: `? / ◇ Ramusio-only.` → `? Ramusio-only.`); it still lints clean.
- **Lint (done in `tools/lint.py`):** new `tags` check; every Note must open with a marker; "Dispute:" label is an error; Ramusio passages need the "Ramusio-only." label in a cited Note. Baseline regenerated: 1/49 pass; `markers` 33, `tags` 12, `ramusio` 28 files with errors.
- **Not decided here:** endnotes vs footnotes and the symbol font (S-08).

## Tasks created on close
- [x] `<ID>.T2` (Ramusio flags and labels; 40 narrative/essay files) and `<ID>.T4` (Notes and apparatus; all 49 files) written into every chapter task file with per-file numbers; each `.T6` baseline refreshed. II-02's T2 and T4 are marked done.
- [x] `APP.T1` how-to-read box (text included) · `APP.T2` ★ sweep · `APP.T3` tag lines · `APP.T4` Ramusio check (partly done): in `tasks/cross/APP-apparatus.md`.
