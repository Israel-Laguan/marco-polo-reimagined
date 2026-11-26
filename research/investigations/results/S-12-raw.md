Tool: Claude Code (Opus 5.5, `claude-opus-5-5`) with web search, Open Library (search + ISBN API), CrossRef, NDL Search and publisher pages · run 2026-11-10 · prompt: `spikes/S-12-bibliography-editions.md` § Deep research prompt

Scope note (written with the run, not added later). Most of Task A was answered on 2026-10-22 by the CIT runs (`CIT-A-raw.md` … `CIT-C-raw.md`), and their entries are already in `registry/bibliography.bib` with status comments. This run therefore researched only what the CIT runs did not cover: Task A gaps (Bushell, Gaubil, de Mailla, Needham by volume, Aldo Ricci), all of Task B, the Task C sources that have no entry, Task D, and the six names in `registry/name-keys.csv` marked `needs-edition`. For every row the "sources" column names the record that was actually opened. Gallica (gallica.bnf.fr) refused automated requests (Cloudflare block), so no Gallica record was opened directly.

## (1) Findings

### Task A — names → works (gaps only)

| # | Claim or topic | Finding | Verdict | Sources | Confidence | Sections |
|---|---|---|---|---|---|---|
| A1 | Bushell on Shangdu | S. W. Bushell, "Notes of Journey outside the Great Wall of China", *Journal of the Royal Geographical Society of London* 44 (1874), first page 73. A shorter version, "Notes of a Journey outside the Great Wall of China", is in *Proceedings of the RGS* 18 (1873), first page 149. The visit the Notes describe was made in 1872. | confirmed (end page not in the record) | CrossRef DOI 10.2307/1798779 (JRGS); CrossRef DOI 10.2307/1799971 (PRGS) | high | I-13, II-04, III-12 |
| A2 | Gaubil | Antoine Gaubil, *Histoire de Gentchiscan et de toute la dinastie des Mongous ses successeurs, conquérans de la Chine* (Paris: Briasson et Piget, 1739). | confirmed | Open Library OL17919939W, OL44714944W | high | I-12, I-13, II-01 … II-05 |
| A3 | de Mailla | Joseph-Anne-Marie de Moyriac de Mailla, *Histoire générale de la Chine* (Paris: Pierres, Clousier, 1777–1785), multi-volume. Volume count not seen. | confirmed (title, publisher, first year) | Open Library OL10306695W, OL10306697W | high | II-02, II-03, II-05, II-10, II-11, III-01 |
| A4 | Needham: ships (junk bulkheads) | *Science and Civilisation in China*, vol. 4, pt. 3, *Civil Engineering and Nautics*, by Joseph Needham with Wang Ling and Lu Gwei-Djen (Cambridge University Press, 1971). | confirmed | Wellcome Collection catalogue record (via search) | high | III-01, III-12 |
| A5 | Needham: paper money | vol. 5, pt. 1, *Paper and Printing*, by Tsien Tsuen-hsuin (Cambridge University Press, 1985), ISBN 0521086906. | confirmed | Open Library OL6032232W | high | II-05, III-12 |
| A6 | Needham: coal | vol. 5, pt. 13, *Mining*, by Peter J. Golas (Cambridge University Press), ISBN 0521580005. Open Library dates it January 2000; a library catalogue gives c1999 for the volume. | disputed (year) | Open Library OL8324873W; TAMU catalogue (search result) | medium | II-05, III-12 |
| A7 | Needham: astronomy | vol. 3, *Mathematics and the Sciences of the Heavens and the Earth* (Cambridge University Press, 1959). Not cited by the Notes today, so no entry was added. | confirmed | Open Library OL32928383W | high | — |
| A8 | Benedetto in English | *The Travels of Marco Polo*, translated from Benedetto's text by Aldo Ricci, introduction and index by E. Denison Ross (New York: Viking Press, 1931). A London issue (Routledge, Broadway Travellers) is commonly cited; it was not seen. | confirmed (Viking issue) | Open Library OL42483586W | high | III-11, III-12 |
| A9 | Timothy May | None of the "May" hits in `vol-*/` is the scholar: all 23 are the month. No entry is needed for the Notes. (`may2011baybars` already exists from ENR-A.) | not found (no citation) | grep of `vol-*/*.md`, 2026-11-10 | high | — |
| A10 | Cleaves (Yongle dadian, envoys of Arghun) | Already in the bibliography: `cleaves1976chinese` (*HJAS* 36, 1976), confirmed through its DOI at the S-05 intake. No name in `vol-*/` cites it yet; `registry/facts.md` F-15 uses it. | confirmed (earlier) | CrossRef DOI 10.2307/2718743 | high | III-09, III-11, III-12, III-B1 |
| A11 | Every other Task A name | Answered by CIT-A … CIT-C (Yule, Cordier, Ramusio, Benedetto, Moule–Pelliot, Pelliot, Olschki, Larner, Critchley, Wood, de Rachewiltz, Haw, Vogel, Rossabi, Allsen, Morgan, Jackson, Dutschke, Franke, Steinhardt, Baber, de Groot, Pauthier, Moule). Not re-researched here. | see CIT raws | `CIT-A-raw.md` … `CIT-C-raw.md` | — | general |

