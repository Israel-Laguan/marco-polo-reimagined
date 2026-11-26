# Agent prompt: corrections to four character sheets (CHR.T9)

Paste everything below the line into the GPT agent. It continues the work in `AGENT-PROMPT.md`, and the hard rules there still apply.

---

Four of the draft character sheets failed review. Re-make each one with the corrected prompt below, using the same procedure and sidecar format as `media/characters/AGENT-PROMPT.md`.

**For each of the four sheets:**
1. Rename the current image to `<sheet-id>-sheet-v1.png`. Do not delete it.
2. Replace `media/characters/prompts/<sheet-id>.txt` with the corrected prompt below. Keep the same image inputs as before unless the section says otherwise.
3. Generate the image. You get up to 3 tries.
4. Save it as `<sheet-id>-sheet.png` and update that sidecar:
   - `params.tries`: the total so far.
   - `date`: today.
   - `review`: rewritten for the new image.
   - `notes`: one line saying what v1 got wrong.
   - `status`: stays `draft`.
5. Update the date in that sheet's row of `media/ATTRIBUTIONS.md`.

**Also, with no new images:** the sidecars for `toghrul-1203`, `arghuns-envoys-1291` and `polo-daughters-1324` say `cards: []`. Add a `people:` list to each one, using the ids from `plans/registry/characters.yaml`:
- `toghrul-1203`: `[toghrul]`
- `arghuns-envoys-1291`: `[oulatay, apusca, coja]`
- `polo-daughters-1324`: `[fantina, bellela, moreta]`

Add the line `cards: none yet (CHR.T2), dress is a working convention` beside it.

**Report back** one line per sheet: the file, the number of tries, and whether the fault is gone.

## 1. `donata-1305`: the sheet reads as the Virgin Mary

**What went wrong:** a blue mantle over a red gown, with a white veil and a hand laid on the breast, is the standard way the Virgin is painted. Style-guide rule 6 forbids sacred iconography in a scene that isn't religious. Change the palette and the pose; keep the dress.

```
Painted in the manner of Venetian Gothic painting of the early fourteenth century (secular donor and townswoman figures, and the San Marco Sant'Alipio lunette): thin dark outlines, flat tempera colour, linear hems, a measured upright pose; plain undecorated pale parchment ground, no landscape.

A character reference sheet of one woman, Donata Badoer, Marco Polo's wife, a Venetian patrician housewife of about 25 in 1305. One full-length standing figure in three-quarter view. She is a lay townswoman, not a saint or a devotional figure.

Face and body: a composed young married woman with an ordinary, individual face; upright and practical in bearing.

Dress: a long, plain, close-fitting gown in deep green, with a sleeveless overgown or mantle in warm russet-brown worn open at the front; a white linen married woman's veil over a close white wimple framing the face and covering the neck. Solid colours, good cloth, no gold.

Pose: her hands are low and busy, not on her breast. One holds a small ring of keys on a cord at the belt, the other lifts the hem of her overgown slightly as if about to walk. Her head is level and her gaze is straight ahead, not lowered.

Format: 4:3 landscape, pale ivory parchment, light even ageing, no damage; the whole figure at about 82% of the canvas height, with clear margins.

Do not include: any text, calligraphy, inscriptions, writing, seals or red stamps, signatures; a blue mantle; a blue-over-red colour scheme; a star on the mantle; a hand on the breast; hands joined in prayer; a lowered or downcast gaze; a halo or any gold behind the head; a crown, tiara or loose hair; a child; a book of hours; lilies; a gold ground; a widow's black veil; Renaissance sleeves; photographic realism; 3D render.
```

## 2. `chabi-1275`: the riding figure looks like a child

**What went wrong:** the mounted Chabi is drawn small, with a child's face and proportions, next to a full-size court figure. Both views must show the same middle-aged woman at the same scale. Keep the court view as it was.

Replace only the "Hunt, on horseback" paragraph and the subject paragraph of the current prompt. Keep the rest:

```
A character reference sheet of one woman, Chabi, Kublai's empress, a mature woman in her fifties in 1275 (her birth year, 1216 or 1227, is unsettled). Show her twice on the same unbroken silk ground: standing full-length at court, and mounted on a compact Mongol horse. Both figures are drawn at the same scale: her head in the mounted view is as large as in the standing view, and her seated body is an adult woman's, broad-shouldered and full-figured, filling the saddle. Both are unmistakably the same middle-aged woman, with the same round full face, narrow dark eyes, fine brows and small mouth, and with the softness of age in the cheeks and jaw.

Hunt, on horseback: no tall headdress; a plain white robe with a crossed collar, a small dark cap with one red band, black hair in compact looped braids at the ears. She sits upright and calm, holding the reins in both hands. The horse is small and stocky, so she looks large on it, as the riders in Liu Guandao's hunt do.
```

Add these to the "Do not include" line: `child, girl, youthful face, small or doll-like rider, oversized horse`.

## 3. `peter-the-tartar-1324`: he doesn't read as a Tatar

**What went wrong:** the v1 prompt banned "Mongol or Tatar costume" and "exotic costume", and asked for "Venetian paint conventions". As a result the face came out as a generic Venetian. The card says a Tatar man in Venetian dress: the dress stays Venetian, but the face must be clearly Central Asian.

```
Painted in the manner of Venetian Gothic painting of the early fourteenth century (secular figures and the San Marco Sant'Alipio lunette): thin dark outlines, flat tempera colour, linear hems, a measured pose; plain undecorated pale ivory parchment ground, no landscape.

A character reference sheet of one man, Peter the Tartar, a man from the Mongol steppe living in Venice as a household servant, about 45 in 1324. One full-length standing figure in three-quarter view, attentive and dignified.

Face and body: clearly a Mongol or Tatar man from Central Asia: a broad flat face with high, wide cheekbones, narrow dark eyes with a single eyelid, a low nose bridge, a light olive-brown complexion, a sparse dark moustache and a few chin hairs, and straight coarse black hair cut short in the Venetian manner and greying at the temples. A real individual, not a caricature.

Dress: entirely Venetian: a knee-length servant's tunic of plain brown or grey wool with a simple belt, dark hose, low leather shoes, bareheaded or a plain cloth coif. His foreignness is in his face only, not in his clothes.

Format: 4:3 landscape, pale ivory parchment, light even ageing, no damage; the whole figure at about 83% of the canvas height, with clear margins.

Do not include: any text, calligraphy, inscriptions, writing, seals or red stamps, signatures; a European face; a red cap; a fur hat; Mongol robes; braids; a bow or sword; any exotic or orientalist costume; caricatured features; jewellery or a badge; other people; photographic realism; 3D render.
```

## 4. `nayan-1287`: the banner looks like a crusader's

**What went wrong:** a red Latin cross on a white rectangular flag reads as a crusader or Templar banner. The Book gives Nayan a cross on his standard; a Christian of the Church of the East would carry their own form of the cross. Change only the standard; keep the figure and armour.

Replace the standard sentences of the current prompt with:

```
He stands with his left hand holding a single tall standard-pole beside him. From it hangs a long, narrow Mongol cloth pennon of deep blue, with a black horsehair tuft at the top of the pole. On the pennon is one small cross in gold of the Church of the East type: four equal arms that widen toward their ends, each end split into two small rounded points, inside a plain ring. It is the only emblem on the sheet.
```

Add these to the "Do not include" line: `red cross on white, crusader banner, Templar cross, Latin cross with a long lower arm, square flag`.
