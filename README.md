# The Book of the Million

A three-volume retelling of *Le Devisement dou monde*, Marco Polo’s account as written down by Rustichello da Pisa. This edition follows the 1903 Yule–Cordier translation and includes endnotes, maps, timelines, and illustrated plates.

## Read the book

- [Volume I · From Venice to the Khan](manuscript/vol-1/README.md)
- [Volume II · The Realm of Kublai](manuscript/vol-2/README.md)
- [Volume III · Seas, Return, and After](manuscript/vol-3/README.md)
- [Published editions and downloads](https://github.com/Israel-Laguan/marco-polo-reimagined/releases)

## Work on the book

| Folder | Contents |
|---|---|
| [Manuscript](manuscript/) | Markdown, reading order, bibliography, and print assets |
| [Research](research/) | Source texts, evidence, gazetteer, and citation registries |
| [Materials](materials/) | Reusable art references, prompts, and figure sources |
| [Editorial](editorial/) | [Series status](editorial/SERIES-STATUS.md), [planning](editorial/plans/README.md), and [publishing guide](editorial/PUBLISHING.md) |
| [Archive](archive/) | Superseded drafts and retired artwork |
| [Tools](tools/) | Build scripts, lint, and media generators |

Open changes against `staging`. GitHub Actions produces downloadable proofs for review. A signed-off `staging` → `main` merge publishes the PDF and TXT editions and a buildable LaTeX package.

Run these from the repository root.

```sh
python3 tools/lint.py
python3 -m unittest discover -s tests -q
tools/build/build.sh vol1
tools/build/build.sh txt vol1
```

The build writes to the ignored `build/` directory. See the [tooling guide](tools/build/README.md) for dependencies and more formats.

## Licence

The project’s own text and code use the [Apache 2.0 licence](LICENSE). Images and quoted sources retain their individual terms. See the [media credits](manuscript/assets/ATTRIBUTIONS.md) and [reference texts](research/refs/).
