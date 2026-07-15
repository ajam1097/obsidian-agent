---
name: delegated-task-routing
description: Classify a delegated task queue and route each task to an appropriate agent role, model class, and completion check without executing tasks automatically.
---

# Delegated Task Routing

Use this skill when a user keeps a task-manager list for assistant-owned work and wants an agent to pick up the queue safely.

## Workflow

1. Read the delegated task list from the user's task manager or from pasted tasks.
2. Load `task-routes.json` and classify each task using the first matching route.
3. Produce a short review table with: task, work type, recommended agent role, model route, and completion check.
4. Before dispatching, decide what the main agent must handle locally first; delegate only bounded sidecar work.
5. For each delegated task, pass only the task title, notes, relevant paths, success criteria, and write boundaries.
6. Review returned work before applying changes or closing the source task.

## Routing Rules

Routes are data, not prompt prose. Update `task-routes.json` when task types or model recommendations change.

- Put specific routes before broad routes.
- Keep model routes generic: `strongest_available_planning_model`, `default_or_strong_coding_model`, `default`.
- Do not hardcode private model names, task-manager IDs, vault paths, or user-specific project names in the public route file.

## Completion Rule

Never close a delegated task because it was classified or dispatched. Close it only after the requested artifact, change, answer, or accepted plan exists.
