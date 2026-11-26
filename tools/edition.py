"""Validate the edition manifest and bind the publisher's sign-off to a proof."""

import argparse
import json
import re
from pathlib import Path

from paths import MANUSCRIPT

MANIFEST = MANUSCRIPT / "edition.json"
VERSION = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-rc\.[1-9]\d*)?")
REVIEW_ITEMS = (
    "Literary editing and voice",
    "Grammar and copyediting",
    "Historical claims and citations",
    "Art and image rights",
    "Final pagination and layout",
)


def load(path=MANIFEST):
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not VERSION.fullmatch(manifest["version"]) or not manifest["title"].strip():
        raise ValueError("The edition needs a title and a version such as 1.0.0-rc.1")
    expected = [(f"vol{i}", f"vol-{i}", "I" * i) for i in range(1, 4)]
    volumes = manifest["volumes"]
    if [(v["id"], v["directory"], v["number"]) for v in volumes] != expected:
        raise ValueError("List the three volumes in series order")
    for volume in volumes:
        directory = path.parent / volume["directory"]
        actual = {p.name for p in directory.glob("*.md") if p.name != "README.md"}
        files = volume["files"]
        if not files or not volume["title"].strip() or len(set(files)) != len(files) or set(files) != actual:
            raise ValueError(f"{directory}: list every manuscript file exactly once")
    return manifest


def version_key(version):
    numbers, sep, candidate = version.partition("-rc.")
    return (*map(int, numbers.split(".")), not sep, int(candidate or 0))


def approved(proof, owner, comments, approvals):
    proof_line = f"Proof: {proof['run']}.{proof['attempt']} {proof['head']}"
    required = {proof_line, *(f"- [x] {item}" for item in REVIEW_ITEMS)}
    for comment in reversed(comments):
        lines = set(line.strip() for line in comment["body"].splitlines())
        if comment["user"]["id"] == owner and proof_line in lines:
            if not required <= lines or not any(re.fullmatch(r"Findings: \S.*", line) for line in lines):
                return False
            break
    else:
        return False
    for review in reversed(approvals):
        if any(env["name"] == "book-signoff" for env in review["environments"]):
            return review["user"]["id"] == owner and review["state"] == "approved"
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("field", choices=["version", "arguments"])
    parser.add_argument("volume", nargs="?")
    args = parser.parse_args()
    manifest = load()
    if args.field == "version":
        print(manifest["version"])
        return
    volume = next((v for v in manifest["volumes"] if v["id"] == args.volume), None)
    if not volume:
        parser.error("Specify vol1, vol2, or vol3")
    metadata = {
        "title": volume["title"],
        "volume": f"Volume {volume['number']}",
        "volume-id": volume["number"],
        "series": manifest["title"],
    }
    for key, value in metadata.items():
        print("-M", f"{key}={value}", sep="\n")
    for name in volume["files"]:
        print(Path("manuscript") / volume["directory"] / name)


if __name__ == "__main__":
    main()
