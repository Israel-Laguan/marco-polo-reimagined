# S-11 — Public-domain artwork sourcing and licensing

**Status:** closed 2026-11-10 (one decision left with the user: the BnF licence) · **Timebox:** 1 session · **Gates:** PD items in `PLT` (I-2, II-front, II-4, III-1, III-7, III-11, III-12) and PD photo pairings (e.g. the Zhiyuan banknote in II-5)

## Question
For each planned public-domain artwork, where is the best high-resolution copy, what are its exact reuse terms (including commercial print), and what is the correct provenance caption?

## Why it matters
The artworks are public domain, but scans can carry holder restrictions (e.g. BnF Gallica charges for commercial use). A plate that can't be printed legally is a hole discovered late.

## Inputs
- `illustration-plan.md` PD rows
- Candidates: *Livre des merveilles* (BnF fr. 2810); Yuan imperial portrait of Kublai (NPM Taipei); Liu Guandao, *Khubilai Khan Hunting* (NPM); *Mōko Shūrai Ekotoba* (Museum of the Imperial Collections); al-Qazwini rukh folio (several MSS); Columbus postils (Biblioteca Colombina); 1477 Creussner woodcut; Catalan Atlas (BnF); Fra Mauro map (Marciana); Zhiyuan banknote

## Method
1. For each: holding institution, shelfmark/folio, Wikimedia Commons file (PD-Art tag?), maximum resolution, licence text.
2. Flag any that are non-commercial only, and name a substitute (another MS of the same image, or a GEN fallback).
3. Write the caption + credit line.

## Output (definition of done)
- [x] `plans/registry/pd-sources.md` table: artwork → source URL → resolution → licence → caption → OK for commercial print? (8 rows plus the Fra Mauro secondary; captions, holder terms, leads)
- [x] Downloaded masters in `media/public-domain/` with licence notes (`README.md` there: 8 files, 32 MB; II-4 is an interim master)

## Feedback to plan
- `illustration-plan.md`: switch any blocked PD slot to GEN or to a substitute

## Findings
_2026-11-10. Commons API for files, sizes and licence tags; holders' reuse pages by web research; each image looked at before it was chosen._

**Verdicts (detail in `registry/pd-sources.md`).**
- **OK for commercial print, credit only (5 + pairing):** II-front and II-4 (NPM open data, CC BY 4.0), III-1 (Kyushu University copy, public domain), III-11 (CC BY-SA photograph of the Colombina copy; the 1477 woodcut in Dibdin's 1822 facsimile as the PD alternative), and the II-5 Zhiyuan note (CC BY-SA photograph).
- **Fee (2):** I-2 (LdM, fol. 2v) and III-12 (Catalan Atlas caravan) exist only as BnF scans. Gallica is free for non-commercial use; commercial reuse needs a paid licence. The fee rests on French public-information law, not copyright, so neither the work's PD status nor a Commons copy removes it. The same applies to every secondary that reproduces an LdM miniature.
- **No source (1):** III-7. No Qazwini rukh-with-elephant is free for commercial use: the Met's leaf is not open access, the Munich manuscript is probably NC, the Freer folios carry conditions. The slot goes to GEN.

**What the check turned up beyond licences**
- **III-1's scene does not exist.** The *Mōko Shūrai Ekotoba* paints Suenaga's fighting, not the 1281 typhoon. The hero is now the scroll-2 boarding of a Yuan ship, and the caption says the storm is not painted.
- **II-4 is a hanging scroll** (182.9 × 104.1 cm), not a handscroll: format P, not H. The best Commons copy is 1346 px wide, 4 px under the full-page target; NPM's own 6 MP file fixes that.
- **III-12's inscription** says the caravan left "the empire of Sarai" for Cathay. That supports the caption's caution: the Polos are a modern reading.
- **III-11 has a direct image after all:** a CC BY-SA photograph of the Colombina copy, open at Abyssinia and Aden, with postils and a manicule. The Creussner woodcut drops to the alternative.
- **I-2:** fol. 2v carries the rubric "Comment les .ij. freres vindrent au grant kaan"; the turbaned Khan stands before a tent. The miniature is landscape, so the P slot takes the whole folio.
- **Fra Mauro (secondary):** a Marciana image carries the Italian heritage fee (DM 108/2024). Naya's 1873 photographic facsimile and Fraser's 1804–06 copy (British Library) are PD substitutes.
- **The II-5 note:** the photograph does not say whether the sheet is a period note or a later pull from the plate. The caption must not call it original.

**Not checked here** (listed as leads in `pd-sources.md`): other Polo manuscripts with the audience scene (BL Royal 19 D I, Bodl. 264) as a BnF-free I-2; whether ColBase lists the original *Mōko* scrolls; the Gallica terms page itself (blocked here; its terms are quoted from BnF documents).

## Decision
- Six PD heroes (I-2, II-front, II-4, III-1, III-11, III-12) and the II-5 pairing stay PD; III-7 moves to GEN. The plan is now **35 GEN + 6 PD**.
- I-2 and III-12 print only with a BnF licence. **The user decides:** buy the two licences (and any LdM secondaries), or switch both to GEN. Until then `PLT.I-02` and `PLT.III-12` are blocked; check the BL/Bodleian lead for I-2 first.
- Captions and credit lines in `pd-sources.md` are the ones to print; the holder's required credit wording is part of each.

## Tasks to create on close
- [x] `PLT.I-02`, `PLT.II-front`, `PLT.II-04`, `PLT.II-05P`, `PLT.III-01`, `PLT.III-11`, `PLT.III-12` in `tasks/cross/PLT-plates.md` (placement + caption; I-02 and III-12 blocked on the BnF decision)
