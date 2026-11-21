# Lint baseline

`python3 tools/lint.py --md` · 7/49 files pass. Errors decide pass/fail; warnings are prompts for the human read.

## Summary by check

| Check | Files with errors | Files with warnings |
|---|---|---|
| verbatim | 36 | 0 |
| first_person | 14 | 0 |
| archaism | 35 | 0 |
| you_must_know | 25 | 0 |
| budgets | 34 | 0 |
| asides | 36 | 0 |
| quotes | 1 | 0 |
| recaps | 7 | 23 |
| openers | 0 | 8 |
| length | 5 | 0 |
| sentence | 0 | 27 |
| ramusio | 0 | 4 |
| names | 0 | 12 |
| name_policy | 0 | 27 |
| captions | 3 | 0 |

## Per file

| File | Kind | Errors | Warnings | Words | Verbatim | Quotes | Asides | Ramusio flagged/expected | Failing checks |
|---|---|---|---|---|---|---|---|---|---|
| vol-1/back-01-trivia-and-disputes.md | frontback | 1 | 0 | 1262 | 1% |  |  |  | length |
| vol-1/ch-01-genoa-prison.md | narrative | 6 | 6 | 1974 | 7% | 1 | 2 | 3/0 | asides, budgets, quotes |
| vol-1/ch-02-house-of-polo.md | narrative | 12 | 9 | 2310 | 29% | 0 | 3 | 1/0 | archaism, asides, budgets, verbatim |
| vol-1/ch-03-second-setting-forth.md | narrative | 13 | 7 | 2587 | 33% | 0 | 4 | 3/1 | archaism, asides, budgets, verbatim |
| vol-1/ch-04-hermenia-georgiania.md | narrative | 11 | 3 | 2312 | 49% | 0 | 3 | 3/2 | archaism, asides, budgets, verbatim, you_must_know |
| vol-1/ch-05-mausul-baudas.md | narrative | 13 | 6 | 2944 | 61% | 0 | 3 | 3/1 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-06-tauris-persia.md | narrative | 13 | 4 | 2712 | 58% | 0 | 2 | 2/2 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-07-kerman-hormos.md | narrative | 11 | 4 | 2963 | 70% | 0 | 2 | 3/3 | archaism, asides, budgets, first_person, recaps, verbatim, you_must_know |
| vol-1/ch-08-arbre-sec-old-man.md | narrative | 6 | 4 | 2395 | 62% | 0 | 2 | 2/2 | archaism, asides, verbatim |
| vol-1/ch-09-balc-badashan.md | narrative | 10 | 8 | 3156 | 65% | 0 | 3 | 3/2 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-1/ch-10-pamier-cotan.md | narrative | 12 | 12 | 2792 | 50% | 0 | 2 | 5/5 | archaism, asides, budgets, verbatim |
| vol-1/ch-11-lop-tangut.md | narrative | 18 | 5 | 2782 | 45% | 0 | 4 | 4/4 | archaism, asides, budgets, recaps, verbatim, you_must_know |
| vol-1/ch-12-caracoron-tenduc.md | narrative | 14 | 14 | 3089 | 17% | 0 | 5 | 1/1 | archaism, asides, budgets, first_person, verbatim |
| vol-1/ch-13-chandu.md | narrative | 12 | 5 | 2626 | 57% | 0 | 3 | 3/4 | archaism, asides, budgets, verbatim, you_must_know |
| vol-1/front-01-world-before-the-road.md | frontback | 0 | 1 | 1188 | 2% |  |  |  | — |
| vol-1/front-02-maps-outbound.md | frontback | 2 | 0 | 578 | 2% |  |  |  | captions |
| vol-2/back-01-trivia-and-disputes.md | frontback | 0 | 0 | 862 | 3% |  |  |  | — |
| vol-2/ch-01-cublay-nayan.md | narrative | 21 | 11 | 3077 | 61% | 0 | 3 | 3/0 | archaism, asides, budgets, recaps, verbatim, you_must_know |
| vol-2/ch-02-person-palace.md | narrative | 0 | 5 | 1829 | 3% | 6 | 2 | 11/9 | — |
| vol-2/ch-03-feasts-keshican.md | narrative | 24 | 5 | 3094 | 80% | 0 | 2 | 5/6 | archaism, asides, budgets, recaps, verbatim, you_must_know |
| vol-2/ch-04-hunt-traffic.md | narrative | 24 | 4 | 3129 | 71% | 0 | 3 | 5/5 | archaism, asides, budgets, recaps, verbatim, you_must_know |
| vol-2/ch-05-ahmad-paper-coal.md | narrative | 15 | 5 | 3198 | 31% | 0 | 3 | 6/3 | archaism, asides, budgets, recaps, verbatim |
| vol-2/ch-06-pulisanghin-sindafu.md | narrative | 13 | 4 | 3034 | 63% | 0 | 2 | 4/4 | archaism, asides, budgets, recaps, verbatim |
| vol-2/ch-07-tebet-carajan.md | narrative | 10 | 6 | 3019 | 47% | 0 | 0 | 2/2 | archaism, budgets, verbatim |
| vol-2/ch-08-mien-bangala.md | narrative | 15 | 5 | 2819 | 78% | 0 | 1 | 1/1 | archaism, asides, budgets, verbatim, you_must_know |
| vol-2/ch-09-caugigu-cuiju.md | narrative | 10 | 3 | 2033 | 55% | 0 | 1 | 1/0 | archaism, asides, budgets, verbatim, you_must_know |
| vol-2/ch-10-manzi-sung.md | narrative | 19 | 10 | 2985 | 71% | 0 | 2 | 1/2 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-2/ch-11-yanju-saianfu.md | narrative | 13 | 10 | 2426 | 60% | 0 | 3 | 1/0 | archaism, asides, budgets, verbatim, you_must_know |
| vol-2/ch-12-kian-suju.md | narrative | 21 | 4 | 2526 | 62% | 0 | 4 | 3/2 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-2/ch-13-kinsay.md | narrative | 16 | 5 | 3343 | 44% | 0 | 3 | 10/4 | archaism, asides, budgets, first_person, length, verbatim, you_must_know |
| vol-2/ch-14-fuju-zayton.md | narrative | 19 | 4 | 2554 | 74% | 0 | 4 | 6/6 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-2/ch-15-great-turkey-ponent.md | narrative | 10 | 20 | 3108 | 52% | 0 | 3 | 0/0 | archaism, asides, budgets, verbatim, you_must_know |
| vol-2/front-01-yuan-china-context.md | frontback | 0 | 0 | 1030 | 2% |  |  |  | — |
| vol-2/front-02-maps-cathay-manzi.md | frontback | 2 | 0 | 421 | 8% |  |  |  | captions |
| vol-3/back-01-trivia-and-afterlives.md | frontback | 0 | 0 | 777 | 1% |  |  |  | — |
| vol-3/ch-01-ships-chipangu.md | narrative | 16 | 3 | 2273 | 48% | 0 | 3 | 6/4 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-02-chamba-java.md | narrative | 10 | 4 | 1791 | 47% | 0 | 3 | 1/1 | asides, budgets, length, verbatim, you_must_know |
| vol-3/ch-03-java-less-sumatra.md | narrative | 13 | 6 | 2247 | 62% | 0 | 2 | 3/5 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-04-necuveran-seilan.md | narrative | 22 | 3 | 2576 | 77% | 0 | 3 | 0/0 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-3/ch-05-maabar-st-thomas.md | narrative | 16 | 1 | 2761 | 38% | 0 | 3 | 2/1 | archaism, asides, budgets, first_person, verbatim, you_must_know |
| vol-3/ch-06-mutfili-kesmacoran.md | narrative | 13 | 2 | 3617 | 63% | 0 | 5 | 4/4 | archaism, asides, budgets, first_person, length, verbatim, you_must_know |
| vol-3/ch-07-male-abash.md | narrative | 11 | 1 | 2682 | 46% | 0 | 3 | 2/2 | archaism, asides, budgets, verbatim, you_must_know |
| vol-3/ch-08-aden-hormos.md | narrative | 13 | 0 | 2035 | 64% | 0 | 6 | 1/0 | archaism, asides, budgets, first_person, verbatim |
| vol-3/ch-09-cocachin-return.md | narrative | 5 | 11 | 2827 | 37% | 0 | 1 | 6/1 | archaism, first_person, verbatim |
| vol-3/ch-10-ca-polo-milione.md | narrative | 7 | 1 | 3225 | 38% | 0 | 1 | 8/0 | archaism, asides, length, verbatim |
| vol-3/ch-11-afterlives.md | narrative | 3 | 2 | 2513 | 3% | 0 | 2 | 4/0 | asides |
| vol-3/ch-12-reliability-essay.md | essay | 0 | 1 | 3490 | 1% |  |  |  | — |
| vol-3/front-01-indian-ocean-world.md | frontback | 0 | 0 | 898 | 1% |  |  |  | — |
| vol-3/front-02-maps-seas-and-return.md | frontback | 1 | 0 | 397 | 8% |  |  |  | captions |

