# I-11 — Charchan, Lop, Tangut, Camul: Desert Voices and the Edge of Cathay

**File:** `vol-1/ch-11-lop-tangut.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,741 | 46% | — (n/a in Vol. I) | ok | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Strong marvel handling (asbestos)". Measured verbatim is 46% here; the critique's C3 table prints 47%.

### Critical
- Transcription share 46%. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: after I-4, before I-3. — vol-1 C3 · ch-11

### Factual / fidelity
- Great Wall "seed": "Suhchau sits just within its extreme north-west angle" is Yule's 19th-century phrasing (Y:24254) and implies the Wall stood there in the 1270s. The masonry Wall at Suzhou/Jiayuguan is **Ming** (Jiayu Pass fort 1372); in Polo's day the Hexi defences were eroded Han-era earthworks. Fix: add "…though the brick-and-stone Wall a modern reader pictures there is Ming, a century after Polo; in his day only eroded earthen ramparts of the Han ran along the Hexi road." Content plan W2 (I-11). — vol-1 M7 · ch-11:43

### Dispute handling and Ramusio flags
- The Wall seed leaves out the main counter-argument to Wood; the text gives only "a merchant itinerary need not chorograph every landmark" (see M7 fix above). — vol-1 M7 · ch-11:43
- Ramusian (bracketed) text narrated as Book fact: the phantom cavalcade (:15; Y:22948 "[Sometimes the stray travellers will hear… cavalcade…]"), caravan bells and night signal (:19), Camul's three years of crop failure (:29), the hoof-poisoning plant (:37). Load-bearing: the Lop cavalcade and bells, the Camul crop failure. Fix: 3–6-word tag ("Ramusio's text adds", "one version adds"); mark matching Notes "◇ Ramusio". — vol-1 M5 · ch-11:15, :19, :29, :37

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB); "starts by" is wrong outright here, as he is not starting. Fix: rotate openers. — vol-1 M6 · ch-11:9
- "Anyway" ×4 (1 "Anyway, next he…"); other hinges 9. Lint budget ≤1. — vol-1 M6 · ch-11:17, :25, :31, :35
- Stock frame "— A quick note on…". — vol-1 M6 · ch-11:31

### Notes and apparatus
- Gazetteer reliability tags in Notes (*likely_visited*, *visited*, *reported_only*). Fix: plain words. — vol-1 m6 · ch-11:49, :51, :65, :75, :77

### Naming and gazetteer
- Chapter form **Sukchur** vs gazetteer **Succiu**. — vol-1 M8 · ch-11
- Missing gazetteer rows: **Sachiu/Dunhuang** (a main stop here), **Chingintalas**. — vol-1 M8 · gazetteer.csv

### Length and structure
- Chapter-closing recap. Fix: one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-11:43
- Scorecard: outline coverage "Full; Wall seed half-argued" (see M7). — vol-1 §3 · ch-11

## Media hooks
- **Hero plate:** I-11 The straggler hears spirit voices in the Lop desert — GEN, **Dunhuang Mogao murals** (Yuan caves 3 and 465), L. Must get right: night dunes; lone rider; phantom caravan faint. Caption: folklore; "cavalcade" is Ramusio. Anchor ch-11:15.
- **Secondary plates:** Reclining Buddha at Campichu (anchor ch-11:39), after the real Western Xia reclining Buddha at Zhangye's Dafo Si (1098). Critique-only: Asbestos cloth bleached in fire (ch-11:33; process vignette); Paper offerings burned at a Sachiu funeral (ch-11:23).
- **Maps:** A6 Lop to Chandu (I-11 – I-13); off-route Camul, Chingintalas.
- **Timelines / diagrams / tables:** D (I-7 / I-9 / I-11) Geographic text vs Ramusio (here: the Lop cavalcade). Critique §5 also proposes an asbestos-processing diagram (no C-ID assigned) and a "singing sands" soundscape (multimedia plan E: audio becomes the printed pronunciation glossary).
- **Characters appearing:** Marco Polo, Möngke (Mangu Kaan), Zurficar (Zu'lfikār), Kublai (passing), Chinggis (passing)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style, Notes format)
- S-04 Gazetteer authority (Sukchur, Sachiu, Chingintalas; A6)
- S-06 Fact verification sheet (M7 Ming Wall)
- S-08 LaTeX build pipeline (D table, plates)
- S-09 Map and diagram pipeline (A6)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-11.T1` Critical and factual fixes
- `I-11.T5` Media placement (figures, tables, captions)
- `I-11.T6` Lint pass and human voice read

### I-11.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #23 (batch 6)
- **Now:** 2,773 words · 46% verbatim · "You must know" 1 · "Anyway" 4 · formula hinges 4 · archaisms 7 · Book first person 0 · asides 4
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :27 (74%), :37 (79%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, :19, :37, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (108), :25 (87). Trim; move traveller/scholar lists to Notes.
  - Cut the closing recap :43 (137 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :43; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-11.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-11.T3` (the flags are written during the re-voice pass)
- **Now:** 4 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-11-lop-tangut.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-11.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-11.T3` (re-voice renumbers Notes)
- **Now:** 17 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-11-lop-tangut.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-11.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 30 errors · 2 warnings — failing: archaism, asides, budgets, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: ramusio, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-11-lop-tangut.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
