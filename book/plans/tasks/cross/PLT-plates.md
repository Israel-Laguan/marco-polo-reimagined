# PLT — Drawings and plates

**Status:** backlog · **Plan docs:** `illustration-plan.md`, `illustration-style-guide.md`

## Scope
Event illustrations: 34 generated (GEN) hero plates, 7 public-domain (PD) heroes, about 25 optional secondaries, plus retirement of the 6 legacy `drawing-*.png`. Cutaway bases for diagrams C12–C16 are produced here and labelled in `DIA`.

## Backlog
- Hero list per chapter: `illustration-plan.md` § Hero plates (also mirrored in each chapter backlog's Media hooks).
- PD slots: I-2 (LdM Polos at court), II-front (Kublai portrait), II-4 (Liu Guandao), III-1 (*Mōko Shūrai*), III-7 (Qazwini rukh), III-11 (Columbus postils / 1477 woodcut), III-12 (Catalan Atlas caravan).
- Legacy plates to retire (period errors per critique):
  - `drawing-venetian-galley` (17th-c. Salute domes, Viking-like hull);
  - `drawing-chandu-palace` (Renaissance villa);
  - `drawing-genoa-dictation` (monk's habit, chains);
  - `drawing-manzi-junk` (Western galleried stern, portholes);
  - `drawing-kinsay-west-lake`, `drawing-indian-ocean-schematic` (mislabelled as maps).
- Each plate: sidecar `.yaml` (prompt, model, seed, date, tradition, caption) → an `ATTRIBUTIONS.md` row.

## Gated by spikes
S-10 (generator, pilot) · S-11 (PD licences) · S-05 ✓ (character cards: `registry/character-cards.yaml`; each plate with a recurring person takes its `[PERIOD]`/`[AVOID]` lines from `tools/characters.py cue`, and its scene row must pass `tools/characters.py ages`) · S-08 (pixel sizes from trim)

## Tasks
_After S-10 and S-11: one task per plate, in volume order:_ `PLT.I-01` … `PLT.III-12`, plus `PLT.S*` for secondaries and `PLT.LEGACY` (retire and re-caption).