## Issues

### vol-1/back-01-trivia-and-disputes.md

- **error** — `length` narrative 1262 words (outside 0–1200)

### vol-1/ch-01-genoa-prison.md

- **error** L21 `budgets` “Anyway” ×2 (> 1) at L21, L37
- **error** L21 `asides` aside 153 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 103 words (> 80)
- **error** L37 `asides` aside ends in an exit formula
- **error** L33 `quotes` marked quotation 50 words (> 25): “Great Princes, Emperors, and Kings, Duke…”
- **warning** L11 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** L25 `name_policy` “Rusticiano” used bare; the book form for this person is “Rustichello” (S-05)
- **warning** L25 `name_policy` “Rusticien” used bare; the book form for this person is “Rustichello” (S-05)
- **warning** L35 `name_policy` “Rusticiano” used bare; the book form for this person is “Rustichello” (S-05)

### vol-1/ch-02-house-of-polo.md

- **error** — `verbatim` verbatim Yule 29% (> 15%); worst: L23 73%
- **error** L23 `archaism` archaism outside quotes: “Whilst”
- **error** L23 `archaism` archaism outside quotes: “thereof”
- **error** L23 `archaism` archaism outside quotes: “hath”
- **error** L23 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “’tis”
- **error** L13 `budgets` “Anyway” ×2 (> 1) at L13, L31
- **error** L9 `budgets` formula hinges ×8 (> 3)
- **error** L13 `asides` aside ends in an exit formula
- **error** L31 `asides` aside 111 words (> 80)
- **error** L31 `asides` aside ends in an exit formula
- **error** L43 `asides` aside 105 words (> 80)
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 28.1 words (> 25)
- **warning** L15 `name_policy` “Berke” used bare; the book form for this person is “Barca” (S-05)
- **warning** L17 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L17 `name_policy` “Berke” used bare; the book form for this person is “Barca” (S-05)
- **warning** L21 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L31 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L15 `name_policy` first mention of “Barca” has no gloss (Berke) (S-05)

### vol-1/ch-03-second-setting-forth.md

- **error** — `verbatim` verbatim Yule 33% (> 15%); worst: L31 70%, L35 77%, L37 72%, L39 91%
- **error** L31 `archaism` archaism outside quotes: “sundry”
- **error** L31 `archaism` archaism outside quotes: “insomuch”
- **error** L37 `archaism` archaism outside quotes: “insomuch”
- **error** L13 `budgets` “Anyway” ×4 (> 1) at L13, L21, L25, L33
- **error** L9 `budgets` formula hinges ×6 (> 3)
- **error** L13 `asides` aside ends in an exit formula
- **error** L21 `asides` aside 123 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 118 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 109 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 28.9 words (> 25)
- **warning** L17 `name_policy` “Nicolas” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L19 `name_policy` “Bendocquedar” used bare; the book form for this person is “Bundukdar” (S-05)
- **warning** L25 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L19 `name_policy` first mention of “Bundukdar” has no gloss (Baibars) (S-05)
- **warning** L41 `name_policy` first mention of “Bolgana” has no gloss (Bulughan) (S-05)
- **warning** L41 `name_policy` first mention of “Cocachin” has no gloss (Kököchin) (S-05)

