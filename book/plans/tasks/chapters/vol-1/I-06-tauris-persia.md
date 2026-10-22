# I-06 — Tauris, Persia of the Three Kings, and the Eight Kingdoms

**File:** `vol-1/ch-06-tauris-persia.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,753 | 58% | — (n/a in Vol. I) | ok; [4] repeats [1] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Good dispute work"; ch-06:13 and :39 are cited as models of flagging bracketed (Ramusian) text.

### Critical
- Transcription share 58%. Worst block: the Magi and fire tale. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: 5th in Vol. I (after I-5). — vol-1 C3 · ch-06:23–27

### Factual / fidelity
- "Istanit… half-legible through manuscript wear" in the body, but Note [12] gives the real reason (copyist *sf/st* confusion). Fix: align them. — vol-1 nit 3 · ch-06:33, :71
- Note [13] arithmetic: "livre tournois ≈ £1… → horse ~£193" (200 × £1 ≠ £193). Fix: cite Yule's £193 directly (Y:16596). — vol-1 nit 5 · ch-06:73

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- Opener: "The Book…" then "Marco Polo starts by narrating…" (SB). Fix: rotate openers. — vol-1 M6 · ch-06:9
- "Anyway" ×2 (2 "Anyway, next he…"); other hinges 5; book-voice tags 5–7. Lint budget ≤1. — vol-1 M6 · ch-06:15, :31
- Stock frames: "— A quick note on…" (:15); "Thus Chapter I-6 holds…" (:43) reads as help-desk meta. — vol-1 M6 · ch-06:15, :43
- Pet phrases: "factor's" (:11, :43), "shrug" (:43). — vol-1 M6 · ch-06:11, :43
- Long dash-aside: 127 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-06:31
- Commentary paragraph embedded in narrative: a Rashid al-Din panegyric inside the Tauris paragraph (Yule's notes moved into narrative). Fix: move name lists to Notes, keep one key fact. — vol-1 M11 · ch-06:11

### Notes and apparatus
- Note [4] repeats [1]. Fix: merge or give it content. — vol-1 m7 · ch-06:49, :55
- "Gazetteer: *visited*" production tags in Notes (and "gazetteer marks Tauris as visited" in body :15). Fix: keep the reliability idea in plain words. — vol-1 m6 · ch-06:49, :79

### Naming and gazetteer
- Chapter form **Yasdi** vs gazetteer **Yazd**. — vol-1 M8 · ch-06

### Length and structure
- Chapter-closing recap. Fix: one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-06:43

## Media hooks
- **Hero plate:** I-6 Marco questions the townsfolk at the Magi tombs of Saba — GEN, Ilkhanid (JT), L. Must get right: Ilkhanid brick domed tomb towers; Persian dress; puzzled townsmen. Caption: local tradition. Anchor ch-06:21.
- **Secondary plates:** none in `illustration-plan.md`. Critique-only: Fire falls into the well (ch-06:25; legend, illuminated-manuscript style); The Tabriz gem bazaar (ch-06:11; Ilkhanid Tabriz c. 1270s, Genoese merchants in the crowd).
- **Maps:** A4 Outbound: Ayas to Hormos (via-Tauris variant line, dashed).
- **Timelines / diagrams / tables:** D (I-6) Eight kingdoms of Persia: book name → identification → confidence (Yule's).
- **Characters appearing:** Marco Polo, the Three Magi (Jaspar, Melchior, Balthasar; legend), Hulagu (passing); the Ilkhan (unnamed)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format)
- S-04 Gazetteer authority (Yasdi; A4)
- S-05 Character registry (Marco in hero plate)
- S-06 Fact verification sheet (nit 3 Istanit, nit 5 £193)
- S-08 LaTeX build pipeline (D table, plate)
- S-09 Map and diagram pipeline (A4)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-06.T1` Critical and factual fixes
- `I-06.T5` Media placement (figures, tables, captions)
- `I-06.T6` Lint pass and human voice read

### I-06.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #19 (batch 5)
- **Now:** 2,702 words · 58% verbatim · "You must know" 1 · "Anyway" 2 · formula hinges 3 · archaisms 5 · Book first person 2 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :23 (100%), :25 (100%), :27 (100%), :35 (74%), :37 (82%), :41 (96%).
  - Asides over 80 words: :31 (132). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :43; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-06.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-06.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-06-tauris-persia.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-06.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-06.T3` (re-voice renumbers Notes)
- **Now:** 16 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - "Dispute" label in Note(s) [11]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-1/ch-06-tauris-persia.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-06.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 18 errors · 4 warnings — failing: archaism, asides, budgets, first_person, ramusio, scaffolding, verbatim, you_must_know; warnings: names, openers, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-06-tauris-persia.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
