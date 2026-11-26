# Agent prompt: GEN hero plates, Batch B, and the cutaway bases (PLT)

Paste everything below the line into the GPT agent. It continues `media/plates/AGENT-PROMPT.md`. That file's sections **Read first**, **Hard rules**, **Steps for each plate** and **Subagents** apply unchanged, so read them again before starting.

---

Batch A (9 plates) is done and in review. Now make **Batch B**, the remaining `ready` hero plates, and then the **cutaway bases** for the diagrams. Everything stays `draft`; the user accepts plates.

## What changed since Batch A

- **Character cards (CHR.T2, CHR.T8).** There are now 26 cards. The 7 new ones are `toghrul`, `oulatay`, `apusca`, `coja`, `fantina`, `bellela` and `moreta`. `python3 tools/characters.py cue <id> <year>` now also prints each figure's references:
  - **`[INPUT]` lines** may be attached: the accepted sheets and `edit OK` files.
  - **`[LOOK]` lines** are for looking only, never attached.

  Use these lines instead of choosing references by hand.
- **Lessons from Batch A:**
  1. **No lettering, even when the scene has writing in it (rule 4).** I-12's psalter came out with a legible Latin psalm and had to be redone with lettering-free bands. Any book, letter, banknote, paiza, seal, banner, tablet or inscription is drawn as **smooth grey-brown bands with a short red rubric bar**, or left blank. Never use real or fake letters, in any script. The caption carries the meaning.
  2. **Dress follows the card year by year.** On arrival, travellers wear travel dress. Check every Polo against `cue` for the scene's year, not against the last sheet you used.
  3. **Show the action the row names.** II-1 came out as a parade rather than a battle. If the row names an action, it must be visible.
  4. **Keep the counts modest.** Where the row says "dozens, not 2,000" or "a handful", draw that.

## Batch B: hero plates

Work in this order. The first group uses traditions already proven; the second group are first-of-tradition mini-pilots.

**Group 1: proven traditions (Yuan court and landscape, *jiehua*, Ilkhanid, Song–Yuan, Gothic)**

| Plate | Scene | Watch for (from the plan row) |
|---|---|---|
| II-2 | Elephants carry trees up the Green Mount | Qionghua island and Taiye lake; green-tiled hall; **no Qing White Dagoba** |
| II-5 | Printing the Kaan's paper money | Mulberry-bark sheets, a vermilion seal, clerks. **The notes, the seal and the plates carry no characters**: use plain panels and borders only. Check the printing-block material in the chapter task |
| II-6 | Caravan on the Pulisanghin bridge | Jin bridge; check the arch and lion details against the chapter task before drawing them |
| II-9 | Two dogs hold a tiger at bay | A **tiger**, though the Book says "lion" |
| II-10 | Song envoys surrender the seal, 1276 | Lin'an outskirts; Bayan (`cue bayan 1276`); **no Polos** (`ages`); the seal is blank; no "Hundred Eyes" |
| II-11 | Counterweight trebuchet at Xiangyang | Hinged box counterweight; Song walls across the Han; **no Venetians**; C46 is the engine frame only (look only) |
| II-12 | Trackers haul a junk up the Kiang | Bamboo hawsers; Golden Island monastery |
| II-14 | Zayton harbour: junks unloading pepper | The Quanzhou ship type (nailed hull, bulkheads); Kaiyuan stone pagodas; Arab and Tamil merchants |
| III-9 | Golden tablets; Cocachin and the fleet | Make the Yuan court hero only, not the Ilkhanid part. Cublay about 75; Cocachin unmarried (braids, no *boqta*); the Polos and the three envoys (`cue` for each, 1291); **13 junks**; the paiza tablets are blank gold |
| I-10 | Crossing the Pamier | Persianate (JT); *Ovis poli*; snow plateau; **no horn cairns** |
| I-9 | The balas-ruby mines under royal seal | Ilkhanid (JT); Badakhshan highland dress, oil lamps, officers sealing stones; the seals are blank |
| I-5 | Hulagu shuts the Caliph in the treasure tower | Livre des merveilles marvel lens. The LdM folios are **look only**; the Omont 1907 facsimile is edit OK. Abbasid black robes; Mongol lamellar armour; C6 |

**Group 2: first of their tradition (mini-pilots)**

The rule: 2 rounds at most. If both fail the hard checklist items, stop that plate and report. Do not switch tradition yourself.

