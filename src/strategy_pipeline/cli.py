"""Generic public control-plane command line interface."""

from __future__ import annotations

import argparse
import json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="strategy-pipeline")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "publish", "handoff"):
        command = commands.add_parser(name)
        command.add_argument("--run-id", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(json.dumps({"command": args.command, "run_id": args.run_id}))
    return 0
