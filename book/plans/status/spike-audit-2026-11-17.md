# Spike claim audit — 17 November 2026

This audit follows the [16 November audit](spike-audit-2026-11-16.md), which reviewed scope and the boundary between closing a spike and finishing production. This pass checks each spike's **concrete claims** (counts, artifacts, tools, handoffs and stated manuscript state) against the repository as it stands, including the uncommitted 16–17 Nov research intakes. It does not reread external sources.

## Verified (claim holds)

| Spike | Claim | Check |
|---|---|---|
| S-01–S-26 | Closed spikes have no open checklist items, except the two recorded as incomplete (S-22 all-hero cues, S-23 deep dives) | Checklist scan: 0 stray `[ ]` |
| all | Local links resolve | 0 broken links in spikes, registry, README and intakes/closures (2 are `<file>` placeholders) |
| all | Every `@key` cited in the manuscript, spikes, registry and VOICE-GUIDE is in `bibliography.bib` | 0 missing; 369 entries, no duplicate keys |
| S-02/S-24 | Lint and tests run | `unittest`: 5/5 OK. `lint.py`: 1/49 pass, the same as the 2026-10-22 baseline |
| S-05 | 19 visual cards; ages and co-presence check | `character-cards.yaml`: 19 cards, 22 scenes; `characters.py ages`: 0 problems |
| S-06/S-14 | `facts.md` has 44 rows; unresolved items hedged | 44 rows: 24 confirmed, 11 corrected, 8 still-open, 1 disputed |
| S-08 | Build tooling | `tools/build/` (build.sh, Lua filter, template) present |
| S-09 | Pilots A1, A16, B5 | SVG and PDF of each in `media/maps/` and `media/timelines/` |
| S-10 | I-7, II-13, III-5 accepted, with sidecars | PNG, YAML and prompt for each in `media/plates/` |
| S-11 | 6 PD heroes plus the II-5 pairing | Masters in `media/public-domain/` for I-02, II-front, II-04, III-01, III-11, III-12, plus II-05 |
| S-13 | Handoffs in 9 tasks | 9 task files mention S-13 |
| S-22 | C9–C22 removed from active cues; failed supplement labelled | No `[PERIOD]` line uses C9–C22; PLT forbids them; the registry's "comprehensive supplement" carries its failed-intake banner |
| S-23 | Coverage of the 35 GEN hero scenes | 35 scene rows in `visual-references.md` |
| S-26 | 65 rows: 44 confirmed / 18 corrected / 3 removed / 0 open | Tally from `locators.md`: 35 + 9 confirmed, 11 + 7 corrected, 3 not found, 65 total. Holds |

## Discrepancies (claim does not hold, or the record contradicts itself)

1. **HOT.3 is listed as ready but has not been done.** II-05 l. 25 still reads "the Emperor desired Polo, Assessor of the Privy Council…", and Note [7] still calls the de Mailla/Gaubil notice "a presence pillar". That contradicts F-08 (Po-lo = Bolad) and CHR. Check II-11 and III-12 as well.
2. **The S-21 handoff conflicts are all still in the manuscript (5/5):** I-07 Note [2] "Mines … attested"; II-07 l. 39 "The core is crocodile" and Note [11] "✓ Crocodile core"; III-03 l. 25 "Marco *sees* the beast"; III-05 l. 29 and Note [10] "independently corroborated"; III-07 l. 15 and Note [4], with no `Ramusio-only.` label. These are expected open work, but they are reader-facing errors of the same kind as the HOT items.
3. **S-25 citation count and ownership.** The spike says 11 citations; the manuscript now has 12 (`derachewiltz1997marco` 6, `tao1959nancun` 3, `dutschke1993francesco` 2, `atwood2004encyclopedia` 1). The spike says no chapter tasks are needed, yet both audits say metadata does not prove a Note's claim, and **no task file mentions S-25**. No one owns the claim-level check.
4. **The 16 Nov audit says "four removals" for S-26**, but S-26 counts 3 removed. The Rossabi/Ahmad drop is counted among the 18 corrections. Use 3.
5. **Stale numbers on the board.** S-12 says "162 entries" (the bibliography now has 369). S-25 says "11 citations" (now 12).
6. **Status vocabulary.** The board uses "done" for S-16/S-17/S-18 and "closed" for the rest. The S-15 line on the board ("closed, best effort done; archival follow-ups") and its spike header ("closed with documented follow-ups") differ. Pick one term, e.g. *closed (best effort)*.
7. **`tools/lint.py` l. 27 is stale.** It still says thresholds are "PROVISIONAL … wait on S-03 and S-04"; both closed 2026-10-22 and their values are in the `T` block. S-02 l. 112 still lists that follow-up as pending.
8. **`BLD.T3` is still "to write"** (BLD l. 60), but S-09 ticks it as created. The commands are recorded; the task body is not.

## Research follow-ups: prompts written, no return yet

Under the 80% rule ([research/README.md](../research/README.md)), these returns sit below the threshold or are optional:

| Spike | Last return hit rate | Pending prompt | Note |
|---|---|---|---|
| S-15 | 7/10 | [strict follow-up](../research/S-15-priority-strict-follow-up-2026-11-16.md) | below 80%, so the protocol requires the rerun |
| S-19 | 6/10 | [strict follow-up](../research/S-19-priority-strict-follow-up-2026-11-16.md) | below 80%, so the protocol requires the rerun |
| S-18 | Latest return: 2/4 supported at OCR level, 2 inaccessible | Deferred by user decision | Retain access-dependent questions as gaps; use checked fallbacks and do not request another S-18 rerun. See [intake](../research/results/S-18-library-access-return-2026-11-17-intake.md). |
| S-22 | 8/10 | [targeted follow-up](../research/S-22-visual-priority-targeted-follow-up-2026-11-16.md) | optional |
| S-17 | 8/10 | [older follow-up](../research/S-17-follow-up-prompt.md) | largely superseded by priority prompt §1; the research README still offers it as available |

