# S-15 — Venice, Genoa and the Polo family record

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** I-01, I-02, III-10 `.T1`/`.T4`; `CHR` registry (family members); `PLT` will-plate caption; `DIA` B-timelines (family dates)

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
- [ ] `research/results/S-15-raw.md` saved
- [ ] Family and biography rows in `registry/facts.md`, each with an evidence class
- [ ] Anecdotes in `registry/enrichment.md` (I-01, I-02, III-10), each with an evidence class
- [ ] Person records handed to S-05

## Feedback to plan
- `illustration-plan.md`: captions for the will and homecoming plates
- `tasks/cross/CHR-characters.md`: family entries

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `I-01.T1`, `I-02.T1`, `III-10.T1` (biography by evidence class); `CHR.T*` family rows; `DIA` B-timeline data
