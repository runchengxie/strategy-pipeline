"""Stable, domain-neutral objects exchanged by the public control plane."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ArtifactRef:
    kind: str
    uri: str
    digest: str
    producer: str


@dataclass(frozen=True, slots=True)
class RunRequest:
    run_id: str
    inputs: tuple[ArtifactRef, ...]


@dataclass(frozen=True, slots=True)
class RunReceipt:
    run_id: str
    status: str
    artifacts: tuple[ArtifactRef, ...] = ()
    failure_category: str | None = None
    failure_message: str | None = None
