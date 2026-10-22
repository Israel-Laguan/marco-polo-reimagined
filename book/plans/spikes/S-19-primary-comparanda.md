# S-19 — Comparative primary sources: translations and citable passages

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** every "Comparative:" clause in the Notes; III-12 § controls; the S-02 lint rule that marked quotations must match `refs/` (non-Yule sources need their own entries)

## Question
For each contemporary witness the book sets beside Polo (Rubruck, Carpini, Odoric, Ibn Battuta, Rashid al-Din, Juvaini, Wassaf, the *Secret History*, the *Yuan shi*, Zhou Daguan, Wang Dayuan, Zhao Rugua, Montecorvino's letters): which translation should we cite, is it public domain or open access, and which specific passages match the book's comparisons?

## Why it matters
- The Notes say "Comparative: Rubruck; Odoric; Ibn Battuta" without saying what those witnesses actually say.
- Short quotations from them would make the Notes checkable and vivid. But the lint only checks quotations against `refs/` (Yule). A quotation from another source needs that source on disk, and a quotation from a copyrighted translation needs a fair-use judgement.
- Public-domain translations can go into `refs/` and be linted; modern translations can only be paraphrased.

## Inputs
- `grep -rn "Comparative" vol-*/` (the book's comparison sites)
- `tools/lint.py` (marked-quotation check, `refs/` loader)
- S-12 bibliography keys

## Method
1. Run the prompt and save the output to `research/results/S-19-raw.md`.
2. Intake: for each witness, choose the citation edition (S-12 key) and the quotation edition, which must be public domain.
3. Download public-domain texts into `refs/` (plain text, one file per work, with a source header), so that the lint can match quotations from them. Record the URL and licence.
4. Write `registry/comparanda.md`: book passage → witness → location (book or chapter) → paraphrase → PD-quotable yes/no.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). Its endnotes compare Polo with other contemporary witnesses. I need, for each witness below: (a) the scholarly translation to CITE today; (b) the best PUBLIC-DOMAIN English translation I can QUOTE from, with a stable full-text URL (Internet Archive, HathiTrust, Project Gutenberg, Wikisource), its date and copyright status in the USA and the EU; (c) the specific passages (by book/chapter/section, not page) that match the Polo topics I list, each with a one-sentence paraphrase.

WITNESSES AND TOPICS
1. William of Rubruck (1253–55): Karakorum; the silver fountain-tree; Mongol drink (kumiss); the debate of religions; Nestorians; yurts on carts; the Uighur script; Cathay and paper money. [I-12, II-03, II-05]
2. John of Plano Carpini (1245–47): Mongol customs, warfare, burial, election of Güyük. [I-12, II-01]
3. Odoric of Pordenone (c. 1318–1330): Hormuz, Thana, Malabar pepper, Mylapore and St Thomas, Champa, Java, Zayton, Fuzhou, Hangzhou ("Cansay"), Yangzhou, Khanbaliq and the court, fishing with cormorants, long fingernails, foot-binding (he mentions it, Polo does not). [III-*, II-12, II-13, II-14, II-02]
4. Ibn Battuta (1330s–40s): Chinese junks, Zaytun, Hangzhou (al-Khansa), paper money, the Maldives, Ceylon and Adam's Peak, Malabar, Calicut, Sumatra (Samudra), Kish/Hormuz. [III-01, III-03, III-04, III-07, III-08, II-13, II-14]
5. Rashid al-Din, Jami' al-tawarikh: Kublai's administration, Ahmad's murder, Bolad, the envoys to Arghun and Kököchin, the Ilkhanid succession, Nayan, Kaidu, Chinese paper money (the Ilkhanid chao fiasco of 1294 under Gaykhatu). [II-01, II-05, II-15, III-09]
6. Juvaini, History of the World Conqueror: the Assassins and Alamut, Mongol conquests in Central Asia. [I-08, I-09]
7. Wassaf: the Ma'bar horse trade and Pandya politics; Kish. [III-05]
8. The Secret History of the Mongols: Chinggis's origins, Ong Khan, Jamukha. [I-12]
9. Yuan shi (any English-translated sections): Ahmad, the Xiangyang engineers, the Nayan campaign, the Java and Champa expeditions, Burma. [II-01, II-05, II-08, II-11, III-02]
10. Zhou Daguan, A Record of Cambodia (1296–97): Chinese merchant life and trade goods in Southeast Asia. [III-02]
11. Wang Dayuan, Daoyi zhilüe (1349), and Zhao Rugua, Zhufan zhi (c. 1225; Hirth & Rockhill 1911 translation): ports and products of the Southern Seas and India. [III-02 to III-08]
12. John of Montecorvino's letters from Khanbaliq (1305–06), and Andrew of Perugia's letter from Zayton (1326). [II-02, II-14]
13. Hayton (Hethum) of Korykos, La Flor des estoires (1307): the Mongols and the Ilkhanate. [I-04, II-15]
14. The Persian and Arabic geographers on Polo's marvels: al-Qazwini (the rukh), Abu Zayd / Akhbar al-Sin wa'l-Hind (the "Arab Relations"). [III-07, II-10]

For each witness, also note any famous direct contradiction of, or agreement with, Polo that scholars routinely cite.

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-19-raw.md` saved
- [ ] Public-domain texts in `refs/`, each with a source and licence header
- [ ] `registry/comparanda.md`
- [ ] Decision on the lint (handed to `BLD`). The corpus is a fixed list (`CORPUS` in `tools/yule.py`), so new texts in `refs/` are invisible to the lint until they are added there. Decide whether they join the quotation check only, or the 7-gram verbatim check as well.

## Feedback to plan
- `VOICE-GUIDE.md` § Notes: the Comparative clause shape (paraphrase, or a short PD quotation with its location)
- `S-02` / `tools/lint.py`: source-aware quotation matching, if needed

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `BLD.T*` (`refs/` loader); per-chapter `.T4` Comparative-clause upgrades
