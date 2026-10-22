# BLD — Build and tooling

**Status:** backlog · **Plan docs:** `content-revision-plan.md` § W0; `multimedia-plan.md` § Toolchain

## Scope
Everything that turns the Markdown repo into checked and typeset output: lint, LaTeX build, media generation scripts, commit hooks.

## Backlog
- None of pandoc, LuaLaTeX, matplotlib or cartopy is installed (system install needs user approval).
- Seed scripts in `tools/seed/` (overlap, stats, Ramusio brackets).
- Vector swap (`.svg/.png` → `.pdf`) Lua filter; per-chapter endnotes; fonts with Unicode + CJK coverage.

## Gated by spikes
S-02 (lint) · S-08 (LaTeX) · S-09 (media scripts)

## Tasks
_After the spikes:_ `BLD.T1` lint in a pre-commit script · `BLD.T2` full-book build · `BLD.T3` media regeneration (one command) · `BLD.T4` front/back matter, index, glossary layout
