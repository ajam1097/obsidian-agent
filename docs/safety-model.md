# Safety Model

This starter uses layered safety:

1. **Read freely.**
   Agents can read the vault to gather context.

2. **Write through schemas.**
   Governed folders have schemas. Proposed writes are checked before they land.

3. **Review judgment.**
   Anything involving personal judgment, status changes, or strategy should be shown to the human before writing.

4. **Keep history.**
   Use git for the vault or sample vault so bad writes can be inspected and reverted.

5. **Start small.**
   Govern one folder first, run audits until clean, then expand.

## What Schema Validation Catches

- Missing required frontmatter.
- Invalid enum values.
- Wrong page kind for a folder.
- Deprecated fields during audits.

## What Schema Validation Does Not Catch

- Bad advice.
- Outdated prose.
- Poor prioritization.
- Private information accidentally included in a note body.
- A write path that bypasses the hook entirely.

