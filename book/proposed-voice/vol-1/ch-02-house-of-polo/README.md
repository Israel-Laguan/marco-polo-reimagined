# I-02: The House of Polo and the Elder Voyage

**Status:** Pending Theatrical Voice Review  
**Canonical Manuscript:** [`book/vol-1/ch-02-house-of-polo.md`](file:///home/anthony/code/marco-polo-reimagined/book/vol-1/ch-02-house-of-polo.md)  
**Proposed Sandbox Draft:** `book/proposed-voice/vol-1/ch-02-house-of-polo/proposed.md`  
**Chapter Task & Fact Sheet:** [`book/plans/tasks/chapters/vol-1/I-02-house-of-polo.md`](file:///home/anthony/code/marco-polo-reimagined/book/plans/tasks/chapters/vol-1/I-02-house-of-polo.md)  
**Voice Guide:** [`book/proposed-voice/PROPOSED-VOICE-GUIDE.md`](file:///home/anthony/code/marco-polo-reimagined/book/proposed-voice/PROPOSED-VOICE-GUIDE.md)  
**Big-Picture & Baton Plan:** [`book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md`](file:///home/anthony/code/marco-polo-reimagined/book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md)  

---

## Quick-Start Prompt for Separate Chat

Copy and paste this into a new chat:

```text
Let's calmly analyze and revise I-02 (The House of Polo and the Elder Voyage) to apply the theatrical single-narrator voice.
1. Read @[book/proposed-voice/PROPOSED-VOICE-GUIDE.md], @[book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md], and this chapter's diagnostic brief @[book/proposed-voice/vol-1/ch-02-house-of-polo/README.md].
2. Read the current chapter @[book/vol-1/ch-02-house-of-polo.md] and its fact/apparatus constraints in @[book/plans/tasks/chapters/vol-1/I-02-house-of-polo.md].
3. First, show me your analysis and specific proposal for:
   - Big-Picture Arc & Mode Cue: Narrative Arc: Follow Niccolò and Maffeo from Constantinople and Soldaia across the Volga and Bocara to Cublay's court and back to Venice.
   - Pillar 1: Dramatic Introduction (catching the Incoming Baton — "From I-01: The Venetian trading house of Polo sending two brothers with a pouch of jewels across the Greater Sea." — and exploding with theatrical scale/stakes)
   - Pillar 2: Inserted Dramatic & "For Modern Audiences" Interludes
   - Pillar 3: Dramatic Outro (landing the closing image and handing off the Outgoing Baton — "To I-03: Returning to Venice in 1269 with the Kaan's golden tablet while the cardinals at Viterbo stall on electing a Pope, and young Marco waits.")
   - Pillar 4: Moving immersion-breaking inline scholar/Ramusio citations and academic em-dash asides into the Notes.
4. After we align on the proposal, write the revised chapter to book/proposed-voice/vol-1/ch-02-house-of-polo/proposed.md and run `python3 tools/lint.py -v proposed-voice/vol-1/ch-02-house-of-polo/proposed.md` from `book/`.
```

---

## Big-Picture Framing for I-02 (from `BIG-PICTURE-NARRATION-PLAN.md`)

* **Series Position:** Act I: The Elder Voyage (1260–1269)
* **Narrator Mode / Gear Cue:** Narrative Arc: Follow Niccolò and Maffeo from Constantinople and Soldaia across the Volga and Bocara to Cublay's court and back to Venice.
* **Incoming Baton (Catch in Opening Paragraph):** From I-01: The Venetian trading house of Polo sending two brothers with a pouch of jewels across the Greater Sea.
* **Outgoing Baton (Hand Off in Closing Paragraph):** To I-03: Returning to Venice in 1269 with the Kaan's golden tablet while the cardinals at Viterbo stall on electing a Pope, and young Marco waits.

---

## Diagnostic Audit Against the 4 Pillars

### Pillar 1: Dramatic Introduction & Seam from Previous Chapter
* **Previous Chapter (I-01) Closing Paragraph:**
  > Beyond the prison bars and the clerks’ busy pens, Venice was still sending her galleys east. Turn the page to see the trading house that sent two brothers with a pouch of jewels across the Greater Sea.

* **Current I-02 Opening Paragraph:**
  > Venetian records, not the Book, sketch the house Niccolò and Maffeo Polo came from [1]. They were merchants of the kind commerce made substantial without ever making famous. There was a base at Constantinople (Istanbul), a trading house in Soldaia (Sudak) on the Crimean shore, and wills and property notices that survive because men of business stamped their names on paper. Tradition pushes the line back to one Andrea Polo of the parish of San Felice [2]. He was said to be father of three sons. Marco the Elder kept the Constantinople foothold and the Soldaia house; Niccolò, second of the brothers, was father of the traveller; and Maffeo was Niccolò’s partner in the ventures that follow [3]. They dealt in jewels, cloth, credit and the judgement of markets, and in the mid-thirteenth century those markets ran east along the Greater Sea.

### Pillar 2: Inserted Dramatic & "For Modern Audiences" Interludes
* **Detected Narrator Hooks / Interlude Cues (0):**
  - *None detected with standard interlude cues — good candidate for adding 2–3 vivid modern-audience staging interludes.*

### Pillar 3: Dramatic Outro & Seam to Next Chapter
* **Current I-02 Closing Paragraph:**
  > The Kaan still waited for learned men and for oil of the Sepulchre; Christendom still waited for a Pope. Between those two waits stood the House of Polo, ledgers thickened by Barca’s gifts and Bocara’s three years, its future leaning toward a second departure — one that would take the boy Marco into the Book’s own centre. But first the cardinals had to make a Pope, and at Viterbo they were proving slow; the brothers, tarrying on the lagoon, would not wait much longer.

* **Next Chapter (I-03) Opening Paragraph:**
  > The cardinals at Viterbo are still shut up with the question of who will be Pope. In Venice, Niccolò Polo has to decide how much longer a promise to an emperor can be left waiting on their deliberations. There is a new member of the party this time. Marco, the son he found at home when he came back, is about seventeen by the usual reckoning when the three leave in 1271 [1].

### Pillar 4: Main-Text Immersion Breaks (Move / Weave into Notes)
* **Current Sequential Notes Count:** 25
* **Inline `Ramusio` Provenance Stammers in Body Prose (1):**
  - Line 49: `What the Book does insist on is simpler and more human. The house had lost a wife and mother; the father had gained a fine lad of fifteen; and the two brothers abode at Venice a...`
* **19th/20th-Century Scholar Name-Drops in Body Prose (3):**
  - Line 13: `— A quick note on the dates: the manuscripts read 1250 for this crossing, a figure that cannot stand beside the return of 1269 and a son of fifteen. Yule corrected it to about 1...`
  - Line 35: `— No Mongol original of that letter survives. The request for learned men and for oil of the Sepulchre fits Chinghizide curiosity about skilled foreigners and Latin Holy Land pi...`
  - Line 47: `— Whether Niccolò saw that son as an infant before riding east, or left before the child was born and met him for the first time in 1269, the oldest French texts do not insist. ...`
* **Standalone Em-Dash (`—`) Asides in Body Prose (3):**
  - Line 13: `— A quick note on the dates: the manuscripts read 1250 for this crossing, a figure that cannot stand beside the return of 1269 and a son of fifteen. Yule corrected it to about 1...`
  - Line 35: `— No Mongol original of that letter survives. The request for learned men and for oil of the Sepulchre fits Chinghizide curiosity about skilled foreigners and Latin Holy Land pi...`
  - Line 47: `— Whether Niccolò saw that son as an infant before riding east, or left before the child was born and met him for the first time in 1269, the oldest French texts do not insist. ...`
* **Mid-Scene Academic Comparison Tables (0):**
  - *0 mid-scene tables (clean).*

---

## Guardrails for Revision
1. **Keep all verified facts, S-04 place glosses, and S-05 character glosses** from the chapter task file.
2. **Keep 1:1 sequential `[n]` claim anchors** paired with `## Notes` (renumbering cleanly if any note is split or merged, and updating `plans/registry/locators.md` if affected).
3. **Pass `tools/lint.py`** (1,800–3,200 narrative words; ≤15% Yule 7-gram overlap; 0 archaisms/book-1st-person outside quotes).
