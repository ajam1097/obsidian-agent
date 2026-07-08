---
name: session-close
description: Close a work session by preserving durable project state without creating routine activity logs.
---

# Session Close

Use this skill at the end of a substantive work session.

## Steps

1. Identify what changed.
2. Update the project plan or status document if durable state changed.
3. Note unresolved blockers and the next concrete action.
4. Skip routine logs that do not help a future session resume.

## Output

Return:

- what changed,
- what was verified,
- what remains,
- where durable state was updated.

## Rules

- Do not duplicate git history in prose.
- Do not write to personal task systems without approval.
- Keep the handoff concise enough that the next session can act.

