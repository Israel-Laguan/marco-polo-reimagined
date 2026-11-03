# S-02 — Acceptance lint and thresholds

**Status:** closed 2026-10-21 · **Timebox:** 1 session · **Gates:** `.T6` lint pass in every file; the definition of done for the whole project

## Question
Which automated checks define "done" for a file, with what thresholds, and what does the baseline look like today?

## Why it matters
Without a gate, "complete" means whatever the last pass claimed (see SERIES-STATUS). The lint makes progress measurable and stops regressions such as reintroduced "Anyway" tics or scaffolding leaks.

## Inputs
- `tools/seed/overlap.py`, `stats.py`, `brackets.txt`
- `content-revision-plan.md` § W0 (proposed checks)
- Thresholds from S-01 (voice): handed over in S-01 § Decision and content plan W0 (verbatim ≤ 15%, hinge/aside/quote/recap budgets)
- Thresholds from S-03 (markers, tags)

## Method
1. Build `tools/lint.py` with the W0 checks: verbatim %, Book first person, archaisms outside quotes, hinge budgets, scaffolding strings, citation integrity, epigraph/quotation found in `refs/`, marker set, length, gazetteer names, Ramusio bracket matches without a flag.
2. Run it on all 49 files; save the baseline report to `plans/status/lint-baseline.md`.
3. Calibrate. Check false positives: quotations, proper names, legitimate short shared phrases. Is 7-gram right? S-01 set ≤ 15% (pilot II-2 = 3%, I-1 = 7%); confirm it holds on quotation-heavy chapters.
4. Make it fast enough to run on every commit.

## Output (definition of done)
- [x] `tools/lint.py` with per-file and summary output (`-v`, `--json`, `--md`)
- [x] Baseline report committed (`plans/status/lint-baseline.md`)
- [x] Thresholds fixed and recorded in the planning README "Definition of done"

## Feedback to plan
- `content-revision-plan.md` § W0: final thresholds
- `README.md` § Definition of done

## Findings
_2026-10-21. The first part was investigated with the seed scripts; the lint built from it is described under "Built" below._

**Scope.** 49 files = 39 narrative chapters + the III-12 essay + 9 front/back files (the 3 volume READMEs are outside the gate). The lint needs three profiles: *narrative* (every check), *essay* (≤ 3,500 words; no hinge/recap budgets), and *front/back* (verbatim, scaffolding, citations, epigraph, markers; no length range). Original prose scores 0–1% verbatim, so the verbatim gate costs nothing on those files.

**What the seed already covers.** `revoice_targets.py` already does verbatim %, Book first person, archaisms, "Anyway", hinges, "You must know", asides, recaps, length and unflagged Ramusio passages. `stats.py` adds citation integrity. A full run over all 49 files takes **0.6 s**, so running it on every commit is no problem.

**Missing checks:** scaffolding; quotation budgets (per scene, per chapter, ≤ 25 words); the attribution-verb cap (≤ 4, needs a verb list); asides ending in an exit formula; epigraph/quotation verification; the marker set; gazetteer names; average sentence length (warning). The hinge regex differs between `stats.py` and `revoice_targets.py`. Merge them into one list.

**Bugs and calibration**

