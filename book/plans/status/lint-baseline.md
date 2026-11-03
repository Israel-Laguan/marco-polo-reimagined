# Lint baseline

`python3 tools/lint.py --md` · 1/49 files pass. Errors decide pass/fail; warnings are prompts for the human read.

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
| quote_verify | 19 | 0 |
| recaps | 12 | 23 |
| openers | 0 | 7 |
| length | 6 | 0 |
| sentence | 0 | 30 |
| scaffolding | 40 | 0 |
| citations | 2 | 0 |
| markers | 33 | 0 |
| tags | 12 | 0 |
| ramusio | 28 | 20 |
| names | 0 | 14 |
| name_policy | 0 | 37 |

## Per file

| File | Kind | Errors | Warnings | Words | Verbatim | Quotes | Asides | Ramusio flagged/expected | Failing checks |
|---|---|---|---|---|---|---|---|---|---|
| vol-1/back-01-trivia-and-disputes.md | frontback | 4 | 0 |  | 0% |  |  |  | markers, quote_verify, scaffolding |
| vol-1/ch-01-genoa-prison.md | narrative | 6 | 6 | 1967 | 7% | 1 | 2 | 3/0 | asides, budgets, quotes |
| vol-1/ch-02-house-of-polo.md | narrative | 13 | 8 | 2326 | 28% | 0 | 3 | 1/0 | archaism, asides, budgets, scaffolding, verbatim |
| vol-1/ch-03-second-setting-forth.md | narrative | 17 | 25 | 2572 | 34% | 0 | 4 | 2/1 | archaism, asides, budgets, quote_verify, ramusio, scaffolding, verbatim |
| vol-1/ch-04-hermenia-georgiania.md | narrative | 16 | 18 | 2316 | 50% | 0 | 3 | 1/2 | archaism, asides, budgets, citations, ramusio, verbatim, you_must_know |
| vol-1/ch-05-mausul-baudas.md | narrative | 16 | 15 | 2933 | 62% | 0 | 3 | 2/1 | archaism, asides, budgets, first_person, ramusio, scaffolding, verbatim, you_must_know |
| vol-1/ch-06-tauris-persia.md | narrative | 18 | 18 | 2686 | 58% | 0 | 2 | 2/2 | archaism, asides, budgets, first_person, ramusio, scaffolding, verbatim, you_must_know |
| vol-1/ch-07-kerman-hormos.md | narrative | 18 | 9 | 2960 | 70% | 0 | 2 | 0/3 | archaism, asides, budgets, first_person, ramusio, recaps, scaffolding, verbatim, you_must_know |
| vol-1/ch-08-arbre-sec-old-man.md | narrative | 13 | 12 | 2389 | 62% | 0 | 2 | 0/2 | archaism, asides, ramusio, scaffolding, verbatim |
| vol-1/ch-09-balc-badashan.md | narrative | 21 | 19 | 3134 | 65% | 0 | 3 | 1/2 | archaism, asides, budgets, first_person, markers, ramusio, scaffolding, verbatim, you_must_know |
| vol-1/ch-10-pamier-cotan.md | narrative | 27 | 21 | 2766 | 51% | 0 | 2 | 1/5 | archaism, asides, budgets, markers, ramusio, scaffolding, verbatim |
| vol-1/ch-11-lop-tangut.md | narrative | 30 | 11 | 2756 | 47% | 0 | 4 | 0/4 | archaism, asides, budgets, ramusio, recaps, scaffolding, verbatim, you_must_know |
| vol-1/ch-12-caracoron-tenduc.md | narrative | 22 | 3 | 3091 | 17% | 0 | 5 | 0/1 | archaism, asides, budgets, first_person, markers, quote_verify, ramusio, scaffolding, verbatim |
| vol-1/ch-13-chandu.md | narrative | 21 | 15 | 2600 | 58% | 0 | 3 | 2/4 | archaism, asides, budgets, markers, ramusio, scaffolding, verbatim, you_must_know |
| vol-1/front-01-world-before-the-road.md | frontback | 5 | 1 |  | 1% |  |  |  | citations, markers, quote_verify, scaffolding |
| vol-1/front-02-maps-outbound.md | frontback | 9 | 0 |  | 0% |  |  |  | markers, quote_verify, scaffolding |
| vol-2/back-01-trivia-and-disputes.md | frontback | 4 | 0 |  | 0% |  |  |  | markers, quote_verify |
| vol-2/ch-01-cublay-nayan.md | narrative | 22 | 6 | 3082 | 61% | 0 | 3 | 3/0 | archaism, asides, budgets, recaps, scaffolding, verbatim, you_must_know |
| vol-2/ch-02-person-palace.md | narrative | 0 | 4 | 1871 | 3% | 6 | 2 | 11/9 | — |
| vol-2/ch-03-feasts-keshican.md | narrative | 36 | 4 | 3086 | 80% | 0 | 2 | 1/6 | archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim, you_must_know |
| vol-2/ch-04-hunt-traffic.md | narrative | 40 | 5 | 3120 | 72% | 0 | 3 | 1/5 | archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim, you_must_know |
| vol-2/ch-05-ahmad-paper-coal.md | narrative | 24 | 2 | 3211 | 31% | 0 | 3 | 4/3 | archaism, asides, budgets, length, markers, ramusio, recaps, verbatim |
| vol-2/ch-06-pulisanghin-sindafu.md | narrative | 22 | 11 | 3008 | 64% | 0 | 2 | 2/4 | archaism, asides, budgets, markers, ramusio, recaps, scaffolding, verbatim |
| vol-2/ch-07-tebet-carajan.md | narrative | 18 | 11 | 3067 | 46% | 0 | 0 | 2/2 | archaism, budgets, markers, ramusio, recaps, scaffolding, verbatim |
| vol-2/ch-08-mien-bangala.md | narrative | 20 | 17 | 2876 | 77% | 0 | 1 | 0/1 | archaism, asides, budgets, ramusio, recaps, scaffolding, tags, verbatim, you_must_know |
| vol-2/ch-09-caugigu-cuiju.md | narrative | 13 | 31 | 2030 | 55% | 0 | 1 | 1/0 | archaism, asides, budgets, markers, quote_verify, scaffolding, verbatim, you_must_know |
| vol-2/ch-10-manzi-sung.md | narrative | 25 | 20 | 3055 | 69% | 0 | 2 | 1/2 | archaism, asides, budgets, first_person, markers, quote_verify, ramusio, recaps, scaffolding, verbatim, you_must_know |
| vol-2/ch-11-yanju-saianfu.md | narrative | 17 | 17 | 2518 | 58% | 0 | 3 | 1/0 | archaism, asides, budgets, markers, recaps, scaffolding, verbatim, you_must_know |
| vol-2/ch-12-kian-suju.md | narrative | 25 | 27 | 2513 | 63% | 0 | 4 | 1/2 | archaism, asides, budgets, first_person, ramusio, verbatim, you_must_know |
| vol-2/ch-13-kinsay.md | narrative | 22 | 9 | 3375 | 44% | 0 | 3 | 7/4 | archaism, asides, budgets, first_person, length, ramusio, scaffolding, verbatim, you_must_know |
| vol-2/ch-14-fuju-zayton.md | narrative | 29 | 21 | 2628 | 72% | 0 | 4 | 1/6 | archaism, asides, budgets, first_person, ramusio, recaps, scaffolding, tags, verbatim, you_must_know |
| vol-2/ch-15-great-turkey-ponent.md | narrative | 11 | 9 | 3089 | 52% | 0 | 3 | 0/0 | archaism, asides, budgets, quote_verify, verbatim, you_must_know |
| vol-2/front-01-yuan-china-context.md | frontback | 3 | 0 |  | 1% |  |  |  | markers, quote_verify |
| vol-2/front-02-maps-cathay-manzi.md | frontback | 7 | 0 |  | 2% |  |  |  | markers, quote_verify, scaffolding |
| vol-3/back-01-trivia-and-afterlives.md | frontback | 3 | 0 |  | 0% |  |  |  | markers, quote_verify |
| vol-3/ch-01-ships-chipangu.md | narrative | 30 | 12 | 2246 | 49% | 0 | 3 | 2/4 | archaism, asides, budgets, markers, ramusio, scaffolding, verbatim, you_must_know |
| vol-3/ch-02-chamba-java.md | narrative | 27 | 11 | 1779 | 47% | 0 | 3 | 0/1 | asides, budgets, length, markers, quote_verify, ramusio, scaffolding, tags, verbatim, you_must_know |
| vol-3/ch-03-java-less-sumatra.md | narrative | 37 | 23 | 2171 | 64% | 0 | 2 | 0/5 | archaism, asides, budgets, markers, ramusio, scaffolding, tags, verbatim, you_must_know |
| vol-3/ch-04-necuveran-seilan.md | narrative | 39 | 12 | 2582 | 77% | 0 | 3 | 0/0 | archaism, asides, budgets, first_person, markers, scaffolding, tags, verbatim, you_must_know |
| vol-3/ch-05-maabar-st-thomas.md | narrative | 35 | 13 | 2747 | 39% | 0 | 3 | 1/1 | archaism, asides, budgets, first_person, markers, ramusio, scaffolding, tags, verbatim, you_must_know |
| vol-3/ch-06-mutfili-kesmacoran.md | narrative | 42 | 9 | 3609 | 64% | 0 | 5 | 0/4 | archaism, asides, budgets, first_person, length, markers, ramusio, scaffolding, verbatim, you_must_know |
| vol-3/ch-07-male-abash.md | narrative | 20 | 19 | 2671 | 46% | 0 | 3 | 0/2 | archaism, asides, budgets, markers, quote_verify, ramusio, scaffolding, tags, verbatim, you_must_know |
| vol-3/ch-08-aden-hormos.md | narrative | 21 | 6 | 2034 | 64% | 0 | 6 | 1/0 | archaism, asides, budgets, first_person, markers, quote_verify, scaffolding, tags, verbatim |
| vol-3/ch-09-cocachin-return.md | narrative | 13 | 14 | 2709 | 39% | 0 | 1 | 4/1 | archaism, first_person, markers, ramusio, scaffolding, tags, verbatim |
| vol-3/ch-10-ca-polo-milione.md | narrative | 35 | 1 | 3321 | 37% | 0 | 1 | 8/0 | archaism, asides, length, markers, scaffolding, tags, verbatim |
| vol-3/ch-11-afterlives.md | narrative | 52 | 2 | 2634 | 0% | 0 | 2 | 4/0 | asides, markers, quote_verify, scaffolding, tags |
| vol-3/ch-12-reliability-essay.md | essay | 81 | 2 | 3753 | 0% |  |  |  | length, markers, quote_verify, scaffolding, tags |
| vol-3/front-01-indian-ocean-world.md | frontback | 4 | 0 |  | 0% |  |  |  | markers, quote_verify, scaffolding |
| vol-3/front-02-maps-seas-and-return.md | frontback | 4 | 0 |  | 0% |  |  |  | markers, quote_verify, scaffolding |

## Issues

### vol-1/back-01-trivia-and-disputes.md

- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “i did not tell half of what i saw for i knew i wou”
- **error** L83 `scaffolding` scaffolding: “/workspace”
- **error** L63 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L83 `markers` Note [11] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-1/ch-01-genoa-prison.md

- **error** L21 `budgets` “Anyway” ×2 (> 1) at L21, L37
- **error** L21 `asides` aside 153 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 102 words (> 80)
- **error** L37 `asides` aside ends in an exit formula
- **error** L33 `quotes` marked quotation 50 words (> 25): “Great Princes, Emperors, and Kings, Duke…”
- **warning** L11 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** L35 `name_policy` “Pagan” used bare; the book form is “Mien” (gloss it beside the book form, once)
- **warning** L13 `name_policy` first mention of “Tana” has no modern gloss (Thane)
- **warning** L13 `name_policy` first mention of “Trebizond” has no modern gloss (Trabzon)

### vol-1/ch-02-house-of-polo.md

- **error** — `verbatim` verbatim Yule 28% (> 15%); worst: L23 73%
- **error** L23 `archaism` archaism outside quotes: “Whilst”
- **error** L23 `archaism` archaism outside quotes: “thereof”
- **error** L23 `archaism` archaism outside quotes: “hath”
- **error** L23 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “’tis”
- **error** L13 `budgets` “Anyway” ×2 (> 1) at L13, L31
- **error** L9 `budgets` formula hinges ×8 (> 3)
- **error** L13 `asides` aside ends in an exit formula
- **error** L31 `asides` aside 118 words (> 80)
- **error** L31 `asides` aside ends in an exit formula
- **error** L43 `asides` aside 105 words (> 80)
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 28.3 words (> 25)
- **error** L31 `scaffolding` scaffolding: “asides have to be honest”
- **warning** L21 `name_policy` “Bukhara” used bare; the book form is “Bocara” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Cilician Armenia” used bare; the book form is “Lesser Hermenia” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L15 `name_policy` first mention of “Bolghar” has no modern gloss (Bolgar)

