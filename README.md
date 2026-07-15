# Trellis

Where knowledge grows into action. Trellis is a starter kit for running an Obsidian vault with agent-friendly structure, schema validation, and reviewable assistant workflows.

This repo is a public, sanitized reference pattern. It is not a mirror of any private vault. It shows how to combine:

- a small Obsidian sample vault,
- JSON Schemas for page kinds,
- `vault-management` audits and write validation,
- a sample pre-write gate,
- starter agent skills in one `skills/` folder,
- a promotion flow for turning private workflow improvements into public examples.

This public repository is a generated distribution. Its canonical source is the intentionally public `public/trellis/` tree in private My Trellis. Generated does not mean copied from private schemas: these examples are curated specifically for public use.

## Docs

- [Architecture](docs/architecture.md) — how the vault, schemas, gate, and skills fit together.
- [Designing page kinds](docs/designing-page-kinds.md) — probing questions for deciding page kinds, field groups, and frontmatter.
- [Source capture options](docs/source-capture-options.md) — ways to get web/highlight/source material into the vault.
- [Safety model](docs/safety-model.md) — what schema gates do and do not protect.
- [Promotion flow](docs/promotion-flow.md) — maintainer guide for curating private improvements into this public starter.

## Quickstart

Install the validator from the separate engine repo:

```bash
pipx install git+https://github.com/ajam1097/vault-management.git
```

Then audit the sample vault:

```bash
vault-management page audit --kind idea --vault-root sample-vault --schema-root schemas
vault-management page audit --kind project --vault-root sample-vault --schema-root schemas
vault-management page audit --kind source --vault-root sample-vault --schema-root schemas
vault-management page audit --kind concept --vault-root sample-vault --schema-root schemas
vault-management page audit --kind system --vault-root sample-vault --schema-root schemas
```

You can also validate a proposed write:

```bash
vault-management authorize sample-vault/efforts/ideas/Inbox Rules.md --vault-root sample-vault --schema-root schemas < sample-vault/efforts/ideas/Inbox Rules.md
```

## Layout

```text
sample-vault/      Example Obsidian vault content using fake notes
schemas/           Page-kind schemas consumed by vault-management
gates/             Reference hook/wrapper patterns
skills/            Starter assistant skills in one flat folder
agents/            Optional starter agent briefs
docs/              Public docs plus maintainer guidance
```

## What To Copy

Copy the pattern, not the exact taxonomy. Start with one or two page kinds that matter in your own vault, audit them until clean, then add a write gate only after the audit surface is boring.

## What Not To Copy Blindly

- Do not point a write gate at your real vault until audits pass.
- Do not publish your live vault without an allowlist export and privacy scan.
- Do not auto-sync private skills into a public repo. Promote generalized, tested snapshots.

## Related Project

[Forge](https://github.com/ajam1097/forge) is the federated public library for domain-general agent skills. Trellis remains the public home for Obsidian-specific starter workflows.

## Contributing

Do not treat this generated repository as the canonical editing surface. Open an issue or pull request for review; maintainers back-port accepted changes into My Trellis and publish a new approval-gated snapshot. See [CONTRIBUTING.md](CONTRIBUTING.md).
