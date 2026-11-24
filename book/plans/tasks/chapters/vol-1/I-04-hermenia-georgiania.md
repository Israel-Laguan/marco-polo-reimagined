# I-04 — Lesser and Greater Hermenia; Turcomania; Georgiania

**File:** `vol-1/ch-04-hermenia-georgiania.md` · **Status:** completed (2026-11-24) · **Kind:** narrative

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 1,875 | 1% | — (n/a in Vol. I) | ok [1–28] | no |

**W4 voice pass (2026-11-23).** Ayas trade leads to the mountain route. The Notes distinguish Paipurth, the provenance of reported material, the Baku gloss and Sasanian Derbend. Targeted lint: 1,808 words, 1% Yule overlap, 0 errors, 0 warnings. Current anchors are numbered 1–27.

## Backlog (from critique; not yet tasks)

Each item cites its critique ID (`vol-1.md` C1/M3/m4/nit) and `file:line`. It holds facts only; no fix is decided here unless the critique gave a concrete one.

### Critical
- Heavy Yule transcription: 49% of narrative words inside verbatim 7-gram runs. Fix: re-voice in the ch-01 manner; target ≤25%. W4 order: after I-10, before I-11. — vol-1 C3 · ch-04

### Factual / fidelity
— none found

### Dispute handling and Ramusio flags
- Ramusian (bracketed) text narrated as Book fact: the Paipurth silver mine. Fix: 3–6-word tag ("Ramusio's text adds…"), "◇ Ramusio" in the matching Note. (ch-04:31 "some texts add" is cited as a good model.) — vol-1 M5 · ch-04:19

### Voice and prose
- Opener "Marco Polo starts by narrating that…" (SB). Fix: rotate openers. — vol-1 M6 · ch-04:9
- "Anyway" ×2 (1 "Anyway, next he…"); other hinges 5. Lint budget ≤1. — vol-1 M6 · ch-04:17, :25
- Pet phrases flagged series-wide: "shrug", "factor's". — vol-1 M6 · ch-04:13, :37
- Long dash-aside: 136 words. Fix: ~60–80 words, one key fact + Note cross-ref. — vol-1 M11 · ch-04:17

### Notes and apparatus
- Orphan Note [15] ("Whole Caucasian block personally traversed"): body cites [1]–[14] only, last marker [14] at line 35. Fix: at ch-04:37, "…is a question the notes must keep open. [15]". Content plan W5. — vol-1 M10 · ch-04:71 Tracked for completion in `APP.T9` (2026-11-17). **Closed (best effort) 2026-11-18 under `APP.T9`:** fixed and lint-clean; human read not completed.

### Naming and gazetteer
- "Mosul (Mausul)" reverses the book-form-first rule. — vol-1 nit 2 · ch-04:21
- Chapter forms **Savast**, **Arzinga / Arziron** vs gazetteer Sivas, Erzincan / Erzurum. Fix: gazetteer book_name to Yule forms. — vol-1 M8 · ch-04
- Missing gazetteer rows: **Derbend**, **Ararat**, **Conia**, **Casaria**. — vol-1 M8 · gazetteer.csv
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `I-04.T3`.

### Length and structure
- Chapter-closing recap lists what was just read. Fix: keep one forward-looking sentence, cut the inventory. — vol-1 m9 · ch-04:37

## Media hooks
- **Hero plate:** I-4 The quay at Layas — GEN, Cilician Armenian illumination, P. Must get right: sea castle; lateen ships; spice, silk and cotton bales; Italian and Armenian merchants; camels on the shore. Anchor ch-04:13.
- **Secondary plates:** none in `illustration-plan.md`. Critique-only candidates: oil fountain and mangy camels (ch-04:23; the Book puts it at the Georgian border, the real wells are at Baku: caption accordingly); Iron Gate at Derbend (ch-04:29; Sasanian walls to the Caspian; Alexander attribution is legend); Ararat with eternal snow (ch-04:21; no Ark).
- **Maps:** A4 Outbound: Ayas to Hormos (I-4 – I-8), two variant lines (via Tauris or via Mausul/Baudas), both dashed as reconstructions.
- **Timelines / diagrams / tables:** none
- **Characters appearing:** Marco Polo (as narrator), the Polos, David Melic (King David of Georgia), Baibars (Bundukdar), the Hetumid kings of Cilicia (dynasty), Alexander (legend)

