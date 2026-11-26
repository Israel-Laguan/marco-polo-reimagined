"""Record proof identity, check owner sign-off, and publish approved editions."""

import argparse
import json
import os
from pathlib import Path
import shutil
from subprocess import PIPE, run
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_edition import sha256
from edition import approved, load, version_key
from paths import ROOT

OUTPUT = ROOT / "build"
APPROVAL_ARTIFACT = "book-approved-proof"
CHECKS_WORKFLOW = "book-checks.yml"


def execute(*args, **kwargs):
    return run(args, cwd=ROOT, check=True, text=True, **kwargs)


def git(*args):
    return execute("git", *args, stdout=PIPE).stdout.strip()


def api(endpoint, paginate=False, data=None):
    args = ["gh", "api", f"repos/{os.environ['GITHUB_REPOSITORY']}/{endpoint}"]
    if paginate:
        args.extend(("--paginate", "--slurp"))
    if data is not None:
        args.extend(("--input", "-"))
    response = execute(*args, input=json.dumps(data) if data is not None else None, stdout=PIPE)
    return json.loads(response.stdout)


def output(name, value):
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as target:
        target.write(f"{name}={value}\n")


def eligible(pr):
    return (
        pr["base"]["ref"] == "main"
        and pr["head"]["ref"] == "staging"
        and pr["head"]["repo"]
        and pr["head"]["repo"]["full_name"] == os.environ["GITHUB_REPOSITORY"]
    )


def proof_context(event):
    pr = event.get("pull_request")
    release = bool(pr and pr["base"]["ref"] == "main")
    if release and not eligible(pr):
        raise ValueError("Release PRs must come from this repository's staging branch")
    version = load()["version"]
    if release:
        # First publication follows a bootstrap commit with no edition manifest.
        entry = "HEAD^1:manuscript/edition.json"
        base = run(("git", "show", entry), cwd=ROOT, text=True, capture_output=True)
        if base.returncode == 0 and version_key(version) <= version_key(json.loads(base.stdout)["version"]):
            raise ValueError("Bump the edition version before opening a release PR")
        if any(r["tag_name"] == f"v{version}" for r in releases()):
            raise ValueError(f"v{version} already has a release; choose a new version")
        if git("ls-remote", "--tags", "origin", f"refs/tags/v{version}"):
            raise ValueError(f"v{version} is already tagged; choose a new version")
    head = pr["head"]["sha"] if pr else git("rev-parse", "HEAD")
    return {
        "run": os.environ["GITHUB_RUN_ID"],
        "attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "pr": pr["number"] if pr else None,
        "head": head,
        "tree": git("rev-parse", "HEAD^{tree}"),
        "epoch": git("show", "-s", "--format=%ct", head),
        "version": version,
    }


def prepare(event):
    proof = proof_context(event)
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "proof.json").write_text(json.dumps(proof, indent=2) + "\n")
    output("epoch", proof["epoch"])


