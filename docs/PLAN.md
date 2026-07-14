# Trellis Plan

## Outcome

Trellis demonstrates a schema-gated Obsidian + agent workflow pattern end to end: sample vault, sample schemas, sample gate, starter skills, and a private-to-public promotion flow.

Non-goals: publishing a private vault; replacing `vault-management`; shipping production-ready Codex/Claude hook packages; mirroring private skill repos automatically.

## Status

- **Phase:** Initial scaffold.
- **In flight:** Public-readiness polish: field-design guidance, source-capture options, and maintainer promotion flow.
- **Recently completed**:
  - 2026-07-13 — Renamed the public starter to Trellis at `ajam1097/trellis`; tagline: "Where knowledge grows into action."
  - 2026-07-08 — Published the starter as a public GitHub repo: `ajam1097/obsidian-agent`.
  - 2026-07-08 — Added page-kind/frontmatter design guidance, source-capture options, and an `idea-research` starter skill.
  - 2026-07-08 — Created initial repo scaffold and public-safe starter structure.

## Roadmap

- [ ] Initial public starter
  - [x] Create repo structure under `vault-work/obsidian-agent`
  - [x] Add README, AGENTS, architecture, and promotion-flow docs
  - [x] Add sample schemas and sample vault pages
  - [x] Add flat starter skills folder
  - [x] Verify sample audits pass
  - [x] Initialize git repo
- [ ] Public-readiness pass
  - [x] Add page-kind/frontmatter design guide
  - [x] Add source capture options
  - [x] Add idea research starter skill
  - [ ] Add privacy scan script or checklist
  - [ ] Add `CHANGELOG.md`
  - [ ] Add friend setup walkthrough
  - [x] Decide GitHub visibility and remote
- [ ] Promotion flow
  - [x] Add a maintainer checklist for promoting private skills into public starter form
  - [ ] Add examples of private-specific text rewritten into public placeholders

## Backlog

- Add a minimal CI workflow once the public remote exists.
- Add a sample valid/invalid write test using `vault-management authorize`.
- Add optional adapter notes for Claude Code and Codex hooks.

## Ideas

- A generated HTML diagram for the architecture.
- A generated worksheet version of the page-kind design questions.

## Decisions

### Open

- Whether the sample taxonomy should stay at five kinds or grow toward a fuller reference model.
- Whether to include runnable hook scripts or keep gates as documented examples only.

### Locked

- 2026-07-13 — Public name is **Trellis** at `ajam1097/trellis`; the name reflects a governed structure that helps knowledge grow into action.
- 2026-07-08 — Keep `vault-management` separate as the engine package; this repo is the starter/reference kit.
- 2026-07-08 — Keep skills in one flat `skills/` folder for the starter.

## References

- Engine package: `vault-management`
- Starter validator commands: `README.md` → Quickstart
- Promotion rules: `docs/promotion-flow.md`
