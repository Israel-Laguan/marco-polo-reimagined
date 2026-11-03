# Volume I: Editorial Critique (*From Venice to the Khan*)

Scope: `vol-1/` (front-01, front-02, ch-01 to ch-13, back-01, README). This was a read-only pass. Line numbers refer to the files as they stand now. "Yule" means `refs/yule-vol1.txt`, and Yule line numbers are given as `Y:nnnn`.

---

## 1. Volume verdict

Volume I is accurate, well sourced and complete against the outline. Every chapter covers its outline beats and its dispute hooks. All 13 chapter epigraphs were found verbatim in Yule. The asides are usually right and often smart: the Jacopo/Ayas problem, the Pipino interpolation, Chagatai's kinship, asbestos, King George. **ch-01 is the model the other chapters should follow.** It is a real retelling, and only 7% of its text is verbatim Yule. Outside ch-01 the volume is mostly *Yule's 1903 English, glossed*.

**Top 3 systemic issues:**
1. **The chapters transcribe Yule rather than retell it.** In ch-04 to ch-11 and ch-13, 47–70% of the narrative words sit inside verbatim 7-word runs from Yule. The Book's own first person ("I will tell you…") is left in place. The Voice Guide calls for a storyteller recounting the book, and says not to speak as if the narrator *were* the Book.
2. **Hinge formulas are repeated mechanically.** Eleven of the 12 narrative chapters open with "Marco Polo starts by narrating that" or "Marco Polo narrates that". There are 34 uses of "Anyway" (21 of them "Anyway, next he…"), and every one of the ~37 dash-asides ends with "Anyway". Over 150k words that projects to roughly 130 uses.
3. **The front/back matter and chapters disagree, and inferences are presented as the Book's words.** The Hormuz "turning back" (Yule's own inference) is stated as Book fact in 5 places, against ch-03's correct handling. back-01 and front-01 credit the Curzola tradition to Jacopo d'Acqui, although ch-01 correctly says Jacopo puts the capture at Ayas. Two front-matter epigraphs are invented. Ramusian material is absorbed inconsistently despite back-01's promise that it never is.

Severity counts: **3 critical · 12 major · 12 minor · 10 nits.**

---

## 2. Findings (ranked by severity)

### Critical

**C1. `front-01-world-before-the-road.md:4`: the epigraph is invented** (axis: fidelity)
- Problem: the epigraph *"Ye must know that in the year of Christ… there were living in Venice two brothers…"* does not appear in Yule. The phrase "there were living in Venice two brothers" has 0 hits.
- Evidence: the real opening of Prologue ch. I is at Y:12495: "It came to pass in the year of Christ 1260, when Baldwin was reigning at Constantinople, that Messer Nicolas Polo… and Messer Maffeo Polo… were at the said city of CONSTANTINOPLE".
- Fix: replace it with *"It came to pass in the year of Christ 1260, when Baldwin was reigning at Constantinople…"* and attribute it to "Prologue, ch. I (Yule–Cordier)".

**C2. `front-02-maps-outbound.md:4`: the epigraph is invented or conflated** (axis: fidelity)
- Problem: the epigraph reads *"from this city of Lop it is forty days' journey across the desert…"*. In Yule the Lop desert takes **a month** at its narrowest (Y:22928, "where its breadth is least, it takes a month to cross it"). The "forty days" comes from **Etzina** (Y:24539–24541).
- Wider risk: this misstatement also teaches readers the wrong number, because line 92 of the same file talks about "forty days".
- Fix: *"And here, where its breadth is least, it takes a month to cross it."* (Book I, Of the City of Lop and the Great Desert).

**C3. Systemic: chapters transcribe Yule instead of retelling it** (axis: voice, prose)
- Evidence: share of narrative words inside verbatim 7-gram runs from Yule:

  | Chapter | Verbatim share |
  |---|---|
  | ch-01 | 7% |
  | ch-02 | 28% |
  | ch-03 | 34% |
  | ch-04 | 49% |
  | ch-05 | 61% |
  | ch-06 | 58% |
  | ch-07 | **70%** |
  | ch-08 | 62% |
  | ch-09 | 65% |
  | ch-10 | 51% |
  | ch-11 | 47% |
  | ch-12 | 17% |
  | ch-13 | 58% |

  Script: `scratchpad/scripts/overlap.py`.
- Worst blocks:
  - ch-05:29–45, the mountain miracle (~1,300 words, nearly all Yule, ending with "And now you have heard in what wise…").
  - ch-06:23–27, the Magi and fire tale.
  - ch-08:27–35, the Old Man's garden.
  - ch-10:27–29, the Samarkand column.
  - ch-07:33–35, the ships and the simoom.
  - ch-13:31–37, the Bacsi and Sensin.
- Book-voice first person left in the narration: ch-05:29 "I will tell you then, the dictation continues…"; ch-05:49 "Now I have told you something of Baudas…"; ch-09:47 "that I do not wish to do at present"; ch-13:41 "Now let us have done with this subject."
- Why this matters:
  - It breaks the Voice Guide, which says not to use a "silent omniscient third-person that pretends to *be* the Book".
  - It flattens the volume's voice: ch-01 sounds like a storyteller, ch-07 like Yule with footnotes.
  - It undercuts the series' claim to be a "retelling".
- Fix:
  - Re-voice the marvel blocks in the ch-01 manner: summarise in the storyteller's own words and keep **one or two** short quoted lines per marvel as flavour, set off as quotations.
  - Target ≤25% verbatim per chapter.
  - Example rewrite for ch-05:33–35: "The Christians prayed eight days and nights, he says, until an angel told a bishop to seek out a certain one-eyed cobbler — a man so chaste that, when a customer's lovely foot stirred an impure thought, he took his own awl to his eye, as the Gospel bids. 'So you can judge what a holy man he was,' the book adds."

### Major

