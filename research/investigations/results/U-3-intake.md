# U-3 return — source-check intake (2026-11-17)

The return for prompt U-3 ([prompt](../2026-11-17-unresearched-claims-prompts.md)) is preserved unchanged as [raw](U-3-raw.md). The user did not say which tool or model produced it. It worked from OCR and HTML through a summarising fetch tool, saw no page images, and marks the Yuan legal codes, Allsen, Aubin, Mostaert, Carpini's Latin and Haw as NOT SEEN.

## Spot check: 10 propositions, 10 hits (100%, above the 80% threshold)

Yule–Cordier was checked in the project's own copy (`refs/yule-vol1.txt`, `refs/yule-vol2.txt`). Pelliot was read through the Toyo Bunko/NII OCR, Iranica online, and Ragagnin 2017 through the publisher's PDF.

| # | Source opened | Proposition | Result |
|---|---|---|---|
| 1 | Yule–Cordier II.20 (`refs/yule-vol1.txt`) | The 20-days' radius applies to keeping hawks or hounds; the March–October ban on hare, stag, buck and roe applies "throughout all the Emperor's territories" | **Hit**, verbatim |
| 2 | Yule II.20, note 9 | Yule quotes Pétis's Yasa rule as "between March and October 'no one should take stags, deer, roebucks, hares…'", then calls it "just the reverse of Polo's statement … merely a careless adoption of the latter" | **Hit**. Pétis therefore gives the same months as Polo by Yule's own quotation. Pétis's 1722 book was not reopened here |
| 3 | Yule II.38, note 1 (`refs/yule-vol2.txt`) | Roi d'Or = the Kin emperor, "Altun Khán", following Marsden; "Of the legend itself I can find no trace"; Wylie searched the Liao and Kin histories | **Hit** |
| 4 | Same, footnote | Cordier: "no trace of it in Harlez's French translation … of the History of the Kin Empire, 1887" | **Hit** |
| 5 | Yule note on Caichu; index | Kiai-chau (Jiezhou) is Marsden's suggestion, adopted by Wylie and Richthofen; Yule's index: Cachanfu = P'u-chau fu / Ho-chung fu | **Hit**. The return names only Wylie and Richthofen; Marsden came first |
| 6 | Pelliot, *Notes* I, scan 140 ("Caiciu") | "I feel confident that «Caiciu» is Chiang-chou" (絳州); Chi-chou rejected; Marsden's Chieh-chou "not on the main track" | **Hit**. The return omits Pelliot's caveat that the text's distances and bearings fit neither this nor any other site |
| 7 | Yule II.34, note 3 (`refs/yule-vol1.txt`) | The passage is "more or less interpolated", reintroducing the Tartar god of I.53 as a Chinese one; the "Most High" may be "the ancestral tablet" | **Hit**, verbatim |
| 8 | Pelliot, *Notes* II, scan 195 ("Natigai") | Readings nacigai (F, VA) and others; Natigai = Plan Carpine's «Ytoga» (var. Itoga, Vtoga) = Ötükän/Ätügän, after Banzarov; Blochet's "Rubrouck" corrected to Plan Carpine | **Hit** |
| 9 | Spuler, "Atābakān-e Lorestān", *EIr* II/8, pp. 896–898 | Great Lur: Yūsofshāh I from 1274–75, confirmed by Abaqa; Afrāsiyāb I from c. 1288, executed by Ghazan 26 Oct 1296. Little Lur: Tāj al-Dīn executed 1278–79, rulers deposed by Gaykhatu 1293, Ṣamṣām al-Dīn executed 1296 | **Hit** |
| 10 | Ragagnin, "L'ambiguità del teonimo poliano Natigay-Načigay", *Quaderni Veneti* 6/2 (2017); Ragagnin, "Some further notes on Marco Polo's Tatar gods", *Acta Mongolica* 18 (2019), 63–68 | Mostaert's analysis of a 1312 Buddhist fragment with *Načigai eke* ("Mother Načigai"); a protoform *\*nitügei*; Carpini's Itoga/Utoga, *Hist. Mong.* III 10. The 2019 article's references list Mostaert (1967) and Haenisch on the 1312 fragment | **Hit**. The 2017 text dates Mostaert 1957 and the 2019 references date him 1967, as the return noted. The 2019 body text was not visible |

