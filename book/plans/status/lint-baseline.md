# Lint baseline

`python3 tools/lint.py --md` · 24/52 files pass. Errors decide pass/fail; warnings are prompts for the human read.

## Summary by check

| Check | Files with errors | Files with warnings |
|---|---|---|
| verbatim | 24 | 0 |
| first_person | 11 | 0 |
| archaism | 23 | 0 |
| you_must_know | 15 | 0 |
| budgets | 22 | 0 |
| asides | 23 | 0 |
| recaps | 3 | 11 |
| openers | 0 | 4 |
| length | 7 | 0 |
| sentence | 0 | 18 |
| citations | 1 | 0 |
| ramusio | 0 | 3 |
| names | 0 | 13 |
| name_policy | 0 | 18 |

## Per file

| File | Kind | Errors | Warnings | Words | Verbatim | Quotes | Asides | Failing checks |
|---|---|---|---|---|---|---|---|---|
| vol-1/back-01-trivia-and-disputes.md | frontback | 1 | 0 | 1262 | 1% |  |  | length |
| vol-1/back-02-glossary.md | frontback | 0 | 0 | 13 | 0% |  |  | — |
| vol-1/ch-01-genoa-prison.md | narrative | 0 | 0 | 1800 | 5% | 0 | 2 | — |
| vol-1/ch-02-house-of-polo.md | narrative | 0 | 0 | 1893 | 12% | 5 | 3 | — |
| vol-1/ch-03-second-setting-forth.md | narrative | 13 | 7 | 2616 | 32% | 0 | 4 | archaism, asides, budgets, verbatim |
| vol-1/ch-04-hermenia-georgiania.md | narrative | 11 | 3 | 2323 | 49% | 0 | 3 | archaism, asides, budgets, verbatim, you_must_know |
| vol-1/ch-05-mausul-baudas.md | narrative | 13 | 6 | 2955 | 61% | 0 | 3 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-06-tauris-persia.md | narrative | 13 | 4 | 2723 | 58% | 0 | 2 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-07-kerman-hormos.md | narrative | 11 | 4 | 2974 | 69% | 0 | 2 | archaism, asides, budgets, first_person, recaps, verbatim, you_must_know |
| vol-1/ch-08-arbre-sec-old-man.md | narrative | 6 | 4 | 2406 | 62% | 0 | 2 | archaism, asides, verbatim |
| vol-1/ch-09-balc-badashan.md | narrative | 10 | 8 | 3156 | 65% | 0 | 3 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-10-pamier-cotan.md | narrative | 12 | 13 | 2804 | 50% | 0 | 2 | archaism, asides, budgets, verbatim |
| vol-1/ch-11-lop-tangut.md | narrative | 18 | 6 | 2804 | 45% | 0 | 4 | archaism, asides, budgets, recaps, verbatim, you_must_know |
| vol-1/ch-12-caracoron-tenduc.md | narrative | 14 | 14 | 3100 | 16% | 0 | 5 | archaism, asides, budgets, first_person, verbatim |
| vol-1/ch-13-chandu.md | narrative | 12 | 4 | 2639 | 57% | 0 | 3 | archaism, asides, budgets, verbatim, you_must_know |
| vol-1/front-01-world-before-the-road.md | frontback | 0 | 1 | 1199 | 2% |  |  | — |
| vol-1/front-02-maps-outbound.md | frontback | 0 | 0 | 434 | 3% |  |  | — |
| vol-2/back-01-trivia-and-disputes.md | frontback | 0 | 0 | 862 | 3% |  |  | — |
| vol-2/back-02-glossary.md | frontback | 0 | 0 | 13 | 0% |  |  | — |
| vol-2/ch-01-cublay-nayan.md | narrative | 0 | 2 | 1814 | 2% | 0 | 1 | — |
| vol-2/ch-02-person-palace.md | narrative | 0 | 0 | 1830 | 3% | 6 | 2 | — |
| vol-2/ch-03-feasts-keshican.md | narrative | 0 | 0 | 2141 | 2% | 1 | 0 | — |
| vol-2/ch-04-hunt-traffic.md | narrative | 0 | 0 | 2012 | 2% | 1 | 0 | — |
| vol-2/ch-05-ahmad-paper-coal.md | narrative | 15 | 5 | 3198 | 31% | 0 | 3 | archaism, asides, budgets, recaps, verbatim |
| vol-2/ch-06-pulisanghin-sindafu.md | narrative | 0 | 1 | 1812 | 1% | 0 | 1 | — |
| vol-2/ch-07-tebet-carajan.md | narrative | 10 | 6 | 3019 | 47% | 0 | 0 | archaism, budgets, verbatim |
| vol-2/ch-08-mien-bangala.md | narrative | 0 | 0 | 1815 | 2% | 0 | 0 | — |
| vol-2/ch-09-caugigu-cuiju.md | narrative | 0 | 0 | 1851 | 2% | 0 | 0 | — |
| vol-2/ch-10-manzi-sung.md | narrative | 0 | 0 | 1802 | 2% | 0 | 4 | — |
| vol-2/ch-11-yanju-saianfu.md | narrative | 0 | 0 | 1800 | 2% | 0 | 0 | — |
| vol-2/ch-12-kian-suju.md | narrative | 0 | 0 | 1843 | 3% | 0 | 1 | — |
| vol-2/ch-13-kinsay.md | narrative | 16 | 9 | 3354 | 44% | 0 | 3 | archaism, asides, budgets, first_person, length, verbatim, you_must_know |
| vol-2/ch-14-fuju-zayton.md | narrative | 0 | 0 | 1813 | 2% | 0 | 0 | — |
| vol-2/ch-15-great-turkey-ponent.md | narrative | 3 | 14 | 1374 | 3% | 0 | 1 | budgets, citations, length |
| vol-2/front-01-yuan-china-context.md | frontback | 0 | 0 | 1030 | 2% |  |  | — |
| vol-2/front-02-maps-cathay-manzi.md | frontback | 0 | 0 | 293 | 12% |  |  | — |
| vol-3/back-01-trivia-and-afterlives.md | frontback | 0 | 0 | 777 | 1% |  |  | — |
| vol-3/back-02-glossary.md | frontback | 0 | 0 | 13 | 0% |  |  | — |
| vol-3/ch-01-ships-chipangu.md | narrative | 16 | 3 | 2273 | 48% | 0 | 3 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-02-chamba-java.md | narrative | 10 | 4 | 1791 | 47% | 0 | 3 | asides, budgets, length, verbatim, you_must_know |
| vol-3/ch-03-java-less-sumatra.md | narrative | 13 | 5 | 2237 | 62% | 0 | 2 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-04-necuveran-seilan.md | narrative | 22 | 3 | 2576 | 77% | 0 | 3 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-3/ch-05-maabar-st-thomas.md | narrative | 16 | 1 | 2761 | 38% | 0 | 3 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-3/ch-06-mutfili-kesmacoran.md | narrative | 13 | 2 | 3630 | 63% | 0 | 5 | archaism, asides, budgets, first_person, length, verbatim, you_must_know |
| vol-3/ch-07-male-abash.md | narrative | 11 | 1 | 2682 | 46% | 0 | 3 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-08-aden-hormos.md | narrative | 13 | 0 | 2035 | 64% | 0 | 6 | archaism, asides, budgets, first_person, verbatim |
| vol-3/ch-09-cocachin-return.md | narrative | 5 | 11 | 2743 | 37% | 0 | 1 | archaism, first_person, verbatim |
| vol-3/ch-10-ca-polo-milione.md | narrative | 7 | 1 | 3244 | 38% | 0 | 1 | archaism, asides, length, verbatim |
| vol-3/ch-11-afterlives.md | narrative | 3 | 2 | 2513 | 3% | 0 | 2 | asides |
| vol-3/ch-12-reliability-essay.md | essay | 1 | 1 | 3519 | 1% |  |  | length |
| vol-3/front-01-indian-ocean-world.md | frontback | 0 | 0 | 898 | 1% |  |  | — |
| vol-3/front-02-maps-seas-and-return.md | frontback | 0 | 0 | 210 | 14% |  |  | — |