**M1. Curzola is misattributed to Jacopo d'Acqui** (`back-01:33`, `back-01:15`, `front-01` Note [6] at line 74) (axes: continuity, fidelity)
- Problem: back-01 says the Curzola capture "is strong tradition (Jacopo d'Acqui and later tellings)". front-01 Note [6] makes the same claim. back-01:15 states as plain fact that the captivity came "after Curzola (Korčula), 1298".
- Evidence: ch-01:21 and Note [5] say correctly that Jacopo puts the capture **at Ayas**, dated impossibly, and that Curzola rests on later tradition (Ramusio) plus inference from the year. Yule's sidenote at Y:7369 ("Grounds on which the story… rests") supports ch-01.
- Fix for back-01:33: "…dictated in Genoa is the book's own claim (1298). Curzola as the battle is later tradition (Ramusio) plus inference from the year; Jacopo d'Acqui, the nearest witness, puts the capture at Ayas." In front-01 [6], change "(Jacopo d'Acqui and later tradition…)" to "(Ramusio and later tradition; Jacopo names Ayas)". At back-01:15, hedge the claim: "…during a Genoese captivity in 1298, traditionally after Curzola".

**M2. The Hormuz "turning back" is stated as the Book's own words** (`back-01:19`, `ch-07:43` and Note [15], `ch-08:9`, `front-01:54`, `front-02:17`) (axes: dispute handling, continuity)
- Problem:
  - back-01:19 says: *"The outbound plan to take ship at Hormos fails in the book: stitched hulls, deadly summer wind, **bad faith in the haven**."* "Bad faith" appears nowhere in the Book.
  - ch-07 Note [15] marks "**Explicit refusal of sea route**" with ✓.
  - ch-08:9 says "having refused the Ocean Sea at Hormos".
- Evidence:
  - The Book only says "let us return by another road to the aforesaid city of Kerman, for we cannot get at those countries… except through that city" (ch-07:41). That is narrative organisation, not a travel decision.
  - The aborted sea plan is Yule's inference: "Judging from certain indications we conceive it probable… with the view of going on by sea, but that some obstacle arose" (Y:5902–5906).
  - ch-03:25 already handles this correctly ("Yule's reconstruction… not from Prologue itinerary"), so the volume contradicts itself.
- Fix:
  - back-01: "**Did Hormuz turn them around?** Yule inferred that the Polos meant to sail from Hormuz and gave it up; the book itself only says 'let us return by another road to Kerman.' The stitched ships and the heat make the inference attractive, not certain."
  - ch-07 [15]: change the marker to `~` and reword it as "Book's narrative return to Kerman; Yule infers an abandoned sea plan".
  - ch-08:9: "Having brought the reader back from Hormos to Kerman…"

**M3. `ch-02:17` and Note [5]: the outcome of the Berke–Hulagu war goes unflagged and is wrongly marked ✓** (axes: fidelity, dispute handling)
- Problem: the chapter tells the Book's "Barca in the end was worsted" and then says "one of the better-corroborated beats… Rashid al-Din… agree[s]". Note [5] carries ✓.
- Evidence:
  - The Book does say Barca was defeated (Y:12596).
  - Yule's note (Y:12831–12834) corroborates only that the war happened (summer 1262, about eight months long), not who won.
  - Historically, Hulagu's army was routed at the Terek in early 1263, and Rashid al-Din records that defeat. This comes from general history; Yule's note is silent on it.
- Fix: add an aside: "…came to blows then — though the outcome the book gives is backwards: Hulagu's army was routed on the Terek in the winter of 1263." Change the note to "✓ war and date; ✗ outcome".

**M4. `ch-12:25` and Note [8]: the place of Aung Khan's final defeat is garbled** (axis: fidelity, an error in an aside)
- Problem: the chapter says the final defeat came "near the Onon or Buir Nor in 1203".
- Evidence: Yule (Y:25590–25600) says the Onon/Buir Nor battle was **"not the final defeat of Aung Khan… which took place some time later (in 1203) at… the Chacher Ondur (or Heights)… between the Tula and the Kerulun"**.
- Fix: "…was not on the plain of Tenduc in 1200: an earlier clash lay near Buir Nor, and the final defeat came in 1203 at the Jeje'er (Chacher) Heights between the Tula and Kerulen; Aung Khan fled and was killed by Naiman officers."

**M5. Systemic: Ramusian (bracketed) text is absorbed without a flag** (axis: dispute handling)
- Background: Yule puts Ramusio's additions and other supplementary readings in square brackets. Some chapters flag them well: ch-04:31 ("some texts add"), ch-06:13 and :39, ch-08:13, ch-09:33. Many others are told as plain Book fact. back-01:13 promises such material is "never silently absorbed".
- Bracketed passages narrated without a flag:
  - ch-07:35, the Kerman army baked by the simoom. Note [13] admits it is "Ramusian colour"; the body does not.
  - ch-07:15, the turtledoves.
  - ch-07:39, the hired mourners.
  - ch-09:31, the Bucephalus horse breed. Note [10] says Ramusio; the body is silent.
  - ch-10:13, wolves and horn cairns.
  - ch-11:15, the phantom cavalcade.
  - ch-11:19, the caravan bells and night signal.
  - ch-11:29, Camul's three years of crop failure.
  - ch-11:37, the hoof-poisoning plant.
  - ch-12:11, Caracoron's earthen rampart and citadel.
  - ch-12:47, the yak cross-breeds.
  - ch-12 Note [19], "Marco claims to have brought" a musk-deer's head and feet to Venice (bracketed in Y).
  - ch-04:19, the Paipurth silver mine.
  - front-02:73, Badakhshan "Marco's recovery" (Ramusio only).
- Evidence: the bracket list is extracted to `scratchpad/critique/brackets.txt`. Examples: Y:17847 "[And to prove the great heat of this wind, Messer Mark related…"; Y:22948 "[Sometimes the stray travellers will hear… cavalcade…]".
- Fix: add a 3–6-word tag ("Ramusio's text adds", "one version adds") at minimum to the load-bearing items: the Kerman army, the Lop cavalcade and bells, the Bucephalus breed, the Camul crop failure and the musk relic. Mark the matching Notes with "◇ Ramusio".