### vol-1/ch-03-second-setting-forth.md

- **error** — `verbatim` verbatim Yule 34% (> 15%); worst: L31 70%, L35 77%, L37 72%, L39 96%
- **error** L31 `archaism` archaism outside quotes: “sundry”
- **error** L31 `archaism` archaism outside quotes: “insomuch”
- **error** L37 `archaism` archaism outside quotes: “insomuch”
- **error** L13 `budgets` “Anyway” ×4 (> 1) at L13, L21, L25, L33
- **error** L9 `budgets` formula hinges ×6 (> 3)
- **error** L13 `asides` aside ends in an exit formula
- **error** L21 `asides` aside 130 words (> 80)
- **error** L21 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 118 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 107 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 67% of 5-grams match): “sire tis my son and your liegeman”
- **warning** — `sentence` average sentence 28.4 words (> 25)
- **error** L21 `scaffolding` scaffolding: “aside has to be honest”
- **error** L39 `ramusio` Ramusio-only passage without an inline flag
- **error** L39 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [16]
- **warning** L13 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Cilician Armenia” used bare; the book form is “Lesser Hermenia” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Cilician Armenia” used bare; the book form is “Lesser Hermenia” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Sivas” used bare; the book form is “Savast” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Mosul” used bare; the book form is “Mausul” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Balkh” used bare; the book form is “Balc” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Pamir” used bare; the book form is “Pamier” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Kashgar” used bare; the book form is “Cascar” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Yarkand” used bare; the book form is “Yarcan” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Khotan” used bare; the book form is “Cotan” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Pamir” used bare; the book form is “Pamier” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Kemenfu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Jurchen” used bare; the book form is “Chorcha” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Karajang” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Kemenfu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L33 `name_policy` first mention of “Suju” has no modern gloss (Suzhou)

### vol-1/ch-04-hermenia-georgiania.md

- **error** — `verbatim` verbatim Yule 50% (> 15%); worst: L15 83%, L19 74%, L21 76%, L23 97%, L29 71%
- **error** L23 `archaism` archaism outside quotes: “insomuch”
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L33 `archaism` archaism outside quotes: “whilst”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L25
- **error** L9 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside 130 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 97 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 29.5 words (> 25)
- **error** L71 `citations` Note [15] is never cited
- **error** L21 `ramusio` Ramusio-only passage without an inline flag
- **error** L21 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [7]
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [13]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 1 paragraphs flag Ramusio (check: on the summit of which snow is; The said sea produces quantiti…)
- **warning** L11 `names` “Hermenie” is close to gazetteer name “Hermenia” (variant spelling?)
- **warning** L13 `name_policy` “Layas” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L13 `name_policy` “Sivas” used bare; the book form is “Savast” (gloss it beside the book form, once)
- **warning** L13 `name_policy` “Erzingan” used bare; the book form is “Arzinga” (gloss it beside the book form, once)
- **warning** L13 `name_policy` “Erzrum” used bare; the book form is “Arziron” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Iconium” used bare; the book form is “Conia” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Mosul” used bare; the book form is “Mausul” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Georgia” used bare; the book form is “Georgiania” (gloss it beside the book form, once)
- **warning** L29 `name_policy` “Iron Gate” used bare; the book form is “Derbend” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Erzingan” used bare; the book form is “Arzinga” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Iron Gate” used bare; the book form is “Derbend” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Mosul” used bare; the book form is “Mausul” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L9 `name_policy` first mention of “Ayas” has no modern gloss (Yumurtalık (Ayas))
- **warning** L37 `name_policy` first mention of “Baudas” has no modern gloss (Baghdad)

### vol-1/ch-05-mausul-baudas.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L17 73%, L23 72%, L25 86%, L31 94%, L33 83%
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
- **error** L47 `asides` aside 107 words (> 80)
- **warning** L41 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.3 words (> 25)
- **error** L87 `scaffolding` scaffolding: “reported_only”
- **error** L13 `ramusio` Ramusio-only passage without an inline flag
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **warning** L11 `name_policy` “Mosul” used bare; the book form is “Mausul” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Peking” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Kish” used bare; the book form is “Kisi” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Basra” used bare; the book form is “Bastra” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Mosul” used bare; the book form is “Mausul” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Kish” used bare; the book form is “Kisi” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L11 `name_policy` first mention of “Baudas” has no modern gloss (Baghdad)
- **warning** L47 `name_policy` first mention of “Tauris” has no modern gloss (Tabriz)

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
- **warning** — `sentence` average sentence 26.0 words (> 25)
- **error** L49 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L69 `scaffolding` scaffolding: “Dispute hook”
- **error** L79 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **error** L39 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [15]
- **warning** L33 `names` “Tunocain” is close to gazetteer name “Tonocain” (variant spelling?)
- **warning** L11 `name_policy` “Laias” used bare; the book form is “Ayas” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Yazd” used bare; the book form is “Yasdi” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Tibet” used bare; the book form is “Tebet” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Dry Tree” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Kish” used bare; the book form is “Kisi” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Sava” used bare; the book form is “Saba” (gloss it beside the book form, once)
- **warning** L9 `name_policy` first mention of “Baudas” has no modern gloss (Baghdad)
- **warning** L35 `name_policy` first mention of “Kisi” has no modern gloss (Kish (Qays) Island)

### vol-1/ch-07-kerman-hormos.md

- **error** — `verbatim` verbatim Yule 70% (> 15%); worst: L13 78%, L15 73%, L19 93%, L23 82%, L27 74%
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
- **error** L49 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L15 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **error** L35 `ramusio` Ramusio-only passage without an inline flag
- **error** L35 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [13]
- **error** L39 `ramusio` Ramusio-only passage without an inline flag
- **error** L39 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [14]
- **warning** — `ramusio` first draft carried 3 Ramusio passages; 0 paragraphs flag Ramusio (check: There are vast numbers of turt; And to prove the great heat of; And they have women who are mo…)
- **warning** L23 `names` “Keshemur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L25 `names` “Conosalmi” is close to gazetteer name “Canosalmi” (variant spelling?)
- **warning** L23 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Kish” used bare; the book form is “Kisi” (gloss it beside the book form, once)
- **warning** L13 `name_policy` first mention of “Camadi” has no modern gloss (Kamadin (ruins)
- **warning** L43 `name_policy` first mention of “Cobinan” has no modern gloss (Kuhbanan)

### vol-1/ch-08-arbre-sec-old-man.md

- **error** — `verbatim` verbatim Yule 62% (> 15%); worst: L11 79%, L19 75%, L21 91%, L27 97%, L29 86%
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L23 `asides` aside 169 words (> 80)
- **error** L23 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 138 words (> 80)
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 29.3 words (> 25)
- **error** L49 `scaffolding` scaffolding: “likely_visited”
- **error** L53 `scaffolding` scaffolding: “Gazetteer: Tonocain / Arbre Sec *uncerta”
- **error** L57 `scaffolding` scaffolding: “reported_only”
- **error** L13 `ramusio` Ramusio-only passage without an inline flag
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **error** L35 `ramusio` Ramusio-only passage without an inline flag
- **error** L35 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [12]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 0 paragraphs flag Ramusio (check: you arrive at a stream of fres; and the Castle with its Garden…)
- **warning** L21 `name_policy` “Dry Tree” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Tree of the Sun” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Dry Tree” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Tree of the Sun” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Mulehet” used bare; the book form is “Old Man of the Mountain” (gloss it beside the book form, once)
- **warning** L9 `name_policy` first mention of “Reobarles” has no modern gloss (Rudbar (Rudbari))
- **warning** L9 `name_policy` first mention of “Hormos” has no modern gloss (Old Hormuz (near Minab))
- **warning** L25 `name_policy` first mention of “Old Man of the Mountain” has no modern gloss (Alamut)
- **warning** L39 `name_policy` first mention of “Sapurgan” has no modern gloss (Shibarghan)

### vol-1/ch-09-balc-badashan.md

- **error** — `verbatim` verbatim Yule 65% (> 15%); worst: L21 71%, L23 93%, L25 91%, L29 77%, L31 76%
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
- **error** L27 `scaffolding` scaffolding: “dispute hook”
- **error** L45 `scaffolding` scaffolding: “dispute hook”
- **error** L55 `scaffolding` scaffolding: “likely_visited”
- **error** L57 `scaffolding` scaffolding: “Gazetteer: Balkh *visited*”
- **error** L61 `scaffolding` scaffolding: “likely_visited”
- **error** L83 `markers` Note [16] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L83 `markers` Note [16] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L31 `ramusio` Ramusio-only passage without an inline flag
- **error** L31 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [10]
- **error** L43 `ramusio` Ramusio-only passage without an inline flag
- **error** L43 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [15]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 1 paragraphs flag Ramusio (check: They go at a great pace even d; The people of the province do …)
- **warning** L33 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L11 `name_policy` “Dry Tree” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Balkh” used bare; the book form is “Balc” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Talikan” used bare; the book form is “Taican” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L31 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Pamir” used bare; the book form is “Pamier” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L39 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L45 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L45 `name_policy` “Tibet” used bare; the book form is “Tebet” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L17 `name_policy` first mention of “Taican” has no modern gloss (Taloqan)
- **warning** L37 `name_policy` first mention of “Pashai” has no modern gloss (Pashai country (Laghman–Kunar))
- **warning** L47 `name_policy` first mention of “Pamier” has no modern gloss (Pamir Plateau (Tajikistan/Afghanistan))

### vol-1/ch-10-pamier-cotan.md

- **error** — `verbatim` verbatim Yule 51% (> 15%); worst: L13 98%, L15 92%, L21 76%, L27 97%, L29 100%
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
- **warning** — `sentence` average sentence 27.0 words (> 25)
- **error** L51 `scaffolding` scaffolding: “Gazetteer: Wakhan *visited*”
- **error** L55 `scaffolding` scaffolding: “Gazetteer: Pamir *visited*”
- **error** L61 `scaffolding` scaffolding: “Gazetteer: Kashgar *visited*”
- **error** L71 `scaffolding` scaffolding: “Dispute hook”
- **error** L73 `scaffolding` scaffolding: “Gazetteer: Yarkand *visited*”
- **error** L75 `scaffolding` scaffolding: “Gazetteer: Khotan *visited*”
- **error** L81 `scaffolding` scaffolding: “Gazetteer: Pem *uncertain*”
- **error** L71 `markers` Note [12] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L13 `ramusio` Ramusio-only passage without an inline flag
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [13]
- **error** L35 `ramusio` Ramusio-only passage without an inline flag
- **error** L35 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [14]
- **error** L41 `ramusio` Ramusio-only passage without an inline flag
- **warning** — `ramusio` first draft carried 5 Ramusio passages; 1 paragraphs flag Ramusio (check: a great lake between two mount; Messer Marco was told also tha; particularly of cotton. The in…)
- **warning** L19 `names` “Faizabad” is close to gazetteer name “Fayzabad” (variant spelling?)
- **warning** L37 `names` “Country” is close to gazetteer name “County” (variant spelling?)
- **warning** L43 `names` “Keria” is close to gazetteer name “Keriya” (variant spelling?)
- **warning** L9 `name_policy` “Kishm” used bare; the book form is “Casem” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Pamir” used bare; the book form is “Pamier” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Badakhshan” used bare; the book form is “Badashan” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Kashgar” used bare; the book form is “Cascar” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Yarkand” used bare; the book form is “Yarcan” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Yarkand” used bare; the book form is “Yarcan” (gloss it beside the book form, once)
- **warning** L31 `name_policy` “Samarkand” used bare; the book form is “Samarcan” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Yarkand” used bare; the book form is “Yarcan” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Kashgar” used bare; the book form is “Cascar” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Khotan” used bare; the book form is “Cotan” (gloss it beside the book form, once)
- **warning** L25 `name_policy` first mention of “Bocara” has no modern gloss (Bukhara)
- **warning** L23 `name_policy` first mention of “Yarcan” has no modern gloss (Yarkand (Yarkant))
- **warning** L43 `name_policy` first mention of “Charchan” has no modern gloss (Qiemo (Cherchen))
- **warning** L41 `name_policy` first mention of “Lop” has no modern gloss (Charklik / Ruoqiang)

### vol-1/ch-11-lop-tangut.md

- **error** — `verbatim` verbatim Yule 47% (> 15%); worst: L27 74%, L37 79%
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
- **error** L17 `asides` aside 104 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 81 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L35 `asides` aside ends in an exit formula
- **error** L43 `recaps` closing recap (138 words)
- **warning** — `sentence` average sentence 29.2 words (> 25)
- **error** L49 `scaffolding` scaffolding: “likely_visited”
- **error** L51 `scaffolding` scaffolding: “gazetteer *visited*”
- **error** L65 `scaffolding` scaffolding: “reported_only”
- **error** L75 `scaffolding` scaffolding: “gazetteer Succiu *visited*”
- **error** L77 `scaffolding` scaffolding: “gazetteer *visited*”
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L15 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **error** L19 `ramusio` Ramusio-only passage without an inline flag
- **error** L29 `ramusio` Ramusio-only passage without an inline flag
- **error** L29 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [10]
- **error** L37 `ramusio` Ramusio-only passage without an inline flag
- **error** L37 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [14]
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 0 paragraphs flag Ramusio (check: Sometimes the stray travellers; Hence in making this journey ’; but to provide public hostelri…)
- **warning** L11 `name_policy` “Charklik” used bare; the book form is “Lop” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Shachau” used bare; the book form is “Sachiu” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Jiuquan” used bare; the book form is “Sukchur” (gloss it beside the book form, once)
- **warning** L25 `name_policy` first mention of “Samarcan” has no modern gloss (Samarkand)
- **warning** L9 `name_policy` first mention of “Cotan” has no modern gloss (Hotan)
- **warning** L9 `name_policy` first mention of “Pein” has no modern gloss (Keriya / Uzun-Tati area)
- **warning** L27 `name_policy` first mention of “Desert of Lop” has no modern gloss (Lop Desert)
- **warning** L41 `name_policy` first mention of “Etzina” has no modern gloss (Khara-Khoto (Ejina))
- **warning** L41 `name_policy` first mention of “Caracoron” has no modern gloss (Karakorum (Kharkhorin))

### vol-1/ch-12-caracoron-tenduc.md

- **error** — `verbatim` verbatim Yule 17% (> 15%); worst: —
- **error** L11 `first_person` Book first person outside quotes: “I will tell”
- **error** L11 `archaism` archaism outside quotes: “wherein”
- **error** L15 `archaism` archaism outside quotes: “sundry”
- **error** L13 `budgets` “Anyway” ×5 (> 1) at L13, L19, L25, L29, L53
- **error** L9 `budgets` formula hinges ×7 (> 3)
- **error** L13 `asides` 5 asides (> 4)
- **error** L13 `asides` aside ends in an exit formula
- **error** L19 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 125 words (> 80)
- **error** L25 `asides` aside ends in an exit formula
- **error** L29 `asides` aside ends in an exit formula
- **error** L53 `asides` aside 92 words (> 80)
- **error** L53 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 96% of 5-grams match): “and when chinghis kaan heard the brutal message th”
- **error** L25 `scaffolding` scaffolding: “asides have to be honest”
- **error** L63 `scaffolding` scaffolding: “likely_visited”
- **error** L65 `scaffolding` scaffolding: “reported_only”
- **error** L103 `scaffolding` scaffolding: “gazetteer Tenduc *uncertain*”
- **error** L79 `markers` Note [9] uses retired marker ★
- **error** L39 `ramusio` Ramusio-only passage without an inline flag
- **error** L39 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [15]
- **warning** — `ramusio` first draft carried 1 Ramusio passages; 0 paragraphs flag Ramusio (check: They say there is a Most High …)
- **warning** L49 `name_policy` “Calachan” used bare; the book form is “Egrigaia” (gloss it beside the book form, once)
- **warning** L53 `name_policy` “Peking” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)

