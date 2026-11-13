# Verification pass: G4–G6 (2026-11-13)

Format: claim as in report → status → evidence.
Fetched with plain HTTP; for blocked sites the status is BLOCKED, never inferred.

## G6

- Morgan M.500 viewer at ica.themorgan.org/manuscript/thumbs/77363 → CONFIRMED (HTTP 200; 97 folio thumbnails, fol. 2r–84v, page views at /manuscript/page/N/77363) → https://ica.themorgan.org/manuscript/thumbs/77363
- Morgan record themorgan.org/manuscript/77363 → BLOCKED (403 to script) → https://www.themorgan.org/manuscript/77363
- M.500 "no IIIF found" → CONFIRMED (no IIIF/manifest link in the viewer HTML) → https://ica.themorgan.org/manuscript/thumbs/77363
- M.500 date line "and 19th cent." → CONFIRMED and explained. The viewer heading reads "Iran, 1297-1298 or 1299-1300, and 19th century". The catalogue text: a 19th- or early-20th-c. restoration repainted heavily and ADDED miniatures on fols. 3v, 6v, 23v, 25v, 36r, 47v, 58v, 72v, 78r, 78v, 84r. Exclude those folios from plates → https://ica.themorgan.org/manuscript/thumbs/77363 ; https://bestiary.ca/manuscripts/manu2739.htm
- M.500 colophon on fol. 84v; Maragha; 1297–98 or 1299–1300; 103 miniatures → CONFIRMED (bestiary.ca quotes the catalogue text: "Dated in the colophon on fol. 84v", "103 miniatures"; commissioned by Ghazan) → https://bestiary.ca/manuscripts/manu2739.htm
- M.500 "camels, horses … (folios from memory)" → STILL UNCONFIRMED (specific folios were not checked)
- BSB Cod.arab. 464 date field "678 oder 778" → CONFIRMED. IIIF metadata Date = "678 oder 778 [h.q.] [1279-1377]", Published = "Wāsiṭ". The BSB description in the same manifest says "completed in 1280, three years before the author's death" and "more than 400 miniatures". The record's two fields disagree; the description supports 1280 → https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00037026/manifest
- BSB manifest has 428 canvases, HTTP 200 → CONFIRMED (same URL)
- Qalamos record → BLOCKED (connection failed) → https://qalamos.net/receive/DE12Book_manuscript_00003827
- BnF Suppl. persan 205, archives ark cc33978s "(403)" → CORRECTED: now returns HTTP 200, full notice. Copy finished 4 Dhu l-Hijja 689 H = 8 Dec 1290 (f. 176v), copyist Rašīd al-Ḫwāfī. Double painted page on ff. 1v–2, contemporary with the copy and "perhaps Baghdad": 1v shows a groom holding a prince's horse; 2 shows a Mongol prince "[Abaqā ?]" standing beside Juvaynī, identified by inscription. Faces are damaged. Folio 1 has a šamsa. The notice cites Ettinghausen 1959 and Simpson 1982 → https://archivesetmanuscrits.bnf.fr/ark:/12148/cc33978s
- Suppl. persan 205 Gallica ark "unknown" → CORRECTED: ark:/12148/btv1b84149955, linked from the BnF notice ("Consulter le document numérisé"). Gallica itself still returns 403 to scripts → https://gallica.bnf.fr/ark:/12148/btv1b84149955
- Suppl. persan 205 "sitter's identification is disputed (from memory)" → CONFIRMED in substance. The BnF's own notice marks the prince as "[Abaqā ?]" → as above
- Naumann 1976 AMAR free PDF → CONFIRMED. Full title "Takht-i Suleiman: Ausgrabung d. Dt. Archäolog. Inst. in Iran: Ausstellung München 1976: Einf. u. Katalog", 71 + 12 pp.; direct PDF 22.9 MB → https://commons.library.stonybrook.edu/cgi/viewcontent.cgi?article=1302&context=amar
- SMB Takht-i Sulayman project 2023–25, about 1,200 tile fragments → CONFIRMED. Runs Dec 2023 to Dec 2025 and covers almost 5,000 objects, 1,200 of them tile fragments, from the 1959–78 DAI excavations → https://www.smb.museum/en/museums-institutions/museum-fuer-islamische-kunst/collection-research/research-cooperation/summer-palace-takht-e-soleyman/
- Takht tiles "1270s inscriptions (from memory)" → STILL UNCONFIRMED

## G5

