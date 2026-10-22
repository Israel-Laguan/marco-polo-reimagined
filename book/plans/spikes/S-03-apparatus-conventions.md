# S-03 — Apparatus conventions

**Status:** open · **Timebox:** 1 session · **Gates:** `.T2` (Ramusio flags) and `.T4` (Notes/apparatus) in every file; `APP` cross tasks

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
- [ ] Convention section added to `VOICE-GUIDE.md`
- [ ] "How to read this book" box text (goes to I-F1, short form in II-F1 and III-F1)
- [ ] Lint rules handed to S-02

## Feedback to plan
- `content-revision-plan.md` § W3, § W5

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `<ID>.T2`, `<ID>.T4` per file; `APP.T1` the how-to-read box; `APP.T2` the ★ conversion sweep
