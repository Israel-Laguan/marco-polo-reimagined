# Intake — people deep research, run 3 (S-05 follow-up)

_2026-11-10. Raw run: `CHR-people-3-raw.md` (Consensus; the 8 rows in `CHR-people-2-intake.md` § Still open). Applies to `CHR.T7`; partly to S-14 and S-15._

## Trust check

**Verdict: leads only. No row moves.** The run says so itself: it opened none of the target passages, so nothing is SAW. What it found are abstracts of newer secondary works.

- **Citations (6 of 6 checked):** the 5 DOIs resolve on Crossref, with matching title, author, journal and year: Menshikova 2025, Çelik 2022, Whitfield 2019 (*Oxford Bibliographies in Chinese Studies*, not *West-Eastern Divan* as the run's reference list says), Gertwagen 2001 and Cleaves 1976. Andreose 2015 (*Francigena* 1) has no DOI and was not found on Crossref, so it stays `unconfirmed`. **Hit rate: 5/6 (83%), above the 80% bar.**
- **Cleaves DOI:** `10.2307/2718743` is correct. It was already confirmed in run 2's intake (`cleaves1976chinese`). The run-3 prompt wrongly said it was not. That was a prompt error, not a source problem.

## Leads

| Row | Lead | Source | Status |
|---|---|---|---|
| chabi | Gives 1227–1281; her authority for 1227 was not recovered. No source for 1216 found | `menshikova2025porcelain` (abstract) | lead: one secondary source, basis unknown. Date rule not met |
| dorji | Names Dorji among Chabi's four sons by Kublai; no birth year | `celik2022yuan` (abstract) | lead for the Chabi side of the mother dispute |
| marco | 1254 repeated by Whitfield and by Gertwagen (reviewing Larner); origin not traced | — | adds nothing; not entered |
| rustichello | Andreose's Meloria point concerns Pisan prisoner-scribes' manuscripts, **not** Rustichello's own capture | Andreose 2015 (abstract; unconfirmed) | agrees with the registry ("Yule's conjecture, not a document") |
| maffeo, bellela, peter-the-tartar, coja | nothing found | — | unchanged |

## Applied

- `characters.yaml`: `chabi` and `dorji` name their lead sources.
- `bibliography.bib`: `menshikova2025porcelain` and `celik2022yuan` (confirmed: the DOIs resolve; only abstracts have been seen).
- `enrichment.md` § 2: E22–E25, the by-products (Chabi porcelain, Chabi biography, the Oxford Bibliographies list, the Genoese prison-scriptorium).

## Still open

All 8 rows from run 2 are unchanged. Two search runs have now failed to open these sources, so **do not run a fourth search**. Each row needs a reader with the book, the scan or the catalogue in front of them (*Yuan shi* 107 and 114 on ctext.org; Orlandini 1926; Moule–Pelliot 1938 I; Bolognari 2021; Plebani 2019; the Marciana catalogue; the full text of Cleaves 1976). The rows stay in `CHR.T7` and the S-15 intake.
