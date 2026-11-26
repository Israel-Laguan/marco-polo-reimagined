"""Build the three volumes and report proof details or package a release."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from edition import load
from paths import ASSETS, BIBLIOGRAPHY, ROOT

OUTPUT = ROOT / "build"
BUILD = ROOT / "tools/build/build.sh"


def command(*args, **kwargs):
    return subprocess.run(args, cwd=ROOT, check=True, **kwargs)


def sha256(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def fingerprint(pdf):
    digest = hashlib.sha256()
    with TemporaryDirectory() as temporary:
        prefix = Path(temporary) / "page"
        command("pdftoppm", "-r", "96", "-png", pdf, prefix)
        pages = sorted(prefix.parent.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
        if not pages:
            raise ValueError(f"{pdf}: no PDF pages rendered")
        for page in pages:
            digest.update(bytes.fromhex(sha256(page)))
    text = command("pdftotext", "-layout", pdf, "-", stdout=subprocess.PIPE).stdout
    return {"pages": len(pages), "visual_sha256": digest.hexdigest(),
            "text_sha256": hashlib.sha256(text).hexdigest()}


def check_grammar(name, text):
    with (OUTPUT / f"{name}.grammar.json").open("w") as report:
        command("java", "-Xmx768m", "-jar", os.environ["LANGUAGETOOL_JAR"],
                "--json", "-l", "en-GB", "--encoding", "UTF-8", text, stdout=report)
    data = json.loads((OUTPUT / f"{name}.grammar.json").read_text())
    return len(data["matches"])


def check_latex(name):
    with (OUTPUT / f"{name}.chktex.log").open("w") as report:
        result = subprocess.run(["chktex", "-q", str(OUTPUT / f"{name}.tex")],
                                cwd=ROOT, stdout=report, stderr=subprocess.STDOUT)
    if result.returncode not in (0, 1, 2, 3):
        result.check_returncode()
    return sum(line.startswith(("Warning ", "Error ", "Message "))
               for line in (OUTPUT / f"{name}.chktex.log").read_text().splitlines())


def build_volume(name, lint):
    command(BUILD, name, env={**os.environ, "BOOK_STRICT": "1"})
    command(BUILD, "txt", name)
    pdf = OUTPUT / f"{name}.pdf"
    text = OUTPUT / f"{name}.txt"
    result = fingerprint(pdf)
    page_info = command("pdfinfo", pdf, text=True, stdout=subprocess.PIPE).stdout
    if "432 x 648 pts" not in page_info:
        raise ValueError(f"{pdf}: expected 6 × 9 inch trim")
    result["txt_sha256"] = sha256(text)
    result["layout_warnings"] = sum(
        "Overfull " in line for line in (OUTPUT / f"{name}.log").read_text(errors="replace").splitlines()
    )
    if lint:
        result["grammar_findings"] = check_grammar(name, text)
        result["latex_findings"] = check_latex(name)
    return name, result


def recorded_assets(name):
    directory = ROOT
    for line in (OUTPUT / f"{name}.fls").read_text().splitlines():
        if line.startswith("PWD "):
            directory = Path(line.removeprefix("PWD "))
        elif line.startswith("INPUT "):
            path = (directory / line.removeprefix("INPUT ")).resolve()
            if path.is_relative_to(ASSETS):
                yield path


def pack_latex(destination, names):
    files = {
        str(path.relative_to(ROOT)): path
        for path in {BIBLIOGRAPHY, ASSETS / "ATTRIBUTIONS.md", ROOT / "LICENSE"}
        | {path for name in names for path in recorded_assets(name)}
    }
    files.update({f"{name}.tex": OUTPUT / f"{name}.tex" for name in names})
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for name, source in sorted(files.items()):
            entry = ZipInfo(name)
            entry.compress_type = ZIP_DEFLATED
            archive.writestr(entry, source.read_bytes())
        readme = ZipInfo("README.txt")
        readme.compress_type = ZIP_DEFLATED
        archive.writestr(
            readme,
            "Build from this directory with latexmk -lualatex -halt-on-error vol1.tex.\n"
            "Repeat for vol2.tex and vol3.tex. The build uses LuaLaTeX, latexmk, Biber,\n"
            "biblatex-chicago, Noto Serif, Noto Serif CJK SC and DejaVu Sans.\n"
            "Image credits are in manuscript/assets/ATTRIBUTIONS.md.\n",
        )


def build(lint):
    manifest = load()
    OUTPUT.mkdir(exist_ok=True)
    if lint:
        for log, arguments in (
            ("manuscript-lint.log", ("python3", "tools/lint.py", "-v")),
            ("tests.log", ("python3", "-m", "unittest", "discover", "-s", "tests", "-q")),
        ):
            report = OUTPUT / log
            with report.open("w") as stream:
                result = subprocess.run(arguments, cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
            print(report.read_text(), end="", flush=True)
            result.check_returncode()
    names = [volume["id"] for volume in manifest["volumes"]]
    # Avoid simultaneous LaTeX font-cache initialization and Java memory spikes.
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = dict(pool.map(lambda name: build_volume(name, lint), names))
    return manifest["version"], results


def release_files(version, volumes):
    directory = OUTPUT / "release"
    directory.mkdir(exist_ok=True)
    prefix = f"the-book-of-the-million-v{version}"
    for name in volumes:
        for suffix in ("pdf", "txt"):
            shutil.copyfile(OUTPUT / f"{name}.{suffix}", directory / f"{prefix}-{name}.{suffix}")
    pack_latex(directory / f"{prefix}-latex.zip", volumes)
    assets = sorted(p for p in directory.iterdir() if p.name != "SHA256SUMS")
    (directory / "SHA256SUMS").write_text("".join(f"{sha256(p)}  {p.name}\n" for p in assets))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["proof", "release"])
    parser.add_argument("--approved", type=Path)
    args = parser.parse_args()
    lint = args.mode == "proof"
    version, results = build(lint)
    if lint:
        (OUTPUT / "proof-files.json").write_text(json.dumps(results, indent=2) + "\n")
        return
    if not args.approved:
        parser.error("Release packaging requires verified proof metadata")
    proof = json.loads(args.approved.read_text())
    for name, result in results.items():
        metrics = ("pages", "visual_sha256", "text_sha256", "txt_sha256")
        if any(result[key] != proof["volumes"][name][key] for key in metrics):
            raise SystemExit(f"{name}: release build differs from the approved proof")
    if version != proof["version"]:
        raise SystemExit("The release version differs from the approved proof")
    release_files(version, results)


if __name__ == "__main__":
    main()
