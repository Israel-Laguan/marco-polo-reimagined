# II-04 — Hunt, Hounds, Litter, and the Traffic of a Million

**File:** `vol-2/ch-04-hunt-traffic.md` · **Status:** v3 pass complete (2026-11-23) · **Kind:** narrative

**W4 v3 (2026-11-23):** 24 sequential claim-level Notes. Targeted lint: 1,860 words, 2% Yule overlap, 0 errors, 0 warnings. F-53 (hunting closed season in *Yuan shi*, *Tongzhi tiaoge* j. 28, *Yuan dianzhang* j. 38 summary table, and Pétis de la Croix in YC 2.20 n. 9) is Note 17; Rossabi (ch. 6) locators are Notes 10 and 24.

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 3,113 | 72% | [V] | 21/21; Notes [7], [21] empty stubs; [20] unqualified | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-2.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one. Severity prefix: **[C]** critical · **[M]** major · **[m]** minor · **[N]** nit.

### Critical
- **[C]** Near-transcription of Yule: 72%. Scorecard verdict: "Good linguistic asides; leaked instruction :17; Ramusio unflagged". Keep Yule only as short marked quotations, one or two per scene; "Sire! Look out for Cranes!" is the critique's own example of a quotation worth keeping. Scorecard: 7 hinges, "You must know" ×3. — vol-2 C2, §3 · ch-04 (whole), :33

### Factual / fidelity
- **[m]** Note [20] presents *Milione*'s "double life (wealth vs 'million lies')" without qualification. Vol. III ch-10 says "'million lies' insult — popular later reading; not the archival sense" and gives the house-name theory. Fix: align with III-10. — vol-2 m11 · ch-04:99

### Dispute handling and Ramusio flags
- **[M]** Ramusio-only passages narrated unflagged: :15 approach the game against the wind; :23 the Two Brothers' thousand-head tenure (only Note [6] says "Ramusio"); :47 nation-sorted hostelries; :51 night patrols and beatings. Fix: two-to-four-word inline tag per paragraph plus "◇ Ramusio-only" in the matching Note; model ch-13:53. — vol-2 M1 · ch-04:15, :23, :47, :51; content plan W3

### Voice and prose
- **[M]** Drafting instruction left in the prose: "Narrate 'lion' as the Book says; gloss tiger without flattening the medieval lexicon." Fix: delete the instruction, keep only the substance. — vol-2 M3 · ch-04:17; content plan W1.3
- **[M]** Recap padding: opens with "The Book has shown…" (:11) and closes with "Here the chapter stops short of… For the present it has shown…" (:55). Fix: cut closing recap to at most one sentence or remove; drop the opening recap. — vol-2 M4 · ch-04:11, :55
- **[M]** Aside-exit tic "Anyway, next he mentions X"; cap one per chapter, vary exits. Grep count of "Anyway" in file: 3. — vol-2 M4 · ch-04 (whole)

### Notes and apparatus
- **[M]** Notes [7] and [21] leak tooling ("Soft transition to the imperial tour"; "Soft landing to II-5"). — vol-2 M3 · ch-04:73, :101
- **[m]** Notes [7] and [21] add nothing (cross-reference / transition stubs). Fix: merge into neighbouring Notes and drop the citations. — vol-2 m9 · ch-04:73, :101; content plan W5

### Naming and gazetteer
- **[M]** The gazetteer marks Cachar Modun as unfixed. C17 shows the seasonal sequence without placing the camp on a map. — vol-2 M11 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `II-04.T3`.

### Length and structure
- W4 re-voice order: Vol. II batch position 3 of 14 after the II-2 pilot. — content plan W4