## Issues

### vol-1/back-01-trivia-and-disputes.md

- **error** — `length` narrative 1262 words (outside 0–1200)

### vol-1/ch-03-second-setting-forth.md

- **error** — `verbatim` verbatim Yule 32% (> 15%); worst: L37 70%, L50 77%, L52 72%, L54 91%
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L37 `archaism` archaism outside quotes: “insomuch”
- **error** L52 `archaism` archaism outside quotes: “insomuch”
- **error** L13 `budgets` “Anyway” ×4 (> 1) at L13, L25, L29, L39
- **error** L9 `budgets` formula hinges ×6 (> 3)
- **error** L13 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 123 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L29 `asides` aside 118 words (> 80)
- **error** L29 `asides` aside ends in an exit formula
- **error** L39 `asides` aside 109 words (> 80)
- **error** L39 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 28.6 words (> 25)
- **warning** L17 `name_policy` “Nicolas” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L19 `name_policy` “Bendocquedar” used bare; the book form for this person is “Bundukdar” (S-05)
- **warning** L29 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L19 `name_policy` first mention of “Bundukdar” has no gloss (Baibars) (S-05)
- **warning** L56 `name_policy` first mention of “Bolgana” has no gloss (Bulughan) (S-05)
- **warning** L56 `name_policy` first mention of “Cocachin” has no gloss (Kököchin) (S-05)

