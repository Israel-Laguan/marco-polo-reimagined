# S-22 — Visual references from modern media (manga, anime, film, TV, games, illustration)

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** the `[PERIOD]` cues in every plate prompt (`illustration-plan.md`); S-05 visual character cards (costume, hair, headgear); S-10 pilot review checklist (period errors); `PLT` secondaries

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
- [ ] `research/results/S-22-raw.md` saved
- [ ] `registry/visual-references.md` (by region and chapter; by work), with existence and source checks recorded
- [ ] `[PERIOD]` cue lines drafted for the hero scenes, worded from the period sources
- [ ] Costume entries handed to S-05
- [ ] Use rules adopted into the style guide (or amended by the user)

## Feedback to plan
- `illustration-style-guide.md` § Rules: add the use rules above; rule 7 (people and dress) links to `registry/visual-references.md`
- `illustration-plan.md`: per-scene accuracy notes and `[PERIOD]` cues
- `S-10`: review checklist gains "period errors" items found here (common anachronisms in modern media are the same errors generators make)

## Follow-up prompts
_(add here if the results leave gaps; e.g. one region or one visual problem in more depth)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `PLT.T*` cue updates per hero plate; `CHR.T*` costume rows; S-10 checklist items