### vol-1/ch-04-hermenia-georgiania.md

- **error** — `verbatim` verbatim Yule 49% (> 15%); worst: L15 84%, L19 74%, L21 75%, L23 97%, L29 71%
- **error** L23 `archaism` archaism outside quotes: “insomuch”
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L33 `archaism` archaism outside quotes: “whilst”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L25
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside 130 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 98 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 29.8 words (> 25)
- **warning** L11 `names` “Hermenie” is close to gazetteer name “Hermenia” (variant spelling?)
- **warning** L13 `name_policy` first mention of “Bundukdar” has no gloss (Baibars) (S-05)

### vol-1/ch-05-mausul-baudas.md

- **error** — `verbatim` verbatim Yule 61% (> 15%); worst: L17 73%, L23 72%, L25 86%, L31 94%, L33 83%
- **error** L29 `first_person` Book first person outside quotes: “I will tell”
- **error** L49 `first_person` Book first person outside quotes: “I will tell”
- **error** L25 `archaism` archaism outside quotes: “wist”
- **error** L33 `archaism` archaism outside quotes: “whilst”
- **error** L43 `archaism` archaism outside quotes: “whilst”
- **error** L43 `archaism` archaism outside quotes: “insomuch”
- **error** L45 `archaism` archaism outside quotes: “thereof”
- **error** L11 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×2 (> 1) at L19, L27
- **error** L19 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 138 words (> 80)
- **error** L47 `asides` aside 108 words (> 80)
- **warning** L41 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.4 words (> 25)
- **warning** L15 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L27 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L27 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L27 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-06-tauris-persia.md

- **error** — `verbatim` verbatim Yule 58% (> 15%); worst: L21 74%, L23 100%, L25 100%, L27 100%, L29 93%
- **error** L13 `first_person` Book first person outside quotes: “we will quit”
- **error** L33 `first_person` Book first person outside quotes: “I will tell”
- **error** L23 `archaism` archaism outside quotes: “to wit”
- **error** L25 `archaism` archaism outside quotes: “thereof”
- **error** L25 `archaism` archaism outside quotes: “wherein”
- **error** L33 `archaism` archaism outside quotes: “to wit”
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×2 (> 1) at L15, L31
- **error** L15 `asides` aside ends in an exit formula
- **error** L31 `asides` aside 125 words (> 80)
- **error** L31 `asides` aside ends in an exit formula
- **warning** L27 `openers` consecutive paragraphs open with “and when”
- **warning** L37 `openers` consecutive paragraphs open with “in this”
- **warning** — `sentence` average sentence 26.2 words (> 25)
- **warning** L11 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-07-kerman-hormos.md

- **error** — `verbatim` verbatim Yule 70% (> 15%); worst: L13 76%, L15 78%, L19 93%, L23 83%, L27 74%
- **error** L41 `first_person` Book first person outside quotes: “we will quit”
- **error** L15 `archaism` archaism outside quotes: “thereof”
- **error** L23 `archaism` archaism outside quotes: “whilst”
- **error** L31 `archaism` archaism outside quotes: “to wit”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×2 (> 1) at L21, L37
- **error** L9 `budgets` formula hinges ×6 (> 3)
- **error** L21 `asides` aside ends in an exit formula
- **error** L37 `asides` aside ends in an exit formula
- **error** L41 `recaps` closing recap (181 words)
- **warning** — `sentence` average sentence 27.6 words (> 25)
- **warning** L23 `names` “Keshemur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L25 `names` “Conosalmi” is close to gazetteer name “Canosalmi” (variant spelling?)
- **warning** L23 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)

### vol-1/ch-08-arbre-sec-old-man.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L11 79%, L21 75%, L23 88%, L29 97%, L31 86%
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L25 `asides` aside 162 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L39 `asides` aside 138 words (> 80)
- **warning** L35 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 29.4 words (> 25)
- **warning** L37 `name_policy` “Alau” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L39 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-09-balc-badashan.md

- **error** — `verbatim` verbatim Yule 65% (> 15%); worst: L21 71%, L23 95%, L25 91%, L29 77%, L31 75%
- **error** L15 `first_person` Book first person outside quotes: “I will tell”
- **error** L47 `first_person` Book first person outside quotes: “we will quit”
- **error** L41 `archaism` archaism outside quotes: “insomuch”
- **error** L37 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L27, L39
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L27 `asides` aside ends in an exit formula
- **error** L39 `asides` aside ends in an exit formula
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** L23 `openers` consecutive paragraphs open with “when you”
- **warning** L33 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L13 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L13 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L17 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L35 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L45 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)

### vol-1/ch-10-pamier-cotan.md

- **error** — `verbatim` verbatim Yule 50% (> 15%); worst: L13 96%, L15 100%, L21 76%, L27 97%, L29 100%
- **error** L13 `archaism` archaism outside quotes: “’tis”
- **error** L13 `archaism` archaism outside quotes: “insomuch”
- **error** L27 `archaism` archaism outside quotes: “gat”
- **error** L27 `archaism` archaism outside quotes: “thereof”
- **error** L29 `archaism` archaism outside quotes: “wist”
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L31
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside 228 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L31 `asides` aside 150 words (> 80)
- **error** L31 `asides` aside ends in an exit formula
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.5 words (> 25)
- **warning** L19 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L37 `names` “Country” is close to gazetteer name “County” (variant spelling?)
- **warning** L43 `names` “Keria” is close to gazetteer name “Keriya” (variant spelling?)
- **warning** L23 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L23 `name_policy` “Kaidu” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L25 `name_policy` “Caidou” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L31 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L31 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L31 `name_policy` “Kaidu” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L37 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)

