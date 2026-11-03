# Deep research prompt — verify gazetteer coordinates and identifications

Run in a deep-research tool. Save the output to `plans/research/results/GAZ-coords-raw.md`, then bring it back for intake (`GAZ.T6`).

```text
I am building a gazetteer for a new English retelling of Marco Polo's *Il Milione* (base text: Yule–Cordier, 1903/1920). Below are place rows with my current modern identification and a coordinate. I need each one VERIFIED or CORRECTED against independent sources.

For every row, return:
1. Verdict: CONFIRMED / CORRECTED / STILL DISPUTED / NO FIX POSSIBLE.
2. Best current modern identification and the coordinate (decimal degrees, 4 places) of the site a map should plot (city centre, ruin site, river crossing or region centroid — say which).
3. If disputed: the main candidates, who argues for each (author, year), and which one the majority of recent scholarship prefers.
4. Sources: at least one source that is NOT Yule/Cordier (e.g. Pelliot's *Notes on Marco Polo*, Moule & Pelliot 1938, Ronald Latham, Hans Ulrich Vogel, Stephen Haw, Frances Wood, Peter Jackson, Jean Richard, UNESCO/archaeological reports, Wikipedia/Wikidata for modern coordinates). Give a URL for every Wikipedia or Wikidata page used, with its coordinates.
5. Spelling: the form most used in English scholarship today for the name Polo wrote (not the modern place), if it differs from my "book_name".

Rules: Do not guess. If a coordinate cannot be sourced, say so and give the region and its approximate bounds instead. Separate what a source states from your inference. Flag any row where my modern name is actually a different place from the one Polo means. Do not invent citations; if unsure whether a work says something, say "unverified".

Priority group A (my confidence is not "firm"; verify all in detail):
sarai | Sarai | Sarai (near Selitrennoye), Russia | 47.1833, 47.4500 | probable | vol 1
ucaca | Ucaca | Uvek (near Saratov), Russia | 51.4000, 46.1000 | probable | vol 1
turcomania | Turcomania | Central Anatolia, Turkey | 38.5000, 33.5000 | probable | vol 1
arzizi | Arzizi | Erciş (Arjish), by Lake Van, Turkey | 38.9833, 43.3667 | probable | vol 1
avah | Avah | Āvah (Āveh), south of Saveh, Iran | 34.8200, 50.4500 | probable | vol 1
kashan | Kashan | Kashan, Iran | 33.9850, 51.4100 | probable | vol 1
camadi | Camadi | Kamadin (ruins, near Minab), Iran | 27.3500, 57.0500 | probable | vol 1
reobarles | Reobarles | Rudbar (Rudbari), Kerman, Iran | 28.2700, 57.7800 | probable | vol 1
canosalmi | Canosalmi | — | —, — | unfixed | vol 1
tonocain | Tonocain | Tun and Qāʾen, South Khorasan, Iran | 33.7267, 59.1844 | probable | vol 1
arbre-sec | Arbre Sec | — | —, — | unfixed | vol 1
old-man-of-the-mountain | Old Man of the Mountain | Alamut, Iran | 36.4447, 50.5864 | probable | vol 1
casem | Casem | Kishm (Keshem), Badakhshan, Afghanistan | 36.8000, 70.9000 | probable | vol 1
dogana | Dogana | — | —, — | unfixed | vol 1
pashai | Pashai | Pashai country (Laghman–Kunar), Afghanistan | 34.8000, 70.4000 | probable | vol 1
bolor | Bolor | Bolor (Gilgit–Chitral mountains) | 36.0000, 74.5000 | disputed | vol 1
pein | Pein | Keriya / Uzun-Tati area, Xinjiang, China | 37.0000, 81.6000 | disputed | vol 1
lop | Lop | Charklik / Ruoqiang, Xinjiang, China | 39.0236, 88.1681 | probable | vol 1
chingintalas | Chingintalas | — | —, — | unfixed | vol 1
erguiul | Erguiul | Wuwei (Liangzhou), Gansu, China | 37.9280, 102.6380 | probable | vol 1
egrigaia | Egrigaia | Yinchuan (Ningxia), China | 38.4872, 106.2309 | probable | vol 1
bargu | Bargu | Barguzin (Lake Baikal region), Russia | 53.6200, 109.6300 | probable | vol 1
tenduc | Tenduc | Tumed / Hohhot region, Inner Mongolia, China | 40.8414, 111.7519 | disputed | vol 1
chagannor | Chagannor | — | —, — | unfixed | vol 1
prester-john | Prester John | — | —, — | unfixed | vol 1
cathay | Cathay | North China (Yellow River basin) | 37.0000, 114.0000 | probable | vol 2
caichu | Caichu | — | —, — | unfixed | vol 2
pianfu | Pianfu | Linfen (Pingyang), Shanxi, China | 36.0880, 111.5190 | probable | vol 2
caramoran | Caramoran | Yellow River at Puzhou crossing, Shanxi, China | 34.8500, 110.3000 | probable | vol 2
cachanfu | Cachanfu | Puzhou (Hezhong), Yongji, Shanxi, China | 34.8700, 110.4500 | probable | vol 2
cuncun | Cuncun | Qinling–Hanzhong mountains, Shaanxi, China | 33.6000, 107.3000 | disputed | vol 2
acbalec-manzi | Acbalec Manzi | Hanzhong area, Shaanxi, China | 33.0700, 107.0200 | disputed | vol 2
manzi | Manzi | South China (south of the Yangzi) | 28.0000, 115.0000 | probable | vol 2
tebet | Tebet | Eastern Tibet / Kham region | 30.0000, 97.0000 | probable | vol 2
caindu | Caindu | Xichang (Jianchang valley), Sichuan, China | 27.8942, 102.2644 | probable | vol 2
brius | Brius | Jinsha River crossing, Yunnan–Sichuan, China | 26.1000, 101.6000 | probable | vol 2
carajan | Carajan | Yunnan (Dali / Kunming region), China | 25.0000, 101.5000 | probable | vol 2
vochan | Vochan | Baoshan (Yongchang), Yunnan, China | 25.1204, 99.1675 | probable | vol 2
zardandan | Zardandan | Western Yunnan (Baoshan–Tengchong), China | 25.0000, 99.0000 | probable | vol 2
mien | Mien | Bagan / Myanmar (Pagan kingdom) | 21.1717, 94.8580 | probable | vol 2
bangala | Bangala | — | —, — | disputed | vol 2
caugigu | Caugigu | Kiang Hung (Jinghong), Yunnan, China | 22.0097, 100.7971 | disputed | vol 2
anin | Anin | Jianshui (Lin-ngan), Yunnan, China | 23.6300, 102.8300 | disputed | vol 2
coloman | Coloman | Guizhou / Guangxi border region, China | 26.0000, 107.0000 | disputed | vol 2
cuiju | Cuiju | Guiyang area, Guizhou, China | 26.6470, 106.6302 | disputed | vol 2
fungul | Fungul | Yibin (Suifu), Sichuan, China | 28.7513, 104.6417 | disputed | vol 2
cacanfu | Cacanfu | Hejian, Hebei, China | 38.4440, 116.0900 | probable | vol 2
changlu | Changlu | Cangzhou, Hebei, China | 38.3037, 116.8387 | probable | vol 2
chinangli | Chinangli | Jinan, Shandong, China | 36.6512, 117.1201 | probable | vol 2
tadinfu | Tadinfu | Yanzhou, Shandong, China | 35.5530, 116.8450 | probable | vol 2
sinjumatu | Sinjumatu | Jining, Shandong, China | 35.4147, 116.5874 | probable | vol 2
linju | Linju | Linqing, Shandong, China | 36.8527, 115.7010 | disputed | vol 2
piju | Piju | Pizhou, Jiangsu, China | 34.3100, 117.9500 | probable | vol 2
siju | Siju | Suqian, Jiangsu, China | 33.9633, 118.2753 | probable | vol 2
coiganju | Coiganju | Huai'an, Jiangsu, China | 33.5975, 119.0140 | probable | vol 2
paukin | Paukin | Baoying, Jiangsu, China | 33.2400, 119.3100 | probable | vol 2
cayu | Cayu | Gaoyou, Jiangsu, China | 32.7850, 119.4400 | probable | vol 2
tiju | Tiju | Taizhou, Jiangsu, China | 32.4550, 119.9230 | probable | vol 2
tinju | Tinju | Nantong (Tung-chau), Jiangsu, China | 31.9800, 120.8940 | disputed | vol 2
nanghin | Nanghin | Anqing (Ngan-king), Anhui, China | 30.5430, 117.0630 | disputed | vol 2
sinju-2 | Sinju | Yizheng, Jiangsu, China | 32.2700, 119.1800 | probable | vol 2
vuju-1 | Vuju | Huzhou, Zhejiang, China | 30.8670, 120.0900 | probable | vol 2
vughin | Vughin | Wujiang, Jiangsu, China | 31.1600, 120.6400 | disputed | vol 2
changan | Changan | Jiaxing, Zhejiang, China | 30.7522, 120.7500 | probable | vol 2
tanpiju | Tanpiju | Shaoxing, Zhejiang, China | 30.0000, 120.5800 | disputed | vol 2
vuju-2 | Vuju | Jinhua (Wuzhou), Zhejiang, China | 29.0790, 119.6470 | probable | vol 2
ghiuju | Ghiuju | Quzhou, Zhejiang, China | 28.9360, 118.8680 | probable | vol 2
changshan | Changshan | Changshan, Zhejiang, China | 28.9020, 118.5070 | disputed | vol 2
cuju | Cuju | — | —, — | disputed | vol 2
kelinfu | Kelinfu | Jian'ou (Kien-ning), Fujian, China | 27.0350, 118.3200 | probable | vol 2
unken | Unken | Minhou (Hu-kwan), Fujian, China | 26.1500, 119.1500 | disputed | vol 2
tyunju | Tyunju | Dehua, Fujian, China | 25.4900, 118.2400 | probable | vol 2
rosia | Rosia | Russia (Rus' lands) | 57.0000, 40.0000 | probable | vol 2
chorcha | Chorcha | Manchuria, China | 44.0000, 126.0000 | probable | vol 2
cachar-modun | Cachar Modun | — | —, — | unfixed | vol 2
cheinan | Gulf of Cheinan | Gulf of Tonkin, China/Vietnam | 20.0000, 108.0000 | disputed | vol 3
chamba | Chamba | Central Vietnam (Champa coast) | 13.5000, 109.2000 | probable | vol 3
sondur | Sondur | — | —, — | unfixed | vol 3
condur | Condur | Pulo Condore (Côn Đảo), Vietnam | 8.6900, 106.6100 | probable | vol 3
locac | Locac | Malay Peninsula (southern Thailand/Malaysia) | 7.0000, 100.0000 | disputed | vol 3
pentam | Pentam | Bintan / Riau Islands, Indonesia | 1.1500, 104.5000 | probable | vol 3
malaiur | Malaiur | Melaka / Sumatra Malay coast | 2.2000, 102.2500 | disputed | vol 3
gauenispola | Gauenispola | — | —, — | unfixed | vol 3
basma | Basma | Pasai / NE Sumatra coast, Indonesia | 5.1000, 97.2000 | probable | vol 3
dagroian | Dagroian | NE Sumatra coastal polity | 4.5000, 98.0000 | disputed | vol 3
soli | Soli | Chola country (Thanjavur area), India | 10.7800, 79.1400 | probable | vol 3
mutfili | Mutfili | Motupalli, Andhra Pradesh, India | 15.5800, 80.3000 | probable | vol 3
lar | Lar | — | —, — | unfixed | vol 3
semenat | Semenat | Somnath area, Gujarat, India | 20.8880, 70.4010 | probable | vol 3
male-and-female | Male and Female | — | —, — | unfixed | vol 3
madeigascar | Madeigascar | Madagascar | -18.7669, 46.8691 | probable | vol 3
zanghibar | Zanghibar | Zanzibar / Swahili coast, Tanzania | -6.1659, 39.2026 | probable | vol 3
soer | Soer | Sohar, Oman | 24.3500, 56.7100 | probable | vol 3

Group B (I believe these are firm; spot-check coordinates only — flag any that are more than ~15 km off, or are the wrong place):
genoa | Genoa | Genoa, Italy | 44.4056, 8.9463
venice | Venice | Venice, Italy | 45.4408, 12.3155
curzola | Curzola | Korčula, Croatia | 42.9597, 17.1357
negropont | Negropont | Chalkida (Euboea), Greece | 38.4636, 23.5985
constantinople | Constantinople | Istanbul, Turkey | 41.0082, 28.9784
soldaia | Soldaia | Sudak, Crimea | 44.8500, 34.9667
bolghar | Bolghar | Bolgar, Tatarstan, Russia | 54.9833, 49.0500
bocara | Bocara | Bukhara, Uzbekistan | 39.7747, 64.4286
acre | Acre | Acre (Akko), Israel | 32.9269, 35.0818
ayas | Ayas | Yumurtalık (Ayas), Turkey | 36.7667, 35.7833
lesser-hermenia | Lesser Hermenia | Cilician Armenia, Turkey | 37.0000, 35.4000
greater-hermenia | Greater Hermenia | Armenian Highland (Turkey/Armenia) | 39.8000, 42.5000
conia | Conia | Konya, Turkey | 37.8746, 32.4932
casaria | Casaria | Kayseri, Turkey | 38.7312, 35.4787
savast | Savast | Sivas, Turkey | 39.7477, 37.0179
arzinga | Arzinga | Erzincan, Turkey | 39.7500, 39.5000
arziron | Arziron | Erzurum, Turkey | 39.9043, 41.2679
ararat | Ararat | Mount Ararat, Turkey | 39.7020, 44.2982
baku | Baku | Baku, Azerbaijan | 40.4093, 49.8671
derbend | Derbend | Derbent, Dagestan, Russia | 42.0575, 48.2886
georgiania | Georgiania | Georgia (country) | 42.0000, 44.0000
mausul | Mausul | Mosul, Iraq | 36.3400, 43.1300
baudas | Baudas | Baghdad, Iraq | 33.3152, 44.3661
kisi | Kisi | Kish (Qays) Island, Iran | 26.5575, 53.9803
bastra | Bastra | Basra, Iraq | 30.5085, 47.7804
persia | Persia | Iran | 32.0000, 54.0000
tauris | Tauris | Tabriz, Iran | 38.0962, 46.2738
saba | Saba | Saveh, Iran | 35.0214, 50.3566
yasdi | Yasdi | Yazd, Iran | 31.8974, 54.3569
kerman | Kerman | Kerman, Iran | 30.2839, 57.0834
hormos | Hormos | Old Hormuz (near Minab), Iran | 27.1000, 56.4500
cobinan | Cobinan | Kuhbanan, Iran | 31.4100, 56.2800
sapurgan | Sapurgan | Shibarghan, Afghanistan | 36.6650, 65.7520
balc | Balc | Balkh, Afghanistan | 36.7581, 66.8986
taican | Taican | Taloqan, Afghanistan | 36.7361, 69.5345
badashan | Badashan | Badakhshan (Fayzabad area), Afghanistan | 37.1167, 70.5800
keshimur | Keshimur | Kashmir (valley), India | 34.0837, 74.7973
vocan | Vocan | Wakhan Corridor, Afghanistan | 37.0000, 73.0000
pamier | Pamier | Pamir Plateau (Tajikistan/Afghanistan) | 38.5000, 73.5000
cascar | Cascar | Kashgar, Xinjiang, China | 39.4704, 75.9898
samarcan | Samarcan | Samarkand, Uzbekistan | 39.6270, 66.9750
yarcan | Yarcan | Yarkand (Yarkant), Xinjiang, China | 38.4167, 77.2500
cotan | Cotan | Hotan, Xinjiang, China | 37.1100, 79.9300
charchan | Charchan | Qiemo (Cherchen), Xinjiang, China | 38.1333, 85.5333
desert-of-lop | Desert of Lop | Lop Desert, Xinjiang, China | 40.0000, 90.0000
camul | Camul | Hami, Xinjiang, China | 42.8333, 93.5000
sachiu | Sachiu | Dunhuang, Gansu, China | 40.1421, 94.6620
sukchur | Sukchur | Jiuquan, Gansu, China | 39.7333, 98.5000
campichu | Campichu | Zhangye, Gansu, China | 38.9333, 100.4500
etzina | Etzina | Khara-Khoto (Ejina), Inner Mongolia, China | 41.7667, 101.1500
sinju-1 | Sinju | Xining, Qinghai, China | 36.6171, 101.7782
caracoron | Caracoron | Karakorum (Kharkhorin), Mongolia | 47.1978, 102.8208
chandu | Chandu | Shangdu (Duolun County), Inner Mongolia, China | 42.3581, 116.1850
cambaluc | Cambaluc | Beijing, China | 39.9042, 116.4074
pulisanghin | Pulisanghin | Lugou (Marco Polo) Bridge, Beijing, China | 39.8492, 116.2156
juju | Juju | Zhuozhou, Hebei, China | 39.4850, 115.9740
taianfu | Taianfu | Taiyuan, Shanxi, China | 37.8706, 112.5489
kenjanfu | Kenjanfu | Xi'an, Shaanxi, China | 34.3416, 108.9398
sindafu | Sindafu | Chengdu, Sichuan, China | 30.5728, 104.0668
talifu | Talifu | Dali, Yunnan, China | 25.6065, 100.2676
yachi | Yachi | Kunming, Yunnan, China | 25.0389, 102.7183
yanju | Yanju | Yangzhou, Jiangsu, China | 32.3942, 119.4120
saianfu | Saianfu | Xiangyang, Hubei, China | 32.0100, 112.1400
caiju | Caiju | Guazhou, Jiangsu, China | 32.2500, 119.4200
chinghianfu | Chinghianfu | Zhenjiang, Jiangsu, China | 32.1892, 119.4250
chinginju | Chinginju | Changzhou, Jiangsu, China | 31.8100, 119.9740
suju | Suju | Suzhou, Jiangsu, China | 31.2989, 120.5853
kinsay | Kinsay | Hangzhou, Zhejiang, China | 30.2741, 120.1551
ganfu | Ganfu | Ganpu (Haiyan area), Zhejiang, China | 30.4000, 120.9000
fuju | Fuju | Fuzhou, Fujian, China | 26.0745, 119.2965
zayton | Zayton | Quanzhou, Fujian, China | 24.9139, 118.5858
cauly | Cauly | Korea | 37.0000, 127.5000
chipangu | Chipangu | Japan | 35.0000, 136.0000
java | Java | Java, Indonesia | -7.5000, 110.0000
java-the-less | Java the Less | Sumatra, Indonesia | 0.5000, 101.5000
ferlec | Ferlec | Perlak, Aceh, Sumatra, Indonesia | 4.8000, 97.6000
samara | Samara | Samudera Pasai, Sumatra, Indonesia | 5.1667, 97.1667
lambri | Lambri | Lamuri (Aceh headland), Sumatra, Indonesia | 5.5500, 95.3000
fansur | Fansur | Barus, NW Sumatra, Indonesia | 2.0000, 98.4000
necuveran | Necuveran | Nicobar Islands, India | 7.5000, 93.7000
angamanain | Angamanain | Andaman Islands, India | 12.5000, 92.8000
seilan | Seilan | Sri Lanka | 7.8731, 80.7718
maabar | Maabar | Coromandel Coast (Tamil Nadu), India | 10.8000, 79.8000
mailapur | Mailapur | Mylapore (Chennai), India | 13.0338, 80.2698
cail | Cail | Kayalpatnam / Old Kayal, Tamil Nadu, India | 8.6667, 78.0667
coilum | Coilum | Kollam, Kerala, India | 8.8932, 76.6141
comari | Comari | Kanyakumari (Cape Comorin), India | 8.0883, 77.5385
eli | Eli | Mount Eli / Ezhimala, Kerala, India | 12.0000, 75.2000
melibar | Melibar | Malabar Coast, Kerala, India | 11.2500, 75.7800
gozurat | Gozurat | Gujarat, India | 22.2587, 71.1924
tana | Tana | Thane, Maharashtra, India | 19.2183, 72.9781
cambaet | Cambaet | Khambhat (Cambay), Gujarat, India | 22.3000, 72.6200
kesmacoran | Kesmacoran | Makran coast (Gwadar/Pasni area), Pakistan | 25.1500, 62.3500
scotra | Scotra | Socotra, Yemen | 12.5000, 53.8000
magadoxo | Magadoxo | Mogadishu, Somalia | 2.0469, 45.3182
abash | Abash | Ethiopian highlands | 9.1450, 40.4897
aden | Aden | Aden, Yemen | 12.7855, 45.0187
esher | Esher | Ash-Shihr, Yemen | 14.7600, 49.6000
dufar | Dufar | Dhofar (Salalah area), Oman | 17.0151, 54.0924
calatu | Calatu | Qalhat, Oman | 22.7000, 59.3700
abhar | Abhar | Abhar, Zanjan, Iran | 36.1466, 49.2186
trebizond | Trebizond | Trabzon, Turkey | 41.0027, 39.7168

Output format: one Markdown table per group (id | verdict | modern name | lat, lon | what the point is | sources), then a short "Disagreements with Yule" section, then a list of rows you could not verify.
```
