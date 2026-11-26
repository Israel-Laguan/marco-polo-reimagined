# Intake — people deep research (S-05 follow-up)

_2026-10-22. Raw run: `CHR-people-raw.md` (28 claims on registry rows). Applies to `CHR.T4`, and partly to S-14 (#1, #4–6, #15–17) and S-15 (family)._

## Trust check

**Verdict: leads, not sources. Nothing is upgraded to ✓, and no `verify` pointer is removed.** Under the trust rules this run falls below the 80% bar, so the right next step is a stricter re-run (prompt below), not salvage.

- **Source quality.** Of 48 bibliography entries, every one is `@misc` with a bare site URL; none is a book, article, edition or archive record with an author, title and year. The sources are English, German, Italian, Spanish, French, Japanese, Korean, Chinese and Catalan Wikipedia; Digital Silk Road pages; Archive.org; Google Books *snippets*; and tourist sites (VeniceTours, History Walks in Venice). The prompt asked for peer-reviewed work and primary sources, and named Pelliot, Allsen, Rossabi, Haw, Larner and Zorzi: none is cited as a work.
- **Not independent of our base text.** The Digital Silk Road project reproduces Yule–Cordier's own chapter notes. Items 9, 11, 12, 14, 16, 18 and 22 cite it, so "confirmed" there means "Yule says so", which we already have.
- **Resolution check (24 page-level URLs, `curl`, 2026-10-22).** 22 resolve; `iranicaonline.org/articles/baydu` returns 403 to a script (not checked); `mariuscomper.uk/did-marco-polo-go-to-china/`, the only source for item 2 (Yongle dadian), is a **404**. The bare site-root URLs (brill.com, dsr.nii.ac.jp, books.google.com, archive.org) cannot be checked against any claim.
- **Content check (7 claims read against the cited page).** 5 agree with the page; 2 do not hold:
  - **#24 Maffeo's "daughter Fiordelisa"** is a mix-up: *Fiordelisa Trevisan* is Niccolò's second wife (de.wikipedia, en.wikipedia *Marco Polo*). The Google Books snippet "father of Pasqua and Fiordelisa" cannot be placed. No evidence in the run that Maffeo married or had children.
  - **#22 "death 8 or 9 January 1324"** contradicts the run's own will date of 9 January 1324: a man cannot have died on the 8th and made a will on the 9th. The 8 January is the old traditional date; we leave Marco's `died` at 1324 and the exact day to S-15.
- **Overstated verdicts.** #28 says "confirmed" that Rustichello was a layman and was taken at Meloria; the run's own sources say "presumibilmente" (Rialfri) and "Yule's assumption", and none says "layman". #20 "7 monasteries (6+1)" rests on Chinese Wikipedia and an Archive.org line, not on the *Zhishun Zhenjiang zhi* or Moule. #1 gives two dates and does not settle them. #19 asserts the Pelliot origin but quotes none.

## Item by item

Grades: **lead** = plausible, one weak or Yule-derived source; **agrees** = matches what the registry already held (from Yule and general reference); **new** = adds something the registry lacked; **reject** = contradicted on checking; **open** = the run did not settle it.

| # | Row | Result | Grade |
|---|---|---|---|
| 1 | arghun | 10 March 1291 (most) or 7 March (ca.wikipedia); reign 1284–91 | open (day); agrees (reign) |
| 2 | oulatay, apusca, coja | names attested in the Yongle dadian notice; Coja's survival not in the notice; only source 404 | open |
| 3 | baidu | 24 March – 4 Oct 1295; grandson of Hulagu via Taraqai, so a cousin | agrees; **new** exact days (lead) |
| 4 | gaykhatu | brother of Arghun; 23 July 1291 – March/April 1295 | agrees; **new** accession day (lead) |
| 5 | ghazan | born 5 Nov 1271; Islam June 1295; accession 3 Nov 1295; Cocachin's marriage "end of 1293 or early 1294" (Pelliot, via DSR) | agrees (the registry already says 1293/94) |
| 6 | cocachin | born c. 1273–74 (deduced from "seventeen": circular); died June 1296 | agrees |
| 7 | alau, berke | Hulagu d. 8 Feb 1265; routed at the Terek by Noqai | agrees |
| 8 | abaga | 1265–82; d. 1 April 1282 | agrees |
| 9 | chinghis | birth 1155/1162/1167; d. Aug 1227; Polo's arrow story has no earlier source (Yule's own note, via DSR) | agrees |
| 10 | sigatay | Kublai's uncle; d. 1242 | agrees (Yule's note) |
| 11 | bayan | 1236 – Jan 1295 (6th or 11th) | agrees |
| 12 | cublay | 23 Sep 1215 – 18 Feb 1294 | agrees |
| 13 | chabi | d. 1281 confirmed; birth **1216** (en.wikipedia, "c. 1216–1281") or 1227 | **conflict with registry (1227)**: age blanked |
| 14 | chinkin | born 8 July 1243; d. 5 Jan 1286 (*Yuan shi*, en.wikipedia *Zhenjin*); Yule's 1284–85 is the slip | agrees; the *Yuan shi* is the primary, not yet seen |
| 15 | dorji | existed, died young; "1233–1263" (ko.wikipedia); Chingkim was Chabi's *first* son (en.wikipedia), so Dorjé's mother was another wife | lead; **new** |
| 16 | temur | 1265 – 1307; succeeded 10 May 1294 | agrees |
| 17 | nayan | Otchigin line (Pelliot); d. 1287; baptism and age not found | agrees (Pelliot not seen in the run) |
| 18 | ahmad | killed 10 April 1282 by Wang Zhu and Gao Heshang; weapon "copper hammer" | agrees |
| 19 | bolad | the *Yuan shi* "Po-lo" is Bolad Chingsang; d. 26 April 1313 | agrees; HOT.3 stands |
| 20 | mar-sarghis | governor from 1277; "seven monasteries (six at Zhenjiang, one at Hangzhou)" | open (not from the primary) |
| 21 | tedaldo | c. 1210; elected 1 Sep 1271; d. 10 Jan 1276 | agrees |
| 22 | marco | birth 1254 has no document; will 9 Jan 1324 (m.v. 1323); capture dispute not researched; death day contradictory | open |
| 23 | niccolo | second wife **Fiordelisa Trevisan**; son Maffeo (will Aug 1300); illegitimate Stefano and Giovannino by Maria; d. between Feb and Aug 1300 (de.wikipedia) | lead; **new** (III-10 already names Stefano and Zannino from Yule) |
| 24 | maffeo | d. 1310–18 (de.wikipedia) vs 1309–18; "daughter Fiordelisa" | **reject** (the child claim); open (marriage, children) |
| 25 | donata | daughter of Vitale Badoer; married 1300; it.wikipedia also cites a **dowry document of 17 March 1312** (Hart 1942) and a 24 June 1325 act (Frari, busta 67) | agrees; **new** (1312 unreconciled) |
| 26 | fantina, bellela, moreta | Fantina m. Marco Bragadin (widow by 1325, sued his heirs); **Bellela m. Bertuccio Querini**; Moreta unmarried in 1324, later m. Ranuzzo Dolfin | lead; **new** |
| 27 | peter-the-tartar | manumitted in the 1324 will; will in the Marciana; shelfmark and arrival not found | open |
| 28 | rustichello | = *Rusticien de Pise*; Meloria 1284 "presumably"; layman not sourced | open |

