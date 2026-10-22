# II-13 — Kinsay: Capital of Manzi

**File:** `vol-2/ch-13-kinsay.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,432 | 44% | [V] | 9/9 but sparse (Note [7] overloaded); "Gazetteer" tooling in [1] | **yes** (+232 over 3,200) |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 44% (critique C2 text prints 45%), with 4 first-person Book lines. Scorecard: 5 hinges, "You must know" ×3; verdict "Good Geographic/Ramusio split; over length; 3 recaps". Keep Yule only as short marked quotations, one or two per scene. — vol-2 C2, §3 · ch-13 (whole)

### Factual / fidelity
- — none found

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged (before the honest Ramusio opening at :53): :21 a hundred parties on the islands; :25 "fair and comely"; :27 bridge-guard timekeepers and fire drill; :33 unpaved verge for couriers. Fix: two-to-four-word inline tag per paragraph plus "◇ Ramusio-only" in the matching Note. Note: :53 itself ("So far the older texts. What follows… is Ramusio's continuation") is the critique's **model** for the whole volume. — vol-2 M1 · ch-13:21, :25, :27, :33; content plan W3

### Voice and prose
- **[M]** Drafting instruction in the prose: "The narrative flags it plainly and then tells it." Fix: delete, keep the honest Ramusio opening. — vol-2 M3 · ch-13:53; content plan W1.3
- **[M]** Outline-beat list pasted as the closing paragraph ("Thus Book II.lxxvi–lxxviii closes Heaven's city: …"). Fix: one forward-looking sentence, or nothing. — vol-2 M3, M4 · ch-13:87; content plan W1.3
- **[M]** Mid-chapter "So/Thus [place]…" restatements re-list the previous paragraph. — vol-2 M4 · ch-13:23, :41, :73
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 2. — vol-2 M4 · ch-13 (whole)
- **[N]** "*Milioni*" inconsistent with "*Milione*" elsewhere. — vol-2 N4 · ch-13:87

### Notes and apparatus
- **[m]** Citation density: 9 citations across 3,432 words. The pepper figure (:63), the Facfur tour (:69) and the revenue (:77–81) share broad Notes. Fix: split Note [7] so that pork, market and pepper each get their own entry. — vol-2 m13 · ch-13:63, :69, :77–81, Note [7] ch-13:105
- **[M]** Note [1] leaks tooling ("gazetteer *visited*"). — vol-2 M3 · ch-13:93

### Naming and gazetteer
- **[M]** Gazetteer `book_name` forms differ from the chapter: "Quinsay (Kinsay)" vs "Kinsay"; "Ganpu" vs "Ganfu" (front-02 follows the gazetteer). — vol-2 M11

### Length and structure
- **[M]** Over target: 3,432 narrative words (3,484 with title/epigraph/tag). Cut about 350: delete recaps :41 (70 words), :73 (62 words; move the Moule pepper point to Note [7]) and :87 (44 words); reduce :53 to one sentence (about 30 words); merge the Geographic palace (:47) with Ramusio's Facfur palace (:69–71), near-duplicates (about 80 words); trim the pears and peaches list at :57 (about 60 words). — vol-2 M10 · ch-13:41, :47, :53, :57, :69–71, :73, :87; content plan W4 "Over length"
- W4 re-voice order: Vol. II batch position 13 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Pleasure barges on the West Lake — GEN, Song–Yuan city-genre scroll, handscroll 3:1; must get right: Leifeng Pagoda, **no Qing pavilions**; caption: Ramusio's description — see `illustration-plan.md`. This is **Pilot 2** of the illustration plan's three-plate generator pilot (prompt written there). Anchor ch-13:67.
- **Secondary plates:** GEN Fire alarm in Kinsay (plan; anchor :29, bridge-watchmen, goods carried to stone store-towers). Critique §4 candidate: household registers (:51; a street of doors with name boards). Existing `drawing-kinsay-west-lake.png` named by critique §4/§5 for ch-13; the multimedia plan retires all `drawing-*.png`, and its twin `map-hangzhou-kinsay.*` is mis-captioned in front-02 (see II-F2).
- **Maps:** A12 The canal spine (terminus at Kinsay).
- **Timelines / diagrams / tables:** D table II-13 Kinsay numbers (Polo / Odoric / Ibn Battuta / Wassaf). Critique §5 also proposes a "Kinsay revenue metrology" diagram (tomans, *saggi*, tael, *ting*); no C-ID in `multimedia-plan.md`.
- **Characters appearing:** Facfur (the last Song ruler, as the Book names him), the Queen (Facfur's consort), Bayan, Kublai (the Kaan), Marco Polo; traveller discussed: Odoric

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style; Note split)
- S-04 Gazetteer authority and naming policy (Kinsay, Ganfu)
- S-07 Structure and length decisions (over length)
- S-08 LaTeX build pipeline (plates, map, D table)
- S-09 Map and diagram pipeline (A12; unassigned metrology diagram)
- S-10 Image generation pilot (**hero is Pilot 2**; GEN secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-13.T2` Ramusio flags (four passages)
- `II-13.T3` Re-voice to the S-01 standard (incl. ~350-word cut, instruction, beat-list, N4)
- `II-13.T4` Notes and apparatus normalisation (split Note [7])
- `II-13.T5` Media placement (hero, secondary, A12, Kinsay table)
- `II-13.T6` Lint pass and human voice read
