# Agent prompt: I-12, replace the Latin psalter text with lettering-free lines

Paste everything below the line into the GPT agent. The hard rules of `media/plates/AGENT-PROMPT.md` still apply.

---

Plate I-12 (`media/plates/I-12-cane-divination.png`) fails style-guide rule 4. The open psalter carries legible Latin (*DOMINVS REGIT ME / ET NIHIL MIHI DEERIT*), and the review checklist's item 1 is a hard fail for any script. The Latin is also historically wrong. The clerics belong to the Church of the East, whose psalter was Syriac. Latin reached the Mongols only with the Franciscans, from 1294. So the book must show **no letters at all**. The meaning goes in the caption instead.

## 1. Keep the current version

Copy the current master to `media/plates/drafts/I-12/before-lines.png`, and its sidecar to `drafts/I-12/before-lines.yaml`.

## 2. Edit the book only

Edit the current master as an image edit. Do not regenerate the scene. Write the edit text to `media/plates/prompts/I-12-lines-correction.txt`:

```
Edit only the open book held by the central cleric in this Ilkhanid manuscript painting. Change nothing else: faces, hands, canes, figures, colours, border and paper stay exactly as they are.

Remove every letter from both pages. In their place, draw each page as a plain cream page carrying 7 or 8 evenly spaced horizontal lines of soft grey-brown wash, like the rhythm of text seen from a distance. Each line is a smooth, continuous band of even thickness with softly rounded ends. The bands have no strokes, no dots, no loops, no gaps that could be read as letters or words, and no marks above or below them. Add one short band in faded vermilion at the top of each page, as a rubric. Keep a plain margin around the bands. The binding and the cleric's fingers stay unchanged.

Do not include: letters of any alphabet (Latin, Syriac, Arabic, Persian, Chinese or Mongol), pseudo-script, squiggles, scribbles, calligraphy, numbers, initials, crosses or pictures on the pages, seals, stamps.
```

If the edit leaves anything that looks like a letter, or anything that looks like a squiggle imitating writing, try again, up to 3 tries. As a last resort, edit the pages to plain blank cream with a single vermilion rubric band.

## 3. Check

Zoom to 100% on both pages and on the whole plate. Nothing may read as a character in any script (checklist item 1). Also compare the rest of the plate with `before-lines.png`: it must be unchanged.

## 4. Save and update the sidecar

Save the result as the master `media/plates/I-12-cane-divination.png`; keep it lossless and the same size. Then update `I-12-cane-divination.yaml`:
- **`caption`:** change "Church of the East clerics read a psalm" to "Church of the East clerics read a psalm (in Syriac, their liturgical language)". Leave the rest of the caption as it is.
- **`review.script`:** replace it with: "Pass. The psalter pages show lettering-free ruled bands and a vermilion rubric. No letters in any script, and no pseudo-script."
- **Remove** the "user-requested exception" wording and the Latin Vulgate `source` / `historical_note` entries.
- **Add** this `historical_note`: "The Church of the East psalter was in Syriac (Turfan, Bulayïq fragments; Syriac psalter leaves transliterated into Old Uyghur). Latin reached the Mongols only with John of Montecorvino, from 1294, who translated the Psalter into the local language. A legible Latin text (v1, `drafts/I-12/before-lines.png`) was withdrawn for rule 4 and for period accuracy."
- **`post`:** add the edit step, after the existing steps.
- **`date`:** today. **`status`:** stays `draft`.

Leave the plate's row in `media/ATTRIBUTIONS.md` as it is, unless its date column needs today's date.

## Report back

Give the file, the number of tries, and a one-line result of the zoom check on both pages.
