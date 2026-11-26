# Big-Picture Narration Plan: The Meta-Frame, Chapter Batons, & Colophon

This document defines the **macro-narrative architecture** of *The Book of the Million* across all three volumes.

> [!IMPORTANT]
> **Execution Order: Run This Big-Picture Pass FIRST**  
> Before running individual chapter chats, run the **Phase 1 Master Prompt** below. It crafts the series-wide Meta-Introduction, Volume Preludes, Mode-Shift Cues, and Closing Colophon—and then **updates the individual chapter prompts** (`book/proposed-voice/vol-*/ch-*/README.md`) so every small chapter chat inherits the exact general view and baton handoffs.

---

## Phase 1 Master Prompt (Run First in a Dedicated Chat)

Copy and paste this prompt to execute the Big-Picture pass before running individual chapters:

```text
Let's run Phase 1 (The Big-Picture Narration Pass) from @[book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md] and @[book/proposed-voice/PROPOSED-VOICE-GUIDE.md].

1. Read @[book/proposed-voice/BIG-PICTURE-NARRATION-PLAN.md], @[book/proposed-voice/PROPOSED-VOICE-GUIDE.md], and the current macro files:
   - @[book/vol-1/front-01-world-before-the-road.md] (Opening Meta-Introduction & 1260 stage)
   - @[book/vol-2/front-01-yuan-china-context.md] (Volume II Prelude)
   - @[book/vol-3/front-01-indian-ocean-world.md] (Volume III Prelude)
   - @[book/vol-3/ch-12-reliability-essay.md] and @[book/vol-3/back-01-trivia-and-afterlives.md] (Closing Essay & Colophon target)

2. First, propose and review with me:
   - The Opening Meta-Introduction ("The Narrator's Pact": how our single theatrical narrator introduces the modernization of a 700-year-old book and the two-layer main text + Notes design)
   - The Volume II and Volume III Threshold Preludes and the key intra-volume Mode-Shift Cues (I-01, I-03→I-04, I-13→II-01, II-05→II-06, II-09→II-10, II-15→III-01, III-09→III-10)
   - The Closing Modern Colophon ("Explicit Liber") at the end of Volume III
   - Any refinements to the 39 chapter-to-chapter baton passes in Section 3.

3. Once we align, write the proposed macro drafts to:
   - `book/proposed-voice/vol-1/front-01-world-before-the-road/proposed.md`
   - `book/proposed-voice/vol-2/front-01-yuan-china-context/proposed.md`
   - `book/proposed-voice/vol-3/front-01-indian-ocean-world/proposed.md`
   - `book/proposed-voice/vol-3/colophon-and-closing/proposed.md`

4. Finally, propagate the approved Big-Picture framing, mode-shift cues, and exact Incoming/Outgoing Baton instructions into the per-chapter prompt files (`book/proposed-voice/vol-*/ch-*/README.md`) so each subsequent small chapter chat keeps the general view.
```

---

## 1. The Meta-Frame: Taking a 700-Year-Old Book and Modernizing It

### Why the Reader Needs a "Narrator's Pact" Up Front
*Il Milione* is not a modern novel, nor is it a modern travel diary. It began in 1298 as an oral performance hatched in a Genoese prison between a Venetian merchant (**Marco Polo**) and an Arthurian romance writer (**Rustichello da Pisa**), and over seven hundred years it collected layers of Latin abridgments (Pipino), Renaissance expansions (Ramusio), and Victorian scholarly apparatus (Yule–Cordier).

If we drop a modern reader straight into the text without framing *what we are doing to this old book*, they won't appreciate why the narrator steps onstage to talk to them, or why the academic detective work sits in the Notes.