| Plate | Scene | Tradition | Watch for |
|---|---|---|---|
| I-4 | The quay at Layas | Cilician Armenian illumination | Sea castle (see the Ayas phases in the 2026-11-16 intake); lateen ships; bales; Italian and Armenian merchants (C28–C33 dress) |
| I-8 | The Dry Tree alone on the plain | LdM marvel lens | One solitary tree and a passing caravan; the species is disputed, so keep it generic |
| I-11 | Spirit voices in the Lop desert | Dunhuang Mogao murals | Night dunes; a lone rider; a faint phantom caravan; no Buddhist deities as decoration (rule 6) |
| II-7 | Exploding bamboo in the night camp | Dali kingdom scroll | Hobbled, hooded horses; Kham forest |
| II-8 | Battle of Vochan | Pagan temple murals | Howdah castles breaking into the trees; **dozens** of elephants, not 2,000 |
| III-2 | Junks lift their rudders in the shoal strait | Javanese temple relief | Raisable axial rudders; mangrove coast; Malay perahu |
| III-3 | Five months stranded at Samara | Javanese / Sumatran relief | A **modest** camp; toddy-tappers; junks at anchor; no 2,000 men or ditches (those are later redactions) |
| III-4 | Pilgrims on Adam's Peak chains | Polonnaruwa murals | Buddhist and Muslim pilgrims together; don't resolve which tradition is right |
| III-6 | Corsair cordon off Malabar | Western Indian (Jain) palm-leaf | **4:1 strip**: generate wide, crop to 4:1, then resize to 2700×675; smoke-signal relay; families aboard; C42 dress |
| III-7 | The rukh carrying off an elephant | Persian *'aja'ib* (Qazwini) | Elephant in the bird's talons, with sea and coast below; the NLM and Walters folios are edit OK; avoid the 1911 European engraving look |
| III-8 | The wind-catchers of Hormos | Baghdad school (al-Wasiti) | Old mainland Hormuz; *bād-gīr* towers as a type; C7 ship |

For each plate, read its full row in `illustration-plan.md`, its chapter task's period-source handoff, and `PLT-plates.md` § R-3 handoff. Run `python3 tools/characters.py ages` to confirm who may appear.

## The cutaway bases: PLT.C12, C13, C14, C16

These are not scene plates. Each is a **label-free base drawing** that `DIA` will label with typeset TikZ labels, so leave room for them.

- **Style:** a clear technical cutaway in line and light wash on plain pale paper. Isolate the object, use even light, and keep wide empty margins on all four sides for the labels. No period-painting pastiche, no figures except where the row needs them, no lettering, numbers or leader lines. DIA adds the labels and lines.
- **Format:** 4:3 landscape, at least 1350×1013. Save as `media/plates/C<nn>-<slug>.png` with the usual sidecar. In the sidecar, set `use: DIA base (labels added in TikZ)`.
- **Sources:**
  - Each sidecar's `unsourced` field must be honest.
  - Every feature drawn from Polo's text alone is listed as "after Polo's description", not as archaeology.

| Base | Object | Draw | Sources and limits |
|---|---|---|---|
| C12 | Seagoing junk | A lengthwise cutaway showing **13 compartments** divided by 12 bulkheads, small limber holes at the bulkhead feet, a nailed plank hull, an axial rudder in its stock, batten sails on three masts, and cargo jars in the holds | F-14 (the Quanzhou wreck: 12 bulkheads, 13 compartments, about 28 m long by 10 m wide, nailed, with limber holes); `registry/visual-references.md`. Draw no "watertight" sealing, because the limber holes contradict it |
| C13 | Sewn-plank ship of Hormos | A small single-masted hull with planks stitched edge to edge with cord, no iron nails, one steering oar or rudder, and the open hold covered with hides, with horses standing on the cover | **Polo's description only.** No sewn hull from 1250–1300 has been found or viewed (gap ledger), and Vosmer 2019 is unread. Mark every feature "after Polo's description" |
| C14 | Traction vs counterweight trebuchet | Two machines side by side, with no crews and no siege. **Left:** a traction trebuchet, a beam pulled by a team's ropes. **Right:** a counterweight trebuchet with a **hinged box counterweight**, beam, sling and trestle frame | C46 (Annales Ianuenses, Savona 1227) gives the frame type only and is **look only**; text accounts of Xiangyang 1273. Draw nothing claimed as the exact Xiangyang engine |
| C16 | Cane palace roof | A section of the Chandu cane palace roof: whole canes split lengthwise and laid like tiles, alternately cupped up and down, on gilded columns, with the roof tied down by silk cords | **Polo's description only**; no period image. Mark it so |

**Skip C15 (qanat).** DIA.C15 already allows a pure TikZ drawing. A generated cross-section would invent geometry that a TikZ drawing gets exactly right. Don't make a base for it.

## Report back

Give one line per plate and base:
- the file, or "failed" or "stopped (mini-pilot)";
- the rounds used;
- any failed or borderline checklist items;
- the details left unsourced.

Then list:
- the first-of-tradition traditions that passed, which the user may want written into the style guide's per-tradition negatives;
- any plate where you were tempted to draw lettering.
