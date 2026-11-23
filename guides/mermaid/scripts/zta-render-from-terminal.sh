#!/usr/bin/env bash
set -euo pipefail
cd "$HOME/projects/zta-decomposition"
if ! command -v node >/dev/null 2>&1; then
  source "$HOME/.nvm/nvm.sh"
fi
render_dir=$(mktemp -d /tmp/zta-render.XXXXXX)
printf '%s\n' '{"executablePath":"/usr/bin/chromium"}' > "$render_dir/puppeteer-config.json"
for source_file in 020_architecture/physical-topology.md 020_architecture/logical-topology.md zta-project-guide.md; do
  output_name=$(basename "$source_file" .md)
  for format in svg png; do
    ./node_modules/.bin/mmdc -i "$source_file" -o "$render_dir/$output_name.$format" -p "$render_dir/puppeteer-config.json" -b white -s 2
  done
done
printf 'Render output: %s\n' "$render_dir"
