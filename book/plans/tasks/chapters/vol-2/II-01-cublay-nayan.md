# II-01 — Cublay Kaan: Puissance, Nayan, and the Ordo of Victory

**File:** `vol-2/ch-01-cublay-nayan.md` · **Status:** v3 pass complete (2026-11-23) · **Kind:** narrative

> **Voice Guide v3 pass (2026-11-23):** Claim-level anchor splits across dates, Caidu coalition, battle scale/capture, four provinces, and victory rewards; Nayan table reduced to single verdicts; all 36 Notes expanded to 2–3 sentences with all four Ramusio passages marked. Targeted lint passes (`1,801 w`, `2%` Yule overlap, `E0 W1` non-blocking `Caidu`/`Caindu` proximity warning).

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,801 (pre-v3: 3,082) | 2% (pre-v3: 61%) | [M] | ok (36/36 Notes, single verdicts) | no |

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
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-01.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 8 of 14 after the II-2 pilot (by verbatim share). — content plan W4

## Media hooks
- **Hero plate:** Kublai on the elephant-borne tower at the Nayan battle — GEN, Yuan court (Liu Guandao manner), handscroll 3:1; must get right: Kublai about 72 and heavy, white *tug* standard, modest host; caption: spectacle numbers inflated — see `illustration-plan.md`. Anchor ch-01:25.
- **Secondary plates:** none in the plan's secondary list. Critique §4 candidates: "Before the clash" (two hosts singing, *nakkara* kettledrums, :25); "Bloodless execution" (rolled felt, treat obliquely; method contested, :29); "Gerfalcon paiza bestowed" (surviving Yuan paiza, 'Phags-pa, :47).
- **Maps:** no A-ID assigned. Critique §5 map 5 "Nayan theatre" (Cambaluc → Liao/Nonni plain; Chorcha, Cauly, Barscol, soft) has no entry in `multimedia-plan.md`.
- **Timelines / diagrams / tables:** C5 Paiza hierarchy (silver → gerfalcon, script change 1269; II-1 / I-2); D table II-1 Nayan (kinship, year 1286 vs 1287, host size, sequel Qadaan). Pronunciation glossary entry for naccara/naqqāra (§E substitute for the critique's fiddle-and-kettledrum audio idea).
- **Characters appearing:** Kublai (Cublay Kaan), Nayan, Caidu (Kaidu), Chinghis Khan, Möngke, Belgutai / Temüge Otchigin (ancestry), Niccolò and Maffeo Polo (mentioned), Marco Polo, Rustichello ("a Pisan scribe"); travellers discussed: Rubruck, Monte Corvino, Marignolli, Ibn Battuta
- **Character check (S-05):** Cublay c. 72 (1287), carried, not mounted; Nayan c. 30, at a distance under a cross banner (the Book makes him a Christian). **No Polos on the field**: the text does not place them there. Cards: `plans/registry/character-cards.yaml`.

### Period sources (gap-source ledger, 2026-11-13)
- Mongol arms dated 1281 (Takashima): Matsuura City Report 4 (2011) has helmets (figs. 83–86, pls. 19–20; a deep bowl helmet with brow band, neck guard and riveted crest fitting), swords, bows, crossbows, arrows and red-lacquered lamellae. Matsuura Report 2 (2008) has colour photos. See the register's text facts. These are text facts, not yet cues.
- Mōko Shūrai Ekotoba: **avoid** the five Mongol figures added after 1709 (winged helmets, short robes, black boots) and the bomb explosion (Conlan 2013, `conlan2013myth`).
- S-23 closing: draft **C49**, a laced lamellar helmet bowl (Met 1999.158, viewed; 13th–15th c.), matches the Takashima helmet type.
- Register: `registry/visual-references.md § Gap-source ledger`.

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions
- S-05 Character registry (Kublai's age/appearance in hero; Nayan's descent)
- S-06 Fact verification sheet (Otchigin line; Kaifeng synagogue date)
- S-08 LaTeX build pipeline (plate, D table)
- S-09 Map and diagram pipeline (C5; unassigned Nayan-theatre map)
- S-10 ✓ Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-01.T5` Media placement (hero, C5, Nayan table) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `II-01.T6` Lint pass and human voice read

### II-01.T1 — Critical and factual fixes
- **Status:** complete · **Depends:** S-06 ✓, `II-01.T3` (W2: applied in the re-voice pass)
- **Do:**
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - F-04: Nayan descends from Temüge Otchigin (Yule's Uchegin), not Belgutai, Chinghis's step-brother.
    - F-28: the aside separates the two points: the Kaifeng synagogue dates from 1163 (its inscriptions, Yule); the thinness is in Polo.
  - Still-open rows use their hedge. When a library check settles one, update `registry/facts.md` first, then the chapter.
- **Done when:** every item under *Factual / fidelity* (and each *Critical* item not owned by `.T3` or a `HOT` task) is applied, or hedged as `registry/facts.md` says; each corrected Note cites the source key given there; a person has checked the changed sentences against the sheet.

### II-01.T3 — Re-voice to the S-01 standard
- **Status:** v3 draft recorded; independent human voice review pending · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #8 (batch 2)
- **Current lint (2026-11-24):** 1,818 w · 2% verbatim · 0 quotes · 1 asides; 0 errors, 0 warnings. Measurements are automated; source, apparatus and human review remain separate.
- **Literary pass (2026-11-24):** Trimmed repetitive modifiers ("cleanly", stacked adjectives/adverbs), varied paragraph openers around the Ramusio Easter passage and paiza section, added a short narrator pause after the Nayan battle, and confirmed the II-01 -> II-02 transition. Human voice review remains open.
- **Earlier baseline:** 3,101 words · 61% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 7 · archaisms 13 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :17 (82%), :25 (89%), :29 (96%), :43 (81%), :45 (80%), :47 (97%).
  - Asides over 80 words: :15 (110), :35 (183). Trim; move traveller/scholar lists to Notes.
  - Cut the closing recap :49 (174 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :23, :27, :41, :49; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Korea → Cauly ×1; unglossed first mentions: none. `python3 tools/lint.py -v vol-2/ch-01-cublay-nayan.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: Chinghiz → Chinghis ×1, Kublai → Cublay ×2, Möngke → Mongou ×2, Nicolo → Niccolò ×1; unglossed first mentions: none. The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-01.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** complete · **Depends:** S-03 ✓, `II-01.T3` (the flags are written during the re-voice pass)
- **Now:** 0 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-01-cublay-nayan.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-01.T4 — Notes and apparatus to the S-03 convention
- **Status:** complete · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-01.T3` (re-voice renumbers Notes)
- **Now:** 19 Notes · 0 ★ · 0 without a lead marker · tag [M]
- **Do:**
  - Tag line `**[M]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - Run `python3 tools/lint.py -v vol-2/ch-01-cublay-nayan.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-26 ✓ (2026-11-16):** The citation audit covers original Note(s) [19]; preserve the checked locators, scope and corrections from [the locator registry](../../../registry/locators.md) when rewriting or renumbering. These findings do not complete the wider Notes task.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

- **S-19 comparison intake (2026-11-12):** Use `plans/registry/comparanda.md` for this chapter’s checked witness locations and open leads. In the relevant Notes, say what each cited witness reports and give an edition-specific locator; verify lead passages before use, and omit unsupported comparisons. A public-domain quotation must be checked against the scan and attributed to the translation; BLD.T10 is pending. Do not treat shared subject matter as proof of Polo’s presence.

### II-01.T5 — Media placement (figures, tables, captions)
- **Status:** done (2026-11-23; plate II-1 `#fig-ii-1-nayan-elephant-tower` placed and proofed) · **Depends:** S-08 ✓, `II-01.T3` (re-voice establishes final anchors) · **W4 order:** with T5 batch
- **Do:**
  - **D (II-1) Nayan:** Create comparison table for the Nayan campaign. Structure per TBL.T1: pipe table, header row, `|---|---|` separator, no caption line, `booktabs` style, small type. Include a verdict column with markers (✓, ~, ✗, ◇, ?) where appropriate.
  - **S-17 research limit (2026-11-11):** The supplied report does **not** establish that the elephant-borne command platform or other color in the Nayan campaign is independently attested. Treat those details as Polo's account until a passage-by-passage *Yuan shi* comparison is checked. The table **must label its witnesses** clearly.
  - **S-17 priority return:** *Yuan shi* j. 14, 154 and 162 report imperial command, fighting and Li Ting's actions, but do not make the report's Persian elephant-litter passage independently verified. Ensure the table distinguishes between Polo's account and verified *Yuan shi* data.
  - **Table structure suggestion:**
    - Columns: Aspect (strategy, forces, elephant platform, outcome), Polo's account, *Yuan shi* account, Other sources, Verdict
    - Rows: Key elements of the Nayan campaign
    - Verdict column: reliability assessment
  - **Critical requirement:** Label the Book's details as its account; do **not** fill an independent-source column from a Polo-derived retelling.
  - Anchor the table where the Nayan campaign is described.
  - Write the table in Markdown pipe format as specified in `registry/markdown-conventions.md`.
- **Done when:** `tools/build/build.sh` places the table without errors, and the table adheres to TBL.T1 style guidelines with proper witness labeling.

### II-01.T6 — Lint green and human read
- **Status:** complete · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 22 errors · 4 warnings — failing: archaism, asides, budgets, recaps, scaffolding, verbatim, you_must_know; warnings: recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-01-cublay-nayan.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.

## S-17 research limit (2026-11-11)

The supplied report does not establish that the elephant-borne command platform or other color in the Nayan campaign is independently attested. Treat those details as Polo's account until a passage-by-passage *Yuan shi* comparison is checked; see [S-17 intake](../../../research/results/S-17-intake.md) and the [follow-up prompt](../../../research/S-17-follow-up-prompt.md). The II-1 comparison table must label its witnesses.

## S-17 priority return (2026-11-16)

[Checked intake](../../../research/results/S-17-priority-return-2026-11-16-intake.md): *Yuan shi* j. 14, 154 and 162 report imperial command, fighting and Li Ting's actions, but do not make the report's Persian elephant-litter passage independently verified. The Pelliot scan and Rashid passage remain unread in this check; do not claim the four-elephant platform is exclusively Polo's on an incomplete search. Note [8]'s crupper-transport corroboration needs a source-dependence check: Gaubil's report may not be independent of Polo. Verify the full Pelliot argument before making that claim. Correct the existing Belgutai genealogy per F-04 in the planned factual work.

## U-1 source handoff (2026-11-17)

From the [U-1 intake](../../../research/results/U-1-intake.md) (12 checks, 11 hits). F-49. Note [12]'s "thinly documented at this date" holds: Loewe reports *Yuan shi* mentions of Jews only under 1329, 1340 and 1354, in a fiscal context (`loewe1987jewish`). Check whether the gibe passage is Ramusio-only. These are inputs to the chapter's `.T1`/`.T4` work, not completed edits.
