# S-22 follow-up — intake (2026-11-13), read for S-23

Raw file: [S-22-followup-raw](S-22-followup-raw.md). It answers the [S-22 follow-up prompt](../S-22-follow-up-prompt.md) (period objects by group). The user supplied it as the base for [S-23](../../../editorial/plans/spikes/S-23-media-scouting.md). **It contains no modern work**, so it does not answer S-23's question; it is checked here because the registry and `illustration-plan.md` had already taken it in as "verified" and "resolved".

Checks were run in this repo with one web search or one page fetch each, against the holding institution where it could be reached. No image was viewed.

## Sixteen record checks

Chosen on purpose: every row that gives an accession number or shelfmark and that a registry cue or a "resolved" mark rests on.

| # | Raw-file claim | What the record says | Result |
|---|---|---|---|
| 1 | Cleveland 1989.50, cloth of gold, Yuan, licence CC BY-NC-ND | Museum page: *Cloth of gold with winged lions and griffins*, 1225–75, Central Asia, **public domain (open access)** | Supported; licence and date label wrong in the raw file |
| 2 | Freer F1954.21, *Tilling Rice, after Lou Shou*, attr. Cheng Qi | Freer record: as stated; traditional attribution, mid- to late 13th c., 21 scenes | Supported |
| 3 | Freer F1954.21, "*Silk Weaving, after Lou Shou*" | The sericulture scroll is **F1954.20**; F1954.21 is the rice scroll | Wrong number |
| 4 | Morgan M.500, *Manāfiʿ al-ḥayawān*, "c. 1290", inside the period | Morgan: Maragha, **1297–98 or 1299–1300**; heavy 19th-century overpainting and added miniatures | Exists; date wrong; **later**, and each miniature needs a period-or-repaint check |
| 5 | BnF Suppl. persan 205, 1290, "commissioned by Arghun" | Iranica: dated 689/1290, probably Baghdad; frontispiece with Chinese cloud and peony motifs. No source found for the patron | Exists and dated; patron claim unsupported. The Gallica link given is the same one the raw file gives for Arabe 5847, so at least one is wrong (Gallica returned 403; not resolved) |
| 6 | Sinan wreck (1323), "Jeju National Museum" | Hull and cargo are at the National Research Institute of Maritime Cultural Heritage (National Maritime Museum), **Mokpo** | Exists; holder wrong |
| 7 | Acre marble hoard, "Polonnaruwa Archaeological Museum, Sri Lanka" | Israel Antiquities Authority excavation, about 350 pieces; published in *Marmora* 6 (2010), 151–61 | Exists; holder wrong (a row-merge error) |
| 8 | Huang Sheng tomb, "men's and women's clothing", "inside" the period | Fujian Museum: the tomb of one woman, Huang Sheng, **d. 1243**, found 1975; 354 silk textiles | Exists; **earlier** by 20–50 years; women's dress only |
| 9 | BL "Additional MS 36129, fol. 23v", treatise on vices, "late 13th c." | The Genoese treatise on the vices is the Cocharelli codex, **BL Add MS 27695** (and 28841), **c. 1330–40** | Wrong shelfmark and date; 40 years late |
| 10 | "BnF Ms. Or. 20 f. 120r", Rashīd al-Dīn, "c. 13th century" | Or.MS 20 is **Edinburgh** University Library, 1314. Already in the registry | Wrong holder and date |
| 11 | Royal Armouries XXVIC.82, Yuan mace | No record found; the XXVIC series surfaced only for Indian maces | Not found |
| 12 | Princeton 1977.58, clay tent model | Princeton's record for the green-glazed *Mongolian tent*, Yuan, 14th c., is **y1951-34** | Object exists; number wrong |
| 13 | Met 1978.412.56, given both as a "Mongol war mask" and as a "ceramic tent model" | Not found. The 1978.412 series is the Rockefeller collection (Africa, Oceania, Americas). The Met page returned 429 | Not found; one number for two objects |
| 14 | Walters 54.2766, Sukhothai Buddha head | No record found | Not found |
| 15 | Ashmolean TM1915.15, "Tangut-style bowl with rider" | No record found under that number | Not found |
| 16 | Juyong Pass, 1345: "relief carving of a tent" and "of a portable palace" contrasting Dadu and Shangdu | The Cloud Platform reliefs are Buddhist: the Four Heavenly Kings, mandalas and six-script texts | Not supported. Reads like a paraphrase of an article's argument, not a description of a relief |