### vol-1/ch-11-lop-tangut.md

- **error** — `verbatim` verbatim Yule 45% (> 15%); worst: L27 73%, L37 76%
- **error** L9 `archaism` archaism outside quotes: “whilst”
- **error** L13 `archaism` archaism outside quotes: “’tis”
- **error** L21 `archaism` archaism outside quotes: “sundry”
- **error** L21 `archaism` archaism outside quotes: “whilst”
- **error** L23 `archaism` archaism outside quotes: “whilst”
- **error** L29 `archaism` archaism outside quotes: “whilst”
- **error** L39 `archaism` archaism outside quotes: “whilst”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×4 (> 1) at L17, L25, L31, L35
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside 105 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 82 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L35 `asides` aside ends in an exit formula
- **error** L43 `recaps` closing recap (138 words)
- **warning** — `sentence` average sentence 29.5 words (> 25)
- **warning** L29 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L29 `name_policy` “Mangu” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L31 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L35 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-1/ch-12-caracoron-tenduc.md

- **error** — `verbatim` verbatim Yule 17% (> 15%); worst: —
- **error** L11 `first_person` Book first person outside quotes: “I will tell”
- **error** L11 `archaism` archaism outside quotes: “wherein”
- **error** L15 `archaism` archaism outside quotes: “sundry”
- **error** L13 `budgets` “Anyway” ×5 (> 1) at L13, L19, L25, L29, L55
- **error** L9 `budgets` formula hinges ×7 (> 3)
- **error** L13 `asides` 5 asides (> 4)
- **error** L13 `asides` aside ends in an exit formula
- **error** L19 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 118 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L29 `asides` aside ends in an exit formula
- **error** L55 `asides` aside 93 words (> 80)
- **error** L55 `asides` aside ends in an exit formula
- **warning** L19 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L19 `name_policy` “Wang Khan” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L19 `name_policy` “Toghrul” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L25 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L25 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L25 `name_policy` “Aung Khan” used bare; the book form for this person is “Unc Can” (S-05)
- **warning** L27 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L29 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L29 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L29 `name_policy` “Qubilai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L29 `name_policy` “Hülegü” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L33 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L33 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L53 `name_policy` first mention of “King George” has no gloss (Körgüz of the Önggüd) (S-05)

### vol-1/ch-13-chandu.md

- **error** — `verbatim` verbatim Yule 57% (> 15%); worst: L15 76%, L19 84%, L21 90%, L25 74%, L31 90%
- **error** L15 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “to wit”
- **error** L31 `archaism` archaism outside quotes: “’Tis”
- **error** L37 `archaism` archaism outside quotes: “’Tis”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L23, L27
- **error** L17 `asides` aside 101 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L23 `asides` aside ends in an exit formula
- **error** L27 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 29.0 words (> 25)
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 3 paragraphs flag Ramusio (check: at a spot in the Park where th; It is stayed on gilt and lacke; They are cut across at each kn…)
- **warning** L41 `names` “Kesimur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L23 `name_policy` “Chinggis” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L11 `name_policy` first mention of “Cublay” has no gloss (Kublai) (S-05)

### vol-1/front-01-world-before-the-road.md

- **warning** L23 `names` “Mongolica” is close to gazetteer name “Mongolia” (variant spelling?)

### vol-1/front-02-maps-outbound.md

- **error** L27 `captions` caption goes in the image brackets, not a *Caption:* paragraph
- **error** L35 `captions` caption goes in the image brackets, not a *Caption:* paragraph

### vol-2/ch-01-cublay-nayan.md

- **error** — `verbatim` verbatim Yule 61% (> 15%); worst: L17 81%, L23 88%, L25 88%, L29 96%, L31 78%
- **error** L11 `archaism` archaism outside quotes: “hath”
- **error** L11 `archaism` archaism outside quotes: “existeth”
- **error** L11 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L17 `archaism` archaism outside quotes: “fain”
- **error** L23 `archaism` archaism outside quotes: “insomuch”
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L39 `archaism` archaism outside quotes: “whilst”
- **error** L43 `archaism` archaism outside quotes: “insomuch”
- **error** L45 `archaism` archaism outside quotes: “hath”
- **error** L45 `archaism` archaism outside quotes: “hath”
- **error** L45 `archaism` archaism outside quotes: “hath”
- **error** L45 `archaism` archaism outside quotes: “hath”
- **error** L29 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L19, L35
- **error** L11 `budgets` formula hinges ×7 (> 3)
- **error** L15 `asides` aside 113 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L35 `asides` aside 182 words (> 80)
- **error** L51 `recaps` closing recap (176 words)
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L41 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 29.8 words (> 25)
- **warning** L17 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L15 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L19 `name_policy` “Chinghiz” used bare; the book form for this person is “Chinghis” (S-05)
- **warning** L39 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L39 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L39 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L51 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-2/ch-02-person-palace.md

- **warning** L21 `name_policy` “Chingkim” used bare; the book form for this person is “Chinkin” (S-05)
- **warning** L21 `name_policy` “Temür” used bare; the book form for this person is “Temur” (S-05)
- **warning** L39 `name_policy` “Chingkim” used bare; the book form for this person is “Chinkin” (S-05)
- **warning** L39 `name_policy` “Temür” used bare; the book form for this person is “Temur” (S-05)
- **warning** L15 `name_policy` first mention of “Chinghis” has no gloss (Chinggis Khan) (S-05)

### vol-2/ch-03-feasts-keshican.md