**M6. Systemic: the hinge formulas fatigue the reader** (axis: voice)
- Evidence: see the scorecard below.
  - Openers: ch-02, 03, 04, 05, 06, 11, 12 and 13 begin with "Marco Polo starts by narrating that". ch-07 and 08 begin "Marco Polo narrates that". ch-09 and 10 use "Marco Polo narrates" in the first sentence. "Starts by" in ch-11, 12 and 13 is wrong outright, because he is not starting.
  - "Anyway": 34 uses in ch-01 to ch-13, of which 21 are "Anyway, next he (mentions/describes/digresses)". Every dash-aside closes with "Anyway…".
  - Book-voice tags ("the book says/insists/adds/assures/must") run 5–7 per chapter in ch-05, 06, 08, 12 and 13.
  - Stock frames repeat: "— A quick note on…" (ch-02, 03, 06, 11); "Here the asides have to be honest" (ch-02:31, ch-03:21, ch-12:25); "Thus Chapter I-5 holds… / Thus Chapter I-6 holds…" (ch-05:51, ch-06:43), which reads as help-desk meta.
  - Pet phrases: "factor's" ×6; "shrug" ×3; "romance sky" ×2; "as one movement of Book I… stand behind" (ch-08:39 and ch-09:47, almost the same sentence); "without courtesy / without softness / without irony / without surprise" as a recurring device.
- Fix:
  - Allow at most one "Anyway" per chapter, and close most asides with a plain return ("So, back to the road:" or simply the next sentence).
  - Rotate openers. Start on place or action, as ch-01, 06 and 09 already do: "Beyond Tonocain…", "The Book, having done with Baudas…".
  - Add a lint to the series style sheet with per-chapter budgets: "starts by narrating" 0 after ch-02; "Anyway" ≤1; "the book insists" ≤2.

**M7. `ch-11:43` and `back-01:45`: the Great Wall "seed" leaves out the main counter-argument** (axis: dispute handling)
- Problem: ch-11 says "Suhchau sits just within its extreme north-west angle". That is Yule's 19th-century phrasing (Y:24254), and it implies the Wall stood there in the 1270s.
- Missing context: the masonry Wall at Suzhou/Jiayuguan is **Ming** (the Jiayu Pass fort dates from 1372). In Polo's day the Hexi defences were eroded Han-era earthworks. This is the central reply to Wood, and the text gives only "a merchant itinerary need not chorograph every landmark".
- Fix: add one clause: "…though the brick-and-stone Wall a modern reader pictures there is Ming, a century after Polo; in his day only eroded earthen ramparts of the Han ran along the Hexi road."

**M8. The gazetteer's naming conflicts with the chapters, and it has gaps** (axis: naming)
- Problem: `gazetteer.csv` is declared the naming authority, and its readme says book_name "follows forms familiar from Polo / Yule". In practice its book_name column uses modern forms.
- Gazetteer form vs chapter form:

  | Gazetteer | Chapters |
  |---|---|
  | Bokhara | Bocara |
  | Mosul | Mausul |
  | Sivas | Savast |
  | Erzincan / Erzurum | Arzinga / Arziron |
  | Yazd | Yasdi |
  | Balkh | Balc |
  | Talikan | Taican |
  | Badakhshan | Badashan |
  | Wakhan | Vocan |
  | Pamir | Pamier |
  | Kashgar / Yarkand / Khotan | Cascar / Yarcan / Cotan |
  | Pem | Pein |
  | Karakorum | Caracoron |
  | Shangdu (Xanadu) | Chandu |
  | Succiu | Sukchur |

- Consequence: front-02's tables follow the gazetteer, so front-02 disagrees with every chapter.
- Error in the gazetteer: the Badakhshan alias "Balashan" is wrong; Yule's form is Badashan.
- Missing rows (about 25 Vol. I places): Sachiu/Dunhuang (a main stop in ch-11), Samarcand, Keshimur, Pashai, Casem, Dogana, Bolor, Chingintalas, Erguiul, Sinju, Egrigaia, Chagannor, Bargu, Kemenfu/Kaipingfu, Genoa, Curzola, Ucaca, Negropont, Kisi, Bastra, Camadi, Reobarles, Canosalmi, Derbend, Ararat, Conia and Casaria.
- Fix: change gazetteer book_name to Yule forms and keep the modern form in modern_name. Add the missing rows, which the maps need anyway. Regenerate the front-02 tables.

**M9. `ch-05` Note [16] does not match body [16]** (axis: citation integrity)
- Problem: body [16] (line 47) is the mountain-miracle aside about dates, parallels and voicing. Note [16] instead discusses "Whole Mausul–Baudas block personally traversed". The parallels are actually in Note [14].
- Fix: either rewrite [16] as "? Mountain-miracle legend cycle: impossible MS dates; parallels (Gregory Thaumaturgus, Muqaṭṭam, Nakhchivan relocation); voice without sneer or endorsement", and move the traversal note to a new [17] anchored at line 51 after "the Book does not say."; or anchor the current [16] at line 51.

**M10. `ch-04` has an orphan Note [15]** (known issue, confirmed) (axis: citation integrity)
- Evidence: the body cites [1]–[14] only; the last marker is [14] at line 35. Note [15] (line 71), on "Whole Caucasian block personally traversed", has no anchor.
- Fix: at ch-04:37, "…is a question the notes must keep open. [15]"

**M11. Long academic asides kill momentum** (axis: prose, voice)
- Problem: the Voice Guide says "Keep asides short… no long academic digressions mid-paragraph". These dash-asides run over 120 words:

  | Location | Words |
  |---|---|
  | ch-10:17 | **224** |
  | ch-08:23 | 166 |
  | ch-01:21 | 157 |
  | ch-10:31 | 149 |
  | ch-05:27 | 141 |
  | ch-08:37 | 138 |
  | ch-04:17 | 136 |
  | ch-03:21 | 134 |
  | ch-06:31 | 127 |
  | ch-12:25 | 125 |
  | ch-02:31 | 122 |

- Commentary paragraphs embedded in the narrative are worse still:
  - ch-10:43 (~280 words on jade, mut'a and Pein's site).
  - ch-10:19 (Bolor).
  - ch-06:11 (a Rashid al-Din panegyric inside the Tauris paragraph).
  - ch-09:45 (Kashmir Buddhism).
  - ch-13:39 (Daoists).
  - All of these list travellers by name (Wood, Gordon, Younghusband, Timkowski, Johnson, Grenard…), which is Yule's notes moved into the narrative.
- Fix: cap each aside at about 60–80 words and keep one key fact plus a cross-reference to the Note. Move the lists of names to the Notes. Example for ch-10:17: "— This is one of the book's great hits. Chinese pilgrims already called these heights 'midway between heaven and earth'; the giant sheep now bear Marco's name, *Ovis poli*; and at this altitude water boils so low that rice never softens. Only Ramusio's version makes the fire-notice hearsay. [5]"

