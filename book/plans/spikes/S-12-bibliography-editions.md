# S-12 — Master bibliography, editions and translations

**Status:** closed 2026-11-10 (one open choice: a *Further reading* page, see Decision) · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** `registry/bibliography.bib` (keys reused by S-13 … S-21); back-matter bibliography; `BLD` biblatex setup; the citation policy question below

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
- [x] `research/results/S-12-raw.md` saved
- [x] `registry/bibliography.bib` and `registry/sources.md`, with spot-check hit rate recorded
- [x] Name → key map for every scholar named in `vol-*/`; orphan names listed
- [x] Name → key map handed to S-24

## Feedback to plan
- `VOICE-GUIDE.md` § Notes rule 2, if the citation policy changes
- `FRONT-BACK-MATTER.md`: add the bibliography to the back matter
- `S-08` / `BLD`: biblatex style and `.bib` location

## Follow-up prompts
Not a search run: these need a library or a reader, not another prompt.
- **Gallica identifiers** for BnF fr. 1116 and fr. 2810 (gallica.bnf.fr blocks automated requests). Open both in a browser and record the ark in `registry/sources.md` via the `.bib`.
- **Huntingford, Elverskog, Subrahmanyam:** the Note's author picks the work, or the name goes (III-07, II-03, III-05 `.T4`).

## Findings
**2026-11-10.** Raw: `research/results/S-12-raw.md`.

**How it was run.** Most of Task A had already come back through the CIT runs of 2026-10-22 (S-24), whose 91 entries and 211-name map were in the registry. So this run covered only the gaps: Task B (modern editions), the Task C sources with no entry, Task A's missing names, and the six `needs-edition` names. It was run in this repo with web search and catalogue APIs (Open Library, CrossRef, NDL, publisher pages), not in an external tool. **Caveat:** the run and the intake were the same session, so the spot check below is not independent. It counts only rows backed by a record that was actually opened.

**Spot check: 25 of 25 works exist** (catalogue, DOI or publisher record); 22 of 25 have every field confirmed. The three gaps: Golas's year (1999 or 2000); Ricci 1931 (Viking issue seen, Routledge not seen); Marchisio as editor of the 2016 Odoric. Not counted: the two Gallica identifiers (site blocked). The prompt's "Simion and Burgio's work" is the digital Ramusio itself, not a separate edition.

**Written:**
- `registry/bibliography.bib` § "S-12 intake": **24 entries** (162 in all), each with a status comment. Task B: Ménard 2001–09, Eusebi–Burgio 2018 (F, open access, DOI), Burgio–Simion 2015 (digital Ramusio, open access, DOI), Bertolucci Pizzorusso 1975 (TA), Ronchi 1982, Barbieri 1998 (Z), Barbieri–Andreose 1999 (VA), Kinoshita 2016, Latham 1958, Cliff 2015, Ricci 1931. Task C: Dawson 1955 and Menestò et al. 1989 (Carpini), Marchisio 2016 (Odoric), Hammer-Purgstall 1856 (Wassaf). Task A: Bushell 1874 (DOI), Gaubil 1739, de Mailla 1777–85, Needham vols. 4.3 / 5.1 (Tsien) / 5.13 (Golas). Orphans: Schottenhammer 2001, Chen Dasheng 1984, Hsiao 1978. `biber --tool --validate-datamodel`: no warnings on the new entries (26 older warnings remain, mostly edited books typed `@book`).
- `registry/sources.md`: generated by `tools/sources_index.py` (key, citation, status, access link, chapters citing). 142 confirmed · 9 unconfirmed · 12 known (163 entries, after `needham1959mathematics` was added during pass B). Rerun it after any `.bib` change.
- `registry/name-keys.csv`: keys added for Bushell, Gaubil, De Mailla, Carpini, Wassaf, Odoric, Needham (now per volume); Schottenhammer, Chen Dasheng and Hsiao Ch'i-ch'ing moved from `needs-edition` to `key`; new rows **Yule**, **Cordier**, **Ramusio** (base text and Ramusio, rule `context`). 214 names.
- `tools/cite_convert.py`: a Needham context resolver (ships → 4.3, paper money → 5.1, coal → 5.13).

**Orphan names** (no work behind them; the Note's author picks one or drops the name): **Huntingford** (III-07; candidates: *Glorious Victories of ʿĀmda Ṣeyon*, 1965, or the *Periplus*, 1980), **Elverskog** (II-03), **Subrahmanyam** (III-05). "May" is not a scholar anywhere in `vol-*/`: all 23 hits are the month. The 39 `via-yc` names marked "no edition chosen" are cited through Yule (S-24 rule), so they are not orphans.

**Hand-off to S-24 (pass B): applied 2026-11-10 at the user's request.** 11 chapters, 17 citations; details and the tool fixes are in S-24 § Decision, "Pass B rerun".

## Decision
**2026-11-10.**
1. **Citation policy:** settled in S-24 (Chicago author-date, Pandoc keys, base text as YC). Nothing changes here; VOICE-GUIDE rule 2 was already rewritten there.
2. **Editions the Notes cite beside Yule–Cordier:** for the F text, **Eusebi–Burgio 2018**; for Ramusio-only passages, **Burgio–Simion 2015**, cited with the 1559 print. Both are open access. For an English reader: Moule–Pelliot 1938, then **Kinoshita 2016**. Ménard (Fr), Barbieri (Z), Barbieri–Andreose (VA) and Bertolucci Pizzorusso (TA) are cited only where a Note turns on that redaction. Proposal, applied by each chapter's `.T4`.
3. **Back matter:** *Works cited* per volume stays (S-24; already in `FRONT-BACK-MATTER.md` and wired by S-08). **Open, for the user:** whether to add a one-page *Further reading* to Vol. III using the 15 core works ranked in the raw file (Task D). Biblatex prints only the works cited, so the `.bib` itself needs no change either way.
4. **Feedback to plan:** `VOICE-GUIDE.md` (no change, done in S-24); `FRONT-BACK-MATTER.md` (no change unless item 3 is a yes); S-08/`BLD` (no change: biber reads `registry/bibliography.bib` already).
5. **Carried into the files that waited on it (2026-11-10):**
   - *Research:* `research/README.md` (S-12 closed; `sources.md` is generated; in-repo runs allowed, with the spot-check caveat).
   - *Spikes:* S-13 (prompt item 2 names the known editions), S-19 (citation editions already chosen; the prompt asks (a) only for the rest), S-20 (edition keys; Gallica IDs to check in a browser).
   - *Plan docs:* `content-revision-plan.md` W7; `FRONT-BACK-MATTER.md` (*Further reading* listed as not decided); `enrichment.md` E24.
   - *Cross tasks:* `APP.T4` (Ramusio citation proposal), `APP.T6` (new keys), `BLD.T1` (hook checks that `sources.md` is current).
   - *Chapter `.T4`s:* I-01 (F edition), II-03 (Elverskog), III-05 (Subrahmanyam), III-07 (Huntingford), III-11 (redaction editions), III-12 (core set, the outdated policy sentence at :93).

## Tasks to create on close
- `BLD.T*` biblatex wiring; `APP.T*` bibliography page; per-chapter `.T4` Notes citation pass (if the policy changes)
- **On close (2026-11-10):** none new. Biblatex is wired (S-08); *Works cited* and *Abbreviations* are `BLD.T4`/APP. The per-Note keying is `APP.T6`, whose scope now includes the S-12 keys (note added there). Pass B rerun: done (S-24).
