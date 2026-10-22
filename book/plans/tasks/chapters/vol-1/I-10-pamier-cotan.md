# I-10 — Pamier, Cascar, Samarcand, Yarcan, Cotan: Roof of the World to Jade Country

**File:** `vol-1/ch-10-pamier-cotan.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,740 | 51% | — (n/a in Vol. I) | ok | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** ch-10:31 correctly flags Chagatai's kinship error (uncle, not brother, to Kublai); I-07 should cross-reference it.

### Critical
- Transcription share 51%. Worst block: the Samarkand column. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: 7th in Vol. I (after I-13). — vol-1 C3 · ch-10:27–29

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- Ramusian (bracketed) text narrated as Book fact: wolves and horn cairns. Fix: 3–6-word tag ("Ramusio's text adds"), "◇ Ramusio" in the Note. — vol-1 M5 · ch-10:13

### Voice and prose
- Opener "Marco Polo narrates…" (MPN). Fix: rotate openers. — vol-1 M6 · ch-10:9
- "Anyway" ×2 (2 "Anyway, next he…"); other hinges 7. Lint budget ≤1. — vol-1 M6 · ch-10:17, :31
- Pet phrase "romance sky" ×2. — vol-1 M6 · ch-10:17, :57
- Longest dash-aside in the volume: **224 words**. Critique's rewrite: "— This is one of the book's great hits. Chinese pilgrims already called these heights 'midway between heaven and earth'; the giant sheep now bear Marco's name, *Ovis poli*; and at this altitude water boils so low that rice never softens. Only Ramusio's version makes the fire-notice hearsay. [5]" — vol-1 M11 · ch-10:17
- Long dash-aside: 149 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-10:31
- Commentary paragraphs embedded in narrative, listing travellers by name (Wood, Gordon, Younghusband, Timkowski, Johnson, Grenard…): ~280 words on jade, mut'a and Pein's site (:43); Bolor (:19). Scorecard: these "stall the climb". Fix: move name lists to Notes, keep one key fact. — vol-1 M11 · ch-10:43, :19
- "Wood" unqualified (John Wood, 1838). Fix: "Lt. John Wood" on first use. — vol-1 nit 9 · ch-10:17

### Notes and apparatus
- "Gazetteer: … *visited* / *uncertain*" production tags in Notes. Fix: plain words. — vol-1 m6 · ch-10:51, :55, :61, :73, :75, :81

### Naming and gazetteer
- Chapter forms **Vocan**, **Pamier**, **Cascar / Yarcan / Cotan**, **Pein** vs gazetteer Wakhan, Pamir, Kashgar / Yarkand / Khotan, Pem. — vol-1 M8 · ch-10
- Missing gazetteer rows: **Samarcand**, **Bolor** (A5 dotted side-places). — vol-1 M8 · gazetteer.csv

### Length and structure
— none found

## Media hooks
- **Hero plate:** I-10 Crossing the Pamier: wild sheep and a fire that won't cook — GEN, Persianate (JT), H. Must get right: *Ovis poli*; snow plateau. Caption: omit the horn cairns (Ramusio-only). Note: critique §4's ★ was "Horn cairns on the Pamir" (anchor ch-10:13) with the Ramusian caution; the illustration plan drops the cairns.
- **Secondary plates:** Jade gatherers of Cotan (anchor ch-10:39): wading gatherers, white and green jade boulders. Critique-only: The hanging column of Samarcand (ch-10:29; pious tale; Marco did not visit).
- **Maps:** A5 Balc to Pein (Wakhan → Pamir → Kashgar → Yarkand → Khotan → Pem); Samarcand and Bolor dotted.
- **Timelines / diagrams / tables:** none
- **Characters appearing:** Marco Polo, Kaidu (Caidou), Chagatai (Sigatay), Kublai

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style, Notes format)
- S-04 Gazetteer authority (Vocan, Pamier, Cascar, Yarcan, Cotan, Pein; missing rows; A5)
- S-08 LaTeX build pipeline (plates, A5 figure)
- S-09 Map and diagram pipeline (A5)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-10.T1` Critical and factual fixes
- `I-10.T5` Media placement (figures, tables, captions)
- `I-10.T6` Lint pass and human voice read

### I-10.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #21 (batch 6)
- **Now:** 2,783 words · 51% verbatim · "You must know" 0 · "Anyway" 2 · formula hinges 4 · archaisms 5 · Book first person 0 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :13 (99%), :21 (77%), :27 (97%), :29 (100%), :35 (96%), :39 (87%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :13, :33, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (238), :31 (156). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :37; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-10.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-10.T3` (the flags are written during the re-voice pass)
- **Now:** 5 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-10-pamier-cotan.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-10.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-10.T3` (re-voice renumbers Notes)
- **Now:** 17 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - "Dispute" label in Note(s) [12]: drop the label, merge into the Note of its anchor, or give it `?` plus a sentence on what is contested.
  - Run `python3 tools/lint.py -v vol-1/ch-10-pamier-cotan.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-10.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 27 errors · 8 warnings — failing: archaism, asides, budgets, markers, ramusio, scaffolding, verbatim; warnings: names, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-10-pamier-cotan.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
