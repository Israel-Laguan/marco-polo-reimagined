# S-14 — Fact verification sweep (feeds S-06)

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** S-06 closure; factual `.T1` items in I-02, I-05, I-11, I-12, I-F2, II-01, II-02, II-05, II-11, II-12, II-14, II-15, III-01, III-09, III-10, III-11, III-B1

## Question
For each correction the critique made from general knowledge, and each item marked (unverified), what is the verified value and its source?

## Why it matters
This is S-06's research step, done externally. The claims below were written by critique agents without sources. If one of them is wrong, the "fix" plants a new error in place of the old one.

## Inputs
- `content-revision-plan.md` § W2 table and its unverified list
- Every "(unverified)" item in `tasks/chapters/` (15 files; `grep -rn -i unverified plans/tasks`)
- S-06 spike (this spike's results become S-06's *Findings*)

## Method
1. Run the prompt and save the output to `research/results/S-14-raw.md`.
2. Intake: trust checks. Two sources, or one primary, before ✓. Write `registry/facts.md` in S-06's format.
3. Carry the verdicts into S-06 and close it there. This spike closes when the facts sheet exists.

## Deep research prompt

```text
I am fact-checking a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). Below are claims an editor proposed as corrections, or flagged as unverified. For EACH one, tell me whether it is right, give the correct value if not, and cite the source. Primary sources (Chinese dynastic histories, Persian chronicles, Venetian archival documents) or the standard modern authority are preferred. Where scholars disagree, give each position with its proponent. The ID after each item is the book section it affects.

MONGOL AND ILKHANID HISTORY
1. The war of 1262–63 between Berke (Golden Horde) and Hulagu (Ilkhanate): Hulagu's army was routed at the Terek river in early 1263. Confirm the outcome and the date. [I-02]
2. Mosul fell to the Mongols after a siege in 1262 (not 1261), and its ruler (Malik Salih, son of Badr al-Din Lu'lu') was executed. Date and manner of death? [I-05]
3. Ong Khan (Toghrul, "Aung Khan" in Polo) was finally defeated by Chinggis Khan at the Jeje'er Heights in 1203. [I-12]
4. Nayan, the rebel prince of 1287, descended from Temüge Otchigin (Chinggis Khan's youngest brother), not from Belgütei. [II-01]
5. Gaykhatu (Polo's "Kiacatu") was Arghun's brother; Baidu was a cousin; Ghazan acceded in 1295. [II-15]
6. Chingkim (Zhenjin), Kublai's heir, died in the 12th month of Zhiyuan 22, i.e. early January 1286. Exact date? Also: Kublai's son Dorji (Dorjé), said to be an elder son who died young. [II-02]

YUAN CHINA
7. At the siege of Xiangyang/Fancheng (1268–73) the counterweight trebuchets were built by Muslim engineers Isma'il and 'Ala' al-Din, sent from the Ilkhanate by Abaqa. Their origins (Mosul? Shiraz? Herat?) per the Yuan shi; and the date the siege ended. The Polos could not have been present at the climax on the standard chronology — confirm that the Polos reached Kublai's court in 1275. [II-11]
8. Ahmad Fanakati's assassination (1282): the "Polo" who appears in the Chinese record (de Mailla/Gaubil, as cited by Yule) is now identified as Bolad (Boluo), not Marco Polo. Confirm. The correction is said to be in Cordier's own addenda. [II-05; also II-11, III-12]
9. The Ahmad episode is also in the Z (Zelada/Toledo) Latin text published by Moule and Pelliot in 1938, not only in Ramusio. [II-05]
10. Mar Sargis (Ma Xuelijisi), a Nestorian Christian, was the Mongol official at Zhenjiang and founded several Christian monasteries there from 1278–79. The source is the Zhishun Zhenjiang zhi (1332), translated by A. C. Moule in Christians in China before the Year 1550. How many monasteries, and on what dates? [II-12]
11. Cachanfu in Polo = Puzhou/Hezhong on the Yellow River (Shanxi), while Kenjanfu = Xi'an (Jingzhao). [II-F1, II-F2, gazetteer]
12. "Tyunju", Polo's porcelain town near Zayton (Quanzhou), is probably Dehua, a real Yuan export kiln centre. Is this the accepted identification? Alternatives? [II-14]
13. Chinese local histories confirm that sugar refining in Fujian (Polo's "Unken") was improved by men from "Babylonia" (Egypt). Is there any Chinese source for this, or is it a Ramusio-only statement with no Chinese corroboration? [II-14]
14. The Quanzhou (Houzhu harbour) shipwreck excavated in 1974, dated to c. 1270s, has a hull divided into 13 compartments, matching Polo's "thirteen". Number of compartments, dating, and the publication. [III-01; II-14]

THE RETURN AND AFTER
15. The Yongle dadian notice (via the Zhanchi), published by Yang Zhijiu in 1941, names three envoys of Arghun (Uladai, Abishqa, Khoja) in a document of 1290. It does not name the Polos. Rashid al-Din does not name them either. Confirm. What departure date do Cleaves and Haw derive from it (early 1291?), against Yule's "opening of 1292"? [III-09, III-11, III-12]
16. Marco Polo's wife was Donata Badoer. What do Venetian documents say about her and their three daughters (Fantina, Bellela, Moreta)? Date of the marriage, if known. [III-10]
17. Maffeo Polo's marital status. Was he married? Children? What do the Venetian documents (his will, the 1310 or other documents) show? [I-02]
18. Francesco Pipino's Latin translation is dated by modern scholars to c. 1310–1314, i.e. within Marco's lifetime, against Ramusio's later dating. Best current date and authority. [III-10]
19. Columbus's annotated copy of Polo is the Latin Pipino version printed by Gerard Leeu at Gouda (or Antwerp), c. 1483–85, now in the Biblioteca Colombina, Seville. How is the dating of Columbus's postils debated? Toscanelli's 1474 letter: its relation to Polo. [III-11]
20. The Catalan Atlas (c. 1375) does NOT show Chipangu/Japan. Japan first appears on a European map with Fra Mauro's mappa mundi (c. 1450–59) as "Zimpagu" or "Cimpagu". Also: was the Catalan Atlas commissioned for, or given to, the French king? [III-11]
21. Early print history of Polo's book: 1477 German (Nuremberg, Creussner); Latin (Leeu) c. 1483–85; 1496 Venetian Italian; 1503 Castilian (Rodrigo de Santaella, Seville); 1559 Ramusio (vol. 2 of Navigationi et viaggi, posthumous). Confirm or correct each date and place; add the Portuguese edition of 1502 (Valentim Fernandes) if correct. [III-11, III-B1]
22. Bento de Góis's journey (1602–1607) and Matteo Ricci's identification of Cathay with China. Is there any source for the claim that the Jesuits "measured" Polo's silences (tea, foot-binding) against their own observations? [III-11]
23. Adam's Peak (Sri Pada) traditions: Buddhist (Buddha's footprint), Muslim (Adam's footprint), Hindu (Shiva's). Is there also a Christian tradition (St Thomas), and when is it attested? [III-B1, III-04]
24. The Great Wall at Suzhou/Jiayuguan: the masonry fortifications date from the Ming (Jiayuguan fort founded 1372). What existed there in Polo's time (Han and other earlier walls)? [I-11, II-02]
25. Which boundaries does a typical "Mongol Empire" map show: c. 1260–1294 (the successor khanates) or the c. 1279 maximum? For a caption, what date range is accurate for the empire "in Polo's generation"? [I-F2, I-F1, II-15]

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-14-raw.md` saved
- [ ] `registry/facts.md` with all 25 claims graded, each with a source key
- [ ] S-06 *Findings* filled from this sheet

## Feedback to plan
- `content-revision-plan.md` § W2: overturned rows corrected; unverified list emptied or reduced to hedged items
- Chapter backlogs: "(unverified)" replaced by the verdict

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- Hands off to S-06, which writes the factual `.T1` tasks
