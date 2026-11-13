# S-15 — Venice, Genoa and the Polo family record

**Status:** closed with documented follow-ups (2026-11-11) · **Phase:** R (research + intake) · **Timebox:** 1 external run + 1 intake session · **Gates:** I-01, I-02, III-10 `.T1`/`.T4`; `CHR` registry (family members); `PLT` will-plate caption; `DIA` B-timelines (family dates)

## Question
What does the documentary record say about Marco Polo, his family, his capture, his collaborator and his last years? Which of the book's biographical statements rest on documents, which on Ramusio's later stories, and which on modern inference?

## Why it matters
- I-02 credits "the book" with a biography that comes from Venetian records and Yule's Introduction.
- I-01 and III-10 mix Jacopo d'Acqui, Ramusio's novella (the homecoming feast, the seams of jewels) and archival fact without separating them.
- The family appears in the character registry (S-05) and on plates, so the names and dates must be right before anything is drawn.

## Inputs
- `vol-1/ch-01-genoa-prison.md`, `vol-1/ch-02-house-of-polo.md`, `vol-3/ch-10-ca-polo-milione.md` and their Notes
- Chapter backlogs I-01, I-02, III-10; `tasks/cross/CHR-characters.md`
- Yule's Introduction in `refs/yule-vol1.txt`
- **Handed over from S-05 (`CHR.T7`):** the family facts two people-research runs left open: Maffeo's marriage, Bellela's husband, the daughter Agnese (Bolognari 2021), any document for Marco's 1254, Rustichello's lay status, the will's shelfmark. What is already settled is in `registry/characters.yaml` and `research/results/CHR-people-2-intake.md`; don't re-research it.

## Method
1. Run the prompt and save the output to `research/results/S-15-raw.md`.
2. Intake: trust checks; write family facts to `registry/facts.md` and anecdotes to `registry/enrichment.md`, each tagged *document* / *Ramusio-tradition* / *modern inference*.
3. Feed the person records to S-05 (character registry).

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). I need the documentary record of the Polo family and Polo's life in Venice and Genoa, separated cleanly from later legend. For every item, classify the evidence as DOCUMENT (archival record, with archive and shelfmark if known), EARLY TESTIMONY (e.g. Jacopo d'Acqui, Pipino, Pietro d'Abano), RAMUSIO TRADITION (Ramusio's 1559 preface and anecdotes), or MODERN INFERENCE (and whose).

1. THE FAMILY. Andrea Polo and his sons Marco "the elder", Niccolò and Maffeo; the Constantinople and Soldaia (Sudak) houses; Marco the elder's 1280 will. Niccolò's wives and children (Marco's mother; Niccolò's later sons Maffeo, Giovannino, Stefano). Maffeo's will (1309/1310?) and whether he married. Marco's wife Donata Badoer and the date of the marriage; the daughters Fantina, Bellela and Moreta, and their marriages.

2. MARCO'S BIRTH AND THE "1254" DATE. What is the basis for 1254? Is his birth in Venice certain? (The Korčula/Curzola birth claim: origin and status.)

3. CAPTURE AND PRISON. The competing accounts: the battle of Curzola (Korčula, 1298) per Ramusio, against Jacopo d'Acqui's account of a skirmish near Ayas (Laiazzo), and modern views. The Genoa–Venice peace of 1299 and the release of prisoners. What is known of where he was held (the Palazzo San Giorgio claim).

4. RUSTICHELLO DA PISA. Identification with the Arthurian compiler "Maistre Rusticien de Pise". His captivity in Genoa (since the battle of Meloria, 1284?). His share in the text: current scholarly views.

5. CA' POLO AND THE "MILIONE" NICKNAME. Location of the Polo house (Corte del Milion, San Giovanni Grisostomo; the later Teatro Malibran site). Archaeological or architectural findings at the site. The origin of "Il Milione" as nickname or book title (Emilione? hyperbole?), with the earliest attestations.

6. LATER LIFE. Documents of Marco's business in Venice 1300–1324 (lawsuits, e.g. over musk with Paulo Girardo; property; his brother-in-law). The 1324 will: date, content, the freeing of his Tatar slave Pietro, its archive and shelfmark. The 1366 inventory of his possessions (or whatever the inventory's date is): what it lists (Mongol items, a paiza/golden tablet?). Burial at San Lorenzo, and what is known of the tomb.

