# S-17 — Yuan China: institutions, cities, corroborations (Vol. II)

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** Vol. II `.T1`/`.T4` enrichment; `GAZ` rows for Vol. II (feeds S-04); `DIA` (paper money, the yam, the Cambaluc plan); `TBL` comparison tables; Vol. II back-matter trivia

## Question
Which of Polo's descriptions of Kublai's court, administration and cities have modern corroboration, especially from Chinese-language scholarship and archaeology? Which have been refuted? And which of the disputed Vol. II place identifications now have a best answer?

## Why it matters
- Vol. II carries the heaviest weight in the presence debate: money, salt, the post, Hangzhou, Yangzhou.
- Its Notes cite Vogel, Haw and Needham by name only, and use Yule's 19th-century sinology for everything else.
- Since then there has been the Dadu/Khanbaliq archaeology in Beijing, Yuan-era finds in Hangzhou, Quanzhou's 2021 World Heritage inscription, and a large Chinese literature on the Yuan.
- Six Vol. II identifications in the gazetteer are uncertain: Caugigu, Anin, Coloman, Cuiju, Acbalec Manzi and Cacanfu.

## Inputs
- `vol-2/` all files; Notes that cite Vogel, Haw, Needham, Rossabi or the *Yuan shi*
- `gazetteer.csv` Vol. II uncertain rows; critique II-M2, II-M11
- S-14 results for II-05, II-11, II-12 and II-14 (don't duplicate those items)

## Method
1. Run the prompt and save the output to `research/results/S-17-raw.md`.
2. Intake: trust checks; identifications → S-04 notes; material → `registry/enrichment.md` § Vol. II; numbers for diagrams → `registry/facts.md` tagged `DIA`.
3. Select per chapter, as in S-16.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). For the China chapters, I need what modern scholarship adds to, corrects in, or corroborates in Polo's descriptions. Chinese-language scholarship and archaeology are especially welcome; cite them with pinyin titles and English glosses. For each topic: Polo's claim (I summarise it), what modern evidence says, and the best sources.

- II-01: Kublai's campaign against Nayan (1287) — the Yuan shi account against Polo's; Kublai in a litter (howdah) on elephants; Kaidu.
- II-02: Kublai's appearance, wives and sons (Chabi, Chingkim); the Dadu (Cambaluc/Khanbaliq) palace and city plan — modern archaeology under Beijing; Liu Bingzhong's design; Polo's "silences" (tea, foot-binding, the Great Wall): what modern scholars say they do and do not prove.
- II-03: The Keshig (the "Keshican" bodyguard); the White Feast (New Year) and the birthday feast; jisün/zhisun robes of one colour and the "13 feasts"; the gifts of 100,000 white horses.
- II-04: The great hunt; trained cheetahs, lynxes and tigers ("lions"); gyrfalcons and the falconers; the yam/jamchi postal relay — station numbers, paiza tablets (surviving examples in museums); the "Sing" central secretariat; famine relief granaries; Kublai's road trees.
- II-05: Paper money (Zhongtong and Zhiyuan chao; issue years; the 1287 Zhiyuan reform; surviving notes and plates) — Vogel's Marco Polo Was in China (2013) on money, salt and revenue: summarise his findings; coal ("black stones"); the astrologers and the calendar; Ahmad's assassination in 1282 (Wang Zhu; the role of Bolad).
- II-06/II-07: The Pulisanghin (Lugou) bridge and its count of arches and lions; Taiyuan, Pingyang; Sindafu (Chengdu) and its bridges; Tibet after the Mongol campaigns; bamboo burning; salt money in Yunnan (Carajan); cowries; the conquest of the Dali kingdom (1253); couvade among the Zardandan; gold-capped teeth.
- II-08: The Mongol–Burmese wars (Battle of Ngasaunggyan 1277; the 1287 fall of Pagan): the Yuan and Burmese sources against Polo's battle of Vochan; the gold and silver towers of Mien; Bangala.
- II-09: Caugigu, Anin, Coloman, Cuiju — current identifications and their competitors.
- II-10: The fall of the Song: Bayan and the "hundred eyes" pun; Empress Dowager Xie; the foundlings; the Song capital.
- II-11: Yanju (Yangzhou) and Marco's claimed office: candidate offices in the Yuan salt administration; the Yangzhou Latin tombstones (Katerina Vilioni, 1342; Antonio Vilioni, 1344) and Italian merchants there; the Xiangyang siege (the S-14 sweep covers the engineers; here, the Polo claim's reception).
- II-12: Kian (the Yangtze) traffic and Polo's ship counts at Sinju (Yizhen?); the Grand Canal under the Yuan; Suju (Suzhou) and its bridges; the Zhenjiang Christians (beyond Mar Sargis).
- II-13: Kinsay (Hangzhou): the "12,000 bridges", the 100-mile circumference, population estimates for Song–Yuan Hangzhou; the West Lake; the "letter" of the Song empress (as described in Moule's Quinsai); archaeology of the Southern Song imperial city; public baths, fire watch, household registers (the "every house writes its names on the door" claim against Yuan baojia/household practice).
- II-14: Fuju (Fuzhou); Zayton (Quanzhou): the 2021 UNESCO site "Quanzhou: Emporium of the World in Song-Yuan China"; the Arabic, Persian, Syriac and Tamil inscriptions; the Kaiyuan temple; pepper import volumes; "Tyunju" porcelain kilns (Dehua; Cizao?).
- II-15: The Ilkhanate succession (Arghun, Gaykhatu, Baidu, Ghazan); the Kaidu wars; the "Book IV" battle narratives: where they came from.
- II-F1: the best modern overview works on Yuan China to recommend (e.g. Cambridge History of China vol. 6; Brook; Rossabi; Biran; Atwood) — and their up-to-date editions.

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-17-raw.md` saved
- [ ] Identifications for the six uncertain Vol. II rows, handed to S-04
- [ ] `registry/enrichment.md` § Vol. II; diagram data in `registry/facts.md` (tag `DIA`)

## Feedback to plan
- `multimedia-plan.md` § C (paper money, the yam, the Cambaluc plan) and § D (comparison tables)
- `illustration-plan.md`: caption facts (the Zhiyuan banknote, a paiza, the Lugou bridge)

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- Vol. II `.T1`/`.T4` items; `GAZ.T*`; `DIA.T*` data; `II-B1` trivia
