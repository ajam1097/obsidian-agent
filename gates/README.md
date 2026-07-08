# Gates

A gate is a harness-specific wrapper that calls:

```bash
vault-management authorize <target-path> --vault-root <vault-root> --schema-root <schema-root>
```

The engine validates the proposed final Markdown. The gate decides how to intercept a write in a specific agent tool and how to translate an `ALLOW` or `DENY` result back to that tool.

## Starter Rule

Start with audits. Add a gate only after the folder you want to govern is clean.

## Example

```bash
vault-management authorize sample-vault/efforts/ideas/Inbox Rules.md \
  --vault-root sample-vault \
  --schema-root schemas \
  < sample-vault/efforts/ideas/Inbox Rules.md
```

