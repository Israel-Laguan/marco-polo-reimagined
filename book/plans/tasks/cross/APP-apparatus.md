# APP — Apparatus

**Status:** backlog · **Plan doc:** `content-revision-plan.md` § W3, § W5; S-03

## Scope
Series-wide reader apparatus: reliability markers, [V]/[R]/[M] tags, the "How to read this book" box, Ramusio flag convention, Notes hygiene rules, epigraph policy. Per-chapter application happens in each chapter's `.T2`/`.T4`; this file holds the shared decisions and sweeps.

## Backlog
- About 80 ★ ratings in Notes with no legend (II-M7, III-M9); "★ Dispute:" duplicate Notes.
- Undefined compound tags [V/M], [R/M] (II-m10); tags missing in III-7 to III-12 (III-M8).
- No reader-facing explanation of the tags or markers (II-M8).
- About 60 unflagged Ramusio passages (I-M5, II-M1, III-M7). Bracket list in `tools/seed/brackets.txt`.
- Epigraph policy: exact Yule wording, or marked *(adapted)* (II-N5, III-C1).

## Decided (S-03, closed 2026-10-22)
Convention: `VOICE-GUIDE.md` § Apparatus conventions. Markers ✓ ~ ✗ ◇ ?; ★ retired; compound tags fold into [M]; [reception] for III-10 to III-12; Ramusio flag = inline words + "Ramusio-only." Note label (provenance, not a marker). The lint enforces tags, lead markers, "Dispute:" labels and the Ramusio label (`tools/lint.py`).

## Gated by spikes
S-03 ✓ · S-08 (rendering: confirm a font with ✓ ✗ ◇ glyphs; endnotes vs footnotes)

## Tasks
### APP.T1 — "How to read this book" box
- **Status:** backlog · **Depends:** S-03 ✓
- **Do:** add the full box (below, ≈150 words) to the front of `vol-1/front-01-world-before-the-road.md` as `::: howto … :::` after the epigraph rule; add the short form to `vol-2/front-01-yuan-china-context.md` and `vol-3/front-01-indian-ocean-world.md` (the Vol. III form adds `[reception]`). Vol. I's chapters carry no tags, so its box says tags begin in Vol. II.
- **Done when:** the three boxes are in place and the lint still shows no new errors in those files.

**Full form (Vol. I):**

> **How to read this book.** Each chapter retells one stretch of *Il Milione*. Small numbers in the text, like [3], point to the Notes at the end of the chapter, where a claim is checked against other witnesses. Every Note opens with a mark: ✓ corroborated by independent sources · ~ plausible, but a detail is under strain · ✗ probably wrong or exaggerated · ◇ marvel or hearsay, kept as the Book tells it · ? scholars disagree. From Volume II, each chapter also carries a tag: **[V]** mostly what Polo says he saw or did · **[R]** mostly what he heard · **[M]** a mixture. Some passages exist only in Ramusio's sixteenth-century version, or in Pipino's Latin or another later text. The story says so as it goes, and the Note labels them "Ramusio-only." Read them as later layers, not as Polo's earliest words.

**Short form (Vol. II; Vol. III adds "**[reception]** the Book's afterlife"):**

> **Reading the marks.** Notes open with ✓ corroborated · ~ plausible · ✗ probably wrong · ◇ marvel or hearsay · ? contested. Tags: **[V]** seen · **[R]** heard · **[M]** both. "Ramusio-only." labels a passage found only in a later text. Full key: Volume I, front matter.

### APP.T2 — ★ → marker sweep
- **Status:** backlog · **Depends:** S-03 ✓ · **Do first**, before the chapter re-voices
- **Do:** write `tools/star_sweep.py` that lists every ★ in Notes (81 across 19 files at baseline) with its clause and a proposed replacement per the sweep rules in the guide (★★★ → ✓, ★★ → ~, ★ → ?, deleted beside an existing marker, "Dispute:" dropped); a person confirms each; apply one commit per volume.
- **Done when:** `grep -rn "★" vol-*/` finds nothing in Notes, and the lint `markers` check reports no retired-marker errors.

### APP.T3 — Tag lines
- **Status:** backlog · **Depends:** S-03 ✓
- **Do:** apply the assigned tags: II-8, II-14, III-2, III-3, III-4, III-5 → `**[M]**`; III-7 `**[R]**`; III-8 `**[M]**`; III-9 `**[V]**`; III-10, III-11, III-12 `**[reception]**`. Each chapter's `.T4` confirms the tag against its content, so this task may be folded into those.
- **Done when:** the lint `tags` check passes for all 49 files.

