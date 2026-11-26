# S-15 — Final external research intake

_2026-11-11. The user pasted the final research tool's response in this conversation in response to `research/S-15-final-deep-research-prompt.md`; this note records its disposition and independent checks. It is a synthesis, not a verbatim copy. See also `S-15-external-intake.md` and `S-15-other-claims-intake.md`._

## Verdict

**No decisive findings from the external run.** The tool reports that its retrieval context did not contain the requested wills, editions or case records. Its candid NOT SEEN labels are useful, but a source absent from that tool's context is not absent from the project or the web. Do not downgrade sources previously read here, and do not import the unrelated references in its automatically appended bibliography. The report's claim that a 1293 Persian arrival and a 1295 Venetian return conflict is unsupported: those statements can describe consecutive stages of one trip and do not establish incompatible dates.

## Comparison with sources actually available here

| Question | What the final tool could not see | Status after this intake |
|---|---|---|
| Yule's Maffeo date | Yule §49 | Already read in local `book/refs/yule-vol1.txt:8538–8545`: his report gives 6 Feb 1308 Venetian style = 1309 modern. This must still be compared with Gullino's 1310 will; the underlying 1328 act and Orlandini's will transcription are not seen. |
| Jacoby / Burgio / Bruno | All three | Jacoby and Bruno were read directly, Burgio's quotation of Bolognari–Simion was read directly. Earlier source-access labels and the competing claims remain as in `S-15-external-intake.md`; the final tool did not independently settle the will. |
| Bellela | Gallo, Gullino and modern scholarship | [Bolognari 2020](https://iris.unive.it/retrieve/e4239ddd-b4f5-7180-e053-3705fe0a3322/Conte_Montefusco_Simion_Ad_consolationem_legentium_Marco_Polo_ECF_2020.pdf) p. 19, seen, reports 1326–27 documents for masses after Bellela's death and identifies her as wife of Bertuccio Querini, citing Gallo. Gullino and Burgio were also seen. Do not substitute Wikipedia as primary evidence. The original 1326–28 texts and exact death-date reconciliation remain open. |
| Agnese | Bolognari 2021 and 1319 will | Still not seen. Ca' Foscari's institutional report and Orlando 2025 have been seen; identification with the traveller is possible and not upgraded. |
| Marco's will: number 33 | Marciana catalogue | **New correction to our own earlier intake.** [Bartoli Langeli's 2019 critical edition in Plebani's collection](https://www.academia.edu/38270090/IL_TESTAMENTO_DI_MARCO_POLO_Il_documento_la_storia_il_contesto_a_cura_di_Tiziana_Plebani), p. 19, was found as an author-posted accessible text and read: it designates the original *Cod. Lat. V, 58 (=2437), n. 33*. The collection's conservation chapter describes the assembled volume as Lat. V, 58–59 (=2437–2438). Thus use the editor's **no. 33**, not our unsupported expansion “folio 33”; Gullino's “c. 33” is a different notation. The original parchment and live Marciana catalogue were not inspected, so no claim about every catalogue convention follows. |
| Will text itself | Will and diplomatic text unavailable to final tool | Bartoli Langeli's interpretative transcription is actually accessible in the cited 2019 collection; its opening identifies 9 January 1324 in modern dating, the surviving date 1323 and the location Rialto. The edition was read, not the original manuscript. Its publication corrects the earlier status “Plebani 2019 not seen.” |
| Malibran | Agazzi–Cester 2024 | The university repository abstract was previously read. The full archaeological study remains unseen; the report's NOT SEEN remains valid for the actual study. |
| Famagusta / October 1298 | Both documents | Still unresolved. Bruno cites a 1294 Famagusta will and a contested identification; 1293 versus 1294 and the underlying wording require the scholarly edition. No primary document placing this Marco physically in Venice in October 1298 has been found. |

## Practical retrieval and bibliographic caution

1. The University of Pennsylvania's [serial record](https://onlinebooks.library.upenn.edu/webbin/serial?id=archvenetrent) points to Biblioteca Nazionale Centrale di Roma holdings for *Archivio Veneto-Tridentino* vols. 1–10 (1922–1926). It is a **retrieval lead**, not a verified open scan of volume 9 or doc. 6. Also request an interlibrary scan of the 1926 offprint, pp. 25–31, or the ASVe Pietro Pagano protocol.
2. Citations disagree on Orlandini's given name: Moule's 1932 [Cambridge reference](https://www.cambridge.org/core/journals/journal-of-the-royal-asiatic-society/article/abs/marco-polo/37F002C7C88F56B82F31444E76E69E0C) and the CNR's [historical Italian bibliography](https://iris.cnr.it/retrieve/818ac519-34ef-4d98-ba42-ee03945d52de/prod_437185-doc_156668.pdf) say **Giovanni**; the Plebani collection and other modern authors print **Giuseppe**. The 1926 [contemporary review](https://www.persee.fr/doc/bec_0373-6237_1926_num_87_1_460522_t1_0398_0000_002) gives only **G.** Until the title page or an authoritative name record is checked, request and cite **G. Orlandini**, and keep the existing BibTeX expansion flagged rather than silently changing it.
3. Request Gallo 1957–58, pp. 320–321, and the 1326–28 case records; Bolognari 2021, pp. 745–758, and the Agnese will; then the Famagusta edition. Prioritize exact clauses, context and identification rather than another generic search run.

## Applied

- `registry/facts.md` S15-F7, `characters.yaml` Peter, the will illustration plan, III-10 and CHR handoffs now use **no. 33** with Bartoli Langeli 2019; they no longer claim a folio from the critical edition.
- Added `bartoli2019edizione`, corrected `plebani2019testamento` to an edited collection and updated `bartoli2019leggere` access status. The 2019 critical edition—not the archival original—was read.
- The saved final prompt is annotated with the shelfmark discovery and uses G. Orlandini pending a title-page check.
