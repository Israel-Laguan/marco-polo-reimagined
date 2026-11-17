# MED — Existing media triage

**Status:** backlog · **Plan doc:** `multimedia-plan.md` § Existing media triage

## Scope
The 22 files already in `media/` and every caption that references them. This is the only area with **reader-facing errors fixable today**, without waiting on spikes.

## Backlog
- `map-indian-ocean.*` is a generated image, geographically wrong (Hormuz at Aden), and captioned as Wikimedia in III-F2 (III-M12).
- `map-hangzhou-kinsay.*` = the West Lake drawing, captioned as a Wikimedia map in II-F2 (II-M8).
- `map-return-route.jpg` is byte-identical to the overview, but captioned as a return schematic (III-F2).
- The overview is captioned "outbound corridor" in I-F2, but shows the whole round trip (I-nit 6).
- Stale "placeholder" text in all three F2 files.
- `map-cambaluc.jpg` and `map-caugigu.jpg` are unused.
- Duplicates: the three Yuan map copies; the `.png`/`.jpg` pairs.
- Resolution: all files except `map-marco-polo-overview.png` are below print size.
- Mongol Empire map: one 9-frame GIF animation, 1206 → 1294, saved also as `.jpg` and `.png` (same bytes). A static print shows the 1206 frame; caption the 1294 frame, "c. 1294" (S-06, `registry/facts.md` F-25).

## Gated by spikes
None for the caption fixes. S-09 ✓ / S-10 ✓ for the replacements: the GEN replacements are `PLT` tasks, and legacy retirement is `PLT.LEGACY`.

## Tasks
- `MED.T1` **done 2026-11-17.** Captions and alt text now say what each image shows: the overview is Dörrbecker’s round-trip reconstruction (German labels noted); the Mongol map is the 1294 frame; the Yuan map shows the 1294 borders only; the Kinsay and Indian Ocean pictures are marked as modern generated illustrations, not maps; III-F2’s duplicate return embed is replaced by a pointer to the overview’s sea loop. All three front-02 files now pass lint. Original task: Correct the captions in I-F2, II-F2 and III-F2: mark generated images as generated, not maps; remove the duplicate return-route embed; drop the "placeholder" sentences.
- `MED.T3` **done 2026-11-17.** Make the legacy files placeable (S-08): 11 of 22 have the wrong extension (all six `drawing-*.png` and `map-hangzhou-kinsay.png`, `map-indian-ocean.png` are JPEGs; both `map-asia-mongol-empire` files are GIFs; `map-china-yuan.jpg` is a PNG). Rename each to its real type (GIF → PNG), drop byte-identical duplicates, and update the references in the F2 files. Only 4 files reach 1,350 px; don't upscale legacy maps for print, since S-09 maps and `PLT` plates replace them. Done when `tools/build/build.sh` shows no placeholder for any file the manuscript references.
  - **Result:** the four kept `drawing-*` files renamed `.png` → `.jpg`. Byte-identical copies removed: `drawing-kinsay-west-lake.png`, `map-hangzhou-kinsay.png`, `drawing-indian-ocean-schematic.png`, `map-indian-ocean.png`, `map-china-yuan.jpg`, `map-yuan-1294.png`, `map-return-route.jpg`, `map-asia-mongol-empire.jpg`. `map-asia-mongol-empire.png` is now a real PNG of the **1294** frame (F-25), not the GIF's default 1206 frame; `map-mongol-empire.gif` is kept as the animated master. F2 references and ATTRIBUTIONS updated. A build of the three front-02 files places all five images with no placeholder. III-F2's return map now points at the overview it was always a copy of; its caption still says "return schematic", which is `MED.T1`.
- `MED.T2` Move the files to `media/legacy/`, dedupe, update ATTRIBUTIONS (after the replacements exist). Also check the licence and credit line of each kept Wikimedia map (the Chumwa overview, the Shepherd 1911 overlay): the I-F2 and II-F2 backlogs had listed this under S-11, which covered plates only.
