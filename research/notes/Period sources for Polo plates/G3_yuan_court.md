# G3 — Khubilai's court (Yuan hall / Shangdu–Dadu interior, banquet vessels, court dress 1260–1295, Green Mount before 1300)

Method note: this run used about 17 tool calls and was interrupted once by a rate limit. whc.unesco.org returned HTTP 403 to every scripted fetch. The Heidelberg journal server is behind an Anubis bot check. No Chinese search found the Pucheng or Yuanbaoshan tomb reports online. Confidence labels: **OC** = opened and confirmed; **CAT** = found in a catalogue, search listing or citation (not opened); **MEM** = from memory, unverified. "NEW" = published after 2013.

## Q1. Ranked sources (up to 6) likely to hold a dated, viewable, in-window image

### Takeaway
No source turned up a G3 image that is **both** firmly dated inside 1260–1295 **and** free to script.
- **Best for court dress:** NPM Taipei's open-data platform (CC0 / CC BY 4.0) holds the Yuan emperor and empress portrait albums. The Khubilai and Chabi leaves are attributed to about 1294, but that rests on attribution, not on an inscription.
- **Green Mount:** the only in-window anchor is the jade jar Dushan dayuhai. The *Yuanshi* dates it to Zhiyuan 2 (1265), when it was set in the Guanghan Hall on Qionghua island. It was later reworked.
- **Halls and interiors:** these exist only as excavated foundations and plans (UNESCO Xanadu dossier; Steinhardt). No contemporary picture of an interior is known to me.

### Cited Findings

