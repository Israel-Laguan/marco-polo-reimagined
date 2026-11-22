# Prompts for follow-up chats

## Voice v3 rollout (2026-11-21)

Copy one block into a new chat opened in this repository. Use a workspace that contains the latest Voice Guide and the revised II-3 and II-4. These changes were in the working tree at handoff, so an isolated worktree needs them carried over first.

The voice chat can begin with II-8 while the apparatus chat works on II-3 and the companions. The media chat can verify and prepare assets in parallel. Reconcile Note numbers and place figures once the relevant chapter’s narrative is stable.

### 1. Re-voice all remaining chapters

```text
Roll out the approved Voice Guide v3 across all three volumes of The Book of the Million. Read book/VOICE-GUIDE.md and W4 in book/plans/content-revision-plan.md. Use book/vol-2/ch-03-feasts-keshican.md for the approved structure and book/vol-2/ch-04-hunt-traffic.md for the latest narrator, scene pauses and outro. Start with book/vol-2/ch-08-mien-bangala.md, then use W4 and the chapter task files to prioritise the rest. Audit chapters already re-voiced under v2 when you reach their volume. Keep the distinct forms of the reception chapters and the closing reliability essay.

Read each chapter’s source range, task backlog and checked factual handoffs before rewriting. Carry exact Yule–Cordier epigraph wording, each chapter’s factual corrections and its uncertainty forward. Build scenes around Marco’s mercantile detail, Rustichello’s pageantry and a Ramusio-inspired modern narrator. Give the guide a little showmanship and British diction where it suits the scene. Use invitations like “Picture this” selectively, and let an occasional short aside change the reader’s viewpoint. Open on a concrete link to the preceding chapter. End on an image or question that leads into the next chapter’s actual opening scene.

Keep sequential [n] anchors beside their claims and preserve matching evidence and provenance in the Notes as you move passages. Log companion or source issues for the apparatus chat. Work in batches, run python3 tools/lint.py from book/ on changed chapters, and read neighbouring chapter transitions aloud. Record the chapters revised, targeted lint results and remaining work in W4. The end goal is a voice pass across all three volumes.
```

### 2. Revise Notes and companion sections

```text
Apply the v3 Note architecture across The Book of the Million and reconcile the reader-facing companions. Start with book/VOICE-GUIDE.md, book/FRONT-BACK-MATTER.md, W3 and W5 in book/plans/content-revision-plan.md, the APP and GLO task files under book/plans/tasks/cross/, and book/plans/research/results/footnote-apparatus-models-raw.md. Use current manuscript files to establish what is already present. Start the chapter pass with II-3 and II-4, then move volume by volume as the voice batches settle.

Put each [n] next to the claim it supports and give it one matching Note. Begin with a ✓, ~, ✗ or ? verdict and write two or three readable sentences of curiosity, witness contrast, or authority and navigation. Use the bibliography, comparative witnesses and locator registries to retain checked claims and Chicago author-date citations. Name later witnesses in the Notes and keep the scope of their contribution clear. In II-3, recover the checked distinction between the club-bearing attendants and tall palace guards in the earlier Note 5, and the limits of the witness comparisons in the earlier Note 15. Use the project history and locator registry to recover that evidence.

Give longer material a findable home in the trivia and disputes files, glossaries, maps and city plans, appendices or the reliability essay and ledger. Update the reading key and companion index where the conventions or destinations change. Resolve II-3’s provisional banquet plate, Appendix C and ledger pointers against actual destinations. Decide whether an appendix needs to be created by checking what the existing companions already cover. Verify names against the gazetteer and character registry. Check every edited cross-reference against its current target, lint changed manuscript files, and verify that a representative build pairs each anchor with its endnote. Record remaining source or destination gaps in W5.
```

### 3. Add supporting images and research visual gaps

```text
Build out the supporting visuals for The Book of the Million. Read book/plans/illustration-plan.md, illustration-style-guide.md, image-generation-guide.md, multimedia-plan.md, and the PLT and MAP tasks under book/plans/tasks/cross/. Inventory the existing plates, maps, diagrams and attributions before choosing what to add. Start in Volume II with II-3’s planned White Feast procession and the banquet plate pointer, and II-4’s existing Liu Guandao hunting scroll and proposed elephant-litter scene. Check which images are already usable and which would help the reader understand a scene or orient themselves. Continue across volumes using the existing priorities.

Prefer verified period artwork or objects with suitable rights. Use historically grounded illustrations where existing material leaves a gap. Use book/plans/registry/pd-sources.md, visual-references.md, the relevant chapter tasks and the S-17, S-22 and S-23 research handoffs before commissioning anything. If a detail would change a composition or caption and the sources leave it open, research that question specifically. Record the source, what it supports, and any uncertainty. Leave a focused spike in book/plans/spikes/ for a question that needs a separate investigation.

Place accepted assets using the established conventions and record source, credits, rights and reconstruction status in the appropriate caption and book/media/ATTRIBUTIONS.md. Match plate and map identifiers to what readers can actually find. Coordinate figure placement with the chapter edits, then run a representative book build and inspect the pages for legibility, crop, resolution and captions. Report what was placed, what research changed, and what remains queued.
```

## Earlier handoffs (2026-11-17)

The earlier voice and locator prompts below record the work as it stood before v3. Use the current prompts above for that work. Research prompts for an external deep-research tool are in [the research handoff](research/2026-11-17-next-research-prompts.md).

### 1. Intake of a research return (use whenever a return comes back)

