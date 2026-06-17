#!/usr/bin/env bash
#
# Vercel build command. Regenerates lib/test-status.json from the live test
# results, then builds the Next.js app. The dashboard imports that JSON, so the
# unlock state is baked into each deployment.
#
# The status step is best-effort: if Python or pytest is unavailable in the
# build image we fall back to the committed lib/test-status.json rather than
# failing the deploy.
set -euo pipefail

echo "▶ Generating dashboard unlock status…"
if command -v python3 >/dev/null 2>&1; then
  if python3 -m pip install --quiet --disable-pip-version-check pytest \
    && python3 scripts/generate_test_status.py; then
    echo "✓ lib/test-status.json regenerated from test results."
  else
    echo "⚠ Could not run the test suite; using committed lib/test-status.json."
  fi
else
  echo "⚠ python3 not found; using committed lib/test-status.json."
fi

echo "▶ Building Next.js app…"
next build