**1. National Palace Museum (Taipei) Open Data — Yuan emperor and empress half-length portrait albums**
- (a) What and where: NPM Taipei. The albums are 元代帝半身像冊 (8 emperor leaves) and 元代后半身像冊.
  - Khubilai leaf: accession number cited as 中-畫-000324-00003, ink and colour on silk, 59.4 × 47 cm — [Commons-mirror file description](https://en.Wikipedia.com/wiki/File:YuanEmperorAlbumKhubilaiPortrait.jpg).
  - Chabi leaf: cited as 中畫000325N000000000 — [Commons mirror](https://en.Wikipedia.com/wiki/File:YuanEmpressAlbumChabi.jpg). A University of Washington teaching page gives 61.5 × 48 cm, which conflicts with the above — [UW China Civ](https://depts.washington.edu/chinaciv/painting/4pmtchab.htm).
  - The album is 8 leaves; the Taizu leaf is 中畫00324 — [storm.mg article, via search snippet](https://www.storm.mg/article/2452951).
  - Status: platform **OC**; item records **CAT** (I did not open any NPM item page for these leaves).
- (b) Why in-window: they show court dress (white *jisün*-type robe and hat for Khubilai; the *gugu* headdress for Chabi).
  - Dating rests on attribution only. Commons describes the Khubilai leaf as posthumous, painted shortly after his death in February 1294, possibly by Anige (CAT; secondary). The Anige attribution is credited to Anning Jing (CAT).
  - A Chinese article notes the leaves carry no artist signature, so authorship is unresolved. It also compares the face with the Khubilai in *Khubilai Khan Hunting* (1280) — storm.mg (CAT).
- (c) Access: open API / direct download.
  - The platform has 108,670 items, including 16,697 paintings. Low-resolution (1 MP) images are CC0; mid-resolution (6 MP) are CC BY 4.0. The site gives no API documentation.
  - Item URL pattern: `/opendata/Pub/Detail/{id}?dep=U&mode=full`. Images come from `/opendata/Image/GetImage?imageId=…`. English UI: `/opendata/Pub/EngVersion` — [NPM Open Data](https://digitalarchive.npm.gov.tw/opendata) (**OC**).
  - The 2017 open-data release is described in [Open Culture](https://openculture.com/2018/08/free-download-70000-high-resolution-images-chinese-art-taipeis-national-palace-museum.html).
  - A 2021 hackathon handout lists "Open API" functions (single item, collection list, exhibitions) but no endpoints — [NPM handout PDF](https://presidential-hackathon.taiwan.gov.tw/history/2021/files/中英文_國立故宮博物院.pdf) (CAT).
- (d) Search terms: 元世祖, 元世祖后, 察必, 元代帝半身像, 元代后半身像, 中-畫-000324, 中-畫-000325; filter 朝代 = 元, 分類 = 繪畫.
- (e) Risks:
  - No date is inscribed; c.1294 is an attribution. The leaves are bust-length only (no hall, no vessels).
  - Qing remounting: the Nanxun Hall imperial portraits were reorganised and moved under Qianlong (Qianlong 12–14, 1747–49). An NPM monthly article says this about the Nanxun dian group as a whole, while discussing Ming portraits — Shi Zhaozhao, 故宮文物月刊 455 [PDF](https://www.npm.edu.tw/NewChineseArtDownload.ashx?bid=4252) (**OC**, Ming-focused).
  - That article cites a **NEW** catalogue: 國立故宮博物院編《南薰殿歷代帝后圖像》上冊 (Taipei: NPM, 2020). It should contain the formal NPM dating for the Yuan albums; I have not seen it.

**2. UNESCO World Heritage nomination file 1389, *Site of Xanadu* (Shangdu)**
- (a) What and where: State Party nomination dossier (China), received 20 January 2011 and inscribed 2012 (Decision 36 COM 8B.21). The documents page lists "Nomination file 1389" (390 MB), the ICOMOS evaluation and maps — [documents page](https://whc.unesco.org/en/list/1389/documents); dossier text record [document/152541](https://whc.unesco.org/document/152541); French [152542](https://whc.unesco.org/document/152542); maps [1389/maps](https://whc.unesco.org/en/list/1389/maps/).
  - Status: **CAT** (search listing only). Both whc.unesco.org URLs returned 403 when fetched.
- (b) Why in-window:
  - Shangdu was founded in 1256 by Liu Bingzhong and was Khubilai's summer capital throughout 1260–1295.
  - The excavated palace platforms (e.g. 穆清閣, 大安閣) and the city plans date to Khubilai's reign by construction history, not by any image.
  - The plates and site plans are what an illustrator needs for layout and foundation scale (MEM for hall names).
- (c) Access: direct PDF, but blocked to scripts (403). Download manually in a browser. The file is very large (390 MB).
- (d) Search terms: 元上都遗址, 穆清阁, 大安阁, 宫城, 皇城; "Site of Xanadu", "Muqing Pavilion".
- (e) Risks: ruins and reconstructions only, no contemporary interior; access blocked.

**3. Jade wine jar 瀆山大玉海 (Dushan dayuhai), Tuancheng, Beihai, Beijing — the Green Mount anchor**
- (a) What and where: the object is in situ in the 玉瓮亭 pavilion, Tuancheng (Beihai Park). It has no museum digital record that I found.
  - The *Yuanshi* (Shizu benji) says it was finished in Zhiyuan 2/12 (early 1266 in the Western calendar; usually cited as 1265) and ordered placed in the Guanghan Hall on the summit of Qionghua island (Wanshou shan). It held wine at Khubilai's banquets.
  - Later history: it ended up in the Zhenwu temple, was moved to Tuancheng under Qianlong and given a marble stand, and Qianlong's 《玉瓮歌》 was carved inside — [Sohu article quoting the *Yuanshi*](https://m.sohu.com/a/276852856_708264/) (CAT; secondary/media, here only to point to the *Yuanshi* entry).
- (b) Why in-window: this is the only surviving Green Mount object with a reign-year date in a primary text, and it doubles as a banquet vessel.
- (c) Access: no open-licensed scholarly image found. Primary text: 《元史·世祖本紀》 at Chinese Text Project (not opened).
- (d) Search terms: 瀆山大玉海, 玉瓮, 廣寒殿, 萬壽山/萬歲山, 瓊華島, 至元二年.
- (e) Risk (MEM, unverified): the Qianlong court is said to have had it re-cut and repolished several times, so the present surface is partly 18th-century. My search for this ("四次修琢") returned nothing confirming. Use it for form and scale, not surface detail.

**4. Nancy S. Steinhardt — plans and reconstructions of Dadu and Shangdu**
- (a) Works:
  - "The Plan of Khubilai Khan's Imperial City", *Artibus Asiae* 44.2/3 (1983): 137–58 — cited in [Acta Mongolica PDF](https://journal.num.edu.mn/actamongolica/issue/download/445/261) (CAT).
  - **NEW:** *Yuan: Chinese Architecture in a Mongol Empire* (Princeton UP, 2024) — [Princeton UP](https://press.princeton.edu/node/59535); [De Gruyter, DOI 10.1515/9780691253350](https://www.degruyterbrill.com/document/doi/10.1515/9780691253350/html) (CAT).
  - A review of the 2024 book exists in *Journal of Transcultural Studies*-type outlet "xxi" at Heidelberg (blocked by bot check, not opened).
  - *Chinese Imperial City Planning* (Honolulu: University of Hawai'i Press, 1990) (MEM).
- (b) Why in-window: hall plans of Dadu's palace city (大明殿, 延春閣) and the Qionghua/Taiye pond layout, drawn from the Yuan texts 《南村輟耕錄·宮闕制度》 and from excavation.
- (c) Access: JSTOR / publisher, paywalled. The 2024 book is an ebook only.
- (d) Search terms: Khanbaliq, Daidu, Dadu palace city, Taiye chi, Qionghua.
- (e) Risks: modern reconstructions, not period images. Use them as constraints on layout, not as pictures to describe.

**5. James C. Y. Watt et al., *The World of Khubilai Khan: Chinese Art in the Yuan Dynasty* (New York: Metropolitan Museum of Art, 2010)**
- (a) Bibliography: 360 pp., 407 illustrations. Contributors: Maxwell K. Hearn, Denise Patry Leidy, Zhixin Jason Sun, John Guy, Joyce Denney, Birgitta Augustin, Nancy S. Steinhardt — [MetPublications listing](https://www.metmuseum.org/met-publications/the-world-of-khubilai-khan-chinese-art-in-the-yuan-dynasty) (CAT; metmuseum.org pages are known to fail, so not opened).
- (b) Why: Steinhardt's chapter on Dadu and Shangdu, Dadu excavation finds (Houyingfang etc. — MEM), Yuan court textiles and silver, and loans of dated objects.
- (c) Access: unconfirmed. I found no free-PDF link, and I did not locate the "Watt PDF route" the brief mentions.
- (e) Risk: may be view-only or purchase-only. Plates show objects, mostly labelled only "Yuan dynasty".

**6. Dated Yuan tomb murals (Pucheng Dongercun 1269; Chifeng Yuanbaoshan)**
- (a) Excavation reports in Chinese journals. MEM, not verified:
  - 陝西蒲城洞耳村元代壁畫墓, *考古與文物* c.2000.
  - 內蒙古赤峰市元寶山元代壁畫墓, *文物* 1983.
- My English and Chinese searches found **no** online record of either. The only related hit was a Chifeng Museum Yuan mural of a seated couple labelled just "Yuan Dynasty (1271–1368)" — [China Daily](https://govt.chinadaily.com.cn/s/202405/16/WS6645a532498ed2d7b7eadce3/exquisite-inner-mongolia-murals-to-provide-local-visitors-with-vibrant-history_4.html) (CAT).
- (b) Why: Pucheng carries a reported ink date in Zhiyuan 6 (1269) (MEM). It shows a Mongol couple at a table with vessels: in-window Mongol dress and banquet ware, but provincial, not court.
- (c) Access: CNKI, paywalled; nothing found on the open web.
- (d) Search terms: 蒲城 洞耳村 元墓, 元寶山 元墓 壁畫, 元墓壁畫 至元, 夫婦對坐 宴飲圖.
- (e) Risks: provincial elite, not court; date and bibliography unverified.

**Not ranked**
- Palace Museum Beijing (digicol.dpm.org.cn): a search for Yuan 至元-dated items returned nothing from that site. Whether it can be scripted is unconfirmed.
- *Shilin guangji* (Yuan editions, 1330s): too late for the window (MEM).

### Inferences
- For court dress, the NPM leaves are the strongest source that can be scripted and reused. Present them as "attributed c.1294, possibly Anige", never as "dated 1294".
- For halls and the Green Mount, describe from the *Yuanshi* and 《輟耕錄》 texts, with Steinhardt's plans as the frame and the Dushan dayuhai as the one tangible in-window object. There is no period interior image to fall back on.

### Gaps
- I could not confirm the NPM item IDs, or that the Yuan albums are actually in open data. The platform covers paintings, but I opened no item page.
- UNESCO PDF contents (plates, figure numbers) could not be fetched (403).
- I did not find a free PDF of Watt 2010.
- Pucheng and Yuanbaoshan report citations, and the 1269 date, are unverified.
- Qianlong's reworking of the Dushan dayuhai is unverified.
- I found no Yuan silver hoard with a 至元 inscription online.

## Q2. Scholars and works a specialist would read first for G3

### Takeaway
Start with Steinhardt for the capitals, Watt 2010 for court material culture, and NPM's 2020 Nanxun Hall catalogue for the portraits. None is confirmed free.

### Cited Findings
- Steinhardt, "The Plan of Khubilai Khan's Imperial City", *Artibus Asiae* 44 (1983) 137–58 (JSTOR, not free) — [cited in Acta Mongolica](https://journal.num.edu.mn/actamongolica/issue/download/445/261).
- Steinhardt, *Yuan: Chinese Architecture in a Mongol Empire*, Princeton UP 2024, **NEW** (not free) — [Princeton UP](https://press.princeton.edu/node/59535).
- Watt et al., *The World of Khubilai Khan*, Met 2010 (free status unknown) — [MetPublications](https://www.metmuseum.org/met-publications/the-world-of-khubilai-khan-chinese-art-in-the-yuan-dynasty).
- 國立故宮博物院編《南薰殿歷代帝后圖像》上冊, Taipei 2020, **NEW** (not free) — cited in [故宮文物月刊 455](https://www.npm.edu.tw/NewChineseArtDownload.ashx?bid=4252).
- MEM, unverified:
  - Anning Jing, "Anige" / Yuan imperial portraits, *Artibus Asiae* c.1994.
  - Shane McCausland, *The Mongol Century* (Reaktion, 2014, NEW).
  - Zhao Feng and James Watt, *When Silk Was Gold* (1997), for court textiles.

### Inferences
- Draft BibTeX keys: steinhardt1983plan, steinhardt2024yuan, watt2010khubilai, npm2020nanxundian, unesco2011xanadu.
- Fields that need checking before use: the publisher for Watt is "Metropolitan Museum of Art / Yale UP" (MEM). For the UNESCO dossier, author = "People's Republic of China", year 2011, institution = UNESCO WHC, number = 1389.

### Gaps
- Free-access status for every scholar work above.
- Exact page and plate numbers for any Yuan hall plan.