### vol-1/ch-04-hermenia-georgiania.md

- **error** — `verbatim` verbatim Yule 49% (> 15%); worst: L17 84%, L21 74%, L23 75%, L25 97%, L31 71%
- **error** L25 `archaism` archaism outside quotes: “insomuch”
- **error** L33 `archaism` archaism outside quotes: “thereof”
- **error** L35 `archaism` archaism outside quotes: “whilst”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×2 (> 1) at L19, L27
- **error** L11 `budgets` formula hinges ×4 (> 3)
- **error** L19 `asides` aside 130 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 98 words (> 80)
- **error** L27 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 29.6 words (> 25)
- **warning** L13 `names` “Hermenie” is close to gazetteer name “Hermenia” (variant spelling?)
- **warning** L15 `name_policy` first mention of “Bundukdar” has no gloss (Baibars) (S-05)

### vol-1/ch-05-mausul-baudas.md

- **error** — `verbatim` verbatim Yule 61% (> 15%); worst: L19 73%, L25 72%, L27 86%, L40 94%, L42 83%
- **error** L38 `first_person` Book first person outside quotes: “I will tell”
- **error** L58 `first_person` Book first person outside quotes: “I will tell”
- **error** L27 `archaism` archaism outside quotes: “wist”
- **error** L42 `archaism` archaism outside quotes: “whilst”
- **error** L52 `archaism` archaism outside quotes: “whilst”
- **error** L52 `archaism` archaism outside quotes: “insomuch”
- **error** L54 `archaism` archaism outside quotes: “thereof”
- **error** L13 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×2 (> 1) at L21, L29
- **error** L21 `asides` aside ends in an exit formula
- **error** L29 `asides` aside 138 words (> 80)
- **error** L56 `asides` aside 108 words (> 80)
- **warning** L50 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.3 words (> 25)
- **warning** L17 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L29 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L29 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L29 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-06-tauris-persia.md

- **error** — `verbatim` verbatim Yule 58% (> 15%); worst: L23 74%, L25 100%, L27 100%, L29 100%, L31 93%
- **error** L15 `first_person` Book first person outside quotes: “we will quit”
- **error** L35 `first_person` Book first person outside quotes: “I will tell”
- **error** L25 `archaism` archaism outside quotes: “to wit”
- **error** L27 `archaism` archaism outside quotes: “thereof”
- **error** L27 `archaism` archaism outside quotes: “wherein”
- **error** L35 `archaism` archaism outside quotes: “to wit”
- **error** L50 `archaism` archaism outside quotes: “sundry”
- **error** L35 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L33
- **error** L17 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 125 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **warning** L29 `openers` consecutive paragraphs open with “and when”
- **warning** L50 `openers` consecutive paragraphs open with “in this”
- **warning** — `sentence` average sentence 26.1 words (> 25)
- **warning** L13 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-07-kerman-hormos.md

