#!/usr/bin/env sh
set -eu

PROFILE="${1:-all}"
if [ "$#" -gt 0 ]; then
  shift
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "Python 3.11+ is required." >&2
  exit 1
fi

exec "$PYTHON" "$SCRIPT_DIR/scripts/install.py" --profile "$PROFILE" "$@"
