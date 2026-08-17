#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install --requirement requirements.txt

mkdir -p "$HOME/.local"
npm install --global --prefix "$HOME/.local" @openai/codex@0.147.0
sudo ln -sf "$HOME/.local/bin/codex" /usr/local/bin/codex

.venv/bin/python -m ipykernel install \
  --user \
  --name isye4031 \
  --display-name "Python (ISYE 4031)"

.venv/bin/python scripts/check_environment.py

echo
echo "ISYE 4031 setup is complete."
echo "Run 'codex login --device-auth' to authenticate, then 'codex login status'."
