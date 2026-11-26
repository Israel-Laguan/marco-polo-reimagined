I'll try to open each source directly and report, per item, exactly what was seen (pixels, OCR, transcription, or catalog only) and where access failed.

The local shell has no outbound network access (confirmed — proxy rejects it); only WebSearch/WebFetch reach external sites, and I already used those successfully for the Pelliot pages. Continuing with the remaining items via WebFetch/WebSearch.

## Evidence table — what was actually seen vs. not

**Legend:** 🟢 = image/pixels viewed · 📄 = transcribed edition/translation seen (not ASVe original) · 🔤 = OCR text seen (archive's own OCR, not a visual check) · 📋 = catalog/description only · ⛔ = NOT SEEN (barrier stated)

### 1. Venice — Pagano will & 1328 Avogadori proceeding

| Record | Status | What I actually have |
|---|---|---|
| ASVe, Notarile testamenti, Pietro Pagano, b. 830, **prog. 5** | ⛔ NOT SEEN | ASVe has no public page‑image viewer reachable from here (archiviodistatovenezia.it refused the fetch; no IIIF/digitization found for this busta). I found a *different* unit in the same busta — b.830, **n. 36**, f. 11r, Agnese Polo's 1319 will (Bolognari 2022) — but nothing matching "prog. 5." I cannot confirm or deny its contents, and did not infer anything about it from the unsearched busta index. |
| The "actual March 1328 Domini Advocatores proceeding…summarized by Yule" | 📄 Transcribed edition seen | Via a mirror of the Gutenberg Yule‑Cordier text (bookrags.com, p.147 of the printed edition): *"In March, 1328, Marco Polo, called Marcolino, of St. John Chrysostom… represents before the Domini Advocatores… that certain imprestita that had belonged to the late Maffeo Polo the Elder, had been alienated and transferred in May 1318… to whom the said Messer Maffeo had bequeathed 1000 lire by his will executed on **6th February, 1308 (i.e. 1309)**. The Advocatores find that the transfer was… unjust… and order that… it should be revoked."* This is Yule's English rendering, not the ASVe Latin original — I did not open the Gutenberg page itself (robots‑disallowed) but did see this exact passage via the mirror. |
| "Published 1309 Venetian‑style will converts to 1310 modern" (Orlandini / Moule‑Pelliot) | ⛔ NOT SEEN | I located citations *to* Orlandini's 1926 work (in Ca' Foscari papers) but not its text, and no Moule‑Pelliot edition text. Cannot verify the "1309→1310" conversion claim directly. |

**Comparison requested (parties/conditions of the imprestiti bequest vs. the separate 1,000‑lire payment):** Cannot be done responsibly. I have only Yule's summary of the 1328 proceeding (bequest: 1,000 lire to **Marcolino**, by Maffeo the Elder's will of 6 Feb 1308 m.v./1309 modern, later found wrongly alienated). I do **not** have the 1309 will itself (Orlandini/Moule‑Pelliot) to compare parties/conditions against, and I do **not** have ASVe b.830 prog.5 to check whether that's the same instrument. Per your instruction, I am not assuming these are the same will absent the records, and I'm not conflating the two already‑distinguished year‑conversions. The separate "Marco's own 1,000‑lire payment for multiple losses" does not appear anywhere in what I retrieved — NOT SEEN, not confirmed as existing in this material.

### 2. Pelliot, *Notes on Marco Polo* II — Toyo Bunko/NII digital archive

All four pages were opened at `dsr.nii.ac.jp/toyobunko/III-2-F-c-104/V-2/page-hr/…`. What's returned by WebFetch for these URLs is the site's **OCR Text** field — per your instruction, this is *not* a visual inspection of the page image, only the archive's OCR layer. The actual JPEG/IIIF image URLs exist (e.g. `…/images/gray/0207.jpg`, IIIF viewer link) but I did not render/view pixels — I only have the OCR transcript and the printed page‑footer numerals shown in the navigation strip.

