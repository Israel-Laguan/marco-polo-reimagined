# GAZ — Gazetteer

**Status:** backlog · **Plan doc:** `content-revision-plan.md` § W5; S-04

## Scope
`gazetteer.csv` as the single authority for place names (prose) and coordinates (maps).

## Backlog
- `book_name` uses modern forms; the chapters use Yule's (I-M8 table: Bokhara/Bocara, Kashgar/Cascar…; II-M11; III-m4: Basman/Basma, Sememant/Semenat, Abyssinia/Abash, Kalhat/Calatu).
- Missing rows: about 27 (Vol. I), about 32 (Vol. II), about 8 (Vol. III); lists in the critiques.
- Wrong or conflicting IDs:
  - Cachanfu = Xi'an (wrong; II-M2);
  - Caugigu (Tonkin vs Kiang Hung);
  - Cacanfu (Puyang vs Hejian);
  - Nanghin (Nanjing vs Anqing);
  - two cities named Vuju;
  - Male = Maldives (III-m3);
  - Badakhshan alias "Balashan" wrong;
  - "Pazanjin / Hezhong" row unused and duplicates an ID.
- front-02 place tables (3 volumes) are generated from it, so regenerate them after the fix.

## Gated by spikes
S-04

## Tasks
_After S-04:_ `GAZ.T1` schema v2 · `GAZ.T2` rename to Yule forms + aliases · `GAZ.T3` missing rows · `GAZ.T4` resolve conflicts · `GAZ.T5` regenerate front-02 tables