- **error** — `verbatim` verbatim Yule 69% (> 15%); worst: L15 76%, L17 78%, L21 93%, L25 83%, L36 74%
- **error** L50 `first_person` Book first person outside quotes: “we will quit”
- **error** L17 `archaism` archaism outside quotes: “thereof”
- **error** L25 `archaism` archaism outside quotes: “whilst”
- **error** L40 `archaism` archaism outside quotes: “to wit”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L23 `budgets` “Anyway” ×2 (> 1) at L23, L46
- **error** L11 `budgets` formula hinges ×6 (> 3)
- **error** L23 `asides` aside ends in an exit formula
- **error** L46 `asides` aside ends in an exit formula
- **error** L50 `recaps` closing recap (181 words)
- **warning** — `sentence` average sentence 27.4 words (> 25)
- **warning** L25 `names` “Keshemur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L27 `names` “Conosalmi” is close to gazetteer name “Canosalmi” (variant spelling?)
- **warning** L25 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)

### vol-1/ch-08-arbre-sec-old-man.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L13 79%, L23 75%, L25 88%, L31 97%, L33 86%
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L27 `asides` aside 162 words (> 80)
- **error** L27 `asides` aside ends in an exit formula
- **error** L41 `asides` aside 138 words (> 80)
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 29.1 words (> 25)
- **warning** L39 `name_policy` “Alau” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L41 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-09-balc-badashan.md

- **error** — `verbatim` verbatim Yule 65% (> 15%); worst: L25 71%, L27 95%, L29 91%, L33 77%, L35 75%
- **error** L19 `first_person` Book first person outside quotes: “I will tell”
- **error** L58 `first_person` Book first person outside quotes: “we will quit”
- **error** L52 `archaism` archaism outside quotes: “insomuch”
- **error** L48 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×3 (> 1) at L21, L31, L50
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L21 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L50 `asides` aside ends in an exit formula
- **warning** L56 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `openers` consecutive paragraphs open with “when you”
- **warning** L37 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L13 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L13 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L21 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L46 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L56 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-10-pamier-cotan.md

- **error** — `verbatim` verbatim Yule 50% (> 15%); worst: L15 96%, L17 100%, L23 76%, L29 97%, L31 100%
- **error** L15 `archaism` archaism outside quotes: “’tis”
- **error** L15 `archaism` archaism outside quotes: “insomuch”
- **error** L29 `archaism` archaism outside quotes: “gat”
- **error** L29 `archaism` archaism outside quotes: “thereof”
- **error** L31 `archaism` archaism outside quotes: “wist”
- **error** L19 `budgets` “Anyway” ×2 (> 1) at L19, L33
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L19 `asides` aside 228 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 150 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **warning** L39 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.4 words (> 25)
- **warning** L43 `ramusio` possible Ramusio passage without a note anchor
- **warning** L21 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L39 `names` “Country” is close to gazetteer name “County” (variant spelling?)
- **warning** L45 `names` “Keria” is close to gazetteer name “Keriya” (variant spelling?)
- **warning** L25 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L25 `name_policy` “Kaidu” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L27 `name_policy` “Caidou” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L33 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L33 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L33 `name_policy` “Kaidu” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L39 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)

### vol-1/ch-11-lop-tangut.md

- **error** — `verbatim` verbatim Yule 45% (> 15%); worst: L38 73%, L48 76%
- **error** L9 `archaism` archaism outside quotes: “whilst”
- **error** L17 `archaism` archaism outside quotes: “’tis”
- **error** L32 `archaism` archaism outside quotes: “sundry”
- **error** L32 `archaism` archaism outside quotes: “whilst”
- **error** L34 `archaism` archaism outside quotes: “whilst”
- **error** L40 `archaism` archaism outside quotes: “whilst”
- **error** L50 `archaism` archaism outside quotes: “whilst”
- **error** L34 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×4 (> 1) at L21, L36, L42, L46
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L21 `asides` aside 105 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L36 `asides` aside 82 words (> 80)
- **error** L36 `asides` aside ends in an exit formula
- **error** L42 `asides` aside ends in an exit formula
- **error** L46 `asides` aside ends in an exit formula
- **error** L54 `recaps` closing recap (160 words)
- **warning** — `sentence` average sentence 29.4 words (> 25)
- **warning** L30 `ramusio` possible Ramusio passage without a note anchor
- **warning** L40 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L40 `name_policy` “Mangu” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L42 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L46 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-1/ch-12-caracoron-tenduc.md

