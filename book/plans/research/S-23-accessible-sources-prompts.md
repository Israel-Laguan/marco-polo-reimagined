# S-23 — accessible-sources prompts for the gaps still open

Three short external prompts, one per region, so each fits a tool's limits. Run externally; save each output untouched as `results/S-23-acc-A-raw.md`, `-B-raw.md`, `-C-raw.md` with a header line (tool, model, date). They ask only for objects whose images **this repo can fetch directly**, because the last two runs found good records that could not be viewed (Smithsonian and the Met's web pages block automated access; the Walters refuses direct downloads).

What has already worked from this repo: the Met API (`collectionapi.metmuseum.org/public/collection/v1/objects/<id>`, image URLs inside), the Cleveland API (`openaccess-api.clevelandart.org/api/artworks/`, image URLs inside), the Walters zoom viewer in a normal browser, Wikimedia Commons file pages, and PDF downloads from museum sites. What failed: Smithsonian asia.si.edu (Cloudflare check), metmuseum.org pages (429), archive.org items that were withdrawn.

## Shared rules (paste at the top of each prompt)

```text
I am illustrating a three-volume English retelling of Marco Polo's book (events c. 1260–1295). I use period objects only as CONTENT sources (dress, arms, tents, ships, buildings) and describe them in words; I never copy images. Two earlier research passes failed on the same points, so follow these rules exactly.

1. ACCESSIBLE ONLY. List an object only if its image can be fetched by a script without logging in or passing a bot check. For each object give ONE of: (a) the museum's open-access API record URL that returns an image link; (b) a IIIF manifest or image URL; (c) a Wikimedia Commons file page with the licence; (d) a direct PDF or image URL. Say which, and say you opened it. Prefer: Met Open Access, Cleveland Museum of Art Open Access, Art Institute of Chicago API, Rijksmuseum, Europeana, Gallica (IIIF), e-codices, Digital Walters, British Library, Library of Congress, Wikimedia Commons, Internet Archive items that are NOT lending-restricted, Harvard Art Museums, Yale, Getty, National Palace Museum Open Data, ColBase (Japan), Kyushu University and other university repositories.
2. OPENED ONLY. Quote the record's title line and date line exactly as printed, with the accession number or shelfmark exactly as printed. Never reuse a number for two objects. Never invent a URL.
3. DATE. State the museum's own date. Mark each object inside / earlier / later than 1260–1295 and by how many years. "Yuan dynasty (1271–1368)" and "14th century" count as UNDATED. Objects later than 1300 go in a separate "comparanda" table and say what they can and cannot be used for.
4. DESCRIBE only what you can see in the image you opened. If you could not view it, write "not viewed".
5. No Wikipedia, Baidu, blogs, travel or social sites as sources. A lead you cannot open goes under "Leads" with what is missing.
6. A short list of checked objects beats a long unchecked one. "Not found" is a good answer. Do not mark a problem "answered" unless an object passed rules 1–4.

Already have, do not repeat: Met 1992.54, 1999.158, 1973.120.3, 2012.399, 1997.33, 2020.122, 2015.500.1.21, 1993.256, 12.49.4, 66.95.8; Cleveland 1989.50, 1996.297, 1990.2, 1993.140, 1915.524, 1944.480, 1915.704, 1915.106, 1957.501, 1985.61, 1971.125; Walters W.539; Diez Album A fol. 70–72; Edinburgh Or.MS 20; BnF Arabe 5847; Liu Guandao, Khubilai Khan Hunting; the Quanzhou ship; the Mōko Shūrai Ekotoba.
Known wrong, do not offer: Met 1978.412.56; Royal Armouries XXVIC.82; Princeton 1977.58 (the tent model is y1951-34); Ashmolean 1915.15; Walters 54.2766; BL Add MS 36129; Juyong Pass "tent reliefs" (they are Buddhist); Met 11.8.4 (Korean).

OUTPUT: (1) a ledger, one line per problem: passed / partly / not found. (2) One table per problem: # · object · holder · accession or shelfmark · quoted title line · quoted date line · inside/earlier/later (years) · access route (a–d) and the URL you opened · licence · what the image shows (only if viewed) · scenes. (3) Comparanda (later than 1300). (4) Leads. (5) Questions you could not resolve.
```

