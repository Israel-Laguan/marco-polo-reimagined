# Agent prompt: Batch B corrections (III-9, I-4, III-8)

Paste everything below the line into the GPT agent. The hard rules of `media/plates/AGENT-PROMPT.md` still apply.

---

Three Batch B plates failed review. Each fault is in one part of the image, so **edit the current master; do not regenerate the scene**. For each plate:

1. Copy the current master and sidecar to `media/plates/drafts/<plate>/before-fix.png` and `before-fix.yaml`.
2. Write the edit text below to `media/plates/prompts/<plate>-fix.txt` and run it as an image edit. You get up to 3 tries. If the edit damages faces, hands or the parts it should leave alone, try again from `before-fix.png`, not from the damaged result.
3. Zoom to 100% on the edited area and on every face. Then compare the rest of the plate with `before-fix.png`: it must be unchanged.
4. Save the result over the master, at the same size and lossless. In the sidecar, update `review` for the fixed items, add the edit step to `post`, add one `notes` line on what was wrong, and set `date` to today. `status` stays `draft`.

## 1. III-9: the Polos' hats read as pith helmets, and too many hold tablets

**What went wrong:** the C1 hat (small, rounded, narrow brim, a knob on top) came out as hard white domes, which read as colonial pith helmets. Also all six men hold gold tablets. The Book has the Kaan give the tablets to the Polos. The envoys get none.

```
Edit only the hats of the three Latin men in the centre (white, red and blue robes) and the gold tablets held by the six standing men. Change nothing else: faces, beards, robes, the Kaan, the young woman, the guards, the architecture, the fleet and the silk ground stay exactly as they are.

Hats: replace each white dome with a small, soft, low felt cap with a rounded crown that sits close on the head, a narrow turned-up brim, and a small knob on top. The cap is a muted cloth colour that goes with each man's robe (dark red-brown, dark blue, and dull ochre), not white, not glossy, not rigid.

Tablets: the three Latin men each wear one small, plain, blank gold tablet hanging on a cord at the chest, and their hands are lowered or folded. The three men on the right (the envoys) hold nothing: their hands are folded into their sleeves.

Do not include: pith helmets, sun helmets, hard hats, white domed hats, letters or marks on the tablets, any script, seals, extra tablets.
```

## 2. I-4: the Italian merchants are in fifteenth-century dress

**What went wrong:** the three men on the right wear red berets and bobbed pageboy hair. That is fifteenth-century Italian fashion, about 180 years late; the card's `[AVOID]` for Marco names Renaissance dress for the same reason. The Armenian merchants on the left are fine (C32).

```
Edit only the three young merchants on the right side of the quay (red, blue and purple clothes). Change nothing else: the Armenian merchants on the left, the porters, the camels, the ships, the castle and the border stay exactly as they are.

Re-dress them as Italian merchants of the 1270s: a long, plain, belted wool tunic reaching the calf, with long close sleeves; over it a hooded shoulder-cape, the hood down or worn loose on the head, or a plain white linen coif tied under the chin. Hair cut to the jaw or shorter, not bobbed into a smooth bowl. One is clean-shaven, two have short beards. Keep their colours (red, blue, purple), their poses and their gestures.

Do not include: berets, flat caps, round red hats, pageboy or bowl haircuts, doublets, slashed or puffed sleeves, gold chains, letters, script, coats of arms.
```

## 3. III-8: the ship strays from its C7 source and from Polo

**What went wrong:** the ship follows C7 in its lookout box and domed cabin, but three details don't:
- **Anchor:** it is a two-armed anchor with a stock, where C7 has a four-fluked grapnel.
- **Rudder:** none can be seen. C7 has a stern rudder worked by lines, and Polo gives the Hormos ships one rudder.
- **Hull:** it is studded with rows of nail heads, but Polo says these ships use no iron nails.

```
Edit only the ship. Change nothing else: the wind-catcher towers, the men under the awning, the quay, the sea, the coast and the sun stay exactly as they are.

1. The anchor hanging at the bow becomes a four-fluked grapnel: a straight shank ending in four curved hooks, with no crossbar.
2. At the stern, add one clearly visible rudder: a broad, flat wooden blade hung on the sternpost, its upper end joined by two steering lines that run up to the man at the stern, who holds them.
3. Remove every nail head and rivet from the hull. The planks are smooth, joined edge to edge, with plain seams and no iron.
4. The three men hauling ropes at the bow are dark-skinned sailors, bare-chested, in short waist-cloths. Keep their poses.

Do not include: a stocked anchor, a crossbar on the anchor, rows of nails or rivets, a European ship, a crow's nest of planks wider than the C7 lookout box, letters, script.
```

## Report back

Give one line per plate: the file, the number of tries, and whether the fault is gone at 100%.
