# Period sources for the Polo plates: what holds up

Only two sources in this research are both dated inside the window by a primary text or event and confirmed open to scripts. The first is the Munich Qazwini, BSB Cod.arab. 464 (Wasit, 1280), which has an open IIIF manifest with 428 canvases. The second is the 1281 Takashima wreck assemblage, published in free Japanese site-report PDFs. One more source comes close: the Kyushu University IIIF copy of the Mōko Shūrai Ekotoba is public domain, but it is a late-Edo copy of a scroll made c. 1293–1320s. Everything else is one of four things: dated but blocked to scripts (BnF Suppl. persan 205, the UNESCO Xanadu dossier), viewable but dated by attribution (the NPM Taipei Khubilai and Chabi leaves), viewable but just outside the window (Morgan M.500, 1297–1300; Vesconte, c. 1320), or modern documentation of period fabric (Ayas ruins, Stein photographs, Takht-i Sulayman finds). I could not find a good source for G1, for the Xiangyang trebuchet, for ships of 1250–1300 in either sea, for pearl diving, Adam's Peak, the Pandya coast, or Badakhshan mining. For those, the honest basis for a plate is a text (Rubruck, the *Yuanshi*, Pryor's contracts) plus dated parts drawn from neighbouring sources. The research run was cut short by rate limits: each thread made about 14–17 tool calls, and several key pages were never opened. Many leads below are therefore marked "found in a catalogue or citation" or "from memory" and need checking by hand.

**Confidence marks.** I use three marks: **opened and confirmed**, **found in a catalogue or citation**, and **from memory**. They map one-to-one onto the marks in the notes (OPENED / OC; CITED / CAT / CATALOGUE / DOC; MEMORY / MEM). **NEW** means published or built after 2013. Items you already hold are excluded (Met and Cleveland Open Access, Walters W.539, Edinburgh Or.MS 20, Diez Albums, the Cleveland mariegola leaf, and the others in your list).

## Ledger: six gaps, two confirmed in-window anchors

| Gap | Best thing found | Confirmed? | In window? | Verdict |
|---|---|---|---|---|
| **G1** ger on a wagon before c. 1350 | Nothing. The closest are the Topkapı H.1653/H.1654 copies of Rashid al-Din (1314/1317, with Timurid additions), Liao cart murals (11th–12th c.) and Bronze Age clay wagon models | Catalogue or citation, and memory | No | **I could not find a good source for G1.** Work from Rubruck's text (1253–55) |
| **G2** Mongol/Yuan kit 1250–1300; Xiangyang trebuchet | The Takashima 1281 site reports (free PDFs on 全国遺跡報告総覧), and the Kyushu public-domain IIIF copy of the Ekotoba | The Kyushu IIIF copy was opened; **Matsuura Report 4 (2011, record 62589) was opened: it has helmet, sword, bow, crossbow and arrow drawings and photos (helmets pp. 135–138, pls. 19–20), and the 1277 seal.** Record 21714 has stone shot only | Takashima yes (1281); the Ekotoba is c. 1293–1320s; the Kyushu copy is late Edo | **Met for kit (dated 1281).** I could not find a good image source for the Xiangyang trebuchet; the *Yuanshi* text and Chevedden 2000 are the basis |
| **G3** Yuan hall, vessels, court dress, Green Mount | The NPM Taipei open-data portrait leaves (Khubilai and Chabi, attributed c. 1294), and the Dushan dayuhai jar (*Yuanshi*: Zhiyuan 2, 1265) | The platform and both item records (15489, 15495) were opened | Dress: by attribution only. Halls: plans only | **Partly met for dress.** I could not find a period image of an interior or of the Green Mount |
| **G4** Venice/Genoa people, ships c. 1270, Ayas | BnF lat. 10136 (Genoese Annals drawings, c. 1150–1230s); the Carte Pisane (c. 1270, disputed, no vignettes); Vesconte, Pal. lat. 1362 A (c. 1320) | Haug's front matter was opened; the MEDEA-CHART dating note was opened; the Gallica and Heidelberg pages were blocked | No firmly dated in-window figure or ship image | **Not met.** Ships rest on Pryor's 1246–1269 contracts; Ayas on modern survey photographs |
| **G5** ships, Pasai, Singhasari, Pandya, pearls, Adam's Peak | Candi Singasari statues ("late 13th c.", Kertanagara r. 1268–1292); Candi Jago reliefs on Commons; the Malik al-Salih gravestone (d. 1297) | The CKC advice PDF and the Commons category were opened | Singhasari yes (by dedication); Jago possibly 1343 fabric | **Met for Java only.** I could not find good sources for ships, pearl diving, Adam's Peak or the Pandya coast |
| **G6** Persian town and caravan, Lop, Pamir, Badakhshan | BSB Cod.arab. 464 (1280, open IIIF); Morgan M.500 (1297–1300); BnF Suppl. persan 205 (1290) | The BSB manifest was opened and tested; the Morgan viewer and the BnF notice for Suppl. persan 205 were opened | Qazwini yes; Juvayni yes; Morgan 2–5 years late | **Met for figures, dress and animals,** not for a bazaar or caravan scene. Lop/Pamir: terrain only (Stein, 1906–16). I could not find a good source for Badakhshan mining |

**Verification pass, 2026-11-13.** A second pass checked the rows flagged in this report. It recorded 46 confirmed, 21 corrected, 15 still unconfirmed and 7 blocked verdicts (a few items were checked in more than one file). The marks and values below now follow it. The main corrections: Ghiasian on H.1654 is 2018 and paywalled; the NPM leaves are open-data items 15489 and 15495; BnF Suppl. persan 205 is dated 8 December 1290 and has a Gallica ark; Morgan M.500 has eleven restored folios to avoid; the Cocharelli fragments are now digitised; the Singasari statues went back to Jakarta in August 2023; the Mogao paper is by Kogou et al.; and the Sasaki thesis may be embargoed. The evidence is in `research_notes/Period sources for Polo plates/`: `verify_G1_G3_P3.md`, `verify_G4_G6.md` and `verify_P1_P4_bib.md`.

**Sites that blocked scripts and need a manual browser fetch:**

| Site | What happened |
|---|---|
| Gallica / BnF | Cloudflare challenge on both IIIF and SRU; archivesetmanuscrits.bnf.fr returned 403 |
| British Library | iiif.bl.uk returned 403; bl.digirati.io returned AccessDenied |
| British Museum | The collection API returned a Cloudflare 403 |
| Heidelberg | digi.ub.uni-heidelberg.de showed a "not a bot" check, and so did the Heidelberg journal server |
| cini.it | Returned 403 |
| whc.unesco.org | Returned 403 on every fetch |
| DAI | publications.dainst.org showed an Anubis bot check |
| Digital Silk Road | dsr.nii.ac.jp returned 403 |
| Met | metmuseum.org returned 429; resources.metmuseum.org showed an Incapsula challenge |

These sites also failed: Leiden Digital Collections (connection reset three times), Brooklyn, Chester Beatty, Princeton Art Museum, the Walters, asia.si.edu, Conlan's Princeton page (its direct PDF does open), and ScienceDirect.

On the 2026-11-13 verification pass, cini.it, the BnF archives notice for Suppl. persan 205 and the BL archives record for Add MS 27695 opened. Gallica, metmuseum.org (429), Leiden (connection reset), Qalamos, the Morgan record page (403) and the nabunken site-report records (HTTP 429) still failed.

## G1 — the wagon-borne ger has no dated image before 1350

**I could not find a good source for G1.** None of the searches found a dated image from before 1350 of a round felt tent carried whole on a wagon. No Golden Horde model of one turned up either. The only dated witness is textual: Rubruck (1253–55) describes a tent of about 20 ft carried on a cart drawn by 22 oxen. The rows below are the nearest analogues, ranked. None of them is an in-window ger-on-wagon image.

