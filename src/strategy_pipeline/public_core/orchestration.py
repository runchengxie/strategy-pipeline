"""Domain-neutral orchestration for owner-produced artifacts."""

from collections.abc import Callable

from .models import ArtifactRef, RunReceipt, RunRequest


def run_pipeline(
    request: RunRequest,
    *,
    run_owner: Callable[[RunRequest], ArtifactRef],
    publish: Callable[[ArtifactRef], ArtifactRef],
) -> RunReceipt:
    """Run one owner operation and publish its result.

    Owner exceptions are intentionally reduced to an operational category so
    domain-specific or private exception details cannot leak into receipts.
    """

    try:
        produced = run_owner(request)
    except Exception:
        return RunReceipt(
            run_id=request.run_id,
            status="failed",
            failure_category="owner_failure",
            failure_message="owner execution failed",
        )

    try:
        published = publish(produced)
    except Exception:
        return RunReceipt(
            run_id=request.run_id,
            status="failed",
            failure_category="publication_failure",
            failure_message="artifact publication failed",
        )

    return RunReceipt(run_id=request.run_id, status="published", artifacts=(published,))
