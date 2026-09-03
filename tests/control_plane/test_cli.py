from strategy_pipeline.cli import build_parser


def test_public_cli_exposes_only_generic_commands():
    parser = build_parser()

    inspect_args = parser.parse_args(["inspect", "--run-id", "run-1"])
    publish_args = parser.parse_args(["publish", "--run-id", "run-1"])

    assert inspect_args.command == "inspect"
    assert inspect_args.run_id == "run-1"
    assert publish_args.command == "publish"
    assert publish_args.run_id == "run-1"
