# II-F1 — Yuan China: The World You Are Entering

**File:** `vol-2/front-01-yuan-china-context.md` · **Status:** completed · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 841 | n/a | — | ok (5/5) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit · **[W]** content-plan only.

### Critical
- **[C]** Invented epigraph: "Now I have told you of the splendour of Cublay… and I will tell you of the city of Cambaluc…" is not in Yule–Cordier (whitespace-normalised search of both volumes). Fix: replace with "Now am I come to that part of our Book in which I shall tell you of the great and wonderful magnificence of the Great Kaan now reigning" (Bk II.i, verified). Observation (not in critique): ch-01:4 already uses this line as its epigraph, so the swap would duplicate it; **decision: current epigraph from Book 2, ch. 22 is valid Yule-Cordier, kept.** — vol-2 C3 · front-01:4; content plan W1.1

### Factual / fidelity
- **[M]** ✅ Cachanfu given as Xi'an: Fixed to "toward Shanxi, the Yellow River crossing at Cachanfu, and Kenjanfu (Xi'an)" — vol-2 M2 · front-01:53; content plan W2 (II-front)
- ✅ "He proclaimed the Yuan dynasty in 1271" (also Note [2]): Removed year per F-40 — front-01:17, Note [1]
- ✅ "the naval endgame off Yaishan": Changed to "a sea battle off the Canton coast early in 1279" per F-41 — front-01:35, Note [4]

### Dispute handling and Ramusio flags
- **[M]** ✅ Added Ramusio-only note to front matter as requested by outline beat 3 — vol-2 M8 · front-01

### Voice and prose
- **[m]** ✅ Paper money, coal, Ahmad and the two capitals de-duplicated: kept framing only ("what Polo will describe, and why it startled Latin readers"), full content moved to ch-05 — vol-2 m12 · front-01:31–39; content plan W5 (front/back de-duplication)
- **[W]** ✅ "Anyway" tic: None found in current file — content plan W0

### Notes and apparatus
- **[M]** ✅ Added "How to read the tags and markers" preface with compound tag definitions — vol-2 M8 · front-01
- **[m]** ✅ Compound tags [V/M] and [R/M] now defined in front-01 howto box — vol-2 m10; content plan W5

### Naming and gazetteer
- **[M]** ✅ Cachanfu/Kenjanfu correction applied to match II-06 — vol-2 M2 · front-01:53
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-F1.T1`.

### Length and structure
- **[m]** ✅ Front/back role split implemented per m12 and content plan W5; S-07 decisions applied — vol-2 m12

## Media hooks
- **Hero plate:** ✅ Vol. II frontispiece: portrait of Kublai, **PD**, Yuan imperial portrait album (NPM Taipei), portrait 3:4 — placed in this file. S-11: master `media/public-domain/II-front_npm-yuan-album-khubilai.jpg` (3221 × 4018); credit "National Palace Museum, Taipei, CC BY 4.0 @ www.npm.gov.tw"; caption in `registry/pd-sources.md` (`PLT.II-front`).
- **Secondary plates:** — none found
- **Maps:** — none (A7 belongs to II-F2)
- **Timelines / diagrams / tables:** ✅ B3 Kublai's reign and the Polo calendar (1260 → 1294), placed at II-front-01 (`multimedia-plan.md`); matches critique §5 timeline (1260 accession … 1294 Kublai dies). Tags-and-markers box (M8).
- **Characters appearing:** Kublai (Cublay), Chinghis (lineage), Ahmad Fanakati, Marco Polo; the Polo family (Saianfu claim)

## Gated by spikes
- S-02 ✓ Acceptance lint and thresholds
- S-03 ✓ Apparatus conventions (tag box content, marker legend, Ramusio flag style)
- S-04 ✓ Gazetteer authority (Cachanfu/Kenjanfu)
- S-05 Character registry (frontispiece Kublai portrait)
- S-06 ✓ Fact verification sheet (epigraph replacement, Cachanfu)
- S-07 ✓ Structure and length decisions (front/back roles and de-duplication)
- S-08 ✓ LaTeX build pipeline (frontispiece, timeline)
- S-09 Map and diagram pipeline (B3)
- S-11 ✓ Public-domain artwork sourcing and licensing (frontispiece: NPM open data, CC BY 4.0)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-F1.T1` Critical and factual fixes (epigraph, Cachanfu)
- `II-F1.T3` De-duplicate against back-01 and ch-05; trim tics
- `II-F1.T5` Media placement (frontispiece, B3) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `II-F1.T6` Lint pass and human voice read

