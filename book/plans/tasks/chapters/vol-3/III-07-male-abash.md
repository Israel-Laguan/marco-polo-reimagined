# III-07 — Male and Female, Scotra, Madeigascar, Zanghibar, Abash

**File:** `vol-3/ch-07-male-abash.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,742 | 46% | — (missing; outline gives [R]) | ok (21/21) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription: 46% of narrative in 7-gram Yule runs (critique 8-gram 42%; threshold ≤ 25%). Fix: paraphrase at least half of each long run. — vol-3 C3 · ch-07

### Factual / fidelity
— see the Ramusio item below

### Dispute handling and Ramusio flags
- The Scotra whale hunt is Ramusian, narrated in the body and flagged only in Note [4]. Fix (W3): inline tag ("Ramusio's text adds…") plus "◇ Ramusio-only". — vol-3 M7 · ch-07:15, :63
- The Ruc: "'Tis said…" frames it, but there is no aside on the legend or the Aepyornis background. Fix: one-line dash aside. — vol-3 m6 · ch-07:27

### Voice and prose
- Formula opener "Marco Polo starts by narrating that…", copied straight from the voice-guide example (same in III-08, III-09). Fix: vary the opener (start on place or action). — vol-3 m14 · ch-07:9
- "Anyway" ×3 (:13, :25, :37) → at most one; "A quick note" (:13). Scorecard: 10 hinges. — vol-3 m14 · ch-07:13, :25, :37
- Recap closer "Thus the western wonder-run from Male and Female stands in this chapter…" with "it is enough that" and "one … breath". Fix: one bridging sentence or delete. — vol-3 M10 · ch-07:51

### Notes and apparatus
- Tag line missing; the outline gives [R]. Fix: add **[R]**. (Also W5: restore tag lines on III-7 to III-9.) — vol-3 M8 · ch-07:5-7
- ★ ×1 in Notes; convert to ✓ ~ ✗ ◇ ?. — vol-3 M9 · ch-07 Notes
- New trailing "**Comparative:**" block format (ch-07 to ch-10), unlike ch-01 to ch-06, which fold comparatives into numbered Notes. — vol-3 §3 rushed signals · ch-07:99

### Naming and gazetteer
- Redundant gloss "Champa (Champa / the Vietnam coast)"; also use the book form *Chamba*. — vol-3 n1 · ch-07:37
- Gazetteer `Abyssinia` vs the book's `Abash`. — vol-3 m4 · ch-07
- (Context only: :13 and Note [2] rightly refuse Male = Maldives; the fix sits in III-F2 and the gazetteer.)
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-07.T3`.
- **Pelliot contradicts the chapter (2026-10-22):** Polo's Madeigascar is **Mogadishu** in both name and description, not Madagascar mixed with Mogadishu. Pelliot, *Notes* II pp. 779–781, after Grandidier 1892; the modern name 'Madagascar' comes from Polo's misread form via Behaim's globe. Revise the narrative gloss and the Notes; the gazetteer row now points to Mogadishu. Source register: `research/results/GAZ-citable-findings.md`.

### Length and structure
— none found (2,742 words; scorecard: "Good disputes")

## Media hooks
- **Hero plate:** III-7 *The rukh carrying off an elephant* — **GEN** in the Persian *'aja'ib* idiom (al-Qazwini manuscripts), portrait; S-11 found no PD copy free for commercial use; caption: legend; Aepyornis — see `illustration-plan.md`. (Critique §4's ★ pick was a "Ruc feather" at Kublai's court — Ramusian and legendary; caption as a court curiosity.)
- **Secondary plates:** none in plan. Critique §4 options not adopted: Scotra whale hunt (Ramusian detail), the giraffe (not Madagascar)
- **Maps:** none placed here
- **Timelines / diagrams / tables:** critique §5 item 6 proposes a "Madeigascar vs Magadoxo" table (camels, elephants, sheikhs, giraffes, current) — not in the multimedia plan's D list; critique §5 item 2 links the monsoon diagram (C11) to ch-07:25 (Madagascar current: 20 days out, more than 3 months back)
- **Characters appearing:** the Soldan of Aden, the bishop of Abash (unnamed), St Thomas; comparative sources: Niccolò de' Conti, Fra Mauro, Ibn Battuta, Duarte Barbosa

