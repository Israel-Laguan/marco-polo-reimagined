# MED — Existing media triage

**Status:** done 2026-11-21 · **Plan doc:** `multimedia-plan.md` § Existing media triage

## Scope
The 22 original files in `media/` and the captions that referenced them.

## Original findings
- `map-indian-ocean.*` is a generated image, geographically wrong (Hormuz at Aden), and captioned as Wikimedia in III-F2 (III-M12).
- `map-hangzhou-kinsay.*` = the West Lake drawing, captioned as a Wikimedia map in II-F2 (II-M8).
- `map-return-route.jpg` is byte-identical to the overview, but captioned as a return schematic (III-F2).
- The overview is captioned "outbound corridor" in I-F2, but shows the whole round trip (I-nit 6).
- Stale "placeholder" text in all three F2 files.
- `map-cambaluc.jpg` and `map-caugigu.jpg` are unused.
- Duplicates: the three Yuan map copies; the `.png`/`.jpg` pairs.
- Resolution: most originals fell short of the 1,350-pixel print width checked in S-08.
- Mongol Empire map: one 9-frame GIF animation, 1206 → 1294, saved also as `.jpg` and `.png` (same bytes). A static print shows the 1206 frame; caption the 1294 frame, "c. 1294" (S-06, `registry/facts.md` F-25).

## Gated by spikes
None for the caption fixes. S-09 ✓ / S-10 ✓ for the replacements: the GEN replacements are `PLT` tasks, and legacy retirement is `PLT.LEGACY`.

## Tasks
- `MED.T1` **done 2026-11-17.** Captions and alt text now say what each image shows: the overview is Dörrbecker’s round-trip reconstruction (German labels noted); the Mongol map is the 1294 frame; the Yuan map shows the 1294 borders only; the Kinsay and Indian Ocean pictures are marked as modern generated illustrations, not maps; III-F2’s duplicate return embed is replaced by a pointer to the overview’s sea loop. All three front-02 files now pass lint. Original task: Correct the captions in I-F2, II-F2 and III-F2: mark generated images as generated, not maps; remove the duplicate return-route embed; drop the "placeholder" sentences.
- `MED.T3` **done 2026-11-17.** Make the legacy files placeable (S-08): 11 of 22 have the wrong extension (all six `drawing-*.png` and `map-hangzhou-kinsay.png`, `map-indian-ocean.png` are JPEGs; both `map-asia-mongol-empire` files are GIFs; `map-china-yuan.jpg` is a PNG). Rename each to its real type (GIF → PNG), drop byte-identical duplicates, and update the references in the F2 files. Only 4 files reach 1,350 px; don't upscale legacy maps for print, since S-09 maps and `PLT` plates replace them. Done when `tools/build/build.sh` shows no placeholder for any file the manuscript references.
  - **Result:** the four kept `drawing-*` files renamed `.png` → `.jpg`. Byte-identical copies removed: `drawing-kinsay-west-lake.png`, `map-hangzhou-kinsay.png`, `drawing-indian-ocean-schematic.png`, `map-indian-ocean.png`, `map-china-yuan.jpg`, `map-yuan-1294.png`, `map-return-route.jpg`, `map-asia-mongol-empire.jpg`. `map-asia-mongol-empire.png` is a PNG of the **1294** frame (F-25). `map-mongol-empire.gif` is the animated master. The three front-02 files built with zero placeholders after references and attributions were updated.
- `MED.T2` **done 2026-11-21.** Archived the 14 surviving files in `media/legacy/` and verified their distinct SHA-256 hashes before and after the move. The three front-02 sections use the edition maps. The Wikimedia PNG remains the sole legacy embed as a credited facsimile in I-B1. Verified the Commons credits and licences in [ATTRIBUTIONS.md](../../../../manuscript/assets/ATTRIBUTIONS.md), including both Chumwa JPEGs. All 38 local manuscript image links resolve. The four-file PDF build reported zero placeholders and rendered the facsimile with its caption. All three front-02 files pass lint. I-B1 still has the existing length error (1,262 words against 1,200).
