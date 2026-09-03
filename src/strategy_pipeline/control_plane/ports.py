"""Protocols implemented by private owners and storage adapters."""

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, runtime_checkable

from .contracts import ArtifactRef, HandoffRequest, PublicationRequest, RunRequest


@runtime_checkable
class RunOwner(Protocol):
    def run(self, request: RunRequest) -> ArtifactRef: ...


@runtime_checkable
class ArtifactPublisher(Protocol):
    def publish(self, request: PublicationRequest) -> ArtifactRef: ...


@runtime_checkable
class HandoffPublisher(Protocol):
    def publish(self, request: HandoffRequest) -> ArtifactRef: ...


ArtifactWriter = Callable[[PublicationRequest], ArtifactRef]
