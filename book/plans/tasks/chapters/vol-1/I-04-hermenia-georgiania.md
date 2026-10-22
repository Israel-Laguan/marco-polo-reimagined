# I-04 — Lesser and Greater Hermenia; Turcomania; Georgiania

**File:** `vol-1/ch-04-hermenia-georgiania.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,375 | 49% | — (n/a in Vol. I) | orphan Note [15] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Heavy Yule transcription: 49% of narrative words inside verbatim 7-gram runs. Fix: re-voice in the ch-01 manner; target ≤25%. W4 order: after I-10, before I-11. — vol-1 C3 · ch-04

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- Ramusian (bracketed) text narrated as Book fact: the Paipurth silver mine. Fix: 3–6-word tag ("Ramusio's text adds…"), "◇ Ramusio" in the matching Note. (ch-04:31 "some texts add" is cited as a good model.) — vol-1 M5 · ch-04:19

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB). Fix: rotate openers. — vol-1 M6 · ch-04:9
- "Anyway" ×2 (1 "Anyway, next he…"); other hinges 5. Lint budget ≤1. — vol-1 M6 · ch-04:17, :25
- Pet phrases flagged series-wide: "shrug", "factor's". — vol-1 M6 · ch-04:13, :37
- Long dash-aside: 136 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-04:17

### Notes and apparatus
- Orphan Note [15] ("Whole Caucasian block personally traversed"): body cites [1]–[14] only, last marker [14] at line 35. Fix: at ch-04:37, "…is a question the notes must keep open. [15]". Content plan W5. — vol-1 M10 · ch-04:71

### Naming and gazetteer
- "Mosul (Mausul)" reverses the book-form-first rule. — vol-1 nit 2 · ch-04:21
- Chapter forms **Savast**, **Arzinga / Arziron** vs gazetteer Sivas, Erzincan / Erzurum. Fix: gazetteer book_name to Yule forms. — vol-1 M8 · ch-04
- Missing gazetteer rows: **Derbend**, **Ararat**, **Conia**, **Casaria**. — vol-1 M8 · gazetteer.csv

### Length and structure
- Chapter-closing recap lists what was just read. Fix: keep one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-04:37

## Media hooks
- **Hero plate:** I-4 The quay at Layas — GEN, Cilician Armenian illumination, P. Must get right: sea castle; lateen ships; spice, silk and cotton bales; Italian and Armenian merchants; camels on the shore. Anchor ch-04:13.
- **Secondary plates:** none in `illustration-plan.md`. Critique-only candidates: oil fountain and mangy camels (ch-04:23; the Book puts it at the Georgian border, the real wells are at Baku: caption accordingly); Iron Gate at Derbend (ch-04:29; Sasanian walls to the Caspian; Alexander attribution is legend); Ararat with eternal snow (ch-04:21; no Ark).
- **Maps:** A4 Outbound: Ayas to Hormos (I-4 – I-8), two variant lines (via Tauris or via Mausul/Baudas), both dashed as reconstructions.
- **Timelines / diagrams / tables:** none
- **Characters appearing:** Marco Polo (as narrator), the Polos, David Melic (King David of Georgia), Baibars (Bundukdar), the Hetumid kings of Cilicia (dynasty), Alexander (legend)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style, Notes format)
- S-04 Gazetteer authority (Savast, Arzinga, Arziron; missing rows; A4)
- S-08 LaTeX build pipeline (plate, A4 figure)
- S-09 Map and diagram pipeline (A4)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-04.T1` Critical and factual fixes
- `I-04.T2` Ramusio flags and dispute asides
- `I-04.T4` Notes and apparatus normalisation
- `I-04.T5` Media placement (figures, tables, captions)
- `I-04.T6` Lint pass and human voice read

### I-04.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #22 (batch 6)
- **Now:** 2,330 words · 49% verbatim · "You must know" 1 · "Anyway" 2 · formula hinges 4 · archaisms 3 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (84%), :19 (74%), :21 (77%), :29 (72%), :31 (72%), :33 (76%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :21, :33, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (138), :25 (99). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :37; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-04.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 15 errors · 4 warnings — failing: archaism, asides, budgets, citations, ramusio, verbatim, you_must_know; warnings: names, ramusio, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-04-hermenia-georgiania.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
