# Designing Page Kinds

Start with workflows, not schemas. A page kind is useful when a group of notes needs the same lifecycle, routing, or validation.

## Probing Questions

Ask these before adding a page kind:

1. **What job does this page do?**
   Is it a captured source, a synthesized idea, an active project, a current-state system description, or something else?

2. **What makes it different from neighboring kinds?**
   If two kinds have the same lifecycle and fields, they may be one kind with a field or folder distinction.

3. **What state changes over time?**
   If the answer is "nothing," the kind may need only identity and metadata. If the answer is "reviewed, promoted, archived," that state belongs in frontmatter.

4. **What will you query across many pages?**
   Frontmatter earns its place when it supports queries, automation, lifecycle transitions, or overview displays.

5. **What should stay in the body?**
   One-off relationships, narrative context, quotes, reasoning, and nuance usually belong in Markdown prose.

6. **Who is allowed to change it?**
   Low-risk inventory fields might be gate-only. Project status or personal reflection probably needs human review.

## Frontmatter Test

Use this test for every field:

| Question | If yes | If no |
| --- | --- | --- |
| Is it required to identify the kind? | Keep it, often as `type` | Move on |
| Is it queried across many pages? | Keep it | Prefer body text |
| Does it drive automation or lifecycle? | Keep it | Prefer body text |
| Does it appear in a dashboard/table? | Keep it if the dashboard is real | Avoid speculative fields |
| Is it just "related to X"? | Usually use a body backlink | Keep only if the relation has workflow meaning |

## Field Groups

Field groups are a design aid. They make schemas easier to read and help people understand why a field exists.

| Group | Use For | Example fields |
| --- | --- | --- |
| `identity` | Page kind and naming | `type`, `aliases` |
| `classification` | Stable grouping and filtering | `domains`, `source_type` |
| `lifecycle` | State that changes by rule | `status`, `stage`, `processing_status` |
| `relationships` | Integration or lifecycle-bearing links | `promoted_to`, `repo`, `source_url` |
| `metadata` | Maintenance facts | `created`, `updated` |

If a field does not fit a group, pause before adding it. It may be body content.

## Common Starter Kinds

- `idea`: a possibility; useful fields include `stage`, `status`, and `research_status`.
- `project`: a committed outcome; useful fields include `status`, `outcome`, and optional external links.
- `source`: captured material; useful fields include `source_type`, `source_url`, and `processing_status`.
- `concept`: synthesized knowledge; often needs fewer fields than expected.
- `system`: current-state operational documentation; usually deserves stricter review.

## Anti-Patterns

- Adding frontmatter because a fact exists once.
- Creating separate kinds for every folder before the lifecycle is clear.
- Letting agent convenience fields become stale mirrors of another system.
- Treating schema validation as content quality.

