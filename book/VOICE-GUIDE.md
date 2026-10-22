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

Anything Yule brackets as Ramusio-only gets a short inline tag (3–6 words) plus "◇ Ramusio-only: …" in the matching Note. Rotate the tag:

- "Ramusio's text adds…"
- "Ramusio's version fills in…"
- "In Ramusio's version…"
- "(…, Ramusio adds)"
- "in another Ramusian passage"

A wholly Ramusian paragraph opens by saying so (model: II-13 at "So far the older texts…"). The same applies to Pipino, Jacopo d'Acqui and Z-only material, each named. Final wording belongs to S-03; these are the pilot's working variants.

## Naming

- Book / medieval form first; modern equivalent in parentheses on first mention in a chapter, e.g. Bocara (Bukhara).
- Book names thereafter, per `gazetteer.csv`.

## Inline dispute notes

When something is contested, inaccurate, second-hand, or exaggerated, either correct it in one clause inside the narrative ("Chinese sources count eleven gates") or interrupt with a short aside (≤ 80 words), then simply resume. Don't dump all disputes into a separate "Reliability" table.

## Citations and Notes

1. **Numbered citations** inline: [1], [2], [3]… in order, each used once.
2. After the narrative, a single **## Notes** section listing [1], [2]… with source, why disputed, and comparative witness.
3. Markers inside Notes: ✓ corroborated · ~ plausible · ✗ likely wrong/exaggerated · ◇ second-hand or Ramusio-only · ? contested.
4. No placeholder Notes ("see [5]", "soft transition"), no tooling language. Facts awaiting verification are marked **To verify (S-06)**.

## Chapter shape

1. Title (+ optional short epigraph, verified in Yule)
2. Head tag [V] / [R] / [M]
3. Continuous storyteller narrative
4. **## Notes** with numbered entries

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
3. Apply the chapter's W2 facts and W3 Ramusio flags in the same pass.
4. Cut recaps; merge stub Notes; renumber.
5. Measure (lint, S-02) against the table above.
6. Human read: does it sound like II-2? Is any fact, flavour or citation lost?
