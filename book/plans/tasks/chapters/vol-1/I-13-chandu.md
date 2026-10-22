# I-13 — Chandu: Bamboo Palace, White Horses, Bacsi and Sensin

**File:** `vol-1/ch-13-chandu.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,576 | 58% | — (n/a in Vol. I) | ok; [5] ★ marker; [8] and [10] empty | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

**Status note:** scorecard "Good landing; cane palace correctly ★★★".

### Critical
- Transcription share 58%. Worst block: the Bacsi and Sensin. Fix: re-voice in the ch-01 manner, one or two short quoted lines per marvel; target ≤25%. W4 order: 6th in Vol. I (after I-6). — vol-1 C3 · ch-13:31–37
- Book-voice first person left in narration: "Now let us have done with this subject." Fix: reported speech or marked quotation (W0 lint: 0). — vol-1 C3 · ch-13:41

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB); "starts by" is wrong outright here. Fix: rotate openers. — vol-1 M6 · ch-13:9
- "Anyway" ×3 (2 "Anyway, next he…"); other hinges 8; book-voice tags 5–7. Lint budget: "Anyway" ≤1, "the book insists" ≤2. — vol-1 M6 · ch-13:17, :23, :27
- Commentary paragraph embedded in narrative: Daoists (lists of names; Yule's notes moved into narrative). Fix: keep one key fact + Note cross-ref; move names to Notes. — vol-1 M11 · ch-13:39

### Notes and apparatus
- Note [5] "✓★★★" mixes the outline's star legend into the ✓~✗◇? system. Content plan W5: convert ★ ratings. — vol-1 m5 · ch-13:57
- Note [10] is meta ("Dispute hook: … narrate… weigh the frame"); Note [8] is irrelevant (Vámbéry "grey horse", Kunkrat). Fix: merge or give them content. W0 lint also bans "dispute hook". — vol-1 m7 · ch-13:67, :63
- Gazetteer reliability tag in a Note ("gazetteer Shangdu *visited*"). Fix: plain words. — vol-1 m6 · ch-13:49

### Naming and gazetteer
- Chapter form **Chandu** vs gazetteer **Shangdu (Xanadu)**. — vol-1 M8 · ch-13
- Missing gazetteer rows: **Chagannor**, **Kemenfu/Kaipingfu**. — vol-1 M8 · gazetteer.csv

### Length and structure
- Chapter-closing recap. Fix: one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-13:41

## Media hooks
- **Hero plate:** I-13 Mare's-milk libation as the court leaves Chandu — GEN, Yuan court painting (YC), H. Must get right: white mares; shamans and lamas scattering milk; the court packing; cane palace being struck, with silk guy-cords and gilt dragon columns; Shangdu walls of rammed earth faced with brick and stone; Da'an Ge hall. Anchor ch-13:21.
- **Secondary plates:** Kublai with a leopard on his crupper (anchor ch-13:13; "strong, unusual and well-attested"). Critique-only: The cane palace braced with silk cords (ch-13:15; gilt dragon-wrapped columns, split-bamboo tile roof); The cups flying to the Kaan (ch-13:31; render as the book's claim and its stagecraft). Existing `drawing-chandu-palace.png` only half fits: its "marble palace" is a Renaissance arcaded villa and the cane hall an open bamboo scaffold with no dragons or cords; redraw against Shangdu archaeology (multimedia plan retires it).
- **Maps:** A6 Lop to Chandu (terminus); A8 Seasonal orbit (II-4 / I-13): Dadu ↔ Shangdu ↔ Cachar Modun, month labels, 28 August libation.
- **Timelines / diagrams / tables:** C16 Cane palace roof cutaway (split bamboo tiles). Critique §5 "Yuan seasonal migration" diagram is covered by A8.
- **Characters appearing:** Kublai (Cublay), Chinggis (privilege origin), Marco Polo

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★ vs ✓~✗◇? markers, Notes format)
- S-04 Gazetteer authority (Chandu, Chagannor, Kemenfu; A6, A8)
- S-05 Character registry (Kublai in secondary plate)
- S-08 LaTeX build pipeline (C16, plates, maps)
- S-09 Map and diagram pipeline (A6, A8, C16)
- S-10 Image generation pilot (GEN hero and secondary; C16 base)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-13.T1` Critical and factual fixes
- `I-13.T2` Ramusio flags and dispute asides
- `I-13.T4` Notes and apparatus normalisation
- `I-13.T5` Media placement (figures, tables, captions)
- `I-13.T6` Lint pass and human voice read

### I-13.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #20 (batch 5)
- **Now:** 2,617 words · 58% verbatim · "You must know" 2 · "Anyway" 3 · formula hinges 3 · archaisms 4 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (86%), :21 (91%), :25 (75%), :31 (90%), :33 (100%), :37 (95%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (107). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-13.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 18 errors · 2 warnings — failing: archaism, asides, budgets, markers, ramusio, scaffolding, verbatim, you_must_know; warnings: ramusio, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-13-chandu.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
