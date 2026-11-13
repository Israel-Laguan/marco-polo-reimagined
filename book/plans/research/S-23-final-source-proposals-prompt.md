# S-23 — final prompt: propose sources for the remaining gaps

Run externally; save the output untouched as `results/S-23-final-raw.md` with a header line (tool, model, date). Unlike the earlier prompts, this one does **not** ask for objects first. It asks the agent to propose **where to look** (collections, catalogues, scholars, free PDFs, APIs), ranked, with how each can be reached, so the next pass in this repo can open them.

```text
I am illustrating a three-volume English retelling of Marco Polo's book (events c. 1260–1295). Plates are painted in period art traditions; I need period CONTENT (dress, arms, tents, ships, buildings) from objects I can look at online. I describe objects in words and never copy them.

WHAT I ALREADY HAVE (do not propose): Met Open Access and Cleveland Open Access (both searched by API for 1250–1300); Walters W.539 (Roslin Gospels, 1262); Smithsonian Armenian Gospels F1956.11 and F1932.18; Met 1992.54 (Yuan donor portraits), 1993.256 (paiza), 12.49.4 (tile), 2012.399, 1997.33, 2020.122, 2015.500.1.21; Cleveland 1915.524 (1266 tile), 1944.480 (c. 1299 Shahnama leaf), 1989.50 and three other cloths of gold, 1971.12x Jain folios; Diez Albums, Edinburgh Or.MS 20, BnF Arabe 5847; Liu Guandao's Khubilai Khan Hunting; the Quanzhou ship report (Green 1997); the Met's free PDF of *The Legacy of Genghis Khan* (2002); San Marco's Sant'Alipio lunette and the Arsenal Bible frontispiece on Commons.

WHAT FAILED (so do not propose it blindly): sites that block scripts (Smithsonian asia.si.edu; metmuseum.org web pages; archive.org items that were withdrawn); Walters direct image links; "Yuan dynasty (1271–1368)" and "14th century" labels (undated for me); Wikipedia, Baidu, blogs and travel sites as sources; anything I cannot open without logging in or passing a bot check.

THE GAPS (nothing usable found yet). For each, propose sources, not just objects:
G1. A Mongol round tent carried whole on a wagon, before c. 1350 (Rubruck describes one 20 ft across).
G2. Mongol and Yuan armour and kit dated 1250–1300: helmets, coats, shields, sabres, bows, saddles, stirrups; and a counterweight trebuchet at Xiangyang (1273).
G3. A Yuan hall or Shangdu/Dadu interior, banquet vessels, court dress of Khubilai's court dated 1260–1295; the Green Mount (Qionghua) island before 1300.
G4. Venetian and Genoese merchants, women, notaries, a civic room or prison, c. 1260–1300; ships of c. 1270 (galleys, round ships) and the harbour of Ayas/Layas.
G5. Ships of the Gulf, India and Southeast Asia c. 1250–1300 (sewn hulls, lifting rudders), Sumatra (Samudra-Pasai) and Java (Singhasari), the Pandya coast, pearl diving, Adam's Peak.
G6. Persian town and caravan life c. 1260–1295; the Lop desert and Pamir; Badakhshan mining.

WHAT I NEED FROM YOU — PROPOSE SOURCES:
For each gap give up to 6 proposed sources, ranked by how likely they are to hold a dated, viewable, in-window image. A source may be: a museum or library collection with an open API or IIIF; a published exhibition or excavation catalogue with a free PDF; a scholarly article or thesis with plates; a digitised manuscript with a stable viewer; a Commons category; a national or university repository; a named scholar whose bibliography is the fastest route (give the work, not just the name). For every proposal state:
 (a) what it is, with the holder and a stable URL you actually opened, or "not opened";
 (b) why it should hold in-window material for THIS gap (name the object type or scene, and the dating basis: inscription, colophon, excavation context, dated by whom);
 (c) how I can reach it by script: open API / IIIF / direct PDF / Commons / viewer-only / blocked / paywalled;
 (d) the best search terms or catalogue fields to use there (in the source's own language where relevant);
 (e) its main risk (late date, repainted, restored, blocked, image not free, a nineteenth-century copy).
Mark confidence: opened and confirmed / found in a catalogue or citation / from memory.

ALSO PROPOSE, across all gaps:
 P1. The 10 museum or library collections with open APIs or IIIF that I have NOT used and that are most likely to hold 1250–1300 Mongol, Yuan, Ilkhanid, Mamluk, Byzantine, Venetian or Indian Ocean material. Give the API root or IIIF manifest pattern.
 P2. The 10 free exhibition or excavation catalogues (PDF) most likely to illustrate these gaps with dated objects, with the download URL, page count, and whether the PDF has a text layer.
 P3. Reenactment, reconstruction or conservation projects that publish their object sources (armour, tents, dress, ships), with the real objects each rests on.
 P4. The scholars and works that a specialist would read first for each gap (name, title, year, where it can be read free).

RULES. Do not invent holders, accession numbers, URLs, folios or dates. If you did not open a page, say so. "I could not find a good source for G_" is an acceptable answer for a gap. Prefer sources whose dating I can check myself. Flag anything published after 2013 as NEW. Keep the answer to the ledger, the per-gap proposals (a table per gap), P1–P4, a short bibliography with BibTeX where it is a publication, and the questions you could not resolve.
```

## How to use the answer

Take it in with one session here: open each proposed source by its stated route, keep the ones that return a dated, viewable, in-window object, view the image, and draft cues only from what is seen, as in C23–C42.
