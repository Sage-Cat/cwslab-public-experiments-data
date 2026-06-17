#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/run_session.sh" "d09_c4_t2_l2_budget_aware_controller_high_load" "${1:-}"
