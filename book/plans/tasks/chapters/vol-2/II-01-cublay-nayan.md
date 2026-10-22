# II-01 — Cublay Kaan: Puissance, Nayan, and the Ordo of Victory

**File:** `vol-2/ch-01-cublay-nayan.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,082 | 61% | [M] | ok (19/19); Note [1] "Soft landing" stub | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 61% of narrative words sit in 7-word strings verbatim in Yule (target ≤ 30% per critique; lint ≤ 25%). Examples: :11 "he is the most potent man… that existeth in the world, or ever hath existed from Adam" (word for word); :17 "waxed proud in the insolence of his youth… he would fain wrest the empire". Fix (critique's sample rewrite of :17): "Nayan, Polo says, was a young lord of about thirty who could put three hundred thousand horsemen in the field, and the power went to his head: he decided he would no longer be the Kaan's vassal, and sent to Caidu proposing they strike from two sides at once." Keep Yule only as short marked quotations, one or two per scene. Scorecard: 10 hinges ("starts by narrating", "he says", "according to the Book"…), "You must know" ×1; e.g. :11 "Marco Polo starts by narrating…". — vol-2 C2, §3 · ch-01:11, :17

### Factual / fidelity
- **[M]** Nayan's descent wrong: body says "great-great-grandson of Chinghiz's brother Belgutai". Yule's note says Uchegin (Temüge Otchigin), "called in the Chinese annals Pilgutai"; Cordier/Palladius add "Belgutai was Chinghiz's step-brother". The chapter merged the two. Fix: "…a great-great-grandson of Chinghiz's youngest brother Temüge Otchigin"; Note [5]: "Otchigin line (Yule's *Uchegin*; Chinese transcription confused with Belgutai)". — vol-2 M5 · ch-01:19, Note [5] ch-01:63; content plan W2 (II-1)

### Dispute handling and Ramusio flags
- **[m]** Aside over-reaches: "the Kaifeng synagogue tradition is later reception with thin medieval basis in Polo himself" muddles two points (the synagogue dates from 1163; the thinness is in Polo). Fix: "Polo's own allusions to Jews are slender, though others (Marignolli at Cambaluc, Ibn Baṭṭūṭa at Khansa) met Jewish communities." — vol-2 m15 · ch-01:35

### Voice and prose
- **[M]** Recap padding: chapter ends with a recap paragraph ("Thus the Ordo of Victory closes into the machinery of favour…"). Fix: cut to at most one sentence, or remove. — vol-2 M4 · ch-01:49
- **[M]** Aside-exit tic "Anyway, next he mentions X" (27 of the volume's 37 em-dash asides). Cap at one per chapter; vary exits ("Back to the road:", "The Book moves on to…", or simply resume). Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-01 (whole)
- **[N]** Abrupt scene jump: "And what next? The Kaan was there on the hill" (hill not introduced). Fix: "The Kaan took his stand on a rise, on a great wooden tower…". — vol-2 N9 · ch-01:25

### Notes and apparatus
- **[M]** Note [1] leaks tooling ("Soft landing" stub). Remove the label; keep substance. — vol-2 M3 · ch-01:55

### Naming and gazetteer
- — none found (Nayan theatre places Chorcha, Cauly, Barscol are "soft" per critique §5; see Media hooks)

### Length and structure
- W4 re-voice order: Vol. II batch position 8 of 14 after the II-2 pilot (by verbatim share). — content plan W4

## Media hooks
- **Hero plate:** Kublai on the elephant-borne tower at the Nayan battle — GEN, Yuan court (Liu Guandao manner), handscroll 3:1; must get right: Kublai about 72 and heavy, white *tug* standard, modest host; caption: spectacle numbers inflated — see `illustration-plan.md`. Anchor ch-01:25.
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: "Before the clash" (two hosts singing, *nakkara* kettledrums, :25); "Bloodless execution" (rolled felt, treat obliquely; method contested, :29); "Gerfalcon paiza bestowed" (surviving Yuan paiza, 'Phags-pa, :47).
- **Maps:** no A-ID assigned. Critique §5 map 5 "Nayan theatre" (Cambaluc → Liao/Nonni plain; Chorcha, Cauly, Barscol, soft) has no entry in `multimedia-plan.md`.
- **Timelines / diagrams / tables:** C5 Paiza hierarchy (silver → gerfalcon, script change 1269; II-1 / I-2); D table II-1 Nayan (kinship, year 1286 vs 1287, host size, sequel Qadaan). Pronunciation glossary entry for naccara/naqqāra (§E substitute for the critique's fiddle-and-kettledrum audio idea).
- **Characters appearing:** Kublai (Cublay Kaan), Nayan, Caidu (Kaidu), Chinghis Khan, Möngke, Belgutai / Temüge Otchigin (ancestry), Niccolò and Maffeo Polo (mentioned), Marco Polo, Rustichello ("a Pisan scribe"); travellers discussed: Rubruck, Monte Corvino, Marignolli, Ibn Battuta

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions
- S-05 Character registry (Kublai's age/appearance in hero; Nayan's descent)
- S-06 Fact verification sheet (Otchigin line; Kaifeng synagogue date)
- S-08 LaTeX build pipeline (plate, D table)
- S-09 Map and diagram pipeline (C5; unassigned Nayan-theatre map)
- S-10 Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-01.T1` Critical and factual fixes (Otchigin)
- `II-01.T2` Dispute asides (Jews/Kaifeng)
- `II-01.T4` Notes and apparatus normalisation
- `II-01.T5` Media placement (hero, C5, Nayan table)
- `II-01.T6` Lint pass and human voice read

### II-01.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #8 (batch 2)
- **Now:** 3,101 words · 61% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 7 · archaisms 13 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :17 (82%), :25 (89%), :29 (96%), :43 (81%), :45 (80%), :47 (97%).
  - Asides over 80 words: :15 (110), :35 (183). Trim; move traveller/scholar lists to Notes.
  - Cut the closing recap :49 (174 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :23, :27, :41, :49; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)