### Task B — modern editions and translations of Polo's book

| # | Claim or topic | Finding | Verdict | Sources | Confidence | Sections |
|---|---|---|---|---|---|---|
| B1 | Ménard's French edition (Fr) | *Le Devisement du monde*, critical edition under the direction of Philippe Ménard, 6 vols. (Genève: Droz, 2001–2009; Textes littéraires français). Vol. 1 2001 (TLF 533), 2 2003, 3 2004, 4 2005, 5 2006 (TLF 586; Delclos and Roussel), 6 2009 (Boutet, Delcourt, James-Raoul). Edits the "Fr" (Old French) redaction. Not open access. | confirmed | Retailer and library listings (laprocure.com vol. 4; bibliotheques.paris.fr); Burgio's review of Ménard (iris.unive.it PDF); Ménard's own bibliography (info.hazu.hr PDF) | high | III-11, III-12 |
| B2 | Eusebi's edition of F (fr. 1116) | First as *Il manoscritto della Bibliothèque nationale de France fr. 1116. I. Testo* (Roma–Padova: Antenore, 2010; series "Poliana"). Reworked and reissued open access: *Marco Polo. Le Devisement dou monde*, vol. 1 text ed. Mario Eusebi, vol. 2 ed. Eugenio Burgio (language introduction, glossary, index of names) (Venezia: Edizioni Ca' Foscari, 2018; Filologie medievali e moderne 16), DOI 10.30687/978-88-6969-223-9, CC BY 4.0. **NEW** (2018). | confirmed (2018); 2010 seen only in citations | Edizioni Ca' Foscari book page (opened); Antenore series front matter (arca.unive.it) | high | III-11, III-12, I-01 |
| B3 | Digital Ramusio | *Giovanni Battista Ramusio, "Dei viaggi di Messer Marco Polo": edizione critica digitale*, ed. Eugenio Burgio and Samuela Simion, project coordinated by Burgio, Marina Buzzoni and Antonella Ghersetti (Venezia: Edizioni Ca' Foscari, 2015; Filologie medievali e moderne 5), DOI 10.14277/978-88-6969-00-06, CC BY 4.0. Edits R (Ramusio 1559) with commentary and the other versions alongside. **NEW** (2015). | confirmed | Edizioni Ca' Foscari book page (opened); Simion, *ZrP* 2017 (iris.unive.it) | high | III-10, III-11, III-12 and every Ramusio-only Note |
| B4 | Bertolucci Pizzorusso's Tuscan text (TA) | *Milione: Versione toscana del Trecento*, ed. Valeria Bertolucci Pizzorusso, indice ragionato by Giorgio R. Cardona (Milano: Adelphi, 1975); reprinted 1994. Not open access. | confirmed | Bookseller listing (dimanoinmano.it); Open Library OL20654275M (1994 printing); university course bibliography (Loescher PDF) | high | III-11 |
| B5 | Ronchi's F + TA reading edition | *Milione. Le divisament dou monde: Il Milione nelle redazioni toscana e franco-italiana*, ed. Gabriella Ronchi, introduction by Cesare Segre (Milano: Mondadori, 1982; I Meridiani). Not in the prompt; added. | confirmed | Open Library OL575892W | high | III-11 |
| B6 | Z (Latin, Toledo Zelada 49.20) | *Milione: Redazione latina del manoscritto Z; versione italiana a fronte*, ed. Alvaro Barbieri (Fondazione Pietro Bembo / Guanda, 1998), ISBN 978-88-8246-064-8. Still the reference edition of Z (Ca' Foscari 2024 study). Not in the prompt; added. | confirmed | Open Library ISBN record; Edizioni Ca' Foscari, *Milione Z. Fenomenologia…* (search result) | high | III-11, III-12 |
| B7 | VA (Venetian) | *Il «Milione» veneto: ms. CM 211 della Biblioteca Civica di Padova*, ed. Alvaro Barbieri and Alvise Andreose (Venezia: Marsilio, 1999; Medioevo veneto). Not in the prompt; added. | confirmed (through a review, no catalogue record opened) | Burgio's review, *Quaderni veneti* 33 (2001) (iris.unive.it PDF) | medium | III-11 |
| B8 | "Simion and Burgio's work" | The prompt's item is the digital Ramusio (B3): Simion is its co-editor. Their other joint output found is a conference paper (CILPR 2013) on the VB redaction. No separate edition. | corrected | Ca' Foscari page (B3); CILPR 2013 actes (atilf.fr) | medium | — |
| B9 | Kinoshita | *The Description of the World*, trans. Sharon Kinoshita (Indianapolis: Hackett, 2016), ISBN 978-1-62466-436-6 (pbk), 978-1-62466-437-3 (hbk). Translates F (Franco-Italian). **NEW**. | confirmed | Open Library ISBN record (Hackett, 1 Mar 2016) | high | III-11, III-12 |
| B10 | Latham | *The Travels of Marco Polo*, trans. Ronald Latham (Harmondsworth: Penguin, 1958). Seen as a 1982 printing, ISBN 0140440577. Base text not checked. | confirmed | Open Library ISBN record (1982 printing) | high | III-11 |
| B11 | Cliff | *The Travels*, trans. Nigel Cliff (London: Penguin Classics, 2015), ISBN 978-0-14-119877-4. Publisher calls it the first new English translation in over fifty years. **NEW**. | confirmed | Open Library ISBN record (29 Dec 2015) | high | III-11 |
| B12 | Digitised manuscripts | BnF fr. 2810 (*Livre des merveilles*, c. 1410–12): Gallica ark:/12148/btv1b10021503v per the Wikimedia Commons file already used in `registry/pd-sources.md`; one thesis gives ark:/12148/btv1b52000858n instead. BnF fr. 1116 (F): Gallica ark **not found**. | disputed (2810) / not found (1116) | `registry/pd-sources.md` (Commons); unitesi.unive.it thesis | low | III-11, plates |
| B13 | Bibliographies | The Fondazione Università Ca' Foscari "Bibliografia Marco Polo 2024" PDF appeared in search but returned 404 when opened. | not found | — | — | III-11 |

### Task C — standard translations of the comparative sources

| # | Claim or topic | Finding | Verdict | Sources | Confidence | Sections |
|---|---|---|---|---|---|---|
| C1 | Rubruck | Already in: `jackson1990mission` (Jackson and Morgan, Hakluyt 1990). | confirmed (earlier) | CIT intake | high | I-05, I-12, I-13 … |
| C2 | Carpini (English) | Christopher Dawson, ed., *The Mongol Mission* (London and New York: Sheed and Ward, 1955): Carpini and Rubruck in English. | confirmed | Open Library OL1457505W | high | I-12, I-F1, II-01, II-03 |
| C3 | Carpini (critical Latin) | Giovanni di Pian di Carpine, *Storia dei Mongoli*, ed. P. Daffinà, C. Leonardi, M. C. Lungarotti, E. Menestò and L. Petech (Spoleto: Centro italiano di studi sull'alto medioevo, 1989), viii + 522 pp. Called the best edition of the longer redaction (*Acta Via Serica* 2023). | confirmed (through a review record) | *JRAS* review record (cambridge.org); koreascience.kr article | medium | same |
| C4 | Odoric | Critical Latin: Odorico da Pordenone, *Relatio de mirabilibus orientalium Tatarorum*, ed. Annalia Marchisio (Firenze: SISMEL – Edizioni del Galluzzo, 2016), ISBN 978-88-8450-699-3. **NEW**. English: Yule's in *Cathay* (`yule1913cathay`, already in). | confirmed | Open Library OL32742554W | high | I-06 … III-05 |
| C5 | Ibn Battuta | Already in: `gibb1958travels` (Gibb and Beckingham, Hakluyt, 1958–1994). | confirmed (earlier) | CIT intake | high | — |
| C6 | Rashid al-Din | Already in: `thackston1998rashiduddin`; `boyle1971successors`. | confirmed (earlier) | CIT intake | high | — |
| C7 | Juvaini | Already in: `boyle1958history`. | confirmed (earlier) | CIT intake | high | III-12 |
| C8 | Wassaf | No complete English translation found. Yule used Hammer-Purgstall: *Geschichte Wassaf's*, vol. 1, Persian text and German translation (Wien: Hof- und Staatsdruckerei, 1856). Continued by the Austrian Academy (vols. from 2010). | confirmed | Open Library OL16542466W, OL20222647M | high | III-05, III-06, III-09 |
| C9 | Secret History | Already in: `derachewiltz2004secret`. | confirmed (earlier) | CIT intake | high | — |
| C10 | *Yuan shi* | Already in: `yuanshi1370` (Zhonghua shuju 1976 addendum). No translation of the Polo-relevant sections was found beyond Cleaves 1976 (A10). | confirmed (earlier) | CIT intake | medium | — |

### Orphan names in `name-keys.csv` (`needs-edition`)

| # | Name | Finding | Verdict | Sources | Confidence | Sections |
|---|---|---|---|---|---|---|
| O1 | Schottenhammer (Quanzhou port history) | Angela Schottenhammer, ed., *The Emporium of the World: Maritime Quanzhou, 1000–1400* (Leiden: Brill, 2001), ISBN 90-04-11773-3. | confirmed | Open Library OL19045716W | high | II-14, III-12 |
| O2 | Chen Dasheng (Quanzhou archaeology) | Quanzhou Maritime Museum, comp., chief author Chen Dasheng, English trans. Chen Enming, 泉州伊斯兰教石刻 *Islamic Inscriptions in Quanzhou* (Fuzhou: Fujian renmin chubanshe, with Ningxia renmin chubanshe, 1984). Chinese, English, Arabic and Persian. | confirmed | NDL Search record R100000002-I025579520 (opened) | high | II-14, III-12 |
| O3 | Hsiao Ch'i-ch'ing (Yuan military) | *The Military Establishment of the Yuan Dynasty* (Cambridge, MA: Council on East Asian Studies, Harvard University, 1978), ISBN 0674574613. | confirmed | Open Library OL6799256W | high | II-01 |
| O4 | Huntingford (Abyssinia, III-07) | Two candidates: *The Glorious Victories of ʿĀmda Ṣeyon, King of Ethiopia* (Oxford: Clarendon, 1965) and *The Periplus of the Erythraean Sea* (London: Hakluyt Society, 1980). The Note cites him beside "Abyssinian chronologies", which fits the 1965 book better, but the Note does not say. | not resolved | Open Library OL4388089W, OL18339912W | medium | III-07 |
| O5 | Elverskog ("on Mongol ritual") | No work matches the Note's context with confidence. | not found | — | low | II-03 |
| O6 | Subrahmanyam (St Thomas, Mylapore) | No work matches the Note's context with confidence. | not found | — | low | III-05 |

## (2) Disagreements

- **Golas, *Mining*:** Open Library dates it January 2000; a library catalogue gives c1999. The title page was not seen.
- **fr. 2810 on Gallica:** the Commons file name (which copies BnF's own identifier) gives btv1b10021503v; a Venice thesis gives btv1b52000858n. Both may be real (a colour scan and an older one). Neither was opened on Gallica.
- **Chen Dasheng 1984, publisher:** citations give either Fujian or Ningxia People's Press. The NDL record gives Fujian as publisher, with Ningxia as a co-publisher.

## (3) Task D — core works for a general-reader edition (the tool's ranking; a proposal, not a decision)

1. Yule–Cordier 1903/1920 (`yc`, `ycadd`): the base text and still the largest commentary in English.
2. Moule and Pelliot 1938 (`moule1938description`): the collated text, Z included; the scholarly English standard.
3. Pelliot, *Notes on Marco Polo* (`pelliot1959notes`): names and places, item by item.
4. Kinoshita 2016 (`kinoshita2016description`): the current English translation of F.
5. Eusebi–Burgio 2018 (`eusebi2018devisement`): the critical F text, open access.
6. Burgio–Simion 2015 (`ramusio2015viaggi`): the critical Ramusio, open access; needed for every Ramusio-only passage.
7. Ménard 2001–2009 (`menard2001devisement`): the French redaction, fully annotated.
8. Larner 1999 (`larner1999marco`): the book in its European context and reception.
9. Haw 2006 (`haw2006marco`): Polo's China checked against Chinese sources.
10. Vogel 2013 (`vogel2013marco`): currencies, salt and revenues; the strongest single case for presence.
11. Wood 1995 (`wood1995did`) with de Rachewiltz 1997 (`derachewiltz1997marco`): the sceptical case and its main reply, read together.
12. Rossabi 1988 (`rossabi1988khubilai`): Khubilai and his court.
13. Jackson 2005 (`jackson2005mongols`): the Mongols and Latin Europe.
14. Olschki 1960 (`olschki1960marco`): Polo's Asia as a medieval reader understood it.
15. Critchley 1992 (`critchley1992marco`): how the book was made and transmitted.

## (4) Bibliography of sources used (status = what was opened)

All BibTeX for these works is in `registry/bibliography.bib` § "S-12 intake (2026-11-10)", each with its status comment. Open access: B2 (CC BY 4.0), B3 (CC BY 4.0). All others are in copyright and not open access, except A1–A3 and C8 (public domain; scans exist, not linked here because none was opened).

Lookup sources: CrossRef API (A1, A10); Open Library search and ISBN API (A2, A3, A5–A8, B4–B6, B9–B11, C2, C4, C8, O1, O3, O4); NDL Search (O2); Edizioni Ca' Foscari book pages (B2, B3); search-result summaries only (A4, B1, B7, C3, B12).

## (5) Not resolved

1. BnF fr. 1116 Gallica identifier; fr. 2810's two identifiers (Gallica blocks automated access).
2. Golas, *Mining*: 1999 or 2000.
3. de Mailla, *Histoire générale*: number of volumes (13 is the usual count; not seen).
4. Bushell 1874: end page (CrossRef gives only the first page, 73).
5. Huntingford, Elverskog, Subrahmanyam: which work each Note means.
6. Eusebi 2010 (Antenore): no catalogue record opened.
7. Marchisio as editor of the 2016 Odoric: matched by an Open Library search on her name; title page not seen.
8. Ricci 1931: the London (Routledge) issue was not seen.
