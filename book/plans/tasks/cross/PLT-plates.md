# PLT — Drawings and plates

**Status:** 23 of 35 GEN hero slots placed and proofed, including all three S-10 pilots · **Plan docs:** `illustration-plan.md`, `illustration-style-guide.md`

The [placement report](../../status/visual-placement-2026-11-23.md) lists the printed figures and the remaining draft decisions. Generator routes in the table are the original production specifications. The sidecars identify the actual route.

## Scope
Event illustrations: 35 generated (GEN) hero plates, 6 public-domain (PD) heroes, about 25 optional secondaries, plus retirement of six legacy illustrations. Cutaway bases for diagrams C12–C16 are produced here and labelled in `DIA`.

## Backlog
- Hero list per chapter: `illustration-plan.md` § Hero plates (also mirrored in each chapter backlog's Media hooks).
- PD slots: I-2 (LdM Polos at court), II-front (Kublai portrait), II-4 (Liu Guandao), III-1 (*Mōko Shūrai*, boarding scene), III-11 (Columbus postils / 1477 woodcut), III-12 (Catalan Atlas caravan); plus the II-5 Zhiyuan-note pairing. III-7 (Qazwini rukh) moved to GEN by S-11. Sources and captions: `registry/pd-sources.md`; masters: `media/public-domain/`.
- Retired legacy illustrations (period errors per critique):
  - `drawing-venetian-galley` (17th-c. Salute domes, Viking-like hull);
  - `drawing-chandu-palace` (Renaissance villa);
  - `drawing-genoa-dictation` (monk's habit, chains);
  - `drawing-manzi-junk` (Western galleried stern, portholes);
  - `drawing-kinsay-west-lake`, `drawing-indian-ocean-schematic` (mislabelled as maps).
- **Gap-source ledger (2026-11-13):** new period sources for GEN prompts and two print leads:
  - **I-1 inset:** Cocharelli f. 8r, counting house. PD outside the UK, but only 1200 px via IIIF, so order a master from the BL.
  - **Annales Ianuenses** council and Savona siege: Gallica, **fee** for print.
  - **Cues and avoid lines:** `registry/visual-references.md` § Gap-source ledger.
  - **Reference images and use rights:** `media/references/README.md` § Added 2026-11-13.
- **2026-11-17 review:** For III-3 and III-9, follow the [text and media handoff](../../status/critique-text-media-handoff-2026-11-17.md): the Samara camp is not Ramusio-only, no direct period Samara camp image has been checked, and the ship count, clothing and tablet references need their stated qualifications.
- Each plate: sidecar `.yaml` (prompt, negative, model, job id or seed, date, tradition, caption, review) → an `ATTRIBUTIONS.md` row.

## Gated by spikes
S-10 ✓ (generator and pilot, closed 2026-11-10: `media/plates/`, `plans/image-generation-guide.md`) · S-11 ✓ (PD licences: `registry/pd-sources.md`) · S-05 ✓ (character cards: `registry/character-cards.yaml`; each plate with a recurring person takes its `[PERIOD]`/`[AVOID]` lines from `tools/characters.py cue`, and its scene row must pass `tools/characters.py ages`) · S-08 (pixel sizes from trim)

## Tasks
**Every GEN task** (S-10):
1. Before prompt writing, check the scene's period-source handoff in its chapter task and the current S-23 gap ledger. **Ready** in the table means the production task can be started, not that every depicted detail has been sourced. Research, omit, or explicitly qualify details for which no suitable source has been checked. C9–C22 are rejected cue IDs and must not be used. Then write `media/plates/prompts/<id>.txt` from the scene row (`illustration-plan.md`) and the template, with the tradition's `NEGATIVE:` line, plus `tools/characters.py cue` lines for recurring figures, and the applicable checked cue lines (`illustration-plan.md` § S-22 period cues; a card line wins where they differ). No modern title goes into the prompt; image inputs only from `edit OK` reference files or accepted sheets, listed in the sidecar (style guide rules 8–12, rule 9 as amended 2026-11-18).
2. Generate by the route in the table (`plans/image-generation-guide.md`):
   - **Akool:** `python3 tools/plate_gen.py … --n 4`.
   - **Gemini chat:** copy the shape of `prompts/I-7-chat.txt`, with one corrective follow-up turn.
3. Review with `illustration-style-guide.md` § Review checklist.
4. Post-process to print size, then file the master, sidecar and `ATTRIBUTIONS.md` row. Keep the rejects in `media/plates/drafts/<id>/`.

**First of its tradition** (marked in the table) means that tradition is untested. Its first plate is a mini-pilot:
- If 2 Akool rounds (8 images) fail, switch that tradition to Gemini chat.
- If Gemini fails too, fall back to the LdM marvel lens.
- Either way, write the result into the style guide's per-tradition negatives.

**Done when:** the plate passes every hard line of the checklist, and the volume build places it with no size warning.

**Budget** (S-10): about 32 Akool credits per plate, i.e. 2 rounds of 4; Gemini chat costs no credits.

| Task | Hero scene | Tradition | Fmt | Route | Status |
|---|---|---|---|---|---|
| `PLT.I-1` | Marco dictating to Rustichello | Italian Gothic illumination | P | Akool | placed and proofed |
| `PLT.I-3` | "Sire, 'tis my son and your liegeman" | YC | L | Akool | placed and proofed |
| `PLT.I-4` | The quay at Layas | Cilician Armenian illumination | P | Akool, first of its tradition | placed and proofed |
| `PLT.I-5` | Hulagu shuts the Caliph in the treasure tower | LdM marvel lens | P | Akool, first of its tradition | draft queued |
| `PLT.I-6` | Marco at the Magi tombs of Saba | Ilkhanid (JT) | L | Gemini chat | placed and proofed |
| `PLT.I-7` | Marco escapes the Caraunas | Ilkhanid (JT) | L | — | placed and proofed |
| `PLT.I-8` | The Dry Tree alone on the plain | LdM marvel lens | P | Akool, first of its tradition | placed and proofed |
| `PLT.I-9` | The balas-ruby mines under royal seal | Ilkhanid (JT) | L | Gemini chat | draft queued |
| `PLT.I-10` | Crossing the Pamier | Persianate (JT) | H | Gemini chat | placed and proofed |
| `PLT.I-11` | Spirit voices in the Lop desert | Dunhuang Mogao murals | L | Akool, first of its tradition | placed and proofed |
| `PLT.I-12` | Cane divination before Chinggis's battle | Ilkhanid (JT) | L | Gemini chat | draft queued |
| `PLT.I-13` | Mare's-milk libation leaving Chandu | YC | H | Akool | placed and proofed |
| `PLT.II-1` | Kublai on the elephant tower, Nayan battle | YC (Liu Guandao manner) | H | Akool | draft queued |
| `PLT.II-2` | Elephants carry trees up the Green Mount | *jiehua* | H | Akool, first of its tradition | placed and proofed |
| `PLT.II-3` | The White Feast procession | YC | H | Akool | placed and proofed |
| `PLT.II-5` | Printing the Kaan's paper money | Yuan woodblock (*pinghua*) | L | Akool, first of its tradition; check block material for the scene | draft queued |
| `PLT.II-6` | Caravan on the Pulisanghin bridge | Yuan landscape / *jiehua* | H | Akool | draft queued |
| `PLT.II-7` | Exploding bamboo in the night camp | Dali kingdom scroll | L | Akool, first of its tradition | placed and proofed |
| `PLT.II-8` | Battle of Vochan | Pagan temple murals | L | Akool, first of its tradition | draft queued |
| `PLT.II-9` | Two dogs hold a tiger at bay | Dali kingdom scroll | L | Akool, first of its tradition | placed and proofed |
| `PLT.II-10` | Song envoys surrender the seal, 1276 | Southern Song academy | P | Akool | placed and proofed |
| `PLT.II-11` | Counterweight trebuchet at Xiangyang | Ilkhanid (JT siege) | L | Gemini chat | draft queued |
| `PLT.II-12` | Trackers haul a junk up the Kiang | Yuan landscape | H | Akool | placed and proofed |
| `PLT.II-13` | Pleasure barges on the West Lake | Song–Yuan city-genre scroll | H | — | placed and proofed |
| `PLT.II-14` | Zayton harbour: junks unloading pepper | Song–Yuan city-genre scroll | H | Akool | placed and proofed |
| `PLT.II-15` | Aijaruc throws the prince | Ilkhanid (JT) | L | Gemini chat | placed and proofed |
| `PLT.III-2` | Junks lift their rudders in the shoal strait | Javanese temple relief | L | Akool, first of its tradition | draft queued |
| `PLT.III-3` | Five months stranded at Samara | Javanese / Sumatran relief | L | Akool, first of its tradition | draft queued |
| `PLT.III-4` | Pilgrims on Adam's Peak chains | Polonnaruwa murals | P | Akool, first of its tradition | placed and proofed |
| `PLT.III-5` | Pearl divers and the shark-charmer | Chola temple mural | L | — | placed and proofed |
| `PLT.III-6` | Corsair cordon off Malabar | Western Indian (Jain) palm-leaf | 4:1 | Akool, first of its tradition | draft queued |
| `PLT.III-7` | The rukh carrying off an elephant | Persian *'aja'ib* (Qazwini) | P | Gemini chat, first of its tradition | placed and proofed |
| `PLT.III-8` | The wind-catchers of Hormos | Baghdad school (al-Wasiti) | L | Akool, first of its tradition | draft queued |
| `PLT.III-9` | Golden tablets; Cocachin and the fleet | YC (+ Ilkhan court: JT) | H | Akool (YC) + Gemini (JT) | placed and proofed |
| `PLT.III-10` | Jewels ripped from the Tartar coats | Venetian Gothic | P | Akool | placed and proofed |

**No modern reference found (S-23, 2026-11-13):** I-7, I-8, I-9, II-5, II-6, II-7, II-9, III-3, III-4, III-5, III-6, III-7, III-8. These rest on period art and scholarship alone: expect more rounds, as for "first of its tradition". III-5 is already done; review it if a source turns up.

**Also from GEN:**
- `PLT.S*` for secondaries, picked after the heroes.
- `PLT.C12`–`PLT.C16`, the cutaway base plates for `DIA`. They take the Akool route; C15 may be pure TikZ instead.
- `PLT.LEGACY` **done 2026-11-21.** All six retired illustrations are archived and identified as generated in the [media credits](../../../media/ATTRIBUTIONS.md). See [MED.T2](MED-existing-media.md#tasks) for verification.

_PD plates (from S-11) are below._

**Every PD task:** crop the master in `media/public-domain/` to the slot's format and print target (`illustration-style-guide.md` § Resolution); place it with the build's figure line, `![Caption. *(Credit.)*](../media/public-domain/<file>)`, taking caption and credit from `registry/pd-sources.md` § Captions; add an `ATTRIBUTIONS.md` row. **Done when:** the volume build places the figure without a size warning, and the credit matches the holder's required wording.

### PLT.I-02 — PD: the Polos before Kublai (LdM fol. 2v)
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** place `I-02-alt_omont1907-pl3-fol2v-mono.jpg` as a half-width landscape figure in `vol-1/ch-02-house-of-polo.md`, with the 1907-facsimile credit from `pd-sources.md`. It is 1177 px wide (262 dpi at full width). The build sets every figure at full width (`registry/markdown-conventions.md`), and `tools/build/book.lua` warns under 1350 px whatever width is asked. So: add Pandoc's `{width=60%}` after the image (about 435 dpi), and make `book.lua` scale its 1350 px check by that width, or record the one expected warning here. Add the attribute form to the conventions table either way. If the BL restores Royal 19 D I, f. 59v is a colour option to recheck.

### PLT.II-front — PD: Kublai, Yuan portrait album
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** P frontispiece in `vol-2/front-01-yuan-china-context.md` (or the volume's front page, per S-08). Credit in NPM's CC BY 4.0 form.

### PLT.II-04 — PD: Liu Guandao, *Khubilai Khan Hunting*
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** first replace the interim master with NPM's 6 MP open-data file (digitalarchive.npm.gov.tw; confirm the inventory number there). P, not H: it is a hanging scroll. Place in `vol-2/ch-04-hunt-traffic.md`.

### PLT.II-05P — PD pairing: Zhiyuan note
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** half-page inset beside the II-5 GEN hero in `vol-2/ch-05-ahmad-paper-coal.md`; crop to the note, or keep the plate if the layout allows. Photographer credit, CC BY-SA 3.0. Do not call the sheet an original note; do not date the individual plate solely from the 1287 issue. The S-17 CUHK catalog describes different bronze blocks (200/500 *wen*), not this 2-*guan* plate.

### PLT.III-01 — PD: Suenaga boards a Yuan ship, 1281
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** handscroll spread (2700 × 900) or 2:1 crop from the Kyushu master, in `vol-3/ch-01-ships-chipangu.md`. Optional upgrade: the original via ColBase, if listed there.

### PLT.III-11 — PD: Columbus's copy (postils)
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** crop one page of the Colombina photograph to P, in `vol-3/ch-11-afterlives.md`; the Dibdin woodcut is the alternative. Use the proposed [S-20 caption](../../research/results/S-20-closure.md): notes by Columbus and others, dates uncertain; do not imply pre-1492 use. Confirm crop and photographer credit at production.

### PLT.III-12 — PD: the Catalan Atlas caravan
- **Status:** placed and proofed, 2026-11-23
- **Original brief:** H crop of `III-12-alt_loc1959-facsimile-caravan.jpg` (keep the inscription), in `vol-3/ch-12-reliability-essay.md`; credit it as the 1959 facsimile.

**Priority visual intake, 2026-11-16:** Before I-4 / II-14 / III-3, consult the [updated visual register](../../registry/visual-references.md#2026-11-16-priority-visual-source-intake) for Ayas fortress phases, the excavated Deji Gate and Kota Cina sample limits. For II-4's hunting scroll the NPM now states CC0 / CC BY 4.0 terms for specified files; confirm the exact downloaded file, credit and print resolution before placement. No plate or prompt was changed by the intake.

## R-3 period-source handoff (2026-11-17)

See `registry/visual-references.md` § 2026-11-17 R-3 period-source pass. In short:
- New records for II-5 (CUHK 1988.0028 blocks), II-10 (Zhao Boyun tomb dress) and I-7 (Great Mongol Shahnama dress).
- Two leads rejected: Mogao 3 and 465 for I-11, and Freer F1954.21 for II-12.
- I-9, I-10, II-7 and II-8 still have no period source: prompt them as reconstruction, and say so in the caption.
- Before using BnF Arabe 5847 for I-7, I-11 or III-6, confirm the folios on Gallica. **Done 2026-11-17** ([FINAL-ACCESS intake](../../research/results/FINAL-ACCESS-intake.md)): f. 119v ship confirmed; ff. 10r, 19r, 101r are not caravans (seated men by a camel; a mounted procession; a camel herd); dated 634 AH / 1236–37.
- III-4: the chains are in Polo's own text. Do not repeat UNESCO's "Polo climbed it in 1286".

