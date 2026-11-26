# S-25 raw — confirm the four cited works

Run in-session on 2026-11-13 (web search plus opening each record), in place of the external deep-research run. Every row says what was actually opened.

## (1) Table

| # | Confirmed record | Evidence (opened) | Not confirmed | Confidence |
|---|---|---|---|---|
| 1 | Igor de Rachewiltz, "Marco Polo Went to China," *Zentralasiatische Studien* 27 (1997): 34–92. A review article on Wood 1995. Additions and corrections in *ZAS* 28 (1998): 177. | The author's own posting at ANU, "F. Wood's *Did Marco Polo Go to China?* A critical appraisal" (2002 working paper), cites it as "Zentralasiatische Studien 27 (1997), pp. 34-92" and gives the 28 (1998) corrections in note 1: https://openresearch-repository.anu.edu.au/bitstream/1885/41883/1/Marcopolo.html (record: http://hdl.handle.net/1885/41883). The same citation appears in Rossabi's Asia for Educators essay and in the Wiley *Literature Compass* and Firenze UP bibliographies (secondary). | No library catalogue or table of contents for *ZAS* 27 was opened. No DOI exists; the article itself is not online. | High: the author's own statement, matched by three independent bibliographies. |
| 2 | Consuelo Wager Dutschke, "Francesco Pipino and the Manuscripts of Marco Polo's 'Travels'" (PhD diss., University of California, Los Angeles, 1993). Distributed by UMI Dissertation Services, Ann Arbor. | WorldCat OCLC 494165759 (https://search.worldcat.org/oclc/494165759): the search listing shows the title, 1993, thesis, UMI Ann Arbor; the record page itself was behind a bot check. The Innsbruck Marco Polo project bibliography (uibk.ac.at, seen in search results; the page returned empty when fetched) gives the same title and "Diss. University of California, Los Angeles, 1993." Ca' Foscari articles (2019, 2024) cite it as the basic study of Pipino's manuscripts (secondary). | The ProQuest/UMI order number was not found. The full WorldCat record page was not readable. | High for title, university and year; none for the UMI number. |
| 3 | Christopher P. Atwood, *Encyclopedia of Mongolia and the Mongol Empire* (New York: Facts on File, 2004). x, 678 pp. Series: Facts on File Library of World History. ISBN 0-8160-4671-9 (978-0-8160-4671-3). LCCN 2003061696. | Open Library edition OL11359625M (JSON opened: Facts on File, July 2004, 678 pp., ISBN-10/13, LCCN, LC call no. DS798.4 .A88 2004, OCLC 52901464; built from LC, Harvard and Columbia MARC records). CiNii Books NCID BA69362002 (opened: New York, Facts on File, c2004, x, 678 p., 29 cm, series, ISBN 0816046719). Reviewed in *Journal of Asian Studies* 65, no. 3 (2006): 613–15 (secondary). | Nothing. (Open Library's title field has a typo, "Mongolian"; CiNii and the LC data give "Mongolia".) | High. |
| 4 | 陶宗儀 Tao Zongyi, 南村輟耕錄 *Nancun chuogeng lu*, Yuan Ming shiliao biji congkan 元明史料筆記叢刊 (Beijing: Zhonghua shuju, 1959). 13, 385 pp. Later printings carry ISBN 7-101-01727-4. | NDL Search a1000034269 (opened): 北京 : 中華書局, 1959.2, 13, 385p, series 歴代史料筆記叢刊. 元明史料筆記叢刊, ISBN 7101017274, described from the 4th printing (2004.4). CiNii BA36769092 (opened): same book, 中華書局, 1997.11, 湖北第3次印刷, 13, 385p, ISBN 7101017274, 35 holdings. | Which printing scholars "normally" cite: both catalogues treat 1959 as the edition and later dates as reprints of the same 13+385 pp. setting, so 1959 is the edition date to cite. The 1959 text itself was not opened; juan 21 was read on Wikisource (Sibu congkan). The Academia Sinica and Shanghai records from CIT-decisions-2 were not reopened. | High for the imprint and series. |

## (2) BibTeX

As entered in `registry/bibliography.bib` (biblatex fields).

```bibtex
@article{derachewiltz1997marco,
  author       = {de Rachewiltz, Igor},
  title        = {Marco Polo Went to China},
  journaltitle = {Zentralasiatische Studien},
  volume       = {27},
  date         = {1997},
  pages        = {34--92},
}

@thesis{dutschke1993francesco,
  author      = {Dutschke, Consuelo Wager},
  title       = {Francesco Pipino and the Manuscripts of Marco Polo's Travels},
  type        = {phdthesis},
  institution = {University of California, Los Angeles},
  date        = {1993},
}

@book{atwood2004encyclopedia,
  author    = {Atwood, Christopher P.},
  title     = {Encyclopedia of Mongolia and the Mongol Empire},
  publisher = {Facts on File},
  location  = {New York},
  date      = {2004},
  isbn      = {978-0-8160-4671-3},
}

@book{tao1959nancun,
  author    = {Tao, Zongyi},
  title     = {Nancun chuogeng lu [南村輟耕錄]},
  series    = {Yuan Ming shiliao biji congkan},
  publisher = {Zhonghua shuju},
  location  = {Beijing},
  date      = {1959},
}
```

## (3) Not confirmed, and why

1. The page range 34–92 from a catalogue or the journal's table of contents. *ZAS* has no DOI and no online index was found; the range rests on the author's own citation (plus three secondary bibliographies). This is enough for a Works cited entry.
2. The UMI/ProQuest number for Dutschke. Not printed in any source found; ProQuest Dissertations is subscription-only. Chicago does not require it.
3. The full WorldCat record for Dutschke (bot check); title and year come from the WorldCat listing and the Innsbruck bibliography.
4. The 1959 Zhonghua text of the *Nancun chuogeng lu* itself; the Palm Hall sentence was checked on Wikisource (Sibu congkan), as before.
