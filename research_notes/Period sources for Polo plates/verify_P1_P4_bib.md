# Verification pass: P1, P2, P4, Bibliography

Checked 2026-11-13 against `reports/Period sources for Polo plates.md`. Format: item → status → evidence.

## 1. Bibliography entries flagged `% UNCERTAIN`

- **sasaki2015lostfleet** → CORRECTED: publisher and year confirmed (Texas A&M University Press, 2015; ISBN 978-1-62349-194-9 cloth, 978-1-62349-230-4 e-book; 224 pp. on MUSE). Address not confirmed: one review gives "Houston, TX", which is probably wrong, so the address field is dropped. The thesis title is singular ("Origin") and the book title is plural ("Origins"); both are correct as given. → https://muse.jhu.edu/book/38210 ; https://openlibrary.org/isbn/9781623491949 ; https://api.crossref.org/works/10.1111/hisn.12714
  ```bibtex
  @book{sasaki2015lostfleet,
    author = {Sasaki, Randall J.},
    title = {The Origins of the Lost Fleet of the Mongol Empire},
    publisher = {Texas A\&M University Press}, year = {2015},
    isbn = {978-1-62349-194-9}, note = {NEW}
  }
  ```
- **karakorum_vol1** → CORRECTED: editors are Bemmann, Erdenebat and Pohl. The print edition is Reichert, Wiesbaden, 2010 (338 pp.). The DAI digital edition with the DOI is 2022. Title in the record: "Mongolian-German Karakorum Expedition". → https://api.datacite.org/dois/10.34780/133a-8dr5 ; https://openlibrary.org/isbn/9783895006975
  ```bibtex
  @book{karakorum_vol1,
    editor = {Bemmann, Jan and Erdenebat, Ulambayar and Pohl, Ernst},
    title = {Mongolian-German Karakorum Expedition, Vol. 1: Excavations in the Craftsmen Quarter at the Main Road},
    series = {Forschungen zur Arch{\"a}ologie Au{\ss}ereurop{\"a}ischer Kulturen}, volume = {8},
    publisher = {Reichert}, address = {Wiesbaden}, year = {2010},
    isbn = {9783895006975}, doi = {10.34780/133a-8dr5},
    note = {DAI digital edition 2022}
  }
  ```
  The subtitle "Excavations in the Craftsmen Quarter at the Main Road" was not in either record. It is STILL UNCONFIRMED.
- **conlan2001divine** → CORRECTED (minor): the title and year are confirmed. The publisher is the East Asia Program, Cornell University, in the Cornell East Asia Series no. 113. Ithaca. 302 pp. ISBN 1-885445-13-X. → https://openlibrary.org/isbn/9781885445131
  ```bibtex
  @book{conlan2001divine,
    author = {Conlan, Thomas D.},
    title = {In Little Need of Divine Intervention: Takezaki Suenaga's Scrolls of the Mongol Invasions of Japan},
    series = {Cornell East Asia Series}, number = {113},
    publisher = {East Asia Program, Cornell University}, address = {Ithaca, NY}, year = {2001},
    isbn = {1-885445-13-X}
  }
  ```
- **watt2010khubilai** → CONFIRMED: Yale University Press is the co-publisher. Imprint: New York, Metropolitan Museum of Art / New Haven, Yale UP, 2010, 342 pp. The statement of responsibility reads "James C.Y. Watt; with contributions by Maxwell K. Hearn ... [et al.]". → https://openlibrary.org/isbn/9781588394033
  ```bibtex
  @book{watt2010khubilai,
    author = {Watt, James C. Y. and others},
    title = {The World of Khubilai Khan: Chinese Art in the Yuan Dynasty},
    publisher = {Metropolitan Museum of Art and Yale University Press}, address = {New York and New Haven}, year = {2010},
    isbn = {978-1-58839-403-3}
  }
  ```
- **unesco2011xanadu** → CONFIRMED for the year. ICOMOS records the dossier as "Date received by the World Heritage Centre: 20 January 2011". The site was inscribed in 2012. The author as "People's Republic of China" (the State Party) is the normal convention but the dossier itself was not opened (390 MB). Direct file: https://whc.unesco.org/uploads/nominations/1389.pdf. → https://whc.unesco.org/document/152541 ; https://whc.unesco.org/en/list/1389/documents/
- **lambourn2008tombstones** → CONFIRMED: title, journal, volume 51 and issue 2 are as given. Added from the record: pages 252–286 and the DOI. → https://api.crossref.org/works/10.1163/156852008x307447
  ```bibtex
  @article{lambourn2008tombstones,
    author = {Lambourn, Elizabeth},
    title = {Tombstones, Texts, and Typologies: Seeing Sources for the Early History of Islam in Southeast Asia},
    journal = {Journal of the Economic and Social History of the Orient},
    volume = {51}, number = {2}, year = {2008}, pages = {252--286},
    doi = {10.1163/156852008X307447}
  }
  ```
