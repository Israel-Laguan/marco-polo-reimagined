# Marco Polo Gazetteer — Method Note

This gazetteer supports a long-form retelling of Marco Polo’s travels in the **Yule–Cordier / *Il Milione*** tradition. It is a place index only (no narrative prose).

**File:** `gazetteer.csv`  
**Columns:** `book_name,modern_name,latitude,longitude,volume,sequence,leg,reliability,notes`

## Naming policy

- **book_name** follows forms familiar from Polo / Yule (e.g. *Cambaluc*, *Quinsay*, *Zayton*, *Hormuz*), with a common modern gloss in parentheses when helpful.
- **modern_name** is the best scholarly or conventional equivalent (city, oasis, region, or coast). Aliases and alternate spellings appear in **notes**, not as duplicate rows.
- One row per **distinct place**. Cities that recur (Venice, Hormuz, Tabriz, Cambaluc, etc.) are not repeated for outbound vs return; recurrence is noted in **notes**.

## Volume and sequence

| volume | Scope |
|--------|--------|
| 1 | Venice / prologue and the overland journey to the Khan |
| 2 | Realm of Kublai — China circuits and related inland chapters |
| 3 | Seas, India, Africa/Arabia digressions, and the return |

**sequence** is an integer narrative order (outbound → China → maritime → return → other/marvels), not a precise day-by-day itinerary. Gaps in numbering leave room for later inserts.

**leg** is one of: `prologue` | `outbound` | `china` | `maritime` | `return` | `other`.

## Reliability meanings

| value | Meaning |
|-------|---------|
| `visited` | Strong tradition that Polo (or the elder Polos, for prologue stops) was there |
| `likely_visited` | On the described route; visit is probable but not certain |
| `reported_only` | Described from hearsay, official knowledge, or digression |
| `uncertain` | Place appears in the book, but modern ID is disputed or soft |
| `legendary` | Marvel / folkloric locale with little or no fixed geography |

## Coordinates

- Latitude and longitude are **approximate modern centroids** (city, oasis, or region), drawn from established public geographic references (Wikipedia/Wikidata-style city points and standard Yule-note identifications).
- Rounded to **at most four decimal places**. They are suitable for maps and storytelling, **not** archaeological precision.
- Purely legendary entries may leave lat/long blank and explain why in **notes**.
- Regional entries (deserts, coasts, plateaus) use a representative center of the area Polo implies.

## Coverage and limits

About 80–120 major places: not every village or ethnonym in the book. Soft or contested IDs (e.g. *Pem*, *Tenduc*, *Locac*, *Dagroian*, *Caugigu*) are included with `uncertain` (or `reported_only`) and a short caveat. Emblematic marvels (*Chipangu*, Prester John, Islands of Men/Women, Lop “spirits”) are flagged accordingly.

