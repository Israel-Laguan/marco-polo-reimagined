# Final access check — intake and best-effort closure (2026-11-17)

This is the last research pass ([prompt](../2026-11-17-final-access-check-prompt.md)). The tool ran it in two passes: an automated one ([FINAL-ACCESS-1-raw.md](FINAL-ACCESS-1-raw.md)) and a browser follow-up in the user's Chrome ([FINAL-ACCESS-2-raw.md](FINAL-ACCESS-2-raw.md)). The tool and model were not stated. Final count: **14 accessed, 8 partial, 8 blocked.** The browser pass verified several readings on page images. The other readings are OCR, or text that went through the tool's summariser.

**Closure rule (user decision):** anything still blocked is **closed as best effort**. The hedged wording already in the manuscript stands, and the gap is recorded here and not chased again.

## Spot check: 11 readings, 11 hits (100%)

Each reading was checked here, independently of the tool. The checks used archive.org djvu text, Wikisource raw text, the RM 2024 PDF (pdftotext) and the saved ANU HTML.

| # | Item | Checked here | Result |
|---|---|---|---|
| 1 | 9 Rockhill 1915 | Running text: "Kan-mai-li (Comoro islands"; the entry heading reads "Comoro Islands (?)"; Hormuz is a separate entry (Hu-lu-mo-ssu) | **Hit** |
| 2 | 7 Rubruck p. 85 | "sweat with horror and surprise, for I had never drunk of it. It seemed to me, however, very palatable" | **Hit** |
| 3 | 7 Rubruck pp. 66–67 | "leaves a taste of milk of almonds on the tongue" | **Hit** |
| 4 | 18a Hammer p. 391 | "Sie gaben ihm ein aus Schwefel und Merkur zusammengesetztes Mittel als die Panacee der Lebensverlängerung" | **Hit** |
| 5 | 1 Orlandini doc. 6 | Heading "6. 1310. 6 febbraio. — Testamento di Matteo Polo seniore"; "sororibus Juliane et Clare filiabus anime"; "condam Marthe uxori mee" | **Hit** |
| 6 | 12 *Nancun chuogeng lu* j. 1 | 雲都赤 「負骨朶於肩」; a separate entry 「國朝鎮殿將軍，募選身軀長大異常者充…大漢衣粮」; 玉斧 occurs 0 times | **Hit** |
| 7 | 5a *Yuan shi* j. 114 | 「名察必，弘吉剌氏…生裕宗」, with no birth year | **Hit** |
| 8 | 8 Gibb (1992 reprint) | "The port of Zaytun is one of the largest in the world… about a hundred large junks" | **Hit** |
| 9 | 23 Maspero 1911 | "Le Champa se trouvait ainsi délivré des Mongols" | **Hit** |
| 10 | 15b Formentin–Schiavon 2024 | *bocheta*: "'gioiello d'oro e di gemme', dal lat. bŭcca"; the *boghta* reading "è un abbaglio che continua a essere ripetuto"; the *tola* glossed as paiza | **Hit** |
| 11 | 11 de Rachewiltz 2002 | "the Wall, as we know it, did not exist in Marco's time. As shown by A.N. Waldron…"; "Marco was certainly never the governor of that city, although he may have held a temporary position… as inspector or court appointed commissioner" | **Hit** |

These items were not checked here and are taken on the browser pass's page-image reading:
- *Tashrīf* p. 172 (Noorlib);
- the *Yuan dianzhang* 廿 (shidianguji);
- the BnF Arabe 5847 folios and metadata (Gallica);
- Cleaves p. 181 (JSTOR preview);
- *Viatica* §§4 and 18;
- Hammer's title page.

## What changes

### Applied to the manuscript

1. **II-03 Note [5].** The Note said that the *Ch'ue keng lu* has "athletes with clubs and jade axes". The text instead has club-bearing attendants (雲都赤) and, in a separate entry, a picked guard of unusually tall men (鎮殿將軍, "大漢"). The tall men are not given clubs, and juan 1 has no jade axes. Palladius's paraphrase, as cited by Yule (`refs/yule-vol1.txt`, II.13 note), adds two guards beside the Khan holding "natural" jade axes. The Note now says the giants' staves combine the two.
2. **II-11 Note [5] and I-11 Note [17].** Both now cite `derachewiltz2002wood` beside the 1997 article. II-11 adds his position: never governor, but perhaps a temporary inspector or court-appointed commissioner.

### Registry and tasks

- **bibliography.bib**
  - `derachewiltz2002wood` added (confirmed; full HTML read).
  - The `derachewiltz1997marco` comment corrected: hdl 1885/41883 is the 2002 paper, not the ZAS article.
  - `formentin2023inventario` now notes the page conflict: 169–204 (Ateneo Veneto, RM 2024) against 167–202 (IRIS).
- **characters.yaml and characters.md (Maffeo).**
  - The will is dated *more veneto* 1309, i.e. 6 Feb 1310 modern. This reconciles Yule's 1309 with Gullino's 1310.
  - Marta is his dead wife.
  - Juliana and Clara are nuns of Santa Caterina di Mazzorbo, "filiabus anime mee". The will therefore does not support Bruno's "two natural daughters".
  - Dorjé's mother stays open: the *Yuan shi* (j. 107, 114) names none.
  - Chabi's entry already records that the *Yuan shi* gives no birth year, so no change was needed.
