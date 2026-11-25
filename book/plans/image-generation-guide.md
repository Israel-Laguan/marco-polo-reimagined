# Image generation guide — reproducing the plates locally

Use this guide to generate and file plate candidates. The S-10 pilot established the Akool and Gemini routes. Codex image generation supplied 32 of the 35 generated hero plates in the November 23 proofs. The [style guide](illustration-style-guide.md) defines the review checklist and per-tradition negatives. Each placed plate's sidecar records the route actually used.

## 1. Prerequisites

- Python 3.10+ for the repository scripts (the standard library is sufficient).
- ImageMagick (`convert`, `identify`), for cropping and upscaling.
- API keys for the Akool or NIM command-line routes. **Never commit them.**
  ```bash
  export AKOOL_API_KEY=...      # paid API, ~4 credits per image at 4k
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

### Codex image generation

1. Use the text from `media/plates/prompts/<plate>.txt` in the image-generation request, including the negative instructions. Save any revision prompt in the same directory.
2. Attach eligible inputs under [style guide rule 9](illustration-style-guide.md#rules-for-every-plate). Record each attached file, its role, licence and credit in the sidecar. The [III-9 revision sidecar](../media/plates/III-9-court-farewell-palace-revised.yaml) shows how to record accepted character sheets.
3. Save candidates under `media/plates/drafts/<plate>/`. Review them with the checklist below and record the rounds, corrective turns and selected file. The [II-6 sidecar](../media/plates/II-6-pulisanghin-bridge.yaml) records a corrective turn and the post-processing command.
4. In the sidecar record the generator, the model version if shown, the date, prompt, negative instructions, input files, and post-processing. Use `version not disclosed` or `none, chat output` when the model version or job ID, respectively, is unavailable. File the accepted master and attribution as in §6.

### Akool and NIM

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
- Keep rejected candidates in `media/plates/drafts/<plate>/` with their generation records when available. The S-10 grid is in `drafts/s10-pilot/`. The labels `p1`, `p2` and `p3` refer to I-7, II-13 and III-5. The labels `akool`, `akool2` and `klein` refer to the first Akool round, the second round with negatives, and NIM.

## 7. Gemini chat pilot (Ilkhanid)

Flux Krea drew Safavid turbans in all eight I-7 pilot candidates. Gemini chat passed I-7 in two turns using `media/plates/prompts/I-7-chat.txt`. The [I-7 sidecar](../media/plates/I-7-carauna-escape.yaml) records the corrective follow-up.

- Keep the negative instructions in the prompt text.
- If using a folio as a style reference, follow the same input rules as for Codex. Ask the model to use the folio's style and create a new composition.
- Other period references gathered by S-11 are in `media/references/` (*'aja'ib* birds for III-7, the *Mōko* scroll strips, Catalan Atlas sheets, LdM folios). Its README says which may be edit input and which are "look only" (BnF scans). Added 2026-11-13: Cocharelli folios (Genoese dress, counting house, harbour, interiors; edit OK outside the UK), the Annales Ianuenses pages and the Carte Pisane crop (look only), and the Singhasari statue photos (look only).
- Save the result into `media/plates/drafts/I-7/`, with a `.json` or `.yaml` noting the chat model, date and prompt. Then review it as above.