### Period sources (gap-source ledger, 2026-11-13)
- I-4 quay at Layas: **C44** (harbour, galleys, round ships; Cocharelli f. 5r, late) and **C48** (Carte Pisane chart idiom). The site layout comes from CHARLVAR Album 227, R. W. Edwards 1974: Land Castle, Island Castle, harbour, medieval town and bridge (© CHARLV; look only).
- Name: on the Carte Pisane, Ayas is **probably** the red *[l]aiaso*, read between *alexandreta* and red *terſſo* (a fold line runs through it). Later dated charts give *laiaza* (1313), *laiazo* (132[1]) and *Laiacium* (c. 1321) (Lin 2019). The red box at the bend reads *Leuante*: it is the east-wind label, not a port.
- Full ledger: reports/Period sources for Polo plates.md, G4.
- Ayas deeds edition confirmed: Balletto (ed.), *Notai genovesi in Oltremare: atti rogati a Laiazzo…* (1989), `balletto1989laiazzo` (publisher unconfirmed).
- Register: `registry/visual-references.md § Gap-source ledger`.

## Gated by spikes
- S-01 Voice standard
- S-02 Acceptance lint and thresholds
- S-03 Apparatus conventions (Ramusio flag style, Notes format)
- S-04 Gazetteer authority (Savast, Arzinga, Arziron; missing rows; A4)
- S-08 LaTeX build pipeline (plate, A4 figure)
- S-09 Map and diagram pipeline (A4)
- S-10 ✓ Image generation pilot (GEN hero)

## Tasks
_Created after the gating spikes close. Expected shapes:_
- `I-04.T1` Critical and factual fixes — **done (2026-11-24).**
- `I-04.T5` Media placement (figures, tables, captions) · S-08 ✓: **done (2026-11-24; hero plate `#fig-i-4-layas-quay` and Map A4 link placed and proofed).**
- `I-04.T6` Lint pass and human voice read — **done (2026-11-24; E0 · W0).**

