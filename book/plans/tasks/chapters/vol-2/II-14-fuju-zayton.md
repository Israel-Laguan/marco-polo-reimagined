# II-14 — Fuju, Zayton, and the Haven of the World

**File:** `vol-2/ch-14-fuju-zayton.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,648 | 72% | [V/M] (undefined) | 7/7; Note [3] unverified claim; Note [6] overcorrects; "Gazetteer:" tooling in [5] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 72%, with 8 of the volume's 38 first-person Book lines (e.g. :57 "Let me tell you also…"). Scorecard: 9 hinges, "You must know" ×6. Fix: convert first-person Book lines to reported speech or marked quotation; keep Yule only as short marked quotations. — vol-2 C2, §3 · ch-14 (whole)

### Factual / fidelity
- **[M]** Tyunju porcelain overcorrected: the aside says the claim "will not stand" and points to Jingdezhen; Note [6] calls the locale "wrong". Yule–Cordier's itinerary list identifies Tyunju as Tek-hwa (Dehua, Fujian), a real Yuan porcelain centre exporting through Quanzhou; only the "sole source" claim is wrong. Fix: "Tyunju is probably Dehua, whose white wares really did go out through Zayton; what fails is only the boast that porcelain was made nowhere else — Jingdezhen was already greater." Also delete "Ramusian geography muddles rivers…", which is unsupported. — vol-2 M13 · ch-14:57–59, Note [6] ch-14:87; content plan W2 (II-14)

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged: :33 Unken sugar refined by "men of Babylonia" (Note [3] even says "Chinese local histories confirm", which is **(unverified)**); :55 "charming country"; tattooers for Upper India. Fix: two-to-four-word inline tag per paragraph plus "◇ Ramusio-only" in the matching Note; model ch-13:53. — vol-2 M1 · ch-14:33, :55, Note [3] ch-14:81; content plan W3

### Voice and prose
- **[M]** Drafting instructions in the prose: "tigers, as honesty restores" (:15); "Keep the charge as what the Book says; do not elevate it to fact." (:27). Fix: delete, keep only the substance. — vol-2 M3 · ch-14:15, :27; content plan W1.3
- **[M]** Outline-beat list pasted as the closing paragraph ("Thus Book II.lxxix–lxxxii has done what the departure from Heaven's city required…"). Fix: one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-14:71; content plan W1.3
- **[M]** Mid-chapter "So/Thus [place]…" restatements re-list the previous paragraph. — vol-2 M4 · ch-14:19, :37, :45
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-14 (whole)

### Notes and apparatus
- **[M]** Note [5] leaks tooling ("gazetteer *visited*"). — vol-2 M3 · ch-14:85
- **[m]** Tag [V/M] undefined (README and outline define only [V], [R], [M]). Fix: use [M] with a one-line gloss, or define compounds in front-01. — vol-2 m10 · ch-14:7

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Tanpiju, Vuju, Ghiuju, Changshan, Cuju, Unken, Tyunju. Fix example: "Vuju (Wuzhou, today's Jinhua) — not the Vuju (Huzhou) of the last chapter". — vol-2 M11 · ch-14:13 and first mentions
- **[M]** Vuju is used for two different cities: ch-12:65 (Huzhou) and ch-14:13 (Wuzhou/Jinhua, per Yule); front-02 lists only Huzhou. — vol-2 M11 · ch-14:13
- **[M]** No gazetteer rows for Tanpiju, Ghiuju, Changshan, Cuju, Kelinfu, Unken, Tyunju (blocks map A13). — vol-2 M11

### Length and structure
- W4 re-voice order: Vol. II batch position 4 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Zayton harbour: junks unloading pepper — GEN, Song–Yuan city-genre scroll, handscroll 3:1; must get right: Quanzhou ship type, Kaiyuan stone pagodas, Arab and Tamil merchants; caption: 100:1 ratio is rhetoric — see `illustration-plan.md`. Anchor ch-14:49 (Quanzhou ship excavated 1974, V-hull, 13 bulkheads; twin pagodas 1228–50; Qingjing mosque).
- **Secondary plates:** GEN Silkie fowls at Kelinfu (plan; anchor :31). Critique §4 candidate: tattooists for Indian visitors (:55). Existing `drawing-manzi-junk.png` named by critique for ch-14; the multimedia plan retires all `drawing-*.png`.
- **Maps:** A13 The Fujian road and Zayton (Kinsay → Tanpiju → Vuju (Jinhua) → Ghiuju → Changshan → Cuju → Kelinfu → Unken → Fuju → Zayton; Tyunju (Dehua) inset).
- **Timelines / diagrams / tables:** C7 Zayton cost stack (10% duty plus 30–44% freight = "half the investment"); C12 seagoing junk cutaway (placed in III-1, "preview in II-14"; critique: Quanzhou ship cross-section).
- **Characters appearing:** Marco Polo, Kublai (the Kaan); travellers and clerics discussed: Odoric, Ibn Battuta, Andrew of Perugia

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (compound tag, Gazetteer label, Ramusio flag style)
- S-04 Gazetteer authority and naming policy (glosses, two Vujus, missing rows)
- S-06 Fact verification sheet (Tyunju = Dehua; Note [3] "local histories" claim, unverified; 13 compartments)
- S-08 LaTeX build pipeline (plates, map, diagram, cutaway)
- S-09 Map and diagram pipeline (A13, C7, C12)
- S-10 Image generation pilot (GEN hero, secondary; C12 cutaway base)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-14.T1` Factual fix (Tyunju/Dehua)
- `II-14.T2` Ramusio flags (two passages; Note [3])
- `II-14.T4` Notes and apparatus normalisation
- `II-14.T5` Media placement (hero, secondary, A13, C7, C12 preview)
- `II-14.T6` Lint pass and human voice read

### II-14.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #4 (batch 1)
- **Now:** 2,635 words · 72% verbatim · "You must know" 6 · "Anyway" 3 · formula hinges 6 · archaisms 6 · Book first person 2 · asides 4
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :33 (99%), :41 (97%), :47 (94%), :49 (97%), :53 (93%), :67 (100%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :31, :33, :53, :55, :61, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :51 (90). Trim; move traveller/scholar lists to Notes.
  - Cut the closing recap :71 (86 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :19, :37, :45, :71; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-14.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-21, `plans/status/lint-baseline.md`):** 28 errors · 6 warnings — failing: archaism, asides, budgets, first_person, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: openers, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-14-fuju-zayton.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
