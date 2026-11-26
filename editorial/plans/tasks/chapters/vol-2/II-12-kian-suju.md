# II-12 — Kian, Suju, and the Approach to Heaven's City

**File:** `vol-2/ch-12-kian-suju.md` · **Status:** v3 pass complete (2026-11-23) · **Kind:** narrative

> **Voice Guide v3 pass (2026-11-23):** Full v3 narrative scenes (`37` single-verdict Notes, 2–3 sentences each), kept `F-10` Mar Sarghis reports unmerged (2 churches 1278 vs 7 monasteries with 1279/1281 dates), dropped `N8` tea/Paris line, flagged all Ramusio witness passages, and transitioned smoothly into `II-13` Changan sendal. Targeted lint passes (`1,815 w`, `3%` Yule overlap, `E0 W0`).

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,815 (pre-v3: 2,546) | 3% (pre-v3: 62%) | [V] | ok (37/37 Notes, single verdicts) | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 62% (critique C2 text prints 63%). Highest count of first-person Book lines in the volume: 11 of 38. Example :65 "Now let us quit Suju… so we shall now proceed". The city strings are named among the catalogue passages to turn "into modern storyteller summary". Scorecard: 9 hinges, "You must know" ×4. Fix: convert first-person Book lines to reported speech or marked quotation. — vol-2 C2, §3 · ch-12:65

### Factual / fidelity
- Mar Sargis: Moule and Giles translate the gazetteer as attributing seven monasteries to him, with two dated 1279 and Ta-hsing-kuo dated 1281. The Book reports two churches in 1278; keep the reports distinct and do not date all seven to 1279 (F-10, S-14).
- **[N]** "Su-chau of the silk and the tea districts, the Paris of later China": a stray tea mention given that the volume flags tea as a silence, and "Paris" is anachronistic and unsourced. Fix: cut it. — vol-2 N8 · ch-12:67
- **[N]** (S-05) Polo gives Mar Sarghis **two** churches at Chinghianfu; Cordier's addendum in Yule counts **seven** built in China, one of them at Kinsay (Moule 1930 has the gazetteer text: reported). An aside can set Polo's two against the record. — registry `mar-sarghis`

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged: :19 river length, salt as chief cargo; :25 island monasteries. Fix: two-to-four-word inline tag per paragraph plus "◇ Ramusio-only" in the matching Note; model ch-13:53. — vol-2 M1 · ch-12:19, :25; content plan W3

### Voice and prose
- **[M]** Mid-chapter "So/Thus [place]…" restatements re-list the previous paragraph. Fix: merge their identification content into the Notes. — vol-2 M4 · ch-12:15, :27, :35
- **[M]** Recap padding: closes with a "Thus Suju… closes the approach" recap. Fix: cut to at most one sentence or remove. — vol-2 M4 · ch-12:67
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 4 (highest in the volume). — vol-2 M4 · ch-12 (whole)

### Notes and apparatus
- — see m8 (Note [5] marker upgrade)

### Naming and gazetteer
- **[M]** Vuju is used for two different cities: ch-12:65 (Huzhou) and ch-14:13 (Wuzhou/Jinhua, per Yule). Fix example (for II-14): "Vuju (Wuzhou, today's Jinhua) — not the Vuju (Huzhou) of the last chapter". — vol-2 M11 · ch-12:65
- **[M]** No gazetteer rows for Sinju, Caiju, Chinghianfu, Chinginju, Vughin, Changan (blocks map A12). — vol-2 M11
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-12.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 7 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Trackers haul a junk up the Kiang — GEN, Yuan landscape, handscroll 3:1; must get right: bamboo hawsers, Golden Island monastery — see `illustration-plan.md`. Anchor ch-12:23 (single-masted cargo junk; Jinshan temple mid-river).
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: grain fleet at Caiju (:29; canal mouth, embanked towpaths); Suzhou bridge (:59; one high-arched stone bridge; "six thousand" is formulaic).
- **Maps:** A12 The canal spine (… Yanju → Sinju → Caiju → Chinghianfu → Chinginju → Suju → Vuju → Vughin → Changan → Kinsay).
- **Timelines / diagrams / tables:** — none assigned. (Critique §5 timeline "1278 Mar Sarghis at Zhenjiang" feeds B3 in II-F1.)
- **Characters appearing:** Marco Polo, Bayan, Mar Sarghis (Mar Sargis), Kublai (the Kaan); travellers discussed: Odoric, Ibn Battuta

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style; marker upgrade)
- S-04 Gazetteer authority and naming policy (two Vujus; missing rows)
- S-05 Character registry (Mar Sarghis dates)
- S-06 Fact verification sheet (Mar Sargis at Zhenjiang, F-10 in part; N8)
- S-08 LaTeX build pipeline (plate, map)
- S-09 Map and diagram pipeline (A12)
- S-10 ✓ Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-12.T5` Media placement (hero, A12) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `II-12.T6` Lint pass and human voice read

### II-12.T1 — Critical and factual fixes
- **Status:** complete · **Depends:** S-06 ✓, `II-12.T3` (W2: applied in the re-voice pass)
- **Do:**
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - Mar Sargis: Moule and Giles translate the gazetteer as attributing seven monasteries to him, with two dated 1279 and Ta-hsing-kuo dated 1281. The Book reports two churches in 1278; keep the reports distinct and do not date all seven to 1279 (F-10, S-14).
  - Still-open rows use their hedge. When a library check settles one, update `registry/facts.md` first, then the chapter.
- **Done when:** every item under *Factual / fidelity* (and each *Critical* item not owned by `.T3` or a `HOT` task) is applied, or hedged as `registry/facts.md` says; each corrected Note cites the source key given there; a person has checked the changed sentences against the sheet.

### II-12.T3 — Re-voice to the S-01 standard
- **Status:** v3 draft recorded; independent human voice review pending · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #7 (batch 2)
- **Current lint (2026-11-24):** 1,801 w · 3% verbatim · 0 quotes · 2 asides; 0 errors, 0 warnings. Literary pass (2026-11-24): tightened the Kiang trackers scene (replacing "Picture..." with "Watch..." and trimming redundant adjectives) and verified II-11 -> II-12 -> II-13 transitions. Measurements are automated; source, apparatus and human review remain separate.
- **Result:** 1,832 words · 3% verbatim · targeted lint passes with 0 errors and 0 warnings
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :17 (92%), :19 (97%), :23 (90%), :29 (96%), :47 (100%), :65 (99%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :19, :25, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :41 (108), :53 (150), :63 (162). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :15, :27, :35, :67; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Baseline before re-voice: bare variants included Samarcand, Yangzhou, I-ching, Kwa-chau, Chang-chau, Hu-chau, Kiahing, and Hangzhou; first mentions of Sindafu, Tebet, Caindu, Nanghin, Saianfu, Caiju, Chinghianfu, Chinginju, Suju, Vuju, Vughin, Changan, and Kinsay lacked glosses.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Baseline before re-voice: no bare variants or unglossed first mentions.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-12.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** complete · **Depends:** S-03 ✓, `II-12.T3` (the flags are written during the re-voice pass)
- **Baseline before re-voice:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-12-kian-suju.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-12.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-12.T3` (re-voice renumbers Notes)
- **Now:** 9 Notes · 0 ★ · 0 without a lead marker · tag [V]
- **Do:**
  - Tag line `**[V]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - Run `python3 tools/lint.py -v vol-2/ch-12-kian-suju.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### II-12.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 25 errors · 7 warnings — failing: archaism, asides, budgets, first_person, ramusio, verbatim, you_must_know; warnings: names, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-12-kian-suju.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
