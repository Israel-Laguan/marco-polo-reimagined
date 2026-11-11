# Intake: S-13 follow-up (five narrow questions)

_2026-11-11. Raw runs: `S-13-followup-raw-consensus.md` and `S-13-followup-raw-qwen.md` (both run by the user; prompt in `spikes/S-13-scholarship-update.md` § Follow-up prompts). Applies to `registry/scholarship.md` Q1, Q3, Q7, Q10 and the departure date._

## Trust check

**Consensus: passes. Qwen: fails (about 3 of 9 checked claims hold). Use Consensus as a set of leads that have now been checked; use nothing from Qwen.**

### Consensus

All seven works it cites exist (Crossref). It answers "not found" where it has no passage, which is what the prompt asked for.

| Run says | Check | OK? |
|---|---|---|
| Mascherpa, "Sulla fonte Z del *Milione* di Ramusio", *Quaderni Veneti* | Crossref: vol. 6, no. 2 (dated December 2017, published 26 Nov 2018), doi:10.30687/qv/1724-188x/2017/02/003. Open-access PDF read; its footer gives pp. 45–64 | yes |
| Mascherpa p. 46: Benedetto saw Z as translating a text close to the Genoa original, later pruned into the ancestor of the rest | read on p. 46 | yes |
| Mascherpa p. 46 n. 3: Benedetto 1928, CLXXXII, and Terracini 1933, 409–20, on V and L as intermediate stages | read | yes |
| Mascherpa p. 50: the chapters on the plain between Qamadin and Hormuz are re-ordered (F XXXV–XXXVI; R I 14–16; Z 13–14) | read on p. 50 | yes |
| Mascherpa p. 62: notes and memories on Quinsai, later worked into one or more Z copies, "with or without his supervision" | read on p. 62 | yes |
| Andreose, «… io essendo giovanetto…», abstract: the additions are Polo's reworking | Crossref abstract; PDF opened (pp. 31–44) | yes |
| Lin and Zhang (2017): the envoys' names are in the *Yongle dadian* (citing Yang and Ho 1945, Cleaves 1976); departure late 1290 or very early 1291; stops Malacca, Mabar, Hormuz | Crossref: *European Journal of Archaeology* 21/1, 39–56, doi:10.1017/eaa.2017.21. Article page read through a fetch summary: all three points confirmed; Champa is not mentioned. The second author's family name is Zhang (Zhang Ran), not "Ran" | yes |
| Haw 2020, abstract (Persian; pepper) | matches the Crossref abstract | yes |
| Haw, "Marco Polo's Departure from China" (2023) exists | Crossref: *ZDMG* 173/1 (2023), 145–171, doi:10.13173/zdmg.173.1.145. **New to the registry**; no abstract; not read | yes |
| Magone's review of Vogel (2015); Haw's review of Cliff (2016) | Crossref records. Their contents (Vogel pp. 291–295; "Singiu") not checked | exists |

### Qwen

Eighty-odd links, mostly to aggregator copies (dokumen.pub, academia.edu, bookrags, enotes). It writes "highly probable", "plausible" and "it is possible to infer" where the prompt asked for "not found".