- **niziolek2018javasea** → CORRECTED (completed): → https://api.crossref.org/works/10.1016/j.jasrep.2018.04.002
  ```bibtex
  @article{niziolek2018javasea,
    author = {Niziolek, Lisa C. and Feinman, Gary M. and Kimura, Jun and Respess, Amanda and Zhang, Lu},
    title = {Revisiting the Date of the Java Sea Shipwreck from Indonesia},
    journal = {Journal of Archaeological Science: Reports},
    volume = {19}, year = {2018}, pages = {781--790},
    doi = {10.1016/j.jasrep.2018.04.002}, note = {NEW}
  }
  ```
- **wyart1981lapis** → CORRECTED: pages 184–190 are confirmed. There is a fourth author, Carol Stockton. → https://api.crossref.org/works/10.5741/gems.17.4.184
  ```bibtex
  @article{wyart1981lapis,
    author = {Wyart, Jean and Bariand, Pierre and Filippi, Jean and Stockton, Carol},
    title = {Lapis Lazuli from Sar-e-Sang, Badakhshan, Afghanistan},
    journal = {Gems \& Gemology}, volume = {17}, number = {4}, year = {1981}, pages = {184--190},
    doi = {10.5741/GEMS.17.4.184},
    url = {https://www.gia.edu/doc/Lapis-Lazuli-from-Sar-E-Sang-Badakhshan-Afghanistan.pdf}
  }
  ```
- **pryor1984crusader** → CONFIRMED: the title and the three parts are confirmed. Part I is issue 2, pp. 171–219, DOI 10.1080/00253359.1984.10655967. Part II is issue 3, pp. 275–292, DOI …10655978. Part III is issue 4, pp. 363–386, DOI …10655992. → https://api.crossref.org/works/10.1080/00253359.1984.10655967
  ```bibtex
  @article{pryor1984crusader,
    author = {Pryor, John H.},
    title = {The Naval Architecture of Crusader Transport Ships: A Reconstruction of Some Archetypes for Round-Hulled Sailing Ships},
    journal = {The Mariner's Mirror}, volume = {70}, number = {2--4}, year = {1984},
    pages = {171--219, 275--292, 363--386},
    doi = {10.1080/00253359.1984.10655967},
    note = {Parts I--III; DOIs of Parts II and III: 10.1080/00253359.1984.10655978, 10.1080/00253359.1984.10655992}
  }
  ```
- **liang2020mogao465** → CORRECTED (completed). This is Kogou et al. 2020, and Liang is the fourth author, so the cite key is misleading. → https://api.crossref.org/works/10.1038/s41598-020-76457-9
  ```bibtex
  @article{kogou2020mogao465,
    author = {Kogou, Sotiria and Shahtahmassebi, Golnaz and Lucian, Andrei and Liang, Haida and Shui, Biwen and Zhang, Wenyuan and Su, Bomin and van Schaik, Sam},
    title = {From Remote Sensing and Machine Learning to the History of the Silk Road: Large Scale Material Identification on Wall Paintings},
    journal = {Scientific Reports}, volume = {10}, pages = {19312}, year = {2020},
    doi = {10.1038/s41598-020-76457-9}, note = {NEW}
  }
  ```
  The DOI was checked, but the claim that this paper is specifically about Mogao Cave 465 was not checked against the abstract.

Side finding (Haug, not flagged): the Crossref record for DOI 10.14220/9783737004992 gives the digital edition the date 2015-12-09. The bib entry gives 2016 and the print ISBN. This is probably the imprint year, and was left as is.

## 2. P1 licences

- **Art Institute of Chicago** → CONFIRMED: API data is CC0 1.0, except the `description` field, which is CC BY 4.0. Images marked `is_public_domain` are open access. The website terms page returned 403 to the script, so the licence comes from the API's own `info.license_text`. → https://api.artic.edu/api/v1/artworks/search?q=yuan&limit=1 (with the AIC-User-Agent header); https://www.artic.edu/terms
- **V&A** → CONFIRMED, not CC0: content is free for **non-commercial** use only. The API terms (§9.1) allow "non-commercial personal and educational purposes", and commercial use needs V&A Images. → https://www.vam.ac.uk/info/va-websites-terms-conditions
- **Vatican DigiVatLib** → CONFIRMED as restrictive: the manifest `attribution` reads "Images Copyright Biblioteca Apostolica Vaticana". There is no licence field. Online JPGs are watermarked. Publication needs a paid professional-use licence with the credit "© [anno] Biblioteca Apostolica Vaticana … ogni diritto riservato". → https://digi.vatlib.it/iiif/MSS_Vat.lat.3773/manifest.json ; https://www.vaticanlibrary.va/it/studio-e-consultazione/fotoriproduzione-uso-professionale.html
- **e-codices** → CONFIRMED: non-commercial use is free. The licence is set per library. The csg-0390 manifest declares **CC BY-NC 4.0**. Some libraries release images for unrestricted use, including commercial use. Any other commercial use or republication needs permission. → https://www.e-codices.unifr.ch/en/about/terms ; https://www.e-codices.unifr.ch/metadata/iiif/csg-0390/manifest.json
- **Getty** → CONFIRMED: public-domain images are **CC0** through the Open Content Program, for commercial and non-commercial use. Getty's own texts are CC BY 4.0. → https://www.getty.edu/projects/open-content-program/ ; https://media.getty.edu/iiif/manifest/3/966ac161-01b1-45b9-8dd2-f727ff7b8d50

