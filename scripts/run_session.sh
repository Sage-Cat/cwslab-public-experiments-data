#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

usage() {
  echo "usage: $0 <session-id> [session-env-path]" >&2
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "missing command: $1" >&2
    exit 1
  fi
}

require_env() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    echo "missing environment variable: $name" >&2
    exit 1
  fi
}

log_line() {
  local message="$1"
  printf "%s\n" "$message" | tee -a "$RUN_LOG"
}

run_remote_logged() {
  local log_file="$1"
  local label="$2"
  local command="$3"
  {
    printf "### %s\n" "$label"
    printf "$ %s\n" "$command"
    ssh -p "$CWSLAB_PUBLIC_AP_PORT" -o StrictHostKeyChecking=accept-new \
      "$CWSLAB_PUBLIC_AP_USER@$CWSLAB_PUBLIC_AP_HOST" "$command" < /dev/null
    printf "\n"
  } | tee -a "$log_file"
}

epoch_ms_now() {
  python3 - <<'PY'
import time
print(int(time.time() * 1000))
PY
}

play_notification_sound() {
  if [[ "${CWSLAB_PUBLIC_NOTIFY_SOUND_ENABLE:-0}" != "1" ]]; then
    return
  fi
  if [[ -n "${CWSLAB_PUBLIC_NOTIFY_SOUND_FILE:-}" ]] && [[ -r "${CWSLAB_PUBLIC_NOTIFY_SOUND_FILE}" ]] && command -v paplay >/dev/null 2>&1; then
    (paplay "$CWSLAB_PUBLIC_NOTIFY_SOUND_FILE" >/dev/null 2>&1 || true) &
    return
  fi
  if command -v canberra-gtk-play >/dev/null 2>&1; then
    (canberra-gtk-play -i dialog-information >/dev/null 2>&1 || true) &
  fi
}

countdown() {
  local remaining="$1"
  while (( remaining > 0 )); do
    printf "\rremaining=%ss " "$remaining"
    sleep 1
    ((remaining--))
  done
  printf "\rremaining=0s \n"
}

prompt_enter() {
  local prompt="$1"
  printf "%s" "$prompt" > /dev/tty
  IFS= read -r _
}

prompt_optional_note() {
  local prompt="$1"
  printf "%s" "$prompt" > /dev/tty
  IFS= read -r BLOCK_NOTE
}

append_event() {
  local event="$1"
  local block_id="$2"
  local duration_s="$3"
  local epoch_ms="$4"
  local wall_time="$5"
  local payload="$6"
  payload="${payload//$'\t'/ }"
  payload="${payload//$'\n'/ }"
  printf "%s\t%s\t%s\t%s\t%s\t%s\n" "$event" "$block_id" "$duration_s" "$epoch_ms" "$wall_time" "$payload" >> "$EVENT_LOG"
}

append_block_log() {
  local block_id="$1"
  local duration_s="$2"
  local start_wall="$3"
  local end_wall="$4"
  local note="$5"
  note="${note//|//}"
  printf "| `%s` | %s | %s | %s | %s |\n" "$block_id" "$duration_s" "$start_wall" "$end_wall" "$note" >> "$BLOCK_LOG"
}

run_preflight() {
  require_cmd bash
  require_cmd python3
  require_cmd timeout
  require_cmd stty
  require_cmd ssh
  require_cmd ping
  require_cmd stdbuf

  log_line "=== preflight_local ==="
  log_line "reference implementation preflight for the primary prplOS-compatible dual-band AP node"
  log_line "bundle_dir=$BUNDLE_DIR"
  log_line "sensor_device=$CWSLAB_PUBLIC_SENSOR_DEVICE"
  if [[ ! -e "$CWSLAB_PUBLIC_SENSOR_DEVICE" ]]; then
    echo "sensor device not found: $CWSLAB_PUBLIC_SENSOR_DEVICE" >&2
    exit 1
  fi
  bash -lc 'python3 --version' | tee -a "$RUN_LOG"
  bash -lc 'git rev-parse --show-toplevel' | tee -a "$RUN_LOG" || true
  ping -c 2 -W 1 "$CWSLAB_PUBLIC_AP_HOST" | tee -a "$RUN_LOG"
}