- **error** — `verbatim` verbatim Yule 16% (> 15%); worst: —
- **error** L13 `first_person` Book first person outside quotes: “I will tell”
- **error** L13 `archaism` archaism outside quotes: “wherein”
- **error** L17 `archaism` archaism outside quotes: “sundry”
- **error** L15 `budgets` “Anyway” ×5 (> 1) at L15, L21, L27, L31, L67
- **error** L9 `budgets` formula hinges ×7 (> 3)
- **error** L15 `asides` 5 asides (> 4)
- **error** L15 `asides` aside ends in an exit formula
- **error** L21 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 116 words (> 80)
- **error** L27 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L67 `asides` aside 93 words (> 80)
- **error** L67 `asides` aside ends in an exit formula
- **warning** L21 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L21 `name_policy` “Wang Khan” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L21 `name_policy` “Toghrul” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L27 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L27 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L27 `name_policy` “Aung Khan” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L29 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L31 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L31 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L31 `name_policy` “Qubilai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L31 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L45 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L45 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L65 `name_policy` first mention of “King George” has no gloss (Körgüz of the Önggüd) (S-05)

### vol-1/ch-13-chandu.md

- **error** — `verbatim` verbatim Yule 57% (> 15%); worst: L17 76%, L21 84%, L23 90%, L27 74%, L33 90%
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L21 `archaism` archaism outside quotes: “to wit”
- **error** L33 `archaism` archaism outside quotes: “’Tis”
- **error** L39 `archaism` archaism outside quotes: “’Tis”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L35 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×3 (> 1) at L19, L25, L29
- **error** L19 `asides` aside 101 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L25 `asides` aside ends in an exit formula
- **error** L29 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 28.9 words (> 25)
- **warning** L43 `names` “Kesimur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L25 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L13 `name_policy` first mention of “Cublay” has no gloss (Kublai) (S-05)

### vol-1/front-01-world-before-the-road.md

- **warning** L29 `names` “Mongolica” is close to gazetteer name “Mongolia” (variant spelling?)

### vol-2/ch-01-cublay-nayan.md

- **warning** L21 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L13 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-2/ch-05-ahmad-paper-coal.md

- **error** — `verbatim` verbatim Yule 31% (> 15%); worst: L13 72%
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L43 `archaism` archaism outside quotes: “hath”
- **error** L43 `archaism` archaism outside quotes: “hath”
- **error** L53 `archaism` archaism outside quotes: “thereof”
- **error** L55 `archaism` archaism outside quotes: “hath”
- **error** L57 `archaism` archaism outside quotes: “whilst”
- **error** L69 `archaism` archaism outside quotes: “hath”
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L39, L59
- **error** L17 `asides` aside ends in an exit formula
- **error** L39 `asides` aside ends in an exit formula
- **error** L59 `asides` aside ends in an exit formula
- **error** L11 `recaps` opening recap
- **error** L71 `recaps` closing recap (88 words)
- **warning** L19 `names` “Zhenjin” is close to gazetteer name “Zhenjiang” (variant spelling?)
- **warning** L17 `name_policy` “Jamui Khatun” used bare; the book form for this person is “Chabi” (S-05)
- **warning** L17 `name_policy` “Ahmad” used bare; the book form for this person is “Achmath” (S-05)
- **warning** L17 `name_policy` “Ahama” used bare; the book form for this person is “Achmath” (S-05)
- **warning** L25 `name_policy` “Ahmad” used bare; the book form for this person is “Achmath” (S-05)

### vol-2/ch-06-pulisanghin-sindafu.md

- **warning** L22 `names` “Jiangzhou” is close to gazetteer name “Liangzhou” (variant spelling?)

### vol-2/ch-07-tebet-carajan.md

