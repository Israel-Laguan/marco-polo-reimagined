# S-21 — Natural history, commodities and marvels

**Status:** open · **Phase:** R (follow-up deep research) · **Timebox:** initial external run + intake complete; targeted follow-up needed · **Gates:** asides and Notes on animals, plants, minerals and marvels in all volumes; the three trivia back-matter files; `PLT` caption facts; `TBL` commodity tables

## Question
For each animal, plant, mineral, trade good and marvel Polo describes, what is it in modern terms? What explains his description (accurate, misunderstood, hearsay, ancient legend)? And what one vivid, checkable fact would a reader enjoy?

## Why it matters
- This is the book's most quotable material and the least checked.
- The Notes currently give Yule's 19th-century naturalism, e.g. clove claims ("true cloves unlikely"), salamander = asbestos, the "unicorn".
- It is also where enrichment pays off most: a good fact here makes an aside, a trivia entry or a plate caption.

## Inputs
- Names that recur in the Notes (grep): *Ovis poli*, *Boswellia*, *Rheum palmatum*, musk, rukh, salamander, unicorn, brazil/sappan, sago, ginger, galingale, porcelain, pearls, rubies, lapis, turquoise, coal, asbestos, horses
- `multimedia-plan.md` § D (comparison tables)

## Method
1. Run the prompt and save the output to `research/results/S-21-raw.md`.
2. Intake: `registry/enrichment.md` § natural history, one row per item: modern ID (Latin name), verdict, the fun fact, the source key, and the chapters it affects.

## Deep research prompt

