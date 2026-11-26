#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
docker build --pull --tag million-publishing -f tools/ci/Dockerfile tools/ci
docker run --rm --user "$(id -u):$(id -g)" --tmpfs /tmp:exec \
  --env HOME=/tmp --env SOURCE_DATE_EPOCH --volume "$PWD:/book" \
  million-publishing python3 tools/ci/build_edition.py "$@"
