# Character registry — method note (S-05)

The registry is the **single authority for people**: how the prose names them, their dates, and how the plates draw them. It does for people what `gazetteer.csv` does for places (S-04), with the same rules wherever they apply.

| File | Holds |
|---|---|
| [`characters.yaml`](characters.yaml) | 54 people: book form, gloss, variants, other names, dates, role, relations, what the Book gets wrong, which spike must verify, chapters (generated) |
| [`character-cards.yaml`](character-cards.yaml) | 26 visual cards, the Polo party's itinerary by year, 22 plate scenes with their figures |
| [`../status/character-name-diff.md`](../../editorial/plans/status/character-name-diff.md) | generated: bare variants and unglossed first mentions per chapter |

```
python3 tools/characters.py check            # schema, unique forms, no clash with gazetteer forms, scenes consistent
python3 tools/characters.py ages [--md]      # every figure's age in every plate scene; impossible co-presence fails
python3 tools/characters.py cue marco 1291   # the [PERIOD] / [AVOID] lines for a plate prompt
python3 tools/characters.py chapters         # rewrite `chapters` in characters.yaml from the manuscript
python3 tools/characters.py report --md      # > plans/status/character-name-diff.md
```

The lint applies the naming rule through `name_policy`. In narrative chapters, violations are **errors** tagged *(S-05)*. The report uses the same first-mention check.

## Naming policy

