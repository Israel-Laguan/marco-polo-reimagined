# S-21 — Natural history, commodities and marvels

**Status:** open · **Phase:** R (deep research) · **Timebox:** 1 external run + 1 intake session · **Gates:** asides and Notes on animals, plants, minerals and marvels in all volumes; the three trivia back-matter files; `PLT` caption facts; `TBL` commodity tables

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
- [ ] `research/results/S-21-raw.md` saved
- [ ] `registry/enrichment.md` § natural history, grouped by chapter
- [ ] Candidate rows for the `TBL` commodity tables

## Feedback to plan
- `multimedia-plan.md` § D (commodity tables)
- `illustration-plan.md`: caption facts for natural-history secondaries

## Follow-up prompts
_(add here if the results leave gaps)_

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- Per-chapter `.T4` Note upgrades; `I-B1`, `II-B1`, `III-B1` trivia items; `TBL.T*` rows
