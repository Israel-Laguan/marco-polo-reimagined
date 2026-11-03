# S-24 — Citation and bibliography style

**Status:** decided 2026-10-22; pass A done; pass B waits on S-12 · **Timebox:** 1 session to decide + a scripted conversion in two passes · **Depends:** S-12 (bibliography keys, for pass B); S-08 (biblatex in the build) · **Gates:** every Note's citations; epigraph attributions; the back-matter bibliography; lint rules for citations

## Question
Which modern citation style replaces "cite modern scholars by well-known position"? How do we cite the base text, a 1903/1920 book that we read through a 2004 digitisation? And how do we convert the existing ~700 Notes with as little hand work as possible?

## Why it matters
- **There is no bibliography,** and citations come in many forms: "(Vogel; Haw; Rossabi)", "Larner, *Marco Polo and the Discovery of the World*", "Wood 1838", "Book I.lxi", "Book II.xii (Yule–Cordier)", "Prologue xvii–xviii". A reader can't look most of them up.
- **The base text is easy to mis-date.** It is the third edition of Yule's translation as revised by Cordier (John Murray, 1903), plus Cordier's *Notes and Addenda* (1920). We read it through Project Gutenberg eBooks 10636 and 12410. Those were released in 2004, and their catalogue pages show "last updated" dates in 2025. The citation must give 1903/1920; the digitisation is only how we accessed it.
- **One name can mean two people.** "Wood" is both the explorer John Wood (Oxus, 1838) and Frances Wood (1995). "May" is mostly the month and once in a while Timothy May. A careless conversion would merge them.
- **The LaTeX build (S-08) needs a mechanism** (biblatex). Without one the bibliography has to be kept by hand.

## Inputs
- Audit: `python3 tools/cite_audit.py` (run from `book/`)
- `registry/bibliography.bib` (seeded with the two base-text entries, verified)
- `VOICE-GUIDE.md` § Notes rules 2 and § Apparatus (lines 98, 150, 153)
- S-12 (keys for every scholar), S-19 (translations for the comparative witnesses), S-08 (build)

## Findings (audit, 2026-10-22)

`tools/cite_audit.py` over the 49 manuscript files (695 Notes):

| Form | Count | Conversion |
|---|---|---|
| Epigraph attributions: `Book II.xii (Yule–Cordier)` / `Book I, Of Baudas (Yule–Cordier)` / `…, Prologue (Yule–Cordier)` | 22 / 11 / 6 | script (pass A) |
| Epigraph attributions in free text ("Attributed to Polo on his deathbed…", "The book's habitual gasp…") | 12 | by hand: real locator, or *(adapted)* / *(tradition)* |
| Base-text locators `Book I.lxi` style | 55 | script (pass A) |
| "Book I" / "Prologue" without a chapter number | 49 / 71 | mostly prose, not citations; review by hand, convert only real citations |
| Scholars named without title or year | 304 | script with the S-12 name → key map (pass B) |
| Scholar + italic title / + year | 15 / 1 | script (pass B) |
| Ambiguous names: Wood 110 · May 23 · Jackson 8 · Morgan 4 | 145 | by hand, by context; the script only lists them |

The most-named sources: Wood 110 (both Woods), Larner 29, Vogel 29, Haw 26, Palladius 26, Pelliot 25, Pauthier 21, Gaubil 19, Rossabi 19, de Rachewiltz 18, Moule 17.

**Base text, verified 2026-10-22** (title pages in `refs/` + Project Gutenberg catalogue):
- *The Book of Ser Marco Polo, the Venetian, Concerning the Kingdoms and Marvels of the East*, trans. and ed. Henry Yule, 3rd ed. rev. Henri Cordier, 2 vols. (London: John Murray, 1903).
- Henri Cordier, *Ser Marco Polo: Notes and Addenda to Sir Henry Yule's Edition* (London: John Murray, 1920).
- Digitised as PG eBook 10636 (vol. 1; released 1 Jan 2004) and eBook 12410 (vol. 2 + the 1920 Addenda; released 1 May 2004). In the Gutenberg title pages the series is called "The Travels of Marco Polo: The Complete Yule-Cordier Edition". That is the digitisation's title, not the 1903 one.

## Proposed decision

