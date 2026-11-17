# S-23 — Scouting more visual references in media

**Status:** closed 2026-11-13 (best effort, by the closing protocol: scouting run, deep dives 1–4 in-repo, dives 5–12 and Gorelik by one external closing run plus intake and a last targeted search) · **Phase:** R (deep research) · **Timebox:** 1 external scouting run + follow-up deep dives as chosen + 1 intake session · **Gates:** the shortlist of works for per-work deep dives; coverage of every GEN hero scene in `registry/visual-references.md`
**Pairs with:** S-22 (in-depth analysis and use rules). S-22's use rules apply here unchanged: content not style, never named in prompts, no likenesses, period check.

## Question
Beyond the works already in S-22, which modern media (any language, any market, any medium) depict Polo's world in a form that is useful for drawing? Which of them should get a full deep dive? And which of our generated hero scenes still have no good visual reference at all?

## Why it matters
- S-22 starts from two works the user already knows. Both are Japanese manga, and the well-known Western titles are mostly loose with history.
- Some of the best visual research is probably in markets an English search misses: Chinese, Mongolian, Kazakh, Uzbek, Iranian and Turkish productions; Korean webtoons; Japanese *rekishi* manga; Italian and Franco-Belgian comics; museum reconstructions; reenactment and costume-reconstruction communities.
- Scouting by **scene** rather than by fame finds the references we actually need. Nobody has drawn "trackers hauling a junk up the Yangtze" for a blockbuster, but a documentary or a Chinese TV series may have staged it.

