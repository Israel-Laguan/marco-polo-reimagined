# II-F2 — Maps for Cathay and Manzi

**File:** `vol-2/front-02-maps-cathay-manzi.md` · **Status:** revised 2026-11-24, human review pending · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 290 | 11% | — | 5/5 | no |

## Original critique

The references below point to the draft examined in the critique. The task entries record the revisions. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit · **[W]** content-plan only.

### Critical
- **[C]** Invented epigraph: "And so I will tell you of the great province of Manzi…" is not in Yule–Cordier. Fix: "And when you pass this river you enter the great province of Manzi" (Bk II.lxv, verified). Observation (not in critique): ch-10:4 quotes the same Yule line (as "So when you pass…", N5), so the swap would echo II-10's epigraph. — vol-2 C3 · front-02:4; content plan W1.1

### Factual / fidelity
- **[M]** Place table row "Cachanfu | Xi'an (Chang'an) | Kenjanfu; Nestorians noted" is wrong twice: Cachanfu is Puzhou/Hezhong (II-06 Note [8]), and "Nestorians noted" contradicts ch-06:33, which makes the *silence* about the Nestorian stele its dispute hook. Fix: add a Kenjanfu row (Xi'an, Prince Mangala's seat), set Cachanfu to Puzhou/Hezhong, delete "Nestorians noted". — vol-2 M2 · front-02:41
- **[M]** `map-hangzhou-kinsay.jpg` shown as a map ("Kinsay and neighbours — Suju, Ganpu, and the estuary approaches") and credited to "Wikimedia Commons"; it is the AI-generated West Lake plate (same md5 as `map-hangzhou-kinsay.jpg (generated drawing)`; ATTRIBUTIONS lists it under "Generated illustrations"). Credit and labelling error. Fix: re-caption "Generated plate — West Lake atmosphere, not a map". Multimedia plan: **drop** the file. — vol-2 M8 · front-02:27–29; multimedia "Existing media triage"

### Dispute handling and Ramusio flags
- — none found

### Voice and prose
- **[M]** Stale scaffolding: "The images below are placeholders for files in `../media/`." Fix: drop "placeholders". — vol-2 M8 · front-02:9; content plan W1.3 (stale "placeholder" captions)
- **[W]** Hinge tic: "Anyway, keep these maps nearby…" (grep count of "Anyway": 1; lint cap ≤ 1). — content plan W0 · front-02:73

### Notes and apparatus
- **[W]** Note [1] leaks tooling: "Gazetteer filter: `volume=2` in `/workspace/marco-polo/gazetteer.csv`. Media placeholders: …". Content plan W1.3 lists `/workspace/…` paths in Notes and "placeholder" captions as scaffolding leaks (lint: 0). — content plan W1.3 · front-02:79