- **error** — `verbatim` verbatim Yule 80% (> 15%); worst: L13 72%, L19 93%, L21 98%, L23 97%, L25 99%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L25 `archaism` archaism outside quotes: “doth”
- **error** L31 `archaism` archaism outside quotes: “doth”
- **error** L35 `archaism` archaism outside quotes: “’tis”
- **error** L37 `archaism` archaism outside quotes: “whilst”
- **error** L39 `archaism` archaism outside quotes: “sundry”
- **error** L39 `archaism` archaism outside quotes: “whilst”
- **error** L41 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “insomuch”
- **error** L43 `archaism` archaism outside quotes: “hath”
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L29 `you_must_know` “You must know” outside quotes
- **error** L31 `you_must_know` “You must know” outside quotes
- **error** L35 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×2 (> 1) at L15, L33
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L15 `asides` aside ends in an exit formula
- **error** L33 `asides` aside ends in an exit formula
- **error** L35 `asides` paragraph after an aside announces the return
- **error** L11 `recaps` opening recap
- **error** L45 `recaps` closing recap (115 words)
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L23 `openers` consecutive paragraphs open with “in ramusio's”
- **warning** — `sentence` average sentence 31.4 words (> 25)
- **warning** — `ramusio` first draft carried 6 Ramusio passages; 5 paragraphs flag Ramusio (check: Further, you are not to suppos; is set a large and very beauti; of the capacity of a firkin…)
- **warning** L33 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)

### vol-2/ch-04-hunt-traffic.md

- **error** — `verbatim` verbatim Yule 71% (> 15%); worst: L13 86%, L15 74%, L21 90%, L23 86%, L27 96%
- **error** L15 `archaism` archaism outside quotes: “hath”
- **error** L15 `archaism` archaism outside quotes: “hath”
- **error** L15 `archaism` archaism outside quotes: “hath”
- **error** L15 `archaism` archaism outside quotes: “’tis”
- **error** L21 `archaism` archaism outside quotes: “hath”
- **error** L21 `archaism` archaism outside quotes: “hath”
- **error** L21 `archaism` archaism outside quotes: “whilst”
- **error** L35 `archaism` archaism outside quotes: “whilst”
- **error** L41 `archaism` archaism outside quotes: “to wit”
- **error** L41 `archaism` archaism outside quotes: “to wit”
- **error** L49 `archaism` archaism outside quotes: “hath”
- **error** L49 `archaism` archaism outside quotes: “whilst”
- **error** L51 `archaism` archaism outside quotes: “’tis”
- **error** L53 `archaism` archaism outside quotes: “hath”
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L51 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L25, L31
- **error** L17 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L11 `recaps` opening recap
- **error** L57 `recaps` closing recap (93 words)
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L51 `openers` consecutive paragraphs open with “you must”
- **warning** — `sentence` average sentence 28.9 words (> 25)
- **warning** L57 `name_policy` first mention of “Achmath” has no gloss (Ahmad Fanakati) (S-05)

### vol-2/ch-05-ahmad-paper-coal.md

- **error** — `verbatim` verbatim Yule 31% (> 15%); worst: L13 72%
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L27 `archaism` archaism outside quotes: “hath”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L45 `archaism` archaism outside quotes: “thereof”
- **error** L47 `archaism` archaism outside quotes: “hath”
- **error** L49 `archaism` archaism outside quotes: “whilst”
- **error** L61 `archaism` archaism outside quotes: “hath”
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L31, L51
- **error** L17 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L51 `asides` aside ends in an exit formula
- **error** L11 `recaps` opening recap
- **error** L63 `recaps` closing recap (88 words)
- **warning** L19 `names` “Zhenjin” is close to gazetteer name “Zhenjiang” (variant spelling?)
- **warning** L17 `name_policy` “Jamui Khatun” used bare; the book form for this person is “Chabi” (S-05)
- **warning** L17 `name_policy` “Ahmad” used bare; the book form for this person is “Achmath” (S-05)
- **warning** L17 `name_policy` “Ahama” used bare; the book form for this person is “Achmath” (S-05)
- **warning** L25 `name_policy` “Ahmad” used bare; the book form for this person is “Achmath” (S-05)

### vol-2/ch-06-pulisanghin-sindafu.md

- **error** — `verbatim` verbatim Yule 63% (> 15%); worst: L21 82%, L23 74%, L27 71%, L29 76%, L31 88%
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L31 `archaism` archaism outside quotes: “hath”
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L35 `archaism` archaism outside quotes: “wherein”
- **error** L35 `archaism` archaism outside quotes: “sundry”
- **error** L35 `archaism` archaism outside quotes: “thereof”
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L25, L33
- **error** L11 `budgets` formula hinges ×8 (> 3)
- **error** L17 `asides` aside 200 words (> 80)
- **error** L33 `asides` aside 102 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **error** L47 `recaps` closing recap (98 words)
- **warning** — `sentence` average sentence 25.4 words (> 25)
- **warning** L11 `name_policy` “Ahmad” used bare; the book form for this person is “Achmath” (S-05)
- **warning** L33 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L33 `name_policy` “Mangala” used bare; the book form for this person is “Mangalai” (S-05)

### vol-2/ch-07-tebet-carajan.md

- **error** — `verbatim` verbatim Yule 47% (> 15%); worst: L13 78%, L25 70%, L47 75%
- **error** L21 `archaism` archaism outside quotes: “sundry”
- **error** L23 `archaism` archaism outside quotes: “wherein”
- **error** L27 `archaism` archaism outside quotes: “whilst”
- **error** L29 `archaism` archaism outside quotes: “sundry”
- **error** L33 `archaism` archaism outside quotes: “sundry”
- **error** L33 `archaism` archaism outside quotes: “sundry”
- **error** L47 `archaism` archaism outside quotes: “whilst”
- **error** L47 `archaism` archaism outside quotes: “’tis”
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **warning** L41 `openers` consecutive paragraphs open with “in this”
- **warning** L11 `name_policy` “Möngke” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L11 `name_policy` “Mongu” used bare; the book form for this person is “Mongou” (S-05)
- **warning** L33 `name_policy` “Temür” used bare; the book form for this person is “Temur” (S-05)
- **warning** L33 `name_policy` “Essentimur” used bare; the book form for this person is “Sentemur” (S-05)
- **warning** L37 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)

