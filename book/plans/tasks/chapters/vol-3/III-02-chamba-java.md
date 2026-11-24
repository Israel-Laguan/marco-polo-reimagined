# III-02 — Chamba, Java, Locac, Pentam: The Southern Ocean Road

**File:** `vol-3/ch-02-chamba-java.md` · **Status:** v3 drafted, reader review pending · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,814 | 46% | [R/M] | issues: Note [13] placeholder; Notes [4]–[6] overlap | no |

**W4 voice pass (2026-11-23).** 1,810 words, 3% Yule overlap, zero errors and warnings. Notes 6–7, 18–20 and 26 carry F-51, F-52 and F-43. Notes 15–16 distinguish the Book’s spice list from the market comparison.

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-3.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Misquoted epigraph: "When you leave the port of Zayton…" — Yule has "You must know that on leaving the port of Zayton…". Fix: restore the exact wording. — vol-3 C1 · ch-02:4
- Transcription: 46% of narrative in 7-gram Yule runs (threshold ≤ 25%). Fix: paraphrase at least half of each long run. — vol-3 C3 · ch-02
- "Soft" label tic ×2: "Soft digression now:" (:23), "Soft close here:" (:39); also Note [13] "Soft close toward Java the Less" (:69). Fix: strip the labels. — vol-3 C2 · ch-02:23, :39, :69

### Factual / fidelity
- "Yule leans toward… or the return voyage still ahead": Yule inclines to the Geographic Latin 1288 and the c. 1290 Indian mission (`yule-vol2.txt:14790`) and does not propose the return voyage. — vol-3 n8 · ch-02:21
- Note [11] dates the Rāma Khamhaeng inscription "~1292–93"; the date is Yule's ("almost exactly coincident with Polo's voyage"), but the later authenticity debate is not mentioned. **S-06 sweep:** F-43. — ch-02:65

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- "Anyway" ×3 (:17, :27, :33) → at most one; "A quick note" (:17). Scorecard: 9 hinges. — vol-3 m14 · ch-02:17, :27, :33
- Soft-close variant of the recap closer ("Soft close here: …", with "it is enough that"). Fix: one bridging sentence or delete. — vol-3 M10 · ch-02:39
- Pre-summary and mid-chapter restatement ("Thus Chamba stands…", "Thus the southern Ocean road narrows…"). Fix: cut where an aside already exists. — vol-3 M10 · ch-02:21-23 (also :37)

