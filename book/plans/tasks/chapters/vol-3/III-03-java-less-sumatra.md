# III-03 — Java the Less: Ferlec to Fansur — Sumatran Kingdoms

**File:** `vol-3/ch-03-java-less-sumatra.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,202 | 64% | [V/M] | issues: Note [4] placeholder; Note [7] duplicates [6] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription: 64% of narrative in 7-gram Yule runs (threshold ≤ 25%); 6 archaisms in narrative (e.g. :13). Fix: paraphrase at least half of each long run, **especially ch-03:31–47** (named priority); archaic phrases only inside quotation marks. — vol-3 C3 · ch-03:31-47
- "Soft" label tic ×2: "Soft premise here:" (:13), "Soft close here:" (:51); also in Notes (:79, :91). Fix: strip the labels. — vol-3 C2 · ch-03:13, :51

### Factual / fidelity
— see the Ramusio item below (W2 lists it as a factual correction for III-3 and III-9)

### Dispute handling and Ramusio flags
- Ramusian matter absorbed as main text: the 2,000-man landing, ditches and stockade, and the "better than wine" coconut liquor are narrated as the Book's own words; in Yule all of it is a bracketed Ramusian insertion (`yule-vol2.txt:15996-16017`). :33 then calls it "the autobiographical hinge of Volume III's Sumatran run"; Note [10] says only "plausible castaway practice". Fix: add an aside, e.g. "— the stockade and the two thousand men come from Ramusio's fuller text, not the French; the five-month wait itself is in all versions [10]", and hedge Note [10] (mirror in III-09:25). — vol-3 M7 · ch-03:31, :33, :75
- Tailed men narrated with no inline aside (flagged only in Note [16]). Fix: "— a marvel the Archipelago had told since Ptolemy; perhaps a costume or a forest people misdescribed [16]". — vol-3 m6 · ch-03:43

### Voice and prose
- "Anyway" ×2 (:25, :39) → at most one. Scorecard: 7 hinges. — vol-3 m14 · ch-03:25, :39
- Recap closer "Thus the Sumatran kingdoms stand in order…". Fix: one bridging sentence or delete. — vol-3 M10 · ch-03:51
- Mid-chapter restatements ("So Ferlec stands as the hinge of Islam…", :19; :33). Fix: cut where an aside already exists. — vol-3 M10 · ch-03:19, :33

### Notes and apparatus
- ★ ×9; "★ Dispute" Note [7] repeats Note [6] (unicorn = rhinoceros). Fix: convert to ✓ ~ ✗ ◇ ? and merge [7] into [6]. — vol-3 M9 · ch-03:67-69
- Note [4] gives gazetteer status only ("Gazetteer: Ferlec *likely_visited*"), a placeholder; also matches the W0 scaffolding pattern `Gazetteer: *visited*`. Fix: give it content or drop the citation. — vol-3 m9 · ch-03:63

### Naming and gazetteer
- First-mention modern glosses missing in the body (only in Notes): Ferlec (Perlak) :15, Basma (Pasai) :21, Lambri (Lamuri) :41, Fansur (Barus) :45. — vol-3 m5 · ch-03:15, :21, :41, :45
- Gazetteer `Basman` vs chapter and Yule `Basma`. — vol-3 m4 · ch-03:21
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-03.T3`.

### Length and structure
— none found (2,202 words)

## Media hooks
- **Hero plate:** III-3 *Five months stranded at Samara* — GEN, Javanese / Sumatran relief, landscape; must get right: junks at anchor, toddy-tappers, monsoon sky, a **modest** camp; caption: stockade and 2,000 men are Ramusio-only — see `illustration-plan.md`
- **Secondary plates:** The "unicorn" split panel — LdM unicorn vs a Sumatran rhino (critique §4: the Sumatran rhino is hairy and two-horned; the Book says one horn — note the discrepancy). Critique §4 alternative not adopted: toddy-tapping (gomuti/sugar palm)
- **Maps:** none placed here (A16 shows the Samara wait as a Prologue-certain stage)
- **Timelines / diagrams / tables:** **C10** Pole Star altitude chart (III-3 / III-6; Sumatra "not seen" point, about 5°N); critique §5 item 2 links the monsoon diagram (C11) to the Sumatra wait
- **Characters appearing:** Marco Polo (detained five months at Samara), Kublai (Great Kaan), Cocachin (mentioned); comparative sources: Odoric, Ibn Battuta, Niccolò de' Conti, Duarte Barbosa, Rashid al-Din

## Gated by spikes
- S-01, S-02, S-03 (Ramusio flag style, Notes), S-04 (glosses, Basma), S-06 (Ramusian stockade correction), S-08, S-09 (C10), S-10

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-03.T1` Critical and factual fixes
- `III-03.T5` Media placement (figures, captions)
- `III-03.T6` Lint pass and human voice read

### III-03.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #28 (batch 7)
- **Now:** 2,189 words · 64% verbatim · "You must know" 2 · "Anyway" 2 · formula hinges 4 · archaisms 6 · Book first person 0 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :21 (98%), :23 (100%), :31 (84%), :37 (98%), :41 (98%), :47 (96%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :23, :31, plus any listed under *Dispute handling* above.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :19, :33, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Sumatra → Java the Less ×3, Samudra → Samara ×2, Perlak → Ferlec ×1, Pasai → Basma ×1, Nicobar → Necuveran ×1, Andaman → Angamanain ×1; unglossed first mentions: Chipangu, Pentam, Malaiur, Ferlec, Basma, Samara, Dagroian, Lambri, Fansur. `python3 tools/lint.py -v vol-3/ch-03-java-less-sumatra.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-03.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-03.T3` (the flags are written during the re-voice pass)
- **Now:** 5 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-03-java-less-sumatra.md` shows no `ramusio` errors, and the flag count matches the passages found.

### III-03.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-03.T3` (re-voice renumbers Notes)
- **Now:** 18 Notes · 9 ★ · 4 without a lead marker · tag [V/M]
- **Do:**
  - Replace tag `[V/M]` with `**[M]**` (compound tags are retired; if the lean matters, say it in one clause of Note [1]).
  - 9 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: [4], [7], [11], [14] (fill, merge or rewrite; none may be a placeholder or pointer).
  - "Dispute" label in Note(s) [7], [14], [16]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-3/ch-03-java-less-sumatra.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### III-03.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 37 errors · 6 warnings — failing: archaism, asides, budgets, markers, ramusio, scaffolding, tags, verbatim, you_must_know; warnings: names, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-03-java-less-sumatra.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
