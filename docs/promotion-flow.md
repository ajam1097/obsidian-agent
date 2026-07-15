# Private To Public Promotion Flow

This is a maintainer guide for this starter repo. It belongs in the public repo because it explains how public examples stay clean, but it does **not** belong in a user's sample vault as operational knowledge.

Do not mirror private skills or schemas into the distribution automatically. Author or adapt public-specific material in My Trellis under `public/trellis/`, then publish it through the allowlist, scans, diff review, and approval digest.

## Flow

1. **Change privately first.**
   Work in My Trellis, which owns both private system modules and the intentionally public `public/trellis/` source tree.

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
   - No private paths, names, IDs, or credentials.
   - README or docs explain any new assumption.
   - `CHANGELOG.md` notes the public-facing change once a changelog exists.
   - The exhaustive public path allowlist is current.
   - Personal-content and secret scans pass over the staged tree and public history.
   - The complete staged diff and approval digest are reviewed before apply or push.

6. **Publish a generated snapshot.**
   Never commit directly in the public checkout. Use the My Trellis publisher to prepare, approve, apply, and push the exact snapshot.

## Rule Of Thumb

If the change improves the reusable pattern, promote it here.

If the change only improves one private operating system, keep it private until the reusable lesson is clear.

Inbound public fixes follow the same direction in reverse: review the proposal, back-port it into My Trellis, then republish. The public repository is never the source of truth.
