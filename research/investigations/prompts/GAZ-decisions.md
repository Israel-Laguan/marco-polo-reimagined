# Deep research prompt — three open gazetteer decisions

Run in a deep-research tool that can read books and databases. Save the output to `plans/research/results/GAZ-decisions-raw.md` with a first line naming the tool, model and date. Intake: `plans/research/results/GAZ-intake.md`, fourth-pass section.

Why this prompt: three rows need a decision before the maps and chapter naming can be finished. Each decision depends on evidence we do not yet have in a checkable form. This prompt asks only for that evidence.

```text
I am building a gazetteer for a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920). Three decisions are open. For each, find named, checkable evidence. Do not give me a recommendation based on what is "usual" or "standard"; do not invent citations; mark anything you could not open as NOT FOUND.

ALREADY ESTABLISHED (do not re-research; use as the starting point and cite these as given):
- Pelliot, Notes on Marco Polo, Vol. I pp. 232–235 (entry 128, CAUGIGU): the name is Chiao-chih-kuo (Tonkin, Kafjāh-guh of Rashid al-Din). Pelliot places the described conditions on the Upper Red River, contiguous with Yunnan, and says Upper Laos was independent of Annam. Yule's Kiang Hung (Jinghong) reading is independent of Pelliot.
- Pelliot, Notes II pp. 856–858 (entry 363, TOLOMAN): the best manuscripts read "Toloman" (Yule adopted "Coloman" against them). Pelliot explains it as T'u-lao-man, the barbarians of the Hsü-chou / Wu-mêng region of north-east Yunnan.
- Pelliot, Notes I pp. 91–92 (BELOR) and II pp. 800–802 (PEM) are checked; they are not part of this prompt.
- Tenduc (Pelliot, Notes II pp. 848–852, entry 358): the province is the north-eastern corner of the great bend of the Yellow River, occupied by the Öngüt. For the city Pelliot favours Tung-shêng (Yuan name, modern Togtoh / Tuoketuo) over Sui-yüan. The name is from T'ien-tê (Klaproth).

DECISION 1 — CAUGIGU: where is the point?
Options: (a) Kiang Hung / Jinghong, Yule's reading; (b) the Upper Red River / Lao Cai–Yunnan border country, Pelliot's reading; (c) region only (no point).
Find:
1. Any published identification of Caugigu's *location* (not only its name) after Pelliot, with the author, year, work, page, and a verbatim quote of at most 40 words. Priority: Haw, Marco Polo's China (2006), chapter on Yunnan and the south-west; Vogel, Marco Polo Was in China (2013); Atwood, Encyclopedia of Mongolia (2004); Wheatley, The Golden Khersonese (1961); Luce, Old Burma–Early Pagán (1969); Chinese-language studies of 交趾 / 金齒 / 車里 in the Yuan period.
2. Yuan-period administrative names for the Upper Red River and Yunnan–Tonkin border seats that Polo's itinerary could reach from Zardandan and Mien (c. 1280–1295), with the CHGIS ID and coordinates. CHGIS API for placename search: https://chgis.hudci.org/tgaz/placename?fmt=json&n=<name>&yr=1290 ; per-ID lookup: https://chgis.hudci.org/tgaz/placename/json/<hvd_ID>. Verify each ID by calling the API; do not give IDs from memory.
3. Whether Rashid al-Din's Kafjāh-guh (Chiao-chih) is placed by any source at the Red River or at Kiang Hung, and what the source says.
4. Which of (a), (b), (c) each source supports, and which it contradicts.
Return: a table of sources (author, year, work, page, quote ≤40 words, access: full view / search-only / snippet), then the Yuan-period seats with CHGIS IDs and coordinates, then "Not found".

DECISION 2 — COLOMAN / TOLOMAN: which book form?
Options: (a) keep Coloman (Yule's book form, used in the chapters); (b) switch to Toloman (the best manuscripts, per Pelliot).
Find:
1. Which English editions and translations use Coloman and which use Toloman: Yule–Cordier (1903), Moule & Pelliot (1938), Latham (Penguin, 1958), and any modern edition or translation you can open. Give the page and a verbatim quote of the name in each.
2. The manuscript readings for the name as listed by Moule & Pelliot's apparatus, and whether any of the printed English editions note the variant. Pelliot's own entry is at Notes II pp. 856–858; give anything you can confirm from its apparatus.
3. Any scholarly argument since 1938 for or against Toloman as the book form, with author and page.
4. Modern scholarly usage of T'u-lao-man / Tulaoman as the ethnonym in Yuan sources (e.g. Yuan shi ch. 61 and the postal-station records), with the Chinese characters and a source for each use.
Return: a usage table (edition | form used | page | quote), then the scholarly arguments, then "Not found".

DECISION 3 — TENDUC: is there a city point, and where?
Options: (a) keep only the province (current); (b) add a city point at Tung-shêng / Togtoh; (c) add a city point at Sui-yüan / Kuei-hua-ch'êng (Pelliot's other candidate).
Find:
1. Pelliot's own account is cited above. Find the scholarly evidence for Tung-shêng vs Sui-yüan as Polo's Tenduc city, with author, year, page and verbatim quote. Priority: Pelliot, T'oung Pao 1914 pp. 631–634 (cited in Notes II p. 850); Haw 2006 Tenduc discussion; Moule & Pelliot 1938 apparatus on Tenduc.
2. The CHGIS entries for Tung-shêng (东胜州), Sui-yüan (绥远), and Kuei-hua-ch'êng (归化城), with IDs, Yuan-period validity (must include c. 1280–1295), and coordinates. Note any that have no point valid in 1290. Use the CHGIS API as above; verify each ID.
3. A named modern coordinate for Togtoh (托克托县 / Togtoh County) from Wikipedia or a Chinese administrative source with its name; compare with CHGIS.
4. Whether the Öngüt capital (Olon Süme / Olon Sume, 'many temples') or any site in the Tümed plain is argued by a named scholar to be Tenduc's city, and what distance from the Yellow River each source gives.
Return: a table of candidates (name, Chinese, CHGIS ID, Yuan validity, coordinates, source), then the scholarly preference with quote, then "Not found".

OUTPUT FORMAT
One section per decision, each ending with a short line: "Evidence supports: ..." — state what the evidence supports, not what I should choose.
Then "Sources consulted" (full references) and "Could not open" (paywall, login, region block).
Do not supply a recommendation for the decision itself; I will make it.
```

## Intake notes

- Verify any CHGIS ID by calling the API before you use it. Earlier runs gave IDs that did not exist.
- A coordinate without a named source does not enter the gazetteer.
- Decision 2 may be settled by a person; the research only shows which editions use which form.
