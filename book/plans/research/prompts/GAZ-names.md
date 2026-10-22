# Deep research prompt — place-name forms, pronunciation and reference links

Run in a deep-research tool. Save the output to `plans/research/results/GAZ-names-raw.md`, then bring it back for intake (it feeds `GAZ.T6`, the glossary `GLO`, and each chapter's naming pass).

```text
I am preparing a new English retelling of Marco Polo's *Il Milione* (base text: Yule–Cordier). I use ONE spelling per place in the prose (the "book form"), glossed once per chapter with a modern name (e.g. "Cascar (Kashgar)"). I want to decide each book form on evidence, add short notes on pronunciation and name origin, and link to online references.

Policy I want to test: the book form is the spelling Polo's English translators use (Yule), but where English readers overwhelmingly know a place by another name, the gloss or an alias covers it. Wikipedia's article title is my yardstick for "the most commonly used English name".

For every row below, return:
1. Book form check: is my book form the one Yule uses for Polo's name? Give Yule's chapter-heading spelling and the variants in Latham (Penguin 1958), Moule & Pelliot (1938), Pelliot's *Notes*, Ronald Latham, and Wikipedia's article on Marco Polo or the place. Mark any that I should change.
2. Wikipedia: the English Wikipedia article title for the modern place (and for the historical name if it has its own article) and the URL. If Wikipedia calls it something else than my modern_name, say so.
3. Name origin and meaning, one line (e.g. Persian, Mongol, Chinese original and its reading; "Cambaluc" = Turkic Khanbaliq 'city of the Khan'). Mark as certain / likely / speculative.
4. Pronunciation as an English reader should say it, as a plain respelling (e.g. "KAM-ba-luk") plus IPA if a reliable source gives one. Say which source. If scholars pronounce it two ways, give both.
5. Any trap: the same spelling meaning two places (Sinju, Vuju), a name used for a person and a place, or a Polo spelling that is really a manuscript error.

Specific questions:
- Chandu vs Shangdu/Xanadu; Kinsay vs Quinsay; Zayton vs Zaiton; Hormos vs Hormuz; Tauris vs Tabriz; Kisi vs Kish: which English spelling dominates in print and on Wikipedia, and which should be the book form for a general reader?
- Where Yule's spelling and the Latham/Penguin spelling differ, list both.
- Which names have a widely known English exonym that is NOT Polo's (e.g. Peking, Canton, Ceylon, Persia) and how Wikipedia treats them.

Rules: cite every claim; give URLs; do not invent pronunciations or etymologies; mark uncertainty. Prefer scholarly sources; use Wikipedia as the reference for current common usage, and say when Wikipedia itself disagrees with scholarship.

Rows (id | book form | aliases | modern name):
genoa | Genoa | Genova | Genoa, Italy
venice | Venice | Venezia | Venice, Italy
curzola | Curzola | Korčula | Korčula, Croatia
negropont | Negropont | Euboea;Chalkis | Chalkida (Euboea), Greece
constantinople | Constantinople | Istanbul | Istanbul, Turkey
soldaia | Soldaia | Soldaya;Sudak | Sudak, Crimea
sarai | Sarai | — | Sarai (near Selitrennoye), Russia
bolghar | Bolghar | Bolgar;Bulgar | Bolgar, Tatarstan, Russia
ucaca | Ucaca | Ukek;Uvek | Uvek (near Saratov), Russia
bocara | Bocara | Bokhara;Bukhara | Bukhara, Uzbekistan
acre | Acre | Akko;Acri | Acre (Akko), Israel
ayas | Ayas | Lajazzo;Laias;Layas;Yumurtalık | Yumurtalık (Ayas), Turkey
lesser-hermenia | Lesser Hermenia | Cilician Armenia;Little Armenia | Cilician Armenia, Turkey
greater-hermenia | Greater Hermenia | — | Armenian Highland (Turkey/Armenia)
turcomania | Turcomania | Turkmen;Anatolia | Central Anatolia, Turkey
conia | Conia | Konya;Iconium | Konya, Turkey
casaria | Casaria | Kayseri;Caesarea of Cappadocia | Kayseri, Turkey
savast | Savast | Sivas;Sebaste | Sivas, Turkey
arzinga | Arzinga | Erzingan;Erzincan | Erzincan, Turkey
arziron | Arziron | Erzrum;Erzurum | Erzurum, Turkey
arzizi | Arzizi | Arjish | Erciş (Arjish), by Lake Van, Turkey
ararat | Ararat | Ağrı Dağı;Mount Ararat | Mount Ararat, Turkey
baku | Baku | Bakı | Baku, Azerbaijan
derbend | Derbend | Derbent;Iron Gate | Derbent, Dagestan, Russia
georgiania | Georgiania | Georgia;Sakartvelo | Georgia (country)
mausul | Mausul | Mosul;al-Mawṣil | Mosul, Iraq
baudas | Baudas | Baghdad;Baghdād | Baghdad, Iraq
kisi | Kisi | Kis;Kish;Kais;Qays | Kish (Qays) Island, Iran
bastra | Bastra | Basra;al-Baṣra | Basra, Iraq
persia | Persia | Iran | Iran
tauris | Tauris | Tabriz;Tabrīz | Tabriz, Iran
saba | Saba | Sava;Saveh | Saveh, Iran
avah | Avah | Āvah;Ābeh | Āvah (Āveh), south of Saveh, Iran
kashan | Kashan | — | Kashan, Iran
yasdi | Yasdi | Yazd | Yazd, Iran
kerman | Kerman | Kirman;Kermān;Chirman | Kerman, Iran
camadi | Camadi | Kamadin | Kamadin (ruins, near Minab), Iran
reobarles | Reobarles | Rudbar;Rūdbār | Rudbar (Rudbari), Kerman, Iran
canosalmi | Canosalmi | — | —
hormos | Hormos | Hormuz;Hormes;Old Hormuz | Old Hormuz (near Minab), Iran
cobinan | Cobinan | Banan;Kuhbanan;Kuhbenān | Kuhbanan, Iran
tonocain | Tonocain | Tun and Kain;Tun-o-Kain;Kain;Qaen | Tun and Qāʾen, South Khorasan, Iran
arbre-sec | Arbre Sec | Dry Tree;Tree of the Sun;Arbor Secco | —
old-man-of-the-mountain | Old Man of the Mountain | Alamut;Mulehet | Alamut, Iran
sapurgan | Sapurgan | Shibarghan;Shibrgān;Shiburghan | Shibarghan, Afghanistan
balc | Balc | Balkh | Balkh, Afghanistan
taican | Taican | Talikan;Taloqan;Tāloqān | Taloqan, Afghanistan
casem | Casem | Kishm;Keshm;Krishma | Kishm (Keshem), Badakhshan, Afghanistan
dogana | Dogana | — | —
badashan | Badashan | Badakhshan;Balashan (wrong) | Badakhshan (Fayzabad area), Afghanistan
pashai | Pashai | Pashai;Pāshāʾī | Pashai country (Laghman–Kunar), Afghanistan
keshimur | Keshimur | Kashmir;Kāshmīr | Kashmir (valley), India
vocan | Vocan | Wakhan;Wakhān | Wakhan Corridor, Afghanistan
bolor | Bolor | Balur | Bolor (Gilgit–Chitral mountains)
pamier | Pamier | Pamir | Pamir Plateau (Tajikistan/Afghanistan)
cascar | Cascar | Kashgar;Kāshghar | Kashgar, Xinjiang, China
samarcan | Samarcan | Samarcand;Samarkand;Samarqand | Samarkand, Uzbekistan
yarcan | Yarcan | Yarkand;Yarkant | Yarkand (Yarkant), Xinjiang, China
cotan | Cotan | Khotan;Hotan;Ilchi | Hotan, Xinjiang, China
pein | Pein | Pem;Pen | Keriya / Uzun-Tati area, Xinjiang, China
charchan | Charchan | Ciarcian;Cherchen;Qiemo | Qiemo (Cherchen), Xinjiang, China
lop | Lop | Charklik;Ruoqiang | Charklik / Ruoqiang, Xinjiang, China
desert-of-lop | Desert of Lop | Lop Desert;Taklamakan;Great Desert | Lop Desert, Xinjiang, China
camul | Camul | Hami;Kumul | Hami, Xinjiang, China
chingintalas | Chingintalas | Chinchintalas | —
sachiu | Sachiu | Shachau;Dunhuang | Dunhuang, Gansu, China
sukchur | Sukchur | Succiu;Jiuquan | Jiuquan, Gansu, China
campichu | Campichu | Kanchau;Ganzhou;Zhangye | Zhangye, Gansu, China
etzina | Etzina | Khara-Khoto;Ejina;Edsina | Khara-Khoto (Ejina), Inner Mongolia, China
erguiul | Erguiul | Liangzhou;Wuwei | Wuwei (Liangzhou), Gansu, China
sinju-1 | Sinju | Xining;Sining | Xining, Qinghai, China
egrigaia | Egrigaia | Calachan;Ningxia;Yinchuan | Yinchuan (Ningxia), China
caracoron | Caracoron | Karakorum;Kharkhorin | Karakorum (Kharkhorin), Mongolia
bargu | Bargu | Barguzin;Baikal | Barguzin (Lake Baikal region), Russia
tenduc | Tenduc | Tumed;Hohhot | Tumed / Hohhot region, Inner Mongolia, China
chagannor | Chagannor | Chagan Nor;Chaghan Nor | —
chandu | Chandu | Shangdu;Xanadu;Kemenfu;Kaipingfu;Kaiping | Shangdu (Duolun County), Inner Mongolia, China
cambaluc | Cambaluc | Khanbaliq;Taidu;Dadu;Peking;Beijing | Beijing, China
prester-john | Prester John | Kingdom of Prester John | —
cathay | Cathay | Khitai;Kitai | North China (Yellow River basin)
pulisanghin | Pulisanghin | Lugou Bridge;Marco Polo Bridge | Lugou (Marco Polo) Bridge, Beijing, China
juju | Juju | Giogiu;Zhuozhou | Zhuozhou, Hebei, China
taianfu | Taianfu | Tainfu;Taiyuan | Taiyuan, Shanxi, China
caichu | Caichu | — | —
pianfu | Pianfu | Pingyang;Linfen | Linfen (Pingyang), Shanxi, China
caramoran | Caramoran | Qara Mören;Hwang Ho | Yellow River at Puzhou crossing, Shanxi, China
cachanfu | Cachanfu | Hezhong;Puchau;Puzhou;Pazanjin | Puzhou (Hezhong), Yongji, Shanxi, China
kenjanfu | Kenjanfu | Xi'an;Chang'an;Quengianfu | Xi'an, Shaanxi, China
cuncun | Cuncun | — | Qinling–Hanzhong mountains, Shaanxi, China
acbalec-manzi | Acbalec Manzi | — | Hanzhong area, Shaanxi, China
manzi | Manzi | Mangi;South China | South China (south of the Yangzi)
sindafu | Sindafu | Chengdu | Chengdu, Sichuan, China
tebet | Tebet | Tibet | Eastern Tibet / Kham region
caindu | Caindu | Kien-ch'ang;Jianchang;Xichang | Xichang (Jianchang valley), Sichuan, China
brius | Brius | Jinsha;Kin-sha Kiang | Jinsha River crossing, Yunnan–Sichuan, China
carajan | Carajan | Yunnan;Karajang | Yunnan (Dali / Kunming region), China
talifu | Talifu | Dali;Tali-fu | Dali, Yunnan, China
yachi | Yachi | Kunming | Kunming, Yunnan, China
vochan | Vochan | Yongchang;Baoshan | Baoshan (Yongchang), Yunnan, China
zardandan | Zardandan | Jinchi | Western Yunnan (Baoshan–Tengchong), China
mien | Mien | Burma;Pagan;Bagan | Bagan / Myanmar (Pagan kingdom)
bangala | Bangala | Bengal;Pegu | —
caugigu | Caugigu | Kiaochi;Kiang Hung;Tonkin;Jiaozhi | Kiang Hung (Jinghong), Yunnan, China
anin | Anin | Aniu;Lin-ngan;Jianshui | Jianshui (Lin-ngan), Yunnan, China
coloman | Coloman | Toloman | Guizhou / Guangxi border region, China
cuiju | Cuiju | Kweichau;Guizhou;Guiyang | Guiyang area, Guizhou, China
fungul | Fungul | Phungan-lu;Siu-chau;Suifu;Yibin | Yibin (Suifu), Sichuan, China
cacanfu | Cacanfu | Hejian;Ho-kien-fu | Hejian, Hebei, China
changlu | Changlu | Ciangu;Cangzhou;Ch'ang-lu | Cangzhou, Hebei, China
chinangli | Chinangli | Jinan;Tsinan | Jinan, Shandong, China
tadinfu | Tadinfu | Yanzhou;Yen-chau | Yanzhou, Shandong, China
sinjumatu | Sinjumatu | Jining;Tsi-ning | Jining, Shandong, China
linju | Linju | Lingiu;Linqing;Lin-ch'ing | Linqing, Shandong, China
piju | Piju | Pizhou;Pei-chau | Pizhou, Jiangsu, China
siju | Siju | Suqian;Su-t'sien;Si-chau | Suqian, Jiangsu, China
coiganju | Coiganju | Huai'an;Hwai-ngan | Huai'an, Jiangsu, China
paukin | Paukin | Baoying;Pao-ying | Baoying, Jiangsu, China
cayu | Cayu | Gaoyou;Kao-yu | Gaoyou, Jiangsu, China
tiju | Tiju | Taizhou;Tai-chau | Taizhou, Jiangsu, China
tinju | Tinju | Tung-chau;Nantong;I-chin | Nantong (Tung-chau), Jiangsu, China
yanju | Yanju | Yangiu;Yangzhou | Yangzhou, Jiangsu, China
nanghin | Nanghin | Ngan-king;Anqing;Nanjing | Anqing (Ngan-king), Anhui, China
saianfu | Saianfu | Xiangyang | Xiangyang, Hubei, China
sinju-2 | Sinju | Yizheng;I-ching;Chen-chau | Yizheng, Jiangsu, China
caiju | Caiju | Kwa-chau;Guazhou | Guazhou, Jiangsu, China
chinghianfu | Chinghianfu | Zhenjiang;Chin-kiang | Zhenjiang, Jiangsu, China
chinginju | Chinginju | Changzhou;Chang-chau | Changzhou, Jiangsu, China
suju | Suju | Suzhou | Suzhou, Jiangsu, China
vuju-1 | Vuju | Huzhou;Hu-chau;Wuchu | Huzhou, Zhejiang, China
vughin | Vughin | Wujiang;Wukiang | Wujiang, Jiangsu, China
changan | Changan | Jiaxing;Kiahing;Ciangan | Jiaxing, Zhejiang, China
kinsay | Kinsay | Quinsay;Hangzhou;Lin'an | Hangzhou, Zhejiang, China
ganfu | Ganfu | Ganpu;Kanp'u;Haiyan | Ganpu (Haiyan area), Zhejiang, China
tanpiju | Tanpiju | Shaoxing;Fu-yang | Shaoxing, Zhejiang, China
vuju-2 | Vuju | Wuzhou;Wu-chau;Jinhua;Kin-hwa | Jinhua (Wuzhou), Zhejiang, China
ghiuju | Ghiuju | Quzhou;K'iu-chau | Quzhou, Zhejiang, China
changshan | Changshan | Chan-shan;Suichang | Changshan, Zhejiang, China
cuju | Cuju | Chuzhou;Ch'u-chau | —
kelinfu | Kelinfu | Jianning;Kien-ning;Jian'ou | Jian'ou (Kien-ning), Fujian, China
unken | Unken | Hu-kwan;Huguan | Minhou (Hu-kwan), Fujian, China
fuju | Fuju | Fuzhou | Fuzhou, Fujian, China
zayton | Zayton | Zaiton;Quanzhou;Chinchew;Zaitun | Quanzhou, Fujian, China
tyunju | Tyunju | Tek-hwa;Dehua | Dehua, Fujian, China
rosia | Rosia | Russia;Rus' | Russia (Rus' lands)
cauly | Cauly | Kaoli;Korea | Korea
chorcha | Chorcha | Jurchen;Manchuria | Manchuria, China
cachar-modun | Cachar Modun | — | —
chipangu | Chipangu | Cipangu;Japan | Japan
cheinan | Gulf of Cheinan | Cheinan;Hainan | Gulf of Tonkin, China/Vietnam
chamba | Chamba | Champa | Central Vietnam (Champa coast)
java | Java | — | Java, Indonesia
sondur | Sondur | — | —
condur | Condur | Pulo Condore;Con Dao | Pulo Condore (Côn Đảo), Vietnam
locac | Locac | — | Malay Peninsula (southern Thailand/Malaysia)
pentam | Pentam | Bintan;Riau | Bintan / Riau Islands, Indonesia
malaiur | Malaiur | Malayu;Melaka | Melaka / Sumatra Malay coast
gauenispola | Gauenispola | — | —
java-the-less | Java the Less | Java Minor;Sumatra | Sumatra, Indonesia
ferlec | Ferlec | Perlak;Perlak | Perlak, Aceh, Sumatra, Indonesia
basma | Basma | Basman;Pasai | Pasai / NE Sumatra coast, Indonesia
samara | Samara | Samudra;Samudera Pasai | Samudera Pasai, Sumatra, Indonesia
dagroian | Dagroian | — | NE Sumatra coastal polity
lambri | Lambri | Lamuri | Lamuri (Aceh headland), Sumatra, Indonesia
fansur | Fansur | Barus | Barus, NW Sumatra, Indonesia
necuveran | Necuveran | Nicobar;Nicobars | Nicobar Islands, India
angamanain | Angamanain | Andaman | Andaman Islands, India
seilan | Seilan | Ceylon;Sri Lanka | Sri Lanka
maabar | Maabar | Coromandel;Ma'bar | Coromandel Coast (Tamil Nadu), India
mailapur | Mailapur | Mylapore | Mylapore (Chennai), India
soli | Soli | Chola;Soḷadeśam | Chola country (Thanjavur area), India
mutfili | Mutfili | Motupalli | Motupalli, Andhra Pradesh, India
lar | Lar | Lata | —
cail | Cail | Kayal;Kayalpatnam | Kayalpatnam / Old Kayal, Tamil Nadu, India
coilum | Coilum | Quilon;Kollam | Kollam, Kerala, India
comari | Comari | Cape Comorin;Kanyakumari | Kanyakumari (Cape Comorin), India
eli | Eli | Mount Eli;Ezhimala;Deli | Mount Eli / Ezhimala, Kerala, India
melibar | Melibar | Malabar | Malabar Coast, Kerala, India
gozurat | Gozurat | Gujarat | Gujarat, India
tana | Tana | Thane | Thane, Maharashtra, India
cambaet | Cambaet | Cambay;Khambhat | Khambhat (Cambay), Gujarat, India
semenat | Semenat | Sememant;Somnath | Somnath area, Gujarat, India
kesmacoran | Kesmacoran | Makran;Kij-Makran | Makran coast (Gwadar/Pasni area), Pakistan
male-and-female | Male and Female | Island of Women;Island of Men;Islands of Men and Women;Male | —
scotra | Scotra | Socotra | Socotra, Yemen
madeigascar | Madeigascar | Madagascar | Madagascar
magadoxo | Magadoxo | Mogadishu;Mogadiscio | Mogadishu, Somalia
zanghibar | Zanghibar | Zanzibar;Zanj | Zanzibar / Swahili coast, Tanzania
abash | Abash | Abyssinia;Ḥabash | Ethiopian highlands
aden | Aden | ʿAdan | Aden, Yemen
esher | Esher | Escier;Shihr;ash-Shiḥr | Ash-Shihr, Yemen
dufar | Dufar | Dofar;Dhofar;Dhafār | Dhofar (Salalah area), Oman
calatu | Calatu | Kalhat;Qalhāt | Qalhat, Oman
soer | Soer | Sohar | Sohar, Oman
abhar | Abhar | — | Abhar, Zanjan, Iran
trebizond | Trebizond | Trabzon | Trabzon, Turkey

Output: one Markdown table (id | Yule's form | other forms | Wikipedia URL | origin | respelling | IPA/source | trap), then a short list of recommended book-form changes with a reason each.
```

## Intake notes (for me)
- Add `wikipedia` and `pron` columns to `gazetteer.csv` only if the data is solid; otherwise put the line in `notes`.
- Pronunciation and origin notes belong in the volume glossary (`GLO`), with one Wikipedia link per entry; chapters stay clean.
- Any book-form change must update `aliases`, the chapters column and the name-diff report (`python3 tools/gazetteer.py chapters`).
