# Deep research prompt — locate the sources (third pass, source-finding)

Run in a tool that can search inside books and databases (a research agent with browsing, or by hand). Save the output to `plans/research/results/GAZ-sources-raw.md`, with a first line naming the tool, model and date. Intake: `GAZ.T6`.

Why a third pass: the first two runs could not open the specialist literature, so they fell back on Yule. This one does not ask for a verdict. It asks *where* each source discusses each name, with a short verbatim quote that can be checked, and it points to tools that can search inside works still in copyright.

```text
TASK: SOURCE LOCATION, NOT INTERPRETATION.
For 23 place names in Marco Polo's book (listed below), find exactly where the specialist literature discusses each one, and quote it. I will read the sources myself. Do not summarise scholarly consensus and do not give me your own identification.

USE THESE TOOLS (they reach content that general web search does not):
1. HathiTrust full-text search (https://babel.hathitrust.org/cgi/ls). It searches inside in-copyright books and returns page numbers even when the text is "search only". Search each name in:
   - Pelliot, *Notes on Marco Polo* (1959–73);
   - Moule & Pelliot, *The Description of the World* (1938);
   - Haw, *Marco Polo's China* (2006);
   - Wheatley, *The Golden Khersonese* (1961);
   - Luce, *Old Burma–Early Pagán* (1969);
   - Yule–Cordier (1903) and Cordier, *Ser Marco Polo: Notes and Addenda* (1920).
2. Google Books "search inside" (books.google.com, search within the volume) for the same titles, plus Vogel, *Marco Polo Was in China* (2013), and Atwood, *Encyclopedia of Mongolia and the Mongol Empire* (2004). Record the page shown in the snippet.
3. Internet Archive full text (archive.org, "search text contents"), including borrowable copies of Pelliot's *Notes*, Wheatley and Haw.
4. Toyo Bunko / Digital Silk Road (dsr.nii.ac.jp) for Pelliot material and the Toyo Bunko Marco Polo collection, if available.
5. Persée (persee.fr) and JSTOR for articles in *T'oung Pao*, *BEFEO*, *Journal Asiatique*, *JMBRAS*, *JRAS*, *Journal of the Siam Society*. In particular:
   - Wheatley, "Lochac Revisited";
   - articles on Tenduc / the Öngüt and Olon Süme;
   - articles on the Polo itinerary in Yunnan and Guizhou, and on Malayu / Dharmasraya.
6. Chinese sources for the Chinese rows:
   - Chinese Text Project (ctext.org): the *Yuan shi* 元史 *Dili zhi* 地理志, and the *Zhanchi* 站赤 (Yuan post-station lists from the *Yongle dadian*);
   - CNKI (cnki.net), searching Chinese studies of 馬可波羅 / 马可·波罗 with each candidate place name.
   For each Chinese row, give the Yuan-period administrative name of each candidate and confirm it existed under that name c. 1280–1295 (e.g. was Anqing 安慶路 and Nanjing 集慶路 in Yuan times?).
7. CHGIS, the China Historical GIS (Harvard / Fudan; https://chgis.fas.harvard.edu, and the TGAZ gazetteer API at https://maps.cga.harvard.edu/tgaz/). For each Chinese candidate, give the CHGIS ID, the Yuan-period name, and the CHGIS coordinates of the seat valid in 1280–1295. This is the coordinate source I want for China.
8. For Southeast Asia and Inner Asia, give coordinates from GeoNames (geonames.org) or a named archaeological report. Do not use coordinates without a source.

FOR EACH ROW RETURN A "SOURCE MAP":
- For each work above that discusses the name:
  - full reference;
  - volume and page (or entry headword);
  - URL or tool where you saw it, and access type: full view / search-only / snippet / borrowed;
  - a VERBATIM quote of at most 40 words containing the identification, in the original language with an English gloss if not English.
- Works searched where the name was NOT found: list them (this matters as much as hits).
- For Chinese rows: the candidates' Yuan names, Chinese characters, and CHGIS ID + coordinates.
- Nothing else. No consensus statement, no recommendation.

RULES:
- A citation without a verbatim quote and a page is not acceptable. If only a snippet with no page is visible, say "snippet, page not shown".
- Never quote from memory. If a tool returned nothing, write "searched, no hit".
- Search variant spellings: F / Z / R / Latin forms and Pelliot's headwords (Pelliot often indexes under a reconstructed form, e.g. "Balur", "Tänduc", "Ciugiu"). Say which spelling produced the hit.
- Two snippets I need checked verbatim: Pelliot, *Notes* I p. 108 (Bolor) and II p. 17 (Dagroian).

THE ROWS (id | Polo's name | variant spellings to search | candidates to search with it):
1. bolor | Bolor | Belor, Balor, Balur | Gilgit, Chitral, Yasin, Baltistan, 勃律
2. pein | Pein | Pem, Pen, Peym | Keriya, Uzun-Tati, Dandan-Uiliq, Domoko, 媲摩 Pimo
3. tenduc | Tenduc | Tanduc, Tänduc | Tümed, Hohhot, Olon Süme, Togtoh, Öngüt, 天德 Tiande
4. cuncun | Cuncun | Cuncum, Chunchun | Qinling, Baoxie road, Lianyun road, 褒斜, 連雲棧
5. acbalec-manzi | Acbalec Manzi | Achbaluch, Acbaluc | Hanzhong 興元路, Mianzhou, Lüeyang
6. bangala | Bangala | Bengala | Bengal, Pegu, Lower Burma
7. caugigu | Caugigu | Cangigu, Cauzigu, Kafchikue | Kiang Hung / Jinghong 車里, Kengtung, Chiang Mai 八百媳婦, Jiaozhi 交趾
8. anin | Anin | Aniu, Amu | Lin'an 臨安路 (Jianshui), Mile, Honghe
9. coloman | Coloman | Toloman | 土老蠻, Wumeng 烏蒙, Zhaotong
10. cuiju | Cuiju | Cuigiu | Guizhou 貴州, Kuizhou 夔州, Xuzhou 敘州
11. fungul | Fungul | Sinugul, Singul | Xuzhou / Suifu 敘州 (Yibin), Luzhou 瀘州
12. linju | Linju | Lingiu, Ligni | Linqing 臨清, Xuzhou 徐州
13. tinju | Tinju | Tingiu, Cingiu | Tongzhou 通州 (Nantong), Taizhou 泰州
14. nanghin | Nanghin | Namghin, Nanchin | Anqing 安慶路, Nanjing 集慶路 / 建康, Nanyang 南陽
15. vughin | Vughin | Vugin, Uguin | Wujiang 吳江, Wuxi 無錫
16. tanpiju | Tanpiju | Tanpigiu, Tapinzu | Shaoxing 紹興路, Fuyang 富陽, Xiaoshan 蕭山
17. changshan | Changshan | Cianscian, Zengian | Changshan 常山, Suichang 遂昌, Xianxia pass 仙霞關
18. cuju | Cuju | Cugiu | Chuzhou 處州 (Lishui), Pucheng 浦城
19. unken | Unken | Vuguen, Unquen | Houguan 侯官 (Minhou), Minqing 閩清, Youxi 尤溪, Yongfu 永福
20. cheinan | Cheinan | Cheynam, Cheinam | Gulf of Tonkin, Hainan 海南
21. locac | Locac | Lochac, Soucat | Lavo / Lopburi, 羅斛 Luohu, Ligor / Tambralinga, Langkasuka
22. malaiur | Malaiur | Malauir, Maliur | Malayu-Jambi, Dharmasraya, 末羅遊, Tumasik
23. dagroian | Dagroian | Dragoian, Dagroiam | Pidie, Nagur / 花面 Huamian, Lamreh, Tamiang

OUTPUT FORMAT
One section per row (Source map), then a table:
id | source | page | access | quote (≤40 words) | tool/URL.
End with a list of works and databases you could not reach (paywall, login, region block) so I can request them through a library.
```

## Intake notes (for me)

- Verify a sample of quotes against the page images before relying on any (start with Pelliot I p. 108 and II p. 17).
- CHGIS coordinates for a Yuan-period seat replace the modern-city point when the two differ. Set `coord_check` to `approximate` until a `chgis` value is added to the enum (`tools/gazetteer.py`).
- The "not reachable" list becomes a library request list (interlibrary loan / scans).
