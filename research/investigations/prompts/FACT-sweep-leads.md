# Deep research prompts — the obscure rows of the S-06 sweep

**For:** `registry/facts.md` rows F-38, F-39, F-43 and F-44, found by the S-06 sweep beyond the critique (2026-11-03). F-40–F-42 (the Yuan name, Yaishan, Guo Shoujing) are textbook facts that one look at Rossabi or Needham settles; they get no run.
**Run** each batch as its own deep-research job. Save each output untouched, with a first line naming the tool, model and date:

| Batch | Rows | Question | Save to |
|---|---|---|---|
| A | F-44 | Polo's Ceylon king Sendemain, and the Sinhalese regnal numbers Yule and Cordier disagree on | `plans/research/results/FACT-A-ceylon-raw.md` |
| B | F-43 | The Rāma Khamhaeng inscription: its date, its standing, and whether a Locac Note may call it "coeval" | `plans/research/results/FACT-B-sukhothai-raw.md` |
| C | F-38, F-39 | The War of St Sabas at Acre (start, end), and Baibars's reign and death | `plans/research/results/FACT-C-acre-raw.md` |

**Intake:** the trust rules in `research/README.md` apply. The output is a lead: a row moves from *still open* only when the intake sees the source (dates and numbers: two independent sources, or one primary source). Update `registry/facts.md` first, then the `.T1` item in the files the row lists, then `characters.yaml` for F-39 (`CHR`).

---

```text
BATCH A — The king of Ceylon in Marco Polo's book (c. 1280–1295)

I am preparing a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903, with Cordier's 1920 Addenda) for print. I need the modern scholarly answer to one identification and one chronology, with sources I can check.

WHAT THE BOOK SAYS. Book III, chapter 14 ("Concerning the Island of Seilan"): the island has a king called SENDEMAIN (Ramusio: SENDERNAZ) and pays tribute to nobody. Chapter 15 tells of a Mongol embassy that Kublai sent in 1284 to obtain relics of the Buddha (teeth, hair, an alms bowl). Polo passed Ceylon on his return voyage, c. 1292–93; the Ceylon notice may also draw on earlier reports.

WHAT MY BASE TEXT SAYS, AND WHY IT IS A PROBLEM. Yule's note: "The native king at this time was Pandita Prakrama Bahu III., who reigned from 1267 to 1301 at Dambadenia." Cordier's 1920 Addenda give a different list: "Pandita Prakama Bahu II., who reigned from 1267 to 1301 at Dambadenia (Marco Polo's time); Vijaya Bahu IV. (1301–1303); Bhuwaneka Bahu I. (1303–1314); Prakama Bahu III. (1314–1319); Bhuwaneka Bahu II. (1319)." So my base text calls the same king both II and III. Yule also reports Sir Emerson Tennent's suggestion that Sendemain is CHANDRA BANU, a Malay (Javaka) chief who invaded Ceylon twice in this reign, and offers a Tamil chief of the north as the other choice ("the first part of the name may have been either Chandra or Sundara"). My draft currently says "Parākramabāhu III". I suspect both 19th-century lists are superseded, but I have not seen a modern chronology.

QUESTIONS
1. The modern regnal chronology of the Sinhalese kings from about 1230 to 1330 (Dambadeniya, Yapahuwa, Kurunegala): each king's name, regnal number and reign dates as current scholarship gives them. Where the authorities disagree, give each one's dates.
2. Who reigned in the Sinhalese kingdom (a) in 1284 and (b) in 1292–93? Was any part of the island then under another power (a Pandyan occupation, the Jaffna kingdom, a Javaka/Tambralinga presence)? Who ruled each part?
3. Why do Yule and Cordier number the king differently? Which older chronology (Turnour, Tennent, Wijesinha's Mahavamsa, others) does each follow, and how does the modern numbering differ from both?
4. Chandrabhanu of Tambralinga: the dates of his invasions of Ceylon, and when he disappears from the record. Could he be Polo's Sendemain in the 1280s–90s, on modern dates? Say yes, no or unknown, with the evidence.
5. Every proposed identification or etymology of "Sendemain / Sendernaz": what Paul Pelliot (Notes on Marco Polo, entry for the name), Moule–Pelliot (1938) and later scholars say. Include any Pandyan candidate (e.g. a Sundara Pandya) if one has been proposed, and say who proposed it.
6. Kublai's relic embassy of 1284: is it in the Yuan shi or another Chinese source, and is it in the Sinhalese chronicle (Cūlavaṃsa)? Does either source name the Sinhalese king who received it?

SOURCES TO PREFER: the Cūlavaṃsa (Geiger's translation, 1929–30, with its chronological tables); University of Ceylon, History of Ceylon, vol. 1 (1959–60); K. M. de Silva, A History of Sri Lanka; Amaradasa Liyanagamage, The Decline of Polonnaruwa and the Rise of Dambadeniya (1968); S. Paranavitana and C. W. Nicholas; Pelliot, Notes on Marco Polo; Moule–Pelliot (1938); recent peer-reviewed work on Sri Lanka and the Yuan.

BOOK SECTIONS (use these IDs): III-04 (Ceylon chapter: the king's Note and the relic-embassy Note), F-44.

OUTPUT FORMAT (required). (1) A findings table with columns: `#` · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. **Rules:** do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as **NEW**.
```

```text
BATCH B — The Rāma Khamhaeng inscription and Marco Polo's "Locac"

