# I-09: Balc, Badashan, Pashai, Keshimur: Rubies, Azure, and High Valleys

**Status:** Pending Theatrical Voice Review  
**Canonical Manuscript:** [`book/vol-1/ch-09-balc-badashan.md`](file:///home/anthony/code/marco-polo-reimagined/book/vol-1/ch-09-balc-badashan.md)  
**Proposed Sandbox Draft:** `book/proposed-voice/vol-1/ch-09-balc-badashan/proposed.md`  
**Chapter Task & Fact Sheet:** [`book/plans/tasks/chapters/vol-1/I-09-balc-badashan.md`](file:///home/anthony/code/marco-polo-reimagined/book/plans/tasks/chapters/vol-1/I-09-balc-badashan.md)  
**Voice Guide:** [`book/proposed-voice/PROPOSED-VOICE-GUIDE.md`](file:///home/anthony/code/marco-polo-reimagined/book/proposed-voice/PROPOSED-VOICE-GUIDE.md)  
**Big-Picture & Baton Plan:** [`book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md`](file:///home/anthony/code/marco-polo-reimagined/book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md)  

---

## Quick-Start Prompt for Separate Chat

Copy and paste this into a new chat:

```text
Let's calmly analyze and revise I-09 (Balc, Badashan, Pashai, Keshimur: Rubies, Azure, and High Valleys) to apply the theatrical single-narrator voice.
1. Read @[book/proposed-voice/PROPOSED-VOICE-GUIDE.md], @[book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md], and this chapter's diagnostic brief @[book/proposed-voice/vol-1/ch-09-balc-badashan/README.md].
2. Read the current chapter @[book/vol-1/ch-09-balc-badashan.md] and its fact/apparatus constraints in @[book/plans/tasks/chapters/vol-1/I-09-balc-badashan.md].
3. First, show me your analysis and specific proposal for:
   - Big-Picture Arc & Mode Cue: Narrative Arc: Climb from the ruined palaces of Balc and Taican's salt hills into the royal ruby monopoly, silver mines, and unshod mountain horses of Badashan.
   - Pillar 1: Dramatic Introduction (catching the Incoming Baton — "From I-08: Emerging from besieged mountain castles into the grass and melon fields of Sapurgan." — and exploding with theatrical scale/stakes)
   - Pillar 2: Inserted Dramatic & "For Modern Audiences" Interludes
   - Pillar 3: Dramatic Outro (landing the closing image and handing off the Outgoing Baton — "To I-10: Following the river up out of Badashan's high valleys toward the freezing roof of the world on the Pamier plateau.")
   - Pillar 4: Moving immersion-breaking inline scholar/Ramusio citations and academic em-dash asides into the Notes.
4. After we align on the proposal, write the revised chapter to book/proposed-voice/vol-1/ch-09-balc-badashan/proposed.md and run `python3 tools/lint.py -v proposed-voice/vol-1/ch-09-balc-badashan/proposed.md` from `book/`.
```

---

## Big-Picture Framing for I-09 (from `BIG-PICTURE-NARRATION-PLAN.md`)

* **Series Position:** Act II: The Overland Caravan Atlas — Khorasan to the Ruby Mountains of Badashan
* **Narrator Mode / Gear Cue:** Narrative Arc: Climb from the ruined palaces of Balc and Taican's salt hills into the royal ruby monopoly, silver mines, and unshod mountain horses of Badashan.
* **Incoming Baton (Catch in Opening Paragraph):** From I-08: Emerging from besieged mountain castles into the grass and melon fields of Sapurgan.
* **Outgoing Baton (Hand Off in Closing Paragraph):** To I-10: Following the river up out of Badashan's high valleys toward the freezing roof of the world on the Pamier plateau.

---

## Diagnostic Audit Against the 4 Pillars

### Pillar 1: Dramatic Introduction & Seam from Previous Chapter
* **Previous Chapter (I-08) Closing Paragraph:**
  > Inside a besieged castle, every crust is counted, and every day without relief shrinks the garrison’s hopes. Out beyond the hills on the road to Sapurgan (Shibarghan), an army can halt simply because the grass is thick and the orchards are full—and that is where we pick up the trail.

* **Current I-09 Opening Paragraph:**
  > Troops that have spent months starving a castle find a very different country on the road to Sapurgan (Shibarghan). Grass spreads thick for the horses, and orchards and fields keep the soldiers fed. Polo counts six days through towns and villages, yet breaks the stretch with fifty- or sixty-mile dry runs where every rider must carry his own water and the horses wait to drink [1]. Look at the road first through a quartermaster’s eyes: it pays to halt where the grazing is lush rather than drive gaunt beasts forward on empty bellies. Then look through a merchant’s: every water-skin lashed to a pack-saddle steals room from silk or spice, and a dry stretch forces you to trade payload for survival. Both pasture and thirst belong in the same march, though fitting all of it neatly into six days takes some squeezing.

### Pillar 2: Inserted Dramatic & "For Modern Audiences" Interludes
* **Detected Narrator Hooks / Interlude Cues (0):**
  - *None detected with standard interlude cues — good candidate for adding 2–3 vivid modern-audience staging interludes.*

### Pillar 3: Dramatic Outro & Seam to Next Chapter
* **Current I-09 Closing Paragraph:**
  > Keep the coral packed for the road toward India. The Book turns back to Badashan, where a mountain river offers the only road higher into the range—and from here, we follow the water upstream.

* **Next Chapter (I-10) Opening Paragraph:**
  > Follow the river up out of Badashan (Badakhshan). For twelve days the trail climbs between east and north-east, bending with the valley through lands ruled by a brother of the Badashan prince [1]. Villages and scattered farms still line the banks, so a caravan can buy bread and fodder along the way without unloading its spare packs. Farther up, provisions become something you weigh and pack before you dare set out. Every day’s climb narrows the valley floor and reminds the muleteers how soon the last inhabited hamlet will drop behind them.

### Pillar 4: Main-Text Immersion Breaks (Move / Weave into Notes)
* **Current Sequential Notes Count:** 30
* **Inline `Ramusio` Provenance Stammers in Body Prose (4):**
  - Line 23: `At Taican (Taloqan), a hungry traveller heads straight for the grain market, though the town’s real curiosity lies south in the hills. There the rock salt is so dense it takes a...`
  - Line 39: `Unshod horses gallop over these rocky tracks without splitting a hoof. Ramusio adds that they tear downhill at a pace no lowland mount can match [18], and tucks in a tale of a b...`
  - Line 41: `Climb for a full day in Ramusio’s version, and the gorge opens onto a high plateau of grass, trees, and cold springs. Trout dart in the brooks, and wild sheep graze in flocks of...`
  - Line 59: `Monasteries and hermits dot the hills, keeping to a spare diet and strict vows of abstinence [28]. In the Zelada Latin and Ramusio, devout locals who refuse to slaughter an anim...`
* **19th/20th-Century Scholar Name-Drops in Body Prose (1):**
  - Line 23: `At Taican (Taloqan), a hungry traveller heads straight for the grain market, though the town’s real curiosity lies south in the hills. There the rock salt is so dense it takes a...`
* **Standalone Em-Dash (`—`) Asides in Body Prose (1):**
  - Line 17: `— Between Sapurgan’s dried melons and Balc’s broken marble, the road already teaches you how quickly a landscape shifts: one stage feeds an army, the next leaves a ruined capita...`
* **Mid-Scene Academic Comparison Tables (1):**
  - Around line 46: `| Detail | Base account in Yule–Cordier | Ramusio’s addition | Evidence and limit |`

---

## Guardrails for Revision
1. **Keep all verified facts, S-04 place glosses, and S-05 character glosses** from the chapter task file.
2. **Keep 1:1 sequential `[n]` claim anchors** paired with `## Notes` (renumbering cleanly if any note is split or merged, and updating `plans/registry/locators.md` if affected).
3. **Pass `tools/lint.py`** (1,800–3,200 narrative words; ≤15% Yule 7-gram overlap; 0 archaisms/book-1st-person outside quotes).
