from __future__ import annotations

import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).parents[1] / "scripts/dev/history_publication_audit.py"
_SPEC = importlib.util.spec_from_file_location("history_publication_audit", _MODULE_PATH)
assert _SPEC is not None and _SPEC.loader is not None
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)
scan_text = _MODULE.scan_text


def test_public_owner_git_sources_are_allowed() -> None:
    text = (
        "alpha-research @ git+https://github.com/runchengxie/alpha-research.git@abc123\n"
        "portfolio-backtester @ git+https://github.com/runchengxie/portfolio-backtester.git@def456"
    )

    assert scan_text(text, path="pyproject.toml") == []


def test_unreviewed_git_sources_remain_findings() -> None:
    findings = scan_text(
        "dependency @ " + "git+" + "https://github.com/example/" + "private-research.git@abc123",
        path="pyproject.toml",
    )

    assert findings == [{"category": "git-source-reference", "path": "pyproject.toml"}]
