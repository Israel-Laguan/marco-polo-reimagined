# S-10 — Image generation pilot

**Status:** open · **Timebox:** 1–2 sessions · **Gates:** all GEN items in `PLT`; cutaway bases C12–C16 in `DIA`

## Question
Which generator and settings can hold the regional period idioms (Ilkhanid, Song–Yuan scroll, Chola mural…) without garbled script, anachronisms or modern polish? And what does the review and upscale step take per plate?

## Why it matters
34 generated hero plates plus about 25 secondaries. If the generator can't do Persian miniature or Chola mural convincingly, the regional-styles concept needs a fallback before any plate is commissioned.

## Inputs
- `illustration-style-guide.md` (rules, prompt template, technical spec)
- `illustration-plan.md` § Pilot (3 ready prompts: I-7 Ilkhanid, II-13 Song–Yuan scroll, III-5 Chola mural)
- S-05 character cards (Marco appears in Pilot 1)

## Method
1. Choose 2–3 candidate generators (the old plates used Grok). Run the 3 pilot prompts × 4 candidates each.
2. Score each output: idiom fidelity · period errors · script/glyph leakage · "could pass for a real artifact" risk · consistency of recurring figures.
3. Test upscaling to 300 dpi at the S-08 trim size; inspect faces, hands, rigging.
4. Time and cost per accepted plate.

## Output (definition of done)
- [ ] Generator + settings locked; scored comparison saved here
- [ ] 3 accepted pilot plates in `media/plates/` with `.yaml` sidecars
- [ ] Review checklist finalised in the style guide
- [ ] Fallback decided for any tradition that fails (e.g. use the marvel lens, or a PD artwork)

## Feedback to plan
- `illustration-style-guide.md`: prompt-template tweaks, per-tradition idiom cues that worked
- `illustration-plan.md`: re-assign traditions that failed

## Findings
_(fill while working)_

## Decision
_(fill when closing)_

## Tasks to create on close
- `PLT.T*` one per plate (hero first, by volume)