## 3. P2 archive.org mirrors (https://archive.org/metadata/{id})

None of the items has a `licenseurl` or `rights` field. All are live: not dark, and the PDF and `_text.pdf` are listed. The `imagecount` matches the recorded page counts where present.

- **WhenSilkWasGoldCentralAsianandChineseTextiles** → CONFIRMED live. Uploader kaplan@archive.org, collection `americana`, 2014-02-06, 250 images. No licence field. → https://archive.org/metadata/WhenSilkWasGoldCentralAsianandChineseTextiles
- **byzantium-faith-and-power-1261-1557** → CONFIRMED live. **Community upload** by a private uploader, collections `opensource` and `community`, 2021-04-07. No licence field, so the "may be withdrawn" caveat stands. → https://archive.org/metadata/byzantium-faith-and-power-1261-1557
- **TheTreasuryofSanMarcoVenice** → CONFIRMED live. kaplan@archive.org, `americana`, 355 images. → https://archive.org/metadata/TheTreasuryofSanMarcoVenice
- **FollowingtheStarsImagesoftheZodiacinIslamicArt** → CONFIRMED live. kaplan@archive.org, `americana`, 50 images. → https://archive.org/metadata/FollowingtheStarsImagesoftheZodiacinIslamicArt
- **PersianTiles** → CONFIRMED live. kaplan@archive.org, `americana`, 50 images. No contributor, sponsor or publisher field. → https://archive.org/metadata/PersianTiles
- **SacredVisionsEarlyPaintingsfromCentralTibet** → CONFIRMED live. kaplan@archive.org, `americana`, 241 images. → https://archive.org/metadata/SacredVisionsEarlyPaintingsfromCentralTibet
- **TheFlameandtheLotusIndianandSoutheastAsianArtfromtheKronosCollections** → CONFIRMED live. kaplan@archive.org, `americana`, 193 images. → https://archive.org/metadata/TheFlameandtheLotusIndianandSoutheastAsianArtfromtheKronosCollections
- **mathers_flecker_1997_java_sea_wreck** (not a Met catalogue) → CONFIRMED live. Community upload by a private uploader, 2020-10-28, 204 images. No licence field. → https://archive.org/metadata/mathers_flecker_1997_java_sea_wreck

Conclusion: the six Met items were uploaded by an Internet Archive staff account (kaplan@archive.org) into `americana`, all on one day in 2014. That fits a bulk mirror of the Met's free MetPublications PDFs, but the metadata does not state the source. The licence remains undocumented.

## 4. P4 "where free" claims

- **Ghiasian on H.1654 (G1)** → CORRECTED: the year is **2018**, not 2022. *Iranian Studies* 51(3): 399–425, DOI 10.1080/00210862.2018.1428085. The article is paywalled ("Get access"), so it is **not free**. → https://www.cambridge.org/core/product/D298994042B2643F0E25DAA747EA7E09 ; https://api.crossref.org/works/10.1080/00210862.2018.1428085
- **Sasaki thesis 2009, TDL (G2)** → STILL UNCONFIRMED as free. The record is live (date issued 2009-05-15), but the anonymous DSpace API shows no file bundles, and the page carries "embargo" and "restricted" strings. The PDF may not be publicly downloadable. → https://tdl-ir.tdl.org/server/api/core/items/f0dc70cd-066a-4a91-9cf7-ea93670394dd/bundles
- **Sasaki book 2015, MUSE (G2)** → CONFIRMED not free: MUSE shows "Open Access: No". → https://muse.jhu.edu/book/38210
- **Haug 2016 on the V&R eLibrary (G4)** → BLOCKED: the eLibrary returned 403. The Crossref record has no licence. → https://doi.org/10.14220/9783737004992
- **Kieven 2013 (G5)** → CONFIRMED open access: on OAPEN under CC BY-NC-ND 3.0 (DOI 10.26530/oapen_613436). Brill edition: 10.1163/9789004258655. → https://api.crossref.org/works/10.26530/oapen_613436
- **CKC 2023 advice (G5)** → CONFIRMED free: the PDF is live (application/pdf, about 600 KB). Its first page reads "Advies … Vier beelden uit het tempelcomplex van Singasari". → https://zoek.officielebekendmakingen.nl/blg-1100343.pdf
- **Naumann 1976 (G6)** → CONFIRMED free: there is a full-text download (22.9 MB) on Stony Brook Academic Commons. → https://commons.library.stonybrook.edu/amar/303/
- **The other P4 items marked "not free" or "from memory"** (Rubruck/Jackson, Andrews, Blair, Conlan, Steinhardt, McCausland and others) → not checked. P4 gives no URL for them.
