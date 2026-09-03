from strategy_pipeline.public_core.models import ArtifactRef, RunRequest
from strategy_pipeline.public_core.orchestration import run_pipeline


def test_run_pipeline_records_published_artifact_without_owner_imports():
    request = RunRequest(run_id="synthetic-run", inputs=())
    produced = ArtifactRef(
        kind="example.output",
        uri="memory://synthetic-run/output.json",
        digest="sha256:synthetic",
        producer="synthetic-owner",
    )
    published = ArtifactRef(
        kind="example.output",
        uri="memory://published/output.json",
        digest="sha256:synthetic",
        producer="public-publisher",
    )

    receipt = run_pipeline(
        request,
        run_owner=lambda received: produced,
        publish=lambda artifact: published,
    )

    assert receipt.status == "published"
    assert receipt.run_id == "synthetic-run"
    assert receipt.artifacts == (published,)


def test_run_pipeline_returns_safe_operational_failure():
    request = RunRequest(run_id="failed-run", inputs=())

    receipt = run_pipeline(
        request,
        run_owner=lambda received: (_ for _ in ()).throw(RuntimeError("private detail")),
        publish=lambda artifact: artifact,
    )

    assert receipt.status == "failed"
    assert receipt.failure_category == "owner_failure"
    assert receipt.failure_message == "owner execution failed"
