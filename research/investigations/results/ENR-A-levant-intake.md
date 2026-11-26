# Intake: enrichment leads, Batch A (Levant)

_2026-11-10. Raw run: `ENR-A-levant-raw.md` (tool not stated; prompt `prompts/ENR-enrichment-leads.md` Batch A). Applies to `registry/enrichment.md` E25, E31, E32, E33, E38, E39, E58._

## Trust check

**Verdict: the run fails the bar. Do not salvage it; re-run (see § Re-run).** It returned no bibliography (contract item 3): its `[[n]]` citations point to a list that is not in the output. It gave no DOIs or URLs except one, which is wrong. Two of its "corrections" are themselves wrong.

**Citations (12 checked against Crossref, Open Library and the live web):**

| Run cites | Check | OK? |
|---|---|---|
| Shotten-Hallel, "Architectural Language of the Hospitaller Church…", *Syria in Crusader Times* (EUP), for the Genoese wall | Exists, but in *Crusading and Trading between West and East* (Routledge 2018), doi:10.4324/9781315142753-8, and it is about the Hospitaller church. The wall comes from Stern et al. 2024 (E30). | no |
| "Jacoby, Michael R.", "The War of Towers: Venice and Genoa at War in Crusader Syria, 1256–8", *Syria in Crusader Times* | The chapter exists, by **Thomas F. Madden**, EUP 2019, pp. 211–224, doi:10.1515/9781474429726-016 | no (author wrong) |
| Epstein, *The Crusades, the Genoese and the Latin East, 1187–1220s* | not found | no |
| Effenberger, "Neues zu den Tetrarchenfiguren in Venedig…", *Millennium* 2013 | not found on Crossref (*Millennium* has DOIs) | no |
| Harrison, "Excavations at Saraçhane", *Annual of the British School at Athens* | The work is a book: Harrison, *Excavations at Saraçhane in Istanbul* 1 (Princeton UP / Dumbarton Oaks, 1986), doi:10.1515/9781400857975 | no (venue wrong) |
| Perry, "Saint Mark's Trophies", *Journal of World History and Culture* | It is *JWCI* 40 (1977), doi:10.2307/750990 | no |
| Wilson, "The Role of Nogai in the Golden Horde: A Reassessment", 2022 | Exists: *Acta Orientalia Acad. Sci. Hung.* 75: 609–637, doi:10.1556/062.2022.00232. The abstract does **not** call Nogai Berke's nephew. | yes (work) |
| Kinoshita, *The World of Marco Polo in Three Portraits* | Exists as an article: "The Painter, the Warrior, and the Sultan…", *Medieval Globe* 2 (2016): 101–128, doi:10.17302/tmg.2-1.6 | yes (title clipped) |
| Gaunt, *Le Devisement dou monde: A Critical Edition* (CUP) | No such edition. Gaunt's book is *Marco Polo's Le Devisement du Monde* (Boydell & Brewer, 2013), a monograph | no |
| Gadrat-Ouerfelli, *Lire Marco Polo au Moyen Âge* (Peeters) | Exists (reviewed in *Romania* 134 and *Studi Francesi* 181); the publisher is Brepols, not Peeters | partial |
| Favereau, *The Horde* (2021) | Exists: Harvard UP, doi:10.4159/9780674259997 | yes |
| Rialfri at `https://www.rpia.unipd.it/` | does not resolve; Rialfri is at `https://www.rialfri.eu/` (HTTP 200) | no |

**Hit rate: 3 of 12 (25%), with one partial.** Far below the 80% bar.

**Its two "corrections" are wrong.** Checked in Caro, *Genua und die Mächte am Mittelmeer 1257–1311*, vol. 1 (1895), IA `genuaunddiemcht00carogoog` (OCR text):

- **Pisa did change sides in 1257.** Caro, p. 32: on 18 July 1257, at Modena, Venice "schliesst … einen zehnjährigen Bund mit Pisa, der ganz offen seine Spitze gegen Genua kehrt". Before that, the Genoese had beaten the Venetians "mit Hülfe der Pisaner" (p. 31). The run's "only after 1291" is false.
- **The "Tower of Flies" (1267) is real.** Caro, p. 201: on 16 August 1267 the Genoese fleet (Luchetto Grimaldi) appears before Acre and plants its banner "auf dem sie beherrschenden Fliegenthurm"; two Pisan ships burn; the harbour is blockaded. Caro cites the *Annales Ianuenses* and Canale. The run called it "a fabrication".

## What the intake saw (one source each; the date rule needs a second)

| Item | Seen in Caro I | Still needed |
|---|---|---|
| E31 | Pisa–Venice league at Modena, 18 July 1257 (p. 32). Tiepolo's fleet breaks the harbour chain and burns the Genoese ships; S. Saba is taken. This is in 1257, in Caro's chapter "Der Krieg mit Venedig 1257" (p. 35), not 1258. The Templars and the Teutonic Order back Venice; the Hospitallers favour Genoa (pp. 39–41). The sea battle off Acre is on 24 June 1258 (contents list: "Die Seeschlacht bei Accon, 1258. 24. Juni"). | A second source for the dates: Madden 2019 (EUP), or the *Annales Ianuenses* (MGH SS 18). Rosso della Turca's name was not found in the OCR; check Caro's battle chapter by eye. The restoration of the Genoese quarter in 1288: not checked (Caro vol. 2). |
| E32 | Tower of Flies, 16 August 1267 (p. 201). | Settepozzi (1263) and Trapani (1266): a second source (Lane 1973; Epstein 1996, both standard, not seen here). Curzola, and the alternative capture at Laiazzo: Jacopo d'Acqui places Marco's capture near Laiazzo; see E11 (`bolognari2024chronica`). |

## Leads worth keeping

- **Madden 2019**, "The War of Towers: Venice and Genoa at War in Crusader Syria, 1256–8", in *Syria in Crusader Times* (EUP), doi:10.1515/9781474429726-016: the modern account for E31. Library.
- **Wilson 2022** (`Acta Orientalia`, doi:10.1556/062.2022.00232) and **Wilson 2022b**, "Nogai the Khanmaker: A Historiographical Problem", *Golden Horde Review* 10: 332–343, doi:10.22378/2313-6197.2022-10-2.332-343 (Crossref), for E39. Nogai's kinship to Berke is still unconfirmed.
- **Harrison 1986** (Princeton) for the Polyeuktos pilasters (E33).
- **Andreose 2015**: Padua's repository lists *Francigena* 1 as object `o:329126` at phaidra.cab.unipd.it. The asset URL returned 404 to scripts. The run's article title is unconfirmed.

## Applied

- `enrichment.md` E25, E31, E32, E33, E39, E58: Status notes updated. No status moves to **verified**, except that E58's URL now resolves. One source in each case does not meet the date rule.

## Re-run

If Batch A is re-run, tell the tool: return the bibliography with a DOI or URL for every work; cite no work it has not opened; and do not "correct" a lead without quoting the passage that contradicts it. Better: get Madden 2019 and the *Annales Ianuenses* (MGH SS 18, open on dMGH) and read them directly. Those two settle E31 and E32 without another search run.
