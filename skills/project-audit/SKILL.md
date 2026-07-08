---
name: project-audit
description: Review project pages, task linkage, and schema drift in an Obsidian vault without making automatic changes.
---

# Project Audit

Use this skill when a user wants to check whether their project pages still match their task system, repo state, and vault schema.

## Steps

1. Read the vault's `AGENTS.md`.
2. Audit project pages with the configured schema root.
3. Compare each active project with its task-manager link, if one exists.
4. Separate findings into:
   - deterministic repairs, such as missing required fields,
   - judgment calls, such as changing project status.
5. Show findings before writing anything.

## Rules

- Never infer project completion from an empty task list.
- Never archive, delete, promote, or create tasks without explicit approval.
- Treat missing task-manager integration as informational unless the schema requires it.
- Prefer a short review table over a long narrative.

