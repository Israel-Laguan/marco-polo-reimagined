# S-18 follow-up — Research intake (2026-11-12)

The [supplied follow-up report](S-18-followup-raw.md) answers the [follow-up prompt](../S-18-follow-up-prompt.md). It is preserved verbatim. This intake audits it and carries the usable results into the registry. As in the [first intake](S-18-intake.md), `verified` means only that the source says this.

## Trust check

**Verdict: the best run so far for this spike.** It reports access levels honestly and makes real primary-text reads (EI XII, Talbot, Moule–Pelliot vol. I and Maffeo's will, Dayalan, Rougeulle, Hall, Nilakanta Sastri). But it has one systematic error and several invented "corrections to the brief".

1. **Pelliot page numbers: the report's "correction" is wrong.** It treats Toyo Bunko scan-image numbers as printed pages. The offsets are fixed and already in the project: in vol. I, Çipingu is printed pp. 608–609 at scan 0624 (offset +16); in vol. II, Dagroian is printed p. 613 at scan 0017 (offset −596). So:
   - BASMAN at "scan 0102" = **printed p. 86**. The project's locator, pp. 86–87, was right.
   - SEMENAT at "scan 0234" = **printed p. 830**, as the prompt said.
   - SAGAMONI BORCAN at "scan 0227" = printed p. 823.
   - FERLEC, LAMBRI and PENTAN were "not reachable" only because the report looked for printed 725/761/802 among scans that run to about 300. They are at scans **0129, 0165 and 0206**, well inside the folder.
   The entry *content* it read is still usable, at the printed pages.
2. **Invented brief errors.** The prompt never gave Dayalan's subtitle as "with Special Reference to Tamil Nadu"; it gave the title the report then "corrects" to. Nor did it place the Cocachin episode in Book III: it said "Book III and the return voyage". In this series the return is III-09 by design; in Yule it is Prologue ch. XVIII, and ch. 19 in Moule–Pelliot. Ignore both "corrections".
3. **Its explanation of 8 vs 18 is half right.** Yule says that the French text he translated (Pauthier's) has 8, and that the G.T. (the Geographic Text, Moule–Pelliot's base MS F) has 18. These are **two manuscript readings**, not Yule's private choice. Moule–Pelliot follows F, so 14 ships and 18 survivors. Yule's text has 13 and 8.
4. **Citation errors in its own bibliography**, checked on Crossref and doi.org (2026-11-12):

| Report gives | Check | Correct |
|---|---|---|
| Lambourn 2008, "…Seeing Gujarat in the World of Southeast Asian Islam" | wrong subtitle | "Tombstones, Texts, and Typologies: Seeing Sources for the Early History of Islam in Southeast Asia", *JESHO* 51 (2008): 252–286, doi:10.1163/156852008x307447 |
| Favi, *Self Through the Other*, 2020 | wrong year | Ca' Foscari, **2018** (ISBN 978-88-6969-237-6; chapter DOIs 10.30687/978-88-6969-237-6/…) |
| *Current Science* 2019: authors, pages and DOI "unconfirmed" | resolves | Ikeda Yoshifumi, Randall Sasaki, Kimura Jun, 117(10): 1635–1639, doi:10.18520/cs/v117/i10/1635-1639 |
| Sasaki 2015 typed `@article` | type | a book (Texas A&M UP) |
| Dayalan DOI 10.22679/avs.2019.4.1.025 | not in Crossref; doi.org resolves (KoreaScience) | keep it |
| Rougeulle, doi:10.4000/cy.3442 | resolves; sole author | keep it |
| Conlan review, *The Historian* 79(4) | resolves, doi:10.1111/hisn.12714 | keep it |

## Checked findings

| ID | Finding | Verdict and limits | Destination |
|---|---|---|---|
| FU-1 | **Basman (Pelliot I pp. 86–87):** in northern Sumatra, between his Ferlec and Sumatra entries. MS forms *basarom/besarom/bosaram* (VA) and *basmam/basmon* (FA, P). | Verified at OCR-fragment level; printed page per the offset above. He gives a region, not Pasai by name, in what was read. | `basma` note; GAZ.T6 |
| FU-2 | **Semenat (Pelliot II p. 830):** all MSS read *Semenat*. Pelliot emends to *Somenat* = Somnath, citing the Medici chart's "Somenath" (via Hallberg p. 468). | Verified (single-page OCR fragment). It supports the row's Somnath reading with Pelliot's own authority. | `semenat` note; GAZ.T6 |
| FU-3 | **Fleet and losses.** Moule–Pelliot (MS F): **14** ships, **18** survivors. The death figures differ by witness: FA, P 600; FB 500; LT/TA 700 (or 600 men + 100 women); V 600 + 100 women; VB "more than 600"; R about 600 dead "of mariners and others". | Verified as OCR of M&P vol. I pp. 90–91 and apparatus. Some sigla are OCR-damaged (L's "plusquam centum"). No editorial verdict was found. The 13 of Yule's text was not located in the M&P apparatus; that is an OCR coverage gap, not proof it is missing. | S18-F1/F2; III-09; A16; C11 |
| FU-4 | **Motupalli:** *EI* XII no. 22, ed. **E. Hultzsch**, pp. 188–197, Śaka 1166 = 1244–45. Ganapatideva gives up the old royal claim to wrecked cargo: everything beyond the fixed duty (*klipta-śulka*) goes to "those who have incurred the great risk of a sea-voyage". | Verified on third-party OCR of *EI* (not a plate image). Ganapati, not Rudrama, issued it. The term *abhaya-śāsana* is a later scholars' label, not seen in the text. | III-06; F-31 |
| FU-5 | **Rudrama Devi (Talbot 2001):** daughter and successor of Ganapatideva, r. **1263–1289** (p. ix); took a masculine persona and reportedly led troops (p. 135). Talbot treats the Motupalli charter as Ganapati's (pp. 73, 131). No reissue by Rudrama was found in about half the book. | Verified (archive.org OCR). **Resolves F-31: Yule's "widow" is corrected to daughter.** A reissue is unproven (absence of evidence, half the book searched). | F-31 → corrected; III-06 |
| FU-6 | **The Trebizond loss.** Maffeo Polo's will (6 Feb. 1309 m.v. = 1310) records a *dampnum* of about **4,000 hyperpera** caused by "the lord Comnenus of Trebizond". It credits about **1,000 lire** that Marco received from the Doge and Commune "for part of the loss done to us". Marco's own will (1324) is silent. The identification is Orlandini 1926's, as reported by Moule–Pelliot. | Verified as M&P's quoted Latin (short OCR fragments). The will says **loss**, not robbery; how it happened is not stated. Orlandini (`orlandini1926marco`, already in the bib) was not read. "Robbed" in Britannica and History.com is unsourced elaboration. | III-09 / III-10 aside; back-01 |
| FU-7 | **Kayal (Dayalan 2019):** a Pandya-era port that flourished in the 12th–14th centuries. Material evidence: Caldwell's 1861 coin hoard, including a coin of Peter of Aragon (1276), plus Chinese celadon and porcelain. | Verified (full text). The article gives no 1280s–90s date for Kayal itself; tying the coin to Polo's decade is our inference. | III-05 Note; `cail` |
| FU-8 | **Qalhat (Rougeulle 2017):** "the only port mentioned by Marco Polo on the Omani coast". Governor Ayāz from about 1280; a succession crisis ended in the 1291 murder of Sayf al-Dīn Nuṣrat. Outer quarters were not settled before the late 13th century; kilns worked in the late 13th and early 14th; wall bases sit on 13th–14th-century ceramics. The Friday mosque date (c. 1290–1311) is her interpretation. | Verified (about 70% of the full text read). Keep text, material evidence and inference apart, as she does. | III-08 Note; `calatu` |
| FU-9 | **Maabar (Nilakanta Sastri 1929):** Polo's eldest of the five brothers ("Asciar") = **Maravarman Kulaśekhara I**. The *Mahāvaṃsa* and Chinese envoys from 1280 also speak of five brothers. **Sonder Bandi** = Jaṭāvarman Sundara Pāṇḍya, acceded **c. 1276**; his highest regnal year (17, inscription no. 594 of 1907) falls in **1292–93**, and Waṣṣāf puts his death in AH 692. | Verified (OCR, page about 181 and 188–189). The other four brothers are not named. **Always print the regnal dates**: three rulers share the name. The I/II/III numbering is Wikipedia's. Karashima 2014 was not read. | III-05 Note |
| FU-10 | **Java's spices (Hall 2011, pp. 226–227):** Polo overstates Java as a producer. Java was an entrepôt, trading its rice for Banda/Moluccan nutmeg, Timor sandalwood and Sumatran pepper. Hall's Malāyu = **Jambi**, with Temasek as a separate place. Hall puts Polo at Samudra in 1292. | Verified (OCR; the page may be off by one). It closes the first run's unsourced inference (raw row 23). Hall uses Malāyu, not Polo's "Malaiur". | III-02 Note; `malaiur` |
| FU-11 | **Pasai gravestone:** Moquette first published it (1913, via Lambourn). Fatimi, and Lambourn as reported, reject a Cambay origin for *this* stone. Lambourn, as reported, dates the surviving stone about two centuries after 1297 (a replacement); Ismail et al. 2022 argue it is contemporary. No source links it to Polo. | **Disputed.** Third-hand for Lambourn and Guillot–Kalus. Do not call the stone "the oldest evidence of Islam" without this dispute. | III-03 Note (hedged) |
| FU-12 | **Takashima.** KOSUWA (Hayashida Kenzō) worked in Imari Bay from 1991; in 2001 they found a hull with iron-fastened planking and a bulkhead fragment. Ikeda Yoshifumi's 2011 find was a ~12 m keel (ship ≥ 20 m). His storm case rests on four anchors pointing south. Ikeda himself notes a Goryeo record that 80% of the Eastern Route Army got home. Sasaki's publisher hedges on hull origin ("no conclusive statements"); Conlan's review says southern Chinese timber. | Magazine/news-level for the excavations; review-level for Sasaki. The *Current Science* metadata is now confirmed (above). | III-01 aside; A15 caption |
| FU-13 | **Chipangu and the Konjikidō:** no mainstream Polo scholar was found making the link. Favi 2018 reads the golden palace as a literary trope (the "land of gold" moving from China to Japan). Ōkubo 2000, a numismatist, argues a Chūson-ji rumour could have reached China through trade with the Song; he does not say "Konjikidō". | Verified (Favi ch. 1 and Ōkubo full text). Larner is known only from a review. | III-01; ch-12: present the Konjikidō as a later popular link, with Ōkubo as a minority view |

## Gazetteer — S-04 / GAZ.T6

- `basma`: keep **probable** (Pasai). Add the Pelliot note (FU-1). Pelliot's region (northern Sumatra, between Ferlec and Samudra) is consistent with the point; he does not prove Pasai in what was read.
- `semenat`: keep **probable**. Pelliot emends to Somenat = Somnath (FU-2), so the reading is now Yule's *and* Pelliot's. The point remains the Somnath area.
- `locac`, `malaiur`, `dagroian`: no change. Hall's Malāyu = Jambi (FU-10) agrees with `malaiur`.
- `GAZ-pelliot-locators.csv`: unchanged; its pages were right.

## Still open

These need a person with library access, or Toyo Bunko read by eye at the scan numbers above:
- Pelliot's FERLEC (scan II/0129), LAMBRI (0165), PENTAN (0206) and SEILAN.
- Orlandini 1926's own wording on Trebizond.
- Trimingham 1952 and Pankhurst 1982 on Yagbeʾa Ṣeyon; Taddesse Tamrat.
- Lambourn 2003/2008 and Guillot–Kalus 2008 read directly.
- Karashima 2014 on the Pandyas.
- Miksic 2013 on Malaiur.
- Sasaki 2015's own chapters.
- CiNii/J-STAGE: 金色堂 + マルコ・ポーロ.

None blocks a Vol. III draft: each has a hedge in the table above.
