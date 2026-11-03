# S-18 — Maritime Asia and the return voyage (Vol. III)

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** Vol. III `.T1`/`.T4` enrichment; `GAZ` rows for Vol. III (feeds S-04); `MAP` A15–A17; `DIA` (monsoon calendar, ship cross-section C12); Vol. III back-matter trivia

## Question
What do maritime archaeology and Indian Ocean history add to Polo's ships, islands, ports and return voyage? What are the best current identifications for his disputed sea-route places?

## Why it matters
- Vol. III leans on Yule's notes for the Indian Ocean, and Yule wrote before the field of maritime archaeology existed.
- Since then: the Quanzhou ship (1974), Nanhai I (raised 2007), the Takashima wrecks of the 1281 invasion fleet (identified from 2011 onward), the Sinan wreck (1976), excavations at Kollam and Pasai, and a large Indian Ocean literature (Abu-Lughod, Chaudhuri, Sheriff, Kauz, Lambourn and others).
- Four Vol. III gazetteer rows are uncertain: Locac, Malaiur, Basman/Dagroian and Sememant.

## Inputs
- `vol-3/ch-01` … `ch-09`, `front-01`, `front-02`, `back-01`
- `gazetteer.csv` Vol. III rows; critique III-m3, III-m4
- S-14 results for III-01 and III-09 (don't duplicate those items)

## Method
1. Run the prompt and save the output to `research/results/S-18-raw.md`.
2. Intake as in S-16/S-17. Monsoon and voyage dates → `registry/facts.md` tagged `DIA`.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). For the SEA chapters and the return voyage (c. 1291–1295), I need what modern maritime archaeology and Indian Ocean history add to, correct in, or corroborate in Polo's account. For each topic: Polo's claim, modern evidence, best sources.

- III-01: Chinese ocean-going junks: Polo describes four-masted ships, 13 watertight bulkhead compartments, double/triple planking re-sheathed yearly, crews of 200–300, tenders. Compare: the Quanzhou ship (1974), Nanhai I, the Sinan wreck, Zhou Daguan and Ibn Battuta on junks. Chipangu (Japan): the gold "palace roofed with gold" (Chūson-ji Konjikidō?), the Mongol invasions of 1274 and 1281 (the Takashima underwater finds), the kamikaze typhoon, and the "stone heads" / magic-stone story.
- III-02: Chamba (Champa): Polo's visit c. 1285 (or on the return?); King Jaya Indravarman / the tribute of elephants and aloes wood; Sogatu (Sögetü)'s campaign of 1282–85. Java: the Mongol expedition of 1292–93 against Singhasari/Kertanagara and the founding of Majapahit; Java's wealth in pepper, nutmeg, cloves.
- III-03: Locac (southern Thailand / Langkasuka?), Pentam (Bintan), Malaiur (Melayu/Jambi? Singapore/Temasek?); Java the Less (Sumatra) and its kingdoms: Ferlec (Perlak), Basman (Pasai), Sumatra (Samudra), Dagroian, Lambri, Fansur — current identifications; the Samudra-Pasai gravestones (Sultan Malik al-Salih, d. 1297) and Islamisation; the five-month wait for the monsoon; sago; the "unicorn" (Sumatran rhinoceros); fake pygmies made from monkeys.
- III-04: Necuveran (the Nicobars) and Angamanain (the Andamans: the "dog-headed" legend); Seilan (Sri Lanka): the great ruby of the king (sources), Adam's Peak and the Buddha's tooth and alms bowl relics, Sergamoni Borcan (the Buddha's life as told by Polo — its accuracy).
- III-05: Maabar (the Pandya coast, Tamil Nadu): the pearl fishery in the Gulf of Mannar and the shark-charmers (brahmins); the five Pandya brothers and King Sundara Pandya; sati; the horse trade from Hormuz and Kish (the Wassaf figures); St Thomas at Mylapore — tradition and archaeology; the Kayal port (Cail).
- III-06: Mutfili (the Kakatiya kingdom, Motupalli port; Queen Rudrama Devi — the Motupalli port inscription: its date and what it says about merchants) and the diamond valley with eagles and meat (the legend's ancient sources); Lar and the brahmins; Kesmacoran (Makran).
- III-07: Coilum (Kollam/Quilon): brazilwood, pepper, indigo; the Kollam excavations and Chinese ceramics; Eli (Mount Eli/Ezhimala); Melibar (Malabar) and the pirates; Gozurat (Gujarat), Tana (Thane), Cambaet (Khambhat/Cambay), Semenat (Somnath), Kesmacoran; the Male and Female Islands (sources of the legend); Socotra and its Christians and sorcerers; Madagascar (Mogadishu confusion) and the rukh; Zanghibar; Abash (Abyssinia/Ethiopia): the 1288 war Polo describes against the Ethiopian (Solomonic) chronicles.
- III-08: Aden and the trade to Egypt; Escier (Shihr) and Dufar (Zafar): frankincense; Calatu (Qalhat): archaeology (UNESCO 2018); Hormuz again.
- III-09: The return voyage: dates, fleet size (14 ships, 600 dead?), the stop in Sumatra, the princess Kököchin (Cocachin) married to Ghazan; the envoys' names; the Polos' route home via Tabriz, Trebizond (and the robbery there; is it documented?), Constantinople, Negropont; the golden paizas given by Gaykhatu.
- III-F1: the best modern overviews of the 13th–14th-century Indian Ocean world to recommend.

Also: a short summary of the monsoon calendar (NE and SW monsoons) and the sailing seasons Polo implies, with a source.

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-18-raw.md` saved
- [ ] Identifications for the uncertain Vol. III rows, handed to S-04
- [ ] `registry/enrichment.md` § Vol. III; voyage and monsoon data in `registry/facts.md` (tag `DIA`)

## Feedback to plan
- `multimedia-plan.md` § A (A15–A17 route) and § C (C11 monsoon, C12 junk cross-section)
- `illustration-plan.md`: caption facts for the junk, Chipangu invasion and pearl-fishery plates

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- Vol. III `.T1`/`.T4` items; `GAZ.T*`; `DIA.T*` data; `III-B1` trivia
