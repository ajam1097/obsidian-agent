# Contributing to Trellis

Trellis is published as a generated snapshot from its canonical source in My Trellis. The public repository is useful for discussion and review, but maintainers do not merge or author changes there as the source of truth.

## Propose a change

1. Open an issue or pull request that explains the reusable problem and proposed public-safe change.
2. Do not include real vault content, personal paths, credentials, task IDs, or machine-specific configuration.
3. A maintainer reviews and back-ports accepted changes into My Trellis under `public/trellis/`.
4. The next publication runs the exhaustive allowlist check, personal-content scan, secret scan, full diff review, and approval digest before updating this repository.

This direction keeps one canonical editing surface while preserving normal public feedback and attribution.
