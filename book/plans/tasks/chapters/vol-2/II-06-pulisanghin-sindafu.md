# II-06 — West and Southwest: Pulisanghin to Sindafu

**File:** `vol-2/ch-06-pulisanghin-sindafu.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,066 | 64% | [V] | 14/14; ★★ in Note [14]; "Gazetteer:" tooling in [3], [12], [14] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 64%; example :23–25 (the Golden King story). Hinge-heaviest chapter in the volume: 14 hinges, "You must know" ×1. Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-06:23–25

### Factual / fidelity
- **[N]** Note [3] says "Juju… ~30 miles west"; Zhuozhou lies south-west. — vol-2 N6 · ch-06:57

### Dispute handling and Ramusio flags
- — none found. (Scorecard: "Good stele and Acbalec handling". ch-06:29–31 and Note [8] correctly separate Cachanfu from Kenjanfu, and :33 makes the *silence* on the Nestorian stele its dispute hook; these are the reference for the M2 fix in II-F1/II-F2 and must survive the re-voice.)

### Voice and prose
- **[M]** Drafting instruction left in the prose: "flag it as such." Fix: delete, keep only the substance. — vol-2 M3 · ch-06:17; content plan W1.3
- **[M]** Recap padding: closes with "Here the chapter stops short of… For the present it has shown…". Fix: cut to at most one sentence or remove. — vol-2 M4 · ch-06:47
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-06 (whole)

### Notes and apparatus
- **[M]** Notes leak tooling: "Gazetteer: *…*" status labels in Notes [3], [12], [14]. — vol-2 M3 · ch-06:57, :75, :79
- **[M]** Outline star legend in Notes: Note [14] uses ★★. Fix: convert to ✓/~/✗/◇/?. — vol-2 M7 · ch-06:79; content plan W5

### Naming and gazetteer
- **[M]** No modern gloss on first mention in the body for Caichu, Cachanfu, Cuncun, Acbalec Manzi, Kian-suy. Fix: one-word glosses in the body. — vol-2 M11 · ch-06 (first mentions)
- **[M]** Gazetteer `book_name` "Tainfu" differs from the chapter's "Taianfu" (front-02 follows the gazetteer). Fix: align gazetteer to the Yule form the chapter uses, others as aliases. — vol-2 M11
- **[M]** No gazetteer rows for Kenjanfu, Caichu, Caramoran, Cuncun (blocks map A10); Acbalec Manzi's front-02 row is in the wrong (Manzi corridor) table. — vol-2 M11, M2

### Length and structure
- W4 re-voice order: Vol. II batch position 6 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Caravan crossing the Pulisanghin bridge — GEN, Yuan landscape / *jiehua*, handscroll 3:1; must get right: Jin bridge, 11 arches, archaic lions (many of today's lions are Ming/Qing re-carvings; Jin-built 1189–92); caption: Polo says 24 arches — see `illustration-plan.md`. Anchor ch-06:13.
- **Secondary plates:** GEN Roofed bridge market, Sindafu (plan; anchor :43, morning stalls, the Kaan's *Comercque* toll-house). Critique §4 candidate: gallery road of Cuncun (:35; plank road over a Qinling gorge).
- **Maps:** A10 The west road (Cambaluc → Pulisanghin → Juju → (Acbaluc) → Taianfu → Pianfu → Caichu → Caramoran crossing → Cachanfu → Kenjanfu → Cuncun → Acbalec Manzi → Sindafu; critique §5 map 1).
- **Timelines / diagrams / tables:** — none assigned
- **Characters appearing:** Kublai (the Kaan), Prince Mangalai (Mangala), Prester John and the Golden King (legend), Marco Polo, Ahmad (mentioned)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (★★, Gazetteer labels in Notes)
- S-04 Gazetteer authority and naming policy (glosses, Taianfu, missing rows)
- S-06 Fact verification sheet (Juju bearing)
- S-08 LaTeX build pipeline (plates, map)
- S-09 Map and diagram pipeline (A10)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-06.T1` Factual fix (N6)
- `II-06.T4` Notes and apparatus normalisation
- `II-06.T5` Media placement (hero, secondary, A10)
- `II-06.T6` Lint pass and human voice read

### II-06.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #6 (batch 2)
- **Now:** 3,022 words · 64% verbatim · "You must know" 0 · "Anyway" 3 · formula hinges 8 · archaisms 6 · Book first person 0 · asides 2
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :23 (74%), :31 (88%), :35 (74%), :37 (87%), :39 (87%), :43 (99%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :27, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (203), :33 (99). Trim; move traveller/scholar lists to Notes.
  - Cut the closing recap :47 (92 words) to ≤ 1 forward sentence.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)
