# Deep research prompts — the five sources Yule–Cordier does not place

**For:** S-24 pass B, the last 5 names in `plans/registry/name-keys.csv` with rule `research`. The other ~550 "via YC" mentions are already located in Yule (see `plans/status/pass-b-worklist.md`, columns *Where in YC* and *Scope*) and need no research.
**Run** each batch as its own deep-research job. Save each output untouched:

| Batch | Sources | Save to |
|---|---|---|
| A | Chinese and Mongol-period works: *Mengliang lu*, *Chuogeng lu* (Ch’ue keng lu) | `plans/research/results/CIT-batch-A-raw.md` |
| B | *Marāṣid al-iṭṭilāʿ*, Tsung tien (*Tongdian* or other), Columbus's *Libro de las Profecías* | `plans/research/results/CIT-batch-B-raw.md` |

**Why these five:** Yule cites each of them with the writer's own name or a title spelling we could not match, and the Notes rely on them for a specific point. Each Note names the work, so the research only has to find the right edition.

**Intake:** the answer goes into `plans/registry/bibliography.bib` (one entry per edition, with a status comment), and the name map gets the key. Per `research/README.md`, a key is only added once the edition is confirmed in a library catalogue.

---

```text
BATCH A — Chinese and Mongol-period works

I am preparing a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920) for print, with endnotes cited in Chicago author-date style. Two Chinese works are named in the Notes. For each, I need the exact citation for the edition the Notes should cite, and the scholarly English translation or study if one exists.

1. MENGLIANG LU (夢粱錄, "Record of the Dream of the Millet Harvest"). Yule–Cordier quotes it as "Mêng-liang-lu", the description of Hang-chau (Hangzhou, Kinsay) published by Wu Tzu-mu (Wu Zimu) in 1274. Give: (a) the standard modern critical edition (Chinese, with publisher, year); (b) any annotated English translation or study of the Hangzhou sections (Hangzhou as a city description; Yule cites Bretschneider and Hirth-era translations, so check what they were); (c) a free digitised copy (Chinese digital library, Internet Archive, Harvard-Yenching, or similar).

2. CH’UE KENG LU (輟耕錄, "Notes Written While Pausing from Ploughing"), by Tao Zongyi (Tao Zongyi, c. 1316–1403), finished 1366. Yule quotes it under "Ch’ue keng lu" for the Yuan palace and city material. Give: (a) the standard modern Chinese edition (publisher, year, and whether it is the Zhonghua shuju edition); (b) English translations or studies of the passages on the Yuan capital and palaces (Bretschneider's *Mediaeval Researches* quotes it; check which passages); (c) a free digitised copy.

For each work, say which of the two Chinese editions (original Ming print or modern critical edition) a scholar cites today, and give a locator system that does not need page numbers (chapter/juan numbers).

BibTeX: one entry per work. Key = lower-case surname or title word + year + first title word (e.g. `wu1274mengliang`, `tao1366chuogeng`). Never date an old work by its scan or upload date; put the digitisation in an addendum field.

OUTPUT FORMAT (required). (1) A table: work · who · edition to cite (publisher, year) · English translation or study (if any) · free copy URL · confidence. (2) BibTeX for every edition cited. (3) What you could not confirm. Rules: do not invent editions, dates, juan numbers or URLs. If you have not seen a catalogue record, say "unconfirmed". Prefer library catalogues (WorldCat, national libraries), publisher pages and scholarly bibliographies.
```

```text
BATCH B — Arabic geographical dictionary, a Chinese encyclopaedia, and Columbus's book

I am preparing a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920) for print, with endnotes cited in Chicago author-date style. Three works are named in the Notes. For each, I need the exact citation for the edition the Notes should cite, and the scholarly English translation or study if one exists.

1. MARĀṢID AL-IṬṬILĀʿ ("Observatory of Information", Arabic geographical dictionary of place names, compiled in the early 14th century, often attributed to Ṣafī al-Dīn al-Baghdādī, d. 1338). The Notes cite it for place names along the Gulf and Persian coast. Give: (a) the standard critical edition (Leiden, Brill, or other; editor, year); (b) whether the Notes' citation should be to the dictionary itself or to a secondary study that quotes it; (c) a free digitised copy (Internet Archive, Gallica, Brill open access, or similar).

2. TSUNG TIEN (Palm Hall / Tsung-tien, Yule's note in the Chandu/Shangdu chapter). Yule (Book I, ch. LXI) reads it as "Tsung tien, alias Tsung mao tien", a Chinese architectural term. The likely source is an encyclopaedia or dynastic treatise (the Tongdian of Du You, or a Yuan-period work such as the *Yuan shi*). Identify the work and the passage that Yule means, using Yule's notes and Palladius (1876) if needed. Give the standard edition and any English translation.

3. LIBRO DE LAS PROFECÍAS (Columbus's "Book of Prophecies", compiled 1501–1505). The Notes cite it for Columbus's reading of Polo and the Ptolemaic and biblical geography behind the western route. Give: (a) the standard critical edition (Spanish; Cecil Jane's 1930 English translation as *The Book of Prophecies*, or any later edition; check and give the best current one); (b) a free digitised copy or facsimile, if any; (c) the locator system scholars use.

BibTeX: one entry per work. Key = lower-case surname or title word + year + first title word (e.g. `marasid1300s`, `columbus1501prophecies`). Never date an old work by its scan or upload date.

OUTPUT FORMAT (required). (1) A table: work · who · edition to cite (editor, publisher, year) · English translation or study (if any) · free copy URL · confidence. (2) BibTeX for every edition cited. (3) What you could not confirm, and any work you think the Notes might mean instead. Rules: do not invent editions, dates or URLs. If you have not seen a catalogue record, say "unconfirmed". Prefer library catalogues, critical editions and scholarly bibliographies.
```
