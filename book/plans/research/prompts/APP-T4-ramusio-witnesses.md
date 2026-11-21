# Deep research prompt — which manuscripts carry the passages labelled "Ramusio-only" (APP.T4)

**For:** `APP.T4` (the 2026-11-17 source review) and each chapter's `.T2`. Every passage the manuscript reproduces from Yule's Ramusian brackets is listed, as matched by `tools/lint.py` (80 passages in 28 chapters, 2026-11-18). Only Samara (III-3, Note 10) has been checked so far.
**Run** each batch as its own deep-research job. Save each output untouched, with a first line naming the tool, model and date:

| Batch | Passages | Save to |
|---|---|---|
| A | Prologue and Book I (Vol. I chapters): 27 | `plans/research/results/APP-T4-A-ramusio-witnesses-raw.md` |
| B | Book II (Vol. II chapters): 35 | `plans/research/results/APP-T4-B-ramusio-witnesses-raw.md` |
| C | Book III and the return Prologue (Vol. III chapters): 18 | `plans/research/results/APP-T4-C-ramusio-witnesses-raw.md` |

**Intake** (the trust rules in `research/README.md` apply; a row counts only when the intake sees the edition's text or apparatus):
- **R only:** keep "Ramusio-only." and the inline flag.
- **R and Z only:** relabel "Zelada- and Ramusio-only." and name the Zelada Latin in the inline flag (model: III-3, Note 10).
- **Also in an older witness:** drop the label and flag for the part the older witness carries; say in the Note what that witness has, citing the edition (`VOICE-GUIDE.md` § Apparatus conventions, *Ramusio and later layers*).
- **Cannot tell:** leave the label; note "exclusivity unchecked" in the Note only if a source suggests otherwise.
- Never edit `tools/ramusio-manifest.json` to make the lint pass; if a passage is no longer Ramusian, record the decision in the chapter's `.T2` and in `APP.T4`.

---

```text
BATCH A — Prologue and Book I (Vol. I chapters): which manuscripts carry Yule's Ramusian passages

I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, third edition revised by Henri Cordier (1903), with Cordier's Addenda (1920). Yule printed in square brackets the passages he took from Ramusio's Italian version (Navigationi et viaggi, vol. 2, 1559) because his French base text lacks them. My retelling labels each such passage in its endnote as "Ramusio-only."

WHY THIS IS A PROBLEM. Yule's brackets show where *his* edition took the text, not that Ramusio is its only witness. Ramusio drew on a lost Latin manuscript close to the Zelada Latin (Z, Toledo, Biblioteca Capitular 49.20), and some bracketed passages also stand, in whole or in part, in other witnesses: the Franco-Italian F (Paris, BnF fr. 1116), the Venetian V (Berlin, Hamilton 424), the Tuscan TA, the Venetian VA, Pipino's Latin P, the Latin L, and others. One case is already checked: for the camp at Samara (Book III, ch. 10), Simion's edition of V (Edizioni Ca' Foscari, 2019, § 3.2.3, printed p. 141) prints wooden defences in F and V and the 2,000 men and ditches in Z. So "Ramusio-only" was wrong there. I need the same check for every passage below.

FOR EACH NUMBERED PASSAGE, TELL ME
(a) Which witnesses carry it: F, Z, V, TA, VA, P, L, R (Ramusio), others. Say "whole", "part" (and which part) or "absent" for each witness you could check, and "not checked" for the rest.
(b) Your source for (a): the edition or apparatus, with chapter or paragraph number and page. The best sources mark witnesses passage by passage:
   - A. C. Moule and P. Pelliot, Marco Polo: The Description of the World (1938), which prints Z and R additions in distinct type with sigla;
   - L. F. Benedetto, Il Milione (1928), critical apparatus;
   - the Ca' Foscari digital edition of Ramusio's text, Dei viaggi di Messer Marco Polo (ed. E. Burgio, M. Eusebi, S. Simion, 2015), which annotates the source of each Ramusian passage;
   - A. Barbieri, Milione: redazione latina del manoscritto Z (1998);
   - S. Simion, Il Devisement dou monde nella redazione veneziana V (2019);
   - M. Eusebi's edition of F (2010/2018) and Ménard's Devisement du monde (2001–2009) for the French tradition;
   - Mascherpa's studies of Z and Ramusio (2018, 2025).
(c) A verdict: R only · R and Z only · also in F (or another older witness) · cannot tell from available sources.
(d) Any passage where Ramusio's wording looks like his own gloss or addition rather than a manuscript reading, with who says so.

PASSAGES (my chapter ID and endnote, Yule's Book.chapter locator, and the start of Yule's bracketed text)

1. [I-03, Note 16] YC Prol. 17: "For, to say nothing of the length and infinite perils of the way, when…"
2. [I-04, Note 7] YC 1.3: "on the summit of which snow is so constant that no one can ascend;…"
3. [I-04, Note 13] YC 1.4: "The said sea produces quantities of fish, especially sturgeon, at the river-mouths salmon, and…"
4. [I-05, Note 3] YC 1.5: "Near this province is another called MUS and MERDIN, producing an immense quantity of…"
5. [I-06, Note 3] YC 1.11: "From Tauris to Persia is a journey of twelve days.…"
6. [I-06, Note 15] YC 1.15: "Some one may say, “But the Saracens don’t drink wine, which is prohibited by…"
7. [I-07, Note 4] YC 1.18: "There are vast numbers of turtledoves, attracted by the abundance of fruits, but the…"
8. [I-07, Note 13] YC 1.19: "And to prove the great heat of this wind, Messer Mark related a case…"
9. [I-07, Note 14] YC 1.19: "And they have women who are mourners by trade, and do it for hire.…"
10. [I-08, Note 3] YC 1.20: "you arrive at a stream of fresh water running underground, but along which there…"
11. [I-08, Note 12] YC 1.25: "and the Castle with its Garden of Paradise was levelled with the ground…"
12. [I-09, Note 10] YC 1.29: "They go at a great pace even down steep descents, where other horses neither…"
13. [I-09, Note 15] YC 1.31: "The people of the province do not kill animals nor spill blood; so if…"
14. [I-10, Note 3] YC 1.32: "a great lake between two mountains, and out of it…"
15. [I-10, Note 3] YC 1.32: "Messer Marco was told also that the wolves were numerous, and killed many of…"
16. [I-10, Note 13] YC 1.35: "particularly of cotton. The inhabitants are also great craftsmen, but a large proportion of…"
17. [I-10, Note 14] YC 1.36: "with flax, hemp, wheat, wine, and the like…"
18. [I-10, Note -] YC 1.37: "as far as the city of Lop…"
19. [I-11, Note 4] YC 1.39: "Sometimes the stray travellers will hear as it were the tramp and hum of…"
20. [I-11, Note -] YC 1.39: "Hence in making this journey ’tis customary for travellers to keep close together. All…"
21. [I-11, Note 10] YC 1.41: "but to provide public hostelries for travellers…"
22. [I-11, Note 14] YC 1.43: "Travellers, however, dare not visit those mountains with any cattle but those of the…"
23. [I-12, Note 15] YC 1.53: "They say there is a Most High God of Heaven, whom they worship daily…"
24. [I-13, Note 4] YC 1.61: "at a spot in the Park where there is a charming wood…"
25. [I-13, Note 4] YC 1.61: "It is stayed on gilt and lackered columns, on each of which is a…"
26. [I-13, Note 4] YC 1.61: "They are cut across at each knot, and then the pieces are split so…"
27. [I-13, Note 4] YC 1.61: "against mishaps from the wind…"

OUTPUT FORMAT (required). (1) A findings table, one row per numbered passage, with columns: `#` · my ID and Note · witnesses carrying it (F / Z / V / TA / VA / P / L / R, each whole / part / absent / not checked) · verdict (R only / R and Z only / also in an older witness / cannot tell) · source (edition, chapter or paragraph, page) · confidence (high / medium / low). (2) Short prose only where a passage is split between witnesses or the sources disagree: name who holds which reading. (3) A bibliography of every source used, each with a BibTeX entry and a note on whether it is open access. (4) The passages you could not check, and why. **Rules:** do not invent page numbers, sigla, quotations, DOIs or URLs. If you inferred a witness's reading from a secondary source rather than an edition's text or apparatus, say so in the row. Say "not checked" rather than guess. Flag anything published after 2013 as **NEW**.
```
```text
BATCH B — Book II (Vol. II chapters): which manuscripts carry Yule's Ramusian passages

I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, third edition revised by Henri Cordier (1903), with Cordier's Addenda (1920). Yule printed in square brackets the passages he took from Ramusio's Italian version (Navigationi et viaggi, vol. 2, 1559) because his French base text lacks them. My retelling labels each such passage in its endnote as "Ramusio-only."

WHY THIS IS A PROBLEM. Yule's brackets show where *his* edition took the text, not that Ramusio is its only witness. Ramusio drew on a lost Latin manuscript close to the Zelada Latin (Z, Toledo, Biblioteca Capitular 49.20), and some bracketed passages also stand, in whole or in part, in other witnesses: the Franco-Italian F (Paris, BnF fr. 1116), the Venetian V (Berlin, Hamilton 424), the Tuscan TA, the Venetian VA, Pipino's Latin P, the Latin L, and others. One case is already checked: for the camp at Samara (Book III, ch. 10), Simion's edition of V (Edizioni Ca' Foscari, 2019, § 3.2.3, printed p. 141) prints wooden defences in F and V and the 2,000 men and ditches in Z. So "Ramusio-only" was wrong there. I need the same check for every passage below.

