# III-F2 — Maps for the Seas and the Return

**File:** `vol-3/front-02-maps-seas-and-return.md` · **Status:** revised 2026-11-24, human review pending · **Kind:** front

| Narrative words | Verbatim Yule | Tag | Citations | Over length? |
|---|---|---|---|---|
| 237 | 12% | — | 8/8 | no |

## Original critique

References point to the draft examined in the critique. The task entries record the revisions.

### Critical
- Invented epigraph: "And from Zayton they sailed…", labelled a "Book III itinerary hinge". It does not exist in Yule; the Prologue never names Zayton (III-09 Note [8] concedes as much). Fix: use Prologue xviii, "They put forth to sea, and after sailing for some three months they arrived at a certain Island towards the South…" (`yule-vol1.txt`). — vol-3 C1 · front-02:4
- "Soft" label tic: 1 in the place table ("Soft peninsula ID", :39), plus Note [3] "Soft and legendary toponyms" (:90). Fix: strip the label. — vol-3 C2 · front-02:39, :90
- Scaffolding: "Image paths point at `../media/` placeholders" (:9) and Note [1] "media placeholders" (:86) — stale "placeholder" text, caught by the W0 scaffolding check. — content-revision-plan W1.3 / W0 · front-02:9, :86

### Factual / fidelity
- Generated "map" is geographically wrong and mis-credited: `media/map-indian-ocean.jpg` captioned "(Wikimedia Commons — credit in media/ATTRIBUTIONS.md)", but `ATTRIBUTIONS.md` lists it as a *generated* plate (byte-identical in size to `map-indian-ocean.jpg (generated drawing)`). Errors: "Hormuz" at the southern tip of Arabia (the Aden position); "SINAE" over Persia; China north-east of India with an overland route across the Himalaya; Ceylon on the wrong side of the peninsula; post-1500 three-masted European ships. Fix: replace, or caption "decorative plate — not a map" (credit: generated). Multimedia plan verdict: **Drop**. — vol-3 M12 · front-02:19-21
- `map-return-route.jpg` is byte-identical to `map-marco-polo-overview.jpg` (checked with `cmp`), though its caption describes a dedicated return schematic; caption also credits Wikimedia. Fix: replace with the real return-route map (A16 / critique §5 item 1). Multimedia plan: front-02 captions "must be corrected now". — vol-3 M12 · front-02:27-29
- Place table equates Polo's Male with the Maldives ("Male / Maldives | Maldives | Cowries and ambergris"), as does the gazetteer row. III-07:13 and its Note [2] explicitly refuse that collapse, and Polo mentions no cowries there. Fix: list "Male and Female Isles — legendary (no fix)" and rename or annotate the gazetteer row. — vol-3 m3 · front-02:62

### Dispute handling and Ramusio flags
— none found

### Voice and prose
— none found (one "Anyway" at :80, within the ≤ 1 limit)

### Notes and apparatus
— none found beyond the Soft/placeholder items above

### Naming and gazetteer
- Gazetteer forms instead of the book's Yule forms: `Sememant` (ch-06 and Yule: *Semenat*, :23) and `Kalhat` (ch-08 and Yule: *Calatu*, :68). Scorecard also flags "non-gazetteer names". Fix: W5 switches gazetteer `book_name` to the Yule forms and regenerates the front-02 place tables from it. — vol-3 m4 · front-02:23, :68
- **Resolved at policy level by S-04 (2026-10-22):** `gazetteer.csv` v2 uses Yule forms and has the missing rows; this file's names are applied in `III-F2.T1`.

### Length and structure
- Front/back de-duplication per W5 (front matter frames; chapters narrate). — content-revision-plan W5 · front-02