- **error** — `verbatim` verbatim Yule 47% (> 15%); worst: L17 78%, L29 70%, L51 75%
- **error** L25 `archaism` archaism outside quotes: “sundry”
- **error** L27 `archaism` archaism outside quotes: “wherein”
- **error** L31 `archaism` archaism outside quotes: “whilst”
- **error** L33 `archaism` archaism outside quotes: “sundry”
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L51 `archaism` archaism outside quotes: “whilst”
- **error** L51 `archaism` archaism outside quotes: “’tis”
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **warning** L45 `openers` consecutive paragraphs open with “in this”
- **warning** L11 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L11 `name_policy` “Mongu” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L37 `name_policy` “Temür” used bare; the book form for this person is “Temur” (S-05)
- **warning** L37 `name_policy` “Essentimur” used bare; the book form for this person is “Sentemur” (S-05)
- **warning** L41 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-2/ch-13-kinsay.md

- **error** — `verbatim` verbatim Yule 44% (> 15%); worst: L15 86%, L17 96%, L19 89%, L31 73%, L35 87%
- **error** L93 `first_person` Book first person outside quotes: “we will quit”
- **error** L17 `archaism` archaism outside quotes: “hath”
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “thereof”
- **error** L49 `archaism` archaism outside quotes: “hath”
- **error** L57 `archaism` archaism outside quotes: “hath”
- **error** L61 `archaism` archaism outside quotes: “Certes”
- **error** L35 `you_must_know` “You must know” outside quotes
- **error** L45 `you_must_know` “You must know” outside quotes
- **error** L91 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×2 (> 1) at L21, L95
- **error** L21 `asides` aside 92 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L95 `asides` aside ends in an exit formula
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** L51 `recaps` “So/Thus …” restatement paragraph?
- **warning** L63 `recaps` “So/Thus …” restatement paragraph?
- **warning** L83 `recaps` “So/Thus …” restatement paragraph?
- **error** — `length` narrative 3354 words (outside 1800–3200)
- **warning** — `sentence` average sentence 26.3 words (> 25)
- **warning** L17 `ramusio` possible Ramusio passage without a note anchor
- **warning** L31 `ramusio` possible Ramusio passage without a note anchor
- **warning** L35 `ramusio` possible Ramusio passage without a note anchor
- **warning** L43 `ramusio` possible Ramusio passage without a note anchor

### vol-2/ch-15-great-turkey-ponent.md

- **error** L15 `budgets` attribution verb “gives” ×5 (> 4)
- **error** — `length` narrative 1374 words (outside 1800–3200)
- **error** — `citations` body citations not sequential 1..n: [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7]…
- **warning** L13 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L13 `name_policy` “Chaghatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L31 `name_policy` “Ulatai” used bare; the book form for this person is “Oulatay” (S-05)
- **warning** L33 `name_policy` “Geikhatu” used bare; the book form for this person is “Kiacatu” (S-05)
- **warning** L35 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L35 `name_policy` “Abaqa” used bare; the book form for this person is “Abaga” (S-05)
- **warning** L35 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L35 `name_policy` “Geikhatu” used bare; the book form for this person is “Kiacatu” (S-05)
- **warning** L35 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)
- **warning** L51 `name_policy` “Berke” used bare; the book form for this person is “Barca” (S-05)
- **warning** L51 `name_policy` “Abaqa” used bare; the book form for this person is “Abaga” (S-05)
- **warning** L53 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L53 `name_policy` “Berke” used bare; the book form for this person is “Barca” (S-05)
- **warning** L35 `name_policy` first mention of “Alaü” has no gloss (Hulagu) (S-05)

### vol-3/ch-01-ships-chipangu.md

- **error** — `verbatim` verbatim Yule 48% (> 15%); worst: L23 76%, L29 89%, L51 72%, L53 75%
- **error** L13 `archaism` archaism outside quotes: “wherein”
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L25 `archaism` archaism outside quotes: “hath”
- **error** L51 `archaism` archaism outside quotes: “’tis”
- **error** L11 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L51 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L27, L37
- **error** L13 `budgets` formula hinges ×6 (> 3)
- **error** L11 `budgets` attribution verb “says” ×6 (> 4)
- **error** L15 `asides` aside ends in an exit formula
- **error** L27 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 83 words (> 80)
- **error** L37 `asides` aside ends in an exit formula
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L55 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.2 words (> 25)

