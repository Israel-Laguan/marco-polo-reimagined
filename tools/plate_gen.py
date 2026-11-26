"""Generate plate candidates (S-10). Stdlib only.

usage: python3 tools/plate_gen.py PROMPT_FILE --scale 4:3 --n 4 --out build/artwork/<plate> [--provider akool|klein]

PROMPT_FILE is plain text; an optional line starting with 'NEGATIVE:' begins the negative prompt.
Env: AKOOL_API_KEY (akool), NVIDIA_API_KEY (klein). Each image gets a .json with prompt, params and job id.
"""
import argparse, base64, json, os, time, urllib.request
from pathlib import Path

AKOOL = "https://openapi.akool.com/api/open"
# NIM klein: any /16 size up to 1,062,400 px, prompt <= 800 chars, no negative field.
KLEIN_DIMS = {"4:3": (1184, 880), "3:4": (880, 1184), "16:9": (1360, 768)}


def http(url, body=None, headers=None):
    req = urllib.request.Request(url, body and json.dumps(body).encode(),
                                 {"Content-Type": "application/json", **(headers or {})})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def akool(prompt, neg, scale):
    key = {"x-api-key": os.environ["AKOOL_API_KEY"]}
    body = {"prompt": prompt, "scale": scale, "resolution": "4k"} | ({"negative_prompt": neg} if neg else {})
    r = http(f"{AKOOL}/v4/content/image/createBySourcePrompt", body, key)
    if r.get("code") != 1000:
        raise RuntimeError(r)
    jid = r["data"]["_id"]
    for _ in range(60):  # jobs take ~30-60 s
        time.sleep(5)
        d = http(f"{AKOOL}/v3/content/image/infobymodelid?image_model_id={jid}", headers=key)["data"]
        if d["image_status"] == 3:
            with urllib.request.urlopen(d["image"], timeout=120) as f:  # URL expires after 7 days
                return f.read(), body | {"model": r["data"].get("model_name"), "job_id": jid,
                                         "credits": r["data"].get("deduction_credit")}
        if d["image_status"] == 4:
            raise RuntimeError(f"akool job {jid} failed")
    raise RuntimeError(f"akool job {jid} timed out")


def klein(prompt, neg, scale, seed):
    w, h = KLEIN_DIMS[scale]
    body = {"prompt": prompt[:800], "width": w, "height": h, "seed": seed, "steps": 4}
    a = http("https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.2-klein-4b", body,
             {"Authorization": f"Bearer {os.environ['NVIDIA_API_KEY']}", "Accept": "application/json"})["artifacts"][0]
    if a.get("finishReason") == "CONTENT_FILTERED":
        raise RuntimeError("content filtered")
    return base64.b64decode(a["base64"]), body | {"model": "flux.2-klein-4b"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt_file")
    ap.add_argument("--scale", default="4:3", choices=["4:3", "3:4", "16:9"])
    ap.add_argument("--n", type=int, default=4)
    ap.add_argument("--out", required=True)
    ap.add_argument("--provider", default="akool", choices=["akool", "klein"])
    a = ap.parse_args()
    text = Path(a.prompt_file).read_text()
    prompt, _, neg = text.partition("NEGATIVE:")
    prompt, neg = " ".join(prompt.split()), " ".join(neg.split())
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    stem = Path(a.prompt_file).stem
    for i in range(1, a.n + 1):
        t = time.time()
        try:
            img, params = akool(prompt, neg, a.scale) if a.provider == "akool" else klein(prompt, neg, a.scale, i)
        except Exception as e:
            print(f"FAIL {stem} #{i}: {e}")
            continue
        ext = "jpg" if img[:2] == b"\xff\xd8" else "png"
        path = out / f"{stem}-{a.provider}-{time.strftime('%Y%m%d-%H%M%S')}-{i}.{ext}"
        path.write_bytes(img)
        path.with_suffix(path.suffix + ".json").write_text(json.dumps(
            {"prompt": prompt, "negative_prompt": neg, "params": params, "secs": round(time.time() - t, 1),
             "date": time.strftime("%Y-%m-%d")}, indent=1))
        print(f"OK {path}")


if __name__ == "__main__":
    main()