run_ap_configure() {
  local log_file="$BUNDLE_DIR/logs/ap_configure.log"
  log_line "=== ap_configure ==="
  run_remote_logged "$log_file" "bind-ssid-lower-layers" "ba-cli -a '${CWSLAB_PUBLIC_AP_SSID_REF}LowerLayers=\"${CWSLAB_PUBLIC_AP_RADIO_REF}\"'"
  run_remote_logged "$log_file" "bind-access-point-ssid-reference" "ba-cli -a '${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}SSIDReference=\"${CWSLAB_PUBLIC_AP_SSID_REF}\"'"
  run_remote_logged "$log_file" "set-radio-auto-channel" "ba-cli -a ${CWSLAB_PUBLIC_AP_RADIO_REF}AutoChannelEnable=0"
  run_remote_logged "$log_file" "set-radio-bandwidth" "ba-cli -a '${CWSLAB_PUBLIC_AP_RADIO_REF}OperatingChannelBandwidth=\"${CWSLAB_PUBLIC_AP_BANDWIDTH}\"'"
  run_remote_logged "$log_file" "set-radio-channel" "ba-cli -a ${CWSLAB_PUBLIC_AP_RADIO_REF}Channel=${CWSLAB_PUBLIC_AP_CHANNEL}"
  run_remote_logged "$log_file" "set-ssid-name" "ba-cli -a '${CWSLAB_PUBLIC_AP_SSID_REF}SSID=\"${CWSLAB_PUBLIC_AP_SSID}\"'"
  run_remote_logged "$log_file" "set-access-point-bridge-interface" "ba-cli -a '${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}BridgeInterface=\"${CWSLAB_PUBLIC_AP_BRIDGE_INTERFACE}\"'"
  run_remote_logged "$log_file" "set-access-point-security-mode" "ba-cli -a '${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}Security.ModeEnabled=\"${CWSLAB_PUBLIC_AP_SECURITY_MODE}\"'"
  run_remote_logged "$log_file" "set-access-point-passphrase" "ba-cli -a '${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}Security.KeyPassPhrase=\"${CWSLAB_PUBLIC_AP_KEY_PASSPHRASE}\"'"
  run_remote_logged "$log_file" "set-access-point-wps-enable" "ba-cli -a ${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}WPS.Enable=0"
  run_remote_logged "$log_file" "set-access-point-wds-enable" "ba-cli -a ${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}WDSEnable=0"
  run_remote_logged "$log_file" "set-access-point-ssid-advertisement" "ba-cli -a ${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}SSIDAdvertisementEnabled=1"
  run_remote_logged "$log_file" "set-radio-enable" "ba-cli -a ${CWSLAB_PUBLIC_AP_RADIO_REF}Enable=1"
  run_remote_logged "$log_file" "set-ssid-enable" "ba-cli -a ${CWSLAB_PUBLIC_AP_SSID_REF}Enable=1"
  run_remote_logged "$log_file" "set-access-point-enable" "ba-cli -a ${CWSLAB_PUBLIC_AP_ACCESS_POINT_REF}Enable=1"
}

run_ap_snapshot() {
  local log_file="$BUNDLE_DIR/logs/ap_snapshot.log"
  log_line "=== ap_snapshot ==="
  run_remote_logged "$log_file" "uname" "uname -a"
  run_remote_logged "$log_file" "ip-brief" "ip -br addr || true"
  run_remote_logged "$log_file" "iw-dev" "iw dev || true"
  run_remote_logged "$log_file" "iwinfo" "iwinfo || true"
  run_remote_logged "$log_file" "ping-sensor" "ping -c 2 -W 1 ${CWSLAB_PUBLIC_SENSOR_PING_HOST} || true"
}