### vol-3/ch-02-chamba-java.md

- **error** — `verbatim` verbatim Yule 47% (> 15%); worst: L13 84%, L15 74%, L19 76%, L25 92%, L29 94%
- **error** L13 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L27, L33
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 108 words (> 80)
- **error** L27 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 93 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **error** — `length` narrative 1791 words (outside 1800–3200)
- **warning** — `sentence` average sentence 26.1 words (> 25)
- **warning** L27 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-3/ch-03-java-less-sumatra.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L17 93%, L21 88%, L23 97%, L29 100%, L31 74%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L23 `archaism` archaism outside quotes: “’Tis”
- **error** L23 `archaism` archaism outside quotes: “’tis”
- **error** L27 `archaism` archaism outside quotes: “sundry”
- **error** L27 `archaism` archaism outside quotes: “’tis”
- **error** L54 `archaism` archaism outside quotes: “sundry”
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L50 `you_must_know` “You must know” outside quotes
- **error** L25 `budgets` “Anyway” ×2 (> 1) at L25, L39
- **error** L11 `budgets` formula hinges ×4 (> 3)
- **error** L25 `asides` aside ends in an exit formula
- **error** L39 `asides` aside ends in an exit formula
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 25.3 words (> 25)
- **warning** L21 `names` “Islanders” is close to gazetteer name “Islands” (variant spelling?)
- **warning** L33 `name_policy` first mention of “Cocachin” has no gloss (Kököchin) (S-05)

### vol-3/ch-04-necuveran-seilan.md

- **error** — `verbatim` verbatim Yule 77% (> 15%); worst: L13 89%, L17 95%, L21 94%, L25 96%, L33 95%
- **error** L13 `first_person` Book first person outside quotes: “I tell you”
- **error** L17 `first_person` Book first person outside quotes: “I assure you”
- **error** L25 `first_person` Book first person outside quotes: “Now I will”
- **error** L33 `first_person` Book first person outside quotes: “I tell you”
- **error** L35 `first_person` Book first person outside quotes: “I assure you”
- **error** L45 `first_person` Book first person outside quotes: “I have been telling”
- **error** L49 `first_person` Book first person outside quotes: “And why should I”
- **error** L13 `archaism` archaism outside quotes: “sundry”
- **error** L35 `archaism` archaism outside quotes: “thereof”
- **error** L41 `archaism` archaism outside quotes: “hath”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×3 (> 1) at L19, L23, L43
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L19 `asides` aside ends in an exit formula
- **error** L23 `asides` aside ends in an exit formula
- **error** L43 `asides` aside 98 words (> 80)
- **error** L43 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L39 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 26.7 words (> 25)

### vol-3/ch-05-maabar-st-thomas.md

- **error** — `verbatim` verbatim Yule 38% (> 15%); worst: L4 100%, L11 79%, L19 82%, L38 73%
- **error** L11 `first_person` Book first person outside quotes: “I will tell”
- **error** L19 `first_person` Book first person outside quotes: “I can tell you”
- **error** L30 `first_person` Book first person outside quotes: “I am going to”
- **error** L56 `first_person` Book first person outside quotes: “I will relate”
- **error** L19 `archaism` archaism outside quotes: “hath”
- **error** L34 `archaism` archaism outside quotes: “hath”
- **error** L38 `archaism` archaism outside quotes: “hath”
- **error** L11 `you_must_know` “You must know” outside quotes
- **error** L17 `you_must_know` “You must know” outside quotes
- **error** L30 `you_must_know` “You must know” outside quotes
- **error** L32 `budgets` “Anyway” ×3 (> 1) at L32, L40, L48
- **error** L11 `budgets` formula hinges ×4 (> 3)
- **error** L32 `asides` aside ends in an exit formula
- **error** L40 `asides` aside ends in an exit formula
- **error** L48 `asides` aside ends in an exit formula
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?

### vol-3/ch-06-mutfili-kesmacoran.md

