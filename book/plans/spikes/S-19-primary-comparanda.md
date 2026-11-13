# S-19 — Comparative primary sources: translations and citable passages

**Status:** closed best effort 2026-11-12 (direct checks done; gaps listed in Findings) · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** every "Comparative:" clause in the Notes; III-12 § controls; the S-02 lint rule that marked quotations must match `refs/` (non-Yule sources need their own entries)

## Question
For each contemporary witness the book sets beside Polo (Rubruck, Carpini, Odoric, Ibn Battuta, Rashid al-Din, Juvaini, Wassaf, the *Secret History*, the *Yuan shi*, Zhou Daguan, Wang Dayuan, Zhao Rugua, Montecorvino's letters): which translation should we cite, is it public domain or open access, and which specific passages match the book's comparisons?

## Why it matters
- The Notes say "Comparative: Rubruck; Odoric; Ibn Battuta" without saying what those witnesses actually say.
- Short quotations from them would make the Notes checkable and vivid. But the lint only checks quotations against `refs/` (Yule). A quotation from another source needs that source on disk, and a quotation from a copyrighted translation needs a fair-use judgement.
- Public-domain translations can go into `refs/` and be linted; modern translations can only be paraphrased.

## Inputs
- `grep -rn "Comparative" vol-*/` (the book's comparison sites)
- `tools/lint.py` (marked-quotation check, `refs/` loader)
- S-12 bibliography keys (closed 2026-11-10; `registry/sources.md`). Citation editions already chosen: Rubruck `jackson1990mission`; Carpini `dawson1955mongol` (English), `menesto1989storia` (critical Latin); Odoric `yule1913cathay` (English), `marchisio2016relatio` (critical Latin); Ibn Battuta `gibb1958travels`; Rashid al-Din `thackston1998rashiduddin`, `boyle1971successors`; Juvaini `boyle1958history`; Wassaf `hammer1856geschichte` (German, vol. 1; no complete English translation); *Secret History* `derachewiltz2004secret`; *Yuan shi* `yuanshi1370`; Wang Dayuan `wang1349daoyi`. So the prompt asks (a) only for the other witnesses.

## Method
1. Run the prompt and save the output to `research/results/S-19-raw.md`.
2. Intake: for each witness, choose the citation edition (S-12 key) and the quotation edition, which must be public domain.
3. Download public-domain texts into `refs/` (plain text, one file per work, with a source header), so that the lint can match quotations from them. Record the URL and licence.
4. Write `registry/comparanda.md`: book passage → witness → location (book or chapter) → paraphrase → PD-quotable yes/no.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). Its endnotes compare Polo with other contemporary witnesses. I need, for each witness below: (a) the scholarly translation to CITE today; (b) the best PUBLIC-DOMAIN English translation I can QUOTE from, with a stable full-text URL (Internet Archive, HathiTrust, Project Gutenberg, Wikisource), its date and copyright status in the USA and the EU; (c) the specific passages (by book/chapter/section, not page) that match the Polo topics I list, each with a one-sentence paraphrase.

For Rubruck, Carpini, Odoric, Ibn Battuta, Rashid al-Din, Juvaini, Wassaf, the Secret History and the Yuan shi I already have the edition to cite: for them give only (b) and (c).

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
- [x] `research/results/S-19-raw.md` saved
- [x] Available public-domain texts in `refs/`, each with a source and licence header; 1733 *Ancient Accounts* retained as a rights-pending research copy
- [x] `registry/comparanda.md` (checked passages separated from leads; gaps remain)
- [x] Decision on the lint (handed to `BLD.T10`). The corpus is a fixed list (`CORPUS` in `tools/yule.py`), so new texts in `refs/` are invisible to the lint until they are added there. Decide whether they join the quotation check only, or the 7-gram verbatim check as well.

## Feedback to plan
- `VOICE-GUIDE.md` § Notes: the Comparative clause shape (paraphrase, or a short PD quotation with its location)
- `S-02` / `tools/lint.py`: source-aware quotation matching, if needed

## Follow-up prompts

The first run has substantial topic-level and rights gaps. Run this as a focused follow-up; the user-supplied output is already preserved unchanged apart from the intake header. Do not use it as evidence without checking the primary text:

```text
I am preparing a commercially published English retelling of Marco Polo's account of Asia and the Indian Ocean. Its base text is Henry Yule's translation of Marco Polo, revised by Henri Cordier (1903, with 1920 addenda). The endnotes compare Polo's claims with other medieval travellers, historians and Chinese records. I need to make those comparisons specific and checkable.

RESEARCH QUESTION

Which passages in the sources below actually address the same places, events or customs as Polo? For each useful comparison, what does each source say, where exactly can a reader find it, and is there a public-domain English translation suitable for a short quotation? Identify gaps honestly. A witness describing the same place is not, by itself, evidence that Polo visited it; a later writer may also have used Polo rather than provide independent corroboration.

PRIORITIES

Work in priority order. A smaller number of passages actually inspected is more useful than a comprehensive list of plausible but unverified citations. Spend your effort on specific passages and edition-specific locators, not general biographies or repeating this project description.

1. Rashid al-Din and the return voyage: locate the account of Kököchin, her intended marriage to Arghun, and the subsequent succession and marriage. What exactly does the Persian history say, and does it name any Polo? Give the relevant locations in W. M. Thackston's Jamiʿ al-tawarikh (1998–99) and/or J. A. Boyle's The Successors of Genghis Khan (1971). Check Francis W. Cleaves's 1976 article on the Chinese and Persian sources if accessible. Also locate Rashid's relevant accounts of Ahmad, Bolad, Nayan, Kaidu and Gaykhatu's 1294 paper-money issue, where feasible.

2. Chinese records and Mongol history: locate the Yuan shi passages on Ahmad, the Xiangyang siege engineers, Nayan, and the Java, Champa, Burma and Japan expeditions. Give verified juan and translated passage, identifying the English translator. Check the chronology of the siege and the Polos' journey without treating their precise arrival date as certain. Locate canonical sections of the Secret History of the Mongols on Temüjin's birth, Ong Khan and Jamukha, and Polo's corresponding account. For Juvaini, locate the fall of Alamut and related Ismaili passages in Boyle's History of the World-Conqueror (1958) and, if possible, the Persian edition.

3. Earlier and later travel accounts: locate Rubruck on portable dwellings, fermented mare's milk, the religious debate, Uyghur writing and, if present, Chinese paper money; and Carpini on customs, warfare, burial and Güyük's election. Use Rockhill's 1900 translation and the modern translations by Peter Jackson (Rubruck, 1990) and Christopher Dawson's Mongol Mission (Carpini, 1955) where accessible. Rockhill's volume contains only part of Carpini's account: identify what is actually translated. For Odoric, check Cansay/Hangzhou, Yangzhou, Fuzhou and the location of the waterfowl fishing episode, the Khan's court, and foot-binding in Yule–Cordier's Cathay and the Way Thither, vol. II (1913), comparing the critical Latin where possible. For Ibn Battuta, locate Chinese ships and paper money, Zaytun, al-Khansa, the Maldives, Adam's Peak, Samudra, Aden and Hormuz in Gibb/Beckingham and Samuel Lee's 1829 abridged translation; say which passages Lee omits or changes.

4. Indian Ocean and missionary material: locate Zhou Daguan on Chinese residents and trade goods in Peter Harris's A Record of Cambodia (2007); locate specific Southeast Asian or Indian ports in Wang Dayuan's Daoyi zhilüe and identify available English translations and their rights. Check Zhao Rugua on Java, Malabar, the Chola coast and Kish in Hirth and Rockhill's 1911 Chau Ju-kua. Locate Al-Ramni in the Arabic Accounts of China and India, and identify the English translator of the 1733 Ancient Accounts of India and China associated with Eusebius Renaudot. Locate al-Qazwini's account of the rukh and a reliable translation. Identify John of Montecorvino's 1305 and 1306 letters and his earlier India letter, and Andrew of Perugia's 1326 Zayton letter, with specific passages relevant to Polo. Check whether Hayton of Korykos used Polo, and if possible cross-reference the French/Latin edition with Robert Bedrosian's English translation from an Armenian textual tradition.

5. Where accessible, compare what Igor de Rachewiltz actually argues in his 1997 article “Marco Polo Went to China” and his 2002 appraisal of Frances Wood. Do not assume they make the same argument. Identify which witnesses he uses to discuss Polo's omissions, and which evidence he treats as positive corroboration.

EXISTING LEADS TO VERIFY, NOT PREMISES TO REPEAT

Wassaf's Maʿbar horse-trade and dynastic material appears in H. M. Elliot and John Dowson, The History of India as Told by Its Own Historians, vol. III (1871), around pp. 32–34. Yule–Cordier's Cathay vol. III (1914) includes selected English extracts from Rashid al-Din and letters by Montecorvino and Andrew; this is not a complete English translation of Rashid's chronicle. Bedrosian's Hayton translation carries an explicit public-domain statement. Verify these claims and the scope of each translation. An open-access translation is not automatically public domain.

EVIDENCE AND RIGHTS RULES

- Prefer the primary text, its scan, a critical edition, an academic publication, a publisher, or a library record. Give a stable URL or DOI for every source actually used. Label a source that you located but could not read as not inspected.
- Give book/chapter/section/juan and page only for the specific edition you checked. Do not transfer numbering between translations or invent page numbers, quotations, dates, DOIs or URLs. A table of contents verifies a heading, not the detailed wording of the passage. If you cannot inspect it, say “not found” or “not inspected,” not “confirmed.”
- Identify the original author's words, quoted speech, hearsay and the translator's/editor's commentary separately. Paraphrase passages you did not see; do not quote them. For each comparison, distinguish agreement on a general setting from corroboration of a particular event or personal presence, and note potential textual dependence.
- For each quotation edition, identify translator, publication date, source link, scope and copyright status in the United States and EU. Explain the basis for a public-domain conclusion, including translator/editor death dates where relevant; flag uncertainty and jurisdiction-specific complications. State separately whether a source is open access. Do not infer that copyright forbids every possible quotation; this project's editorial policy is to select public-domain wording for proposed verbatim quotations.
- Give priority to the chosen scholarly translations named above for citation. A public-domain translation can be a separate quotation source; do not imply its wording or locator is identical to the modern edition. Do not reproduce long copyrighted passages.

OUTPUT

1. A table with one row per specific comparison: Polo topic and locator in Yule–Cordier; other witness and edition-specific locator; concise account of what each says and the relationship; source actually inspected (full text, scan, contents or secondary source); stable link; confidence; and status (verified, partial, disputed or not found). Do not use project-specific chapter IDs.
2. An edition and rights table: witness, recommended edition to cite, proposed public-domain English quotation edition if any, scope, US/EU rights basis, and stable full-text link. State “none found” rather than claiming none exists without evidence.
3. Brief notes on significant disagreements, source dependence, translation differences, and any correction to the leads above. Attribute scholarly positions to named works. Flag sources published after 2013 as NEW.
4. A bibliography of sources actually consulted, with complete bibliographic information and DOI or stable URL where available, followed by a prioritized list of unresolved questions and exactly what source or library check would resolve each one.
```

## Findings

**Retry intake 2026-11-12.** The [Consensus report](../research/results/S-19-retry-raw.md) is candid that it did not inspect the main primary passages; it cannot override the direct checks already recorded. The report supplies bibliographic leads, including Cleaves’s valid DOI, but makes no new primary-text or rights clearance. In an independent search, Boyle, “Rashīd al-Dīn and the Franks” (1970), p. 66, yielded an English rendering of the specific Rashid bride-embassy passage and Persian-edition references, and Yule–Cordier Prologue XVIII n. 6 supplied a separate mediated extract. The [retry intake](../research/results/S-19-retry-intake.md) records what each can and cannot establish. Add `boyle1970rashidfranks` to the bibliography; 1970 is not automatically PD. The direct Persian text, Thackston location and Cleaves article remain unchecked; do not require another research run just to repeat those limitations. S-19 remains open for remaining witness and rights gaps.


**Follow-up intake 2026-11-12.** The [second supplied report](../research/results/S-19-followup-raw.md) was saved and [audited](../research/results/S-19-followup-intake.md). Bibliographic existence spot check: 10/10 works located; that does not verify the report’s claims or rights. A separate focused ten-claim sample produced 0/10 verified as stated: nine are contradicted or erroneous and one is internally contradictory and unverified; the sample is not a population error estimate. Its copyright claims and exact locators cannot be accepted without primary checks. The independent checks found *Secret History* §§96, 116–119 and 122 and corrected the scope of Boyle 1971; these are recorded in the comparanda register. A narrower [retry prompt](../research/S-19-follow-up-retry-prompt.md) is ready. S-19 remains open.


**2026-11-12.** The user-supplied run is preserved at `research/results/S-19-raw.md`, with a provenance header; its tool, model and original date were not supplied. Results are leads, not independent authority. Eight texts were saved with source/rights headers: Rockhill 1900 (Rubruck and partial Carpini), Yule–Cordier *Cathay* II and III, Lee 1829, Hirth–Rockhill 1911, Elliot–Dowson III, Bedrosian's Hayton, and the 1733 *Ancient Accounts*. The last is research-only until the English translator and EU rights are checked. All except Bedrosian are OCR and require comparison to scans. Several files contain multiple authors and editorial matter.

**Bibliographic spot check: 10 of 10 edition records located**, not 10 verified comparisons: the eight local title pages/front matters and the [Harris publisher record](https://silkwormbooks.com/products/a-record-of-cambodia) and [NYU Press paperback record](https://nyupress.org/9781479830596/accounts-of-china-and-india/). This confirms existence/basic edition identity, not all rights, pagination, translations, or any uninspected passage. The intake independently inspected the original edition's contents for Odoric, Ibn Battuta, the missionary letters, Rashid's extracts, and Zhao, plus the Wassaf horse/politics and Rubruck tree narratives. Contents-only rows are identified as such in the register. Rights for 1733 remain open. Four new edition keys were added to the master bibliography; `sources.md` regenerated.

**Corrections.** Wassaf is translated in Elliot–Dowson III pp. 32–34; Rashid has selected PD English extracts in Yule–Cordier III; the latter also contains Montecorvino's letters I–III and Andrew's IV. Bedrosian explicitly dedicates his Hayton translation to the public domain, but it is based on an Armenian text and is not automatically interchangeable with the French/Latin edition. Odoric ch. 46 covers foot-binding; ch. 31 places waterfowl fishing after Fuzo, not necessarily in the city. NYU identifies the 2017 paperback of *Accounts of China and India*; this does not determine the date of every issue. The raw report's different section IDs do not match this book. Its claimed original-prompt premise about de Rachewiltz is not present in this spike's prompt. An OCR search for a single spelling does not establish absence. III-12 Note [11] cites the Juvaini Boyle key for Rashid; handed to III-12.T4.

**2026-11-12 direct check (best effort).** Rashid's bride-embassy passage was read on page scans: Thackston pp. 606 and 593, and Jahn's Persian edition p. 40 (Internet Archive scans). Neither names the Polos or describes a sea route, and both credit Arghun with sending the embassy. Thackston p. 450 and Boyle (1971) pp. 290–291 were read for the siege engineers, and the *Yuan shi* juan 7, 8, 128, 203 and 210 entries for Xiangyang and Burma were read in Chinese. Full locators and inspection status: [S-19-claude-raw](../research/results/S-19-claude-raw.md). **Not found:** Cleaves 1976 (not accessible); Kököchin's death date; an English version of any *Yuan shi* entry; Alizade vol. 3 p. 280 (not seen). **Rights:** the 1733 *Ancient Accounts* is public domain in the US and EU and is cleared. Boyle 1971, Cleaves 1982, Harris 2007, Thackston 1998 and the 2015 de Rachewiltz/Street licence are not public domain. Bedrosian's Hayton is cleared by its translator's statement.

## Decision

**2026-11-12.** Use the register's checked locations for editorial work; check lead and open rows before making claims. Keep the S-19 follow-up open: the definition's comprehensive passage matching is not met. Chapter `.T4` handoffs and Notes guidance are in place, but no manuscript claims or quotations have been silently rewritten. Public domain is the project's quotation policy, distinct from open access or potential legal quotation exceptions.

**Lint:** keep the existing Yule-only 7-gram verbatim and Ramusio corpus unchanged. Add explicitly source-aware comparative quotation verification as `BLD.T10`, with per-source boundaries, no cross-author/editorial false matches, OCR cautions and wrong-source tests. Nothing newly downloaded is currently linted. Changes recorded in `VOICE-GUIDE.md`, S-02, BLD, relevant chapter `.T4`s, and the research/spike boards.

**2026-11-12 close (best effort).** Use the checked rows in `registry/comparanda.md`; Lead and Open rows stay out of the text until a chapter's `.T4` inspects them or drops the comparison. Lint: the Yule-only 7-gram check is unchanged. Source-aware quotation matching for the new public-domain texts is `BLD.T10`, which can use the `refs/` headers as its source boundaries. The spike is closed as best effort; `BLD.T10` and the `.T4` handoffs remain open.

## Tasks to create on close

- `BLD.T10` and affected `.T4` handoffs created as best-effort follow-through. Full close is deferred until remaining passage-level and rights gaps are resolved or explicitly disposed of.
