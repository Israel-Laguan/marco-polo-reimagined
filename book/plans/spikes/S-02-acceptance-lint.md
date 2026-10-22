# S-02 — Acceptance lint and thresholds

**Status:** open · **Timebox:** 1 session · **Gates:** `.T6` lint pass in every file; the definition of done for the whole project

## Question
Which automated checks define "done" for a file, with what thresholds, and what does the baseline look like today?

## Why it matters
Without a gate, "complete" means whatever the last pass claimed (see SERIES-STATUS). The lint makes progress measurable and stops regressions such as reintroduced "Anyway" tics or scaffolding leaks.

## Inputs
- `tools/seed/overlap.py`, `stats.py`, `brackets.txt`
- `content-revision-plan.md` § W0 (proposed checks)
- Thresholds from S-01 (voice) and S-03 (markers, tags)

## Method
1. Build `tools/lint.py` with the W0 checks: verbatim %, Book first person, archaisms outside quotes, hinge budgets, scaffolding strings, citation integrity, epigraph/quotation found in `refs/`, marker set, length, gazetteer names, Ramusio bracket matches without a flag.
2. Run it on all 49 files; save the baseline report to `plans/status/lint-baseline.md`.
3. Calibrate. Check false positives: quotations, proper names, legitimate short shared phrases. Is 7-gram right? Is 25% reachable, given that I-1 = 7% and I-12 = 16%?
4. Make it fast enough to run on every commit.

## Output (definition of done)
- [ ] `tools/lint.py` with per-file and summary output
- [ ] Baseline report committed
- [ ] Thresholds fixed and recorded in the planning README "Definition of done"

## Feedback to plan
- `content-revision-plan.md` § W0: final thresholds
- `README.md` § Definition of done

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `<ID>.T6` per file (lint green + human read)
- `BLD.T*`: hook the lint into a pre-commit script