## Media hooks
- **Hero plate:** Kublai hunting — **PD**, Liu Guandao, *Khubilai Khan Hunting* (1280), hanging scroll, portrait (S-11; `PLT.II-04`) — see `illustration-plan.md`.
- **Secondary plates:** Placed Omont pl. 47, the elephant-litter miniature from fr. 2810, fol. 42v. Earlier GEN proposal: "Sire! Look out for Cranes!" from the elephant litter (plan's Vol. II secondaries; critique §4 ★ scene, anchor :33: roof of the timber chamber thrown open, gerfalcon cast, Toscaol watchers in pairs; spring marshes south-east of Dadu). Critique §4 further candidates: red and blue hound corps (:21; caution: 10,000 men per brother inflated); tiger hunt (:15; "label it a tiger").
- **Maps:** A9 in II-2 gives the city plan. The seasonal itinerary is diagram C17.
- **Timelines / diagrams / tables:** C17 seasonal orbit, placed after the return to Cambaluc. Existing `drawing-chandu-palace.jpg` is suggested for ch-04 by critique §5 ("if not already used in Vol. I ch-13"), but the multimedia plan retires all `drawing-*.png` (wrong style, too small; period errors include "a Renaissance villa at Shangdu").
- **Characters appearing:** Kublai (the Great Kaan), Baian and Mingan (the two brother Masters of the hounds), Marco Polo, Achmath / Ahmad (mentioned)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (stub Notes, Ramusio flag style)
- S-04 Gazetteer authority (Cachar Modun; C17)
- S-05 Character registry (Kublai in PD hero and GEN secondary)
- S-06 Fact verification sheet (*Milione* name reading, aligned with III-10)
- S-08 LaTeX build pipeline (plates, map)
- S-09 Map and diagram pipeline (C17)
- S-10 ✓ Image generation pilot (GEN secondary)
- S-11 ✓ Public-domain artwork sourcing and licensing (Liu Guandao: NPM open data, CC BY 4.0; production uses NPM’s full-scroll IIIF photograph PAB)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `II-04.T5` Placed and print-proofed · media placement (museum hanging scroll, Omont litter miniature, C17) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `II-04.T6` Lint pass and human voice read

### II-04.T1 — Critical and factual fixes
- **Status:** backlog · **Depends:** S-06 ✓, `II-04.T3` (W2: applied in the re-voice pass)
- **Do:**
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - No claim here needed a verdict: each *Factual / fidelity* item cites its Yule line, so apply it as the backlog gives it.
  - Still-open rows use their hedge. When a library check settles one, update `registry/facts.md` first, then the chapter.
- **Done when:** every item under *Factual / fidelity* (and each *Critical* item not owned by `.T3` or a `HOT` task) is applied, or hedged as `registry/facts.md` says; each corrected Note cites the source key given there; a person has checked the changed sentences against the sheet.

### II-04.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #3 (batch 1)
- **Now:** 3,141 words · 71% verbatim · "You must know" 2 · "Anyway" 3 · formula hinges 4 · archaisms 15 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :21 (90%), :27 (96%), :33 (97%), :35 (96%), :47 (90%), :49 (99%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :15, :23, :33, :47, plus any listed under *Dispute handling* above.
  - Drop the opening recap (:11).
  - Cut the closing recap :55 (92 words) to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :15; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Peking → Cambaluc ×1; unglossed first mentions: none. `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: none; unglossed first mentions: Achmath (Ahmad Fanakati). The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### II-04.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `II-04.T3` (the flags are written during the re-voice pass)
- **Now:** 5 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` shows no `ramusio` errors, and the flag count matches the passages found.

### II-04.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `II-04.T3` (re-voice renumbers Notes)
- **Now:** 19 Notes · 0 ★ · 0 without a lead marker · tag [V]
- **Do:**
  - Tag line `**[V]**` is already correct; confirm it against the chapter's evidence (V = seen, R = heard, M = both).
  - Notes with no lead marker: none — resolved 2026-11-17 under `APP.T9` (lint `markers` clean); a person still reads the new markers.
  - Run `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
  - **S-26 ✓ (2026-11-16):** The citation audit covers original Note(s) [21]; preserve the checked locators, scope and corrections from [the locator registry](../../../registry/locators.md) when rewriting or renumbering. These findings do not complete the wider Notes task.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

- **S-19 comparison intake (2026-11-12):** Use `plans/registry/comparanda.md` for this chapter’s checked witness locations and open leads. In the relevant Notes, say what each cited witness reports and give an edition-specific locator; verify lead passages before use, and omit unsupported comparisons. A public-domain quotation must be checked against the scan and attributed to the translation; BLD.T10 is pending. Do not treat shared subject matter as proof of Polo’s presence.

### II-04.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 40 errors · 4 warnings — failing: archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim, you_must_know; warnings: openers, ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-2/ch-04-hunt-traffic.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.

## S-17 research handoff (2026-11-11)

S17-E2 / S17-F2: the Met late-thirteenth-century iron-and-silver paiza is a safe-conduct example, not Marco’s own. Station totals and the Nayan elephant platform are not independently established by this intake. [Source audit and unresolved questions](../../../research/results/S-17-intake.md). Choose within the 2–3 enrichment-item budget; this is a backlog handoff, not a completed manuscript edit.

## S-21 source handoff

S-21 closed 2026-11-13 ([closure](../../../research/results/S-21-closure.md)). Apply in this file's chapter tasks: H6 (hunting cats, falcons: ordinary names; Book's figures, S21-E5).

## U-3 source handoff (2026-11-17)

From the [U-3 intake](../../../research/results/U-3-intake.md) (10 checks, 10 hits). F-53. **Applied 2026-11-17** (body l. 41 and Note [15]). Was: body l. 41 "Beyond that term, however—to wit from March to October—everybody may take these animals" inverts Yule ("Beyond the term I have mentioned … to wit that from March to October"). Make it "Outside that season, however—that is, outside March to October—everybody may take these animals as he list." Note [15]: Pétis gives the same months, not the reverse; "reverse" is Yule's remark (`[@yc, 2.20, note 9]`). Change "✓ Imperial game law type (*Yasa* / Yuan)" to ~, since Yuan law was not checked. These are inputs to the chapter's `.T1`/`.T4`/`.T3` work, not completed edits.

**FINAL-ACCESS (2026-11-17):** *Yuan dianzhang* j. 38, 捕獵 summary table (CADAL/PKU scan, page image): 「正月為頭至七月廿日…不得打捕」, the 20th, not the 28th. Confirms Note [15]; the full article 禁治打捕月日 was not located. [FINAL-ACCESS intake](../../../research/results/FINAL-ACCESS-intake.md)
