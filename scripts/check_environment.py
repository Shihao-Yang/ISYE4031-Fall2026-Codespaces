"""Verify that the standard ISYE 4031 Python environment is usable."""

from __future__ import annotations

import importlib
import shutil
import sys


PACKAGES = (
    "numpy",
    "pandas",
    "scipy",
    "statsmodels",
    "sklearn",
    "matplotlib",
    "seaborn",
    "jupyterlab",
    "openpyxl",
)


def main() -> int:
    failures: list[str] = []

    print(f"Python: {sys.version.split()[0]}")
    for package in PACKAGES:
        try:
            module = importlib.import_module(package)
        except Exception as exc:  # pragma: no cover - diagnostic path
            failures.append(f"{package}: {exc}")
            continue
        version = getattr(module, "__version__", "installed")
        print(f"{package}: {version}")

    for command in ("codex", "agy"):
        executable = shutil.which(command)
        if executable:
            print(f"{command}: {executable}")
        else:
            failures.append(f"{command}: command not found on PATH")

    if failures:
        print("\nEnvironment check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("\nEnvironment check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