| Run says | Check | OK? |
|---|---|---|
| Yule's theory: the Polos sailed from Hormuz (to Basra, or to China) | **Backwards.** Yule: they meant to take ship and had to "abandon this project and turn north again from Hormuz" (`yc`, refs/yule-vol1.txt:5907). The prompt itself said so | no |
| Larner criticised Yule's Hormuz reconstruction | The link is to Akbari and Iannucci (eds.), *Marco Polo and the Encounter of East and West*, not to Larner; the table gives Larner's work as "Not Specified" | not shown |
| Sykes proposed a route that avoids Baghdad | Real, but it is Cordier's note of 1903 (`yc`, refs/yule-vol1.txt:16363): Sykes thinks the Polos entered Persia near Tabriz and went by Sultania, Kashan and Yezd to Kerman and Hormuz. Pre-2000, and not about the turn-back | exists; off the question |
| Haw (2006) argues the first Champa mention is an earlier visit of about 1285, not a call in 1291 | The links are to Olschki's *Marco Polo's Asia* and to a book on Franciscan martyrs. The 1285 visit is the Book's own statement, and Yule already tied it to an earlier mission (below) | no |
| The notice is in juan 19,418 of the *Yongle dadian*, not in the *Yuan shi* | The source name agrees with Lin and Zhang. The juan number, "a report from the governor of Quanzhou" and "third month of Zhiyuan 27" are not confirmed | partly |
| Cleaves (1976) and Vogel (2013) date the sailing to June/July 1291 | The JSTOR link is not Cleaves's article (his is doi:10.2307/2718743). Two sources that were read give late 1290 or early 1291 (Ma 2025; Lin and Zhang 2017). No source for June/July | no |
| Andreose: the single-redaction arguments are "compelling, but far from … satisfactory" | The sentence is real (`andreose2024textual`, p. 73, read) | yes |
| The Book was translated "from the original Italian (Venetian) into Medieval French" | Against `andreose2024textual`: the original was Franco-Italian; the Venetian-original thesis is Wehr's and is rejected | no |
| Haw's 2024 article: a full account of its claims and targets | Inference from his other work, by the run's own words. It calls a 2024 article "forthcoming" | no |

## What the intake saw

| Question | Seen | Source |
|---|---|---|
| **5. Single redaction: who?** | Answered from the notes of Andreose's 2024 chapter, which the main run had already opened. For the authenticity and original presence of the Z and R additions he cites Casella (1929), Benedetto (1930), Peretti (1930), Terracini (1933), Pasquali (1952) and Barbieri (2004). He adds that "a few scholars deny the authenticity of some or all the additions" and treat them as late interpolations: Dieu (1947), Reichert (1997). Mascherpa (2018, p. 46) states Benedetto's model in full. No living proponent who has answered the Venice school was found by either run | `andreose2024textual` (read, pp. 72–73 and notes); `mascherpa2018fonte` (read) |
| **3. Source of the 1290 notice** | *Yongle dadian*, as F-15 has it. Ma 2025's "in the *Yuanshi*" is the slip | Lin and Zhang 2017 (summary), citing Yang and Ho 1945 and Cleaves 1976 |
| **3. Sailing date** | Late 1290 or very early 1291, a second time. What Cleaves, Vogel and Haw each say is still not seen. Haw has a whole article on it (2023), unread | Lin and Zhang 2017 (summary); `haw2023departure` (record) |
| **2. Champa** | The Book itself puts Marco in Champa in a stated year, and the manuscripts differ: 1285 in the Geographic Text, 1280 in Pauthier and Ramusio, 1288 in the Geographic Latin. Yule prefers 1288 and links it to the mission "to the Indian Seas" from which Marco returned about 1290. So "an earlier visit" is Yule's reading, not a new thesis. Who argues for a call on the voyage home: still not found | `yc` (refs/yule-vol2.txt:14550, 14790–14794) |
| **1. Hormuz** | Nothing on the route. One textual fact: in a late stage of Z the chapters on the plain between Qamadin and Hormuz are put in a different, tidier order | `mascherpa2018fonte` (read, p. 50) |
| **4. Haw 2024** | Nothing. The publisher's page for *ZDMG* 174 lists the title only | harrassowitz-verlag.de (summary) |

**One point to keep apart.** Qwen has the dispatch of the envoys in the third month of 1290; Ma 2025 dates the notice to the eighth month. Both can be true (an order in spring, a memorial about it in autumn), but neither run shows the text. Cleaves has it.

## Applied

- `registry/scholarship.md`: Q1 (the single-redaction camp named), Q3 and Q7 (still unchanged, with what was seen), Q10 (Mascherpa 2018 and Andreose 2018 as read sources), the departure date (source name settled; Haw 2023 added), the reading list.
- `registry/bibliography.bib` § "S-13 follow-up": `mascherpa2018fonte`, `andreose2018giovanetto`, `lin2017chinese`, `haw2023departure`, `magone2015vogel`, `haw2016travels`.
- `registry/facts.md`: no change. F-15 already names the *Yongle dadian*.
- **Still open after two more tools:** Hormuz outbound; Champa on the return; the three scholars' own sailing dates; Haw 2024. These need the articles themselves (Haw 2023 and 2024 in *ZDMG*; Cleaves 1976), not another search run.