- Wereldmuseum records RV-1403-1622/-1623/-1624/-1680/-1681/-1682 → STILL UNCONFIRMED. collectie.wereldculturen.nl redirects to collectie.wereldmuseum.nl, a JavaScript-only app, and no record text came back → https://collectie.wereldmuseum.nl/?query=search=RV-1403-1622
- "Probably repatriated in 2024 (not confirmed)" → CORRECTED (single source): the Historia repatriation page for Mahakala says the objects were returned on 18 August 2023 and are now in the Museum Nasional, Jakarta. Not cross-checked against a Dutch government source → https://repatriasi2024.historia.id/en/mahakala
- Leiden Digital Collections, "Tjandi Djago" / "Singasari" → BLOCKED (connection reset, curl exit 56) → https://digitalcollections.universiteitleiden.nl/search/Tjandi%20Djago
- Tripati 2006, IJNA 35(1): 88–96 → CONFIRMED. "Ships on Hero Stones from the West Coast of India", doi 10.1111/j.1095-9270.2005.00081.x → https://doi.org/10.1111/j.1095-9270.2005.00081.x
- Niziolek et al. 2018 (AMS dates, mid-to-late 12th c.) → CONFIRMED citation: Niziolek, Feinman, Kimura, Respess, Zhang, "Revisiting the date of the Java Sea Shipwreck from Indonesia", J. Archaeol. Sci.: Reports 19 (2018): 781–790, doi 10.1016/j.jasrep.2018.04.002 (dating content not re-read) → https://doi.org/10.1016/j.jasrep.2018.04.002
- Niziolek 2015 JIPA → CONFIRMED: JIPA 35, doi 10.7152/jipa.v35i0.14893 → https://doi.org/10.7152/jipa.v35i0.14893
- Lambourn 2008 disputing Moquette's Cambay thesis → CORRECTED to a full citation: Lambourn, "Tombstones, Texts, and Typologies: Seeing Sources for the Early History of Islam in Southeast Asia", JESHO 51(2) (2008): 252–286, doi 10.1163/156852008x307447. That the paper argues against Moquette on the al-Malik al-Salih stone is not verified (abstract not read). Related papers: Lambourn 2003, Indonesia and the Malay World 31(90): 221–284, doi 10.1080/1363981032000165903 (Cambay → Pasai export, 15th c.), and Lambourn 2004, IMW 32(93): 211–248, doi 10.1080/1363981042000320143 → https://doi.org/10.1163/156852008x307447
- Pasai epitaph AH 696 → STILL UNCONFIRMED

## G4

- BnF lat. 10136: "No Gallica ARK found" → STILL UNCONFIRMED. Gallica SRU returns 403, and an Archives et manuscrits search for "Latin 10136" gave "Aucun résultat" → https://archivesetmanuscrits.bnf.fr/
- lat. 10136: 116 images; drawings from the mid-12th c.; Kat. Nr. 1 = fol. 1r → CONFIRMED (Haug 2016 front matter, "insgesamt 116 unterschiedliche Bilder"; Abb. 1 = fol. 1r) → https://content.e-bookshelf.de/media/reading/L-4237396-47cf0890f7.pdf
- lat. 10136 "ship drawings not confirmed" → STILL UNCONFIRMED (no ship or fleet drawing named in the opened front matter; the catalogue section is not in the excerpt) → same PDF
- "A phototype facsimile was printed in 1890" → CORRECTED: Haug dates the facsimile "Cafari (1899)". 1890 is Belgrano's *Annali Genovesi* edition → same PDF, n. 5
- Carte Pisane ark btv1b52503226n → CONFIRMED (linked from BnF catalogue notice cb406673515). Gallica returns 403 to scripts. The notice dates it "[Gênes?], [ca 1270]", 48 x 103 cm, and records "Aucune décoration" apart from a red cross → https://catalogue.bnf.fr/ark:/12148/cb406673515
- Carte Pisane: is Laiazzo/Layas named? → STILL UNCONFIRMED. The notice lists no place-names (no Lajazzo, Laiazzo, Aiazzo, Layas or Ayas) and the image could not be fetched
- Humphrey mariegole book "year from memory"; "cini.it is blocked" → CORRECTED: cini.it now returns 200. The book is *La miniatura per le confraternite e le arti veneziane. Mariegole dal 1260 al 1460*, ed. Lyle Humphrey, Cierre Edizioni, December 2015 (Istituto di Storia dell'Arte) → https://www.cini.it/en/?p=51517
- Cocharelli BL Add MS 27695: "BL viewer possibly degraded; BL IIIF blocked" → CORRECTED: the BL record now gives Digitised Content, a Universal Viewer link with manifest https://bl.digirati.io/iiif/ark:/81055/vdc_100165147237.0x000001. Date range c. 1330–1340; 15 leaves of 27 surviving. The manifest itself was not fetched → https://searcharchives.bl.uk/catalog/040-002031109
- CHARLVAR site 76, Edwards photographs 1974–81 → CONFIRMED. Albums include "Ay" site plans and "Ay I" 29 colour transparencies (1974), by Robert W. Edwards. No licence statement appeared in the page HTML, so the licence is STILL UNCONFIRMED → https://charlvarchive.org/Site/76
- Eser article on hrcak 95082 "(title, author and journal not confirmed)" → CORRECTED: Erdal Eser, "From the Roman Settlement of Aigai to Ayas", Vjesnik Arheološkog muzeja u Zagrebu (VAMZ), 3rd ser., XLII (2009): 421–441. It includes Sea Castle excavation areas A and B → https://hrcak.srce.hr/file/95082
