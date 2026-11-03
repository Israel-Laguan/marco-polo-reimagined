# GAZ — Gazetteer

**Status:** in progress (T1–T4 done by S-04, 2026-10-22) · **Plan doc:** `content-revision-plan.md` § W5; S-04

## Scope
`gazetteer.csv` as the single authority for place names (prose) and coordinates (maps). Method note: `gazetteer-readme.md`. Tooling: `python3 tools/gazetteer.py check | chapters | report`.

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

- **Lint rule** (`tools/lint.py` `name_policy`, warning): a non-canonical form used bare in a narrative chapter; the first mention of a book form without a gloss. Promote to error after the last chapter naming pass (`.T3`/`.T1` of every file).

## Backlog
- **After S-04 (2026-10-22), Pelliot's full entries changed three rows:** Nanghin → Kaifeng; Madeigascar → Mogadishu (Magadoxo merged; 194 rows); Locac → Lopburi. See `research/results/GAZ-citable-findings.md` § 6 and `GAZ-pelliot-locators.csv` (Pelliot locators for 156 rows).
- Coordinates are county-seat precision for the 58 `probable` rows and absent for the 14 rows without a point (12 `unfixed`, plus the `disputed` Bangala and Cuju); none has been checked against a second source beyond Yule/Cordier notes and general reference.
- front-02 place tables (3 volumes) still follow the old gazetteer and must be regenerated.
- The chapters themselves are inconsistent (*Tauris/Tabriz*, *Hormos/Hormuz*, *Kisi/Kish/Kis*, *Chandu/Shangdu*): 86 places, 245 bare variants in `plans/status/gazetteer-name-diff.md`. They are fixed in each chapter's naming pass.
- ch-11 mentions a "little Caiju" opposite Coiganju; Yule's only Caiju is Kwa-chau (flag for II-11's naming pass).

## Gated by spikes
S-04 ✓ · S-09 (map styling of `disputed`/`unfixed`) · S-16, S-17, S-18 (identification checks per volume)

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
- **Status:** backlog · **Depends:** S-04 ✓ · feeds `I-F2.T1`, `II-F2.T1`, `III-F2.T1`
- **Do:** write `tools/gazetteer.py tables <vol>` that prints the three-column tables (Book name | Modern | Role) from rows with `volume = N`, split by `leg`/group as the current front-02 does, using `book_name`, `modern_name` and a short role taken from the first sentence of `notes`. Replace the hand-written tables; keep the "map cautions" prose by hand. Skip `unfixed` rows or list them in a "no fix" line (Male and Female, Arbre Sec).
- **Done when:** the tables in the three front-02 files equal the generated output and the lint shows no new errors.

### GAZ.T6 — Verify provisional coordinates and identifications
- **Status:** in progress (2026-10-22: first research pass taken in, `research/results/GAZ-intake.md`; 123 points agree with Wikipedia, 4 moved, `coord_check` and `wikipedia` columns added; no `id_confidence` changed) · **Depends:** S-16 (Vol. I), S-17 (Vol. II), S-18 (Vol. III) — their deep-research output (`research/results/`) did not exist when S-04 closed
- **Do:** when each run is taken in, check the `probable` and `disputed` rows against a second source (Cordier's notes, Pelliot, a modern gazetteer) and move each to `firm` or record why not. Priority: Brius, Camadi, Avah, Casem, Pashai, Erguiul, Egrigaia, Bargu, Linju, Vughin, Changshan, Unken, Mutfili, Soer.
- **Done when:** no row's `notes` says "approximate" without a source, and `disputed` rows name their candidates.

### GAZ.T7 — Promote `name_policy` to an error
- **Status:** backlog · **Depends:** the naming pass in every chapter (`.T3` / `.T1` items)
- **Do:** change the `name_policy` severity in `tools/lint.py` from warning to error and rebaseline.
- **Done when:** `python3 tools/lint.py` reports no `name_policy` errors on the 49 files.
