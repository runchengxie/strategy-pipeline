# Control-plane API

`strategy-pipeline` coordinates an owner implementation with artifact
publication. It carries references and receipts; it does not calculate the
artifact contents.

## Contracts

`ArtifactRef` identifies an immutable output with a kind, URI, digest, and
producer. `RunRequest` carries a run ID and input artifact references.
`PublicationRequest` and `HandoffRequest` describe downstream delivery.
`RunReceipt` records the public result without exposing owner exception text.

```python
from strategy_pipeline import ArtifactRef, RunRequest, run

request = RunRequest(run_id="run-2026-01-01", inputs=())
```

All contracts are immutable, validated dataclasses. Artifact-producing code
should return an `ArtifactRef`, not an in-memory domain object or provider
client.

## Orchestration

The public runner calls a `RunOwner`, then an `ArtifactPublisher`:

```python
receipt = run(request, owner=owner, publisher=publisher)
if receipt.status == "published":
    print(receipt.artifacts)
```

The runner returns a redacted `owner_failure` or `publication_failure`
category when an injected implementation raises. It never serializes private
exception details into the receipt.

## Other boundaries

Use `publish_artifact` for a callable writer and `publish_handoff` for a
destination publisher. Both validate that the injected implementation returns
an `ArtifactRef`.

The public package has no provider SDK, credentials, network client, storage
backend, model implementation, or strategy registry. Those belong behind an
adapter in the consuming repository.