```text
A research return has been saved, unedited, at book/plans/research/results/<ID>-raw.md (from the prompt in book/plans/research/<prompt file>). Run an intake following book/plans/research/README.md, "Trust rules" and "Output contract":
- Spot-check at least 10 of its citations (or all, if fewer) by opening the sources yourself. Record each check (source, proposition, hit/partial/miss, access level) in results/<ID>-intake.md, with the hit rate. Below 80%, recommend a stricter rerun rather than salvaging.
- Re-read the current manuscript text for every claim before proposing a change; other sessions may have edited it.
- Add checked findings to book/plans/registry/facts.md (next F- number), new works to registry/bibliography.bib with a status comment, and a "<ID> source handoff" section to each affected chapter task file under book/plans/tasks/chapters/. Do not edit chapter text unless I ask.
- Run python3 tools/sources_index.py and python3 -m unittest discover -s tests -q from book/. Report the hit rate, what changes in the manuscript, and what stays open.
```

### 2. Earlier one-chapter voice prompt (S-01)

Run one chapter per chat. Chapters are independent, but a chat should only touch its own chapter and task files.

```text
Re-voice book/vol-2/ch-03-feasts-keshican.md to the S-01 standard. Its task is "II-03.T3" in book/plans/tasks/chapters/vol-2/II-03-feasts-keshican.md; apply that task's "Do" list and every source handoff section in the same file (S-21, U-1/U-2/U-3 and others), which state the corrections to keep.
Read first: book/VOICE-GUIDE.md (voice, length, markers, Ramusio flags, citations), book/plans/spikes/S-01-voice-standard.md (the approved II-2 pilot and what it showed), and book/vol-2/ch-02-person-palace.md as the model.
Rules: retell, do not paraphrase line by line; verbatim ≤ 15% (measured by tools/lint.py); keep every fact, Note number and citation key; do not drop hedges or ✗ verdicts; flag Ramusio-only passages inline and label them "Ramusio-only." in the Note; no scaffolding or tooling language.
Done when python3 tools/lint.py vol-2/ch-03-feasts-keshican.md (run from book/) shows no errors, the warnings are listed for my human read, and the task's "Done when" line is met. Show me a short before/after summary (word count, verbatim %, asides, hinges) and update the task's status.
```

To run another chapter, change the two paths and the task ID (e.g. `vol-2/ch-04-hunt-traffic.md` / `II-04.T3`; `vol-2/ch-08-mien-bangala.md` / `II-08.T3`).

### 3. Small W1 corrections left over (one short chat)

```text
Apply two decided corrections from book/plans/content-revision-plan.md, W1 items 4 and 5; check the current text first.
(a) Curzola: Jacopo d'Acqui puts Marco's capture at Ayas; Curzola comes from Ramusio plus inference. Fix the attributions in book/vol-1/back-01-trivia-and-disputes.md (around lines 15 and 33), book/vol-1/front-01-world-before-the-road.md Note [6], and book/vol-3/ch-12-reliability-essay.md (around line 27, and Note [4]). Confirm Jacopo's wording in Yule–Cordier's Introduction (book/refs/yule-vol1.txt) before editing, and cite it.
(b) The Xi'an stele: III-12 lists the Nestorian stele's absence from the Book as a "miss" (around line 41). The stele was unearthed c. 1623–25, so Polo could not have seen it; remove it from the misses or say why it is not one.
Run python3 tools/lint.py on the changed files from book/ and show that no new errors appear on the edited lines. Mark the items done in book/plans/content-revision-plan.md and the relevant chapter task files.
```

### 4. Yule chapter locators on every Note (APP.T5), then per-work keys (APP.T6)

```text
Do task APP.T5 in book/plans/tasks/cross/APP-apparatus.md: for each Note with no [@yc, …] locator, match its body paragraph against Yule's chapters with tools/cite_locate.py (5-gram overlap) and add the locator only where the task's threshold is met (≥ 8 shared 5-grams and at least twice the runner-up, inside the chapter's Yule range). Write the unmatched Notes to the worklist the task names. Do not change any claim or marker. Then, if time allows, start APP.T6 (per-work keys for "As cited in Yule" names), logging every decision.
Run python3 tools/lint.py and the tests from book/ before and after; the only change should be fewer Notes without a source. Avoid chapters another chat is re-voicing (II-03, II-04, II-08 this round).
```

### 5. Build work (one chat; build tooling only)

```text
Work on the build tasks in book/plans/tasks/cross/BLD-build-tooling.md, in this order, touching only tools/ and build docs:
(1) BLD.T3: one command that runs the map and timeline self-tests and regenerates all media (tools/media/map.py and timeline.py; see their headers).
(2) BLD.T9: citation parity in previews and EPUB. Make a Pandoc citeproc path with a Chicago author-date CSL that prints the YC and YC Add. sigla and locators like the PDF does ("YC 1.61", "YC Add. on 2.23"), and lists only the volume's cited works. Verify against the print build with real Notes.
(3) BLD.T10, if time allows: source-aware checking of comparative quotations against named texts in book/refs/, keeping the existing Yule-only 7-gram metric unchanged.
For each, meet the task's "Done when" line, add a small test where logic is non-trivial, run python3 -m unittest discover -s tests -q from book/, and update the task status.
```

### Items kept in the original chat

- **Committing** today's work: do it in this chat or your own terminal, so one person reviews what goes in.
- **S-22 and S-23 plate production**: wait for R-3 (period visual sources) first.