## Media hooks
- **Maps in the guide:** A1 series overview and A16 Cocachin return. Both depict Chamba–Samara as inferred. A16 identifies Abhar separately as an embassy site and shows the named western stages along an illustrative course. See [MAP.T01 and MAP.T16](../../cross/MAP-maps.md) and the [text and media handoff](../../../../../archive/editorial/status/critique-text-media-handoff-2026-11-17.md).
- **Chapter links:** A15 (III-1), A17 (III-5) and C11 (III-9).
- **Tables:** Both place tables and the no-fix list come from the series gazetteer.

## Gated by spikes

- S-02, S-03 (Notes format), S-04 (gazetteer authority; Male/Maldives; Yule forms), S-06 (map and Male corrections), S-07 (front/back roles), S-08 (tables, figures), S-09 (A1, A16)

## Tasks

### III-F2.T1 — Names to the S-04 policy; facts per S-06

- **Status:** revised 2026-11-24, human names and factual review pending · **Depends:** S-04 ✓, `GAZ.T5` ✓, S-06 ✓.
- **Epigraph:** Retained the exact Book III.1 quotation verified in the local Yule–Cordier text. It replaces the invented quotation flagged in the original critique.
- **Names:** Checked prose against the gazetteer because `name_policy` omits front matter. The tables match their generated output, including Semenat, Calatu and the no-fix entry for Male and Female.
- **Attribution:** Distinguishes the Prologue’s “Java” from the separate Samara passage and attributes their connection to Yule. Qualifies the proposed Zayton departure, intermediate calls and Hormos landfall. Abhar locates Cocachin’s marriage in Rashid al-Din’s record, which leaves the Polos unnamed.

### III-F2.T3 — De-duplicate to the S-07 role matrix

- **Status:** revised 2026-11-24, human voice review pending · **Depends:** S-07 ✓.
- **Applied:** The guide carries the sea route and map index, one sentence on claimed visits and reports, and a single monsoon pointer. Identification cautions cover Java, Madeigascar and the Volume I entries. The Chipangu reception aside is removed. Lint measures 237 prose words against a target of 500.

### III-F2.T4 — Notes and apparatus to the S-03 convention

- **Status:** revised 2026-11-24, human Notes review pending · **Depends:** S-03 ✓, `APP.T2` ✓.
- **Applied:** Eight marked Notes with sequential anchors. Checked the Yule–Cordier passages and the pointers to III-3, Notes 1 and 14, III-7, Note 13, and III-9, Notes 12–15, 20–22 and 28. The Abhar locator follows the scan check recorded in the comparanda registry.
- **Check:** `markers`, `tags` and `citations` pass.

### III-F2.T5 — Media placement

- **Status:** verified 2026-11-24 · **Depends:** S-08 ✓, S-09 ✓.
- **Applied:** Retained A1 and A16’s vector artwork. The captions explain the reconstructed legs, Abhar’s separate marker, and the Minab-area reference. A16 keeps Yule’s and Yang Zhijiu’s attributed departure estimates. The index points to A15, A17 and C11.
- **Check:** Volume III PDF and HTML built successfully. All three links resolve to their figures in both formats. Proofed print pages xv–xxii, including the maps and captions on xvi–xvii, the table breaks, and the eight linked Notes. The PDF build reported zero placeholders and zero undersized rasters. It reported one overfull line in Chapter III-6.

### III-F2.T6 — Lint green and human read

- **Status:** automated checks pass, human sign-off pending · **Depends:** every other task in this file · S-02 ✓.
- **Baseline (2026-10-22, `plans/status/lint-baseline.md`):** 4 errors and 0 warnings in `markers`, `quote_verify` and `scaffolding`.
- **Checked 2026-11-24:** `python3 tools/lint.py -v vol-3/front-02-maps-seas-and-return.md` reported 0 errors and 0 warnings. `python3 tools/gazetteer.py check` reported 198 rows and 0 problems. Both tables and the no-fix list match `python3 tools/gazetteer.py tables 3`. All 49 book tests passed.
- **Remaining:** Human review of names, factual wording and the Notes, and a voice read against II-2.
