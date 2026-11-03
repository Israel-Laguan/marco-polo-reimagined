# S-16 — The overland route: archaeology and identifications (Vol. I)

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** Vol. I `.T1`/`.T4` enrichment; `GAZ` rows for Vol. I (feeds S-04); `MAP` A3–A6; Vol. I back-matter trivia

## Question
For each place and episode on the outbound road, from Ayas to Shangdu: what does modern archaeology, history and geography add to or correct in Yule's identifications? Which disputed identifications have a current best answer?

## Why it matters
- Vol. I's corroborations stop at 19th-century travellers (Wood, Gordon, Stein's predecessors) cited through Yule.
- Since then there have been major excavations: Karakorum (German–Mongolian work), Shangdu/Xanadu (UNESCO 2012), the Silk Road oasis sites, Alamut and the Ismaili castles, Hormuz and Old Hormuz (Minab).
- Gazetteer rows for Tonocain/Arbre Sec, Pem and Tenduc are marked uncertain (S-04).

## Inputs
- `vol-1/ch-03` … `ch-13`, `front-01`, `front-02`, `back-01`
- `gazetteer.csv` (Vol. I rows; uncertain: Tonocain/Arbre Sec, Pem, Tenduc)
- Critique vol-1 (I-M8 naming); chapter backlogs § Naming

## Method
1. Run the prompt and save the output to `research/results/S-16-raw.md`.
2. Intake: trust checks; identifications → S-04 working notes (`registry/facts.md`, tagged `GAZ`); new material → `registry/enrichment.md` by chapter, with a suggested slot.
3. Pick at most two or three enrichment items per chapter for the re-voice. The rest go to back matter or are dropped, so the asides budget (≤ 4 per chapter) holds.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). For the OUTBOUND overland route (c. 1271–1275), I need what modern scholarship, archaeology and geography add to, or correct in, Yule's identifications and notes. Focus on findings since c. 1920, and especially since 1990. For each place: the current best identification (with coordinates if possible), significant excavations or finds, and one or two concrete details that corroborate or contradict Polo's description.

Places and topics, with book section IDs:
- I-03/I-04: Laias/Ayas (Lesser Armenia's port; Venetian and Genoese presence); "Turcomania" (Konya, Kayseri, Sivas carpets); Greater Armenia, Arzinga (Erzincan), Mount Ararat; Georgiania (Georgia) and the "Iron Gate" / Alexander's wall at Derbent; the "fountain of oil" at Baku (earliest oil-field references).
- I-05: Mausul (Mosul) and its muslin; Baudas (Baghdad) and the 1258 sack; the caliph starved among his treasure (sources of the legend in Persian and Latin texts); Tauris.
- I-06: Tauris (Tabriz) as the Ilkhanid commercial centre (the Italian merchant colony there); Saba/Saveh and the Magi legend; the eight kingdoms of Persia; Persian horses and asses.
- I-07: Kerman (turquoise, steel, embroidery); the Caraonas raiders and the "darkness" they make; Old Hormuz (Minab) — archaeology, and the move to Jarun island c. 1300; Gulf ships "sewn" without nails; Hormuz heat and the hot wind.
- I-08: The "Arbre Sec" / Arbre Sol and Tonocain — current identifications; the Old Man of the Mountain (the Nizari Ismailis, Alamut and its fall in 1256, the "garden" legend and its sources; Farhad Daftary's work on the Assassin legends); Sapurgan melons; Balc (Balkh).
- I-09: Badashan (Badakhshan): balas rubies (spinel mines on the Kuh-i-Lal), lapis lazuli at Sar-i Sang; horses descended from Bucephalus; Wakhan.
- I-10: The Pamir (the "roof of the world" phrase — is it Polo's?); Ovis poli; fire burning less hot at altitude; Cascar (Kashgar), Samarcan, Yarcan (Yarkand), Cotan (Khotan) jade; Pem (Keriya?) and Charchan — current identifications.
- I-11: Lop and the desert spirits (compare Faxian and Xuanzang); Sachiu (Dunhuang) and its Buddhist culture; Camul (Hami) hospitality custom; Chingintalas and asbestos ("salamander"); Sukchur and rhubarb; Campichu (Ganzhou) and its reclining Buddha (the Zhangye Great Buddha Temple); Etzina (Khara-Khoto, Kozlov's 1908 excavations); the Tangut (Xi Xia) heritage.
- I-12: Caracoron (Karakorum) — results of the German–Mongolian excavations (Hans-Georg Hüttel, Ernst Pohl, others: verify), the silver tree of Guillaume Boucher (Rubruck), the palace identification debate; the Chinggisid origin story and Prester John (the Ong Khan identification); Tenduc and the Önggüt Christians (Prince George, Olon Süme excavations); Bargu; the Mecrit/Merkit; gyrfalcons; the "Land of Darkness".
- I-13: Chandu/Shangdu (Xanadu): site plan, UNESCO 2012 inscription, the bamboo or cane palace; Kublai's mare's milk libation (the Ordo); the Bacsi (Tibetan and Kashmiri lamas) weather-magic; Coleridge's route to Xanadu via Purchas.
- I-F1: the political world c. 1260 (Mongol successor khanates, Mamluks, Byzantium, Italian trading posts in the Black Sea) — the best modern overview works to cite.

Also: for the whole outbound itinerary, what is the current scholarly reconstruction of the Polos' route and dates (Yule versus later reconstructions; did they go via Hormuz and turn back, or is that Yule's inference)?

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-16-raw.md` saved
- [ ] Identifications for the uncertain Vol. I gazetteer rows, with rationale, handed to S-04
- [ ] `registry/enrichment.md` § Vol. I: candidates per chapter, each with a slot and a source key

## Feedback to plan
- `multimedia-plan.md` § A (route reconstruction for A3–A6)
- `illustration-plan.md`: caption facts for the Vol. I plates (Alamut, Shangdu)

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- Vol. I `.T1` (corrections) and `.T4` (Notes enrichment) items; `GAZ.T*` rows; `I-B1` trivia items