## Gated by spikes
- S-01, S-02, S-03 (tag line, Ramusio flag, ★, Comparative block), S-04 (Abash, Chamba), S-06 (Ramusian whale hunt), S-08, S-09 (only if the C11 / Madeigascar table hooks are adopted), S-11 ✓ (hero moved to GEN)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-07.T5` Media placement (figures, captions) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `III-07.T6` Lint pass and human voice read

### III-07.T1 — Critical and factual fixes
- **Status:** backlog · **Depends:** S-06 ✓, `III-07.T3` (W2: applied in the re-voice pass)
- **Do:**
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - No claim here needed a verdict: each *Factual / fidelity* item cites its Yule line, so apply it as the backlog gives it.
  - Still-open rows use their hedge. When a library check settles one, update `registry/facts.md` first, then the chapter.
  - **S-13 ✓ (`registry/scholarship.md` Q8):** the Madeigascar Note: the chapter describes Mogadishu; the form is a copying error that Z alone escapes (`andreose2024textual`, read). Check Pelliot's wording before print.
- **Done when:** every item under *Factual / fidelity* (and each *Critical* item not owned by `.T3` or a `HOT` task) is applied, or hedged as `registry/facts.md` says; each corrected Note cites the source key given there; a person has checked the changed sentences against the sheet.

### III-07.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #33 (batch 9)
- **Now:** 2,692 words · 46% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 9 · archaisms 4 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :17 (81%), :19 (76%), :43 (83%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, :29, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :13 (94), :25 (127). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :21, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Madagascar → Madeigascar ×3, Socotra → Scotra ×2, Zanj → Zanghibar ×2, Baghdad → Baudas ×1, Pagan → Mien ×1, Champa → Chamba ×1, Coromandel → Maabar ×1, Maldives → Male and Female ×1 (+1 more); unglossed first mentions: Hormos, Cambaluc, Scotra, Abash, Esher, Dufar. `python3 tools/lint.py -v vol-3/ch-07-male-abash.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: none; unglossed first mentions: none. The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-07.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-07.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-07-male-abash.md` shows no `ramusio` errors, and the flag count matches the passages found.

### III-07.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-07.T3` (re-voice renumbers Notes)
- **Now:** 21 Notes · 1 ★ · 1 without a lead marker · tag none
- **Do:**
  - Add the missing tag line `**[R]**` under the epigraph (assigned in S-03; confirm against the chapter).
  - 1 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: [8] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-3/ch-07-male-abash.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-12 (2026-11-10):** "Huntingford" in the Comparative line (:99) has no work behind it. Candidates: *The Glorious Victories of ʿĀmda Ṣeyon* (Clarendon, 1965), which fits the Abyssinian chronology, or the *Periplus* (Hakluyt, 1980). Pick one and add it to the `.bib`, or drop the name.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

- **S-19 comparison intake (2026-11-12):** Use `plans/registry/comparanda.md` for this chapter’s checked witness locations and open leads. In the relevant Notes, say what each cited witness reports and give an edition-specific locator; verify lead passages before use, and omit unsupported comparisons. A public-domain quotation must be checked against the scan and attributed to the translation; BLD.T10 is pending. Do not treat shared subject matter as proof of Polo’s presence.

### III-07.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 20 errors · 2 warnings — failing: archaism, asides, budgets, markers, quote_verify, ramusio, scaffolding, tags, verbatim, you_must_know; warnings: ramusio, recaps
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-07-male-abash.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.

## S-21 source handoff

S-21 closed 2026-11-13 ([closure](../../../research/results/S-21-closure.md)). Apply in this file's chapter tasks: H10, H12. **Draft conflict (fixed 2026-11-17; re-voice must keep the fix):** `vol-3/ch-07-male-abash.md:15` gives the Socotra whale hunt as Polo's narration. Add the inline Ramusio flag and the “Ramusio-only.” Note label (S-03), citing Ramusio 1559 II fol. 57v (*bottesella*, a small floating cask; S21-E33). Ambergris origin: sperm-whale intestine, mechanism tentative (S21-E1). Roc: no elephant-bird or raffia causation.

## S-18 priority source handoff (2026-11-16)

Yule proposed the Aden/Adel identification and Yikunno Amlak c. 1278; keep these attributed. Tamrat p. 127 does not substantiate assigning the bishop story to Yagbeʾa Ṣeyon; Trimingham was subsequently read as noted below, while Pankhurst remains unread. See [intake](../../../research/results/S-18-priority-return-2026-11-16-intake.md).

**S-18 library follow-up:** Trimingham p. 69 and note 3 identifies the king as Yagbeʾa Ṣeyon (1285–94), with Aden meaning Adal, cautiously conditional on Polo; Yule proposed Yikunno Amlak c. 1278. Loiseau 2019 pp. 642–43 and 652–53 reports a 1290 embassy and cites Ibn ʿAbd al-Ẓāhir; the underlying Arabic remains unread and the embassy is not proven to be Polo’s bishop. See [source-check intake](../../../research/results/S-18-library-returns-2026-11-16-intake.md).

**S-18 translation follow-up (2026-11-17):** An online text extraction of Cook’s 2020 translation pp. 175–178 gives Ibn ʿAbd al-Ẓāhir’s account of the 1290 embassy and an envoy’s death at ʿAydhāb; note 280 suggests a connection to Polo. The chronicle passage itself does not identify Polo’s bishop or describe the alleged circumcision and war. Check a reliable edition image and the Arabic before relying on exact wording. See [intake](../../../research/results/S-18-targeted-archive-return-2026-11-17-intake.md).