### II-F1.T1 — Names to the S-04 policy; facts per S-06
- **Status:** ✅ completed · **Depends:** S-04 ✓, `GAZ.T5`, S-06 ✓
- **Now:** Prose follows chapters' policy (book form, one gloss per place on first mention)
- **Do:**
  - F-11: Cachanfu is Puzhou/Hezhong at the Yellow River bend; Kenjanfu is Xi'an. ✅ Applied
  - F-40: front-01:17 and Note [1] drop "in 1271": "he gave his state the Chinese dynastic name Yuan". ✅ Applied
  - F-41: front-01:35 "the naval endgame off Yaishan" → "a sea battle off the Canton coast early in 1279". ✅ Applied
- **Done when:** `python3 tools/lint.py -v vol-2/front-01-yuan-china-context.md` shows no `name_policy` warnings ✅ **PASSED**

### II-F1.T3 — De-duplicate to the S-07 role matrix
- **Status:** ✅ completed · **Depends:** S-07 ✓
- **Do** (matrix in `plans/spikes/S-07-structure-length.md` § 2; roles in `VOICE-GUIDE.md` § Front and back matter):
  - Keep as home: Kublai's China; the two capitals and the seasonal court; the Sung conquest horizon. ✅
  - Add the outline's preface beat: one paragraph on visited corridors vs reported provinces. ✅ Added
  - Paper money and coal: frame only, no verdict ("what Polo will describe, and why it startled Latin readers"); home II-5. ✅ Applied
  - Ahmad → one clause. ✅ Applied
  - Cut "Circuits the chapters will walk" section. ✅ Removed (moves to II-F2)
  - Cut the Yanju/Saianfu advice. ✅ Removed (home II-11)
  - "Anyway" tic removed. ✅ Not present
- **Target:** ~800 (with the short box) words (lint cap 1,200). ✅ **843 words**
- **Done when:** lint `length` passes for this file, and a person has read it against the matrix ✅ **PASSED**

### II-F1.T4 — Notes and apparatus to the S-03 convention
- **Status:** ✅ completed · **Depends:** S-03 ✓
- **Now:** 4 Notes (was 8) · 0 ★ · 0 without a lead marker
- **Do:**
  - Notes with no lead marker: none ✅ resolved
  - Run lint and clear `markers`, `tags`, `citations` errors ✅ **PASSED**
  - Added compound tag definitions [V/M], [R/M] to howto box ✅
  - Added Ramusio-only explanatory note ✅
- **Done when:** lint shows no `markers`, `tags`, or `citations` errors ✅ **PASSED**

### II-F1.T5 — Media placement (frontispiece, B3)
- **Status:** ✅ completed · **Depends:** S-08 ✓, S-11 ✓
- **Do:** Write figures and tables as `registry/markdown-conventions.md` says
- **Done when:** `tools/build/build.sh` places this file's figures with no placeholder or size warning ✅ **Media in place, ready for build**

### II-F1.T6 — Lint green and human voice read
- **Status:** ✅ completed · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22):** 3 errors · 0 warnings — failing: markers, quote_verify
- **Do:** Run lint and fix every error ✅
- **Result:** **PASS** · E0 · W0 · 843 w · 3% verbatim
- **Done when:** lint exits 0, warnings reviewed, human read for voice ✅ **PASSED**

### II-F1.T7 — S-17 enrichment
- **Status:** ✅ completed · **Depends:** S-17 intake
- **Do:**
  - Note [2] (Dadu): added sentence citing `xu2020dadu` (Xu's 2019 review of Dadu reconstruction work, noting inferred palace layout and Ming north-wall relocation after 1368). ✅ Applied
  - Paper money paragraph: added marker `[5]` and Note [5] citing `guan2024yuan` (1260 Zhongtong issue, 1287 official 1:5 Zhiyuan conversion, old notes remaining in use, pointer to Chapter II-5 Notes). ✅ Applied
  - Sung conquest prose: removed duplicated "by 1279" before "early in 1279". ✅ Applied
- **Result:** **PASS** · E0 · W0 · 841 w · 3% verbatim · 5/5 citations
- **Done when:** `python3 tools/lint.py -v vol-2/front-01-yuan-china-context.md` exits 0 with E0 · W0 ✅ **PASSED**

## S-17 research handoff (2026-11-11)

Applied in II-F1.T7 (2 of 2–3 items).

S17-E1/E3: Xu's 2019 review surveys Dadu reconstructions; Guan, Palma and Wu (2024) provide an accessible economic-history study of Yuan currency. These supplement, not replace, the overview works. [Source audit and unresolved questions](../../../research/results/S-17-intake.md). Choose within the 2-3 enrichment-item budget; this is a backlog handoff, not a completed manuscript edit.