1. **Style: *Chicago Manual of Style*, 18th ed. (2024), author-date, used inside the endnotes.** The body keeps only the `[n]` markers, so the storyteller voice is untouched. A Note reads "✓ … Vogel (2013) shows the salt figures match Yuan revenue records." Author-date is chosen over Chicago's notes-bibliography system because our Notes are already endnotes; that system would put footnote-style references inside them.
2. **The base text is cited by siglum.** `YC` = Yule–Cordier 1903; `YC Add.` = Cordier 1920. Locators are book.chapter in Arabic numerals: Book I, ch. LXI → **YC 1.61**; Prologue → **YC Prol. 17–18**; Yule's own note to a chapter → **YC 2.23 n. 4**. A *List of abbreviations* in the front matter explains the sigla and the Roman-to-Arabic mapping, so a reader can open the Gutenberg text at "CHAPTER LXI".
3. **Authoring syntax: Pandoc citation keys** in the Markdown: `[@vogel2013marco]`, `Vogel [-@vogel2013marco]`, `[@yc, 1.61]`. The `.bib` `shorthand` field makes the base text print as "YC 1.61". One source renders through two routes:
   - LaTeX: `biblatex-chicago` (authordate), one `refsection` per volume, and `\printbiblist{shorthand}` for the abbreviations;
   - previews and EPUB: `citeproc` with the Chicago author-date CSL.
4. **Page numbers:** the voice-guide rule stays. A page or section locator is added only after someone has seen it in the source. Book and chapter locators for primary texts are always fine.
5. **Epigraph attributions take one fixed, lintable form:** `> — Marco Polo, Book 2, ch. 12 (Yule–Cordier)`, i.e. readable words, not keys. Free-text attributions become a real locator, or end in *(adapted)* or *(tradition)*.
6. **Old books are cited by their print edition,** with the digitisation (repository, ID, URL) as the access route. A work is never dated by its upload or "last updated" date. This applies to Yule, and later to Pauthier, Palladius, Bretschneider, Baber, Bushell and everything S-19 adds to `refs/`.
7. **Bibliography placement:** a *Works cited* at the end of each volume, listing only the works cited in that volume. (Alternative: one consolidated list at the end of Vol. III. Decide with the user.)

## Method (once approved)
1. **Pass A (now, mechanical):** `tools/cite_convert.py --pass A` (dry run; `--apply` to write) converts epigraph attributions and `Book N.roman` locators to the new forms. Review the dry-run diff, apply, run the lint.
2. **Pass B (after the CIT research comes back):** the input is the four prompts in [`research/prompts/CIT-sources-and-epigraphs.md`](../research/prompts/CIT-sources-and-epigraphs.md). CIT-A to CIT-C list all 211 authorities named in the Notes, each with a context snippet. CIT-D sources the non-Polo epigraphs for HOT.1. Then the same script, using the resulting name → key map, converts unambiguous scholar mentions in the Notes to keys. It lists every ambiguous mention (Wood, May, Jackson, Morgan) with file and line; those are resolved by hand.
3. **Remainder:** during each chapter's W4 / `.T4`, any citation still not converted is done by hand. The lint enforces this from then on.
4. Extend the lint (S-02):
   - every `@key` exists in `registry/bibliography.bib`;
   - no `Book I.lxi`-style locators remain;
   - epigraph attributions match the pattern;
   - a scholar surname from the S-12 map without a key in a Note is a warning, and becomes an error after pass B.

## Output (definition of done)
- [x] Decision approved (style, sigla, epigraph form, bibliography placement)
- [x] `VOICE-GUIDE.md`: Notes rule 2 and § Apparatus rewritten for the new style
- [ ] `tools/cite_convert.py` (pass A ✓; pass B after S-12) and the lint rules ✓
- [ ] Pass A applied ✓; pass B applied after S-12; ambiguous list resolved
- [ ] Front-matter *List of abbreviations*; back-matter *Works cited* wired into the build (with S-08)

## Feedback to plan
- `VOICE-GUIDE.md` lines 98 and 153: "by well-known position only" becomes "by position, with a citation key; no unseen page numbers". Line 150: the base-text wording (already corrected 2026-10-22, see Findings).
- `FRONT-BACK-MATTER.md`: List of abbreviations; Works cited per volume
- `S-08` / `BLD`: biblatex-chicago, refsections, shorthand list; Pandoc `--biblatex` or a citeproc route
- `S-12`: owns the name → key map that pass B consumes; its citation-policy question is answered here
- `S-02` / `tools/lint.py`: the citation rules above

## Decision
**2026-10-22, approved by the user:** Chicago author-date in the Notes (proposal items 1–6 as written); epigraph credit `— Marco Polo, Book 2, ch. 12 (Yule–Cordier)`; *Works cited* at the end of each volume. Base-text keys are the sigla themselves (`yc`, `ycadd`).