run_firmware_build() {
  local log_file="$BUNDLE_DIR/logs/firmware_build.log"
  log_line "=== firmware_build ==="
  (
    cd "$CWSLAB_PUBLIC_FIRMWARE_ROOT"
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_TOOLS_PATH:-}" ]]; then
      export IDF_TOOLS_PATH="$CWSLAB_PUBLIC_FIRMWARE_TOOLS_PATH"
    fi
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_ENV_SCRIPT:-}" ]]; then
      # shellcheck disable=SC1090
      source "$CWSLAB_PUBLIC_FIRMWARE_ENV_SCRIPT"
    fi
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_TARGET:-}" ]]; then
      export IDF_TARGET="$CWSLAB_PUBLIC_FIRMWARE_TARGET"
    fi
    bash -lc 'idf.py build'
  ) | tee -a "$log_file"
}

run_firmware_flash() {
  local log_file="$BUNDLE_DIR/logs/firmware_flash.log"
  log_line "=== firmware_flash ==="
  (
    cd "$CWSLAB_PUBLIC_FIRMWARE_ROOT"
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_TOOLS_PATH:-}" ]]; then
      export IDF_TOOLS_PATH="$CWSLAB_PUBLIC_FIRMWARE_TOOLS_PATH"
    fi
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_ENV_SCRIPT:-}" ]]; then
      # shellcheck disable=SC1090
      source "$CWSLAB_PUBLIC_FIRMWARE_ENV_SCRIPT"
    fi
    if [[ -n "${CWSLAB_PUBLIC_FIRMWARE_TARGET:-}" ]]; then
      export IDF_TARGET="$CWSLAB_PUBLIC_FIRMWARE_TARGET"
    fi
    bash -lc "idf.py -p \"$CWSLAB_PUBLIC_SENSOR_DEVICE\" flash"
  ) | tee -a "$log_file"
}

