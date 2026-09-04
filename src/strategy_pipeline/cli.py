"""Generic public control-plane command line interface."""

from __future__ import annotations

import argparse
import json

from .cli_evidence import register_afml_evidence_commands
from .cli_protocol import register_protocol_commands


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="strategy-pipeline")
    commands = parser.add_subparsers(dest="command", required=True)
    register_afml_evidence_commands(commands)
    register_protocol_commands(commands)
    for name in ("inspect", "publish", "handoff"):
        command = commands.add_parser(name)
        command.add_argument("--run-id", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if hasattr(args, "func"):
        return args.func(args)
    print(json.dumps({"command": args.command, "run_id": args.run_id}))
    return 0
