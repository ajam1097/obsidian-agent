# Private To Public Promotion Flow

Do not mirror private skills or schemas into this repo automatically. Promote public updates intentionally.

## Flow

1. **Change privately first.**
   Work in the private/source repo where the workflow is real.

2. **Prove the behavior.**
   Run local validators and use the skill or schema in real work. If it touches vault writes, prove it through the private gate first.

3. **Classify the change.**
   - Private-only: depends on personal paths, accounts, relationships, task IDs, or local tooling.
   - Public-worthy: teaches a reusable workflow pattern or safety improvement.
   - Public-worthy after adaptation: useful, but needs placeholders or sample data.

4. **Adapt into starter form.**
   Replace private specifics with generic placeholders:
   - `<vault-root>`
   - `<schema-root>`
   - `<task-manager>`
   - `<agent-tool>`

5. **Check before publishing.**
   - Sample vault audits pass.
   - No private paths, names, IDs, or secrets.
   - README or docs explain any new assumption.
   - `CHANGELOG.md` notes the public-facing change once a changelog exists.

## Rule Of Thumb

If the change improves the reusable pattern, promote it here.

If the change only improves one private operating system, keep it private until the reusable lesson is clear.

