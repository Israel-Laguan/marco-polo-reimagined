# S-20 — Reception and afterlives: manuscripts, print, maps, myths

**Status:** closed 2026-11-13 · **Phase:** R (research and qualified handoff complete) · **Timebox:** multiple research intakes and independent checks; production tasks remain · **Gates:** III-11 and III-B1 `.T1`/`.T4`; I-B1 and II-B1 trivia; `DIA` B5 (reception timeline); `PLT` reception plates (Columbus postils, Fra Mauro, Catalan Atlas)

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
- S-12 (closed 2026-11-10): the modern editions of each redaction and their keys are in `registry/sources.md` (F, Fr, TA, VA, Z, R). Still open there: the Gallica identifiers of BnF fr. 1116 and fr. 2810. Gallica refused automated requests, so check them in a browser, not with the research tool.
- S-11 ✓ (`registry/pd-sources.md`): the Catalan caravan's inscription says it left "the empire of Sarai" for Cathay; Columbus's copy is photographed open at Abyssinia and Aden; the 1477 woodcut is available in Dibdin's 1822 facsimile; Fra Mauro images from the Marciana carry an Italian heritage fee (Naya's 1873 facsimile does not)

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
- [x] `research/results/S-20-raw.md` saved
- [x] B5 reception-timeline rows in `registry/facts.md`; selected set and qualifications in [closure](../../../research/investigations/results/S-20-closure.md)
- [x] Myth-check table and modern-afterlives selection in [closure](../../../research/investigations/results/S-20-closure.md), grounded in `registry/enrichment.md` § reception

## Feedback to plan
- `multimedia-plan.md` § B5 (timeline data source)
- `illustration-plan.md`: reception plate captions (PD sources settled by S-11)

## Decision and downstream handoff

**Closed with qualified findings and explicit unverified items.** The [closure record](../../../research/investigations/results/S-20-closure.md) selects B5 entries, a myth/afterlife table, wording for the disputed central claims and a proposed Columbus plate caption. The [cross-project handoff](../../../research/investigations/results/S-20-cross-project-handoff.md) routes useful sources to other chapter and spike work. The latest [dossier](../../../research/investigations/results/S-20-final-columbus-raw.md) is preserved; its excerpts are identified as reported where they were not independently accessible. [F-19–F-22](../../../research/registry/facts.md) and the [reception register](../../../research/registry/enrichment.md) record evidence levels.

III-10, III-11, III-B1, DIA-B5 and PLT retain their ordinary implementation and source/rights checks. The current chapter drafts still contain claims slated for correction; closing this spike does not mark those tasks done. The prior [high-priority](../../../research/investigations/S-20-follow-up-prompt.md) and [optional](../../../research/investigations/S-20-optional-follow-up-prompt.md) prompts are archived for context, not active gates or automatic further research. Unverified details must be checked if a later editorial choice requires them.

## Findings
**2026-11-13 — five-claim report checked after closure.** [Raw](../../../research/investigations/results/S-20-five-claims-raw.md); [independent intake](../../../research/investigations/results/S-20-five-claims-intake.md). Gil 2006 identifies specific folios and provides an attributed argument linking Day’s Polo book to the Seville exemplar and much of its annotation to 1497–98; those claims exceed what the letter itself proves. Liščák 2018 identifies concrete Atlas legends linked to Polo. The report’s universal annotation date and inference that an unmentioned Japan label is absent are too strong. S-20 remains closed and the conservative plate caption stands.

**2026-11-13 — closed.** [Final decisions and source limits](../../../research/investigations/results/S-20-closure.md); [latest dossier](../../../research/investigations/results/S-20-final-columbus-raw.md). Independently checked Shawcross’s abstract/opening, the Day translation and Vogel’s account of the 1319 nickname record; later Shawcross pages and individual postil dating remain unverified. The closure supplies a qualified caption, B5 selection and myth table; downstream revisions remain open.