**Not an error in the sources, but a misreading by the return.** Its "Corrections to make first" table treats our file IDs (II-04, I-06, II-06, II-05) as Yule book and chapter numbers. It also treats the prompt's paraphrase as the endnote: "within 20 days' journey nobody may take game", "fallow deer", and "Itoga as an earlier Polo reading". The manuscript Notes do not make those statements; II-04 Note [15] already says "20-day hawking reserve". Disregard those rows.

**Not checked here:** Pétis 1722 directly; Bosworth, "Hazāraspids"; Spuler, "Ābeš Ḵātūn"; Pelliot's Cielstan, Ispaan, Soncara and Tunocain entries; Jia Yiren 2023 on 天地君親師 tablets; Palladius via Cordier.

## A manuscript error found during intake

**II-04 body l. 41** ends the closed-season passage with: "Beyond that term, however—to wit from March to October—everybody may take these animals as he list." Yule reads: "Beyond the term I have mentioned, however, to wit **that** from March to October, everybody may take these animals". The paraphrase drops "the term I have mentioned … that". It now says the open season is March–October, contradicting the sentence before it. **Fix:** "Outside that season, however—that is, outside March to October—everybody may take these animals as he list." This is a straightforward correction of the retelling, with no research question in it. **Applied 2026-11-17**, together with Note [15] and the I-12 Natigay gloss.

## Findings and handoffs

1. **Hunting (II-04 Note [15]).** "Pétis de la Croix may reverse Polo" is wrong. Pétis's Yasa rule gives the same months (March–October). Yule's "just the reverse" is his own remark and appears to be a slip; he himself suspected Pétis had copied Polo. **Proposed:** "~ Pétis de la Croix's Yasa rule (after Mirkhond) gives the same March–October season; Yule calls it 'the reverse' but suspects Pétis copied Polo [@yc, 2.20, note 9]. No Yuan legal text checked." The "✓ Imperial game law type (*Yasa* / Yuan)" is unverified for Yuan law, so make it ~. Leads for the Yuan codes: *Yuan shi* j. 101 and 105; *Yuan dianzhang*, Ministry of War, 打捕; Allsen 2006.
2. **Eight kingdoms (I-06 Note [12]).** The Note holds. Pelliot accepts Šūlistān, Ispahān (Z *yspaan*), Šabānkārah and Tūn-o-Qāïn (reported; not reopened here). Optional addition, from Spuler's checked article: in Polo's day Great and Little Lur were ruled by local atabegs under the Ilkhans, installed, confirmed or executed by them. Cite *EIr* "Atābakān-e Lorestān" (`spuler1987atabakan`). Fars under Abish Khatun until 1284 is reported, not checked.
3. **Golden King (II-06 Notes [6]–[7]).** Add Pelliot's site, Jiangzhou 絳州, to the site list, with his caveat that the distances fit no site (`[@pelliot1959notes, vol. 1, "Caiciu"]`). Credit Kiai-chau to Marsden, Wylie and Richthofen. Note [7]'s "no Jin-history match" now has a source: Wylie (Liao and Kin histories) and Cordier (Harlez), via Yule.
4. **Natigai (II-05 Note [22]; I-12 body l. 39, Note [15]).** II-05: cite Yule's own note that the passage is "more or less interpolated" and that the tablet may be ancestral (`[@yc, 2.34, note 3]`). I-12 body l. 39 states "Natigay—Etügen—" as a fact. The identification is disputed: Pelliot (after Banzarov) equates Natigai with Ötükän and Carpini's Itoga; Mostaert and Ragagnin read *Načigai*, a goddess attested in 1312, and exclude Ötükän. **Fix:** soften the dash-gloss to "Natigay (often linked with the earth goddess Etügen)". In Note [15], cite `[@pelliot1959notes, vol. 2, "Natigai"]` and `ragagnin2017natigay`.

## Registry

- `facts.md`: rows F-53 (hunting season and Pétis), F-54 (eight kingdoms), F-55 (Caichu), F-56 (Natigai).
- `bibliography.bib`: `ragagnin2017natigay` and `ragagnin2019tatar` confirmed (text or landing page read); `spuler1987atabakan` confirmed (*EIr*, doi:10.1163/2330-4804_EIRO_COM_6043).
- Chapter handoffs: `U-3 source handoff` in II-04, I-06, II-06, II-05 and I-12.
