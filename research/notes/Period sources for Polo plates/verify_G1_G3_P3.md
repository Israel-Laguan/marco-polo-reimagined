# Verification pass: G1, G2, G3, P3

Report checked: `reports/Period sources for Polo plates.md`. Checked 2026-11-13. Format: claim → status → evidence.

## 1. Takashima site reports (G2 rank 1, P3)

- Record 62578 → CONFIRMED that it is a Takashima report, but CORRECTED identity: 鷹島海底遺跡 8, 副書名 長崎県北松浦郡鷹島町神崎港改修工事に伴う発掘調査概報②, 鷹島町文化財調査報告書 7, ed. 小川光彦, 松尾昭子, 林田憲三, Takashima Town Board of Education, 2002-03-31. Frequent terms in the text include 小札 (lamellae), 帯金具, 球状土製品 and 船材. There is no 冑, 刀 or 印 in the frequent-term list, and no page numbers for plates. → https://sitereports.nabunken.go.jp/62578
- Records 21714, 62589 and 131601 (titles, numbers, years) → BLOCKED: HTTP 429 "アクセスが集中", including after a slow retry. A second fetcher was refused as bot-check circumvention. → https://sitereports.nabunken.go.jp/{21714,62589,131601}
- Which report has plates of the helmet (冑), swords, armour and the 1277 管軍総把印 → STILL UNCONFIRMED (records blocked).
- "Seal dated 至元十四年 (1277)" → STILL UNCONFIRMED.
- KAKEN 23222002 final report PDF, "not opened" → CONFIRMED and opened. It is the 研究成果報告書 for 平成28 (2016) and lists 4 project volumes: ① 最終報告書 第三冊, 230 pp., March 2016; ② 第2冊, 108 pp., 2015; ③ 文献史料編 第1冊, 136 pp., 2014; ④ 海底音波探査成果報告書 第1冊, 42 pp., 2013 (ed. 池田栄史). The body mentions 磚, ceramics and 球形土製品 ("てつはう"). It does not name helmet or sword plates. → https://kaken.nii.ac.jp/file/KAKENHI-PROJECT-23222002/23222002seika.pdf

## 2. NPM Taipei Yuan portrait leaves (G3 rank 1)

- Khubilai leaf "中-畫-000324-00003 (59.4 × 47 cm)" → CORRECTED: open-data item **15489** (`/opendata/Pub/Detail/15489?dep=P&mode=full`, so dep=**P**, not U). 文物統一編號 中畫000324N000000003, 作品號 中畫00032400003, 元代帝半身像 冊 元世祖. Painting (本幅) 59.2 × 47.4 cm on silk; facing leaf (對幅) 59.1 × 47.8 cm. Artist "anonymous". 著錄 故宮書畫錄 卷七 冊4 pp. 46–50. → https://digitalarchive.npm.gov.tw/opendata/Pub/Detail/15489?dep=P&mode=full
- Chabi leaf "中畫000325N000000000" → CORRECTED: item **15495**. 文物統一編號 中畫000325N000000001, 作品號 中畫00032500001, 元代后半身像 冊 元世祖后. Inscription 世祖皇帝后徹伯爾. 61.2 × 47.6 cm on silk. 著錄 故宮書畫錄 卷七 冊4 pp. 50–53. → https://digitalarchive.npm.gov.tw/opendata/Pub/Detail/15495?dep=P&mode=full
- Licence "1 MP CC0, 6 MP CC BY 4.0" → CONFIRMED on both item pages (credit line "國立故宮博物院，臺北，CC BY 4.0 @ www.npm.gov.tw").
- Item pattern "…?dep=U&mode=full" → CORRECTED: these painting items use `dep=P`. Search is a JSON POST to `/opendata/Pub/Search`, where `SearchContent` holds the search terms.
- Stated date → CONFIRMED as no date. The pages give only "元代" in the title and no date field, which fits "attributed c. 1294". References cited on the page: 陳韻如 in 《大汗的世紀》 (NPM 2001), p. 288, and 故宮文物月刊 223 (2001.10), pp. 9–11.

## 3. Bibliographic checks

- Sasaki thesis, 2009, hdl 1969.1/ETD-TAMU-3100 → CONFIRMED: "The origin of the lost fleet of the Mongol Empire", Randall James Sasaki, issued 2009-05-15. The degree and the PDF were not shown on the TDL page, and OakTrust returned 403. → https://tdl-ir.tdl.org/handle/1969.1/ETD-TAMU-3100
- Chevedden, *DOP* 54: 71–116, doi:10.2307/1291833 → CONFIRMED for the title, vol. 54, 2000 and start page 71. Crossref gives no end page, so 116 is STILL UNCONFIRMED. → https://api.crossref.org/works/10.2307/1291833
- Steinhardt, "The Plan of Khubilai Khan's Imperial City", *Artibus Asiae* 44 (1983) → CONFIRMED and extended: vol. 44, no. 2/3, starting p. 137, doi:10.2307/3249595 (end page not in Crossref). → https://doi.org/10.2307/3249595
- Related, not in the report: Jing Anning, "The Portraits of Khubilai Khan and Chabi by Anige", *Artibus Asiae* 54.1/2 (1994), starting p. 40, doi:10.2307/3250079. This is relevant to the "possibly Anige" attribution.
- Watt 2010 free PDF status → BLOCKED: metmuseum.org returned 429. STILL UNCONFIRMED.