def summarize():
    path = OUTPUT / "proof.json"
    proof = json.loads(path.read_text())
    proof["volumes"] = json.loads((OUTPUT / "proof-files.json").read_text())
    path.write_text(json.dumps(proof, indent=2) + "\n")
    body = [
        f"## Edition {proof['version']}", "",
        f"Proof: `{proof['run']}.{proof['attempt']} {proof['head']}`", "",
        "| Volume | Pages | Overfull boxes | Grammar findings | ChkTeX findings |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for name, checks in proof["volumes"].items():
        body.append(f"| {name} | {checks['pages']} | {checks['layout_warnings']} | "
                    f"{checks['grammar_findings']} | {checks['latex_findings']} |")
    body += ["", "The proof artifact contains PDFs, text, and full lint reports.",
             "The print build verified glyphs, citations, references, and print assets."]
    with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a") as summary:
        summary.write("\n".join(body) + "\n")


def signoff(event):
    pr = event["pull_request"]
    proof = json.loads((OUTPUT / "proof.json").read_text())
    if not eligible(pr) or (
        proof["pr"], proof["head"], proof["run"], proof["attempt"]
    ) != (
        pr["number"], pr["head"]["sha"], os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    ):
        raise ValueError("The proof does not match this pull request and run attempt")
    pages = api(f"issues/{proof['pr']}/comments?per_page=100", paginate=True)
    comments = [comment for page in pages for comment in page]
    approvals = api(f"actions/runs/{proof['run']}/approvals")
    owner = int(event["repository"]["owner"]["id"])
    if not approved(proof, owner, comments, approvals):
        raise ValueError("Add the completed owner checklist for this proof, then approve book-signoff")
    shutil.copyfile(OUTPUT / "proof.json", OUTPUT / "approved.json")


def select_approval(pr):
    head = pr["head"]["sha"]
    sha = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    if not eligible(pr) or not pr["merged"] or pr["merge_commit_sha"] != sha or git("rev-parse", "HEAD^2") != head:
        raise ValueError("Expected the exact staging-to-main merge commit")
    pages = api(f"actions/workflows/{CHECKS_WORKFLOW}/runs?event=pull_request"
                f"&head_sha={head}&status=success&per_page=100", paginate=True)
    OUTPUT.mkdir(exist_ok=True)
    for page in pages:
        for candidate in page["workflow_runs"]:
            attempt = candidate["run_attempt"]
            artifacts = api(f"actions/runs/{candidate['id']}/artifacts?name={APPROVAL_ARTIFACT}-{attempt}")
            if not any(not asset["expired"] for asset in artifacts["artifacts"]):
                continue
            folder = OUTPUT / "approval"
            execute("gh", "run", "download", str(candidate["id"]),
                    "--name", f"{APPROVAL_ARTIFACT}-{attempt}", "--dir", str(folder))
            path = folder / "approved.json"
            proof = json.loads(path.read_text())
            if (proof["pr"], proof["head"], proof["tree"], proof["version"]) == (
                pr["number"], head, tree, load()["version"]
            ) and (proof["run"], proof["attempt"]) == (str(candidate["id"]), str(attempt)):
                output("epoch", proof["epoch"])
                return
            path.unlink()
    raise ValueError("The merged tree has no matching, successful owner-approved proof")


def releases():
    return [item for page in api("releases?per_page=100", paginate=True) for item in page]


def matching_assets(directory, uploaded):
    assets = {}
    for entry in uploaded:
        name = entry["name"]
        local = directory / name
        if local.parent != directory or not local.is_file() or entry["state"] != "uploaded":
            raise ValueError(f"Unexpected or incomplete release asset {name}")
        if entry["size"] != local.stat().st_size or entry["digest"] != f"sha256:{sha256(local)}":
            raise ValueError(f"Published asset verification failed for {name}")
        assets[name] = entry
    return assets


def publish(directory, version, commit):
    tag = f"v{version}"
    existing = [item for item in releases() if item["tag_name"] == tag]
    if len(existing) > 1:
        raise ValueError(f"Multiple releases found for {tag}")
    expected = {"SHA256SUMS", f"the-book-of-the-million-{tag}-latex.zip"}
    expected.update(f"the-book-of-the-million-{tag}-vol{i}.{suffix}"
                    for i in range(1, 4) for suffix in ("pdf", "txt"))
    if {p.name for p in directory.iterdir()} != expected:
        raise ValueError("The release must contain all three PDFs, three text editions, LaTeX, and checksums")
    if existing:
        release = existing[0]
    else:
        release = api("releases", data={
            "tag_name": tag,
            "target_commitish": commit,
            "name": f"The Book of the Million {tag}",
            "body": f"Volumes I–III, rebuilt from the approved manuscript at {commit}.",
            "draft": True,
            "prerelease": "-rc." in version,
        })
    if release["target_commitish"] != commit or release["prerelease"] != ("-rc." in version):
        raise ValueError(f"{tag} belongs to a different source or release type")
    release_id = release["id"]
    if not release["draft"]:
        if matching_assets(directory, release["assets"]).keys() != expected:
            raise ValueError(f"{tag} is already published with different files")
        return
    uploaded_assets = []
    for asset in release["assets"]:
        if asset["name"] in expected and asset["state"] == "starter" and asset["size"] == 0:
            endpoint = f"repos/{os.environ['GITHUB_REPOSITORY']}/releases/assets/{asset['id']}"
            execute("gh", "api", "--method", "DELETE", endpoint)
        else:
            uploaded_assets.append(asset)
    uploaded = matching_assets(directory, uploaded_assets)
    for name in sorted(expected - uploaded.keys()):
        execute("gh", "release", "upload", tag, str(directory / name))
    uploaded = matching_assets(directory, api(f"releases/{release_id}")["assets"])
    if uploaded.keys() != expected:
        raise ValueError("Draft remains unpublished because assets are incomplete")
    execute("gh", "api", "--method", "PATCH",
            f"repos/{os.environ['GITHUB_REPOSITORY']}/releases/{release_id}",
            "-F", "draft=false", stdout=PIPE)
    print(f"Published {tag}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("step", choices=["prepare", "summarize", "signoff", "select-approval", "publish"])
    args = parser.parse_args()
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    if args.step == "prepare":
        prepare(event)
    elif args.step == "summarize":
        summarize()
    elif args.step == "signoff":
        signoff(event)
    elif args.step == "select-approval":
        select_approval(event["pull_request"])
    elif args.step == "publish":
        publish(OUTPUT / "release", load()["version"], git("rev-parse", "HEAD"))


if __name__ == "__main__":
    main()