run_operator_guided_capture() {
  local raw_file="$BUNDLE_DIR/serial/esp32_guided_session.log"
  local log_file="$BUNDLE_DIR/logs/operator_guided_capture.log"

  if [[ ! -t 0 ]]; then
    echo "operator-guided capture requires an interactive terminal" >&2
    exit 1
  fi

  cat > "$BLOCK_LOG" <<EOF
# Operator Block Log

- Session ID: \`$SESSION_ID\`
- Publication surface: public-safe reference implementation
- Controlled node: \`primary prplOS-compatible dual-band AP node\`

| Block | Planned Duration (s) | Start Wall Time | End Wall Time | Notes |
| --- | --- | --- | --- | --- |
EOF

  printf "event\tblock_id\tplanned_duration_s\tepoch_ms\twall_time\tpayload\n" > "$EVENT_LOG"
  stty -F "$CWSLAB_PUBLIC_SENSOR_DEVICE" "$CWSLAB_PUBLIC_SENSOR_BAUD" raw -echo || true
  stdbuf -oL cat "$CWSLAB_PUBLIC_SENSOR_DEVICE" | tee "$raw_file" &
  CAPTURE_PID=$!
  trap 'kill "$CAPTURE_PID" >/dev/null 2>&1 || true; wait "$CAPTURE_PID" >/dev/null 2>&1 || true' EXIT INT TERM

  local capture_start_wall capture_start_epoch_ms
  capture_start_wall="$(date "+%F %T %Z")"
  capture_start_epoch_ms="$(epoch_ms_now)"
  append_event "capture_started" "-" "0" "$capture_start_epoch_ms" "$capture_start_wall" "serial/esp32_guided_session.log"

  while IFS=$'\t' read -r block_id duration_s human_present scenario objective instructions; do
    [[ "$block_id" == "block_id" ]] && continue
    log_line ""
    log_line "=== block $block_id ==="
    log_line "scenario: $scenario"
    log_line "objective: $objective"
    log_line "human_present: $human_present"
    IFS=';;' read -r -a instruction_lines <<< "$instructions"
    for instruction in "${instruction_lines[@]}"; do
      log_line "$instruction"
    done
    prompt_enter "Press Enter to start block $block_id... "
    local start_wall start_epoch_ms end_wall end_epoch_ms
    start_wall="$(date "+%F %T %Z")"
    start_epoch_ms="$(epoch_ms_now)"
    append_event "block_started" "$block_id" "$duration_s" "$start_epoch_ms" "$start_wall" "$scenario"
    countdown "$duration_s"
    end_wall="$(date "+%F %T %Z")"
    end_epoch_ms="$(epoch_ms_now)"
    append_event "block_finished" "$block_id" "$duration_s" "$end_epoch_ms" "$end_wall" ""
    BLOCK_NOTE=""
    play_notification_sound
    prompt_optional_note "Optional note for $block_id (press Enter to leave blank): "
    append_block_log "$block_id" "$duration_s" "$start_wall" "$end_wall" "$BLOCK_NOTE"
    if [[ -n "$BLOCK_NOTE" ]]; then
      append_event "block_note" "$block_id" "$duration_s" "$end_epoch_ms" "$end_wall" "$BLOCK_NOTE"
    fi
  done < "$BLOCKS_FILE"

  local capture_end_wall capture_end_epoch_ms
  capture_end_wall="$(date "+%F %T %Z")"
  capture_end_epoch_ms="$(epoch_ms_now)"
  append_event "capture_finished" "-" "0" "$capture_end_epoch_ms" "$capture_end_wall" "serial/esp32_guided_session.log"
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

SESSION_ID="$1"
SESSION_DIR="$SCRIPT_DIR/sessions/$SESSION_ID"
BLOCKS_FILE="$SESSION_DIR/blocks.tsv"
SESSION_ENV_FILE="${2:-${CWSLAB_PUBLIC_SESSION_ENV:-$SESSION_DIR/session.env}}"
SESSION_ENV_EXAMPLE="$SESSION_DIR/session.env.example"

if [[ ! -d "$SESSION_DIR" ]]; then
  echo "unknown session profile: $SESSION_ID" >&2
  exit 1
fi
if [[ ! -f "$BLOCKS_FILE" ]]; then
  echo "missing blocks.tsv for session: $SESSION_ID" >&2
  exit 1
fi
if [[ ! -f "$SESSION_ENV_FILE" ]]; then
  echo "missing session env file: $SESSION_ENV_FILE" >&2
  echo "use the example as a starting point: $SESSION_ENV_EXAMPLE" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$SESSION_ENV_FILE"

require_env CWSLAB_PUBLIC_OUTPUT_ROOT
require_env CWSLAB_PUBLIC_AP_HOST
require_env CWSLAB_PUBLIC_AP_USER
require_env CWSLAB_PUBLIC_AP_PORT
require_env CWSLAB_PUBLIC_AP_RADIO_REF
require_env CWSLAB_PUBLIC_AP_SSID_REF
require_env CWSLAB_PUBLIC_AP_ACCESS_POINT_REF
require_env CWSLAB_PUBLIC_AP_BRIDGE_INTERFACE
require_env CWSLAB_PUBLIC_AP_CHANNEL
require_env CWSLAB_PUBLIC_AP_BANDWIDTH
require_env CWSLAB_PUBLIC_AP_SSID
require_env CWSLAB_PUBLIC_AP_SECURITY_MODE
require_env CWSLAB_PUBLIC_AP_KEY_PASSPHRASE
require_env CWSLAB_PUBLIC_SENSOR_DEVICE
require_env CWSLAB_PUBLIC_SENSOR_BAUD
require_env CWSLAB_PUBLIC_SENSOR_PING_HOST
require_env CWSLAB_PUBLIC_FIRMWARE_ROOT

BUNDLE_TIMESTAMP="$(date -u +%Y%m%dT%H%M%SZ)"
BUNDLE_DIR="$CWSLAB_PUBLIC_OUTPUT_ROOT/${SESSION_ID}_${BUNDLE_TIMESTAMP}"
RUN_LOG="$BUNDLE_DIR/logs/run_experiment.log"
BLOCK_LOG="$BUNDLE_DIR/logs/operator_block_log.md"
EVENT_LOG="$BUNDLE_DIR/logs/operator_block_events.tsv"
mkdir -p "$BUNDLE_DIR/logs" "$BUNDLE_DIR/serial"

log_line "Launcher: public reference hardware session"
log_line "session_id=$SESSION_ID"
log_line "bundle_dir=$BUNDLE_DIR"

run_preflight
run_ap_configure
run_ap_snapshot
run_firmware_build
run_firmware_flash
run_operator_guided_capture

log_line ""
log_line "Session finished. Review bundle artifacts under $BUNDLE_DIR."