### vol-2/ch-08-mien-bangala.md

- **error** — `verbatim` verbatim Yule 78% (> 15%); worst: L15 93%, L19 81%, L21 99%, L23 100%, L25 100%
- **error** L15 `archaism` archaism outside quotes: “insomuch”
- **error** L19 `archaism` archaism outside quotes: “Natheless”
- **error** L23 `archaism` archaism outside quotes: “whilst”
- **error** L23 `archaism` archaism outside quotes: “wist”
- **error** L27 `archaism` archaism outside quotes: “trowed”
- **error** L31 `archaism` archaism outside quotes: “hath”
- **error** L43 `archaism` archaism outside quotes: “insomuch”
- **error** L45 `archaism` archaism outside quotes: “thereof”
- **error** L49 `archaism` archaism outside quotes: “insomuch”
- **error** L45 `you_must_know` “You must know” outside quotes
- **error** L45 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L47 `asides` aside ends in an exit formula
- **warning** L17 `recaps` “So/Thus …” restatement paragraph?
- **warning** L29 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 28.6 words (> 25)
- **warning** L13 `name_policy` first mention of “Sentemur” has no gloss (Esen-Temür) (S-05)

### vol-2/ch-09-caugigu-cuiju.md

- **error** — `verbatim` verbatim Yule 55% (> 15%); worst: L13 95%, L17 84%, L23 94%, L27 87%, L31 72%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “sundry”
- **error** L27 `archaism` archaism outside quotes: “to wit”
- **error** L37 `archaism` archaism outside quotes: “’tis”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L41 `asides` aside 125 words (> 80)
- **error** L41 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 28.0 words (> 25)

### vol-2/ch-10-manzi-sung.md

- **error** — `verbatim` verbatim Yule 71% (> 15%); worst: L13 77%, L15 90%, L19 77%, L21 78%, L25 86%
- **error** L67 `first_person` Book first person outside quotes: “I will tell”
- **error** L21 `archaism` archaism outside quotes: “hath”
- **error** L27 `archaism` archaism outside quotes: “thereof”
- **error** L37 `archaism` archaism outside quotes: “natheless”
- **error** L57 `archaism` archaism outside quotes: “thereof”
- **error** L59 `archaism` archaism outside quotes: “whilst”
- **error** L61 `archaism` archaism outside quotes: “wist”
- **error** L15 `you_must_know` “You must know” outside quotes
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L53 `you_must_know` “You must know” outside quotes
- **error** L71 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L55
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L55 `asides` aside ends in an exit formula
- **warning** L29 `recaps` “So/Thus …” restatement paragraph?
- **warning** L39 `recaps` “So/Thus …” restatement paragraph?
- **warning** L47 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 1 paragraphs flag Ramusio (check: There are also certain Christi; A great river passes through i…)
- **warning** L25 `name_policy` “Li Tan” used bare; the book form for this person is “Litan” (S-05)
- **warning** L29 `name_policy` “Li Tan” used bare; the book form for this person is “Litan” (S-05)
- **warning** L49 `name_policy` “Faghfur” used bare; the book form for this person is “Facfur” (S-05)
- **warning** L55 `name_policy` “Hulagu” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L61 `name_policy` “Siechi” used bare; the book form for this person is “Empress Dowager Xie” (S-05)
- **warning** L29 `name_policy` first mention of “Litan” has no gloss (Li Tan) (S-05)

### vol-2/ch-11-yanju-saianfu.md

- **error** — `verbatim` verbatim Yule 60% (> 15%); worst: L15 92%, L17 98%, L21 92%, L25 99%, L29 88%
- **error** L17 `archaism` archaism outside quotes: “insomuch”
- **error** L47 `archaism` archaism outside quotes: “wist”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L37 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L27 `budgets` “Anyway” ×3 (> 1) at L27, L39, L45
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L27 `asides` aside 237 words (> 80)
- **error** L39 `asides` aside 100 words (> 80)
- **error** L39 `asides` aside ends in an exit formula
- **error** L45 `asides` aside 249 words (> 80)
- **error** L45 `asides` aside ends in an exit formula
- **warning** L13 `recaps` “So/Thus …” restatement paragraph?
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?
- **warning** L31 `recaps` “So/Thus …” restatement paragraph?
- **warning** L49 `recaps` “So/Thus …” restatement paragraph?
- **warning** L17 `openers` consecutive paragraphs open with “when you”
- **warning** L41 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L43 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L45 `name_policy` “Abaqa” used bare; the book form for this person is “Abaga” (S-05)
- **warning** L49 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)

### vol-2/ch-12-kian-suju.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L13 97%, L17 92%, L19 93%, L23 85%, L29 96%
- **error** L17 `first_person` Book first person outside quotes: “I assure you”
- **error** L23 `first_person` Book first person outside quotes: “I can assure”
- **error** L23 `first_person` Book first person outside quotes: “we will quit”
- **error** L23 `archaism` archaism outside quotes: “’Tis”
- **error** L29 `archaism` archaism outside quotes: “hath”
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L57 `archaism` archaism outside quotes: “hath”
- **error** L61 `archaism` archaism outside quotes: “insomuch”
- **error** L13 `you_must_know` “You must know” outside quotes
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L59 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×4 (> 1) at L21, L41, L53, L63
- **error** L21 `budgets` formula hinges ×5 (> 3)
- **error** L21 `asides` aside ends in an exit formula
- **error** L41 `asides` aside 98 words (> 80)
- **error** L41 `asides` aside ends in an exit formula
- **error** L53 `asides` aside 140 words (> 80)
- **error** L53 `asides` aside ends in an exit formula
- **error** L63 `asides` aside 150 words (> 80)
- **error** L63 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L35 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 25.4 words (> 25)

### vol-2/ch-13-kinsay.md

