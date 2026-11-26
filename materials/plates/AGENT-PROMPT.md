# Agent prompt: GEN hero plates (PLT)

Paste everything below the line into the GPT agent. It assumes the agent can read and write this repo, run `python3` and ImageMagick (`convert`), and generate images.

---

You are making **printed illustration plates** for *The Book of the Million*, an illustrated retelling of Marco Polo in three volumes. The repo root is the `book/` folder. These plates go into the printed book. Each one shows one scene in the painting tradition of the region where it happens. Each must pass review and be labelled as a modern illustration.

This is a **trial of a new route**: a GPT image model in place of Akool/Flux and Gemini. Record the route honestly in every sidecar.

## Read first

1. `plans/illustration-style-guide.md`, all of it. It covers the rules (1–12), the tradition map, the technical spec, the prompt template and the review checklist.
2. `plans/illustration-plan.md`:
   - § Hero plates: each scene's row, with its tradition, format, **Must get right** and **Caution in caption** columns.
   - § S-22 period cues: the C-lines.
3. `plans/tasks/cross/PLT-plates.md`: the GEN steps, the plate table, and the R-3 and S-23 handoffs at the end.
4. `plans/image-generation-guide.md` § 5 (print sizes) and § 6 (filing).
5. Each plate's chapter task, `plans/tasks/chapters/vol-*/<chapter>.md`, for its period-source handoff.
6. `plans/registry/visual-references.md` for the cue sources and the gap-source ledger.
7. The three finished plates and their sidecars in `media/plates/` (I-7, II-13, III-5), as the quality and filing benchmark. `media/plates/prompts/I-7-chat.txt` is the model for a long prose prompt.
8. `media/characters/STYLE-REFERENCES.md` and the character sheets, as the house look of the recurring figures.

## Hard rules

- **Never in the image:** no script of any kind, including pseudo-script, seals, stamps, signatures or numbers (rule 4). No sacred figure used as decoration (rule 6). No modern work's title, artist or character name in any prompt (rule 9).
- **Image inputs:** only `edit OK` files from `media/references/README.md` or `media/reference/s22/`, and character sheets whose sidecar says `status: accepted`. A `draft` sheet is not an input. Never attach a `look only` file. Even with inputs attached, describe everything in words.
- **People:** for every recurring figure in the scene, run `python3 tools/characters.py cue <id> <year>`. Its dress and attributes are binding, and a card line wins over a cue line. Count the figures: the scene must have the people the row names, no crowd where the text implies a few, and no Polo where `ages` says none can be.
- **Rejected cues:** C9–C22 must not be used. A detail with no checked source is omitted, or kept generic and noted in the sidecar.
- **Do not edit** the plan docs, the cards, the chapters, or anything outside `media/plates/` and `media/ATTRIBUTIONS.md`. Do not place plates in chapters. Do not commit. The user accepts plates; you never set `accepted`.

## Batches

**Batch A (do now):** traditions the character sheets already proved, all with recurring figures.

| Plate | Scene | Tradition | Fmt |
|---|---|---|---|
| I-1 | Marco dictating to Rustichello | Italian Gothic illumination | P |
| I-3 | "Sire, 'tis my son and your liegeman" | YC | L |
| I-6 | Marco at the Magi tombs of Saba | Ilkhanid (JT) | L |
| I-12 | Cane divination before Chinggis's battle | Ilkhanid (JT) | L |
| I-13 | Mare's-milk libation leaving Chandu | YC | H |
| II-1 | Kublai on the elephant tower, Nayan battle | YC (Liu Guandao manner) | H |
| II-3 | The White Feast procession | YC | H |
| II-15 | Aijaruc throws the prince | Ilkhanid (JT) | L |
| III-10 | Jewels ripped from the Tartar coats | Venetian Gothic | P |

Stop after Batch A and report. **Batch B** is every other plate marked `ready` in the PLT table. Do it only when the user says so. Its "first of its tradition" plates are mini-pilots: if 2 rounds fail, stop that plate and report rather than switching tradition.

## Steps for each plate

1. **Gather.** Collect the following:
   - the scene's row in `illustration-plan.md`;
   - the chapter task's period-source handoff;
   - the C-cues the row names;
   - the `cue` lines for each recurring figure, with the year of the scene;
   - any accepted character sheet for those figures;
   - up to 3 `edit OK` references that help the tradition or the objects.
2. **Prompt.** Write `media/plates/prompts/<plate>.txt` as a long prose prompt in the shape of `I-7-chat.txt`:
   - **Style first:** the tradition, the period works named in the style guide, and 5–7 concrete idiom cues. Also say what the tradition is *not*; for example, Ilkhanid is not Safavid.
   - **Scene:** the place and year, then each figure with their card dress and age, the action, and the setting objects from the cues.
   - **Strictly avoid:** script and seals, the cards' `[AVOID]` lines, the review checklist's common misses for this tradition, photographic realism, and heavy damage.
   - **Format:** the plan's format.
     - P: portrait 3:4.
     - L: landscape 4:3.
     - H: generate the widest landscape you can; it will be cropped to 2:1.
     - Light even ageing, matching the series.
3. **Generate.** Make up to 2 rounds. A round is one image plus at most one corrective turn. Keep every candidate in `media/plates/drafts/<plate>/` as `gpt-r<round>-<n>.png`.
4. **Review.** Check each candidate against all 9 items of the style guide's § Review checklist, and against the row's **Must get right** column, item by item. Look at faces, hands, borders and corners at 100%. A smeared face is a re-roll; upscaling won't fix it.
5. **Post-process** to print size, per the image-generation guide § 5, with ImageMagick: Lanczos, plus a light unsharp mask only when upscaling.
   - P: at least 1350 px wide.
   - L: at least 1350×1013.
   - H: crop to 2:1, then 2700×1350.

   Save the lossless master as `media/plates/<plate>-<slug>.png`, using the slug style of the existing masters.
6. **Sidecar.** Write `media/plates/<plate>-<slug>.yaml` in the exact shape of `II-13-west-lake-barges.yaml`, with these values and additions:
   - `status: draft`.
   - `caption`: the scene, plus the plan's caution text, plus the rule-1 label: "Modern illustration in the manner of <tradition>. Not a historical artifact."
   - `generator`: the product and model name as shown to you.
   - `job_id`: none, chat output.
   - `route`: `GPT trial (not the PLT table's route)`.
   - `prompt`: the path of the prompt file.
   - `negative`: `in-prompt`.
   - `reference_images`: a list of file, use, licence and credit, or `[]`.
   - `figures`: a list of card id, year and the `cue` lines used.
   - `cues`: the C-numbers used.
   - `unsourced`: the details drawn without a checked source.
   - `post`: the exact commands.
   - `review`: one line per checklist item, plus one line per **Must get right** item.
7. **Attribution.** Add one row per plate to `media/ATTRIBUTIONS.md` § Generated plates, with the existing columns (Local file | Plate | Tradition | Generator). Add a note column only if the table already has one. The lead agent does this once at the end.

## Subagents

You may run one subagent per plate in parallel. Each writes only its own prompt, drafts, master and sidecar. **Only you (the lead)** edit `media/ATTRIBUTIONS.md`, once at the end. Give each subagent this whole prompt and its row of the batch table.

## Report back

Give one line per plate:
- the master file, or "failed";
- the rounds used;
- the checklist items that failed or are borderline;
- the details left unsourced;
- whether the figures match their cards.

Then list any sheet you wished you could have attached but could not, because it was still a draft.
