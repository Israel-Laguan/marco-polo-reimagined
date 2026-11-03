# Volume III critique — *Seas, Return, and After*

Scope: `vol-3/` (README, front-01, front-02, ch-01…ch-12, back-01), read in full. I spot-checked against `refs/yule-vol1.txt` (Prologue and Introduction) and `refs/yule-vol2.txt` (Book III), and against `gazetteer.csv`, `outline-volumes.md`, `VOICE-GUIDE.md`, `media/`, and the relevant vol-1/vol-2 chapters. I did not edit any manuscript file. Two helper scripts, used only for the counts below, live in the scratchpad at `tools/stats.py` (word, hinge and citation counts) and `tools/overlap.py` (8-gram verbatim overlap with the Yule text).

Severity key: **critical** (must fix before any reader sees it) · **major** · **minor** · **nit**.

---

## 1. Volume verdict

The travel half (ch-01 to ch-09) is largely faithful to Yule–Cordier. Quotations, numbers and itinerary check out wherever I grepped them, and most marvels get honest Notes. The cost of that fidelity is that the "retelling" is often a lightly re-punctuated transcription of Yule's 1903 English. In ch-04, 78% of the narrative words sit inside 8-word runs copied verbatim from Yule; ch-03 and ch-08 are at 64% and ch-06 at 59%. That brings the archaic register ("hath", "'tis", "wot", "forsooth") and the Book's own first-person "I tell you" into the narrator's mouth.

The reception and essay half (ch-10 to ch-12) reads rushed. Drafting scaffolding leaks into the prose: "Soft …" appears 137 times in those three chapters alone, and there are meta-references to "the outline", "the drafter" and "first-draft prose … complete". Two epigraphs are invented. The chapters also carry several factual errors about post-1300 history and modern scholarship.

