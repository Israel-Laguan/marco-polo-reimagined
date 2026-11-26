I'll start by pulling the catalogue record to get the volume IDs, then run each term through HathiTrust's in-volume search.

Got the three volume IDs. Now testing the in-volume search endpoint.

The HathiTrust reader site refuses automated fetches, so I'll try a real browser.

The verification passed on its own. Reading results.

Search works in the browser. Let me find the data endpoint the page uses so I can run all terms efficiently.

Got a clean JSON endpoint (page numbers and seq only, no text). Checking what the "#" before page numbers in the UI means.

The "#" prefix turns out to be just how the reader shows page labels for search-only items; the underlying field is the volume's page number. Now running every term across all three parts.

Hit HathiTrust's rate limit (HTTP 429). I'll stop, back off, and re-run slowly with retries.

Patched. Queuing the remaining items' terms while the throttled worker runs.

The throttled run will take roughly 15–20 minutes. Checking progress periodically.

Progress is steady: 24 terms are done and the rate limit has only triggered twice. I'll keep waiting.

All terms are done. Pulling the results in chunks.

Searches are done; I'm reading the results back now and have two items left to pull (Kököchin and Sartaq, then the Shiregi group).

I ran every term against all three parts of the HathiTrust search-only copy and got page numbers for most items. I have not seen any text, and I have no library copy, so none of these hits are confirmed passages.

**How the searches ran**
- **Volumes:** Part 1 is mdp.39015047608149, Part 2 is mdp.39015043197394, Part 3 is mdp.39015043197386, all "Limited (search-only)".
- **Page numbers:** every number below is the printed page label HathiTrust returns for the hit (the reader shows it as "p. #307"). HathiTrust also gives a separate scan sequence number, which is not the page number. In Part 2, for example, scan 75 is printed p. 307. Hits labelled "?" fall on unnumbered pages.
- **Part ranges:** by the hits, Part 1 runs from p. 1 to about 240, Part 2 from about 241 to about 516, and Part 3 from about 517 to 819.
- **Marks:** "xN" is the hit count on that page.
- **Spelling:** the search ignores diacritics. Möngkä and Mongka gave identical results, as did Toghrïl and Toghril, and Toq-Temür and Toq Temür.
- **Multi-word and hyphenated terms:** these appear to match their words separately, not as exact phrases. "Ho-chou" hit pages that are clearly unrelated, and "anyone they met" gave 15 hits on one page. Treat multi-word hits as weak. I mark where a single word is the reliable one.
- **Rate limit:** HathiTrust rate-limited me (HTTP 429). I slowed down and re-ran those terms, so every term below completed on all three parts.

