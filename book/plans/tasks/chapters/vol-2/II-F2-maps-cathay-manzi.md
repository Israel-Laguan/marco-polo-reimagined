# II-F2 — Maps for Cathay and Manzi

**File:** `vol-2/front-02-maps-cathay-manzi.md` · **Status:** backlog · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 766 | n/a | — | 3/3; Note [1] leaks `/workspace` path | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit · **[W]** content-plan only.

### Critical
- **[C]** Invented epigraph: "And so I will tell you of the great province of Manzi…" is not in Yule–Cordier. Fix: "And when you pass this river you enter the great province of Manzi" (Bk II.lxv, verified). Observation (not in critique): ch-10:4 quotes the same Yule line (as "So when you pass…", N5), so the swap would echo II-10's epigraph. — vol-2 C3 · front-02:4; content plan W1.1

### Factual / fidelity
- **[M]** Place table row "Cachanfu | Xi'an (Chang'an) | Kenjanfu; Nestorians noted" is wrong twice: Cachanfu is Puzhou/Hezhong (II-06 Note [8]), and "Nestorians noted" contradicts ch-06:33, which makes the *silence* about the Nestorian stele its dispute hook. Fix: add a Kenjanfu row (Xi'an, Prince Mangala's seat), set Cachanfu to Puzhou/Hezhong, delete "Nestorians noted". — vol-2 M2 · front-02:41
- **[M]** `map-hangzhou-kinsay.jpg` shown as a map ("Kinsay and neighbours — Suju, Ganpu, and the estuary approaches") and credited to "Wikimedia Commons"; it is the AI-generated West Lake plate (same md5 as `drawing-kinsay-west-lake.png`; ATTRIBUTIONS lists it under "Generated illustrations"). Credit and labelling error. Fix: re-caption "Generated plate — West Lake atmosphere, not a map". Multimedia plan: **drop** the file. — vol-2 M8 · front-02:27–29; multimedia "Existing media triage"

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
- **Hero plate:** — none (map page)
- **Secondary plates:** — none
- **Maps:** A1 series overview (each volume's front-02, replaces the Wikimedia one); A7 Kublai's realm c. 1290 (II-front-02). Existing files: `map-china-yuan.jpg` is a duplicate of `map-yuan-1294.png` (dedupe; multimedia plan: **replace** with generated map, too small); `map-cambaluc.jpg` (**replace** with redrawn A9 Dadu plan); `map-caugigu.jpg` (keep as small facsimile, superseded by A11); `map-hangzhou-kinsay.*` (**drop**). Multimedia "Order of work" step 1: fix these mis-captions now.
- **Timelines / diagrams / tables:** place tables (regenerate from gazetteer, W5)
- **Characters appearing:** Marco Polo (claims at Yanju/Saianfu); Prince Mangala (in critique's Kenjanfu row fix only)

## Gated by spikes
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format)
- S-04 Gazetteer authority and naming policy
- S-06 Fact verification sheet (epigraph, Cachanfu/Caugigu/Nanghin IDs)
- S-07 Structure and length decisions (front/back roles)
- S-08 LaTeX build pipeline (maps, tables)
- S-09 Map and diagram pipeline (A1, A7)
- S-11 Public-domain artwork sourcing and licensing (facsimile credits; Wikimedia mis-credits)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-F2.T1` Critical and factual fixes (epigraph, Cachanfu/Kenjanfu rows)
- `II-F2.T3` Prose clean-up (placeholders, tic)
- `II-F2.T5` Media placement and caption correction (A1, A7, Cambaluc, Caugigu; drop Kinsay "map")
- `II-F2.T6` Lint pass and human read

### II-F2.T1 — Names to the S-04 policy
- **Status:** backlog · **Depends:** S-04 ✓, `GAZ.T5`
- **Now:** bare variants: Beijing → Cambaluc ×1, Tibet → Tebet ×1, Yunnan → Carajan ×1, Burma → Mien ×1, Yangzhou → Yanju ×1, Xiangyang → Saianfu ×1, Suzhou → Suju ×1, Hangzhou → Kinsay ×1 (+2 more)
- **Do:**
  - Prose follows the chapters' policy (book form, one gloss per place on first mention). Place tables are regenerated from `gazetteer.csv` by `GAZ.T5` — do not hand-edit them.
  - Chapter-specific conflicts are listed under *Naming and gazetteer* above.
- **Done when:** `python3 tools/lint.py -v vol-2/front-02-maps-cathay-manzi.md` shows no `name_policy` warnings (or the reviewer accepts the remaining ones), and a person has read the names.

### II-F2.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), —
- **Now:** 3 Notes · 0 ★ · 1 without a lead marker
- **Do:**
  - Notes with no lead marker: [1] (fill, merge or rewrite; none may be a placeholder or pointer).
  - Run `python3 tools/lint.py -v vol-2/front-02-maps-cathay-manzi.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-F2.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 7 errors · 0 warnings — failing: markers, quote_verify, scaffolding
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/front-02-maps-cathay-manzi.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