### I-04.T3 — Re-voice to the S-01 standard
- **Status:** done (2026-11-24) · **Depends:** S-01 ✓, S-02 (lint), S-03 (flag wording) · **W4 order:** #22 (batch 6)
- **Current lint (2026-11-24):** 1,875 w · 1% verbatim · 1 quotes · 0 asides; 0 errors, 0 warnings. Measurements are automated; source, apparatus and human review remain separate. Literary pass replaced "The Book" / "a man who" repetition with concrete scene openings and sensory pauses (Ayas quay, Turcoman uplands, Ararat pass timing, naphtha spring, Derbend bottleneck, St Leonard's fish), added marked Yule quote (*"a hundred shiploads"*), removed the duplicated closing recap sentence (m9), and tightened the outro into I-05.
- **Earlier baseline:** 2,330 words · 49% verbatim · "You must know" 1 · "Anyway" 2 · formula hinges 4 · archaisms 3 · Book first person 0 · asides 3
- **Do:**
  - Retell to ≤ 15% verbatim. Worst blocks: :15 (84%), :19 (74%), :21 (77%), :29 (72%), :31 (72%), :33 (76%).
  - Flag Ramusio-only passages (inline tag + "◇ Ramusio-only" Note) at :21, :33, plus any listed under *Dispute handling* above.
  - Asides over 80 words: :17 (138), :25 (99). Trim; move traveller/scholar lists to Notes.
  - Cut any closing recap to ≤ 1 forward sentence.
  - Remove "So/Thus …" restatement paragraphs :37; merge any identification content into Notes.
  - Zero archaisms, Book first person and "You must know" outside marked quotes; "Anyway" ≤ 1; formula hinges ≤ 3; quotes ≤ 2 per scene.
  - Resolve every item under *Voice and prose* and *Length and structure* above, and fold in this file's T1/T2 items (W2 facts, W3 flags) in the same pass.
  - Re-measure length after the re-voice (pilot dropped 40%); apply a cut plan only if still over 3,200; floor 1,800.
  - **Naming (S-04 ✓):** Use the book form (`gazetteer.csv` `book_name`) throughout; give each place one gloss on first mention (book form + modern form, e.g. *Cascar (Kashgar)*); no bare modern or alternate forms outside quotations. Chapter-specific conflicts are listed under *Naming and gazetteer* above. Now: bare variants: Layas → Ayas ×2, Erzingan → Arzinga ×2, Iron Gate → Derbend ×2, Mosul → Mausul ×2, Iconium → Conia ×1, Sivas → Savast ×1, Erzrum → Arziron ×1, Georgia → Georgiania ×1 (+2 more); unglossed first mentions: Ayas, Baudas. `python3 tools/lint.py -v vol-1/ch-04-hermenia-georgiania.md` lists them as `name_policy` warnings; the rule becomes an error once every chapter has had its pass.
  - **People (S-05 ✓):** Same rule for people (`plans/registry/characters.yaml`): the book form throughout (Yule's form where Polo names the person, e.g. *Cublay*, *Alaü*, *Argon*; the modern form where he does not, e.g. *Chabi*, *Bolad*), glossed once on first mention (*Cublay (Kublai)*); no bare variant outside quotations. Now: bare variants: none; unglossed first mentions: Bundukdar (Baibars). The lint lists them as `name_policy` warnings marked (S-05).
- **Done when:** lint green (S-02) + human voice read against II-2 (`VOICE-GUIDE.md` v2)

### I-04.T2 — Ramusio flags and labels to the S-03 convention
- **Status:** done (2026-11-24; Notes [12], [14], [20], [26] labelled `Ramusio-only.` / `Ramusio-only in part.`) · **Depends:** S-03 ✓, `I-04.T3` (the flags are written during the re-voice pass)
- **Now:** 2 Ramusio-only passage(s) reproduced from the first draft (`tools/ramusio-manifest.json`; Yule brackets). The manifest catches only near-verbatim passages, so read the covered Yule range for brackets the re-voice has paraphrased.
- **Do:**
  - Every Ramusio-only (or Pipino-, Jacopo-, Zelada-only) passage gets a 3–6-word inline flag naming its source, one flag per contiguous passage; a wholly Ramusian paragraph opens by saying so.
  - Its Note carries the label "Ramusio-only." (or the matching name) straight after the lead marker. The label is provenance and sits beside a reliability marker; ◇ is not used for it.
- **Done when:** `python3 tools/lint.py -v vol-1/ch-04-hermenia-georgiania.md` shows no `ramusio` errors, and the flag count matches the passages found.

### I-04.T4 — Notes and apparatus to the S-03 convention
- **Status:** done (2026-11-24; 28 Notes, 0 ★, lint green) · **Depends:** S-03 ✓, `APP.T2` (★ sweep), `I-04.T3` (re-voice renumbers Notes)
- **Now:** 28 Notes · 0 ★ · 0 without a lead marker
- **Do:**
  - Run `python3 tools/lint.py -v vol-1/ch-04-hermenia-georgiania.md` and clear the `markers`, `tags` and `citations` errors; order markers per *Apparatus conventions* (one citation per anchor, ≤ 4 marker clauses per Note, `~` with a space).
  - Any chapter-specific Notes fixes from *Notes and apparatus* in the backlog above (orphans, swaps, renumbering) belong here too.
- **Done when:** the lint shows no `markers`, `tags` or `citations` errors for this file, and a person has read the Notes.

- **S-19 comparison intake (2026-11-12):** Use `plans/registry/comparanda.md` for this chapter’s checked witness locations and open leads. In the relevant Notes, say what each cited witness reports and give an edition-specific locator; verify lead passages before use, and omit unsupported comparisons. A public-domain quotation must be checked against the scan and attributed to the translation; BLD.T10 is pending. Do not treat shared subject matter as proof of Polo’s presence.

### I-04.T6 — Lint green and human read
- **Status:** done (2026-11-24; E0 · W0) · **Depends:** every other task in this file · S-02 ✓
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 16 errors · 4 warnings — failing: archaism, asides, budgets, citations, ramusio, verbatim, you_must_know; warnings: names, ramusio, sentence
- **Do:** from `book/`, run `python3 tools/lint.py -v vol-1/ch-04-hermenia-georgiania.md`; fix every error; take the warnings into the human read.
- **Done when:** the lint exits 0 for this file, its warnings have been reviewed, and a human has read it for voice against II-2.


## S-16 handoff — T4

- **Status:** done (2026-11-24; S16-E1/E8 Sasanian Derbend and earlier Baku naphtha records applied in body and Notes [16] and [22]). See [S-16 closeout](../../../research/results/S-16-closeout.md); choose within the chapter enrichment and aside budgets.