FOR EACH NUMBERED PASSAGE, TELL ME
(a) Which witnesses carry it: F, Z, V, TA, VA, P, L, R (Ramusio), others. Say "whole", "part" (and which part) or "absent" for each witness you could check, and "not checked" for the rest.
(b) Your source for (a): the edition or apparatus, with chapter or paragraph number and page. The best sources mark witnesses passage by passage:
   - A. C. Moule and P. Pelliot, Marco Polo: The Description of the World (1938), which prints Z and R additions in distinct type with sigla;
   - L. F. Benedetto, Il Milione (1928), critical apparatus;
   - the Ca' Foscari digital edition of Ramusio's text, Dei viaggi di Messer Marco Polo (ed. E. Burgio, M. Eusebi, S. Simion, 2015), which annotates the source of each Ramusian passage;
   - A. Barbieri, Milione: redazione latina del manoscritto Z (1998);
   - S. Simion, Il Devisement dou monde nella redazione veneziana V (2019);
   - M. Eusebi's edition of F (2010/2018) and Ménard's Devisement du monde (2001–2009) for the French tradition;
   - Mascherpa's studies of Z and Ramusio (2018, 2025).
(c) A verdict: R only · R and Z only · also in F (or another older witness) · cannot tell from available sources.
(d) Any passage where Ramusio's wording looks like his own gloss or addition rather than a manuscript reading, with who says so.