**Pass A, applied 2026-10-22** (`tools/cite_convert.py --pass A --apply`):
- 30 epigraph credits converted, each book and chapter taken from where the quotation sits in Yule (not from the old credit). 1 Ramusio epigraph set by hand (III-10).
- 50 Roman locators in the Notes converted: 43 to `[@yc, …]`, 7 used inside sentences to `YC …`.
- Lint before and after: no file gained or lost an error; the passing count is unchanged.
- **Left for others:** 19 epigraphs whose quotation isn't in Yule's text; they are HOT.1's invented or misquoted epigraphs. After HOT.1 fixes a quotation, rerun pass A on the file and the credit sets itself. 7 Roman locators in narrative bodies ("Thus Book II.lx–lxv has done what it promised…") are recap scaffolding for the re-voice to delete.
- Lint rules added (`tools/cite_rules.py`): `cite_keys`, `roman_locators`, `epigraph_credit` (all errors).

**CIT intake, 2026-10-22** (raw: `research/results/CIT-A-raw.md`, `CIT-B-raw.md`, `CIT-C-raw.md`):
- **Spot check.** 9/9 Internet Archive identifiers exist; 3 are other editions than claimed (Larner 2001 pbk, Bretschneider 1910 reprint, Odoric = Chiesa 2002, not Yule). Open Library confirms 54/61 books; the misses are catalogue gaps, not invented works (old Hakluyt and Harvard series). Two years vary between records (Vogel 2012/2013, Pauthier 1865/1866).
- **Corrections to the tool:** it merged Moule into Moule–Pelliot (added `moule1957quinsai`, `moule1930christians`); it missed de Rachewiltz's 1997 rebuttal (added, unconfirmed); Allsen's hunt contexts need `allsen2006royal`.
- **Written:** 71 entries in `registry/bibliography.bib`, each with a status comment; `registry/name-keys.csv` maps all 211 names (28 key · 9 per-context · 138 via YC · 6 needs edition · 1 not a source · 29 pending).
- **Missing:** CIT-C rows 50–79 and its BibTeX block (the paste hit the 50,000-character limit); CIT-D not received. CIT-B gave only 8 BibTeX entries.
- **Roman pointers in narrative bodies (7, Vol. II):** all sat in closing recaps ("For the present it has done what Book II.xlv–l promised…"), which the voice guide already bans. Cut: the recap sentence in II-07, II-08, II-09; the whole recap paragraph in II-10, II-11, II-13, II-14. Each file loses its `roman_locators` error and, where flagged, its `recaps` error; no new errors.

**CIT-C (rows 50–79) and CIT-D intake, 2026-10-22:**
- CIT-C re-pasted complete; `results/CIT-C-raw.md` now holds all 79 rows. Spot check: 2/2 Internet Archive identifiers exist (Wood 1841, Salt 1814); 11/14 books confirmed in Open Library (misses: Timkowski, Groeneveldt, Gil 1986). The 2024 Bolognari article's DOI resolves.
- 18 more bibliography entries (91 in all). `name-keys.csv`: no names pending; 167 via YC, 28 key, 9 per context, 6 needs edition, 1 not a source.
- **CIT-D → four non-Polo epigraphs replaced with text found in `refs/`:** I-B1 deathbed line (Yule's English of Jacopo d'Acqui, Intro. § 37; the clause "for I knew I would not be believed" has no source and is gone); III-11 the Prologue's real statement of purpose, and Chipangu's "quantity of gold they have is endless" (YC 3.2) in place of the invented Columbus line, also fixed where the body reused it; III-12 the preamble verbatim, with "things seen as seen, and things heard as heard only"; III-B1 Mariana's "one Marco Polo, a Florentine Physician!" (Yule's Intro. § 74 n. 3) in place of the invented "Because of this book many set forth…". Columbus's actual postils need Gil 1986, which is not open; none is quoted.
- `epigraph_credit` now accepts "(c. 1330)".