## Prompt A — Mongol and Yuan world (China, steppe)

```text
[paste the shared rules above]

PROBLEMS — find accessible, dated objects for each:
A1. A ROUND FELT TENT CARRIED ON A WAGON (scenes: a court leaving Shangdu; a Mongol camp; Rubruck describes one 20 ft across). Any image before c. 1350 of a tent on a cart, or of a Mongol tent AND a cart together: Persian and Chinese paintings, album leaves, tomb murals, woodblock prints, ceramics, rock art, Armenian and Georgian miniatures. Check the Edinburgh Jāmiʿ al-tawārīkh (Or.MS 20), the Khalili and Diez leaves in Wikimedia Commons, the Hermitage and Topkapı albums, and the free catalogue PDFs of *The Legacy of Genghis Khan* (Met 2002) and *The World of Khubilai Khan* (Met 2010). Say plainly if none exists.
A2. MONGOL AND YUAN ARMOUR AND KIT, 1250–1300 (scenes: the sack of Baghdad; the battle of Nayan; the battle of Vochan). Helmets, coats (lamellar, scale, brigandine, quilted), shields, sabres, bows, quivers, saddles, stirrups, horse armour. Use the Met, Cleveland, Art Institute of Chicago, Royal Armouries, Hermitage, Khalili and Livrustkammaren open records. Date discipline is the whole task: give the museum's date for each and reject anything later than 1400 unless it is labelled a comparandum. Also the clearest dated painting of armoured Mongols or Persians before 1320 (Diez, Edinburgh, Morgan, Cleveland 1944.480-type leaves).
A3. A YUAN OR LATE SONG HALL AND ITS INTERIOR (scenes: the audience at Kaiping; the White Feast; the Green Mount island). Paintings in ruled-line (jiehua) manner dated or attributed to 1250–1350; the Yongle Gong and Guangsheng Temple murals as free images (Wikimedia Commons or museum sites); the Nelson-Atkins *Assembly of Tejaprabha* (32-91/1) if its record and image are open; excavated tiles and architectural fragments in open collections; any image of a Mongol banquet with its vessels. Free PDFs: the Met *World of Khubilai Khan* chapters on architecture and dress (Steinhardt, Denney) — give the URL and the page range of any chapter you can open.
A4. SHIP RIG AND THE LIFTING RUDDER. Period images of Chinese sea or river craft 1100–1350 showing battened sails, stern rudders, anchors: the *Qingming* scroll leaves, Ma Hezhi's 1170 river-craft drawing (find its holder and number), the Bayon reliefs on Commons, the *Mōko Shūrai Ekotoba* boat scenes on Kyushu University's repository, Japanese and Korean scrolls. The Shinan wreck and the Takashima wrecks: open reports with figures.
A5. THE SONG SURRENDER OF 1276 AND SOUTHERN SONG OFFICIALS' DRESS; THE LUGOU BRIDGE IN THE 13TH CENTURY; YUAN PAPER-MONEY PRINTING. Open images or reports for each (NPM Open Data, Palace Museum, Cleveland, Met, CUHK).
```

## Prompt B — Mediterranean and the Levant

