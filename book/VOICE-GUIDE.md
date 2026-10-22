# Voice Guide — Marco Polo Retelling (v2)

Use this for every chapter re-voice (content plan W4). v2 replaces v1's list of "typical hinges" with measurable rules. The reference chapter is **II-2 *Person & Palace*** (spike S-01 pilot); the before/after excerpt is in `plans/spikes/S-01-voice-standard.md`.

## Core voice

Write as a **storyteller recounting what Marco Polo / *Il Milione* narrates** — not as an epic novelist inhabiting the Middle Ages, not as a dry encyclopedia, and never as the Book itself.

Tone: clear, oral, intelligent, readable. Warm storyteller. Correct, publishable modern English that still sounds spoken. Not slangy, not help-desk, not archaic pastiche, not high-literary third-person epic.

**Retell, don't transcribe.** Read the Yule passage, close it, and say what happens in your own sentences. Compress catalogues (arsenals, gates, robes, dishes) into one or two sentences that keep every fact and the one detail a listener would repeat. Keep Polo's own judgements ("the greatest Palace that ever was") as his, attributed or quoted, never adopted by the narrator.

## Measurable rules

| Rule | Limit | Notes |
|---|---|---|
| Verbatim Yule (words in shared 7-grams, narrative incl. epigraph) | **≤ 15%** | Pilot: 80% → 3%. I-1: 7%. |
| Marked Yule quotations | **≤ 2 per scene, ≤ 8 per chapter**, each ≤ 25 words | Italic inside quotation marks: *"in good sooth 'tis named well."* Choose for flavour, not information. Epigraph not counted. |
| Archaisms outside marked quotes (hath, doth, foison, certes, sundry, whilst, thereof, insomuch, to wit, 'tis…) | **0** | Pilot: 18 → 0. |
| Book first person outside marked quotes ("I tell you", "I assure you", "Now I will…", "I ought to mention") | **0** | Turn into reported speech: "Polo insists…", or quote it. |
| "You must know" outside marked quotes | **0** | |
| "Anyway" | **≤ 1** per chapter | Never "Anyway, next he mentions X". |
| Formula hinges ("Marco Polo starts by narrating", "Polo narrates", "According to the book", "next he mentions", "Then Polo describes", "Tradition has it") | **≤ 3** per chapter in total | |
| Any one attribution verb (says, explains, adds, insists, notes…) | **≤ 4** per chapter | Rotate. Rhetorical "says nothing of" doesn't count. |
| Asides (paragraphs opening with "—") | **≤ 80 words** each, **≤ 4** per chapter | Lists of later travellers and scholars go to Notes. |
| Opening recap ("The Book has told…") | **0** | Start in the scene. |
| Closing recap | **≤ 1 sentence, ≤ 25 words**, forward-looking | Pilot: "Inside these walls the court now comes to life: the feasts, the robes of gold, and the twelve thousand Keshican." |
| Mid-chapter "So/Thus X…" restatement paragraphs | **0** | Merge any identification content into Notes. |
| Narrative length | **1,800–3,200** words | Expect a catalogue chapter to shrink 25–40% on re-voice (pilot 3,167 → 1,894). Don't pad back to length. |
| Average sentence length | **≤ 25 words** (advisory) | Pilot 22.5; before 29.1; I-1 23.1. |

## Openers and transitions

Open a chapter, scene or paragraph on something concrete. Rotate among:

1. **The person or thing:** "Cublay Kaan is not drawn as a giant."
2. **The place:** "Off the north-west corner spreads a lake…"
3. **The time or season:** "Winter is the season of the capital."
4. **A number or measure:** "Taidu is a square, six miles a side…"
5. **An action:** "At night a great bell sounds in the middle of the city."
6. **A short signpost** (≤ 4 words, at most twice per chapter): "Then the household." / "Then the city."
7. **Attribution** (sparingly): "Among the Tartars, Polo explains, is a tribe…"

No two consecutive paragraphs open with the same two words or the same opener type.

**Leaving an aside:** just resume with the next paragraph. Don't announce the return.

## Ramusio and later layers

Anything Yule brackets as Ramusio-only gets two things: **a few words in the narrative** and **a label in the Note** (see *Apparatus conventions* below for the full rules). Inline, rotate:

- "Ramusio's text adds…" / "Ramusio's version fills in…"
- "In Ramusio's version…"
- "(…, Ramusio adds)"
- "in another Ramusian passage" (continuation only, after an earlier flag in the same chapter)

A wholly Ramusian paragraph opens by saying so (model: II-13 at "So far the older texts…"). The same applies to Pipino, Jacopo d'Acqui and Zelada-Latin-only material, each named.

## Naming

- Book / medieval form first; modern equivalent in parentheses on first mention in a chapter, e.g. Bocara (Bukhara).
- Book names thereafter, per `gazetteer.csv`.

## Inline dispute notes

When something is contested, inaccurate, second-hand, or exaggerated, either correct it in one clause inside the narrative ("Chinese sources count eleven gates") or interrupt with a short aside (≤ 80 words), then simply resume. Don't dump all disputes into a separate "Reliability" table.

## Apparatus conventions (S-03, closed 2026-10-22)

One system, four parts: **Notes** (numbered, at the chapter's end), **markers** (a verdict on each claim), **tags** (a verdict on the whole chapter) and **Ramusio labels** (where the text comes from). Each answers a different question, and none of them stands in for another.

### Chapter shape

1. Title (+ optional short epigraph: exact Yule wording, or marked *(adapted)*)
2. Tag line: `**[V]**`, `**[R]**`, `**[M]**` or `**[reception]**` on its own line (Vols. II–III narrative chapters only)
3. `---`, then continuous storyteller narrative with inline citations [1], [2]…
4. `## Notes`

### Reliability markers (Notes only)

| Marker | Meaning |
|---|---|
| ✓ | corroborated: an independent source (Yuan, Persian, Arab, archaeology) confirms it |
| ~ | plausible: it fits, but a detail, date, scale or name is under strain |
| ✗ | probably wrong or exaggerated: contradicted, or a copyist's or later error |
| ◇ | marvel or hearsay: wonder-tale, legend or second-hand report, kept as what the Book says |
| ? | contested: scholars disagree and the evidence does not settle it |

- Markers appear **only in Notes, only at the start of a clause**, never in the narrative.
- The **★ system is retired** (★★★ → ✓, ★★ → ~, ★ → ?; see the sweep rules below). The old "★ Dispute:" label is retired with it. A contested point takes `?` and a sentence saying what is contested.
- `~` is a marker only when a space follows it. Write approximations as "about" or "c." ("about 60 miles", never "~60 miles").
- ◇ means *marvel or hearsay* and nothing else. It does **not** mean Ramusio (see below).
- Use the plain characters ✓ ✗ ◇ (U+2713, U+2717, U+25C7), never emoji forms, so the print build can map them to one symbol font.

### Notes

1. **One Note per citation, one citation per anchor.** A Note opens with the verdict on the anchored passage: one marker, or a pair "core / detail" when they differ ("✓ / ~ …"). Clauses after it carry their own markers. More than four marker clauses means the anchor is doing too much: split the sentence and add a citation.
2. Shape: `[n] ✓ The claim in a few words. Evidence and corroboration. Comparative witnesses.` Cite modern scholars by well-known position only; no invented page numbers.
3. **No placeholder Notes** ("see [5]", "soft transition", "companion framing only"). A Note that only points to another Note is merged into it and its citation is dropped.
4. **No duplicate Notes** on one claim: "★ Dispute:" fragments and "Dispute hook / Dispute stance:" labels are merged into the Note they belong to.
5. **No scaffolding or tooling language** (`/workspace`, gazetteer labels like *visited*, "outline", "drafter"). Facts awaiting verification are marked **To verify (S-06)**.
6. Every Note opens with a marker. Front and back matter follow the same rule.

### Tags (whole-chapter verdict, Vols. II–III)

| Tag | Meaning |
|---|---|
| **[V]** | most of the chapter rests on what Polo says he saw or did |
| **[R]** | most of it rests on what he heard: reports, hearsay, court intelligence |
| **[M]** | both, in comparable measure |
| **[reception]** | the chapter is about the Book's afterlife, not about travel (III-10 to III-12) |

- **Compound tags are retired.** `[V/M]` and `[R/M]` fold into `[M]`. If the lean matters, say it in one clause of Note [1].
- Vol. I chapters, front matter and back matter carry no tag. The outline reserves tags for the realm and sea volumes, and Vol. I is one outward journey framed by its own front matter.
- Assigned tags (from the outline; each chapter's `.T4` confirms): II-8, II-14, III-2, III-3, III-4, III-5 → **[M]** (all were compounds); III-7 **[R]**; III-8 **[M]**; III-9 **[V]**; III-10, III-11, III-12 **[reception]**. All other tags stay as they are.

### Ramusio and later layers

A passage Yule brackets as Ramusio-only (or Pipino-only, Jacopo-only, Zelada-Latin-only) is flagged in **two places**:

1. **In the narrative**, a flag of 3–6 words naming the source (variants under *Ramusio and later layers* above). The flag stands at the start of the passage and covers **one contiguous passage**; a second, separate Ramusian detail in the same paragraph needs its own flag. A wholly Ramusian paragraph opens by saying so. Pipino's Latin, Jacopo d'Acqui and the Zelada Latin are named in full; the sigla Z, P and R never appear in prose.
2. **In the Note**, the label **"Ramusio-only."** (or "Pipino-only.", "Jacopo-only.", "Zelada-only.") directly after the lead marker, followed by the content: `[4] ? Ramusio-only. Carat appraisal of beauty. …`

The label is **provenance**, not reliability. It sits beside a reliability marker and never replaces one: Ramusian detail can be ✓ (Kinsay's markets) or ◇ (a marvel). Do not label material Ramusio shares with the older texts; Yule's brackets decide.

### ★ → marker sweep rules (for `APP.T2`)

- ★★★ → ✓ · ★★ → ~ · ★ → ?
- **A ★ on a clause that already has ✓ ~ ✗ ◇ ?** is deleted (e.g. "✓ Salt cakes… ★★★ Vogel" → "✓ Salt cakes… Vogel").
- A bare ★ is **✗** when the same clause calls the claim wrong, scrambled or exaggerated; **◇** when it calls it myth, topos or legend.
- "Dispute:" is dropped wherever it appears. A Note that is only "★ Dispute: …" is merged into the Note of its anchor, or given a lead marker by hand if it stands alone.
- The sweep is run as a script that **proposes** each change; a person confirms each of the ~81 ★ (the meaning is per clause).

### How the apparatus survives into LaTeX

The Markdown stays plain; the build (S-08) converts mechanically because every element has one fixed shape.

| Element | Markdown | LaTeX build |
|---|---|---|
| Citation | `[n]` plain text, sequential | filter turns `[n]` + the `## Notes` list into per-chapter endnotes (S-08 may choose footnotes; nothing here changes) |
| Marker | literal ✓ ~ ✗ ◇ ? at clause start | filter wraps the five glyphs in one macro that sets them in a symbol font (or `pifont`) |
| Tag line | a paragraph that is only `**[V]**` etc. | filter sets it as a small-caps line under the title |
| Ramusio flag | ordinary words | no markup needed |
| How-to-read box | `::: howto … :::` (Pandoc fenced div) | boxed environment |

For S-08: confirm a font with ✓ ✗ ◇ coverage and the endnote-vs-footnote choice.

## Base text and honesty

- Working base: Yule–Cordier (PG / 1903–1920 tradition), eclectic toward the Geographic Old French line.
- Keep factual coverage from the outline beats; don't invent itinerary or quotations. Every quotation must be findable in `refs/`.
- Flag Ramusio, Pipino, Jacopo d'Acqui and later embroidery honestly; never absorb them silently as primary fact.
- Cite modern scholars by well-known positions (Yule, Larner, Benedetto, Moule–Pelliot, de Rachewiltz, etc.); no fabricated page numbers.

## What to avoid

- Yule's syntax with modern spelling ("He has also caused the whole hill to be covered…") — that is transcription, however lightly edited.
- High-literary epic pastiche ("In the late summer of the year of Our Lord…")
- Silent omniscient third person that pretends to *be* the Book
- Long academic digressions mid-paragraph
- Help-desk phrasing ("In this chapter we will explore…")
- Slang or jokey sarcasm that undercuts the material

## Re-voice checklist (per chapter)

1. Read the backlog file in `plans/tasks/chapters/` and the Yule chapters it covers.
2. Retell scene by scene; pick at most two quotations per scene.
3. Apply the chapter's W2 facts and W3 Ramusio flags in the same pass (*Apparatus conventions*).
4. Cut recaps; merge stub Notes; renumber.
5. Measure (lint, S-02) against the table above.
6. Human read: does it sound like II-2? Is any fact, flavour or citation lost?
