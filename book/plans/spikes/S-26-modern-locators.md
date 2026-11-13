# S-26 — Chapter locators in the most-cited modern works

**Status:** open · **Timebox:** 2–3 reading sessions (human) · **Depends:** S-24 pass B ✓ · **Gates:** locators in the Notes that cite the five works; the "no page you haven't seen" rule (`VOICE-GUIDE.md` § Citations)
**Origin:** the citation sweep after S-24 (2026-10-22).

## Question
Where, chapter by chapter (or page, if seen), do the five most-cited modern books make the points the Notes credit them with? And does each book actually say what the Note says?

| Key | Citations in the Notes | Copy to use |
|---|---|---|
| `larner1999marco` | 15 | Internet Archive lending copy `marcopolodiscove00john` (2001 paperback) |
| `haw2006marco` | 14 | Internet Archive lending copy `marcopoloschinav0000step` (2009 paperback) |
| `wood1995did` | 12 | library copy (no free copy found) |
| `vogel2013marco` | 12 | library copy; Brill preview pages |
| `rossabi1988khubilai` | 12 | Internet Archive lending copy `khubilaikhanhisl00ross` |

## Why it matters
- The Notes cite these books for specific positions, for example "Vogel on salt and money" or "Haw on the 1291 departure". At present they give no locator, so a reader cannot check them.
- The citations were attached by name (pass B). Nobody has yet confirmed that each book makes the exact point the Note credits it with. This is the step that catches a misattribution.

## Inputs
- The Notes citing each key: `grep -rn "@vogel2013marco" vol-*/` (and so on for each key)
- The lending copies above; Internet Archive's "search inside" finds a term within the book

## Method
1. For each key, list every Note that cites it, with the claim in one line.
2. For each claim, search inside the book. Record a chapter (preferred) or a page you have seen, plus a short paraphrase of what the book says.
3. Three outcomes per claim:
   - **confirmed**: add the locator, e.g. `[@vogel2013marco, ch. 5]`;
   - **different**: reword the Note to match what the book says;
   - **not found**: drop the citation, or move it to a book that does make the point.
4. Log the outcomes in `registry/locators.md` (key · Note · claim · locator · outcome).

## Output (definition of done)
- [ ] `registry/locators.md` with one row per citation of the five works
- [ ] Locators added in the Notes; "different" and "not found" outcomes fixed in the same pass (lint green on cite keys)

## Feedback to plan
- `VOICE-GUIDE.md` § Citations: an example locator from a real case
- Chapter backlogs: the "different" and "not found" cases, if they are not fixed directly

## Findings

- 2026-11-13: the [locator registry](../registry/locators.md) inventories
  all 65 citation occurrences. Wood and Rossabi have now been checked against
  readable 1996 and 2009 editions respectively, using chapter locators. Their
  24 original citation occurrences are recorded, including corrections. Vogel’s
  author preface supports two general references to his fiscal research. The
  remaining 39 await passage-level checks. The 1996/2009 chapter locations
  should still be checked against the cited 1995/1988 editions.
- Wood accepts the interpretation that Marco stayed rather than governed at
  Yangzhou (ch. 15), and describes his coal account as accurate (ch. 8). The
  Notes now reflect both points. Rossabi cites Polo on court feasts rather than
  supplying independent corroboration; the Note makes that dependence clear.
- Rossabi's 1988 biography predates Wood's 1995 thesis. It has been moved out
  of a list framed as replies, and removed from the claim that Chinese annals
  name Polo in the Ahmad episode: his account of Ahmad does not say that.
- The other passages have chapter search leads in the registry. Tables of
  contents and summaries do not by themselves establish the claims. The remaining
  passages and affected Notes still need the same direct check.

## Decision
_(fill when closing)_

## Tasks to create on close
- None if fixed in the same pass; otherwise the chapter's `.T4`