PASSAGES (my chapter ID and endnote, Yule's Book.chapter locator, and the start of Yule's bracketed text)

1. [II-03, Note 3] YC 2.13: "Further, you are not to suppose that everybody sits at table; on the contrary,…"
2. [II-03, Note 4] YC 2.13: "is set a large and very beautiful piece of workmanship in the form of…"
3. [II-03, Note 4] YC 2.13: "of the capacity of a firkin…"
4. [II-03, Note 4] YC 2.13: "And on the buffet aforesaid are set all the Lord’s drinking vessels, among which…"
5. [II-03, Note 5] YC 2.13: "There are certain Barons specially deputed to see that foreigners, who do not know…"
6. [II-03, Note 10] YC 2.15: "And you must know ’tis their custom in offering presents to the Great Kaan…"
7. [II-04, Note 2] YC 2.18: "They are obliged to approach the game against the wind, otherwise the animals would…"
8. [II-04, Note 6] YC 2.19: "The Two Brothers I have mentioned are bound by the tenure of their office…"
9. [II-04, Note 9] YC 2.20: "for he always travels in this way on his fowling expeditions, because he is…"
10. [II-04, Note 15] YC 2.22: "for the suburb of one gate spreads in width till it meets the suburb…"
11. [II-04, Note 15] YC 2.22: "There are in each of the suburbs, to a distance of a mile from…"
12. [II-05, Note 15] YC 2.27: "There is another trait of the Great Kaan I should tell you; and that…"
13. [II-05, Note 17] YC 2.30: "Moreover with that vast number of people, and the number of hot baths that…"
14. [II-05, Note 20] YC 2.32: "He also provides the poor with clothes. For he lays a tithe upon all…"
15. [II-06, Note 4] YC 2.37: "But at the end of five days’ journey out of those ten, they say…"
16. [II-06, Note -] YC 2.38: "This Golden King was a great and potent Prince, and during his stay at…"
17. [II-06, Note 8] YC 2.40: "On the lands adjoining this river there grow vast quantities of great canes, some…"
18. [II-06, Note 12] YC 2.43: "which signifies “the White City of the Manzi Frontier”…"
19. [II-07, Note 5] YC 2.47: "The chief city is also called Caindu, and stands at the upper end of…"
20. [II-07, Note 7] YC 2.47: "flat below and round above…"
21. [II-08, Note 9] YC 2.54: "The tomb likewise was plated partly with gold, and partly with silver.…"
22. [II-10, Note 2] YC 2.60: "There are also certain Christians at this place, who have a church.…"
23. [II-10, Note 2] YC 2.60: "A great river passes through it, on which much merchandise is carried to the…"
24. [II-12, Note 2] YC 2.71: "Indeed as it has a course of such great length, and receives so many…"
25. [II-12, Note 3] YC 2.71: "There are at many places on this river hills and rocky eminences on which…"
26. [II-13, Note -] YC 2.76: "And though the bridges be so high the approaches are so well contrived that…"
27. [II-13, Note -] YC 2.76: "Sometimes there would be at these palaces an hundred different parties; some holding a…"
28. [II-13, Note -] YC 2.76: "Both men and women are fair and comely, and for the most part clothe…"
29. [II-13, Note -] YC 2.76: "But as the Great Kaan’s couriers could not gallop their horses over the pavement,…"
30. [II-14, Note -] YC 2.80: "which they weave into various stuffs…"
31. [II-14, Note -] YC 2.80: "They also make much cotton cloth of dyed thread, which is sent all over…"
32. [II-14, Note -] YC 2.80: "And before this city came under the Great Kaan these people knew not how…"
33. [II-14, Note -] YC 2.82: "though on the other half he makes such a profit that he is always…"
34. [II-14, Note -] YC 2.82: "It is a charming country, and the people are very quiet, and fond of…"
35. [II-14, Note -] YC 2.82: "For you must know that throughout all Manzi they employ one speech and one…"

