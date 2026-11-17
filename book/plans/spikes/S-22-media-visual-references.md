# S-22 — Visual references from modern media (manga, anime, film, TV, games, illustration)

**Status:** closed 2026-11-13 (best effort; follow-up prompt available) · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** the `[PERIOD]` cues in every plate prompt (`illustration-plan.md`); S-05 visual character cards (costume, hair, headgear); the review checklist in `illustration-style-guide.md` (period errors; S-10 ✓ closed); `PLT` secondaries

## Question
Which modern works of fiction and reconstruction depict Polo's world (the Mongol steppe, Ilkhanid Persia, Yuan and Song China, the Silk Road oases, the 1274/1281 invasions of Japan, the Indian Ocean, Venice) carefully enough to be useful references for our plates? For each one: what does it show well, what does it get wrong for c. 1270–1295, and which museum objects, excavations, ethnography or scholarship did its creators base it on?

## Why it matters
- Our plates use period art traditions (the style guide's region → tradition table). But a generator still needs concrete **content**: how a *boqta* headdress sits, how a ger-cart is yoked, what a keshig guard carries, how a junk's sails are rigged, what a Tabriz bazaar looks like.
- Period paintings often don't show these from the angle a scene needs. Well-researched modern works like *Jaadugar* and *A Bride's Story* have already solved many of them visually, and they cite or credit their sources.
- The real value is the **trail back to sources**: a manga's afterword bibliography or an art-book interview leads us to museum objects we can cite and describe in a prompt.
- These works are also a trap. *A Bride's Story* is set in the 19th century, and much Mongol-era fiction mixes centuries. Each work therefore needs an accuracy verdict against our period.

## Use rules (proposed; adopt into `illustration-style-guide.md` § Rules on close)
1. **Content, not style.** A modern work may inform *what* is depicted (objects, dress, architecture, gear, staging). The plate is still drawn in the style its scene's period tradition sets.
2. **Never in a prompt.** No modern title, artist or character name goes into a generation prompt, and no frame or page is used as an image input. Prompts describe the object in words, ideally citing the museum source found here.
3. **No character likenesses.** Recurring figures (Marco, Kublai, Chabi, Cocachin) come from S-05's cards and period portraits, not from an actor's or manga character's look.
4. **Period check.** A detail taken from a work later than our period (e.g. 19th-century Central Asian dress in *A Bride's Story*) needs a period source of its own before it is used.
5. **Nothing is reproduced.** Frames, panels and stills stay out of the book. Only our generated plates or public-domain art appear, so no permissions are needed.

## Inputs
- `illustration-style-guide.md` (region → tradition table; rule 7, people and dress)
- `illustration-plan.md` (hero and secondary scene list; per-scene accuracy notes)
- `tasks/cross/CHR-characters.md`, `tasks/cross/PLT-plates.md`
- Seed works named by the user: *Tenmaku no Jaadugar* (天幕のジャードゥーガル; *Jaadugar: A Witch in Mongolia* / *A Witch's Life in Mongol*), Tomato Soup; *Otoyomegatari* (乙嫁語り; *A Bride's Story*), Kaoru Mori

## Method
1. Run the prompt and save the output to `research/results/S-22-raw.md`.
2. Intake: check that each work exists (title, creator, year) and that each named source is real, e.g. a museum object with an accession number or a cited excavation. The creators' research claims (interviews, afterwords) count as leads until the underlying object or study is found.
3. Write `registry/visual-references.md` in two parts:
   - **By region and chapter:** element → best period source (museum object or scholarship) → modern works that visualise it, as viewing aids only → period caveat.
   - **By work:** title variants, creator, year, medium, period setting, accuracy verdict, what to look at, what to ignore, where the creator got it.
4. Turn the strongest entries into `[PERIOD]` cue lines for the scene entries in `illustration-plan.md`, worded from the period sources and not from the modern work.
5. Pass the costume entries to S-05 (character cards).

## Deep research prompt

```text
I am illustrating a new three-volume English retelling of Marco Polo's book (events c. 1260–1295). The plates are painted in the period art tradition of each region (Ilkhanid Persian miniature, Yuan court painting, Kamakura emaki, etc.). For CONTENT accuracy — costume, headgear, hair, arms and armour, horse tack, gers and ger-carts, caravans, ships, architecture, interiors, food, feasts, hunting with eagles, falcons and cheetahs, crowds, landscapes — I want to learn from modern works of fiction and reconstruction that depict this world carefully. I will NOT copy their art or put their names into image prompts. I want to know what they show, how accurate it is for the late 13th century, and above all which real sources (museum objects with accession numbers, excavations, ethnographic studies, scholarly books) their creators used, so I can go to those sources directly.

PART 1 — Analyse these two works in depth:
a. Tenmaku no Jaadugar (天幕のジャードゥーガル; English: Jaadugar: A Witch in Mongolia / A Witch's Life in Mongol; also romanised Tenmaku no Jadugar / Jadoogar), manga by Tomato Soup (and its anime adaptation, if one exists). Period depicted (Chinggis to Ögedei/Güyük era, Töregene, Fatima), which settings and peoples appear, and the creator's stated sources (afterwords, interviews, bibliography pages).
b. Otoyomegatari (乙嫁語り; A Bride's Story), manga by Kaoru Mori, set in 19th-century Central Asia (Caspian region, Turkic and Persian peoples, the Great Game era). What it depicts in detail (textiles and embroidery, felt-making, yurts, house interiors, eagle hunting, horse culture, bread and cooking, wedding customs, Persian urban life); which of those elements are fairly stable from the 13th to the 19th century and which are clearly later (firearms, Russian influence, specific garment cuts, ikat fashions); and Kaoru Mori's documented research sources (interviews, art books, travel; collections she consulted).

PART 2 — Find and evaluate 20–40 more works across media that depict Polo's world. For each, give: title (original script + romanisation + English title variants), creator(s), year(s), medium, period and places depicted, a historical-accuracy verdict for c. 1260–1295 (high / mixed / low, with specific examples of what is right and what is anachronistic), the visual elements most worth studying, the book sections they map to (IDs below), and any documented research sources, consultants or official art books. Cover at least:
- Manga, manhua, webtoons, bandes dessinées and graphic novels (e.g. Angolmois: Genkō Kassenki on the 1274 invasion of Tsushima; Franco-Belgian albums about Marco Polo or Genghis Khan; Chinese manhua set in the Song–Yuan transition; others you find).
- Anime and animation (e.g. the 1979 NHK anime Marco Polo no Bōken; others).
- Film and TV (e.g. Mongol, 2007, Sergei Bodrov; Netflix's Marco Polo, 2014–16, and its costume designer's sources; RAI's Marco Polo, 1982; Japanese, Chinese, Korean, Mongolian and Kazakh historical films and dramas set in the Mongol/Yuan era, e.g. Kublai Khan dramas and Jin Yong adaptations set in the Song–Mongol wars, judged for costume quality; Turkish and Iranian productions on the Ilkhanate or Mongol Persia).
- Video and board games (e.g. Ghost of Tsushima, 2020, its research on the 1274 invasion and Mongol equipment; Age of Empires II/IV Mongol and Chinese content; Crusader Kings III; The Voyages of Marco Polo board game art; others).
- Historical-reconstruction illustration: Osprey Publishing titles on Mongol, Yuan, Song, Ilkhanid, Mamluk, Japanese Kamakura and Venetian forces (illustrators such as Angus McBride, Wayne Reynolds, Peter Dennis, others — verify which titles exist); museum-commissioned reconstructions; costume-reconstruction work (Mongolian historical costume reconstructions; Song/Yuan hanfu reconstruction research grounded in excavated garments); documentaries with strong visual reconstruction (e.g. NHK's The Silk Road series).
- Illustrated books about Marco Polo for general or young readers that are known for careful research.

PART 3 — For each of these visual problems, name the best PERIOD source (museum object, painting, excavation) and the modern work(s) that visualise it best:
1) Mongol court dress for men and women c. 1280 (jisün robes, boqta headdress, hairstyles); 2) Mongol cavalry kit (lamellar armour, bows, quivers, saddles, stirrups); 3) ger and ger-cart (Rubruck's carts); 4) Yuan Dadu/Shangdu palace architecture and interiors; 5) Song/Yuan urban crowds in Hangzhou and Quanzhou; 6) Ilkhanid Tabriz court and bazaar; 7) Silk Road oasis towns (Kashgar, Khotan, Dunhuang); 8) the 1274/1281 invasion fleets and Kamakura samurai; 9) Chinese ocean junks; 10) Indian Ocean dhows and sewn boats; 11) Venetian galleys and 13th-c. Venetian dress; 12) eagle, falcon and cheetah hunting; 13) caravan camels and loads; 14) Champa, Java and Sumatra c. 1290; 15) South Indian (Pandya) coast and the pearl fishery.

Book section IDs by region: Venice/Genoa I-01, I-02, III-10 · Acre, Armenia, Georgia I-03, I-04 · Mosul, Baghdad, Persia, Hormuz I-05–I-08, III-08 · Badakhshan, Pamir, Tarim I-09–I-11 · Mongol steppe, Karakorum, Shangdu I-12, I-13 · Kublai's court, Dadu II-01–II-05 · Sichuan, Tibet, Yunnan, Burma II-06–II-09 · South China cities II-10–II-14 · Ilkhanate and Golden Horde wars II-15, III-09 · Japan and the invasions III-01 · Southeast Asia III-02, III-03 · Sri Lanka and India III-04–III-07 · Arabia and East Africa III-07, III-08.

OUTPUT FORMAT (required). (1) A table of works with columns: # · title (original / romanised / English) · creator · year · medium · period and places · accuracy for c. 1260–1295 (high / mixed / low) · what is accurate · what is anachronistic · elements worth studying · book sections · documented sources or consultants (with links to interviews, afterwords or art books). (2) A table for Part 3 with columns: # · visual problem · best period source (object name, holding museum, accession number or excavation, URL) · modern works that visualise it · caveats. (3) A bibliography of every source you used (art books, interviews, museum pages, scholarship), each with a BibTeX entry where it is a publication. (4) Questions you could not resolve. Rules: do not invent titles, creators, accession numbers, interviews or URLs; if you could not confirm a work's research sources, say "not documented". Prefer creator interviews, official art books, museum records and scholarship over fan wikis. Flag works released after 2013 as NEW.
```

## Output (definition of done)
- [x] `research/results/S-22-raw.md` saved (2026-11-13, run in this repo)
- [x] `registry/visual-references.md` (by region and chapter; by work), with existence and source checks recorded (2026-11-13; many rows still `lead`)
- [ ] `[PERIOD]` cue lines drafted for all hero scenes from checked period sources. The initial handoff was partial: eight draft cues for 13 plates, copied and tagged on 10 hero rows; subsequent S-23 work adds more, with significant gaps still open. See the S-23 gap ledger.
- [x] Costume entries handed to S-05 (`CHR.T5` set to ready with cues C1–C4, 2026-11-13; Venetian dress and armour still missing)
- [x] Use rules adopted into the style guide as rules 8–12 (2026-11-13), with one addition: the period reference images are also never image inputs

## Feedback to plan
- `illustration-style-guide.md` § Rules: add the use rules above; rule 7 (people and dress) links to `registry/visual-references.md`
- `illustration-plan.md`: per-scene accuracy notes and `[PERIOD]` cues
- `illustration-style-guide.md` § Review checklist, item 2 (S-10 closed it): gains "period errors" items found here (common anachronisms in modern media are the same errors generators make)

## Follow-up prompts
**Ready to run:** [`research/S-22-follow-up-prompt.md`](../research/S-22-follow-up-prompt.md) (written at close, 2026-11-13). It asks for period objects with records and viewable images, in eleven groups, and covers the three gaps below plus arms and armour. Save its output to `research/results/S-22-followup-raw.md`.

Gaps left by the 2026-11-13 intake:
1. **Period image sources, by problem:** Dadu and Shangdu interiors; Hangzhou and Quanzhou street crowds; Venetian galleys and dress c. 1270; a ger on a cart; Mongol saddle, stirrup and boqta objects with accession numbers; a sewn Indian Ocean hull; Java and Sumatra c. 1290; the Pandya coast and pearl fishery.
2. **Chinese-language work:** reconstruction of Yuan dress from excavated garments (named teams, exhibitions, catalogues); manhua and webtoons set in the Song–Yuan transition.
3. **Catalogue hunt:** the 1999 Suntory Museum exhibition Kaoru Mori names (exact title, lender museum, object list); the bibliography pages inside the *Jaadugar* volumes and the full run of Tanigawa Haruna's Souffle column.

## Findings
2026-11-13. Raw run and intake were both done in this repo, so the check is **not independent**. Records: [raw](../research/results/S-22-raw.md), [intake](../research/results/S-22-intake.md), [registry](../registry/visual-references.md).

- **Spot check:** 13 of the raw file's own flagged doubts tested; 10 supported, 1 not checked, 2 not established or not found (77%). The publisher- and museum-confirmed rows were not re-tested. No image was viewed at any stage.
- **Both seed creators name their sources.** Tomato Soup: d'Ohsson for the outline, checked against Sugiyama, Honda, Shimo and Miya; **Carpini and Rubruck for customs detail**. Kaoru Mori: Krist, Eleanor Lattimore, a 1999 Suntory Museum exhibition (catalogue not found), the Russian Museum of Ethnography, and fieldwork; no consultant. The trail from *Jaadugar* leads to texts the book already cites (see `registry/comparanda.md`), not to new museum objects.
- **The *Jaadugar* anime (2026) has two historical supervisors** and rebuilt the settings in the round; the author says the manga fudged things for composition. For geometry the anime's setting art is the better viewing aid.
- ***A Bride's Story* is a process reference only** (felt, bread, handling an eagle). Its dress, jewellery, tent form, firearms and tea ware are 19th-century.
- **Period objects with a confirmed record:** NPM 故畫000866 (*Khubilai Khan Hunting*, number second-hand); Met 1992.54; Cleveland 1989.50 and three related cloths of gold; Diez A fol. 70–72; Edinburgh Or.MS 20; BnF Arabe 5847; the Quanzhou ship; the *Mōko Shūrai Ekotoba* and the Takashima site.
- **No usable source yet** for Dadu interiors, Song city crowds, Venetian galleys, Java and Sumatra, or the Pandya coast. Follow-up prompts above.
- **Common anachronisms seen in modern media** (candidates for the review checklist): late samurai armour and swords in 1274; the Forbidden City standing in for Dadu; the 19th-century Turkic yurt standing in for the Mongol ger; leather-and-fur "barbarian" Mongols; invented court dress for Mongol women.

**Cues (later, 2026-11-13):** four objects were viewed and eight draft cue lines written into the registry. Viewing settled one open check: Met 1992.54 does show the boqta clearly.

**At this interim stage:** cues for the uncovered regions and armour, costume rows for S-05 / `CHR.T5`, and adoption of the use rules were not done. Later work and the best-effort close are recorded below.


## Supplement intake (2026-11-13)

The supplied extra research is preserved unchanged as [S-22-supplement-raw.md](../research/results/S-22-supplement-raw.md). It largely overlaps the first run, adds a few useful object and reconstruction leads, and does **not** resolve the follow-up gaps on its own. This is a targeted check, not an audit of the report's 37-work survey or its bibliography; its accuracy ratings and specific claims should not be inherited without checking their evidence. The spike remains closed best effort and the existing follow-up prompt remains applicable.

## Failed period-source follow-up and subsequent leads

The supplied follow-up is preserved in [the raw report](../research/results/S-22-followup-raw.md). Its [intake](../research/results/S-22-followup-intake.md) checked 16 deliberately selected records: only 2 held as stated, and no image was viewed. Its claimed 81 sources, resolved gaps, confirmed records and resulting C9–C22 cue text are not reliable. The intake documents the errors and retains eight leads for independent checking. The stricter subsequent work and remaining gaps are in [S-23](S-23-media-scouting.md); do not infer that an unlocated source does not exist.

The following later supplement leads were checked separately at the stated level; they are not new approved cues.

| Lead | Check and use | Remaining work |
|---|---|---|
| Mongol cavalry armour: [Met lamellar helmet 1999.158](https://www.metmuseum.org/art/collection/search/25112) | **Record checked, image not inspected.** The Met describes it as Mongolian or Tibetan, 13th–15th century; carbon dating of the lacing gives 1271–1431. A useful physical comparandum, not a securely identified Polo-era Mongol helmet. | View the object and find better-dated, securely attributed armour before drafting a `[PERIOD]` cue. The C-14 range is for the lacing; it is not proof of the helmet's manufacture date. |
| Caravan animals: [Met 47.18.139, *Mongol with Horse and Camel*](https://www.metmuseum.org/art/collection/search/51738) | **Record checked, image not inspected.** The Met questions its Yuan attribution and identifies it as a copy after Li Gonglin. | View and evaluate it as a possible comparandum, not a securely dated independent witness to late-13th-century caravan loads. |
| Maritime Southeast Asia: [Field Museum Java Sea wreck](https://www.fieldmuseum.org/about/press/shipwreck-and-800-year-old-made-china-label-reveal-lost-history) | **Institutional summary checked, artifacts not viewed.** The museum reports evidence for a date around a century earlier than its previous mid-to-late-13th-century estimate; the wooden hull disintegrated. The cargo may inform maritime trade, with its date qualified. | Check the underlying research and individual objects; this does not establish a ship design or Java/Sumatra scene for c. 1290. |
| Sewn vessels: Belitung wreck and *Jewel of Muscat* | **Leads only.** The report identifies a 9th-century wreck, roughly four centuries before Polo, and a modern experimental reconstruction. | Consult the excavation and reconstruction publications; establish what is evidenced versus reconstructed. Do not transfer the rig or hull unchanged to c. 1290. The existing follow-up prompt already asks for these. |
| Mongolian dress: 2024 Balar's Khad deel reconstruction | **Publication metadata checked:** Crossref confirms the title, authors, journal and DOI `10.69561/mjac.v25i49.3826`; the article and artifact have not been inspected. | Read the article and verify the artifact's date, provenance and reconstruction methods before assigning it to Polo's period or adding a costume cue. |
| *Ghost of Tsushima*: [Paul O'Brien interview](https://www.thesixthaxis.com/2020/07/18/ghost-of-tsushima-interview-history-ps4/) | **Interview checked.** O'Brien describes expertise in Japanese swordsmanship and offers a separate commentary on the game. The supplement's language suggesting an accuracy audit should not be read as evidence that he was a production consultant or as a definitive scholarly verdict. | Check any particular armour, weapon or date claim against period evidence; the existing register's caution remains. |

**Conflicts and limits.** The supplement claims Tomato Soup has never published a bibliography and that Kaoru Mori names no museums or texts. Its own search was incomplete; those claims do not overturn the named sources in the earlier [intake](../research/results/S-22-intake.md) and [registry](../registry/visual-references.md). Compare the underlying creator interviews and volume pages when available. Its more permissive recommendation to use *A Bride's Story* for silhouette and architectural atmosphere also does not establish 13th-century continuity: retain the existing process-only rule and require period evidence for each detail. Its claim that no period source exists for a given problem means **not found in that research**, not proof of absence. The report's proposed *Ghost of Tsushima* judgments and its claim that an Osprey reconstruction used a particular object likewise need direct substantiation.

**Handoff:** These are research leads, not new plate or character-card cues. No images were viewed for this supplement intake; the existing `[PERIOD]` cues, character handoff and style-guide rules are unchanged. For the unresolved costume, armour, ship and regional questions, continue with the [follow-up prompt](../research/S-22-follow-up-prompt.md).

## Decision
2026-11-13. **Closed, best effort.**

1. **Modern works are viewing aids only.** The five use rules are adopted as style-guide rules 8–12. The by-work list in `registry/visual-references.md` says what to look at and what to ignore in each.
2. **Cues are based on period objects or identified museum descriptions.** C1–C7 were viewed; C8 is based on a museum description and its object was not viewed. Eight cue lines (C1–C8) are in `illustration-plan.md`, tagged on ten hero rows. A cue from an object later than 1295 is marked as such.
3. **The seed works' value was their trail.** *Jaadugar* leads to Rubruck and Carpini, which the book already cites; *A Bride's Story* is kept for processes only (felt, bread, handling an eagle).
4. **Reference images are kept in `media/reference/s22/`** (13 files, with a manifest of source and stated licence). They are for looking at, not for print and not for generator input.
5. **What this spike did not deliver** goes to the follow-up prompt, not to guesswork: armour; the ger-cart; Dadu and Shangdu; South China streets; ships beyond one Gulf ship; Venice; Southeast Asia; South India. Plates for those scenes keep their existing "must get right" notes until the follow-up is taken in.

**Plan docs changed:** `illustration-style-guide.md` (rule 7 link; new rules 8–12; review checklist item 2); `illustration-plan.md` (§ S-22 period cues; ten rows tagged); `tasks/cross/PLT-plates.md` (GEN step 1); `tasks/cross/CHR-characters.md` (`CHR.T5` ready); `README.md` (board, decision log).

## Tasks to create on close
- `PLT.T*` cue updates per hero plate; `CHR.T*` costume rows; review-checklist items

**Created 2026-11-13:** no new task numbers were needed. Cue use is now part of step 1 of every `PLT` GEN task; `CHR.T5` already existed and is set to ready; the review-checklist items went straight into the style guide.

**Priority visual return, 2026-11-16:** [Intake](../research/results/S-22-priority-return-2026-11-16-intake.md) sampled ten cited claims: **8/10** held at the stated access level; two overstated or misstated their source. The protocol's strict-rerun threshold is not triggered. The return is not a replacement for prior project image viewing or Takashima/Quanzhou report checks. New official NPM catalog/rights data, the Deji Gate record, and qualified Ayas/Kota Cina leads are in the visual register. The spike's best-effort closure remains; [optional targeted research](../research/S-22-visual-priority-targeted-follow-up-2026-11-16.md) addresses open gaps.
