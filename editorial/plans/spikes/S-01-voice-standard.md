# S-01 — Voice standard (pilot re-voice)

**Status:** closed (2026-10-21) · **Owner:** — · **Timebox:** 1–2 sessions · **Gates:** `.T3` re-voice tasks in every narrative chapter file

## Question
What exactly does a "retelling" look like, measured and by example? This spike is done when one fully re-voiced chapter is approved and the rules are written down.

## Why it matters
29 of 40 chapters are 45–80% verbatim Yule. If ~37 chapters get rewritten without a locked standard, voice drifts and the work is redone. The original "storyteller rewrite" failed exactly this way: a guide existed, but no measurable target.

## Inputs
- `VOICE-GUIDE.md`; I-1 (7% verbatim, the existing model)
- Pilot target **II-2 *Person & Palace*** (80% verbatim, Ramusio-heavy, at the length ceiling) and its backlog `tasks/chapters/vol-2/II-02-*.md`
- `critique/vol-*.md` voice findings (hinge tics, recaps, first-person Book voice, aside length)

## Method
1. Re-voice II-2 applying its whole backlog (W1–W3 items included), so the pilot is also the template for a full chapter pass.
2. Measure: verbatim %, quote budget used, hinge counts, aside lengths, words.
3. Human read: does it sound like I-1? Is anything lost (facts, flavour, citations)?
4. Iterate once if needed, then extract the rules.

## Output (definition of done)
- [x] II-2 rewritten (`vol-2/ch-02-person-palace.md`) and approved by a human read (2026-10-21)
- [x] `VOICE-GUIDE.md` v2: quote budget, opener rotation list, aside cap, recap rule, first-person rule, banned phrases, Ramusio tag variants, re-voice checklist
- [x] Numeric thresholds handed to S-02 (see Decision)
- [x] Before/after excerpt kept below as the reference for chapter agents

## Feedback to plan
- `content-revision-plan.md` § W4: confirm or adjust the threshold (25%?), the order, and the batch size
- `VOICE-GUIDE.md`: v2

## Findings

**Measurements, II-2 before → after** (`tools/seed/overlap.py`, `stats.py`, narrative only):

| Measure | Before | After | I-1 (model) |
|---|---|---|---|
| Verbatim Yule (7-gram) | 80% | **3%** | 7% |
| Narrative words | 3,167 | 1,894 (−40%) | 1,984 |
| Avg sentence length | 29.1 | 22.5 | 23.1 |
| Archaisms (hath, foison, sundry, whilst…) | 18 | 0 | 1 |
| "You must know" | 4 | 0 | 0 |
| "Anyway" | 3 | 0 | 2 |
| Formula hinges (narrates / according to the book / next he mentions) | 7 | 0 | 2 |
| Book first person outside quotes | 0 (but "the Book will tell" ×3) | 0 | 0 |
| Marked Yule quotations (excl. epigraph) | — | 6 (max 1 per scene) | — |
| Asides | 4 (max ~125 words) | 2 (80, 72 words) | 2 |
| Citations / Notes | 20 / 20, two stub Notes | 20 / 20, no stubs | 15 / 15 |
| Ramusio-only passages flagged | 2 of 10 | 10 of 10 | — |

The 3% that remains is the epigraph and the six marked quotations, i.e. all of it is intentional.

**What the pilot showed**

1. **Verbatim % collapses as soon as you retell scene by scene.** The 25–30% target in the critique and plan is far too loose: it would let a chapter keep a third of Yule's sentences. 15% (raw, including marked quotes and epigraph) leaves room for quotation and still fails I-2 (28%).
2. **Length drops ~40% in a catalogue chapter**, not the ~10% the cut plan expected (−300 +60). Nothing factual was lost: every Yule fact in II.viii–xi is still there, compressed. The palace inventory (arsenal by arsenal, gate by gate) shrinks most. II-2 now sits near the 1,800 floor; II-3, II-8 and other catalogue chapters will behave the same. The over-length problem in W4 largely solves itself.
3. **Ramusio flags are the new tic risk.** Ten flags in one chapter (II-2 is the Ramusio-heaviest) produced "Ramusio" ten times. Rotating five tag forms kept it readable, but S-03 should approve the variants and allow grouping adjacent Ramusian details under one flag.
4. **The old hinges were the voice.** v1 *prescribed* "Anyway, next he mentions…" and "He says that…"; the critique's tic counts are the guide working as written. v2 replaces them with an opener rotation and a cap per attribution verb.
5. **I-1 is a model for verbatim, not for structure.** It has two "Anyway" exits and a two-paragraph closing recap. From now on II-2 is the reference; I-1 needs a light T3 (exits + closing recap) like everything else.
6. **Facts touched during the pilot** (for S-06): Chingkim's death date: Yule's own note says "12th moon of 1284–1285, aged 43" (so it *is* in refs, contrary to the backlog), but the *Yuan shi* date (Zhiyuan 22, 12th month) is January 1286; text now says "winter of 1285–86", Note [6] marked *to verify*. Silences aside: tea known to Persian writers; foot-binding elite and mostly southern; masonry wall largely Ming. All standard; Note [20] marked *to verify*.
7. **Dependency shortcuts taken.** S-03 (apparatus) and S-06 (facts) are still open. The pilot used the critique's proposed conventions (◇ Ramusio-only suffix, [M] instead of [V/M], stub Notes merged). If S-03 decides otherwise, II-2's Notes need a mechanical update, not a re-voice.

