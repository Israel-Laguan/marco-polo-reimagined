# Intake — people research, run 4, and the close of the open rows

_2026-11-10. Raw run: `CHR-people-4-raw.md` (Consensus; 5 questions, second-hand allowed). Closes the 8 rows in `CHR-people-2-intake.md` § Still open, one way or the other._

## Trust check

**Verdict: the run is empty.** Consensus searches only its own paper index. It cannot open ctext, Wikisource or the Internet Archive, so it found nothing beyond Menshikova's abstract, which run 3 had already found. **Do not use Consensus for primary-text questions.**

So the intake opened the open-access sources the prompt named and read them directly:
- the *Yuan shi* on zh.wikisource (juan 106, 107, 114);
- Moule–Pelliot 1938 vol. 1 (IA `descriptionofwor01polo`, OCR text);
- `refs/yule-vol1.txt` and `refs/yule-vol2.txt`.

Everything marked **seen** below was read there.

## Findings (seen by the intake)

| Row | Finding | Source (seen) |
|---|---|---|
| chabi | Neither the biography nor the empresses' table gives a birth year or an age. She died in the 2nd month of Zhiyuan 18 (1281). The biography says she bore Yuzong (生裕宗), i.e. Zhenjin, and no other son. | *Yuan shi* 114 (世祖昭睿順聖皇后); 106 (后妃表, 察必皇后) |
| dorji | "世祖皇帝，十子：長朵而只王；次二皇太子真金…": Dorji is the eldest of ten sons. **No mother is named.** | *Yuan shi* 107 (宗室世系表) |
| marco (1254) | The 1254 date is an inference from the Book: Marco is "said to have been fifteen years old in 1269, so that he must have been born in 1254". | Moule–Pelliot I, introduction (OCR text) |
| peter-the-tartar | The will is Biblioteca Marciana, **Cod. Lat. V, 58–59, collocazione 2437–2438**. The folio reads 33 or 35 (OCR unclear; the page image would settle it). The Marciana bought it from Amedeo Svajer's library in 1794; Cicogna and Lazari printed it. The clause reads: *"Jtem absoluo petrum famulum meum de genere tartarorum ab omni vinculo seruitutis ut deus absoluat animam meam ab omni culpa & pecato."* Yule's English ("Also I release Peter the Tartar, my servant, from all bondage…") is in `refs/yule-vol1.txt`, and his 1328 grant of Venetian citizenship is in `refs/yule-vol2.txt` (Appendix C, doc. 13). | Moule–Pelliot I (the will, Latin transcription); Yule I and II |

## Applied

`characters.yaml`: `chabi`, `dorji`, `marco` and `peter-the-tartar` now carry the seen evidence. The yaml parses.

## Final status of the 8 rows

| Row | Status | What we know | What would settle the rest |
|---|---|---|---|
| chabi | **not possible for now** (birth year) | The primary source is silent on birth and age. 1227 rests on Menshikova 2025 (abstract only). No source for 1216 was found | Rossabi 1988 and Menshikova's references, in a library |
| dorji | **settled in part** | Eldest son (seen). The primary source doesn't say who his mother was; Çelik 2022 says Chabi (abstract only) | Çelik's full text; Rashid al-Din on Kublai's wives |
| marco | **settled in part** | 1254 is an inference from the Book's "fifteen in 1269", not a document (seen). Agnese/Bolognari 2021: not found | *Studi Medievali* 62 (2021) in a library |
| peter-the-tartar | **settled** (folio pending) | Shelfmark and clause seen in Moule–Pelliot; English and the 1328 grant in Yule | The IA page image for the folio (33 or 35) |
| coja | **not possible for now** | The Book says only Coja survived. The Chinese record (*Yongle dadian*, 站赤) is not online in any form found here | Cleaves 1976 full text (JSTOR) or Yang Zhijiu's article |
| maffeo | **not possible for now** | Not attempted in run 4 | Orlandini 1926 (archive or library) |
| bellela | **not possible for now** | Yule: "the name of Bellela's husband does not appear" | Orlandini 1926; Moule–Pelliot I's family documents (open, but not yet searched for her) |
| rustichello | **not possible for now** | Layman or not is unsourced either way; Meloria is Yule's conjecture | Larner 1999; the Arthurian-compilation scholarship |

**Best effort done:** four search runs, plus a direct read of every open-access source named. The "not possible for now" rows need a library or archive, and no further search run should be made for them.
