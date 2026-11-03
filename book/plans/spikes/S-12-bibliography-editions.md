# S-12 — Master bibliography, editions and translations

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** `registry/bibliography.bib` (keys reused by S-13 … S-21); back-matter bibliography; `BLD` biblatex setup; the citation policy question below

## Question
What is the complete, correct citation for every work the manuscript names? Which modern critical editions and translations of the *Devisement* / *Milione* should a 2020s edition cite beside Yule–Cordier? And should the book move from "cite by well-known position" to short-form citations (author year) now that it will have a bibliography?

## Why it matters
- The book names about 25 modern scholars and a dozen primary-source translations, but never with a title, edition or year, apart from Wood (1995) and Vogel.
- The LaTeX target needs a `.bib` file. Without verified keys, every later spike would invent its own.
- The base text, Yule–Cordier, is over a century old. A reader who checks the references should find the current standard editions as well, e.g. the Ménard edition of the French text, the Eusebi edition of F, the digital Ramusio, and the newer English translations.

## Inputs
- Names cited in `vol-*/` (counts from a grep on 2026-10-22): Yule 205, Ramusio 165, Cordier 79, Odoric 67, Wood 58, Rashid 45, Rubruck 40, Larner 32, Vogel 31, Pelliot 28, Haw 28, May 23, Ibn Battuta 22, Rossabi 21, de Rachewiltz 21, Moule 20, Benedetto 14, Carpini 12, Wassaf 10, Critchley 8, Allsen 8, Jackson 4, Olschki 2, Juvaini 1. Also Needham, Morgan, Dutschke, Franke, Gaubil, de Mailla, Bushell, Steinhardt, Baber, de Groot, Pauthier.
- III-12 Notes [10]–[11] and the "Core comparative set".
- `VOICE-GUIDE.md` rules 98 and 153: cite by position; no fabricated page numbers.

## Method
1. Run the prompt below and save the output to `research/results/S-12-raw.md`.
2. Intake: run the trust checks (`research/README.md`), then write `registry/bibliography.bib` and `registry/sources.md`.
3. Map every name used in `vol-*/` to a key. List the names that have no work behind them; they must get one or be dropped.
4. The citation policy itself is decided in **S-24** (proposed: Chicago author-date in the Notes, Pandoc citation keys, base text by siglum). This spike supplies the name → key map that S-24's pass B consumes.

## Deep research prompt

```text
I am preparing a new three-volume English retelling of Marco Polo's book (the Devisement dou monde / Il Milione) for print. The working base text is Henry Yule's translation, 3rd edition revised by Henri Cordier (1903), with Cordier's Notes and Addenda (1920). The retelling's endnotes cite modern scholars only by name and position. I now need a proper, verified bibliography.

TASK A — Resolve these names to full citations. For each, give the work(s) most likely meant in a Marco Polo context (author, full title, publisher, place, year, edition; DOI or stable URL if any). Where a scholar has several relevant works, list the key ones and say which is the standard reference:
Yule & Cordier (The Book of Ser Marco Polo; and Cathay and the Way Thither); Cordier's 1920 Addenda; Ramusio (Navigationi et viaggi, vol. 2, 1559); Luigi Foscolo Benedetto (1928 critical edition; his English translation by Aldo Ricci); A. C. Moule & Paul Pelliot (Marco Polo: The Description of the World, 1938, incl. the Z/Zelada text); Paul Pelliot (Notes on Marco Polo); Leonardo Olschki (Marco Polo's Asia); John Larner (Marco Polo and the Discovery of the World); John Critchley (Marco Polo's Book); Frances Wood (Did Marco Polo Go to China?); Igor de Rachewiltz (his review/rebuttal of Wood; his Secret History translation); Stephen G. Haw (Marco Polo's China); Hans Ulrich Vogel (Marco Polo Was in China); Morris Rossabi (Khubilai Khan); Thomas T. Allsen (relevant monographs); Timothy May; David Morgan (The Mongols); Peter Jackson (The Mongols and the West); Joseph Needham (Science and Civilisation in China — which volumes are relevant to Polo's coal, paper money, ships, astronomy); Consuelo Wager Dutschke (dissertation on the manuscript tradition); Herbert Franke; Nancy Shatzman Steinhardt (Shangdu / Dadu); S. W. Bushell (Shangdu); Edward Colborne Baber; J. J. M. de Groot; Guillaume Pauthier (1865 edition); Antoine Gaubil; Joseph-Anne-Marie de Moyriac de Mailla; A. C. Moule (Christians in China before the Year 1550; Quinsai, with Other Notes on Marco Polo); F. W. Cleaves (on the Yongle dadian passage about the envoys of Arghun).

TASK B — Modern critical editions and translations of Polo's book. List and describe the current standard editions, including (verify, correct and extend this list): Philippe Ménard's multi-volume edition of the French version (Droz); Mario Eusebi's edition of the Franco-Italian F text; the Ramusio digital edition by Eugenio Burgio, Marina Buzzoni and Antonella Ghersetti (Ca' Foscari); Valeria Bertolucci Pizzorusso's Tuscan edition; Samuela Simion and Eugenio Burgio's work; Sharon Kinoshita's 2016 English translation; Ronald Latham's Penguin translation; Nigel Cliff's Penguin translation. For each: what text it represents (F, Fr, TA, VA, Z, P, R), year, publisher, and open-access status. Also name the main digital resources (manuscript databases, online editions, digitised manuscripts such as BnF fr. 1116 and fr. 2810).

TASK C — Standard translations of the comparative primary sources the book cites, with the edition a scholar would cite today: William of Rubruck; John of Plano Carpini; Odoric of Pordenone; Ibn Battuta; Rashid al-Din (Jami' al-tawarikh); Juvaini; Wassaf; the Secret History of the Mongols; Yuan shi (any translated sections relevant to Polo).

TASK D — Short guidance: in current Marco Polo scholarship, which 10–15 works are the indispensable core a general-reader edition's bibliography must include? Rank them, and give one line on why for each.

Label each row with the book section(s) where it matters when obvious (III-12 is the closing reliability essay; III-11 is reception; otherwise "general").

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-12-raw.md` saved
- [ ] `registry/bibliography.bib` and `registry/sources.md`, with spot-check hit rate recorded
- [ ] Name → key map for every scholar named in `vol-*/`; orphan names listed
- [ ] Name → key map handed to S-24

## Feedback to plan
- `VOICE-GUIDE.md` § Notes rule 2, if the citation policy changes
- `FRONT-BACK-MATTER.md`: add the bibliography to the back matter
- `S-08` / `BLD`: biblatex style and `.bib` location

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `BLD.T*` biblatex wiring; `APP.T*` bibliography page; per-chapter `.T4` Notes citation pass (if the policy changes)
