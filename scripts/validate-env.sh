#!/usr/bin/env bash
# validate-env.sh - Checks that required environment variables are set before deployment.
# Usage: ./scripts/validate-env.sh

set -euo pipefail

REQUIRED_VARS=(
  "DATABASE_URL"
  "API_KEY"
  "SECRET_TOKEN"
)

missing=()

for var in "${REQUIRED_VARS[@]}"; do
  if [[ -z "${!var:-}" ]]; then
    missing+=("$var")
  fi
done

if [[ ${#missing[@]} -gt 0 ]]; then
  echo "ERROR: The following required environment variables are not set:" >&2
  for var in "${missing[@]}"; do
    echo "  - $var" >&2
  done
  echo "Please set these variables before deploying. See .env.example for reference." >&2
  exit 1
fi

echo "All required environment variables are set."