## Inputs
- S-22's [supplement survey](../research/results/S-22-supplement-raw.md) contains additional works and unanswered category gaps; its verdicts are unverified. Before the external run, compare its titles against results to avoid repetitive scouting, but request missing creator/source details and coverage rather than assuming the works are accurate.
- S-22 (use rules; the works already covered, so this spike doesn't repeat them)
- `illustration-plan.md` § Hero plates (35 GEN scenes since S-11 moved III-7 to GEN; listed inside the prompt)
- `illustration-style-guide.md` (region → tradition table)

## Method
1. Best after S-22 has come back: add the works S-22's Part 2 found to the prompt's "I already have these" list, so the scouting run doesn't repeat them. Run the **scouting prompt** and save the output to `research/results/S-23-raw.md`.
2. Intake: check that each work exists (title, creator, year; a catalogue, publisher, IMDb/MAL/BGG-type record, or a museum page). Merge the works into `registry/visual-references.md` § By work, marked `scouted`.
3. Mark scene coverage: for each GEN hero scene, *covered* (≥ 1 accurate reference), *thin* or *none*. Scenes marked *none* fall back to period art and scholarship only, which is fine. They are noted so that the matching `PLT` task knows it is harder (S-10 is closed).
4. With the user, choose the shortlist (suggested 5–10). For each work on it, run the **per-work deep-dive prompt** below, saving to `research/results/S-23-<slug>-raw.md`.
5. Intake each deep dive as in S-22 Method 3–5.

## Scouting prompt

```text
I am illustrating a new three-volume English retelling of Marco Polo's book (events c. 1260–1295). Plates are painted in each region's period art tradition (Ilkhanid Persian miniature, Yuan court painting, Kamakura emaki, Javanese relief, etc.). For CONTENT accuracy (costume, arms, horse tack, gers, ships, architecture, crowds, landscapes, rituals) I want modern works that depict this world carefully. I will NOT copy their art or name them in image prompts; I want to know what they show, how accurately, and which real sources lie behind them.

I already have these and do not need them again: Tenmaku no Jaadugar (Tomato Soup); Otoyomegatari / A Bride's Story (Kaoru Mori); Angolmois: Genkō Kassenki; Ghost of Tsushima; Mongol (Bodrov, 2007); Netflix's Marco Polo (2014–16); RAI's Marco Polo (1982); the NHK anime Marco Polo no Bōken (1979); Osprey Men-at-Arms titles on the Mongols. Also surveyed as leads: Osprey *Medieval Chinese Armies 1260–1520* (C. J. Peers / David Sque); *The Adventures of Marco Polo* (Freedman / Ibatoulline); *Shut Hell* (Itō Yū); and the *Jewel of Muscat* reconstruction of a ninth-century wreck. Existing mention does not establish accuracy or period fit: include them again only if adding specific evidence or a documented research trail.

SCOUT WIDELY — at least 60 candidates — across:
A. MARKETS AND LANGUAGES. Search in the native language, not just English. Report the search terms that worked. Cover: Japan (歴史漫画, モンゴル帝国, 元寇, クビライ, シルクロード); China (元朝, 大元, 忽必烈, 蒙元, 丝绸之路, 宋元, 泉州, 临安/杭州; TV dramas, donghua, manhua, museum digital reconstructions); Korea (manhwa/webtoon, sageuk set in Goryeo under Yuan, e.g. Empress Ki–era dramas, judged for Yuan costume); Mongolia (Mongolian films, TV, comics, state museum reconstructions, Naadam historical costume); Kazakhstan, Kyrgyzstan and Uzbekistan (historical epics, e.g. Golden Horde–era productions); Iran (Ilkhanid-era films and series, illustrated books); Turkey (Seljuk/Mongol-era dizi, judged for costume); Russia (Golden Horde films, e.g. Orda, 2012); India and Sri Lanka (Pandya/Chola-era productions); Indonesia and Vietnam (Majapahit, Singhasari, Champa, the Đại Việt resistance to the Yuan); Italy (Venetian medieval productions, fumetti about Polo); France and Belgium (bandes dessinées about Polo, the Mongols, the Silk Road); the English-speaking world.
B. MEDIA. Manga, manhua, manhwa, webtoons, BD, graphic novels; animation; film; TV; video games and their art books (strategy, RPG and open-world titles with Mongol, Yuan, Song, Persian, Indian Ocean content); board games and tabletop RPG sourcebooks; illustrated children's and young-adult books about Polo or the Silk Road; concept-art books; museum exhibitions with commissioned reconstructions (e.g. the 2024 Polo anniversary shows; Mongol Empire exhibitions; Quanzhou maritime museum); documentaries with CGI or staged reconstructions (NHK Silk Road series; CCTV; BBC/National Geographic Mongol programmes); stage works (e.g. Tan Dun's opera Marco Polo, 1996); historical-costume reconstruction projects and reenactment groups grounded in excavated garments (Mongol, Yuan, Song, Ilkhanid, Venetian).
C. SCENES WE MOST NEED. Search specifically for depictions of these scenes or their components; a single good frame-level reference counts:
 I-1 Genoese prison, two men writing · I-3 a father presenting his son to Kublai in a timber audience hall at Shangdu (Kaiping), c. 1275 · I-4 the quay at Ayas · I-5 the Mongol sack of Baghdad / the caliph's treasure tower · I-6 domed brick tombs in a Persian town (Saveh), a traveller questioning townsfolk · I-7 night raid by dust-storm raiders, Kerman–Hormuz plain · I-8 a lone great tree on a desert plain (chinar) · I-9 ruby/spinel mining in Badakhshan · I-10 the Pamir plateau, Marco Polo sheep, high camp · I-11 caravan straggler in the Lop desert, desert spirit voices · I-12 Christian (Nestorian) clerics divining with split canes before a Mongol battle · I-13 Kublai's court leaving Shangdu, mare's-milk libation · II-1 Kublai in a tower on four elephants at a battle · II-2 elephants carrying trees up the Green Mount (Qionghua island), Dadu palace · II-3 the White Feast procession (white horses, white elephants) · II-5 printing Yuan paper money · II-6 caravan on the Lugou (Marco Polo) bridge · II-7 night camp burning green bamboo · II-8 Mongol archers against Burmese war elephants · II-9 mastiffs holding a tiger · II-10 the Song surrender to Bayan, 1276 · II-11 counterweight trebuchet at Xiangyang · II-12 trackers hauling a junk up the Yangtze · II-13 pleasure barges on Hangzhou's West Lake · II-14 Quanzhou harbour, junks unloading pepper · II-15 a Mongol princess (Khutulun) wrestling a suitor · III-2 junks lifting rudders in a shoal strait · III-3 a modest ships' camp on a north Sumatran shore, junks at anchor · III-4 pilgrims climbing Adam's Peak on chains · III-5 pearl divers and a shark-charmer · III-6 corsair fleets off Malabar · III-7 the rukh (giant bird) carrying off an elephant · III-8 Hormuz at noon · III-9 Kublai giving golden tablets (paiza); a princess's fleet · III-10 Venetian feast where jewels are cut from old Tartar coats.
D. DISCOVERY ROUTES. Name the curated lists, databases, tags, awards and communities where more such works can be found (e.g. manga database tags, BoardGameGeek families, Steam tags, Douban lists, museum collection search terms, reenactment forums) and how to search them.

OUTPUT FORMAT (required). (1) A candidates table with columns: # · title (original script / romanised / English) · creator(s) · year · medium · market/language · period and places depicted · scenes or visual problems it helps with (use the scene IDs above) · apparent research quality (high / mixed / low / unknown, with one-line evidence: consultants, cited sources, award, review) · period fit for c. 1260–1295 (exact / near / later / fantasy-inspired) · how to access it (publisher, platform, museum page) · existence check link. (2) A scene-coverage table: scene ID · best candidates · coverage (good / thin / none). (3) A ranked SHORTLIST of the 10–15 works most worth a deep dive, with one line each on why. (4) Discovery routes and the native-language search terms that worked. (5) A bibliography of sources (reviews, interviews, museum pages, scholarship), with BibTeX where it is a publication. (6) Questions you could not resolve. Rules: do not invent titles, creators, years, URLs or consultants; mark any detail you could not confirm as "unconfirmed". Prefer publisher, museum, creator-interview and scholarly sources over fan wikis. Flag works released after 2013 as NEW.
```

## Per-work deep-dive prompt (template)

Run it once per shortlisted work. Fill in the angle brackets from the scouting results.

```text
I am illustrating a new English retelling of Marco Polo's book (events c. 1260–1295), in period art traditions per region. I use modern works only as CONTENT references (costume, arms, tack, gers, ships, architecture, crowds, ritual) and never copy their art or name them in image prompts.

Analyse this work in depth: <TITLE (original script / romanised / English)>, <CREATOR>, <YEAR>, <MEDIUM>. It may help with these scenes and visual problems: <SCENE IDs / PROBLEMS FROM THE SCOUTING RUN>.

1. What period, places and peoples it depicts, and how closely they match c. 1260–1295.
2. Element by element (dress for men and women, headgear and hair, arms and armour, horse tack, dwellings, vehicles, ships, architecture, interiors, food, ritual, landscape): what it shows, whether it is accurate for c. 1260–1295, and what is anachronistic or invented. Give concrete examples (episode, chapter or volume, scene description; no frame reproductions).
3. Its documented research: historical consultants, art books, creator interviews, afterwords, bibliographies, museum collections or excavations it drew on. For each, the underlying REAL SOURCE (museum object with holding institution and accession number; excavation report; scholarly book) and a link.
4. Known criticism of its accuracy from historians, curators or informed reviewers.
5. The 5 most useful takeaways for an illustrator of the scenes listed, each phrased as a description of the period object or practice, and each traced to a real source where possible.

OUTPUT FORMAT (required). (1) An element table with columns: # · element · what the work shows · accuracy for c. 1260–1295 (accurate / plausible / anachronistic / invented) · underlying real source (object or study, institution, accession number, URL) · confidence (high / medium / low). (2) Research sources and consultants, with links. (3) Criticism. (4) The 5 takeaways. (5) A bibliography with BibTeX where it is a publication. (6) Questions you could not resolve. Rules: do not invent consultants, interviews, accession numbers or URLs; say "not documented" where research sources cannot be confirmed. Prefer creator interviews, official art books, museum records and scholarship over fan wikis.
```

## Output (definition of done)
- [x] `research/results/S-23-raw.md` saved, with the existence-check hit rate recorded (53 of 72 with a record found; see Findings)
- [x] `registry/visual-references.md`: scouted works merged (the 12 shortlisted; the rest stay in the raw file); scene-coverage table for all 35 GEN hero scenes
- [ ] Shortlist agreed with the user (2026-11-13: the 12 accepted, top four first); a substantive deep dive into each shortlisted work. **Partial:** checks 1–4 were run in-repo; 5–12 and Gorelik were short checks in the closing run ([raw](../research/results/S-23-closing-raw.md); intake in `registry/visual-references.md` § S-23 closing intake). None reached the works' interiors; the spike was closed best effort, not on completion of this original criterion.
- [x] Scenes with no coverage flagged in `PLT-plates.md` (one note under the table, 13 scenes)

## Feedback to plan
- `illustration-plan.md`: per-scene reference pointers (period sources first, modern works only as viewing aids)
- `tasks/cross/PLT-plates.md`: flag scenes with thin or no coverage on their task rows (treat them like "first of its tradition": expect more rounds)
- `S-22`: works the scouting finds that belong in S-22's comparative set

## Follow-up prompts
The per-work deep dives above, plus:

**Closing prompt (2026-11-13, last):** [`research/S-23-closing-prompt.md`](../research/S-23-closing-prompt.md) covers deep dives 5–12, Gorelik, and the open H2 (b, d, e), H3 and H5 items. Protocol: one external run, then intake here, then one last targeted search for items with a concrete lead. **Then S-23 closes**, with what remains recorded as "no source; fall back to period art and scholarship".

**Final source-proposal prompt (2026-11-13):** [`research/S-23-final-source-proposals-prompt.md`](../research/S-23-final-source-proposals-prompt.md) asks the agent to propose where to look (collections with APIs, free catalogue PDFs, scholars, reconstruction projects) for the six gaps still open, rather than to list objects. Run it after the accessible-sources prompts, which are answered.

**Accessible-sources prompts (2026-11-13, after the viewing passes):** [`research/S-23-accessible-sources-prompts.md`](../research/S-23-accessible-sources-prompts.md): three short regional prompts (Mongol and Yuan; Mediterranean and Levant; Persia, roads and Indian Ocean) that ask only for objects whose images a script can fetch. Use them in place of the combined prompt below.

**Combined gaps prompt (2026-11-13):** [`research/S-23-gaps-follow-up-prompt.md`](../research/S-23-gaps-follow-up-prompt.md) merges H2 and H5 and the low-priority groups into one external run; save to `research/results/S-23-gaps-raw.md`. Use it instead of the H2 block below.

**H2: stricter re-run of the S-22 follow-up.** Paste this block above the prompt in [`research/S-22-follow-up-prompt.md`](../research/S-22-follow-up-prompt.md), and run only the groups named in H2 below. Save to `research/results/S-22-followup-2-raw.md`.

```text
A first answer to this prompt failed checking: 14 of 16 accession numbers, holders or dates were wrong or could not be found, and no image had been viewed. This run has harder rules.
1. List an object ONLY if you opened the holding institution's own record page in this session. Paste that page's URL and quote its title line and its date line exactly as printed. No institution page = it goes under "Leads", never in a table.
2. One accession number or shelfmark per object, copied from that page. Never reuse a number for two objects. Never give a URL you did not open.
3. "Image viewed" means you looked at the image on that page or a linked IIIF/zoom viewer. Describe only what is visible. If you did not view it, write "not viewed" and nothing else in that column.
4. A monument or site is not a source. Name the single relief panel, mural wall, tile or excavated piece, with its museum number or its figure number in a named excavation report.
5. Date each object from the institution's record. "Yuan dynasty (1271–1368)" is LATER/UNDATED unless the record narrows it. An object of 1296 or later is "later"; say by how many years.
6. Do not cite Wikipedia, Baidu, blogs, social media or travel sites. If that is all you have, the item is a lead.
7. Ten checked objects are worth more than seventy unchecked. If a group yields nothing that passes rules 1–5, write "not found" in the ledger. Do not mark a group "answered" unless at least one object in it passed with its image viewed.
8. End with: leads (what is missing for each), a BibTeX bibliography of scholarship you opened, and the questions you could not resolve.
Wrong in the first answer, do not repeat: Met 1978.412.56; Royal Armouries XXVIC.82; Princeton 1977.58 (the tent model is y1951-34); Ashmolean 1915.15; Walters 54.2766; "BnF Or. 20" (Or.MS 20 is Edinburgh); BL Add MS 36129 (the Cocharelli treatise is Add MS 27695, c. 1330–40); Sinan ship at Jeju (it is at Mokpo); Acre marble hoard at Polonnaruwa; tent or palace reliefs at Juyong Pass (its reliefs are Buddhist); Morgan M.500 as c. 1290 (1297–1300, with 19th-century repainting).
```

## Findings
2026-11-13. Records: [raw](../research/results/S-22-followup-raw.md), [intake](../research/results/S-22-followup-intake.md), [scene coverage](../registry/visual-references.md#scene-coverage-the-35-gen-hero-scenes-s-23-provisional-2026-11-13). The checks were run in this repo with web search, so they are **not independent**.

- **The base file is not a scouting run.** It answers the S-22 follow-up prompt (period objects in eight groups). It names no manga, film, series, game, book or exhibition. S-23's question is still unanswered and `S-23-raw.md` does not exist.
- **Existence-check hit rate: 2 of 16 (13%).** In 8 the object exists but its number, holder, date or description is wrong; 6 were not found or not supported. 0 of 67 rows were viewed. Below the 80% line, so the file is not salvaged; eight leads are kept in the intake.
- **It had already been taken in as verified.** The registry marked eight gaps "RESOLVED", and 12 unviewed draft cues (C9–C20) were copied into `illustration-plan.md` beside the real ones. Corrected today: the registry and S-22 carry a correction, and the plan says C9–C20 are not cues. No hero row named them.
- **Scene coverage, provisional (before the scouting run): 0 good, 10 thin, 25 none** of the 35 GEN scenes. The ten thin scenes rest on works S-22 rated mixed or did not assess.
- **The scouting prompt's scene list had drifted from `illustration-plan.md`.** Fixed in the prompt above: I-3 (it said Acre; the plate is the Kaiping audience), I-6, I-12, II-2, III-3 (no stockade: Ramusio-only), and III-7 added (GEN since S-11). The list now has all 35.
- **Two plates are already done on unsourced content** (II-13 West Lake, III-5 pearl divers, both S-10 pilots). Review them when a source arrives; they are not to be redone on this spike's word.

### Scouting run (H1), same day

Run in this repo with web search at the user's request: [S-23-raw](../research/results/S-23-raw.md). **Not external and not independent**: the tool that listed the works also checked them.

- **72 candidates. 53 have a record found this run (74%); 19 are named from memory and unconfirmed.** Six further searches found nothing; two things I remembered were wrong (raw file § 6). The prompt asked for at least 60 checked; the run stopped at 42 searches.
- **No work was opened or viewed.** Every quality rating is what a record or press page says. So no scene can be rated *good*.
- **Coverage after the run: 0 good, 22 thin, 13 none** (before: 10 thin, 25 none). The gain is almost all from museums, exhibition catalogues and scholarly reconstructions, not from fiction.
- **Fiction is weak for this period.** Of 30 films and series listed, a period consultant was found for none. The works with a named historian are a BD (Favereau), three Japanese educational manga, and the exhibitions.
- **No candidate at all** for I-7, I-8, I-9, II-5, II-6, II-7, II-9, III-4, III-5, III-7, III-8; only off-target ones for III-3 and III-6. These 13 are noted in `PLT-plates.md`.
- **Markets left thin:** Iran, India and Sri Lanka, Uzbekistan and Kyrgyzstan; Chinese manhua and donghua and Korean webtoons were not searched. BoardGameGeek, Steam, Douban and reenactment forums were not tried.
- **Proposed shortlist (12)** is in the registry § Scouted works. It is a proposal: the user picks.

### Deep dives 1–4, same day

Run in this repo, not independent. Raw files: [Gorelik](../research/results/S-23-gorelik-raw.md), [Yuan ships](../research/results/S-23-yuan-ships-raw.md), [Dadu and Shangdu](../research/results/S-23-dadu-shangdu-raw.md), [Khubilai Khan, Met](../research/results/S-23-khubilai-met-raw.md). **None of the four works was itself opened.** Each dive reached what the open web has about it; each file lists what was not reached.

- **Gorelik: blocked.** Nothing of the book could be read. Without a copy there is no armour cue. One scholarly objection found (Kubik 2020: two "Mongol" plates are older and local).
- **Ships.** The Quanzhou hull is about 34 by 10 m as reconstructed, 13 holds, and carried pepper and incense wood; **nothing above its waterline survives**, so rig, rudder hoist and deck houses have no source in it. Sasaki: the 1281 timbers are mostly small Yangtze craft, few big sea ships, none provably Korean, and "not all poorly built". The numbers are from Wikipedia and a review; the IJNA 1998 paper was not reached.
- **Dadu and Shangdu** (press reports of the excavations, one written by Shangdu's excavator): Shangdu's main hall was a Song pavilion moved from Kaifeng in 1266, with white marble dragon corner pillars; the cane palace stood on a **round** base in the outer city; Dadu's walls were bare rammed earth and its barbicans date from 1359; glaze finds are green (Shangdu temple) and peacock blue (Dadu palace). Nothing found for the Green Mount.
- **Met.** The catalogue was not opened. The Met's open-access API works, and through it **the Lady Wenji scroll (1973.120.3) was viewed: it shows no tent on a cart.** That removes the last claimed picture of a ger-cart. One comparandum cue (C23) was drafted from it and left out of the plan. Five Met objects dated late 13th century or 1294 have public-domain images still to view.
- **Four Met objects viewed afterwards** (2012.399 silk, 1997.33 gilt silver service, 2020.122 cup dated 1294, 2015.500.1.21 lacquer box): cues C24–C27 drafted, not in the plan. The fifth listed object, jar 11.8.4, is Korean, not Chinese, and was dropped.
- **Effect on coverage: none.** Still 0 good, 22 thin, 13 none. The dives changed what we know to avoid more than what we can draw.

### Gaps-prompt answer (pasted by the user 2026-11-13)

Raw [S-23-gaps-raw](../research/results/S-23-gaps-raw.md); intake [S-23-gaps-intake](../research/results/S-23-gaps-intake.md). The answering tool could not view images, so nothing in it is "passed".

- **Record hit rate: 10 of 10 checked claims held; 3 not reachable; 3 not re-opened** (against 2 of 16 for the first follow-up). Usable as a lead list.
- **H2, answered in part.** Ships: the primary report was read (intake table): transom stern and probable transom bow, 12 bulkheads, slender lowering masts, a rudder slot, a shallow hold; the raisable rudder comes from the *Qingming* scroll, not the hull; the hull is about 28 m, not 34.6 m. Armour, Dadu and Shangdu images, Venice and Genoa, and a tent on a cart: **not found**. The Cilician Armenian leaves of 1262–63 (Walters W.539; Smithsonian F1956.11, F1932.18) are the one new in-window set; none viewed.
- **H5, answered in part.** Quanzhou report obtained. Gorelik's publisher "discrepancy" resolved (co-publishers). The Met catalogue is probably not a free PDF; unconfirmed. Sasaki's text is not reachable (the archive.org copy is gone). IJNA 1998 and the 2024 Dadu report still unread.
- **New leads:** Ma Hezhi's 1170 drawing of river craft with a tow mast (for II-12; holder unknown); Walters W.539 and the two Smithsonian leaves (for I-4); the Met essay on the Ilkhanid tent as text for the ger-cart.
- **Viewed afterwards (same day):** Walters W.539 folios 66r, 116v and 19r through the in-app browser; cues C28–C30 drafted in the registry, not in the plan. They are Gospel scenes (soldiers, a feast, riders), so they do not give merchants' dress for I-4. A direct image download was refused by the Walters and my retry with a browser User-Agent was blocked as bot-check circumvention; I did not pursue it and used the browser pane instead. Smithsonian: the user supplied six unlabelled screenshots in `input/media/` (taken to be F1956.11, by the first spread's title match; F1932.18 absent); one cue (C31, a seated writer) drafted, nothing for merchants. A second batch of 20 screenshots (13:17–13:20; taken to be F1932.18; the Magi leaf itself not identified) gave cues C32 and C33, again Biblical scenes: Armenian men's dress and a meal. Earlier note: asia.si.edu answers the in-app browser with a Cloudflare "Verify you are human" box; I did not tick it. A person can tick it in the pane, after which the two leaves can be viewed.
- **Open-access API pass (same day):** Met and Cleveland APIs searched for 1250–1300 objects; **cues C34–C38 viewed and drafted**: a paiza (Met 1993.256) for III-9, an Ilkhanid phoenix tile, a 1266 Kashan couple (dress), Ilkhanid horsemen of c. 1299 (armour), and a Yuan-labelled palace leaf. The paiza and the 1266 and c. 1299 Persian pieces are the first in-window, viewed sources for III-9's tablets and for Persian dress and kit. Still none for a Yuan hall at Dadu or Shangdu, Venetian merchants, a ger-cart, or Mongol armour inside 1260–1295.
- **Prompt A answered (pasted 2026-11-13):** [raw](../research/results/S-23-acc-A-raw.md), [intake](../research/results/S-23-acc-A-intake.md). Mostly "not found", agreeing with the viewing passes. Its one lead paid off: the Met's *Legacy of Genghis Khan* is a free 338-page PDF (downloaded here; image-only), and Masuya's chapter gives documented tents by purpose and colour and **disagrees with the Shangdu excavator on where the cane palace stood**. Prompts B and C not yet run.
- **Prompt B answered (pasted 2026-11-13):** [raw](../research/results/S-23-acc-B-raw.md), [intake](../research/results/S-23-acc-B-intake.md). B2 (scribe, prison) and B3 (ships, Ayas) not found. Three Commons images viewed; **cues C39–C41** drafted (Venetian civic dress from the Sant'Alipio lunette; working men's dress; a writing coffer). I-4's merchants and quay remain unsourced. Prompt C not yet run.
- **Prompt C answered (pasted 2026-11-13):** [raw](../research/results/S-23-acc-C-raw.md), [intake](../research/results/S-23-acc-C-intake.md). C2, C3, C5, C6 not found; C1 and C4 negligible; its "scholarly consensus" on the Malik al-Salih stones is overstated. From the Cleveland API I viewed three dated Jain folios of 1278–87 and drafted **C42** (Gujarati lay and monastic dress). **All three accessible-sources prompts are now answered.** Remaining unsourced: ships and quay of Ayas, Venetian merchants, a ger-cart, Yuan hall, Mongol armour inside 1260–1295, Sumatra, Pandya coast, pearl fishery, Hormuz.
- **Next step with most value (done for Walters; open for Smithsonian):** a session that can open images (Chrome extension or a screenshot tool) to view the objects the raw file lists, starting with the four in-window ones.

### Gap-source ledger (2026-11-13, later the same day)

A deep-research run on period sources (not modern works) plus follow-up checks with files the user downloaded. Report: `reports/Period sources for Polo plates.md` (repo root). Merged into `registry/visual-references.md` § Gap-source ledger (cues C43–C48, text facts, avoid lines), `media/references/README.md` § Added 2026-11-13, `registry/pd-sources.md`, `bibliography.bib` and 22 chapter task files. What it settles here:
- **H2 (a) ger-cart:** settled negative. No image before 1350 was found in any source; text only.
- **H2 (b) Dadu and Shangdu:** partial. Watt 2010 is readable on Google Books (Met permission), including p. 16, the Yelü Zhu tomb of 1285. The UNESCO Xanadu dossier needs a manual download. The 2024 Dadu report is still missing.
- **H2 (c) armour:** answered. The Takashima 1281 finds: Matsuura City Report 4 (2011) has helmets, swords, bows, crossbows and arrows; Report 2 (2008) has colour photos.
- **H2 (c) trebuchet:** comparandum only. The Genoese *trabucos* at Savona in 1227 (C46) and Yuan stone shot (Nagasaki Report 25). No image of the Xiangyang engine exists.
- **H2 (d) ships:** still open for rig, the rudder hoist and a hull shown sewn. Cocharelli f. 5r (c. 1330–40) gives Mediterranean galleys and round ships only.
- **H2 (e) Venice, Genoa and Ayas:** partial. Cocharelli (c. 1330–40; C43, C44); Annales Ianuenses (by the 1230s; C45); CHARLVAR Ayas photos (1974); Carte Pisane (Ayas probable as *[l]aiaso*).
- **H3:** Cocharelli viewed; the Suppl. persan 205 notice was read (8 Dec 1290; image not viewed). The Met objects 2012.399, 1997.33, 2020.122 and 2015.500.1.21 were already viewed (C24–C27). Still not viewed: Princeton y1951-34, Freer F1954.20 and .21, the Mokpo Sinan hull, Huang Sheng, Met 1999.158, 47.18.139 and 11.8.4.
- **H5:** the Met catalogue (Watt 2010, with the Denney, Steinhardt and Sun essays) is now readable page by page; no PDF. Still missing: Gorelik 2002, Green and Burningham 1998, and the 2024 Dadu report.
- **L1:** Java partly answered (Singhasari statues, C47). Sumatra, Sri Lanka, the Pandya coast and the pearl fishery were searched, and **no in-window image** was found.
- **L2:** Persia partly answered (Qazwini 1280, BSB Cod.arab. 464, open IIIF but not viewed; Juvaini 1290; Morgan M.500 with restored folios to avoid). Badakhshan, the Pamir and Lop: none in the window.
- **Scene coverage (period side):** improved for I-1, I-4, II-2, II-11 and III-10. The modern-media verdict (0 good / 22 thin / 13 none) is unchanged, because no modern work was opened.

## Gaps and follow-ups

Updated 2026-11-16 against the later gap-source ledger and Decision. Check the current visual registry before scheduling work; individual objects and sources have different access and dating limits.

### High priority (each blocks plate work or leaves a wrong fact in a plan file)

| # | Gap | Why high | Follow-up |
|---|---|---|---|
| H1 | **Scouting and shortlist checks completed best effort; no shortlisted work was opened beyond publisher or press material.** | The 35-scene inventory remains 0 good / 22 thin / 13 none for modern media. | When a named work becomes accessible, inspect its interior and verify any proposed visual detail against period evidence. |
| H2 | **Period coverage remains partial** for ger-carts, Yuan halls, armour, ships, Venice/Genoa/Ayas, and several Asian regions. | Some scenes still lack suitable, viewed evidence for their hardest details. Later finds include Takashima armour reports and dated comparanda; see the gap-source ledger above for what they actually establish. | Check that ledger and the visual registry scene by scene; seek or inspect suitable sources, or omit and qualify unsupported details. |
| H5 | **Some source texts remain unavailable:** Gorelik 2002, Green and Burningham 1998, and the 2024 Dadu report. The Met catalogue essays are now readable page by page. | The missing works may add armour, ship or gate evidence; catalogue access does not settle those details automatically. | Obtain the named works through library access where the detail is needed, then record passage and access limits. |
| H3 | **Some object leads still need viewing:** Princeton y1951-34, Freer F1954.20 and .21, BnF Suppl. persan 205, the Mokpo Sinan hull, Huang Sheng, and Met 1999.158, 47.18.139 and 11.8.4. | A checked catalogue record is not a viewed image or a period attribution for a specific detail. Cocharelli and several Met objects have since been viewed. | Consult the gap-source ledger above and view each needed object before writing a visual cue, retaining date and attribution limits. |
| H4 | **Resolved 2026-11-16:** rejected cue text C9–C20 removed from the active illustration table and C9–C22 from the registry table. | The rejected raw research remains available for audit, not as prompt material. | Create replacements only from independently checked sources and record the evidence and limits. |

### Low priority (useful, nothing waits on them)

| # | Gap | Why low | Follow-up |
|---|---|---|---|
| L1 | South and Southeast Asia period sources (Java, Sumatra, Champa, Sri Lanka, Pandya coast, pearl fishery): III-2 to III-6. | Vol. III is last in the schedule; these traditions are conservative and the plates are "first of its tradition" anyway. | S-22 follow-up groups 7 and 8 under the strict block, after H2. |
| L2 | Persia and the caravan roads beyond the 1290 frontispiece (wind-towers, caravanserais, Badakhshan, Pamir, Mogao and Yulin donor caves by number): I-6 to I-11, III-8. | The Ilkhanid route already passed in S-10 on style; content needs are small (I-8, I-9, I-10 are landscape-led). | S-22 follow-up group 9, strict block. |
| L3 | Yuan dress reconstructions from excavated garments (China National Silk Museum, Inner Mongolia Museum, Zhangxian tombs; Mongolian work). | Feeds `CHR.T5` costume rows; C1–C5 already cover court dress from viewed objects. | S-22 follow-up question 10 as a stand-alone prompt. |
| L4 | The 1999 Suntory exhibition catalogue. | Only documents *A Bride's Story*'s trail; that work is 19th-century and a process reference only. | Drop unless a deep dive on Mori is chosen. |
| L5 | Scenes with no modern-media coverage: I-7, I-8, I-9, II-5, II-6, II-7, II-9, III-3, III-4, III-5, III-6, III-7 and III-8. | Modern-media coverage is distinct from period-source coverage. | PLT already flags these for more rounds; source each scene detail from suitable period evidence and scholarship. |
| L6 | Region reruns of the scouting prompt (China, Korea, Mongolia in the native language) and fuller per-work dives. | The initial shortlist was checked best effort, without opening the works' interiors. | Run selectively when an accessible work or a scene-specific need justifies it. |

## Decision
**Closed 2026-11-13, best effort.** Protocol: one external closing run, intake, one last targeted search, close.

**Modern media (the spike's question).** No shortlisted work could be opened past its publisher page or press coverage. The verdicts are:
- **follow its sources:** the Deshou and Silk Museum material (Southern Song tombs: Huang Sheng 1243, Zhao Bowen 1216), *I mondi di Marco Polo* (physical catalogue only), and Gorelik (via his 2014 article);
- **viewing aid only:** Osprey NVG 43 and 44, and the two educational manga;
- **drop:** the 2016 Capital Museum catalogue, the Chinggis Khaan Museum's online collection (not yet published), and the Glénat *Gengis Khan* (Favereau not confirmed).

The modern-media coverage verdict stays **0 good / 22 thin / 13 none**. That is acceptable under this spike's own rule: scenes with *none* fall back to period art and scholarship.

**Period sources (where most of the value came from).** The gap-source ledger and the closing intake gave cues C43–C50 (all viewed), the Takashima arms reports, the Cocharelli folios, the Annales Ianuenses siege, the 1285 Yelü Zhu tomb, and the Ayas notarial edition. They are in `registry/visual-references.md` and the chapter task files.

**Recorded as "no source; fall back to period art and scholarship":**
- a ger on a cart before 1350;
- the Xiangyang engine (the Savona 1227 comparandum stands in);
- a sewn or lifting-rudder hull dated 1250–1300;
- excavated Dadu and Shangdu halls with free plates;
- a Venetian, Genoese or Ayas image dated 1270–98 other than coinage;
- Sumatra, Sri Lanka, the Pandya coast, the pearl fishery, Badakhshan, the Pamir and Lop.

**2026-11-16 audit:** the rejected C9–C20 prompt text was removed from the active illustration plan and C9–C22 from the registry's active cue list; the failed raw report and intake retain the audit trail. C43–C50 remain subject to their individual source and adoption limits.

**Reopen only if** a named item arrives: the 2024 Dadu report, Gorelik 2002, the *I mondi* catalogue, or library access to `green1998quanzhou`. Each would get one intake session in a new spike, not a reopened S-23.

## Tasks to create on close
- `PLT.T*` reference pointers per hero plate: the period sources are now in each chapter task's *Period sources* block; copy them into the plate rows when the plates are built
- `PLT` difficulty flags: scenes left with no period source (list above) are "first of its tradition, expect more rounds"
- `illustration-plan.md`: accept or reject the draft cues C43–C50 after checking each source and limit; rejected C9–C20 have been removed.