- **error** — `verbatim` verbatim Yule 63% (> 15%); worst: L4 97%, L11 71%, L15 88%, L17 77%, L21 92%
- **error** L15 `first_person` Book first person outside quotes: “I will tell”
- **error** L31 `archaism` archaism outside quotes: “hath”
- **error** L53 `archaism` archaism outside quotes: “whilst”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L45 `you_must_know` “You must know” outside quotes
- **error** L63 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×2 (> 1) at L19, L61
- **error** L19 `asides` 5 asides (> 4)
- **error** L19 `asides` aside ends in an exit formula
- **error** L61 `asides` aside ends in an exit formula
- **error** — `length` narrative 3630 words (outside 1800–3200)
- **warning** — `sentence` average sentence 25.4 words (> 25)
- **warning** L29 `names` “Banyan” is close to gazetteer name “Banan” (variant spelling?)

### vol-3/ch-07-male-abash.md

- **error** — `verbatim` verbatim Yule 46% (> 15%); worst: L19 81%, L21 76%, L52 82%
- **error** L34 `archaism` archaism outside quotes: “whilst”
- **error** L36 `archaism` archaism outside quotes: “’Tis”
- **error** L38 `archaism` archaism outside quotes: “whilst”
- **error** L52 `archaism` archaism outside quotes: “wherein”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L34, L46
- **error** L11 `budgets` formula hinges ×9 (> 3)
- **error** L15 `asides` aside 90 words (> 80)
- **error** L15 `asides` aside ends in an exit formula
- **error** L34 `asides` aside 110 words (> 80)
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?

### vol-3/ch-08-aden-hormos.md

- **error** — `verbatim` verbatim Yule 64% (> 15%); worst: L4 80%, L13 95%, L17 83%, L23 82%, L25 87%
- **error** L49 `first_person` Book first person outside quotes: “we will quit”
- **error** L17 `archaism` archaism outside quotes: “insomuch”
- **error** L17 `archaism` archaism outside quotes: “’tis”
- **error** L25 `archaism` archaism outside quotes: “Whilst”
- **error** L27 `archaism` archaism outside quotes: “’tis”
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L21, L35
- **error** L11 `budgets` formula hinges ×8 (> 3)
- **error** L15 `asides` 6 asides (> 4)
- **error** L15 `asides` aside 81 words (> 80)
- **error** L15 `asides` aside ends in an exit formula
- **error** L21 `asides` aside ends in an exit formula
- **error** L35 `asides` aside ends in an exit formula

### vol-3/ch-09-cocachin-return.md

- **error** — `verbatim` verbatim Yule 37% (> 15%); worst: L15 79%, L19 89%, L56 75%, L58 96%
- **error** L47 `first_person` Book first person outside quotes: “I should have told”
- **error** L60 `first_person` Book first person outside quotes: “What more shall I say”
- **error** L19 `archaism` archaism outside quotes: “sundry”
- **error** L58 `archaism` archaism outside quotes: “whilst”
- **warning** — `sentence` average sentence 36.3 words (> 25)
- **warning** L11 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L13 `name_policy` “Abaqa” used bare; the book form for this person is “Abaga” (S-05)
- **warning** L13 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L19 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L39 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L39 `name_policy` “Kukachi” used bare; the book form for this person is “Cocachin” (S-05)
- **warning** L39 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)
- **warning** L47 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)
- **warning** L60 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L60 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)

### vol-3/ch-10-ca-polo-milione.md

- **error** — `verbatim` verbatim Yule 38% (> 15%); worst: L4 100%, L17 83%
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L31 `archaism` archaism outside quotes: “whilst”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L15 `asides` aside ends in an exit formula
- **error** — `length` narrative 3244 words (outside 1800–3200)
- **warning** — `sentence` average sentence 32.9 words (> 25)

### vol-3/ch-11-afterlives.md

- **error** L18 `asides` aside 156 words (> 80)
- **error** L20 `asides` paragraph after an aside announces the return
- **error** L26 `asides` aside 215 words (> 80)
- **warning** L36 `openers` consecutive paragraphs open with “then the”
- **warning** — `sentence` average sentence 31.6 words (> 25)

### vol-3/ch-12-reliability-essay.md

- **error** — `length` narrative 3519 words (outside 2500–3500)
- **warning** L73 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)