Top three systemic issues:
1. **Invented or paraphrased quotations in quotation marks**, plus production-scaffolding leaks ("Soft …", "dispute hook", "SERIES-STATUS") in reader-facing text.
2. **One-sided handling of the strongest evidence in the "did he go to China" debate.** The 1941 Yongle dadian document published by Yang Zhijiu is absent. No chapter says that no Chinese or Persian source names the Polos. A discredited "Polo in Chinese annals" point (the official is Bolad) and a false "miss" (the Xi'an stele) are counted in the ledger. Wood's case is summarised without her central arguments.
3. **Structural drift in ch-07 to ch-12.** The [V]/[R]/[M] tag lines disappear, three consecutive chapters open with the identical voice-guide formula, the ★ ratings are used with no legend, and every chapter ends with a 100–200-word asyndetic recap list. That recap is the main cause of the over-length in ch-06, ch-10 and ch-12.

**Counts:** 3 critical · 13 major · 14 minor · 10 nits.

---

## 2. Findings

### Critical

**C1. Invented or paraphrased quotations presented as epigraphs (fidelity).**
- `ch-11:4` — *"He who made this work… put in writing all that he saw and heard, so that other people might know of it."* (attributed to "Prologue tradition").
- `ch-12:7` — *"He put in writing all that he saw and heard…"* (attributed to "the Book's own claim").
  - Neither string exists in Yule. The real line, `yule-vol1.txt:12475`, is "it would be a very great pity did he not cause to be put in writing all the great marvels that he had seen, or on sure information heard of, so that other people who had not these advantages might, by his Book, get such knowledge."
  - Fix: replace both with that real line. For ch-12 there is an even better real line, `yule-vol1.txt:12463`: *"And we shall set down things seen as seen, and things heard as heard only, so that no jot of falsehood may mar the truth of our Book."* It is the Book's own visited/reported method, which makes it the natural epigraph for the essay.
- `ch-11:7` — *"And this island [Chipangu] is so rich in gold that no man can tell it…"* is attributed to "Pipino Latin; postils". It is not in Yule, I could not verify it, and it is re-used in the body at `ch-11:22` as Polo's own words ("an island so rich that no man can tell it").
  - Fix: delete it, or quote Yule III.ii verbatim ("the quantity of gold they have is endless"). Quote a Columbus postil only from a verified edition.
- `front-02:4` — *"And from Zayton they sailed…"* is labelled a "Book III itinerary hinge". It does not exist in Yule, and the Prologue never names Zayton; `ch-09` Note [8] concedes as much. Fix: use `yule-vol1.txt` Prologue xviii, "They put forth to sea, and after sailing for some three months they arrived at a certain Island towards the South…".
- `back-01:4` — *"Because of this book many set forth…"* is a self-confessed "paraphrase" sitting inside quotation marks. Fix: cut it.
- Lesser misquotes inside quotation marks:
  - `front-01:4` "And when the ships had been made ready…" — Yule has "had been equipt".
  - `ch-02:4` "When you leave the port of Zayton…" — Yule has "You must know that on leaving the port of Zayton…".
  - Fix: restore the exact wording.

**C2. Drafting scaffolding and production meta-text in reader-facing prose (voice).**
- "Soft" used as a paragraph-label tic: **ch-12 has 72, ch-11 41, ch-10 24**; there are about 155 across the volume, against 0 in the narrative of Vols. I–II. Examples: "Soft ledger breath:", "Soft Wood breath:", "Soft bequests of a Christian merchant:", "Soft anathema of the close:" (`ch-10:33`), "Soft dispute hook stated plainly" (`ch-11:30`). These are outline-note labels that were never removed.
- Meta-references:
  - "restated from the outline's preface" (`ch-11:34`).
  - "without inventing page numbers the drafter has not verified" (`ch-12:96`).
  - "first-draft prose, as craft and as promise, is complete — and the storyteller-voice rewrite of all volumes now stands with it" (`ch-12:130`).
  - "noted in SERIES-STATUS" (`ch-12` Note [13], line 160).
  - Open questions 13–14, "promised in outline end matter, not completed here" (`ch-12:122-123`).
  - "Volume III's Venice chapter must not quietly reabsorb it" (`back-01:43`).
- Fix:
  - Strip every "Soft X:" label. In most cases simply delete the two to four words before the colon; the sentence after it stands.
  - Delete the production-status sentences and SERIES-STATUS references.
  - Move open questions 13–14 to an editorial TODO, not the book.
  - Suggested last line for `ch-12:130`: "…wonders in voice, quarrels in Notes, and no false modernisation of belief."

**C3. Wholesale transcription of Yule's 1903 English, including the Book's first-person voice, without quotation marks (voice / VOICE-GUIDE "Silent omniscient third-person that pretends to *be* the Book"; "not archaic pastiche").**
- Verbatim 8-gram overlap with the Yule text (`tools/overlap.py`):

  | ch-01 | ch-02 | ch-03 | ch-04 | ch-05 | ch-06 | ch-07 | ch-08 | ch-09 | ch-10 |
  |---|---|---|---|---|---|---|---|---|---|
  | 45% | 44% | 64% | **78%** | 34% | 59% | 42% | 64% | 36% | 31% |

- Archaisms in narrative: ch-06 has 11, ch-04 10, ch-01 and ch-03 6 each.
- The narrator says "I" as the Book:
  - `ch-04:13` "And I tell you they go all naked"; `:17` "And I assure you"; `:25` "Now I will quit these particulars"; `:39` "the story I have been telling you"; `:43` "And why should I make a long story of it?"
  - `ch-05:11` "I will tell you how they are got"; `:19` "except what I am going to mention"; `:45` "as I will relate".
  - `ch-06:13` "and I will tell you how"; `:15` "So now I have told you three different ways"; `:59` "I have now detailed to you…".
  - `ch-09:35` "But I should have told you"; `:41` "What more shall I say?"
- Fix:
  - Convert first-person lines to reported speech ("he assures us…", "the Book promises to explain how they are got") or to marked direct quotation.
  - Paraphrase at least half of each long Yule run, especially ch-04:29–43 (the Buddha life, near-verbatim for about 1,100 words), ch-03:31–47 and ch-08:21–47.
  - Keep a few archaic phrases only inside quotation marks.

### Major

**M1. Cocachin and the Wood debate: the decisive Chinese corroboration is missing, and the claims are over-stated without the needed caveat (fidelity / dispute handling / ch-12 fairness).**
- `ch-09:31` calls Rashid al-Din "flagship corroboration", and Note [12] (line 71) says "of the return embassy itself". `ch-12:36`, `ch-11:32` and `back-01:33` say the same.
- None of them mentions:
  - (a) Yang Zhijiu's 1941 publication of a Yongle dadian (*Zhanchi*) document. It names the three envoys (Uladai, Apushka, Koja) in 1290, and Cleaves (1976) treated it in English. This is the strongest single evidence that Polo knew the embassy from inside China, because a Persian-side informant could not have supplied it.
  - (b) The fact that neither that document nor Rashid names the Polos, which is Wood's rejoinder.
- `grep -ri "Yang\|Yongle\|Zhanchi"` across vols I–III returns nothing relevant.
- The same document dates the envoys to 1290 and implies a departure in early 1291. `ch-09:27` follows Yule's "opening of 1292" without flagging the revision.
- Fix: add one inline aside in ch-09 at the [12] position, a Notes entry, and one sentence each in ch-11 [11] and ch-12 [9]–[10]. Suggested aside: "— A Chinese administrative notice of 1290, published by Yang Zhijiu in 1941, names the same three envoys; neither it nor Rashid names the Polos, which is why sceptics and defenders both cite it."
- Mark the 1291-versus-1292 departure as debated (Yule 1292; Haw/Cleaves early 1291 — the latter is unverified here, so check before printing).

**M2. "Polo named in Chinese annals" is listed as a hit (fidelity / continuity with vol-2).**
- `ch-12:36` counts "Ahmad the Bailo's fall echoing Chinese annals in which a Polo name has been read as presence pillar (II-5)" among the hits. Open question 5 at `ch-12:114` repeats the claim.
- It inherits `vol-2/ch-05-ahmad-paper-coal.md:77`: "✓ De Mailla/Gaubil notice is a presence pillar (Vogel; Haw; Rossabi)".
- The *Yuan shi* "Boluo / Po-lo" who examined Ahmad's crimes is generally identified with the Mongol official **Bolad (Pulad) Chingsang**, following Pelliot. Pauthier's identification with Marco is abandoned in the mainstream.
- The genuine hit is the detail of the assassination plot (Wang Zhu, Gao), which matches Chinese sources.
- Fix: replace with "Ahmad's assassination told in detail that matches the *Yuan shi*; the 'Po-lo' once read as Marco is now taken to be Bolad Chingsang." Raise the vol-2 note with that volume's reviewer.

**M3. A false "miss": the Xi'an Nestorian stele (fidelity, essay fairness).**
- `ch-12:44` lists "the Nestorian stele of Xi'an unmentioned at Kenjanfu" as a miss; Note [6] (line 146) repeats it.
- The stele was buried in the 9th century and unearthed only c. 1623–25. Polo could not have seen it, so its absence counts for nothing on either side.
- Fix: delete it from the list and the Note.

**M4. Columbus reception is over-simplified and partly wrong (fidelity, ch-11).**
- `ch-11:22` says Columbus "owned and annotated a Latin Polo, almost certainly in the Pipino tradition". It *is* Pipino: the c. 1483–85 Gerard Leeu printing in the Biblioteca Colombina, Seville.
- The chapter implies the postils fed the 1492 project. The John Day letter (1497/98) suggests Columbus obtained or annotated this copy after the first voyage. His pre-1492 Polo came chiefly through Toscanelli's 1474 letter (Quinsay, Cipangu), and Toscanelli is never named in ch-11 although `back-01:37` names him.
- Linking the postils to the *Book of Prophecies* is loose.
- `front-01:27` ("bent the Atlantic") contradicts ch-11's own caution.
- Fix: add the edition, add Toscanelli, add a one-clause dating caveat ("whether the annotations precede 1492 is debated"), and tone down front-01.

**M5. The Catalan Atlas probably does not show Chipangu (fidelity, ch-11).**
- `ch-11:14` says "Chipangu (Japan) gleams as an island of reported wealth beyond the China Sea" on the 1375 Atlas.
- The standard view is that Japan first appears in European cartography on Fra Mauro's map (c. 1450–59, *Zimpagu/Cimpagu*). I could not verify this from refs, so treat the claim as likely wrong.
- Also: "commissioned for the Crown of Aragon" should be hedged (it was in the French royal library by 1380), and "within three generations" is about 51 years after 1324.
- Fix: move the Chipangu sentence to the Fra Mauro paragraph and keep Cathay, Chanbalech and Chansay for the Atlas.

**M6. Polo's wife given with Yule's 1903 uncertainty instead of the modern identification (fidelity, ch-10).**
- `ch-10:21` says "her family is not assured, though a Loredano connexion has been suspected." That is verbatim Yule (`yule-vol1.txt:8331`).
- Modern scholarship identifies her as **Donata Badoer** (daughter of Vitale Badoer), married c. 1300.
- Fix: "His wife was Donata Badoer, married about 1300 (Yule, before the documents surfaced, guessed a Loredano link)."
- While here, `ch-10:27` gives Pipino's date as "Ramusio thought about 1315–1320". Modern estimates are earlier, c. 1310–1314 (unverified here). Use "in Marco's lifetime, probably the 1310s".

**M7. Ramusian matter absorbed as main text, especially the "autobiographical hinge" (dispute handling).**
- `ch-03:31` narrates the 2,000-man landing, ditches and stockade, and the "better than wine" coconut liquor as the Book's own words. In Yule all of it is a bracketed Ramusian insertion (`yule-vol2.txt:15996-16017`).
- `ch-03:33` then calls it "the autobiographical hinge of Volume III's Sumatran run". `ch-09:25` builds on it ("Ditches and timber, rice and toddy… what III-3 told as a merchant's castaway wait"). Notes [10] say only "plausible castaway practice".
- Smaller, unflagged in the body:
  - `ch-05:19` *Pacauta* prayer (bracketed Ramusio at `yule-vol2.txt:18737`).
  - `ch-07:15` the Scotra whale hunt (Ramusian; flagged only in Note [4]).
  - `ch-01:23` "the King does not allow it to be exported" (bracketed).
- Fix: add an aside in ch-03, e.g. "— the stockade and the two thousand men come from Ramusio's fuller text, not the French; the five-month wait itself is in all versions [10]". Mirror the hedge in ch-09:25 and in Note [10].

**M8. [V]/[R]/[M] tags are not used consistently (consistency / outline).**
- ch-01 to ch-06 carry a tag line. ch-07, ch-08 and ch-09 have none, although the outline gives ch-07 [R] and ch-08 [R/M] and the README gives ch-09 [V/M]. ch-10 to ch-12 have none, although the README lists "[reception]" and similar.
- This contradicts `README.md:17` and SERIES-STATUS ("used consistently").
- `ch-10` Note [1] even says "Reception chapter, not travel **[V]**".
- Justification of the existing tags:
  - ch-01 **[R]** sits awkwardly with its own claim that the junks were "known by eye and deck" (`ch-01:11`); [R/M] or a one-line rationale would fit.
  - ch-06 **[R]** while the gazetteer marks Cail, Coilum and Melibar *visited*; consider [R/M].
- Fix: add tag lines to ch-07 [R], ch-08 [R/M] and ch-09 [V/M]. Use a non-V/R/M label for ch-10 to ch-12, e.g. *[reception]*, and fix the stray [V] in ch-10 Note [1].

**M9. The ★ rating system is used with no legend and clashes with ✓ ~ ✗ ◇ ? (citation integrity).**
- 60 ★ marks appear in Notes across ch-01 to ch-11. The outline legend (★★★ = corroborated … ★ = contested) appears in no front matter. The voice guide prescribes only ✓ ~ ✗ ◇ ?.
- Mixed and confusing uses:
  - `ch-06` Note [4] "★ Dispute: diamond-gathering legend ◇ over mining fact ★★".
  - `ch-04` Note [14] "★★★ Dispute: Buddha life — remarkable sympathy" (★★★ used for "cultural moment", not corroboration).
- Separate "★ Dispute:" Notes are often duplicates of the preceding Note: `ch-03` [7] repeats [6], `ch-04` [5] repeats [4] and [7] repeats [6], `ch-05` [10] repeats [8].
- Fix: either add the ★ legend to `front-01`, or (better) convert all ★ to the five voice-guide markers and merge each "★ Dispute" Note into its neighbour.

**M10. Formulaic recap closers and triple summarising (prose / length).**
- 10 of 12 chapters end with an asyndetic list paragraph: "Thus … stands in order: …; …; … for this chapter it is enough that … in one Venetian breath".
  - "Thus …" closers: ch-01:47, ch-03:51, ch-04:45, ch-05:51, ch-06:61, ch-07:51, ch-08:51, ch-09:43, ch-10:41.
  - Soft-close variant: ch-02:39.
  - "it is enough that" appears in 8 chapters; "one Venetian/coastal breath" in 4.
- Many chapters also pre-summarise in the opening paragraph and again mid-chapter: `ch-02:21-23`, `ch-03:19,33`, `ch-04:15`, `ch-05:17`, `ch-06:27`.
- Roughly 1,500 words of the volume restate what the reader has just read.
- Fix: cut every final "Thus …" paragraph to a single bridging sentence or delete it, and cut the mid-chapter "So X stands as…" paragraphs where an aside already exists.

**M11. Over-length chapters (prose; narrative words before ## Notes, headings and epigraphs excluded).**
- **ch-06 — 3,637 words** (README tolerates about 3,500). Cut to about 3,150:
  - the closing recap `:61` (about 150 words);
  - the Lar wrap-up aside `:27` → one sentence (about 90);
  - the "Idolaters with a language and a king of their own, tributary to nobody" formula repeated in Tana/Cambaet/Semenat `:51-55` → once, then "likewise" (about 70);
  - Chughi `:23-25` compressed (about 100);
  - the duplicated "interior omitted" sentences in `:45` and `:59` (about 40).
- **ch-10 — 3,339 words.** Cut to about 2,800:
  - the will paragraph `:33` (about 420 words of itemised legacies) → about 150, keeping trustees, San Lorenzo, Peter the Tartar's manumission, Donata and the daughters (saves about 270);
  - the Cepoy paragraph `:25` → about 200 (saves about 130);
  - the closing recap `:41` (about 130);
  - plus the "Soft" labels.
- **ch-12 — 3,784 words.** Cut to about 2,900:
  - remove the "Soft" labels (about 72 words, plus the following labelling clauses, about 250);
  - delete `:130` (about 150);
  - delete `:72`, which repeats ch-11's false-binary paragraph (about 110);
  - fold the "court and canal texture" paragraph `:38` into `:36` (about 80);
  - cut open questions 13–14 and merge 4 into 7 with stress-points (about 80);
  - trim the "Principles" bullets that restate the README (`:96-100`, about 100).

**M12. Generated "map" is geographically wrong and mis-credited as Wikimedia (multimedia / accuracy).**
- `front-02:19-21` embeds `media/map-indian-ocean.jpg` with the caption "(Wikimedia Commons — credit in media/ATTRIBUTIONS.md)".
- `ATTRIBUTIONS.md` lists this file as a *generated* plate; it is byte-identical in size to `drawing-indian-ocean-schematic.png`.
- On inspection the image has:
  - "Hormuz" at the southern tip of Arabia (the Aden position);
  - "SINAE" written over Persia;
  - China placed north-east of India with a route running overland across the Himalaya;
  - Ceylon on the wrong side of the peninsula;
  - post-1500 three-masted European ships.
- `map-return-route.jpg` is byte-identical to `map-marco-polo-overview.jpg` (checked with `cmp`), although its caption describes a dedicated return schematic.
- Fix: replace the generated image or caption it "decorative plate — not a map" (credit: generated). See §5 for the real return-route map.

**M13. Wood's case is under-stated (ch-12 fairness; ch-11).**
- `ch-11:32` and `ch-12:66` summarise Wood as silences (Wall, tea, foot-binding, names), Yanju and "convenience of wonders".
- Missing:
  - her central argument that **no Chinese (or Persian) record names the Polos**;
  - Persianised place-name forms as evidence for a Persian-language source;
  - the Saianfu chronology. It is treated separately as a "stress-point" but is not credited to her case.
- On the defence side, `ch-12:44` calls foot-binding "a social law of gendered bodies in the Song–Yuan world", over-stating its Yuan-era extent. It omits the standard reply that it was then limited to elite Han women, and that Odoric (c. 1320s) does mention prized small feet.
- No date is given for Wood (1995) or the replies (de Rachewiltz 1997, Haw 2006, Vogel 2013) in ch-11 or ch-12; back-01 gives 1995.
- Fix: add one sentence each and date the works.

### Minor

- **m1.** `ch-12:30` (and Note [4]) says "Jacopo d'Acqui–type notices of Curzola and prison". This contradicts `vol-1/ch-01-genoa-prison.md:21`, which correctly says Jacopo puts the capture at **Ayas**, dated impossibly, and that Curzola comes from Ramusio. Fix: "Ramusio's Curzola and Jacopo d'Acqui's Ayas are later tradition…". Note that `vol-1/back-01:33` has the same error.
- **m2.** `back-01:17` says Adam's Peak "gathers Muslim, Hindu, and Christian footstep traditions in the book's telling". In the Book it is **Muslim (Adam) and Buddhist (Sagamoni Borcan)** (`ch-04:27,39`). Fix: "Muslim and Buddhist".
- **m3.** `front-02:62` and the gazetteer row "Male / Maldives | Maldives | cowries and ambergris" equate Polo's Male island with the Maldives. `ch-07:13` and Note [2] explicitly refuse that collapse, and Polo mentions no cowries there. Fix: list "Male and Female Isles — legendary (no fix)" in front-02 and rename or annotate the gazetteer row.
- **m4.** Gazetteer and book-name mismatches:
  - gazetteer `Basman` vs ch-03 and Yule `Basma`;
  - gazetteer and front-02 `Sememant` vs ch-06 and Yule `Semenat`;
  - gazetteer `Abyssinia` vs `Abash`;
  - gazetteer and front-02 `Kalhat` vs ch-08 and Yule `Calatu`.
  - Missing rows that chapters rely on: Mutfili, Lar, Mailapur (St Thomas), Sondur/Condur, Gauenispola, Kis (Qais), Negropont, Abhar.
- **m5.** First-mention modern glosses are missing in body text (they appear only in Notes):
  - ch-03: Basma (Pasai) `:21`, Lambri (Lamuri) `:41`, Fansur (Barus) `:45`, Ferlec (Perlak) at first mention `:15`.
  - ch-04: Necuveran — "Nicobar" never appears in the narrative (`:11-15`).
  - ch-05: Maabar (Coromandel) not glossed until `:45`.
  - ch-01: Gulf of Cheinan `:43` (Hainan / An-nan conception).
- **m6.** Marvels narrated with no inline aside, flagged only in Notes:
  - tailed men `ch-03:43`;
  - the Ruc `ch-07:27` ("'Tis said…" frames it, but there is no aside on the legend or the Aepyornis background);
  - St Thomas miracles and martyrdom `ch-05:45-49`;
  - suttee `ch-05:23,31`.
  - Fix: add a one-line dash aside to each, e.g. ch-03 "— a marvel the Archipelago had told since Ptolemy; perhaps a costume or a forest people misdescribed [16]".
- **m7.** Outline hook not inline: the dislocation of the Indian chapter order is listed as a ch-05 dispute hook but appears only in `ch-05` Note [1]. ch-06 does handle it inline (`:39,:49`). Add half a sentence in ch-05 or a forward pointer.
- **m8.** Notes out of step with the body in ch-05:
  - Body [13] (`:35`, washing, right hand, sureties, debt rule) is answered by Note [13] (`:81`), which discusses rain, omens and 13-year-old boy traders — the content of body [15].
  - Note [15] (`:85`) is a placeholder: "Soft bridge toward consecrated damsels".
  - Fix: swap the contents and write a real [15].
- **m9.** Placeholder Notes that say nothing: `ch-06` [9] "Soft bridge to Cail", [13] "Soft colour…", [20] "Soft bridge to Tana–Kesmacoran sequence"; `ch-02` [13]; `ch-03` [4] (gazetteer status only). Either give them content or drop the citation from the body.
- **m10.** A promise that is never kept: `ch-06:39` and Note [15] say the Pole Star at Comari "is key for the Cocachin-fleet landfall argument later". ch-09 never makes that argument. Delete it or add it.
- **m11.** `ch-01:11` calls Manzi "the Sung name the Book still uses". Manzi (*Manzi*, "southern barbarians") is a northern and Mongol term for the Song realm, not a Song name. Fix: "Manzi (southern China — the conquered Sung realm, under its northern nickname)".
- **m12.** `ch-01:43` attaches "Moreover, Messer Marco Polo never was there" to the Ramusian Gulf of Cheinan passage. In Yule (`yule-vol2.txt:14400`) that sentence closes the Sea of Chin / 7,459-islands chapter, before the Cheinan note. Re-sequence it, or say that the confession belongs to the eastern isles.
- **m13.** ch-11 Jesuit paragraph (`:28`):
  - It omits Bento de Góis (1602–07) and Ricci's identification of Cathay with China, the classic beat.
  - It asserts without support that Jesuits "measure[d] silences" (tea, foot-binding) against Polo. I know of no source for this, so mark it unverified or cut it.
  - The print paragraph (`:26`) gives no dates; supply 1477 German, c. 1483–85 Latin, 1496 Venetian, 1503 Santaella, 1559 Ramusio.
- **m14.** `ch-07:9`, `ch-08:9` and `ch-09:9` all open with "Marco Polo starts by narrating that…", copied straight from the voice-guide example. Together with "Anyway" (2–3 per chapter, about 1 per 900 words, which projects to roughly 170 across the series), "A quick note/aside" (5) and "Here the asides have to be honest" (3), this is a fatigue risk. See the scorecard for per-chapter counts. Fix: vary the openers, allow at most one "Anyway" per chapter, and retire "the asides have to be honest".

### Nits (10)

- **n1.** Redundant glosses in the rewritten chapters: "Aden (ʿAdan / Aden)" `ch-08:9`; "Acre (Acre / ʿAkkā)" `ch-08:17`; "Champa (Champa / the Vietnam coast)" `ch-07:37` (also use the book form *Chamba*).
- **n2.** `ch-12:130` says "across forty chapters and this closing essay". The series is 40 chapters *including* the essay (SERIES-STATUS).
- **n3.** `ch-09` Note [17] (`:81`) says "some argue 1296 to fit 'twenty-six years' absence from 1271". 1271 + 26 = 1297, and the Prologue's "six-and-twenty years" is time spent in Asia, not total absence.
- **n4.** `ch-09:29` says "In the fuller Ramusian expansion, word of their arrival went up from Hormos". Ramusio does not name Hormuz; "on landing at Hormuz" is Yule's inference (`yule-vol1.txt` note 6).
- **n5.** `ch-06:11` "five hundred, say some manuscripts": it is Ramusio only (`yule-vol2.txt:19843`).
- **n6.** `ch-06:17` "matches Rudrama Devi of the Kākateya line" follows Yule's widow reading. Modern accounts make her Ganapati's daughter who ruled in her own right; hedge with "Yule identified". The modern spelling is Kākatīya.
- **n7.** `ch-08:45` says "the book explains … of the stitched ships and the dates-and-fish diet, of the simoom and the turn inland". Yule's text (`yule-vol2.txt:24817`) has none of this list; it is the narrator's gloss inside the Book's speech.
- **n8.** `ch-02:21` says "Yule leans toward… or the return voyage still ahead". Yule inclines to the Geographic Latin 1288 and the c. 1290 Indian mission (`yule-vol2.txt:14790`) and does not propose the return voyage.
- **n9.** `ch-11:22` calls Columbus "Genoa's most famous son after — and beside — the Venetian", which muddles Polo (Venetian) with Genoa.
- **n10.** `ch-01` Note [3]: for the watertight bulkheads, add the strongest corroboration, the 1274-era Quanzhou (Houzhu) shipwreck excavated in 1974, whose hull is divided into 13 compartments — matching Polo's "thirteen". This is from my own knowledge; verify before citing.

---

## 3. Per-chapter scorecard

Narrative words exclude headings, epigraphs and Notes. "Hinges" counts "Marco Polo narrates", "Polo narrates", "He says", "According to the book", "Anyway", "Then he/Polo describes" and "Tradition has it". "Soft" counts the label tic. "Verbatim" is the share of narrative inside 8-gram runs copied from Yule.

| File | Words | Hinges (of which "Anyway") | "Soft" | Verbatim | Tag in file | Citations | Outline coverage | Verdict |
|---|---:|---|---:|---:|---|---|---|---|
| front-01 | 832 | 2 (1) | 0 | – | – | 8/8 ok | Preface ✓; legend ✗; map list partial | Good primer. Fix the misquoted epigraph and the "bend the Atlantic" overstatement. |
| front-02 | 662 | 1 (1) | 1 | – | – | 3/3 ok | Map list ✓ | Invented epigraph; Male = Maldives; non-gazetteer names; mis-credited, wrong generated map. |
| ch-01 | 2,264 | 11 (3) | 1 | 45% | [R] (arguably [M]) | 15/15 seq ok | Full | Strong and faithful. Fix "Manzi = Sung name" and the Cheinan "never was there" placement. |
| ch-02 | 1,796 | 9 (3) | 2 | 44% | [R/M] ✓ | 13/13 | Full | Solid and lean. Epigraph wording; Notes [4]–[6] overlap; [13] is a placeholder. |
| ch-03 | 2,193 | 7 (2) | 2 | 64% | [V/M] ✓ | 18/18 | Full | Ramusian stockade absorbed as the autobiographical hinge; tailed men unflagged; glosses missing. |
| ch-04 | 2,603 | 9 (3) | 2 | **78%** | [R/M] ✓ | 17/17 | Full | Best material (the Buddha passage) but near-verbatim Yule with first-person "I". Re-voice. |
| ch-05 | 2,770 | 6 (3) | 3 | 34% | [R/M] ✓ | 19/19 (Notes [13]/[15] out of step) | Dislocation hook only in Notes | Good economics aside; fix the Notes misalignment; add Thomas and suttee asides. |
| ch-06 | **3,637** | 4 (2) | 5 | 59% | [R] (arguably [R/M]) | 25/25 (3 placeholders) | Full | Over length; repetitive port formula; dangling Pole Star promise. |
| ch-07 | 2,694 | 10 (3) | 0 | 42% | **missing** ([R]) | 21/21 | Full | Good disputes; tag missing; formula opener; Ruc not flagged inline. |
| ch-08 | 2,057 | 10 (3) | 1 | 64% | **missing** ([R/M]) | 21/21 | Full | Accurate. Formula opener; redundant glosses; heavy verbatim. |
| ch-09 | 2,728 | 2 (0) | 2 | 36% | **missing** ([V/M]) | 17/17 | Beats ✓; corroboration one-sided | Faithful to the Prologue and Yule notes; lacks Yang Zhijiu and modern chronology; inherits Ramusian stockade. |
| ch-10 | **3,339** | 2 (1) | **24** | 31% | none ([reception]) | 16/16 | Full | Rich and well sourced from Yule's Introduction, but dated (Donata), over long (the will), heavy "Soft" tic. |
| ch-11 | 2,648 | 2 (1) | **41** | 0% | none | 12/12 | Beats ✓ but thin on print and Jesuits | Invented epigraphs; Catalan Atlas/Cipangu; Columbus over-simplified; meta leaks; paragraphs over 400 words. |
| ch-12 | **3,784** | essay (formulas only quoted) | **72** | 0% | none | 13/13 (sparse for an essay) | All 9 sections ✓ | Right architecture, but invented epigraph, Bolad and stele errors, thin Wood précis, production leaks, over length. |
| back-01 | 770 | 0 | 0 | – | – | 7/7 | ✓ | Useful pocket form; fake epigraph; Adam's Peak error; some duplication with ch-11 (acceptable as pointers). |
| README | 764 | – | – | – | – | stray [1]–[3] are format examples (ok) | – | Claims a tag convention that ch-07 to ch-12 don't follow. |

**Rushed signals in ch-07 to ch-12 (rewritten 2026-09-14):**
- tag lines dropped from ch-07 on;
- identical formula openers in ch-07, ch-08 and ch-09;
- a new trailing "**Comparative:**" block format in ch-07 to ch-10 (ch-01 to ch-06 fold comparatives into numbered Notes);
- the "Soft" tic jumps from 0–5 per chapter to 24, then 41, then 72;
- invented epigraphs and meta leaks in ch-11 and ch-12;
- paragraph sizes balloon (ch-11:30, :32, :34 are each over 400 words).

**Citations:** every [n] in the body has a Notes entry and vice versa, numbering is sequential in all files, and there are no orphans (checked by script). The problems are semantic: placeholder Notes, duplicate "★ Dispute" Notes, the ch-05 misalignment and the undefined ★ scale.

---

## 4. Illustration candidates (★ = hero image for the chapter)

| Ch | Scene | Anchor (≤15 words, file) | What is happening | Period-accuracy notes | Caution |
|---|---|---|---|---|---|
| 01 | ★ **Saving a holed junk** | "empty the cargo from that compartment into those adjoining" (ch-01) | Crew shift pepper baskets out of a flooded hold while carpenters plug the leak | Fujian seagoing junk c. 1270–90: V-hull, transom stern, axial stern rudder, 4 masts with battened mat sails, iron-nailed double planking, lime/tung-oil caulk; Quanzhou wreck as a reference | The whale-strike cause is Ramusian folklore — show a reef |
| 01 | The 1281 storm | "A north wind blew with great fury and caused great damage" (ch-01) | The Yuan fleet driven onto a small island; men struggling ashore | Use the *Mōko Shūrai Ekotoba* scroll (c. 1293) for Japanese samurai and Mongol/Korean ships; stone anchors from the Takashima wreck | Do not depict the "false-banner capture of the capital" as history |
| 01 | Chipangu's golden palace (as imagined) | "entirely roofed with fine gold, just as our churches are roofed with lead" (ch-01) | A Venetian listener's mental image | Render in a Latin manuscript-illumination idiom, not Kamakura architecture | Legendary; caption as rumour |
| 02 | ★ **Lifting rudders in the shoal strait** | "great ships in passing this channel have to lift their rudders" (ch-02) | Junks hoisting their axial rudders off the Bintan coast | Raisable Chinese rudders (true technology); Malay perahu; mangrove coast | — |
| 02 | Elephant tribute from Chamba | "a tribute of twenty of the greatest and finest elephants" (ch-02) | Cham envoys present elephants | Cham dress, brick kalan towers; Yuan officials | The pity-tale softens a brutal 1282–85 war |
| 03 | ★ **Five months at Samara** | "detained five months by the weather, which would not allow of his going on" (ch-03) | Junks at anchor, sailors ashore, toddy-tappers, waiting skies | Northern Sumatran coast, palms, Yuan junks | Stockade and 2,000 men are Ramusian — keep the camp modest or caption it |
| 03 | The "unicorn" in the mud | "not in the least like that which our stories tell" (ch-03) | Split panel: Sumatran rhino vs a Western virgin-and-unicorn | Sumatran rhino is hairy and two-horned | The Book says one horn; note the discrepancy |
| 03 | Toddy-tapping | "they cut a branch and attach a great pot to the stem" (ch-03) | A man ascends a palm to fix a pot | Gomuti/sugar palm | — |
| 04 | ★ **Pilgrims on Adam's Peak chains** | "several great and massive iron chains, so disposed that by help of these men" (ch-04) | Buddhist and Muslim pilgrims climbing together | 13th-c. Sinhalese and Arab pilgrim dress; chains attested by Ibn Battuta | Dual Adam/Buddha claim; don't resolve it |
| 04 | Relics arrive at Cambaluc (1284) | "the whole population of Cambaluc went forth to meet those reliques" (ch-04) | Procession with the alms-bowl and teeth | Yuan court; Tibetan and Chinese Buddhist clergy | Book's "Adam" framing; embassy plausible but unconfirmed |
| 04 | The prince meets death and age | "by the roadside he beheld a dead man" (ch-04) | The Great Departure as the Book tells it | Choose between an Indic idiom and a Latin re-imagining and say which | Localised wrongly in Ceylon |
| 04 | Dog-headed men (optional) | "in the face they are all just like big mastiff dogs" (ch-04) | — | Reproduce the *Livre des Merveilles* (c. 1410) miniature, not a new image | Myth; never show as ethnography |
| 05 | ★ **Pearl divers and the shark-charmer** | "The divers jump from the small boats and go to the bottom" (ch-05) | Divers with net bags; a Brahman charmer chanting on deck | Gulf of Mannar boats; stone weights; Pandya coast | Charm "dissolved at night" is belief |
| 05 | Arab horses landed in Maabar | "They bring the horses by sea aboard ship" (ch-05) | Horses swung off sewn-plank dhows | Stitched Indian Ocean boats; Persian Gulf merchants | — |
| 05 | Pilgrims take the red earth | "take earth from the place where the Saint was killed" (ch-05) | Pilgrims at the Mailapur shrine | Coromandel shrine c. 1290; St Thomas Christians and Muslims | Miracle cures are cult claims |
| 06 | ★ **Corsair cordon off Malabar** | "a signal is made by fire or smoke, and the whole make for it" (ch-06) | A line of pirate craft relays smoke and closes on a merchantman | Konkan/Malabar coastal craft, families aboard | Tactics may be stylised |
| 06 | Pole Star off Comari | "you see it about a cubit above the water" (ch-06) | Sailor sighting a low Polaris at night | Night seascape at about 8°N | — (diagram-friendly) |
| 06 | Diamond valley | "White eagles that haunt those mountains... pounce upon the meat" (ch-06) | Eagles lifting meat from a serpent ravine | Inset: real alluvial washing on the Kistna | Legend (Sindbad type) |
| 06 | Brahman reads his shadow | "takes note of his own shadow in the sun" (ch-06) | Merchant pausing a deal to measure his shadow | Sacred thread; Coromandel market | — |
| 07 | ★ **A "Ruc feather" at Kublai's court** | "a feather of the said Ruc measuring ninety spans" (ch-07) | Courtiers marvelling at a giant frond-like "feather" | Yuan court dress; quill likely a palm frond or bamboo | Ramusian and legendary — caption as a court curiosity |
| 07 | Scotra whale hunt | "barbed iron darts that cannot come out once fixed" (ch-07) | Islanders harpooning a sperm whale | Socotri boats | Ramusian detail |
| 07 | The giraffe described | "colour all red and white in round spots" (ch-07) | A giraffe on the Swahili/Somali coast | — | Not Madagascar |
| 08 | ★ **Wind-catchers of Hormos** | "their houses are built with ventilators to catch the wind" (ch-08) | A street of bād-gīr towers at noon heat | Old (mainland) Hormuz c. 1290; surviving towers are later, so treat them as type | — |
| 08 | Cattle fed on dried fish | "live upon small fish and nought besides" (ch-08) | Camels eating fish on drying racks | Hadramawt coast | — |
| 08 | Tapping frankincense at Dufar | "notched with a knife in several places" (ch-08) | Harvesting *Boswellia* resin | *Boswellia* trees, not fir | — |
| 09 | ★ **Kublai gives the paiza; the fleet at Zayton** | "gave them two golden Tablets of Authority" (ch-09) | Kublai hands golden tablets to the three Polos; 13 junks behind | Phags-pa-script paiza (surviving examples exist); Persian envoys; Cocachin in a *boqta* headdress | Port of departure is inferred; year 1291 vs 1292 debated |
| 09 | Cocachin weeps at parting | "she wept for sorrow at the parting" (ch-09) | Farewell in an Ilkhanid camp | Ilkhanid dress and tents from *Jami' al-Tawarikh* miniatures | Narrative pathos |
| 09 | Escort riders on the Persian road | "furnished with two hundred horsemen, more or less, to escort them" (ch-09) | A mounted column with gerfalcon tablets | Ilkhanid cavalry c. 1294 | — |
| 10 | ★ **Jewels from the seams** | "to rip up some of the seams and welts, and to take out of them jewels" (ch-10) | Polos slashing shabby Tartar coats at a banquet | 1295 Venetian Veneto-Byzantine interior | Ramusio's legend — caption as tradition. Avoid Salute domes or Renaissance façades |
| 10 | Dictating the will, January 1324 | "He has sent for Giovanni Giustiniani, Priest of San Proculo and Notary" (ch-10) | Sick Marco, notary, Donata and daughters; Peter the Tartar | 1320s Venetian domestic setting; the will is extant (Marciana) | — |
| 10 | The Cepoy copy, 1307 | "gave and presented to the Lord of Cepoy the first copy" (ch-10) | Marco hands a manuscript to a French knight | French knightly dress c. 1307 | — |
| 11 | ★ **Columbus annotating his Polo** | "who owned and annotated a Latin Polo" (ch-11) | Columbus with the Leeu Latin edition, quill at the margin | c. 1490s Castile; reproduce the actual postil hand | Annotation date debated (possibly after 1497) |
| 11 | Cresques workshop, Majorca | "the great Catalan Atlas of 1375" (ch-11) | Jewish cartographers gilding vellum panels | 1370s Palma | Japan likely absent from this atlas |
| 11 | Fra Mauro at his mappamundi | "Fra Mauro's world map" (ch-11) | The monk at the disk in Murano | 1450s San Michele; the Fra Mauro medal as reference | — |
| 12 | ★ **Marco and Rustichello in the Genoese prison** | "took down from Messer Marco Polo in a Genoese prison" (ch-12) | Dictation scene | Use the existing `drawing-genoa-dictation.png`; 1298–99 Genoa | Prison circumstances partly tradition |
| 12 | The control panel | "Rubruck, Odoric, Ibn Baṭṭūṭa, and Rashid keep the control panel lit" (ch-12) | Four travellers' manuscripts side by side | Use real manuscript images; no invented portraits | — |

---

## 5. Multimedia opportunities

**1. Real return-route map (replaces the stand-in `map-return-route.jpg`).** Feeds front-02 and ch-09.

Plot these gazetteer rows, in order: Cambaluc (Khanbaliq) → Zayton (Quanzhou) [departure inferred] → Chamba (Champa) [possible] → Pentam → Samara / Java the Less [Sumatra wait, certain from the Prologue] → Necuveran → Seilan (Ceylon) → Maabar / Cail (Kayal) → Coilum (Quilon) → Comari → Eli → Melibar → [Gozurat / Cambaet optional] → Kesmacoran → Hormuz (Hormos) [landfall inferred] → overland via Kerman → Abhar near Qazvin (marriage to Ghazan) → Tauris (Tabriz) → Trebizond → Constantinople → Negropont → Venice.

Design rules:
- Solid lines for Prologue-named stages (Java/Sumatra, Trebizond, Constantinople, Negropont, Venice). Dashed lines for inferred ones.
- Seasonal labels: NE-monsoon departure; SW-monsoon wait; 18 months on the Sea of India; landfall 1293/94; Kublai's death (Feb 1294) received on the road; Venice 1295.
- Inset: Ilkhanate and Yuan borders c. 1294, reusing `map-yuan-1294.png` and `map-mongol-empire.gif` as base.
- Prerequisite: gazetteer rows for Abhar and Negropont, which do not exist yet.

**2. Monsoon and season diagram.** Feeds front-01, ch-01:41 ("two winds"), ch-03 and ch-09 (Sumatra wait), ch-05:39 (rains June–August) and ch-07:25 (Madagascar current: 20 days out, more than 3 months back). A two-panel wind map (NE Nov–Mar, SW May–Sep) with a calendar strip of the Cocachin fleet.

**3. "Polo's order vs the coast's order" strip map.** Feeds ch-05/06 (the dislocation hook). Book sequence Maabar → Mutfili → Lar → Cail → Coilum → Comari → Eli → Melibar → Gozurat → Tana → Cambaet → Semenat → Kesmacoran, drawn against true coastal order, with crossings highlighted (Coilum before Comari; Gozurat before Tana and Cambaet).

**4. Pole Star altitude chart.** Feeds ch-03 and ch-06. Sumatra "not seen" → Comari 1 cubit → Melibar 2 → Gozurat 6 → Cambaet "higher", plotted against the real latitudes (about 5°, 8°, 11°, 21°, 22°N). A neat empirical-hit graphic.

**5. Reception timeline.** Feeds ch-10, ch-11 and back-01; check every date before printing:
1298–99 dictation · 1305 "Milioni" document · 1307 Cepoy copy · c. 1310s Pipino Latin · 1324 will · Jacopo d'Acqui (1330s) · John of Ypres (c. 1350) · 1375 Catalan Atlas · c. 1450–59 Fra Mauro · 1474 Toscanelli letter · 1477 first printing (German) · c. 1483–85 Leeu Latin (Columbus's copy) · 1492 · 1496 Venice · 1503 Santaella · 1559 Ramusio · 1602–07 Góis · 1818 Marsden · 1871/1903 Yule–Cordier · 1928 Benedetto · 1938 Moule–Pelliot · 1941 Yang Zhijiu · 1959–73 Pelliot *Notes* · 1995 Wood · 1997 de Rachewiltz · 1999 Larner · 2006 Haw · 2013 Vogel.

**6. Side-by-side source tables.**
- **Cocachin in three sources** (ch-09/ch-12): Polo's Prologue / Rashid al-Din / the Yongle dadian (Yang 1941). Columns for envoy names, dates, the bride, the Polos named or not.
- **Japan 1274/1281** (ch-01): Polo vs Japanese and Yuan sources — commanders, storm, outcome, date.
- **Madeigascar vs Magadoxo** (ch-07): camels, elephants, sheikhs, giraffes, current.
- **Return mortality variants** (ch-09): 600 / 8 (Fr.) / 18 / Ramusio's 600 dead with one envoy surviving.
- **Hits, misses and silences ledger** (ch-12), with ✓ ~ ✗ ◇ ? and cross-volume chapter refs.

**7. Audio / pronunciation moments.** Sagamoni Borcan (Śākyamuni Burqan); Cocachin (Kököchin); Kiacatu (Geikhatu); Casan (Ghazan); Abraiaman; *Choiach*; *Pacauta*; *Tembul*; *bād-gīr*; Chipangu (Jih-pên-kuo); *Milione*. A short read-aloud of the Prologue's "things seen as seen, and things heard as heard" would suit ch-12.

**8. Existing `media/` fit.**

| File | Where it fits | Notes |
|---|---|---|
| `drawing-manzi-junk.png` | ch-01, ch-09 | Usable. Caveats: Western-style galleried stern and portholes, five masts |
| `drawing-genoa-dictation.png` | ch-12 hero | Fits |
| `drawing-venetian-galley.png` | ch-10, with caveat | Skyline shows domes resembling 17th-c. Santa Maria della Salute and a later Ducal Palace — anachronistic for 1295 |
| `map-marco-polo-overview.*` | front-02 / ch-12 overview | Fits |
| `map-yuan-1294.png`, `map-mongol-empire.gif` | ch-09 political context | Fits |
| `map-indian-ocean.*` / `drawing-indian-ocean-schematic.png` | — | Not usable as a map (see M12); at most a decorative endpaper, captioned as generated |
| `map-return-route.jpg` | — | Byte-identical stand-in; replace per item 1 |
