# S-18 — Maritime Asia and the return voyage (Vol. III)

**Status:** done (best-effort intake, 2026-11-12; follow-up research open) · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** Vol. III `.T1`/`.T4` enrichment; `GAZ` rows for Vol. III (feeds S-04); `MAP` A15–A17; `DIA` (monsoon calendar, ship cross-section C12); Vol. III back-matter trivia

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
- [x] `research/results/S-18-raw.md` saved (supplied report kept verbatim; audited in the [intake](../research/results/S-18-intake.md))
- [x] Identifications for the uncertain Vol. III rows handed to S-04 (§ S-18 handoff): no row changes
- [x] `registry/enrichment.md` § S-18; voyage and monsoon data in `registry/facts.md` § S-18 (tag `DIA`)

## Feedback to plan
- `multimedia-plan.md` § A (A15–A17 route) and § C (C11 monsoon, C12 junk cross-section)
- `illustration-plan.md`: caption facts for the junk, Chipangu invasion and pearl-fishery plates

## Follow-up prompts
**S-22 supplement cross-reference (2026-11-13):** The Java Sea wreck dating study (`niziolek2018revisiting`) and Vosmer's sewn-boat synthesis (`vosmer2019sewn`) are catalogued as potential III-02/III-03 and III-08 sources in `registry/enrichment.md` S22-E1–E2. Abstracts/metadata were checked, not the full papers. The wreck's redating is a scholarly assessment, not proof of Polo's ship or port; *Jewel of Muscat* reconstructs a much earlier vessel. Read the relevant studies before using specific details. This does not close any S-18 follow-up item.

The [targeted follow-up prompt](../research/S-18-follow-up-prompt.md) covers what the run left open and the base text could not answer. Pelliot's BASMAN and SEMENAT come first, then EI XII (Motupalli), Talbot on Rudrama, Moule–Pelliot on the fleet and survivor counts, the Trebizond loss in the family documents, Taddesse Tamrat on Abash 1288, the Takashima reports, Kayal and Qalhat, the Pasai gravestone, the Pandya brothers, Champa/Malaiur in Hall and Miksic, and the Konjikidō link. Items 1–3 need a person with library or Toyo Bunko access.

**Follow-up run taken in (2026-11-12):** [raw](../research/results/S-18-followup-raw.md) · [intake](../research/results/S-18-followup-intake.md). It read Pelliot's BASMAN and SEMENAT, EI XII no. 22, Talbot, Moule–Pelliot vol. I with Maffeo's will, Dayalan, Rougeulle, Hall and Nilakanta Sastri. Its Pelliot "page corrections" are scan numbers and are rejected. Still open: Pelliot FERLEC/LAMBRI/PENTAN/SEILAN (scans II/0129, 0165, 0206), Orlandini, Trimingham/Pankhurst/Taddesse Tamrat, Lambourn and Guillot–Kalus read directly, Karashima, Miksic, Sasaki's chapters, CiNii on the Konjikidō.

## Findings
[Supplied raw report](../research/results/S-18-raw.md) · [gap audit, base-text answers, checked findings and gazetteer handoff](../research/results/S-18-intake.md).

The report is honest about its gaps but did not read Yule. The base text answers four of its open questions. (1) Polo describes a **sepulchre** on Adam's Peak, not a footprint. (2) The fleet is **13** ships, not 14. (3) "600" is two different figures: the French text has 600 embarked and 8 (G.T. 18) survivors; Ramusio has 600 dead. (4) Yule himself raised and rejected the Amda Ṣeyon parallel for the 1288 Abash war. The Book has no Trebizond robbery.

The report also missed the project's Pelliot readings for Locac, Malaiur and Dagroian; Pelliot does discuss Langkasuka, and rejects it. Five citations were wrong or incomplete and are corrected from Crossref: the Nanhai I and Sen DOIs, the Talbot year, the authors of the typhoon study and of the 1964 essay. Newly checked: the Gulf of Mannar midden study, the Deng–Li monsoon calendar, the kamikaze sediment study, Kovesi's rhinoceros essay, Prange, Sen and Talbot. Leads only, not yet citable: Ganapatideva's Motupalli charter (EI XII no. 22, 1244–45) and Yagbeʾa Ṣeyon (r. 1285–94) as Polo's Abash king. Most of the report's "confirmed" rows rest on Wikipedia and stay leads.

**After the follow-up:**
- Fleet: 13 ships (Yule/Pauthier) or 14 (F, Moule–Pelliot). Survivors: 8 or 18. Deaths: 500–700 by witness.
- F-31 is corrected: Rudrama was Ganapati's daughter, r. 1263–89 (Talbot).
- The Motupalli charter is Ganapati's, 1244–45 (Hultzsch, EI XII).
- The "Trebizond robbery" is a ~4,000-hyperpera *loss* in Maffeo's 1310 will.
- Sonder Bandi: c. 1276–1292/93.
- Qalhat grew from Polo's decade on (Rougeulle).
- Java was an entrepôt for spices, not their producer (Hall).
- The Pasai gravestone's date is disputed.
- The Konjikidō link is not a scholarly identification.

## Decision
Close this timeboxed intake **best effort**. It does not claim the historical questions are settled. Use only the base-text answers and the source-checked rows in the intake; everything marked *lead* waits for the follow-up. No gazetteer row changes: the Pelliot readings already in the rows outrank the report. The monsoon panel (C11) keeps its simplified months, now with a citation. The C12 junk keeps the 13 compartments (F-14).

## Tasks created on close
- Chapter backlog handoffs are listed in the intake under "Corrections to carry into Vol. III files": III-01, III-04, III-06, III-07, III-09, back-01. These are future Notes and re-voice work, not manuscript edits; ch-09 [14] and F-23 already carry the 8/18 survivors and the sepulchre.
- `GAZ.T6`: S-04 § S-18 handoff (no changes; Pelliot BASMAN/SEMENAT pending).
- `DIA`: facts S18-F1–F6 feed A15, A16, C11, C12 and the III-9 plate brief (13 ships, as it already says).
- `III-B1` trivia candidates: S18-E1, E2, E6, E8 in `registry/enrichment.md`.
