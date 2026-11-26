# Intake: enrichment leads, Batch C (Inner Asia)

_2026-11-10. Raw run: `ENR-C-inner-asia-raw.md` (tool not stated; prompt `prompts/ENR-enrichment-leads.md` Batch C). Applies to `registry/enrichment.md` E22, E42, E43, E46a, E51, E52._

## Trust check

**Verdict: about 5 of 7 citations hold (71%), below the bar. One of its "not found" verdicts is wrong.** The intake read the sources it could open. Three items move on that reading. Do not re-run; the rest needs a library.

| Run cites | Check | OK? |
|---|---|---|
| Menshikova 2025, doi:10.1016/j.joics.2025.100014, "open access" | DOI resolves (Crossref: Maria L. Menshikova). **Not open access:** the Crossref licence is Elsevier's standard user licence, and ScienceDirect returns 403. Museums, dating and Chabi's dates are not seen. | partial |
| Houtum-Schindler 1909, *JRAS*, pp. 154–162 | Crossref: "Marco Polo's Travels; New Editions; His 'Arbre Sol' not 'Sun-Tree', but Cypress of Zoroaster", *JRAS* 41 (1909): 154–162, doi:10.1017/s0035869x00038417. The 1909 volume's index (IA `in.ernet.dli.2015.24463`) lists "Marco Polo, his Arbre Sol, 154"; the article's own OCR is not usable | yes |
| Pelliot, *Notes*, "Dry (Lone) Tree" | consistent with the index locator already in `GAZ-citable-findings.md` (DRY (LONE) TREE, p. 630; not read) | yes |
| Iranica "Bāydū", URL given | opens: Bertold Spuler, "BĀYDŪ", *Encyclopaedia Iranica* III/8, pp. 887–888 (1988) | yes |
| Haw 2014, "The Persian Language in Yuan-Dynasty China: A Reappraisal", *East Asian History* 39 | opens (eah.anu.edu.au/39/haw/). The run says it does not discuss Acbalec. **It does** (below). | yes (the work) / no (the verdict) |
| Dang Baohai 2006, Kunlun, ISBN 978-7-80040-820-5 | title, publisher and year are confirmed by a scholarly footnote (Korean journal article, accesson.kr), not a catalogue. ISBN not found on Open Library | partial |
| Nedashkovsky 2000 | not found on Open Library; unchecked | — |

## What the intake saw

| Item | Seen | Source |
|---|---|---|
| **E46a** | Bāydū, son of Ṭaraḡāy and grandson of Hülegü, "reigned as il-khan in Iran from Jomādā I to Ḏu'l-qaʿda, 694/March–October, 1295". Gaykhatu was put to death on his order on 6 Jomādā I 694 / 24 March 1295. He was captured near Naḵčevān and "executed on Tuesday, 23 Ḏu'l-qaʿda 694/4 October 1295". Ghazan was enthroned at Tabrīz and converted to Islam on 29 Ḏu'l-ḥejja 694 / 9 November 1295. Bāydū "relied on Christian counselors". | Spuler 1988, Iranica online |
| **E51** | Haw on Polo's two Acbalecs. The first is Zhending: Polo's "Acbalec" is Turkic, "White City", where Rashīd al-Dīn uses the Mongolian "Chagha'an Balghasun". On the second, "Acbalec Mangi", Pelliot "sees a Persian construction, 'Aq-balïq-i-Manzi'". Haw: "It might just as well be an Italianate, or Frankish, or perhaps Latin, construction: 'Acbalec [di/de] Mangi'." **Correction to the lead:** the article is "The Persian Language in Yuan-Dynasty China: A Reappraisal", *East Asian History* 39 (Dec. 2014), not an article on Acbalec. Pelliot's reading is Persian, not plain Turkic. | eah.anu.edu.au/39/haw/ (HTML; print pages not seen) |
| **E42** | A real source for the link: Houtum-Schindler's 1909 *JRAS* article argues, as its title says, that Polo's "Arbre Sol" is "not 'Sun-Tree', but Cypress of Zoroaster". The text was not read. Not seen: the primary sources for the cypress (Shāhnāma, Yāqūt, *Tārīkh-i Bayhaq*), the felling under al-Mutawakkil (861), and anything by Adrienne Mayor. | Crossref; *JRAS* 1909 index |
| E22 | Nothing beyond the Crossref record; the article is paywalled | — |
| E43 | Nothing seen. The run's "Selitrennoye is now New Sarai, Old Sarai unlocated" rests, by its own account, partly on Wikipedia | — |
| E52 | Title, publisher and year (党宝海《蒙元驿站交通研究》, Beijing: Kunlun, 2006) are cited in a scholarly footnote. No catalogue record has been seen. | — |

## Applied

- `enrichment.md`: E46a, E51 → **verified**; E42 → **verified** (source exists, by title; contents not read); E22 → **library**; E43 and E52 stay **claimed**, with the run's leads noted.
- `bibliography.bib`: `spuler1988baydu`, `haw2014persian`, `houtumschindler1909marco`.
