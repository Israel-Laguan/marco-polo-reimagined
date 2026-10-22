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
- Mongol Empire map date range unverified.

## Gated by spikes
None for the caption fixes. S-09 / S-10 for the replacements.

## Tasks
- `MED.T1` **(ready now)** Correct the captions in I-F2, II-F2 and III-F2: mark generated images as generated, not maps; remove the duplicate return-route embed; drop the "placeholder" sentences.
- `MED.T2` Move the files to `media/legacy/`, dedupe, update ATTRIBUTIONS (after the replacements exist).
