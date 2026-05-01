#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/run_session.sh" "d07_c3_t2_l1_heterogeneity_subset_value" "${1:-}"