```text
I am preparing a new English retelling of Marco Polo's book (base: Yule–Cordier, 1903/1920). Polo describes many animals, plants, minerals, goods and marvels. For EACH item below give: (a) modern identification (Latin binomial for organisms; mineral name); (b) verdict on Polo's description: accurate / partly accurate / misunderstanding / hearsay / ancient legend (name the legend's earliest source); (c) one vivid, checkable fact suitable for a general reader; (d) sources (modern scholarship or natural-history references, not Yule alone). Book section IDs are in brackets.

ANIMALS: the "unicorn" (Sumatran or Javan rhinoceros) [III-03]; Ovis poli (Marco Polo sheep) [I-10]; yak and the "beautiful cattle" of Tangut [I-11]; musk deer and musk extraction [I-11, II-07]; the rukh / roc (sources: Arabic tales, al-Qazwini; Madagascar's extinct elephant bird Aepyornis; and Polo's "feathers" — raffia palm fronds sent to Kublai?) [III-07]; crocodiles as "huge serpents" with legs in Carajan (Yunnan) and their gall as medicine [II-07]; gyrfalcons and peregrines of the north [I-12, II-04]; cheetahs, lynx and tigers used in hunting [II-04]; Persian and Arab horses, and the Indian horse-trade problem (why horses died in India) [III-05]; the black-and-white "lions" (tigers?) [II-04]; fat-tailed sheep and the humped oxen of Kerman [I-07]; pygmies made from monkeys [III-03]; the hairy "dog-headed" men of Angamanain [III-04]; ostriches and giraffes of Abash and Zanghibar [III-07]; the Tartar dogs and sled dogs of the Land of Darkness [II-15].

PLANTS AND FOODS: rhubarb (Rheum palmatum) of Sukchur [I-11]; ginger, galingale, cassia and cinnamon [II-07, II-12]; pepper volumes at Zayton (Polo's 100-to-1 comparison with Alexandria) [II-14]; cloves (and the Nicobar "clove" claim) [III-04]; nutmeg, spikenard, cubebs [III-02]; sago and the "flour from trees" [III-03]; brazilwood/sappan (Caesalpinia sappan) [III-07]; indigo manufacture at Coilum [III-07]; coconut ("Indian nut") [III-03]; date wine and dried fish at Hormuz [I-07]; rice wine and grape wine [II-04]; frankincense (Boswellia sacra) at Dufar [III-08]; aloes wood (Aquilaria) of Champa [III-02]; camphor of Fansur [III-03]; the dry tree (Arbre Sec / Arbre Sol: a chinar or a pistachio?) [I-08]; Persian melons of Sapurgan [I-08]; ice/kumiss and mare's milk [I-13].

MINERALS AND GOODS: balas rubies (spinel) and lapis lazuli of Badakhshan [I-09]; turquoise of Kerman [I-07]; tutty (zinc oxide) and spodium of Cobinan [I-08]; asbestos ("salamander") of Chingintalas [I-11]; coal ("black stones") [II-05]; salt cakes as money in Yunnan and Tibet [II-07]; cowrie money [II-07]; porcelain [II-14]; pearls of the Gulf of Mannar [III-05]; diamonds of Mutfili [III-06]; ambergris (and the whale it comes from) [III-07]; the Ceylon king's great ruby [III-04]; silk, gold brocade (nasij) and cloth of gold [I-05, II-03]; the "fountain of oil" at Baku [I-04]; steel of Kerman ("ondanique") [I-07].

MARVELS AND TECHNIQUES: the singing sands / desert voices of Lop [I-11]; fire burning less well on the Pamir [I-10]; the shark-charmers of the pearl fishery [III-05]; the diamond valley with eagles and meat (from Epiphanius and the Sinbad story?) [III-06]; the Male and Female Islands [III-07]; the Socotra sorcerers who raise winds [III-07]; the Bacsi lamas' weather magic and the self-moving cups at Kublai's feast [I-13, II-03]; the stones that keep invaders from being wounded (Chipangu) [III-01]; tattooing [II-14]; couvade [II-07]; the long nails of the Chinese gentry; gold-covered teeth [II-07].

Group the output by section ID so I can use it chapter by chapter.

OUTPUT FORMAT (required). (1) A findings table with columns: # · claim or topic · finding · verdict (confirmed / corrected / disputed / not found) · sources (author, title, year, and DOI or stable URL) · confidence (high / medium / low) · book sections affected (use the IDs I give). (2) Under each table, short prose only where a disagreement needs explaining: name who holds which position. (3) A bibliography of every source you used, each with a BibTeX entry and a note on whether it is open access. (4) A list of questions you could not resolve. Rules: do not invent page numbers, quotations, DOIs or URLs; if you did not see a passage, paraphrase and say so. Prefer peer-reviewed scholarship, critical editions and museum or archive records over popular sites. Say "not found" rather than guess. Flag anything published after 2013 as NEW.
```

## Output (definition of done)
- [x] `research/results/S-21-raw.md` saved (exact supplied attachment)
- [ ] `registry/enrichment.md` § natural history, grouped by chapter
- [ ] Candidate rows for the `TBL` commodity tables

## Feedback to plan
- `multimedia-plan.md` § D (commodity tables)
- `illustration-plan.md`: caption facts for natural-history secondaries

## Follow-up prompts

[Targeted stricter rerun for passes 1 and 2](../research/S-21-passes-targeted-rerun-prompt.md) — publication-critical witness checks and unresolved evidence, required after both spot checks fell below 80%.

[Remaining high-priority pass 1](../research/S-21-high-priority-pass1-prompt.md) — customs, animals, metals and money.

[Remaining high-priority pass 2](../research/S-21-high-priority-pass2-prompt.md) — pearls, goods, trade and marvels.

[High-priority research prompt](../research/S-21-high-priority-prompt.md) — standalone external-agent run; see the separate low-priority first pass below.

[S-21 follow-up deep research prompt](../research/S-21-follow-up-prompt.md) — stricter claim-level rerun, prioritized by impact; includes a coverage ledger for unresolved items.

**Latest follow-up:** The supplied [critical source audit](../research/results/S-21-followup-raw.md) has been preserved. Its remaining gaps are classified, with manuscript-specific fallbacks, in [S-21 research priorities](../research/S-21-research-priorities.md). This is editorial triage, not an independent verification intake; report-only findings are not promoted. High-priority work targets existing claims and source inspection; low-priority work is optional unless a particular detail is selected.