**One more new lead, outside the 28:** en.wikipedia (*Marco Polo*) says that in **2022** a daughter, **Agnese** (b. 1295/99, d. 1319), was found, from a partnership or marriage that ended before 1300. Unverified. It matters to S-15 and S-13 (a post-2013 find) and to the III-10 plate, where Marco's daughters are named.

## Applied to the registry (`characters.yaml`)

Only what the checks support, each marked as a lead in the text:
- `chabi`: `born` 1227 → null (conflict); no age is computed (II-04 shows "?").
- `dorji`: mother not Chabi (lead); "1233–1263" noted as unverified.
- `baidu`, `gaykhatu`: exact accession dates added as leads.
- `niccolo`: second wife, son Maffeo's will, the two illegitimate sons; death between Feb and Aug 1300 (lead).
- `maffeo`: death range 1309/1310 – 1318 noted; the daughter claim is **not** recorded.
- `donata`: the 1312 dowry document noted as unreconciled.
- `fantina`, `bellela`, `moreta`: husbands added as leads.
- `marco`: the Agnese find noted for S-15.

Not changed: every `verify` pointer, every other date, `book_says`, and the chapter texts. No chapter states any of this as settled.

## Follow-up prompt (stricter run)

Only the rows the run could not settle, with a stricter contract. Run it, save the raw output to `CHR-people-2-raw.md`, bring it back.

