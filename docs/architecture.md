# Architecture

`obsidian-agent` demonstrates a layered pattern:

```text
agent skill decides intent
        |
        v
human review when judgment is needed
        |
        v
pre-write gate validates final Markdown
        |
        v
Obsidian vault stores durable truth
```

## Layers

| Layer | Job | In this starter |
| --- | --- | --- |
| Vault | Markdown notes and YAML frontmatter | `sample-vault/` |
| Model | Page kinds, required fields, allowed values | `schemas/` |
| Engine | Audit and authorize pages | external `vault-management` package |
| Gate | Harness-specific pre-write wrapper | `gates/` |
| Skills | Assistant workflows that decide what to do | `skills/` |

## Safety Model

The gate and human review answer different questions.

- The gate asks: "Is this resulting file structurally valid?"
- Human review asks: "Is this change semantically right?"

Use both. Schema validation is a guardrail, not judgment.

## Starter Taxonomy

This repo starts with five page kinds:

- `idea` — uncommitted possibility.
- `project` — committed outcome.
- `source` — captured external material.
- `concept` — synthesized knowledge.
- `system` — current-state description of a setup.

That is enough to show the workflow without turning the starter into someone else's whole operating system.

## Designing Your Own Model

Do not start by copying every sample kind. Start by asking:

- What pages do agents need to read or update repeatedly?
- Which pages have lifecycle state?
- Which fields will be queried or displayed across pages?
- Which writes should require human review?

See [Designing page kinds](designing-page-kinds.md) for the worksheet.
