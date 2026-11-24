# GAZ — Gazetteer

**Status:** T1–T7 complete, T8 sheets in editorial review · **Plan doc:** `content-revision-plan.md` § W5 and S-04

## Scope
`gazetteer.csv` is the authority for place names and map coordinates. See the [method note](../../../gazetteer-readme.md) for the validation, chapter usage, naming report and table commands.

## Decided (S-04, closed 2026-10-22)
- **Authority.** `book_name` = Yule's form of Polo's name, as the chapters use it; every other spelling is in `aliases`; `modern_name` is the gloss.
- **Schema v2.** `id,book_name,aliases,modern_name,latitude,longitude,volume,sequence,leg,reliability,id_confidence,chapters,notes`. `reliability` (did Polo go?) and `id_confidence` (do we know where it is?) are separate; `notes` holds only prose. `chapters` is generated.
- **Gloss rule.** Book form + modern gloss on first mention per chapter; none for Venice, Genoa, Java, Aden, Acre or region labels. No bare non-canonical forms in narrative prose. Reception chapters (III-10 to III-12) and front/back matter are exempt in the lint.
- **Rows.** 112 → 195: 86 added (Vol. I 34, Vol. II 41, Vol. III 11; five of them region labels), three merged away (Pazanjin/Hezhong into Cachanfu; Desert of Lop spirits into Desert of Lop; Male / Maldives and Island of Women / Men into one *Male and Female*).
- **Conflicts resolved** (rationale in each row's `notes`):

| Name | Old gazetteer | v2 | Authority |
|---|---|---|---|
| Cachanfu | Xi'an | Puzhou (Hezhong), Yellow River; Kenjanfu = Xi'an | II-M2; Yule |
| Cacanfu | Puyang/Heze | Hejian, Hebei | ch-10:13; Yule |
| Caugigu | Tonkin | Kiang Hung (`disputed`; Tonkin is the *name*, Laos the *description*) | Yule note 6, ch. LVI–LIX; ch-09; `map-caugigu.jpg` |
| Nanghin | Nanjing | Anqing (`disputed`; Nanjing kept as alias) | Yule note 1, ch. LXIX; ch-11:31 |
| Vuju | one row (Huzhou) | `vuju-1` Huzhou (after Suju); `vuju-2` Jinhua (Fuju road) | ch-12:65; ch-14:13; Cordier |
| Sinju | — | `sinju-1` Xining (Vol. I); `sinju-2` Yizheng (Vol. II) | Yule |
| Male | Maldives | *Male and Female*, legendary, unplotted | III-m3; ch-07:13 |
| Badakhshan | alias "Balashan" | form *Badashan*; "Balashan" is not Polo's name | I-M8 |
| Arbre Sec | Dasht-e Kavir centroid | `unfixed`, no coordinates (the centroid was a placeholder) | Yule |

- **Lint rule** (`tools/lint.py` `name_policy`): a bare place variant or a missing first gloss is an error in narrative prose. The place naming pass is complete.

## Follow-ups and decisions since S-04
- **After S-04 (2026-10-22), Pelliot's full entries changed three rows:** Nanghin → Kaifeng; Madeigascar → Mogadishu (Magadoxo merged; 194 rows); Locac → Lopburi. See `research/results/GAZ-citable-findings.md` § 6 and `GAZ-pelliot-locators.csv` (Pelliot locators for 156 rows).
- The [T6 review](../../research/results/GAZ-T6-review.md) records the sources and limits of the provisional points. Blank coordinates remain for 12 unfixed rows and the disputed Bangala and Cuju.
- Yule distinguishes the unlocated Caiju opposite Coiganju on the Yellow River (II-10) from Caiju on the Kiang (II-12), which he identifies with Kwa-chau. The gazetteer point represents the latter. The Tana of the Sea of Azov in I-01 is also distinct from the Indian Tana in the CSV.

## Gated by spikes
S-04 and S-09 closed. S-16, S-17 and S-18 intakes complete on a best-effort basis.

## Tasks
### GAZ.T1 — Schema v2
- **Status:** done (S-04) · `gazetteer.csv` has the 13 columns above; `python3 tools/gazetteer.py check` validates enums, ids, sequences, coordinates and form clashes.

### GAZ.T2 — Rename to Yule forms and add aliases
- **Status:** done (S-04) · every `book_name` is the Yule form the chapters use; alias columns carry the modern and variant forms; the readme states the policy.

### GAZ.T3 — Missing rows
- **Status:** done (S-04) · 86 rows added; every row is used by at least one chapter (`chapters` column).

### GAZ.T4 — Resolve conflicting identifications
- **Status:** done (S-04) · see the table above.

### GAZ.T5 — Regenerate the front-02 place tables
- **Status:** done (2026-11-21). The three front-matter sections match the generator and cover all 194 rows, including the no-fix lists.
- **Do:** write `tools/gazetteer.py tables <vol>` that prints the three-column tables (Book name | Modern | Role) from rows with `volume = N`, split by `leg`/group as the current front-02 does, using `book_name`, `modern_name` and a short role taken from the first sentence of `notes`. Replace the hand-written tables; keep the "map cautions" prose by hand. Skip `unfixed` rows or list them in a "no fix" line (Male and Female, Arbre Sec).
- **Done when:** the tables in the three front-02 files equal the generated output and the lint shows no new errors.

### GAZ.T6 — Verify provisional coordinates and identifications
- **Status:** done, best effort (2026-11-21). Camadi moved to the Jiroft regional reference and A1 was rebuilt. The [review](../../research/results/GAZ-T6-review.md) records the evidence limits for the remaining provisional points. The S-18 access-dependent checks remain deferred.
- **Do:** when each run is taken in, check the `probable` and `disputed` rows against a second source (Cordier's notes, Pelliot, a modern gazetteer) and move each to `firm` or record why not. Priority: Brius, Camadi, Avah, Casem, Pashai, Erguiul, Egrigaia, Bargu, Linju, Vughin, Changshan, Unken, Mutfili, Soer.
- **Done when:** no row's `notes` says "approximate" without a source, and `disputed` rows name their candidates.

### GAZ.T7 — Promote `name_policy` to an error
- **Status:** done (2026-11-21). Place-name violations are errors and the 49-file lint run reported zero. On 2026-11-24, CHR.T6 promoted character-name findings to errors as well.
- **Do:** change the `name_policy` severity in `tools/lint.py` from warning to error and rebaseline.
- **Done when:** `python3 tools/lint.py` reports no `name_policy` errors on the 49 files.


### GAZ.T8 — Place reference lists and reference sheets
- **Status:** in editorial review (2026-11-21). The [registry](../../registry/place-references.yaml) covers 44 settings and contextual references. Seven draft sheets have reviewed sidecars. Hormos, Badashan, Pamier and the Desert of Lop have gap sidecars.
- **Why:** the plates show places (Chandu, Cambaluc, Kinsay, Zayton, Hormos, Venice, Ayas, Baudac…). Their sources (C-cues, S-23 site records such as Deji Gate, the Ayas castles, Kota Cina) are spread across `registry/visual-references.md`, and nothing ties them to a gazetteer row.
- **Scope:** only places that a plate in `illustration-plan.md` shows, about 30 of the 194 rows. The others need no image.
- **Do:**
  1. Add `registry/place-references.yaml`, keyed by gazetteer `id`. For each place, list the references in the same fields as `CHR.T8`, plus `period` (does the source show 1260–95 fabric, or later?) and `avoid` (for example the Forbidden City or yellow Ming tiles for Dadu, and the Ottoman circuit for Ayas).
  2. For the places that recur, make one establishing sheet each, in the CHR.T9 format: `media/places/<id>-sheet.*` with a sidecar. The recurring places are Cambaluc/Dadu, Chandu, Kinsay, Zayton, Hormos, Venice and Acre/Ayas. A gap with no source (Badakhshan, Pamier, Lop, per the gap ledger) gets a sidecar that says so, and no sheet.
- **Coverage:** The Kublai portrait frontispiece, the Aijaruc wrestling scene, and the paper-money and post scenes without a fixed setting rely on figure, object or narrative sources. The III-9 farewell venue is unknown. Cambaluc and Chandu are court comparanda for that material.
- **Done when:** every plate place has a reference list, and every recurring place has a sheet or a recorded reason why it has none.

## S-16 best-effort handoff to GAZ.T6 (2026-11-11)

- **Hormos:** approximate uncertain pin is modern Minab as a regional reference; it is not the K-103 site. Label “Hormos? (Minab area)” and state the proxy in captions.
- **Tonocain:** Qaen is a regional reference, not a provincial boundary; **Arbre Sec** is unlocated and has no point.
- **Pein:** provisional Uzun-tatïr with Keriya as named alternative; **Tenduc:** Hohhot region marker only, not a city identification. Preserve `disputed` and do not conflate Sichintingiu.
- See [S-16 closeout](../../research/results/S-16-closeout.md) and the [later T6 review](../../research/results/GAZ-T6-review.md).

## S-17 handoff to GAZ.T6 (2026-11-11)

Use `registry/facts.md` S17-F4 and [the six-case table](../../research/results/S-17-intake.md#six-gazetteer-cases--s-04--gazt6). Existing locations are provisional regional reference points. Label Yule and Pelliot's competing Caugigu, Anin and Coloman interpretations separately; Cuiju is not an established Guiyang city identification. Do not silently upgrade the six confidence grades or move pins without a source and synchronized map review.
