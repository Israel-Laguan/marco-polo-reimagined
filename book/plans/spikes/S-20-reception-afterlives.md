# S-20 — Reception and afterlives: manuscripts, print, maps, myths

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** III-11 and III-B1 `.T1`/`.T4`; I-B1 and II-B1 trivia; `DIA` B5 (reception timeline); `PLT` reception plates (Columbus postils, Fra Mauro, Catalan Atlas)

## Question
What is the verified history of the book's transmission and reception, from manuscripts to print, cartography, exploration and modern culture? Which popular "Marco Polo facts" (pasta, ice cream, the deathbed line, the nickname) are myths, and where did each one start?

## Why it matters
- III-11 has unsupported claims: the Catalan Atlas showing Chipangu, the Jesuits measuring Polo's silences, and print dates missing.
- The trivia back matter is the place where readers most often repeat popular myths.
- A dated, sourced reception timeline (B5) needs this data.

## Inputs
- `vol-3/ch-11-afterlives.md`, `vol-3/back-01-trivia-and-afterlives.md`, `vol-1/back-01`, `vol-2/back-01`
- III-11 backlog (M4, M5, m13, n9); `multimedia-plan.md` B5
- S-14 items 19–22 (don't duplicate; this spike widens them)

## Method
1. Run the prompt and save the output to `research/results/S-20-raw.md`.
2. Intake: timeline rows → `registry/facts.md` tagged `DIA-B5`; myths and modern afterlives → `registry/enrichment.md` § reception, each tagged *myth* / *fact* / *disputed*.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). Its final chapters cover the book's afterlife. I need a verified, dated reception history and a myth-check.

1. MANUSCRIPTS. How many manuscripts survive (the usual figure is about 150; give the current count and source)? The main families and their dates: F (BnF fr. 1116), Fr (the Court French, incl. the Thibaut de Cepoy copy given to Charles of Valois in 1307 — verify), TA (Tuscan), VA (Venetian), P (Pipino's Latin), Z (Zelada/Toledo), R (Ramusio). The illuminated Livre des merveilles (BnF fr. 2810, c. 1410–12) and Bodleian MS Bodley 264.

2. PRINT. First editions with dates and places: German 1477 (Nuremberg, Creussner); Latin (Leeu, Gouda, c. 1483–85); Venetian Italian 1496; Portuguese 1502 (Valentim Fernandes); Castilian 1503 (Santaella); Ramusio 1559; first English translation (John Frampton, 1579); Marsden 1818; Yule 1871. Correct and complete.

3. CARTOGRAPHY. Polo's influence on maps: the Catalan Atlas (1375) — which Polo place names it uses, and whether Japan appears; Fra Mauro's mappa mundi (c. 1450–59) and his Polo sources; Martin Behaim's globe (1492); Toscanelli; Waldseemüller (1507); Ortelius; Mercator. When did "Cathay" and "Mangi" disappear from European maps?

4. EXPLORATION. Columbus's copy and postils (number of annotations; famous ones on Chipangu, Quinsay, the Great Khan); Columbus's letters mentioning the Great Khan; Henry the Navigator; the copy the Infante Dom Pedro of Portugal received in Venice in 1428; Bento de Góis and Matteo Ricci (Cathay = China); the Jesuits' and later Western readings of Polo in China.

5. CHINA AND ASIA. When did Chinese scholarship engage with Polo (Zhang Xinglang's 1913–29 translation; Feng Chengjun; Yang Zhijiu)? Modern Chinese, Mongolian and Iranian reception; Polo in Chinese education and diplomacy (Belt and Road references).

6. MYTHS — classify each as myth, fact or disputed, with the earliest source of the claim: Polo brought pasta (spaghetti) to Italy (the 1929 Macaroni Journal story?); Polo brought ice cream; Polo introduced gunpowder, paper money or eyeglasses to Europe; Polo was born on Korčula; "I have not told half of what I saw"; "Il Milione" = "a million lies"; Polo's portrait (authentic?); Marco Polo the swimming-pool game; the "Polo" in sheep (Ovis poli) and other eponyms.

7. MODERN AFTERLIVES. Major works only, with dates: Coleridge's "Kubla Khan" (1797/1816) and its Purchas source; Italo Calvino, Invisible Cities (1972); Eugene O'Neill, Marco Millions (1928); notable films and TV (incl. the 1982 RAI miniseries; Netflix 2014–16); the 2024 anniversary exhibitions in Venice and elsewhere; Marco Polo airport (Venice) and similar; notable recent novels.

Book section IDs: III-11 (afterlives), III-B1 (trivia and afterlives), I-B1 and II-B1 (trivia and disputes), III-12 (reliability essay).

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [ ] `research/results/S-20-raw.md` saved
- [ ] B5 reception-timeline rows in `registry/facts.md`
- [ ] Myth-check table and modern-afterlives list in `registry/enrichment.md` § reception

## Feedback to plan
- `multimedia-plan.md` § B5 (timeline data source)
- `illustration-plan.md`: reception plate captions; PD candidates passed to S-11

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `III-11.T1`, `III-B1.T1`, `I-B1.T1`, `II-B1.T1` (myth-check pass); `DIA.T*` B5 data
