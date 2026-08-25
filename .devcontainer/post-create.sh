#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install --requirement requirements.txt

mkdir -p "$HOME/.local/bin"
npm install --global --prefix "$HOME/.local" @openai/codex@0.147.0
sudo ln -sf "$HOME/.local/bin/codex" /usr/local/bin/codex

antigravity_installer="$(mktemp)"
cleanup_antigravity_installer() {
  rm -f "$antigravity_installer"
}
trap cleanup_antigravity_installer EXIT

curl -fsSL https://antigravity.google/cli/install.sh \
  -o "$antigravity_installer"
bash "$antigravity_installer" --dir "$HOME/.local/bin"

.venv/bin/python -m ipykernel install \
  --user \
  --name isye4031 \
  --display-name "Python (ISYE 4031)"

.venv/bin/python scripts/check_environment.py

echo
echo "ISYE 4031 setup is complete."
echo "Run 'agy' to authenticate Antigravity with Google OAuth."
echo "Codex is also available: run 'codex login --device-auth'."
