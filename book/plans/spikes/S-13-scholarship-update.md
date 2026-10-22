# S-13 — State of the field, 2013–2026

**Status:** open (next Phase R run for the references, per the 2026-10-22 citation sweep) · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** III-12 `.T1`/`.T4` (reliability essay), III-11, III-B1, I-01 Notes on composition; `registry/scholarship.md`

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

## Method
1. Run the prompt and save the output to `research/results/S-13-raw.md`.
2. Intake: trust checks; write `registry/scholarship.md` with one section per open question: positions, proponents and source keys. Add any new works to the `.bib`.
3. Mark each III-12 open question as *moved*, *unchanged* or *new*, and list the edits that follow for III-12 and III-11.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (Yule–Cordier translation as the base) with a closing essay on the book's reliability. The essay currently covers scholarship up to about 2013: Frances Wood, Did Marco Polo Go to China? (1995); Igor de Rachewiltz's rebuttal (1997); Stephen G. Haw, Marco Polo's China (2006); Hans Ulrich Vogel, Marco Polo Was in China (2013); plus John Larner (1999), John Critchley (1992), Pelliot, Moule–Pelliot (1938) and Olschki.

I need a rigorous survey of what has happened in Marco Polo studies from 2013 to today.

1. THE PRESENCE DEBATE. Arguments for and against Polo's presence in China published since 2013. Any new documentary evidence: Chinese, Persian, Mongol or Venetian sources newly identified, re-read or re-dated. Has a consensus formed? Who are the main voices now?

2. THE TEXT. New work on the manuscript tradition and the genesis of the text: the Franco-Italian F text, the role of Rustichello da Pisa, the Z (Zelada/Toledo) Latin version, Ramusio's sources, the Venetian VA tradition, Pipino's Latin. Include new critical or digital editions, and stemmatic findings.

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
- [ ] `research/results/S-13-raw.md` saved
- [ ] `registry/scholarship.md`: one section per open question, plus "new since 2013" and "2024 anniversary"
- [ ] III-12 open-questions list marked moved / unchanged / new
- [ ] New works added to `registry/bibliography.bib`

## Feedback to plan
- `content-revision-plan.md` § W2 (III-12 row: works dated and post-2013 work added)
- `outline-volumes.md` III-12 programme, if a section needs adding (e.g. "since Vogel")

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `III-12.T1` (update the debate), `III-11.T1` (2024 reception), `III-B1.T1` (trivia), `I-01.T4` (composition Notes)