| Rank | Source | (a) What, holder, URL | (b) Why it might hold in-window material | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Jami' al-tawarikh copies, Hazine 1653 and 1654 | Topkapı Palace Museum Library (TSMK), Istanbul. No viewer URL was opened. See Ghiasian 2018, "The Topkapı Manuscript of the Jāmiʿ al-Tawārikh (Hazine 1654) from Rashidiya to the Ottoman Court", *Iranian Studies* 51(3): 399–425, doi:10.1080/00210862.2018.1428085, paywalled ([Cambridge Core](https://www.cambridge.org/core/product/D298994042B2643F0E25DAA747EA7E09); 2022 is only the online date) (**NEW**) and a [Commons category mirror for H.1654](https://download.osmand.net/wiki/Category:Jami_al-Tawarikh_(1317-1425)_H.1654,_TSMK) | The colophons are dated 1314 and 1317. Outside Edinburgh and Diez, these are the best chance of an Ilkhanid nomad-camp scene | No public IIIF is known. Images exist only as scattered Commons uploads and in publications | "Hazine 1653", "H.1654", "TSMK", "Câmiü't-tevârîh"; Turkish *göçebe çadır*, *araba* | Much of H.1653 is Timurid (c. 1425); separate the two using Inal's and Ghiasian's folio lists. H.1654 holds only about 7 original paintings. No wagon-tent scene is confirmed: Ghiasian's abstract and references show no wagon, tent or camp scene, and the body is paywalled | Found in a catalogue or citation |
| 2 | Topkapı albums Hazine 2152, 2153, 2160 ("Siyah Qalam") | TSMK. Not opened | Nomad camp scenes with carts and tents; some leaves are attributed to the 14th c. | Viewer only and in publications; partial uploads on Commons | "Hazine 2153", "Saray albums", "Siyah Qalam" | The dating is stylistic and disputed (late 14th–15th c.) | From memory |
| 3 | Liao tomb murals of felt-canopied carts (e.g. Kulun Banner) | Chinese excavation reports. Not opened | Excavation-dated steppe carts with tent superstructures, 11th–12th c. Useful as a dated analogue only | CNKI (*Wenwu*, *Kaogu*), often paywalled | 库伦辽墓 壁画 车帐 / 毡车 / 出行图 | Too early; these are box carts, not round gers | From memory |
| 4 | Yuan tomb murals, Inner Mongolia and Shanxi (e.g. Chifeng Yuanbaoshan, Liangcheng) | Excavation reports. Not opened | Some carry dated inscriptions and show Mongol dress under tent-like settings | CNKI; sometimes PDFs | 元墓壁画 毡帐 / 穹庐 / 车 | Probably no wagon; many are labelled only "Yuan" | From memory |
| 5 | DAI Karakorum volumes, FAAK Bd. 8 and Bd. 12 (Franken, *Die "Große Halle"*, **NEW**, 2022 digital edition) | DAI. [Zenon record](https://zenon.dainst.org/Record/000850527), [DAI catalogue](https://publications.dainst.org/books/dai/catalog/view/2052/2379/4075). Not opened (Anubis bot check) | Urban material from Karakorum: ceramics, metalwork, architecture | Open access in principle; blocked to scripts | "Karakorum", "Große Halle", DOI 10.34780/coic-cbqc, 10.34780/133a-8dr5 | No ger or wagon depiction was seen | Found in a catalogue or citation |
| 6 | Steppe clay wagon models | State Historical Museum, Moscow: [exhibit 2422](https://nav.shm.ru/en/exhibits/2422/), [exhibit 2424](https://nav.shm.ru/en/exhibits/2424/) | Structural analogue only: a mid-3rd-millennium BC kibitka model, and an 18th–17th c. BC vessel | Open web pages | "кибитка", "модель повозки" | Out of window by about 3,000 years | Found in a catalogue or citation |

## G2 — Takashima 1281 is the one single-year anchor for Mongol kit

Takashima is the only Mongol arms assemblage in the research dated to a single year inside the window. The finds include iron helmets, swords, arrows, crossbow fittings and *tetsuhau* bombs. The bronze seal of a 管軍総把 is dated 至元十四年九月 (1277) by its incised inscription. **Confirmed in Matsuura Report 4 (2011), printed pp. 8, 42–45:** the seal was picked up on the shore at Kōzaki by an islander in 1974; it was not found in a dig. One side of the knob is incised 「中書礼部至元十四年九月造」, made by the Ministry of Rites of the Central Secretariat in the ninth month of 至元14 (1277). The other side reads 「□軍□把□」. It weighs 726 g and its face is in Phags-pa script. Drawn as 第15・16図 and photographed as 図版4 and 図版25. A 2001 celadon bowl inked 「王百戸」 also came from Kōzaki (printed p. 50). **I could not find any image of the Xiangyang counterweight trebuchet made in 1250–1300.** The *Yuanshi* biographies of ʿAlāʾ al-Dīn and Ismāʿīl are text, compiled 1369–70 (from memory). Chevedden dates the engine to 1272, not 1273 ([medievalists.net listing](https://www.medievalists.net/2010/09/the-invention-of-the-counterweight-trebuchet-a-study-in-cultural-diffusion/)).

| Rank | Source | (a) What, holder, URL | (b) Why in window | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Takashima underwater site reports | Nagasaki Prefecture Buried Cultural Properties Center Report 25 (2018, **NEW**); Matsuura City Report 12 (2023, **NEW**); Matsuura City Report 4 (summary volume); Takashima Town Report 1 (1993). **THE source for G2 kit (PDF opened and read, 427 pp., text layer):** record [62589](https://sitereports.nabunken.go.jp/en/62589), 松浦市鷹島海底遺跡 総集編, Matsuura City Report 4 (2011), the summary volume of all excavations to 2011. It publishes the 2001–02 Kōzaki rescue finds:
- **Iron helmets (鉄製冑):** 11 or more examples. Scale drawings are 第83–86図 (printed pp. 135–138, 1/4). Photos are 図版19 (8 helmets) and 図版20 nos. 1–2 (printed pp. 399–400). X-ray and CT images of a deep bowl-shaped helmet (深鉢形冑, the "蒙古鉢" type) show the brow band, neck guard and the rivets for a crest fitting (printed p. 290).
- **Swords:** 第91–95図 (pp. 143–148), and photos in 図版20–21. A scabbard is 図版22-1.
- **Arrows:** arrow bundles (矢束, some in a lacquered quiver) are 第87–90図 (pp. 139–143).
- **Crossbows and bows:** crossbows are 第81–82図 (pp. 132–133); bows are 第96–97図 (p. 148), with a lacquer study of the bows on pp. 255–260.
- **Armour scales:** red-lacquered armour scales (朱漆小札) appear on p. 256 and p. 347.
- **Bombs (てつはう):** 第79–80図 (pp. 130–131) and 図版18.
- **The 1277 seal:** see above.
Find numbers (e.g. KZK02 No.597) are given for each object. An English summary is on p. 373 (PDF p. 386). Files: four PDFs, the main one 27 MB. The others are fold-out maps. Other record: [46559](https://sitereports.nabunken.go.jp/en/46559), 松浦市鷹島海底遺跡: 平成13・14年度鷹島町神崎港改修工事に伴う緊急調査報告書, Matsuura City Report 2 (2008), ed. 池田榮史, 山本信夫, 中田敦之, 松尾昭子. It covers the rescue digs of 17 Aug–25 Oct 2001 and 11 Jul–7 Dec 2002. Main finds listed: 船材, てつはう, **鉄刀**, **箭**, 銅銭, 碇石, 陶磁器, 木製品, 磚, 青銅製品, 縄, 鉄製品. The direct PDF is 22.9 MB ([PDF](https://sitereports.nabunken.go.jp/files/attach/34/34008/46559_1_%E6%9D%BE%E6%B5%A6%E5%B8%82%E9%B7%B9%E5%B3%B6%E6%B5%B7%E5%BA%95%E9%81%BA%E8%B7%A1.pdf)). PDF opened: 309 pp. Its text layer is poor OCR, so search by eye, not by keyword. This is the primary report on the same 2001–02 finds that Report 4 summarises, and it adds colour photo plates. 図版1–45 run from PDF p. 255. **図版30 onward (PDF pp. 284–293) show the iron objects, swords and a helmet photographed in place on the seabed and after lifting, with arrow bundles, lacquered pieces and red-lacquered armour scales.** Use these for colour and condition. Report 4 is better for drawings. Record [131601](https://sitereports.nabunken.go.jp/en/131601) (PDF opened, 14 pp.) is Matsuura Report 12 (2023, **NEW**). It covers the 2022 dig of a one-stone wooden anchor (一石型木製椗) with 3D imaging: ship gear, not arms. Record [21714](https://sitereports.nabunken.go.jp/en/21714) is Nagasaki Prefecture Report 25 (2018, **NEW**), 平成25年度から平成29年度までの調査成果, by 寺田正剛, 古澤義久, 林田憲三, 滝野義幸 and 片多雅樹, DOI 10.24484/sitereports.21714. The PDF was opened and read: 99 pp., with a text layer. It reports a diving and sonar survey of 2013–2017. Its finds are brick (磚), ceramics, stone shot (石弾) and anchor stones. **It has no plates of helmets, swords or armour.** It mentions 甲冑 and 武器 only in passing (printed p. 10), and says on printed p. 49 that the 2000–2002 Kōzaki rescue digs produced てつはう and many weapons, which points to record 46559. It does carry 3D photogrammetry of the Takashima No. 2 wreck (第1図, printed p. 1) and the sonar records of wrecks 1 and 2 (第48・50図, printed p. 82). For the trebuchet, see row 6. Other records: [62589](https://sitereports.nabunken.go.jp/62589), [131601](https://sitereports.nabunken.go.jp/131601) (all three returned HTTP 429; not opened); [62578](https://sitereports.nabunken.go.jp/62578) (opened: 鷹島海底遺跡 8, Takashima Town Report 7, ed. 小川光彦, 松尾昭子, 林田憲三, 2002; frequent terms 小札, 帯金具, 球状土製品, 船材, but no 冑, 刀 or 印, and no plate pages). Also the [KAKEN 23222002 final report PDF](https://kaken.nii.ac.jp/file/KAKENHI-PROJECT-23222002/23222002seika.pdf) (opened: the 2016 研究成果報告書, listing four project volumes of 2013–2016, ed. 池田栄史; it mentions 磚, ceramics and てつはう, but names no helmet or sword plates) | Dated by the typhoon of 1281 that destroyed the Kōan invasion fleet. KOSUWA reported a helmet and red leather armour scraps ([Archaeology 2003](https://archive.archaeology.org/0301/etc/kamikaze.html)) | Direct PDF. The site has an API, but bot access was not tested | 鷹島海底遺跡, 元寇, 冑, 刀剣, てつはう, 管軍総把印, 蒙古襲来 | Many objects are corroded concretions, shown as X-ray or CT images. I did not confirm which report has the helmet and sword plates. No inventory numbers | Opened and confirmed (record 62589's PDF: helmets, swords, bows, crossbows, arrows, scales and the 1277 seal; also record 21714's PDF, record 62578 and the KAKEN report) |
| 2 | Mōko Shūrai Ekotoba, the original | Museum of the Imperial Collections, Sannomaru Shōzōkan (National Treasure, 2021, from memory). Not opened | Suenaga's text is dated 1293 (from memory). Conlan says only that the scrolls were made between the invasions and Suenaga's death in the 1320s ([Conlan, "Myth, Memory…", direct PDF](https://tconlan.scholar.princeton.edu/sites/g/files/toruqf3991/files/tconlan/files/conlan_myth_memory_.pdf), opened, 20 pp., text layer). Shows Mongol and Korean lamellar coats, helmets, bows, shields and the bomb | Viewer only; licence unknown; no IIIF known | 蒙古襲来絵詞 宮内庁 三の丸尚蔵館 | **Later additions, confirmed from Conlan:** five Mongol figures were painted in after 1709, probably in the mid-18th c. by the Tsuda family (Matsumoto Aya's finding). These are the three large Mongols with winged helmets, short robes and black boots beside the exploding *teppō* in the scene where Suenaga is thrown from his horse, plus two in scroll 2 (one on a ship's rail, one red-robed commander). The *teppō* explosion and a tree near Suenaga's horse were added too, and Suenaga's face was redrawn. **Don't use these five figures for kit.** Use the "dull brown" lamellar of the fleeing Mongols on foot, the shields and gongs of the 1274 encampment, and the scroll-2 boarding scenes | Opened and confirmed (Conlan PDF); from memory (the 1293 date and the National Treasure listing) |
| 3 | Kyushu University copy of the Ekotoba | Kyushu University Library, call no. 726/モ/1, 2 scrolls — [hdl 2324/411726](https://hdl.handle.net/2324/411726); IIIF manifest `https://catalog.lib.kyushu-u.ac.jp/image/manifest_custom/1/820/411726.json` (IIIF Presentation 3, 94 canvases); Public Domain | The full composition, reusable without application. Some canvases are 9823 × 7825 px; the long scroll canvases run up to 28540 × 1554 px ([library notice](https://www.lib.kyushu-u.ac.jp/en/news/21444)) | Open IIIF | 蒙古襲来絵詞, 模本 | **A late-Edo copy** of the version then held at Aso Shrine, copied after the additions were made. The manifest confirms the Aso source (肥後国阿蘇宮蔵画巻物寫) but does not state the copy's date. Use it to navigate, then check details against the original | Opened and confirmed |
| 4 | Mongol-period burials in open-access Russian journals | Karasuyr cemetery, Ulytau, radiocarbon-dated late 13th–early 14th c., with laminar armour fragments and arrowheads ([IAET abstract](https://archaeology.nsc.ru/en/publications/jr-aeae-en/18-46-2/annot-12/), 2018, **NEW**). Yashil, northern Mongolia: 7 armour plates X-rayed ([PDF](https://journal.archaeology.nsc.ru/jour/article/download/358/490), 2024, **NEW**). Kharabchi bracers, mostly 14th c. ([PDF](https://www.universum-humanitarium.ru/jour/article/download/61/60)) | Burials dated by radiocarbon or coins, with plates of armour, bows and stirrups | Open-access PDFs (DOAJ) | доспех монгольского времени, панцирные пластины, курган золотоордынского времени, налучье; Mongolian: хуяг, дуулга, сэлэм, нум | Most items are labelled only "13th–14th c."; the date must come from the specific grave | Found in a catalogue or citation |
| 5 | Hermitage Golden Horde finds (helmets, saddle mounts) | State Hermitage. Not opened | Dated by context and coins | Viewer only; no open API found | Золотая Орда, шлем, Эрмитаж | Many items are "13th–14th c."; the Chingul kurgan is pre-1240 (from memory) | From memory |
| 6a | **Stone shot for the trebuchet:** 古澤義久, chapter III of Nagasaki Pref. Report 25 (2018, **NEW**; record 21714, PDF opened) | Printed pp. 41–47 (PDF pp. 51–57). Takashima stone shot is compared with dated Yuan stone balls from **Shangdu** (元上都, including Torii Ryūzō's material), Dadu/Beijing sites and Penglai ship No. 3. Furusawa concludes they are the same class of trebuchet shot (抛石機の石弾). Takano's three Takashima classes: c. 8 cm/800 g, c. 11 cm/1.7 kg, c. 15 cm/3 kg+. Figures 20–23 are drawings and size/weight plots, and 巻頭図版4 is a photo of a stone shot raised in 2015. The text also says the 回回砲 (= 襄陽砲) was used against Xiangyang–Fancheng in 至元11 (1274), citing 劉旭 1986. That conflicts with the usual 1273 date, so check it | Takashima is dated by the 1281 fleet; Shangdu by its 1260–1358 occupation | Direct PDF (the site rate-limits scripts; download by hand) | 石弾, 石球, 抛石機, 回回砲, 襄陽砲, 元上都 | Ammunition only, no engine. Some small Shangdu balls come from buildings and may not be shot | Opened and confirmed |
| 6c | **Analogue for the engines: "Trabucos" at the siege of Savona (1227)**, Annales Ianuenses, BnF lat. 10136, Gallica `btv1b525197582`, PDF pp. 289–290 | Genoese drawings, c. 1227–1230s, of two labelled trestle-framed trebuchets beside striped round tents | Dated by the annal entry; Haug dates the drawings to the 1230s at the latest | Gallica PDF/IIIF (blocked to scripts; download by hand) | Trabucos, Saona, Saonenses | Western, about 45 years before Xiangyang. The beams and counterweights are only partly drawn. Gallica reuse is free for non-commercial and academic use; commercial use needs a paid licence (PDF cover page) | Opened and confirmed |
| 6b | Chevedden 2000, and the *Yuanshi* on the Xiangyang engine (囘囘砲 / 襄陽砲) | *DOP* 54: 71–116, doi:10.2307/1291833. *Yuanshi* on ctext.org (not opened) | Text dating of the 1272/1273 engine; no image | JSTOR paywalled; DOP back issues may be free on doaks.org (not checked) | 阿老瓦丁, 亦思马因, 囘囘砲, 襄陽 | Text only. No in-window image of the trebuchet was found | Found in a catalogue or citation |

Not to use: an archive.org PDF of Sasaki's 2015 book exists, but its authorisation is doubtful. His 2009 thesis is the better route ([TDL record](https://tdl-ir.tdl.org/handle/1969.1/ETD-TAMU-3100), opened and confirmed for title and date, issued 2009-05-15; the record does not confirm plates). It may not be free: the record shows no public file and carries "embargo" and "restricted" strings. The Ulaanbaatar Military History Museum "13th-century bow" is a copy with no provenance on its label ([frauenadler gallery](https://www.frauenadler.com/galleries/mongolian-arms-and-armor/archery-artifacts-in-mongolian-museums/), opened and confirmed; this is a hobbyist site).

## G3 — court dress is attributed, halls survive only as plans

No source turned up a G3 image that is both firmly dated inside 1260–1295 and free to script. Describe the NPM leaves as "attributed c. 1294, possibly Anige", never as "dated 1294". There is no period picture of an interior.

| Rank | Source | (a) What, holder, URL | (b) Why in window | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Yuan emperor and empress half-length portrait albums | NPM Taipei. Khubilai leaf: open-data item [15489](https://digitalarchive.npm.gov.tw/opendata/Pub/Detail/15489?dep=P&mode=full), 中畫000324N000000003 (作品號 中畫00032400003), painting 59.2 × 47.4 cm on silk, facing leaf 59.1 × 47.8 cm. Chabi leaf: item [15495](https://digitalarchive.npm.gov.tw/opendata/Pub/Detail/15495?dep=P&mode=full), 中畫000325N000000001 (作品號 中畫00032500001), inscribed 世祖皇帝后徹伯爾, 61.2 × 47.6 cm on silk. 故宮書畫錄 卷七 冊4 pp. 46–50 and 50–53. Platform: [NPM Open Data](https://digitalarchive.npm.gov.tw/opendata) | Court dress: Khubilai's white robe and hat, and Chabi's *gugu* headdress. The c. 1294 date (posthumous, possibly Anige) rests on attribution only: the item pages give "元代" and no date field. They cite 陳韻如 in 《大汗的世紀》 (NPM 2001), p. 288, and 故宮文物月刊 223 (2001), pp. 9–11 | Open data: 1 MP images are CC0, 6 MP images are CC BY 4.0 (confirmed on both item pages). Item pattern `/opendata/Pub/Detail/{id}?dep=P&mode=full`; search is a JSON POST to `/opendata/Pub/Search` (terms in `SearchContent`); images from `/opendata/Image/GetImage?imageId=…` | 元世祖, 察必, 元代帝半身像, 元代后半身像, 中-畫-000324; filter 朝代 = 元 | No inscribed date or signature. Bust-length only. Remounted under Qianlong, 1747–49 ([NPM monthly 455](https://www.npm.edu.tw/NewChineseArtDownload.ashx?bid=4252)). The UW teaching page gives different dimensions for the Chabi leaf | Opened and confirmed (the platform and both item pages) |
| 2 | UNESCO nomination file 1389, *Site of Xanadu* | China, State Party dossier, received by the World Heritage Centre on 20 January 2011 per ICOMOS (390 MB; inscribed 2012), plus the ICOMOS evaluation and maps — [documents page](https://whc.unesco.org/en/list/1389/documents), [document 152541](https://whc.unesco.org/document/152541); direct file `https://whc.unesco.org/uploads/nominations/1389.pdf` | Shangdu was founded in 1256 and used as Khubilai's summer capital. Its palace platforms date by construction history | Direct PDF, but **blocked to scripts (403)**. Download by hand | 元上都遗址, 穆清阁, 大安阁, 宫城; "Site of Xanadu" | Ruins and plans only; the hall names are from memory | Found in a catalogue or citation |
| 3 | Jade wine jar 瀆山大玉海 (Dushan dayuhai) | In situ, Yuweng pavilion, Tuancheng, Beihai Park. No museum record found. The *Yuanshi* entry is quoted in a [Sohu article](https://m.sohu.com/a/276852856_708264/) | The only surviving Green Mount object with a reign-year date in a primary text: finished Zhiyuan 2 (1265), placed in the Guanghan Hall on Qionghua island, used at banquets | No open scholarly image found | 瀆山大玉海, 玉瓮, 廣寒殿, 瓊華島, 至元二年 | Qianlong's re-cutting of the surface (from memory, unverified). Use it for form and scale only | Found in a catalogue or citation |
| 4 | Nancy Steinhardt's plans of Dadu and Shangdu | "The Plan of Khubilai Khan's Imperial City", *Artibus Asiae* 44.2/3 (1983), from p. 137, doi:10.2307/3249595 — cited in [Acta Mongolica](https://journal.num.edu.mn/actamongolica/issue/download/445/261); *Yuan: Chinese Architecture in a Mongol Empire* (2024, **NEW**) — [Princeton UP](https://press.princeton.edu/node/59535) | Hall plans (大明殿, 延春閣) and the Taiye pond layout, drawn from 《輟耕錄·宮闕制度》 and excavation | Paywalled | Khanbaliq, Daidu, Taiye chi, Qionghua | These are modern reconstructions; use them as constraints on layout | Found in a catalogue or citation |
| 5 | Watt et al., *The World of Khubilai Khan* (Met 2010) | 360 pp., 407 illustrations — [MetPublications](https://www.metmuseum.org/met-publications/the-world-of-khubilai-khan-chinese-art-in-the-yuan-dynasty) (blocked). **Readable on [Google Books](https://books.google.com.co/books?id=nCIPD1V39QkC)** (opened 2026-11-13): page images "shown with permission of the Metropolitan Museum of Art", searchable, deep pages such as p. 150 display. Viewer only, no PDF. In-book search hits: Shangdu ×10 (pp. x, xv, 5, 49, 71–73, 310…), Dadu ×10, Zhiyuan ×6 (pp. 38, 41, 55, 332–3, 340), "jade wine bowl" ×5 (pp. 49, 296, 328, 332, 338), Chabi ×10 (incl. p. 82 on her *gugu* headdress). **In-window dated anchor, p. 16 (figs. 25–26):** stone sculptures, a horse on clouds and a recumbent dog, excavated in 1998 from the tomb of **Yelü Zhu (1221–1285)** and his wife (d. 1285), Beijing, now in the Capital Museum. Yelü Zhu was Yelü Chucai's son and served at Khubilai's court. Also p. 34: a tomb dated 1247 | Steinhardt's chapter on the capitals, Dadu finds, court textiles and silver | No free PDF found; the Met blocks scripts (429 again on recheck). Open Library gives the Met / Yale UP imprint and 342 pp. | — | May be view-only; most objects are labelled only "Yuan" | Found in a catalogue or citation |
| 6 | Dated Yuan tomb murals: Pucheng Dongercun (1269), Chifeng Yuanbaoshan | *Kaogu yu wenwu* c. 2000; *Wenwu* 1983 (both from memory). No online record found | Pucheng is said to carry an ink date of Zhiyuan 6 (1269) and shows a Mongol couple at a table with vessels | CNKI, paywalled | 蒲城 洞耳村 元墓, 元寶山 元墓 壁畫, 夫婦對坐 宴飲圖 | Provincial, not court; the date and citations are unverified | From memory |

## G4 — Genoese drawings stop c. 1230 and Venetian ships rest on contracts

No candidate holds a firmly dated image of Venetian or Genoese people or ships inside 1260–1300. For a ship of c. 1270, the reliable basis is documentary: Pryor's reconstruction from Louis IX's 1246–1269 contracts with Genoa and Venice (*The Mariner's Mirror* 70 (1984): 171–219, 275–292, 363–386, confirmed in Crossref; first found via [weaponsandwarfare.com](https://weaponsandwarfare.com/?p=3116), a low-grade aggregator). The Boccalama galley, probably sunk in the early 1300s and now reburied, has no scientific date ([Scientific American](https://www.scientificamerican.com/article/secrets-from-venices-lago/)). For Ayas there is no period image.

| Rank | Source | (a) What, holder, URL | (b) Why in window | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Annales Ianuenses, BnF ms. lat. 10136 | **Gallica ARK found: `btv1b525197582`** (user download, "Annales de Gênes, par Cafaro. 1101-1300", 394-page PDF, images only). **I scanned every page.** The drawings sit on PDF pp. 7–39 and 215–234, with one more at p. 287 and a siege scene on pp. 289–290:
- **Civic room:** p. 231 is a gold-ground miniature of Genoese consuls seated in council under a double arcade, beside a 1190s entry.
- **Armed men and a demolition:** p. 224 shows a mounted official with a mace, spearmen with kite shields, and men pulling down an arcaded house, beside the entry on the podestà Manegoldus.
- **Marginal figures:** pp. 218–223 have figures of the 1180s, including a death-bed scene.
- **A knight:** p. 287 shows a knight with lion heraldry, beside the 1227 entry.
- **The siege of Savona, 1227:** pp. 289–290. The red labels name **Saona** (the walled town), two trestle-framed engines marked **"Trabucos"**, a banner marked "vexillum", striped round tents, and the **Saonenses** submitting in a pavilion.
**I saw no ship drawing in the thumbnail scan.** Earlier: no Gallica ARK was found (an Archives et manuscrits search for "Latin 10136" gave no result). Shelfmark per [Haug 2016 front matter](https://content.e-bookshelf.de/media/reading/L-4237396-47cf0890f7.pdf) (opened) | 116 drawings and miniatures ("insgesamt 116 unterschiedliche Bilder"; Kat. Nr. 1 = fol. 1r), added "from the mid-12th century to the 1230s" (Haug, p. 15). The *Art Bulletin* cites fols. 110r and 116r ([Art Bulletin 2015](https://www.tandfonline.com/doi/full/10.1080/00043079.2015.1009318), snippet) | Viewer only; **Gallica is blocked**. A phototype facsimile was printed in 1899 (Haug, n. 5; 1890 is Belgrano's *Annali Genovesi* edition) | "Latin 10136", "Annales Ianuenses", "Caffaro"; Haug's Kat. Nr. give the folios | About 30 years before the window. Ship drawings are not confirmed. The 1270–1294 section appears not to be illustrated | Found in a catalogue or citation |
| 2 | Carte Pisane, BnF GE B-1118 (RES) | Gallica ARK `btv1b52503226n` ([CNRS Images](https://images.cnrs.fr/en/video/6873)); [BnF notice cb406673515](https://catalogue.bnf.fr/ark:/12148/cb406673515), which links that ark and gives "[Gênes?], [ca 1270]", 48 × 103 cm | The parchment is radiocarbon-dated 1170–1270 and the content is not before c. 1265 ([MEDEA-CHART](https://medea-chart.wixsite.com/medea-chart/single-post/chart-of-the-week-carte-pisane-anonymous-circa-1270), opened). Pujades argues for a late-14th-c. date ([maphistory.info](https://www.maphistory.info/CartePisaneTEXT.html)) | Viewer only; **Gallica is blocked** | "Carte Pisane", "GE B-1118"; "Laiazzo / Lajazzo / Aiazzo / Layas" | No ships, figures or vignettes (the notice records "Aucune décoration" apart from a red cross). Ayas is not confirmed on the chart: the notice lists no place-names. The date is disputed | Found in a catalogue or citation |
| 3 | Vesconte atlas for Sanudo, BAV Pal. lat. 1362 A | [Heidelberg digi](https://digi.ub.uni-heidelberg.de/diglit/bav_pal_lat_1362a), dated "1320" | Signed by Vesconte; the eastern sheets should show Cilicia and Laiazzo | IIIF and download normally (from memory); **Heidelberg is blocked** | "Pal. lat. 1362 A", "Vesconte", "Laiazzo" | 20+ years late; Laiazzo and any vignettes are unverified | Found in a catalogue or citation |
| 4 | Venetian mariegole (statute books), following Lyle Humphrey's corpus 1260–1460 | Museo Correr, ASVe, Marciana; leaves dispersed. Humphrey (ed.), *La miniatura per le confraternite e le arti veneziane. Mariegole dal 1260 al 1460*, Cierre Edizioni, December 2015 ([Cini page](https://www.cini.it/en/?p=51517), **NEW**) | Founding dates and colophons; frontispieces of members (men, women, officers) before a saint | Mostly viewer only or undigitised; the Correr images are on paywalled Bridgeman ([example, 1385](https://www.bridgemanimages.com/en/noartistknown/miniature-from-the-wool-guild-corporation-mariegola-venice-manuscript-1385-italy-14th-century/nomedium/asset/765256)) | "mariegola", "capitolare", "scuola", "arte dei …", "Classe IV" | Most illuminated mariegole are 14th c.; no pre-1300 example was identified. The San Giovanni Evangelista leaf is in Cleveland (excluded) | Found in a catalogue or citation |
| 5 | Cocharelli treatise fragments, BL Add MS 27695 (+ 28841, Egerton 3127, 3781) | **Manifest opened, 2026-11-13:** [IIIF manifest](https://bl.digirati.io/iiif/ark:/81055/vdc_100165147237.0x000001) (opens to scripts, 51 canvases: ff. 1r–15v plus flyleaves). The usage terms read "Public Domain in most countries other than the UK". Viewer: [UV](https://uv-v4.netlify.app/#?manifest=https://bl.digirati.io/iiif/ark:/81055/vdc_100165147237.0x000001). I checked every folio:
- **f. 5r: harbour and siege scene.** A walled city with arcaded palace, red-roofed houses and a gate; oared galleys flying cross banners; round ships with sails, castles and top-castles; a landing with ladders; cavalry.
- **f. 8r: counting house.** Upper register: men counting coins at a plank table, a studded strongbox and chests, and a seated official in red. Lower register: two clerks in blue writing in ledgers at a carpeted table, with women, children and men waiting. This is the best image in the report for merchants, notaries, women and a business room.
- **Merchants and townspeople** in Genoese dress: ff. 2v, 3v, 4r, 9v and 11v.
- **Other scenes:** a group at table (f. 12r), a feast (f. 13r), a wine cellar with barrels (f. 14r) and a tent or pavilion (f. 15r).
**Date c. 1330–40**, so about 40–60 years after the window. Earlier notes:  [BL record](https://searcharchives.bl.uk/catalog/040-002031109); dating discussed in [Concina & Faunce, Medioevi 2020](https://iris.univr.it/retrieve/93a524a5-7171-414f-914e-b3bb1b580d30/Concina_Faunce%20Estratto%20Medioevi%206_2020.pdf) (**NEW**; not opened). Facsimile 2025 (**NEW**) | The richest Genoese source for dress, merchants and families | Now digitised: the BL record links a Universal Viewer with manifest `https://bl.digirati.io/iiif/ark:/81055/vdc_100165147237.0x000001` (manifest not opened) | "Cocharelli", "Add MS 27695" | c. 1330–1340 per the BL record (15 leaves of 27 surviving), and the date is debated | Found in a catalogue or citation |
| 6 | Ayas/Laiazzo site documentation | **[CHARLVAR Album 227 "Ay I"](https://charlvarchive.org/Album/227) (opened 2026-11-13): 29 colour transparencies by Robert W. Edwards, 1974, each captioned.** They show the fortified medieval harbour / Land Castle (Ay I.2–4, Towers A–B); the medieval town east of it (I.5–6); the foundations of a medieval bridge about 500 m north (I.9); the Island Castle with Chambers A and D, Tower A, Undercroft B, Salient B and the west wall (I.17–26); and the Sultan Süleyman Tower about 1.2 km west (I.11–16). The page says "Copyright © 2019 The Christian Architecture of the Levant", so reuse needs permission; describing in words is fine. Earlier notes:  [CHARLVAR site 76, Edwards survey photographs 1974–81](https://charlvarchive.org/Site/76) (albums include "Ay" site plans and "Ay I", 29 colour transparencies of 1974, by Robert W. Edwards); Erdal Eser, "From the Roman Settlement of Aigai to Ayas", *Vjesnik Arheološkog muzeja u Zagrebu* 3rd ser. XLII (2009): 421–441, PDF on [hrcak 95082](https://hrcak.srce.hr/file/95082), with Sea Castle excavation areas A and B | Modern photographs and plans of the 13th-c. harbour towers, mole, and sea and land castles | Open web pages; direct PDF | "Ayas", "Yumurtalık", "Laiazzo", "Kız Kalesi", "kazı" | Not period images; no licence statement appears on the CHARLVAR page | Opened and confirmed (the licence is unconfirmed) |

For the Cilician hinterland, the free *Treasures from the Ark* PDF (see P2) is the scriptable route. Nersessian's catalogue is a 2001 British Library / Getty publication.

## G5 — Singhasari Java is reachable, the ships are not

The strongest in-window material is Javanese. The Dutch Colonial Collections Committee's 2023 advice (opened and confirmed) dates the Singasari statues to the late 13th century and ties the temple to Kertanegara, who ruled from 1268 until his death in 1292 ([CKC advice I-2023-3](https://zoek.officielebekendmakingen.nl/blg-1100343.pdf)). **I could not find a good in-window source for ships** of the Gulf, India or Southeast Asia. Every ship image found was too early (hero stones, the Java Sea wreck) or too late (Shinan, 1323). **I could not find a good source for pearl diving, Adam's Peak or the Pandya coast.** No Pandya searches were run before the rate limit.

| Rank | Source | (a) What, holder, URL | (b) Why in window | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Leiden University Libraries Digital Collections (OD / Kern / KITLV photographs) | [digitalcollections.universiteitleiden.nl](https://digitalcollections.universiteitleiden.nl/view/item/809238); OD photographs found in search. **Connection reset on every fetch** | The colonial archaeological service photographed the East Javanese temples c. 1901–1940s. Jago is traditionally Wisnuwardhana's (d. 1268) funerary temple (from memory) | Viewer and IIIF (from memory) | "Tjandi Djago", "Toempang", "Singasari", "Tjandi Djawi", "Pasei", "Samoedra", "OD-" | No Jago record surfaced. Jago's surviving fabric may date from the 1343 rebuilding | Found in a catalogue or citation (the holdings are from memory) |
| 2 | Wikimedia Commons, Category:Candi Jago | [Category:Candi Jago](https://commons.wikimedia.org/wiki/Category:Candi_Jago): about 10 Tropenmuseum scans (e.g. TMnr 60027346) and a modern series of numbered narrative reliefs (Tantri, Arjunawiwaha, Parthayajna) | Narrative reliefs showing dress, pavilions and landscape | Commons API; check each licence | "Candi Jago", "Candi Tumpang", "Toempang" | No ship relief found; same date risk as rank 1 | Opened and confirmed |
| 3 | Candi Singasari statues RV-1403-1622, -1623, -1624, -1681 (with -1680, -1682) | Wereldmuseum / NMVW (Leiden); [CKC advice 2023](https://zoek.officielebekendmakingen.nl/blg-1100343.pdf) (**NEW**). Repatriation pages: [Mahakala](https://repatriasi2024.historia.id/en/mahakala) | "Late 13th century" by dedication to Kertanagara | Wereldmuseum database: collectie.wereldmuseum.nl is a JavaScript-only app and returned no record text to scripts; licence unknown | "RV-1403-1622", "Singosari", "Tjandi Singasari" | Returned on 18 August 2023 and now in the Museum Nasional, Jakarta, per the Historia page (single source; not cross-checked against a Dutch government source), so records may change. Deities only, no coastal scenes | Opened and confirmed (the advice; the repatriation date, single source); the Wereldmuseum records are unconfirmed. **You saved images of all six (input/media/RV-1403-*.png), but they carry no record text, date or licence.** My reading of the figures, by iconography only: 1622 Durga slaying the buffalo demon; 1623 a bearded guardian with a club (Mahakala type); 1624 a standing guardian with patterned hip-cloth; 1680 Bhairava on a dog over skulls; 1681 Ganesha on a skull base; 1682 the bull Nandi. The file RV-1403-1622-1.png is also a Ganesha, so it may be 1681 mislabelled. **Useful for Singhasari court dress:** the guardians' patterned hip-cloths, sashes, armlets and jewellery, and the Nandi's decorated saddle-cloth |
| 4 | Ship hero stones, west coast of India | Tripati 2006, *IJNA* 35(1): 88–96 ([ICAR record](https://krishi.icar.gov.in/ohs-2.3.1/index.php/record/view/207167)); ASI Museum, Old Goa | Kadamba-era stones (c. 950–1300) showing ships; one Malcornem naval battle stone, c. 12th c. | Paywalled article; no image API | "naval hero stone", "viragal ship", "Malcornem", ವೀರಗಲ್ಲು | Dated stylistically; none is securely 1250–1300; the only dated stone is 1354 | Found in a catalogue or citation |
| 5 | Gravestone of Sultan al-Malik al-Salih, Samudra-Pasai (d. 1297) | In situ, Aceh. Lambourn 2008 (*JESHO* 51(2): 252–286) is cited as disputing Moquette's Cambay-import thesis ([scite](https://scite.ai/authors/elizabeth-lambourn-6v1zp)); that argument was not checked against the paper. A [Sketchfab model](https://sketchfab.com/3d-models/grave-of-malik-al-zahir-at-samudera-pasai-18415027a6684cb1bf74314529c4811c) shows the *successor's* grave (1326) | A dated in-window object (the AH 696 epitaph date is from memory) for the Pasai plate | No verified free image; colonial photographs are probably in Leiden (from memory) | "Malikussaleh", "Pasei grafsteen", "Moquette", "makam Sultan Malikussaleh" | No image confirmed; the Sketchfab model is the wrong grave | Found in a catalogue or citation |
| 6 | Java Sea Shipwreck | Field Museum, Chicago ([press release 2018](https://www.fieldmuseum.org/about/press/shipwreck-and-800-year-old-made-china-label-reveal-lost-history)); Niziolek 2015 in open-access *JIPA* 35, doi:10.7152/jipa.v35i0.14893 ([article](https://journals.lib.washington.edu/index.php/JIPA/article/view/14893/12501)) (**NEW**) | Cargo of a Southeast Asian trade ship | Open-access JIPA; no collection API | "Java Sea Shipwreck", "Jianning Fu" | **Pre-window**: AMS dates put it in the mid-to-late 12th c. ([Archaeology](https://archaeology.org/news/2018/05/16/18051-china-trade-ceramic/); Niziolek et al. 2018, *JAS: Reports* 19: 781–790). Little of the hull survives | Found in a catalogue or citation |

For the Gulf side, Burke's *Sheikh's House at Quseir al-Qadim* (2021, **NEW**; see P2) documents a dated 13th-century Red Sea port and is the best free 13th-c. port material found.

## G6 — the 1280 Qazwini is the only dated, open, in-window manuscript

| Rank | Source | (a) What, holder, URL | (b) Why in window | (c) Access | (d) Search terms | (e) Main risk | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | al-Qazwīnī, ʿAjāʾib al-makhlūqāt, BSB Cod.arab. 464 | Bayerische Staatsbibliothek — [DDB record](https://www.deutsche-digitale-bibliothek.de/item/BQHHGMBPMO4EDGXRUPFX7T4JDZYKKFRW); manifest `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00037026/manifest` (428 canvases); [Qalamos](https://qalamos.net/receive/DE12Book_manuscript_00003827) | Made at Wasit in 1280, during the author's lifetime; the oldest known copy, with over 400 miniatures and drawings. Figures, headgear, robes, animals | **Open IIIF**, tested and returning HTTP 200 | "Cod.arab. 464", "bsb00037026", عجائب المخلوقات, "Wāsiṭ 678"; use the canvas labels as folios | The record's date field reads "678 oder 778" (1279–1377), but the BSB description in the same manifest says "completed in 1280" with "more than 400 miniatures"; the description supports 1280. The Qalamos record did not connect on recheck. Iraqi, not Iranian. Cosmographic marvels, not bazaars. Retouching not checked | Opened and confirmed |
| 2 | Manāfiʿ-i ḥayavān, Morgan MS M.500 | [Morgan record](https://www.themorgan.org/manuscript/77363) (403 to scripts); [viewer](https://ica.themorgan.org/manuscript/thumbs/77363) (HTTP 200; 97 folio thumbnails, fol. 2r–84v, page views at `/manuscript/page/N/77363`); [bestiary.ca](https://bestiary.ca/manuscripts/manu2739.htm) | Maragha, 1297–98 or 1299–1300, with the colophon on fol. 84v; 103 miniatures; commissioned by Ghazan (catalogue text quoted on bestiary.ca). Camels, horses and Ilkhanid dress (folios from memory) | Viewer only; no IIIF (no manifest link in the viewer HTML) | "M.500", منافع حيوان, "Maragheh" | 2–5 years late. The viewer heading reads "1297-1298 or 1299-1300, and 19th century": a 19th- or early-20th-c. restoration repainted heavily and added miniatures on fols. 3v, 6v, 23v, 25v, 36r, 47v, 58v, 72v, 78r, 78v and 84r. Do not use those folios for plates | Opened and confirmed (the viewer); found in a catalogue or citation (colophon and miniature count) |
| 3 | Juvaynī, Tārīkh-i Jahāngushāy, BnF Suppl. persan 205 | [BnF archives ark cc33978s](https://archivesetmanuscrits.bnf.fr/ark:/12148/cc33978s) (now HTTP 200, full notice); Gallica [ark btv1b84149955](https://gallica.bnf.fr/ark:/12148/btv1b84149955), linked from the notice | Copy finished 4 Dhu l-Hijja 689 H = 8 December 1290 (f. 176v), copyist Rašīd al-Ḫwāfī. Double painted page on ff. 1v–2, contemporary with the copy, "perhaps Baghdad": 1v shows a groom holding a prince's horse; 2 shows a Mongol prince "[Abaqā ?]" standing beside Juvaynī, identified by inscription. Folio 1 has a šamsa. The notice cites Ettinghausen 1959 and Simpson 1982 | Digitised on Gallica, but **Gallica returns 403 to scripts** | "Supplément persan 205", تاریخ جهانگشای | Only the frontispiece is illustrated, and the faces are damaged. The sitter's identification is uncertain: the BnF notice itself marks the prince "[Abaqā ?]". Do not confuse it with Suppl. persan 2018 | Opened and confirmed (the BnF notice; the Gallica images not opened) |
| 4 | Takht-i Sulayman, Abaqa's summer palace (from 1270) | [SMB project 2023–25](https://www.smb.museum/en/museums-institutions/museum-fuer-islamische-kunst/collection-research/research-cooperation/summer-palace-takht-e-soleyman/) (**NEW**; Dec 2023 to Dec 2025, almost 5,000 objects from the 1959–78 DAI excavations, about 1,200 of them tile fragments, in Berlin); Naumann 1976 catalogue, 71 + 12 pp., [free PDF on AMAR](https://commons.library.stonybrook.edu/amar/303) ([direct PDF](https://commons.library.stonybrook.edu/cgi/viewcontent.cgi?article=1302&context=amar), 22.9 MB) | Dated by excavation context; some tiles may carry 1270s inscriptions (from memory) | Direct PDF (non-commercial); SMB Online viewer | "Takht-e Soleyman", تخت سلیمان, "Lüsterfliese", "lajvardina" | Fragmentary palace material, not town imagery. SMB results are not yet published | Opened and confirmed |
| 5 | Stein, *Serindia* (1921) and *Innermost Asia* (1928) | Digital Silk Road, NII / Toyo Bunko — [example page](https://dsr.nii.ac.jp/toyobunko/T-VIII-5-A-a-3/V-1/page/0005.html.en); BL Photo 392 prints ([BL record](https://searcharchives.bl.uk/catalog/041-003073427)) | **Terrain only**: Lop Nur, Charklik, Miran and the Wakhan, photographed 1906–16 | **Digital Silk Road blocked (403)**; "all rights reserved" | "Charklik", "Lop-nor", "Wakhan", "Sarikol"; 若羌, 罗布泊 | Not period images | Found in a catalogue or citation |
| 6 | Mogao Cave 465 murals | Dunhuang Academy; pigment study by Kogou et al. (Liang is fourth author), *Scientific Reports* 10 (2020): 19312, doi 10.1038/s41598-020-76457-9 (**NEW**; [NTU release](https://www.ntu.ac.uk/about-us/news/news-articles/2020/11/scientists-reveal-700-year-old-caves-hidden-secrets)) | The pigments "correspond best with the Mongol/Yuan period" | e-dunhuang not checked; the cave is restricted | 莫高窟 第465窟, 敦煌 元代 | Contested dating; esoteric Buddhist subjects. The paper's focus on Cave 465 was not checked against its abstract | Found in a catalogue or citation |

**I could not find a good source for Badakhshan mining.** Sar-i Sang, Kuh-i Lal and the silver mines have no known period image. The substitutes are John Wood's 1838 visit, which is text only ([Mindat excerpt](https://zh.mindat.org/article.php/110/Mining+Lapis+in+1838)), and modern photographs in Wyart, Bariand, Filippi and Stockton 1981, *Gems & Gemology* 17(4): 184–190, doi:10.5741/GEMS.17.4.184 ([GIA PDF](https://www.gia.edu/doc/Lapis-Lazuli-from-Sar-E-Sang-Badakhshan-Afghanistan.pdf), not opened). Kleiss's *Karawanenbauten in Iran* has measured plans of Ilkhanid caravanserais, but no free PDF was found ([Zenon](https://zenon.dainst.org/Record/000922873)).

## P1 — ten scriptable collections not yet used

All ten were tested by curl on 2026-11-13. Only four have real numeric date filters: AIC, the V&A, the Getty and Europeana.

| # | Collection | API root / manifest pattern | Date filter | Status and caveat |
|---|---|---|---|---|
| 1 | Art Institute of Chicago | `https://api.artic.edu/api/v1/artworks/search`; manifest `https://api.artic.edu/api/v1/artworks/{id}/manifest.json` | `query[range][date_start][gte]=1250&...[lte]=1300` (use curl `-g`) | Opened and confirmed. **Send the header `AIC-User-Agent`**, or Cloudflare blocks the call. `q=Ilkhanid` gave 370 hits in the window ([API](https://api.artic.edu/api/v1/artworks/search?q=yuan)). Licence (from the API's `info.license_text`): data CC0 1.0, except the `description` field (CC BY 4.0); images flagged `is_public_domain` are open access |
| 2 | V&A Collections API v2 | `https://api.vam.ac.uk/v2/objects/search`; manifest `https://iiif.vam.ac.uk/collections/{systemNumber}/manifest.json` | `year_made_from` / `year_made_to` | Opened and confirmed. `q=mongol` gave 55 records ([manifest O120597](https://iiif.vam.ac.uk/collections/O120597/manifest.json)). Licence not CC0: free for non-commercial use only (API terms §9.1); commercial use needs V&A Images ([terms](https://www.vam.ac.uk/info/va-websites-terms-conditions)) |
| 3 | Getty Museum | SPARQL `https://data.getty.edu/museum/collection/sparql`; manifest `https://media.getty.edu/iiif/manifest/{2\|3}/{uuid}` | CIDOC-CRM P82a/P82b | Opened and confirmed. Holds the Zeyt'un Gospels (Ms. 59), Cilician ([manifest example](https://media.getty.edu/iiif/manifest/3/966ac161-01b1-45b9-8dd2-f727ff7b8d50)). Public-domain images are CC0 through the Open Content Program; Getty's own texts are CC BY 4.0 |
| 4 | Smithsonian Open Access | `https://api.si.edu/openaccess/api/v1.0/search?q=…&api_key=…` | Decades only | Opened, but DEMO_KEY hit its rate limit; Freer (NMAA) filtering is unresolved. Needs a free api.data.gov key ([API](https://api.si.edu/openaccess/api/v1.0/search?q=yuan+dynasty&api_key=DEMO_KEY)) |
| 5 | Europeana | `https://api.europeana.eu/record/v2/search.json`; manifest `https://iiif.europeana.eu/presentation/{dataset}/{localId}/manifest` | `qf=YEAR:[1250 TO 1300]` | Opened and confirmed (a Treviso statute of 1263). Low recall ([API](https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=mongol&rows=3)) |
| 6 | Yale LUX | `https://lux.collections.yale.edu/api/search/item?q={"text":"…"}` | Failed (CloudFront 403) | Opened for simple search only ([LUX](https://lux.collections.yale.edu/api/search/item?q=%7B%22text%22%3A%22yuan%22%7D)) |
| 7 | Vatican DigiVatLib | `https://digi.vatlib.it/iiif/MSS_{shelfmark}/manifest.json` | None | Opened, manifest only ([Vat.lat.3773](https://digi.vatlib.it/iiif/MSS_Vat.lat.3773/manifest.json)). Licence restrictive (confirmed): the manifest attribution reads "Images Copyright Biblioteca Apostolica Vaticana", with no licence field; online JPGs are watermarked; publication needs a paid professional-use licence, all rights reserved |
| 8 | BSB / MDZ | `https://api.digitale-sammlungen.de/iiif/presentation/v2/{bsbID}/manifest` | `navDate` in the manifest | Opened and confirmed; this is the route to Cod.arab. 464 |
| 9 | e-codices | `https://www.e-codices.unifr.ch/metadata/iiif/{ms-id}/manifest.json` | Century in the metadata | Opened, pattern test only ([csg-0390](https://www.e-codices.unifr.ch/metadata/iiif/csg-0390/manifest.json)). Licence set per library: non-commercial use is free, csg-0390 declares CC BY-NC 4.0, some libraries allow commercial use, and other commercial use needs permission |
| 10 | Minneapolis Institute of Art | `https://search.artsmia.org/{query}`; `/id/{id}` | Free text only | Opened; no image endpoint found ([search](https://search.artsmia.org/Yuan%20dynasty)) |

Other routes: NPM Taipei Open Data (see G3; no API documentation) and Kyushu University IIIF (see G2). Princeton Figgy works (`/concern/scanned_resources/{id}/manifest`) but holds mostly library material. Harvard needs an API key. The Bodleian manifest pattern was found only in documentation.

## P2 — ten free catalogue PDFs, strongest for G4–G6

Page counts come from pdfinfo, except rows 9–10, which use archive.org image counts. The Met originals on archive.org are image-only. Each has an OCR'd `_text.pdf` alongside. Their licence is undocumented, and they look like the Met's own free PDFs (an inference). The archive.org metadata, checked on 2026-11-13, shows all eight mirrors live, with no licence or rights field. The six Met items (rows 3, 5, 6, 7, 9, 10) were uploaded by the Internet Archive staff account kaplan@archive.org into `americana`, all on one day in 2014. That fits a bulk mirror of MetPublications PDFs, but the metadata does not name the source. Rows 4 (2021) and 8 (2020) are community uploads by private uploaders.

| # | Title | Download | Pages | Text layer | Gap |
|---|---|---|---|---|---|
| 1 | Burke, *The Sheikh's House at Quseir al-Qadim* (OIP 144), ISAC Chicago, 2021, **NEW** | [S3 PDF](https://isac-assets.s3.amazonaws.com/isac-publications/oip144.pdf) | 424 | Yes | G5 |
| 2 | Nersessian, *Treasures from the Ark*, BL/Getty, 2001 | [media.getty.edu](https://media.getty.edu/Text/25f2d39c-015d-589b-ab5b-eaabf0ea40fe.pdf) | 244 | Yes (OCR) | G4 |
| 3 | Watt & Wardwell, *When Silk Was Gold*, Met/Cleveland, 1997 | [original](https://archive.org/download/WhenSilkWasGoldCentralAsianandChineseTextiles/WhenSilkWasGoldCentralAsianandChineseTextiles.pdf) / [OCR](https://archive.org/download/WhenSilkWasGoldCentralAsianandChineseTextiles/WhenSilkWasGoldCentralAsianandChineseTextiles_text.pdf) | 250 | Original no; `_text.pdf` yes | G1–G3, G6 |
| 4 | Evans (ed.), *Byzantium: Faith and Power (1261–1557)*, Met, 2004 | [archive.org](https://archive.org/download/byzantium-faith-and-power-1261-1557/Byzantium_Faith_and_Power_1261_1557.pdf) | 682 | Original no; `_text.pdf` exists | G4 (community upload; may be withdrawn) |
| 5 | Buckton (ed.), *The Treasury of San Marco*, Met, 1984 | [archive.org](https://archive.org/download/TheTreasuryofSanMarcoVenice/TheTreasuryofSanMarcoVenice.pdf) | 355 | Original no; `_text.pdf` exists | G4 |
| 6 | Carboni, *Following the Stars*, Met, 1997 | [archive.org](https://archive.org/download/FollowingtheStarsImagesoftheZodiacinIslamicArt/FollowingtheStarsImagesoftheZodiacinIslamicArt.pdf) | 50 | Original no; `_text.pdf` exists | G6 |
| 7 | Carboni & Masuya, *Persian Tiles*, Met, 1993 | [archive.org](https://archive.org/download/PersianTiles/PersianTiles.pdf) | 50 | Original no; `_text.pdf` exists | G6 |
| 8 | Mathers & Flecker (eds), *Archaeological Recovery of the Java Sea Wreck*, 1997 | [archive.org](https://archive.org/download/mathers_flecker_1997_java_sea_wreck/mathers_flecker_1997_java_sea_wreck.pdf) | 204 | Yes | G5 (pre-window on the newer dating) |
| 9 | Kossak & Singer, *Sacred Visions*, Met, 1998 | [archive.org item](https://archive.org/details/SacredVisionsEarlyPaintingsfromCentralTibet) | 241 (image count) | `_text.pdf` listed | G3 (tangential) |
| 10 | Lerner, *The Flame and the Lotus*, Met, 1984 | [archive.org item](https://archive.org/details/TheFlameandtheLotusIndianandSoutheastAsianArtfromtheKronosCollections) | 193 (image count) | `_text.pdf` listed | G5 (tangential) |

Two more free PDFs turned up in the gap threads, with page counts not taken: Naumann's *Takht-i Suleiman* (1976; see G6) and the Takashima site reports (see G2). No free PDF was found for *The World of Khubilai Khan* (but it is readable page by page on Google Books with the Met's permission; see G3 row 5), NPM *Age of the Great Khan*, *Chinese Art under the Mongols*, *Venice and the Islamic World*, *Armenia: Art, Religion and Trade* (2018), or *Dschingis Khan und seine Erben*. The DAI Karakorum volumes are open access but behind a bot check.

## P3 — replicas rest on the wrong century; excavated finds carry the weight

Most well-dated evidence comes from excavated and conserved finds, not from reconstructions. Every Indian Ocean replica that has actually sailed rests on evidence centuries before 1290.

| Project / find | Real objects it rests on | Grade and caveat | Confidence |
|---|---|---|---|
| Takashima (KOSUWA; University of the Ryukyus) | The 1281 invasion-fleet wrecks: a helmet, red leather armour scraps, hull timbers ([Archaeology 2003](https://archive.archaeology.org/0301/etc/kamikaze.html); [KAKEN 18102004](https://kaken.nii.ac.jp/report/KAKENHI-PROJECT-18102004/18102004seika)) | A/B. Dated by the 1281 typhoon. **No reconstruction exists.** No inventory numbers found. The notes say "Ikeda Kenzo" merges Hayashida Kenzo and Ikeda Yoshifumi | Found in a catalogue or citation |
| M. V. Gorelik's armour plates | Samarkand lamellar plates (13th–14th c.), a Golden Horde burial near Yablonovsky, a falchion from a Kairka burial ([Gorelik PDF](https://aheku.net/f1jok/files/4473/Gorelik.pdf)) | B/C. Contested by Kubik 2020 ([Historia i Świat](https://czasopisma.uph.edu.pl/historiaswiat/article/download/1768/3116/6721), **NEW**) and Negin 2025 ([PDF](https://nav.jvolsu.com/index.php/en/component/attachments/download/630), **NEW**) | Found in a catalogue or citation |
| Mingshui robe | Onggut tomb at Dasujixiang Mingshui, Darhan Muminggan, excavated 1978, Inner Mongolia Museum; silk with gold brocade, 142 × 246 cm; dated "13th–14th c." ([UW Silk Road fig. 104](https://depts.washington.edu/silkroad/exhibit/mongols/fig_104.html)) | A/B, but no accession number. No reconstruction by Zhao Feng or the China National Silk Museum was found | Opened and confirmed |
| Abegg-Stiftung, "Mongol splendour" | A cloth-of-gold garment in the Abegg collection (Vogt, in Riggisberger Berichte 21, 2016, **NEW**; [review](https://journals.openedition.org/abstractairanica/43114)) | A/B; inventory number not found | Found in a catalogue or citation |
| Karakorum arrowheads | National Museum of Mongolian History, Inv. U.63-1-7, 13th–14th c., excavated 1949 ([frauenadler](https://www.frauenadler.com/galleries/mongolian-arms-and-armor/archery-artifacts-in-mongolian-museums/)) | B. The source is a hobbyist site reporting the museum captions | Opened and confirmed |
| Pryor's crusader transports | Louis IX's Genoese and Venetian contracts, 1246–1269 (Pryor in *The Mariner's Mirror*: 68 (1982): 9–27, 103–125; 70 (1984): 171–219, 275–292, 363–386; 76 (1990): 255–273; per Crossref) | A for dimensions, but documentary: drawings, not hulls | Found in a catalogue or citation |
| Boccalama galley | Venetian lagoon, exposed 2001 and reburied; probably early 1300s ([Scientific American](https://www.scientificamerican.com/article/secrets-from-venices-lago/)) | B. No radiocarbon or dendro date | Found in a catalogue or citation |
| Jewel of Muscat | The Belitung wreck, early 9th c.; only about 20% of the hull studied ([Aramco World](https://archive.aramcoworld.com/issue/201203/sailing.through.time.jewel.of.muscat.htm); Vosmer et al. 2011, [PSAS](https://www.archaeopresspublishing.com/ojs/index.php/PSAS/article/view/1705)) | A for its own period, C for 1290 | Found in a catalogue or citation |
| INSV Kaundinya (2025, **NEW**) | A line drawing of a 5th-c. Ajanta painting ([Arab News](https://www.arabnews.com/node/2628486/)) | C | Found in a catalogue or citation |
| Samudra Raksa (2003); Spirit of Majapahit (2016, **NEW**) | The 8th–9th c. Borobudur reliefs ([injourney](https://injourneydestination.id/en/experience/Ocean-Raksa-Ship-Museum/)) | C; D for Majapahit (the wrong ship type; the period ship was the *jong*) | Found in a catalogue or citation |
| Las Huelgas, Burgos | The garments of Fernando de la Cerda (d. 1275) | Right date, wrong region (Castile) | From memory |
| Quanzhou ship; Shinan wreck | A Song hull sunk c. 1270s; a wreck dated by a 1323 cargo tag | No replica found | From memory |

No ger-on-wagon reconstruction, Ilkhanid dress reconstruction, or Golden Horde textile conservation project was found.

## P4 — what to read first, per gap

| Gap | Read first | Free? |
|---|---|---|
| G1 | Rubruck, trans. Jackson & Morgan (Hakluyt, 1990, from memory); Andrews, *Felt Tents and Pavilions* (1999, from memory); Ghiasian 2018 on H.1654, *Iranian Studies* 51(3): 399–425 (**NEW**, [Cambridge Core](https://www.cambridge.org/core/product/D298994042B2643F0E25DAA747EA7E09)); Blair, *A Compendium of Chronicles* (1995) | Ghiasian: paywalled, not free. The rest are not free |
| G2 | Conlan, *In Little Need of Divine Intervention* (Cornell East Asia Series 113, 2001); Sasaki thesis 2009 ([TDL](https://tdl-ir.tdl.org/handle/1969.1/ETD-TAMU-3100)) and book 2015 (**NEW**, [MUSE](https://muse.jhu.edu/book/38210)); Ikeda Yoshifumi 2018 (**NEW**, from memory); Chevedden 2000; Needham & Yates, *SCC* 5.6 (1994, from memory); Gorelik (from memory); May 2007 (from memory) | None confirmed free. The Sasaki thesis record shows no public file and carries embargo strings; the 2015 book is "Open Access: No" on MUSE. Conlan's companion site is dead, and its Wayback copy (2018) is an unreadable Flash shell |
| G3 | Steinhardt 1983 and 2024 (**NEW**); Watt et al. 2010; NPM, 《南薰殿歷代帝后圖像》上冊 (2020, **NEW**); Jing Anning, "The Portraits of Khubilai Khan and Chabi by Anige", *Artibus Asiae* 54.1/2 (1994), doi:10.2307/3250079; McCausland, *The Mongol Century* (2014, **NEW**, from memory) | None confirmed free |
| G4 | Haug 2016 (**NEW**); Humphrey (ed.), *La miniatura per le confraternite e le arti veneziane. Mariegole dal 1260 al 1460* (Cierre, 2015, **NEW**); Pryor 1984/1988 (1984 confirmed in Crossref; from memory for 1988); Martin 2001; Balard, *La Romanie génoise* (1978); Edwards 1987; Hellenkemper 1976 (all from memory) | Haug: unknown. The V&R eLibrary returned 403 and the Crossref record has no licence |
| G5 | Tripati 2006; Lambourn 2008 (*JESHO* 51(2): 252–286); Agius 2008; Manguin 1980/1993; Hourani 1951/1995; Kieven 2013 (open access, doi:10.26530/oapen_613436); CKC 2023 (**NEW**, free) | The CKC advice is free (confirmed). Kieven is open access on OAPEN under CC BY-NC-ND 3.0 (confirmed) |
| G6 | Masuya 1997 dissertation (from memory); Huff 2006; Naumann 1976 (free); Kleiss 1996–; Blair on Ilkhanid manuscripts; Herrmann 1968 (from memory) | Only Naumann is confirmed free |

## Bibliography

The non-standard `% UNCERTAIN` lines sit outside the entries, so BibTeX ignores them. Manuscripts appear as `@misc`.

```bibtex
@book{haug2016annales,
  author = {Haug, Henrike},
  title = {Annales Ianuenses: Orte und Medien des historischen Ged{\"a}chtnisses im mittelalterlichen Genua},
  series = {Orbis mediaevalis}, volume = {15},
  publisher = {V\&R unipress}, address = {G{\"o}ttingen}, year = {2016},
  isbn = {978-3-8471-0499-5}, note = {NEW}
}

@mastersthesis{sasaki2009lostfleet,
  author = {Sasaki, Randall James},
  title = {The Origin of the Lost Fleet of the Mongol Empire},
  school = {Texas A\&M University}, year = {2009},
  url = {https://tdl-ir.tdl.org/handle/1969.1/ETD-TAMU-3100}
}

@book{sasaki2015lostfleet,
  author = {Sasaki, Randall J.},
  title = {The Origins of the Lost Fleet of the Mongol Empire},
  publisher = {Texas A\&M University Press}, year = {2015},
  isbn = {978-1-62349-194-9}, note = {NEW}
}

% UNCERTAIN: end page 116 not in Crossref
@book{matsuura2011takashima,
  author    = {{長崎県松浦市教育委員会}},
  title     = {松浦市鷹島海底遺跡 総集編},
  series    = {松浦市文化財調査報告書},
  number    = {4},
  publisher = {長崎県松浦市教育委員会},
  year      = {2011},
  url       = {https://sitereports.nabunken.go.jp/62589},
  note      = {Helmets: figs. 83--86, pp. 135--138, pls. 19--20; seal pp. 8, 42--45}
}
% UNCERTAIN: matsuura2011takashima: the record page gives the date 2011-09-16. No DOI is added; the 10.24484/sitereports.62589 pattern is unchecked.

@book{nagasaki2018takashima,
  author    = {{長崎県埋蔵文化財センター}},
  title     = {鷹島海底遺跡：平成25年度から平成29年度までの調査成果},
  series    = {長崎県埋蔵文化財センター調査報告書},
  number    = {25},
  publisher = {長崎県教育委員会},
  year      = {2018},
  doi       = {10.24484/sitereports.21714},
  url       = {https://sitereports.nabunken.go.jp/21714},
  note      = {Ch. III on stone shot by 古澤義久, printed pp. 41--47}
}

@article{chevedden2000trebuchet,
  author = {Chevedden, Paul E.},
  title = {The Invention of the Counterweight Trebuchet: A Study in Cultural Diffusion},
  journal = {Dumbarton Oaks Papers}, volume = {54}, year = {2000}, pages = {71--116},
  doi = {10.2307/1291833}
}

@book{franken2022halle,
  author = {Franken, Christina},
  title = {Die ``Gro{\ss}e Halle'' von Karakorum},
  series = {Forschungen zur Arch{\"a}ologie Au{\ss}ereurop{\"a}ischer Kulturen}, volume = {12},
  publisher = {Deutsches Arch{\"a}ologisches Institut}, year = {2022},
  doi = {10.34780/coic-cbqc}, note = {digital edition; NEW}
}

% UNCERTAIN: subtitle "Excavations in the Craftsmen Quarter at the Main Road" not in either record
@book{karakorum_vol1,
  editor = {Bemmann, Jan and Erdenebat, Ulambayar and Pohl, Ernst},
  title = {Mongolian-German Karakorum Expedition, Vol. 1: Excavations in the Craftsmen Quarter at the Main Road},
  series = {Forschungen zur Arch{\"a}ologie Au{\ss}ereurop{\"a}ischer Kulturen}, volume = {8},
  publisher = {Reichert}, address = {Wiesbaden}, year = {2010},
  isbn = {9783895006975}, doi = {10.34780/133a-8dr5},
  note = {DAI digital edition 2022}
}

@incollection{conlan2013myth,
  author    = {Conlan, Thomas D.},
  title     = {Myth, Memory, and the Scrolls of the Mongol Invasions of Japan},
  booktitle = {Archaism and Antiquarianism in Korean and Japanese Art},
  year      = {2013},
  pages     = {54--73},
  url       = {https://tconlan.scholar.princeton.edu/sites/g/files/toruqf3991/files/tconlan/files/conlan_myth_memory_.pdf}
}
% UNCERTAIN: conlan2013myth editor (Elizabeth Lillehoj) and publisher (Center for the Art of East Asia, Univ. of Chicago / Art Media Resources) are from memory. Pages are read from the PDF; the year comes from the PDF creation date (2013).

@article{testa2020moko,
  author  = {Testa, Giuseppina Aurora},
  title   = {``M{\=o}ko Sh{\=u}rai Ekotoba'' (Illustrated Account of the Mongol Invasions)},
  journal = {Eikon / Imago},
  volume  = {9},
  pages   = {35--57},
  year    = {2020},
  doi     = {10.5209/eiko.73275}
}

@book{conlan2001divine,
  author = {Conlan, Thomas D.},
  title = {In Little Need of Divine Intervention: Takezaki Suenaga's Scrolls of the Mongol Invasions of Japan},
  series = {Cornell East Asia Series}, number = {113},
  publisher = {East Asia Program, Cornell University}, address = {Ithaca, NY}, year = {2001},
  isbn = {1-885445-13-X}
}

% UNCERTAIN: end page 158 not in Crossref
@article{steinhardt1983plan,
  author = {Steinhardt, Nancy S.},
  title = {The Plan of Khubilai Khan's Imperial City},
  journal = {Artibus Asiae}, volume = {44}, number = {2/3}, year = {1983}, pages = {137--158},
  doi = {10.2307/3249595}
}

@book{steinhardt2024yuan,
  author = {Steinhardt, Nancy S.},
  title = {Yuan: Chinese Architecture in a Mongol Empire},
  publisher = {Princeton University Press}, year = {2024},
  doi = {10.1515/9780691253350}, note = {NEW}
}

@book{watt2010khubilai,
  author = {Watt, James C. Y. and others},
  title = {The World of Khubilai Khan: Chinese Art in the Yuan Dynasty},
  publisher = {Metropolitan Museum of Art and Yale University Press}, address = {New York and New Haven}, year = {2010},
  isbn = {978-1-58839-403-3}
}

@book{watt1997silk,
  author = {Watt, James C. Y. and Wardwell, Anne E.},
  title = {When Silk Was Gold: Central Asian and Chinese Textiles},
  publisher = {Metropolitan Museum of Art, in cooperation with the Cleveland Museum of Art},
  address = {New York}, year = {1997}
}

% UNCERTAIN: author field is the usual State Party convention; the dossier itself was not opened (year confirmed via ICOMOS)
@techreport{unesco2011xanadu,
  author = {{People's Republic of China}},
  title = {Site of Xanadu: Nomination File 1389},
  institution = {UNESCO World Heritage Centre}, year = {2011}, number = {1389},
  url = {https://whc.unesco.org/en/list/1389/documents}
}

@misc{ckc2023singasari,
  author = {{Commissie Koloniale Collecties}},
  title = {Advies I-2023-3: Vier beelden uit het tempelcomplex van Singasari},
  address = {The Hague}, year = {2023},
  url = {https://zoek.officielebekendmakingen.nl/blg-1100343.pdf}, note = {NEW}
}

@article{tripati2006hero,
  author = {Tripati, Sundaresh},
  title = {Ships on Hero Stones from the West Coast of India},
  journal = {International Journal of Nautical Archaeology},
  volume = {35}, number = {1}, year = {2006}, pages = {88--96},
  doi = {10.1111/j.1095-9270.2005.00081.x}
}

@article{lambourn2008tombstones,
  author = {Lambourn, Elizabeth},
  title = {Tombstones, Texts, and Typologies: Seeing Sources for the Early History of Islam in Southeast Asia},
  journal = {Journal of the Economic and Social History of the Orient},
  volume = {51}, number = {2}, year = {2008}, pages = {252--286},
  doi = {10.1163/156852008X307447}
}

@article{niziolek2018javasea,
  author = {Niziolek, Lisa C. and Feinman, Gary M. and Kimura, Jun and Respess, Amanda and Zhang, Lu},
  title = {Revisiting the Date of the Java Sea Shipwreck from Indonesia},
  journal = {Journal of Archaeological Science: Reports},
  volume = {19}, year = {2018}, pages = {781--790},
  doi = {10.1016/j.jasrep.2018.04.002}, note = {NEW}
}

@book{burke2021quseir,
  author = {Burke, K. S.},
  title = {The Sheikh's House at Quseir al-Qadim: Documenting a Thirteenth-Century Red Sea Port},
  series = {Oriental Institute Publications}, number = {144},
  publisher = {Oriental Institute (ISAC), University of Chicago}, year = {2021},
  isbn = {978-1-61491-056-5},
  url = {https://isac-assets.s3.amazonaws.com/isac-publications/oip144.pdf}, note = {NEW}
}

@book{nersessian2001ark,
  author = {Nersessian, V.},
  title = {Treasures from the Ark: 1700 Years of Armenian Christian Art},
  publisher = {British Library / J. Paul Getty Museum}, year = {2001}, isbn = {0-89236-639-7}
}

@misc{bsb_cod_arab_464,
  author = {{al-Qazw{\=\i}n{\=\i}, Zakar{\=\i}y{\=a} ibn Mu{\d h}ammad}},
  title = {Kit{\=a}b {\textquoteleft}Aj{\=a}{\textquoteright}ib al-makhl{\=u}q{\=a}t},
  howpublished = {Munich, Bayerische Staatsbibliothek, Cod.arab. 464; W{\=a}si{\d t}, 678 H/1280 (record also gives ``678 oder 778'')},
  url = {http://mdz-nbn-resolving.de/urn:nbn:de:bvb:12-bsb00037026-7}
}

@misc{morgan_m500,
  title = {Man{\=a}fi{\textquoteleft}-i {\d h}ayav{\=a}n},
  howpublished = {New York, Morgan Library \& Museum, MS M.500; Mar{\=a}gha, 1297--1298 or 1299--1300},
  url = {https://www.themorgan.org/manuscript/77363}
}

@misc{bnf_suppl_pers_205,
  author = {Juvayn{\=\i}, {\textquoteleft}A{\d t}{\=a}-Malik},
  title = {T{\=a}r{\=\i}kh-i Jah{\=a}ngush{\=a}y},
  howpublished = {Paris, BnF, Suppl{\'e}ment persan 205; dated 4 Dhu l-Hijja 689 H/8 December 1290},
  url = {https://archivesetmanuscrits.bnf.fr/ark:/12148/cc33978s},
  note = {Gallica ark:/12148/btv1b84149955}
}

@book{naumann1976takht,
  author = {Naumann, Rudolf},
  title = {Takht-i Suleiman: Ausgrabung des Deutschen Arch{\"a}ologischen Instituts in Iran. Ausstellung M{\"u}nchen 1976},
  publisher = {Pr{\"a}historische Staatssammlung}, address = {M{\"u}nchen}, year = {1976},
  series = {Ausstellungskataloge der Pr{\"a}historischen Staatssammlung}, volume = {3},
  url = {https://commons.library.stonybrook.edu/amar/303}
}

@incollection{huff2006takht,
  author = {Huff, Dietrich},
  title = {The Ilkhanid Palace at Takht-i Sulayman: Excavation Results},
  booktitle = {Beyond the Legacy of Genghis Khan}, editor = {Komaroff, Linda},
  publisher = {Brill}, address = {Leiden}, year = {2006}
}

@article{wyart1981lapis,
  author = {Wyart, Jean and Bariand, Pierre and Filippi, Jean and Stockton, Carol},
  title = {Lapis Lazuli from Sar-e-Sang, Badakhshan, Afghanistan},
  journal = {Gems \& Gemology}, volume = {17}, number = {4}, year = {1981}, pages = {184--190},
  doi = {10.5741/GEMS.17.4.184},
  url = {https://www.gia.edu/doc/Lapis-Lazuli-from-Sar-E-Sang-Badakhshan-Afghanistan.pdf}
}

@article{vosmer2011jewel,
  author = {Vosmer, Tom and Belfioretti, Luca and Staples, Eric and Ghidoni, Alessandro},
  title = {The ``Jewel of Muscat'' Project: Reconstructing an Early Ninth-Century {CE} Shipwreck},
  journal = {Proceedings of the Seminar for Arabian Studies}, volume = {41}, year = {2011}, pages = {411--425}
}

@book{fircks2016oriental,
  editor = {von Fircks, Juliane and Schorta, Regula},
  title = {Oriental Silks in Medieval Europe},
  series = {Riggisberger Berichte}, number = {21},
  publisher = {Abegg-Stiftung}, address = {Riggisberg}, year = {2016}, note = {NEW}
}

@article{pryor1984crusader,
  author = {Pryor, John H.},
  title = {The Naval Architecture of Crusader Transport Ships: A Reconstruction of Some Archetypes for Round-Hulled Sailing Ships},
  journal = {The Mariner's Mirror}, volume = {70}, number = {2--4}, year = {1984},
  pages = {171--219, 275--292, 363--386},
  doi = {10.1080/00253359.1984.10655967},
  note = {Parts I--III; DOIs of Parts II and III: 10.1080/00253359.1984.10655978, 10.1080/00253359.1984.10655992}
}

% UNCERTAIN: that the paper is specifically about Mogao Cave 465 was not checked against the abstract
@article{kogou2020mogao465,
  author = {Kogou, Sotiria and Shahtahmassebi, Golnaz and Lucian, Andrei and Liang, Haida and Shui, Biwen and Zhang, Wenyuan and Su, Bomin and van Schaik, Sam},
  title = {From Remote Sensing and Machine Learning to the History of the Silk Road: Large Scale Material Identification on Wall Paintings},
  journal = {Scientific Reports}, volume = {10}, pages = {19312}, year = {2020},
  doi = {10.1038/s41598-020-76457-9}, note = {NEW}
}
```

## Questions left unresolved

These points stay open, in rough order of value to the plates:

- **G1.** Whether H.1654 has a tent-on-wagon scene: Ghiasian 2018's abstract and references show none, and the body is paywalled.
- **G2.** (Settled: Matsuura Report 4 (2011, record 62589) carries the helmet, sword, bow, crossbow and arrow plates and confirms the seal's 至元十四年九月 (1277) date. See G2 row 1.) (Settled: the five Mongol figures, the *teppō* and the tree added to the Ekotoba are identified from Conlan's direct PDF. See G2 row 2.) Suenaga's 1293 text date and the 2021 National Treasure listing are unconfirmed. Whether the Sasaki 2009 thesis PDF is public (the record suggests an embargo).
- **G3.** The NPM 2020 dating of the leaves. The plates in the UNESCO dossier (blocked). (Settled: Watt 2010 is readable on Google Books with the Met's permission, viewer only, no PDF.) The Pucheng 1269 date and its citation. Qianlong's re-cutting of the Dushan dayuhai.
- **G4.** (Settled: lat. 10136 is Gallica btv1b525197582. A full thumbnail scan found no ship drawing, but it did find a council chamber (p. 231) and the 1227 Savona siege with labelled trabucos (pp. 289–290).) Is Laiazzo named on the Carte Pisane (the BnF notice lists no place-names) or on Pal. lat. 1362 A? A whole-chart Gallica image (1536 × 766 px, input/media) is too small to read: the red cartouche at the Cilician bend is illegible. An unsourced note claiming the reading "Layazo" in red was not verified. A high-resolution IIIF crop (pct:10,30,12,18, read 2026-11-13) shows the Levant coast clearly. It runs south to north: saiet (Sidon, red), barut (Beirut, red), gibelet, botron, Tripuli · Suria (red), margato (Margat, red), maraclea, ualanea, belda, la lecca (Latakia, red), then up to the bend at what looks like alexandreta. The red cartouche at the bend reads **Leuante**: it is the label for the east wind, not a port. The Cilician names beyond the bend are written diagonally and are too faint to read in that crop, so **Layazo is still unconfirmed**. A second unsourced AI summary was checked too. It reads the boxed red name as "lica" (Latakia), but the box reads Leuante, and Latakia is the red "la lecca" further down. It claims "terra de erminia" and "gloriosa" in red, neither of which is visible in the crop. It says north is at the top, but the names in this area are written upside down. It also cites Lin 2019 for "laiazo" on the chart, which is wrong: Lin (Birmingham PhD, 2017/2019, [PDF](https://etheses.bham.ac.uk/id/eprint/8689/5/Lin2019PhD.pdf), opened) **explicitly excludes the Carte Pisane** from his toponym tables (pp. 103–104). His forms (laiaza, laiazo, Laiacium…) come from Vesconte 1313 onward. The summary's black-ink readings "porto uallo" and "la sudino" (Soldino, the port of Antioch) do match the crop. Lin's tables list the chart order Licia – Soldino – Alexandretta – **Laiazo** – Tarsus – Curco, so on the Pisane, Ayas should be the next name or names past the bend. **A later close reading of the same crop:** the diagonal Cilician names include a red **terſſo** (Tarsus, Lin's form "tersso"). Before it, toward the bend, a red word reads roughly *lo ma(l)o*, which is possibly Mallo. Nearer the bend there is a faint red line I can only make out as "…dell… [i]mpere…". **None of these reads laiazo.** A third AI table claimed red "g. de laiazo" and "laiazo", plus "la gloriata" for Latakia. Neither laiazo form is visible, and Latakia is the red "la lecca". Its tarso, malo, alexandreta, la sudino and porto uallo readings agree with the crop. So Ayas is still unconfirmed, but it is now bracketed between alexandreta and terſſo. **A possible reading (2026-11-13, from the user's tight crop):** the faint red word in that slot can be read as *(l)aiaſo*, with a tall long-s before the final o. The comparison that counts is the same hand's ſ in the red *terſſo* beside it. A printed insular alphabet is a different script tradition, so it is no help here. *Layaso* is an attested chart form of Ayas (Lin 2019, toponym list), which makes the reading plausible. But a fold line runs through the word, and the first letters are uncertain. **Status: probable, not confirmed.** Cite it as "a red name, probably *[l]aiaso*, in the Ayas position". **Charts to contrast**, from Lin 2019, Table 2-1 and figs. 2-3–2-6 (opened):
- Vesconte 1313, BnF Rés. Ge. DD 687 (reads *laiaza*).
- Vesconte 132[1], BAV Pal. lat. 1362A f. 4v (*laiazo*).
- Vesconte workshop c. 1321, BAV Vat. lat. 2972 f. 108v (*Laiacium*).
- Anonymous Genoese, 2nd quarter of the 14th c., BnF lat. 4850 f. 7r.

All are later than the Pisane, but each is dated and names Ayas legibly. **For the plates, the port's existence does not depend on the Pisane.** It rests on Polo's own text (*Laias*) and on Genoese notarial deeds drawn up at Ayas by Federico di Piazzalunga and Pietro di Bargone in 1274–1279 (Lin 2019, ch. 2). The edition of those deeds, Balletto's *Notai genovesi in Oltremare… Laiazzo*, is from memory and unverified. Try the next crop along, e.g. pct:18,42,10,14. Check it against a high-resolution IIIF crop, e.g. `https://gallica.bnf.fr/iiif/ark:/12148/btv1b52503226n/f1/pct:10,30,12,18/full/0/native.jpg`. Is any illuminated mariegola before 1300? (Settled: the Cocharelli manifest is open and public domain outside the UK; CHARLVAR Album 227 is © 2019 CHARLV, viewable.) The San Marco atrium mosaics, the Contarina wrecks and the Genoese notarial cartularies were not checked.
- **G5.** What Leiden holds for Jago, Singasari, Jawi and Pasai (the site was unreachable again). The Wereldmuseum RV-1403 record text (date, licence); images are now saved locally, records not. The 18 August 2023 repatriation date rests on one source. The AH 696 date of the Pasai epitaph, and whether Lambourn 2008 argues against Moquette. Candi Jawi, Tamil temple ship reliefs and the BL Maqamat Or. 1200 were not searched.
- **G6.** The BSB record's date field still reads "678 oder 778"; only its description supports 1280. The Gallica images of Suppl. persan 205 (the ark is known; Gallica blocks scripts). Which M.500 folios show camels, horses and dress. The 1270s inscriptions on the Takht tiles. Whether the Kogou et al. paper is about Cave 465. The Marzubannama (1299), the IDP's relaunched IIIF viewer and the Digital Dunhuang terms were not checked.
- **P1/P2.** The Freer (NMAA) filtering syntax is unresolved. The archive.org mirror licences are undocumented, and the metadata does not name the source.
- **P3.** Inventory numbers for the Takashima finds, the Mingshui robe and the Abegg garment. The Karakorum arrowhead number U.63-1-7 rests only on the hobbyist page. Vosmer et al. 2011 in *PSAS* 41 (the publisher page timed out, and Crossref has no record). The "Cagaan Chad" bow. Kubik 2020's title.
- **P4.** Whether Haug 2016 is open access (the V&R eLibrary returned 403). The subtitle of the Karakorum vol. 1 entry.

## Conclusion

Two of the six gaps can be illustrated from a dated, open image today. G6's figures come from the 1280 Qazwini manifest, and G2's kit from the Takashima reports. Two more gaps get part of the way, but only through attribution or analogue: G3's dress (the NPM leaves) and G5's Singhasari Java. G1 and G4 cannot be illustrated from a period image at all, and neither can the ship rows of G5. Their plates should be credited openly as reconstructions from text: Rubruck for the ger cart, Pryor's 1246–1269 contracts for the Mediterranean nave, and the *Yuanshi* for the Xiangyang engine. Saying so in the plate notes is more defensible than borrowing a Timurid or Edo-period image.

The next return comes from browser work, not more searching. About half the decisive answers sit behind the bot-blocked sites: the Gallica folios, the Heidelberg Vesconte sheet, the UNESCO plates, the Leiden OD photographs and the DAI Karakorum PDFs. A single manual session on those sites would settle most of the open questions above.