**M12. `ch-12` is inconsistent in texture and overloaded** (axes: prose, structure)
- Problem: ch-12 is 17% verbatim Yule, but unlike the other chapters it is a telegraphic summary. Lines 35–49 read like note cards ("Justice: for petty theft…", "Their religion:…", "Five days east from Campichu…").
- Load: it carries 23 citations and the most outline beats (Etzina, Caracoron, Chinghis, Prester John, the succession, burial, Tartar customs, Bargu, Erguiul, Sinju, Egrigaia, Tenduc, Chagannor).
- Effect: the ethnography reads as a catalogue, and the Bargu digression (line 45) breaks the eastward road.
- Fix: the outline allows a split (I-12a "How the Tartars Became Lords" and I-12b "Tartar Customs; Bargu to Chagannor"). Alternatively, keep one chapter, rewrite the customs paragraphs as narrated scenes, and cut the Bargu/gerfalcon material to about 80 words.

### Minor

**m1. `front-02:17` and `ch-03:23`: the outbound route differs** (axis: continuity)
- front-02 gives Ayas → Anatolian highlands → **Tauris** → Kerman → Hormuz as the route.
- ch-03 gives Yule's Ayas → Sivas → **Mardin → Mosul → Baghdad** → Hormuz (Y:5904).
- ch-05 Note [16] and ch-06 Note [16] leave both open.
- Fix: front-02 should present both as reconstructions.

**m2. `ch-07:23`: Chagatai's kinship error is unflagged** (axis: dispute handling)
- Problem: the text says Chagatai was "own brother to the Great Kaan" and "then in Greater Armenia". Chagatai was Kublai's uncle and died in 1242. ch-10:31 flags the same error; ch-07 Note [7] says only "genealogy compressed".
- Fix: add a 15-word aside with a cross-reference to I-10.

**m3. `front-01:48–54`: citations are out of order** (axis: citation integrity)
- [11] appears in the body (line 48) before [10] (line 54). Renumber them.

**m4. `back-01:4`: the epigraph is embellished** (axes: fidelity, continuity)
- Problem: "*…for I knew I would not be believed*" is a popular expansion. Jacopo's notice is that he had not told half of what he saw, as ch-01 Note [14] correctly paraphrases. Calling it "late tradition" also contradicts ch-01, where Jacopo is a near-contemporary.
- Fix: "*I have not told the half of what I saw.*" Attribute it to Jacopo d'Acqui, *Imago Mundi* (reported deathbed words).

**m5. Notes markers do not match their claims** (axis: dispute handling)
- ch-02 [5]: ✓ on the war's outcome (see M3).
- ch-07 [15]: ✓ "explicit refusal" (see M2).
- ch-08 [13]: ✗ on "Marco personally visited Alamūt", a claim the Book never makes. Use "◇ report; Book says hearsay".
- ch-13 [5]: "✓★★★" mixes the outline's star legend into the ✓~✗◇? system.

**m6. Production scaffolding shows in reader-facing Notes** (axis: prose)
- `/workspace/marco-polo/gazetteer.csv` paths: front-01 [10], front-02 [1], back-01 [11].
- "Gazetteer: *visited*" tags in nearly every chapter Note.
- front-02:9 and Note [1] say "captions below use placeholders until those files are filled" / "when files arrive", but the files exist in `media/`.
- Fix: strip the paths, keep the reliability idea in plain words, and delete the stale lines.

**m7. Notes that duplicate or carry no information** (axis: citation integrity)
- ch-06 [4] repeats [1].
- ch-05 [6] repeats [5].
- ch-12 [3] repeats [2], and [13] repeats [12].
- ch-13 [10] is meta ("Dispute hook: … narrate… weigh the frame").
- ch-09 [16] is a meta summary.
- ch-13 [8] is irrelevant (Vámbéry "grey horse", Kunkrat).
- Fix: merge these or give them content.

**m8. `ch-02:9`: biography is credited to "the book"** (axis: fidelity)
- Problem: "According to the book, the House of Polo belonged to that class…", followed by the Andrea Polo genealogy, and Maffeo who "so far as the book tells, remained a bachelor". The Book contains none of this; it comes from Yule's Introduction and documents. Maffeo's marital status is **unverified** here.
- Fix: "Venetian records, not the book, sketch the house…" and drop the bachelor clause.

**m9. Chapter-closing recaps repeat what was just read** (axis: prose)
- Locations: ch-04:37, ch-05:51, ch-06:43, ch-07:43, ch-09:47, ch-11:43, ch-12:57, ch-13:41. Each closes with a list-recap of the chapter just read.
- Fix: keep one forward-looking sentence and cut the inventory.

**m10. Front matter duplicates ch-02** (axis: continuity / duplication)
- front-01:39–41 ("Second, necessity… Third, papal…") re-argues ch-02's war and letter beats.
- The phrase "the conversion pledge… is the weakest clause" appears verbatim at front-01:41 and ch-02:31, and as "weak joint" at back-01:37.
- Fix: front-01 should point forward to ch-02, not pre-empt it.

**m11. `ch-05` Note [1]: date of the Mosul Atabeg's fall** (axis: fidelity)
- The note says "Malik Ṣāliḥ tortured to death 1261". Mosul fell after a siege in **1262** (general history; not found in the refs). **Unverified.** Check before keeping.

**m12. `ch-02:31` and `back-01:37`: vague scholarship attribution** (axis: fidelity)
- The text cites "de Rachewiltz's work on Mongol administration" for the embassy reading. The apt work is de Rachewiltz, *Papal Envoys to the Great Khans* (1971).
- Fix: cite that by title, without page numbers.

### Nits (10)

