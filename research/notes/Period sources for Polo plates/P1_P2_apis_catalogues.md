# P1/P2: open APIs, IIIF collections and free PDF catalogues for 1250–1300 period sources

Tested 2026-11-13 from a Linux script environment with curl. Excluded as already used: the Met Open Access API, the Cleveland Open Access API, and *The Legacy of Genghis Khan* (2002).

Confidence labels:
- **OPENED**: I fetched it and confirmed it works.
- **DOC**: found in documentation or search results, not fetched.
- **MEM**: from memory, unverified.

## P1: The 10 best collections not yet used, reachable by script

### Takeaway
Ten collections work by script today:
- **Art Institute of Chicago (AIC):** works only with an `AIC-User-Agent` header. A browser-style User-Agent gets a Cloudflare challenge.
- **V&A API v2**
- **Getty Museum Linked Art / SPARQL**
- **Smithsonian Open Access:** needs a free key, because DEMO_KEY was rate-limited after about 6 calls.
- **Europeana**
- **Yale LUX**
- **Vatican DigiVatLib, BSB/MDZ and e-codices:** IIIF manifests only.
- **Minneapolis (Mia):** Elasticsearch endpoint.

Four of them have real numeric date filters: AIC, V&A, Getty and Europeana. Many big holders blocked script access outright: British Museum, British Library, Gallica, Brooklyn, Chester Beatty, Princeton Art Museum, the Walters and the DAI.

### Cited Findings

