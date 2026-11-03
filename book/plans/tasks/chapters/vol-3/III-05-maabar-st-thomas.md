# III-05 — Maabar: Pearls, Suttee, Horses, and St Thomas

**File:** `vol-3/ch-05-maabar-st-thomas.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,805 | 38% | [R/M] | issues: Notes [13]/[15] out of step; [15] placeholder; [10] duplicates [8] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription: 38% of narrative in 7-gram Yule runs (threshold ≤ 25%). Fix: paraphrase at least half of each long run. — vol-3 C3 · ch-05
- The narrator says "I" as the Book: "I will tell you how they are got" (:11); "except what I am going to mention" (:19); "as I will relate" (:45). Fix: reported speech ("the Book promises to explain how they are got") or marked quotation. — vol-3 C3 · ch-05:11, :19, :45
- "Soft" label tic ×3: "Soft turn now:" (:17), "Soft rise now:" (:43), "Soft close here:" (:51); also Notes [15] (:85) and :93. Fix: strip. — vol-3 C2 · ch-05:17, :43, :51

### Factual / fidelity
— see the Ramusio item below

### Dispute handling and Ramusio flags
- The *Pacauta* prayer is narrated unflagged; in Yule it is bracketed Ramusio (`yule-vol2.txt:18737`). Fix (W3): 3–6-word inline tag plus "◇ Ramusio-only" in the Note. — vol-3 M7 · ch-05:19
- Marvels with no inline aside, flagged only in Notes: suttee (:23, :31) and the St Thomas miracles and martyrdom (:45-49). Fix: a one-line dash aside for each. — vol-3 m6 · ch-05:23, :31, :45-49
- Outline dispute hook not inline: the dislocation of the Indian chapter order appears only in Note [1] (III-06 handles it inline at :39, :49). Fix: half a sentence here or a forward pointer. — vol-3 m7 · ch-05:57

### Voice and prose
- "Anyway" ×3 (:21, :29, :37) → at most one. Scorecard: 6 hinges. — vol-3 m14 · ch-05:21, :29, :37
- Recap closer "Thus the western run from Seilan stands in this chapter…" with "it is enough that" and "one … breath". Fix: one bridging sentence or delete. — vol-3 M10 · ch-05:51
- Mid-chapter pre-summary. Fix: cut where an aside already exists. — vol-3 M10 · ch-05:17
- Keep: the economics aside (scorecard: "Good economics aside"). — vol-3 §3 scorecard

### Notes and apparatus
- Notes out of step with the body: body [13] (:35, washing, right hand, sureties, debt rule) is answered by Note [13] (:81), which discusses rain, omens and 13-year-old boy traders — the content of body [15]; Note [15] (:85) is a placeholder, "Soft bridge toward consecrated damsels". Fix: swap the contents and write a real [15]. (Also W5 Notes hygiene.) — vol-3 m8 · ch-05:35, :81, :85
- ★ ×9; "★★★ Dispute" Note [10] repeats Note [8] (horse imports). Fix: convert to ✓ ~ ✗ ◇ ? and merge. — vol-3 M9 · ch-05:71, :75

### Naming and gazetteer
- Maabar (Coromandel) is not glossed until :45. — vol-3 m5 · ch-05:11, :45
- Gazetteer lacks rows for Mailapur (St Thomas) and Kis (Qais). — vol-3 m4 · ch-05
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-05.T3`.

### Length and structure
— none found (2,805 words)

## Media hooks
- **Hero plate:** III-5 *Pearl divers and the shark-charmer* — GEN, Chola temple mural, landscape; Gulf of Mannar boats, stone weights, Brahman charmer on deck; caption: the charm is belief. This is **Pilot 3** of the illustration plan — see `illustration-plan.md`
- **Secondary plates:** Arab horses landed in Maabar (critique §4: stitched Indian Ocean boats; Persian Gulf merchants). Critique §4 option not adopted: pilgrims take the red earth at Mailapur (miracle cures are cult claims)
- **Maps:** **A17** Polo's order vs the coast's order (III-5 / III-6; critique §5 item 3)
- **Timelines / diagrams / tables:** critique §5 item 2 links the monsoon diagram (C11) to ch-05:39 (rains June–August). Glossary: Abraiaman, *Pacauta*
- **Characters appearing:** Sonder Bandi Davar (Sundara Pāṇḍya), the five royal brothers (unnamed), St Thomas the Apostle; comparative sources: Rashid al-Din, Ibn Battuta, Duarte Barbosa, Odoric, Niccolò de' Conti, Montecorvino

## Gated by spikes
- S-01, S-02, S-03 (Ramusio flag, Notes swap, ★), S-04 (Maabar gloss, Mailapur/Kis rows, A17), S-06 (Pacauta fidelity), S-08, S-09 (A17), S-10

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-05.T1` Critical and factual fixes
- `III-05.T5` Media placement (figures, captions)
- `III-05.T6` Lint pass and human voice read

### III-05.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #34 (batch 9)
- **Now:** 2,766 words · 38% verbatim · "You must know" 3 · "Anyway" 3 · formula hinges 4 · archaisms 3 · Book first person 4 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :11 (86%), :15 (83%), :27 (74%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :13, plus any listed under *Dispute handling* above.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :17, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Kis → Kisi ×2, Hormes → Hormos ×2, Ceylon → Seilan ×1, Coromandel → Maabar ×1, Dofar → Dufar ×1; unglossed first mentions: Seilan, Maabar, Mailapur, Mutfili, Cail, Kesmacoran. `python3 tools/lint.py -v vol-3/ch-05-maabar-st-thomas.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: none; unglossed first mentions: none. The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-05.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-05.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-05-maabar-st-thomas.md` shows no `ramusio` errors, and the flag count matches the passages found.

### III-05.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-05.T3` (re-voice renumbers Notes)
- **Now:** 19 Notes · 9 ★ · 4 without a lead marker · tag [R/M]
- **Do:**
  - Replace tag `[R/M]` with `**[M]**` (compound tags are retired; if the lean matters, say it in one clause of Note [1]).
  - 9 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: [4], [6], [10], [15] (fill, merge or rewrite; none may be a placeholder or pointer).
  - "Dispute" label in Note(s) [7], [10], [17]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-3/ch-05-maabar-st-thomas.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-05.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 35 errors · 3 warnings — failing: archaism, asides, budgets, first_person, markers, ramusio, scaffolding, tags, verbatim, you_must_know; warnings: names, recaps
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-05-maabar-st-thomas.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