1. ch-01:13 "Venice (Venezia) and Genoa (Genova)" and ch-03:9 "Venice (Venezia)": when the book form is the English form, the gloss is noise. ch-03:11 "Jerusalem (Yerushalayim)" likewise.
2. ch-04:21 "Mosul (Mausul)" reverses the book-form-first rule.
3. ch-06:33 says "Istanit… half-legible through manuscript wear", but Note [12] gives the real reason (copyist *sf/st* confusion). Align them.
4. ch-07 Note [9]: "island transfer postdates or post-dates his notice" is a garble.
5. ch-06 Note [13] arithmetic: "livre tournois ≈ £1… → horse ~£193" (200 × £1 ≠ £193). Cite Yule's £193 directly (Y:16596).
6. front-02:27: the caption calls the Chumwa map an "outbound corridor", but it shows the whole round trip including the return.
7. front-01:25 "Anyway, next it helps to name…": the narrative hinge is misused in expository front matter.
8. back-01:21 "one of the first widely read Latin sources": write "Western" (the book was not Latin originally).
9. "Wood" appears unqualified in ch-09:17/19/31 and ch-10:17 (John Wood, 1838) in a volume that also cites Frances Wood. Write "Lt. John Wood" on first use.
10. ch-12:21 "Tanduc—Tenduc" gives no modern gloss at first mention in the chapter; it arrives only at line 51.

---

## 3. Per-chapter scorecard

Column notes:
- **Words**: narrative portion only, excluding the epigraph and Notes.
- **Opener**: SB = "Marco Polo starts by narrating"; MPN = "Marco Polo narrates".
- **Anyway**: total uses (uses of "Anyway, next he…" in brackets).
- **Other hinges**: count of "Polo narrates", "he says", "according to the book" and "the book says/insists/adds/assures/must/will…".
- **Verbatim**: % of narrative words inside verbatim 7-gram runs from Yule.

| File | Words | Opener | Anyway | Other hinges | Verbatim | Citations | Outline coverage | Verdict |
|---|---|---|---|---|---|---|---|---|
| front-01 | 1,512 | — | 1 | 2 | n/a | [10]/[11] out of order | Front-matter spec met | Good context; **invented epigraph**; duplicates ch-02; Curzola/Jacopo error in [6] |
| front-02 | 1,124 | — | 1 | 2 | n/a | OK | Map list partly met (no Venice–Genoa or first-journey map) | **Invented epigraph**; tables conflict with chapter names; stale placeholder text |
| ch-01 | 2,012 | — ("The book itself opens…") | 2 (0) | 0 | 7% | OK [1–15] | Full | Best chapter; a model retelling; capture dispute handled exactly right |
| ch-02 | 2,381 | SB | 2 (1) | 9 | 28% | OK [1–20] | Full | Strong; fix the Berke outcome (M3) and the "according to the book" biography |
| ch-03 | 2,622 | SB | 4 (3) | 4 | 34% | OK [1–16] | Full | Strong; route handled honestly; 4 "Anyway" in 2.6k words |
| ch-04 | 2,376 | SB | 2 (1) | 5 | 49% | **Orphan [15]** | Full | Accurate; heavy Yule transcription; add the [15] anchor |
| ch-05 | 2,995 | SB | 2 (1) | 6 | 61% | **[16] mismatch** | Full | Miracle block is ~1,300 words of Yule; the aside is good but the voice is the Book's |
| ch-06 | 2,754 | SB ("The Book…" then SB) | 2 (2) | 5 | 58% | OK; [4] repeats [1] | Full | Good dispute work; Magi block transcribed; academic paragraph at line 11 |
| ch-07 | 2,950 | MPN | 2 (2) | 11 | **70%** | OK; [15] marker wrong | Full but turn-back over-asserted | Most transcribed chapter; Ramusian army anecdote unflagged; Chagatai unflagged |
| ch-08 | 2,378 | MPN | 1 (1) | 11 | 62% | OK | Full | Assassin dispute well handled; garden block transcribed; "refused the Ocean Sea" |
| ch-09 | 3,120 | MPN (in sentence 1) | 3 (3) | 9 | 65% | OK; [16] meta | Full | Near the length ceiling; Badakhshan illness handled well; Bucephalus breed unflagged |
| ch-10 | 2,741 | MPN | 2 (2) | 7 | 51% | OK | Full | Rich, but ch-10:17 (224 words) and ch-10:43 (~280 words) asides stall the climb |
| ch-11 | 2,742 | SB | 4 (1) | 9 | 47% | OK | Full; Wall seed half-argued | Strong marvel handling (asbestos); Lop Ramusian lines unflagged; Ming Wall point missing |
| ch-12 | 3,038 | SB | 5 (2) | 10 | 17% | OK; [3] and [13] duplicates | Full but crammed | Telegraphic catalogue; Aung Khan aside error; consider a split |
| ch-13 | 2,577 | SB | 3 (2) | 8 | 58% | OK; [8] and [10] empty | Full | Good landing; cane palace correctly ★★★; Bacsi/Sensin transcribed |
| back-01 | 1,278 | — | 0 | 0 | n/a | OK | Spec met | Useful, but repeats errors (Curzola/Jacopo, Hormuz "fails in the book", "bad faith") and has an embellished epigraph |

Epigraph verification:
- ch-01 to ch-13: all 13 found verbatim in Yule (Y:12457, 12495ff, 14225, 15435, 17828, 20774, 21541, 22950 and others).
- front-01 and front-02: **not found** (C1, C2).
- back-01: embellished (m4).

---

## 4. Illustration candidates

★ marks the hero image for each chapter. Each entry gives the anchor quote, what the scene shows, period notes, and any caution.

### front-01 (optional)
- **The world of 1260.** No scene. Use the political map (see §5) instead of an illustration.

