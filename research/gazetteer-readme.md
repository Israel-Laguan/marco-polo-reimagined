# Marco Polo Gazetteer — Method Note (v2)

This gazetteer is the **single authority for place names** in the prose and for **coordinates** on the maps. It supports a long-form retelling of Marco Polo's travels in the **Yule–Cordier / *Il Milione*** tradition. It is a place index only (no narrative prose).

The data lives in [gazetteer.csv](gazetteer.csv). Its columns are `id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,id_confidence,coord_check,wikipedia,chapters,notes`.

Run these commands from `book/`.

```bash
python3 tools/gazetteer.py check        # validate the CSV
python3 tools/gazetteer.py report       # report non-canonical place names by chapter
python3 tools/gazetteer.py chapters     # regenerate the chapters column in the CSV
python3 tools/gazetteer.py tables 1     # print Volume I's front-02 place tables
```

## Naming policy

- **`book_name`** is the form Yule gives for Polo's name for the place (*Bocara*, *Cascar*, *Tauris*, *Hormos*, *Chandu*, *Kinsay*, *Zayton*). The prose uses it throughout.
- **`aliases`** holds every other spelling (`;`-separated): modern forms (*Bukhara*, *Kashgar*), Yule's or Cordier's variants (*Quinsay*, *Sukchur / Succiu*), Chinese romanisations (*Hu-chau*), and older gazetteer forms. An alias is never a second row.
- **`modern_name`** is the best conventional modern equivalent (city, oasis, region or coast), used as the gloss.
- **Gloss rule.** On the first mention in a chapter, give the book form with its modern gloss, as in *Cascar (Kashgar)*. After that, use the book form throughout narrative prose. Quotations, Notes and tables are exempt. Places whose forms coincide (Venice, Genoa, Java, Aden, Acre) and region labels (Persia, Cathay, Manzi) can stand without a gloss. The lint reports violations as `name_policy` errors. See the [naming report](../editorial/plans/status/gazetteer-name-diff.md).
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
- `disputed` rows carry the coordinates of the identification the chapters follow; the alternatives are in `notes`. `unfixed` rows leave them blank on purpose, as do `disputed` rows where no defensible point has been selected (*Bangala* and *Cuju*). For *Hormos*, the point is a regional reference at modern Minab, not the site of Old Hormuz; every map must label it “Hormos? (Minab area)” and explain the proxy in its caption.
- Region rows (*Persia, Cathay, Manzi, Turcomania, Rosia*, the two Hermenias) are labels, not points. Plot the cities, label the regions.
- **Provisional points.** Several `probable` rows use an approximate modern city, county or river reference. Camadi uses modern Jiroft, for example, and Casem uses the Kishim District point. The [coordinate review](investigations/results/GAZ-T6-review.md) records the evidence and limits of each retained point.

## Coordinate check and Wikipedia

- **`coord_check`** says how the point was checked:
  - `wikipedia`: within 15 km of the coordinates on the English Wikipedia page for the modern place, checked through the API;
  - `region`: a region, river or coast centroid, not comparable to a point;
  - `approximate`: a provisional point, including modern positions used as proxies for unlocated historical sites;
  - `none`: no coordinates.
- **`wikipedia`** is the English Wikipedia URL for the modern place (the gloss). Wikipedia's article title is the reference for "the most commonly used English name". Where Wikipedia and scholarship disagree, the row follows scholarship and says why in `notes` (e.g. Hormos is the mainland *Kingdom of Hormuz*, not *Hormuz Island*).
- Pronunciation and name-origin notes do not live here. They go in the per-volume place glossary (`GLO`), which links each entry through this column. See `plans/research/results/GAZ-intake.md`.

## Chapters column

`chapters` lists the files whose prose uses the book form or any alias (`I-06;II-12;III-F1` — `F` front, `B` back matter). `python3 tools/gazetteer.py chapters` regenerates it; do not edit it by hand.

## Front-matter tables and place references

Run `python3 tools/gazetteer.py tables <1|2|3>` and use its output to replace the place-table section in the corresponding `front-02`. The volume determines which rows appear. The route groups follow narrative sequence and briefly describe each stop using the opening sentence of its notes. The separate list at the end gives the names without a map fix.

The [plate reference registry](registry/place-references.yaml) uses these same place IDs for scene references and establishing sheets. Source dates and limits accompany each reference. Sheet sidecars record the prompt, sources, and review status.

## Coverage and limits

The gazetteer has 194 rows as of 2026-11-21, with 79 assigned to Volume I, 68 to Volume II, and 47 to Volume III. Magadoxo was merged into Madeigascar after the S-04 review. The gazetteer covers places from Polo's itinerary and the Book's geography, plus region labels. It excludes people, places named only in scholarship (such as Rome, Pisa, and Alexandria), and rivers except where the Book treats them as places in their own right, such as *Caramoran* and *Brius*. For disputed identifications such as *Pein*, *Tenduc*, and *Caugigu*, the candidates appear in `notes`.
