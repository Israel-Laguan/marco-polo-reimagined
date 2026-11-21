# Agent prompt: character reference sheets (CHR.T9)

Paste everything below the line into the GPT agent. It assumes the agent can read and write this repo, run `python3`, and generate images.

---

You are making **character reference sheets** for *The Book of the Million*, an illustrated retelling of Marco Polo in three volumes. The repo root is the `book/` folder. A reference sheet is a working image that keeps one historical figure consistent from plate to plate. It is **never printed** and never presented as a real likeness.

## Read first (do not skip)

1. `plans/illustration-style-guide.md`: § Rules for every plate (rules 1–12, especially 4, 6, 7 and 9), § Prompt template and § Review checklist.
2. `plans/registry/character-cards.yaml`: one card per figure (`house`, `attributes`, `dress` by year, `traditions`, `avoid`).
3. `plans/tasks/cross/CHR-characters.md` § CHR.T9: the task you are doing.
4. The reference manifests: `media/references/README.md` (its **Use** column) and `media/reference/s22/README.md` (every file there is `edit OK`).
5. The first accepted sheet, `media/characters/kublai-1280-sheet.webp`, is the benchmark for quality and layout.

## Hard rules

- **Image inputs:** attach only files that their manifest marks `edit OK`, plus sheets already accepted in `media/characters/`. Never attach a `look only` file (for example the BnF scans of the *Livre des merveilles* or the Catalan Atlas). Even with images attached, the prompt still describes everything in words.
- **No modern works:** no film, game, manga or actor's name, and no modern artist's name, in any prompt.
- **No script anywhere:** no letters, calligraphy, seals, stamps or signatures. Put this in every prompt's "Do not include" line.
- **No Polo likeness exists.** Marco, Niccolò and Maffeo are house conventions taken from their cards' `house` lines.
- **Dress follows the card for the sheet's year**, and nothing else. Where a card line and a cue line differ, the card wins.
- **Do not edit** `character-cards.yaml`, the style guide, the chapters, or anything outside `media/characters/` and `media/ATTRIBUTIONS.md`. Do not commit.

## The sheets

`kublai-1280` is done: only write its sidecar (see step 5; the generator was the GPT image model in the chat agent, on 2026-11-18, with no reference images attached, and the prompt is in `media/characters/prompts/kublai-1280.txt`, which you must create from the text below).

