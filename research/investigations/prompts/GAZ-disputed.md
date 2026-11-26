# Deep research prompt — the 23 disputed identifications (second pass)

Run in a deep-research tool. Save the output to `plans/research/results/GAZ-disputed-raw.md` with a first line naming the tool, model and date, then bring it back for intake (`GAZ.T6`).

Why a second pass: the first run (`results/GAZ-coords-raw.md`) mostly repeated our own coordinates as "confirmed" with "Standard" as the source. This prompt leaves our coordinates out and asks for sources at entry level for each claim.

```text
I am building a gazetteer for a new English retelling of Marco Polo's book (base text: Yule–Cordier, 1903/1920). Twenty-three of Polo's place names have disputed identifications. For each one I need the full state of the question: who proposed what, on what evidence, and which reading current scholarship prefers. I do not want a single answer chosen for me without the evidence.

SOURCES TO WORK THROUGH, in this order, for every row:
1. Paul Pelliot, *Notes on Marco Polo* (3 vols, 1959–73): the entry under Polo's name (give the entry headword and volume/page).
2. A. C. Moule & P. Pelliot, *Marco Polo: The Description of the World* (1938): the reading in the text and the index.
3. Yule–Cordier (1903, with Cordier's 1920 *Addenda*): the note number and chapter.
4. Later work where relevant:
   - China: Stephen G. Haw, *Marco Polo's China* (2006); Hans Ulrich Vogel, *Marco Polo Was in China* (2013); Chinese-language studies of Yuan itineraries and post roads (*zhan*), e.g. Dang Baohai on the Yuan postal system.
   - Inner Asia: Pelliot; Paul D. Buell; Christopher Atwood, *Encyclopedia of Mongolia and the Mongol Empire*.
   - Southeast Asia: Roderich Ptak; Paul Wheatley, *The Golden Khersonese*; G. R. Tibbetts; Pierre-Yves Manguin; Anthony Reid; E. Edwards McKinnon (archaeology of Lamreh, Kota Cina, Barus).
   - Burma / Bengal: G. H. Luce; Michael Aung-Thwin; Jon Fernquest.
   - Other recent peer-reviewed articles you find.
5. English Wikipedia and Wikidata, only for the modern coordinates of a candidate site once the identification is argued from 1–4.

HARD RULES (the previous run broke these):
- Every claim names its source with an exact locator (author, work, volume, page or note number, or a URL). "Standard", "Accepted", "Common identification" and "majority" are not sources. If you cannot locate a source, write NOT FOUND.
- If you could not open a work (e.g. Pelliot's *Notes* is not online), say so for that row and do not attribute views to it from memory.
- Take each candidate's coordinate from a source you name. Do not invent or round a coordinate to look precise.
- Distinguish (a) what a source states, (b) what it infers, (c) your own inference. Label (c) as INFERENCE.
- Use Polo's itinerary (distances, directions, order) as evidence. Say whether each candidate fits the days and direction Polo gives, under the French (F) and Ramusio (R) readings where they differ.
- If a name is better explained as a confusion (two places merged, a scribal error, hearsay placed on the wrong road), say so. That is an acceptable answer.

FOR EACH ROW RETURN:
- Candidates: every serious identification, each with its proponent(s) and year, the main argument, and a sourced coordinate (lat, lon, what the point is).
- Itinerary fit: does each candidate fit Polo's days and direction? (F vs R if relevant.)
- Current preference: which candidate recent scholarship (after 1950) prefers, with who says so. "No consensus" is a valid answer.
- Recommendation for a map: plot candidate X / plot as a region (give bounds) / do not plot. One-line reason.
- Variant spellings of Polo's name across F, Z, R, and the Latin (P) if Pelliot or Moule give them.
- Confidence in your own answer: high / medium / low.

THE 23 ROWS (id | Polo's name (Yule) | Polo's context | readings I currently know of):

Volume I — overland
1. bolor | Bolor | Mountains reached after the Pamier, "forty days' ride east-north-east" of mountain country; wild idolatrous hunters (Yule Bk I ch. 32) | Gilgit–Chitral–Yasin (Balur / Chinese Bolü); Great vs Little Bolor; Baltistan
2. pein | Pein (Pem) | Province five days from Cotan towards east-north-east; river with jasper and chalcedony; temporary-marriage custom (Bk I ch. 37) | Keriya; Uzun-Tati (Dandan-Uiliq area); Domoko; Kenya-ruin sites of Stein's surveys
3. tenduc | Tenduc | Province "towards the east" after Egrigaia/Calachan; capital Tenduc; ruled by King George, descendant of Prester John; Öngüt Christians (Bk I ch. 59) | Tümed / Hohhot plain; Ordos; Olon Süme (Öngüt capital, Darhan Muminggan); Togtoh (Dongsheng); Tianjiao

Volume II — Cathay, the south-west and Manzi
4. cuncun | Cuncun | After Kenjanfu (Xi'an): three days of plain, then twenty days through mountains and forests to Acbalec Manzi (Bk II ch. 42) | Qinling crossing by the Baoxie / Lianyun "plank road" to Hanzhong; Hanzhong basin itself; alternative roads (Ziwu, Tangluo)
5. acbalec-manzi | Acbalec Manzi | "White city of the Manzi border"; then twenty days of plain to Sindafu (Chengdu) (Bk II ch. 43) | Hanzhong; Mianzhou / Mianxian; Lüeyang; Guangyuan; Zhending (named by the first run; check it, it is in Hebei)
6. bangala | Bangala | South of Mien (Burma), under Mien's king in Polo's scheme; thirty days from Caugigu (Bk II ch. 55) | Bengal (by name and products); Pegu / Lower Burma (by position: Yule); a confusion of both
7. caugigu | Caugigu | Province "towards the east" with a king, tattooing, many wives; 30 days from Bangala, 25 (F) or 15 days to Anin (Bk II ch. 56) | Kiang Hung (Jinghong, Sipsong Panna); Muang Yong / Kengtung; Chiang Mai (Pauthier); Tonkin / Jiaozhi (Kafchikue of Rashid al-Din) as the *name*
8. anin | Anin (Aniu) | 25 (or 15) days from Caugigu; eight days to Coloman (Bk II ch. 57) | Lin-ngan (Jianshui) – Homi (Mile) territory (Garnier/Yule); Annam; Honghe Hani region
9. coloman | Coloman (Toloman) | Eight days from Anin; then Cuiju (Bk II ch. 58) | "Tu-lao-man" people of NE Yunnan / W Guizhou; Wumeng; Zhaotong
10. cuiju | Cuiju | Province with a river; twelve days along it to the city of Fungul (Bk II ch. 59) | Guizhou (Kwei-chau) / Guiyang; Kuizhou (Fengjie, Sichuan); Xuzhou-Yibin river region
11. fungul | Fungul (Sinugul) | City twelve river-days from Cuiju, then twelve days on to Sindafu (Chengdu) (Bk II ch. 59) | Suifu / Yibin; Phungan-lu; Luzhou; Xuzhou
12. linju | Linju (Lingiu) | Eight days south of Sinjumatu (Jining) on the canal; then three days to Piju (Pizhou) (Bk II ch. 63) | Linqing (Shandong); Xuzhou; Odoric's *Lenzin*; Pizhou-area towns
13. tinju | Tinju | Salt-making city near the sea, reached from Tiju (Taizhou), before Yanju (Yangzhou) (Bk II ch. 68) | Tongzhou (Nantong); Taizhou's salt yards (Hailing); Yizheng / I-chin (but I already use Yizheng for Sinju)
14. nanghin | Nanghin | "A very noble province towards the west" after Yanju; silk, cheap grain, lions; before Saianfu (Bk II ch. 69) | Anqing / Ngan-king (Yule, after Pauthier); Nanjing (Jiankang / Jiqing in Yuan times); Nanyang (Henan)
15. vughin | Vughin | Between Vuju (one day from Suju/Suzhou) and Changan (Jiaxing) (Bk II ch. 75) | Wujiang (Kingsmill/Yule); Wuxi; Huzhou-area towns
16. tanpiju | Tanpiju | First city after leaving Kinsay (Hangzhou) on the road to Fuju; one day's journey (Bk II ch. 79) | Shaoxing (Yule); Fuyang; Xiaoshan; Tonglu
17. changshan | Changshan | Four days on from Ghiuju (Quzhou); a hill dividing the waters (Bk II ch. 79) | Changshan county; Suichang (Cordier); the Xianxia pass on the Zhejiang–Fujian border
18. cuju | Cuju | Three days after Changshan; last city of the kingdom of Kinsay; six days to Kelinfu (Jian'ou) (Bk II ch. 79) | Chuzhou (Lishui) (Cordier); Pucheng (Fujian); Jiangshan; Quzhou (clash: already Ghiuju)
19. unken | Unken | City of sugar, refined by men from "Babylonia" (Egypt); a short way before Fuju (Fuzhou) (Bk II ch. 80) | Houguan / Minhou (Cordier: Hu-kwan); Minqing; Youxi; Yongfu; "Yongchun"

Volume III — the seas
20. cheinan | Gulf of Cheinan | Ramusio-only passage: a great gulf between Manzi and Chamba, two months' sail, many islands (Bk III, Yule ch. 4 note) | Gulf of Tonkin; Hainan waters (Hainan Dao); the Annam sea
21. locac | Locac | Kingdom about 500 miles beyond Sondur and Condur, south of Chamba; brazilwood, gold, elephants (Bk III ch. 7) | Lavo (Lopburi) via Chinese *Lo-hu*; Ligor (Nakhon Si Thammarat / Tambralinga); Langkasuka; Malay Peninsula generally; a Siam / Sukhothai confusion
22. malaiur | Malaiur | City on or near Pentam (Bintan), 500 miles south of Locac (Bk III ch. 8) | Malayu-Jambi; Dharmasraya; Melaka (anachronistic for 1290s?); Tumasik / Singapore; Palembang
23. dagroian | Dagroian | Kingdom of Java the Less (Sumatra) after Samara; cannibal funerary custom (Bk III ch. 10) | Pidie (Pedir); Nagur; Lide; Lamreh area; Tamiang

OUTPUT FORMAT
For each row, a short section with the fields above, then one summary table:
id | candidates (short) | preferred reading + who | plot? (point / region bounds / no) | coordinate + source | confidence.
End with "Sources consulted" (full references) and "Sources I could not open".
```

## Intake notes (for me)

- Change `id_confidence` from `disputed` to `probable` or `firm` only when the run gives a locator for a post-1950 source; otherwise record the candidates in `notes` and leave it.
- If a reading changes the point, update `latitude`/`longitude`, set `coord_check` (`wikipedia` if the new site has a Wikipedia point, else `approximate`), and log it in the chapter's backlog (the chapter may assert the old reading).
- Watch the two clashes flagged in the prompt (Tinju vs Sinju = Yizheng; Cuju vs Ghiuju = Quzhou).