**HOT.1 and pass B, 2026-10-22:**
- HOT.1: the 15 misquoted Polo epigraphs now quote Yule exactly; six that would duplicate another chapter's epigraph were swapped for other verified lines. No `epigraph_credit`, `roman_locators` or epigraph `quote_verify` errors remain.
- Pass B (`tools/cite_convert.py --pass B`): 105 mentions → `Name [-@key]`, 2 pure lists → `[@a; @b]`, in 49 Note lines. Converted only modern scholarship (rule `key`, plus per-context Wood/Moule/Allsen/de Rachewiltz/Morgan/Jackson); primary sources (Rubruck, Ibn Baṭṭūṭa, Pegolotti, Juvaini…) are reclassified via YC, since the Notes know them through Yule, not Gibb or Jackson. Lint unchanged (1,012 errors before and after; same files pass).
- Left for each chapter's `.T4`: `plans/status/pass-b-worklist.md` — 555 via-YC mentions (each needs its YC chapter), 7 needs-edition, 5 by hand (de Rachewiltz on Mongol administration ×2; Allsen with no topic ×3).

**Locating the 'via YC' mentions, 2026-10-22:** `tools/cite_locate.py` searches Yule's text case-sensitively, first in the Yule chapters that the manuscript chapter covers (from `outline-volumes.md`), then in Yule's Introduction, then elsewhere. Result for the 555 worklist mentions: 453 in range, 36 in the Introduction, 53 elsewhere in Yule, 13 not found. Yule cites most sources under his own spellings (Yuen-shi, Mêng-liang-lu, Yakut, De Sacy), which are now aliases. Five sources need outside research (`plans/research/prompts/CIT-batch-remaining.md`); the three translators (Boyle, Gibb, Thackston) and de Rachewiltz's translation take their modern keys.

**Batches A and B intake, 2026-10-22:**
- Five research items came back with partial answers. Batch A (Mengliang lu, Chuogeng lu): neither Chinese edition is confirmed; the translations named are Moule's and Gernet's English studies, and the free-copy URLs are not confirmed. Batch B (Marāṣid, Tsung tien, Columbus): the research output's references do not support its claims (e.g. one review cited for Rusconi's edition is about another book), so the citations are not used as evidence.
- Confirmed in Open Library: West–Kling 1990 (catalogue shows 1991; check the imprint). Not in Open Library: Rusconi 1994, Juynboll's Marāṣid, both Chinese editions. These are in the bibliography marked unconfirmed.
- Tsung tien is still unidentified and is not converted.

**Decisions round, 2026-10-22:**
- Columbus, West–Kling: **1991** (Open Library record; the 1990 date was wrong). Key renamed `columbus1991libro`.
- Rusconi, *Libro de las profecías*: research gives **1993** (not 1994). Not in Open Library; kept as claimed, key `columbus1993rusconi`.
- Juynboll, *Marāṣid al-iṭṭilāʿ*: research gives **1852–1864**, issued in parts (Leipzig and Heidelberg records). Not verified here; key `marasid1852`.
- *Mengliang lu*: research gives the 2015 Bashu shushe critical edition (Kan Haijuan, ed.). The cited OPAC record was unreachable, so it is claimed, not verified; key `wu2015mengliang`.
- *Nancun chuogeng lu*: research gives Zhonghua shuju, 1959. The cited OPAC records are unreachable or do not show the entry; claimed, not verified; key `tao1959nancun`.
- **Tsung tien**: the research called the source identified in *Ch'ue keng lu*, juan 21. The verdict is too strong. Yule's own note says only "of the Chinese authors", and the Chinese text the research quoted (zhonghuashu.com) did not respond. Bretschneider's text on Internet Archive has no Palm Hall passage. Verdict: **probable**. Name map: cited as Yule's note (YC 1.61), not as Palladius.