7. ANECDOTES TO SORT. Classify each as document, early testimony, Ramusio tradition or legend: the returning Polos unrecognised in Tatar clothes and the feast where jewels are cut from the seams; the deathbed request to recant and "I did not tell half of what I saw" (source: Jacopo d'Acqui?); Marco's portrait(s) — is any portrait authentic?; Marco the elder's ship and the brothers' 1260 departure from Constantinople.

8. NEW FINDS. Any documents found or re-read since 2000, including work for the 2024 anniversary (e.g. by the Archivio di Stato di Venezia or the Biblioteca Marciana; name the scholars and their publications; Alvise Zorzi's biography is the older benchmark).

Book section IDs: I-01 (Genoa prison and composition), I-02 (the House of Polo; the brothers' first journey), III-10 (Ca' Polo, later life, the will), III-11 (afterlives), III-B1 (trivia).

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [x] `research/results/S-15-raw.md` saved
- [x] Family and biography rows in `registry/facts.md`, each with an evidence class
- [x] Anecdotes in `registry/enrichment.md` (I-01, I-02, III-10), each with an evidence class
- [x] Person records handed to S-05

## Feedback to plan
- `illustration-plan.md`: captions for the will and homecoming plates
- `tasks/cross/CHR-characters.md`: family entries

## Follow-up prompts
Best-effort research is complete; no further general search or deep-research run is needed. Remaining source-level checks are Maffeo’s 1309/1310 will dates and possible children, Agnese’s identification, Bellela’s exact death date, Rustichello’s lay status, the Famagusta/1298 chronology, and the full Malibran report. These require the named editions, archival documents, or library access; use the hedges in `registry/facts.md` and `research/results/S-15-final-intake.md` meanwhile. The 2024 inventory edition does contain the gold command tablet (S15-F8); its identification as a paiza is attributed to Burgio.

## Findings
See `research/results/S-15-raw.md` and `registry/facts.md` S15-F1–F10. Distinguish reports, records, narrative witnesses and inference. Agnese’s identification is possible, not established; 1324 inventory survives in the 1366 judgment; the will is Cod. Lat. V, 58 (=2437), no. 33 in the 2019 critical edition; 1309 and 1310 will evidence needs comparison.

## Decision
**Best effort done; S-15 is closed.** The final external run did not obtain the decisive documents, and the remaining archival questions stay unresolved rather than blocking the project. Use the explicit hedges and evidence classes; `CHR.T7` retains source-level checks if the named works become available. Chapter, plate, timeline and character backlogs have received the findings; narrative revisions remain their existing downstream tasks.

## Tasks to create on close
- Existing `I-01.T1`, `I-02.T1`, `III-10.T1`/`.T4` updated; `CHR.T7` retains open source checks; `DIA` B-timeline and plate caption handoffs added.


## External research intake (2026-11-11)

User-supplied research preserved as `research/results/S-15-external-raw.md`; source checks and accepted/rejected claims are in `S-15-external-intake.md`. Corrects the initial intake on Maffeo's marriage (Marta, via Burgio), Bellela's husband (Bertuccio Querini, Bolognari 2020 citing Gallo), Andrea's Ramusian provenance, and the gold tablet in the 2024 critical edition. Children and 1309/1310 remain unresolved; the external report's calendar-only explanation does not match Yule's stated 1308 Venetian-style date. Relevant registries and backlogs updated.

## Final targeted research and source sweep

The copy-ready follow-up is `research/S-15-final-deep-research-prompt.md`: it asks for direct readings of the uncle's will, Agnese and Bellela documents, disputed 1298/1293–94 chronology, and a small number of archival checks. The check of other useful sources is `research/results/S-15-other-claims-intake.md`; findings S15-H1–H7 are in `registry/enrichment.md` and relevant chapter and timeline backlogs.

## Final external run intake

The final tool found none of the priority editions in its retrieval context; `research/results/S-15-final-intake.md` compares that limited result with sources previously seen here. During intake we located Bartoli Langeli's 2019 will edition: the original is cited as Marciana Cod. Lat. V, 58 (=2437), **no. 33**. This corrects our earlier “folio 33” wording. The uncle's will, Agnese, Bellela death-date and Famagusta questions remain open for source-level inspection.


## S-20 cross-reference (2026-11-13)

The 1319 confraternity entry is identified as the traveller by Pozza as reported independently by Bolognari and Vogel (S15-H3; S20-E43). The 1305 namesake is not an unqualified identification, and neither attestation establishes the nickname’s origin. The explanations in S20-E27/E43 are attributed and the “million lies” chronology is unverified. For the Korčula claim, Orlić studies a modern invented tradition rather than proving a medieval birthplace (S20-E19). See [S-20 closure](../research/results/S-20-closure.md); S-15 remains closed.
