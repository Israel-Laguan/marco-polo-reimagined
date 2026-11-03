# S-23 — Scouting more visual references in media

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external scouting run + follow-up deep dives as chosen + 1 intake session · **Gates:** the shortlist of works for per-work deep dives; coverage of every GEN hero scene in `registry/visual-references.md`
**Pairs with:** S-22 (in-depth analysis and use rules). S-22's use rules apply here unchanged: content not style, never named in prompts, no likenesses, period check.

## Question
Beyond the works already in S-22, which modern media (any language, any market, any medium) depict Polo's world in a form that is useful for drawing? Which of them should get a full deep dive? And which of our generated hero scenes still have no good visual reference at all?

## Why it matters
- S-22 starts from two works the user already knows. Both are Japanese manga, and the well-known Western titles are mostly loose with history.
- Some of the best visual research is probably in markets an English search misses: Chinese, Mongolian, Kazakh, Uzbek, Iranian and Turkish productions; Korean webtoons; Japanese *rekishi* manga; Italian and Franco-Belgian comics; museum reconstructions; reenactment and costume-reconstruction communities.
- Scouting by **scene** rather than by fame finds the references we actually need. Nobody has drawn "trackers hauling a junk up the Yangtze" for a blockbuster, but a documentary or a Chinese TV series may have staged it.

