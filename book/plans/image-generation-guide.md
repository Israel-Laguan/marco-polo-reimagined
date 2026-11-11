# Image generation guide — reproducing the plates locally

How to make a plate candidate from this repo, as worked out in S-10 (2026-11-10). Rules, the review checklist and per-tradition negatives live in `illustration-style-guide.md`. This file covers only the mechanics.

## 1. Prerequisites

- Python 3.10+ (the stdlib is enough; no `pip install`).
- ImageMagick (`convert`, `identify`), for cropping and upscaling.
- API keys in your shell. **Never commit them.**
  ```bash
  export AKOOL_API_KEY=...      # main generator (paid: ~4 credits per image at 4k)
  export NVIDIA_API_KEY=...     # optional: NIM FLUX.2 Klein (free; blocks many prompts)
  ```
  If the keys sit in a `.env` file: `set -a; . path/to/.env; set +a`.

## 2. Write the prompt file

Make one plain-text file per plate in `media/plates/prompts/<plate>.txt`:

```
<tradition first, then the scene, then period cues, then ground and format>

NEGATIVE: text, calligraphy, inscription, seal, signature, <tradition-specific terms>
```

- Build it from the template in `illustration-style-guide.md` § Prompt template: `[STYLE] [SCENE] [PERIOD] [FORMAT]` as prose, and `[AVOID]` → `NEGATIVE:`.
- Recurring people: paste the lines from `python3 tools/characters.py cue <id> <year>`.
- Avoid "on the left… on the right…": Flux Krea turns it into a two-page diptych.

Examples: `media/plates/prompts/II-13.txt`, `III-5.txt` (accepted) and `I-7.txt` (failed on Akool).

## 3. Generate candidates

Run from `book/`:

```bash
python3 tools/plate_gen.py media/plates/prompts/II-13.txt --scale 16:9 --n 4 --out media/plates/drafts/II-13
```

- `--scale`: `4:3` (landscape miniature), `3:4` (portrait), `16:9` (handscroll; crop to 2:1 later). Akool has no 3:1.
- `--provider klein` uses the free NIM model. Its prompt cap is 800 chars and it has no negative field; its content filter rejects many scenes.
- Each image is written with a `.json` next to it holding the prompt, negative, model, Akool `job_id`, credits and date. Akool has **no seed**: the job id is the only handle, and its download URL expires in 7 days, so the tool downloads at once.
- Expect about 30–60 s per image. Generate 4 and pick 1.

## 4. Review

Go through the checklist in `illustration-style-guide.md` § Review checklist. Zoom into every border and corner for pseudo-script. Reject rather than retouch.

## 5. Post-process to print size

The targets are 300 dpi on the 6×9 in trim:

| Plate | Target | From Akool 4k |
|---|---|---|
| half page 4:3 | ≥ 1350×1013 | 1536×1152: no upscale |
| handscroll spread 2:1 | 2700×1350 | 1536×864 → crop to 1536×768 → ×1.76 |
| full page 3:4 | 1350×2160 | 1152×1536 → ×1.4 or more |

```bash
# handscroll: crop to 2:1 (adjust the +0+48 offset to the composition), then upscale
convert raw.jpg -crop 1536x768+0+48 +repage crop.png
convert crop.png -filter Lanczos -resize 2700x1350 -unsharp 0x0.75+0.5+0 media/plates/II-13-west-lake-barges.png
# no upscale needed: just make the lossless master
convert raw.jpg media/plates/III-5-pearl-divers.png
```

Faces smeared in the raw image stay smeared: re-roll, don't upscale. Real-ESRGAN is optional and untested here.

## 6. File it

- Master: `media/plates/<vol>-<ch>-<slug>.png`.
- Sidecar: `media/plates/<vol>-<ch>-<slug>.yaml`. Copy the shape of `II-13-west-lake-barges.yaml`: plate, tradition, caption (with the rule-1 label), generator, model, job id, date, prompt, negative, post-processing, and review notes.
- Add a row to `media/ATTRIBUTIONS.md` § Generated plates.
- Keep the rejected candidates in `media/plates/drafts/<plate>/` with their `.json` files. `drafts/s10-pilot/` holds the whole S-10 grid: `p1` = I-7, `p2` = II-13, `p3` = III-5; `akool` = round 1, `akool2` = round 2 with negatives, `klein` = NIM.

## 7. Traditions the API model can't do (Ilkhanid)

Flux Krea draws Safavid turbans for any "Persian miniature" prompt. **Ilkhanid plates use Gemini (chat app)**, which passed I-7 in two turns (the follow-up text is in `media/plates/I-7-carauna-escape.yaml`). Use a chat image model (GPT-image or Gemini, in their web chat) with `media/plates/prompts/I-7-chat.txt`.

- Those models follow long prose and in-prompt "avoid" lists, so the negatives sit inside the text.
- If the chat accepts an image, attach a public-domain *Jami' al-Tawarikh* folio as a **style** reference, e.g. Edinburgh Ms Or 20 f.110v on Wikimedia Commons. Add: "Use the attached only for style. Do not copy its composition."
- Save the result into `media/plates/drafts/I-7/`, with a `.json` or `.yaml` noting the chat model, date and prompt. Then review it as above.