OUTPUT FORMAT (required). (1) A findings table, one row per numbered passage, with columns: `#` · my ID and Note · witnesses carrying it (F / Z / V / TA / VA / P / L / R, each whole / part / absent / not checked) · verdict (R only / R and Z only / also in an older witness / cannot tell) · source (edition, chapter or paragraph, page) · confidence (high / medium / low). (2) Short prose only where a passage is split between witnesses or the sources disagree: name who holds which reading. (3) A bibliography of every source used, each with a BibTeX entry and a note on whether it is open access. (4) The passages you could not check, and why. **Rules:** do not invent page numbers, sigla, quotations, DOIs or URLs. If you inferred a witness's reading from a secondary source rather than an edition's text or apparatus, say so in the row. Say "not checked" rather than guess. Flag anything published after 2013 as **NEW**.
```
```text
BATCH C — Book III and the return Prologue (Vol. III chapters): which manuscripts carry Yule's Ramusian passages

I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, third edition revised by Henri Cordier (1903), with Cordier's Addenda (1920). Yule printed in square brackets the passages he took from Ramusio's Italian version (Navigationi et viaggi, vol. 2, 1559) because his French base text lacks them. My retelling labels each such passage in its endnote as "Ramusio-only."

WHY THIS IS A PROBLEM. Yule's brackets show where *his* edition took the text, not that Ramusio is its only witness. Ramusio drew on a lost Latin manuscript close to the Zelada Latin (Z, Toledo, Biblioteca Capitular 49.20), and some bracketed passages also stand, in whole or in part, in other witnesses: the Franco-Italian F (Paris, BnF fr. 1116), the Venetian V (Berlin, Hamilton 424), the Tuscan TA, the Venetian VA, Pipino's Latin P, the Latin L, and others. One case is already checked: for the camp at Samara (Book III, ch. 10), Simion's edition of V (Edizioni Ca' Foscari, 2019, § 3.2.3, printed p. 141) prints wooden defences in F and V and the 2,000 men and ditches in Z. So "Ramusio-only" was wrong there. I need the same check for every passage below.