### vol-1/ch-13-chandu.md

- **error** — `verbatim` verbatim Yule 58% (> 15%); worst: L15 85%, L19 84%, L21 90%, L25 75%, L31 90%
- **error** L15 `archaism` archaism outside quotes: “whilst”
- **error** L19 `archaism` archaism outside quotes: “to wit”
- **error** L31 `archaism` archaism outside quotes: “’Tis”
- **error** L37 `archaism` archaism outside quotes: “’Tis”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L23, L27
- **error** L17 `asides` aside 102 words (> 80)
- **error** L17 `asides` aside ends in an exit formula
- **error** L23 `asides` aside ends in an exit formula
- **error** L27 `asides` aside ends in an exit formula
- **warning** — `sentence` average sentence 28.4 words (> 25)
- **error** L27 `scaffolding` scaffolding: “. Narrate”
- **error** L49 `scaffolding` scaffolding: “gazetteer Shangdu *visited*”
- **error** L67 `scaffolding` scaffolding: “Dispute hook”
- **error** L57 `markers` Note [5] uses retired marker ★
- **error** L57 `markers` Note [5] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L67 `markers` Note [10] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L67 `markers` Note [10] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L15 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 2 paragraphs flag Ramusio (check: at a spot in the Park where th; It is stayed on gilt and lacke; They are cut across at each kn…)
- **warning** L25 `names` “Kesimur” is close to gazetteer name “Keshimur” (variant spelling?)
- **warning** L11 `name_policy` “Kemenfu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Peking” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Shangdu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Kashmir” used bare; the book form is “Keshimur” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Tibet” used bare; the book form is “Tebet” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Shangdu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L39 `name_policy` “Shangdu” used bare; the book form is “Chandu” (gloss it beside the book form, once)
- **warning** L9 `name_policy` first mention of “Lop” has no modern gloss (Charklik / Ruoqiang)
- **warning** L41 `name_policy` first mention of “Etzina” has no modern gloss (Khara-Khoto (Ejina))
- **warning** L9 `name_policy` first mention of “Caracoron” has no modern gloss (Karakorum (Kharkhorin))
- **warning** L9 `name_policy` first mention of “Tenduc” has no modern gloss (Tumed / Hohhot region)
- **warning** L25 `name_policy` first mention of “Tebet” has no modern gloss (Eastern Tibet / Kham region)

### vol-1/front-01-world-before-the-road.md

- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 50% of 5-grams match): “ye must know that in the year of christ”
- **error** L82 `scaffolding` scaffolding: “/workspace”
- **error** — `citations` body citations not sequential 1..n: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
- **error** L64 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L82 `markers` Note [10] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **warning** L21 `names` “Mongolica” is close to gazetteer name “Mongolia” (variant spelling?)

### vol-1/front-02-maps-outbound.md

- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 21% of 5-grams match): “and you may know that from this city of lop it is ”
- **error** L9 `scaffolding` scaffolding: “placeholder”
- **error** L9 `scaffolding` scaffolding: “project gazetteer”
- **error** L100 `scaffolding` scaffolding: “/workspace”
- **error** L100 `scaffolding` scaffolding: “/workspace”
- **error** L108 `scaffolding` scaffolding: “Soft IDs:”
- **error** L108 `scaffolding` scaffolding: “likely_visited”
- **error** L108 `scaffolding` scaffolding: “reported_only”
- **error** L100 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-2/back-01-trivia-and-disputes.md

- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “all these cities are so great that”
- **error** L57 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L67 `markers` Note [6] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L69 `markers` Note [7] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

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
- **error** L49 `recaps` closing recap (176 words)
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L41 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 29.5 words (> 25)
- **error** L19 `scaffolding` scaffolding: “asides have to be honest”
- **warning** L17 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L19 `name_policy` “Korea” used bare; the book form is “Cauly” (gloss it beside the book form, once)

### vol-2/ch-02-person-palace.md

- **warning** L23 `name_policy` “Dadu” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Beijing” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Taidu” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Taidu” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)

### vol-2/ch-03-feasts-keshican.md

- **error** — `verbatim` verbatim Yule 80% (> 15%); worst: L13 72%, L17 95%, L19 100%, L21 99%, L23 99%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L23 `archaism` archaism outside quotes: “doth”
- **error** L29 `archaism` archaism outside quotes: “doth”
- **error** L33 `archaism` archaism outside quotes: “’tis”
- **error** L35 `archaism` archaism outside quotes: “whilst”
- **error** L37 `archaism` archaism outside quotes: “sundry”
- **error** L37 `archaism` archaism outside quotes: “whilst”
- **error** L39 `archaism` archaism outside quotes: “hath”
- **error** L39 `archaism` archaism outside quotes: “insomuch”
- **error** L41 `archaism` archaism outside quotes: “hath”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L27 `you_must_know` “You must know” outside quotes
- **error** L29 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L39 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×2 (> 1) at L15, L31
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L15 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L33 `asides` paragraph after an aside announces the return
- **error** L11 `recaps` opening recap
- **error** L43 `recaps` closing recap (115 words)
- **warning** L25 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 31.0 words (> 25)
- **error** L31 `scaffolding` scaffolding: “asides have to be honest”
- **error** L75 `scaffolding` scaffolding: “Soft landing to II-4:”
- **error** L77 `markers` Note [15] uses retired marker ★
- **error** L77 `markers` Note [15] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L17 `ramusio` Ramusio-only passage without an inline flag
- **error** L17 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **error** L19 `ramusio` Ramusio-only passage without an inline flag
- **error** L19 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **error** L21 `ramusio` Ramusio-only passage without an inline flag
- **error** L21 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [5]
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [10]
- **warning** — `ramusio` first draft carried 6 Ramusio passages; 1 paragraphs flag Ramusio (check: Further, you are not to suppos; is set a large and very beauti; of the capacity of a firkin…)
- **warning** L11 `name_policy` “Taidu” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)

### vol-2/ch-04-hunt-traffic.md

- **error** — `verbatim` verbatim Yule 72% (> 15%); worst: L13 86%, L15 76%, L21 90%, L23 92%, L27 96%
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
- **error** L41 `archaism` archaism outside quotes: “to wit”
- **error** L47 `archaism` archaism outside quotes: “hath”
- **error** L47 `archaism` archaism outside quotes: “whilst”
- **error** L49 `archaism` archaism outside quotes: “’tis”
- **error** L51 `archaism` archaism outside quotes: “hath”
- **error** L47 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L25, L31
- **error** L17 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L25 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L11 `recaps` opening recap
- **error** L55 `recaps` closing recap (93 words)
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L49 `openers` consecutive paragraphs open with “you must”
- **warning** — `sentence` average sentence 28.8 words (> 25)
- **error** L17 `scaffolding` scaffolding: “. Narrate”
- **error** L17 `scaffolding` scaffolding: “aside has to be honest”
- **error** L101 `scaffolding` scaffolding: “Soft landing to II-5:”
- **error** L73 `markers` Note [7] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L79 `markers` Note [10] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L87 `markers` Note [14] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L101 `markers` Note [21] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L15 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [2]
- **error** L23 `ramusio` Ramusio-only passage without an inline flag
- **error** L23 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [6]
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [11]
- **error** L47 `ramusio` Ramusio-only passage without an inline flag
- **error** L47 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [17]
- **warning** — `ramusio` first draft carried 5 Ramusio passages; 1 paragraphs flag Ramusio (check: They are obliged to approach t; The Two Brothers I have mentio; for he always travels in this …)
- **warning** L31 `name_policy` “Peking” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)

### vol-2/ch-05-ahmad-paper-coal.md

- **error** — `verbatim` verbatim Yule 31% (> 15%); worst: L13 72%, L45 71%
- **error** L19 `archaism` archaism outside quotes: “whilst”
- **error** L27 `archaism` archaism outside quotes: “hath”
- **error** L33 `archaism` archaism outside quotes: “hath”
- **error** L33 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “thereof”
- **error** L43 `archaism` archaism outside quotes: “hath”
- **error** L45 `archaism` archaism outside quotes: “whilst”
- **error** L57 `archaism` archaism outside quotes: “hath”
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L31, L47
- **error** L17 `asides` aside ends in an exit formula
- **error** L31 `asides` aside ends in an exit formula
- **error** L47 `asides` aside ends in an exit formula
- **error** L11 `recaps` opening recap
- **error** L59 `recaps` closing recap (88 words)
- **error** — `length` narrative 3211 words (outside 1800–3200)
- **error** L69 `markers` Note [3] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L99 `markers` Note [18] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L111 `markers` Note [24] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L41 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [15]
- **error** L45 `ramusio` Ramusio-only passage without an inline flag
- **error** L45 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [17]
- **error** L51 `ramusio` Ramusio-only passage without an inline flag
- **error** L51 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [20]
- **warning** L19 `names` “Zhenjin” is close to gazetteer name “Zhenjiang” (variant spelling?)
- **warning** L19 `name_policy` first mention of “Chandu” has no modern gloss (Shangdu (Duolun County))

