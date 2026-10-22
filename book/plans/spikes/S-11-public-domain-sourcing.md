# S-11 — Public-domain artwork sourcing and licensing

**Status:** open · **Timebox:** 1 session · **Gates:** PD items in `PLT` (I-2, II-front, II-4, III-1, III-7, III-11, III-12) and PD photo pairings (e.g. the Zhiyuan banknote in II-5)

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
- [ ] `plans/registry/pd-sources.md` table: artwork → source URL → resolution → licence → caption → OK for commercial print?
- [ ] Downloaded masters in `media/public-domain/` with licence notes

## Feedback to plan
- `illustration-plan.md`: switch any blocked PD slot to GEN or to a substitute

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `PLT.T*` for each PD plate (placement + caption)