- **error** — `verbatim` verbatim Yule 44% (> 15%); worst: L13 86%, L15 96%, L17 89%, L21 73%, L25 87%
- **error** L83 `first_person` Book first person outside quotes: “we will quit”
- **error** L15 `archaism` archaism outside quotes: “hath”
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L17 `archaism` archaism outside quotes: “thereof”
- **error** L39 `archaism` archaism outside quotes: “hath”
- **error** L47 `archaism` archaism outside quotes: “hath”
- **error** L51 `archaism` archaism outside quotes: “Certes”
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L35 `you_must_know` “You must know” outside quotes
- **error** L81 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×2 (> 1) at L19, L85
- **error** L19 `asides` aside 92 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L85 `asides` aside ends in an exit formula
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?
- **warning** L41 `recaps` “So/Thus …” restatement paragraph?
- **warning** L53 `recaps` “So/Thus …” restatement paragraph?
- **warning** L73 `recaps` “So/Thus …” restatement paragraph?
- **error** — `length` narrative 3343 words (outside 1800–3200)
- **warning** — `sentence` average sentence 26.4 words (> 25)

### vol-2/ch-14-fuju-zayton.md

- **error** — `verbatim` verbatim Yule 74% (> 15%); worst: L11 78%, L13 74%, L15 72%, L17 92%, L21 96%
- **error** L59 `first_person` Book first person outside quotes: “Let me tell you”
- **error** L67 `first_person` Book first person outside quotes: “We could tell you”
- **error** L21 `archaism` archaism outside quotes: “insomuch”
- **error** L29 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “’tis”
- **error** L53 `archaism` archaism outside quotes: “hath”
- **error** L59 `archaism` archaism outside quotes: “insomuch”
- **error** L67 `archaism` archaism outside quotes: “to wit”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L29 `you_must_know` “You must know” outside quotes
- **error** L31 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L53 `you_must_know` “You must know” outside quotes
- **error** L27 `budgets` “Anyway” ×3 (> 1) at L27, L51, L61
- **error** L11 `budgets` formula hinges ×6 (> 3)
- **error** L27 `asides` aside ends in an exit formula
- **error** L51 `asides` aside ends in an exit formula
- **error** L61 `asides` aside ends in an exit formula
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** L17 `openers` consecutive paragraphs open with “when you”

### vol-2/ch-15-great-turkey-ponent.md

- **error** — `verbatim` verbatim Yule 52% (> 15%); worst: L13 82%, L21 96%, L23 83%, L39 89%, L43 93%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “natheless”
- **error** L23 `archaism` archaism outside quotes: “gat”
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L19, L49
- **error** L15 `asides` aside ends in an exit formula
- **error** L19 `asides` aside ends in an exit formula
- **error** L49 `asides` aside ends in an exit formula
- **warning** L25 `recaps` “So/Thus …” restatement paragraph?
- **warning** L35 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 26.9 words (> 25)
- **warning** L13 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L13 `name_policy` “Chagatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L15 `name_policy` “Chaghatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L15 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L25 `name_policy` “Kaidu” used bare; the book form for this person is “Caidu” (S-05)
- **warning** L27 `name_policy` “Chaghatai” used bare; the book form for this person is “Sigatay” (S-05)
- **warning** L31 `name_policy` “Ulatai” used bare; the book form for this person is “Oulatay” (S-05)
- **warning** L35 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L35 `name_policy` “Ulatai” used bare; the book form for this person is “Oulatay” (S-05)
- **warning** L35 `name_policy` “Geikhatu” used bare; the book form for this person is “Kiacatu” (S-05)
- **warning** L51 `name_policy` “Alau” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L53 `name_policy` “Kublai” used bare; the book form for this person is “Cublay” (S-05)
- **warning** L53 `name_policy` “Alau” used bare; the book form for this person is “Alaü” (S-05)
- **warning** L13 `name_policy` first mention of “Cublay” has no gloss (Kublai) (S-05)
- **warning** L21 `name_policy` first mention of “Aijaruc” has no gloss (Khutulun) (S-05)
- **warning** L47 `name_policy` first mention of “Barca” has no gloss (Berke) (S-05)
- **warning** L53 `name_policy` first mention of “Cocachin” has no gloss (Kököchin) (S-05)

### vol-2/front-02-maps-cathay-manzi.md

- **error** L21 `captions` caption goes in the image brackets, not a *Caption:* paragraph
- **error** L29 `captions` caption goes in the image brackets, not a *Caption:* paragraph

### vol-3/ch-01-ships-chipangu.md

- **error** — `verbatim` verbatim Yule 48% (> 15%); worst: L23 76%, L29 89%, L41 72%, L43 75%
- **error** L13 `archaism` archaism outside quotes: “wherein”
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L25 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “’tis”
- **error** L11 `you_must_know` “You must know” outside quotes
- **error** L39 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L27, L35
- **error** L13 `budgets` formula hinges ×6 (> 3)
- **error** L11 `budgets` attribution verb “says” ×6 (> 4)
- **error** L15 `asides` aside ends in an exit formula
- **error** L27 `asides` aside ends in an exit formula
- **error** L35 `asides` aside 83 words (> 80)
- **error** L35 `asides` aside ends in an exit formula
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
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
- **error** L47 `archaism` archaism outside quotes: “sundry”
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L25 `budgets` “Anyway” ×2 (> 1) at L25, L39
- **error** L11 `budgets` formula hinges ×4 (> 3)
- **error** L25 `asides` aside ends in an exit formula
- **error** L39 `asides` aside ends in an exit formula
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 25.7 words (> 25)
- **warning** — `ramusio` first draft carried 5 Ramusio passages; 3 paragraphs flag Ramusio (check: and when savage with any one t; he landed with about 2000 men ; for there is great store of wo…)
- **warning** L21 `names` “Islanders” is close to gazetteer name “Islands” (variant spelling?)
- **warning** L33 `name_policy` first mention of “Cocachin” has no gloss (Kököchin) (S-05)

### vol-3/ch-04-necuveran-seilan.md