1. **`tools/seed/ramusio-brackets.txt` is polluted.** 73 of its 211 lines are Yule's `[Sidenote: …]` editorial sidenotes (vol. 1 introduction). One line is a chapter heading and several are truncated. That leaves about 137 usable lines; the rebuilt list has 152 passages (see "Built"). The impact is low, because a hit needs 3 shared 8-grams, but the list should be regenerated without `Sidenote:` lines and the T3 "unflagged Ramusio" counts rerun. Also, the check only asks whether "Ramus" appears anywhere in the paragraph, so one flag hides every other unflagged Ramusio detail in that paragraph. It also doesn't verify the matching "◇ Ramusio-only" Note.
2. **The W0 scaffolding regex `Soft \w+:` finds only 36 of 197 "Soft" labels.** Most labels have several words ("Soft caution at the start:", "Soft Wood target and reply field:"). Use `\bSoft\b[^.:\n]{0,40}:` (III-12 has most of them; W1's estimate of ~155 is about right). Gazetteer reliability labels must be matched in their label form (`Gazetteer: *visited*`, `*uncertain*`), not as bare words. Notes legitimately say "Marco personally visited…". Every bare `outline` hit sampled was a real meta reference, so keep it as an error.
3. **7-gram is the right size.** Original prose scores 0–1% (III-12 essay, III-11, I-F1, II-F1), so 7-gram has no measurable false positives. Overlap on II-2 by n-gram size: 5-gram 8%, 6-gram 5%, 7-gram 3%, 8-gram 2%. 5-gram adds noise and 8-gram undercounts.
4. **15% is consistent with the quotation budget.** At the caps, 8 quotes × 25 words + a ~30-word epigraph ≈ 230 words, which is 12.8% of a chapter at the 1,800-word floor. That leaves about 2% for incidental shared phrasing. It can't be tested on a re-voiced quotation-heavy chapter yet, because only II-2 is re-voiced (I-1 is 7%).
5. **Exact-match quotation verification fails 34 of 51 epigraphs.** It is too strict. Ellipses, `[Chipangu]`-style insertions and abridgements break the match. Scored by 5-gram coverage, the epigraphs split cleanly:
   - 0–40%: exactly the critique's invented ones (I-back, II-back, III-back, I-F1, I-F2, II-F1, III-F2, III-11 ×2, III-12).
   - 50–80%: real lines abridged with "…".

   Rule: strip `[…]` insertions, split at "…", and require every segment of ≥ 4 words to be found (normalised) in `refs/`. Otherwise fail, unless the quote is marked *(adapted)*. Italic in-text quotes: 5 of 5 found.
6. **Citation integrity is nearly clean.** Only 2 files fail: I-4 has orphan Note [15], and I-F1 cites out of order.
7. **Markers:** 81 ★ in 19 files. The marker set is provisional until S-03, so read it from config.
8. **The gazetteer has no alias column** (`gazetteer.csv`, 112 rows, `book_name` only), and finding place names in prose needs a candidate list. Keep it warning-only until S-04 adds aliases.

**Rough baseline (seed checks only, before the lint).** II-2 is the only narrative file that passes everything. Verbatim > 15% in 36 of 39 narrative chapters; I-1 (7%), II-2 (3%) and III-11 pass. Per chapter, 3–9 checks fail. Worst: II-3 (80%, 6× "You must know"), III-4 (78%, 7 Book first person), II-8 (77%).

**Recommended shape.** One `tools/lint.py` with:
- thresholds in a single config block, with the S-03 and S-04 values marked provisional;
- severity levels: error vs warning;
- per-file and summary output, plus `--json`.

Fix the Ramusio list first.

**Built** (`tools/lint.py` 492 lines, `tools/yule.py` 111 lines, stdlib only)
- **Errors vs warnings.** Errors are mechanical rule breaks and decide pass/fail. Warnings are heuristics for the human read: "So/Thus" restatements, repeated openers, stub Notes, average sentence length, Ramusio flag count vs first draft, and name variants.
- **Ramusio list rebuilt** from the column-0 main text of Yule's chapters: 152 passages, with no sidenotes, captions or Cordier brackets. The seed file is regenerated from it. The 74 junk lines had caused **no** false hits: the T3 unflagged counts are unchanged (53 → 53), so the task files stand.
- **Ramusio after a re-voice.** Paraphrase defeats both n-gram and content-word matching (tested on II-2: 0 hits either way). The lint therefore errors on near-verbatim passages that lack a flag or a ◇ Note. For re-voiced text it falls back to `tools/ramusio-manifest.json`, which lists the 89 passages in 29 files that the first draft (commit `1204156`) reproduced, and warns when a chapter flags fewer.
- **Quotation verification.** Each failure is labelled *invented?* (< 50% of 5-grams in Yule) or *misquoted*. All 13 epigraphs the critique flagged fail. So do 7 more that are real lines with small edits:
  - an added or swapped word: I-12 adds "And"; II-10 has "So" for "And"; II-15 has "He" for "this King Caidu"; III-7 has "they" for "the people of those isles";
  - spliced speech with no ellipsis (I-3);
  - reworded segments (II-9);
  - an inserted phrase (III-8 "houses built with ventilators", which comes from Yule's index, not the text).

  Each of the 7 needs a correction or an *(adapted)* mark.
- **No scene breaks.** Chapters have only the two `---` rules (after the tag, before Notes), so "≤ 2 quotations per scene" is enforced per paragraph. If W4 adds scene breaks, switch the check to scenes.
- **I-1 isn't lint-clean:** 2 "Anyway" aside exits, two asides over 80 words (153, 102), and a 50-word italic block quotation (the Book's prologue address). This matches S-01's light T3 for I-1. The block quote needs either a cut or an exception.
- **Speed:** ~2 s for 49 files, ~1 s for one file.

**Baseline** (`plans/status/lint-baseline.md`): **1/49 files pass (II-2).** Files with errors, by check:

| Check | Files |
|---|---|
| scaffolding | 40 |
| verbatim | 36 |
| asides | 36 |
| archaisms | 35 |
| budgets | 34 |
| ramusio | 27 |
| you_must_know | 25 |
| quote_verify | 19 |
| markers (★) | 19 |
| first_person | 14 |
| recaps | 12 |
| length | 6 |
| citations | 2 |
| quotes | 1 |

## Decision
_Closed 2026-10-21._

- **Definition of done** = `python3 tools/lint.py <file>` exits 0, plus warnings reviewed in the human read. Thresholds are recorded in README § Definition of done and live in the `T` block of `tools/lint.py`.
- **Verbatim:** 7-gram, ≤ 15%, including the epigraph and marked quotes, for every profile. 7-gram has no measurable false positives (original prose 0–1%), and the quotation budget fits under the cap (≤ 12.8% at the length floor).
- **Provisional rules** (to update when the spikes close, by editing the `T` block and the pattern lists only):
  - S-03: the ★ ban, ◇ as the Ramusio Note marker, the stub-Note size, and accepting any "Ramus…" mention as the inline flag;
  - S-04: name variants stay warnings until the gazetteer has aliases.
- **The T3 Ramusio targets stand** (unchanged by the list fix).

## Tasks created on close
- [x] `<ID>.T6` in all 49 chapter task files, each with its baseline error/warning count and failing checks.
- [x] `BLD.T1` pre-commit hook in `tasks/cross/BLD-build-tooling.md`: block regressions against the baseline, not baseline debt.
- Follow-up for S-03 and S-04: when they close, update the provisional rules in `tools/lint.py`, then regenerate the baseline.

