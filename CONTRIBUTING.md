# Contributing

Changes to the public package must preserve its dependency-free, domain-neutral
boundary. Pull requests should use synthetic fixtures and must not add owner
repository imports, provider SDKs, credentials, private paths, or strategy
selection rules.

Run the public clean-room workflow locally by exporting the reviewed surface
with `scripts/dev/public_surface_export.py`, installing the generated package
without dependencies, and running the synthetic tests under `tests/public_core`.