| Location | Printed page # (from nav strip) | OCR heading / entry # | Note |
|---|---|---|---|
| FERLEC | p.129 (footer shows "8" as a signature mark, not folio #) | **231. FERLEC** | Confirmed entry number 231, as asked. Content: identifies Ferlec with Malay Perlak. |
| LAMBRI | p.165 | **270. LAMBRI** | LAMBRI is indeed on 165 (continues to 166, where entry **271. LAR** begins — not a second LAMBRI entry). Your expected "0165–0166" is OCR-confirmed: 165 opens LAMBRI, 166 continues it then starts LAR. |
| PENTAN | p.206–207 | **313. PENTAN** begins top of 206 (not 0206 mid‑page) and continues onto 207, where **314. PIANFU** begins | So "OCR shows entry 313 PENTAN begins on 0206" is correct — confirmed by direct refetch, not secondhand. |
| 0207 text re: Ṭawālisī | p.207 | — | Exact OCR sentence, confirmed: *"By reading « Talamasi », we should not be very far from Ibn Baṭṭūṭah's « Ṭawālisī »; that does not help much however, as « Ṭawālisī » is otherwise unknown."* This is within the Odoric/"Paten" discussion that precedes entry 314 PIANFU on the same page — **not** inside the PENTAN entry itself. |
| Vol. III index / SEILAN / SAGAMONI BORCAN | ⛔ NOT SEEN | I did not locate or open vol. III pages in this session; no inference drawn about their contents. |

### 3. Guillot & Kalus 2008; Pankhurst 1982; Sasaki 2015

| Source | Status |
|---|---|
| Guillot & Kalus, *Les monuments funéraires…Pasai* (2008), on the Malik al‑Salih tomb specifically | ⛔ NOT SEEN. I found only a book review (Studia Islamika, van der Meij, pp.185‑187, describing the book generally) and citation strings in later articles referencing pp.69‑74 and 326‑332 for various tombs — but not the book's own text on Malik al‑Salih's stone. No full text reachable from here. |
| Pankhurst 1982 on the "Abash" story | ⛔ NOT SEEN. No source matching "Pankhurst 1982" on an "Abash" legend turned up; searches returned unrelated Pankhurst works (1955 *Ethiopia*, other dates). Cannot confirm this citation exists as described, nor deny it — simply not located. |
| Sasaki, *The Origins of the Lost Fleet of the Mongol Empire* (Texas A&M UP, 2015) | 🔤 Partial OCR/text seen via archive.org PDF (`Book_1137`). **Confirmed single‑authored monograph**, not an edited volume (matches your note). Table of contents and passages on storm/timber were retrieved (first 100,000 of 363,802 characters — later chapters, incl. Ch.9/Conclusion, not yet read). **Storm** is treated as primary cause throughout (pp. viii, 7, 19, 26, 29 per running heads). **Fire**: not found as a cause in the portion read — only as a weapon description (the *tetsuhau* bomb) and the separate 1274 Hakata burning; no fire‑as‑cause‑of‑fleet‑loss passage surfaced yet. If you need the later chapters checked for fire/timber-decay discussion specifically, that requires a second pass I haven't done.

### 4. Ibn ʿAbd al‑Ẓāhir, *Tashrīf al‑ayyām*, ed. Murād Kāmil, Cairo 1961, pp.170‑73

| | Status |
|---|---|
| Arabic primary text, pp.170‑73 | ⛔ NOT SEEN. Only a library catalog record (ARCE) was reachable, giving full bibliographic description (editors Murād Kāmil **and Muḥammad ʿAlī Najjār**, Cairo 1961, 8+90+329 pp.) — catalog/description only, no page images or text. |
| Published translation | ⛔ NOT SEEN. None located. |
| Loiseau 2019 chapter citing it for the 689/1290 embassy | ⛔ NOT SEEN. The PDF link found (`cours.univ-paris1.fr/…Chrétiens d'Égypte, musulmans d'Éthiopie…`) sits behind a Moodle course login — fetch returned only the login shell, no chapter text. I cannot state what Loiseau's chapter says, and did not find it elsewhere. |
| Whether the primary passage links the mission to Polo's bishop story | ⛔ Cannot be assessed — no access to either the Arabic text or Loiseau's discussion of it. |

---

**Summary of access barriers:** ASVe has no reachable public digitization/viewer; the Guillot‑Kalus monograph, the Pankhurst citation, the Tashrīf al‑ayyām primary text, its translation, and Loiseau's chapter text are all behind no-access/paywall/login barriers from this environment (web-tool only — the sandbox shell itself has no outbound network access at all, confirmed by a direct connection test). Where I quote something, I've marked whether it's OCR, a transcribed/translated edition, or catalog metadata — none of it is a verified visual inspection of a manuscript or original printed page image in this session.