Also looked at, not scored: the "Wen-chi" scrolls exist (Met 1973.120.3 is an early-15th-century copy; four leaves in Boston are taken as 12th-century), but no record read says they show a tent **on a cart**.

**Hit rate: 2 of 16 supported as stated (13%). In 8 of 16 the object exists but the holder, number, date or description is wrong; 6 were not found or not supported.** This is far below the 80% line in the research README. The file is not salvaged row by row; the prompt is re-run with stricter terms (follow-up H2 in the spike).

## Failures against the prompt's own contract

- **0 of 67 rows were viewed.** Every row says "record read, image not viewed", including rows whose record URL is "Not Available", sites that have no record, and Rubruck's text.
- The coverage ledger marks all 11 groups "Answered", including the pearl fishery, which its own table calls a knowledge gap, and the two catalogue questions (Yuan dress reconstructions; the Suntory exhibition), which get one sentence each and no catalogue record.
- No "Leads" section, no bibliography or BibTeX, no unresolved questions.
- The citations are mostly Wikipedia, blogs, Baidu and a Facebook group. Several do not match their claim: the Wikipedia page on Zhao Feng is cited for Armenian illumination, the Huang Sheng tomb, Dunhuang and the pearl fishery; a professor's CV is cited for the Suntory exhibition.
- Date discipline: 13 rows are filed "inside" on a dynasty-wide date (1271–1368) or on a wrong date.
- Internal slips: "Houzhou" for Houzhu; "unexcavated object" for excavated ones; the Dunhuang donor row describes the NPM consort album; the "Quadriga mosaic" is a garbled Porta Sant'Alipio mosaic; the Pala d'Oro is dated "c. 10th century".

## Corrections to what was already taken in

The registry's supplement and `illustration-plan.md` were written from this file before it was checked.

- The registry counted "81 sources"; the raw file has 67 rows, several of them duplicates.
- "RESOLVED ✅" for Dadu, Shangdu, South China streets, Venetian galleys, the ger-cart, the sewn hull, Java and Sumatra, and the Pandya coast: **none is resolved.** No object in those groups has both a confirmed record and a viewed image.
- Draft cues C9–C22 are not cues. They are worded from the raw file's descriptions of unviewed objects; C12 describes reliefs that do not exist; C14 contradicts what was seen on 2026-11-13 (no stitching visible on Arabe 5847 f248); C11, C19 and C20 state facts about an object instead of describing what a painter should draw.

## What can be kept (as leads, each still to be viewed)

| Lead | Record to open | For |
|---|---|---|
| Green-glazed tent model | Princeton y1951-34 | I-12, I-13 ger form (not the cart) |
| *Tilling Rice* and *Sericulture* | Freer F1954.21, F1954.20 (open access) | II-10, II-12 rural dress, boats, tools |
| Huang Sheng garments, 1243 | Fujian Museum; the excavation report | II-10, II-13 women's dress, a generation early |
| *Tārīkh-i jahāngushāy* frontispiece, 1290 | BnF Suppl. persan 205 on Gallica | I-5, I-6 the one dated Ilkhanid painting inside the period |
| Sinan ship | Mokpo institute | II-14, III-2 junk hull and cargo, 1323 |
| Lady Wenji scrolls | Met 1973.120.3 (open access); MFA Boston leaves | I-12 camp, tents, carts; Khitan dress, so check each detail |
| Cocharelli codex | BL Add MS 27695 | I-1 Genoese interiors and dress, but c. 1330–40 |
| Acre hoard | *Marmora* 6 (2010) | I-4 stone types only |