I am preparing a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920) for print. One endnote says, of Polo's kingdom of LOCAC (Book III, chapter 7: a kingdom about 500 miles beyond the islands of Sondur and Condur, south of Chamba, rich in brazilwood, gold and elephants, "a very wild region"), that "the Rāma Khamhaeng inscription, c. 1292–93, is almost coeval". My base text does not mention the inscription, and I have no source for the date or for the claim. I need to know whether the sentence can stand, and in what form.

QUESTIONS
1. Sukhothai Inscription No. 1 (the "Ram Khamhaeng inscription"): what date does the text itself give, in which era, and what is that in CE? When and by whom was the stone found or brought to notice?
2. The authenticity controversy: who argued that the inscription is a later (19th-century) composition, when, and on what grounds; who answered, and with what evidence (epigraphic, linguistic, physical analysis of the stone)? What is the position of current scholarship? Name each side's proponents and their main publications (e.g. the essays collected in James R. Chamberlain, ed., The Ram Khamhaeng Controversy, 1991).
3. Given 1–2, is it accurate to call the inscription "almost coeval" with Polo's notice of the 1290s? Suggest the most cautious accurate wording, or say the sentence should go.
4. Does anyone connect the inscription, or Sukhothai, with Polo's Locac? Who, and how? Separately, list the main identifications of Locac (Lavo/Lopburi via Chinese Luohu; Ligor/Nakhon Si Thammarat; Langkasuka; the peninsula in general; a confusion with Siam/Xian) with one proponent each. A full survey is not needed: this question is only to see whether the inscription has any place in the Locac argument.
5. Contacts between the Yuan court and Sukhothai or Lavo in the 1280s–1290s (embassies in the Yuan shi): dates and the Chinese names used. These could replace the inscription as the "coeval" evidence in the Note.

SOURCES TO PREFER: Chamberlain (ed.), The Ram Khamhaeng Controversy (1991); A. B. Griswold and Prasert na Nagara, Epigraphic and Historical Studies (Journal of the Siam Society); Michael Vickery; Piriya Krairiksh; Chris Baker and Pasuk Phongpaichit, A History of Ayutthaya / A History of Thailand; Paul Wheatley, The Golden Khersonese; Pelliot, Notes on Marco Polo (entry "Locac"); Geoff Wade's translations of Chinese sources on Southeast Asia; recent peer-reviewed work.

BOOK SECTIONS (use these IDs): III-02 (Chamba–Java chapter, the Locac Note), F-43.

OUTPUT FORMAT (required). (1) A findings table with columns: `#` · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. **Rules:** do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as **NEW**.
```

```text
BATCH C — The War of St Sabas at Acre, and the Mamluk sultan Baybars

I am preparing a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920) for print. Two dates in the front matter and the Notes go beyond my base text, and my base text disagrees with them. I need the modern dates, each from a named source I can check.

PART 1 — THE WAR OF ST SABAS. My draft says: "The War of Saint Sabas (1256–1270) around Acre". Yule says only: "A dispute which broke out at Acre in 1255 came to a head in a war which lasted for years, and was felt all over Syria. It began in a quarrel about a very old church called St. Sabba's, which stood on the common boundary of the Venetian and Genoese estates in Acre... Venice at this time generally kept the upper hand, beating Genoa by land and sea, and driving her from Acre altogether. Four ancient porphyry figures from St. Sabba's were sent in triumph to Venice, and... still stand at the exterior corner of St. Mark's."
1. When did the dispute begin (1255 or 1256), and when did open war begin? What was the trigger?
2. The main events: the fighting in Acre, the naval battle off Acre (1258?), the Genoese expulsion and move to Tyre.
3. When and how did it end? Was there a truce or peace in 1270 (e.g. through Louis IX or at Cremona), or a different date? Did fighting between Venice and Genoa in the Levant continue after it? Give the date a careful historian would print as the end, or say that no single end date is agreed.
4. Yule's "four ancient porphyry figures from St. Sabba's" at St Mark's: does modern scholarship accept that they came from Acre? Distinguish the porphyry Tetrarchs from the two "pilastri acritani", and give the current view of each one's origin with its evidence.

