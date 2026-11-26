# S-07 — Structure and length decisions

**Status:** closed (2026-11-10) · **Timebox:** 1 session · **Gates:** I-12, III-10, III-11, III-12, over-length chapters (II-13, III-6), all front/back files

## Question
1. Does I-12 split into two chapters?
2. What does each front/back file do, so they stop repeating each other and the chapters?
3. Do the reception chapters (III-10 to III-12) need a structural rebuild rather than a re-voice?
4. What is the length policy?

## Why it matters
- **I-12** is a crammed note-card catalogue (23 citations, 13 outline beats).
- **Front and back matter** explain paper money, coal and the conversion pledge two or three times. Vol. II front matter misses its outline beats (tag preface, legend, map list).
- **III-10 to III-12** were written last and show it: dropped tags, "Soft" labels, invented epigraphs, a one-sided debate summary.
- **Length:** the recaps account for most of the over-length.

## Inputs
- `outline-volumes.md` (allows I-12a/b; front-matter specs)
- Critique: I-M12, I-m10; II-M8, II-m12; III-M10, III-M11, III-M13; length cut plans
- S-01 outcome (re-voicing shrinks chapters)

## Method
1. I-12: outline both options (split vs scene-ify) and pick one.
2. Front/back role matrix: one row per topic, one column per file; assign each topic to exactly one home.
3. III-10 to III-12: per-section keep / rewrite / add list (Yang Zhijiu, Toscanelli, Góis, print dates, Wood's full case).
4. Length: confirm 1,800–3,200 (essay 3,500), or relax for "long" chapters.

## Output (definition of done)
- [x] Decision on I-12: no split; scene-ify (section plan below)
- [x] Front/back role matrix
- [x] III-10 to III-12 section plans
- [x] Length policy recorded in `VOICE-GUIDE.md` (and enforced for front/back in `tools/lint.py`)

## Feedback to plan
- `content-revision-plan.md` § W4 (order, I-12), § W5 (de-duplication)
- `multimedia-plan.md` placements if a chapter splits

## Findings

Word counts are the lint's own count (narrative above `## Notes`; headings, tables, images and epigraphs excluded), measured 2026-11-10.

### 1. I-12: split or scene-ify

| Block | Lines | Words |
|---|---|---|
| Etzina, Caracoron, how the Tartars became lords, the Kaans, the Altay burials | :9–33 | 1,392 |
| Tartar customs (huts, marriage, gods, war, justice) | :35–43 | 718 |
| Bargu digression | :45 | 202 |
| East: Erguiul, Egrigaia, Tenduc, Sindachu, Chagannor + closing recap | :47–57 | 725 |
| **Total** | | **3,091** |

- **A split gives two chapters under the floor.** The outline's I-12a ("How the Tartars Became Lords") would be about 1,400 words and I-12b ("Tartar Customs; Bargu to Chagannor") about 1,650, both below 1,800 *before* the re-voice. The re-voice shrinks prose: asides go to ≤ 80 words, the closing recap goes, and the :33 aside-like paragraph becomes a Note. Neither part could hold its length without padding, which the guide forbids.
- **The problem is texture, not load.** I-12 is only 16% verbatim. It reads badly because :35–43 are note cards with labels ("Justice:", "Their religion:"), not because it has too much matter. II-2 carried a palace inventory of the same density and came out at 1,894 words once it was told as scenes.
- **A split costs a lot for no gain.** 85 Markdown files mention I-12 or I-13 (task IDs, W4 order, plate rows, multimedia placements, the gazetteer's first-appearance column). Every one would need renumbering, and Vol. I would go from 13 chapters to 14 when the outline's trim map points the other way (13 → 11).
- **Bargu stays where Polo puts it.** It breaks the eastward road because the Book itself breaks it there. The series keeps episode order, so the fix is to frame it as Polo's look north and compress it, not to move it.

**Section plan, one chapter (target 2,300–2,800; four asides):**

| § | Content (current lines) | Action |
|---|---|---|
| 1 | Campichu → Etzina → Caracoron (:9–13) | Keep; retell. Caracoron aside ≤ 80 words (Rubruck; walled 1235). |
| 2 | How the Tartars became lords (:15–25) | Retell as one story: tribute to Prester John → Chinghis made king → embassy and insult → **cane divination** (hero-plate anchor; one marked quote) → battle. Merge the :19 and :25 asides into one ≤ 80-word aside (1187 will not stand; Toghrul/Aung Khan; final defeat 1203 at the Jeje'er Heights, per `I-12.T1`). Everything else goes to Notes. |
| 3 | The Kaans and the Altay (:27–33) | Polo's succession list in one sentence + one aside (Ögedei left out, Batu and Hülegü put in). Burial convoy told as a scene. :33 (Rashid, "which Altay") becomes a Note. |
| 4 | Tartar life (:35–43) | **Drop the labels.** Retell in Polo's order as one moving camp: camp on the march (felt huts on carts, door to the south, women trading) → the household (wives, the marriage gift, levirate, the marriage of the dead as a told scene) → the felt gods (Natigay; fat on the idols' mouths, broth at the door; kumis) → the host (bow, boiled-hide armour, mare's milk and blood, the decimal army: C4 anchor) → justice (the stick counts; nine-fold ransom). About 700 words. |
| 5 | Bargu (:45) | ≤ 80 words, framed as Polo's look north before the road turns east: the Mescript riding their stags, the falcon cliffs by the ocean, the gerfalcon islands. |
| 6 | East to Chagannor (:47–55) | Retell: Erguiul (yaks, musk), Egrigaia (camlets), Tenduc + King George aside ≤ 80 words (Monte Corvino 1305), Sindachu, Chagannor's cranes. About 600 words. |
| 7 | Closing (:57) | One forward sentence (≤ 25 words) toward Chandu. |

### 2. Front/back role matrix

The current files have no rule for what goes where, so every file re-explains the headline topics. The roles:

- **F1 (context): what the reader needs *before* the volume.** Background no chapter narrates, the volume's scope in one paragraph, and the reader's key (APP.T1 box). It names a topic and points forward; it never gives the verdict a chapter gives.
- **F2 (maps): orientation only.** Map list, maps, captions, generated place tables (`GAZ.T5`), and map cautions limited to *identifications*. Routes and circuits are described here, not in F1.
- **Chapters narrate.** The verdict on a claim lives in the chapter's aside and Note, or in the III-12 ledger for the cross-volume hits and misses.
- **B1 (back): pointers, not re-explanation.** (a) A dispute shortlist: one line per dispute (verdict + "see II-11, Note n"; no brackets, since a bracketed number prints as a citation: S-08), ≤ 40 words each. (b) Trivia the chapters' bodies do not already tell: names that entered Europe, later nicknames and echoes. No closing summary paragraph.
- **III-11 tells the reception (events); III-12 weighs the arguments.** III-B1 does neither.
- **No phrase twice.** A sentence used in one file is never reused in another ("the conversion pledge… is the weakest clause", "quiet proof", "bent the Atlantic").

Key: **H** home (the full treatment) · **f** frame only (≤ 2 sentences, no verdict) · **p** pointer (≤ 1 sentence or one shortlist line) · **✂** cut · blank = absent, keep absent.

| Topic | Chapter | I-F1 | I-F2 | I-B1 | II-F1 | II-F2 | II-B1 | III-F1 | III-F2 | III-B1 | III-11 / III-12 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mediterranean trade; Venice–Genoa rivalry | I-1 narrates the war | **H** | | | | | | | | | |
| Mongol successor realms, Pax Mongolica | | **H** | f (caption) | | | | | | | | |
| Why the Polos went east: blocked road, papal letter, conversion pledge | **H** I-2 | f (:39–41 → 1 sentence; keep "opportunity" and "information hunger") | | p | | | | | | | |
| Curzola, Jacopo's Ayas, the prison frame | **H** I-1 | ✂ (Note [6] fix stands) | | p | | | | | | | p (III-12 §2) |
| Manuscript families ("the book has many books") | I-1 (dictation) | | | ✂ → p | | | | | | | **H** III-12 §2 |
| Reader's key: markers, tags, Ramusio label | | **H** (APP.T1 box) | | | f (short box) | | | f (short box + *[reception]*) | | | |
| Visited vs reported, per volume | tag + Note [1] | | | ✂ (:47) | f (preface, outline beat 1) | | ✂ (:43) | f | ✂ (:13 "coastal rosary" → 1 sentence) | ✂ (:35) | III-12 §2 |
| Name and date conventions | | **H** (:56) | | | f (Chinese forms only) | | | f (Indian and African forms only) | | | |
| Volume route / circuits | chapters | f (:54 → scope sentence) | **H** | | ✂ (:41–48 → II-F2) | **H** | | f (:43 scope) | **H** | | |
| Map list (outline beat) | | | **H** | | | **H** (add Cambaluc, SW circuit; M8) | | | **H** | | |
| Two capitals, seasonal court | II-2, I-13 | | | | **H** | | ✂ (:15) | | | | |
| Paper money | **H** II-5 | | | | f (:35 → no verdict) | | ✂ trivia :17; p dispute :39 | | | | ledger III-12 §3 |
| Coal | **H** II-5 | | | | f (:37) | | ✂ trivia :19; p dispute :41 | | | | ledger III-12 §3 |
| Ahmad | **H** II-5 | | | | ✂ (:39 → clause) | | p (:21) | | | | |
| Yanju, Saianfu | **H** II-11 | | | | ✂ (:52) | p (identification only, :69) | p | | | | III-12 §5 |
| Kinsay numbers | **H** II-13 | | | | | f (caption only; :31 ✂) | p | | | | III-12 §5 |
| Book IV as horizon | **H** II-15 | | | | ✂ (goes with circuits) | f (map list) | ✂ (:27) | | | | |
| Silences: Wall, tea, foot-binding, script | asides where Polo passes (I-11, II-2) | ✂ (:50) | | ✂ (:45) | | | ✂ (:45) | | | ✂ (:41) | **H** III-12 §4 |
| Numbers and days' journeys | | | p (:92 caution) | ✂ (:49) | | | | | | | **H** III-12 §5 |
| Old Hormuz | I-7, III-8 | | **H** (:90 caution) | | | | | | | | |
| Monsoon | III-3 (the wait) | | | | | | | **H** | p (:78) | ✂ (:15) | |
| Chipangu gold | **H** III-1 | | | | | | | f (:27) | | p | III-11 (Columbus); III-12 §5 |
| Cocachin embassy | **H** III-9 | | | | | | | f (:31–33 politics) | | p (with Yang Zhijiu) | III-12 §3 |
| Ramusio homecoming; *Milione* | **H** III-10 | | | | | | | | | ✂ (:23, :43) | |
| Maps, Columbus, print, Jesuits | | | | | | | | ✂ ("bent the Atlantic", M4) | | ✂ (:27, :37, "Afterlives in one breath") | **H** III-11 |
| Wood debate | | | | | | | | | | ✂ (:39) | **H** III-12 §6; III-11 p (event) |
| Why a retelling; its principles | | f (series preface, ≤ 60 words) | | | | | | | | | **H** III-12 §8; III-11 :34 ✂ |

Expected effect: I-B1 1,229 → about 700, II-B1 862 → about 550, III-B1 761 → about 400, II-F1 984 → about 800 (with the short box), I-F1 1,434 → about 1,150 (with the full box). The F2s change little in length; they gain map-list items.

### 3. III-10 to III-12: rebuild or re-voice?

**None needs a rebuild.** All three follow their outline beats (III-12's nine sections are "the right architecture", per the critique scorecard). What was wrong: scaffolding ("Soft" ×14 / 17 / 44 still), recaps, block sizes, facts, and **overlap between them** (MS trail in III-10 and III-12, Wood in III-11, III-12 and III-B1, "why a retelling" in III-11 and III-12). So each gets a re-voice with a section plan, and the boundary is set: **III-10 ends at 1324 plus the manuscripts and readers of Marco's own lifetime; III-11 starts in 1375 and tells events; III-12 argues.** Facts come from `registry/facts.md` (F-15, F-16, F-18 to F-22, F-27, F-32, F-34, F-35, F-37).

**III-10 (3,321 → target 2,300–2,600)**

| § | Content (lines) | Action |
|---|---|---|
| 1 | Homecoming tableau (:9–17, ~740) | **Rewrite, ~400.** Frame as Ramusio's tradition from the first sentence (one Ramusio flag for the whole tableau). Malipiero source chain as one ≤ 80-word aside. Worst verbatim block :15 (83%). |
| 2 | *Il Milione* (:19, 257) | Keep, ~200: competing attributed explanations; use the 1319 traveller identification via Bolognari/Vogel and do not assert a chronology for “million lies” (S20-E27/E43). |
| 3 | Merchant life, marriage, daughters (:21–23, 371) | Rewrite, ~250. **Donata Badoer**, married early 14th c.; the daughters per F-16. |
| 4 | Manuscript trail: Cepoy (:25, 355); Pipino (:27, 223) | Cepoy → ~200; Pipino → ~170, "in Marco's lifetime, probably the 1310s" (F-18). |
| 5 | Early readers: d'Abano, *Bauduin*, distrust and delight (:29–31, :39 first half) | Merge, ~300. |
| 6 | The will, deathbed, death, burial (:33–35, :39 Jacopo) | **Reorder:** will (433 → ~170: trustees, San Lorenzo, Peter the Tartar freed, Donata, daughters) → Jacopo's deathbed "not told one half" → death 8/9 January 1324 (F-35) and burial (~150). |
| 7 | Portraits and relics (:37) | ≤ 80-word aside. |
| 8 | Closing recap (:41, 132) | One forward sentence toward the maps of III-11. |

**III-11 (2,629 → target 2,400–2,800)**

S-20 closed 2026-11-13; the [qualified handoff](../../../research/investigations/results/S-20-closure.md) supersedes older reception assumptions in this plan.

| § | Content (lines) | Action |
|---|---|---|
| 1 | Opening "Tradition has it…" (:12) | Rewrite: open in the scene (Paris, the Atlas). |
| 2 | Catalan Atlas (:14–16) | Keep; omit the unsupported Chipangu claim; whether Japan is represented remains unverified; in the French royal library (F-20). Aside :16 (166) → ≤ 80. |
| 3 | Fra Mauro (:18) | Keep; cut "Anyway"; describe Fra Mauro's surviving map as mid-15th century, without an unqualified first or exact Japan-label spelling (F-20). |
| 4 | Lesser charts (:20) | Keep. |
| 5 | **Add: Toscanelli** | Optional, ~100: attribute the contested correspondence and its disputed influence, or omit the causal link (F-19; S20-E42). |
| 6 | Columbus (:22–24) | Rewrite: Leeu's Latin, Gouda 1483–84, in the Colombina; annotations by Columbus and his circle with dates uncertain; do not imply this copy or its postils fed the 1492 voyage (F-19); epigraph and :22 quote per F-27; fix n9 ("Genoa's most famous son"). Aside :24 (227) → ≤ 80. |
| 7 | Print (:26) | **Add the dates** (F-21): 1477 Nuremberg German; Gouda Latin; 1496 Venice; 1502 Lisbon; 1503 Castilian; 1559 Ramusio. |
| 8 | Missionaries and Jesuits (:28) | **Add Góis** with Yule's facts only (Pamir 1603; Suzhou; died there); cut "measured silences"; Ricci hedged (F-22). |
| 9 | Modern scholarship (:30, 321) | Keep, ~250: Yule, Cordier, Pelliot, Moule–Pelliot. |
| 10 | Wood (:32, 325) | **Shrink to an event, ~120:** 1995 book and the public reaction, her central claim in one clause (no Chinese or Persian record names the Polos), the replies by date (1997, 2006, 2013); the case itself is weighed in III-12 §6. |
| 11 | "Why a formal retelling now" (:34, 368) | **Cut** to one forward sentence; its content belongs to III-12 §8. |

**III-12 (3,753 → target 2,800–3,200; essay)**

| § | Content (lines) | Action |
|---|---|---|
| 0 | Opening recap (:9–11) | Cut; open on the method line of the epigraph. |
| 1 | What kind of book (:15–21, ~500) | Keep; rewrite → ~380. |
| 2 | Method; MS types; Ramusio (:25–27, ~385) | Keep → ~300. **Home of the MS-families topic.** Curzola/Jacopo per F-34. |
| 3 | Hits (:31–37, ~510) | Rewrite → ~400: drop the Bolad "hit" (F-08); fold :35 into :33; Cocachin with Yang Zhijiu as Cleaves reports it (F-15). |
| 4 | Misses and silences (:41–45, ~385) | Rewrite → ~330: drop the Xi'an stele (F-32); foot-binding hedged (F-37, M13). **Home of the silences topic.** |
| 5 | Stress-points (:49–59, ~370) | Keep → ~330; credit Saianfu chronology to Wood's case; absorb open question 4. |
| 6 | Wood and the replies (:63–69, ~395) | **Rebuild, ~450, the home of the debate.** Wood 1995 in full: no Chinese or Persian record names the Polos; Persianised place-names; the Saianfu chronology; the silences. Then the replies by date: de Rachewiltz 1997, Haw 2006, Vogel 2013 (currency, salt), and Yang Zhijiu's notice with its limit (it doesn't name the Polos). Delete :69 ("restated from III-11"). S-13 may later update this section; it does not gate it. |
| 7 | Comparative travellers (:73–83) | Keep → ~280. |
| 8 | Principles (:87–101, ~390) | Rewrite → ~200. Drop :93, :95 and :101 (they restate the README), and :97, which quotes the v1 hinges the v2 guide now bans. **Home of "why a retelling".** |
| 9 | Open questions (:105–123) | Keep 1–3 and 6–12, minus 5 (Bolad); 4 goes to §5; cut 13–14 (meta) → ~180. |
| 10 | Close (:127, 143) | One sentence: "…wonders in voice, quarrels in Notes, and no false modernisation of belief." |

### 4. Length

- **Narrative 1,800–3,200 holds; no relaxation for "long" chapters.** The over-length chapters are the ones with Yule left to remove: II-13 (3,330 words, 44% verbatim) and III-6 (3,609, 63%). The S-01 shrink of 25–40% puts both at about 2,200–2,700. III-10 (36% verbatim) falls inside by its section plan. Raising the ceiling would only invite padding.
- **Essay 2,500–3,500.** A floor is new: the cut plan (about −900) must not hollow out the nine sections.
- **Front/back ≤ 1,200 words** each (none had a limit). That fits every file once de-duplicated. As a guide, F2 prose should stay under about 500 and B1 under about 800.
- **Order of work is unchanged:** re-voice first, re-measure, apply a cut plan only if still over the ceiling (W4).

## Decision
_Closed 2026-11-10._

1. **I-12 stays one chapter, told as scenes** (section plan above). No new files and no renumbering; `multimedia-plan.md` placements are unchanged.
2. **Front/back roles:** F1 frames, F2 orients, chapters narrate, B1 points. Each topic has one home (matrix above). Recorded in `VOICE-GUIDE.md` § Front and back matter.
3. **III-10 to III-12: re-voice with section plans, no rebuild.** Boundary: III-10 to 1324 and Marco's lifetime readers; III-11 the reception events from 1375; III-12 the arguments. Wood's full case lives in III-12 §6; "why a retelling" in III-12 §8.
4. **Length:** narrative 1,800–3,200 (unchanged), essay 2,500–3,500 (floor added), front/back ≤ 1,200 (new; lint `length` now checks front/back).

## Tasks to create on close
- [x] `I-12.T3`: section plan added (scene-ify; no split).
- [x] `III-10.T3`, `III-11.T3`: section plans added.
- [x] `III-12.T3`: created (essay prose pass with section plan).
- [x] `.T3` de-duplication tasks created in all nine front/back files (I-F1, I-F2, I-B1, II-F1, II-F2, II-B1, III-F1, III-F2, III-B1), each listing its cuts and pointers from the matrix.
- No new chapter files (I-12 does not split).