## Findings

**Pass 1 and pass 2 returned:** [raw pass 1](../research/results/S-21-pass1-raw.md), [raw pass 2](../research/results/S-21-pass2-raw.md), and [checked intake](../research/results/S-21-pass1-pass2-intake.md). Ten purposively selected claim-level citation checks per report yielded **7/10** and **6/10** respectively; access limitations and metadata errors count as misses, and these are not random error-rate estimates. The project rule calls for a stricter rerun below 80%. Pass 2 falsely denies the diamond-valley story and misses Yule’s Ramusio attribution of the full whale-hunt paragraph. Pass 1 misidentifies a crocodilian article and overlooks Kunz–Stevenson’s 1885 statement; pass 2 misidentifies the 2024 Mannar article’s authors and title. Corrected, scoped candidates are in the enrichment registry. The full chapter register and table remain incomplete.


**High-priority first tranche:** [raw report](../research/results/S-21-high-priority-raw.md) and [checked intake](../research/results/S-21-high-priority-intake.md). Ten targeted source checks: 8/10 support the narrow proposition, with a wrong author initial and a digitized viewer not accessible in this environment; this is not a random error-rate estimate. Eusebi’s F-text edition independently supports the narrow textual distinction between the Basma description and the Fansur “we ate” passage; it is not a fresh manuscript collation. Most requested groups remain unattempted, so the spike stays open and the remaining prompts split their scope.

**Low-priority first pass:** [source checks and research ledger](../research/results/S-21-low-priority-research.md) covers L1–L14, with partial answers and explicit unattempted items. Ten purposive checks of sources cited by the follow-up report found 6/10 fully supported the particular proposition checked; four fell short or contained metadata/routing errors. This is not a random error-rate estimate. The stricter [high-priority prompt](../research/S-21-high-priority-prompt.md) is ready; it has not been run externally. The pass directly inspected Talbot’s composite-rhinoceros argument, sourced an earlier seasonal-separation parallel and corrected several passage locations; remaining questions and proposed wording are in the ledger.
**S-20 carryover — Pamir sheep:** S20-E17 records Blyth’s 1841 printed use of *Ovis Polii*, citing Polo, and Yang et al.’s use of *Ovis ammon polii*. [ITIS](https://www.itis.gov/servlet/SingleRpt/SingleRpt?print_version=SCR&search_topic=TSN&search_value=898792) gives 1840 for the original name, so do not call the 1841 publication its first appearance without resolving the bibliographic discrepancy. The [Mammal Diversity Database](https://www.mammaldiversity.org/taxon/1006203/) treats *polii* within *Ovis ammon* and notes other taxonomic treatments. This supports an attributed naming-history note in I-10; it does not independently establish that Polo observed the animal. S-21 remains open for its wider natural-history work.

Initial report preserved as [raw](../research/results/S-21-raw.md); see the [intake](../research/results/S-21-intake.md) for source checks and candidate table rows. Ten purposively selected report sources were tested against narrow propositions: **3/10 supported the proposition tested at the inspection level available**. This is not an error-rate estimate; seven failures include inaccessible, indirect or non-specific evidence, not proof of falsehood. The research README requires a stricter rerun below 80%; the follow-up prompt provides it.

The report covers 59 topics but often conflates an underlying modern phenomenon with Polo’s precise observation, place or century. The first intake corrects a pearl-fishery continuity overclaim, supplies the ambergris paper citation, flags the unsupported Java entrepôt explanation and spots the misplaced Lambri brazil passage. A few scoped facts are in `registry/enrichment.md`; the full chapter register and TBL rows remain incomplete.

## Decision
_(fill when closing)_

## Tasks to create on close
- Per-chapter `.T4` Note upgrades; `I-B1`, `II-B1`, `III-B1` trivia items; `TBL.T*` rows
