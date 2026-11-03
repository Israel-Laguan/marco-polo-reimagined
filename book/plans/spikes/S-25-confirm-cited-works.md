# S-25 — Confirm the unconfirmed works the Notes already cite

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** the Notes that cite these four keys (11 citations); `registry/bibliography.bib` status comments
**Origin:** the citation sweep after S-24 (2026-10-22): of 104 bibliography entries, four that are marked unconfirmed are already cited in the Notes.

## Question
For the four works below, what is the exact bibliographic record (journal volume and pages, dissertation title, imprint), confirmed from a catalogue record, a DOI, or the item's own title page?

| Key | Cited | What is unconfirmed | Where it matters |
|---|---|---|---|
| `derachewiltz1997marco` | 6 citations | Journal, volume, year and pages of de Rachewiltz's "Marco Polo Went to China" | The presence debate (I-01, I-11, I-B1, III-12) |
| `dutschke1993francesco` | 2 citations | Exact dissertation title, university and year | Manuscript tradition (I-01, III-12) |
| `atwood2004encyclopedia` | 1 citation | Imprint (Facts on File, New York, 2004?); no catalogue record found so far | I-13 (Yuan capitals) |
| `tao1959nancun` | 1 citation | Zhonghua shuju 1959, series 元明史料筆記叢刊; catalogue records cited by the research were unreachable | I-13 (Palm Hall, juan 21) |

## Why it matters
These keys carry argument, especially de Rachewiltz 1997, the main scholarly reply to Wood, which the Notes cite six times. A Works cited list with a wrong volume or title for that entry would undercut the very point the Notes make.

## Inputs
- `registry/bibliography.bib` (the four entries and their status comments)
- `research/results/CIT-A-raw.md` (de Rachewiltz, Dutschke, Atwood as first identified); `CIT-decisions-2-raw.md` (Nancun chuogeng lu)

## Method
1. Run the prompt below; save the output to `research/results/S-25-raw.md`.
2. Intake: open each record yourself (CrossRef, Open Library, WorldCat, a university repository, ProQuest's dissertation abstract page). Update each entry and its status comment. If a work cannot be confirmed, decide with the user whether the Notes keep citing it (with a hedge) or drop it.

## Deep research prompt

```text
I am finishing the bibliography for a new English retelling of Marco Polo's book, in Chicago author-date style. Four works are already cited in my endnotes, but their bibliographic details are unconfirmed. For each, give the exact record and the evidence for it: a catalogue record (WorldCat, a national or university library), a DOI or CrossRef record, a publisher's page, or a scan of the title page. If you cannot confirm a detail from such a source, leave it blank and say so. Do not answer from general knowledge.

1. Igor de Rachewiltz, "Marco Polo Went to China". I believe it appeared in Zentralasiatische Studien 27 (1997). Confirm the journal, volume, year and page range, and give a stable URL if a copy is online (the author's own posting at the Australian National University, or a library repository).
2. Consuelo Wager Dutschke's doctoral dissertation on the manuscripts of Francesco Pipino's Latin version of Polo (University of California, Los Angeles, 1993?). Confirm the exact title, university, year and the ProQuest or UMI number.
3. Christopher P. Atwood, Encyclopedia of Mongolia and the Mongol Empire (New York: Facts on File, 2004?). Confirm the publisher, city, year and ISBN.
4. 陶宗儀 Tao Zongyi, 南村輟耕錄 Nancun chuogeng lu (Beijing: Zhonghua shuju, 1959, in the series 元明史料筆記叢刊?). Confirm the publisher, year and series, and whether the 1959 printing or a later one (1980, 1997, 2004) is the one normally cited.

OUTPUT FORMAT (required). (1) A table with columns: # · the confirmed record (all fields) · the evidence (source name and URL) · what you could not confirm · confidence. (2) BibTeX for each confirmed work, with a note giving its status. (3) A list of what you could not confirm, and why.

Rules: do not invent volume numbers, page ranges, ISBNs, dissertation numbers or URLs. Do not cite a review or a secondary mention as if it were the record itself; say when a source is secondary. If a catalogue is not reachable, say so.
```

## Output (definition of done)
- [ ] `research/results/S-25-raw.md` saved
- [ ] The four entries in `registry/bibliography.bib` updated, each with a status comment saying what was opened
- [ ] For any work that stays unconfirmed: the user's decision (keep with a hedge, or drop from the Notes)

## Feedback to plan
- `registry/bibliography.bib`: the four entries
- Chapter backlogs: only if a citation has to change or be dropped

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- None expected, unless a citation has to change (then the chapter's `.T4`)
