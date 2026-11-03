# Intake — people deep research, run 2 (S-05 follow-up)

_2026-10-22. Raw run: `CHR-people-2-raw.md` (the 12 rows run 1 left open; prompt in `CHR-people-intake.md` § Follow-up prompt). Applies to `CHR.T4`; partly to S-14 (#1, #6, #15) and S-15._

## Trust check

**Verdict: usable.** Unlike run 1, this run cites real works (Yule–Cordier, Cleaves 1976, Formentin–Schiavon 2024, Pelliot, Moule, Moule–Pelliot, Orlandini 1926, Larner, Rossabi, Hart, Plebani, Bolognari 2021) and says for each claim whether it SAW or only REPORTED the source. Its "SAW Yule" claims could be checked against `refs/` directly, so this intake checked claims, not only citations.

- **Works:** every work checked exists. `doi:10.2307/2718743` resolves to JSTOR, and Crossref matches title, author, journal, volume and first page (Cleaves 1976). `doi:10.6093/1593-2214/10840` resolves to *Reti Medievali Rivista*, and the open-access PDF was read (Formentin–Schiavon 2024). The other works are known standard titles. Bolognari 2021 and Orlandini 1926 were not found online here and go into the bibliography as `unconfirmed`.
- **Claims read against the source** (11). **8 hold, 3 overstate:**

| # | Claim | Checked against | Result |
|---|---|---|---|
| 1 | Argon d. 10 March 1291 = 7 Rabīʿ I 690; "7 March" is the Hijri day misread | Yule I (note: "died 10th March, 1291"; a footnote has 12 March); tabular Hijri conversion run here: 7 Rabīʿ I 690 → 10 March 1291 (Julian) | **holds** |
| 4 | Dorjé was Chabi's eldest son, born 1240 ("SAW Yule") | Yule I: a son older than Chingkim, *Jurji/Torchi/Dorjé*, "probably died early"; Yule gives **no mother and no 1240**, and no 1243 for Chingkim | **overstated**: only "elder son, died early" taken |
| 6b | Capture: Ramusio's Curzola 1298 vs Jacopo d'Acqui's Ayas; Yule rejects Ayas because the battle was May 1294 and Marco was not home until 1295 | Yule I, prolegomena (the passage is there, nearly word for word) | **holds** |
| 6c | Marco died 8 or 9 January 1324; will 9 January | Formentin–Schiavon 2024, p. 1 text: "quando vi morì, l'8 o il 9 gennaio 1324" | **holds** (the "memorandum, after sunset" detail is not in the article: not taken) |
| 7a | Two Fiordelisas: Niccolò's probable wife (Trevisan?) and a daughter of the younger Maffeo | Yule I: "The same Maffeo [the younger] had a daughter Fiordelisa… I conjecture that this cognata Fiordelisa (Trevisan?) was the wife of the absent Nicolo" | **holds**; this also explains run 1's error |
| 7b | Stefano and Zannino were Niccolò's illegitimate sons; Niccolò dead before 1300 ended | Yule I: "Nicolo, who died before the end of the century, left behind him two illegitimate sons, Stefano and Zannino" | **holds** |
| 7c | Maffeo the uncle's will is dated 31 August 1300 | Yule I: his last will was **February 1309**, not extant; the extant 1300 will is the *younger* Maffeo's | **overstated** (conflation): Yule's date taken |
| 8 | Yule's Loredano guess rests on a "sister of Lady Donata" | Yule I: "Agnes Loredano as the sister of the Lady Donata" in two documents | **holds** |
| 9a | Fantina m. Marco Bragadin, who died at Candia in 1360; her suit in 1366 | Formentin–Schiavon 2024 (Bragadin d. 13 July 1360; the sentence of 13 July 1366); Yule I (Fantina's husband Marco Bragadino) | **holds** |
| 9b | Bellela m. Bertuccio Querini; Moreta m. Ranuccio Delfin, then Tommaso Gradenigo ("SAW Formentin–Schiavon and Yule") | Formentin–Schiavon: no Querini, Delfin or Gradenigo in the text. Yule I: Moreta's husband Ranuzzo Dolfino; "**the name of Bellela's husband does not appear**"; a Bertuccio Quirino appears only as a claimant against Donata | Moreta/Dolfino **holds** (Yule); Bellela/Querini **overstated**; Gradenigo unchecked |
| 11 | Meloria is Yule's conjecture, not a document | Yule I sidenote: "Rusticiano, perhaps a prisoner from Meloria" | **holds** ("layman" still unsourced) |
| 12 | Six churches at Zhenjiang plus one at Hangzhou | Cordier's addendum in Yule II: the Kinsay church "was one of the seven churches built in China by Mar Sarghis" | **holds** (seven in all) |

Not checkable here (REPORTED by the run, and marked so in the registry): #2 the Yongle dadian wording (Cleaves's full article is paywalled); #3 Chabi's birth year (run 2 also could not settle it); #5 Pelliot's Otchigin argument; #6d the Agnese will (Bolognari 2021; Ca' Foscari release not found from here); #10 the will's Marciana shelfmark.

## Applied

**Registry (`characters.yaml`):**
- `arghun`: 10 March 1291, with the conversion note.
- `gaykhatu`: 23 July 1291 – 24 March 1295 (now Yule).
- `oulatay`, `apusca`, `coja`: Chinese forms and the notice's silence on survivors.
- `dorji`: only Yule's "first-born, died early"; mother disputed.
- `nayan`: Polo-only age and cross banner; Pelliot for the descent (reported).
- `marco`: birth by inference; the capture argument; death 8 or 9 January 1324; Agnese (reported).
- `niccolo`, `maffeo`: per Yule; run 1's "daughter Fiordelisa" explained and dropped.
- `donata`: dead 1333–36; the basis of the Loredano guess.
- `fantina` (`verify` cleared), `bellela`, `moreta`: per Yule and Formentin–Schiavon.
- `peter-the-tartar`: shelfmark and editions (reported).
- `rustichello`, `mar-sarghis`: as checked.

Elsewhere:
- **Chapter backlogs:**
  - III-09: keep "tenth of March"; "only Coja survived" is the Book's claim.
  - III-10: half-brothers and Maffeo checked; a new item for Agnese, the eldest daughter and the Bragadin suit.
  - II-12: Polo's two churches against the record's seven.
  - I-02: the bachelor clause is still unsupported.
- **`registry/bibliography.bib`:** `cleaves1976chinese` and `formentin2024codice` (confirmed); `bolognari2021agnes` and `orlandini1926marco` (unconfirmed).
- **`registry/characters.md`:** the contested-facts table.
- **`CHR.T4`:** progress.

## Still open

| Row | Question | Next |
|---|---|---|
| chabi | Birth 1216 or 1227 | *Yuan shi* 114 (Houfei zhuan); Rossabi 1988 in a library |
| dorji | Mother; birth year | *Yuan shi* 107 (Zongshi table) |
| maffeo | Married? | Orlandini 1926 (to see) |
| bellela | Husband | Orlandini 1926; Moule–Pelliot 1938 I (the will) |
| marco | Agnese article; documentary basis of 1254 | Bolognari, *Studi Medievali* 62 (2021) (to see) |
| rustichello | Layman? | Larner 1999; the Arthurian-compilation scholarship (S-15) |
| peter-the-tartar | Shelfmark, as seen | Plebani 2019; the Marciana catalogue |
| coja | Survival | Cleaves 1976, full text |

These are library checks, not another search run. They belong to S-15's intake when it comes.
