# Intake — gazetteer deep research (coordinates, names)

_2026-10-22. Raw runs: `GAZ-coords-raw.md`, `GAZ-names-raw.md` (prompts in `../prompts/`). Applies to `GAZ.T6` and `GLO`._

## Trust check

**Coordinates run: weak as evidence.** Of 93 Group A rows, 52 come back "CONFIRMED", but nearly all of them repeat our own coordinates to the last digit, with "Standard" or "Accepted" in the source column. The prompt asked for at least one non-Yule source per row; only two rows have one (Sarai, Ucaca). Group B is a single paragraph, not a per-row check. So the run does not raise any row's `id_confidence`. What it is good for:
- two cited points (Ukek, Sarai);
- an independent list of which rows have no fix (it matches our `unfixed` and `disputed` sets exactly);
- leads for further reading (Pelliot, Haw, Vogel, Nedashkovsky on Ukek), none checked here.

**Names run: partial and mostly unsourced.** The table covers about 120 of 195 rows. The Latham and Moule–Pelliot variant columns are not actually filled in. The answer to "Yule vs Latham" is generic. IPA is given for 3 rows; every other respelling has no source. Errors spotted:
- **Hormos** is linked to *Hormuz Island*, the later island town. Polo's Hormos is the mainland town, Wikipedia *Kingdom of Hormuz*.
- **Negropont "Italian 'black bridge'"** is a folk etymology. The name comes from Greek *Evripos* via *Egripo*, later reshaped as *Negro ponte*.
- **Caracoron "Mongol 'black camp'"** is doubtful. Usual glosses are "black rocks / boulders". Unverified.
- **Ucaca "Mongol *ügäk*, 'dam'"** is unverified.
- **Kisi "island vs mainland" trap**, which doesn't apply.

Its one firm conclusion agrees with S-04: **no book-form changes**. Keep the Yule forms and use the gloss for the common modern name (Chandu (Shangdu), Tauris (Tabriz), Hormos (Old Hormuz), Kisi (Kish), Kinsay (Hangzhou), Zayton (Quanzhou)).

## Independent check run here (Wikipedia API, 2026-10-22)

To check the runs rather than trust them, every Wikipedia title the names run gave (102), plus our own title for each modern place (156), was queried against the English Wikipedia API. Each page was checked for existence, its final title after redirects, and its coordinates.
- **Every one of the 102 URLs exists.** Two redirect to a better title: *Khanbaliq* → *Dadu (Beijing)*, *Somnath* → *Somnath Temple*.
- **123 rows now agree with Wikipedia's point to within 15 km.** That counts the four moved below, plus Curzola, whose point is the town and Wikipedia's is the island.
- **46 region, river or coast rows** differ from Wikipedia's centroid by 30–950 km. That is expected (Wikipedia places the Yellow River at its mouth and Rus' at Kyiv), and they are labels, not points.
- **12 rows have no Wikipedia point to compare** (Sarai, Avah, Camadi, Vughin, Ganfu, Ferlec, Basma, Samara, Lambri, Mutfili, Eli, Soer). They stay `approximate`.

## Applied to `gazetteer.csv`

- **New columns:**
  - `coord_check` = `wikipedia` (123) | `region` (46) | `approximate` (12) | `none` (14, blank coordinates).
  - `wikipedia` = the English Wikipedia URL for the modern place (175 rows). It is left out where the only page would name one candidate of a dispute the chapters don't follow (Dagroian, Locac, Bolor, Coloman, Zardandan), or where there is no fitting page (Greater Hermenia).
- **Points moved to Wikipedia's:**
  - Ucaca → Ukek (51.4208, 45.9625; 12 km)
  - Casem → Kishim District (36.7700, 70.1317; 69 km)
  - Reobarles → Rudbar, Kerman (28.0275, 57.9975; 34 km)
  - Pein → Keriya / Yutian (36.8667, 81.7000; 17 km)
- **Not changed:**
  - Every `id_confidence` value. A coordinate match confirms *where the modern place is*, not *that Polo meant it*.
  - Sarai: the run's point is 1.3 km from ours, and Wikipedia's API has no coordinates for the page.

## Pronunciation, origin and links (for `GLO`)