**1. Art Institute of Chicago: API + IIIF. OPENED**
- **API root:** `https://api.artic.edu/api/v1/artworks/search`. It returned 403 with a Cloudflare "Just a moment" page when called with a browser-style UA. It returned 200 when called with header `AIC-User-Agent: <name>` and no browser UA — [AIC API](https://api.artic.edu/api/v1/artworks/search?q=yuan)
- **Date filter:** the Elasticsearch range syntax works. Call `query[range][date_start][gte]=1250&query[range][date_start][lte]=1300` with curl `-g`.
  - `q=Yuan` in that window gave 206 hits, e.g. 12476 "Foliate Dish with Crane and Deer…, late 13th century" (public domain = true).
  - `q=Ilkhanid` gave 370 hits, e.g. 92287 "Eight Point Star Tile with a Phoenix, late 13th c."
- **Fields:** `date_start`, `date_end`, `date_display`, `is_public_domain`, `image_id`.
- **Manifest pattern:** `https://api.artic.edu/api/v1/artworks/{id}/manifest.json`. I opened `https://api.artic.edu/api/v1/artworks/50983/manifest.json` (IIIF Presentation 2). That object is Qing, not in-window. I did not open a manifest for an in-window object.
- **Key:** none. **Licence:** CC0 when `is_public_domain=true` (MEM for the exact licence wording).
- **Queries:** `q=Ilkhanid` + range; `q=Yuan dynasty` + range; `q=Kashan lustre` + range.
- **Risk:** the Cloudflare challenge if the header is missing. Always send `AIC-User-Agent`.

**2. V&A Collections API v2. OPENED**
- **Search:** `https://api.vam.ac.uk/v2/objects/search?q=mongol&year_made_from=1250&year_made_to=1300&page_size=5` gave 55 records, e.g. O120597 "Tile" 1275–1325 and O85917 "Bowl" 1260–1350 — [V&A API](https://api.vam.ac.uk/v2/objects/search?q=mongol&year_made_from=1250&year_made_to=1300)
- **Manifest pattern:** `https://iiif.vam.ac.uk/collections/{systemNumber}/manifest.json`. I opened `https://iiif.vam.ac.uk/collections/O120597/manifest.json`, the star tile with phoenix (Ilkhanid) — [manifest](https://iiif.vam.ac.uk/collections/O120597/manifest.json)
- **Date filters:** `year_made_from` and `year_made_to`. Each record also has `_primaryDate` (a string).
- **Key:** none.
- **Licence:** V&A's own terms, free for non-commercial use, not CC0 (MEM; check before commercial print).
- **Queries:** `q=Ilkhanid`, `q=Mamluk`, `q=Venice` or `q=Yuan`, each with year_made_from=1250&year_made_to=1300.
- **Risk:** the licence on a commercial book.

**3. J. Paul Getty Museum: Linked Art + SPARQL + IIIF. OPENED**
- **SPARQL:** `https://data.getty.edu/museum/collection/sparql`. A CIDOC-CRM query filtering `P82a_begin_of_the_begin >= 1250` and `P82b_end_of_the_end <= 1301` returned in-window objects, e.g. the Rothschild Bestiary (Ms. 100) "A Camel", fol. 30, 1250–1260. A label search found "Canon tables from the Zeyt'un Gospels (Ms. 59)", object `fe7e217b-da19-4939-a10a-db34da0a41a5`. That is the Cilician Armenian manuscript illuminated by T'oros Roslin (attribution MEM) — [Getty SPARQL](https://data.getty.edu/museum/collection/sparql)
- **Object JSON:** `https://data.getty.edu/museum/collection/object/{uuid}`.
- **Manifest pattern:** `https://media.getty.edu/iiif/manifest/{2|3}/{uuid}`. I opened `https://media.getty.edu/iiif/manifest/3/966ac161-01b1-45b9-8dd2-f727ff7b8d50` (IIIF v3, the bestiary camel) — [manifest](https://media.getty.edu/iiif/manifest/3/966ac161-01b1-45b9-8dd2-f727ff7b8d50)
- **Key:** none. **Licence:** each object carries a rights-statement node (OPENED). "Open Content" for public-domain images is MEM.
- **Queries:** SPARQL with the date filter; labels containing "Zeyt'un", "Ms. 100" or "Ludwig".
- **Risk:** SPARQL is demanding; the Getty holds little Asian material.

**4. Smithsonian Open Access API (api.si.edu, separate from the blocked asia.si.edu). OPENED, but in-window NMAA records not confirmed**
- **Endpoint:** `https://api.si.edu/openaccess/api/v1.0/search?q=…&api_key=…` returned 200 JSON with DEMO_KEY (`q=yuan dynasty` gave 3,269 rows). Records carry `metadata_usage.access: CC0`. The first hits were Smithsonian Libraries (SIL) books, not Freer objects — [SI API](https://api.si.edu/openaccess/api/v1.0/search?q=yuan+dynasty&api_key=DEMO_KEY)
- **Filtering failed:**
  - `fq=unit_code:FSG` was ignored.
  - `unit_code:FSG AND Yuan` gave 0.
  - `category/art_design/search` gave 0.
  - Then DEMO_KEY returned `OVER_RATE_LIMIT` after about 6 calls.
- **Key:** free api.data.gov key required in practice.
- **Date fields:** `indexedStructured.date` (decades such as "1200s") and `freetext.date` (free text). There is no numeric range.
- **Queries to try with a real key:** `q=Ilkhanid AND unit_code:"FSG"`, `q=Kashan`, `q="Yuan dynasty" AND online_media_type:Images`.
- **Risk:** the right unit-code syntax for Freer|Sackler (NMAA) records was not confirmed; dating is coarse.

**5. Europeana Search + Record API + IIIF. OPENED**
- **Search:** `https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=Venezia&qf=YEAR:[1250 TO 1300]&reusability=open&media=true` returned "Statutum Comunis civitatis Tarvisii", 1263, Public Domain Mark (Veneto New Manuscript Library) — [Europeana API](https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=mongol&rows=3)
- **Manifest pattern:** `https://iiif.europeana.eu/presentation/{dataset}/{localId}/manifest`. I opened it for that record — [manifest](https://iiif.europeana.eu/presentation/2023813/proxy_provider_2023813_Generale_ricerca_AnteprimaManoscritto_html_codiceMan_39569/manifest)
- **Key:** `api2demo` works for tests; a personal key is free (DOC). **Date filter:** `qf=YEAR:[a TO b]`. **Licence filter:** `reusability=open`.
- **Queries:** `Venezia` / `Genova` / `Armenia` / `Byzantine` with YEAR:[1250 TO 1300].
- **Risk:** sparse. The YEAR facet only exists where providers supplied it, so recall is low.

**6. Yale LUX (Linked Art). OPENED for simple search**
- **Search:** `https://lux.collections.yale.edu/api/search/item?q={"text":"yuan"}` returned 21,913 items as Linked Art JSON — [LUX](https://lux.collections.yale.edu/api/search/item?q=%7B%22text%22%3A%22yuan%22%7D)
- **Date query failed:** a query combining `producedDate` with `_comp:"<="` got a CloudFront 403. Either the syntax is wrong or a WAF blocked it; I did not resolve which.
- **Key:** none. Manifest not opened. **Licence:** per-record (MEM: Yale open-access policy for public-domain images).
- **Risk:** WAF on complex queries; the item endpoint mixes objects and digital objects.

**7. Vatican Library DigiVatLib IIIF. OPENED (manifest only)**
- **Manifest pattern:** `https://digi.vatlib.it/iiif/MSS_{shelfmark}/manifest.json`. I opened `https://digi.vatlib.it/iiif/MSS_Vat.lat.3773/manifest.json` — [manifest](https://digi.vatlib.it/iiif/MSS_Vat.lat.3773/manifest.json)
- **Search API / date filter:** none known (MEM). You need shelfmarks from catalogues.
- **Key:** none. **Licence:** restrictive, non-commercial with permission (MEM).
- **Risk:** licence; no date search.

**8. Bayerische Staatsbibliothek / MDZ IIIF. OPENED**
- **Manifest pattern:** `https://api.digitale-sammlungen.de/iiif/presentation/v2/{bsbID}/manifest`. I opened bsb00072456 (a modern book, used only as a pattern test). The manifest carries `navDate`, usable for date screening — [manifest](https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00072456/manifest)
- **Key:** none. **Licence:** many items are CC BY-NC-SA or public domain (MEM).
- **Queries:** Clm/Cod.gall. manuscripts of the 13th c. (shelfmarks via the OPAC).
- **Risk:** no confirmed date-search API.

**9. e-codices (Swiss manuscripts) IIIF. OPENED**
- **Manifest pattern:** `https://www.e-codices.unifr.ch/metadata/iiif/{ms-id}/manifest.json`. I opened `csg-0390`, which is out of window and was used only as a pattern test — [manifest](https://www.e-codices.unifr.ch/metadata/iiif/csg-0390/manifest.json)
- **Key:** none. **Licence:** CC BY-NC (MEM). **Dating:** century metadata in the manifest.
- **Risk:** little Eastern material.

**10. Minneapolis Institute of Art (Mia) search. OPENED**
- **Search:** `https://search.artsmia.org/{query}` is a raw Elasticsearch JSON endpoint. "Yuan dynasty" gave 93 hits, e.g. 45829 "Wine ewer and cover", early 14th century, `rights_type: Public Domain` — [Mia search](https://search.artsmia.org/Yuan%20dynasty)
- **Single object:** `https://search.artsmia.org/id/{id}`.
- **Date field:** `dated` (free text only).
- **Images:** the guessed host `api.artsmia.org/images/...` did not resolve. I found no IIIF and no image pattern.
- **Risk:** free-text dates; no confirmed image endpoint.

**Honourable mentions**
- **Princeton University Library Figgy.** `https://figgy.princeton.edu/catalog.json?q=yuan` gave 1,165 results. The manifest pattern `https://figgy.princeton.edu/concern/scanned_resources/{id}/manifest` worked (opened for f52989dd-…, a modern Chinese book). It is mostly library material — [Figgy](https://figgy.princeton.edu/catalog.json?q=yuan)
- **Rijksmuseum.** The old API `rijksmuseum.nl/api/en/collection` returns 410 Gone. The new `https://data.rijksmuseum.nl/search/collection?description=Mongol` works (Linked Art) but gave 0 Mongol hits. It holds little in-window material.

**Blocked or failed (OPENED: these are the failures I saw)**
- **British Museum:** `britishmuseum.org/collection/api/search` returned a Cloudflare "Just a moment" page (403).
- **British Library:**
  - `iiif.bl.uk`: 403 Forbidden.
  - `bl.digirati.io/iiif/...`: AccessDenied.
  - The guessed host `api.bl.uk`: no response.
- **BnF Gallica:** both the IIIF manifest and SRU returned a Cloudflare "Attention Required" page (403).
- **Brooklyn Museum:** `/api/v2/object/1` returned a Vercel Security Checkpoint (429).
- **Chester Beatty:** `viewer.cbl.ie` showed an Anubis "Making sure you're not a bot" page.
- **Princeton University Art Museum:** artmuseum.princeton.edu returned Cloudflare 403.
- **Walters:**
  - art.thewalters.org returned Cloudflare 403.
  - The guessed `manuscripts.thedigitalwalters.org/iiif/W659/manifest` returned 404.
  - The manuscripts.thedigitalwalters.org home page does load (HTML).
- **Harvard Art Museums:** `api.harvardartmuseums.org/object` returned 401 Unauthorized, so a key is required. The key being free is DOC/MEM; I had no key to test with.
- **Bodleian:**
  - Two guessed manifest UUIDs returned 404.
  - The search page renders results with JavaScript, so I could not extract a real manifest.
  - Manifest pattern `iiif.bodleian.ox.ac.uk/iiif/manifest/{uuid}.json` is DOC only.
- **No response (curl code 000):** LACMA, Philadelphia, SMB API, NPM Taipei openaccess, Morgan, BML Teca, iiif.chesterbeatty, iiif.thewalters. These hostnames were my guesses, so this is not proof the services are down.
- **SMB recherche.smb.museum:** the HTML page loads (200). I found no API.
- **Not tested:** David Collection and Aga Khan Museum. Both home pages loaded, but neither has an API I know of (MEM).

### Inferences
- For 13th-century Ilkhanid and Yuan objects with numeric date filtering, the strongest unused routes are AIC (with the header fix) and the V&A. The Getty is the best route for Cilician Armenian and European manuscript material, via SPARQL.
- For Venice, Genoa and Byzantium, the image-rich holders (BL, BnF, BM) are all bot-blocked here. Europeana is the only scriptable aggregator route, and its recall is poor.

### Gaps
- Smithsonian NMAA (Freer) in-window records not confirmed. Needs a real api.data.gov key and the correct unit-code syntax.
- No in-window manifest opened for AIC, LUX, Vatican, MDZ or e-codices; I opened only pattern-test manifests.
- Licence terms for V&A, Vatican, e-codices, Getty and AIC are from memory. Check each before print use.
- Harvard, NPM Taipei, David Collection and Aga Khan Museum are unverified.

## P2: Free PDF catalogues for gaps G1–G6

### Takeaway
I downloaded and checked 8 free PDFs and listed 2 more by archive.org metadata. Coverage by gap:
- **Weak:** G1–G2 (Mongol tents and arms). Only *When Silk Was Gold* touches them.
- **Weak:** G3 (Yuan court). *The World of Khubilai Khan* (2010), NPM *Age of the Great Khan* (2001) and Cleveland *Chinese Art under the Mongols* (1968) were not reachable as free PDFs.
- **Good:** G4 (Venice/Cilicia/Byzantium), G5 (Red Sea / Java Sea) and G6 (Ilkhanid tiles and metalwork).

No free PDF was found for:
- *Venice and the Islamic World* (2007)
- *Armenia: Art, Religion and Trade in the Middle Ages* (2018)
- *Dschingis Khan und seine Erben* (2005, Hirmer)
- The DAI Karakorum volumes. These are open access per DAI's Zenon catalogue, but publications.dainst.org showed an Anubis bot check to scripts.

metmuseum.org returned 429. `resources.metmuseum.org` returned an Incapsula challenge. The Met catalogues below are archive.org mirrors uploaded by kaplan@archive.org in 2014 into "americana", apparently copies of the Met's free MetPublications PDFs (my inference). Their original PDFs are image-only, but each has an OCR'd `_text.pdf` and `_djvu.txt` alongside.

All downloads went into separate fresh folders under the session scratchpad (`dl_*`).

### Cited Findings

| # | Title, publisher, year | Direct PDF | Pages (pdfinfo) | Text layer (checked) | Gap |
|---|---|---|---|---|---|
| 1 | Burke, K. S., *The Sheikh's House at Quseir al-Qadim: Documenting a Thirteenth-Century Red Sea Port* (OIP 144). Oriental Institute (ISAC), Univ. of Chicago, 2021. ISBN 978-1-61491-056-5. **NEW** | [isac-assets S3 PDF](https://isac-assets.s3.amazonaws.com/isac-publications/oip144.pdf) (landing page: [ISAC](https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/Publications/OIP/oip144.pdf)) | 424 | YES. Born-digital InDesign; about 20k words on pp. 20–60 | G5: Red Sea / Indian Ocean trade, 13th c. |
| 2 | Nersessian, V., *Treasures from the Ark: 1700 Years of Armenian Christian Art*. British Library / J. Paul Getty Museum, 2001. ISBN 0-89236-639-7 | [media.getty.edu PDF](https://media.getty.edu/Text/25f2d39c-015d-589b-ab5b-eaabf0ea40fe.pdf) (via [Getty page](https://www.getty.edu/publications-reports/item/248TQP)) | 244 | YES. ABBYY OCR; about 31k words on pp. 20–60 | G4: Cilician Armenia (Ayas hinterland) |
| 3 | Watt, J. C. Y. & Wardwell, A. E., *When Silk Was Gold: Central Asian and Chinese Textiles*. Metropolitan Museum of Art in cooperation with Cleveland Museum of Art; distributed by Abrams, 1997 | [original](https://archive.org/download/WhenSilkWasGoldCentralAsianandChineseTextiles/WhenSilkWasGoldCentralAsianandChineseTextiles.pdf) / [OCR](https://archive.org/download/WhenSilkWasGoldCentralAsianandChineseTextiles/WhenSilkWasGoldCentralAsianandChineseTextiles_text.pdf) | 250 | Original: NO (0 words). `_text.pdf`: YES (about 19k words, pp. 5–40) | G1–G3, G6: Mongol-era textiles and dress (cloth of gold) |
| 4 | Evans, H. C. (ed.), *Byzantium: Faith and Power (1261–1557)*. Met / Yale UP, 2004 | [archive.org](https://archive.org/download/byzantium-faith-and-power-1261-1557/Byzantium_Faith_and_Power_1261_1557.pdf) | 682 | Original: NO. `_text.pdf` exists (not downloaded) | G4: Palaiologan Byzantium, Genoa/Venice contacts |
| 5 | Buckton, D. (ed.), *The Treasury of San Marco, Venice*. Met / Olivetti, 1984 | [archive.org](https://archive.org/download/TheTreasuryofSanMarcoVenice/TheTreasuryofSanMarcoVenice.pdf) | 355 | Original: NO. `_text.pdf` and `_djvu.txt` exist | G4: Venice |
| 6 | Carboni, S., *Following the Stars: Images of the Zodiac in Islamic Art*. Met, 1997 | [archive.org](https://archive.org/download/FollowingtheStarsImagesoftheZodiacinIslamicArt/FollowingtheStarsImagesoftheZodiacinIslamicArt.pdf) | 50 | Original: NO. `_text.pdf` exists | G6: Ilkhanid/Mamluk metalwork |
| 7 | Carboni, S. & Masuya, T., *Persian Tiles*. Met, 1993 | [archive.org](https://archive.org/download/PersianTiles/PersianTiles.pdf) | 50 | Original: NO. `_text.pdf` exists | G6: Ilkhanid tiles (Takht-i Sulaiman / Kashan; MEM) |
| 8 | Mathers, W. M. & Flecker, M. (eds), *Archaeological Recovery of the Java Sea Wreck*. Pacific Sea Resources, Annapolis MD, 1997 | [archive.org](https://archive.org/download/mathers_flecker_1997_java_sea_wreck/mathers_flecker_1997_java_sea_wreck.pdf) | 204 | YES. Word-generated; about 17k words on pp. 5–40 | G5: Java Sea trade ship |
| 9 | Kossak, S. M. & Singer, J. C., *Sacred Visions: Early Paintings from Central Tibet*. Met, 1998 | [archive.org item](https://archive.org/details/SacredVisionsEarlyPaintingsfromCentralTibet) | 241 (archive imagecount; NOT downloaded) | `_text.pdf` and `_djvu.txt` listed in metadata | G3 (tangential): Mongol/Yuan-period Tibetan painting |
| 10 | Lerner, M., *The Flame and the Lotus: Indian and Southeast Asian Art from the Kronos Collections*. Met, 1984 | [archive.org item](https://archive.org/details/TheFlameandtheLotusIndianandSoutheastAsianArtfromtheKronosCollections) | 193 (archive imagecount; NOT downloaded) | `_text.pdf` and `_djvu.txt` listed in metadata | G5 (tangential): Java/India sculpture |

**Notes on the rows**
- **Row 2, *Treasures from the Ark*:** the Getty path `getty.edu/publications/resources/virtuallibrary/0892366397.pdf` 301-redirects to the HTML item page. The real PDF is on media.getty.edu.
- **Row 4, *Byzantium: Faith and Power*:** this is a community upload (sorindanut, 2021), not the kaplan mirror, so it is more likely to be withdrawn.
- **Row 8, Java Sea Wreck:** this is also a community upload (2020). Its dating is the risk. The authors place the wreck in the 13th c.; later radiocarbon work redated it to the late 12th c. (MEM). It may be pre-window.

**Excluded after checking**
- *Of Palm Wine, Women and War* (Mongol invasion of Java, 1293). It was on archive.org as a 338-page Google-Books-derived PDF. The student uploader claims CC BY-NC-ND, which looks doubtful, and it is a history, not a catalogue — [archive.org](https://archive.org/details/of-palm-wine-women-and-war)

**Searched, no free PDF found**
- *The World of Khubilai Khan* (Met 2010; 360 pp. per Met). Only metmuseum.org pages, which are blocked to scripts — [search](https://www.metmuseum.org/met-publications/the-world-of-khubilai-khan-chinese-art-in-the-yuan-dynasty)
- NPM *Age of the Great Khan* (Taipei 2001) — [HathiTrust record](https://catalog.hathitrust.org/Record/003794733)
- Lee & Ho, *Chinese Art under the Mongols* (Cleveland 1968, viii + 403 pp.). Only a restricted archive.org lending copy — [CiNii](https://ci.nii.ac.jp/ncid/BA1208689X)
- *Dschingis Khan und seine Erben* (Hirmer 2005) — [Freitag review](https://www.freitag.de/autoren/rosemarie-boelts/horde-heisst-gruppe)
- Dumbarton Oaks Byzantine coins vol. 5 (Grierson 1999).

**DAI Karakorum volumes: open access, but a bot check blocks scripts**
- Zenon (DAI's library catalogue) lists *Mongolian-German Karakorum Expedition Vol. 1* (2010, DOI 10.34780/133a-8dr5) as open access — [Zenon](https://zenon.dainst.org/Record/000850527)
- publications.dainst.org/books/dai/catalog/book/2057, 2052 and 2054 all redirected to an Anubis bot check (OPENED). Download those by hand in a browser.

### Inferences
- G5 is now well covered by #1 (dated 13th-c. letters and port finds). G4 is covered by #2, #4 and #5. G6 is covered by #3, #6 and #7.
- G1–G2 (tents and arms) has no free catalogue. The best scriptable substitute is single-object records, for example the Met lamellar helmet radiocarbon-dated 1271–1431 per the Met record cited in search — [Met 25112](https://www.metmuseum.org/art/collection/search/25112). That uses the already-used Met API.
- For G3, the gap stays open unless the user opens the Met Khubilai PDF by hand in a browser.

### Gaps
- No free PDF found for:
  - *Venice and the Islamic World* (2007)
  - *Armenia: Art, Religion and Trade in the Middle Ages* (2018, NEW)
  - *The World of Khubilai Khan* (2010)
  - *Dschingis Khan und seine Erben* (2005)
  - Getty *Armenian Gospels of Gladzor*, which a library record lists as Getty Virtual Library but I did not locate.
- Pandya, Sumatra, Lop, Pamir and Badakhshan: no catalogue found.
- Rows 9–10 were not downloaded, so their page counts are archive.org imagecounts.
- The licence status of the archive.org mirrors is not documented on the items (no licenseurl field). Kaplan uploads look like the Met's own free PDFs (inference, not confirmed).
