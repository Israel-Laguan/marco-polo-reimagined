# S-26 — Chapter locators in the most-cited modern works

**Status:** closed (2026-11-16) · **Timebox:** 2–3 reading sessions (human) · **Depends:** S-24 pass B ✓ · **Gates:** locators in the Notes that cite the five works; the "no page you haven't seen" rule (`VOICE-GUIDE.md` § Citations)
**Origin:** the citation sweep after S-24 (2026-10-22).

## Question
Where, chapter by chapter (or page, if seen), do the five most-cited modern books make the points the Notes credit them with? And does each book actually say what the Note says?

| Key | Citations in the Notes | Copy to use |
|---|---|---|
| `larner1999marco` | 15 | Internet Archive lending copy `marcopolodiscove00john` (2001 paperback) |
| `haw2006marco` | 14 | Internet Archive lending copy `marcopoloschinav0000step` (2009 paperback) |
| `wood1995did` | 12 | Internet Archive lending copy `didmarcopologoto0000wood_x0z1` (1995) for chapter structure; 1996 Westview full text for the passages |
| `vogel2013marco` | 12 | 2013 full text (Internet Archive public copy); author preface |
| `rossabi1988khubilai` | 12 | Internet Archive lending copy `khubilaikhanhisl00ross` |

## Why it matters
- The Notes cite these books for specific positions, for example "Vogel on salt and money" or "Haw on the 1291 departure". At the start of the spike they lacked locators, so a reader could not check them.
- The citations were attached by name (pass B) before their particular claims were checked against the books. This spike tests those attributions.

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
- [x] `registry/locators.md` with one row per citation of the five works
- [x] Locators added in the Notes; "different" and "not found" outcomes fixed in the same pass (lint green on cite keys)

## Feedback to plan
- `VOICE-GUIDE.md` § Citations: an example locator from a real case
- Chapter backlogs: the "different" and "not found" cases, if they are not fixed directly

## Findings

- 2026-11-13 (superseded by the 2026-11-16 entries below): the [locator registry](../registry/locators.md) inventories
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
- At that interim stage, the other passages had chapter search leads only;
  the later passes below record the subsequent claim checks.

- 2026-11-16 (final pass): every one of the 65 rows got an outcome
  (Internet Archive search-inside on the lending copies, page ranges fixed
  from contents pages and running heads; see the registry's "Final pass").
  Some Larner and Wood rows rested on chapter ranges rather than a reread
  passage; the re-check below closes that gap. The four pending rows closed: Larner on
  the Nayan battle's Arthurian diction (ch. 6, p. 109) and on the 1295 return
  (ch. 2, p. 43); Haw on Shangdu (ch. 5, p. 69); Haw on the first-journey
  chronology (ch. 3, pp. 47–49: a correction, see below). Two unpinned rows
  were pinned: Larner on Yangzhou (ch. 3, p. 63) and Haw on 1295 (ch. 3, p. 51).
- Wood's chapter locators (8, 11, 15) and Rossabi's (2, 4, 5, 6, 7, 8) hold
  in the cited 1995 and 1988 editions, with one Rossabi exception below.
- Corrections in this pass: (1) Larner's reply to the omission argument and to
  Wood is ch. 3 (pp. 59–62), not ch. 10, which covers 17th–18th-century
  sceptics; five Notes fixed. (2) Rossabi's tea/foot-binding omission passage
  is ch. 5 (p. 148), not ch. 6; vol-2/ch-02 [20] fixed. (3) Haw never discusses
  the manuscript "1250"; he dates the first journey by Golden Horde and
  Chaghadaid reigns (Barak, 1266–71), not Ilkhanid/Yuan ones; vol-1/ch-02 [3]
  reworded. (4) Haw's arrival date (1274 or 1275) is ch. 3 p. 50, with the
  Hangzhou framing at ch. 5 p. 68; the earlier evidence came from a
  publisher's abstract and is replaced. (5) Haw on Yangzhou widened to
  chs. 11–12 (pp. 165, 173).

- 2026-11-16 (passage re-check, Larner and Wood): every Larner and Wood row
  now records the passage, edition and page (registry, "Passage re-check").
  Three corrections: (1) Larner does not argue for an invented traveller
  persona: ch. 3 defends the Genoa collaboration and shows Rustichello
  casting Marco's geography in Arthurian formulas (pp. 50, 57) and adding the
  Yangzhou and Saianfu boasts (pp. 63–64); vol-1/ch-01 [12] and its body
  sentence reworded, locator chs. 3, 5. (2) Larner disputes that Columbus's
  annotated Polo shaped the 1492 project (ch. 9, pp. 153–156: copy probably
  received c. 1497–98, some postils after the Second Voyage, no decisive
  trace in the *Diario*); vol-3/back-01 [5] and its body sentence now mark
  the link disputed. (3) Larner's "finite medieval readers" point is ch. 7
  (p. 131), not only ch. 6; vol-3/ch-10 [10] now cites chs. 6–7. All 12
  Wood rows hold, with pages from the 1996 text inside the 1995 chapter
  ranges (coal p. 67; tea and bound feet pp. 72–75; Wall pp. 96, 101;
  *sejourna* p. 133; second journey unlikely p. 149).

## Decision
Closed. Totals across the 65 occurrences, including earlier passes: 44
confirmed (35 outright, 9 for part of a list Note); 18 corrected (11 different
claim, 7 wrong locator; one of these, Rossabi on the Ahmad naming claim, drops
the citation from that claim); 3 removed as not found (Haw on Kashmir, Vogel
on Hormuz and on Kesmacoran); 0 unresolved.
Example locator for `VOICE-GUIDE.md`: `Wood [-@wood1995did, ch. 11]` on the
Great Wall, already the guide's example and now verified in the 1995 edition.
The affected chapter `.T4` tasks link to the registry so later edits preserve
the checked scope and corrections; their broader apparatus work remains open.

## Tasks to create on close
- None if fixed in the same pass; otherwise the chapter's `.T4`
