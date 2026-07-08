# Schemas

This folder is a sample schema root for `vault-management`.

## Files

```text
schemas/
  field-groups.json
  vocabularies/domains.json
  page-kinds/
    idea.schema.json
    project.schema.json
    source.schema.json
    concept.schema.json
    system.schema.json
```

## How To Think About Fields

Frontmatter should earn its place. Prefer body prose unless a field is:

- required to identify the page kind,
- queried across many pages,
- used by automation or lifecycle rules,
- displayed in a real dashboard,
- an integration link that agents need to resume work.

See [Designing page kinds](../docs/designing-page-kinds.md) for probing questions and field group guidance.

