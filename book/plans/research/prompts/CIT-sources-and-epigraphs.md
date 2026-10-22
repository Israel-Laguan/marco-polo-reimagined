# Deep research prompts — sources cited in the Notes, and non-Polo epigraphs

**For:** S-24 pass B (scholar names → citation keys) and HOT.1 (the epigraphs that quote something other than Polo).
**Run** each prompt as a separate deep-research job. The lists are long, and one job per prompt keeps each output complete. Save each output untouched:

| Prompt | Group | Entries | Save to |
|---|---|---|---|
| CIT-A | Modern scholarship (20th–21st c.) | 34 | `plans/research/results/CIT-A-raw.md` |
| CIT-B | Medieval and early-modern sources, Jesuits, classical authors | 98 | `plans/research/results/CIT-B-raw.md` |
| CIT-C | 19th-century travellers, orientalists and sinologists | 79 | `plans/research/results/CIT-C-raw.md` |
| CIT-D | Sources for the non-Polo epigraphs | 4 questions | `plans/research/results/CIT-D-raw.md` |

**Intake** (in this repo, following the trust rules in `plans/research/README.md`):
- CIT-A to CIT-C become entries in `plans/registry/bibliography.bib`, plus the name → key map that `tools/cite_convert.py --pass B` reads. Each ambiguous name (Frances Wood vs John Wood, the two Andersons, "Hall") is then settled Note by Note from its context.
- Most 19th-century names reach us only through Yule's notes. Where a Note relies on Yule's report of a writer we have not read, the citation says so ("John Wood 1841, in YC 1.32 n."). The intake checks which case applies by searching `refs/`.
- CIT-D feeds HOT.1. The 15 misquoted Polo epigraphs are fixed locally from `refs/` and need no research.
- **Overlap:** S-12 Task A asks for a subset of CIT-A. If these prompts run first, skip S-12 Task A. S-12 Tasks B–D (editions, translations, core reading) still apply.

The lists below were generated from the Notes on 2026-10-22: each name, the sections that cite it, and one context snippet. Regenerate them if the Notes change before you run the prompts.

## CIT-A — Modern scholarship

```text
I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, 3rd edition revised by Henri Cordier (London: John Murray, 1903), with Cordier's Notes and Addenda (1920). The endnotes are being converted to Chicago author-date style (18th ed.), but they currently name their authorities without titles or dates. Below are the authorities in one group. Each comes with the book sections where it is cited (I-05 = Vol. I ch. 5; II-F1 = Vol. II front matter; III-B1 = Vol. III back matter) and one snippet from my notes showing how it is used.

For EACH entry, identify the specific work meant in that context and return:
1. Who: full name, dates, one-line identification.
2. Work(s): the work the context points to. If the name could mean several people or works, list each, say which context matches which, and flag the row AMBIGUOUS. If the entry is not a source at all (a place, a people or a character in the story), say NOT A SOURCE.
3. Citation: the first edition (author, full title, place, publisher, year, number of volumes). For a work in another language, also give the standard English translation, if one exists.
4. Free copy: a stable URL to a digitised copy (Internet Archive, HathiTrust, Gallica, Project Gutenberg, Google Books, BHL, a publisher's open-access page), or "none found".
5. BibTeX: one biblatex entry per work. Key = lower-case surname + year of the edition cited + first significant title word (e.g. vogel2013marco). For an old book, cite the print edition and put the digitisation in an addendum field ("Digitised by Internet Archive, <URL>"). Never date an old book by its scan or upload date.
6. Confidence: high / medium / low.

Group notes: these are modern scholars. Give the edition current today, and say if a later edition revised the relevant material. "Frances Wood" is the 1995 sceptic; the explorer John Wood is in another group. "Morgan" and "Jackson" are most likely David Morgan and Peter Jackson, both as monograph authors and as translators of Rubruck (Hakluyt Society, 1990): give both kinds of work. "Thackston", "Boyle" and "Gibb" are translators: give the translated work (Rashid al-Din; Juvaini; Ibn Battuta). "Hall" is probably Kenneth R. Hall (early Southeast Asian maritime history).

GROUP A — MODERN SCHOLARSHIP (34 entries):
- Larner — I-01, I-11, I-B1, I-F1, II-01, II-02 … — “…Rustichello collaboration — traditional; degree of literary shaping contested (Larner; modern textual scholarship).…”
- Vogel — I-07, I-11, II-02, II-05, II-07, II-11 … — “…es Wood, Did Marco Polo Go to China?, vs replies (de Rachewiltz; Haw; Larner; Vogel). Planted here; fuller essay in Vol. III.…”
- Haw — I-02, I-03, I-07, I-09, I-11, I-13 … — “…sence — Frances Wood, Did Marco Polo Go to China?, vs replies (de Rachewiltz; Haw; Larner; Vogel). Planted here; fuller essay in Vol. III.…”
- Rossabi — I-13, I-F1, II-01, II-02, II-03, II-04 … — “…shell; Shangdu archaeology / UNESCO; Yuan Shi; Gaubil; Rashid; Odoric; Rubruck; Rossabi, Khubilai Khan; Steinhardt on Yuan capitals; Haw; Atwood.…”
- Moule — I-01, I-B1, II-13, II-B1, III-02, III-10 … — “…ace 10-mi demesne; 20 gold halls; 1,000 chambers — palace on Phoenix Hill real (Moule); dimensions/marvel counts exaggerated. 1,600,000 houses (160 tomans) — formu…”
- Moule–Pelliot — I-01, I-B1, II-B1, III-02, III-10, III-11 … — “…Manuscript family typology — Benedetto; Moule–Pelliot; Yule–Cordier introductions. Working base: Yule–Cordier, Geographic Old French…”
- Pelliot — I-01, I-B1, II-B1, III-02, III-10, III-11 … — “…rner; Ramusio preface; Jesuit China correspondence (Ricci orbit); Yule–Cordier; Pelliot Notes; Moule–Pelliot; Benedetto; Wood; de Rachewiltz; Haw; Vogel; Critchley;…”
- Benedetto — I-01, I-B1, III-10, III-11, III-12 — “…e formula (Seigneurs Empereurs et Princes…); consensus of Paulin Paris, Yule, Benedetto, later editors. Meloria captivity since 1284: fair conjecture only, not prove…”
- Allsen — I-F1, II-03, II-04, II-F1, III-12 — “…ctions, Larner’s reception history, and Mongol-empire surveys (Morgan; Rossabi; Allsen).…”
- Critchley — III-10, III-11, III-12 — “…ogy and name philology. Larner (Marco Polo and the Discovery of the World); Critchley; Rossabi and Yuan studies — readership, composition, court context.…”
- Needham — II-05, III-01, III-12 — “…Gaubil; De Mailla; Franke; Vogel (Marco Polo was in China) on money and salt; Needham (coal; astronomy—selective); Haw; Wood vs critics; Rashīd al-Dīn (Sing; coal)…”
- Steinhardt — I-13, II-02, III-12 — “…is not proof of absence; weighed in III-12. Comparative: Yuan Dadu archaeology; Steinhardt; Odoric; Ibn Baṭṭūṭa on Daidu (later); Xijin zhi; Rossabi, Khubilai Khan; B…”
- Frances Wood — I-03, I-10, I-11, I-B1, II-02, II-05 … — “…rridor. Textual silence real. Whether silence undermines presence — Frances Wood, Did Marco Polo Go to China?, vs replies (de Rachewiltz; Haw; Larner; Vogel).…”
- de Rachewiltz — I-02, I-11, I-B1, I-F1, II-02, II-11 … — “…? Great Wall silence — major modern debate (Wood vs Haw, Larner, de Rachewiltz, et al.); seeded here, argued later.…”
- Olschki — III-12 — “…): Wood; de Rachewiltz; Haw; Vogel; Larner; Pelliot Notes; Moule & Pelliot; Olschki; Critchley; Rossabi; Allsen; Jackson; Rubruck; Ibn Battuta; Odoric; Rashid al-D…”
- Franke — II-05 — “…II-6). Comparative: Yuan shi (Ahmad; granaries; calendar); Gaubil; De Mailla; Franke; Vogel (Marco Polo was in China) on money and salt; Needham (coal; astronomy—…”
- Dutschke — I-01, III-12 — “…9 French original. Early French recoverable in types (Benedetto; Moule–Pelliot; Dutschke on MS tradition); “the” autograph dictation not extant. This retelling follows…”
- Morgan — I-F1, III-12 — “…e–Cordier introductions, Larner’s reception history, and Mongol-empire surveys (Morgan; Rossabi; Allsen).…”
- Jackson — III-12 — “…Larner; Pelliot Notes; Moule & Pelliot; Olschki; Critchley; Rossabi; Allsen; Jackson; Rubruck; Ibn Battuta; Odoric; Rashid al-Din; Yule–Cordier; Needham (selective)…”
- Atwood — I-13 — “…d; Odoric; Rubruck; Rossabi, Khubilai Khan; Steinhardt on Yuan capitals; Haw; Atwood.…”
- Chaudhuri — III-F1 — “…Monsoon sailing constraints — standard Indian Ocean history (Hall; Chaudhuri; maritime archaeology overviews); Polo’s Sumatran winter wait fits the pattern.…”
- Hall — III-02, III-F1 — “…Comparative: Yuan–Champa war records; Gaubil; Wolters; Hall; Aymonier on Chams. Polo’s neat vassalage vs bruising frontier (prince’s resist…”
- Wolters — III-02 — “…Comparative: Yuan–Champa war records; Gaubil; Wolters; Hall; Aymonier on Chams. Polo’s neat vassalage vs bruising frontier (prince’s…”
- Schottenhammer — II-14, III-12 — “…superseded by Yule–Cordier, Bretschneider, Yuan shi-po, Rashīd, archaeology (Schottenhammer; Chen Dasheng). / one of two / the greatest world havens; 100× Alexandria p…”
- Chen Dasheng — II-14, III-12 — “…ule–Cordier, Bretschneider, Yuan shi-po, Rashīd, archaeology (Schottenhammer; Chen Dasheng). / one of two / the greatest world havens; 100× Alexandria pepper — order-…”
- Daftary — I-08 — “…l fact. Crusader stereotype vs Ismā‘īlī history (Juvainī; Rashīd al-Dīn; Farhad Daftary).…”
- Hsiao Ch’i-ch’ing — II-01 — “…omparative: Yuan Shi; Rashīd al-Dīn on Kaidu front; Rossabi, Khubilai Khan; Hsiao Ch’i-ch’ing on Yuan military institutions; Yule App. on Nayan; Larner on romance battle dic…”
- Elverskog — II-03 — “…-Dīn; Wassáf; Yuan ceremonial codes / Yuan shi; Palladius; Gaubil; De Mailla; Elverskog on Mongol ritual; Allsen; Rossabi; Yule on vernique / camut; Shah Rukh emba…”
- Gernet — II-13 — “…y block; lake parties and soft Sung court in Chinese sources (Mengliang lu; Gernet). / pork omitted from market meats — silence vs Odoric swine and Chinese st…”
- Huntingford — III-07 — “…Fra Mauro; De Barros; Barbosa; Bruce / Salt / Rüppell Abyssinian chronologies; Huntingford; Chinese Ming notices of Mu-ku-tu-su / Pu-la-wa.…”
- Subrahmanyam — III-05 — “…: Montecorvino; Marignolli; Odoric; Conti; Barbosa; Assemani; Caldwell; Nelson; Subrahmanyam; Syrian Christian / Thomacide traditions.…”
- Thackston — III-09, III-12 — “…Comparative: YC Prol. 17–18 and Intro. §§21–22; Rashid al-Din (Quatremère; Thackston/Boyle); Hammer Geschichte der Ilchane; Wassaf (Elliot); Rossabi on Kublai; Ha…”
- Boyle — III-09, III-12 — “…tive: YC Prol. 17–18 and Intro. §§21–22; Rashid al-Din (Quatremère; Thackston/Boyle); Hammer Geschichte der Ilchane; Wassaf (Elliot); Rossabi on Kublai; Haw chro…”
- Gibb — III-12 — “…rative method. Rubruck (Jackson/Morgan edition tradition); Odoric; Ibn Baṭṭūṭa (Gibb); Rashid al-Din (Thackston/Boyle); Juvaini / Secret History for Mongol deep b…”

OUTPUT FORMAT (required). (1) One table with columns: # · name as I cite it · who · work meant (and which context) · first edition · English translation (if any) · free copy URL · confidence · flag (AMBIGUOUS / NOT A SOURCE / blank). (2) One BibTeX block with every entry. (3) A list of the names you could not resolve, and why. Rules: do not invent titles, editions, dates, URLs or DOIs. If you cannot confirm an edition, say "unconfirmed". Prefer library catalogues (WorldCat, national libraries), publisher pages and scholarly bibliographies over general websites. Do not stop early: cover every entry.
```

