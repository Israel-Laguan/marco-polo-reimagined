# Marco Polo Gazetteer — Method Note (v2)

This gazetteer is the **single authority for place names** in the prose and for **coordinates** on the maps. It supports a long-form retelling of Marco Polo's travels in the **Yule–Cordier / *Il Milione*** tradition. It is a place index only (no narrative prose).

**File:** `gazetteer.csv` · **Tooling:** `python3 tools/gazetteer.py check | chapters | report`
**Columns:** `id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,id_confidence,coord_check,wikipedia,chapters,notes`

## Naming policy

- **`book_name`** is the form Yule gives for Polo's name for the place (*Bocara*, *Cascar*, *Tauris*, *Hormos*, *Chandu*, *Kinsay*, *Zayton*). The prose uses it throughout.
- **`aliases`** holds every other spelling (`;`-separated): modern forms (*Bukhara*, *Kashgar*), Yule's or Cordier's variants (*Quinsay*, *Sukchur / Succiu*), Chinese romanisations (*Hu-chau*), and older gazetteer forms. An alias is never a second row.
- **`modern_name`** is the best conventional modern equivalent (city, oasis, region or coast), used as the gloss.
- **Gloss rule.** On the first mention in a chapter, give the book form with its modern gloss: *Cascar (Kashgar)*. After that, the book form only. No bare modern or alternate form in narrative prose (quotations, Notes and tables are exempt). No gloss is needed where the forms coincide (Venice, Genoa, Java, Aden, Acre) or for region labels (Persia, Cathay, Manzi). The lint checks this as `name_policy` (warnings until every chapter has had its pass; see `plans/status/gazetteer-name-diff.md`).
- **Reception chapters** (III-10 to III-12) and front/back matter may use modern forms where they discuss modern scholarship or modern geography; Polo's own places take the book form on first mention.
- **One row per distinct place.** Cities that recur (Venice, Hormos, Tauris, Cambaluc) are not repeated for outbound and return. When two different places share a book form, each gets its own row with ids `-1` / `-2` (*Sinju*: Xining in Vol. I, Yizheng in Vol. II; *Vuju*: Huzhou after Suju, Jinhua on the Fuju road).

## Volume, sequence and leg

| volume | Scope |
|--------|--------|
| 1 | Venice / prologue and the overland journey to the Khan |
| 2 | Realm of Kublai — China circuits and related inland chapters |
| 3 | Seas, India, Africa/Arabia digressions, and the return |

**sequence** is an integer narrative order (steps of 10, so a row can be inserted without renumbering), not a day-by-day itinerary. **leg** is one of: `prologue` | `outbound` | `china` | `maritime` | `return` | `other`.

## Reliability and identification confidence

Two independent questions, two columns.

**`reliability`**: did Polo go there?

| value | Meaning |
|-------|---------|
| `visited` | Strong tradition that Polo (or the elder Polos, for prologue stops) was there |
| `likely_visited` | On the described route; visit is probable but not certain |
| `reported_only` | Described from hearsay, official knowledge, or digression |
| `uncertain` | Place appears in the book, but the visit or the place itself is soft |
| `legendary` | Marvel / folkloric locale with little or no fixed geography |

**`id_confidence`**: do we know where the name points on a modern map?

| value | Meaning |
|-------|---------|
| `firm` | One identification, no serious dispute |
| `probable` | Leading identification (usually Yule's), or a firm place with an approximate point |
| `disputed` | Two or more serious candidates; `notes` names them and says which one the coordinates follow |
| `unfixed` | No usable identification. Latitude and longitude stay blank. **Do not plot.** |

## Coordinates

- Latitude and longitude are **approximate modern centroids** (city, oasis, river crossing or region), rounded to four decimals. They suit maps and storytelling, not archaeology.
- `disputed` rows carry the coordinates of the identification the chapters follow; the alternatives are in `notes`. `unfixed` rows leave them blank on purpose, as do two `disputed` rows whose candidates are too far apart to pick one (*Bangala*: Bengal or Pegu; *Cuju*).
- Region rows (*Persia, Cathay, Manzi, Turcomania, Rosia*, the two Hermenias) are labels, not points. Plot the cities, label the regions.
- **Provisional points.** Many `probable` rows (small Manzi stage-towns, Brius, Camadi, Avah, Casem and the like) carry coordinates set from Yule's or Cordier's notes at the level of a county seat. They are good for a map at book scale and need checking before a close-up (see `GAZ.T6`).

## Coordinate check and Wikipedia

- **`coord_check`** says how the point was checked:
  - `wikipedia`: within 15 km of the coordinates on the English Wikipedia page for the modern place, checked through the API;
  - `region`: a region, river or coast centroid, not comparable to a point;
  - `approximate`: no independent point found yet;
  - `none`: no coordinates.
- **`wikipedia`** is the English Wikipedia URL for the modern place (the gloss). Wikipedia's article title is the reference for "the most commonly used English name". Where Wikipedia and scholarship disagree, the row follows scholarship and says why in `notes` (e.g. Hormos is the mainland *Kingdom of Hormuz*, not *Hormuz Island*).
- Pronunciation and name-origin notes do not live here. They go in the per-volume place glossary (`GLO`), which links each entry through this column. See `plans/research/results/GAZ-intake.md`.

## Chapters column

`chapters` lists the files whose prose uses the book form or any alias (`I-06;II-12;III-F1` — `F` front, `B` back matter). `python3 tools/gazetteer.py chapters` regenerates it; do not edit it by hand.

## Coverage and limits

195 rows: about 80 for Vol. I, 70 for Vol. II, 50 for Vol. III. It covers every place the chapters name as part of Polo's itinerary or the Book's geography, plus the region labels. Not included: peoples and rulers, European and Mediterranean places named only in scholarship (Rome, Pisa, Alexandria), and rivers (the Kian, the Oxus) except where the Book gives them a place of their own (*Caramoran*, *Brius*). Soft identifications (*Pein, Tenduc, Locac, Dagroian, Caugigu, Anin, Nanghin*) stay in with `disputed` and the candidates in `notes`.