- **facts.md**
  - F-53: the *Yuan dianzhang* summary table reads 七月廿日, the 20th.
  - F-59: de Rachewiltz's replies recorded (from the 2002 paper).
  - F-61: Hammer p. 391 seen as a page image.
- **comparanda.md**
  - Rubruck p. 55 dropped (the page is about carts and houses).
  - The Rockhill 1915 Hormuz lead withdrawn, because Rockhill identifies Kan-mai-li (甘埋里) tentatively as the Comoros.
  - Gibb page numbers and rights added.
  - Cleaves: only p. 181 seen.
  - *Tashrīf*: pp. 170–173, with the death at p. 172.
- **visual-references.md and PLT**
  - Arabe 5847 is dated 634 AH / 1236–37.
  - f. 119v (the ship) and f. 138r (the village) are confirmed.
  - ff. 10r, 19r and 101r are **not caravans**: seated men beside a camel, a mounted procession, and a camel herd.
  - The PLT folio check is marked done.
- **scholarship.md:** `gadrat2026marco` has now been read. Its main points:
  - reading the deathbed anecdotes as doubt is "un contresens" (§4);
  - John Green (1747) was the first to note the missing Wall (§18);
  - sinologists did most to refute Wood (§§22–23).
- **Tasks**
  - Handoffs added to III-07 (*Tashrīf* pages), III-02 (Maspero, *Pararaton*), III-06 (Hammer p. 391) and II-04 (*Yuan dianzhang*).
  - II-03 records the applied fix.
  - **APP.T8 is closed best effort.**
- **Board:** a decisions-log row was added, and research is marked closed.

### Rights (item 10)

| Work | US | UK/EU |
|---|---|---|
| Rockhill 1900 and 1915 | PD | PD |
| Yule–Cordier 1903 with Cordier's 1920 addenda | PD | PD |
| Gibb 1929 | PD | **Protected to 31 Dec 2041** (Gibb d. 1971) |

Any Gibb wording in a UK/EU edition must be paraphrased. The book already cites Gibb–Beckingham (`gibb1958travels`) only for positions, and no verbatim Gibb was found in the manuscript. One rights point is unverified: Amy Frances Yule's memoir in the 1903 edition, because her death date was not checked.

## Closed as best effort

These items stay unread. In each case the manuscript keeps its present hedge, and no further pass is planned.

| # | Item | Obstacle | Where the hedge lives |
|---|---|---|---|
| 2 | Bolognari 2021, Agnes's will (the Latin naming her father) | not openly available | III-10, III-B1 ("as reported") |
| 3 | Gallo 1957–58, Bellela 1326–28 | not digitized | III-10 Note [8] (via Bolognari 2020) |
| 5b | A scholarly reconstruction of Chabi's birth year | not found | `characters.yaml` (no age computed) |
| 6 | Cleaves 1976, beyond p. 181 | JSTOR login | II-05, III-09 Comparative clauses |
| 11 | de Rachewiltz 1997 (ZAS) itself | not online | cited alongside the 2002 paper |
| 13 | Dutschke 1993 | catalogue only | I-01 [15], III-12 [4] |
| 14 | Haw 2023, 2024 (ZDMG) | not open access | III-09, III-12 |
| 15a | Schiavon et al. 2023, full text and page range | no open file | the bib note on pages |
| 17 | Mostaert, Natigay | catalogue only (*Oriente Poliano*, year 1957 inferred) | I-12 Note [15] |
| 18b | Quatremère p. 194 | viewer renders no pages | III-06 (Hammer suffices) |
| 19 | Thackston, Rashid | no lawful copy | III-09, III-12, I-12 |
| 20b | Cook 2020, on the page | no lawful copy | III-07 (Arabic pp. 170–173 now cited) |
| 21 | Aubin 1969; Jackson 1999 App. III | not on Persée; lending restrictions | I-07 Note [7] |
| 22 | *Yuan dianzhang* full article 禁治打捕月日 | not located in the scan | II-04 [15] (summary table read) |
| 23b | Champa's tribute (Maspero) | only p. 592 | III-02 |
| 24 | *Pararaton*, translation page | not read | III-02 |
| 25 | Twynam 1902, p. 24 | HathiTrust search-only | S-21 / III-05 |
| 26 | Wen et al. 1980 | not found; **title unverified, do not cite** | II-07 |
| 27 | Weisgerber 2004 | not found; **possibly misattributed, do not cite** | S-21 |
| 28 | The Arabe 5847 colophon page; the Maqama number of f. 138r | not viewed | `visual-references.md` |
| 29 | Met, *Legacy of Genghis Khan* catalogue numbers | PDF not opened | PLT |
| 30 | Luce, Pagan murals | no authorised copy | PLT |

**Still owed by the manuscript, outside this pass:**
- A page-image check of the OCR-only quotations, if any of them is quoted verbatim in print: Orlandini clause page, Gibb's 1929 pagination, the Brandes translation page.
- The Venice ASVe originals (already best effort).
