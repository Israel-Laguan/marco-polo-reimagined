# S-10 — Image generation pilot

**Status:** closed 2026-11-10 · **Timebox:** 1–2 sessions · **Gates:** all GEN items in `PLT`; cutaway bases C12–C16 in `DIA`

## Question
Which generator and settings can hold the regional period idioms (Ilkhanid, Song–Yuan scroll, Chola mural…) without garbled script, anachronisms or modern polish? And what does the review and upscale step take per plate?

## Why it matters
35 generated hero plates plus about 25 secondaries. If the generator can't do Persian miniature or Chola mural convincingly, the regional-styles concept needs a fallback before any plate is commissioned.

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
- [x] Generator + settings locked; scored comparison saved here (Akool Flux Krea; Ilkhanid → Gemini chat)
- [x] 3 accepted pilot plates in `media/plates/` with `.yaml` sidecars (I-7, II-13, III-5)
- [x] Review checklist finalised in the style guide
- [x] Fallback decided for any tradition that fails (Ilkhanid: Kontext → stronger model → marvel lens)

## Feedback to plan
- `illustration-style-guide.md`: prompt-template tweaks, per-tradition idiom cues that worked
- `illustration-plan.md`: re-assign traditions that failed

## Findings
*Session 1, 2026-11-10.* Run from a throwaway script (keys from the sibling project's `.env`). Accepted plates' full prompts and job ids are in their sidecars.

**1. Candidate generators: what was reachable.**

| Candidate | Route | Result |
|---|---|---|
| FLUX.2 Klein 4B | NVIDIA NIM (free) | Ran P1 only. **Content filter blocked every P2 and P3 call** (`CONTENT_FILTERED`, even with the bare torso or the sharks removed). Not usable for a series. |
| FLUX.1-dev | NVIDIA NIM | HTTP 500 on every call, even "a cat". Down. |
| FLUX Krea dev | Akool direct API, 4 credits/image at 4k | Ran everything. **The only viable candidate.** |
| FLUX Kontext dev (img2img) | Akool direct API | Both jobs failed (status 4): Akool would not fetch the Wikimedia reference URL. **Untested**, not failed. |
| Gemini 3.1 Flash Image | OpenRouter | 402: account needs ≥ $1 balance. Not run. |
| Z-Image, FLUX 1.1 pro and others | Pollinations | 401: keyless access now limited to tiny sizes. Not run. |

The Grok model used for the old plates was not reachable either.

**2. Scored comparison** (1–5; artifact risk: higher = more likely to be taken for a real artifact).

| Pilot | Run | Idiom | Period | Script leak | Artifact risk | Scene held | Verdict |
|---|---|---|---|---|---|---|---|
| P1 I-7 Ilkhanid | Klein ×4 | 2 (comic-book) | 2 | **fail**: pseudo-Arabic captions in 4/4 | 3 | 1: no horses, flying putti | ✗ |
| | Krea r1 ×4 | 3: *generic* Persian miniature, Safavid not Ilkhanid | 2: turbans | pass | 5 | 1: no raiders in 4/4 | ✗ |
| | Krea r2 ×4 (+negative) | 3 | 2: turbans despite the negative | pass | 5 | 1: "left… right…" yields **diptychs**; still no raiders | ✗ |
| P2 II-13 Song–Yuan | Krea r1 ×4 | 4 | 3: upswept Ming-ish roofs | **fail** in 3/4 (pseudo-calligraphy, seals) | 4 | 3 | 1 usable |
| | Krea r2 ×4 (+negative) | 4 | 3 | pass 3/4 | 4: fake mounting seam | 4 | **accepted s4** |
| P3 III-5 Chola | Krea r1 ×4 | 4 | 2: crowned deity-like figures in 4/4 | pass | 4: heavy flaking | 2: divers read as dancers | ✗ |
| | Krea r2 ×4 (+negative) | 3: palette right, figures folkier than Thanjavur | 4 | pass | 3 | 4 | **accepted s4** |

**3. What worked.**
- **The `negative_prompt` field is the main control.** It removed pseudo-script and seals (P2) and deities and crowns (P3). The same terms written as "no X" inside the prompt did little: Flux weakens negations in the prompt text.
- Lead the prompt with the tradition, then the scene. Name concrete objects ("stones in their hands", "dive head-first") rather than outcomes ("pearl divers").
- Don't write "on the left… on the right…": Krea renders it as two facing manuscript pages.
- Akool has **no 3:1 scale**. 16:9 cropped to 2:1 is the handscroll path; the style guide already allows 2:1.

**4. What failed: Ilkhanid.** Krea knows "Persian miniature" only as the later Safavid/Mughal look: turbans, single riders, a pale ground. It ignored *Jami' al-Tawarikh* cues (Mongol faces, lamellar armour, fur hats) in 8 of 8 seeds and never drew the raiders. That covers six GEN plates: I-6, I-7, I-9, I-12, II-11 and II-15, plus the Ilkhan court half of III-9.

**5. Upscale.** At 4k, Akool returns 1536×1152 (4:3) and 1536×864 (16:9).
- A 4:3 half-page plate (1350×1013) needs **no upscale**.
- A 2:1 handscroll spread needs ×1.76: Lanczos plus a light unsharp mask gives a clean 2700×1350, with no halos and crisp linework and rigging.
- **Faces under about 20 px are already smeared in the generator's output**, so no upscaler recovers them. In scroll scenes this is acceptable at print scale. Close figure plates (portrait 3:4 full page, 1350×2160) will need a 2.0× upscale, and faces must be judged there.
- Real-ESRGAN was not run: the downloaded binary needs your approval to execute.

**6. Time and cost.** About 30–60 s per image. An accepted plate took 8 images (2 rounds × 4), so about 32 credits, about 8 min of generation and about 10 min of review. Balance after the session: 1,100 credits. Projection for 34 heroes plus about 25 secondaries: **about 1,900 credits** at the pilot hit rate, less once the negatives are templated in from the start.

## Decision
*Partial; spike stays open for Ilkhanid.*
- **Generator for non-Ilkhanid traditions: Akool `flux-krea-dev-lora`, direct API, `resolution: 4k`, with a per-tradition `negative_prompt`.** Rationale: the only candidate that ran all three idioms, and it passed two of them.
- Ilkhanid is **not locked**. Next step, in order:
  1. Kontext img2img with a public-domain JT folio re-hosted on an Akool-fetchable URL (Akool's own CloudFront or a temporary public bucket). Watch rule 5: idiom, not composition.
  2. A stronger model: Gemini or GPT-image via OpenRouter (needs a ≥ $1 top-up), or the Akool web UI, which uses `gpt-image-2.5-sunburst` (not reachable through the API).
  3. Fallback if both fail: draw the six Ilkhanid scenes in the **marvel lens** (*Livre des merveilles*), which can already show Franks and Mongols together. Real JT folios stay as PD secondaries via S-11, never captioned as these events.
- Pilot plates: II-13 and III-5 accepted (`media/plates/`). I-7 is pending the step above.
- *Update, same day:* **Gemini (chat app) with `I-7-chat.txt` holds the Ilkhanid idiom.** It gives JT-style Mongol raiders and Franks in soft caps, with no turbans and no script. The scene beat still misses: the merchants ride calmly and the youngest doesn't look back. Draft: `media/plates/drafts/I-7/`. **Second turn (a follow-up in the same chat asking for a gallop and Marco looking back) passed: I-7 accepted** (`media/plates/I-7-carauna-escape.png`). **Ilkhanid → Gemini chat.** Use `I-7-chat.txt` as the template, plus one corrective follow-up turn. Option 3 (marvel lens) is dropped. Cost: 2 chat turns, no API credits. Limits: 1200×896 output (needs ×1.125 for a half page), no seed or job id, and the model version isn't recorded.
- Reproduce with `plans/image-generation-guide.md` and `tools/plate_gen.py`. Every S-10 candidate is kept in `media/plates/drafts/s10-pilot/`. The Ilkhanid prompt for a chat image model is `media/plates/prompts/I-7-chat.txt`.

## Tasks to create on close
- [x] One task per GEN hero, `PLT.I-1` … `PLT.III-10`, in `tasks/cross/PLT-plates.md`, with a route per tradition and a mini-pilot rule for untested traditions. Plus `PLT.S*`, `PLT.C12`–`C16` and `PLT.LEGACY`.
