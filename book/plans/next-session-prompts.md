# Prompts for other Claude Code chats (2026-11-17)

Each block is a self-contained task for a new Claude Code chat opened in this repository. They touch different files, so they can run in parallel, except where noted. **Commit today's work first**: a new chat on a fresh worktree or branch would not see uncommitted changes.

Research prompts for an external deep-research tool are in [`research/2026-11-17-next-research-prompts.md`](research/2026-11-17-next-research-prompts.md).

## 1. Intake of a research return (use whenever a return comes back)

```text
A research return has been saved, unedited, at book/plans/research/results/<ID>-raw.md (from the prompt in book/plans/research/<prompt file>). Run an intake following book/plans/research/README.md, "Trust rules" and "Output contract":
- Spot-check at least 10 of its citations (or all, if fewer) by opening the sources yourself. Record each check (source, proposition, hit/partial/miss, access level) in results/<ID>-intake.md, with the hit rate. Below 80%, recommend a stricter rerun rather than salvaging.
- Re-read the current manuscript text for every claim before proposing a change; other sessions may have edited it.
- Add checked findings to book/plans/registry/facts.md (next F- number), new works to registry/bibliography.bib with a status comment, and a "<ID> source handoff" section to each affected chapter task file under book/plans/tasks/chapters/. Do not edit chapter text unless I ask.
- Run python3 tools/sources_index.py and python3 -m unittest discover -s tests -q from book/. Report the hit rate, what changes in the manuscript, and what stays open.
```

## 2. Re-voice one chapter (W4; batch 1 is II-03, II-04, II-08)

Run one chapter per chat. Chapters are independent, but a chat should only touch its own chapter and task files.

```text
Re-voice book/vol-2/ch-03-feasts-keshican.md to the S-01 standard. Its task is "II-03.T3" in book/plans/tasks/chapters/vol-2/II-03-feasts-keshican.md; apply that task's "Do" list and every source handoff section in the same file (S-21, U-1/U-2/U-3 and others), which state the corrections to keep.
Read first: book/VOICE-GUIDE.md (voice, length, markers, Ramusio flags, citations), book/plans/spikes/S-01-voice-standard.md (the approved II-2 pilot and what it showed), and book/vol-2/ch-02-person-palace.md as the model.
Rules: retell, do not paraphrase line by line; verbatim ≤ 15% (measured by tools/lint.py); keep every fact, Note number and citation key; do not drop hedges or ✗ verdicts; flag Ramusio-only passages inline and label them "Ramusio-only." in the Note; no scaffolding or tooling language.
Done when python3 tools/lint.py vol-2/ch-03-feasts-keshican.md (run from book/) shows no errors, the warnings are listed for my human read, and the task's "Done when" line is met. Show me a short before/after summary (word count, verbatim %, asides, hinges) and update the task's status.
```

To run another chapter, change the two paths and the task ID (e.g. `vol-2/ch-04-hunt-traffic.md` / `II-04.T3`; `vol-2/ch-08-mien-bangala.md` / `II-08.T3`).

## 3. Small W1 corrections left over (one short chat)

```text
Apply two decided corrections from book/plans/content-revision-plan.md, W1 items 4 and 5; check the current text first.
(a) Curzola: Jacopo d'Acqui puts Marco's capture at Ayas; Curzola comes from Ramusio plus inference. Fix the attributions in book/vol-1/back-01-trivia-and-disputes.md (around lines 15 and 33), book/vol-1/front-01-world-before-the-road.md Note [6], and book/vol-3/ch-12-reliability-essay.md (around line 27, and Note [4]). Confirm Jacopo's wording in Yule–Cordier's Introduction (book/refs/yule-vol1.txt) before editing, and cite it.
(b) The Xi'an stele: III-12 lists the Nestorian stele's absence from the Book as a "miss" (around line 41). The stele was unearthed c. 1623–25, so Polo could not have seen it; remove it from the misses or say why it is not one.
Run python3 tools/lint.py on the changed files from book/ and show that no new errors appear on the edited lines. Mark the items done in book/plans/content-revision-plan.md and the relevant chapter task files.
```

## 4. Yule chapter locators on every Note (APP.T5), then per-work keys (APP.T6)

```text
Do task APP.T5 in book/plans/tasks/cross/APP-apparatus.md: for each Note with no [@yc, …] locator, match its body paragraph against Yule's chapters with tools/cite_locate.py (5-gram overlap) and add the locator only where the task's threshold is met (≥ 8 shared 5-grams and at least twice the runner-up, inside the chapter's Yule range). Write the unmatched Notes to the worklist the task names. Do not change any claim or marker. Then, if time allows, start APP.T6 (per-work keys for "As cited in Yule" names), logging every decision.
Run python3 tools/lint.py and the tests from book/ before and after; the only change should be fewer Notes without a source. Avoid chapters another chat is re-voicing (II-03, II-04, II-08 this round).
```

## 5. Build work (one chat; build tooling only)

```text
Work on the build tasks in book/plans/tasks/cross/BLD-build-tooling.md, in this order, touching only tools/ and build docs:
(1) BLD.T3: one command that runs the map and timeline self-tests and regenerates all media (tools/media/map.py and timeline.py; see their headers).
(2) BLD.T9: citation parity in previews and EPUB. Make a Pandoc citeproc path with a Chicago author-date CSL that prints the YC and YC Add. sigla and locators like the PDF does ("YC 1.61", "YC Add. on 2.23"), and lists only the volume's cited works. Verify against the print build with real Notes.
(3) BLD.T10, if time allows: source-aware checking of comparative quotations against named texts in book/refs/, keeping the existing Yule-only 7-gram metric unchanged.
For each, meet the task's "Done when" line, add a small test where logic is non-trivial, run python3 -m unittest discover -s tests -q from book/, and update the task status.
```

## Not for another chat

- **Committing** today's work: do it in this chat or your own terminal, so one person reviews what goes in.
- **S-22 and S-23 plate production**: wait for R-3 (period visual sources) first.