## 4. Mōko Shūrai Ekotoba (G2 ranks 2–3)

- Kyushu manifest URL, Public Domain → CONFIRMED. IIIF Presentation 3, label 蒙古襲来絵詞 (模本), 94 canvases, Rights "パブリックドメイン / Public Domain". → https://catalog.lib.kyushu-u.ac.jp/image/manifest_custom/1/820/411726.json
- "9823 × 7825 px" → CORRECTED: only some canvases are 9823 × 7825. Long scroll canvases run up to 28540 × 1554 (canvas 1 is 27968 × 1682).
- "late-Edo copy of the version then held at Aso Shrine" → CONFIRMED in part. The manifest description reads 肥後国阿蘇宮蔵画巻物寫 / 卧遊舎蔵, which says it was copied from the Aso Shrine scroll. The date of the copy is not stated there.
- Conlan's list of later additions (three bowmen around the bomb are 18th c.) → STILL UNCONFIRMED. The Wayback copy of bowdoin.edu/mongol-scrolls/ (2018-09-24) is a Flash shell (index.swf) with no readable text. There is no Wayback copy of tconlan.scholar.princeton.edu/document/41, and the CDX index was "Temporarily Offline". → http://web.archive.org/web/20180924111720/http://www.bowdoin.edu:80/mongol-scrolls/
- Suenaga text dated 1293; National Treasure 2021 → STILL UNCONFIRMED (not opened).

## 5. Topkapı Hazine 1653/1654 (G1 rank 1)

- "Ghiasian 2022, Cambridge Core" → CORRECTED: Mohamad Reza Ghiasian, "The Topkapı Manuscript of the Jāmiʿ al-Tawārikh (Hazine 1654) from Rashidiya to the Ottoman Court: A Preliminary Analysis", *Iranian Studies* 51.3 (2018): 399–425. 2022 is only the online date shown on the page. → https://www.cambridge.org/core/product/D298994042B2643F0E25DAA747EA7E09
- A citable statement of a tent-on-wagon scene → STILL UNCONFIRMED. The abstract and references show no wagon, tent or camp scene, and the body text is paywalled.
- G1 ranks 2–6 (Siyah Qalam albums, Liao and Yuan murals, DAI FAAK, SHM models) → not rechecked; out of scope for this pass.

## 6. P3 items

- Mingshui robe "Darhan Muminggan, excavated 1978, Inner Mongolia Museum, 13th–14th c." → CONFIRMED: Onggut tomb at Dasujixiang Mingshui, Daerhanmaomingan United Banner, excavated 1978, images courtesy of the Inner Mongolian Museum. Added detail: 142 × 246 cm, silk with gold brocade. No accession number on the page. → https://depts.washington.edu/silkroad/exhibit/mongols/fig_104.html
- Abegg inventory number → STILL UNCONFIRMED (not attempted; no URL given beyond the review).
- Karakorum arrowheads, Inv. U.63-1-7 → STILL UNCONFIRMED. Not re-fetched; it rests only on the hobbyist page.
- Pryor in *Mariner's Mirror* → CONFIRMED with exact citations:
  - "Transportation of Horses by Sea during the Era of the Crusades": MM 68.1 (1982): 9–27, doi:10.1080/00253359.1982.10655843; and 68.2 (1982): 103–125, doi:10.1080/00253359.1982.10655855.
  - "The Naval Architecture of Crusader Transport Ships": MM 70.2 (1984): 171–219, doi:10.1080/00253359.1984.10655967; 70.3: 275–292, doi:…10655978; 70.4: 363–386, doi:…10655992.
  - "… and Horse Transports Revisited": MM 76.3 (1990): 255–273, doi:10.1080/00253359.1990.10656308.
  - Source: Crossref, https://api.crossref.org/works?query.bibliographic=Pryor+naval+architecture+of+crusader+transport+ships+Mariner%27s+Mirror
- Vosmer et al. 2011, *PSAS* 41 → BLOCKED: the archaeopresspublishing.com article page timed out, and Crossref has no PSAS record. STILL UNCONFIRMED. Crossref shows only a related Vosmer paper in *Historic Ships 2009* (RINA), pp. 31–40, doi:10.3940/rina.hist.2009.05.
