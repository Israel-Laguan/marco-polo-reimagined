# I-09 — Balc, Badashan, Pashai, Keshimur: Rubies, Azure, and High Valleys

**File:** `vol-1/ch-09-balc-badashan.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,119 | 65% | — (n/a in Vol. I) | ok; [16] meta | no (near the 3,200 ceiling) |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Badakhshan illness handled well"; ch-09:33 is cited as a model of flagging bracketed (Ramusio-only) text.

### Critical
- Transcription share 65%. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: 2nd in Vol. I (after I-7). — vol-1 C3 · ch-09
- Book-voice first person left in narration: "that I do not wish to do at present". Fix: reported speech or marked quotation (W0 lint: 0). — vol-1 C3 · ch-09:47

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- Ramusian (bracketed) text narrated as Book fact: the Bucephalus horse breed. Note [10] says Ramusio; the body is silent. Load-bearing item: add a 3–6-word tag ("Ramusio's text adds") and mark Note [10] "◇ Ramusio". — vol-1 M5 · ch-09:31, :71

### Voice and prose
- Opener: "Marco Polo narrates" in the first sentence (MPN). Fix: rotate openers. — vol-1 M6 · ch-09:9
- "Anyway" ×3 (3 "Anyway, next he…"); other hinges 9. Lint budget ≤1. — vol-1 M6 · ch-09:17, :27, :39
- "as one movement of Book I… stand behind" is almost the same sentence as ch-08:39; "without …" device (:21). — vol-1 M6 · ch-09:47, :21
- Commentary paragraph embedded in narrative: Kashmir Buddhism, listing travellers by name (Yule's notes moved into narrative). Fix: keep one key fact + Note cross-ref; move name lists to Notes. — vol-1 M11 · ch-09:45
- "Wood" unqualified (John Wood, 1838) in a volume that also cites Frances Wood. Fix: "Lt. John Wood" on first use. — vol-1 nit 9 · ch-09:17, :19, :31

### Notes and apparatus
- Note [16] is a meta summary. Fix: merge or give it content. — vol-1 m7 · ch-09:83
- "Gazetteer: … *visited* / *likely_visited*" production tags in Notes. Fix: plain words. — vol-1 m6 · ch-09:55, :57, :61

### Naming and gazetteer
- Chapter forms **Balc**, **Taican**, **Badashan** vs gazetteer Balkh, Talikan, Badakhshan. Gazetteer's Badakhshan alias "Balashan" is wrong; Yule's form is Badashan. — vol-1 M8 · ch-09
- Missing gazetteer rows: **Keshimur**, **Pashai**, **Casem**, **Dogana** (A5 needs them). — vol-1 M8 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-09.T3`.

### Length and structure
- Near the length ceiling (3,119 / 3,200). — vol-1 §3 scorecard · ch-09
- Chapter-closing recap. Fix: one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-09:47

## Media hooks
- **Hero plate:** I-9 The balas-ruby mines under royal seal — GEN, Ilkhanid (JT), L. Must get right: miners at Syghinan; Badakhshan highland dress (*postin*); oil lamps; officers sealing stones. Anchor ch-09:29.
- **Secondary plates:** none in `illustration-plan.md`. Critique-only: Marco convalescing on the high pasture (ch-09:33; **Ramusio only**, caption as such); Salt mountain at Taican (ch-09:19; market day); Ruins of Balc (ch-09:13).
- **Maps:** A5 Balc to Pein (Sapurgan → Balkh → Talikan → Casem → Badakhshan → Wakhan …); reported side-places dotted: Pashai, Keshimur.
- **Timelines / diagrams / tables:** D (I-7 / I-9 / I-11) Geographic text vs Ramusio (here: Marco's illness).
- **Characters appearing:** Marco Polo, Alexander and Darius (legend), Roxana (Note), Chinggis, Hulagu (passing)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style, Notes format)
- S-04 Gazetteer authority (Balc, Taican, Badashan, Balashan alias; missing rows; A5)
- S-05 Character registry (Marco in a candidate secondary plate)
- S-08 LaTeX build pipeline (D table, plate)
- S-09 Map and diagram pipeline (A5)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-09.T1` Critical and factual fixes
- `I-09.T5` Media placement (figures, tables, captions)
- `I-09.T6` Lint pass and human voice read

### I-09.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #16 (batch 4)
- **Now:** 3,150 words · 65% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 4 · archaisms 1 · Book first person 2 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :21 (71%), :23 (94%), :29 (78%), :31 (76%), :33 (76%), :41 (100%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :31, :43, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :39 (87). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :45; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Badakhshan → Badashan ×4, Kashmir → Keshimur ×4, Dry Tree → Arbre Sec ×1, Balkh → Balc ×1, Talikan → Taican ×1, Pamir → Pamier ×1, Tibet → Tebet ×1; unglossed first mentions: Taican, Pashai, Pamier. `python3 tools/lint.py -v vol-1/ch-09-balc-badashan.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-09.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-09.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-09-balc-badashan.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-09.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-09.T3` (re-voice renumbers Notes)
- **Now:** 16 Notes · 0 ★ · 1 without a lead marker
- **Do:**
  - Notes with no lead marker: [16] (fill, merge or rewrite; none may be a placeholder or pointer).
  - "Dispute" label in Note(s) [16]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-1/ch-09-balc-badashan.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-09.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 21 errors · 7 warnings — failing: archaism, asides, budgets, first_person, markers, ramusio, scaffolding, verbatim, you_must_know; warnings: names, openers, ramusio, recaps
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-09-balc-badashan.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