Ten files in `research/` (the 16–17 Nov prompts) are untracked, and 60+ files have uncommitted changes. Commit them so that the spike links point at committed files.

## Open reading the spikes named at the time of the audit

- **S-13 → III-12:** the "still to read" list had five items covering seven works. Subsequent result: `gadrat2024read` was read as indexed PDF text; access to `gadrat2026marco` was blocked during this pass despite its open-access status. The Haw 2023/2024 *ZDMG* papers are paywalled.
- **S-21 optional:** Twynam, Wen 1980 and Weisgerber are unread, with fallbacks recorded.
- **S-22/S-23:** the all-hero `[PERIOD]` cues and the per-work interior deep dives are incomplete. No scouted modern work has been viewed.

## Ready-now hotfixes still outstanding (board § Ready now)

- `DOC.T1`: `/workspace` paths remain in 7 files (I-F1, I-F2, I-B1, II-F2 and three volume READMEs).
- `MED.T3`: all 11 mistyped media files are unchanged (6 `drawing-*.png` and 2 maps are JPEG; `map-asia-mongol-empire.*` are GIF; `map-china-yuan.jpg` is PNG).
- `HOT.2`: "Soft join:/caution:/hinge:" scaffolding remains, 23 hits in III-12 alone, plus III-06, III-09, III-10, III-11.
- `HOT.3`: see Discrepancy 1.
- Lint archaisms outside quotes, e.g. I-02 l. 23, 41 and I-03 l. 31, belong to `.T6`/re-voice and are not hotfixes.

## Recommended actions, in order

1. Do HOT.3 and the five S-21 conflicts in one corrections pass. All are small, reader-facing, and their wording is already specified.
2. Do DOC.T1, MED.T3 and HOT.2. They are mechanical and unblock clean builds.
3. Bookkeeping: fix the S-25 count to 12 and add a `.T4` line for claim checks in the 12 affected Notes; correct the 16 Nov audit's "four removals"; update the board counts and status terms; remove the stale PROVISIONAL comment in `lint.py` and tick S-02's follow-up; write the BLD.T3 body.
4. Review the pending S-15 and S-19 prompts for accessible targets; S-18 access-dependent work is deferred by user decision; the S-17 older prompt has been marked superseded.
5. Use the 2024 Gadrat reading recorded below; retain the 2026 article as summary-only until it can be read directly.
6. Commit the untracked research prompts and intakes.

## Applied the same day (2026-11-17)

- **HOT.3:** in II-05, the body (l. 25) and Note [7] now say the annals' "Po-lo" is Bolad, citing `ycadd` and `ma2025chinese`, and the "presence pillar" claim is gone. III-12 open question 5 is marked settled, and Note [13] is updated. II-11 had no Po-lo claim left. Board, F-08 and F-26 are marked applied.
- **The five S-21 conflicts are fixed, using the closure's H2/H5/H6/H7/H10 wording.** I-07 Note [2] attributes the mine to Yule. II-07's body and Note [11] say "usually identified as a crocodilian". III-03 drops the eyewitness claim. III-05's aside and Note [10] attribute the breeding failure to the Book. III-07 gets an inline Ramusio flag plus `Ramusio-only.` and the folio in Note [4]. Each chapter's handoff is marked fixed. Lint: II-05 −1 error, III-07 −2 errors (its Ramusio flag is now detected); no other file changed.
- **Bookkeeping:**
  - S-25 now says 12 citations, and the claim-level check is new task `APP.T8`.
  - The 16 Nov audit now says three removals.
  - Board: S-12's count is updated, and S-15–S-18 now read *closed (best effort)*.
  - `lint.py`: the PROVISIONAL comment is removed, and S-02's follow-up is ticked.
  - `BLD.T3` now has a proper task body.
  - The S-17 older prompt is marked superseded in `research/README.md`.
- **Hotfixes (second pass, same day):**
  - `DOC.T1`: `/workspace` paths are gone from the manuscript and status docs, and five reader-facing Notes were rewritten.
  - `MED.T3`: every media file now has its true extension, duplicates are removed, and the Mongol map is the 1294 frame. A build of the front-02 files places all five images.
  - `HOT.2`: 165 "Soft …:" labels and every other scaffolding hit are removed. The lint `scaffolding` check is now 0 in all files, and total lint errors are down 263 with no file worse.
- **Still open at the time of that pass:** `MED.T1` captions (III-F2's return map is now openly the overview); the S-15 and S-19 strict reruns; the Gadrat reading; committing. Subsequently the user chose to retain access-dependent S-18 questions as gaps and stop chasing them; see below.

## Accessible scholarship follow-up (2026-11-17)

- Read Gadrat-Ouerfelli's 2024 chapter as indexed PDF text and reread the Andreose passage on the *Madeigascar* variants. Updated III-11, its handoff, the bibliography and scholarship registry; see the [source check](../research/results/S-13-open-access-source-check-2026-11-17.md).
- The 2026 Gadrat-Ouerfelli article remains summary-only because the publisher blocked automated access. Its conclusions and pre-Wood claims are not promoted to directly verified. S-18's remaining access-dependent questions are deferred by user choice.

## Method

These are scripted checks from `book/`: checklist scan, link resolver, bib-key cross-reference, `unittest`, `lint.py`, `characters.py ages`, outcome tally of `locators.md`, `file` header sniffing of `media/`, and grep of the manuscript for each conflict and hotfix the spikes name. Prompt-to-return mapping by filename and backlink. No external source was consulted.