### ch-01: In a Genoese Prison
- ★ **Dictation in the cell.**
  - Anchor: "It was perhaps Rustichello who urged that such knowledge not perish in a cell" (ch-01:27).
  - Scene: Marco, about 44, speaking; Rustichello writing on loose parchment quires.
  - Period notes:
    - Venetian patrician dress c. 1298: long *gonella* tunic, mantle, coif or cap.
    - Rustichello is a **layman**, not a monk; the existing plate puts him in a habit.
    - Use quill and ink-horn on unbound gatherings, not a bound codex.
    - The setting is a Genoese civic building, not a dungeon. Tradition sometimes names the Palazzo di San Giorgio (built 1260); treat that as tradition.
  - Caution: method and setting are tradition. Do not label any figure as Ramusio's "Genoese gentleman".
  - Existing media: `drawing-genoa-dictation.png` fits after fixes (monk's habit, chains, Renaissance skyline in the window).
- **Dawn at Curzola.**
  - Anchor: "At dawn on Sunday the seventh the Venetians advanced with the wind behind them" (ch-01:19).
  - Scene: two galley lines closing; Doria's reserve squadron appearing on the flank.
  - Period notes:
    - *Galee sottili*: long and low, with lateen rig and about 25 oar banks rowed *alla sensile* (2–3 oars per bench).
    - Fighting from the bow platform and forecastle; crossbowmen.
    - Genoese red cross on white; Venetian lion of St Mark.
    - No cannon.
  - Caution: Marco's presence is inference, so do not caption a figure as Marco.
  - Existing media: `drawing-venetian-galley.png` is **anachronistic**. Its skyline shows the domes of Santa Maria della Salute (1631–87) and the Gothic Doge's Palace façade (14th–15th c.), and its hull is Viking-like. Redraw.
- **Peace and release, 1299.**
  - Anchor: "before the end of August… Marco Polo was restored to the family mansion" (ch-01:39).
  - Scene: Marco returning to the San Giovanni Grisostomo courtyard.
  - Period notes: Venetian-Byzantine house fronts of c. 1300.

### ch-02: The House of Polo and the Elder Voyage
- ★ **The brothers before Kublai.**
  - Anchor: "He asked a great number of questions: first of the emperors" (ch-02:27).
  - Scene: Kublai enthroned with consorts; the brothers kneeling; interpreters.
  - Period notes:
    - c. 1266, so before Dadu was built (from 1267). Set it at Kaiping/Shangdu or in a palace-tent.
    - Mongol court robes (*jisün*); *keshig* guards.
    - The brothers in Latin merchant travel dress.
  - Caution: the scene is Prologue theatre, and the location is not given in the text.
- **The golden tablet.**
  - Anchor: "he caused to be given them a Tablet of Gold" (ch-02:33).
  - Scene: the paiza handed over.
  - Period notes: an elongated rounded plaque with a suspension hole. Before 1269 it would carry **Uighur-Mongol script, not 'Phags-pa**. Surviving examples are in the Met and in Inner Mongolia.
- **Envoys find the Latins at Bocara.**
  - Anchor: "they were amazed, for they had never before seen Latins" (ch-02:23).
  - Scene: a Bukhara caravanserai.
  - Period notes: the Kalyan minaret (1127) survived the Mongols; the city was still partly ruined.
- **The homecoming of 1269.**
  - Anchor: "his wife was dead, and that she had left behind her a son of fifteen" (ch-02:41).
  - Caution: avoid Pipino's "first sight of a son" pathos.

### ch-03: The Second Setting-Forth
- ★ **Marco presented as liegeman.**
  - Anchor: "“Sire,” said his father… “’tis my son and your liegeman.”" (ch-03:29).
  - Scene: the three Polos kneeling; the oil flask and papal letters on a tray; Kublai about 60.
  - Period notes: Kaipingfu c. 1275; timber hall on a raised platform; Mongol and Chinese officials.
  - Caution: Prologue theatre.
- **The friars turn back at Layas.**
  - Anchor: "When the Preaching Friars saw this they were greatly frightened" (ch-03:19).
  - Period notes: Dominican habit (white tunic, black *cappa*); the Templar Master; Ayas sea-castle; Cilician galley.
- **Oil from the Sepulchre lamp.**
  - Anchor: "take oil from the lamp that burns continually upon the Sepulchre" (ch-03:11).
  - Period notes: the Crusader-era Holy Sepulchre rotunda. Jerusalem was **under Mamluk control** in 1271, with pilgrims tolerated.

### ch-04: Hermenias, Turcomania, Georgiania
- ★ **The quay at Layas.**
  - Anchor: "the merchants of Venice and Genoa, and of other countries, come thither" (ch-04:13).
  - Scene: bales of spice, silk and cotton; Italian galleys; Armenian officials.
  - Period notes: Cilician-Armenian sea castle; lateen-rigged ships; camels on the shore.
- **The oil fountain and mangy camels.**
  - Anchor: "it is good to burn, and is also used to anoint camels" (ch-04:23).
  - Caution: the Book puts this at the Georgian border; the real wells are at Baku. Caption accordingly.
- **The Iron Gate at Derbend.**
  - Anchor: "Alexander caused a very strong tower to be built there" (ch-04:29).
  - Period notes: Sasanian stone walls running down to the Caspian.
  - Caution: the Alexander attribution is legend.
- **Ararat with eternal snow.**
  - Anchor: "on the summit of which snow is so constant that no one can ascend" (ch-04:21).
  - Caution: no Ark.

### ch-05: Mausul, Baudas, and the Mountain That Moved
- ★ **The Caliph in the treasure tower.**
  - Anchor: "He shut the Calif up in the Treasure Tower" (ch-05:25).
  - Scene: Hulagu in lamellar armour; the Caliph among heaps of gold.
  - Period notes: Abbasid dress (black robes, turban); Mongol lamellar armour and fur hats.
  - Caution: **this is an exemplum.** Muslim sources say he was rolled in a carpet and trampled. Caption it "as the book tells it".
- **The mountain moves at the cobbler's prayer.**
  - Anchor: "the mountain rose out of its place and moved" (ch-05:43).
  - Scene: a procession with a cross; Nestorian or Jacobite clergy in Eastern vestments.
  - Caution: **legend**, so style it as an illumination, not a realist scene.
- **Baudas silk weavers.**
  - Anchor: "richly wrought with figures of beasts and birds" (ch-05:21).
  - Note: this works better as a textile detail plate (*nasīj*).

### ch-06: Tauris and the Magi
- ★ **Marco questioning the townsfolk at Saba's tombs.**
  - Anchor: "Messer Marco Polo asked a great many questions of the people of that city" (ch-06:21).
  - Scene: three domed tombs; puzzled townsmen.
  - Period notes: Ilkhanid brick tomb towers; Persian dress.
  - Caution: the tombs are a local tradition.
- **Fire falls into the well.**
  - Anchor: "a fire from Heaven descended into that well wherein the stone had been cast" (ch-06:25).
  - Caution: legend; use an illuminated-manuscript style.
- **The Tabriz gem bazaar.**
  - Anchor: "Tauris is also a great market for precious stones" (ch-06:11).
  - Period notes: Ilkhanid Tabriz c. 1270s; Genoese merchants in the crowd.

### ch-07: Kerman, Camadi, Hormos
- ★ **Marco escapes the Caraunas in the darkness.**
  - Anchor: "Messer Marco himself was all but caught by their bands in such a darkness" (ch-07:25).
  - Scene: a dust-storm gloom; mounted raiders; a mud-walled village (Canosalmi).
  - Period notes: Jiroft plain; date palms; mud walls.
  - Caution: draw the "enchantment" as a dust storm. This is a personal claim, uncorroborated.
- **The stitched ships of Hormos.**
  - Anchor: "on the top of these hides they put the horses" (ch-07:33).
  - Scene: sewn-plank hulls with coir lashings; a single mast; a quarter-rudder; horses standing on hides over the cargo.
  - Note: ideal as a cutaway diagram too.
- **Neck-deep against the simoom.**
  - Anchor: "they plunge into water up to the neck" (ch-07:35).
  - Caution: do **not** illustrate the baked-army anecdote, which is Ramusian hyperbole.

### ch-08: Cobinan, the Arbre Sec, the Old Man
- ★ **The Dry Tree alone on the plain.**
  - Anchor: "there are no other trees near it nor within a hundred miles" (ch-08:21).
  - Scene: a single large *chinar* (oriental plane), half green and half white bark, with a caravan passing.
  - Caution: the landmark is legendary (Alexander romance). Caption it "the book's Dry Tree".
- **Youths carried sleeping into the Garden.**
  - Anchor: "a certain potion which cast them into a deep sleep" (ch-08:29).
  - Caution: this is the **Crusader stereotype**, not Nizari practice. Frame it as legend.
- **The tutia furnace at Cobinan.**
  - Anchor: "over the furnace there is an iron grating" (ch-08:17).
  - Note: works as a process diagram (see §5).

### ch-09: Balc, Badashan, Pashai, Keshimur
- ★ **The balas-ruby mine under royal guard.**
  - Anchor: "the people dig great caves underground, just as is done by miners for silver" (ch-09:29).
  - Scene: miners at Syghinan; royal officers sealing the stones.
  - Period notes: Badakhshan highland dress (*postin*); oil lamps.
- **Marco convalescing on the high pasture.**
  - Anchor: "when in those parts he had been ill for about a year" (ch-09:33).
  - Caution: **Ramusio only.** Caption it as such.
- **The salt mountain at Taican.**
  - Anchor: "so hard that it can only be broken with iron picks" (ch-09:19).
  - Scene: a market day.
- **The ruins of Balc.**
  - Anchor: "fine palaces and buildings of marble, and the ruins of them still remain" (ch-09:13).

### ch-10: Pamier to Jade Country
- ★ **Horn cairns on the Pamir.**
  - Anchor: "these were made into great heaps by the way-side, in order to guide travellers" (ch-10:13).
  - Scene: a snowy plateau; *Ovis poli* horns piled as markers; a fire that will not cook.
  - Caution: the cairn detail is Ramusian (bracketed in Yule).
- **The hanging column of Samarcand.**
  - Anchor: "the foot of the column was without support" (ch-10:29).
  - Caution: pious tale; Marco did not visit.
- **Jade-gatherers in the Khotan rivers.**
  - Anchor: "There are rivers in this country, in which quantities of Jasper and Chalcedony are found" (ch-10:39).
  - Period notes: wading gatherers; white and green jade boulders.

### ch-11: Lop to Tangut
- ★ **The straggler and the spirit voices.**
  - Anchor: "Sometimes the spirits will call him by name" (ch-11:15).
  - Scene: night dunes; a lone rider; a ghostly caravan in the distance.
  - Caution: folklore; the "cavalcade" is Ramusian.
- **The reclining Buddha at Campichu.**
  - Anchor: "The great idols lie at length" (ch-11:39).
  - Period notes: the **real** Western Xia reclining Buddha at Zhangye's Dafo Si (1098) is a precise model.
- **Asbestos cloth bleached in fire.**
  - Anchor: "put into the fire for a while they come out white as snow" (ch-11:33).
  - Note: works as a process vignette.
- **Paper offerings burned at a Sachiu funeral.**
  - Anchor: "figures cut of parchment and paper in the shape of men and horses" (ch-11:23).

### ch-12: Caracoron to Chagannor
- ★ **The cane divination before battle.**
  - Anchor: "the cane bearing Chinghis's name, untouched, climbed atop Prester John's" (ch-12:23).
  - Scene: Nestorian clerics reading a psalm over a split cane; Chinggis watching.
  - Caution: book theatre; the battle site and date are wrong (1203, not Tenduc in 1200).
- **The steppe camp.**
  - Anchor: "Their houses are circular, of wands covered with felts" (ch-12:35).
  - Scene: gers on ox-carts (the *ger-tergen*); women trading; kumis churning.
  - Period notes: 13th-century Mongol dress; deel robes; *boqta* headdress for married women.
- **Merkit reindeer riders of Bargu.**
  - Anchor: "these stags, the book assures you, they used to ride" (ch-12:45).
  - Period notes: taiga; reindeer.
- **Kublai hawking cranes at Chagannor.**
  - Anchor: "plains of cranes, partridges, and pheasants, that he may hawk" (ch-12:55).

### ch-13: Chandu
- ★ **The mare's-milk libation on departure day.**
  - Anchor: "the milk of all those mares is taken and sprinkled on the ground" (ch-13:21).
  - Scene: a herd of white mares; priests (shamans and lamas) scattering milk; the court packing to leave; the cane palace being struck.
  - Period notes: Shangdu's walls of rammed earth faced with brick and stone; the Da'an Ge hall; Mongol court robes.
- **The cane palace braced with silk cords.**
  - Anchor: "braced against mishaps from the wind by more than two hundred cords of silk" (ch-13:15).
  - Period notes: gilt dragon-wrapped columns; a split-bamboo tile roof.
  - Existing media: `drawing-chandu-palace.png` only half fits. Its "marble palace" is a Renaissance arcaded villa (wrong), and the cane hall is an open bamboo scaffold with no dragons or cords. Redraw.
- **Kublai with a leopard on his crupper.**
  - Anchor: "he rides through the park with a leopard behind him on his horse's croup" (ch-13:13).
  - Note: a strong, unusual and well-attested image.
- **The cups flying to the Kaan.**
  - Anchor: "cause the cups to move from their place without being touched" (ch-13:31).
  - Caution: a marvel; render it as the book's claim and its stagecraft.

---

## 5. Multimedia opportunities

### Route-segment maps

Book names are given with the gazetteer row where one exists. **Bold** marks places that need new gazetteer rows.

| Map | Places to plot | Notes |
|---|---|---|
| ch-01 | Venice, **Genoa**, **Curzola** | Inset of the Adriatic; Doria's raid path |
| ch-02 | Constantinople → Soldaia → Sarai → Bolghar → **Ucaca** → Bokhara → (Kublai) → Ayas → Acre → **Negropont** → Venice | The elder voyage |
| ch-03 | Acre ↔ **Jerusalem**, Ayas, then Yule's reconstructed route to **Kemenfu** | Mark the route as a reconstruction |
| ch-04–08 | Ayas → Sivas → Erzincan → Erzurum ±(Mosul/Baudas) → Tauris → Saba → Yazd → Kerman → **Camadi/Reobarles** → Hormuz → Kerman → Cobinan → Tun-o-Kain | Two variant lines (via Tabriz or via Baghdad); dashed for "reported only" |
| ch-09–10 | Sapurgan → Balkh → Talikan → **Casem** → Badakhshan → Wakhan → Pamir → Kashgar → Yarkand → Khotan → Pem | Off-route reported places dotted: **Pashai, Keshimur, Samarcand, Bolor** |
| ch-11–13 | Charchan → Lop → Desert of Lop → **Sachiu** → Succiu → Campichu → Etzina → (Karakorum, digression) → **Erguiul/Sinju/Egrigaia** → Tenduc → **Chagannor** → Shangdu | Off-route: Camul, **Chingintalas**, **Bargu** |

- Existing `map-marco-polo-overview.jpg` and `map-marco-polo-shepherd.jpg` suit front-02 only (whole journey). Per-chapter segment maps need generating from the gazetteer after the M8 fix.

### Timelines
1. **Polo family timeline:** 1254 Marco born; 1260 Constantinople; 1261–62 Berke; 1262–63 war; ~1265 with the envoys (Sartak); 1269 Acre; 1271 departure; 1271 Gregory X elected; ~1275 Kemenfu; 1298 Curzola; 1299 release. Use for front-01 or ch-02/03.
2. **"Book date vs history" table-timeline:**

   | Event | Book date | Historical date | Chapter |
   |---|---|---|---|
   | Sack of Baudas | 1255 | 1258 | ch-05 |
   | Mountain miracle | 1275 / 1225 | impossible | ch-05 |
   | Hulagu's attack on the Old Man | 1252 / 1262 | 1256 | ch-08 |
   | Chinggis made king | 1187 | 1206 | ch-12 |
   | Prester John war | 1200 | 1203 | ch-12 |
   | Elder voyage begins | 1250 | 1260 | ch-02 |

   This is a high-value sidebar for ch-12 or back-01.
3. **Mongol political timeline:** 1206; 1227; 1256 Alamut; 1258 Baghdad; 1260 Kublai's accession; 1264 Shangdu named; 1271 the Yuan name. Pair with front-01.

### Explanatory diagrams
- **Paiza** (ch-02): shape, script and function. Note the change from Uighur-Mongol to 'Phags-pa script in 1269.
- **Sewn-boat construction** (ch-07): coir stitching, trenails, quarter-rudder, hide deck carrying horses.
- **Tutia furnace** (ch-08): earth → furnace → grating that catches zinc-oxide soot (tutia) → slag (spodium).
- **Qanat cross-section** (ch-08:13): the underground stream with access shafts.
- **Mongol decimal army** (ch-12): *arban / jaghun / mingghan / tümen* against the book's *Guz / Toman / Tuc*.
- **Asbestos processing** (ch-11): steps as Zurficar describes them.
- **Cane palace roofing** (ch-13): a bamboo culm split into two hollow tiles, laid interlocking and nailed.
- **Yuan seasonal migration** (ch-13): Dadu ↔ Shangdu with the two roads, the months, and the 28 August libation.

### Tables and side-by-side comparisons
- **Four scripts** (ch-03): Pauthier's list vs Yule's options vs the scripts actually in use.
- **Eight kingdoms of Persia** (ch-06): book name → identification → confidence (Yule's).
- **Kaan succession** (ch-12): the Book's list vs the real line (Ögedei omitted; Batu and Hülegü inserted).
- **How the Caliph died** (ch-05): Polo / Hayton / Rashid al-Din / Ibn al-Furāt.
- **Who captured Marco, and where?** (ch-01): preamble vs Jacopo d'Acqui vs Ramusio.
- **Text witnesses** (ch-01): F (Franco-Italian), Pipino Latin, Z, Ramusio, Yule–Cordier, with dates and traits.
- **GT vs Ramusio** (ch-07, 09, 11): the Kerman army, Marco's illness, the Lop cavalcade. This puts the M5 problem to use for readers.

### Audio and pronunciation moments
- ch-01: Rustichello's preamble read in Franco-Italian ("Seignors emperaor et rois…") alongside Yule's English.
- Place and title glossary audio: Cambaluc/Khanbaliq, Chandu/Shangdu, Badashan, Tauris, Zulcarnain (*Dhū'l-Qarnayn*), Natigay/Etügen, Kemiz/kumis, Bacsi/bakhshi, Sensin, paiza.
- ch-11: a "singing sands" soundscape (Mingsha Shan near Dunhuang) beside the spirit-voices passage, captioned as the natural phenomenon.

### Fixes to existing media
- `drawing-venetian-galley.png`: the 17th-century Salute domes and the hull type are anachronistic. Redraw, or caption it "imaginative" and keep it away from the 1298 text.
- `drawing-chandu-palace.png`: the Renaissance villa is wrong for Yuan architecture. Redraw against Shangdu archaeology.
- `drawing-genoa-dictation.png`: change the monk's habit to lay dress and remove the chains and anachronistic skyline.
- front-02 caption: the overview map shows the full round trip; re-caption it.
- `map-mongol-empire.gif` and `map-asia-mongol-empire.*` share one source. Whether that map shows c. 1260–1295 boundaries or the 1279 maximum extent is **unverified**; check before captioning it as "Polo's generation".
