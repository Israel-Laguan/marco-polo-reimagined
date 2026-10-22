# I-08 — Cobinan, the Arbre Sec, and the Old Man of the Mountain

**File:** `vol-1/ch-08-arbre-sec-old-man.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,377 | 62% | — (n/a in Vol. I) | ok; [13] marker wrong | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Assassin dispute well handled"; ch-08:13 is cited as a model of flagging bracketed text.

### Critical
- Transcription share 62%. Worst block: the Old Man's garden. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: 3rd in Vol. I (after I-9). — vol-1 C3 · ch-08:27–35

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- "having refused the Ocean Sea at Hormos" states Yule's inference as the Book's decision (M2; Y:5902–5906). Fix: "Having brought the reader back from Hormos to Kerman…". Content plan W2 (I-8). — vol-1 M2 · ch-08:9

### Voice and prose
- Opener "Marco Polo narrates that…" (MPN). Fix: rotate openers. — vol-1 M6 · ch-08:9
- "Anyway" ×1 (1 "Anyway, next he…") — within budget; other hinges 11; book-voice tags 5–7 ("the book insists" budget ≤2). — vol-1 M6 · ch-08:23
- "as one movement of Book I… stand behind" is almost the same sentence as ch-09:47. — vol-1 M6 · ch-08:39
- Long dash-asides: 166 words (:23) and 138 words (:37). Fix: ~60–80 words each, one key fact + Note cross-ref. — vol-1 M11 · ch-08:23, :37

### Notes and apparatus
- Note [13] marks ✗ on "Marco personally visited Alamūt", a claim the Book never makes. Fix: "◇ report; Book says hearsay". — vol-1 m5 · ch-08:69
- Gazetteer reliability tags in Notes ("Gazetteer: Cobinan *likely_visited*", "Tonocain / Arbre Sec *uncertain*", "Old Man / Alamūt *reported_only*"). Fix: plain words. — vol-1 m6 · ch-08:49, :53, :57

### Naming and gazetteer
— none found

### Length and structure
— none found

## Media hooks
- **Hero plate:** I-8 The Dry Tree alone on the plain — GEN, LdM marvel lens, P. Must get right: a single *chinar* (oriental plane), half green and half white bark; passing caravan. Caption: legendary landmark (Alexander romance), "the book's Dry Tree". Anchor ch-08:21.
- **Secondary plates:** Garden of the Old Man (LdM; anchor ch-08:29): the **Crusader stereotype**, not Nizari practice; frame as legend.
- **Maps:** A4 Outbound: Ayas to Hormos (Kerman → Cobinan → Tun-o-Kain).
- **Timelines / diagrams / tables:** C6 Tutia furnace process (earth → furnace → grating catching zinc-oxide soot → slag/spodium; anchor ch-08:17); C15 Qanat cross-section (ch-08:13). B6 row "Hulagu's attack on the Old Man 1252 / 1262 vs 1256" (placed I-B1).
- **Characters appearing:** the Old Man of the Mountain (Aloadin), Hulagu (Alau), Rukn al-Dīn Khurshāh, Kitbuqa (Note), Alexander and Darius (legend), Marco Polo

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (✗ vs ◇ markers, Notes format)
- S-04 Gazetteer authority (A4 map hook)
- S-05 Character registry (Old Man in secondary plate)
- S-06 Fact verification sheet (M2 correction)
- S-08 LaTeX build pipeline (C6, C15, plates)
- S-09 Map and diagram pipeline (A4, C6, C15)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-08.T1` Critical and factual fixes
- `I-08.T5` Media placement (figures, tables, captions)
- `I-08.T6` Lint pass and human voice read

### I-08.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #17 (batch 5)
- **Now:** 2,402 words · 62% verbatim · "You must know" 0 · "Anyway" 1 · formula hinges 2 · archaisms 2 · Book first person 0 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :11 (80%), :27 (97%), :29 (87%), :31 (99%), :33 (84%), :35 (92%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :13, :35, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :23 (176), :37 (153). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :33; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-08.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-08.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-08-arbre-sec-old-man.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-08.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-08.T3` (re-voice renumbers Notes)
- **Now:** 13 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-08-arbre-sec-old-man.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-08.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 13 errors · 3 warnings — failing: archaism, asides, ramusio, scaffolding, verbatim; warnings: ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-08-arbre-sec-old-man.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