- **Where it goes.** Pronunciation and name-origin notes go in the per-volume place glossary (`GLO`), one entry per place: book form → modern form → respelling → origin line → Wikipedia link (from the `wikipedia` column). Chapter prose stays clean. A chapter Note links to Wikipedia only where it discusses a disputed identification.
- **Wikipedia as the usage reference.** Wikipedia's article title is the "most used name" reference for the gloss. When Wikipedia and scholarship disagree (Hormuz Island vs the mainland kingdom), the gazetteer follows scholarship and says so in `notes`.
- **Respellings are house suggestions, not sourced facts.** No authority pronounces Yule's spellings. The names run's respellings (e.g. *KAM-ba-luk*, *kas-KAR*, *sah-RYE*) are a draft for `GLO.T2`, to be reviewed by a person. Where a form is Italianate (Ciandu, Giogiu), the glossary may give both an anglicised and an Italian reading as options.
- **Origin lines the run gives that are standard** (keep, with a source when written up):
  - *Pulisanghin* < Persian *pul-i sangīn* 'stone bridge'
  - *Sarai* 'palace, court'
  - *Cambaluc* < *Khanbaliq* 'city of the Khan'
  - *Manzi* < Chinese *Manzi* 'southern barbarians'
  - *Cathay* < Khitan
  - *Kinsay* < *xingzai* 'temporary residence (of the court)'
  - *Zardandan* < Persian 'gold teeth'
  - *Caramoran* < Mongol *Qara Mören* 'black river'
  - *Zayton* < Chinese *Citong*, often read as Arabic *zaytūn* 'olive'
- **Origin lines rejected or needing a source:** Negropont, Caracoron, Ucaca (above), and any marked "—".

## Still open (`GAZ.T6`)

- The 23 `disputed` and 58 `probable` identifications still have no second source. The S-16, S-17 and S-18 deep-research runs, which have per-volume prompts and sources, are the next step. A narrower follow-up prompt can work through Pelliot's *Notes* entry by entry for the Chinese and Sumatran rows.
- 12 `approximate` points need a gazetteer source other than Wikipedia (e.g. GeoNames) or an archaeological report.

## Second pass — the 23 disputed rows (`GAZ-disputed-raw.md`)