| # | Sheet id | Card `id` | Year | Tradition (style-guide name) | What the sheet shows |
|---|---|---|---|---|---|
| 1 | `chabi-1275` | chabi | 1275 | Yuan court painting | court dress with boqta; riding dress, no boqta |
| 2 | `marco-1271` | marco | 1271 | Italian Gothic / Venetian | 17, beardless, setting out from Venice |
| 3 | `marco-1285` | marco | 1285 | Yuan court painting | about 31, in the Kaan's service, with the paiza |
| 4 | `marco-1298` | marco | 1298 | Italian Gothic / Genoese | about 44, a citizen of Genoa, then Venice |
| 5 | `niccolo-maffeo-1285` | niccolo, maffeo | 1285 | Yuan court painting | the two elder Polos together, clearly told apart |
| 6 | `cocachin-1291` | cocachin | 1291 | Yuan court painting | the bride before marriage: braids, no boqta |
| 7 | `bayan-1275` | bayan | 1275 | Yuan court painting | commander in armour |
| 8 | `nayan-1287` | nayan | 1287 | Yuan court painting | prince in armour |
| 9 | `chinghis-1206` | chinghis | 1206 | Yuan court painting | from the NPM portrait album |
| 10 | `hulagu-1258` | hulagu | 1258 | Ilkhanid (Jami' al-Tawarikh) | Ilkhan in armour |
| 11 | `ghazan-1295` | ghazan | 1295 | Ilkhanid (Jami' al-Tawarikh) | young prince, turban after his conversion |
| 12 | `mustasim-1258` | mustasim | 1258 | Ilkhanid (Jami' al-Tawarikh) | the last Abbasid caliph |
| 13 | `kaidu-1280` | kaidu | 1280 | Ilkhanid (Jami' al-Tawarikh) | Central Asian Mongol prince |
| 14 | `aijaruc-1280` | aijaruc | 1280 | Ilkhanid (Jami' al-Tawarikh) | Kaidu's daughter dressed for the wrestling bout |
| 15 | `rustichello-1298` | rustichello | 1298 | Italian Gothic | a writer at work in prison, lay or clerical status left open |
| 16 | `tedaldo-1270` | tedaldo | 1270 | Italian Gothic | archdeacon and legate at Acre |
| 17 | `donata-1305` | donata | 1305 | Italian Gothic / Venetian | Marco's wife |
| 18 | `peter-the-tartar-1324` | peter-the-tartar | 1324 | Italian Gothic / Venetian | a Tatar servant in Venetian dress |
| 19 | `cepoy-1307` | cepoy | 1307 | Italian Gothic | a French noble in Venice |

If a card's `dress` lines do not cover the year, stop that sheet and report it; do not make up dress.

## Steps for each sheet

1. **Cue.** For each card on the sheet, run `python3 tools/characters.py cue <card-id> <year>`. Its `[PERIOD]` lines give the face, age and dress; its `[AVOID]` line goes into "Do not include". Also read the card's `traditions` line for the chosen tradition.
2. **References.** From the two manifests, choose up to 3 `edit OK` files that help this figure (a portrait for the face, a period painting for dress or idiom). If there are none, attach nothing and say so in the sidecar.
3. **Prompt.** Write `media/characters/prompts/<sheet-id>.txt` in this shape, the same as the accepted Kublai sheet:
   - **Style:** "Painted in the manner of <tradition> (<a period work named in the style guide>): <3–5 idiom cues>, plain undecorated background, no landscape."
   - **Subject:** "A character reference sheet of one person, <who and age>, shown <once or twice: the dress lines chosen>. Clearly the same person in each view."
   - **Face and body**, from the card's `house` line.
   - **One paragraph per dress line**, copied from `cue`.
   - **Format:** 4:3 landscape, the tradition's ground (silk, paper or parchment), light even ageing, no damage.
   - **Do not include:** "any text, calligraphy, inscriptions, writing, seals or red stamps, signatures", the `[AVOID]` items, "photographic realism, 3D render".
4. **Generate and review.** Generate the image, then review it against the style-guide checklist items 1 (no script), 2 (period), 3 (figures match the card's attributes; count them) and 5 (idiom). You may re-roll or send one correction turn, up to 3 tries. If the sheet still fails, save the best attempt as `<sheet-id>-sheet-rejected.<ext>` and record why.
5. **Save.** Save the image as `media/characters/<sheet-id>-sheet.<ext>`, keeping the generator's own format; do not upscale. Then write the sidecar `media/characters/<sheet-id>-sheet.yaml`:

```yaml
sheet: <sheet-id>
cards: [<card-id>, ...]
year: <year>
status: draft            # the user accepts it; you never set "accepted"
use: reference only, never printed (CHR.T9)
tradition: <tradition>
likeness: <"house convention, no authentic likeness" for Polo figures and any card whose likeness is "none"; else the card's likeness source>
generator: <product and model name exactly as shown to you>
job_id: <id if any, else "none: chat output">
date: <YYYY-MM-DD>
params: {size: <WxH>, tries: <n>}
prompt: media/characters/prompts/<sheet-id>.txt
reference_images:        # [] if none
  - file: <path>
    use: edit OK
    licence: <as stated in its manifest>
    credit: <as stated in its manifest>
attribution: >-
  Generated image (<generator>, <date>) for The Book of the Million, a working reference
  sheet in the manner of <tradition>. Not a historical artifact.<" Reference images: <credits>." if any>
review:
  script: <pass/fail + where>
  period: <pass/fail + what was checked against which cue>
  figures: <card attributes present or missing>
  idiom: <reads as the tradition or not>
  notes: <anything the user should look at>
```

6. **Attribution.** Add one row per sheet to `media/ATTRIBUTIONS.md`, under a new section `## Character reference sheets (CHR.T9; not printed)` placed after "Generated plates". The table columns are `| Local file | Figure, year | Tradition | Generator, date | Reference images |`.

## Subagents

You may run one subagent per sheet in parallel. Each subagent writes only its own `prompts/<sheet-id>.txt`, its image and its sidecar. **Only you (the lead)** edit `media/ATTRIBUTIONS.md`, once at the end, so that parallel edits do not clash. Give each subagent this whole prompt and its row of the table. Run sheet 5 after sheets 3 and 4 are done, and attach `marco-1285-sheet` to it so the family resemblance holds.

## Report back

Give one line per sheet: the file, its status (draft or rejected), the number of tries, and anything that failed review. Also list the sheets you skipped and why. Do not mark anything accepted.

### Kublai prompt (for `prompts/kublai-1280.txt`)

```
Painted in the manner of Yuan dynasty court painting (Liu Guandao's "Khubilai Khan Hunting", 1280, and the Yuan imperial portrait album): ink outline with fine even brushwork, flat mineral colours on pale silk, plain undecorated background, no landscape, figures drawn in three-quarter view, calm and dignified.

A character reference sheet of one man, the Mongol Great Khan Kublai at about 65, shown twice on the same plain silk ground: standing at court, and mounted for the hunt. He must be clearly the same person in both.

Face and body: broad round face, fair skin with ruddy cheeks, dark eyes, a thin moustache and a small beard; heavy and stout in body, a large man but not a giant. No crown.

Standing, at court: a single-colour white Mongol robe with a crossed collar and a short-sleeved outer robe over a long-sleeved under-robe, fur trim at the cuffs; a small rounded pale hat with a narrow brim and a knob on top; his hair in looped braids behind each ear.

Mounted, hunting: a white fur coat flecked with black tufts, with a dark fur collar and cuffs, worn over a red robe patterned in gold; a red-topped cap; boots; a bow case and quiver hanging at the saddle; a white gerfalcon on his gloved fist. The horse is dark, small and stocky, with a round blue saddle-cloth and red tassels on its breast-strap.

Format: 4:3 landscape, pale silk ground, light even ageing, no damage.

Do not include: any text, calligraphy, inscriptions, writing, seals or red stamps, signatures, colophons; crowns; Qing dragon robes; yellow as an imperial colour; the queue hairstyle; Ming or Qing dress; armour; fur-and-leather "barbarian" costume; photographic realism; 3D render.
```