### vol-2/ch-06-pulisanghin-sindafu.md

- **error** — `verbatim` verbatim Yule 64% (> 15%); worst: L21 82%, L23 74%, L27 75%, L29 76%, L31 88%
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L31 `archaism` archaism outside quotes: “hath”
- **error** L31 `archaism` archaism outside quotes: “thereof”
- **error** L35 `archaism` archaism outside quotes: “wherein”
- **error** L35 `archaism` archaism outside quotes: “sundry”
- **error** L35 `archaism` archaism outside quotes: “thereof”
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L25, L33
- **error** L11 `budgets` formula hinges ×8 (> 3)
- **error** L17 `asides` aside 200 words (> 80)
- **error** L33 `asides` aside 97 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **error** L47 `recaps` closing recap (92 words)
- **warning** — `sentence` average sentence 25.2 words (> 25)
- **error** L57 `scaffolding` scaffolding: “likely_visited”
- **error** L75 `scaffolding` scaffolding: “Gazetteer: *uncertain*”
- **error** L79 `scaffolding` scaffolding: “Gazetteer: Sindafu *visited*”
- **error** L79 `markers` Note [14] uses retired marker ★
- **error** L17 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **error** L27 `ramusio` Ramusio-only passage without an inline flag
- **error** L27 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [8]
- **error** L37 `ramusio` Ramusio-only passage without an inline flag
- **error** L37 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [12]
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 2 paragraphs flag Ramusio (check: But at the end of five days’ j; This Golden King was a great a; On the lands adjoining this ri…)
- **warning** L13 `name_policy` “Lugou Bridge” used bare; the book form is “Pulisanghin” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Qara Mören” used bare; the book form is “Caramoran” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Hwang Ho” used bare; the book form is “Caramoran” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Chengdu” used bare; the book form is “Sindafu” (gloss it beside the book form, once)
- **warning** L33 `name_policy` first mention of “Cuncun” has no modern gloss (Qinling–Hanzhong mountains)
- **warning** L37 `name_policy` first mention of “Acbalec Manzi” has no modern gloss (Hanzhong area)
- **warning** L45 `name_policy` first mention of “Tebet” has no modern gloss (Eastern Tibet / Kham region)
- **warning** L47 `name_policy` first mention of “Caindu” has no modern gloss (Xichang (Jianchang valley))
- **warning** L47 `name_policy` first mention of “Carajan” has no modern gloss (Yunnan (Dali / Kunming region))

### vol-2/ch-07-tebet-carajan.md

- **error** — `verbatim` verbatim Yule 46% (> 15%); worst: L13 78%, L25 70%, L47 75%
- **error** L21 `archaism` archaism outside quotes: “sundry”
- **error** L23 `archaism` archaism outside quotes: “wherein”
- **error** L27 `archaism` archaism outside quotes: “whilst”
- **error** L29 `archaism` archaism outside quotes: “sundry”
- **error** L33 `archaism` archaism outside quotes: “sundry”
- **error** L33 `archaism` archaism outside quotes: “sundry”
- **error** L47 `archaism` archaism outside quotes: “whilst”
- **error** L47 `archaism` archaism outside quotes: “’tis”
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L53 `recaps` closing recap (124 words)
- **warning** L41 `openers` consecutive paragraphs open with “in this”
- **error** L59 `scaffolding` scaffolding: “reported_only”
- **error** L75 `scaffolding` scaffolding: “likely_visited”
- **error** L75 `scaffolding` scaffolding: “Gazetteer: Carajan *visited*”
- **error** L83 `scaffolding` scaffolding: “Gazetteer: Zardandan *uncertain*”
- **error** L71 `markers` Note [7] uses retired marker ★
- **error** L23 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [5]
- **error** L27 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [7]
- **warning** L11 `name_policy` “Chengdu” used bare; the book form is “Sindafu” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Tibet” used bare; the book form is “Tebet” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L25 `name_policy` first mention of “Camul” has no modern gloss (Hami)
- **warning** L23 `name_policy` first mention of “Caindu” has no modern gloss (Xichang (Jianchang valley))
- **warning** L31 `name_policy` first mention of “Brius” has no modern gloss (Jinsha River crossing)
- **warning** L31 `name_policy` first mention of “Carajan” has no modern gloss (Yunnan (Dali / Kunming region))
- **warning** L45 `name_policy` first mention of “Zardandan” has no modern gloss (Western Yunnan (Baoshan–Tengchong))
- **warning** L53 `name_policy` first mention of “Mien” has no modern gloss (Bagan / Myanmar (Pagan kingdom))

### vol-2/ch-08-mien-bangala.md