### APP.T4 — Ramusio bracket check in the lint (with `BLD`)
- **Status:** partly done · **Depends:** S-02 ✓
- **Done (S-02/S-03):** the lint matches reproduced Ramusio passages, requires an inline flag and a "Ramusio-only." (or Pipino-/Jacopo-/Zelada-only) label in the cited Note.
- **Left:** the lint only sees near-verbatim passages, so paraphrased Ramusio detail escapes it. After the re-voices, compare flag counts with the manifest (already a warning) and spot-check against Yule's brackets (`tools/seed/ramusio-brackets.txt`, rebuilt without `Sidenote:` lines).
- **S-12 (2026-11-10), proposal:** a Ramusio-only Note cites the 1559 print (`ramusio1559navigationi`), and the open-access critical edition (`ramusio2015viaggi`) once the passage has been checked there.

### APP.T5 — A Yule chapter locator on every Note
- **Status:** ready · **Depends:** S-24 ✓ · **Origin:** citation sweep, 2026-10-22
- **Do:** for each Note with no `[@yc, …]`, find the body paragraph that carries its `[n]` and match it against Yule's chapters by 5-gram overlap (as in `tools/cite_locate.py`). Where one Yule chapter wins clearly (≥ 8 shared 5-grams and at least twice the runner-up) and lies inside the range the chapter covers, put `[@yc, b.c]` after the Note's opening marker. Weak and no-match cases go to a worklist, not into the text. A trial run on 2026-10-22: 252 clear in-range matches, 52 weak, 59 no match (mostly re-voiced passages), 1 clear match out of range.
- **Done when:** every clear match is placed; the worklist lists the rest; lint unchanged apart from fewer Notes without a source.