**Trust check: better than the first pass, but still thin.** It stopped using "standard" as a source and named what it could not open (most of Pelliot's *Notes*; all of Haw, Vogel, Ptak, Luce and McKinnon at page level). Only two claims carry a post-1950 locator, both from Pelliot snippets that we have not seen: Bolor (*Notes* I p. 108) and Dagroian (*Notes* II p. 17). Its "current preference" is Yule's reading in 19 of 23 rows. It gives two coordinates, both from unnamed "secondary" sources, so neither is used.

**Applied to `gazetteer.csv`:**
- **Malaiur:** point moved from Melaka to Malayu-Jambi (Wikipedia *Jambi (city)*, −1.59, 103.61). Melaka was founded c. 1400, so as a gloss for a 1290s port it is an anachronism, and the run cites Wheatley for Malayu. It stays `disputed`. Checked: the chapter (III-02) does not use Melaka.
- **Bolor:** `disputed` → `probable` (region), on Pelliot's Chitral–Yasin–Gilgit reading. The note marks the locator as a snippet, not seen.
- **All 23 rows:** the candidate list and the run's plotting advice are added to `notes`, tagged "second research pass, 2026-10-22". These are the caption material for `MAP`.
- **Tenduc:** Olon Süme (the Öngüt Christian centre) is added as a candidate with its Wikipedia point. The plotted point stays on the Tümed plain.
- **Not changed:** every other `id_confidence` and every other point.

**What would settle the rest:** page-level reading of Pelliot's *Notes* (the Toyo Bunko scan) and Haw 2006 for the 19 Chinese rows, and Wheatley / Luce for Locac and Bangala. A deep-research tool that cannot open those books will keep returning Yule. Library access, or a person with the volumes, is the next step, not another prompt.

## Third pass — source location (three runs, `GAZ-sources-raw-*.md`)

**Trust check: none of the three runs is usable as a source map.**
- **Perplexity** reached none of the databases and says so. It gives three real locators (Cordier's BOLOR entry, a Locac citation, the Dagroian volume range) and no quotes.
- **Consensus** is a refusal with no data, and the paste was cut off. Saved in full.
- **Gemini** looks complete but fails every check I could run. All 35 CHGIS IDs are wrong: 18 do not exist, and the rest belong to other places. Its quotes are paraphrases, and its coordinates copy or pad ours. Marked "do not cite".

**What I checked myself (Toyo Bunko scan of Pelliot's *Notes*, and the CHGIS gazetteer API, `chgis.hudci.org`):**

| Row | Pelliot entry (printed pp.) | Finding | Gazetteer action |
|---|---|---|---|
| bolor | BELOR 67, pp. 91–92 | Balūr, not "Bolor" (form "devoid of authority"); Mirza Haidar's Baluristan = Chitral, Yasin, Gilgit valleys; Po-lü = Baltistan, Little Po-lü = Gilgit | Note corrected: the p. 108 cited earlier is BUCARA |
| pein | PEM 312, pp. 800–802 | Pelliot: the Uzun-tatïr identification (Stein) is "the only plausible one, and at least probable" | Note updated. Still disputed; point stays at Keriya until Uzun-Tati has a named coordinate |
| tenduc | TENDUC 358, pp. 848–852 | Province = NE corner of the great bend of the Yellow River, Öngüt territory; city probably Tung-shêng (Togtoh) | Note updated. CHGIS has no point for Tiande or Tung-shêng valid in 1290 |
| cuncun | CUNCUN 191, pp. 573–575 | Mountains = Qinling; site north of the range (Fengxiang tract), not at Han-chung | Note updated |
| acbalec-manzi | ACBALEC 4, pp. 7–8 | Aq-balīq = Han-chung (Xingyuan), "little doubt". CHGIS Xingyuan Lu hvd_116022 is 2 km from our point | `id_confidence` disputed → probable; note updated |
| coloman | TOLOMAN 363, pp. 856–858 | Best manuscripts read **Toloman**: T'u-lao-man of the Hsü-chou / Wu-mêng area, NE Yunnan | Note updated; "Toloman" added as alias. Book form left as Coloman (the chapters use it); a naming decision |
| anin | AMU 22, pp. 38–40 | Yule's "Anin" is a corruption of *Annam. Pelliot rejects Lin'an | Note updated; still disputed |
| caugigu | CAUGIGU 128, pp. 232–235 | Name = Chiao-chih-kuo (Tonkin); the described conditions are the Upper Red River, contiguous with Yunnan; Upper Laos was independent | Note updated. Kiang Hung point rests on Yule, not Pelliot; a point decision, not yet made |
| bangala | BANGALA 55, pp. 72–75 | Name certainly Bengal; Pelliot disagrees with Yule and Benedetto on the Pegu reading | Note left as is |
| dagroian | DAGROIAN 204, pp. 613–615 | A crux; between Samudra and Lambri; Battak people | Locator corrected from "II p. 17" (a scan page) to printed pp. 613–615 |
| cheinan, locac, malaiur, cuiju, fungul, linju, tinju, nanghin, vughin, tanpiju, changshan, cuju, unken | not yet read in full | — | none |

**Scan page vs printed page:** the Toyo Bunko scan numbers differ from Pelliot's printed numbers. Volume I: scan = printed + 16. Volume II: scan = printed − 596. Every locator here is printed.

**CHGIS (queried on 1290 seats; the API is public and works):**
- Agrees with our point within a few km: Changshan (28.90, 118.51), Shaoxing Lu (30.00, 120.58), Linqing (36.83, 115.70), Anqing Lu (30.51, 117.03, about 4 km), Xingyuan Lu (about 2 km).
- Differs: Houguan (26.07, 119.32) is about 20 km from our Minhou point.
- No 1290 point for Tiande, Tung-shêng, Cheli, Wumeng, Tongzhou or Xuzhou. Those rows keep their regional or approximate coordinates.

**Open:**
- Read the remaining Pelliot entries (vol. I and II) in full.
- Decide the Caugigu point (Pelliot's Upper Red River vs Yule's Kiang Hung).
- Decide the Coloman / Toloman book form.
- Source Uzun-Tati and Togtoh coordinates from a named archaeological report.
- Library access for Haw 2006, Vogel 2013, Wheatley and Luce: none of the three runs reached them.

## Fourth pass — the "update" text checked against the sources (2026-10-22)

The update's page numbers and several claims didn't match the scan. Corrected:

| Claim in the update | Checked | Result |
|---|---|---|
| Locac, "vol. 2 p. 173" | LOCHAC, entry 274, **pp. 766–770** | Page wrong. Pelliot rejects Ligor, the Malay Peninsula, Trengganu and Lo-ch'a. He keeps Lo-hu (Lavo / Lopburi, lower Menam) as "the only one which deserves to be retained". "Logac" is only a possibility he raises ("almost tempted"). Pulo Condore and the cowrie claim do not appear in the entry. |
| Malaiur, "vol. 2 p. 177" | MALAIUR, entry 278, **pp. 771–773** | Page wrong. Minangkabau kingdom centred on the Jambi river, "practically certain". Melaka is not Pelliot's argument. |
| Cheinan "not retrieved" | CHEYNAM, entry 140, **pp. 242–243** | Retrieved. Name = *Cainam*, "South of the Sea" (Hainan). Yule's An-nan reading rejected. The name covers the whole Gulf of Tonkin with Hainan. |
| Caugigu, Vogel / Haw / "Dai Việt dossier" | none checked | Unverified; not used. |
| Coloman: Yule "preferred" Toloman | COLOMAN/TOLOMAN, entry 363 | Wrong. Pelliot says Yule adopted Coloman against the best manuscripts. |
| Uzun-Tati 37.2515 N, 80.8801 E ("Hedin place-card") | Wikipedia, *List of archaeological sites of the Taklamakan and Lop Desert* | Unsourced. The list gives **37.2809 N, 80.9482 E**. |
| Dandan-Uiliq 37.77444 N, 81.07306 E | Wikipedia *Dandan Oilik* (article's own name) | Sourced under the article's name. |
| Togtoh 40.277431 N, 111.194313 E ("standard GPS") | Wikipedia *Togtoh County* | Unsourced. The county point is **40.2833 N, 111.2 E**. |

Changes applied to `gazetteer.csv`:
- **locac:** point → Lopburi (14.8000, 100.6269, Wikipedia *Lopburi*); `probable`.
- **malaiur:** `probable`; the Pelliot locator is in the notes.
- **cheinan:** modern name → "Hainan and the Gulf of Tonkin"; the point stays at the gulf.
- **pein:** point → Uzun-tati (37.2809, 80.9482), coordinate from Wikipedia's archaeological list, `coord_check` = `approximate`. Still disputed.
- **caugigu:** Pelliot's Upper Red River reading is recorded. The plotted point stays at Kiang Hung until a decision is made.
- **coloman:** Yule-preference correction recorded.

Still open: the Caugigu decision; the Coloman / Toloman book form; the Togtoh point for Tenduc's city (the current row is the province); and Haw / Vogel / Wheatley / Luce, which still aren't reachable.

## Fifth pass — the three open decisions (2026-10-22)

The run was mostly careful: it labels most of what it could not open, and it doesn't recommend. Its claims were checked against the sources I can reach:

| Claim | Check | Result |
|---|---|---|
| CHGIS 安南道防送军千户所 hvd_45611, 1276–1381, point 103.78905, 23.40351 | CHGIS API | Verified. The place is Mengzi county, Yunnan (云南省蒙自县). It is **not on the Upper Red River**, so the run's use of it as "border" evidence for Decision 1 does not hold. |
| CHGIS 1290: 东胜州, 绥远, 归化城, 车里, 丰州, 云内州 — no point | CHGIS API | Verified. None has a point valid in 1290. |
| Yule, Caugigu: "I would identify provisionally … Caugigu with Kiang Hung" | refs/yule-vol2.txt, note 6 to ch. LIX | Verified. Yule's recapitulation also gives Anin = Homi and **Coloman = the country about Wei-ning in Western Kwei-chau**. The run did not report the Coloman identification, which is a real difference from Pelliot. |
| Pelliot, TOLOMAN: YS 10 (1278), 13 (1284), 16 (1291), 121 (1256); Ching-shih ta-tien 1290, 1291, 1293 | Pelliot entry 363 | Verified. |
| Yule adopts Coloman against the manuscripts | Yule note 1 to ch. LVIII | Verified. Yule says he "ventured to make the correction". Our earlier note was right. |
| Pelliot, TENDUC: Tung-shêng "to-day Toĭto" favoured over Sui-yüan | Pelliot entry 358 | Verified. |
| Togtoh County 40°17′N 111°12′E (Wikipedia) | Wikipedia | Verified (40.2833, 111.2). |
| Egami, "Olon-Sume…", *Orient* 30/31 (1994) | Crossref | The article exists (DOI 10.5356/orient1960.30and31.1), but the year is **1995**. |
| Haw 2006 identifies Caugigu with Jiaozhi (quoted from a French secondary source) | not opened | **Unverified.** Dropped from the evidence. |
| Moule & Pelliot 1938 table of contents: "PULISANGHIN TO TOLOMAN" | not opened | Unverified. |
| Latham 1958: "Toloman" (secondary snippet) | not opened | Unverified. |
| J-STAGE Olon-Sume passage on Huhe-khoto / Tokto | not opened | Unverified. |
| "Classiques Garnier, F Camul" | — | Irrelevant search result; ignored. |

**What the evidence supports, after these checks**
- **Caugigu:** the only located identification of the *place* is Pelliot's (Upper Red River). Yule's Kiang Hung is his own provisional reading. No post-Pelliot identification of the place has been verified. Option (b) rests on Pelliot alone, and (c) has no contrary source.
- **Coloman / Toloman:** the best manuscripts and Pelliot support Toloman. Yule adopted Coloman deliberately and also placed it in western Kweichow, not north-east Yunnan. Both Moule & Pelliot and Latham are unverified.
- **Tenduc:** Pelliot's preference for Tung-shêng / Togtoh is verified. Neither CHGIS nor any opened source gives a 1290 point for the three candidate cities. The Olon Süme claim is unverified.

**Gazetteer change applied:** only the Yule notes for caugigu and coloman (locators and the Wei-ning identification). No point or book-form changes, since those decisions are yours.

**Still needed:** Haw 2006 and Vogel 2013 at the relevant pages (paywalled); the Moule & Pelliot apparatus; Latham; and the Egami article itself.
