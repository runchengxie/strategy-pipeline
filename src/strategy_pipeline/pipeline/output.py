"""Generic run-output persistence orchestration.

The public layer owns ordering and lifecycle. Research-specific summary,
evidence, and metadata writers are injected by the application owner.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any

from .output_artifacts import write_run_artifacts

OutputCallback = Callable[..., Any]


def persist_run_outputs(
    *,
    context: Mapping[str, Any],
    summary_builder: OutputCallback,
    metadata_writer: OutputCallback,
    evidence_builder: OutputCallback | None = None,
) -> dict[str, Any]:
    """Write artifacts and invoke owner-provided output callbacks in order."""
    if not context.get("SAVE_ARTIFACTS", False):
        return {}

    artifacts = write_run_artifacts(context=context)
    if evidence_builder is not None:
        evidence_builder(context=context, artifacts=artifacts)
    summary = summary_builder(context=context, artifacts=artifacts)
    metadata_writer(context=context, summary=summary)
    return artifacts