```text
I am fact-checking a new English retelling of Marco Polo's Book (base: Yule–Cordier, 1903/1920). A first search-based pass settled most dates from Wikipedia and from sites that copy Yule's own notes, which I cannot use as evidence. I need only the items below, answered from SCHOLARSHIP AND PRIMARY RECORDS.

HARD RULES
- Do not cite Wikipedia, Digital Silk Road, tourism sites, blogs or general encyclopaedias as evidence. You may use them to find a lead, but each claim needs a source I can look up: a book, article, edition or archive record, given as author, title, publisher or journal, year, and (where you saw it) page range, DOI or stable URL.
- Digital Silk Road and Yule–Cordier count as ONE source, Yule. Say when a claim rests on Yule alone.
- For every claim give the source's own wording in a short paraphrase, and say whether you SAW the passage or are relying on another scholar's report of it (and name that scholar). If you did not see it, mark it "reported, not seen".
- Prefer, where they exist: Rashid al-Din (Thackston's translation, or Boyle's for the Ilkhans); the Yuan shi; Pelliot, Notes on Marco Polo (1959–63) and Moule–Pelliot (1938); Cordier's addenda to Yule (1920); Cleaves 1976 on the Yongle dadian notice; Yang Zhijiu 1941; Allsen; Rossabi; Haw (2006); Jackson, The Mongols and the West; Amitai-Preiss; Orlandini 1926 and Zorzi on the Venetian documents; Larner (1999). Where a work is paywalled, name it and give the argument as reported.
- Say "not found" rather than guess. Do not invent page numbers, quotations, DOIs or URLs.

THE ITEMS (row id in brackets)
1. [arghun] Day of death in March 1291: which source gives 7 March, which 10 March, and why do they differ (Hijri conversion? a different event)? Give the primary text (Rashid al-Din, Wassaf, Mamluk sources) and the scholar who reconciles them.
2. [coja, oulatay, apusca] The Yongle dadian notice published by Yang Zhijiu (1941), as discussed by Cleaves (1976) and Haw: exactly what does it name, and does it say anything about who survived the voyage? Is it true that the Book's claim that only Coja survived has no Chinese or Persian confirmation?
3. [chabi] Birth year: 1216 or 1227? Which source gives each, and what does the Yuan shi biography say? How old was she at Chingkim's birth in 1243? (If an age is stated, quote it as reported.)
4. [dorji] Kublai's eldest son Dorji: birth and death years and mother, from the Yuan shi genealogy (Zongshi). Was Chingkim Chabi's first son?
5. [nayan] Age at the 1287 revolt, and the evidence that he was a Christian (Syriac or Latin sources; Rashid al-Din; the Yuan shi). Who proposed the Temüge Otchigin descent, and in which work?
6. [marco] (a) What documentary basis, if any, supports 1254 as the birth year? (b) Where was Marco captured: Curzola 1298 (Ramusio) or near Ayas (Jacopo d'Acqui)? Who argues which, with the key work. (c) Date of death: the will is dated 9 January 1324 (1323 more veneto); what does any document say about the date of death? (d) The 2022 report of a daughter Agnese (b. 1295/99, d. 1319): who found it, in which publication, with what archive reference?
7. [niccolo, maffeo] From the Venetian notarial record (Orlandini 1926, Cecchetti, Zorzi, Larner): Niccolò's second wife (Fiordelisa Trevisan?), his sons Maffeo, Stefano and Giovannino, their legitimacy, the date of Niccolò's death; Maffeo (the uncle): marriage, children, will date, death date. Please check that "Fiordelisa" is Niccolò's wife and NOT a daughter of Maffeo.
8. [donata] The dowry document of 17 March 1312 cited via Hart (1942): is it real, what does it say, and how does it fit a marriage "about 1300"? Is there any basis for Yule's Loredano suggestion?
9. [fantina, bellela, moreta] Husbands and dates, from the 1324 will and the 1325 and later acts (the Frari "busta 67" act of 24 June 1325; Fantina's suit against the Bragadin heirs). Confirm Bellela's husband (Bertuccio Querini?).
10. [peter-the-tartar] Archive and shelfmark of the 1324 will (Biblioteca Marciana, Archivio di Stato?), and the edition (Orlandini? Moule–Pelliot?) in which the manumission clause can be read.
11. [rustichello] (a) The evidence that Rustichello da Pisa the prisoner is the Arthurian compiler Rusticien de Pise: who established it and how. (b) Was he a layman? (c) Evidence that he was taken at Meloria in 1284, as opposed to in a later war.
12. [mar-sarghis] The Zhishun Zhenjiang zhi (1332) entry: number of churches, their dates, and their location. A.C. Moule, Christians in China before 1550 (1930), is the usual translation: what does it say?

OUTPUT FORMAT (required). (1) A table: # · row id · finding · verdict (confirmed / corrected / disputed / not found) · sources as works (author, title, publisher or journal, year; DOI or URL if seen) · SAW or REPORTED · confidence (high / medium / low). (2) Short prose only where scholars disagree, naming who holds which position. (3) A bibliography of the WORKS used, each with a real BibTeX entry (@book, @article, @incollection), not site pages. (4) Questions you could not resolve.
```

When the second run comes back, the rows it settles go through `CHR.T4`; the rest stay `verify`.