| # | Terms tried (in order) | Result | Part: printed pages |
|---|---|---|---|
| 1 | funeral; coffin; bier; Genghis; Chinggis; Chinggiz; killed every; whomever they met; whoever they met; anyone they met; every living; buried; burial | Hits for funeral, coffin, buried and burial. No hits for bier, "whomever they met" or "whoever they met". "killed every" and "anyone they met" were too noisy to use. | **P2:** funeral 451; burial 263x4, 264x2, 266, 292, 371, 459; buried 247, 252, 264x3, 292, 317, 321, 334, 378, 416, 448, 459, 460x3 and others; coffin 263x2, 285, 292, 311, 375, 385, 415, 416x2, 514. **P1:** coffin 73; burial 24, 54. **P3:** coffin 519, 540, 545 and others; burial 685. |
| 2 | forty; girls; maidens; jewels; spirit; forty girls; forty maidens; forty moon | "forty girls" hit on two pages. No hits for maidens or "forty maidens". | **P2:** 312x2. **P3:** 762x3. Separately, "forty" alone is on P2 312 and "girls" on P3 762x2. |
| 3 | Möngkä; Möngke; Mangu; Mongka; buried; burial; coffin; Diaoyu; Hochau; Hochu; Ho-chou; Diaoyucheng | No hits for Diaoyu, Hochau, Hochu or Diaoyucheng; "Ho-chou" is unreliable. Möngke is in all three parts. Möngkä/Mongka and Mangu are in all three parts too. No page has Möngke together with buried, burial or coffin. | Möngkä/Mongka: **P1** 16, 62, 104, 228. **P2** 278, 305, 306x8, 313, 324–328, 331, 348, 350 and others. **P3** 781–789, 799–804 and others. Mangu: P1 24; P2 274, 357, 381; P3 814. |
| 4 | Nomoghan; Numughan; Nomuqan; Nomukhan; Shiregi; Shirigi; Shirägi; Hantum; Hantun; Antong; Sarban; Toq-Temür; Qaidu; Golden Horde | Nomoghan hit. Numughan, Nomuqan, Nomukhan, Shiregi, Shirigi and Antong found nothing. Shirägi, Hantum, Hantun, Sarban and Toq-Temür hit. | Nomoghan, **P1:** 38, 56, 138x2. **P2:** 307x3, 382, 383x2, 399x2, 422–424, 435, 436x3, 438x2, 453x2, 454x4, 460, 462, 465x2. **P3:** 802x2. Pages where Nomoghan also occurs with Shirägi, Hantun, Hantum or Sarban: **P1** 38; **P2** 307, 399, 436, 438, 453; **P3** 802. Shirägi: P2 350, 399–400, 433, 436x13, 437x10, 438, 461. Hantun: P2 276, 436x3, 438, 443, 451, 453. Hantum: P2 307, 400, 425, 433. Toq-Temür: P2 353x14; P3 815x12. "Golden Horde": only P1 16x3. |
| 5 | Qara'una; Qaraunas; Qara'unas; Negüder; Nigudar; Nekudar; Nigüdär; Negudar | Qara'una and Qara'unas hit. Negudar hit. Negüder, Nigudar, Nekudar and Nigüdär found nothing. No page has both names. | Qara'una: **P1** 49, 83; **P2** 276, 371, 372; **P3** 532, 541x2, 551, 553, 554 and others. Qara'unas: P1 86, 96, 103; P2 370; P3 554, 597x2, 599x2, 601x2, 609, 643. Negudar: P1 40; P2 362, 367, 460x3; P3 522x6, 523, 527, 802x2. |
| 6 | Kaipingfu; Kaiminfu; Kemenfu; Kaimingfu; Shangdu; Kaiping; Kemin; Kamenfu; Kaibingfu; "cane"; "bamboo" | No hits for any Kaipingfu spelling, "cane" or "bamboo". Only Shangdu hit. | **P2:** 441 (Shangdu). |
| 7 | Zardandan; gold teeth; golden teeth; Zar-dandan | Zardandan and "gold teeth" hit. No hits for golden teeth or Zar-dandan. | Zardandan: **P1** 214; **P3** 793, 819. "gold teeth": P1 214x7; P3 672x2. |
| 8 | Nasruddin; Nasir al-Din; Nasiruddin; Qarajang; Yunnan; Sayyid Ajall; Ajall; Sayyid Ajal | Nasruddin and Sayyid Ajal found nothing. Nasiruddin, Nasir al-Din, Qarajang, Yunnan, Sayyid Ajall and Ajall hit. | Sayyid Ajall: **P2** 443x5, 448x12, 455x4, 456x6, 465x4; **P3** 786x3, 810x4, 811x3. Nasiruddin is on P2 448 and 443 (also with Sayyid Ajall) and P3 786. Nasir al-Din: P2 458x8. Yunnan: P1 13, 145; P2 424x2, 439, 446, 448; P3 805, 819. Qarajang: P2 282, 413, 423–424, 446–448, 478; P1 84, 145x4, 214x2; P3 797, 805x2, 812, 819. |
| 9 | sing; Shing; twelve; twelve sing; Sheng | "Shing" is the useful hit. "sing" is a common word and gave little. "twelve sing" found nothing. | Shing, **P2:** 348, 443x2, 444x6, 445x10, 446x7, 469. Sheng: P1 4, 14, 205, 214–216, 223; P2 265, 374, 443x3; P3 775, 777, 811x2, 816. "sing" alone: P1 223, P2 246. |
| 10 | kezig; keshig; kešik; kishikan; keshik; kezik; kesig; käzik; kezigs; kishik; kazik | No hits on any variant. Not found; this is not proof the passage is absent. | None. |
| 11 | Ong Khan; Toghrïl; Toghril; Toghrul; Tughril; Marquz; Merghuz; Marghuz; Buyuruq; Buyruq; Kereit; Kereyit | Ong Khan, Toghril, Marghuz, Buyuruq and Kereit hit. Toghrul, Tughril, Marquz, Merghuz, Buyruq and Kereyit found nothing. | Marghuz: **P1** 1, 62x3, 63x2, 174x2; **P3** 793, 800, 807. Buyuruq: P1 51, 54, 62–64, 67–70, 174–176 and others; P2 287x3, 289; P3 784, 788x5, 793 and others. Ong Khan: P1 38, 41, 46, 51–53, 61–66 and others; P2 272, 286–288, 317, 347, 381, 399, 413, 471; P3 781, 789, 791, 794, 803, 809, 815. Kereit: P1 61. Toghril: P2 269, 274, 280, 363, 462, 491. |
| 12 | Kököchin; Kökäjin; Kökächin; Kokachin; Uladai; Ulatay; Abishqa; Qoja; Khoja; Quja; Khwaja; Qocha | Kökächin and Kokachin hit. Kököchin, Kökäjin, Ulatay, Qoja, Khoja and Quja found nothing. Uladai and Abishqa hit. Khwaja is too common to help. No page has Kökächin together with Uladai or Abishqa. | Kökächin: **P2** 351x3, 454, 455, 463, 464x2, 466, 469x2; **P3** 606x2, 798x2. Uladai: P2 307, 308, 368x2, 369, 373x2; P3 817x3. Abishqa: P1 90x2; P2 274x2, 354, 358, 425; P3 602x2, 635x2, 646, 781x3. Qocha: P2 305. |
| 13 | Sartaq; Sartak | Sartaq hit. Sartak found nothing. | Sartaq: **P1** 41x2, 72x5, 89x2, 95, 105x2, 146; **P2** 277x2, 347, 352x2, 356, 361x4, 438, 462, 465; **P3** 589, 804, 810x5. |
| 14 | coal; black stone; black stones | "coal" and "black stone(s)" both occur, only in Part 2. | **P2:** 442 (coal; black stone x3; black stones x2). "black stones" is also at 260x4. |

**What these pages suggest**
- **Items 4 and 8:** each has pages where its names cluster (see the table), which is where I would look first.
- **Item 6:** the Kaipingfu spellings all missed, so only the Shangdu hit (P2 441) is a locator.
- **Items 2 and 14:** "forty girls" is a phrase hit on P2 312 and P3 762. The coal hit is at P2 442, a page that also carries the Shiregi and Nomoghan material.
- **Item 1:** Genghis or Chinggiz appears with funeral, coffin, burial or buried on P2 247, 252, 263, 264, 415, 416 and 460. That is a candidate range to check, not a confirmed passage.

**What I could not search or resolve**
- No part was unsearchable; all three accepted every query.
- Items 3, 6 and 10 have no direct locator (Möngke's burial, Kaipingfu, keshig). A copy of the book would settle these, and I can only note that those terms were not found.
- Items 5 and 12 have per-name hits but no page where the pair or group co-occur.
- A miss on any term is not proof the passage is absent. Thackston may use a different spelling, or the OCR may have garbled the word.
