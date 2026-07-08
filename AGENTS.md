# obsidian-agent Agent Notes

Read this file before making changes in this project. Then read `docs/PLAN.md` for current status and next work.

## Project Shape

- Lane: `vault-work`
- Stack: Markdown, JSON Schema, Python-compatible CLI examples
- Canonical plan: `docs/PLAN.md`
- Design docs: `docs/architecture.md`, `docs/promotion-flow.md`

## Commands

```bash
vault-management page audit --kind idea --vault-root sample-vault --schema-root schemas
vault-management page audit --kind project --vault-root sample-vault --schema-root schemas
vault-management page audit --kind source --vault-root sample-vault --schema-root schemas
vault-management page audit --kind concept --vault-root sample-vault --schema-root schemas
vault-management page audit --kind system --vault-root sample-vault --schema-root schemas
```

## Conventions

- Keep this repo public-safe: no private vault content, personal context, task IDs, local absolute paths, API keys, or machine-specific settings.
- Keep skills in a single `skills/` folder. This starter favors easy cloning over tool-specific packaging lanes.
- Treat `vault-management` as an external engine. Do not vendor its source here.
- Use fake sample notes that demonstrate behavior without mirroring a real vault.
- Update `docs/PLAN.md` when status or roadmap changes.

## Working Notes

- This repo is a starter/reference kit, not the source of truth for a private system.
- Public changes should arrive through the promotion flow in `docs/promotion-flow.md`.
- Keep examples small enough that a new reader can understand them in one sitting.
