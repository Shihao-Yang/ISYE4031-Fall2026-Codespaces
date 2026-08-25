# ISYE 4031: Regression and Forecasting

This is the standard browser-based computing environment for ISYE 4031 in Fall 2026. It includes Python, Jupyter, the course analysis packages, GitHub CLI, Codex CLI, and Google Antigravity CLI. You do not need to install the course software on your own computer.

## First launch

1. Open your individual course repository on GitHub.
2. Select **Code**, select **Codespaces**, and choose **Create codespace on main**. Keep the default 2-core machine.
3. Wait until the terminal reports `ISYE 4031 setup is complete.`
4. Choose and authenticate at least one agent:

   - **Google Antigravity:** Run `agy`, select **Google OAuth**, open the displayed browser link, and complete the login. Google's current Antigravity CLI instructions specify a personal Gmail account. If your Georgia Tech account is rejected, use a personal Gmail account or use Codex instead.
   - **Codex:** Run `codex login --device-auth`, open the displayed link, enter the one-time code, and sign in with the account authorized for the course.

5. Back in the terminal, verify the environment:

   ```bash
   python scripts/check_environment.py
   pytest -q
   ```

6. Start either agent from the repository root:

   ```bash
   agy
   # or
   codex
   ```

Authentication belongs to you. Never commit or share API keys, login tokens, `.env` files, or files under `~/.codex`. You may need to authenticate again after deleting or rebuilding a codespace.

## First lab

Begin with [`labs/00_getting_started`](labs/00_getting_started/README.md). Every agent-assisted analysis follows the same pattern:

1. **Baseline:** produce a simple result you understand.
2. **Agent:** ask Codex to improve, extend, or explain the analysis.
3. **Audit:** test the code, check assumptions and leakage, and explain which output you accepted or rejected.

The statistical ideas remain central. AI-generated output is a proposal to verify, not evidence that the analysis is correct.

## Saving work and controlling usage

- Commit and push your work before deleting a codespace.
- Stop the codespace when you finish. GitHub also stops it after the configured idle period.
- Use one 2-core codespace unless the instructor says otherwise.
- Do not put restricted course material, student records, or private data in prompts or repositories.

## Troubleshooting

- If `codex` or `agy` is not found, run `bash .devcontainer/post-create.sh` once.
- If Python imports fail, select the `Python (ISYE 4031)` notebook kernel or run `source .venv/bin/activate`.
- Check login state with `codex login status`; clear it with `codex logout`.
- Antigravity prompts for Google OAuth the first time you run `agy`.
- If setup still fails, copy the complete terminal error into the course help channel. Do not include credentials.

## Local installation

Codespaces is the supported classroom environment. Students who independently install the tools locally may do so, but should notify the instructor and remain able to reproduce submitted work in the course Codespace.