- **Book form.** Where Polo names the person, the prose uses **Yule's form of Polo's text**: *Cublay*, *Alaü*, *Argon*, *Casan*, *Kiacatu*, *Caidu*, *Achmath*, *Chinkin*, *Mongou*, *Sigatay*, *Barca*, *Abaga*, *Acomat*, *Unc Can*. Where Polo does not name them, it uses the standard modern English form: *Chabi*, *Bolad*, *Empress Dowager Xie*. The voice guide already used the book form for people ("Cublay Kaan is not drawn as a giant"), so this formalises existing practice.
- **Europeans keep their modern form**, as Venice and Genoa do: *Niccolò* (Yule: Nicolas/Nicolo), *Rustichello* (Yule: Rusticiano), *Tedaldo*.
- **Gloss rule.** On the first mention in a chapter, give the book form with its modern gloss: *Cublay (Kublai)*, *Argon (Arghun)*, *Casan (Ghazan)*. After that, the book form only. No gloss where the forms coincide or differ only by a diacritic (*Nayan*, *Bayan*, *Temur*). A title form can carry the gloss: *Acomat Soldan (Ahmad Tegüder)*.
- **No bare variants** in narrative prose. That covers *Kublai*, *Hulagu*, *Chagatai*, *Ghazan* and the rest, in asides as much as in story; quotations, Notes and tables are exempt. An aside that corrects the Book still names its people in the book form: "Argon's brother Kiacatu", not "Arghun's brother Geikhatu".
- **Other names are not variants.** `also` lists names that are right in their place: *Tedaldo* becomes *Gregory X* at his election (1 Sept 1271); *Cublay Kaan*, *Bayan Chincsan*, *Acomat Soldan*, *the Old Man* / *Aloadin*. The lint never flags them.
- **One form, one person.** *Bayan* (the general, II-10, II-12) and *Baian* (the Kaan's huntsman, II-04) are different men; keep the spellings apart. *Ahmad* in *Ahmad Tegüder* is not *Achmath*. I-12's *Argons* are a people, not the Ilkhan (`SCOPE_OUT` in the tool).
- **Exemptions** (as for places): front/back matter and the reception chapters III-10 to III-12 may use modern forms in prose. Polo's own people still take the book form where those chapters retell the Book.
- **Out of scope.** Scholars, editors and witnesses cited as sources (Ramusio, Pipino, Jacopo d'Acqui, Yule, Wood) belong in the bibliography. Saints and figures of legend (St Thomas, Adam, Alexander) are not characters. *Prester John* is a legendary row in `gazetteer.csv`, which owns that form; the people Polo pins the name on (Unc Can, King George) are here.

The 2026-11-24 naming sweep found zero bare variants and zero missing first glosses. The [generated report](../../editorial/plans/status/character-name-diff.md) records the results. Earlier findings remain in the chapter naming tasks.

## The cast

The 2026-10-22 cast snapshot ranks people by the number of manuscript files whose prose names them. The YAML `chapters` field holds the current references.

| Rank | Book form (gloss) | Files | Group | Card |
|---|---|---|---|---|
| 1 | Marco | 48 | Polo party | ✓ |
| 2 | Cublay (Kublai) | 19 | Yuan | ✓ |
| 3 | Rustichello | 13 | Venice | ✓ |
| 4 | Niccolò | 12 | Polo party | ✓ |
| 5 | Maffeo | 12 | Polo party | ✓ |
| 6 | Cocachin (Kököchin) | 10 | Ilkhanate | ✓ |
| 7 | Chinghis (Chinggis Khan) | 9 | Mongol | ✓ |
| 8 | Alaü (Hulagu) | 9 | Ilkhanate | ✓ |
| 9 | Achmath (Ahmad Fanakati) | 7 | Yuan | — |
| 10 | Columbus | 7 | reception | — (PD plate) |
| 11 | Mongou (Möngke) | 7 | Mongol | — |
| 12 | Caidu (Kaidu) | 5 | Mongol | ✓ |
| 13 | Argon (Arghun) | 5 | Ilkhanate | — |
| 14 | Sigatay (Chagatai) | 5 | Mongol | — |
| 15 | the Old Man of the Mountain | 5 | Levant | — |
| 16 | Barca (Berke) | 4 | Golden Horde | — |
| 17 | Tedaldo / Gregory X | 4 | Church | ✓ |
| 18–22 | Casan (Ghazan) ✓, Kiacatu (Geikhatu), Bayan ✓, Abaga (Abaqa), Bundukdar (Baibars) | 3 each | | |
| 23– | Nayan ✓, Chinkin (Chingkim), Facfur, Bolgana, Temur, Oulatay, Litan, King George, Barac, Mar Sarghis, Sentemur, Clement IV | 2 each | | |

Single-chapter figures are in the registry only when a plate shows them (Aijaruc, Donata, the daughters, Peter the Tartar, Cepoy, the Caliph, Chabi), when the text gets them wrong (Unc Can, Baidu, Acomat), or when they matter to another entry (Dorjé, Mangalai, Coja, Apusca, Empress Dowager Xie, Andrea Polo). HOT.3 identifies **Bolad** in II-05 and III-12.

## Who is where, when

The itinerary in `character-cards.yaml` is coarse on purpose (regions, by year). It is enough to prove the absences that matter. The tool fails if a scene puts a figure where the dates or the itinerary forbid.

| Years | Elder Polos | Marco | Fixed points for the plates |
|---|---|---|---|
| 1254 | Constantinople trade | born, Venice | — |
| 1258 | — | Venice | Alaü takes Baudac (Feb); the Caliph dies |
| 1260–62 | Soldaia → Barca's court | Venice | Barca–Alaü war; Alaü routed on the Terek, 1263 |
| 1262–65 | Bocara, three years | Venice | — |
| 1265–66 | at Cublay's court | Venice | Cublay c. 50; the first paiza |
| 1269 | Acre (April) → Venice | 15; mother dead | Clement IV dead (Nov 1268); conclave until Sept 1271 |
| 1271 | Acre, Layas (Nov) | 17, sets out | Tedaldo elected Gregory X (1 Sept) |
| 1272–74 | Persia, Badashan, Pamier, Lop, Tangut | 18–20 | **Xiangyang falls March 1273: no Polos** |
| 1275 | Kemenfu / Chandu | 21 | Cublay c. 60 |
| 1275–91 | in China | 21–37, missions | Bayan takes Lin'an 1276 (Polos not there); Chabi d. 1281; Achmath murdered 1282; Chingkim d. mid-1280s; Nayan 1287 (no Polos on the field) |
| 1291 | Zayton, sail early 1291 (or 1292) | 37 | Argon already dead (March 1291) |
| 1291–93 | the voyage; Samara five months | 37–39 | — |
| 1293–94 | Cocachin to Casan; Kiacatu at Tauris | 39–40 | Cublay d. Feb 1294 (news reaches them in Persia) |
| 1295 | Venice | 41 | Donata not yet married to Marco |
| 1298–99 | (Venice) | 44, Genoa prison | Rustichello writes; release 1299 |
| by 1300 | Niccolò dead | marriage to Donata, date uncertain | — |
| 1307 | — | 53 | Cepoy copy (August) |
| 1309–18 | Maffeo dies | — | — |
| 1324 | — | will, 9 Jan; dies | Peter the Tartar freed |

**Impossible co-presence the tool guards:** Polos at Xiangyang (II-11); Chabi at any court scene after 1281 (II-03); Argon at the bride's arrival (III-09.s); Niccolò or Maffeo at the 1324 will. **Absences the text decides** (`not_shown`, not provable by region): Polos at the Nayan battle (II-01) and Bayan's camp (II-10); Cublay at the Persian farewell; Donata at the 1295 homecoming.

## Contested facts about people

These go to S-06 (and S-14 / S-15 for the research). A chapter states them only with the verdict, or hedged. S-06's verdicts for the S-14 rows below are in `registry/facts.md` (F-01, F-04, F-05, F-06, F-08, F-15, F-16, F-17, F-33, F-34, F-35).

| Person | Claim | Status | Where |
|---|---|---|---|
| Alaü / Barca | Outcome of the 1262–63 war (the Book has it backwards) | S-14 #1 | I-02 |
| Nayan | Descent from Temüge Otchigin, not Belgutai; 1287 not 1286 | S-14 #4 | II-01 |
| Chabi | Birth year and age unestablished | *Yuan shi* 106 and 114 give no birth year (CHR-people-4 and FINAL-ACCESS) | Registry and card |
| Dorjé | Eldest son of Cublay; birth year and mother unknown | *Yuan shi* 107 gives his rank, and 114 names Chinkin as Chabi’s son (FINAL-ACCESS) | II-02 Note [11] |
| Chinkin | Death in the mid-1280s. January 1286 is a lead from the *Yuan shi* chronology; Yule gives 1284–85. | S-14 #6 and F-06 | II-02 Note [12] |
| Kiacatu, Baidu, Casan | Brother, cousin, accession 1295 | S-14 #5 | II-15 |
| Achmath / Bolad | The annals' "Po-lo" is Bolad | settled (Yule–Cordier addenda); HOT.3 | II-05, II-11, III-12 |
| Argon | Death 10 March 1291 (Yule = 7 Rabīʿ I 690; "7 March" is the Hijri day misread) | **settled** (CHR-people-2) | III-09 |
| Oulatay, Apusca, Coja | The 1290 *Yongle dadian* notice names the envoys and reports about 160 companions. The notice leaves the envoys' fate open. Ramusio names Coja as the only surviving envoy. | S-14 #15 and FINAL-ACCESS (Cleaves 1976, p. 181, checked) | III-09, III-12 |
| Maffeo | Widower of Marta. Orlandini’s edition dates the will to 6 February 1310 modern (1309 Venetian). It calls the nuns Juliana and Clara his spiritual daughters. Yule reports an earlier date from a separate 1328 proceeding. | Orlandini 1926 doc. 6 (OCR read), FINAL-ACCESS and S-18 targeted archive intakes; see F-17 | I-02 Note [3] |
| Bellela | Bertuccio Querini was her husband. Her exact death year is unresolved. | Bolognari 2020 cites Gallo’s 1326–27 records. | III-10 Note [15] |
| Peter the Tartar | Marciana Cod. Lat. V, 58 (=2437), no. 33 in Bartoli Langeli’s edition of Marco’s will. | 2019 edition read. The original and live catalogue were uninspected. | III-10 Note [27] |
| Donata | Identified as Badoer, daughter of Vitale, by Gullino; marriage date uncertain; Yule gives death 1333–36. | S-15 external intake | III-10 |
| Niccolò | Second wife probably Fiordelisa (Trevisan?) (Yule's conjecture); illegitimate Stefano and Zannino (Yule: settled); death before end of 1300 | S-15 (the wife) | III-10 |
| Rustichello | Identification with Arthurian compiler supported by manuscript comparison; Cigni favors Meloria captivity, an inference. Lay or clerical status remains unsourced. | S-15 external intake | I-01, III-12 |
| Marco | Birth c. 1254 inferred; capture disputed, Ayas 1296 per Jacopo vs Curzola 1298 per Ramusio; died 8 or 9 Jan 1324. Agnese may be his daughter, not established; dates and parentage of mother unproven. | S-15 #8–12 | I-01, I-02, III-10 |
| Sigatay | Kublai's uncle, d. 1242 (the Book: brother) | settled (Yule's own note) | I-07, I-10 |

**Research intake, run 2 (2026-10-22).** A stricter run (`research/results/CHR-people-2-raw.md`, graded in `CHR-people-2-intake.md`) cited real works; its claims were checked against Yule in `refs/`, two resolved DOIs and the open-access Formentin–Schiavon article. Settled in that intake: Argon's 10 March, Marco's death on 8 or 9 January 1324, Fantina's marriage and Niccolò's illegitimate sons. Its Maffeo and Agnese conclusions are qualified by S-15 above. Three of its claims overstated their sources and were not taken (Dorjé's mother and birth year; Maffeo's will "1300"; Bellela's husband).

**Research intake, run 1 (2026-10-22).** A first search-based run (`research/results/CHR-people-raw.md`, graded in `CHR-people-intake.md`) gave leads only: its sources are Wikipedia and pages that copy Yule, so nothing above is upgraded and no `verify` pointer is removed. What it changed: Chabi's birth year is contested (1216 or 1227), so her age is blank; Maffeo's "daughter Fiordelisa" is a mix-up with Niccolò's second wife, Fiordelisa Trevisan; and new leads are recorded as leads (Bellela's husband, Niccolò's sons, a 1312 dowry document for Donata, a 2022 report of a daughter Agnese). A stricter second prompt for the open rows is in the intake note.

## Plate ages

Generated by `python3 tools/characters.py ages --md` (2026-10-22). Ages are year minus birth year, ±1; "?" means the birth year is unknown, and the card's `house` line gives the apparent age. "(text)" marks people who were in the region but whom the text does not put in the scene.

| Plate | Scene | Src | Year | Figures (age) | Must not show |
|---|---|---|---|---|---|
| I-01 | Marco dictating to Rustichello | GEN | 1298 | Marco (c. 44), Rustichello (?) | — |
| I-02 | The brothers before Kublai (LdM) | PD | 1265–1266 | Cublay (c. 50–51), Niccolò (?), Maffeo (?) | Marco |
| I-02.s | Golden tablet given | GEN | 1266 | Cublay (c. 51), Niccolò (?), Maffeo (?) | — |
| I-03 | 'Sire, 'tis my son' | GEN | 1275 | Cublay (c. 60), Marco (c. 21), Niccolò (?), Maffeo (?) | — |
| I-03.s | Friars turn back at Layas | GEN | 1271 | Marco (c. 17), Niccolò (?), Maffeo (?) | — |
| I-05 | Alaü shuts the Caliph in the treasure tower | GEN | 1258 | Alaü (c. 41), the Caliph (c. 45) | — |
| I-06 | Marco at the Magi tombs of Saba | GEN | 1272 | Marco (c. 18) | — |
| I-07 | Escape from the Caraunas | GEN | 1272 | Marco (c. 18), Niccolò (?), Maffeo (?) | — |
| I-12 | Cane divination before Chinghis's battle | GEN | 1203 | Chinghis (c. 41), Unc Can (?) | — |
| I-13.s | Kublai with a leopard on his crupper | GEN | 1275–1290 | Cublay (c. 60–75) | — |
| II-01 | Kublai on the elephant tower against Nayan | GEN | 1287 | Cublay (c. 72), Nayan (?) | Marco (text), Niccolò (text), Maffeo (text) |
| II-03 | The White Feast | GEN | 1282–1290 | Cublay (c. 67–75) | Chabi |
| II-04 | Khubilai Khan Hunting (Liu Guandao) | PD | 1280 | Cublay (c. 65), Chabi (?) | — |
| II-04.s | Cranes from the elephant litter | GEN | 1280–1290 | Cublay (c. 65–75) | — |
| II-10 | Song envoys surrender the seal to Bayan | GEN | 1276 | Bayan (c. 40) | Facfur, Marco (text), Niccolò (text), Maffeo (text) |
| II-11 | Counterweight trebuchet at Xiangyang | GEN | 1273 | — | Marco, Niccolò, Maffeo |
| II-15 | Aijaruc throws the prince | GEN | 1280–1290 | Aijaruc (c. 20–30), Caidu (c. 45–55) | — |
| III-09 | Kublai gives the tablets; Cocachin and the fleet | GEN | 1291 | Cublay (c. 76), Marco (c. 37), Niccolò (?), Maffeo (?), Cocachin (c. 18), Oulatay (?), Apusca (?), Coja (?) | — |
| III-09.s | Cocachin's farewell | GEN | 1294 | Cocachin (c. 21), Casan (c. 23), Marco (c. 40), Niccolò (?), Maffeo (?) | Argon, Cublay (text) |
| III-10 | Jewels ripped from the seams | GEN | 1295 | Marco (c. 41), Niccolò (?), Maffeo (?) | Donata (text) |
| III-10.s1 | The Cepoy copy | GEN | 1307 | Marco (c. 53), Thibault de Cepoy (?) | — |
| III-10.s2 | Marco's will | GEN | 1324 | Marco (c. 70), Donata (?), Fantina (?), Bellela (?), Moreta (?), Peter the Tartar (?) | — |

Kublai spans **c. 50 (I-02) to c. 76 (III-09)**, not 78: he was 78 when he died in February 1294, after the fleet had sailed.

## Using a card in a plate prompt

1. Run `tools/characters.py cue <id> <year>` and paste its lines into the prompt's `[PERIOD]` and `[AVOID]` slots (style guide § Prompt template).
2. Take the `traditions` line for the plate's tradition into `[STYLE]`. It says how *that* tradition draws this person (a Frank in Ilkhanid painting, a western foreigner in Yuan painting, a French gentleman in the LdM lens).
3. At review, check the card's attributes. They are what keeps a figure recognisable across idioms: Marco is always the youngest of the three Latins before 1291, always has the belt-purse, and carries a paiza only from 1275. Cublay is carried after 1280.
4. `house` lines are our conventions, not facts. A caption never states them.

**S-15 external intake (2026-11-11):** Bellela married Bertuccio Querini (Bolognari 2020, citing Gallo); Moreta's second husband was Tommaso Gradenigo per Gullino. Andrea of San Felice is reported by Ramusio, not established by a surviving document per Tanase. Maffeo's marriage to Marta is reported by Burgio quoting Bolognari–Simion; his alleged daughters need an edition check. Details: `research/results/S-15-external-intake.md`.