- **error** — `verbatim` verbatim Yule 77% (> 15%); worst: L15 93%, L19 81%, L21 99%, L23 100%, L25 100%
- **error** L15 `archaism` archaism outside quotes: “insomuch”
- **error** L19 `archaism` archaism outside quotes: “Natheless”
- **error** L23 `archaism` archaism outside quotes: “whilst”
- **error** L23 `archaism` archaism outside quotes: “wist”
- **error** L27 `archaism` archaism outside quotes: “trowed”
- **error** L31 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “insomuch”
- **error** L43 `archaism` archaism outside quotes: “thereof”
- **error** L47 `archaism` archaism outside quotes: “insomuch”
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L47 `you_must_know` “You must know” outside quotes
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L45 `asides` aside ends in an exit formula
- **error** L51 `recaps` closing recap (125 words)
- **warning** L17 `recaps` “So/Thus …” restatement paragraph?
- **warning** L29 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 28.9 words (> 25)
- **error** L57 `scaffolding` scaffolding: “reported_only”
- **error** L7 `tags` tag line **[R/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **error** L41 `ramusio` Ramusio-only passage without an inline flag
- **error** L41 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [9]
- **warning** — `ramusio` first draft carried 1 Ramusio passages; 0 paragraphs flag Ramusio (check: The tomb likewise was plated p…)
- **warning** L13 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Bengal” used bare; the book form is “Bangala” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Pegu” used bare; the book form is “Bangala” (gloss it beside the book form, once)
- **warning** L13 `name_policy` first mention of “Carajan” has no modern gloss (Yunnan (Dali / Kunming region))
- **warning** L11 `name_policy` first mention of “Vochan” has no modern gloss (Baoshan (Yongchang))
- **warning** L17 `name_policy` first mention of “Zardandan” has no modern gloss (Western Yunnan (Baoshan–Tengchong))
- **warning** L13 `name_policy` first mention of “Mien” has no modern gloss (Bagan / Myanmar (Pagan kingdom))
- **warning** L51 `name_policy` first mention of “Caugigu” has no modern gloss (Kiang Hung (Jinghong))
- **warning** L51 `name_policy` first mention of “Anin” has no modern gloss (Jianshui (Lin-ngan))
- **warning** L51 `name_policy` first mention of “Coloman” has no modern gloss (Guizhou / Guangxi border region)
- **warning** L51 `name_policy` first mention of “Cuiju” has no modern gloss (Guiyang area)

### vol-2/ch-09-caugigu-cuiju.md

- **error** — `verbatim` verbatim Yule 55% (> 15%); worst: L13 95%, L17 98%, L23 94%, L27 87%, L33 100%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “sundry”
- **error** L27 `archaism` archaism outside quotes: “to wit”
- **error** L37 `archaism` archaism outside quotes: “’tis”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L11 `budgets` formula hinges ×5 (> 3)
- **error** L41 `asides` aside 130 words (> 80)
- **error** L41 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 67% of 5-grams match): “from sindafu you set out again and travel some sev”
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 27.6 words (> 25)
- **error** L55 `scaffolding` scaffolding: “Gazetteer: Caugigu, Anin, Coloman, Cuiju”
- **error** L55 `markers` Note [1] uses retired marker ★
- **warning** L11 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L11 `name_policy` “Guizhou” used bare; the book form is “Cuiju” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Burma” used bare; the book form is “Mien” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Kiang Hung” used bare; the book form is “Caugigu” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Tonkin” used bare; the book form is “Caugigu” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “Jiaozhi” used bare; the book form is “Caugigu” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Lin-ngan” used bare; the book form is “Anin” (gloss it beside the book form, once)
- **warning** L29 `name_policy` “Yunnan” used bare; the book form is “Carajan” (gloss it beside the book form, once)
- **warning** L29 `name_policy` “Toloman” used bare; the book form is “Coloman” (gloss it beside the book form, once)
- **warning** L29 `name_policy` “Guizhou” used bare; the book form is “Cuiju” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Chengdu” used bare; the book form is “Sindafu” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Phungan-lu” used bare; the book form is “Fungul” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Siu-chau” used bare; the book form is “Fungul” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Guizhou” used bare; the book form is “Cuiju” (gloss it beside the book form, once)
- **warning** L49 `name_policy` first mention of “Cambaluc” has no modern gloss (Beijing)
- **warning** L49 `name_policy` first mention of “Taianfu” has no modern gloss (Taiyuan)
- **warning** L49 `name_policy` first mention of “Kenjanfu” has no modern gloss (Xi'an)
- **warning** L49 `name_policy` first mention of “Cuncun” has no modern gloss (Qinling–Hanzhong mountains)
- **warning** L49 `name_policy` first mention of “Tebet” has no modern gloss (Eastern Tibet / Kham region)
- **warning** L29 `name_policy` first mention of “Caindu” has no modern gloss (Xichang (Jianchang valley))
- **warning** L29 `name_policy` first mention of “Carajan” has no modern gloss (Yunnan (Dali / Kunming region))
- **warning** L49 `name_policy` first mention of “Zardandan” has no modern gloss (Western Yunnan (Baoshan–Tengchong))
- **warning** L15 `name_policy` first mention of “Mien” has no modern gloss (Bagan / Myanmar (Pagan kingdom))
- **warning** L11 `name_policy` first mention of “Caugigu” has no modern gloss (Kiang Hung (Jinghong))
- **warning** L17 `name_policy` first mention of “Anin” has no modern gloss (Jianshui (Lin-ngan))
- **warning** L31 `name_policy` first mention of “Cuiju” has no modern gloss (Guiyang area)
- **warning** L31 `name_policy` first mention of “Fungul” has no modern gloss (Yibin (Suifu))
- **warning** L47 `name_policy` first mention of “Cacanfu” has no modern gloss (Hejian)

### vol-2/ch-10-manzi-sung.md

- **error** — `verbatim` verbatim Yule 69% (> 15%); worst: L13 77%, L15 90%, L19 77%, L21 79%, L25 87%
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
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 96% of 5-grams match): “so when you pass this river you enter the great pr”
- **error** L73 `recaps` closing recap (121 words)
- **warning** L29 `recaps` “So/Thus …” restatement paragraph?
- **warning** L39 `recaps` “So/Thus …” restatement paragraph?
- **warning** L47 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 25.4 words (> 25)
- **error** L79 `scaffolding` scaffolding: “likely_visited”
- **error** L93 `scaffolding` scaffolding: “soft ID”
- **error** L89 `markers` Note [6] uses retired marker ★
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [2]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 1 paragraphs flag Ramusio (check: There are also certain Christi; A great river passes through i…)
- **warning** L13 `name_policy` “Hejian” used bare; the book form is “Cacanfu” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Jinan” used bare; the book form is “Chinangli” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Yen-chau” used bare; the book form is “Tadinfu” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Jinan” used bare; the book form is “Chinangli” (gloss it beside the book form, once)
- **warning** L55 `name_policy` “Xiangyang” used bare; the book form is “Saianfu” (gloss it beside the book form, once)
- **warning** L55 `name_policy` “Hangzhou” used bare; the book form is “Kinsay” (gloss it beside the book form, once)
- **warning** L61 `name_policy` “Hwai-ngan” used bare; the book form is “Coiganju” (gloss it beside the book form, once)
- **warning** L61 `name_policy` “Yangzhou” used bare; the book form is “Yanju” (gloss it beside the book form, once)
- **warning** L43 `name_policy` first mention of “Caramoran” has no modern gloss (Yellow River at Puzhou crossing)
- **warning** L11 `name_policy` first mention of “Cacanfu” has no modern gloss (Hejian)
- **warning** L17 `name_policy` first mention of “Chinangli” has no modern gloss (Jinan)
- **warning** L19 `name_policy` first mention of “Tadinfu” has no modern gloss (Yanzhou)
- **warning** L37 `name_policy` first mention of “Linju” has no modern gloss (Linqing)
- **warning** L45 `name_policy` first mention of “Coiganju” has no modern gloss (Huai'an)
- **warning** L45 `name_policy` first mention of “Caiju” has no modern gloss (Guazhou)

### vol-2/ch-11-yanju-saianfu.md

- **error** — `verbatim` verbatim Yule 58% (> 15%); worst: L15 92%, L17 98%, L21 94%, L25 99%, L29 88%
- **error** L17 `archaism` archaism outside quotes: “insomuch”
- **error** L47 `archaism` archaism outside quotes: “wist”
- **error** L21 `you_must_know` “You must know” outside quotes
- **error** L37 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L27 `budgets` “Anyway” ×3 (> 1) at L27, L39, L45
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L27 `asides` aside 229 words (> 80)
- **error** L39 `asides` aside 100 words (> 80)
- **error** L39 `asides` aside ends in an exit formula
- **error** L45 `asides` aside 248 words (> 80)
- **error** L45 `asides` aside ends in an exit formula
- **error** L53 `recaps` closing recap (103 words)
- **warning** L13 `recaps` “So/Thus …” restatement paragraph?
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L23 `recaps` “So/Thus …” restatement paragraph?
- **warning** L31 `recaps` “So/Thus …” restatement paragraph?
- **warning** L49 `recaps` “So/Thus …” restatement paragraph?
- **warning** L51 `recaps` “So/Thus …” restatement paragraph?
- **warning** L17 `openers` consecutive paragraphs open with “when you”
- **error** L31 `scaffolding` scaffolding: “project gazetteer”
- **error** L31 `scaffolding` scaffolding: “soft ID”
- **error** L67 `markers` Note [5] uses retired marker ★
- **warning** L19 `name_policy` “Kao-yu” used bare; the book form is “Cayu” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Tung-chau” used bare; the book form is “Tinju” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “I-chin” used bare; the book form is “Tinju” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Yangzhou” used bare; the book form is “Yanju” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Yangzhou” used bare; the book form is “Yanju” (gloss it beside the book form, once)
- **warning** L31 `name_policy` “Ngan-king” used bare; the book form is “Nanghin” (gloss it beside the book form, once)
- **warning** L31 `name_policy` “Nanjing” used bare; the book form is “Nanghin” (gloss it beside the book form, once)
- **warning** L45 `name_policy` “Dadu” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L21 `name_policy` first mention of “Tinju” has no modern gloss (Nantong (Tung-chau))
- **warning** L27 `name_policy` first mention of “Nanghin” has no modern gloss (Anqing (Ngan-king))

### vol-2/ch-12-kian-suju.md

- **error** — `verbatim` verbatim Yule 63% (> 15%); worst: L13 97%, L17 92%, L19 97%, L23 90%, L29 95%
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
- **error** L41 `asides` aside 96 words (> 80)
- **error** L41 `asides` aside ends in an exit formula
- **error** L53 `asides` aside 140 words (> 80)
- **error** L53 `asides` aside ends in an exit formula
- **error** L63 `asides` aside 150 words (> 80)
- **error** L63 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L27 `recaps` “So/Thus …” restatement paragraph?
- **warning** L35 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 25.2 words (> 25)
- **error** L19 `ramusio` Ramusio-only passage without an inline flag
- **error** L19 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [2]
- **error** L25 `ramusio` Ramusio-only passage without an inline flag
- **error** L25 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [3]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 1 paragraphs flag Ramusio (check: Indeed as it has a course of s; There are at many places on th…)
- **warning** L15 `name_policy` “Yangzhou” used bare; the book form is “Yanju” (gloss it beside the book form, once)
- **warning** L15 `name_policy` “I-ching” used bare; the book form is “Sinju” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Kwa-chau” used bare; the book form is “Caiju” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Samarcand” used bare; the book form is “Samarcan” (gloss it beside the book form, once)
- **warning** L53 `name_policy` “Chang-chau” used bare; the book form is “Chinginju” (gloss it beside the book form, once)
- **warning** L63 `name_policy` “Hangzhou” used bare; the book form is “Kinsay” (gloss it beside the book form, once)
- **warning** L67 `name_policy` “Hu-chau” used bare; the book form is “Vuju” (gloss it beside the book form, once)
- **warning** L67 `name_policy` “Kiahing” used bare; the book form is “Changan” (gloss it beside the book form, once)
- **warning** L15 `name_policy` first mention of “Sindafu” has no modern gloss (Chengdu)
- **warning** L27 `name_policy` first mention of “Tebet” has no modern gloss (Eastern Tibet / Kham region)
- **warning** L27 `name_policy` first mention of “Caindu” has no modern gloss (Xichang (Jianchang valley))
- **warning** L11 `name_policy` first mention of “Nanghin” has no modern gloss (Anqing (Ngan-king))
- **warning** L11 `name_policy` first mention of “Saianfu” has no modern gloss (Xiangyang)
- **warning** L23 `name_policy` first mention of “Caiju” has no modern gloss (Guazhou)
- **warning** L33 `name_policy` first mention of “Chinghianfu” has no modern gloss (Zhenjiang)
- **warning** L41 `name_policy` first mention of “Chinginju” has no modern gloss (Changzhou)
- **warning** L51 `name_policy` first mention of “Suju” has no modern gloss (Suzhou)
- **warning** L65 `name_policy` first mention of “Vuju” has no modern gloss (Huzhou)
- **warning** L65 `name_policy` first mention of “Vughin” has no modern gloss (Wujiang)
- **warning** L65 `name_policy` first mention of “Changan” has no modern gloss (Jiaxing)
- **warning** L61 `name_policy` first mention of “Kinsay” has no modern gloss (Hangzhou)
- **warning** L65 `name_policy` first mention of “Vuju” has no modern gloss (Jinhua (Wuzhou))

### vol-2/ch-13-kinsay.md

- **error** — `verbatim` verbatim Yule 44% (> 15%); worst: L13 86%, L15 100%, L17 89%, L21 75%, L25 91%
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
- **error** — `length` narrative 3375 words (outside 1800–3200)
- **warning** — `sentence` average sentence 26.2 words (> 25)
- **error** L59 `scaffolding` scaffolding: “dispute hook”
- **error** L93 `scaffolding` scaffolding: “gazetteer *visited*”
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L21 `ramusio` Ramusio-only passage without an inline flag
- **error** L25 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **warning** L19 `name_policy` “Hangzhou” used bare; the book form is “Kinsay” (gloss it beside the book form, once)
- **warning** L11 `name_policy` first mention of “Suju” has no modern gloss (Suzhou)
- **warning** L87 `name_policy` first mention of “Fuju” has no modern gloss (Fuzhou)
- **warning** L73 `name_policy` first mention of “Zayton” has no modern gloss (Quanzhou)

### vol-2/ch-14-fuju-zayton.md

- **error** — `verbatim` verbatim Yule 72% (> 15%); worst: L11 80%, L13 75%, L15 71%, L17 98%, L21 95%
- **error** L57 `first_person` Book first person outside quotes: “Let me tell you”
- **error** L65 `first_person` Book first person outside quotes: “We could tell you”
- **error** L21 `archaism` archaism outside quotes: “insomuch”
- **error** L29 `archaism` archaism outside quotes: “hath”
- **error** L41 `archaism` archaism outside quotes: “’tis”
- **error** L53 `archaism` archaism outside quotes: “hath”
- **error** L57 `archaism` archaism outside quotes: “insomuch”
- **error** L65 `archaism` archaism outside quotes: “to wit”
- **error** L23 `you_must_know` “You must know” outside quotes
- **error** L29 `you_must_know` “You must know” outside quotes
- **error** L31 `you_must_know` “You must know” outside quotes
- **error** L49 `you_must_know` “You must know” outside quotes
- **error** L53 `you_must_know` “You must know” outside quotes
- **error** L61 `you_must_know` “You must know” outside quotes
- **error** L27 `budgets` “Anyway” ×3 (> 1) at L27, L51, L59
- **error** L11 `budgets` formula hinges ×6 (> 3)
- **error** L27 `asides` aside ends in an exit formula
- **error** L51 `asides` aside ends in an exit formula
- **error** L59 `asides` aside ends in an exit formula
- **error** L71 `recaps` closing recap (88 words)
- **warning** L19 `recaps` “So/Thus …” restatement paragraph?
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **warning** L45 `recaps` “So/Thus …” restatement paragraph?
- **warning** L17 `openers` consecutive paragraphs open with “when you”
- **warning** — `sentence` average sentence 25.6 words (> 25)
- **error** L15 `scaffolding` scaffolding: “honesty restores”
- **error** L85 `scaffolding` scaffolding: “gazetteer *visited*”
- **error** L7 `tags` tag line **[V/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **error** L31 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L53 `ramusio` Ramusio-only passage without an inline flag
- **error** L55 `ramusio` Ramusio-only passage without an inline flag
- **error** L61 `ramusio` Ramusio-only passage without an inline flag
- **warning** — `ramusio` first draft carried 6 Ramusio passages; 1 paragraphs flag Ramusio (check: which they weave into various ; They also make much cotton clo; And before this city came unde…)
- **warning** L19 `name_policy` “Hangzhou” used bare; the book form is “Kinsay” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Fu-yang” used bare; the book form is “Tanpiju” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Kin-hwa” used bare; the book form is “Vuju” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Chang-chau” used bare; the book form is “Chinginju” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Quanzhou” used bare; the book form is “Zayton” (gloss it beside the book form, once)
- **warning** L65 `name_policy` first mention of “Yanju” has no modern gloss (Yangzhou)
- **warning** L13 `name_policy` first mention of “Vuju” has no modern gloss (Huzhou)
- **warning** L11 `name_policy` first mention of “Tanpiju” has no modern gloss (Shaoxing)
- **warning** L13 `name_policy` first mention of “Vuju” has no modern gloss (Jinhua (Wuzhou))
- **warning** L13 `name_policy` first mention of “Ghiuju” has no modern gloss (Quzhou)
- **warning** L27 `name_policy` first mention of “Kelinfu” has no modern gloss (Jian'ou (Kien-ning))
- **warning** L33 `name_policy` first mention of “Unken” has no modern gloss (Minhou (Hu-kwan))
- **warning** L17 `name_policy` first mention of “Fuju” has no modern gloss (Fuzhou)
- **warning** L41 `name_policy` first mention of “Zayton” has no modern gloss (Quanzhou)
- **warning** L57 `name_policy` first mention of “Tyunju” has no modern gloss (Dehua)

### vol-2/ch-15-great-turkey-ponent.md

- **error** — `verbatim` verbatim Yule 52% (> 15%); worst: L13 82%, L21 96%, L23 83%, L37 89%, L41 93%
- **error** L13 `archaism` archaism outside quotes: “hath”
- **error** L13 `archaism` archaism outside quotes: “natheless”
- **error** L23 `archaism` archaism outside quotes: “gat”
- **error** L33 `you_must_know` “You must know” outside quotes
- **error** L39 `you_must_know` “You must know” outside quotes
- **error** L15 `budgets` “Anyway” ×3 (> 1) at L15, L19, L47
- **error** L15 `asides` aside ends in an exit formula
- **error** L19 `asides` aside ends in an exit formula
- **error** L47 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 96% of 5-grams match): “he is never at peace with his uncle the great kaan”
- **warning** L25 `recaps` “So/Thus …” restatement paragraph?
- **warning** L35 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 26.9 words (> 25)
- **warning** L13 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)
- **warning** L17 `name_policy` “Samarcand” used bare; the book form is “Samarcan” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Dry Tree” used bare; the book form is “Arbre Sec” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Russia” used bare; the book form is “Rosia” (gloss it beside the book form, once)
- **warning** L35 `name_policy` first mention of “Cambaluc” has no modern gloss (Beijing)
- **warning** L51 `name_policy` first mention of “Chipangu” has no modern gloss (Japan)

### vol-2/front-01-yuan-china-context.md

- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 50% of 5-grams match): “now i have told you of the splendour of cublay”
- **error** L60 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L76 `markers` Note [9] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-2/front-02-maps-cathay-manzi.md

- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 88% of 5-grams match): “and so i will tell you of the great province of ma”
- **error** L9 `scaffolding` scaffolding: “placeholder”
- **error** L48 `scaffolding` scaffolding: “Soft ID”
- **error** L79 `scaffolding` scaffolding: “/workspace”
- **error** L79 `scaffolding` scaffolding: “placeholder”
- **error** L81 `scaffolding` scaffolding: “outline-volumes”
- **error** L79 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-3/back-01-trivia-and-afterlives.md

- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “because of this book many set forth”
- **error** L55 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L61 `markers` Note [4] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-3/ch-01-ships-chipangu.md

- **error** — `verbatim` verbatim Yule 49% (> 15%); worst: L23 78%, L29 89%, L41 72%, L43 88%
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
- **warning** — `sentence` average sentence 26.6 words (> 25)
- **error** L27 `scaffolding` scaffolding: “asides have to be honest”
- **error** L65 `markers` Note [7] uses retired marker ★
- **error** L65 `markers` Note [7] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L65 `markers` Note [7] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L73 `markers` Note [11] uses retired marker ★
- **error** L73 `markers` Note [11] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L13 `ramusio` Ramusio-only passage without an inline flag
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [2]
- **error** L23 `ramusio` Ramusio-only passage without an inline flag
- **error** L23 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [5]
- **error** L25 `ramusio` Ramusio-only passage without an inline flag
- **error** L25 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [6]
- **error** L33 `ramusio` Ramusio-only passage without an inline flag
- **error** L33 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [10]
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 2 paragraphs flag Ramusio (check: Moreover the larger of their v; and the King does not allow it; In this Island some of the dea…)
- **warning** L11 `name_policy` “Cheinan” used bare; the book form is “Gulf of Cheinan” (gloss it beside the book form, once)
- **warning** L39 `name_policy` “Japan” used bare; the book form is “Chipangu” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Cheinan” used bare; the book form is “Gulf of Cheinan” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Cheinan” used bare; the book form is “Gulf of Cheinan” (gloss it beside the book form, once)
- **warning** L43 `name_policy` first mention of “Anin” has no modern gloss (Jianshui (Lin-ngan))
- **warning** L43 `name_policy` first mention of “Coloman” has no modern gloss (Guizhou / Guangxi border region)
- **warning** L11 `name_policy` first mention of “Gulf of Cheinan” has no modern gloss (Gulf of Tonkin)
- **warning** L47 `name_policy` first mention of “Chamba” has no modern gloss (Central Vietnam (Champa coast))

### vol-3/ch-02-chamba-java.md

