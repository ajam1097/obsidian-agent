#!/usr/bin/env python3
"""Tiny pre-write validation example.

This script is intentionally harness-neutral. Real tools have different hook
payloads; adapt the payload parsing, then keep the validator call boring.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_path", help="Path the agent wants to write")
    parser.add_argument("--vault-root", required=True)
    parser.add_argument("--schema-root", required=True)
    parser.add_argument("--content-file", required=True)
    parser.add_argument("--vault-management", default="vault-management")
    args = parser.parse_args()

    content = Path(args.content_file).read_text()
    result = subprocess.run(
        [
            args.vault_management,
            "authorize",
            args.target_path,
            "--vault-root",
            args.vault_root,
            "--schema-root",
            args.schema_root,
        ],
        input=content,
        text=True,
        capture_output=True,
        check=False,
    )

    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