```text
[paste the shared rules above]

PROBLEMS — find accessible, dated objects for each:
B1. VENETIAN AND GENOESE MERCHANTS, WOMEN AND NOTARIES, 1260–1300 (scenes: Marco dictating in a Genoese prison; jewels cut from coats in a Venetian house; the quay at Ayas). Dress and everyday objects, not Gospel scenes. Sources: San Marco atrium and Cappella Zen mosaics by scene (Commons or a scholarly PDF with plates), Venetian and Genoese statute books and notarial registers with images (Antenati, Archivio di Stato, Biblioteca Marciana IIIF), tomb slabs, seals, guild and *mariegola* manuscripts, the Arsenal Bible and other Acre-school manuscripts on Gallica, the catalogue of *I mondi di Marco Polo* (Palazzo Ducale 2024: list the objects it prints dated 1260–1300 with holders), the Cocharelli codex (BL Add MS 27695, c. 1330–40) as a labelled comparandum.
B2. A SCRIBE OR NOTARY AT WORK; A CIVIC ROOM OR PRISON IN GENOA OR VENICE (scene I-1). Any image c. 1250–1320 of a layman writing with a quill, ink-horn and loose quires; a room with furniture; Genoese palace-prison interiors.
B3. SHIPS OF c. 1270: Venetian and Genoese galleys and round ships (lateen sails, side rudders), by object: mosaics, seals, portolan chart decoration, manuscripts. And the harbour of Ayas / Layas: any image of the sea castle or quay (Cilician Armenian leaves, travellers' sketches before 1900 labelled as such).
B4. CILICIAN ARMENIAN CIVIL DRESS AND ARCHITECTURE 1260–1300: T'oros Roslin's other manuscripts (Walters, Matenadaran, Jerusalem St James, BnF, BL) with folios showing secular figures: donors, rulers, merchants, soldiers. Give folio numbers and viewer URLs.
B5. ACRE AND THE CRUSADER LEVANT BEFORE 1291: Acre-school manuscripts (Arsenal Bible, BnF fr. 22495 *Histoire ancienne*, BL Add. MS 15268 *Livre d'Eracles* leaves): dress, arms, a port, a legate. Give shelfmarks and Gallica or BL image links.
```

## Prompt C — Persia, the caravan roads, the Indian Ocean

```text
[paste the shared rules above]

PROBLEMS — find accessible, dated objects for each:
C1. PERSIAN TOWN LIFE AND THE CARAVAN ROADS, 1250–1300 (scenes: a Persian square with domed tombs; a night raid; a lone great tree; the Pamir). Ilkhanid objects in open collections (Cleveland, Met, Freer open data on Wikimedia Commons, Louvre, Hermitage, David Collection, Khalili on Commons, Morgan *Manāfiʿ al-ḥayawān* M.500 leaves with warning: 1297–1300 and heavily repainted): dress, camels and loads, mud-brick villages, tombs, wind-towers, caravanserai fragments. And any pre-1350 image of a bazaar or a caravan.
C2. THE LOP DESERT, TARIM OASES AND THE PAMIR: Yuan and earlier cave murals at Mogao and Yulin as free images with cave numbers; Turfan and Bezeklik fragments in the Berlin, Guimet and British Museum open collections, dated; any image of Bactrian camels with loads before 1350.
C3. BADAKHSHAN: ruby (spinel) mining and highland dress. Open records or scholarly PDFs (not travel sites).
C4. JAVA, SUMATRA AND CHAMPA, 1260–1300 (scenes: junks lifting rudders; a modest camp on a Sumatran shore): East Javanese temple reliefs securely dated to Singhasari or early Majapahit (give temple, date, and the scholar who assigns it); Samudra-Pasai gravestones (Malik al-Salih, d. 1297) as open images; Cham sculpture 1250–1300 in open collections. Say what ships and houses they show.
C5. THE PANDYA COAST, ADAM'S PEAK AND THE PEARL FISHERY (scenes: pilgrims on iron chains; divers and the shark-charmer; corsairs off Malabar): Pandya and late-Chola sculpture and murals; Polonnaruwa and Gampola-period images; Jain palm-leaf manuscripts of western India dated 1250–1300 with folios showing ships or dress (Cleveland 1971.12x are in hand: find others in the LACMA, Met, V&A and British Library open collections); the earliest image of pearl diving and the first careful description of the method, marking how late each is; Mappila and Arab ships in any pre-1350 image.
C6. HORMUZ AND THE GULF: ships of the Gulf c. 1250–1300 beyond BnF Arabe 5847 (al-Hariri copies in St Petersburg, London, Istanbul, Vienna: give shelfmark, folio and an image link); wind-towers (*bād-gīr*) before 1350 in any image or description.
```

## How to use the answers

Take each answer in with one session: open every access link the tool gives, view the images, and draft cues only from what is seen, as in the C23–C38 pass. Do not paste an object into a prompt until it has passed.
