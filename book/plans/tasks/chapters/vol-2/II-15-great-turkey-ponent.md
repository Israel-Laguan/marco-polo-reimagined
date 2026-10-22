# II-15 — Great Turkey, Caidu's Daughter, and the Wars of the Ponent

**File:** `vol-2/ch-15-great-turkey-ponent.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,143 | 52% | [R] | 10/10; Note [6] mismatches body (1294 vs 1295) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 52%. Scorecard: 7 hinges, "You must know" ×2; verdict "Sensible compression; Kiacatu/Casan slips". Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-15 (whole)

### Factual / fidelity
- **[m]** Kiacatu called "an uncle of his — own brother, the better texts will say, to Abaga", which makes the "better texts" endorse the error, while :35 correctly says Geikhatu was Arghun's *brother*. Fix: "an uncle of his, the Book says — in fact his own brother, Geikhatu". — vol-2 m1 · ch-15:33; content plan W2 (II-15)
- **[m]** Baidu "his uncle" left uncorrected (he was a cousin, grandson of Hülegü through Taraqai). — vol-2 m1 · ch-15 (Baidu passage); content plan W2 (II-15)
- **[m]** :27 compresses Arghun's victory over Baraq (Baraq d. 1271) and Abaqa's death (1282) into "no long time passed". Fix: add a clause. — vol-2 m1 · ch-15:27
- **[N]** "Pharaoh's rat" has no gloss (Yule: a marmot or jerboa type). — vol-2 N7 · ch-15:37

### Dispute handling and Ramusio flags
- **[M]** Marker mismatch: body says "Casan began to reign in the year 1294", but Note [6] gives "✓ Gházán's victory 1295 sound"; the 1294 figure is never marked ✗ (Ghazan acceded in 1295). — vol-2 M7 · ch-15:33, Note [6] ch-15:67; content plan W2 (II-15)

### Voice and prose
- **[M]** Recap padding: chapter ends with a recap paragraph ("Thus Book IV, compressed, closes Volume II's horizon: …"). Fix: cut to at most one sentence, or remove. — vol-2 M4 · ch-15:51
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-15 (whole)

### Notes and apparatus
- — see M7 (Note [6])

### Naming and gazetteer
- **[M]** No modern gloss on first mention for Lac (Wallachia, per Yule's index). — vol-2 M11, N7 · ch-15:43

### Length and structure
- W4 re-voice order: Vol. II batch position 11 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Aijaruc throws the prince — GEN, Ilkhanid (*Jami' al-Tawarikh*), landscape 4:3; must get right: Kaidu's court, wagered horses; caption: folkloric; historical name Khutulun — see `illustration-plan.md`. Anchor ch-15:23.
- **Secondary plates:** GEN Dog-sledge post (plan; anchor :39, six dogs to a sledge, bear-skin for the courier). Critique §4 candidate: Land of Darkness raid (:41; legendary geography).
- **Maps:** A14 The Mongol horizon (Ilkhanate, Chagatai and Kaidu, Golden Horde, "Land of Darkness" dotted). Existing `map-asia-mongol-empire.jpg` / `map-mongol-empire.gif` suggested by critique §5; the multimedia plan **replaces** them (too small; date range unverified).
- **Timelines / diagrams / tables:** C8 Ilkhan succession: the Book vs the record (critique timeline: Abaqa d. 1282; Tegüder 1282–84; Arghun 1284–91; Geikhatu 1291–95; Baidu 1295; Ghazan 1295). Critique §5 also lists a "Golden Horde khan list (Book vs actual)" table; it has no D-row in `multimedia-plan.md`.
- **Characters appearing:** Caidu (Kaidu), Aijaruc (Khutulun), Kublai (Cublay), Chinghis Khan, Argon (Arghun), Abaga (Abaqa), Acomat (Tegüder Ahmad), Kiacatu (Geikhatu), Baidu, Casan (Ghazan), Barac (Baraq), Alau (Hülegü), Barca (Berke), Batu, Toctai (Tokhta), Nogai, Conchi, Nomogan (Nomukhan), Cocachin (mentioned), Marco Polo, Rustichello

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (✓/✗ on Note [6])
- S-04 Gazetteer authority and naming policy (Lac; A14 places)
- S-05 Character registry (Ilkhan names, kinship, regnal dates; Aijaruc/Khutulun in hero)
- S-06 Fact verification sheet (Kiacatu, Baidu, Ghazan 1295, Baraq/Abaqa dates)
- S-08 LaTeX build pipeline (plates, map, diagram)
- S-09 Map and diagram pipeline (A14, C8)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-15.T1` Factual fixes (Kiacatu, Baidu, Ghazan, Baraq/Abaqa clause, N7)
- `II-15.T4` Notes and apparatus normalisation (Note [6])
- `II-15.T5` Media placement (hero, secondary, A14, C8)
- `II-15.T6` Lint pass and human voice read

### II-15.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #11 (batch 3)
- **Now:** 3,099 words · 52% verbatim · "You must know" 2 · "Anyway" 3 · formula hinges 2 · archaisms 3 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :13 (83%), :21 (97%), :23 (84%), :37 (90%), :41 (94%), :43 (73%).
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :25, :35, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)