### Notes and apparatus
- Note [13] is a placeholder that says nothing. Fix: give it content or drop the citation from the body. — vol-3 m9 · ch-02:69
- Notes [4]–[6] overlap (Champa war records / Marco's presence / "★ Dispute: personal presence"). — vol-3 §3 scorecard · ch-02:51-55
- ★ ×3 (incl. Note [6] "★ Dispute"); convert to ✓ ~ ✗ ◇ ? and merge "★ Dispute" into its neighbour. — vol-3 M9 · ch-02:55

### Naming and gazetteer
- Gazetteer lacks a row for Sondur/Condur, which the chapter relies on. — vol-3 m4 · ch-02
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-02.T3`.

### Length and structure
— none found (1,814 words; "Solid and lean")

## Media hooks
- **S-22 maritime research lead:** `niziolek2018revisiting` and `registry/enrichment.md` S22-E1: the Java Sea wreck cargo can be investigated as a regional trade comparison. Its reassessed date may be earlier than Polo; it does not establish a port, route or ship design for his voyage. Read the study before using a Note.
- **Hero plate:** III-2 *Junks lift their rudders in the shoal strait* — GEN, Javanese temple relief, landscape; must get right: raisable axial rudders, mangrove coast, Malay perahu — see `illustration-plan.md` (critique §4 anchor: "great ships in passing this channel have to lift their rudders", Bintan coast)
- **Secondary plates:** none in plan. Critique §4 alternative not adopted: Elephant tribute from Chamba (Cham dress, brick *kalan* towers; caution: the pity-tale softens a brutal 1282–85 war)
- **Maps:** none placed here (A16 passes Chamba as "possible")
- **Timelines / diagrams / tables:** none
- **Characters appearing:** Marco Polo, Kublai (Great Kaan), Sagatu (Sogetu), Accambale (king of Chamba), Tughan (Toghan), Rustichello; comparative sources: Odoric, Niccolò de' Conti, Ibn Battuta, Duarte Barbosa

### Period sources (gap-source ledger, 2026-11-13)
- Java: Singhasari temple dress, draft **C47** (Wereldmuseum RV-1403-1623, -1624, -1682; late 13th c. per CKC 2023, `ckc2023singasari`; returned to Indonesia in 2023). Images in media/references, look only.
- Register: `registry/visual-references.md § Gap-source ledger`.

## Gated by spikes
- S-01, S-02, S-03, S-04 (Sondur/Condur row), S-06 (n8), S-08, S-10 ✓

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `III-02.T5` Media placement (figures, captions) · S-08 ✓: write figures and tables as `registry/markdown-conventions.md` says; done when `tools/build/build.sh` places this file's figures with no placeholder or size warning.
- `III-02.T6` Lint pass and human voice read

### III-02.T1 — Critical and factual fixes
- **Status:** backlog · **Depends:** S-06 ✓, `III-02.T3` (W2: applied in the re-voice pass)
- **Do:**
  - **Facts (S-06 ✓, `registry/facts.md`):**
    - The critique's items needed no verdict: each cites its Yule line, so apply it as the backlog gives it.
    - F-43: Note [11] keeps the inscription, credited to Yule and hedged: "an inscription of Sukhothai dated 1292, which Yule thought almost exactly coincident with Polo's voyage (its authenticity was later questioned)".
  - Still-open rows use their hedge. When a library check settles one, update `registry/facts.md` first, then the chapter.
- **Done when:** every item under *Factual / fidelity* (and each *Critical* item not owned by `.T3` or a `HOT` task) is applied, or hedged as `registry/facts.md` says; each corrected Note cites the source key given there; a person has checked the changed sentences against the sheet.

### III-02.T3 — Re-voice to the S-01 standard
- **Status:** v3 draft recorded; literary/storytelling pass completed (2026-11-24); independent human voice review pending · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #32 (batch 8)
- **Current lint (2026-11-24):** 1,830 w · 3% verbatim · 0 quotes · 1 asides; 0 errors, 0 warnings. Varied imperative openings at Chamba, Java, and Pentam, added a narrator transition into the date variants and shoal-rudder scene, and tightened the closing bridge into III-3. Measurements are automated; source, apparatus and human review remain separate.
- **Earlier baseline:** 1,792 words · 46% verbatim · "You must know" 1 · "Anyway" 3 · formula hinges 4 · archaisms 0 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (75%), :19 (76%), :25 (93%), :29 (97%), :31 (96%), :35 (83%).
  - Asides over 80 words: :27 (112), :33 (98). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :21, :37; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Bintan → Pentam ×2, Champa → Chamba ×1, Sumatra → Java the Less ×1; unglossed first mentions: Condur, Locac, Pentam, Malaiur. `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: Kublai → Cublay ×1; unglossed first mentions: none. The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### III-02.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `III-02.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` shows no `ramusio` errors, and the flag count matches the passages found.

**S-21 research handoff (2026-11-13):** During T3/T4, preserve the Book’s claim that Java produces the listed spices as an attributed claim. Yule proposes a market for nutmeg and cloves; do not present re-export or absence of local cultivation as conclusively established for 1290. Wang et al. discuss a much earlier Javan clove find while leaving its source unresolved. See `research/results/S-21-high-priority-intake.md` and S21-E13.

### III-02.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `III-02.T3` (re-voice renumbers Notes)
- **Now:** 13 Notes · 0 ★ · 0 without a lead marker · tag [R/M]
- **Do:**
  - Replace tag `[R/M]` with `**[M]**` (compound tags are retired; if the lean matters, say it in one clause of Note [1]).
  - 3 ★ rating(s): handled by the `APP.T2` sweep; here, check that none remain and that merged "★ Dispute:" text reads as a proper clause.
  - Notes with no lead marker: none — resolved 2026-11-17 under `APP.T9` (lint `markers` clean); a person still reads the new markers.
  - "Dispute" label in Note(s) [6], [11]: none remain — removed or merged 2026-11-17 (`APP.T2`/`APP.T9`).
  - Run `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

- **S-19 comparison intake (2026-11-12):** Use `plans/registry/comparanda.md` for this chapter’s checked witness locations and open leads. In the relevant Notes, say what each cited witness reports and give an edition-specific locator; verify lead passages before use, and omit unsupported comparisons. A public-domain quotation must be checked against the scan and attributed to the translation; BLD.T10 is pending. Do not treat shared subject matter as proof of Polo’s presence.

### III-02.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 27 errors · 4 warnings — failing: asides, budgets, length, markers, quote_verify, ramusio, scaffolding, tags, verbatim, you_must_know; warnings: ramusio, recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-3/ch-02-chamba-java.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.

## S-21 source handoff

S-21 closed 2026-11-13 ([closure](../../../research/results/S-21-closure.md)). Apply in this file's chapter tasks: H3 (Java spice list: Book's claim; re-export attributed; S21-E4, E13).

**S-18 strict return:** Pelliot entry 313 in [Toyo Bunko OCR](https://dsr.nii.ac.jp/toyobunko/III-2-F-c-104/V-2/page/0206.html.en) identifies Pentan with Bintan and proposes a Singapore Strait route; attribute both as his interpretations, not proof of Polo’s personal course. See [intake](../../../research/results/S-18-strict-follow-up-2026-11-16-intake.md).

## U-2 source handoff (2026-11-17)

From the [U-2 intake](../../../research/results/U-2-intake.md) (14 checks against the *Yuan shi*, 13 hits). These are inputs to `.T1`/`.T4`, not completed edits.

- **Applied 2026-11-17.** **F-51, Note [3]:** keep the body (it tells the Book's story); correct the Note. No 1278 expedition: that year Sogetu opened relations and the king was invested (j. 210). The war ran 1282–84 and ended in withdrawal; the recall request, the tribute promise and three elephants came after it (j. 13). No twenty-elephant tribute is recorded for Champa (twenty tame elephants a year is Burma's 1297 offer). Sogetu died in the Annam war, 1285. Cite `[@yuanshi1370, juan 13, 129, 210]`; "Polo compresses" is interpretation.
- **Applied 2026-11-17 (Note [8]; body l. 27 unchanged).** **F-52, Note [8] and body l. 27:** "loss ~3,000" becomes "more than 3,000 dead by the return to Quanzhou (Shi Bi's biography)". The envoy is Meng Qi only in Gao Xing's biography; "branded" holds. The force is 20,000 in 500 or 1,000 ships, and only 5,000 went. Optional: the commanders were caned and fined a third, Gao Xing excepted. Cite `[@yuanshi1370, juan 17, 162, 210]`.

**FINAL-ACCESS handoff (2026-11-17):** Maspero, "Le royaume de Champa", *T'oung Pao* 12 (1911), ch. VIII (OCR read): Sögetü ("Sagatou") campaign 1281–85; Champa "délivré des Mongols" and Sögetü's death in 1285, p. 474; no tribute passage found beyond p. 592. Brandes's *Pararaton* (VBG 49, OCR read): the Tatar envoys and troops attack Daha; Raṅga Lawe then turns on the Tatars over the princesses (Javanese text pp. [23]–[24]; translation page not read). Leads for Notes [3] and [8]; no edit made. [FINAL-ACCESS intake](../../../research/results/FINAL-ACCESS-intake.md)

## W4 audit (2026-11-23)

Re-voiced to Voice Guide v3, split stacked Notes to 30 sequential claim-level `[n]` Notes, preserved `U-2` Sogetu/Java handoffs and standardized Ramusio labels. Lint: `PASS E0 W0 (1,835 w · 3% verbatim · 0 quotes · 1 asides)`.