### APP.T6 — Per-work keys for the "As cited in Yule" names
- **Status:** ready · **Depends:** S-24 pass C ✓ (APP.T5 optional)
- **Do:** for each name in an "As cited in Yule" sentence, read Yule's own reference at the located spot (the *Yule's reference* column of `plans/status/pass-b-worklist.md`). Add the key (`Name [-@key]`) only where that reference names the same work as the bibliography entry: a matching title word, or a work Yule cites only once. Leave the name bare where the surname is shared, e.g. Baber (the emperor Babur in Vol. I, E. C. Baber in Vol. II) or Major (two different books). Log each attachment and each refusal.
- **Done when:** the log covers every name; the 68 uncited bibliography entries shrink to those with no safe match.
- **S-12 (2026-11-10):** new keys for names Yule cites: Bushell (`bushell1874notes`), Gaubil (`gaubil1739histoire`), De Mailla (`demailla1777histoire`), Wassaf (`hammer1856geschichte`, Yule's own translation), Carpini (`dawson1955mongol`, `menesto1989storia`), Odoric (`marchisio2016relatio`), Needham by volume. Three names still have no work: Huntingford (III-07), Elverskog (II-03), Subrahmanyam (III-05); pick one or drop the name.

### APP.T7 — Explain the base-text abbreviations
- **Status:** implemented 2026-11-11 · **Depends:** S-24; BLD.T4
- **Do:** place the following explanation under the *Abbreviations* heading, before the generated shorthand list. The list and *Works cited* remain limited to sources cited in that volume.

> **YC** refers to Henry Yule's translation of Marco Polo, third edition, revised by Henri Cordier (1903). **YC Add.** refers to Cordier's *Notes and Addenda* (1920). The Project Gutenberg editions are the copies consulted, not the dates of the original books.
>
> In a reference such as **YC 1.61**, the first number is the book and the second is the chapter: this is Book I, Chapter LXI in Yule's text. **YC Prol. 17–18** means Prologue chapters XVII–XVIII. An **n.** followed by a number refers to Yule's note to that chapter; **Intro. §** refers to a section of his Introduction.

- **Done when:** the explanation and generated list appear together in each volume's front matter and the shorthand list and bibliography still contain only that volume's cited works.
- **Verified 2026-11-11:** a focused PDF build test passes; all three full-volume PDFs place the explanation and shorthand list on their abbreviations page and include *Works cited*. The existing one-PDF-per-volume citation scope is unchanged. Broader front/back layout and human page review remain with BLD.T4.

### APP.T8 — Claim-level check of the S-25 keys
- **Status:** done (best effort) · **Depends:** S-25 ✓ · **Origin:** spike audit 2026-11-17
- **Do:** S-25 confirmed that the four works exist; it did not check what they say. For each of the 12 Notes that cite `derachewiltz1997marco` (6), `tao1959nancun` (3), `dutschke1993francesco` (2) and `atwood2004encyclopedia` (1), read the passage behind the claim. Then add a locator, correct the claim, or drop the citation, and log each outcome as `registry/locators.md` does.
- **Done when:** every one of the 12 has a recorded outcome, and there are no unread `pending` rows.
- **Progress 2026-11-17 ([R-1 intake](../../research/results/R-1-intake.md)):** Atwood supports the I-13 citation, for Shangdu only. Tao's Palm Hall is consistent with I-13 Note [4] (Dadu, not Shangdu). Wood's own positions are checked (F-59), but de Rachewiltz 1997 itself, the Tao 骨朵 passage (II-03 [5]) and Dutschke (I-01 [15], III-12 [4]) are still unread. **Status:** in progress.
- **Closed best effort 2026-11-17 ([FINAL-ACCESS intake](../../research/results/FINAL-ACCESS-intake.md)):** de Rachewiltz: the 1997 article stays unread, but his 2002 ANU paper (`derachewiltz2002wood`, read), which summarises it, confirms the replies the six Notes attribute (Wall after Waldron; Yangzhou: never governor, perhaps a temporary inspector or commissioner); added to II-11 [5] and I-11 [17]. Tao: II-03 [5] corrected (clubs and the tall guard are separate entries; no jade axes in juan 1). Dutschke: catalogue record only; I-01 [15] and III-12 [4] keep their hedged wording. **Status:** done (best effort).


### APP.T9 — Bounded apparatus cleanup (four known items)
- **Status:** backlog · **Depends:** S-03 ✓, S-26 ✓ (`registry/locators.md`), `APP.T2` for item 3 · **Origin:** targeted continuity pass, 2026-11-17 (critique follow-up)
- **Scope:** only the four items below. This task does **not** replace the series-wide citation work (`APP.T5`, `APP.T6`), the chapter Ramusio flags (`.T2`) or the per-chapter Notes passes (`.T4`); it gathers four small, reader-facing defects that are already known so one person can close and check them together. Where an item already belongs to a chapter task, that task stays the owner; this one tracks it to completion.
- **Do:**
  1. **I-04 orphan Note [15]** (owner `I-04.T4`; backlog item M10 in `tasks/chapters/vol-1/I-04-hermenia-georgiania.md`). Lint: "Note [15] is never cited". Anchor it at the sentence that makes its claim (the Caucasian block as personally traversed; the backlog proposes ch-04:37), or merge it into the Note that already covers that sentence if `I-04.T3` has moved the paragraph. Do not leave a pointer-only Note.
  2. **I-F1 out-of-order citations** (owner `I-F1.T4`; backlog m3 in `tasks/chapters/vol-1/I-F1-world-before-the-road.md`). Lint: "body citations not sequential … 9, 11, 10". Renumber body markers and Notes together so each Note keeps its claim. Note [6] was corrected on 2026-11-17 (F-34): keep that wording.
  3. **Marker sweep.** Run `APP.T2` (★ → ✓ ~ ✗ ◇ ?; **72 ★ in 17 files** on 2026-11-17) and, in the same reviewed pass, give a lead marker to every Note that lacks one (**49** lint `markers` errors of that kind on 2026-11-17, across the 27 files failing `markers`). Choose each marker from the Note's own claim and `registry/facts.md`; never upgrade a claim the registry hedges.
  4. **Reader-facing explanation of the apparatus.** Apply `APP.T1` (the three boxes). Check the boxes against the `APP.T7` abbreviations text and the `APP.T3` tag list so the three explanations agree; Vol. III's box adds `[reception]`.
- **Cautions:** `registry/locators.md` refers to original Note numbers; when a renumbering touches a Note it lists, update the row, not the checked locator. Do not change claims, keys or locators while renumbering or re-marking.
- **Done when:**
  - `python3 tools/lint.py vol-*/*.md` reports **0** `citations` errors (on 2026-11-17 the only two are items 1 and 2);
  - `grep -rn "★" vol-*/` finds nothing in Notes, and the lint `markers` check reports no retired-marker and no missing-lead-marker errors;
  - the three `APP.T1` boxes are in place with no new lint errors in those files;
  - **human review:** a person has confirmed each ★ and each new lead marker against its Note, read the renumbered Notes in I-04 and I-F1 against their anchors, and read the three boxes. Then mark `APP.T1`, `APP.T2` and the two chapter backlog items done; this task closes with them.