### Naming and gazetteer
- **[M]** Tables follow gazetteer `book_name` forms that differ from the chapters: Tainfu/Taianfu, Yangiu/Yanju, Ciangu/Changlu, Quinsay (Kinsay)/Kinsay, Ganpu/Ganfu, Tibet/Tebet. Fix: align gazetteer `book_name` to the Yule forms the chapters use (others as aliases), then regenerate these tables from it. — vol-2 M11 · front-02:35–65; content plan W5
- **[M]** Conflicting IDs carried in the tables: Caugigu = "Northern Vietnam / Tonkin" (ch-09:15 and `map-caugigu.jpg` put it at Kiang Hung, Lao side); Nanghin = Nanjing (ch-11:31 prefers Anqing, Yule); Vuju = Huzhou only (ch-14:13 uses Vuju for Wuzhou/Jinhua). — vol-2 M11 · front-02:48, :58, :61
- **[M]** Acbalec Manzi row sits in the "Manzi corridor to the haven" table but belongs to the west circuit. — vol-2 M11 · front-02:55
- **[M]** Gazetteer "Pazanjin / Hezhong" row (seq 66) appears in no chapter and duplicates the Hezhong ID; reconcile it with the Cachanfu fix. — vol-2 M2 · gazetteer.csv seq 66
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-F2.T1`.

### Length and structure
- **[M]** Map list covers only half the outline's four (Cambaluc and Shangdu; SW circuit; Grand Canal/Manzi spine; Zayton). `map-cambaluc.jpg` (Dadu plan) and `map-caugigu.jpg` (Yule Itinerary No. V) exist but are unused. Fix: add map-cambaluc and map-caugigu (SW circuit section). — vol-2 M8 · front-02 (whole)

## Media hooks

- **Maps in the guide:** A1 series round trip and A7 Kublai’s realm, including the Nayan inset.
- **Chapter map index:** A9 (II-2), A10 (II-6), A11 (II-7), A12 (II-10), A13 and its Tyunju inset (II-14), and A14 (II-15). See `MED.T2` for legacy media and credits.
- **Tables:** three place tables and the no-fix list from the series gazetteer.

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format)
- S-04 Gazetteer authority and naming policy
- S-06 Fact verification sheet (epigraph, Cachanfu/Caugigu/Nanghin IDs)
- S-07 Structure and length decisions (front/back roles)
- S-08 LaTeX build pipeline (maps, tables)
- S-09 Map and diagram pipeline (A1, A7)
- S-11 ✓ closed for plates only; facsimile credits and Wikimedia mis-credits are `MED.T1` (captions) and `MED.T2` (ATTRIBUTIONS)

## Tasks

### II-F2.T1 — Names to the S-04 policy; facts per S-06
- **Status:** revised 2026-11-24, human names and factual review pending · **Depends:** S-04 ✓, `GAZ.T5` ✓, S-06 ✓
- **Epigraph:** Retained the verified Book II.26 quotation about the roads out of Cambaluc. It avoids repeating the Manzi crossing used in II-10.
- **Names and tables:** Applied Book forms and first-mention glosses. Regenerated the tables and no-fix list and checked that they match the generator. Checked prose names separately because front-matter lint omits `name_policy`.
- **Identifications:** Cachanfu is Puzhou/Hezhong and Kenjanfu is Xi’an (F-11). Pazanjin survives as an alias of Cachanfu. Acbalec Manzi is in the western table. Caugigu uses Yule’s provisional Kiang Hung reference and Nanghin uses Pelliot’s Kaifeng with Yule’s Anqing alternative. Both Vuju entries appear. The Tyunju row now gives Dehua as provisional and names Tingzhou/Changting as an alternative.

### II-F2.T3 — De-duplicate to the S-07 role matrix
- **Status:** revised 2026-11-24, human voice review pending · **Depends:** S-07 ✓
- **Applied:** The guide gives the capitals and circuits, the map index, the generated tables and the identification cautions. It distinguishes reconstructed courses from reported places. The Yanju and Saianfu table entries describe the locations. II-11 holds the disputes. Removed the closing recap. The guide is 290 prose words against a target of 500.
- **Human review:** Read against the S-07 role matrix and II-2 for voice.

### II-F2.T4 — Notes and apparatus to the S-03 convention
- **Status:** revised 2026-11-24, human Notes review pending · **Depends:** S-03 ✓, `APP.T2` ✓
- **Applied:** Five marked Notes with sequential anchors. The Notes cover gazetteer use, the capitals and messenger roads, the western and southwest circuits, the southern route, and disputed southwest identifications. The chapter Note locators were checked in II-2, II-6, II-9, II-11 and II-14.
- **Check:** `markers`, `tags` and `citations` pass.

### II-F2.T5 — Media placement
- **Status:** verified 2026-11-24 · **Depends:** S-08 ✓, S-09 ✓, `MED.T2` ✓
- **Applied:** A1 and A7 retain their credits and uncertainty labels. The map index points to seven existing chapter map destinations.
- **Check:** Volume II PDF and HTML builds completed. All seven index links reach their maps in both builds. Print pages xv–xxiii were proofed, including map captions, table breaks and Notes. The PDF build reported zero placeholders and zero undersized rasters.

### II-F2.T6 — Lint green and human read
- **Status:** automated checks pass, human sign-off pending · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 7 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Checked 2026-11-24:** `python3 tools/lint.py -v vol-2/front-02-maps-cathay-manzi.md` reported 0 errors and 0 warnings. `python3 tools/gazetteer.py check` reported 198 rows and 0 problems.
- **Remaining:** Human review of names, factual wording, Notes and voice.

## S-17 map handoff (2026-11-11)

See `registry/facts.md` S17-F4/F6, the [intake](../../../research/results/S-17-intake.md), and `MAP.T09`–`MAP.T13`. A9 credits Fu Xinian’s reconstruction as reproduced by Funo and distinguishes reconstructed and approximate features. A11 uses provisional regional references and gives the Yule and Pelliot alternatives in its caption. The A13 inset gives Dehua and Tingzhou/Changting as competing readings for Tyunju.