FOR EACH NUMBERED PASSAGE, TELL ME
(a) Which witnesses carry it: F, Z, V, TA, VA, P, L, R (Ramusio), others. Say "whole", "part" (and which part) or "absent" for each witness you could check, and "not checked" for the rest.
(b) Your source for (a): the edition or apparatus, with chapter or paragraph number and page. The best sources mark witnesses passage by passage:
   - A. C. Moule and P. Pelliot, Marco Polo: The Description of the World (1938), which prints Z and R additions in distinct type with sigla;
   - L. F. Benedetto, Il Milione (1928), critical apparatus;
   - the Ca' Foscari digital edition of Ramusio's text, Dei viaggi di Messer Marco Polo (ed. E. Burgio, M. Eusebi, S. Simion, 2015), which annotates the source of each Ramusian passage;
   - A. Barbieri, Milione: redazione latina del manoscritto Z (1998);
   - S. Simion, Il Devisement dou monde nella redazione veneziana V (2019);
   - M. Eusebi's edition of F (2010/2018) and Ménard's Devisement du monde (2001–2009) for the French tradition;
   - Mascherpa's studies of Z and Ramusio (2018, 2025).
(c) A verdict: R only · R and Z only · also in F (or another older witness) · cannot tell from available sources.
(d) Any passage where Ramusio's wording looks like his own gloss or addition rather than a manuscript reading, with who says so.

PASSAGES (my chapter ID and endnote, Yule's Book.chapter locator, and the start of Yule's bracketed text)

1. [III-01, Note 2] YC 3.1: "Moreover the larger of their vessels have some thirteen compartments or severances in the…"
2. [III-01, Note 5] YC 3.2: "and the King does not allow it to be exported. Moreover…"
3. [III-01, Note 6] YC 3.2: "In this Island some of the dead are buried, and others are burnt. When…"
4. [III-01, Note 10] YC 3.3: "Now the Island was very high in the middle, and whilst the enemy were…"
5. [III-02, Note 9] YC 3.7: "it is on the mainland…"
6. [III-03, Note 6] YC 3.9: "and when savage with any one they crush him under their knees and then…"
7. [III-03, Note 10] YC 3.10: "he landed with about 2000 men in his company; they dug large ditches on…"
8. [III-03, Note 10] YC 3.10: "for there is great store of wood there; and the Islanders having confidence in…"
9. [III-03, Note 10] YC 3.10: "as big as a man’s head…"
10. [III-03, Note 10] YC 3.10: "being sweet and savoury, and white as milk. The inside of the meat of…"
11. [III-05, Note 2] YC 3.16: "and these they put into a net bag tied round the waist, and mount…"
12. [III-06, Note 5] YC 3.20: "If a foreign merchant who does not know the ways of the country applies…"
13. [III-06, Note 7] YC 3.20: "Also if they meet any one who treats them well, they daub a little…"
14. [III-06, Note 11] YC 3.21: "All the people of this city, as well as of the rest of India,…"
15. [III-06, Note 25] YC 3.30: "but the most part are Saracens…"
16. [III-07, Note 4] YC 3.32: "The ambergris comes from the stomach of the whale, and as it is a…"
17. [III-07, Note 11] YC 3.33: "They brought (as I heard) to the Great Kaan a feather of the said…"
18. [III-09, Note 6] YC Prol. 17: "and his countenance showed great dissatisfaction…"

OUTPUT FORMAT (required). (1) A findings table, one row per numbered passage, with columns: `#` · my ID and Note · witnesses carrying it (F / Z / V / TA / VA / P / L / R, each whole / part / absent / not checked) · verdict (R only / R and Z only / also in an older witness / cannot tell) · source (edition, chapter or paragraph, page) · confidence (high / medium / low). (2) Short prose only where a passage is split between witnesses or the sources disagree: name who holds which reading. (3) A bibliography of every source used, each with a BibTeX entry and a note on whether it is open access. (4) The passages you could not check, and why. **Rules:** do not invent page numbers, sigla, quotations, DOIs or URLs. If you inferred a witness's reading from a secondary source rather than an edition's text or apparatus, say so in the row. Say "not checked" rather than guess. Flag anything published after 2013 as **NEW**.
```