PART 2 — BAYBARS (al-Malik al-Ẓāhir Rukn al-Dīn Baybars al-Bunduqdārī). Yule says he "became the fourth of the Mameluke Sultans, and reigned from 1259 to 1276", and that excess of kumiz killed him. My draft says "r. 1259/60–1277", and my character registry says "c. 1223 – 1 July 1277; Mamluk sultan 1260–77". None of these modern dates is sourced.
5. The exact date of his accession (and the event: Qutuz's murder after ʿAyn Jālūt), and the exact date and place of his death, in both Hijri and Common Era reckoning.
6. The cause of death as the sources give it: kumiz, poison (and the story of the poisoned cup), illness. Name the source for each version.
7. Is "fourth of the Mameluke Sultans" right? Count the Bahri sultans before him, as modern historians list them.
8. His birth year: what range do the sources support?
9. Three dates my chapter takes from Yule, to confirm: Baybars's invasion of Cilician Armenia in 1266; his second invasion, burning Ayas and Sis, in 1275; and his appearance at Damascus in September 1271 (with Mongol pressure in northern Syria that autumn).

SOURCES TO PREFER: Frederic C. Lane, Venice: A Maritime Republic (1973); Steven A. Epstein, Genoa and the Genoese, 958–1528 (1996); David Jacoby's articles on Acre and the Italian communes; Jonathan Riley-Smith; the Annales Ianuenses (Caffaro's continuators) and Martin da Canal's Estoires de Venise as primary sources; Peter Thorau, The Lion of Egypt (1992); P. M. Holt; Reuven Amitai-Preiss, Mongols and Mamluks (1995); Ibn ʿAbd al-Ẓāhir and al-Maqrīzī's Sulūk (Quatremère's translation); the Encyclopaedia of Islam (2nd and 3rd editions), "Baybars I"; Otto Demus on the sculpture of St Mark's; recent peer-reviewed work.

BOOK SECTIONS (use these IDs): I-F1 (front matter: St Sabas), I-03 (the second setting forth: Baybars and the 1271 alarm), CHR (character registry: Baybars), F-38, F-39.

OUTPUT FORMAT (required). (1) A findings table with columns: `#` · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. **Rules:** do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as **NEW**.
```

## Intake notes (for me)

- **A:** if the modern chronology puts a different king in 1284 or 1292–93, F-44 records both Yule–Cordier numberings and the modern one, and says which the Note follows (README, *Newer than Yule*). Also check III-04's relic-embassy Note [16] against question 6.
- **B:** superseded: Yule himself dates the inscription (refs/yule-vol2.txt:15133–15159), so F-43 keeps it, credited and hedged (2026-11-10).
- **C:** question 4 is enrichment, not a fix. Nothing in the chapters claims the porphyries' origin yet; log the answer in `registry/enrichment.md` (I-F1) rather than facts.md. Question 9 rechecks Yule dates that I-03 already uses; a mismatch there gets a new row.

## Intake (2026-11-03)

Runs A–C came back (Consensus plus a second tool each; raw in `results/FACT-*-raw.md`). Leads are written into F-38, F-39, F-43, F-44; no verdict moved. Spot-check failed for several Consensus citations: the DOIs given for "Jay 1993" (a Nias review), "Irvine 1990" (a Ṣanʿāʾ review), "Yoshimura 2020" and "Sharon 2025" resolve to unrelated works; "Hsia 2026" is unconfirmed. Do not use them. Enrichment lead for I-F1: the porphyry Tetrarchs and the *pilastri acritani* are Constantinopolitan spolia of 1204, not Acre (both runs; Perry 1977). Next: the open-access checks named in each row.

**Round 3 (2026-11-10).** A third run of each batch came back (appended to each raw file). It settled no verdict but changed three things: F-43 is Yule's own claim (refs/yule-vol2.txt:15133–15159), regraded from "not in refs"; F-39's cause of death is now disputed (illness, per Ibn ʿAbd al-Ẓāhir, against poisoned kumiz); and F-44's 1292–93 king is less certain (one run gives Parākramabāhu III c. 1302–10). Unused sources went to `registry/enrichment.md` § 5 (E59–E64). Batches A–C are closed; the open rows wait on the library checks in S-06.