**2026-11-13 — prioritized reports checked.** [Audit raw](../../../research/investigations/results/S-20-prioritized-audit-raw.md); [verification raw](../../../research/investigations/results/S-20-prioritized-verification-raw.md); [critical intake](../../../research/investigations/results/S-20-prioritized-intake.md). Ma 2025 supplies an attributed 1941 Yang example and Chinese translation bases; dated official 2017 and 2023 speeches offer selective modern examples. The report misdates the 2017 speech as a separate 2024 event and mistakes Morison's narrative for a Columbus postil. Van Duzer gives an attributable Toscanelli dispute; core postil, Atlas and nickname questions remain bounded, with fallbacks. The two prompts now contain only unresolved work; final selections and source records remain open.

**2026-11-13 — remaining research prioritized.** [Priority assessment](../../../research/investigations/S-20-research-priorities.md); [high-priority prompt](../../../research/investigations/S-20-follow-up-prompt.md); [optional prompt](../../../research/investigations/S-20-optional-follow-up-prompt.md). Priorities follow existing III-10/III-11 claims, the selected Columbus plate and B5, with explicit fallbacks when evidence is unavailable. Optional myth origins, cultural extras and exact manuscript/map details no longer block the whole spike merely because they are interesting. No new historical claim is established by this prioritization.

**2026-11-13 — fourth-pass reception findings.** [Raw](../../../research/investigations/results/S-20-fourth-pass-raw.md); [intake](../../../research/investigations/results/S-20-fourth-pass-intake.md). The report repeats prior findings and misattributes several citations; its negative map results do not undo the earlier source checks. Malfatto independently reports 366 annotations in Columbus’s Polo copy but does not identify the hands or method and uses an outdated imprint; the count is registered as an attributed figure. Shawcross’s disputed note and other remaining research stay open.