### A. The Opening Meta-Introduction ("How to Listen to a Seven-Hundred-Year-Old Book")
**Where it lives:** At the opening of [**Volume I Front Matter (`vol-1/front-01-world-before-the-road.md`)**](file:///home/anthony/code/marco-polo-reimagined/book/vol-1/front-01-world-before-the-road.md) (and echoed as the stage curtain rises in [**Chapter I-1 (`vol-1/ch-01-genoa-prison.md`)**](file:///home/anthony/code/marco-polo-reimagined/book/vol-1/ch-01-genoa-prison.md)).

**What the Narrator tells the reader:**
1. **The Original Performance:** Seven centuries ago, this book was meant to be read aloud to rooms full of people who wanted both hard merchant truth (what pepper costs, how paper money works, where the water holes are) and grand chivalric spectacle (twelve thousand horsemen in robes of beaten gold).
2. **Why Modernize It:** If you read a literal medieval translation today, you trip over repetitive scribe formulas (*"Now let us quit this province and tell you of the next..."*). If you read the classic 1903 Yule–Cordier monument, every sentence is ambushed by fifty lines of tiny Victorian footnotes arguing over vowel shifts and extinct bishoprics.
3. **Our Two-Layer Bargain:**
   - **Onstage (The Main Text):** One modern storyteller retells the journey in living prose—keeping Marco's sharp eye for cargoes and prices, Rustichello's flair for pageantry, and Ramusio's vivid sixteenth-century details, while stepping in with brief *"for modern audiences"* interludes so you can feel what two-finger-thick gold flagstones or a three-day waterless crossing actually mean.
   - **Backstage (The Notes & Companions):** Every number `[n]` beside a claim leads to the secondary academic narration at the end of the chapter—where we weigh Chinese dynastic annals (*Yuan shi*), Persian chronicles (*Rashīd al-Dīn*), shipwrecks, and seven centuries of scholarly cross-examination (`✓ ~ ✗ ?`) without ever stopping the show.

---

### B. Volume-Threshold Preludes (Preparing the Reader When the Book Changes Gear)
Each volume of *Il Milione* operates by a different narrative logic. The narrator must explicitly prepare the reader at the volume openings (**`I-F1`**, **`II-F1`**, **`III-F1`**) and at major structural pivots inside the volumes:

| Transition / Pivot | How the Old Book Changes Gear | What Our Narrator Tells the Reader |
|---|---|---|
| **Opening of Vol. I (`I-F1` → `I-01`–`I-03`)** | Starts as a family adventure & diplomatic thriller (the Prologue: 1260–1275). | *"We begin in a Genoese prison cell, then rewind to two Venetian uncles who walked east with a pouch of jewels and came back with an emperor's golden passport."* |
| **The Caravan Pivot (`I-03` → `I-04`–`I-13`)** | Shifts from sequential biography to a **route-book / gazetteer with boots on** across Armenia, Persia, the Pamirs, and the Gobi to Shangdu. | *"From here, the Book stops keeping a daily diary and starts reading the road like a merchant's atlas: city by city, desert by desert, ware by ware, following the caravan spine east."* |
| **Opening of Vol. II (`I-13` → `II-F1` → `II-01`–`II-05`)** | Shifts from desert survival to **imperial court theatre and state machinery** under Cublay Kaan at Cambaluc. | *"The dust of the Gobi is behind us. Volume II walks through the palace gates into the most sophisticated state machine on thirteenth-century earth."* |
| **The Provincial Circuits (`II-05` → `II-06`–`II-14`)** | Shifts from the capital to **two grand inspection tours**: south-west to Yunnan/Burma (`II-06`–`II-09`), then down the Grand Canal through conquered Song China (`II-10`–`II-14`). | *"Now the Kaan sends his messengers out from the capital. Follow two great spokes of the wheel: first into the wild river gorges of the south-west, then down the canal cities of Manzi toward the sea."* |
| **Opening of Vol. III (`II-15` → `III-F1` → `III-01`–`III-09`)** | Shifts from horse-posts and canals to **monsoon seamanship, sailors' periplus lore, and Princess Cocachin's bridal fleet**. | *"Trade your saddle for a fir deck with thirteen watertight compartments. Out here the monsoon sets the calendar, sailors' yarns ride alongside real pepper cargoes, and a Mongol princess's wedding fleet is our ticket home."* |
| **The Afterlife Pivot (`III-09` → `III-10`–`III-12`)** | The travelogue ends at Venice in 1295; the story becomes **the biography of the Book itself** and a courtroom weighing of its truth. | *"The travellers have stepped ashore in Venice, but the Book's own voyage is just beginning—from carnival nicknames and Columbus's ink margins to modern forensic history."* |

---

### C. The Closing Colophon / Curtain Call ("Explicit Liber")
**Where it lives:** At the close of Volume III—either as the final section of [**Chapter III-12 (`vol-3/ch-12-reliability-essay.md`)**](file:///home/anthony/code/marco-polo-reimagined/book/vol-3/ch-12-reliability-essay.md) or at the close of [**Back Matter III-1 (`vol-3/back-01-trivia-and-afterlives.md`)**](file:///home/anthony/code/marco-polo-reimagined/book/vol-3/back-01-trivia-and-afterlives.md).

**What the Colophon does:**
Medieval scribes ended manuscripts of *Il Milione* with a formal colophon (*"Explicit liber... Deo gratias"*). Our narrator closes the three volumes with a **Modern Colophon** that brings the meta-frame full circle:
1. **Recalling the 1298 Cell:** Returns one last time to the stone room in Genoa where a merchant counted his memories and a romancer dipped his pen, reminding us how unlikely it was that their prison collaboration would outlive both their republics and the Mongol Empire itself.
2. **Honoring the Chain of Custodians:** Tips the hat to the long relay that carried the book across seven hundred years—Franco-Italian copyists, Friar Pipino, Giovan Battista Ramusio in Venice, Sir Henry Yule and Henri Cordier in their nineteenth-century library, and the modern historians and archaeologists who dug up the Quanzhou ship planks and audited the Yuan salt accounts.
3. **Final Curtain Drop:** Leaves the reader with a resonant closing image of the merchant's voice still speaking across seven centuries whenever someone opens the book and causes it to be read aloud.

---

## 2. The Chapter-to-Chapter Baton-Pass Guideline (Out & In)

When working on any single chapter in a separate chat, the **Outro** (end of Chapter $N$) and **Intro** (start of Chapter $N+1$) form a **two-beat theatrical relay**:

### Rule 1: How to Prepare the Reader at the End of a Chapter (The Outgoing Baton)
Never end a chapter by merely running out of items on a list, and never end with a dry summary (*"Thus we have seen the cities of Persia"*). Every Dramatic Outro must execute three moves in one short paragraph (3–5 sentences):
1. **Land the Final Scene's Image:** Let the last detail of the chapter ring out clearly (e.g., the unchained lion lying down at Cublay's feet in `II-3`; the 1,000 silk carts rolling through the gates in `II-4`).
2. **Pull the Camera Back (The Theatrical Pivot):** In one clause, frame what this chapter just showed us on the larger canvas.
3. **Hand Over a Concrete Baton:** Point to a specific physical object, road, person, or brewing danger that waits on the very next page (e.g., the hunting carts waiting outside in the February cold; the midnight messenger knocking on Achmath's door; the stone lion bridge waiting outside the western gate).

### Rule 2: How to Catch the Baton at the Start of the Next Chapter (The Incoming Hook)
When opening Chapter $N+1$ after the Yule–Cordier epigraph:
1. **Catch the Previous Chapter's Baton in Sentence 1–2:** Reference the concrete detail, place, or cliffhanger left by Chapter $N$'s final paragraph so a continuous reader feels zero jolt across the page turn.
2. **Widen the Lens for a New Reader:** Frame that detail clearly enough that someone opening the book fresh at Chapter $N+1$ also knows immediately where they are standing.
3. **Spring the "Attention Trap":** Within the first paragraph, pivot from the bridge into the new chapter's central spectacle, danger, or sensory hook before unpacking the historical mechanics in paragraph 2.

---

## 3. Master Baton-Pass Ledger (All 39 Chapter Transitions)

When revising Chapter $N$ in an isolated chat, check its **Incoming Baton** (from Chapter $N-1$) and **Outgoing Baton** (to Chapter $N+1$) below so you never break the chain:

### Volume I — *From Venice to the Khan*
| Seam | Outgoing Baton (End of Prev Ch.) | Incoming Catch & Dramatic Hook (Start of Next Ch.) |
|---|---|---|
| **`I-F1` → `I-01`** | Black Sea galleys and the Venice–Genoa rivalry (1298 capture). | The aloud call in Genoa's prison (*"Take this Book and cause it to be read to you"*) + the 1298 sea-war stakes. |
| **`I-01` → `I-02`** | Leaving the 1298 prison cell to look at the Venetian trading house that sent two brothers east with a pouch of jewels. | The Polo family counting-houses in Constantinople & Soldaia → the 1260 jewel venture that traps Niccolò and Maffeo deep inside Mongol Eurasia. |
| **`I-02` → `I-03`** | Returning to Venice in 1269 with the Kaan's golden tablet while the cardinals at Viterbo stall on electing a Pope, and 15-year-old Marco waits. | The deadlocked conclave at Viterbo → the brothers losing patience, taking 17-year-old Marco and the Jerusalem lamp oil, and riding out as Gregory X's couriers recall them. |
| **`I-03` → `I-04`** | Flash-forward of the holy oil reaching the Kaan, then rewinding to the port of Ayas where the long overland atlas begins. | Stepping back onto the quay at Ayas → entering the mountain frontier of Hermenia and Georgiania (silver mines, Noah's Ark, Baku's gushing oil fire). |
| **`I-04` → `I-05`** | Riding south from Tiflis down the Tigris corridor toward Mausul and Baudas. | Crossing the Greater Hermenia frontier into Mausul → the gold-and-silk weavers (*mosolin*) and the fall of the Caliph of Baudas in his tower of gold. |
| **`I-05` → `I-06`** | The shoemaker's one-eyed faith miracle at Baudas and the road climbing east into the great bazaar of Tauris. | The silk-and-gold cloth reappearing in the jewel market of Tauris → the eight kingdoms of Persia, Magi fire-worship, and two-hundred-pound warhorses. |
| **`I-06` → `I-07`** | Persian warhorses and Yasdi silk caravans heading seven days across the plain toward Kerman. | Reaching Kerman's steel workshops and turquoise mines → the plunge down the freezing pass to the scorching harbor of Hormos and its stitched, nail-less ships. |
| **`I-07` → `I-08`** | Turning back north from Hormos through the bitter-water plain toward Kerman's desert rim. | Trading bitter bread-water for three waterless days out of Kerman → Cobinan's *tutia* furnaces, the solitary Dry Tree, and the Old Man of the Mountain's drugged paradise. |
| **`I-08` → `I-09`** | Leaving the starved ruins of the Old Man's fortress for the thick pastures and melon orchards of Sapurgan. | Halting among Sapurgan's honey-sweet dried melons → the ruined palaces of Balc, Taican's mountains of salt, and Badashan's royal ruby monopoly and Alexander's horses. |
| **`I-09` → `I-10`** | Climbing out of Badashan's high valleys along the river toward the roof of the world. | Following the river up onto the freezing, birdless plateau of Pamier (where fire burns dim) → descending into the jade rivers and cotton oasis towns of Cascar, Yarcan, and Cotan. |
| **`I-10` → `I-11`** | Leaving Pein's jasper pebbles and marital customs for Charchan and the edge of the haunted waste of Lop. | Packing thirty days' rations at the oasis of Lop → stepping into the singing sands and spirit-drums of the Great Desert toward Sachiu and the asbestos mines of Tangut. |
| **`I-11` → `I-12`** | Stockpiling forty days of victuals at Etzina for the northern ride into the Mongol homeland. | Counting rations at Etzina → riding into Caracoron, the rise of Chinghis Khan against Unc Can, steppe felt carts, and the crane-hunting marshes of Chagannor. |
| **`I-12` → `I-13`** | Leaving Chagannor's five species of cranes for the three-day ride northeast to the Kaan's summer park. | Arriving at the marble palace and sixteen-mile walled park of Chandu → the portable split-bamboo Cane Palace, weather-conjuring sorcerers, and the August libation of white mares' milk. |

### Volume II — *The Realm of Kublai*
| Seam | Outgoing Baton (End of Prev Ch.) | Incoming Catch & Dramatic Hook (Start of Next Ch.) |
|---|---|---|
| **`I-13` → `II-01`** | Leaving the white mares' milk scattered on the grass at Chandu as the Book turns to how Cublay won and held his throne. | Riding out from Chandu onto the battlefield → Prince Nayan's Christian-banner rebellion, the elephant-borne battle tower, and the strangling of a rebel prince in carpets. |
| **`II-01` → `II-02`** | Handling the inscribed golden tablets (*paiza*) of command and asking what the Emperor who issues them looks like in person. | Looking directly at Cublay Kaan's face and household → the four empresses, the crown prince Chinkin, and the double walls, artificial Green Mount, and curfew bell of Cambaluc. |
| **`II-02` → `II-03`** | The outer walls, chess-board avenues, and midnight curfew bell falling silent outside the palace gates. | *(Benchmark)* Swinging open the palace doors into the great banquet hall → 12,000 Keshican guards, threshold wardens, the gilded wine buffet, and the unchained lion at the Kaan's feet. |
| **`II-03` → `II-04`** | *(Benchmark)* Guests stepping carefully back across the wooden threshold after the White Feast while hunting carts and hounds wait outside. | *(Benchmark)* Stepping outside the gates with the narrator to inspect the covered tiger cart, the 20,000 dog-handlers, the roof-opening elephant litter, and the 1,000 daily silk carts. |
| **`II-04` → `II-05`** | *(Benchmark)* Silk rolling through the gates while Cublay is north at Chandu, and a midnight messenger summoning finance minister Achmath to an empty palace. | Following Achmath through the dark streets past garrison captain Cogatai into the lighted hall → the assassination plot, the mulberry-bark paper mint, the 300,000-horse *yam* relay, and burning black stones. |
| **`II-05` → `II-06`** | Leaving court boots at the palace door as Marco rides out on the Kaan's western highway toward a stone-lion bridge. | Counting the marble lions on the Pulisanghin bridge ten miles west of Cambaluc → the golden king narrative at Caichu, Kenjanfu's palace, and the shop-lined bridge over the great waters at Sindafu. |
| **`II-06` → `II-07`** | Leaving the toll-collector on Sindafu's covered bridge for the scorched borderlands of Tebet. | Stepping off Sindafu's bridge into Tebet's ruined towns → exploding green bamboo fires to scare lions, Caindu's pearl Lake and spice-clove hills, Carajan's gold-dust rivers, and giant serpents sliced on spiked logs. |
| **`II-07` → `II-08`** | Watching the gold-for-silver exchange and couvade beds of Zardandan as the Kaan's armies face the elephant host of Mien. | Weighing five ounces of silver for one of gold in Zardandan → Tartar archers stampeding two thousand armoured war-elephants into the forest, the gold-and-silver pyramid towers of Mien, and tattooed Bangala. |
| **`II-08` → `II-09`** | Turning east from Bangala's spice and eunuch markets into the tattooed court of Caugigu. | Crossing into Caugigu's dragon-tattooed nobility → Anin's horse trade, Coloman's cliff-top copper-urn burials, and Cuiju's bark-cloth garments and pack-dogs guarding river camps from tigers by night. |
| **`II-09` → `II-10`** | Closing the four-month southwestern circuit back at Juju to take the eastern road down the Grand Canal into conquered Manzi. | Settling the inn bill at Juju and taking the eastern fork → the Yellow River at Cacanfu, Coiganju's salt basins, and general Bayan's campaign against the peaceful charity-king Facfur of Manzi. |
| **`II-10` → `II-11`** | Watching the salt fleets leave Coiganju down the paved causeway toward Yanju. | Stepping ashore from the salt barges along the Pauin dike → the twenty-seven subject cities of Yanju (where Marco claims three years' rule) and the counterweight trebuchets that smashed Saianfu. |
| **`II-11` → `II-12`** | Leaving the 300-pound mangonel stones of Saianfu for the river port of Sinju on the mighty Kian (Yangtze). | Riding fifteen miles from Yanju to the ten-mile-wide Kian at Sinju → fifteen thousand vessels moored at one port, split-bamboo towing hawsers, Caigiu's grain canal to Cambaluc, and Suju's six thousand stone bridges. |
| **`II-12` → `II-13`** | Riding through the sendal-weaving towns of Vuju and Changan toward the water-threaded approaches of Kinsay. | Carrying a bolt of sendal from Changan into Kinsay → the "City of Heaven" with its 12,000 bridges, stone fire-towers, West Lake pleasure barges, paved horse-lanes, and million-gold-saggi salt and spice ledgers. |
| **`II-13` → `II-14`** | Walking south out of Kinsay's tax districts through continuous suburbs and gardens toward the hills of Fuju. | Riding south from Kinsay into the mountain gorges of the kingdom of Fuju → tiger-prowled passes, human-flesh-eating warriors, sugar-refining towns, Tyunju porcelain aged for generations, and Zayton's global pepper harbor. |
| **`II-14` → `II-15`** | Leaving the tattoo needles and customs sheds of Zayton to look back across the northern steppes at Cublay's rival cousins in Great Turkey. | Shifting from Zayton's warm quays to the frozen frontier of Great Turkey → King Caidu's rebellion, Princess Aiyaruk's hundred-horse wrestling wagers, Argon's war against Achmath's usurpation in Persia, and dog-sled relays into the Land of Darkness. |

### Volume III — *Seas, Return, and After*
| Seam | Outgoing Baton (End of Prev Ch.) | Incoming Catch & Dramatic Hook (Start of Next Ch.) |
|---|---|---|
| **`II-15` → `III-01`** | Returning from the northern dark and Persian battlefields to the harbor of Zayton, where the great ocean junks are loading for the Indies. | Stepping aboard a four-masted fir merchantman riding at anchor off Zayton → thirteen watertight compartments, six-layer lime-and-hemp hulls, Chipangu's two-finger-thick gold palace floors, and the typhoon-shattered armada. |
| **`III-01` → `III-02`** | Leaving the 1,370 aromatic islands of the Sea of Chin to drop south-west before the monsoon toward Chamba. | Hauling up the stone anchor off Zayton and running fifteen hundred miles south-west to Chamba → King Accambale's elephant tribute, aloeswood forests, the vast spice mart of Java, and the shoals of Pentan. |
| **`III-02` → `III-03`** | Clearing the shallow sixty-mile strait of Pentan where ships must lift their rudders, heading into the eight kingdoms of Java the Less. | Dropping the heavy axial rudder back down in deep water as Java the Less rises ahead → losing the Pole Star, the Polos' five-month monsoon stockade at Samara, the ugly black "unicorn" (rhinoceros), and baking sago bread from palm pith. |
| **`III-03` → `III-04`** | Sailing out from Fansur's camphor groves and sago ovens toward the naked islanders of Necuveran and the great peak of Seilan. | Tracing the sea-lane west from Fansur past Necuveran and the dog-headed cannibals of Angamanain → Seilan's palm-thickened royal ruby and the iron-chained cliff ascent to Adam's and Sagamoni Borcan's disputed summit. |
| **`III-04` → `III-05`** | Crossing sixty miles of emerald shallows west from Seilan to the pearl banks of Maabar. | Watching naked divers drop into the Gulf of Mannar while Brahman shark-charmers mutter spells ashore → King Sonder Bandi Davar's pearl necklace, sacred cattle, temple dancers, Gulf warhorses dying of boiled grain, and St Thomas's peacock shrine. |
| **`III-05` → `III-06`** | Leaving St Thomas's red healing earth in Maabar to coast north into Queen Rudrama's diamond kingdom of Mutfili. | Sailing north into Mutfili's wise queen's realm → throwing raw mutton into snake-infested gorges so white eagles bring up diamonds, long-lived yogis drinking quicksilver and sulphur, and the sighting of the North Star again off Comari and Melibar. |
| **`III-06` → `III-07`** | Watching the North Star climb six cubits above the horizon off Kesmacoran before steering out toward the open western ocean islands. | Leaving Kesmacoran's date-and-fish coast astern for the twin islands of Male and Female → ambergris whaling with barbed harpoons at Scotra, Madeigascar's elephant-lifting *Ruc* feather, Zanghibar's giraffes, and the King of Abash avenging his branded bishop. |
| **`III-07` → `III-08`** | Turning from the highland wars of Abash toward the Red Sea bottleneck and the horse-export ports of Arabia. | Following the coffee-and-incense coast down from Abash into the iron customs gate of Aden → transshipping Indian pepper up the Nile to Alexandria, Esher's fish-eating warhorses and bleeding frankincense trees, and Hormos's suffocating summer wind-catchers. |
| **`III-08` → `III-09`** | Standing again on the sweltering shore of Hormos—where the outward journey once turned back—ready to tell why a fourteen-ship imperial wedding fleet brought the Polos here. | Touching the sewn-in rubies in the Polos' travel coats and rewinding to Cambaluc's palace → Queen Bolgana's dying wish, Cublay's two golden tablets, the two-year sea voyage that cost six hundred lives, and delivering Princess Cocachin to marry Casan in Persia. |
| **`III-09` → `III-10`** | Stepping off the gangplank in Venice in 1295 as the travelogue ends and the strange afterlife of *Il Milione* begins. | Knocking on the door of Ca' Polo in the parish of San Giovanni Grisostomo → Ramusio's ragged-coat homecoming banquet with rubies spilling from ripped seams, the *Milione* nickname, early readers (Thibault de Cepoy, Friar Pipino), and the 1324 deathbed will. |
| **`III-10` → `III-11`** | Closing Marco's chest of effects in 1324 as his words escape Venice into the map-rooms and printing presses of Europe. | Unrolling Abraham Cresques's 1375 Catalan Atlas on parchment → Fra Mauro's 1459 world map, Ramusio's 1559 Venice print, Christopher Columbus's ink margins in Seville, and the 1995–2024 scholarly battles over whether Marco ever reached China. |
| **`III-11` → `III-12`** | Leaving the 2024 Foligno manuscript discovery to open the final courtroom ledger on what in this seven-hundred-year-old Book holds up. | Opening the Book's first-page promise (*"things seen as seen, and things heard as heard only"*) → the 8-row Evidence Ledger, weighing the fiscal hits against the famous silences, and closing with the **Modern Colophon**. |
