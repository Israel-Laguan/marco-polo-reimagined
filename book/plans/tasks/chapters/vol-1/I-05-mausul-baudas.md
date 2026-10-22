# I-05 — Mausul, Baudas, and the Mountain That Moved

**File:** `vol-1/ch-05-mausul-baudas.md` · **Status:** backlog · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 2,994 | 61% | — (n/a in Vol. I) | [16] mismatch; [6] repeats [5] | no |

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Transcription share 61%. Worst block: the mountain miracle, ~1,300 words nearly all Yule, ending "And now you have heard in what wise…". Fix: summarise in the storyteller's words, keep one or two short quoted lines per marvel; target ≤25%. W4 order: 4th in Vol. I (after I-8). — vol-1 C3 · ch-05:29–45
- Book-voice first person left in narration: "I will tell you then, the dictation continues…" (ch-05:29); "Now I have told you something of Baudas…" (ch-05:49). Fix: reported speech or marked quotation (W0 lint: 0). — vol-1 C3 · ch-05:29, :49
- Critique's example rewrite for ch-05:33–35: "The Christians prayed eight days and nights, he says, until an angel told a bishop to seek out a certain one-eyed cobbler — a man so chaste that, when a customer's lovely foot stirred an impure thought, he took his own awl to his eye, as the Gospel bids. 'So you can judge what a holy man he was,' the book adds." — vol-1 C3 · ch-05:33–35

### Factual / fidelity
- Note [1] says "Malik Ṣāliḥ tortured to death 1261"; Mosul fell after a siege in **1262** (general history; not found in the refs). **(unverified)** Check before keeping. Content plan W2 unverified list. — vol-1 m11 · ch-05:57

### Dispute handling and Ramusio flags
— none found

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB). Fix: rotate openers. — vol-1 M6 · ch-05:9
- "Anyway" ×2 (1 "Anyway, next he…"); other hinges 6; book-voice tags ("the book says/insists/adds/assures/must") run 5–7 here. Lint budget: "Anyway" ≤1, "the book insists" ≤2. — vol-1 M6 · ch-05:19, :27
- "Thus Chapter I-5 holds…" reads as help-desk meta. — vol-1 M6 · ch-05:51
- Pet phrases: "factor's" (:13, :51), "shrug" (:51), "without courtesy / softness / irony / surprise" device (:31, Note :79). — vol-1 M6 · ch-05:13, :31, :51
- Long dash-aside: 141 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-05:27
- Scorecard: "the aside is good but the voice is the Book's" (mountain-miracle block). — vol-1 §3 · ch-05

### Notes and apparatus
- Note [16] does not match body [16]: body [16] (line 47) is the mountain-miracle aside on dates, parallels and voicing; Note [16] discusses "Whole Mausul–Baudas block personally traversed"; the parallels are actually in Note [14]. Fix: rewrite [16] as "? Mountain-miracle legend cycle: impossible MS dates; parallels (Gregory Thaumaturgus, Muqaṭṭam, Nakhchivan relocation); voice without sneer or endorsement", and move the traversal note to a new [17] anchored at line 51 after "the Book does not say."; or anchor the current [16] at line 51. Content plan W5. — vol-1 M9 · ch-05:47, :87
- Note [6] repeats [5]. Fix: merge or give it content. — vol-1 m7 · ch-05:65–67
- Production scaffolding: gazetteer reliability tag in a Note ("Gazetteer flags both as *reported_only*"). Fix: keep the reliability idea in plain words. — vol-1 m6 · ch-05:87

### Naming and gazetteer
- Chapter form **Mausul** vs gazetteer **Mosul**. — vol-1 M8 · ch-05
- Missing gazetteer rows: **Kisi**, **Bastra**. — vol-1 M8 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-05.T3`.

### Length and structure
- Chapter-closing recap. Fix: one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-05:51

## Media hooks
- **Hero plate:** I-5 Hulagu shuts the Caliph in the treasure tower — GEN, LdM marvel lens, P. Must get right: Abbasid black robes and turban; Mongol lamellar armour and fur hats. Caption: **exemplum**; Muslim sources say he was rolled in a carpet and trampled; "as the book tells it". Anchor ch-05:25.
- **Secondary plates:** Mountain moves at the cobbler's prayer (LdM; anchor ch-05:43): procession with a cross, Nestorian or Jacobite clergy; **legend**, style as illumination. Critique-only: Baudas silk weavers (ch-05:21) as a textile detail plate (*nasīj*).
- **Maps:** A4 Outbound: Ayas to Hormos (variant line via Mausul/Baudas, dashed).
- **Timelines / diagrams / tables:** D (I-5) How the Caliph died: Polo / Hayton / Rashid al-Din / Ibn al-Furāt. B6 rows "Sack of Baudas 1255 vs 1258" and "Mountain miracle 1275 / 1225, impossible" (B6 placed I-B1).
- **Characters appearing:** Hulagu (Alaü), the Caliph of Baudas (al-Musta'sim, unnamed in text), Möngke, Malik Ṣāliḥ (Note [1]), the one-eyed cobbler and the bishop (unnamed, legend), Marco Polo (as narrator)

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Notes format, ? marker)
- S-04 Gazetteer authority (Mausul, Kisi, Bastra; A4)
- S-05 Character registry (Hulagu and the Caliph in hero plate)
- S-06 Fact verification sheet (m11 Mosul 1262, unverified)
- S-08 LaTeX build pipeline (D table, plates)
- S-09 Map and diagram pipeline (A4)
- S-10 Image generation pilot (GEN hero and secondary)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-05.T1` Critical and factual fixes
- `I-05.T5` Media placement (figures, tables, captions)
- `I-05.T6` Lint pass and human voice read

### I-05.T3 — Re-voice to the S-01 standard
- **Status:** backlog · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #18 (batch 5)
- **Now:** 2,949 words · 61% verbatim · "You must know" 1 · "Anyway" 2 · formula hinges 2 · archaisms 5 · Book first person 2 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :23 (73%), :25 (86%), :31 (95%), :35 (96%), :39 (95%), :43 (100%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :13, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :27 (141), :47 (111). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :41, :51; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Baghdad → Baudas ×4, Kish → Kisi ×3, Mosul → Mausul ×2, Basra → Bastra ×1, Tabriz → Tauris ×1, Peking → Cambaluc ×1; unglossed first mentions: Baudas, Tauris. `python3 tools/lint.py -v vol-1/ch-05-mausul-baudas.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-05.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `I-05.T3` (the flags are written during the re-voice pass)
- **Now:** 1 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-05-mausul-baudas.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-05.T4 — Notes and apparatus to the S-03 convention
- **Status:** backlog · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-05.T3` (re-voice renumbers Notes)
- **Now:** 16 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-05-mausul-baudas.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

### I-05.T6 — Lint green and human read
- **Status:** backlog · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 16 errors · 2 warnings — failing: archaism, asides, budgets, first_person, ramusio, scaffolding, verbatim, you_must_know; warnings: recaps, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-05-mausul-baudas.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.