**Before / after (reference excerpt)**

Before (Green Mount, 95% Yule):

> Moreover on the north side of the Palace, about a bow-shot off, there is a hill which has been made by art from the earth dug out of the lake; it is a good hundred paces in height and a mile in compass. This hill is entirely covered with trees that never lose their leaves, but remain ever green. And wherever a beautiful tree may exist, and the Emperor gets news of it, he sends for it and has it transported bodily with all its roots and the earth attached to them, and planted on that hill of his. […] and hence it is called the Green Mount; and in good sooth 'tis named well.

After:

> A bowshot north of the palace rises a hill made by hand (from the earth dug for the lake, Ramusio adds), a hundred paces high and a mile round, planted with trees that never lose their leaves. Here Polo gives one of the great pictures of the Book. Whenever the Kaan hears of a beautiful tree anywhere, he has it dug up whole, roots and earth and all, and carried to his hill by elephants, however big it is, until he owns the finest trees in the world. […] People call it the Green Mount, and Polo approves: *"in good sooth 'tis named well."*

Before (aside, 125 words, exit formula):

> — A quick note on the numbers: Chinese lists give about ten legitimate sons; Hammer twelve; Polo's twenty-two is likely an early clerical error for twelve (*dodeci* in one manuscript). Chingkim was not literally named "for Chinghis," and he was not quite the eldest—an older brother Dorjé existed; he died in the twelfth moon of 1284–85 aged forty-three. […] Anyway, so much for the person and the blood. Now the Book must tell of the house in which that person winters.

After (72 words, no exit; the next paragraph simply starts "Winter is the season of the capital."):

> — The Chinese records trim this. They know of ten or twelve lawful sons, so "twenty-two" is probably a copyist's slip for twelve. Chingkim was not quite the eldest, since an older brother, Dorjé, seems to have died young, and his name has nothing to do with Chinghis. Chingkim himself died in the winter of 1285–86, while the Polos were still in China, and Temür did succeed his grandfather in 1294.

Before (closing recap, 113 words) → after (one forward sentence):

> Inside these walls the court now comes to life: the feasts, the robes of gold, and the twelve thousand Keshican.

## Decision
_Closed 2026-10-21 on human sign-off of II-2._

- **Standard:** `VOICE-GUIDE.md` v2, with II-2 as the reference chapter.
- **Thresholds for S-02 lint** (narrative = text above `## Notes`, minus title lines):
  - verbatim Yule 7-gram share ≤ 15% (incl. epigraph and marked quotes);
  - marked quotations ≤ 2 per scene / ≤ 8 per chapter, ≤ 25 words each; every quotation found in `refs/`;
  - archaisms outside quotes = 0; Book first person outside quotes = 0; "You must know" outside quotes = 0;
  - "Anyway" ≤ 1; formula hinges ≤ 3 in total; any single attribution verb ≤ 4 (excluding "says nothing");
  - asides ≤ 80 words, ≤ 4 per chapter; no aside ends in an exit formula;
  - no opening recap; closing paragraph ≤ 1 sentence / ≤ 25 words when it is a forward pointer;
  - narrative 1,800–3,200 words; average sentence ≤ 25 words (warning only);
  - every Ramusio bracket match carries an inline flag and a "◇ Ramusio-only" Note.
- **W4 adjustments:** threshold 15% (not 25–30%); order unchanged; batches of 3–4 chapters per human-read session; the length cut plans are superseded by the re-voice itself (re-check length after, don't cut before); add a light T3 for I-1 and I-2.

## Tasks to create on close
- [x] `<ID>.T3` written into all 39 narrative chapter files (incl. reception chapters III-10, III-11), with measured targets: verbatim %, worst blocks by line, unflagged Ramusio passages (matched against the 211 bracketed passages in `refs/`, saved as `tools/seed/ramusio-brackets.txt`), long asides, recaps, restatements, tic counts, and a W4 order/batch number. Generator: `tools/seed/revoice_targets.py` (seed for S-02's lint). The essay III-12 and front/back files are outside this gate.
- `II-02.T3` itself is the pilot and is done, and II-02's remaining tasks shrink to T4 (S-03 convention check), T5 (media) and T6 (lint).