- **error** — `verbatim` verbatim Yule 77% (> 15%); worst: L13 89%, L17 95%, L21 94%, L25 96%, L27 95%
- **error** L13 `first_person` Book first person outside quotes: “I tell you”
- **error** L17 `first_person` Book first person outside quotes: “I assure you”
- **error** L25 `first_person` Book first person outside quotes: “Now I will”
- **error** L27 `first_person` Book first person outside quotes: “I tell you”
- **error** L29 `first_person` Book first person outside quotes: “I assure you”
- **error** L39 `first_person` Book first person outside quotes: “I have been telling”
- **error** L43 `first_person` Book first person outside quotes: “And why should I”
- **error** L13 `archaism` archaism outside quotes: “sundry”
- **error** L29 `archaism` archaism outside quotes: “thereof”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L25 `you_must_know` “You must know” outside quotes
- **error** L27 `you_must_know` “You must know” outside quotes
- **error** L19 `budgets` “Anyway” ×3 (> 1) at L19, L23, L37
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L19 `asides` aside ends in an exit formula
- **error** L23 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 98 words (> 80)
- **error** L37 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 26.7 words (> 25)

### vol-3/ch-05-maabar-st-thomas.md

- **error** — `verbatim` verbatim Yule 38% (> 15%); worst: L4 100%, L11 79%, L15 82%, L27 73%
- **error** L11 `first_person` Book first person outside quotes: “I will tell”
- **error** L15 `first_person` Book first person outside quotes: “I can tell you”
- **error** L19 `first_person` Book first person outside quotes: “I am going to”
- **error** L45 `first_person` Book first person outside quotes: “I will relate”
- **error** L15 `archaism` archaism outside quotes: “hath”
- **error** L23 `archaism` archaism outside quotes: “hath”
- **error** L27 `archaism` archaism outside quotes: “hath”
- **error** L11 `you_must_know` “You must know” outside quotes
- **error** L13 `you_must_know` “You must know” outside quotes
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L21 `budgets` “Anyway” ×3 (> 1) at L21, L29, L37
- **error** L11 `budgets` formula hinges ×4 (> 3)
- **error** L21 `asides` aside ends in an exit formula
- **error** L29 `asides` aside ends in an exit formula
- **error** L37 `asides` aside ends in an exit formula
- **warning** L17 `recaps` “So/Thus …” restatement paragraph?

### vol-3/ch-06-mutfili-kesmacoran.md

- **error** — `verbatim` verbatim Yule 63% (> 15%); worst: L4 97%, L11 71%, L13 88%, L15 77%, L19 92%
- **error** L13 `first_person` Book first person outside quotes: “I will tell”
- **error** L29 `archaism` archaism outside quotes: “hath”
- **error** L51 `archaism` archaism outside quotes: “whilst”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L61 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L59
- **error** L17 `asides` 5 asides (> 4)
- **error** L17 `asides` aside ends in an exit formula
- **error** L59 `asides` aside ends in an exit formula
- **error** — `length` narrative 3617 words (outside 1800–3200)
- **warning** — `sentence` average sentence 25.5 words (> 25)
- **warning** L27 `names` “Banyan” is close to gazetteer name “Banan” (variant spelling?)

### vol-3/ch-07-male-abash.md

- **error** — `verbatim` verbatim Yule 46% (> 15%); worst: L19 81%, L21 76%, L45 82%
- **error** L27 `archaism` archaism outside quotes: “whilst”
- **error** L29 `archaism` archaism outside quotes: “’Tis”
- **error** L31 `archaism` archaism outside quotes: “whilst”
- **error** L45 `archaism` archaism outside quotes: “wherein”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L27, L39
- **error** L11 `budgets` formula hinges ×9 (> 3)
- **error** L15 `asides` aside 90 words (> 80)
- **error** L15 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 110 words (> 80)
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

- **error** — `verbatim` verbatim Yule 37% (> 15%); worst: L15 79%, L19 89%, L41 75%, L43 96%
- **error** L39 `first_person` Book first person outside quotes: “I should have told”
- **error** L45 `first_person` Book first person outside quotes: “What more shall I say”
- **error** L19 `archaism` archaism outside quotes: “sundry”
- **error** L43 `archaism` archaism outside quotes: “whilst”
- **warning** — `sentence` average sentence 36.5 words (> 25)
- **warning** L11 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L13 `name_policy` “Abaqa” used bare; the book form for this person is “Abaga” (S-05)
- **warning** L13 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L19 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L37 `name_policy` “Arghun” used bare; the book form for this person is “Argon” (S-05)
- **warning** L37 `name_policy` “Kukachi” used bare; the book form for this person is “Cocachin” (S-05)
- **warning** L37 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)
- **warning** L39 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)
- **warning** L45 `name_policy` “Nicolo” used bare; the book form for this person is “Niccolò” (S-05)
- **warning** L45 `name_policy` “Ghazan” used bare; the book form for this person is “Casan” (S-05)

### vol-3/ch-10-ca-polo-milione.md

- **error** — `verbatim` verbatim Yule 38% (> 15%); worst: L4 100%, L17 83%
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L31 `archaism` archaism outside quotes: “whilst”
- **error** L35 `archaism` archaism outside quotes: “hath”
- **error** L15 `asides` aside ends in an exit formula
- **error** — `length` narrative 3225 words (outside 1800–3200)
- **warning** — `sentence` average sentence 32.7 words (> 25)

### vol-3/ch-11-afterlives.md

- **error** L18 `asides` aside 156 words (> 80)
- **error** L20 `asides` paragraph after an aside announces the return
- **error** L26 `asides` aside 215 words (> 80)
- **warning** L36 `openers` consecutive paragraphs open with “then the”
- **warning** — `sentence` average sentence 31.6 words (> 25)

### vol-3/ch-12-reliability-essay.md

- **warning** L61 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)

### vol-3/front-02-maps-seas-and-return.md

- **error** L21 `captions` caption goes in the image brackets, not a *Caption:* paragraph

