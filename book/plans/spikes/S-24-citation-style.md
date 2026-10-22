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

**Changed in plan docs:** `VOICE-GUIDE.md` § Notes rule 2, new § Citations, LaTeX apparatus table, § Base text; `FRONT-BACK-MATTER.md` § Apparatus generated by the build; `S-12` method step 4.

## Tasks to create on close
- `BLD.T*`: `cite_convert.py`, lint rules, biblatex wiring
- `APP.T*`: List of abbreviations, Works cited pages
- Each chapter's `.T4`: residual citation conversion (checked by the lint)
