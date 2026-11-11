# S-13 — State of the field, 2013–2026

**Status:** closed 2026-11-11 · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** III-12 `.T1`/`.T4` (reliability essay), III-11, III-B1, I-01 Notes on composition; `registry/scholarship.md`

## Question
What has changed in Marco Polo studies since Vogel's *Marco Polo Was in China* (2013)? That covers new arguments, documents, archaeology, editions, and anything that came out of the 700th anniversary of his death (2024). Which of the book's "open questions" (III-12 Note [13]) have moved?

## Why it matters
- III-12 frames the "did he go?" debate as Wood (1995) against the de Rachewiltz / Haw / Vogel replies. A reader in the 2020s could reasonably ask "and since then?"
- The 2024 anniversary produced exhibitions, conferences and publications. A book printed after it that ignores them looks dated.
- An open question the field has since settled must not be presented as open, and the reverse.

## Inputs
- `vol-3/ch-12-reliability-essay.md`, Notes [7]–[13] and the core comparative set
- `vol-3/ch-11-afterlives.md`, `vol-3/back-01-trivia-and-afterlives.md`
- Critique vol-3 M-items on III-12 (Wood's case stated fully; works dated)
- S-12 (closed 2026-11-10): the editions found there are in `registry/sources.md` (Eusebi–Burgio 2018, Burgio–Simion 2015, Kinoshita 2016, Cliff 2015, Marchisio 2016). The prompt's item 2 now names them, so the run looks for others.

## Method
1. Run the prompt and save the output to `research/results/S-13-raw.md`.
2. Intake: trust checks; write `registry/scholarship.md` with one section per open question: positions, proponents and source keys. Add any new works to the `.bib`.
3. Mark each III-12 open question as *moved*, *unchanged* or *new*, and list the edits that follow for III-12 and III-11.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (Yule–Cordier translation as the base) with a closing essay on the book's reliability. The essay currently covers scholarship up to about 2013: Frances Wood, Did Marco Polo Go to China? (1995); Igor de Rachewiltz's rebuttal (1997); Stephen G. Haw, Marco Polo's China (2006); Hans Ulrich Vogel, Marco Polo Was in China (2013); plus John Larner (1999), John Critchley (1992), Pelliot, Moule–Pelliot (1938) and Olschki.

I need a rigorous survey of what has happened in Marco Polo studies from 2013 to today.

1. THE PRESENCE DEBATE. Arguments for and against Polo's presence in China published since 2013. Any new documentary evidence: Chinese, Persian, Mongol or Venetian sources newly identified, re-read or re-dated. Has a consensus formed? Who are the main voices now?

2. THE TEXT. New work on the manuscript tradition and the genesis of the text: the Franco-Italian F text, the role of Rustichello da Pisa, the Z (Zelada/Toledo) Latin version, Ramusio's sources, the Venetian VA tradition, Pipino's Latin. Include new critical or digital editions, and stemmatic findings. I already have: Eusebi and Burgio's open-access edition of F (Edizioni Ca' Foscari, 2018), the digital critical Ramusio by Burgio and Simion (Ca' Foscari, 2015), and the English translations by Kinoshita (2016) and Cliff (2015); list only other editions, or corrections to these.

3. THE 2024 ANNIVERSARY (700 years since Polo's death in 1324). Major exhibitions (e.g. in Venice), conferences, edited volumes, new archival finds or document re-examinations (e.g. Polo's 1324 will, the inventory of his possessions, family documents) and their findings.

4. THE OPEN QUESTIONS my essay lists. For each, say whether scholarship since 2013 has moved it, and how (name proponents and works):
 a. the stemma, and whether a single original can be recovered;
 b. the Hormuz route: did the Polos turn back at Hormuz on the way out, or is that Yule's inference?;
 c. Marco's claimed governorship of Yangzhou (Yanju) — what office, if any?;
 d. whether the Chinese record of the Ahmad assassination (1282) mentions a "Polo" (Bolad/Boluo misidentification);
 e. how much of the Yunnan, Burma (Mien) and Bengal material is autopsy and how much hearsay;
 f. whether Champa was visited on the return voyage;
 g. the Madagascar / Mogadishu confusion;
 h. where the "Book IV" material on the Golden Horde and Ilkhanate wars came from;
 i. the reliability of Ramusio-only passages;
 j. the Kinsay (Hangzhou) figures, e.g. 12,000 bridges and the circumference;
 k. the date of departure from China (1290, 1291 or 1292) and the evidence of the Yongle dadian notice naming Arghun's envoys (Cleaves);
 l. the "silences" (tea, foot-binding, the Great Wall, Chinese script, printing).

5. NEW APPROACHES. Global-history, Mongol-studies, Indian Ocean or digital-humanities work since 2013 that changes how Polo is read: e.g. work coming out of the Cambridge History of the Mongol Empire, the network/commerce literature, and Chinese-language scholarship (Yang Zhijiu's successors, Peng Hai, others).

Use these section IDs where relevant: III-12 (reliability essay), III-11 (reception and afterlives), III-10 (Polo's later life in Venice), I-01 (Genoa prison and composition), II-05 (Ahmad affair), II-11 (Yangzhou and the Xiangyang siege), II-13 (Hangzhou/Kinsay), III-09 (Cocachin and the return), I-07 (Kerman and Hormuz).

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [x] `research/results/S-13-raw.md` saved
- [x] `registry/scholarship.md`: one section per open question, plus "new since 2013" and "2024 anniversary"
- [x] III-12 open-questions list marked moved / unchanged / new
- [x] New works added to `registry/bibliography.bib`

## Feedback to plan
- `content-revision-plan.md` § W2 (III-12 row: works dated and post-2013 work added)
- `outline-volumes.md` III-12 programme, if a section needs adding (e.g. "since Vogel")

## Follow-up prompts
One follow-up, for an external tool with library access (the in-repo run could not open paywalled articles):

```text
Marco Polo studies, five narrow questions. For each, name the scholar, the work and where in it; say "not found" rather than guess; do not invent pages.
1. Since 2000, has anyone argued for or against the view (Yule's) that the Polos went down to Hormuz on the outward journey and turned back? Check Stephen Haw, Marco Polo's China (2006), and Qiu Zhirong, Lishi yanjiu 2021/1.
2. Did Polo call at Champa on the voyage home (1291–92), or only earlier? Who argues which?
3. Yang Zhijiu's 1290 notice of the envoys Uludai, Abishqa and Qoja: is it in the Yuan shi or in the Yongle dadian (Zhanchi section)? What date for the fleet's sailing do Cleaves (HJAS 36, 1976), Vogel (2013) and Haw (2006) each give?
4. Stephen G. Haw, "Anachronisms and Other Misunderstandings in Studies of Marco Polo", ZDMG 174/2 (2024): what are its main claims, and whom does it correct?
5. Which scholars hold that Polo's book had a single redaction (the passages found only in Z and Ramusio being original), against the multiple-redaction view of Burgio, Simion, Mascherpa and Andreose?
```

## Findings
**2026-11-11.** Raw: `research/results/S-13-raw.md`, with its BibTeX in `S-13-raw.bib`.

**How it was run.** In this repo, like S-12: web search, Crossref, and open-access PDFs read as text. It leans on five surveys written for or after the anniversary (Vogel and Theobald 2024; Orlando 2025; Ma Xiaolin 2025; Bolognari 2026; Gadrat-Ouerfelli 2026). **Caveats:** run and intake were one session, so the check below is not independent. Several publishers refused automated reading, so the Haw and Atwood articles and most monographs are known by record or abstract only. One survey (Gadrat-Ouerfelli) was read only through a fetch tool's summary and is not quoted.

**Trust check.** 57 works entered. For **39 a record or the text was opened, and all 39 exist** (181 confirmed in `sources.md`, up from 142). The other **18 are reports** by a source that was read (27 unconfirmed, up from 9); they may be named as "X, as Y reports" and never quoted. Two slips were found in a source and not copied: Ma 2025 gives Wood's title as *Was Marco Polo in China?* and places Yang's notice in the *Yuanshi* (F-15 says *Yongle dadian*; open, see the follow-up).

**What moved** (`registry/scholarship.md` has the positions and keys):
- **The debate:** specialists treat the presence as settled; no sceptic since 2013 was found; no new Asian document names the Polos. The question has become which layer of the text is whose.
- **Moved:** the stemma (a Genoa text, then a Venetian rewriting in stages; no agreed stemma); the languages (now a three-way dispute); the Ahmad names (settled: Bolod, and Cenchu/Vanchu are titles); Madagascar (it is Mogadishu); Ramusio-only passages (a lost fuller Z); Book IV and the Kinsay figures (a little); readership (a full study exists).
- **Unchanged:** Hormuz outbound, Yangzhou's office, Yunnan, Champa, the departure date (end of 1290 or early 1291, Yang Zhijiu), the silences.
- **New:** what Polo was in China (merchant-partner, guardsman or official); when the Genoa prison ended (a 2026 document); two doubted objects in the 1324 inventory.
- **Anniversary:** exhibition, five collective volumes, the *Codice Diplomatico Poliano*, new family documents (Agnese 1319; contracts of 1317), death day now 9 January 1324 for most.

**Written:** `registry/scholarship.md` (new); `registry/bibliography.bib` § "S-13 intake" (57 entries; `bolognari2021agnes` gains its issue and pages, still unconfirmed); `registry/sources.md` regenerated (220 entries).

## Decision
**2026-11-11.**
1. **III-12 states the consensus plainly** and adds a "since Vogel" close to §6. Wood's case stays in full. The open-questions list is re-marked as in `registry/scholarship.md` § Summary.
2. **Source rule for this material:** only sources marked *read* may be quoted; *record* and *via* sources are attributed and get no page. Five works are to be read before III-12 is rewritten (listed at the end of `scholarship.md`).
3. **No new section in the outline:** "since Vogel" closes §6; the nine sections stand (S-07).
4. **Feedback to plan, applied:** `content-revision-plan.md` § W2 (III-12 row) and the S-13 line; `outline-volumes.md` III-12 §6; `plans/README.md` board and decision log.
5. **Open, for the user:** (a) run the follow-up prompt above, or leave questions 3 and 7 marked unchanged; (b) whether `registry/facts.md` should take the three corrections this run suggests (F-35 towards 9 January; F-17 1309 or 1310; F-15 source name). They are noted in the task files, not applied to the sheet, because S-06 closed it without web research.

## Tasks to create on close
- `III-12.T1` (update the debate), `III-11.T1` (2024 reception), `III-B1.T1` (trivia), `I-01.T4` (composition Notes)
- **On close (2026-11-11):** no new task IDs. An "S-13 ✓" item was added to each of those four tasks, and to `III-10.T1`, `I-02.T1`, `II-05.T1`, `II-13.T4` and `III-07.T1`, which the findings also touch.