## CIT-B — Medieval and early-modern sources

```text
I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, 3rd edition revised by Henri Cordier (London: John Murray, 1903), with Cordier's Notes and Addenda (1920). The endnotes are being converted to Chicago author-date style (18th ed.), but they currently name their authorities without titles or dates. Below are the authorities in one group. Each comes with the book sections where it is cited (I-05 = Vol. I ch. 5; II-F1 = Vol. II front matter; III-B1 = Vol. III back matter) and one snippet from my notes showing how it is used.

For EACH entry, identify the specific work meant in that context and return:
1. Who: full name, dates, one-line identification.
2. Work(s): the work the context points to. If the name could mean several people or works, list each, say which context matches which, and flag the row AMBIGUOUS. If the entry is not a source at all (a place, a people or a character in the story), say NOT A SOURCE.
3. Citation: the first edition (author, full title, place, publisher, year, number of volumes). For a work in another language, also give the standard English translation, if one exists.
4. Free copy: a stable URL to a digitised copy (Internet Archive, HathiTrust, Gallica, Project Gutenberg, Google Books, BHL, a publisher's open-access page), or "none found".
5. BibTeX: one biblatex entry per work. Key = lower-case surname + year of the edition cited + first significant title word (e.g. vogel2013marco). For an old book, cite the print edition and put the digitisation in an addendum field ("Digitised by Internet Archive, <URL>"). Never date an old book by its scan or upload date.
6. Confidence: high / medium / low.

Group notes: these are primary sources and pre-1800 writers. For each, also give: (a) the standard critical edition of the original; (b) the scholarly English translation a historian cites today; (c) any public-domain English translation with a free copy; (d) the locator system scholars use to cite it without page numbers (e.g. book.chapter for Herodotus; Defrémery–Sanguinetti volume.page for Ibn Battuta; chapter numbers for Rubruck). "Relations" means the Arabic Akhbar al-Sin wa'l-Hind ("the Arab Relations"). "Al-Ramni" may be a place (Lambri) rather than an author; say which. For the 17th–18th-century Jesuit and Enlightenment works (Magaillans, Martini, Duhalde, Amyot, Lecomte, Gaubil, De Mailla), give the original edition and the contemporary English translation if there was one.

GROUP B — MEDIEVAL AND EARLY-MODERN SOURCES (98 entries):
- Odoric — I-06, I-08, I-12, I-13, II-02, II-03 … — “…ial primacy; Viglioni will 1264; later Genoese/Venetian factories; Ibn Baṭṭūṭa, Odoric, Rashid al-Din. / Tauris placed in “Yrac” — as Ilkhanid capital metonym (…”
- Rashid — I-02, I-03, I-05, I-06, I-12, I-13 … — “…gfu wound with Möngke’s death at Hochau (Caagiu). Comparative: Sanang Sechen; Rashid; Chinese annals.…”
- Ibn Baṭṭūṭa — I-05, I-06, I-07, I-09, II-02, II-03 … — “…, nac, cramoisy; animal-figure gold brocades; baldachin etymology. Pegolotti, Ibn Baṭṭūṭa, Rubruck, Yuan nakh/nasīj; baldachino from Baldac. Animal-pattern gold broc…”
- Rubruck — I-05, I-12, I-13, I-F1, II-01, II-03 … — “…oisy; animal-figure gold brocades; baldachin etymology. Pegolotti, Ibn Baṭṭūṭa, Rubruck, Yuan nakh/nasīj; baldachino from Baldac. Animal-pattern gold brocade is a…”
- Carpini — I-12, I-F1, II-01, II-03 — “…t, horse/dog/Pharaoh’s rats; chaste wives. Classic steppe ethnography (Rubruck, Carpini, Pallas). YC 1.52.…”
- Hayton — I-02, I-04, I-05, II-03, II-05, II-15 … — “…~ / “Bocara the best city in all Persia.” Medieval Persian cultural sphere (Hayton; Vámbéry’s note on pre-Mongol usage). if read as modern political geography.…”
- Jordanus — III-01, III-04, III-05, III-06, III-09 — “…king; merchant cabins. Chinese junk construction broadly attested (Ibn Battuta; Jordanus; Conti).…”
- Ricold — I-04, I-05, II-01 — “…Oil fountain: abundant naphtha for fuel and camel mange. Baku wells; Ricold, Barbaro, later production figures.…”
- Pegolotti — I-03, I-04, I-05, I-11, II-05, II-14 … — “…/ Camul as autopsy vs elder Polos or hearsay (Pegolotti, Marignolli, Shah Rukh, Goes routes pass the oasis). Nestorian bishopric attest…”
- Marignolli — I-11, II-06, II-13, III-04, III-05 — “…/ Camul as autopsy vs elder Polos or hearsay (Pegolotti, Marignolli, Shah Rukh, Goes routes pass the oasis). Nestorian bishopric attested 1266.…”
- Wassaf — III-05, III-06, III-09 — “…Comparative: Wassaf; Rashid; Ibn Battuta; Tennent; pearl-fishery histories (Stewart; Pridham). Yule…”
- Makrizi — I-03, I-05, II-03, III-08 — “…with 1275 burning of Ayas/Sis; if read as autumn 1271 Syrian–frontier alarm (Makrizi). Baybars Bundukdari r. 1259/60–1277; “Babylon” = Cairo in Latin usage.…”
- Edrisi — I-07, III-06, III-08 — “…ested (Shahr-i-Bābak / Pārīz; Nīrīz / Parpa); ondanique well argued (Ramusio; Edrisi). “Best falcons in the world” as absolute superlative unverified; regional l…”
- Idrīsī — III-07 — “…and App. on Rukh; Ibn Baṭṭūṭa (Makdashau, East Africa, Aden); Masʿūdī; Kazwini; Idrīsī; Cosmas (Socotra); Conti; Fra Mauro; De Barros; Barbosa; Bruce / Salt / Rüppell…”
- Kazwini — III-03, III-06, III-07 — “…/ Tailed men in Lambri mountains. Marvel; Archipelago commonplace (Kazwini; Marsden Orang Gugu; Ctesias; Ptolemy Satyrs); soft ethnographic core (interi…”
- Masʿūdī — III-03, III-05, III-07 — “…suri best, gold-weight price. Arab Fansūrī camphor from 9th c. (Relations; Masʿūdī; Avicenna) — trade-fact. Gazetteer: reported_only.…”
- Mas’udi — I-11 — “…ong debated (Richthofen–Hedin–Kozlov). Universal desert-goblin folklore (Pliny, Mas’udi, Ibn Battuta, Conti).…”
- al-Bīrūnī — III-06 — “…–xxx; Rashid; Wassaf; Ibn Battuta; Abulfeda; Barbosa; Conti; Caldwell on Kāyal; al-Bīrūnī; Ma Huan (later Ming); Vogel trade notes.…”
- Abulfeda — III-05, III-06 — “…abar = Coromandel / Maʿbar coast; India the Greater. Standard Arabic geography (Abulfeda; Wassaf: “key of Hind”). ~60 miles west from Seilan — orientation compressed;…”
- Abū’l-Fidā — III-03 — “…Less = Sumatra; northern kingdoms chain after Pentam. Arab Jawa for Sumatra (Abū’l-Fidā; Ibn Battuta’s Jáwah). / circuit ≥2,000 miles — order of magnitude; round…”
- Moḳaddasi — I-08 — “…steel, ondanique, steel mirrors. Place and metalworking district attested (Moḳaddasi; Yāḳūt; Abbott); “large town” and mirror superlatives inflated. Tutia /…”
- Yāḳūt — I-08 — “…danique, steel mirrors. Place and metalworking district attested (Moḳaddasi; Yāḳūt; Abbott); “large town” and mirror superlatives inflated. Tutia / spodium…”
- Mustawfi — I-06 — “…tawfi’s parallel character sketch. Gardens and excellent fruit around Tauris (Mustawfi and later travellers). Twelve days to Persia — Ramusio road-stage.…”
- Juvaini — III-12 — “…dition tradition); Odoric; Ibn Baṭṭūṭa (Gibb); Rashid al-Din (Thackston/Boyle); Juvaini / Secret History for Mongol deep background where Book I digressions scramble…”
- Juvainī — I-08 — “…-paradise taken as institutional fact. Crusader stereotype vs Ismā‘īlī history (Juvainī; Rashīd al-Dīn; Farhad Daftary).…”
- Ibn Muhalhal — I-11 — “…petition and “keep your shame.” Custom-type paralleled (Hung Hao on Uighúrs; Ibn Muhalhal; Chukchi/Koryak; Polo’s own E. Tibet notice). Mangu anecdote. Moralising La…”
- Abu Zaid — III-05 — “…ausible. / Trusty Lieges burn with the king — companions-in-death attested (Abu Zaid; Masʿūdī; Barbosa; Malabar Amuki). Female suttee praised — well attested in…”
- Al-Ramni — III-03 — “…tive: Junghuhn; Anderson; Conti Batech; Barbosa; De Barros; Arab Relations (Al-Ramni).…”
- Relations — II-10, III-03, III-04 — “…mation common enough (Ku Yen-wu; de Groot; Mayers); burial also attested (Arab Relations; Conti).…”
- Conti — I-11, II-10, III-01, III-02, III-03, III-04 … — “…n–Hedin–Kozlov). Universal desert-goblin folklore (Pliny, Mas’udi, Ibn Battuta, Conti).…”
- Barbosa — II-08, III-02, III-03, III-05, III-06, III-07 … — “…f Bengal. / Eunuch and slave export; cotton and spice trade (Āʾīn-i Akbarī; Barbosa). / Oxen “tall as elephants” — simile; very tall Indian cattle / Arna heigh…”
- De Barros — III-03, III-07 — “…lec likely_visited. Comparative: Junghuhn; Anderson; Conti Batech; Barbosa; De Barros; Arab Relations (Al-Ramni).…”
- Della Valle — I-06, II-01, III-08 — “…racen” drinking. Persian wine culture and dūshāb/must practices (Tavernier, Della Valle, classical lore); as universal legal gloss. Ramusian aside.…”
- Teixeira — I-08, III-08 — “…notice; zinc-oxide / collyrium tradition well paralleled (Galen on pompholyx; Teixeira; Gulf trade of Kermān tutia). One of Polo’s stronger technological passages.…”
- Tavernier — I-06 — “…llowing “Saracen” drinking. Persian wine culture and dūshāb/must practices (Tavernier, Della Valle, classical lore); as universal legal gloss. Ramusian aside.…”
- Figueroa — III-08 — “…Wind-catchers corroborated (Della Valle / Figueroa / Fryer; Oman, Kerman, Baghdad, Mekran, Sind; Cairo analogue). Neat ethnographi…”
- Fryer — III-08 — “…Wind-catchers corroborated (Della Valle / Figueroa / Fryer; Oman, Kerman, Baghdad, Mekran, Sind; Cairo analogue). Neat ethnographic hit of…”
- Clavijo — I-09 — “…sian destruction and long ruin amply attested (Ibn Baṭṭūṭa still ruined ~1330s; Clavijo; Burnes/Ferrier). / Alexander married Darius’s daughter at Balkh: local/r…”
- Sidi Ali — I-09 — “…for true lion; recurrent medieval and early-modern testimony (Rashīd al-Dīn; Sidi Ali; Moorcroft; Wood).…”
- Shah Rukh — I-11, II-03, II-05 — “…/ Camul as autopsy vs elder Polos or hearsay (Pegolotti, Marignolli, Shah Rukh, Goes routes pass the oasis). Nestorian bishopric attested 1266.…”
- Hiuen Tsang — I-10, I-11, II-05, III-04, III-07 — “…on Ramusian “miracolo” not in old texts. Chinese pilgrims (Hwui Seng, Sung Yun, Hiuen Tsang Pomilo) on altitude and lake; Bām-i-Duniah.…”
- Fa-hian — I-11 — “…ums and musical sounds. Motif in Chinese and pilgrim sources for this desert (Fa-hian, Hiuen Tsang, Ma Twan-lin). As literal demonology. YC 1.39.…”
- Hwui Seng — I-10 — “…boldt’s doubt rested on Ramusian “miracolo” not in old texts. Chinese pilgrims (Hwui Seng, Sung Yun, Hiuen Tsang Pomilo) on altitude and lake; Bām-i-Duniah.…”
- Sung Yun — I-10 — “…bt rested on Ramusian “miracolo” not in old texts. Chinese pilgrims (Hwui Seng, Sung Yun, Hiuen Tsang Pomilo) on altitude and lake; Bām-i-Duniah.…”
- Ma Huan — III-02, III-06 — “…ic for III-9. Comparative: Yule–Cordier III.v–viii; Groeneveldt; Odoric; Conti; Ma Huan / Daooyi zhilue; Ibn Battuta (later Samudra); Wolters; Hall; Moule–Pelliot.…”
- Ma Twan-lin — I-11 — “…. Motif in Chinese and pilgrim sources for this desert (Fa-hian, Hiuen Tsang, Ma Twan-lin). As literal demonology. YC 1.39.…”
- Chang Te-hui — I-13 — “…stige and Oirad privilege tradition; mare’s-milk libations (Rubruck, Palladius, Chang Te-hui). Headcount; Polo’s date vs May/7th-moon parallels. YC 1.61.…”
- Altan Tobchi — I-13 — “…Cane/Palm Hall / tent architecture at Shangtu (Palladius Tsung tien; Rashid; Altan Tobchi). Ramusian ornamental fullness. YC 1.61 (Ramusio fuller on columns and r…”
- Sanang Sechen — I-12 — “…use 1212 Taitongfu wound with Möngke’s death at Hochau (Caagiu). Comparative: Sanang Sechen; Rashid; Chinese annals.…”
- Secret History — I-12, III-12 — “…Unc Can = Toghrul Wang Khan of the Kerait under Prester John romance dress. Secret History; Rashid al-Din; Yule on Prester John.…”
- Yuan Shi — I-13, II-01, II-11, II-15 — “…istory, not developed here. Comparative: Bushell; Shangdu archaeology / UNESCO; Yuan Shi; Gaubil; Rashid; Odoric; Rubruck; Rossabi, Khubilai Khan; Steinhardt on Yuan…”
- Yuan shi — II-02, II-03, II-04, II-05, II-08, II-09 … — “…Chinggis (Yule). Death date: Yule gives "12th moon of 1284–1285, aged 43"; the Yuan shi dates it to the 12th month of Zhiyuan 22, i.e. January 1286. To verify (S-06…”
- Ch’ue keng lu — II-03 — “…yourt ropes). / Ushers for foreigners; giant door-wardens with staves: Ch’ue keng lu athletes with clubs and jade axes (Palladius); “giants” colour.…”
- Mengliang lu — II-13 — “…as Ramusio-only block; lake parties and soft Sung court in Chinese sources (Mengliang lu; Gernet). / pork omitted from market meats — silence vs Odoric swine and C…”
- Tsung tien — I-13 — “…races, demountable. Cane/Palm Hall / tent architecture at Shangtu (Palladius Tsung tien; Rashid; Altan Tobchi). Ramusian ornamental fullness. YC 1.61 (Ramusio…”
- Ku Yen-wu — II-10 — “…ist/clerical and Jiangnan practice as national custom. Cremation common enough (Ku Yen-wu; de Groot; Mayers); burial also attested (Arab Relations; Conti).…”
- Ain-i-Akbari — II-01 — “…nsport in Gaubil; naqqāra as pan-Asiatic signal-drum (Joinville; Della Valle; Ain-i-Akbari). Four-elephant tower as Polo spectacle; mass chorus unique to Polo among Yul…”
- Firishta — III-05 — “…dia. / Heirs leave father’s treasure untouched — accumulation real (Wassaf; Firishta; Malik Kāfūr spoils); absolute taboo overstated. Dispute: suttee / companions…”
- Malay Chronicle — III-03 — “…ak; coastal Islam from Saracen merchants. Strong toponym and conversion timing (Malay Chronicle; Rashid Barlak; Diamond Point). / Hill-people cannibalism inland — Batta…”
- Jacopo — I-01, I-F1, III-10, III-12 — “…Nickname Milione / Marchus Paulo Milioni — Great Council 10 Apr 1305; Jacopo; house-name Corte del Milione. Ramusio: from Marco’s habitual “millions” of Kaa…”
- Pipino — I-01, I-02, III-10, III-11, III-12 — “…ip wide but not ubiquitous (Larner caution) — named 14th-c. refs finite (Cepoy, Pipino, Jacopo, Villani, d’Abano, John of Ypres); MS geography real; print-age inflati…”
- d’Abano — III-10 — “…s (Larner caution) — named 14th-c. refs finite (Cepoy, Pipino, Jacopo, Villani, d’Abano, John of Ypres); MS geography real; print-age inflation to be resisted.…”
- Villani — III-10 — “…ubiquitous (Larner caution) — named 14th-c. refs finite (Cepoy, Pipino, Jacopo, Villani, d’Abano, John of Ypres); MS geography real; print-age inflation to be resisted…”
- Joinville — II-01, III-08 — “…nakkara. Crupper transport in Gaubil; naqqāra as pan-Asiatic signal-drum (Joinville; Della Valle; Ain-i-Akbari). Four-elephant tower as Polo spectacle; mass chor…”
- Pachymeres — I-05 — “…r / forced to “eat” gold. Widely circulated Christian exemplum (Hayton, Ricold, Pachymeres; Sanuto’s molten-gold variant is Crassus-transfer). Muslim sources share the ta…”
- Montecorvino — III-05 — “…o. / Wild-ox hair as battle amulet. Soft close toward Mutfili. Comparative: Montecorvino; Marignolli; Odoric; Conti; Barbosa; Assemani; Caldwell; Nelson; Subrahmanyam;…”
- Epiphanius — III-06 — “…esh–eagle–serpent valley gathering — ancient migratory legend, not mining fact (Epiphanius; Edrisi; Kazwini; Sindbad; Conti). / Diamonds unique to Mutfili; flower to…”
- Cosmas — III-04, III-07 — “…/ Scotra = Socotra; Christian community (Cosmas; Arab geographers; long Christian survival). / Ramusian whale-hunt with bar…”
- Herodotus — II-07, II-08, III-03 — “…/ Premarital hospitality + lover’s tokens (≥20). Wide parallels (Herodotus; Martini; Garnier; Westermarck); local attribution may blend tribes; Book’s jes…”
- Ctesias — III-03, III-04 — “…mbri mountains. Marvel; Archipelago commonplace (Kazwini; Marsden Orang Gugu; Ctesias; Ptolemy Satyrs); soft ethnographic core (interior peoples; costume) under wond…”
- Pliny — I-09, I-11 — “…province” inflated. / Porcupines project quills at dogs: projection myth (Pliny); huddling defensive behaviour real.…”
- Galen — I-08 — “…ing: strong technical notice; zinc-oxide / collyrium tradition well paralleled (Galen on pompholyx; Teixeira; Gulf trade of Kermān tutia). One of Polo’s stronger t…”
- Avicenna — III-03 — “…t, gold-weight price. Arab Fansūrī camphor from 9th c. (Relations; Masʿūdī; Avicenna) — trade-fact. Gazetteer: reported_only.…”
- Pseudo-Callisthenes — I-08 — “…ker. Arbre Sec names drawn from Alexander romance / Christian Dry Tree lore (Pseudo-Callisthenes; Chanson d’Alixandre; Maundevile): romance topography pasted onto eastern Ir…”
- Maundevile — I-08 — “…omance / Christian Dry Tree lore (Pseudo-Callisthenes; Chanson d’Alixandre; Maundevile): romance topography pasted onto eastern Iran.…”
- Golden Legend — III-04 — “…Barlaam & Josaphat parallel — Christianised Buddha romance (John of Damascus; Golden Legend); annotate, don’t flatten: Polo’s tale is Indian/Buddhist report filtered by La…”
- Jerome — III-05 — “…? Apostolic preaching/death in S. India as historical fact — ancient tradition (Jerome; Acts of Thomas / Gondophares echo); not settled by Polo. / Wild-ox hair as…”
- Benjamin of Tudela — III-07 — “…“Middle India” = European/Oriental-Christian confusion of Ethiopia with India (Benjamin of Tudela; Cosmas’ “interior Indians”), not standard Arabic usage. Six kings, three Chr…”
- Ptolemy — III-03 — “…tains. Marvel; Archipelago commonplace (Kazwini; Marsden Orang Gugu; Ctesias; Ptolemy Satyrs); soft ethnographic core (interior peoples; costume) under wonder-label.…”
- Periplus — III-06, III-F2 — “…ble. Spider-web buckrams of Mutfili — long muslin fame (Masulipatam / Masalia Periplus).…”
- Marāṣid — III-08 — “…opoly (buy 10 / sell 60 livres gold per cwt) — Sheḥr–Dhafār monopoly pattern (Marāṣid); exact ratio. Dates; little rice (imported); tunny cheap; sugar/rice/date wi…”
- Martini — II-07, II-13 — “…/ Premarital hospitality + lover’s tokens (≥20). Wide parallels (Herodotus; Martini; Garnier; Westermarck); local attribution may blend tribes; Book’s jest tone.…”
- Magaillans — II-02, II-04, II-06, II-09 — “…le-storey audience hall. Glazed, coloured roof finish independently attested (Magaillans). Ramusio-only: the private treasury and the women's apartments on the interi…”
- Duhalde — II-10 — “…e grain. Cangzhou–Yen-shan salt district; process paralleled near Yangzi mouth (Duhalde; Lettres Édifiantes).…”
- Amyot — II-05, III-01 — “…s. Spiced rice-wine, strong and clear. Chinese mi jiu / shao jiu culture (Amyot; Rubruck Auxerre comparison; Odoric bigni).…”
- Lecomte — II-06 — “…ver the Sanggan–Yongding. Scale, lion parapet, marble balustrade (Magaillans; Lecomte; Bretschneider). Arch-count: Polo’s 24 vs historical ~11–13; possible confusi…”
- Gaubil — I-12, I-13, II-01, II-02, II-03, II-05 … — “…sert; wild asses (Asinus hemionus). Etsina corridor; Chinggis took it 1226 (Gaubil). Schematic “forty.” YC 1.45; gazetteer likely_visited.…”
- De Mailla — II-02, II-03, II-05, II-10, II-11, III-01 — “…oted for beauty; gave more wives to the Chinggisids than any other tribe (Yule; De Mailla). / Yearly levy of about 100 maidens and the six-by-six, three-day roster:…”
- Pallas — I-11, I-12 — “…sheep dedication and feast. Kalmak/Shaman–Buddhist “Heaven’s Ram” parallels (Pallas). YC 1.40.…”
- Valentyn — III-04 — “…Dispute: dimensions of Ceylon exaggerated. Comparative: Hiuen Tsang; Valentyn; Tennent.…”
- Assemani — III-05 — “…toward Mutfili. Comparative: Montecorvino; Marignolli; Odoric; Conti; Barbosa; Assemani; Caldwell; Nelson; Subrahmanyam; Syrian Christian / Thomacide traditions.…”
- Ysbrandt Ides — II-03 — “…. Court jongleurs / Chinese feast entertainers widely noted (Chaucer; Odoric; Ysbrandt Ides).…”
- Cardan — I-11 — “…hed napkins; Rome napkin for Sudarium. Asbestos fabric process sound (Browne; Cardan). Province name/location (Chi-kin / Kemkemjút / Kobdo). YC 1.42. G. Text…”
- Chaucer — II-03 — “…glers and players. Court jongleurs / Chinese feast entertainers widely noted (Chaucer; Odoric; Ysbrandt Ides).…”
- Book of Prophecies — III-11 — “…n scholarship. Margins and related notes feed western-Ocean expectancy and the Book of Prophecies orbit. Selective amplification: gold of Chipangu, Cathay, Great Kaan, spices,…”
- Ricci — III-11 — “…s / Book of Prophecies; Larner; Ramusio preface; Jesuit China correspondence (Ricci orbit); Yule–Cordier; Pelliot Notes; Moule–Pelliot; Benedetto; Wood; de Rache…”
- Fra Mauro — III-07, III-11 — “…Mahābhārata Amazons; Hiuen Tsang Kingdom of Western Women; Conti near Socotra; Fra Mauro Mangla/Nebila; Portuguese still attached the tale to Socotra. Kuria Muria /…”
- Bruce — III-07 — “…Aden confounded with Adel (Danākil / Zailaʿ). Resemblance to Amda Seyon’s wars (Bruce ~1312–16) too late for ~1298 dictation if Bruce holds; Salt/Pauthier shove date…”

OUTPUT FORMAT (required). (1) One table with columns: # · name as I cite it · who · work meant (and which context) · first edition · English translation (if any) · free copy URL · confidence · flag (AMBIGUOUS / NOT A SOURCE / blank). (2) One BibTeX block with every entry. (3) A list of the names you could not resolve, and why. Rules: do not invent titles, editions, dates, URLs or DOIs. If you cannot confirm an edition, say "unconfirmed". Prefer library catalogues (WorldCat, national libraries), publisher pages and scholarly bibliographies over general websites. Do not stop early: cover every entry.
```