- **error** — `verbatim` verbatim Yule 47% (> 15%); worst: L13 84%, L15 74%, L19 76%, L25 92%, L29 97%
- **error** L13 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×3 (> 1) at L17, L27, L33
- **error** L15 `budgets` formula hinges ×4 (> 3)
- **error** L17 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 108 words (> 80)
- **error** L27 `asides` aside ends in an exit formula
- **error** L33 `asides` aside 93 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 92% of 5-grams match): “when you leave the port of zayton you sail west so”
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?
- **warning** L37 `recaps` “So/Thus …” restatement paragraph?
- **error** — `length` narrative 1779 words (outside 1800–3200)
- **warning** — `sentence` average sentence 26.0 words (> 25)
- **error** L23 `scaffolding` scaffolding: “Soft digression now:”
- **error** L39 `scaffolding` scaffolding: “Soft close here:”
- **error** L45 `scaffolding` scaffolding: “reported_only”
- **error** L45 `scaffolding` scaffolding: “likely_visited”
- **error** L45 `scaffolding` scaffolding: “Gazetteer: Chamba *visited*”
- **error** L51 `markers` Note [4] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L55 `markers` Note [6] uses retired marker ★
- **error** L55 `markers` Note [6] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L55 `markers` Note [6] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L65 `markers` Note [11] uses retired marker ★
- **error** L65 `markers` Note [11] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L65 `markers` Note [11] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L69 `markers` Note [13] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L7 `tags` tag line **[R/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **error** L29 `ramusio` Ramusio-only passage without an inline flag
- **error** L29 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [9]
- **warning** — `ramusio` first draft carried 1 Ramusio passages; 0 paragraphs flag Ramusio (check: it is on the mainland…)
- **warning** L37 `name_policy` “Bintan” used bare; the book form is “Pentam” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L39 `name_policy` “Champa” used bare; the book form is “Chamba” (gloss it beside the book form, once)
- **warning** L11 `name_policy` first mention of “Condur” has no modern gloss (Pulo Condore (Côn Đảo))
- **warning** L11 `name_policy` first mention of “Locac” has no modern gloss (Malay Peninsula (southern Thailand/Malaysia))
- **warning** L11 `name_policy` first mention of “Pentam” has no modern gloss (Bintan / Riau Islands)
- **warning** L11 `name_policy` first mention of “Malaiur” has no modern gloss (Melaka / Sumatra Malay coast)

### vol-3/ch-03-java-less-sumatra.md

- **error** — `verbatim` verbatim Yule 64% (> 15%); worst: L17 93%, L21 98%, L23 100%, L29 100%, L31 84%
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
- **warning** — `sentence` average sentence 25.5 words (> 25)
- **error** L13 `scaffolding` scaffolding: “Soft premise here:”
- **error** L51 `scaffolding` scaffolding: “Soft close here:”
- **error** L63 `scaffolding` scaffolding: “likely_visited”
- **error** L73 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L79 `scaffolding` scaffolding: “Soft ID”
- **error** L85 `scaffolding` scaffolding: “likely_visited”
- **error** L89 `scaffolding` scaffolding: “reported_only”
- **error** L63 `markers` Note [4] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L69 `markers` Note [7] uses retired marker ★
- **error** L69 `markers` Note [7] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L69 `markers` Note [7] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L77 `markers` Note [11] uses retired marker ★
- **error** L77 `markers` Note [11] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L83 `markers` Note [14] uses retired marker ★
- **error** L83 `markers` Note [14] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L83 `markers` Note [14] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L87 `markers` Note [16] uses retired marker ★
- **error** L87 `markers` Note [16] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L89 `markers` Note [17] uses retired marker ★
- **error** L7 `tags` tag line **[V/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **error** L23 `ramusio` Ramusio-only passage without an inline flag
- **error** L23 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [6]
- **error** L31 `ramusio` Ramusio-only passage without an inline flag
- **error** L31 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [10]
- **warning** — `ramusio` first draft carried 5 Ramusio passages; 0 paragraphs flag Ramusio (check: and when savage with any one t; he landed with about 2000 men ; for there is great store of wo…)
- **warning** L21 `names` “Islanders” is close to gazetteer name “Islands” (variant spelling?)
- **warning** L11 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L13 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Perlak” used bare; the book form is “Ferlec” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Samudra” used bare; the book form is “Samara” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Pasai” used bare; the book form is “Basma” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Samudra” used bare; the book form is “Samara” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Nicobar” used bare; the book form is “Necuveran” (gloss it beside the book form, once)
- **warning** L49 `name_policy` “Andaman” used bare; the book form is “Angamanain” (gloss it beside the book form, once)
- **warning** L13 `name_policy` first mention of “Chipangu” has no modern gloss (Japan)
- **warning** L11 `name_policy` first mention of “Pentam” has no modern gloss (Bintan / Riau Islands)
- **warning** L11 `name_policy` first mention of “Malaiur” has no modern gloss (Melaka / Sumatra Malay coast)
- **warning** L13 `name_policy` first mention of “Ferlec” has no modern gloss (Perlak)
- **warning** L21 `name_policy` first mention of “Basma” has no modern gloss (Pasai / NE Sumatra coast)
- **warning** L29 `name_policy` first mention of “Samara” has no modern gloss (Samudera Pasai)
- **warning** L35 `name_policy` first mention of “Dagroian” has no modern gloss (NE Sumatra coastal polity)
- **warning** L33 `name_policy` first mention of “Lambri” has no modern gloss (Lamuri (Aceh headland))
- **warning** L39 `name_policy` first mention of “Fansur” has no modern gloss (Barus)

### vol-3/ch-04-necuveran-seilan.md

- **error** — `verbatim` verbatim Yule 77% (> 15%); worst: L13 89%, L17 95%, L21 94%, L25 97%, L27 95%
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
- **error** L19 `asides` aside 82 words (> 80)
- **error** L19 `asides` aside ends in an exit formula
- **error** L23 `asides` aside ends in an exit formula
- **error** L37 `asides` aside 107 words (> 80)
- **error** L37 `asides` aside ends in an exit formula
- **warning** L15 `recaps` “So/Thus …” restatement paragraph?
- **warning** L33 `recaps` “So/Thus …” restatement paragraph?
- **warning** — `sentence` average sentence 26.5 words (> 25)
- **error** L15 `scaffolding` scaffolding: “Soft turn now:”
- **error** L37 `scaffolding` scaffolding: “asides have to be honest”
- **error** L45 `scaffolding` scaffolding: “Soft close here:”
- **error** L51 `scaffolding` scaffolding: “likely_visited”
- **error** L51 `scaffolding` scaffolding: “reported_only”
- **error** L59 `markers` Note [5] uses retired marker ★
- **error** L59 `markers` Note [5] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L59 `markers` Note [5] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L63 `markers` Note [7] uses retired marker ★
- **error** L63 `markers` Note [7] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L63 `markers` Note [7] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L73 `markers` Note [12] uses retired marker ★
- **error** L77 `markers` Note [14] uses retired marker ★
- **error** L77 `markers` Note [14] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L77 `markers` Note [14] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L7 `tags` tag line **[R/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **warning** L15 `name_policy` “Lamuri” used bare; the book form is “Lambri” (gloss it beside the book form, once)
- **warning** L19 `name_policy` “Andaman” used bare; the book form is “Angamanain” (gloss it beside the book form, once)
- **warning** L23 `name_policy` “Ceylon” used bare; the book form is “Seilan” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Ceylon” used bare; the book form is “Seilan” (gloss it beside the book form, once)
- **warning** L11 `name_policy` first mention of “Java the Less” has no modern gloss (Sumatra)
- **warning** L11 `name_policy` first mention of “Necuveran” has no modern gloss (Nicobar Islands)
- **warning** L11 `name_policy` first mention of “Angamanain” has no modern gloss (Andaman Islands)
- **warning** L45 `name_policy` first mention of “Maabar” has no modern gloss (Coromandel Coast (Tamil Nadu))

### vol-3/ch-05-maabar-st-thomas.md

- **error** — `verbatim` verbatim Yule 39% (> 15%); worst: L4 100%, L11 85%, L15 82%, L27 73%
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
- **error** L17 `scaffolding` scaffolding: “Soft turn now:”
- **error** L43 `scaffolding` scaffolding: “Soft rise now:”
- **error** L51 `scaffolding` scaffolding: “Soft close here:”
- **error** L57 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L57 `markers` Note [1] uses retired marker ★
- **error** L63 `markers` Note [4] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L67 `markers` Note [6] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L69 `markers` Note [7] uses retired marker ★
- **error** L69 `markers` Note [7] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L71 `markers` Note [8] uses retired marker ★
- **error** L75 `markers` Note [10] uses retired marker ★
- **error** L75 `markers` Note [10] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L75 `markers` Note [10] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L85 `markers` Note [15] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L89 `markers` Note [17] uses retired marker ★
- **error** L89 `markers` Note [17] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L7 `tags` tag line **[R/M]** is not one of **[V]** **[R]** **[M]** **[reception]**
- **error** L13 `ramusio` Ramusio-only passage without an inline flag
- **error** L13 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [2]
- **warning** L25 `names` “Dhufar” is close to gazetteer name “Dufar” (variant spelling?)
- **warning** L13 `name_policy` “Ceylon” used bare; the book form is “Seilan” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Hormes” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Dofar” used bare; the book form is “Dufar” (gloss it beside the book form, once)
- **warning** L45 `name_policy` “Coromandel” used bare; the book form is “Maabar” (gloss it beside the book form, once)
- **warning** L51 `name_policy` “Hormes” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L11 `name_policy` first mention of “Seilan” has no modern gloss (Sri Lanka)
- **warning** L11 `name_policy` first mention of “Maabar” has no modern gloss (Coromandel Coast (Tamil Nadu))
- **warning** L45 `name_policy` first mention of “Mailapur” has no modern gloss (Mylapore (Chennai))
- **warning** L51 `name_policy` first mention of “Mutfili” has no modern gloss (Motupalli)
- **warning** L51 `name_policy` first mention of “Cail” has no modern gloss (Kayalpatnam / Old Kayal)
- **warning** L51 `name_policy` first mention of “Kesmacoran” has no modern gloss (Makran coast (Gwadar/Pasni area))

### vol-3/ch-06-mutfili-kesmacoran.md

- **error** — `verbatim` verbatim Yule 64% (> 15%); worst: L4 97%, L11 76%, L13 88%, L15 77%, L19 97%
- **error** L13 `first_person` Book first person outside quotes: “I will tell”
- **error** L29 `archaism` archaism outside quotes: “hath”
- **error** L51 `archaism` archaism outside quotes: “whilst”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L41 `you_must_know` “You must know” outside quotes
- **error** L43 `you_must_know` “You must know” outside quotes
- **error** L59 `you_must_know` “You must know” outside quotes
- **error** L17 `budgets` “Anyway” ×2 (> 1) at L17, L57
- **error** L17 `asides` 5 asides (> 4)
- **error** L17 `asides` aside ends in an exit formula
- **error** L57 `asides` aside ends in an exit formula
- **error** — `length` narrative 3609 words (outside 1800–3200)
- **warning** — `sentence` average sentence 25.4 words (> 25)
- **error** L17 `scaffolding` scaffolding: “Soft aside:”
- **error** L27 `scaffolding` scaffolding: “Soft rise now:”
- **error** L39 `scaffolding` scaffolding: “Soft sail west:”
- **error** L49 `scaffolding` scaffolding: “Soft sail on:”
- **error** L61 `scaffolding` scaffolding: “Soft close here:”
- **error** L85 `scaffolding` scaffolding: “Gazetteer: *visited*”
- **error** L97 `scaffolding` scaffolding: “likely_visited”
- **error** L73 `markers` Note [4] uses retired marker ★
- **error** L73 `markers` Note [4] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L73 `markers` Note [4] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L81 `markers` Note [8] uses retired marker ★
- **error** L81 `markers` Note [8] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L83 `markers` Note [9] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L91 `markers` Note [13] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L95 `markers` Note [15] uses retired marker ★
- **error** L95 `markers` Note [15] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L95 `markers` Note [15] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L105 `markers` Note [20] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L113 `markers` Note [24] uses retired marker ★
- **error** L113 `markers` Note [24] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L113 `markers` Note [24] uses a retired “Dispute:” label (use ? and say what is contested)
- **error** L19 `ramusio` Ramusio-only passage without an inline flag
- **error** L19 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [5]
- **error** L23 `ramusio` Ramusio-only passage without an inline flag
- **error** L23 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [7]
- **error** L31 `ramusio` Ramusio-only passage without an inline flag
- **error** L31 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [11]
- **error** L59 `ramusio` Ramusio-only passage without an inline flag
- **error** L59 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [25]
- **warning** — `ramusio` first draft carried 4 Ramusio passages; 0 paragraphs flag Ramusio (check: If a foreign merchant who does; Also if they meet any one who ; All the people of this city, a…)
- **warning** L27 `names` “Banyan” is close to gazetteer name “Banan” (variant spelling?)
- **warning** L11 `name_policy` first mention of “Maabar” has no modern gloss (Coromandel Coast (Tamil Nadu))
- **warning** L39 `name_policy` first mention of “Eli” has no modern gloss (Mount Eli / Ezhimala)
- **warning** L49 `name_policy` first mention of “Tana” has no modern gloss (Thane)
- **warning** L49 `name_policy` first mention of “Cambaet” has no modern gloss (Khambhat (Cambay))
- **warning** L49 `name_policy` first mention of “Semenat” has no modern gloss (Somnath area)
- **warning** L49 `name_policy` first mention of “Kesmacoran” has no modern gloss (Makran coast (Gwadar/Pasni area))

### vol-3/ch-07-male-abash.md

- **error** — `verbatim` verbatim Yule 46% (> 15%); worst: L17 81%, L19 76%, L43 82%
- **error** L25 `archaism` archaism outside quotes: “whilst”
- **error** L27 `archaism` archaism outside quotes: “’Tis”
- **error** L29 `archaism` archaism outside quotes: “whilst”
- **error** L43 `archaism` archaism outside quotes: “wherein”
- **error** L19 `you_must_know` “You must know” outside quotes
- **error** L13 `budgets` “Anyway” ×3 (> 1) at L13, L25, L37
- **error** L9 `budgets` formula hinges ×9 (> 3)
- **error** L13 `asides` aside 91 words (> 80)
- **error** L13 `asides` aside ends in an exit formula
- **error** L25 `asides` aside 122 words (> 80)
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 95% of 5-grams match): “they call the bird ruc”
- **warning** L21 `recaps` “So/Thus …” restatement paragraph?
- **error** L25 `scaffolding` scaffolding: “aside has to be honest”
- **error** L71 `markers` Note [8] uses retired marker ★
- **error** L71 `markers` Note [8] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0
- **error** L15 `ramusio` Ramusio-only passage without an inline flag
- **error** L15 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [4]
- **error** L29 `ramusio` Ramusio-only passage without an inline flag
- **error** L29 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [11]
- **warning** — `ramusio` first draft carried 2 Ramusio passages; 0 paragraphs flag Ramusio (check: The ambergris comes from the s; They brought (as I heard) to t…)
- **warning** L13 `name_policy` “Maldives” used bare; the book form is “Male and Female” (gloss it beside the book form, once)
- **warning** L13 `name_policy` “Socotra” used bare; the book form is “Scotra” (gloss it beside the book form, once)
- **warning** L17 `name_policy` “Pagan” used bare; the book form is “Mien” (gloss it beside the book form, once)
- **warning** L21 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Coromandel” used bare; the book form is “Maabar” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Madagascar” used bare; the book form is “Madeigascar” (gloss it beside the book form, once)
- **warning** L29 `name_policy` “Madagascar” used bare; the book form is “Madeigascar” (gloss it beside the book form, once)
- **warning** L31 `name_policy` “Zanj” used bare; the book form is “Zanghibar” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Zanj” used bare; the book form is “Zanghibar” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Champa” used bare; the book form is “Chamba” (gloss it beside the book form, once)
- **warning** L47 `name_policy` “Abyssinia” used bare; the book form is “Abash” (gloss it beside the book form, once)
- **warning** L51 `name_policy` first mention of “Hormos” has no modern gloss (Old Hormuz (near Minab))
- **warning** L51 `name_policy` first mention of “Cambaluc” has no modern gloss (Beijing)
- **warning** L11 `name_policy` first mention of “Scotra” has no modern gloss (Socotra)
- **warning** L37 `name_policy` first mention of “Abash” has no modern gloss (Ethiopian highlands)
- **warning** L51 `name_policy` first mention of “Esher” has no modern gloss (Ash-Shihr)
- **warning** L51 `name_policy` first mention of “Dufar” has no modern gloss (Dhofar (Salalah area))

### vol-3/ch-08-aden-hormos.md

- **error** — `verbatim` verbatim Yule 64% (> 15%); worst: L11 95%, L15 83%, L21 82%, L23 87%, L25 83%
- **error** L47 `first_person` Book first person outside quotes: “we will quit”
- **error** L15 `archaism` archaism outside quotes: “insomuch”
- **error** L15 `archaism` archaism outside quotes: “’tis”
- **error** L23 `archaism` archaism outside quotes: “Whilst”
- **error** L25 `archaism` archaism outside quotes: “’tis”
- **error** L13 `budgets` “Anyway” ×3 (> 1) at L13, L19, L33
- **error** L9 `budgets` formula hinges ×8 (> 3)
- **error** L13 `asides` 6 asides (> 4)
- **error** L13 `asides` aside 81 words (> 80)
- **error** L13 `asides` aside ends in an exit formula
- **error** L19 `asides` aside ends in an exit formula
- **error** L27 `asides` aside 81 words (> 80)
- **error** L33 `asides` aside ends in an exit formula
- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 97% of 5-grams match): “houses built with ventilators to catch the wind”
- **error** L27 `scaffolding` scaffolding: “Soft rise now:”
- **error** L57 `scaffolding` scaffolding: “reported_only”
- **error** L75 `markers` Note [10] uses retired marker ★
- **error** L75 `markers` Note [10] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L97 `markers` Note [21] uses retired marker ★
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0
- **warning** L27 `name_policy` “Dhafār” used bare; the book form is “Dufar” (gloss it beside the book form, once)
- **warning** L33 `name_policy` “Dhafār” used bare; the book form is “Dufar” (gloss it beside the book form, once)
- **warning** L35 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Baghdad” used bare; the book form is “Baudas” (gloss it beside the book form, once)
- **warning** L27 `name_policy` first mention of “Dufar” has no modern gloss (Dhofar (Salalah area))
- **warning** L33 `name_policy` first mention of “Calatu” has no modern gloss (Qalhat)

### vol-3/ch-09-cocachin-return.md

- **error** — `verbatim` verbatim Yule 39% (> 15%); worst: L13 79%, L17 89%, L37 75%, L39 96%
- **error** L35 `first_person` Book first person outside quotes: “I should have told”
- **error** L41 `first_person` Book first person outside quotes: “What more shall I say”
- **error** L17 `archaism` archaism outside quotes: “sundry”
- **error** L39 `archaism` archaism outside quotes: “whilst”
- **warning** — `sentence` average sentence 36.8 words (> 25)
- **error** L19 `scaffolding` scaffolding: “Soft turn here:”
- **error** L29 `scaffolding` scaffolding: “Soft blow:”
- **error** L53 `markers` Note [3] uses retired marker ★
- **error** L71 `markers` Note [12] uses retired marker ★
- **error** L71 `markers` Note [12] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0
- **error** L19 `ramusio` Ramusio-only passage without an inline flag
- **error** L19 `ramusio` Ramusio-only passage: no “Ramusio-only.” label in Notes [6]
- **warning** L11 `name_policy` “Georgia” used bare; the book form is “Georgiania” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Bengal” used bare; the book form is “Bangala” (gloss it beside the book form, once)
- **warning** L25 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Hormuz” used bare; the book form is “Hormos” (gloss it beside the book form, once)
- **warning** L27 `name_policy` “Sri Lanka” used bare; the book form is “Seilan” (gloss it beside the book form, once)
- **warning** L37 `name_policy` “Khanbaliq” used bare; the book form is “Cambaluc” (gloss it beside the book form, once)
- **warning** L41 `name_policy` “Tabriz” used bare; the book form is “Tauris” (gloss it beside the book form, once)
- **warning** L43 `name_policy` “Sumatra” used bare; the book form is “Java the Less” (gloss it beside the book form, once)
- **warning** L25 `name_policy` first mention of “Java the Less” has no modern gloss (Sumatra)
- **warning** L27 `name_policy` first mention of “Seilan” has no modern gloss (Sri Lanka)
- **warning** L27 `name_policy` first mention of “Maabar” has no modern gloss (Coromandel Coast (Tamil Nadu))
- **warning** L27 `name_policy` first mention of “Mutfili” has no modern gloss (Motupalli)
- **warning** L27 `name_policy` first mention of “Kesmacoran” has no modern gloss (Makran coast (Gwadar/Pasni area))

### vol-3/ch-10-ca-polo-milione.md

- **error** — `verbatim` verbatim Yule 37% (> 15%); worst: L4 100%, L15 83%
- **error** L15 `archaism` archaism outside quotes: “whilst”
- **error** L17 `archaism` archaism outside quotes: “whilst”
- **error** L29 `archaism` archaism outside quotes: “whilst”
- **error** L33 `archaism` archaism outside quotes: “hath”
- **error** L13 `asides` aside ends in an exit formula
- **error** — `length` narrative 3321 words (outside 1800–3200)
- **warning** — `sentence` average sentence 33.4 words (> 25)
- **error** L9 `scaffolding` scaffolding: “Soft caution at the start:”
- **error** L19 `scaffolding` scaffolding: “Soft dispute already:”
- **error** L19 `scaffolding` scaffolding: “Soft sting:”
- **error** L21 `scaffolding` scaffolding: “Soft turn now:”
- **error** L21 `scaffolding` scaffolding: “Soft merchant breath:”
- **error** L23 `scaffolding` scaffolding: “Soft family colour:”
- **error** L23 `scaffolding` scaffolding: “Soft correction without killing the roma”
- **error** L25 `scaffolding` scaffolding: “Soft rise of the manuscript trail:”
- **error** L25 `scaffolding` scaffolding: “Soft pride of the note:”
- **error** L25 `scaffolding` scaffolding: “Soft fan of transmission:”
- **error** L27 `scaffolding` scaffolding: “Soft clerical spread:”
- **error** L27 `scaffolding` scaffolding: “Soft caution of Larner and of honest cou”
- **error** L29 `scaffolding` scaffolding: “Soft witness of science:”
- **error** L29 `scaffolding` scaffolding: “Soft join to Volume III’s southern ocean”
- **error** L31 `scaffolding` scaffolding: “Soft double life of the text:”
- **error** L33 `scaffolding` scaffolding: “Soft bequests of a Christian merchant:”
- **error** L33 `scaffolding` scaffolding: “Soft human particular:”
- **error** L33 `scaffolding` scaffolding: “Soft anathema of the close:”
- **error** L35 `scaffolding` scaffolding: “Soft burial:”
- **error** L35 `scaffolding` scaffolding: “Soft fade of the family:”
- **error** L37 `scaffolding` scaffolding: “Soft dispute of relics and images:”
- **error** L39 `scaffolding` scaffolding: “Soft last turn:”
- **error** L39 `scaffolding` scaffolding: “Soft double verdict of Venice and of Eur”
- **error** L47 `scaffolding` scaffolding: “Soft caution:”
- **error** L59 `scaffolding` scaffolding: “Soft merchant breath:”
- **error** L57 `markers` Note [6] uses retired marker ★
- **error** L63 `markers` Note [9] uses retired marker ★
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0

### vol-3/ch-11-afterlives.md

- **error** L16 `asides` aside 163 words (> 80)
- **error** L18 `asides` paragraph after an aside announces the return
- **error** L24 `asides` aside 222 words (> 80)
- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “he who made this work”
- **error** L7 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “and this island is so rich in gold that no man can”
- **warning** L32 `openers` consecutive paragraphs open with “then the”
- **warning** — `sentence` average sentence 36.2 words (> 25)
- **error** L12 `scaffolding` scaffolding: “Soft caution at the start:”
- **error** L14 `scaffolding` scaffolding: “Soft cartographic breath:”
- **error** L16 `scaffolding` scaffolding: “Soft dispute already:”
- **error** L16 `scaffolding` scaffolding: “Soft breath of proportion:”
- **error** L18 `scaffolding` scaffolding: “Soft Venetian return:”
- **error** L18 `scaffolding` scaffolding: “Soft wandering of names:”
- **error** L18 `scaffolding` scaffolding: “Soft caution of method:”
- **error** L20 `scaffolding` scaffolding: “Soft dispute restated:”
- **error** L20 `scaffolding` scaffolding: “Soft join:”
- **error** L22 `scaffolding` scaffolding: “Soft postil breath:”
- **error** L24 `scaffolding` scaffolding: “Soft selective amplification named:”
- **error** L24 `scaffolding` scaffolding: “Soft honest hinge:”
- **error** L24 `scaffolding` scaffolding: “Soft cross-echo to III-1:”
- **error** L26 `scaffolding` scaffolding: “Soft rise of the press:”
- **error** L26 `scaffolding` scaffolding: “Soft Ramusio elevation:”
- **error** L26 `scaffolding` scaffolding: “Soft double edge, already sworn in III-1”
- **error** L26 `scaffolding` scaffolding: “Soft print paradox:”
- **error** L28 `scaffolding` scaffolding: “Soft missionary rereading:”
- **error** L28 `scaffolding` scaffolding: “Soft Jesuit breath:”
- **error** L28 `scaffolding` scaffolding: “Soft caution:”
- **error** L28 `scaffolding` scaffolding: “Soft join to empire:”
- **error** L30 `scaffolding` scaffolding: “Soft long nineteenth century:”
- **error** L30 `scaffolding` scaffolding: “Soft dispute hook stated plainly:”
- **error** L30 `scaffolding` scaffolding: “Soft Pelliot and the French school:”
- **error** L30 `scaffolding` scaffolding: “Soft Benedetto and the stemmata:”
- **error** L30 `scaffolding` scaffolding: “dispute hook”
- **error** L32 `scaffolding` scaffolding: “Soft Wood breath:”
- **error** L32 `scaffolding` scaffolding: “Soft replies without theatre or scorn:”
- **error** L32 `scaffolding` scaffolding: “Soft pillars of reply:”
- **error** L32 `scaffolding` scaffolding: “Soft false binary named and refused:”
- **error** L32 `scaffolding` scaffolding: “Soft sting of method:”
- **error** L34 `scaffolding` scaffolding: “Soft close toward purpose:”
- **error** L34 `scaffolding` scaffolding: “Soft dignity without naïveté:”
- **error** L34 `scaffolding` scaffolding: “Soft last hinge:”
- **error** L34 `scaffolding` scaffolding: “Soft close here:”
- **error** L34 `scaffolding` scaffolding: “the outline”
- **error** L34 `scaffolding` scaffolding: “dispute hook”
- **error** L40 `scaffolding` scaffolding: “Soft caution:”
- **error** L40 `scaffolding` scaffolding: “Outline III-11”
- **error** L44 `scaffolding` scaffolding: “Dispute hook”
- **error** L48 `scaffolding` scaffolding: “Soft method:”
- **error** L54 `scaffolding` scaffolding: “Soft print paradox:”
- **error** L56 `scaffolding` scaffolding: “Soft conscription:”
- **error** L62 `scaffolding` scaffolding: “Soft series purpose:”
- **error** L64 `scaffolding` scaffolding: “outline III-11”
- **error** L46 `markers` Note [4] uses retired marker ★
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0

### vol-3/ch-12-reliability-essay.md

- **error** L7 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “he put in writing all that he saw and heard”
- **error** — `length` narrative 3753 words (outside 0–3500)
- **warning** — `sentence` average sentence 25.6 words (> 25)
- **error** L14 `scaffolding` scaffolding: “Soft caution at the start:”
- **error** L18 `scaffolding` scaffolding: “Soft opening of kinds:”
- **error** L20 `scaffolding` scaffolding: “Soft ledger breath:”
- **error** L20 `scaffolding` scaffolding: “Soft join:”
- **error** L22 `scaffolding` scaffolding: “Soft autobiographical spine:”
- **error** L22 `scaffolding` scaffolding: “Soft caution:”
- **error** L24 `scaffolding` scaffolding: “Soft double authorship named without sca”
- **error** L24 `scaffolding` scaffolding: “Soft hinge:”
- **error** L24 `scaffolding` scaffolding: “Soft name of the whole:”
- **error** L28 `scaffolding` scaffolding: “Soft method restated:”
- **error** L28 `scaffolding` scaffolding: “Soft tangle confessed:”
- **error** L30 `scaffolding` scaffolding: “Soft textual panel:”
- **error** L30 `scaffolding` scaffolding: “Soft Moule–Pelliot and Benedetto lesson:”
- **error** L30 `scaffolding` scaffolding: “Soft rule of this retelling:”
- **error** L30 `scaffolding` scaffolding: “Soft further caution:”
- **error** L30 `scaffolding` scaffolding: “Soft join to reliability:”
- **error** L36 `scaffolding` scaffolding: “Soft salt and revenue breath:”
- **error** L36 `scaffolding` scaffolding: “Soft Cocachin pillar:”
- **error** L36 `scaffolding` scaffolding: “Soft further hits in brief:”
- **error** L38 `scaffolding` scaffolding: “Soft Ocean hits beside bulkheads:”
- **error** L38 `scaffolding` scaffolding: “Soft point:”
- **error** L40 `scaffolding` scaffolding: “Soft synthesis of hits:”
- **error** L40 `scaffolding` scaffolding: “Soft honesty beside the hits:”
- **error** L44 `scaffolding` scaffolding: “Soft famous absences:”
- **error** L44 `scaffolding` scaffolding: “Soft script and name limits:”
- **error** L44 `scaffolding` scaffolding: “Soft further misses:”
- **error** L46 `scaffolding` scaffolding: “Soft character of miss versus silence:”
- **error** L46 `scaffolding` scaffolding: “Soft method:”
- **error** L48 `scaffolding` scaffolding: “Soft counter-weight:”
- **error** L48 `scaffolding` scaffolding: “Soft join:”
- **error** L54 `scaffolding` scaffolding: “Soft markers:”
- **error** L54 `scaffolding` scaffolding: “Soft Wood target and reply field:”
- **error** L56 `scaffolding` scaffolding: “Soft markers:”
- **error** L56 `scaffolding` scaffolding: “Soft reading:”
- **error** L58 `scaffolding` scaffolding: “Soft Vogel lesson:”
- **error** L60 `scaffolding` scaffolding: “Soft markers:”
- **error** L60 `scaffolding` scaffolding: “Soft reception sting already told in III”
- **error** L60 `scaffolding` scaffolding: “campaign outline”
- **error** L62 `scaffolding` scaffolding: “Soft series choice confessed:”
- **error** L66 `scaffolding` scaffolding: “Soft précis without caricature:”
- **error** L66 `scaffolding` scaffolding: “Soft targets:”
- **error** L68 `scaffolding` scaffolding: “Soft Igor de Rachewiltz:”
- **error** L68 `scaffolding` scaffolding: “Soft Hans Ulrich Vogel:”
- **error** L68 `scaffolding` scaffolding: “Soft John Larner:”
- **error** L68 `scaffolding` scaffolding: “Soft further company:”
- **error** L70 `scaffolding` scaffolding: “Soft remaining battlefield:”
- **error** L70 `scaffolding` scaffolding: “Soft useful outcome:”
- **error** L72 `scaffolding` scaffolding: “Soft middle path:”
- **error** L72 `scaffolding` scaffolding: “Soft binary refused:”
- **error** L78 `scaffolding` scaffolding: “Soft control:”
- **error** L80 `scaffolding` scaffolding: “Soft control:”
- **error** L82 `scaffolding` scaffolding: “Soft control:”
- **error** L84 `scaffolding` scaffolding: “Soft control:”
- **error** L86 `scaffolding` scaffolding: “Soft panel lesson:”
- **error** L86 `scaffolding` scaffolding: “Soft join:”
- **error** L92 `scaffolding` scaffolding: “Soft refusal:”
- **error** L94 `scaffolding` scaffolding: “Soft honesty:”
- **error** L96 `scaffolding` scaffolding: “drafter”
- **error** L100 `scaffolding` scaffolding: “Soft warmth in restraint:”
- **error** L102 `scaffolding` scaffolding: “Soft art:”
- **error** L104 `scaffolding` scaffolding: “Soft confession:”
- **error** L108 `scaffolding` scaffolding: “first-draft”
- **error** L122 `scaffolding` scaffolding: “outline end matter”
- **error** L126 `scaffolding` scaffolding: “Soft close of the list:”
- **error** L130 `scaffolding` scaffolding: “Soft last breath:”
- **error** L130 `scaffolding` scaffolding: “Soft art of this retelling:”
- **error** L130 `scaffolding` scaffolding: “Soft farewell to the three volumes:”
- **error** L130 `scaffolding` scaffolding: “first-draft”
- **error** L136 `scaffolding` scaffolding: “Soft caution:”
- **error** L136 `scaffolding` scaffolding: “Outline III-12”
- **error** L142 `scaffolding` scaffolding: “Soft rule:”
- **error** L146 `scaffolding` scaffolding: “Soft silence hermeneutic:”
- **error** L154 `scaffolding` scaffolding: “Soft series stance:”
- **error** L156 `scaffolding` scaffolding: “Soft lesson:”
- **error** L160 `scaffolding` scaffolding: “Soft close:”
- **error** L160 `scaffolding` scaffolding: “SERIES-STATUS”
- **error** L160 `scaffolding` scaffolding: “first-draft”
- **error** L160 `markers` Note [13] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** — `tags` expected exactly one tag line ([V] [R] [M] [reception]), found 0
- **warning** L62 `names` “Caidu” is close to gazetteer name “Caindu” (variant spelling?)

### vol-3/front-01-indian-ocean-world.md

- **error** L4 `quote_verify` epigraph not found in refs/ (misquoted, 50% of 5-grams match): “and when the ships had been made ready”
- **error** L55 `scaffolding` scaffolding: “reported_only”
- **error** L51 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)
- **error** L55 `markers` Note [3] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

### vol-3/front-02-maps-seas-and-return.md

- **error** L4 `quote_verify` epigraph not found in refs/ (invented?, 0% of 5-grams match): “and from zayton they sailed”
- **error** L9 `scaffolding` scaffolding: “placeholder”
- **error** L86 `scaffolding` scaffolding: “placeholder”
- **error** L86 `markers` Note [1] does not open with a marker (✓ ~ ✗ ◇ ? or a “core / detail” pair)

