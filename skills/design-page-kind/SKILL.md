---
name: design-page-kind
description: Interview a user to decide whether an Obsidian page kind is warranted and define its lifecycle, frontmatter, body template, queries, and write authority. Use when creating or revising a page kind, schema, or per-kind template. Do not use for formatting one existing note.
---

# Design a Page Kind

Read `../../docs/designing-page-kinds.md` for the design tests. Work conversationally and ask one decision at a time.

## Interview

Start from the workflow, not a schema:

1. What job will this page perform?
2. Which neighboring kind is closest, and why is a separate lifecycle or validation contract needed?
3. What states or transitions change over time?
4. Which real queries, dashboards, or automations will consume structured fields?
5. What belongs in narrative body content instead?
6. Who may create or change the page, and what requires human review?

Challenge unnecessary structure. Prefer an existing kind, body content, links, or a folder distinction when the proposed kind or field does not earn a distinct workflow role.

For each proposed field, establish:

- name and plain-language purpose;
- group: identity, classification, lifecycle, relationships, or metadata;
- required or optional;
- type, allowed values, and default when justified;
- the query, automation, transition, or validation rule that earns its place;
- write authority and review boundary.

Do not import a private taxonomy as a universal default. Use examples as prompts, not requirements.

## Output

Return a reviewable design brief containing:

- proposed page-kind name and folder;
- job and boundary from neighboring kinds;
- lifecycle states and transitions;
- field table with rationale, group, required status, type, default, and allowed values;
- body-template outline;
- intended queries or automations;
- write authority and trust tier;
- rejected fields or alternative designs;
- unresolved decisions;
- next artifacts to create or update.

Default to no writes. Create draft schema or template files only when the user explicitly asks, and keep them provisional until reviewed and validated.
