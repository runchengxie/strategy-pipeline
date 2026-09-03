# Integrating an owner implementation

An owner repository supplies the domain behavior and implements the public
protocols. The adapter should remain thin: translate the public request,
invoke the owner, and return a validated `ArtifactRef`.

```python
from strategy_pipeline import ArtifactRef, PublicationRequest, RunRequest, run


class Owner:
    def run(self, request: RunRequest) -> ArtifactRef:
        # Domain-specific computation stays in the owner repository.
        return ArtifactRef(
            kind="owner.result",
            uri=f"memory://runs/{request.run_id}/result.json",
            digest="sha256:replace-with-real-digest",
            producer="owner-repository",
        )


class Publisher:
    def publish(self, request: PublicationRequest) -> ArtifactRef:
        # Storage and publication policy stay in the consuming repository.
        return request.artifact


receipt = run(RunRequest("example", ()), owner=Owner(), publisher=Publisher())
```

Keep strategy ideas, feature construction, model selection, portfolio rules,
provider clients, credentials, and private data out of this package. The
public control plane should be usable with a synthetic owner and publisher in
a clean environment.

For a workspace integration, pin a reviewed public commit or release in the
consumer's dependency lock file and add an integration test that exercises the
full request-to-receipt path without importing private modules.
