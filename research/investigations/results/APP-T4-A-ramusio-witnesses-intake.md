# APP.T4 batch A — Ramusio witnesses intake (2026-11-18)

The batch A return for [APP-T4-ramusio-witnesses.md](../prompts/APP-T4-ramusio-witnesses.md) (Prologue and Book I, 27 passages) is preserved unchanged as [raw](APP-T4-A-ramusio-witnesses-raw.md). The user did not say which tool or model produced it. It read machine extracts only: publisher PDFs of Eusebi's F and Simion's V, OCR of Moule–Pelliot vols. 1–2 and of Ramusio 1559, and Wikisource. It saw no page images, could not open the digital Ramusio, and marks every TA, VA, P, L, VB and FB reading as inferred from OCR sigla.

## Spot check: 10 propositions, 10 hits (100%, above the 80% threshold)

The F and V editions were downloaded from Edizioni Ca' Foscari and read as text (`pdftotext`). Yule's note was read in `refs/yule-vol1.txt`. **Moule–Pelliot vol. 2 (the Z transcription) could not be opened:** NII Digital Silk Road returns HTTP 403 to scripted fetches and to the in-app browser, and archive.org has only vol. 1. **No Z reading was seen at intake.**

| # | Source opened | Proposition | Result |
|---|---|---|---|
| 1 | F, Eusebi ed., ch. XLVI § 13 | Badakhshan horses are great runners, unshod, always in the mountains; nothing on steep descents (#12) | **Hit** |
| 2 | F, ch. XLIX § 9 | A plain between two mountains with a fine river and the best pasture; no lake (#14) | **Hit** |
| 3 | V, Simion ed., 26.16 | Plain between two mountains with two rivers and the best pasture (#14) | **Hit** |
| 4 | V, 26.17 | Horns of the wild oxen made into bowls; no horn-and-bone heaps (#15) | **Hit** |
| 5 | V, 28.3 | Most people have a goitre under the throat (#16) | **Hit** |
| 6 | V, 28.8 | Cotan: cotton and wine "chomo in le nostre parte" (#17) | **Hit** |
| 7 | F, ch. LIII §§ 2–8 | Cotan: Muslim, cotton, vineyards, gardens, trade and crafts, not men of arms; no flax, hemp or wheat (#17) | **Hit**, and wider than the return says: F carries most of the bracket |
| 8 | V, 30.8–9 | Spirit sounds like bells; bells on the animals' necks (#19–20) | **Hit** |
| 9 | F, ch. LXXIV §§ 9–13; V, 39.5–6 | Cane palace gilt inside, varnished cane roof, canes cut knot to knot (F); marble, varnished columns, split-cane tiles, two hundred silk cords, no dragons, no wind (V) (#25–27) | **Hit** |
| 10 | Yule I.61, note 4 (`refs/yule-vol1.txt`) | "Ramusio's is here so much more lucid than the other texts, that I have adhered mainly to his account of the building" | **Hit**, verbatim in the 1903 text |

## Applied 2026-11-18 (only readings seen at intake)

The label "Ramusio-only in part: <details>." now marks a passage whose core stands in an older witness (`VOICE-GUIDE.md`, *Ramusio and later layers*). Each Note names what the older witness has and cites the edition by chapter and section, not page.

| Passage | Change |
|---|---|
| #12 I-09 Note [10] | In part: the pace down steep descents; F has the unshod mountain runners. |
| #14–15 I-10 Note [3] | In part: the lake and the horn-and-bone heaps; F and V have the plain, river and pasture, V the horn bowls. Flag moved to the lake. |
| #16 I-10 Note [13] | In part: cotton, craftsmen and the water cause; V has the goitre. Flag narrowed. |
| #17 I-10 Note [14] | In part: flax, hemp and wheat; F has the rest of the Cotan notice, V the wine. Flag narrowed. |
| #24–27 I-13 Note [4] | In part: the grove, the gilt dragons and the nailed tiles; F and V carry the palace, roof, columns, canes and silk cords. Three flags placed. Yule's note 4 cited. |

## Second pass, 2026-11-18: held rows settled

Moule–Pelliot vol. 2 stays unreachable (NII DSR refuses automated access; it was not worked around). Instead, the intake read **Moule–Pelliot vol. 1 page images** (archive.org `descriptionofwor01polo`, leaf = printed page + 7), whose italics and margin sigla name the witness for each non-F reading, and **Simion's V text** for chapters 11–26. Every row below was seen at intake.

| # | Seen | Verdict | Applied |
|---|---|---|---|
| 1 | MP1 p. 87: the perils-of-the-way sentence is italic under R | R only | no change (I-03 [16]) |
| 2 | MP1 p. 97: unclimbable, never-melting snow = Z; grassy slopes, flocks, mud = R | Z + R, R-only part | I-04 [7] "Zelada- and Ramusio-only in part" |
| 3 | MP1 p. 99: sturgeon and salmon = Z (and L); V 12.4 sturgeon; no river-mouths | R-only part | I-04 [13] "in part: at the river-mouths" |
| 4 | V 13.9: "Masa Meredimi", cotton, buckram, merchants and craftsmen, subject to the Tartars | also in V, whole | I-05 [3] "Not Ramusio-only"; flag reworded |
| 5 | V 16.9: "da questa Toris fina in Persia sono dodexe zornade" | also in V, whole | I-06 [3] "Not Ramusio-only"; flag reworded |
| 6 | MP1 p. 117: objection and boiled wine = Z | Z + R | I-06 [15]; flag names the Zelada Latin |
| 7 | MP1 p. 120: turtledoves = Z | Z + R | I-07 [4]; flag |
| 8 | MP1 p. 125: army killed by the wind = R; V lacks it | R only | no change |
| 9 | MP1 p. 125: hired wailers = Z | Z + R | I-07 [14]; flag |
| 10 | MP1 p. 127: underground river = R | R only | no change |
| 11 | V 21.10: "feze spianare quel chastelo"; MP1 p. 133: destruction LT, levelling V | R-only part: the garden | I-08 [12] "in part" |
| 13 | MP1 p. 140: no killing = Z; V 26 lacks it | Z + R | I-09 [15]; flag |
| 14–15 | MP1 pp. 141–142: lake = TA and R; wolves = Z; horn-and-bone mounds = R | R-only part narrower | I-10 [3] adds TA and Z |
| 22 | MP1 p. 158: herb, hooves, native beasts = Z; travellers' rule = R | Z + R, R-only part | I-11 [14] "Zelada- and Ramusio-only in part" |
| 23 | MP1 p. 170: the high God with censer and incense = R | R only | no change (I-12 [15]) |
| 24 | MP1 p. 185: "where there is a most beautiful [grove]" under V R / VB L; not separable | cannot tell | no change |
| 26–27 | MP1 p. 186: dragons = R; nails against the wind = L and R; wind clause = R and P | R-only part narrower | I-13 [4] adds L and P |

Sigla readings depend on Moule–Pelliot's line-by-line convention (each siglum names the next italic segment starting on that line); where a line holds several segments the attribution is the intake's reading of that convention. `VOICE-GUIDE.md` now defines "Not Ramusio-only: <witness> has it" for passages an older witness carries whole.

### Third pass, 2026-11-18

| # | Seen (MP1 page image) | Verdict | Applied |
|---|---|---|---|
| 12 | p. 137: the gallop over slopes where other animals cannot = R; P has only the unhurt feet | R-only part confirmed | no change (I-09 [10]) |
| 16 | p. 146: cotton and craftsmen = R; one foot large = Z; swollen legs = R; lump in the throat = L; water cause = R | R-only part confirmed; throat also in L | I-10 [13] adds L |
| 17 | p. 146: flax and hemp = L; oil and wheat = VL; corn and wine = L | also in older witnesses | I-10 [14] "Not Ramusio-only"; flag names the Latin texts |
| 20 | p. 150: not straying = LT; bells on the necks = V; bells against wandering = L; company and night mark = R | R-only part: the night signal | flag moved to the signal (no Note) |
| 21 | p. 155: Mangu's order is in F; the public lodgings = P | Pipino and Ramusio | I-11 [10] "Pipino- and Ramusio-only"; flag moved to the lodgings |
| 24 | p. 185: the grove line carries V R, the next VB L; not separable | cannot tell | no change |

**Batch A is closed (best effort).** Every passage has a verdict from a source seen at intake except #24, whose sigla cannot be separated. Not consulted: the digital Ramusio's source notes (robots-blocked), Benedetto's apparatus, Moule–Pelliot vol. 2 (DSR refuses automated access).

## Held after the first pass (superseded above)

- **Z readings (#2, 3, 4, 6, 7, 9, 13, 15 wolves, 22):** not seen. Labels stay "Ramusio-only." until a person opens Moule–Pelliot vol. 2 (DSR images 0032–0047, or a library copy) and confirms the quoted Latin. If confirmed, relabel "Zelada- and Ramusio-only." (or "in part" where V or F also carry a share).
- **V readings inferred from Gennari–Burgio (#3, 4) and sigla-only witnesses (#21 VA; TA, L, P, VB, FB anywhere):** not seen.
- **Cannot tell (#1, 5, 10, 11, 23, 24 grove, 27 wind):** no change; the return's cheapest checks (MP1 page images, the digital Ramusio's source notes) stand as the follow-up.
- **R only (#8, 18, 19):** consistent with F and V as read here; no change needed.
- **#20 (keep together; bells; signal)** has no Note; V's bells sit in the same paragraph as #19. No change.
- The return's gloss hypotheses are its own inferences, not published claims; none enters the book.

## Follow-ups (closed best effort 2026-11-18)

Declared closed by the project owner. Not done, and not pending:

1. Moule–Pelliot vol. 2 (Z transcription) was never opened; the Z rows rest on vol. 1's sigla.
2. Batches B and C of the prompt were not run; those passages keep Yule's brackets as their label.
