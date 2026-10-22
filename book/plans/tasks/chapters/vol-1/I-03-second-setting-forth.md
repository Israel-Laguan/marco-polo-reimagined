# I-03 — The Second Setting-Forth: Pope, Oil, and the Boy Marco

**File:** `vol-1/ch-03-second-setting-forth.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,621 | 34% | — (n/a in Vol. I) | ok [1–16] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard verdict "Strong; route handled honestly". ch-03:25 handles the Hormuz inference correctly ("Yule's reconstruction… not from Prologue itinerary") and is the reference for the M2 fixes elsewhere.

### Critical
- Transcription share 34%, above the ≤25% target. Fix: re-voice in the ch-01 manner; one or two short marked quotations per scene. W4 order: second-to-last in Vol. I. — vol-1 C3 · ch-03

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- Outbound route here (Yule's Ayas → Sivas → Mardin → Mosul → Baghdad → Hormuz, Y:5904) disagrees with front-02's via-Tauris line. Fix lands in I-F2 (present both as reconstructions); ch-03 is the correct side. — vol-1 m1 · ch-03:23

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB). Fix: rotate openers. — vol-1 M6 · ch-03:9
- "Anyway" ×4 (3 "Anyway, next he…") in 2.6k words; other hinges 4. Lint budget ≤1. — vol-1 M6 · ch-03:13, :21, :25, :33
- Stock frames: "— A quick note on…" (ch-03:13) and "Here the asides have to be honest" (ch-03:21). — vol-1 M6 · ch-03:13, :21
- Long dash-aside: 134 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-03:21

### Notes and apparatus
— none found

### Naming and gazetteer
- "Venice (Venezia)" and "Jerusalem (Yerushalayim)": gloss is noise when the book form is the English form. — vol-1 nit 1 · ch-03:9, :11
- Missing gazetteer row: **Kemenfu/Kaipingfu**; critique §5 also bolds **Jerusalem** as needing a row for the ch-03 map. — vol-1 M8 · gazetteer.csv

### Length and structure
— none found

## Media hooks
- **Hero plate:** I-3 "Sire, 'tis my son and your liegeman" — GEN, Yuan court painting (YC), L (tradition follows where the scene takes place). Must get right: Kaiping c. 1275; timber hall on a raised platform; oil flask and papal letters on a tray; Kublai about 60; Mongol and Chinese officials. Caption: Prologue theatre. Anchor ch-03:29.
- **Secondary plates:** Friars turn back at Layas (anchor ch-03:19): Dominican habit (white tunic, black *cappa*), the Templar Master, Ayas sea-castle, Cilician galley. Critique-only: Oil from the Sepulchre lamp (ch-03:11): Crusader-era rotunda; Jerusalem **under Mamluk control** in 1271, pilgrims tolerated.
- **Maps:** critique §5 ch-03 map: Acre ↔ Jerusalem, Ayas, then Yule's reconstructed route to Kemenfu, marked as a reconstruction. No dedicated A-ID in `multimedia-plan.md` (A3 is I-2; A4 starts at I-4).
- **Timelines / diagrams / tables:** D (I-3) The four scripts (Pauthier's list vs Yule's options vs scripts in use). B1 Polo family timeline (placed I-F1; critique: "front-01 or ch-02/03").
- **Characters appearing:** Marco Polo, Niccolò Polo, Maffeo Polo, Kublai (Cublay), Tedaldo Visconti / Gregory X, Clement IV (death), Baibars (Bundukdar), Friar Nicolas of Vicenza, Friar William of Tripoli, the Master of the Temple (unnamed), Cocachin (forward reference)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions
- S-04 Gazetteer authority (Kemenfu, Jerusalem rows; nit 1 gloss rule)
- S-05 Character registry (three Polos and Kublai in hero plate)
- S-08 LaTeX build pipeline (D table, plates)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-03.T1` Critical and factual fixes
- `I-03.T5` Media placement (figures, tables, captions)
- `I-03.T6` Lint pass and human voice read

### I-03.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #24 (batch 6)
- **Now:** 2,588 words · 34% verbatim · "You must know" 0 · "Anyway" 4 · formula hinges 6 · archaisms 3 · Book first person 0 · asides 4
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :31 (70%), :35 (78%), :37 (72%), :39 (96%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :39, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :13 (84), :21 (128), :25 (122), :33 (113). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :43; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-03.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-03.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-03-second-setting-forth.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-03.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-03.T3` (re-voice renumbers Notes)
- **Now:** 16 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-03-second-setting-forth.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-03.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 17 errors · 1 warnings — failing: archaism, asides, budgets, quote_verify, ramusio, scaffolding, verbatim; warnings: sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-03-second-setting-forth.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