## Inputs
- S-22 (use rules; the works already covered, so this spike doesn't repeat them)
- `illustration-plan.md` § Hero plates (34 GEN scenes; listed inside the prompt)
- `illustration-style-guide.md` (region → tradition table)

## Method
1. Best after S-22 has come back: add the works S-22's Part 2 found to the prompt's "I already have these" list, so the scouting run doesn't repeat them. Run the **scouting prompt** and save the output to `research/results/S-23-raw.md`.
2. Intake: check that each work exists (title, creator, year; a catalogue, publisher, IMDb/MAL/BGG-type record, or a museum page). Merge the works into `registry/visual-references.md` § By work, marked `scouted`.
3. Mark scene coverage: for each GEN hero scene, *covered* (≥ 1 accurate reference), *thin* or *none*. Scenes marked *none* fall back to period art and scholarship only, which is fine. They are noted so that S-10 knows they are harder.
4. With the user, choose the shortlist (suggested 5–10). For each work on it, run the **per-work deep-dive prompt** below, saving to `research/results/S-23-<slug>-raw.md`.
5. Intake each deep dive as in S-22 Method 3–5.

## Scouting prompt

```text
I am illustrating a new three-volume English retelling of Marco Polo's book (events c. 1260–1295). Plates are painted in each region's period art tradition (Ilkhanid Persian miniature, Yuan court painting, Kamakura emaki, Javanese relief, etc.). For CONTENT accuracy (costume, arms, horse tack, gers, ships, architecture, crowds, landscapes, rituals) I want modern works that depict this world carefully. I will NOT copy their art or name them in image prompts; I want to know what they show, how accurately, and which real sources lie behind them.

I already have these and do not need them again: Tenmaku no Jaadugar (Tomato Soup); Otoyomegatari / A Bride's Story (Kaoru Mori); Angolmois: Genkō Kassenki; Ghost of Tsushima; Mongol (Bodrov, 2007); Netflix's Marco Polo (2014–16); RAI's Marco Polo (1982); the NHK anime Marco Polo no Bōken (1979); Osprey Men-at-Arms titles on the Mongols.

SCOUT WIDELY — at least 60 candidates — across:
A. MARKETS AND LANGUAGES. Search in the native language, not just English. Report the search terms that worked. Cover: Japan (歴史漫画, モンゴル帝国, 元寇, クビライ, シルクロード); China (元朝, 大元, 忽必烈, 蒙元, 丝绸之路, 宋元, 泉州, 临安/杭州; TV dramas, donghua, manhua, museum digital reconstructions); Korea (manhwa/webtoon, sageuk set in Goryeo under Yuan, e.g. Empress Ki–era dramas, judged for Yuan costume); Mongolia (Mongolian films, TV, comics, state museum reconstructions, Naadam historical costume); Kazakhstan, Kyrgyzstan and Uzbekistan (historical epics, e.g. Golden Horde–era productions); Iran (Ilkhanid-era films and series, illustrated books); Turkey (Seljuk/Mongol-era dizi, judged for costume); Russia (Golden Horde films, e.g. Orda, 2012); India and Sri Lanka (Pandya/Chola-era productions); Indonesia and Vietnam (Majapahit, Singhasari, Champa, the Đại Việt resistance to the Yuan); Italy (Venetian medieval productions, fumetti about Polo); France and Belgium (bandes dessinées about Polo, the Mongols, the Silk Road); the English-speaking world.
B. MEDIA. Manga, manhua, manhwa, webtoons, BD, graphic novels; animation; film; TV; video games and their art books (strategy, RPG and open-world titles with Mongol, Yuan, Song, Persian, Indian Ocean content); board games and tabletop RPG sourcebooks; illustrated children's and young-adult books about Polo or the Silk Road; concept-art books; museum exhibitions with commissioned reconstructions (e.g. the 2024 Polo anniversary shows; Mongol Empire exhibitions; Quanzhou maritime museum); documentaries with CGI or staged reconstructions (NHK Silk Road series; CCTV; BBC/National Geographic Mongol programmes); stage works (e.g. Tan Dun's opera Marco Polo, 1996); historical-costume reconstruction projects and reenactment groups grounded in excavated garments (Mongol, Yuan, Song, Ilkhanid, Venetian).
C. SCENES WE MOST NEED. Search specifically for depictions of these scenes or their components; a single good frame-level reference counts:
 I-1 Genoese prison, two men writing · I-3 Acre and the papal legate · I-4 the quay at Ayas · I-5 the Mongol sack of Baghdad / the caliph's treasure tower · I-6 Persian town square, Saveh · I-7 night raid by dust-storm raiders, Kerman–Hormuz plain · I-8 a lone great tree on a desert plain (chinar) · I-9 ruby/spinel mining in Badakhshan · I-10 the Pamir plateau, Marco Polo sheep, high camp · I-11 caravan straggler in the Lop desert, desert spirit voices · I-12 Mongol cane/scapulimancy divination before battle · I-13 Kublai's court leaving Shangdu, mare's-milk libation · II-1 Kublai in a tower on four elephants at a battle · II-2 Dadu palace and the Green Mount (Qionghua island) · II-3 the White Feast procession (white horses, white elephants) · II-5 printing Yuan paper money · II-6 caravan on the Lugou (Marco Polo) bridge · II-7 night camp burning green bamboo · II-8 Mongol archers against Burmese war elephants · II-9 mastiffs holding a tiger · II-10 the Song surrender to Bayan, 1276 · II-11 counterweight trebuchet at Xiangyang · II-12 trackers hauling a junk up the Yangtze · II-13 pleasure barges on Hangzhou's West Lake · II-14 Quanzhou harbour, junks unloading pepper · II-15 a Mongol princess (Khutulun) wrestling a suitor · III-2 junks lifting rudders in a shoal strait · III-3 a stockaded camp on a Sumatran shore · III-4 pilgrims climbing Adam's Peak on chains · III-5 pearl divers and a shark-charmer · III-6 corsair fleets off Malabar · III-8 Hormuz at noon · III-9 Kublai giving golden tablets (paiza); a princess's fleet · III-10 Venetian feast where jewels are cut from old Tartar coats.
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
- [ ] `research/results/S-23-raw.md` saved, with the existence-check hit rate recorded
- [ ] `registry/visual-references.md`: scouted works merged; scene-coverage table for all 34 GEN hero scenes
- [ ] Shortlist agreed with the user; a deep dive run and taken in for each shortlisted work
- [ ] Scenes with no coverage flagged to S-10

## Feedback to plan
- `illustration-plan.md`: per-scene reference pointers (period sources first, modern works only as viewing aids)
- `S-10`: list of scenes with thin or no coverage (pilot candidates for testing difficulty)
- `S-22`: works the scouting finds that belong in S-22's comparative set

## Follow-up prompts
_(the per-work deep dives above; plus any region- or scene-specific scouting reruns)_

## Findings
_(fill while working)_

## Decision
_(fill when closing: the shortlist, and the coverage verdict)_

## Tasks to create on close
- `PLT.T*` reference pointers per hero plate; S-10 difficulty notes