## CIT-C — 19th-century travellers, orientalists and sinologists

```text
I am preparing a new English retelling of Marco Polo's book for print. The base text is Henry Yule's translation, 3rd edition revised by Henri Cordier (London: John Murray, 1903), with Cordier's Notes and Addenda (1920). The endnotes are being converted to Chicago author-date style (18th ed.), but they currently name their authorities without titles or dates. Below are the authorities in one group. Each comes with the book sections where it is cited (I-05 = Vol. I ch. 5; II-F1 = Vol. II front matter; III-B1 = Vol. III back matter) and one snippet from my notes showing how it is used.

For EACH entry, identify the specific work meant in that context and return:
1. Who: full name, dates, one-line identification.
2. Work(s): the work the context points to. If the name could mean several people or works, list each, say which context matches which, and flag the row AMBIGUOUS. If the entry is not a source at all (a place, a people or a character in the story), say NOT A SOURCE.
3. Citation: the first edition (author, full title, place, publisher, year, number of volumes). For a work in another language, also give the standard English translation, if one exists.
4. Free copy: a stable URL to a digitised copy (Internet Archive, HathiTrust, Gallica, Project Gutenberg, Google Books, BHL, a publisher's open-access page), or "none found".
5. BibTeX: one biblatex entry per work. Key = lower-case surname + year of the edition cited + first significant title word (e.g. vogel2013marco). For an old book, cite the print edition and put the digitisation in an addendum field ("Digitised by Internet Archive, <URL>"). Never date an old book by its scan or upload date.
6. Confidence: high / medium / low.

Group notes: most of these are quoted in Yule–Cordier's notes, usually by surname only. Identify the work Yule–Cordier cites for that topic: a book, a journal article (give the journal, volume and year), or an official report. Several names are common surnames, so use the snippet. "Anderson" appears in two unrelated contexts (II-08 Burma/Yunnan; III-03 Sumatra) and is probably two different people: resolve both. "John Wood" is the explorer of the Oxus (journey 1838, published 1841; the 1872 edition has an essay by Yule). "Salt" is Henry Salt (Abyssinia). "Elliot" is Elliot and Dowson, The History of India as Told by Its Own Historians (Wassaf extracts). "Stein" is Aurel Stein. "Major" is R. H. Major. "Palladius" is the Archimandrite Palladius (Kafarov).

GROUP C — 19TH-CENTURY TRAVELLERS, ORIENTALISTS AND SINOLOGISTS (79 entries):
- Palladius — I-10, I-12, I-13, II-01, II-02, II-03 … — “…oof, silk braces, demountable. Cane/Palm Hall / tent architecture at Shangtu (Palladius Tsung tien; Rashid; Altan Tobchi). Ramusian ornamental fullness. [@yc, 1.…”
- Pauthier — I-03, I-05, I-07, I-09, II-01, II-02 … — “…ted. Chinese annal “POLO” commissioner 1277 = Marco — attractive, not proven (Pauthier; Yule “happy to believe”).…”
- Bretschneider — I-10, II-02, II-03, II-05, II-06, II-07 … — “…erved for the Kaan. Reserved middle-gate etiquette. Five vs three gateways (Bretschneider). Inner enclosure with matching arsenals and gates.…”
- Hammer — I-08, II-02, II-03, II-04, III-09 — “…e-training tales in Odoric, Chinese notice of Mulahi, Arabic romance materials (Hammer).…”
- Baber — I-09, II-04, II-07, II-08 — “…~ Boiled wine; cord head-dress; skin coats/shoes. Parallels in hill cultures (Baber; Elphinstone; Wood); “evil murderous” moralizing.…”
- Richthofen — I-11, II-05, II-06, II-07, II-09 — “…l-Dīn (Sing; coal); Pegolotti; Odoric; Ibn Baṭṭūṭa; Palladius; Bretschneider; Richthofen; Rossabi; Yule–Cordier notes passim.…”
- Caldwell — III-05, III-06 — “…tfili. Comparative: Montecorvino; Marignolli; Odoric; Conti; Barbosa; Assemani; Caldwell; Nelson; Subrahmanyam; Syrian Christian / Thomacide traditions.…”
- Marsden — I-08, II-02, II-04, II-06, III-03 — “…/ Arbre Sec as described (plane-like fruit/wood). Chīnār botany plausible (Marsden; Olearius parallels); individual tree and “100 miles” isolation. / Locals…”
- Tennent — III-04, III-05 — “…n Battuta (Peak, chains); Odoric; Marignolli; Hayton; Jordanus; Conti; Ma-Huan; Tennent; Hardy; Almond on Barlaam/Josaphat; Mahāvaṃsa (careful).…”
- Houtum-Schindler — I-07, I-08 — “…ctural; turtledove taboo local report. Apples of Paradise: citrus or konār (Houtum-Schindler), not plantain.…”
- Sykes — I-08, III-09 — “…circuitous rather than the short modern Kermān–Kuhbenān line (Houtum-Schindler; Sykes).…”
- Rockhill — I-09, I-13, II-06 — “…visible hooks. Comparative: Wood; Mirza Haidar; Buddhist histories of Kashmir; Rockhill; Xuanzang sparingly; Yule on dialects; Stephen Haw. Stop at return to Badashan;…”
- Shaw — I-10, I-11 — “…swollen necks from water. Goitre at Yarkand repeatedly confirmed (’Izzat Ullah; Shaw; Hedin ~¾ population; Roborovsky; Mirza)—water-quality theory matches Polo. /…”
- Grenard — I-10, I-11 — “…ra Khān ~980–990; Hiuen Tsang jade/textiles; 10th-c. grapes/wine; Johnson 1865; Grenard). Gazetteer: Khotan visited.…”
- Forsyth — I-10, II-04 — “…? Pein = Pima / Kiria (Keriya) area. Location debated (App. L-type; Forsyth; Grenard); route toward Lop accepted. / Provinces Cascar→Lop belong to “Gre…”
- Garnier — II-07, II-09 — “…marital hospitality + lover’s tokens (≥20). Wide parallels (Herodotus; Martini; Garnier; Westermarck); local attribution may blend tribes; Book’s jest tone.…”
- Doolittle — I-11 — “…wall-hole instead of door. Classic Chinese/Buddhist funerary complex (De Groot; Doolittle). YC 1.40.…”
- de Groot — I-12, II-10 — “…, Rubruck, Ibn Battuta, Wassāf; Chinese and Caucasian ghost-marriage parallels (de Groot). YC 1.55. As specifically “Tartar” may blend Chinese practice.…”
- Mayers — II-10 — “…gnan practice as national custom. Cremation common enough (Ku Yen-wu; de Groot; Mayers); burial also attested (Arab Relations; Conti).…”
- Paulin Paris — I-01 — “…ared unusual preamble formula (Seigneurs Empereurs et Princes…); consensus of Paulin Paris, Yule, Benedetto, later editors. Meloria captivity since 1284: fair conjectur…”
- Stein — I-10 — “…. Gazetteer: Pem uncertain. Comparative: Mirza Haidar; Tang–Yuan itineraries; Stein (Khotan archaeology); Syriac/Nestorian Central Asia; Wood; Forsyth Mission. Sto…”
- Hedin — I-10, I-11 — “…n necks from water. Goitre at Yarkand repeatedly confirmed (’Izzat Ullah; Shaw; Hedin ~¾ population; Roborovsky; Mirza)—water-quality theory matches Polo. / Nest…”
- Kozlov — I-11 — “…day Lop→Sachiu timing and Lob-nor route geometry long debated (Richthofen–Hedin–Kozlov). Universal desert-goblin folklore (Pliny, Mas’udi, Ibn Battuta, Conti).…”
- D’Ohsson — II-10 — “…) revolt vs Kublai. Chinese annals 1262; T’si-nan siege (Gaubil; De Mailla; D’Ohsson; Pauthier). Year corrupt (1273 for 1262); captains Aguil & Mongotay exist (Ag…”
- Quatremère — III-09 — “…Comparative: YC Prol. 17–18 and Intro. §§21–22; Rashid al-Din (Quatremère; Thackston/Boyle); Hammer Geschichte der Ilchane; Wassaf (Elliot); Rossabi on…”
- Devéria — II-09 — “…memoria technica (cf. Java Kwawa) vs real Thai / Lao / Shan names. Cordier / Devéria: Xieng-mai / Pa-pe dossier.…”
- Phillips — II-14 — “…Zayton = Quanzhou (T’swan-chau) — largely settled; gazetteer visited. Older Phillips Chang-chau fight superseded by Yule–Cordier, Bretschneider, Yuan shi-po, Rash…”
- Gill — II-07, II-08 — “…= Jinsha (Kin-sha Kiang / “Golden Sands”). Cassia of Kien-ch’ang (Richthofen; Gill); Brius ID firm. “Clove” name.…”
- Anderson — II-08, III-03 — “…Gazetteer: Ferlec likely_visited. Comparative: Junghuhn; Anderson; Conti Batech; Barbosa; De Barros; Arab Relations (Al-Ramni).…”
- Abbott — I-06, I-08 — “…e. Medieval tradition strand; Yule: Sávah ~50 mi SW of Tehran; Ávah ~16 mi SSE (Abbott). Odoric places Magi at Kashan (some MSS Saba).…”
- Gordon — I-10 — “…sheep, horns ~six palms; horn heaps as snow guides: Ovis Poli (Blyth); Wood, Gordon, Severtsof, Younghusband. Wolves and bone-heaps: Ramusio/G tradition.…”
- Trotter — I-10 — “…small vassal province; peculiar language. Firm ID; Iranian Pamir dialect; Wood/Trotter. / Chief titled None (= Count), liege to Badashan: vassal count accurate;…”
- Burnes — I-09 — “…cave dwellings in earth hills. Kishm ID and caves paralleled (Bamian, Heibak; Burnes; Moorcroft); “very great province” inflated. / Porcupines project quills…”
- Elphinstone — I-09 — “…d wine; cord head-dress; skin coats/shoes. Parallels in hill cultures (Baber; Elphinstone; Wood); “evil murderous” moralizing.…”
- Moorcroft — I-09 — “…lion; recurrent medieval and early-modern testimony (Rashīd al-Dīn; Sidi Ali; Moorcroft; Wood).…”
- Montgomerie — I-10 — “…Extreme cold makes fire burn/cook poorly. Altitude boiling-point / poor fuel (Montgomerie; Huc–Gabet); traveller truth under romance sky. Humboldt’s doubt rested on Ramu…”
- Khanikoff — I-08 — “…with bitter undrinkable water. Lūt / salt-desert conditions match travellers (Khanikoff on Shor-Rūd); exact staging and “seven days” schematic. Route likely circui…”
- Curzon — I-08 — “…d al-Dīn; Daftary on Nizārīs; Yule’s long Assassin and Arbre Sec notes; Sykes / Curzon / Houtum-Schindler on Lūt and Tun-o-Kain.…”
- Ferrier — I-09 — “…and long ruin amply attested (Ibn Baṭṭūṭa still ruined ~1330s; Clavijo; Burnes/Ferrier). / Alexander married Darius’s daughter at Balkh: local/romance claim (L…”
- Rawlinson — I-09 — “…of Udyāna); identification (living Pashai tribe SW vs Chitrāl/Udyāna complex; Rawlinson on older Aprasin/Paresīn). Marco personally visited Pashai and Keshimur: inte…”
- Blyth — I-10 — “…. Great wild sheep, horns ~six palms; horn heaps as snow guides: Ovis Poli (Blyth); Wood, Gordon, Severtsof, Younghusband. Wolves and bone-heaps: Ramusio/G tradi…”
- Cunningham — I-10 — “…vage skin-clad Idolaters. Bolor as areal high-country name real (Hiuen Tsang; Cunningham Balti; Shaw Chitrál; Mirza Haidar’s four-month circuit)—not the Jesuit misplace…”
- ’Izzat Ullah — I-10 — “…s; goitre and swollen necks from water. Goitre at Yarkand repeatedly confirmed (’Izzat Ullah; Shaw; Hedin ~¾ population; Roborovsky; Mirza)—water-quality theory matches Pol…”
- Roborovsky — I-10 — “…oitre at Yarkand repeatedly confirmed (’Izzat Ullah; Shaw; Hedin ~¾ population; Roborovsky; Mirza)—water-quality theory matches Polo. / Nestorian and Jacobite Christi…”
- Johnson — I-10, I-11 — “…water, flight into sand before armies. Cherchen/jade/salt-water ethnography (Johnson, Shaw, Grenard). Exact “five days” and army-escape colour. YC 1.38; gazet…”
- Browne — I-11 — “…re-bleached napkins; Rome napkin for Sudarium. Asbestos fabric process sound (Browne; Cardan). Province name/location (Chi-kin / Kemkemjút / Kobdo). YC 1.42.…”
- Koeppen — II-01 — “…policy pledge. Simultaneous patronage as Chinghizide political practice (Yule; Koeppen), not private wistfulness à la Akbar.…”
- Michie — II-03 — “…relaxed. Multiply attested (Carpini; Rubruck; Odoric; Makrizi; Mongol proverb; Michie yourt ropes). / Ushers for foreigners; giant door-wardens with staves:…”
- Vámbéry — I-02, I-13, II-03 — “…tic nines (9×9): well-attested Mongol/Turkic ritual arithmetic (Hammer; Hayton; Vámbéry).…”
- Atkinson — II-04 — “…own at wolves and foxes. Strong Inner Asian ethnographic confirmation (Kirghiz; Atkinson; Forsyth; Baber; Timkowski).…”
- Timkowski — II-04 — “…trong Inner Asian ethnographic confirmation (Kirghiz; Atkinson; Forsyth; Baber; Timkowski).…”
- Hooker — II-07 — “…Giant bamboo fires explode; frighten beasts; wrap ears/horses. Explosions (Hooker; Lindsay; Bretschneider). Girth and “ten miles” theatre.…”
- Lindsay — II-07 — “…bamboo fires explode; frighten beasts; wrap ears/horses. Explosions (Hooker; Lindsay; Bretschneider). Girth and “ten miles” theatre.…”
- Westermarck — II-07 — “…ospitality + lover’s tokens (≥20). Wide parallels (Herodotus; Martini; Garnier; Westermarck); local attribution may blend tribes; Book’s jest tone.…”
- Sladen — II-08 — “…Ratio cluster with Zardandan. Market rhythm (5-day Shan cycle also attested; Sladen). Kakhyen gold still reported north of Bhamo.…”
- Bridgman — II-09 — “…sts hung in mountain caverns; cowries + gold. Kolo-man / hill-fort character (Bridgman; Magaillans); cowries fit Yunnan–SEA shell zone of II-7. Exact hanging-cave r…”
- Perny — II-09 — “…ogs bait tigers for archers; silk on the river. Xiabu / hemp-nettle cloths (Perny); tigers in Kwei-chau mountains; Macleod’s caravan dogs toward Kiang Hung. Le…”
- Hosie — II-07, II-09 — “…lb moulds); 80 = 1 saggio gold; stamped; hill arbitrage. Vogel; Garnier; Hosie at Pai-yen-ching; Ramusian colour fits practice. Central presence argument.…”
- Gandar — II-10 — “…matu; ma-t’ou = jetty. Lin-t’sing alternative for “from the south” (Cordier/Gandar). Wen and Sse diverted NW/SE; confluence at Nan-wang as summit.…”
- Favé — II-11 — “…ne engines well attested. Western counterpoise as the real technical novelty (Favé/Yule inference). Polo presence at siege climax 1272–73 under standard chronol…”
- Hanbury — II-14 — “…d as custom. saffron-fruit → Gardenia crocine or Carthamus (Bretschneider/Hanbury).…”
- Titsingh — III-01 — “…mikaze typhoon tradition; capital ruse and 1279 dating contested. Comparative: Titsingh; Gaubil; De Mailla; Yuan shi; Rossabi on Kublai.…”
- Aymonier — III-02 — “…Comparative: Yuan–Champa war records; Gaubil; Wolters; Hall; Aymonier on Chams. Polo’s neat vassalage vs bruising frontier (prince’s resistance 1282;…”
- Major — III-01, III-02 — “…iption ~1292–93 almost coeval. Phantom Australia from misread “Java” departure (Major).…”
- Groeneveldt — III-02 — “…monsoon delay as return logic for III-9. Comparative: Yule–Cordier III.v–viii; Groeneveldt; Odoric; Conti; Ma Huan / Daooyi zhilue; Ibn Battuta (later Samudra); Wolters…”
- Junghuhn — III-03 — “…Gazetteer: Ferlec likely_visited. Comparative: Junghuhn; Anderson; Conti Batech; Barbosa; De Barros; Arab Relations (Al-Ramni).…”
- Schlegel — III-03, III-04 — “…/ Angamanain = Andamans; Arabic dual form. place; etymology (Schlegel). / Dog-headed men (mastiff faces) — geographic myth; possible soft core in…”
- Hardy — III-04 — “…(Peak, chains); Odoric; Marignolli; Hayton; Jordanus; Conti; Ma-Huan; Tennent; Hardy; Almond on Barlaam/Josaphat; Mahāvaṃsa (careful).…”
- Stewart — III-05 — “…Comparative: Wassaf; Rashid; Ibn Battuta; Tennent; pearl-fishery histories (Stewart; Pridham). Yule: fishery account “still substantially correct.”…”
- Pridham — III-05 — “…rative: Wassaf; Rashid; Ibn Battuta; Tennent; pearl-fishery histories (Stewart; Pridham). Yule: fishery account “still substantially correct.”…”
- Nelson — III-05 — “…parative: Montecorvino; Marignolli; Odoric; Conti; Barbosa; Assemani; Caldwell; Nelson; Subrahmanyam; Syrian Christian / Thomacide traditions.…”
- Birdwood — III-08 — “…(~ simile only; actual Boswellia not fir); sometimes sun-flow without notch. Birdwood on Boswellia; Arabian incense-route archaeology.…”
- Elliot — III-09 — “…al-Din (Quatremère; Thackston/Boyle); Hammer Geschichte der Ilchane; Wassaf (Elliot); Rossabi on Kublai; Haw chronology; Larner; Sykes on Persian return road.…”
- Salt — III-07 — “…Amda Seyon’s wars (Bruce ~1312–16) too late for ~1298 dictation if Bruce holds; Salt/Pauthier shove dates back; Yule treats as type. / Elephant-castles in Abyss…”
- Bushell — I-13, II-04, III-12 — “…ridge’s “Xanadu” = Vol. III reception history, not developed here. Comparative: Bushell; Shangdu archaeology / UNESCO; Yuan Shi; Gaubil; Rashid; Odoric; Rubruck; Rossa…”
- de Sacy — I-08 — “…tion-sleep; awakening in Garden. Real fidā’ī devotion; hashish etymology (de Sacy) behind Assassin; Crusader title Old Man of the Mountain = Shaikh al-Jibāl.…”
- John Wood — I-09, I-10 — “…Finest azure (lapis) in vein like silver. Kokcha / Yamgān lājward classic (Wood 1838). / Excellent unshod mountain horses; Kataghan type: breed reputatio…”
- Severtsof — I-10 — “…horns ~six palms; horn heaps as snow guides: Ovis Poli (Blyth); Wood, Gordon, Severtsof, Younghusband. Wolves and bone-heaps: Ramusio/G tradition.…”
- Younghusband — I-10 — “…palms; horn heaps as snow guides: Ovis Poli (Blyth); Wood, Gordon, Severtsof, Younghusband. Wolves and bone-heaps: Ramusio/G tradition.…”

OUTPUT FORMAT (required). (1) One table with columns: # · name as I cite it · who · work meant (and which context) · first edition · English translation (if any) · free copy URL · confidence · flag (AMBIGUOUS / NOT A SOURCE / blank). (2) One BibTeX block with every entry. (3) A list of the names you could not resolve, and why. Rules: do not invent titles, editions, dates, URLs or DOIs. If you cannot confirm an edition, say "unconfirmed". Prefer library catalogues (WorldCat, national libraries), publisher pages and scholarly bibliographies over general websites. Do not stop early: cover every entry.
```

