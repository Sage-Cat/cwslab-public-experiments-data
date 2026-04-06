#!/usr/bin/env bash
set -euo pipefail

render_with_plantuml() {
  if command -v plantuml >/dev/null 2>&1; then
    plantuml "$@"
    return
  fi

  if [[ -n "${PLANTUML_JAR:-}" && -f "${PLANTUML_JAR}" ]]; then
    java -Djava.awt.headless=true -jar "${PLANTUML_JAR}" "$@"
    return
  fi

  echo "TODO(verify): install plantuml locally or set PLANTUML_JAR to a local PlantUML jar." >&2
  exit 1
}

render_pattern() {
  local pattern="$1"
  if compgen -G "${pattern}" >/dev/null; then
    local files=(${pattern})
    render_with_plantuml "${files[@]}"
  fi
}

if command -v plantuml >/dev/null 2>&1 || [[ -n "${PLANTUML_JAR:-}" && -f "${PLANTUML_JAR}" ]]; then
  if [[ "$#" -gt 0 ]]; then
    for pattern in "$@"; do
      render_pattern "${pattern}"
    done
  else
    render_pattern "docs/architecture/diagrams/*.puml"
    render_pattern "docs/structure/diagrams/*.puml"
  fi
else
  echo "TODO(verify): install plantuml locally or set PLANTUML_JAR to a local PlantUML jar."
fi
