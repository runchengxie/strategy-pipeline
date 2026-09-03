import subprocess
import sys
from pathlib import Path


def test_public_core_imports_without_owner_packages():
    root = Path(__file__).resolve().parents[2]
    script = """
import builtins

owner_names = (
    "alpha_research",
    "market_data_platform",
    "portfolio_backtester",
    "strategy_app",
    "research_contracts",
)
real_import = builtins.__import__

def guarded_import(name, *args, **kwargs):
    if name.startswith(owner_names):
        raise ModuleNotFoundError(name)
    return real_import(name, *args, **kwargs)

builtins.__import__ = guarded_import
from strategy_pipeline.public_core import ArtifactRef, run_pipeline
assert ArtifactRef and run_pipeline
"""
    result = subprocess.run(
        [sys.executable, "-c", script],
        cwd=root,
        env={"PYTHONPATH": str(root / "src")},
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