## CIT-D — Sources for the non-Polo epigraphs

```text
I am preparing a new English retelling of Marco Polo's book for print (base text: Yule–Cordier, 1903/1920). Four chapter epigraphs quote something other than Polo's text, and their wording or source is wrong or invented. For each question, give the exact original wording, its language, the standard English translation, and where a reader can check it (the edition, and a stable URL to a scan or open edition). Then give me a one-line credit for it (author, work, date).

1. THE DEATHBED LINE (book section I-B1). My draft has: "I did not tell half of what I saw, for I knew I would not be believed." Find the earliest source: Jacopo d'Acqui, Imago Mundi (c. 1330s)? Give the Latin text as printed in the standard edition, and which manuscript it comes from; a faithful English translation; the published translation scholars cite (e.g. in Moule–Pelliot 1938 or Yule's Introduction); and whether the clause "for I knew I would not be believed" has any basis.

2. COLUMBUS ON CHIPANGU (book section III-11). My draft has an invented line: "And this island [Chipangu] is so rich in gold that no man can tell it." Find Columbus's actual postils (marginal notes) on Chipangu and its gold in his copy of the Latin Polo (Pipino's version, printed by Gerard Leeu, c. 1483–85; Biblioteca Colombina, Seville). Give the Latin text of the relevant postil(s); their number in the standard edition (e.g. Juan Gil, El libro de Marco Polo anotado por Cristóbal Colón); an English translation; and the state of the debate about when Columbus wrote them. Give the corresponding passage of Pipino's Latin text too.

3. THE BOOK'S STATED PURPOSE (book sections III-11, III-12). My draft has: "He who made this work… put in writing all that he saw and heard, so that other people might know of it." Find the real statements of purpose in (a) the F (Franco-Italian) prologue, (b) Pipino's Latin prologue (his reasons for translating), and (c) Ramusio's 1559 preface. Give the original wording and a standard English translation for each.

4. EARLY INSPIRATION (book section III-B1). My draft has an invented line: "Because of this book many set forth…". Give 3–5 genuine, citable statements from before 1600 that Polo's book shaped exploration or geography. Candidates: Toscanelli's 1474 letter (Quinsay, the Great Khan); Columbus's own writings; Fra Mauro's map legends; Ramusio's preface; Portuguese or Spanish chroniclers. For each: exact wording, source, date, translation, and one line on its reliability.

OUTPUT FORMAT (required). For each question: (1) the original text; (2) an English translation, saying whose; (3) the edition and a stable URL; (4) the one-line credit; (5) confidence and any caveat. Then a BibTeX block for every edition cited, and a list of what you could not confirm. Rules: never invent quotations. If you have not seen the original wording, say so and give only a paraphrase. Prefer critical editions, library catalogue records and scholarly translations.
```