**2026-11-13 — third-pass reception findings.** [Raw](../../../research/investigations/results/S-20-third-pass-raw.md); [independent intake](../../../research/investigations/results/S-20-third-pass-intake.md). O’Doherty identifies Fra Mauro’s Japan label (#1334); independent scholarly transcriptions and an index locate *2442 and *2306, although variant spellings await a map-image check. Bolognari’s critical edition documents the 1323 Dominican bequest act; Mascherpa’s Quinsai source explanation remains a hypothesis with an alternative. Simion dates the digital Ramusio edition’s availability to 4 February 2015. The 1459 map-identity dispute and remaining gates stay open.

**2026-11-13 — refined reception findings.** [Raw](../../../research/investigations/results/S-20-refined-findings-raw.md); [independent intake](../../../research/investigations/results/S-20-refined-findings-intake.md). Augelli’s study supplies a qualified history of the so-called Marco Polo Bible and dates its wooden box much later; ownership by Polo is unproven. The e-codices catalogue identifies Bern Cod. 125 and transcribes its Cépoy notice. Hu’s 2012 embassy-hosted Xue book launch is on p. 34, not p. 33. Apfelstadt distinguishes different rejections of the Toscanelli correspondence; the documentary context does not authenticate the letters. The follow-up removes the resolved manuscript identification; S-20 remains open.

**2026-11-13 — second-pass reception dossier.** [Raw](../../../research/investigations/results/S-20-second-pass-raw.md); [independent intake](../../../research/investigations/results/S-20-second-pass-intake.md). The report conflates *pelorce* with the nickname *Milione*, gives Columbus classmarks conflicting with Shawcross’s own opening, and gives mutually unclear dating claims; these are not promoted. Independent source checks supply Calvino, O’Neill, and Netflix dates, Nasi’s attributed Coleridge–Purchas–Polo comparison, and competing nickname explanations. A ministry decree dates the airport’s opening to air traffic, not its formal naming. The follow-up removes resolved requests; S-20 remains open.

**2026-11-13 — partial Columbus dossier.** [Dossier](../../../research/investigations/results/S-20-columbus-dossier-raw.md); [intake and source check](../../../research/investigations/results/S-20-columbus-dossier-intake.md). The dossier supplies a promising Shawcross page-and-note locator for a post-1499 or post-1501 argument, but not the passage or reasoning; its dating remains a lead. Shawcross’s independently read opening identifies the copy’s current and former classmarks. The follow-up asks for the note and underlying evidence; the postil dating remains open.

**2026-11-12 — further source corrections.** [Raw](../../../research/investigations/results/S-20-corrections-raw.md); [independent intake](../../../research/investigations/results/S-20-corrections-intake.md). Library records support the 1477 Creussner and 1579 Frampton editions, Marsden 1818, Yule 1871 and Cordier 1903/1920; a writers' society lists Bukal's 2006 novel. Conte's interpretation of a manuscript image and Simion's Z-tradition reconstruction are qualified in the reception registry. Burgio and Simion additionally propose Ghisi as Fra Mauro's source from two map names; a separate list of witnesses does not disprove their identity. Carlsson's alleged 1930 ice-cream passage remains unverified. The follow-up now asks only remaining questions; S-20 stays open.

**2026-11-12 — source-qualified additions.** [Raw](../../../research/investigations/results/S-20-additions-raw.md); [independent intake](../../../research/investigations/results/S-20-additions-intake.md). Checked Blyth's 1841 sheep-naming page, Lima's account of Calvino's 1960 letter and Orlić's 2011 Yangzhou controversy against accessible sources; recorded the findings and limitations. Two Blyth installments with identical titles have different page ranges and DOIs. Carlsson's alleged 1930 ice-cream passage remains an AI-extracted lead, not an independently verified quotation. The follow-up is revised; remaining gates stay open.

**2026-11-12 — reception supplement.** [Raw](../../../research/investigations/results/S-20-supplement-raw.md); [intake and independent source checks](../../../research/investigations/results/S-20-supplement-intake.md). Added attributed Chinese and Mongolian reception examples and selected dated modern events to the registries, including the 2024 Venice exhibition and RAI's 1982–83 broadcast. The supplement's claimed Carlsson 1930 ice-cream passage remains a lead: it gives no page and the actual article was inaccessible here. It does not establish Iranian reception, a full translation chronology, all myth origins, Columbus postils or map-source claims. The follow-up prompt is revised; the spike stays open.

**2026-11-12 — external follow-up.** [Raw attachment](../../../research/investigations/results/S-20-external-followup-raw.md); [intake and targeted source checks](../../../research/investigations/results/S-20-external-followup-intake.md). The supplied report stops after five food/technology myths and leaves Asian and modern cultural reception uncovered. A BnF record confirms Polo in the 1532 Paris *Novus Orbis* and describes its Basel predecessor; Shawcross's abstract supports attribution of notes to Columbus and his circle. The claimed 1930 Carlsson ice-cream story is a lead, not independently checked; its alleged reference to “Cruse 2015” is impossible and may be AI citation contamination. Remaining deliverables are open.

**2026-11-12 — follow-up audit.** The [partial intake](../../../research/investigations/results/S-20-followup-intake.md) was independently checked against selected catalogues, the 2025 manuscript census, Bolognari's PDF, Yule and map scholarship; the [audit](../../../research/investigations/results/S-20-followup-audit.md) records inspection limits and corrections. Most consequential: the 1459 date is a settlement after dispatch of a Portuguese-commissioned map, not an established completion date for the surviving Marciana map; their relationship is disputed. The Bodley 264 ownership entry belongs to the whole composite, and Cepoy's son presented a later copy to Charles. The 2026 publisher abstract states 146 manuscripts surveyed but does not itself reconcile census scopes. The intake is partial; B5 and the myth/afterlives deliverables remain open.

**2026-11-12 — initial intake.** [Raw supplied report](../../../research/investigations/results/S-20-raw.md); [claim-level intake and gap audit](../../../research/investigations/results/S-20-intake.md). The report covers all seven themes, but its BibTeX ends mid-entry, it lacks the requested unresolved list, and most findings do not say which passages were inspected. Do not promote report-only claims. Independent spot checks show that the report's proposed 135–141 current manuscript range misses the 2024 announcement of a 145th codex; the John Day letter alone does not identify the surviving Columbus copy; and the stated 1920–21 origin of the pasta legend is unsubstantiated. These are targeted checks, not an overall error-rate estimate. Preserve S-14's F-19–F-22 hedges, especially for Atlas Chipangu, Columbus's annotations and Jesuit silences. A dated, attributed 2024 discovery has been added to the B5 registry row; the myth table and full timeline remain incomplete.

## Decision
_(fill when closing)_

## Tasks to create on close
- `III-11.T1`, `III-B1.T1`, `I-B1.T1`, `II-B1.T1` (myth-check pass); `DIA.T*` B5 data