**Decisions round 2, 2026-10-22** (raw: `research/results/CIT-decisions-2-raw.md`; three tools on one prompt, only DeepSeek's answer had checkable records):
- **Palm Hall: identified.** The sentence 棕毛殿在假山東偏，三間，後盝頂殿三間 is in *Nancun chuogeng lu* juan 21 (宮闕制度), checked directly on Wikisource (Sibu congkan text), in the palace-garden passage beside the Jin Shui pool. Name map: `Tsung tien` → `tao1959nancun`, locator juan 21.
- **Rusconi 1993: confirmed.** The BnF record (ark:/12148/cb39245594j) showed 1993 and Rusconi before the server went down for maintenance. Qwen's "1997 Rusconi" substitute is not supported and is rejected.
- **Still claimed, not verified here:** Juynboll 1852–1864 (HathiTrust 403; volume count disputed between 6-in-5 and 3); *Mengliang lu* 2015 and *Nancun chuogeng lu* 1959 (Shanghai Library rate-limited, Academia Sinica and NCEPU unreachable). DeepSeek's records for these look sound but were not opened.
- Consensus found nothing; Qwen's references did not support its claims. Neither answer was used.

**By-products, 2026-10-22:** `registry/enrichment.md` § 1 collects what the citation research turned up beyond its questions (21 items: corrections, details, newer sources, free copies, locator systems). The main one is verified directly: the Palm Hall Palladius matched to Polo's Cane Palace is in **Dadu**, not Shangdu (*Nancun chuogeng lu* juan 21; attested 1311, rebuilt 1324–25 per *Yuan shi* juan 29), so the YC 1.61 identification fails; a Shangdu palm-fibre tower is attested by Sa Dula. Correction to the batch A/B intake: Gernet's 1958 review of Moule's *Quinsai* does exist (CrossRef).

**Pass C, 2026-10-22** (`tools/cite_locate.py --apply-via-yc --write`): 244 Note lines gain one sentence "As cited in Yule: Name, Name [@yc, n.n]; …", grouped by Yule chapter, for every via-YC mention the locator placed in the chapter's own range or in Yule's Introduction. Names only, no per-work keys: one surname can be two people (Baber = the emperor Babur in Vol. I, E. C. Baber in Vol. II; Major's Australia book, not his *India*), so keys are added per Note at each chapter's `.T4`. Excluded after a hand check: "Salt" in II-07 (the word), "Major" in III-01 (Major Sykes), "Relations" everywhere (a French book title). Left on the worklist: the 53 "elsewhere" hits, 13 not found, and the by-hand and needs-edition rows. Lint unchanged (1,012 errors before and after).

**Rewording, I-13:** the Cane Palace Note [4] and the aside it anchors no longer use Palladius's Palm Hall as confirmation; Note [4] now gives Sa Dula's palm-fibre tower and marks the Palm Hall match ✗ (Dadu, 1311, rebuilt 1324–25), citing *Nancun chuogeng lu* juan 21, *Mishujian zhi* juan 5 and *Yuan shi* juan 29 (new entries, texts read on Wikisource). The aside is one word shorter than before. No other chapter repeats the invented deathbed clause (E3 checked).

**Leads round, 2026-10-22** (raw: `research/results/CIT-leads-raw.md`; Perplexity and DeepSeek). Checked here:
- **Leeu edition: verified.** Gouda, between 1483 and 11 June 1484 (Glasgow and BnF records, dated from *HPT*); ISTC ip00902000, GW M34796. Goff's 1483–85 is the older dating. Applied in III-11 Note [6].
- **Postil hands: verified in outline.** Shawcross 2023 (*Medieval History Journal* 26.2: 376–424; CrossRef abstract): the notes are by Columbus and members of his circle, and his own notes fix on material things. Applied in III-11 Note [6]. The counts (c. 366, c. 98 by Columbus), the amanuensis and Hernando, and the two Chipangu notes on fol. 57v are claimed only (via Gil as reported in a review the intake could not open): `enrichment.md` E5a.
- ***Marāṣid*: verified** as an abridgment of Yāqūt (Open Library record; 6 tomes, which settles the volume count). Perplexity's advice to treat them as two witnesses is not taken: an abridgment is not independent corroboration. III-08 Note [8] now says so.
- **Chinese editions:** *Yuan shi* Zhonghua shuju 1976 and *Yanmen ji* Shanghai guji 1982 have Open Library records; *Mishujian zhi* (Gao Rongsheng, 1992) stays claimed. Added as addenda to the existing entries.
- **Chen Gaohua: verified** (Silkroad Press, 2015; ISBN in the *JEAL* review). New entries: `chen2015capital`, `steinhardt2015capital`, `gil1987libro`, `shawcross2023materiality`, `polo1484consuetudinibus`.

**Changed in plan docs:** `VOICE-GUIDE.md` § Notes rule 2, new § Citations, LaTeX apparatus table, § Base text; `FRONT-BACK-MATTER.md` § Apparatus generated by the build; `S-12` method step 4.

## Tasks to create on close
- **Created 2026-10-22, from the citation sweep:** `APP.T5` (a YC locator on every Note), `APP.T6` (per-work keys for the "As cited in Yule" names), `BLD.T5` (audit tool); spikes **S-25** (confirm the four unconfirmed works already cited) and **S-26** (chapter locators in the five most-cited modern books). **S-13** (scholarship since 2013) is the next Phase R run for the references.
- `BLD.T*`: `cite_convert.py`, lint rules, biblatex wiring
- `APP.T*`: List of abbreviations, Works cited pages
- Each chapter's `.T4`: residual citation conversion (checked by the lint)
